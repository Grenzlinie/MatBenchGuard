# Phonon-assisted hopping model for K0 centre thermal relaxation

## Problem background
In amorphous silicon nitride (a-SiNx:H) films, light exposure causes a metastable increase in subgap absorption, which has been linked to the neutralisation of charged dangling-bond defects known as K centres. After illumination, the concentration of neutral K0 centres is enhanced, and the material exhibits a slow thermal relaxation back toward equilibrium. The thermal relaxation rate is quantitatively modelled by a phonon-assisted hopping process: electrons hop between localized band-tail states and the metastable K0 centres. Implementing this kinetic model from the published theoretical framework allows one to predict the decay of the K0 concentration as a function of annealing time for a given set of material parameters.

## Approach
The model describes the density of K0 states as a Gaussian distribution G(ε) of width εw around mid-gap. The conduction-band tail states follow an exponential density g(ε) = (N/ε0) exp(ε/ε0), where ε0 is the tail width and N the total concentration of tail states. Conduction is assumed to occur predominantly through a “transport energy” εt, which depends on ε0, temperature, and the localisation radius. The average hopping rate at εt is νt = ν0 exp(−3 ε0 / kT), with ν0 a characteristic phonon frequency. At time t during annealing, only K0 centres with thermal emission rates faster than 1/t can have released an electron; this defines a time-dependent demarcation energy εd. As εd sweeps through the Gaussian K0 density, electrons are released to the transport energy, captured by other K0 centres, converting them to charged K+ and K−. The rate equation for the K0 concentration is

d[K0]/dt = −2 G(εd) kT / t * (b0[K0])/(b0[K0] + b+[K+]),

where b0 and b+ are electron capture coefficients. Local charge neutrality and total K-centre conservation provide the relations [K+] = [K−] + n and [K+] + [K0] + [K−] = constant. With a very small ratio b+/b0, the relaxation kinetics are dominated by the numerator term. The model is integrated as an initial-value problem starting from a saturated metastable K0 population. The specific parameter set for the target sample (ε0 = 0.10 eV, εw = 0.29 eV, ν0 = 1×10^12 s−1, b+/b0 = 0.01, anneal temperature Ta = 500 K) is provided in the workflow step below.

## Reproduction target
Produce a CSV file containing the normalised K0 fraction, [K0](t)/[K0](0), evaluated at 20 logarithmically spaced time points from t = 1 s to t = 10 000 s. The CSV must have two columns: time_s (seconds) and fraction_remaining (dimensionless). This output serves as the scored artifact; its values will be compared against a hidden reference solution computed from the identical model and parameters.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute the K0 annealing curve from the hopping model
- Role: scored (load-bearing)
- Action: Implement the phonon-assisted hopping model for thermal relaxation of K0 centres using a Gaussian density of K0 states, an exponential conduction-band tail density, a transport energy, and the rate equation d[K0]/dt = -2 G(εd) kT t^{-1} * (b0[K0]/(b0[K0]+b+[K+])). Use the parameters ε0=0.10 eV, εw=0.29 eV, v0=1×10^12 s^{-1}, b+/b0=0.01, anneal temperature Ta=500 K, and charge conservation constraints. Solve the ODE starting from saturated metastable K0 state and output the normalized remaining K0 fraction ([K0](t)/[K0](0)) at 20 logarithmically spaced time points from t=1 s to t=10000 s.
- Output file: `/app/outputs/step_01_annealing_curve.csv`
- Format: csv
- Contract: time_s (float), fraction_remaining (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_annealing_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_annealing_curve.csv
- path: `/app/outputs/step_01_annealing_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Annealing curve of normalized K0 fraction as a function of time computed from the phonon-assisted hopping model for the E04=3.3 eV sample. The checker recomputes the reference curve and scores via mean absolute error (MAE).
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `fraction_remaining`
  - `column_types`:
    - `time_s`: float (seconds)
    - `fraction_remaining`: float (dimensionless)

Notes: The agent must use the specific parameter set for the E04=3.3 eV sample as described. The reference curve is derived from the same equations and parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_annealing_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "fraction_remaining"
        ],
        "column_types": {
          "time_s": "float (seconds)",
          "fraction_remaining": "float (dimensionless)"
        }
      },
      "description": "Annealing curve of normalized K0 fraction as a function of time computed from the phonon-assisted hopping model for the E04=3.3 eV sample. The checker recomputes the reference curve and scores via mean absolute error (MAE)."
    }
  ],
  "notes": "The agent must use the specific parameter set for the E04=3.3 eV sample as described. The reference curve is derived from the same equations and parameters."
}
```

## How you are scored
A hidden verifier will independently solve the same ODE system using the declared parameters to obtain a reference annealing curve at the exact times you output. The verifier will then compute the mean absolute error (MAE) between your submitted fraction_remaining values and the reference values. Your score is derived from this MAE: a perfect match (MAE ≈ 0) yields full credit, and larger MAE values result in a proportionally reduced score. The verifier also checks that the output file is properly formatted with the specified two-column schema and exactly 20 rows. Note that the verifier's tolerance thresholds are hidden; your goal is to reproduce the model solution as accurately as possible.
