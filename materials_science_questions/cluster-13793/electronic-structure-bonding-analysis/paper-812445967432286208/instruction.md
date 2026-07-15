# Cell-CPA for Random Adsorbate-Substrate System

## Problem background
Understanding the electronic structure of disordered adsorbate layers on crystalline surfaces and its coverage dependence is a central problem in surface science. For adsorbate-substrate systems such as alkali metals on silicon, the interplay of hybridization, lateral interactions, and electrostatic depolarization shifts governs properties like work function and charge transfer. The cell-CPA (coherent potential approximation) formalism, built on an LCAO tight-binding basis, provides a self-consistent framework to treat random adsorbate configurations and extract coverage-dependent electronic quantities. Reproducing these calculations for an exemplar system (alkali metal on the Si(001)2×1 reconstruction) allows one to test the predictive power of the theory and to produce quantitative trends for the work function change, charge transfer, and local density of states at the Fermi level.

## Approach
Implement the cell-CPA theory for a random adsorbate–substrate system within a tight-binding LCAO model. The theory treats the adsorbate layer as a random alloy and solves for the configuration-averaged Green’s function self-consistently; it includes substrate-adsorbate hybridization, lateral adsorbate–adsorbate interactions, and electrostatic depolarization shifts of the adsorbate level. The surface geometry is that of the Si(001)2×1 dimer reconstruction, and the onsite energies and hopping parameters for Si and the alkali-metal adsorbate (Cs) are taken from published references. The self-consistent loop yields the local density of states (LDOS), from which the adsorbate charge transfer, the work function change (computed from the surface dipole layer), and the LDOS at the Fermi energy are extracted. The calculation is repeated for a series of coverages to obtain the coverage-dependent trends.

## Reproduction target
Compute the coverage dependence of three quantities for Cs adsorbed on Si(001)2×1 using the cell-CPA method: (1) change in work function (eV), (2) charge transfer (e) from the substrate to the adsorbate, and (3) local density of states at the Fermi level (arbitrary units). Perform the calculations for six coverages: 0.0, 0.2, 0.4, 0.6, 0.8, and 1.0 monolayer (ML). Output the results in a single JSON file (/app/outputs/calculated_results.json) with keys 'coverages', 'work_function_changes', 'charge_transfers', and 'ldos_at_fermi', each containing a list of six values in the same coverage order.

## Assets

- LCAO tight-binding parameters and Si(001)2×1 surface geometry
- Python scientific libraries (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Acquire model parameters and geometry
- Role: process
- Action: Collect LCAO tight-binding parameters for Si substrate and alkali-metal adsorbate atoms, and the geometry of the Si(001)2×1 surface reconstruction, from published literature (references within the paper). Document the chosen parameters in a file.
- Evidence: `/app/outputs/parameters_used.json`

### Step 2: Cell-CPA simulation and analysis
- Role: scored (load-bearing)
- Action: Implement the cell-CPA formalism for a random adsorbate–substrate system within an LCAO basis. Perform self-consistent calculations for coverage values 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ML. From the resulting local density of states, compute the work function change (eV), charge transfer (e), and LDOS at the Fermi level (arbitrary units) for each coverage. Write all results into the output file.
- Output file: `/app/outputs/calculated_results.json`
- Format: json
- Contract: JSON object with exactly the following keys: 'coverages' (list of 6 floats), 'work_function_changes' (list of 6 floats, unit eV), 'charge_transfers' (list of 6 floats, unit e), 'ldos_at_fermi' (list of 6 floats, arbitrary units). Each list length is 6, corresponding to coverages 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ML in that order.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_results.json
- path: `/app/outputs/calculated_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Coverage-dependent work function change, charge transfer, and LDOS at the Fermi level for Cs/Si(001)2×1 at six coverages.
- schema:
  - `type`: object
  - `required`:
    - `coverages`: list of 6 floats
    - `work_function_changes`: list of 6 floats (eV)
    - `charge_transfers`: list of 6 floats (e)
    - `ldos_at_fermi`: list of 6 floats (arbitrary units)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "coverages": "list of 6 floats",
          "work_function_changes": "list of 6 floats (eV)",
          "charge_transfers": "list of 6 floats (e)",
          "ldos_at_fermi": "list of 6 floats (arbitrary units)"
        }
      },
      "description": "Coverage-dependent work function change, charge transfer, and LDOS at the Fermi level for Cs/Si(001)2×1 at six coverages."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier grades your submission by examining the artifacts you produce in each workflow step. For the scored simulation step, the verifier compares your reported quantities to a reference, applying tolerances that reflect legitimate numerical and implementation differences. It also checks whether the coverage-dependent trends (e.g., monotonicity of the work function change) are physically sound. Each step contributes a weight to the final reward (a floating point between 0 and 1). Merely copying expected numbers without executing the self-consistent simulation will not earn the full reward because the verifier evaluates the correctness of the computed values and trends.
