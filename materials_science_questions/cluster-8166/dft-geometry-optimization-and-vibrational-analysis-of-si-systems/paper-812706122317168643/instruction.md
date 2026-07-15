# Ethylene Adsorption on Si5-7 Clusters: DFT Geometry Optimization and Binding Energy Reproduction

## Problem background
Silicon clusters are of fundamental and technological interest because they bridge atomic and extended surface properties. Understanding how small molecules such as ethylene adsorb on neutral silicon clusters is essential for interpreting cluster reactivity and comparing it with surface chemistry. This task investigates ethylene adsorption on Si5, Si6, and Si7 clusters using density functional theory. The key quantities to determine are the adsorption energies at several distinct binding sites and the structural changes induced in both the ethylene molecule and the cluster. Such calculations help reveal the nature of the bonding (e.g., di‑σ vs. π) and any reconstruction of the cluster following adsorption.

## Approach
The reproduction uses an open‑source periodic density‑functional‑theory (DFT) code at the PBE level with standard pseudopotentials. No molecular dynamics is required; all calculations are static geometry optimizations. First, the isolated silicon clusters—Si5 (trigonal bipyramid), Si6 (tetragonal bipyramid), Si7 (pentagonal bipyramid)—and the free ethylene molecule are optimized. Then, for each cluster, initial adsorption geometries are constructed by placing ethylene at specified sites: atop the capped atom, atop a side atom, the short bridge (between a capped and a side atom), and the long bridge (between two side atoms) on Si5; atop a side atom, short bridge, and long bridge on Si6; and the short bridge on Si7. All adsorption complexes are relaxed, and total energies are recorded. The adsorption energy for each site is computed as ΔE = E(complex) – E(isolated cluster) – E(ethylene). For the site on Si5 that yields the highest adsorption energy, the relaxed geometry is analyzed to extract the C–C bond length, two Si–C bond lengths, the CH2 bend angle, and three interatomic distances within the cluster (d1‑2, d1‑4, d4‑5). The relative ordering of the adsorption energies on Si5 and Si6 is also determined.

## Reproduction target
Produce the following scored CSV artifacts:
- `si5_adsorption_energies.csv`: adsorption energies (eV) for the four Si5 sites: atop_capped, atop_side, short_bridge, long_bridge.
- `si5_short_bridge_structure.csv`: six structural parameters from the relaxed short‑bridge complex on Si5 (C‑C_bond_length, Si1‑C_bond_length, Si4‑C_bond_length, CH2_bend_angle, d1‑2, d1‑4, d4‑5).
- `si6_adsorption_energies.csv`: adsorption energies (eV) for the three Si6 sites: atop_side, short_bridge, long_bridge.
- `si7_adsorption_energy.csv`: adsorption energy (eV) for the Si7 short‑bridge site.
The energies must be consistent with the correct energetic ordering: on Si5 the highest adsorption energy should correspond to one of the computed sites, and on Si6 the highest energy should also correspond to a specific site. The structural parameters must be those of the Si5 complex with the highest adsorption energy. All values must result from DFT geometry optimizations following the workflow described in the steps below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE efficiency): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Free cluster and molecule geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for the isolated Si5 (trigonal bipyramid), Si6 (tetragonal bipyramid), Si7 (pentagonal bipyramid) clusters, and the isolated C2H4 molecule. The optimized atomic coordinates serve as reference structures for subsequent adsorption energy calculations.
- Evidence: `/app/outputs/si5.xyz, si6.xyz, si7.xyz, c2h4.xyz`

### Step 2: Adsorption complex relaxations
- Role: process
- Action: For each cluster, build initial adsorption geometries at the required sites: Si5: atop_capped, atop_side, short_bridge, long_bridge; Si6: atop_side, short_bridge, long_bridge; Si7: short_bridge. Relax these complexes using DFT. Record total energies and final coordinates for each site.
- Evidence: `/app/outputs/ (directory with relaxation logs and coordinates)`

### Step 3: Si5 adsorption energies
- Role: scored (load-bearing)
- Action: From the relaxed complexes, compute adsorption energies E_ads = E_complex - E_si5 - E_c2h4 for each of the four Si5 adsorption sites. Write a CSV with columns site and energy_eV.
- Output file: `/app/outputs/si5_adsorption_energies.csv`
- Format: csv
- Contract: columns: site (string), energy_eV (float). Sites: atop_capped, atop_side, short_bridge, long_bridge.
- Scoring: scored by hidden verifier

### Step 4: Si5 short bridge structure parameters
- Role: scored
- Action: From the relaxed short_bridge complex of Si5, extract the C-C bond length (Å), Si1-C bond length (Å), Si4-C bond length (Å), CH2 scissor plane bend angle (degrees), and the cluster distances d1-2 (Å), d1-4 (Å), d4-5 (Å). Write a CSV with columns parameter and value.
- Output file: `/app/outputs/si5_short_bridge_structure.csv`
- Format: csv
- Contract: columns: parameter (string), value (float). Required parameters: C-C_bond_length, Si1-C_bond_length, Si4-C_bond_length, CH2_bend_angle, d1-2, d1-4, d4-5.
- Scoring: scored by hidden verifier

### Step 5: Si6 adsorption energies
- Role: scored
- Action: Compute adsorption energies for the three Si6 sites (atop_side, short_bridge, long_bridge) as E_ads = E_complex - E_si6 - E_c2h4. Write a CSV with columns site and energy_eV.
- Output file: `/app/outputs/si6_adsorption_energies.csv`
- Format: csv
- Contract: columns: site (string), energy_eV (float). Sites: atop_side, short_bridge, long_bridge.
- Scoring: scored by hidden verifier

### Step 6: Si7 adsorption energy
- Role: scored
- Action: Compute adsorption energy for the Si7 short_bridge site. Write a CSV with columns site and energy_eV.
- Output file: `/app/outputs/si7_adsorption_energy.csv`
- Format: csv
- Contract: columns: site (string), energy_eV (float). Site: short_bridge.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/si5_adsorption_energies.csv`
- `/app/outputs/si5_short_bridge_structure.csv`
- `/app/outputs/si6_adsorption_energies.csv`
- `/app/outputs/si7_adsorption_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### si5_adsorption_energies.csv
- path: `/app/outputs/si5_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies for Si5 at four sites: atop_capped, atop_side, short_bridge, long_bridge. The checker compares each value to the hidden gold within tolerance and verifies the short_bridge energy is highest.
- schema:
  - `type`: table
  - `required_columns`: `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### si5_short_bridge_structure.csv
- path: `/app/outputs/si5_short_bridge_structure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Structural parameters for the short-bridge Si5+ethylene complex. Parameters: C-C_bond_length, Si1-C_bond_length, Si4-C_bond_length, CH2_bend_angle, d1-2, d1-4, d4-5.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`
  - `units`:
    - `value`: Angstrom for lengths, degrees for angles

### si6_adsorption_energies.csv
- path: `/app/outputs/si6_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies for Si6 at three sites: atop_side, short_bridge, long_bridge. Checker validates values and that atop_side is highest.
- schema:
  - `type`: table
  - `required_columns`: `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### si7_adsorption_energy.csv
- path: `/app/outputs/si7_adsorption_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energy for Si7 short-bridge site. Checker compares to gold with tolerance and ensures positivity.
- schema:
  - `type`: table
  - `required_columns`: `site`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

Notes: Scoring uses result-level comparison: the hidden checker has the paper's reported values (adsorption energies, bond lengths, angles) and tolerances. The checker also enforces the ranking requirement for Si5 (short bridge highest) and Si6 (atop side highest).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "si5_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Adsorption energies for Si5 at four sites: atop_capped, atop_side, short_bridge, long_bridge. The checker compares each value to the hidden gold within tolerance and verifies the short_bridge energy is highest."
    },
    {
      "file": "si5_short_bridge_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value"
        ],
        "units": {
          "value": "Angstrom for lengths, degrees for angles"
        }
      },
      "description": "Structural parameters for the short-bridge Si5+ethylene complex. Parameters: C-C_bond_length, Si1-C_bond_length, Si4-C_bond_length, CH2_bend_angle, d1-2, d1-4, d4-5."
    },
    {
      "file": "si6_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Adsorption energies for Si6 at three sites: atop_side, short_bridge, long_bridge. Checker validates values and that atop_side is highest."
    },
    {
      "file": "si7_adsorption_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "Adsorption energy for Si7 short-bridge site. Checker compares to gold with tolerance and ensures positivity."
    }
  ],
  "notes": "Scoring uses result-level comparison: the hidden checker has the paper's reported values (adsorption energies, bond lengths, angles) and tolerances. The checker also enforces the ranking requirement for Si5 (short bridge highest) and Si6 (atop side highest)."
}
```

## How you are scored
A hidden verifier reads each submitted CSV file. It compares the reported adsorption energies and structural parameters to reference values (the paper’s originally reported results) using tolerances that capture legitimate differences between computational setups. It also checks that on Si5 the short‑bridge energy is the highest among the four sites and on Si6 the atop‑side energy is the highest among the three sites. The reward is a weighted composite score (0 to 1) that reflects the fraction of checks that pass. Simply writing numbers that match the reference without genuinely running the DFT workflow will not satisfy the downstream load‑bearing requirements; the artifacts must be produced by executing the simulation pipeline.
