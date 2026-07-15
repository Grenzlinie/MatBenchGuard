# CALPHAD Thermodynamic Optimization of the Ga-Ti Binary System

## Problem background
The Ga–Ti binary system is of interest for semiconductor device fabrication and novel soldering applications. Accurate thermodynamic data are essential for understanding phase stability and optimising processing conditions. This work consists of a CALPHAD thermodynamic optimisation that determines a self-consistent set of Gibbs energy parameters for all stable phases—liquid, b.c.c., h.c.p., f.c.c. solid solutions, and several intermetallic compounds—using available experimental phase diagram and thermochemical data.

## Approach
The CALPHAD method treats each phase with appropriate thermodynamic models. Solution phases (liquid, b.c.c., h.c.p., f.c.c.) are described by substitutional regular solutions with Redlich–Kister excess Gibbs energy expansions. Compounds with narrow homogeneity ranges are treated as stoichiometric line compounds, while those exhibiting measurable solubility (GaTi3, Ga4Ti5, GaTi) are represented by a two-sublattice compound energy model (CEM) with (Ga,Ti) mixing on each sublattice. A two-step least-squares optimisation is employed: first, all compounds are treated as stoichiometric to establish the overall phase diagram topology; then the CEM is introduced for the ordered phases to refine the description. The optimisation uses the provided experimental dataset (invariant reaction temperatures, phase boundary points, calorimetric values) and the standard SGTE pure-element Gibbs energy functions (available within pycalphad). Once optimised, the parameter set is used to compute the equilibrium phase diagram (extracting all invariant reactions and their temperatures) and the formation enthalpies of the intermetallic compounds at 298 K.

## Reproduction target
Using the supplied Ga–Ti experimental dataset and the pycalphad package, perform the CALPHAD optimisation as described above and produce:

1. A CSV file listing all stable invariant reactions (eutectic, peritectic, peritectoid, congruent melting) with their reaction type and calculated temperature.
2. A CSV file listing the formation enthalpy (kJ per mole of atoms) at 298 K for each intermetallic compound (GaTi3, GaTi2, Ga3Ti5, Ga4Ti5, GaTi, Ga3Ti2, Ga2Ti, Ga3Ti).

The computed temperatures and enthalpies should be consistent with the experimental data that were used in the optimisation.

## Assets

- Ga-Ti experimental phase diagram and thermodynamic data
- pycalphad: pip install pycalphad

## Workflow steps

### Step 1: Least-squares optimization of Ga-Ti thermodynamic parameters
- Role: process
- Action: Using pycalphad, perform a least-squares optimization of the Gibbs energy parameters for the Ga-Ti system. Use the Ga-Ti experimental dataset (invariant temperatures, phase boundaries, calorimetric data) and pure element Gibbs energies from the SGTE database (bundled with pycalphad). Solution phases (liquid, bcc, hcp, fcc) are described by subregular Redlich-Kister models. Compounds GaTi2, Ga3Ti5, Ga3Ti2, Ga2Ti, and Ga3Ti are treated as stoichiometric; GaTi3, Ga4Ti5, and GaTi are modeled with the two-sublattice compound energy model (CEM) to account for homogeneity ranges. Follow a two-step approach: first fit all compounds as line compounds to establish the basic phase diagram framework, then refine with the CEM for the ordered compounds. Write the final optimized parameter set to optimized_parameters.txt.
- Evidence: `/app/outputs/optimized_parameters.txt`

### Step 2: Calculate invariant reaction temperatures
- Role: scored (load-bearing)
- Action: Compute the equilibrium phase diagram with the optimized parameters using pycalphad and extract all invariant reactions (eutectic, peritectic, peritectoid, congruent melting) together with their temperatures and compositions. Export the list as a CSV file.
- Output file: `/app/outputs/calculated_invariant_reactions.csv`
- Format: csv
- Contract: CSV with columns: reaction_type (string, e.g., 'eutectic'), temperature_K (float), phase_compositions (string, optional)
- Scoring: scored by hidden verifier

### Step 3: Calculate formation enthalpies at 298 K
- Role: scored
- Action: Using the optimized parameters, calculate the formation enthalpies (kJ per mole of atoms) at 298 K for all eight intermetallic compounds: GaTi3, GaTi2, Ga3Ti5, Ga4Ti5, GaTi, Ga3Ti2, Ga2Ti, Ga3Ti. Write the results to a CSV file.
- Output file: `/app/outputs/calculated_formation_enthalpies_298K.csv`
- Format: csv
- Contract: CSV with columns: compound (string), enthalpy_kJ_per_mol_atom (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_invariant_reactions.csv`
- `/app/outputs/calculated_formation_enthalpies_298K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_invariant_reactions.csv
- path: `/app/outputs/calculated_invariant_reactions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: List of invariant reactions with their types and calculated temperatures; each row is one reaction.
- schema:
  - `type`: table
  - `required_columns`: `reaction_type`, `temperature_K`
  - `units`:
    - `temperature_K`: K

### calculated_formation_enthalpies_298K.csv
- path: `/app/outputs/calculated_formation_enthalpies_298K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation enthalpies of intermetallic compounds at 298 K; each row one compound.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `enthalpy_kJ_per_mol_atom`
  - `units`:
    - `enthalpy_kJ_per_mol_atom`: kJ/mol-atom

Notes: The checker reads the agent's optimized_parameters.txt and recomputes invariant reaction data and formation enthalpies using pycalphad, then compares the recomputed values (not the agent's CSV files) against hidden experimental gold with tolerances. The CSV files are cross-checked for consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_invariant_reactions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_type",
          "temperature_K"
        ],
        "units": {
          "temperature_K": "K"
        }
      },
      "description": "List of invariant reactions with their types and calculated temperatures; each row is one reaction."
    },
    {
      "file": "calculated_formation_enthalpies_298K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "enthalpy_kJ_per_mol_atom"
        ],
        "units": {
          "enthalpy_kJ_per_mol_atom": "kJ/mol-atom"
        }
      },
      "description": "Formation enthalpies of intermetallic compounds at 298 K; each row one compound."
    }
  ],
  "notes": "The checker reads the agent's optimized_parameters.txt and recomputes invariant reaction data and formation enthalpies using pycalphad, then compares the recomputed values (not the agent's CSV files) against hidden experimental gold with tolerances. The CSV files are cross-checked for consistency."
}
```

## How you are scored
Your submission will be graded by a hidden automated verifier that independently evaluates each output artifact. For the invariant reactions, the verifier compares your calculated temperatures (and optionally phase compositions) against a set of experimentally determined reference values; each reaction with a temperature within an automatically defined tolerance contributes to the score. For the formation enthalpies, your 298 K values are compared against reference experimental enthalpies with a separate tolerance. The final reward is a weighted combination of these two components. The verifier may also cross-check consistency between your submitted files and a recomputation from your optimised parameters. Simply reporting literature values without actually performing the optimisation will not yield a valid score.
