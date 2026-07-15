# Superconducting Tc of Mo4/3B2 and W4/3B2 via Electron-Phonon Coupling

## Problem background
Two-dimensional borides are of strong interest as potential phonon-mediated superconductors because the light boron atoms are expected to exhibit strong electron‑phonon coupling. A recently synthesized 2D boridene can be exfoliated into a Mo4/3B2 monolayer with a hexagonal P‑3m1 crystal structure. This task investigates whether the freestanding Mo4/3B2 monolayer is a conventional superconductor, what its critical temperature (Tc) is, and how that Tc changes under biaxial tensile strain and when molybdenum is replaced by tungsten (W4/3B2).

## Approach
Use density functional theory (DFT) with the open‑source Quantum ESPRESSO package and the SSSP efficiency pseudopotentials for Mo, B, and W. For each of the three materials (pristine Mo4/3B2, Mo4/3B2 under +5% biaxial tensile strain, and isostructural W4/3B2) perform the following conceptual workflow:

1. Relax the monolayer structure to obtain the equilibrium geometry.
2. Compute the phonon dispersion and the electronic density of states (DOS) at the Fermi level N(EF) using density‑functional perturbation theory (DFPT).
3. From the phonon linewidths and the phonon spectrum, calculate the Eliashberg electron‑phonon spectral function α²F(ω), the total electron‑phonon coupling constant λ, and the logarithmic average frequency ω_log via linear‑response theory.
4. Estimate the superconducting critical temperature Tc using the Allen–Dynes modified McMillan formula with an effective Coulomb pseudopotential μ* = 0.1.

The three cases are treated independently, each starting from an appropriate initial geometry (the P‑3m1 Mo4/3B2 monolayer with a≈5.14 Å; for the strained case, set the in‑plane lattice constant to 1.05 × the relaxed value; for W4/3B2, replace Mo by W and relax).

## Reproduction target
Compute and report the superconducting critical temperature Tc (in Kelvin) for each of the three systems using the DFT+DFPT+Allen‑Dynes procedure described above:
- Pristine Mo4/3B2 monolayer
- Mo4/3B2 monolayer under +5% biaxial tensile strain
- W4/3B2 monolayer (isostructural, with Mo fully replaced by W)

Produce three JSON files under /app/outputs, each containing exactly one key "Tc_K" with the calculated Tc as a floating‑point number.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax Mo4/3B2 monolayer
- Role: process
- Action: Perform full geometry relaxation of the hexagonal P-3m1 Mo4/3B2 monolayer using DFT, starting from an initial lattice constant of ~5.14 Å. Save the relaxed structure for subsequent steps.
- Evidence: `/app/outputs/relax_pristine.log`

### Step 2: Phonon and electronic structure of pristine Mo4/3B2
- Role: process
- Action: Compute the phonon dispersion (using DFPT) and the electronic density of states (DOS) at the Fermi level N(E_F) for the relaxed Mo4/3B2 monolayer. Output phonon frequencies, eigenvectors, and N(E_F).
- Evidence: `/app/outputs/phonon_dos_pristine.log`

### Step 3: Tc of pristine Mo4/3B2
- Role: scored (load-bearing)
- Action: Perform linear-response electron-phonon coupling calculation to obtain the total EPC constant λ and logarithmic average frequency ω_log. Compute Tc using the Allen-Dynes formula (μ*=0.1). Write the result to /app/outputs/pristine_Mo43B2_Tc.json.
- Output file: `/app/outputs/pristine_Mo43B2_Tc.json`
- Format: json
- Contract: {"Tc_K": float}
- Scoring: scored by hidden verifier

### Step 4: Relax Mo4/3B2 under +5% biaxial strain
- Role: process
- Action: Apply a +5% biaxial tensile strain to the monolayer (lattice constant a = 1.05 × a_eq) and perform a full DFT relaxation of the atomic positions. Save the strained geometry.
- Evidence: `/app/outputs/relax_strained.log`

### Step 5: Phonon and electronic structure of strained Mo4/3B2
- Role: process
- Action: Compute phonon dispersion and electronic DOS for the +5% strained monolayer, obtaining phonon frequencies, eigenvectors, and N(E_F).
- Evidence: `/app/outputs/phonon_dos_strained.log`

### Step 6: Tc of strained Mo4/3B2
- Role: scored (load-bearing)
- Action: Compute the EPC constant λ and ω_log for the strained monolayer, then Tc via the Allen-Dynes formula (μ*=0.1). Write the result to /app/outputs/strained_Mo43B2_Tc.json.
- Output file: `/app/outputs/strained_Mo43B2_Tc.json`
- Format: json
- Contract: {"Tc_K": float}
- Scoring: scored by hidden verifier

### Step 7: Relax W4/3B2 monolayer
- Role: process
- Action: Starting from the Mo4/3B2 geometry with Mo replaced by W, perform a full DFT relaxation of the W4/3B2 monolayer. Save the relaxed structure.
- Evidence: `/app/outputs/relax_W.log`

### Step 8: Phonon and electronic structure of W4/3B2
- Role: process
- Action: Compute phonon dispersion and electronic DOS for the relaxed W4/3B2 monolayer, obtaining phonon frequencies, eigenvectors, and N(E_F).
- Evidence: `/app/outputs/phonon_dos_W.log`

### Step 9: Tc of W4/3B2
- Role: scored (load-bearing)
- Action: Compute λ and ω_log for W4/3B2, then Tc (μ*=0.1). Write the result to /app/outputs/W43B2_Tc.json.
- Output file: `/app/outputs/W43B2_Tc.json`
- Format: json
- Contract: {"Tc_K": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_Mo43B2_Tc.json`
- `/app/outputs/strained_Mo43B2_Tc.json`
- `/app/outputs/W43B2_Tc.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_Mo43B2_Tc.json
- path: `/app/outputs/pristine_Mo43B2_Tc.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature of pristine Mo4/3B2 monolayer.
- schema:
  - `type`: object
  - `required`: `Tc_K`
  - `properties`:
    - `Tc_K`:
      - `type`: number
      - `unit`: K

### strained_Mo43B2_Tc.json
- path: `/app/outputs/strained_Mo43B2_Tc.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature of Mo4/3B2 monolayer under +5% biaxial strain.
- schema:
  - `type`: object
  - `required`: `Tc_K`
  - `properties`:
    - `Tc_K`:
      - `type`: number
      - `unit`: K

### W43B2_Tc.json
- path: `/app/outputs/W43B2_Tc.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Superconducting critical temperature of W4/3B2 monolayer.
- schema:
  - `type`: object
  - `required`: `Tc_K`
  - `properties`:
    - `Tc_K`:
      - `type`: number
      - `unit`: K

Notes: Each Tc value will be compared to the paper-reported value with a hidden tolerance (±0.5 K). Additionally, the three Tc values must satisfy the ordering: Tc(W4/3B2) < Tc(pristine Mo4/3B2) < Tc(strained Mo4/3B2). Full reward requires all three within tolerance and the correct ordering.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_Mo43B2_Tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Tc_K"
        ],
        "properties": {
          "Tc_K": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Superconducting critical temperature of pristine Mo4/3B2 monolayer."
    },
    {
      "file": "strained_Mo43B2_Tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Tc_K"
        ],
        "properties": {
          "Tc_K": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Superconducting critical temperature of Mo4/3B2 monolayer under +5% biaxial strain."
    },
    {
      "file": "W43B2_Tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Tc_K"
        ],
        "properties": {
          "Tc_K": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Superconducting critical temperature of W4/3B2 monolayer."
    }
  ],
  "notes": "Each Tc value will be compared to the paper-reported value with a hidden tolerance (±0.5 K). Additionally, the three Tc values must satisfy the ordering: Tc(W4/3B2) < Tc(pristine Mo4/3B2) < Tc(strained Mo4/3B2). Full reward requires all three within tolerance and the correct ordering."
}
```

## How you are scored
An automated verifier will evaluate your three output files. For each case, the verifier compares your reported Tc against a hidden reference value (derived from the source calculation) with a predetermined tolerance. The verifier also checks that the three Tc values obey a required ordering relationship across the three conditions. Each output contributes to the final reward according to a predefined weighting. Simply reporting the published Tc values without executing the full workflow will not satisfy the scoring requirements; you must perform the calculations to produce the artifacts.
