# Thermoelectric figure-of-merit and lattice thermal conductivity of a half-Heusler material

## Problem background
Half-Heusler compounds are promising thermoelectric materials owing to their good electronic transport properties, but their typically high lattice thermal conductivity limits their figure-of-merit ZT. It is predicted that in the half-Heusler compound BiBaK, light K atoms rattle inside a cage formed by the heavier Bi and Ba atoms, leading to intrinsically low lattice thermal conductivity. Combined with favourable electronic transport, this could yield a high thermoelectric performance. The task is to compute the key transport quantities of BiBaK using first‑principles density functional theory and Boltzmann transport theory, thereby quantifying its thermoelectric potential.

## Approach
The workflow uses a chain of open‑source computational codes to reproduce the result entirely from the crystal structure and physical theory. First, the electronic band structure of BiBaK is obtained via density functional theory (DFT) using a hybrid functional with spin‑orbit coupling, from which the band gap, density‑of‑states effective masses, and deformation potential constants are extracted; the elastic constant is also computed via strained‑cell calculations. Second, harmonic phonon properties are obtained using the finite‑displacement method and the Phonopy package to compute second‑order interatomic force constants and the resulting phonon dispersion and group velocities. Third, third‑order force constants are generated for anharmonic phonon scattering. Fourth, the lattice thermal conductivity is computed by solving the phonon Boltzmann transport equation with the ShengBTE code. Fifth, electronic transport coefficients (Seebeck coefficient, electrical conductivity, electronic thermal conductivity) are computed using BoltzTraP, with the carrier relaxation time determined from deformation potential theory using the previously derived elastic constant and deformation potentials. Finally, the lattice and electronic contributions are combined to calculate the thermoelectric figure‑of‑merit ZT as a function of temperature and carrier concentration, and the mean group velocities of the acoustic phonon branches are collected.

## Reproduction target
Compute and report the following five quantities for BiBaK:
- Lattice thermal conductivity at 300 K and at 900 K (units W/mK).
- Maximum n‑type ZT at 900 K (dimensionless).
- Mean phonon group velocity for the transverse acoustic (TA) branch and for the longitudinal acoustic (LA) branch (units m/s).
All values must be written to `/app/outputs/results.json`.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/
- ShengBTE: https://github.com/shengbtc/ShengBTE
- BoltzTraP: https://bitbucket.org/sousaw/boltztra_p2/src/master/
- BiBaK crystal structure (Wyckoff positions)

## Workflow steps

### Step 1: DFT electronic structure and deformation potential
- Role: process
- Action: Build the BiBaK crystal structure from the provided Wyckoff positions and lattice constant. Perform DFT self-consistent field calculation and band structure using HSE06 functional with spin-orbit coupling to obtain band gap, density-of-states effective masses, and deformation potential constants. Compute the elastic constant via strained-cell calculations.
- Evidence: `/app/outputs/dft_electronic.log`

### Step 2: Harmonic phonon calculation
- Role: process
- Action: Using finite-displacement method with a 3×3×3 supercell, compute second-order interatomic force constants; run Phonopy to obtain phonon dispersion and group velocities. Record the mean group velocities for the transverse acoustic (TA) and longitudinal acoustic (LA) branches for later extraction.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 3: Third-order force constants
- Role: process
- Action: Compute third-order interatomic force constants using a 4×4×4 supercell with a cutoff radius of 7.7 Å.
- Evidence: `/app/outputs/FORCE_CONSTANTS_3RD`

### Step 4: Lattice thermal conductivity via ShengBTE
- Role: process
- Action: Run ShengBTE with the second- and third-order force constants to compute the lattice thermal conductivity as a function of temperature.
- Evidence: `/app/outputs/kappa_l_T.dat`

### Step 5: Electronic transport with BoltzTraP
- Role: process
- Action: Compute electronic transport coefficients using BoltzTraP from the band structure obtained in step 1. Determine carrier relaxation time from deformation potential theory using the computed elastic constant and deformation potentials, then calculate Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of temperature and carrier concentration.
- Evidence: `/app/outputs/boltztrap_output.trace`

### Step 6: Thermoelectric figure-of-merit and final compilation
- Role: scored (load-bearing)
- Action: Combine the lattice thermal conductivity data from step 4 with the electronic transport data from step 5 to calculate ZT as a function of carrier concentration at 900 K. Identify the maximum n-type ZT. Extract the mean TA and LA group velocities from the harmonic phonon results of step 2. Write the five required numeric quantities to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type":"object","required":{"kappa_l_300K":"number (unit: W/mK)","kappa_l_900K":"number (unit: W/mK)","ZT_max_n_type_900K":"number (dimensionless)","v_TA_mean":"number (unit: m/s)","v_LA_mean":"number (unit: m/s)"}}
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
- description: Final JSON file containing the computed lattice thermal conductivity at 300 K and 900 K, the mean phonon group velocities for TA and LA branches, and the maximum n-type ZT at 900 K.
- schema:
  - `type`: object
  - `required`:
    - `kappa_l_300K`: number (unit: W/mK)
    - `kappa_l_900K`: number (unit: W/mK)
    - `ZT_max_n_type_900K`: number (dimensionless)
    - `v_TA_mean`: number (unit: m/s)
    - `v_LA_mean`: number (unit: m/s)

Notes: The checker compares these values against hidden reference thresholds using a threshold-or-better policy: a value equal or better than the reference earns full credit. Tolerances absorb method-to-method scatter.

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
        "required": {
          "kappa_l_300K": "number (unit: W/mK)",
          "kappa_l_900K": "number (unit: W/mK)",
          "ZT_max_n_type_900K": "number (dimensionless)",
          "v_TA_mean": "number (unit: m/s)",
          "v_LA_mean": "number (unit: m/s)"
        }
      },
      "description": "Final JSON file containing the computed lattice thermal conductivity at 300 K and 900 K, the mean phonon group velocities for TA and LA branches, and the maximum n-type ZT at 900 K."
    }
  ],
  "notes": "The checker compares these values against hidden reference thresholds using a threshold-or-better policy: a value equal or better than the reference earns full credit. Tolerances absorb method-to-method scatter."
}
```

## How you are scored
A hidden verifier will read the `/app/outputs/results.json` file you produce and compare each of its five fields independently against hidden reference thresholds. The scoring uses a threshold‑or‑better policy: for a quantity where a higher value is better (ZT, group velocities) or a lower value is better (lattice thermal conductivity), meeting or exceeding the reference earns full credit for that field; only results worse than the reference are penalised. The checker accounts for expected method‑to‑method variability. The final reward is the weighted combination of the individual field scores; simply reporting a number is not sufficient—the value must be computed following the specified workflow.
