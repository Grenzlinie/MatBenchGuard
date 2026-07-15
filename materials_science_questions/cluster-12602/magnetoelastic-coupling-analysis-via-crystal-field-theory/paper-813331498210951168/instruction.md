# Crystal Field Susceptibility and Elastic Constant Computation

## Problem background
The rare-earth clathrate compound Pr₃Pd₂₀Ge₆ exhibits pronounced elastic softening at low temperatures. The crystal contains two inequivalent Pr³⁺ sites (4a and 8c) where the 4f electrons experience crystalline electric fields (CEF) that partially lift the ninefold J=4 multiplet. The elastic constants (C₁₁−C₁₂)/2 and C₄₄ are strongly temperature-dependent, and this softening can be modelled by quadrupole susceptibilities arising from the CEF level schemes. The task is to compute the quadrupole susceptibilities and the resulting elastic constants from first principles, providing the theoretical curves that would be compared with ultrasonic measurements.

## Approach
Construct the CEF Hamiltonian for each site using Stevens operators: H_CEF = B₄ (O₄⁰ + 5 O₄⁴) + B₆ (O₆⁰ − 21 O₆⁴). Diagonalise this 9×9 Hamiltonian for Pr³⁺ (J=4) to obtain eigenenergies and eigenvectors. The quadrupole susceptibility for a given symmetry channel Γ (Γ₃ for O_v = J_x²−J_y², Γ₅ for O_zx = J_zJ_x+J_xJ_z) is then evaluated at each temperature T by combining a temperature-independent van Vleck term (thermal average of the second strain derivative of the energy) and a Curie term proportional to 1/T (variance of the first strain derivative). The first strain derivative ∂E/∂ε_Γ is proportional to the matrix element of the corresponding quadrupole operator, with proportionality constant g_Γ, so the computation reduces to evaluating thermal averages of the quadrupole operators and their squares in the CEF basis. Finally, the elastic constants C_Γ(T) for the Γ₃ channel ((C₁₁−C₁₂)/2) and the Γ₅ channel (C₄₄) are obtained by the two-site weighted-sum formula: C_Γ(T) = C⁰_Γ − (N/3)[g²_Γ[4a] χ_Γ[4a] / (1 − g′_Γ[4a] χ_Γ[4a])] − (2N/3)[g²_Γ[8c] χ_Γ[8c] / (1 − g′_Γ[8c] χ_Γ[8c])], with a temperature-dependent background C⁰_Γ = a + bT + cT². Use the following parameters (all from published experimental data):

- Total Pr³⁺ number density N = 6.225×10²⁷ m⁻³ (N/3 = 2.075×10²⁷ m⁻³ for the 4a site, 2N/3 = 4.151×10²⁷ m⁻³ for the 8c site).
- CEF parameters:
  · 4a site: B₄ = 2.570×10⁻² K, B₆ = −3.860×10⁻⁴ K.
  · 8c site: B₄ = 2.243×10⁻² K, B₆ = −4.363×10⁻⁴ K.
- Background and coupling constants for Γ₃ (channel for (C₁₁−C₁₂)/2):
  · a = 3.717×10¹⁰ J/m³, b = −1×10⁷ J/(K·m³), c = −9×10³ J/(K²·m³).
  · |g_{Γ₃}[4a]| = 30 K, g′_{Γ₃}[4a] = 0 K.
  · |g_{Γ₃}[8c]| = 90 K, g′_{Γ₃}[8c] = −0.036 K.
- Background and coupling constants for Γ₅ (channel for C₄₄):
  · a = 3.585×10¹⁰ J/m³, b = −1×10³ J/(K·m³), c = −3.5×10⁴ J/(K²·m³).
  · |g_{Γ₅}[4a]| = 31 K, g′_{Γ₅}[4a] = 0.013 K.
  · |g_{Γ₅}[8c]| = 13 K, g′_{Γ₅}[8c] = −0.030 K.

## Reproduction target
Produce the two scored output files: (1) quadrupole_susceptibilities.csv containing the dimensionless quadrupole susceptibilities −χ_{Γ₃} and −χ_{Γ₅} for both the 4a and 8c sites; (2) elastic_constants.csv containing the elastic constants (C₁₁−C₁₂)/2 and C₄₄ as functions of temperature over the range 0.1 K to 50 K, with at least 20 temperature points. The results should faithfully represent the temperature-dependent softening predicted by the CEF model described above.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve CEF Hamiltonian
- Role: process
- Action: Construct the crystal electric field (CEF) Hamiltonian for Pr3+ (J=4) on the 4a and 8c crystallographic sites using Stevens operators and the published B4, B6 parameters. Diagonalize the Hamiltonian to obtain eigenenergies and eigenstates.
- Evidence: `/app/outputs/cef_eigensystem.npz`

### Step 2: Compute quadrupole susceptibilities
- Role: scored
- Action: Using the eigenstates from the previous step, compute the temperature-dependent quadrupole susceptibilities -χ_Γ3 (for the O_v quadrupole operator) and -χ_Γ5 (for the O_zx operator) for both sites over the range 0.1–50 K using the quadrupole susceptibility formula with van Vleck and Curie terms (as described in the Approach section).
- Output file: `/app/outputs/quadrupole_susceptibilities.csv`
- Format: csv
- Contract: CSV with columns: temperature (K), chi_Gamma3_4a, chi_Gamma3_8c, chi_Gamma5_4a, chi_Gamma5_8c. All susceptibility values are dimensionless.
- Scoring: scored by hidden verifier

### Step 3: Compute elastic constants
- Role: scored (load-bearing)
- Action: Using the susceptibilities from the previous step, the given background elastic constant parameters (a, b, c), the Pr3+ ion number density N, and the coupling constants g_Γ and g_Γ' for each site and symmetry channel, compute the elastic constants (C11-C12)/2 (Γ3 channel) and C44 (Γ5 channel) as functions of temperature via the two-site weighted-sum formula given in the Approach section.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns: temperature (K), C_Gamma3 (J/m^3), C_Gamma5 (J/m^3).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quadrupole_susceptibilities.csv`
- `/app/outputs/elastic_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quadrupole_susceptibilities.csv
- path: `/app/outputs/quadrupole_susceptibilities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quadrupole susceptibilities -χ_Γ3 and -χ_Γ5 for the 4a and 8c sites over the temperature range 0.1–50 K. The checker will recompute these values from the same CEF parameters and compare.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `chi_Gamma3_4a`, `chi_Gamma3_8c`, `chi_Gamma5_4a`, `chi_Gamma5_8c`
  - `units`:
    - `temperature`: K
    - `chi_Gamma3_4a`: dimensionless
    - `chi_Gamma3_8c`: dimensionless
    - `chi_Gamma5_4a`: dimensionless
    - `chi_Gamma5_8c`: dimensionless

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants (C11-C12)/2 (Γ3 channel) and C44 (Γ5 channel) as functions of temperature. The checker will recompute these from the susceptibilities and the published coupling constants and background parameters.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `C_Gamma3`, `C_Gamma5`
  - `units`:
    - `temperature`: K
    - `C_Gamma3`: J/m^3
    - `C_Gamma5`: J/m^3

Notes: All parameters (B4, B6, a, b, c, g, g', N) are taken from the paper's Table I and text, and are thus publicly available. The temperature range is 0.1–50 K with at least 20 points. The checker will independently diagonalize the CEF Hamiltonian and compute the same quantities for comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quadrupole_susceptibilities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "chi_Gamma3_4a",
          "chi_Gamma3_8c",
          "chi_Gamma5_4a",
          "chi_Gamma5_8c"
        ],
        "units": {
          "temperature": "K",
          "chi_Gamma3_4a": "dimensionless",
          "chi_Gamma3_8c": "dimensionless",
          "chi_Gamma5_4a": "dimensionless",
          "chi_Gamma5_8c": "dimensionless"
        }
      },
      "description": "Quadrupole susceptibilities -χ_Γ3 and -χ_Γ5 for the 4a and 8c sites over the temperature range 0.1–50 K. The checker will recompute these values from the same CEF parameters and compare."
    },
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "C_Gamma3",
          "C_Gamma5"
        ],
        "units": {
          "temperature": "K",
          "C_Gamma3": "J/m^3",
          "C_Gamma5": "J/m^3"
        }
      },
      "description": "Elastic constants (C11-C12)/2 (Γ3 channel) and C44 (Γ5 channel) as functions of temperature. The checker will recompute these from the susceptibilities and the published coupling constants and background parameters."
    }
  ],
  "notes": "All parameters (B4, B6, a, b, c, g, g', N) are taken from the paper's Table I and text, and are thus publicly available. The temperature range is 0.1–50 K with at least 20 points. The checker will independently diagonalize the CEF Hamiltonian and compute the same quantities for comparison."
}
```

## How you are scored
Both output files are scored by a hidden verifier. The verifier independently recomputes the quadrupole susceptibilities and elastic constants using the same parameters and formulas, then compares your submitted values point‑by‑point against its own reference values. The score for each file is the fraction of compared temperature points that fall within a preset tolerance; the two file scores are combined with weighting, with the elastic constants carrying a higher weight. Reporting a value alone is not sufficient—the underlying computation must produce the correct temperature dependence.
