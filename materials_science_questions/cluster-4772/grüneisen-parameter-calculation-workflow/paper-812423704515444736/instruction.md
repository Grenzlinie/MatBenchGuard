# Electronic Thermodynamics of Close-Packed Iron under High Pressure

## Problem background
The electronic thermodynamics of iron under Earth core conditions (high pressure, high temperature) are crucial for understanding the core's heat capacity, thermal evolution, and geophysical dynamics. This task addresses the computation of the electronic density of states (DOS) for the close-packed phases of iron — hcp (ε-Fe) and fcc (γ-Fe) — at three compressions relevant to core pressures. From the DOS, the electronic specific heat, free energy, thermal pressure, and an electronic Grüneisen parameter are derived. Reproducing these quantities provides constraints on the thermal budget of Earth's core.

## Approach
The approach uses first-principles density functional theory (DFT) with the local density approximation (LDA) exchange-correlation functional, in a non-magnetic, non-relativistic treatment. Self-consistent band structure calculations are performed for hcp and fcc iron at three atomic volumes (Wigner-Seitz radii 2.3, 2.4, 2.5 bohr) using a plane-wave/pseudopotential code. The electronic density of states is computed on a fine energy grid. Subsequently, Fermi-Dirac statistical mechanics is applied: numerical integration (trapezoidal rule) of the DOS is performed to obtain the electronic internal energy, free energy, and specific heat as functions of temperature up to 10000 K, assuming a fixed valence electron count of 8. The low-temperature linear coefficient of the specific heat (β) and the electronic Grüneisen parameter (γₑ) are extracted from the temperature and volume dependence of the computed specific heat, and the thermal electronic pressure is obtained from the volume derivative of the free energy. The comparison is between the two phases and across the three compressions.

## Reproduction target
The goal is to reproduce the electronic density of states (DOS) for hcp and fcc iron at Wigner-Seitz radii 2.3, 2.4, 2.5 bohr, and from the DOS to derive the following electronic thermodynamic quantities: the linear specific heat coefficient β (mJ K⁻² mol⁻¹), the electronic Grüneisen parameter γₑ (dimensionless), and the electronic internal energy (eV/atom), free energy (eV/atom), and thermal pressure (GPa) at temperatures of 3000 K and 6000 K. The results must be reported for each phase and compression combination.

## Assets

- Quantum ESPRESSO (QE): https://www.quantum-espresso.org/
- Fe LDA pseudopotential: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Data preparation: volumes and structures
- Role: process
- Action: For each phase (hcp, fcc) and Wigner-Seitz radii R_WS = 2.3, 2.4, 2.5 bohr, compute atomic volume V = (4/3)π R_WS³. Optionally map to zero-temperature pressure using a semiempirical equation of state. Prepare crystal structures (lattice vectors and atomic positions) for the DFT calculations.
- Evidence: `/app/outputs/data_prep_log.txt`

### Step 2: DFT electronic density of states
- Role: scored (load-bearing)
- Action: Perform self-consistent non-magnetic, non-relativistic DFT calculations using an LDA exchange-correlation functional (approximating von Barth–Hedin) on hcp and fcc iron at each R_WS. Use a dense k-point mesh and a sufficient plane-wave energy cutoff. After self-consistency, compute the DOS on a fine energy grid covering at least from −10 eV to 30 eV relative to the Fermi level, using the tetrahedron method. Output the DOS as states/(eV·atom) into dos_data.csv.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: columns: phase (string, 'hcp' or 'fcc'), R_WS_bohr (float, 2.3/2.4/2.5), energy_eV (float), dos_states_per_eV_per_atom (float). One row per energy point. The energy range must fully cover the occupied valence bands and extend well above the Fermi level (>10 eV) to allow accurate Fermi-Dirac integration.
- Scoring: scored by hidden verifier

### Step 3: Electronic thermodynamic properties
- Role: scored
- Action: From dos_data.csv, perform trapezoidal-rule Fermi-Dirac integration with a temperature grid from 0 to 10000 K and fixed electron count n_e = 8 to obtain c_v_e(T), u_e(T), and f_e(T). Fit the low‑temperature linear portion of c_v_e to extract β (mJ K⁻² mol⁻¹). Compute the electronic Grüneisen parameter γₑ from a log–log fit of β vs volume V or from the ratio Δpₑ/Δuₑ. Compute the thermal electronic pressure Δpₑ via volume differentiation of fₑ. Report β, γₑ, uₑ and fₑ at 3000 K and 6000 K, and Δpₑ at those temperatures, in thermo_properties.csv.
- Output file: `/app/outputs/thermo_properties.csv`
- Format: csv
- Contract: columns: phase (string), R_WS_bohr (float), beta_mJ_K2_mol (float), gamma_e (float), u_e_3000K_eV_per_atom (float), u_e_6000K_eV_per_atom (float), f_e_3000K_eV_per_atom (float), f_e_6000K_eV_per_atom (float), dp_e_3000K_GPa (float), dp_e_6000K_GPa (float). One row per (phase, R_WS) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_data.csv`
- `/app/outputs/thermo_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw electronic density of states for hcp and fcc iron at three compressions; the checker reads this to recompute thermodynamic quantities.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `R_WS_bohr`, `energy_eV`, `dos_states_per_eV_per_atom`
  - `units`:
    - `energy_eV`: eV
    - `dos_states_per_eV_per_atom`: states/(eV·atom)

### thermo_properties.csv
- path: `/app/outputs/thermo_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electronic thermodynamic quantities derived from the DOS; compared to hidden paper-reported values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `R_WS_bohr`, `beta_mJ_K2_mol`, `gamma_e`, `u_e_3000K_eV_per_atom`, `u_e_6000K_eV_per_atom`, `f_e_3000K_eV_per_atom`, `f_e_6000K_eV_per_atom`, `dp_e_3000K_GPa`, `dp_e_6000K_GPa`
  - `units`:
    - `beta_mJ_K2_mol`: mJ K⁻² mol⁻¹
    - `gamma_e`: dimensionless
    - `u_e_3000K_eV_per_atom`: eV/atom
    - `u_e_6000K_eV_per_atom`: eV/atom
    - `f_e_3000K_eV_per_atom`: eV/atom
    - `f_e_6000K_eV_per_atom`: eV/atom
    - `dp_e_3000K_GPa`: GPa
    - `dp_e_6000K_GPa`: GPa

Notes: The scoring primarily relies on the recomputation from dos_data.csv. The thermo_properties.csv is cross-checked for consistency and compared against hidden gold values. The pressure calibration is optional and not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "R_WS_bohr",
          "energy_eV",
          "dos_states_per_eV_per_atom"
        ],
        "units": {
          "energy_eV": "eV",
          "dos_states_per_eV_per_atom": "states/(eV·atom)"
        }
      },
      "description": "Raw electronic density of states for hcp and fcc iron at three compressions; the checker reads this to recompute thermodynamic quantities."
    },
    {
      "file": "thermo_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "R_WS_bohr",
          "beta_mJ_K2_mol",
          "gamma_e",
          "u_e_3000K_eV_per_atom",
          "u_e_6000K_eV_per_atom",
          "f_e_3000K_eV_per_atom",
          "f_e_6000K_eV_per_atom",
          "dp_e_3000K_GPa",
          "dp_e_6000K_GPa"
        ],
        "units": {
          "beta_mJ_K2_mol": "mJ K⁻² mol⁻¹",
          "gamma_e": "dimensionless",
          "u_e_3000K_eV_per_atom": "eV/atom",
          "u_e_6000K_eV_per_atom": "eV/atom",
          "f_e_3000K_eV_per_atom": "eV/atom",
          "f_e_6000K_eV_per_atom": "eV/atom",
          "dp_e_3000K_GPa": "GPa",
          "dp_e_6000K_GPa": "GPa"
        }
      },
      "description": "Electronic thermodynamic quantities derived from the DOS; compared to hidden paper-reported values with tolerances."
    }
  ],
  "notes": "The scoring primarily relies on the recomputation from dos_data.csv. The thermo_properties.csv is cross-checked for consistency and compared against hidden gold values. The pressure calibration is optional and not scored."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier. The verifier reads your `dos_data.csv` and independently recomputes the electronic specific heat, free energy, thermal pressure, and Grüneisen parameter from the DOS using numerical integration and fitting. The recomputed quantities are compared against expected reference values derived from the original study. In addition, your `thermo_properties.csv` is cross-checked for consistency with these recomputed values. The final reward is a weighted combination of the scores for each output file; simply reporting numbers is not sufficient — the underlying DOS must support the derived quantities. No tolerance or gold values are provided to you; the verifier applies appropriate tolerances that account for legitimate implementation differences.
