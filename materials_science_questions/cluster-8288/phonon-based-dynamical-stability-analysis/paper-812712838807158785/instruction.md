# DFT-based mechanical and dynamical stability analysis of Li4P2S6

## Problem background
Solid-state electrolytes are key to safer all-solid-state batteries. Among lithium thiophosphates, Li4P2S6 (space group P-31m) is a candidate material whose mechanical stability, brittleness/ductility, hardness, and vibrational properties govern its practical viability. First-principles calculations can predict these properties, but they have not been systematically reproduced in an open-source workflow. This task asks you to compute the single‑crystal elastic constants, polycrystalline elastic moduli, Vickers hardness, and Γ‑point phonon spectrum of Li4P2S6 and to assess its mechanical and dynamical stability.

## Approach
Use density functional theory (DFT) with the GGA-PBE exchange-correlation functional and norm-conserving pseudopotentials to perform a full geometry optimization of Li4P2S6. From the relaxed structure, calculate the elastic stiffness tensor C_ij via a stress‑strain (or energy‑strain) approach for trigonal symmetry. Apply the Voigt‑Reuss‑Hill averaging scheme to derive polycrystalline bulk, shear, and Young’s moduli, Poisson’s ratio, and the B/G ratio; then compute Vickers hardness using a standard empirical relation. Finally, use density functional perturbation theory (DFPT) to obtain the 36 phonon frequencies at the Brillouin‑zone center (Γ point) and check for imaginary modes. All calculations should be carried out with the open‑source Quantum ESPRESSO package and a public plane‑wave pseudopotential library.

## Reproduction target
Produce the following numerical artifacts from the described DFT/DFPT workflow:
- The independent elastic constants (C_ij) for Li4P2S6 in trigonal symmetry (GPa).
- The Voigt‑Reuss‑Hill averaged polycrystalline moduli B, G, E, Poisson’s ratio σ, B/G ratio, and Vickers hardness H_v.
- A list of the 36 Γ‑point phonon frequencies (in cm⁻¹) and a boolean flag indicating whether any imaginary modes exist.
The aim is to faithfully re‑compute these quantities from the specified protocol, not to match any particular previously reported value.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library (e.g., SSSP Efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform full geometry optimization of Li4P2S6 crystal structure in space group P-31m (No. 162) using density functional theory (DFT) with GGA-PBE exchange-correlation functional and appropriate pseudopotentials. Start from the experimental structure: a=6.078 Å, c=6.599 Å; Li at 2c (1/3,2/3,0), Li at 2d (2/3,1/3,1/2), P at 2e (0,0,0.1672), S at 6k (0.3225,0,0.2471). Converge forces and stress to high accuracy.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Compute elastic stiffness tensor
- Role: scored (load-bearing)
- Action: Using the DFT-optimized crystal structure, compute the single-crystal elastic constants C_ij via the stress-strain (or energy-strain) method. Apply appropriate strain patterns for trigonal symmetry to extract all independent components.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: CSV with columns i, j, C_ij_GPa. One row per independent pair: (1,1), (1,2), (1,3), (1,4), (1,5), (3,3), (4,4), (6,6). All values in GPa.
- Scoring: scored by hidden verifier

### Step 3: Derive polycrystalline moduli and Vickers hardness
- Role: scored
- Action: From the elastic constants C_ij, compute the Voigt and Reuss bounds for bulk and shear moduli using the standard trigonal formulas, then obtain Hill averages. From these, compute Young's modulus, Poisson's ratio, B/G ratio, and Vickers hardness using H_v = 0.92 (B/G)^{1.137} G^{0.708}.
- Output file: `/app/outputs/polycrystalline_moduli.json`
- Format: json
- Contract: { "B_V": number, "B_R": number, "B": number, "G_V": number, "G_R": number, "G": number, "E": number, "sigma": number, "B_G": number, "H_v": number } (all moduli in GPa, sigma and B_G unitless)
- Scoring: scored by hidden verifier

### Step 4: Compute Γ-point phonon frequencies
- Role: scored
- Action: Using density functional perturbation theory (DFPT) on the DFT-optimized crystal structure, compute the phonon frequencies at the Brillouin zone center (Γ point). Verify that all modes have positive real frequencies, indicating dynamical stability.
- Output file: `/app/outputs/phonon_gamma_frequencies.json`
- Format: json
- Contract: { "gamma_frequencies": [float, ...] (36 positive numbers, in cm^{-1}), "has_imaginary_modes": false }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/polycrystalline_moduli.json`
- `/app/outputs/phonon_gamma_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic constants C_ij for trigonal Li4P2S6. The checker compares these to the paper's reported values with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `i`, `j`, `C_ij_GPa`
  - `units`:
    - `C_ij_GPa`: GPa

### polycrystalline_moduli.json
- path: `/app/outputs/polycrystalline_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Voigt-Reuss-Hill averaged polycrystalline moduli, Poisson's ratio, B/G ratio, and Vickers hardness. The checker compares these to reference values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `B_V`: number (GPa)
    - `B_R`: number (GPa)
    - `B`: number (GPa)
    - `G_V`: number (GPa)
    - `G_R`: number (GPa)
    - `G`: number (GPa)
    - `E`: number (GPa)
    - `sigma`: unitless
    - `B_G`: unitless
    - `H_v`: number (GPa)

### phonon_gamma_frequencies.json
- path: `/app/outputs/phonon_gamma_frequencies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Γ-point phonon frequencies. The checker verifies all frequencies are positive real numbers and has_imaginary_modes is false, indicating dynamical stability.
- schema:
  - `type`: object
  - `required`:
    - `gamma_frequencies`: array of 36 positive numbers (cm^{-1})
    - `has_imaginary_modes`: boolean

Notes: The task uses open-source Quantum ESPRESSO instead of the paper's proprietary CASTEP. Systematic differences are absorbed by the tolerances specified on the scoring side (hidden). Only the elastic constants, polycrystalline moduli, Vickers hardness, and Γ-point phonon frequencies are required; anisotropy, dielectric tensors, thermodynamic properties, and minimum thermal conductivity are excluded per the taskability scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "i",
          "j",
          "C_ij_GPa"
        ],
        "units": {
          "C_ij_GPa": "GPa"
        }
      },
      "description": "Single-crystal elastic constants C_ij for trigonal Li4P2S6. The checker compares these to the paper's reported values with an absolute tolerance."
    },
    {
      "file": "polycrystalline_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B_V": "number (GPa)",
          "B_R": "number (GPa)",
          "B": "number (GPa)",
          "G_V": "number (GPa)",
          "G_R": "number (GPa)",
          "G": "number (GPa)",
          "E": "number (GPa)",
          "sigma": "unitless",
          "B_G": "unitless",
          "H_v": "number (GPa)"
        }
      },
      "description": "Voigt-Reuss-Hill averaged polycrystalline moduli, Poisson's ratio, B/G ratio, and Vickers hardness. The checker compares these to reference values within tolerances."
    },
    {
      "file": "phonon_gamma_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "gamma_frequencies": "array of 36 positive numbers (cm^{-1})",
          "has_imaginary_modes": "boolean"
        }
      },
      "description": "Γ-point phonon frequencies. The checker verifies all frequencies are positive real numbers and has_imaginary_modes is false, indicating dynamical stability."
    }
  ],
  "notes": "The task uses open-source Quantum ESPRESSO instead of the paper's proprietary CASTEP. Systematic differences are absorbed by the tolerances specified on the scoring side (hidden). Only the elastic constants, polycrystalline moduli, Vickers hardness, and Γ-point phonon frequencies are required; anisotropy, dielectric tensors, thermodynamic properties, and minimum thermal conductivity are excluded per the taskability scope."
}
```

## How you are scored
A hidden verifier will independently check each of the three scored output files and combine the results into a final reward. The verifier will verify that the elastic constants are physically reasonable and numerically consistent with the trigonal symmetry, that the derived polycrystalline moduli and hardness are correctly computed from the elastic constants, and that the Γ‑point phonon frequencies are all real and positive (indicating dynamical stability). Simply reporting numbers is not enough — the verifier evaluates whether your outputs are the honest outcome of the described procedure.
