---
title: "LOTO-ELEC-03: Industrial Capacitor Bank & Uninterruptible Power Supply (UPS) Residual Energy Discharge SOP"
sop_id: "LOTO-ELEC-03"
standard: "OSHA 29 CFR 1910.147"
equipment_group: "Electrical & Automation"
facility_reference: "FAC_GLOBAL_01"
author: "Nguyen Tri Dung (Industrial OT Authority)"
date: 2026-11-13
sha256_checksum: "29fc12270877043f8b61d690b24e82f1780742afdb5a96cd88915a40ceae0c6b"
tags: ["Safety", "LOTO", "Electrical", "Automation", "OSHA", "SHA-256", "SAP-PM", "IBM-Maximo"]
---

# LOTO-ELEC-03: Industrial Capacitor Bank & Uninterruptible Power Supply (UPS) Residual Energy Discharge SOP
### (Quy trình Xả điện áp dư & Cô lập Bộ tích điện (Capacitor Bank & UPS))

> **🔒 NDA & Reference Model Notice:** All equipment identifiers, breaker codes, and location tags in this Standard Operating Procedure are defined under the **Standard Reference Model (`FAC_GLOBAL_01`)**. No proprietary factory data or actual operational plant logs are exposed.
> 
> **🛡️ Cryptographic Verification Watermark:** 
> **SHA-256 Digest:** `29fc12270877043f8b61d690b24e82f1780742afdb5a96cd88915a40ceae0c6b`

---

## 1. System Scope & Energy Control Overview

This Standard Operating Procedure (SOP) defines the mandatory **6-Step Hazardous Energy Control Protocol** required under **OSHA 29 CFR 1910.147** prior to performing maintenance, servicing, or technical intervention on **400V Power Factor Correction Capacitor Bank (300 kVAR) & 100kVA Industrial On-line UPS**.

* **Target System / Equipment:** 400V Power Factor Correction Capacitor Bank (300 kVAR) & 100kVA Industrial On-line UPS (Tủ tụ bù công suất phản kháng 400V (300 kVAR) & Hệ thống nguồn điện liên tục UPS 100kVA)
* **Regulatory Compliance Standard:** OSHA 29 CFR 1910.147 (Control of Hazardous Energy)
* **Hazardous Energy Types Present:** 400VAC 3-Phase Main Power, High Voltage Stored Capacitive Charge (Up to 690V Peak), 384VDC UPS Battery Bank Energy
* **Verification Protocol:** STAR Method (Stop - Test - Actuate - Read)

---

## 2. Bilingual 6-Step Energy Isolation Matrix

The matrix below details the exact step-by-step physical actions required to achieve a verified **Zero Energy State (ZES)**.

| Step # | Phase Name (EN / VI) | Location & Isolation Point | Required Action (English) | Thao Tác Bắt Buộc (Tiếng Việt) | Verification Method / STAR Protocol |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Notification & Prep**<br>*( Thông báo & Chuẩn bị )* | `Substation Control Room` | Notify plant electrical engineer. Review single-line diagram SLD-FAC01-POW-003 and gear up with Arc Flash PPE Category 3. | Thông báo cho kỹ sư điện nhà máy. Kiểm tra sơ đồ đơn tuyến SLD-FAC01-POW-003 và trang bị PPE chống hồ quang cấp 3. | PPE Level 3 donned (Arc flash suit, face shield, 10kV insulated gloves). |
| **2** | **Machine Shutdown**<br>*( Tắt thiết bị )* | `PFC Controller & UPS Touchscreen` | Turn OFF PFC Automatic Step Controller. Transfer UPS to Static Maintenance Bypass mode then command Inverter Shutdown. | Tắt Bộ điều khiển tự động tủ tụ bù. Chuyển UPS sang chế độ Maintenance Bypass rồi thực hiện Tắt Inverter. | PFC steps display 0 steps active. UPS display shows 'INVERTER_OFF / BYPASS_ACTIVE'. |
| **3** | **Equipment Isolation**<br>*( Cách ly năng lượng )* | `Main Distribution Panel & Battery Room` | Open Main PFC Breaker PFC-Q01. Open Main Battery Isolator UPS-BAT-CB and UPS Output Breaker. | Ngắt MCCB tổng tủ tụ bù PFC-Q01. Ngắt Aptomat Ắc-quy tổng UPS-BAT-CB và CB đầu ra UPS. | Breakers PFC-Q01 and UPS-BAT-CB visually in 'TRIPPED/OFF' state. |
| **4** | **LOTO Application**<br>*( Gắn khóa & Biển báo )* | `PFC-Q01 and UPS-BAT-CB Breaker Locks` | Apply heavy-duty circuit breaker lockouts and padlocks with Tag TAG-CAP-03 on PFC-Q01 and UPS-BAT-CB. | Gắn khóa CB chuyên dụng và ổ khóa kèm Thẻ TAG-CAP-03 lên PFC-Q01 và UPS-BAT-CB. | Verify physical locking mechanism prevents breaker re-closure. |
| **5** | **Energy Dissipation**<br>*( Xả năng lượng dư )* | `Capacitor Discharge Resistors & Earthing Rod` | Wait MANDATORY 10 MINUTES for internal discharge resistors. Then attach 10kV Grounding/Earthing Rod across capacitor terminals to earth. | CHỜ BẮT BUỘC 10 PHÚT để điện trở xả nội bộ hoạt động. Sau đó dùng Sào tiếp địa 10kV nối ngắn mạch cực tụ xuống đất. | Earthing rod connected solidly; zero spark discharge observed. |
| **6** | **Zero Energy Test**<br>*( Kiểm tra Năng lượng 0 )* | `Capacitor Terminals & UPS Battery Bus` | STAR Protocol: Measure residual DC voltage across capacitor steps (<5VDC) and across UPS battery terminals (<12VDC). | Quy tắc STAR: Đo điện áp DC dư giữa các cực tụ (<5VDC) và tại cọc tổng ắc-quy UPS (<12VDC). | All voltage measurements confirm safe Zero Energy State (<5VDC). |


---

## 3. CMMS Payload (SAP PM / IBM Maximo API Ready)

The canonical JSON structure below is fully formatted for automated ingestion into **SAP PM (Plant Maintenance)** or **IBM Maximo Asset Management** REST/OData API endpoints. It carries an embedded `sha256_checksum` watermark to guarantee payload integrity.

```json
{
  "sop_id": "LOTO-ELEC-03",
  "title_en": "Industrial Capacitor Bank & Uninterruptible Power Supply (UPS) Residual Energy Discharge SOP",
  "title_vi": "Quy trình Xả điện áp dư & Cô lập Bộ tích điện (Capacitor Bank & UPS)",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "reference_facility": "FAC_GLOBAL_01",
  "equipment_group": "Electrical & Automation",
  "target_equipment_en": "400V Power Factor Correction Capacitor Bank (300 kVAR) & 100kVA Industrial On-line UPS",
  "target_equipment_vi": "Tủ tụ bù công suất phản kháng 400V (300 kVAR) & Hệ thống nguồn điện liên tục UPS 100kVA",
  "energy_types_controlled": [
    "400VAC 3-Phase Main Power",
    "High Voltage Stored Capacitive Charge (Up to 690V Peak)",
    "384VDC UPS Battery Bank Energy"
  ],
  "isolation_points": [
    {
      "point_id": "PFC-Q01",
      "type": "ELECTRICAL_AC",
      "rating": "400VAC / 630A",
      "location": "MAIN_DISTRIBUTION_PANEL_01"
    },
    {
      "point_id": "UPS-BAT-CB",
      "type": "BATTERY_DC",
      "rating": "384VDC / 300A",
      "location": "UPS_BATTERY_RACK_ROOM"
    },
    {
      "point_id": "UPS-BYPASS",
      "type": "MAINTENANCE_BYPASS",
      "rating": "400VAC / 200A",
      "location": "UPS_MAIN_PANEL"
    }
  ],
  "control_sequence_steps": [
    {
      "step_number": 1,
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "location": "Substation Control Room",
      "action_en": "Notify plant electrical engineer. Review single-line diagram SLD-FAC01-POW-003 and gear up with Arc Flash PPE Category 3.",
      "action_vi": "Thông báo cho kỹ sư điện nhà máy. Kiểm tra sơ đồ đơn tuyến SLD-FAC01-POW-003 và trang bị PPE chống hồ quang cấp 3.",
      "verification_star": "PPE Level 3 donned (Arc flash suit, face shield, 10kV insulated gloves)."
    },
    {
      "step_number": 2,
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "location": "PFC Controller & UPS Touchscreen",
      "action_en": "Turn OFF PFC Automatic Step Controller. Transfer UPS to Static Maintenance Bypass mode then command Inverter Shutdown.",
      "action_vi": "Tắt Bộ điều khiển tự động tủ tụ bù. Chuyển UPS sang chế độ Maintenance Bypass rồi thực hiện Tắt Inverter.",
      "verification_star": "PFC steps display 0 steps active. UPS display shows 'INVERTER_OFF / BYPASS_ACTIVE'."
    },
    {
      "step_number": 3,
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "location": "Main Distribution Panel & Battery Room",
      "action_en": "Open Main PFC Breaker PFC-Q01. Open Main Battery Isolator UPS-BAT-CB and UPS Output Breaker.",
      "action_vi": "Ngắt MCCB tổng tủ tụ bù PFC-Q01. Ngắt Aptomat Ắc-quy tổng UPS-BAT-CB và CB đầu ra UPS.",
      "verification_star": "Breakers PFC-Q01 and UPS-BAT-CB visually in 'TRIPPED/OFF' state."
    },
    {
      "step_number": 4,
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "location": "PFC-Q01 and UPS-BAT-CB Breaker Locks",
      "action_en": "Apply heavy-duty circuit breaker lockouts and padlocks with Tag TAG-CAP-03 on PFC-Q01 and UPS-BAT-CB.",
      "action_vi": "Gắn khóa CB chuyên dụng và ổ khóa kèm Thẻ TAG-CAP-03 lên PFC-Q01 và UPS-BAT-CB.",
      "verification_star": "Verify physical locking mechanism prevents breaker re-closure."
    },
    {
      "step_number": 5,
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "location": "Capacitor Discharge Resistors & Earthing Rod",
      "action_en": "Wait MANDATORY 10 MINUTES for internal discharge resistors. Then attach 10kV Grounding/Earthing Rod across capacitor terminals to earth.",
      "action_vi": "CHỜ BẮT BUỘC 10 PHÚT để điện trở xả nội bộ hoạt động. Sau đó dùng Sào tiếp địa 10kV nối ngắn mạch cực tụ xuống đất.",
      "verification_star": "Earthing rod connected solidly; zero spark discharge observed."
    },
    {
      "step_number": 6,
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "location": "Capacitor Terminals & UPS Battery Bus",
      "action_en": "STAR Protocol: Measure residual DC voltage across capacitor steps (<5VDC) and across UPS battery terminals (<12VDC).",
      "action_vi": "Quy tắc STAR: Đo điện áp DC dư giữa các cực tụ (<5VDC) và tại cọc tổng ắc-quy UPS (<12VDC).",
      "verification_star": "All voltage measurements confirm safe Zero Energy State (<5VDC)."
    }
  ],
  "author": "Nguyen Tri Dung (Industrial OT Authority)",
  "cmms_integration": {
    "target_systems": [
      "SAP PM (Plant Maintenance)",
      "IBM Maximo Asset Management"
    ],
    "permit_required": true,
    "isolation_type": "ELECTRICAL_AUTOMATION_LOCKOUT"
  },
  "sha256_checksum": "29fc12270877043f8b61d690b24e82f1780742afdb5a96cd88915a40ceae0c6b"
}
```

---

## 4. Cryptographic SHA-256 Integrity Verification

To verify that this document payload has not suffered version drift, manual tampering, or corruption during transmission to the CMMS middleware, run the following Python verification snippet:

```python
import hashlib
import json

# Target Payload JSON (Canonical Form)
payload_data = {
  "author": "Nguyen Tri Dung (Industrial OT Authority)",
  "cmms_integration": {
    "isolation_type": "ELECTRICAL_AUTOMATION_LOCKOUT",
    "permit_required": true,
    "target_systems": [
      "SAP PM (Plant Maintenance)",
      "IBM Maximo Asset Management"
    ]
  },
  "control_sequence_steps": [
    {
      "action_en": "Notify plant electrical engineer. Review single-line diagram SLD-FAC01-POW-003 and gear up with Arc Flash PPE Category 3.",
      "action_vi": "Thông báo cho kỹ sư điện nhà máy. Kiểm tra sơ đồ đơn tuyến SLD-FAC01-POW-003 và trang bị PPE chống hồ quang cấp 3.",
      "location": "Substation Control Room",
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "step_number": 1,
      "verification_star": "PPE Level 3 donned (Arc flash suit, face shield, 10kV insulated gloves)."
    },
    {
      "action_en": "Turn OFF PFC Automatic Step Controller. Transfer UPS to Static Maintenance Bypass mode then command Inverter Shutdown.",
      "action_vi": "Tắt Bộ điều khiển tự động tủ tụ bù. Chuyển UPS sang chế độ Maintenance Bypass rồi thực hiện Tắt Inverter.",
      "location": "PFC Controller & UPS Touchscreen",
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "step_number": 2,
      "verification_star": "PFC steps display 0 steps active. UPS display shows 'INVERTER_OFF / BYPASS_ACTIVE'."
    },
    {
      "action_en": "Open Main PFC Breaker PFC-Q01. Open Main Battery Isolator UPS-BAT-CB and UPS Output Breaker.",
      "action_vi": "Ngắt MCCB tổng tủ tụ bù PFC-Q01. Ngắt Aptomat Ắc-quy tổng UPS-BAT-CB và CB đầu ra UPS.",
      "location": "Main Distribution Panel & Battery Room",
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "step_number": 3,
      "verification_star": "Breakers PFC-Q01 and UPS-BAT-CB visually in 'TRIPPED/OFF' state."
    },
    {
      "action_en": "Apply heavy-duty circuit breaker lockouts and padlocks with Tag TAG-CAP-03 on PFC-Q01 and UPS-BAT-CB.",
      "action_vi": "Gắn khóa CB chuyên dụng và ổ khóa kèm Thẻ TAG-CAP-03 lên PFC-Q01 và UPS-BAT-CB.",
      "location": "PFC-Q01 and UPS-BAT-CB Breaker Locks",
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "step_number": 4,
      "verification_star": "Verify physical locking mechanism prevents breaker re-closure."
    },
    {
      "action_en": "Wait MANDATORY 10 MINUTES for internal discharge resistors. Then attach 10kV Grounding/Earthing Rod across capacitor terminals to earth.",
      "action_vi": "CHỜ BẮT BUỘC 10 PHÚT để điện trở xả nội bộ hoạt động. Sau đó dùng Sào tiếp địa 10kV nối ngắn mạch cực tụ xuống đất.",
      "location": "Capacitor Discharge Resistors & Earthing Rod",
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "step_number": 5,
      "verification_star": "Earthing rod connected solidly; zero spark discharge observed."
    },
    {
      "action_en": "STAR Protocol: Measure residual DC voltage across capacitor steps (<5VDC) and across UPS battery terminals (<12VDC).",
      "action_vi": "Quy tắc STAR: Đo điện áp DC dư giữa các cực tụ (<5VDC) và tại cọc tổng ắc-quy UPS (<12VDC).",
      "location": "Capacitor Terminals & UPS Battery Bus",
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "step_number": 6,
      "verification_star": "All voltage measurements confirm safe Zero Energy State (<5VDC)."
    }
  ],
  "energy_types_controlled": [
    "400VAC 3-Phase Main Power",
    "High Voltage Stored Capacitive Charge (Up to 690V Peak)",
    "384VDC UPS Battery Bank Energy"
  ],
  "equipment_group": "Electrical & Automation",
  "isolation_points": [
    {
      "location": "MAIN_DISTRIBUTION_PANEL_01",
      "point_id": "PFC-Q01",
      "rating": "400VAC / 630A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "UPS_BATTERY_RACK_ROOM",
      "point_id": "UPS-BAT-CB",
      "rating": "384VDC / 300A",
      "type": "BATTERY_DC"
    },
    {
      "location": "UPS_MAIN_PANEL",
      "point_id": "UPS-BYPASS",
      "rating": "400VAC / 200A",
      "type": "MAINTENANCE_BYPASS"
    }
  ],
  "reference_facility": "FAC_GLOBAL_01",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "sop_id": "LOTO-ELEC-03",
  "target_equipment_en": "400V Power Factor Correction Capacitor Bank (300 kVAR) & 100kVA Industrial On-line UPS",
  "target_equipment_vi": "Tủ tụ bù công suất phản kháng 400V (300 kVAR) & Hệ thống nguồn điện liên tục UPS 100kVA",
  "title_en": "Industrial Capacitor Bank & Uninterruptible Power Supply (UPS) Residual Energy Discharge SOP",
  "title_vi": "Quy trình Xả điện áp dư & Cô lập Bộ tích điện (Capacitor Bank & UPS)"
}

# Re-compute SHA-256 Hash
computed_hash = hashlib.sha256(
    json.dumps(payload_data, sort_keys=True, ensure_ascii=False).encode('utf-8')
).hexdigest()

expected_hash = "29fc12270877043f8b61d690b24e82f1780742afdb5a96cd88915a40ceae0c6b"

print("=" * 70)
print("CMMS LOTO SOP INTEGRITY AUDIT")
print("=" * 70)
print(f"SOP ID:        LOTO-ELEC-03")
print(f"Expected Hash: {expected_hash}")
print(f"Computed Hash: {computed_hash}")
print(f"Match Result:  {computed_hash == expected_hash}")
print("=" * 70)
```

---
*Document produced as part of the Digital IP Assets Collection for One-Person Digital Enterprise.*
