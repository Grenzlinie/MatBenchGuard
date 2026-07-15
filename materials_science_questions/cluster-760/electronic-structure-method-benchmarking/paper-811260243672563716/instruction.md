# Compute ion association thermodynamics for LiBOB in EC:DMC mixture with DFT and mixed solvation approach

## Problem background
Ion association of lithium salts in aprotic solvent mixtures directly affects the conductivity and performance of lithium-ion batteries. Accurately predicting the extent of ion pairing is challenging because different computational solvation models can yield contradictory results. This task focuses on computing the standard Gibbs free energy change of ion association for lithium bis(oxalato)borate (LiBOB) in a binary solvent mixture of ethylene carbonate and dimethyl carbonate (EC:DMC, 7:3 weight ratio). The goal is to evaluate the predictive capability of continuum, discrete, and mixed discrete-continuum solvation descriptions within a density functional theory (DFT) framework.

## Approach
The ion association process is described by a thermodynamic cycle that relates the gas-phase ion-pair formation free energy and the solvation free energies of the free ions and the ion pair. Three solvation models are implemented: (I) continuum model – bare ions and ion pair are embedded in a structureless dielectric continuum; (II) discrete model – the first solvation shell is explicitly included via the most stable gas-phase solvatocomplexes; (III) mixed discrete-continuum model – the chemically bound solvent molecules are kept explicit, and the remainder of the solvent is represented by a continuum dielectric. All quantum-chemical calculations are performed at the B3LYP/6-31+G(2d) level (or an equivalent open-source implementation). Gas-phase geometries and harmonic frequencies are obtained for all relevant species, and the most exergonic cation, anion, and ion-pair solvatocomplexes are identified from the computed Gibbs free energies of formation. Solvation free energies are computed with the isodensity polarizable continuum model (IPCM) using the experimental dielectric constant (ε = 51.0) of the solvent mixture. Combining the gas-phase and solvation data via the thermodynamic cycle yields the standard Gibbs free energy change of ion association for each solvation model.

## Reproduction target
Compute the standard Gibbs free energy change of ion association (ΔassG°) for LiBOB in the EC:DMC (7:3) solvent mixture under the three solvation models: continuum-only (I), discrete-only (II), and mixed discrete-continuum (III). Additionally, report the gas-phase ion-pair formation Gibbs free energy Δass(g)G°. The final output must be a JSON file containing four floating-point values in kJ/mol.

## Assets

- ORCA quantum chemistry software (or Psi4): https://orcaforum.kofo.mpg.de/
- Python numeric packages (numpy, scipy): numpy, scipy

## Workflow steps

### Step 1: Gas-phase DFT calculations and identification of stable solvatocomplexes
- Role: process
- Action: Perform geometry optimization and harmonic frequency calculations at B3LYP/6-31+G(2d) level (or equivalent with an open-source code) for all species: Li+, BOB-, EC, [Li+BOB-] ion pair, [Li(EC)n]+ (n=1..5), [BOB(EC)#]- (#=A..D), [Li+(EC)mBOB-] (m=1,2). Compute standard thermodynamic potentials (ΔE, ΔU°, ΔH°, ΔS°, ΔG°) for each gas-phase complex formation reaction at T=298.15 K. Based on gas-phase ΔG° of formation, identify the most stable cation solvatocomplex ([Li(EC)4]+), anion solvatocomplex ([BOB(EC)C]-), and ion-pair solvatocomplex ([Li+(EC)2BOB-]). Save the raw thermodynamic data and the identity of the selected complexes to an evidence file.
- Evidence: `/app/outputs/gas_phase_gibbs.csv`

### Step 2: Continuum solvation IPCM calculations
- Role: process
- Action: Using the gas-phase optimized geometries from step 1, perform IPCM single-point energy calculations with dielectric constant ε=51.0 (the EC:DMC 7:3 mixture) on the following species: Li+, BOB-, [Li+BOB-], [Li(EC)4]+, [Li+(EC)2BOB-], and EC. Apply standard-state corrections to compute solvation Gibbs free energies as described in the method (IPCM contour 0.0002 e Bohr^-3). Save the computed solvation energies (ΔsolvH, ΔsolvS, ΔsolvG) for each species to an evidence file.
- Evidence: `/app/outputs/solvation_energies.json`

### Step 3: Ion association thermodynamics from thermodynamic cycle
- Role: scored (load-bearing)
- Action: Combine the gas-phase ion-pair formation thermodynamics (from step 1) and the solvation data (from step 2) to compute, via the thermodynamic cycle described in the reference method, the standard Gibbs free energy change of ion association for the three solvation models: ΔassG° (AI, continuum-only), ΔassG° (AII, discrete-only), and ΔassG° (AIII, mixed discrete-continuum). Also compute the gas-phase ion-pair formation Δass(g)G°. Output the four values in a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with four numeric fields: delta_ass_G_AI_kJ_per_mol, delta_ass_G_AII_kJ_per_mol, delta_ass_G_AIII_kJ_per_mol, delta_ass_g_G_kJ_per_mol. Each value is a floating-point number in units kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Standard Gibbs free energy changes (kJ/mol) for LiBOB ion association in EC:DMC (7:3) computed under the continuum-only (AI), discrete-only (AII), mixed discrete-continuum (AIII) solvation models, and the gas-phase ion-pair formation reference.
- schema:
  - `type`: object
  - `required`:
    - `delta_ass_G_AI_kJ_per_mol`: float (units: kJ/mol)
    - `delta_ass_G_AII_kJ_per_mol`: float (kJ/mol)
    - `delta_ass_G_AIII_kJ_per_mol`: float (kJ/mol)
    - `delta_ass_g_G_kJ_per_mol`: float (kJ/mol)

Notes: The hidden checker compares each reported value against the paper's reference values with appropriate sign and magnitude tolerances. Compliance with the required sign patterns (AI positive large, AII negative large, AIII positive small) is expected. The gas-phase Δass(g)G° is checked within a tolerance window.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_ass_G_AI_kJ_per_mol": "float (units: kJ/mol)",
          "delta_ass_G_AII_kJ_per_mol": "float (kJ/mol)",
          "delta_ass_G_AIII_kJ_per_mol": "float (kJ/mol)",
          "delta_ass_g_G_kJ_per_mol": "float (kJ/mol)"
        }
      },
      "description": "Standard Gibbs free energy changes (kJ/mol) for LiBOB ion association in EC:DMC (7:3) computed under the continuum-only (AI), discrete-only (AII), mixed discrete-continuum (AIII) solvation models, and the gas-phase ion-pair formation reference."
    }
  ],
  "notes": "The hidden checker compares each reported value against the paper's reference values with appropriate sign and magnitude tolerances. Compliance with the required sign patterns (AI positive large, AII negative large, AIII positive small) is expected. The gas-phase Δass(g)G° is checked within a tolerance window."
}
```

## How you are scored
A hidden verifier checks each workflow stage's output independently. The final results.json is the load-bearing scored artifact. The verifier compares your reported ΔassG° values against reference gold values obtained under the same physical conditions and assigns a score based on how close your numbers are to the correct answers, with appropriate tolerance windows. Scores are awarded monotonically: the closer your computed value to the correct target (in absolute or sign senses), the higher your score, with full credit when the value meets or exceeds the acceptable threshold. Partial credit is given for results within allowed deviations. The overall reward is a weighted combination of the per-quantity scores. Reproducing the reference numbers without faithfully executing the described DFT and thermodynamic cycle steps is not sufficient; the verifier may perform structural consistency checks.
