# Thermodynamic modeling of In-N cluster self-assembling in GaP

## Problem background
GaP:N is a promising material for ensembles of single photon sources, but large internal strains around isolated nitrogen atoms cause inhomogeneous emission energy. Co-doping with In can reduce strain through self-assembling of 4N10In and 1N4In impurity clusters. The alloy becomes GaP-rich In_xGa_{1-x}N_yP_{1-y}, where the equilibrium distribution of In and N atoms among isolated sites and the two cluster types is determined by thermodynamic competition between bonding preferences (InN+GaP over InP+GaN) and strain compensation. The main quantitative outcome is the cluster order parameters α (fraction of N atoms in 4N10In clusters) and β (fraction in 1N4In clusters) as functions of temperature and impurity content. Your task is to compute these order parameters from the Helmholtz free energy model described in the approach.

## Approach
The free energy per unit cell (or per formula unit) is g = g⁰ + u − T s, where g⁰ is the sum of free energies of the four constituent binary compounds InN, InP, GaN, GaP; u is the strain energy from impurity-induced lattice distortions; and Ts is the configurational entropy of mixing of impurities and clusters. Two cluster types are considered: 4N10In (a nitrogen tetrahedron surrounded by 10 In atoms) and 1N4In (a nitrogen atom surrounded by 4 In atoms). Their formation is parametrized by the cluster order parameters α and β, both in [0,1] with α+β ≤ 1, representing the fractions of total nitrogen atoms that reside in each cluster type, bounded by the overall impurity concentrations x (In) and y (N). The free-energy difference Δμ⁰(T) = μ_InN − μ_InP − μ_GaN + μ_GaP is computed from standard thermochemical data (enthalpies of formation, entropies, and heat capacities) using their temperature dependence. Strain energies u_In, u_N, u_4N10In, u_1N4In are obtained from a valence force field (VFF) model with elastic constants taken from the literature. The configurational entropy term −Ts (with R the gas constant and T in Kelvin) is given explicitly by:

$$
-Ts = RT(1-\alpha)y\ln\frac{(1-\alpha)y}{1-\alpha y} + RT(1-y)\ln\frac{1-y}{1-\alpha y}
      + RT\left(x - \frac{10}{4}\alpha y - 4\beta y\right)\ln\frac{x - \frac{10}{4}\alpha y - 4\beta y}{1 - \frac{10}{4}\alpha y - 4\beta y}
      + RT(1-x)\ln\frac{1-x}{1 - \frac{10}{4}\alpha y - 4\beta y}
      + RT(1-\alpha-\beta)y\ln\frac{1-\alpha-\beta}{1-\alpha}
      + RT\beta y\ln\frac{\beta}{1-\alpha}
      + \frac{1}{10}RT\alpha y\ln\frac{27\alpha y}{20}
      + \frac{2}{27}RT\ln\frac{20-27\alpha y}{20}.
$$

All terms are per mole of formula units. Use this expression directly in the free energy minimization. For each target alloy composition (x,y) and temperature, the total free energy g(α,β) is minimized numerically to find the equilibrium order parameters. Your implementation should compute these quantities step by step as outlined in the workflow below.

## Reproduction target
For the GaP-rich In_xGa_{1-x}N_yP_{1-y} alloy, compute the equilibrium cluster order parameters α (COP_4N10In) and β (COP_1N4In) for the following impurity content sets:
- x = y = 1.0 × 10⁻⁵
- x = 1.0 × 10⁻³, y = 1.0 × 10⁻⁵
- x = 1.0 × 10⁻², y = 1.0 × 10⁻⁴
For each composition, evaluate at temperatures from 0 °C to 1000 °C in steps of 100 °C (i.e., 0, 100, 200, ..., 1000 °C). Use the free energy model g = g⁰ + u − T s with the computed Δμ⁰(T) and strain energies, and minimize g with respect to α and β subject to the constraints α ≥ 0, β ≥ 0, α + β ≤ 1. Write the resulting cluster order parameters to the file cluster_order_parameters.csv with columns: composition_x, composition_y, temperature_C, COP_4N10In, COP_1N4In. The rows must cover the full set of (x,y,T) combinations (33 rows total).

## Assets

- Landolt-Börnstein thermochemical data (InN, InP, GaN, GaP)
- Valence force field elastic constants (Martin, Phys. Rev. B 1, 4005, 1970): 10.1103/PhysRevB.1.4005
- Additional elastic constants (Elyukhin & Nikishin, Semicond. Sci. Technol. 11, 917, 1996): 10.1088/0268-1242/11/6/004
- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute free-energy difference Δμ⁰(T)
- Role: process
- Action: Using standard thermochemical data (enthalpies of formation, entropies, heat capacities from Landolt-Börnstein), compute Δμ⁰(T) = μ_InN - μ_InP - μ_GaN + μ_GaP as a function of temperature. Write the results to delta_mu0_function.json.
- Evidence: `/app/outputs/delta_mu0_function.json`

### Step 2: Estimate strain energies of impurities and clusters
- Role: process
- Action: Using the valence force field model with elastic constants from Martin (Phys. Rev. B 1, 4005) and Elyukhin & Nikishin (Semicond. Sci. Technol. 11, 917), compute the strain energies u_In, u_N, u_4N10In, u_1N4In for an isolated In atom, isolated N atom, 4N10In cluster and 1N4In cluster in a GaP matrix. Write the results to strain_energies.json.
- Evidence: `/app/outputs/strain_energies.json`

### Step 3: Minimize free energy to obtain equilibrium cluster order parameters
- Role: scored (load-bearing)
- Action: For each specified alloy composition (x,y) and temperature (0–1000 °C), construct the Helmholtz free energy g(α,β) = g⁰ + u − T s using the computed Δμ⁰(T) and strain energies, and the configurational entropy expression. Find α and β that minimize g, subject to 0 ≤ α+β ≤ 1 and α,β ≥ 0. Write the resulting COP values to cluster_order_parameters.csv.
- Output file: `/app/outputs/cluster_order_parameters.csv`
- Format: csv
- Contract: Columns: composition_x (float), composition_y (float), temperature_C (float), COP_4N10In (float in [0,1]), COP_1N4In (float in [0,1]).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_order_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_order_parameters.csv
- path: `/app/outputs/cluster_order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium cluster order parameters (α for 4N10In and β for 1N4In) for the required (x,y,T) combinations. The required conditions are: (x=y=1e-5) for T = 0,100,...,1000 °C; (x=1e-3, y=1e-5) for the same temperatures; (x=1e-2, y=1e-4) for the same temperatures. The columns should be comma-separated, with temperature in degrees Celsius.
- schema:
  - `required_columns`: `composition_x`, `composition_y`, `temperature_C`, `COP_4N10In`, `COP_1N4In`

Notes: The hidden reference values are digitised from the paper's figures and used to score within a tolerance. No further environmental details are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "composition_x",
          "composition_y",
          "temperature_C",
          "COP_4N10In",
          "COP_1N4In"
        ]
      },
      "description": "Equilibrium cluster order parameters (α for 4N10In and β for 1N4In) for the required (x,y,T) combinations. The required conditions are: (x=y=1e-5) for T = 0,100,...,1000 °C; (x=1e-3, y=1e-5) for the same temperatures; (x=1e-2, y=1e-4) for the same temperatures. The columns should be comma-separated, with temperature in degrees Celsius."
    }
  ],
  "notes": "The hidden reference values are digitised from the paper's figures and used to score within a tolerance. No further environmental details are required."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier inspects your cluster_order_parameters.csv and performs several checks:
- Structural correctness: the file must contain all required rows and columns with correct data types; the COP values must lie in [0,1].
- Physical consistency: the COP values must exhibit expected monotonic trends (e.g., decreasing with increasing temperature) and satisfy the constraints α ≥ 0, β ≥ 0, α+β ≤ 1. The verifier examines these patterns without requiring an exact match to any curve.
- Reference comparison: the verifier holds hidden reference cluster order parameters obtained from an independent implementation of the same thermodynamic model. Your computed α and β values will be compared against these references, and closeness is rewarded.
The final score is a number between 0 and 1 that combines the outcome of these checks, with the reference comparison being the primary contributor. You are expected to faithfully implement the model and optimization as described; do not attempt to guess or reverse‑engineer the reference values.
