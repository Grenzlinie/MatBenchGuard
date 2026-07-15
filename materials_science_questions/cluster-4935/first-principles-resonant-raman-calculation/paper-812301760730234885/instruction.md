# Polariton Dispersion and Absorption in Multilayer Dielectric Films

## Problem background
Thin dielectric and semiconductor films on metal substrates form hybrid light-matter states known as polaritons, which arise from the coupling of the electromagnetic field with lattice vibrations (phonons) and plasmon excitations in the metal. In three-layer vacuum–film–substrate structures, the macroscopic dielectric function approach, combined with the polariton concept, provides a unified framework to describe optical properties such as absorption, thermal emission, and scattering. The polariton dispersion equation predicts families of radiative modes (interference polaritons) and nonradiative modes (waveguide and surface polaritons). The presence of local impurity vibrations in the film can strongly modify the spectrum through resonance between an impurity mode and the film's interference modes, leading to dramatic absorption enhancement. The task is to implement this macroscopic polariton framework and to compute dispersion curves and absorption spectra for model systems, thereby characterizing the polariton branches and the resonance effect.

## Approach
The theoretical model considers a p-polarized (TM) electromagnetic wave in a layered structure: a semi-infinite vacuum, a dielectric film of thickness d, and a semi-infinite metal substrate. The polariton dispersion relation is derived from Maxwell's equations with standard boundary conditions and can be written as a transcendental equation involving the in-plane wavevector q and the frequency ω. The condition involves the out-of-plane wavevector components βⱼ = √(εⱼ ω²/c² – q² ε₁) for each layer. Branches with real β₁ correspond to radiative polaritons, while those with imaginary β₁ correspond to nonradiative ones. Light absorption by the structure in an attenuated total reflection (ATR) geometry is computed from a closed-form expression that depends on the incidence angle, the thicknesses of the gap and film, and the complex dielectric functions of all four media (prism, gap, film, substrate). The dielectric functions of the film materials are parameterized using Lorentz oscillator models to capture phonon resonances; for the metal substrate, a Drude model is employed. The overall approach is to: (i) implement the dielectric functions using known literature parameters; (ii) numerically solve the dispersion equation over a range of q to obtain the polariton branches and classify them as radiative or nonradiative; (iii) evaluate the ATR absorption formula for several film compositions to obtain spectra that reveal the influence of different polariton modes and the effect of an impurity local vibration.

## Reproduction target
Produce four output files under /app/outputs:
- `dispersion_curves.csv`: For a vacuum–ideal dielectric (ε₂=5.8, d=10 μm) on an aluminium mirror, compute the polariton dispersion branches (wavenumber vs in-plane wavevector q) and classify each as 'radiative' or 'nonradiative'.
- `absorption_ideal.csv`: Compute the p-polarized absorption spectrum for the same ideal dielectric structure at an incidence angle φ=20°, with prism and gap dielectric constant ε=1.
- `absorption_pure_ZnTe.csv`: Using the ZnTe Lorentz oscillator parameters (ω_TO=177 cm⁻¹, ω_LO=205 cm⁻¹, ε₀=9.6, ε∞=7.0, γ=5 cm⁻¹) and a film thickness d=2 μm, compute the p-polarized absorption spectrum of a pure ZnTe film on an aluminium mirror at φ=20° (prism/gap ε=1).
- `absorption_CdZnTe.csv`: Extend the ZnTe dielectric function with an additional Lorentz oscillator near 170 cm⁻¹ to model a local impurity vibration of Cd in Cd₀.₀₅Zn₀.₉₅Te. Use the same film thickness d=2 μm and compute the p-polarized absorption spectrum for this film on an aluminium mirror at φ=20° (prism/gap ε=1). The spectrum should demonstrate enhanced absorption due to resonance of the impurity mode with an interference mode.
All absorption spectra are computed for the same ATR geometry.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Dielectric function parameterization
- Role: process
- Action: Implement frequency‑dependent dielectric functions for the ideal dielectric film (ε2=5.8), ZnTe, CdZnTe (with an impurity oscillator near 170 cm⁻¹), Al substrate, and other required media using Lorentz oscillator and Drude models. Use literature parameters: for ZnTe, ω_TO=177 cm⁻¹, ω_LO=205 cm⁻¹, ε0=9.6, ε∞=7.0, γ=5 cm⁻¹; for Al, plasma frequency ~120000 cm⁻¹, damping ~1000 cm⁻¹. The functions will be used by subsequent steps.
- Evidence: `/app/outputs/dielectric_parameters.json`

### Step 2: TM polariton dispersion curves
- Role: scored
- Action: Solve the TM polariton dispersion equation for a vacuum-ideal dielectric (ε2=5.8, d=10 μm)-Al mirror structure. For each in-plane wavevector q, find allowed frequencies ω that satisfy the equation. Classify each (ω, q) mode as radiative (real β₁) or nonradiative (imaginary β₁). Save the dispersion branches.
- Output file: `/app/outputs/dispersion_curves.csv`
- Format: csv
- Contract: wavenumber (cm-1) [float], in_plane_wavevector_q (cm-1) [float], branch_type (string: 'radiative' or 'nonradiative')
- Scoring: scored by hidden verifier

### Step 3: Absorption spectrum – ideal dielectric film
- Role: scored
- Action: Compute p‑polarized absorption using the ATR formula for the same ideal dielectric structure at incidence angle φ=20°, with prism and gap medium having ε=1. Scan wavenumber range and output absorption vs wavenumber.
- Output file: `/app/outputs/absorption_ideal.csv`
- Format: csv
- Contract: wavenumber (cm-1) [float], absorption [float]
- Scoring: scored by hidden verifier

### Step 4: Absorption spectrum – pure ZnTe film
- Role: scored
- Action: Using the ZnTe dielectric function from step-0, compute p‑polarized absorption for a pure ZnTe film on an Al substrate at φ=20° (prism/gap ε=1). Output absorption vs wavenumber.
- Output file: `/app/outputs/absorption_pure_ZnTe.csv`
- Format: csv
- Contract: wavenumber (cm-1) [float], absorption [float]
- Scoring: scored by hidden verifier

### Step 5: Absorption spectrum – CdZnTe film
- Role: scored (load-bearing)
- Action: Extend the ZnTe dielectric function with an additional Lorentz oscillator near 170 cm⁻¹ (local impurity vibration) using physically reasonable oscillator strength and damping. Compute p‑polarized absorption for a Cd₀.₀₅Zn₀.₉₅Te film on Al at φ=20° (same prism/gap). Output absorption vs wavenumber, showing enhanced absorption due to resonance with the impurity mode.
- Output file: `/app/outputs/absorption_CdZnTe.csv`
- Format: csv
- Contract: wavenumber (cm-1) [float], absorption [float]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dispersion_curves.csv`
- `/app/outputs/absorption_ideal.csv`
- `/app/outputs/absorption_pure_ZnTe.csv`
- `/app/outputs/absorption_CdZnTe.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dispersion_curves.csv
- path: `/app/outputs/dispersion_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dispersion branches of TM polaritons for a vacuum-ideal dielectric (ε2=5.8, d=10 μm) - Al mirror structure. The checker verifies presence of at least one radiative and one nonradiative branch and correct classification.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber`, `in_plane_wavevector_q`, `branch_type`
  - `units`:
    - `wavenumber`: cm-1
    - `in_plane_wavevector_q`: cm-1
  - `description`: wavenumber (cm-1) float, in_plane_wavevector_q (cm-1) float, branch_type string ('radiative' or 'nonradiative')

### absorption_ideal.csv
- path: `/app/outputs/absorption_ideal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: p‑polarized absorption spectrum of the ideal dielectric film on Al mirror at φ=20°.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber`, `absorption`
  - `units`:
    - `wavenumber`: cm-1
    - `absorption`: dimensionless
  - `description`: wavenumber (cm-1) float, absorption float

### absorption_pure_ZnTe.csv
- path: `/app/outputs/absorption_pure_ZnTe.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: p‑polarized absorption spectrum of a pure ZnTe film on Al mirror at φ=20°.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber`, `absorption`
  - `units`:
    - `wavenumber`: cm-1
    - `absorption`: dimensionless
  - `description`: wavenumber (cm-1) float, absorption float

### absorption_CdZnTe.csv
- path: `/app/outputs/absorption_CdZnTe.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: p‑polarized absorption spectrum of a Cd₀.₀₅Zn₀.₉₅Te film on Al mirror at φ=20°, showing resonance‑enhanced absorption near 170 cm⁻¹.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber`, `absorption`
  - `units`:
    - `wavenumber`: cm-1
    - `absorption`: dimensionless
  - `description`: wavenumber (cm-1) float, absorption float

Notes: All absorption spectra are computed for the same geometry: prism and gap ε=1, incidence angle φ=20°. The CdZnTe film includes an additional impurity oscillator near 170 cm⁻¹. The checker will detect absorption peaks and compare their positions and relative intensities to hidden reference values derived from the paper’s figures. For the dispersion data, the checker will audit branch classification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dispersion_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber",
          "in_plane_wavevector_q",
          "branch_type"
        ],
        "units": {
          "wavenumber": "cm-1",
          "in_plane_wavevector_q": "cm-1"
        },
        "description": "wavenumber (cm-1) float, in_plane_wavevector_q (cm-1) float, branch_type string ('radiative' or 'nonradiative')"
      },
      "description": "Dispersion branches of TM polaritons for a vacuum-ideal dielectric (ε2=5.8, d=10 μm) - Al mirror structure. The checker verifies presence of at least one radiative and one nonradiative branch and correct classification."
    },
    {
      "file": "absorption_ideal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber",
          "absorption"
        ],
        "units": {
          "wavenumber": "cm-1",
          "absorption": "dimensionless"
        },
        "description": "wavenumber (cm-1) float, absorption float"
      },
      "description": "p‑polarized absorption spectrum of the ideal dielectric film on Al mirror at φ=20°."
    },
    {
      "file": "absorption_pure_ZnTe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber",
          "absorption"
        ],
        "units": {
          "wavenumber": "cm-1",
          "absorption": "dimensionless"
        },
        "description": "wavenumber (cm-1) float, absorption float"
      },
      "description": "p‑polarized absorption spectrum of a pure ZnTe film on Al mirror at φ=20°."
    },
    {
      "file": "absorption_CdZnTe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber",
          "absorption"
        ],
        "units": {
          "wavenumber": "cm-1",
          "absorption": "dimensionless"
        },
        "description": "wavenumber (cm-1) float, absorption float"
      },
      "description": "p‑polarized absorption spectrum of a Cd₀.₀₅Zn₀.₉₅Te film on Al mirror at φ=20°, showing resonance‑enhanced absorption near 170 cm⁻¹."
    }
  ],
  "notes": "All absorption spectra are computed for the same geometry: prism and gap ε=1, incidence angle φ=20°. The CdZnTe film includes an additional impurity oscillator near 170 cm⁻¹. The checker will detect absorption peaks and compare their positions and relative intensities to hidden reference values derived from the paper’s figures. For the dispersion data, the checker will audit branch classification."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. For `dispersion_curves.csv`, the verifier audits branch classification: it checks that at least one radiative and one nonradiative branch are present and that the classification is consistent with the polariton physics. For each absorption CSV, the verifier performs peak detection and compares the detected peak positions and relative intensities against reference values derived from experimental measurements in the literature, using tolerances appropriate for numerical recomputation. Each artifact contributes a share to the final reward (weighted combination). Simply writing known reference numbers without performing the required computation will not satisfy the verifier, which inspects structural consistency and expects the data to result from actual numerical solution of the equations.
