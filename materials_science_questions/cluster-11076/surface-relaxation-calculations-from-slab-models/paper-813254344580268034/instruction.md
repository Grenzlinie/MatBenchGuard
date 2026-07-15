# First-principles surface and interface energy calculations for metal/carbide interfaces

## Problem background
Magnesium alloys are attractive lightweight structural materials, but their mechanical properties often require grain refinement. Carbon inoculation, where Al4C3 particles form in the melt, is thought to provide potent heterogeneous nucleation sites for primary α‑Mg grains. The nucleation efficiency depends on the atomic structure, bonding, and interfacial energetics of the Mg(0002)/Al4C3(0001) interface. By computing the surface energies of Al4C3(0001) slabs, the work of adhesion, and the interfacial energies as functions of the Al chemical potential, one can thermodynamically assess whether Al4C3 is an effective substrate for α‑Mg and determine the most stable interface structure.

## Approach
You will perform first‑principles density‑functional theory (DFT) calculations using the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) form. Slab models of Mg(0002) and Al4C3(0001) (both C‑ and Al‑terminated) are built with bulk‑like interiors and a vacuum gap. After relaxing the slabs, the surface energy of each Al4C3 termination is derived from the slab total energies and the chemical potentials of Al and C, with the allowed range of the Al chemical potential fixed by the formation enthalpy of bulk Al4C3. Coherent Mg(0002)/Al4C3(0001) interface supercells are then constructed for four combinations: C‑terminated with OT and HCP stacking, and Al‑terminated with OT and HCP stacking. The Mg slab is strained to match the Al4C3 in‑plane lattice constant. Following DFT relaxations, the ideal work of adhesion is obtained from the energy difference between the interface and the isolated relaxed slabs, divided by twice the interface area. The interfacial energy is computed by extending the thermodynamic formulation to include the Mg chemical potential, again as a function of the Al chemical potential. All energies are expressed in J/m².

## Reproduction target
Your task is to compute and report the following:
1. Surface energies of the C‑terminated and Al‑terminated Al4C3(0001) slabs as a function of the relative Al chemical potential μ_Al – μ_Al_bulk, spanning the entire allowed range derived from the formation enthalpy of Al4C3. Output in surface_energies.csv.
2. Ideal work of adhesion for the four interface models: C-OT, C-HCP, Al-OT, Al-HCP. Output in work_of_adhesion.csv.
3. Interfacial energies for each of the four interface models as a function of μ_Al – μ_Al_bulk. Output in interfacial_energies.csv.
All energy values must be in J/m².

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE, efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Construct symmetric slab models for Mg(0002) (5 atomic layers), Al-terminated Al4C3(0001) (10 atomic layers), and C-terminated Al4C3(0001) (11 atomic layers) using the provided lattice constants. Generate input files for DFT relaxations.
- Evidence: `/app/outputs/slab_input_files.tar.gz`

### Step 2: Slab relaxations
- Role: process
- Action: Perform DFT relaxations for the three slab models (Mg(0002), Al-terminated Al4C3(0001), C-terminated Al4C3(0001)) using the specified functional and settings (plane-wave cutoff 340 eV, k-point mesh 9×9×1, etc.) until forces are converged. Save total energies and optimized geometries.
- Evidence: `/app/outputs/slab_energies.json`

### Step 3: Surface energy calculation
- Role: scored (load-bearing)
- Action: Using the total energies of the relaxed Al4C3(0001) slabs and bulk chemical potentials, compute the surface energies of C-terminated and Al-terminated slabs as a function of Al chemical potential (mu_Al - mu_Al_bulk). Output values in J/m².
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: Columns: mu_Al_mu_Al_bulk (eV), surface_energy_C (J/m^2), surface_energy_Al (J/m^2). Rows cover the allowed chemical potential range.
- Scoring: scored by hidden verifier

### Step 4: Interface model construction
- Role: process
- Action: Construct four Mg(0002)/Al4C3(0001) coherent interface supercells using the relaxed slabs: C-terminated with OT stacking, C-terminated with HCP stacking, Al-terminated with OT stacking, Al-terminated with HCP stacking. Apply appropriate tensile strain on the Mg slab to match the Al4C3 lattice. Set up DFT input files for interface relaxations.
- Evidence: `/app/outputs/interface_input_files.tar.gz`

### Step 5: Interface relaxations
- Role: process
- Action: Run DFT relaxations for the four interface supercells using similar DFT parameters as the slab relaxations but with a k-point mesh appropriate for the supercell (e.g., 4×4×1). Save total energies and optimized geometries.
- Evidence: `/app/outputs/interface_energies.json`

### Step 6: Work of adhesion calculation
- Role: scored
- Action: Using the total energies of the relaxed isolated slabs and the relaxed interface supercells, compute the ideal work of adhesion W_ad for each interface model according to the standard formula (energy difference divided by 2×interface area). Output values in J/m².
- Output file: `/app/outputs/work_of_adhesion.csv`
- Format: csv
- Contract: Columns: termination (C or Al), stacking (OT or HCP), W_ad (J/m^2). Exactly 4 rows.
- Scoring: scored by hidden verifier

### Step 7: Interfacial energy calculation
- Role: scored
- Action: Using the interface total energies, slab energies, and bulk chemical potentials, compute the interfacial energy γ for each interface model as a function of the Al chemical potential. Output values in J/m².
- Output file: `/app/outputs/interfacial_energies.csv`
- Format: csv
- Contract: Columns: termination (C or Al), stacking (OT or HCP), mu_Al_mu_Al_bulk (eV), gamma (J/m^2). Rows covering the same chemical potential range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energies.csv`
- `/app/outputs/work_of_adhesion.csv`
- `/app/outputs/interfacial_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface energies of Al4C3(0001) C- and Al-terminated slabs as a function of Al chemical potential relative to bulk.
- schema:
  - `type`: table
  - `required_columns`: `mu_Al_mu_Al_bulk`, `surface_energy_C`, `surface_energy_Al`

### work_of_adhesion.csv
- path: `/app/outputs/work_of_adhesion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ideal work of adhesion for the four Mg(0002)/Al4C3(0001) interface models.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `stacking`, `W_ad`

### interfacial_energies.csv
- path: `/app/outputs/interfacial_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Interfacial energies of the four interface models as a function of Al chemical potential.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `stacking`, `mu_Al_mu_Al_bulk`, `gamma`

Notes: All energies are in J/m². The chemical potential range and conversion factors are provided in the instructions. The agent must re-run all DFT calculations and use the derived total energies to compute these outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mu_Al_mu_Al_bulk",
          "surface_energy_C",
          "surface_energy_Al"
        ]
      },
      "description": "Surface energies of Al4C3(0001) C- and Al-terminated slabs as a function of Al chemical potential relative to bulk."
    },
    {
      "file": "work_of_adhesion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "stacking",
          "W_ad"
        ]
      },
      "description": "Ideal work of adhesion for the four Mg(0002)/Al4C3(0001) interface models."
    },
    {
      "file": "interfacial_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "stacking",
          "mu_Al_mu_Al_bulk",
          "gamma"
        ]
      },
      "description": "Interfacial energies of the four interface models as a function of Al chemical potential."
    }
  ],
  "notes": "All energies are in J/m². The chemical potential range and conversion factors are provided in the instructions. The agent must re-run all DFT calculations and use the derived total energies to compute these outputs."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each of the three scored artifacts (surface_energies.csv, work_of_adhesion.csv, interfacial_energies.csv). The verifier compares your computed values to reference values obtained from the original study. Each artifact carries a weight; the verifier assigns a score for each based on agreement within a tolerance and, where applicable, on the correct qualitative trends (e.g., ordering of adhesion energies across models). The composite final reward is the weighted sum of these component scores. Simply reporting the reference numbers without actually performing the DFT workflow will not produce a valid submission that passes the consistency checks.
