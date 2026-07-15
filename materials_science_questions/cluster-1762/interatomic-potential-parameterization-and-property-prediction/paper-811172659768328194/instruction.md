# Reproduce Superconducting Transition Temperature of bcc Vanadium under Pressure via TB-LMTO and Allen–Dynes Formula

## Problem background
The pressure dependence of the superconducting transition temperature (Tc) in elemental metals provides insights into electron-phonon coupling mechanisms. Vanadium, a bcc transition metal, exhibits interesting superconducting behavior under pressure, and first-principles electronic structure methods can be used to predict Tc from the band structure. This task reproduces the theoretical calculation of Tc for bcc vanadium as a function of pressure, using tight-binding linear muffin-tin orbital (TB-LMTO) band structure calculations and the Allen–Dynes formula for superconductivity.

## Approach
The workflow consists of three main stages. First, self-consistent TB-LMTO total energy calculations are performed for bcc vanadium at a set of cell volumes spanning roughly 1.05 V₀ to 0.6 V₀ (with V₀ the equilibrium volume). Second, the total energy vs volume data are fitted to the Birch equation of state to obtain the ground-state equilibrium lattice parameter and the pressure corresponding to each volume. From the band structure outputs, the total density of states at the Fermi level N(E_F), partial electron counts (s, p, d), Fermi energy, and logarithmic derivatives are extracted. Third, the superconducting transition temperature Tc is computed using the Allen–Dynes formula: Tc = ⟨ω⟩/1.2 × exp{−1.04(1+λ) / [λ − μ*(1+0.62λ)]}. The electron-phonon coupling constant λ is obtained from the McMillan relation λ = N(E_F)⟨I²⟩ / (M⟨ω²⟩), where M is the atomic mass of vanadium (50.9415 u) and ⟨I²⟩ is evaluated from the partial densities of states N_l and electron‑phonon matrix elements M_{l,l+1}. The matrix elements depend on the logarithmic derivatives and the one-electron potential at the sphere boundary, obtained from the TB-LMTO outputs. The electron‑electron interaction constant μ* is estimated from the empirical relation μ* = 0.26 N(E_F) / [1 + N(E_F)]. The ambient reference phonon frequency ⟨ω⟩(0) is taken as 245 K. The pressure dependence of the phonon frequency is accounted for by scaling with the Debye temperature using the pressure‑dependent lattice parameter a(P) and Fermi energy E_F(P) according to the relation Θ_D(P)/Θ_D(0) = [a(0)/a(P)] √[E_F(P)/E_F(0)].

## Reproduction target
For bcc vanadium, compute and report the following quantities as a function of pressure for the pressures 0, 9.5, 24.3, 43.2, 51.9, 66.0, 76.8, 95.3, and 130.7 GPa: (i) the total density of states at the Fermi level N(E_F) in states/(Ryd atom) and the integrated numbers of s, p, and d electrons; (ii) the superconducting transition temperature Tc in Kelvin. Additionally, determine the ground‑state equilibrium lattice parameter (in atomic units) from the total energy vs volume fit.

## Assets

- TB-LMTO electronic structure code (e.g., Questaal): https://www.questaal.org/

## Workflow steps

### Step 1: Self-consistent TB-LMTO calculations for bcc vanadium
- Role: process
- Action: Run self-consistent TB-LMTO calculations for bcc vanadium at multiple cell volumes covering the range 1.05 V0 down to 0.6 V0 (where V0 is the equilibrium volume determined iteratively). Use a k-point mesh converged to at least 8000 points and the tetrahedron method for density of states. Store total energy versus volume and band eigenvalues for subsequent analysis.
- Evidence: `/app/outputs/tblmto_log.txt`

### Step 2: Equilibrium lattice parameter
- Role: scored
- Action: Fit the total energy versus volume data from the TB-LMTO calculations to the Birch equation of state to obtain the ground-state equilibrium lattice parameter. Write the result as a single floating-point number in atomic units (Bohr).
- Output file: `/app/outputs/equilibrium_lattice_parameter.txt`
- Format: txt
- Contract: A single line containing the equilibrium lattice parameter as a floating-point number in atomic units (Bohr).
- Scoring: scored by hidden verifier

### Step 3: Electronic structure under pressure
- Role: scored
- Action: From the TB-LMTO band structure outputs, extract for each specified pressure (0, 9.5, 24.3, 43.2, 51.9, 66.0, 76.8, 95.3, 130.7 GPa) the total density of states at the Fermi level N(EF) in states/(Ryd atom) and the integrated numbers of s, p, and d electrons. Write the data as a CSV file.
- Output file: `/app/outputs/electronic_structure_table.csv`
- Format: csv
- Contract: CSV with header: pressure (GPa), N(EF) (states/Ryd atom), s_electrons, p_electrons, d_electrons. Exactly one row for each of the specified pressures.
- Scoring: scored by hidden verifier

### Step 4: Superconducting transition temperature Tc
- Role: scored (load-bearing)
- Action: Compute the superconducting transition temperature Tc (in Kelvin) for each of the pressures (0, 9.5, 24.3, 43.2, 51.9, 66.0, 76.8, 95.3, 130.7 GPa) using the Allen–Dynes formula. The electron–phonon coupling constant λ is obtained from the TB-LMTO outputs (partial densities of states, logarithmic derivatives, and one-electron potential at the sphere boundary) together with the atomic mass of vanadium (50.9415 u). Use the ambient reference phonon frequency of 245 K. Scale the phonon frequency with pressure via the Debye-temperature scaling relation using the Fermi energy and lattice parameter from the band structure calculations. Write the resulting Tc versus pressure as a CSV file.
- Output file: `/app/outputs/tc_vs_pressure.csv`
- Format: csv
- Contract: CSV with header: Pressure (GPa), Tc (K). Exactly one row for each of the specified pressures.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_lattice_parameter.txt`
- `/app/outputs/electronic_structure_table.csv`
- `/app/outputs/tc_vs_pressure.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_lattice_parameter.txt
- path: `/app/outputs/equilibrium_lattice_parameter.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Ground-state equilibrium lattice parameter of bcc vanadium from the Birch equation-of-state fit to TB-LMTO total energies.
- schema:
  - `type`: text
  - `description`: A single line containing the equilibrium lattice parameter as a floating-point number in atomic units (Bohr).

### electronic_structure_table.csv
- path: `/app/outputs/electronic_structure_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure-dependent electronic structure data: total density of states at the Fermi level and integrated s, p, d electron numbers, for the specified pressures.
- schema:
  - `type`: table
  - `required_columns`: `pressure (GPa)`, `N(EF) (states/Ryd atom)`, `s_electrons`, `p_electrons`, `d_electrons`

### tc_vs_pressure.csv
- path: `/app/outputs/tc_vs_pressure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Superconducting transition temperature Tc as a function of pressure, computed from the TB-LMTO outputs and the Allen–Dynes formula.
- schema:
  - `type`: table
  - `required_columns`: `Pressure (GPa)`, `Tc (K)`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_lattice_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single line containing the equilibrium lattice parameter as a floating-point number in atomic units (Bohr)."
      },
      "description": "Ground-state equilibrium lattice parameter of bcc vanadium from the Birch equation-of-state fit to TB-LMTO total energies."
    },
    {
      "file": "electronic_structure_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure (GPa)",
          "N(EF) (states/Ryd atom)",
          "s_electrons",
          "p_electrons",
          "d_electrons"
        ]
      },
      "description": "Pressure-dependent electronic structure data: total density of states at the Fermi level and integrated s, p, d electron numbers, for the specified pressures."
    },
    {
      "file": "tc_vs_pressure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pressure (GPa)",
          "Tc (K)"
        ]
      },
      "description": "Superconducting transition temperature Tc as a function of pressure, computed from the TB-LMTO outputs and the Allen–Dynes formula."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that checks each output file against independently determined reference values. The equilibrium lattice parameter is checked for agreement within a tolerance, and the electronic structure table and Tc values are compared for numerical consistency with expected reference data. The final reward is a weighted sum over all scored stages, with the Tc calculation carrying the largest weight. Merely reporting numbers that happen to match a known result is not sufficient; your workflow must generate these numbers through the specified computational procedure. The verifier will not accept precomputed or plagiarized values.
