# Water Exchange Simulations on Fluoridated Keggin Clusters

## Problem background
The paper investigates the influence of fluorine substitution on the structure and water-exchange reactivity of Keggin aluminum tridecamers (K-Al₁₃) in aqueous solution. These polynuclear clusters serve as molecular models for mineral surfaces, and understanding how fluoride modifies the dissociative character and activation barriers of water exchange is relevant to geochemical aluminum cycling and mineral dissolution. The key open question is whether fluorine bridges change the water-exchange mechanism and how the activation energy varies with the number and type of fluorine bridges.

## Approach
The study uses density functional theory (DFT) to simulate water exchange on Keggin-Al₁₃ clusters. Three cluster variants are considered: a non-fluoridated reference (0F), one where a bridging hydroxyl is replaced by fluorine between trimer units (F_inter), and one with a fluorine bridge within a trimer unit (F_intra). Each cluster is solvated with 15 explicit water molecules plus an implicit PCM continuum solvent (water, ε=78.39). Geometries of the reactant and the water-exchange transition state are optimized at the B3LYP/6-31G(d) level. From these geometries, the total metal–ligand distance change ΔΣ_Al−L (the sum of bond distances to the six ligands at the exchanging Al site) is computed as a structural measure of dissociative character. Electronic activation energies are obtained via single-point MPWKCIS/6-31+G(d,p) calculations with the same PCM solvent on the optimized reactant and transition-state structures. The approach allows one to quantify the effect of distinct fluorine substitution patterns on the water-exchange mechanism and barrier.

## Reproduction target
For the three K-Al₁₃ clusters (0F, F_inter, F_intra), compute and report the ΔΣ_Al−L values and the activation energy barriers for the water-exchange reaction. Based on the computed values, determine whether the mechanism is dissociative (all ΔΣ_Al−L positive) and how the ΔΣ_Al−L values and barriers differ between the fluoridated clusters and the non-fluoridated cluster.

## Assets

- ORCA (or NWChem, PySCF): https://orcaforum.kofo.mpg.de/
- Keggin-Al13 cluster structure

## Workflow steps

### Step 1: Build and optimize reactant structures
- Role: process
- Action: Build initial molecular models of the three K-Al₁₃ clusters: non-fluoridated (0F), one inter-trimer fluorine bridge (F_inter), and one intra-trimer fluorine bridge (F_intra). Add 15 explicit water molecules per cluster to form the first solvation shell. Perform DFT geometry optimization at the B3LYP/6-31G(d) level with PCM implicit solvent (water, ε=78.39). Confirm that optimized geometries are minima (no imaginary frequencies).
- Evidence: `/app/outputs/optimized_reactants.xyz`

### Step 2: Locate water-exchange transition states
- Role: process
- Action: Using the optimized reactants from step 1, perform transition-state searches for the dissociative water-exchange pathway on each cluster (0F, F_inter, F_intra) at the B3LYP/6-31G(d) level with PCM implicit solvent. Verify each TS by a frequency calculation (exactly one imaginary frequency) and an intrinsic reaction coordinate (IRC) calculation confirming connectivity between reactant and product (five-coordinate intermediate).
- Evidence: `/app/outputs/transition_states.xyz`

### Step 3: Compute ΔΣ_Al-L values
- Role: scored (load-bearing)
- Action: From the optimized reactant and TS geometries of the three clusters (0F, F_inter, F_intra), compute the total metal–ligand distance Σ_Al–L (sum of bond distances between the target octahedral Al and its six ligands). For each cluster, compute ΔΣ_Al–L = Σ_Al–L(TS) − Σ_Al–L(reactant). Write a CSV file with columns: cluster, delta_sigma_Al_L (Å).
- Output file: `/app/outputs/delta_sigma_al_l.csv`
- Format: csv
- Contract: Columns: cluster (string), delta_sigma_Al_L (float, Å).
- Scoring: scored by hidden verifier

### Step 4: Compute activation energy barriers
- Role: scored
- Action: Perform single-point energy calculations at the MPWKCIS/6-31+G(d,p) level with PCM implicit solvent (water, ε=78.39) on the B3LYP/6-31G(d) optimized reactant and TS geometries of each cluster (0F, F_inter, F_intra). Compute the electronic activation energy ΔE‡ = E(TS) − E(reactant) in kJ/mol. Write a CSV file with columns: cluster, activation_energy_kJmol (kJ/mol).
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: Columns: cluster (string), activation_energy_kJmol (float, kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_sigma_al_l.csv`
- `/app/outputs/activation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_sigma_al_l.csv
- path: `/app/outputs/delta_sigma_al_l.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total metal-ligand distance change ΔΣ_Al-L for the reactant-to-TS water exchange. All values must be positive (dissociative mechanism) and the fluoridated clusters (F_inter, F_intra) must show larger ΔΣ_Al-L than the non-fluoridated cluster (0F).
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `delta_sigma_Al_L`
  - `units`:
    - `delta_sigma_Al_L`: Å

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic activation energy barriers for water exchange. The barriers for fluoridated clusters (F_inter, F_intra) must be greater than for the non-fluoridated cluster (0F).
- schema:
  - `type`: table
  - `required_columns`: `cluster`, `activation_energy_kJmol`
  - `units`:
    - `activation_energy_kJmol`: kJ/mol

Notes: The agent must construct the K-Al13 structures from public knowledge; no pre-built coordinates are provided. All DFT calculations should use an open-source code such as ORCA, NWChem, or PySCF.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_sigma_al_l.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "delta_sigma_Al_L"
        ],
        "units": {
          "delta_sigma_Al_L": "Å"
        }
      },
      "description": "Total metal-ligand distance change ΔΣ_Al-L for the reactant-to-TS water exchange. All values must be positive (dissociative mechanism) and the fluoridated clusters (F_inter, F_intra) must show larger ΔΣ_Al-L than the non-fluoridated cluster (0F)."
    },
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cluster",
          "activation_energy_kJmol"
        ],
        "units": {
          "activation_energy_kJmol": "kJ/mol"
        }
      },
      "description": "Electronic activation energy barriers for water exchange. The barriers for fluoridated clusters (F_inter, F_intra) must be greater than for the non-fluoridated cluster (0F)."
    }
  ],
  "notes": "The agent must construct the K-Al13 structures from public knowledge; no pre-built coordinates are provided. All DFT calculations should use an open-source code such as ORCA, NWChem, or PySCF."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the two CSV files you produce (delta_sigma_al_l.csv and activation_energies.csv). The verifier checks that all ΔΣ_Al−L values are positive, that the fluoridated clusters exhibit larger ΔΣ_Al−L and higher activation barriers than the non-fluoridated cluster, and compares each numerical value to the paper-reported reference within a tolerance that absorbs legitimate implementation differences due to choice of code, basis sets, or convergence. The final reward is a weighted combination of the scores for the two artifacts, with the main burden on the correct reproduction of the ΔΣ_Al−L trends and the activation energy ordering. Reporting the paper's target numbers without running the described calculations is not sufficient to obtain full credit.
