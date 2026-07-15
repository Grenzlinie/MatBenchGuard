# Grüneisen Parameter Calculation Workflow

## Problem background
Cadmium fluoride (CdF₂) and β‑lead fluoride (β‑PbF₂) crystallize in the fluorite structure and show distinct thermal and transport properties at elevated temperatures. Reliable values for the coefficient of linear thermal expansion α and the Grüneisen parameter γ as functions of temperature are essential for understanding their thermal behaviour and for comparing them with other fluorite‑type crystals. The task is to compute α and γ over the 300–670 K range from published lattice‑parameter expressions and auxiliary thermodynamic data, thereby determining how these quantities evolve with temperature.

## Approach
The starting point is a pair of quadratic expressions a(T) = p₀ + p₁·T + p₂·T² that describe the temperature dependence of the lattice constant (Å) for each material. The linear thermal expansion coefficient α is obtained by differentiating a(T): da/dT = p₁ + 2 p₂ T, and normalising by the lattice constant at 300 K, a₃₀₀ = a(300 K), so that α = (1/a₃₀₀)·da/dT, reported in units of 10⁻⁶ K⁻¹.

The Grüneisen parameter γ is then calculated from γ = 3·α·V / (ψ_T·C_v), where V is the molar volume (V = a³·N_A/4, with N_A = 6.02214076×10²³ mol⁻¹ and 4 formula units per fluorite cell), ψ_T is the isothermal compressibility derived from the elastic constants C₁₁ and C₁₂ via ψ_T = 3/(C₁₁+2C₁₂), and C_v is the molar heat capacity at constant volume evaluated from the Debye function using the Debye temperatures θ_D = 328 K (CdF₂) and 237 K (β‑PbF₂).

The workflow proceeds in two stages: first, the auxiliary thermodynamic quantities (compressibility, molar volume, and specific heat at each temperature) are assembled; second, α and γ are evaluated at eight temperatures between 300 K and 650 K and written to a CSV file that serves as the scored deliverable.

## Reproduction target
Using the quadratic lattice‑parameter expressions for CdF₂ (p₀ = 5.3550, p₁ = 1.090×10⁻⁴, p₂ = 1.395×10⁻⁸) and β‑PbF₂ (p₀ = 5.9004, p₁ = 1.233×10⁻⁴, p₂ = 4.629×10⁻⁸), together with the literature elastic constants (C₁₁, C₁₂) and the stated Debye temperatures, compute α (10⁻⁶ K⁻¹) and γ (dimensionless) at temperatures 300, 350, 400, 450, 500, 550, 600, and 650 K. Write the results to a CSV file with columns Material (exactly 'CdF2' or 'PbF2'), Temperature (integer, K), Alpha (float), Gamma (float), producing 16 rows total. The reported numbers should reflect the procedure described in the workflow steps.

## Assets

- Elastic constants of CdF₂ (Alterovitz & Gerlich 1970): 10.1103/PhysRevB.1.4136
- Elastic constants of β-PbF₂ (Manasreh & Pederson 1984): 10.1103/PhysRevB.30.3482
- Debye temperature for CdF₂ (Hayes 1974; value 328 K)
- Debye temperature for β-PbF₂ (Dandekar et al. 1979; value 237 K)

## Workflow steps

### Step 1: Prepare auxiliary thermodynamic quantities
- Role: process
- Action: From the literature elastic constants C11 and C12, compute isothermal compressibility ψ_T = 3/(C11+2C12) for both materials. Compute molar volume V = a³·N_A/4 using the lattice parameter a at each temperature from the quadratic fits (a = p0 + p1·T + p2·T²) and Avogadro's number N_A = 6.02214076×10²³ mol⁻¹ (fluorite structure, 4 formula units per cell). Compute molar specific heat C_v at each temperature via the Debye function with Debye temperatures θ_D = 328 K (CdF₂) and 237 K (β-PbF₂). Write all quantities to an evidence file for the downstream step.
- Evidence: `/app/outputs/auxiliary_quantities.csv`

### Step 2: Compute thermal expansion coefficient and Grüneisen parameter
- Role: scored (load-bearing)
- Action: For CdF₂ (p0=5.3550, p1=1.090×10⁻⁴, p2=1.395×10⁻⁸) and β-PbF₂ (p0=5.9004, p1=1.233×10⁻⁴, p2=4.629×10⁻⁸), evaluate the lattice parameter a(T) and its derivative da/dT at temperatures 300,350,400,450,500,550,600,650 K. Compute the reference constant a₃₀₀ = a(300 K). Calculate the linear thermal expansion coefficient α = (1/a₃₀₀)·da/dT and express it in units of 10⁻⁶ K⁻¹. Using the molar volume V, isothermal compressibility ψ_T, and molar specific heat C_v from the auxiliary step, calculate the Grüneisen parameter γ = 3·α·V/(ψ_T·C_v). Write the final results to a CSV file.
- Output file: `/app/outputs/thermal_expansion_gruneisen.csv`
- Format: csv
- Contract: Columns: Material (string, exactly 'CdF2' or 'PbF2'), Temperature (integer, K), Alpha (float, in 10⁻⁶ K⁻¹), Gamma (float, dimensionless). One row per material per temperature, 16 rows total.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_expansion_gruneisen.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_expansion_gruneisen.csv
- path: `/app/outputs/thermal_expansion_gruneisen.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored reproduction of the coefficient of thermal expansion α and Grüneisen parameter γ for CdF₂ and β‑PbF₂ at temperatures 300–650 K. Values are compared against reference values derived from the same physical protocol within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Temperature`, `Alpha`, `Gamma`
  - `units`:
    - `Alpha`: 10^-6 K^-1
    - `Gamma`: dimensionless

Notes: Only the alpha_gamma CSV is scored. The auxiliary quantities CSV is an intermediate evidence file and is not part of the output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_expansion_gruneisen.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Temperature",
          "Alpha",
          "Gamma"
        ],
        "units": {
          "Alpha": "10^-6 K^-1",
          "Gamma": "dimensionless"
        }
      },
      "description": "Scored reproduction of the coefficient of thermal expansion α and Grüneisen parameter γ for CdF₂ and β‑PbF₂ at temperatures 300–650 K. Values are compared against reference values derived from the same physical protocol within a hidden tolerance."
    }
  ],
  "notes": "Only the alpha_gamma CSV is scored. The auxiliary quantities CSV is an intermediate evidence file and is not part of the output contract."
}
```

## How you are scored
A hidden verifier independently inspects the CSV file and compares each (Material, Temperature) entry against a set of reference values obtained from the same physical protocol. The reward is proportional to the number of α and γ entries that fall within a hidden tolerance of the reference; only entries whose relative deviation is within that tolerance contribute to the score. Additionally, lightweight structural checks verify that the computed quantities respect physically reasonable trends (e.g., monotonic evolution with temperature); failure to satisfy these checks reduces the reward slightly. The exact tolerance and weighting are not disclosed, so the only way to maximise your score is to faithfully implement the physical models and computations described in the workflow steps.
