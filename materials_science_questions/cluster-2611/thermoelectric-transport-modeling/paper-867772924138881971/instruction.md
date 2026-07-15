# First-principles phonon-limited conductivity of 2D semiconductors

## Problem background
Phonon-limited electrical transport is a key determinant of performance in 2D semiconductor devices. Predicting which monolayer materials exhibit high intrinsic conductivity and carrier mobility at room temperature and field-effect doping levels is a challenge that requires first-principles calculations encompassing electronic structure, lattice dynamics, and electron-phonon coupling. This task addresses that challenge for two prototypical 2D semiconductors: electron-doped InSe and hole-doped phosphorene.

## Approach
The methodology combines density-functional theory (DFT) with density-functional perturbation theory (DFPT) to compute electronic bands, phonon dispersions, and electron-phonon matrix elements, all under a symmetric double-gate field-effect boundary condition that models high carrier-density doping. From these first-principles quantities, momentum-resolved phonon scattering probabilities are constructed at room temperature, and the linearized Boltzmann transport equation (BTE) is solved to obtain the carrier relaxation times. Finally, the longitudinal electrical conductivity and the drift mobility are evaluated by integrating the BTE solution. The workflow is carried out for monolayer InSe (electron-doped) and phosphorene (hole-doped) at a fixed sheet carrier density of 1×10¹³ cm⁻² and T = 300 K. The comparison focuses on how the two distinct band-structure strategies – a steep isotropic single valley versus an anisotropic single valley with directionally dependent scattering – determine transport performance.

## Reproduction target
Compute the phonon-limited electrical conductivity (in units of e²/h) and carrier mobility (in cm²/Vs) for electron-doped monolayer InSe and hole-doped monolayer phosphorene at T = 300 K and a sheet carrier density of 10¹³ cm⁻². Write the results to a CSV file with one row per material and the columns material, conductivity_e2h, mobility_cm2Vs. The target is to obtain values that result from faithfully executing the described first-principles and BTE protocol.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials efficiency v0.7: https://www.materialscloud.org/discover/sssp/
- Exfoliable 2D materials database (Mounet et al., 2018): https://www.materialscloud.org/discover/2dstructures/
- AiiDA workflow (optional): https://www.aiida.net/

## Workflow steps

### Step 1: Retrieve crystal structures
- Role: process
- Action: Obtain the crystallographic structures for monolayer InSe and phosphorene from the Materials Cloud exfoliable 2D materials database (Mounet et al., 2018). These structures will serve as inputs for the subsequent DFT calculations.
- Evidence: `/app/outputs/crystal_structures_used.json`

### Step 2: Gated DFT and DFPT calculations
- Role: process
- Action: For each material, run Quantum ESPRESSO ground-state DFT (PBE, SSSP pseudopotentials, 32x32 Monkhorst-Pack k-grid, 0.02 Ry cold smearing) followed by density-functional perturbation theory using the symmetric double-gate field-effect boundary condition with a target sheet carrier density of 10^13 cm^{-2}. Compute electronic band energies, band velocities, phonon frequencies, and electron-phonon matrix elements g_{k,k+q,ν}.
- Evidence: `/app/outputs/dft_dfpt_summary.txt`

### Step 3: Construct phonon scattering probabilities
- Role: process
- Action: Using the electron-phonon matrix elements, phonon energies, and electronic band energies, build the room-temperature (300 K) momentum-resolved scattering probabilities P_{kk'} for phonon absorption and emission. The Fermi level must be determined self-consistently to yield the required carrier density of 10^13 cm^{-2}.
- Evidence: `/app/outputs/scattering_probabilities_info.npy`

### Step 4: Solve BTE and compute conductivity/mobility
- Role: scored (load-bearing)
- Action: Solve the linearized Boltzmann transport equation for the momentum-dependent relaxation time τ(k) using the scattering probabilities. Then compute the longitudinal conductivity σ and the mobility μ = σ/(e n) for each material. Write the results to /app/outputs/conductivity_mobility.csv.
- Output file: `/app/outputs/conductivity_mobility.csv`
- Format: csv
- Contract: Columns: material (string), conductivity_e2h (float), mobility_cm2Vs (float). One row per material.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/conductivity_mobility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### conductivity_mobility.csv
- path: `/app/outputs/conductivity_mobility.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed phonon-limited electrical conductivity (in e^2/h) and carrier mobility (in cm^2/Vs) for electron-doped InSe (InSe-e) and hole-doped phosphorene (P4-h) at T=300 K and sheet carrier density 10^13 cm^{-2}.
- schema:
  - `type`: table
  - `required_columns`: `material`, `conductivity_e2h`, `mobility_cm2Vs`
  - `units`:
    - `conductivity_e2h`: e^2/h
    - `mobility_cm2Vs`: cm^2 / Vs

Notes: The scored checker compares these values against the paper's reported results using a threshold_or_better tolerance policy. No other outputs are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "conductivity_mobility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "conductivity_e2h",
          "mobility_cm2Vs"
        ],
        "units": {
          "conductivity_e2h": "e^2/h",
          "mobility_cm2Vs": "cm^2 / Vs"
        }
      },
      "description": "Computed phonon-limited electrical conductivity (in e^2/h) and carrier mobility (in cm^2/Vs) for electron-doped InSe (InSe-e) and hole-doped phosphorene (P4-h) at T=300 K and sheet carrier density 10^13 cm^{-2}."
    }
  ],
  "notes": "The scored checker compares these values against the paper's reported results using a threshold_or_better tolerance policy. No other outputs are scored."
}
```

## How you are scored
A hidden verifier will inspect each workflow artifact and assign a per-stage score, then combine them into a final reward in the range [0, 1]. The dominant weight is on the final conductivity_mobility.csv: the verifier compares your reported conductivity and mobility for each material against independent reference values using a tolerance policy that awards full credit when the computed results meet or exceed the reference, and gradually reduces credit as deviations increase. Process stages are checked for existence and plausible content but carry lower weight. Reporting the correct numbers alone without executing the computational pipeline will not receive full credit.
