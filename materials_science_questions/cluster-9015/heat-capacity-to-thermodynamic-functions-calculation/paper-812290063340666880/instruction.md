# Thermodynamic Functions and Vapor Pressure Equation for NiO

## Problem background
The temperature‑dependent vapor pressure of a solid is thermodynamically linked to its heat of sublimation at absolute zero through the free energy functions of the solid and vapor phases. For a solid, the free energy function can be calculated from its heat capacity and entropy at a reference temperature; for the vapor, statistical thermodynamics provides the free energy function from molecular constants. Combining these functions with experimental vapor‑pressure measurements allows one to determine the heat of sublimation ΔH₀ and to derive an empirical vapor‑pressure equation for the substance. This task reproduces the thermodynamic analysis for nickel oxide (NiO) using published thermochemical data and statistical‑mechanical parameters, starting from a given solid‑phase heat capacity equation and a set of vapor‑pressure observations. The objective is to compute the free energy functions for solid and gaseous NiO over the range 1000–2000 K, deduce the heat of sublimation, and obtain the vapor‑pressure equation.

## Approach
The solid NiO free energy function is obtained from the supplied heat capacity equation 

$$C_p = 13.69 + 0.83\times 10^{-3}\,T - 2.915\times 10^{5}\,T^{-2}$$

together with the enthalpy increment \(H_{298.1}^{\circ} - H_{0}^{\circ} = 1630\;\text{cal}\) and the entropy \(S_{298.1}^{\circ} = 9.22\;\text{cal K}^{-1}\) at 298.1 K, by numerical integration from the reference temperature to each target temperature. The vapor free energy function is evaluated from the statistical‑mechanics expression for a rigid‑rotator harmonic‑oscillator using the molecular weight, reduced mass, vibrational frequency, internuclear distance, and ground‑state electronic multiplicity given as input. The difference between the vapor and solid free energy functions, \(\Delta (F^{\circ} - H_{0}^{\circ})/T\), is then interpolated to the temperatures of the experimental vapor pressure runs. For each run, the heat of sublimation at absolute zero is computed from the thermodynamic relation 

$$\Delta H_{0}^{\circ} = -T\,[R\,\ln p + \Delta (F^{\circ} - H_{0}^{\circ})/T]$$

with \(R = 1.987\;\text{cal mol}^{-1}\text{ K}^{-1}\). The per‑run values are averaged to obtain an experimental heat of sublimation. Finally, the average \(\Delta H_{0}^{\circ}\) and an empirical polynomial representation of \(\Delta (F^{\circ} - H_{0}^{\circ})/T\) are substituted back into the fundamental thermodynamic relation, yielding a vapor‑pressure equation of the form 

$$\log_{10}(p/\text{atm}) = A/T + B\,T + C\,T^{2} + D.$$

## Reproduction target
Compute the free energy functions for solid NiO and gaseous NiO at integer temperatures from 1000 K to 2000 K in steps of 100 K and output a CSV table with columns `T_K`, `F_solid`, `F_vapor`, and `Delta_F_evap` (the difference). Then, using the supplied table of NiO vapor pressures, calculate the heat of sublimation ΔH₀ for each run and the overall average ΔH₀, writing the results as a plain text file. Finally, from the average ΔH₀ and the empirical ΔF_evap representation, derive the vapor‑pressure equation in the form \(\log_{10}(p/\text{atm}) = A/T + B\,T + C\,T^{2} + D\) and output it as a single‑line text file. The deliverables are the three files described in the Workflow Steps; the verifier will compare the computed values against hidden reference expectations.

## Assets

- NiO Vapor Pressure Data (Table VI)
- Python scientific computing environment: numpy, scipy

## Workflow steps

### Step 1: Compute NiO free energy functions for solid and vapor
- Role: scored (load-bearing)
- Action: Compute the free energy function for solid NiO from the given heat capacity equation Cp = 13.69 + 0.83×10⁻³ T – 2.915×10⁵ T⁻², the starting enthalpy H298.1 – H0 = 1630 cal and entropy S298.1 = 9.22 cal/K, by integrating from 298.1 K to each target temperature. Compute the free energy function for gaseous NiO using the statistical‑mechanics expression for a rigid‑rotator harmonic‑oscillator with molecular weight M=74.7, reduced mass μ=1.617×10⁻²³ g, vibrational frequency ν=700 cm⁻¹, internuclear distance r0=1.65×10⁻⁸ cm, and ground‑state multiplicity q=3. Tabulate the temperature, the solid free energy, the vapor free energy, and their difference (ΔF_evap) for integer temperatures from 1000 to 2000 K (100 K steps).
- Output file: `/app/outputs/free_energy_functions.csv`
- Format: csv
- Contract: CSV with header: T_K, F_solid, F_vapor, Delta_F_evap. All values are floating‑point numbers; no missing entries.
- Scoring: scored by hidden verifier

### Step 2: Calculate ΔH₀ for NiO sublimation
- Role: scored
- Action: Read the supplied NiO vapor‑pressure file. For each run compute log₁₀(pressure) and, using the ΔF_evap values from step 1 interpolated to the run temperature, apply the thermodynamic relation ΔH₀ = –T·[R·ln(p) + ΔF_evap] with R = 1.987 cal mol⁻¹ K⁻¹. Output the run number, temperature, log₁₀(p), and ΔH₀; then compute and output the average ΔH₀ over all runs.
- Output file: `/app/outputs/delta_H0_values.txt`
- Format: txt
- Contract: Plain text file. Each run line: 'Run X: T=..., log10(p)=..., ΔH₀=...' (values to 1 decimal). Final line: 'Average ΔH₀ = ... cal/mol'.
- Scoring: scored by hidden verifier

### Step 3: Derive the NiO vapor‑pressure equation
- Role: scored
- Action: Using the average ΔH₀ from step 2 and the empirical representation ΔF_evap = –46.656 + 3.508×10⁻³ T – 3.30×10⁻⁷ T², derive the vapor‑pressure equation in the form log₁₀(p/atm) = A/T + B T + C T² + D. Write the full equation as a single line in the output file.
- Output file: `/app/outputs/vapor_pressure_equation.txt`
- Format: txt
- Contract: Single line of text starting with 'log10(p/atm) = '. Coefficients rounded to 1 decimal for the constant term and to 3 significant figures for others.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_functions.csv`
- `/app/outputs/delta_H0_values.txt`
- `/app/outputs/vapor_pressure_equation.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_functions.csv
- path: `/app/outputs/free_energy_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of free energy functions for solid and gaseous NiO, compared to the paper’s Table VII values with per‑field tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `F_solid`, `F_vapor`, `Delta_F_evap`

### delta_H0_values.txt
- path: `/app/outputs/delta_H0_values.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Per‑run and average ΔH₀; the average is compared to the paper’s 117 055 cal/mol with tolerance ±500 cal.
- schema:
  - `type`: text

### vapor_pressure_equation.txt
- path: `/app/outputs/vapor_pressure_equation.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Vapor‑pressure equation for solid NiO; each coefficient is compared to the paper’s equation (10) with tolerance ±1%.
- schema:
  - `type`: text

Notes: All constants and the bundled vapor‑pressure CSV are taken from the paper. The hidden checker compares the agent’s computed numbers to the paper‑reported values with the stated tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "F_solid",
          "F_vapor",
          "Delta_F_evap"
        ]
      },
      "description": "Table of free energy functions for solid and gaseous NiO, compared to the paper’s Table VII values with per‑field tolerance."
    },
    {
      "file": "delta_H0_values.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Per‑run and average ΔH₀; the average is compared to the paper’s 117 055 cal/mol with tolerance ±500 cal."
    },
    {
      "file": "vapor_pressure_equation.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Vapor‑pressure equation for solid NiO; each coefficient is compared to the paper’s equation (10) with tolerance ±1%."
    }
  ],
  "notes": "All constants and the bundled vapor‑pressure CSV are taken from the paper. The hidden checker compares the agent’s computed numbers to the paper‑reported values with the stated tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of the three stage artifacts and combines them by weight into a final reward between 0 and 1.  
- **Free energy table**: the values at each temperature are compared to reference values with a small per‑field tolerance.  
- **Heat of sublimation ΔH₀**: the average ΔH₀ is compared to an expected value within a specified tolerance.  
- **Vapor‑pressure equation**: the coefficients of the empirical equation are compared to target coefficients with a tolerance per coefficient.  

Simply reporting the paper’s published numbers is not enough; the evaluation checks that your implementation of the thermodynamic pipeline produces consistent, accurate results. The exact gold values and tolerances are hidden.
