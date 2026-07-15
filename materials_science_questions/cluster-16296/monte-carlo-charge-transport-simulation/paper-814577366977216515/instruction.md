# Kinetic Monte Carlo Transport Simulation in Disordered Semiconductors

## Problem background
In highly doped disordered organic semiconductors, the temperature- and electric-field dependence of the conductivity can be analyzed using two scaling frameworks: universal scaling (US) and the effective temperature (Marianer-Shklovskii, MS) concept. Both frameworks aim to collapse conductivity data onto universal curves and are linked to the heating of the charge carrier distribution under an applied electric field. Kinetic Monte Carlo (MC) simulations of nearest-neighbor hopping on a lattice with Gaussian disorder and Coulomb interactions provide a controlled testbed to examine these scaling phenomena. From the simulated current-voltage characteristics, one can extract the Ohmic conductivity exponent \(\alpha\), the Marianer-Shklovskii parameters \(\delta, \varsigma, a\), and the effective temperature exponent \(\alpha_{\text{eff}}\). The goal of this task is to implement such a simulation and compute these exponents.

## Approach
The core idea is to model charge transport as Miller–Abrahams nearest-neighbor hopping on a cubic lattice with a Gaussian distribution of site energies (width 0.1 eV). Charge carriers interact via Coulomb potentials (relative permittivity 3.6). The simulation is run for several lattice temperatures and applied electric fields, averaging over multiple disorder realizations, to obtain steady-state current densities \(j(F,T)\). From these data, the Ohmic conductivity at low fields is extracted as a function of temperature, and a power law \(\sigma(0,T) \propto T^{\alpha}\) is fitted to obtain \(\alpha\). For each field and temperature, an effective temperature \(T_{\text{eff}}\) is determined by matching the finite-field conductivity to the Ohmic curve: \(\sigma(0,T_{\text{eff}}) = \sigma(F,T)\). The set of \(T_{\text{eff}}, T_{\text{latt}}, F\) triplets is fitted to the Marianer-Shklovskii expression \(T_{\text{eff}}^{\varsigma} = T_{\text{latt}}^{\varsigma} + (\delta e F a / k_B)^{\varsigma}\) to yield \(\delta, \varsigma, a\). Finally, \(\sigma(F,T)\) is plotted against \(T_{\text{eff}}\) and fitted to a power law \(\sigma \propto T_{\text{eff}}^{\alpha_{\text{eff}}}\) to obtain the effective temperature exponent \(\alpha_{\text{eff}}\). The workflow writes all five parameters to a scored JSON artifact.

## Reproduction target
Implement the kinetic Monte Carlo simulation using the specified system parameters (cubic lattice, lattice constant 1.8 nm, relative permittivity 3.6, Gaussian disorder width 0.1 eV, carrier concentration \(c=0.1\), Miller–Abrahams hopping rates). Run simulations at lattice temperatures \(T = 300, 350, 400, 450, 500\) K and electric fields spanning \(10^5\)–\(10^7\) V/m, averaging over at least 20 independent disorder configurations. From the resulting current-voltage data, extract the five scaling parameters: Ohmic exponent \(\alpha\), Marianer-Shklovskii parameters \(\delta\), \(\varsigma\), and \(a\) (in nm), and effective-temperature exponent \(\alpha_{\text{eff}}\). Write these five values as a JSON object to `/app/outputs/parameters.json`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run Kinetic Monte Carlo simulation
- Role: process
- Action: Implement a kinetic Monte Carlo simulation of nearest-neighbor hopping on a cubic lattice. Use Gaussian energetic disorder of width 0.1 eV, Coulomb interactions with relative permittivity 3.6, carrier concentration c=0.1 (100 charges in a 10×10×10 box), lattice constant a=1.8 nm, and Miller–Abrahams hopping rates. Simulate at lattice temperatures T = 300, 350, 400, 450, 500 K and electric fields spanning 1e5 to 1e7 V/m, averaging over at least 20 independent disorder configurations. For each (F,T) pair compute the steady-state current density j(F,T) and save the raw current-voltage data for subsequent analysis.
- Evidence: `/app/outputs/iv_data.csv`

### Step 2: Extract scaling parameters
- Role: scored (load-bearing)
- Action: From the simulated j(F,T) data, extract the Ohmic conductivity at low bias and fit σ(0,T) ∝ T^α to obtain the exponent α. For each field and lattice temperature pair, determine the effective temperature T_eff by interpolating the Ohmic curve such that σ(0,T_eff) = σ(F,T). Fit the Marianer–Shklovskii expression T_eff^ς = T_latt^ς + (δ e F a / k_B)^ς to the (T_latt, F, T_eff) data to obtain δ, ς, and a (where e is the elementary charge and k_B is the Boltzmann constant). Finally, fit σ(F,T) versus T_eff to a power law σ ∝ T_eff^{α_eff} to obtain the effective temperature exponent α_eff. Write all five parameters to a JSON file.
- Output file: `/app/outputs/parameters.json`
- Format: json
- Contract: {"ohmic_alpha": float, "ms_delta": float, "ms_zeta": float, "ms_a_nm": float, "alpha_eff": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### parameters.json
- path: `/app/outputs/parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scaling parameters obtained from the kinetic Monte Carlo simulation: Ohmic exponent α, Marianer–Shklovskii parameters δ, ς, and a (in nm), and the effective temperature exponent α_eff.
- schema:
  - `type`: object
  - `required`: `ohmic_alpha`, `ms_delta`, `ms_zeta`, `ms_a_nm`, `alpha_eff`
  - `properties`:
    - `ohmic_alpha`:
      - `type`: number
    - `ms_delta`:
      - `type`: number
    - `ms_zeta`:
      - `type`: number
    - `ms_a_nm`:
      - `type`: number
    - `alpha_eff`:
      - `type`: number

Notes: The MC simulation uses a lattice constant of 1.8 nm, relative permittivity 3.6, Gaussian disorder width 0.1 eV, carrier concentration c=0.1, temperatures 300–500 K, and electric fields in the range 1e5–1e7 V/m. The extraction follows standard procedures described in the field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "ohmic_alpha",
          "ms_delta",
          "ms_zeta",
          "ms_a_nm",
          "alpha_eff"
        ],
        "properties": {
          "ohmic_alpha": {
            "type": "number"
          },
          "ms_delta": {
            "type": "number"
          },
          "ms_zeta": {
            "type": "number"
          },
          "ms_a_nm": {
            "type": "number"
          },
          "alpha_eff": {
            "type": "number"
          }
        }
      },
      "description": "Scaling parameters obtained from the kinetic Monte Carlo simulation: Ohmic exponent α, Marianer–Shklovskii parameters δ, ς, and a (in nm), and the effective temperature exponent α_eff."
    }
  ],
  "notes": "The MC simulation uses a lattice constant of 1.8 nm, relative permittivity 3.6, Gaussian disorder width 0.1 eV, carrier concentration c=0.1, temperatures 300–500 K, and electric fields in the range 1e5–1e7 V/m. The extraction follows standard procedures described in the field."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/parameters.json` and compares each of the five reported parameters to independently stored reference values using absolute tolerances. The final score is a weighted sum: full credit if all five parameters lie within their respective tolerance windows, and partial credit proportional to the number of parameters within tolerance. The verifier does not re-run your simulation; it trusts the numbers you report and checks them against hidden benchmarks. Submitting a correctly formatted JSON with plausible values is required to receive any credit.
