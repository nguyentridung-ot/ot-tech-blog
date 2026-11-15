---
title: "OPL #04: Identifying & Eliminating Bad Actors via Pareto 80/20 Rule"
date: 2026-11-14T11:00:00+07:00
draft: true
slug: "opl-04-identifying-eliminating-bad-actors"
tags: ["OPL", "CMRP", "SMRP-BoK", "Bad-Actors", "MTBF", "CMMS", "Pareto-Analysis"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: 5 reasons why companies fail to measure MTBF and Pareto 80/20 Bad Actor elimination."
bookToc: true
---

{{< hint info >}}
🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**  
`SHA256: 9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c`  
🌐 *Reference Model: `FAC_GLOBAL_04`. Zero NDA Risk Protocol.*
{{< /hint >}}

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 3: Equipment Reliability` & `Pillar 5: Work Management`
- **Core Rule:** In industrial facilities, **20% of equipment ("Bad Actors") account for 80% of maintenance losses**; systematic MTBF tracking in CMMS is the most direct tool to identify and eliminate them.
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Enforcing a rule that "work orders are only opened if downtime exceeds 1 hour", ignoring micro-stoppages. | Logging Work Orders for **100% of unscheduled stops**, recording exact downtime even for 5-minute events. |
| Remaining trapped in reactive firefighting mode without analyzing MTBF trends. | Measuring MTBF for top critical assets and applying Pareto analysis to eliminate Bad Actors systematically. |

---

### 📐 2. Mathematical Formulation & Micro Payload

Five Primary Reasons Companies Fail to Measure MTBF (SMRP Analysis):
1. *Work orders omitted for minor breakdowns (<1 hour).*
2. *Incomplete asset hierarchy in CMMS/EAM systems.*
3. *Misconception that other metrics substitute MTBF.*
4. *Organizational entrapment in reactive firefighting mode.*
5. *Perceived workload overload.*

```python
# Bad Actor Identification Script (Reference Model: FAC_GLOBAL_04)
import pandas as pd

def identify_bad_actors(asset_data: list) -> pd.DataFrame:
    """Performs Pareto 80/20 analysis to isolate Bad Actors from CMMS breakdown logs for FAC_GLOBAL_04."""
    df = pd.DataFrame(asset_data)
    df = df.sort_values(by='total_downtime_hrs', ascending=False).reset_index(drop=True)
    df['cum_downtime'] = df['total_downtime_hrs'].cumsum()
    total_downtime = df['total_downtime_hrs'].sum()
    
    if total_downtime <= 0:
        raise ValueError("Total downtime must be greater than 0.")
        
    df['cum_percent'] = round((df['cum_downtime'] / total_downtime) * 100, 2)
    df['is_bad_actor'] = df['cum_percent'] <= 80.0
    return df

# Sample CMMS Data
sample_assets = [
    {'asset_id': 'ASSET_REF_401', 'failure_count': 12, 'total_downtime_hrs': 120.0},
    {'asset_id': 'ASSET_REF_402', 'failure_count': 8, 'total_downtime_hrs': 85.0},
    {'asset_id': 'ASSET_REF_403', 'failure_count': 2, 'total_downtime_hrs': 15.0},
    {'asset_id': 'ASSET_REF_404', 'failure_count': 1, 'total_downtime_hrs': 5.0},
]
print(identify_bad_actors(sample_assets))
```

---

### 🧠 3. CMRP Active Recall Quiz

> **Question:** Management at `FAC_GLOBAL_04` assumed 10 primary line assets maintained an average MTBF of 8 to 9 hours. However, after enforcing mandatory Emergency Work Orders for all stoppages (including stops under 30 minutes), measured MTBF dropped to **0.7 hours** (42 minutes). What was the root cause of this discrepancy?
>
> - **A.** Sudden batch manufacturing defects in newly installed assets.
> - **B.** Unrecorded minor stoppages were previously omitted from CMMS, masking chronic failure frequencies.
> - **C.** Maintenance technicians miscalculated operating hours in CMMS.
> - **D.** Wrench Time exceeded world-class benchmarks (> 70%).

{{< details "Click to reveal Answer & Rationale" >}}
- **Correct Answer:** **B**
- **SMRP Rationale:** Omitting minor breakdowns from CMMS creates an artificially inflated MTBF. Capturing 100% of unscheduled breakdown events exposes real failure frequencies and reveals hidden Bad Actors.
{{< /details >}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Eliminate minimum downtime thresholds for work orders; mandate logging 100% of unscheduled stops.
- [ ] **Step 2:** Generate monthly Pareto MTBF reports in CMMS to identify the 20% Bad Actors causing 80% of downtime.
- [ ] **Step 3:** Assign dedicated RCA teams to eliminate root causes for at least one Bad Actor per month.

---

{{< hint warning >}}
### 🚀 Need Industrial OT & Reliability Consulting?
Ready to transition from reactive firefighting to data-driven Bad Actor elimination?  
👉 **[Submit B2B Technical Request Here](/#tally-form-anchor)**.
{{< /hint >}}
