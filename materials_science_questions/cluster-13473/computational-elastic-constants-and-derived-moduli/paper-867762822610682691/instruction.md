# Effective Young's Moduli of Nanoporous Gold from MD and FEM Simulations

## Problem background
Nanoporous gold (NPG) made by dealloying exhibits an effective Young's modulus that is far lower than the classical Gibson-Ashby scaling prediction for open-cell foams. Two competing hypotheses have been proposed to explain this anomalous compliance: (i) network-level disorder, such as broken ligaments or irregular node connectivity, which reduces stiffness even if the individual ligaments behave as linearly elastic bulk gold; (ii) a nonlinear elastic response of the nanoscale ligaments themselves, caused by surface-induced stresses that soften the material at small sizes. Disentangling these contributions requires comparing the mechanical response of the same microstructure under two different constitutive descriptions: one that fully captures atomic-scale nonlinear elasticity, and one restricted to linear elasticity. This task computes that comparison.

## Approach
The strategy is to simulate uniaxial compression of a nanoporous gold network using two independent methods on the same initial configuration, then compare the resulting effective Young's moduli. The workflow consists of five stages:

1. **Bulk reference modulus** – Derive the isotropic polycrystalline Young's modulus of gold from the single-crystal elastic constants of the same interatomic potential that drives the atomistic simulation. This value feeds the Gibson-Ashby foam scaling law.

2. **Microstructure generation** – Create a three-dimensional bicontinuous porous network by simulating spinodal decomposition via Monte Carlo, producing a solid fraction around 0.30.

3. **Molecular dynamics (MD) simulation** – Perform a full atomistic simulation using an embedded-atom method (EAM) potential for gold. The protocol includes relaxation, thermal equilibration at 300 K, and compression with interspersed load/unload cycles. From the unloading segments, the secant modulus is extracted as the effective Young's modulus.

4. **Linear-elastic finite element (FEM) simulation** – Reconstruct the surface of the relaxed MD configuration using an alpha-shape algorithm, generate a volumetric mesh, and run a purely linear-elastic FEM analysis with the same elastic constants that underlie the EAM potential. The macroscopic reaction force at 0.02 compressive strain yields the effective Young's modulus.

5. **Gibson-Ashby prediction and final compilation** – Compute the Gibson-Ashby modulus from the bulk Young's modulus and the solid fraction, then collect all three moduli (MD, FEM, GA) and the solid fraction into a single scored JSON file.

The central comparison is between the MD result, which allows nanoscale nonlinear elasticity, and the linear-elastic FEM result, which excludes it. Any systematic difference between them isolates the role of nonlinear elastic effects, independent of network geometry.

## Reproduction target
The goal is to carry out the full pipeline and produce the file `/app/outputs/simulation_results.json` containing four numerical fields: `md_y_eff_GPa` (the effective Young's modulus from the MD simulation, in GPa), `fem_y_eff_GPa` (the effective Young's modulus from the FEM simulation, in GPa), `ga_y_eff_GPa` (the Gibson-Ashby prediction, in GPa), and `solid_fraction` (the solid fraction of the relaxed NPG structure, dimensionless). The pipeline must re-run the computational steps rather than rely on pre-computed values: generate the microstructure, run the MD compression to obtain a stress-strain curve, extract the secant modulus, perform the FEM linear-elastic calculation, compute the Gibson-Ashby estimate from the bulk modulus and solid fraction, and write the final JSON. All intermediate and final artifacts are written under `/app/outputs`.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- EAM potential for gold (Foiles, Baskes, Daw 1986): https://www.ctcms.nist.gov/potentials/entry/1986--Foiles-S-M-Baskes-M-I-Daw-M-S--Au/
- Alpha-shape surface reconstruction and meshing tool (OVITO or CGAL): https://www.ovito.org
- Open-source linear-elastic finite element solver (e.g., CalculiX): http://www.calculix.de
- Python with numpy and scipy

## Workflow steps

### Step 1: Compute isotropic Young's modulus from EAM elastic constants
- Role: process
- Action: Using the single-crystal elastic constants C11=183 GPa, C12=159 GPa, C44=45 GPa of the Au EAM potential, compute the isotropic polycrystalline Young's modulus Y_bulk via Kröner's formulation and write the result to a JSON file.
- Evidence: `/app/outputs/bulk_modulus.json`

### Step 2: Generate nanoporous gold microstructure via spinodal decomposition
- Role: process
- Action: Create an atomistic NPG network by simulating spinodal decomposition on an FCC lattice (144×144×144 spacings) using a Metropolis Monte Carlo algorithm with an Ising-type Hamiltonian. Remove one component to obtain a network with solid fraction ~0.30. Save the initial atomic configuration (LAMMPS data file) and record the solid fraction.
- Evidence: `/app/outputs/initial_npg.lammps`

### Step 3: Run MD compression simulation with load/unload and extract Y_eff
- Role: process
- Action: Using LAMMPS with the Au EAM potential, relax the initial configuration (energy minimization + thermal relaxation at 300 K). Perform uniaxial compression at 300 K, strain rate 1e8 /s, with interspersed load/unload segments. From the stress-strain data, compute the secant modulus during an unloading segment as the effective Young's modulus (Y_eff^MD) and write the stress-strain curve.
- Evidence: `/app/outputs/md_stress_strain.csv`

### Step 4: Run linear-elastic FEM simulation to obtain effective Young's modulus
- Role: process
- Action: Reconstruct the surface of the relaxed MD initial structure using an alpha-shape algorithm. Smooth the surface, generate a volumetric mesh, and perform a linear-elastic finite element analysis with the same orthotropic elastic constants from the EAM potential. Apply periodic boundary conditions and compute the macroscopic response at 0.02 compressive strain to obtain Y_eff^FEM. Write the result to a text file.
- Evidence: `/app/outputs/fem_y_eff.txt`

### Step 5: Compile and report all effective Young's moduli and solid fraction
- Role: scored (load-bearing)
- Action: Read Y_bulk from bulk_modulus.json, Y_eff^MD from md_stress_strain.csv (extracted secant modulus), Y_eff^FEM from fem_y_eff.txt, and the solid fraction φ from the generation step. Compute the Gibson-Ashby prediction: Y_eff^GA = Y_bulk * φ². Write a single JSON file with keys: md_y_eff_GPa, fem_y_eff_GPa, ga_y_eff_GPa, solid_fraction.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: JSON object with numeric fields: md_y_eff_GPa (float), fem_y_eff_GPa (float), ga_y_eff_GPa (float), solid_fraction (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Compiled effective Young's moduli and solid fraction for the initial nanoporous gold configuration. The checker uses structural_audit to verify relative ordering and threshold ranges without requiring exact reproduction of paper-specific values.
- schema:
  - `type`: object
  - `required`:
    - `md_y_eff_GPa`: number
    - `fem_y_eff_GPa`: number
    - `ga_y_eff_GPa`: number
    - `solid_fraction`: number
  - `units`:
    - `md_y_eff_GPa`: GPa
    - `fem_y_eff_GPa`: GPa
    - `ga_y_eff_GPa`: GPa
    - `solid_fraction`: dimensionless

Notes: Checker verifies relative ordering: md_y_eff_GPa < fem_y_eff_GPa, both are substantially smaller than ga_y_eff_GPa, and solid_fraction falls in a plausible range. The exact numeric thresholds are hidden; the policy ensures the paper's claim is correctly captured.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "md_y_eff_GPa": "number",
          "fem_y_eff_GPa": "number",
          "ga_y_eff_GPa": "number",
          "solid_fraction": "number"
        },
        "units": {
          "md_y_eff_GPa": "GPa",
          "fem_y_eff_GPa": "GPa",
          "ga_y_eff_GPa": "GPa",
          "solid_fraction": "dimensionless"
        }
      },
      "description": "Compiled effective Young's moduli and solid fraction for the initial nanoporous gold configuration. The checker uses structural_audit to verify relative ordering and threshold ranges without requiring exact reproduction of paper-specific values."
    }
  ],
  "notes": "Checker verifies relative ordering: md_y_eff_GPa < fem_y_eff_GPa, both are substantially smaller than ga_y_eff_GPa, and solid_fraction falls in a plausible range. The exact numeric thresholds are hidden; the policy ensures the paper's claim is correctly captured."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/simulation_results.json` and applies a structural audit. It checks that the solid fraction lies within a plausible range for a spinodal NPG network and that the three reported effective Young's moduli obey a required ordering: `md_y_eff_GPa` must be smaller than `fem_y_eff_GPa`, and both must be substantially smaller than `ga_y_eff_GPa`. In addition, the verifier confirms that `ga_y_eff_GPa` falls within physically reasonable bounds. The exact numeric thresholds are not disclosed; the verifier awards full credit when the ordering holds and the solid fraction is sensible, reflecting the physical claim that the atomistic material is softer than the linear-elastic continuum and both are far below the foam scaling prediction. Each stage's evidence artifacts are checked for presence and format; the final reward aggregates these checks into a single score.
