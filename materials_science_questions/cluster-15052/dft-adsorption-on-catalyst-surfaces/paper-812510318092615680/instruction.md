# Reproduce DFT energy barriers for ammonia oxidation on Ni-Cu-OOH and Ni-Cu-Fe-OOH catalyst surfaces

## Problem background
The ammonia oxidation reaction (AOR) is a promising route for utilizing ammonia as an energy carrier. Nickel-based oxyhydroxides are active and low-cost catalysts for AOR, but the reaction kinetics are often limited by slow NH3 adsorption on the surface. Doping NiOOH with copper and iron is a rational strategy for improving activity, yet the detailed reaction mechanism and the effect of codoping on energy barriers need to be systematically understood. Density functional theory (DFT) is used here to investigate the AOR mechanism on Ni-Cu-OOH and Ni-Cu-Fe-OOH surfaces and determine the energetics of elementary reaction steps.

## Approach
The DFT calculations employ the PBE functional with on-site Coulomb correction (Ueff=5.3 eV) and van der Waals corrections. The catalyst surface is modelled by a supercell slab of NiOOH, with Cu and Fe atoms substitutionally doped near the surface. The reaction pathway is mapped by nudged elastic band (NEB) calculations. First, the bifurcation between two possible routes—the N+N mechanism (sequential dehydrogenation of NH3 and subsequent N–N coupling) and the G-M mechanism (N–N bond formation before full dehydrogenation)—is examined to establish the dominant mechanism. Then, the complete N+N pathway consisting of five elementary steps (NH3 adsorption, three dehydrogenation steps, and N2 formation) is computed for both Ni-Cu-OOH and Ni-Cu-Fe-OOH. The resulting energy barriers are used to identify the rate-limiting step and to evaluate the impact of Fe codoping.

## Reproduction target
Using DFT (PBE+U, vdW correction), build slab models of Ni-Cu-OOH and Ni-Cu-Fe-OOH. Perform NEB calculations for the five elementary steps of the N+N mechanism: (1) NH3 adsorption, (2) NH3→NH2* dehydrogenation, (3) NH2*→NH* dehydrogenation, (4) NH*→N* dehydrogenation, and (5) N*+N*→N2 formation. Report the computed energy barrier (in eV) for each step in a structured CSV file. Then, identify the rate-limiting step (the step with the highest barrier) for each system and determine the factor by which the barrier of the rate-limiting step changes between Ni-Cu-OOH and Ni-Cu-Fe-OOH.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials (efficiency version): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): ase
- pymatgen: pymatgen

## Workflow steps

### Step 1: Optimize β-Ni(OH)2 unit cell
- Role: process
- Action: Perform DFT geometry optimization of bulk β-Ni(OH)2 to obtain equilibrium lattice parameters (a, b, c). Use PBE+U (Ueff=5.3 eV) and a converged k-point grid.
- Evidence: `/app/outputs/ni_oh2_lattice.json`

### Step 2: Build Ni-Cu-OOH and Ni-Cu-Fe-OOH surface slab models
- Role: process
- Action: Using the optimized Ni(OH)2 unit cell, construct a NiOOH surface slab (supercell with 60 Ni, 120 O, 60 H atoms) by removing one-side H atoms. Create one slab with a single Cu dopant (replacing one Ni) and another with Cu and Fe dopants (Fe placed near Cu). Ensure slabs include a vacuum layer.
- Evidence: `/app/outputs/slab_models.pkl`

### Step 3: NEB bifurcation step (mechanism selection)
- Role: process
- Action: On the Ni-Cu-Fe-OOH slab, set up NEB calculations for the two competing bifurcation steps: dehydrogenation of NH2* (N+N path) and N-N bond formation (G-M path). Compute the energy barriers to confirm that the N+N path is kinetically favored.
- Evidence: `/app/outputs/bifurcation_barriers.json`

### Step 4: NEB pathway barriers for N+N mechanism (scored)
- Role: scored (load-bearing)
- Action: On both the Ni-Cu-OOH and Ni-Cu-Fe-OOH slabs, perform NEB calculations for each of the five elementary steps of the N+N mechanism: (1) NH3 adsorption, (2) NH3→NH2* dehydrogenation, (3) NH2*→NH* dehydrogenation, (4) NH*→N* dehydrogenation, and (5) N*+N*→N2 formation. Record the computed energy barrier (in eV) for every step in a CSV file.
- Output file: `/app/outputs/energy_barriers.csv`
- Format: csv
- Contract: system (string), step_number (int), barrier_ev (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_barriers.csv
- path: `/app/outputs/energy_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed energy barriers for the five elementary steps of the N+N mechanism on Ni-Cu-OOH and Ni-Cu-Fe-OOH surfaces. Checked against paper-reported barriers with tolerances, and verified that Step 1 is the rate-limiting step and Fe codoping reduces barrier by approximately 4.5-fold.
- schema:
  - `type`: table
  - `required_columns`: `system`, `step_number`, `barrier_ev`
  - `units`:
    - `barrier_ev`: eV

Notes: The checker will compare individual barrier values to reference values and assess trends (rate-limiting step, exothermicity of N2 formation on codoped system). Charge difference analysis is omitted because it provides only qualitative isosurface maps without a numerical reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "step_number",
          "barrier_ev"
        ],
        "units": {
          "barrier_ev": "eV"
        }
      },
      "description": "Computed energy barriers for the five elementary steps of the N+N mechanism on Ni-Cu-OOH and Ni-Cu-Fe-OOH surfaces. Checked against paper-reported barriers with tolerances, and verified that Step 1 is the rate-limiting step and Fe codoping reduces barrier by approximately 4.5-fold."
    }
  ],
  "notes": "The checker will compare individual barrier values to reference values and assess trends (rate-limiting step, exothermicity of N2 formation on codoped system). Charge difference analysis is omitted because it provides only qualitative isosurface maps without a numerical reference."
}
```

## How you are scored
Your submission is evaluated automatically by a hidden verifier. The verifier reads `energy_barriers.csv` and compares each barrier value against hidden reference values (the original DFT result) using appropriate tolerances. It also checks that the rate-limiting step is correctly identified and that the change in the rate-limiting barrier between the two systems matches an expected trend. The final score is a weighted combination of the barrier accuracy and trend verification; the rate-limiting step and the barrier change carry higher weight. Do not attempt to locate or consult the source paper; scoring uses only the verifier's internal references.
