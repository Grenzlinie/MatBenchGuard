# Superconducting Critical Temperature Trend via Electron-Phonon Coupling in Rocksalt Hydrides

## Problem background
The report of near-ambient superconductivity in nitrogen-doped lutetium hydride has been controversial. Guided by X-ray diffraction data, a candidate cubic phase—rocksalt-type LuH (RS‑LuH)—has been proposed and studied theoretically. This work investigates the superconducting properties of RS‑LuH and its derivatives by performing first‑principles calculations. It examines how lanthanide element substitution, applied pressure, and nitrogen doping affect the superconducting critical temperature (Tc) and the underlying parameters: the electron‑phonon coupling constant λ, the logarithmic average phonon frequency ω_log, and the electronic density of states at the Fermi level N(E_F). The goal is to compute these quantities for a series of rocksalt hydrides and to determine how they depend on composition and pressure.

## Approach
The study uses density functional theory (DFT) and density functional perturbation theory (DFPT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and standard pseudopotentials. For each compound and pressure, the workflow proceeds as follows:

1. Relax the crystal structure to obtain the equilibrium lattice parameters and atomic positions.
2. Compute the electronic density of states with a dense k‑point mesh and extract N(E_F) in units of states/(spin·Ry·unitcell).
3. Perform DFPT calculations to obtain the phonon dispersions and the Eliashberg function α²F(ω); from these compute the total electron‑phonon coupling constant λ and the logarithmic average phonon frequency ω_log.
4. Estimate the superconducting critical temperature Tc using the McMillan–Allen–Dynes formula with a Coulomb pseudopotential μ* = 0.1.

By applying this protocol to the full lanthanide series RS‑XH (X = La to Lu) at ambient pressure, and to pristine RS‑LuH and nitrogen‑doped Lu₄NH₃ at several pressures, one can extract the trends in Tc, λ, ω_log, and N(E_F) with lanthanide substitution, pressure, and doping.

## Reproduction target
Produce a single CSV file named `superconducting_properties.csv` containing the computed Tc, λ, ω_log, and N(E_F) for the following systems:

- RS‑XH (X = La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu) at 0 GPa (15 rows).
- RS‑LuH at pressures 0, 1, and 10 GPa (3 rows).
- Lu₄NH₃ at pressures 0, 1, and 10 GPa (3 rows).

The file must have columns: compound, pressure_GPa, Tc_K, lambda, omega_log_K, N_EF_states_per_spin_Ry_unitcell. All calculations must use the open‑source Quantum ESPRESSO package and publicly available pseudopotentials (e.g., PSlibrary or SSSP). The required rows and column schema are fully specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (PSlibrary or SSSP efficiency): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Structure relaxation
- Role: process
- Action: Perform DFT structure relaxation for all required rocksalt hydride systems (RS-XH with X = La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu at 0 GPa; RS-LuH at 0, 1, 10 GPa; Lu4NH3 at 0, 1, 10 GPa) to obtain optimized lattice constants and atomic positions. Use the rocksalt (Fm-3m) or Pm-3m crystal structures as starting points.
- Evidence: none

### Step 2: Electronic structure and density of states
- Role: process
- Action: For each relaxed structure, compute the electronic density of states (DOS) using a dense k-point grid. Extract the DOS at the Fermi level, N(E_F), in units of states/(spin·Ry·unitcell).
- Evidence: none

### Step 3: Phonon and electron-phonon coupling calculation
- Role: process
- Action: For each system, perform density functional perturbation theory (DFPT) calculations to obtain phonon dispersions and the Eliashberg function α²F(ω). Compute the total electron-phonon coupling constant λ and the logarithmic average phonon frequency ω_log.
- Evidence: none

### Step 4: Superconducting Tc estimation and compilation
- Role: scored (load-bearing)
- Action: Using the McMillan-Allen-Dynes formula with Coulomb pseudopotential μ* = 0.1, compute the superconducting critical temperature Tc from λ and ω_log for every compound and pressure. Compile all computed superconducting parameters into a single CSV file with columns: compound, pressure_GPa, Tc_K, lambda, omega_log_K, N_EF_states_per_spin_Ry_unitcell.
- Output file: `/app/outputs/superconducting_properties.csv`
- Format: csv
- Contract: CSV with columns: compound (string), pressure_GPa (float), Tc_K (float), lambda (float), omega_log_K (float), N_EF_states_per_spin_Ry_unitcell (float). Required rows include all 15 RS-XH (La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu) at 0 GPa; RS-LuH at 0, 1, 10 GPa; Lu4NH3 at 0, 1, 10 GPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/superconducting_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### superconducting_properties.csv
- path: `/app/outputs/superconducting_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed superconducting parameters for all studied compounds and pressures. The hidden checker compares the Tc, λ, ω_log, and N(E_F) values to paper-reported reference numbers and validates the monotonic increase of Tc with lanthanide atomic number (excluding Yb and La anomalies), the decrease of Tc with increasing pressure for RS-LuH and Lu4NH3, and the lower Tc of the N-doped compound compared to pristine RS-LuH at each pressure.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `pressure_GPa`, `Tc_K`, `lambda`, `omega_log_K`, `N_EF_states_per_spin_Ry_unitcell`
  - `units`:
    - `pressure_GPa`: GPa
    - `Tc_K`: K
    - `omega_log_K`: K
    - `N_EF_states_per_spin_Ry_unitcell`: states/(spin*Ry*unitcell)

Notes: All required compounds and pressures are listed in the step action. For YbH at 0 GPa (dynamically unstable) the Tc field may be left blank or omitted; the checker handles this when evaluating trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "superconducting_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "pressure_GPa",
          "Tc_K",
          "lambda",
          "omega_log_K",
          "N_EF_states_per_spin_Ry_unitcell"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "Tc_K": "K",
          "omega_log_K": "K",
          "N_EF_states_per_spin_Ry_unitcell": "states/(spin*Ry*unitcell)"
        }
      },
      "description": "Table of computed superconducting parameters for all studied compounds and pressures. The hidden checker compares the Tc, λ, ω_log, and N(E_F) values to paper-reported reference numbers and validates the monotonic increase of Tc with lanthanide atomic number (excluding Yb and La anomalies), the decrease of Tc with increasing pressure for RS-LuH and Lu4NH3, and the lower Tc of the N-doped compound compared to pristine RS-LuH at each pressure."
    }
  ],
  "notes": "All required compounds and pressures are listed in the step action. For YbH at 0 GPa (dynamically unstable) the Tc field may be left blank or omitted; the checker handles this when evaluating trends."
}
```

## How you are scored
A hidden verifier reads your `superconducting_properties.csv` and compares each reported value (Tc, λ, ω_log, N(E_F)) to reference calculations within appropriate tolerances, yielding a score for the absolute numerical accuracy. In addition, the verifier evaluates the dependence of Tc on lanthanide atomic number, pressure, and nitrogen doping by checking whether the computed data satisfy the expected relationships (e.g., monotonic trend with atomic number, pressure and doping suppression) using statistical tests. The final reward is a weighted combination of these checks, with a larger weight given to the accuracy of the computed Tc values and the main trends. The exact tolerances and weighting are hidden; your task is to execute the full computational pipeline faithfully and report the resulting superconducting parameters.
