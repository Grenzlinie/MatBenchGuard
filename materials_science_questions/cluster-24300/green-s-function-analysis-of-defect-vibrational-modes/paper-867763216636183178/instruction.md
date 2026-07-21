# Two-Path Phonon Interference Transmission and Thermal Conductance

## Problem background
In a three-dimensional atomic-scale phononic metamaterial, a crystal plane partially filled with defect-atom arrays forces phonons to propagate through two distinct interference paths. This setup can give rise to a frequency-dependent transmission antiresonance that strongly suppresses phonon transmission. The phenomenon is modeled by an equivalent quasi-1D harmonic oscillator network, yielding an analytical energy transmission coefficient α(ω). The key question is how this interference affects the interfacial thermal conductance when the transmission is integrated in the Landauer formalism.

## Approach
The defect plane is replaced by an equivalent quasi-1D harmonic oscillator network that contains two parallel phonon paths. This network yields an analytical expression for the plane-wave energy transmission coefficient α(ω) that depends on a few characteristic frequencies and a coupling constant. The transmission coefficient is first evaluated over the entire allowed frequency range. Then, the interfacial thermal conductance G is computed using the Landauer-like formula, integrating over all phonon modes with the obtained α(ω). A simplified Debye model for the phonon dispersion is used to perform the integration in polar coordinates. The conductance obtained with the interference transmission is compared to the defect-free case where α=1.

## Reproduction target
Compute the energy transmission coefficient α(ω) from the quasi-1D two-path interference formula for the given Ar-lattice parameters (ω_R=1.0 rad/s, ω_T=1.4 rad/s, ω_max=2.0 rad/s, C=0.25) across the frequency range 0 to ω_max, and write the resulting curve as a CSV file. Then compute the interfacial thermal conductance G per unit area at T=300 K using the Landauer integration with the computed α(ω) and the specified Debye model (v_s=1.2×10³ m/s, ω_max=2.0 rad/s). Compare the resulting conductance to that of a defect-free plane (where α=1) to determine the relative change.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute transmission coefficient α(ω)
- Role: scored (load-bearing)
- Action: Evaluate the energy transmission coefficient α(ω) using the two-path phonon interference formula for the quasi-1D model with given parameters ω_R = 1.0 rad/s, ω_T = 1.4 rad/s, ω_max = 2.0 rad/s, and C = 0.25. Compute α(ω) on a dense frequency grid from ω = 0 to ω_max and write a CSV file.
- Output file: `/app/outputs/step_01_transmission.csv`
- Format: csv
- Contract: csv with header: frequency (rad/s), alpha (dimensionless). One row per computed frequency point.
- Scoring: scored by hidden verifier

### Step 2: Compute interfacial thermal conductance G
- Role: scored
- Action: Using the Landauer-like formalism, compute the interfacial thermal conductance G per unit area (W/m²K) at T=300 K for the Ar lattice with the transmission coefficient α(ω) from step_01. Adopt a simplified Debye model with one longitudinal acoustic branch: linear dispersion ω = v_s k, v_s = 1.2×10³ m/s, Debye cutoff frequency ω_max = 2.0 rad/s. Integrate over the 2D transverse wavevector in polar coordinates up to the cutoff. Write the resulting G as a single floating-point number.
- Output file: `/app/outputs/step_02_thermal_conductance.txt`
- Format: txt
- Contract: Single floating-point number representing G in W/m²K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_transmission.csv`
- `/app/outputs/step_02_thermal_conductance.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_transmission.csv
- path: `/app/outputs/step_01_transmission.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Transmission coefficient α(ω) evaluated on a frequency grid. The checker recomputes α at hidden frequency points and verifies that α is near 0 at ω_R and ω_max, near 1 at ω=0 and ω_T, and that a deep antiresonance dip exists.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `alpha`
  - `units`:
    - `frequency`: rad/s
    - `alpha`: dimensionless

### step_02_thermal_conductance.txt
- path: `/app/outputs/step_02_thermal_conductance.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Interfacial thermal conductance G obtained by Landauer integration. The checker recomputes G from the agent's transmission.csv and compares it to a hidden reference value, applying a threshold-or-better criterion (meeting or exceeding the expected conductance reduction).
- schema:
  - `type`: text
  - `units`: W/m²K

Notes: All parameters needed for the analytical model and Debye dispersion are given in the public instruction. The agent must not assume any pre-computed tables; all integrations must be performed from scratch.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_transmission.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "alpha"
        ],
        "units": {
          "frequency": "rad/s",
          "alpha": "dimensionless"
        }
      },
      "description": "Transmission coefficient α(ω) evaluated on a frequency grid. The checker recomputes α at hidden frequency points and verifies that α is near 0 at ω_R and ω_max, near 1 at ω=0 and ω_T, and that a deep antiresonance dip exists."
    },
    {
      "file": "step_02_thermal_conductance.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": "W/m²K"
      },
      "description": "Interfacial thermal conductance G obtained by Landauer integration. The checker recomputes G from the agent's transmission.csv and compares it to a hidden reference value, applying a threshold-or-better criterion (meeting or exceeding the expected conductance reduction)."
    }
  ],
  "notes": "All parameters needed for the analytical model and Debye dispersion are given in the public instruction. The agent must not assume any pre-computed tables; all integrations must be performed from scratch."
}
```

## How you are scored
A hidden verifier independently checks both output artifacts. For the transmission curve, the verifier recomputes α(ω) at hidden frequency points and verifies that it exhibits the expected interference structure (near-zero at the reflection frequency, near-unity at the transmission frequency and at zero frequency). For the thermal conductance, the verifier recomputes G from your transmission.csv and compares it to a hidden reference value using a threshold-or-better criterion: a result that equals or exceeds the expected conductance reduction earns full credit, while a worse result reduces credit. The final reward is a weighted combination of the scores for the two stages.
