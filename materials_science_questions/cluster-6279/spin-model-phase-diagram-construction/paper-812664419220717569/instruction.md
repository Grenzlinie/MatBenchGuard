# Ferronematic Suspension Mean-Field Theory: Phase Diagram and Coupling Parameter Determination

## Problem background
The problem is to construct the finite-temperature phase diagram of ferromagnetic liquid crystal suspensions (ferronematics) using a tensorial molecular-statistical mean-field theory. The system is a homogeneous binary mixture of nematic liquid-crystal molecules and anisometric magnetic particles, described by scalar nematic order parameters for both components and a magnetization vector. The free energy includes nonmagnetic and magnetic-origin orientational couplings. Solving the self-consistency equations yields the stability regions of isotropic, ferromagnetic nematic, antiferromagnetic nematic, and superparamagnetic nematic phases, and the values of mean-field coupling parameters from experimental inputs.

## Approach
The approach is based on a mean-field free energy that includes entropic contributions from the liquid crystal and particles, an anisotropic nonmagnetic orientational coupling between their alignment tensors, and a magnetic-origin coupling between liquid crystal order and the particle magnetization vector. Minimizing this free energy with respect to the single-particle distribution functions yields a closed system of self-consistency equations for three scalar order parameters: the nematic order of the liquid crystal, the nematic order of the particles, and the magnetization. These equations involve dimensionless temperature and two mean-field coupling parameters (one for nonmagnetic interaction, one for magnetic interaction).

The goal is to solve these equations numerically under two distinct conditions:
1. **Phase diagram construction:** For fixed values of the nonmagnetic coupling parameter ω, scan the reduced temperature and the magnetic coupling parameter ω_m. At each point, determine the stable phase (isotropic I, ferromagnetic nematic FMN, antiferromagnetic nematic AFMN, superparamagnetic nematic SPMN) and the order of any phase transitions. Identify triple points where three phases coexist.
2. **Coupling parameter determination:** For prescribed values of the phenomenological coupling constant κ̃, combine the self-consistency equations with the relation linking κ̃, ω, ω_m, and the order parameters. From the resulting solution family, find the maximum achievable magnetization M and the corresponding ω and ω_m.

All material parameters are computed from the provided system constants (molar mass, density, clearing point, particle dimensions, etc.), and all calculations are performed with standard numerical libraries.

## Reproduction target
Implement the mean-field free energy and the self-consistency equations for the order parameters (liquid crystal nematic order, particle nematic order, magnetization). Compute all material parameters from the given numeric constants (molar mass and density of 5CB, clearing point, platelet dimensions, Avogadro number, volume fraction, and saturation magnetization). Then produce two scored artifacts:

- For ω = 0, 0.4, 1.2, scan the parameter space of reduced temperature and coupling parameter ω_m. Locate the phase boundaries and extract the coordinates (ω_m value at the transition) and the transition orders of the triple points. Classify the order of the transition from isotropic to the ordered phase (first or second order) and, when an AFMN phase is present, the order of the FMN–AFMN boundary.

- For the phenomenological coupling parameters κ̃ = 60 and 130, solve the coupled system consisting of the self-consistency equations and the relation between κ̃, ω, ω_m, and the order parameters. Obtain the valid (ω, ω_m) pairs as a function of magnetization M. Find the maximum achievable M and record the corresponding ω and ω_m.

Write the results to JSON files as specified in the workflow steps.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Material parameter computation and equilibrium equations
- Role: process
- Action: Compute all material parameters (v_n, v_p, γ, λ, τ, y_n, y_p, M₀) from the provided numeric constants (molar mass and density of 5CB, clearing point, platelet dimensions, Avogadro number, volume fraction y_p, and saturation magnetization M₀). Implement the function g(σ,ζ) and the self-consistency equations for scalar order parameters η, S, M as functions of the coupling parameters ω, ω_m and reduced temperature τ.
- Evidence: none

### Step 2: Determine mean-field coupling parameters ω, ω_m from experimental κ̃
- Role: scored (load-bearing)
- Action: For the two given values of the phenomenological coupling parameter κ̃ = 60 and κ̃ = 130, solve the coupled system consisting of the self-consistency equations together with the relation linking κ̃, ω, ω_m, and the order parameters. Obtain the valid (ω, ω_m) pairs as a function of magnetization M. Locate the maximum achievable M and the corresponding ω and ω_m. Write the results to /app/outputs/fig1_maxima.json.
- Output file: `/app/outputs/fig1_maxima.json`
- Format: json
- Contract: JSON array of objects, each with keys: kappa_tilde (int), M (float), omega (float), omega_m (float).
- Scoring: scored by hidden verifier

### Step 3: Construct phase diagrams and extract triple points
- Role: scored (load-bearing)
- Action: For the three values ω = 0, 0.4, 1.2, scan the (reduced temperature, ω_m) parameter space. At each point solve the equilibrium equations to determine the stable phase (I, FMN, AFMN, SPMN) and the order of any phase transitions. Identify the triple points (coordinates in ω_m and temperature) and the nature of the transitions involved (first-order or second-order). Write the triple points to /app/outputs/triple_points.json.
- Output file: `/app/outputs/triple_points.json`
- Format: json
- Contract: JSON array of objects, each with: omega (float), triple_omega_m (float), transition_order_I_to_ordered (string, "first" or "second"), transition_order_FMN_AFMN (string, "second" or null if not applicable).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fig1_maxima.json`
- `/app/outputs/triple_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fig1_maxima.json
- path: `/app/outputs/fig1_maxima.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum magnetization and corresponding coupling parameters for given phenomenological coupling constants κ̃=60 and 130.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `kappa_tilde`, `M`, `omega`, `omega_m`
    - `properties`:
      - `kappa_tilde`:
        - `type`: integer
      - `M`:
        - `type`: number
      - `omega`:
        - `type`: number
      - `omega_m`:
        - `type`: number

### triple_points.json
- path: `/app/outputs/triple_points.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Triple point coordinates and transition orders for phase diagrams at given ω values.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `omega`, `triple_omega_m`, `transition_order_I_to_ordered`, `transition_order_FMN_AFMN`
    - `properties`:
      - `omega`:
        - `type`: number
      - `triple_omega_m`:
        - `type`: number
      - `transition_order_I_to_ordered`:
        - `type`: string
        - `enum`: `first`, `second`
      - `transition_order_FMN_AFMN`:
        - `type`: `string`, `null`
        - `enum`: `second`, `None`
    - `additionalProperties`: False

Notes: The checker will compare the agent's reported values to hidden reference values with absolute tolerance 0.001 for triple_omega_m and 0.01 for M, ω, ω_m. Transition order strings must match exactly. The field transition_order_FMN_AFMN is "second" if an FMN-AFMN boundary exists at the triple point, otherwise null (e.g., when the ordered phase is not AFMN).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fig1_maxima.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "kappa_tilde",
            "M",
            "omega",
            "omega_m"
          ],
          "properties": {
            "kappa_tilde": {
              "type": "integer"
            },
            "M": {
              "type": "number"
            },
            "omega": {
              "type": "number"
            },
            "omega_m": {
              "type": "number"
            }
          }
        }
      },
      "description": "Maximum magnetization and corresponding coupling parameters for given phenomenological coupling constants κ̃=60 and 130."
    },
    {
      "file": "triple_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "omega",
            "triple_omega_m",
            "transition_order_I_to_ordered",
            "transition_order_FMN_AFMN"
          ],
          "properties": {
            "omega": {
              "type": "number"
            },
            "triple_omega_m": {
              "type": "number"
            },
            "transition_order_I_to_ordered": {
              "type": "string",
              "enum": [
                "first",
                "second"
              ]
            },
            "transition_order_FMN_AFMN": {
              "type": [
                "string",
                "null"
              ],
              "enum": [
                "second",
                null
              ]
            }
          },
          "additionalProperties": false
        }
      },
      "description": "Triple point coordinates and transition orders for phase diagrams at given ω values."
    }
  ],
  "notes": "The checker will compare the agent's reported values to hidden reference values with absolute tolerance 0.001 for triple_omega_m and 0.01 for M, ω, ω_m. Transition order strings must match exactly. The field transition_order_FMN_AFMN is \"second\" if an FMN-AFMN boundary exists at the triple point, otherwise null (e.g., when the ordered phase is not AFMN)."
}
```

## How you are scored
Each scored workflow step produces an output file (fig1_maxima.json and triple_points.json). A hidden verifier reads your files and compares the reported numeric values (M, ω, ω_m, triple_ω_m) to the expected reference results for this model and parameter set. The transition order strings are checked for exact match. The reward for each step is weighted, and the final score is the weighted combination. You must compute these quantities by solving the self-consistency equations yourself—the verifier checks the output of your computation, not whether you can look up the results. Appropriate absolute tolerances are applied to the numeric comparisons, so small numerical differences from implementation details are acceptable.
