# Lattice thermal conductivity of pyrochlore boron allotropes from first-principles

## Problem background
Pyrochlore lattices, built from corner‑sharing tetrahedra, are geometrically frustrated structures. Such frustration can give rise to flat bands in the phonon spectrum, which may strongly enhance phonon scattering and thereby reduce lattice thermal conductivity. This task investigates the lattice thermal transport of two hypothetical boron allotropes with pyrochlore‑related structures: a standard pyrochlore lattice (PL‑B4) and a pyrochlore‑like variant (PL‑B8). Using first‑principles density functional theory (DFT) and the phonon Boltzmann transport equation (BTE), we aim to compute their lattice thermal conductivity at room temperature and the branch‑averaged phonon scattering rates and group velocities for the transverse acoustic (TA1, TA2), longitudinal acoustic (LA), and optical branches. The computed quantities will reveal how phonon flat bands and potential band gaps influence thermal transport.

## Approach
The computational workflow replaces the proprietary VASP code used in the original study with the open‑source plane‑wave DFT package Quantum ESPRESSO. For each structure (PL‑B4 and PL‑B8) the workflow is:
1. Fully relax the atomic positions and lattice parameters with Quantum ESPRESSO.
2. Compute second‑order (harmonic) interatomic force constants via the finite‑displacement method using the phonopy package.
3. Compute third‑order (anharmonic) force constants with the thirdorder.py tool, distributed as part of the ShengBTE suite.
4. With both the harmonic and anharmonic force constants, solve the phonon Boltzmann transport equation iteratively using ShengBTE to obtain lattice thermal conductivity as a function of temperature, as well as mode‑resolved phonon lifetimes and group velocities.
5. From the ShengBTE output at 300 K, extract the total lattice thermal conductivity K_L and compute branch‑averaged scattering rates and group velocities for the acoustic branches (TA1, TA2, LA) and all optical branches combined.
The workflow is repeated independently for PL‑B4 and PL‑B8; the results are then compared to examine the effect of flat bands and phonon band gaps on thermal transport.

## Reproduction target
The primary goal is to produce two scored JSON files (one per structure) placed under `/app/outputs`.

Each file must contain three top‑level fields:
- `K_L_300K` (float): total lattice thermal conductivity at 300 K, in W/mK.
- `branch_scattering_rates` (object): branch‑averaged phonon scattering rates in ps⁻¹ with keys `TA1`, `TA2`, `LA`, `Optical`.
- `branch_group_velocities` (object): branch‑averaged phonon group velocities in km/s with keys `TA1`, `TA2`, `LA`, `Optical`.

The extracted quantities should correspond to the definitions used in the original study. In addition to the absolute values, the relative ordering of the thermal conductivity between the two structures, and the relative magnitudes of the scattering rates, should be consistent with the physical trends expected from the respective phonon band structures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: https://pypi.org/project/phonopy/
- thirdorder.py (ShengBTE distribution): https://www.shengbte.org/
- ShengBTE: https://www.shengbte.org/

## Workflow steps

### Step 1: Structural relaxation of PL-B4
- Role: process
- Action: Using Quantum ESPRESSO, optimize the atomic positions and lattice constant of PL-B4 (space group Fd-3m, conventional lattice constant 4.99 Å, primitive cell 4 atoms, atomic position 16d (0.625, 0.125, 0.125)). Produce a relaxed structure file.
- Evidence: `/app/outputs/pl_b4_relax.out`

### Step 2: Structural relaxation of PL-B8
- Role: process
- Action: Using Quantum ESPRESSO, optimize the atomic positions and lattice constant of PL-B8 (space group Fd-3m, conventional lattice constant 8.57 Å, primitive cell 8 atoms, atomic position 32e (0.570, 0.070, 0.070)). Produce a relaxed structure file.
- Evidence: `/app/outputs/pl_b8_relax.out`

### Step 3: Harmonic force constants for PL-B4
- Role: process
- Action: Use phonopy with Quantum ESPRESSO to compute second-order interatomic force constants for PL-B4. Use a suitable supercell and finite displacements. Output the FORCE_CONSTANTS file.
- Evidence: `/app/outputs/pl_b4_FORCE_CONSTANTS`

### Step 4: Harmonic force constants for PL-B8
- Role: process
- Action: Use phonopy with Quantum ESPRESSO to compute second-order interatomic force constants for PL-B8. Use a suitable supercell and finite displacements. Output the FORCE_CONSTANTS file.
- Evidence: `/app/outputs/pl_b8_FORCE_CONSTANTS`

### Step 5: Anharmonic force constants for PL-B4
- Role: process
- Action: Use thirdorder.py with Quantum ESPRESSO to compute third-order interatomic force constants for PL-B4. Use a suitable supercell and a cut-off distance as described in the paper. Output the FORCE_CONSTANTS_3RD file.
- Evidence: `/app/outputs/pl_b4_FORCE_CONSTANTS_3RD`

### Step 6: Anharmonic force constants for PL-B8
- Role: process
- Action: Use thirdorder.py with Quantum ESPRESSO to compute third-order interatomic force constants for PL-B8. Use a suitable supercell and a cut-off distance as described in the paper. Output the FORCE_CONSTANTS_3RD file.
- Evidence: `/app/outputs/pl_b8_FORCE_CONSTANTS_3RD`

### Step 7: Solve BTE for PL-B4
- Role: process
- Action: Run ShengBTE iteratively for PL-B4 using the harmonic and anharmonic force constants. Use a q-point grid that yields converged thermal conductivity and include 300 K in the temperature range. Produce the standard ShengBTE output files.
- Evidence: `/app/outputs/pl_b4_BTE.kappa_tensor`

### Step 8: Solve BTE for PL-B8
- Role: process
- Action: Run ShengBTE iteratively for PL-B8 using the harmonic and anharmonic force constants. Use a q-point grid that yields converged thermal conductivity and include 300 K in the temperature range. Produce the standard ShengBTE output files.
- Evidence: `/app/outputs/pl_b8_BTE.kappa_tensor`

### Step 9: Extract PL-B4 results
- Role: scored (load-bearing)
- Action: From the ShengBTE outputs for PL-B4 at 300 K, extract the total lattice thermal conductivity K_L (W/mK), branch-averaged scattering rates (ps⁻¹) for TA1, TA2, LA, and all optical branches, and branch-averaged group velocities (km/s) for the same branches. Write a JSON file /app/outputs/pl_b4_results.json.
- Output file: `/app/outputs/pl_b4_results.json`
- Format: json
- Contract: {"K_L_300K": float, "branch_scattering_rates": {"TA1": float, "TA2": float, "LA": float, "Optical": float}, "branch_group_velocities": {"TA1": float, "TA2": float, "LA": float, "Optical": float}}
- Scoring: scored by hidden verifier

### Step 10: Extract PL-B8 results
- Role: scored (load-bearing)
- Action: From the ShengBTE outputs for PL-B8 at 300 K, extract the total lattice thermal conductivity K_L (W/mK), branch-averaged scattering rates (ps⁻¹) for TA1, TA2, LA, and all optical branches (and optionally optical modes below the band gap), and branch-averaged group velocities (km/s) for the same branches. Write a JSON file /app/outputs/pl_b8_results.json.
- Output file: `/app/outputs/pl_b8_results.json`
- Format: json
- Contract: {"K_L_300K": float, "branch_scattering_rates": {"TA1": float, "TA2": float, "LA": float, "Optical": float}, "branch_group_velocities": {"TA1": float, "TA2": float, "LA": float, "Optical": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pl_b4_results.json`
- `/app/outputs/pl_b8_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pl_b4_results.json
- path: `/app/outputs/pl_b4_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed lattice thermal conductivity and branch-averaged properties for PL-B4 at 300 K. Checker compares against paper values.
- schema:
  - `type`: object
  - `required`:
    - `K_L_300K`: float (W/mK)
    - `branch_scattering_rates`: object
    - `branch_group_velocities`: object
  - `items`:
    - `branch_scattering_rates.TA1`: float (ps⁻¹)
    - `branch_scattering_rates.TA2`: float
    - `branch_scattering_rates.LA`: float
    - `branch_scattering_rates.Optical`: float
    - `branch_group_velocities.TA1`: float (km/s)
    - `branch_group_velocities.TA2`: float
    - `branch_group_velocities.LA`: float
    - `branch_group_velocities.Optical`: float
  - `units`:
    - `K_L_300K`: W/mK
    - `branch_scattering_rates.TA1`: ps⁻¹
    - `branch_scattering_rates.TA2`: ps⁻¹
    - `branch_scattering_rates.LA`: ps⁻¹
    - `branch_scattering_rates.Optical`: ps⁻¹
    - `branch_group_velocities.TA1`: km/s
    - `branch_group_velocities.TA2`: km/s
    - `branch_group_velocities.LA`: km/s
    - `branch_group_velocities.Optical`: km/s

### pl_b8_results.json
- path: `/app/outputs/pl_b8_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed lattice thermal conductivity and branch-averaged properties for PL-B8 at 300 K. Checker compares against paper values.
- schema:
  - `type`: object
  - `required`:
    - `K_L_300K`: float (W/mK)
    - `branch_scattering_rates`: object
    - `branch_group_velocities`: object
  - `items`:
    - `branch_scattering_rates.TA1`: float (ps⁻¹)
    - `branch_scattering_rates.TA2`: float
    - `branch_scattering_rates.LA`: float
    - `branch_scattering_rates.Optical`: float
    - `branch_group_velocities.TA1`: float (km/s)
    - `branch_group_velocities.TA2`: float
    - `branch_group_velocities.LA`: float
    - `branch_group_velocities.Optical`: float
  - `units`:
    - `K_L_300K`: W/mK
    - `branch_scattering_rates.TA1`: ps⁻¹
    - `branch_scattering_rates.TA2`: ps⁻¹
    - `branch_scattering_rates.LA`: ps⁻¹
    - `branch_scattering_rates.Optical`: ps⁻¹
    - `branch_group_velocities.TA1`: km/s
    - `branch_group_velocities.TA2`: km/s
    - `branch_group_velocities.LA`: km/s
    - `branch_group_velocities.Optical`: km/s

Notes: The two output files capture the main thermal conductivity result and the branch-averaged scattering rates/group velocities from Tables 1 and 2 of the paper. The agent must extract after completing the full DFT+BTE workflow. Tolerances and paper reference values are stored in the hidden grading spec.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pl_b4_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K_L_300K": "float (W/mK)",
          "branch_scattering_rates": "object",
          "branch_group_velocities": "object"
        },
        "items": {
          "branch_scattering_rates.TA1": "float (ps⁻¹)",
          "branch_scattering_rates.TA2": "float",
          "branch_scattering_rates.LA": "float",
          "branch_scattering_rates.Optical": "float",
          "branch_group_velocities.TA1": "float (km/s)",
          "branch_group_velocities.TA2": "float",
          "branch_group_velocities.LA": "float",
          "branch_group_velocities.Optical": "float"
        },
        "units": {
          "K_L_300K": "W/mK",
          "branch_scattering_rates.TA1": "ps⁻¹",
          "branch_scattering_rates.TA2": "ps⁻¹",
          "branch_scattering_rates.LA": "ps⁻¹",
          "branch_scattering_rates.Optical": "ps⁻¹",
          "branch_group_velocities.TA1": "km/s",
          "branch_group_velocities.TA2": "km/s",
          "branch_group_velocities.LA": "km/s",
          "branch_group_velocities.Optical": "km/s"
        }
      },
      "description": "Computed lattice thermal conductivity and branch-averaged properties for PL-B4 at 300 K. Checker compares against paper values."
    },
    {
      "file": "pl_b8_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K_L_300K": "float (W/mK)",
          "branch_scattering_rates": "object",
          "branch_group_velocities": "object"
        },
        "items": {
          "branch_scattering_rates.TA1": "float (ps⁻¹)",
          "branch_scattering_rates.TA2": "float",
          "branch_scattering_rates.LA": "float",
          "branch_scattering_rates.Optical": "float",
          "branch_group_velocities.TA1": "float (km/s)",
          "branch_group_velocities.TA2": "float",
          "branch_group_velocities.LA": "float",
          "branch_group_velocities.Optical": "float"
        },
        "units": {
          "K_L_300K": "W/mK",
          "branch_scattering_rates.TA1": "ps⁻¹",
          "branch_scattering_rates.TA2": "ps⁻¹",
          "branch_scattering_rates.LA": "ps⁻¹",
          "branch_scattering_rates.Optical": "ps⁻¹",
          "branch_group_velocities.TA1": "km/s",
          "branch_group_velocities.TA2": "km/s",
          "branch_group_velocities.LA": "km/s",
          "branch_group_velocities.Optical": "km/s"
        }
      },
      "description": "Computed lattice thermal conductivity and branch-averaged properties for PL-B8 at 300 K. Checker compares against paper values."
    }
  ],
  "notes": "The two output files capture the main thermal conductivity result and the branch-averaged scattering rates/group velocities from Tables 1 and 2 of the paper. The agent must extract after completing the full DFT+BTE workflow. Tolerances and paper reference values are stored in the hidden grading spec."
}
```

## How you are scored
A hidden scoring verifier will independently evaluate your submitted JSON files. It compares your reported `K_L_300K`, branch scattering rates, and group velocities against reference values using predetermined tolerances. The scoring is monotonic: for directional metrics, meeting or surpassing the reference within the tolerance earns full credit, and the reward degrades only when the result is worse. The verifier also checks qualitative trends (e.g., scattering rates in one structure substantially larger than the other, and the thermal conductivity ordering) as part of the scoring rubric. Each scored artifact contributes a weighted portion to the final reward, with the main thermal conductivity and scattering properties carrying the largest weight. You do not need to know the reference values or tolerances; simply execute the workflow accurately and report the computed numbers.
