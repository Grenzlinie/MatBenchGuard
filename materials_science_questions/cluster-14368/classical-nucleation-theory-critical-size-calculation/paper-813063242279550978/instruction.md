# Computing RESS Process Nucleation Rates and Supersaturation

## Problem background
The Rapid Expansion of Supercritical Solutions (RESS) process produces fine particles by expanding a supercritical solution through a capillary nozzle. The sudden drop in pressure and temperature creates a high degree of supersaturation, which drives nucleation and particle growth. The exact location within the expansion path where nucleation occurs and the magnitude of the nucleation rate are critical for controlling particle size, yet they are difficult to measure directly in the microscale nozzle and free jet. A computational model that can predict the fluid flow, solute supersaturation, and homogeneous nucleation rate along the expansion path is therefore essential for understanding and optimizing RESS.

## Approach
This task implements a one-dimensional steady-state flow model for the pure solvents CO₂ and CHF₃ in a capillary inlet, capillary nozzle, and supersonic free jet. The model solves the coupled mass, momentum, and energy balances using the extended generalized Bender equation of state (egB-EoS) to obtain axial profiles of pressure, temperature, density, and velocity. Heat exchange with the nozzle wall and friction are included, and the sonic condition (Ma = 1) at the nozzle exit determines the entrance velocity. The computed pressure and temperature profiles are then used with a modified Peng–Robinson equation of state to calculate the equilibrium solubility of the solutes cholesterol and benzoic acid in CO₂ and CHF₃. From the solubility and flow profiles, the supersaturation ratio along the expansion path is evaluated for each solute–solvent pair. Finally, classical nucleation theory is applied to compute the homogeneous nucleation rate profile, and the values at the capillary exit (x/L = 1) are extracted for comparison with theoretical predictions.

## Reproduction target
Compute the nucleation rate J (cm⁻³ s⁻¹) and supersaturation S (dimensionless) at the capillary exit for the three solute–solvent systems CO₂/cholesterol, CO₂/benzoic acid, and CHF₃/benzoic acid under the reference conditions: pre-expansion pressure 20 MPa, pre-expansion temperature 380 K, nozzle temperature 430 K, nozzle diameter 55 µm, nozzle length 350 µm, extraction temperature 313 K for cholesterol and 318 K for benzoic acid. You must produce all intermediate artifacts (validation report, flow profiles, solubility data, supersaturation profiles) that demonstrate the complete computational workflow, in addition to the final scored output file nucleation_rates.json.

## Assets

- Extended Generalized Bender Equation of State (Platzer and Maurer, 1989): 10.1016/0378-3812(89)87262-X
- Modified Peng–Robinson Equation of State (Schmitt and Reid, 1986): 10.1021/je00032a006
- Span–Wagner Fundamental Equation of State for CO₂: 10.1063/1.555991
- NIST Chemistry WebBook: https://webbook.nist.gov/chemistry/

## Workflow steps

### Step 1: Validate egB-EoS for CO₂ against Span–Wagner EoS
- Role: process
- Action: Implement the extended generalized Bender equation of state (egB-EoS) and the Span–Wagner fundamental EoS for CO₂. Compute sonic velocity over a pressure and temperature range relevant to the RESS expansion path. Verify that the maximum relative difference in predicted sonic velocity is less than 3%.
- Evidence: `/app/outputs/validation_report.json`

### Step 2: Solve 1D steady‑state flow model for pure solvents
- Role: process
- Action: Set up and solve the coupled mass, momentum, and energy balance equations for pure CO₂ and CHF₃ in the capillary inlet, capillary nozzle, and supersonic free jet using the egB-EoS. Include heat exchange and friction in the nozzle, adiabatic inlet, sonic condition at nozzle exit (Ma=1), and empirical Mach‑disk relations. Compute axial profiles of pressure, temperature, density, and velocity under reference conditions: p₀=20 MPa, T₀=380 K, T_nozzle=430 K, D_nozzle=55 µm, L_nozzle=350 µm.
- Evidence: `/app/outputs/flow_profiles.json`

### Step 3: Calculate equilibrium solubility with modified PR‑EoS
- Role: process
- Action: Implement the modified Peng–Robinson equation of state for the binary mixtures CO₂/cholesterol, CO₂/benzoic acid, and CHF₃/benzoic acid. Compute the equilibrium mole fraction y*(T,p) and fugacity coefficients Φ over a pressure range 0.1–30 MPa and temperatures spanning the flow path.
- Evidence: `/app/outputs/solubility_data.json`

### Step 4: Compute supersaturation profiles
- Role: process
- Action: Using the flow profiles (step 2) and the solubility model (step 3), compute the supersaturation S(x) for each mixture. Extraction conditions: CO₂/cholesterol – T_Extr=313 K, p_Extr=20 MPa; CO₂/benzoic acid and CHF₃/benzoic acid – T_Extr=318 K, p_Extr=20 MPa.
- Evidence: `/app/outputs/supersaturation_profiles.json`

### Step 5: Compute nucleation rates and extract exit values
- Role: scored (load-bearing)
- Action: For each mixture, apply classical nucleation theory using the interfacial tension σ=0.02 N/m, condensation coefficient α_c=0.1, non‑isothermal factor θ=1, and molecular volumes: cholesterol v_S=6×10⁻²⁸ m³, benzoic acid v_S=1.6×10⁻²⁸ m³. Calculate the nucleation rate profile J(x) from the supersaturation S(x) and temperature T(x) profiles. Extract the values of J (cm⁻³ s⁻¹) and S at the capillary exit (x/L=1) and write them to nucleation_rates.json.
- Output file: `/app/outputs/nucleation_rates.json`
- Format: json
- Contract: {"CO2_cholesterol": {"J": <number>, "S": <number>}, "CO2_benzoic_acid": {"J": <number>, "S": <number>}, "CHF3_benzoic_acid": {"J": <number>, "S": <number>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_rates.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_rates.json
- path: `/app/outputs/nucleation_rates.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Nucleation rate J (cm⁻³ s⁻¹) and supersaturation S (dimensionless) at the capillary exit for the three solute–solvent systems under the reference pre-expansion and nozzle conditions. The hidden checker compares these values against the paper's theoretical results using generous tolerances appropriate for re‑implementation differences.
- schema:
  - `type`: object
  - `required`:
    - `CO2_cholesterol`: object
    - `CO2_benzoic_acid`: object
    - `CHF3_benzoic_acid`: object
  - `items`:
    - `J`: number
    - `S`: number
  - `units`:
    - `J`: cm^{-3} s^{-1}
    - `S`: dimensionless

Notes: The experimental particle size measurements are excluded. The reference conditions and all material parameters required for the computation are stated in the instruction. The checker uses tolerances that absorb numerical implementation spread while still requiring genuine re‑execution of the workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_rates.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CO2_cholesterol": "object",
          "CO2_benzoic_acid": "object",
          "CHF3_benzoic_acid": "object"
        },
        "items": {
          "J": "number",
          "S": "number"
        },
        "units": {
          "J": "cm^{-3} s^{-1}",
          "S": "dimensionless"
        }
      },
      "description": "Nucleation rate J (cm⁻³ s⁻¹) and supersaturation S (dimensionless) at the capillary exit for the three solute–solvent systems under the reference pre-expansion and nozzle conditions. The hidden checker compares these values against the paper's theoretical results using generous tolerances appropriate for re‑implementation differences."
    }
  ],
  "notes": "The experimental particle size measurements are excluded. The reference conditions and all material parameters required for the computation are stated in the instruction. The checker uses tolerances that absorb numerical implementation spread while still requiring genuine re‑execution of the workflow."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that checks each output artifact produced by the workflow. The primary scored artifact is nucleation_rates.json; the verifier compares the reported J and S values at the capillary exit against the paper's theoretical expectations, using tolerant thresholds that account for implementation-dependent numerical differences. The intermediate process-step artifacts (validation_report.json, flow_profiles.json, solubility_data.json, supersaturation_profiles.json) are also audited for structural plausibility but carry lower weight. The final reward is a weighted combination of these checks. Simply reporting plausible-looking numbers without genuinely running the computational pipeline is insufficient—the verifier's internal cross-checks will detect missing or inconsistent profiles.
