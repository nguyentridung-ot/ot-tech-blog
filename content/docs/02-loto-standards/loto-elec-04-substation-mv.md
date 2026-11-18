---
title: "LOTO-ELEC-04: Internal Substation & Medium Voltage (MV) Switchgear Isolation SOP"
sop_id: "LOTO-ELEC-04"
standard: "OSHA 29 CFR 1910.147"
equipment_group: "Electrical & Automation"
facility_reference: "FAC_GLOBAL_01"
author: "Nguyen Tri Dung (Industrial OT Authority)"
date: 2026-11-13
sha256_checksum: "f41c364dd5e0dabbfd22411b02e8bdda37b445d878076700c130046d4eca4e12"
tags: ["Safety", "LOTO", "Electrical", "Automation", "OSHA", "SHA-256", "SAP-PM", "IBM-Maximo"]
---

# LOTO-ELEC-04: Internal Substation & Medium Voltage (MV) Switchgear Isolation SOP
### (Quy trình Cô lập Trạm biến áp nội bộ & Tủ trung thế (Substation & MV Switchgear))

> **🔒 NDA & Reference Model Notice:** All equipment identifiers, breaker codes, and location tags in this Standard Operating Procedure are defined under the **Standard Reference Model (`FAC_GLOBAL_01`)**. No proprietary factory data or actual operational plant logs are exposed.
> 
> **🛡️ Cryptographic Verification Watermark:** 
> **SHA-256 Digest:** `f41c364dd5e0dabbfd22411b02e8bdda37b445d878076700c130046d4eca4e12`

---

## 1. System Scope & Energy Control Overview

This Standard Operating Procedure (SOP) defines the mandatory **6-Step Hazardous Energy Control Protocol** required under **OSHA 29 CFR 1910.147** prior to performing maintenance, servicing, or technical intervention on **22kV/0.4kV Distribution Transformer (2000kVA), Ring Main Unit (RMU) & 22kV Vacuum Circuit Breaker (VCB)**.

* **Target System / Equipment:** 22kV/0.4kV Distribution Transformer (2000kVA), Ring Main Unit (RMU) & 22kV Vacuum Circuit Breaker (VCB) (Máy biến áp phân phối 22kV/0.4kV (2000kVA), Tủ trung thế RMU & Máy cắt chân không VCB 22kV)
* **Regulatory Compliance Standard:** OSHA 29 CFR 1910.147 (Control of Hazardous Energy)
* **Hazardous Energy Types Present:** 22,000VAC Medium Voltage 3-Phase, 400VAC Low Voltage Main Busbar, 110VDC Switchgear Control & Tripping Power
* **Verification Protocol:** STAR Method (Stop - Test - Actuate - Read)

---

## 2. Bilingual 6-Step Energy Isolation Matrix

The matrix below details the exact step-by-step physical actions required to achieve a verified **Zero Energy State (ZES)**.

| Step # | Phase Name (EN / VI) | Location & Isolation Point | Required Action (English) | Thao Tác Bắt Buộc (Tiếng Việt) | Verification Method / STAR Protocol |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Notification & Prep**<br>*( Thông báo & Chuẩn bị )* | `Chief Electrical Engineer / Site Operations` | Issue High Voltage Work Permit (HV-WP). Notify plant management of planned substation shutdown. Equip 24kV Class 3 Safety Gear. | Cấp Giấy phép làm việc điện cao thế (HV-WP). Thông báo ban giám đốc về lịch cúp điện trạm. Trang bị đồ bảo hộ 24kV Class 3. | HV Work Permit signed by Plant Electrical Authority. |
| **2** | **Machine Shutdown**<br>*( Tắt thiết bị )* | `LV Main Switchboard & MV Control Panel` | Trip Low Voltage Main ACB (LV-ACB-MAIN) FIRST to remove transformer load. Then trip MV Vacuum Circuit Breaker (MV-VCB-01). | Ngắt Máy cắt hạ thế ACB (LV-ACB-MAIN) TRƯỚC để ngắt tải biến áp. Sau đó ngắt Máy cắt chân không trung thế (MV-VCB-01). | LV ACB indicates 'OPEN/DISCHARGED'. MV VCB indicator shows 'OFF/GREEN O'. |
| **3** | **Equipment Isolation**<br>*( Cách ly năng lượng )* | `RMU Bay & LV Switchboard` | RACK OUT MV VCB to Test/Disconnected position. Open MV Line Disconnector. Open DC Tripping Power Breaker DC-TRIP-CB. | RÚT MÁY CẮT VCB ra vị trí Thí nghiệm/Cách ly. Mở Dao cách ly đường dây RMU. Ngắt CB nguồn điều khiển 110VDC. | Breaker truck physically withdrawn; mechanical shutter closed over live busbar contacts. |
| **4** | **LOTO Application**<br>*( Gắn khóa & Biển báo )* | `MV VCB Rack-in Shutter & LV ACB Lock` | Padlock the MV VCB racking mechanism shutter with Red Lock & Tag TAG-MV-04. Lock out LV ACB handle mechanism. | Khóa nắp che lỗ quay máy cắt MV VCB bằng Ổ khóa đỏ & Thẻ TAG-MV-04. Khóa cơ cấu thao tác LV ACB. | Racking handle insert hole blocked by padlock hasp. |
| **5** | **Energy Dissipation**<br>*( Xả năng lượng dư )* | `MV Cable Earthing Switch` | CLOSE MV Cable Earthing Switch (Earth Switch) on feeder bay to dump residual capacitive charge from 22kV underground cables to ground. | ĐÓNG Dao tiếp địa cáp trung thế (Earthing Switch) tại ngăn xuất tuyến để xả điện áp cảm ứng cáp ngầm 22kV xuống đất. | Earthing Switch position indicator shows 'EARTHED / CLOSED (YELLOW/GREEN)'. |
| **6** | **Zero Energy Test**<br>*( Kiểm tra Năng lượng 0 )* | `VPIS Voltage Indicators & HV Tester` | STAR Protocol: Check Voltage Presence Indicator (VPIS) unlit. Test with calibrated 22kV High Voltage Detector Rod on all 3 phases. | Quy tắc STAR: Kiểm tra đèn báo VPIS tắt. Dùng Bút thử điện cao thế 22kV đã kiểm định kiểm tra 3 pha. | HV Tester confirms NO VOLTAGE PRESENT on 22kV terminals. Zero Energy State verified. |


---

## 3. CMMS Payload (SAP PM / IBM Maximo API Ready)

The canonical JSON structure below is fully formatted for automated ingestion into **SAP PM (Plant Maintenance)** or **IBM Maximo Asset Management** REST/OData API endpoints. It carries an embedded `sha256_checksum` watermark to guarantee payload integrity.

```json
{
  "sop_id": "LOTO-ELEC-04",
  "title_en": "Internal Substation & Medium Voltage (MV) Switchgear Isolation SOP",
  "title_vi": "Quy trình Cô lập Trạm biến áp nội bộ & Tủ trung thế (Substation & MV Switchgear)",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "reference_facility": "FAC_GLOBAL_01",
  "equipment_group": "Electrical & Automation",
  "target_equipment_en": "22kV/0.4kV Distribution Transformer (2000kVA), Ring Main Unit (RMU) & 22kV Vacuum Circuit Breaker (VCB)",
  "target_equipment_vi": "Máy biến áp phân phối 22kV/0.4kV (2000kVA), Tủ trung thế RMU & Máy cắt chân không VCB 22kV",
  "energy_types_controlled": [
    "22,000VAC Medium Voltage 3-Phase",
    "400VAC Low Voltage Main Busbar",
    "110VDC Switchgear Control & Tripping Power"
  ],
  "isolation_points": [
    {
      "point_id": "MV-VCB-01",
      "type": "MEDIUM_VOLTAGE_AC",
      "rating": "22kV / 630A",
      "location": "MV_SUBSTATION_ROOM_BAY_1"
    },
    {
      "point_id": "LV-ACB-MAIN",
      "type": "LOW_VOLTAGE_AC",
      "rating": "400VAC / 3200A",
      "location": "LV_MAIN_DISTRIBUTION_ROOM"
    },
    {
      "point_id": "DC-TRIP-CB",
      "type": "CONTROL_DC",
      "rating": "110VDC / 32A",
      "location": "MV_CONTROL_PANEL"
    }
  ],
  "control_sequence_steps": [
    {
      "step_number": 1,
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "location": "Chief Electrical Engineer / Site Operations",
      "action_en": "Issue High Voltage Work Permit (HV-WP). Notify plant management of planned substation shutdown. Equip 24kV Class 3 Safety Gear.",
      "action_vi": "Cấp Giấy phép làm việc điện cao thế (HV-WP). Thông báo ban giám đốc về lịch cúp điện trạm. Trang bị đồ bảo hộ 24kV Class 3.",
      "verification_star": "HV Work Permit signed by Plant Electrical Authority."
    },
    {
      "step_number": 2,
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "location": "LV Main Switchboard & MV Control Panel",
      "action_en": "Trip Low Voltage Main ACB (LV-ACB-MAIN) FIRST to remove transformer load. Then trip MV Vacuum Circuit Breaker (MV-VCB-01).",
      "action_vi": "Ngắt Máy cắt hạ thế ACB (LV-ACB-MAIN) TRƯỚC để ngắt tải biến áp. Sau đó ngắt Máy cắt chân không trung thế (MV-VCB-01).",
      "verification_star": "LV ACB indicates 'OPEN/DISCHARGED'. MV VCB indicator shows 'OFF/GREEN O'."
    },
    {
      "step_number": 3,
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "location": "RMU Bay & LV Switchboard",
      "action_en": "RACK OUT MV VCB to Test/Disconnected position. Open MV Line Disconnector. Open DC Tripping Power Breaker DC-TRIP-CB.",
      "action_vi": "RÚT MÁY CẮT VCB ra vị trí Thí nghiệm/Cách ly. Mở Dao cách ly đường dây RMU. Ngắt CB nguồn điều khiển 110VDC.",
      "verification_star": "Breaker truck physically withdrawn; mechanical shutter closed over live busbar contacts."
    },
    {
      "step_number": 4,
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "location": "MV VCB Rack-in Shutter & LV ACB Lock",
      "action_en": "Padlock the MV VCB racking mechanism shutter with Red Lock & Tag TAG-MV-04. Lock out LV ACB handle mechanism.",
      "action_vi": "Khóa nắp che lỗ quay máy cắt MV VCB bằng Ổ khóa đỏ & Thẻ TAG-MV-04. Khóa cơ cấu thao tác LV ACB.",
      "verification_star": "Racking handle insert hole blocked by padlock hasp."
    },
    {
      "step_number": 5,
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "location": "MV Cable Earthing Switch",
      "action_en": "CLOSE MV Cable Earthing Switch (Earth Switch) on feeder bay to dump residual capacitive charge from 22kV underground cables to ground.",
      "action_vi": "ĐÓNG Dao tiếp địa cáp trung thế (Earthing Switch) tại ngăn xuất tuyến để xả điện áp cảm ứng cáp ngầm 22kV xuống đất.",
      "verification_star": "Earthing Switch position indicator shows 'EARTHED / CLOSED (YELLOW/GREEN)'."
    },
    {
      "step_number": 6,
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "location": "VPIS Voltage Indicators & HV Tester",
      "action_en": "STAR Protocol: Check Voltage Presence Indicator (VPIS) unlit. Test with calibrated 22kV High Voltage Detector Rod on all 3 phases.",
      "action_vi": "Quy tắc STAR: Kiểm tra đèn báo VPIS tắt. Dùng Bút thử điện cao thế 22kV đã kiểm định kiểm tra 3 pha.",
      "verification_star": "HV Tester confirms NO VOLTAGE PRESENT on 22kV terminals. Zero Energy State verified."
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
  "sha256_checksum": "f41c364dd5e0dabbfd22411b02e8bdda37b445d878076700c130046d4eca4e12"
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
      "action_en": "Issue High Voltage Work Permit (HV-WP). Notify plant management of planned substation shutdown. Equip 24kV Class 3 Safety Gear.",
      "action_vi": "Cấp Giấy phép làm việc điện cao thế (HV-WP). Thông báo ban giám đốc về lịch cúp điện trạm. Trang bị đồ bảo hộ 24kV Class 3.",
      "location": "Chief Electrical Engineer / Site Operations",
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "step_number": 1,
      "verification_star": "HV Work Permit signed by Plant Electrical Authority."
    },
    {
      "action_en": "Trip Low Voltage Main ACB (LV-ACB-MAIN) FIRST to remove transformer load. Then trip MV Vacuum Circuit Breaker (MV-VCB-01).",
      "action_vi": "Ngắt Máy cắt hạ thế ACB (LV-ACB-MAIN) TRƯỚC để ngắt tải biến áp. Sau đó ngắt Máy cắt chân không trung thế (MV-VCB-01).",
      "location": "LV Main Switchboard & MV Control Panel",
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "step_number": 2,
      "verification_star": "LV ACB indicates 'OPEN/DISCHARGED'. MV VCB indicator shows 'OFF/GREEN O'."
    },
    {
      "action_en": "RACK OUT MV VCB to Test/Disconnected position. Open MV Line Disconnector. Open DC Tripping Power Breaker DC-TRIP-CB.",
      "action_vi": "RÚT MÁY CẮT VCB ra vị trí Thí nghiệm/Cách ly. Mở Dao cách ly đường dây RMU. Ngắt CB nguồn điều khiển 110VDC.",
      "location": "RMU Bay & LV Switchboard",
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "step_number": 3,
      "verification_star": "Breaker truck physically withdrawn; mechanical shutter closed over live busbar contacts."
    },
    {
      "action_en": "Padlock the MV VCB racking mechanism shutter with Red Lock & Tag TAG-MV-04. Lock out LV ACB handle mechanism.",
      "action_vi": "Khóa nắp che lỗ quay máy cắt MV VCB bằng Ổ khóa đỏ & Thẻ TAG-MV-04. Khóa cơ cấu thao tác LV ACB.",
      "location": "MV VCB Rack-in Shutter & LV ACB Lock",
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "step_number": 4,
      "verification_star": "Racking handle insert hole blocked by padlock hasp."
    },
    {
      "action_en": "CLOSE MV Cable Earthing Switch (Earth Switch) on feeder bay to dump residual capacitive charge from 22kV underground cables to ground.",
      "action_vi": "ĐÓNG Dao tiếp địa cáp trung thế (Earthing Switch) tại ngăn xuất tuyến để xả điện áp cảm ứng cáp ngầm 22kV xuống đất.",
      "location": "MV Cable Earthing Switch",
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "step_number": 5,
      "verification_star": "Earthing Switch position indicator shows 'EARTHED / CLOSED (YELLOW/GREEN)'."
    },
    {
      "action_en": "STAR Protocol: Check Voltage Presence Indicator (VPIS) unlit. Test with calibrated 22kV High Voltage Detector Rod on all 3 phases.",
      "action_vi": "Quy tắc STAR: Kiểm tra đèn báo VPIS tắt. Dùng Bút thử điện cao thế 22kV đã kiểm định kiểm tra 3 pha.",
      "location": "VPIS Voltage Indicators & HV Tester",
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "step_number": 6,
      "verification_star": "HV Tester confirms NO VOLTAGE PRESENT on 22kV terminals. Zero Energy State verified."
    }
  ],
  "energy_types_controlled": [
    "22,000VAC Medium Voltage 3-Phase",
    "400VAC Low Voltage Main Busbar",
    "110VDC Switchgear Control & Tripping Power"
  ],
  "equipment_group": "Electrical & Automation",
  "isolation_points": [
    {
      "location": "MV_SUBSTATION_ROOM_BAY_1",
      "point_id": "MV-VCB-01",
      "rating": "22kV / 630A",
      "type": "MEDIUM_VOLTAGE_AC"
    },
    {
      "location": "LV_MAIN_DISTRIBUTION_ROOM",
      "point_id": "LV-ACB-MAIN",
      "rating": "400VAC / 3200A",
      "type": "LOW_VOLTAGE_AC"
    },
    {
      "location": "MV_CONTROL_PANEL",
      "point_id": "DC-TRIP-CB",
      "rating": "110VDC / 32A",
      "type": "CONTROL_DC"
    }
  ],
  "reference_facility": "FAC_GLOBAL_01",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "sop_id": "LOTO-ELEC-04",
  "target_equipment_en": "22kV/0.4kV Distribution Transformer (2000kVA), Ring Main Unit (RMU) & 22kV Vacuum Circuit Breaker (VCB)",
  "target_equipment_vi": "Máy biến áp phân phối 22kV/0.4kV (2000kVA), Tủ trung thế RMU & Máy cắt chân không VCB 22kV",
  "title_en": "Internal Substation & Medium Voltage (MV) Switchgear Isolation SOP",
  "title_vi": "Quy trình Cô lập Trạm biến áp nội bộ & Tủ trung thế (Substation & MV Switchgear)"
}

# Re-compute SHA-256 Hash
computed_hash = hashlib.sha256(
    json.dumps(payload_data, sort_keys=True, ensure_ascii=False).encode('utf-8')
).hexdigest()

expected_hash = "f41c364dd5e0dabbfd22411b02e8bdda37b445d878076700c130046d4eca4e12"

print("=" * 70)
print("CMMS LOTO SOP INTEGRITY AUDIT")
print("=" * 70)
print(f"SOP ID:        LOTO-ELEC-04")
print(f"Expected Hash: {expected_hash}")
print(f"Computed Hash: {computed_hash}")
print(f"Match Result:  {computed_hash == expected_hash}")
print("=" * 70)
```

---
*Document produced as part of the Digital IP Assets Collection for One-Person Digital Enterprise.*
