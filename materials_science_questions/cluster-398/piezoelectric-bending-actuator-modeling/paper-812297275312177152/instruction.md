# Compute low-frequency phase response of PZT cylindrical shell fiber phase modulator

## Problem background
Optical fibre interferometric sensors often employ a thin‑shell piezoelectric (PZT) cylindrical phase modulator to demodulate sensing signals. Accurately predicting the phase response of such a modulator as a function of applied voltage and driving frequency is essential for sensor design and signal processing. The problem is to derive the transfer function that relates the electrical input to the optical phase shift produced in a fibre wound tightly around the PZT cylinder. A comprehensive model couples the piezoelectric constitutive equations governing the radial motion of the cylindrical shell with the strain‑optic phase shift induced in the optical fibre. This model, together with an earlier expression that uses a different piezoelectric constant, yields predictions of the low‑frequency phase sensitivity for representative PZT materials. Reproducing these derived sensitivities by computation verifies the analytical formulation and serves as a benchmark for comparing the two modelling approaches.

## Approach
The computational approach consists of two parallel evaluations.

1.  **Paper’s transfer‑function model (uses d₃₁).**  Starting from the piezoelectric equations for a thin radially symmetric shell, the radial displacement under a harmonic electric field is obtained by solving the equation of motion, which includes inertial, elastic, and (if considered) damping terms.  For frequencies far below the mechanical resonance, the displacement simplifies to a constant proportional to the applied voltage and inversely proportional to the cylinder thickness.  The radial strain couples to a circumferential length change of the fibre, which, via the strain‑optic effect, produces an optical phase shift.  The final low‑frequency sensitivity per volt‑turn depends on the piezoelectric constant d₃₁, the density ρ and elastic modulus C₁₁ᴱ of the PZT material, the cylinder’s mean radius r and thickness t, the free‑space wavelength λ, the fibre core refractive index n, the fibre length per turn L, and the elasto‑optic coefficients P₁₁, P₁₂ and Poisson’s ratio ν of the fibre.  The resonance frequency of the shell is also computed.

2.  **De Paula expression (uses d₃₃).**  An earlier model expresses the phase shift per volt‑turn in terms of the piezoelectric constant d₃₃, the free‑space wave number, the fibre refractive index, and the fibre’s elasto‑optic coefficients.  This expression does not involve the cylinder thickness or the fibre length per turn.

Both models are evaluated for two common piezoelectric ceramics—PZT‑4 and PZT‑5A—using publicly available material constants and standard optical fibre parameters.  The required constants (ρ, C₁₁ᴱ, d₃₁, d₃₃) are obtained from open piezoelectric material datasheets; the fibre parameters are well‑established in the literature and can be hard‑coded.

## Reproduction target
Compute, using the low‑frequency limit of the derived transfer function and the De Paula expression, the phase response per volt‑turn (rad V⁻¹ turn⁻¹) for two PZT samples:
- Sample I: PZT‑4, outer diameter 1.5 inch, thickness 0.19 cm.
- Sample II: PZT‑5A, outer diameter 1.5 inch, thickness 0.326 cm.
For the paper’s model also compute the resonance frequency (Hz).

All necessary material constants for PZT‑4 and PZT‑5A must be fetched from public datasheets (e.g., APC International).  The standard fibre parameters to use are: core refractive index n = 1.46, free‑space wavelength λ = 0.83 µm, elasto‑optic coefficients P₁₁ = 0.121, P₁₂ = 0.270, Poisson’s ratio ν = 0.17.  The fibre length per turn is calculated from the mean diameter as π × (outer diameter − thickness).

Output the results in two CSV files:
- `phase_response_d31.csv` (d₃₁ model: low‑frequency sensitivity and resonance frequency for each sample).
- `phase_response_de_paula.csv` (d₃₃ model: low‑frequency sensitivity for each sample).

A hidden verifier will compare the computed sensitivities and the resonance frequency against expected values; the exact target values are not revealed here.

## Assets

- PZT material properties (d31, d33, density, elastic modulus C11^E for PZT-4 and PZT-5A): https://www.americanpiezo.com/
- Silica optical fiber parameters
- Python scientific computing stack: numpy scipy

## Workflow steps

### Step 1: Compute phase response using paper's transfer function (d31)
- Role: scored
- Action: Compute the low-frequency phase response per volt‑turn (rad/(V·turn)) and the resonance frequency (Hz) for Sample I (PZT‑4) and Sample II (PZT‑5A) using the low‑frequency limit of the derived transfer function. The transfer function is obtained by combining the radial displacement of the PZT shell (piezoelectric equations, Newton's law) with the fiber phase shift, and simplifies in the low‑frequency regime to the expression:

    Δφ/V = (2π/(λ t)) n L d31 {1 + (n²/2)[(P11+P12)ν − P12]}.

    The resonance angular frequency is ω₀² = 1/(ρ r² C₁₁ᴱ). Hard‑code the standard fiber parameters (λ=0.83 µm, n=1.46, P11=0.121, P12=0.270, ν=0.17). Obtain ρ, C11^E, and d31 for PZT‑4 and PZT‑5A from publicly available piezoelectric material datasheets (e.g., APC International). Calculate the mean radius r from the outer diameter and thickness, and the fiber length per turn L as π × (outer diameter − thickness). Use the sample dimensions: Sample I has outer diameter 1.5 inch (0.0381 m), thickness 0.19 cm; Sample II has outer diameter 1.5 inch, thickness 0.326 cm. Compute the resonance frequency f0 = ω0/(2π) using ω0² = 1/(ρ r² C11^E). Output the results in CSV format.
- Output file: `/app/outputs/phase_response_d31.csv`
- Format: csv
- Contract: Columns: Sample (string, values 'I'/'II'), Material (string, values 'PZT-4'/'PZT-5A'), LowFreqPhaseResponse_rad_per_V_turn (float), ResonanceFrequency_Hz (float). Units: rad/(volt‑turn) for phase response, Hz for frequency.
- Scoring: scored by hidden verifier

### Step 2: Compute phase response using De Paula's expression (d33)
- Role: scored
- Action: Using the expression from an earlier model by De Paula and More, compute the phase response per volt‑turn (rad/(V·turn)) for the same two samples. The expression relates phase response to the piezoelectric constant d33, the free‑space wave number k0, fiber core refractive index n, fiber elasto‑optic coefficients P11, P12, Poisson's ratio ν, and the number of fiber turns N. Specifically, the phase shift per volt‑turn is φ/(V N) = 2π k0 n d33 {1 − (n²/2)[P11 − (P11+P12)ν]}. Use the same fiber parameters and the sample dimensions to determine the number of turns N (N = 1 for a single turn) — note that the computation does not depend on fiber length L or PZT thickness t. Obtain d33 for PZT‑4 and PZT‑5A from the same public datasheets. Output the results in CSV format.
- Output file: `/app/outputs/phase_response_de_paula.csv`
- Format: csv
- Contract: Columns: Sample (string, values 'I'/'II'), Material (string, values 'PZT-4'/'PZT-5A'), LowFreqPhaseResponse_rad_per_V_turn (float). Unit: rad/(volt‑turn).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_response_d31.csv`
- `/app/outputs/phase_response_de_paula.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_response_d31.csv
- path: `/app/outputs/phase_response_d31.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed low‑frequency phase sensitivity (paper's d31 model) and resonance frequency for Sample I (PZT-4) and Sample II (PZT-5A).
- schema:
  - `type`: table
  - `required_columns`: `Sample`, `Material`, `LowFreqPhaseResponse_rad_per_V_turn`, `ResonanceFrequency_Hz`
  - `units`:
    - `LowFreqPhaseResponse_rad_per_V_turn`: rad/(volt-turn)
    - `ResonanceFrequency_Hz`: Hz

### phase_response_de_paula.csv
- path: `/app/outputs/phase_response_de_paula.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed low‑frequency phase sensitivity using De Paula's expression (d33) for the two samples.
- schema:
  - `type`: table
  - `required_columns`: `Sample`, `Material`, `LowFreqPhaseResponse_rad_per_V_turn`
  - `units`:
    - `LowFreqPhaseResponse_rad_per_V_turn`: rad/(volt-turn)

Notes: The checker will compare the computed values to the paper's reported theoretical sensitivities with appropriate tolerances. Both files must have exactly two rows (one per sample) with the required columns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_response_d31.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Sample",
          "Material",
          "LowFreqPhaseResponse_rad_per_V_turn",
          "ResonanceFrequency_Hz"
        ],
        "units": {
          "LowFreqPhaseResponse_rad_per_V_turn": "rad/(volt-turn)",
          "ResonanceFrequency_Hz": "Hz"
        }
      },
      "description": "Computed low‑frequency phase sensitivity (paper's d31 model) and resonance frequency for Sample I (PZT-4) and Sample II (PZT-5A)."
    },
    {
      "file": "phase_response_de_paula.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Sample",
          "Material",
          "LowFreqPhaseResponse_rad_per_V_turn"
        ],
        "units": {
          "LowFreqPhaseResponse_rad_per_V_turn": "rad/(volt-turn)"
        }
      },
      "description": "Computed low‑frequency phase sensitivity using De Paula's expression (d33) for the two samples."
    }
  ],
  "notes": "The checker will compare the computed values to the paper's reported theoretical sensitivities with appropriate tolerances. Both files must have exactly two rows (one per sample) with the required columns."
}
```

## How you are scored
Each scored workflow stage produces one output CSV file that is independently inspected by a hidden verifier.  The verifier reads the contents of `phase_response_d31.csv` and `phase_response_de_paula.csv` and compares the computed low‑frequency phase sensitivity values and (for the d₃₁ file) the resonance frequency against hidden reference values.  The comparison uses tolerances that account for small differences in material constants obtained from different datasheets and for rounding.

The final reward is a weighted combination of the scores for the two stages.  The d₃₁‑model stage carries a higher weight than the De‑Paula stage.  To achieve a high score, the computations must faithfully implement the models and use correct material constants; simply writing a number without performing the calculation, or copying a reported value from the literature, will not match the hidden references.
