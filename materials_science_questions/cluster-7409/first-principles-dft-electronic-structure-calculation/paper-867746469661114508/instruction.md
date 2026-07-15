# Optical Conductivity Computation for Co-doped Anatase TiO2

## Problem background
Room-temperature ferromagnetism in Co-doped anatase TiO₂ has attracted considerable attention due to its potential applications in spintronics. Understanding the electronic structure and optical properties is crucial for explaining the observed ferromagnetic behaviour and the role of oxygen vacancies. First-principles density functional theory (DFT) offers a direct way to compute how doping concentration and vacancy placement modify the electronic states and the resulting optical response. In the linear optical conductivity spectrum, the absorption edge and the position of the first strong peak are sensitive to the local environment around the dopant, making it possible to discriminate between different vacancy configurations. This task requires computing these spectral features for several well-defined structural models of Co-doped anatase TiO₂.

## Approach
The calculation follows a DFT workflow within the local spin density approximation (LSDA), using a plane-wave pseudopotential implementation. Four supercell models of anatase TiO₂ are constructed to represent different doping cases: (i) 2×2×1 supercell with one Ti replaced by Co (x ≈ 0.0417, no oxygen vacancy); (ii) 2×3×1 supercell with one Co (x ≈ 0.0625, no vacancy); (iii) same as (ii) but with one oxygen atom removed from the CoO₆ octahedron (vacancy near Co); (iv) same as (ii) with one oxygen removed from a neighbouring TiO₆ octahedron (vacancy near Ti). The lattice parameters are taken from the experimental anatase structure (a = 3.782 Å, c = 9.502 Å). For each configuration, the workflow proceeds through geometry optimisation (forces converged to a low threshold), a self-consistent spin-polarised LSDA ground-state calculation, and finally the computation of the optical conductivity. The imaginary part of the dielectric function, ε₂(ω), is obtained from the electric-dipole matrix elements between Kohn-Sham states; the real part ε₁(ω) is derived via Kramers‑Kronig transformation. The linear optical conductivity is then given by σ(ω) = ‑i ω (ε(ω) – 1) / (4π). A rigid scissor shift is applied to the conduction bands to align the theoretical absorption onset with the experimental band gap of 3.2 eV. After the shift, the absorption edge is defined as the lowest photon energy where σ(ω) exceeds 0.1 × max(σ) in the 0–6 eV range, and the first strong peak is the highest local maximum of σ(ω) above the absorption edge and below 6 eV. All DFT steps can be carried out with an open-source plane-wave pseudopotential code such as Quantum ESPRESSO.

## Reproduction target
The objective is to generate a CSV file that reports, for each of the four configurations listed above, the scissor-corrected absorption edge (in eV) and the position of the first strong peak (in eV). The reported values must result from a full re-implementation of the LSDA+scissor procedure, including the construction of the supercell models, geometry relaxation, spin-polarised SCF calculations, and the optical conductivity analysis. No external dataset is required; the only input is the publicly available anatase TiO₂ crystal structure. The task is considered successful if the produced features are consistent with the expected physical trends and numerical ranges for these configurations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Anatase TiO2 crystal structure: https://materialsproject.org/materials/mp-390/

## Workflow steps

### Step 1: Construct supercell models
- Role: process
- Action: Build four atomic configurations of Co-doped anatase TiO2 using supercells: (a) 2×2×1, one Ti replaced by Co (x=0.0417, δ=0); (b) 2×3×1, one Ti replaced by Co (x=0.0625, δ=0); (c) same as (b) with one O removed from CoO6 octahedron (vacancy near Co); (d) same as (b) with one O removed from a neighboring TiO6 octahedron (vacancy near Ti). Use anatase lattice parameters a=3.782 Å, c=9.502 Å. Save the structures for subsequent DFT steps.
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: Geometry optimization
- Role: process
- Action: Perform LSDA geometry optimization for each of the four configurations using plane-wave pseudopotential DFT. Relax atomic positions until forces are sufficiently converged.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 3: Spin-polarized LSDA electronic structure calculation
- Role: process
- Action: Run a self-consistent spin-polarized LSDA calculation for each optimized configuration to obtain the Kohn-Sham eigenstates and energies needed for the dielectric function. Use appropriate k-point sampling.
- Evidence: `/app/outputs/scf_output.log`

### Step 4: Scissor-corrected optical conductivity
- Role: scored (load-bearing)
- Action: Using the eigenstates from step_03, compute the imaginary part of the dielectric function ε₂(ω) in the electric-dipole approximation. Obtain ε₁(ω) via Kramers–Kronig transformation, then compute the linear optical conductivity σ(ω) = -i ω (ε(ω) - 1) / (4π). Apply a rigid scissor shift to the conduction bands so that the onset of σ(ω) matches the experimental absorption edge of 3.2 eV. For each configuration, determine the absorption edge as the lowest photon energy where σ(ω) exceeds 0.1 × max(σ) in the range 0–6 eV, and the first strong peak as the highest local maximum of σ(ω) above the absorption edge, below 6 eV. Write the results to optical_conductivity_results.csv.
- Output file: `/app/outputs/optical_conductivity_results.csv`
- Format: csv
- Contract: columns: configuration (str, e.g. 'x0.0417_no_vac', 'x0.0625_no_vac', 'x0.0625_vac_Co', 'x0.0625_vac_Ti'), absorption_edge_eV (float), first_strong_peak_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_conductivity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_conductivity_results.csv
- path: `/app/outputs/optical_conductivity_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed optical conductivity features (absorption edge and first strong peak) for the four Co-doped anatase TiO2 configurations. The absorption edge is defined as the energy where σ exceeds 0.1 of its maximum in 0–6 eV; the first strong peak is the highest local maximum above that edge, below 6 eV.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `absorption_edge_eV`, `first_strong_peak_eV`
  - `units`:
    - `absorption_edge_eV`: eV
    - `first_strong_peak_eV`: eV

Notes: The scored output is compared against the paper's LSDA optical conductivity values within tolerances and checked for correct vacancy-induced relative trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_conductivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "absorption_edge_eV",
          "first_strong_peak_eV"
        ],
        "units": {
          "absorption_edge_eV": "eV",
          "first_strong_peak_eV": "eV"
        }
      },
      "description": "Computed optical conductivity features (absorption edge and first strong peak) for the four Co-doped anatase TiO2 configurations. The absorption edge is defined as the energy where σ exceeds 0.1 of its maximum in 0–6 eV; the first strong peak is the highest local maximum above that edge, below 6 eV."
    }
  ],
  "notes": "The scored output is compared against the paper's LSDA optical conductivity values within tolerances and checked for correct vacancy-induced relative trends."
}
```

## How you are scored
A hidden verifier inspects the submitted optical_conductivity_results.csv file. It evaluates the reported absorption edge and first strong peak for each configuration by comparing them against a set of reference values that capture the expected LSDA-based spectral features. The verifier accounts for the typical variability introduced by different DFT implementations, pseudopotential choices, and convergence settings: reported values within a reasonable tolerance of the reference receive full credit, while deviations larger than the tolerance receive reduced or no credit. In addition, the verifier checks whether the relative shifts between configurations follow the physically required trends — for example, how the presence of an oxygen vacancy near Co vs. near Ti affects the absorption edge and the first peak position. The final reward is a weighted combination of the accuracy of the individual energy values and the correctness of the qualitative ordering. No additional workload beyond the prescribed step sequence is assessed.
