# Grain boundary energy prediction via virtual screening and SVR

## Problem background
Grain boundaries are the interfaces between two crystal grains of different orientation and can dramatically alter a material's mechanical, transport, and chemical properties. Determining the thermodynamically stable atomic structure and its energy requires exploring the three‑dimensional rigid‑body translation of one grain relative to the other, which generates a large combinatorial set of candidate configurations. For [001] symmetric tilt coincidence‑site‑lattice (CSL) boundaries in face‑centered cubic copper, up to ~1 000 000 configurations may need to be atomistically relaxed, making exhaustive search computationally prohibitive. This reproduction task implements a virtual screening method that trains a machine‑learning model on a few boundaries and uses it to predict the most promising translation state for new boundaries before performing a single relaxation.

## Approach
The method builds a regression model that predicts the grain‑boundary energy directly from 83 geometrical descriptors computed on the unrelaxed initial configurations (rigid‑body translations). The workflow is: (i) For four training CSL boundaries, perform full lattice‑statics relaxations for all rigid‑body translations using the Cleri‑Rosato embedded‑atom method (EAM) potential for Cu, and record the grain‑boundary energy of each. (ii) From these training data, select the 800 configurations with the lowest energies, compute the 83 geometrical descriptors (such as bond‑length statistics and local atomic density) on the corresponding initial configurations, and standardize the descriptors to zero mean and unit variance. (iii) Train an ε‑support vector regression (ε‑SVR) model with a Gaussian (RBF) kernel using these standardized descriptors as input and the computed grain‑boundary energies as the target. (iv) For each of the 13 test boundaries, generate all translation‑grid configurations, compute and standardize their descriptors using the same scaling, apply the trained SVR to predict energies, and identify the configuration with the minimum predicted energy. (v) Perform a single lattice‑statics relaxation on that selected configuration to obtain the accurate final grain‑boundary energy. The open‑source lattice‑statics code GULP or LAMMPS and the scikit‑learn library are used throughout.

## Reproduction target
Generate the final predicted grain‑boundary energies (in J/m²) for the following 13 test [001] symmetric tilt CSL grain boundaries of copper: Σ13[001]/(230), Σ25[001]/(430), Σ25[001]/(710), Σ29[001]/(520), Σ29[001]/(730), Σ37[001]/(610), Σ37[001]/(750), Σ41[001]/(910), Σ41[001]/(540), Σ53[001]/(720), Σ53[001]/(950), Σ61[001]/(11 1 0), Σ125[001]/(11 2 0). Produce a CSV file `/app/outputs/predicted_energies.csv` with columns: `boundary_name`, `misorientation_angle_deg`, and `predicted_energy_Jm2`. Each row corresponds to one test boundary, after virtual screening and a single relaxation.

## Assets

- Cleri-Rosato embedded-atom method potential for Cu: https://www.ctcms.nist.gov/potentials/
- GULP or LAMMPS
- scikit-learn: scikit-learn

## Workflow steps

### Step 1: Generate all-candidate training data for four grain boundaries
- Role: process
- Action: For each of the four training boundaries Σ5[001]/(210), Σ5[001]/(310), Σ17[001]/(410), Σ17[001]/(350): construct periodic CSL supercells, generate all rigid-body translation candidates (step size 0.1 Å in x and z, 0.1 Å steps in y from 1.0 to 1.5 Å), perform lattice statics relaxation using the Cleri-Rosato EAM potential (fixed far atoms, fixed volume), and compute grain-boundary energy for each candidate.
- Evidence: `/app/outputs/training_energies_raw.csv`

### Step 2: Select training subset and compute standardized descriptors
- Role: process
- Action: From the computed training data, select 800 configurations (the most stable and metastable, i.e., the 800 configurations with the lowest grain-boundary energies). For each selected initial (unrelaxed) configuration, compute the 83 geometrical descriptors (minimum/maximum bond lengths, atomic density, derived nonlinear combinations, as listed in the paper's supplementary information). Standardize all descriptors to zero mean and unit variance (store scaling parameters).
- Evidence: `/app/outputs/training_features_standardized.npy`

### Step 3: Train ε‑SVR predictor
- Role: process
- Action: Using the standardized descriptor vectors and the corresponding grain-boundary energies of the selected 800 points, train an ε‑SVR with a Gaussian (RBF) kernel. Use the reported optimal hyperparameters: margin ε = 0.01, penalty C = 1000, kernel coefficient γ = 10⁻⁴. Save the trained model.
- Evidence: `/app/outputs/svr_model.pkl`

### Step 4: Virtual screening of 13 test grain boundaries
- Role: process
- Action: For each of the 13 test [001] symmetric tilt CSL boundaries (Σ13/(230), Σ25/(430), Σ25/(710), Σ29/(520), Σ29/(730), Σ37/(610), Σ37/(750), Σ41/(910), Σ41/(540), Σ53/(720), Σ53/(950), Σ61/(11 1 0), Σ125/(11 2 0)): generate all initial configurations with the same translation grid, compute descriptors (using the same standardization parameters), apply the trained SVR to predict the energy of each configuration, and select the configuration with the minimum predicted energy.
- Evidence: `/app/outputs/selected_candidates.json`

### Step 5: Single relaxation for selected candidates and report final energies
- Role: scored (load-bearing)
- Action: For each test boundary, take the configuration selected in step 04 and perform a single lattice statics relaxation with the same EAM potential to obtain the accurate grain-boundary energy. Collect the results and write the final predicted energies.
- Output file: `/app/outputs/predicted_energies.csv`
- Format: csv
- Contract: CSV with columns: boundary_name (string, e.g., 'Sigma13/(230)'), misorientation_angle_deg (float), predicted_energy_Jm2 (float). One row per test boundary.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_energies.csv
- path: `/app/outputs/predicted_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Grain-boundary energies for the 13 test boundaries, obtained after virtual screening and a single relaxation. The checker compares these values to hidden reference energies from the paper and performs a structural audit on the energy vs misorientation curve (convex shape and cusps at characteristic angles).
- schema:
  - `type`: table
  - `required_columns`: `boundary_name`, `misorientation_angle_deg`, `predicted_energy_Jm2`
  - `units`:
    - `predicted_energy_Jm2`: J/m²

Notes: The checker also verifies that the reported energies produce a convex profile with cusps at misorientation angles 16.26°, 28.07°, 36.87°, 53.13°, 67.38° within ±1°, but these structural constraints are encoded in the scoring logic and do not require an additional output file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary_name",
          "misorientation_angle_deg",
          "predicted_energy_Jm2"
        ],
        "units": {
          "predicted_energy_Jm2": "J/m²"
        }
      },
      "description": "Grain-boundary energies for the 13 test boundaries, obtained after virtual screening and a single relaxation. The checker compares these values to hidden reference energies from the paper and performs a structural audit on the energy vs misorientation curve (convex shape and cusps at characteristic angles)."
    }
  ],
  "notes": "The checker also verifies that the reported energies produce a convex profile with cusps at misorientation angles 16.26°, 28.07°, 36.87°, 53.13°, 67.38° within ±1°, but these structural constraints are encoded in the scoring logic and do not require an additional output file."
}
```

## How you are scored
A hidden verifier checks your `predicted_energies.csv` against reference grain‑boundary energies (derived from the original paper) with a tolerance that accounts for implementation differences. It also performs a structural audit on the reported energy–misorientation curve: it verifies that the curve is convex with a maximum near 45° and that local minima (cusps) appear at the expected misorientation angles. The verifier combines a result‑level comparison and the structural check into a single reward between 0 and 1. You do not need to match a specific exact value; the scoring rewards energies that fall within a physically reasonable range while satisfying the structural trends.
