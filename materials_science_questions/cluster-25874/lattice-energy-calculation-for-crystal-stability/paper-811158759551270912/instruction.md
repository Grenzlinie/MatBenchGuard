# DFT/ESP Thermochemical Property Estimation for Tetrazine Derivatives

## Problem background
High-energy-density materials (HEDMs), especially nitrogen-rich heterocyclic compounds, are actively investigated for energetic applications. Six-membered 1,2,4,5-tetrazine derivatives are promising candidates whose detonation performance is strongly linked to their condensed-phase enthalpy of formation and crystal density. Accurately predicting these thermochemical properties from molecular structure using computational methods allows rapid screening of novel candidates. This task targets the prediction of molecular electrostatic potential (ESP) descriptors, enthalpy of sublimation, crystal density, and gas- and solid-phase enthalpies of formation for a set of ten nitrogen-rich tetrazine derivatives bearing various energetic substituents. The quantities to be computed are those that would be obtained by a modern quantum chemistry workflow combining density functional theory (DFT) with empirical correlations, as described next.

## Approach
The computational protocol follows a well-established approach: (1) geometry optimisation and frequency analysis at the B3LYP/6-311G(d,p) level of density functional theory for all target compounds and the reference species needed for isodesmic reaction cycles; (2) electrostatic potential analysis on the 0.001 e/Bohr³ electron-density isosurface to compute a suite of molecular surface descriptors (average potentials, variances, deviation, balance parameter); (3) empirical estimation of the standard enthalpy of sublimation using a Politzer-type formula that depends on molecular surface area and the product of the electrostatic balance parameter with the total variance; (4) empirical estimation of crystal density from molecular weight, molecular volume, and the same electrostatic product; (5) calculation of gas-phase enthalpy of formation via carefully balanced isodesmic reactions that involve small reference molecules with known experimental or high-accuracy gas-phase enthalpies of formation; and (6) conversion to solid-phase enthalpy of formation by subtracting the sublimation enthalpy. The ten derivatives span two parent scaffolds (1,2,4,5-tetrazine and its 1,4‑N‑oxide) and include commonly employed energetic substituents such as amino, nitro, nitramino, and azido groups. The complete set of isodesmic reaction schemes for each compound, together with the required reference gas-phase enthalpies for 1,2,4-triazole, 1H‑tetrazole, aniline, NO₂, NH₃, N₃, 1,2,4,5‑tetrazine, and 1,4‑N‑oxide 1,2,4,5‑tetrazine, is given in the workflow steps. This protocol, when executed with an open-source quantum chemistry code and standard Python packages, yields a consistent set of property values that can be compared to published results.

## Reproduction target
Produce a single CSV file containing all computed molecular surface properties, crystal density, enthalpy of sublimation, and gas‑ and solid‑phase enthalpies of formation for the ten nitrogen‑rich tetrazine derivatives (compounds 1–10). The file must contain exactly one row per compound, with the columns and units specified in the output contract. The complete workflow must be executed as described in the steps; reporting numbers without running the full DFT and ESP analysis pipeline will not satisfy the task.

## Assets

- Open-source quantum chemistry package (e.g., PySCF, NWChem, ORCA): https://pyscf.org
- Python scientific computing packages: numpy pandas scipy rdkit cclib
- Reference gas-phase enthalpies of formation
- Molecular structure definitions for target compounds

## Compound structures

The ten target compounds are the following nitrogen-rich tetrazine derivatives. Use RDKit or another cheminformatics tool to generate initial 3D coordinates from the IUPAC names. The compound numbering matches Table 1.

1. 3,6-diamino-1,2,4,5-tetrazine
2. 3,6-diamino-1,2,4,5-tetrazine 1,4-dioxide
3. 3,6-bis(1H-tetrazol-5-ylamino)-1,2,4,5-tetrazine
4. 3,6-bis(1H-tetrazol-5-ylamino)-1,2,4,5-tetrazine 1,4-dioxide
5. 3,6-bis(5-nitro-1H-tetrazol-1-yl)-1,2,4,5-tetrazine
6. 3,6-bis(5-nitro-1H-tetrazol-1-yl)-1,2,4,5-tetrazine 1,4-dioxide
7. 3,6-bis(5-azido-1H-tetrazol-1-yl)-1,2,4,5-tetrazine
8. 3,6-bis(5-azido-1H-tetrazol-1-yl)-1,2,4,5-tetrazine 1,4-dioxide
9. 3,6-bis(5-nitramino-1H-tetrazol-1-yl)-1,2,4,5-tetrazine
10. 3,6-bis(5-nitramino-1H-tetrazol-1-yl)-1,2,4,5-tetrazine 1,4-dioxide

## Workflow steps

### Step 1: Geometry optimization and frequency check
- Role: process
- Action: Perform geometry optimization and harmonic vibrational frequency calculation at the B3LYP/6-311G(d,p) level for all ten target compounds and all reference species: 1,2,4,5-tetrazine, 1,4 N-oxide 1,2,4,5-tetrazine, 1,2,4-triazole, 1H-tetrazole, aniline, NO2, NH3, N3, H2, and 5-amino-1H-tetrazole. Confirm that all optimized structures have no imaginary frequencies. Save the optimized geometries and total electronic energies for subsequent steps.
- Evidence: `/app/outputs/step_01_verification.log`

### Step 2: Compute molecular surface properties and formation enthalpies
- Role: scored (load-bearing)
- Action: For each of the ten compounds, using the optimized geometry: (1) Perform electrostatic potential (ESP) analysis on the 0.001 e/Bohr³ electron-density isosurface to compute molecular surface electrostatic potential descriptors (V̄_S^+, V̄_S^-, V̄_S, σ_+^2, σ_-^2, σ_tot^2, v, Π), molecular surface area A_S, and molecular volume V_m. (2) Estimate the standard enthalpy of sublimation ΔH_sub^° using the Politzer-derived empirical formula ΔH_sub^° = 0.000267 A_S² + 1.650087 (v σ_tot²)^0.5 + 2.966078. (3) Estimate crystal density ρ using ρ = 0.9183 (M/V_m) + 0.0028 (v σ_tot²) + 0.0443. (4) Compute gas-phase enthalpy of formation Δ_fH°(g) using the following exact isodesmic reaction schemes. First, determine the gas-phase enthalpy of formation of the fragment 5-amino-1H-tetrazole (denoted H2N_4N) via the auxiliary isodesmic reaction:

1H-tetrazole + NH_3 → 5-amino-1H-tetrazole + H_2

Compute its reaction enthalpy from the DFT total electronic energies (including zero-point and thermal corrections to enthalpy at 298 K) of all species, and then obtain Δ_fH°(5-amino-1H-tetrazole) using the known Δ_fH°(1H-tetrazole)=76.5 kcal/mol, Δ_fH°(NH_3)=-11.0 kcal/mol, Δ_fH°(H_2)=0 kcal/mol.

Then, for each target compound, use the following prescribed isodesmic reactions (reactants and products are given as in the original paper; compound numbering matches Table 1):

- Compound 1: 2 HN_4N + N_4N + 2 NH_3 → compound 1 + 5 H_2
- Compound 2: 2 HN_4N + O_2N_4N^+ + 2 NH_3 → compound 2 + 5 H_2
- Compound 3: 2 H_2N_4N + N_4N + 2 NO_2 → compound 3 + 7 H_2
- Compound 4: 2 H_2N_4N + O_2N_4N^+ + 2 NO_2 → compound 4 + 7 H_2
- Compound 5: 2 HN_4N + N_4N + 4 NH_3 + 4 NO_2 → compound 5
- Compound 6: 2 HN_4N + O_2N_4N^+ + 4 NH_3 + 4 NO_2 → compound 6 + 7 H_2
- Compound 7: 2 HN_4N + N_4N + 2 NH_3 + 2 NO_2 + N_3 → compound 7 + 6 H_2
- Compound 8: 2 HN_4N + O_2N_4N^+ + 2 NH_3 + 2 NO_2 + N_3 → compound 8 + 6 H_2
- Compound 9: 2 HN_4N + N_4N + 2 NH_3 + 2 NO_2 → compound 9 + 7 H_2
- Compound 10: 2 HN_4N + O_2N_4N^+ + 2 NH_3 + 2 NO_2 → compound 10 + 7 H_2

where the abbreviations denote:
  HN_4N  = 1H-tetrazole
  H_2N_4N = 5-amino-1H-tetrazole
  N_4N   = 1,2,4,5-tetrazine
  O_2N_4N^+ = 1,4 N-oxide 1,2,4,5-tetrazine
  N_3    = azide radical (N_3)

The known gas-phase enthalpies of formation (kcal/mol) at 298 K for these species are:
  HN_4N                            76.5
  H_2N_4N          (to be obtained from the auxiliary reaction)
  N_4N            -70.81
  O_2N_4N^+       -106.74
  NO_2            7.9
  NH_3           -11.0
  N_3            99.0
  H_2              0.0 (by definition)

For each target reaction, compute the reaction enthalpy from the DFT total electronic energies (including zero-point and thermal corrections to enthalpy at 298 K) of all reactants and products, then obtain Δ_fH°(g) of the target by Δ_fH°(target) = Σ Δ_fH°(products) - Δ_rH - Σ Δ_fH°(reactants), where the sum is over all species except the target (its Δ_fH° is unknown). Use the values above for the reactants/products that have listed enthalpies.

(5) Compute solid-phase enthalpy of formation Δ_fH°(s) = Δ_fH°(g) − ΔH_sub^°. Write all computed properties to step_07_computed_properties.csv.
- Output file: `/app/outputs/step_07_computed_properties.csv`
- Format: csv
- Contract: Columns: compound_id (integer 1-10), V_m (Å^3), A_S (Å^2), ρ (g/cm^3), V̄_S (kcal/mol), V̄_S^+ (kcal/mol), V̄_S^- (kcal/mol), σ_tot^2 (kcal^2/mol^2), σ_+^2 (kcal^2/mol^2), σ_-^2 (kcal^2/mol^2), ν (unitless), vσ_tot^2 (kcal^2/mol^2), Π (kcal/mol), ΔH_sub^° (kcal/mol), Δ_fH^°(g) (kcal/mol), Δ_fH^°(s) (kcal/mol). One row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_07_computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_07_computed_properties.csv
- path: `/app/outputs/step_07_computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed molecular surface properties, crystal density, enthalpy of sublimation, and gas- and solid-phase enthalpies of formation for the ten nitrogen-rich tetrazine derivatives (compounds 1-10).
- schema:
  - `type`: table
  - `required_columns`: `compound_id`, `V_m`, `A_S`, `ρ`, `V̄_S`, `V̄_S^+`, `V̄_S^-`, `σ_tot^2`, `σ_+^2`, `σ_-^2`, `ν`, `vσ_tot^2`, `Π`, `ΔH_sub^°`, `Δ_fH^°(g)`, `Δ_fH^°(s)`
  - `units`:
    - `V_m`: Å^3
    - `A_S`: Å^2
    - `ρ`: g/cm^3
    - `V̄_S`: kcal/mol
    - `V̄_S^+`: kcal/mol
    - `V̄_S^-`: kcal/mol
    - `σ_tot^2`: kcal^2/mol^2
    - `σ_+^2`: kcal^2/mol^2
    - `σ_-^2`: kcal^2/mol^2
    - `ν`: unitless
    - `vσ_tot^2`: kcal^2/mol^2
    - `Π`: kcal/mol
    - `ΔH_sub^°`: kcal/mol
    - `Δ_fH^°(g)`: kcal/mol
    - `Δ_fH^°(s)`: kcal/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_07_computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound_id",
          "V_m",
          "A_S",
          "ρ",
          "V̄_S",
          "V̄_S^+",
          "V̄_S^-",
          "σ_tot^2",
          "σ_+^2",
          "σ_-^2",
          "ν",
          "vσ_tot^2",
          "Π",
          "ΔH_sub^°",
          "Δ_fH^°(g)",
          "Δ_fH^°(s)"
        ],
        "units": {
          "V_m": "Å^3",
          "A_S": "Å^2",
          "ρ": "g/cm^3",
          "V̄_S": "kcal/mol",
          "V̄_S^+": "kcal/mol",
          "V̄_S^-": "kcal/mol",
          "σ_tot^2": "kcal^2/mol^2",
          "σ_+^2": "kcal^2/mol^2",
          "σ_-^2": "kcal^2/mol^2",
          "ν": "unitless",
          "vσ_tot^2": "kcal^2/mol^2",
          "Π": "kcal/mol",
          "ΔH_sub^°": "kcal/mol",
          "Δ_fH^°(g)": "kcal/mol",
          "Δ_fH^°(s)": "kcal/mol"
        }
      },
      "description": "Computed molecular surface properties, crystal density, enthalpy of sublimation, and gas- and solid-phase enthalpies of formation for the ten nitrogen-rich tetrazine derivatives (compounds 1-10)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your submitted `step_07_computed_properties.csv` and compare every required column against a set of reference values. Each column is checked with a fixed absolute or relative tolerance, and the verifier additionally checks that relative orderings among the compounds agree with expectation. The reward is the fraction of compounds whose rows satisfy all per-column tolerance and ordering checks. This is a result‑level comparison; fabricating numbers that do not originate from the prescribed workflow will result in a low score.
