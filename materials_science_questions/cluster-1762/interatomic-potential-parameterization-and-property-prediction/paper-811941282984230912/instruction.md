# Central-Force Potential Fitting and High-Pressure Shear Instability Prediction for Alkali Halides

## Problem background
The elastic properties of minerals at high pressure and temperature are essential for understanding the composition and dynamics of the Earth's interior. Reliable extrapolation of laboratory measurements to deep-Earth conditions requires physically motivated interatomic potential models. This task focuses on the NaCl-type alkali halides, which serve as benchmark systems for testing central-force lattice models. Using a model that includes electrostatic, Born-Mayer nearest-neighbor repulsion, and Lennard-Jones next-nearest-neighbor anion interactions, we can quantitatively connect ambient-condition elastic constants and their pressure derivatives to high-pressure shear behavior. The goal is to predict the pressure at which a shear instability signals a structural phase transition from the NaCl (B1) to the CsCl (B2) structure for two compounds where this transition is not yet well established.

## Approach
The approach is built on a central-force interatomic potential for the NaCl lattice. The energy per ion pair consists of three contributions: (i) a long-range Coulomb term with an effective ionic charge Z; (ii) a Born-Mayer repulsion between nearest neighbours characterized by a pre-exponential factor b and a range parameter ρ; (iii) a Lennard-Jones 6-12 potential between next-nearest-neighbour anions, with a well depth ε₀ and equilibrium separation rₘ. From this energy expression one derives closed-form equations for the static-lattice (zero-temperature) pressure, isothermal bulk modulus, and the two shear moduli C₄₄ and C_s, together with their pressure derivatives. These five quantities are nonlinear functions of the five unknown parameters.

Room-temperature experimental data for three compounds — NaCl, KF, and NaF — are provided in the instructions: the nearest-neighbour distance, thermal expansion coefficient, a Debye-model vibrational energy factor W_V/TC_V, the measured isothermal bulk modulus, shear moduli, and their temperature and pressure derivatives. Thermal corrections based on the Mie–Grüneisen equation of state and the Debye model are applied to remove the vibrational contributions and obtain the static-lattice counterparts P̃, K̃, C̃₄₄, C̃_s and their pressure derivatives.

The five potential parameters are then determined for each compound by solving a system of five nonlinear equations that enforce equality between the model's static-lattice expressions and the experimentally derived static-lattice target values. This is performed numerically (e.g., with SciPy’s fsolve).

Once the model parameters are fitted, the equations are used to compute the shear modulus C₄₄ as a function of pressure for KF and NaF. The phase transition pressure is identified as the pressure at which the ratio C₄₄/K reaches the critical value α that is known from compounds where the transition pressure has been measured: α = 0.13 for KF and α = 0.14 for NaF. The pressure where C₄₄ itself vanishes provides an upper bound on the macroscopic instability.

### Model equations

The static-lattice (zero-temperature) quantities P̃, K̃, C̃44, C̃s, K̃′, C̃44′, C̃_s′ are derived from the central-force potential. The expressions below are evaluated with r = r₀ (the room-temperature nearest-neighbor distance, given in Table 1) during the fitting step, and with variable r for the high-pressure calculations. The variable r′ = √2 r. All quantities are in cgs units; the elementary charge e = 4.80320425 × 10⁻¹⁰ esu. Pressures and moduli in the formulas are in dyn cm⁻²; to convert to kb divide by 10⁹.

**Static-lattice pressure**

\[
\tilde{P} = \frac{1}{2 r_0^3}\left[ -0.58252\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 + 2b\,\frac{r_0}{\rho}\left(\frac{r_0}{r}\right)^2 e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(48\left(\frac{r_m}{r'}\right)^{15} - 48\left(\frac{r_m}{r'}\right)^9\right) \right]
\]

**Static-lattice bulk modulus**

\[
\tilde{K} = \frac{1}{2 r_0^3}\left[ -0.77669\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 + \frac{2}{3}b\,\frac{r_0}{\rho}\left(2\left(\frac{r_0}{r}\right)^2 + \frac{r_0}{\rho}\frac{r_0}{r}\right) e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(240\left(\frac{r_m}{r'}\right)^{15} - 144\left(\frac{r_m}{r'}\right)^9\right) \right]
\]

**Static-lattice shear modulus C̃44**

\[
\tilde{C}_{44} = \frac{1}{2 r_0^3}\left[ 1.27802\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 - 2b\,\frac{r_0}{\rho}\left(\frac{r_0}{r}\right)^2 e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(120\left(\frac{r_m}{r'}\right)^{15} - 48\left(\frac{r_m}{r'}\right)^9\right) \right]
\]

**Static-lattice shear modulus C̃_s**

\[
\tilde{C}_s = \frac{1}{2 r_0^3}\left[ -1.22153\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 + b\,\frac{r_0}{\rho}\left(\frac{r_0}{\rho}\frac{r_0}{r} - \left(\frac{r_0}{r}\right)^2\right) e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(36\left(\frac{r_m}{r'}\right)^{15}\right) \right]
\]

**Pressure derivative of the bulk modulus**

\[
\tilde{K}' = \frac{1}{6 \tilde{K} r_0^3}\left[ -3.1068\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 + \frac{2}{3}b\,\frac{r_0}{\rho}\left(4\left(\frac{r_0}{r}\right)^2 + 3\frac{r_0}{\rho}\frac{r_0}{r} + \left(\frac{r_0}{\rho}\right)^2\right) e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(3600\left(\frac{r_m}{r'}\right)^{15} - 1296\left(\frac{r_m}{r'}\right)^9\right) \right]
\]

**Pressure derivative of C̃44**

\[
\tilde{C}_{44}' = \frac{1}{6 \tilde{K} r_0^3}\left[ 5.1121\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 - 2b\,\frac{r_0}{\rho}\left(2\left(\frac{r_0}{r}\right)^2 + \frac{r_0}{\rho}\frac{r_0}{r}\right) e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(1800\left(\frac{r_m}{r'}\right)^{15} - 432\left(\frac{r_m}{r'}\right)^9\right) \right]
\]

**Pressure derivative of C̃_s**

\[
\tilde{C}_s' = \frac{1}{6 \tilde{K} r_0^3}\left[ 4.8861\,\frac{Z^2 e^2}{r_0}\left(\frac{r_0}{r}\right)^4 + b\,\frac{r_0}{\rho}\left(\left(\frac{r_0}{\rho}\right)^2 - 2\left(\frac{r_0}{r}\right)^2\right) e^{-r/\rho} + \sqrt{2}\,\varepsilon_0\left(\frac{r_0}{r_m}\right)^3 \left(540\left(\frac{r_m}{r'}\right)^{15}\right) \right]
\]

**Thermal corrections**

The measured room‑temperature quantities (K^T, C₄₄, C_s, P = 0) are corrected to static‑lattice values using

\[
P = \tilde{P} + \frac{W_V}{C_V}\,\beta\,K^T
\]

\[
K^T = \tilde{K} + \frac{W_V}{C_V}\left(\frac{dK^T}{dT}\right)_V + V\left(\frac{K^T \beta}{C_V}\right)^2\left[ T C_V - W_V - T\,\frac{W_V}{C_V}\left(\frac{dC_V}{dT}\right)_V \right]
\]

\[
C_{44} = \tilde{C}_{44} + \frac{W_V}{C_V}\left(\frac{dC_{44}}{dT}\right)_V
\]

\[
C_s = \tilde{C}_s + \frac{W_V}{C_V}\left(\frac{dC_s}{dT}\right)_V
\]

Here β is the volume coefficient of thermal expansion, V = 2 r₀³ is the volume per ion pair, and the temperature derivatives are taken from Table 2. The vibrational energy W_V and heat capacity C_V are those of a Debye solid; the ratio W_V/(T C_V) is given in Table 1. The Debye temperature θ_D is chosen so that the Debye model yields the same W_V/(T C_V) at T = 295 K. Once θ_D is fixed, C_V and (dC_V/dT)_V are evaluated from the Debye functions:

\[
C_V = 9 N k_B \left(\frac{T}{\theta_D}\right)^3 \int_0^{\theta_D/T} \frac{x^4 e^x}{(e^x-1)^2}\,dx
\]

\[
W_V = 9 N k_B T \left(\frac{T}{\theta_D}\right)^3 \int_0^{\theta_D/T} \frac{x^3}{e^x-1}\,dx
\]

(where N = 1 for the ion‑pair calculation). The temperature derivative (dC_V/dT)_V can be obtained by finite‑difference differentiation of C_V around T = 295 K.

## Reproduction target
Implement the thermal correction and parameter-fitting workflow described above for NaCl, KF, and NaF. For each compound, report the fitted potential parameters (Z, b, ρ, ε₀, rₘ) and all computed static-lattice quantities (P̃, K̃, C̃₄₄, C̃_s, and their pressure derivatives) in the unit conventions given in the output schema. For KF and NaF, numerically determine the pressure at which C₄₄/K equals the respective critical α value (0.13 and 0.14), and the pressure at which C₄₄ becomes zero. The final result must be written to /app/outputs/model_predictions.json with the exact structure described in the output contract.

## Assets

- NumPy: numpy
- SciPy: scipy
- Experimental elastic constants for NaCl, KF, NaF

## Workflow steps

### Step 1: Extract experimental data
- Role: process
- Action: Read and parse the tabulated experimental constants for NaCl, KF, and NaF (nearest-neighbor distance r₀, thermal expansion coefficient β, vibrational factor W_V/TC_V, isothermal bulk modulus K^T, shear moduli C₄₄ and C_s, and their temperature- and pressure-derivatives) provided in the instruction. Store them in a structured numerical format.
- Evidence: `/app/outputs/experimental_data.json`

### Step 2: Apply thermal corrections to obtain static-lattice constants
- Role: process
- Action: Using the experimental data and the Mie-Grüneisen/Debye equations (thermal correction formulas for pressure, bulk modulus, and shear moduli), compute the static-lattice (zero-temperature) pressure P̃, bulk modulus K̃, shear moduli C̃_s and C̃₄₄, and their pressure derivatives K̃', C̃₄₄', C̃_s' for each compound. The required temperature derivatives are given in the tables.
- Evidence: `/app/outputs/static_lattice.json`

### Step 3: Fit central-force potential parameters
- Role: process
- Action: Formulate the five nonlinear equations that relate the unknown potential parameters (Z, b, ρ, ε₀, rₘ) to the static-lattice quantities from step 2. Solve this system numerically for each compound independently (e.g., using SciPy's fsolve). Ensure the solution reproduces the target pressure, bulk modulus, C₄₄, and their pressure derivatives.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 4: Compute high-pressure curves and phase-transition pressures
- Role: process
- Action: For KF and NaF, using the fitted parameters and the model equations together with the thermal corrections, compute C₄₄ and the bulk modulus K as functions of pressure. Determine the pressure at which C₄₄/K reaches the critical value α=0.13 for KF and α=0.14 for NaF, as well as the pressure where C₄₄ becomes zero.
- Evidence: `/app/outputs/high_pressure_results.json`

### Step 5: Output final model predictions
- Role: scored
- Action: Assemble all results into a single JSON file model_predictions.json containing: for each compound (NaCl, KF, NaF) the fitted parameters (Z, b, ρ, ε₀, rₘ) and the computed static-lattice quantities (P̃, K̃, C̃₄₄, C̃_s, K̃', C̃₄₄', C̃_s'), and the predicted phase-transition pressures for KF and NaF.
- Output file: `/app/outputs/model_predictions.json`
- Format: json
- Contract: {"compounds": [{"name": "NaCl/KF/NaF", "Z": number, "b": number (10^{-10} erg/bond), "rho": number (10^{-8} cm), "epsilon_0": number (10^{-16} erg/bond), "r_m": number (10^{-8} cm), "P_tilde": number (kb), "K_tilde": number (kb), "C44_tilde": number (kb), "Cs_tilde": number (kb), "K_prime": number, "C44_prime": number, "Cs_prime": number}], "phase_transitions": {"KF": number (kb), "NaF": number (kb)}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model_predictions.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model_predictions.json
- path: `/app/outputs/model_predictions.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final model predictions including fitted potential parameters, static-lattice elastic constants and their pressure derivatives for NaCl, KF, NaF, and predicted phase-transition pressures for KF and NaF.
- schema:
  - `type`: object
  - `required`: `compounds`, `phase_transitions`
  - `properties`:
    - `compounds`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `name`, `Z`, `b`, `rho`, `epsilon_0`, `r_m`, `P_tilde`, `K_tilde`, `C44_tilde`, `Cs_tilde`, `K_prime`, `C44_prime`, `Cs_prime`
        - `properties`:
          - `name`:
            - `type`: string
          - `Z`:
            - `type`: number
            - `description`: dimensionless
          - `b`:
            - `type`: number
            - `description`: 10^{-10} erg/bond
          - `rho`:
            - `type`: number
            - `description`: 10^{-8} cm
          - `epsilon_0`:
            - `type`: number
            - `description`: 10^{-16} erg/bond
          - `r_m`:
            - `type`: number
            - `description`: 10^{-8} cm
          - `P_tilde`:
            - `type`: number
            - `description`: kb
          - `K_tilde`:
            - `type`: number
            - `description`: kb
          - `C44_tilde`:
            - `type`: number
            - `description`: kb
          - `Cs_tilde`:
            - `type`: number
            - `description`: kb
          - `K_prime`:
            - `type`: number
            - `description`: dimensionless
          - `C44_prime`:
            - `type`: number
            - `description`: dimensionless
          - `Cs_prime`:
            - `type`: number
            - `description`: dimensionless
    - `phase_transitions`:
      - `type`: object
      - `required`: `KF`, `NaF`
      - `properties`:
        - `KF`:
          - `type`: number
          - `description`: Predicted transition pressure in kb
        - `NaF`:
          - `type`: number
          - `description`: Predicted transition pressure in kb

Notes: All pressures and moduli in kb, lengths in 10^{-8} cm, energy parameters in units matching the formulas (b in 10^{-10} erg/bond, epsilon_0 in 10^{-16} erg/bond).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model_predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "compounds",
          "phase_transitions"
        ],
        "properties": {
          "compounds": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "name",
                "Z",
                "b",
                "rho",
                "epsilon_0",
                "r_m",
                "P_tilde",
                "K_tilde",
                "C44_tilde",
                "Cs_tilde",
                "K_prime",
                "C44_prime",
                "Cs_prime"
              ],
              "properties": {
                "name": {
                  "type": "string"
                },
                "Z": {
                  "type": "number",
                  "description": "dimensionless"
                },
                "b": {
                  "type": "number",
                  "description": "10^{-10} erg/bond"
                },
                "rho": {
                  "type": "number",
                  "description": "10^{-8} cm"
                },
                "epsilon_0": {
                  "type": "number",
                  "description": "10^{-16} erg/bond"
                },
                "r_m": {
                  "type": "number",
                  "description": "10^{-8} cm"
                },
                "P_tilde": {
                  "type": "number",
                  "description": "kb"
                },
                "K_tilde": {
                  "type": "number",
                  "description": "kb"
                },
                "C44_tilde": {
                  "type": "number",
                  "description": "kb"
                },
                "Cs_tilde": {
                  "type": "number",
                  "description": "kb"
                },
                "K_prime": {
                  "type": "number",
                  "description": "dimensionless"
                },
                "C44_prime": {
                  "type": "number",
                  "description": "dimensionless"
                },
                "Cs_prime": {
                  "type": "number",
                  "description": "dimensionless"
                }
              }
            }
          },
          "phase_transitions": {
            "type": "object",
            "required": [
              "KF",
              "NaF"
            ],
            "properties": {
              "KF": {
                "type": "number",
                "description": "Predicted transition pressure in kb"
              },
              "NaF": {
                "type": "number",
                "description": "Predicted transition pressure in kb"
              }
            }
          }
        }
      },
      "description": "Final model predictions including fitted potential parameters, static-lattice elastic constants and their pressure derivatives for NaCl, KF, NaF, and predicted phase-transition pressures for KF and NaF."
    }
  ],
  "notes": "All pressures and moduli in kb, lengths in 10^{-8} cm, energy parameters in units matching the formulas (b in 10^{-10} erg/bond, epsilon_0 in 10^{-16} erg/bond)."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/model_predictions.json and compares each numeric field to reference values derived from the paper’s own reported results. Each field is evaluated against a tolerance appropriate for the quantity (e.g., a relative tolerance for the parameters and moduli, an absolute tolerance for the transition pressures). The reward is a weighted sum of the accepted fields, normalized to [0,1]. Fields that fall within tolerance earn full weight; fields that deviate beyond tolerance earn zero. The verifier may also inspect the intermediate evidence files (experimental_data.json, static_lattice.json, fitted_parameters.json, high_pressure_results.json) for structural consistency, but the primary score comes from the final model_predictions.json. Simply reporting numbers that match the paper’s tables is not sufficient — the numbers must arise from a correctly implemented computational pipeline.
