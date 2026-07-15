# Compute SiC Active-Passive Transition Pressures under CO2 via Dynamic Mass Transfer Model

## Problem background
Silicon carbide (SiC) is a candidate material for aerospace applications where it may be exposed to high-temperature, low-pressure carbon dioxide atmospheres, such as during Martian atmospheric entry. Under these conditions, SiC can undergo passive oxidation—forming a protective silica (SiO2) layer—or active oxidation, where SiO gas is vaporized and the material is etched away. The pressure and temperature conditions that separate these two regimes (the active-to-passive transition) are critical for predicting material lifetime and performance. This work computationally determines the transition boundary (CO2 total pressure as a function of temperature) using two theoretical models and compares them.

## Approach
Two distinct computational models are used, both requiring equilibrium constants derived from standard public thermochemical data for the Si–C–O system. The first is a closed-system equilibrium model (analogous to Solgasmix) that minimizes total free enthalpy at fixed temperature and total CO2 pressure, iteratively searching for the pressure at which solid SiO2 becomes thermodynamically stable. The second is an open-system dynamic model that couples gas-phase mass transfer with local thermochemical equilibria at the SiC surface. It considers five gas species (SiO, CO2, CO, O2, O) diffusing and convecting through a boundary layer. Mass conservation at the interface and four equilibrium reactions (active oxidation of SiC to SiO, passive oxidation to SiO2, CO2/CO/O2 interconversion, and O2 dissociation) yield a set of coupled nonlinear algebraic equations. Numerical solution of this system gives the bulk CO2 pressure at which a protective SiO2 layer becomes favorable. Gas-phase transport parameters (diffusion coefficients and boundary layer thicknesses) must be estimated from Chapman–Enskog theory and the geometry/flow of the MESOX solar oxidation facility described in the literature.

## Reproduction target
Produce two ordered lists of CO2 total pressure (in Pa) that define the active-to-passive transition for SiC in pure CO2 at temperatures 1600, 1700, 1800, 1900, 2000, and 2100 K. The first list corresponds to the closed-system equilibrium (Solgasmix-like) pressures; the second list corresponds to the open-system dynamic model pressures. Both lists must be strictly increasing with temperature. Additionally, compute SiO partial pressures at the SiO2 surface under pure CO2 and pure CO at 1600 K and 2000 K for total pressures of 100 Pa and 10 000 Pa as supporting results. All results must be written to the specified JSON output files.

## Assets

- Standard thermochemical database for Si-C-O species: https://cearun.grc.nasa.gov/
- Gas-phase transport properties and boundary layer thickness
- NumPy: pip install numpy
- SciPy: pip install scipy

## Workflow steps

### Step 1: Obtain thermochemical data and compute equilibrium constants
- Role: process
- Action: Retrieve standard Gibbs free energies from a public thermochemical database for the Si-C-O species. For each temperature (1600-2100 K) compute the equilibrium constants K1 (SiC+2CO2=SiO+3CO), K2 (SiC+3CO2=SiO2+4CO), K3 (CO2=CO+0.5O2), K4 (O2=2O) using thermodynamic relations.
- Evidence: `/app/outputs/equilibrium_constants.json`

### Step 2: Closed-system equilibrium transition pressures (Solgasmix)
- Role: scored
- Action: For each temperature, determine the CO2 total pressure at which passive oxidation (SiO2 formation) becomes thermodynamically favorable by free-enthalpy minimization or equilibrium condition solving. Output the list of pressures in Pa.
- Output file: `/app/outputs/solgasmix_transition_pressures.json`
- Format: json
- Contract: JSON array of 6 numbers in the order of increasing temperature: 1600 K, 1700 K, 1800 K, 1900 K, 2000 K, 2100 K. Units: Pa.
- Scoring: scored by hidden verifier

### Step 3: Estimate gas-phase transport parameters
- Role: process
- Action: Obtain or compute the diffusion coefficients D_i and boundary layer thicknesses delta_i for all gas species in CO2 at the relevant temperatures. Derive the ratios D_i/delta_i used in the dynamic model.
- Evidence: `/app/outputs/transport_parameters.json`

### Step 4: Implement dynamic model equations
- Role: process
- Action: Construct the nonlinear system of two equations that couples mass transfer and interface equilibria, using the equilibrium constants K1-K4 and transport ratios. Implement a numerical solver (e.g., stabilized relaxation or Newton-type method) to compute the unknown interface CO partial pressure and bulk CO2 pressure.
- Evidence: none

### Step 5: Dynamic open-system transition pressures
- Role: scored (load-bearing)
- Action: For each temperature (1600-2100 K), solve the dynamic model to find the transition CO2 pressure P_CO2^∞ (bulk) at which passive oxidation begins. Output the list of pressures in Pa.
- Output file: `/app/outputs/dynamic_transition_pressures.json`
- Format: json
- Contract: JSON array of 6 numbers in the order of increasing temperature: 1600 K, 1700 K, 1800 K, 1900 K, 2000 K, 2100 K. Units: Pa.
- Scoring: scored by hidden verifier

### Step 6: Supporting: SiO partial pressure calculation
- Role: process
- Action: Using the equilibrium model, compute the SiO partial pressure at the SiO2 surface under pure CO2 and pure CO at total pressures 100 Pa and 10000 Pa for temperatures 1600 K and 2000 K, as done in Table 4 of the paper.
- Evidence: `/app/outputs/sio_partial_pressures.json`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/solgasmix_transition_pressures.json`
- `/app/outputs/dynamic_transition_pressures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### solgasmix_transition_pressures.json
- path: `/app/outputs/solgasmix_transition_pressures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Closed-system equilibrium transition pressures computed by free-energy minimization.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
  - `minItems`: 6
  - `maxItems`: 6
  - `description`: Ordered list of CO2 total transition pressure (Pa) for temperatures 1600, 1700, 1800, 1900, 2000, 2100 K.

### dynamic_transition_pressures.json
- path: `/app/outputs/dynamic_transition_pressures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Open-system dynamic model transition pressures with mass transfer coupling.
- schema:
  - `type`: array
  - `items`:
    - `type`: number
  - `minItems`: 6
  - `maxItems`: 6
  - `description`: Ordered list of CO2 total transition pressure (Pa) for temperatures 1600, 1700, 1800, 1900, 2000, 2100 K from the open-system dynamic model.

Notes: Verification compares submitted arrays to paper-reported values (Table 1 and Table 2) with a generous tolerance to allow for differences in thermochemical databases and transport estimates. Both arrays must be strictly increasing with temperature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "solgasmix_transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "minItems": 6,
        "maxItems": 6,
        "description": "Ordered list of CO2 total transition pressure (Pa) for temperatures 1600, 1700, 1800, 1900, 2000, 2100 K."
      },
      "description": "Closed-system equilibrium transition pressures computed by free-energy minimization."
    },
    {
      "file": "dynamic_transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "number"
        },
        "minItems": 6,
        "maxItems": 6,
        "description": "Ordered list of CO2 total transition pressure (Pa) for temperatures 1600, 1700, 1800, 1900, 2000, 2100 K from the open-system dynamic model."
      },
      "description": "Open-system dynamic model transition pressures with mass transfer coupling."
    }
  ],
  "notes": "Verification compares submitted arrays to paper-reported values (Table 1 and Table 2) with a generous tolerance to allow for differences in thermochemical databases and transport estimates. Both arrays must be strictly increasing with temperature."
}
```

## How you are scored
A hidden verifier independently evaluates each of the two transition-pressure arrays (solgasmix and dynamic). The arrays are compared to reference values derived from the study using a tolerance that accounts for legitimate differences in thermochemical databases and transport estimates, so a correct re-implementation should fall within the allowed margin. The verifier also checks that each array is strictly increasing with temperature. The final reward is a weighted combination: a majority of the weight comes from the fraction of pressures that satisfy the tolerance, and the remaining weight is based on the monotonicity check. Simply reporting numbers that match published tables is not sufficient; the workflow must produce the prescribed output files and the numbers must arise from genuine computations.
