# Defect complex formation and diffusion in tungsten surface from first-principles

## Problem background
Tungsten is a leading candidate for plasma-facing materials in fusion reactors. Experiments show that helium (He) pre-exposure increases hydrogen (H) retention near the tungsten surface while simultaneously facilitating desorption and suppressing blistering. Understanding the micro-mechanisms behind these opposite trends requires studying how H and He interact with surface vacancies (V) and He-vacancy (HeV) complexes on the most stable W(110) surface. This reproduction uses first-principles density functional theory (DFT) to investigate the dissolution and desorption behaviour of H in a W(110) surface containing a single V or a HeV complex.

## Approach
The theoretical framework is spin-polarised DFT with the generalised gradient approximation (GGA-PBE) and pseudopotentials to describe core electrons. A slab model of the W(110) surface is built from the relaxed bulk lattice. The slab contains eleven atomic layers with a vacuum gap, where the bottom layers are fixed at the bulk lattice constant and the top layers are allowed to relax. Defects (single vacancies and HeV complexes) are introduced at specific subsurface layers. The energetics are analysed by computing formation energies, solution energies, binding energies, and diffusion/desorption barriers. The climbing-image nudged elastic band (CI-NEB) method is used to locate minimum energy paths and barriers for H and He migration. The key comparisons are: (a) binding of H and He to a vacancy, (b) diffusion barriers of H and He toward a vacancy, (c) H desorption barriers from a bare vacancy and from a HeV complex, and (d) the number of stable H capture sites around each defect type. All quantities are computed with the open-source Quantum ESPRESSO code and standard SSSP pseudopotentials.

## Reproduction target
Compute and report, for a W(110) slab with a vacancy or HeV complex at the second and third surface layers, the following quantities:
1. Formation energies of a single vacancy (V) and a He-vacancy complex (HeV).
2. Binding energies of H and He with V and HeV.
3. Maximum diffusion barriers for He and H to migrate from a distant tetrahedral interstitial site to a vacancy center at the second layer.
4. Desorption barriers of H from V and HeV at the second layer to the surface vacuum.
5. Number of distinct stable H capture sites around V and HeV at the second layer.
All energies must be reported in electronvolts (eV). Numerical results are written to the specified CSV files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for W, H, He: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Bulk tungsten relaxation
- Role: process
- Action: Relax the BCC tungsten primitive cell using DFT to obtain the equilibrium lattice constant and total energy per atom E(W).
- Evidence: `/app/outputs/bulk_relax.log`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: Construct an 11-layer (3x2) W(110) slab with 13 Å vacuum. Relax the top seven layers while keeping the bottom four fixed at the theoretical lattice constant. Obtain the perfect surface total energy E_S.
- Evidence: `/app/outputs/surface_relax.log`

### Step 3: Reference atom/molecule energies
- Role: process
- Action: Compute the total energies of an isolated He atom and an isolated H2 molecule using spin-polarized DFT. These are used in formation and solution energy formulas.
- Evidence: `/app/outputs/ref_energies.json`

### Step 4: H solution in perfect surface
- Role: process
- Action: Compute the solution energies (or total energies) of H at the threefold hollow surface site and at the relevant tetrahedral interstitial sites (TIS1, TIS2, TIS3) in the perfect surface. Record the total energies E_S+H for each site; they are needed for binding energy calculations.
- Evidence: `/app/outputs/perfect_H_energies.csv`

### Step 5: Formation energies of V and HeV
- Role: scored
- Action: Calculate vacancy formation energies E_V^f for a single vacancy at the second and third atomic layers, and He-vacancy complex formation energies E_HeV^f for the same layers using the standard definitions: E_V^f = E_S,V − E_S + E(W) and E_HeV^f = E_S,HeV − E_S + E(W) − E(He), where E_S,V and E_S,HeV are total energies of the surface with a vacancy or HeV complex, E_S is the perfect surface energy, E(W) is the energy of a bulk W atom, and E(He) is the energy of an isolated He atom. Output the values.
- Output file: `/app/outputs/step_01_formation_energies.csv`
- Format: csv
- Contract: layer (int), E_V_f (eV), E_HeV_f (eV)
- Scoring: scored by hidden verifier

### Step 6: Binding energies of H and He with V and HeV
- Role: scored (load-bearing)
- Action: Compute the binding energies of H and He with a single vacancy (V) at layers 2 and 3, and the binding energies of H with a He-vacancy complex (HeV) at layers 2 and 3, using the standard definitions: E_V+H^b = E_S,V + E_S+H − E_S,V+H − E_S and E_HeV+H^b = E_S,HeV + E_S+H − E_S,HeV+H − E_S, where E_S+H is the total energy of H in the perfect surface, E_S,V+H and E_S,HeV+H are total energies of the surface with a vacancy and H or a HeV complex and H, respectively. For each defect type, species, and layer, report the binding energy of the most stable configuration.
- Output file: `/app/outputs/step_02_binding_energies.csv`
- Format: csv
- Contract: defect_type (str, V or HeV), layer (int, 2 or 3), species (str, H or He), binding_energy (eV)
- Scoring: scored by hidden verifier

### Step 7: Diffusion barriers of He and H to a vacancy
- Role: scored
- Action: Using the climbing image nudged elastic band (CI-NEB) method, compute the minimum energy barriers for He and H to diffuse from a distant tetrahedral interstitial site to the vacancy center at the second layer. Report the maximum barrier along each path.
- Output file: `/app/outputs/step_03_diffusion_barriers.csv`
- Format: csv
- Contract: diffusion_path (str, e.g., He_TIS_to_V, H_TIS_to_V), barrier (eV)
- Scoring: scored by hidden verifier

### Step 8: H desorption barriers from V and HeV
- Role: scored
- Action: Compute the desorption barriers of H from a vacancy (V) and from a He-vacancy complex (HeV) located at the second layer to the surface vacuum using CI-NEB.
- Output file: `/app/outputs/step_04_desorption_barriers.csv`
- Format: csv
- Contract: defect (str, V or HeV), layer (int, 2), barrier_H (eV)
- Scoring: scored by hidden verifier

### Step 9: Stable H sites around V and HeV
- Role: scored
- Action: Identify the number of distinct, energetically stable H capture sites around a vacancy (V) and around a He-vacancy complex (HeV) located at the second layer, within the effective trapping region.
- Output file: `/app/outputs/step_05_stable_site_count.csv`
- Format: csv
- Contract: defect (str, V or HeV), layer (int, 2), num_sites (int)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.csv`
- `/app/outputs/step_02_binding_energies.csv`
- `/app/outputs/step_03_diffusion_barriers.csv`
- `/app/outputs/step_04_desorption_barriers.csv`
- `/app/outputs/step_05_stable_site_count.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.csv
- path: `/app/outputs/step_01_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vacancy and He-vacancy complex formation energies at surface layers 2 and 3.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `E_V_f`, `E_HeV_f`
  - `units`:
    - `layer`: int (2 or 3)
    - `E_V_f`: eV
    - `E_HeV_f`: eV

### step_02_binding_energies.csv
- path: `/app/outputs/step_02_binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies of H and He with vacancies and He-vacancy complexes at layers 2 and 3.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `layer`, `species`, `binding_energy`
  - `units`:
    - `defect_type`: str (V or HeV)
    - `layer`: int (2 or 3)
    - `species`: str (H or He)
    - `binding_energy`: eV

### step_03_diffusion_barriers.csv
- path: `/app/outputs/step_03_diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum diffusion barrier for He and H from a distant TIS to a vacancy at the second layer.
- schema:
  - `type`: table
  - `required_columns`: `diffusion_path`, `barrier`
  - `units`:
    - `diffusion_path`: str
    - `barrier`: eV

### step_04_desorption_barriers.csv
- path: `/app/outputs/step_04_desorption_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Desorption barrier of H from V and HeV at the second layer.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `layer`, `barrier_H`
  - `units`:
    - `defect`: str (V or HeV)
    - `layer`: int (2)
    - `barrier_H`: eV

### step_05_stable_site_count.csv
- path: `/app/outputs/step_05_stable_site_count.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Number of stable H capture sites around V and HeV at the second layer.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `layer`, `num_sites`
  - `units`:
    - `defect`: str (V or HeV)
    - `layer`: int (2)
    - `num_sites`: int

Notes: All energies are in eV. The checker will compare reported values to reference numbers with appropriate tolerances; zero-point energy corrections may be omitted.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "E_V_f",
          "E_HeV_f"
        ],
        "units": {
          "layer": "int (2 or 3)",
          "E_V_f": "eV",
          "E_HeV_f": "eV"
        }
      },
      "description": "Vacancy and He-vacancy complex formation energies at surface layers 2 and 3."
    },
    {
      "file": "step_02_binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "layer",
          "species",
          "binding_energy"
        ],
        "units": {
          "defect_type": "str (V or HeV)",
          "layer": "int (2 or 3)",
          "species": "str (H or He)",
          "binding_energy": "eV"
        }
      },
      "description": "Binding energies of H and He with vacancies and He-vacancy complexes at layers 2 and 3."
    },
    {
      "file": "step_03_diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "diffusion_path",
          "barrier"
        ],
        "units": {
          "diffusion_path": "str",
          "barrier": "eV"
        }
      },
      "description": "Maximum diffusion barrier for He and H from a distant TIS to a vacancy at the second layer."
    },
    {
      "file": "step_04_desorption_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "layer",
          "barrier_H"
        ],
        "units": {
          "defect": "str (V or HeV)",
          "layer": "int (2)",
          "barrier_H": "eV"
        }
      },
      "description": "Desorption barrier of H from V and HeV at the second layer."
    },
    {
      "file": "step_05_stable_site_count.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "layer",
          "num_sites"
        ],
        "units": {
          "defect": "str (V or HeV)",
          "layer": "int (2)",
          "num_sites": "int"
        }
      },
      "description": "Number of stable H capture sites around V and HeV at the second layer."
    }
  ],
  "notes": "All energies are in eV. The checker will compare reported values to reference numbers with appropriate tolerances; zero-point energy corrections may be omitted."
}
```

## How you are scored
A hidden verifier reads your submitted CSV artifacts and compares each reported value to a reference (not disclosed). Scoring is based on two criteria: (i) correct relative ordering between conditions (e.g., binding energy trend, barrier ordering), and (ii) numerical accuracy of the reported values within allowed tolerances. Each scored file contributes a defined weight to the final reward. The total reward is a weighted combination; achieving the correct trends and reasonable numerical agreement is required for full credit. Writing values that approximately match the expected answer without executing the required DFT workflow is not sufficient.
