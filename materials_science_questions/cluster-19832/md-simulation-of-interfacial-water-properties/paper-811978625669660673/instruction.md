# Nonlocal Dielectric Solvent Model at Protein-Solvent Interface

## Problem background
Dielectric properties of the interfacial solvent at protein‑solvent boundaries influence electrostatic interactions (EI) that govern protein folding, binding, and recognition. Classical continuum models treat the solvent as a uniform high‑dielectric medium, ignoring short‑range nonlocal correlation effects that arise from the finite correlation length of water dipoles. This task evaluates a nonlocal electrostatic model in which the solvent’s dielectric response shows spatial dispersion, leading to a low‑dielectric interfacial water layer. The objective is to compute pair‑wise electrostatic interaction (PEI) energies between two charges in solvent near a planar protein‑like interface, cross‑media (one charge in solvent, one in protein) interaction energies, and slab‑model energies relevant to protein association, and to quantify how the effective dielectric function depends on distance and orientation relative to the interface.

## Approach
The model represents the protein medium as a uniform low‑dielectric (ε₁ = 4) and the aqueous solvent by a nonlocal bulk dielectric function with long‑wavelength dielectric constant εₛ = 78.3, short‑wavelength constant ε∗ = 6, and dipole correlation length L = 5 Å. At the planar interface, pair‑wise energies are expressed as Coulomb’s law with effective distance‑dependent permittivities that involve integrals over the interfacial response. The workflow computes: (i) the nonlocal PEI energy U₁₂₋NL and effective dielectric function εₑ𝒻𝒇₋NL for two charges in the solvent (same side); (ii) the nonlocal cross‑media energy U₁₃₋NL_cross and effective cross‑media permittivity εₑ𝒻𝒇₋NL_cross for one charge in solvent and one in protein; and (iii) the slab‑model electrostatic energy for a low‑dielectric (εₛₐₗ = 9) and a high‑dielectric (εₛₐₗ = 41.2) slab, representing the solvent layer between two associating proteins. For comparison, classical (local) counterparts using εₛ = 78.3 and εₛ = ε∗ = 6 are also evaluated. The calculations are purely analytical/numerical; all required parameters are public.

## Test points

### Points for same-side PEI (Steps 1 and 3)
The following (R, Z, Z0) points cover different regimes relative to the correlation length L=5 Å. All coordinates are in Å.

| R  | Z   | Z0  |
|----|-----|-----|
| 0  | 1.5 | 1.5 |
| 0  | 1.5 | 6.5 |
| 0  | 6.5 | 1.5 |
| 0  | 6.5 | 6.5 |
| 0  | 35  | 35  |
| 5  | 1.5 | 1.5 |
| 10 | 6.5 | 6.5 |

### Points for cross-media CPEI (Steps 2 and 4)
All Z are negative (in the protein region), Z0 are positive. Coordinates in Å.

| R  | Z    | Z0  |
|----|------|-----|
| 0  | -1.5 | 1.5 |
| 0  | -1.5 | 6.5 |
| 0  | -6.5 | 1.5 |
| 0  | -6.5 | 6.5 |
| 0  | -35  | 35  |
| 5  | -1.5 | 1.5 |
| 10 | -6.5 | 6.5 |

## Reproduction target
Implement the nonlocal dielectric model. Numerically evaluate the integrals Φ and Ψ and, from them, compute the effective permittivities and interaction energies for a prescribed set of (R, Z, Z₀) points that probe different regimes of the interface (e.g., distances small or large compared to L, charges deep in solvent or near the interface). The three required scored artifacts are: (1) pe_energies.csv — U₁₂₋NL and εₑ𝒻𝒇₋NL for the same‑side PEI; (2) cpe_energies.csv — U₁₃₋NL_cross and εₑ𝒻𝒇₋NL_cross for the cross‑media case (Z negative, Z₀ positive); and (3) slab_energies.csv — the slab‑model energy Uₛₑₗ₁₂ for the two slab dielectric constants using the given geometry (R=0, Z=11 Å, d=6 Å). Additionally, produce the intermediate integral tables phi_values.csv and psi_values.csv as process evidence.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Evaluate nonlocal PEI correction integral Φ(R,Z,Z0)
- Role: process
- Action: Numerically evaluate the integral Φ(R,Z,Z0) defined by the paper's Eq. (8) using the parameters ε_s=78.3, ε_*=6, ε_1=4, L=5 Å, and for the test points listed in the Test points section (same-side PEI table). Save the computed values as a CSV file with columns R, Z, Z0, Phi.
- Evidence: `/app/outputs/phi_values.csv`

### Step 2: Evaluate nonlocal CPEI correction integral Ψ(R,Z,Z0)
- Role: process
- Action: Numerically evaluate the integral Ψ(R,Z,Z0) defined by the paper's Eq. (17) using the same parameters and for the test points listed in the Test points section (cross-media CPEI table). Save a CSV file with columns R, Z, Z0, Psi.
- Evidence: `/app/outputs/psi_values.csv`

### Step 3: Compute nonlocal PEI energy and effective dielectric function
- Role: scored (load-bearing)
- Action: Using the Φ values from the previous step and the explicit formulas (Coulomb law with effective distance-dependent permittivity), compute the nonlocal pair-wise electrostatic interaction energy U12_NL (dimensionless, normalized by 560 ξ1 ξ2 k_B T) and the effective dielectric function ε_eff_NL for each test point from the same-side PEI table in the Test points section. Output a CSV file with columns R, Z, Z0, U12_NL, epsilon_eff_NL.
- Output file: `/app/outputs/pe_energies.csv`
- Format: csv
- Contract: Columns: R (float, Å), Z (float, Å), Z0 (float, Å), U12_NL (float, unitless), epsilon_eff_NL (float, unitless).
- Scoring: scored by hidden verifier

### Step 4: Compute nonlocal cross-media interaction energy and effective cross-media dielectric function
- Role: scored
- Action: Using the Ψ values and the formulas (Coulomb law with effective cross-media permittivity), compute the nonlocal cross-media pair-wise electrostatic interaction energy U13_NL_cross (dimensionless) and the effective cross-media dielectric function ε_eff_NL_cross for each test point from the cross-media CPEI table in the Test points section. Output a CSV file with columns R, Z, Z0, U13_NL_cross, epsilon_eff_NL_cross.
- Output file: `/app/outputs/cpe_energies.csv`
- Format: csv
- Contract: Columns: R (float, Å), Z (float, Å, negative), Z0 (float, Å, positive), U13_NL_cross (float, unitless), epsilon_eff_NL_cross (float, unitless).
- Scoring: scored by hidden verifier

### Step 5: Compute slab-model electrostatic energy for protein association
- Role: scored
- Action: Implement the slab-model electrostatic energy formula (Eq. 21) with geometry parameters d=6 Å, R=0, Z=11 Å, ε_1=4. Compute the negative electrostatic energy U_slab_12 (in units of k_B T) for two cases: a low-dielectric slab with ε_slab=9 and a high-dielectric slab with ε_slab=41.2. Output a CSV file with columns case, epsilon_slab, U_slab_12.
- Output file: `/app/outputs/slab_energies.csv`
- Format: csv
- Contract: Columns: case (string, e.g. 'low_dielectric', 'high_dielectric'), epsilon_slab (float), U_slab_12 (float, in units of k_B T).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pe_energies.csv`
- `/app/outputs/cpe_energies.csv`
- `/app/outputs/slab_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pe_energies.csv
- path: `/app/outputs/pe_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nonlocal PEI energy and effective dielectric function computed at the specified test points. The checker compares the reported values to hidden reference values with a relative tolerance of 5%.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Z`, `Z0`, `U12_NL`, `epsilon_eff_NL`
  - `units`: object

### cpe_energies.csv
- path: `/app/outputs/cpe_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nonlocal cross-media PEI energy and effective cross-media dielectric function. The checker compares to hidden reference values with relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `R`, `Z`, `Z0`, `U13_NL_cross`, `epsilon_eff_NL_cross`
  - `units`: object

### slab_energies.csv
- path: `/app/outputs/slab_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Slab-model electrostatic energies for the protein association application. The checker compares the reported U_slab_12 values to the paper's stated values (approx. 11.7 k_B T for ε_slab=9 and 6.7 k_B T for ε_slab=41.2) with an absolute tolerance of 0.5 k_B T.
- schema:
  - `type`: table
  - `required_columns`: `case`, `epsilon_slab`, `U_slab_12`
  - `units`: object

Notes: All outputs are compared to hidden reference values derived from the paper's formulas. For pe_energies and cpe_energies, a relative tolerance absorbs numerical integration differences. For slab_energies, an absolute tolerance is used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pe_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Z",
          "Z0",
          "U12_NL",
          "epsilon_eff_NL"
        ],
        "units": {}
      },
      "description": "Nonlocal PEI energy and effective dielectric function computed at the specified test points. The checker compares the reported values to hidden reference values with a relative tolerance of 5%."
    },
    {
      "file": "cpe_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "Z",
          "Z0",
          "U13_NL_cross",
          "epsilon_eff_NL_cross"
        ],
        "units": {}
      },
      "description": "Nonlocal cross-media PEI energy and effective cross-media dielectric function. The checker compares to hidden reference values with relative tolerance."
    },
    {
      "file": "slab_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "epsilon_slab",
          "U_slab_12"
        ],
        "units": {}
      },
      "description": "Slab-model electrostatic energies for the protein association application. The checker compares the reported U_slab_12 values to the paper's stated values (approx. 11.7 k_B T for ε_slab=9 and 6.7 k_B T for ε_slab=41.2) with an absolute tolerance of 0.5 k_B T."
    }
  ],
  "notes": "All outputs are compared to hidden reference values derived from the paper's formulas. For pe_energies and cpe_energies, a relative tolerance absorbs numerical integration differences. For slab_energies, an absolute tolerance is used."
}
```

## How you are scored
A hidden verifier will check each scored output file separately. For pe_energies.csv and cpe_energies.csv, the verifier compares the computed U and εₑ𝒻𝒇 values against reference values obtained from a correct implementation of the nonlocal formulas at the same (R,Z,Z₀) points; it also verifies that the effective permittivity approaches the expected classical limit (εₛ+ε₁)/2 at large separations. For slab_energies.csv, the verifier compares the reported Uₛₑₗ₁₂ values to the results expected from the slab‑model formula with the given dielectric constants. Each scored file contributes a portion of the total reward; the final score is the weighted sum. Producing correct numbers from a faithful implementation of the model is required; merely reporting the target values without the underlying computation is insufficient.
