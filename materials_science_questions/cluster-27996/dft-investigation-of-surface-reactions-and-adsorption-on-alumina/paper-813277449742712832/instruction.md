# DFT Computation of Adsorption and Hydrogenation Barriers for C1–C4 Carbonyls on Ru(0001)

## Problem background
The catalytic conversion of biomass-derived oxygenates into fuels and chemicals requires understanding how molecular structure affects reactivity on metal surfaces. Aldehydes and ketones are key intermediates, and their hydrogenation on transition metals like ruthenium is governed by elementary steps whose barriers depend on the alkyl substituents attached to the carbonyl group. This task reproduces a systematic first-principles investigation of the adsorption and initial hydrogen addition for a series of C1–C4 carbonyls on Ru(0001).

## Approach
Periodic density functional theory (DFT) calculations are used to model the Ru(0001) surface and the reacting molecules. A four-layer slab represents the metal, with the bottom layer fixed at the experimental lattice constant. The exchange-correlation functional is PW91, and a plane-wave basis set with ultrasoft pseudopotentials is employed. For each carbonyl, the most stable adsorption configuration on the slab is found by geometry optimization, and the adsorption energy is computed. The first hydrogen addition steps—to the carbonyl oxygen (hydroxy route) and to the carbonyl carbon (alkoxy route)—are studied by locating transition states with the climbing-image nudged elastic band (CI-NEB) method. All required molecular models and reaction intermediates must be constructed, and the final energetic results gathered into a structured output file.

## Reproduction target
Compute the adsorption energy (E_ads) and the activation barriers for the first hydrogen addition to the carbonyl oxygen (hydroxy TS1) and to the carbonyl carbon (alkoxy TS1) for each of the six carbonyls: formaldehyde, acetaldehyde, propionaldehyde, acetone, butyraldehyde, and methyl ethyl ketone (MEK) on a Ru(0001) surface. Report the results in a CSV file named carbonyl_results.csv with columns: species (string), adsorption_energy (float, kJ/mol), hydroxy_TS1_barrier (float, kJ/mol), alkoxy_TS1_barrier (float, kJ/mol). Any missing value should be recorded as NaN.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build Ru(0001) surface slab and adsorbate models
- Role: process
- Action: Construct a periodic 4-layer Ru(0001) slab with the experimental lattice constant a=2.71 Å, fixing the bottom layer and allowing the top three layers and adsorbates to relax. Build gas-phase molecular models for formaldehyde, acetaldehyde, propionaldehyde, acetone, butyraldehyde, methyl ethyl ketone (MEK), atomic hydrogen, and the relevant hydroxyalkyl and alkoxy intermediates for transition state searches.
- Evidence: `/app/outputs/slab_and_models.log`

### Step 2: Compute adsorption energies and activation barriers
- Role: scored (load-bearing)
- Action: Run periodic DFT calculations using Quantum ESPRESSO with the PW91 functional, a plane-wave basis set, and ultrasoft pseudopotentials. For each carbonyl (formaldehyde, acetaldehyde, propionaldehyde, acetone, butyraldehyde, MEK) on the Ru(0001) slab: (a) perform geometry optimization of the adsorbed carbonyl to find the most stable adsorption configuration and compute the adsorption energy E_ads = E_adsorbate/slab − E_adsorbate(gas) − E_slab; (b) use the CI-NEB method to locate transition states for the first hydrogen addition to the carbonyl oxygen (hydroxy TS1) and to the carbonyl carbon (alkoxy TS1), and compute the corresponding activation barriers. Extract all results into the CSV file.
- Output file: `/app/outputs/carbonyl_results.csv`
- Format: csv
- Contract: species (string), adsorption_energy (float, kJ/mol), hydroxy_TS1_barrier (float, kJ/mol), alkoxy_TS1_barrier (float, kJ/mol). One row per carbonyl. Missing values as NaN.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/carbonyl_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### carbonyl_results.csv
- path: `/app/outputs/carbonyl_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies and activation barriers for the first hydrogen addition steps of six carbonyls on Ru(0001). The checker compares these values to a hidden reference with tolerances and verifies qualitative trends.
- schema:
  - `required_columns`: `species`, `adsorption_energy`, `hydroxy_TS1_barrier`, `alkoxy_TS1_barrier`
  - `units`:
    - `adsorption_energy`: kJ/mol
    - `hydroxy_TS1_barrier`: kJ/mol
    - `alkoxy_TS1_barrier`: kJ/mol

Notes: Only the first hydrogen addition barriers are required; second hydrogenation steps and kinetic Monte Carlo simulations are excluded. The agent must use an open-source DFT code (Quantum ESPRESSO) with comparable settings (PW91 functional, ultrasoft pseudopotentials, appropriate k-point mesh and energy cutoff).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "carbonyl_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "species",
          "adsorption_energy",
          "hydroxy_TS1_barrier",
          "alkoxy_TS1_barrier"
        ],
        "units": {
          "adsorption_energy": "kJ/mol",
          "hydroxy_TS1_barrier": "kJ/mol",
          "alkoxy_TS1_barrier": "kJ/mol"
        }
      },
      "description": "Adsorption energies and activation barriers for the first hydrogen addition steps of six carbonyls on Ru(0001). The checker compares these values to a hidden reference with tolerances and verifies qualitative trends."
    }
  ],
  "notes": "Only the first hydrogen addition barriers are required; second hydrogenation steps and kinetic Monte Carlo simulations are excluded. The agent must use an open-source DFT code (Quantum ESPRESSO) with comparable settings (PW91 functional, ultrasoft pseudopotentials, appropriate k-point mesh and energy cutoff)."
}
```

## How you are scored
Your submitted carbonyl_results.csv is evaluated by an automated hidden verifier. The verifier reads your file and compares each reported numerical value to a hidden reference dataset, checking numerical agreement within reasonable tolerance bounds. It also examines whether certain expected qualitative trends across the set of molecules are correctly reproduced. The final reward is a fraction between 0 and 1, reflecting the proportion of comparisons that pass. The workflow itself is not directly scored; only the content of the output file is assessed, but the computations must be genuinely performed to produce a valid artifact.
