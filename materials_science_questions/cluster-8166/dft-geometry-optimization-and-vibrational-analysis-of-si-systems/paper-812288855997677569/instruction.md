# Binding Energy Calculation for Si-Centered Tetrahedra in Amorphous SiOxNy Films

## Problem background
Amorphous silicon oxynitride (a‑SiOₓNᵧ) films are industrially important materials whose bonding structures remain poorly understood. A common approach models the network as a collection of Si‑centered tetrahedra, where each silicon atom is bonded to four atoms chosen from Si, O, and N. Depending on the composition, up to 15 distinct tetrahedral bonding units (Si–Si₄₋₍ᵥ₊₎OᵥN_η) can exist. X‑ray photoelectron spectroscopy (XPS) is used to probe the bonding environment via the Si 2p₃/₂ and N 1s core‑level binding energies, but assigning observed spectral features to specific tetrahedra requires reliable theoretical binding energies for each candidate unit. This task computes those expected binding energies for all 15 candidate tetrahedra using a practical scheme based on linear interpolation of reference energies and a partial‑charge model, providing a foundational ingredient for later spectral deconvolution.

## Approach
The Si 2p₃/₂ binding energy for each tetrahedron is determined by linear interpolation between the energies of well‑known reference phases, assuming the shift scales with the number of oxygen or nitrogen neighbours. Specifically:
- For tetrahedra of the series Si–Si₄₋ᵥOᵥ (v = 0…4), the energy ranges linearly from 99.6 eV (a‑Si) to 103.6 eV (SiO₂).
- For tetrahedra Si–OᵥN₄₋ᵥ (v = 0…4), it ranges from 102.0 eV (Si₃N₄) to 103.6 eV (SiO₂).
- For tetrahedra Si–SiOᵥN₃₋ᵥ (v = 0…3), it ranges from 101.4 eV (Si–SiN₃) to 102.6 eV (Si–SiO₃).

The N 1s binding‑energy shift (ΔE_B relative to Si₃N₄) is computed using a charge‑transfer model based on Sanderson electronegativities. Each tetrahedron is assigned a bonding unit Si_k O_m N_p whose composition follows from stoichiometric constraints. For this unit, the Sanderson electronegativity S_SiON is the geometric mean of the individual atomic electronegativities (S_Si = 2.84, S_O = 5.21, S_N = 4.49). The partial charge P_N on nitrogen is then P_N = (S_SiON − S_N) / (2.08 √S_N). The N 1s shift relative to Si₃N₄ is proportional to the change in P_N, with a proportionality constant of −11 eV per unit negative partial charge (a more negative P_N shifts the binding energy to a lower value). For tetrahedra containing no nitrogen, ΔE_B is undefined and should be left as NaN.

## Reproduction target
Calculate the Si 2p₃/₂ binding energy (eV) and the N 1s binding‑energy shift relative to Si₃N₄ (eV) for every one of the 15 candidate Si‑centered tetrahedra: Si–Si₄, Si–Si₃N, Si–Si₂O, Si–Si₂N₂, Si–Si₂ON, Si–SiN₃, Si–Si₂O₂, Si–SiON₂, Si–N₄, Si–SiO₂N, Si–N₃O, Si–SiO₃, Si–O₂N₂, Si–O₃N, Si–O₄. For tetrahedra without nitrogen, output a NaN for the N 1s shift. Write the results as a CSV file (`table_I_reproduction.csv`) with columns: tetrahedron_number (1–15), tetrahedron (e.g., 'Si–Si₄'), bonding_unit (e.g., 'Si'), EB_Si2p3_2 (eV), deltaEB_N1s (eV).

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Calculate binding energies for all 15 candidate tetrahedra
- Role: scored (load-bearing)
- Action: Compute the Si 2p₃/₂ binding energy (eV) and the N 1s binding-energy shift (ΔE_B) relative to Si₃N₄ (eV) for each of the 15 Si-centered tetrahedra listed in the paper's Table I, using the linear interpolation rules for Si 2p₃/₂ and the partial-charge model (Sanderson electronegativity mixing) for N 1s, with the given reference energies and electronegativities. Write the results as a CSV table with columns: tetrahedron_number, tetrahedron, bonding_unit, EB_Si2p3_2, deltaEB_N1s.
- Output file: `/app/outputs/table_I_reproduction.csv`
- Format: csv
- Contract: Columns: tetrahedron_number (int), tetrahedron (str), bonding_unit (str), EB_Si2p3_2 (float, eV), deltaEB_N1s (float, eV, may be NaN if no N present). 15 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_I_reproduction.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_I_reproduction.csv
- path: `/app/outputs/table_I_reproduction.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed binding energies and N 1s shifts for the 15 Si-centered tetrahedra. Values are deterministic given the public constants; comparison to hidden gold tolerates a small absolute deviation.
- schema:
  - `type`: table
  - `required_columns`: `tetrahedron_number`, `tetrahedron`, `bonding_unit`, `EB_Si2p3_2`, `deltaEB_N1s`
  - `items`: object
  - `required`: object
  - `units`:
    - `EB_Si2p3_2`: eV
    - `deltaEB_N1s`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_I_reproduction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tetrahedron_number",
          "tetrahedron",
          "bonding_unit",
          "EB_Si2p3_2",
          "deltaEB_N1s"
        ],
        "items": {},
        "required": {},
        "units": {
          "EB_Si2p3_2": "eV",
          "deltaEB_N1s": "eV"
        }
      },
      "description": "Computed binding energies and N 1s shifts for the 15 Si-centered tetrahedra. Values are deterministic given the public constants; comparison to hidden gold tolerates a small absolute deviation."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your CSV and compare each value of EB_Si2p3_2 and deltaEB_N1s to expected reference values. Your score is the fraction of computed values that fall within a small tolerance of the expected values, with deltaEB_N1s evaluated only for tetrahedra that contain nitrogen. The verifier does not inspect your code; only the CSV matters. Reporting any pre‑known numbers from an external source would be ineffective because the expected values are specific to the protocol described in this instruction.
