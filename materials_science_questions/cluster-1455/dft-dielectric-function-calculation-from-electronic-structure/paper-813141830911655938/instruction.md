# Self-consistent dielectric-dependent hybrid functional for three crystalline solids

## Problem background
Density functional theory (DFT) with hybrid functionals is widely used for predicting band gaps and dielectric properties of semiconductors and insulators, but choosing the fraction of exact exchange (the mixing parameter α) remains a challenge. For nonmetallic condensed systems, the effective screening of the Coulomb interaction is described by the inverse of the static electronic dielectric constant ε∞. This suggests that an optimal choice for α in a full-range hybrid functional may be α = 1/ε∞, where ε∞ itself depends on the electronic structure governed by α. Therefore a self-consistent scheme in which α and ε∞ are determined iteratively can lead to a nonempirical, dielectric-dependent hybrid functional with improved accuracy for band gaps and static dielectric constants.

## Approach
In this task you will implement a self-consistent hybrid (sc-hybrid) functional scheme. The core idea is to iterate between a hybrid DFT calculation with a given α and the evaluation of the static electronic dielectric constant ε∞ from the resulting electronic structure, updating α = 1/ε∞ until the dielectric constant stabilizes. Specifically, for each considered crystalline solid, you will start with an initial α (e.g., 0 or 0.25), perform a hybrid density functional self-consistent field (SCF) calculation using the PBE exchange-correlation functional with that fraction of exact exchange, and compute ε∞ using a method that captures the full electronic response (e.g., a finite-field/Berry-phase approach). You will then set α to the inverse of the computed ε∞ and repeat the hybrid SCF and ε∞ evaluation until the change in ε∞ between consecutive outer iterations falls below 0.01. After convergence, you will extract the Kohn-Sham band gap (difference between the conduction-band minimum and the valence-band maximum) from the final SCF cycle. This protocol must be carried out for three nonmetallic solids: silicon (diamond structure, experimental lattice constant a = 5.43 Å), carbon (diamond structure, a = 3.57 Å), and MgO (rock salt structure, a = 4.21 Å). The computational engine will be Quantum ESPRESSO, which provides the necessary hybrid functional and finite-field capabilities, combined with standard pseudopotentials (e.g., from the SSSP or PSLibrary).

## Reproduction target
For the three materials given above, you must execute the self-consistent hybrid procedure and collect the evolution of the static dielectric constant, the final converged values, and the resulting band gaps. Your submission must be a single output file, `/app/outputs/sc_hybrid_results.json`, containing a JSON array of three objects — one per material — with the following keys:
- `material`: string identifying the solid (`"Si"`, `"C"`, `"MgO"`)
- `initial_alpha`: the starting α value you used
- `epsilon_inf_iterations`: an array of the computed ε∞ values from each outer iteration, in order from the first to the last (must contain at least two entries, with the difference between the last two less than 0.01)
- `converged_epsilon_inf`: the final ε∞ value (must equal the last element of `epsilon_inf_iterations`)
- `converged_alpha`: the self-consistent α value, which should equal 1/converged_epsilon_inf (within a small numerical tolerance)
- `band_gap`: the Kohn-Sham band gap in eV from the final SCF.
The objective is to demonstrate that the iterative scheme converges and to produce physically reasonable dielectric constants and band gaps for these test materials.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP or PSLibrary): https://www.quantum-espresso.org/pseudopotentials
- Experimental lattice constants

## Workflow steps

### Step 1: Self-consistent hybrid functional loop and data collection
- Role: scored (load-bearing)
- Action: For each material (Si, C, MgO) at the given experimental lattice constant, perform the sc-hybrid scheme: start with an initial mixing parameter α (0 or 0.25). Run a hybrid DFT self-consistent field (SCF) calculation with that fraction of exact exchange. Compute the macroscopic static electronic dielectric constant ε∞ using a finite-field approach that captures the full electronic response (e.g., Berry-phase method). Update α = 1/ε∞. Repeat the hybrid SCF and ε∞ evaluation until the change in ε∞ between consecutive outer iterations is less than 0.01. After convergence, extract the Kohn-Sham band gap (difference between conduction-band minimum and valence-band maximum) from the final SCF. Record for each material: initial α, the sequence of ε∞ values from all outer iterations, the converged ε∞, the converged α (= 1/ε∞), and the band gap in eV.
- Output file: `/app/outputs/sc_hybrid_results.json`
- Format: json
- Contract: A JSON array of three objects, one per material. Each object has keys: material (string, one of 'Si', 'C', 'MgO'), initial_alpha (number), epsilon_inf_iterations (array of numbers, length >= 2, in order from first to last outer iteration), converged_epsilon_inf (number, must equal the last element of epsilon_inf_iterations), converged_alpha (number, equal to 1/converged_epsilon_inf), band_gap (number, in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sc_hybrid_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sc_hybrid_results.json
- path: `/app/outputs/sc_hybrid_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Self-consistent hybrid functional convergence data and final quantities for Si, C, and MgO. The hidden checker verifies structural consistency (|Δε∞| < 0.01, α ≈ 1/ε∞) and compares converged_epsilon_inf and band_gap against the paper's reported sc-hybrid values within tolerances.
- schema:
  - `type`: array
  - `items`:
    - `material`: string
    - `initial_alpha`: number
    - `epsilon_inf_iterations`: array of numbers
    - `converged_epsilon_inf`: number
    - `converged_alpha`: number
    - `band_gap`: number (eV)

Notes: The agent must use Quantum ESPRESSO with a finite-field (Berry-phase) method for ε∞, which automatically includes local-field effects. The sc-hybrid loop requires several outer iterations per material, each involving hybrid SCF calculations. The hidden checker performs a result-level comparison (T0) using the paper's sc-hybrid results as reference; tolerances are set to absorb legitimate implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sc_hybrid_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "material": "string",
          "initial_alpha": "number",
          "epsilon_inf_iterations": "array of numbers",
          "converged_epsilon_inf": "number",
          "converged_alpha": "number",
          "band_gap": "number (eV)"
        }
      },
      "description": "Self-consistent hybrid functional convergence data and final quantities for Si, C, and MgO. The hidden checker verifies structural consistency (|Δε∞| < 0.01, α ≈ 1/ε∞) and compares converged_epsilon_inf and band_gap against the paper's reported sc-hybrid values within tolerances."
    }
  ],
  "notes": "The agent must use Quantum ESPRESSO with a finite-field (Berry-phase) method for ε∞, which automatically includes local-field effects. The sc-hybrid loop requires several outer iterations per material, each involving hybrid SCF calculations. The hidden checker performs a result-level comparison (T0) using the paper's sc-hybrid results as reference; tolerances are set to absorb legitimate implementation differences."
}
```

## How you are scored
A hidden verifier will read your `sc_hybrid_results.json` and independently score your submission. The verifier will first check that your output is structurally consistent: for each material, the last two elements of `epsilon_inf_iterations` must differ by less than 0.01, `converged_epsilon_inf` must match the last iteration value, and `converged_alpha` must be approximately 1/`converged_epsilon_inf`. It will then compare your final dielectric constant and band gap against reference values for these systems. The comparison is done with numerical tolerances that account for legitimate differences in computational setup (pseudopotentials, plane-wave cutoff, k-point sampling). Your reward is proportional to the number of materials that pass both the structural and the quantitative checks. Reporting the correct paper values is not enough; you must actually execute the workflow to obtain your own results.
