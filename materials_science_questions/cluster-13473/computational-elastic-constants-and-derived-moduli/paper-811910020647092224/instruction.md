# Young's Modulus of Silicon Nanoplates from Semi-Continuum Keating Model

## Problem background
Silicon nanoplates exhibit mechanical properties that differ from bulk silicon because their high surface-to-volume ratio makes surface effects dominant at the nanoscale. One important property is Young's modulus along the [100] direction, which depends on the nanoplate thickness (number of atomic layers) and on the arrangement of atoms at the surfaces. In particular, (2×1) surface reconstruction changes the bonding at the surfaces and can alter the elasticity. Temperature also influences the modulus through thermal expansion and anharmonic softening of the atomic bonds. The goal of this task is to compute, analytically, how Young's modulus of a Si(001) nanoplate varies with thickness and temperature, for both unreconstructed and (2×1) reconstructed surfaces, using a semi-continuum Keating model.

## Approach
We use a semi-continuum approach that combines a continuum description of the in-plane directions (x,y) with a discrete atomistic model in the thickness direction (z). The strain energy of the silicon lattice is evaluated with the Keating valence-force model, which includes bond-stretching (force constant k_b) and bond-bending (k_θ) terms. For the ideal unreconstructed surface, the strain energy reduces to a simple expression, while for the (2×1) reconstructed surface we account for the dimer displacement δ that describes the in-plane shift of surface atoms. Finite-temperature effects enter in two ways: (i) the lattice parameter a(T) is taken from a quasiharmonic model, and (ii) the force constants are scaled anharmonically with bond length according to k_b ∝ r⁻⁴, k_θ ∝ r⁻⁷. The task is to implement the semi-continuum model to compute the temperature-dependent force constants and then the Young's modulus E for specified numbers of atomic layers N and temperatures T. All necessary numerical inputs (base force constants, a(T) table, δ, and the exact analytical formulas for Young's modulus) are provided below.

## Model constants and formulas

### Physical constants (from literature)
- Base bond-stretching force constant: \(k_b^0 = 6.187 \times 10^{20} \,\text{N/m}^3\)
- Base bond-bending force constant: \(k_\theta^0 = 1.813 \times 10^{20} \,\text{N/m}^3\)
- Zero-temperature lattice parameter (one quarter of conventional Si lattice constant): \(a_0 = 0.135775 \,\text{nm}\) (use \(a_0\) in meters when computing energies)
- Surface reconstruction dimer displacement: \(\delta = 0.05197 \,\text{nm}\) (use in meters)

### Temperature-dependent lattice parameter \(a(T)\)
From the quasiharmonic approximation, the silicon lattice parameter \(a\) [nm] at the required temperatures is:

| Temperature (K) | \(a\) (nm)   |
|----------------|-------------|
| 0              | 0.135775    |
| 100            | 0.135830    |
| 500            | 0.136200    |
| 1000           | 0.136800    |

### Anharmonic scaling of force constants
The force constants are scaled with bond length \(r\) (proportional to \(a\)) as described in the model:
\[
k_b(T) = k_b^0 \left(\frac{a_0}{a(T)}\right)^4, \qquad
k_\theta(T) = k_\theta^0 \left(\frac{a_0}{a(T)}\right)^7.
\]

### Young's modulus formulas from the semi-continuum Keating model
All lengths are in meters; the results are in Pa (convert to GPa for output).

**Unreconstructed surface** (Eq. (12) of the model):
\[
E_{\text{ur}}(N, a, k_b, k_\theta) = \frac{4 N a}{4 N + 1} \bigl(k_b + 1.5\,k_\theta\bigr).
\]

**Reconstructed (2×1) surface** (Eq. (16) of the model):
\[
\begin{aligned}
E_{\text{rc}}(N, a, k_b, k_\theta, \delta) = \frac{1}{(4 N + 1) a^3} \Bigg[
& 4 (N-1) a^4 \bigl(k_b + 1.5\,k_\theta\bigr) \\
& + k_b \left( 8 (a-\delta)^4 + \bigl((a+\delta)^2 - \tfrac{\delta^2}{2}\bigr)^2 + \bigl((a-\delta)^2 - \tfrac{\delta^2}{2}\bigr)^2 + 2 \bigl(a^2 + \tfrac{\delta^2}{2}\bigr)^2 \right) \\
& + 0.5\,k_\theta \left( \bigl(2 a^2 - \delta^2\bigr)^2 + 4 a^2 (a+\delta)^2 + 4 a^2 (a-\delta)^2 \right)
\Bigg].
\end{aligned}
\]

Use these formulas with the temperature-corrected force constants and lattice parameter to compute \(E\).

## Reproduction target
Produce a CSV file, `youngs_modulus_results.csv`, containing the Young's modulus values (in GPa) for the following combinations:

- For thickness layers N = 1, 2, 3, 4, 5, 10, 20, compute E for both the unreconstructed and the reconstructed surface, at temperature 0 K.
- For N = 5 with the reconstructed surface only, compute E at temperatures 0, 100, 500, and 1000 K.

The file must have exactly four columns in order: `N` (integer), `condition` (string `unreconstructed` or `reconstructed`), `temperature_K` (float), and `E_GPa` (float). Each computed value must be written as a separate row.

## Workflow steps

### Step 1: Compute temperature-dependent Keating force constants
- Role: process
- Action: Using the provided base force constants k_b^0=6.187e20 N/m³ and k_θ^0=1.813e20 N/m³, the temperature-dependent lattice parameter table a(T) above, and the anharmonic scaling laws, compute k_b(T) and k_θ(T) for the temperatures 0, 100, 500, 1000 K. The bond length r is derived from a(T). No separate output file is required for this step; the computed force constants are used as input to Step 2.
- Evidence: internal computation (no file output)

### Step 2: Compute Young's modulus of Si nanoplates
- Role: scored (load-bearing)
- Action: Using the Young's modulus formulas provided above (Eqs. (12) and (16)) with the temperature-dependent force constants from Step 1, the lattice parameter a(T), the surface reconstruction displacement δ=0.05197 nm, and the thickness N, compute the Young's modulus E for each required combination: N in {1,2,3,4,5,10,20} for both 'unreconstructed' and 'reconstructed' conditions at temperature 0 K, and N=5 'reconstructed' only at temperatures 0,100,500,1000 K. Write the results to youngs_modulus_results.csv with columns N, condition, temperature_K, E_GPa.
- Output file: `/app/outputs/youngs_modulus_results.csv`
- Format: csv
- Contract: Columns: N (int), condition (string: 'unreconstructed' or 'reconstructed'), temperature_K (float), E_GPa (float). Required rows: for N in {1,2,3,4,5,10,20}, both conditions at temperature_K=0; for N=5, reconstructed condition only, at temperature_K in {0,100,500,1000}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/youngs_modulus_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### youngs_modulus_results.csv
- path: `/app/outputs/youngs_modulus_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Young's modulus of Si(001) nanoplate for given thickness N, surface condition, and temperature, computed analytically from the semi-continuum Keating model.
- schema:
  - `type`: table
  - `required_columns`: `N`, `condition`, `temperature_K`, `E_GPa`
  - `units`:
    - `E_GPa`: GPa

Notes: The checker recomputes the expected E_GPa values using the same closed-form expressions and provided constants, comparing with tolerance ±0.001 GPa.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "youngs_modulus_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "condition",
          "temperature_K",
          "E_GPa"
        ],
        "units": {
          "E_GPa": "GPa"
        }
      },
      "description": "Young's modulus of Si(001) nanoplate for given thickness N, surface condition, and temperature, computed analytically from the semi-continuum Keating model."
    }
  ],
  "notes": "The checker recomputes the expected E_GPa values using the same closed-form expressions and provided constants, comparing with tolerance ±0.001 GPa."
}
```

## How you are scored
A hidden verifier independently recomputes the expected Young's modulus values using the same semi-continuum model and the constants provided in this instruction. It reads your `youngs_modulus_results.csv` and compares every entry to the recomputed gold values within an absolute tolerance of 0.001 GPa. Your score is based on how well your numbers match the physically correct results across all required thicknesses, conditions, and temperatures. Reporting an approximate or guessed value without running the model will not succeed. The final reward is a weighted combination of the scores for each required combination, with the majority of the weight on the scored step.