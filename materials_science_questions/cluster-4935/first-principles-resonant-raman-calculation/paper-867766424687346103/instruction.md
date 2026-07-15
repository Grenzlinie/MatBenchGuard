# Doping dependence of Raman D peak area in monolayer graphene from DFT and double-resonance theory

## Problem background
Defects in graphene give rise to characteristic Raman peaks (D and D'), whose intensities are widely used to quantify defect density. Electrostatic doping (Fermi level shift) modifies the electronic structure and scattering rates, and can therefore influence the intensities of these defect-activated peaks. Understanding how doping affects the D peak area is critical for reliable defect quantification in doped graphene, a condition encountered in many practical samples. In this task, we investigate the doping dependence of the normalized D peak integrated area ratio A(D)/A(G) in monolayer graphene, as predicted by a combination of first-principles calculations and double-resonance Raman theory.

## Approach
We adopt a two-stage approach. First, density functional perturbation theory (DFPT) using Quantum ESPRESSO calculates the phonon spectrum and electron-phonon matrix elements of monolayer graphene on a coarse q-point grid; these are then interpolated to a fine grid suitable for Raman intensity calculations. Second, a fifth-nearest-neighbour tight-binding model for graphene is combined with a point-defect scattering model (a weakened nearest-neighbour hopping parameter, with an effective defect strength parameter α_hopp) and a doping-dependent electron-electron scattering broadening term (γ_ee = 0.06|E_F|). The double-resonance D peak Raman intensity is computed by summing over all allowed scattering pathways (electron/hole, phonon/defect ordering) within the Fermi golden rule framework, for several Fermi levels E_F up to 0.7 eV. The G peak is used as a doping-independent normalization reference. The computed A(D)/A(G) ratio at each doping level is then normalized to its zero-doping value.

## Reproduction target
Produce a CSV file, `doping_dependence.csv`, with columns `E_F` (Fermi level in eV) and `normalized_A_D_over_A_G` (dimensionless). The normalized ratio is obtained by computing A(D)/A(G) at each E_F and dividing by the ratio at E_F = 0. At least 8 rows must be provided, covering E_F = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 eV. The CSV file is the sole scored artifact; the intermediate DFPT results should be saved as `phonon_interp.h5` for evidence.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Carbon norm-conserving pseudopotential (LDA): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFPT phonon and electron-phonon calculation
- Role: process
- Action: Run Quantum ESPRESSO to perform DFT ground-state calculation and DFPT for monolayer graphene in order to obtain phonon frequencies, eigenvectors, and electron-phonon matrix elements on a coarse q-point grid, then interpolate to a fine grid suitable for double-resonance calculations. Save the interpolated data for reuse.
- Evidence: `/app/outputs/phonon_interp.h5`

### Step 2: Compute doping dependence of A(D)/A(G)
- Role: scored (load-bearing)
- Action: Using the DFPT electron-phonon matrix elements, a fifth-nearest neighbour tight-binding model for graphene, a defect scattering model with α_hopp = 6.4×10^13 eV^2 cm^{-2}, and doping-dependent electron-electron scattering broadening (γ_ee = 0.06|E_F|), compute the double-resonance D peak Raman intensity by summing over all scattering pathways. Output the normalized A(D)/A(G) ratio for Fermi levels E_F = 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 eV, normalized to the value at E_F = 0.
- Output file: `/app/outputs/doping_dependence.csv`
- Format: csv
- Contract: CSV with columns: E_F (float, eV), normalized_A_D_over_A_G (float, dimensionless). At least 8 rows covering [0.0, 0.7] eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/doping_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### doping_dependence.csv
- path: `/app/outputs/doping_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Doping dependence of the normalized D peak area ratio computed from first-principles DFPT phonons and double-resonance Raman simulation. Values are normalized to the zero-doping ratio.
- schema:
  - `type`: table
  - `required_columns`: `E_F`, `normalized_A_D_over_A_G`
  - `units`:
    - `E_F`: eV
    - `normalized_A_D_over_A_G`: dimensionless

Notes: The agent must execute the DFPT process step before the scored simulation step. The scored artifact must contain at least 8 rows spanning E_F from 0.0 to 0.7 eV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "doping_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "E_F",
          "normalized_A_D_over_A_G"
        ],
        "units": {
          "E_F": "eV",
          "normalized_A_D_over_A_G": "dimensionless"
        }
      },
      "description": "Doping dependence of the normalized D peak area ratio computed from first-principles DFPT phonons and double-resonance Raman simulation. Values are normalized to the zero-doping ratio."
    }
  ],
  "notes": "The agent must execute the DFPT process step before the scored simulation step. The scored artifact must contain at least 8 rows spanning E_F from 0.0 to 0.7 eV."
}
```

## How you are scored
A hidden verifier inspects your submitted output files. It checks that `doping_dependence.csv` contains the required columns and at least 8 rows. It then performs structural checks: it verifies that the normalized value at E_F = 0 is within a tight tolerance of 1.0 (the ratio is self-normalized to the undoped value), and that the overall shape of the doping curve is physically plausible (e.g., no erratic non-monotonic behaviour). No direct comparison to the paper's reported numbers is performed. The verifier assigns a score between 0 and 1 based on these structural criteria, with most weight on the shape and normalization checks.
