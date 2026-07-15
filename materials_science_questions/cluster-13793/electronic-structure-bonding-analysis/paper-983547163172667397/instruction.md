# Mechanical Properties of Doped Cu₃P Alloys from DFT Calculations

## Problem background
Copper–phosphorus brazing alloys based on the Cu₃P phase are widely used in electronics and aerospace, but their room-temperature plasticity and mechanical properties need improvement. Alloying with additional elements is a practical route to tailor stiffness, shear resistance, and hardness. First-principles density functional theory (DFT) calculations can predict how different dopants affect the elastic moduli, Poisson's ratio, and Vickers hardness of the Cu₃P crystal structure. This task reproduces the computed mechanical properties for pristine Cu₃P and several doped systems, comparing the effects of different substitutional dopants on the material's hardness.

## Approach
The mechanical properties are obtained from DFT total-energy calculations using the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional and plane-wave basis sets. For each system, the crystal structure is first relaxed to its ground-state geometry. Elastic constants are then computed by applying small finite strains and extracting the stress response. The single-crystal elastic constants are converted to polycrystalline bulk modulus, shear modulus, and Young's modulus using Voigt–Reuss–Hill averaging. Poisson's ratio follows from the isotropic moduli, and the Vickers hardness is estimated with an empirical formula that relates hardness to the shear and bulk moduli. The workflow is implemented with the open-source Quantum ESPRESSO code and standard PBE pseudopotentials. Five systems are studied: pristine Cu₃P and four doped variants in which a single atom is substituted—CuPIn (Cu replaced by In), CuPSi (P replaced by Si), CuPSc (Cu replaced by Sc), and CuPTa (Cu replaced by Ta).

## Reproduction target
Compute and report the polycrystalline bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Vickers hardness for pristine Cu₃P and the four doped systems CuPIn, CuPSi, CuPSc, and CuPTa. All values must be derived from the elastic constants obtained via the DFT workflow described in the steps below. The results should allow a clear determination of whether each dopant (In, Si, Sc, Ta) increases or decreases the hardness relative to pristine Cu₃P.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Cu₃P crystal structure (Materials Project mp-2734): https://next-gen.materialsproject.org/materials/mp-2734

## Workflow steps

### Step 1: DFT geometry optimization and elastic constant calculations
- Role: process
- Action: Using Quantum ESPRESSO with the PBE functional and SSSP efficiency pseudopotentials, perform geometry optimizations and elastic constant calculations (finite-difference strain method) for pristine Cu₃P and the four doped systems: CuPIn (replace one Cu with In), CuPSi (replace one P with Si), CuPSc (replace one Cu with Sc), CuPTa (replace one Cu with Ta). Save all raw DFT outputs including optimized structures and elastic constants; the downstream step depends on these results.
- Evidence: none

### Step 2: Compute and report mechanical properties
- Role: scored (load-bearing)
- Action: From the elastic constants obtained in step 1, compute for each system the polycrystalline bulk modulus (B), shear modulus (G), and Young's modulus (E) using Voigt-Reuss-Hill averaging. Then compute Poisson's ratio ν = (3B - 2G) / [2(3B + G)]. Finally, compute the Vickers hardness Hv using the empirical formula Hv = 2·(G/B)²·G⁰.⁵⁸⁵ - 3. Report all computed values in the JSON file specified.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"systems": [{"name": "string", "bulk_modulus_GPa": number, "shear_modulus_GPa": number, "youngs_modulus_GPa": number, "poisson_ratio": number, "hardness_GPa": number}, ...]}  // one entry per system: "Cu3P", "CuPIn", "CuPSi", "CuPSc", "CuPTa"
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
- description: Mechanical properties (bulk modulus, shear modulus, Young's modulus, Poisson's ratio, Vickers hardness) for pristine Cu3P and the four doped systems derived from DFT elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `systems`: array of system objects
  - `items`:
    - `name`: string
    - `bulk_modulus_GPa`: number (GPa)
    - `shear_modulus_GPa`: number (GPa)
    - `youngs_modulus_GPa`: number (GPa)
    - `poisson_ratio`: number (dimensionless)
    - `hardness_GPa`: number (GPa)
  - `required_columns`:
  - `units`:
    - `bulk_modulus_GPa`: GPa
    - `shear_modulus_GPa`: GPa
    - `youngs_modulus_GPa`: GPa
    - `hardness_GPa`: GPa

Notes: The agent must compute these properties from the elastic constants; raw DFT outputs are not scored. Trends and tolerances are checked by the hidden verifier.

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
        "type": "object",
        "required": {
          "systems": "array of system objects"
        },
        "items": {
          "name": "string",
          "bulk_modulus_GPa": "number (GPa)",
          "shear_modulus_GPa": "number (GPa)",
          "youngs_modulus_GPa": "number (GPa)",
          "poisson_ratio": "number (dimensionless)",
          "hardness_GPa": "number (GPa)"
        },
        "required_columns": [],
        "units": {
          "bulk_modulus_GPa": "GPa",
          "shear_modulus_GPa": "GPa",
          "youngs_modulus_GPa": "GPa",
          "hardness_GPa": "GPa"
        }
      },
      "description": "Mechanical properties (bulk modulus, shear modulus, Young's modulus, Poisson's ratio, Vickers hardness) for pristine Cu3P and the four doped systems derived from DFT elastic constants."
    }
  ],
  "notes": "The agent must compute these properties from the elastic constants; raw DFT outputs are not scored. Trends and tolerances are checked by the hidden verifier."
}
```

## How you are scored
A hidden verifier reads your `results.json` file and compares the reported moduli and hardness values for each system against a reference computed under comparable conditions. It also checks that the relative hardness ordering among the five systems is consistent with the expected trend for these dopants. Your score reflects the closeness of your computed values to the reference and the correctness of the hardness trends. Only the final `results.json` is scored; the raw DFT outputs are not scored but are required to produce the final result.
