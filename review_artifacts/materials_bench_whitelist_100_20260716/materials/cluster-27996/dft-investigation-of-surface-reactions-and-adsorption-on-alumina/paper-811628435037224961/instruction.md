# Free Radical Adsorption on Graphene Fragment: Physical vs Chemical Bonding via DFTB-D

## Problem background
This task investigates how free radicals (CH, CH₃, C₂H, C₂H₃, C₂H₅, and OH) interact with a hydrogen-terminated graphene fragment (C₅₄H₁₈). Depending on the radical orientation, the interaction may be physical adsorption (physisorption) or lead to the formation of a chemical bond (chemisorption). The goal is to compute the structural and energetic properties that distinguish these two regimes: adsorption energies, charge transfer, the distance between the radical and the graphene, and the deformation of the graphene layer. Understanding these differences is important for radical scavenging and for interpreting molecule–surface interactions in general.

## Approach
We employ a density functional tight-binding approach with an empirical dispersion correction (DFTB-D). The simulation proceeds as follows: First, a planar C₅₄H₁₈ graphene fragment is built. Then the six radical species are prepared. For each radical, multiple initial placements are generated above the graphene surface, varying the adsorption site (on-top, bridge, hollow) and the radical orientation. A total of 144 starting configurations are created. Isolated graphene and radical energies are computed as references. All complexes are geometry-optimized with DFTB-D, yielding relaxed structures and total energies. The 16 most favourable distinct minima are identified. For each, the adsorption energy is obtained as the difference between the complex energy and the sum of the isolated species energies. Mulliken population analysis provides the charge transfer. The distance from the nearest non-hydrogen atom of the radical to the graphene plane is measured, and for chemisorption cases the maximum out-of-plane displacement of a graphene carbon atom is recorded. Finally, each structure is classified as physical (PA) or chemical (CA) adsorption based on the computed distance thresholds given in the workflow steps.

## Reproduction target
You must build the graphene fragment and radical geometries, generate the 144 initial conformations, compute the reference energies, perform all geometry optimizations, select the 16 unique minima, and compute the quantities described in the workflow. Produce a single CSV file, `optimization_results.csv`, containing one row for each of the 16 final structures. The columns are: `system_type` (e.g., CH(III)), `adsorption_type` (PA or CA), `distance_angstrom`, `adsorption_energy_kcal_per_mol`, `charge_transfer_e`, and `displacement_angstrom` (leave empty for PA rows). This CSV will be compared against hidden reference values by the verifier. Your computed numbers should be accurate enough to match the expected results within reasonable tolerances that account for minor differences due to DFTB+ version, parameter set, or convergence settings.

## Assets

- DFTB+ code: https://github.com/dftbplus/dftbplus
- Slater-Koster parameter set for C, H, O (e.g., mio-1-1 or pbc-0-3): https://dftb.org/parameters

## Workflow steps

### Step 1: Build graphene fragment model
- Role: process
- Action: Construct the C54H18 graphene fragment: a planar hexagonal carbon sheet with 54 C atoms, each edge C saturated by one H atom (18 H atoms). Place the fragment strictly in the x-y plane and save the initial geometry.
- Evidence: `/app/outputs/graphene_fragment.xyz`

### Step 2: Prepare free radical geometries
- Role: process
- Action: Define the initial geometries of the six free radicals: CH, CH3, C2H, C2H3, C2H5, and OH. Create one XYZ file per radical, using reasonable gas-phase bond lengths and angles.
- Evidence: none

### Step 3: Generate initial FR-graphene conformations
- Role: process
- Action: For each of the six radicals, place it above the central area of the graphene surface in various orientations (different rotational angles and sites) to create 144 distinct initial adsorption geometries. Save each starting complex as a separate input file.
- Evidence: none

### Step 4: Compute isolated species energies
- Role: process
- Action: Perform DFTB-D single-point energy calculations (or brief geometry optimisations) for each isolated radical and for the C54H18 fragment alone. Save the total energies as reference values for later adsorption energy calculation.
- Evidence: `/app/outputs/isolated_energies.json`

### Step 5: Geometry optimizations of FR-graphene complexes
- Role: process
- Action: For each of the 144 initial complexes, run a DFTB-D geometry optimisation using DFTB+ (with an empirical dispersion term). Keep all optimised geometries and total energies.
- Evidence: none

### Step 6: Identify stable minima
- Role: process
- Action: From the optimised structures, select the 16 most favourable unique minima (based on adsorption energy and geometric characteristics) corresponding to the types listed in the paper (e.g., CH(I)-(IV), CH3(I)-(III), etc.). These 16 structures constitute the final analysed set.
- Evidence: `/app/outputs/selected_structures.txt`

### Step 7: Calculate adsorption properties and classify PA/CA
- Role: scored (load-bearing)
- Action: For each of the 16 selected optimised complexes, compute: (i) adsorption energy ΔE = E(complex) - E(graphene) - E(radical) [kcal/mol]; (ii) Mulliken charge transfer (e); (iii) distance from the nearest nonhydrogen atom (C or O) of the radical to the graphene (Å); (iv) maximum graphene atomic displacement in the z-direction for those structures where the distance qualifies as chemical adsorption (CA). Classify each complex as PA or CA based on the computed distance: PA if distance is in the range 2.35–3.44 Å, CA if in 0.95–1.59 Å. The 16 structures correspond to the following system types: CH(I), CH(II), CH(III), CH(IV), CH3(I), CH3(II), CH3(III), C2H, C2H3(I), C2H3(II), C2H5(I), C2H5(II), C2H5(III), OH(I), OH(II), OH(III). Save the results as `optimization_results.csv`.
- Output file: `/app/outputs/optimization_results.csv`
- Format: csv
- Contract: CSV with columns: system_type (string, e.g. 'CH(III)'), adsorption_type ('PA' or 'CA'), distance_angstrom (float), adsorption_energy_kcal_per_mol (float), charge_transfer_e (float), displacement_angstrom (float, empty for PA rows). One row per structure (16 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimization_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimization_results.csv
- path: `/app/outputs/optimization_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Properties of the 16 optimized FR-graphene structures: system type, adsorption class, distance, adsorption energy, charge transfer, and graphene atomic displacement.
- schema:
  - `type`: table
  - `required_columns`: `system_type`, `adsorption_type`, `distance_angstrom`, `adsorption_energy_kcal_per_mol`, `charge_transfer_e`, `displacement_angstrom`
  - `units`:
    - `distance_angstrom`: Å
    - `adsorption_energy_kcal_per_mol`: kcal/mol
    - `charge_transfer_e`: e
    - `displacement_angstrom`: Å

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimization_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system_type",
          "adsorption_type",
          "distance_angstrom",
          "adsorption_energy_kcal_per_mol",
          "charge_transfer_e",
          "displacement_angstrom"
        ],
        "units": {
          "distance_angstrom": "Å",
          "adsorption_energy_kcal_per_mol": "kcal/mol",
          "charge_transfer_e": "e",
          "displacement_angstrom": "Å"
        }
      },
      "description": "Properties of the 16 optimized FR-graphene structures: system type, adsorption class, distance, adsorption energy, charge transfer, and graphene atomic displacement."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by an automated checker that reads `optimization_results.csv`. The checker will extract the 16 rows and verify that the columns are present and of correct type. For each structure it compares your reported distance, adsorption energy, charge transfer, and displacement (where applicable) to a hidden set of expected values, using appropriate tolerances that allow for the inherent variability of computational reproduction. In addition, the checker performs a structural consistency check: distances for PA cases must fall within the physisorption range given in the workflow, CA distances must fall within the chemisorption range, and CA displacements must exceed the minimum threshold stated in the workflow. The final reward is a weighted sum: a majority of the weight comes from the numeric match on the property columns across all 16 rows. A perfect submission is one where all reported values are within tolerance and the structural ranges are satisfied. You do not need to produce any other output file.
