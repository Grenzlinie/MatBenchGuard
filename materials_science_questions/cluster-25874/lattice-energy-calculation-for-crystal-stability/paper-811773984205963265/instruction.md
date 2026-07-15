# Lattice Energy Minimization for Phenothiazine and Phenoselenazine Polymorphs

## Problem background
Lattice-energy calculations with atom–atom potentials are widely used to test the ability of simple interatomic potential functions to reproduce experimentally known crystal structures. In this task we focus on phenothiazine and phenoselenazine, two heterocyclic compounds that crystallize in multiple polymorphic forms with different space groups. The goal is to assess whether a Buckingham potential with given parameters can predict the observed unit-cell dimensions, molecular packing, and relative stabilities of these polymorphs by performing lattice-energy minimizations starting from the experimental structures. The minimizations must converge to stable minima and produce structural parameters that can be compared with experiment, as well as agreement metrics that quantify how well the computed and experimental structures match.

## Approach
The calculation adopts an atom–atom potential approach. The total lattice energy is expressed as a sum over all intermolecular non-bonded atom pairs of a Buckingham function φ = –A/r⁶ + B exp(–Cr), using parameters for C, H, N, S, and Se interactions combined by geometric-mean mixing rules. Truncation errors in the van der Waals sums are controlled via the Ewald–Bertaut–Williams accelerated-convergence technique with a 6 Å interaction cutoff. The energy is minimized with respect to the unit-cell constants and the rigid-body molecular coordinates (three centre-of-mass translations and three Euler angles), respecting the symmetry constraints of each space group (P2₁, Pnma, and P2₁2₁2₁). Post-minimization, the agreement between the minimized and experimental structures is evaluated via the root-mean-square Cartesian coordinate deviation, the packing coefficient, and the second-derivative (Hessian) eigenvalues at the experimental geometry. The workflow proceeds in three stages: building hydrogen‑ated starting models from the published non‑hydrogen coordinates, running the lattice‑energy minimizations, and compiling the final structural and agreement metrics.

## Reproduction target
For each of the three experimentally observed crystal structures (phenothiazine P2₁, phenothiazine Pnma, phenoselenazine P2₁2₁2₁), perform a full lattice-energy minimization as described. Output a single JSON file (`minimization_results.json`) containing, for each structure, the compound name, space group, minimized cell constants (a, b, c, and β for the monoclinic form), cell volume, molecular centre‑of‑mass coordinates and Euler angles, the agreement factor φ, the packing coefficient K, the lattice energy E (in kJ mol⁻¹), and a boolean indicating whether all Hessian eigenvalues are positive. All quantities must result from the actual minimization; the experimental values supplied as starting points differ from the minimized values due to thermal contraction and force‑field relaxation, so reporting the experimental data will not satisfy the target.

## Assets

- Crystal structure of phenothiazine (P2₁) from Bell et al. (1968): https://doi.org/10.1039/C19680001656
- Crystal structure of phenothiazine (Pnma) from McDowell (1976): https://doi.org/10.1107/S0567740876002156
- Crystal structure of phenoselenazine (P2₁2₁2₁) from Villares et al. (1976): https://doi.org/10.1107/S0567740876002156
- Lattice energy minimization software (e.g., DMACRYS or custom implementation): https://www.chem.ox.ac.uk/dmacrys

## Workflow steps

### Step 1: Prepare starting structures with hydrogen atoms
- Role: process
- Action: Retrieve the published experimental crystal structures (non‑hydrogen coordinates) for phenothiazine P2₁, phenothiazine Pnma, and phenoselenazine P2₁2₁2₁ from the literature. Place hydrogen atoms using standard geometry to create complete atomic coordinate sets and cell parameters. Produce initial structural models ready for energy minimization.
- Evidence: `/app/outputs/starting_structures.txt`

### Step 2: Minimize lattice energy
- Role: process
- Action: For each of the three observed structures, perform lattice‑energy minimization using an atom–atom Buckingham potential with the parameters listed in the paper (Table 1) and the Ewald–Bertaut–Williams accelerated convergence technique with a 6 Å interaction cutoff. Minimize the total energy with respect to the unit‑cell constants and the rigid‑body molecular coordinates (three translations and three Euler angles, respecting space‑group constraints). Start from the experimental cell and coordinates from the previous step.
- Evidence: `/app/outputs/minimized_structures.txt`

### Step 3: Compute agreement metrics and final results
- Role: scored (load-bearing)
- Action: For each minimized structure, compute the agreement factor φ (using only the non‑hydrogen atom positions, as hydrogen atoms were added with standard geometry and are not part of the experimental reference), the packing coefficient K, the lattice energy E, and evaluate whether all eigenvalues of the Hessian at the experimental geometry are positive. Write a JSON file containing, for each structure, the compound name, space group, minimized cell constants, volume, molecular centre‑of‑mass coordinates and Euler angles, φ, K, E, and a boolean for Hessian positivity.
- Output file: `/app/outputs/minimization_results.json`
- Format: json
- Contract: JSON array of three objects, each containing keys: compound (string), space_group (string), cell (object with a, b, c numbers in Å, and optionally beta in °), volume_V (number, Å³), molecular_coordinates (object with x, y, z in Å, and theta, phi, psi in °), agreement_factor_phi (number), packing_coefficient_K (number), lattice_energy_E (number, kJ mol⁻¹), hessian_positive_eigenvalues (boolean).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/minimization_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### minimization_results.json
- path: `/app/outputs/minimization_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the minimized lattice energy, structural parameters, agreement factors (φ from non‑H atoms), packing coefficients, and Hessian eigenvalue test results for the three experimentally known crystal structures.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `compound`, `space_group`, `cell`, `volume_V`, `molecular_coordinates`, `agreement_factor_phi`, `packing_coefficient_K`, `lattice_energy_E`, `hessian_positive_eigenvalues`
    - `properties`:
      - `compound`:
        - `type`: string
      - `space_group`:
        - `type`: string
      - `cell`:
        - `type`: object
        - `required`: `a`, `b`, `c`
        - `properties`:
          - `a`:
            - `type`: number
            - `units`: Å
          - `b`:
            - `type`: number
            - `units`: Å
          - `c`:
            - `type`: number
            - `units`: Å
          - `beta`:
            - `type`: number
            - `units`: °
      - `volume_V`:
        - `type`: number
        - `units`: Å³
      - `molecular_coordinates`:
        - `type`: object
        - `required`: `x`, `y`, `z`, `theta`, `phi`, `psi`
        - `properties`:
          - `x`:
            - `type`: number
            - `units`: Å
          - `y`:
            - `type`: number
            - `units`: Å
          - `z`:
            - `type`: number
            - `units`: Å
          - `theta`:
            - `type`: number
            - `units`: °
          - `phi`:
            - `type`: number
            - `units`: °
          - `psi`:
            - `type`: number
            - `units`: °
      - `agreement_factor_phi`:
        - `type`: number
        - `description`: Computed from non‑hydrogen atom coordinates only
      - `packing_coefficient_K`:
        - `type`: number
      - `lattice_energy_E`:
        - `type`: number
        - `units`: kJ mol⁻¹
      - `hessian_positive_eigenvalues`:
        - `type`: boolean

Notes: The agreement factor φ must be computed using only the non‑hydrogen atom positions; hydrogen atoms are not part of the experimental reference and their inclusion would alter the value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "minimization_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "compound",
            "space_group",
            "cell",
            "volume_V",
            "molecular_coordinates",
            "agreement_factor_phi",
            "packing_coefficient_K",
            "lattice_energy_E",
            "hessian_positive_eigenvalues"
          ],
          "properties": {
            "compound": {
              "type": "string"
            },
            "space_group": {
              "type": "string"
            },
            "cell": {
              "type": "object",
              "required": [
                "a",
                "b",
                "c"
              ],
              "properties": {
                "a": {
                  "type": "number",
                  "units": "Å"
                },
                "b": {
                  "type": "number",
                  "units": "Å"
                },
                "c": {
                  "type": "number",
                  "units": "Å"
                },
                "beta": {
                  "type": "number",
                  "units": "°"
                }
              }
            },
            "volume_V": {
              "type": "number",
              "units": "Å³"
            },
            "molecular_coordinates": {
              "type": "object",
              "required": [
                "x",
                "y",
                "z",
                "theta",
                "phi",
                "psi"
              ],
              "properties": {
                "x": {
                  "type": "number",
                  "units": "Å"
                },
                "y": {
                  "type": "number",
                  "units": "Å"
                },
                "z": {
                  "type": "number",
                  "units": "Å"
                },
                "theta": {
                  "type": "number",
                  "units": "°"
                },
                "phi": {
                  "type": "number",
                  "units": "°"
                },
                "psi": {
                  "type": "number",
                  "units": "°"
                }
              }
            },
            "agreement_factor_phi": {
              "type": "number",
              "description": "Computed from non‑hydrogen atom coordinates only"
            },
            "packing_coefficient_K": {
              "type": "number"
            },
            "lattice_energy_E": {
              "type": "number",
              "units": "kJ mol⁻¹"
            },
            "hessian_positive_eigenvalues": {
              "type": "boolean"
            }
          }
        }
      },
      "description": "Scored artifact containing the minimized lattice energy, structural parameters, agreement factors (φ from non‑H atoms), packing coefficients, and Hessian eigenvalue test results for the three experimentally known crystal structures."
    }
  ],
  "notes": "The agreement factor φ must be computed using only the non‑hydrogen atom positions; hydrogen atoms are not part of the experimental reference and their inclusion would alter the value."
}
```

## How you are scored
A hidden verifier compares each submitted quantity against the expected values for a correct minimization. For each structure, the cell constants, molecular parameters, φ, K, E, and Hessian positivity are independently checked. The final reward is a weighted combination of the per-structure scores, with full credit awarded only if all three structures meet the required agreement. Note that simply echoing the experimental starting values or the paper's reference numbers without performing the minimization will fail, because the hidden reference corresponds to the minimized structures (which are systematically different from the experimental room‑temperature structures).
