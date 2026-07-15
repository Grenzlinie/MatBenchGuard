# Grüneisen Parameter Calculation: Molecular Pressure and Specific Strain Energy

## Problem background
Micropipes are the primary macroscopic defects in silicon carbide single crystals. It is believed that a stable hollow core of a dislocation can serve as the initial site for micropipe development. In this model, the specific strain energy inside the dislocation core determines whether a hollow core can form thermodynamically. The central challenge is to estimate this specific strain energy from material properties that are accessible. Starting from a quasi-elastic expansion of the atomic interaction force, the core’s molecular (bond) pressure and specific strain energy can be expressed in terms of the Young’s modulus and the Grüneisen constant of the material. Your task is to compute these quantities numerically for silicon carbide and silicon using the provided material constants, and report the results in a structured JSON file.

## Approach
The key idea is to relate the harmonic and anharmonic force constants of the crystal lattice to macroscopic parameters. By expanding the quasi-elastic force to second order and linking the elastic force constant to Young’s modulus and the anharmonic constant to the Grüneisen coefficient, the molecular pressure inside the crystal becomes P_M = Y/(6η). The maximum atomic displacement before plastic deformation can also be expressed in terms of the Grüneisen constant. The specific strain energy at the dislocation core is then obtained from the molecular pressure and the expanded lattice volume at that displacement. You will first compute the lattice constant a0 from the molecular weight, density, and Avogadro’s number. Then compute the molecular pressure and, using the maximum displacement, the specific strain energy. Finally, convert the energy to kJ/mol.

## Reproduction target
Produce a JSON file, results.json, containing the molecular pressure (in Pa) and specific strain energy (in kJ/mol) for both SiC and Si. Use the material parameters listed in the workflow step below. The output must follow the exact schema: an object with keys "SiC" and "Si", each containing "P_M_Pa" (a float) and "U0_kJ_per_mol" (a float). All four values must be computed solely from the given constants; no external data or fitting is required.

## Assets
No external assets are needed. All necessary material constants (Young’s modulus, Grüneisen constant, density, molecular weight, Avogadro’s number) are provided in the workflow step; the computation uses only arithmetic.

## Workflow steps

### Step 1: Compute molecular pressure and specific strain energy for SiC and Si
- Role: scored (load-bearing)
- Action: Using the provided material parameters for SiC (Young's modulus Y=4.4e11 Pa, Grüneisen constant η=2, density ρ=3.2e3 kg/m³, molecular weight M=41 g/mol) and Si (Y=4.0e10 Pa, η=2, ρ=2.3e3 kg/m³, M=28.06 g/mol), compute the lattice constant a0 = (M/(N_A·ρ))^(1/3) with Avogadro's number N_A = 6.02214076e23 mol⁻¹. Then compute molecular pressure P_M = Y/(6η) (Pa). For each material, compute the molar volume Vm = (M / 1000) / ρ (m³/mol) (converting M from g/mol to kg/mol). Then compute the specific strain energy U0 = P_M * Vm * (1 + 1/(12η))^3 (J/mol), and convert to kJ/mol by dividing by 1000. Write the computed P_M (Pa) and U0 (kJ/mol) for both materials to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"SiC": {"P_M_Pa": float, "U0_kJ_per_mol": float}, "Si": {"P_M_Pa": float, "U0_kJ_per_mol": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored results file containing molecular pressure (Pa) and specific strain energy (kJ/mol) for SiC and Si.
- schema:
  - `SiC`:
    - `P_M_Pa`: number
    - `U0_kJ_per_mol`: number
  - `Si`:
    - `P_M_Pa`: number
    - `U0_kJ_per_mol`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "SiC": {
          "P_M_Pa": "number",
          "U0_kJ_per_mol": "number"
        },
        "Si": {
          "P_M_Pa": "number",
          "U0_kJ_per_mol": "number"
        }
      },
      "description": "Scored results file containing molecular pressure (Pa) and specific strain energy (kJ/mol) for SiC and Si."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your output file results.json and compare each of the four numeric values (SiC P_M, SiC U0, Si P_M, Si U0) against the reference values obtained from the paper’s formulas using the same constants. A tolerance will be applied to account for minor numerical differences. Each value contributes equally to the final score; the verifier combines them into a single reward between 0 and 1. You must write a valid JSON file at the specified path; missing or malformed output earns no credit.
