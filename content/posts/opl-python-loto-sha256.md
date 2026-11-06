---
# --- CẤU HÌNH HIỂN THỊ (HUGO BOOK THEME) ---
title: "OPL #02: Python Script xác thực SHA-256 Hash cho LOTO JSON Payload"
date: 2026-11-07T00:00:00+07:00
draft: false
bookToC: true               # Bật Mục lục tự động bên phải bài viết
bookSearchExclude: false    # Cho phép thanh tìm kiếm nội bộ quét bài viết này
weight: 20                  # Đứng sau bài OPL #01 trên Sidebar

# --- CẤU HÌNH TỐI ƯU HÓA SEO ---
description: "Hướng dẫn bài học 1 điểm (OPL) về viết script Python tạo và đối soát mã băm Cryptographic SHA-256 cho LOTO JSON Payload nhằm chống biến đổi dữ liệu quy trình an toàn."

# --- ĐỊNH DANH & PHÂN LOẠI NỘI DUNG ---
categories: ["Industrial OT Safety"]
tags: ["OPL", "Python", "LOTO", "SHA-256", "OSHA 1910.147", "OT Safety"]
---

## 1. Mục tiêu Bài học 1 điểm (OPL)

Trong hệ thống tự động hóa an toàn công nghiệp và quản trị bảo trì (**CMMS/EAM**), việc truyền tải dữ liệu quy trình LOTO (Lockout/Tagout) qua hệ thống API đòi hỏi cơ chế **Xác thực tính toàn vẹn (Zero-Tampering Verification)** để đảm bảo an toàn tuyệt đối cho kỹ sư thực địa.

Bài học 1 điểm này hướng dẫn kỹ thuật:
*   Đóng gói quy trình LOTO dưới dạng một cấu trúc **JSON Payload chuẩn hóa**.
*   Xây dựng thuật toán **Python Cryptographic SHA-256** để tạo mã băm độc bản 64 ký tự hex.
*   Tự động phát hiện và phát cảnh báo nếu có bất kỳ hành vi thay đổi dữ liệu trái phép nào trên tài liệu thực địa. 

***

## 2. Đoạn Mã Nguồn Python Chuẩn Hóa (Production-Ready Script)

Script Python dưới đây thực hiện mã hóa băm SHA-256 & giả lập thử nghiệm cơ chế đối soát tự động khi cấu trúc Payload bị can thiệp thay đổi thông số:

```python
import hashlib
import json
import copy

def calculate_loto_payload_sha256(payload: dict) -> str:
    """
    Tính toán mã băm SHA-256 độc bản cho LOTO JSON Payload.
    Sử dụng sort_keys=True để đảm bảo thứ tự key nhất quán tuyệt đối.
    """
    # Chuẩn hóa chuỗi JSON (sắp xếp key và định dạng mã hóa UTF-8)
    serialized_json = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    
    # Tạo mã băm SHA-256
    sha256_hash = hashlib.sha256(serialized_json.encode('utf-8')).hexdigest()
    return sha256_hash

def verify_payload_integrity(original_hash: str, current_payload: dict) -> bool:
    """
    Đối soát mã băm hiện tại thực tế với mã băm gốc được lưu giữ trên hệ thống.
    """
    current_hash = calculate_loto_payload_sha256(current_payload)
    return current_hash == original_hash

# ----------------------------------------------------------------------
# DỮ LIỆU THỬ NGHIỆM: Payload LOTO Máy bơm ly tâm PUMP-201A
# ----------------------------------------------------------------------
loto_payload_original = {
    "sop_id": "LOTO-PUMP-201A-V1",
    "standard": "OSHA 29 CFR 1910.147",
    "asset_id": "FAC_GLOBAL_01_PUMP_201A",
    "isolation_steps": [
        {
            "step": 1,
            "energy_type": "Electrical 380V AC",
            "point": "MCC-01 CB-12",
            "action_vi": "Ngắt CB-12 tại tủ MCC-01 và khóa Lockout",
            "verification": "Test Zero Voltage with VOM (0V AC)"
        },
        {
            "step": 2,
            "energy_type": "Fluid Pressure",
            "point": "Suction Valve V-101 & Discharge Valve V-102",
            "action_vi": "Đóng van hút V-101 và van xả V-102, xả áp dư",
            "verification": "Check Pressure Gauge PG-201 reading 0 Bar"
        }
    ]
}

# --- KỊCH BẢN KIỂM THỬ HỆ THỐNG ---

# 1. Tính toán mã băm SHA-256 gốc khi xuất bản quy trình
original_sha256 = calculate_loto_payload_sha256(loto_payload_original)
print(f"🟢 Original SHA-256 Hash: {original_sha256}")

# 2. Kiểm chứng Payload nguyên bản tại thực địa trước ca làm việc
is_valid_original = verify_payload_integrity(original_sha256, loto_payload_original)
print(f"✓ Trạng thái đối soát Payload gốc: {is_valid_original} (Hợp lệ)")

# 3. Giả lập hành vi can thiệp trái phép (Sửa đổi giá trị điện áp kiểm tra từ 0V thành 220V)
loto_payload_tampered = copy.deepcopy(loto_payload_original)
loto_payload_tampered["isolation_steps"][0]["verification"] = "Test Zero Voltage with VOM (220V AC)"

tampered_sha256 = calculate_loto_payload_sha256(loto_payload_tampered)
is_valid_tampered = verify_payload_integrity(original_sha256, loto_payload_tampered)

print(f"\n🔴 Tampered SHA-256 Hash : {tampered_sha256}")
print(f"✗ Trạng thái đối soát Payload bị sửa: {is_valid_tampered} (CẢNH BÁO VI PHẠM!)")
```
