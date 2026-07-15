# Structural Descriptor Model for OH Adsorption Free Energy on Doped Graphene via DFT

## Problem background
The adsorption free energy of OH (ΔG_OH) on carbon sites is a key descriptor for the oxygen reduction reaction (ORR) activity of graphene-based catalysts. Substitutional doping with nitrogen or boron alters the electronic structure and changes the binding strength of ORR intermediates. A structural descriptor based solely on the number of dopant atoms in the ortho, para, and meta positions relative to an active site could enable rapid prediction of ΔG_OH, bypassing costly DFT calculations for every candidate configuration.

## Approach
We use plane-wave density functional theory (DFT) with the PBE exchange‑correlation functional to compute ΔG_OH for a series of doped graphene supercells containing different configurations of nitrogen and boron dopants. From these DFT results we fit a linear model that expresses ΔG_OH as a linear combination of the numbers of ortho, para, and meta dopants relative to the adsorbing carbon atom. The model is validated against independent DFT calculations on multi‑dopant test configurations that were not used in the fitting. Finally, the nitrogen model is used to identify a candidate optimal site, whose full ORR free‑energy profile is obtained via further DFT calculations to extract the overpotential, onset potential, and potential‑limiting step.

## Reproduction target
Construct periodic 5×5 graphene supercell models (50 carbon atoms) with the following doping configurations: one N (1N), two N (2N), three N (3N); one B (1B), two B (2B), three B (3B); and at least two multi‑dopant test supercells (one with three N, one with three B) arranged to provide a variety of ortho/meta/para counts. For every inequivalent carbon active site in each configuration, compute ΔG_OH by performing DFT geometry relaxations and total‑energy calculations (Quantum ESPRESSO, PBE, applicable free‑energy corrections) and record the structural counts (n_O, n_P, n_M). Fit the linear models ΔG_OH = intercept + c_O*n_O + c_P*n_P + c_M*n_M separately for nitrogen and boron using only the single‑dopant configurations, and save the fitted coefficients. Validate each model by comparing the DFT‑computed ΔG_OH on the corresponding multi‑dopant test configurations against the model‑predicted ΔG_OH, and report R². Use the nitrogen model to identify the site with n_P=3, n_O=0, n_M=0 (the 3‑Para site) and compute its full ORR free‑energy diagram (OOH, O, OH, H₂O) to obtain the overpotential, onset potential, and potential‑limiting step.

## Assets

- Quantum ESPRESSO (PWscf): https://www.quantum-espresso.org/download
- PBE ultrasoft pseudopotentials: http://www.quantum-espresso.org/pseudopotentials
- Standard ORR free-energy correction scheme
- Graphene supercell generation tools

## Workflow steps

### Step 1: Construct doped graphene supercell models
- Role: process
- Action: Generate atomic coordinates for a 5×5 graphene supercell (50 carbon atoms) and create substitutional doping configurations for N and B according to standard doping nomenclature (1N, 2N, 3N; 1B, 2B, 3B; plus multi-dopant configurations with three dopants each for validation). For each configuration, identify all inequivalent carbon active sites and label them. Also construct the specific 3-Para site supercell (three N atoms each in para position to a central carbon) needed for the final overpotential calculation.
- Evidence: `/app/outputs/structures.log`

### Step 2: Perform DFT total‑energy calculations and derive ΔG_OH
- Role: process
- Action: For each supercell from step s1, run Quantum ESPRESSO (PWscf) using the PBE functional, ultrasoft pseudopotentials, kinetic energy cutoff 30 Ry (density cutoff 240 Ry), 5×5×1 k-point mesh, Marzari–Vanderbilt smearing. Perform geometry relaxations for the clean slab and for every OH adsorbate configuration on each inequivalent carbon site. Compute total energies. Apply the standard ORR free‑energy corrections (computational hydrogen electrode) to obtain ΔG_OH for every active site. Additionally, for the 3‑Para site, compute total energies of all ORR intermediates (OOH, O, OH) and gas‑phase references (H₂, H₂O) required to build the ORR free‑energy diagram.
- Evidence: `/app/outputs/dft_energies.txt`

### Step 3: Fit structural predictive models for N‑ and B‑doped graphene
- Role: scored
- Action: From the ΔG_OH values computed for the single‑dopant configurations (1N, 2N, 3N; 1B, 2B, 3B) and the structural counts (n_O, n_P, n_M) of each site, perform linear regression ΔG_OH = intercept + a_O * n_O + a_P * n_P + a_M * n_M separately for N and B. Save the fitted coefficients.
- Output file: `/app/outputs/step_01_fitted_models.json`
- Format: json
- Contract: JSON object with keys 'N' and 'B', each containing 'intercept' (float), 'c_O' (float), 'c_P' (float), 'c_M' (float) in eV units.
- Scoring: scored by hidden verifier

### Step 4: Validate nitrogen structural model
- Role: scored
- Action: For all inequivalent carbon sites in the multi‑dopant nitrogen test configurations (supercells with three N dopants arranged to give various ortho/meta/para combinations), count n_O, n_P, n_M. Compute ΔG_OH_generated from the fitted N model. Record side‑by‑side with the DFT‑computed ΔG_OH (from step s2).
- Output file: `/app/outputs/step_02_validation_N.csv`
- Format: csv
- Contract: CSV with columns: site_name (str), n_O (int), n_P (int), n_M (int), delta_G_OH_DFT (float, eV), delta_G_OH_generated (float, eV).
- Scoring: scored by hidden verifier

### Step 5: Validate boron structural model
- Role: scored
- Action: Analogous to step s4, but for the boron multi‑dopant test configurations.
- Output file: `/app/outputs/step_03_validation_B.csv`
- Format: csv
- Contract: CSV with columns: site_name (str), n_O (int), n_P (int), n_M (int), delta_G_OH_DFT (float, eV), delta_G_OH_generated (float, eV).
- Scoring: scored by hidden verifier

### Step 6: Compute ORR overpotential for the 3‑Para optimal site
- Role: scored (load-bearing)
- Action: From the DFT total energies computed for the 3‑Para site and its ORR intermediates (step s2), apply the same free‑energy corrections to construct the ORR free‑energy diagram at zero potential. Determine the largest free‑energy uphill step to obtain the overpotential, the corresponding onset potential, and identify the potential‑limiting step.
- Output file: `/app/outputs/step_04_overpotential_3Para.json`
- Format: json
- Contract: JSON object with keys: overpotential_V (float), onset_potential_V (float), limiting_step (string, e.g., 'OOH formation'), limiting_step_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fitted_models.json`
- `/app/outputs/step_02_validation_N.csv`
- `/app/outputs/step_03_validation_B.csv`
- `/app/outputs/step_04_overpotential_3Para.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fitted_models.json
- path: `/app/outputs/step_01_fitted_models.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted coefficients of the linear structural descriptor models (ΔG_OH vs. n_O, n_P, n_M) for N‑ and B‑doped graphene.
- schema:
  - `type`: object
  - `required`:
    - `N`:
      - `intercept`: float (eV)
      - `c_O`: float (eV)
      - `c_P`: float (eV)
      - `c_M`: float (eV)
    - `B`:
      - `intercept`: float (eV)
      - `c_O`: float (eV)
      - `c_P`: float (eV)
      - `c_M`: float (eV)

### step_02_validation_N.csv
- path: `/app/outputs/step_02_validation_N.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Validation set for the nitrogen structural model: per‑site structural counts, DFT‑computed ΔG_OH, and model‑predicted ΔG_OH. Used to recompute the goodness‑of‑fit R².
- schema:
  - `type`: table
  - `required_columns`: `site_name`, `n_O`, `n_P`, `n_M`, `delta_G_OH_DFT`, `delta_G_OH_generated`
  - `units`:
    - `delta_G_OH_DFT`: eV
    - `delta_G_OH_generated`: eV

### step_03_validation_B.csv
- path: `/app/outputs/step_03_validation_B.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Validation set for the boron structural model: per‑site structural counts, DFT‑computed ΔG_OH, and model‑predicted ΔG_OH. Used to recompute the goodness‑of‑fit R².
- schema:
  - `type`: table
  - `required_columns`: `site_name`, `n_O`, `n_P`, `n_M`, `delta_G_OH_DFT`, `delta_G_OH_generated`
  - `units`:
    - `delta_G_OH_DFT`: eV
    - `delta_G_OH_generated`: eV

### step_04_overpotential_3Para.json
- path: `/app/outputs/step_04_overpotential_3Para.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: ORR overpotential, onset potential, potential‑limiting step, and its free‑energy cost for the 3‑Para optimal site identified by the nitrogen structural model.
- schema:
  - `type`: object
  - `required`:
    - `overpotential_V`: float (V)
    - `onset_potential_V`: float (V)
    - `limiting_step`: str
    - `limiting_step_energy_eV`: float (eV)

Notes: All scored outputs rely on DFT total energies from process steps s1 and s2. The verification strategy is T0 (result‑level compare) coupled with metric recomputation: the checker will recompute R² from the validation CSVs and compare the overpotential/onset potential/limiting step against hidden gold values from the paper, with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fitted_models.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "N": {
            "intercept": "float (eV)",
            "c_O": "float (eV)",
            "c_P": "float (eV)",
            "c_M": "float (eV)"
          },
          "B": {
            "intercept": "float (eV)",
            "c_O": "float (eV)",
            "c_P": "float (eV)",
            "c_M": "float (eV)"
          }
        }
      },
      "description": "Fitted coefficients of the linear structural descriptor models (ΔG_OH vs. n_O, n_P, n_M) for N‑ and B‑doped graphene."
    },
    {
      "file": "step_02_validation_N.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "site_name",
          "n_O",
          "n_P",
          "n_M",
          "delta_G_OH_DFT",
          "delta_G_OH_generated"
        ],
        "units": {
          "delta_G_OH_DFT": "eV",
          "delta_G_OH_generated": "eV"
        }
      },
      "description": "Validation set for the nitrogen structural model: per‑site structural counts, DFT‑computed ΔG_OH, and model‑predicted ΔG_OH. Used to recompute the goodness‑of‑fit R²."
    },
    {
      "file": "step_03_validation_B.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "site_name",
          "n_O",
          "n_P",
          "n_M",
          "delta_G_OH_DFT",
          "delta_G_OH_generated"
        ],
        "units": {
          "delta_G_OH_DFT": "eV",
          "delta_G_OH_generated": "eV"
        }
      },
      "description": "Validation set for the boron structural model: per‑site structural counts, DFT‑computed ΔG_OH, and model‑predicted ΔG_OH. Used to recompute the goodness‑of‑fit R²."
    },
    {
      "file": "step_04_overpotential_3Para.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "overpotential_V": "float (V)",
          "onset_potential_V": "float (V)",
          "limiting_step": "str",
          "limiting_step_energy_eV": "float (eV)"
        }
      },
      "description": "ORR overpotential, onset potential, potential‑limiting step, and its free‑energy cost for the 3‑Para optimal site identified by the nitrogen structural model."
    }
  ],
  "notes": "All scored outputs rely on DFT total energies from process steps s1 and s2. The verification strategy is T0 (result‑level compare) coupled with metric recomputation: the checker will recompute R² from the validation CSVs and compare the overpotential/onset potential/limiting step against hidden gold values from the paper, with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow artifact. The fitted model coefficients are validated by recomputing the R² between your generated ΔG_OH values and the hidden DFT reference for the test configurations. The computed overpotential and onset potential are compared against hidden reference values with predetermined tolerances that account for numerical and method differences; the limiting‑step label is compared for an exact match. The final reward is a weighted sum of per‑step scores. Simply reporting expected numbers without performing the required DFT calculations and model fitting will yield a low score.
