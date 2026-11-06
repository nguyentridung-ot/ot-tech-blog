---
title: "OPL #01: Cấu hình Grafana Control Room Dashboard kết nối PostgreSQL Query Time-Series"
date: 2026-11-05
draft: false
description: "Hướng dẫn nhanh 1 điểm (OPL) về cách viết câu lệnh SQL truy vấn thời gian dừng máy (Downtime Events) để vẽ biểu đồ MTTR trên Grafana."
tags: ["OPL", "Grafana", "PostgreSQL", "SMRP", "OT Analytics"]
---

## 1. Mục tiêu Bài học 1 điểm (OPL)
Chuẩn hóa câu lệnh SQL truy vấn dữ liệu chuỗi thời gian (*Time-series Query*) từ PostgreSQL để trực quan hóa chỉ số **MTTR (Mean Time to Repair)** theo tuần trên Grafana Control Room Dashboard.

## 2. Truy vấn SQL Chuẩn hóa (PostgreSQL Time-Series Query)

```sql
-- Truy vấn tính MTTR trung bình theo từng tuần
SELECT
  \$__timeGroupAlias(start_time, 1w),
  AVG(EXTRACT(EPOCH FROM (end_time - start_time))/3600) AS "MTTR (Hours)",
  COUNT(event_id) AS "Total Failures"
FROM downtime_events
WHERE
  category = 'Unplanned Breakdown'
  AND \$__timeFilter(start_time)
GROUP BY 1
ORDER BY 1 ASC;
```

## 3. Cấu hình Panel trên Grafana
1. **Data Source**: Chọn PostgreSQL Database.
2. **Panel Type**: Time Series.
3. **Threshold Cảnh báo**:
   - 🟢 **An toàn (Green)**: MTTR < 1.0 giờ.
   - 🟡 **Cảnh báo (Yellow)**: 1.0 giờ ≤ MTTR ≤ 2.5 giờ.
   - 🔴 **Nợ kỹ thuật cao (Red)**: MTTR > 2.5 giờ.
