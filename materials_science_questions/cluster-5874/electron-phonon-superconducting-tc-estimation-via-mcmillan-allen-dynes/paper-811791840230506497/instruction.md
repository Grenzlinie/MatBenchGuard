# High-Pressure Phase Stability and Superconducting Tc Prediction of CaLi2

## Problem background
CaLi₂ is a binary compound of Li and Ca, both elements that exhibit anomalous superconductivity and electronic properties under pressure. Prior studies disagreed on whether CaLi₂ dissociates into elements at high pressure, and whether observed superconductivity arose from CaLi₂ or elemental Ca/Li. The present task aims to resolve the high-pressure phase diagram and explain the superconducting transition temperature of CaLi₂ through first-principles computational modeling.

## Approach
The computational workflow uses evolutionary crystal structure prediction (USPEX) to search for stable CaLi₂ structures in the pressure range 10–250 GPa, coupled with density functional theory (DFT) relaxations using Quantum ESPRESSO (PBE functional, PAW pseudopotentials). Enthalpy comparisons relative to the elemental phases determine phase stability. For the predicted stable structures, phonon and electron-phonon coupling (EPC) parameters are computed via density-functional perturbation theory (DFPT) to estimate the superconducting critical temperature Tc from the Allen-Dynes modified McMillan equation with Coulomb pseudopotential μ*=0.13.

## Reproduction target
Produce the enthalpy-pressure phase diagram of CaLi₂ for candidate structures (including decomposition into elements), identify the stability pressure ranges of the discovered phases, and calculate the superconducting Tc of CaLi₂ at 45 GPa.

## Assets

- USPEX (Universal Structure Predictor: Evolutionary Xtallography): https://uspex-team.org/uspex/
- Quantum ESPRESSO (pw.x, ph.x): https://www.quantum-espresso.org/
- PAW pseudopotentials for Li and Ca: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Evolutionary structure search and relaxation
- Role: process
- Action: Run USPEX evolutionary structure search for CaLi₂ in the pressure range 10–250 GPa using Quantum ESPRESSO as the DFT engine (PBE functional, PAW pseudopotentials). Use simulation cells containing 1, 2, 3, 4, 6, and 8 formula units. For each generated structure, perform variable-cell DFT relaxation to obtain total energy and enthalpy. Also relax elemental Ca and Li cells. Save a search log for provenance.
- Evidence: `/app/outputs/search_log.txt`

### Step 2: Enthalpy stability analysis
- Role: scored (load-bearing)
- Action: From the relaxed total energies of CaLi₂ candidate structures and the elemental reference states, compute enthalpy differences relative to decomposition into elements for each pressure. Identify the stable phases and their pressure intervals, and write a CSV table with columns: pressure (float, GPa), phase (str), enthalpy_per_fu (float, eV).
- Output file: `/app/outputs/enthalpy_curves.csv`
- Format: csv
- Contract: CSV with columns: pressure (float, GPa), phase (str identifying the structure), enthalpy_per_fu (float, eV per formula unit).
- Scoring: scored by hidden verifier

### Step 3: Extract relaxed C2/c structure
- Role: scored
- Action: From the search results, select the lowest-enthalpy monoclinic C2/c structure at a pressure near 36 GPa. Output its relaxed atomic coordinates, space group, and lattice parameters as a standard CIF file.
- Output file: `/app/outputs/C2_c_relaxed.cif`
- Format: txt
- Contract: Standard Crystallographic Information File (CIF) containing _symmetry_space_group_name_H-M, _cell_length_a/b/c, _cell_angle_alpha/beta/gamma, and _atom_site_* loops.
- Scoring: scored by hidden verifier

### Step 4: Extract relaxed P2₁/c structure
- Role: scored
- Action: From the search results, select the lowest-enthalpy monoclinic P2₁/c structure at a pressure near 55 GPa. Output its relaxed atomic coordinates, space group, and lattice parameters as a standard CIF file.
- Output file: `/app/outputs/P2_1_c_relaxed.cif`
- Format: txt
- Contract: Standard CIF containing _symmetry_space_group_name_H-M, _cell_length_a/b/c, _cell_angle_alpha/beta/gamma, and _atom_site_* loops.
- Scoring: scored by hidden verifier

### Step 5: Phonon and electron-phonon coupling calculation
- Role: process
- Action: Using density-functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO, compute phonon dispersions, the Eliashberg spectral function α²F(ω), the electron-phonon coupling constant λ, and the logarithmic average phonon frequency ω_log for the C2/c structure at 45 GPa. Save a summary (λ and ω_log) to an evidence file for the next step.
- Evidence: `/app/outputs/epc_summary.json`

### Step 6: Superconducting Tc estimation
- Role: scored (load-bearing)
- Action: Using the λ and ω_log obtained in the previous step, compute the superconducting critical temperature Tc for the C2/c phase at 45 GPa via the Allen-Dynes modified McMillan formula with a Coulomb pseudopotential μ* = 0.13. Write the Tc value (in Kelvin) to a text file.
- Output file: `/app/outputs/tc_at_45GPa.txt`
- Format: txt
- Contract: Plain text containing a single floating-point number representing Tc in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/enthalpy_curves.csv`
- `/app/outputs/C2_c_relaxed.cif`
- `/app/outputs/P2_1_c_relaxed.cif`
- `/app/outputs/tc_at_45GPa.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### enthalpy_curves.csv
- path: `/app/outputs/enthalpy_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Enthalpy-pressure curves for candidate CaLi₂ phases and the elemental reference states. Used to determine phase stability pressure ranges and the decomposition–recombination–decomposition sequence.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `phase`, `enthalpy_per_fu`
  - `units`:
    - `pressure`: GPa
    - `enthalpy_per_fu`: eV

### C2_c_relaxed.cif
- path: `/app/outputs/C2_c_relaxed.cif`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Relaxed crystal structure of the C2/c phase of CaLi₂. Verifier audits lattice parameters, space group, and key interatomic distances characteristic of the predicted structure.
- schema:
  - `type`: text

### P2_1_c_relaxed.cif
- path: `/app/outputs/P2_1_c_relaxed.cif`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Relaxed crystal structure of the P2₁/c phase of CaLi₂. Verifier audits lattice parameters, space group, and the presence of Li₂ graphene-like sheets and Li1 linear chains.
- schema:
  - `type`: text

### tc_at_45GPa.txt
- path: `/app/outputs/tc_at_45GPa.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Superconducting critical temperature Tc of CaLi₂ at 45 GPa computed from the Allen-Dynes formula with μ*=0.13.
- schema:
  - `type`: text

Notes: All outputs are produced by the computational workflow; the solving agent must execute the complete pipeline and write the specified artifacts. The verifier compares these artifacts against the paper's reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "enthalpy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "phase",
          "enthalpy_per_fu"
        ],
        "units": {
          "pressure": "GPa",
          "enthalpy_per_fu": "eV"
        }
      },
      "description": "Enthalpy-pressure curves for candidate CaLi₂ phases and the elemental reference states. Used to determine phase stability pressure ranges and the decomposition–recombination–decomposition sequence."
    },
    {
      "file": "C2_c_relaxed.cif",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Relaxed crystal structure of the C2/c phase of CaLi₂. Verifier audits lattice parameters, space group, and key interatomic distances characteristic of the predicted structure."
    },
    {
      "file": "P2_1_c_relaxed.cif",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Relaxed crystal structure of the P2₁/c phase of CaLi₂. Verifier audits lattice parameters, space group, and the presence of Li₂ graphene-like sheets and Li1 linear chains."
    },
    {
      "file": "tc_at_45GPa.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Superconducting critical temperature Tc of CaLi₂ at 45 GPa computed from the Allen-Dynes formula with μ*=0.13."
    }
  ],
  "notes": "All outputs are produced by the computational workflow; the solving agent must execute the complete pipeline and write the specified artifacts. The verifier compares these artifacts against the paper's reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. The enthalpy curves, relaxed crystal structures in CIF format, and the estimated Tc are compared to hidden reference values using appropriate tolerances and structural checks. Each scored artifact's reward is combined by weight into the final score. The verifier checks that the workflow produces correct phase stability ranges, structural parameters, and a Tc value consistent with the approach. Reporting paper-reported numbers without actual computation will not satisfy the verification.
