# Ground-state magnetic phase diagram and anisotropy of a 5d pyrochlore oxide with spin-orbit coupling

## Problem background
Pyrochlore transition-metal oxides containing 5d elements, such as Cd₂Os₂O₇, display a complex interplay between spin-orbit coupling and electronic correlations. Experimentally, this compound undergoes a metal-insulator transition (MIT) concurrently with magnetic ordering at around 227 K, yet the nature of the insulating state and the origin of the high transition temperature remain puzzling. First-principles calculations based on density-functional theory with on-site Coulomb repulsion and full spin-orbit coupling can elucidate the ground-state electronic and magnetic properties as a function of the effective Hubbard U. The goal is to compute the magnetic phase diagram (non-magnetic metal, antiferromagnetic metal, antiferromagnetic insulator), the stability of the proposed all-in/all-out non-collinear magnetic order, the magnetic anisotropy energy, and the density of states near the MIT to determine whether a pseudogap forms.

## Approach
The reproduction employs density-functional theory within the local spin-density approximation (LSDA) supplemented by an on-site Coulomb repulsion U (using the Dudarev approach) and fully relativistic spin-orbit coupling. Calculations are performed for the pyrochlore Cd₂Os₂O₇ in its face-centered cubic primitive cell, with the lattice constant and oxygen position taken from experiment. The key control parameter is U_eff = U - J, which is varied over a range that covers the reported metal-insulator transition. For each U_eff value, self-consistent field (SCF) calculations are carried out for both the non-magnetic state and for the all-in/all-out antiferromagnetic spin configuration. From these, total energies, projected magnetic moments on the Os atoms, direct band gaps, charge gaps, and electronic density of states (DOS) are obtained. The ground-state magnetic phase at each U_eff is defined as the configuration with the lowest total energy. At a U_eff value in the antiferromagnetic insulating regime (1.25 eV), constrained SCF calculations are performed where the Os spin directions are rigidly rotated from the all-in/all-out ground-state orientation around the [001] axis. In addition, the 3-in/1-out configuration (one spin flipped) is computed. The total energies of these constrained configurations give the magnetic anisotropy energy as a function of rotation angle, as well as the energy difference between the all-in/all-out and 3-in/1-out states. Finally, a phenomenological spin model with nearest-neighbor exchange (J), single-ion easy-axis anisotropy (A_sia), and Dzyaloshinskii-Moriya interaction (A_DM) is fitted to the anisotropy energies to extract the effective magnetic couplings.

## Reproduction target
Reproduce the following four numerical artifacts:

1. **Phase diagram table** (`phase_diagram.csv`) – for each U_eff value (0.0, 0.5, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5 eV), report the ground-state magnetic phase ('NMM', 'AFM', or 'AFI'), the Os magnetic moment (μ_B), the direct gap Δ_D (eV), and the charge gap Δ_C (eV).

2. **Energy comparison** (`energy_comparison.csv`) – at U_eff = 1.25 eV, provide the total energy per Os atom for the all-in/all-out order and for the 3-in/1-out order.

3. **Magnetic anisotropy curve** (`anisotropy_curve.csv`) – at U_eff = 1.25 eV, give the total energy difference (meV per Os) relative to the ground-state all-in/all-out orientation for rotation angles θ around [001] from 0° to 180° in steps no larger than 30°.

4. **Density of states near the MIT** (`dos_near_MIT.csv`) – at a U_eff value near the metal-insulator transition (e.g., 1.1 eV), tabulate the electronic DOS (states/eV/primitive cell) on a fine energy grid spanning at least −1.0 to +1.0 eV relative to the Fermi level, with a maximum step size of 0.01 eV.

## Assets

- Plane-wave DFT code with LSDA+SO+U capability (e.g., Quantum ESPRESSO, VASP, or equivalent): https://www.quantum-espresso.org/ (or http://qmas.jp/ for QMAS)

## Workflow steps

### Step 1: Self-consistent field calculations for ground-state phase diagram
- Role: process
- Action: For each Ueff value in [0.0, 0.5, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5] eV, run LSDA+SO+U DFT calculations for non-magnetic and all-in/all-out antiferromagnetic configurations using a plane-wave DFT code. Use the experimental face-centered cubic primitive cell with a=10.1598 Å and oxygen x=0.319. Retain total energies, Os magnetic moments, band structures, and density of states.
- Evidence: `/app/outputs/scf_outputs_summary.json`

### Step 2: Extract ground-state phase diagram and gaps
- Role: scored (load-bearing)
- Action: From the SCF results of step 1, determine the ground-state phase (lowest total energy) for each Ueff, and compute the local Os magnetic moment m_Os (integrated within 2.5 a.u.), the direct gap Δ_D (minimum gap between valence and conduction bands at same k-point), and the charge gap Δ_C (indicating insulating state). Write the extracted quantities to phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: Ueff (eV), phase (string: 'NMM','AFM','AFI'), m_Os (μB), Delta_D (eV), Delta_C (eV). One row per Ueff value.
- Scoring: scored by hidden verifier

### Step 3: Constrained magnetic anisotropy calculations
- Role: process
- Action: Using the SCF charge density of the all-in/all-out ground state at Ueff=1.25 eV, perform constrained DFT calculations where the Os moment directions are rotated from the ground-state orientation by angles θ around [001] axis (θ from 0° to 180° in steps ≤ 30°). Also compute the 3-in/1-out magnetic configuration. Record total energies for each configuration.
- Evidence: `/app/outputs/anisotropy_log.csv`

### Step 4: Energy comparison: all-in/all-out vs 3-in/1-out
- Role: scored
- Action: From the constrained DFT results of step 3, extract the total energy per Os atom for the all-in/all-out (θ=0) and the 3-in/1-out magnetic configurations. Write the two energies to energy_comparison.csv.
- Output file: `/app/outputs/energy_comparison.csv`
- Format: csv
- Contract: Columns: magnetic_order (string: 'AIAO' or '3in1out'), total_energy_per_Os (eV). Two rows.
- Scoring: scored by hidden verifier

### Step 5: Magnetic anisotropy energy curve
- Role: scored
- Action: From the constrained DFT results of step 3, compute the total energy difference ΔE(θ) = E(θ) - E(0) (in meV per Os) for each rotation angle θ of the all-in/all-out configuration. Write the curve to anisotropy_curve.csv.
- Output file: `/app/outputs/anisotropy_curve.csv`
- Format: csv
- Contract: Columns: theta (degrees), energy_diff (meV/Os). Rows for rotation angles from 0° to 180° in increments ≤ 30°. energy_diff is total energy relative to θ=0.
- Scoring: scored by hidden verifier

### Step 6: Density of states near the metal-insulator transition
- Role: scored
- Action: From the SCF results of step 1 at a Ueff value near the MIT (e.g., 1.1 eV), extract the electronic density of states (DOS) as a function of energy relative to Fermi level. Sample on an energy grid of at most 0.01 eV step, covering at least -1.0 eV to +1.0 eV. Write to dos_near_MIT.csv.
- Output file: `/app/outputs/dos_near_MIT.csv`
- Format: csv
- Contract: Columns: energy (eV), DOS (states/eV/primitive cell). Energy range spanning at least -1.0 to 1.0 eV relative to Fermi level, grid ≤ 0.01 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/energy_comparison.csv`
- `/app/outputs/anisotropy_curve.csv`
- `/app/outputs/dos_near_MIT.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase diagram data: for each Ueff, the assigned magnetic phase, Os moment, direct gap, and charge gap.
- schema:
  - `type`: table
  - `required_columns`: `Ueff`, `phase`, `m_Os`, `Delta_D`, `Delta_C`
  - `units`:
    - `Ueff`: eV
    - `m_Os`: μB
    - `Delta_D`: eV
    - `Delta_C`: eV

### energy_comparison.csv
- path: `/app/outputs/energy_comparison.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Comparison of ground state and lowest excited magnetic state energies, verifying the stability of the all-in/all-out order.
- schema:
  - `type`: table
  - `required_columns`: `magnetic_order`, `total_energy_per_Os`
  - `units`:
    - `total_energy_per_Os`: eV

### anisotropy_curve.csv
- path: `/app/outputs/anisotropy_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic anisotropy energy as a function of rotation angle, used to extract the easy-axis anisotropy and exchange parameters.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `energy_diff`
  - `units`:
    - `theta`: degrees
    - `energy_diff`: meV/Os

### dos_near_MIT.csv
- path: `/app/outputs/dos_near_MIT.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Density of states near the metal-insulator transition, showing the pseudogap feature around the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `DOS`
  - `units`:
    - `energy`: eV
    - `DOS`: states/eV/primitive cell

Notes: All computed values are compared to paper-reported reference values with generous tolerances to account for different DFT implementations. The anisotropy curve is used by the checker to fit the exchange and anisotropy parameters; the fitted parameters are then compared to the paper's reported values. The DOS near MIT is checked for the presence of a pseudo gap (structural audit).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ueff",
          "phase",
          "m_Os",
          "Delta_D",
          "Delta_C"
        ],
        "units": {
          "Ueff": "eV",
          "m_Os": "μB",
          "Delta_D": "eV",
          "Delta_C": "eV"
        }
      },
      "description": "Phase diagram data: for each Ueff, the assigned magnetic phase, Os moment, direct gap, and charge gap."
    },
    {
      "file": "energy_comparison.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "magnetic_order",
          "total_energy_per_Os"
        ],
        "units": {
          "total_energy_per_Os": "eV"
        }
      },
      "description": "Comparison of ground state and lowest excited magnetic state energies, verifying the stability of the all-in/all-out order."
    },
    {
      "file": "anisotropy_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "energy_diff"
        ],
        "units": {
          "theta": "degrees",
          "energy_diff": "meV/Os"
        }
      },
      "description": "Magnetic anisotropy energy as a function of rotation angle, used to extract the easy-axis anisotropy and exchange parameters."
    },
    {
      "file": "dos_near_MIT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "DOS"
        ],
        "units": {
          "energy": "eV",
          "DOS": "states/eV/primitive cell"
        }
      },
      "description": "Density of states near the metal-insulator transition, showing the pseudogap feature around the Fermi level."
    }
  ],
  "notes": "All computed values are compared to paper-reported reference values with generous tolerances to account for different DFT implementations. The anisotropy curve is used by the checker to fit the exchange and anisotropy parameters; the fitted parameters are then compared to the paper's reported values. The DOS near MIT is checked for the presence of a pseudo gap (structural audit)."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. Each of the four scored output files is checked independently:

- **phase_diagram.csv** – verifies that the assigned magnetic phase agrees with the phase determined from total energies, and compares the Os moments, direct gap, and charge gap against reference values.
- **energy_comparison.csv** – checks that the energies are ordered correctly (all-in/all-out lower) and that their difference falls within an expected range.
- **anisotropy_curve.csv** – uses your θ and energy_diff data to fit the spin model (exchange J, single-ion anisotropy A_sia, DM interaction A_DM) and compares the fitted parameters against expected values.
- **dos_near_MIT.csv** – inspects the DOS for the presence of a pseudogap (a significant suppression of spectral weight around the Fermi level over an energy window of ~0.2 eV).

The verifier combines the per-artifact results using a weighted average to produce a final score between 0 (no valid result) and 1 (fully consistent with the reference). Simply reporting a number without the appropriate underlying data will not yield a high score; the verifier examines the content, internal consistency, and physical plausibility of your submitted artifacts. The exact tolerances, reference values, and weights are hidden.
