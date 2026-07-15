# DFT Adsorption Energies for NH3 and NO on a Mo-Exchanged Zeolite Cluster

## Problem background
Selective catalytic reduction of NOx by NH3 is a key pollution-control technology. Mo-loaded ZSM-5 zeolites show high activity, and understanding the initial adsorption step—how NH3 and NO interact with the catalyst's acid sites—is essential for mechanistic insights. This task reproduces a DFT cluster study that quantifies the adsorption energies of NH3 and NO on both Lewis and Brønsted acid sites of the (MoO2)2+/HZSM-5 catalyst, providing the energetic foundation for the subsequent reaction steps.

## Approach
The catalyst is modelled as a (MoO2)2+ moiety grafted onto a 20T ZSM-5 cluster with double Si/Al substitution at T3 and T12 sites, taken from the public orthorhombic ZSM-5 crystal structure. Density functional theory (DFT) with the local density approximation (LDA) and the Perdew–Wang (PWC) exchange‑correlation functional is used to optimize geometries and obtain total energies. Adsorption energies are computed as E_ads = E_complex – E_cluster – E_adsorbate, where E_cluster is the bare cluster energy and E_adsorbate is the energy of the free NH3 or NO molecule. The workflow evaluates NH3 adsorption on the Lewis acid site (N‑down on Mo, three orientations), NH3 on a Brønsted acid site (protonated cluster, leading to NH4+), and NO adsorption N‑down on Mo, terminal oxygen, and the Brønsted hydrogen. The computed E_ads values quantify the relative binding strength and reveal whether NH3 or NO adsorbs preferentially.

## Reproduction target
Run the full DFT workflow and write the resulting adsorption energies (eV) for the seven specific configurations into /app/outputs/adsorption_energies.csv. The file must contain one row for each configuration: N1‑NH3, N2‑NH3, N3‑NH3, B‑NH3, Mo‑NO, O‑NO, H‑NO.

## Assets

- ZSM-5 orthorhombic crystal structure: https://www.iza-structure.org/databases/
- Open-source DFT code (CP2K or Quantum ESPRESSO): https://www.cp2k.org/
- Pseudopotentials / basis sets for LDA calculations

## Workflow steps

### Step 1: Build 20T ZSM-5 cluster model with (MoO2)2+
- Role: process
- Action: Construct a 20T cluster of the ZSM-5 framework from the public crystal structure. Perform double Si/Al substitution at T3 and T12 sites, graft the (MoO2)2+ moiety onto the framework oxygen atoms, and saturate all dangling bonds with hydrogen atoms as described in the paper.
- Evidence: `/app/outputs/cluster_model.xyz`

### Step 2: Optimize bare (MoO2)2+/HZSM-5 cluster
- Role: process
- Action: Perform DFT geometry optimization of the bare cluster model using the LDA/PWC exchange-correlation functional and a suitable basis set. Outer framework layers are fixed to retain the zeolite topology. Save the optimized coordinates and total energy.
- Evidence: `/app/outputs/bare_cluster.xyz`

### Step 3: Optimize isolated NH3 and NO molecules
- Role: process
- Action: Optimize free gas-phase NH3 and NO molecules using the same DFT protocol to obtain reference total energies for each molecule.
- Evidence: `/app/outputs/free_molecules.xyz`

### Step 4: NH3 adsorption on Lewis acid site
- Role: process
- Action: Create initial geometries for NH3 adsorbed on the Mo Lewis site in N1-down, N2-down, N3-down, and H-down configurations. Optimize each complex with DFT and record the total energies.
- Evidence: `/app/outputs/nh3_lewis_geometries.xyz`

### Step 5: Generate and optimize Brønsted acid site model
- Role: process
- Action: Add a proton to terminal oxygen OI of the bare cluster to form a Brønsted acid site (B-model) and optimize its geometry.
- Evidence: `/app/outputs/bronsted_model.xyz`

### Step 6: NH3 adsorption on Brønsted acid site
- Role: process
- Action: Place NH3 near the Brønsted proton of the B-model to form NH4+, optimize the complex with DFT, and record its total energy.
- Evidence: `/app/outputs/nh3_bronsted.xyz`

### Step 7: NO adsorption on (MoO2)2+/HZSM-5
- Role: process
- Action: Set up NO N-down adsorption on the Mo atom, on terminal oxygen OI, and on the Brønsted hydrogen. Optimize each complex with DFT and record total energies.
- Evidence: `/app/outputs/no_adsorption_geometries.xyz`

### Step 8: Compute and output adsorption energies
- Role: scored (load-bearing)
- Action: Using the total energies from the optimized bare cluster, free molecules, and each adsorption complex, compute E_ads = E_complex - E_cluster - E_molecule for the seven configurations (N1-NH3, N2-NH3, N3-NH3, B-NH3, Mo-NO, O-NO, H-NO). Write the results to /app/outputs/adsorption_energies.csv.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: configuration (str), E_ads (float, eV). Seven rows for N1-NH3, N2-NH3, N3-NH3, B-NH3, Mo-NO, O-NO, H-NO.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed DFT adsorption energies (eV) for NH3 and NO on the (MoO2)2+/HZSM-5 cluster. The checker compares each value to the hidden paper-reported values within a tolerance and verifies that all NH3 energies are more negative than all NO energies.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `E_ads`
  - `units`:
    - `E_ads`: eV

Notes: Only the LDA/PWC adsorption energies are scored. Extra columns or rows beyond the seven configurations are ignored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "E_ads"
        ],
        "units": {
          "E_ads": "eV"
        }
      },
      "description": "Computed DFT adsorption energies (eV) for NH3 and NO on the (MoO2)2+/HZSM-5 cluster. The checker compares each value to the hidden paper-reported values within a tolerance and verifies that all NH3 energies are more negative than all NO energies."
    }
  ],
  "notes": "Only the LDA/PWC adsorption energies are scored. Extra columns or rows beyond the seven configurations are ignored."
}
```

## How you are scored
A hidden verifier reads your adsorption_energies.csv and compares each reported E_ads to a reference obtained from a faithful re‑run of the same protocol. The comparison uses tolerances that account for different DFT implementations. In addition, the verifier checks that all NH3 adsorption energies are more negative (stronger binding) than all NO adsorption energies. The final reward combines accuracy of the individual energies and satisfaction of the overall trend. Qualitative electronic‑structure analyses are not scored.
