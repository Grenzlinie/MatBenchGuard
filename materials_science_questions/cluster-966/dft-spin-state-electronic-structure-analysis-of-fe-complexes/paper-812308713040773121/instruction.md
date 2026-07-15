# B3LYP DFT calculations on bis(imidazole) iron-porphyrin: geometries, spin-state energies, and Mössbauer quadrupole splittings

## Problem background
Density functional theory (DFT) is widely used to model the electronic structure of heme proteins, yet the predicted energy ordering of different spin states is highly sensitive to the choice of exchange–correlation functional. For iron–porphyrin complexes, different functionals can yield contradictory predictions for spin ground states, geometries, and spectroscopic observables such as Mössbauer quadrupole splittings. Therefore, it is important to assess DFT predictions by comparing multiple computed properties—optimized metal–ligand bond lengths, high-spin/low-spin total-energy differences, and Mössbauer quadrupole splittings—against available experimental data. This task focuses on a specific hybrid functional and a six-coordinate bis(imidazole) iron–porphyrin model, a representative heme with strong-field axial ligands. The goal is to compute these quantities directly from first-principles DFT calculations so that they can be compared with experimental observations.

## Approach
The central idea is to perform unrestricted Kohn–Sham DFT calculations using a hybrid functional that includes a fraction of exact Hartree–Fock exchange. The model system is a six-coordinate iron–porphyrin with two axial imidazole ligands coordinated in parallel, constrained to Cs symmetry. Four distinct spin/oxidation states are considered: ferrous low-spin (¹A'), ferrous high-spin (⁵A''), ferric low-spin (²A''), and ferric high-spin (⁶A'). For each state, a full geometry optimization is carried out using a triple-zeta basis set on iron and a double-zeta polarized basis on all other atoms, with the hybrid functional B3LYP. Initial orbital occupancies for the open-shell states follow the Fe(3d) occupations reported in the literature (see step 1). After geometry convergence, the electric field gradient (EFG) tensor at the iron nucleus is computed on the optimized structure. From these calculations, two kinds of results are extracted: (i) the average Fe–N bond lengths for the ferrous singlet, providing a geometric check; (ii) the high-spin/low-spin total-energy differences for both the ferrous and ferric redox states; and (iii) the Mössbauer quadrupole splitting ΔE_Q for the ferrous singlet and ferric doublet, derived from the principal components of the EFG tensor using the nuclear quadrupole moment of iron (Q = 0.16 barn) via the standard relation ΔE_Q = (1/2) e Q V_ZZ (1 + η²/3)^{1/2}. The workflow is implemented with the open-source NWChem package.

## Reproduction target
The required output is a single JSON file results.json containing exactly six numeric fields computed from the DFT workflow:

- fe_n_eps (Fe–N_ε distance in Å for the ferrous ¹A' state)
- fe_n_p (Fe–N_p distance in Å for the same state)
- delta_e_hs_ls_fe2 (high-spin – low-spin total-energy difference for ferrous iron, in kcal mol⁻¹)
- delta_e_hs_ls_fe3 (same energy difference for ferric iron, in kcal mol⁻¹)
- delta_e_q_fe2_singlet (Mössbauer quadrupole splitting for the ferrous singlet, in mm s⁻¹)
- delta_e_q_fe3_doublet (Mössbauer quadrupole splitting for the ferric doublet, in mm s⁻¹)

The relative ordering and magnitudes of these quantities are the target of the reproduction; a hidden verifier compares them to independently established reference values.

## Assets

- NWChem computational chemistry package: https://github.com/nwchemgit/nwchem

## Workflow steps

### Step 1: Prepare molecular models and initial densities
- Role: process
- Action: Construct the molecular model for [FeP(Im)₂] with C_s symmetry and parallel axial imidazole ligands. Generate initial Cartesian coordinates for the porphyrin ring, the iron centre, and the two imidazole ligands. Prepare the initial electron density guess (fragment-based UHF) for the four required spin/oxidation states—ferrous low-spin (¹A'), ferrous high-spin (⁵A''), ferric low-spin (²A''), and ferric high-spin (⁶A')—using the Fe(3d) orbital occupation numbers given in the paper.
- Evidence: `/app/outputs/model_config.txt`

### Step 2: DFT geometry optimizations and EFG calculations
- Role: process
- Action: For each of the four spin/oxidation states, run a DFT geometry optimization using the B3LYP functional, Ahlrichs VTZ basis set on iron, and 6-31G* on all other atoms. Use NWChem with the appropriate spin multiplicity and initial orbital occupations from step 1. After geometry convergence, perform an electric field gradient (EFG) calculation at the iron nucleus on the optimized structure to obtain the EFG tensor components.
- Evidence: `/app/outputs/dft_logs.txt`

### Step 3: Extract distances, spin-state energies, and Mössbauer quadrupole splittings
- Role: scored (load-bearing)
- Action: From the completed DFT calculations, extract the average Fe–N_ε and Fe–N_p distances for the ferrous singlet (¹A') state. Compute the high-spin/low-spin total-energy difference ΔE_hs/ls = E(high-spin) − E(low-spin) in kcal mol⁻¹ for the ferrous pair (⁵A'' − ¹A') and the ferric pair (⁶A' − ²A''). Using the EFG tensors, compute the Mössbauer quadrupole splitting ΔE_Q for the ferrous singlet (¹A') and the ferric doublet (²A'') with the nuclear quadrupole moment Q = 0.16 barn, following the standard formula. Write all six numeric values as a JSON object to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"fe_n_eps": <float>, "fe_n_p": <float>, "delta_e_hs_ls_fe2": <float>, "delta_e_hs_ls_fe3": <float>, "delta_e_q_fe2_singlet": <float>, "delta_e_q_fe3_doublet": <float>}
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
- target_policy: exact_match
- description: The six numeric results for the B3LYP bis(imidazole) model: two Fe-ligand bond lengths, two high-spin/low-spin energy differences, and two Mössbauer quadrupole splittings.
- schema:
  - `type`: object
  - `required`: `fe_n_eps`, `fe_n_p`, `delta_e_hs_ls_fe2`, `delta_e_hs_ls_fe3`, `delta_e_q_fe2_singlet`, `delta_e_q_fe3_doublet`
  - `properties`:
    - `fe_n_eps`:
      - `type`: number
      - `description`: Fe–N_ε distance in Å
    - `fe_n_p`:
      - `type`: number
      - `description`: Fe–N_p distance in Å
    - `delta_e_hs_ls_fe2`:
      - `type`: number
      - `description`: Fe(II) high-spin/low-spin energy difference in kcal mol⁻¹
    - `delta_e_hs_ls_fe3`:
      - `type`: number
      - `description`: Fe(III) high-spin/low-spin energy difference in kcal mol⁻¹
    - `delta_e_q_fe2_singlet`:
      - `type`: number
      - `description`: Mössbauer quadrupole splitting for ferrous singlet in mm s⁻¹
    - `delta_e_q_fe3_doublet`:
      - `type`: number
      - `description`: Mössbauer quadrupole splitting for ferric doublet in mm s⁻¹

Notes: The hidden checker compares each field to the paper-reported B3LYP values with per-field tolerances. Tolerances and gold values are not disclosed to the solving agent.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "fe_n_eps",
          "fe_n_p",
          "delta_e_hs_ls_fe2",
          "delta_e_hs_ls_fe3",
          "delta_e_q_fe2_singlet",
          "delta_e_q_fe3_doublet"
        ],
        "properties": {
          "fe_n_eps": {
            "type": "number",
            "description": "Fe–N_ε distance in Å"
          },
          "fe_n_p": {
            "type": "number",
            "description": "Fe–N_p distance in Å"
          },
          "delta_e_hs_ls_fe2": {
            "type": "number",
            "description": "Fe(II) high-spin/low-spin energy difference in kcal mol⁻¹"
          },
          "delta_e_hs_ls_fe3": {
            "type": "number",
            "description": "Fe(III) high-spin/low-spin energy difference in kcal mol⁻¹"
          },
          "delta_e_q_fe2_singlet": {
            "type": "number",
            "description": "Mössbauer quadrupole splitting for ferrous singlet in mm s⁻¹"
          },
          "delta_e_q_fe3_doublet": {
            "type": "number",
            "description": "Mössbauer quadrupole splitting for ferric doublet in mm s⁻¹"
          }
        }
      },
      "description": "The six numeric results for the B3LYP bis(imidazole) model: two Fe-ligand bond lengths, two high-spin/low-spin energy differences, and two Mössbauer quadrupole splittings."
    }
  ],
  "notes": "The hidden checker compares each field to the paper-reported B3LYP values with per-field tolerances. Tolerances and gold values are not disclosed to the solving agent."
}
```

## How you are scored
After you write results.json, a hidden verifier reads the six numbers and compares each one to a hidden reference value that represents the correct B3LYP result for this model. Each field is evaluated with a tolerance appropriate for DFT methodology (the tolerances are not disclosed). The reward is the fraction of the six fields that lie within their respective tolerance ranges. The verifier does not award credit for reporting the correct trend alone; each numeric value must be individually within tolerance. The overall reward ranges from 0.0 (no field within tolerance) to 1.0 (all six fields within tolerance). The verifier runs automatically and does not provide partial feedback.
