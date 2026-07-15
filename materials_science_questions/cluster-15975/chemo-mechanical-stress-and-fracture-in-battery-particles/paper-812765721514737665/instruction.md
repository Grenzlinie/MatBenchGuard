# Mechanics of Diffusion-Induced Fractures in Battery Particles

## Problem background
Li-ion battery cathode material LiFePO₄ undergoes a phase transformation from lithiated (LiFePO₄) to delithiated (FePO₄) during cycling, accompanied by a 5.03% expansion along the a-axis and a 1.9% contraction along the c-axis. This misfit generates significant stress at the coherent phase boundary, which can nucleate and propagate interfacial cracks, leading to capacity fade. Understanding the fracture behaviour requires quantifying the energy release rates and stress intensity factors for cracks at the phase boundary as functions of particle size and crack length. This task computes these fracture parameters for a plate-like particle with an interfacial crack under plane stress.

## Approach
The problem is modelled as a two‑phase plate under plane stress with orthotropic elastic properties for both phases. An interfacial crack of variable length is placed at the phase boundary, and the particle sizes are taken as 500×300×225 nm, 200×120×90 nm, and 100×60×45 nm. The virtual crack closure technique (VCCT) is applied within a finite element framework to extract the mode I and mode II energy release rates (G_I, G_II), the total energy release rate G_T = G_I + G_II, and the mode I stress intensity factor K_I. Crack propagation is evaluated by comparing G_T to twice the surface energy (2γ = 1.32 N/m): if G_T exceeds this threshold, the crack is predicted to advance. Post‑processing computes the excess energy ΔE = G_T − 2γ and the estimated crack extension da = (ΔE · L) / (b · γ), where L is the crack length and b is the particle dimension along the b‑axis. The simulation is carried out for a range of normalized crack lengths L/d from 0.05 to 0.8.

## Reproduction target
Produce a CSV file named 'simulation_results.csv' under /app/outputs containing the computed results for all three particle sizes and the full set of crack‑length ratios (L/d = 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 where data are available). The table must have columns: a_size (nm), b_size (nm), c_size (nm), L/d, GI (N/m), GII (N/m), GT (N/m), KI (MPa·m^0.5), DeltaE (N/m), da (nm). Each row corresponds to one (particle size, crack length) combination. The results must be obtained by re‑implementing the VCCT procedure in an open‑source finite element solver; simply copying numbers from any reference is not acceptable.

## Assets

- FEniCS: fenics
- NumPy: numpy

## Workflow steps

### Step 1: Generate FE model
- Role: process
- Action: Create a 2D plane-stress finite element model of a two-phase LiFePO4/FePO4 plate with an interfacial crack. Define three particle sizes (a×b×c: 500×300×225 nm, 200×120×90 nm, 100×60×45 nm) and a range of crack lengths (L/d = 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8). Assign orthotropic elastic constants from literature and apply displacement boundary conditions corresponding to misfit strains (ε_a = 5.03%, ε_c = -1.9%). Mesh with 8-node quadrilateral elements, and save the model for reuse.
- Evidence: `/app/outputs/mesh_data.h5`

### Step 2: Run VCCT simulation and crack analysis
- Role: scored (load-bearing)
- Action: Load the model from Step 1. Implement the virtual crack closure technique (VCCT) within the open-source solver FEniCS to compute mode I, mode II, and total energy release rates (GI, GII, GT) and mode I stress intensity factor (KI) for every particle size and L/d combination. Post-process to obtain ΔE = GT - 2γ (where γ = 0.66 N/m) and estimate crack extension da = (ΔE * L) / (b * γ). Write all results to simulation_results.csv with the specified columns.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with header: a_size,b_size,c_size,L/d,GI,GII,GT,KI,DeltaE,da. Units: sizes in nm, GI,GII,GT,DeltaE in N/m, KI in MPa·m^0.5, da in nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fracture mechanics results from VCCT simulations for all particle sizes and crack lengths. Each row corresponds to one particle size and L/d combination.
- schema:
  - `type`: table
  - `required_columns`: `a_size`, `b_size`, `c_size`, `L/d`, `GI`, `GII`, `GT`, `KI`, `DeltaE`, `da`
  - `units`:
    - `a_size`: nm
    - `b_size`: nm
    - `c_size`: nm
    - `L/d`: 
    - `GI`: N/m
    - `GII`: N/m
    - `GT`: N/m
    - `KI`: MPa·m^0.5
    - `DeltaE`: N/m
    - `da`: nm

Notes: The hidden checker compares each row's GI, GII, GT, KI values to the paper's Table 1 using relative tolerances, and verifies that for the 100 nm particle GT meets the 2γ threshold criterion.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a_size",
          "b_size",
          "c_size",
          "L/d",
          "GI",
          "GII",
          "GT",
          "KI",
          "DeltaE",
          "da"
        ],
        "units": {
          "a_size": "nm",
          "b_size": "nm",
          "c_size": "nm",
          "L/d": "",
          "GI": "N/m",
          "GII": "N/m",
          "GT": "N/m",
          "KI": "MPa·m^0.5",
          "DeltaE": "N/m",
          "da": "nm"
        }
      },
      "description": "Fracture mechanics results from VCCT simulations for all particle sizes and crack lengths. Each row corresponds to one particle size and L/d combination."
    }
  ],
  "notes": "The hidden checker compares each row's GI, GII, GT, KI values to the paper's Table 1 using relative tolerances, and verifies that for the 100 nm particle GT meets the 2γ threshold criterion."
}
```

## How you are scored
After you submit the file, a hidden verifier will automatically score your output. For each row, your computed GI, GII, GT, and KI are compared against reference values derived from the underlying physics; the score measures how well they agree. Additionally, the verifier checks that for the 100 nm particle your model predicts that GT is below the critical threshold 2γ = 1.32 N/m for crack‑length ratios L/d ≤ 0.2 and exceeds the threshold for L/d ≥ 0.3, consistent with the physical expectation that smaller particles better accommodate initial flaws. The final reward is the fraction of rows that satisfy both the numerical agreement and the threshold‑crossing condition. You must therefore faithfully implement the finite element VCCT simulation; reporting a fabricated table will not pass this check.
