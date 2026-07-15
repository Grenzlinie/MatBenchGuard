# DFT+NRG Kondo Temperature and Conductance Prediction for Impurities on Carbon Nanotubes

## Problem background
This task addresses the Kondo effect arising from isolated magnetic transition-metal impurities (Co and Fe) adsorbed on metallic single-wall carbon nanotubes (SWNTs). In such systems, the spin of the impurity can be partially screened by the conduction electrons of the nanotube, leading to characteristic zero-bias anomalies in the electrical conductance and a low-energy Kondo scale characterized by the Kondo temperature T_K. Predicting these quantities requires a multi-step computational pipeline: first-principles density-functional theory (DFT) calculations to obtain the electronic structure and scattering phase shifts, extraction of a multi-orbital Anderson impurity model, and solution of that model via numerical renormalization group (NRG). The goal of this reproduction task is to compute the Kondo temperatures and zero-bias ballistic conductance ratios for three specific impurity–nanotube combinations: Co on a (4,4) SWNT, Co on an (8,8) SWNT, and Fe on an (8,8) SWNT.

## Approach
The workflow follows the DFT+Anderson+NRG route. First, spin-polarised DFT calculations (using Quantum-ESPRESSO with the GGA functional) are performed for the three impurity–SWNT systems; the atomic geometries are relaxed and the symmetry- and spin-resolved conduction-electron phase shifts at the Fermi energy are extracted together with the impurity projected density-of-states (PDOS) peak positions. Second, these DFT results are used to construct a multi-orbital Anderson Hamiltonian. For each magnetic orbital, the bare on-site energy, the Hubbard repulsion, and the hybridisation broadening are determined by solving the unrestricted Hartree–Fock self-consistency equations that reproduce the DFT phase shifts and the impurity DOS peak positions; Hund’s exchange coupling is likewise fixed from the DFT exchange splittings. Third, the Anderson model is solved with a standard numerical renormalization group (NRG) code (e.g., from the ALPS library). The Kondo temperature is extracted from the impurity Green function. Finally, the many-body phase shifts obtained from the NRG solution are used to compute the zero-bias ballistic conductance ratio G/G0 via the Landauer formula, summing contributions from the symmetric (s) and antisymmetric (a) conduction channels. No explicit knowledge of the source paper is required beyond these method-level instructions; all necessary physical quantities and formulas are defined in the context of the workflow steps.

## Reproduction target
Produce two JSON files under `/app/outputs`:
- `kondo_temperatures.json` : a JSON object with three keys, `Co_44`, `Co_88`, and `Fe_88`, each mapped to the computed Kondo temperature in Kelvin (numeric float).
- `zero_bias_conductances.json` : a JSON object with the same three keys, each mapped to the computed zero-bias conductance ratio G/G0 (dimensionless float).

These numbers must be obtained by executing the full DFT+Anderson+NRG pipeline as described in the workflow steps. Submitting values that have not been produced by that pipeline will not satisfy the verification criteria.

## Assets

- Quantum-ESPRESSO: https://www.quantum-espresso.org/
- NRG solver (e.g., ALPS NRG): https://alps.comp-phys.org/

## Workflow steps

### Step 1: DFT electronic structure and phase shift calculations
- Role: process
- Action: Perform spin-polarized DFT calculations for Co on (4,4) SWNT, Co on (8,8) SWNT, and Fe on (8,8) SWNT using Quantum-ESPRESSO with GGA functional. Relax atomic geometries. Compute symmetry- and spin-resolved conduction-electron phase shifts at the Fermi energy and the impurity projected density of states (PDOS) peak positions. Save the phase shifts and DOS data.
- Evidence: `/app/outputs/dft_results.json`

### Step 2: Extraction of Anderson model parameters
- Role: process
- Action: Using the DFT results (phase shifts, impurity DOS peak positions, exchange splittings) and the constant clean-tube density of states ρ ≈ 1/(12 eV), extract the multi-orbital Anderson Hamiltonian parameters (ε_d, U, Γ for each magnetic orbital; Hund J for Co and Fe) by solving the Hartree–Fock self-consistency equations that reproduce the DFT phase shifts and DOS peaks. Save the extracted parameters.
- Evidence: `/app/outputs/anderson_parameters.json`

### Step 3: NRG calculation of Kondo temperatures
- Role: scored (load-bearing)
- Action: Solve the multi-orbital Anderson Hamiltonian using numerical renormalization group (NRG) with the extracted parameters. Extract the Kondo temperature T_K from the impurity Green function. Write the T_K values (in Kelvin) for the three systems to kondo_temperatures.json.
- Output file: `/app/outputs/kondo_temperatures.json`
- Format: json
- Contract: {"Co_44": "float (K)", "Co_88": "float (K)", "Fe_88": "float (K)"}
- Scoring: scored by hidden verifier

### Step 4: Zero-bias conductance from NRG phase shifts
- Role: scored
- Action: From the NRG solution, extract the many-body phase shifts for the Kondo channels. Compute the zero-bias ballistic conductance ratio G/G0 using the Landauer formula summing over the s and a channels. Write the dimensionless ratios for Co on (4,4), Co on (8,8), and Fe on (8,8) to zero_bias_conductances.json.
- Output file: `/app/outputs/zero_bias_conductances.json`
- Format: json
- Contract: {"Co_44": "float (dimensionless)", "Co_88": "float (dimensionless)", "Fe_88": "float (dimensionless)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kondo_temperatures.json`
- `/app/outputs/zero_bias_conductances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kondo_temperatures.json
- path: `/app/outputs/kondo_temperatures.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted Kondo temperatures for the three impurity‑nanotube systems. Compared to hidden paper reference with appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `Co_44`: float (K)
    - `Co_88`: float (K)
    - `Fe_88`: float (K)

### zero_bias_conductances.json
- path: `/app/outputs/zero_bias_conductances.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted zero‑bias conductance ratios G/G0 for the three systems. Checker compares against hidden thresholds derived from the paper's expected Kondo channel behavior.
- schema:
  - `type`: object
  - `required`:
    - `Co_44`: float (dimensionless)
    - `Co_88`: float (dimensionless)
    - `Fe_88`: float (dimensionless)

Notes: DFT intermediate results and extracted Anderson parameters are not scored but must be produced as evidence of process execution. The load‑bearing Kondo temperature step guarantees the full pipeline is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kondo_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Co_44": "float (K)",
          "Co_88": "float (K)",
          "Fe_88": "float (K)"
        }
      },
      "description": "Predicted Kondo temperatures for the three impurity‑nanotube systems. Compared to hidden paper reference with appropriate tolerance."
    },
    {
      "file": "zero_bias_conductances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Co_44": "float (dimensionless)",
          "Co_88": "float (dimensionless)",
          "Fe_88": "float (dimensionless)"
        }
      },
      "description": "Predicted zero‑bias conductance ratios G/G0 for the three systems. Checker compares against hidden thresholds derived from the paper's expected Kondo channel behavior."
    }
  ],
  "notes": "DFT intermediate results and extracted Anderson parameters are not scored but must be produced as evidence of process execution. The load‑bearing Kondo temperature step guarantees the full pipeline is required."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. The verifier compares your submitted Kondo temperatures and conductance ratios against a hidden reference using a directional threshold policy: meeting or exceeding the expected physical behaviour earns full credit, and the score degrades only when the result deviates from it. The final reward is a weighted combination of the per-artifact scores. The verifier may also check that the intermediate evidence files (`dft_results.json`, `anderson_parameters.json`) are present and consistent with a genuine pipeline execution, but the main reward comes from the two scored JSON artifacts. You must run the pipeline; simply copying the correct target numbers is insufficient.
