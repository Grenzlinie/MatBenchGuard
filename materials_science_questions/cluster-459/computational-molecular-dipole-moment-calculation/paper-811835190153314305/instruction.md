# Hellmann-Feynman H2O R12 HFA Properties Reproduction

## Problem background
In standard quantum chemistry, computing molecular gradients and higher-order properties requires differentiating molecular integrals with respect to nuclear positions. An alternative is the Hellmann–Feynman approximation (HFA), where the atomic orbitals are treated as fixed in space at the reference geometry rather than following the nuclei. Forces then simplify to expectation values of the electric field operator at the nuclei, avoiding integral derivatives. However, the accuracy of this approximation depends strongly on the basis set and requires explicit enforcement of translational and rotational invariance. This task explores the HFA for the water molecule (H₂O) at the Hartree–Fock level using a specialised R12 basis set. The objective is to compute key molecular properties (gradient norm, optimised geometry, vibrational frequencies, and infrared intensities) using both the standard analytical approach and the Hellmann–Feynman approximation, and to evaluate how the HFA results compare with the standard ones.

## Approach
The core idea is to perform Hartree–Fock calculations on H₂O with a custom R12 basis set constructed from explicit exponents (provided below). Two parallel treatments of nuclear gradients are employed: (a) the standard analytical gradient, which includes the response of the moving basis functions, and (b) the Hellmann–Feynman gradient, computed as the sum of the expectation value of the electronic electric-field operator at each nucleus and the classical nuclear–nuclear repulsion gradient. Translational and rotational contamination in the HFA gradient is removed using the T⁺T projection formalism before geometry optimisation. The workflow consists of: building the R12 basis; a standard Hartree–Fock geometry optimisation using analytical gradients to obtain a reference minimum; evaluating the unprojected HFA gradient norm at that reference; a second optimisation that uses the projected HFA gradient as the driving force to find the consistent HFA‑geometry; numerical differentiation of the projected HFA gradient at both minima to obtain the molecular Hessian and dipole gradient (with projection after differentiation); and finally extraction of harmonic vibrational frequencies and double‑harmonic IR intensities from the mass‑weighted Hessian and dipole gradient. All quantities are computed for the Hartree–Fock/R12 level of theory, reflecting the paper’s benchmark of HFA convergence.

## Reproduction target
Your task is to produce the following quantities for the H₂O molecule at the Hartree–Fock level using the R12 basis set:
- the Euclidean norm of the unprojected Hellmann–Feynman gradient vector evaluated at the standard analytical Hartree–Fock minimum geometry;
- the O–H bond length and H–O–H bond angle obtained from a geometry optimisation that used the projected Hellmann–Feynman gradient as the force;
- the three harmonic vibrational frequencies (cm⁻¹) and three double‑harmonic infrared intensities (km mol⁻¹) computed from the HFA Hessian and dipole gradient at both (i) the analytical minimum and (ii) the HFA minimum.
These eight numerical values must be written exactly to the three JSON files specified in the workflow steps below: gradient_norm.json, hfa_geometry.json, and hfa_spectra.json. All calculations are to be performed from scratch using the provided R12 basis exponents; no pre‑computed numbers from the paper are given as input.

## Assets

- R12 basis set exponents: Provided in instruction; explicit exponents from Table 1 of the paper (tight and diffuse functions for H, O).
- Quantum chemistry package: Open-source package like PySCF; capable of Hartree-Fock, computing expectation values of electric field operator.
- H2O initial geometry: Standard equilibrium geometry (OH ≈ 0.96 Å, HOH ≈ 104.5°) can be used as starting guess.

## Workflow steps

### Step 1: Build R12 basis set
- Role: process
- Action: Construct the contracted basis set for H (7s5p4d) and O (13s8p6d5f) by combining the explicit tight and diffuse exponents provided in the instruction with the aug-cc-pV5Z angular functions available in the quantum chemistry package. Create a basis set file or object usable by the chosen code.
- Evidence: `/app/outputs/basis_set_constructed.txt`

### Step 2: Standard Hartree-Fock geometry optimization
- Role: process
- Action: Perform a Hartree-Fock geometry optimization of H2O using the analytical gradient (standard moving orbitals) with the constructed R12 basis. Start from a near-equilibrium geometry and converge to a minimum. Save the optimized Cartesian coordinates.
- Evidence: `/app/outputs/analytical_min.xyz`

### Step 3: Compute unprojected HFA gradient norm
- Role: scored
- Action: At the analytical minimum geometry, compute the Hellmann-Feynman gradient vector for each atom as the sum of the electronic electric field (expectation value of the electric field operator from the HF density) and the nuclear repulsion gradient. Do NOT project out translation/rotation. Output the Euclidean norm of this unprojected gradient vector.
- Output file: `/app/outputs/gradient_norm.json`
- Format: json
- Contract: {"hfa_gradient_norm_Eh_per_a0": float}
- Scoring: scored by hidden verifier

### Step 4: Geometry optimization with projected HFA gradient
- Role: process
- Action: Starting from the analytical minimum, perform a geometry optimization of H2O using the projected Hellmann-Feynman gradient as the force. At each step, compute the HFA gradient (electric field expectation + nuclear gradient), project out translational and rotational components using the T⁺T formalism, and use this projected gradient in a standard optimizer (e.g., BFGS in internal coordinates). Terminate when the projected gradient norm is sufficiently small. Save the final optimized coordinates.
- Evidence: `/app/outputs/hfa_min.xyz`

### Step 5: Extract HFA-optimized bond length and angle
- Role: scored
- Action: From the final coordinates of the HFA optimization, compute the O-H bond length and the H-O-H bond angle. Output them.
- Output file: `/app/outputs/hfa_geometry.json`
- Format: json
- Contract: {"r_OH_pm": float, "angle_HOH_deg": float}
- Scoring: scored by hidden verifier

### Step 6: Compute HFA Hessian and dipole gradient
- Role: process
- Action: At both geometries (analytical minimum from step 2, and HFA minimum from step 4), compute the molecular Hessian and dipole gradient within the HFA using numerical differentiation of the projected HFA gradient (finite displacements along internal coordinates) for the Hessian, and numerical differentiation of the energy or dipole moment with respect to nuclear displacements and an external electric field for the dipole gradient. Ensure translational and rotational invariance after differentiation.
- Evidence: `/app/outputs/hessian_matrices.npy`

### Step 7: Compute harmonic frequencies and IR intensities
- Role: scored (load-bearing)
- Action: From the mass-weighted Hessian at each geometry, compute the harmonic vibrational frequencies (eigenvalues). From the dipole gradient, compute the double-harmonic infrared intensities. Output both sets of three frequencies and three intensities in one JSON file.
- Output file: `/app/outputs/hfa_spectra.json`
- Format: json
- Contract: {"frequencies_analytical_min_cm_1": [float, float, float], "frequencies_hfa_min_cm_1": [float, float, float], "intensities_analytical_min_km_per_mol": [float, float, float], "intensities_hfa_min_km_per_mol": [float, float, float]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gradient_norm.json`
- `/app/outputs/hfa_geometry.json`
- `/app/outputs/hfa_spectra.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gradient_norm.json
- path: `/app/outputs/gradient_norm.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Euclidean norm of the unprojected Hellmann-Feynman gradient vector at the analytical Hartree-Fock minimum.
- schema:
  - `type`: object
  - `required`:
    - `hfa_gradient_norm_Eh_per_a0`:
      - `type`: number

### hfa_geometry.json
- path: `/app/outputs/hfa_geometry.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: OH bond length and HOH bond angle from the geometry optimized with the projected HFA gradient.
- schema:
  - `type`: object
  - `required`:
    - `r_OH_pm`:
      - `type`: number
    - `angle_HOH_deg`:
      - `type`: number

### hfa_spectra.json
- path: `/app/outputs/hfa_spectra.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Harmonic vibrational frequencies and double-harmonic IR intensities computed from the HFA Hessian and dipole gradient at both the analytical minimum and the HFA minimum.
- schema:
  - `type`: object
  - `required`:
    - `frequencies_analytical_min_cm_1`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `frequencies_hfa_min_cm_1`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `intensities_analytical_min_km_per_mol`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `intensities_hfa_min_km_per_mol`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3

Notes: Scored artifacts are compared against paper-reported values for the R12 basis (HF level) using tolerances defined in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gradient_norm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hfa_gradient_norm_Eh_per_a0": {
            "type": "number"
          }
        }
      },
      "description": "Euclidean norm of the unprojected Hellmann-Feynman gradient vector at the analytical Hartree-Fock minimum."
    },
    {
      "file": "hfa_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "r_OH_pm": {
            "type": "number"
          },
          "angle_HOH_deg": {
            "type": "number"
          }
        }
      },
      "description": "OH bond length and HOH bond angle from the geometry optimized with the projected HFA gradient."
    },
    {
      "file": "hfa_spectra.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "frequencies_analytical_min_cm_1": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "frequencies_hfa_min_cm_1": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "intensities_analytical_min_km_per_mol": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "intensities_hfa_min_km_per_mol": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          }
        }
      },
      "description": "Harmonic vibrational frequencies and double-harmonic IR intensities computed from the HFA Hessian and dipole gradient at both the analytical minimum and the HFA minimum."
    }
  ],
  "notes": "Scored artifacts are compared against paper-reported values for the R12 basis (HF level) using tolerances defined in the hidden grading specification."
}
```

## How you are scored
A hidden verifier inspects your three output files (gradient_norm.json, hfa_geometry.json, hfa_spectra.json) and compares your reported values against reference values obtained from the original study. Each stage’s artifact is scored using domain‑appropriate tolerances and contributes to a combined final reward between 0 and 1. Closer agreement yields a higher reward; simply quoting the published numbers without actually running the computations will not produce a passing result. The verifier does not reveal its reference values or tolerance thresholds, so you must obtain the quantities through genuine execution of the described workflow.
