# DFT Adsorption of Benzyl Mercaptan and Pd13 Cluster on 11 Functionalized Graphene Models

## Problem background
The interface between palladium nanoparticles and functionalized reduced graphene oxide is crucial for catalyst design. Understanding how the organic linker benzyl mercaptan (BnSH) adsorbs on various defective and functionalized graphene surfaces, and how it then anchors Pd clusters, is essential for optimizing these materials. This task uses density functional theory (DFT) to quantify the adsorption energies of BnSH and a 13-atom icosahedral palladium cluster (Pd13) on 11 different graphene models, along with the charge transfer between BnSH and the graphene.

## Approach
The computational method uses DFT with the SIESTA code and the local density approximation (LDA). Eleven graphene supercells are built, each containing 240 carbon atoms with one of 11 surface features: pristine graphene, a vacancy, substitutional nitrogen, a vacancy+pyridinic N, an amine group, a vacancy+amine, hydroxyl, a vacancy+hydroxyl, carboxyl, a vacancy+hydroxyl (Vc-OH), and an epoxy group. A BnSH molecule and an icosahedral Pd13 cluster are also constructed. All isolated systems are geometry-optimized to obtain reference energies. Then, for each graphene model, the BnSH molecule is placed on the surface, the combined system relaxed, and the adsorption energy ΔE_ads_BnSH = E_total − E_graphene − E_BnSH computed. Bader charge analysis yields the charge transfer. Finally, the Pd13 cluster is placed on the relaxed BnSH-graphene complex, relaxed together, and its adsorption energy computed as ΔE_ads_Pd13 = E_total − E_BnSH_GS − E_Pd13. The results are reported in a single CSV file.

## Reproduction target
Compute, for each of the 11 graphene models (numbered 1–10 for the defects listed above, then 11 for pristine), the adsorption energy of BnSH (in kJ/mol), the Bader charge transferred between BnSH and the graphene (in e), and the adsorption energy of the Pd13 cluster on the BnSH-graphene system (in kJ/mol). Output a CSV file named adsorption_energies.csv with columns: defect_label (string), E_ads_BnSH_kJmol (float), Bader_charge_e (float), E_ads_Pd13_kJmol (float). Rows must be in order of defect numbering: 1 through 10, then 11 (pristine).

## Assets

- SIESTA DFT code: https://departments.icmab.es/leem/siesta/
- Bader charge analysis tool: http://theory.cm.utexas.edu/henkelman/code/bader/
- Python 3: python3

## Workflow steps

### Step 1: Prepare substrate and molecule/cluster structures
- Role: process
- Action: Build atomic coordinates for the 11 functionalized graphene supercells (240 C atoms, ~2.5 nm × 2.5 nm) containing the defects: vacancy, substitutional N, Vc‑N (vacancy + pyridinic N), amine (R‑NH2), Vc‑NH2, hydroxyl (R‑OH), Vc2‑OH, carboxyl (R‑COOH), Vc‑OH, epoxy, plus pristine graphene. Also construct the benzyl mercaptan (C7H7SH) molecule and an icosahedral Pd13 cluster.
- Evidence: `/app/outputs/structures_created.txt`

### Step 2: Optimize isolated subsystems
- Role: process
- Action: Using SIESTA with the LDA functional, DZ/DZP basis (as appropriate), and 250 Ry real‑space cutoff, perform geometry relaxations on each of the 11 functionalized graphene supercells, the isolated BnSH molecule, and the isolated Pd13 cluster. Record the final total energy of each relaxed system.
- Evidence: `/app/outputs/isolated_energies.json`

### Step 3: Compute adsorption energies and Bader charges
- Role: scored (load-bearing)
- Action: For each of the 11 graphene models: (a) Place BnSH on the graphene, relax the combined system using SIESTA, compute the adsorption energy ΔE_ads_BnSH = E_total − E_graphene − E_BnSH; also perform Bader charge analysis to obtain the charge transfer Δq. (b) Using the relaxed BnSH‑graphene from (a), place the Pd13 cluster on top, relax the system, and compute ΔE_ads_Pd13 = E_total − E_BnSH_GS − E_Pd13. Collect all results and write them as a CSV file.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: defect_label (string), E_ads_BnSH_kJmol (float), Bader_charge_e (float), E_ads_Pd13_kJmol (float). Units: kJ/mol for energies, e for charge. 11 rows, ordered by defect numbering (1–10 then pristine).
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
- description: The computed adsorption energies and Bader charges for BnSH and Pd13 on the 11 graphene models. The hidden checker compares the reported values to reference values for the same physical systems.
- schema:
  - `type`: table
  - `required_columns`: `defect_label`, `E_ads_BnSH_kJmol`, `Bader_charge_e`, `E_ads_Pd13_kJmol`
  - `units`:
    - `E_ads_BnSH_kJmol`: kJ/mol
    - `Bader_charge_e`: e
    - `E_ads_Pd13_kJmol`: kJ/mol

Notes: The agent must produce this CSV after running all SIESTA calculations and Bader analysis. The file should contain exactly 11 rows, one per defect system, in the order: defect 1 (vacancy) through defect 10 (epoxy), then pristine (defect 11).

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
          "defect_label",
          "E_ads_BnSH_kJmol",
          "Bader_charge_e",
          "E_ads_Pd13_kJmol"
        ],
        "units": {
          "E_ads_BnSH_kJmol": "kJ/mol",
          "Bader_charge_e": "e",
          "E_ads_Pd13_kJmol": "kJ/mol"
        }
      },
      "description": "The computed adsorption energies and Bader charges for BnSH and Pd13 on the 11 graphene models. The hidden checker compares the reported values to reference values for the same physical systems."
    }
  ],
  "notes": "The agent must produce this CSV after running all SIESTA calculations and Bader analysis. The file should contain exactly 11 rows, one per defect system, in the order: defect 1 (vacancy) through defect 10 (epoxy), then pristine (defect 11)."
}
```

## How you are scored
A hidden verifier examines your adsorption_energies.csv. It compares your reported adsorption energies and Bader charges to hidden reference values (derived from the published study) using pre‑defined tolerances that account for differences in DFT implementation. The verifier also checks that the CSV has the correct columns, row order, and value ranges. The reward, ranging from 0 to 1, is based on the fraction of systems whose values meet the criteria. The final reward is the weighted sum over all scored artifacts.
