# Lattice potential energy and standard molar enthalpy determination

## Problem background
1‑Dodecylamine hydrobromide (1‑C₁₂H₂₅NH₃·Br) is a key intermediate in the synthesis of solid–solid phase change materials. Accurate knowledge of its thermodynamic properties—lattice potential energy, ionic volume and radius of the organic cation, and standard molar enthalpies of combustion and formation—is essential for assessing stability and designing reactions involving this compound. This task computes these quantities from crystallographic and combustion‑calorimetry data.

## Approach
The lattice potential energy, cation volume, and ionic radius are derived from the compound's molar mass and density using the Jenkins–Glasser formalism for MX (1:1) salts. The molecular volume is first obtained, then the cation volume is calculated by subtracting the known bromide ion volume, and the ionic radius is inferred assuming a spherical cation.

The standard molar enthalpies of combustion and formation are determined through constant‑volume combustion calorimetry. The calorimeter's energy equivalent is calibrated by burning a certified standard (benzoic acid). The compound is then combusted under oxygen, and the measured temperature rise, together with wire heat and acid corrections, yields the constant‑volume energy of combustion. A pressure correction is applied, and the standard molar enthalpy of combustion is obtained via the ideal‑gas relation from the change in gas moles. Finally, the standard molar enthalpy of formation is calculated using a thermochemical cycle that combines the experimental enthalpy of combustion with standard enthalpies of formation of the combustion products.

## Reproduction target
Produce three scored output files that contain the following computed quantities:

- Lattice properties: lattice potential energy (U_POT), cation volume (V_plus), and ionic radius (r_plus).
- Combustion energy and enthalpy: constant‑volume energy of combustion per gram, per mole, and the standard molar enthalpy of combustion.
- Standard molar enthalpy of formation.

All quantities are to be derived from the provided bundled data and constants. The files must follow the exact schemas described in the workflow steps and output contract.

## Assets

- Crystal structure parameters (density, molar mass)
- Combustion calorimeter calibration data (7 runs)
- Combustion sample data (6 runs)
- Thermochemical constants and auxiliary enthalpies

## Workflow steps

### Step 1: Compute lattice properties
- Role: scored
- Action: Calculate molecular volume V_m from density and molar mass using V_m = M_m/(ρ·N_A) (in nm³). Then compute lattice potential energy U_POT using the Jenkins–Glasser equation for MX(1:1) salts: U_POT = γ·(ρ/M_m)^{1/3} + δ, with the constants γ and δ provided in thermo_constants. Compute cation volume V_plus = V_m − V_Br⁻, where V_Br⁻ = 0.0363 nm³ (from thermo_constants). Derive ionic radius r_plus = (3·V_plus/(4π))^{1/3}. Write the result to lattice_properties.csv.
- Output file: `/app/outputs/lattice_properties.csv`
- Format: csv
- Contract: CSV with required columns: quantity (string), value (float), unit (string). Rows: U_POT/kJ·mol⁻¹, V_plus/nm³, r_plus/nm.
- Scoring: scored by hidden verifier

### Step 2: Calibrate calorimeter energy equivalent
- Role: process
- Action: Read the seven calibration runs from the bundled calibration data file. For each run, compute the energy equivalent ε = (Q·W + q_c + q_N) / ΔT, using the certified benzoic acid combustion energy Q = −26434 J·g⁻¹ (from thermo_constants). Compute the mean ε_cal; it will be used in step 3. Optionally write a calibration_evidence.csv with the per-run ε values and the mean.
- Evidence: `/app/outputs/calibration_evidence.csv`

### Step 3: Compute specific energy and apply pressure correction
- Role: process
- Action: For each of the six sample combustion runs in the bundled sample data file, compute the raw constant‑volume energy of combustion per gram: −ΔcU_raw = (ε_cal·ΔT − q_c − q_N)/W. Average the six values to obtain the mean raw specific energy. Apply the pressure correction using the coefficient (∂U/∂P)_T = −0.2 J·g⁻¹·MPa⁻¹ and ΔP = −2.49 MPa (from thermo_constants) to get the corrected specific energy: −ΔcU_corr_per_g = −ΔcU_raw_per_g + 0.50 J·g⁻¹. This corrected value is required for step 4. Optionally write a combustion_evidence.csv with the raw per-experiment energies.
- Evidence: `/app/outputs/combustion_evidence.csv`

### Step 4: Compute standard molar enthalpy of combustion
- Role: scored (load-bearing)
- Action: Convert the corrected specific energy from step 3 to molar basis: ΔcU_m° = (−ΔcU_corr_per_g) × M_m × 10⁻³, with M_m = 266.26 g·mol⁻¹ from crystal_data. Then derive the standard molar enthalpy of combustion using the ideal‑gas relation: ΔcH_m° = ΔcU_m° + Δn·R·T, where Δn = −25/4 mol, R = 8.314 J·K⁻¹·mol⁻¹, T = 298.15 K (from thermo_constants). Write the three quantities to combustion_enthalpy.csv: ΔcU (J·g⁻¹), ΔcU (kJ·mol⁻¹), ΔcH (kJ·mol⁻¹).
- Output file: `/app/outputs/combustion_enthalpy.csv`
- Format: csv
- Contract: CSV with required columns: quantity (string), value (float), unit (string). Rows: Delta_cU_J_per_g, Delta_cU_kJ_per_mol, Delta_cH_kJ_per_mol.
- Scoring: scored by hidden verifier

### Step 5: Compute standard molar enthalpy of formation
- Role: scored
- Action: Using the standard molar enthalpy of combustion ΔcH_m° from step 4 and the provided standard enthalpies of formation of CO₂(g), H₂O(l), and HBr(l) from thermo_constants, apply the thermochemical cycle: ΔfH_m°(compound) = 12·ΔfH°(CO₂) + (27/2)·ΔfH°(H₂O) + ΔfH°(HBr) − ΔcH_m°. Write the result (kJ·mol⁻¹) to formation_enthalpy.csv.
- Output file: `/app/outputs/formation_enthalpy.csv`
- Format: csv
- Contract: CSV with required columns: quantity (string), value (float), unit (string). Row: Delta_fH_kJ_per_mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_properties.csv`
- `/app/outputs/combustion_enthalpy.csv`
- `/app/outputs/formation_enthalpy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_properties.csv
- path: `/app/outputs/lattice_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice potential energy (U_POT / kJ·mol⁻¹), cation volume (V_plus / nm³), and ionic radius (r_plus / nm).
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `value`, `unit`

### combustion_enthalpy.csv
- path: `/app/outputs/combustion_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Constant‑volume energy of combustion per gram (Delta_cU_J_per_g / J·g⁻¹), per mole (Delta_cU_kJ_per_mol / kJ·mol⁻¹), and standard molar enthalpy of combustion (Delta_cH_kJ_per_mol / kJ·mol⁻¹).
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `value`, `unit`

### formation_enthalpy.csv
- path: `/app/outputs/formation_enthalpy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Standard molar enthalpy of formation (Delta_fH_kJ_per_mol / kJ·mol⁻¹).
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `value`, `unit`

Notes: All values are deterministic given the provided bundled data and constants. The hidden checker compares the agent's reported values to the paper's gold values within tolerances. Submitted CSVs must contain exactly the specified rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "value",
          "unit"
        ]
      },
      "description": "Lattice potential energy (U_POT / kJ·mol⁻¹), cation volume (V_plus / nm³), and ionic radius (r_plus / nm)."
    },
    {
      "file": "combustion_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "value",
          "unit"
        ]
      },
      "description": "Constant‑volume energy of combustion per gram (Delta_cU_J_per_g / J·g⁻¹), per mole (Delta_cU_kJ_per_mol / kJ·mol⁻¹), and standard molar enthalpy of combustion (Delta_cH_kJ_per_mol / kJ·mol⁻¹)."
    },
    {
      "file": "formation_enthalpy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "value",
          "unit"
        ]
      },
      "description": "Standard molar enthalpy of formation (Delta_fH_kJ_per_mol / kJ·mol⁻¹)."
    }
  ],
  "notes": "All values are deterministic given the provided bundled data and constants. The hidden checker compares the agent's reported values to the paper's gold values within tolerances. Submitted CSVs must contain exactly the specified rows."
}
```

## How you are scored
Each of the three required output files is independently scored by a hidden verifier. The verifier reads your submitted CSV files and compares each numeric value to a reference within a tolerance that reflects legitimate computational spread. The final reward is a weighted sum of the per‑artifact scores, with the combustion enthalpy file carrying the highest weight and the lattice properties and formation enthalpy files each contributing a meaningful share. The verifier also validates that every required row and column is present. Reporting numbers without faithfully executing the described computational steps will not satisfy the tolerance requirements; the task is designed so that a correct re‑run yields the target values, whereas a guess or fabrication does not.
