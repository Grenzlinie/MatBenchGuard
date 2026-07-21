# Triangular Spring Network Simulation for Elastic Moduli of 2D Hole‑Containing Composites

## Problem background
In this task, we study the elastic properties of a two‑dimensional continuum composite consisting of an elastic matrix with randomly centered circular holes (voids). As the area fraction of the holes increases, the effective Young’s modulus and Poisson ratio of the sheet decrease, eventually vanishing at a geometric percolation threshold. The challenge is to compute the normalized Young’s modulus and Poisson ratio of such a composite as a function of the remaining matrix area fraction, and to determine the critical area fraction at which the rigid matrix first disconnects.

## Approach
We employ a digital‑image‑based triangular spring network method. The continuous sheet is discretized into a periodic triangular lattice of hexagonal pixels. Nearest‑neighbor pixels are connected by linear springs, with three different force constants arranged in an alternating pattern that preserves macroscopic isotropy. Circular holes are introduced by randomly placing overlapping circles of a fixed diameter; any pixel whose centre falls inside a hole is marked as a hole, and springs connected to hole pixels are assigned zero stiffness. The effective elastic response is probed by applying a small uniaxial strain in one direction (both tensile and compressive) and relaxing the node positions and the perpendicular unit‑cell length by conjugate‑gradient minimization of the total harmonic spring energy. From the relaxed energy per unit area and the equilibrium perpendicular cell length, we extract the Young’s modulus and Poisson ratio of the hole‑containing sheet. To normalize the results, we first compute analytic expressions for the moduli of the perfect (hole‑free) lattice for each set of spring constants. The simulation is repeated for many independent random hole configurations at each matrix area fraction, and the average moduli are reported. Additionally, a lattice burning algorithm is used on the digital hole‑matrix images to estimate the geometric percolation threshold.

## Reproduction target
Compute, for each of the three spring‑constant sets (α,β,γ) = (1,1,1), (1,1,4), (1,6,7), the normalized Young’s modulus E/E₀ (where E₀ is the modulus of the perfect lattice) and the Poisson ratio σ as functions of the matrix area fraction p, covering a range from low p (near the percolation threshold) up to p ≈ 1.0 (nearly no holes). Average results over 10 independent random hole configurations per p value. Additionally, estimate the critical matrix area fraction p_c at which the matrix ceases to percolate, using the same hole‑matrix images.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Key definitions and formulas
These are provided so you can build a correct simulation. They are taken from a known published reference on digital‑image‑based elasticity of hole‑containing composites.

### Triangular lattice and pixel geometry
- The sheet is represented by a periodic triangular lattice of **hexagonal pixels** whose centers form a two‑dimensional triangular Bravais lattice.
- Choose nearest‑neighbor centre‑to‑centre distance as the unit of length.  The two primitive lattice vectors can be taken as **a₁ = (1, 0)** and **a₂ = (1/2, √3/2)**.
- A 210×210 pixel system means a 210×210 grid of primitive cells defined by a₁ and a₂.  The simulation cell is a parallelogram with sides **Lₓ = 210·a₁** and **Lᵧ = 210·a₂**.  Periodic boundary conditions are applied.
- Each pixel is a regular hexagon; you do **not** need its exact outline – only its center position matters for spring connections and for checking whether the pixel belongs to a hole.

### Spring network – connection pattern (Fig. 2 of the reference)
- Every pixel center is connected by a linear (Hookean) spring to each of its **six nearest neighbours** on the triangular lattice.  The six neighbour vectors, in units of the nearest‑neighbour distance, are:
  **d₁ = (1, 0),   d₂ = (1/2, √3/2),   d₃ = (-1/2, √3/2),
  d₄ = -d₁,   d₅ = -d₂,   d₆ = -d₃**.
- To allow an isotropic elastic response with adjustable Poisson ratio, three different spring constants **α, β, γ** are used.  The assignment is made according to the **direction** of the bond, forming three interlocking honeycomb sublattices:
  - Bonds along the horizontal direction **(d₁ and d₄)** → spring constant **α**,
  - Bonds along the two upward‑sloping directions **(d₂ and d₃) and their opposites (d₅ and d₆)** → spring constant **β** for one set and **γ** for the other.  Conventionally, **β** is assigned to the pair **d₂ / d₅** and **γ** to **d₃ / d₆** (or vice versa, the important point is that each of the three lattice directions gets its own constant).

### Hole definition
- Circular holes of **diameter 11 pixels** (radius = 5.5 in length units) are placed with randomly chosen centres.  Holes may overlap.
- A pixel is classified as **hole** if its **centre** lies inside any hole (distance to hole centre < 5.5); otherwise it is **matrix**.
- Any spring that connects at least one hole pixel is assigned a force constant of **zero**.
- The matrix area fraction **p** is the ratio of matrix pixels to total pixels.

### Elastic moduli of the perfect (hole‑free) lattice
For the perfect lattice before any holes are introduced, the analytic formulas are:

**Area bulk modulus:**
\[
K_o = \frac{1}{\sqrt{12}} (\alpha + \beta + \gamma) \tag{1}
\]

**Shear modulus:**
\[
\mu_o = \sqrt{\frac{27}{16}} \left( \frac{1}{\alpha} + \frac{1}{\beta} + \frac{1}{\gamma} \right)^{-1} \tag{2}
\]

**Young’s modulus \(E_o\) and Poisson ratio \(\sigma_o\)** (derived from \(K_o\) and \(\mu_o\) in two dimensions):
\[
E_o = \frac{4 K_o \mu_o}{K_o + \mu_o} \tag{3}
\]
\[
\sigma_o = \frac{K_o - \mu_o}{K_o + \mu_o} \tag{4}
\]

Alternatively, the direct expressions in terms of α, β, γ are:
\[
\sigma_o = 1 - \frac{2}{1 + \frac{2}{9}(\alpha+\beta+\gamma)(\frac{1}{\alpha}+\frac{1}{\beta}+\frac{1}{\gamma})} \tag{5}
\]
\[
E_o = \frac{2\sqrt{3}(\alpha+\beta+\gamma)}{3\left[1 + \frac{2}{9}(\alpha+\beta+\gamma)(\frac{1}{\alpha}+\frac{1}{\beta}+\frac{1}{\gamma})\right]} \tag{6}
\]

### Extracting E and σ from a simulation
For a given hole configuration and spring‑constant set:
1. Apply a small uniaxial strain **ε** (∼10⁻³) in the **x‑direction** (the direction of a₁).  
   The strain is applied by scaling all node x‑coordinates by a factor (1 + ε) and simultaneously adjusting the length of the simulation cell in the y‑direction as a free variable.
2. Perform a **conjugate‑gradient relaxation** of the total harmonic spring energy with respect to **all node positions** and the **y‑cell length**.  The node positions are periodic; the y‑cell length is the only macroscopic degree of freedom allowed to vary, mimicking the Poisson contraction.
3. After relaxation, record:
   - The **total elastic energy** of the system, \(E_{\text{total}}\).
   - The **area** A of the undeformed simulation cell (Lₓ · Lᵧ).
   - The **equilibrium length** of the cell in the y‑direction, \(L_y^{\text{def}}\).
4. Compute the **energy density** \(u = E_{\text{total}} / A\).
5. In two dimensions, for a uniaxial strain with transverse relaxation, the energy density is \(u = \frac{1}{2} E \varepsilon^2\).  Therefore,
   \[
   E = \frac{2u}{\varepsilon^2}
   \]
6. The transverse strain is \(\varepsilon_{\perp} = (L_y^{\text{def}} - L_y) / L_y\).  Poisson ratio is
   \[
   \sigma = -\frac{\varepsilon_{\perp}}{\varepsilon}
   \]
7. Perform the simulation for a **tensile** strain (+ε) and a **compressive** strain (−ε), then average the resulting E and σ to cancel any small non‑linearities.

## Workflow steps

### Step 1: Generate random hole configurations on triangular lattice
- Role: process
- Action: For each of the 10 target matrix area fractions p in the range ~0.35–1.0, generate 10 independent random configurations of overlapping circular holes (diameter 11, radius 5.5). Place hole centres randomly on a 210×210 pixel periodic triangular lattice; mark each pixel as matrix or hole by testing whether its centre falls inside any hole. Compute the actual area fraction p from pixel counts. Store each configuration (pixel masks) for later simulation and percolation analysis.
- Evidence: none

### Step 2: Compute perfect-lattice elastic moduli analytically
- Role: process
- Action: For each spring-constant set (α,β,γ) = (1,1,1), (1,1,4), (1,6,7), compute the perfect‑lattice moduli \(K_o, \mu_o, E_o, \sigma_o\) using formulas (1)–(6) above. These values will be used to normalize the simulation results.
- Evidence: none

### Step 3: Simulate elastic response per configuration
- Role: process
- Action: For each hole configuration and each spring set, construct the nearest‑neighbour spring network as described in **Key definitions**: assign α, β, γ to matrix–matrix bonds according to the direction rules, and set force constant to zero for any bond involving a hole pixel. Apply a uniaxial strain ε ≈ ±10⁻³, relax using conjugate gradient (minimising energy with respect to all node co‑ordinates and the y‑cell length), and extract E and σ via the energy‑density formula. Record E and σ for every configuration.
- Evidence: none

### Step 4: Compute geometric percolation threshold
- Role: scored
- Action: Implement a lattice burning algorithm on the hole‑matrix images generated in Step 1. For a range of matrix area fractions p around the critical region, determine the percolation probability across multiple configurations and estimate the critical matrix area fraction p_c. Write the result to `percolation_threshold.csv`.
- Output file: `/app/outputs/percolation_threshold.csv`
- Format: csv
- Contract: Columns: p_c (float, critical matrix area fraction).
- Scoring: scored by hidden verifier

### Step 5: Compute average elastic moduli and normalized ratios
- Role: scored (load‑bearing)
- Action: For each spring set and each p, compute the mean (and optionally standard error) of E/E₀ (using E₀ from Step 2) and σ from the 10 configuration replicates. Write the averaged results to `simulation_results.csv`.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: Columns: set_id (string, one of '111','114','167'), p (float, area fraction), E_over_E0 (float, normalized Young's modulus), sigma (float, Poisson ratio).
- Scoring: scored by hidden verifier

## Output files
Write all final artifacts under `/app/outputs`:
- `/app/outputs/percolation_threshold.csv`
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### percolation_threshold.csv
- path: `/app/outputs/percolation_threshold.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The estimated critical matrix area fraction (percolation threshold) for the system of overlapping circular holes.
- schema:
  - `type`: table
  - `required_columns`: `p_c`
  - `units`:
    - `p_c`: dimensionless

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Averaged Young's modulus ratio and Poisson ratio vs matrix area fraction for three spring-constant sets, as computed from the triangular spring network simulations.
- schema:
  - `type`: table
  - `required_columns`: `set_id`, `p`, `E_over_E0`, `sigma`
  - `units`:
    - `p`: dimensionless
    - `E_over_E0`: dimensionless
    - `sigma`: dimensionless

Notes: The checker will compare simulation_results.csv entries against a hidden reference derived from the paper's interpolation formula and expected trends. The percolation threshold is compared to the paper-reported value within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "percolation_threshold.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p_c"
        ],
        "units": {
          "p_c": "dimensionless"
        }
      },
      "description": "The estimated critical matrix area fraction (percolation threshold) for the system of overlapping circular holes."
    },
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "set_id",
          "p",
          "E_over_E0",
          "sigma"
        ],
        "units": {
          "p": "dimensionless",
          "E_over_E0": "dimensionless",
          "sigma": "dimensionless"
        }
      },
      "description": "Averaged Young's modulus ratio and Poisson ratio vs matrix area fraction for three spring-constant sets, as computed from the triangular spring network simulations."
    }
  ],
  "notes": "The checker will compare simulation_results.csv entries against a hidden reference derived from the paper's interpolation formula and expected trends. The percolation threshold is compared to the paper-reported value within a tolerance."
}
```

## How you are scored
Your work will be evaluated by a hidden verifier that independently scrutinizes each required output artifact. For the percolation threshold, the reported value will be compared to a hidden reference within a tolerance. For the elastic moduli, the verifier will check that the E/E₀ vs p curve decreases monotonically and approaches unity at p≈1, that the Poisson ratio for the isotropic spring set remains constant and for the other sets approaches a value near 1/3 at low p, and that the quantitative values of E/E₀ and σ fall within acceptable relative deviations from theoretical expectations (including the known initial slope and effective medium theory limits). The final reward is a weighted combination of these checks; simply reporting numbers without executing the simulation will not pass.