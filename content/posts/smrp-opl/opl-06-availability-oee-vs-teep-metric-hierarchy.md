---
title: "OPL #06: Measuring Availability in OEE vs TEEP (SMRP Metric Hierarchy)"
date: 2026-11-14T13:00:00+07:00
draft: true
slug: "opl-06-availability-oee-vs-teep-metric-hierarchy"
tags: ["OPL", "CMRP", "SMRP-BoK", "OEE", "TEEP", "Asset-Utilization", "Metric-Hierarchy"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Differentiating OEE (scheduled time) from TEEP (24/7/365 asset utilization) via the Metric Hierarchy."
bookToc: true
---

{{< hint info >}}
🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**  
`SHA256: 1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e`  
🌐 *Reference Model: `FAC_GLOBAL_06`. Zero NDA Risk Protocol.*
{{< /hint >}}

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 2: Manufacturing Process Reliability` & `Pillar 1: Business & Management`
- **Core Rule:** **OEE** evaluates manufacturing performance during scheduled operating time, whereas **TEEP (*Total Effective Equipment Performance*)** measures total asset capacity utilization over 24/7/365 (8,760 hours/year).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Confusing OEE with TEEP; reporting 85% OEE while equipment sits idle 50% of total annual hours. | Reporting OEE for operational optimization while presenting TEEP to executive leadership to reflect asset capacity utilization. |
| Using unaligned metrics across departments causing conflicts between Maintenance and Operations. | Aligning indicators via the **SMRP Metric Hierarchy**: Strategic (RONA/ROCE) \(\rightarrow\) Operational (OEE/TEEP) \(\rightarrow\) Tactical (MTBF/MTTR/Wrench Time). |

---

### 📐 2. Mathematical Formulation & Micro Payload

\\[
\text{OEE (\%)} = \text{Availability} \times \text{Performance} \times \text{Quality}
\\]
\\[
\text{TEEP (\%)} = \text{Asset Utilization} \times \text{OEE} = \left(\frac{T_{\text{Scheduled}}}{8760\text{ hrs}}\right) \times \text{OEE}
\\]

```python
# OEE & TEEP Metric Engine (Reference Model: FAC_GLOBAL_06)
def calculate_oee_and_teep(total_year_hrs: float, scheduled_hrs: float, 
                           operating_hrs: float, ideal_cycle_min: float, 
                           total_pieces: int, good_pieces: int) -> dict:
    """Calculates OEE and TEEP metrics according to the SMRP Metric Hierarchy for FAC_GLOBAL_06."""
    if scheduled_hrs <= 0 or total_pieces <= 0:
        raise ValueError("Scheduled hours and total pieces must be greater than 0.")
        
    availability = operating_hrs / scheduled_hrs
    operating_min = operating_hrs * 60.0
    performance = (ideal_cycle_min * total_pieces) / operating_min
    quality = good_pieces / total_pieces
    
    oee = availability * performance * quality
    utilization = scheduled_hrs / total_year_hrs
    teep = utilization * oee
    
    return {
        "Availability (%)": round(availability * 100, 2),
        "Performance (%)": round(performance * 100, 2),
        "Quality (%)": round(quality * 100, 2),
        "OEE (%)": round(oee * 100, 2),
        "Asset Utilization (%)": round(utilization * 100, 2),
        "TEEP (%)": round(teep * 100, 2),
        "Hidden Factory Gap (%)": round((oee - teep) * 100, 2)
    }

# Quick Test: Line operating 16 hrs/day, 300 days/year (4,800 scheduled hrs / 8,760 total hrs)
print(calculate_oee_and_teep(total_year_hrs=8760, scheduled_hrs=4800, operating_hrs=4320, 
                             ideal_cycle_min=1.0, total_pieces=240000, good_pieces=230000))
```

---

### 🧠 3. CMRP Active Recall Quiz

> **Question:** A manufacturing line at `FAC_GLOBAL_06` is scheduled to operate 16 hours/day, 5 days/week (4,160 scheduled hours/year out of 8,760 total calendar hours). During scheduled production, the line achieves an 80.0% OEE. What is the annual Total Effective Equipment Performance (TEEP)?
>
> - **A.** 80.0%
> - **B.** 37.99%
> - **C.** 50.0%
> - **D.** 95.0%

{{< details "Click to reveal Answer & Rationale" >}}
- **Correct Answer:** **B**
- **SMRP Rationale:** Asset Utilization = $\frac{4160}{8760} = 47.49\%$. $\text{TEEP} = \text{Utilization} \times \text{OEE} = 47.49\% \times 80.0\% = 37.99\%$. Option A mistakes OEE for total annual asset utilization.
{{< /details >}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Report **OEE** to Operations and Maintenance teams for shift performance optimization.
- [ ] **Step 2:** Report **TEEP** to C-Level executive leadership to evaluate total physical asset capital efficiency.
- [ ] **Step 3:** Apply the SMRP Metric Hierarchy to trace tactical maintenance KPIs (MTBF, MTTR, Wrench Time) up to strategic financial goals (RONA, ROCE).

---

{{< hint warning >}}
### 🚀 Need Industrial OT & Reliability Consulting?
Looking to build real-time OEE/TEEP dashboards aligned with the SMRP Metric Hierarchy?  
👉 **[Submit B2B Technical Request Here](/#tally-form-anchor)**.
{{< /hint >}}
