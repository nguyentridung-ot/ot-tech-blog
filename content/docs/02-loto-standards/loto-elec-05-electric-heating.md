---
title: "LOTO-ELEC-05: Industrial Electric Heating Element & Dry Oven Control Panel Isolation SOP"
sop_id: "LOTO-ELEC-05"
standard: "OSHA 29 CFR 1910.147"
equipment_group: "Electrical & Automation"
facility_reference: "FAC_GLOBAL_01"
author: "Nguyen Tri Dung (Industrial OT Authority)"
date: 2026-11-13
sha256_checksum: "df29de46e3270148391e29cedabce411a1d46404311adfbea2006aa86e61c2b3"
tags: ["Safety", "LOTO", "Electrical", "Automation", "OSHA", "SHA-256", "SAP-PM", "IBM-Maximo"]
---

# LOTO-ELEC-05: Industrial Electric Heating Element & Dry Oven Control Panel Isolation SOP
### (Quy trình Cô lập Hệ thống gia nhiệt điện trở & Tủ sấy công nghiệp)

> **🔒 NDA & Reference Model Notice:** All equipment identifiers, breaker codes, and location tags in this Standard Operating Procedure are defined under the **Standard Reference Model (`FAC_GLOBAL_01`)**. No proprietary factory data or actual operational plant logs are exposed.
> 
> **🛡️ Cryptographic Verification Watermark:** 
> **SHA-256 Digest:** `df29de46e3270148391e29cedabce411a1d46404311adfbea2006aa86e61c2b3`

---

## 1. System Scope & Energy Control Overview

This Standard Operating Procedure (SOP) defines the mandatory **6-Step Hazardous Energy Control Protocol** required under **OSHA 29 CFR 1910.147** prior to performing maintenance, servicing, or technical intervention on **Industrial Conveyor Drying Oven (180 kW Heating Bank), Solid State Relays (SSR) & Circulation Blower Fans**.

* **Target System / Equipment:** Industrial Conveyor Drying Oven (180 kW Heating Bank), Solid State Relays (SSR) & Circulation Blower Fans (Dàn sấy băng tải công nghiệp (Dàn điện trở gia nhiệt 180 kW), Bộ điều khiển bán dẫn SSR & Quạt quạt gió tuần hoàn)
* **Regulatory Compliance Standard:** OSHA 29 CFR 1910.147 (Control of Hazardous Energy)
* **Hazardous Energy Types Present:** 400VAC 3-Phase Heating Power, 230VAC PID Controller Power, Stored Thermal Energy (>200°C Residual Heat)
* **Verification Protocol:** STAR Method (Stop - Test - Actuate - Read)

---

## 2. Bilingual 6-Step Energy Isolation Matrix

The matrix below details the exact step-by-step physical actions required to achieve a verified **Zero Energy State (ZES)**.

| Step # | Phase Name (EN / VI) | Location & Isolation Point | Required Action (English) | Thao Tác Bắt Buộc (Tiếng Việt) | Verification Method / STAR Protocol |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | **Notification & Prep**<br>*( Thông báo & Chuẩn bị )* | `Oven Operating Station` | Notify thermal process team. Allow cooling purge cycle to lower internal chamber temperature below 40°C before isolation. | Thông báo cho đội vận hành lò sấy. Chạy chu trình thổi quạt làm nguội để hạ nhiệt độ buồng sấy xuống dưới 40°C trước khi cô lập. | Chamber temperature sensor TE-101 reads < 40°C on PID controller. |
| **2** | **Machine Shutdown**<br>*( Tắt thiết bị )* | `Oven Main PID Controller` | Set PID Heating Output to 0%. Turn OFF Main Heater Start Switch on panel door. Stop circulation fans after purge completion. | Đặt đầu ra gia nhiệt PID về 0%. Tắt Công tắc khởi động gia nhiệt trên cửa tủ. Dừng quạt tuần hoàn sau khi làm nguội xong. | PID Output percentage reads 0.0%. SSR trigger status LEDs turn OFF. |
| **3** | **Equipment Isolation**<br>*( Cách ly năng lượng )* | `Oven Power Panel Bay 1 & 2` | Open Heating Main Disconnect Switch HEAT-Q01, Fan Breaker FAN-CB02, and PID Controller Breaker PID-CB03. | Ngắt Cầu dao chính dàn sấy HEAT-Q01, CB quạt gió FAN-CB02 và CB bộ điều khiển PID PID-CB03. | Disconnect switch handle turned to '0/OFF' position. |
| **4** | **LOTO Application**<br>*( Gắn khóa & Biển báo )* | `HEAT-Q01 Switch Handle & Breaker Bars` | Apply lockout hasp and personal padlocks with Tag TAG-HTR-05 on HEAT-Q01, FAN-CB02, and PID-CB03. | Móc gá khóa chùm và khóa cá nhân kèm Thẻ TAG-HTR-05 lên HEAT-Q01, FAN-CB02 và PID-CB03. | Confirm padlocks securely retain switch handles in OFF position. |
| **5** | **Energy Dissipation**<br>*( Xả năng lượng dư )* | `Oven Heating Chamber & SSR Terminals` | Verify residual thermal dissipation (touch test on outer insulation shell < 35°C). Ensure SSR leakage current is cut off. | Xác nhận nhiệt năng dư đã tản hết (sờ vỏ cách nhiệt outer shell < 35°C). Đảm bảo rò điện qua SSR được ngắt hoàn toàn. | Infrared Thermometer confirms oven busbar temperature < 35°C. |
| **6** | **Zero Energy Test**<br>*( Kiểm tra Năng lượng 0 )* | `Heating Element Terminal Block (U-V-W)` | STAR Protocol: Measure voltage on heating element terminals (Phase-Phase & Phase-Earth) using CAT III Multimeter. | Quy tắc STAR: Đo điện áp tại cọc đấu thanh gia nhiệt (Pha-Pha và Pha-Đất) bằng đồng hồ CAT III. | Multimeter confirms 0.0VAC across all heater element terminals. Zero Energy State verified. |


---

## 3. CMMS Payload (SAP PM / IBM Maximo API Ready)

The canonical JSON structure below is fully formatted for automated ingestion into **SAP PM (Plant Maintenance)** or **IBM Maximo Asset Management** REST/OData API endpoints. It carries an embedded `sha256_checksum` watermark to guarantee payload integrity.

```json
{
  "sop_id": "LOTO-ELEC-05",
  "title_en": "Industrial Electric Heating Element & Dry Oven Control Panel Isolation SOP",
  "title_vi": "Quy trình Cô lập Hệ thống gia nhiệt điện trở & Tủ sấy công nghiệp",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "reference_facility": "FAC_GLOBAL_01",
  "equipment_group": "Electrical & Automation",
  "target_equipment_en": "Industrial Conveyor Drying Oven (180 kW Heating Bank), Solid State Relays (SSR) & Circulation Blower Fans",
  "target_equipment_vi": "Dàn sấy băng tải công nghiệp (Dàn điện trở gia nhiệt 180 kW), Bộ điều khiển bán dẫn SSR & Quạt quạt gió tuần hoàn",
  "energy_types_controlled": [
    "400VAC 3-Phase Heating Power",
    "230VAC PID Controller Power",
    "Stored Thermal Energy (>200°C Residual Heat)"
  ],
  "isolation_points": [
    {
      "point_id": "HEAT-Q01",
      "type": "ELECTRICAL_AC",
      "rating": "400VAC / 400A",
      "location": "OVEN_POWER_PANEL_BAY_1"
    },
    {
      "point_id": "FAN-CB02",
      "type": "ELECTRICAL_AC",
      "rating": "400VAC / 40A",
      "location": "OVEN_POWER_PANEL_BAY_2"
    },
    {
      "point_id": "PID-CB03",
      "type": "CONTROL_AC",
      "rating": "230VAC / 10A",
      "location": "OVEN_CONTROL_DOOR"
    }
  ],
  "control_sequence_steps": [
    {
      "step_number": 1,
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "location": "Oven Operating Station",
      "action_en": "Notify thermal process team. Allow cooling purge cycle to lower internal chamber temperature below 40°C before isolation.",
      "action_vi": "Thông báo cho đội vận hành lò sấy. Chạy chu trình thổi quạt làm nguội để hạ nhiệt độ buồng sấy xuống dưới 40°C trước khi cô lập.",
      "verification_star": "Chamber temperature sensor TE-101 reads < 40°C on PID controller."
    },
    {
      "step_number": 2,
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "location": "Oven Main PID Controller",
      "action_en": "Set PID Heating Output to 0%. Turn OFF Main Heater Start Switch on panel door. Stop circulation fans after purge completion.",
      "action_vi": "Đặt đầu ra gia nhiệt PID về 0%. Tắt Công tắc khởi động gia nhiệt trên cửa tủ. Dừng quạt tuần hoàn sau khi làm nguội xong.",
      "verification_star": "PID Output percentage reads 0.0%. SSR trigger status LEDs turn OFF."
    },
    {
      "step_number": 3,
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "location": "Oven Power Panel Bay 1 & 2",
      "action_en": "Open Heating Main Disconnect Switch HEAT-Q01, Fan Breaker FAN-CB02, and PID Controller Breaker PID-CB03.",
      "action_vi": "Ngắt Cầu dao chính dàn sấy HEAT-Q01, CB quạt gió FAN-CB02 và CB bộ điều khiển PID PID-CB03.",
      "verification_star": "Disconnect switch handle turned to '0/OFF' position."
    },
    {
      "step_number": 4,
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "location": "HEAT-Q01 Switch Handle & Breaker Bars",
      "action_en": "Apply lockout hasp and personal padlocks with Tag TAG-HTR-05 on HEAT-Q01, FAN-CB02, and PID-CB03.",
      "action_vi": "Móc gá khóa chùm và khóa cá nhân kèm Thẻ TAG-HTR-05 lên HEAT-Q01, FAN-CB02 và PID-CB03.",
      "verification_star": "Confirm padlocks securely retain switch handles in OFF position."
    },
    {
      "step_number": 5,
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "location": "Oven Heating Chamber & SSR Terminals",
      "action_en": "Verify residual thermal dissipation (touch test on outer insulation shell < 35°C). Ensure SSR leakage current is cut off.",
      "action_vi": "Xác nhận nhiệt năng dư đã tản hết (sờ vỏ cách nhiệt outer shell < 35°C). Đảm bảo rò điện qua SSR được ngắt hoàn toàn.",
      "verification_star": "Infrared Thermometer confirms oven busbar temperature < 35°C."
    },
    {
      "step_number": 6,
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "location": "Heating Element Terminal Block (U-V-W)",
      "action_en": "STAR Protocol: Measure voltage on heating element terminals (Phase-Phase & Phase-Earth) using CAT III Multimeter.",
      "action_vi": "Quy tắc STAR: Đo điện áp tại cọc đấu thanh gia nhiệt (Pha-Pha và Pha-Đất) bằng đồng hồ CAT III.",
      "verification_star": "Multimeter confirms 0.0VAC across all heater element terminals. Zero Energy State verified."
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
  "sha256_checksum": "df29de46e3270148391e29cedabce411a1d46404311adfbea2006aa86e61c2b3"
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
      "action_en": "Notify thermal process team. Allow cooling purge cycle to lower internal chamber temperature below 40°C before isolation.",
      "action_vi": "Thông báo cho đội vận hành lò sấy. Chạy chu trình thổi quạt làm nguội để hạ nhiệt độ buồng sấy xuống dưới 40°C trước khi cô lập.",
      "location": "Oven Operating Station",
      "phase_en": "Notification & Prep",
      "phase_vi": "Thông báo & Chuẩn bị",
      "step_number": 1,
      "verification_star": "Chamber temperature sensor TE-101 reads < 40°C on PID controller."
    },
    {
      "action_en": "Set PID Heating Output to 0%. Turn OFF Main Heater Start Switch on panel door. Stop circulation fans after purge completion.",
      "action_vi": "Đặt đầu ra gia nhiệt PID về 0%. Tắt Công tắc khởi động gia nhiệt trên cửa tủ. Dừng quạt tuần hoàn sau khi làm nguội xong.",
      "location": "Oven Main PID Controller",
      "phase_en": "Machine Shutdown",
      "phase_vi": "Tắt thiết bị",
      "step_number": 2,
      "verification_star": "PID Output percentage reads 0.0%. SSR trigger status LEDs turn OFF."
    },
    {
      "action_en": "Open Heating Main Disconnect Switch HEAT-Q01, Fan Breaker FAN-CB02, and PID Controller Breaker PID-CB03.",
      "action_vi": "Ngắt Cầu dao chính dàn sấy HEAT-Q01, CB quạt gió FAN-CB02 và CB bộ điều khiển PID PID-CB03.",
      "location": "Oven Power Panel Bay 1 & 2",
      "phase_en": "Equipment Isolation",
      "phase_vi": "Cách ly năng lượng",
      "step_number": 3,
      "verification_star": "Disconnect switch handle turned to '0/OFF' position."
    },
    {
      "action_en": "Apply lockout hasp and personal padlocks with Tag TAG-HTR-05 on HEAT-Q01, FAN-CB02, and PID-CB03.",
      "action_vi": "Móc gá khóa chùm và khóa cá nhân kèm Thẻ TAG-HTR-05 lên HEAT-Q01, FAN-CB02 và PID-CB03.",
      "location": "HEAT-Q01 Switch Handle & Breaker Bars",
      "phase_en": "LOTO Application",
      "phase_vi": "Gắn khóa & Biển báo",
      "step_number": 4,
      "verification_star": "Confirm padlocks securely retain switch handles in OFF position."
    },
    {
      "action_en": "Verify residual thermal dissipation (touch test on outer insulation shell < 35°C). Ensure SSR leakage current is cut off.",
      "action_vi": "Xác nhận nhiệt năng dư đã tản hết (sờ vỏ cách nhiệt outer shell < 35°C). Đảm bảo rò điện qua SSR được ngắt hoàn toàn.",
      "location": "Oven Heating Chamber & SSR Terminals",
      "phase_en": "Energy Dissipation",
      "phase_vi": "Xả năng lượng dư",
      "step_number": 5,
      "verification_star": "Infrared Thermometer confirms oven busbar temperature < 35°C."
    },
    {
      "action_en": "STAR Protocol: Measure voltage on heating element terminals (Phase-Phase & Phase-Earth) using CAT III Multimeter.",
      "action_vi": "Quy tắc STAR: Đo điện áp tại cọc đấu thanh gia nhiệt (Pha-Pha và Pha-Đất) bằng đồng hồ CAT III.",
      "location": "Heating Element Terminal Block (U-V-W)",
      "phase_en": "Zero Energy Test",
      "phase_vi": "Kiểm tra Năng lượng 0",
      "step_number": 6,
      "verification_star": "Multimeter confirms 0.0VAC across all heater element terminals. Zero Energy State verified."
    }
  ],
  "energy_types_controlled": [
    "400VAC 3-Phase Heating Power",
    "230VAC PID Controller Power",
    "Stored Thermal Energy (>200°C Residual Heat)"
  ],
  "equipment_group": "Electrical & Automation",
  "isolation_points": [
    {
      "location": "OVEN_POWER_PANEL_BAY_1",
      "point_id": "HEAT-Q01",
      "rating": "400VAC / 400A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "OVEN_POWER_PANEL_BAY_2",
      "point_id": "FAN-CB02",
      "rating": "400VAC / 40A",
      "type": "ELECTRICAL_AC"
    },
    {
      "location": "OVEN_CONTROL_DOOR",
      "point_id": "PID-CB03",
      "rating": "230VAC / 10A",
      "type": "CONTROL_AC"
    }
  ],
  "reference_facility": "FAC_GLOBAL_01",
  "regulatory_standard": "OSHA 29 CFR 1910.147",
  "sop_id": "LOTO-ELEC-05",
  "target_equipment_en": "Industrial Conveyor Drying Oven (180 kW Heating Bank), Solid State Relays (SSR) & Circulation Blower Fans",
  "target_equipment_vi": "Dàn sấy băng tải công nghiệp (Dàn điện trở gia nhiệt 180 kW), Bộ điều khiển bán dẫn SSR & Quạt quạt gió tuần hoàn",
  "title_en": "Industrial Electric Heating Element & Dry Oven Control Panel Isolation SOP",
  "title_vi": "Quy trình Cô lập Hệ thống gia nhiệt điện trở & Tủ sấy công nghiệp"
}

# Re-compute SHA-256 Hash
computed_hash = hashlib.sha256(
    json.dumps(payload_data, sort_keys=True, ensure_ascii=False).encode('utf-8')
).hexdigest()

expected_hash = "df29de46e3270148391e29cedabce411a1d46404311adfbea2006aa86e61c2b3"

print("=" * 70)
print("CMMS LOTO SOP INTEGRITY AUDIT")
print("=" * 70)
print(f"SOP ID:        LOTO-ELEC-05")
print(f"Expected Hash: {expected_hash}")
print(f"Computed Hash: {computed_hash}")
print(f"Match Result:  {computed_hash == expected_hash}")
print("=" * 70)
```

---
*Document produced as part of the Digital IP Assets Collection for One-Person Digital Enterprise.*
