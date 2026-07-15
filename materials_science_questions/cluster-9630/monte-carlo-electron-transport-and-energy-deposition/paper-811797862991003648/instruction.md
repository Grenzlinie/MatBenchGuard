# Monte Carlo simulation of helium ion beam induced deposition in reaction-rate-limited and mass-transport-limited regimes

## Problem background
Focused helium ion beam induced deposition (He+ IBID) uses a high-brightness He+ beam to locally decompose a precursor gas, enabling direct-write nanofabrication. This work develops a three-dimensional Monte Carlo simulation (EnvisION) that couples helium ion trajectories, secondary electron generation and transport, and precursor gas surface kinetics to predict deposit morphology and growth. Two growth regimes are investigated: a reaction-rate-limited (RRL) regime where the precursor flux is much larger than the ion flux, and a mass-transport-limited (MTL) regime where the ion flux dominates. The simulation tracks the different species responsible for deposition and yields the final deposition efficiency (atoms deposited per incident ion) and the nanopillar width. Understanding and reproducing these regime-dependent trends provides insight into the underlying beam–solid–gas interactions.

## Approach
The core of the reproduction is a single-scattering Monte Carlo simulation for 25 keV He+ ions impinging on a tungsten substrate. Ion trajectories are propagated with solid–vacuum boundary crossing; at each scattering step electronic and nuclear energy losses are computed. Secondary electrons are generated from the electronic stopping power using a scaling energy ε=78 eV, are assigned random trajectories, and their escape probability depends on the total path length to the surface and an inelastic mean free path of 2.9 nm derived from the TPP-2M model. Electrons are classified as SE-I (generated within the first five ion scattering events) and SE-II (later events). The precursor gas handling follows a Langmuir isotherm with zero surface diffusion and a long residence time, and a provisional ion-induced dissociation cross-section 10× that for electrons is used. The simulation is run for two contrasting parameter sets from Table 1 of the paper: (A) reaction-rate-limited – 9 fA beam current, 7 Torr localised pressure, 1 million primary ions; (B) mass-transport-limited – 9 pA, 7 mTorr, 30 million primary ions. From the final deposit shape, the deposition efficiency and the pillar width (FWHM) are extracted.

## Reproduction target
Implement the EnvisION Monte Carlo simulation as described. Run the two simulation scenarios defined in the workflow steps: (1) the reaction-rate-limited (RRL) parameter set, and (2) the mass-transport-limited (MTL) parameter set. For each scenario, compute and report in a CSV file the final deposition efficiency (as a percentage of atoms deposited per incident He+ ion) and the nanopillar width (in nm, full width at half maximum). The two resulting CSV files will be compared to verify the relative ordering of the deposition efficiency and width between the two regimes. No exact numeric match against pre-specified values is required; the scoring is based on the correct directional trend.

## Assets
No external datasets, pre-trained models, or proprietary software are required. The simulation algorithm and all the necessary physical models (Bethe stopping, TPP-2M inelastic mean free path, angular escape probability, Langmuir gas kinetics, etc.) are described in this document and rely on established public physics. You must implement the Monte Carlo code from scratch; no pre-existing code base or package download is needed. Standard numerical libraries (e.g., Python scientific stack or C++ math libraries) are sufficient.

## Workflow steps

### Step 1: Reaction-rate-limited (RRL) IBID simulation
- Role: scored
- Action: Run the EnvisION Monte Carlo simulation with reaction-rate-limited parameters: beam energy 25 keV, beam current 9 fA, beam radius 1.5 nm Gaussian-like, localized precursor pressure 7 Torr, number of primary ions 1,000,000, ε=78 eV, secondary-electron model with TPP-2M based inelastic mean free path of 2.9 nm, angular escape probability with SE-I/SE-II classification after the 5th scattering, and Langmuir gas kinetics with zero surface diffusion and long residence time. Compute the final deposition efficiency (atoms deposited per incident ion, as a percentage) and the nanopillar width (nm, FWHM). Output the results in a CSV file.
- Output file: `/app/outputs/results_rrl.csv`
- Format: csv
- Contract: columns: regime (string, value "RRL"), deposition_efficiency (float, percent), width_nm (float)
- Scoring: scored by hidden verifier

### Step 2: Mass-transport-limited (MTL) IBID simulation
- Role: scored
- Action: Run the EnvisION Monte Carlo simulation with mass-transport-limited parameters: beam energy 25 keV, beam current 9 pA, beam radius 1.5 nm Gaussian-like, localized precursor pressure 7 mTorr, number of primary ions 30,000,000, ε=78 eV, secondary-electron model with TPP-2M based inelastic mean free path of 2.9 nm, angular escape probability with SE-I/SE-II classification after the 5th scattering, and Langmuir gas kinetics with zero surface diffusion and long residence time. Compute the final deposition efficiency (atoms deposited per incident ion, as a percentage) and the nanopillar width (nm, FWHM). Output the results in a CSV file.
- Output file: `/app/outputs/results_mtl.csv`
- Format: csv
- Contract: columns: regime (string, value "MTL"), deposition_efficiency (float, percent), width_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_rrl.csv`
- `/app/outputs/results_mtl.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_rrl.csv
- path: `/app/outputs/results_rrl.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated deposition efficiency and nanopillar width for the reaction-rate-limited regime.
- schema:
  - `type`: table
  - `required_columns`: `regime`, `deposition_efficiency`, `width_nm`
  - `units`:
    - `deposition_efficiency`: percent
    - `width_nm`: nm

### results_mtl.csv
- path: `/app/outputs/results_mtl.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated deposition efficiency and nanopillar width for the mass-transport-limited regime.
- schema:
  - `type`: table
  - `required_columns`: `regime`, `deposition_efficiency`, `width_nm`
  - `units`:
    - `deposition_efficiency`: percent
    - `width_nm`: nm

Notes: The checker compares the two output files to verify that deposition_efficiency(RRL) > deposition_efficiency(MTL) and width_nm(RRL) < width_nm(MTL). No exact numeric match is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_rrl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "regime",
          "deposition_efficiency",
          "width_nm"
        ],
        "units": {
          "deposition_efficiency": "percent",
          "width_nm": "nm"
        }
      },
      "description": "Simulated deposition efficiency and nanopillar width for the reaction-rate-limited regime."
    },
    {
      "file": "results_mtl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "regime",
          "deposition_efficiency",
          "width_nm"
        ],
        "units": {
          "deposition_efficiency": "percent",
          "width_nm": "nm"
        }
      },
      "description": "Simulated deposition efficiency and nanopillar width for the mass-transport-limited regime."
    }
  ],
  "notes": "The checker compares the two output files to verify that deposition_efficiency(RRL) > deposition_efficiency(MTL) and width_nm(RRL) < width_nm(MTL). No exact numeric match is required."
}
```

## How you are scored
A hidden verifier independently evaluates your output. It reads the two CSV files (`results_rrl.csv` and `results_mtl.csv`) and checks that the deposition efficiency and nanopillar width follow the expected relative ordering between the RRL and MTL regimes. The check is structural/tendency-based, not a comparison against a fixed numeric target; run-to-run stochastic spread is absorbed. Both regime outputs carry equal weight, and you earn full credit if both directional trends are correct. Submitting the correct number without having genuinely run the simulation is not sufficient – the verifier may also inspect supporting evidence, but the primary score comes from the correctness of the trends in the submitted CSV files.
