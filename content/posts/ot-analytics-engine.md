---
title: "Industrial OT Analytics Engine – Hướng Dẫn Kiến Trúc & Triển Khai Hạ Tầng"
date: 2026-11-06T17:30:00+07:00
draft: false
tags: ["Industrial OT", "Docker", "PostgreSQL", "Grafana", "Data Pipeline", "Technical Debt"]
categories: ["Flagship Architecture"]
description: "Bản thiết kế kiến trúc và hướng dẫn triển khai toàn diện hệ thống Industrial OT Analytics Engine sử dụng Docker, PostgreSQL Time-Series và Grafana Control Room dựa trên mô hình tham chiếu FAC_GLOBAL_01."
bookToc: true
---

# Industrial OT Analytics Engine – Hướng Dẫn Kiến Trúc & Triển Khai Hạ Tầng

## 1. Tổng Quan Hệ Thống & Bối Cảnh Vận Hành

Trong các môi trường sản xuất công nghiệp hiện đại, việc theo dõi thời gian dừng máy (**Downtime**), tính toán các chỉ số độ tin cậy thiết bị như **MTTR** (Mean Time to Repair - Thời gian sửa chữa trung bình), **MTBF** (Mean Time Between Failures - Thời gian trung bình giữa các sự cố) và định lượng **Điểm nợ kỹ thuật (MOP V7 Score)** thường gặp rào cản lớn do các ốc đảo dữ liệu (Data Silos) cô lập giữa cổng kết nối Edge Gateway (PLC/SCADA) và hệ thống quản trị doanh nghiệp (ERP/MES).

Tài liệu này cung cấp một kiến trúc toàn diện cho **Industrial OT Analytics Engine** — một bộ hạ tầng mô-đun hóa, triển khai nhanh bằng **1-Click Containerized** dựa trên nền tảng Docker, cơ sở dữ liệu chuỗi thời gian PostgreSQL và trung tâm giám sát trực quan Grafana Control Room.

> 🔒 **Giao thức Bảo mật NDA & Ẩn danh dữ liệu:** Tất cả các sơ đồ kiến trúc, cấu trúc SQL, mã lệnh Python và luồng dữ liệu time-series trong bài viết này được xây dựng độc quyền dựa trên **Mô hình tham chiếu tiêu chuẩn `FAC_GLOBAL_01`**. Hệ thống hoàn toàn không chứa bất kỳ nhật ký vận hành thực tế, mã thiết bị độc quyền hoặc dữ liệu sản xuất bảo mật của bất kỳ nhà máy cụ thể nào.

---

## 2. Bản Thiết Kế Hạ Tầng & Container Hóa

Hệ thống ứng dụng mô hình triển khai **1-Click Setup trên Docker**, giúp cô lập hoàn toàn các thư viện phụ thuộc và cho phép triển khai tức thì trên các máy chủ nội bộ (Local Server), thiết bị biên (Edge Devices) hoặc máy ảo đám mây (Cloud VMs).

### Ma Trận Thành Phần Tech Stack

| Dịch vụ Container | Image / Phiên bản | Chức năng vận hành | Vai trò trong Data Pipeline |
| :--- | :--- | :--- | :--- |
| **ot-database** | PostgreSQL 16 (Tối ưu hóa Time-Series) | Lưu trữ siêu dữ liệu thiết bị, log sự cố dừng máy và các chỉ số tin cậy được tính toán. | Lưu trữ dữ liệu lâu dài & Đánh chỉ mục (Index). |
| **ot-ingestion** | Python 3.12 Async Worker | Làm sạch, xác thực và chuyển đổi cấu trúc dữ liệu thô nhận từ luồng OPC-UA/MQTT. | Thu thập & Biến đổi dữ liệu (Ingestion & Transformation). |
| **ot-controlroom** | Grafana 10.x | Hiển thị các bảng điều khiển thời gian thực, biểu đồ OEE và thước đo Nợ kỹ thuật MOP V7. | Trực quan hóa & Báo cáo quản trị (Executive Reporting). |

### Cấu Hình Triển Khai (`docker-compose.yml`)

```yaml
version: '3.8'

services:
  ot-database:
    image: postgres:16-alpine
    container_name: ot_postgres_db
    restart: always
    environment:
      POSTGRES_DB: ot_analytics_db
      POSTGRES_USER: ot_admin
      POSTGRES_PASSWORD: \${POSTGRES_PASSWORD:-SecureOTPass2026!}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d

  ot-controlroom:
    image: grafana/grafana:10.2.0
    container_name: ot_grafana_dashboard
    restart: always
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=\${GRAFANA_PASSWORD:-AdminOT2026!}
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - ot-database

volumes:
  postgres_data:
  grafana_data:
```

---

## 3. Cấu Trúc Cơ Sở Dữ Liệu & Truy Vấn Phân Tích (DDL & SQL)

### 3.1 Cấu Trúc Schema DDL (PostgreSQL)

Mô hình dữ liệu được thiết kế tối ưu để ghi lại thông tin thiết bị và các sự kiện dừng máy cho mô hình tham chiếu `FAC_GLOBAL_01`.

```sql
-- Khởi tạo Enum cho Trạng thái Vận hành của Thiết bị
CREATE TYPE asset_status_enum AS ENUM ('RUNNING', 'UNPLANNED_STOP', 'PLANNED_MAINTENANCE', 'DEGRADED');

-- Bảng 1: Siêu dữ liệu cấu hình thiết bị (Equipment Master Metadata)
CREATE TABLE equipment_master (
    asset_id VARCHAR(50) PRIMARY KEY,          -- Ví dụ: 'FAC_GLOBAL_01_PACK_01'
    asset_name VARCHAR(100) NOT NULL,
    line_code VARCHAR(50) NOT NULL,            -- Ví dụ: 'LINE_ALPHA'
    design_speed_ppm INT NOT NULL,             -- Tốc độ thiết kế (sản phẩm/phút)
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Bảng 2: Nhật ký dừng máy & Nợ kỹ thuật (Downtime Events & Technical Debt Logs)
CREATE TABLE downtime_logs (
    event_id SERIAL PRIMARY KEY,
    asset_id VARCHAR(50) REFERENCES equipment_master(asset_id),
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE,
    -- Tự động tính thời gian dừng máy theo giây (Generated Column)
    duration_seconds INT GENERATED ALWAYS AS (EXTRACT(EPOCH FROM (end_time - start_time))::INT) STORED,
    stop_reason_category VARCHAR(100),          -- Ví dụ: 'ELECTRICAL_SENSOR_FAILURE'
    technical_debt_impact_score NUMERIC(5, 2),  -- Điểm MOP V7 (Từ 0.00 đến 100.00)
    status asset_status_enum DEFAULT 'UNPLANNED_STOP'
);

-- Đánh chỉ mục Index hiệu năng cao cho dữ liệu Time-Series
CREATE INDEX idx_downtime_asset_time ON downtime_logs (asset_id, start_time DESC);
CREATE INDEX idx_downtime_status ON downtime_logs (status);
```

### 3.2 Tối Ưu Hóa Truy Vấn MTTR, MTBF & Tỷ Lệ Sẵn Sàng (%) Với Materialized View

Để đảm bảo độ trễ truy vấn dưới 1 giây (sub-second) trên các Dashboard Grafana khi đối mặt với hàng triệu dòng log sự kiện, các chỉ số độ tin cậy được tổng hợp sẵn vào một **Materialized View**:

```sql
CREATE MATERIALIZED VIEW mv_equipment_reliability_30d AS
SELECT
    asset_id,
    COUNT(event_id) AS total_failure_events,
    ROUND(SUM(duration_seconds) / 3600.0, 2) AS total_downtime_hours,
    ROUND(AVG(duration_seconds) / 60.0, 2) AS mttr_minutes,
    -- Tính toán phần trăm thời gian sẵn sàng của thiết bị trong 30 ngày
    ROUND(
        (30 * 24 * 3600 - COALESCE(SUM(duration_seconds), 0)) * 100.0 / (30 * 24 * 3600), 2
    ) AS availability_percentage,
    ROUND(AVG(technical_debt_impact_score), 2) AS avg_tech_debt_mop_v7
FROM downtime_logs
WHERE start_time >= NOW() - INTERVAL '30 days'
GROUP BY asset_id;

-- Đánh chỉ mục Unique Index trên Materialized View để hỗ trợ làm mới dữ liệu nhanh
CREATE UNIQUE INDEX idx_mv_reliability_asset ON mv_equipment_reliability_30d (asset_id);
```

---

## 4. Cấu Hình Grafana Control Room Dashboard

Grafana kết nối trực tiếp đến PostgreSQL thông qua các câu lệnh SQL thuần (Native SQL). Bố cục phòng điều khiển trung tâm tích hợp 4 loại bảng hiển thị (Panel) cốt lõi:

1. **Thước đo tổng thể độ sẵn sàng (Overall Availability Gauge %):** Liên kết trực tiếp với trường `availability_percentage` từ bảng ảo `mv_equipment_reliability_30d` (Quy ước màu: Xanh lục: >95%, Vàng: 85-95%, Đỏ: <85%).
2. **Thước đo tác động nợ kỹ thuật (Technical Debt Impact Gauge - Thang MOP V7):** Hiển thị `avg_tech_debt_mop_v7` để định lượng mức độ xuống cấp tích lũy của máy móc và khối lượng công việc bảo trì tồn đọng.
3. **Top 5 nguyên nhân gốc rễ gây dừng máy (Bar Chart):** Xếp hạng `stop_reason_category` theo tổng thời gian tích lũy để làm nổi bật các tổn thất thiết bị nghiêm trọng nhất.
4. **Trục thời gian trạng thái thực (State Timeline):** Trực quan hóa các bước chuyển dịch trạng thái giữa `RUNNING`, `UNPLANNED_STOP`, và `DEGRADED` trong khung thời gian 24 giờ liên tục.

---

## 5. Tuyên Bố Miễn Trừ Trách Nhiệm & Hợp Tác B2B Bất Đồng Bộ

### ⚠️ Lưu Ý Về Bản Phác Thảo AI & Yêu Cầu Phê Duyệt Thực Địa

Kiến trúc và toàn bộ mã nguồn này được chuẩn bị với sự hỗ trợ của **Trợ lý AI (Quy trình làm việc Human-in-the-Loop - Có sự giám sát của con người)**.

* **Cung cấp nguyên trạng (As-Is):** Tất cả các script cấu hình và schema cơ sở dữ liệu được cung cấp dưới dạng "như hiện có" nhằm mục đích tham khảo kiến trúc và thử nghiệm trong môi trường Sandbox (môi trường cô lập).
* **Yêu cầu bắt buộc về chữ ký phê duyệt chuyên gia:** Bất kỳ việc triển khai mã nguồn hoặc schema này vào hệ thống PLC, SCADA hoặc CMMS đang vận hành thực tế tại nhà máy **phải được xem xét và ký phê duyệt bởi Kỹ sư trưởng Tự động hóa / Kỹ sư trưởng Bảo trì** có đủ năng lực trước khi đưa vào sản xuất.

### 🛠️ Dịch Vụ Kỹ Thuật B2B Từ Xa - Vận Hành Bất Đồng Bộ (Async-First)

Tôi cung cấp dịch vụ chuyên sâu về **Kỹ thuật hạ tầng dữ liệu OT & Phòng điều khiển trung tâm (Control Room Engineering) B2B từ xa**, hoạt động theo giao thức nghiêm ngặt **Ưu tiên bất động bộ (Không họp trực tiếp)**:

* **Kênh giao tiếp:** Trao đổi 100% bằng văn bản, tài liệu đặc tả và quản lý tác vụ qua Slack, Jira, GitHub, hoặc Email bằng tiếng Anh kỹ thuật chuyên nghiệp (B2 Technical English).
* **Không cung cấp dịch vụ trực tiếp tại hiện trường:** Cắt giảm hoàn toàn các chi phí họp hành hội nghị và khảo sát thực địa, đảm bảo tập trung tối đa hiệu suất cho công việc kỹ thuật cốt lõi.

Để gửi yêu cầu kỹ thuật hoặc đặt hàng thiết kế Data Pipeline tùy chỉnh, vui lòng sử dụng *Biểu mẫu Sàng lọc Kỹ thuật* tại trang Liên hệ hoặc tạo một Ticket yêu cầu thông số kỹ thuật.
