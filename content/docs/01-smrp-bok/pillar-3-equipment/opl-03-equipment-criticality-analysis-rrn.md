---
title: "OPL #03: Equipment Criticality Analysis (ECA) & Relative Risk Number (RRN)"
date: 2026-11-16T06:34:08+07:00
draft: false
slug: "opl-03-equipment-criticality-analysis-rrn"
tags: ["OPL", "CMRP", "SMRP-BoK", "Equipment-Criticality", "ECA", "RRN", "Risk-Management"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Assessing Equipment Criticality (ECA), Total Consequence (TC), and Relative Risk Number (RRN)."
bookToc: true
weight: 3
lastmod: 2026-11-16T06:34:08+07:00
---

> [!NOTE]
> 🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**
>
> `SHA256: fb2aaccee61ae57952f975b8bbfdba62c2d6d76a1169dc9ad512941d91fe3247`
>
> 🌐 *Reference Model: `FAC_GLOBAL_03`. Zero NDA Risk Protocol.*

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 3: Equipment Reliability` & `Pillar 1: Business & Management`
- **Core Rule:** Equipment Criticality Analysis (ECA) replaces subjective opinions with engineering risk quantification, multiplying Total Consequence ({{< katex >}} TC {{< /katex >}}) by Failure Probability ({{< katex >}} F/P {{< /katex >}}) to derive the Relative Risk Number ({{< katex >}} RRN {{< /katex >}}).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Assigning criticality based on emotional claims or operator complaints ("every machine is 100% critical"). | Evaluating standardized criteria across Safety ({{< katex >}} S {{< /katex >}}), Environment ({{< katex >}} E {{< /katex >}}), Quality ({{< katex >}} Q {{< /katex >}}), Throughput ({{< katex >}} T {{< /katex >}}), Customer Service ({{< katex >}} CS {{< /katex >}}), and Cost ({{< katex >}} OC {{< /katex >}}). |
| Prioritizing maintenance solely based on breakdown frequency ({{< katex >}} F/P {{< /katex >}}). | Combining Total Consequence ({{< katex >}} TC {{< /katex >}}) with Failure Probability ({{< katex >}} F/P {{< /katex >}}) to compute {{< katex >}} RRN = TC \times (F/P) {{< /katex >}}. |

---

### 📐 2. Mathematical Formulation & Micro Payload

{{< katex displayMode=true >}}
TC = S + E + Q + T + CS + OC
{{< /katex >}}

{{< katex displayMode=true >}}
RRN = TC \times (F/P)
{{< /katex >}}

```python
# Equipment Criticality & RRN Calculator (Reference Model: FAC_GLOBAL_03)
def calculate_equipment_criticality(consequences: dict, failure_freq_score: float) -> dict:
    """Calculates Total Consequence (TC), Criticality Level, and RRN score for ASSET_REF_303."""
    required_keys = ['Safety', 'Environment', 'Quality', 'Throughput', 'CustomerService', 'OperatingCost']
    tc = sum(consequences.get(k, 0) for k in required_keys)
    rrn = round(tc * failure_freq_score, 2)
    
    # SMRP ECA Classification Logic (Scale 1-9)
    if tc >= 38 or consequences.get('Safety', 0) >= 10 or consequences.get('Environment', 0) >= 10:
        crit_num = 9
    elif tc >= 28:
        crit_num = 8
    elif tc >= 20:
        crit_num = 7
    elif tc >= 16:
        crit_num = 6
    else:
        crit_num = 5
        
    return {
        "Total Consequence (TC)": tc,
        "Failure Frequency Score (F/P)": failure_freq_score,
        "Relative Risk Number (RRN)": rrn,
        "Equipment Criticality Number (1-9)": crit_num,
        "Nominated for Reliability Project": rrn >= 150.0
    }

# Quick Test for Chemical Pump ASSET_REF_303
scores = {'Safety': 10, 'Environment': 8, 'Quality': 6, 'Throughput': 8, 'CustomerService': 4, 'OperatingCost': 6}
print(calculate_equipment_criticality(scores, failure_freq_score=6.5))
```

---

### 🧠 3. CMRP Active Recall Quiz

> **Question:** Two physical assets at `FAC_GLOBAL_03` are evaluated:  
> - **Asset A (Auxiliary Air Blower):** {{< katex >}} TC = 12 {{< /katex >}}, failure frequency {{< katex >}} F/P = 9 {{< /katex >}}, resulting in {{< katex >}} RRN = 108 {{< /katex >}}.  
> - **Asset B (Toxic Chemical Pump):** {{< katex >}} TC = 40 {{< /katex >}} (due to critical safety & environmental hazards), failure frequency {{< katex >}} F/P = 3 {{< /katex >}}, resulting in {{< katex >}} RRN = 120 {{< /katex >}}.  
>
> When allocating capital for a Reliability Improvement Project, which asset must receive priority under SMRP guidelines?
>
> - **A.** Asset A due to higher failure frequency ({{< katex >}} F/P = 9 {{< /katex >}}).
> - **B.** Asset B due to higher Relative Risk Number ({{< katex >}} RRN = 120 {{< /katex >}}) and catastrophic safety/environmental consequences.
> - **C.** Neither asset because both have {{< katex >}} RRN \lt 200 {{< /katex >}}.
> - **D.** Divide budget equally without ranking.

{{% details "Click to reveal Answer & Rationale" %}}

- **Correct Answer:** **B**
- **SMRP Rationale:** SMRP ECA methodology prioritizes risk over raw failure frequency. Asset B has a higher {{< katex >}} RRN {{< /katex >}} (120 vs 108) and carries severe safety/environmental consequences ({{< katex >}} TC = 40 {{< /katex >}}), requiring immediate engineering intervention over high-frequency, low-consequence assets.

{{% /details %}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Standardize the Equipment Hierarchy down to System and Equipment levels in CMMS.
- [ ] **Step 2:** Form a cross-functional evaluation team (Maintenance, Operations, HSE, Quality) to score {{< katex >}} TC {{< /katex >}} and {{< katex >}} F/P {{< /katex >}}.
- [ ] **Step 3:** Rank assets by {{< katex >}} RRN {{< /katex >}} and isolate the Top 20% highest-risk assets for targeted RCM/FMEA improvement projects.

---

> [!WARNING]
> **🚀 Need Industrial OT & Reliability Consulting?**
>
> Need technical assistance in establishing ECA Risk Matrices and RRN scoring models for your facility?
>
> 👉 **[Submit B2B Technical Request Here]({{< relref "/" >}}#tally-form-anchor)**.
