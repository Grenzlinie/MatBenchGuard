# DFT Investigation of M(IV) Chelates: Bond Lengths, Spin States, and Thermochemistry

## Problem background
Stabilizing transition metals in unusually high oxidation states within macrocyclic chelates is a fundamental challenge in coordination chemistry. This task studies four complexes where the metal is formally in the +4 oxidation state: [M(trans-di[benzo]porphyrazine)(F)₂] with M = Fe, Co, Ni, Cu. The objective is to determine the optimized molecular geometries, metal–ligand bond lengths, planarity indicators of the chelate rings, the ground-state spin multiplicities, and the standard formation thermodynamic parameters (enthalpy, entropy, Gibson energy) of these species. All quantities are produced by first-principles gas-phase DFT calculations.

## Approach
Molecular structures are built from the known ligand connectivity and the two fluoride anions. For each metal, gas-phase DFT calculations at the OPBE/TZVP level are performed with an open-source quantum chemistry package (e.g., ORCA). Geometry optimization is carried out for several plausible spin multiplicities, and harmonic vibrational frequencies are computed to confirm the stationary point and to derive thermodynamic corrections. The ground electronic state is identified by comparing total energies.

From the optimized geometries, the M–N and M–F bond lengths are extracted, as well as the individual N–M–N bond angles and N–N–N non-bond angles. The sums of bond angles in the MN₄ chelate site and in the six-membered chelate rings are also computed to assess planarity. The ground-state spin multiplicity is recorded. Using the electronic energy and vibrational frequency data, the standard formation enthalpy (ΔH°f,298), standard entropy (S°f,298), and standard Gibbs energy (ΔG°f,298) are computed.

To ensure consistent reporting of bond labels, adopt the following atom numbering: The four donor nitrogen atoms around the metal form an approximate square. Two opposite nitrogens have shorter M–N bonds and two opposite nitrogens have longer M–N bonds. Label the two short-bond nitrogens as N1 and N3, and the two long-bond nitrogens as N2 and N4, in a cyclic sequence N1–N2–N3–N4 that follows the macrocycle connectivity (i.e., N1 is connected via bridging atoms to N2, N2 to N3, N3 to N4, N4 back to N1). The two six-membered chelate rings are formed by the metal and two adjacent nitrogens: ring1 contains N1 and N4; ring2 contains N2 and N3. The MN₄ chelate site is the set of all four nitrogens.

The analysis is limited to the quantities listed; natural bond orbital (NBO) analysis is not required.

## Reproduction target
Produce the following four CSV files under /app/outputs:

- `step_01_bond_lengths.csv`: M–N and M–F bond lengths (in pm) for each metal
- `step_02_thermodynamics.csv`: standard formation enthalpy, Gibbs energy, and entropy
- `step_03_spin_states.csv`: ground-state spin multiplicity for each metal
- `step_04_planarity_checks.csv`: sums of bond angles in the MN₄ chelate site and in the six-membered chelate rings

The required schemas are provided in the workflow steps below. The values must be obtained from your own DFT calculations; reporting externally looked-up numbers is not acceptable.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Construct initial molecular models
- Role: process
- Action: Build the four molecular complexes [M(trans-di[benzo]porphyrazine)(F)2] (M = Fe, Co, Ni, Cu) using a molecular builder or by scripting approximate geometries based on the known ligand connectivity and standard bond lengths. Save coordinate files for each complex.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT geometry optimization and vibrational frequency analysis
- Role: process
- Action: For each complex, run gas-phase DFT calculations at the OPBE/TZVP level using ORCA. Perform geometry optimization and compute harmonic vibrational frequencies. Evaluate all plausible spin multiplicities to compare total energies and determine the ground electronic state. Save optimized coordinates and the ORCA output files.
- Evidence: `/app/outputs/dft_outputs.log`

### Step 3: Extract metal–ligand bond lengths
- Role: scored (load-bearing)
- Action: From the optimized geometries of the ground-state complexes, extract the M–N and M–F bond lengths. Write them to step_01_bond_lengths.csv.
- Output file: `/app/outputs/step_01_bond_lengths.csv`
- Format: csv
- Contract: CSV with columns: metal, bond, length. metal: Fe/Co/Ni/Cu. bond: M-N1, M-N2, M-N3, M-N4, M-F1, M-F2. length: float (pm). 24 rows total.
- Scoring: scored by hidden verifier

### Step 4: Extract planarity indicators (angle sums)
- Role: scored
- Action: From the optimized geometries, compute for each metal complex the sum of the N–M–N bond angles in the MN₄ chelate site, and the sum of bond angles in each of the two six-membered chelate rings (ring1 containing N1 and N4, ring2 containing N2 and N3). Write the three angle sums per metal to step_04_planarity_checks.csv.
- Output file: `/app/outputs/step_04_planarity_checks.csv`
- Format: csv
- Contract: CSV with columns: metal, site, sum_angles_deg. metal: Fe/Co/Ni/Cu. site: one of 'MN4', 'chelate_ring1', 'chelate_ring2'. sum_angles_deg: float (degrees). 12 rows total (3 per metal).
- Scoring: scored by hidden verifier

### Step 5: Determine ground-state spin multiplicities
- Role: scored
- Action: Identify the spin multiplicity of the lowest-energy electronic state for each complex. Write the results to step_03_spin_states.csv.
- Output file: `/app/outputs/step_03_spin_states.csv`
- Format: csv
- Contract: CSV with columns: metal, ground_state_multiplicity. metal: Fe/Co/Ni/Cu. multiplicity: integer (1=singlet,2=doublet,3=triplet,4=quartet). 4 rows.
- Scoring: scored by hidden verifier

### Step 6: Compute thermodynamic formation parameters
- Role: scored
- Action: Using the total electronic energy and vibrational frequency data from the DFT calculation, compute the standard enthalpy (ΔH°f,298), standard Gibbs energy (ΔG°f,298), and standard entropy (S°f,298) of formation for each complex. Write the results to step_02_thermodynamics.csv.
- Output file: `/app/outputs/step_02_thermodynamics.csv`
- Format: csv
- Contract: CSV with columns: metal, delta_H, delta_G, S. metal: Fe/Co/Ni/Cu. delta_H and delta_G in kJ/mol (float). S in J/mol·K (float). 4 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bond_lengths.csv`
- `/app/outputs/step_02_thermodynamics.csv`
- `/app/outputs/step_03_spin_states.csv`
- `/app/outputs/step_04_planarity_checks.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bond_lengths.csv
- path: `/app/outputs/step_01_bond_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Metal–nitrogen and metal–fluorine bond lengths for each complex.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `bond`, `length`
  - `units`:
    - `length`: pm

### step_02_thermodynamics.csv
- path: `/app/outputs/step_02_thermodynamics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Standard formation enthalpy, Gibbs energy, and entropy.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `delta_H`, `delta_G`, `S`
  - `units`:
    - `delta_H`: kJ/mol
    - `delta_G`: kJ/mol
    - `S`: J/(mol·K)

### step_03_spin_states.csv
- path: `/app/outputs/step_03_spin_states.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Ground-state spin multiplicities.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `ground_state_multiplicity`
  - `units`: object

### step_04_planarity_checks.csv
- path: `/app/outputs/step_04_planarity_checks.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sums of bond angles indicating planarity of chelate site and rings.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `site`, `sum_angles_deg`
  - `units`:
    - `sum_angles_deg`: deg

Notes: All scored outputs are compared to hidden reference values from the paper using appropriate tolerances. Spin multiplicities must match exactly; bond lengths and angle sums use interval tolerances; thermodynamic values use relative/absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bond_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "bond",
          "length"
        ],
        "units": {
          "length": "pm"
        }
      },
      "description": "Metal–nitrogen and metal–fluorine bond lengths for each complex."
    },
    {
      "file": "step_02_thermodynamics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "delta_H",
          "delta_G",
          "S"
        ],
        "units": {
          "delta_H": "kJ/mol",
          "delta_G": "kJ/mol",
          "S": "J/(mol·K)"
        }
      },
      "description": "Standard formation enthalpy, Gibbs energy, and entropy."
    },
    {
      "file": "step_03_spin_states.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "ground_state_multiplicity"
        ],
        "units": {}
      },
      "description": "Ground-state spin multiplicities."
    },
    {
      "file": "step_04_planarity_checks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "site",
          "sum_angles_deg"
        ],
        "units": {
          "sum_angles_deg": "deg"
        }
      },
      "description": "Sums of bond angles indicating planarity of chelate site and rings."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values from the paper using appropriate tolerances. Spin multiplicities must match exactly; bond lengths and angle sums use interval tolerances; thermodynamic values use relative/absolute tolerances."
}
```

## How you are scored
Each output file is scored independently by a hidden evaluation program. Bond lengths and thermodynamic parameters are compared against reference values within tolerances that account for the method's numerical precision. Spin multiplicities must match the reference exactly. Planarity angle sums are checked against ideal planar values and against reference results. The verifier also checks that your results display physically expected structural trends across the metal series. The scores from the four files are combined using a set of fixed weights to produce your final reward (a single number between 0 and 1). The reward depends on the accuracy of your DFT results, not merely on correct formatting.
