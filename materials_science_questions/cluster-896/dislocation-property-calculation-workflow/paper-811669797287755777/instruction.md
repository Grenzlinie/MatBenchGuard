# Monte Carlo Simulation of Thermal Etching of Silicon {111} Surfaces with Intersecting Dislocations

## Problem background
This task investigates equilibrium roughening and dislocation-nucleated thermal etching of diamond-cubic {111} surfaces using a modified solid-on-solid (SOS) Monte Carlo model. The fundamental question is how a dislocation's energy field modifies the surface roughening transition and the rate of etching under a chemical potential driving force. The target results are the surface specific heat as a function of temperature (which reveals characteristic roughening behaviour) and the normal etch rate as a function of chemical potential, both for a perfect {111} surface and for the same surface intersected by a mixed 60° dislocation.

## Approach
The simulation starts from a modified SOS representation that captures the diamond-cubic stacking sequence. The lattice is divided into three column types (A, B, C) with sheet termination rules that enforce correct nearest-neighbor bonding. Metropolis Monte Carlo sampling is used, with the Hamiltonian change ΔH = ΔEb − Δμ ΔN and the standard acceptance probability. Periodic in-plane boundary conditions are applied. For the dislocation case, an additional per‑atom energy field is superimposed: a core region (radius 5 Å, core energy 0.95 eV/Å) plus an elastic strain energy that decays as the inverse square of the distance from the core, parameterised according to published atomistic simulations. Equilibrium simulations are run over a range of dimensionless temperatures (k_BT/J) on a dislocation-free surface; the specific heat is computed from energy fluctuations. Etching simulations are carried out at a chosen, fixed temperature for a set of negative Δμ values. The normal etch rate (bond‑lengths per Monte Carlo sweep) is obtained from the time evolution of the average surface height. The full protocol is executed for the perfect surface and then repeated with the dislocation field active, using the same temperature and Δμ values.

## Reproduction target
Produce three CSV files in the /app/outputs directory:

1. `specific_heat_vs_temperature.csv` – columns: `temperature` (dimensionless, k_BT/J), `specific_heat` (dimensionless, C_V/k_B per atom). The curve should display a pseudoroughening peak at a low temperature and a rising trend associated with the roughening transition.

2. `etch_rate_dislocation_free.csv` – columns: `delta_mu` (in units of J), `etch_rate` (bond‑lengths per Monte Carlo sweep). The simulation temperature (k_BT/J) must be noted in metadata.

3. `etch_rate_with_dislocation.csv` – columns: `delta_mu` (in units of J), `etch_rate` (bond‑lengths per Monte Carlo sweep). Use the same temperature as in the dislocation-free case.

The etch rate must increase monotonically with |Δμ|, and the dislocation case should exhibit a higher etch rate than the perfect surface at every common Δμ.

## Assets

- Python scientific stack: numpy scipy
- Dislocation energy field parameterization: 10.1080/01418619008232980

## Workflow steps

### Step 1: SOS Model Implementation
- Role: process
- Action: Implement the modified solid-on-solid model for diamond-cubic Si {111} surfaces: partition into columns of types A, B, C with sheet termination rules (a, b, c), enforce nearest-neighbor bonding consistent with DC geometry, apply periodic in-plane boundary conditions, and implement Metropolis Monte Carlo updates using the Hamiltonian change ΔH = ΔEb − ΔμΔN and acceptance probability min{1, exp(−βΔH)}.
- Evidence: none

### Step 2: Dislocation Strain Energy Field
- Role: process
- Action: Compute the additive per-atom energy field for a perfect mixed 60° dislocation (core radius 5 Å, core energy 0.95 eV/Å, elastic strain energy ~1/r^2) mapped onto the SOS lattice sites.
- Evidence: `/app/outputs/dislocation_field.npy`

### Step 3: Equilibrium Specific Heat
- Role: scored (load-bearing)
- Action: Run equilibrium Metropolis Monte Carlo simulations on a dislocation-free surface of 2,700 sites at multiple temperatures spanning k_BT/J = 0.1–1.0 (each for at least 500,000 MCS after equilibration). Compute the surface specific heat C_V from energy fluctuations and write the results to specific_heat_vs_temperature.csv.
- Output file: `/app/outputs/specific_heat_vs_temperature.csv`
- Format: csv
- Contract: Columns: temperature (float, k_BT/J), specific_heat (float, C_V/k_B per atom).
- Scoring: scored by hidden verifier

### Step 4: Etching Rate on Perfect Surface
- Role: scored
- Action: Run etching simulations on an 11,907-site dislocation-free surface at a chosen temperature (e.g., k_BT/J = 0.03 or 0.05) for a range of negative chemical potential Δμ values. After equilibration, track the average surface height over time and compute the normal etch rate (bond-lengths per MCS). Output the results to etch_rate_dislocation_free.csv.
- Output file: `/app/outputs/etch_rate_dislocation_free.csv`
- Format: csv
- Contract: Columns: delta_mu (float, in units of J), etch_rate (float, bond-lengths per MCS). Include metadata for the constant temperature used.
- Scoring: scored by hidden verifier

### Step 5: Etching Rate with Dislocation
- Role: scored (load-bearing)
- Action: Run etching simulations on an 11,907-site surface incorporating the dislocation energy field from Step 2, using the same temperature and Δμ values as Step 4. Measure the normal etch rate and output etch_rate_with_dislocation.csv.
- Output file: `/app/outputs/etch_rate_with_dislocation.csv`
- Format: csv
- Contract: Columns: delta_mu (float, in units of J), etch_rate (float, bond-lengths per MCS). Temperature metadata matches the perfect-surface case.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/specific_heat_vs_temperature.csv`
- `/app/outputs/etch_rate_dislocation_free.csv`
- `/app/outputs/etch_rate_with_dislocation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### specific_heat_vs_temperature.csv
- path: `/app/outputs/specific_heat_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Surface specific heat curve; the checker will locate the pseudoroughening peak and verify the roughening transition signature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `specific_heat`
  - `units`:
    - `temperature`: dimensionless (k_BT/J)
    - `specific_heat`: dimensionless (C_V/k_B per atom)

### etch_rate_dislocation_free.csv
- path: `/app/outputs/etch_rate_dislocation_free.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Etch rates for a dislocation-free Si {111} surface; the checker verifies monotonic increase with |Δμ| and uses it for comparison with the dislocation case.
- schema:
  - `type`: table
  - `required_columns`: `delta_mu`, `etch_rate`
  - `units`:
    - `delta_mu`: dimensionless (J)
    - `etch_rate`: bond-lengths per MCS

### etch_rate_with_dislocation.csv
- path: `/app/outputs/etch_rate_with_dislocation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Etch rates for a Si {111} surface intersected by a dislocation; the checker confirms that rates are higher than the dislocation-free case at each Δμ.
- schema:
  - `type`: table
  - `required_columns`: `delta_mu`, `etch_rate`
  - `units`:
    - `delta_mu`: dimensionless (J)
    - `etch_rate`: bond-lengths per MCS

Notes: All outputs are Monte Carlo simulation results. The specific heat CSV must include the pseudoroughening peak at k_BT/J ≈ 0.35 and an elevated specific heat near 0.75. Etch rate CSVs must be monotonic, with the dislocation case showing higher rates than the perfect surface. No gold numeric values are exposed; the checker performs structural and comparative checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "specific_heat_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "specific_heat"
        ],
        "units": {
          "temperature": "dimensionless (k_BT/J)",
          "specific_heat": "dimensionless (C_V/k_B per atom)"
        }
      },
      "description": "Surface specific heat curve; the checker will locate the pseudoroughening peak and verify the roughening transition signature."
    },
    {
      "file": "etch_rate_dislocation_free.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_mu",
          "etch_rate"
        ],
        "units": {
          "delta_mu": "dimensionless (J)",
          "etch_rate": "bond-lengths per MCS"
        }
      },
      "description": "Etch rates for a dislocation-free Si {111} surface; the checker verifies monotonic increase with |Δμ| and uses it for comparison with the dislocation case."
    },
    {
      "file": "etch_rate_with_dislocation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_mu",
          "etch_rate"
        ],
        "units": {
          "delta_mu": "dimensionless (J)",
          "etch_rate": "bond-lengths per MCS"
        }
      },
      "description": "Etch rates for a Si {111} surface intersected by a dislocation; the checker confirms that rates are higher than the dislocation-free case at each Δμ."
    }
  ],
  "notes": "All outputs are Monte Carlo simulation results. The specific heat CSV must include the pseudoroughening peak at k_BT/J ≈ 0.35 and an elevated specific heat near 0.75. Etch rate CSVs must be monotonic, with the dislocation case showing higher rates than the perfect surface. No gold numeric values are exposed; the checker performs structural and comparative checks."
}
```

## How you are scored
A hidden verifier (not provided to you) will inspect each CSV file after submission. For the specific heat data, it will locate peaks and verify that the overall shape and feature locations are physically meaningful. For the etch rate files, it will confirm that the rates increase monotonically with |Δμ| and that the dislocation case yields higher rates than the perfect case under identical conditions. It may also compare numerical values against reference data within allowed tolerances. Each check contributes a partial weight, and the total reward (a number between 0 and 1) is returned to you. Simply reporting the paper’s numbers without running the simulations will not satisfy these structural and consistency checks.
