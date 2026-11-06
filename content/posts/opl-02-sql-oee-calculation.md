---
title: "OPL #02: Viết câu lệnh SQL tính hiệu suất thiết bị tổng thể (OEE) theo ca từ dữ liệu PLC"
date: 2026-11-06
draft: false
description: "Hướng dẫn viết câu lệnh SQL (PostgreSQL) kết hợp dữ liệu log trạng thái máy và sản lượng từ PLC để tự động hóa báo cáo OEE theo ca sản xuất."
tags: ["OPL", "SQL", "OEE", "OT Data Analytics", "PostgreSQL"]
---

## 1. Bài toán Thực tế trong Nhà máy
Thay vì để đội vận hành ghi chép tay sản lượng, thời gian dừng máy vào Excel cuối mỗi ca, hệ thống SCADA/Historian hoàn toàn có thể tự động tính toán **OEE (Overall Equipment Effectiveness)**. 

Bài học 1 điểm này hướng dẫn cách viết một câu lệnh SQL chuẩn hóa để tính toán OEE từ hai bảng dữ liệu gốc đẩy từ PLC lên Database: `machine_runtime_logs` (nhật ký trạng thái) và `production_counters` (sản lượng đếm).

## 2. Cấu trúc Bảng dữ liệu đầu vào (Schema)

* **Bảng `machine_runtime_logs`**: Lưu thời gian máy chạy/dừng.
  * `shift_date`: Ngày làm việc.
  * `shift_name`: Tên ca (`Ca 1`, `Ca 2`, `Ca 3`).
  * `planned_production_time`: Thời gian lên kế hoạch sản xuất (Giờ).
  * `actual_run_time`: Thời gian máy chạy thực tế (Giờ).
* **Bảng `production_counters`**: Lưu sản lượng.
  * `total_pieces`: Tổng sản lượng máy làm ra (Bao gồm cả hàng lỗi).
  * `good_pieces`: Sản lượng sản phẩm đạt chất lượng tiêu chuẩn.
  * `ideal_cycle_time_seconds`: Thời gian lý tưởng để làm ra 1 sản phẩm (Giây).

## 3. Câu lệnh SQL tính toán OEE tự động (PostgreSQL)

Đoạn mã dưới đây sử dụng kỹ thuật **Common Table Expression (CTE)** để tính toán riêng lẻ 3 chỉ số thành phần trước khi nhân lại ra OEE cuối cùng:

```sql
WITH Raw_Metrics AS (
    SELECT 
        r.shift_date,
        r.shift_name,
        -- 1. Tính Availability (Mức độ sẵn sàng)
        (r.actual_run_time / r.planned_production_time) AS availability,
        
        -- 2. Tính Performance (Hiệu suất vận hành)
        ((p.total_pieces * (p.ideal_cycle_time_seconds / 3600.0)) / r.actual_run_time) AS performance,
        
        -- 3. Tính Quality (Chất lượng sản phẩm)
        (p.good_pieces::float / NULLIF(p.total_pieces, 0)) AS quality
    FROM machine_runtime_logs r
    JOIN production_counters p 
      ON r.shift_date = p.shift_date AND r.shift_name = p.shift_name
)
SELECT 
    shift_date AS "Ngày",
    shift_name AS "Ca Làm Việc",
    ROUND((availability * 100)::numeric, 2) AS "Availability (%)",
    ROUND((performance * 100)::numeric, 2) AS "Performance (%)",
    ROUND((quality * 100)::numeric, 2) AS "Quality (%)",
    -- Công thức gốc OEE = A x P x Q
    ROUND((availability * performance * quality * 100)::numeric, 2) AS "OEE tổng thể (%)"
FROM Raw_Metrics
ORDER BY shift_date DESC, shift_name ASC;
```

## 4. Giải thích thuật toán chuyên sâu cho kỹ sư OT
* **Hàm `NULLIF(p.total_pieces, 0)`**: Rất quan trọng để phòng ngừa lỗi chia cho 0 (`division by zero`) trong trường hợp ca làm việc đó máy bị dừng hoàn toàn ngay từ đầu ca và không sản xuất được sản phẩm nào.
* **Quy đổi thời gian lý tưởng**: Do `ideal_cycle_time_seconds` tính bằng giây, ta chia cho `3600.0` để đồng bộ về đơn vị **Giờ** giống như biến thời gian chạy máy `actual_run_time`.

## 5. Trực quan hóa trên Grafana Dashboard
Khi đưa câu lệnh này vào Grafana, bạn hãy cấu hình Panel dạng **Bar Gauge** hoặc **Stat** với các vùng ngưỡng (Thresholds) tiêu chuẩn quốc tế:
* 🟢 **World Class OEE (Xanh)**: $\ge$ 85%
* 🟡 **Acceptable (Vàng)**: 65% - 84% (Mức chấp nhận được nhưng cần cải tiến)
* 🔴 **Low Performance (Đỏ)**: < 65% (Dấu hiệu nghẽn dây chuyền hoặc dừng máy quá nhiều)
