# Ni orbital occupations in La8Ni4O17 from extended Hückel tight-binding

## Problem background
La8Ni4O17 is a mixed-valent nickel oxide with a complex triclinic crystal structure containing six inequivalent nickel sites and ordered interstitial oxygen atoms. The material exhibits semiconducting behaviour and unusual magnetic properties that depend on temperature, attributed to the splitting of the Ni 3d-derived antibonding sigma* bands into very narrow, site-localized sub-bands. The electronic configurations of the nickel ions – specifically the occupancies of their 3d_{z^2} and 3d_{x^2−y^2} orbitals – are central to understanding the oxidation states and the role of interstitial oxygen. Computing these occupations from a monoelectronic band structure, under two different assumptions about the charge state of the interstitial oxygen, reveals how the band topology correlates with the structural distortions and experimental observables.

## Approach
The electronic structure is computed with the extended Hückel tight-binding (EHTB) method, which uses a basis of Slater-type atomic orbitals on all atoms. The full triclinic unit cells of La8Ni4O17 at 9 K and 300 K serve as input geometry. From the resulting band structure one obtains the total and projected density of states (DOS), in particular the partial DOS onto the Ni 3d_{z^2} and 3d_{x^2−y^2} orbitals for each of the six crystallographically distinct nickel sites. Under the rigid-band approximation, the Fermi level is placed such that the integrated DOS yields the total electron count appropriate to the oxygen charge hypothesis being considered. Two scenarios are examined: (i) the interstitial oxygen atoms form (O3)^{5−} entities, and (ii) all oxygen atoms are O^{2−}. For each scenario and each temperature, the integrated partial DOS up to the determined Fermi level gives the per-site occupations of the two relevant d-orbitals.

## Reproduction target
Produce two scored CSV files as detailed in the Workflow steps and Output contract: one for the (O3)^{5−} hypothesis (`occupations_O3_5.csv`) and one for the O^{2−} hypothesis (`occupations_O2.csv`). Each file must contain exactly 12 rows covering all six nickel sites at both 9 K and 300 K, with columns giving the temperature label, the nickel site identifier, and the computed occupations of the 3d_{z^2} and 3d_{x^2−y^2} orbitals. The extraction must follow the approach described above, using the EHTB band structure and the rigid-band Fermi level for each scenario.

## Assets

- Crystal structures of La8Ni4O17 at 9 K and 300 K: 10.1016/0022-4596(93)90229-N
- Extended Hückel tight-binding implementation: https://pymatgen.org

## Workflow steps

### Step 1: Crystal structure acquisition
- Role: process
- Action: Obtain the triclinic crystal structures of La8Ni4O17 at 9 K and 300 K from the published literature (Demourgues et al., J. Solid State Chem. 106, 317 (1993)).
- Evidence: none

### Step 2: EHTB band structure and DOS calculation
- Role: process
- Action: Using the extended Hückel tight-binding method with the atomic orbital parameters from Table 2 of the paper, compute the band structure, total and projected density of states (DOS), and Mulliken atomic orbital populations for both 9 K and 300 K structures. The calculation should yield a converged band structure and projected DOS on Ni 3d orbitals, which are needed for Fermi-level placement.
- Evidence: `/app/outputs/ehtb_band_dos.npz`

### Step 3: Occupation under (O3)5- hypothesis
- Role: scored (load-bearing)
- Action: Determine the number of 3d electrons per formula unit for the (O3)5- interstitial oxygen scenario. Use the rigid-band approximation: integrate the projected DOS of the Ni 3d_z2 and 3d_x2-y2 orbitals up to the Fermi energy that yields that electron count for each temperature. Extract the per-site occupations for all six Ni sites. Write the results to occupations_O3_5.csv.
- Output file: `/app/outputs/occupations_O3_5.csv`
- Format: csv
- Contract: Columns: temperature (string), Ni_site (string), d_z2_occupation (float), d_x2_y2_occupation (float). Exactly 12 rows (6 Ni sites × 2 temperatures).
- Scoring: scored by hidden verifier

### Step 4: Occupation under O2- hypothesis
- Role: scored
- Action: Repeat the Fermi-level placement and occupation extraction assuming all oxygen ions are O2-. Write the results to occupations_O2.csv.
- Output file: `/app/outputs/occupations_O2.csv`
- Format: csv
- Contract: Same format as occupations_O3_5.csv.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupations_O3_5.csv`
- `/app/outputs/occupations_O2.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupations_O3_5.csv
- path: `/app/outputs/occupations_O3_5.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Occupations of Ni 3d_z2 and 3d_x2-y2 orbitals for each Ni site at 9 K and 300 K under the (O3)5- interstitial oxygen hypothesis.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `Ni_site`, `d_z2_occupation`, `d_x2_y2_occupation`
  - `units`:
    - `temperature`: string (9 K or 300 K)
    - `Ni_site`: string (e.g., Ni(1))
    - `d_z2_occupation`: float (electrons)
    - `d_x2_y2_occupation`: float (electrons)

### occupations_O2.csv
- path: `/app/outputs/occupations_O2.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Occupations of Ni 3d_z2 and 3d_x2-y2 orbitals for each Ni site at 9 K and 300 K under the O2- interstitial oxygen hypothesis.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `Ni_site`, `d_z2_occupation`, `d_x2_y2_occupation`
  - `units`:
    - `temperature`: string (9 K or 300 K)
    - `Ni_site`: string
    - `d_z2_occupation`: float (electrons)
    - `d_x2_y2_occupation`: float (electrons)

Notes: The two tables are scored independently. Each must contain exactly 12 rows. Occupation values are compared to paper-reported references with a small absolute tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupations_O3_5.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "Ni_site",
          "d_z2_occupation",
          "d_x2_y2_occupation"
        ],
        "units": {
          "temperature": "string (9 K or 300 K)",
          "Ni_site": "string (e.g., Ni(1))",
          "d_z2_occupation": "float (electrons)",
          "d_x2_y2_occupation": "float (electrons)"
        }
      },
      "description": "Occupations of Ni 3d_z2 and 3d_x2-y2 orbitals for each Ni site at 9 K and 300 K under the (O3)5- interstitial oxygen hypothesis."
    },
    {
      "file": "occupations_O2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "Ni_site",
          "d_z2_occupation",
          "d_x2_y2_occupation"
        ],
        "units": {
          "temperature": "string (9 K or 300 K)",
          "Ni_site": "string",
          "d_z2_occupation": "float (electrons)",
          "d_x2_y2_occupation": "float (electrons)"
        }
      },
      "description": "Occupations of Ni 3d_z2 and 3d_x2-y2 orbitals for each Ni site at 9 K and 300 K under the O2- interstitial oxygen hypothesis."
    }
  ],
  "notes": "The two tables are scored independently. Each must contain exactly 12 rows. Occupation values are compared to paper-reported references with a small absolute tolerance."
}
```

## How you are scored
A hidden verifier independently examines both output CSV files. It checks that each file has the required structure (correct column names and row count) and then compares every occupation entry against a reference. The two files carry equal weight, and the overall reward is determined by how accurately your computed occupations match the reference across all entries, with no reward for merely supplying a correctly formatted file.
