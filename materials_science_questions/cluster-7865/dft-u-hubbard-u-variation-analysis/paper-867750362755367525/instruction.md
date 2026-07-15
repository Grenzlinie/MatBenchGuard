# DFT+U Study of Strain-Driven Magnetic Transitions in a 2D Magnetic Bilayer

## Problem background
Two-dimensional magnetic materials, such as monolayer and few-layer chromium triiodide (CrI₃), exhibit tunable magnetic ordering that is sensitive to the stacking arrangement and external stimuli like strain. In a bilayer with the high-temperature C2/m stacking, each layer is ferromagnetically ordered, while the interlayer magnetic coupling can be either ferromagnetic or antiferromagnetic and can be tuned by strain and other external factors. Understanding how biaxial in-plane strain alters this magnetic order is important because strain can serve as a control knob for magnetic phase transitions in van der Waals heterostructures. The key physical quantities of interest are: (1) the relative total energies of different collinear spin configurations under strain, which determine the magnetic ground state and critical strains for phase transitions; (2) the intralayer and interlayer magnetic exchange couplings that underpin the ordering; (3) the associated Curie temperature; and (4) the energy cost of rotating the magnetization of one layer relative to the other (layer-constrained magnetic anisotropy). This task aims to compute these quantities for the C2/m bilayer CrI₃ system using first-principles methods.

## Approach
We will model the C2/m bilayer CrI₃ with lattice constant a=b=6.9 Å and interlayer spacing 6.6 Å. Three collinear magnetic configurations will be considered: (i) antiferromagnetic coupling between layers (↑↑/↓↓, interlayer-AF); (ii) ferromagnetic coupling between layers (↑↑/↑↑, FM); and (iii) antiferromagnetic coupling within each layer (↑↓/↑↓, intralayer-AF). For biaxial in-plane strains ranging from -6% to +6% in steps no larger than 1%, the total energy of each configuration will be obtained using density-functional theory (DFT) with the PBE exchange-correlation functional, an on-site Hubbard U correction (U=3 eV) on Cr 3d orbitals, and a van der Waals dispersion correction. The calculations will be performed with the open-source OpenMX DFT package. From these total energies, the ground-state configuration and critical strains for phase transitions will be inferred. Using the magnetic force theorem as implemented in OpenMX, the intralayer and interlayer exchange coupling parameters J will be extracted. Those J values will then be fed into Metropolis Monte Carlo simulations of a 2D Ising model to compute the Curie temperature as a function of strain. Finally, noncollinear DFT calculations within the local spin-density approximation (LSDA) including spin-orbit coupling will be carried out for strains of -5%, 0%, and +5%. In these calculations, the magnetization of the bottom layer is held fixed along the out-of-plane direction while the magnetization of the top layer is rotated from 0° to 180° in steps of at most 15°, and the total energy relative to the collinear FM state is recorded to obtain the layer-constrained magnetic anisotropy energy (LC-MAE).

## Reproduction target
Produce three scored output files placed under `/app/outputs`:

1. `phase_energies.json` – an array of objects, each containing the biaxial strain value and the total energies (in meV per unit cell) of the three collinear magnetic configurations (interlayer-AF, FM, intralayer-AF) relative to the interlayer-AF configuration at 0% strain.

2. `exchange_tc.json` – an array of objects, each containing the strain, the intralayer exchange coupling J_intra (meV), the first and second interlayer exchange couplings J_inter_first and J_inter_second (meV), and the Curie temperature Tc (K) estimated from the Ising model simulations.

3. `lc_mae.json` – an array of objects, each containing the strain (-5%, 0%, +5%), the rotation angle of the top-layer magnetization (degrees, from 0° to 180°), and the corresponding energy (meV per unit cell) relative to the FM (collinear ↑↑/↑↑) state at that strain.

The computed values will be evaluated against physical expectations derived from the same computational protocol.

## Assets

- OpenMx DFT package: https://www.openmx-square.org/
- C2/m bilayer CrI3 crystal structure
- Python scientific packages: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Prepare bilayer structure and magnetic configurations
- Role: process
- Action: Generate DFT input files for the C2/m bilayer CrI3 at biaxial strains from -6% to +6% in steps of at most 1%, for the three collinear magnetic configurations: interlayer-AF (↑↑/↓↓), FM (↑↑/↑↑), and intralayer-AF (↑↓/↑↓). Use lattice constant a=b=6.9 Å, interlayer spacing 6.6 Å, and atomic positions consistent with C2/m symmetry.
- Evidence: none

### Step 2: DFT total energies for strain-dependent magnetic phases
- Role: scored (load-bearing)
- Action: Perform DFT+U calculations with OpenMx using PBE functional, Hubbard U=3 eV, and van der Waals corrections. For each strain and magnetic configuration compute the total energy per unit cell (in meV) relative to the interlayer-AF (↑↑/↓↓) configuration at 0% strain. Save the energies to /app/outputs/phase_energies.json.
- Output file: `/app/outputs/phase_energies.json`
- Format: json
- Contract: Array of objects with keys: strain (float), E_upup_downdown (float, meV reference energy), E_upup_upup (float), E_updown_updown (float).
- Scoring: scored by hidden verifier

### Step 3: Compute exchange coupling and Curie temperature
- Role: scored
- Action: Using the DFT results from step_dft, compute intralayer and interlayer exchange coupling parameters J (meV) as functions of strain via the magnetic force theorem in OpenMx. Then, using these J values, run Monte Carlo simulations of the 2D Ising model to determine the Curie temperature Tc (K) for each strain. Save to /app/outputs/exchange_tc.json.
- Output file: `/app/outputs/exchange_tc.json`
- Format: json
- Contract: Array of objects with keys: strain (float), J_intra (float, meV), J_inter_first (float, meV, first interlayer neighbor), J_inter_second (float, meV, second interlayer neighbor), Tc (float, K).
- Scoring: scored by hidden verifier

### Step 4: Compute layer-constrained magnetic anisotropy energy
- Role: scored
- Action: Perform noncollinear DFT calculations with LSDA+SOC (OpenMx) for the bilayer at strains -5%, 0%, and +5%. For each strain, fix the magnetization of the bottom layer along z and rotate the magnetization of the top layer from 0° to 180° in steps not exceeding 15°. Record the total energy (meV per unit cell) relative to the FM (↑↑/↑↑) configuration at each strain. Save to /app/outputs/lc_mae.json.
- Output file: `/app/outputs/lc_mae.json`
- Format: json
- Contract: Array of objects with keys: strain (float), angle_deg (float), energy_meV (float, relative to FM state at that strain).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_energies.json`
- `/app/outputs/exchange_tc.json`
- `/app/outputs/lc_mae.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_energies.json
- path: `/app/outputs/phase_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Total energies of the three collinear magnetic configurations of C2/m bilayer CrI3 as a function of biaxial strain, referenced to the interlayer-AF configuration at 0% strain.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `strain`:
        - `type`: number
        - `description`: Biaxial strain value (dimensionless, e.g. -0.05 for -5%)
      - `E_upup_downdown`:
        - `type`: number
        - `unit`: meV per unit cell
      - `E_upup_upup`:
        - `type`: number
        - `unit`: meV per unit cell
      - `E_updown_updown`:
        - `type`: number
        - `unit`: meV per unit cell
    - `required`: `strain`, `E_upup_downdown`, `E_upup_upup`, `E_updown_updown`

### exchange_tc.json
- path: `/app/outputs/exchange_tc.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Exchange coupling parameters (intralayer and first/second interlayer) and Curie temperature for each strain.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `strain`:
        - `type`: number
      - `J_intra`:
        - `type`: number
        - `unit`: meV
      - `J_inter_first`:
        - `type`: number
        - `unit`: meV
      - `J_inter_second`:
        - `type`: number
        - `unit`: meV
      - `Tc`:
        - `type`: number
        - `unit`: K
    - `required`: `strain`, `J_intra`, `J_inter_first`, `J_inter_second`, `Tc`

### lc_mae.json
- path: `/app/outputs/lc_mae.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Layer-constrained magnetic anisotropy energy: total energy as a function of the angle between layer magnetizations for selected strains.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `strain`:
        - `type`: number
      - `angle_deg`:
        - `type`: number
        - `unit`: degrees
      - `energy_meV`:
        - `type`: number
        - `unit`: meV per unit cell
    - `required`: `strain`, `angle_deg`, `energy_meV`

Notes: The checker recomputes key quantities (phase boundaries, ∆E_inter) from the raw total energies, validates exchange-coupling signs and approximate Tc values, and performs structural cross-consistency checks on the LC-MAE data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "strain": {
              "type": "number",
              "description": "Biaxial strain value (dimensionless, e.g. -0.05 for -5%)"
            },
            "E_upup_downdown": {
              "type": "number",
              "unit": "meV per unit cell"
            },
            "E_upup_upup": {
              "type": "number",
              "unit": "meV per unit cell"
            },
            "E_updown_updown": {
              "type": "number",
              "unit": "meV per unit cell"
            }
          },
          "required": [
            "strain",
            "E_upup_downdown",
            "E_upup_upup",
            "E_updown_updown"
          ]
        }
      },
      "description": "Total energies of the three collinear magnetic configurations of C2/m bilayer CrI3 as a function of biaxial strain, referenced to the interlayer-AF configuration at 0% strain."
    },
    {
      "file": "exchange_tc.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "strain": {
              "type": "number"
            },
            "J_intra": {
              "type": "number",
              "unit": "meV"
            },
            "J_inter_first": {
              "type": "number",
              "unit": "meV"
            },
            "J_inter_second": {
              "type": "number",
              "unit": "meV"
            },
            "Tc": {
              "type": "number",
              "unit": "K"
            }
          },
          "required": [
            "strain",
            "J_intra",
            "J_inter_first",
            "J_inter_second",
            "Tc"
          ]
        }
      },
      "description": "Exchange coupling parameters (intralayer and first/second interlayer) and Curie temperature for each strain."
    },
    {
      "file": "lc_mae.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "strain": {
              "type": "number"
            },
            "angle_deg": {
              "type": "number",
              "unit": "degrees"
            },
            "energy_meV": {
              "type": "number",
              "unit": "meV per unit cell"
            }
          },
          "required": [
            "strain",
            "angle_deg",
            "energy_meV"
          ]
        }
      },
      "description": "Layer-constrained magnetic anisotropy energy: total energy as a function of the angle between layer magnetizations for selected strains."
    }
  ],
  "notes": "The checker recomputes key quantities (phase boundaries, ∆E_inter) from the raw total energies, validates exchange-coupling signs and approximate Tc values, and performs structural cross-consistency checks on the LC-MAE data."
}
```

## How you are scored
A hidden verifier will independently inspect each of the three output files. For `phase_energies.json`, it will re-derive the ground-state magnetic configuration at each strain and identify the strain intervals where each configuration is most stable; it will also compute the energy difference between the FM and interlayer-AF configurations at zero strain. For `exchange_tc.json`, it will examine the strain dependence of the exchange coupling parameters and the Curie temperature, checking for physically expected trends such as sign changes and monotonic evolution. For `lc_mae.json`, it will verify internal consistency: the energy at a 180° rotation angle must match the interlayer-AF to FM energy difference extracted from the collinear results for the same strain. The verifier will assign a score to each artifact based on how well these checks are satisfied, and the final reward (a number between 0 and 1) will be the weighted combination of those scores. The exact scoring thresholds and weights are hidden; you must let your computed physical quantities speak for themselves.
