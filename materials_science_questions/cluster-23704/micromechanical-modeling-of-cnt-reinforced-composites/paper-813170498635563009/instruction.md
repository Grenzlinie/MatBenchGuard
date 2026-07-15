# Functionalized Carbon Nanotube Properties from DFT Simulations

## Problem background
Covalently functionalized carbon nanotubes (CNTs) are promising candidates for composite materials and nanoelectronic devices. Attaching functional groups such as –OH and –COOH modifies the CNTs' structure, elastic response, and electronic states. Quantifying how the equilibrium radius, Young's modulus, and electronic band gap depend on the type and concentration of the functional groups is essential for engineering these systems. This task uses first-principles density functional theory (DFT) to compute these three properties across a defined set of CNT chirality–functional group–concentration combinations, establishing the concentration-dependent trends.

## Approach
The calculations are carried out in the framework of density functional theory (DFT) using the generalized gradient approximation (GGA) for exchange and correlation together with norm-conserving pseudopotentials. Periodic supercell models of pristine (9,0) and (10,0) single-walled carbon nanotubes are constructed. –OH and –COOH groups are covalently attached at surface coverages ranging from 0 % (pristine) up to 12.5 %. For every system, full geometry optimization is performed to obtain the relaxed atomic coordinates. On the relaxed geometry, the electronic band structure is computed along the high-symmetry path to determine the band gap, and a series of uniaxial tensile strains is applied along the tube axis; the resulting stress–strain data are fitted in the linear elastic regime to extract Young's modulus. The equilibrium tube radius is evaluated from the relaxed atomic positions. All results are compiled in a single table for comparison across chiralities, functional groups, and concentrations.

## Reproduction target
Produce a CSV file containing the equilibrium radius (in Å), Young's modulus (in TPa), and band gap (in eV) for every combination of chirality ((9,0) or (10,0)), functional group (pristine, OH, COOH), and concentration (0 % and values up to 12.5 %, e.g., 6.25 % and 12.5 %). The file must follow the specified schema and place the results in `/app/outputs/results.csv`. The target is to obtain concentration-dependent values that reflect the physical changes induced by functionalization, as verified by a hidden checker using reference data.

## Assets

- SIESTA: https://departments.icmab.es/leem/siesta/

## Workflow steps

### Step 1: Atomic model construction
- Role: process
- Action: Generate initial atomic coordinates for pristine (9,0) and (10,0) single-wall carbon nanotubes, and covalently attach -OH and -COOH functional groups at surface concentrations of 0% (pristine) and values up to 12.5% (e.g., 6.25%, 12.5%). Use periodic boundary conditions along the tube axis and ensure the supercell size avoids artificial interactions.
- Evidence: `/app/outputs/structures_created.log`

### Step 2: DFT relaxation, band structure, and stress-strain calculation
- Role: process
- Action: For each generated structure, perform DFT geometry optimization using GGA with norm-conserving pseudopotentials (SIESTA or equivalent open-source code) to obtain relaxed atomic coordinates and total energy. On the relaxed geometry, compute the electronic band structure to extract the band gap. Apply a series of uniaxial strains along the tube axis and run static DFT calculations at each strain to obtain the stress tensor; use the stress-strain data to extract Young's modulus by fitting the linear elastic region.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 3: Post-process and compile results
- Role: scored (load-bearing)
- Action: From the relaxed geometries, compute equilibrium tube radius (average distance of carbon atoms from the tube axis). From the band structure, extract the band gap (energy difference between highest occupied and lowest unoccupied bands at the Γ point). From the stress–strain data, fit the linear elastic region to obtain Young's modulus. Compile all values for every combination of chirality, functional group, and concentration into a single CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: chirality (string, '(9,0)' or '(10,0)'), functional_group (string, 'pristine', 'OH', 'COOH'), concentration (float, percent), radius_A (float, Angstrom), young_modulus_TPa (float, TPa), band_gap_eV (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed structural, mechanical, and electronic properties of functionalized CNTs for each condition.
- schema:
  - `type`: table
  - `required_columns`: `chirality`, `functional_group`, `concentration`, `radius_A`, `young_modulus_TPa`, `band_gap_eV`
  - `units`:
    - `radius_A`: Angstrom
    - `young_modulus_TPa`: TPa
    - `band_gap_eV`: eV
    - `concentration`: percent

Notes: The hidden checker will compare the reported values against paper-derived gold values, verifying monotonic trends for radius and Young's modulus, absolute errors within tolerance, and the metallic transition for a specific semiconducting CNT under certain functionalization conditions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "chirality",
          "functional_group",
          "concentration",
          "radius_A",
          "young_modulus_TPa",
          "band_gap_eV"
        ],
        "units": {
          "radius_A": "Angstrom",
          "young_modulus_TPa": "TPa",
          "band_gap_eV": "eV",
          "concentration": "percent"
        }
      },
      "description": "Computed structural, mechanical, and electronic properties of functionalized CNTs for each condition."
    }
  ],
  "notes": "The hidden checker will compare the reported values against paper-derived gold values, verifying monotonic trends for radius and Young's modulus, absolute errors within tolerance, and the metallic transition for a specific semiconducting CNT under certain functionalization conditions."
}
```

## How you are scored
A hidden verifier reads your `results.csv` and independently scores it against a set of accepted reference values derived from the underlying study. The checker validates three aspects: (i) monotonic trends — whether the radius and Young's modulus change in the expected qualitative direction as concentration increases; (ii) quantitative accuracy — whether the computed values fall within generous tolerance bands that account for differences in DFT implementations; and (iii) a key electronic transition — whether the band gap of a specific semiconductor becomes metallic under certain conditions. Each aspect contributes to a weighted total reward, with the strongest emphasis on trend agreement and the correct electronic-transition behaviour. Reporting the paper's numbers without performing the required DFT workflow will not satisfy the scoring criteria; the verifier evaluates the computed results produced by your pipeline.
