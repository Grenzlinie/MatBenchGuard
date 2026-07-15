# Ground-State Energy and Elastic Stability of Cubic Metallic Hydrogen

## Problem background
Metallic hydrogen is expected to form under high pressure, and its ground-state crystal structure remains a fundamental open question. Reliable prediction of the phase diagram requires accurate computation of structure-dependent ground-state energies for candidate crystal lattices as a function of density. The present task focuses on cubic structures (simple cubic, face-centered cubic, body-centered cubic) of metallic hydrogen, using a perturbation-theory expansion up to third order. From these calculations one obtains energy contributions and elastic constants that determine mechanical stability and the pressure at which the fcc–sc Gibbs free energies cross, as well as an upper bound for the low-pressure phase via a volume-conserving tetragonal distortion of the simple cubic lattice.

## Approach
The ground-state energy is computed as an expansion in the Wigner–Seitz radius r_s using perturbation theory with the kinetic energy as the unperturbed Hamiltonian and the electron–ion and electron–electron Coulomb interactions as perturbations. For each cubic structure, compute the Madelung term from a reciprocal-lattice sum, the second‑order energy using the Lindhard-derived screening function χ(q), and three third‑order contributions—arising from different classes of Brueckner–Goldstone diagrams—that involve integrals over occupied electron states, including the double integral I(g1,g2) and the integral I(g) with proper treatment of the singularity at g=2. Elastic constants (shear moduli) are obtained from strain‑derivative expressions applied to each energy term under volume‑conserving distortions. The total energy is combined with the electron‑gas energy to construct the Gibbs free energy, from which the fcc–sc crossing pressure is determined. For the primitive tetragonal distortion of the sc lattice, the energy is minimized with respect to the distortion parameter at zero pressure to find an upper‑bound ground‑state energy.

## Reproduction target
Compute and output the following quantities:
1. Structure‑dependent energy components for sc, fcc, and bcc: Madelung term times αr_s, second‑order energy E2, and the three third‑order contributions divided by αr_s.
2. Elastic constant expansion coefficients A_i and B_i (i = M, 2, 3^(I), 3^(II), 3^(III)) for each cubic structure.
3. The crossing pressure P_c (in atomic units) at which the Gibbs free energies of fcc and sc become equal.
4. The minimized ground‑state energy per atom (in Rydberg) for the primitive tetragonal structure at zero pressure, obtained by optimizing the volume‑conserving tetragonal distortion parameter e3.
All results must be written to the required JSON files following the exact schema given in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute structure-dependent energy components
- Role: scored
- Action: Compute the Madelung coefficient, the second-order energy E2, and the three third-order contributions E3^I, E3^II, E3^III for the simple cubic (sc), face-centered cubic (fcc), and body-centered cubic (bcc) lattices. This involves summing over reciprocal lattice vectors, evaluating the Lindhard screening function χ(q), and numerically evaluating the integrals I(g1,g2) and I(g) as defined in the paper. Use appropriate methods to handle the singular behavior near g=2.
- Output file: `/app/outputs/structure_dependent_energy_components.json`
- Format: json
- Contract: Object with top-level keys 'sc', 'fcc', 'bcc'. Each value is an object with numeric fields: E_M_alpha_rs, E2, E3_I_over_alpha_rs, E3_II_over_alpha_rs, E3_III_over_alpha_rs.
- Scoring: scored by hidden verifier

### Step 2: Compute elastic constant expansion coefficients
- Role: scored
- Action: Using the previously computed Madelung, second-order, and third-order energy terms, derive the strain-derivative expressions to obtain the elastic constant expansion coefficients A_i and B_i for each cubic structure. Sum over reciprocal lattice vectors according to the perturbation-theory formulas.
- Output file: `/app/outputs/elastic_constant_coefficients.json`
- Format: json
- Contract: Object with top-level keys 'sc', 'fcc', 'bcc'. Each value is an object with numeric fields: A_M, A2, A3_I, A3_II, A3_III, B_M, B2, B3_I, B3_II, B3_III.
- Scoring: scored by hidden verifier

### Step 3: Determine fcc–sc Gibbs free energy crossing pressure
- Role: scored (load-bearing)
- Action: For sc and fcc, compute the total ground-state energy E(r_s) = E_eg(r_s) + E_st(r_s) using the structure-dependent components from the first step and the electron-gas energy formula. Convert to Gibbs free energy G(P) via the pressure relation and find the pressure P_c at which the free energies of fcc and sc cross.
- Output file: `/app/outputs/crossing_pressure.json`
- Format: json
- Contract: Object with a single numeric field: P_c_a_u (float, crossing pressure in a.u.).
- Scoring: scored by hidden verifier

### Step 4: Compute primitive tetragonal upper-bound ground-state energy
- Role: scored (load-bearing)
- Action: For the primitive tetragonal lattice derived from sc by a volume-conserving tetragonal distortion parametrized by e3, compute the ground-state energy as a function of e3 at zero pressure. Minimize with respect to e3 to obtain the upper-bound ground-state energy per atom.
- Output file: `/app/outputs/pt_ground_state_energy.json`
- Format: json
- Contract: Object with a single numeric field: E_pt_Ry (float, upper-bound energy in Ry per atom).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structure_dependent_energy_components.json`
- `/app/outputs/elastic_constant_coefficients.json`
- `/app/outputs/crossing_pressure.json`
- `/app/outputs/pt_ground_state_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structure_dependent_energy_components.json
- path: `/app/outputs/structure_dependent_energy_components.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Dimensionless energy components for the three cubic structures, compared to hidden gold values from the paper's Table I with a relative tolerance of 2%.
- schema:
  - `type`: object
  - `required`:
    - `sc`:
      - `E_M_alpha_rs`: float
      - `E2`: float
      - `E3_I_over_alpha_rs`: float
      - `E3_II_over_alpha_rs`: float
      - `E3_III_over_alpha_rs`: float
    - `fcc`:
      - `E_M_alpha_rs`: float
      - `E2`: float
      - `E3_I_over_alpha_rs`: float
      - `E3_II_over_alpha_rs`: float
      - `E3_III_over_alpha_rs`: float
    - `bcc`:
      - `E_M_alpha_rs`: float
      - `E2`: float
      - `E3_I_over_alpha_rs`: float
      - `E3_II_over_alpha_rs`: float
      - `E3_III_over_alpha_rs`: float

### elastic_constant_coefficients.json
- path: `/app/outputs/elastic_constant_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constant expansion coefficients for the three cubic structures, compared to hidden gold values from the paper's Table II with a relative tolerance of 2%.
- schema:
  - `type`: object
  - `required`:
    - `sc`:
      - `A_M`: float
      - `A2`: float
      - `A3_I`: float
      - `A3_II`: float
      - `A3_III`: float
      - `B_M`: float
      - `B2`: float
      - `B3_I`: float
      - `B3_II`: float
      - `B3_III`: float
    - `fcc`:
      - `A_M`: float
      - `A2`: float
      - `A3_I`: float
      - `A3_II`: float
      - `A3_III`: float
      - `B_M`: float
      - `B2`: float
      - `B3_I`: float
      - `B3_II`: float
      - `B3_III`: float
    - `bcc`:
      - `A_M`: float
      - `A2`: float
      - `A3_I`: float
      - `A3_II`: float
      - `A3_III`: float
      - `B_M`: float
      - `B2`: float
      - `B3_I`: float
      - `B3_II`: float
      - `B3_III`: float

### crossing_pressure.json
- path: `/app/outputs/crossing_pressure.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Crossing pressures: fcc–sc and pt–fcc in atomic units, compared to hidden gold values with an absolute tolerance of 0.01 a.u. each.
- schema:
  - `type`: object
  - `required`:
    - `P_c_a_u`: float
    - `P_c_pt_fcc_a_u`: float

### pt_ground_state_energy.json
- path: `/app/outputs/pt_ground_state_energy.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Upper-bound ground-state energy for the primitive tetragonal phase in Rydberg per atom; more negative is better. The hidden threshold is the paper's reported -1.103 Ry, with a tolerance that accepts any value ≤ -1.098 Ry.
- schema:
  - `type`: object
  - `required`:
    - `E_pt_Ry`: float

Notes: Merged pt–fcc crossing pressure into crossing_pressure.json to avoid an extra output file. All other entries preserved.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structure_dependent_energy_components.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "sc": {
            "E_M_alpha_rs": "float",
            "E2": "float",
            "E3_I_over_alpha_rs": "float",
            "E3_II_over_alpha_rs": "float",
            "E3_III_over_alpha_rs": "float"
          },
          "fcc": {
            "E_M_alpha_rs": "float",
            "E2": "float",
            "E3_I_over_alpha_rs": "float",
            "E3_II_over_alpha_rs": "float",
            "E3_III_over_alpha_rs": "float"
          },
          "bcc": {
            "E_M_alpha_rs": "float",
            "E2": "float",
            "E3_I_over_alpha_rs": "float",
            "E3_II_over_alpha_rs": "float",
            "E3_III_over_alpha_rs": "float"
          }
        }
      },
      "description": "Dimensionless energy components for the three cubic structures, compared to hidden gold values from the paper's Table I with a relative tolerance of 2%."
    },
    {
      "file": "elastic_constant_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "sc": {
            "A_M": "float",
            "A2": "float",
            "A3_I": "float",
            "A3_II": "float",
            "A3_III": "float",
            "B_M": "float",
            "B2": "float",
            "B3_I": "float",
            "B3_II": "float",
            "B3_III": "float"
          },
          "fcc": {
            "A_M": "float",
            "A2": "float",
            "A3_I": "float",
            "A3_II": "float",
            "A3_III": "float",
            "B_M": "float",
            "B2": "float",
            "B3_I": "float",
            "B3_II": "float",
            "B3_III": "float"
          },
          "bcc": {
            "A_M": "float",
            "A2": "float",
            "A3_I": "float",
            "A3_II": "float",
            "A3_III": "float",
            "B_M": "float",
            "B2": "float",
            "B3_I": "float",
            "B3_II": "float",
            "B3_III": "float"
          }
        }
      },
      "description": "Elastic constant expansion coefficients for the three cubic structures, compared to hidden gold values from the paper's Table II with a relative tolerance of 2%."
    },
    {
      "file": "crossing_pressure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "P_c_a_u": "float",
          "P_c_pt_fcc_a_u": "float"
        }
      },
      "description": "Crossing pressures: fcc–sc and pt–fcc in atomic units, compared to hidden gold values with an absolute tolerance of 0.01 a.u. each."
    },
    {
      "file": "pt_ground_state_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "E_pt_Ry": "float"
        }
      },
      "description": "Upper-bound ground-state energy for the primitive tetragonal phase in Rydberg per atom; more negative is better. The hidden threshold is the paper's reported -1.103 Ry, with a tolerance that accepts any value ≤ -1.098 Ry."
    }
  ],
  "notes": "Merged pt–fcc crossing pressure into crossing_pressure.json to avoid an extra output file. All other entries preserved."
}
```

## How you are scored
A hidden automated verifier inspects each output file independently. For the energy components and elastic constant coefficients, the verifier compares the submitted numeric values against reference values obtained from the same calculation, allowing a tolerance that accounts for numerical differences in integral evaluation and summation cutoffs. The crossing pressure and primitive tetragonal energy are similarly compared to reference values with appropriate absolute tolerances. The reward for each artifact is proportional to how close the computed values are to the references, combined across stages by weight into a single final score. All comparison thresholds and weights are hidden; your job is to implement the theory faithfully and report the results to high numerical accuracy.
