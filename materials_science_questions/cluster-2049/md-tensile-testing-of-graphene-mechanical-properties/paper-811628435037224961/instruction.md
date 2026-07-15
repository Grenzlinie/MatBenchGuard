# DFTB-D Study of Free Radical Adsorption on Graphene

## Problem background
Free radicals can interact with graphene surfaces in different ways: they may simply be attracted via weak forces (physical adsorption) or form chemical bonds (chemical adsorption). Understanding these interactions is important for applications such as radical scavenging and surface chemistry. This task examines six representative free radicals—CH, CH3, C2H, C2H3, C2H5, and OH—adsorbed on a hydrogen-terminated graphene fragment. Your goal is to compute, from first principles, the adsorption distances, adsorption energies, charge transfer, and the deformation of the graphene sheet for the stable adsorption structures. You will also determine whether each structure corresponds to physical or chemical adsorption based on the computed adsorption distance.

## Approach
You will employ the density functional tight-binding method with an empirical dispersion correction (DFTB-D), implemented in the open-source DFTB+ code. Use any publicly available Slater-Koster parameter set that includes C, H, and O. The substrate is a hydrogen-saturated graphene flake containing 54 carbon atoms and 18 edge-saturating hydrogens (C54H18), initially placed flat in the xy-plane. For each radical, generate several initial configurations above the central region of the flake, varying the lateral site (on-top, bridge, hollow) and orientation, including both hydrogen-side and nonhydrogen-side approaches. Perform geometry optimizations allowing full relaxation of the graphene lattice. From the optimized results, identify the distinct stable adsorption structures (the original study found 16 types). Then, for each stable structure: classify as physical adsorption (PA) if the distance from the nearest nonhydrogen atom of the radical to the graphene surface is greater than 2.0 Å, or as chemical adsorption (CA) if it is less than 2.0 Å; compute the adsorption energy as the difference between the total energy of the complex and the sum of the isolated radical and isolated graphene energies; extract the Mulliken charge transfer (net electron gain of the radical); and, for CA cases, calculate the mean z-displacement of the graphene atoms. Collect the results into a CSV file.

## Reproduction target
Produce a CSV file named adsorption_results.csv in /app/outputs/ containing one row for each distinct stable adsorption structure (target: 16 rows, covering the six radicals). Each row must include: the radical name (fr), a label for the adsorption type (type, e.g., I, II, III, or similar), the adsorption distance in Angstroms (distance_Angstrom), the adsorption energy in kcal/mol (adsorption_energy_kcal_mol), the net charge transfer in e (charge_transfer), and, for CA structures, the mean graphene z-displacement in Angstroms (displacement_Angstrom); leave the displacement field empty for PA structures. The classification into PA or CA must be consistent with the 2.0 Å threshold on the computed distance. The CSV must contain the numeric values obtained from your DFTB-D calculations; do not copy values from any external source.

## Assets

- DFTB+ software: https://dftbplus.org/
- DFTB Slater-Koster parameter set for C, H, O: https://dftb.org/parameters/

## Workflow steps

### Step 1: Construct graphene fragment and initial FR-graphene geometries
- Role: process
- Action: Build a C54H18 graphene fragment (54 C atoms, 18 edge-saturating H atoms) with the sheet initially in the xy-plane. Generate at least 144 initial structures by placing each of the six free radicals (CH, CH3, C2H, C2H3, C2H5, OH) above the central area at different lateral sites (on-top, bridge, hollow) and orientations, covering both hydrogen-side and nonhydrogen-side approaches.
- Evidence: `/app/outputs/initial_structures_count.txt`

### Step 2: DFTB-D geometry optimization of all initial conformations
- Role: process
- Action: For each initial structure, run a DFTB-D geometry optimization using DFTB+ with a chosen Slater-Koster parameter set (C, H, O) and dispersion correction, allowing the graphene lattice to relax. Save optimized geometries and total energies. From the resulting set, identify distinct stable adsorption structures (target 16 types as in the original study). Also compute total energies of the isolated free radicals and the isolated graphene fragment for adsorption energy calculation.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Classification and property extraction into scored table
- Role: scored (load-bearing)
- Action: For each distinct stable adsorption structure (16 types), classify as physical adsorption (PA) or chemical adsorption (CA) by comparing the distance from the nearest nonhydrogen atom (C or O) of the radical to the graphene surface (PA if >2.0 A, CA if <2.0 A). Compute adsorption energy = E_system - (E_isolated_FR + E_isolated_graphene). Extract Mulliken charge transfer (net electron gain of the radical), adsorption distance, and for CA cases the mean z-displacement of graphene atoms (leave empty for PA). Write a CSV file with one row per structure.
- Output file: `/app/outputs/adsorption_results.csv`
- Format: csv
- Contract: Columns: fr (string), type (string, e.g., PA/CA/I/II/III), distance_Angstrom (float), adsorption_energy_kcal_mol (float), charge_transfer (float), displacement_Angstrom (float, empty for PA rows)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.csv
- path: `/app/outputs/adsorption_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption properties for each stable FR-graphene structure, computed from DFTB-D optimizations. Rows represent the 16 distinct adsorption types found for the six radicals. Values are compared to reference results with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `fr`, `type`, `distance_Angstrom`, `adsorption_energy_kcal_mol`, `charge_transfer`, `displacement_Angstrom`
  - `units`:
    - `distance_Angstrom`: Angstrom
    - `adsorption_energy_kcal_mol`: kcal/mol
    - `charge_transfer`: e
    - `displacement_Angstrom`: Angstrom

Notes: Only the free-graphene optimizations and property extraction are included; fixed-graphene tests, potential energy surface scans, and electronic structure analysis are omitted as they are not required for the quantitative reproduction of the headline Table 1 properties.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "fr",
          "type",
          "distance_Angstrom",
          "adsorption_energy_kcal_mol",
          "charge_transfer",
          "displacement_Angstrom"
        ],
        "units": {
          "distance_Angstrom": "Angstrom",
          "adsorption_energy_kcal_mol": "kcal/mol",
          "charge_transfer": "e",
          "displacement_Angstrom": "Angstrom"
        }
      },
      "description": "Adsorption properties for each stable FR-graphene structure, computed from DFTB-D optimizations. Rows represent the 16 distinct adsorption types found for the six radicals. Values are compared to reference results with tolerances."
    }
  ],
  "notes": "Only the free-graphene optimizations and property extraction are included; fixed-graphene tests, potential energy surface scans, and electronic structure analysis are omitted as they are not required for the quantitative reproduction of the headline Table 1 properties."
}
```

## How you are scored
Your submission will be evaluated by an automated checker. The checker reads your adsorption_results.csv and compares each reported property (distance, energy, charge transfer, displacement) against reference values using appropriate tolerances. The classification (PA/CA) is verified by checking that the reported distance conforms to the 2.0 Å cut-off (PA > 2.0 Å, CA < 2.0 Å) and that displacements for CA structures are non-negligible. The reward is computed as a weighted sum of these comparisons over all rows and properties. The reference values are derived from the original study; therefore, simply reporting numbers without performing the required geometry optimizations will not match the expected results.
