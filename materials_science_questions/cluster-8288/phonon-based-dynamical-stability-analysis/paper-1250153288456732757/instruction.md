# Elastic constants and maximum optical phonon frequency of a tetragonal carbon allotrope

## Problem background
Carbon allotropes with mixed sp²/sp³ hybridization are of interest for designing hard, stable materials. The tetragonal C₆ allotrope features allene-like >C=C=C< tricarbon units (sp²) embedded in a diamond-like tetrahedral (sp³) network. Calculations are needed to determine whether this structure is mechanically and dynamically stable and to evaluate its elastic constants, polycrystalline moduli, hardness, and phonon spectrum.

## Approach
The workflow uses plane-wave density functional theory (DFT) with the GGA-PBE exchange-correlation functional and projector augmented wave (PAW) pseudopotentials. First, the atomic positions and cell parameters are relaxed until low forces and stress thresholds are reached. From the optimized geometry, single-crystal elastic constants are computed by applying finite homogeneous deformations and deriving the strain–stress relationship. Polycrystalline bulk and shear moduli are obtained by Voigt averaging formulas for tetragonal systems, and the Vickers hardness is estimated with the Chen model: H_V = 0.92 (G_V / B_V)^{1.137} G_V^{0.708}. Independently, the phonon dispersion is calculated using the finite displacement method in a supercell, and the highest optical phonon frequency is identified.

## Reproduction target
For the specified C₆ structure (space group P¯4m2, a = 2.624 Å, c = 6.029 Å, and the atomic positions listed in the workflow), produce the six single-crystal elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, C₆₆ (in GPa), the Voigt-averaged bulk modulus B_V and shear modulus G_V (GPa), the Vickers hardness H_V (GPa), and the maximum optical phonon frequency (THz). Write the first group into step_01_elastic_properties.json and the phonon frequency into step_02_phonon.json.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Phonopy: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: DFT geometry optimization of C6
- Role: process
- Action: Perform DFT geometry optimization of the C6 structure (space group P-4m2, initial lattice parameters a=2.624 Å, c=6.029 Å, atomic coordinates as in Table 1 of the paper). Use a plane-wave DFT code with the GGA-PBE functional and PAW pseudopotentials. Relax atomic positions and cell parameters until forces and stress components are below tight thresholds.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Elastic constants and derived mechanical properties of C6
- Role: scored (load-bearing)
- Action: From the optimized C6 structure, compute the single-crystal elastic constants C11, C12, C13, C33, C44, C66 (all in GPa) by applying finite homogeneous deformations and deriving the elastic constants from the strain–stress relationship. Using Voigt averaging formulas for tetragonal systems, compute the polycrystalline bulk modulus B_V and shear modulus G_V. Compute the Vickers hardness H_V using the Chen model. Write the results into a JSON file.
- Output file: `/app/outputs/step_01_elastic_properties.json`
- Format: json
- Contract: {"C11": number, "C12": number, "C13": number, "C33": number, "C44": number, "C66": number, "B_V": number, "G_V": number, "H_V": number} (all in GPa)
- Scoring: scored by hidden verifier

### Step 3: Maximum optical phonon frequency of C6
- Role: scored
- Action: Using the optimized C6 structure, compute the phonon dispersion via the finite displacement method (supercell approach) with Phonopy or an equivalent interface. From the calculated phonon frequencies, identify the maximum optical phonon frequency and write it into a JSON file.
- Output file: `/app/outputs/step_02_phonon.json`
- Format: json
- Contract: {"max_frequency_THz": number} (in THz)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_properties.json`
- `/app/outputs/step_02_phonon.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_properties.json
- path: `/app/outputs/step_01_elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduced single-crystal elastic constants and derived polycrystalline elastic moduli and Vickers hardness for C6.
- schema:
  - `type`: object
  - `required`:
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C13`: number (GPa)
    - `C33`: number (GPa)
    - `C44`: number (GPa)
    - `C66`: number (GPa)
    - `B_V`: number (GPa)
    - `G_V`: number (GPa)
    - `H_V`: number (GPa)

### step_02_phonon.json
- path: `/app/outputs/step_02_phonon.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum optical phonon frequency of the C6 allotrope.
- schema:
  - `type`: object
  - `required`:
    - `max_frequency_THz`: number (THz)

Notes: The acceptable tolerance for each quantity accounts for the natural spread between different DFT implementations and settings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C13": "number (GPa)",
          "C33": "number (GPa)",
          "C44": "number (GPa)",
          "C66": "number (GPa)",
          "B_V": "number (GPa)",
          "G_V": "number (GPa)",
          "H_V": "number (GPa)"
        }
      },
      "description": "Reproduced single-crystal elastic constants and derived polycrystalline elastic moduli and Vickers hardness for C6."
    },
    {
      "file": "step_02_phonon.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "max_frequency_THz": "number (THz)"
        }
      },
      "description": "Maximum optical phonon frequency of the C6 allotrope."
    }
  ],
  "notes": "The acceptable tolerance for each quantity accounts for the natural spread between different DFT implementations and settings."
}
```

## How you are scored
A hidden verifier independently scores the two scored workflow stages. For the elastic properties, each computed constant, modulus, and hardness value is compared to reference values with appropriate tolerances. For the phonon stage, the maximum frequency is compared to a reference. The final reward is the weighted sum of these stage-level scores; simply reporting numbers without performing the DFT calculations will not yield correct results.
