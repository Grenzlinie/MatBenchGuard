# Dopant-vacancy transport coefficient computation via master equation

## Problem background
Dopant atoms in silicon diffuse via vacancies, but the macroscopic transport coefficients describing the coupled dopant–vacancy fluxes have been controversial. Pair-diffusion theory predicts α = T_d^0/D_d^0 = +1, while non-Fickian models predict −1. Resolving this controversy requires computing the four low-concentration transport coefficients directly from a microscopic interaction potential between dopants and vacancies. This task reproduces the atomistic master-equation simulation that accomplishes this computation.

## Approach
The simulation models a dopant atom and a single vacancy on a diamond cubic silicon lattice. The interaction between them is described by an attractive rectangular-well potential of depth 0.5 eV that extends to a given coordination order (range). The probability c(i,j,t) for the dopant to be at site i and the vacancy at site j evolves according to a master equation with vacancy jump rates modified by the interaction potential. A steady state with a constant vacancy gradient is imposed by altering jump frequencies across periodic boundaries using chemical-potential discontinuities. Crystal translational symmetry is exploited to reduce the problem dimensionality, and the master equation is integrated numerically until a steady state. From the steady-state probability, finite-size normalized transport coefficients D_d^n, T_d^n, and T_v^n are extracted. These are then corrected to the low-concentration limits D_d^0 and T_d^0 using exact finite-size correction formulas and the known pure-silicon vacancy diffusion coefficient. The computation is carried out for coordination orders 1 through 5 at 1000 °C (1273 K).

## Reproduction target
Compute the low-concentration normalized transport coefficients D_d^0 and T_d^0 (in units of f₀ a²) and the ratio α = T_d^0/D_d^0 for an attractive rectangular-well interaction of depth 0.5 eV at T = 1000 °C (1273 K) for coordination order ranges 1, 2, 3, 4, and 5. Write the results to a CSV file with columns: coordination_order (integer), D_d0 (float), T_d0 (float), alpha (float).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define silicon lattice and interaction potential
- Role: process
- Action: Construct the diamond cubic lattice of silicon with lattice constant a = 5.43 Å. Define the attractive rectangular-well dopant–vacancy interaction potential V_vd(i,j) with depth 0.5 eV: within the given coordination order range (1 to 5, each range treated separately), V_vd(i,j) = -0.5 eV; outside that range V_vd(i,j) = 0. Identify all lattice sites belonging to each coordination order around a dopant site.
- Evidence: none

### Step 2: Compute vacancy jump frequencies
- Role: process
- Action: For each coordination range and temperature T = 1273 K, compute the vacancy jump frequencies f_{jj'}^i using the attractive-case formula f_{jj'}^i = f0 * exp( -(V_vd(i,j') + V_vd(i,j)) / (2 k T) ), where f0 is the vacancy jump frequency in pure silicon (set f0 = 1 in units of f0).
- Evidence: none

### Step 3: Solve master equation for two-particle probability
- Role: process
- Action: Implement the master equation for the two-particle probability c(i,j,t) on a finite supercell of silicon with periodic boundary conditions. Impose a steady-state gradient by modifying jump frequencies across the z-boundaries: For a vacancy jump from the lower z-surface (1) to the upper (2) (due to periodic boundaries), multiply the natural jump frequency by exp((μ_v^2 - μ_v^1)/kT), where μ_v = kT ln(C_v/C_Si) and C_v^1, C_v^2 are the desired vacancy concentrations at the surfaces. Jumps from upper to lower are not multiplied. If the jump involves exchange with the dopant, also multiply by exp((μ_d^1 - μ_d^2)/kT), with μ_d = kT ln(C_d/C_Si). Use small differences (e.g., δ = 0.01) to create the gradients. Exploit crystal translational symmetry to reduce the storage dimensions, separate the homogeneous equilibrium part of c, and integrate the inhomogeneous part with explicit time stepping until a steady state is reached. Run for selected simulation cell sizes (e.g., N_Si = 1000 or larger as feasible) for each coordination range.
- Evidence: none

### Step 4: Extract finite-size normalized transport coefficients
- Role: process
- Action: From the steady-state probability c_stat(i,j) of each simulation (two independent gradient configurations), compute the dopant flux density J_d (in units of f0 a) and vacancy flux density J_v using:

J_d = (1/(N_cell * ν)) Σ_i Σ_{j∈nn(i)} c_stat(i,j) f_{j,i}^i (r_j - r_i)·ẑ

J_v = (1/(N_cell * ν)) Σ_{i,j} Σ_{j'∈nn(j)} c_stat(i,j) f_{jj'}^i (r_{j'} - r_j)·ẑ

where ν = a³/8 is the volume per silicon site, N_cell is the total number of lattice sites in the supercell, nn(i) denotes the four nearest neighbours of i, and ẑ is the unit vector along the z-axis. Then, from the known imposed concentration gradients ∇C_d and ∇C_v (computed from the boundary concentrations and cell length L_z), solve the linear equations

- J_d = D_d^n (C_v/C_Si) ∇C_d + T_d^n (C_d/C_Si) ∇C_v
- J_v = T_v^n (C_v/C_Si) ∇C_d + D_v ∇C_v

to obtain the finite-size normalized transport coefficients D_d^n, T_d^n, T_v^n, and D_v. Use two independent gradient configurations (one with pure dopant gradient, one with pure vacancy gradient) to uniquely determine the four coefficients.
- Evidence: none

### Step 5: Apply finite-size corrections to obtain low-concentration limits
- Role: process
- Action: Apply the exact finite-size corrections using the following equations (derived in the paper). Define Z = z_vd - N_b - 1, where N_b is the number of silicon sites within the interaction range of the dopant, and z_vd = Σ_{j=1}^{N_b} exp(-V_vd(i,j)/(kT)) (with V_vd in eV, k = 8.6173e-5 eV/K, T = 1273 K). Then, given the finite-size coefficients D_d^n, T_d^n, T_v^n, D_v and the known D_v^0 = 0.125 f0 a^2, solve the following system for the unknowns D_d^0, T_d^0, T_v^0, and T_4:

D_d^n = (N_Si/(N_Si+Z)) · (1 − Z²/(N_Si+Z)²)⁻¹ · (D_d^0 − T_d^0 · Z/(N_Si+Z))

T_d^n = (N_Si/(N_Si+Z)) · (1 − Z²/(N_Si+Z)²)⁻¹ · (T_d^0 − D_d^0 · Z/(N_Si+Z))

T_v^n = (N_Si/(N_Si+Z)) · (1 − Z²/(N_Si+Z)²)⁻¹ · (T_v^0 − T_4 · Z/(N_Si+Z))

D_v = D_v^0 + (N_Si/(N_Si+Z)) · (1 − Z²/(N_Si+Z)²)⁻¹ · (T_4/N_Si − T_v^0 · Z/(N_Si(N_Si+Z)))

where N_Si is the number of silicon sites in the simulation cell. Solve the system for each coordination range. Then compute α = T_d^0 / D_d^0.
- Evidence: none

### Step 6: Output transport coefficients table
- Role: scored (load-bearing)
- Action: Gather the computed D_d^0, T_d^0, and α for each coordination order range (1 through 5) and write them to transport_coefficients.csv.
- Output file: `/app/outputs/transport_coefficients.csv`
- Format: csv
- Contract: coordination_order (int), D_d0 (float), T_d0 (float), alpha (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_coefficients.csv
- path: `/app/outputs/transport_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of low-concentration normalized transport coefficients for attractive rectangular-well interaction potential (depth 0.5 eV, T=1273 K) at coordination orders 1 through 5. D_d0 and T_d0 are in units of f0*a^2.
- schema:
  - `type`: table
  - `required_columns`: `coordination_order`, `D_d0`, `T_d0`, `alpha`

Notes: The checker compares each row of the agent's CSV against hidden reference values from the paper's Table I, applying tolerances that account for numerical differences in the computational implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coordination_order",
          "D_d0",
          "T_d0",
          "alpha"
        ]
      },
      "description": "CSV table of low-concentration normalized transport coefficients for attractive rectangular-well interaction potential (depth 0.5 eV, T=1273 K) at coordination orders 1 through 5. D_d0 and T_d0 are in units of f0*a^2."
    }
  ],
  "notes": "The checker compares each row of the agent's CSV against hidden reference values from the paper's Table I, applying tolerances that account for numerical differences in the computational implementation."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/transport_coefficients.csv` and checks that the file contains exactly five rows (one per coordination order) with the required columns. It then compares your computed D_d0, T_d0, and α against reference values using tolerances suitable for numerical implementations. The final reward is the fraction of rows that pass the comparison (i.e., have values within tolerance for all three coefficients). You must implement the full pipeline; providing numbers without running the simulation will not yield correct results.
