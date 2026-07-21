# Extract Long-Range Exchange Parameters in an Ising Antiferromagnet Using Mean-Field ANNNI Model

## Problem background
NdCo2Si2 is a tetragonal Ising-like antiferromagnet that exhibits a sequence of metamagnetic transitions at low temperatures. Its magnetic structure along the c-axis can be modeled by an extended axial next-nearest-neighbor Ising (ANNNI) Hamiltonian, where the long-range interlayer exchange parameters J1, J2, J3 and the intralayer coupling J0 govern the observed magnetic phases. Using a mean-field approximation, these exchange parameters can be extracted from experimentally measured critical fields and the Néel temperature. This task computes those exchange parameters and their linear pressure derivatives.

## Approach
Within a mean-field treatment of the ANNNI model, the magnetic energies of the four observed phases (phases I, II, III and the forced-ferromagnetic state) are expressed in terms of the exchange parameters J1, J2, J3 and the applied magnetic field. By equating the energies of adjacent phases at the three critical fields B_C1, B_C2, B_C3, one obtains linear relations that directly give J1, J2, J3 in terms of those fields, the Landé g-factor g, the Bohr magneton μ_B, and the spin S. The intralayer coupling J0 is then determined from the Néel temperature T_N using the Fourier transform of the exchange interaction J(q) evaluated at the ordering wave vector Q, together with the mean-field relation connecting T_N to J(Q). To obtain the pressure derivatives, the formulas for J1, J2, J3, J0 are differentiated with respect to pressure, treating g, μ_B, and S as constants and using the published linear pressure slopes of the critical fields and T_N. The logarithmic derivatives d ln J_i / dP are computed from the resulting dJ_i/dP.

## Reproduction target
Compute the ambient-pressure exchange parameters J0/k_B, J1/k_B, J2/k_B, J3/k_B (in Kelvin) and their logarithmic pressure derivatives d ln J0/dP, d ln J1/dP, d ln J2/dP, d ln J3/dP (in %/GPa) using the provided experimental inputs: B_C1 = 3.27 T, B_C2 = 5.35 T, B_C3 = 13.44 T, T_N = 31.9 K, ordering wave vector Q = 11/14 c*, g-factor g = 6.1, spin S = 1/2, and the linear pressure derivatives d B_C1/dP = 0.935 T/GPa, d B_C2/dP = 1.027 T/GPa, d B_C3/dP = 0.60 T/GPa, d T_N/dP = 0.94 K/GPa, along with the physical constants Bohr magneton μ_B and Boltzmann constant k_B.

## Assets

- Bohr magneton
- Boltzmann constant

## Workflow steps

### Step 1: Compute ambient-pressure exchange parameters
- Role: scored
- Action: Using the published experimental inputs (B_C1=3.27 T, B_C2=5.35 T, B_C3=13.44 T, T_N=31.9 K, ordering wave vector Q=11/14 c*, g-factor g=6.1, spin S=1/2) and the physical constants Bohr magneton μ_B and Boltzmann constant k_B, compute the interplane exchange parameters J1, J2, J3 from the mean-field equations derived by equating the magnetic energies at the critical fields:
J1 = (1/168)*(-31 B_C1 + 22 B_C2 - 33 B_C3) * g μ_B / S
J2 = (1/336)*( 67 B_C1 - 34 B_C2 - 33 B_C3) * g μ_B / S
J3 = (1/6)*( B_C1 - B_C2) * g μ_B / S
Then compute the in-plane coupling J0 from the Néel temperature T_N using the Fourier transform of the exchange interaction J(q) = J0 + 2 J1 cos(π q) + 2 J2 cos(2π q) + 2 J3 cos(3π q) evaluated at q=Q, and the mean-field relation T_N = (2/3) J(Q) S(S+1). Express all exchange parameters as J_i/k_B in Kelvin (use k_B to convert energy units). Write the results to ambient_J_values.json.
- Output file: `/app/outputs/ambient_J_values.json`
- Format: json
- Contract: JSON object with keys J0_kB, J1_kB, J2_kB, J3_kB (each a floating-point number, units K)
- Scoring: scored by hidden verifier

### Step 2: Compute pressure derivatives of exchange parameters
- Role: scored (load-bearing)
- Action: Using the ambient exchange parameters from step 1 and the published linear pressure dependencies (d B_C1/dP = 0.935 T/GPa, d B_C2/dP = 1.027 T/GPa, d B_C3/dP = 0.60 T/GPa, d T_N/dP = 0.94 K/GPa), compute the logarithmic pressure derivatives d ln J_i / d P (in %/GPa) for i=0,1,2,3. First differentiate the formulas for J1, J2, J3, and J0 with respect to pressure P, treating g, μ_B, and S as constants and using the given d B_Ci/dP and d T_N/dP. Then compute d ln J_i / d P = (d J_i / d P) / J_i, multiplied by 100 to express as percent per GPa. Write the results to pressure_derivatives.json.
- Output file: `/app/outputs/pressure_derivatives.json`
- Format: json
- Contract: JSON object with keys dlnJ0_dP, dlnJ1_dP, dlnJ2_dP, dlnJ3_dP (each a floating-point number, units %/GPa)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ambient_J_values.json`
- `/app/outputs/pressure_derivatives.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ambient_J_values.json
- path: `/app/outputs/ambient_J_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ambient-pressure exchange parameters J0/kB, J1/kB, J2/kB, J3/kB in Kelvin, computed from the given critical fields and Néel temperature using the mean-field ANNNI model.
- schema:
  - `type`: object
  - `required`: `J0_kB`, `J1_kB`, `J2_kB`, `J3_kB`
  - `properties`:
    - `J0_kB`:
      - `type`: number
      - `unit`: K
    - `J1_kB`:
      - `type`: number
      - `unit`: K
    - `J2_kB`:
      - `type`: number
      - `unit`: K
    - `J3_kB`:
      - `type`: number
      - `unit`: K

### pressure_derivatives.json
- path: `/app/outputs/pressure_derivatives.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Logarithmic pressure derivatives of J0, J1, J2, J3 in %/GPa, computed by differentiating the exchange formulas with respect to pressure.
- schema:
  - `type`: object
  - `required`: `dlnJ0_dP`, `dlnJ1_dP`, `dlnJ2_dP`, `dlnJ3_dP`
  - `properties`:
    - `dlnJ0_dP`:
      - `type`: number
      - `unit`: %/GPa
    - `dlnJ1_dP`:
      - `type`: number
      - `unit`: %/GPa
    - `dlnJ2_dP`:
      - `type`: number
      - `unit`: %/GPa
    - `dlnJ3_dP`:
      - `type`: number
      - `unit`: %/GPa

Notes: All inputs are provided in the instructions. Physical constants should use standard CODATA2018 values. The computation is deterministic and simple; results can be recomputed independently.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ambient_J_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "J0_kB",
          "J1_kB",
          "J2_kB",
          "J3_kB"
        ],
        "properties": {
          "J0_kB": {
            "type": "number",
            "unit": "K"
          },
          "J1_kB": {
            "type": "number",
            "unit": "K"
          },
          "J2_kB": {
            "type": "number",
            "unit": "K"
          },
          "J3_kB": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Ambient-pressure exchange parameters J0/kB, J1/kB, J2/kB, J3/kB in Kelvin, computed from the given critical fields and Néel temperature using the mean-field ANNNI model."
    },
    {
      "file": "pressure_derivatives.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "dlnJ0_dP",
          "dlnJ1_dP",
          "dlnJ2_dP",
          "dlnJ3_dP"
        ],
        "properties": {
          "dlnJ0_dP": {
            "type": "number",
            "unit": "%/GPa"
          },
          "dlnJ1_dP": {
            "type": "number",
            "unit": "%/GPa"
          },
          "dlnJ2_dP": {
            "type": "number",
            "unit": "%/GPa"
          },
          "dlnJ3_dP": {
            "type": "number",
            "unit": "%/GPa"
          }
        }
      },
      "description": "Logarithmic pressure derivatives of J0, J1, J2, J3 in %/GPa, computed by differentiating the exchange formulas with respect to pressure."
    }
  ],
  "notes": "All inputs are provided in the instructions. Physical constants should use standard CODATA2018 values. The computation is deterministic and simple; results can be recomputed independently."
}
```

## How you are scored
A hidden verifier independently recomputes the ambient exchange parameters from the same algebraic formulas and inputs using high-precision arithmetic, then compares your submitted values to the reference values within a pre-defined tolerance. The pressure derivatives are recomputed analytically and likewise compared. Both output files (ambient_J_values.json and pressure_derivatives.json) contribute to the final reward, which is a weighted combination of the per-stage scores. You must actually carry out the derivation and computation; merely recalling or reporting the expected numbers is not sufficient.
