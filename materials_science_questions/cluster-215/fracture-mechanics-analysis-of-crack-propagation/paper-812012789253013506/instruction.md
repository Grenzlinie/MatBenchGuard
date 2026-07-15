# Fracture Energy Analysis of Rectangular Stress Waves in Rocks

## Problem background
In many rock engineering applications (mining, blasting, earthquake), stress waves propagate through rock and can cause fracture. Only a portion of the wave energy is used to create new crack surfaces; the rest is transmitted as elastic waves that do not contribute to fragmentation. Understanding how to predict the useful energy and the frequency components capable of fracturing the rock is key to optimizing fracturing efficiency. This task analyzes the energy dissipation and cutoff frequency behavior of rectangular stress waves in three rock types using a dynamic fracture criterion combined with Fourier analysis.

## Approach
The analysis applies a dynamic fracture criterion, which states that a harmonic component of stress wave with angular frequency ω can fracture the rock if its amplitude squared satisfies |F(ω)|² ≥ γE/(C ω), where γ is the specific surface energy, E is the elastic modulus, and C is the longitudinal wave velocity. The stress wave is assumed to be a rectangular pulse of amplitude σ and duration τ. Its continuous Fourier transform is known analytically, allowing direct algebraic solution for the cutoff frequencies where the inequality holds. The energy dissipation ratio (percentage) is defined as the fraction of the total wave energy that is transmitted as elastic waves, i.e., the energy in spectral components below the fracture threshold. Both an analytical method (solving the inequality and integrating the spectrum analytically) and a discrete method (sampling the waveform, computing its FFT, and applying the discrete criterion) are used.

To bypass the need to select specific rock material properties, the dimensionless stress wave energy R = σ²τ/(γE/C) is supplied for each rock type and stress wave case. The given R values are:

- Shale: Case 1 (σ=50 MPa, τ=10 µs): 3.42; Case 2 (σ=50 MPa, τ=20 µs): 6.84; Case 3 (σ=70 MPa, τ=10 µs): 6.71.
- Malmstone: Case 1: 2.52; Case 2: 5.04; Case 3: 4.94.
- Liparite: Case 1: 2.28; Case 2: 4.55; Case 3: 4.44.

From these R values and the wave parameters, compute the cutoff frequencies (lower and upper, in rad/s) and the energy dissipation ratios (in percent) for each case using both the analytical and discrete approaches. The two methods are expected to yield very similar results; compare them.

## Reproduction target
For each rock type (shale, malmstone, liparite) and each stress wave case (Case 1: σ=50 MPa, τ=10 µs; Case 2: σ=50 MPa, τ=20 µs; Case 3: σ=70 MPa, τ=10 µs), compute the cutoff frequency range (lower and upper in rad/s) and the energy dissipation ratio (percentage) using (i) the analytical Fourier method and (ii) the discrete Fourier transform (FFT) method. Collect all results in a single JSON file (results.json) with the structure specified in the output contract. Additionally, for shale under Case 1, produce the discrete frequency-domain spectrum (angular frequency vs. squared amplitude |F(ω)|²) as a CSV file (shale_case1_spectrum.csv) that allows independent recomputation of the energy dissipation ratio.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute fracture analysis results for all rock cases
- Role: scored
- Action: For each rock type (shale, malmstone, liparite) and each stress wave case (Case1: σ=50 MPa, τ=10 μs; Case2: σ=50 MPa, τ=20 μs; Case3: σ=70 MPa, τ=10 μs), use the given dimensionless stress wave energy R to: (1) analytically solve the fracture criterion to obtain the lower and upper cutoff frequencies (in rad/s); (2) compute the analytical energy dissipation ratio (%); (3) sample the rectangular wave and compute its discrete Fourier transform (FFT), apply the discrete criterion to find cutoff frequencies and compute the discrete dissipation ratio (%). Output all results to a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with top-level keys 'shale', 'malmstone', 'liparite'. Each value is an object with keys 'case1', 'case2', 'case3'. Each case object has keys: 'stress_wave_energy' (float, the given R), 'cutoff_frequency_lower_rad_s' (float), 'cutoff_frequency_upper_rad_s' (float), 'energy_dissipation_ratio_analytical_pct' (float), 'energy_dissipation_ratio_discrete_pct' (float).
- Scoring: scored by hidden verifier

### Step 2: Discrete frequency spectrum for shale case 1
- Role: scored (load-bearing)
- Action: For shale rock under Case 1 (σ=50 MPa, τ=10 μs), generate a high-resolution discrete sampling of the rectangular stress wave, compute its FFT (angular frequency spectrum), and write the squared amplitude |F(ω)|² versus angular frequency ω (rad/s) as a CSV file.
- Output file: `/app/outputs/shale_case1_spectrum.csv`
- Format: csv
- Contract: CSV with two columns: 'frequency_rad_s' (float, angular frequency ω in rad/s), 'amplitude_squared' (float, |F(ω)|²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/shale_case1_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated fracture analysis results for three rock types under three stress wave cases; values are compared to paper-reported gold with tolerance.
- schema:
  - `type`: object
  - `required`:
    - `shale`:
      - `type`: object
      - `required`:
        - `case1`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case2`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case3`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
    - `malmstone`:
      - `type`: object
      - `required`:
        - `case1`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case2`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case3`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
    - `liparite`:
      - `type`: object
      - `required`:
        - `case1`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case2`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float
        - `case3`:
          - `type`: object
          - `required`:
            - `stress_wave_energy`: float
            - `cutoff_frequency_lower_rad_s`: float
            - `cutoff_frequency_upper_rad_s`: float
            - `energy_dissipation_ratio_analytical_pct`: float
            - `energy_dissipation_ratio_discrete_pct`: float

### shale_case1_spectrum.csv
- path: `/app/outputs/shale_case1_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Discrete frequency spectrum for shale under Case1; the checker recomputes the energy dissipation ratio from this data and compares to the paper's discrete method result.
- schema:
  - `type`: table
  - `required_columns`: `frequency_rad_s`, `amplitude_squared`
  - `units`:
    - `frequency_rad_s`: rad/s
    - `amplitude_squared`: dimensionless, |F(ω)|²

Notes: The agent is given the dimensionless stress wave energy R = σ²τ/(γE/C) for each case directly as input, removing the need to select rock parameters. The computation involves standard Fourier transform methods using open-source Python libraries.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "shale": {
            "type": "object",
            "required": {
              "case1": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case2": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case3": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              }
            }
          },
          "malmstone": {
            "type": "object",
            "required": {
              "case1": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case2": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case3": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              }
            }
          },
          "liparite": {
            "type": "object",
            "required": {
              "case1": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case2": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              },
              "case3": {
                "type": "object",
                "required": {
                  "stress_wave_energy": "float",
                  "cutoff_frequency_lower_rad_s": "float",
                  "cutoff_frequency_upper_rad_s": "float",
                  "energy_dissipation_ratio_analytical_pct": "float",
                  "energy_dissipation_ratio_discrete_pct": "float"
                }
              }
            }
          }
        }
      },
      "description": "Aggregated fracture analysis results for three rock types under three stress wave cases; values are compared to paper-reported gold with tolerance."
    },
    {
      "file": "shale_case1_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_rad_s",
          "amplitude_squared"
        ],
        "units": {
          "frequency_rad_s": "rad/s",
          "amplitude_squared": "dimensionless, |F(ω)|²"
        }
      },
      "description": "Discrete frequency spectrum for shale under Case1; the checker recomputes the energy dissipation ratio from this data and compares to the paper's discrete method result."
    }
  ],
  "notes": "The agent is given the dimensionless stress wave energy R = σ²τ/(γE/C) for each case directly as input, removing the need to select rock parameters. The computation involves standard Fourier transform methods using open-source Python libraries."
}
```

## How you are scored
Your submitted artifacts will be evaluated automatically by a hidden verifier. For results.json, the verifier compares each numerical field (cutoff frequencies and energy dissipation ratios) against previously established reference values with an appropriate tolerance. For shale_case1_spectrum.csv, the verifier recomputes the energy dissipation ratio from your spectral data and compares it to a hidden discrete-method reference value for that case. Additionally, the verifier checks that the analytical and discrete dissipation ratios for each case agree with each other to within a small relative difference. All scored artifacts contribute to the final reward; a trivial reporting of numbers without genuine computation will not succeed.
