# Magnetic phase diagram of multi-orbital Hubbard models

## Problem background
Ultracold fermionic atoms loaded into optical lattices can realize multi-orbital Hubbard physics. When the lowest and next-lowest energy bands are populated, the system is described by a two-band Hubbard model with intraorbital and interorbital interactions, Hund's coupling, and an orbital splitting between the bands. At half-filling, the interplay of the interaction strength (U), its sign, and the orbital splitting (D) can lead to a rich variety of ground states, including atomic-density-wave (ADW) order, antiferromagnetic (AF) order, superfluid and metallic phases. Understanding which ordered state is the true ground state for given U and D, and how the system transitions between them, is the central problem addressed here.

## Approach
We use two-site dynamical mean-field theory (DMFT) to solve the model. DMFT maps the lattice model onto a single impurity problem embedded in a self-consistently determined bath; the two-site variant uses a bath with one correlated site and one bath site per orbital, which captures the essential local quantum fluctuations and is capable of describing Mott and ordered states. To allow for spatially modulated orders, the bipartite lattice is divided into two sublattices, A and B. The local Green's function is obtained by solving two impurity problems per orbital and imposing self-consistency with a semicircular density of states of bandwidth W=4t (t is the hopping). From the converged solution one extracts the quasiparticle weight Z, the superfluid order parameter Φ, the sublattice occupations, and the total energy. For attractive U we consider the superfluid, Mott insulator, and ADW states; for repulsive U we consider the metallic, Mott insulator, and AF states. The ground state for each (U, D) is identified by comparing the energies of these candidate phases.

## Reproduction target
The goal is to compute the ground-state properties of the two-band Hubbard model at half-filling and determine the phase boundaries.

- **Attractive regime (U < 0)**: compute the atomic-density-wave order parameter M_ADW = (n_B – n_A)/4 and the quasiparticle weight Z for a range of negative U (from -6.0 to -0.5 in steps of 0.5) at exactly D = 0. Save the results as a CSV file.

- **Repulsive regime (U > 0)**: compute the antiferromagnetic staggered magnetization M_AF (the absolute difference of sublattice magnetizations) and Z for positive U (from 0.5 to 6.0 in steps of 0.5) at D = 0. Save the results as a CSV file.

- **Critical orbital splitting for phase transitions**: for U = -2.5, calculate the energies of the ADW and superfluid phases as functions of D and locate the D where the ADW energy crosses the superfluid energy; record this value as D_c_attractive. For U = 2.0, repeat the comparison between the AF and metallic phases to find D_c_repulsive. Write both critical values to a text file.

## Assets

- Python 3.x: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement DMFT solver for the two-band Hubbard model
- Role: process
- Action: Develop a Python code implementing the two-site dynamical mean-field theory for the two-band Hubbard model on a bipartite lattice. The solver must be able to run both homogeneous (no sublattice division) and sublattice-resolved modes, self-consistently computing the quasiparticle weight Z, superfluid order parameter Φ, sublattice occupations, and energy for given interaction U and orbital splitting D. The code should handle the superfluid, metallic, Mott insulating, ADW, and AF phases as needed. Save the solver code as an evidence file.
- Evidence: `/app/outputs/dmft_solver.py`

### Step 2: Compute ADW order parameter for attractive U at D=0
- Role: scored
- Action: Using the sublattice-resolved DMFT solver, compute the atomic-density-wave order parameter M_ADW = (n_B - n_A)/4 and the quasiparticle weight Z for U values from -6.0 to -0.5 in steps of 0.5, at fixed orbital splitting D=0. For each U, record the converged M_ADW and Z.
- Output file: `/app/outputs/adw_order_parameter.csv`
- Format: csv
- Contract: Columns: U (float, negative values), M_ADW (float, ADW order parameter), Z (float, quasiparticle weight). One row per U value.
- Scoring: scored by hidden verifier

### Step 3: Compute AF order parameter for repulsive U at D=0
- Role: scored
- Action: Using the sublattice-resolved DMFT solver, compute the antiferromagnetic staggered magnetization M_AF (defined as the absolute value of the difference between sublattice magnetizations) and quasiparticle weight Z for U values from 0.5 to 6.0 in steps of 0.5, at D=0. Record each result in a CSV.
- Output file: `/app/outputs/af_order_parameter.csv`
- Format: csv
- Contract: Columns: U (float, positive values), M_AF (float, AF order parameter), Z (float, quasiparticle weight). One row per U value.
- Scoring: scored by hidden verifier

### Step 4: Determine critical orbital splitting D_c for phase transitions
- Role: scored (load-bearing)
- Action: For U = -2.5, compute the ground-state energies of the ADW and superfluid phases as functions of D using the appropriate DMFT solvers. Locate the orbital splitting D where the ADW energy equals the superfluid energy; record this as D_c_attractive. For U = 2.0, repeat using the AF and metallic phases to find D_c_repulsive. Write both values to a text file.
- Output file: `/app/outputs/phase_transition_D.txt`
- Format: txt
- Contract: Two lines: 'D_c_attractive = <float>' and 'D_c_repressive = <float>', where D_c_attractive is for U=-2.5 and D_c_repressive for U=2.0.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adw_order_parameter.csv`
- `/app/outputs/af_order_parameter.csv`
- `/app/outputs/phase_transition_D.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adw_order_parameter.csv
- path: `/app/outputs/adw_order_parameter.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: ADW order parameter M_ADW and quasiparticle weight Z as functions of attractive interaction U at D=0.
- schema:
  - `type`: table
  - `required_columns`: `U`, `M_ADW`, `Z`
  - `units`:
    - `U`: in units of hopping t
    - `M_ADW`: dimensionless
    - `Z`: dimensionless

### af_order_parameter.csv
- path: `/app/outputs/af_order_parameter.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: AF order parameter M_AF and quasiparticle weight Z as functions of repulsive interaction U at D=0.
- schema:
  - `type`: table
  - `required_columns`: `U`, `M_AF`, `Z`
  - `units`:
    - `U`: in units of hopping t
    - `M_AF`: dimensionless
    - `Z`: dimensionless

### phase_transition_D.txt
- path: `/app/outputs/phase_transition_D.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical orbital splitting D_c for the ADW-superfluid transition at U=-2.5 and the AF-metallic transition at U=2.0.
- schema:
  - `type`: text
  - `pattern`: Two lines with format: 'D_c_attractive = <float>' and 'D_c_repressive = <float>'.
  - `units`: in units of hopping t

Notes: The checker will compare the values in adw_order_parameter.csv and af_order_parameter.csv against hidden reference data points with appropriate tolerance for each U. The quasiparticle weight Z should be close to 1.0 in the ordered phases. For phase_transition_D.txt, the two critical D values will be checked against the paper's reported values within a tolerance. No gold values are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adw_order_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "M_ADW",
          "Z"
        ],
        "units": {
          "U": "in units of hopping t",
          "M_ADW": "dimensionless",
          "Z": "dimensionless"
        }
      },
      "description": "ADW order parameter M_ADW and quasiparticle weight Z as functions of attractive interaction U at D=0."
    },
    {
      "file": "af_order_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U",
          "M_AF",
          "Z"
        ],
        "units": {
          "U": "in units of hopping t",
          "M_AF": "dimensionless",
          "Z": "dimensionless"
        }
      },
      "description": "AF order parameter M_AF and quasiparticle weight Z as functions of repulsive interaction U at D=0."
    },
    {
      "file": "phase_transition_D.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "pattern": "Two lines with format: 'D_c_attractive = <float>' and 'D_c_repressive = <float>'.",
        "units": "in units of hopping t"
      },
      "description": "Critical orbital splitting D_c for the ADW-superfluid transition at U=-2.5 and the AF-metallic transition at U=2.0."
    }
  ],
  "notes": "The checker will compare the values in adw_order_parameter.csv and af_order_parameter.csv against hidden reference data points with appropriate tolerance for each U. The quasiparticle weight Z should be close to 1.0 in the ordered phases. For phase_transition_D.txt, the two critical D values will be checked against the paper's reported values within a tolerance. No gold values are revealed here."
}
```

## How you are scored
A hidden automated verifier independently checks each of your scored output artifacts.

- For the ADW and AF CSV files, the verifier compares your computed order parameters M_ADW and M_AF for every U value against a hidden reference; the quasiparticle weight Z is also checked. The comparison uses an appropriate tolerance, and partial credit is awarded per U point.

- For the phase transition text file, the verifier compares your D_c_attractive and D_c_repulsive to a hidden reference, again within a tolerance.

The scores from all scored stages are combined using a weighted sum to produce the final reward. Simply reporting a number is not sufficient; you must generate the output files by genuinely executing the DMFT solver on the prescribed model and parameters.
