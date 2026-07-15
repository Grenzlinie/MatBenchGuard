# Compute thermodynamic descriptors for (CuFeMnNi)₁₋ₓCrₓ high-entropy alloys

## Problem background
High-entropy alloys (HEAs) are multicomponent alloys that can form simple solid solution phases (FCC, BCC) rather than complex intermetallics. Their phase stability and microstructure are often predicted by empirical thermodynamic descriptors: mixing enthalpy (ΔH_mix), configurational entropy (ΔS_mix), the stability parameter Ω, atomic-size difference (δ), and valence electron concentration (VEC). This task computes these five descriptors for a series of (CuFeMnNi)₁₋ₓCrₓ alloys with varying Cr content, providing the quantitative basis to assess whether solid solution phases are expected to form.

## Approach
The computation follows standard HEA empirical formulas using the alloy's atomic fractions and tabulated elemental properties.

- ΔH_mix = Σ_{i<j} c_i c_j · Ω_ij, where Ω_ij (kJ mol⁻¹) is the binary mixing enthalpy parameter for the i–j pair.
- ΔS_mix = –R Σ c_i ln c_i, with the gas constant R = 8.314 J K⁻¹ mol⁻¹.
- Ω = (T · ΔS_mix) / |ΔH_mix| evaluated at T = 298 K.
- δ = 100 · √( Σ c_i (1 – r_i / ⟨r⟩)² ), where ⟨r⟩ = Σ c_i r_i is the average atomic radius.
- VEC = Σ c_i · (VEC)_i.

The alloy compositions are (CuFeMnNi)₁₋ₓCrₓ with x = 0, 0.05, 0.10, 0.15, 0.20, 0.25. The atomic fractions are: Cr = x, and Cu = Fe = Mn = Ni = (1 – x) / 4. All required elemental data (Ω_ij, atomic radii, VEC numbers) are provided in the Assets section.

## Reproduction target
Produce a CSV file containing the five thermodynamic parameters for all six alloy compositions, ordered by increasing Cr content. The output must follow the exact format described in the workflow step: columns Alloy, Cr_content, Delta_H_mix_kJ_mol, Delta_S_mix_J_K_mol, Omega, delta_percent, VEC. Your computed values will be compared to independently obtained reference values using a relative error metric.

## Assets
The elemental data needed for the calculations are given below; no external download is required.

**Binary mixing enthalpy parameters Ω_ij (kJ mol⁻¹)**  
Cu–Fe: 52, Cu–Mn: 16, Cu–Ni: 16, Cu–Cr: 48  
Fe–Mn: 0, Fe–Ni: –8, Fe–Cr: –4  
Mn–Ni: –32, Mn–Cr: 8  
Ni–Cr: –28

**Atomic radii (pm)**  
Cu: 128, Fe: 124, Mn: 135, Ni: 125, Cr: 128

**Valence electron counts**  
Cu: 11, Fe: 8, Mn: 7, Ni: 10, Cr: 6

**Gas constant**  
R = 8.314 J K⁻¹ mol⁻¹; use T = 298 K for the Ω parameter.

## Workflow steps

### Step 1: Compute thermodynamic parameters
- Role: scored (load-bearing)
- Action: Given the alloy compositions (atomic fractions: for (CuFeMnNi)₁₋ₓCrₓ, Cu=Fe=Mn=Ni=(1-x)/4, Cr=x, with x=0, 0.05, 0.1, 0.15, 0.2, 0.25) and the elemental data (binary mixing enthalpies, atomic radii, valence electron counts, and gas constant R=8.314 J/K/mol) provided in the instruction, compute for each alloy: mixing enthalpy ΔH_mix as sum over all i,j of c_i*c_j*ΔH_ij_mix (with ΔH_ij_mix for the Cu-Fe-Mn-Ni-Cr system given), configurational entropy ΔS_mix = -R Σ c_i ln c_i, stability parameter Ω = T ΔS_mix / |ΔH_mix| with T=298 K, atomic-size difference δ = 100 * sqrt( Σ c_i (1 - r_i / ⟨r⟩)² ), and valence electron concentration VEC = Σ c_i VEC_i. Write the results to CSV.
- Output file: `/app/outputs/thermodynamic_parameters.csv`
- Format: csv
- Contract: Header: Alloy,Cr_content,Delta_H_mix_kJ_mol,Delta_S_mix_J_K_mol,Omega,delta_percent,VEC. Alloy values as strings like '0%Cr','5%Cr', etc. Cr_content as float. All numeric fields as floats. One row per alloy, ordered by increasing Cr content.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_parameters.csv
- path: `/app/outputs/thermodynamic_parameters.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact: the computed thermodynamic descriptors for the six HEA compositions. The hidden checker recomputes the mean absolute relative error (MAPE) against the paper-reported values and awards partial credit based on MAPE.
- schema:
  - `type`: table
  - `required_columns`: `Alloy`, `Cr_content`, `Delta_H_mix_kJ_mol`, `Delta_S_mix_J_K_mol`, `Omega`, `delta_percent`, `VEC`
  - `description`: Columns: Alloy (string), Cr_content (float), Delta_H_mix_kJ_mol (float), Delta_S_mix_J_K_mol (float), Omega (float), delta_percent (float), VEC (float).

Notes: Scoring compares the agent's computed values to hidden paper reference values using mean absolute relative error (MAPE). Higher error reduces credit; the exact tolerance band is defined in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Alloy",
          "Cr_content",
          "Delta_H_mix_kJ_mol",
          "Delta_S_mix_J_K_mol",
          "Omega",
          "delta_percent",
          "VEC"
        ],
        "description": "Columns: Alloy (string), Cr_content (float), Delta_H_mix_kJ_mol (float), Delta_S_mix_J_K_mol (float), Omega (float), delta_percent (float), VEC (float)."
      },
      "description": "Scored artifact: the computed thermodynamic descriptors for the six HEA compositions. The hidden checker recomputes the mean absolute relative error (MAPE) against the paper-reported values and awards partial credit based on MAPE."
    }
  ],
  "notes": "Scoring compares the agent's computed values to hidden paper reference values using mean absolute relative error (MAPE). Higher error reduces credit; the exact tolerance band is defined in the hidden grading specification."
}
```

## How you are scored
A hidden verifier will read your thermodynamic_parameters.csv and compare each entry to a hidden reference (derived from the original research). It will compute a relative error metric across all alloys and all five parameters, then convert the overall deviation into a reward between 0 and 1. Smaller errors yield higher rewards; simply reporting the reference values without performing the correct composition-weighted computation will not be sufficient, as the verifier may also employ consistency checks. The result of this scored stage dominates the final reward.
