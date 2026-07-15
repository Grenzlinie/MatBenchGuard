# H-Si-P Monolayer Band Edge and Bandgap under Biaxial Strain

## Problem background
Monolayer hydrogenated silicon phosphide (H-Si-P) structures have been proposed as stable two-dimensional semiconductors. Their electronic structure, in particular the band gap and the absolute positions of the conduction and valence band edges, is expected to change under applied biaxial strain, which could make them suitable for photocatalytic water splitting. This task aims to compute these strain-dependent electronic properties for three monolayer H-Si-P configurations using density functional theory.

## Approach
Three monolayer structures, referred to as HPSi, HSiP, and HSiPbp, differing in the hydrogenation pattern, are constructed. Their atomic geometries are relaxed with a PBE exchange-correlation functional. A series of biaxial strains from -10% (compressive) to +10% (tensile) in 1% steps is then applied to each relaxed structure, and the internal coordinates are re-relaxed while keeping the strained in-plane lattice constants fixed. For every strain level, a hybrid functional calculation (HSE06) is performed to obtain the band gap and the absolute energies of the conduction band minimum (CBM) and valence band maximum (VBM) relative to vacuum by referencing the electrostatic potential in the vacuum region. The results are compiled into two data tables: one reporting the band gap versus strain, and the other reporting the CBM and VBM positions versus strain. At zero strain, the band edge alignment with the water redox potentials is also examined.

## Reproduction target
Produce two CSV files under `/app/outputs`:

1. `bandgap_vs_strain.csv` — columns: `structure` (one of HPSi, HSiP, HSiPbp), `strain` (biaxial strain in percent), `bandgap` (in eV).
2. `band_edges_vs_strain.csv` — columns: `structure`, `strain`, `CBM` (eV, relative to vacuum), `VBM` (eV, relative to vacuum).

Cover strain values from -10% to +10% in steps no larger than 1% for each structure. Additionally, use the zero-strain data to verify that the computed band edges straddle the water redox potentials (the reduction potential at -4.44 eV and the oxidation potential at -5.67 eV relative to vacuum).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP norm-conserving pseudopotentials: https://www.materialscloud.org/discover/sssp/table
- pymatgen: pymatgen

## Workflow steps

### Step 1: Construct initial monolayer structures
- Role: process
- Action: Build the three monolayer structures (HPSi, HSiP, HSiPbp) with initial atomic positions and unit cells. HPSi and HSiP: space group P3M1, lattice constant ~3.55 Å. HSiPbp: space group PMN21, a ~3.53 Å, b ~5.57 Å. Include a vacuum layer of at least 23 Å along the c-axis.
- Evidence: `/app/outputs/initial_structures.cif`

### Step 2: Relax structures with PBE
- Role: process
- Action: Using a norm-conserving pseudopotential with PBE functional and a sufficiently high plane-wave cutoff, relax atomic positions and cell parameters until forces and energy are converged. Obtain equilibrium lattice constants and relaxed total energies.
- Evidence: `/app/outputs/relaxed_structures.cif`

### Step 3: Generate and relax strained structures
- Role: process
- Action: For each relaxed unstrained structure, apply biaxial strain η from -10% to +10% in steps of 1% by scaling in-plane lattice constants and re-relaxing internal coordinates while keeping the strained cell dimensions fixed.
- Evidence: `/app/outputs/strained_structures.cif`

### Step 4: HSE06 band structure and work function calculations
- Role: process
- Action: For each strained (and unstrained) relaxed structure, perform a HSE06 calculation to determine the band gap E_g, and compute the absolute conduction band minimum (CBM) and valence band maximum (VBM) energies relative to vacuum using the electrostatic potential in the vacuum region.
- Evidence: `/app/outputs/hse06_raw_data.json`

### Step 5: Compile bandgap vs strain data
- Role: scored
- Action: Extract the bandgap for each structure and strain from the HSE06 calculations. Write /app/outputs/bandgap_vs_strain.csv with columns: structure, strain, bandgap.
- Output file: `/app/outputs/bandgap_vs_strain.csv`
- Format: csv
- Contract: CSV with columns: structure (string, one of HPSi/HSiP/HSiPbp), strain (float, biaxial strain in percent), bandgap (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Compile band edge positions vs strain
- Role: scored (load-bearing)
- Action: From the HSE06 work function calculations, derive the absolute CBM and VBM energies relative to vacuum for each structure and strain. Write /app/outputs/band_edges_vs_strain.csv with columns: structure, strain, CBM, VBM.
- Output file: `/app/outputs/band_edges_vs_strain.csv`
- Format: csv
- Contract: CSV with columns: structure (string), strain (float, percent), CBM (float, eV relative to vacuum), VBM (float, eV relative to vacuum).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap_vs_strain.csv`
- `/app/outputs/band_edges_vs_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap_vs_strain.csv
- path: `/app/outputs/bandgap_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Bandgap vs strain data for the three monolayer H-Si-P structures, used to verify the bandgap ranges and trends reported in the paper.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `strain`, `bandgap`
  - `units`:
    - `strain`: percent
    - `bandgap`: eV

### band_edges_vs_strain.csv
- path: `/app/outputs/band_edges_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Absolute band edge positions (CBM and VBM) vs strain, used to verify alignment with water redox potentials and strain-tunability.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `strain`, `CBM`, `VBM`
  - `units`:
    - `strain`: percent
    - `CBM`: eV
    - `VBM`: eV

Notes: The checker will compare selected values and trends against the paper's reported data with appropriate tolerances. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "strain",
          "bandgap"
        ],
        "units": {
          "strain": "percent",
          "bandgap": "eV"
        }
      },
      "description": "Bandgap vs strain data for the three monolayer H-Si-P structures, used to verify the bandgap ranges and trends reported in the paper."
    },
    {
      "file": "band_edges_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "strain",
          "CBM",
          "VBM"
        ],
        "units": {
          "strain": "percent",
          "CBM": "eV",
          "VBM": "eV"
        }
      },
      "description": "Absolute band edge positions (CBM and VBM) vs strain, used to verify alignment with water redox potentials and strain-tunability."
    }
  ],
  "notes": "The checker will compare selected values and trends against the paper's reported data with appropriate tolerances. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier program will inspect your two CSV files. It will compare your reported bandgap and band edge values at selected strain points against reference data derived from the original study. It will also check that, at zero strain, the band edges are correctly positioned relative to the water redox potentials. The overall reward is a weighted sum of per‑artifact scores. The check is fully automated; you must run the DFT workflow yourself and submit genuine computed numbers—simply reporting the paper’s published values without performing the calculations will not pass the verification.
