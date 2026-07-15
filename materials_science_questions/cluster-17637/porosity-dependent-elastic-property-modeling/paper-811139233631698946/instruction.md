# FFT-based Homogenization for Size-Dependent Elastic Moduli of Nanocomposites with Imperfect Interfaces

## Problem background
Nanocomposites containing unidirectional nanofibers or nanopores exhibit size-dependent effective elastic properties because the exceptionally high surface-to-volume ratio makes coherent interface/surface stresses non-negligible. At the nanoscale, the elastic moduli (transverse bulk, shear, longitudinal, etc.) deviate significantly from classical micromechanical predictions, and capturing these effects requires a computational method that accounts for surface elasticity. This task implements an FFT‑based periodic homogenization scheme that incorporates such imperfect interface stresses, enabling the computation of all six Hill effective moduli for unidirectional nanocomposites.

## Approach
The solution extends the classical Moulinec–Suquet FFT homogenization framework by adding contributions from coherent imperfect interfaces. The composite is modeled as a periodic unit cell containing one or many aligned cylindrical inclusions. A reference elastic medium is introduced, and the total polarization field includes both bulk phase contrast and surface‑stress terms derived from the interface constitutive law. The governing equations are Fourier‑transformed, yielding a large linear system for the Fourier coefficients of the strain field that couples the inclusion geometry (through characteristic functions), the wave‑vector dependent Green operator, and the interface surface integrals. An iterative solver (e.g., conjugate gradient) is used to solve this system. After convergence, the effective stiffness tensor is obtained from the macroscopic stress formula, from which the six Hill moduli (k*, m*, n*, l*, G*, G'*) are extracted via the standard transversely‑isotropic relations. The implementation must handle general periodic inclusion shapes and two‑dimensional interface stiffness matrices. The solver is exercised on three benchmark sets: (i) circular nanopores with different surface elastic moduli (labeled A, B, C) and two periodic distributions (square, hexagonal) to isolate the surface‑strength effect; (ii) non‑circular nanopores with 4‑ and 8‑oscillation cross‑sections to capture shape effects on the transverse bulk modulus; (iii) circular nanofibers with a prescribed interface modulus, tested under square, hexagonal, and random distributions, to demonstrate size‑dependency. In each case the computed moduli are normalized: for nanopores the reference is the no‑surface‑stress case (surface C); for non‑circular pores the reference is the matrix bulk modulus; for nanofibers the reference is the set of matrix moduli. The exact normalizations are stated in the step definitions below.

## Reproduction target
Implement the FFT‑based homogenization algorithm described in Approach and run it for the three configurations specified in the workflow steps. Produce three CSV files: (1) `step_01_nanopores_circular.csv` – for circular nanopores of radius 1, 2, 5, 10, 20, 30, 40, and 50 nm, under square and hexagonal distributions, with surfaces A, B, and C, at a fixed volume fraction of 0.2; compute the six Hill moduli and divide each by the corresponding modulus for surface C (no surface stress). (2) `step_02_nanopores_noncircular.csv` – for non‑circular nanopores (4‑oscillation and 8‑oscillation shapes defined by a radius function with amplitude 0.4 R0) under surface A and volume fraction 0.2, compute the effective transverse bulk modulus k* and normalize it by the matrix bulk modulus κ0 for R0 values of 1, 2, 5, 10, 20, 30, 40, and 50 nm. (3) `step_03_nanofibers.csv` – for circular nanofibers with the interface and bulk properties listed in Step 5, under square, hexagonal, and random distributions at a volume fraction of 0.3, compute the six Hill moduli and normalize each by the corresponding matrix modulus for radii from 1 to 50 nm; for the random distribution include at least one realization and a realization column. The exact column schemas and output paths are given in the step contracts.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Set up material and geometric parameters
- Role: process
- Action: Define all material and geometric parameters for the three benchmark sets as specified: matrix E0=70 GPa, ν0=0.32; surface elastic moduli A (Esi=-7.58576e-9 GPa·m, νsi=0.39), B (Esi=-1.59233e-9 GPa·m, νsi=1.123), C (no surface stress); pore/fiber radii 1,2,5,10,20,30,40,50 nm; volume fractions f=0.2 (nanopores) and f=0.3 (nanofibers); non-circular cross-sections with A=0.4R0 and B=4,8; nanofiber interface Esi/E0=1.1636e-9 m, νsi=0.45, fiber properties E0=2Ei=70 GPa, ν0=νi=0.25. Organize into data structures suitable for driving the FFT simulations.
- Evidence: none

### Step 2: Implement FFT-based homogenization solver
- Role: process
- Action: Implement the FFT-based periodic homogenization algorithm that incorporates coherent imperfect interface/surface contributions. The implementation must include: computation of inclusion characteristic functions and their Fourier transforms; assembly of the linear system for the strain Fourier coefficients coupling bulk contrast, inclusion geometry, and interface surface integrals; an iterative solver (e.g., conjugate gradient) to solve the system; extraction of the effective stiffness tensor via the macroscopic stress formula; and calculation of the six Hill moduli (k*, m*, n*, l*, G*, G'*). The method must handle general periodic inclusion geometries and 2D surface parameter matrices.
- Evidence: none

### Step 3: Compute normalized effective moduli for circular nanopores
- Role: scored (load-bearing)
- Action: Using the implemented FFT solver, simulate cylindrical nanopores with circular cross-sections for each combination of radius (1,2,5,10,20,30,40,50 nm), distribution (square, hexagonal), and surface type (A, B, C). Compute the six Hill moduli and normalize each by the corresponding modulus for surface C (no surface stress). Write the normalized ratios to step_01_nanopores_circular.csv.
- Output file: `/app/outputs/step_01_nanopores_circular.csv`
- Format: csv
- Contract: Columns: radius (float, nm), distribution (string, 'square'|'hexagonal'), surface (string, 'A'|'B'|'C'), k_norm (float), m_norm (float), n_norm (float), l_norm (float), G_norm (float), Gp_norm (float). One row per (radius, distribution, surface) combination; radii cover [1,2,5,10,20,30,40,50] nm.
- Scoring: scored by hidden verifier

### Step 4: Compute normalized transverse bulk modulus for non-circular nanopores
- Role: scored
- Action: Using the FFT solver, simulate nanopores with non-circular cross-sections (4-oscillation and 8-oscillation shapes defined by radius function with A=0.4R0) under surface A and f=0.2. Compute the effective transverse bulk modulus k* and normalize by the matrix bulk modulus κ0. Write the results to step_02_nanopores_noncircular.csv.
- Output file: `/app/outputs/step_02_nanopores_noncircular.csv`
- Format: csv
- Contract: Columns: R0 (float, nm), shape (string, '4_oscillations'|'8_oscillations'), k_norm (float). One row per (R0, shape); R0 covers [1,2,5,10,20,30,40,50] nm.
- Scoring: scored by hidden verifier

### Step 5: Compute normalized effective moduli for circular nanofibers
- Role: scored
- Action: Using the FFT solver, simulate cylindrical nanofibers with circular cross-sections under square, hexagonal, and random distributions. Use fiber radii 1,2,5,10,20,30,40,50 nm, f=0.3, E0=2Ei=70 GPa, ν0=νi=0.25, Esi/E0=1.1636e-9 m, νsi=0.45. Compute the six Hill moduli and normalize by the corresponding matrix moduli (k*/k0, m*/μ0, n*/μ0, l*/μ0, G*/μ0, G'*/μ0). For the random distribution, report at least one realization and include a realization column. Write the results to step_03_nanofibers.csv.
- Output file: `/app/outputs/step_03_nanofibers.csv`
- Format: csv
- Contract: Columns: radius (float, nm), distribution (string, 'square'|'hexagonal'|'random'), realization (integer, 1 if only one realization), k_norm (float), m_norm (float), n_norm (float), l_norm (float), G_norm (float), Gp_norm (float). One row per (radius, distribution, realization); radii cover [1,2,5,10,20,30,40,50] nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_nanopores_circular.csv`
- `/app/outputs/step_02_nanopores_noncircular.csv`
- `/app/outputs/step_03_nanofibers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_nanopores_circular.csv
- path: `/app/outputs/step_01_nanopores_circular.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized effective moduli (k*/k_C*, m*/m_C*, n*/n_C*, l*/l_C*, G*/G_C*, G'*/G'_C*) for circular nanopores. One row per (radius, distribution, surface). The hidden checker compares these values against reference data with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `distribution`, `surface`, `k_norm`, `m_norm`, `n_norm`, `l_norm`, `G_norm`, `Gp_norm`
  - `units`:
    - `radius`: nm
    - `k_norm`: dimensionless
    - `m_norm`: dimensionless
    - `n_norm`: dimensionless
    - `l_norm`: dimensionless
    - `G_norm`: dimensionless
    - `Gp_norm`: dimensionless

### step_02_nanopores_noncircular.csv
- path: `/app/outputs/step_02_nanopores_noncircular.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized transverse bulk modulus k*/κ0 for non-circular nanopores. One row per (R0, shape). The hidden checker compares against reference values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `R0`, `shape`, `k_norm`
  - `units`:
    - `R0`: nm
    - `k_norm`: dimensionless

### step_03_nanofibers.csv
- path: `/app/outputs/step_03_nanofibers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized effective moduli (k*/k0, m*/μ0, n*/μ0, l*/μ0, G*/μ0, G'*/μ0) for circular nanofibers. One row per (radius, distribution, realization). The hidden checker compares against reference values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `radius`, `distribution`, `realization`, `k_norm`, `m_norm`, `n_norm`, `l_norm`, `G_norm`, `Gp_norm`
  - `units`:
    - `radius`: nm
    - `k_norm`: dimensionless
    - `m_norm`: dimensionless
    - `n_norm`: dimensionless
    - `l_norm`: dimensionless
    - `G_norm`: dimensionless
    - `Gp_norm`: dimensionless

Notes: All normalized moduli are dimensionless. The checker uses a reference implementation (N_k=128) to recompute the same moduli and compares with relative tolerances (tighter for well-conditioned moduli, looser for l* and G*). For the random nanofiber distribution, at least one realization is required; the checker accepts a single realization with relaxed tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_nanopores_circular.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "distribution",
          "surface",
          "k_norm",
          "m_norm",
          "n_norm",
          "l_norm",
          "G_norm",
          "Gp_norm"
        ],
        "units": {
          "radius": "nm",
          "k_norm": "dimensionless",
          "m_norm": "dimensionless",
          "n_norm": "dimensionless",
          "l_norm": "dimensionless",
          "G_norm": "dimensionless",
          "Gp_norm": "dimensionless"
        }
      },
      "description": "Normalized effective moduli (k*/k_C*, m*/m_C*, n*/n_C*, l*/l_C*, G*/G_C*, G'*/G'_C*) for circular nanopores. One row per (radius, distribution, surface). The hidden checker compares these values against reference data with appropriate tolerances."
    },
    {
      "file": "step_02_nanopores_noncircular.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R0",
          "shape",
          "k_norm"
        ],
        "units": {
          "R0": "nm",
          "k_norm": "dimensionless"
        }
      },
      "description": "Normalized transverse bulk modulus k*/κ0 for non-circular nanopores. One row per (R0, shape). The hidden checker compares against reference values with appropriate tolerances."
    },
    {
      "file": "step_03_nanofibers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius",
          "distribution",
          "realization",
          "k_norm",
          "m_norm",
          "n_norm",
          "l_norm",
          "G_norm",
          "Gp_norm"
        ],
        "units": {
          "radius": "nm",
          "k_norm": "dimensionless",
          "m_norm": "dimensionless",
          "n_norm": "dimensionless",
          "l_norm": "dimensionless",
          "G_norm": "dimensionless",
          "Gp_norm": "dimensionless"
        }
      },
      "description": "Normalized effective moduli (k*/k0, m*/μ0, n*/μ0, l*/μ0, G*/μ0, G'*/μ0) for circular nanofibers. One row per (radius, distribution, realization). The hidden checker compares against reference values with appropriate tolerances."
    }
  ],
  "notes": "All normalized moduli are dimensionless. The checker uses a reference implementation (N_k=128) to recompute the same moduli and compares with relative tolerances (tighter for well-conditioned moduli, looser for l* and G*). For the random nanofiber distribution, at least one realization is required; the checker accepts a single realization with relaxed tolerance."
}
```

## How you are scored
A hidden verifier independently checks your submitted CSV files. Each file is compared against gold‑standard values produced by a high‑resolution reference implementation of the same FFT method and the same physical parameters. The comparison uses relative tolerances that account for the numerical spread expected in a correct re‑implementation. The three files are scored independently, and the final reward is a weighted average (with each file contributing roughly one‑third of the total reward). Simply reporting the expected numbers is insufficient; the verifier recomputes the expected moduli from the protocol, so a converged and correct solver is required to achieve a high score.
