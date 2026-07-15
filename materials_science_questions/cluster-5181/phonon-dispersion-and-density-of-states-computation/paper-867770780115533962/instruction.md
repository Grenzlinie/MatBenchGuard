# Phonon Frequency Estimation from PIMD Kubo-Transformed Correlators for 1D Anharmonic Models and Diamond

## Problem background
Vibrational properties of solids and molecules, including anharmonic effects and nuclear quantum fluctuations, are fundamental for understanding thermal expansion, specific heat, and Raman/infrared spectra. The accurate prediction of phonon frequencies in strongly anharmonic systems remains challenging, especially when quantum effects are important. This work addresses the problem of extracting anharmonic phonon frequencies from quantum statistical simulations. The target result is the computation of two distinct phonon frequency estimates—one associated with force-force correlations and one with displacement-displacement correlations—and their ratio, which quantifies anharmonicity. These quantities are evaluated for a set of one-dimensional anharmonic model potentials and for the Raman-active mode of diamond, providing insight into how anharmonicity and quantum effects renormalize vibrational spectra.

## Approach
The core idea is to use path integral molecular dynamics (PIMD) with a Langevin thermostat to sample the quantum thermal distribution of nuclei. From the trajectories, zero-time Kubo-transformed correlation functions of atomic forces and displacements are computed. Two generalized eigenvalue problems are then solved:

- The force-force estimator (based on the bead-averaged Kubo-transformed force covariance) yields the fundamental phonon frequencies (ω_FF).
- The displacement-displacement estimator (based on the bead-averaged Kubo-transformed displacement covariance) gives the lowest-energy phonon excitation energies (ω_δxδx).

The ratio γ = ω_δxδx / ω_FF serves as a dimensionless measure of anharmonicity.

For 1D model potentials (Morse, quartic, symmetric double well) the PIMD code is self-implemented. For diamond, an ab initio PIMD simulation is performed using Quantum ESPRESSO with the PBE exchange-correlation functional and an ultrasoft pseudopotential. The diamond simulation targets the Gamma-point phonon mode. In both cases, the generalized eigenvalue approach is employed because it converges faster and with less time-step bias than the standard normal-mode equations. The computed frequencies and anharmonicity ratios are collected into a single JSON file.

## Reproduction target
Compute the phonon frequencies ω_FF (from force-force correlators) and ω_δxδx (from displacement-displacement correlators) and the anharmonicity ratio γ = ω_δxδx / ω_FF for the following systems:

- 1D model potentials at 20 K: Morse (a_m = 0.2, 0.4, 0.6, 0.8), quartic (c_q = 0.01, 0.1, 1.0), and symmetric double well (c_0 = 0.05, 0.1, 0.3). The spring constant is k = 0.183736 a.u., the particle mass equals the hydrogen atom mass, and the number of beads is 80 (for Morse and quartic) and larger for the double well to ensure convergence.
- The diamond crystal at the Gamma point, at 300 K, using a 2×2×2 supercell (64 atoms) and PIMD with 12 beads.

All results must be written to the file `/app/outputs/phonon_results.json` with the structure described in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Carbon ultrasoft pseudopotential (PBE): https://www.quantum-espresso.org/pseudopotentials
- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: PIMD simulations for 1D model potentials
- Role: process
- Action: Implement a PIMD algorithm with a Langevin thermostat (PIOUD protocol) for a single particle in 1D. Run simulations for each potential (Morse with a_m=0.2,0.4,0.6,0.8; quartic with c_q=0.01,0.1,1.0; symmetric double well with c_0=0.05,0.1,0.3) using parameters: k=0.183736 a.u., mass equal to hydrogen atom mass, temperature T=20 K, bead number P=80 for Morse/quartic and appropriate P for double well, time step ~0.5 fs, until convergence (approx. 4 ps). Save the full trajectory (bead positions, velocities, forces).
- Evidence: `/app/outputs/1d_pimd.log`

### Step 2: Ab initio PIMD simulation of diamond
- Role: process
- Action: Set up a 2x2x2 supercell of diamond (64 atoms). Use Quantum ESPRESSO with PBE exchange-correlation functional and ultrasoft pseudopotential. Perform a PIMD simulation at T=300 K with P=12 beads, time step Δt=0.75 fs, for about 34 ps. Use a plane-wave cutoff of 60 Ry (480 Ry for charge) and a 2x2x2 k-point mesh. Apply a Langevin thermostat (PIOUD). Save the full trajectory (bead positions, forces).
- Evidence: `/app/outputs/diamond_pimd.log`

### Step 3: Phonon frequency estimation from PIMD trajectories
- Role: scored (load-bearing)
- Action: From the 1D trajectories, compute the bead-averaged Kubo-transformed force-force and displacement-displacement correlation matrices. Solve the generalized eigenvalue problems to obtain ω_FF and ω_δxδx and the ratio γ for each potential/parameter. From the diamond trajectory, construct supercell correlation matrices, Fourier-transform to q-space, symmetrize, and extract frequencies at the Gamma point. Obtain ω_FF, ω_δxδx, and γ for diamond. Output all results to a single JSON file.
- Output file: `/app/outputs/phonon_results.json`
- Format: json
- Contract: Final phonon frequencies (ω_FF, ω_δxδx) and anharmonicity ratio γ for all 1D models and diamond Gamma point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_results.json
- path: `/app/outputs/phonon_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon frequencies (omega_FF in cm^-1, omega_dxdx in cm^-1) and anharmonicity ratio gamma (dimensionless) for 1D model potentials and for diamond Gamma point. The 1D potentials include Morse_a0.2 to a0.8, Quartic_c0.01/c0.1/c1.0, SymmetricDoubleWell_c0.05/c0.1/c0.3.
- schema:
  - `type`: object
  - `required`: `1d_potentials`, `diamond_gamma`
  - `properties`:
    - `1d_potentials`:
      - `type`: object
      - `additionalProperties`:
        - `type`: object
        - `properties`:
          - `omega_FF`:
            - `type`: number
            - `unit`: cm^-1
          - `omega_dxdx`:
            - `type`: number
            - `unit`: cm^-1
          - `gamma`:
            - `type`: number
            - `unit`: dimensionless
    - `diamond_gamma`:
      - `type`: object
      - `properties`:
        - `omega_FF`:
          - `type`: number
          - `unit`: cm^-1
        - `omega_dxdx`:
          - `type`: number
          - `unit`: cm^-1
        - `gamma`:
          - `type`: number
          - `unit`: dimensionless

Notes: The checker compares each reported frequency and ratio against hidden gold values from the paper's tables. No tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "1d_potentials",
          "diamond_gamma"
        ],
        "properties": {
          "1d_potentials": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "properties": {
                "omega_FF": {
                  "type": "number",
                  "unit": "cm^-1"
                },
                "omega_dxdx": {
                  "type": "number",
                  "unit": "cm^-1"
                },
                "gamma": {
                  "type": "number",
                  "unit": "dimensionless"
                }
              }
            }
          },
          "diamond_gamma": {
            "type": "object",
            "properties": {
              "omega_FF": {
                "type": "number",
                "unit": "cm^-1"
              },
              "omega_dxdx": {
                "type": "number",
                "unit": "cm^-1"
              },
              "gamma": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          }
        }
      },
      "description": "Phonon frequencies (omega_FF in cm^-1, omega_dxdx in cm^-1) and anharmonicity ratio gamma (dimensionless) for 1D model potentials and for diamond Gamma point. The 1D potentials include Morse_a0.2 to a0.8, Quartic_c0.01/c0.1/c1.0, SymmetricDoubleWell_c0.05/c0.1/c0.3."
    }
  ],
  "notes": "The checker compares each reported frequency and ratio against hidden gold values from the paper's tables. No tolerances are revealed here."
}
```

## How you are scored
The workflow consists of multiple scored and process steps. Each scored step produces a file under `/app/outputs` that is independently evaluated by a hidden verifier. The verifier reads the produced JSON file and compares the reported frequencies (ω_FF and ω_δxδx) and ratios (γ) against reference values derived from exact solutions (for the 1D models) and from the known Raman shift (for diamond). The comparison uses a threshold-or-better policy: for each quantity, if the absolute deviation from the reference does not exceed a pre-defined tolerance (not disclosed here), full credit is awarded; otherwise the credit decreases as the deviation grows. The final score is the weighted sum of the scores of all evaluated quantities. Simply reporting the reference values without performing the required simulations will be detected because the verifier checks the consistency of the submitted artifact with the expected structural properties of the simulation outputs; only genuinely executed PIMD simulations and correct post-processing yield results that fall within the acceptance windows.
