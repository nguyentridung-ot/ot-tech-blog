---
title: "LOTO-ELEC-01: Variable Frequency Drive (VFD) & Motor Control Center (MCC) Isolation SOP"
sop_id: "LOTO-ELEC-01"
standard: "OSHA 29 CFR 1910.147"
equipment_group: "Electrical & Automation"
facility_reference: "FAC_GLOBAL_01"
author: "Nguyen Tri Dung (Industrial OT Authority)"
date: 2026-11-13
sha256_checksum: "da79d4cb758467bc468c5de458c3ad50b2c7d873862ea8590752ce872f5e6a54"
tags: ["Safety", "LOTO", "Electrical", "Automation", "OSHA", "SHA-256", "SAP-PM", "IBM-Maximo"]
---

# LOTO-ELEC-01: Variable Frequency Drive (VFD) & Motor Control Center (MCC) Isolation SOP
### (Quy trình Cô lập Biến tần (VFD) & Tủ động lực (MCC))

> **🔒 NDA & Reference Model Notice:** All equipment identifiers, breaker codes, and location tags in this Standard Operating Procedure are defined under the **Standard Reference Model (`FAC_GLOBAL_01`)**. No proprietary factory data or actual operational plant logs are exposed.
> 
> **🛡️ Cryptographic Verification Watermark:** 
> **SHA-256 Digest:** `da79d4cb758467bc468c5de458c3ad50b2c7d873862ea8590752ce872f5e6a54`

---

## 1. System Scope & Energy Control Overview

This Standard Operating Procedure (SOP) defines the mandatory **6-Step Hazardous Energy Control Protocol** required under **OSHA 29 CFR 1910.147** prior to performing maintenance, servicing, or technical intervention on **Industrial VFD (Danfoss/Siemens/ABB) & MCC 400VAC Motor Breakers**.

* **Target System / Equipment:** Industrial VFD (Danfoss/Siemens/ABB) & MCC 400VAC Motor Breakers (Biến tần công nghiệp VFD & Tủ ngắt nguồn động cơ MCC 400VAC)
* **Regulatory Compliance Standard:** OSHA 29 CFR 1910.147 (Control of Hazardous Energy)
* **Hazardous Energy Types Present:** 400VAC 3-Phase Electrical, DC Bus Capacitor Residual Energy (500-800VDC)
* **Verification Protocol:** STAR Method (Stop - Test - Actuate - Read)

---

## 2. Bilingual 6-Step Energy Isolation Matrix

The matrix below details the exact step-by-step physical actions required to achieve a verified **Zero Energy State (ZES)**.

| Step # | Phase Name (EN / VI) | Location & Isolation Point | Required Action (English) | Thao Tác Bắt Buộc (Tiếng Việt) | Verification Method / STAR Protocol |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Notification & Prep**<br>*( Thông báo & Chuẩn bị )* | `All Energy Points (MCC & VFD)` | Notify line operators. Locate MCC Breaker MCC-Q01 and VFD Drive Cabinet via P&ID FAC-01-ELE-101. | Thông báo cho người vận hành khu vực. Xác định vị trí Aptomat MCC-Q01 và tủ Biến tần theo sơ đồ FAC-01-ELE-101. | Check line HMI status display: 'READY_FOR_STOP'. |
| **2** | **Machine Shutdown**<br>*( Tắt thiết bị )* | `Local HMI / Control Desk` | Execute controlled stop on local HMI. Wait for motor rotation to come to a complete standstill. | Thực hiện dừng điều khiển trên HMI cục bộ. Chờ động cơ dừng quay hoàn toàn. | Motor RPM reads exactly 0 on HMI and drive display. |
| **3** | **Equipment Isolation**<br>*( Cách ly năng lượng )* | `MCC Panel Bay 02` | Switch MCC-Q01 main disconnect switch to OFF position (rotate 90 degrees counter-clockwise). | Bật công tắc ngắt nguồn chính MCC-Q01 về vị trí OFF (xoay 90 độ ngược chiều kim đồng hồ). | Mechanical position indicator on switch points clearly to 'OFF'. |
| **4** | **LOTO Application**<br>*( Gắn khóa & Biển báo )* | `MCC-Q01 Switch Handle` | Apply lockout hasp and personal red padlock with Danger Tag TAG-ELE-01 on MCC-Q01 switch handle. | Móc gá khóa chùm và khóa cá nhân màu đỏ kèm Thẻ cảnh báo TAG-ELE-01 lên tay nắm công tắc MCC-Q01. | Physical pull test: ensure switch handle cannot be rotated to ON. |
| **5** | **Energy Dissipation**<br>*( Xả năng lượng dư )* | `VFD Internal DC Bus` | Wait MANDATORY 5 MINUTES for VFD internal DC bus bleeder resistors to discharge capacitors below 50VDC. | BẮT BUỘC CHỜ 5 PHÚT để điện trở xả nội bộ của VFD xả điện áp bus DC xuống dưới 50VDC. | VFD keypad LED display turns completely OFF; DC Bus LED unlit. |
| **6** | **Zero Energy Test**<br>*( Kiểm tra Năng lượng 0 )* | `VFD Power Terminals L1/L2/L3 & (+)/(-)` | STAR Protocol: Measure AC voltage (L1-L2, L2-L3, L3-L1) < 50VAC and DC Bus (+/-) < 50VDC using calibrated CAT IV multimeter. | Quy tắc STAR: Dùng đồng hồ CAT IV đo điện áp AC (L1-L2, L2-L3, L3-L1) < 50VAC và DC Bus (+/-) < 50VDC. | Multimeter confirms ZERO ENERGY (<50V). Press Local Start button; machine remains inert. |


---

## 3. CMMS Payload (SAP PM / IBM Maximo API Ready)

The canonical JSON structure below is fully formatted for automated ingestion into **SAP PM (Plant Maintenance)** or **IBM Maximo Asset Management** REST/OData API endpoints. It carries an embedded `sha256_checksum` watermark to guarantee payload integrity.

```json
{
  "sop_id": "LOTO-ELEC-01",
  "title_en": "Variable Frequency Drive (VFD) & Motor Control Center (MCC) Isolation SOP",
  "title_vi": "Quy trình Cô lập Biến tần (VFD) & Tủ động lực (MCC)",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "reference_facility": "FAC_GLOBAL_01",
  "equipment_group": "Electrical & Automation",
  "target_equipment_en": "Industrial VFD (Danfoss/Siemens/ABB) & MCC 400VAC Motor Breakers",
  "target_equipment_vi": "Biến tần công nghiệp VFD & Tủ ngắt nguồn động cơ MCC 400VAC",
  "energy_types_controlled": [
    "400VAC 3-Phase Electrical",
    "DC Bus Capacitor Residual Energy (500-800VDC)"
  ],
  "isolation_points": [
    {
      "point_id": "MCC-Q01",
      "type": "ELECTRICAL_AC",
      "rating": "400VAC / 250A",
      "location": "PANEL_MCC_01_BAY_02"
    },
    {
      "point_id": "VFD-DC-BUS",
      "type": "STORED_DC_CAPACITOR",
      "rating": "750VDC Residual",
      "location": "VFD_CABINET_DRIVE_01"
    }
  ],
  "control_sequence_steps": [
    {
      "step_number": 1,
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "location": "All Energy Points (MCC & VFD)",
      "action_en": "Notify line operators. Locate MCC Breaker MCC-Q01 and VFD Drive Cabinet via P&ID FAC-01-ELE-101.",
      "action_vi": "Thông báo cho người vận hành khu vực. Xác định vị trí Aptomat MCC-Q01 và tủ Biến tần theo sơ đồ FAC-01-ELE-101.",
      "verification_star": "Check line HMI status display: 'READY_FOR_STOP'."
    },
    {
      "step_number": 2,
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "location": "Local HMI / Control Desk",
      "action_en": "Execute controlled stop on local HMI. Wait for motor rotation to come to a complete standstill.",
      "action_vi": "Thực hiện dừng điều khiển trên HMI cục bộ. Chờ động cơ dừng quay hoàn toàn.",
      "verification_star": "Motor RPM reads exactly 0 on HMI and drive display."
    },
    {
      "step_number": 3,
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "location": "MCC Panel Bay 02",
      "action_en": "Switch MCC-Q01 main disconnect switch to OFF position (rotate 90 degrees counter-clockwise).",
      "action_vi": "Bật công tắc ngắt nguồn chính MCC-Q01 về vị trí OFF (xoay 90 độ ngược chiều kim đồng hồ).",
      "verification_star": "Mechanical position indicator on switch points clearly to 'OFF'."
    },
    {
      "step_number": 4,
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "location": "MCC-Q01 Switch Handle",
      "action_en": "Apply lockout hasp and personal red padlock with Danger Tag TAG-ELE-01 on MCC-Q01 switch handle.",
      "action_vi": "Móc gá khóa chùm và khóa cá nhân màu đỏ kèm Thẻ cảnh báo TAG-ELE-01 lên tay nắm công tắc MCC-Q01.",
      "verification_star": "Physical pull test: ensure switch handle cannot be rotated to ON."
    },
    {
      "step_number": 5,
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "location": "VFD Internal DC Bus",
      "action_en": "Wait MANDATORY 5 MINUTES for VFD internal DC bus bleeder resistors to discharge capacitors below 50VDC.",
      "action_vi": "BẮT BUỘC CHỜ 5 PHÚT để điện trở xả nội bộ của VFD xả điện áp bus DC xuống dưới 50VDC.",
      "verification_star": "VFD keypad LED display turns completely OFF; DC Bus LED unlit."
    },
    {
      "step_number": 6,
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "location": "VFD Power Terminals L1/L2/L3 & (+)/(-)",
      "action_en": "STAR Protocol: Measure AC voltage (L1-L2, L2-L3, L3-L1) < 50VAC and DC Bus (+/-) < 50VDC using calibrated CAT IV multimeter.",
      "action_vi": "Quy tắc STAR: Dùng đồng hồ CAT IV đo điện áp AC (L1-L2, L2-L3, L3-L1) < 50VAC và DC Bus (+/-) < 50VDC.",
      "verification_star": "Multimeter confirms ZERO ENERGY (<50V). Press Local Start button; machine remains inert."
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
  "sha256_checksum": "da79d4cb758467bc468c5de458c3ad50b2c7d873862ea8590752ce872f5e6a54"
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
      "action_en": "Notify line operators. Locate MCC Breaker MCC-Q01 and VFD Drive Cabinet via P&ID FAC-01-ELE-101.",
      "action_vi": "Thông báo cho người vận hành khu vực. Xác định vị trí Aptomat MCC-Q01 và tủ Biến tần theo sơ đồ FAC-01-ELE-101.",
      "location": "All Energy Points (MCC & VFD)",
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "step_number": 1,
      "verification_star": "Check line HMI status display: 'READY_FOR_STOP'."
    },
    {
      "action_en": "Execute controlled stop on local HMI. Wait for motor rotation to come to a complete standstill.",
      "action_vi": "Thực hiện dừng điều khiển trên HMI cục bộ. Chờ động cơ dừng quay hoàn toàn.",
      "location": "Local HMI / Control Desk",
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "step_number": 2,
      "verification_star": "Motor RPM reads exactly 0 on HMI and drive display."
    },
    {
      "action_en": "Switch MCC-Q01 main disconnect switch to OFF position (rotate 90 degrees counter-clockwise).",
      "action_vi": "Bật công tắc ngắt nguồn chính MCC-Q01 về vị trí OFF (xoay 90 độ ngược chiều kim đồng hồ).",
      "location": "MCC Panel Bay 02",
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "step_number": 3,
      "verification_star": "Mechanical position indicator on switch points clearly to 'OFF'."
    },
    {
      "action_en": "Apply lockout hasp and personal red padlock with Danger Tag TAG-ELE-01 on MCC-Q01 switch handle.",
      "action_vi": "Móc gá khóa chùm và khóa cá nhân màu đỏ kèm Thẻ cảnh báo TAG-ELE-01 lên tay nắm công tắc MCC-Q01.",
      "location": "MCC-Q01 Switch Handle",
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "step_number": 4,
      "verification_star": "Physical pull test: ensure switch handle cannot be rotated to ON."
    },
    {
      "action_en": "Wait MANDATORY 5 MINUTES for VFD internal DC bus bleeder resistors to discharge capacitors below 50VDC.",
      "action_vi": "BẮT BUỘC CHỜ 5 PHÚT để điện trở xả nội bộ của VFD xả điện áp bus DC xuống dưới 50VDC.",
      "location": "VFD Internal DC Bus",
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "step_number": 5,
      "verification_star": "VFD keypad LED display turns completely OFF; DC Bus LED unlit."
    },
    {
      "action_en": "STAR Protocol: Measure AC voltage (L1-L2, L2-L3, L3-L1) < 50VAC and DC Bus (+/-) < 50VDC using calibrated CAT IV multimeter.",
      "action_vi": "Quy tắc STAR: Dùng đồng hồ CAT IV đo điện áp AC (L1-L2, L2-L3, L3-L1) < 50VAC và DC Bus (+/-) < 50VDC.",
      "location": "VFD Power Terminals L1/L2/L3 & (+)/(-)",
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "step_number": 6,
      "verification_star": "Multimeter confirms ZERO ENERGY (<50V). Press Local Start button; machine remains inert."
    }
  ],
  "energy_types_controlled": [
    "400VAC 3-Phase Electrical",
    "DC Bus Capacitor Residual Energy (500-800VDC)"
  ],
  "equipment_group": "Electrical & Automation",
  "isolation_points": [
    {
      "location": "PANEL_MCC_01_BAY_02",
      "point_id": "MCC-Q01",
      "rating": "400VAC / 250A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "VFD_CABINET_DRIVE_01",
      "point_id": "VFD-DC-BUS",
      "rating": "750VDC Residual",
      "type": "STORED_DC_CAPACITOR"
    }
  ],
  "reference_facility": "FAC_GLOBAL_01",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "sop_id": "LOTO-ELEC-01",
  "target_equipment_en": "Industrial VFD (Danfoss/Siemens/ABB) & MCC 400VAC Motor Breakers",
  "target_equipment_vi": "Biến tần công nghiệp VFD & Tủ ngắt nguồn động cơ MCC 400VAC",
  "title_en": "Variable Frequency Drive (VFD) & Motor Control Center (MCC) Isolation SOP",
  "title_vi": "Quy trình Cô lập Biến tần (VFD) & Tủ động lực (MCC)"
}

# Re-compute SHA-256 Hash
computed_hash = hashlib.sha256(
    json.dumps(payload_data, sort_keys=True, ensure_ascii=False).encode('utf-8')
).hexdigest()

expected_hash = "da79d4cb758467bc468c5de458c3ad50b2c7d873862ea8590752ce872f5e6a54"

print("=" * 70)
print("CMMS LOTO SOP INTEGRITY AUDIT")
print("=" * 70)
print(f"SOP ID:        LOTO-ELEC-01")
print(f"Expected Hash: {expected_hash}")
print(f"Computed Hash: {computed_hash}")
print(f"Match Result:  {computed_hash == expected_hash}")
print("=" * 70)
```

---
*Document produced as part of the Digital IP Assets Collection for One-Person Digital Enterprise.*
