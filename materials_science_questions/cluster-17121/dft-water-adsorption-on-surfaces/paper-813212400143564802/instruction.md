# DFT Energetics of Water Adsorption in Sulfonate Hydrate Clusters

## Problem background
Hydrate clusters of 1,3‑benzenedisulfonic acid (1,3‑BDSA) exhibit proton conductivity highly dependent on water content. Understanding which stoichiometry (number of water molecules per SO3H group) is energetically most favorable for cluster formation and quantifying the energetics of water and acid adsorption provides a basis for explaining proton‑conduction behavior.

## Approach
Use density functional theory (DFT) at the B3LYP/6‑31G** level to compute the total electronic energy of a series of hydrate clusters of 1,3‑BDSA with different water contents, plus isolated H2O and isolated 1,3‑BDSA. From these total energies, calculate the specific formation energy (eV per acid molecule) for each cluster and the reaction energies (ΔE, in eV) for five processes: adding missing stoichiometric water (healing), adding an extra (superstoichiometric) water molecule, and adding an acid molecule. Compare the specific energies as a function of the water‑to‑SO3 group ratio, and examine the relative magnitudes of the three types of adsorption energies.

## Reproduction target
Compute the specific energies (eV per acid molecule) for clusters 3–9 defined in the workflow and the reaction energies ΔE for the five adsorption processes. Verify that, among clusters with no more than one stoichiometric water per SO3 group, those with exactly one water per SO3 group have the highest specific energy, and that the healing energy (adding missing stoichiometric water) is larger than the energy for adding a superstoichiometric water molecule. Also verify that the energy for adding an acid molecule is comparable in magnitude to the energy for water adsorption.

## Assets

- ORCA quantum chemistry package (or equivalent open-source DFT code): https://orcaforum.kofo.mpg.de/
- 6-31G** basis set

## Workflow steps

### Step 1: Build initial geometries for clusters and reference molecules
- Role: process
- Action: Construct starting atomic coordinates for the seven hydrate clusters of 1,3-benzenedisulfonic acid with stoichiometries: (1,3-BDSA·2H₂O)₃; (1,3-BDSA·2H₂O)₄ − 2H₂O; (1,3-BDSA·2H₂O)₄ (isomer); (1,3-BDSA·2H₂O)₄ (stoichiometric); (1,3-BDSA·2H₂O)₄·H₂O; (1,3-BDSA·2H₂O)₅ − 3H₂O; (1,3-BDSA·2H₂O)₅ − 2H₂O. Also build isolated H₂O and isolated 1,3-BDSA.
- Evidence: none

### Step 2: DFT geometry optimization and total energy calculation
- Role: process
- Action: For each of the nine systems (seven clusters + H₂O + 1,3-BDSA), perform a full geometry optimization followed by a single-point energy calculation using the B3LYP functional with the 6-31G** basis set (or an equivalent open-source DFT method). Save the final total electronic energy (in eV) of each system to `total_energies.csv` with columns: id (str: '3','4','5','6','7','8','9','H2O','1,3-BDSA') and total_energy (float, eV).
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Compute specific energies Es
- Role: scored (load-bearing)
- Action: Using the total energies from `total_energies.csv`, compute the specific energy Es (eV per acid molecule) for each cluster. For a cluster containing n acid molecules, Es = -total_energy / n (the formation energy per acid molecule, reported as a positive number). The number of acid molecules is: cluster 3 – n=3, 4– n=4, 5– n=4, 6– n=4, 7– n=4, 8– n=5, 9– n=5. Also calculate the water-to-SO₃ group ratio L = (number of water molecules) / (number of SO₃⁻ groups), where each acid has two SO₃H groups. Output `specific_energies.csv` with columns: cluster_id (int), L (float), E_s (float, eV).
- Output file: `/app/outputs/specific_energies.csv`
- Format: csv
- Contract: cluster_id (int), L (float, water per SO3- group), E_s (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Compute reaction energies ΔE
- Role: scored (load-bearing)
- Action: From the total energies of the clusters and isolated molecules, calculate the reaction energies ΔE (eV) for the five adsorption processes: (1) cluster 4 + 2 H₂O → cluster 6, (2) cluster 6 + H₂O → cluster 7, (3) cluster 8 + H₂O → cluster 9, (4) cluster 3 + 1,3-BDSA → cluster 4, (5) cluster 6 + 1,3-BDSA → cluster 9. For each reaction, ΔE = total energy of products – total energy of reactants. Output `reaction_energies.csv` with columns: reaction_id (int), reaction_description (str), delta_E (float, eV).
- Output file: `/app/outputs/reaction_energies.csv`
- Format: csv
- Contract: reaction_id (int), reaction_description (str), delta_E (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/specific_energies.csv`
- `/app/outputs/reaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### specific_energies.csv
- path: `/app/outputs/specific_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Specific formation energy per acid molecule for each cluster, derived from total energies.
- schema:
  - `type`: table
  - `required_columns`: `cluster_id`, `L`, `E_s`
  - `units`:
    - `E_s`: eV

### reaction_energies.csv
- path: `/app/outputs/reaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reaction energies (ΔE) for water and acid adsorption processes on the hydrate clusters.
- schema:
  - `type`: table
  - `required_columns`: `reaction_id`, `reaction_description`, `delta_E`
  - `units`:
    - `delta_E`: eV

Notes: The intermediate file total_energies.csv is not scored but is required for internal consistency checks by the verifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "specific_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster_id",
          "L",
          "E_s"
        ],
        "units": {
          "E_s": "eV"
        }
      },
      "description": "Specific formation energy per acid molecule for each cluster, derived from total energies."
    },
    {
      "file": "reaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_id",
          "reaction_description",
          "delta_E"
        ],
        "units": {
          "delta_E": "eV"
        }
      },
      "description": "Reaction energies (ΔE) for water and acid adsorption processes on the hydrate clusters."
    }
  ],
  "notes": "The intermediate file total_energies.csv is not scored but is required for internal consistency checks by the verifier."
}
```

## How you are scored
A hidden verifier independently evaluates your outputs. It loads `specific_energies.csv` and `reaction_energies.csv`, checks that your computed specific and reaction energies are internally consistent (derivable from the total energies you obtained), and compares your values to hidden reference values with appropriate tolerances. It also verifies that the required trends (highest specific energy at L=1, healing energy > superstoichiometric adsorption, comparable acid and water adsorption energies) are satisfied. The verifier combines these checks into a single reward score in the range [0,1]. Reporting the paper's numbers without performing the DFT calculations will not meet these requirements.
