# Fracture Mechanics: Critical Nucleation Lengths for Hydraulic-Fracture-Induced Slip

## Problem background
When a hydraulic fracture propagates along a fault that obeys slip-weakening friction, the reduction in normal stress can trigger fault slip. Under certain conditions, this slip may become unstable and nucleate a dynamic (seismic) rupture. The stability depends on the background shear stress on the fault relative to its peak and residual frictional strengths. This task investigates the conditions for nucleation by determining the critical hydraulic fracture half-length and the accompanying slipping patch half-length as functions of the fault’s background shear stress, specifically for a case where the friction drops from a peak value to a finite residual level. The key open problem is to compute the threshold at which the quasi‑static slip growth becomes unbounded.

## Approach
The reproduction involves two coupled numerical components. First, the effective normal stress perturbation induced on the fault by a plane‑strain hydraulic fracture is obtained from the self‑similar solution for a zero‑toughness, zero‑leak‑off hydraulic fracture driven by a constant injection rate. This solution provides the normal stress profile ahead of the fracture tip as a function of the fracture half‑length. Second, the stress profile is used as input to a quasi‑static slip model. The fault’s shear stress is governed by a linear slip‑weakening friction law: the friction coefficient decreases linearly with slip from its peak value to a residual value. The slip distribution is solved by enforcing elastic equilibrium on the crack surface. For a given background shear stress, the hydraulic fracture half‑length is gradually increased, and the corresponding quasi‑static slipping patch half‑length is computed. The instability threshold is identified by the condition that the slipping patch growth diverges (da/dℓ → ∞). The analysis is carried out for a fixed loading factor and a fixed ratio of residual to peak friction.

## Reproduction target
Produce a CSV file (`critical_lengths.csv`) with the normalized critical hydraulic fracture half‑length ℓ_c/a_w and critical slipping patch half‑length a_c/a_w as functions of the normalized fault understress (τ_p − τ_0)/τ_p. The simulation must cover a range of understress values from at least 0.05 up to 0.6, using a residual‑to‑peak friction ratio f_r/f_p = 0.6 and a hydraulic‑fracture loading factor λ = 0.2. For points where the background shear stress τ_0 is less than or equal to the residual strength τ_r (i.e., understress ≥ 0.4), the slip should remain stable and no finite instability is found; in those rows the critical length columns should be left empty or contain the string 'stable'. The critical lengths at instability are expected to evolve with understress; the exact trend is the subject of the computation.

## Assets

- Python scientific computing stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Hydraulic fracture self-similar solution
- Role: process
- Action: Compute the normalized effective normal stress perturbation Π(ξ) and opening profile Ω(ξ) for a zero-toughness, zero-leak-off hydraulic fracture, using the self-similar solution of Adachi & Detournay (2002). Produce the effective stress distribution along the fault as a function of the normalized distance x/ℓ, for use in the slip simulation. The result must correspond to a loading factor λ=0.2 (equation 23 in the paper) when the hydraulic fracture half-length equals the characteristic slip length a_w.
- Evidence: `/app/outputs/hf_stress_profile.txt`

### Step 2: Critical nucleation lengths
- Role: scored (load-bearing)
- Action: Using the effective stress perturbation from the previous step, solve the quasi-static elastic equilibrium equations coupled with linear slip-weakening friction (peak coefficient f_p, residual coefficient f_r=0.6f_p, slip-weakening distance δ_w). For a range of normalized background shear stress τ_0/τ_p spanning from 0.95 to just above 0.6 (τ_r/τ_p=0.6), with loading factor λ=0.2, gradually increase the hydraulic fracture half-length ℓ until the slipping patch growth becomes unstable (da/dℓ → ∞ in the quasi-static model). Record the normalized critical hydraulic fracture half-length ℓ_c/a_w and critical slipping patch half-length a_c/a_w at the instability for each understress value (τ_p-τ_0)/τ_p. For background stress values τ_0 ≤ τ_r (i.e., understress ≥ 0.4), the slip remains stable and no finite instability is found; leave the length columns empty or write 'stable'.
- Output file: `/app/outputs/critical_lengths.csv`
- Format: csv
- Contract: CSV with header: understress_normalized, critical_HF_length, critical_slip_length. All values are floats for unstable cases; for understress ≥ 0.4 entries may be empty or the string 'stable'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_lengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_lengths.csv
- path: `/app/outputs/critical_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical hydraulic fracture half-length and slipping patch half-length as a function of fault understress, verifying the stability boundary τ_0=τ_r.
- schema:
  - `type`: table
  - `required_columns`: `understress_normalized`, `critical_HF_length`, `critical_slip_length`
  - `description`: Columns: understress_normalized (float, (τ_p-τ_0)/τ_p), critical_HF_length (float or empty/string 'stable'), critical_slip_length (float or empty/string 'stable').

Notes: The checker compares the reported critical lengths at several understress values to hidden reference data derived from the paper's Figure 10, and confirms that for understress ≥ 0.4 the agent reports stable slip (empty or 'stable'). Trends are also verified (divergence near τ_r, vanishing near τ_p).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "understress_normalized",
          "critical_HF_length",
          "critical_slip_length"
        ],
        "description": "Columns: understress_normalized (float, (τ_p-τ_0)/τ_p), critical_HF_length (float or empty/string 'stable'), critical_slip_length (float or empty/string 'stable')."
      },
      "description": "Critical hydraulic fracture half-length and slipping patch half-length as a function of fault understress, verifying the stability boundary τ_0=τ_r."
    }
  ],
  "notes": "The checker compares the reported critical lengths at several understress values to hidden reference data derived from the paper's Figure 10, and confirms that for understress ≥ 0.4 the agent reports stable slip (empty or 'stable'). Trends are also verified (divergence near τ_r, vanishing near τ_p)."
}
```

## How you are scored
A hidden verifier will independently evaluate each workflow stage. For the scored stage, it will read your `critical_lengths.csv` and compare the reported critical lengths at a predefined set of understress points against hidden reference (gold) values. The verifier will also check that you correctly report stable slip behaviour for understress ≥ 0.4. The verifier does not disclose the gold values; scoring is based on agreement within a tolerance, as well as on the correct identification of stable vs. unstable regimes. The final reward is a weighted combination of the scores from all stages.
