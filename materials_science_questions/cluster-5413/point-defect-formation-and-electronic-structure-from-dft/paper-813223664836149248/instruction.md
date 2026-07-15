# Point Defect Formation and Electronic Structure from DFT Calculations

## Problem background
SrZrO3 (SZO) is a perovskite oxide that has attracted attention as a candidate material for resistive random-access memory (RRAM). The switching mechanism in SZO is not fully understood, but oxygen vacancies are believed to play a central role by forming conductive filaments. This task uses first-principles calculations to investigate how oxygen vacancies affect the electronic properties of SZO. You will examine the structural and electronic properties of bulk SZO containing ordered and disordered oxygen vacancies, in order to understand how vacancy ordering influences conductivity.

## Approach
You will perform density functional theory (DFT) calculations within the GGA-PBE approximation using PAW pseudopotentials, as implemented in the open-source Quantum ESPRESSO suite. Starting from the experimentally known orthorhombic crystal structure (space group Pnma), you will relax the bulk unit cell, then construct a 2×2×1 supercell and introduce oxygen vacancies to create an ordered row (V_O-row). By computing total energies for different charge states (neutral and positive) and for an isolated O2 molecule, you will evaluate defect formation energies and determine the Fermi-level positions where different charge states are equally stable (charge-state transition levels). You will compute the band structure of the V_O-row model to assess its metallic character. Next, you will build a disordered configuration (disrupted-row-I) by moving one oxygen atom into the vacancy row, compute its total energies in the same charge states, and evaluate the energy differences relative to the ordered V_O-row configuration.

## Reproduction target
Compute and output the following four results, each as a JSON file under /app/outputs:
1. Relaxed lattice constants (a, b, c) and unit-cell volume of orthorhombic SrZrO3.
2. Charge-state transition levels ε(2+/1+) and ε(1+/0) for the V_O-row model.
3. Whether the V_O-row model exhibits metallic states (boolean) and its direct band gap.
4. Energy differences ΔE = E(disrupted-row) − E(V_O-row) for charge states q = 0, 1+, 2+.
All quantities must be derived from your DFT calculations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary PAW pseudopotentials (Sr, Zr, O, PBE-GGA): https://www.quantum-espresso.org/pseudopotentials/pslibrary
- Orthorhombic SrZrO3 initial crystal structure: COD 9009612

## Workflow steps

### Step 1: Prepare bulk SrZrO3 unit cell
- Role: process
- Action: Create input files for DFT geometry optimization of the 20-atom orthorhombic SrZrO3 conventional cell using the experimental lattice constants as the initial guess.
- Evidence: `/app/outputs/bulk_input.in`

### Step 2: Bulk geometry optimization
- Role: scored
- Action: Run DFT geometry optimization with Quantum ESPRESSO using PAW-PBE-GGA. Extract the relaxed lattice constants A, B, C and unit-cell volume V and write them to the output file.
- Output file: `/app/outputs/step_01_lattice_constants.json`
- Format: json
- Contract: {"A": float (Å), "B": float (Å), "C": float (Å), "V": float (Å³)}
- Scoring: scored by hidden verifier

### Step 3: Build supercell and V_O-row model
- Role: process
- Action: Generate a 2×2×1 supercell (80 atoms) from the relaxed unit cell. Remove oxygen atoms to create the ordered oxygen-vacancy-row model as described in the paper.
- Evidence: `/app/outputs/vo_row_structure.in`

### Step 4: Total energy calculations for V_O-row system
- Role: process
- Action: Perform static DFT total-energy calculations for the perfect supercell, the V_O-row supercell in charge states q=0, +1, +2, and an isolated O2 molecule. Use uniform background charge for charged defects.
- Evidence: `/app/outputs/total_energies.log`

### Step 5: Charge-state transition levels
- Role: scored (load-bearing)
- Action: Compute formation energies from the total energies (using the standard defect formation energy formula) and determine the Fermi-level positions where the formation energies of different charge states intersect. Output the transition levels ε(2+/1+) and ε(1+/0).
- Output file: `/app/outputs/step_02_transition_levels.json`
- Format: json
- Contract: {"transition_2_1": float (eV), "transition_1_0": float (eV)}
- Scoring: scored by hidden verifier

### Step 6: Band structure calculation for V_O-row
- Role: process
- Action: Compute the electronic band structure for the optimized V_O-row supercell (use appropriate charge state).
- Evidence: `/app/outputs/bands.gnu`

### Step 7: Metallic character check
- Role: scored (load-bearing)
- Action: Analyze the band structure to determine whether the Fermi level crosses bands (metallic) and the direct band gap. Output the result.
- Output file: `/app/outputs/step_03_metallic_check.json`
- Format: json
- Contract: {"has_metallic_states": boolean, "band_gap_eV": float or null}
- Scoring: scored by hidden verifier

### Step 8: Disrupted-row model construction and energy series
- Role: process
- Action: Build the disrupted-row-I model by displacing one oxygen atom into the vacancy row. Perform static DFT total-energy calculations for this model in charge states q=0, +1, +2.
- Evidence: `/app/outputs/disrupted_energies.log`

### Step 9: Energy differences between ordered and disrupted rows
- Role: scored (load-bearing)
- Action: For each charge state, compute ΔE = E(disrupted) - E(V_O-row) using the previously obtained total energies. Output the three values.
- Output file: `/app/outputs/step_04_energy_differences.json`
- Format: json
- Contract: {"q0": float (eV), "q1": float (eV), "q2": float (eV)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_constants.json`
- `/app/outputs/step_02_transition_levels.json`
- `/app/outputs/step_03_metallic_check.json`
- `/app/outputs/step_04_energy_differences.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_constants.json
- path: `/app/outputs/step_01_lattice_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters of orthorhombic SrZrO3 from DFT-PBE-GGA.
- schema:
  - `type`: object
  - `required`:
    - `A`: float
    - `B`: float
    - `C`: float
    - `V`: float
  - `units`:
    - `A`: Å
    - `B`: Å
    - `C`: Å
    - `V`: Å³

### step_02_transition_levels.json
- path: `/app/outputs/step_02_transition_levels.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Charge-state transition levels for the V_O-row model.
- schema:
  - `type`: object
  - `required`:
    - `transition_2_1`: float
    - `transition_1_0`: float
  - `units`:
    - `transition_2_1`: eV
    - `transition_1_0`: eV

### step_03_metallic_check.json
- path: `/app/outputs/step_03_metallic_check.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Metallic character assessment: whether the V_O-row model exhibits a metallic state and its band gap.
- schema:
  - `type`: object
  - `required`:
    - `has_metallic_states`: boolean
    - `band_gap_eV`: float or null
  - `units`:
    - `band_gap_eV`: eV

### step_04_energy_differences.json
- path: `/app/outputs/step_04_energy_differences.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Energy differences ΔE = E(disrupted-row) - E(V_O-row) for charge states q = 0, 1+, 2+.
- schema:
  - `type`: object
  - `required`:
    - `q0`: float
    - `q1`: float
    - `q2`: float
  - `units`:
    - `q0`: eV
    - `q1`: eV
    - `q2`: eV

Notes: All scored outputs are compared to paper-reported gold values with reasonable tolerances to account for differences in DFT implementation and convergence settings. The metallic check uses threshold_or_better: band_gap_eV must be below a small threshold and has_metallic_states must be true. For energy differences, the checker also verifies expected signs and relative ordering among charge states.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A": "float",
          "B": "float",
          "C": "float",
          "V": "float"
        },
        "units": {
          "A": "Å",
          "B": "Å",
          "C": "Å",
          "V": "Å³"
        }
      },
      "description": "Relaxed lattice parameters of orthorhombic SrZrO3 from DFT-PBE-GGA."
    },
    {
      "file": "step_02_transition_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_2_1": "float",
          "transition_1_0": "float"
        },
        "units": {
          "transition_2_1": "eV",
          "transition_1_0": "eV"
        }
      },
      "description": "Charge-state transition levels for the V_O-row model."
    },
    {
      "file": "step_03_metallic_check.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "has_metallic_states": "boolean",
          "band_gap_eV": "float or null"
        },
        "units": {
          "band_gap_eV": "eV"
        }
      },
      "description": "Metallic character assessment: whether the V_O-row model exhibits a metallic state and its band gap."
    },
    {
      "file": "step_04_energy_differences.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "q0": "float",
          "q1": "float",
          "q2": "float"
        },
        "units": {
          "q0": "eV",
          "q1": "eV",
          "q2": "eV"
        }
      },
      "description": "Energy differences ΔE = E(disrupted-row) - E(V_O-row) for charge states q = 0, 1+, 2+."
    }
  ],
  "notes": "All scored outputs are compared to paper-reported gold values with reasonable tolerances to account for differences in DFT implementation and convergence settings. The metallic check uses threshold_or_better: band_gap_eV must be below a small threshold and has_metallic_states must be true. For energy differences, the checker also verifies expected signs and relative ordering among charge states."
}
```

## How you are scored
A hidden verifier will read each your output files, compare the computed quantities against reference benchmarks that characterize a correct computational reproduction, and combine the individual stage scores into a final reward (0–1). Performing the full DFT workflow and writing accurate artifacts is required; simply reporting expected numbers without running the calculations will not yield a passing score.
