# Reproduce SrTiO3 (001) surface energies, relaxations, and charge transfers using a tight-binding variable-charge model

## Problem background
SrTiO₃ is a prototypical perovskite oxide that serves as a model system for surface science studies of metal oxides and as a technologically important substrate for thin-film growth and oxide electronics. The (001) surface can terminate in either SrO or TiO₂ planes, and the surface termination strongly influences surface structure, energetics, and charge distribution. Accurately predicting the equilibrium bulk lattice constant, the surface formation energies, as well as the atomic relaxations and charge transfers at the two terminations at low temperature, is a critical test for interatomic potential models. This task reproduces the 0 K structural, energetic, and charge properties of SrTiO₃(001) surfaces using a variable-charge tight-binding model known as SMTB-Q, which captures both ionic and covalent bonding within a self-consistent charge-equilibration framework.

## Approach
The SMTB-Q model represents the total energy of an oxide as a sum of four contributions: an atomic ionization energy expanded to second order in the charges, a shielded Coulomb interaction between variable atomic charges, a covalent tight-binding energy that depends on the local environment and on the charges themselves, and a short-range repulsive pair term. The model parameters are determined by separate fits to the binary oxides SrO and TiO₂, and then transferred to the ternary SrTiO₃ using coordination-based scaling rules (the set of final parameters for SrTiO₃ is provided). The equilibrium charges are obtained by minimizing the total energy with respect to all atomic charges, solving the resulting non-linear equations. The model is implemented for periodic boundary conditions.

To reproduce the surface properties, one first computes the equilibrium lattice constant of bulk cubic SrTiO₃ by minimizing the total energy with respect to the lattice parameter. Using this constant, periodic slab models of the (001) surface are constructed with SrO and TiO₂ terminations; each slab has a vacuum gap and contains a sufficient number of atomic layers to converge surface properties. The slab is then relaxed via Metropolis Monte Carlo moves at a low temperature of 2 K (≳400 Monte Carlo steps per atom) to reach the equilibrium atomic configuration and charge distribution for each termination. From the relaxed slab total energies and the bulk cohesive energy per SrTiO₃ unit, the surface formation energies are calculated. Atomic displacements along the surface normal are obtained by comparing the relaxed positions of selected surface and subsurface atoms to their ideal bulk-terminated locations. Charge transfers are computed as the difference between the relaxed atomic charges and the corresponding bulk reference charges. The final outputs are compared, by a hidden verifier, against the expected reference values derived from the same model physics; no external dataset is required—the entire reproduction relies solely on the provided model specification and parameters.

## Reproduction target
Your objective is to produce four artifacts from the implemented SMTB-Q model and the slab simulations:
1. The equilibrium cubic lattice constant a of bulk SrTiO₃ (in Å).
2. The surface formation energies for both the SrO-terminated and TiO₂-terminated SrTiO₃(001) surfaces (in J/m²).
3. The displacements along [001] (in Å, positive outward) for the following labeled atoms: for the SrO termination, atoms Sr(9), O(10), Ti(5), O(7), Sr(6); for the TiO₂ termination, atoms Ti(1), O(3), Sr(2), O(4). (See the atom labeling diagram provided in the model description.)
4. The charge transfers (difference from the bulk charge, in elementary charge e) for the same set of atoms.
All results are to be obtained at 0 K using the given SMTB-Q parameters and Monte Carlo relaxation.

## Assets

- SMTB-Q model equations and parameters (for SrO, TiO2, SrTiO3 fitted values and transfer rules)

## Workflow steps

### Step 1: Implement SMTB-Q model and simulation framework
- Role: process
- Action: Implement the SMTB-Q total energy and charge equilibration (Eqs. 1–5 and Appendix equations) capable of periodic bulk and slab calculations, using the provided parameter set. The implementation must support Monte Carlo atomic relaxation.
- Evidence: none

### Step 2: Bulk SrTiO3 equilibrium lattice constant
- Role: scored
- Action: Using the implemented model with the fitted SrTiO3 parameters, perform energy minimization (e.g., scaling/cubic optimization) to find the equilibrium lattice constant a_0 of cubic SrTiO3 at 0 K.
- Output file: `/app/outputs/bulk_lattice_constant.txt`
- Format: txt
- Contract: Single float, units: Å
- Scoring: scored by hidden verifier

### Step 3: Slab relaxation for SrO- and TiO2-terminated SrTiO3(001) surfaces
- Role: process
- Action: Build periodic slab models of SrTiO3(001) with SrO and TiO2 terminations (supercell ~23 Å × 23 Å × Z_L, slab thickness ≥ 23 Å, using the bulk lattice constant from step_02). Run Monte Carlo relaxation at 2 K until equilibrium (≥400 steps/atom) with the SMTB-Q model. Save the final total energy, relaxed atomic coordinates, and atomic charges for each termination to a structured file (relaxation_results.json).
- Evidence: `/app/outputs/relaxation_results.json`

### Step 4: Surface formation energies
- Role: scored (load-bearing)
- Action: From the final slab total energies in relaxation_results.json and the bulk cohesive energy per SrTiO3 unit computed from the model, calculate the surface energy E_surf = (E_slab – N * E_bulk) / (2 * A_surface) for each termination.
- Output file: `/app/outputs/surface_energies.json`
- Format: json
- Contract: JSON object with keys "SrO_terminated" and "TiO2_terminated", each a float (units: J/m²).
- Scoring: scored by hidden verifier

### Step 5: Atomic displacements at the surfaces
- Role: scored
- Action: Using the relaxed atomic coordinates from relaxation_results.json, compute the displacement along the [001] direction relative to the ideal bulk-terminated positions for the following labelled atoms: SrO termination – Sr(9), O(10), Ti(5), O(7), Sr(6); TiO2 termination – Ti(1), O(3), Sr(2), O(4). Positive values indicate outward displacement (toward vacuum).
- Output file: `/app/outputs/atomic_displacements.csv`
- Format: csv
- Contract: CSV with columns: termination (string), atom_label (string), displacement_A (float, Å).
- Scoring: scored by hidden verifier

### Step 6: Charge transfers at the surfaces
- Role: scored
- Action: Using the relaxed charges from relaxation_results.json, compute the charge transfer (difference from bulk reference charge) for the same set of labelled atoms.
- Output file: `/app/outputs/charge_transfers.csv`
- Format: csv
- Contract: CSV with columns: termination (string), atom_label (string), charge_transfer (float, elementary charge e).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_lattice_constant.txt`
- `/app/outputs/surface_energies.json`
- `/app/outputs/atomic_displacements.csv`
- `/app/outputs/charge_transfers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_lattice_constant.txt
- path: `/app/outputs/bulk_lattice_constant.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice constant of SrTiO3 from the SMTB-Q model.
- schema:
  - `type`: text
  - `description`: single float value; equilibrium lattice constant a of cubic SrTiO3 in Å

### surface_energies.json
- path: `/app/outputs/surface_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Surface energies of the two SrTiO3(001) terminations.
- schema:
  - `type`: object
  - `required`:
    - `SrO_terminated`: float
    - `TiO2_terminated`: float
  - `units`: J/m²

### atomic_displacements.csv
- path: `/app/outputs/atomic_displacements.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Per-atom surface displacements along [001] for the labelled surface atoms.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `atom_label`, `displacement_A`

### charge_transfers.csv
- path: `/app/outputs/charge_transfers.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Charge transfers for the same surface atoms, relative to bulk reference charges.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `atom_label`, `charge_transfer`

Notes: All scored artifacts are compared to paper-reported reference values with hidden tolerances. The agent must implement the full SMTB-Q model; pre-made parameter sets are provided in the instruction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_lattice_constant.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "single float value; equilibrium lattice constant a of cubic SrTiO3 in Å"
      },
      "description": "Optimized lattice constant of SrTiO3 from the SMTB-Q model."
    },
    {
      "file": "surface_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "SrO_terminated": "float",
          "TiO2_terminated": "float"
        },
        "units": "J/m²"
      },
      "description": "Surface energies of the two SrTiO3(001) terminations."
    },
    {
      "file": "atomic_displacements.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "atom_label",
          "displacement_A"
        ]
      },
      "description": "Per-atom surface displacements along [001] for the labelled surface atoms."
    },
    {
      "file": "charge_transfers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "atom_label",
          "charge_transfer"
        ]
      },
      "description": "Charge transfers for the same surface atoms, relative to bulk reference charges."
    }
  ],
  "notes": "All scored artifacts are compared to paper-reported reference values with hidden tolerances. The agent must implement the full SMTB-Q model; pre-made parameter sets are provided in the instruction."
}
```

## How you are scored
The verifier independently reads each output file, extracts the reported numeric values, and compares them against the hidden reference values that correspond to the correct solution of the SMTB-Q model. Each artifact is scored against a pre-set tolerance; meeting or exceeding the tolerance yields full credit for that artifact. The per-artifact scores are combined with a weighting that emphasizes the primary quantities (lattice constant, surface energies) and the remaining atomic-level details. You do not need to match exact digits beyond the physical spread expected from a correct implementation; however, completing the full workflow and obtaining values within the allowable windows is required to achieve a high total reward.
