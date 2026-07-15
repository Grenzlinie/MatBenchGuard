# Reconstruction Performance of Figures-of-Merit in Gamma-ray Tracking

## Problem background
Gamma-ray tracking in highly segmented germanium detectors promises a significant improvement in nuclear spectroscopy. Reconstructing the scattering path of gamma rays within a detector volume depends on a figure-of-merit that assesses how well a sequence of interactions satisfies Compton kinematics. Different choices of local figure-of-merit lead to different reconstruction performance, measured by photopeak efficiency (ε) and peak-to-total ratio (P/T). An additional physical uncertainty arises from the momentum distribution of atomic electrons (Compton profile), which affects the angular reconstruction. This study investigates three local figures‑of‑merit and the influence of the atomic Compton profile to determine the conditions that give the best reconstruction performance.

## Approach
The detector is modeled as a solid spherical shell of germanium (inner radius 15 cm, outer radius 24 cm). Monte‑Carlo simulations using GEANT 3.21 (optionally with the GLECS extension to include the bound‑electron momentum) generate interaction points for 1332 keV gamma rays emitted from a central point source with multiplicity Mγ=5. Realistic detector effects are applied: energy resolution (Fano factor 0.12, electronic noise 300 eV, threshold 1.5 keV) and position resolution (Gaussian smearing with σpos=1 mm, merging points closer than 5σpos). The backtracking algorithm is implemented with three local figures‑of‑merit: w₁step = |θen−θpos|, w₂step = |θen−θpos|/σ (where σ combines energy and position uncertainties), and w₃step which additionally weights by γ‑ray interaction probabilities (photoelectric, Compton, total) and an exponential angular mismatch term. The total figure‑of‑merit for a track is the geometric mean of the local values. Reconstructed energy spectra are produced for each FoM, from which ε and P/T are extracted. For w₃step, the effect of the atomic electron momentum is evaluated by incorporating the variance of the germanium Compton profile (σQ² = 7.15 (mec²/ħ)) into the angular uncertainty.

## Reproduction target
Quantify reconstruction performance for three local figures‑of‑merit under the conditions: 1332 keV γ rays, Mγ=5, σpos=1 mm. Produce photopeak efficiency ε and peak‑to‑total ratio P/T for each of w₁step, w₂step, and w₃step. Then, for w₃step alone, compute ε and P/T both without and with the atomic Compton profile effect. Report these metrics in a single JSON file, `reconstruction_results.json`, following the output contract below. No other outputs are required for scoring.

## Assets

- GEANT 3.21 Monte Carlo code: http://wwwasd.web.cern.ch/wwwasd/geant/
- GLECS (Low-Energy Compton Scattering) package: http://gammaray.msfc.nasa.gov/actsim/
- Germanium atomic Compton profile J(Q): 10.1016/0092-640X(75)90002-3

## Workflow steps

### Step 1: Simulate ideal gamma-ray events without Compton profile
- Role: process
- Action: Using the GEANT 3.21 simulation framework, simulate 1332 keV gamma rays from a point source at the center of a solid spherical Ge detector shell (inner radius 15 cm, outer radius 24 cm). Record the position and deposited energy of each interaction. Set gamma-ray multiplicity Mγ=5. Generate at least 10000 events. Write the total original event count and the number of events in the full-energy photopeak to sim_truth.json, and save the list of interaction points and deposited energies per event to no_compton_events.npy.
- Evidence: `/app/outputs/sim_truth.json`

### Step 2: Apply detector response to no-Compton events
- Role: process
- Action: Apply realistic detector effects to each interaction point from step_01: energy resolution (Fano factor F=0.12, electronic noise σ_el=300 eV, threshold 1.5 keV) and position resolution (σ_pos=1 mm Gaussian smearing, merging points closer than 5σ_pos). Save the resulting noisy interaction points to no_compton_noisy_events.npy.
- Evidence: `/app/outputs/no_compton_noisy_events.npy`

### Step 3: Reconstruct tracks with each local figure-of-merit (no Compton)
- Role: process
- Action: Implement the backtracking algorithm. For each local figure-of-merit: (1) w1_step = |θ_en - θ_pos|; (2) w2_step = |θ_en - θ_pos|/σ where σ is the combined uncertainty from energy and position resolutions; (3) w3_step which incorporates γ-ray interaction probabilities (photoelectric, Compton, total) and the angular mismatch weighted by σ. The total figure-of-merit for a track is the geometric mean. Run the reconstruction on the noisy events from step_02. For each accepted track, record the sum of interaction energies. Save the list of reconstructed total energies per FoM as reco_no_compton.json with keys 'w1_step', 'w2_step', 'w3_step'.
- Evidence: `/app/outputs/reco_no_compton.json`

### Step 4: Simulate events with atomic electron momentum (Compton profile) using GLECS
- Role: process
- Action: Using GEANT 3.21 with the GLECS extension and the germanium Compton profile from Biggs et al. (1975), simulate the same detector geometry and source conditions as step_01. Generate at least 10000 events. Write the original event and photopeak counts to sim_truth_compton.json and raw interaction data to compton_events.npy.
- Evidence: `/app/outputs/sim_truth_compton.json`

### Step 5: Apply detector response to Compton events
- Role: process
- Action: Apply the same detector response as in step_02 (F=0.12, σ_el=300 eV, σ_pos=1 mm, merging) to the GLECS interaction data from step_04. Save the noisy points to compton_noisy_events.npy.
- Evidence: `/app/outputs/compton_noisy_events.npy`

### Step 6: Reconstruct with w3_step including Compton angular uncertainty
- Role: process
- Action: Run the backtracking algorithm using ONLY the w3_step local FoM. Augment the angular uncertainty by adding the variance from the Ge Compton profile: σ_total = sqrt(σ_θen² + σ_θpos² + σ_Q²) where σ_Q² = 7.15 (m_e c²/ħ). Reconstruct the noisy GLECS data from step_05, collect total reconstructed energies, and save to reco_compton.json with key 'w3_step_with_compton'.
- Evidence: `/app/outputs/reco_compton.json`

### Step 7: Compute photopeak efficiency and peak-to-total ratio
- Role: scored (load-bearing)
- Action: From the reconstructed total-energy lists (reco_no_compton.json, reco_compton.json) and the photopeak counts in sim_truth.json and sim_truth_compton.json, define the photopeak as tracks whose total energy falls within a narrow window around 1332 keV (e.g., 1332±5 keV). For each FoM in the no-Compton case, compute photopeak efficiency ε = number of tracks in photopeak / N_ph_original, and peak-to-total ratio P/T = number in photopeak / total reconstructed tracks. For the Compton profile effect, compute ε and P/T for the 'without_compton' case (using the w3_step no-Compton results) and for the 'with_compton' case (using the w3_step_with_compton results). Write all results to reconstruction_results.json with keys: 'fom_comparison' (list of {fom, epsilon, P_over_T}) and 'compton_profile_effect' (list of {case, epsilon, P_over_T}).
- Output file: `/app/outputs/reconstruction_results.json`
- Format: json
- Contract: { 'fom_comparison': [{'fom': 'w1_step', 'epsilon': float, 'P_over_T': float}, {'fom': 'w2_step', ...}, {'fom': 'w3_step', ...}], 'compton_profile_effect': [{'case': 'without_compton', 'epsilon': float, 'P_over_T': float}, {'case': 'with_compton', 'epsilon': float, 'P_over_T': float}] }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reconstruction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reconstruction_results.json
- path: `/app/outputs/reconstruction_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the computed photopeak efficiency and peak-to-total ratio for each figure-of-merit and for the atomic Compton profile effect.
- schema:
  - `type`: object
  - `required`:
    - `fom_comparison`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `fom`: string (one of w1_step, w2_step, w3_step)
          - `epsilon`: number (between 0 and 1)
          - `P_over_T`: number (between 0 and 1)
    - `compton_profile_effect`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`:
          - `case`: string (one of without_compton, with_compton)
          - `epsilon`: number (between 0 and 1)
          - `P_over_T`: number (between 0 and 1)

Notes: The checker will compare the reported metrics against the paper's published values using generous tolerances and verify the relative ordering w3_step > w2_step > w1_step for both ε and P/T. For the Compton profile effect, it will verify that the 'with_compton' values are lower than 'without_compton'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reconstruction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "fom_comparison": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "fom": "string (one of w1_step, w2_step, w3_step)",
                "epsilon": "number (between 0 and 1)",
                "P_over_T": "number (between 0 and 1)"
              }
            }
          },
          "compton_profile_effect": {
            "type": "array",
            "items": {
              "type": "object",
              "required": {
                "case": "string (one of without_compton, with_compton)",
                "epsilon": "number (between 0 and 1)",
                "P_over_T": "number (between 0 and 1)"
              }
            }
          }
        }
      },
      "description": "JSON file containing the computed photopeak efficiency and peak-to-total ratio for each figure-of-merit and for the atomic Compton profile effect."
    }
  ],
  "notes": "The checker will compare the reported metrics against the paper's published values using generous tolerances and verify the relative ordering w3_step > w2_step > w1_step for both ε and P/T. For the Compton profile effect, it will verify that the 'with_compton' values are lower than 'without_compton'."
}
```

## How you are scored
A hidden verifier inspects your `reconstruction_results.json`. It compares your reported ε and P/T values to reference benchmarks from the original study, using generous tolerances to absorb differences in implementation. It also checks that the relative ordering w₃step > w₂step > w₁step holds for both ε and P/T, and that the `with_compton` case yields lower values than the `without_compton` case. The final reward combines these checks, with the greatest weight on the magnitude of the metrics.
