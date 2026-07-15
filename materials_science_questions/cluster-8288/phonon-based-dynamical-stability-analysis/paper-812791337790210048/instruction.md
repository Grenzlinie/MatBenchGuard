# First-principles prediction of superhard metallic boron nitride

## Problem background
The search for new materials that simultaneously exhibit extreme hardness and metallic electrical conductivity is crucial for multifunctional devices operating under harsh conditions. Among candidate systems, nitrogen-rich boron nitride compounds are promising because they can form strong covalent networks and may allow electronic delocalization. This task investigates a predicted boron nitride phase, t – B₂N₃, examining whether it is mechanically stable, displays superhard elastic properties, metallic character, and high energy density. The following computational workflow reproduces the key material properties of this phase.

## Approach
The work follows a first-principles computational protocol. Starting from an initial crystal structure for t – B₂N₃ (provided as a resource), density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation is used throughout. The geometry is relaxed, and then a series of post-processing calculations is performed: elastic constants are obtained from finite-strain deformations; electronic band structure and projected density of states reveal conductivity; total energies of the candidate phase, hexagonal BN, and molecular N₂ are combined to obtain the energy density of decomposition. The reproduction uses an open-source plane-wave DFT code (Quantum ESPRESSO) and public pseudopotentials from the SSSP library, replacing the original proprietary toolchain.

## Reproduction target
The objective is to compute and deliver two scored artifacts: (1) an optimized crystal structure of t – B₂N₃ in CIF format, and (2) a JSON file containing the set of mechanical, electronic, and energetic properties listed in the output contract. Specifically, using the provided initial POSCAR, relax the geometry, export the relaxed unit cell and fractional coordinates as optimized_structure.cif. Then compute the six independent elastic constants (C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆), the bulk and shear moduli via the Voigt-Reuss-Hill approximation, the G₀/B₀ ratio, the energy density (kJ/g) from the decomposition t – B₂N₃ → h-BN + N₂, and the band gap together with a metallicity indicator. All values are placed in calculated_properties.json. The workflow must be executed entirely within the sandbox; the initial structure is the only provided input.

## Assets

- Initial t-B₂N₃ structure (POSCAR format)
- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/download
- SSSP Pseudopotentials (PBE) for B and N: https://www.materialscloud.org/discover/sssp/table/pbe

## Workflow steps

### Step 1: DFT relaxation of t-B₂N₃
- Role: process
- Action: Perform DFT geometry optimization of the provided initial t-B₂N₃ structure using Quantum ESPRESSO with the PBE functional and appropriate pseudopotentials to obtain the relaxed structure and total energy.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Save optimized structure as CIF
- Role: scored
- Action: Export the relaxed t-B₂N₃ geometry from the previous step as a CIF file containing the unit cell parameters and fractional coordinates of all B and N atoms.
- Output file: `/app/outputs/optimized_structure.cif`
- Format: other
- Contract: CIF file; the checker will parse it to measure N–N, B–N1, and B–N2 bond lengths.
- Scoring: scored by hidden verifier

### Step 3: Compute elastic, electronic, and energy properties
- Role: scored (load-bearing)
- Action: Using the relaxed structure from step 1, compute elastic constants via finite-strain method, electronic band structure and projected density of states, and total energies of h‑BN and molecular N₂ to calculate the energy density of the decomposition t‑B₂N₃ → h‑BN + N₂. Collect all results in a JSON file.
- Output file: `/app/outputs/calculated_properties.json`
- Format: json
- Contract: Object with keys: c11, c12, c13, c33, c44, c66 (all numeric, GPa), bulk_modulus (GPa), shear_modulus (GPa), g_over_b_ratio (numeric), energy_density_kJ_g (numeric), is_metallic (boolean), band_gap_eV (numeric).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structure.cif`
- `/app/outputs/calculated_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structure.cif
- path: `/app/outputs/optimized_structure.cif`
- format: other
- purpose: scored
- target_policy: reference_match
- description: Relaxed crystal structure of t‑B₂N₃. Bond lengths are checked against the paper's reported values (N–N 1.33 Å, B–N1 1.53 Å, B–N2 1.59 Å) with a 3 % tolerance.
- schema:
  - `type`: other
  - `description`: CIF file; the checker parses it and computes N–N, B–N1, and B–N2 bond lengths from the fractional coordinates and unit cell, comparing them to hidden paper-reported values within a tolerance.

### calculated_properties.json
- path: `/app/outputs/calculated_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed properties of t‑B₂N₃. Numeric values are compared to hidden paper-reported references with tolerances; is_metallic must be true and band_gap_eV ≤ 0.1 eV. The G₀/B₀ ratio is used as an empirical indicator of superhardness.
- schema:
  - `type`: object
  - `required`:
    - `c11`: number
    - `c12`: number
    - `c13`: number
    - `c33`: number
    - `c44`: number
    - `c66`: number
    - `bulk_modulus`: number
    - `shear_modulus`: number
    - `g_over_b_ratio`: number
    - `energy_density_kJ_g`: number
    - `is_metallic`: boolean
    - `band_gap_eV`: number
  - `units`:
    - `c11`: GPa
    - `c12`: GPa
    - `c13`: GPa
    - `c33`: GPa
    - `c44`: GPa
    - `c66`: GPa
    - `bulk_modulus`: GPa
    - `shear_modulus`: GPa
    - `g_over_b_ratio`: unitless
    - `energy_density_kJ_g`: kJ/g
    - `band_gap_eV`: eV

Notes: The agent must use the PBE functional and public pseudopotentials. Any open-source DFT code that provides comparable accuracy is acceptable. The provided initial POSCAR must be used as the starting geometry. All calculations are at 0 GPa.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structure.cif",
      "format": "other",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "description": "CIF file; the checker parses it and computes N–N, B–N1, and B–N2 bond lengths from the fractional coordinates and unit cell, comparing them to hidden paper-reported values within a tolerance."
      },
      "description": "Relaxed crystal structure of t‑B₂N₃. Bond lengths are checked against the paper's reported values (N–N 1.33 Å, B–N1 1.53 Å, B–N2 1.59 Å) with a 3 % tolerance."
    },
    {
      "file": "calculated_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11": "number",
          "c12": "number",
          "c13": "number",
          "c33": "number",
          "c44": "number",
          "c66": "number",
          "bulk_modulus": "number",
          "shear_modulus": "number",
          "g_over_b_ratio": "number",
          "energy_density_kJ_g": "number",
          "is_metallic": "boolean",
          "band_gap_eV": "number"
        },
        "units": {
          "c11": "GPa",
          "c12": "GPa",
          "c13": "GPa",
          "c33": "GPa",
          "c44": "GPa",
          "c66": "GPa",
          "bulk_modulus": "GPa",
          "shear_modulus": "GPa",
          "g_over_b_ratio": "unitless",
          "energy_density_kJ_g": "kJ/g",
          "band_gap_eV": "eV"
        }
      },
      "description": "Computed properties of t‑B₂N₃. Numeric values are compared to hidden paper-reported references with tolerances; is_metallic must be true and band_gap_eV ≤ 0.1 eV. The G₀/B₀ ratio is used as an empirical indicator of superhardness."
    }
  ],
  "notes": "The agent must use the PBE functional and public pseudopotentials. Any open-source DFT code that provides comparable accuracy is acceptable. The provided initial POSCAR must be used as the starting geometry. All calculations are at 0 GPa."
}
```

## How you are scored
Each scored artifact is independently inspected by a hidden verifier. The verifier checks the CIF file by parsing the cell and atomic positions, measuring the N – N and B – N bond lengths, and comparing them to reference values within a tolerance. The JSON file is read, and every reported numeric property is compared to reference values derived from the original study. The metallicity indicator (boolean) and band gap are checked against expected thresholds. Both outputs contribute to a combined reward, with the property file carrying the larger weight because it captures multiple derived quantities. Simply printing the paper's numbers is not sufficient; the verifier expects results that genuinely follow from the DFT workflow.
