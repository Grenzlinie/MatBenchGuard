# Reproduce mechanical properties of solvated RGD peptide (1FUV) via DFT stress‑strain and VRH averaging

## Problem background
Biological molecules possess mechanical properties that are crucial for their function, influencing cellular adhesion, mechanotransduction, and material design. Understanding the stiffness and deformation behavior of biomolecules in their native solvated environment is essential for interpreting their role in biological processes. The solvated RGD peptide (PDB ID: 1FUV), a small integrin‑recognition peptide, serves as a tractable model system for computing elastic moduli from first principles. This task computes the bulk modulus K, shear modulus G, Young’s modulus E, and Poisson’s ratio η for the solvated RGD peptide subjected to small strains, providing quantitative insight into its mechanical response.

## Approach
The mechanical properties are obtained through density functional theory (DFT) calculations combined with the Voigt–Reuss–Hill (VRH) averaging scheme. The workflow begins by solvating the RGD peptide retrieved from the Protein Data Bank (1FUV). A 3 Å water shell containing 155 water molecules is added using the PACKMOL tool, yielding a system of 600 atoms. The solvated structure is then relaxed via DFT using the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and a plane‑wave basis under periodic boundary conditions. From the optimized geometry, a stress‑strain protocol based on the Nielsen–Martin method is employed: for ten positive strain magnitudes (0.25%, 0.50%, 0.75%, 1.00%, 1.25%, 1.50%, 1.75%, 2.00%, 2.25%, 2.50%) the elastic stiffness tensor C_ij is extracted. To capture solvent‑induced variability, the entire strain calculation is repeated five times with different initial configurations (different random seeds for water placement or small random perturbations). For each strain magnitude and each independent set, the compliance tensor S_ij is derived, and the Voigt and Reuss bounds for the bulk and shear moduli are evaluated. The Hill averages (K, G) are then obtained, and Young’s modulus E and Poisson’s ratio η are computed from these averages. Finally, the mean and standard deviation of K, G, E, and η across the five sets are reported for each strain percentage.

## Reproduction target
Compute the mean and standard deviation of the Voigt–Reuss–Hill averaged bulk modulus K, shear modulus G, Young’s modulus E, and Poisson’s ratio η for the solvated RGD peptide (1FUV) at each of the ten positive strain percentages: 0.25%, 0.50%, 0.75%, 1.00%, 1.25%, 1.50%, 1.75%, 2.00%, 2.25%, and 2.50%. The statistics must be derived from five independent simulation sets for each strain. Produce a single CSV file, `/app/outputs/elastic_moduli_results.csv`, with columns: strain_percent, bulk_modulus_mean, bulk_modulus_std, shear_modulus_mean, shear_modulus_std, youngs_modulus_mean, youngs_modulus_std, poisson_ratio_mean, poisson_ratio_std. All moduli are expressed in GPa, and Poisson’s ratio is dimensionless. **Rows must appear in ascending order of strain_percent:** 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50. The column order inside the CSV is not enforced, but every row must contain all nine columns.

## Assets

- RGD 1FUV structure: https://www.rcsb.org/structure/1FUV
- PACKMOL: http://m3g.iqm.unicamp.br/packmol
- Quantum ESPRESSO (or CP2K or VASP): https://www.quantum‑espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Detailed computational parameters
To reproduce the elastic moduli reported in the paper, use the following DFT and modeling settings. These values are consistent with typical plane‑wave PBE calculations and are sufficient to obtain results within the tolerances checked by the hidden verifier.

### Solvation and unit cell
- Solvation: PACKMOL builds a water shell of 3 Å around the peptide, placing exactly 155 water molecules. Use the TIP3P or a simple rigid water model; the exact internal water geometry is not critical because DFT will relax the structure.
- Unit cell: Place the solvated system in an orthorhombic periodic box with enough vacuum to avoid spurious interactions between periodic images. A safe choice is to compute the bounding box of all atoms and add **at least 10 Å** in each Cartesian direction. For the 600‑atom system this typically results in lattice constants of ≈ 20–25 Å. Keep the cell vectors orthogonal (α = β = γ = 90°). All subsequent DFT calculations use this cell.

### DFT setup
- Functional: PBE (Perdew–Burke–Ernzerhof) exchange‑correlation.
- Pseudopotentials: Use the SSSP “efficiency” set of PBE pseudopotentials (or an equivalent standard PBE pseudopotential library). Follow the recommended plane‑wave cutoffs from the SSSP entry for each element (typically around 40 Ry for the wavefunction and 320 Ry for the charge density).
- k‑point sampling: Γ‑point only (since the cell is large and the system is non‑periodic).
- Self‑consistent field (SCF) convergence: threshold on total energy 1 × 10⁻⁶ eV.
- Geometry optimization (relaxation):
  - Convergence criteria: maximum force on any atom < 0.01 eV/Å, total energy change between steps < 1 × 10⁻⁵ eV.
  - Keep the unit cell fixed during relaxation (optimize atomic positions only); the initial cell constructed as above is already spacious enough.

### Independent sets (five repetitions)
To mimic the paper’s five independent calculations, generate five distinct initial configurations for the water shell (e.g., by running PACKMOL with five different random seeds or by applying random displacements of up to 0.1 Å to the water oxygen atoms after the initial solvation). For each seed, re‑relax the geometry and carry out the entire stress‑strain protocol. This yields five independent values for every modulus at each strain.

### Nielsen–Martin stress‑strain protocol
From the optimized geometry, apply small strains to the lattice vectors and compute the stress tensor via a static DFT calculation (single‑point energy + stress). For each strain magnitude s% (s = 0.25, 0.50, …, 2.50) perform the following:

1. **Define six independent strain modes** that span the space of symmetric strain tensors. An example set using Voigt notation (xx, yy, zz, yz, xz, xy) is:
   - Mode 1: ε₁ = (η, 0, 0, 0, 0, 0)    — uniaxial along x
   - Mode 2: ε₂ = (0, η, 0, 0, 0, 0)    — uniaxial along y
   - Mode 3: ε₃ = (0, 0, η, 0, 0, 0)    — uniaxial along z
   - Mode 4: ε₄ = (0, 0, 0, 2η, 0, 0)   — pure shear yz (engineering shear 2η)
   - Mode 5: ε₅ = (0, 0, 0, 0, 2η, 0)   — pure shear xz
   - Mode 6: ε₆ = (0, 0, 0, 0, 0, 2η)   — pure shear xy
   where η = s / 100. (The factor 2 in shear components ensures consistency when computing the stiffness tensor using engineering strains.)

2. For each mode, generate two deformed cells:
   - Positive deformation: cell vectors a′ = (I + ε₊)·a, where ε₊ is the strain tensor of the mode with amplitude +η.
   - Negative deformation: cell vectors a′ = (I + ε₋)·a, with strain amplitude −η.

3. Run a static DFT calculation for the positively and negatively deformed structure (two calculations per mode, 12 per strain magnitude). Collect the stress tensor σ⁺ and σ⁻ (6‑component vector in Voigt order: σ₁ = σ_xx, σ₂ = σ_yy, σ₃ = σ_zz, σ₄ = σ_yz, σ₅ = σ_xz, σ₆ = σ_xy).

4. Build the 6×6 elastic stiffness matrix C using central differences for each mode. For mode i (i = 1…6):
   - For j = 1…6: C_ji = (σⱼ⁺ − σⱼ⁻) / (2η)
   Because the strain mode is purely along one Voigt component, this gives one column of C. After filling all six columns, symmetrize C: C_ij = (C_ij + C_ji) / 2.

   (Alternative: if the DFT code directly outputs the elastic tensor from a single finite‑difference run, use that result; otherwise the manual protocol above is acceptable.)

5. From the symmetrized C, compute the Voigt and Reuss bounds for bulk and shear moduli:
   - **Voigt bounds:**
     9·K_V = C₁₁ + C₂₂ + C₃₃ + 2·(C₁₂ + C₂₃ + C₃₁)
     15·G_V = (C₁₁ + C₂₂ + C₃₃) − (C₁₂ + C₂₃ + C₃₁) + 3·(C₄₄ + C₅₅ + C₆₆)
   - **Reuss bounds:**
     Compute compliance matrix S = C⁻¹.
     1/K_R = S₁₁ + S₂₂ + S₃₃ + 2·(S₁₂ + S₂₃ + S₃₁)
     15/G_R = 4·(S₁₁ + S₂₂ + S₃₃) − 4·(S₁₂ + S₂₃ + S₃₁) + 3·(S₄₄ + S₅₅ + S₆₆)
   - **Hill average:**
     K = (K_V + K_R) / 2
     G = (G_V + G_R) / 2

6. Derive Young’s modulus E and Poisson’s ratio η from the Hill averages:
   - E = 9·K·G / (3·K + G)
   - η_poisson = (3·K − 2·G) / (2·(3·K + G))

   Record K, G, E, and η_poisson for this strain magnitude for the current independent set.

7. After processing all ten strain magnitudes for one independent set, repeat steps 1‑6 for the remaining four independent sets. For each strain magnitude you will have five values of K, five of G, etc. Compute the mean and standard deviation of each property across the five sets. Store the means and standard deviations in the result CSV, using the column names given below. All moduli must be in GPa.

## Output files
Write all scored artifacts under `/app/outputs`:

- `/app/outputs/elastic_moduli_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli_results.csv

- path: `/app/outputs/elastic_moduli_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mean and standard deviation of Voigt–Reuss–Hill averaged bulk modulus K, shear modulus G, Young’s modulus E, and Poisson’s ratio η for solvated RGD (1FUV) at ten strain percentages (0.25% to 2.50%), obtained from five independent DFT stress–strain calculation sets.
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

- Other constraints:
  - The CSV must contain exactly **10 data rows**, one for each strain in **ascending order**: 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50.
  - All standard deviation values must be **positive** (greater than 0).
  - The average moduli (K, G, E, Poisson’s ratio) must **not be constant across all strains**; they should exhibit a physical decreasing trend with increasing strain.

Notes: The hidden checker compares the reported mean values for K, G, E, η at each strain to a hidden reference within tolerances and verifies the overall decreasing trend with increasing strain. Bonding analysis (TBOD, AABP) requires the proprietary OLCAO code and is excluded.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

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
  "notes": "The hidden checker compares the reported mean values for K, G, E, η at each strain to a hidden reference within tolerances and verifies the overall decreasing trend with increasing strain. Bonding analysis (TBOD, AABP) requires the proprietary OLCAO code and is excluded."
}
```

## How you are scored
A hidden verifier evaluates your `elastic_moduli_results.csv`. It compares the reported mean values for K, G, E, and η at each strain to a hidden reference (the paper‑reported values) using tolerances that account for legitimate variations arising from different DFT codes, pseudopotentials, and computational settings. It also verifies that the standard deviations are positive and that the qualitative strain dependence of the moduli matches the expected physical behavior. The final reward is a weighted combination of these component checks; merely stating numbers without correctly executing the computational workflow will not earn full credit because the verifier scrutinizes both the magnitude and the trend of the results.