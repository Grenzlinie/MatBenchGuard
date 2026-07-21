# Charge-dependent structural parameters of Si–P heterodimers on Si(001)

## Problem background
When a single phosphorus atom is incorporated into the Si(001) surface as a substitutional dopant, it forms an asymmetric Si–P heterodimer. In scanning tunneling microscopy (STM) experiments on n-type substrates, the filled-state appearance of this heterodimer changes with increasing negative sample bias, suggesting that the accumulated charge on the surface can localize on the Si dangling bond and alter the atomic structure. The two possible buckling configurations of the heterodimer, referred to as HD1 and HD2, differ in the orientation of the neighboring Si–Si dimers and may respond differently to added electrons. This task sets out to compute the charge-dependent structural parameters of the Si–P heterodimer in both configurations to establish whether and how each geometry changes when electrons are added or removed.

## Approach
The computation is performed using spin-polarised density functional theory (DFT) within a periodic slab model of the Si(001) surface. A 4×4 surface unit cell with four Si layers, hydrogen-terminated on the bottom, and ~10 Å of vacuum is used to isolate the heterodimer. The exchange-correlation functional is GGA-PW91, and Vanderbilt ultrasoft pseudopotentials describe the ion cores. Brillouin-zone integrations use four special k-points in the irreducible surface Brillouin zone.

The workflow considers three charge conditions relative to the neutral system: one electron removed (Nₑ−1), one electron added (Nₑ+1), and two electrons added (Nₑ+2). For the charged slabs, a uniform compensating background charge is included. Geometry optimisations are carried out for the HD1 configuration in states Nₑ−1, Nₑ, Nₑ+1, and Nₑ+2, and for the HD2 configuration in states Nₑ, Nₑ+1, and Nₑ+2. From each relaxed geometry, the heterodimer buckling angle (with the sign convention that positive means phosphorus is the up-atom) and bond length are extracted and reported in a CSV file. The procedure thus yields a set of structural parameters that capture the response of the two heterodimer configurations to progressive charging, enabling a comparison of their behaviour.

## Reproduction target
Produce the file `/app/outputs/structural_parameters.csv` containing the computed buckling angle (degrees) and bond length (Å) for every (configuration, charge_state) pair: HD1 at Nₑ−1, Nₑ, Nₑ+1, Nₑ+2 and HD2 at Nₑ, Nₑ+1, Nₑ+2. The buckling angle sign convention is positive when the phosphorus atom is the up-atom. The reported values must be derived from the DFT geometry optimisations described in the workflow steps; the submission must include all seven rows with the exact column header `configuration,charge_state,buckling_angle_deg,bond_length_A`. The verifier will check that the computed parameters are physically meaningful and that they reflect the charge-dependent behaviour expected for this system.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- GGA-PW91 Vanderbilt ultrasoft pseudopotentials for Si, P, H: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build Si(001) slab models for HD1 and HD2 configurations
- Role: process
- Action: Construct 4×4 surface unit cell slab models of Si(001) with 4 Si layers, hydrogen-terminated bottom, ~10 Å vacuum, containing a single substitutional P atom forming the Si–P heterodimer in the HD1 and HD2 buckling arrangements. Use the equilibrium Si bulk lattice constant to set cell dimensions and initial atomic coordinates.
- Evidence: `/app/outputs/initial_models.json`

### Step 2: DFT geometry optimizations for all configurations and charge states
- Role: process
- Action: Using the chosen DFT code, perform spin-polarized geometry optimizations with GGA-PW91 exchange-correlation and Vanderbilt ultrasoft pseudopotentials, using 4 k-points in the irreducible SBZ, on the slab models: HD1 in charge states Nₑ−1, Nₑ, Nₑ+1, Nₑ+2; HD2 in charge states Nₑ, Nₑ+1, Nₑ+2. For charged cells include a uniform background compensating charge. Save the optimized atomic coordinates for each case.
- Evidence: `/app/outputs/optimized_coordinates`

### Step 3: Extract structural parameters into scored CSV
- Role: scored (load-bearing)
- Action: From the optimized geometries, extract the heterodimer buckling angle (degrees, with sign convention: positive when P is the up-atom) and bond length (Å) for each (configuration, charge_state) pair, and write them to a CSV file.
- Output file: `/app/outputs/structural_parameters.csv`
- Format: csv
- Contract: CSV with header: configuration,charge_state,buckling_angle_deg,bond_length_A. Rows: HD1, Ne-1; HD1, Ne; HD1, Ne+1; HD1, Ne+2; HD2, Ne; HD2, Ne+1; HD2, Ne+2. All values are floats; angle in degrees, length in Å.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_parameters.csv
- path: `/app/outputs/structural_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed buckling angle and bond length of the Si–P heterodimer for each configuration (HD1/HD2) and charge state (Ne-1, Ne, Ne+1, Ne+2 for HD1; Ne, Ne+1, Ne+2 for HD2). The checker compares these values to hidden reference values within absolute tolerances and verifies that the HD1 angle decreases and bond length increases monotonically, while HD2 values show minimal variation.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `charge_state`, `buckling_angle_deg`, `bond_length_A`
  - `units`:
    - `buckling_angle_deg`: degrees
    - `bond_length_A`: angstroms

Notes: The agent must include all seven rows listed in the schema; missing rows score zero for that entry. The hidden reference values are taken from the source paper's Table III (Si–P data only).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "charge_state",
          "buckling_angle_deg",
          "bond_length_A"
        ],
        "units": {
          "buckling_angle_deg": "degrees",
          "bond_length_A": "angstroms"
        }
      },
      "description": "Computed buckling angle and bond length of the Si–P heterodimer for each configuration (HD1/HD2) and charge state (Ne-1, Ne, Ne+1, Ne+2 for HD1; Ne, Ne+1, Ne+2 for HD2). The checker compares these values to hidden reference values within absolute tolerances and verifies that the HD1 angle decreases and bond length increases monotonically, while HD2 values show minimal variation."
    }
  ],
  "notes": "The agent must include all seven rows listed in the schema; missing rows score zero for that entry. The hidden reference values are taken from the source paper's Table III (Si–P data only)."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/structural_parameters.csv` and independently scores the submission. It compares each row’s buckling angle and bond length to reference values that capture the physical behaviour of the system, using tolerances appropriate for the chosen DFT protocol. It also checks that the reported values exhibit the structural trends that follow from the charge accumulation mechanism. The verifier assigns a reward between 0 and 1 based on how closely your computed structural parameters agree with these checks and on the completeness of your submission. Reporting a number that is not supported by the required geometry optimisations will not earn full credit.
