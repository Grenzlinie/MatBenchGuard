# DFT Adsorption Energies and Charge Transfer on Defective Phosphorene

## Problem background
Phosphorene, the monolayer crystal of black phosphorus, is a direct-bandgap semiconductor with high carrier mobility that holds promise for electronics and optoelectronics. However, its structural stability in air is poor, typically attributed to reactions with environmental water and oxygen molecules. Intrinsic phosphorus vacancies, which can form easily and are abundant, may strongly influence the interaction with these molecules. Understanding how H₂O and O₂ adsorb on perfect and vacancy-containing phosphorene, and how they affect electronic structure and dissociation kinetics, is essential for explaining the material's degradation and for devising protection strategies. This task requires you to use first-principles density functional theory to compute the adsorption energetics, equilibrium geometries, charge transfer, electronic-structure signatures, and the O₂ dissociation pathway on perfect, mono-vacancy (MV), and di-vacancy (DV) phosphorene surfaces.

## Approach
Density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and a van der Waals correction (e.g., optB88-vdW or Grimme D3) is used. Monolayer phosphorene supercells of size 4×5×1 (80 P atoms) are constructed: a perfect lattice, a mono-vacancy (MV) consisting of a pentagon-nonagon (5-9) ring, and a di-vacancy (DV) consisting of a pentagon-heptagon-pentagon-heptagon (5-7-5-7) ring, each with a 20 Å vacuum layer. The isolated H₂O and O₂ molecules and the bare supercells are relaxed. Physisorption geometries are explored by placing each molecule on each substrate in several trial positions and relaxing to the lowest-energy configuration. From the total energies, the adsorption energy Eₐ = E(total) − E(substrate) − E(molecule) is extracted, together with the adsorption height (shortest molecule–surface distance). Net charge transfer is obtained from plane-averaged differential charge density or Bader analysis, with the sign convention that positive Δq indicates electron transfer from the molecule to phosphorene. The electronic density of states (DOS) and/or band structures are computed to identify any midgap states induced by adsorption. For O₂, chemisorbed configurations with O–P bonds are constructed, and the minimum energy path for O–O bond dissociation is located via climbing-image nudged elastic band (CI-NEB). All calculations are performed with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and the crystallographic data of black phosphorus monolayer, which is publicly available.

## Reproduction target
Perform the DFT protocol described above for the molecule–substrate combinations specified below and produce the following artifacts:

1. `adsorption_energies.csv` – adsorption energies (eV) for H₂O and O₂ on perfect, MV, and DV phosphorene (nine rows).
2. `adsorption_heights.csv` – equilibrium adsorption heights (Å) for the same nine systems.
3. `charge_transfer.csv` – net electron transfer (in units of e) for each of the six adsorbed systems.
4. `midgap_states.json` – boolean flags indicating whether a midgap electronic state appears after adsorption, for each of the six systems.
5. `O2_dissociation_barriers.csv` – energy barriers (eV) for O₂ dissociation on perfect and MV phosphorene (two rows).

All files must follow the column schemas and formatting given in the workflow steps below. The computed quantities will be compared to hidden reference values derived from the original study.

## Assets

- Monolayer phosphorene crystallographic data: 10....
- Open-source plane-wave DFT code with PBE functional and van der Waals correction: https://www.quantum-espresso.org/
- Bader charge analysis tool: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Construct phosphorene supercells
- Role: process
- Action: Build 4×5×1 supercells (80 P atoms) of monolayer phosphorene for the perfect, mono-vacancy (5-9 ring), and di-vacancy (5-7-5-7 ring) configurations using known lattice parameters. Include a 20 Å vacuum layer.
- Evidence: `/app/outputs/supercell_structures.log`

### Step 2: Optimize isolated H₂O and O₂ molecules
- Role: process
- Action: Perform DFT geometry optimization of an isolated H₂O molecule and an isolated O₂ molecule in a large box. Record the final total energies.
- Evidence: `/app/outputs/isolated_mol_energies.log`

### Step 3: Optimize pristine and defective phosphorene slabs
- Role: process
- Action: Perform DFT relaxations of the perfect, MV, and DV phosphorene supercells. Record final total energies and relaxed atomic positions.
- Evidence: `/app/outputs/slab_energies.log`

### Step 4: Physisorption geometry optimization (all molecule–substrate combinations)
- Role: process
- Action: For each combination of molecule (H₂O, O₂) and substrate (perfect, MV, DV), place the molecule in candidate positions above the surface and perform DFT relaxations to identify the lowest-energy physisorbed configuration. Save final total energy, optimized geometry, and molecule–surface distance.
- Evidence: `/app/outputs/adsorption_geometries.log`

### Step 5: Compute adsorption energies
- Role: scored (load-bearing)
- Action: Using the total energies from steps s02, s03, and s04, compute the adsorption energy Eₐ = E(Mol+P) – E(P) – E(Mol) for each system. Output a CSV with columns: molecule, substrate, adsorption_energy_eV.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Column names: molecule (string), substrate (string, one of perfect/MV/DV), adsorption_energy_eV (float). Nine rows total.
- Scoring: scored by hidden verifier

### Step 6: Extract adsorption heights
- Role: scored (load-bearing)
- Action: From the optimized geometries of step s04, extract the adsorption height as the shortest vertical distance between any molecule atom and the topmost phosphorus atom of the slab. Output a CSV with columns: molecule, substrate, height_A.
- Output file: `/app/outputs/adsorption_heights.csv`
- Format: csv
- Contract: Column names: molecule (string), substrate (string, one of perfect/MV/DV), height_A (float). Nine rows total.
- Scoring: scored by hidden verifier

### Step 7: Charge transfer analysis
- Role: scored (load-bearing)
- Action: For each of the six optimized adsorption systems, compute the net electron transfer between the molecule and the phosphorene surface (positive Δq = electrons transferred from molecule to phosphorene). Use plane-averaged differential charge density or Bader analysis. Output a CSV with columns: molecule, substrate, delta_q_e.
- Output file: `/app/outputs/charge_transfer.csv`
- Format: csv
- Contract: Column names: molecule (string), substrate (string, one of perfect/MV/DV), delta_q_e (float). Nine rows total.
- Scoring: scored by hidden verifier

### Step 8: Electronic structure (DOS) calculations for adsorbed systems
- Role: process
- Action: For each of the six adsorbed systems and the bare slabs, compute the electronic density of states (DOS) and/or band structure using the same DFT functional. Store the data for analysis of in-gap states.
- Evidence: `/app/outputs/dos_data.log`

### Step 9: Gap-state analysis
- Role: scored (load-bearing)
- Action: From the DOS/band structures, determine for each adsorption system whether any additional electronic state appears inside the fundamental band gap of phosphorene (midgap state). Record as a boolean flag. Output a JSON file.
- Output file: `/app/outputs/midgap_states.json`
- Format: json
- Contract: A JSON object with key "midgap_states", its value an array of objects. Each object has fields: molecule (string, "H2O" or "O2"), substrate (string, "perfect", "MV", or "DV"), has_midgap_state (boolean). Six entries total.
- Scoring: scored by hidden verifier

### Step 10: Obtain chemisorbed O₂ configurations
- Role: process
- Action: For the perfect and MV phosphorene surfaces, construct and DFT-optimize configurations where the O₂ molecule forms O–P bonds (chemisorbed state). These serve as endpoints for the NEB pathway.
- Evidence: `/app/outputs/chemisorbed_O2.log`

### Step 11: NEB barrier calculation for O₂ dissociation
- Role: process
- Action: Using the physisorbed O₂ configurations from step s04 and the chemisorbed configurations from step s09, perform climbing-image nudged elastic band (CI-NEB) calculations to locate the minimum energy path for O₂ dissociation on perfect and MV phosphorene. Record the energy profiles.
- Evidence: `/app/outputs/neb_path.log`

### Step 12: Extract O₂ dissociation barriers
- Role: scored (load-bearing)
- Action: From the NEB energy profiles of step s10, determine the dissociation energy barrier (highest energy relative to the physisorbed state) for O₂ on perfect and on MV phosphorene. Output a CSV with columns: substrate, barrier_eV.
- Output file: `/app/outputs/O2_dissociation_barriers.csv`
- Format: csv
- Contract: Column names: substrate (string, "perfect" or "MV"), barrier_eV (float). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/adsorption_heights.csv`
- `/app/outputs/charge_transfer.csv`
- `/app/outputs/midgap_states.json`
- `/app/outputs/O2_dissociation_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Adsorption energies; lower (more negative) values indicate stronger binding.
- schema:
  - `required_columns`: `molecule`, `substrate`, `adsorption_energy_eV`
  - `description`: Each row: molecule (H2O or O2), substrate (perfect, MV, DV), adsorption_energy_eV (float, more negative is better).

### adsorption_heights.csv
- path: `/app/outputs/adsorption_heights.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adsorption heights; compared to hidden reference within a small tolerance.
- schema:
  - `required_columns`: `molecule`, `substrate`, `height_A`
  - `description`: Each row: molecule (H2O or O2), substrate (perfect, MV, DV), height_A (float, distance in Å).

### charge_transfer.csv
- path: `/app/outputs/charge_transfer.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Net electron transfer; value must match reference within a tolerance.
- schema:
  - `required_columns`: `molecule`, `substrate`, `delta_q_e`
  - `description`: Each row: molecule (H2O or O2), substrate (perfect, MV, DV), delta_q_e (float, positive means electron transfer from molecule to phosphorene).

### midgap_states.json
- path: `/app/outputs/midgap_states.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Boolean flags for midgap state presence; exact match required for each system.
- schema:
  - `type`: object
  - `required`: `midgap_states`
  - `items`:
    - `molecule`: string
    - `substrate`: string
    - `has_midgap_state`: boolean

### O2_dissociation_barriers.csv
- path: `/app/outputs/O2_dissociation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: O₂ dissociation energy barriers; a lower value than the reference is also acceptable.
- schema:
  - `required_columns`: `substrate`, `barrier_eV`
  - `description`: Each row: substrate (perfect or MV), barrier_eV (float, lower barrier is better/easier dissociation).

Notes: All scored artifacts are derived from DFT computations. The checker compares submitted values to hidden gold within predefined tolerances; directional metrics allow better-than-paper results to earn full credit.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "required_columns": [
          "molecule",
          "substrate",
          "adsorption_energy_eV"
        ],
        "description": "Each row: molecule (H2O or O2), substrate (perfect, MV, DV), adsorption_energy_eV (float, more negative is better)."
      },
      "description": "Adsorption energies; lower (more negative) values indicate stronger binding."
    },
    {
      "file": "adsorption_heights.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "molecule",
          "substrate",
          "height_A"
        ],
        "description": "Each row: molecule (H2O or O2), substrate (perfect, MV, DV), height_A (float, distance in Å)."
      },
      "description": "Adsorption heights; compared to hidden reference within a small tolerance."
    },
    {
      "file": "charge_transfer.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required_columns": [
          "molecule",
          "substrate",
          "delta_q_e"
        ],
        "description": "Each row: molecule (H2O or O2), substrate (perfect, MV, DV), delta_q_e (float, positive means electron transfer from molecule to phosphorene)."
      },
      "description": "Net electron transfer; value must match reference within a tolerance."
    },
    {
      "file": "midgap_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "midgap_states"
        ],
        "items": {
          "molecule": "string",
          "substrate": "string",
          "has_midgap_state": "boolean"
        }
      },
      "description": "Boolean flags for midgap state presence; exact match required for each system."
    },
    {
      "file": "O2_dissociation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "required_columns": [
          "substrate",
          "barrier_eV"
        ],
        "description": "Each row: substrate (perfect or MV), barrier_eV (float, lower barrier is better/easier dissociation)."
      },
      "description": "O₂ dissociation energy barriers; a lower value than the reference is also acceptable."
    }
  ],
  "notes": "All scored artifacts are derived from DFT computations. The checker compares submitted values to hidden gold within predefined tolerances; directional metrics allow better-than-paper results to earn full credit."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently examines each of the five scored artifacts.

For numerical quantities that improve with better performance (adsorption energies: more negative; dissociation barriers: lower), the verifier awards full credit when your value meets or exceeds the reference, and progressively less credit as the result falls short. For quantities where a better value is undefined (adsorption heights, charge transfer), the verifier requires close agreement with the reference within a tolerance; an exact match is expected for the boolean midgap-state flags.

The verifier checks that the files match the specified schemas (column names, row counts, types) and then compares your reported values to hidden gold values. The final reward is a weighted combination of the scores from all five artifacts, normalized to a float between 0 and 1. Producing credible results requires genuinely running the DFT workflow; the verifier is designed to reward correct physics rather than copied numbers.
