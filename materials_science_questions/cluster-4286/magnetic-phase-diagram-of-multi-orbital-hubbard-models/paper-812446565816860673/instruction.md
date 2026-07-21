# Self-consistent Hartree-Fock solver for spin density waves and magnetization processes in transition metals

## Problem background
Transition metals exhibit complex magnetic order that challenges a purely localized or purely itinerant picture. A unified theory is needed to explain phenomena such as the spin density wave (SDW) in chromium and the antiferromagnetic-to-ferromagnetic transition in FeRh, both of which depend sensitively on the electronic structure near the Fermi level. The interacting virtual states formalism addresses this by treating the 3d states as lorentzian resonances whose occupations are determined self-consistently in the Hartree-Fock approximation, with interatomic electron transfer included via second-order perturbation theory. This allows the magnitude of local magnetic moments and the effective exchange interactions to vary with the magnetic configuration, reflecting itinerant character. The task is to implement the self-consistent solver and compute the magnetic ground-state properties predicted by this model for two materials, thereby testing whether the approach can explain the key experimental features without adjustable parameters beyond the input d-electron count and Coulomb interaction strength.

## Approach
The computational method is based on a single-orbital Anderson model with a constant virtual level half-width Δ. Interatomic electron transfer is treated as a perturbation up to second order, yielding a local density of states that consists of a Lorentzian centered at the Hartree-Fock level plus a correction term that depends on the level differences between neighboring atoms. The spin-dependent atomic levels are determined self-consistently from the occupations obtained by integrating the density of states up to the Fermi energy. The Fermi energy is adjusted to enforce a given average number of d electrons per atom. For the Cr case, a spin density wave of period p is imposed along the [001] direction with nodes placed halfway between atomic planes; the occupation of each inequivalent plane is solved iteratively. A Fourier analysis of the resulting magnetic moment envelope gives the first and third harmonic amplitudes, and the charge density wave is obtained from the deviation of plane occupations from the average. For FeRh, a CsCl-type lattice with Fe and Rh atoms is considered; an external magnetic field is applied, and the angle θ between the Fe sublattice magnetizations and the field is determined by a torque balance condition that involves the Zeeman energy and two configuration-dependent “exchange energies” for Fe–Rh and Fe–Fe couplings. Minimizing the total energy with respect to θ yields the equilibrium state, from which the magnetization per formula unit is computed over a range of applied fields.

## Reproduction target
The objective is divided into two independent scored computations.

1. **Chromium SDW envelope and harmonics**: Using the parameters U/Δ = 4.42, average d-electron count Nd = 5.209, nearest-neighbor transfer V1/Δ = 0.32, and next-nearest-neighbor transfer V2/Δ = 0.12, impose a spin density wave of period p = 20 along [001] with nodes halfway between atomic planes. Solve for the self-consistent spin-dependent occupations on the 10 inequivalent planes. From these, calculate the magnetic moment per plane (in μB), the amplitudes of the first and third Fourier harmonics of the envelope, the ratio of third to first harmonic amplitude, and the charge density wave amplitude (maximum deviation from the average occupancy). Output these quantities as described in Step 1.

2. **FeRh zero‑temperature magnetization curve**: For the CsCl-type ordered FeRh alloy, use the parameters U/Δ = 10, (E_Fe − E_Rh)/Δ = 0.054, Nd = 7.218, and the same transfer integrals V1/Δ = 0.32, V2/Δ = 0.12. For a range of external magnetic fields from zero to saturation, solve the torque balance condition by varying the angle θ between the Fe sublattice magnetizations and the applied field. At each equilibrium θ, compute the self-consistent occupations and the total magnetization per formula unit (μB). Output the resulting magnetization curve as specified in Step 2.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute SDW envelope, harmonic analysis, and CDW amplitude for Cr
- Role: scored (load-bearing)
- Action: Implement the self-consistent Hartree-Fock solver for the interacting virtual states formalism on a bcc Cr lattice with a spin density wave of period p=20 along [001], nodes halfway between atomic planes. Use the second-order perturbed local density of states and Hartree-Fock level equations (Anderson model with constant half-width Δ, transfer integrals V1/Δ=0.32, V2/Δ=0.12, U/Δ=4.42). Iteratively solve for the spin-dependent electron occupations n_jσ on the 10 inequivalent planes until convergence, adjusting the Fermi energy to enforce the average d-electron count Nd=5.209. Extract the magnetic moment (in μB) for each plane. Perform Fourier analysis to obtain the first and third harmonic amplitudes and their ratio. Compute the charge density wave amplitude (deviation from average occupancy per plane). Save all results to /app/outputs/step_01_sdw_results.json.
- Output file: `/app/outputs/step_01_sdw_results.json`
- Format: json
- Contract: {"planes": [{"plane_index": int, "magnetic_moment_mub": float}], "harmonic_analysis": {"first_harmonic_amplitude_mub": float, "third_harmonic_amplitude_mub": float, "ratio_third_to_first": float}, "cdw_amplitude_electrons_per_atom": float}
- Scoring: scored by hidden verifier

### Step 2: Compute zero-temperature magnetization curve for FeRh
- Role: scored
- Action: Implement the self-consistent solver for the CsCl-type FeRh antiferromagnetic state under external magnetic field H. Treat Fe and Rh sites with U/Δ=10, (E_Fe−E_Rh)/Δ=0.054, Nd=7.218, and the same transfer integrals V1/Δ=0.32, V2/Δ=0.12. For a range of H values from zero to saturation, solve the torque balance condition by varying the angle θ between Fe sublattice magnetizations and the field, until the total energy is minimized. At each equilibrium θ, compute the self-consistent occupations and the total magnetization per formula unit (in μB). Save the resulting magnetization curve to /app/outputs/step_02_ferh_magnetization.json.
- Output file: `/app/outputs/step_02_ferh_magnetization.json`
- Format: json
- Contract: {"parameters": {"U_over_Delta": float, "E_Fe_minus_E_Rh_over_Delta": float, "Nd": float}, "magnetization_curve": [{"field_mub_H_over_Delta": float, "magnetization_mub_per_fu": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_sdw_results.json`
- `/app/outputs/step_02_ferh_magnetization.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_sdw_results.json
- path: `/app/outputs/step_01_sdw_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Self-consistent Cr SDW envelope (magnetic moment per plane), harmonic content, and charge density wave amplitude.
- schema:
  - `type`: object
  - `required`:
    - `planes`: array of objects with plane_index (integer) and magnetic_moment_mub (float)
    - `harmonic_analysis`: object with first_harmonic_amplitude_mub (float), third_harmonic_amplitude_mub (float), ratio_third_to_first (float)
    - `cdw_amplitude_electrons_per_atom`: float

### step_02_ferh_magnetization.json
- path: `/app/outputs/step_02_ferh_magnetization.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetization per formula unit of FeRh as a function of external field at T=0, obtained from self-consistent torque balance.
- schema:
  - `type`: object
  - `required`:
    - `parameters`: object with U_over_Delta (float), E_Fe_minus_E_Rh_over_Delta (float), Nd (float)
    - `magnetization_curve`: array of objects with field_mub_H_over_Delta (float) and magnetization_mub_per_fu (float)

Notes: All energies and fields are expressed in units of the virtual level half-width Δ. The agent must implement the self-consistent solver from the paper's formalism and produce the stated JSON artifacts; the checker compares key features (envelope, harmonic ratio, CDW amplitude, saturation magnetization, critical field, curve shape) against hidden paper-reported values with suitable tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_sdw_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "planes": "array of objects with plane_index (integer) and magnetic_moment_mub (float)",
          "harmonic_analysis": "object with first_harmonic_amplitude_mub (float), third_harmonic_amplitude_mub (float), ratio_third_to_first (float)",
          "cdw_amplitude_electrons_per_atom": "float"
        }
      },
      "description": "Self-consistent Cr SDW envelope (magnetic moment per plane), harmonic content, and charge density wave amplitude."
    },
    {
      "file": "step_02_ferh_magnetization.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "parameters": "object with U_over_Delta (float), E_Fe_minus_E_Rh_over_Delta (float), Nd (float)",
          "magnetization_curve": "array of objects with field_mub_H_over_Delta (float) and magnetization_mub_per_fu (float)"
        }
      },
      "description": "Magnetization per formula unit of FeRh as a function of external field at T=0, obtained from self-consistent torque balance."
    }
  ],
  "notes": "All energies and fields are expressed in units of the virtual level half-width Δ. The agent must implement the self-consistent solver from the paper's formalism and produce the stated JSON artifacts; the checker compares key features (envelope, harmonic ratio, CDW amplitude, saturation magnetization, critical field, curve shape) against hidden paper-reported values with suitable tolerances."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that examines each output file independently. The verifier extracts the relevant quantities from the two JSON artifacts and compares them to reference values that are kept hidden. The checks include the magnetic moment per plane envelope, the harmonic ratio, the charge density wave amplitude, and the shape, saturation value, and critical field of the magnetization curve. Each scored stage contributes a weighted component to the final reward; the sum of the weights is 1.0. The comparison accounts for the expected spread between different correct implementations of the self‑consistent solver. You must produce exactly the artifacts listed in the workflow steps; simply reporting numbers from the literature is not sufficient to earn the full score.
