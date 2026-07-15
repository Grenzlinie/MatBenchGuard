# DFT Activation Barriers for Ti-Silica Peroxide Intermediates

## Problem background
Understanding the atomic-scale details of active sites and reactive intermediates in heterogeneous catalysts is central to rational catalyst design. In this context, titanium-containing silica materials are widely used for the epoxidation of alkenes with peroxides. The active site is believed to be a Ti(IV) center tripodally anchored via oxygen bridges to the silica framework, with an additional OH ligand. During catalytic turnover, hydrogen peroxide binds to this Ti–OH site, forming either an η¹ or η² peroxo intermediate. Knowledge of the structures and relative stabilities of these intermediates, as well as the height of the barriers separating them, is critical for interpreting kinetic data and spectroscopic observables. This task targets the computational reproduction of the density functional theory (DFT) study that mapped out the potential energy surface for peroxide binding on such a Ti-silica cluster model. You will compute total energies for all stationary points along the formation and interconversion pathways of the two peroxide intermediates.

## Approach
We adopt a non-local density functional theory (DFT) approach using an open-source code of your choice (e.g., ORCA, CP2K, Quantum ESPRESSO). The catalyst is represented by a finite molecular cluster model of composition (H3SiO3)3–Ti–OH, where the three SiO3 groups mimic the three silicon tetrahedra that anchor the Ti center to the silica surface. The silicon atoms are kept fixed during all calculations to approximate the steric constraints of the extended silica framework. Hydrogen peroxide (H2O2) is treated as an isolated molecule. The workflow proceeds in several stages:
- Geometry optimizations are performed for the bare active site cluster, the isolated peroxide molecule, and the two possible peroxide‑bound intermediates: η¹ (end‑on) and η² (side‑on).
- Transition state searches are carried out for the elementary steps: (i) formation of the η¹ intermediate, (ii) formation of the η² intermediate, and (iii) interconversion between η¹ and η².
- From the converged total energies, activation barriers are computed as the energy difference between the transition state and the appropriate reactant complex (bare site + isolated peroxide for the formation steps, or the respective intermediate for interconversion).
A proper choice of functional and basis set (e.g., a hybrid GGA like B3LYP or PBE0) is expected; the exact combination is left to you, but the calculations should be well‑converged with respect to technical parameters.

## Reproduction target
The primary objective is to compute and report the activation barriers (in kJ/mol) for the three elementary steps: η¹ formation, η² formation, and η¹/η² interconversion, together with the underlying total DFT energies (in Hartree). The final output is a single JSON file, energies.json, containing all seven total energies and the three barriers. The quantities must be physically reasonable and internally consistent; the hidden verifier will check that the barriers obey expected structural relationships (e.g., comparable magnitudes for the two formations, and a low interconversion barrier). No experimental data or pre‑trained model is provided; you must build the cluster, run the full DFT workflow, and extract the energies yourself.

## Assets

- Open-source non-local DFT software (e.g., ORCA, CP2K, Quantum ESPRESSO): https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Build cluster model
- Role: process
- Action: Construct the (H3SiO3)3–Ti–OH cluster model with silicon atoms fixed, and prepare an isolated hydrogen peroxide molecule (H2O2). Write the cluster and peroxide coordinates into a single coordinate file.
- Evidence: `/app/outputs/cluster_model.xyz`

### Step 2: Run DFT optimizations and transition-state searches
- Role: process
- Action: Using an open-source non-local DFT code, perform geometry optimizations of the bare cluster, isolated peroxide, and η¹ and η² peroxide-bound intermediates. Carry out transition-state searches for η¹ formation, η² formation, and interconversion, with silicon atoms fixed. Record total energies of all stationary points.
- Evidence: `/app/outputs/dft_energies.log`

### Step 3: Compile energies and report barriers
- Role: scored (load-bearing)
- Action: Collect the total DFT energies (in Hartree) and compute activation barriers (in kJ/mol) for η¹ formation, η² formation, and interconversion. Write all values to energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: JSON object with keys: E_bare_active_site, E_isolated_peroxide, E_eta1_intermediate, E_eta2_intermediate, E_TS_eta1_formation, E_TS_eta2_formation, E_TS_interconversion, E_eta1_formation_barrier_kJmol, E_eta2_formation_barrier_kJmol, E_interconversion_barrier_kJmol. All energies in Hartree, barriers in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation barriers and total DFT energies for the formation and interconversion of η¹ and η² peroxide intermediates on a Ti-silica cluster model.
- schema:
  - `type`: object
  - `required`: `E_bare_active_site`, `E_isolated_peroxide`, `E_eta1_intermediate`, `E_eta2_intermediate`, `E_TS_eta1_formation`, `E_TS_eta2_formation`, `E_TS_interconversion`, `E_eta1_formation_barrier_kJmol`, `E_eta2_formation_barrier_kJmol`, `E_interconversion_barrier_kJmol`
  - `properties`:
    - `E_bare_active_site`:
      - `type`: number
      - `unit`: Hartree
    - `E_isolated_peroxide`:
      - `type`: number
      - `unit`: Hartree
    - `E_eta1_intermediate`:
      - `type`: number
      - `unit`: Hartree
    - `E_eta2_intermediate`:
      - `type`: number
      - `unit`: Hartree
    - `E_TS_eta1_formation`:
      - `type`: number
      - `unit`: Hartree
    - `E_TS_eta2_formation`:
      - `type`: number
      - `unit`: Hartree
    - `E_TS_interconversion`:
      - `type`: number
      - `unit`: Hartree
    - `E_eta1_formation_barrier_kJmol`:
      - `type`: number
      - `unit`: kJ/mol
    - `E_eta2_formation_barrier_kJmol`:
      - `type`: number
      - `unit`: kJ/mol
    - `E_interconversion_barrier_kJmol`:
      - `type`: number
      - `unit`: kJ/mol

Notes: The scored output is a single JSON file with total energies and derived activation barriers. The hidden checker will compare the reported barriers to a reference value and verify internal structural consistency. No hidden gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "E_bare_active_site",
          "E_isolated_peroxide",
          "E_eta1_intermediate",
          "E_eta2_intermediate",
          "E_TS_eta1_formation",
          "E_TS_eta2_formation",
          "E_TS_interconversion",
          "E_eta1_formation_barrier_kJmol",
          "E_eta2_formation_barrier_kJmol",
          "E_interconversion_barrier_kJmol"
        ],
        "properties": {
          "E_bare_active_site": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_isolated_peroxide": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_eta1_intermediate": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_eta2_intermediate": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_TS_eta1_formation": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_TS_eta2_formation": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_TS_interconversion": {
            "type": "number",
            "unit": "Hartree"
          },
          "E_eta1_formation_barrier_kJmol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "E_eta2_formation_barrier_kJmol": {
            "type": "number",
            "unit": "kJ/mol"
          },
          "E_interconversion_barrier_kJmol": {
            "type": "number",
            "unit": "kJ/mol"
          }
        }
      },
      "description": "Activation barriers and total DFT energies for the formation and interconversion of η¹ and η² peroxide intermediates on a Ti-silica cluster model."
    }
  ],
  "notes": "The scored output is a single JSON file with total energies and derived activation barriers. The hidden checker will compare the reported barriers to a reference value and verify internal structural consistency. No hidden gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads your energies.json file. It will:
1. Verify that the file contains all ten required fields.
2. Recompute the three activation barriers from the total energies you supplied, to confirm internal consistency.
3. Compare each barrier against a hidden reference value that represents the expected range for this system. The closer your barriers are to the reference, the higher the score.
4. Check that the three barriers satisfy a physically motivated structural ordering (the two formation barriers should be similar, and the interconversion barrier should not greatly exceed the formation barriers).

The overall reward is a weighted sum of these checks. A submission that merely reports numbers without having genuinely executed the DFT calculations will not receive credit, because the verifier’s checks depend on values that can only be obtained by completing the computational workflow. All credit is derived from the contents of energies.json; other files (e.g., intermediate coordinate files, log files) are auditable evidence but do not directly contribute to the reward.
