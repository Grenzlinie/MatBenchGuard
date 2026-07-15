# Lanthanide-Based MXene Geometry Preference, Dynamical Stability, and Electronic Properties

## Problem background
Two-dimensional lanthanide-based carbides (MXenes) M₂C, where M is a lanthanide element, are candidate materials for spintronics and semiconductor applications. Before these materials can be synthesized and used, it is essential to know which crystal geometry they prefer (T-type or H-type), whether that geometry is dynamically stable (i.e., exhibits no imaginary phonon modes), and what electronic properties their fluorine- and hydroxyl-terminated forms exhibit — for instance, whether they are half‑metals or semiconductors, their band gaps, magnetic moments, and work functions. This task uses first‑principles density functional theory (DFT) computations to determine these quantities for the twelve lanthanides from Ce to Yb.

## Approach
The core idea is to re‑run the computational protocol that predicts these properties from atomic coordinates using plane‑wave DFT with the PBE exchange‑correlation functional. Spin‑polarized calculations are performed throughout. First, bare M₂C monolayers are built in the two candidate geometries — T‑type and H‑type — and structurally relaxed. The total energies of the relaxed cells are compared to find which geometry is lower in energy. Next, phonon dispersions are computed for the T‑type structures via density‑functional perturbation theory to verify that all phonon frequencies are positive, confirming dynamical stability.

Afterwards, functionalized MXenes are created by attaching fluorine (‑F) and hydroxyl (‑OH) groups in the most stable arrangement (model 2, where groups sit above the bottom metal atoms on both sides). These structures are relaxed, and their magnetic ground state is identified by testing non‑magnetic, ferromagnetic, and antiferromagnetic spin configurations. Electronic band structures are then calculated at the GGA level; for the two Gd‑containing compounds an additional hybrid functional (HSE06) calculation is required to correct the band gaps. From the band structure we extract the half‑metallic character (only one spin channel crosses the Fermi level), band gaps, and total magnetic moment per unit cell. Finally, the work function of each functionalized MXene is obtained from the planar‑averaged electrostatic potential along the out‑of‑plane direction.

The entire workflow is executed with open‑source tools — Quantum ESPRESSO for DFT and Phonopy for phonons — and with pseudopotentials from the SSSP library. The numerical parameters (cutoff energy, k‑mesh, convergence thresholds) are left to the solver, but the procedure described here is the complete experimental design.

## Reproduction target
Produce three scored artifacts under /app/outputs that together capture the main results of the computational study:

1. **bare_preference.csv** — a CSV file listing, for each lanthanide M (Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb), the relaxed total energies of the T‑type and H‑type M₂C monolayers and their difference ΔE = E(T‑type) − E(H‑type). The result must be obtained from your own DFT relaxations.

2. **stability_report.json** — a JSON object with one entry per lanthanide element, reporting whether imaginary phonon modes were found (boolean) and the minimum phonon frequency (in cm⁻¹) for the T‑type M₂C structure. The analysis must be based on your computed phonon dispersions.

3. **functionalized_properties.json** — a JSON array containing, for every (M, T) pair with T = F or OH, the total magnetization (µB), half‑metallic classification, spin‑down band gap (if half‑metallic), semiconductor classification, band gap (if semiconductor), and work function (eV). These quantities must come from your own DFT electronic‑structure and work‑function calculations, including the HSE06 band gaps for Gd₂CF₂ and Gd₂C(OH)₂.

The objective is to compute these numbers from the atomic structures using open‑source codes; no pre‑computed values or look‑up tables are allowed. The hidden verifier will assess how well your computed artifacts agree with physically expected trends and reference values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP Pseudopotential Library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Relax T- and H-type bare M₂C structures
- Role: process
- Action: For each lanthanide M (Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb), construct T-type and H-type monolayer unit cells of M₂C with a vacuum layer >15 Å. Perform spin-polarized DFT relaxation using the PBE functional, plane-wave cutoff of 500 eV, Γ-centred 12×12×1 k‑mesh, force convergence < 1×10⁻⁴ eV/Å, energy tolerance 1×10⁻⁶ eV. Save relaxed structures and total energies.
- Evidence: `/app/outputs/relaxed_bare_structures.tar`

### Step 2: Record relative total energies
- Role: scored
- Action: From the relaxed total energies of step_01, compute the relative total energy difference ΔE = E(T‑type) − E(H‑type) for each M, and write the results to bare_preference.csv.
- Output file: `/app/outputs/bare_preference.csv`
- Format: csv
- Contract: columns: M (string), E_T_type (float, eV), E_H_type (float, eV), delta_E (float, eV); one row per M (12 rows).
- Scoring: scored by hidden verifier

### Step 3: Compute phonon dispersions for T-type M₂C
- Role: process
- Action: For each T-type M₂C relaxed structure from step_01, construct a 4×4×1 supercell and run DFPT phonon calculations using Phonopy with Quantum ESPRESSO as the force calculator. Compute phonon dispersion along high-symmetry lines.
- Evidence: `/app/outputs/phonon_bare_dispersions.tar`

### Step 4: Report dynamical stability of bare M₂C
- Role: scored (load-bearing)
- Action: For each T-type M₂C, inspect the phonon frequencies; record whether any imaginary modes exist (frequency < −5 cm⁻¹) and the minimum phonon frequency. Output stability_report.json.
- Output file: `/app/outputs/stability_report.json`
- Format: json
- Contract: Top-level JSON object; keys are element symbols (Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb); each value is an object with fields 'phonon_imaginary_modes' (boolean) and 'min_frequency' (float, cm⁻¹).
- Scoring: scored by hidden verifier

### Step 5: Relax functionalized M₂CT₂ structures (model 2)
- Role: process
- Action: For each M, construct fluorine-terminated (M₂CF₂) and hydroxyl-terminated (M₂C(OH)₂) MXenes in the stable model 2 configuration (functional groups on top of the bottom M atoms on both sides). Perform DFT relaxation using the same parameters as step_01.
- Evidence: `/app/outputs/relaxed_functionalized_structures.tar`

### Step 6: Determine magnetic ground state (NM, FM, AFM)
- Role: process
- Action: For each functionalized structure from step_05, perform spin-polarized DFT calculations in non-magnetic (NM), ferromagnetic (FM), and antiferromagnetic (AFM) spin configurations. Identify the magnetic ground state as the one with lowest total energy.
- Evidence: `/app/outputs/magnetic_ground_states.json`

### Step 7: Compute electronic band structures
- Role: process
- Action: For each functionalized structure in its magnetic ground state, compute spin-polarized band structure using GGA-PBE. For Gd₂CF₂ and Gd₂C(OH)₂, also compute band structure using the HSE06 hybrid functional to correct the band gap. Extract band gaps (PBE and HSE06), half-metallic character (only one spin channel crosses the Fermi level), and total magnetic moment per unit cell.
- Evidence: none

### Step 8: Compute work functions
- Role: process
- Action: For each functionalized structure from step_05, compute the work function as the difference between the vacuum level and the Fermi level from the planar-averaged electrostatic potential along the out-of-plane direction.
- Evidence: `/app/outputs/work_functions.csv`

### Step 9: Compile functionalized properties
- Role: scored (load-bearing)
- Action: Combine the electronic properties from steps 06-08 into a single JSON file. For each (M, T) pair (M = Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb; T = F or OH), record total magnetization (µᵦ), whether the material is half-metallic, spin-down band gap if half-metallic, whether it is a semiconductor, band gap if semiconductor, and work function (eV). Output functionalized_properties.json.
- Output file: `/app/outputs/functionalized_properties.json`
- Format: json
- Contract: JSON array; each object: M (string, element symbol), T (string, 'F' or 'OH'), total_magnetization (float, µB), half_metallic (bool), spin_down_band_gap (float or null, eV), semiconductor (bool), band_gap (float or null, eV), work_function (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bare_preference.csv`
- `/app/outputs/stability_report.json`
- `/app/outputs/functionalized_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bare_preference.csv
- path: `/app/outputs/bare_preference.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Relative total energy difference between T‑ and H‑type M₂C for all twelve lanthanides; delta_E must be negative (T‑type has lower total energy) for every M within a small tolerance.
- schema:
  - `type`: table
  - `required_columns`: `M`, `E_T_type`, `E_H_type`, `delta_E`
  - `units`:
    - `E_T_type`: eV
    - `E_H_type`: eV
    - `delta_E`: eV

### stability_report.json
- path: `/app/outputs/stability_report.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Dynamical stability verdict for bare T-type M₂C; all entries must show no imaginary phonon modes (phonon_imaginary_modes = false) with min_frequency > -5 cm⁻¹.
- schema:
  - `type`: object
  - `description`: Keys are element symbols (Ce, Pr, …). Each value is an object with fields: 'phonon_imaginary_modes' (boolean) must be false; 'min_frequency' (float, cm⁻¹) must be greater than -5 cm⁻¹.

### functionalized_properties.json
- path: `/app/outputs/functionalized_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Electronic properties of all functionalized MXenes; half‑metallic/semiconductor flags and key band gaps / work functions are checked against paper‑reported values with appropriate tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `M`, `T`, `total_magnetization`, `half_metallic`, `spin_down_band_gap`, `semiconductor`, `band_gap`, `work_function`
    - `properties`:
      - `M`:
        - `type`: string
      - `T`:
        - `type`: string
        - `enum`: `F`, `OH`
      - `total_magnetization`:
        - `type`: number
        - `unit`: µB
      - `half_metallic`:
        - `type`: boolean
      - `spin_down_band_gap`:
        - `type`: `number`, `null`
        - `unit`: eV
      - `semiconductor`:
        - `type`: boolean
      - `band_gap`:
        - `type`: `number`, `null`
        - `unit`: eV
      - `work_function`:
        - `type`: number
        - `unit`: eV

Notes: Scoring compares the agent’s computed values against hidden paper‑reported references using thresholds (e.g., delta_E sign, absence of imaginary modes, Eu₂CF₂ spin‑down gap >2 eV, Gd₂CT₂ band gaps, Tm₂C(OH)₂ work function ≈1.46 eV). All tolerances account for code‑to‑code spread between Quantum ESPRESSO and VASP.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bare_preference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "M",
          "E_T_type",
          "E_H_type",
          "delta_E"
        ],
        "units": {
          "E_T_type": "eV",
          "E_H_type": "eV",
          "delta_E": "eV"
        }
      },
      "description": "Relative total energy difference between T‑ and H‑type M₂C for all twelve lanthanides; delta_E must be negative (T‑type has lower total energy) for every M within a small tolerance."
    },
    {
      "file": "stability_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "description": "Keys are element symbols (Ce, Pr, …). Each value is an object with fields: 'phonon_imaginary_modes' (boolean) must be false; 'min_frequency' (float, cm⁻¹) must be greater than -5 cm⁻¹."
      },
      "description": "Dynamical stability verdict for bare T-type M₂C; all entries must show no imaginary phonon modes (phonon_imaginary_modes = false) with min_frequency > -5 cm⁻¹."
    },
    {
      "file": "functionalized_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "M",
            "T",
            "total_magnetization",
            "half_metallic",
            "spin_down_band_gap",
            "semiconductor",
            "band_gap",
            "work_function"
          ],
          "properties": {
            "M": {
              "type": "string"
            },
            "T": {
              "type": "string",
              "enum": [
                "F",
                "OH"
              ]
            },
            "total_magnetization": {
              "type": "number",
              "unit": "µB"
            },
            "half_metallic": {
              "type": "boolean"
            },
            "spin_down_band_gap": {
              "type": [
                "number",
                "null"
              ],
              "unit": "eV"
            },
            "semiconductor": {
              "type": "boolean"
            },
            "band_gap": {
              "type": [
                "number",
                "null"
              ],
              "unit": "eV"
            },
            "work_function": {
              "type": "number",
              "unit": "eV"
            }
          }
        }
      },
      "description": "Electronic properties of all functionalized MXenes; half‑metallic/semiconductor flags and key band gaps / work functions are checked against paper‑reported values with appropriate tolerances."
    }
  ],
  "notes": "Scoring compares the agent’s computed values against hidden paper‑reported references using thresholds (e.g., delta_E sign, absence of imaginary modes, Eu₂CF₂ spin‑down gap >2 eV, Gd₂CT₂ band gaps, Tm₂C(OH)₂ work function ≈1.46 eV). All tolerances account for code‑to‑code spread between Quantum ESPRESSO and VASP."
}
```

## How you are scored
An automated verifier will inspect the three scored output files you produce. It checks each file independently for correctness of trends, structural validity, and proximity to hidden reference values (with tolerances that account for code‑to‑code differences between Quantum ESPRESSO and the reference DFT code). The verifier does **not** demand bit‑identical numbers; it rewards physically sound results — for example, the correct sign of energy differences, the absence of imaginary phonon modes, the correct classification of materials as half‑metals or semiconductors, and band gaps and work functions that fall within acceptable ranges. Each artifact contributes a portion of the total score, and the weighted sum of these partial scores yields your final reward. Reporting numbers that you did not actually compute will not lead to a high score, because the verifier’s checks are sensitive to the internal consistency of your computed results.
