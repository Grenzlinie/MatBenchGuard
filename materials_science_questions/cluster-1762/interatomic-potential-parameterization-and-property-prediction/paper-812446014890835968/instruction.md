# Raman Frequency of Fluorite Solids from Lundqvist Potential with Three-Body and Thermal Effects

## Problem background
Fluorite-type ionic crystals (CaF₂, SrF₂, BaF₂) exhibit a characteristic Raman‑active vibrational mode whose frequency is sensitive to interatomic forces. Simple two‑body central potentials fail to reproduce experimental elastic constants and Raman frequencies, and earlier theoretical treatments that omitted many‑body (three‑body) interactions and thermal phonon pressure also gave unsatisfactory agreement. This work addresses the question: what room‑temperature Raman frequencies are obtained from a potential model that explicitly includes three‑body interactions and thermal phonon pressure? The answer is a critical test of the improved force model.

## Approach
The method employs the Lundqvist potential model for the lattice energy, which combines a Coulomb term (including a Madelung constant and an exchange‑charge parameter that captures charge transfer) with short‑range repulsive potentials between first and second neighbours. Three‑body interactions are incorporated via the exchange‑charge formalism, and thermal phonon pressure is included through a term proportional to the thermal expansion coefficient and bulk modulus. Closed‑form expressions for the three second‑order elastic constants (C₁₁, C₁₂, C₄₄) are obtained in terms of the short‑range potential parameters (strength b, hardness ρ) and the derivative of the exchange‑charge parameter, f′. Using experimentally measured C₁₁ and C₁₂ as input, the three unknown parameters b, ρ, and f′ are determined by solving the resulting equations. The experimental C₄₄ is then used as a consistency condition to select a physically reasonable ρ. Once the potential is parameterised, the principal Raman frequency is computed from a formula that combines repulsive and three‑body coupling coefficients. For comparison, the prediction of a simpler pairwise Born central‑force model is also computed.

## Reproduction target
Compute the principal Raman frequency (in cm⁻¹) at 298 K for CaF₂, SrF₂, and BaF₂ using the Lundqvist potential model with three‑body interactions and thermal phonon pressure. The calculation must use experimentally measured lattice constants, second‑order elastic constants (C₁₁, C₁₂, C₄₄), and thermal expansion coefficients, together with tabulated ionic radii and valence properties. Short‑range potential parameters and the exchange‑charge derivative must be obtained by fitting the model to the experimental C₁₁ and C₁₂, with C₄₄ employed as a consistency check. Write the three resulting Raman frequencies to a JSON file.

## Assets

- Experimental elastic constants and lattice parameters for CaF2, SrF2, BaF2 at room temperature
- Ionic radii, valencies, and valence electron numbers for Ca, Sr, Ba, F
- Physical constants and Madelung constant for fluorite lattice
- Python scientific computing libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Collect experimental input data
- Role: process
- Action: Assemble the necessary experimental input data for CaF2, SrF2, and BaF2 from standard public reference sources: lattice constant a, second-order elastic constants C11, C12, C44, thermal expansion coefficient β at 298 K, ionic radii r1 (Ca/Sr/Ba), r2 (F⁻), valencies Z1, Z2, numbers of valence electrons n1, n2, mass of fluorine mF, electronic charge e, and Madelung constant α_m for the fluorite structure.
- Evidence: `/app/outputs/input_data.json`

### Step 2: Fit interatomic potential parameters
- Role: process
- Action: Implement the Lundqvist potential model and the derived expressions for second-order elastic constants C11 and C12 (including thermal phonon pressure and three-body interactions) for fluorite-type crystals. For each compound, use the experimental C11 and C12 values to solve for the short-range repulsive potential parameters b, ρ, and the exchange-charge derivative f'. Use the relations A1 = -(a√3)/(2ρ) B1, A2 = -(a/ρ) B2, and the ratio B2/B1. Employ C44 as a consistency condition to select a physically reasonable ρ.
- Evidence: `/app/outputs/fitted_params.json`

### Step 3: Compute Raman frequency
- Role: scored (load-bearing)
- Action: Using the fitted potential parameters from step_02_fit_params and the derived Raman frequency expression that combines repulsive and three-body coupling coefficients, compute the principal Raman frequency WR (in cm⁻¹) for CaF2, SrF2, and BaF2 at 298 K. Write the three values to a JSON file.
- Output file: `/app/outputs/raman_frequencies.json`
- Format: json
- Contract: {"CaF2": number, "SrF2": number, "BaF2": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_frequencies.json
- path: `/app/outputs/raman_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Principal Raman frequencies (in cm⁻¹) for CaF2, SrF2, and BaF2 at 298 K computed with the Lundqvist potential including three-body interactions and thermal phonon pressure.
- schema:
  - `type`: object
  - `required`:
    - `CaF2`: number
    - `SrF2`: number
    - `BaF2`: number
  - `units`:
    - `CaF2`: cm^-1
    - `SrF2`: cm^-1
    - `BaF2`: cm^-1

Notes: The checker compares the three values against hidden reference values with an absolute tolerance. The fitting procedure must be executed by the agent; no pre-fitted parameters are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "CaF2": "number",
          "SrF2": "number",
          "BaF2": "number"
        },
        "units": {
          "CaF2": "cm^-1",
          "SrF2": "cm^-1",
          "BaF2": "cm^-1"
        }
      },
      "description": "Principal Raman frequencies (in cm⁻¹) for CaF2, SrF2, and BaF2 at 298 K computed with the Lundqvist potential including three-body interactions and thermal phonon pressure."
    }
  ],
  "notes": "The checker compares the three values against hidden reference values with an absolute tolerance. The fitting procedure must be executed by the agent; no pre-fitted parameters are provided."
}
```

## How you are scored
A hidden verifier reads your submitted raman_frequencies.json and compares each reported frequency against independently computed reference values. The comparison uses an absolute tolerance that accounts for legitimate variations arising from the choice of input data sources and numerical solution methods. Full credit is awarded when all three frequencies fall within the tolerance band; partial credit is given proportionally based on how many compounds satisfy the tolerance. Simply reporting known published numbers is insufficient—you must carry out the parameter fitting and Raman frequency computation yourself.
