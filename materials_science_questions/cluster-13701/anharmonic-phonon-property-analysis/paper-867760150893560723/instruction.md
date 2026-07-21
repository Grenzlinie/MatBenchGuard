# Anharmonic-Bond Delocalization-Localization Transition Reproduction

## Problem background
One-dimensional anharmonic chains can exhibit a competition between delocalization of energy through phonon-like spreading and localization into discrete breathers. This work studies a reduced model where a single anharmonic bond is embedded in an otherwise harmonic chain. The goal is to investigate whether a single conservation law is sufficient to produce a delocalization-localization transition. The central question is whether there exists a critical initial excitation amplitude that separates a regime where energy spreads away from the bond from a regime where it remains trapped as a breather. Answering this question requires numerically computing the dynamics of the anharmonic bond coordinate and analyzing how its long-time behavior changes with the initial amplitude.

## Approach
The approach reduces the infinite harmonic degrees of freedom to a single equation for the anharmonic bond coordinate $q(\tau)$, where $\tau = \omega_0 t$ is a dimensionless time. The bond potential is the symmetric quartic form $V(x)/C = \frac12 x^2 + \frac14 x^4$, and the memory kernel is $k(\tau) = -J_1(\tau)/\tau$ with $J_1$ the Bessel function of the first kind.

After exact elimination of the harmonic degrees of freedom, the equation of motion for $q(\tau)$ (paper Eq. (3)) is the nonlinear integro-differential equation

$$
\ddot{q}(\tau) + \frac12\bigl[q(\tau) + q^3(\tau)\bigr] + \int_0^\tau \! d\tau' \, \frac{J_1(\tau-\tau')}{\tau-\tau'} \bigl[q(\tau') + q^3(\tau')\bigr] = 0 .
$$

An equivalent form, more convenient for numerical work, is the Volterra integral equation (paper Eq. (9))

$$
q(\tau) = A J_0(\tau) - \int_0^{\tau} d\tau' \, J_1(\tau - \tau') \, q^3(\tau') \qquad (\tau \ge 0) ,
$$

where $J_0$ and $J_1$ are Bessel functions of the first kind. The initial condition is an initial displacement $q(0) = A$ and zero initial velocity $\dot q(0) = 0$, which is already built into the Volterra form.

The core task is to solve this equation numerically for a range of initial amplitudes $A$ across the suspected transition region up to a large final time $\tau_{\max}=10^5$ with a time step $h=0.05$. From the time series we will extract several diagnostics: the envelope of $|q(\tau)|$ at late times to detect delocalization decay or persistent localization; the dominant oscillation frequency $\Omega(A)$ above the transition; a relaxation time $\tau_{\text{rel}}(A)$ below the transition defined by the time for the envelope to fall to $A/10$; and power-law exponents for the divergence of these quantities as the critical amplitude is approached. This numerical experiment is self-contained: the model parameters and initial conditions are fully specified, and the analysis requires only standard time-series and curve-fitting routines.

## Reproduction target
Numerically solve the reduced integro-differential / Volterra equation for the anharmonic bond coordinate $q(\tau)$ with the given potential and memory kernel. Run for initial amplitudes $A$ from 1.0 to 1.4 in steps of 0.01, up to $\tau_{\max} = 10^5$ with step $h=0.05$. From the resulting time series, compute and save:
- The envelope $q_{\text{env}}(A)$ of $|q(\tau)|$ at late times (near $\tau=10^5$).
- For $A$ above the transition, the breather frequency $\Omega(A)$ extracted from the late-time dynamics.
- For $A$ below the transition, the relaxation time $\tau_{\text{rel}}(A)$ defined as the time when the envelope first decays to $A/10$.
- The numerically determined critical amplitude $A_{\text{c}}$ that separates delocalization from localization, identified from the envelope or relaxation-time behavior.
- Power-law fits for the divergence of $\tau_{\text{rel}}$ and the modulation period near $A_{\text{c}}$.
These quantities are to be saved as specific CSV, TXT, and JSON files under `/app/outputs`.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Numerical integration of the reduced integro-differential/Volterra equation
- Role: process
- Action: Solve the equation for the anharmonic bond coordinate $q(\tau)$. For numerical work the Volterra form (Eq. (9)) $q(\tau) = A J_0(\tau) - \int_0^\tau d\tau' J_1(\tau-\tau') q^3(\tau')$ with initial condition $q(0)=A$ may be used; alternatively the integro-differential form (Eq. (3)) with initial conditions $q(0)=A$, $\dot q(0)=0$ can be discretized. Use amplitudes $A \in [1.0, 1.4]$ (step 0.01), final time $\tau_{\max}=10^5$, integration step $h=0.05$. Store the time series for subsequent analysis.
- Evidence: none

### Step 2: Compute envelope $q_{\text{env}}$
- Role: scored (load-bearing)
- Action: For each $A$, compute the envelope of $|q(\tau)|$ at late times ($\tau\approx 10^5$). Save as CSV with columns `A`, `q_env`.
- Output file: `/app/outputs/step_01_envelope.csv`
- Format: csv
- Contract: `A`: float, `q_env`: float
- Scoring: scored by hidden verifier

### Step 3: Compute breather frequency $\Omega(A)$
- Role: scored (load-bearing)
- Action: For $A$ above the critical amplitude, determine the dominant frequency of $q(\tau)$ at late times (e.g., from zero crossings or Fourier transform of the tail). Save as CSV with columns `A`, `omega`.
- Output file: `/app/outputs/step_02_frequency.csv`
- Format: csv
- Contract: `A`: float, `omega`: float
- Scoring: scored by hidden verifier

### Step 4: Compute relaxation time $\tau_{\text{rel}}$
- Role: scored (load-bearing)
- Action: For $A$ below the critical amplitude, determine the time when the envelope $q_{\text{env}}(\tau)$ decays to $A/10$. Save as CSV with columns `A`, `tau_rel`.
- Output file: `/app/outputs/step_03_relaxation_time.csv`
- Format: csv
- Contract: `A`: float, `tau_rel`: float
- Scoring: scored by hidden verifier

### Step 5: Determine critical amplitude $A_c$
- Role: scored (load-bearing)
- Action: From the envelope data, identify the amplitude at which the transition occurs (sharp drop in $q_{\text{env}}$ or divergence of $\tau_{\text{rel}}$) and save as a plain text file containing the numerical value.
- Output file: `/app/outputs/step_04_critical_amplitude.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

### Step 6: Extract power-law exponents of divergence
- Role: scored (load-bearing)
- Action: From the computed $\tau_{\text{rel}}(A)$ for $A<A_c$ and the modulation period $2\pi/\omega_{\text{mod}}(A)$ (extracted from the modulation envelope of $q(\tau)$ for $A>A_c$) fit power laws: $\tau_{\text{rel}} \propto (A_c - A)^{-\gamma}$ and $2\pi/\omega_{\text{mod}} \propto (A - A_c)^{-\delta}$. Save the fitted exponents and fit ranges as a JSON file with keys `gamma`, `gamma_error`, `delta`, `delta_error`, `fit_range`.
- Output file: `/app/outputs/step_05_powerlaw_exponents.json`
- Format: json
- Contract: JSON object with keys: `gamma`, `gamma_error`, `delta`, `delta_error`, `fit_range`
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_envelope.csv`
- `/app/outputs/step_02_frequency.csv`
- `/app/outputs/step_03_relaxation_time.csv`
- `/app/outputs/step_04_critical_amplitude.txt`
- `/app/outputs/step_05_powerlaw_exponents.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_envelope.csv
- path: `/app/outputs/step_01_envelope.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Envelope of $|q(\tau)|$ at late times for each amplitude.
- schema:
  - `type`: table
  - `required_columns`: `A`, `q_env`
  - `units`:
    - `A`: dimensionless
    - `q_env`: dimensionless

### step_02_frequency.csv
- path: `/app/outputs/step_02_frequency.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Breather frequency $\Omega(A)$ for $A$ above the critical amplitude.
- schema:
  - `type`: table
  - `required_columns`: `A`, `omega`
  - `units`:
    - `A`: dimensionless
    - `omega`: frequency in units of $\omega_0$

### step_03_relaxation_time.csv
- path: `/app/outputs/step_03_relaxation_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxation time $\tau_{\text{rel}}$ for $A$ below the critical amplitude.
- schema:
  - `type`: table
  - `required_columns`: `A`, `tau_rel`
  - `units`:
    - `A`: dimensionless
    - `tau_rel`: dimensionless time

### step_04_critical_amplitude.txt
- path: `/app/outputs/step_04_critical_amplitude.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical amplitude $A_c$ separating delocalization from localization.
- schema:
  - `type`: text
  - `description`: single float value

### step_05_powerlaw_exponents.json
- path: `/app/outputs/step_05_powerlaw_exponents.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Power-law exponents of divergence of relaxation time and modulation period near $A_c$.
- schema:
  - `type`: object
  - `required`: `gamma`, `gamma_error`, `delta`, `delta_error`, `fit_range`
  - `properties`:
    - `gamma`:
      - `type`: number
      - `description`: exponent for $\tau_{\text{rel}}$ divergence
    - `gamma_error`:
      - `type`: number
      - `description`: uncertainty in gamma
    - `delta`:
      - `type`: number
      - `description`: exponent for modulation period divergence
    - `delta_error`:
      - `type`: number
      - `description`: uncertainty in delta
    - `fit_range`:
      - `type`: object
      - `description`: range of amplitudes used in the power-law fits (e.g., min_A, max_A for each side)

Notes: All scored outputs are derived from the numerical solution of the integro-differential / Volterra equation. The checker will compare envelope, frequency, relaxation time, critical amplitude, and exponents to paper-reported values (hidden gold) with appropriate tolerances, and verify structural trends (envelope shape, divergence, frequency above band edge). The modulation period extraction is implicit in the power-law exponents step; no separate output file is required for the period values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_envelope.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "A",
          "q_env"
        ],
        "units": {
          "A": "dimensionless",
          "q_env": "dimensionless"
        }
      },
      "description": "Envelope of |q(τ)| at late times for each amplitude."
    },
    {
      "file": "step_02_frequency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "A",
          "omega"
        ],
        "units": {
          "A": "dimensionless",
          "omega": "frequency in units of ω0"
        }
      },
      "description": "Breather frequency Ω(A) for A above the critical amplitude."
    },
    {
      "file": "step_03_relaxation_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "A",
          "tau_rel"
        ],
        "units": {
          "A": "dimensionless",
          "tau_rel": "dimensionless time"
        }
      },
      "description": "Relaxation time τ_rel for A below the critical amplitude."
    },
    {
      "file": "step_04_critical_amplitude.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "single float value"
      },
      "description": "Critical amplitude A_c separating delocalization from localization."
    },
    {
      "file": "step_05_powerlaw_exponents.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "gamma",
          "gamma_error",
          "delta",
          "delta_error",
          "fit_range"
        ],
        "properties": {
          "gamma": {
            "type": "number",
            "description": "exponent for τ_rel divergence"
          },
          "gamma_error": {
            "type": "number",
            "description": "uncertainty in gamma"
          },
          "delta": {
            "type": "number",
            "description": "exponent for modulation period divergence"
          },
          "delta_error": {
            "type": "number",
            "description": "uncertainty in delta"
          },
          "fit_range": {
            "type": "object",
            "description": "range of amplitudes used in the power-law fits (e.g., min_A, max_A for each side)"
          }
        }
      },
      "description": "Power-law exponents of divergence of relaxation time and modulation period near A_c."
    }
  ],
  "notes": "All scored outputs are derived from the numerical solution of the integro-differential equation. The checker will compare envelope, frequency, relaxation time, critical amplitude, and exponents to paper-reported values (hidden gold) with appropriate tolerances, and verify structural trends (envelope shape, divergence, frequency above band edge). The modulation period extraction is implicit in the power-law exponents step; no separate output file is required for the period values."
}
```

## How you are scored
A hidden verifier will independently inspect the submitted artifacts for each workflow step. Each scored artifact is evaluated against a set of reference criteria derived from the physical properties of the system and independent recomputations. The verifier checks not only the existence and format of each file, but also the correctness of the reported numerical results such as the envelope shape (decay vs. finite), the frequency values relative to the expected isolated-bond frequency, the relaxation times, and the critical amplitude. Power-law exponents and their uncertainties are compared to expected values. The final reward is a weighted combination of the per-step scores. Reporting a number alone is not sufficient—the checker verifies that the data was produced by a genuine simulation consistent with the described protocol.