# Voronoi-like protocol for nanocrystalline copper elastic modulus ratio

## Problem background
Nanocrystalline metals — polycrystalline metals with average grain size below 100 nm — possess a large volume fraction of grain boundaries, which strongly affect their mechanical properties. In particular, the elastic modulus of the grain boundary region relative to that of the grain interior has been debated: earlier estimates suggested that the boundary is about 70% as stiff as the core, but recent atomistic simulations and experiments call this into doubt, finding that the grain boundary may be significantly softer. This work introduces a model of fully dense nanocrystalline copper constructed from randomly packed uniform grains, enabling a clean separation of grain-size effects from grain-size dispersity, to determine the grain boundary's elastic modulus through molecular dynamics tensile tests. The headline quantity is the ratio of the grain boundary Young's modulus to the grain core modulus, E_GB/E_core. The task is to reproduce the computational pipeline and obtain this ratio.

## Approach
The central idea is to create nanocrystalline Cu configurations where grains are nearly uniform in size, using as Voronoi seeds the centers of a random close packing (RCP) of identical spheres. First, a packing of n=27 identical spheres is generated in a periodic cell with a volume fraction ≈0.64 via an iterative volume-perturbation and conjugate-gradient energy minimization algorithm. These sphere centers serve as seeds for a standard Voronoi tessellation, yielding polyhedral grains with very low size dispersity (< 5%). Each grain is then filled with a randomly oriented face-centered cubic (fcc) Cu crystallite (lattice parameter 0.3615 nm). By scaling the supercell dimensions, three configurations are produced with average grain diameters of approximately 5, 10, and 15 nm. Molecular dynamics simulations at 300 K are performed using the embedded-atom method (EAM) Mishin potential for Cu: each configuration is first relaxed under zero external stress (NPT ensemble), then subjected to a uniaxial tensile test at a strain rate of 5×10^8 s⁻¹ in the NσT ensemble. The overall Young's modulus is obtained from a linear fit of the stress–strain curve in the elastic regime (strain < 0.3%). Core atoms are identified via Common Neighbor Analysis (CNA), and the core volume fraction φ_core is computed. This yields three (φ_core, E_overall) data points. The Reuss mixture model, E = 1/(φ_core/E_core + (1−φ_core)/E_GB), is then fitted to these points to extract the moduli of the grain core (E_core) and grain boundary (E_GB). Finally, the ratio E_GB/E_core is reported.

## Reproduction target
Implement the full computational pipeline described above on the three grain sizes (≈5, 10, 15 nm). Produce the intermediate output file elastic_data.csv containing the three rows (d_nm, phi_core, E_overall_GPa). Fit the Reuss model to this data, write the fitted parameters to reuss_fit_params.txt, and compute E_GB/E_core, saving it as a single float in ratio.txt. The goal is to obtain a physically plausible ratio that reflects the stiffness of the grain boundary relative to the grain interior, as would be measured by this protocol.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Voro++ Voronoi tessellation library: https://github.com/chr1shr/voro
- EAM Mishin copper interatomic potential: https://www.ctcms.nist.gov/potentials/Download/Cu_mishin_eam.alloy
- Python with numpy and scipy: pip install numpy scipy

## Workflow steps

### Step 1: Generate random close packings
- Role: process
- Action: Generate random close packings of n=27 identical spheres in a periodic cell using the iterative volume perturbation and conjugate‑gradient energy minimization algorithm. Converge to volume fraction ≈0.64. Save sphere center coordinates.
- Evidence: `/app/outputs/packing_output.log`

### Step 2: Create nanocrystalline Cu configurations
- Role: process
- Action: Using the sphere center coordinates as Voronoi seeds, perform standard Voronoi tessellation. Fill each grain with a randomly oriented fcc Cu crystallite (lattice parameter 0.3615 nm). Adjust supercell dimensions to achieve target grain diameters of approximately 5, 10, and 15 nm. Output the atomic configurations in LAMMPS data format.
- Evidence: `/app/outputs/configurations.log`

### Step 3: MD relaxation, tensile tests, and elastic data
- Role: scored (load-bearing)
- Action: For each configuration: (1) Relax at 300 K under NPT/zero‑external‑stress using the Mishin EAM potential until the potential energy stabilizes. (2) Run a uniaxial tensile test at 300 K in NσT ensemble with strain rate 5e8 s⁻¹; record stress‑strain. Compute overall Young's modulus by a linear fit to stress‑strain where strain < 0.3%. (3) After relaxation, perform Common Neighbor Analysis (CNA) to identify grain core atoms; compute core volume fraction φ_core = (N_core × 0.0118 nm³) / V_system. Compile the three data rows and write elastic_data.csv.
- Output file: `/app/outputs/elastic_data.csv`
- Format: csv
- Contract: Columns: d_nm (float), phi_core (float), E_overall_GPa (float). Three rows.
- Scoring: scored by hidden verifier

### Step 4: Fit Reuss model for grain core and boundary moduli
- Role: scored
- Action: Fit the Reuss model E = 1/(phi_core/E_core + (1-phi_core)/E_GB) to the three data points in elastic_data.csv using least‑squares fitting. Output the fitted parameters E_core and E_GB in reuss_fit_params.txt.
- Output file: `/app/outputs/reuss_fit_params.txt`
- Format: txt
- Contract: Two lines: E_core_GPa = <value>, E_GB_GPa = <value>.
- Scoring: scored by hidden verifier

### Step 5: Compute elastic modulus ratio
- Role: scored
- Action: From the fitted E_core and E_GB, compute the ratio E_GB/E_core and write the single float to ratio.txt.
- Output file: `/app/outputs/ratio.txt`
- Format: txt
- Contract: Single floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_data.csv`
- `/app/outputs/reuss_fit_params.txt`
- `/app/outputs/ratio.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_data.csv
- path: `/app/outputs/elastic_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw data from MD tensile tests: overall Young's modulus and core volume fraction. The checker recomputes the Reuss fit and ratio from this file.
- schema:
  - `type`: table
  - `required_columns`: `d_nm`, `phi_core`, `E_overall_GPa`
  - `units`:
    - `d_nm`: nm
    - `phi_core`: dimensionless
    - `E_overall_GPa`: GPa
  - `description`: Three rows, one per grain size (≈5, 10, 15 nm).

### reuss_fit_params.txt
- path: `/app/outputs/reuss_fit_params.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Fitted Young's moduli from the Reuss model. Checker verifies self-consistency with elastic_data.csv.
- schema:
  - `type`: text
  - `required`:
    - `lines`: 2
    - `pattern`: E_core_GPa = <float>, E_GB_GPa = <float>

### ratio.txt
- path: `/app/outputs/ratio.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Ratio E_GB/E_core. Checker verifies self-consistency with fit parameters and elastic data.
- schema:
  - `type`: text
  - `required`:
    - `single_float`: True

Notes: The primary scoring metric is the recomputed ratio from elastic_data.csv; reuss_fit_params.txt and ratio.txt serve as consistency checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "d_nm",
          "phi_core",
          "E_overall_GPa"
        ],
        "units": {
          "d_nm": "nm",
          "phi_core": "dimensionless",
          "E_overall_GPa": "GPa"
        },
        "description": "Three rows, one per grain size (≈5, 10, 15 nm)."
      },
      "description": "Raw data from MD tensile tests: overall Young's modulus and core volume fraction. The checker recomputes the Reuss fit and ratio from this file."
    },
    {
      "file": "reuss_fit_params.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "lines": 2,
          "pattern": "E_core_GPa = <float>, E_GB_GPa = <float>"
        }
      },
      "description": "Fitted Young's moduli from the Reuss model. Checker verifies self-consistency with elastic_data.csv."
    },
    {
      "file": "ratio.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "single_float": true
        }
      },
      "description": "Ratio E_GB/E_core. Checker verifies self-consistency with fit parameters and elastic data."
    }
  ],
  "notes": "The primary scoring metric is the recomputed ratio from elastic_data.csv; reuss_fit_params.txt and ratio.txt serve as consistency checks."
}
```

## How you are scored
A hidden verifier will read the three output files. It will recompute the Reuss fit from the raw data in elastic_data.csv, compute the ratio E_GB/E_core, and compare it against a hidden reference value derived from the original study (T1 recompute). It will also check that elastic_data.csv contains exactly three rows with physically plausible ranges (phi_core between 0.5 and 1, E_overall between 50 and 150 GPa), and verify that the fit parameters in reuss_fit_params.txt are self-consistent with the CSV (within numerical tolerance). The ratio.txt value is cross-checked with the recomputed ratio. The final reward is a weighted combination of these checks, with the highest weight on the recomputed ratio from the CSV. A perfect reproduction will score near 1.0; substantial deviations from the expected ratio will result in lower scores. Simple fabrication or reporting of arbitrary numbers will not pass, as the verifier recomputes and validates internal consistency.
