# DFT study of oxygen-terminated chevron graphene nanoribbon magnetism

## Problem background
Atomically precise graphene nanoribbons show edge-dependent electronic and magnetic behavior. Chevron-type zigzag-edge nanoribbons (CZGNR) functionalized by oxygen atoms are predicted to exhibit tunable magnetic ground states and semiconducting gaps that depend on their width, length, and the kink angle between zigzag segments. Determining the ground-state magnetic configuration and the resulting electronic structure for a prototypical oxygen-terminated CZGNR is a key step toward designing carbon-based spintronic materials.

## Approach
Use first-principles spin-polarized density functional theory (DFT) with the generalized gradient approximation (GGA-PBE). Construct the atomic structure of the O-terminated chevron graphene nanoribbon ZO(3,6): two zigzag-edge segments of width 3 carbon chains, periodic length 6, 120° kink angle, all edge carbon atoms terminated by oxygen. Define five initial magnetic configurations: nonmagnetic (NM); ferromagnetic coupling on all edges (FM); antiferromagnetic ordering along each edge but AFM coupling between the two edges of the same segment (AFM-S); ferromagnetic coupling within each segment but AFM coupling between left and right segments (AFM-LR); and ferromagnetic ordering along each edge but AFM coupling between all neighboring edges (AFM-G). For each configuration, perform spin-polarized geometry optimization using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with standard pseudopotentials, relaxing atomic positions until forces fall below a prescribed threshold. Compare the final total energies to identify the magnetic ground state. For the lowest-energy state, compute the electronic band structure along a dense k‑path and extract the band gap; compute the spin-polarized charge density and the projected density of states onto p_x, p_y, p_z orbitals of an edge oxygen atom; and perform Bader charge analysis to obtain the absolute local magnetic moments on all oxygen atoms. Compile the ground-state configuration, band gap, minimum and maximum oxygen moment, and relative total energies (with NM set to zero) for all converged configurations into the single scored output file.

## Reproduction target
Determine the magnetic ground-state configuration of O-terminated ZO(3,6) from the five initial spin arrangements by comparing their relative total energies. Compute the band gap of the ground state (indirect if applicable) in meV. Compute the range of absolute local magnetic moments on oxygen atoms (in μ_B) via Bader analysis. Report the relative total energies (with NM=0) for all converged configurations. All results must be written to results.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary pseudopotentials for C and O: https://www.quantum-espresso.org/pseudopotentials/pslibrary
- Bader charge analysis code: http://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Construct ZO(3,6) CZGNR supercell and initial magnetic configurations
- Role: process
- Action: Build the atomic structure of O-terminated chevron graphene nanoribbon ZO(3,6): two zigzag-edge segments of width n=3 carbon chains, periodic length m=6, kink angle 120°, all edge atoms terminated by oxygen. Generate initial spin arrangements for the five magnetic configurations (NM, FM, AFM-S, AFM-LR, AFM-G) as defined in the methods. Output structure files suitable for Quantum ESPRESSO input.
- Evidence: none

### Step 2: Spin-polarized DFT geometry optimization and total energy calculation
- Role: process
- Action: For each of the five magnetic configurations, run spin-polarized DFT geometry relaxation using Quantum ESPRESSO with GGA-PBE functional, appropriate pseudopotentials, and plane-wave cutoff equivalent to 520 eV. Converge forces below 0.02 eV/Å. Record the final total energy for each configuration.
- Evidence: none

### Step 3: Identify ground state and compute key properties
- Role: scored (load-bearing)
- Action: Compare the total energies of the five configurations to determine the magnetic ground state. For the ground state, compute the electronic band structure along a dense k‑path and extract the band gap. Compute the projected density of states (PDOS) onto p_x, p_y, p_z orbitals for an edge oxygen atom. Perform Bader charge analysis on the ground‑state charge density to obtain local magnetic moments on all oxygen atoms. Assemble the results: ground‑state configuration label, band gap in meV, minimum and maximum absolute oxygen magnetic moment in μ_B, and relative total energies (with NM=0) for all converged configurations.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"ground_state_configuration": "<string, e.g. AFM-G>", "band_gap_meV": <float>, "oxygen_moment_min_muB": <float>, "oxygen_moment_max_muB": <float>, "relative_energies": {"NM": 0.0, "FM": null or <float>, "AFM-S": null or <float>, "AFM-LR": <float>, "AFM-G": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Hidden checker compares ground_state_configuration to the paper's ground state, band_gap_meV within a tolerance, oxygen moment min/max within tolerances, and verifies AFM-G energy is lowest among all computed configurations (excluding NM=0).
- schema:
  - `type`: object
  - `required`:
    - `ground_state_configuration`: string
    - `band_gap_meV`: float
    - `oxygen_moment_min_muB`: float
    - `oxygen_moment_max_muB`: float
    - `relative_energies`: object
  - `items`:
    - `relative_energies.NM`: 0.0 or missing
    - `relative_energies.FM`: null or float
    - `relative_energies.AFM-S`: null or float
    - `relative_energies.AFM-LR`: float
    - `relative_energies.AFM-G`: float
  - `units`:
    - `band_gap_meV`: meV
    - `oxygen_moment_min_muB`: μ_B
    - `oxygen_moment_max_muB`: μ_B

Notes: Only the ZO(3,6) structure is required. Configurations that did not converge may be represented by null in relative_energies. The checker will validate that AFM-G has the lowest total energy among the converged magnetic configurations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ground_state_configuration": "string",
          "band_gap_meV": "float",
          "oxygen_moment_min_muB": "float",
          "oxygen_moment_max_muB": "float",
          "relative_energies": "object"
        },
        "items": {
          "relative_energies.NM": "0.0 or missing",
          "relative_energies.FM": "null or float",
          "relative_energies.AFM-S": "null or float",
          "relative_energies.AFM-LR": "float",
          "relative_energies.AFM-G": "float"
        },
        "units": {
          "band_gap_meV": "meV",
          "oxygen_moment_min_muB": "μ_B",
          "oxygen_moment_max_muB": "μ_B"
        }
      },
      "description": "Hidden checker compares ground_state_configuration to the paper's ground state, band_gap_meV within a tolerance, oxygen moment min/max within tolerances, and verifies AFM-G energy is lowest among all computed configurations (excluding NM=0)."
    }
  ],
  "notes": "Only the ZO(3,6) structure is required. Configurations that did not converge may be represented by null in relative_energies. The checker will validate that AFM-G has the lowest total energy among the converged magnetic configurations."
}
```

## How you are scored
A hidden verifier reads results.json and evaluates the reported quantities against reference expectations using appropriate tolerances. It checks that the ground_state_configuration label matches the expected ordering, verifies that the band_gap_meV and oxygen_moment_min_muB / oxygen_moment_max_muB lie within allowed tolerance windows, and confirms that the relative_energies object shows the ground state has the lowest total energy among the converged magnetic configurations (excluding NM). The verifier assigns partial credit for each field; the combined score yields a reward between 0 and 1.
