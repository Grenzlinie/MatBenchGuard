# Computing geometric parameters of [H3O+·18-crown-6][Br3-] from published crystallographic data

## Problem background
The compound [H3O+·18‑crown‑6][Br3−] crystallizes in space group P‑1. Its crystal structure was solved from single‑crystal X‑ray diffraction and the atomic positions were refined. The cation contains an oxonium ion (H3O+) hydrogen‑bonded inside an 18‑crown‑6 ether ring, and the anion is a tribromide ion (Br3−). Key geometric features of interest are the Br–Br bond length in the anion, the planarity of the oxonium ion relative to the crown ether oxygen plane, and the O···O hydrogen‑bond distances. From the published fractional coordinates and unit cell parameters, these geometric quantities can be computed directly.

## Approach
Convert the fractional atomic coordinates to Cartesian coordinates using the metric tensor derived from the unit cell parameters (a, b, c, α, β, γ). The tribromide ion is centrosymmetric: Br(1) sits on an inversion center, so only one unique Br–Br distance exists, which is computed as the Euclidean distance between Br(1) and Br(2). The crown ether contains six oxygen atoms (O(1), O(2), O(3) and their inversion‑related counterparts). Fit a least‑squares plane through these six oxygen positions and compute the perpendicular distance from the oxonium oxygen O(4) to that plane. Finally, compute the Euclidean distances from O(4) to each of the six crown oxygen atoms and identify the minimum and maximum values. The computations require no external libraries beyond standard numerical linear algebra.

## Reproduction target
Using the fractional coordinates and unit cell data provided for this task, produce a JSON file, geometry_report.json, containing the following four computed quantities:
- br_br_bond_length_angstrom: the Br(1)–Br(2) bond length in angstroms.
- oxonium_out_of_plane_displacement_angstrom: the absolute perpendicular distance of O(4) to the mean plane through the six crown ether oxygen atoms, in angstroms.
- o_ox_crown_min_dist_angstrom: the minimum O(4)···O(crown) distance among the six contacts.
- o_ox_crown_max_dist_angstrom: the maximum O(4)···O(crown) distance among the six contacts.
The output must conform to the schema described in the output contract.

## Assets

- Python 3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute crystal geometry parameters
- Role: scored (load-bearing)
- Action: Using the fractional atomic coordinates and unit cell parameters provided in the instruction, compute (1) the Br–Br bond length in the centrosymmetric Br3− anion, (2) the perpendicular displacement of the oxonium oxygen from the mean plane of the six crown ether oxygen atoms, and (3) the minimum and maximum distances from the oxonium oxygen to the six crown oxygen atoms. Write the results to geometry_report.json.
- Output file: `/app/outputs/geometry_report.json`
- Format: json
- Contract: {"br_br_bond_length_angstrom": <float>, "oxonium_out_of_plane_displacement_angstrom": <float>, "o_ox_crown_min_dist_angstrom": <float>, "o_ox_crown_max_dist_angstrom": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_report.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_report.json
- path: `/app/outputs/geometry_report.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed geometric parameters: Br-Br bond length, oxonium out-of-plane displacement, and O(oxonium)···O(crown) min/max distances.
- schema:
  - `type`: object
  - `required`:
    - `br_br_bond_length_angstrom`: float
    - `oxonium_out_of_plane_displacement_angstrom`: float
    - `o_ox_crown_min_dist_angstrom`: float
    - `o_ox_crown_max_dist_angstrom`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "br_br_bond_length_angstrom": "float",
          "oxonium_out_of_plane_displacement_angstrom": "float",
          "o_ox_crown_min_dist_angstrom": "float",
          "o_ox_crown_max_dist_angstrom": "float"
        }
      },
      "description": "Computed geometric parameters: Br-Br bond length, oxonium out-of-plane displacement, and O(oxonium)···O(crown) min/max distances."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently recompute the same four quantities from the same input crystallographic data using a different implementation. It will compare your submitted values to reference values with predefined tolerances. Your final reward is a weighted combination (total 1.0) based on how many of the quantities fall within their respective tolerances. Note that simply copying the expected numbers from the paper is not sufficient; you must perform the geometric calculation to receive credit.
