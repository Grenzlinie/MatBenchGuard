# Uncertainty Propagation in Microkinetic Modeling via Group Additivity

## Problem background
Surface‑catalyzed microkinetic models (MKMs) predict reactor performance (conversion, turnover frequency, activation energy) from thermodynamic and kinetic parameters of all species and reactions. For networks larger than ~C2, computing every intermediate with first‑principles DFT is infeasible, so surrogate methods like group additivity (GA) for thermochemistry and Brønsted–Evans–Polanyi (BEP) relations for barriers are used. These surrogates introduce parametric uncertainty whose correlations among species, and the contribution of entropy, are often neglected. Accurately quantifying this uncertainty and its propagation to MKM predictions is essential for assessing model reliability. This task reproduces a statistical framework that estimates correlated thermodynamic uncertainties from a GA training set and propagates them through the MKM to yield distributions of the reactor quantities of interest.

## Approach
The approach has three stages:

1. **Group additivity fit and covariance**: Using a public DFT‑derived training set (pGrAdd:GRWSurface2018), ordinary least squares (OLS) is performed to obtain group contributions for enthalpy and entropy. The training molecule‑group configuration matrix and the fitted residuals are used to compute the model variance and the hat matrix. From these, the covariance matrix among the 66 groups is constructed, capturing correlations that are then accounted for in the uncertainty propagation.

2. **Correlated perturbation sampling**: For the target ethane oxidative dehydrogenation (ODH) network (45 surface species), the same group definitions are used to build the prediction configuration matrix. The multivariate normal distribution of the predicted species enthalpies and entropies, with covariance proportional to (I + H_P), is sampled to generate 5000 sets of perturbed thermochemistry. Each set respects the correlations estimated from the training data.

3. **Microkinetic simulation and distribution analysis**: For each perturbed set, reaction thermochemistry (ΔH, ΔG) is computed, activation energies are obtained via BEP relations, and lateral‑interaction corrections are applied. The microkinetic model is solved using an open‑source solver (Cantera) over a grid of temperatures (500–1100 K) at a fixed feed ratio (C₂H₆:O₂ = 1:0.5). The raw per‑sample conversion and TOF are recorded. From these raw results, distributions of turnover frequency (log₁₀ scale), apparent activation energy (from Arrhenius slopes), and reaction orders for C₂H₆ and O₂ are extracted; if the distributions are multimodal, Gaussian mixture models are fitted. The aggregated statistics (mean, std, and, where applicable, mixture parameters) are then reported.

## Reproduction target
Implement the complete uncertainty propagation pipeline and apply it to the ethane ODH network. The concrete objectives are:

- Fit the GA group contributions and output the 66×66 covariance matrix for enthalpy and entropy.
- Generate 5000 correlated thermodynamic perturbation sets for the 45 surface species and run a microkinetic simulation for each perturbation over the specified temperature grid and feed ratio, producing a CSV file of raw results (T, feed_ratio, sample_id, conversion, TOF).
- From the raw simulations, compute the distribution of log₁₀(TOF) (mean, std), apparent activation energy (mean, std, in kcal/mol), and reaction orders for C₂H₆ and O₂ (mean, std) and save them as a JSON file. If any distribution is clearly multimodal, optionally provide the parameters of a Gaussian mixture model that describes the components.

The task is self‑contained: all required resources are public (pGrAdd, pMuTT, Cantera, NIST WebBook, and the reaction network from the paper’s Supporting Information). The output artifacts allow a later verifier to recompute the key statistics and assess whether the reproduced distributions are consistent with the expected behavior of the framework.

## Assets

- pGrAdd Python package (with GRWSurface2018 database): https://pypi.org/project/pGrAdd/
- pMuTT Python Multiscale Thermochemistry Toolbox: https://pypi.org/project/pMuTT/
- Cantera open-source microkinetic solver: https://cantera.org
- NIST Chemistry WebBook: https://webbook.nist.gov/chemistry/
- Ethane ODH reaction network from paper Supporting Information: 10.1021/acs.jpcc.1c04754

## Workflow steps

### Step 1: Load training data and define group additivity configuration matrices
- Role: process
- Action: Download and load the pGrAdd:GRWSurface2018 database. Extract the training molecule-group configuration matrix X_T and the thermochemistry vectors Y_T for enthalpy and entropy.
- Evidence: none

### Step 2: Fit GA group contributions and compute covariance matrix
- Role: scored
- Action: Perform ordinary least squares fitting to obtain group contributions for enthalpy and entropy. Compute the model variance and the hat matrix. Compute the GA group covariance matrix (66×66) for both enthalpy and entropy and save as JSON.
- Output file: `/app/outputs/ga_covariance_matrix.json`
- Format: json
- Contract: JSON object with keys 'H_cov' and 'S_cov', each a 2D array of shape (66,66) representing the covariance matrix among the 66 groups for enthalpy and entropy, respectively.
- Scoring: scored by hidden verifier

### Step 3: Prepare prediction species and reaction network for ethane ODH
- Role: process
- Action: Identify the 45 surface species for the ethane ODH network and construct their molecule-group configuration matrix X_P using the same group definition. Load or define the reaction network (list of elementary steps) from the paper's Supporting Information.
- Evidence: none

### Step 4: Sample correlated thermodynamic perturbations
- Role: process
- Action: Using the fitted GA model, compute the prediction hat matrix H_P and construct the multivariate normal distribution for predicted enthalpies and entropies of the 45 surface species. Draw 5000 random samples of zero-mean perturbations and add them to the GA predictions to generate perturbed species thermochemistry. Save the sampled sets as evidence.
- Evidence: `/app/outputs/perturbed_species_thermo.csv`

### Step 5: Run microkinetic model simulations with perturbed parameters
- Role: scored (load-bearing)
- Action: For each of the 5000 perturbed thermochemical sets, compute reaction thermochemistry, activation energies via BEP relations, coverage-dependent lateral interactions, and solve the microkinetic model using an open-source solver (e.g., Cantera). Run over a grid of temperatures (e.g., 500-1100 K, 36 points) at a fixed feed ratio C2H6:O2=1:0.5. Record conversion, TOF, and key QoIs for each sample. Save all raw results as CSV.
- Output file: `/app/outputs/ethane_odh_perturbed_results.csv`
- Format: csv
- Contract: CSV with columns: T (float, temperature in K), feed_ratio (string, e.g., '1:0.5'), sample_id (int), conversion (float), TOF (float, turnover frequency in s^{-1}). Additional columns such as surface coverages may be present but are not required for scoring.
- Scoring: scored by hidden verifier

### Step 6: Compute aggregated QoI statistics
- Role: scored
- Action: From the raw perturbed results, compute distributions of TOF (mean and std of log10(TOF)), apparent activation energy (mean and std, from Arrhenius slope for each sample), and reaction orders for C2H6 and O2 (mean and std). If distributions are multimodal, optionally fit Gaussian mixture models and include the parameters. Save the aggregated statistics as JSON.
- Output file: `/app/outputs/aggregated_qoi_stats.json`
- Format: json
- Contract: JSON object with keys: 'TOF' (object with 'mean_log10' float, 'std_log10' float), 'E_app' (object with 'mean_kcal_per_mol' float, 'std_kcal_per_mol' float), 'reaction_order_C2H6' (object with 'mean' float, 'std' float), 'reaction_order_O2' (object with 'mean' float, 'std' float). If a QoI distribution is multimodal, each key may also contain an optional 'gaussian_mixture' array of objects, each with 'weight', 'mean', 'std'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ga_covariance_matrix.json`
- `/app/outputs/ethane_odh_perturbed_results.csv`
- `/app/outputs/aggregated_qoi_stats.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ga_covariance_matrix.json
- path: `/app/outputs/ga_covariance_matrix.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: GA group covariance matrix (enthalpy and entropy) from OLS fit; the checker recomputes the matrix from the same training set and compares element-wise within tolerance.
- schema:
  - `type`: object
  - `required`:
    - `H_cov`: 2D float array of shape (66,66)
    - `S_cov`: 2D float array of shape (66,66)

### ethane_odh_perturbed_results.csv
- path: `/app/outputs/ethane_odh_perturbed_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw MKM simulation results for 5000 perturbations × temperature grid. The checker recomputes QoI statistics (mean log10(TOF), mean apparent activation energy, mean reaction orders) from these raw data and compares to hidden paper-derived gold values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `feed_ratio`, `sample_id`, `conversion`, `TOF`
  - `units`:
    - `T`: K
    - `conversion`: fraction (0-1)
    - `TOF`: s^{-1}

### aggregated_qoi_stats.json
- path: `/app/outputs/aggregated_qoi_stats.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated statistics derived from the raw MKM results; the checker compares the reported means with its own recomputed values to verify consistency.
- schema:
  - `type`: object
  - `required`:
    - `TOF`: object with mean_log10, std_log10
    - `E_app`: object with mean_kcal_per_mol, std_kcal_per_mol
    - `reaction_order_C2H6`: object with mean, std
    - `reaction_order_O2`: object with mean, std

Notes: All scored artifacts are produced in order. The primary scoring weight is on the raw MKM results (ethane_odh_perturbed_results.csv), from which the checker independently recomputes the headline QoI distributions. The aggregated stats file provides a cross-check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ga_covariance_matrix.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "H_cov": "2D float array of shape (66,66)",
          "S_cov": "2D float array of shape (66,66)"
        }
      },
      "description": "GA group covariance matrix (enthalpy and entropy) from OLS fit; the checker recomputes the matrix from the same training set and compares element-wise within tolerance."
    },
    {
      "file": "ethane_odh_perturbed_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "feed_ratio",
          "sample_id",
          "conversion",
          "TOF"
        ],
        "units": {
          "T": "K",
          "conversion": "fraction (0-1)",
          "TOF": "s^{-1}"
        }
      },
      "description": "Raw MKM simulation results for 5000 perturbations × temperature grid. The checker recomputes QoI statistics (mean log10(TOF), mean apparent activation energy, mean reaction orders) from these raw data and compares to hidden paper-derived gold values."
    },
    {
      "file": "aggregated_qoi_stats.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "TOF": "object with mean_log10, std_log10",
          "E_app": "object with mean_kcal_per_mol, std_kcal_per_mol",
          "reaction_order_C2H6": "object with mean, std",
          "reaction_order_O2": "object with mean, std"
        }
      },
      "description": "Aggregated statistics derived from the raw MKM results; the checker compares the reported means with its own recomputed values to verify consistency."
    }
  ],
  "notes": "All scored artifacts are produced in order. The primary scoring weight is on the raw MKM results (ethane_odh_perturbed_results.csv), from which the checker independently recomputes the headline QoI distributions. The aggregated stats file provides a cross-check."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage’s output artifact. For every scored artifact (the GA covariance matrix, the raw perturbed simulation results, and the aggregated QoI statistics), the verifier recomputes quantities from your raw output or compares them to independently derived reference values. The per‑artifact rewards are then combined into a final reward in [0,1]. Simply reporting numbers without executing the pipeline is insufficient; the verifier checks that the artifacts are self‑consistent and that the derived statistics follow from the raw data according to the prescribed calculation methods. The exact comparison logic and tolerances are hidden, but they are designed to accept legitimate run‑to‑run variation while enforcing that the core computations (OLS fit, multivariate sampling, MKM solving) were performed correctly.
