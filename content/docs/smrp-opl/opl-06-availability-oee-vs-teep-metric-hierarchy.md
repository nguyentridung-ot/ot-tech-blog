---
title: "OPL #06: Measuring Availability in OEE vs TEEP (SMRP Metric Hierarchy)"
date: 2026-11-16T06:41:18+07:00
draft: false
slug: "opl-06-availability-oee-vs-teep-metric-hierarchy"
tags: ["OPL", "CMRP", "SMRP-BoK", "OEE", "TEEP", "Asset-Utilization", "Metric-Hierarchy"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Differentiating OEE (scheduled time) from TEEP (24/7/365 asset utilization) via the Metric Hierarchy."
bookToc: true
weight: 6
lastmod: 2026-11-16T06:41:18+07:00
---

> [!NOTE]
> 🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**
>
> `SHA256: af349e39a5a646791f701f3579dded13688487312f357caf8668e223b0ed3833`
>
> 🌐 *Reference Model: `FAC_GLOBAL_06`. Zero NDA Risk Protocol.*

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 2: Manufacturing Process Reliability` & `Pillar 1: Business & Management`
- **Core Rule:** **OEE** evaluates manufacturing performance during scheduled operating time, whereas **TEEP (*Total Effective Equipment Performance*)** measures total asset capacity utilization over 24/7/365 (8,760 hours/year).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Confusing OEE with TEEP; reporting 85% OEE while equipment sits idle 50% of total annual hours. | Reporting OEE for operational optimization while presenting TEEP to executive leadership to reflect asset capacity utilization. |
| Using unaligned metrics across departments causing conflicts between Maintenance and Operations. | Aligning indicators via the **SMRP Metric Hierarchy**: Strategic (RONA/ROCE) {{< katex >}} \rightarrow {{< /katex >}} Operational (OEE/TEEP) {{< katex >}} \rightarrow {{< /katex >}} Tactical (MTBF/MTTR/Wrench Time). |

---

### 📐 2. Mathematical Formulation & Micro Payload

{{< katex displayMode=true >}}
\text{OEE (\%)} = \text{Availability} \times \text{Performance} \times \text{Quality}
{{< /katex >}}

{{< katex displayMode=true >}}
\text{TEEP (\%)} = \text{Asset Utilization} \times \text{OEE} = \left(\frac{T_{\text{Scheduled}}}{8760\text{ hrs}}\right) \times \text{OEE}
{{< /katex >}}

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

{{% details "Click to reveal Answer & Rationale" %}}

- **Correct Answer:** **B**
- **SMRP Rationale:** Asset Utilization = {{< katex >}} \frac{4160}{8760} = 47.49\% {{< /katex >}}. {{< katex >}} \text{TEEP} = \text{Utilization} \times \text{OEE} = 47.49\% \times 80.0\% = 37.99\% {{< /katex >}}. Option A mistakes OEE for total annual asset utilization.

{{% /details %}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Report **OEE** to Operations and Maintenance teams for shift performance optimization.
- [ ] **Step 2:** Report **TEEP** to C-Level executive leadership to evaluate total physical asset capital efficiency.
- [ ] **Step 3:** Apply the SMRP Metric Hierarchy to trace tactical maintenance KPIs (MTBF, MTTR, Wrench Time) up to strategic financial goals (RONA, ROCE).

---

> [!WARNING]
> **🚀 Need Industrial OT & Reliability Consulting?**
>
> Looking to build real-time OEE/TEEP dashboards aligned with the SMRP Metric Hierarchy?
>
> 👉 **[Submit B2B Technical Request Here]({{< relref "/" >}}#tally-form-anchor)**.
