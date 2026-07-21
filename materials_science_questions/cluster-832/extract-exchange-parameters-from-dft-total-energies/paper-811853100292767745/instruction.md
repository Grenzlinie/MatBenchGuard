# Exchange couplings and magnetoresistance in magnetically doped carbon nanotubes

## Problem background
When magnetic impurities substitutionally replace carbon atoms in a metallic carbon nanotube, the indirect exchange coupling between impurity moments is mediated by the nanotube's conduction electrons. The sign of this coupling depends on whether the impurities sit on the same sublattice (like sites) or on opposite sublattices (unlike sites) of the hexagonal lattice. This sublattice-dependent sign can either promote collinear magnetic order or lead to frustration when impurities are randomly distributed. The resulting magnetic ground state strongly affects the spin-resolved conductance and the magnetoresistance (MR) — the relative change in conductance when an external field aligns all moments. The size of the MR depends on the impurity species because different d-band occupations shift the coupling sign regime. Computing the exchange coupling constants and the MR for two representative magnetic impurities is therefore key to understanding the magnetotransport properties of doped nanotubes.

## Approach
The calculations are built on an effective single-orbital tight-binding model for a (6,6) carbon nanotube. Substitutional magnetic impurities are described by spin-dependent on-site potentials parameterized by the impurity d-band occupation and exchange splitting. For Ni we use a d-band occupation $n_{\mathrm{Ni}}=0.6$ and exchange splitting $V_x^{\mathrm{Ni}}=0.5\,\mathrm{eV}$; for Mn we use $n_{\mathrm{Mn}}=0.9$ and $V_x^{\mathrm{Mn}}=0.5\,\mathrm{eV}$. The exchange coupling J between a pair of impurities is computed using a Green’s function formalism that relates J to the inter-impurity propagators. This gives the pairwise couplings J_like and J_unlike as a function of separation. Using these couplings, a Heisenberg Hamiltonian governs the spin interactions in a disordered ensemble of impurities. Monte Carlo simulated annealing is used to find the equilibrium spin configurations for random impurity distributions at several concentrations, with equal a priori probability on both sublattices. Finally, the Kubo transport formalism is applied to the spin-resolved conductances (parallel, anti-parallel, and mixed) for the computed spin configurations, both in zero field and with an external aligning field, yielding the magnetoresistance MR = (Γ̄ − Γ)/Γ. The pipeline is executed for two different impurity d-band occupations, corresponding to Ni and Mn, to capture the contrast between frustrated and collinear regimes.

## Reproduction target
Compute (1) the exchange coupling constants J_like and J_unlike at a fixed impurity separation D = 3a for both Ni and Mn on a (6,6) CNT, and (2) the magnetoresistance MR as a function of impurity concentration (c = 0.5%, 1%, 2%, 3%, 4%) for both Ni and Mn. The J values must be written to the JSON file `step_01_j_values.json`. The MR data, including the spin-resolved conductance components and the MR value for each concentration and impurity, must be written to the CSV file `step_02_mr_data.csv` with columns: impurity, concentration, Gamma_up, Gamma_down, Gamma_mixed, MR. Conductances are to be reported in the same arbitrary units; MR is dimensionless.

## Assets

- Python scientific stack: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Construct effective tight-binding model
- Role: process
- Action: Construct a single-orbital tight-binding Hamiltonian for a (6,6) carbon nanotube with substitutional magnetic impurity sites, incorporating spin-dependent on-site potentials parameterized by the impurity d-band occupation and exchange splitting.
- Evidence: `/app/outputs/model_setup.log`

### Step 2: Implement Green’s function method for J(D)
- Role: process
- Action: Implement the Green’s function method to compute the magnetic coupling J(D) between two substitutional impurities for both like and unlike sublattice configurations, using the effective tight-binding Hamiltonian.
- Evidence: `/app/outputs/j_function_impl.log`

### Step 3: Pairwise exchange coupling at D=3a
- Role: scored
- Action: Using the implemented Green’s function method, compute the exchange coupling constants J_like and J_unlike for Ni and Mn impurities at a fixed separation of D=3a (a is the CNT lattice parameter). Output the results as a JSON file.
- Output file: `/app/outputs/step_01_j_values.json`
- Format: json
- Contract: {"Ni": {"J_like": number, "J_unlike": number}, "Mn": {"J_like": number, "J_unlike": number}} (units: eV)
- Scoring: scored by hidden verifier

### Step 4: Monte Carlo simulated annealing of impurity spin configurations
- Role: process
- Action: For concentrations c = 0.5%, 1%, 2%, 3%, 4%, generate random substitutional impurity distributions on the (6,6) CNT with equal a priori probability on both sublattices. Perform Monte Carlo simulated annealing using the Heisenberg Hamiltonian with the pairwise J couplings to determine the equilibrium spin orientations.
- Evidence: `/app/outputs/mc_spin_data.npy`

### Step 5: Magnetoresistance calculation and data
- Role: scored (load-bearing)
- Action: Using the Kubo transport formalism and the spin configurations from the Monte Carlo step, compute the spin-resolved conductances Γ↑↑, Γ↓↓, Γ↑↓, total Γ (no field), and Γ̄ (with external aligning field), and the magnetoresistance MR = (Γ̄ − Γ)/Γ. Average over a sufficient number of disorder realizations to achieve statistical convergence, for both Ni and Mn impurities. Output the results as a CSV file containing the computed quantities for each concentration.
- Output file: `/app/outputs/step_02_mr_data.csv`
- Format: csv
- Contract: columns: impurity (Ni/Mn), concentration (float), Gamma_up (float), Gamma_down (float), Gamma_mixed (float), MR (float). Conductances in same arbitrary units; MR dimensionless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_j_values.json`
- `/app/outputs/step_02_mr_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_j_values.json
- path: `/app/outputs/step_01_j_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Exchange coupling constants for Ni and Mn on a (6,6) CNT at D=3a, for like and unlike sublattice configurations.
- schema:
  - `type`: object
  - `required`: `Ni`, `Mn`
  - `items`:
    - `Ni`:
      - `J_like`: number (eV)
      - `J_unlike`: number (eV)
    - `Mn`:
      - `J_like`: number (eV)
      - `J_unlike`: number (eV)

### step_02_mr_data.csv
- path: `/app/outputs/step_02_mr_data.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Spin-resolved conductances and magnetoresistance MR for Ni and Mn as functions of impurity concentration. MR computed as (Γ̄−Γ)/Γ; conductances (Gamma_up, Gamma_down, Gamma_mixed) in consistent arbitrary units.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `concentration`, `Gamma_up`, `Gamma_down`, `Gamma_mixed`, `MR`
  - `units`:
    - `MR`: dimensionless
    - `conductances`: same arbitrary units

Notes: The scoring checks that the exchange coupling signs and magnitudes are consistent with the paper-reported reference values, and that the MR data meets the thresholds for frustration (Ni MR low, Mn MR high with vanishing mixed conductance).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_j_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ni",
          "Mn"
        ],
        "items": {
          "Ni": {
            "J_like": "number (eV)",
            "J_unlike": "number (eV)"
          },
          "Mn": {
            "J_like": "number (eV)",
            "J_unlike": "number (eV)"
          }
        }
      },
      "description": "Exchange coupling constants for Ni and Mn on a (6,6) CNT at D=3a, for like and unlike sublattice configurations."
    },
    {
      "file": "step_02_mr_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "concentration",
          "Gamma_up",
          "Gamma_down",
          "Gamma_mixed",
          "MR"
        ],
        "units": {
          "MR": "dimensionless",
          "conductances": "same arbitrary units"
        }
      },
      "description": "Spin-resolved conductances and magnetoresistance MR for Ni and Mn as functions of impurity concentration. MR computed as (Γ̄−Γ)/Γ; conductances (Gamma_up, Gamma_down, Gamma_mixed) in consistent arbitrary units."
    }
  ],
  "notes": "The scoring checks that the exchange coupling signs and magnitudes are consistent with the paper-reported reference values, and that the MR data meets the thresholds for frustration (Ni MR low, Mn MR high with vanishing mixed conductance)."
}
```

## How you are scored
A hidden verifier independently examines the two scored output files. For the exchange couplings in `step_01_j_values.json`, it compares the reported J_like and J_unlike values to hidden reference values derived from the original study, checking that the signs are correct and the magnitudes are within a physically reasonable range. For the magnetoresistance data in `step_02_mr_data.csv`, the verifier inspects the MR curve and the mixed conductance component across concentrations, verifying that the data satisfy threshold conditions that distinguish the frustrated and collinear regimes (e.g., MR magnitude and vanishing of mixed conductance where appropriate). Each scored artifact contributes a portion of the total reward; the final score is the weighted sum. Accurate execution of the full computational pipeline is essential — results that are not backed by the tight-binding, Green’s function, Monte Carlo, and Kubo transport steps will not earn credit.
