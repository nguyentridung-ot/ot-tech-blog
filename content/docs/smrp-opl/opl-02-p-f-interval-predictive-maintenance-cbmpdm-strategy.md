---
title: "OPL #02: P-F Interval & Predictive Maintenance (CBM/PdM) Strategy"
date: 2026-11-15T09:00:00+07:00
draft: false
slug: "opl-02-p-f-interval-predictive-maintenance-cbmpdm-strategy"
tags: ["OPL", "CMRP", "SMRP-BoK", "P-F-Interval", "Predictive-Maintenance", "CBM"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Managing the P-F Interval, detecting Potential Failures (P), and scheduling CBM/PdM inspections."
bookToc: true
weight: 2
---

{{% hint info %}}
🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**  
`SHA256: e065a8c47995b1d6bcd8423b7d628460f020e8251e800ad794bf85d05b7cd239`  
🌐 *Reference Model: `FAC_GLOBAL_02`. Zero NDA Risk Protocol.*
{{% /hint %}}

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 2: Manufacturing Process Reliability` & `Pillar 3: Equipment Reliability`
- **Core Rule:** Over 80% of asset failures follow random patterns; optimizing CBM/PdM inspection frequencies must be based on the P-F Interval to detect Potential Failures (\(P\)) prior to Functional Failures (\(F\)).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Waiting for equipment to exhibit audible noise or total failure before initiating repair actions. | Monitoring vibration, thermography, or ultrasound to detect micro-faults at Point \(P\) on the P-F Curve. |
| Scheduling fixed calendar PMs (e.g., every 30 days) regardless of asset health condition. | Setting CBM/PdM inspection frequency to half or less of the P-F Interval (\(I \le \frac{\text{P-F}}{2}\)). |

---

### 📐 2. Mathematical Formulation & Micro Payload

{{< katex display=true >}}
\[
I_{\text{inspection}} \le \frac{\text{P-F Interval}}{2}
\]
{{< /katex >}}

```python
# P-F Interval Inspection Scheduler (Reference Model: FAC_GLOBAL_02)
def calculate_pdm_inspection_schedule(pf_interval_days: float, asset_criticality: int) -> dict:
    """Calculates PdM inspection frequency based on P-F Interval and Asset Criticality for ASSET_REF_202."""
    if pf_interval_days <= 0:
        raise ValueError("P-F Interval must be greater than 0.")
    
    # SMRP Guideline: Inspection frequency <= 1/2 P-F Interval; critical assets (Score >= 8) use 1/3 P-F Interval
    divider = 3.0 if asset_criticality >= 8 else 2.0
    recommended_frequency_days = round(pf_interval_days / divider, 1)
    
    return {
        "P-F Interval (days)": pf_interval_days,
        "Asset Criticality Score": asset_criticality,
        "Max Inspection Frequency (days)": recommended_frequency_days,
        "Safety Window (days)": round(pf_interval_days - recommended_frequency_days, 1)
    }

# Quick Test for Compressor ASSET_REF_202 (P-F Interval = 30 days for bearing wear)
pdm_plan = calculate_pdm_inspection_schedule(pf_interval_days=30.0, asset_criticality=9)
print(pdm_plan)
```

---

### 🧠 3. CMRP Active Recall Quiz

> **Question:** Vibration spectrum analysis on compressor `ASSET_REF_202` detects early bearing spalling (Point \(P\)) with an estimated P-F Interval of 30 days before total seizure (Point \(F\)). To reliably catch this failure condition before functional breakdown occurs, what is the optimal SMRP-compliant CBM inspection frequency?
>
> - **A.** Every 40 days
> - **B.** Every 30 days
> - **C.** Every 10 to 15 days
> - **D.** Only when bearing temperature exceeds 80°C

{{% details "Click to reveal Answer & Rationale" %}}
- **Correct Answer:** **C**
- **SMRP Rationale:** SMRP best practices dictate that CBM inspection intervals must not exceed half of the P-F Interval {{< katex display=true >}} (\(I \le \frac{\text{P-F}}{2} = 15\text{ days}\)) {{< /katex >}}. An inspection interval of 10 to 15 days provides at least one full inspection opportunity within the safety window. Options A and B risk missing the failure entirely, while temperature rise (Option D) occurs near the very end of the P-F curve adjacent to Point \(F\).
{{% /details %}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Map applicable PdM technologies (Vibration, Infrared, Oil Analysis, Ultrasound) to specific failure modes.
- [ ] **Step 2:** Build a P-F Interval matrix across critical equipment assets and establish inspection cycles {{< katex display=true >}} \(I \le \frac{\text{P-F}}{2}\).{{< /katex >}}
- [ ] **Step 3:** Trigger an automated Planned Work Order in CMMS upon Point \(P\) detection to perform corrective action within the Reliability Window.

---

{{% hint warning %}}
**🚀 Need Industrial OT & Reliability Consulting?**
Looking to deploy automated Condition-Based Monitoring (CBM) integrated with IoT sensors and CMMS?  
👉 **[Submit B2B Technical Request Here]({{< relref "/" >}}#tally-form-anchor)** *(Async response via Slack/Jira/Email in Technical English)*.
{{% /hint %}}

