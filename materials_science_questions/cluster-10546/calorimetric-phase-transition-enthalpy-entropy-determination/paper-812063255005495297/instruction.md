# Kikuchi Cluster-Variation Calculation of Order-Disorder Phase Diagram in f.c.c. Binary Alloys

## Problem background
Binary alloys with a face-centered cubic (f.c.c.) lattice that undergo an order-disorder transformation can form L1₂ (Cu₃Au-type) and L1₀ (CuAu-type) superstructures. Accurate phase diagrams and thermodynamic properties for such systems are essential for understanding alloy stability and guiding materials design. Simple mean-field theories predict only a single maximum in the order-disorder transition temperature, at the equiatomic composition, and systematically underestimate the degree of order near the critical temperature and the ordering energy itself. The Kikuchi cluster-variation method improves on these theories by treating tetrahedron cluster probabilities correctly, thereby capturing short-range order and yielding a more faithful picture of the order-disorder transition, including the first-order character and the possibility of multiple ordered-phase regions. Reproducing the complete phase diagram and the associated thermodynamic quantities—transition temperatures, ordering energies, entropy and energy jumps, and the configurational heat capacity—validates the theoretical methodology and provides reference predictions against which experimental observations can be compared. The present task is to recompute all of these quantities from first principles, using only the published cluster-variation formalism and open-source numerical tools.

## Approach
The core idea is to construct the configuration free energy of a binary A–B alloy on an f.c.c. lattice using the Kikuchi cluster-variation method with the tetrahedron as the basic cluster and nearest-neighbour interactions. The free energy per atom, expressed in terms of the probabilities of the various tetrahedron, pair and point configurations, is first written down. By imposing symmetry appropriate to the disordered state (all sublattice point probabilities equal to the composition) and to the two ordered superstructures L1₂ and L1₀ (distinct sublattice occupations consistent with each long-range order), the number of independent probability variables is reduced. Two-phase equilibrium between the ordered and disordered phases is defined by equality of chemical potentials, which leads to a system of nonlinear equations whose unknowns are the disordered-phase composition, the equilibrium reduced temperature t = k_B T / v (where v is the ordering energy), and the independent tetrahedron probabilities in both phases. Solving this system for a range of ordered-phase compositions maps out the phase boundaries. Once the phase boundaries are known, the internal-equilibrium equations can be solved separately for the ordered phase at temperatures below the two-phase region and for the disordered phase above it, giving the temperature-dependent cluster probabilities. From these solutions one then computes the thermodynamic quantities of interest: the ordering energy–critical temperature relation, the entropy and energy discontinuities at the transition, and the configurational heat capacity obtained by numerical differentiation of the internal energy.

## Reproduction target
Produce the following scored outputs, all derived from your own implementation of the Kikuchi cluster-variation method:
1. **Phase diagram data** (phase_diagram.csv): for the L1₂ and L1₀ ordered phases, the lower and upper reduced order-disorder transition temperatures as functions of the ordered-phase composition c_A.
2. **Transition properties** (transition_properties.json): the maximum reduced transition temperatures for L1₂ and L1₀; the composition at the L1₂ maximum and its shift from the stoichiometric AB₃ composition; the ordering energy ratios v/(k_B T_c) for both superstructures; and the entropy and energy jumps at the transitions for c_A = 0.25 and c_A = 0.50.
3. **Configuration heat capacity** (heat_capacity_data.csv): for c_A = 0.25 and c_A = 0.50, the configurational heat capacity per atom (in units of k) as a function of reduced temperature.
These quantities are to be obtained by numerically solving the equilibrium and homogeneous-phase equations detailed in the workflow steps; they are not to be read from a pre‑computed table or the original paper.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Solve two‑phase equilibrium system
- Role: process
- Action: Implement the Kikuchi cluster‑variation free energy for an f.c.c. binary alloy with nearest‑neighbor interactions. Derive the two‑phase equilibrium conditions (equality of chemical potentials) and the internal equilibrium conditions for the disordered and ordered phases, expressed as a set of nonlinear equations in independent tetrahedron probabilities. Systematically prescribe the ordered‑phase composition c_A^(2) and solve the coupled system to obtain the equilibrium reduced temperature t_e and the coexisting disordered‑phase composition c_A^(1), together with the cluster probabilities at the phase boundaries.
- Evidence: `/app/outputs/equilibrium_solutions.csv`

### Step 2: Produce phase diagram data
- Role: scored (load-bearing)
- Action: From the equilibrium solutions, extract the phase boundaries: for each ordered‑phase composition record the type of ordered superstructure (L1₂ or L1₀), the composition, and the lower and upper reduced transition temperatures (T_c^(2) and T_c^(1)). Write the data to a CSV file.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: Header row: phase_type, composition_c_A, T_c_lower, T_c_upper. All values numeric; no missing entries.
- Scoring: scored by hidden verifier

### Step 3: Solve homogeneous‑phase equilibrium conditions
- Role: process
- Action: Using the equilibrium temperature and disordered‑phase composition obtained from the two‑phase solution, solve the internal‑equilibrium equations for the ordered phase at temperatures below the equilibrium temperature and for the disordered phase at temperatures above it, to obtain the temperature‑dependent cluster probabilities (tetrahedron, pair, and point probabilities).
- Evidence: `/app/outputs/homogeneous_solutions.csv`

### Step 4: Compute transition properties
- Role: scored (load-bearing)
- Action: From the equilibrium and homogeneous‑phase solutions, calculate: the maximum order‑disorder transition temperatures for the L1₂ and L1₀ superstructures, the composition at the L1₂ maximum and its shift from the stoichiometric AB₃ composition, the ordering energy ratios v/kT_c for both superstructures, and the entropy and energy jump magnitudes (ΔS and ΔE) at the transition for compositions c_A=0.25 and c_A=0.5. Write these values to a JSON file.
- Output file: `/app/outputs/transition_properties.json`
- Format: json
- Contract: JSON object with keys: max_Tc_L12, max_Tc_L10, composition_at_max_L12, shift_from_AB3, v_over_kTc_L12, v_over_kTc_L10, entropy_jump_L12_at_0_25, energy_jump_L12_at_0_25, entropy_jump_L10_at_0_5, energy_jump_L10_at_0_5. All values numeric.
- Scoring: scored by hidden verifier

### Step 5: Compute configuration heat capacity
- Role: scored
- Action: Using the temperature‑dependent internal energy from the homogeneous‑phase solutions, compute the configuration heat capacity C_v = dE/dT by numerical differentiation for the compositions c_A=0.25 and c_A=0.5. Write the data (composition, reduced temperature, C_v per atom in units of Boltzmann’s constant) to a CSV file.
- Output file: `/app/outputs/heat_capacity_data.csv`
- Format: csv
- Contract: CSV with columns: composition_c_A, reduced_temperature_t, C_v_per_Nk. All values numeric; no missing entries.
- Scoring: scored by hidden verifier

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
- description: Phase boundaries of L1₂ and L1₀ ordered phases: for each ordered‑phase composition the lower and upper reduced transition temperatures. Compared to hidden gold values within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `phase_type`, `composition_c_A`, `T_c_lower`, `T_c_upper`
  - `units`:
    - `composition_c_A`: mole fraction (dimensionless)
    - `T_c_lower`: k_B T / v (dimensionless)
    - `T_c_upper`: k_B T / v (dimensionless)

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
    - `max_Tc_L12`: k_B T / v
    - `max_Tc_L10`: k_B T / v
    - `composition_at_max_L12`: c_A
    - `shift_from_AB3`: difference in c_A
    - `v_over_kTc_L12`: dimensionless
    - `v_over_kTc_L10`: dimensionless
    - `entropy_jump_L12_at_0_25`: units of R
    - `energy_jump_L12_at_0_25`: units of N v
    - `entropy_jump_L10_at_0_5`: units of R
    - `energy_jump_L10_at_0_5`: units of N v

### heat_capacity_data.csv
- path: `/app/outputs/heat_capacity_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Configuration heat capacity per atom as functions of temperature for c_A=0.25 and 0.5. Checked against hidden gold curve points and a self‑consistency requirement: the integral of C_v/T over the transition region must match the submitted entropy jump.
- schema:
  - `type`: table
  - `required_columns`: `composition_c_A`, `reduced_temperature_t`, `C_v_per_Nk`
  - `units`:
    - `composition_c_A`: mole fraction (dimensionless)
    - `reduced_temperature_t`: k_B T / v (dimensionless)
    - `C_v_per_Nk`: units of k (dimensionless)

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
  ],
  "notes": "All scored outputs derive entirely from the agent's own implementation of the Kikuchi cluster‑variation formalism. No pre‑computed equilibrium data are supplied."
}
```

## How you are scored
A hidden verifier will independently score each of the three scored artifacts. For phase_diagram.csv, the reduced transition temperatures at a set of hidden compositions are compared against reference values with appropriate tolerances. For transition_properties.json, every numeric entry is checked against a hidden gold set. For heat_capacity_data.csv, the verifier performs a self-consistency test—the numerical integral of C_v (per atom) with respect to 1/T over the transition region must reproduce the entropy jump that you reported in transition_properties.json; it may also compare the heat‑capacity values at specific temperatures to hidden reference points. The three artifacts are weighted to produce a single final reward in [0,1]. Submitting paper-reported numbers without implementing the full cluster-variation computation will fail these checks and yield a low score. The verifier does not access the source paper and does not re-run your solver; it works only with the files you write to `/app/outputs`.
