# Spin Frustration and Ground-State Mapping in [Mn4O2]8+ Complexes

## Problem background
The system consists of a [Mn4O2]8+ core with four Mn(III) ions (S=2 each) arranged in a "butterfly" topology. Magnetic exchange is modeled by a Heisenberg spin Hamiltonian with two coupling constants: J_wb for the four wing-body interactions and J_bb for the body-body interaction. Because the interactions are competing and antiferromagnetic, the ground-state spin quantum numbers (total S_T, and the intermediate sums S_A and S_B) are not predetermined but depend on the relative strengths of J_wb and J_bb. The task is to compute these quantum numbers for a specific complex (Complex 1) and to map how the ground state changes as the exchange couplings are varied, revealing the phase boundaries produced by spin frustration.

## Approach
The approach uses the Kambe vector-coupling method to convert the Heisenberg Hamiltonian into an operator-equivalent eigenvalue expression. For the butterfly core (four S=2 ions), the energy of a state labeled by the coupled spins (S_A = S1+S3, S_B = S2+S4, S_T = S_A+S_B) is E = -J_wb [S_T(S_T+1) - S_A(S_A+1) - S_B(S_B+1)] - J_bb S_A(S_A+1). For the isosceles Mn3O triangle of three S=2 ions, the analogous expression is E = -J [S_T(S_T+1) - S_bc(S_bc+1)] - J* S_bc(S_bc+1), where S_bc = S_b+S_c. All possible spin states are enumerated by the rules of angular momentum addition; the ground state for a given coupling set is the state with the lowest energy. By implementing these energy formulas and scanning the coupling parameter spaces (J/J* ratio for the triangle, J_wb and J_bb for the butterfly), one obtains the ground-state quantum numbers and their dependence on the exchange strengths. The required outputs—ground state of Complex 1, triangle scan, and tetranuclear scan—are computed through direct diagonalisation of these small discrete state spaces.

## Reproduction target
Produce three scored artifacts under /app/outputs:

1) ground_state_complex1.json: The ground-state spin quantum numbers (S_T, S_A, S_B) for Complex 1 using J_wb = -5.3 cm⁻¹ and J_bb = -24.6 cm⁻¹.
2) triangle_ground_states.csv: For the isosceles Mn3O triangle, scan J/J* (both negative) from 0.01 to approximately 10, and for each ratio record the ground-state S_T, S_bc, and energy.
3) tetranuclear_ground_states.csv: For the Mn4O2 butterfly core, scan J_wb and J_bb over a grid of negative values and record the ground-state (S_T, S_A, S_B) for each (J_wb, J_bb) pair.

All files must follow the output contract schemas listed below.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ground state of complex 1
- Role: scored
- Action: Using the butterfly Hamiltonian energy expression E = -J_wb [S_T(S_T+1) - S_A(S_A+1) - S_B(S_B+1)] - J_bb S_A(S_A+1) (see Approach), enumerate all spin states (S_A, S_B, S_T) for S=2 per Mn(III) and evaluate energies with J_wb = -5.3 cm⁻¹, J_bb = -24.6 cm⁻¹. Identify the lowest-energy state and report its quantum numbers (S_T, S_A, S_B).
- Output file: `/app/outputs/ground_state_complex1.json`
- Format: json
- Contract: {"S_T": int, "S_A": int, "S_B": int}
- Scoring: scored by hidden verifier

### Step 2: Scan J/J* for isosceles Mn3O triangle
- Role: scored
- Action: Implement the isosceles Mn3O triangle Hamiltonian energy expression E = -J [S_T(S_T+1) - S_bc(S_bc+1)] - J* S_bc(S_bc+1) (see Approach), with S_a=S_b=S_c=2. Scan the ratio J/J* (both negative) from 0.01 to ~10, and for each ratio compute all eigenstates, identify the ground state, and record the ratio, ground state S_T, S_bc, and its energy.
- Output file: `/app/outputs/triangle_ground_states.csv`
- Format: csv
- Contract: columns: ratio (float), S_T (int), S_bc (int), energy (float); units: energy in cm⁻¹
- Scoring: scored by hidden verifier

### Step 3: Scan J_wb and J_bb for Mn4O2 butterfly
- Role: scored (load-bearing)
- Action: Using the butterfly Hamiltonian energy expression E = -J_wb [S_T(S_T+1) - S_A(S_A+1) - S_B(S_B+1)] - J_bb S_A(S_A+1) (see Approach), scan J_wb and J_bb over a grid of negative values. For each (J_wb, J_bb) pair, compute the ground state (S_T, S_A, S_B) as the lowest-energy state and record the values.
- Output file: `/app/outputs/tetranuclear_ground_states.csv`
- Format: csv
- Contract: columns: J_wb (float), J_bb (float), S_T (int), S_A (int), S_B (int); units: J_wb, J_bb in cm⁻¹
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ground_state_complex1.json`
- `/app/outputs/triangle_ground_states.csv`
- `/app/outputs/tetranuclear_ground_states.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ground_state_complex1.json
- path: `/app/outputs/ground_state_complex1.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Ground state spin quantum numbers of complex 1 (J_wb=-5.3, J_bb=-24.6).
- schema:
  - `type`: object
  - `required`:
    - `S_T`: int
    - `S_A`: int
    - `S_B`: int

### triangle_ground_states.csv
- path: `/app/outputs/triangle_ground_states.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ground-state S_T, S_bc, and energy of the isosceles Mn3O triangle as a function of the ratio J/J* (both negative).
- schema:
  - `type`: table
  - `required_columns`: `ratio`, `S_T`, `S_bc`, `energy`
  - `units`:
    - `energy`: cm⁻¹

### tetranuclear_ground_states.csv
- path: `/app/outputs/tetranuclear_ground_states.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ground-state spin quantum numbers (S_T, S_A, S_B) of the Mn4O2 butterfly core as a function of the exchange coupling constants J_wb and J_bb (both negative).
- schema:
  - `type`: table
  - `required_columns`: `J_wb`, `J_bb`, `S_T`, `S_A`, `S_B`
  - `units`:
    - `J_wb`: cm⁻¹
    - `J_bb`: cm⁻¹

Notes: The task uses the exchange constants reported in the paper (J_wb=-5.3, J_bb=-24.6, S=2 for each Mn(III)). All required Hamiltonian expressions and coupling schemes are described in the instruction. The checker will verify the ground state of complex 1 by exact match, and the phase boundaries in the two scans by structural audit against known reference patterns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ground_state_complex1.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "S_T": "int",
          "S_A": "int",
          "S_B": "int"
        }
      },
      "description": "Ground state spin quantum numbers of complex 1 (J_wb=-5.3, J_bb=-24.6)."
    },
    {
      "file": "triangle_ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ratio",
          "S_T",
          "S_bc",
          "energy"
        ],
        "units": {
          "energy": "cm⁻¹"
        }
      },
      "description": "Ground-state S_T, S_bc, and energy of the isosceles Mn3O triangle as a function of the ratio J/J* (both negative)."
    },
    {
      "file": "tetranuclear_ground_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "J_wb",
          "J_bb",
          "S_T",
          "S_A",
          "S_B"
        ],
        "units": {
          "J_wb": "cm⁻¹",
          "J_bb": "cm⁻¹"
        }
      },
      "description": "Ground-state spin quantum numbers (S_T, S_A, S_B) of the Mn4O2 butterfly core as a function of the exchange coupling constants J_wb and J_bb (both negative)."
    }
  ],
  "notes": "The task uses the exchange constants reported in the paper (J_wb=-5.3, J_bb=-24.6, S=2 for each Mn(III)). All required Hamiltonian expressions and coupling schemes are described in the instruction. The checker will verify the ground state of complex 1 by exact match, and the phase boundaries in the two scans by structural audit against known reference patterns."
}
```

## How you are scored
Each of the three output files is independently evaluated by a hidden verifier.

- ground_state_complex1.json is scored by exact match: the reported (S_T, S_A, S_B) must be the correct ground state for the given couplings.
- triangle_ground_states.csv is scored by structural audit: the verifier inspects the sequence of (S_T, S_bc) vs. ratio to ensure that ground-state transitions occur in the correct order and at consistent ratio boundaries.
- tetranuclear_ground_states.csv is scored by structural audit: the verifier checks that the reported (S_T, S_A, S_B) values for sampled (J_wb, J_bb) pairs, including the point corresponding to Complex 1, respect the expected phase boundaries separating different ground-state regions.

The final reward is a weighted combination of the scores from these three stages. Simply inserting plausible numbers without executing the Hamiltonian diagonalization will not satisfy the verifier; the artifacts must be the product of the computation pipeline described in the workflow steps.
