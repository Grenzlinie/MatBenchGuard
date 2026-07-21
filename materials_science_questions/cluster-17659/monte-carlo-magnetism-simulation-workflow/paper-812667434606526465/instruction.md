# Monte Carlo phase diagram and domain growth of a 2D classical spin model

## Problem background
Nuclear spin systems can be cooled to ultra-low temperatures via adiabatic demagnetization, where the spin system evolves in isolation from the lattice heat bath at constant entropy. Understanding the resulting magnetic ordering requires knowledge of the phase diagram in both temperature–magnetic field and entropy–magnetic field coordinates, as well as the nonequilibrium domain growth that follows a quench into the ordered phase. This task investigates a two-dimensional classical spin model that serves as a simplified nuclear antiferromagnet. The Hamiltonian includes nearest-neighbor exchange and dipolar interactions, plus a fourth-order single-ion anisotropy that stabilizes four degenerate antiferromagnetic domains. The model is expected to exhibit a phase boundary with both first-order and second-order segments separated by a tricritical point, and its ordering kinetics after a sudden quench should follow a characteristic power law. The goal is to reproduce the equilibrium phase diagram, compute constant-entropy paths (isentropes) crossing the phase boundary, and measure the domain growth exponent from quench simulations.

## Approach
The approach is to perform Monte Carlo simulations of the classical-spin Hamiltonian using sequential Glauber dynamics. Equilibrium thermodynamic observables — magnetic enthalpy, staggered magnetization, induced magnetization, specific heat, and uniform susceptibility — are computed over a grid of temperatures and magnetic fields that spans the phase transition region. From these data, the phase boundary is identified by detecting discontinuities in the staggered magnetization and slope changes of the enthalpy with respect to field; the zero-field Néel temperature and the tricritical temperature that separates first-order from second-order behavior are extracted. Entropy is obtained by numerical integration of the induced magnetization from a high-field reference, where the free-energy integration constant is supplied by a mean-field calculation. Isentropes for two specified target entropy values are then constructed by interpolation in the temperature–field plane. Separately, nonequilibrium quench simulations are performed: the system is prepared at high temperature or high field, then instantaneously changed to a point inside the ordered phase; the excess energy decay is ensemble-averaged and the inverse excess energy is fitted to a power law at late times to extract the domain growth exponent.

## Reproduction target
Your task is to produce three scored artifacts:
1. **phase_diagram.csv** – a CSV file with columns T, H, M_perp, M_z, boundary_flag, transition_order, containing the equilibrium phase boundary points and the extracted values of the zero-field Néel temperature T_N(0) and the tricritical temperature T^* (encoded in the file header or as separate rows).
2. **isentropes.csv** – a CSV file with columns S, T, H listing points along the two constant-entropy paths S = –3.0 k_B and S = –1.4 k_B, from high field down to H = 0.
3. **growth_exponent.txt** – a text file containing the measured domain growth exponent n (floating-point number) for the primary quench to (T = 0.7 J/k_B, H = 0).

## Assets

- Python scientific stack: numpy scipy matplotlib numba

## Workflow steps

### Step 1: Monte Carlo equilibrium simulation
- Role: process
- Action: Implement Glauber-dynamics Monte Carlo simulations on a 64×64 square lattice with Hamiltonian parameters J=1, P=2J, S=1, k_B=1. For a grid of temperatures and magnetic fields covering the phase transition region, collect per-spin observables: magnetic enthalpy E, staggered magnetization M_perp, induced magnetization M_z, specific heat C_H, and uniform susceptibility χ_0^{zz}. Use up to 3000 MCS for equilibration and production. Store raw observable arrays for subsequent analysis.
- Evidence: `/app/outputs/mc_observables.npz`

### Step 2: Phase diagram analysis
- Role: scored (load-bearing)
- Action: From the Monte Carlo observables, identify the phase boundary points by detecting jumps in M_perp and slope changes in dE/dH. Determine the zero-field Néel temperature T_N(0) and the tricritical temperature T^*. Output a CSV file containing the phase boundary data: columns T (dimensionless J/k_B), H (dimensionless J), M_perp (dimensionless), M_z (dimensionless), boundary_flag (0 or 1), transition_order (1 for first-order, 2 for second-order). The derived T_N(0) and T^* must be encoded in the header or as separate rows.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Columns: T (float, dimensionless J/k_B), H (float, dimensionless J), M_perp (float), M_z (float), boundary_flag (int, 0 or 1), transition_order (int, 1 or 2). The header should include the scalar values T_N(0) and T^* as comments.
- Scoring: scored by hidden verifier

### Step 3: Isentrope computation
- Role: scored
- Action: First compute the mean-field free energy F(T, H0=30J) using mean-field theory for the given Hamiltonian. Then, using the Monte Carlo data for M_z(T,H), numerically integrate from H0=30J to each (T,H) point to obtain F(T,H), then compute entropy S(T,H) = (E – F)/T. Interpolate to construct the two constant-entropy paths: S = –3.0 k_B and S = –1.4 k_B, from high field down to H=0. Output a CSV file with columns S (k_B), T (J/k_B), H (J) for points along these two isentropes.
- Output file: `/app/outputs/isentropes.csv`
- Format: csv
- Contract: Columns: S (float, dimensionless k_B), T (float, dimensionless J/k_B), H (float, dimensionless J). At least 5 points per isentrope.
- Scoring: scored by hidden verifier

### Step 4: Domain growth exponent measurement
- Role: scored
- Action: Perform quench simulations: (i) from equilibrium at T_i=1.5 J/k_B, H=0 quench to (T=0.7 J/k_B, H=0); (ii) from equilibrium at T_i=0.4 J/k_B, H_i=11 J quench to (T=0.4 J/k_B, H=4 J). For each quench, run Glauber dynamics and record ΔE(t) = E(t) – E_eq. Ensemble average over at least 10 independent runs. Compute ΔE^{-1}(t) and fit a power law at late times (t > 100 MCS) to extract exponent n. Output a text file with the single value n (floating point) for the primary quench to (0.7,0).
- Output file: `/app/outputs/growth_exponent.txt`
- Format: txt
- Contract: A single line containing a floating-point number n (e.g., '0.5023').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/isentropes.csv`
- `/app/outputs/growth_exponent.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing phase boundary points and extracted T_N(0) and T* (in header). Scored via tolerance comparison against paper values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `H`, `M_perp`, `M_z`, `boundary_flag`, `transition_order`
  - `units`:
    - `T`: dimensionless J/k_B
    - `H`: dimensionless J
    - `M_perp`: dimensionless
    - `M_z`: dimensionless
    - `boundary_flag`: 
    - `transition_order`: 

### isentropes.csv
- path: `/app/outputs/isentropes.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing points along the isentropes S=-3.0 k_B and S=-1.4 k_B. Scored via tolerance comparison with reference.
- schema:
  - `type`: table
  - `required_columns`: `S`, `T`, `H`
  - `units`:
    - `S`: k_B
    - `T`: J/k_B
    - `H`: J

### growth_exponent.txt
- path: `/app/outputs/growth_exponent.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Text file with the growth exponent n for the quench to (T=0.7, H=0). Scored via tolerance comparison with paper value.
- schema:
  - `type`: text

Notes: The equilibrium MC simulation (process step) must be executed before the phase diagram and isentrope steps. The growth exponent can be computed independently after the initial MC equilibration. All scored artifacts are compared against paper-reported values with appropriate tolerances.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "H",
          "M_perp",
          "M_z",
          "boundary_flag",
          "transition_order"
        ],
        "units": {
          "T": "dimensionless J/k_B",
          "H": "dimensionless J",
          "M_perp": "dimensionless",
          "M_z": "dimensionless",
          "boundary_flag": "",
          "transition_order": ""
        }
      },
      "description": "CSV containing phase boundary points and extracted T_N(0) and T* (in header). Scored via tolerance comparison against paper values."
    },
    {
      "file": "isentropes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "S",
          "T",
          "H"
        ],
        "units": {
          "S": "k_B",
          "T": "J/k_B",
          "H": "J"
        }
      },
      "description": "CSV containing points along the isentropes S=-3.0 k_B and S=-1.4 k_B. Scored via tolerance comparison with reference."
    },
    {
      "file": "growth_exponent.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text"
      },
      "description": "Text file with the growth exponent n for the quench to (T=0.7, H=0). Scored via tolerance comparison with paper value."
    }
  ],
  "notes": "The equilibrium MC simulation (process step) must be executed before the phase diagram and isentrope steps. The growth exponent can be computed independently after the initial MC equilibration. All scored artifacts are compared against paper-reported values with appropriate tolerances."
}
```

## How you are scored
A hidden automated verifier will score your submission by reading each output file and extracting key quantities. For `phase_diagram.csv`, the verifier extracts T_N(0) and T^*, as well as the character of the transition along the boundary. For `isentropes.csv`, the verifier examines the temperature at H=0 and at the transition crossing points for each isentrope. For `growth_exponent.txt`, the verifier reads the reported exponent n. These extracted values are compared against expected physical values (derived from the original paper, but not disclosed to you). The individual scores are weighted and combined to produce a final reward between 0 and 1. Merely reporting numbers without performing the simulations will not yield results consistent with the hidden checks, so the best path to a high score is to faithfully execute the described workflow.
