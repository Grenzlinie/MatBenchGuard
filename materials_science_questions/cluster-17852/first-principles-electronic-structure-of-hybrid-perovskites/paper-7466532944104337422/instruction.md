# Empirical Tight-Binding Calculation of Electron and Hole g-Factors in 2D Perovskites

## Problem background
Two-dimensional (2D) Ruddlesden–Popper lead halide perovskites are quantum-confined layered semiconductors whose thickness can be tuned by the number of inorganic octahedral layers. In spin-based applications, the Landé g‑factors of electrons and holes determine the Zeeman splitting in an external magnetic field. While bulk lead halide perovskites exhibit a universal g‑factor dependence on the band gap energy, atomically thin slabs are expected to show strong renormalization of these g‑factors due to quantum confinement, as well as pronounced anisotropy between the in‑plane and out‑of‑plane directions. This task reproduces the empirical tight‑binding (ETB) calculation that models the electron and hole g‑factor tensor components in 2D perovskite slabs as a function of the number of inorganic layers, thereby quantifying the confinement‑induced trends and anisotropy.

## Approach
The calculation employs an empirical tight‑binding model in the Slater–Koster scheme, using publicly available two‑centre parameters reported for cubic CsPbI₃. Slab structures Cs_N Pb_{N+1} I_{3N+2} with PbI₂‑terminated surfaces are built for N = 1,…,8, adopting a square lateral periodicity large enough to approximate infinite in‑plane extent. From these coordinates the sparse ETB Hamiltonian is assembled. To extract g‑factors, a weak uniform magnetic field is applied separately parallel to the slab plane (Voigt geometry) and perpendicular to it (Faraday geometry) via the Peierls substitution. The Zeeman splitting of the highest valence and lowest conduction states is computed; the linear slope of the energy splitting with field gives the raw g‑factor components g_e_ab, g_e_c, g_h_ab, g_h_c, together with the raw single‑particle band gap. The raw band gaps are subsequently corrected by the exciton binding energy for each layer thickness, taken from a published effective‑mass calculation, to obtain the effective band gap E_eff and the exciton energy E_exc. The final output comprises these corrected g‑factors and associated energies for all layer numbers.

## Reproduction target
Compute the layer‑dependent electron and hole g‑factor tensor components for 2D perovskite slabs with N = 1 to 8 and produce a single CSV file, g_factors.csv, with the following columns: n (integer), E_eff (effective band gap, eV), E_exc (exciton energy, eV), g_e_ab, g_e_c, g_h_ab, g_h_c (all dimensionless). The file must contain exactly one row per layer number n = 1,…,8. The values should reflect the physics of the ETB model after exciton binding energy correction and should exhibit the physically expected trends for quantum‑confined 2D structures.

## Assets

- Slater-Koster parameters for cubic CsPbI3: https://doi.org/10.1021/acs.nanolett.3c01798
- Exciton binding energies for 2D perovskites: https://doi.org/10.1039/D3NA00525H

## Workflow steps

### Step 1: Construct slab models and run ETB calculations
- Role: process
- Action: Construct atomic coordinates for Cs_N Pb_{N+1} I_{3N+2} slabs (N=1..8) with PbI₂ termination and a lateral size adequate to approximate infinite in-plane extent, using the cubic perovskite lattice parameters. Build the empirical tight-binding Hamiltonian from the Slater-Koster parameters, apply weak magnetic fields parallel and perpendicular to the slab plane via the Peierls substitution, and compute the Zeeman splitting of the highest valence and lowest conduction states to obtain the raw g-factor components (g_e_c, g_e_ab, g_h_c, g_h_ab) and the raw single-particle band gaps.
- Evidence: `/app/outputs/raw_etb_log.csv`

### Step 2: Compile corrected g-factors and effective band gaps
- Role: scored (load-bearing)
- Action: Apply the exciton binding energies for each layer number N from the provided reference to the raw band gaps to obtain the effective band gap (E_eff) and exciton energy (E_exc). Gather the corresponding g-factor tensor components for all N=1..8 and write the final CSV output.
- Output file: `/app/outputs/g_factors.csv`
- Format: csv
- Contract: Columns: n (int), E_eff (eV, float), E_exc (eV, float), g_e_ab (float), g_e_c (float), g_h_ab (float), g_h_c (float). One row per layer number n=1..8.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/g_factors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### g_factors.csv
- path: `/app/outputs/g_factors.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Final g-factor tensor components and associated energies for 2D perovskite slabs with N=1..8, after exciton binding energy correction. Checked against hidden reference values with tolerances; structural ordering checks are also applied.
- schema:
  - `type`: table
  - `required_columns`: `n`, `E_eff`, `E_exc`, `g_e_ab`, `g_e_c`, `g_h_ab`, `g_h_c`
  - `units`:
    - `n`: integer
    - `E_eff`: eV
    - `E_exc`: eV
    - `g_e_ab`: dimensionless
    - `g_e_c`: dimensionless
    - `g_h_ab`: dimensionless
    - `g_h_c`: dimensionless

Notes: The task reproduces only the ETB calculation of g-factors, not the experimental measurements. The solver must implement the tight-binding code. The checker compares each g-factor component and energy against gold values extracted from the paper's ETB results with tolerances (±0.05 for g-factors, ±0.01 eV for energies) and enforces ordering rules (g_e_c > g_e_ab, g_h_c < g_h_ab).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "g_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "E_eff",
          "E_exc",
          "g_e_ab",
          "g_e_c",
          "g_h_ab",
          "g_h_c"
        ],
        "units": {
          "n": "integer",
          "E_eff": "eV",
          "E_exc": "eV",
          "g_e_ab": "dimensionless",
          "g_e_c": "dimensionless",
          "g_h_ab": "dimensionless",
          "g_h_c": "dimensionless"
        }
      },
      "description": "Final g-factor tensor components and associated energies for 2D perovskite slabs with N=1..8, after exciton binding energy correction. Checked against hidden reference values with tolerances; structural ordering checks are also applied."
    }
  ],
  "notes": "The task reproduces only the ETB calculation of g-factors, not the experimental measurements. The solver must implement the tight-binding code. The checker compares each g-factor component and energy against gold values extracted from the paper's ETB results with tolerances (±0.05 for g-factors, ±0.01 eV for energies) and enforces ordering rules (g_e_c > g_e_ab, g_h_c < g_h_ab)."
}
```

## How you are scored
Your submission is evaluated by an automated verifier that inspects g_factors.csv. The verifier compares each g‑factor component and each energy against hidden reference values (derived from standard physical models and published data) using appropriate numerical tolerances. Additionally, the verifier checks that your results satisfy the following structural relations: for electrons, the out‑of‑plane component must be larger than the in‑plane component (g_e_c > g_e_ab); for holes, the out‑of‑plane component must be smaller than the in‑plane component (g_h_c < g_h_ab). The final reward is a weighted combination of these checks; simply reporting numbers that match a known source is not sufficient — the verifier scores the physical consistency and accuracy of your computed values.
