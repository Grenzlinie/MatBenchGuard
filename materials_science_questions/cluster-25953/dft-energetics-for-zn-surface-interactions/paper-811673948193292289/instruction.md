# DFT adsorption energies of H2O and NH3 on hydrogen-terminated ZnO nanoclusters and nanosheets

## Problem background
ZnO nanostructures with high surface-to-volume ratios are promising for gas-sensing applications. Understanding how small molecules such as water (H2O) and ammonia (NH3) bind to ZnO surfaces is essential for evaluating sensor sensitivity and selectivity. This task investigates the adsorption of H2O and NH3 on a series of hydrogen-terminated ZnO nanoclusters and graphene-like ZnO nanosheets using density functional theory (DFT) at the B3LYP/LanL2DZ level. The goal is to compute site-resolved adsorption energies for each molecule on five ZnO models of increasing size, providing quantitative insight into the preferred binding geometries and strengths.

## Approach
The adsorption energies are obtained from DFT geometry optimizations using the B3LYP functional and the LanL2DZ effective‑core‑potential basis set, run with an open‑source quantum chemistry package capable of this combination. The workflow proceeds as follows:

1. Build initial atomic coordinates for five hydrogen‑terminated ZnO models: three nanoclusters (AL‑ZnONC, NLL‑ZnONC, PRL‑ZnONC) and two graphene‑like nanosheets (CNL‑ZnONS, CCL‑ZnONS), each with a well‑defined composition and symmetry (C3h or C2v). Generate also the isolated H2O and NH3 molecules.
2. Optimize the isolated adsorbates and the bare substrates to obtain their reference total energies.
3. For each combination of adsorbate and substrate, generate multiple initial adsorption configurations that cover all symmetry‑distinct sites, orienting the adsorbate with its oxygen (or nitrogen) atom toward a surface Zn atom and its hydrogen atoms toward surface O or H atoms.
4. Optimize the geometry of each adsorption complex at the B3LYP/LanL2DZ level to obtain its total energy.
5. Compute the adsorption energy for each site using the formula:
   ΔE_ads = E_complex − (E_adsorbate + E_bare)
   and convert to kcal/mol.

No basis‑set superposition error (BSSE) correction is required. All calculations can be performed with an open‑source DFT code (e.g., PySCF, ORCA, NWChem). The final outputs are two CSV files that list all distinct site‑resolved adsorption energies.

## Reproduction target
Produce two scored output files in `/app/outputs`:
- `h2o_adsorption_energies.csv`: for every distinct H2O adsorption site on each of the five ZnO models, report the model name, a site label, and the computed adsorption energy in kcal/mol.
- `nh3_adsorption_energies.csv`: the same information for NH3 adsorption sites.

The number of distinct minima per model should reflect the underlying symmetry: one minimum for AL‑ZnONC, three for NLL‑ZnONC, six for PRL‑ZnONC, six for CNL‑ZnONS (H2O) / three for CNL‑ZnONS (NH3), and eleven for CCL‑ZnONS (H2O) / six for CCL‑ZnONS (NH3). The adsorption energies themselves must result from a full B3LYP/LanL2DZ optimization of each complex.

## Assets

- Open-source quantum chemistry package (PySCF, ORCA, or NWChem): https://pyscf.org

## Workflow steps

### Step 1: Construct initial structures
- Role: process
- Action: Generate initial atomic coordinates for the five hydrogen-terminated ZnO models (AL-ZnONC, NLL-ZnONC, PRL-ZnONC, CNL-ZnONS, CCL-ZnONS) using their compositions and assumed symmetries (C3h, C2v, C2v, C3h, C3h), and for the isolated H2O and NH3 molecules.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Optimize isolated adsorbates
- Role: process
- Action: Perform DFT geometry optimization of isolated H2O and NH3 at the B3LYP/LanL2DZ level to obtain their total energies.
- Evidence: `/app/outputs/adsorbate_energies.txt`

### Step 3: Optimize bare substrates
- Role: process
- Action: Perform DFT geometry optimization of the five bare hydrogen-terminated ZnO substrates (AL, NLL, PRL, CNL, CCL) at B3LYP/LanL2DZ level to obtain their total energies and optimized geometries.
- Evidence: `/app/outputs/bare_substrate_energies.txt`

### Step 4: Optimize adsorption complexes
- Role: process
- Action: For each combination of adsorbate (H2O, NH3) and substrate, generate multiple initial adsorption configurations covering all symmetry-distinct sites by orienting the adsorbate with oxygen/nitrogen toward surface Zn and hydrogen toward O/H surface atoms. Perform full geometry optimizations at B3LYP/LanL2DZ to obtain total energies of the complexes.
- Evidence: `/app/outputs/complex_energies.json`

### Step 5: Compute H2O adsorption energies
- Role: scored (load-bearing)
- Action: Compute the adsorption energy ΔE_ads(H2O) for each optimized H2O adsorption site using ΔE_ads = E_complex – (E_H2O + E_bare), and report all site-resolved values in kcal/mol.
- Output file: `/app/outputs/h2o_adsorption_energies.csv`
- Format: csv
- Contract: model (string), site_label (string), delta_E_ads_kcal_mol (float)
- Scoring: scored by hidden verifier

### Step 6: Compute NH3 adsorption energies
- Role: scored (load-bearing)
- Action: Compute the adsorption energy ΔE_ads(NH3) for each optimized NH3 adsorption site using ΔE_ads = E_complex – (E_NH3 + E_bare), and report all site-resolved values in kcal/mol.
- Output file: `/app/outputs/nh3_adsorption_energies.csv`
- Format: csv
- Contract: model (string), site_label (string), delta_E_ads_kcal_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/h2o_adsorption_energies.csv`
- `/app/outputs/nh3_adsorption_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### h2o_adsorption_energies.csv
- path: `/app/outputs/h2o_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of adsorption energies for each distinct H2O adsorption site on each ZnO model.
- schema:
  - `type`: table
  - `required_columns`: `model`, `site_label`, `delta_E_ads_kcal_mol`
  - `units`:
    - `delta_E_ads_kcal_mol`: kcal/mol

### nh3_adsorption_energies.csv
- path: `/app/outputs/nh3_adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of adsorption energies for each distinct NH3 adsorption site on each ZnO model.
- schema:
  - `type`: table
  - `required_columns`: `model`, `site_label`, `delta_E_ads_kcal_mol`
  - `units`:
    - `delta_E_ads_kcal_mol`: kcal/mol

Notes: The verifier compares each reported adsorption energy against the paper's values with tolerances, and also checks that the number of minima per model matches the expected counts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "h2o_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "site_label",
          "delta_E_ads_kcal_mol"
        ],
        "units": {
          "delta_E_ads_kcal_mol": "kcal/mol"
        }
      },
      "description": "Table of adsorption energies for each distinct H2O adsorption site on each ZnO model."
    },
    {
      "file": "nh3_adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "site_label",
          "delta_E_ads_kcal_mol"
        ],
        "units": {
          "delta_E_ads_kcal_mol": "kcal/mol"
        }
      },
      "description": "Table of adsorption energies for each distinct NH3 adsorption site on each ZnO model."
    }
  ],
  "notes": "The verifier compares each reported adsorption energy against the paper's values with tolerances, and also checks that the number of minima per model matches the expected counts."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently inspects the two CSV files. The verifier checks that the reported files exist, have the correct columns, and contain the expected number of adsorption sites for each model. It then compares each reported adsorption energy to a hidden reference dataset compiled from published theoretical values at the same level of theory. A numerical tolerance is applied: the strongest (most negative) adsorption energy on a given model must fall within a stricter margin, while all other minima may fall within a wider tolerance. The final reward is computed as the fraction of values that lie within the accepted tolerances. The verifier may also internally check that the site-resolved energies are internally consistent with the expected ordering of minima. No credit is given for simply reporting the paper’s numbers without genuine DFT calculations; the verifier cross‑checks the supplied energies against its hidden reference, and only values that fall within the tolerance contribute to the score.
