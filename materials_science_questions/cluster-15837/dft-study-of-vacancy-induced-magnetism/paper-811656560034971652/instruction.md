# Magnetism from D3-symmetry tetra-vacancy defects in graphene

## Problem background
Graphene is intrinsically nonmagnetic, but introducing vacancy defects can induce magnetic ordering. A central open question is whether lattice relaxation around the defects suppresses or preserves magnetism, and whether passivation of dangling bonds can alter the outcome. This work addresses that question by studying D3-symmetry tetra-vacancy defects in graphene using spin-polarized density-functional theory (DFT). The objective is to compute the total magnetic moment and total energy of a graphene supercell containing these defects under three distinct atomic configurations: (i) unrelaxed ideal positions, (ii) fully relaxed (without hydrogen passivation), and (iii) hydrogen-passivated and then fully relaxed. Understanding how geometry relaxation and hydrogen saturation affect the induced magnetism is the core scientific goal.

## Approach
The workflow uses spin-polarized DFT with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and plane-wave basis sets. A 10×5×1 graphene supercell containing two D3-symmetry tetra-vacancy defects is constructed. The total magnetic moment is extracted as the difference between spin-up and spin-down integrated electron charges. Three scenarios are compared: (i) atomic positions fixed at the ideal graphene lattice (unrelaxed), (ii) full ionic relaxation of the defective sheet, and (iii) passivation of dangling bonds with hydrogen atoms (sp² hybridization) followed by full relaxation. All calculations are performed using an open-source DFT code (Quantum ESPRESSO) with appropriate pseudopotentials, allowing the effect of lattice relaxation and hydrogen passivation on the magnetic moment and total energy to be examined in a self-contained reproducible pipeline.

## Reproduction target
For a graphene supercell containing two D3-symmetry tetra-vacancy defects, perform DFT calculations to compute the total magnetic moment (in Bohr magnetons, μB) and total energy (in eV) for the following three atomic configurations:

1. **Unrelaxed** – all carbon atoms kept at ideal graphene lattice positions.
2. **Relaxed** – full ionic relaxation of all atoms until force convergence.
3. **Hydrogen-saturated** – each dangling bond saturated with a hydrogen atom placed in the sp² plane, followed by full ionic relaxation.

Save the resulting magnetic moment and total energy for each configuration and aggregate them into a single output file as specified in the workflow steps. The magnetic moment is defined as the difference in spin-up and spin-down electron populations in the converged electronic ground state.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase
- C pseudopotential (PBE, PAW): https://www.materialscloud.org/discover/sssp/table/precision
- H pseudopotential (PBE, PAW): https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Build initial supercell with defects
- Role: process
- Action: Using ASE, construct a 10×5×1 graphene supercell (100 carbon atoms in pristine form). Introduce two D3-symmetry tetra-vacancy defects, each removing four carbon atoms in D3 symmetry. Write the resulting atomic coordinates to unrelaxed.xyz.
- Evidence: `/app/outputs/unrelaxed.xyz`

### Step 2: DFT single-point on unrelaxed structure
- Role: process
- Action: Run a spin-polarized DFT single-point (SCF only) calculation on the unrelaxed structure using Quantum ESPRESSO with the PBE functional, appropriate pseudopotentials, a plane-wave cutoff ≥400 eV, and a 2×4×1 k-mesh. Extract total magnetic moment (in μB) and total energy (in eV). Save to unrelaxed_result.json.
- Evidence: `/app/outputs/unrelaxed_result.json`

### Step 3: Fully relax structure and compute magnetism (no H passivation)
- Role: process
- Action: Starting from the unrelaxed coordinates, perform full ionic relaxation using Quantum ESPRESSO until forces are below a tight threshold (e.g., 0.03 eV/Å). After convergence, run a final SCF to obtain total magnetic moment and total energy. Save to relaxed_result.json.
- Evidence: `/app/outputs/relaxed_result.json`

### Step 4: H-passivate, relax, and compute magnetism
- Role: process
- Action: Identify undercoordinated carbon atoms around each D3 tetra-vacancy defect. Attach hydrogen atoms to dangling bonds in the sp² plane. Fully relax the H-passivated structure using the same DFT settings, then run a final SCF to extract total magnetic moment and total energy. Save to hydrogen_passivated_result.json.
- Evidence: `/app/outputs/hydrogen_passivated_result.json`

### Step 5: Aggregate magnetic moments and energies
- Role: scored (load-bearing)
- Action: Read magnetic moment and total energy from unrelaxed_result.json, relaxed_result.json, and hydrogen_passivated_result.json. Assemble them into a JSON array ordered by condition: unrelaxed, relaxed, hydrogen_saturated. Write to magnetic_moments.json.
- Output file: `/app/outputs/magnetic_moments.json`
- Format: json
- Contract: A JSON array of three objects, each with keys: condition (string: 'unrelaxed', 'relaxed', 'hydrogen_saturated'), magnetic_moment (float, μB), total_energy (float, eV). The array must contain exactly these three entries in this order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.json
- path: `/app/outputs/magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: An array of three objects, ordered: unrelaxed, relaxed, hydrogen_saturated. Each object contains the condition name, total magnetic moment in Bohr magnetons, and total energy in eV.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `condition`:
        - `type`: string
        - `enum`: `unrelaxed`, `relaxed`, `hydrogen_saturated`
      - `magnetic_moment`:
        - `type`: number
        - `description`: Total magnetic moment in Bohr magnetons (μB)
      - `total_energy`:
        - `type`: number
        - `description`: Total energy in eV
    - `required`: `condition`, `magnetic_moment`, `total_energy`

Notes: The checker will compare magnetic_moment and total_energy to hidden reference values within appropriate tolerances. The exact DFT implementation details (plane-wave cutoff, k-mesh density, convergence thresholds) are left to the solver, as long as they follow standard practices for this system.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "condition": {
              "type": "string",
              "enum": [
                "unrelaxed",
                "relaxed",
                "hydrogen_saturated"
              ]
            },
            "magnetic_moment": {
              "type": "number",
              "description": "Total magnetic moment in Bohr magnetons (μB)"
            },
            "total_energy": {
              "type": "number",
              "description": "Total energy in eV"
            }
          },
          "required": [
            "condition",
            "magnetic_moment",
            "total_energy"
          ]
        }
      },
      "description": "An array of three objects, ordered: unrelaxed, relaxed, hydrogen_saturated. Each object contains the condition name, total magnetic moment in Bohr magnetons, and total energy in eV."
    }
  ],
  "notes": "The checker will compare magnetic_moment and total_energy to hidden reference values within appropriate tolerances. The exact DFT implementation details (plane-wave cutoff, k-mesh density, convergence thresholds) are left to the solver, as long as they follow standard practices for this system."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier that independently checks each stage of the workflow. The verifier reads the aggregated output file (`magnetic_moments.json`) and compares your computed magnetic moments and total energies against a set of hidden reference values derived from a faithful reproduction of the study. Credit is awarded based on how well your values agree with the references; simply reporting the paper's numbers without actually running the computational pipeline will not meet the verification criteria. The verifier may also enforce consistency constraints across the three conditions. The final reward is the weighted aggregate across all evaluated outputs.
