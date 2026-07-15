# Co-N4 Single-Atom ORR Working Potential from DFT

## Problem background
Single-atom catalysts (SACs) with transition-metal–nitrogen–carbon (M–N–C) active sites are promising for the oxygen reduction reaction (ORR), a key process in fuel cells and metal–air batteries. The electronic structure of the metal centre is sensitive to the surrounding carbon support, and structural defects in the carbon are hypothesised to alter adsorption energetics and catalytic activity. This task investigates, through density functional theory (DFT), whether a carbon vacancy adjacent to a Co–N₄ site (a defect model obtained via decarboxylation of a metal–organic framework precursor) changes the ORR free-energy profile relative to a pristine Co–N₄ site. The working potential U (the highest electrode potential at which all ORR elementary steps are thermodynamically downhill) and the free-energy change of the O₂ → *OOH step at a fixed potential are the quantities to compute, as they serve as indicators of intrinsic activity.

## Approach
Two atomic models are constructed and studied with DFT:
1. A pristine Co–N₄ moiety embedded in a graphene sheet.
2. The Co–N₄-6r-c2 defect model: a Co–N₄ moiety adjacent to a six-membered ring from which one carbon atom is removed (a carbon vacancy).

For each model, spin-polarised periodic DFT total-energy calculations are performed for the clean slab and for the three adsorbed ORR intermediates *OOH, *O, and *OH. The computational hydrogen electrode (CHE) model is then applied to the computed total energies to obtain adsorption free energies. From these, the working potential U is determined for each model: U is the highest potential (V vs. SHE) at which all four elementary steps (O₂ → *OOH, *OOH → *O + H₂O, *O → *OH, *OH → H₂O) are downhill in free energy. Additionally, for the defect model, the free-energy change ΔG for the O₂ → *OOH step is evaluated at an applied potential of U = 0.83 V vs. SHE. The comparison between the pristine and defect models (U values, and the ΔG at 0.83 V) reveals whether the defect alters the thermodynamic ORR activity.

## Reproduction target
Construct the two Co–N₄ atomic models described above. Perform DFT total-energy calculations for the clean slabs and for the *OOH, *O, and *OH adsorbates on each model, and record the energies (Step 1). From these energies, apply the CHE model to compute:
- The working potential U for the pristine Co–N₄ model (pristine_CoN4_U, in V vs. SHE).
- The working potential U for the Co–N₄-6r-c2 defect model (defect_CoN4_U, in V vs. SHE).
- The free-energy change ΔG for the O₂ → *OOH step on the defect model at an applied potential of 0.83 V vs. SHE (defect_O2_to_OOH_deltaG_at_0_83, in eV).

Write the three computed values into the JSON file `/app/outputs/dft_results.json` according to the schema given in the output contract. The results must be obtained from actual DFT and CHE calculations; reporting hand-chosen or literature values will not satisfy the scoring criteria.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, GPAW)
- Atomic Simulation Environment (ASE) or similar: https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: DFT energy calculations for Co-N4 models
- Role: process
- Action: Construct atomic models of (a) a pristine Co-N4 site embedded in a graphene layer and (b) the Co-N4-6r-c2 defect model (a Co-N4 moiety adjacent to a six-membered ring with a carbon vacancy) as described in the Approach section above. Perform DFT total-energy calculations for the clean slab and for adsorbed ORR intermediates (*OOH, *O, *OH) on each model. Save the computed total energies.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 2: Free-energy analysis and working potential calculation
- Role: scored (load-bearing)
- Action: From the DFT energies in step_01_dft_energies, apply the computational hydrogen electrode (CHE) model to compute adsorption free energies for *OOH, *O, and *OH. Determine the working potential U for each model (the highest potential at which all elementary steps are downhill in free energy). Compute the free-energy change for the O2 → *OOH step at a fixed potential of 0.83 V vs. SHE for the defect model. Write the results as a JSON object with the required fields.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {
  "pristine_CoN4_U": { "type": "number", "description": "Working potential for pristine Co-N4 model (V vs. SHE)" },
  "defect_CoN4_U": { "type": "number", "description": "Working potential for Co-N4-6r-c2 defect model (V vs. SHE)" },
  "defect_O2_to_OOH_deltaG_at_0_83": { "type": "number", "description": "Free-energy change (eV) for O2 -> *OOH on the defect model at U=0.83 V vs. SHE" }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's computed working potentials and free-energy change. The checker compares these values to the paper's hidden gold values with tolerances suitable for different DFT toolchains and additionally verifies that defect_CoN4_U > pristine_CoN4_U and defect_O2_to_OOH_deltaG_at_0_83 < 0.
- schema:
  - `type`: object
  - `required`:
    - `pristine_CoN4_U`: number (V vs. SHE)
    - `defect_CoN4_U`: number (V vs. SHE)
    - `defect_O2_to_OOH_deltaG_at_0_83`: number (eV)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The agent must perform DFT calculations independently; no pre-computed energies or data are provided. The working potential U is defined as the highest potential (V vs. SHE) at which all ORR elementary steps (O2 → *OOH, *OOH → *O + H2O, *O → *OH, *OH → H2O) are downhill in free energy using the CHE model. The free-energy change for O2 → *OOH on the defect model must be evaluated at U = 0.83 V vs. SHE.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine_CoN4_U": "number (V vs. SHE)",
          "defect_CoN4_U": "number (V vs. SHE)",
          "defect_O2_to_OOH_deltaG_at_0_83": "number (eV)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The agent's computed working potentials and free-energy change. The checker compares these values to the paper's hidden gold values with tolerances suitable for different DFT toolchains and additionally verifies that defect_CoN4_U > pristine_CoN4_U and defect_O2_to_OOH_deltaG_at_0_83 < 0."
    }
  ],
  "notes": "The agent must perform DFT calculations independently; no pre-computed energies or data are provided. The working potential U is defined as the highest potential (V vs. SHE) at which all ORR elementary steps (O2 → *OOH, *OOH → *O + H2O, *O → *OH, *OH → H2O) are downhill in free energy using the CHE model. The free-energy change for O2 → *OOH on the defect model must be evaluated at U = 0.83 V vs. SHE."
}
```

## How you are scored
A hidden verifier independently processes your submitted artifacts. Each workflow stage contributes a portion of the total reward, and the individual scores are combined into a final reward between 0 and 1. The verifier compares your reported `dft_results.json` values to reference data that embody the paper’s findings, using tolerances that accommodate legitimate variation among open‑source DFT tools and pseudopotentials. In addition to numerical tolerances, the verifier checks structural requirements: for example, that the defect model’s working potential exceeds that of the pristine model and that the O₂ → *OOH free-energy change on the defect model at 0.83 V is negative. No credit is awarded for simply reproducing the paper’s published numbers; the checks are designed to reward a genuine computational reproduction of the DFT workflow and CHE analysis.
