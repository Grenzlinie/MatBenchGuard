# Carbon isoactivity and graphite solubility in C-Fe-Ni using CALPHAD

## Problem background
The C-Fe-Ni system is critical in steel and alloy processing. The CALPHAD (CALculation of PHAse Diagrams) approach models the Gibbs energy of individual phases using parameters optimized against experimental data. A reliable thermodynamic description enables prediction of phase equilibria, chemical activities, and solubilities. A recent assessment provided a set of Gibbs energy parameters for several phases in this ternary, validated by carbon activity and graphite solubility measurements. This task reproduces a core part of that work: computing two key thermodynamic quantities from the given model and parameters.

## Approach
Implement the two-sublattice Gibbs energy model for the fcc phase (including a magnetic ordering contribution) and a subregular solution model for the liquid phase, using the parameter values that are provided. The fcc model treats interstitial carbon and substitutional Fe/Ni on separate sublattices, while the liquid model treats all three elements with composition-dependent excess terms. Hardcode all necessary parameters into a Python script using pycalphad. Then perform two computations:
1) At 1273 K, evaluate the carbon activity across a regular grid of Fe and Ni compositions covering the full composition range, producing carbon isoactivity data.
2) At 1823 K, for each Ni content, solve for the carbon mole fraction in the liquid that makes the chemical potential of carbon equal to that of pure graphite, yielding the graphite solubility curve.

## Reproduction target
The task has two scored targets:
1) A CSV file (`fcc_isoactivity_1273K.csv`) containing computed carbon activity values (a_C, dimensionless) in the fcc phase at 1273 K, along with temperature and Fe/Ni/C mole fractions, across a regular composition grid.
2) A CSV file (`liquid_solubility_1823K.csv`) containing the saturated carbon mole fraction in the liquid phase (x_C_saturated) in equilibrium with graphite at 1823 K, as a function of nickel content (x_Ni_liquid), with temperature.

## Assets

- pycalphad: https://pypi.org/project/pycalphad/
- pandas: https://pypi.org/project/pandas/
- numpy: https://pypi.org/project/numpy/


## Thermodynamic parameters
All Gibbs energy parameters from the paper's Appendix 1 needed for the fcc and liquid phases are listed below in SI units (energy in J/mol, temperature in K, gas constant R=8.31448). The reference states follow SER (Stable Element Reference).

### Graphite (reference for carbon)
The Gibbs energy of graphite relative to SER is:
```
G_gra = -17369 + 170.73*T - 24.3*T*ln(T) - 4.723e-4*T^2
        + 2562600/T - 2.643e8/T^2 + 1.2e10/T^3  (T in K)
```

### fcc phase (two-sublattice model)
Sublattice  1 : (Fe,Ni) with a=1.
Sublattice  2 : (C,Va) with c=1.

Pure-element Gibbs energies (non-magnetic):
```
For 298.15 < T < 1811:
  G_Fe_VA = -237.57 + 132.416*T - 24.6643*T*ln(T) - 3.75752e-3*T^2
              - 5.89269e-8*T^3 + 77358.5/T
For 1811 < T < 6000:
  G_Fe_VA = 27098.266 + 300.25256*T - 46*T*ln(T) + 2.78854e31*T**(-9)

For 298.15 < T < 1728:
  G_Ni_VA = -5179.159 + 117.854*T - 22.096*T*ln(T) - 4.8407e-3*T^2
For 1728 < T < 6000:
  G_Ni_VA = -27840.655 + 279.135*T - 43.1*T*ln(T) + 1.12754e31*T**(-9)
```

End-member compounds with carbon:
```
G_Fe_C  = G_Fe_VA + G_gra + 77207 - 15.877*T
G_Ni_C  = G_Ni_VA + G_gra + 45000 + 1.88*T
```

Interaction parameters (J/mol):
```
 L_Fe:Va,C  = -34671
 0_L_Fe,Ni:Va = -12054.355 + 3.27413*T
 1_L_Fe,Ni:Va =  11082.1315 - 4.45077*T
 2_L_Fe,Ni:Va =  -725.805174
 0_L_Fe,Ni:C  =   49074 - 7.32*T
 1_L_Fe,Ni:C  =  -25800
```

Magnetic contribution:
```
G_mo = R*T*ln(B+1)*f(t)   with t = T/Tc

For t < 1:
  f(t) = 1 - 0.86034*t**(-1) - 0.1745*t**3 - 7.755e-3*t**9 - 1.745e-3*t**15
For t > 1:
  f(t) = -4.269e-2*t**(-5) - 1.355e-3*t**(-15) - 2.846e-4*t**(-25)

  Tc = -201*y_Fe + 633*y_Ni + y_Fe*y_Ni*y_Va*(2133 - 682*(y_Fe - y_Ni))
  B  = -2.1*y_Fe + 0.52*y_Ni
       + y_Fe*y_Ni*y_Va*(9.55 + 7.23*(y_Fe - y_Ni) + 5.93*(y_Fe - y_Ni)^2
                       + 6.18*(y_Fe - y_Ni)^3)
```
Note: y_Fe, y_Ni are site fractions on the first sublattice; y_Va is the site fraction of vacancies on the second sublattice (i.e., 1 - y_C).

### Liquid phase (subregular solution)
Single sublattice, constituents (C,Fe,Ni).

Pure-element Gibbs energies (J/mol):
```
G_C_liq  = 100000 + 146.1*T - 24.3*T*ln(T) - 4.723e-4*T^2
          + 2562600/T - 2.643e8/T^2 + 1.2e10/T^3

For 298.15 < T < 1811:
  G_Fe_liq = G_Fe_VA + 12040.17 - 6.55843*T - 3.6751551e-21*T**7
For 1811 < T < 6000:
  G_Fe_liq = -10839.7 + 291.302*T - 46*T*ln(T)

For 298.15 < T < 1728:
  G_Ni_liq = 11235.527 + 108.457*T - 22.096*T*ln(T) - 4.8407e-3*T**2
            - 3.82318e-21*T**7
For 1728 < T < 6000:
  G_Ni_liq = -9549.775 + 268.598*T - 43.1*T*ln(T)
```

Binary interaction parameters (J/mol):
```
 0_L_Fe,C  = -124320 + 28.5*T
 1_L_Fe,C  =  19300
 2_L_Fe,C  =  49260 - 19*T
 0_L_Ni,C  = -110160 + 34.6*T
 0_L_Fe,Ni = -18378.86 + 6.03912*T
 1_L_Fe,Ni =   9228.1 - 3.54642*T
```

Ternary interaction:
```
L_C,Fe,Ni = 122200 - 58.8*T - 30000*(x_Fe - x_Ni)
```

## Workflow steps

### Step 1: Implement Gibbs energy models and hardcode parameters
- Role: process
- Action: Implement the two-sublattice Gibbs energy model for the fcc phase (including magnetic contribution) and the subregular solution model for the liquid phase as described in the paper, using the parameter values from the paper's appendix. Hardcode all necessary parameters into a Python script using pycalphad.
- Evidence: `/app/outputs/model_setup.py`

### Step 2: Compute fcc carbon isoactivity lines at 1273 K
- Role: scored (load-bearing)
- Action: Use the implemented fcc model to calculate the carbon activity as a function of Fe and Ni composition at 1273 K over a regular grid covering the full composition range. Output a CSV file with columns: T (K), x_Ni (mole fraction), x_Fe (mole fraction), x_C (mole fraction), a_C (dimensionless).
- Output file: `/app/outputs/fcc_isoactivity_1273K.csv`
- Format: csv
- Contract: Columns: T (K), x_Ni (mole fraction), x_Fe (mole fraction), x_C (mole fraction), a_C (dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Compute liquid graphite solubility at 1823 K
- Role: scored
- Action: Using the liquid phase model, compute the equilibrium graphite solubility (saturated carbon content) as a function of nickel content at 1823 K. For each nickel mole fraction, solve for the carbon mole fraction that satisfies equality of carbon chemical potential between liquid and graphite. Output a CSV file with columns: T (K), x_Ni_liquid (mole fraction), x_C_saturated (mole fraction).
- Output file: `/app/outputs/liquid_solubility_1823K.csv`
- Format: csv
- Contract: Columns: T (K), x_Ni_liquid (mole fraction), x_C_saturated (mole fraction)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fcc_isoactivity_1273K.csv`
- `/app/outputs/liquid_solubility_1823K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fcc_isoactivity_1273K.csv
- path: `/app/outputs/fcc_isoactivity_1273K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Carbon activity in fcc phase at 1273 K as a function of composition
- schema:
  - `type`: table
  - `required_columns`: `T`, `x_Ni`, `x_Fe`, `x_C`, `a_C`
  - `units`:
    - `T`: K
    - `x_Ni`: mole fraction
    - `x_Fe`: mole fraction
    - `x_C`: mole fraction
    - `a_C`: dimensionless

### liquid_solubility_1823K.csv
- path: `/app/outputs/liquid_solubility_1823K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Saturated carbon content (graphite solubility) in liquid phase at 1823 K vs. nickel content
- schema:
  - `type`: table
  - `required_columns`: `T`, `x_Ni_liquid`, `x_C_saturated`
  - `units`:
    - `T`: K
    - `x_Ni_liquid`: mole fraction
    - `x_C_saturated`: mole fraction

Notes: The computed data are compared to hidden reference values with a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fcc_isoactivity_1273K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "x_Ni",
          "x_Fe",
          "x_C",
          "a_C"
        ],
        "units": {
          "T": "K",
          "x_Ni": "mole fraction",
          "x_Fe": "mole fraction",
          "x_C": "mole fraction",
          "a_C": "dimensionless"
        }
      },
      "description": "Carbon activity in fcc phase at 1273 K as a function of composition"
    },
    {
      "file": "liquid_solubility_1823K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "x_Ni_liquid",
          "x_C_saturated"
        ],
        "units": {
          "T": "K",
          "x_Ni_liquid": "mole fraction",
          "x_C_saturated": "mole fraction"
        }
      },
      "description": "Saturated carbon content (graphite solubility) in liquid phase at 1823 K vs. nickel content"
    }
  ],
  "notes": "The computed data are compared to hidden reference values with a relative tolerance."
}
```

## How you are scored
A hidden verifier reads the two CSV files and independently evaluates their contents. The verifier compares the computed carbon activity values at a set of held-out compositions against reference values derived from experimental data. Similarly, it compares the computed graphite solubility values at selected nickel contents against reference values. The two scored artifacts are combined with weights to produce the final reward. Simply reporting numbers is not enough; the verifier judges the correctness of the computed thermodynamic quantities.
