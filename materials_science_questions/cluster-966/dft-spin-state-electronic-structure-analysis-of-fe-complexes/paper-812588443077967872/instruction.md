# HCN desorption from Fe-adsorbed char: energy barriers and bond orders

## Problem background
During pulverized coal combustion, nitrogen-containing compounds in the fuel are released and converted, with hydrogen cyanide (HCN) serving as a major precursor to nitrogen oxides (NOx). Understanding the factors that control HCN formation from the solid char is important for designing effective NOx emission control strategies. Iron (Fe) is an abundant intrinsic metal element present in many coals, and experimental studies have reported that iron can influence the release of HCN during pyrolysis and combustion — sometimes appearing to suppress it, and sometimes appearing to promote it. However, the atomic-scale mechanism by which iron affects HCN desorption from nitrogen-containing char is not well understood.

This task addresses this question using density functional theory (DFT). A nitrogen-containing char model is constructed, and the effect of Fe on HCN heterogeneous desorption is investigated by comparing reaction pathways on the bare char surface with those on char where a single Fe atom is adsorbed at different hollow sites. The goal is to determine, through direct computation, how the presence of Fe changes the activation energy for HCN release and how it alters the strength of the key C–N bond in the char, and from these quantitative results to establish whether Fe inhibits or promotes HCN formation.

## Approach
The nitrogen-containing char is modeled as a zigzag-edge aromatic cluster of seven fused benzene rings with a single pyridinic nitrogen atom substituted at the edge (the active site). All calculations are carried out at the density functional theory (DFT) level using the B3LYP functional. The Fe atom is treated with the Lanl2DZ effective-core potential and basis set, while carbon, hydrogen, and nitrogen atoms are described with the 6-31G(d) basis set. London dispersion interactions are included via the D3 correction.

The investigation proceeds in four stages:
1. **Build the char model** — generate the atomic coordinates of the bare nitrogen-containing char cluster (C(N)).
2. **Adsorb Fe** — place a single Fe atom above each of the seven distinct hollow (hexagonal) sites H1 through H7 on the char surface and fully optimize each adsorption complex. Compute the adsorption energies.
3. **Map HCN desorption paths** — for the bare char C(N) and for each of the seven Fe-adsorbed complexes, locate the transition states and intermediates along the HCN desorption pathway. Verify each transition state with intrinsic reaction coordinate (IRC) calculations. Determine the rate-determining step for each pathway and extract its activation energy (ΔE‡).
4. **Analyze bond strengths** — compute the Mayer bond order of the C5–N bond in the initial reactant structure of each of the eight pathways (C(N) and Fe@H1 through Fe@H7).

The key comparison is between the activation energies and bond orders obtained for the bare char baseline and those obtained in the presence of Fe at the seven different adsorption sites. The eight computed activation energies and bond orders together reveal the effect of Fe on the ease of HCN release.

## Reproduction target
Produce a CSV file (`activation_energies_and_bond_orders.csv`) containing, for each of the eight systems (the bare char C(N) and the seven Fe-adsorbed configurations Fe@H1 through Fe@H7), the activation energy (in kJ/mol) of the rate-determining step of HCN desorption and the C5–N Mayer bond order (dimensionless) in the initial reactant structure. The file must have one row per system, with columns `system` (string), `activation_energy_kJ_per_mol` (float), and `c5n_bond_order` (float).

## Assets

- DFT software (ORCA, NWChem, or equivalent): https://orcaforum.kofo.mpg.de/
- Multiwfn: http://sobereva.com/multiwfn/

## Workflow steps

### Step 1: Build nitrogen-containing char model
- Role: process
- Action: Construct the zigzag-edge nitrogen-containing char model (C(N)) consisting of seven fused benzene rings with a pyridinic nitrogen at the edge. Generate atomic coordinates for input to quantum chemistry calculations.
- Evidence: `/app/outputs/char_model.xyz`

### Step 2: Fe adsorption on hollow sites
- Role: process
- Action: Perform DFT geometry optimizations of a single Fe atom adsorbed at each of the seven hollow sites (H1–H7) on C(N). Use B3LYP functional with Lanl2DZ for Fe, 6-31G(d) for C, H, N, and D3 dispersion correction. Compute adsorption energies and optimized structures.
- Evidence: `/app/outputs/adsorption_energies.log`

### Step 3: HCN desorption reaction paths
- Role: process
- Action: For C(N) and each Fe-adsorbed configuration, locate the transition states and intermediates along the HCN desorption pathway. Perform IRC calculations to confirm the paths. Compute energy barriers and identify the rate-determining step for each pathway.
- Evidence: `/app/outputs/reaction_energies.log`

### Step 4: Mayer bond order analysis
- Role: process
- Action: For the initial reactant structure of each pathway (C(N) and Fe@H1 to Fe@H7), compute the C5–N Mayer bond order using wavefunction analysis (e.g., Multiwfn). Record the values.
- Evidence: `/app/outputs/bond_orders.txt`

### Step 5: Compile activation energies and bond orders
- Role: scored (load-bearing)
- Action: Collect for each system (C(N) and Fe@H1 to Fe@H7) the activation energy (ΔE‡, kJ/mol) of the rate-determining step and the C5–N Mayer bond order in the initial reactant structure. Write the results to activation_energies_and_bond_orders.csv.
- Output file: `/app/outputs/activation_energies_and_bond_orders.csv`
- Format: csv
- Contract: Columns: system (string), activation_energy_kJ_per_mol (float), c5n_bond_order (float). One row per pathway (8 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies_and_bond_orders.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies_and_bond_orders.csv
- path: `/app/outputs/activation_energies_and_bond_orders.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with the activation energy of the rate-determining step and the C5–N Mayer bond order for each system (C(N) and Fe@H1 to Fe@H7).
- schema:
  - `type`: table
  - `required_columns`: `system`, `activation_energy_kJ_per_mol`, `c5n_bond_order`
  - `units`:
    - `activation_energy_kJ_per_mol`: kJ/mol
    - `c5n_bond_order`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies_and_bond_orders.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "activation_energy_kJ_per_mol",
          "c5n_bond_order"
        ],
        "units": {
          "activation_energy_kJ_per_mol": "kJ/mol",
          "c5n_bond_order": "dimensionless"
        }
      },
      "description": "CSV file with the activation energy of the rate-determining step and the C5–N Mayer bond order for each system (C(N) and Fe@H1 to Fe@H7)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden automated verifier that compares your computed activation energies and bond orders against independently established reference values. Each quantity is checked for agreement within a tolerance that accounts for legitimate differences between DFT implementations. In addition to the individual value agreement, the verifier also assesses whether the pattern of activation energies across the eight systems follows the expected trend that the paper identified from its own calculations. The final reward is a weighted combination of these checks: larger weight is placed on the activation energies and bond orders, while correctly reproducing the trend contributes additional credit. Simply reporting numbers that happen to pass the tolerance without running the required DFT calculations is not expected to succeed, because the hidden verifier evaluates all eight systems and the numerical values must be internally consistent with the physics of the system.
