---
title: "OPL #03: Equipment Criticality Analysis (ECA) & Relative Risk Number (RRN)"
date: 2026-11-14T10:00:00+07:00
draft: true
slug: "opl-03-equipment-criticality-analysis-rrn"
tags: ["OPL", "CMRP", "SMRP-BoK", "Equipment-Criticality", "ECA", "RRN", "Risk-Management"]
categories: ["One-Point Lessons"]
series: ["SMRP Body of Knowledge"]
description: "SMRP BoK One-Point Lesson: Assessing Equipment Criticality (ECA), Total Consequence (TC), and Relative Risk Number (RRN)."
bookToc: true
---

{{< hint info >}}
🔒 **SECURITY & INTEGRITY CHECKSUM (SHA-256):**  
`SHA256: 8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b`  
🌐 *Reference Model: `FAC_GLOBAL_03`. Zero NDA Risk Protocol.*
{{< /hint >}}

---

### 📌 1. Atomic Core Concept

- **SMRP Pillar:** `Pillar 3: Equipment Reliability` & `Pillar 1: Business & Management`
- **Core Rule:** Equipment Criticality Analysis (ECA) replaces subjective opinions with engineering risk quantification, multiplying Total Consequence (\(TC\)) by Failure Probability (\(F/P\)) to derive the Relative Risk Number (\(RRN\)).
- **Comparison Table:**

| Anti-Pattern (Common Mistake) | SMRP Best Practice |
| :--- | :--- |
| Assigning criticality based on emotional claims or operator complaints ("every machine is 100% critical"). | Evaluating standardized criteria across Safety (\(S\)), Environment (\(E\)), Quality (\(Q\)), Throughput (\(T\)), Customer Service (\(CS\)), and Cost (\(OC\)). |
| Prioritizing maintenance solely based on breakdown frequency (\(F/P\)). | Combining Total Consequence (\(TC\)) with Failure Probability (\(F/P\)) to compute \(RRN = TC \times (F/P)\). |

---

### 📐 2. Mathematical Formulation & Micro Payload

\\[
TC = S + E + Q + T + CS + OC
\\]
\\[
RRN = TC \times (F/P)
\\]

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
> - **Asset A (Auxiliary Air Blower):** \(TC = 12\), failure frequency \(F/P = 9\), resulting in \(RRN = 108\).  
> - **Asset B (Toxic Chemical Pump):** \(TC = 40\) (due to critical safety & environmental hazards), failure frequency \(F/P = 3\), resulting in \(RRN = 120\).  
> When allocating capital for a Reliability Improvement Project, which asset must receive priority under SMRP guidelines?
>
> - **A.** Asset A due to higher failure frequency (\(F/P = 9\)).
> - **B.** Asset B due to higher Relative Risk Number (\(RRN = 120\)) and catastrophic safety/environmental consequences.
> - **C.** Neither asset because both have \(RRN < 200\).
> - **D.** Divide budget equally without ranking.

{{< details "Click to reveal Answer & Rationale" >}}
- **Correct Answer:** **B**
- **SMRP Rationale:** SMRP ECA methodology prioritizes risk over raw failure frequency. Asset B has a higher \(RRN\) (120 vs 108) and carries severe safety/environmental consequences (\(TC = 40\)), requiring immediate engineering intervention over high-frequency, low-consequence assets.
{{< /details >}}

---

### 🎯 4. Industrial OT Actionable Checklist

- [ ] **Step 1:** Standardize the Equipment Hierarchy down to System and Equipment levels in CMMS.
- [ ] **Step 2:** Form a cross-functional evaluation team (Maintenance, Operations, HSE, Quality) to score \(TC\) and \(F/P\).
- [ ] **Step 3:** Rank assets by \(RRN\) and isolate the Top 20% highest-risk assets for targeted RCM/FMEA improvement projects.

---

{{< hint warning >}}
### 🚀 Need Industrial OT & Reliability Consulting?
Need technical assistance in establishing ECA Risk Matrices and RRN scoring models for your facility?  
👉 **[Submit B2B Technical Request Here](/#tally-form-anchor)**.
{{< /hint >}}
