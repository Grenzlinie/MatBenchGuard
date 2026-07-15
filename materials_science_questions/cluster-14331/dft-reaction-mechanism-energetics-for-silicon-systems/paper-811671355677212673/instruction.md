# DFT Reaction Mechanism Energetics for Silicon Systems

## Problem background
The catalytic [3+2] cycloaddition of N-acylhydrazones to cyclopentadiene using a silicon-based Lewis acid (TMSOTf) proceeds with high yields and diastereoselectivities favoring the syn product. Understanding the mechanism and the origin of the selectivity requires computational investigation. This task targets the DFT study that compares two plausible reaction pathways (A and B) and computes the activation energy differences between the syn and anti transition states to predict the product ratio.

## Approach
Perform density functional theory (DFT) calculations at the B3LYP/TZV level of theory on the model system: hydrazone 1a (R = p-O2NC6H4, R' = CO2Et), cyclopentadiene, and TMSOTf catalyst. Two mechanistic pathways are considered: pathway A, based on a previous model, and pathway B, which involves formation of a Si–O bond. For all stationary points (reactant complexes, intermediates, transition states) along both pathways, optimize geometries and compute harmonic frequencies to obtain electronic energies, zero-point vibrational energies, and thermal corrections to enthalpy and free energy at 298.15 K. Use the separate-ion limit TMS+ + TfO− as the reference state. For pathway B, locate the syn and anti transition states of the cycloaddition step. From the computed free energies, use the Eyring equation (rate ∝ exp(-ΔG‡/RT)) to derive the predicted syn:anti product ratio. Compare the overall barriers of pathways A and B to determine which is energetically preferred.

## Reproduction target
Recompute the activation enthalpy difference (ΔΔH‡) and activation free energy difference (ΔΔG‡) between the syn and anti transition states of the favored pathway. Use the free-energy difference in the Eyring equation to predict the syn:anti product ratio at room temperature. Determine whether pathway A or pathway B has the lower overall activation barrier.

## Assets

- Supporting Information (molecular coordinates and method details): http://dx.doi.org/10.1002/ejoc.201100206
- Open-source DFT code supporting B3LYP/TZV (e.g., ORCA, NWChem): https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: DFT geometry optimization and frequency analysis
- Role: process
- Action: Perform DFT calculations at the B3LYP/TZV level of theory for all relevant species in mechanistic pathways A and B (hydrazone isomers, TMSOTf catalyst, reactant complexes, intermediates, syn and anti transition states of the cycloaddition step). Optimize geometries, compute harmonic frequencies, and obtain electronic energies, zero-point vibrational energies, thermal corrections to enthalpy and free energy at 298.15 K. Use the charged reference state TMS+ + TfO− as the separated-ion limit.
- Evidence: `/app/outputs/stationary_point_energies.json`

### Step 2: Reaction energetics and diastereoselectivity prediction
- Role: scored (load-bearing)
- Action: From the computed energies in stationary_point_energies.json, determine the relative stabilities of intermediates and transition states. For pathway B, calculate activation enthalpy (ΔH‡) and activation free energy (ΔG‡) for the syn and anti transition states relative to the separated reactants. Compute ΔΔH‡_syn-anti = ΔH‡(syn) - ΔH‡(anti) and ΔΔG‡_syn-anti = ΔG‡(syn) - ΔG‡(anti). Use the Eyring equation (rate ∝ exp(-ΔG‡/RT)) to predict the syn:anti product ratio from the free-energy difference. Determine whether pathway A or pathway B has the lower overall barrier. Write the results as computed_data.json.
- Output file: `/app/outputs/computed_data.json`
- Format: json
- Contract: { 'pathway_A_relative_energy': float, 'pathway_B_relative_energy': 0.0, 'syn_TS_barrier_H': float, 'anti_TS_barrier_H': float, 'syn_TS_barrier_G': float, 'anti_TS_barrier_G': float, 'DeltaDeltaH_dagger': float, 'DeltaDeltaG_dagger': float, 'predicted_ratio_from_H': string (e.g., '84:16'), 'predicted_ratio_from_G': string, 'pathway_preference': string ('B_favored' or 'A_favored') }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_data.json
- path: `/app/outputs/computed_data.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Headline DFT-computed activation energy differences, predicted diastereomeric ratio, and pathway preference.
- schema:
  - `type`: object
  - `required`: `pathway_A_relative_energy`, `pathway_B_relative_energy`, `syn_TS_barrier_H`, `anti_TS_barrier_H`, `syn_TS_barrier_G`, `anti_TS_barrier_G`, `DeltaDeltaH_dagger`, `DeltaDeltaG_dagger`, `predicted_ratio_from_H`, `predicted_ratio_from_G`, `pathway_preference`
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The agent must first complete the DFT optimization (process step) to generate the raw energies, then derive the scored quantities. The hidden checker will compare ΔΔH‡ and ΔΔG‡ to the paper’s reported values within a tolerance, verify the pathway preference is 'B_favored', and check the predicted ratio from free energies against the paper’s ratio.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "pathway_A_relative_energy",
          "pathway_B_relative_energy",
          "syn_TS_barrier_H",
          "anti_TS_barrier_H",
          "syn_TS_barrier_G",
          "anti_TS_barrier_G",
          "DeltaDeltaH_dagger",
          "DeltaDeltaG_dagger",
          "predicted_ratio_from_H",
          "predicted_ratio_from_G",
          "pathway_preference"
        ],
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Headline DFT-computed activation energy differences, predicted diastereomeric ratio, and pathway preference."
    }
  ],
  "notes": "The agent must first complete the DFT optimization (process step) to generate the raw energies, then derive the scored quantities. The hidden checker will compare ΔΔH‡ and ΔΔG‡ to the paper’s reported values within a tolerance, verify the pathway preference is 'B_favored', and check the predicted ratio from free energies against the paper’s ratio."
}
```

## How you are scored
A hidden verifier checks your submitted /app/outputs/computed_data.json. It compares your computed values for ΔΔH‡ and ΔΔG‡, the predicted syn:anti ratio, and the pathway preference against reference values. Each of the scored quantities contributes a portion of the final reward. The verifier also checks that the submitted file conforms to the required schema and that all fields are present and of the correct type. The reward is a float between 0 and 1; a higher reward indicates better agreement.
