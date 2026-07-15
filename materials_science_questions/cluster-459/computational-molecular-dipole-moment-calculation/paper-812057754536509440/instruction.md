# Ab Initio Proton Affinity of Methionine, Methionine Sulfoxide, and Methionine Sulfone

## Problem background
Proton affinity (PA) is a key thermodynamic quantity describing the basicity of molecules in the gas phase. Understanding which protonation site is most favorable for methionine and its oxidized derivatives (sulfoxide, sulfone) is important for studies of proton transfer in biological systems. This task requires performing ab initio Hartree–Fock calculations to determine the proton affinities for each possible protonation site in these three compounds and to identify the most stable protonation site for each molecule.

## Approach
The approach uses unrestricted Hartree–Fock (UHF) calculations with the 6-31G* basis set. For each of the three molecules (methionine, methionine sulfoxide, methionine sulfone), we first perform full geometry optimisation of the neutral molecule to obtain its total energy and dipole moment. We then construct models of the corresponding protonated forms, adding a proton at each plausible site: for methionine the amino nitrogen, the carboxyl oxygen, and the sulfur atom; for methionine sulfoxide the amino nitrogen, the carboxyl oxygen, and the oxygen of the SO group; for methionine sulfone the amino nitrogen, the carboxyl oxygen, and one oxygen of the SO₂ group. Every protonated form is also geometry-optimised at the same level of theory. Proton affinities are computed as the difference between the total electronic energy of the neutral molecule and the total electronic energy of each protonated form, converted to kcal/mol. The most favourable protonation site for a compound is the one with the highest proton affinity. The final results are the proton affinity values for all considered sites and the dipole moments of the neutral molecules.

## Reproduction target
Compute the proton affinities (in kcal/mol) for all considered protonation sites of methionine (N of amino group, O of carboxyl group, S), methionine sulfoxide (N of amino group, O of carboxyl group, O of SO group), and methionine sulfone (N of amino group, O of carboxyl group, O of SO₂ group), and the dipole moments (in Debye) of the neutral molecules. From the computed proton affinities, determine the most favourable protonation site for each compound.

## Assets

- Psi4 open-source quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: Neutral molecule calculations
- Role: process
- Action: Perform unrestricted Hartree-Fock geometry optimization with the 6-31G* basis set for neutral methionine, methionine sulfoxide, and methionine sulfone. Record the total electronic energies and dipole moments of each optimized structure.
- Evidence: `/app/outputs/neutral_results.json`

### Step 2: Protonated species calculations
- Role: process
- Action: For each compound, perform unrestricted Hartree-Fock geometry optimization with the 6-31G* basis set for all relevant protonated forms: methionine protonated at amino nitrogen, carboxyl oxygen, and sulfur; methionine sulfoxide protonated at amino nitrogen, carboxyl oxygen, and the SO oxygen; methionine sulfone protonated at amino nitrogen, carboxyl oxygen, and one of the SO2 oxygens. Record the total electronic energy for each optimized cation.
- Evidence: `/app/outputs/protonated_energies.json`

### Step 3: Proton affinity computation
- Role: scored (load-bearing)
- Action: Compute proton affinities (PA) as the difference between the neutral total energy and the protonated total energy for each site, using the energies recorded in steps 1 and 2. Output the values in kcal/mol.
- Output file: `/app/outputs/proton_affinities.json`
- Format: json
- Contract: JSON object with top-level keys 'methionine', 'methionine_sulfoxide', 'methionine_sulfone'. Each maps to an object containing site-specific keys ('N', 'O', 'S' for methionine; 'N', 'O', 'SO' for sulfoxide; 'N', 'O', 'SO2' for sulfone) and the corresponding proton affinity (float, kcal/mol).
- Scoring: scored by hidden verifier

### Step 4: Most favorable site determination
- Role: scored
- Action: For each compound, identify the protonation site with the highest proton affinity from the values in proton_affinities.json. Output the site name (string) for each compound.
- Output file: `/app/outputs/most_favorable_sites.json`
- Format: json
- Contract: JSON object with keys 'methionine', 'methionine_sulfoxide', 'methionine_sulfone' mapping to a string: 'N', 'S', 'O', 'SO', or 'SO2'.
- Scoring: scored by hidden verifier

### Step 5: Dipole moment reporting
- Role: scored
- Action: Extract the dipole moments of the neutral molecules from the results of step 1 and output them in Debye.
- Output file: `/app/outputs/dipole_moments.json`
- Format: json
- Contract: JSON object with keys 'methionine', 'methionine_sulfoxide', 'methionine_sulfone' mapping to the dipole moment (float, Debye).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/proton_affinities.json`
- `/app/outputs/most_favorable_sites.json`
- `/app/outputs/dipole_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### proton_affinities.json
- path: `/app/outputs/proton_affinities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Proton affinities (kcal/mol) for all considered protonation sites of the three compounds. Compared against the paper's Table 4 values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `methionine`: object
    - `methionine_sulfoxide`: object
    - `methionine_sulfone`: object
  - `items`:
    - `methionine`:
      - `N`: float
      - `O`: float
      - `S`: float
    - `methionine_sulfoxide`:
      - `N`: float
      - `O`: float
      - `SO`: float
    - `methionine_sulfone`:
      - `N`: float
      - `O`: float
      - `SO2`: float
  - `units`:
    - `all_site_keys`: kcal/mol

### most_favorable_sites.json
- path: `/app/outputs/most_favorable_sites.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Most favorable protonation site for each compound (one of 'N', 'O', 'S', 'SO', 'SO2'). Exact string match against the paper's conclusion.
- schema:
  - `type`: object
  - `required`:
    - `methionine`: string
    - `methionine_sulfoxide`: string
    - `methionine_sulfone`: string
  - `items`:
    - `methionine`: string
    - `methionine_sulfoxide`: string
    - `methionine_sulfone`: string

### dipole_moments.json
- path: `/app/outputs/dipole_moments.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dipole moments of the neutral molecules in Debye. Compared against the paper's Table 1 values within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `methionine`: float
    - `methionine_sulfoxide`: float
    - `methionine_sulfone`: float
  - `units`:
    - `methionine`: Debye
    - `methionine_sulfoxide`: Debye
    - `methionine_sulfone`: Debye

Notes: All gold values and tolerances are hidden. The checker compares the agent's reported numbers against the paper's published values (Table 4 for PA, Table 1 for dipole moments). The most favorable sites are compared as exact strings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "proton_affinities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "methionine": "object",
          "methionine_sulfoxide": "object",
          "methionine_sulfone": "object"
        },
        "items": {
          "methionine": {
            "N": "float",
            "O": "float",
            "S": "float"
          },
          "methionine_sulfoxide": {
            "N": "float",
            "O": "float",
            "SO": "float"
          },
          "methionine_sulfone": {
            "N": "float",
            "O": "float",
            "SO2": "float"
          }
        },
        "units": {
          "all_site_keys": "kcal/mol"
        }
      },
      "description": "Proton affinities (kcal/mol) for all considered protonation sites of the three compounds. Compared against the paper's Table 4 values within a hidden tolerance."
    },
    {
      "file": "most_favorable_sites.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "methionine": "string",
          "methionine_sulfoxide": "string",
          "methionine_sulfone": "string"
        },
        "items": {
          "methionine": "string",
          "methionine_sulfoxide": "string",
          "methionine_sulfone": "string"
        }
      },
      "description": "Most favorable protonation site for each compound (one of 'N', 'O', 'S', 'SO', 'SO2'). Exact string match against the paper's conclusion."
    },
    {
      "file": "dipole_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "methionine": "float",
          "methionine_sulfoxide": "float",
          "methionine_sulfone": "float"
        },
        "units": {
          "methionine": "Debye",
          "methionine_sulfoxide": "Debye",
          "methionine_sulfone": "Debye"
        }
      },
      "description": "Dipole moments of the neutral molecules in Debye. Compared against the paper's Table 1 values within a hidden tolerance."
    }
  ],
  "notes": "All gold values and tolerances are hidden. The checker compares the agent's reported numbers against the paper's published values (Table 4 for PA, Table 1 for dipole moments). The most favorable sites are compared as exact strings."
}
```

## How you are scored
Each scored output (proton_affinities.json, dipole_moments.json, most_favorable_sites.json) is checked by a hidden verifier against the expected results. The verifier independently scores each artifact and combines the scores by weight into a final reward between 0 and 1. Reporting numbers that merely look plausible or match the paper is not sufficient; the verifier checks that the values originate from proper calculations following the prescribed quantum chemical procedure. Only artifacts produced through the UHF/6-31G* geometry optimisations described above will pass the hidden checks.
