---
title: "OPL #01: Equipment Availability, MTBF & MTTR Standard Calculations"
date: 2026-11-15T08:00:00+07:00
draft: false
slug: "opl-01-equipment-availability-mtbf-mttr-standard-calculations"
tags: ["OPL", "CMRP", "SMRP-BoK", "Industrial-OT", "Equipment-Reliability"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Key mathematical formulation and implementation for Equipment Availability, MTBF, and MTTR."
bookToc: true
weight: 1
---

{{% hint info %}}
🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**  
`SHA256: 8caceca0b8e022ad1f5b7ea1790254b5063e1da4f1ced151ccc6a3c795073f98`

🌐 *Reference Model: `FAC_GLOBAL_01`. Zero NDA Risk Protocol.*
{{% /hint %}}

{{< katex >}}{{< /katex >}}


---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 2: Manufacturing Process Reliability` & `Pillar 3: Equipment Reliability`
- **Core Rule:** Operational Availability (\(A\)) quantifies the proportion of scheduled time physical assets remain in an operable state, governed directly by Reliability (MTBF) and Maintainability (MTTR).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Calculating downtime using subjective shift logs while ignoring micro-stoppages (<1 hour). | Capturing automated downtime from CMMS/SCADA logs, strictly separating unscheduled breakdown downtime from planned maintenance. |
| Treating maintenance as a reactive repair expenditure after functional failures occur. | Viewing reliability as the production of asset capacity, quantitatively managed via MTBF and MTTR metrics. |

---

### 📐 2. Mathematical Formulation & Micro Payload

\[
A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}} \times 100\% = \frac{T_{\text{operating}} - T_{\text{downtime}}}{T_{\text{operating}}} \times 100\%
\]

```python
# Industrial OT Quick-Calculations (Reference Model: FAC_GLOBAL_01)
def calculate_equipment_metrics(operating_hrs: float, downtime_hrs: float, failure_count: int) -> dict:
    """Calculates Availability, MTBF, and MTTR based on SMRP standard metrics for ASSET_REF_101."""
    if operating_hrs <= 0 or failure_count <= 0:
        return {"Availability (%)": 0.0, "MTBF (hrs)": 0.0, "MTTR (hrs)": 0.0}
    
    uptime_hrs = operating_hrs - downtime_hrs
    if uptime_hrs < 0:
        raise ValueError("Downtime cannot exceed total scheduled operating hours.")
        
    mtbf = round(uptime_hrs / failure_count, 2)
    mttr = round(downtime_hrs / failure_count, 2)
    availability = round((uptime_hrs / operating_hrs) * 100, 2)
    
    return {
        "Availability (%)": availability,
        "MTBF (hrs)": mtbf,
        "MTTR (hrs)": mttr
    }

# Quick Test for FAC_GLOBAL_01 Line 1
results = calculate_equipment_metrics(operating_hrs=720.0, downtime_hrs=18.0, failure_count=3)
print(results)
```

---

### 🧠 3. CMRP Active Recall Quiz

> **Question:** At facility `FAC_GLOBAL_01`, a production line operates 720 scheduled hours per month. The EAM system records 4 unscheduled technical breakdown events totaling 24 hours of unplanned downtime. What are the correct Mean Time Between Failures (MTBF) and Operational Availability (\(A\)) values according to SMRP standard definitions?
>
> - **A.** MTBF = 180.0 hrs, Availability = 96.67%
> - **B.** MTBF = 174.0 hrs, Availability = 96.67%
> - **C.** MTBF = 174.0 hrs, Availability = 95.00%
> - **D.** MTBF = 180.0 hrs, Availability = 95.00%

{{< details "Click to reveal Answer & Rationale" >}}
- **Correct Answer:** **B**
- **SMRP Rationale:** SMRP defines MTBF strictly on actual operating uptime (\(T_{\text{operating}} - T_{\text{downtime}}\)). Uptime = \(720 - 24 = 696\) hours. Therefore, \(\text{MTBF} = \frac{696}{4} = 174.0\) hours. Operational Availability \(A = \left(\frac{696}{720}\right) \times 100\% = 96.67\%\). Option A incorrectly utilizes gross scheduled hours (\(720/4 = 180\)) without subtracting downtime.
{{< /details >}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Automatically extract operating and downtime event logs for `ASSET_REF_101` from CMMS/SCADA databases.
- [ ] **Step 2:** Execute the automated Python payload to compute MTBF, MTTR, and Availability, streaming real-time metrics to Grafana.
- [ ] **Step 3:** Benchmark against SMRP baseline targets and trigger a Root Cause Analysis (RCA) workflow whenever Availability falls below 95.0%.

---

{{% hint warning %}}
**🚀 Need Industrial OT & Reliability Consulting?**

Looking to package OT Downtime Dashboards or standardize SMRP-compliant Maintenance Workflows?  
👉 **[Submit B2B Technical Request Here]({{< relref "/" >}}#tally-form-anchor)** *(Async response via Slack/Jira/Email in Technical English)*.
{{% /hint %}}
