# ZBLAN Glass Elastic Constants and Grüneisen Parameters Calculation from Ultrasonic Velocity Data

## Problem background
ZBLAN heavy-metal fluoride glasses are promising for mid-IR optics, fiber amplifiers, and remote sensing owing to their extended infrared transparency and low phonon energy. Their mechanical and elastic properties under varying temperature and pressure are critical for practical applications. This task addresses the computation of the complete set of second-order and third-order elastic constants, the temperature and pressure derivatives of the elastic moduli, and the acoustic-mode Grüneisen parameters for a specific ZBLAN glass composition, starting from digitized ultrasonic velocity data.

## Approach
The approach is based on ultrasonic pulse-echo measurements that record longitudinal and transverse sound velocities as functions of temperature (from ambient to ~475 K) and hydrostatic and uniaxial pressure (up to ~1 kbar). From the ambient velocities and the known density, the second-order elastic constants C₁₁ and C₄₄ are obtained, and isotropic moduli (bulk modulus, Young's modulus, Poisson's ratio) are derived. Linear fits to the temperature-dependent velocities give ∂V/∂T, which are converted to ∂S/∂T and ∂B/∂T. The pressure-dependent natural velocity changes (ΔW/W) yield slopes d(ρ₀W²)/dP at zero pressure. These slopes, together with the isothermal moduli, are used to set up the Thurston–Brugger equations for an isotropic solid. Solving the resulting linear system gives the three independent third-order elastic constants (ν₁, ν₂, ν₃); the remaining six TOECs follow from linear combinations. With the complete set of TOECs, the pressure derivatives ∂S/∂P and ∂B/∂P and the mode Grüneisen parameters γ₁₁ and γ₄₄ are calculated using standard isotropic relations.

## Reproduction target
From the provided digitized CSV files of velocity versus temperature and relative natural velocity change versus pressure, together with the baseline properties JSON, execute the computational pipeline and write the following artifacts under /app/outputs:
- TOECs.json: the nine third-order elastic constants (ν₁, ν₂, ν₃ and the six derived C constants).
- temperature_pressure_derivatives.json: the six quantities ∂S/∂T, ∂B/∂T, ∂S/∂P, ∂B/∂P, γ₁₁, and γ₄₄.
The output formats and schemas are specified in the workflow steps and output contract below.

## Assets

- zblan_VL_vs_T.csv
- zblan_VT_vs_T.csv
- zblan_hydrostatic_dW_W.csv
- zblan_uniaxial_dW_W.csv
- zblan_baseline_properties.json
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute Second-Order Elastic Constants and Derived Moduli
- Role: process
- Action: Load the four CSV velocity datasets and the baseline properties JSON (all bundled). From the room‑temperature longitudinal (V_L) and transverse (V_T) velocities and density ρ, compute the second‑order elastic constants C₁₁ = ρ V_L² and C₄₄ = ρ V_T². Derive the bulk modulus B, Young's modulus E, and Poisson's ratio σ using the standard isotropic solid relations. These values are needed as inputs for the subsequent steps.
- Evidence: none

### Step 2: Compute Third-Order Elastic Constants
- Role: scored
- Action: From the hydrostatic and uniaxial pressure ΔW/W data, extract the slopes of d(ρ₀W²)/dP at P=0. Set up the three Thurston–Brugger equations for isotropic solids (one for hydrostatic longitudinal, one for hydrostatic transverse, one for uniaxial transverse perpendicular to stress) using the known isothermal elastic moduli computed in step_01. Solve the linear system for the three independent TOECs ν₁, ν₂, ν₃. Then compute the remaining TOECs (C₁₁₁, C₁₁₂, C₁₂₃, C₁₄₄, C₁₅₅, C₄₅₆) via the linear combinations ν₁+2ν₂, ν₂+2ν₃, ν₁+6ν₂+8ν₃, etc. Write all nine third-order elastic constants to the output JSON file.
- Output file: `/app/outputs/TOECs.json`
- Format: json
- Contract: {"nu1": <number>, "nu2": <number>, "nu3": <number>, "C111": <number>, "C112": <number>, "C123": <number>, "C144": <number>, "C155": <number>, "C456": <number>}
- Scoring: scored by hidden verifier

### Step 3: Compute Temperature and Pressure Derivatives and Grüneisen Parameters
- Role: scored
- Action: Perform linear fits to the V_L vs T and V_T vs T data to obtain ∂V/∂T. Compute the temperature derivatives of the shear modulus S (≡ C₄₄) and bulk modulus B using the appropriate derivatives (∂S/∂T = 2ρ V_T (∂V_T/∂T), and ∂B/∂T derived from the bulk modulus expression). Using the TOECs from step_02, compute the pressure derivatives ∂S/∂P and ∂B/∂P via the standard isotropic relations. Compute the acoustic Grüneisen parameters γ₁₁ and γ₄₄ using formulas that involve SOECs, TOECs, and bulk modulus. Write all six quantities to the output JSON file.
- Output file: `/app/outputs/temperature_pressure_derivatives.json`
- Format: json
- Contract: {"dS_dT_GPa_K": <number>, "dB_dT_GPa_K": <number>, "dS_dP_none": <number>, "dB_dP_none": <number>, "gamma_11": <number>, "gamma_44": <number>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/TOECs.json`
- `/app/outputs/temperature_pressure_derivatives.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### TOECs.json
- path: `/app/outputs/TOECs.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The nine third-order elastic constants derived from pressure‑dependent ultrasonic data.
- schema:
  - `type`: object
  - `required`:
    - `nu1`: number (GPa)
    - `nu2`: number (GPa)
    - `nu3`: number (GPa)
    - `C111`: number (GPa)
    - `C112`: number (GPa)
    - `C123`: number (GPa)
    - `C144`: number (GPa)
    - `C155`: number (GPa)
    - `C456`: number (GPa)

### temperature_pressure_derivatives.json
- path: `/app/outputs/temperature_pressure_derivatives.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The six quantities that summarize the temperature and pressure response of the elastic moduli and the acoustic mode Grüneisen parameters.
- schema:
  - `type`: object
  - `required`:
    - `dS_dT_GPa_K`: number (GPa K⁻¹)
    - `dB_dT_GPa_K`: number (GPa K⁻¹)
    - `dS_dP_none`: number (dimensionless)
    - `dB_dP_none`: number (dimensionless)
    - `gamma_11`: number (dimensionless)
    - `gamma_44`: number (dimensionless)

Notes: All input velocity and pressure data are bundled digital extractions from the source paper. The agent is expected to reproduce the computational pipeline (velocity‑to‑modulus conversion, linear fitting, Thurston–Brugger equation solving, and Grüneisen formulas) and report the derived constants. The hidden checker recomputes the same quantities from the same input data and compares within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "TOECs.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "nu1": "number (GPa)",
          "nu2": "number (GPa)",
          "nu3": "number (GPa)",
          "C111": "number (GPa)",
          "C112": "number (GPa)",
          "C123": "number (GPa)",
          "C144": "number (GPa)",
          "C155": "number (GPa)",
          "C456": "number (GPa)"
        }
      },
      "description": "The nine third-order elastic constants derived from pressure‑dependent ultrasonic data."
    },
    {
      "file": "temperature_pressure_derivatives.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "dS_dT_GPa_K": "number (GPa K⁻¹)",
          "dB_dT_GPa_K": "number (GPa K⁻¹)",
          "dS_dP_none": "number (dimensionless)",
          "dB_dP_none": "number (dimensionless)",
          "gamma_11": "number (dimensionless)",
          "gamma_44": "number (dimensionless)"
        }
      },
      "description": "The six quantities that summarize the temperature and pressure response of the elastic moduli and the acoustic mode Grüneisen parameters."
    }
  ],
  "notes": "All input velocity and pressure data are bundled digital extractions from the source paper. The agent is expected to reproduce the computational pipeline (velocity‑to‑modulus conversion, linear fitting, Thurston–Brugger equation solving, and Grüneisen formulas) and report the derived constants. The hidden checker recomputes the same quantities from the same input data and compares within appropriate tolerances."
}
```

## How you are scored
A hidden verifier recomputes the same pipeline from the same input data and checks each scored artifact (TOECs.json and temperature_pressure_derivatives.json) against reference values. Comparisons use tolerances that account for typical numerical spread from linear fitting and linear system solving. Your final reward is a weighted combination of the scores from the two outputs. Simply reporting the paper's published numbers without performing the required computation is insufficient; the values must arise from correctly executing the workflow described in the steps below.
