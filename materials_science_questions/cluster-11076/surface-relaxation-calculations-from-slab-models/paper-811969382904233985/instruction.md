# DFT and MD reproduction of H₂O adsorption on smithsonite surfaces with defects and impurities

## Problem background
Smithsonite (ZnCO₃) is an important zinc oxide mineral whose flotation separation from gangue minerals occurs in aqueous environments. The natural crystal lattice often contains Zn‑vacancy defects and metallic impurities (e.g., Fe, Mn, Cd, Co), which alter the surface structure and electronic properties. These changes can significantly influence the pre‑adsorption of water molecules, which is a critical step governing subsequent reagent attachment and flotation efficiency. Understanding how H₂O adsorbs on perfect, defective, and impurity‑bearing smithsonite (101) surfaces is therefore essential for designing better mineral processing strategies. This task uses density functional theory with dispersion correction (DFT‑D) and molecular dynamics (MD) simulations to quantify the differences in H₂O adsorption behaviour among these surface types, focusing on the most common (101) cleavage plane.

## Approach
The investigation combines two complementary computational approaches. First, spin‑polarised DFT‑D calculations are performed using a GGA functional with a plane‑wave/pseudopotential method and the TS dispersion correction. The bulk smithsonite crystal is optimised, then a (2×2×1) slab of the (101) surface with five atomic layers and a vacuum gap is cleaved and relaxed. From this, perfect, Zn‑vacancy (VT type), and Fe‑impurity (TFe type) surface models are constructed and relaxed. A single H₂O molecule is placed near the available adsorption sites (e.g., top‑Zn, bottom‑Zn for perfect; vacancy site for VT; impurity site for TFe) and the geometry is fully relaxed. The adsorption energy is computed as E_ad = E(slab+H₂O) − E(slab) − E(H₂O), and the adsorption form (dissociative or molecular) is determined by whether an O–H bond of the adsorbate breaks. Second, a 13‑molecule spherical water cluster is pre‑optimised with DFT and then simulated on the same three surfaces using NVT molecular dynamics at 298 K under the universal force field (UFF). From the resulting trajectories, the average adsorption energy and average cohesive energy per water molecule are calculated. The results from the perfect, Zn‑vacancy, and Fe‑impurity surfaces are compared to reveal how the presence of defects and impurities alters the interaction strength and the nature of the adsorbed state.

## Reproduction target
1. For each of the three surface types — perfect, Zn‑vacancy (VT), and Fe‑impurity (TFe) smithsonite (101) — perform DFT‑D geometry relaxation of a single H₂O adsorbate and compute the adsorption energy (in eV) and the adsorption form (dissociative or molecular). Report one row per adsorption site (which may be multiple sites per surface).
2. Run MD simulations of a water cluster on the same three surfaces and extract the average adsorption energy (kcal/mol) and average cohesive energy (kcal/mol) per water molecule. Report one row per surface type.
The required outputs are two CSV files placed under /app/outputs, as detailed in the workflow steps. The results will be verified by an automated checker that compares both the ordering of values among surfaces and their numerical magnitudes.

## Assets

- Smithsonite crystal structure (ZnCO₃): 0005122
- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- LAMMPS molecular dynamics package: https://www.lammps.org/

## Workflow steps

### Step 1: Bulk smithsonite DFT optimization
- Role: process
- Action: Starting from the experimental lattice parameters (a=b=4.6528 Å, c=15.025 Å, α=β=90°, γ=120°), perform density functional theory (DFT) optimization of the bulk smithsonite crystal structure using a GGA functional with dispersion correction.
- Evidence: none

### Step 2: Perfect (101) surface slab construction and relaxation
- Role: process
- Action: Cleave the optimized bulk crystal to expose the (101) surface, create a (2×2×1) slab with five atomic layers and a vacuum layer, then relax the slab allowing the top two layers to move while fixing the bottom three.
- Evidence: none

### Step 3: Defective and impurity surface construction and relaxation
- Role: process
- Action: Construct Zn‑vacancy (VT) and Fe‑impurity (TFe) smithsonite (101) surface slabs from the relaxed perfect slab, then relax each using the same DFT settings.
- Evidence: none

### Step 4: Bare surface electronic analysis (PDOS, electron density)
- Role: process
- Action: Compute partial density of states (PDOS) and electron density for the relaxed perfect, VT, and TFe surfaces.
- Evidence: `/app/outputs/bare_surface_pdos.json`

### Step 5: Isolated H₂O molecule optimization
- Role: process
- Action: Optimize an isolated H₂O molecule in a periodic box at the same DFT level.
- Evidence: none

### Step 6: DFT H₂O adsorption calculations
- Role: process
- Action: Perform geometry relaxation of H₂O adsorption complexes on perfect (TZn, BZn sites), VT‑vacancy, and TFe‑impurity surfaces using the relaxed slabs and optimized H₂O.
- Evidence: none

### Step 7: Analysis of DFT adsorption energies and forms (scored)
- Role: scored (load-bearing)
- Action: Compute the adsorption energy for each site as E_ad = E(slab+H₂O) – E(slab) – E(H₂O). Determine the adsorption form (dissociative if O–H bond is broken, molecular otherwise) from the final geometry. Write the results to a CSV file.
- Output file: `/app/outputs/step_05_dft_adsorption_results.csv`
- Format: csv
- Contract: surface_name (string, e.g. 'perfect', 'VT_defect', 'TFe_impurity'), site (string, e.g. 'TZn', 'BZn', 'VT', 'TFe'), adsorption_energy_eV (float, unit: eV), adsorption_form (string, one of 'dissociative' or 'molecular')
- Scoring: scored by hidden verifier

### Step 8: Post‑adsorption electronic analysis (PDOS, electron density difference, Mulliken populations)
- Role: process
- Action: Compute PDOS of bonding atoms, electron density difference maps, and Mulliken bond populations for the optimized adsorption complexes.
- Evidence: `/app/outputs/post_adsorption_analysis.json`

### Step 9: DFT pre‑optimization of spherical water cluster
- Role: process
- Action: Pre‑optimize a 13‑molecule spherical water cluster using DFT in a periodic box to obtain atomic charges for subsequent MD force‑field calculations.
- Evidence: none

### Step 10: MD simulation of water cluster on surfaces
- Role: process
- Action: Run NVT molecular dynamics at 298 K for 500 ps using the universal force field (UFF) to simulate a water cluster on perfect, VT‑vacancy, and TFe‑impurity surfaces.
- Evidence: none

### Step 11: Analysis of MD adsorption and cohesive energies (scored)
- Role: scored (load-bearing)
- Action: From MD trajectories, compute the average adsorption energy and average cohesive energy per water molecule for each surface. Write the results to a CSV file.
- Output file: `/app/outputs/step_09_md_results.csv`
- Format: csv
- Contract: surface_name (string), md_adsorption_energy_kcal_per_mol (float, unit: kcal/mol), md_cohesive_energy_kcal_per_mol (float, unit: kcal/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_05_dft_adsorption_results.csv`
- `/app/outputs/step_09_md_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_05_dft_adsorption_results.csv
- path: `/app/outputs/step_05_dft_adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: DFT adsorption energies and adsorption forms for each surface site. The perfect surface is expected to have the most negative energy and dissociative form; defect/impurity surfaces are expected to have less negative energies and molecular/mixed forms.
- schema:
  - `type`: table
  - `required_columns`: `surface_name`, `site`, `adsorption_energy_eV`, `adsorption_form`
  - `units`:
    - `adsorption_energy_eV`: eV

### step_09_md_results.csv
- path: `/app/outputs/step_09_md_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: MD average adsorption and cohesive energies of a water cluster on each surface. The perfect surface is expected to show the most wetting behavior (most negative adsorption energy, more positive cohesive energy) compared to defective/impurity surfaces.
- schema:
  - `type`: table
  - `required_columns`: `surface_name`, `md_adsorption_energy_kcal_per_mol`, `md_cohesive_energy_kcal_per_mol`
  - `units`:
    - `md_adsorption_energy_kcal_per_mol`: kcal/mol
    - `md_cohesive_energy_kcal_per_mol`: kcal/mol

Notes: The checked quantities are the DFT and MD adsorption/cohesive energies and the adsorption form classification. The scorings use hidden paper-reported reference values with tolerances and trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_05_dft_adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface_name",
          "site",
          "adsorption_energy_eV",
          "adsorption_form"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "DFT adsorption energies and adsorption forms for each surface site. The perfect surface is expected to have the most negative energy and dissociative form; defect/impurity surfaces are expected to have less negative energies and molecular/mixed forms."
    },
    {
      "file": "step_09_md_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface_name",
          "md_adsorption_energy_kcal_per_mol",
          "md_cohesive_energy_kcal_per_mol"
        ],
        "units": {
          "md_adsorption_energy_kcal_per_mol": "kcal/mol",
          "md_cohesive_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "MD average adsorption and cohesive energies of a water cluster on each surface. The perfect surface is expected to show the most wetting behavior (most negative adsorption energy, more positive cohesive energy) compared to defective/impurity surfaces."
    }
  ],
  "notes": "The checked quantities are the DFT and MD adsorption/cohesive energies and the adsorption form classification. The scorings use hidden paper-reported reference values with tolerances and trend checks."
}
```

## How you are scored
An automated verifier reads your two CSV artifacts and assigns a weighted reward for each scored stage. The verifier checks:

- **DFT adsorption stage:** Whether the adsorption energy ordering across the perfect, vacancy, and impurity surfaces follows the expected physical trend (i.e., which surface binds the water most strongly). Each reported adsorption form is checked against the correct dissociative/molecular classification for that site. Numerical adsorption energies are compared to a hidden reference within a tolerance.
- **MD cluster stage:** Whether the average adsorption energy and average cohesive energy across the three surface types exhibit the correct relative ordering; values are checked against a hidden reference within a tolerance.

The final reward (0–1) is a weighted combination of the scores from all scored steps. Reproducing the correct qualitative trends and classifying adsorption forms correctly is equally important as obtaining precise energy values. Simply reporting numbers without conducting the full DFT and MD workflow will not suffice.
