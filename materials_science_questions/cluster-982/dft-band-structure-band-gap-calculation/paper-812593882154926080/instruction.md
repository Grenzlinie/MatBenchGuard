# DFT Calculation of Mechanical and Electronic Properties of Pentadiamond

## Problem background
Pentadiamond is a hypothesized three-dimensional carbon allotrope composed of a pentagonal network of sp2 and sp3 carbon atoms. Theoretical investigations suggest it may be a metastable material with unusual mechanical properties—potentially high stiffness, a negative Poisson's ratio, and moduli surpassing diamond—as well as a semiconducting electronic character. Reproducing the density functional theory (DFT) calculations that predict these properties tests the robustness of the computational predictions. Unlike many carbon allotropes, the pentadiamond structure is fully defined by a cubic space group and fractional atomic coordinates, making it amenable to direct computational modeling.

## Approach
The properties are computed from first principles using DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and ultrasoft pseudopotentials, as implemented in the open-source Quantum ESPRESSO package. The workflow consists of four stages:

1. **Geometry optimization**: variable-cell relaxation of the lattice constant and atomic coordinates to obtain the equilibrium structure.
2. **Elastic stiffness constants**: finite differences of total energy under small strains along Voigt directions, yielding the three independent cubic elastic constants c11, c12, c44.
3. **Mechanical moduli and Poisson's ratio**: derivation of bulk modulus from the elastic constants, tensor inversion to obtain compliances, orientation averaging of Young's and shear moduli, and computation of Poisson's ratio from isotropic relations.
4. **Electronic band structure**: self-consistent field calculation followed by band structure calculation along a standard high-symmetry path for an fcc lattice, identification of the valence band maximum and conduction band minimum, and determination of the fundamental band gap (direct or indirect).

The calculations use publicly available structural parameters (space group Fm-3m, lattice constant ~9.195 Å, and fractional coordinates) and open-source tools; no empirical parameters are fitted.

## Reproduction target
Produce the following quantitative results for pentadiamond:

- **Elastic stiffness constants** (in GPa): c11, c12, c44 of the relaxed cubic structure.
- **Derived mechanical properties**: bulk modulus (GPa), orientation-averaged Young's modulus (GPa), averaged shear modulus (GPa), and Poisson's ratio (dimensionless).
- **Electronic band gap**: fundamental band gap value in eV, and the k-point labels of the valence band maximum (VBM) and conduction band minimum (CBM).

All steps are rigorous: the elastic constants must satisfy the Born stability criteria for cubic symmetry; the mechanical moduli are to be compared against known values for diamond and other ultra-hard carbons; the band gap type and location are to be determined from the band structure.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ultrasoft pseudopotential for carbon (PBE): https://www.quantum-espresso.org/pseudopotentials/ultra-soft/C.pbe-n-rrkjus_psl.0.1.UPF

## Workflow steps

### Step 1: Geometry optimization of pentadiamond
- Role: process
- Action: Perform variable-cell DFT geometry optimization of pentadiamond using the PBE functional and an ultrasoft pseudopotential (Quantum ESPRESSO). Start from the published cubic lattice constant and fractional coordinates given in the supplementary material. Relax lattice constant and internal coordinates until forces are converged. The resulting relaxed structure is required for all subsequent steps.
- Evidence: `/app/outputs/relaxation.out`

### Step 2: Compute elastic stiffness constants
- Role: scored (load-bearing)
- Action: Using the relaxed pentadiamond structure, apply small strains along appropriate Voigt directions. Perform static SCF DFT calculations for each strained configuration. Evaluate the second derivatives of total energy with respect to strain to obtain the three independent cubic elastic constants c11, c12, c44 (with cubic symmetry, c11=c22=c33, c12=c13=c23, c44=c55=c66). Report the constants in GPa.
- Output file: `/app/outputs/step_01_elastic_constants.json`
- Format: json
- Contract: {"c11": number, "c12": number, "c44": number}
- Scoring: scored by hidden verifier

### Step 3: Derive mechanical moduli and Poisson's ratio
- Role: scored
- Action: From the computed c11, c12, c44, calculate the bulk modulus B = (c11+2c12)/3. Compute the elastic compliances s11, s12, s44 via standard tensor inversion formulas for cubic symmetry. Evaluate the directional Young's modulus and shear modulus over a grid of Euler angles using the anisotropic formulas, then compute the orientation-averaged (averaged) Young's modulus and averaged shear modulus. Compute a representative isotropic Poisson's ratio from bulk modulus and averaged shear modulus. Output the bulk modulus, averaged Young's modulus, averaged shear modulus (all in GPa), and Poisson's ratio.
- Output file: `/app/outputs/step_02_mechanical_properties.json`
- Format: json
- Contract: {"bulk_modulus": number, "youngs_modulus": number, "shear_modulus": number, "poisson_ratio": number}
- Scoring: scored by hidden verifier

### Step 4: Compute electronic band structure and band gap
- Role: scored
- Action: Perform a self-consistent field (SCF) DFT calculation on the relaxed structure with a suitable k-point mesh. Compute the electronic band structure along a standard high-symmetry path for an fcc lattice (e.g., Γ-X-W-K-Γ-L-U-W-L-K). Identify the valence band maximum (VBM) and conduction band minimum (CBM) k-points. Determine the fundamental band gap: output the gap value in eV and the k-point labels of the VBM and CBM.
- Output file: `/app/outputs/step_03_band_gap.json`
- Format: json
- Contract: {"band_gap": number, "vbm_kpoint": string, "cbm_kpoint": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_constants.json`
- `/app/outputs/step_02_mechanical_properties.json`
- `/app/outputs/step_03_band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_constants.json
- path: `/app/outputs/step_01_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic stiffness constants of cubic pentadiamond.
- schema:
  - `type`: object
  - `required`:
    - `c11`: number (GPa)
    - `c12`: number (GPa)
    - `c44`: number (GPa)

### step_02_mechanical_properties.json
- path: `/app/outputs/step_02_mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Derived mechanical properties: bulk modulus, orientation-averaged Young's and shear moduli, and Poisson's ratio.
- schema:
  - `type`: object
  - `required`:
    - `bulk_modulus`: number (GPa)
    - `youngs_modulus`: number (GPa)
    - `shear_modulus`: number (GPa)
    - `poisson_ratio`: number

### step_03_band_gap.json
- path: `/app/outputs/step_03_band_gap.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Fundamental band gap value and k-point locations of VBM and CBM.
- schema:
  - `type`: object
  - `required`:
    - `band_gap`: number (eV)
    - `vbm_kpoint`: string
    - `cbm_kpoint`: string

Notes: Verification compares elastic constants to reference values with tolerance, checks that mechanical moduli exceed specified thresholds and Poisson's ratio is negative, and ensures band gap lies within an expected range with band edges at specific k-points.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "c11": "number (GPa)",
          "c12": "number (GPa)",
          "c44": "number (GPa)"
        }
      },
      "description": "Elastic stiffness constants of cubic pentadiamond."
    },
    {
      "file": "step_02_mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "bulk_modulus": "number (GPa)",
          "youngs_modulus": "number (GPa)",
          "shear_modulus": "number (GPa)",
          "poisson_ratio": "number"
        }
      },
      "description": "Derived mechanical properties: bulk modulus, orientation-averaged Young's and shear moduli, and Poisson's ratio."
    },
    {
      "file": "step_03_band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "band_gap": "number (eV)",
          "vbm_kpoint": "string",
          "cbm_kpoint": "string"
        }
      },
      "description": "Fundamental band gap value and k-point locations of VBM and CBM."
    }
  ],
  "notes": "Verification compares elastic constants to reference values with tolerance, checks that mechanical moduli exceed specified thresholds and Poisson's ratio is negative, and ensures band gap lies within an expected range with band edges at specific k-points."
}
```

## How you are scored
A hidden verifier scores each workflow stage independently, then combines them by weight into a single reward between 0 and 1. The verifier re-derives mechanical moduli from your reported elastic constants to check internal consistency, verifies adherence to the Born stability criteria, compares the computed moduli and band gap against expected physically meaningful ranges, and checks that the band edges are located at the correct k-points. Simply reporting values is not sufficient; the submitted artifacts must be complete, correctly formatted, and numerically plausible. The verifier does **not** reveal the reference values or tolerances; it only evaluates whether your computed results represent a valid reproduction of the pentadiamond predictions.
