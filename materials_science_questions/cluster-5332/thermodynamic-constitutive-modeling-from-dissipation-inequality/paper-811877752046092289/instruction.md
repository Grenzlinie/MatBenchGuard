# Compute thermodynamic quantities for a two-beam elasto-plastic composite using closed-form expressions

## Problem background
In heterogeneous rate‑independent systems such as composites with elastic and elasto‑plastic constituents, the partition of input work into stored and dissipated energy is critical for predicting self‑heating and thermo‑mechanical response. The classical Taylor–Quinney coefficient is frequently assumed constant and near unity, but micromechanical considerations indicate that it may depend on microstructural detail and loading history. A combined micromechanical–thermodynamic framework can yield closed‑form expressions for the stored energy, free energy, dissipation, and both the differential and integral Taylor–Quinney coefficients. Applied to a simple one‑dimensional two‑beam elasto‑plastic composite, these relations allow the thermodynamic quantities to be evaluated as functions of the inelastic strain. This task reproduces that analytic evaluation so that the behaviour of the coefficients can be quantified.

## Approach
The closed‑form thermodynamic relations that follow from the micromechanical–thermodynamic framework are implemented directly. The composite consists of two perfectly bonded beams of length ℓ and equal cross‑section ℓ²; the lower beam remains linear elastic (modulus K1) while the upper beam is elastic‑perfectly plastic (modulus K2, yield stress σ_y2). The overall response is described by an effective modulus K_eq = (K1+K2)/2. From the equilibrium and constitutive laws, the applied stress Σ, total strain E, and inelastic strain E^i are linked. The stored energy W^i, total free energy Ψ, dissipation rate D (with inelastic strain rate Ė^i = 1 s⁻¹), differential Taylor–Quinney coefficient β^d, and integral coefficient β^int are then expressed as explicit, algebraic functions of E^i and the material parameters. The reproduction consists in evaluating these expressions at a prescribed set of E^i values and recording the results.

## Reproduction target
Using the parameters K1 = 1 GPa, K2 = 5 GPa, σ_y2 = 30 MPa, ℓ = 1 m, and the resulting V = 2 m³ and K_eq = (K1+K2)/2, evaluate the closed‑form expressions at each inelastic strain value E^i from a list that is linearly spaced from 0 to 0.1 in 20 equal steps. Compute the following quantities:
- Stored energy W^i (J)
- Total free energy Ψ (J)
- Dissipation rate D (W, assuming Ė^i = 1 s⁻¹)
- Differential Taylor–Quinney coefficient β^d
- Integral Taylor–Quinney coefficient β^int
Write the results to a CSV file with columns E_i, W_i, Psi, D, beta_d, beta_int. The file must contain exactly one header row and 20 data rows, in order of increasing E^i.

## Assets

- Python 3 standard library (or with numpy)

## Workflow steps

### Step 1: Analytic evaluation of elasto-plastic two-beam composite
- Role: scored (load-bearing)
- Action: Implement the closed-form thermodynamic expressions for the one-dimensional two-beam elasto-plastic composite. Set parameters: K1 = 1e9 Pa, K2 = 5e9 Pa, σ_y2 = 30e6 Pa, ℓ = 1 m, V = 2 m³, K_eq = (K1+K2)/2. For inelastic strain values E^i linearly spaced in [0, 0.1] (20 steps), compute the stored energy W^i = 0.5 * V * (K1/K2) * K_eq * (E^i)²; the total free energy Ψ = 0.5*V*K_eq*(E - E^i)² + W^i, where the total strain E is obtained from the constitutive law Σ = (K_eq/K2)*(σ_y2 + K1*E^i) and E = Σ/K_eq + E^i; the dissipation rate D = V * (K_eq/K2) * σ_y2 * Ė^i with Ė^i = 1 s⁻¹; the differential Taylor–Quinney coefficient β^d = 1 / (1 + (K1/σ_y2) * E^i); and the integral coefficient β^int = 1 / (1 + (K1/(2*σ_y2)) * E^i). Write the results to a CSV file.
- Output file: `/app/outputs/step_01_energetics.csv`
- Format: csv
- Contract: Columns: E_i (float, dimensionless inelastic strain), W_i (float, stored energy in joules), Psi (float, free energy in joules), D (float, dissipation rate in watts, assuming Ė^i=1 s⁻¹), beta_d (float, differential Taylor–Quinney coefficient), beta_int (float, integral Taylor–Quinney coefficient). The CSV file must contain exactly 21 rows (1 header + 20 data rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energetics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energetics.csv
- path: `/app/outputs/step_01_energetics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic quantities for the two-beam elasto-plastic composite. The checker recomputes the same closed-form expressions using the identical parameter set and E^i list, then compares each numeric field against the agent's submission with appropriate relative/absolute tolerances.
- schema:
  - `type`: table
  - `required_columns`: `E_i`, `W_i`, `Psi`, `D`, `beta_d`, `beta_int`
  - `units`:
    - `E_i`: 1
    - `W_i`: J
    - `Psi`: J
    - `D`: W
    - `beta_d`: 1
    - `beta_int`: 1
  - `description`: Each row corresponds to one inelastic strain value; all values are floats.

Notes: The CSV must use exactly the column order and names listed. E^i values must be linearly spaced from 0.0 to 0.1 in 20 steps (i.e., 0.0, 0.005263..., ..., 0.1).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energetics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_i",
          "W_i",
          "Psi",
          "D",
          "beta_d",
          "beta_int"
        ],
        "units": {
          "E_i": "1",
          "W_i": "J",
          "Psi": "J",
          "D": "W",
          "beta_d": "1",
          "beta_int": "1"
        },
        "description": "Each row corresponds to one inelastic strain value; all values are floats."
      },
      "description": "Computed thermodynamic quantities for the two-beam elasto-plastic composite. The checker recomputes the same closed-form expressions using the identical parameter set and E^i list, then compares each numeric field against the agent's submission with appropriate relative/absolute tolerances."
    }
  ],
  "notes": "The CSV must use exactly the column order and names listed. E^i values must be linearly spaced from 0.0 to 0.1 in 20 steps (i.e., 0.0, 0.005263..., ..., 0.1)."
}
```

## How you are scored
A hidden verifier independently recomputes the same closed‑form expressions using the identical parameter set and E^i list. Each numeric column of the submitted CSV is compared to this independently computed reference.
- For W_i, Psi, and D the check uses a relative tolerance of 1e-4.
- For beta_d and beta_int the check uses an absolute tolerance of 1e-4.
The final reward is 1.0 if all 20 data rows satisfy the tolerances, and 0.0 otherwise. Therefore, the correct outputs can only be obtained by faithfully implementing the thermodynamic relations; simply copying a pre‑existing value will not pass the tolerance checks.
