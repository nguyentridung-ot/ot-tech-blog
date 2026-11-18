---
title: "LOTO-ELEC-02: Central PLC/SCADA Cabinet & Servo Drive Power Isolation SOP"
sop_id: "LOTO-ELEC-02"
standard: "OSHA 29 CFR 1910.147"
equipment_group: "Electrical & Automation"
facility_reference: "FAC_GLOBAL_01"
author: "Nguyen Tri Dung (Industrial OT Authority)"
date: 2026-11-13
sha256_checksum: "94cb8cf90e91b8be9ec7a167d9fbf52fe1571f1b170ff66cccdfc588cbda4b92"
tags: ["Safety", "LOTO", "Electrical", "Automation", "OSHA", "SHA-256", "SAP-PM", "IBM-Maximo"]
---

# LOTO-ELEC-02: Central PLC/SCADA Cabinet & Servo Drive Power Isolation SOP
### (Quy trình Cô lập Tủ điều khiển PLC / SCADA & Nguồn Servo Drive)

> **🔒 NDA & Reference Model Notice:** All equipment identifiers, breaker codes, and location tags in this Standard Operating Procedure are defined under the **Standard Reference Model (`FAC_GLOBAL_01`)**. No proprietary factory data or actual operational plant logs are exposed.
> 
> **🛡️ Cryptographic Verification Watermark:** 
> **SHA-256 Digest:** `94cb8cf90e91b8be9ec7a167d9fbf52fe1571f1b170ff66cccdfc588cbda4b92`

---

## 1. System Scope & Energy Control Overview

This Standard Operating Procedure (SOP) defines the mandatory **6-Step Hazardous Energy Control Protocol** required under **OSHA 29 CFR 1910.147** prior to performing maintenance, servicing, or technical intervention on **Central PLC (Siemens S7-1500/AB GuardLogix), 24VDC Power Supplies & Multi-Axis Servo Drives**.

* **Target System / Equipment:** Central PLC (Siemens S7-1500/AB GuardLogix), 24VDC Power Supplies & Multi-Axis Servo Drives (Tủ điều khiển trung tâm PLC, bộ nguồn 24VDC công nghiệp & Bộ điều khiển Servo đa trục)
* **Regulatory Compliance Standard:** OSHA 29 CFR 1910.147 (Control of Hazardous Energy)
* **Hazardous Energy Types Present:** 230VAC Control Power, 24VDC Bus Power, 400VAC Servo Main Power, UPS Auxiliary Battery Backed Supply
* **Verification Protocol:** STAR Method (Stop - Test - Actuate - Read)

---

## 2. Bilingual 6-Step Energy Isolation Matrix

The matrix below details the exact step-by-step physical actions required to achieve a verified **Zero Energy State (ZES)**.

| Step # | Phase Name (EN / VI) | Location & Isolation Point | Required Action (English) | Thao Tác Bắt Buộc (Tiếng Việt) | Verification Method / STAR Protocol |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Notification & Prep**<br>*( Thông báo & Chuẩn bị )* | `SCADA / HMI Master Station` | Inform SCADA system admin. Save current PLC batch parameters and trigger controlled system park sequence. | Thông báo cho quản trị hệ thống SCADA. Lưu thông số batch PLC và kích hoạt chu trình về vị trí gốc (Home/Park). | SCADA screen displays system mode: 'SYSTEM_PARKED_SAFE'. |
| **2** | **Machine Shutdown**<br>*( Tắt thiết bị )* | `Main Control Desk` | Initiate Soft Shutdown via PLC HMI key switch. Turn Key Switch to 'STOP/OFF' position. | Thực hiện Tắt mềm qua công tắc chìa khóa HMI PLC. Vặn chìa khóa sang vị trí 'STOP/OFF'. | PLC CPU RUN LED changes to STOP (Solid Yellow/Amber). |
| **3** | **Equipment Isolation**<br>*( Cách ly năng lượng )* | `PLC Main Cabinet & Servo Bay` | Disconnect Servo Main Breaker SERVO-Q02, PLC Power Breaker PLC-CB01, and UPS Auxiliary Isolator UPS-DISC-01. | Ngắt Cầu dao nguồn Servo SERVO-Q02, CB nguồn PLC PLC-CB01 và Cầu dao cách ly UPS UPS-DISC-01. | All circuit breaker levers physically flipped down to 'OFF/O' position. |
| **4** | **LOTO Application**<br>*( Gắn khóa & Biển báo )* | `Breakers PLC-CB01, SERVO-Q02, UPS-DISC-01` | Attach lockout lockout bar and padlocks with Tag TAG-PLC-02 across all 3 breaker handles. | Gắn thanh khóa CB và ổ khóa kèm Thẻ TAG-PLC-02 trên cả 3 tay bấm breaker. | Check lock tightness; breaker handles immobilized. |
| **5** | **Energy Dissipation**<br>*( Xả năng lượng dư )* | `Servo Bus & 24VDC Capacitors` | Allow 3 minutes for Servo Drive internal DC energy and 24VDC smoothing capacitors to bleed out. | Chờ 3 phút để năng lượng DC nội bộ của Servo Drive và tụ lọc nguồn 24VDC xả hết. | Status 7-segment displays on Servo Drives turned off. |
| **6** | **Zero Energy Test**<br>*( Kiểm tra Năng lượng 0 )* | `PLC Terminals & Servo Power Inlets` | STAR Protocol: Measure 0VAC on PLC-CB01 output terminals, 0VDC on 24V bus, and 0VAC on Servo input terminals. | Quy tắc STAR: Đo 0VAC tại đầu ra PLC-CB01, 0VDC tại bus 24V và 0VAC tại đầu vào Servo Drive. | All multimeter readings confirm 0.0V. CPU and Remote I/O drops completely dark. |


---

## 3. CMMS Payload (SAP PM / IBM Maximo API Ready)

The canonical JSON structure below is fully formatted for automated ingestion into **SAP PM (Plant Maintenance)** or **IBM Maximo Asset Management** REST/OData API endpoints. It carries an embedded `sha256_checksum` watermark to guarantee payload integrity.

```json
{
  "sop_id": "LOTO-ELEC-02",
  "title_en": "Central PLC/SCADA Cabinet & Servo Drive Power Isolation SOP",
  "title_vi": "Quy trình Cô lập Tủ điều khiển PLC / SCADA & Nguồn Servo Drive",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "reference_facility": "FAC_GLOBAL_01",
  "equipment_group": "Electrical & Automation",
  "target_equipment_en": "Central PLC (Siemens S7-1500/AB GuardLogix), 24VDC Power Supplies & Multi-Axis Servo Drives",
  "target_equipment_vi": "Tủ điều khiển trung tâm PLC, bộ nguồn 24VDC công nghiệp & Bộ điều khiển Servo đa trục",
  "energy_types_controlled": [
    "230VAC Control Power",
    "24VDC Bus Power",
    "400VAC Servo Main Power",
    "UPS Auxiliary Battery Backed Supply"
  ],
  "isolation_points": [
    {
      "point_id": "PLC-CB01",
      "type": "ELECTRICAL_AC",
      "rating": "230VAC / 16A",
      "location": "PANEL_PLC_MAIN_BAY_01"
    },
    {
      "point_id": "SERVO-Q02",
      "type": "ELECTRICAL_AC",
      "rating": "400VAC / 63A",
      "location": "PANEL_SERVO_RACK_01"
    },
    {
      "point_id": "UPS-DISC-01",
      "type": "AUXILIARY_DC",
      "rating": "24VDC / 40A",
      "location": "UPS_PANEL_AUX"
    }
  ],
  "control_sequence_steps": [
    {
      "step_number": 1,
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "location": "SCADA / HMI Master Station",
      "action_en": "Inform SCADA system admin. Save current PLC batch parameters and trigger controlled system park sequence.",
      "action_vi": "Thông báo cho quản trị hệ thống SCADA. Lưu thông số batch PLC và kích hoạt chu trình về vị trí gốc (Home/Park).",
      "verification_star": "SCADA screen displays system mode: 'SYSTEM_PARKED_SAFE'."
    },
    {
      "step_number": 2,
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "location": "Main Control Desk",
      "action_en": "Initiate Soft Shutdown via PLC HMI key switch. Turn Key Switch to 'STOP/OFF' position.",
      "action_vi": "Thực hiện Tắt mềm qua công tắc chìa khóa HMI PLC. Vặn chìa khóa sang vị trí 'STOP/OFF'.",
      "verification_star": "PLC CPU RUN LED changes to STOP (Solid Yellow/Amber)."
    },
    {
      "step_number": 3,
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "location": "PLC Main Cabinet & Servo Bay",
      "action_en": "Disconnect Servo Main Breaker SERVO-Q02, PLC Power Breaker PLC-CB01, and UPS Auxiliary Isolator UPS-DISC-01.",
      "action_vi": "Ngắt Cầu dao nguồn Servo SERVO-Q02, CB nguồn PLC PLC-CB01 và Cầu dao cách ly UPS UPS-DISC-01.",
      "verification_star": "All circuit breaker levers physically flipped down to 'OFF/O' position."
    },
    {
      "step_number": 4,
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "location": "Breakers PLC-CB01, SERVO-Q02, UPS-DISC-01",
      "action_en": "Attach lockout lockout bar and padlocks with Tag TAG-PLC-02 across all 3 breaker handles.",
      "action_vi": "Gắn thanh khóa CB và ổ khóa kèm Thẻ TAG-PLC-02 trên cả 3 tay bấm breaker.",
      "verification_star": "Check lock tightness; breaker handles immobilized."
    },
    {
      "step_number": 5,
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "location": "Servo Bus & 24VDC Capacitors",
      "action_en": "Allow 3 minutes for Servo Drive internal DC energy and 24VDC smoothing capacitors to bleed out.",
      "action_vi": "Chờ 3 phút để năng lượng DC nội bộ của Servo Drive và tụ lọc nguồn 24VDC xả hết.",
      "verification_star": "Status 7-segment displays on Servo Drives turned off."
    },
    {
      "step_number": 6,
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "location": "PLC Terminals & Servo Power Inlets",
      "action_en": "STAR Protocol: Measure 0VAC on PLC-CB01 output terminals, 0VDC on 24V bus, and 0VAC on Servo input terminals.",
      "action_vi": "Quy tắc STAR: Đo 0VAC tại đầu ra PLC-CB01, 0VDC tại bus 24V và 0VAC tại đầu vào Servo Drive.",
      "verification_star": "All multimeter readings confirm 0.0V. CPU and Remote I/O drops completely dark."
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
  "sha256_checksum": "94cb8cf90e91b8be9ec7a167d9fbf52fe1571f1b170ff66cccdfc588cbda4b92"
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
      "action_en": "Inform SCADA system admin. Save current PLC batch parameters and trigger controlled system park sequence.",
      "action_vi": "Thông báo cho quản trị hệ thống SCADA. Lưu thông số batch PLC và kích hoạt chu trình về vị trí gốc (Home/Park).",
      "location": "SCADA / HMI Master Station",
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "step_number": 1,
      "verification_star": "SCADA screen displays system mode: 'SYSTEM_PARKED_SAFE'."
    },
    {
      "action_en": "Initiate Soft Shutdown via PLC HMI key switch. Turn Key Switch to 'STOP/OFF' position.",
      "action_vi": "Thực hiện Tắt mềm qua công tắc chìa khóa HMI PLC. Vặn chìa khóa sang vị trí 'STOP/OFF'.",
      "location": "Main Control Desk",
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "step_number": 2,
      "verification_star": "PLC CPU RUN LED changes to STOP (Solid Yellow/Amber)."
    },
    {
      "action_en": "Disconnect Servo Main Breaker SERVO-Q02, PLC Power Breaker PLC-CB01, and UPS Auxiliary Isolator UPS-DISC-01.",
      "action_vi": "Ngắt Cầu dao nguồn Servo SERVO-Q02, CB nguồn PLC PLC-CB01 và Cầu dao cách ly UPS UPS-DISC-01.",
      "location": "PLC Main Cabinet & Servo Bay",
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "step_number": 3,
      "verification_star": "All circuit breaker levers physically flipped down to 'OFF/O' position."
    },
    {
      "action_en": "Attach lockout lockout bar and padlocks with Tag TAG-PLC-02 across all 3 breaker handles.",
      "action_vi": "Gắn thanh khóa CB và ổ khóa kèm Thẻ TAG-PLC-02 trên cả 3 tay bấm breaker.",
      "location": "Breakers PLC-CB01, SERVO-Q02, UPS-DISC-01",
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "step_number": 4,
      "verification_star": "Check lock tightness; breaker handles immobilized."
    },
    {
      "action_en": "Allow 3 minutes for Servo Drive internal DC energy and 24VDC smoothing capacitors to bleed out.",
      "action_vi": "Chờ 3 phút để năng lượng DC nội bộ của Servo Drive và tụ lọc nguồn 24VDC xả hết.",
      "location": "Servo Bus & 24VDC Capacitors",
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "step_number": 5,
      "verification_star": "Status 7-segment displays on Servo Drives turned off."
    },
    {
      "action_en": "STAR Protocol: Measure 0VAC on PLC-CB01 output terminals, 0VDC on 24V bus, and 0VAC on Servo input terminals.",
      "action_vi": "Quy tắc STAR: Đo 0VAC tại đầu ra PLC-CB01, 0VDC tại bus 24V và 0VAC tại đầu vào Servo Drive.",
      "location": "PLC Terminals & Servo Power Inlets",
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "step_number": 6,
      "verification_star": "All multimeter readings confirm 0.0V. CPU and Remote I/O drops completely dark."
    }
  ],
  "energy_types_controlled": [
    "230VAC Control Power",
    "24VDC Bus Power",
    "400VAC Servo Main Power",
    "UPS Auxiliary Battery Backed Supply"
  ],
  "equipment_group": "Electrical & Automation",
  "isolation_points": [
    {
      "location": "PANEL_PLC_MAIN_BAY_01",
      "point_id": "PLC-CB01",
      "rating": "230VAC / 16A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "PANEL_SERVO_RACK_01",
      "point_id": "SERVO-Q02",
      "rating": "400VAC / 63A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "UPS_PANEL_AUX",
      "point_id": "UPS-DISC-01",
      "rating": "24VDC / 40A",
      "type": "AUXILIARY_DC"
    }
  ],
  "reference_facility": "FAC_GLOBAL_01",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "sop_id": "LOTO-ELEC-02",
  "target_equipment_en": "Central PLC (Siemens S7-1500/AB GuardLogix), 24VDC Power Supplies & Multi-Axis Servo Drives",
  "target_equipment_vi": "Tủ điều khiển trung tâm PLC, bộ nguồn 24VDC công nghiệp & Bộ điều khiển Servo đa trục",
  "title_en": "Central PLC/SCADA Cabinet & Servo Drive Power Isolation SOP",
  "title_vi": "Quy trình Cô lập Tủ điều khiển PLC / SCADA & Nguồn Servo Drive"
}

# Re-compute SHA-256 Hash
computed_hash = hashlib.sha256(
    json.dumps(payload_data, sort_keys=True, ensure_ascii=False).encode('utf-8')
).hexdigest()

expected_hash = "94cb8cf90e91b8be9ec7a167d9fbf52fe1571f1b170ff66cccdfc588cbda4b92"

print("=" * 70)
print("CMMS LOTO SOP INTEGRITY AUDIT")
print("=" * 70)
print(f"SOP ID:        LOTO-ELEC-02")
print(f"Expected Hash: {expected_hash}")
print(f"Computed Hash: {computed_hash}")
print(f"Match Result:  {computed_hash == expected_hash}")
print("=" * 70)
```

---
*Document produced as part of the Digital IP Assets Collection for One-Person Digital Enterprise.*
