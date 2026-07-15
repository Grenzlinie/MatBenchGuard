# DFT Hyperfine Couplings and NH2 Internal Rotation Barrier for F2Si(NH2) Radical

## Problem background
Nitrogen-containing paramagnetic defects in vitreous silica play a central role in understanding the material’s electronic properties and in interpreting its EPR signatures. One such defect has been assigned to the surface radical (≡Si–O)₂Si·(NH₂). Its experimental isotropic hyperfine coupling constants for ²⁹Si, ¹⁴N, and ¹H were measured, and a temperature dependence of the ¹⁴N coupling was observed. Quantum-chemical modelling with the fluorinated analogue F₂Si·(NH₂) provided a computational framework to rationalise these observations by reproducing the equilibrium couplings and, after accounting for the low‑barrier internal rotation of the NH₂ group, the effective ¹⁴N coupling at 300 K.

This task asks the solver to re-execute that computational protocol: to determine the equilibrium geometry, hyperfine couplings, NH₂ rotation barrier, and temperature‑averaged ¹⁴N coupling of the F₂Si·(NH₂) radical directly from first principles. The target values are left for the hidden checker to compare against the published reference; the solver must produce the quantities by running the described DFT procedure.

## Approach
The calculations are performed with the open‑source quantum chemistry package ORCA using the unrestricted B3LYP density functional and the 6‑311G(d,p) basis set. The model system is the F₂Si·(NH₂) radical, where the fluorine atoms replace the ≡Si–O– groups of the actual glass environment.

The approach consists of four consecutive stages:

1. **Geometry optimisation** – the minimum‑energy structure of F₂Si·(NH₂) is obtained in the doublet ground state. From the optimised coordinates, the HNSiH torsion angle (which quantifies the non‑planarity of the Si–NH₂ group) is extracted.

2. **Equilibrium hyperfine coupling constants** – a single‑point calculation on the optimised geometry yields the isotropic Fermi‑contact contributions a_iso for the magnetic nuclei ²⁹Si, ¹⁴N, and ¹H.

3. **NH₂ rotation potential energy surface** – a relaxed scan is performed along the NH₂ torsion angle φ. At each constrained angle the remaining degrees of freedom are optimised. The rotation barrier is obtained as the energy difference between the global maximum and minimum of the resulting E(φ) curve.

4. **Boltzmann‑averaged ¹⁴N isotropic constant at 300 K** – for each scan point, a_iso(¹⁴N) is computed (or extracted from the scan calculations). The effective ¹⁴N coupling at room temperature is obtained by Boltzmann averaging over the PES: \[ a_{\text{iso}}(T) = \frac{\int \exp[-E(\varphi)/(RT)] \, a_{\text{iso}}(\varphi)\,d\varphi}{\int \exp[-E(\varphi)/(RT)] \, d\varphi} \] with T = 300 K and R = 1.987 cal mol⁻¹ K⁻¹.

All stages must be executed sequentially, using the output of each preceding stage where appropriate. The exact computational parameters (e.g. grid size, convergence thresholds, scan step) are left to the solver’s discretion, as the hidden verifier compares only the final structural and magnetic quantities within realistic tolerances.

## Reproduction target
For the F₂Si·(NH₂) radical at the UB3LYP/6-311G(d,p) level, produce the following:
- The equilibrium HNSiH torsion angle (in degrees) from the optimised geometry.
- The isotropic hyperfine coupling constants a_iso (in Gauss) for ²⁹Si, ¹⁴N, and ¹H at the equilibrium geometry.
- The NH₂ internal rotation barrier height (in kcal mol⁻¹), determined as the energy difference between the highest and lowest points on the relaxed PES scan.
- The temperature‑averaged ¹⁴N isotropic coupling constant a_iso (in Gauss) at 300 K, obtained by Boltzmann averaging as defined in the Approach.

The task does not require simulating EPR spectra, studying other radicals, or comparing with experiment. The hidden checker holds a set of reference values against which these computed quantities are assessed.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Geometry optimization of F2Si·(NH2)
- Role: scored
- Action: Perform a UB3LYP/6-311G(d,p) geometry optimization of the F2Si·(NH2) radical using ORCA. Save the optimized Cartesian coordinates in XYZ format and extract the HNSiH torsion angle.
- Output file: `/app/outputs/step_01_geometry.txt`
- Format: txt
- Contract: First line: number of atoms. Second line: comment. Following lines: atom symbol and X Y Z coordinates in Angstrom. Last line: 'HNSiH_torsion: <value>' (angle in degrees).
- Scoring: scored by hidden verifier

### Step 2: Equilibrium hyperfine coupling tensor calculation
- Role: scored
- Action: Using the optimized geometry from step 1, run a single‑point UB3LYP/6-311G(d,p) calculation with hyperfine coupling tensor computation in ORCA. Extract the isotropic components a_iso for ²⁹Si, ¹⁴N, and ¹H.
- Output file: `/app/outputs/step_02_hfc_equilibrium.json`
- Format: json
- Contract: JSON object with keys: "a_iso_Si" (float), "a_iso_N" (float), "a_iso_H" (float).
- Scoring: scored by hidden verifier

### Step 3: NH2 rotation potential energy scan and barrier
- Role: scored
- Action: Perform a relaxed potential energy surface scan along the NH2 torsion angle φ at UB3LYP/6-311G(d,p) level. Compute the energy at each grid point and determine the rotation barrier as the energy difference between the maximum and minimum.
- Output file: `/app/outputs/step_03_rotation_barrier.txt`
- Format: txt
- Contract: A single line: 'barrier: <value>'.
- Scoring: scored by hidden verifier

### Step 4: Temperature‑averaged a_iso(¹⁴N) at 300 K
- Role: scored (load-bearing)
- Action: For each point of the scan from step 3, compute a_iso(¹⁴N) (or extract it if available). Apply Boltzmann averaging using the formula a_iso(T) = ∫ exp[-E(φ)/RT] a_iso(φ) dφ / ∫ exp[-E(φ)/RT] dφ at T=300 K. Output the resulting averaged value.
- Output file: `/app/outputs/step_04_average_a_iso_14N_300K.txt`
- Format: txt
- Contract: A single line: 'a_iso_N_300K: <value>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_geometry.txt`
- `/app/outputs/step_02_hfc_equilibrium.json`
- `/app/outputs/step_03_rotation_barrier.txt`
- `/app/outputs/step_04_average_a_iso_14N_300K.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_geometry.txt
- path: `/app/outputs/step_01_geometry.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimized geometry and HNSiH torsion angle.
- schema:
  - `type`: text
  - `description`: Optimized XYZ coordinates followed by a line giving the HNSiH torsion angle. The checker parses the final line for the angle value and compares it to the hidden gold within a tolerance.

### step_02_hfc_equilibrium.json
- path: `/app/outputs/step_02_hfc_equilibrium.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium isotropic hyperfine coupling constants for ²⁹Si, ¹⁴N, and ¹H (in Gauss).
- schema:
  - `type`: object
  - `required`: `a_iso_Si`, `a_iso_N`, `a_iso_H`
  - `properties`:
    - `a_iso_Si`:
      - `type`: number
      - `unit`: Gauss
    - `a_iso_N`:
      - `type`: number
      - `unit`: Gauss
    - `a_iso_H`:
      - `type`: number
      - `unit`: Gauss

### step_03_rotation_barrier.txt
- path: `/app/outputs/step_03_rotation_barrier.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: NH2 internal rotation barrier height (kcal/mol).
- schema:
  - `type`: text
  - `description`: Single line 'barrier: <value>'. The checker extracts the barrier value (kcal/mol) and compares it to the hidden gold within a tolerance.

### step_04_average_a_iso_14N_300K.txt
- path: `/app/outputs/step_04_average_a_iso_14N_300K.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Temperature‑averaged a_iso(¹⁴N) at 300 K (Gauss).
- schema:
  - `type`: text
  - `description`: Single line 'a_iso_N_300K: <value>'. The checker extracts the averaged ¹⁴N isotropic coupling (Gauss) and compares it to the hidden gold within a tolerance.

Notes: All quantities are compared to the reference DFT‑computed values from the paper. Tolerances absorb legitimate toolchain spread. The load‑bearing step (step_04) forces genuine execution of the full workflow.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_geometry.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Optimized XYZ coordinates followed by a line giving the HNSiH torsion angle. The checker parses the final line for the angle value and compares it to the hidden gold within a tolerance."
      },
      "description": "Optimized geometry and HNSiH torsion angle."
    },
    {
      "file": "step_02_hfc_equilibrium.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "a_iso_Si",
          "a_iso_N",
          "a_iso_H"
        ],
        "properties": {
          "a_iso_Si": {
            "type": "number",
            "unit": "Gauss"
          },
          "a_iso_N": {
            "type": "number",
            "unit": "Gauss"
          },
          "a_iso_H": {
            "type": "number",
            "unit": "Gauss"
          }
        }
      },
      "description": "Equilibrium isotropic hyperfine coupling constants for ²⁹Si, ¹⁴N, and ¹H (in Gauss)."
    },
    {
      "file": "step_03_rotation_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line 'barrier: <value>'. The checker extracts the barrier value (kcal/mol) and compares it to the hidden gold within a tolerance."
      },
      "description": "NH2 internal rotation barrier height (kcal/mol)."
    },
    {
      "file": "step_04_average_a_iso_14N_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single line 'a_iso_N_300K: <value>'. The checker extracts the averaged ¹⁴N isotropic coupling (Gauss) and compares it to the hidden gold within a tolerance."
      },
      "description": "Temperature‑averaged a_iso(¹⁴N) at 300 K (Gauss)."
    }
  ],
  "notes": "All quantities are compared to the reference DFT‑computed values from the paper. Tolerances absorb legitimate toolchain spread. The load‑bearing step (step_04) forces genuine execution of the full workflow."
}
```

## How you are scored
Each workflow step produces a prescribed output file under /app/outputs. A hidden verifier independently reads each scored artifact, extracts the reported numbers (torsion angle, a_iso values, barrier, and averaged coupling), and compares them to hidden reference values using tolerances that account for the normal spread introduced by different ORCA versions, compilations, and numerical settings. Every scored step carries a weight that reflects its importance; the weights are combined into a single final reward in [0, 1]. Simply reporting numbers without executing the described DFT calculations will not satisfy the step contracts and cannot yield a high score. The solver must genuinely perform the geometry optimisation, HFC calculation, PES scan, and post-processing to obtain the required outputs.
