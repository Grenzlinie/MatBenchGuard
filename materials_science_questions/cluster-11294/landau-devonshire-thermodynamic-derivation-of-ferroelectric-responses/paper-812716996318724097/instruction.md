# Landau-Devonshire elastocaloric response simulation for ferroelectric polymer copolymers

## Problem background
Ferroelectric polymers such as poly(vinylidene fluoride-trifluoroethylene) [P(VDF-TrFE)] are being explored for solid-state elastocaloric refrigeration. Using thermodynamic theory, it is possible to predict the adiabatic temperature change (ΔT) induced by applying a mechanical stress to these materials. The Landau-Devonshire phenomenological model provides a framework to compute the equilibrium polarization and the resulting entropy and temperature changes as a function of temperature and stress. This task reproduces the theoretical prediction of the elastocaloric response in P(VDF-TrFE) 65/35 and 70/30 copolymer films under a uniaxial compressive stress.

## Approach
The reproduction implements the elastic Gibbs free energy G(P,σ₃) for two P(VDF-TrFE) compositions (65/35 and 70/30) using provided Landau coefficients, elastic compliances, and electrostrictive constants. For a given uniaxial compressive stress σ₃ (0 and −100 MPa), the free energy is minimized numerically with respect to polarization over a temperature range spanning the ferroelectric–paraelectric transition to obtain the equilibrium polarization P(T,σ₃). From the equilibrium polarization, the isothermal entropy change ΔS when switching the stress from 0 to −100 MPa is computed. The entropy change includes three contributions: (1) a polarization change term proportional to the difference in squared polarization between the stressed and unstressed states, (2) an elastic term proportional to the square of the applied stress and the elastic compliance, and (3) a piezoelectric term involving the product of stress, polarization squared, and electrostrictive constant. The adiabatic temperature change ΔT is then obtained via ΔT = –T ΔS / (C ρ), where C is the specific heat capacity and ρ is the density.

## Model equations and material parameters

The elastic Gibbs free energy for a freestanding film with uniaxial stress σ₃ only (σ₁=σ₂=0) is:

G(P,σ₃) = ½ a P² + ¼ β P⁴ + ⅙ γ P⁶ - ½ s₁₁ σ₃² - Q₁₁ σ₃ P²

Where:
- P is the polarization (C/m²).
- a = a₀ (T - T₀) is the Landau temperature-dependent coefficient, with T in °C (converted to absolute temperature if needed, but consistent units). a₀ has units J m C⁻² K⁻¹.
- β, γ are Landau coefficients (J m⁵ C⁻⁴ and J m⁹ C⁻⁶).
- s₁₁ is the elastic compliance (m²/N).
- Q₁₁ is the electrostrictive constant (m⁴/C²).
- σ₃ is the uniaxial stress (Pa). Positive for tension, negative for compression.

The equilibrium polarization P(T,σ₃) is obtained by minimizing G with respect to P at each temperature and stress, i.e., solving ∂G/∂P = 0.

The isothermal entropy change upon changing stress from σ_i to σ_f is given by (zero initial stress, σ_i=0, σ_f = σ₃):

ΔS(T,σ₃) = -½ a₀ [P²(σ₃,T) - P²(0,T)] - 2 αₗ s₁₁ σ₃² - 2 αₗ σ₃ Q₁₁ P²(σ₃,T)

where αₗ is the linear thermal expansion coefficient (K⁻¹).

The adiabatic temperature change:

ΔT(T,σ₃) = - T ΔS / (C ρ)

where C is specific heat capacity (J kg⁻¹ K⁻¹) and ρ is density (kg m⁻³). Temperature T in the denominator must be in Kelvin (K). Use T_K = T_C + 273.15.

### Material coefficients for P(VDF-TrFE) copolymers

| Coefficient | 70/30 | 65/35 | Units |
|-------------|-------|-------|-------|
| T₀ | 33.7 | 40 | °C |
| a₀ | 7.5×10⁷ | 3.5×10⁷ | J m C⁻² K⁻¹ |
| β | -1.9×10¹² | -1.5×10¹² | J m⁵ C⁻⁴ |
| γ | 1.9×10¹⁴ | 1.9×10¹⁴ | J m⁹ C⁻⁶ |
| s₁₁ | 3.32×10⁻¹⁰ | 3.32×10⁻¹⁰ | m² N⁻¹ |
| s₁₂ | -1.44×10⁻¹⁰ | -1.44×10⁻¹⁰ | m² N⁻¹ (not directly used with σ₁=σ₂=0) |
| Q₁₁ | -12 | -12 | m⁴ C⁻² |
| Q₁₂ | 3 | 3 | m⁴ C⁻² (not used directly) |
| C | 1.19×10³ | 1.19×10³ | J kg⁻¹ K⁻¹ |
| ρ | 1.886×10³ | 1.886×10³ | kg m⁻³ |
| αₗ | 2.0×10⁻³ | 2.0×10⁻³ | K⁻¹ |

### Computational notes
- Use a temperature grid covering the relevant phase transition region (e.g., from room temperature up to about 180°C) with sufficient resolution (≈0.5–1°C).
- At each temperature, solve ∂G/∂P=0 for both σ₃=0 and σ₃=-100 MPa (converted to Pa: -100 MPa = -1×10⁸ Pa). Use a robust root-finding method. The minimum of G should be chosen among possible roots (including P=0) because G is a polynomial.
- For the free energy minimization, you may use scipy.optimize.minimize_scalar with a suitable initial guess (e.g., P ≈ 0.1 C/m²).
- Compute ΔS and then ΔT using Eq. (13) and (14), collecting contributions from polarization term, elastic term, and piezoelectric term.

## Reproduction target
Produce a CSV file, delta_T_vs_temperature.csv, that lists the computed adiabatic temperature change ΔT (in Kelvin) as a function of temperature (in °C) for both compositions under an applied uniaxial compressive stress of −100 MPa. The file must contain rows for a temperature grid covering the relevant transition regions, and the columns must be: composition (string, allowed values '65/35' or '70/30'), stress_MPa (float, always −100.0), temperature_C (float), and delta_T_K (float). The quality of the reproduction will be assessed based on the peak ΔT values achieved and their correspondence to the expected transition behavior.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Free energy minimization and equilibrium polarization
- Role: process
- Action: Implement the elastic Gibbs free energy G(P,σ₃) for P(VDF-TrFE) 65/35 and 70/30 using the provided Landau coefficients, elastic compliances, and electrostrictive constants. For each composition, at zero stress and at σ₃=−100 MPa, minimize G with respect to polarization over a temperature range covering the ferroelectric–paraelectric transition to obtain equilibrium polarization P(T,σ₃).
- Evidence: none

### Step 2: Isothermal entropy and adiabatic temperature change calculation
- Role: process
- Action: Using the equilibrium polarization from step 01, compute for each composition the isothermal entropy change ΔS(T) and adiabatic temperature change ΔT(T) when switching the uniaxial stress from 0 to −100 MPa, including polar, elastic, and piezoelectric contributions.
- Evidence: none

### Step 3: Write elastocaloric temperature change result
- Role: scored (load-bearing)
- Action: Write the computed adiabatic temperature change ΔT for both compositions at stress = −100 MPa as a function of temperature to delta_T_vs_temperature.csv.
- Output file: `/app/outputs/delta_T_vs_temperature.csv`
- Format: csv
- Contract: Columns: composition (string, '65/35' or '70/30'), stress_MPa (float, always -100.0), temperature_C (float), delta_T_K (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_T_vs_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_T_vs_temperature.csv
- path: `/app/outputs/delta_T_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Adiabatic elastocaloric temperature change ΔT as a function of temperature for the two copolymer compositions under a uniaxial compressive stress of −100 MPa. The peak ΔT values near the zero-stress Curie temperature are the scored quantities, compared against a hidden reference with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `stress_MPa`, `temperature_C`, `delta_T_K`
  - `units`:
    - `stress_MPa`: MPa
    - `temperature_C`: °C
    - `delta_T_K`: K

Notes: The checker will extract the maximum ΔT for each composition at the given stress and verify they are within an acceptable tolerance of the paper's predicted values, and that the peak occurs within ±20 °C of the expected Curie temperature. The file must contain rows covering a temperature range that includes the peak.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_T_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "stress_MPa",
          "temperature_C",
          "delta_T_K"
        ],
        "units": {
          "stress_MPa": "MPa",
          "temperature_C": "°C",
          "delta_T_K": "K"
        }
      },
      "description": "Adiabatic elastocaloric temperature change ΔT as a function of temperature for the two copolymer compositions under a uniaxial compressive stress of −100 MPa. The peak ΔT values near the zero-stress Curie temperature are the scored quantities, compared against a hidden reference with a tolerance."
    }
  ],
  "notes": "The checker will extract the maximum ΔT for each composition at the given stress and verify they are within an acceptable tolerance of the paper's predicted values, and that the peak occurs within ±20 °C of the expected Curie temperature. The file must contain rows covering a temperature range that includes the peak."
}
```

## How you are scored
A hidden automated verifier will evaluate your submitted CSV file. It will examine the ΔT data to identify the maximum temperature change for each composition at the specified stress. These peak values will be compared to a reference (using appropriate tolerances) and awarded a share of the total score. Additionally, the verifier will check that the observed peaks occur in the vicinity of the respective zero-stress Curie temperatures (as determined by the material parameters). The final reward is a weighted combination of these checks.
