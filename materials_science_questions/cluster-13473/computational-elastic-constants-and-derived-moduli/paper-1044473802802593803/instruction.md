# Reproduce mechanical properties of solvated RGD peptide (1FUV) via DFT stress-strain and VRH averaging

## Problem background
Biological molecules possess mechanical properties that are crucial for their function, influencing cellular adhesion, mechanotransduction, and material design. Understanding the stiffness and deformation behavior of biomolecules in their native solvated environment is essential for interpreting their role in biological processes. The solvated RGD peptide (PDB ID: 1FUV), a small integrin-recognition peptide, serves as a tractable model system for computing elastic moduli from first principles. This task re-runs the ab initio calculation of bulk modulus K, shear modulus G, Young's modulus E, and Poisson's ratio η for the solvated RGD peptide subjected to small strains, providing quantitative insight into its mechanical response.

## Approach
The mechanical properties are obtained through a sequence of density functional theory (DFT) calculations combined with the Voigt–Reuss–Hill (VRH) averaging scheme. The workflow begins by solvating the RGD peptide retrieved from the Protein Data Bank (1FUV). A 3 Å water shell containing 155 water molecules is added using the PACKMOL tool, yielding a system of 600 atoms. The solvated structure is then relaxed via DFT using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and a plane‑wave basis under periodic boundary conditions. From the optimized geometry, a stress‑strain protocol based on the Nielsen–Martin method is employed: symmetric small strains of ±0.25%, ±0.50%, ±0.75%, ±1.00%, ±1.25%, ±1.50%, ±1.75%, ±2.00%, ±2.25%, and ±2.50% are applied, and the stress response is computed to extract the elastic stiffness tensor C_ij. To capture solvent‑induced variability, the entire strain calculation is repeated five times with different initial configurations (e.g., varying random seeds for water placement or applying small random perturbations). For each strain magnitude and each independent set, the compliance tensor S_ij is derived, and the Voigt and Reuss bounds for the bulk and shear moduli are evaluated. The Hill averages (K, G) are then obtained, and Young's modulus E and Poisson's ratio η are computed from these averages. Finally, the mean and standard deviation of K, G, E, and η across the five sets are reported for each strain percentage.

## Reproduction target
Compute the mean and standard deviation of the Voigt–Reuss–Hill averaged bulk modulus K, shear modulus G, Young's modulus E, and Poisson's ratio η for the solvated RGD peptide (1FUV) at each of the ten positive strain percentages: 0.25%, 0.50%, 0.75%, 1.00%, 1.25%, 1.50%, 1.75%, 2.00%, 2.25%, and 2.50%. The statistics must be derived from five independent simulation sets for each strain. Produce a single CSV file, `/app/outputs/elastic_moduli_results.csv`, with columns: strain_percent, bulk_modulus_mean, bulk_modulus_std, shear_modulus_mean, shear_modulus_std, youngs_modulus_mean, youngs_modulus_std, poisson_ratio_mean, poisson_ratio_std. All moduli are expressed in GPa, and Poisson's ratio is dimensionless. The strain dependence of the moduli should allow an assessment of how the mechanical properties vary with increasing strain.

## Assets

- RGD 1FUV structure: https://www.rcsb.org/structure/1FUV
- PACKMOL: http://m3g.iqm.unicamp.br/packmol
- Quantum ESPRESSO (or CP2K or VASP): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build solvated RGD model
- Role: process
- Action: Download the 1FUV PDB structure from RCSB. Using PACKMOL, construct a solvation box with a 3 Å water shell containing 155 water molecules. Write the initial coordinate file for the solvated system (600 atoms).
- Evidence: `/app/outputs/initial_solvated_coords.xyz`

### Step 2: DFT geometry optimization
- Role: process
- Action: Relax the solvated structure using DFT with the PBE functional, a suitable plane-wave energy cutoff, and a single k-point. Archive the optimized atomic coordinates.
- Evidence: `/app/outputs/optimized_geometry.xyz`

### Step 3: DFT elastic tensor calculation via stress-strain
- Role: process
- Action: From the optimized geometry, apply the Nielsen–Martin stress-strain protocol: apply symmetric small strains (±0.25%, ±0.50%, ±0.75%, ±1.00%, ±1.25%, ±1.50%, ±1.75%, ±2.00%, ±2.25%, ±2.50%) and compute the stress response using DFT. Repeat the entire set of strain calculations five times, with different random seeds or initial perturbations to simulate solvent variability. For each of the five independent sets and each strain magnitude, extract the elastic stiffness tensor C_ij and compliance tensor S_ij.
- Evidence: `/app/outputs/elastic_tensors_log.txt`

### Step 4: Compute VRH moduli and statistics
- Role: scored (load-bearing)
- Action: For each of the five independent sets and each of the ten positive strain magnitudes, compute the compliance tensor S_ij, then the Voigt bounds (K_Voigt, G_Voigt) and Reuss bounds (K_Reuss, G_Reuss). Average them to get Hill averages K and G. Derive Young's modulus E = 9KG/(3K+G) and Poisson's ratio η = (3K-2G)/(2(3K+G)). For each strain percentage, calculate the mean and standard deviation of K, G, E, η across the five sets. Write the results to /app/outputs/elastic_moduli_results.csv.
- Output file: `/app/outputs/elastic_moduli_results.csv`
- Format: csv
- Contract: CSV with 10 rows, one per strain percentage. Columns: strain_percent (float, unit: %), bulk_modulus_mean (float, GPa), bulk_modulus_std (float, GPa), shear_modulus_mean (float, GPa), shear_modulus_std (float, GPa), youngs_modulus_mean (float, GPa), youngs_modulus_std (float, GPa), poisson_ratio_mean (float, dimensionless), poisson_ratio_std (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli_results.csv
- path: `/app/outputs/elastic_moduli_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard deviation of Voigt–Reuss–Hill averaged bulk modulus K, shear modulus G, Young's modulus E, and Poisson's ratio η for solvated RGD (1FUV) at ten strain percentages (0.25% to 2.50%), obtained from five independent DFT stress–strain calculation sets.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `bulk_modulus_mean`, `bulk_modulus_std`, `shear_modulus_mean`, `shear_modulus_std`, `youngs_modulus_mean`, `youngs_modulus_std`, `poisson_ratio_mean`, `poisson_ratio_std`
  - `units`:
    - `strain_percent`: %
    - `bulk_modulus_mean`: GPa
    - `bulk_modulus_std`: GPa
    - `shear_modulus_mean`: GPa
    - `shear_modulus_std`: GPa
    - `youngs_modulus_mean`: GPa
    - `youngs_modulus_std`: GPa
    - `poisson_ratio_mean`: dimensionless
    - `poisson_ratio_std`: dimensionless

Notes: The hidden checker compares the reported mean values for K, G, E, η at each strain to the paper's Table S1 within tolerances and verifies the overall decreasing trend with increasing strain. Bonding analysis (TBOD, AABP) requires the proprietary OLCAO code and is excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "bulk_modulus_mean",
          "bulk_modulus_std",
          "shear_modulus_mean",
          "shear_modulus_std",
          "youngs_modulus_mean",
          "youngs_modulus_std",
          "poisson_ratio_mean",
          "poisson_ratio_std"
        ],
        "units": {
          "strain_percent": "%",
          "bulk_modulus_mean": "GPa",
          "bulk_modulus_std": "GPa",
          "shear_modulus_mean": "GPa",
          "shear_modulus_std": "GPa",
          "youngs_modulus_mean": "GPa",
          "youngs_modulus_std": "GPa",
          "poisson_ratio_mean": "dimensionless",
          "poisson_ratio_std": "dimensionless"
        }
      },
      "description": "Mean and standard deviation of Voigt–Reuss–Hill averaged bulk modulus K, shear modulus G, Young's modulus E, and Poisson's ratio η for solvated RGD (1FUV) at ten strain percentages (0.25% to 2.50%), obtained from five independent DFT stress–strain calculation sets."
    }
  ],
  "notes": "The hidden checker compares the reported mean values for K, G, E, η at each strain to the paper's Table S1 within tolerances and verifies the overall decreasing trend with increasing strain. Bonding analysis (TBOD, AABP) requires the proprietary OLCAO code and is excluded."
}
```

## How you are scored
A hidden verifier evaluates your `elastic_moduli_results.csv`. It compares the reported mean values for K, G, E, and η at each strain to a hidden reference (the paper‑reported values) using tolerances that account for legitimate variations arising from different DFT codes, pseudopotentials, and computational settings. It also verifies that the standard deviations are positive and that the qualitative strain dependence of the moduli matches the expected physical behavior. The final reward is a weighted combination of these component checks; merely stating numbers without correctly executing the computational workflow will not earn full credit because the verifier scrutinizes both the magnitude and the trend of the results.
