# Resonant Raman Susceptibility of Single- and Triple-Layer MoTe₂ via Finite-Difference Dielectric Susceptibility

## Problem background
Resonant Raman spectroscopy probes electron-phonon coupling in layered transition metal dichalcogenides. Accurately predicting the laser-energy dependent Raman intensities requires combining density functional theory (DFT) with many-body corrections (GW and Bethe-Salpeter equation) and a finite-difference evaluation of the dielectric susceptibility. This task reproduces the computed Raman susceptibility tensor for the prominent A1' and E' modes in single- and triple-layer MoTe2, as well as the phonon frequencies of these modes, at both independent-particle (IP) and Bethe-Salpeter equation (BSE) levels. The quantum interference analysis of the signals is not required for scoring.

## Approach
The approach uses first-principles calculations based on DFT (LDA, spin-orbit coupling) and many-body perturbation theory. The dielectric susceptibility is computed for the equilibrium structure and for structures displaced along the phonon eigenvectors of the Raman-active modes. Finite differences yield the Raman susceptibility tensor, whose xx-component squared is computed as a function of laser energy. The independent-particle (IP) spectrum is obtained from Kohn-Sham transitions; excitonic effects are included by applying a scissor shift from a G0W0 quasiparticle gap correction and solving the Bethe-Salpeter equation (BSE). The workflow is applied to single-layer and triple-layer 2H-MoTe2 using the experimental lattice constant. The final aim is to compute and compare the laser-energy dependence of the squared Raman susceptibility for the A1' and E' modes (single-layer) and the two A1' Davydov-split modes (triple-layer) at the IP and BSE levels.

## Reproduction target
Compute the phonon frequencies of the Raman-active modes: A1' and E' for single-layer MoTe2; A1'(a), A1'(b), and E' for triple-layer MoTe2. Compute the squared modulus of the xx-component of the Raman susceptibility tensor, |α_xx|^2, for the same modes at laser energies from 1.0 eV to 2.5 eV in steps of 0.1 eV, both in the independent-particle (IP) approximation and including excitonic effects via the Bethe-Salpeter equation (BSE). Write the phonon frequencies to /app/outputs/phonon_frequencies.csv and the Raman susceptibility data to /app/outputs/raman_susceptibility.csv according to the schemas below. The Raman susceptibility scaling is arbitrary; the checker evaluates relative trends.

## Assets

- Quantum ESPRESSO (PWscf and ph.x): https://www.quantum-espresso.org
- yambo code: https://www.yambo-code.eu
- LDA pseudopotentials for Mo and Te: https://pseudopotentials.quantum-espresso.org
- Crystal structure of 2H-MoTe₂

## Workflow steps

### Step 1: DFT ground-state calculation
- Role: process
- Action: Perform DFT ground-state calculations for single-layer and triple-layer MoTe₂ using Quantum ESPRESSO (PWscf) with LDA exchange-correlation, spin-orbit coupling, Mo semi-core 4s/4p states, a plane-wave energy cutoff of 100 Ry, and a 16×16×1 k-point grid. Use the experimental lattice constant a=3.52 Å and appropriate atomic positions for 2H-MoTe₂. Obtain Kohn-Sham wavefunctions, eigenvalues, and charge density.
- Evidence: none

### Step 2: DFPT phonon calculation
- Role: process
- Action: Compute Γ-point phonon frequencies and mass-normalized eigenvectors for Raman-active modes using density functional perturbation theory (DFPT) as implemented in ph.x of Quantum ESPRESSO, utilizing the ground-state results from step_01. Normalize eigenvectors according to the mass-weighted orthonormality condition.
- Evidence: none

### Step 3: Phonon frequencies
- Role: scored
- Action: Extract the frequencies of the Raman-active modes (E' and A₁' for single-layer; A₁'(a), A₁'(b), and E' for triple-layer) from the DFPT results and write them to phonon_frequencies.csv.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: system (SL/TL), mode_label (string), frequency_cm-1 (float). One row per mode.
- Scoring: scored by hidden verifier

### Step 4: GW quasiparticle correction
- Role: process
- Action: Perform a non-self-consistent G₀W₀ calculation on the equilibrium structures using the yambo code with a 36×36×1 k-point grid, 40 Ry plane-wave cutoff, 120 bands (single-layer) / 360 bands (triple-layer), and a Coulomb cutoff for the 2D slab. Obtain the quasiparticle band gap correction and determine the scissor shift (the value that will be applied to DFT eigenvalues in the BSE step).
- Evidence: none

### Step 5: DFT for displaced geometries
- Role: process
- Action: For each Raman-active phonon mode (A₁' and E' for single-layer; A₁'(a) and A₁'(b) for triple-layer), generate structures displaced by a small amplitude in the positive and negative direction along the phonon eigenvector. Run DFT calculations for each displaced geometry using the same settings as step_01, obtaining Kohn-Sham eigenvalues and wavefunctions.
- Evidence: none

### Step 6: Independent-particle dielectric susceptibility
- Role: process
- Action: For the equilibrium and all displaced geometries, compute the independent-particle (IP) dielectric susceptibility χ_IP(ω) using yambo with dipole matrix elements and a constant electronic broadening of 100 meV, over the photon energy range 1.0–2.5 eV.
- Evidence: none

### Step 7: BSE dielectric susceptibility
- Role: process
- Action: Apply the scissor shift from step_04 to the DFT eigenvalues. For the equilibrium and all displaced geometries, compute the Bethe-Salpeter equation (BSE) dielectric susceptibility χ_BSE(ω) using yambo with statically screened Coulomb interaction, a 36×36×1 k-point grid, 30 Ry plane-wave cutoff, and electronic transitions within a 3 eV window, over the photon energy range 1.0–2.5 eV.
- Evidence: none

### Step 8: Raman susceptibility tensor
- Role: scored (load-bearing)
- Action: Using the IP and BSE dielectric susceptibilities from steps 06 and 07 at equilibrium and displaced geometries, compute the Raman susceptibility tensor α_μ^xx(ω) for each Raman-active mode via finite differences, employing the phonon eigenvectors from step_02. Compute the squared modulus |α_μ^xx(ω)|² at laser energies from 1.0 to 2.5 eV in steps of 0.1 eV. Write the results to raman_susceptibility.csv.
- Output file: `/app/outputs/raman_susceptibility.csv`
- Format: csv
- Contract: Columns: laser_energy_eV (float), |alpha|^2_A1_prime_SL_IP (float), |alpha|^2_E_prime_SL_IP (float), |alpha|^2_A1_prime_SL_BSE (float), |alpha|^2_E_prime_SL_BSE (float), |alpha|^2_A1_prime_a_TL_IP (float), |alpha|^2_A1_prime_b_TL_IP (float), |alpha|^2_A1_prime_a_TL_BSE (float), |alpha|^2_A1_prime_b_TL_BSE (float). Header required; rows for laser energies 1.0–2.5 eV in steps of 0.1 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/raman_susceptibility.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies of the Raman-active modes in single-layer (SL) and triple-layer (TL) MoTe₂. Compared to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `system`, `mode_label`, `frequency_cm-1`
  - `units`:
    - `frequency_cm-1`: cm⁻¹

### raman_susceptibility.csv
- path: `/app/outputs/raman_susceptibility.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Squared modulus of the Raman susceptibility tensor xx-component for selected modes, at independent-particle (IP) and Bethe–Salpeter (BSE) levels. The checker computes intensity ratios and verifies crossover/inversion trends against hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `laser_energy_eV`, `|alpha|^2_A1_prime_SL_IP`, `|alpha|^2_E_prime_SL_IP`, `|alpha|^2_A1_prime_SL_BSE`, `|alpha|^2_E_prime_SL_BSE`, `|alpha|^2_A1_prime_a_TL_IP`, `|alpha|^2_A1_prime_b_TL_IP`, `|alpha|^2_A1_prime_a_TL_BSE`, `|alpha|^2_A1_prime_b_TL_BSE`
  - `units`:
    - `laser_energy_eV`: eV
    - `all |alpha|^2 columns`: arbitrary units (consistent scaling)

Notes: The Raman susceptibility scaling factor is arbitrary; the checker uses intensity ratios to cancel common factors. The scissor shift from GW is applied to DFT eigenvalues; re-running full GW for each displaced geometry is not required. The quantum interference analysis (Argand plots) is not part of the scored verification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "mode_label",
          "frequency_cm-1"
        ],
        "units": {
          "frequency_cm-1": "cm⁻¹"
        }
      },
      "description": "Phonon frequencies of the Raman-active modes in single-layer (SL) and triple-layer (TL) MoTe₂. Compared to paper-reported values."
    },
    {
      "file": "raman_susceptibility.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "laser_energy_eV",
          "|alpha|^2_A1_prime_SL_IP",
          "|alpha|^2_E_prime_SL_IP",
          "|alpha|^2_A1_prime_SL_BSE",
          "|alpha|^2_E_prime_SL_BSE",
          "|alpha|^2_A1_prime_a_TL_IP",
          "|alpha|^2_A1_prime_b_TL_IP",
          "|alpha|^2_A1_prime_a_TL_BSE",
          "|alpha|^2_A1_prime_b_TL_BSE"
        ],
        "units": {
          "laser_energy_eV": "eV",
          "all |alpha|^2 columns": "arbitrary units (consistent scaling)"
        }
      },
      "description": "Squared modulus of the Raman susceptibility tensor xx-component for selected modes, at independent-particle (IP) and Bethe–Salpeter (BSE) levels. The checker computes intensity ratios and verifies crossover/inversion trends against hidden gold values."
    }
  ],
  "notes": "The Raman susceptibility scaling factor is arbitrary; the checker uses intensity ratios to cancel common factors. The scissor shift from GW is applied to DFT eigenvalues; re-running full GW for each displaced geometry is not required. The quantum interference analysis (Argand plots) is not part of the scored verification."
}
```

## How you are scored
A hidden verifier scores each of the two scored output files independently, then combines them with the following approximate weight: 50% from single-layer intensity ratio trends and values, 50% from triple-layer intensity ratio trends and values, with a small additional weight on phonon frequencies. For phonon_frequencies.csv, the checker verifies that the reported frequencies are close to a hidden reference within a tolerance. For raman_susceptibility.csv, the checker computes the intensity ratio R_SL = |α|^2(A1')/|α|^2(E') for single-layer, and R_TL = |α|^2(A1'(b))/|α|^2(A1'(a)) for triple-layer, at each laser energy. It then checks that the IP-level and BSE-level ratio curves exhibit the correct qualitative trends (i.e., crossover behavior) between specified laser energies, and that the BSE-level ratios at selected key energies are numerically within a prescribed tolerance of hidden reference values. Reporting the correct trends and reproducing the correct BSE-level ratios are essential; absolute values that differ by a global factor are still acceptable as long as ratios are correct. The verifier does not require the quantum interference analysis or comparison with experimental data.
