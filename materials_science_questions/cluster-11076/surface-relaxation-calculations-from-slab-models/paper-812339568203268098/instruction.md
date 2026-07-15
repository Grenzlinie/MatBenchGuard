# Simulated SPA-LEED diffraction from a 1D Frenkel-Kontorova model of Cu(001)

## Problem background
The clean Cu(001) surface shows no reconstruction, but recent experiments with grazing-incidence ion bombardment revealed a persistent diffraction feature in SPA-LEED that suggests a uniaxial in-plane lattice contraction when atomic steps are present. The paper proposes that steps along the ⟨100⟩ azimuth relieve tensile surface stress, leading to a local energy minimum where the upper terrace contracts. A 1D Frenkel-Kontorova (FK) model, followed by kinematic diffraction, is used to simulate the SPA-LEED pattern and to explore how the relaxation creates a measurable diffraction signature.

## Approach
Implement a periodic chain of Cu surface atoms with a substrate potential of amplitude W and a misfit f (negative, indicating contraction). The energy of the chain combines a harmonic spring term that penalizes deviation from the contracted equilibrium spacing and a sinusoidal substrate term. Minimize the total energy (e.g., by gradient descent or a convex solver) to obtain the equilibrium lateral positions. The model also implies a vertical corrugation: atoms displaced from the potential minima rise by up to a√2 (a is the Cu lattice constant). Using these positions, compute the kinematic SPA-LEED intensity as a function of parallel wave vector k// (expressed in % of the Brillouin Zone). For each k//, sum the contribution from each atom in the chain, taking a phase factor that depends on lateral and vertical coordinates, and an exponential attenuation with an electron mean free path. Finally, convolve the raw intensity with an instrumental broadening (a narrow Gaussian) and normalize so the global maximum intensity equals 1.

## Reproduction target
Produce a two-column CSV file named `step_01_diffraction_profile.csv` containing the simulated SPA-LEED intensity profile. The first column (`k_percent_BZ`) lists parallel wave vector offsets in % of the Brillouin Zone. The second column (`intensity`) gives the normalized, non‑negative intensity (maximum = 1). The profile must result from solving the 1D Frenkel-Kontorova model with the supplied parameters, adding vertical corrugation, performing the kinematic diffraction summation, and applying convolution with plausible instrumental broadening. The goal is a physically correct profile that exhibits a distinct, well‑defined diffraction feature.

## Assets

- Cu bulk lattice constant
- Elastic constants of Cu
- Frenkel-Kontorova model parameters
- Instrumental resolution function

## Workflow steps

### Step 1: Simulated SPA-LEED diffraction intensity profile
- Role: scored (load-bearing)
- Action: Implement the 1D Frenkel-Kontorova model for a periodic chain of Cu(001) surface atoms using a substrate potential amplitude W=0.8 eV and a 1% in-plane contraction. Estimate the spring constant from Cu elastic properties or the strain‑relief energy. Minimize the total energy to obtain equilibrium atomic positions. Compute the kinematic SPA-LEED diffraction intensity as a function of parallel wave vector (in % BZ), include vertical corrugation (amplitude a√2) and an electron mean free path of 0.8 nm. Convolve with an instrumental broadening and normalize the intensity to a maximum of 1. Save the profile as a CSV.
- Output file: `/app/outputs/step_01_diffraction_profile.csv`
- Format: csv
- Contract: CSV with header: k_percent_BZ (float, wave vector offset in % of Brillouin Zone), intensity (float, normalized non-negative value).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_diffraction_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_diffraction_profile.csv
- path: `/app/outputs/step_01_diffraction_profile.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Simulated SPA-LEED diffraction intensity profile that must exhibit a clear peak near 1% Brillouin Zone.
- schema:
  - `type`: table
  - `required_columns`: `k_percent_BZ`, `intensity`
  - `units`:
    - `k_percent_BZ`: % BZ
    - `intensity`: arbitrary units (normalized)

Notes: The physical target is the peak location at approximately 1% BZ. The hidden checker will verify the peak position and a minimum intensity threshold; agents must genuinely run the FK energy minimization and diffraction calculation to produce a correct profile.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_diffraction_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_percent_BZ",
          "intensity"
        ],
        "units": {
          "k_percent_BZ": "% BZ",
          "intensity": "arbitrary units (normalized)"
        }
      },
      "description": "Simulated SPA-LEED diffraction intensity profile that must exhibit a clear peak near 1% Brillouin Zone."
    }
  ],
  "notes": "The physical target is the peak location at approximately 1% BZ. The hidden checker will verify the peak position and a minimum intensity threshold; agents must genuinely run the FK energy minimization and diffraction calculation to produce a correct profile."
}
```

## How you are scored
Your submitted `step_01_diffraction_profile.csv` is evaluated by a hidden verifier that inspects the profile’s shape and physical consistency. Points are awarded for correct structure (normalization, non‑negative intensity, etc.) and for presenting a clear diffraction peak at a physically expected location (excluding the central specular region). A profile that faithfully captures the Frenkel-Kontorova relaxation and the resulting diffraction pattern will earn a high reward. No manual judgment is involved; the verifier produces an automatic score on a 0–1 scale.
