# Substrate distortion induced by adsorption: Brownian dynamics simulation and order parameter computation

## Problem background
When molecules adsorb onto a solid surface, strong lateral interactions among the adsorbates can compete with the substrate’s own cohesive forces and potentially distort the surface atomic positions. This task investigates whether such adsorbate-adsorbate interactions can induce a structural rearrangement of the underlying substrate. The goal is to compute an order parameter that quantifies the degree of substrate distortion as a function of the strength of adsorbate-adsorbate coupling.

## Approach
The system is modelled as two interacting particle subsystems: substrate atoms that are confined by an external periodic potential near the sites of a square lattice, and adsorbate atoms that interact with the substrate but not directly with the external periodic potential. The dynamics is described by Brownian equations of motion with Gaussian white noise as a thermal bath. The pair interaction is a repulsive Gaussian within each species and attractive between species. Parameters are fixed to ensure that the bare substrate structure (at negligible adsorbate coupling) is a square lattice. As the adsorbate-adsorbate interaction strength is increased from zero, the adsorbate subsystem drives the substrate away from its original configuration towards a distorted structure. For each interaction strength the two-body correlation function of the substrate is computed, its Fourier transform is analysed, and the height of a characteristic diffraction peak (corresponding to the bare substrate order) is tracked. The normalised reduction of this peak height defines the order parameter.

## Model equations

The equations of motion for the atomic positions \(\mathbf{R}_{ji}\) (subsystem index \(j=1,2\); particle index \(i=1,\dots,N\)) are

\[
\ddot{\mathbf{R}}_{ji} + \eta \dot{\mathbf{R}}_{ji} + \frac{\partial}{\partial \mathbf{R}_{ji}} V_0(\mathbf{R}_{ji}) \delta_{j1}
+ \frac{\partial}{\partial \mathbf{R}_{ji}} \sum_{k,l} V(|\mathbf{R}_{ji} - \mathbf{R}_{kl}|) = \delta F(\mathbf{R}_{ji}; t),
\]

with damping coefficient \(\eta = 1\) and temperature \(T = 1\).  The random force \(\delta F(\mathbf{R}_{ji}; t)\) is a Gaussian white noise whose correlation is

\[
\langle \delta F(\mathbf{R}_{ji}; t) \, \delta F(\mathbf{R}_{j'i'}; t') \rangle
= 2 \eta T \, \delta_{jj'} \, \delta(\mathbf{R}_{ji} - \mathbf{R}_{j'i'}) \, \delta(t - t').
\]

Only the substrate (\(j=1\)) feels the external periodic potential that models a square lattice of spacing \(d=1\):

\[
V_0(\mathbf{R}) = V_0 \left[ \cos\!\left(\frac{2\pi x}{d}\right) + \cos\!\left(\frac{2\pi y}{d}\right) \right],
\qquad V_0 = 1.
\]

The pairwise interaction is a Gaussian:

\[
V(|\mathbf{R}_{ji} - \mathbf{R}_{kl}|) = V_{jj'} \, \exp\!\left( -\frac{|\mathbf{R}_{ji} - \mathbf{R}_{kl}|^2}{a_{jj'}} \right),
\]

with the following parameter values (all energies are given in units of \(V_0\)):

\[
\begin{aligned}
V_{11} &= +1.0 \quad (\text{substrate–substrate repulsive}), \\
V_{12} &= -1.0 \quad (\text{substrate–adsorbate attractive}), \\
V_{22} &= +3.0 \quad (\text{adsorbate–adsorbate repulsive}), \\
a_{11} &= a_{22} = 0.875, \qquad a_{12} = 0.5.
\end{aligned}
\]

The adsorbate–adsorbate strength \(V_{22}\) will be varied from 0 to \(V_{22}^{\max} = 50\) (still in units of \(V_0\)).  The relative strength is defined as \(V_{22} / V_{22}^{\max}\).

## Reproduction target
Execute the Brownian dynamics simulation for the two-subsystem model with \(N \approx 1000\) particles each, periodic boundary conditions, temperature \(T=1\), damping coefficient \(\eta=1\), and the Gaussian interaction parameters listed above. For a range of \(V_{22}\) values from 0 up to \(V_{22}^{\max}=50\), run to steady state and compute the order parameter as

\[
1 - \frac{G_{11}(\mathbf{q}_b; V_{22})}{G_{11}(\mathbf{q}_b; V_{22}=0)},
\]

where \(G_{11}(\mathbf{q}; V_{22})\) is the two-dimensional Fourier transform of the substrate correlation function at wave vector \(\mathbf{q}_b\) corresponding to a characteristic peak of the square lattice (for instance, \(\mathbf{q}_b = (\pi,\pi)\) in units of \(2\pi/d\) with \(d=1\); the exact peak can be identified from the \(V_{22}=0\) reference simulation).

Produce a CSV file with the **required** columns `V22_relative_strength` and `order_parameter_sim`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Run Brownian dynamics simulation
- Role: process
- Action: Implement the two-subsystem Brownian dynamics model described above. Use \(N_1=N_2\) up to \(10^3\), periodic boundaries, and the parameter values given in the Model equations section. Run simulations for a range of \(V_{22}\) values from 0 to \(V_{22}^{\max}=50\) in steps, recording the steady-state particle trajectories for the substrate subsystem after equilibration. (This step has no explicit output file; its results feed into Step 2.)

### Step 2: Compute order parameter and compile results table
- Role: scored (load-bearing)
- Action: From the simulated substrate trajectories, compute the two-body correlation function \(G_{11}(\mathbf{q})\) via Fourier transform. Locate the diffraction peak corresponding to the substrate-induced structure from the \(V_{22}=0\) reference simulation. For each \(V_{22}\) value, calculate the order parameter as \(1 - G_{11}(\mathbf{q}_b; V_{22}) / G_{11}(\mathbf{q}_b; V_{22}=0)\). Write a CSV file.
- Output file: `/app/outputs/order_parameter.csv`
- Format: csv
- Contract: Required columns: `V22_relative_strength` (float, unitless ratio \(V_{22}/V_{22}^{\max}\)), `order_parameter_sim` (float, unitless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameter.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameter.csv
- path: `/app/outputs/order_parameter.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV table of order parameter for varying relative interaction strength. The checker extracts the simulated order parameter curve to locate the inflection point and compares to the paper's threshold within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `V22_relative_strength`, `order_parameter_sim`
  - `units`:
    - `V22_relative_strength`: unitless
    - `order_parameter_sim`: unitless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V22_relative_strength",
          "order_parameter_sim"
        ],
        "units": {
          "V22_relative_strength": "unitless",
          "order_parameter_sim": "unitless"
        }
      },
      "description": "CSV table of order parameter for varying relative interaction strength. The checker extracts the simulated order parameter curve to locate inflection point and compares to the paper's threshold within tolerance."
    }
  ],
  "notes": "Only the simulated order parameter defines the scored inflection point."
}
```

## How you are scored
A hidden verifier will read your `order_parameter.csv` and independently evaluate your simulated order parameter curve. The verifier will compute the approximate location of the distortive threshold (e.g., the inflection point of the simulated curve) and compare it against a hidden reference. It will also compute an overall deviation (such as the L2 norm of the difference) between your simulated order parameter values and a reference set of values at the same \(V_{22}\) ratios. Your final reward is a weighted combination of these checks, with the simulated curve carrying the majority of the weight.