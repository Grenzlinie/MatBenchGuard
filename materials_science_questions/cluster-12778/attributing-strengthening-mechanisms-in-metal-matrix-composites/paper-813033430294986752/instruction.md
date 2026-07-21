# Attributing Strengthening Mechanisms in Metal Matrix Composites

## Problem background
Ferritic steels strengthened by nanoscale oxide dispersions are attractive for high-temperature structural applications in nuclear reactors. Alloying with hafnium can promote the formation of Hf–O nanoparticles, providing dispersion strengthening. The total hardness of such alloys arises from a combination of mechanisms: dispersion (Orowan) strengthening and grain boundary (Hall‑Petch) strengthening. Understanding the relative contributions of each is essential for optimizing alloy design. This task concerns a Fe‑14Cr‑0.22Hf alloy consolidated by spark plasma sintering. Your goal is to quantify these strengthening contributions from microstructural data and mechanical constants.

## Approach
The total hardening is defined as the difference between the measured hardness of the alloy and the hardness of a reference Fe‑14Cr material (which contains no nanoscale dispersoids). The Orowan dispersion hardening is computed using the classical Orowan equation. For each region identified by atom probe tomography (high cluster density, low cluster density, and cluster‑free), the partial Orowan hardening is given by

H_O = 3√3 ⋅ ( ln(d / r₀) / ln(L / r₀) )^{3/2} ⋅ (G b / (2π L)) ⋅ ln(L / r₀)

where d is the particle diameter, L is the mean inter‑particle spacing, G is the shear modulus, b is the Burgers vector, and r₀ is the dislocation core radius. The overall Orowan hardening is obtained as a volume‑fraction‑weighted sum of the partial contributions. Finally, the Hall‑Petch grain boundary hardening is found by subtracting the total Orowan hardening from the total hardening.

## Reproduction target
Given the microstructural parameters (alloy hardness, base alloy hardness, cluster statistics for each region, and mechanical constants) provided in the first workflow step, compute the three hardening contributions: total hardening (alloy hardness minus base hardness), Orowan dispersion hardening (via the weighted summation described above), and Hall‑Petch hardening (total minus Orowan). Write these three values to a CSV file with the specified columns and formatting.

## Assets
No external assets are required. All input data, material constants, and the Orowan equation are provided directly in this instruction. You may use any standard scientific computing library (e.g., NumPy) to perform the calculations.

## Workflow steps

### Step 1: Compute strengthening contributions
- Role: scored
- Action: Using the provided microstructural parameters (alloy hardness 2.31 GPa, base Fe-14Cr hardness 1.74 GPa; APT cluster data: high density region – number density 2.37e23 m^{-3}, mean Guinier diameter 2.34 nm, mean intercluster distance 14.43 nm, volume fraction 0.35; low density region – number density 0.83e23 m^{-3}, diameter 3.64 nm, intercluster distance 17.81 nm, volume fraction 0.27; no clusters region volume fraction 0.38; constants: shear modulus G=82 GPa, Burgers vector b=0.384 nm, dislocation core radius r0=1.536 nm; Orowan equation (Eq. 1) as given in the paper), compute the partial Orowan hardening for each region, calculate the volume-weighted total Orowan hardening, compute total hardening = alloy hardness - base hardness, and then Hall-Petch hardening = total hardening - total Orowan. Write the three values to hardening_contributions.csv.
- Output file: `/app/outputs/hardening_contributions.csv`
- Format: csv
- Contract: columns: total_hardening_GPa, orowan_hardening_GPa, hall_petch_hardening_GPa; one row with three numeric values
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hardening_contributions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hardening_contributions.csv
- path: `/app/outputs/hardening_contributions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Hardening decomposition: total, Orowan, and Hall-Petch contributions to hardness in GPa.
- schema:
  - `type`: table
  - `required_columns`: `total_hardening_GPa`, `orowan_hardening_GPa`, `hall_petch_hardening_GPa`
  - `units`:
    - `total_hardening_GPa`: GPa
    - `orowan_hardening_GPa`: GPa
    - `hall_petch_hardening_GPa`: GPa

Notes: All inputs are provided in the instruction; no external resources needed. The checker compares each computed value against the paper’s reported results (derived from the same inputs) with an absolute tolerance of 0.001 GPa.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hardening_contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_hardening_GPa",
          "orowan_hardening_GPa",
          "hall_petch_hardening_GPa"
        ],
        "units": {
          "total_hardening_GPa": "GPa",
          "orowan_hardening_GPa": "GPa",
          "hall_petch_hardening_GPa": "GPa"
        }
      },
      "description": "Hardening decomposition: total, Orowan, and Hall-Petch contributions to hardness in GPa."
    }
  ],
  "notes": "All inputs are provided in the instruction; no external resources needed. The checker compares each computed value against the paper’s reported results (derived from the same inputs) with an absolute tolerance of 0.001 GPa."
}
```

## How you are scored
Your submission is evaluated by an automated verifier. The verifier reads your CSV file and extracts the three numeric values. It compares each to a hidden gold standard that was derived from the same input data using the same computational procedure. The reward is based on how closely your computed values match the gold values, within a tolerance appropriate for numerical precision. You must produce exactly one row with three numbers and exactly the required column headers. Success depends on correctly implementing the Orowan equation and the volume‑weighted summation, not on guessing the final numbers.