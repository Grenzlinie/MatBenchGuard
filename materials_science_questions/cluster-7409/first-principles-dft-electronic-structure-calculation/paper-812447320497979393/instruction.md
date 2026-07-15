# Electronic structure and tight-binding modeling of LaNiO3 from first-principles DFT

## Problem background
The electronic structure of the perovskite oxide LaNiO3 is characterized by crystal-field splitting and covalent mixing between Ni 3d and O 2p orbitals. Understanding the energy positions and widths of antibonding, nonbonding, and bonding bands, and extracting the underlying tight-binding hopping interactions, is key to interpreting spectroscopic experiments and modelling charge‑transfer excitations in transition‑metal oxides. This task computes the density of states and band structure of LaNiO3 and derives a nearest‑neighbour Slater‑Koster tight‑binding description from the first‑principles results.

## Approach
Perform a scalar‑relativistic density‑functional theory (DFT) calculation for LaNiO3 using an open‑source plane‑wave code such as Quantum ESPRESSO, with the experimental rhombohedral crystal structure and standard pseudopotentials. From the self‑consistent calculation, obtain the total and projected (Ni 3d and O 2p) density of states and the electronic band structure along high‑symmetry paths. In the combined PDOS and band structure, identify four characteristic feature groups (labelled A, B, C, D) that correspond to antibonding eg*, nonbonding t2g*, nonbonding O 2p, and bonding bands. Determine the energy window (minimum and maximum energy) occupied by each feature. Then, fit a nearest‑neighbour Slater‑Koster tight‑binding model that includes Ni 3d and O 2p orbitals to the DFT band structure. The fit parametrizes the hopping integrals according to the Slater‑Koster scheme and yields the bare on‑site energy difference Δ = ε_d − ε_p.

## Reproduction target
From the computed band structure and projected density of states for LaNiO3:
- Identify the energy ranges (min, max) of the four DOS features A, B, C, D as defined by their orbital character and save them to `/app/outputs/dos_features.json`.
- Fit a nearest‑neighbour Slater‑Koster tight‑binding model to the DFT band structure and extract the hopping parameters ppσ, ppπ, pdσ, pdπ and the bare energy difference Δ = ε_d − ε_p. Save these values to `/app/outputs/tb_parameters.json`.

## Assets

- LaNiO3 crystal structure (rhombohedral perovskite): https://materialsproject.org/materials/mp-1008722
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: DFT calculation for LaNiO3
- Role: process
- Action: Perform a scalar-relativistic DFT calculation for LaNiO3 using an open-source plane-wave code (e.g., Quantum ESPRESSO). Use the experimental rhombohedral crystal structure and a converged k‑point mesh. Compute the total density of states, Ni 3d and O 2p projected density of states, and the band structure along high-symmetry directions.
- Evidence: `/app/outputs/dft_run.log`

### Step 2: Identify DOS features A, B, C, D
- Role: scored
- Action: From the computed PDOS and band structure, locate the four features A, B, C, D as defined in the original study. Determine the energy window (minimum and maximum) where each characteristic band group / PDOS peak appears. Save the bounds.
- Output file: `/app/outputs/dos_features.json`
- Format: json
- Contract: JSON object with keys: feature_A, feature_B, feature_C, feature_D. Each value is an object with 'min_energy' and 'max_energy' (float, in eV).
- Scoring: scored by hidden verifier

### Step 3: Fit Slater-Koster tight-binding model
- Role: scored (load-bearing)
- Action: Fit a nearest-neighbor Slater-Koster tight-binding model (including Ni 3d and O 2p orbitals) to the DFT band structure. Extract the hopping integrals and the bare on-site energy difference Δ = ε_d − ε_p. Save the fitted values.
- Output file: `/app/outputs/tb_parameters.json`
- Format: json
- Contract: JSON object with keys: pp_sigma (float), pp_pi (float), pd_sigma (float), pd_pi (float), bare_energy_d_minus_p (float). All values in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_features.json`
- `/app/outputs/tb_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_features.json
- path: `/app/outputs/dos_features.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy bounds of the four characteristic DOS features for LaNiO3.
- schema:
  - `type`: object
  - `required`:
    - `feature_A`:
      - `min_energy`: float (eV)
      - `max_energy`: float (eV)
    - `feature_B`:
      - `min_energy`: float (eV)
      - `max_energy`: float (eV)
    - `feature_C`:
      - `min_energy`: float (eV)
      - `max_energy`: float (eV)
    - `feature_D`:
      - `min_energy`: float (eV)
      - `max_energy`: float (eV)

### tb_parameters.json
- path: `/app/outputs/tb_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted Slater-Koster hopping parameters and the bare energy difference Δ = ε_d − ε_p.
- schema:
  - `type`: object
  - `required`:
    - `pp_sigma`: float (eV)
    - `pp_pi`: float (eV)
    - `pd_sigma`: float (eV)
    - `pd_pi`: float (eV)
    - `bare_energy_d_minus_p`: float (eV)

Notes: Scoring compares reported energy windows and TB parameters to hidden reference values with tolerances that account for DFT-code differences. Structural checks (sign and energy ordering) are also applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_features.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "feature_A": {
            "min_energy": "float (eV)",
            "max_energy": "float (eV)"
          },
          "feature_B": {
            "min_energy": "float (eV)",
            "max_energy": "float (eV)"
          },
          "feature_C": {
            "min_energy": "float (eV)",
            "max_energy": "float (eV)"
          },
          "feature_D": {
            "min_energy": "float (eV)",
            "max_energy": "float (eV)"
          }
        }
      },
      "description": "Energy bounds of the four characteristic DOS features for LaNiO3."
    },
    {
      "file": "tb_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pp_sigma": "float (eV)",
          "pp_pi": "float (eV)",
          "pd_sigma": "float (eV)",
          "pd_pi": "float (eV)",
          "bare_energy_d_minus_p": "float (eV)"
        }
      },
      "description": "Fitted Slater-Koster hopping parameters and the bare energy difference Δ = ε_d − ε_p."
    }
  ],
  "notes": "Scoring compares reported energy windows and TB parameters to hidden reference values with tolerances that account for DFT-code differences. Structural checks (sign and energy ordering) are also applied."
}
```

## How you are scored
A hidden verifier independently evaluates the artifact produced by each scored workflow stage (`dos_features.json` and `tb_parameters.json`) and combines the results into the final reward according to a predefined weight distribution. The verifier checks the correctness of the reported energy ranges and tight‑binding parameters against a reference derived from the original study. Reporting a number without faithful execution of the described steps will not produce a matching result.
