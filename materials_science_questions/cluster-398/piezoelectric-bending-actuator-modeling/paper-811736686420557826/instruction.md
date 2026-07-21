# Active piezoelectric absorber for plate vibration attenuation

## Problem background
A simply supported aluminum plate is subjected to a transverse harmonic point force at its center. Two thin piezoelectric sheets are symmetrically bonded to the plate. One sheet, together with a closed electric circuit containing an inductor and a resistor, serves as a dynamic vibration absorber; a voltage source in that circuit allows active control. The second sheet is used as a sensor with a bridge circuit that outputs a signal proportional to the plate velocity. This work investigates whether the active absorber can suppress the resonant vibration of the fundamental (1,1) mode more effectively than a conventional passive absorber, and whether it can additionally attenuate vibrations of higher-order modes that are not directly targeted by the absorber tuning.

## Approach
The coupled plate–piezo system is modeled using classical plate theory with Love simplifications. Hamilton's principle yields the equations of motion for the composite plate, incorporating the piezoelectric coupling terms and the circuit equations for the absorber and sensor. The transverse displacement is expanded in the normalized mode shapes of the simply supported base plate. Galerkin's method projects the governing partial differential equation onto these mode shapes to obtain a set of ordinary differential equations for the generalized coordinates. The circuit equations for the active absorber (R‑L‑C‑voltage‑source) and the sensor (bridge network) are coupled to the generalized coordinates. The complete electromechanical system is then cast into a state‑space form, truncated to the odd modes (1,1), (1,3), (3,1), and (3,3). Under harmonic excitation, frequency responses are computed by solving the linear algebraic system at each excitation frequency. The dimensionless center displacement amplitude is evaluated as a function of dimensionless excitation frequency. Different absorber configurations are explored: passive absorbers with two different damping ratios, and an active absorber with specific control and sensor gains. The absorber natural frequency is set either to the fundamental composite‑plate frequency or to that of the higher (1,3) mode, allowing investigation of cross‑modal effects.

## Reproduction target
Compute the dimensionless steady‑state center displacement amplitude of the plate as a function of dimensionless excitation frequency for the following configurations:

1. Baseline comparison: absorber tuned to the fundamental composite‑plate frequency; passive absorber with two damping ratios and active absorber with specified gains.
2. Uncontrolled‑mode response: absorber tuned to the fundamental frequency, but excitation frequencies near the (1,3) resonance; several sets of control and sensor gains.
3. Cross‑tuning: absorber tuned to the (1,3) composite‑plate frequency, excitation near the fundamental resonance; three gain combinations.

For each configuration, output a CSV file with columns `case`, `freq_ratio` (dimensionless frequency), and `amplitude` (dimensionless center displacement). The maximum amplitude in the resonance region of each case will be the primary quantity evaluated.

## Assets

- Material and geometric parameters
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Load physical parameters
- Role: process
- Action: Read the provided material and geometric parameters (aluminum plate and PVDF piezoelectric sheets) from the task instructions and store them for computation.
- Evidence: none

### Step 2: Compute natural frequencies and mode shapes
- Role: process
- Action: For the simply supported plate and the composite plate (with piezoelectric coverage), compute the natural frequencies of the odd modes (1,1), (1,3), (3,1), (3,3) and the normalized mode shapes φ_{m1m2}(x,y) using analytical formulas. Save the computed frequencies to a text file.
- Evidence: `/app/outputs/frequencies.txt`

### Step 3: Build state‑space model via Galerkin discretization
- Role: process
- Action: Carry out Galerkin projection of the coupled plate–piezo PDE onto the mode shapes, incorporating piezoelectric coupling terms and the circuit equations for the absorber and sensor. Assemble mass, stiffness, and coupling matrices, and form a state‑space representation truncated to modes (1,1), (1,3), (3,1), (3,3). Verify that the assembled system reproduces the composite-plate natural frequencies when electrical terms are removed and save a verification JSON summarizing the check.
- Evidence: `/app/outputs/system_verification.json`

### Step 4: Baseline frequency‑response curves (Fig. 4b)
- Role: scored
- Action: Using the state‑space model, sweep the dimensionless excitation frequency ω/ω_n1 and compute the steady‑state dimensionless centre displacement amplitude u_c*(ω/ω_n1) for three configurations: passive absorber ζ_a=0.001, passive absorber ζ_a=0.01, and active absorber (ζ_a=0.001, K=5000, K_s=100, 1/(R₁C₂)=10⁶). Write the results to a CSV file with columns: case, freq_ratio, amplitude.
- Output file: `/app/outputs/fig4b_frequency_response.csv`
- Format: csv
- Contract: case:string (one of 'passive_zeta0.001', 'passive_zeta0.01', 'active_zeta0.001'), freq_ratio:float (dimensionless frequency omega/omega_n1), amplitude:float (dimensionless centre displacement u_c*)
- Scoring: scored by hidden verifier

### Step 5: Uncontrolled‑mode response (Fig. 8) – mode (1,3)
- Role: scored
- Action: With the absorber tuned to the fundamental composite-plate frequency ω_c1, compute the frequency response near the (1,3) resonance for five sets of control/sensor gains (K=5000, K_s=100; K=5000, K_s=1000; K=5000, K_s=3000; K=5000, K_s=6000; K=8000, K_s=100). Extract the steady‑state amplitude of the generalized coordinate for mode (1,3), convert to dimensionless centre displacement, and write a CSV file with columns: case, freq_ratio, amplitude.
- Output file: `/app/outputs/fig8_frequency_response.csv`
- Format: csv
- Contract: case:string (one of 'K5000_Ks100', 'K5000_Ks1000', 'K5000_Ks3000', 'K5000_Ks6000', 'K8000_Ks100'), freq_ratio:float, amplitude:float
- Scoring: scored by hidden verifier

### Step 6: Cross‑tuning response (Fig. 9) – mode (1,1) while absorber tuned to mode (1,3)
- Role: scored
- Action: Set the absorber natural frequency to ω_c(1,3) ≈ 4.705 ω_n1 and sweep excitation frequencies around the fundamental resonance. Record the dimensionless centre displacement of mode (1,1) for three gain combinations (K=5000, K_s=100; K=5000, K_s=6000; K=8000, K_s=100). Output a CSV file with columns: case, freq_ratio, amplitude.
- Output file: `/app/outputs/fig9_frequency_response.csv`
- Format: csv
- Contract: case:string (one of 'K5000_Ks100', 'K5000_Ks6000', 'K8000_Ks100'), freq_ratio:float, amplitude:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fig4b_frequency_response.csv`
- `/app/outputs/fig8_frequency_response.csv`
- `/app/outputs/fig9_frequency_response.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fig4b_frequency_response.csv
- path: `/app/outputs/fig4b_frequency_response.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frequency response curves for baseline comparison (passive absorber with two damping ratios and active absorber with specified gains); the checker will evaluate the attenuation characteristics.
- schema:
  - `type`: table
  - `required_columns`: `case`, `freq_ratio`, `amplitude`
  - `units`: object

### fig8_frequency_response.csv
- path: `/app/outputs/fig8_frequency_response.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frequency response of mode (1,3) for various sensor gains when the absorber is tuned to the fundamental composite-plate frequency; the checker will evaluate the attenuation characteristics.
- schema:
  - `type`: table
  - `required_columns`: `case`, `freq_ratio`, `amplitude`
  - `units`: object

### fig9_frequency_response.csv
- path: `/app/outputs/fig9_frequency_response.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frequency response of mode (1,1) when the absorber is tuned to the (1,3) composite-plate frequency for three gain combinations; the checker will evaluate the attenuation characteristics.
- schema:
  - `type`: table
  - `required_columns`: `case`, `freq_ratio`, `amplitude`
  - `units`: object

Notes: The verifier reads the agent's CSVs and computes metrics for scoring; the scoring criteria are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fig4b_frequency_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "freq_ratio",
          "amplitude"
        ],
        "units": {}
      },
      "description": "Frequency response curves for baseline comparison (passive absorber with two damping ratios and active absorber with specified gains); the checker will evaluate the attenuation characteristics."
    },
    {
      "file": "fig8_frequency_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "freq_ratio",
          "amplitude"
        ],
        "units": {}
      },
      "description": "Frequency response of mode (1,3) for various sensor gains when the absorber is tuned to the fundamental composite-plate frequency; the checker will evaluate the attenuation characteristics."
    },
    {
      "file": "fig9_frequency_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "freq_ratio",
          "amplitude"
        ],
        "units": {}
      },
      "description": "Frequency response of mode (1,1) when the absorber is tuned to the (1,3) composite-plate frequency for three gain combinations; the checker will evaluate the attenuation characteristics."
    }
  ],
  "notes": "The verifier reads the agent's CSVs and computes metrics for scoring; the scoring criteria are hidden."
}
```

## How you are scored
A hidden verifier will independently score the three scored CSV artifacts. For each CSV, the verifier will locate the resonance region, extract the maximum dimensionless displacement amplitude for every case, and compare these maxima to hidden reference values (derived from the experimental setup described). The reward is a weighted sum of the scores from the three artifacts. Reporting only a final single number is not accepted; you must produce the full frequency‑response curves as specified. The verifier does not run your simulation code—it only reads your submitted CSVs and checks the resulting peak amplitudes.
