# Resonant Raman Intensity for MoS2 A1' Mode from First-Principles GW-BSE

## Problem background
Resonant Raman scattering in two-dimensional semiconductors such as monolayer MoS2 reveals rich exciton-phonon coupling physics, but the measured intensity does not simply track the absorption spectrum. The near-absence of Raman response at the A and B exciton resonances and the disproportionate strength at the C exciton suggest a strong regulatory role of excitonic effects that goes beyond the conventional Placzek approximation. This work aims to compute the frequency-dependent resonant Raman intensity of the A1' phonon mode from first principles, using a perturbative treatment that includes excitonic effects through GW and the Bethe-Salpeter equation (BSE).

## Approach
The computational approach begins with a density functional theory (DFT) ground-state calculation for monolayer MoS2 to obtain Kohn-Sham eigenvalues and wavefunctions. Density functional perturbation theory (DFPT) then yields the electron-phonon coupling matrix elements for the A1' phonon mode. Quasiparticle corrections are computed within the GW approximation, and the resulting quasiparticle band structure is used to construct and diagonalize the BSE Hamiltonian, giving exciton eigenvalues, eigenvectors, and optical matrix elements. The resonant Raman susceptibility is then evaluated using a perturbative expression that combines two-band and three-band contributions, which account for the derivative of the exciton Hamiltonian with respect to the phonon displacement. This formulation, which goes beyond the Placzek approximation, naturally includes exciton-exciton scattering terms that become significant when exciton energies are bunched. A phenomenological broadening is applied to mimic realistic exciton lifetimes.

## Reproduction target
Compute the resonant Raman intensity (squared modulus of the Raman susceptibility |α|²) of the A1' phonon mode in monolayer MoS2 at three laser energies: 1.85 eV, 1.98 eV, and 2.4 eV. These energies correspond to the A, B, and C exciton features of the material. Produce a CSV file with three rows, each giving a laser energy and the corresponding computationally predicted intensity in arbitrary units. The three-intensity profile captures the excitonic regulation of the Raman response, and your submission will be judged by how well the profile reflects the underlying exciton‑phonon coupling physics.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BerkeleyGW: https://berkeleygw.org/
- Monolayer MoS2 crystal structure (2H phase): https://materialsproject.org/materials/mp-1434

## Workflow steps

### Step 1: DFT ground-state calculation
- Role: process
- Action: Perform a DFT ground-state calculation for monolayer MoS2 using the local density approximation (LDA) and relativistic pseudopotentials to obtain Kohn-Sham eigenvalues and wavefunctions.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Electron-phonon coupling for A1' mode
- Role: process
- Action: Using density functional perturbation theory (DFPT), compute the derivative of the DFT Hamiltonian with respect to the A1' phonon displacement to obtain the electron-phonon matrix elements ⟨ck|∂H|ck⟩ and ⟨vk|∂H|vk⟩ for the relevant bands.
- Evidence: `/app/outputs/eph_output.log`

### Step 3: GW quasiparticle correction
- Role: process
- Action: Perform a GW calculation to obtain quasiparticle band energies. Compute the dielectric matrix within RPA and apply the GW approximation to the Kohn-Sham states, using Coulomb truncation and the static remainder technique.
- Evidence: `/app/outputs/gw_output.log`

### Step 4: BSE exciton calculation
- Role: process
- Action: Assemble and diagonalize the Bethe-Salpeter equation (BSE) matrix using the GW quasiparticle energies and Kohn-Sham wavefunctions. Include a sufficient number of valence and conduction bands and interpolate to a fine k-grid to obtain exciton eigenvalues ω_S, eigenvectors, and optical matrix elements ⟨0|r|S⟩.
- Evidence: `/app/outputs/bse_output.log`

### Step 5: Perturbative resonant Raman intensity
- Role: scored (load-bearing)
- Action: Compute the resonant Raman intensity (squared susceptibility |α|^2) for the A1' phonon mode at three laser energies: 1.85 eV, 1.98 eV, and 2.4 eV. Use the perturbative expressions that combine two-band (d₂) and three-band (d₃) contributions from the exciton and electron‑phonon data, with a phenomenological broadening of 0.2 eV. Output the intensities (arbitrary units) to a CSV file.
- Output file: `/app/outputs/raman_profile.csv`
- Format: csv
- Contract: Columns: laser_energy (float in eV), intensity (float in arbitrary units). Three rows for 1.85, 1.98, 2.4 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raman_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raman_profile.csv
- path: `/app/outputs/raman_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Resonant Raman intensity (|α|^2) for the A1' phonon mode at 1.85, 1.98, and 2.4 eV laser energies. The hidden checker recomputes intensity ratios and compares them against hidden reference thresholds derived from the paper’s reported exciton regulation trend.
- schema:
  - `type`: table
  - `required_columns`: `laser_energy`, `intensity`
  - `units`:
    - `laser_energy`: eV
    - `intensity`: arbitrary units

Notes: The checker will evaluate the intensity ratios I(2.4)/I(1.85) and I(2.4)/I(1.98) against hidden thresholds and verify the qualitative trend that intensity at 2.4 eV is much larger than at 1.85 and 1.98 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raman_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "laser_energy",
          "intensity"
        ],
        "units": {
          "laser_energy": "eV",
          "intensity": "arbitrary units"
        }
      },
      "description": "Resonant Raman intensity (|α|^2) for the A1' phonon mode at 1.85, 1.98, and 2.4 eV laser energies. The hidden checker recomputes intensity ratios and compares them against hidden reference thresholds derived from the paper’s reported exciton regulation trend."
    }
  ],
  "notes": "The checker will evaluate the intensity ratios I(2.4)/I(1.85) and I(2.4)/I(1.98) against hidden thresholds and verify the qualitative trend that intensity at 2.4 eV is much larger than at 1.85 and 1.98 eV."
}
```

## How you are scored
A hidden verifier reads your `raman_profile.csv`, extracts the three intensities, and computes numerical ratios or trends that are then compared against hidden reference thresholds. These thresholds have been derived from the expected exciton‑regulation behavior and are broad enough to accommodate legitimate implementation differences while rejecting arbitrary guesses. The reward (a value between 0 and 1) increases as your computed profile better approximates the correct physics. Simply reporting pre‑looked‑up numbers from the published work is unlikely to pass the hidden check, as the reference criteria are based on an independent recomputation rather than on exact reproduction of the original paper’s values.
