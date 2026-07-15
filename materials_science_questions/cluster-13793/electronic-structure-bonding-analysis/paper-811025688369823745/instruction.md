# DFT Calculation of Impurity Strengthening Energies at a Ni Grain Boundary

## Problem background
Impurity segregation at grain boundaries can embrittle or strengthen metals. Whether a particular impurity acts as an embrittler or cohesion enhancer depends on its relative preference for the grain boundary versus the free surface. This task uses first-principles calculations to determine the strengthening energy ΔE_B = ΔE_b − ΔE_s for hydrogen, boron, and phosphorus at a Σ5(210) nickel grain boundary and nickel (210) free surface. ΔE_b and ΔE_s are the binding energies of the impurity at the grain boundary and free surface, respectively. A positive ΔE_B indicates a cohesion enhancer; a negative value indicates an embrittler.

## Approach
The approach is based on density-functional theory calculations using the full-potential linearized augmented plane-wave (FLAPW) method with the generalized-gradient approximation (GGA-PBE) for exchange and correlation. The workflow consists of:
- constructing periodic slab models for the clean Ni(210) free surface, the clean Ni Σ5(210) grain boundary, and the same systems with H, B, or P impurities placed at specified sites;
- performing spin-polarized total-energy calculations with atomic relaxation until forces are negligible;
- computing the binding energies ΔE_s and ΔE_b via the total energies of the impurity-containing slab, the clean slab, and an impurity monolayer;
- optionally decomposing each binding energy into chemical (direct impurity-host interaction) and mechanical (host relaxation energy) contributions;
- calculating the strengthening energy ΔE_B = ΔE_b − ΔE_s.
This method allows a quantitative classification of each impurity's effect on grain boundary cohesion.

## Reproduction target
Produce the strengthening energies ΔE_B (in eV) for H, B, and P, along with the corresponding binding energies ΔE_s and ΔE_b and their mechanical/chemical contributions (also in eV). Write the binding energies for both FS and GB environments into binding_energies.csv, and the ΔE_B values into strengthening_energies.csv. The target is to faithfully implement the FLAPW-DFT protocol as described and report the computed numeric results.

## Assets

- FLEUR (FLAPW code): http://www.flapw.de

## Workflow steps

### Step 1: Bulk lattice constant of fcc Ni
- Role: process
- Action: Compute the equilibrium lattice constant of bulk fcc Ni using the FLAPW code with the PBE-GGA exchange-correlation functional. The resulting lattice constant will serve as the in-plane lattice constant for all subsequent slab models.
- Evidence: none

### Step 2: Construct slab models
- Role: process
- Action: Build initial atomic structures for the following systems using the computed GGA lattice constant: clean 11-layer Ni(210) free-surface slab, clean 21-layer Ni Σ5(210) grain-boundary slab, impurity-containing slabs (H, B, P placed pseudomorphically on next Ni sites on both sides of the FS slab, and at the hollow site in the GB core), and a free impurity monolayer. Ensure appropriate slab symmetries and constraints as required to model the surface and grain boundary.
- Evidence: none

### Step 3: FLAPW total-energy and force calculations with geometry optimization
- Role: process
- Action: Run spin-polarized FLAPW-DFT calculations for all systems: clean FS, clean GB, X/FS, X/GB, and the impurity monolayer. Use numerical parameters appropriate for FLAPW (e.g., APW cutoff, charge/potential cutoff, muffin-tin radii, k-point mesh, convergence criteria). Relax atomic positions until forces on free atoms are below a specified threshold, with selected layers fixed to simulate bulk-like environment. Record total energies, relaxed atomic coordinates, charge densities, and spin densities for each system.
- Evidence: none

### Step 4: FLAPW calculations on unrelaxed reference systems
- Role: process
- Action: For each impurity and each environment (FS and GB), compute the total energy of the host system with the impurity atom removed while keeping all Ni atoms fixed at the relaxed positions obtained in step 2. These unrelaxed reference systems are needed to decompose the binding energy into mechanical and chemical contributions.
- Evidence: none

### Step 5: Compute binding energies with mechanical/chemical contributions
- Role: scored (load-bearing)
- Action: Using total energies from steps 2 and 3, compute for each impurity the binding energy to the free surface (ΔE_s), the binding energy to the grain boundary (ΔE_b), and their decomposition into mechanical and chemical contributions, following the paper's definitions. Output the results in a CSV file.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: Header: impurity,surface,binding_energy,mechanical,chemical. impurity: H/B/P; surface: FS/GB; binding_energy, mechanical, chemical: float (eV). 6 rows.
- Scoring: scored by hidden verifier

### Step 6: Compute strengthening energies ΔE_B
- Role: scored
- Action: From the binding energies in step 4, compute the strengthening energy ΔE_B = ΔE_b - ΔE_s for each impurity. Report the value and its sign (positive indicating cohesion enhancer, negative embrittler). Output the results in a CSV file.
- Output file: `/app/outputs/strengthening_energies.csv`
- Format: csv
- Contract: Header: impurity,delta_EB. impurity: H/B/P; delta_EB: float (eV). 3 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.csv`
- `/app/outputs/strengthening_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies (ΔE_s and ΔE_b) and their mechanical/chemical contributions for H, B, P on Ni(210) free surface and Ni Σ5(210) grain boundary.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `surface`, `binding_energy`, `mechanical`, `chemical`
  - `units`:
    - `binding_energy`: eV
    - `mechanical`: eV
    - `chemical`: eV

### strengthening_energies.csv
- path: `/app/outputs/strengthening_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Strengthening energy ΔE_B = ΔE_b - ΔE_s for H, B, P. Positive values indicate cohesion enhancer; negative values indicate embrittler.
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `delta_EB`
  - `units`:
    - `delta_EB`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "surface",
          "binding_energy",
          "mechanical",
          "chemical"
        ],
        "units": {
          "binding_energy": "eV",
          "mechanical": "eV",
          "chemical": "eV"
        }
      },
      "description": "Binding energies (ΔE_s and ΔE_b) and their mechanical/chemical contributions for H, B, P on Ni(210) free surface and Ni Σ5(210) grain boundary."
    },
    {
      "file": "strengthening_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "delta_EB"
        ],
        "units": {
          "delta_EB": "eV"
        }
      },
      "description": "Strengthening energy ΔE_B = ΔE_b - ΔE_s for H, B, P. Positive values indicate cohesion enhancer; negative values indicate embrittler."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that compares your computed values in binding_energies.csv and strengthening_energies.csv against reference results expected from the protocol, using appropriate tolerances. The verifier checks that the binding energies and strengthening energies are numerically consistent with the reference, and that the sign of each ΔE_B correctly identifies the impurity as embrittler or cohesion enhancer according to the hidden reference classification. Each scored artifact contributes to a combined reward, with the main weight on the strengthening energies. Reporting the paper's numbers without executing the workflow will not receive credit.
