# Ethanol Dehydrogenation on 2Rh/γ-Al2O3(110) Surface under Dehydrated and Hydrated Conditions

## Problem background
Ethanol steam reforming over Rh/γ-Al2O3 catalysts is a promising route for hydrogen production, but it can suffer from catalyst deactivation due to coke formation via ethene. The presence of water is known to influence the selectivity of ethanol decomposition, but the atomistic mechanism by which water alters the reaction pathway—particularly how it affects ethanol adsorption modes and C–C bond scission barriers on model catalyst surfaces—remains an important open question. This task aims to compute, using periodic density functional theory, the adsorption energies and reaction barriers for ethanol on a well-defined 2Rh/γ-Al2O3(110) surface under both dehydrated and hydrated conditions, and to determine whether water changes the stability of key ring intermediates that control ethene formation.

## Approach
The investigation is conducted with periodic density functional theory (DFT) using the PW91 exchange-correlation functional and PAW pseudopotentials. The model catalyst consists of a γ-Al2O3(110) slab (8 layers, with the bottom five fixed) onto which two Rh atoms are placed at specified surface sites that represent the preferred binding positions. The clean slab is built from the bulk γ-Al2O3 structure and relaxed. Two surface states are compared: (i) the dehydrated 2Rh surface and (ii) a hydrated surface prepared by adding three water molecules that adsorb dissociatively (as H + OH) on the Al surface sites.

Gas-phase reference energies of isolated ethanol and water molecules are computed in large periodic boxes. For each surface state, the most stable adsorption mode of ethanol is located by geometry optimization, and the adsorption energy is derived. The minimum-energy path for C–C bond cleavage is then determined with the Nudged Elastic Band (NEB) method, yielding the reaction barrier. Finally, for the dehydrated surface, an attempt is made to stabilize a five-membered-ring (oxametallacycle) intermediate, and its stability is checked via vibrational analysis; the same search is repeated on the hydrated surface to see whether the ring is absent. The calculations are expected to be performed in an open-source plane-wave DFT code with consistent computational parameters (plane-wave cutoff, k-point sampling) throughout.

## Reproduction target
The goal is to produce the following quantities, all in kcal/mol, by executing the workflow described in the steps:
  - The most stable ethanol adsorption energy on the dehydrated 2Rh/γ-Al2O3(110) surface.
  - The energy barrier for C–C bond scission of ethanol on that dehydrated surface.
  - The ethanol adsorption energy on the hydrated 3H2O/2Rh surface.
  - The energy barrier for C–C bond scission on that hydrated surface.
  - A verification of the stability of a five-membered-ring oxametallacycle intermediate on the dehydrated surface (stable or not) and its electronic energy, and the corresponding result for the hydrated surface.
The values must be computed from DFT total energies obtained with the PW91 functional and the described surface model, and reported in the specified output CSV files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PW91 PAW pseudopotentials for Al, O, Rh, H, C: https://www.quantum-espresso.org/pseudopotentials/
- γ-Al2O3 bulk crystal structure: 10.1016/j.jcat.2004.06.027
- Gas-phase ethanol and water molecular structures

## Workflow steps

### Step 1: Reference energies of isolated gas-phase species
- Role: process
- Action: Compute DFT total energy of an isolated ethanol molecule and an isolated water molecule in large periodic boxes (≈12 Å³) using PW91 functional and the same plane-wave cutoff as the surface calculations. These energies serve as references for adsorption energy formulas.
- Evidence: `/app/outputs/gas_phase_energies.log`

### Step 2: Bulk γ-Al2O3 structure optimization
- Role: process
- Action: Starting from the experimental monoclinic unit cell of γ-Al2O3 (8 Al2O3 units), perform a variable-cell DFT relaxation to obtain equilibrium lattice parameters (a, b, c, β) that will later be used to build the surface slab.
- Evidence: `/app/outputs/bulk_optimized.log`

### Step 3: Construction and relaxation of the clean γ-Al2O3(110) slab
- Role: process
- Action: Cleave the (110) surface from the optimized bulk, build an 8-layer slab with ~12 Å vacuum. Fix the bottom five layers and relax the top three layers using DFT.
- Evidence: `/app/outputs/clean_slab_relaxed.structure`

### Step 4: Construction of the 2Rh/γ-Al2O3(110) model surface
- Role: process
- Action: Place two Rh atoms on the relaxed clean slab at grid coordinates (6,4) and (8,6) (positions from the paper's potential energy surface). Optimize the geometry of the top three layers plus Rh atoms while fixing the bottom five layers. This yields the dehydrated 2Rh/slab.
- Evidence: `/app/outputs/2Rh_slab_relaxed.structure`

### Step 5: Ethanol adsorption energy on dehydrated surface
- Role: scored (load-bearing)
- Action: Adsorb one ethanol molecule on the relaxed 2Rh/slab in the most stable mode (mode B, with the Cβ-H bond engaging Rh and the O-H group oriented toward the surface). Optimize the geometry and compute the adsorption energy E_ads = E(slab+ethanol) - E(slab) - E(gas-phase ethanol). Report in kcal/mol.
- Output file: `/app/outputs/ethanol_adsorption_dehydrated.csv`
- Format: csv
- Contract: CSV with one row, column "E_ads_kcal_mol" (float).
- Scoring: scored by hidden verifier

### Step 6: C–C bond scission barrier on dehydrated surface
- Role: scored
- Action: First construct a stable four-membered-ring (oxametallacycle) intermediate on the dehydrated 2Rh/slab, analogous to the intermediate formed after Cα–H scission, in which Cα binds to Rh and the OH group binds to an Al surface atom. Optimise its geometry to obtain a true minimum (no imaginary frequencies). Then, using the Nudged Elastic Band (NEB) method, locate the minimum-energy path for C–C bond cleavage from this four-membered-ring intermediate to the dissociated products (CH3(a) + CO(a) + 3H(a) on the surface). Report the energy barrier (highest point along the path relative to the initial four-membered-ring intermediate state) in kcal/mol.
- Output file: `/app/outputs/c_c_barrier_dehydrated.csv`
- Format: csv
- Contract: CSV with one row, column "barrier_kcal_mol" (float).
- Scoring: scored by hidden verifier

### Step 7: Construction of the hydrated 3H2O/2Rh surface
- Role: process
- Action: Add three water molecules to the relaxed 2Rh/slab, allowing dissociative adsorption (H2O → H + OH on surface Al sites). Optimize the resulting hydrated surface geometry, keeping the bottom five layers fixed.
- Evidence: `/app/outputs/hydrated_2Rh_slab.structure`

### Step 8: Ethanol adsorption energy on hydrated surface
- Role: scored
- Action: Adsorb one ethanol molecule on the relaxed 3H2O/2Rh slab in mode C2 (Cα–H bond interacting with Rh, no direct O–H adsorption on Al). Optimize and compute the adsorption energy relative to the hydrated slab and gas-phase ethanol. Report in kcal/mol.
- Output file: `/app/outputs/ethanol_adsorption_hydrated.csv`
- Format: csv
- Contract: CSV with one row, column "E_ads_kcal_mol" (float).
- Scoring: scored by hidden verifier

### Step 9: C–C bond scission barrier on hydrated surface
- Role: scored
- Action: Use NEB to find the minimum-energy path for C–C bond cleavage of ethanol on the hydrated slab. Start from the optimized ethanol adsorbate and end with dissociated products (same as step 5). Report the energy barrier in kcal/mol.
- Output file: `/app/outputs/c_c_barrier_hydrated.csv`
- Format: csv
- Contract: CSV with one row, column "barrier_kcal_mol" (float).
- Scoring: scored by hidden verifier

### Step 10: Five-membered-ring intermediate stability
- Role: scored
- Action: For the dehydrated surface, attempt to localize a stable five-membered-ring (oxametallacycle) intermediate analogous to LM7 by relaxing the expected structure and checking for imaginary frequencies. Record its electronic energy. For the hydrated surface, perform the same structural search and verify that a stable ring intermediate is not obtained. Report a boolean (true/false) and the corresponding energy (or final energy after attempted optimization) in kcal/mol.
- Output file: `/app/outputs/ring_stability.csv`
- Format: csv
- Contract: CSV with columns "system" (string, either 'dehydrated' or 'hydrated'), "ring_stable" (boolean, true/false), "intermediate_energy_kcal_mol" (float). Two rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ethanol_adsorption_dehydrated.csv`
- `/app/outputs/c_c_barrier_dehydrated.csv`
- `/app/outputs/ethanol_adsorption_hydrated.csv`
- `/app/outputs/c_c_barrier_hydrated.csv`
- `/app/outputs/ring_stability.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ethanol_adsorption_dehydrated.csv
- path: `/app/outputs/ethanol_adsorption_dehydrated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Most stable ethanol adsorption energy on the dehydrated 2Rh/γ-Al2O3(110) surface.
- schema:
  - `type`: table
  - `required_columns`: `E_ads_kcal_mol`
  - `units`:
    - `E_ads_kcal_mol`: kcal/mol

### c_c_barrier_dehydrated.csv
- path: `/app/outputs/c_c_barrier_dehydrated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy barrier for C–C bond scission of ethanol on the dehydrated surface.
- schema:
  - `type`: table
  - `required_columns`: `barrier_kcal_mol`
  - `units`:
    - `barrier_kcal_mol`: kcal/mol

### ethanol_adsorption_hydrated.csv
- path: `/app/outputs/ethanol_adsorption_hydrated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ethanol adsorption energy on the hydrated 3H2O/2Rh surface.
- schema:
  - `type`: table
  - `required_columns`: `E_ads_kcal_mol`
  - `units`:
    - `E_ads_kcal_mol`: kcal/mol

### c_c_barrier_hydrated.csv
- path: `/app/outputs/c_c_barrier_hydrated.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy barrier for C–C bond scission of ethanol on the hydrated surface.
- schema:
  - `type`: table
  - `required_columns`: `barrier_kcal_mol`
  - `units`:
    - `barrier_kcal_mol`: kcal/mol

### ring_stability.csv
- path: `/app/outputs/ring_stability.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stability of the five-membered-ring intermediate on dehydrated and hydrated surfaces; structural evidence for the mechanism change induced by water.
- schema:
  - `type`: table
  - `required_columns`: `system`, `ring_stable`, `intermediate_energy_kcal_mol`
  - `units`:
    - `intermediate_energy_kcal_mol`: kcal/mol

Notes: All energies must be reported in kcal/mol. The checker will compare the reported adsorption energies and barriers against paper values with appropriate tolerances (exact_match). The ring stability file must contain correct boolean states and energy values consistent with a stable minimum on the dehydrated surface and absence thereof on the hydrated surface (structural_audit). No hidden gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ethanol_adsorption_dehydrated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_ads_kcal_mol"
        ],
        "units": {
          "E_ads_kcal_mol": "kcal/mol"
        }
      },
      "description": "Most stable ethanol adsorption energy on the dehydrated 2Rh/γ-Al2O3(110) surface."
    },
    {
      "file": "c_c_barrier_dehydrated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "barrier_kcal_mol"
        ],
        "units": {
          "barrier_kcal_mol": "kcal/mol"
        }
      },
      "description": "Energy barrier for C–C bond scission of ethanol on the dehydrated surface."
    },
    {
      "file": "ethanol_adsorption_hydrated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_ads_kcal_mol"
        ],
        "units": {
          "E_ads_kcal_mol": "kcal/mol"
        }
      },
      "description": "Ethanol adsorption energy on the hydrated 3H2O/2Rh surface."
    },
    {
      "file": "c_c_barrier_hydrated.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "barrier_kcal_mol"
        ],
        "units": {
          "barrier_kcal_mol": "kcal/mol"
        }
      },
      "description": "Energy barrier for C–C bond scission of ethanol on the hydrated surface."
    },
    {
      "file": "ring_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "ring_stable",
          "intermediate_energy_kcal_mol"
        ],
        "units": {
          "intermediate_energy_kcal_mol": "kcal/mol"
        }
      },
      "description": "Stability of the five-membered-ring intermediate on dehydrated and hydrated surfaces; structural evidence for the mechanism change induced by water."
    }
  ],
  "notes": "All energies must be reported in kcal/mol. The checker will compare the reported adsorption energies and barriers against paper values with appropriate tolerances (exact_match). The ring stability file must contain correct boolean states and energy values consistent with a stable minimum on the dehydrated surface and absence thereof on the hydrated surface (structural_audit). No hidden gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier checks each of your five output files independently. For the adsorption energy and barrier files, it compares your reported numbers to reference values (derived from the original DFT study) using appropriate tolerances; better-than-reference results are accepted. For the ring stability file, it verifies that the boolean states and the reported energies are physically consistent with the expected trend (a stable ring on the dehydrated surface and no stable ring on the hydrated surface). Each output contributes a weight to a total reward between 0 and 1. You must produce the files as described; the verifier does not re-run your DFT calculations, so every reported quantity must be computed honestly from actual calculations.
