# Green's Function Self-Consistent Calculation for 2D Easy-Plane Ferromagnet with Dipole-Dipole Interactions

## Problem background
The interplay of dipole-dipole interactions and single-ion easy-plane anisotropy in two-dimensional ferromagnets determines whether a long-range ordered magnetic state can survive at finite temperature. While isotropic short-range exchange alone destroys order in two dimensions, additional terms — dipolar interactions and magnetocrystalline anisotropy — can stabilise it. For an easy-plane system (anisotropy favouring a plane rather than a single axis), the mechanism that stabilises order is more subtle and must be computed. This task reproduces the self-consistent Green's-function calculation that quantifies the role of these interactions: it computes the spin-wave dispersion, the spontaneous magnetization, and the transition temperature as functions of the anisotropy constant and the dipolar coupling strength for a spin-1 ferromagnet on a two-dimensional square lattice.

## Approach
The calculation is built around a spin-1 Heisenberg model on a 2D square lattice with nearest-neighbour exchange J, a single-ion easy-plane anisotropy D (forcing the spins into the y-z plane), and a long-range dipole-dipole interaction of strength Ω. A Green's-function method is used, modified to handle the off-diagonal quantum mixing induced by the easy-plane term. Inter-site terms are decoupled in the random-phase approximation (RPA), while on-site correlations are treated with a Callen–Anderson decoupling. The resulting self-consistent equations involve several independent expectation values (like <S^z>, <(S^z)^2>, <(S^-)^2>, <(S^-)^2 S^z>) that are solved iteratively on a temperature grid. The dipolar lattice sums are evaluated efficiently with an Ewald summation technique that transforms the slowly convergent real-space lattice sums into rapidly convergent series of modified Bessel functions. From the converged solutions, one extracts the magnon dispersion relation E(k), the temperature-dependent magnetization M(T)=<S^z>, and the Curie temperature Tc where the magnetization vanishes.

## Reproduction target
Implement the self-consistent Green's-function scheme for a spin-1 ferromagnet on a 2D square lattice and produce three outputs:

- **Magnetization vs temperature** (file `magnetization.csv`): Curves of spontaneous magnetization M = <S^z> as a function of reduced temperature T/J for several fixed pairs of (D/J, Ω/J), specifically Ω/J = 0.005 with D/J = 0.1, 0.2, 0.5; the file must contain columns `T_div_J` and `M`.

- **Spin-wave dispersion** (file `spinwave_spectrum.csv`): Magnon energy E(k) along a high-symmetry path in the Brillouin zone at a low reduced temperature T/J = 0.1, for Ω/J = 0.005 and three values of the easy-plane anisotropy D/J = 0.1, 0.5, 1.0; the file must contain columns `k_path`, `k_x`, `k_y`, `E`.

- **Transition temperature** (file `transition_temperature.csv`): Curie temperature Tc/J extracted from the magnetization curves, given as a function of D/J at fixed Ω/J = 0.006, and as a function of Ω/J at fixed D/J = 0.2; the file must contain columns `parameter`, `value`, `Tc_div_J`.

All results are obtained by running the computation; no external dataset is required.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute dipole-dipole lattice sums
- Role: process
- Action: Compute the dipole-dipole interaction functions p_xx(k), p_yy(k), p_zz(k) on a user-chosen k-point mesh for a 2D square lattice using the Ewald summation method involving rapidly convergent series of modified Bessel functions. Store the computed arrays.
- Evidence: `/app/outputs/dipole_sums.npy`

### Step 2: Solve self-consistent Green's-function equations
- Role: process
- Action: Implement the self-consistent scheme for a spin-1 Heisenberg ferromagnet on a 2D square lattice with nearest-neighbour exchange J, easy-plane anisotropy D, and dipole-dipole interaction Ω. Use RPA decoupling for inter-site terms and Callen-Anderson on-site decoupling. Solve the closed equations for the independent expectation values <S^z>, <(S^z)^2>, <(S^-)^2>, <(S^-)^2 S^z> at each temperature for a grid of temperatures T/J covering the required parameter sets (D/J, Ω/J). Store converged quantities.
- Evidence: `/app/outputs/sc_results.npz`

### Step 3: Output magnetization vs temperature
- Role: scored (load-bearing)
- Action: From the stored self-consistent solutions, extract the spontaneous magnetization M=<S^z> as a function of reduced temperature T/J for the specified combinations of D/J and Ω/J (e.g., Ω/J=0.005, D/J=0.1,0.2,0.5). Write the curves to magnetization.csv.
- Output file: `/app/outputs/magnetization.csv`
- Format: csv
- Contract: T_div_J:float, D_div_J:float, Omega_div_J:float, M:float
- Scoring: scored by hidden verifier

### Step 4: Compute spin-wave dispersion
- Role: scored
- Action: Using the converged expectation values at reduced temperature T/J=0.1 and the expressions for F1(k) and F2(k), compute the magnon energy E(k) = sqrt(F1^2 - F2^2) along a high-symmetry path in the Brillouin zone for Ω/J=0.005 and D/J=0.1,0.5,1.0. Write the dispersion to spinwave_spectrum.csv.
- Output file: `/app/outputs/spinwave_spectrum.csv`
- Format: csv
- Contract: k_path:string, k_x:float, k_y:float, D_div_J:float, E:float
- Scoring: scored by hidden verifier

### Step 5: Determine transition temperatures
- Role: scored
- Action: From the magnetization curves, extract the Curie temperature Tc (where M→0) by interpolation/extrapolation. Compile Tc/J as a function of D/J for fixed Ω/J=0.006 and as a function of Ω/J for fixed D/J=0.2. Write results to transition_temperature.csv.
- Output file: `/app/outputs/transition_temperature.csv`
- Format: csv
- Contract: parameter:string, value:float, Tc_div_J:float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization.csv`
- `/app/outputs/spinwave_spectrum.csv`
- `/app/outputs/transition_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization.csv
- path: `/app/outputs/magnetization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spontaneous magnetization M as function of reduced temperature T/J for selected (D,J,Ω) parameter sets.
- schema:
  - `type`: table
  - `required_columns`: `T_div_J`, `D_div_J`, `Omega_div_J`, `M`

### spinwave_spectrum.csv
- path: `/app/outputs/spinwave_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnon energy E along a high-symmetry k-path at T/J=0.1 for Ω/J=0.005 and several D/J values.
- schema:
  - `type`: table
  - `required_columns`: `k_path`, `k_x`, `k_y`, `D_div_J`, `E`

### transition_temperature.csv
- path: `/app/outputs/transition_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Curie temperature Tc/J as function of D/J (Ω/J fixed) or Ω/J (D/J fixed).
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`, `Tc_div_J`

Notes: All scored outputs are CSV tables. The checker compares the agent's values against hidden reference data digitized from the paper's figures using tolerances appropriate for numerical reproduction (mean absolute error < 0.1 for magnetization, absolute tolerance 0.05*J for spin-wave energies, relative error ≤10% for Tc).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_div_J",
          "D_div_J",
          "Omega_div_J",
          "M"
        ]
      },
      "description": "Spontaneous magnetization M as function of reduced temperature T/J for selected (D,J,Ω) parameter sets."
    },
    {
      "file": "spinwave_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_path",
          "k_x",
          "k_y",
          "D_div_J",
          "E"
        ]
      },
      "description": "Magnon energy E along a high-symmetry k-path at T/J=0.1 for Ω/J=0.005 and several D/J values."
    },
    {
      "file": "transition_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value",
          "Tc_div_J"
        ]
      },
      "description": "Curie temperature Tc/J as function of D/J (Ω/J fixed) or Ω/J (D/J fixed)."
    }
  ],
  "notes": "All scored outputs are CSV tables. The checker compares the agent's values against hidden reference data digitized from the paper's figures using tolerances appropriate for numerical reproduction (mean absolute error < 0.1 for magnetization, absolute tolerance 0.05*J for spin-wave energies, relative error ≤10% for Tc)."
}
```

## How you are scored
A hidden verifier checks each of the three scored artifacts independently. It compares your computed values to a set of reference values (digitized from the relevant published figures) using tolerances appropriate for the numerical nature of the method. The verifier only reads the CSV files you write; it neither re-runs your solver nor fetches any data from the network. The overall reward is a weighted sum of the scores for the magnetization, spin-wave spectrum, and transition temperature stages. To earn full credit you must implement the complete self-consistent pipeline — simply reporting numbers that match a target is insufficient because the checker will examine the entire data set, not just a single summary statistic.
