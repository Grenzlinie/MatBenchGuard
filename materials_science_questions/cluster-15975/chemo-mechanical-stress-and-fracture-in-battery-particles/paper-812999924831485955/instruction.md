# Large Deformation Elastic-Viscoplastic Model of Lithium Metal

## Problem background
Lithium metal anodes in all-solid-state batteries undergo large viscoplastic deformations at room temperature. An essential ingredient for modeling the mechanical interaction between lithium and a solid electrolyte is a constitutive model that captures the finite-strain, rate-dependent response of lithium. A recently developed isotropic elastic-viscoplastic model, calibrated against microindentation data, describes this behavior. This task reproduces two key predictions of that model: the homogeneous stress-strain response at several strain rates and a representative microindentation load-depth curve.

## Approach
The constitutive model is a finite-strain isotropic elastic-viscoplastic formulation. It uses multiplicative decomposition of the deformation gradient into elastic and plastic parts, logarithmic elastic strain, a free energy quadratic in elastic strain, an associative viscoplastic flow rule with a power-law dependence of plastic strain rate on equivalent stress and flow resistance, and saturation hardening. Material parameters are: Young's modulus E = 5 GPa, Poisson's ratio ν = 0.3, reference strain rate ε̇₀ = 0.05 s⁻¹, rate-sensitivity exponent m = 0.18, initial flow resistance S₀ = 2 MPa, hardening modulus H₀ = 40 MPa, saturation resistance S* = 8 MPa, hardening exponent a = 1.8.

First, implement this model as a reusable Python routine that, given a deformation gradient, returns the Cauchy stress and updates the internal variables (plastic distortion, flow resistance). Then perform two simulations:

1. Homogeneous compression: deform a material point at constant true strain rates of 0.1, 0.2, 0.5, 1.0 s⁻¹ from strain 0 to 1.0. Record true stress versus logarithmic strain.
2. Axisymmetric microindentation: model a conical indenter (included angle 140.6°, equivalent to a Berkovich indenter) with the same constitutive model in an open-source FE solver (FEniCS or equivalent). The lithium specimen is a cylinder 200 μm tall and 300 μm radius, meshed with refinement near the tip. Apply a load-controlled protocol: loading at constant dP/P = 1 s⁻¹ (P = k exp(c t) with k = 0.009 mN, c = 1 s⁻¹) until load reaches 5.88 mN; hold constant for 10 s; unload at 18.49 mN/s to zero load. Record load (mN) and indentation depth (nm) throughout.

## Reproduction target
Produce the following two scored artifacts:
- stress_strain_curves.csv: homogeneous true stress-strain curves of lithium at strain rates 0.1, 0.2, 0.5, and 1 s⁻¹ up to a true strain of 1.0. Columns: strain, stress_0.1, stress_0.2, stress_0.5, stress_1 (true stress in MPa). At least 100 points covering the strain range.
- indentation_P_h_curve_dP_over_P_1.csv: load versus indentation depth for the microindentation test under constant dP/P = 1 s⁻¹, covering loading, hold, and unloading. Columns: displacement_nm (indentation depth in nanometers), load_mN (applied force in millinewtons). At least 200 data points.

## Assets

- FEniCS or equivalent open-source FE solver: https://fenicsproject.org/
- Python scientific computing stack (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Implement constitutive model
- Role: process
- Action: Implement the finite-strain isotropic elastic-viscoplastic constitutive equations (multiplicative decomposition, logarithmic elastic strain, free energy, stress, plastic flow rule with power-law viscoplasticity, and saturation hardening) as a reusable Python routine. Use material parameters: E=5 GPa, ν=0.3, ε̇₀=0.05 s⁻¹, m=0.18, S₀=2 MPa, H₀=40 MPa, S*=8 MPa, a=1.8. The routine should accept a deformation gradient and return stress and updated internal variables.
- Evidence: `/app/outputs/material_model.py`

### Step 2: Homogeneous compression tests
- Role: scored (load-bearing)
- Action: Using the implemented constitutive model, simulate simple compression at constant true strain rates of 0.1, 0.2, 0.5, and 1.0 s⁻¹. Deform a material point from 0 to 1.0 true strain and record true stress (MPa) vs. logarithmic strain. Compile the results into a single CSV with columns: strain, stress_0.1, stress_0.2, stress_0.5, stress_1. Provide at least 100 rows covering the strain range.
- Output file: `/app/outputs/stress_strain_curves.csv`
- Format: csv
- Contract: CSV with header 'strain,stress_0.1,stress_0.2,stress_0.5,stress_1'; strain is logarithmic strain (0 to 1), stress columns contain true stress in MPa at the corresponding strain rate; at least 100 rows covering the strain range.
- Scoring: scored by hidden verifier

### Step 3: Microindentation simulation
- Role: scored (load-bearing)
- Action: Implement an axisymmetric finite element model of conical indentation (included angle 140.6°) using the same constitutive model and an open-source FE solver. Lithium specimen: cylinder 200 μm tall, 300 μm radius, meshed with refinement near tip. Apply load-controlled protocol: loading phase with dP/P=1 s⁻¹ (P=k exp(c t), k=0.009 mN, c=1 s⁻¹) until load reaches 5.88 mN; hold constant for 10 s; unload at 18.49 mN/s to zero. Output load (mN) vs. indentation depth (nm) data covering all phases.
- Output file: `/app/outputs/indentation_P_h_curve_dP_over_P_1.csv`
- Format: csv
- Contract: CSV with header 'displacement_nm,load_mN'; displacement_nm is indentation depth in nanometers, load_mN is applied force in millinewtons; at least 200 data points covering loading, hold, and unloading phases.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_curves.csv`
- `/app/outputs/indentation_P_h_curve_dP_over_P_1.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_curves.csv
- path: `/app/outputs/stress_strain_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Homogeneous true stress-strain curves for lithium at strain rates 0.1, 0.2, 0.5, 1 s⁻¹ up to strain 1.0.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_0.1`, `stress_0.2`, `stress_0.5`, `stress_1`
  - `units`:
    - `strain`: 1
    - `stress_0.1`: MPa
    - `stress_0.2`: MPa
    - `stress_0.5`: MPa
    - `stress_1`: MPa

### indentation_P_h_curve_dP_over_P_1.csv
- path: `/app/outputs/indentation_P_h_curve_dP_over_P_1.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Load vs. indentation depth curve for the microindentation experiment under constant dP/P=1 s⁻¹, covering loading, hold, and unloading.
- schema:
  - `type`: table
  - `required_columns`: `displacement_nm`, `load_mN`
  - `units`:
    - `displacement_nm`: nm
    - `load_mN`: mN

Notes: The hidden checker will compare the agent's submitted stress-strain curves and indentation load-depth curve against reference values derived from the paper's reported results, applying tolerances and qualitative shape checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_0.1",
          "stress_0.2",
          "stress_0.5",
          "stress_1"
        ],
        "units": {
          "strain": "1",
          "stress_0.1": "MPa",
          "stress_0.2": "MPa",
          "stress_0.5": "MPa",
          "stress_1": "MPa"
        }
      },
      "description": "Homogeneous true stress-strain curves for lithium at strain rates 0.1, 0.2, 0.5, 1 s⁻¹ up to strain 1.0."
    },
    {
      "file": "indentation_P_h_curve_dP_over_P_1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_nm",
          "load_mN"
        ],
        "units": {
          "displacement_nm": "nm",
          "load_mN": "mN"
        }
      },
      "description": "Load vs. indentation depth curve for the microindentation experiment under constant dP/P=1 s⁻¹, covering loading, hold, and unloading."
    }
  ],
  "notes": "The hidden checker will compare the agent's submitted stress-strain curves and indentation load-depth curve against reference values derived from the paper's reported results, applying tolerances and qualitative shape checks."
}
```

## How you are scored
A hidden verifier runs after you submit. It independently evaluates each scored artifact against reference values (derived from the published model and experimental data). For the stress-strain curves, it checks that the reported stresses at each strain rate agree with the reference within appropriate tolerances and that the curves exhibit the expected monotonicity and smoothness. For the indentation curve, it compares your load values at specific displacements to hidden reference loads and verifies that the curve qualitatively shows creep during the hold period and elastic recovery during unloading. Each artifact carries a fraction of the total reward; the final score is a weighted combination. Reporting a plausible number without executing the correct simulation will not pass the verifier.
