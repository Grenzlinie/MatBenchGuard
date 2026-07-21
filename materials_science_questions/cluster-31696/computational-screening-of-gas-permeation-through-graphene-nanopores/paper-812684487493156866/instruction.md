# Water Permeation through T-C3N Monolayer Nanofiltration Membrane

## Problem background
Freshwater scarcity drives the search for high-performance membrane materials for seawater desalination and nanofiltration. An ideal molecular-sieve membrane should combine high water permeability with strong rejection of hydrated salt ions and organic contaminants. A recently proposed two-dimensional carbonitride monolayer, T‑C₃N, possesses a regular array of sub‑nanometer pores whose size is close to the critical diameter that allows single‑water transport while blocking larger hydrated species. Reproducing the key first‑principles predictions for water interaction with this monolayer — adsorption strength, the intrinsic permeation energy barrier, and the resulting analytical water permeance — is an essential step toward assessing its desalination potential. This task asks you to compute those quantities yourself using density‑functional‑theory (DFT) methods and a simple fluid‑dynamics model, so that the monolayer’s performance can be independently evaluated.

## Approach
The central idea is to treat the monolayer as a periodic DFT slab and to compute the energetic surface it presents to water molecules one by one and in small clusters, then to feed the geometric properties of the pore into a continuum permeance formula. You will build the unit cell of monolayer T‑C₃N from the published bond‑length blueprint, relax it with a van‑der‑Waals‑inclusive functional (PBE‑D3), and determine the fully optimised monolayer structure. Next you will place a single water molecule at the pore centre and relax the combined system to obtain the absolute (exothermic) adsorption energy — a measure of how strongly the pore attracts an isolated water. To gauge the intrinsic transport penalty, you will locate the transition state for a water molecule crossing the pore by scanning the potential‑energy surface, reporting the barrier height relative to the most stable adsorbed configuration. The same relaxation and energy‑difference protocol is then applied to the water dimer and trimer, revealing how water–water hydrogen‑bond networks compete with the pore‑surface interactions. Finally, you will estimate the water permeance from the monolayer’s pore radius, membrane thickness, surface porosity, pore areal density, and the viscosity of water by applying the Hagen‑Poiseuille relation. The more expensive adaptive‑steered‑MD simulations for ions are excluded because the required force‑field parameterisation for T‑C₃N is not sufficiently specified for unambiguous reproduction; therefore the task concentrates on the fully specified DFT and analytical calculations that can be performed with open‑source codes such as Quantum ESPRESSO, CP2K, or GPAW.

## Reproduction target
Compute (1) the relaxed monolayer structure with a clear numeric characterisation of the pore size; (2) the absolute adsorption energy of a single H₂O molecule at the pore centre (in eV); (3) the one‑molecule permeation barrier through the pore (in kcal mol⁻¹); (4) the absolute adsorption energies of (H₂O)₂ and (H₂O)₃ on the pore (in eV, provided as a JSON object); and (5) an analytical water‑permeance estimate (in L m⁻² h⁻¹ bar⁻¹) using the geometric parameters supplied in the workflow steps. All results should be obtained with a van‑der‑Waals‑corrected PBE calculation, and the numerical outputs must be written in the exact file formats and units described in the workflow steps below. Your task is to run the entire pipeline and deliver these artifacts; the correctness of each will be assessed independently against a reference expectation derived from the original study.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, GPAW): https://www.quantum-espresso.org/
- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Geometry optimisation of monolayer T-C3N
- Role: scored (load-bearing)
- Action: Build a periodic unit cell of monolayer T-C3N using the reported bond lengths (C-C intra-tetrahedron ~1.456 Å, inter-tetrahedron ~1.409 Å, C-N ~1.522 Å) and a pore diameter ~5.50 Å. Perform a full DFT geometry relaxation (PBE functional with D3 dispersion correction) with a vacuum layer >15 Å. Output the relaxed atomic coordinates as an XYZ file with cell vectors in the comment line.
- Output file: `/app/outputs/step_01_monolayer_coordinates.xyz`
- Format: txt
- Contract: XYZ format: line1 = number of atoms, line2 = comment (with e.g. 'Lattice="ax ay az bx by bz cx cy cz"'), then element x y z per atom.
- Scoring: scored by hidden verifier

### Step 2: Water adsorption energy
- Role: scored
- Action: Using the relaxed monolayer from step_01, place a single water molecule at the pore centre and perform a DFT geometry relaxation (PBE-D3). Compute the adsorption energy as Eads = |E(T-C3N+H2O) – E(T-C3N) – E(H2O)| (absolute value, exothermic). Write the value in eV.
- Output file: `/app/outputs/step_02_water_adsorption_energy.txt`
- Format: txt
- Contract: Text: a number immediately followed by ' eV' (e.g., '0.617 eV').
- Scoring: scored by hidden verifier

### Step 3: Water permeation barrier
- Role: scored
- Action: Locate the transition state for a single water molecule crossing the pore (e.g., using a distinguished reaction coordinate (DRC) search or the nudged elastic band (NEB) method). Refine the TS and compute the energy barrier as E_TS – E_adsorbed in kcal/mol. Write the barrier.
- Output file: `/app/outputs/step_03_permeation_barrier.txt`
- Format: txt
- Contract: Text: a number immediately followed by ' kcal/mol' (e.g., '26.58 kcal/mol').
- Scoring: scored by hidden verifier

### Step 4: Water cluster adsorption energies
- Role: scored
- Action: Using the relaxed monolayer, optimise the geometries of the water dimer (H2O)2 and trimer (H2O)3 placed at the pore centre (PBE-D3). Compute the absolute adsorption energies for each cluster and write them in a JSON object with keys '(H2O)2' and '(H2O)3'.
- Output file: `/app/outputs/step_04_cluster_adsorption_energies.json`
- Format: json
- Contract: {"(H2O)2": <float>, "(H2O)3": <float>}
- Scoring: scored by hidden verifier

### Step 5: Hagen-Poiseuille water permeance estimation
- Role: scored
- Action: Using the geometric parameters from the monolayer (pore radius r_p = 2.75 Å, surface porosity ε = 0.97, membrane thickness δ = 6.2 Å), pore density 4×10¹⁴ cm⁻², water viscosity μ = 1.002×10⁻³ Pa·s, and tortuosity τ = 1.0, compute the water permeance J/Δp via the Hagen-Poiseuille relation and output the value in L·m⁻²·h⁻¹·bar⁻¹.
- Output file: `/app/outputs/step_05_permeance.txt`
- Format: txt
- Contract: Text: a number immediately followed by ' L·m⁻²·h⁻¹·bar⁻¹' (e.g., '750 L·m⁻²·h⁻¹·bar⁻¹').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_monolayer_coordinates.xyz`
- `/app/outputs/step_02_water_adsorption_energy.txt`
- `/app/outputs/step_03_permeation_barrier.txt`
- `/app/outputs/step_04_cluster_adsorption_energies.json`
- `/app/outputs/step_05_permeance.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_monolayer_coordinates.xyz
- path: `/app/outputs/step_01_monolayer_coordinates.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized atomic coordinates of the monolayer T-C3N unit cell; will be checked for pore size (center-to-center distance of opposite C atoms) against a reference of ~5.50 Å.
- schema:
  - `type`: text
  - `description`: XYZ file with first line = number of atoms, second line = comment containing lattice vectors (e.g., 'Lattice="ax ay az bx by bz cx cy cz"'), followed by element x y z per atom.

### step_02_water_adsorption_energy.txt
- path: `/app/outputs/step_02_water_adsorption_energy.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Absolute adsorption energy of a single H2O on the pore centre, in eV (exothermic).
- schema:
  - `type`: text
  - `pattern`: number + ' eV'

### step_03_permeation_barrier.txt
- path: `/app/outputs/step_03_permeation_barrier.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy barrier for single water permeation through the pore, in kcal/mol.
- schema:
  - `type`: text
  - `pattern`: number + ' kcal/mol'

### step_04_cluster_adsorption_energies.json
- path: `/app/outputs/step_04_cluster_adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies of water dimer and trimer on the monolayer, in eV.
- schema:
  - `type`: object
  - `required`: `(H2O)2`, `(H2O)3`
  - `properties`:
    - `(H2O)2`:
      - `type`: number
      - `unit`: eV
    - `(H2O)3`:
      - `type`: number
      - `unit`: eV

### step_05_permeance.txt
- path: `/app/outputs/step_05_permeance.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Estimated water permeance using the Hagen-Poiseuille relation; meeting or exceeding a high-performance threshold earns full credit.
- schema:
  - `type`: text
  - `pattern`: number + ' L·m⁻²·h⁻¹·bar⁻¹'

Notes: The ASMD/PMF simulations for water and ions are excluded from this task because the force field parameterization for T-C3N is not specified in the paper at a level that permits unambiguous reproduction. The task focuses on the fully specified DFT calculations and the analytical permeance estimation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_monolayer_coordinates.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "XYZ file with first line = number of atoms, second line = comment containing lattice vectors (e.g., 'Lattice=\"ax ay az bx by bz cx cy cz\"'), followed by element x y z per atom."
      },
      "description": "Optimized atomic coordinates of the monolayer T-C3N unit cell; will be checked for pore size (center-to-center distance of opposite C atoms) against a reference of ~5.50 Å."
    },
    {
      "file": "step_02_water_adsorption_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "pattern": "number + ' eV'"
      },
      "description": "Absolute adsorption energy of a single H2O on the pore centre, in eV (exothermic)."
    },
    {
      "file": "step_03_permeation_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "pattern": "number + ' kcal/mol'"
      },
      "description": "Energy barrier for single water permeation through the pore, in kcal/mol."
    },
    {
      "file": "step_04_cluster_adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "(H2O)2",
          "(H2O)3"
        ],
        "properties": {
          "(H2O)2": {
            "type": "number",
            "unit": "eV"
          },
          "(H2O)3": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Adsorption energies of water dimer and trimer on the monolayer, in eV."
    },
    {
      "file": "step_05_permeance.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "pattern": "number + ' L·m⁻²·h⁻¹·bar⁻¹'"
      },
      "description": "Estimated water permeance using the Hagen-Poiseuille relation; meeting or exceeding a high-performance threshold earns full credit."
    }
  ],
  "notes": "The ASMD/PMF simulations for water and ions are excluded from this task because the force field parameterization for T-C3N is not specified in the paper at a level that permits unambiguous reproduction. The task focuses on the fully specified DFT calculations and the analytical permeance estimation."
}
```

## How you are scored
A hidden verifier will inspect the five scored artifacts you produce. Each artifact carries a portion of the total reward: the monolayer geometry is checked for structural fidelity (pore size), the scalar energies are compared to reference values within tolerances appropriate for a re‑run with a different DFT implementation, and the permeance is evaluated on a threshold‑or‑better basis (meeting or exceeding a high‑performance level earns full credit). The individual stage scores are combined by weight into a final [0,1] reward. Merely reporting a number without having executed the required DFT calculations will not succeed because the geometry check forces the core simulation to be performed, and the combined evidence across several independent quantities raises the bar against trivial fabrication. Your goal is to run the complete workflow faithfully and to produce internally consistent outputs that reflect genuine first‑principles modelling of the T‑C₃N monolayer.
