# Yield Strength Components of High Strength Enameling Steel

## Problem background
Low-carbon enameling steels used in water heater tanks experience a reduction in yield strength during the enamel-fire anneal (EFA). Understanding which microstructural factors (solid solution strengthening, grain size, dislocation density) change during the EFA is critical for developing higher after-fire strength steels. This work uses empirical relationships to estimate the contributions of each factor to the total yield strength for both cold rolled (CR) and hot rolled (HR) forms before and after the anneal.

## Approach
The total yield strength $\sigma_y$ of these low-carbon steels is modeled as the sum of four parts:

$\sigma_y = \sigma_0 + \sigma_s + \sigma_g + \sigma_d$

where $\sigma_0 = 30\;\mathrm{MPa}$ is a constant friction stress.

**Solid solution strengthening** $\sigma_s$ is given by

$\sigma_s = 4570\,[\mathrm{C}] + 4570\,[\mathrm{N}] + 37\,[\mathrm{Mn}] + 83\,[\mathrm{Si}] + 470\,[\mathrm{P}] + 38\,[\mathrm{Cu}]$

where each $[\mathrm{X}]$ is the concentration of element X dissolved in the matrix (wt%). The solubilities are the same before and after EFA. For the CR steel, use Mn=1.2849, Si=0.45, P=0.048, C=$1.20\times10^{-22}$–$2.77\times10^{-4}$, N=$3.66\times10^{-37}$–$2.14\times10^{-10}$, Cu=0.07 (wt%). For the HR steel, use Mn=1.2414, Si=0.35, P=0.043, C=$1.94\times10^{-22}$–$2.96\times10^{-4}$, N=$2.61\times10^{-37}$–$1.44\times10^{-10}$, Cu=0.10 (wt%). The ranges for C and N produce a range for $\sigma_s$; compute both min and max.

**Grain size strengthening** $\sigma_g$ uses the Hall–Petch relation:

$\sigma_g = k_y\,d^{-1/2}$

with $k_y = 17.4\;\mathrm{N\,mm^{-3/2}}$ and ferrite grain diameter $d$ (in mm). Convert the input grain sizes from μm to mm (1 μm = $10^{-3}$ mm). The grain sizes before and after EFA are:
- CR before: 8.7 μm
- CR after: 10.5 μm
- HR before: 7.4 μm
- HR after: 9.5 μm

**Dislocation strengthening** $\sigma_d$ is computed from:

$\sigma_d = \alpha\,G\,b\,\rho^{1/2}$

with $\alpha = 0.38$, shear modulus $G = 8.3\;\mathrm{GPa}$ (note: 1 GPa = $10^3$ MPa), Burgers vector magnitude $b = 0.248\;\mathrm{nm}$ (convert to mm: $1\;\mathrm{nm} = 10^{-6}\;\mathrm{mm}$), and dislocation density $\rho$ in $10^{9}\,\mathrm{cm/cm^{3}}$. The dislocation density input values (in $10^9\;\mathrm{cm/cm^{3}}$) are:
- CR before: 12.2–18.2
- CR after: 4.2–6.3
- HR before: 8.3–12.5
- HR after: 4.3–6.5

Use the range to compute min and max $\sigma_d$ (and consequently min and max $\sigma_y$).

**Changes due to EFA** ($\Delta\sigma_g$, $\Delta\sigma_d$, $\Delta\sigma_y$): subtract the after-EFA value from the before-EFA value for each form (CR and HR). For quantities with a range, compute the deltas from the min and max pairs.

All computations should be implemented in Python using numpy.

## Reproduction target
Compute the solid solution strengthening ($\sigma_s$), grain size strengthening ($\sigma_g$), dislocation strengthening ($\sigma_d$), and total yield strength ($\sigma_y$) for the cold rolled (CR) and hot rolled (HR) steels before and after the enamel-fire anneal (EFA). Also compute the changes $\Delta\sigma_g$, $\Delta\sigma_d$, $\Delta\sigma_y$ due to the anneal. Where an input is given as a range, compute both the minimum and maximum possible value. Output all results in a CSV file named `yield_strength_components.csv` under `/app/outputs/` following the contract described below.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Calculate Yield Strength Components
- Role: scored (load-bearing)
- Action: Compute the solid solution strengthening (σ_s), grain size strengthening (σ_g), dislocation strengthening (σ_d), and total yield strength (σ_y) for the cold rolled (CR) and hot rolled (HR) steels before and after the enamel-fire anneal (EFA), as well as the changes Δσ_g, Δσ_d, Δσ_y due to EFA, using the empirical equations and provided input data. Output all results in a CSV file.
- Output file: `/app/outputs/yield_strength_components.csv`
- Format: csv
- Contract: Columns: form (CR or HR), condition (before_EFA, after_EFA, or delta), sigma_s_min (MPa), sigma_s_max (MPa), sigma_g (MPa), sigma_d_min (MPa), sigma_d_max (MPa), sigma_y_min (MPa), sigma_y_max (MPa), delta_sigma_g (MPa), delta_sigma_d_min (MPa), delta_sigma_d_max (MPa), delta_sigma_y_min (MPa), delta_sigma_y_max (MPa). For absolute rows, delta columns are empty; for delta rows, sigma columns are empty.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/yield_strength_components.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### yield_strength_components.csv
- path: `/app/outputs/yield_strength_components.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed yield strength components and their changes due to enamel-fire anneal for both cold rolled and hot rolled steels.
- schema:
  - `type`: table
  - `required_columns`: `form`, `condition`, `sigma_s_min`, `sigma_s_max`, `sigma_g`, `sigma_d_min`, `sigma_d_max`, `sigma_y_min`, `sigma_y_max`, `delta_sigma_g`, `delta_sigma_d_min`, `delta_sigma_d_max`, `delta_sigma_y_min`, `delta_sigma_y_max`
  - `units`:
    - `sigma_s_min`: MPa
    - `sigma_s_max`: MPa
    - `sigma_g`: MPa
    - `sigma_d_min`: MPa
    - `sigma_d_max`: MPa
    - `sigma_y_min`: MPa
    - `sigma_y_max`: MPa
    - `delta_sigma_g`: MPa
    - `delta_sigma_d_min`: MPa
    - `delta_sigma_d_max`: MPa
    - `delta_sigma_y_min`: MPa
    - `delta_sigma_y_max`: MPa

Notes: The agent uses input data (compositions, grain sizes, dislocation densities, solubilities, and literature constants) that will be provided in the instruction. The checker recomputes the same quantities from the same fixed inputs and compares with tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "yield_strength_components.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "form",
          "condition",
          "sigma_s_min",
          "sigma_s_max",
          "sigma_g",
          "sigma_d_min",
          "sigma_d_max",
          "sigma_y_min",
          "sigma_y_max",
          "delta_sigma_g",
          "delta_sigma_d_min",
          "delta_sigma_d_max",
          "delta_sigma_y_min",
          "delta_sigma_y_max"
        ],
        "units": {
          "sigma_s_min": "MPa",
          "sigma_s_max": "MPa",
          "sigma_g": "MPa",
          "sigma_d_min": "MPa",
          "sigma_d_max": "MPa",
          "sigma_y_min": "MPa",
          "sigma_y_max": "MPa",
          "delta_sigma_g": "MPa",
          "delta_sigma_d_min": "MPa",
          "delta_sigma_d_max": "MPa",
          "delta_sigma_y_min": "MPa",
          "delta_sigma_y_max": "MPa"
        }
      },
      "description": "Computed yield strength components and their changes due to enamel-fire anneal for both cold rolled and hot rolled steels."
    }
  ],
  "notes": "The agent uses input data (compositions, grain sizes, dislocation densities, solubilities, and literature constants) that will be provided in the instruction. The checker recomputes the same quantities from the same fixed inputs and compares with tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the same yield strength components from the same fixed inputs and constants. It reads your CSV, checks that all required columns are present, and compares each computed value (min and max, where applicable) to the reference values. The verifier awards a proportional score based on how many of your values fall within an appropriate tolerance. Simply copying the paper's reported numbers is not enough; the verifier requires the correct computation from the given inputs.
