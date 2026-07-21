# Spin Model Phase Diagram Construction

## Problem background
Relaxor ferroelectrics such as Pb(In<sub>1/2</sub>Nb<sub>1/2</sub>)O<sub>3</sub> (PIN) exhibit nanoscale domain formation, slow dynamics, and dispersive dielectric responses driven by B-site disorder. A minimal model of coupled dipole moments with long-range dipole–dipole interaction and random local anisotropy is able to capture the competition between antiferroelectric (AFE) and ferroelectric (FE) phases. By performing large-scale Monte Carlo simulations of this model, one can compute the phase diagram (AFE transition temperatures as a function of disorder), the energy autocorrelation in the glassy phase, and the frequency-dependent dielectric constant. The task is to reproduce these three quantities through a reimplementation of the model and simulation protocol.

## Approach
We consider a rotator Hamiltonian on a 2D square lattice with a bipartite sublattice shift to ensure FE instability. The dipole–dipole interaction is summed via Ewald summation. The Monte Carlo update uses an O(N) method (Walker/Fukui–Todo) together with temperature-exchange (replica-exchange) Monte Carlo to overcome slow dynamics. For a range of disorder probabilities p we compute the four-fold staggered polarization and uniform polarization. By performing finite-size scaling with system sizes L=16 and L=32 we extract AFE transition temperatures from the Binder cumulant crossing; the threshold for FE domain formation is estimated from the rise of uniform polarization. In separate runs without replica exchange we record energy time series to compute the normalized energy autocorrelation function. Finally, we apply a small oscillating external electric field along the Monte Carlo timestep and measure the linear dielectric response at three distinct frequencies.

## Reproduction target
Implement the model Hamiltonian and Monte Carlo protocol. Run simulations for disorder values p = 0, 0.1, 0.2, 0.3, 0.4 with L=16 and 32, and for p=0.5 with L=32. Determine AFE transition temperatures from the Binder-parameter crossing of the staggered polarization and locate the FE domain formation threshold from the uniform polarization; write phase_diagram.csv. Run additional simulations for p=0.5 at T=0.2 (and for comparison at T=0.3 and zero anisotropy) without replica exchange, compute the normalized energy autocorrelation function, and write energy_autocorrelation.csv. Run simulations for p=0 and p=0.5 under a small oscillating electric field, compute the dielectric constant in the linear response regime at three Monte Carlo timestep frequencies, and write dielectric_function.csv. All output files must conform to the specified schemas.

## Assets
The workflow requires a standard Python scientific computing environment. The following public packages should be installed at runtime:
- Python (>=3.8)
- NumPy
- SciPy
- Matplotlib

No external datasets, pretrained models, or proprietary tools are needed; the model and simulation code are to be implemented from the specification given in this instruction.

## Workflow steps

### Step 1: Model implementation and simulation setup
- Role: process
- Action: Implement the rotator Hamiltonian on a 2D square lattice with bipartite sublattice shift, periodic boundary conditions, and the specified disorder distribution. Implement Ewald summation for dipole-dipole interaction, the O(N) Walker/Fukui-Todo update, and temperature-exchange Monte Carlo.
- Evidence: `/app/outputs/model_implementation.log`

### Step 2: Equilibrium Monte Carlo simulation for phase diagram
- Role: process
- Action: Run simulations for disorder values p = 0, 0.1, 0.2, 0.3, 0.4 with system sizes L=16 and L=32 over a suitable temperature range. Also simulate p=0.5 with L=32. Record time series of the four-fold staggered polarization and the uniform polarization.
- Evidence: `/app/outputs/phase_diagram_mc.log`

### Step 3: Phase boundary determination
- Role: scored (load-bearing)
- Action: From the simulation time series, compute the squared staggered polarization and its Binder parameter. Determine AFE transition temperatures for each p by the crossing of Binder curves for L=16 and 32. Estimate the FE domain formation threshold from the abrupt rise in uniform polarization. Write phase_diagram.csv.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: p (float), transition_type (string, one of 'AFE' or 'FE'), Tc (float).
- Scoring: scored by hidden verifier

### Step 4: Monte Carlo simulation for dynamics (no exchange)
- Role: process
- Action: Run separate simulations for p=0.5 at T=0.2 and T=0.3, and for the no-anisotropy case (|D_i|=0) at T=0.2, all with L=32 and without temperature exchange, recording energy time series.
- Evidence: `/app/outputs/dynamics_mc.log`

### Step 5: Energy autocorrelation analysis
- Role: scored
- Action: Compute the normalized energy autocorrelation function from the energy time series for the p=0.5, T=0.2 case. Write energy_autocorrelation.csv.
- Output file: `/app/outputs/energy_autocorrelation.csv`
- Format: csv
- Contract: Columns: t (int), phi (float).
- Scoring: scored by hidden verifier

### Step 6: Monte Carlo simulation under ac electric field
- Role: process
- Action: Run Monte Carlo for ordered (p=0) and disordered (p=0.5) cases with a small external electric field that oscillates periodically along the MC step (three distinct frequencies). Perform measurements over a range of temperatures, recording total polarization time series.
- Evidence: `/app/outputs/ac_field_mc.log`

### Step 7: Dielectric constant calculation
- Role: scored
- Action: From the polarization response, compute the dielectric constant in the linear regime for each frequency and temperature. Write dielectric_function.csv with rows for p=0 and p=0.5 at three frequencies.
- Output file: `/app/outputs/dielectric_function.csv`
- Format: csv
- Contract: Columns: p (float), T (float), omega (float), epsilon (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/energy_autocorrelation.csv`
- `/app/outputs/dielectric_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted AFE and FE transition temperatures as a function of disorder p. The checker compares these to hidden reference values obtained from the paper's phase diagram.
- schema:
  - `type`: table
  - `required_columns`: `p`, `transition_type`, `Tc`
  - `units`:
    - `Tc`: dimensionless temperature

### energy_autocorrelation.csv
- path: `/app/outputs/energy_autocorrelation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized energy autocorrelation function for the completely disordered case at low temperature. The checker verifies the qualitative slow decay pattern (e.g., phi remains above 0.1 at large t).
- schema:
  - `type`: table
  - `required_columns`: `t`, `phi`
  - `units`:
    - `t`: Monte Carlo step
    - `phi`: dimensionless

### dielectric_function.csv
- path: `/app/outputs/dielectric_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dielectric constant as a function of temperature for several MC step frequencies. The checker verifies that for p=0.5, epsilon decreases with increasing frequency at low temperature and the peak near the transition is broader than for p=0.
- schema:
  - `type`: table
  - `required_columns`: `p`, `T`, `omega`, `epsilon`
  - `units`:
    - `T`: dimensionless temperature
    - `omega`: Monte Carlo step frequency
    - `epsilon`: dimensionless dielectric constant

Notes: The phase diagram transition temperatures are compared against hidden gold values extracted from the paper's Fig. 1(c). The energy autocorrelation and dielectric function are scored via structural checks (trends and qualitative behavior) rather than exact numerical matches.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "transition_type",
          "Tc"
        ],
        "units": {
          "Tc": "dimensionless temperature"
        }
      },
      "description": "Extracted AFE and FE transition temperatures as a function of disorder p. The checker compares these to hidden reference values obtained from the paper's phase diagram."
    },
    {
      "file": "energy_autocorrelation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "phi"
        ],
        "units": {
          "t": "Monte Carlo step",
          "phi": "dimensionless"
        }
      },
      "description": "Normalized energy autocorrelation function for the completely disordered case at low temperature. The checker verifies the qualitative slow decay pattern (e.g., phi remains above 0.1 at large t)."
    },
    {
      "file": "dielectric_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "T",
          "omega",
          "epsilon"
        ],
        "units": {
          "T": "dimensionless temperature",
          "omega": "Monte Carlo step frequency",
          "epsilon": "dimensionless dielectric constant"
        }
      },
      "description": "Dielectric constant as a function of temperature for several MC step frequencies. The checker verifies that for p=0.5, epsilon decreases with increasing frequency at low temperature and the peak near the transition is broader than for p=0."
    }
  ],
  "notes": "The phase diagram transition temperatures are compared against hidden gold values extracted from the paper's Fig. 1(c). The energy autocorrelation and dielectric function are scored via structural checks (trends and qualitative behavior) rather than exact numerical matches."
}
```

## How you are scored
A hidden verifier independently scores each of the three output artifacts (phase_diagram.csv, energy_autocorrelation.csv, dielectric_function.csv) using reference values and structural checks that are not disclosed to you. The scores are combined by weight into a final reward between 0 and 1. Reporting numbers that match the paper is not sufficient; the verifier examines the submitted CSV files and compares them to hidden expected results. The final reward reflects how well your reproduced quantities agree with the expected behavior.
