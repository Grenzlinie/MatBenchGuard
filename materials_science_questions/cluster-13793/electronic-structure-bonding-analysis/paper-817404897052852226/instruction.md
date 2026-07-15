# First-Principles Study of Elastic and Electronic Properties of Cubic KCaF₃

## Problem background
Fluoro-perovskite materials of the form ABF3 are promising for energy conversion, information storage, and display applications owing to their strong ionic character, low phonon energy, and wide band gaps. Cubic KCaF3 is a member of this family for which a systematic theoretical understanding of its electronic structure, elastic behaviour, thermal properties (Debye temperature), and elastic anisotropy is needed to guide materials design. First-principles density functional theory (DFT) provides a route to compute these properties from the crystal structure without empirical input.

## Approach
Use an open‑source plane‑wave DFT code (e.g. Quantum ESPRESSO) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. Begin from the cubic Pm‑3m perovskite structure of KCaF3 and perform full geometry optimisation to obtain the equilibrium lattice constant. On the optimised structure, calculate the electronic band structure to determine the indirect band gap. Next, compute the three independent elastic constants (C11, C12, C44) of the cubic system via the stress‑strain method. From these, apply Voigt–Reuss–Hill averaging to obtain the homogenised bulk (B_H), shear (G_H) and Young’s (E_H) moduli; compute the Debye temperature from the Hill average wave velocities and the density derived from the lattice constant and atomic masses; finally, compute the directional Young’s moduli E[100], E[110], E[111] using the standard cubic elastic relations.

## Reproduction target
Compute the equilibrium lattice constant (Å), the indirect band gap (eV), the elastic constants C11, C12, C44 (GPa), the Voigt–Reuss–Hill homogenised moduli B_H, G_H, E_H (GPa), the Debye temperature (K), and the directional Young’s moduli E[100], E[110], E[111] (GPa) of cubic KCaF3. Report all quantities in a single JSON file.

## Assets

- KCaF₃ crystal structure description (cubic Pm-3m)
- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- PBE pseudopotentials for K, Ca, F: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Geometry optimization of KCaF₃
- Role: process
- Action: Perform DFT geometry optimization of cubic KCaF₃ (space group Pm-3m) using Quantum ESPRESSO with the PBE functional. Relax both the lattice parameter and atomic positions to obtain the equilibrium lattice constant. Save the optimized structure (e.g., as a CIF or input file) and record the final lattice constant in a text file.
- Evidence: `/app/outputs/optimized_structure.cif`

### Step 2: Electronic structure and band gap calculation
- Role: process
- Action: Using the optimized structure from step_01, perform a DFT calculation to obtain the electronic band structure and determine the indirect band gap. Write the calculated indirect band gap value (in eV) to a text file.
- Evidence: `/app/outputs/band_gap.txt`

### Step 3: Elastic constants calculation
- Role: process
- Action: Using the optimized structure from step_01, compute the three independent elastic constants (C₁₁, C₁₂, C₄₄) of cubic KCaF₃ via the stress–strain method with Quantum ESPRESSO. Write the constants as a JSON file with keys C11, C12, C44, values in GPa.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 4: Final property computation and scored output
- Role: scored (load-bearing)
- Action: Aggregate the lattice constant from step_01, the band gap from step_02, and the elastic constants from step_03. Compute the Voigt–Reuss–Hill homogenized moduli B_H, G_H, E_H (GPa), the Debye temperature (K) using the Hill average wave velocities and density derived from the lattice constant and atomic masses, and the directional Young's moduli E[100], E[110], E[111] (GPa). Write all quantities to a JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {"lattice_constant": number (Å), "band_gap": number (eV), "C11": number (GPa), "C12": number (GPa), "C44": number (GPa), "B_H": number (GPa), "G_H": number (GPa), "E_H": number (GPa), "Debye_temperature": number (K), "E_100": number (GPa), "E_110": number (GPa), "E_111": number (GPa)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated computed properties of cubic KCaF₃: lattice constant, indirect band gap, elastic constants, Voigt–Reuss–Hill homogenized moduli, Debye temperature, and directional Young’s moduli. The hidden checker compares each field to the paper’s reference values using tolerances appropriate for DFT reproducibility.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant`: number (Å)
    - `band_gap`: number (eV)
    - `C11`: number (GPa)
    - `C12`: number (GPa)
    - `C44`: number (GPa)
    - `B_H`: number (GPa)
    - `G_H`: number (GPa)
    - `E_H`: number (GPa)
    - `Debye_temperature`: number (K)
    - `E_100`: number (GPa)
    - `E_110`: number (GPa)
    - `E_111`: number (GPa)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `lattice_constant`: Å
    - `band_gap`: eV
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B_H`: GPa
    - `G_H`: GPa
    - `E_H`: GPa
    - `Debye_temperature`: K
    - `E_100`: GPa
    - `E_110`: GPa
    - `E_111`: GPa

Notes: All fields are numerical scalars; missing or non-numeric fields will score zero for that property. The final score is based on the proportion of properties that meet the hidden tolerance criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant": "number (Å)",
          "band_gap": "number (eV)",
          "C11": "number (GPa)",
          "C12": "number (GPa)",
          "C44": "number (GPa)",
          "B_H": "number (GPa)",
          "G_H": "number (GPa)",
          "E_H": "number (GPa)",
          "Debye_temperature": "number (K)",
          "E_100": "number (GPa)",
          "E_110": "number (GPa)",
          "E_111": "number (GPa)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "lattice_constant": "Å",
          "band_gap": "eV",
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B_H": "GPa",
          "G_H": "GPa",
          "E_H": "GPa",
          "Debye_temperature": "K",
          "E_100": "GPa",
          "E_110": "GPa",
          "E_111": "GPa"
        }
      },
      "description": "Aggregated computed properties of cubic KCaF₃: lattice constant, indirect band gap, elastic constants, Voigt–Reuss–Hill homogenized moduli, Debye temperature, and directional Young’s moduli. The hidden checker compares each field to the paper’s reference values using tolerances appropriate for DFT reproducibility."
    }
  ],
  "notes": "All fields are numerical scalars; missing or non-numeric fields will score zero for that property. The final score is based on the proportion of properties that meet the hidden tolerance criteria."
}
```

## How you are scored
A hidden verifier independently scores each field of your `computed_properties.json` against expected values with domain‑appropriate tolerances. The final reward is the weighted combination of these field‑level scores (range 0–1). Reporting numbers alone is not sufficient; the verifier expects the values to result from genuine DFT calculations and post‑processing as described in the workflow.
