# Kinetic parameter determination and TTT diagram reconstruction for MnAl ε→τ solid-state transformation

## Problem background
The metastable ferromagnetic τ phase (L1₀ structure) in Mn‑Al‑C alloys offers attractive magnetic properties, but its formation during solidification or solid‑state processing is controlled by the competition between thermodynamics and kinetics. Understanding the ε→τ solid‑state transformation is critical for designing heat treatments that either promote or suppress the τ phase. This task focuses on reconstructing the complete temperature‑time‑transformation (TTT) diagram for the ε→τ reaction in a Mn₀.₅₅Al₀.₄₃₃C₀.₀₁₇ alloy from reported thermodynamic data and published isothermal transformation times. The goal is to determine the key kinetic parameters governing the transformation and to estimate the critical cooling rate required to bypass τ‑phase nucleation.

## Approach
The approach combines thermodynamic driving‑force calculations with kinetic nucleation‑growth modeling. First, using measured heats of transformation and fusion, the molar Gibbs free energy difference ΔG^{ε→τ} and the volumetric driving force ΔG_V^{ε→τ} are computed as functions of temperature via a linear approximation. Second, experimental τ‑start times (for 1% volume fraction) in the low‑temperature regime (625–700 K) are obtained from Dreizler & Menth (1980) to serve as the primary kinetic data. A linear least‑squares fit of ln(t) vs 1/T in this regime yields initial estimates for the pre‑exponential factor and the activation energy term. Those estimates are then refined by a nonlinear regression that incorporates the full nucleation‑growth kinetic equation, which includes a term related to the solid‑solid interfacial energy. The fitted parameters allow full reconstruction of the TTT curve over a wide temperature range. From the TTT curve’s nose coordinates, the critical cooling rate for avoiding τ‑phase formation during solid‑state cooling can be estimated.

## Reproduction target
Reproduce the three kinetic parameters that govern the ε→τ transformation: the logarithmic pre‑exponential factor ln A₃ (s⁻¹), the activation energy term Q/k (K), and the interfacial energy term bσ³f(θ)/4k (K J² m⁻⁶). Also compute the range of the interfacial energy σ (J m⁻²) derived from the interfacial energy term using a shape‑factor interval f(θ) ∈ [0.1, 0.9] and the geometrical factor b = 16π/3. Finally, from the fully parameterized TTT diagram, estimate the critical cooling rate (K s⁻¹) that avoids τ‑phase nucleation. All computational inputs are public: the thermodynamic measurements reported for this alloy composition and the τ‑start times from the literature.

## Assets

- Python scientific stack (numpy, scipy, matplotlib): numpy scipy matplotlib
- Dreizler & Menth τ‑start times for ε→τ transformation in Mn‑Al‑C alloy: 10.1109/TMAG.1980.1060649

## Workflow steps

### Step 1: Compute thermodynamic driving force functions
- Role: process
- Action: Using the provided calorimetric data (ΔH_t^{τ→ε}=1992 J mol⁻¹, T_t^{τ/ε}=1068 K, ΔH_f^{ε→l}=10500 J mol⁻¹, T_0^{ε/l}≈1490 K) and the linear approximation for ΔG, compute the molar Gibbs free energy differences ΔG^{τ→ε}(T) and ΔG^{ε→τ}(T). Convert to volumetric driving force ΔG_V^{ε→τ}(T) using the τ‑phase lattice parameters a0=0.2769 nm, c0=0.3618 nm. Also compute the critical temperature T_0^{τ/l}=1403 K and minimum undercooling ΔT=87 K.
- Evidence: `/app/outputs/driving_force_functions.json`

### Step 2: Extract experimental τ‑start times from Dreizler & Menth
- Role: process
- Action: Obtain the isothermal τ‑start transformation times (1% volume fraction) in the 625–700 K range from Dreizler & Menth (1980). Create a CSV file with columns `T` (K) and `t` (s).
- Evidence: `/app/outputs/tau_start_data.csv`

### Step 3: Fit kinetic parameters (ln A₃, Q/k, bσ³f(θ)/4k)
- Role: scored
- Action: Perform a linear least‑squares fit of ln(t) vs 1/T using the low‑temperature τ‑start data to obtain initial values for ln A₃ and Q/k. Then, using the full nucleation‑growth kinetic equation (eq. 13) together with the ΔG^{ε→τ}(T) and ΔG_V^{ε→τ}(T) functions, perform a nonlinear regression over all available τ‑start time data to determine the interfacial energy term bσ³f(θ)/4k. Save the three parameters in a JSON file.
- Output file: `/app/outputs/kinetic_parameters.json`
- Format: json
- Contract: {"ln_A3": <float>, "Q_over_k": <float>, "b_sigma3_f_over_4k": <float>}
- Scoring: scored by hidden verifier

### Step 4: Compute interfacial energy range σ
- Role: scored
- Action: From the fitted term bσ³f(θ)/4k, compute the minimum and maximum interfacial energy σ (J m⁻²) using the geometrical factor b = 16π/3 and the shape‑factor range f(θ) ∈ [0.1, 0.9].
- Output file: `/app/outputs/interfacial_energy_range.json`
- Format: json
- Contract: {"sigma_min": <float>, "sigma_max": <float>}
- Scoring: scored by hidden verifier

### Step 5: Compute complete TTT curve
- Role: process
- Action: Using the fully parameterised kinetic equation (A₃, Q/k, bσ³f(θ)/4k) together with the ΔG_V^{ε→τ}(T) function, calculate the τ‑start transformation time as a function of temperature over a range spanning at least 550–1050 K. Identify the nose coordinates (time, temperature). Save the curve data to a CSV file.
- Evidence: `/app/outputs/ttt_curve.csv`

### Step 6: Estimate critical cooling rate
- Role: scored (load-bearing)
- Action: From the computed TTT curve, estimate the critical cooling rate (K s⁻¹) required to avoid τ‑phase nucleation during solid‑state cooling, using the nose temperature and an appropriate temperature span between the nose and liquidus. Save the value in a JSON file.
- Output file: `/app/outputs/critical_cooling_rate.json`
- Format: json
- Contract: {"critical_cooling_rate": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kinetic_parameters.json`
- `/app/outputs/interfacial_energy_range.json`
- `/app/outputs/critical_cooling_rate.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kinetic_parameters.json
- path: `/app/outputs/kinetic_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted kinetic parameters for the ε→τ transformation: pre‑exponential factor, activation energy term, and interfacial energy term.
- schema:
  - `type`: object
  - `required`: `ln_A3`, `Q_over_k`, `b_sigma3_f_over_4k`
  - `properties`:
    - `ln_A3`:
      - `type`: number
      - `units`: s⁻¹
    - `Q_over_k`:
      - `type`: number
      - `units`: K
    - `b_sigma3_f_over_4k`:
      - `type`: number
      - `units`: K J² m⁻⁶

### interfacial_energy_range.json
- path: `/app/outputs/interfacial_energy_range.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated range of the interfacial energy σ, derived from the kinetic fit and assumed shape‑factor bounds.
- schema:
  - `type`: object
  - `required`: `sigma_min`, `sigma_max`
  - `properties`:
    - `sigma_min`:
      - `type`: number
      - `units`: J m⁻²
    - `sigma_max`:
      - `type`: number
      - `units`: J m⁻²

### critical_cooling_rate.json
- path: `/app/outputs/critical_cooling_rate.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Critical cooling rate required to bypass τ‑phase nucleation during solid‑state cooling, computed from the full TTT diagram.
- schema:
  - `type`: object
  - `required`: `critical_cooling_rate`
  - `properties`:
    - `critical_cooling_rate`:
      - `type`: number
      - `units`: K s⁻¹

Notes: All numerical comparisons are based on hidden tolerances appropriate for the digitisation and fitting variability. The critical cooling rate is evaluated in a threshold‑or‑better manner to avoid penalising estimates that are safely above the reported value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kinetic_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "ln_A3",
          "Q_over_k",
          "b_sigma3_f_over_4k"
        ],
        "properties": {
          "ln_A3": {
            "type": "number",
            "units": "s⁻¹"
          },
          "Q_over_k": {
            "type": "number",
            "units": "K"
          },
          "b_sigma3_f_over_4k": {
            "type": "number",
            "units": "K J² m⁻⁶"
          }
        }
      },
      "description": "Fitted kinetic parameters for the ε→τ transformation: pre‑exponential factor, activation energy term, and interfacial energy term."
    },
    {
      "file": "interfacial_energy_range.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "sigma_min",
          "sigma_max"
        ],
        "properties": {
          "sigma_min": {
            "type": "number",
            "units": "J m⁻²"
          },
          "sigma_max": {
            "type": "number",
            "units": "J m⁻²"
          }
        }
      },
      "description": "Estimated range of the interfacial energy σ, derived from the kinetic fit and assumed shape‑factor bounds."
    },
    {
      "file": "critical_cooling_rate.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "critical_cooling_rate"
        ],
        "properties": {
          "critical_cooling_rate": {
            "type": "number",
            "units": "K s⁻¹"
          }
        }
      },
      "description": "Critical cooling rate required to bypass τ‑phase nucleation during solid‑state cooling, computed from the full TTT diagram."
    }
  ],
  "notes": "All numerical comparisons are based on hidden tolerances appropriate for the digitisation and fitting variability. The critical cooling rate is evaluated in a threshold‑or‑better manner to avoid penalising estimates that are safely above the reported value."
}
```

## How you are scored
A hidden verifier reads your submitted JSON artifacts and compares them against independently determined reference values. Each scored artifact contributes a weighted portion to the final reward (0 to 1). The kinetic parameters are evaluated on their numerical agreement with reference values within appropriate tolerances. The interfacial energy range is checked for consistency with the fitted term. The critical cooling rate is compared against a reference threshold using a directional check: a rate at or above the threshold earns full credit, while a rate below the threshold is penalized. The verifier does not require an exact match to any particular published figure, but your results must follow from the prescribed workflow and be physically plausible. Submitting only the expected numbers without following the process steps will not produce the required intermediate evidence and will fail the verification.
