# Bayesian Monte Carlo Optimization of Polarizable Force Field Parameters for Alkali Halides

## Problem background
Accurate force fields that describe interatomic interactions are essential for molecular dynamics simulations of materials. For alkali halides, previous models often fail to simultaneously reproduce gas-phase, liquid-phase, and solid-phase properties with good accuracy, limiting their phase transferability. This work develops a new polarizable force field based on a modified Buckingham (WBK) potential with Gaussian charge distributions and a core–shell polarizability model. The parameters are optimized against a composite set of experimental gas-phase ion-pair observables and crystal pressure/density constraints. The goal is to derive a single consistent set of ion-level parameters and then use these to compute gas-phase ion-pair properties, room-temperature solid densities, and liquid densities at the melting point. The task is to reproduce that parameterization and property prediction pipeline.

## Approach
The force field model combines Coulomb interactions described by Gaussian charge distributions with a core–shell polarizability scheme. The core and shell charges and the Gaussian width β are first calibrated to reproduce experimental dipole moments of alkali halide ion pairs by minimizing a χ²_dipole function using a Bayesian Monte Carlo (or equivalent global optimization) loop. At each trial the shell positions are obtained by local minimization of the Coulomb plus polarization energy. Fixed ion polarizabilities from Molina et al. are used. In the second stage, the van der Waals parameters (σ, ε, γ) of the WBK potential are optimized for the eight ions (Li⁺, Na⁺, K⁺, Cs⁺, F⁻, Cl⁻, Br⁻, I⁻) by simultaneously matching ion-pair dissociation energies, equilibrium distances, harmonic force constants (from vibrational frequencies), and crystal pressure/density constraints for 20 salts, employing the Hogervorst combining rules to obtain cross-interactions. After the parameters are determined, the model is tested by computing gas-phase ion-pair properties (interionic distance, dissociation energy, vibrational frequency, dipole moment) via energy minimizations or single‑point calculations in GROMACS, running NPT simulations at 298 K to obtain solid-state densities, and running NVT (or NPT) simulations at the experimental melting points to obtain liquid densities for a representative subset of salts.

## Reproduction target
Implement the Bayesian Monte Carlo optimization workflow to derive the WBK force field parameters (σ, ε, γ) for Li⁺, Na⁺, K⁺, Cs⁺, F⁻, Cl⁻, Br⁻, I⁻ using the core–shell Gaussian-charge polarizable model. Then, using the optimized parameters, compute:
- gas-phase properties (rₑ, Dₑ, ν̃, μ) for all 20 alkali halide ion pairs;
- solid-state densities at 298 K and 1 bar for the same 20 salts;
- liquid densities at the experimental melting point for the subset LiF, LiCl, NaCl, KF, KCl, KBr, RbCl, RbBr, CsF, CsCl.
The results must be written to the specified output files (`force_field_parameters.json`, `gas_properties.csv`, `solid_density_298K.csv`, `liquid_density_Tm.csv`) following the schemas given in the output contract.

## Assets

- Experimental gas-phase data (rₑ, Dₑ, ν̃, μ) for 20 alkali halides: http://physics.nist.gov/cgi-bin/MolSpec/diperiodic.pl
- Experimental solid-state lattice constants / densities for 20 alkali halides at 298 K: ISBN 3-540-41090-2
- Experimental liquid densities at melting point (Tm) for 10 alkali halides: 10.1007/s10973-005-6969-0
- Polarizability values for alkali/halide ions (Molina et al. set): 10.1063/1.3527893
- GROMACS MD simulation package (2018 or later): http://www.gromacs.org
- SciPy (Python library) for L-BFGS-B and Bayesian Monte Carlo algorithms: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Bayesian Monte Carlo optimization of Coulomb parameters
- Role: process
- Action: Implement the core–shell Gaussian-charge polarizable model. Using fixed polarizabilities from Molina et al. and experimental dipole moments as targets, perform Bayesian Monte Carlo (or equivalent optimizer) to determine core/shell charge partitioning and Gaussian width β for Li⁺, Na⁺, K⁺, Cs⁺, F⁻, Cl⁻, Br⁻, I⁻. At each trial the shell positions are found by minimizing the sum of Coulomb and polarization energies with L-BFGS-B. The optimization minimizes χ²_dipole.
- Evidence: `/app/outputs/coulomb_optimization.log`

### Step 2: Bayesian Monte Carlo optimization of WBK van der Waals parameters
- Role: process
- Action: Using the Coulomb parameters from the previous step, perform Bayesian Monte Carlo optimization of the WBK van der Waals parameters (σ, ε, γ) for the same set of ions. The composite objective function consists of χ²_IP (ion-pair dissociation energy, equilibrium distance, force constant from vibrational frequency) and χ²_cryst (crystal pressure/density constraints for 20 salts). Include analytical long-range pressure corrections and any required iterative p_offset from preliminary NVT simulations. Use Hogervorst combining rules to obtain cross-interactions.
- Evidence: `/app/outputs/wbk_optimization.log`

### Step 3: Save optimized WBK force field parameters
- Role: scored
- Action: Write the optimized WBK parameter set (σ, ε, γ for each ion) to force_field_parameters.json, using the Hogervorst combining rule specification.
- Output file: `/app/outputs/force_field_parameters.json`
- Format: json
- Contract: JSON object with keys for each cation/anion identifier (e.g., 'Li+', 'F-'), each containing 'sigma' (float, nm), 'epsilon' (float, kJ/mol), 'gamma' (float, dimensionless). Also a key 'combining_rule' with value 'Hogervorst'.
- Scoring: scored by hidden verifier

### Step 4: Compute gas-phase ion-pair properties
- Role: scored (load-bearing)
- Action: Using the optimized WBK force field, perform GROMACS energy minimizations or single-point calculations for all 20 alkali halide ion pairs. Compute interionic distance rₑ, dissociation energy Dₑ = V_tot at rₑ, vibrational frequency via harmonic force constant from the second derivative of V_tot, and dipole moment μ = Σ qᵢ rᵢ. Output the results to gas_properties.csv.
- Output file: `/app/outputs/gas_properties.csv`
- Format: csv
- Contract: CSV with columns: salt (string, e.g., LiF), re_pm (float, in pm), De_kjmol (float, in kJ/mol), nu_cm1 (float, in cm⁻¹), mu_D (float, in Debye). 20 rows total.
- Scoring: scored by hidden verifier

### Step 5: Compute solid-state densities at 298 K
- Role: scored
- Action: With the optimized WBK force field, run GROMACS NPT simulations of the 20 alkali halide crystals (NaCl-type or CsCl-type as appropriate) at 298 K and 1 bar. Determine the equilibrium density for each salt and write the results to solid_density_298K.csv.
- Output file: `/app/outputs/solid_density_298K.csv`
- Format: csv
- Contract: CSV with columns: salt (string), density_kgm3 (float, in kg/m³). 20 rows.
- Scoring: scored by hidden verifier

### Step 6: Compute liquid densities at melting point
- Role: scored
- Action: Using the optimized WBK force field, run GROMACS NVT or NPT simulations of the molten salts at the experimental melting point for the subset of salts (LiF, LiCl, NaCl, KF, KCl, KBr, RbCl, RbBr, CsF, CsCl). Determine the equilibrium liquid density and write the results to liquid_density_Tm.csv.
- Output file: `/app/outputs/liquid_density_Tm.csv`
- Format: csv
- Contract: CSV with columns: salt (string), density_kgm3 (float, in kg/m³). 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_field_parameters.json`
- `/app/outputs/gas_properties.csv`
- `/app/outputs/solid_density_298K.csv`
- `/app/outputs/liquid_density_Tm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_field_parameters.json
- path: `/app/outputs/force_field_parameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Final force field parameters for the WBK potential. Validated for structure and physically plausible ranges.
- schema:
  - `type`: object
  - `required`: `combining_rule`, `Li+`, `Na+`, `K+`, `Cs+`, `F-`, `Cl-`, `Br-`, `I-`
  - `description`: JSON object containing per-ion WBK parameters and the combining rule. Each ion key maps to an object with keys sigma (float, nm), epsilon (float, kJ/mol), gamma (float, dimensionless). combining_rule must be the string 'Hogervorst'.

### gas_properties.csv
- path: `/app/outputs/gas_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed gas-phase ion-pair properties for all 20 alkali halide salts.
- schema:
  - `type`: table
  - `required_columns`: `salt`, `re_pm`, `De_kjmol`, `nu_cm1`, `mu_D`
  - `units`:
    - `re_pm`: pm
    - `De_kjmol`: kJ/mol
    - `nu_cm1`: cm⁻¹
    - `mu_D`: Debye
  - `row_count`: 20

### solid_density_298K.csv
- path: `/app/outputs/solid_density_298K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Room-temperature solid densities for all 20 salts.
- schema:
  - `type`: table
  - `required_columns`: `salt`, `density_kgm3`
  - `units`:
    - `density_kgm3`: kg/m³
  - `row_count`: 20

### liquid_density_Tm.csv
- path: `/app/outputs/liquid_density_Tm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Liquid densities at the melting point for the specified 10 salts.
- schema:
  - `type`: table
  - `required_columns`: `salt`, `density_kgm3`
  - `units`:
    - `density_kgm3`: kg/m³
  - `row_count`: 10

Notes: The force_field_parameters.json step is scored via structural audit to ensure the correct format and physically reasonable parameter ranges. The gas, solid, and liquid property artifacts are scored by computing RMSD/NRMSD against hidden experimental references; meeting or beating the hidden thresholds earns full credit (threshold_or_better policy). All required experimental input data are publicly available from the sources listed in resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_field_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "combining_rule",
          "Li+",
          "Na+",
          "K+",
          "Cs+",
          "F-",
          "Cl-",
          "Br-",
          "I-"
        ],
        "description": "JSON object containing per-ion WBK parameters and the combining rule. Each ion key maps to an object with keys sigma (float, nm), epsilon (float, kJ/mol), gamma (float, dimensionless). combining_rule must be the string 'Hogervorst'."
      },
      "description": "Final force field parameters for the WBK potential. Validated for structure and physically plausible ranges."
    },
    {
      "file": "gas_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "salt",
          "re_pm",
          "De_kjmol",
          "nu_cm1",
          "mu_D"
        ],
        "units": {
          "re_pm": "pm",
          "De_kjmol": "kJ/mol",
          "nu_cm1": "cm⁻¹",
          "mu_D": "Debye"
        },
        "row_count": 20
      },
      "description": "Computed gas-phase ion-pair properties for all 20 alkali halide salts."
    },
    {
      "file": "solid_density_298K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "salt",
          "density_kgm3"
        ],
        "units": {
          "density_kgm3": "kg/m³"
        },
        "row_count": 20
      },
      "description": "Room-temperature solid densities for all 20 salts."
    },
    {
      "file": "liquid_density_Tm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "salt",
          "density_kgm3"
        ],
        "units": {
          "density_kgm3": "kg/m³"
        },
        "row_count": 10
      },
      "description": "Liquid densities at the melting point for the specified 10 salts."
    }
  ],
  "notes": "The force_field_parameters.json step is scored via structural audit to ensure the correct format and physically reasonable parameter ranges. The gas, solid, and liquid property artifacts are scored by computing RMSD/NRMSD against hidden experimental references; meeting or beating the hidden thresholds earns full credit (threshold_or_better policy). All required experimental input data are publicly available from the sources listed in resources."
}
```

## How you are scored
A hidden verifier will independently examine each scored artifact. `force_field_parameters.json` is checked for correct structure and physically reasonable parameter ranges. For `gas_properties.csv`, the verifier computes normalized root‑mean‑square deviations (NRMSD) against hidden experimental reference values for the four gas-phase quantities. For `solid_density_298K.csv` and `liquid_density_Tm.csv`, it computes RMSD against hidden experimental densities. Full credit is awarded for meeting or exceeding a set of hidden thresholds; partial credit is assigned when the error exceeds the threshold. All stage scores are combined by weight into a final overall reward between 0 and 1. Meeting the paper's own reported numbers is not sufficient — the model and the properties must be genuinely re-derived through the prescribed optimization and simulation workflow.
