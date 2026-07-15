# Specific Heat of Spin-3/2 Blume-Capel Model via Effective-Field Formulations

## Problem background
The spin-3/2 Blume-Capel model is a generalization of the spin-1 Blume-Capel model to spin operators taking values ±3/2 and ±1/2. The Hamiltonian is
H = -J Σ S_i^z S_j^z - D Σ (S_i^z)^2,
with ferromagnetic exchange J, crystal-field D, and nearest-neighbor interactions on a lattice of coordination number z. On the honeycomb lattice (z=3) the ground-state configuration changes from |S^z| = 1/2 to |S^z| = 3/2 at the critical crystal-field value D/J = -z/2 = -1.5, leading to peculiar thermodynamic behavior. This work applies two effective-field formulations to compute the magnetization, quadrupolar moment, cubic moment, internal energy, and magnetic specific heat of the model, aiming to characterize the specific heat near the critical crystal field.

## Approach
Two formulations based on Ising spin identities and a differential-operator technique are employed.

Formulation A (exact): Use the exact van der Waerden identity for spin-3/2,
exp(a S_i^z) = A(a) + B(a) S_i^z + C(a) (S_i^z)^2 + D(a) (S_i^z)^3,
with
A(a) = 1/8[9 cosh(a/2) - cosh(3a/2)],
B(a) = 1/12[27 sinh(a/2) - sinh(3a/2)],
C(a) = 1/2[cosh(3a/2) - cosh(a/2)],
D(a) = 1/3[sinh(3a/2) - 3 sinh(a/2)].

The spin identity functions and the differential-operator technique yield coupled self-consistent equations for the magnetization m = ⟨S_i^z⟩, quadrupolar moment q = ⟨(S_i^z)^2⟩, and cubic moment r = ⟨(S_i^z)^3⟩:
m = [A(J∇) + B(J∇) m + C(J∇) q + D(J∇) r]^z f(x)|_{x=0},
q = [A(J∇) + B(J∇) m + C(J∇) q + D(J∇) r]^z g(x)|_{x=0},
r = [A(J∇) + B(J∇) m + C(J∇) q + D(J∇) r]^z h(x)|_{x=0},
where ∇ = ∂/∂x and the functions f, g, h are defined by
f(x) = (1/2) [3 sinh(3βx/2) + e^{-2Dβ} sinh(βx/2)] / [cosh(3βx/2) + e^{-2Dβ} cosh(βx/2)],
g(x) = (1/4) [9 cosh(3βx/2) + e^{-2Dβ} cosh(βx/2)] / [cosh(3βx/2) + e^{-2Dβ} cosh(βx/2)],
h(x) = (1/8) [27 sinh(3βx/2) + e^{-2Dβ} sinh(βx/2)] / [cosh(3βx/2) + e^{-2Dβ} cosh(βx/2)],
with β = 1/(k_B T).

Formulation B (approximate): Use a generalized approximate van der Waerden identity,
exp(a S_i^z) ≈ cosh((η/α) a) + (α/η) S_i^z sinh((η/α) a),
with α=2 and (η/α)^2 = q. This leads to the simpler coupled equations
m = [cosh((η/α) J ∇) + (α/η) m sinh((η/α) J ∇)]^z f(x)|_{x=0},
q = [cosh((η/α) J ∇) + (α/η) m sinh((η/α) J ∇)]^z g(x)|_{x=0}.

For both formulations on the honeycomb lattice (z=3), the critical temperature Tc is determined by linearizing the equations in the paramagnetic phase. Then the full equations are solved self-consistently over a temperature grid to obtain m, q, r (Formulation A) or m, q (Formulation B). The internal energy U is computed from
U/N = -1/2 ⟨E_i S_i^z⟩ - D q,
with ⟨E_i S_i^z⟩ given by
Formulation A: ⟨E_i S_i^z⟩ = (Jz/2)[-9/8 D(J∇) + 2 A(J∇) m + E(J∇) q + 2 C(J∇) r] [...]^{z-1} f(x)|_{x=0},
where E(J∇) = 1/2[3 sinh(3J∇/2) - sinh(J∇/2)],
Formulation B: ⟨E_i S_i^z⟩ = zJ (η/α)[sinh((Jη/α)∇) + m(α/η) cosh((Jη/α)∇)] [...]^{z-1} f(x)|_{x=0}.

The specific heat C = dU/dT is obtained by numerical differentiation.

## Reproduction target
Compute and output the following quantities for both Formulation A and Formulation B:

1. Critical temperatures Tc (units of J/k_B) for crystal-field ratios D/J = -2.0, -1.6, -1.5, 0.0, 2.0.
2. Magnetic specific heat C (units of k_B per spin) as a function of reduced temperature T/Tc for D/J = -2.0, -1.6, -1.5, 2.0, over the range T/Tc ≈ 0.05 to 1.2.
3. Internal energy per spin U/(JN) and order parameters m, q, r (only Formulation A includes r) at selected low temperatures (including T/Tc ≈ 0.001 to approximate T=0) for D/J = -2.0, -1.5, 2.0, plus a few additional temperatures that illustrate the low-T behavior.

The results must be saved as the CSV files specified in the workflow steps, with columns and formats as described in the output contract.

## Assets

- Python numerical libraries (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Define analytical functions for spin-3/2 BC model
- Role: process
- Action: Implement the Ising spin identity functions f(x), g(x), h(x), the exact van der Waerden identity coefficients A(a), B(a), C(a), D(a) for spin-3/2, and the generalized approximate cosh/sinh expansion with parameter eta/alpha, as callable numerical routines.
- Evidence: none

### Step 2: Solve Formulation A (exact van der Waerden identity)
- Role: process
- Action: For a honeycomb lattice (z=3), numerically solve the coupled self-consistent equations for magnetization m, quadrupolar moment q, and cubic moment r from Formulation A to obtain m, q, r and the critical temperature Tc for each crystal-field value D/J in {-2.0, -1.6, -1.5, 0.0, 2.0}. Solve over a fine temperature grid from near zero to above Tc. Store m, q, r, and Tc for each D/J in a structured JSON file.
- Evidence: `/app/outputs/formulation_A_solution.json`

### Step 3: Solve Formulation B (generalized approximate identity)
- Role: process
- Action: Using the generalized approximate van der Waerden identity (with alpha=2 and (eta/alpha)^2 = q) described in the Approach, numerically solve the coupled equations for magnetization m and quadrupolar moment q from Formulation B on the same lattice and D/J values and temperature grid. Determine Tc for each D/J. Store the results in a JSON file.
- Evidence: `/app/outputs/formulation_B_solution.json`

### Step 4: Compute internal energy and specific heat (Formulation A)
- Role: process
- Action: From the solved m, q, r of Formulation A, compute the internal energy U using the formula U/N = -1/2 ⟨E_i S_i^z⟩ - D q and the expression for ⟨E_i S_i^z⟩ from Formulation A given in the Approach. Then numerically differentiate U to obtain the magnetic specific heat C for each D/J and temperature. Save the computed U and C data alongside the original order parameters.
- Evidence: `/app/outputs/formulation_A_U_C.json`

### Step 5: Compute internal energy and specific heat (Formulation B)
- Role: process
- Action: Analogously, compute the internal energy U using the formula U/N = -1/2 ⟨E_i S_i^z⟩ - D q and the expression for ⟨E_i S_i^z⟩ from Formulation B. Differentiate to obtain C. Save results.
- Evidence: `/app/outputs/formulation_B_U_C.json`

### Step 6: Critical temperatures table
- Role: scored
- Action: Read the Tc values from the solution files of both formulations. Write a CSV file `tc_values.csv` with columns: formulation (A or B), D_div_J (float), Tc (float, units of J/k_B). Include rows for D/J = -2.0, -1.6, -1.5, 0.0, 2.0 for each formulation.
- Output file: `/app/outputs/tc_values.csv`
- Format: csv
- Contract: CSV with columns: formulation (str), D_div_J (float), Tc (float)
- Scoring: scored by hidden verifier

### Step 7: Specific heat curves
- Role: scored (load-bearing)
- Action: Read the specific heat C and reduced temperature T/Tc from the solution files of both formulations. Write `specific_heat_curves.csv` with columns: formulation (A or B), D_div_J (float), T_div_Tc (float, from ~0.05 to 1.2), specific_heat (float). Include data for D/J = -2.0, -1.6, -1.5, 2.0 for both formulations.
- Output file: `/app/outputs/specific_heat_curves.csv`
- Format: csv
- Contract: CSV with columns: formulation (str), D_div_J (float), T_div_Tc (float), specific_heat (float)
- Scoring: scored by hidden verifier

### Step 8: Internal energy and order parameters at low temperature
- Role: scored
- Action: Read the order parameters m, q, r and internal energy U from the solution files at selected temperatures. Write `internal_energy_order_params.csv` with columns: formulation (A or B), D_div_J (float), T_div_Tc (float), m (float), q (float), r (float, empty for Formulation B), U_div_J (float). Include data for D/J = -2.0, -1.5, 2.0 at T_div_Tc ≈ 0.001 (approximate T=0) and at a few other temperatures that illustrate the low-temperature behaviour.
- Output file: `/app/outputs/internal_energy_order_params.csv`
- Format: csv
- Contract: CSV with columns: formulation (str), D_div_J (float), T_div_Tc (float), m (float), q (float), r (float or empty), U_div_J (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_values.csv`
- `/app/outputs/specific_heat_curves.csv`
- `/app/outputs/internal_energy_order_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_values.csv
- path: `/app/outputs/tc_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical temperatures from both formulations at five crystal-field values.
- schema:
  - `type`: table
  - `required_columns`: `formulation`, `D_div_J`, `Tc`
  - `units`:
    - `D_div_J`: dimensionless
    - `Tc`: J/k_B

### specific_heat_curves.csv
- path: `/app/outputs/specific_heat_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Specific heat curves for both formulations at the D/J values where anomalous behaviour is expected.
- schema:
  - `type`: table
  - `required_columns`: `formulation`, `D_div_J`, `T_div_Tc`, `specific_heat`
  - `units`:
    - `D_div_J`: dimensionless
    - `T_div_Tc`: dimensionless
    - `specific_heat`: k_B per spin

### internal_energy_order_params.csv
- path: `/app/outputs/internal_energy_order_params.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Internal energy and order parameters at near-zero temperature, confirming ground-state values.
- schema:
  - `type`: table
  - `required_columns`: `formulation`, `D_div_J`, `T_div_Tc`, `m`, `q`, `r`, `U_div_J`
  - `units`:
    - `D_div_J`: dimensionless
    - `T_div_Tc`: dimensionless
    - `m`: dimensionless
    - `q`: dimensionless
    - `r`: dimensionless
    - `U_div_J`: dimensionless

Notes: The checker will validate that Tc at D=0 matches paper-reported values within tolerance, that specific heat shows the required structural features (broad maximum, sharp peak), and that ground-state internal energy and cubic moment at D=2.0 are correctly reproduced. Exact tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "formulation",
          "D_div_J",
          "Tc"
        ],
        "units": {
          "D_div_J": "dimensionless",
          "Tc": "J/k_B"
        }
      },
      "description": "Critical temperatures from both formulations at five crystal-field values."
    },
    {
      "file": "specific_heat_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "formulation",
          "D_div_J",
          "T_div_Tc",
          "specific_heat"
        ],
        "units": {
          "D_div_J": "dimensionless",
          "T_div_Tc": "dimensionless",
          "specific_heat": "k_B per spin"
        }
      },
      "description": "Specific heat curves for both formulations at the D/J values where anomalous behaviour is expected."
    },
    {
      "file": "internal_energy_order_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "formulation",
          "D_div_J",
          "T_div_Tc",
          "m",
          "q",
          "r",
          "U_div_J"
        ],
        "units": {
          "D_div_J": "dimensionless",
          "T_div_Tc": "dimensionless",
          "m": "dimensionless",
          "q": "dimensionless",
          "r": "dimensionless",
          "U_div_J": "dimensionless"
        }
      },
      "description": "Internal energy and order parameters at near-zero temperature, confirming ground-state values."
    }
  ],
  "notes": "The checker will validate that Tc at D=0 matches paper-reported values within tolerance, that specific heat shows the required structural features (broad maximum, sharp peak), and that ground-state internal energy and cubic moment at D=2.0 are correctly reproduced. Exact tolerances are hidden."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently compares your output files against reference values and structural criteria.

- For tc_values.csv, the verifier checks that the critical temperatures are accurate within an appropriate tolerance.
- For specific_heat_curves.csv, the verifier checks for the presence of expected structural features: the shape (e.g., broad maximum, sharp peak), the approximate location of features on the T/Tc axis, and relative magnitudes.
- For internal_energy_order_params.csv, the verifier checks the ground-state internal energy per spin and the value of the cubic moment r at D/J=2.0 are correctly reproduced, and verifies low-temperature consistency.

Each scored artifact contributes a weight toward the final reward (0.0–1.0). You must produce the artifacts by running the full numerical solution; merely reporting the paper's numbers or a guess without executing the workflow is insufficient.
