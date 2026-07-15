# Site preference and elastic properties of gamma-AlON from DFT calculations

## Problem background
γ-AlON is a spinel-type aluminium oxynitride in which the nitrogen atoms and oxygen atoms share the 32e anion sites, and aluminium vacancies are present to maintain charge neutrality. The resulting compositional disorder gives rise to open questions about the local structure: which arrangements of nitrogen atoms are most stable, and which aluminium sites are preferred for vacancies. Resolving these site preferences is essential for building a realistic structural model that can be used in first-principles calculations to predict mechanical and electronic properties such as the bulk modulus, elastic constants, and electronic band gap. This task uses density functional theory (DFT) to compute energies, geometries, and derived properties for ordered structural models of Al₂₄O₂₄N₈ and Al₂₃O₂₇N₅, and thereby determine the site preferences and key material properties of γ-AlON.

## Approach
First-principles density functional theory (DFT) calculations are performed using both GGA (PBE) and LDA exchange–correlation functionals, employing an open-source plane‑wave DFT code (Quantum ESPRESSO) and standard pseudopotentials. The workflow proceeds in several stages:

1. **Ordered N configurations in Al₂₄O₂₈N₈:** Starting from the spinel Fd3̄m crystal structure, three distinct ordered models are constructed by placing the eight nitrogen atoms into specific face‑center anion groups (32e sites). For each model, the geometry is relaxed and the total energy, equilibrium cell volume, and nearest‑neighbour N–N distance are computed.
2. **Al‑vacancy configurations in Al₂₃O₂₇N₅:** Using the anion arrangement of the most stable Al₂₄O₂₄N₈ model, three N atoms are replaced by O atoms, and seven independent aluminium‑vacancy configurations are generated, differing in the vacancy site (octahedral or tetrahedral) and the local nitrogen coordination. Each model is structurally optimised, and the total energy, cell volume, and electronic band gap are obtained.
3. **Equation of state and bulk modulus:** For the most stable Al₂₃O₂₇N₅ model, a series of total‑energy calculations is carried out at several cell volumes. The Birch–Murnaghan equation of state is fitted to the energy‑volume data to extract the equilibrium volume, bulk modulus, and pressure derivative.
4. **Elastic constants:** For the same most stable structure, the elastic constants C₁₁, C₁₂, and C₄₄ are evaluated at the GGA level using the energy‑displacement method.

## Reproduction target
Produce the following scored output files placed under `/app/outputs`:

- `al24o24n8_results.csv`: a CSV file containing, for each of the three ordered Al₂₄O₂₄N₈ models and for both GGA and LDA, the final total energy (eV), equilibrium cell volume (Å³), and the nearest‑neighbour N–N distance (Å).
- `al23o27n5_results.csv`: a CSV file containing, for each of the seven Al₂₃O₂₇N₅ vacancy models and for both GGA and LDA, the total energy (eV), cell volume (Å³), and the electronic band gap (eV).
- `bulk_modulus_fit.txt`: a text file that reports, for both functionals, the fitted Birch–Murnaghan parameters — equilibrium volume V₀ (Å³), bulk modulus B₀ (GPa), pressure derivative B′, and the percentage deviations of V₀ and B₀ relative to the experimental reference.
- `elastic_constants.txt`: a text file that lists the computed elastic constants C₁₁, C₁₂, and C₄₄ (GPa) at the GGA level for the most stable Al₂₃O₂₇N₅ structure.

The results must be obtained from the DFT re‑calculations described in the workflow steps. The determination of which model is most stable follows from comparing the computed total energies; use those energies to select the appropriate models for the later analyses.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE and LDA): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct ordered Al24O24N8 models
- Role: process
- Action: Construct three independent structural configurations (model 1, 2, 3) by placing eight N atoms into the following face‑center anion groups: model 1 uses groups 1 and 2 (or equivalently 3, 4); model 2 uses groups 1 and 5; model 3 uses groups 1 and 6 (or 7, 8). The models are built on the spinel Fd3̄m structure (32e sites).
- Evidence: `/app/outputs/models_al24o24n8.txt`

### Step 2: DFT geometry optimization and total energy for Al24O24N8
- Role: process
- Action: For each model (1,2,3) run DFT geometry optimization and total energy calculation using GGA (PBE) and LDA functionals. After relaxation extract total energy, cell volume, and nearest-neighbour N–N distance.
- Evidence: `/app/outputs/dft_al24o24n8.log`

### Step 3: Compile Al24O24N8 results
- Role: scored
- Action: Write a CSV file containing, for each model and functional, the final total energy, equilibrium volume, and nearest-neighbour N–N distance.
- Output file: `/app/outputs/al24o24n8_results.csv`
- Format: csv
- Contract: model (int 1/2/3), functional (string GGA or LDA), total_energy (float, eV), volume (float, Å³), d_NN (float, Å)
- Scoring: scored by hidden verifier

### Step 4: Construct Al23O27N5 vacancy models
- Role: process
- Action: Starting from the anion arrangement of the most stable Al24O24N8 model (model 2), substitute three N atoms by O atoms (in group 5, or equivalently group 1) to obtain the Al23O27N5 composition. Generate seven distinct Al‑vacancy configurations using the following positions: model 1 – octahedral, fractional coordinates (7/8, 7/8, 5/8); model 2 – tetrahedral, (1/4, 3/4, 3/4); model 3 – octahedral, (5/8, 7/8, 7/8); model 4 – tetrahedral, (3/4, 3/4, 1/4); model 5 – octahedral, (5/8, 5/8, 5/8); model 6 – tetrahedral, (0, 0, 1); model 7 – tetrahedral, (1/2, 1/2, 1).
- Evidence: `/app/outputs/models_al23o27n5.txt`

### Step 5: DFT calculations for Al23O27N5
- Role: process
- Action: For each of the seven Al23O27N5 models, run DFT geometry optimization followed by a band-gap calculation using GGA and LDA. Record total energy, volume, and band gap.
- Evidence: `/app/outputs/dft_al23o27n5.log`

### Step 6: Compile Al23O27N5 results
- Role: scored
- Action: Write a CSV file containing, for each model and functional, the total energy, volume, and electronic band gap.
- Output file: `/app/outputs/al23o27n5_results.csv`
- Format: csv
- Contract: model (int 1-7), functional (string GGA or LDA), total_energy (float, eV), volume (float, Å³), band_gap (float, eV)
- Scoring: scored by hidden verifier

### Step 7: EOS fitting for the most stable Al23O27N5 model
- Role: process
- Action: For the most stable model of Al23O27N5 (model 1), perform a series of DFT total-energy calculations at several volumes around equilibrium using both GGA and LDA. Fit the E(V) data to the Birch-Murnaghan equation of state to obtain equilibrium volume (V0), bulk modulus (B0), and pressure derivative (B′).
- Evidence: `/app/outputs/eos_fit.log`

### Step 8: Report bulk modulus from EOS
- Role: scored
- Action: Write a text file containing the EOS fitting results for GGA and LDA, including V0, B0, B′, and the percentage deviations DV_percent and DB_percent relative to the experimental reference values (V_exp = 503.67 Å³, B_exp = 215.81 GPa). Compute DV_percent = 100 × (V0 − 503.67) / 503.67 and DB_percent = 100 × (B0 − 215.81) / 215.81.
- Output file: `/app/outputs/bulk_modulus_fit.txt`
- Format: txt
- Contract: For each functional (GGA, LDA): V0 (float, Å³), B0 (float, GPa), B_prime (float), DV_percent (float), DB_percent (float)
- Scoring: scored by hidden verifier

### Step 9: Elastic constants calculation for Al23O27N5
- Role: process
- Action: Using the most stable Al23O27N5 model (model 1), compute the elastic constants C11, C12, C44 with the energy-displacement method at the GGA level.
- Evidence: `/app/outputs/elastic_energy_vs_strain.log`

### Step 10: Report elastic constants
- Role: scored (load-bearing)
- Action: Write a text file containing the computed C11, C12, and C44 (GGA).
- Output file: `/app/outputs/elastic_constants.txt`
- Format: txt
- Contract: functional (string GGA), C11 (float, GPa), C12 (float, GPa), C44 (float, GPa)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/al24o24n8_results.csv`
- `/app/outputs/al23o27n5_results.csv`
- `/app/outputs/bulk_modulus_fit.txt`
- `/app/outputs/elastic_constants.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### al24o24n8_results.csv
- path: `/app/outputs/al24o24n8_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total energies, volumes, and nearest-neighbour N–N distances for the three ordered Al24O24N8 configurations, calculated with GGA and LDA.
- schema:
  - `type`: table
  - `required_columns`: `model`, `functional`, `total_energy`, `volume`, `d_NN`
  - `columns`:
    - `model`:
      - `type`: int
      - `description`: Model index (1,2,3)
    - `functional`:
      - `type`: string
      - `description`: GGA or LDA
    - `total_energy`:
      - `type`: float
      - `unit`: eV
    - `volume`:
      - `type`: float
      - `unit`: Å^3
    - `d_NN`:
      - `type`: float
      - `unit`: Å

### al23o27n5_results.csv
- path: `/app/outputs/al23o27n5_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total energies, volumes, and electronic band gaps for the seven Al23O27N5 vacancy models, calculated with GGA and LDA.
- schema:
  - `type`: table
  - `required_columns`: `model`, `functional`, `total_energy`, `volume`, `band_gap`
  - `columns`:
    - `model`:
      - `type`: int
      - `description`: Model index (1..7)
    - `functional`:
      - `type`: string
      - `description`: GGA or LDA
    - `total_energy`:
      - `type`: float
      - `unit`: eV
    - `volume`:
      - `type`: float
      - `unit`: Å^3
    - `band_gap`:
      - `type`: float
      - `unit`: eV

### bulk_modulus_fit.txt
- path: `/app/outputs/bulk_modulus_fit.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Birch-Murnaghan EOS fitting results for the most stable Al23O27N5 model (model 1) with GGA and LDA.
- schema:
  - `type`: text
  - `format`: key-value entries
  - `fields`:
    - `name`: functional
    - `type`: string
    - `name`: V0
    - `type`: float
    - `unit`: Å^3
    - `name`: B0
    - `type`: float
    - `unit`: GPa
    - `name`: B_prime
    - `type`: float
    - `name`: DV_percent
    - `type`: float
    - `unit`: %
    - `name`: DB_percent
    - `type`: float
    - `unit`: %

### elastic_constants.txt
- path: `/app/outputs/elastic_constants.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Elastic constants for the most stable Al23O27N5 structure computed with GGA.
- schema:
  - `type`: text
  - `format`: key-value entries
  - `fields`:
    - `name`: functional
    - `type`: string
    - `name`: C11
    - `type`: float
    - `unit`: GPa
    - `name`: C12
    - `type`: float
    - `unit`: GPa
    - `name`: C44
    - `type`: float
    - `unit`: GPa

Notes: All outputs should be generated from first-principles DFT re-calculations using the open-source Quantum ESPRESSO code. The reference targets are based on the paper-reported values and will be compared with tolerances that reflect expected differences due to code/pseudopotential variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "al24o24n8_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "functional",
          "total_energy",
          "volume",
          "d_NN"
        ],
        "columns": {
          "model": {
            "type": "int",
            "description": "Model index (1,2,3)"
          },
          "functional": {
            "type": "string",
            "description": "GGA or LDA"
          },
          "total_energy": {
            "type": "float",
            "unit": "eV"
          },
          "volume": {
            "type": "float",
            "unit": "Å^3"
          },
          "d_NN": {
            "type": "float",
            "unit": "Å"
          }
        }
      },
      "description": "Total energies, volumes, and nearest-neighbour N–N distances for the three ordered Al24O24N8 configurations, calculated with GGA and LDA."
    },
    {
      "file": "al23o27n5_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "functional",
          "total_energy",
          "volume",
          "band_gap"
        ],
        "columns": {
          "model": {
            "type": "int",
            "description": "Model index (1..7)"
          },
          "functional": {
            "type": "string",
            "description": "GGA or LDA"
          },
          "total_energy": {
            "type": "float",
            "unit": "eV"
          },
          "volume": {
            "type": "float",
            "unit": "Å^3"
          },
          "band_gap": {
            "type": "float",
            "unit": "eV"
          }
        }
      },
      "description": "Total energies, volumes, and electronic band gaps for the seven Al23O27N5 vacancy models, calculated with GGA and LDA."
    },
    {
      "file": "bulk_modulus_fit.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "format": "key-value entries",
        "fields": [
          {
            "name": "functional",
            "type": "string"
          },
          {
            "name": "V0",
            "type": "float",
            "unit": "Å^3"
          },
          {
            "name": "B0",
            "type": "float",
            "unit": "GPa"
          },
          {
            "name": "B_prime",
            "type": "float"
          },
          {
            "name": "DV_percent",
            "type": "float",
            "unit": "%"
          },
          {
            "name": "DB_percent",
            "type": "float",
            "unit": "%"
          }
        ]
      },
      "description": "Birch-Murnaghan EOS fitting results for the most stable Al23O27N5 model (model 1) with GGA and LDA."
    },
    {
      "file": "elastic_constants.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "format": "key-value entries",
        "fields": [
          {
            "name": "functional",
            "type": "string"
          },
          {
            "name": "C11",
            "type": "float",
            "unit": "GPa"
          },
          {
            "name": "C12",
            "type": "float",
            "unit": "GPa"
          },
          {
            "name": "C44",
            "type": "float",
            "unit": "GPa"
          }
        ]
      },
      "description": "Elastic constants for the most stable Al23O27N5 structure computed with GGA."
    }
  ],
  "notes": "All outputs should be generated from first-principles DFT re-calculations using the open-source Quantum ESPRESSO code. The reference targets are based on the paper-reported values and will be compared with tolerances that reflect expected differences due to code/pseudopotential variations."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. The checker compares your submitted results — values and relative trends — against expected reference data (hidden) using appropriate tolerances. For example, it verifies that the computed total energies correctly identify the most stable configurations and that derived properties (bond distances, bulk modulus, elastic constants, band gap) lie within acceptable physical ranges of the paper's reported values. Each scored artifact contributes a weighted fraction to the overall reward; the final reward is a single number in [0, 1] that combines these per‑artifact scores. Genuinely executing the DFT pipeline and producing the required files is necessary to achieve a high score — simply reporting numbers without computation will not satisfy the verification checks.
