# Phonon displacement-induced metallization in La2CuO4: frozen-phonon optical conductivity

## Problem background
The role of the crystal lattice in the insulator-to-metal transition of cuprates is debated. In the parent compound La2CuO4, an insulating gap exists between the O-2p and Cu-3d upper Hubbard band, and optical conductivity shows a charge-transfer peak around 2.2 eV with negligible low-energy weight. It has been proposed that certain lattice vibrations (phonons) can strongly couple to the electronic degrees of freedom and possibly induce a metallic state, but the relative efficacy of different vibrational modes remains an open question. This task focuses on the computational investigation of whether frozen (static) ionic displacements along specific Raman-active phonon eigenvectors can drive metallization in La2CuO4, as evidenced by the emergence of Drude spectral weight in the in-plane optical conductivity.

## Approach
We use a combined first-principles and many-body approach: (1) Perform density-functional theory (DFT) relaxation and linear-response phonon calculation on orthorhombic La2CuO4 (space group Cmca) to obtain the relaxed structure and the eigenvectors of the fully symmetric A_g(3) and the non‑fully symmetric B_1g Γ‑point phonon modes. (2) From the relaxed structure, create three unit cells: the undisplaced reference, one with all ions displaced by 0.04 Å along the normalized A_g(3) eigenvector, and one with ions displaced by 0.04 Å along the B_1g eigenvector. (3) For each of the three structures, compute the real part of the in‑plane optical conductivity, σ₁(ω), using the quasiparticle self‑consistent GW plus dynamical mean‑field theory (QSGW+DMFT) method over 0–3.5 eV. The key quantity of interest is the spectral weight at low energy (below ≈1 eV), integrated by trapezoidal rule, which serves as a proxy for the Drude response indicative of metallicity. Comparing the integrated weights across the three structures allows us to assess whether a particular phonon distortion can induce metallic behavior.

## Reproduction target
Compute the in‑plane optical conductivity σ₁(ω) for the undisplaced, A_g(3)-displaced, and B_1g-displaced La2CuO4 structures using DFT‑phonon calculations (Quantum Espresso) and QSGW+DMFT (Questaal). For each case, output the energy grid and the corresponding σ₁ values over 0–3.5 eV, together with the spectral weight integrated from 0 to 1 eV. The aim is to determine how the different frozen‑phonon distortions affect the low‑energy optical conductivity, specifically whether any of the distortions yields a substantial Drude-like spectral weight that is absent in the undisplaced case.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- Questaal: http://www.questaal.org/
- La2CuO4 orthorhombic crystal structure: 10.1103/PhysRevB.50.3221
- Norm-conserving pseudopotentials for La, Cu, O: pseudo dojo or SSSP

## Workflow steps

### Step 1: DFT relaxation and phonon calculation
- Role: process
- Action: Use Quantum Espresso to perform DFT structural relaxation and linear-response phonon calculation for orthorhombic La2CuO4 (space group Cmca). Obtain relaxed atomic positions and eigenvectors of all Γ-point phonons, specifically those of A_g(3) and B_1g modes.
- Evidence: none

### Step 2: Generate displaced structures
- Role: process
- Action: From the relaxed structure, create two distorted unit cells: displace ionic positions by 0.04 Å along the normalized A_g(3) eigenvector and by 0.04 Å along the B_1g eigenvector. Keep the undisplaced structure as reference. Save the three structures (undisplaced, A_g-displaced, B_1g-displaced) for subsequent calculations.
- Evidence: none

### Step 3: Compute optical conductivity for displaced and undisplaced structures
- Role: scored (load-bearing)
- Action: Using Questaal, run QSGW+DMFT calculations for each of the three structures (undisplaced, A_g(3)-displaced, B_1g-displaced) to compute the real part of the in-plane optical conductivity σ₁(ω) over the energy range 0–3.5 eV. Output results as optical_conductivity_results.json containing energy_ev and sigma1 arrays for each case, plus the integrated spectral weight from 0 to 1 eV computed by trapezoidal integration.
- Output file: `/app/outputs/optical_conductivity_results.json`
- Format: json
- Contract: JSON object with keys: 'undisplaced', 'A_g_displaced', 'B_1g_displaced'. Each value is an object with 'energy_ev' (list of float, energies in eV) and 'sigma1' (list of float, corresponding σ₁(ω) values). Each also contains 'integrated_weight_below_1eV' (float) computed via trapezoidal integration.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_conductivity_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_conductivity_results.json
- path: `/app/outputs/optical_conductivity_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: In-plane optical conductivity σ₁(ω) for undisplaced, A_g(3)-displaced, and B_1g-displaced La2CuO4, along with integrated spectral weight below 1 eV. This artifact enables verification of metallization (Drude weight) induced by A_g phonon mode while B_1g does not.
- schema:
  - `type`: object
  - `required`:
    - `undisplaced`: object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)
    - `A_g_displaced`: object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)
    - `B_1g_displaced`: object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)
  - `units`:
    - `energy_ev`: eV
    - `sigma1`: arbitrary units (same scale for all three cases)

Notes: The scored target is the appearance of significant Drude spectral weight (integrated σ₁ below 1 eV) for the A_g-displaced structure, with minimal weight for the other two cases. The checker will recompute the integrated weights from the provided curves and verify threshold-based inequalities and monotonic Drude shape.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_conductivity_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "undisplaced": "object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)",
          "A_g_displaced": "object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)",
          "B_1g_displaced": "object with energy_ev (array of numbers), sigma1 (array of numbers), integrated_weight_below_1eV (number)"
        },
        "units": {
          "energy_ev": "eV",
          "sigma1": "arbitrary units (same scale for all three cases)"
        }
      },
      "description": "In-plane optical conductivity σ₁(ω) for undisplaced, A_g(3)-displaced, and B_1g-displaced La2CuO4, along with integrated spectral weight below 1 eV. This artifact enables verification of metallization (Drude weight) induced by A_g phonon mode while B_1g does not."
    }
  ],
  "notes": "The scored target is the appearance of significant Drude spectral weight (integrated σ₁ below 1 eV) for the A_g-displaced structure, with minimal weight for the other two cases. The checker will recompute the integrated weights from the provided curves and verify threshold-based inequalities and monotonic Drude shape."
}
```

## How you are scored
A hidden verifier will read your submitted `optical_conductivity_results.json`, re‑compute the integrated σ₁(ω) below 1 eV by trapezoidal integration for each of the three structures, and then evaluate the relationships among the integrated weights. The reward is based solely on whether the submitted conductivity curves capture the expected relative effect of the lattice distortions on the low‑energy Drude spectral weight — not on reproducing any specific numeric value from the literature. Simply reporting plausible numbers without genuinely performing the computational workflow will produce a low reward.
