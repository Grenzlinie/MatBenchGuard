# Microwave filter S-parameter analysis using semi-analytical spectral elements

## Problem background
Electromagnetic modelling of layered structures—such as microwave filters, waveguide discontinuities, and electronic packaging interconnects—is fundamental for integrated optics, geophysics, and high-speed circuit design. The finite-element method (FEM) can model arbitrary cross‑sections, but a full three‑dimensional discretization of a long layered structure produces an enormous system of equations. A semianalytical spectral element method (SEM) exploits piecewise homogeneity along the longitudinal direction by treating each layer (or substructure) as a separate region and solving the wave propagation with a combination of 2‑D spectral elements and a high‑precision integration technique, aiming to deliver high accuracy with far fewer unknowns. This task reproduces the SEM for a 10‑cell microwave filter and investigates how the reflection and transmission coefficients depend on frequency and interpolation order.

## Approach
The workflow mirrors the semianalytical SEM. The filter is divided into substructures that are each homogeneous along the longitudinal (z) direction. The cross‑section of each substructure is discretized with 2‑D vector and scalar spectral elements built from Gauss–Lobatto–Legendre (GLL) polynomials. Transverse element mass and stiffness matrices (M1–M4) are assembled by numerical integration on the reference element. Those matrices are combined into Lagrangian system matrices K11 and K22; a Legendre transformation converts the problem to a Hamiltonian system with matrices B and D. The key longitudinal integration is performed via the Riccati‑equation–based high‑precision integration (HPI) method, which yields the stiffness matrices for each substructure with machine‑level accuracy. The substructure stiffnesses are assembled into a global block‑tridiagonal system, corresponding to the interfaces between cells. After imposing the TE10 incident wave as an excitation on the first interface, the system is solved with the block Thomas algorithm to obtain the transverse field at every interface; the reflection and transmission coefficients (S‑parameters) are extracted from the fields. A reference solution is obtained by running the same SEM with a very high interpolation order (or a finer mesh) to provide a converged baseline. Spectral convergence is assessed by repeating the SEM for orders 3 through 8 and comparing the resulting S‑parameters to that reference.

## Reproduction target
Compute the |S11| and |S12| magnitudes for the 10‑cell microwave filter (each cell composed of three substructures, with six 2‑D spectral elements on the cross‑section, dimensions as shown in a provided geometry sketch) under TE10 excitation, covering 8.0–9.0 GHz in 0.1 GHz steps, using third‑order spectral elements. Save these as sc_s11_s12.csv. Then, for interpolation orders 3 through 8, repeat the SEM and compute the maximum relative error of |S11| and |S12| across the band relative to the high‑order reference; also record the number of unknowns, approximate memory usage (MB), and CPU time (minutes). Save these metrics as convergence_table.csv. Both CSVs will be examined by the verifier.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Mesh generation and transverse matrix assembly
- Role: process
- Action: Generate the 2-D spectral element mesh for each substructure (each of the ten cells divided into three substructures, six spectral elements per cross‑section) using Gauss–Lobatto–Legendre (GLL) basis functions. Assemble the transverse element matrices M1, M2, M3 and M4 by integrating over each element as described in the method. This creates the fundamental building blocks used by all subsequent SEM runs.
- Evidence: `/app/outputs/transverse_matrices_info.json`

### Step 2: Compute reference S‑parameters using a high‑order converged SEM
- Role: process
- Action: Run the complete semianalytical SEM pipeline (Lagrangian matrices, Hamiltonian transformation, high‑precision integration, global assembly, block Thomas solver) for a high interpolation order (e.g., order 12) and/or a refined mesh to obtain a converged reference set of reflection and transmission coefficient magnitudes (|S11|, |S12|) across 8.0–9.0 GHz. This reference will serve as the ground truth for the convergence study.
- Evidence: `/app/outputs/reference_s11_s12.csv`

### Step 3: S‑parameters for 3rd‑order SEM (primary result)
- Role: scored (load-bearing)
- Action: Run the semianalytical SEM pipeline for 3rd‑order spectral elements. For frequencies from 8.0 to 9.0 GHz in 0.1 GHz steps (or similar fine sampling), extract the reflection and transmission coefficients (|S11|, |S12|) and write them to the output CSV.
- Output file: `/app/outputs/sc_s11_s12.csv`
- Format: csv
- Contract: CSV with columns: frequency (GHz, float), S11_mag (float), S12_mag (float). One row per frequency covering 8.0–9.0 GHz.
- Scoring: scored by hidden verifier

### Step 4: Run SEM for orders 3–8 and compute relative errors
- Role: process
- Action: For each interpolation order from 3 to 8, run the semianalytical SEM pipeline and obtain the |S11| and |S12| magnitudes across the same frequency band. For each order, compute the maximum absolute relative error of |S11| and |S12| across all frequencies, taking the reference solution from step 2 as the baseline. Also record the total number of unknowns, the approximate memory usage (in MB), and the CPU time (in minutes) for each order.
- Evidence: `/app/outputs/convergence_data.json`

### Step 5: Convergence table
- Role: scored (load-bearing)
- Action: Write the convergence metrics (order, unknowns, memory_MB, cpu_time_min, rel_error_S11, rel_error_S12) to a CSV file.
- Output file: `/app/outputs/convergence_table.csv`
- Format: csv
- Contract: CSV with columns: order (int), unknowns (int), memory_MB (float), cpu_time_min (float), rel_error_S11 (float), rel_error_S12 (float). One row per order, from 3 to 8 inclusive.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sc_s11_s12.csv`
- `/app/outputs/convergence_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sc_s11_s12.csv
- path: `/app/outputs/sc_s11_s12.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed |S11| and |S12| magnitudes for the microwave filter at frequencies 8.0–9.0 GHz, using the semianalytical SEM with 3rd‑order spectral elements. The checker compares these values to the paper’s published reference data with a fixed absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `S11_mag`, `S12_mag`
  - `units`:
    - `frequency`: GHz
    - `S11_mag`: dimensionless
    - `S12_mag`: dimensionless

### convergence_table.csv
- path: `/app/outputs/convergence_table.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Spectral convergence metrics for orders 3–8. The checker scores rel_error_S11 and rel_error_S12 by comparing them to the paper’s published values with a generous relative tolerance (agent values within a factor of 2 of the gold are accepted). Collective monotonic decrease with order is also verified.
- schema:
  - `type`: table
  - `required_columns`: `order`, `unknowns`, `memory_MB`, `cpu_time_min`, `rel_error_S11`, `rel_error_S12`
  - `units`:
    - `order`: dimensionless
    - `unknowns`: count
    - `memory_MB`: MB
    - `cpu_time_min`: minutes
    - `rel_error_S11`: dimensionless
    - `rel_error_S12`: dimensionless

Notes: The task reproduces the microwave filter example from the paper. The agent must implement the complete semianalytical SEM pipeline; no external datasets or third‑party solvers are required. The reference solution used for the convergence study can be obtained by running the same SEM with a much higher interpolation order (e.g., 12) and/or a finer mesh, as a computationally efficient alternative to a dense 3‑D FEM.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sc_s11_s12.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "S11_mag",
          "S12_mag"
        ],
        "units": {
          "frequency": "GHz",
          "S11_mag": "dimensionless",
          "S12_mag": "dimensionless"
        }
      },
      "description": "Computed |S11| and |S12| magnitudes for the microwave filter at frequencies 8.0–9.0 GHz, using the semianalytical SEM with 3rd‑order spectral elements. The checker compares these values to the paper’s published reference data with a fixed absolute tolerance."
    },
    {
      "file": "convergence_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "order",
          "unknowns",
          "memory_MB",
          "cpu_time_min",
          "rel_error_S11",
          "rel_error_S12"
        ],
        "units": {
          "order": "dimensionless",
          "unknowns": "count",
          "memory_MB": "MB",
          "cpu_time_min": "minutes",
          "rel_error_S11": "dimensionless",
          "rel_error_S12": "dimensionless"
        }
      },
      "description": "Spectral convergence metrics for orders 3–8. The checker scores rel_error_S11 and rel_error_S12 by comparing them to the paper’s published values with a generous relative tolerance (agent values within a factor of 2 of the gold are accepted). Collective monotonic decrease with order is also verified."
    }
  ],
  "notes": "The task reproduces the microwave filter example from the paper. The agent must implement the complete semianalytical SEM pipeline; no external datasets or third‑party solvers are required. The reference solution used for the convergence study can be obtained by running the same SEM with a much higher interpolation order (e.g., 12) and/or a finer mesh, as a computationally efficient alternative to a dense 3‑D FEM."
}
```

## How you are scored
A hidden verifier reads your two scored output files. It compares the S‑parameters in sc_s11_s12.csv to independently computed reference values for the filter; the closeness within an allowed absolute tolerance determines the score. For convergence_table.csv, the verifier checks that the relative errors decrease monotonically with increasing order and that the error magnitudes are consistent with a rapid (spectral) convergence, comparing them against a hidden gold set. The final reward is a weighted average over the two artifacts. Reporting numbers without running the actual SEM pipeline will not pass the verifier’s checks.
