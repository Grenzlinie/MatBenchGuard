# First-Principles Classification of Spin-Dependent Electronic and Magnetic Properties in Fluorinated Graphene Nanoribbons

## Problem background
Graphene nanoribbons (GNRs) exhibit electronic and magnetic properties that can be tuned by chemical doping. Fluorination introduces strong chemical bonds with carbon and is predicted to give rise to distinct spin-dependent behaviour, including non-magnetic semiconductors and metals, ferromagnetic metals, and antiferromagnetic semiconductors with or without spin splitting. First-principles density-functional-theory (DFT) calculations can determine, for a given GNR configuration, its energy band gap, magnetic moment, spin-density pattern, and corresponding spin/electronic category. This task reproduces such an analysis for a set of pristine and fluorine‑doped armchair (NA=12) and zigzag (NZ=8) nanoribbons using an open‑source DFT code.

## Approach
Use spin‑polarised DFT with the Perdew‑Burke‑Ernzerhof (PBE) exchange‑correlation functional and standard pseudopotentials (e.g. from the SSSP library). For each required pristine and fluorine‑doped configuration:

1. Build the atomic structure and perform a spin‑polarised geometry relaxation to obtain the stable lattice geometry and initial magnetic moments.
2. On the relaxed geometry, run a self‑consistent field (SCF) calculation with a dense k‑mesh and compute the spin‑polarised band structure along the Γ–X direction and the spin density.
3. From the electronic structure, extract the energy band gap (direct or indirect; set to 0.0 eV if the system is metallic) and the total magnetic moment per unit cell. Determine the presence of spin splitting by comparing spin–up and spin–down bands.
4. Classify each configuration into exactly one of five categories based on the gap, moment, spin splitting, and spin‑density ordering: NM_Semiconductor, NM_Metal, FM_Metal, AFM_Semiconductor_no_split, AFM_Semiconductor_with_split.

The workflow is implemented with Quantum ESPRESSO (pw.x, bands.x) and the results are collected into a single CSV file.

## Reproduction target
Produce a CSV file results_table.csv that, for each specified GNR configuration, reports the energy band gap (eV; 0.0 if metallic), the gap type (direct, indirect, metal), the total magnetic moment per unit cell (μB), and the spin‑dependent electronic/magnetic classification. The file must have columns: configuration_name, band_gap_eV, gap_type, magnetic_moment_muB, classification. The reported quantities will be compared against hidden reference values to verify the reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE Pseudopotentials (or equivalent): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry relaxation
- Role: process
- Action: Build atomic structures for pristine AGNR (NA=12), pristine ZGNR (NZ=8), and the specified fluorine-doped configurations (list taken from the paper's Table 1: (13)s, (1)s, (6,21)s, (6,21)d, (1,6)d, (1,23)s, (1,23)d, (3)s, (3,30)s, (3,30)d, (11,14)d, (3,14)d). For each, perform spin-polarized DFT geometry optimization using Quantum ESPRESSO pw.x (PBE functional, plane‑wave cutoff ≥ 60 Ry, k‑mesh ~15×1×1, vacuum ≥ 15 Å in y and z). Save relaxed coordinates and optimization logs.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Electronic structure calculation
- Role: process
- Action: For each relaxed configuration, run an SCF calculation with a dense k‑mesh (≥ 100×1×1) and compute the spin-polarized band structure along the Γ‑X path. Also compute the spin density. Store all raw DFT output files.
- Evidence: `/app/outputs/scf_bands_output.txt`

### Step 3: Extract band gaps, magnetic moments, and classify
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract the energy band gap (set to 0.0 if metallic; specify direct/indirect/metal) and the total magnetic moment per unit cell for each configuration. Determine the presence of spin splitting by comparing spin‑up and spin‑down band energies. Classify each configuration into exactly one category: NM_Semiconductor, NM_Metal, FM_Metal, AFM_Semiconductor_no_split, AFM_Semiconductor_with_split, based on gap, moment, spin splitting, and spin‑density pattern. Write a CSV file results_table.csv with columns: configuration_name, band_gap_eV, gap_type, magnetic_moment_muB, classification. The configuration_name must be exactly one of: AGNR_N12_pristine, AGNR_13s, AGNR_1s, AGNR_6_21s, AGNR_6_21d, AGNR_1_6d, AGNR_1_23s, AGNR_1_23d, ZGNR_N8_pristine, ZGNR_3s, ZGNR_3_30s, ZGNR_3_30d, ZGNR_11_14d, ZGNR_3_14d.
- Output file: `/app/outputs/results_table.csv`
- Format: csv
- Contract: CSV with columns: configuration_name (string, must be one of the listed canonical names), band_gap_eV (float, 0.0 if metallic), gap_type (string: direct, indirect, metal), magnetic_moment_muB (float, 0.0 if non-magnetic/antiferromagnetic), classification (string: NM_Semiconductor, NM_Metal, FM_Metal, AFM_Semiconductor_no_split, AFM_Semiconductor_with_split).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_table.csv
- path: `/app/outputs/results_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted band gaps (eV), magnetic moments (μB), gap type, and spin-dependent electronic/magnetic classification for each GNR configuration. The configuration_name must be exactly one of the canonical names listed in the schema.
- schema:
  - `type`: table
  - `required_columns`: `configuration_name`, `band_gap_eV`, `gap_type`, `magnetic_moment_muB`, `classification`
  - `units`:
    - `band_gap_eV`: eV
    - `magnetic_moment_muB`: μB
  - `configuration_name_values`: `AGNR_N12_pristine`, `AGNR_13s`, `AGNR_1s`, `AGNR_6_21s`, `AGNR_6_21d`, `AGNR_1_6d`, `AGNR_1_23s`, `AGNR_1_23d`, `ZGNR_N8_pristine`, `ZGNR_3s`, `ZGNR_3_30s`, `ZGNR_3_30d`, `ZGNR_11_14d`, `ZGNR_3_14d`

Notes: The hidden checker maps each row by configuration_name and compares band_gap_eV and magnetic_moment_muB against gold values (tolerances ±0.1 eV and ±0.05 μB) and validates classification consistency. Only rows with the exact canonical configuration names listed in the schema will be recognised.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration_name",
          "band_gap_eV",
          "gap_type",
          "magnetic_moment_muB",
          "classification"
        ],
        "units": {
          "band_gap_eV": "eV",
          "magnetic_moment_muB": "μB"
        },
        "configuration_name_values": [
          "AGNR_N12_pristine",
          "AGNR_13s",
          "AGNR_1s",
          "AGNR_6_21s",
          "AGNR_6_21d",
          "AGNR_1_6d",
          "AGNR_1_23s",
          "AGNR_1_23d",
          "ZGNR_N8_pristine",
          "ZGNR_3s",
          "ZGNR_3_30s",
          "ZGNR_3_30d",
          "ZGNR_11_14d",
          "ZGNR_3_14d"
        ]
      },
      "description": "Extracted band gaps (eV), magnetic moments (μB), gap type, and spin-dependent electronic/magnetic classification for each GNR configuration. The configuration_name must be exactly one of the canonical names listed in the schema."
    }
  ],
  "notes": "The hidden checker maps each row by configuration_name and compares band_gap_eV and magnetic_moment_muB against gold values (tolerances ±0.1 eV and ±0.05 μB) and validates classification consistency. Only rows with the exact canonical configuration names listed in the schema will be recognised."
}
```

## How you are scored
A hidden verifier reads your results_table.csv. For each listed configuration, it checks whether the band gap and magnetic moment you report agree with reference values within set tolerances, and whether the classification is internally consistent with those quantities. The final reward is proportional to the number of configurations that pass both the numerical checks and the classification assessment. Submitting the file is not enough; the values must be obtained from the specified DFT workflow.
