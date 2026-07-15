# First-Principles Thermoelectric Transport Coefficients of Pnictogen-Substituted Ternary Skutterudites

## Problem background
Pnictogen-substituted ternary skutterudites (PSTSs) are a class of materials that combine low lattice thermal conductivity with electronic properties that may be suitable for thermoelectric energy conversion. First-principles calculations can predict key transport quantities—direct band gaps, Seebeck coefficients, and power factors—from the crystal structure and chemical composition. This task investigates how substituting the pnictogen site in the prototypical skutterudite CoSb₃ with pairs of group‑14 (Ge, Sn) and group‑16 (S, Se, Te) elements changes the electronic band structure and thermoelectric transport characteristics.

## Approach
The computational workflow combines density functional theory (DFT) within the local density approximation (LDA) and Boltzmann transport theory under the constant relaxation time approximation.

1. Starting from publicly available experimental crystal structures, perform DFT‑LDA structural relaxation for each of the six PSTS compositions and for CoSb₃.
2. From the relaxed structures, carry out self‑consistent and band‑structure calculations to obtain Kohn–Sham eigenvalues and wavefunctions.
3. Use maximally localized Wannier functions (Wannier90) to interpolate the DFT band structure onto a fine k‑point mesh and build an accurate tight‑binding Hamiltonian.
4. Solve the Boltzmann transport equation with the constant relaxation time τ = 10 fs to compute the Seebeck coefficient, electrical conductivity, and power factor as a continuous function of chemical potential at 300 K.
5. Extract the direct band gap at the appropriate k‑point for each compound, and report the transport quantities for specific carrier concentrations (10²⁰ cm⁻³) and as full traces over chemical potential.

## Reproduction target
Your task is to execute the full DFT → Wannier → Boltzmann pipeline and produce the following scored artifacts:

- **band_gaps.json**: the direct band gap (in eV) for each of the seven compounds (CoGe₁.₅S₁.₅, CoGe₁.₅Se₁.₅, CoGe₁.₅Te₁.₅, CoSn₁.₅S₁.₅, CoSn₁.₅Se₁.₅, CoSn₁.₅Te₁.₅, and CoSb₃).
- **seebeck_CoGe1.5S1.5_p_1e20.csv**: the Seebeck coefficient (µV/K) at 300 K for p‑type CoGe₁.₅S₁.₅ at a hole concentration of 10²⁰ cm⁻³.
- **seebeck_CoSn1.5Te1.5_n_1e20.csv**: the Seebeck coefficient (µV/K) at 300 K for n‑type CoSn₁.₅Te₁.₅ at an electron concentration of 10²⁰ cm⁻³.
- **power_factors_300K.csv**: the power factor (W m⁻¹ K⁻²) as a function of chemical potential at 300 K for every compound.

The deposited output must come from a consistent execution of the workflow described in the steps above. Using pre‑computed numbers or shortcuts that avoid the actual DFT/Wannier/transport calculations will be detected by the verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Wannier90: https://www.wannier.org/
- BoltzTraP (or BoltzTraP2): https://www.boltzser.org/
- LDA pseudopotentials for Co, Ge, Sn, S, Se, Te, Sb: https://www.materialscloud.org/discover/sssp/
- Relaxed crystal structures (POSCAR or equivalent) for the seven compounds

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Using Quantum ESPRESSO, relax the atomic positions (and cell if required) for all seven compounds (CoGe₁.₅S₁.₅, CoGe₁.₅Se₁.₅, CoGe₁.₅Te₁.₅, CoSn₁.₅S₁.₅, CoSn₁.₅Se₁.₅, CoSn₁.₅Te₁.₅, and CoSb₃) starting from the provided experimental crystal structures. Use LDA exchange-correlation and appropriate pseudopotentials.
- Evidence: `/app/outputs/relax.log`

### Step 2: DFT electronic structure calculation
- Role: process
- Action: For each relaxed compound, perform self-consistent and non-self-consistent band structure calculations within DFT-LDA using the same pseudopotentials and basis-set parameters as for relaxation. Obtain Kohn-Sham eigenvalues and wavefunctions.
- Evidence: `/app/outputs/bands.out`

### Step 3: Wannier function construction
- Role: process
- Action: Using Wannier90, construct maximally localized Wannier functions from the DFT Bloch states to generate a tight-binding Hamiltonian for each compound.
- Evidence: `/app/outputs/wannier.chk`

### Step 4: Compute direct band gaps
- Role: scored
- Action: From the DFT band structure output, determine the direct band gap at the appropriate k-point for each of the seven compounds and write a JSON file listing each compound's name and gap value.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: [{"compound": "string", "direct_band_gap_eV": "float"}]
- Scoring: scored by hidden verifier

### Step 5: Boltzmann transport calculation
- Role: process
- Action: Using the Wannier Hamiltonian and the BoltzTraP code (or equivalent), compute the Seebeck coefficient, electrical conductivity, and power factor for each compound as a function of chemical potential at 300 K, assuming a constant relaxation time τ = 10 fs.
- Evidence: `/app/outputs/transport.npz`

### Step 6: Seebeck coefficient for CoGe₁.₅S₁.₅ (p-type, 10²⁰ cm⁻³)
- Role: scored (load-bearing)
- Action: From the transport results at 300 K, extract the Seebeck coefficient corresponding to a chemical potential that yields a hole concentration of 10²⁰ cm⁻³ in CoGe₁.₅S₁.₅. Write a CSV file with columns temperature_K and Seebeck_uV_per_K containing the 300 K data point.
- Output file: `/app/outputs/seebeck_CoGe1.5S1.5_p_1e20.csv`
- Format: csv
- Contract: temperature_K (float), Seebeck_uV_per_K (float)
- Scoring: scored by hidden verifier

### Step 7: Seebeck coefficient for CoSn₁.₅Te₁.₅ (n-type, 10²⁰ cm⁻³)
- Role: scored
- Action: From the transport results at 300 K, extract the Seebeck coefficient corresponding to a chemical potential that yields an electron concentration of 10²⁰ cm⁻³ in CoSn₁.₅Te₁.₅. Write a CSV with the same columns as the previous step.
- Output file: `/app/outputs/seebeck_CoSn1.5Te1.5_n_1e20.csv`
- Format: csv
- Contract: temperature_K (float), Seebeck_uV_per_K (float)
- Scoring: scored by hidden verifier

### Step 8: Power factors at 300 K
- Role: scored
- Action: For all seven compounds, extract the power factor (S²σ) at 300 K as a function of chemical potential. Write a CSV with columns compound, chemical_potential_eV and power_factor_W_per_m_K2.
- Output file: `/app/outputs/power_factors_300K.csv`
- Format: csv
- Contract: compound (string), chemical_potential_eV (float), power_factor_W_per_m_K2 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`
- `/app/outputs/seebeck_CoGe1.5S1.5_p_1e20.csv`
- `/app/outputs/seebeck_CoSn1.5Te1.5_n_1e20.csv`
- `/app/outputs/power_factors_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Direct band gap values for the six PSTS compounds and CoSb₃, compared against paper‑reported reference values within an allowed tolerance.
- schema:
  - `type`: array
  - `required`: `compound`, `direct_band_gap_eV`
  - `items`:
    - `compound`: string
    - `direct_band_gap_eV`: float

### seebeck_CoGe1.5S1.5_p_1e20.csv
- path: `/app/outputs/seebeck_CoGe1.5S1.5_p_1e20.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficient at 300 K for p‑type CoGe₁.₅S₁.₅ at a hole concentration of 10²⁰ cm⁻³, compared against the paper's implied reference value.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `Seebeck_uV_per_K`
  - `units`:
    - `Seebeck_uV_per_K`: µV/K

### seebeck_CoSn1.5Te1.5_n_1e20.csv
- path: `/app/outputs/seebeck_CoSn1.5Te1.5_n_1e20.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Seebeck coefficient at 300 K for n‑type CoSn₁.₅Te₁.₅ at an electron concentration of 10²⁰ cm⁻³, compared against the paper's implied reference value.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `Seebeck_uV_per_K`
  - `units`:
    - `Seebeck_uV_per_K`: µV/K

### power_factors_300K.csv
- path: `/app/outputs/power_factors_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Power factor as a function of chemical potential at 300 K. Verified by a structural audit: the maximum p‑type power factor of any PSTS must be lower than that of CoSb₃.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `chemical_potential_eV`, `power_factor_W_per_m_K2`
  - `units`:
    - `power_factor_W_per_m_K2`: W/(m·K²)

Notes: All outputs are produced from the same DFT+DFPT+Wannier+Boltzmann workflow, ensuring internal consistency. Phonon and Born effective charge calculations are included as process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": [
          "compound",
          "direct_band_gap_eV"
        ],
        "items": {
          "compound": "string",
          "direct_band_gap_eV": "float"
        }
      },
      "description": "Direct band gap values for the six PSTS compounds and CoSb₃, compared against paper‑reported reference values within an allowed tolerance."
    },
    {
      "file": "seebeck_CoGe1.5S1.5_p_1e20.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "Seebeck_uV_per_K"
        ],
        "units": {
          "Seebeck_uV_per_K": "µV/K"
        }
      },
      "description": "Seebeck coefficient at 300 K for p‑type CoGe₁.₅S₁.₅ at a hole concentration of 10²⁰ cm⁻³, compared against the paper's implied reference value."
    },
    {
      "file": "seebeck_CoSn1.5Te1.5_n_1e20.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "Seebeck_uV_per_K"
        ],
        "units": {
          "Seebeck_uV_per_K": "µV/K"
        }
      },
      "description": "Seebeck coefficient at 300 K for n‑type CoSn₁.₅Te₁.₅ at an electron concentration of 10²⁰ cm⁻³, compared against the paper's implied reference value."
    },
    {
      "file": "power_factors_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "chemical_potential_eV",
          "power_factor_W_per_m_K2"
        ],
        "units": {
          "power_factor_W_per_m_K2": "W/(m·K²)"
        }
      },
      "description": "Power factor as a function of chemical potential at 300 K. Verified by a structural audit: the maximum p‑type power factor of any PSTS must be lower than that of CoSb₃."
    }
  ],
  "notes": "All outputs are produced from the same DFT+DFPT+Wannier+Boltzmann workflow, ensuring internal consistency. Phonon and Born effective charge calculations are included as process steps."
}
```

## How you are scored
A hidden verifier inspects each output file independently. For the band gaps and Seebeck coefficients, the verifier compares your results to reference values obtained from a correct implementation of the described protocol. For the power factor, the verifier checks a required structural trend among the compounds. Each scored artifact carries a weight; the final reward is a weighted combination of the individual scores.

Important: the verifier has access to the intermediate evidence files (e.g. relax.log, bands.out, transport.npz) and may use them to confirm that the full computational pipeline was executed. Reporting plausible numbers without genuinely running the DFT‑to‑transport chain will not pass.
