# MD simulation of mechanical properties and deformation of nanoglass AlN with 1 nm grain size

## Problem background
Aluminium nitride (AlN) is a high-strength ceramic with excellent thermal and electrical properties, but its intrinsic brittleness restricts structural applications. Nanoglass ceramics—non-crystalline materials composed of glassy nanograins connected by glass–glass interfaces—have attracted interest because they may exhibit enhanced ductility compared to their homogeneous amorphous counterparts. Understanding how the size of the glassy grains influences the deformation mechanisms in nanoglass AlN (ng‑AlN) is essential for designing damage‑tolerant ceramics. This task uses large‑scale molecular dynamics (MD) simulations to reproduce the structural and mechanical behaviour of ng‑AlN with an average grain size of 1 nm under uniaxial tension at 10 K and a strain rate of 1e8 s⁻¹. The pipeline produces elastic moduli, short‑ and medium‑range order descriptors, a stress–strain curve, and a quantitative measure of local plastic activity (shear transformation zones).

## Approach
The workflow follows a three‑stage simulation protocol. First, a homogeneous amorphous AlN unit cell is prepared by melting a wurtzite AlN crystal at 3500 K and then rapidly quenching to 10 K under zero‑pressure conditions. Second, a nanoglass sample with 1 nm columnar grains is constructed by Voronoi tessellation of the amorphous unit, with overlapping atoms removed; the sample is then energy‑minimised and relaxed at 10 K. Structural characterisation of the relaxed configuration includes calculating the elastic constants (C11, C12) and their derived moduli (bulk and Young’s), the fractions of three‑fold, four‑fold and five‑fold coordinated atoms, and the radial distribution function with a focus on its second peak. Third, uniaxial tension is applied along the long (z) axis using an NVE ensemble with a Langevin thermostat, periodic boundaries in the y and z directions, and a free surface in the x direction. The simulation runs at a constant strain rate of 1e8 s⁻¹ for a total strain exceeding 0.30. Atomic von Mises shear strains are computed from the deformation trajectory to identify shear transformation zones (STZs), and the fraction of STZ atoms is recorded at three characteristic strains. All atomistic interactions are described by the Vashishta interatomic potential for AlN, and the MD package LAMMPS provides the computational engine.

## Reproduction target
Produce the following five scored artefacts for ng‑AlN with 1 nm grain size at 10 K and a strain rate of 1e8 s⁻¹:

- `elastic_constants.json` – bulk modulus B (GPa), Young’s modulus Y (GPa), and the elastic constants C11 and C12 (GPa).
- `coordination_fractions.json` – fractions (dimensionless) of three‑fold, four‑fold, and five‑fold coordinated atoms, summing to approximately 1.
- `rdf_second_peak.json` – intensity (dimensionless) and position (Å) of the second peak in the total radial distribution function.
- `stress_strain.csv` – engineering strain (dimensionless) and engineering stress (GPa) recorded from the tensile MD run, covering strains from 0 up to at least 0.30.
- `stz_fraction.csv` – fraction of atoms with von Mises shear strain > 0.2 (STZ fraction) at tensile strains ε = 0.14, 0.18, and 0.30.

The verifier will compare these outputs to reference values or threshold criteria; the goal is to faithfully compute them by executing the simulation pipeline described in the workflow steps.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- Vashishta interatomic potential for AlN: 10.1063/1.3552716

## Workflow steps

### Step 1: Build amorphous AlN unit via melt-quench
- Role: process
- Action: Create a wurtzite AlN crystal unit cell (approx. 49.76 x 48.47 x 49.80 Å³), melt at 3500 K for 500 ps under NPT at zero pressure, then quench to 10 K at a cooling rate of 2e14 K/s. This produces a homogeneous amorphous AlN configuration.
- Evidence: none

### Step 2: Construct and relax ng-AlN sample (1 nm grain size)
- Role: process
- Action: Using the amorphous AlN unit from step_01 as a source, build a nanoglass sample with average grain size 1 nm by Voronoi tessellation with 436 randomly distributed seeds. Box dimensions: 262 Å (x) × 51 Å (y) × 523 Å (z). Delete overlapping atoms at grain interfaces. Minimise energy via conjugate gradient, then relax at 10 K under NPT for 200 ps.
- Evidence: `/app/outputs/ng_aln_relaxed.data`

### Step 3: Compute elastic moduli of relaxed ng-AlN
- Role: scored
- Action: From the relaxed ng-AlN configuration, compute the elastic constants C11 and C12 (e.g., via strain fluctuations or small deformation). Derive bulk modulus B = (C11+2C12)/3 and Young's modulus Y = (C11+2C12)(C11-C12)/(C11+C12).
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with keys: B (number, GPa), Y (number, GPa), C11 (number, GPa), C12 (number, GPa).
- Scoring: scored by hidden verifier

### Step 4: Compute coordination number fractions
- Role: scored
- Action: Analyse the relaxed ng-AlN configuration to obtain the distribution of coordination numbers (Al and N sites). Compute the fractions of threefold-, fourfold-, and fivefold-coordinated atoms.
- Output file: `/app/outputs/coordination_fractions.json`
- Format: json
- Contract: JSON object with keys: threefold (number, fraction), fourfold (number, fraction), fivefold (number, fraction). The three fractions should sum to approximately 1.
- Scoring: scored by hidden verifier

### Step 5: Compute RDF second-peak intensity and position
- Role: scored
- Action: Calculate the radial distribution function g(r) of the relaxed ng-AlN configuration. Locate the second peak (related to Al-Al and N-N correlations) and record its intensity (height) and position (r in Å).
- Output file: `/app/outputs/rdf_second_peak.json`
- Format: json
- Contract: JSON object with keys: intensity (number, dimensionless g(r) value), position (number, r in Å).
- Scoring: scored by hidden verifier

### Step 6: Run uniaxial tension MD simulation and record stress-strain curve
- Role: scored
- Action: Perform uniaxial tension along the z-direction on the relaxed ng-AlN configuration using NVE ensemble with a Langevin thermostat at 10 K. Use a constant strain rate of 1e8 s⁻¹, timestep 1 fs, with periodic boundaries in y and z and free surface in x. Run for 3000 ps. Record the engineering stress (virial) and strain as a time series.
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: CSV with header: strain, stress (GPa). Rows cover the full deformation up to at least strain 0.30.
- Scoring: scored by hidden verifier

### Step 7: Compute STZ fraction at selected strains from tension trajectory
- Role: scored (load-bearing)
- Action: From the atomic trajectory of the tension simulation, compute the atomic von Mises shear strain for each atom. For the strains ε = 0.14, 0.18, 0.30, count the fraction of atoms with Mises strain greater than 0.2 (identified as shear transformation zones).
- Output file: `/app/outputs/stz_fraction.csv`
- Format: csv
- Contract: CSV with header: strain, fraction (dimensionless). Rows: strain=0.14, 0.18, 0.30 with their corresponding STZ fractions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/coordination_fractions.json`
- `/app/outputs/rdf_second_peak.json`
- `/app/outputs/stress_strain.csv`
- `/app/outputs/stz_fraction.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic moduli computed from the relaxed ng-AlN structure.
- schema:
  - `type`: object
  - `required`:
    - `B`: number
    - `Y`: number
    - `C11`: number
    - `C12`: number
  - `units`:
    - `B`: GPa
    - `Y`: GPa
    - `C11`: GPa
    - `C12`: GPa

### coordination_fractions.json
- path: `/app/outputs/coordination_fractions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coordination number fractions extracted from the relaxed structure.
- schema:
  - `type`: object
  - `required`:
    - `threefold`: number
    - `fourfold`: number
    - `fivefold`: number
  - `units`:
    - `threefold`: fraction
    - `fourfold`: fraction
    - `fivefold`: fraction

### rdf_second_peak.json
- path: `/app/outputs/rdf_second_peak.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Radial distribution function second-peak properties.
- schema:
  - `type`: object
  - `required`:
    - `intensity`: number
    - `position`: number
  - `units`:
    - `intensity`: dimensionless
    - `position`: Å

### stress_strain.csv
- path: `/app/outputs/stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Stress-strain curve from the tension MD simulation; the checker verifies ductility by a threshold condition on stress at ε=0.25 relative to peak stress.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

### stz_fraction.csv
- path: `/app/outputs/stz_fraction.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Fractions of STZ atoms at three tensile strains; the checker verifies extensive STZ activity (fraction at ε=0.3 ≥ 0.50).
- schema:
  - `type`: table
  - `required_columns`: `strain`, `fraction`
  - `units`:
    - `strain`: dimensionless
    - `fraction`: dimensionless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B": "number",
          "Y": "number",
          "C11": "number",
          "C12": "number"
        },
        "units": {
          "B": "GPa",
          "Y": "GPa",
          "C11": "GPa",
          "C12": "GPa"
        }
      },
      "description": "Elastic moduli computed from the relaxed ng-AlN structure."
    },
    {
      "file": "coordination_fractions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "threefold": "number",
          "fourfold": "number",
          "fivefold": "number"
        },
        "units": {
          "threefold": "fraction",
          "fourfold": "fraction",
          "fivefold": "fraction"
        }
      },
      "description": "Coordination number fractions extracted from the relaxed structure."
    },
    {
      "file": "rdf_second_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "intensity": "number",
          "position": "number"
        },
        "units": {
          "intensity": "dimensionless",
          "position": "Å"
        }
      },
      "description": "Radial distribution function second-peak properties."
    },
    {
      "file": "stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Stress-strain curve from the tension MD simulation; the checker verifies ductility by a threshold condition on stress at ε=0.25 relative to peak stress."
    },
    {
      "file": "stz_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "fraction"
        ],
        "units": {
          "strain": "dimensionless",
          "fraction": "dimensionless"
        }
      },
      "description": "Fractions of STZ atoms at three tensile strains; the checker verifies extensive STZ activity (fraction at ε=0.3 ≥ 0.50)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted files are evaluated by a hidden verifier that compares each scored output to a reference or threshold. Each scored artifact contributes to a final reward between 0 and 1; the stress‑strain ductility and the STZ fraction carry higher weight because they directly reflect the plastic deformation behaviour, while the elastic and structural descriptors receive somewhat lower weight. The verifier does not re‑run the simulations—it trusts that you executed the workflow honestly. Accurate outputs obtained from a correctly performed MD pipeline are sufficient to earn full credit; merely reporting numbers without actually running the workflow will be detectable and will not pass. The exact tolerances and thresholds are hidden, but they are chosen to accommodate normal run‑to‑run variability and to ensure that a faithful reproduction succeeds.
