# Lattice thermal conductivity calculation for nanostructured composite using effective-mass Landauer model

## Problem background
Thermoelectric materials convert heat to electricity, and their figure of merit ZT benefits from low lattice thermal conductivity. Embedding silicon nanowires in a SiGe₀.₃ matrix can strongly suppress phonon transport through boundary scattering while preserving electrical performance. This task investigates the lattice thermal conductivity of such a SiNW–SiGe₀.₃ composite and compares it to that of bulk silicon. The central open question is: what is the resulting lattice thermal conductivity of the composite, and how large is the reduction compared to bulk Si?

## Approach
The study uses an effective‑mass, linear‑elastic, Landauer‑transport framework. Electron band structures are obtained from the effective‑mass Schrödinger equation under Bloch periodicity; phonon dispersions come from the elastodynamic wave equation with cubic elastic constants. Both are solved with a finite‑element method on the appropriate unit cell. From the dispersions, the number of conducting channels per unit area M(E) is derived for electrons and phonons.

For the lattice thermal conductivity, the Landauer formula relates M(E) and the phonon mean free path. The bulk‑Si phonon mean free path is calibrated by matching the computed bulk thermal conductivity to an experimental reference value from the literature. For the composite, boundary scattering is incorporated via Matthiessen’s rule, taking the nanowire diameter as the internal scattering length. The lattice thermal conductivity of the composite is then computed and compared to bulk Si. The target composite is a square superlattice of SiNWs with radius 5 nm and centre‑to‑centre spacing 15 nm embedded in SiGe₀.₃.

## Reproduction target
Compute and report the following for the composite with radius 5 nm and spacing 15 nm:
- lattice thermal conductivity of bulk Si, κ_ph_bulk (W/mK)
- lattice thermal conductivity of the composite, κ_ph_composite (W/mK)
- reduction ratio κ_ph_bulk / κ_ph_composite (dimensionless)

Write these three numbers in the JSON file `/app/outputs/results.json` with keys `kappa_ph_bulk_Si`, `kappa_ph_composite`, and `kappa_ph_reduction_ratio`.

## Assets

- Elastic constants, effective masses, and densities for Si and SiGe0.3
- Bulk Si experimental thermal conductivity (reference value): 10.1038/nature06381
- Finite-element solver for PDEs (e.g., FEniCS, deal.II): fenics

## Workflow steps

### Step 1: Define material parameters
- Role: process
- Action: Create a file with all required material constants: for Si and SiGe0.3, the elastic constants C11, C12, C44 (GPa), effective masses (longitudinal, transverse, heavy hole, light hole), band offsets, and mass densities. Use the values provided in the task instruction.
- Evidence: `/app/outputs/params.json`

### Step 2: Compute bulk Si phonon dispersion and conducting channels
- Role: process
- Action: Solve the elastodynamic wave equation for bulk Si with cubic symmetry using a finite-element method (or equivalent) on a unit cell to obtain phonon eigenfrequencies over the irreducible Brillouin zone. From the dispersion, compute the number of phonon conducting channels per unit area Mph,bulk as a function of energy.
- Evidence: `/app/outputs/bulk_phonon_channels.json`

### Step 3: Calibrate average phonon mean free path
- Role: process
- Action: Using the bulk Mph,bulk and the Landauer formula for lattice thermal conductivity, assume an average phonon mean free path and adjust it until the computed bulk Si thermal conductivity matches the experimental reference value of 150 W/mK. Output the calibrated backscattering mean free path (in nm) and the corresponding conventional mean free path.
- Evidence: `/app/outputs/bulk_mfp.json`

### Step 4: Compute composite phonon dispersion and conducting channels
- Role: process
- Action: Solve the elastodynamic wave equation for the SiNW-SiGe0.3 composite assuming a square superlattice unit cell with SiNW radius 5 nm and spacing 15 nm. Use the same finite-element method with position-dependent elastic constants and mass densities. Obtain phonon eigenfrequencies and derive the number of phonon conducting channels per unit area Mph,comp as a function of energy.
- Evidence: `/app/outputs/composite_phonon_channels.json`

### Step 5: Compute effective phonon mean free path for composite
- Role: process
- Action: Apply Matthiessen's rule to combine the calibrated bulk mean free path with an internal scattering length equal to the nanowire diameter (10 nm). Compute the effective conventional mean free path and then the effective backscattering mean free path.
- Evidence: `/app/outputs/effective_mfp.json`

### Step 6: Compute lattice thermal conductivity and reduction ratio
- Role: scored (load-bearing)
- Action: Use the Landauer formula with the phonon conducting channels and the effective mean free path to compute the lattice thermal conductivity of bulk Si and the composite. Calculate the reduction ratio (κ_ph_bulk / κ_ph_composite). Write a JSON file results.json containing kappa_ph_bulk_Si (W/mK), kappa_ph_composite (W/mK), and kappa_ph_reduction_ratio (dimensionless).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"kappa_ph_bulk_Si": number, "kappa_ph_composite": number, "kappa_ph_reduction_ratio": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed lattice thermal conductivity values. The checker validates that kappa_ph_composite is within an expected range and that kappa_ph_reduction_ratio meets a required threshold, with credit increasing as composite conductivity is lower and ratio is higher.
- schema:
  - `type`: object
  - `required`: `kappa_ph_bulk_Si`, `kappa_ph_composite`, `kappa_ph_reduction_ratio`
  - `properties`:
    - `kappa_ph_bulk_Si`:
      - `type`: number
      - `units`: W/mK
    - `kappa_ph_composite`:
      - `type`: number
      - `units`: W/mK
    - `kappa_ph_reduction_ratio`:
      - `type`: number
      - `dimensionless`: True

Notes: The composite geometry (radius 5 nm, spacing 15 nm) and the internal scattering length (nanowire diameter 10 nm) are fixed to enable a deterministic reproduction. The checker uses hidden gold values and thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "kappa_ph_bulk_Si",
          "kappa_ph_composite",
          "kappa_ph_reduction_ratio"
        ],
        "properties": {
          "kappa_ph_bulk_Si": {
            "type": "number",
            "units": "W/mK"
          },
          "kappa_ph_composite": {
            "type": "number",
            "units": "W/mK"
          },
          "kappa_ph_reduction_ratio": {
            "type": "number",
            "dimensionless": true
          }
        }
      },
      "description": "Computed lattice thermal conductivity values. The checker validates that kappa_ph_composite is within an expected range and that kappa_ph_reduction_ratio meets a required threshold, with credit increasing as composite conductivity is lower and ratio is higher."
    }
  ],
  "notes": "The composite geometry (radius 5 nm, spacing 15 nm) and the internal scattering length (nanowire diameter 10 nm) are fixed to enable a deterministic reproduction. The checker uses hidden gold values and thresholds."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and compares the reported values to reference expectations. It checks that `kappa_ph_composite` is within an accepted tolerance of the expected nanostructured value and that `kappa_ph_reduction_ratio` meets or exceeds a predetermined threshold. `kappa_ph_bulk_Si` is also checked for consistency with the calibration reference. The verifier computes a reward between 0 and 1. The reward is monotonic in the quality of the result: a higher reduction ratio (lower composite conductivity) never reduces the score; meeting or beating the required threshold earns full credit. The exact tolerances and thresholds are hidden – the only way to succeed is to faithfully execute the described workflow.
