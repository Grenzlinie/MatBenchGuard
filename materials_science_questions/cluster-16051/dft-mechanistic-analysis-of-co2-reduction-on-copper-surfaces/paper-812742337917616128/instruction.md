# DFT Study of Biaxial Strain Effects on CO2 Reduction Intermediates on Cu(100)

## Problem background
Electrochemical CO₂ reduction on copper electrodes can produce hydrocarbons and oxygenates, but the selectivity toward multi‑carbon (C₂₊) products is often limited by the energetics of key intermediates and the barriers for C–C bond formation.  Surface strain has been proposed as a means to tune the binding of reaction intermediates, yet the systematic influence of biaxial strain on the adsorption energies of CO₂ reduction intermediates and on the kinetics of C–C coupling is not fully resolved.  A detailed atomic‑scale understanding of how strain alters the competition between C₁, C₂, and C₃ pathways is needed to guide catalyst design.

## Approach
The work uses a first‑principles computational approach to map the formation energies of six CO₂ reduction intermediates (*H, *CO₍atop₎, *CO₍bridge₎, *CHO, *COOH, and *OCCOH) across a dense grid of biaxially strained Cu(100) surface models.  By comparing the relative formation energies and analysing the site preferences, the influence of strain on selectivity can be assessed.  In addition, the activation free energies for key C–C coupling steps (CO–CO coupling and the formation of C₃ intermediates) are calculated on selected surfaces under explicit solvation, using the nudged elastic band method together with zero‑point energy and entropy corrections.  The combination of thermodynamic and kinetic data reveals how strain affects both the stability of intermediates and the barriers that control product distribution.

## Reproduction target
You must produce three scored CSV files under `/app/outputs`:

1. **formation_energies.csv** – the formation energies of *H, *CO₍atop₎, *CO₍bridge₎, *CHO, *COOH, and *OCCOH on every biaxially strained Cu(100) surface (121 strain states).

2. **relative_formation_energies.csv** – the relative formation energies with respect to the unstrained (0,0) surface, derived from the formation energies.

3. **activation_energies.csv** – the activation free energy barriers and reaction free energies for (a) CO–CO coupling on the (0,0), (−6,10), and (−10,10) surfaces, and (b) *CCH + *CO and *CCOH + *CO coupling on the (−10,0) and (−10,10) surfaces, all under explicit solvation and including zero‑point energy and entropy corrections.

The hidden verifier will also check that your relative formation energies satisfy a hidden structural consistency condition.  Your data must be consistent with this condition to receive full credit for the structural check.

## Assets

- Quantum ESPRESSO (plane-wave DFT code with PAW and rPBE functional): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE) or similar structure builder: https://wiki.fysik.dtu.dk/ase/
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Tunable-polarizability water force field (published in J. Phys. Chem. A 2018, 122, 4654-4622): 10.1021/acs.jpca.8b01234

## Workflow steps

### Step 1: Generate strained Cu(100) slab models
- Role: process
- Action: Construct 121 Cu(100) slab models (four-layer, 4×3 supercell) by applying biaxial strain along the two in‑plane lattice vectors a and b, sampling a grid of strain values that spans compressive and tensile combinations. Identify the displaced surface morphologies that emerge at high compression.
- Evidence: `/app/outputs/slab_models_manifest.txt`

### Step 2: Compute total energies for bare strained slabs and adsorbed intermediates
- Role: process
- Action: Using plane‑wave DFT (rPBE functional, PAW, spin‑polarized, appropriate energy cutoff and k‑point mesh), relax and compute the total energy of every bare strained slab, and of each surface with the adsorbed intermediates *H (fourfold hollow), *CO at atop and bridge sites, *CHO, *COOH, and *OCCOH (bridge). Also compute the standard‑state reference energies of C (graphene), H₂, and O₂.
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Compile formation energies of all intermediates on all strained surfaces
- Role: scored
- Action: From the computed total energies and reference energies, calculate the formation energy for each adsorbate on each strain state using the definition E_form^X = E^(X·Cu) – (E^Cu + Nc·E_C + NH·E_H + NO·E_O). Write one row per strain–adsorbate combination to formation_energies.csv.
- Output file: `/app/outputs/formation_energies.csv`
- Format: csv
- Contract: strain_a (int), strain_b (int), adsorbate (str), E_form (float, eV)
- Scoring: scored by hidden verifier

### Step 4: Compute relative formation energies
- Role: scored
- Action: Using the formation energies from the previous step, compute for each adsorbate the relative formation energy ΔE_form = E_form(strained) – E_form(0,0). Write to relative_formation_energies.csv.
- Output file: `/app/outputs/relative_formation_energies.csv`
- Format: csv
- Contract: strain_a (int), strain_b (int), adsorbate (str), delta_E_form (float, eV)
- Scoring: scored by hidden verifier

### Step 5: Prepare explicit solvation models for selected surfaces
- Role: process
- Action: For the surfaces (0,0), (-6,10), (-10,10), and (-10,0), construct a solvation layer (water molecules and a sodium ion), equilibrate using classical molecular dynamics (LAMMPS) with the published tunable‑polarizability water force field, followed by short ab initio MD, then optimize the geometry. Compute electrostatic potential and Fermi energy to determine the effective applied cathode potential.
- Evidence: `/app/outputs/solvation_setup_report.txt`

### Step 6: Compute activation free energies for C–C coupling
- Role: scored (load-bearing)
- Action: Using the solvated slab models, perform NEB calculations to locate transition states for: (a) CO–CO coupling on (0,0), (-6,10), (-10,10); (b) *CCH + *CO and *CCOH + *CO coupling on (-10,0) and (-10,10). Apply zero‑point energy and entropy corrections to obtain free‑energy barriers and reaction energies. Write results to activation_energies.csv.
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: surface (str), reaction (str), barrier (float, eV), reaction_energy (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.csv`
- `/app/outputs/relative_formation_energies.csv`
- `/app/outputs/activation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.csv
- path: `/app/outputs/formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of *H, *CO_atop, *CO_bridge, *CHO, *COOH, and *OCCOH on biaxially strained Cu(100) surfaces.
- schema:
  - `type`: table
  - `required_columns`: `strain_a`, `strain_b`, `adsorbate`, `E_form`
  - `units`:
    - `E_form`: eV

### relative_formation_energies.csv
- path: `/app/outputs/relative_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relative formation energies with respect to the unstrained (0,0) surface, recomputed from formation_energies.csv and assessed for a structural trend among intermediates.
- schema:
  - `type`: table
  - `required_columns`: `strain_a`, `strain_b`, `adsorbate`, `delta_E_form`
  - `units`:
    - `delta_E_form`: eV

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation free energies and reaction free energies for C–C coupling reactions under explicit solvation on selected Cu(100) surfaces.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `reaction`, `barrier`, `reaction_energy`
  - `units`:
    - `barrier`: eV
    - `reaction_energy`: eV

Notes: The checker will recompute relative formation energies from formation_energies.csv, verify internal consistency, and assess a specific structural trend (preference for one intermediate over another in a defined strain region). Activation barriers are compared to known reference values within physically motivated tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_a",
          "strain_b",
          "adsorbate",
          "E_form"
        ],
        "units": {
          "E_form": "eV"
        }
      },
      "description": "Formation energies of *H, *CO_atop, *CO_bridge, *CHO, *COOH, and *OCCOH on biaxially strained Cu(100) surfaces."
    },
    {
      "file": "relative_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_a",
          "strain_b",
          "adsorbate",
          "delta_E_form"
        ],
        "units": {
          "delta_E_form": "eV"
        }
      },
      "description": "Relative formation energies with respect to the unstrained (0,0) surface, recomputed from formation_energies.csv and assessed for a structural trend among intermediates."
    },
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "reaction",
          "barrier",
          "reaction_energy"
        ],
        "units": {
          "barrier": "eV",
          "reaction_energy": "eV"
        }
      },
      "description": "Activation free energies and reaction free energies for C–C coupling reactions under explicit solvation on selected Cu(100) surfaces."
    }
  ],
  "notes": "The checker will recompute relative formation energies from formation_energies.csv, verify internal consistency, and assess a specific structural trend (preference for one intermediate over another in a defined strain region). Activation barriers are compared to known reference values within physically motivated tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file after your submission.  For `formation_energies.csv`, the verifier compares your computed formation energies to reference values within physically motivated tolerances.  For `relative_formation_energies.csv`, the verifier recomputes the relative energies from your `formation_energies.csv`, verifies internal consistency, and also checks that a hidden structural consistency condition is satisfied.  For `activation_energies.csv`, the verifier compares your reported barriers and reaction energies to reference values.  Each stage carries a weighted share of the total reward, and your final score is the weighted sum, normalized to a value between 0 and 1.
