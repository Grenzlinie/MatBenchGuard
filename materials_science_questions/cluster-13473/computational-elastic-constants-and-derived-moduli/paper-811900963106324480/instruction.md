# Size-dependent Elastic Constants and Stress Distribution of HCP Co Nanowires from MD

## Problem background
As metallic structures shrink to the nanoscale, their mechanical properties deviate from bulk values due to the increasing fraction of surface atoms with reduced coordination. This size dependence is critical for designing nanodevices and nanocomposites. Cobalt (Co) nanowires with a hexagonal closed-packed (HCP) crystal structure are one such system: the large surface-to-volume ratio alters the effective elastic constants and induces inhomogeneous internal stress fields even in the absence of external loading. Understanding how the axial Young's modulus and Poisson's ratio vary with the nanowire side dimension, and characterizing the cross-sectional stress profile at free relaxation, is essential for predicting the performance of Co-based nanocomposites.

## Approach
Molecular dynamics (MD) simulations are used with an embedded-atom method (EAM) potential to model the interatomic interactions in HCP cobalt. The approach proceeds by constructing atomistic models of Co nanowires as "cubic hexagons"—structures with the same side length along all three HCP directions—for a range of side dimensions (approximately 2–8 nm). Each nanowire first undergoes energy minimization and free relaxation at zero external stress to reach equilibrium. From this relaxed state, a uniaxial tensile load is applied along the axial direction at a low strain rate, and the per-atom stresses (e.g., via a smoothed particle hydrodynamics definition) are recorded along with global stress–strain and transverse strain data. The axial Young's modulus is extracted as the slope of the linear elastic part of the stress–strain curve, and Poisson's ratio is obtained from the ratio of transverse contraction to axial extension. In addition, the free-relaxation configuration provides the per-atom stress tensor; binning these values along a transverse direction yields the cross-sectional profile of the axial normal stress component at zero external load. The entire workflow is executable using the open-source LAMMPS code together with the public EAM potential, making it fully reproducible from the described protocol.

## Reproduction target
Perform MD simulations for HCP Co cubic hexagon nanowires with side dimensions d covering the range ~2–8 nm. For each size, compute the axial Young's modulus E (in GPa) and Poisson's ratio ν (dimensionless) from uniaxial tension and write them to the file `elastic_moduli.csv` with columns `d_nm`, `E_GPa`, `nu`. Separately, for one representative nanowire size, compute the cross-sectional profile of the axial normal stress σ_zz (in GPa) at free relaxation as a function of distance from the wire centre, and write it to `stress_profile.csv` with columns `position_nm`, `sigma_zz_GPa`. Both CSV files must be placed under `/app/outputs`.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- EAM potential for HCP Co (Pasianot & Savino 1992): https://www.ctcms.nist.gov/potentials/Co.html

## Workflow steps

### Step 1: Build HCP Co nanowire atomistic models
- Role: process
- Action: Construct atomistic models of HCP Co nanowires as 'cubic hexagons' with side dimensions d from ~2 nm to ~8 nm. Lattice constants: a = 2.507 Å, c = 4.069 Å (c/a ≈ 1.623) for HCP Co. Generate input coordinate files for each size.

### Step 2: Run molecular dynamics simulations
- Role: process
- Action: For each nanowire model, run MD simulation using LAMMPS with the Co EAM potential: energy minimization, free relaxation (NPT, zero external stress), then uniaxial tension along axial direction at low constant strain rate. Record per-atom stresses (SPH) and global stress–strain and transverse strain data.

### Step 3: Extract size-dependent elastic constants
- Role: scored (load-bearing)
- Action: From the MD stress–strain data for each side dimension d, compute axial Young's modulus E as the linear slope of the axial stress–strain curve, and Poisson's ratio ν as negative ratio of transverse strain to axial strain in the same linear regime. Output a CSV with columns d_nm, E_GPa, nu.
- Output file: `/app/outputs/elastic_moduli.csv`
- Format: csv
- Contract: CSV with header: d_nm, E_GPa, nu. d_nm is side dimension in nm; E_GPa is a float; nu is a float.
- Scoring: scored by hidden verifier

### Step 4: Compute cross-sectional normal stress distribution
- Role: scored
- Action: For a representative side dimension (e.g., any size where the pattern is clear), from the free-relaxation configuration extract per-atom stress tensors, bin along a transverse direction to obtain profile of axial normal stress σ_zz as a function of position across the nanowire cross-section. Output a CSV with columns position_nm, sigma_zz_GPa.
- Output file: `/app/outputs/stress_profile.csv`
- Format: csv
- Contract: CSV with header: position_nm, sigma_zz_GPa. position_nm is distance from wire centre (nm); sigma_zz_GPa is the average normal stress in GPa at that position.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_moduli.csv`
- `/app/outputs/stress_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_moduli.csv
- path: `/app/outputs/elastic_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Size-dependent axial elastic modulus and Poisson's ratio. The checker will compare to the paper's reported asymptotes and monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `d_nm`, `E_GPa`, `nu`
  - `units`:
    - `d_nm`: nm
    - `E_GPa`: GPa
    - `nu`: dimensionless

### stress_profile.csv
- path: `/app/outputs/stress_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Cross-sectional normal stress profile at free relaxation. The checker will verify tensile near surface and compressive near centre.
- schema:
  - `type`: table
  - `required_columns`: `position_nm`, `sigma_zz_GPa`
  - `units`:
    - `position_nm`: nm
    - `sigma_zz_GPa`: GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "d_nm",
          "E_GPa",
          "nu"
        ],
        "units": {
          "d_nm": "nm",
          "E_GPa": "GPa",
          "nu": "dimensionless"
        }
      },
      "description": "Size-dependent axial elastic modulus and Poisson's ratio. The checker will compare to the paper's reported asymptotes and monotonic trends."
    },
    {
      "file": "stress_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "position_nm",
          "sigma_zz_GPa"
        ],
        "units": {
          "position_nm": "nm",
          "sigma_zz_GPa": "GPa"
        }
      },
      "description": "Cross-sectional normal stress profile at free relaxation. The checker will verify tensile near surface and compressive near centre."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that scores each required output artifact independently and combines the stage scores into an overall reward. For `elastic_moduli.csv`, the verifier compares your reported size‑dependent moduli and Poisson’s ratios to known reference trends and asymptotes, using tolerances that accommodate expected variation from different implementations and simulation choices. For `stress_profile.csv`, the verifier checks that the stress distribution exhibits the qualitative features expected for a self‑balancing inhomogeneous field in a nanoscale wire. Merely reporting the paper’s published numbers without following the workflow will not satisfy the verifier; the artifacts must be the product of the described simulation pipeline. All checks are deterministic and do not require network access.