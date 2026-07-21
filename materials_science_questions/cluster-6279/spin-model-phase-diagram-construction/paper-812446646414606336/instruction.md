# Real-Space RG Phase Diagram of Extended Ising Model with Two-Body Interactions

## Problem background
This task investigates the phase behavior of an extended Ising model on a square lattice with competing two-body interactions. The model is relevant to order-disorder transitions in adatom layers, where the coverage of occupied lattice sites is tuned by temperature and an effective chemical potential. The Hamiltonian includes a nearest-neighbor antiferromagnetic coupling (corresponding to repulsive interactions between adatoms) and an additional next-to-nearest-neighbor coupling that can be attractive. A key open question is to what extent the attractive next-to-nearest coupling broadens the ordered region in the temperature-coverage phase diagram.

## Approach
A real-space renormalization group (RG) transformation is used to map the phase boundaries. The RG groups 20 original spins into 4 cells arranged to preserve the relevant superlattice symmetries. By iterating the RG transformation and tracking the flow of coupling constants, one obtains critical temperatures and critical coverages. For the present study the three-body interaction is set to zero (J3=0) so that the effect of the next-to-nearest coupling J2' can be isolated.

You will implement this RG transformation and perform two main computational runs:
1. Compute the full temperature-coverage phase boundary for J2' = 0 and extract the maximum critical temperature T_c*.
2. At a fixed scaled temperature T = 0.8 T_c*, run the RG for a range of next-to-nearest coupling ratios (at least J2'/J2 = 0 and J2'/J2 = -0.5) to determine the critical coverage where the order-disorder transition occurs.

All interactions are expressed in units of the nearest-neighbor coupling |J2| (which is negative), and coverages are defined through the relation theta = 0.5 (1 - <sigma>). Critical boundaries are located by monitoring discontinuities in the RG flow or by tracking maxima in the susceptibility of the free energy.

## Reproduction target
Your objective is to produce two scored artifacts:
- `T_c_star.txt`: the maximum critical temperature T_c* (in units of kT/|J2|) extracted from the phase diagram of the model with J3=0 and J2'=0.
- `critical_coverages.csv`: a table listing, for at least two values of the next-to-nearest coupling ratio (0.0 and -0.5), the critical coverage at the fixed temperature T = 0.8 T_c*.

These quantities are computed entirely from the RG procedure described above. Together they provide a numerical characterization of how the next-to-nearest attraction influences the width of the ordered region.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: RG simulation for nearest-neighbor model (J2'=0)
- Role: process
- Action: Implement the 20-spin to 4-cell real-space RG transformation for the square-lattice extended Ising model with J3=0, J2<0 (antiferromagnetic), and J2'=0. Run the RG procedure to map the temperature-coverage phase boundary and locate the maximum critical temperature T_c*. Save the raw phase boundary data as evidence.
- Evidence: `/app/outputs/phase_boundary_J20.csv`

### Step 2: Extract maximum critical temperature T_c*
- Role: scored
- Action: From the computed phase diagram for J2'=0, identify the maximum critical temperature T_c* (in units of kT/|J2|) and write it to T_c_star.txt.
- Output file: `/app/outputs/T_c_star.txt`
- Format: txt
- Contract: A single floating-point number with two decimal places, representing T_c*.
- Scoring: scored by hidden verifier

### Step 3: RG sweep of next-to-nearest coupling at fixed temperature
- Role: process
- Action: Using the same RG transformation, compute the critical coverage at the fixed temperature T = 0.8 * T_c* (extracted from step 1) for at least the J2' values 0 and -0.5 J2. Determine the critical coverage where the order-disorder transition occurs. Save the raw sweep data as evidence.
- Evidence: `/app/outputs/sweep_raw_data.csv`

### Step 4: Report critical coverage vs next-to-nearest coupling
- Role: scored (load-bearing)
- Action: Compile the critical coverage results into a CSV file with columns J2prime_ratio and critical_coverage, containing at least the rows for J2'=0 and J2'=-0.5 J2.
- Output file: `/app/outputs/critical_coverages.csv`
- Format: csv
- Contract: CSV file with header row: J2prime_ratio, critical_coverage. Each row is a float pair. Must contain rows for 0.0 and -0.5.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/T_c_star.txt`
- `/app/outputs/critical_coverages.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### T_c_star.txt
- path: `/app/outputs/T_c_star.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Maximum critical temperature for the model with J2'=0.
- schema:
  - `type`: text
  - `description`: A single floating-point number with two decimal places representing the maximum critical temperature T_c* in units of kT/|J2|.

### critical_coverages.csv
- path: `/app/outputs/critical_coverages.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical coverage at T=0.8 T_c* for J2'=0 and J2'=-0.5 J2.
- schema:
  - `type`: table
  - `required_columns`: `J2prime_ratio`, `critical_coverage`
  - `units`:
    - `J2prime_ratio`: dimensionless ratio J2'/J2
    - `critical_coverage`: coverage fraction (θ)

Notes: The checker compares the submitted T_c* and critical coverage values to hidden gold from the paper with appropriate tolerances, and verifies that the broadening effect is small.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "T_c_star.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number with two decimal places representing the maximum critical temperature T_c* in units of kT/|J2|."
      },
      "description": "Maximum critical temperature for the model with J2'=0."
    },
    {
      "file": "critical_coverages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "J2prime_ratio",
          "critical_coverage"
        ],
        "units": {
          "J2prime_ratio": "dimensionless ratio J2'/J2",
          "critical_coverage": "coverage fraction (θ)"
        }
      },
      "description": "Critical coverage at T=0.8 T_c* for J2'=0 and J2'=-0.5 J2."
    }
  ],
  "notes": "The checker compares the submitted T_c* and critical coverage values to hidden gold from the paper with appropriate tolerances, and verifies that the broadening effect is small."
}
```

## How you are scored
A hidden verifier will independently read your submitted `T_c_star.txt` and `critical_coverages.csv`. It compares your reported T_c* and critical coverage values to hidden reference numbers using absolute tolerances that account for the numerical spread expected from a correct RG implementation. The verifier may also check that the relation between the two critical coverages is consistent with the underlying physics, without relying on whether a single absolute number matches. Each scored artifact contributes a weighted share to the final reward (total 1.0); shape and format checks carry only minimal weight. The reference values are never exposed to you, so you must genuinely implement the RG transformation and compute the results.
