# First-principles calculation of structural, elastic, phonon, and thermal properties of ReB2

## Problem background
Rhenium diboride (ReB₂) is an ultra-incompressible, superhard material with a simple hexagonal crystal structure (space group P6₃/mmc). Its exceptional mechanical properties stem from strong covalent B–B and Re–B bonding, making it a candidate for cutting tools and wear-resistant coatings. A complete picture of its performance requires knowledge of its ground-state structure, elastic stiffness, lattice vibrations (phonons), and thermal expansion behaviour. This task asks you to compute these quantities from first principles, providing an independent prediction that can be compared to reference data.

## Approach
You will perform a series of density-functional theory (DFT) calculations using the plane-wave pseudopotential method, as implemented in the Quantum ESPRESSO package (PWscf). The exchange-correlation functional is the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation, and the ionic cores are represented by Vanderbilt ultrasoft pseudopotentials. The workflow is a sequential pipeline:

1. **Static structural relaxation:** Optimise both the hexagonal lattice parameters (a, c) and the internal atomic coordinates, including the boron fractional coordinate z, to obtain the zero‑temperature ground‑state geometry.
2. **Elastic constants:** Starting from the relaxed structure, apply the five symmetry‑independent strain modes for a hexagonal crystal. For each strained configuration, compute the total energy and extract the independent elastic constants c₁₁, c₁₂, c₁₃, c₃₃, and c₄₄ by fitting the energy‑versus‑strain data.
3. **Phonon properties:** Build a supercell of the relaxed structure and use the finite‑displacement method to obtain the dynamical matrix. From it, calculate the phonon dispersion along the high‑symmetry directions in the Brillouin zone and the total phonon density of states.
4. **Quasi‑harmonic thermal expansion:** At each point of a grid of (a, c) values, relax the internal coordinates and compute the phonon spectrum, then construct the Helmholtz free energy. For each temperature from 0 K to 1000 K, find the lattice parameters that minimise the free energy, yielding the temperature dependence a(T) and c(T).

All of these calculations use the same underlying DFT setup, and the results are reported in the specified CSV output files.

## Reproduction target
Your task is to produce the following computed quantities from the DFT pipeline described above:

- **Step 1:** The relaxed lattice constants a (Å), c (Å) and the fractional boron coordinate z for hexagonal ReB₂.
- **Step 2:** The five independent hexagonal elastic constants c₁₁, c₁₂, c₁₃, c₃₃, c₄₄ in GPa.
- **Step 3:** The phonon dispersion along the Brillouin‑zone path Γ–A–H–K–Γ–M–Λ, recorded as frequency (cm⁻¹) versus path label and index, as well as the total phonon density of states (energy in meV, DOS in arbitrary units).
- **Step 5:** The temperature dependence of the lattice parameters a(T) and c(T) from 0 K to 1000 K, at temperature steps no larger than 50 K.

You must write each of these results exactly as specified in the output contract, using only the public resources listed in the Assets section. No pre‑computed data may be used; you must execute the full computational pipeline yourself.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotential for Re (PBE): https://www.quantum-espresso.org/pseudopotentials/
- Vanderbilt ultrasoft pseudopotential for B (PBE): https://www.quantum-espresso.org/pseudopotentials/
- ReB2 experimental crystal structure (space group P6₃/mmc, a=2.900 Å, c=7.478 Å, z=0.048)

## Workflow steps

### Step 1: DFT structural relaxation
- Role: scored
- Action: Perform DFT structural relaxation of hexagonal ReB2 (space group P6₃/mmc) to obtain the zero-temperature ground-state geometry. Optimize both lattice parameters (a, c) and internal atomic positions, including the boron fractional coordinate z.
- Output file: `/app/outputs/step_01_relaxed_output.csv`
- Format: csv
- Contract: Columns: a(Å), c(Å), z (fractional); one data row.
- Scoring: scored by hidden verifier

### Step 2: Elastic constants calculation
- Role: scored
- Action: Compute the five independent elastic constants (c11, c12, c13, c33, c44) for the relaxed ReB2 structure by applying symmetry-adapted strains and fitting the total energy response.
- Output file: `/app/outputs/step_02_elastic_constants.csv`
- Format: csv
- Contract: Columns: c11(GPa), c12, c13, c33, c44; one data row.
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion calculation
- Role: scored
- Action: Calculate phonon dispersion curves along high-symmetry Brillouin‑zone paths using the supercell finite‑displacement method from the relaxed ReB2 structure.
- Output file: `/app/outputs/step_03_phonon_dispersion.csv`
- Format: csv
- Contract: Columns: q_path_label (string, e.g. 'Γ→A'), q_index (int), frequency_cm-1 (float).
- Scoring: scored by hidden verifier

### Step 4: Phonon density of states
- Role: scored
- Action: Calculate the total phonon density of states from the same supercell dynamical matrix as the dispersion.
- Output file: `/app/outputs/step_03_phonon_dos.csv`
- Format: csv
- Contract: Columns: energy_meV (float), dos_arb_units (float).
- Scoring: scored by hidden verifier

### Step 5: Quasi‑harmonic thermal expansion
- Role: scored (load-bearing)
- Action: Within the quasi‑harmonic approximation, compute the temperature dependence of lattice parameters a and c by minimizing the Helmholtz free energy over a grid of (a, c) values, using phonon spectra at each grid point.
- Output file: `/app/outputs/step_04_thermal_expansion.csv`
- Format: csv
- Contract: Columns: T_K (float), a_AA (float), c_AA (float); data points covering 0–1000 K with step ≤ 50 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_relaxed_output.csv`
- `/app/outputs/step_02_elastic_constants.csv`
- `/app/outputs/step_03_phonon_dispersion.csv`
- `/app/outputs/step_03_phonon_dos.csv`
- `/app/outputs/step_04_thermal_expansion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_relaxed_output.csv
- path: `/app/outputs/step_01_relaxed_output.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized lattice parameters, electronic density of states at Fermi level, and Vickers hardness. The checker compares all values to paper‑reported references with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `a(Å)`, `c(Å)`, `z`, `N_Ef(states/eV)`, `H(GPa)`

### step_02_elastic_constants.csv
- path: `/app/outputs/step_02_elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Independent elastic constants. The checker compares each constant to the paper‑reported values with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `c11(GPa)`, `c12`, `c13`, `c33`, `c44`

### step_03_phonon_dispersion.csv
- path: `/app/outputs/step_03_phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon dispersion data. The checker verifies that frequencies at selected high‑symmetry points match the paper’s values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `q_path_label`, `q_index`, `frequency_cm-1`

### step_03_phonon_dos.csv
- path: `/app/outputs/step_03_phonon_dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total phonon density of states. The checker verifies structural properties (smoothness, main peak positions consistent with the paper).
- schema:
  - `type`: table
  - `required_columns`: `energy_meV`, `dos_arb_units`

### step_04_thermal_expansion.csv
- path: `/app/outputs/step_04_thermal_expansion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent lattice parameters. The checker verifies the curves are smooth and the linear thermal expansion coefficient at 1000 K matches the paper’s reference within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `a_AA`, `c_AA`

Notes: All outputs are derived from the same DFT and phonon computations. The agent must run the full pipeline; no precomputed data may be substituted. The hidden checker will use the paper’s reported numbers as reference gold, but the instruction does not reveal them. The electronic DOS and hardness quantities are now scored as part of step_01.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_relaxed_output.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a(Å)",
          "c(Å)",
          "z",
          "N_Ef(states/eV)",
          "H(GPa)"
        ]
      },
      "description": "Optimized lattice parameters, electronic density of states at Fermi level, and Vickers hardness. The checker compares all values to paper‑reported references with appropriate tolerances."
    },
    {
      "file": "step_02_elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "c11(GPa)",
          "c12",
          "c13",
          "c33",
          "c44"
        ]
      },
      "description": "Independent elastic constants. The checker compares each constant to the paper‑reported values with tolerances."
    },
    {
      "file": "step_03_phonon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_path_label",
          "q_index",
          "frequency_cm-1"
        ]
      },
      "description": "Phonon dispersion data. The checker verifies that frequencies at selected high‑symmetry points match the paper’s values within tolerance."
    },
    {
      "file": "step_03_phonon_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_meV",
          "dos_arb_units"
        ]
      },
      "description": "Total phonon density of states. The checker verifies structural properties (smoothness, main peak positions consistent with the paper)."
    },
    {
      "file": "step_04_thermal_expansion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "a_AA",
          "c_AA"
        ]
      },
      "description": "Temperature-dependent lattice parameters. The checker verifies the curves are smooth and the linear thermal expansion coefficient at 1000 K matches the paper’s reference within tolerance."
    }
  ],
  "notes": "All outputs are derived from the same DFT and phonon computations. The agent must run the full pipeline; no precomputed data may be substituted. The hidden checker will use the paper’s reported numbers as reference gold, but the instruction does not reveal them. The electronic DOS and hardness quantities are now scored as part of step_01."
}
```

## How you are scored
A hidden verifier will independently score each of the five output CSV files. For the lattice parameters, elastic constants, and thermal expansion, the verifier compares your computed values against reference data using appropriate tolerances. For the phonon results, it checks that the dispersion frequencies at specific high‑symmetry points and the overall shape of the density of states are consistent with expectations. The individual stage scores are combined with weights that emphasise the main quantitative results, giving a final reward between 0 and 1. The reference values and the exact tolerances are hidden from you; your goal is to faithfully execute the described DFT workflow and report the outcomes, not to guess a particular target.
