# Fracture probability comparison of two bracket designs under mixed-mode failure criterion

## Problem background
This work addresses overstress failure of components containing internal flaws. The central idea is to compare design alternatives and select the one with the highest resistance to failure. The proposed method uses a mixed-mode crack‑initiation criterion and Monte Carlo simulation to compute the probability of failure directly from the flaw population, without relying on empirical power-law assumptions. The demonstration case involves two fixed bracket designs (A and B) subjected to the same uniform pressure. The task is to compute the probability of failure for each design, which forms the main experimental finding.

## Approach
The workflow combines finite‑element stress analysis with a Monte Carlo simulation. First, a static linear‑elastic finite‑element analysis is performed for each bracket design to extract the signed principal stresses and the volume of every element. Then, in the Monte Carlo phase, random flaw locations are sampled with probability proportional to element volume. The size of each flaw is drawn from a log‑normal distribution, and a mixed‑mode failure criterion is evaluated using the local principal stresses and the given material fracture toughnesses (mode I and mode II). The fraction of trials in which the flaw initiates failure defines the conditional individual failure probability F_c. The component probability of failure p_flaws is obtained from F_c using a Poisson model. By comparing the two designs, the method identifies the shape with higher failure resistance.

## Reproduction target
Compute the conditional individual probability of failure F_c and the total probability of failure p_flaws for both bracket designs A and B. Use the given geometry and loading (fixed supports, uniform pressure 166.7 N/mm² over a 20 mm × 30 mm area), material fracture toughnesses K_Ic = 25 MPa√m and K_IIc = 21 MPa√m, flaw size distribution (log‑normal with mean of ln(D) = 5 µm and standard deviation 0.5), and flaw number density λ = 2 cm⁻³. The results must clearly differentiate the two designs.

## Assets

- CalculiX ccx: calculix-ccx
- Gmsh: https://gmsh.info
- Python packages (numpy, scipy, meshio): numpy scipy meshio

## Workflow steps

### Step 1: Finite element stress analysis for designs A and B
- Role: process
- Action: Create 3D solid meshes for the two bracket designs according to the provided geometry and boundary conditions (fixed supports, uniform pressure 166.7 N/mm² over a 20 mm × 30 mm area). Use Gmsh for meshing and CalculiX for linear elastic static analysis (material: isotropic elastic constants, e.g., E=70 GPa, ν=0.33). Extract at each element centroid the signed principal stresses σ1 ≥ σ2 ≥ σ3 and the element volume. Save the extracted per-element data to files (e.g., design_A_stresses.csv, design_B_stresses.csv with columns: sigma1, sigma2, sigma3, volume). Produce a summary report fe_analysis_report.json containing mesh size, maximum principal stress, and element count for each design.
- Evidence: `/app/outputs/fe_analysis_report.json`

### Step 2: Monte Carlo simulation and failure probability for Design A
- Role: scored
- Action: Using the per-element stress and volume data for Design A, perform a Monte Carlo simulation with 1,000,000 trials. Each trial: (1) select a random element with probability proportional to its volume; (2) sample a flaw diameter D from a log-normal distribution with mean of ln(D)=5 (µm) and standard deviation 0.5 (convert to half-size a = D/2); (3) evaluate the mixed-mode failure criterion using the closed-form expressions for A_max and boundary values (as given in the paper) with the local principal stresses, fracture toughnesses K_Ic=25 MPa√m, K_IIc=21 MPa√m, and the sampled flaw half-size; (4) if A_max ≥ 1, increment the failure counter. Compute F_c = failures / trials and p_flaws = 1 − exp(−λ V F_c) with λ=2 cm⁻³ and the design volume. Save the results to design_A_MC_results.json containing fields F_c, p_flaws, trials, failures.
- Output file: `/app/outputs/design_A_MC_results.json`
- Format: json
- Contract: JSON object with numeric fields: F_c (float), p_flaws (float), trials (integer), failures (integer).
- Scoring: scored by hidden verifier

### Step 3: Monte Carlo simulation and failure probability for Design B
- Role: scored
- Action: Same procedure as for Design A, but using the per-element stress and volume data for Design B. Save the results to design_B_MC_results.json containing fields F_c, p_flaws, trials, failures.
- Output file: `/app/outputs/design_B_MC_results.json`
- Format: json
- Contract: JSON object with numeric fields: F_c (float), p_flaws (float), trials (integer), failures (integer).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/design_A_MC_results.json`
- `/app/outputs/design_B_MC_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### design_A_MC_results.json
- path: `/app/outputs/design_A_MC_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Monte Carlo simulation results for Design A: conditional individual probability of failure (F_c), total probability of failure (p_flaws), number of trials, and count of failures.
- schema:
  - `type`: object
  - `required`:
    - `F_c`: float
    - `p_flaws`: float
    - `trials`: integer
    - `failures`: integer

### design_B_MC_results.json
- path: `/app/outputs/design_B_MC_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Monte Carlo simulation results for Design B: conditional individual probability of failure (F_c), total probability of failure (p_flaws), number of trials, and count of failures.
- schema:
  - `type`: object
  - `required`:
    - `F_c`: float
    - `p_flaws`: float
    - `trials`: integer
    - `failures`: integer

Notes: Both outputs are derived from the same material properties and flaw distribution; the checker will compare the reported F_c and p_flaws values against the paper-reported gold values (F_cA=0.0032, p_flawsA=0.27, F_cB=0.000223, p_flawsB=0.019) using tolerant thresholds that accept better-than-paper results. Additionally, the trend p_flaws_B < p_flaws_A will be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "design_A_MC_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "F_c": "float",
          "p_flaws": "float",
          "trials": "integer",
          "failures": "integer"
        }
      },
      "description": "Monte Carlo simulation results for Design A: conditional individual probability of failure (F_c), total probability of failure (p_flaws), number of trials, and count of failures."
    },
    {
      "file": "design_B_MC_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "F_c": "float",
          "p_flaws": "float",
          "trials": "integer",
          "failures": "integer"
        }
      },
      "description": "Monte Carlo simulation results for Design B: conditional individual probability of failure (F_c), total probability of failure (p_flaws), number of trials, and count of failures."
    }
  ],
  "notes": "Both outputs are derived from the same material properties and flaw distribution; the checker will compare the reported F_c and p_flaws values against the paper-reported gold values (F_cA=0.0032, p_flawsA=0.27, F_cB=0.000223, p_flawsB=0.019) using tolerant thresholds that accept better-than-paper results. Additionally, the trend p_flaws_B < p_flaws_A will be verified."
}
```

## How you are scored
A hidden verifier independently inspects the scored output files `design_A_MC_results.json` and `design_B_MC_results.json`. For each design, the verifier checks that all required fields are present and valid, then compares the reported F_c and p_flaws against reference values (the paper’s reported results). The comparison uses tolerance thresholds that account for the stochastic nature of Monte Carlo simulation and implementation differences. The final reward is a weighted combination of the scores from both designs. Submitting hard‑coded numbers without executing the full pipeline is not sufficient to receive a high reward.
