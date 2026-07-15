# Pore-Load Modulus of Mesoporous Silicon: FEM and Analytical Model Reproduction

## Problem background
Porous materials deform when fluids fill their pores and exert capillary pressures on the pore walls. For mesoporous silicon with parallel, cylindrical, non-interconnected channels, this adsorption-induced deformation is described by the *pore-load modulus* M, which relates the internal pore pressure to the macroscopic strain. Understanding how M depends on the porosity φ and the elastic constants (Young's modulus E and Poisson's ratio ν) of the pore walls is important for both interpreting adsorption experiments and evaluating the mechanical properties of the pore walls themselves. This task reproduces the computational part of a study that proposed an analytical model for M/E as a function of φ and ν, and validated it against finite-element simulations and experimental data.

## Approach
The conceptual approach consists of two complementary computational methods that are compared against each other, followed by an inference step. 

- **Analytical model:** The pore-load modulus is approximated by treating the deformation of a pressurized cylindrical pore in an infinite plate. Symmetry arguments relate the swelling of a representative cylindrical domain (outer radius equal to half the nearest-neighbor distance) to the macroscopic strain, yielding a closed-form expression for the normalized modulus M/E as a function of porosity φ and Poisson's ratio ν. 
- **FEM simulations:** Finite-element simulations solve 2D plane-strain linear elasticity for a hexagonal lattice of cylindrical pores under a uniform internal pressure P. Periodic boundary conditions mimic an infinite array. Simulations are run at several porosities, and for each the average engineering strain is computed, from which the pore-load modulus M and the ratio M/E are extracted using the known bulk silicon Young's modulus E=130 GPa. 
- **Comparison and inference:** The FEM and analytical M/E values are compared to assess the analytical model. Finally, a reported experimental pore-load modulus M=34.5 GPa at φ=0.60 is used together with the analytical expression to *infer* the pore-wall Young's modulus E_wall – that is, to solve for E given M, φ, and ν.

## Reproduction target
Compute the dimensionless pore-load modulus ratio M/E at four porosities φ = 0.35, 0.45, 0.55, 0.65 from both a finite-element simulation (hexagonal lattice, 2D plane strain, E=130 GPa, ν=0.28) and the analytical model (using Poisson's ratio ν=0.28). Then, using the analytical model and the given experimental measurement M=34.5 GPa at φ=0.60, calculate the pore-wall Young's modulus E_wall. Assemble all results – the M/E values (from FEM and analytical) and the inferred E_wall (in GPa) – into a single JSON file as specified in the output contract.

## Assets

- Open-source FEM solver (e.g., FreeFEM, FEniCS): https://freefem.org/
- Bulk silicon elastic constants (E=130 GPa, ν=0.28 for ⟨100⟩ orientation)
- Experimental pore-load modulus M=34.5 GPa at φ=0.60

## Workflow steps

### Step 1: FEM simulation of pore-load modulus
- Role: process
- Action: Perform finite-element simulations of the pore-load modulus for a hexagonal arrangement of cylindrical pores under uniform internal pressure P. Use bulk silicon elastic constants E=130 GPa, ν=0.28, and a 2D plane-strain formulation. Run simulations at porosities φ = 0.35, 0.45, 0.55, 0.65. For each φ, determine the average engineering strain and compute M = P / average_strain, then calculate M_over_E = M/E. Store the intermediate results (porosity and M_over_E) in a JSON file.
- Evidence: `/app/outputs/fem_data.json`

### Step 2: Analytical model evaluation
- Role: process
- Action: Using the analytical expression M/E = 1/(2(1-ν²)) (φ⁻¹ - 1) with ν=0.28, compute the M/E ratio at φ=0.35, 0.45, 0.55, 0.65. Store the results as a JSON file containing objects with porosity and M_over_E.
- Evidence: `/app/outputs/analy_data.json`

### Step 3: Assemble reproduction results
- Role: scored (load-bearing)
- Action: Read the intermediate FEM and analytical data files. Combine the M/E values into a single JSON structure. Compute the inferred pore-wall Young's modulus E_wall from the experimental condition M=34.5 GPa at φ=0.60 using the inverted analytical formula: E_wall = 2 M (1-ν²) / (φ⁻¹ - 1) with ν=0.28. Write the complete results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"analytical": [{"porosity": "float", "M_over_E": "float"}], "fem": [{"porosity": "float", "M_over_E": "float"}], "inferred_E_GPa": "float"}
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
- target_policy: reference_match
- description: Contains the M/E ratios from analytical and FEM simulations at porosities 0.35, 0.45, 0.55, 0.65, and the inferred pore-wall Young's modulus (in GPa) from the experimental pore-load modulus at porosity 0.60.
- schema:
  - `type`: object
  - `required`:
    - `analytical`: array of objects with porosity (float) and M_over_E (float)
    - `fem`: array of objects with porosity (float) and M_over_E (float)
    - `inferred_E_GPa`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `porosity`: dimensionless
    - `M_over_E`: dimensionless
    - `inferred_E_GPa`: GPa

Notes: The checker will compare the reported M_over_E values to reference digitized values with a relative tolerance, and recompute the inferred E_wall from the known inputs to verify internal consistency.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "analytical": "array of objects with porosity (float) and M_over_E (float)",
          "fem": "array of objects with porosity (float) and M_over_E (float)",
          "inferred_E_GPa": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "porosity": "dimensionless",
          "M_over_E": "dimensionless",
          "inferred_E_GPa": "GPa"
        }
      },
      "description": "Contains the M/E ratios from analytical and FEM simulations at porosities 0.35, 0.45, 0.55, 0.65, and the inferred pore-wall Young's modulus (in GPa) from the experimental pore-load modulus at porosity 0.60."
    }
  ],
  "notes": "The checker will compare the reported M_over_E values to reference digitized values with a relative tolerance, and recompute the inferred E_wall from the known inputs to verify internal consistency."
}
```

## How you are scored
A hidden verifier will read your submitted `results.json` and independently score each component. 

- The FEM M/E values will be compared to reference values digitized from the original published figure for the same geometry, with an acceptable relative tolerance. 
- The analytical M/E values will be checked for internal consistency and against the FEM results. 
- The inferred pore-wall Young's modulus will be compared to the paper's inferred value (with tolerance) and also recomputed from the known inputs (M=34.5 GPa, φ=0.60, ν=0.28) to confirm that your derivation is correct. 

Each check contributes to a weighted reward between 0.0 and 1.0. Submitting correct results produced by genuine execution of the workflow is required; simply quoting numbers without performing the computations will not pass all checks.
