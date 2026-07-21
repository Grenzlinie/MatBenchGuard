# Mean-Field Model of Transverse Internal Rearrangement in UO2

## Problem background
Uranium dioxide (UO2) undergoes a first-order antiferromagnetic transition accompanied by an unusual lattice distortion in which oxygen planes slide relative to one another—a transverse internal rearrangement (TIR)—without macroscopic strain. Competing distortions include the homogeneous Allen internal distortion and longitudinal internal rearrangements. The selection of the TIR over other modes is thought to be governed by a trade-off between crystal-field energy lowering and elastic energy cost. The goal of this task is to compute the effective elastic constants for the TIR and Allen modes within a rigid-ion model, and to solve the self-consistent mean-field equations for the TIR mode to obtain the temperature-dependent oxygen displacement and magnetic moment. The outcome demonstrates which mode is favored and predicts the magnitude of the low-temperature distortion.

## Approach
The physical model treats the U4+ 5f2 ions as having a Γ5 cubic crystal-field ground-state triplet, an effective angular momentum J=4, and a Landé g-factor g=0.8. The crystal-field distortion terms are described in a point-charge picture using operator equivalents, with an effective charge parameter that controls the coupling between the distortion amplitude and the electronic degrees of freedom. Magnetic exchange is treated in the molecular-field approximation with a coupling λ. The elastic energy of each candidate distortional mode is computed from a rigid-ion model that sums Coulomb (Ewald) and short-range repulsive contributions, parameterized by cation charge Zc, lattice constant a, and repulsive parameters A1,B1,A2,B2,A3,B3 given in units of e²/(2v). The effective Hamiltonian for the TIR mode reduces to a quadrupolar term and a magnetic term, and the equilibrium distortion is obtained from a self-consistency condition linking the displacement to the thermal expectation of a quadrupole operator. The resulting system is solved by diagonalizing the Hamiltonian in the Γ5 basis and iterating until convergence at each temperature.

## Reproduction target
1. Implement the elastic energy expressions for the TIR and Allen modes using the rigid-ion parameters listed in Step 1. Compute the effective elastic constants κ_TIR and κ_Allen in units K/a². Write the results to elastic_constants.csv with columns 'mode' and 'kappa_K'. Verify that one mode is elastically softer than the other.
2. Using the κ value for the TIR from Step 1, together with magnetic exchange λ=7.04 K and quadrupolar coupling ratio Q/λ=0.033, solve the self-consistent mean-field equations for the TIR mode over a temperature range from 0 K to at least 35 K. Produce tir_phase_results.csv with columns 'T_K', 'delta_over_a' (oxygen relative displacement per lattice constant), and 'Jz_avg' (expectation of Jz). The T=0 value of delta_over_a is the key scored quantity.
3. The artifacts are CSV files placed in /app/outputs/.

## Assets
All necessary numerical parameters (rigid-ion repulsive coefficients, cation charge, lattice constant, exchange constant, quadrupolar coupling ratio) are provided in the workflow steps. No external datasets, models, or pre-trained files need to be fetched. The implementation can be completed using standard Python libraries (numpy, scipy, etc.). No additional downloads beyond package installation are required.

## Workflow steps

### Step 1: Compute elastic constants for TIR and Allen modes
- Role: scored
- Action: Implement the elastic energy expressions for the transverse internal rearrangement (TIR) and Allen distortional modes in the rigid-ion model. The model combines Coulomb (Ewald summation) and short-range repulsive contributions. Use the parameters from column 5 of Table II: A1=21.0, B1=3.9, A2=8.8, B2=-1.1, A3=13.5, B3=-3.8, cation charge Zc=2.142 (in units of e^2/(2v)), and lattice constant a=5.470 Å. The effective elastic constant κ (in units K/a^2) for the Allen mode is given by the sum of repulsive terms (no Coulomb contribution) and for the TIR mode by the sum of Coulomb and repulsive terms, with careful sign handling for the TIR Coulomb term. Compute both κ_TIR and κ_Allen. Write the results to /app/outputs/elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: Two columns: 'mode' (string, values 'TIR' or 'Allen'), 'kappa_K' (float, elastic constant in units of K).
- Scoring: scored by hidden verifier

### Step 2: Solve self-consistent TIR equations for oxygen displacement and magnetization
- Role: scored (load-bearing)
- Action: Implement the mean-field Hamiltonian for the TIR mode within the Γ5 cubic crystal-field ground-state triplet (effective J=4, g=0.8). Use the parameters: magnetic exchange λ=7.04 K, quadrupolar coupling ratio Q/λ=0.033, and the TIR elastic constant κ from the previous step. The effective Hamiltonian contains a quadrupolar term (-Q⟨O2^0-O2^2⟩(O2^0-O2^2)) and a magnetic exchange term (-λ⟨Jz⟩Jz), plus constant terms. Solve self-consistently for the thermal averages ⟨O2^0-O2^2⟩ and ⟨Jz⟩ at each temperature by diagonalizing the Hamiltonian in the Γ5 basis. The oxygen relative shift δ/a is obtained from the equilibrium condition δ = -(Cρ)/(2κ)⟨O2^0-O2^2⟩, where Cρ = √(2κQ). Iterate until convergence at each temperature from T=0 K to at least 35 K, capturing the first-order transition. Output a CSV with temperature T_K, δ_over_a, and Jz_avg. Include T=0 as the first row. Write the results to /app/outputs/tir_phase_results.csv.
- Output file: `/app/outputs/tir_phase_results.csv`
- Format: csv
- Contract: Three columns: 'T_K' (float, temperature in K), 'delta_over_a' (float, dimensionless oxygen relative shift), 'Jz_avg' (float, dimensionless average angular momentum).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/tir_phase_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective elastic constants for TIR and Allen modes, computed from rigid-ion parameters. The checker compares values against paper-reported results within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `kappa_K`
  - `units`:
    - `kappa_K`: K

### tir_phase_results.csv
- path: `/app/outputs/tir_phase_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature-dependent oxygen relative shift and magnetization for the TIR mode. The checker extracts the T=0 value of delta_over_a and compares to the target within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `delta_over_a`, `Jz_avg`
  - `units`:
    - `T_K`: K
    - `delta_over_a`: dimensionless
    - `Jz_avg`: dimensionless

Notes: The solver must compute elastic constants from the given analytical expressions and parameters, then use those constants in the self-consistent solver. The hidden gold values are derived from the paper's reported results for the specific parameter set (column 5 of Table II).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "kappa_K"
        ],
        "units": {
          "kappa_K": "K"
        }
      },
      "description": "Effective elastic constants for TIR and Allen modes, computed from rigid-ion parameters. The checker compares values against paper-reported results within a tolerance."
    },
    {
      "file": "tir_phase_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "delta_over_a",
          "Jz_avg"
        ],
        "units": {
          "T_K": "K",
          "delta_over_a": "dimensionless",
          "Jz_avg": "dimensionless"
        }
      },
      "description": "Temperature-dependent oxygen relative shift and magnetization for the TIR mode. The checker extracts the T=0 value of delta_over_a and compares to the target within tolerance."
    }
  ],
  "notes": "The solver must compute elastic constants from the given analytical expressions and parameters, then use those constants in the self-consistent solver. The hidden gold values are derived from the paper's reported results for the specific parameter set (column 5 of Table II)."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. For elastic_constants.csv, the verifier checks that κ_TIR and κ_Allen are correctly computed and that the TIR mode is elastically softer than the Allen mode. For tir_phase_results.csv, the verifier compares the T=0 value of delta_over_a against a hidden reference value derived from the original work, within an appropriate tolerance that allows for numerical differences from a reimplementation. Additional checks may examine the presence of a first-order transition signature in the temperature scan. The final reward is a weighted combination of these checks — merely writing the paper's numbers without performing the correct computation will not earn full credit. The exact thresholds and reference values remain hidden.
