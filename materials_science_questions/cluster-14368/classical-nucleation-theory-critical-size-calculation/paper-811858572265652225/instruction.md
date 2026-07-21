# Snow Crystal Growth Simulation using Lattice Boltzmann Volumetric Reactive Boundary

## Problem background
Understanding how ice crystals grow from supersaturated water vapor in clouds is a fundamental problem in atmospheric physics. Crystal morphology can range from compact, roughly circular shapes to intricate, branched dendritic structures, depending on environmental conditions such as temperature, supersaturation, and the relative rates of diffusion and surface deposition. Reproducing this morphological variation is challenging because it requires capturing the interplay between vapor‑phase diffusion, surface reaction kinetics, and the evolving crystal shape. This task addresses the problem by applying a lattice Boltzmann method with a volumetric reactive boundary condition to simulate two‑dimensional crystal growth. The goal is to compute how the geometry of the growing solid phase changes with the Damköhler number and supersaturation, and to validate the simulation against an analytical reaction‑diffusion benchmark.

## Approach
The simulation is built on a two‑dimensional, nine‑speed (D2Q9) lattice Boltzmann model. Vapor‑phase water concentration evolves according to a convection‑diffusion equation recovered from the lattice Boltzmann scheme. At the fluid‑solid interface, a first‑order kinetic reaction removes mass from the vapor according to the local supersaturation, and the accumulated solid mass advances the interface in discrete steps. The growth direction is randomized to avoid grid anisotropy. Physical parameters (saturation vapor density over ice, vapor diffusivity, and the kinetic deposition rate) are obtained from published thermophysical expressions and used to scale the lattice Boltzmann model parameters (D_m, k_m) via similarity analysis. The key control parameter is the Damköhler number, Da, which sets the relative strength of reactive deposition versus diffusion. First, the reactive transport scheme is tested by solving a steady‑state diffusion‑reaction problem on a rectangular domain and comparing the resulting concentration field with the analytical solution. Then, two crystal growth simulations are performed, each at a different Da value, from a small central seed in a supersaturated environment. The resulting solid‑phase patterns are analyzed to quantify their morphology.

## Reproduction target
Implement the lattice Boltzmann simulator and produce the following artifacts:
1. For the rectangular‑domain validation (Da = 1440, domain size 125×100 lattice units), a file containing the steady‑state solute concentration at every grid point.
2. Two growth simulations on a 100×100 lattice, both at T = –15 °C, S = 1.20, with random growth and 750 000 time steps, but at two different Da values (Da = 16 and Da = 400). The outputs are the final solid mass arrays.
3. From these mass arrays, compute the box‑counting fractal dimension of each crystal.
4. Compute the theoretical critical dendrite arm spacing λ_c using the surface‑vapor‑layer model, with the same physical parameters and conditions.
All results are to be written to the specified output files under /app/outputs.

## Assets

- D2Q9 lattice Boltzmann method description
- Physical parameters for water vapor and ice
- Python 3 with numpy, scipy: numpy scipy

## Implementation details

### Lattice Boltzmann method for solute transport (D2Q9)
The solute concentration is represented by distribution functions \(g_i(\mathbf{x},t)\) for discrete velocities \(\mathbf{e}_i\) (\(i=0,\dots,8\)). The evolution equation is
\[
g_i(\mathbf{x}+\mathbf{e}_i\delta t, t+\delta t) = g_i(\mathbf{x}, t) - \frac{1}{\tau}[g_i(\mathbf{x}, t) - g_i^{eq}(\mathbf{x}, t)],
\]
with equilibrium distribution
\[
g_i^{eq} = w_i C\Bigl[1 + 3\mathbf{e}_i\cdot\mathbf{u} + 4.5(\mathbf{e}_i\cdot\mathbf{u})^2 - 1.5\mathbf{u}^2\Bigr],
\]
where \(\mathbf{u}=0\) for pure diffusion. The weights are \(w_0=4/9\), \(w_{1-4}=1/9\), \(w_{5-8}=1/36\). The lattice velocities are the standard D2Q9 set. The solute concentration at a node is \(C = \sum_i g_i\). The diffusivity in lattice units is
\[
D_m = \frac{1}{3}(\tau - 0.5).
\]
All simulations use \(\delta x = \delta t = 1\). For the growth simulations, the LB scalar diffusion coefficient is \(D_m = 0.0104\), which corresponds to \(\tau = 3 D_m + 0.5 = 0.5312\). For the validation simulation the parameters \(D_m = 3.47\times10^{-3}\) and \(k_m = 0.05\) are used directly (see Step 1).

### Volumetric reactive boundary with random growth
The solid phase is represented by a scalar mass field \(m(\mathbf{x})\). A node is solid if \(m \ge 1.0\); otherwise it is fluid. The reaction occurs at interface nodes—fluid nodes that have at least one solid neighbour. At each time step, for every interface node the solid mass increment is computed as
\[
\Delta m = k_m (C - C_{eq}) \, \delta t,
\]
where \(C\) is the local concentration, \(C_{eq}\) is the equilibrium concentration, and \(k_m\) is the lattice‑unit reaction rate constant. The accumulated mass is updated, and the fluid concentration is adjusted to conserve mass: \(C \leftarrow C - \Delta m\). The distribution functions at that node are reinstated to their equilibrium values based on the new concentration.

When \(m\) reaches or exceeds the threshold 1.0, the node undergoes a phase change:
- The node becomes solid; its mass is set to 1.0.
- The excess mass \(\Delta m_{\text{excess}} = m - 1.0\) is transferred to one of its four orthogonal (von Neumann) fluid neighbour nodes, chosen at random with equal probability. That neighbour receives the excess as its initial solid mass (or added to existing mass). This random growth step breaks grid symmetry and promotes dendritic branching.

Before the next LB streaming step, all solid nodes are treated as impermeable boundaries: the distribution functions that would stream from a fluid node into a solid node are bounced back.

### Boundary conditions for growth simulation
The computational domain is 100×100 lattice nodes. The outer boundaries (all four sides) are held at a constant concentration \(C_{\text{far}} = S \cdot C_{sat}\) by setting the incoming distribution functions at the boundary nodes to their equilibrium values corresponding to \(C_{\text{far}}\). The equilibrium (saturation) concentration in lattice units is \(C_{eq} = C_{sat} = 1.0\); the far‑field concentration is therefore \(C_{\text{far}} = 1.20\) (since \(S = 1.20\)).

### Initial condition
A circular seed crystal of radius 2 lattice units is placed at the center of the domain (coordinates (50, 50)). All nodes inside this circle have their solid mass set to 1.0, marking them as solid. All fluid nodes are initialized with \(C = C_{\text{far}} = 1.20\) and their distribution functions set to equilibrium.

### Scaling analysis (used in Step 2 to obtain \(k_m\))
The physical system is defined by temperature \(T = -15\,^\circ\mathrm{C} = 258.15\,\mathrm{K}\), pressure \(p = 900\,\mathrm{mbar} = 9\times10^{4}\,\mathrm{Pa}\), and condensation coefficient \(\chi = 0.1\).
- Saturated vapour pressure over ice (Murray 1967):
  \[
  e_{sat}(T) = 6.112 \;\exp\!\Bigl( \frac{22.46\,(T-273.16)}{T-0.53} \Bigr) \;\mathrm{hPa}.
  \]
  Convert to Pa by multiplying by 100.
- Saturation vapour concentration:
  \[
  C_{sat}^{(p)} = \frac{e_{sat} M}{R T},
  \]
  with \(M = 0.018\,\mathrm{kg\,mol^{-1}}\), \(R = 8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}\). The result is in \(\mathrm{kg\,m^{-3}}\).
- Water vapour diffusivity in air (Hall & Pruppacher):
  \[
  D_p = 0.211 \Bigl(\frac{T}{273.15}\Bigr)^{1.94} \Bigl(\frac{1013.25}{p}\Bigr) \;\mathrm{cm^{2}\,s^{-1}}.
  \]
  Convert to \(\mathrm{m^{2}\,s^{-1}}\): \(D_p \left( \mathrm{m^{2}\,s^{-1}} \right) = D_p(\mathrm{cm^{2}\,s^{-1}}) \times 10^{-4}\).
- Kinetic deposition rate constant (kinetic theory):
  \[
  k_p = \chi \sqrt{\frac{RT}{2\pi M}} \;\mathrm{m\,s^{-1}}.
  \]
- Physical length scale:
  \[
  \lambda_p = \frac{D_p}{k_p} \;\mathrm{m}.
  \]
Similarity between the physical system and the LB model requires that the Damköhler number be equal:
\[
Da = \frac{k_p L_p}{D_p} = \frac{k_m L_m}{D_m},
\]
and that the dimensionless length scales correspond: \(\lambda_p / L_p = \lambda_m / L_m\) with \(\lambda_m = D_m/k_m\).
Given the chosen lattice domain size \(L_m = 100\) (lattice units) and the LB diffusivity \(D_m = 0.0104\), the required reaction rate constant for a target \(Da\) is
\[
k_m = \frac{D_m \, Da}{L_m}.
\]
Thus for \(Da = 16\), \(k_m = 0.0104 \times 16 / 100 = 1.664\times10^{-3}\); for \(Da = 400\), \(k_m = 0.0104 \times 400 / 100 = 4.16\times10^{-2}\).

### Physical parameters for theoretical dendrite spacing (Step 6)
Using the same physical parameters (\(T = -15\,^\circ\mathrm{C}\), \(p = 900\,\mathrm{mbar}\), \(\chi = 0.1\)) compute \(D_p\) and \(k_p\) as described above, then \(\lambda_p = D_p / k_p\) (convert to micrometres: \(\lambda_p[\mu\mathrm{m}] = \lambda_p[\mathrm{m}] \times 10^{6}\)).
The critical dendrite arm spacing is given by
\[
\lambda_c = 2\pi \lambda_p \sqrt{\frac{S}{S-1}},
\]
with supersaturation \(S = 1.20\). Calculate \(\lambda_c\) in micrometres.

## Workflow steps

### Step 1: Validation simulation (Da=1440)
- **Role:** scored
- **Action:** Set up a steady‑state diffusion‑reaction problem on a 125 × 100 grid (x: 0 … 124, y: 0 … 99). The solute concentration \(C\) obeys \(\nabla^2 C = 0\) with a first‑order reaction boundary condition on the top edge:
  \[
  D_m \frac{\partial C}{\partial y} = k_m (C - C_{eq}) \quad \text{at } y = 99.
  \]
  The left edge (x = 0) is held at constant concentration \(C_0 = 10.0\); the bottom edge (y = 0) and right edge (x = 124) are no‑flux (\(\partial C/\partial n = 0\)). The equilibrium concentration is \(C_{eq} = 1.0\). Use the LB parameters \(D_m = 3.47\times10^{-3}\), \(k_m = 0.05\) (lattice units). Implement the solution by iterating the LB advection‑diffusion solver until convergence (e.g., relative change < 1e-7). Output the final concentration at every grid node.
- **Output file:** `/app/outputs/step_01_validation_contour.csv`
- **Format:** csv
- **Contract:** CSV with columns: `x` (integer, 0..124), `y` (integer, 0..99), `concentration` (float).
- **Scoring:** scored by hidden verifier

### Step 2: Scaling analysis and parameter setup
- **Role:** process (no output file required)
- **Action:** Using temperature \(T = -15\,^\circ\mathrm{C}\), pressure \(p = 900\,\mathrm{mbar}\), condensation coefficient \(\chi = 0.1\), compute the physical parameters as described in the Implementation details (saturation vapour concentration over ice \(C_{sat}^{(p)}\), vapour diffusivity \(D_p\), kinetic rate constant \(k_p\), and physical length scale \(\lambda_p\)). Then, following the scaling relations and the given LB constants \(L_m = 100\), \(D_m = 0.0104\), compute the required LB reaction rate constants \(k_m\) that yield \(Da = 16\) and \(Da = 400\). Record these values for use in the subsequent growth steps. No permanent output file is produced.

### Step 3: Random growth simulation Da=16
- **Role:** scored (load‑bearing)
- **Action:** On a 100 × 100 lattice, initialise the domain as described in the Implementation details (seed radius 2 lu, \(C_{sat}=1.0\), \(S=1.20\), \(C_{far}=1.20\)) and set the LB rate constant to the value computed for \(Da=16\) (\(k_m = 1.664\times10^{-3}\)). Evolve the concentration field and solid mass using the volumetric reactive boundary algorithm with random growth. Run for 750 000 time steps. Output the final solid mass at every lattice node.
- **Output file:** `/app/outputs/step_02_growth_da16.csv`
- **Format:** csv
- **Contract:** CSV with columns: `x` (integer, 0..99), `y` (integer, 0..99), `solid_mass` (float).
- **Scoring:** scored by hidden verifier

### Step 4: Random growth simulation Da=400
- **Role:** scored (load‑bearing)
- **Action:** Repeat the growth simulation using the LB parameters for \(Da=400\) (\(k_m = 4.16\times10^{-2}\)), with all other conditions identical (100 × 100 domain, seed radius 2 lu, \(S=1.20\), 750 000 time steps, random growth). Output the final solid mass array.
- **Output file:** `/app/outputs/step_03_growth_da400.csv`
- **Format:** csv
- **Contract:** CSV with columns: `x` (integer, 0..99), `y` (integer, 0..99), `solid_mass` (float).
- **Scoring:** scored by hidden verifier

### Step 5: Compute fractal dimensions
- **Role:** scored
- **Action:** From the two solid mass arrays, binarise by thresholding (solid node if mass ≥ 0.5). Compute the box‑counting fractal dimension \(D_f\) for each crystal using square box sizes that start at 1, increase by a step of 2, and stop at half the minimum grid dimension. Specifically, for a square array of side length \(N\), the sequence of box sizes is  
  \[
  L = 1, 3, 5, \dots, L_{\max}, \quad\text{where } L_{\max} = \lfloor N/2 \rfloor - 1 \;\;(\text{or the largest odd integer } < N/2).
  \]
  For the 100 × 100 grids in this problem the box sizes are 1, 3, 5, …, 49.  
  Count the number of boxes that contain at least one solid node for each size, then perform a linear regression of \(\log(N(L))\) versus \(\log(L)\); the negative slope gives the fractal dimension. Output the two fractal dimensions.
- **Output file:** `/app/outputs/step_04_fractal_dimensions.json`
- **Format:** json
- **Contract:** JSON object with keys `"da16"` (float) and `"da400"` (float).
- **Scoring:** scored by hidden verifier

### Step 6: Compute theoretical dendrite spacing limit
- **Role:** scored
- **Action:** Using the physical parameters described in the Implementation details (\(T = -15\,^\circ\mathrm{C}\), \(p = 900\,\mathrm{mbar}\), \(\chi = 0.1\)), compute \(D_p\), \(k_p\), then \(\lambda_p = D_p/k_p\) (in micrometres). With supersaturation \(S = 1.20\), compute the critical dendrite arm spacing
  \[
  \lambda_c = 2\pi \lambda_p \sqrt{\frac{S}{S-1}} \quad [\mu\mathrm{m}].
  \]
  Output the value.
- **Output file:** `/app/outputs/step_05_theoretical_critical_spacing.json`
- **Format:** json
- **Contract:** JSON object with key `"lambda_c"` (float, units µm).
- **Scoring:** scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_validation_contour.csv`
- `/app/outputs/step_02_growth_da16.csv`
- `/app/outputs/step_03_growth_da400.csv`
- `/app/outputs/step_04_fractal_dimensions.json`
- `/app/outputs/step_05_theoretical_critical_spacing.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_validation_contour.csv
- path: `/app/outputs/step_01_validation_contour.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Steady-state solute concentration field for the reactive boundary benchmark (Da=1440). Checker recomputes RMSE against the analytical solution.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `concentration`
  - `items`: object
  - `required`: object
  - `units`:
    - `concentration`: dimensionless concentration

### step_02_growth_da16.csv
- path: `/app/outputs/step_02_growth_da16.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Final solid mass array after crystal growth at Da=16. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `solid_mass`
  - `items`: object
  - `required`: object
  - `units`:
    - `solid_mass`: accumulated solid mass (lattice units)

### step_03_growth_da400.csv
- path: `/app/outputs/step_03_growth_da400.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Final solid mass array after crystal growth at Da=400. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array.
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `solid_mass`
  - `items`: object
  - `required`: object
  - `units`:
    - `solid_mass`: accumulated solid mass (lattice units)

### step_04_fractal_dimensions.json
- path: `/app/outputs/step_04_fractal_dimensions.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Box-counting fractal dimensions of the crystals at Da=16 and Da=400. The checker compares each to hidden threshold values (compact high, dendritic low) and also recomputes from the mass arrays for consistency.
- schema:
  - `type`: object
  - `required`: `da16`, `da400`
  - `items`: object
  - `units`:
    - `da16`: dimensionless
    - `da400`: dimensionless

### step_05_theoretical_critical_spacing.json
- path: `/app/outputs/step_05_theoretical_critical_spacing.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Theoretical dendrite spacing limit λ_c derived from the surface-vapor-layer model. Checked against the paper-calculated value within a tolerance.
- schema:
  - `type`: object
  - `required`: `lambda_c`
  - `items`: object
  - `units`:
    - `lambda_c`: micrometers

Notes: All output files are written under /app/outputs. The growth simulations are the core of the reproduction; the fractal dimensions are the primary scored headline with load-bearing property that requires the process and growth steps to have been executed. The theoretical spacing is a supporting scored output.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_validation_contour.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "concentration"
        ],
        "items": {},
        "required": {},
        "units": {
          "concentration": "dimensionless concentration"
        }
      },
      "description": "Steady-state solute concentration field for the reactive boundary benchmark (Da=1440). Checker recomputes RMSE against the analytical solution."
    },
    {
      "file": "step_02_growth_da16.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "solid_mass"
        ],
        "items": {},
        "required": {},
        "units": {
          "solid_mass": "accumulated solid mass (lattice units)"
        }
      },
      "description": "Final solid mass array after crystal growth at Da=16. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array."
    },
    {
      "file": "step_03_growth_da400.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "solid_mass"
        ],
        "items": {},
        "required": {},
        "units": {
          "solid_mass": "accumulated solid mass (lattice units)"
        }
      },
      "description": "Final solid mass array after crystal growth at Da=400. The checker audited shape and non‑trivial content; the actual fractal dimension is derived from this array."
    },
    {
      "file": "step_04_fractal_dimensions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "da16",
          "da400"
        ],
        "items": {},
        "units": {
          "da16": "dimensionless",
          "da400": "dimensionless"
        }
      },
      "description": "Box-counting fractal dimensions of the crystals at Da=16 and Da=400. The checker compares each to hidden threshold values (compact high, dendritic low) and also recomputes from the mass arrays for consistency."
    },
    {
      "file": "step_05_theoretical_critical_spacing.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "lambda_c"
        ],
        "items": {},
        "units": {
          "lambda_c": "micrometers"
        }
      },
      "description": "Theoretical dendrite spacing limit λ_c derived from the surface-vapor-layer model. Checked against the paper-calculated value within a tolerance."
    }
  ],
  "notes": "All output files are written under /app/outputs. The growth simulations are the core of the reproduction; the fractal dimensions are the primary scored headline with load-bearing property that requires the process and growth steps to have been executed. The theoretical spacing is a supporting scored output."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes the key quantities from your output files. The process is:
- The validation concentration grid is compared against the analytical solution for the same boundary conditions. The reward reflects how closely your field matches the true solution.
- The growth mass arrays (Da=16 and Da=400) are read, binarized, and their fractal dimensions are recomputed by the verifier. These recomputed dimensions are compared against expected thresholds that characterize the compact‑to‑dendritic transition.
- The fractal dimensions you report in the JSON file are checked for consistency with the mass arrays; any discrepancy reduces the reward.
- The theoretical dendrite spacing λ_c is compared against a reference value derived from the simulation parameters.
Each scored stage carries a weight, and the final reward is the weighted sum across all stages. The main weight rests on the fractal dimensions and their consistency with the simulated crystals. Merely reporting numbers without genuinely running the simulation is detectable and will yield a low score.