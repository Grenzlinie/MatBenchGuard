# Potential Energy Minimization of a Benzene Crystal Fragment

## Problem background
In earlier work, potential-energy minimization using an exp‑6‑1 non‑bonded atom–atom potential identified two stable 13‑molecule benzene clusters (tridecamers) with distinct conformations. Independently, a 13‑molecule fragment was taken from the crystal structure of orthorhombic benzene and compared to those clusters without relaxation. The key open question is: if that crystal fragment is allowed to relax under the same potential, will its conformation become identical to one of the known tridecamer clusters? Answering this would clarify which cluster conformation might be relevant for crystallization and whether small clusters can be directly compared to unrelaxed crystal fragments.

## Approach
The approach is a computational energy-minimization experiment. Extract the initial coordinates of the 13‑molecule fragment from the orthorhombic benzene crystal structure. Collect the exp‑6‑1 non‑bonded potential parameters, atomic charges, and molecular geometry from the published source. Implement a steepest‑descent minimization algorithm with Newton–Raphson step estimation, using numerically evaluated second derivatives. Allow all 78 molecular coordinates (translations and rotations of each rigid molecule) to vary simultaneously. Run the minimization multiple times starting from the unperturbed fragment as well as from configurations with small and large random perturbations to verify that the final stationary point is independent of the starting configuration. Finally, compute the total potential energy of the relaxed fragment and compare this energy with the energies of the known stable tridecamer clusters. The minimized geometry is saved as an XYZ file; the minimized energy is written as a plain‑text number.

## Reproduction target
Re‑implement the energy minimization of the 13‑molecule crystal fragment derived from the orthorhombic benzene crystal (Bacon, Curry & Wilson, 1964) using the exp‑6‑1 non‑bonded potential parameters of Williams (1980). Perform the minimization with all 78 molecular coordinates free, using steepest‑descent with Newton–Raphson step estimation and numerical second derivatives. Verify robustness by running the minimization from multiple perturbed starting points. Produce two scored artifacts: 
- `relaxed_fragment_coordinates.xyz` – the relaxed atomic coordinates of the 13‑molecule fragment in XYZ format (156 atoms).
- `minimized_energy.txt` – the final minimized potential energy in kJ mol⁻¹.
The overarching objective is to determine whether the resulting energy matches one of the previously reported stable tridecamer cluster energies, thereby assessing the conformational identity of the relaxed fragment relative to those clusters.

## Assets

- Orthorhombic benzene crystal structure (Bacon, Curry & Wilson, 1964): 10.1098/rspa.1964.0085
- Williams (1980) exp‑6‑1 potential parameters for benzene: 10.1107/S0567739480001611

## Workflow steps

### Step 1: Prepare initial fragment and potential parameters
- Role: process
- Action: Extract the coordinates of the 13‑molecule fragment from the orthorhombic benzene crystal structure of Bacon et al. (1964) and collect the exp‑6‑1 non‑bonded potential parameters, atomic charges, and molecular geometry from Williams (1980).
- Evidence: `/app/outputs/initial_fragment_structure.txt`

### Step 2: Minimize potential energy of the 13‑molecule crystal fragment
- Role: process
- Action: Minimize the potential energy of the 13‑molecule fragment using the exp‑6‑1 potential. Implement steepest‑descent minimization with Newton–Raphson step estimation and numerically evaluated second derivatives. Allow all 78 molecular coordinates to vary. Perform multiple runs with small and large perturbations of the initial configuration to verify robustness.
- Evidence: `/app/outputs/minimization.log`

### Step 3: Output relaxed fragment coordinates
- Role: scored
- Action: Write the relaxed atomic coordinates of the 13‑molecule fragment to an XYZ file: 13 benzene molecules, each with 12 atoms (C6H6), totalling 156 atoms. Format: first line number of atoms, second line comment, following lines element symbol and x, y, z in Ångströms.
- Output file: `/app/outputs/relaxed_fragment_coordinates.xyz`
- Format: txt
- Contract: XYZ file: first line = `156`; second line = a comment; then 156 lines each with `C` or `H` and three space-separated coordinates.
- Scoring: scored by hidden verifier

### Step 4: Output minimized potential energy
- Role: scored (load-bearing)
- Action: Write the minimized potential energy of the fragment, computed with the same exp‑6‑1 potential, as a single number in kJ mol⁻¹ to a plain text file.
- Output file: `/app/outputs/minimized_energy.txt`
- Format: txt
- Contract: Single line containing a real number, e.g., `-325.3`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_fragment_coordinates.xyz`
- `/app/outputs/minimized_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_fragment_coordinates.xyz
- path: `/app/outputs/relaxed_fragment_coordinates.xyz`
- format: txt
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed atomic coordinates of the 13‑molecule benzene fragment in XYZ format. The checker recomputes the total potential energy from this file.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

### minimized_energy.txt
- path: `/app/outputs/minimized_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Minimized potential energy of the fragment. The checker compares this value to the hidden gold energy of the iso‑tridecamer cluster within a tolerance.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: kJ mol⁻¹

Notes: The checker recomputes the energy from the XYZ file and also reads the self‑reported energy; both must match the reference. The scoring is weighted heavily on the energy match, with a minor structural sanity check on the coordinate file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_fragment_coordinates.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Relaxed atomic coordinates of the 13‑molecule benzene fragment in XYZ format. The checker recomputes the total potential energy from this file."
    },
    {
      "file": "minimized_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "kJ mol⁻¹"
        }
      },
      "description": "Minimized potential energy of the fragment. The checker compares this value to the hidden gold energy of the iso‑tridecamer cluster within a tolerance."
    }
  ],
  "notes": "The checker recomputes the energy from the XYZ file and also reads the self‑reported energy; both must match the reference. The scoring is weighted heavily on the energy match, with a minor structural sanity check on the coordinate file."
}
```

## How you are scored
A hidden verifier will independently recompute the total potential energy from your submitted `relaxed_fragment_coordinates.xyz` using the same exp‑6‑1 parameters. It compares this recomputed energy, as well as your reported value in `minimized_energy.txt`, against a hidden reference energy derived from one of the stable tridecamer clusters. The reward is the weighted sum of: (i) how closely the recomputed energy matches the reference, (ii) consistency between the self‑reported energy and the recomputed energy, and (iii) syntactic and structural validity of the XYZ file. The energy match from the coordinates carries the greatest weight; the file‑format checks are low‑weight sanity checks. The self‑reported energy alone is not sufficient – the verifier recomputes the value from the geometry to ensure the minimization was genuinely performed.
