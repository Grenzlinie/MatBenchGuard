# Phonon transport properties of boron pyrochlore lattices

## Problem background
Pyrochlore lattices, characterized by corner-sharing tetrahedra, can host flat bands in their phonon spectra due to geometric frustration and lattice symmetry. Flat bands are regions where phonon frequencies change little with wavevector, leading to near-zero group velocities and potentially enhanced three-phonon scattering. These features can strongly influence lattice thermal conductivity. Two boron allotropes, PL-B4 (standard pyrochlore, primitive cell with 4 atoms) and PL-B8 (pyrochlore-like, primitive cell with 8 atoms where each lattice site is a dimer), provide a platform to study how flat bands and phonon band gaps together determine thermal transport in such lattices. The task is to compute the lattice thermal conductivity, branch-averaged phonon scattering rates, and branch-averaged group velocities for both structures at room temperature and to compare their thermal transport properties.

## Approach
The workflow uses first-principles density functional theory (DFT) within the generalized gradient approximation (GGA) to obtain structural relaxation and force constants. Starting from the crystallographic data of PL-B4 (space group Fd-3m (227), conventional lattice constant ~4.99 Å, primitive 3.53 Å, atomic position at Wyckoff 16d (0.625,0.125,0.125)) and PL-B8 (same space group, conventional 8.57 Å, primitive 6.06 Å, Wyckoff 32e (0.570,0.070,0.070)), geometry optimizations are performed to produce relaxed primitive cells. Second-order (harmonic) force constants are then obtained via finite displacements using phonopy, yielding phonon dispersions and mode-resolved group velocities. Third-order (anharmonic) force constants are computed with the thirdorder.py script on larger supercells. These force constants are fed into ShengBTE to solve the phonon Boltzmann transport equation iteratively, giving the lattice thermal conductivity tensor, phonon scattering rates, and relaxation times. Finally, the branch-averaged scattering rates and group velocities are extracted for the acoustic branches TA₁, TA₂, LA and the optical branch. The comparison between PL-B4 and PL-B8 reveals how flat bands and band gaps govern thermal transport.

## Reproduction target
For both PL-B4 and PL-B8, compute and report: (1) the total lattice thermal conductivity at 300 K (in W/mK); (2) the branch-averaged phonon scattering rates (in ps⁻¹) for branches TA₁, TA₂, LA, and Optical; (3) the branch-averaged phonon group velocities (in km/s) for the same four branches. Save each structure's results in separate JSON files as specified in the workflow steps. The evaluation verifies the computed quantities and their relative trends across the two structures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- phonopy: phonopy
- thirdorder.py: https://bitbucket.org/shengbte/thirdorder/src/master/
- ShengBTE: https://www.shengbte.org/
- Boron pseudopotential for Quantum ESPRESSO: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Structure optimization of PL-B4 and PL-B8
- Role: process
- Action: Using the provided atomic structures of PL-B4 (space group Fd-3m (227), conventional lattice constant ~4.99 Å, primitive 3.53 Å, Wyckoff position 16d (0.625,0.125,0.125)) and PL-B8 (same space group, conventional 8.57 Å, primitive 6.06 Å, Wyckoff position 32e (0.570,0.070,0.070)), perform DFT geometry optimization to obtain relaxed primitive cell structures.
- Evidence: none

### Step 2: Second-order force constants and phonon dispersion
- Role: process
- Action: From the relaxed primitive cells, create supercells and compute second-order interatomic force constants via finite displacements using phonopy coupled with DFT. Obtain phonon band structure and mode-resolved group velocities.
- Evidence: none

### Step 3: Third-order force constants
- Role: process
- Action: Using the relaxed structures, create supercells, generate displaced configurations with thirdorder.py, and compute third-order force constants via DFT. Post-process to obtain anharmonic force constants suitable for ShengBTE.
- Evidence: none

### Step 4: Solve Boltzmann transport equation for PL-B4
- Role: process
- Action: Prepare ShengBTE input using the second- and third-order force constants of PL-B4. Run ShengBTE iteratively on a converged q-point mesh to obtain mode-resolved scattering rates, relaxation times, group velocities, and the lattice thermal conductivity tensor.
- Evidence: none

### Step 5: Solve Boltzmann transport equation for PL-B8
- Role: process
- Action: Same as step_04 but for the PL-B8 structure.
- Evidence: none

### Step 6: Branch-averaged properties for PL-B4
- Role: scored (load-bearing)
- Action: From the ShengBTE output and mode group velocities, compute the branch-averaged scattering rates (ps⁻¹) and group velocities (km/s) for phonon branches TA₁, TA₂, LA, and Optical; also extract the total lattice thermal conductivity at 300 K. Save these values in a JSON file.
- Output file: `/app/outputs/step_04_results_PL-B4.json`
- Format: json
- Contract: { thermal_conductivity_300K: number (W/mK), branch_averaged_scattering_rates: { TA1: number (ps⁻¹), TA2: number, LA: number, Optical: number }, branch_averaged_group_velocities: { TA1: number (km/s), TA2: number, LA: number, Optical: number } }
- Scoring: scored by hidden verifier

### Step 7: Branch-averaged properties for PL-B8
- Role: scored (load-bearing)
- Action: Same as step_06 but for PL-B8.
- Output file: `/app/outputs/step_04_results_PL-B8.json`
- Format: json
- Contract: { thermal_conductivity_300K: number (W/mK), branch_averaged_scattering_rates: { TA1: number (ps⁻¹), TA2: number, LA: number, Optical: number }, branch_averaged_group_velocities: { TA1: number (km/s), TA2: number, LA: number, Optical: number } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_results_PL-B4.json`
- `/app/outputs/step_04_results_PL-B8.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_results_PL-B4.json
- path: `/app/outputs/step_04_results_PL-B4.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact that captures the main lattice thermal transport results for PL-B4.
- schema:
  - `type`: object
  - `properties`:
    - `thermal_conductivity_300K`:
      - `type`: number
      - `units`: W/mK
    - `branch_averaged_scattering_rates`:
      - `type`: object
      - `properties`:
        - `TA1`:
          - `type`: number
          - `units`: ps^-1
        - `TA2`:
          - `type`: number
          - `units`: ps^-1
        - `LA`:
          - `type`: number
          - `units`: ps^-1
        - `Optical`:
          - `type`: number
          - `units`: ps^-1
      - `required`: `TA1`, `TA2`, `LA`, `Optical`
    - `branch_averaged_group_velocities`:
      - `type`: object
      - `properties`:
        - `TA1`:
          - `type`: number
          - `units`: km/s
        - `TA2`:
          - `type`: number
          - `units`: km/s
        - `LA`:
          - `type`: number
          - `units`: km/s
        - `Optical`:
          - `type`: number
          - `units`: km/s
      - `required`: `TA1`, `TA2`, `LA`, `Optical`
  - `required`: `thermal_conductivity_300K`, `branch_averaged_scattering_rates`, `branch_averaged_group_velocities`

### step_04_results_PL-B8.json
- path: `/app/outputs/step_04_results_PL-B8.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact that captures the main lattice thermal transport results for PL-B8.
- schema:
  - `type`: object
  - `properties`:
    - `thermal_conductivity_300K`:
      - `type`: number
      - `units`: W/mK
    - `branch_averaged_scattering_rates`:
      - `type`: object
      - `properties`:
        - `TA1`:
          - `type`: number
          - `units`: ps^-1
        - `TA2`:
          - `type`: number
          - `units`: ps^-1
        - `LA`:
          - `type`: number
          - `units`: ps^-1
        - `Optical`:
          - `type`: number
          - `units`: ps^-1
      - `required`: `TA1`, `TA2`, `LA`, `Optical`
    - `branch_averaged_group_velocities`:
      - `type`: object
      - `properties`:
        - `TA1`:
          - `type`: number
          - `units`: km/s
        - `TA2`:
          - `type`: number
          - `units`: km/s
        - `LA`:
          - `type`: number
          - `units`: km/s
        - `Optical`:
          - `type`: number
          - `units`: km/s
      - `required`: `TA1`, `TA2`, `LA`, `Optical`
  - `required`: `thermal_conductivity_300K`, `branch_averaged_scattering_rates`, `branch_averaged_group_velocities`

Notes: The PL-B8 file may optionally include an additional field for the optical modes below the phonon band gap; the main contract only requires the average over all optical modes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_results_PL-B4.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "thermal_conductivity_300K": {
            "type": "number",
            "units": "W/mK"
          },
          "branch_averaged_scattering_rates": {
            "type": "object",
            "properties": {
              "TA1": {
                "type": "number",
                "units": "ps^-1"
              },
              "TA2": {
                "type": "number",
                "units": "ps^-1"
              },
              "LA": {
                "type": "number",
                "units": "ps^-1"
              },
              "Optical": {
                "type": "number",
                "units": "ps^-1"
              }
            },
            "required": [
              "TA1",
              "TA2",
              "LA",
              "Optical"
            ]
          },
          "branch_averaged_group_velocities": {
            "type": "object",
            "properties": {
              "TA1": {
                "type": "number",
                "units": "km/s"
              },
              "TA2": {
                "type": "number",
                "units": "km/s"
              },
              "LA": {
                "type": "number",
                "units": "km/s"
              },
              "Optical": {
                "type": "number",
                "units": "km/s"
              }
            },
            "required": [
              "TA1",
              "TA2",
              "LA",
              "Optical"
            ]
          }
        },
        "required": [
          "thermal_conductivity_300K",
          "branch_averaged_scattering_rates",
          "branch_averaged_group_velocities"
        ]
      },
      "description": "Scored artifact that captures the main lattice thermal transport results for PL-B4."
    },
    {
      "file": "step_04_results_PL-B8.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "thermal_conductivity_300K": {
            "type": "number",
            "units": "W/mK"
          },
          "branch_averaged_scattering_rates": {
            "type": "object",
            "properties": {
              "TA1": {
                "type": "number",
                "units": "ps^-1"
              },
              "TA2": {
                "type": "number",
                "units": "ps^-1"
              },
              "LA": {
                "type": "number",
                "units": "ps^-1"
              },
              "Optical": {
                "type": "number",
                "units": "ps^-1"
              }
            },
            "required": [
              "TA1",
              "TA2",
              "LA",
              "Optical"
            ]
          },
          "branch_averaged_group_velocities": {
            "type": "object",
            "properties": {
              "TA1": {
                "type": "number",
                "units": "km/s"
              },
              "TA2": {
                "type": "number",
                "units": "km/s"
              },
              "LA": {
                "type": "number",
                "units": "km/s"
              },
              "Optical": {
                "type": "number",
                "units": "km/s"
              }
            },
            "required": [
              "TA1",
              "TA2",
              "LA",
              "Optical"
            ]
          }
        },
        "required": [
          "thermal_conductivity_300K",
          "branch_averaged_scattering_rates",
          "branch_averaged_group_velocities"
        ]
      },
      "description": "Scored artifact that captures the main lattice thermal transport results for PL-B8."
    }
  ],
  "notes": "The PL-B8 file may optionally include an additional field for the optical modes below the phonon band gap; the main contract only requires the average over all optical modes."
}
```

## How you are scored
Your two output JSON files are scored by a hidden verifier. Each scored stage is evaluated independently against a hidden reference (values and/or relative trends) and assigned a fractional reward; the weighted sum across all scored stages yields the final reward ∈ [0,1]. The verifier does not simply compare your reported numbers to the paper's; it may also check structural consistency and direction of expected trends between the two structures. Exact tolerances and gold values are not disclosed. Producing an honest, physics-based result through the prescribed workflow is the only way to achieve a high score.
