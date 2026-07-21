# Kinetic Monte Carlo Crystal Growth Morphology Simulation

## Problem background
During deep crustal metamorphism, garnet crystals often develop dendritic or anhedral cores that transition to compact, faceted rims. This morphological progression is believed to record initial growth under high supersaturation (disequilibrium) followed by near-equilibrium conditions. Monte Carlo (MC) simulations of crystal growth can reproduce these textures and quantify the thermodynamic overstepping required. This task involves implementing a kinetic Monte Carlo (kMC) model of crystal growth on a trigonal lattice, mapping the morphological transition from branched to faceted forms as a function of dimensionless supersaturation Δμ/kT, and estimating the transition threshold.

## Approach
The method follows a kinetic Monte Carlo model for crystal growth from solution on a two-dimensional trigonal lattice. The model includes: diffusion of growth units through a fluid, surface attachment kinetics, and surface diffusion along crystal faces. A single effective growth species is used.

### Model components

**Lattice and coordination:**
The simulation takes place on a 2D trigonal lattice where each site has up to 6 nearest neighbours and up to 6 next-nearest neighbours. The crystal grows by occupying lattice sites.

**Source and diffusion:**
Growth units are released from a circular source region located some distance from an initial crystal seed. They diffuse through the fluid via a random walk on the lattice, moving to adjacent empty sites. When a growth unit reaches a site that is adjacent to at least one occupied crystal site, it may become attached.

**Attachment probability:**
When a growth unit is adjacent to the crystal, it attaches with a probability determined by the local interaction energy \(E_i\) and the dimensionless supersaturation \(Δμ/kT\):

\[
P_{\text{attach}} = A \cdot \exp\left( \frac{Δμ - E_i}{k_B T} \right)
\]

where \(A\) is a normalisation constant chosen such that \(P_{\text{attach}} \le 1\) for the range of parameters used. A standard choice is \(P_{\text{attach}} = \min(1, \exp((Δμ - E_i)/k_B T))\). If a particle reaches a site adjacent to the crystal but does not attach, it continues its random walk.

The local interaction energy \(E_i\) is computed from the numbers of occupied nearest neighbours \(n_i\) (max 6) and next-nearest neighbours \(m_i\) (max 6) at the attachment site:

\[
E_i = Φ_1 n_i + Φ_2 m_i
\]

**Surface diffusion:**
Particles already incorporated into the crystal surface may diffuse along the surface to reduce the total energy. A surface particle at a site can attempt to hop to an adjacent empty site that is also adjacent to the crystal. The hop is accepted with probability:

\[
P_{\text{hop}} = \begin{cases}
1 & \text{if } E_{\text{final}} \le E_{\text{initial}} \\
\exp\left( -\frac{E_{\text{final}} - E_{\text{initial}}}{k_B T} \right) & \text{if } E_{\text{final}} > E_{\text{initial}}
\end{cases}
\]

where \(E_{\text{initial}}\) and \(E_{\text{final}}\) are the interaction energies of the particle at its current and prospective sites. Surface diffusion helps smooth the crystal faces and, at low supersaturation, promotes the formation of compact, euhedral shapes.

**Dimensionless parameters:**
The simulation is governed by two dimensionless parameters:
- Normalised bond strength: \(Φ_1/k_B T = 7\) (fixed)
- Ratio of next-nearest to nearest bond strength: \(Φ_2/Φ_1 = 0.1\) (fixed)

The dimensionless supersaturation \(Δμ/kT\) is varied across simulations to control the driving force for crystallisation. High \(Δμ/kT\) (≈ 1–10) corresponds to strong disequilibrium and produces branched, dendritic morphologies; low \(Δμ/kT\) (≈ 0.01–1) favours compact, faceted crystals.

**Simulation termination:**
Each simulation runs until a predefined number of growth units have been incorporated into the crystal (e.g., 200–500 particles) or until the source is depleted. The maximum lattice size should be chosen large enough to accommodate the grown crystal without boundary effects.

**Morphological metrics:**
After growth completes, two metrics are computed from the final crystal occupancy grid:
- **Branch count**: The number of distinct branches extending from the central core. Branches are identified as connected components of the crystal after removing the compact central region.
- **Compactness (circularity)**: \(C = \frac{4\pi \cdot A}{P^2}\), where \(A\) is the crystal area (number of occupied sites) and \(P\) is the perimeter length (number of edges between occupied and empty sites, measured on the lattice). A perfect circle would have \(C = 1\); lower values indicate more irregular shapes.

## Reproduction target
Implement the kMC model on a 2D trigonal lattice with the parameters specified above. Run a set of at least 8 constant-\(Δμ/kT\) simulations spanning a range from approximately 0.01 to 10. Record the computed branch count and compactness for each. Also run one time‑varying simulation in which \(Δμ/kT\) decreases during growth: start with \(\log_{10}(Δμ/kT) = 0.7\) and end at \(\log_{10}(Δμ/kT) = -2\), decreasing linearly with the number of attached particles. From the constant-\(Δμ/kT\) results, estimate the supersaturation \(Δμ/kT\) at which branching disappears (branch count ≤ 1). Compute, if possible, the corresponding thermodynamic overstep in kJ/mol (hint: \(Δμ\) per mole = \((Δμ/kT) \cdot R T\), where \(R\) is the gas constant and \(T\) can be taken as 873 K, a typical metamorphic temperature). Save all outputs as specified below.

## Assets
- numpy: numpy
- matplotlib: matplotlib
- scipy: scipy

## Workflow steps

### Step 1: Implement and run kinetic Monte Carlo simulations
- Role: process
- Action: Write a program that implements the kMC model as described. Run all required constant‑\(Δμ/kT\) simulations and the time‑varying simulation. Store all simulation data (parameters, occupancy grids, branch counts, compactness) in memory or temporary storage.
- Evidence: not applicable (this step produces the data used by subsequent scored steps).

### Step 2: Compile morphology table
- Role: scored
- Action: From the simulation results, create a CSV file with columns: `run_id`, `delta_mu_kT`, `branch_count`, `compactness`. Include all constant‑supersaturation runs and the variable‑overstepping run. For the variable run, `delta_mu_kT` should be empty.
- Output file: `/app/outputs/morphology_table.csv`
- Format: csv
- Contract: CSV with columns: run_id (string), delta_mu_kT (float, empty for variable run), branch_count (int), compactness (float).
- Scoring: scored by hidden verifier

### Step 3: Estimate morphological transition threshold
- Role: scored
- Action: Using branch_count vs. Δμ/kT data from the constant runs, determine the dimensionless supersaturation at which branching disappears (branch_count ≤ 1). Write the estimated threshold to a plain text file. If desired, also compute the equivalent overstep in kJ/mol using the conversion hint above and include it.
- Output file: `/app/outputs/transition_estimate.txt`
- Format: txt
- Contract: Single line: `Transition_Δμ_kT = <float>`. Optionally second line: `Overstep_kJ_per_mol = <float>`.
- Scoring: scored by hidden verifier

### Step 4: Save final grid for variable overstepping run
- Role: scored
- Action: Save the final crystal occupancy grid from the time-varying Δμ/kT simulation into a plain text file.
- Output file: `/app/outputs/final_grid_variable.txt`
- Format: txt
- Contract: Space-separated integers (0 or 1), row-major order; the grid should be rectangular and contain only 0s and 1s.
- Scoring: scored by hidden verifier

## Output files
Write the following artifacts under `/app/outputs`:
- `/app/outputs/morphology_table.csv`
- `/app/outputs/transition_estimate.txt`
- `/app/outputs/final_grid_variable.txt`

No other files are required. Intermediate files (e.g., checkpoints, logs) may be written but are not scored.

## How you are scored
The hidden verifier independently checks each of the three required output artifacts. For `morphology_table.csv`, it checks that branch count is non‑decreasing with increasing Δμ/kT (monotonic trend). For `transition_estimate.txt`, it compares the reported transition supersaturation against a plausible range and, if provided, the overstep value against a reference. For `final_grid_variable.txt`, it validates that the file contains a well‑formed rectangular 2D grid of 0/1 entries. You must actually run the simulations; reporting values without computation will not satisfy the checks.