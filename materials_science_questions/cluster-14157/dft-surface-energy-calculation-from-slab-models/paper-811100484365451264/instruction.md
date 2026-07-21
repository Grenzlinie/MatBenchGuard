# DFT Surface Energy Calculation of B4C Slab Models

## Problem background
Boron carbide (B4C) is a hard, light-weight ceramic used in armor, wear-resistant parts, and nuclear applications. When B4C powders are treated in a high-energy planetary ball mill, the grains develop specific crystallographic defects—cracks, twins, and stacking faults—along certain low- and high-index planes. Because the energy required to form a free surface correlates with the tendency of a plane to fracture or twin, the surface energies of candidate crystallographic planes provide a key quantity for understanding why defects appear preferentially on those planes. Your task is to compute the surface energy for several B4C orientations from first principles and thereby determine which planes are energetically most favorable.

## Approach
You will use density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional to calculate total energies of B4C in the bulk phase and for stoichiometric slab models of six different crystallographic orientations. From the bulk unit cell energy you determine a reference energy per atom. For each orientation you construct a slab with enough thickness and vacuum to avoid interactions between periodic images, relax the atomic positions, and record the slab total energy, number of atoms, and surface area. The specific surface energy is then obtained from the standard relation:

  E_surf = [E_slab(n) - n * E_bulk] / (2 A)

where E_slab(n) is the total energy of a slab containing n atoms, E_bulk is the energy per atom in the bulk, and A is the surface area of one face of the slab. This approach directly connects the raw DFT outputs to a verifiable surface energy that can be compared across planes.

The DFT calculations must use the following computational parameters (as reported in the study whose results you are reproducing):
- Plane-wave energy cutoff: 400 eV
- k-point grid for the bulk phase: 4×4×2 Monkhorst–Pack
- k-point grid for slab models: 4×2×1 Monkhorst–Pack
- Vacuum gap in slab supercells: at least 10 Å
- Slab thickness (excluding vacuum): at least 10 Å
- Force convergence criterion: maximum force component < 0.05 eV/Å

## Reproduction target
For the six B4C slab orientations listed in the workflow steps — (10-11), (20-23), (01-12), (20-21), (01-10), (0001) — compute the specific surface energy in eV/Å² using the protocol above. Report the surface energies together with the intermediate bulk energy and slab raw energies and areas. The core objective is to produce accurate surface energies and to establish their relative ordering: which plane has the lowest energy, which are nearly degenerate, and which are highest.

## Assets

- B4C crystal structure (hexagonal, a=0.56 nm, c=1.207 nm): ICSD collection code 24373
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE pseudopotentials for B and C: SSSP library or standard Quantum ESPRESSO pseudopotential library

## Workflow steps

### Step 1: Bulk B4C reference energy calculation
- Role: process
- Action: Build the B4C hexagonal unit cell from the known crystal structure. Run a DFT total-energy calculation for the bulk phase with the PBE functional, using a plane-wave energy cutoff of 400 eV and a 4×4×2 Monkhorst–Pack k-point grid. Relax atomic positions until all force components are below 0.05 eV/Å. Extract the bulk energy per atom E_bulk and write it to bulk_energy.txt.
- Evidence: `/app/outputs/bulk_energy.txt`

### Step 2: Slab model construction and DFT energies
- Role: process
- Action: For each of the six crystallographic orientations: (10-11), (20-23), (01-12), (20-21), (01-10), (0001), build a stoichiometric slab model with a vacuum gap of at least 10 Å and a slab thickness (excluding vacuum) of at least 10 Å. Perform DFT total-energy calculations on each slab using the PBE functional with a plane-wave energy cutoff of 400 eV and a 4×2×1 k-point grid. Relax atomic positions until all force components are below 0.05 eV/Å. Record slab total energies, numbers of atoms, and surface areas in slab_energies.csv.
- Evidence: `/app/outputs/slab_energies.csv`

### Step 3: Compute surface energies and report
- Role: scored (load-bearing)
- Action: Using the slab energies from slab_energies.csv and the bulk energy from bulk_energy.txt, compute the specific surface energy for each orientation via the standard surface energy formula: E_surf = [E_slab(n) - n*E_bulk] / (2A). Write the results to surface_energies.csv.
- Output file: `/app/outputs/surface_energies.csv`
- Format: csv
- Contract: Columns: orientation, surface_energy (float, eV/Å²)
- Scoring: scored by hidden verifier

## Output files
Write the following artifacts under `/app/outputs`:

**Scored file:**
- `/app/outputs/surface_energies.csv` – final surface energies for the six orientations

**Intermediate files required by the checker:**
- `/app/outputs/bulk_energy.txt` – bulk energy per atom (plain text, one float)
- `/app/outputs/slab_energies.csv` – table with columns: orientation, E_slab (eV), n_atoms (integer), area (Å²)

All intermediate files must be present for the checker to evaluate your submission.

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies.csv
- path: `/app/outputs/surface_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Specific surface energies for six B4C slab orientations. The checker recomputes surface energies from the agent's intermediate bulk and slab energies and compares to this file.
- schema:
  - `type`: table
  - `required_columns`: `orientation`, `surface_energy`
  - `units`:
    - `surface_energy`: eV/Å²

Notes: The checker also reads the intermediate process files bulk_energy.txt and slab_energies.csv to recompute surface energies, but those are not part of the scored contract.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "orientation",
          "surface_energy"
        ],
        "units": {
          "surface_energy": "eV/Å²"
        }
      },
      "description": "Specific surface energies for six B4C slab orientations. The checker recomputes surface energies from the agent's intermediate bulk and slab energies and compares to this file."
    }
  ],
  "notes": "The checker also reads the intermediate process files bulk_energy.txt and slab_energies.csv to recompute surface energies, but those are not part of the scored contract."
}
```

## How you are scored
A hidden verifier will read your intermediate files `bulk_energy.txt` and `slab_energies.csv`, recompute the surface energy for each orientation using E_surf = (E_slab – n·E_bulk) / (2A), and compare the recomputed values against reference values from the published DFT study (the “gold” standard). It will also verify that the relative ordering of the recomputed surface energies agrees with the ordering found in the paper. Scoring is based on these comparisons; the verifier evaluates how closely your recomputed surface energies match the gold values and whether the ordering is correct. An appropriate numerical tolerance is applied for comparisons.