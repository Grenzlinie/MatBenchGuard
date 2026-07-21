# Kikuchi Cluster-Variation Calculation of Order-Disorder Phase Diagram in f.c.c. Binary Alloys

## Problem background
Binary alloys with a face-centered cubic (f.c.c.) lattice that undergo an order-disorder transformation can form L1₂ (Cu₃Au-type) and L1₀ (CuAu-type) superstructures. Accurate phase diagrams and thermodynamic properties for such systems are essential for understanding alloy stability and guiding materials design. Simple mean-field theories predict only a single maximum in the order-disorder transition temperature, at the equiatomic composition, and systematically underestimate the degree of order near the critical temperature and the ordering energy itself. The Kikuchi cluster-variation method improves on these theories by treating tetrahedron cluster probabilities correctly, thereby capturing short-range order and yielding a more faithful picture of the order-disorder transition, including the first-order character and the possibility of multiple ordered-phase regions. Reproducing the complete phase diagram and the associated thermodynamic quantities—transition temperatures, ordering energies, entropy and energy jumps, and the configurational heat capacity—validates the theoretical methodology and provides reference predictions against which experimental observations can be compared. The present task is to recompute all of these quantities from first principles, using only the published cluster-variation formalism and open-source numerical tools.

## Approach
The core idea is to construct the configuration free energy of a binary A–B alloy on an f.c.c. lattice using the Kikuchi cluster-variation method with the tetrahedron as the basic cluster and nearest-neighbour interactions. The free energy per atom, expressed in terms of the probabilities of the various tetrahedron, pair and point configurations, is first written down. By imposing symmetry appropriate to the disordered state (all sublattice point probabilities equal to the composition) and to the two ordered superstructures L1₂ and L1₀ (distinct sublattice occupations consistent with each long-range order), the number of independent probability variables is reduced. Two-phase equilibrium between the ordered and disordered phases is defined by equality of chemical potentials, which leads to a system of nonlinear equations whose unknowns are the disordered-phase composition, the equilibrium reduced temperature t = k_B T / v (where v is the ordering energy), and the independent tetrahedron probabilities in both phases. Solving this system for a range of ordered-phase compositions maps out the phase boundaries. Once the phase boundaries are known, the internal-equilibrium equations can be solved separately for the ordered phase at temperatures below the two-phase region and for the disordered phase above it, giving the temperature-dependent cluster probabilities. From these solutions one then computes the thermodynamic quantities of interest: the ordering energy–critical temperature relation, the entropy and energy discontinuities at the transition, and the configurational heat capacity obtained by numerical differentiation of the internal energy.

## Mathematical formalism

All quantities are defined in the paper. The complete set of equations needed to implement the cluster‑variation calculation is reproduced below.

### Lattice and probabilities
The f.c.c. lattice is decomposed into four simple cubic sublattices (labelled 0,1,2,3). The probabilities of finding configurations on points, nearest‑neighbour pairs, and tetrahedra (the cluster) are denoted by:
- $x_l$ ($l=1,\dots,8$) – point probabilities,
- $y_k$ ($k=1,\dots,24$) – pair probabilities,
- $z_j$ ($j=1,\dots,16$) – tetrahedron probabilities.

The indexing follows Fig. 2 of the paper. The $z_j$ describe the occupancy of the four tetrahedron vertices $(0,1,2,3)$; for example $z_2$ is the probability that site 0 is occupied by an $A$ atom and sites 1, 2, 3 by $B$ atoms.

Normalisation:
$$
\sum_{j=1}^{16} z_j = 1,
\qquad
\sum_{k=1}^{24} y_k = 1,
\qquad
\sum_{l=1}^{8} x_l = 1 .
$$

### Free energy
The configuration free energy per atom, divided by the ordering energy
$v = 2v_{AB} - v_{AA} - v_{BB}$, is

$$
\begin{aligned}
f = \frac{F}{N v}
   = &-\frac12 \sum_{i=0}^{5} \bigl( y_{2+4i} + y_{3+4i} \bigr) \\
     &- t \Bigl( \sum_{k=1}^{24} y_k \ln y_k
               - \frac54 \sum_{l=1}^{8} x_l \ln x_l
               - 2 \sum_{j=1}^{16} z_j \ln z_j \Bigr),
\end{aligned}
\tag{2.2}
$$
with $t = k_{\!B} T / v$ the dimensionless temperature.

### Geometric relations
The point and pair probabilities are linear combinations of the $z_j$:

**Point probabilities**  
$$
\begin{aligned}
x_1 &= z_2+z_6+z_7+z_8+z_{12}+z_{13}+z_{14}+z_{16} \\
x_2 &= z_1+z_3+z_4+z_5+z_9+z_{10}+z_{11}+z_{15} \\
x_3 &= z_3+z_6+z_9+z_{11}+z_{12}+z_{14}+z_{15}+z_{16} \\
x_4 &= z_1+z_2+z_4+z_5+z_7+z_8+z_{10}+z_{13} \\
x_5 &= z_4+z_7+z_9+z_{10}+z_{12}+z_{13}+z_{15}+z_{16} \\
x_6 &= z_1+z_2+z_3+z_5+z_6+z_8+z_{11}+z_{14} \\
x_7 &= z_5+z_8+z_{10}+z_{11}+z_{13}+z_{14}+z_{15}+z_{16} \\
x_8 &= z_1+z_2+z_3+z_4+z_6+z_7+z_9+z_{12}
\end{aligned}
$$

**Pair probabilities** (24 relations)
$$
\begin{aligned}
y_{1}&=z_1+z_4+z_5+z_{10},      & y_{2}&=z_3+z_9+z_{11}+z_{15},   & y_{3}&=z_2+z_7+z_8+z_{13}, \\
y_{4}&=z_6+z_{12}+z_{14}+z_{16},& y_{5}&=z_1+z_3+z_5+z_{11},      & y_{6}&=z_4+z_9+z_{10}+z_{15}, \\
y_{7}&=z_2+z_6+z_8+z_{14},      & y_{8}&=z_7+z_{12}+z_{13}+z_{16}, & y_{9}&=z_1+z_3+z_4+z_9, \\
y_{10}&=z_5+z_{10}+z_{11}+z_{15},& y_{11}&=z_2+z_6+z_7+z_{12},      & y_{12}&=z_8+z_{13}+z_{14}+z_{16}, \\
y_{13}&=z_1+z_2+z_5+z_8,        & y_{14}&=z_4+z_7+z_{10}+z_{13},   & y_{15}&=z_3+z_6+z_{11}+z_{14}, \\
y_{16}&=z_9+z_{12}+z_{15}+z_{16},& y_{17}&=z_1+z_2+z_4+z_7,        & y_{18}&=z_5+z_8+z_{10}+z_{13}, \\
y_{19}&=z_3+z_6+z_9+z_{12},      & y_{20}&=z_{11}+z_{14}+z_{15}+z_{16},& y_{21}&=z_1+z_2+z_3+z_6, \\
y_{22}&=z_5+z_8+z_{11}+z_{14},   & y_{23}&=z_4+z_7+z_9+z_{12},      & y_{24}&=z_{10}+z_{13}+z_{15}+z_{16}.
\end{aligned}
$$

These relations allow $f$ to be expressed solely in terms of the $z_j$.

### Disordered state – independent variables
In the totally disordered state all four sublattices are equally occupied:
$$
x_1 = x_3 = x_5 = x_7 = c_A .
$$
From the normalisation and the geometric relations one can eliminate $z_1$–$z_5$. The remaining independent tetrahedron probabilities are $z_6,\dots,z_{16}$. The eliminated probabilities are:

$$
\begin{aligned}
z_1 &= 1 - 4c_A + z_6+z_7+z_8+z_9+z_{10}+z_{11} \\
    &\quad + 2(z_{12}+z_{13}+z_{14}+z_{15}) + 3z_{16}, \tag{3.2}\\
z_2 &= c_A - z_6 - z_7 - z_8 - z_{12} - z_{13} - z_{14} - z_{16},\\
z_3 &= c_A - z_6 - z_9 - z_{11} - z_{12} - z_{14} - z_{15} - z_{16},\\
z_4 &= c_A - z_7 - z_9 - z_{10} - z_{12} - z_{13} - z_{15} - z_{16},\\
z_5 &= c_A - z_8 - z_{10} - z_{11} - z_{13} - z_{14} - z_{15} - z_{16}.
\end{aligned}
$$

### Ordered state – independent variables (general)
For the ordered phases the conserved composition is
$$
x_1 + x_3 + x_5 + x_7 = 4c_A .
$$
Together with normalisation this allows the elimination of $z_1$ and $z_2$:

$$
\begin{aligned}
z_1 &= 1 - 4c_A + z_6+z_7+z_8+z_9+z_{10}+z_{11} \\
    &\quad + 2(z_{12}+z_{13}+z_{14}+z_{15}) + 3z_{16}, \tag{4.1}\\[2mm]
z_2 &= 4c_A - z_3 - z_4 - z_5
      - 2(z_6+z_7+z_8+z_9+z_{10}+z_{11}) \\
    &\quad - 3(z_{12}+z_{13}+z_{14}+z_{15}) - 4z_{16}. \tag{4.2}
\end{aligned}
$$

The independent variables are $z_3,\dots,z_{16}$ (14 variables) for a generic ordered state. **Additional symmetry constraints, specific to the L1₂ and L1₀ superstructures, must now be imposed to further reduce the number of independent variables and to identify which ordered phase a solution belongs to.**

### Symmetry constraints for the L1₂ and L1₀ superstructures

The f.c.c. ordered phases are characterised by the occupation pattern of the four sublattices.

- **L1₂ superstructure** (Cu₃Au-type): three sublattices are equivalent, and one is distinct. Conventionally, sublattices 1, 2, and 3 are equivalent, while sublattice 0 is distinct. Therefore the point probabilities satisfy
  $$
  x_3 = x_5 = x_7 \quad\text{and}\quad x_4 = x_6 = x_8 .
  $$
  Equivalently, the probability of finding an $A$ atom is the same on sites 1,2,3 and the probability of a $B$ atom is the same on those three sites. These relations, together with the geometric relations, imply a set of linear equations among the $z_j$. They reduce the number of independent $z$ variables to **7** (the exact identities can be derived by the agent; the important point is that only 7 independent tetrahedron probabilities remain). Every solution of the ordered‑state equilibrium equations that satisfies these constraints corresponds to the L1₂ phase.

- **L1₀ superstructure** (CuAu-type): sublattices 0 and 1 are equivalent, and sublattices 2 and 3 are equivalent. Thus
  $$
  x_1 = x_3,\quad x_2 = x_4,\quad x_5 = x_7,\quad x_6 = x_8 .
  $$
  Again, these relations give linear constraints among the $z_j$ and reduce the number of independent variables to **6**. Solutions satisfying these constraints correspond to the L1₀ phase.

During the calculation, for each ordered composition $c_A$, two separate sets of internal equilibrium equations (5.4) are solved: one with the L1₂ symmetry constraints and one with the L1₀ constraints. The solution with the lower free energy (or, equivalently, the one that yields a stable equilibrium) is selected, and its phase type is recorded. This classification directly supplies the `phase_type` column in the phase‑diagram output.

### Phase equilibrium
The two phases (disordered = 1, ordered = 2) are in equilibrium when the chemical potentials of both components are equal. For a binary system this leads to

$$
\begin{aligned}
\frac{\partial f^{(1)}}{\partial c_A^{(1)}} - \frac{\partial f^{(2)}}{\partial c_A^{(2)}} &= 0, \\
f^{(1)} - f^{(2)} - \bigl(c_A^{(1)}-c_A^{(2)}\bigr)
\frac{\partial f^{(2)}}{\partial c_A^{(2)}} &= 0,
\end{aligned}
\tag{5.2}
$$
where the total derivatives $\partial f/\partial c_A$ are evaluated by applying the chain rule through the eliminated $z$ variables and the $x_l$. Full expressions are given in the paper (Eqs. following (5.2)); they involve the derivatives of the free energy with respect to $x_l$, $y_k$, $z_m$ and the derivatives of the eliminated $z$ with respect to $c_A$.

### Internal equilibrium
In addition to the phase‑equilibrium conditions, each phase must be in internal equilibrium with respect to its remaining independent $z$ variables.

For the **disordered phase** (11 equations):
$$
\frac{\partial f^{(1)}}{\partial z_i^{(1)}}
+ \sum_{k=1}^{24} \frac{\partial f^{(1)}}{\partial y_k^{(1)}}
   \frac{\partial y_k^{(1)}}{\partial z_i^{(1)}}
+ \sum_{m=1}^{5} \frac{\partial f^{(1)}}{\partial z_m^{(1)}}
   \frac{\partial z_m^{(1)}}{\partial z_i^{(1)}}
= 0,
\qquad i=6,\dots,16. \tag{5.3}
$$

For the **ordered phase** – after imposing the symmetry constraints of either L1₂ or L1₀, only the independent variables that survive the constraints appear. For instance, with L1₂ symmetry there are 7 independent variables, and with L1₀ there are 6. In each case, the equilibrium condition is
$$
\frac{\partial f^{(2)}}{\partial z_i^{(2)}}
+ \sum_{l=1}^{8} \frac{\partial f^{(2)}}{\partial x_l^{(2)}}
   \frac{\partial x_l^{(2)}}{\partial z_i^{(2)}}
+ \sum_{k=1}^{24} \frac{\partial f^{(2)}}{\partial y_k^{(2)}}
   \frac{\partial y_k^{(2)}}{\partial z_i^{(2)}}
+ \sum_{m=1}^{2} \frac{\partial f^{(2)}}{\partial z_m^{(2)}}
   \frac{\partial z_m^{(2)}}{\partial z_i^{(2)}}
= 0,
$$
where the sum over $m$ includes $z_1$ and $z_2$ (which are expressed in terms of the independent $z$ via (4.1)–(4.2)), and the indices $i$ run over the independent set. The partial derivatives of $f$ with respect to the basic probabilities are straightforward:
$$
\begin{aligned}
\frac{\partial f}{\partial x_l}   &= \frac54\, t \, (1 + \ln x_l), \\
\frac{\partial f}{\partial y_k}   &= 
-\frac12\bigl(\delta_{k=2+4i}+\delta_{k=3+4i}\bigr)
- t \, (1 + \ln y_k), \\
\frac{\partial f}{\partial z_j}   &= 2\, t \, (1 + \ln z_j),
\end{aligned}
$$
where the Kronecker‑delta terms for $y_k$ contribute only for those $k$ that appear in the energy sum of (2.2).

### Numerical solution strategy
The complete system of nonlinear equations consists of:
- 2 phase‑equilibrium conditions (5.2),
- 11 disordered‑phase internal equilibrium equations (5.3),
- internal equilibrium equations for the ordered phase, whose number depends on the symmetry (7 for L1₂, 6 for L1₀).

The unknowns are:
- $t$ – reduced equilibrium temperature,
- $c_A^{(1)}$ – composition of the disordered phase,
- disordered‑phase independent $z$ (11 variables),
- ordered‑phase independent $z$ (7 or 6 variables).

Total number of equations equals the number of unknowns when $c_A^{(2)}$ is held fixed, because the system is closed: 2 (phase equil.) + 11 (disordered) + (7 or 6) = 20 or 19 equations for the same number of unknowns. Therefore one ordered‑phase composition $c_A^{(2)}$ is treated as a given parameter. For each chosen $c_A^{(2)}$ the system is closed and can be solved numerically with an iterative method (e.g. SciPy’s `fsolve` or `root`). Good initial guesses can be obtained by starting at the stoichiometric compositions and then stepping along the composition axis.

After obtaining the two‑phase equilibrium ($t_e$, $c_A^{(1)}$, and all $z$) for several $c_A^{(2)}$, the phase boundaries are constructed:
- **Ordered‑phase boundary**: for a given ordered composition $c_A$, the lower transition temperature is $T_c^{\text{lower}}(c_A)=t_e$ obtained by solving the system with the appropriate symmetry constraints and with $c_A^{(2)}=c_A$.
- **Disordered‑phase boundary**: for a given disordered composition $c_A$, the upper transition temperature is $T_c^{\text{upper}}(c_A)=t_e$ obtained by solving the system with $c_A^{(1)}$ treated as given (i.e., swap the roles and treat the disordered composition as the parameter; the equilibrium temperature is unchanged but the corresponding ordered composition is found).

To produce smooth phase‑diagram data, solve the system for a dense set of $c_A^{(2)}$ values covering the composition ranges where L1₂ and L1₀ appear, each time applying both symmetry constraints and selecting the stable ordered phase, or simply solve for each symmetry assumption independently and later determine the phase boundaries from the lowest free energy branch.

For the **homogeneous phases** (Step 3 in the workflow) the internal‑equilibrium equations (5.3) or the appropriate symmetry‑restricted version of (5.4) are solved separately at fixed $c_A$ and $t$, without the phase‑equilibrium conditions. The solutions give the temperature‑dependent cluster probabilities.

## Workflow steps

### Step 1: Solve two‑phase equilibrium system
- Role: process
- Action: Implement the Kikuchi cluster‑variation free energy as detailed above. For a given ordered‑phase composition $c_A^{(2)}$, formulate the full system of equations (5.2)–(5.4) **with the symmetry constraints of either the L1₂ or the L1₀ superstructure** and solve numerically to obtain $t_e$, $c_A^{(1)}$, and the independent $z$ variables in both phases. Repeat this procedure for a range of $c_A^{(2)}$ that covers the L1₂ and L1₀ phase regions, and for **both** symmetries. Record the stable ordered phase (the one giving the lowest free energy at the equilibrium $t_e$) and its `phase_type`.
- No output file is required from this step; all needed information is kept in memory for the subsequent scored outputs.

### Step 2: Produce phase diagram data
- Role: scored (load‑bearing)
- Action: From the stable equilibrium solutions, construct the phase boundaries. For a set of compositions $c_A$ that belong to the L1₂ and L1₀ phase regions, compute the lower transition temperature (ordered‑phase boundary) and the upper transition temperature (disordered‑phase boundary) by interpolation of the solved equilibria. Write the data to a CSV file. Each row corresponds to one composition and one ordered superstructure type.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Header row: `phase_type, composition_c_A, T_c_lower, T_c_upper`. The `phase_type` field contains the string `"L12"` or `"L10"` according to which symmetry was identified as stable. All values numeric; no missing entries.
- Scoring: scored by hidden verifier

### Step 3: Solve homogeneous‑phase equilibrium conditions
- Role: process
- Action: Using the equilibrium temperature and composition obtained from the two‑phase solution, solve the internal‑equilibrium equations for the ordered phase (with the appropriate symmetry) at temperatures below the equilibrium temperature and for the disordered phase at temperatures above it, to obtain the temperature‑dependent cluster probabilities. These solutions are internal and are not written to a separate output file; they are used to compute the transition properties and heat capacity.
- No standalone output file is generated from this step.

### Step 4: Compute transition properties
- Role: scored (load‑bearing)
- Action: From the equilibrium and homogeneous‑phase solutions, calculate: the maximum order‑disorder transition temperatures for the L1₂ and L1₀ superstructures, the composition at the L1₂ maximum and its shift from the stoichiometric AB₃ composition, the ordering energy ratios $v/(k_BT_c)$ for both superstructures, and the entropy and energy jump magnitudes ($\Delta S$ and $\Delta E$) at the transition for compositions $c_A=0.25$ and $c_A=0.5$. Write these values to a JSON file.
- Output file: `/app/outputs/transition_properties.json`
- Format: json
- Contract: JSON object with keys: `max_Tc_L12, max_Tc_L10, composition_at_max_L12, shift_from_AB3, v_over_kTc_L12, v_over_kTc_L10, entropy_jump_L12_at_0_25, energy_jump_L12_at_0_25, entropy_jump_L10_at_0_5, energy_jump_L10_at_0_5`. All values numeric.
- Scoring: scored by hidden verifier

### Step 5: Compute configuration heat capacity
- Role: scored
- Action: Using the temperature‑dependent internal energy from the homogeneous‑phase solutions, compute the configuration heat capacity $C_v = dE/dT$ by numerical differentiation for the compositions $c_A=0.25$ and $c_A=0.5$. Write the data (composition, reduced temperature, $C_v$ per atom in units of the Boltzmann constant) to a CSV file.
- Output file: `/app/outputs/heat_capacity_data.csv`
- Format: csv
- Contract: CSV with columns: `composition_c_A, reduced_temperature_t, C_v_per_Nk`. All values numeric; no missing entries.
- Scoring: scored by hidden verifier; a structural audit checks that the heat‑capacity peak is located near the expected transition temperature for each composition. No explicit entropy‑jump integration is performed by the verifier.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/transition_properties.json`
- `/app/outputs/heat_capacity_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phase boundaries of L1₂ and L1₀ ordered phases: for each composition the lower and upper reduced transition temperatures. Compared to hidden gold values within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `phase_type`, `composition_c_A`, `T_c_lower`, `T_c_upper`
  - `units`:
    - `composition_c_A`: mole fraction (dimensionless)
    - `T_c_lower`: $k_B T / v$ (dimensionless)
    - `T_c_upper`: $k_B T / v$ (dimensionless)

### transition_properties.json
- path: `/app/outputs/transition_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregate transition properties computed from the cluster‑variation solutions. Each numeric key is compared to a hidden gold value with absolute or relative tolerance.
- schema:
  - `type`: object
  - `required`:
    - `max_Tc_L12`: number
    - `max_Tc_L10`: number
    - `composition_at_max_L12`: number
    - `shift_from_AB3`: number
    - `v_over_kTc_L12`: number
    - `v_over_kTc_L10`: number
    - `entropy_jump_L12_at_0_25`: number
    - `energy_jump_L12_at_0_25`: number
    - `entropy_jump_L10_at_0_5`: number
    - `energy_jump_L10_at_0_5`: number
  - `units`:
    - `max_Tc_L12`: $k_B T / v$
    - `max_Tc_L10`: $k_B T / v$
    - `composition_at_max_L12`: $c_A$
    - `shift_from_AB3`: difference in $c_A$
    - `v_over_kTc_L12`: dimensionless
    - `v_over_kTc_L10`: dimensionless
    - `entropy_jump_L12_at_0_25`: units of $R$
    - `energy_jump_L12_at_0_25`: units of $N v$
    - `entropy_jump_L10_at_0_5`: units of $R$
    - `energy_jump_L10_at_0_5`: units of $N v$

### heat_capacity_data.csv
- path: `/app/outputs/heat_capacity_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Configuration heat capacity per atom as functions of temperature for $c_A=0.25$ and $0.5$. The verifier performs a structural audit: it checks that the heat capacity peak occurs near the expected transition temperature for each composition.
- schema:
  - `type`: table
  - `required_columns`: `composition_c_A`, `reduced_temperature_t`, `C_v_per_Nk`
  - `units`:
    - `composition_c_A`: mole fraction (dimensionless)
    - `reduced_temperature_t`: $k_B T / v$ (dimensionless)
    - `C_v_per_Nk`: units of $k_B$ (dimensionless)

Notes: All scored outputs derive entirely from the agent's own implementation of the Kikuchi cluster‑variation formalism. No pre‑computed equilibrium data are supplied.

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
          "phase_type",
          "composition_c_A",
          "T_c_lower",
          "T_c_upper"
        ],
        "units": {
          "composition_c_A": "mole fraction (dimensionless)",
          "T_c_lower": "k_B T / v (dimensionless)",
          "T_c_upper": "k_B T / v (dimensionless)"
        }
      },
      "description": "Phase boundaries of L1₂ and L1₀ ordered phases: for each ordered‑phase composition the lower and upper reduced transition temperatures. Compared to hidden gold values within a relative tolerance."
    },
    {
      "file": "transition_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "max_Tc_L12": "number",
          "max_Tc_L10": "number",
          "composition_at_max_L12": "number",
          "shift_from_AB3": "number",
          "v_over_kTc_L12": "number",
          "v_over_kTc_L10": "number",
          "entropy_jump_L12_at_0_25": "number",
          "energy_jump_L12_at_0_25": "number",
          "entropy_jump_L10_at_0_5": "number",
          "energy_jump_L10_at_0_5": "number"
        },
        "units": {
          "max_Tc_L12": "k_B T / v",
          "max_Tc_L10": "k_B T / v",
          "composition_at_max_L12": "c_A",
          "shift_from_AB3": "difference in c_A",
          "v_over_kTc_L12": "dimensionless",
          "v_over_kTc_L10": "dimensionless",
          "entropy_jump_L12_at_0_25": "units of R",
          "energy_jump_L12_at_0_25": "units of N v",
          "entropy_jump_L10_at_0_5": "units of R",
          "energy_jump_L10_at_0_5": "units of N v"
        }
      },
      "description": "Aggregate transition properties computed from the cluster‑variation solutions. Each numeric key is compared to a hidden gold value with absolute or relative tolerance."
    },
    {
      "file": "heat_capacity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition_c_A",
          "reduced_temperature_t",
          "C_v_per_Nk"
        ],
        "units": {
          "composition_c_A": "mole fraction (dimensionless)",
          "reduced_temperature_t": "k_B T / v (dimensionless)",
          "C_v_per_Nk": "units of k (dimensionless)"
        }
      },
      "description": "Configuration heat capacity per atom as functions of temperature for c_A=0.25 and 0.5. Checked against hidden gold curve points and a self‑consistency requirement: the integral of C_v/T over the transition region must match the submitted entropy jump."
    }
  ]
}
```