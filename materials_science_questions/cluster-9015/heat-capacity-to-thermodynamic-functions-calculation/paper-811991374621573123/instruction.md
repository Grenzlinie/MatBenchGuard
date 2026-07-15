# Calculate thermodynamic properties of gaseous neopentane from PVT data

## Problem background
The problem is to determine the thermodynamic properties (enthalpy, entropy, specific volume, and fugacity coefficient) of gaseous neopentane over a range of temperatures from 620 to 900 °R and pressures up to 4500 psia. These thermodynamic data are needed for constructing Mollier diagrams and for engineering calculations involving compression, expansion, and heat exchange of neopentane.

## Approach
The computation uses a volume‑residual method. Starting from experimental PVT measurements of neopentane, the volume residual γ = RT/P − V is calculated (R = 0.14874). A localized equation of state
  γ = C1 + C2·P + C3·P² + C4·T + C5·P·T + C6·P²·T + C7·T² + C8·P·T² + C9·P²·T²
is fitted to a smoothed grid of γ values. Ideal‑gas state enthalpy and entropy changes are obtained by analytical integration of the known ideal‑gas heat capacity equation Cp° = 15.4496 + 92.6474·exp(−571.7382/T) (T in K). Pressure corrections H_P and S_P are computed by numerical integration of the fitted γ equation over subintervals of 5 psi. The reference state is the saturated liquid at 620 °R and 87.61 psia; heats and entropies of vaporization from the PVT data source are used to establish absolute values. Specific volume is recovered as V = RT/P − γ, and fugacity coefficients are computed via pressure integration of γ. The workflow therefore consists of (1) processing the PVT data into a smoothed residual array, (2) fitting the EoS coefficients, and (3) computing all required gaseous properties at the specified P‑T grid.

## Reproduction target
Produce a CSV file `thermodynamic_properties.csv` containing the computed enthalpy H (Btu/lb), entropy S (Btu/(lb·°R)), specific volume V (ft³/lb), and fugacity coefficient ν (dimensionless) for gaseous neopentane at two temperature lines:
- at T = 620 °R for pressures P = 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 80 psia;
- at T = 900 °R for pressures P = 10, 20, 40, 60, 80, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4500 psia.
The CSV must have columns T, P, V, H, S, nu with at least 4 decimal places for H, S, nu and 5 for V. The output is scored by a hidden verifier.

## Assets

- PVT data for neopentane (Dawson et al., 1973): 10.1021/je60056a007
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare volume residual array from PVT data
- Role: process
- Action: Obtain experimental PVT data for neopentane from Dawson et al. (1973). For each data point (P, V, T), compute the volume residual γ = RT/P − V using the gas constant R = 0.14874 (psi·ft³)/(°R·lb). Smooth and interpolate the γ values onto an evenly spaced grid of temperature and pressure using least‑squares smoothing.
- Evidence: `/app/outputs/residual_array.csv`

### Step 2: Fit localized equation of state for volume residual
- Role: process
- Action: Fit the polynomial function γ = C1 + C2·P + C3·P² + C4·T + C5·P·T + C6·P²·T + C7·T² + C8·P·T² + C9·P²·T² to the smoothed γ grid using least‑squares regression. Save the fitted coefficients.
- Evidence: `/app/outputs/eos_coefficients.json`

### Step 3: Compute thermodynamic properties of gaseous neopentane
- Role: scored (load-bearing)
- Action: Using the fitted γ equation of state, the ideal gas heat capacity equation Cp° = 15.4496 + 92.6474·exp(−571.7382/T) (T in K), the gas constant R = 0.14874, the dimensional constant J = 0.00256644, and the reference state (saturated liquid at 620 °R and 87.61 psia; heat of vaporization and entropy of vaporization from the companion PVT paper), compute: (1) ideal‑state enthalpy and entropy changes via analytical integration of Cp°; (2) pressure corrections H_P and S_P via numerical integration over 5‑psi subintervals; (3) total enthalpy H and entropy S; (4) specific volume V = RT/P − γ; (5) fugacity coefficient ν via pressure integration. Produce a table for the temperature‑pressure grid described in the output schema.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: CSV file with columns: T (temperature in °R), P (pressure in psia), V (specific volume in ft³/lb), H (enthalpy in Btu/lb), S (entropy in Btu/(lb·°R)), nu (fugacity coefficient, dimensionless). The grid covers: T=620 °R at P = 5,10,15,20,25,30,35,40,50,60,70,80 psia; T=900 °R at P = 10,20,40,60,80,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1100,1200,1300,1400,1500,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800,4000,4200,4400,4500 psia. Use at least 4 decimal places for H, S, nu and 5 for V.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed thermodynamic properties of gaseous neopentane for the specified T‑P grid. The checker compares these values to the paper’s reported gold within per‑quantity tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P`, `V`, `H`, `S`, `nu`
  - `units`:
    - `T`: degR
    - `P`: psia
    - `V`: ft3/lb
    - `H`: Btu/lb
    - `S`: Btu/(lb degR)
    - `nu`: dimensionless

Notes: The secondary internal‑consistency check (isobaric integration of S along P=60 psia) is a hidden structural audit applied during grading, not a separate agent step.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P",
          "V",
          "H",
          "S",
          "nu"
        ],
        "units": {
          "T": "degR",
          "P": "psia",
          "V": "ft3/lb",
          "H": "Btu/lb",
          "S": "Btu/(lb degR)",
          "nu": "dimensionless"
        }
      },
      "description": "Computed thermodynamic properties of gaseous neopentane for the specified T‑P grid. The checker compares these values to the paper’s reported gold within per‑quantity tolerances."
    }
  ],
  "notes": "The secondary internal‑consistency check (isobaric integration of S along P=60 psia) is a hidden structural audit applied during grading, not a separate agent step."
}
```

## How you are scored
A hidden verifier grades the submission by independently evaluating each workflow artifact. The main scored artifact (`thermodynamic_properties.csv`) is compared against reference values derived from the original study; the verifier checks that the computed H, S, V, and ν agree within per‑quantity tolerances. Additionally, an internal consistency check is performed on one isobar (P = 60 psia) using the thermodynamic relation ΔH = T₂S₂ − T₁S₁ − ∫ S dT to verify that the enthalpy–entropy relationship holds to high precision. The final reward is a weighted sum of scores from the stages, with the thermodynamic property table carrying the largest weight. Reporting numbers from the original literature is insufficient; the verifier expects the values to be generated by the computational workflow described in the steps.
