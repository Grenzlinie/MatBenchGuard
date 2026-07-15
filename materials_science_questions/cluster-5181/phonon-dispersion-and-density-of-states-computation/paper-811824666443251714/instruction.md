# Soft-phonon instability and zincblende-to-C222₁ transition in HgSe and HgTe from DFT calculations

## Problem background
The mercury chalcogenides HgSe and HgTe crystallise in the zincblende (zb) structure at ambient conditions. Under moderate compression, the zb phases develop a soft-phonon instability in the transverse-acoustic (TA) branch that drives a displacive transition to a metastable orthorhombic phase with space group C222₁. Density-functional theory (DFT) calculations within the local-density approximation (LDA) have been used to characterise this instability by computing equilibrium volumes, bulk moduli, phonon frequencies (including the soft TA mode at the Brillouin-zone boundary X point), and the relaxed structural parameters of the C222₁ phase. The task is to reproduce these calculated quantities and thereby verify the soft-mode mechanism.

## Approach
The reproduction employs an open-source plane-wave DFT code with projector-augmented wave (PAW) LDA pseudopotentials. The methodology consists of three main stages:

1. **Equation of state of the zb phases:** Total energy as a function of volume is computed for zb HgSe and zb HgTe. The resulting E(V) data are fitted to a Murnaghan equation of state to obtain the zero-pressure equilibrium volume V₀ and bulk modulus B₀ for each compound.

2. **Phonon frequencies:** The finite-displacement method is used in a supercell to compute phonon frequencies at the Γ point (transverse-optic, TO) and the X point (transverse-acoustic, TA) for both compounds. Calculations are performed at zero pressure (using the equilibrium volume from the EOS) and at a compressed volume corresponding to approximately 3 GPa, where the TA(X) mode is expected to soften.

3. **C222₁ structural relaxation:** The atomic positions and cell shape of the C222₁ phase (space group C222₁) are fully relaxed at the experimental volumes (53.2 Å³ for HgSe, 62.5 Å³ for HgTe) using the same DFT-LDA setup, yielding the axial ratios b/a and c/a and the internal fractional coordinates x(Hg) and y(Se/Te).

The entire workflow is executed independently from scratch; the only inputs are the crystal structures and the public LDA PAW pseudopotentials.

## Reproduction target
Produce three scored JSON files in `/app/outputs`:

1. **equilibrium_properties.json** – zero-pressure equilibrium volume V₀ (Å³) and bulk modulus B₀ (GPa) for zb-HgSe and zb-HgTe.
2. **phonon_frequencies.json** – for both compounds, the TO phonon frequency at Γ (THz) at zero pressure, and the TA phonon frequency at the X point (THz) at zero pressure and at a compressed volume near 3 GPa. The compressed volume should be chosen from the E(V) curve where the TA(X) mode softens; the exact volume is not enforced, only the resulting frequencies are scored.
3. **c2221_parameters.json** – relaxed structural parameters of the C222₁ phase at the experimental volumes (53.2 Å³ for HgSe, 62.5 Å³ for HgTe): axial ratios b/a and c/a and internal fractional coordinates x(Hg) and y(Se/Te), all dimensionless.

All calculations use DFT-LDA with PAW pseudopotentials. Output file schemas are given in the Workflow steps and the Output contract.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code with PAW support): https://www.quantum-espresso.org
- LDA PAW pseudopotentials for Hg, Se, Te: http://www.pseudo-dojo.org

## Workflow steps

### Step 1: DFT total energy vs volume for zincblende phases
- Role: process
- Action: Perform DFT-LDA calculations for the zincblende structures of HgSe and HgTe at a range of volumes spanning the experimental equilibrium volumes, using PAW pseudopotentials and a suitable k-point grid. Output total energies per formula unit as a function of volume.
- Evidence: `/app/outputs/energy_vs_volume_data.json`

### Step 2: Equilibrium volume and bulk modulus
- Role: scored (load-bearing)
- Action: Fit the E(V) data from step_01 to a Murnaghan equation of state and extract the zero-pressure equilibrium volume V0 and bulk modulus B0 for HgSe and HgTe. Write the values to equilibrium_properties.json.
- Output file: `/app/outputs/equilibrium_properties.json`
- Format: json
- Contract: JSON object with keys HgSe_V0 (float, Å³), HgSe_B0 (float, GPa), HgTe_V0 (float), HgTe_B0 (float).
- Scoring: scored by hidden verifier

### Step 3: Phonon frequency calculation for zincblende phases
- Role: process
- Action: Perform phonon calculations using the finite-displacement method in a supercell for zb-HgSe and zb-HgTe at the equilibrium zero-pressure volume (from the EOS) and at a compressed volume corresponding to approximately 3 GPa (choose a volume where TA(X) softening is expected). Compute the TO frequency at Γ and the TA frequency at the X point.
- Evidence: `/app/outputs/phonon_raw_frequencies.json`

### Step 4: Report phonon frequencies
- Role: scored
- Action: Extract from step_03 the required phonon frequencies: the TO frequency at Γ at zero pressure, the TA frequency at X at zero pressure, and the TA frequency at X at the compressed volume, for both compounds. Write to phonon_frequencies.json.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys HgSe_TO_Gamma_0GPa, HgSe_TA_X_0GPa, HgSe_TA_X_3GPa, HgTe_TO_Gamma_0GPa, HgTe_TA_X_0GPa, HgTe_TA_X_3GPa (all floats, THz).
- Scoring: scored by hidden verifier

### Step 5: C2221 structural relaxation
- Role: process
- Action: Fully relax the atomic positions and cell shape of the C2221 phase (space group C2221) for HgSe and HgTe at the experimental volumes (53.2 Å³ for HgSe, 62.5 Å³ for HgTe) using DFT-LDA.
- Evidence: `/app/outputs/c2221_relax_output.json`

### Step 6: Report C2221 structural parameters
- Role: scored
- Action: Extract the relaxed structural parameters from step_05: axial ratios b/a and c/a, and internal parameters x(Hg) and y(anion). Write to c2221_parameters.json.
- Output file: `/app/outputs/c2221_parameters.json`
- Format: json
- Contract: JSON object with keys HgSe_x, HgSe_y, HgSe_b_over_a, HgSe_c_over_a, HgTe_x, HgTe_y, HgTe_b_over_a, HgTe_c_over_a (all floats, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_properties.json`
- `/app/outputs/phonon_frequencies.json`
- `/app/outputs/c2221_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_properties.json
- path: `/app/outputs/equilibrium_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zero-pressure equilibrium volumes and bulk moduli of zincblende HgSe and HgTe.
- schema:
  - `type`: object
  - `required`:
    - `HgSe_V0`: float (Å³)
    - `HgSe_B0`: float (GPa)
    - `HgTe_V0`: float (Å³)
    - `HgTe_B0`: float (GPa)

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at Γ (TO) and X (TA) points at zero pressure and at ~3 GPa.
- schema:
  - `type`: object
  - `required`:
    - `HgSe_TO_Gamma_0GPa`: float (THz)
    - `HgSe_TA_X_0GPa`: float (THz)
    - `HgSe_TA_X_3GPa`: float (THz)
    - `HgTe_TO_Gamma_0GPa`: float (THz)
    - `HgTe_TA_X_0GPa`: float (THz)
    - `HgTe_TA_X_3GPa`: float (THz)

### c2221_parameters.json
- path: `/app/outputs/c2221_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: C2221 structural parameters at experimental volumes (53.2 Å³ for HgSe, 62.5 Å³ for HgTe).
- schema:
  - `type`: object
  - `required`:
    - `HgSe_x`: float (dimensionless)
    - `HgSe_y`: float (dimensionless)
    - `HgSe_b_over_a`: float (dimensionless)
    - `HgSe_c_over_a`: float (dimensionless)
    - `HgTe_x`: float (dimensionless)
    - `HgTe_y`: float (dimensionless)
    - `HgTe_b_over_a`: float (dimensionless)
    - `HgTe_c_over_a`: float (dimensionless)

Notes: All outputs are compared against the paper-reported hidden gold values with appropriate tolerances. The phonon frequencies at the compressed volume are for a volume chosen near 3 GPa where the TA(X) softening is expected; the exact volume is not enforced, only the resulting frequencies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "HgSe_V0": "float (Å³)",
          "HgSe_B0": "float (GPa)",
          "HgTe_V0": "float (Å³)",
          "HgTe_B0": "float (GPa)"
        }
      },
      "description": "Zero-pressure equilibrium volumes and bulk moduli of zincblende HgSe and HgTe."
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "HgSe_TO_Gamma_0GPa": "float (THz)",
          "HgSe_TA_X_0GPa": "float (THz)",
          "HgSe_TA_X_3GPa": "float (THz)",
          "HgTe_TO_Gamma_0GPa": "float (THz)",
          "HgTe_TA_X_0GPa": "float (THz)",
          "HgTe_TA_X_3GPa": "float (THz)"
        }
      },
      "description": "Phonon frequencies at Γ (TO) and X (TA) points at zero pressure and at ~3 GPa."
    },
    {
      "file": "c2221_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "HgSe_x": "float (dimensionless)",
          "HgSe_y": "float (dimensionless)",
          "HgSe_b_over_a": "float (dimensionless)",
          "HgSe_c_over_a": "float (dimensionless)",
          "HgTe_x": "float (dimensionless)",
          "HgTe_y": "float (dimensionless)",
          "HgTe_b_over_a": "float (dimensionless)",
          "HgTe_c_over_a": "float (dimensionless)"
        }
      },
      "description": "C2221 structural parameters at experimental volumes (53.2 Å³ for HgSe, 62.5 Å³ for HgTe)."
    }
  ],
  "notes": "All outputs are compared against the paper-reported hidden gold values with appropriate tolerances. The phonon frequencies at the compressed volume are for a volume chosen near 3 GPa where the TA(X) softening is expected; the exact volume is not enforced, only the resulting frequencies."
}
```

## How you are scored
A hidden verifier reads the three output files and compares each reported quantity to the expected reference values. The comparison uses tolerances that account for the differences between DFT implementations and pseudopotentials, so a faithful re-execution is expected to pass. The final reward is a weighted fraction of the criteria met:

- **equilibrium_properties.json** (weight 0.50) – all four quantities (V₀ and B₀ for both compounds) must fall within the acceptance window.
- **phonon_frequencies.json** (weight 0.25) – both compounds and both pressure conditions (zero pressure and compressed) must pass.
- **c2221_parameters.json** (weight 0.25) – all four parameters per compound (b/a, c/a, x, y) must pass.

Only the final JSON artifacts are evaluated; intermediate data are not scored. The reference values are not disclosed; you must produce them from scratch by running the described DFT workflow.
