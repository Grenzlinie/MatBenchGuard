# Atomistic Simulation of Hydrogen Embrittlement in α‑Fe

## Problem background
Hydrogen embrittlement significantly reduces the ductility of α-Fe, leading to premature failure of structural components. Despite decades of research, the underlying atomistic mechanism is not fully understood. Two leading hypotheses are hydrogen-enhanced decohesion (HEDE), where hydrogen weakens metal–metal bonds, and hydrogen-enhanced localized plasticity (HELP), where hydrogen alters dislocation behaviour. Recent atomistic simulations point toward a hybrid mechanism in which hydrogen trapped at dislocation cores enhances dislocation mobility and promotes fracture along slip planes. Reproducing the quantitative atomic-scale interactions that support this hybrid picture is the goal of this task.

## Approach
All simulations are conducted at 0 K using the EAM‑W interatomic potential for the α-Fe–H system within the open‑source code LAMMPS. The approach is a series of static calculations (molecular statics and nudged elastic band) that progressively build understanding:

1. Bulk elastic properties of pure α-Fe are obtained from small‑strain energy minimisations.
2. Hydrogen dissolution and migration energetics in a perfect iron crystal are evaluated by comparing total energies of supercells with and without hydrogen at interstitial sites.
3. An edge dislocation with Burgers vector along [111] on the (112) slip plane is constructed, and the trapping energy of a single hydrogen at every distinct tetrahedral and octahedral site near the core is mapped via energy minimisation.
4. Nudged elastic band (NEB) calculations are performed to find the energy barrier for the dislocation to glide by one Burgers vector (1 b) under three hydrogen conditions: no hydrogen, a hydrogen atom initially at the dislocation core, and a hydrogen atom initially located 1 b ahead of the core.
5. For the same dislocation, the shear stress on the slip plane is computed from the virial stress, both without hydrogen and with a low concentration of hydrogen atoms at the core.
6. Finally, slab models are built for the {100}, {110} and {112} surfaces, and the surface energies are computed for each clean surface and after adsorbing a hydrogen atom at a stable site.

By comparing cases with and without hydrogen, you will quantify the effect hydrogen has on dislocation mobility and surface energy, which are the key ingredients of the proposed embrittlement mechanism.

## Reproduction target
Produce six CSV files from your own LAMMPS simulations, all written to `/app/outputs`:

- `elastic_constants.csv`: columns `property` (C11, C12, C44) and `value` (GPa).
- `hydrogen_properties.csv`: columns `property` (heat_of_solution, migration_energy) and `value` (eV).
- `trap_energy.csv`: for each interstitial site near the dislocation core, columns `site_type` (T‑site or O‑site), `x`, `y`, `z` (nm), and `trap_energy` (eV).
- `energy_barriers.csv`: columns `case` (no_H, H_at_core, H_ahead) and `barrier` (J).
- `shear_stress.csv`: columns `x` (nm), `y` (nm), `shear_stress` (GPa); include profiles both with and without hydrogen.
- `surface_energies.csv`: columns `orientation` ({100}, {110}, {112}), `condition` (clean, with_H), and `surface_energy` (J/m²).

All calculations must use the EAM‑W potential and be performed in LAMMPS. Consistency across the outputs — e.g., a meaningful trap energy map around the dislocation and a plausible change in surface energies — is required.

## Assets

- EAM‑W interatomic potential for Fe–H (Wen et al., 2001): https://www.ctcms.nist.gov/potentials/entry/2001--Wen-M-Xu-X-J-Fukuyama-S-Yokogawa-K--Fe-H/
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- OVITO visualization tool: https://www.ovito.org

## Workflow steps

### Step 1: Compute elastic constants of α‑Fe with EAM‑W
- Role: scored
- Action: Using LAMMPS and the EAM‑W potential, perform small‑strain energy minimizations on a perfect α‑Fe crystal to compute the three independent elastic constants C11, C12, C44 (GPa). Write the results to a CSV file.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: Columns: property (string: C11, C12, C44), value (float, GPa).
- Scoring: scored by hidden verifier

### Step 2: Compute heat of solution and migration energy of H in α‑Fe
- Role: scored
- Action: Using LAMMPS and the EAM‑W potential, calculate the heat of solution as the energy difference between a supercell with one H at a tetrahedral site and pure α‑Fe. Calculate the migration energy (eV) as the energy barrier for H to move from a tetrahedral to an adjacent octahedral site (using NEB or static difference as appropriate). Write the two values to a CSV file.
- Output file: `/app/outputs/hydrogen_properties.csv`
- Format: csv
- Contract: Columns: property (string: heat_of_solution, migration_energy), value (float, eV).
- Scoring: scored by hidden verifier

### Step 3: Map hydrogen trap energy around an edge dislocation
- Role: scored (load-bearing)
- Action: Build an atomistic model of a (112)[111] edge dislocation in α‑Fe (≈8054 atoms) with periodic boundary conditions in x and z. Insert a single H atom at every distinct tetrahedral and octahedral site near the core, relax the structure (conjugate gradient), and compute the trap energy as the difference between the total energy with H at that site and the sum of the energy of the dislocation without H plus an isolated H reference. Output a CSV with all site coordinates and trap energies.
- Output file: `/app/outputs/trap_energy.csv`
- Format: csv
- Contract: Columns: site_type (string: T-site or O-site), x (float, nm), y (float, nm), z (float, nm), trap_energy (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Compute energy barriers for dislocation glide (1b) with and without H
- Role: scored
- Action: Using the same dislocation model, perform NEB calculations for an edge dislocation moving by one Burgers vector (1b) under three conditions: (a) no hydrogen, (b) a hydrogen atom initially at the dislocation core, (c) a hydrogen atom initially 1b ahead of the dislocation core. Output the barrier height (J) for each case to a CSV file.
- Output file: `/app/outputs/energy_barriers.csv`
- Format: csv
- Contract: Columns: case (string: no_H, H_at_core, H_ahead), barrier (float, J).
- Scoring: scored by hidden verifier

### Step 5: Calculate shear stress distribution along the slip plane
- Role: scored
- Action: For the relaxed dislocation structure, compute the shear stress component acting on the slip plane as a function of position along the plane near the dislocation core, using the virial stress formulation in LAMMPS. Provide the stress profile both for the case without hydrogen and for a configuration with hydrogen atoms at the core (low concentration). Write the stress profiles to a CSV file.
- Output file: `/app/outputs/shear_stress.csv`
- Format: csv
- Contract: Columns: x (float, nm), y (float, nm), shear_stress (float, GPa).
- Scoring: scored by hidden verifier

### Step 6: Compute surface energies of {100},{110},{112} surfaces with and without H
- Role: scored
- Action: Create slab models for the {100}, {110} and {112} surfaces of α‑Fe. For each orientation, relax the clean slab and compute the surface energy (J/m²). Then place a hydrogen atom on the surface at a stable adsorption site, relax, and compute the surface energy with H. Write the six values to a CSV file.
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: Columns: orientation (string: {100},{110},{112}), condition (string: clean, with_H), surface_energy (float, J/m²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/hydrogen_properties.csv`
- `/app/outputs/trap_energy.csv`
- `/app/outputs/energy_barriers.csv`
- `/app/outputs/shear_stress.csv`
- `/app/outputs/surface_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Elastic constants C11, C12, C44 of α‑Fe computed with the EAM‑W potential.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `units`:
    - `value`: GPa

### hydrogen_properties.csv
- path: `/app/outputs/hydrogen_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Heat of solution and migration energy of hydrogen in α‑Fe from EAM‑W.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`
  - `units`:
    - `value`: eV

### trap_energy.csv
- path: `/app/outputs/trap_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Hydrogen trap energy at tetrahedral and octahedral sites around an edge dislocation core. The distribution must show strongest trapping at the core, a high‑trap region along the slip plane, and energies approaching zero far from the dislocation.
- schema:
  - `type`: table
  - `required_columns`: `site_type`, `x`, `y`, `z`, `trap_energy`
  - `units`:
    - `x`: nm
    - `y`: nm
    - `z`: nm
    - `trap_energy`: eV

### energy_barriers.csv
- path: `/app/outputs/energy_barriers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: NEB energy barriers for an edge dislocation moving 1b under three hydrogen configurations.
- schema:
  - `type`: table
  - `required_columns`: `case`, `barrier`
  - `units`:
    - `barrier`: J

### shear_stress.csv
- path: `/app/outputs/shear_stress.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Shear stress profile along the slip plane near the edge dislocation core, with and without hydrogen. The profiles under the two conditions should be essentially identical (no significant hydrogen‑induced shielding).
- schema:
  - `type`: table
  - `required_columns`: `x`, `y`, `shear_stress`
  - `units`:
    - `x`: nm
    - `y`: nm
    - `shear_stress`: GPa

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Surface energies of {100}, {110} and {112} α‑Fe surfaces, clean and with adsorbed hydrogen. Hydrogen must reduce the surface energy, with the reduction being most pronounced for the {112} surface.
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `condition`, `surface_energy`
  - `units`:
    - `surface_energy`: J/m²

Notes: All outputs are produced by re-running atomistic simulations with LAMMPS and the EAM‑W potential. The checker compares values to the paper‑reported results within appropriate tolerances for deterministic quantities, and applies structural audits for distributions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "units": {
          "value": "GPa"
        }
      },
      "description": "Elastic constants C11, C12, C44 of α‑Fe computed with the EAM‑W potential."
    },
    {
      "file": "hydrogen_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value"
        ],
        "units": {
          "value": "eV"
        }
      },
      "description": "Heat of solution and migration energy of hydrogen in α‑Fe from EAM‑W."
    },
    {
      "file": "trap_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "site_type",
          "x",
          "y",
          "z",
          "trap_energy"
        ],
        "units": {
          "x": "nm",
          "y": "nm",
          "z": "nm",
          "trap_energy": "eV"
        }
      },
      "description": "Hydrogen trap energy at tetrahedral and octahedral sites around an edge dislocation core. The distribution must show strongest trapping at the core, a high‑trap region along the slip plane, and energies approaching zero far from the dislocation."
    },
    {
      "file": "energy_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "barrier"
        ],
        "units": {
          "barrier": "J"
        }
      },
      "description": "NEB energy barriers for an edge dislocation moving 1b under three hydrogen configurations."
    },
    {
      "file": "shear_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "y",
          "shear_stress"
        ],
        "units": {
          "x": "nm",
          "y": "nm",
          "shear_stress": "GPa"
        }
      },
      "description": "Shear stress profile along the slip plane near the edge dislocation core, with and without hydrogen. The profiles under the two conditions should be essentially identical (no significant hydrogen‑induced shielding)."
    },
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "condition",
          "surface_energy"
        ],
        "units": {
          "surface_energy": "J/m²"
        }
      },
      "description": "Surface energies of {100}, {110} and {112} α‑Fe surfaces, clean and with adsorbed hydrogen. Hydrogen must reduce the surface energy, with the reduction being most pronounced for the {112} surface."
    }
  ],
  "notes": "All outputs are produced by re-running atomistic simulations with LAMMPS and the EAM‑W potential. The checker compares values to the paper‑reported results within appropriate tolerances for deterministic quantities, and applies structural audits for distributions."
}
```

## How you are scored
A hidden verifier will score each output artifact independently. For deterministic scalar quantities (elastic constants, hydrogen heat of solution and migration energy, energy barriers), the verifier compares your computed values against reference results with appropriate numerical tolerances. For the spatial distributions (trap energy map, shear stress profiles) and the surface energy trends, it performs structural audits: it checks that the trap energy is strongest near the dislocation core and along the slip plane, that the shear stress profiles with and without hydrogen are essentially identical, and that hydrogen adsorption reduces the surface energy, with the reduction being most pronounced for the {112} surface. Each scored stage carries a weight; your final reward is the weighted sum of the stage scores. Simply reporting numbers, even if they agree with the reference, is not sufficient — your numerical outputs must be the consistent product of a single simulation workflow that genuinely reproduces the physics of the Fe–H system.
