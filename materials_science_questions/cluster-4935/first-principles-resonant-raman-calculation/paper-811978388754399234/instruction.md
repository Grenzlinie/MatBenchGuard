# Crystal-Field Parameter Fitting for Yb Garnets Using Raman Scattering Data

## Problem background
Ytterbium-doped garnets (YbAG and YbGG) serve as model systems for studying crystal-field (CF) splittings of rare-earth ions in solid-state hosts. The electronic Raman scattering and optical spectra provide direct measures of the CF energy levels, while electron paramagnetic resonance (EPR) gives g‑values. Earlier CF analyses of these materials yielded parameter sets that differ significantly between the aluminium and gallium garnets, and also depart from the systematic trends observed in other rare-earth garnets, raising questions about the correct assignment of the excited ²F₅/₂ multiplet levels. The central problem is to determine the full set of nine phenomenological crystal‑field parameters Bₖq (k=2,4,6; q even) for both YbAG and YbGG, together with the Raman intensity parameter R and magnetic susceptibility constant α, using a least‑squares fit to all available experimental data, and to resolve the assignment ambiguities that contaminated prior work.

## Approach
The method builds a crystal‑field Hamiltonian for the Yb³⁺ 4f¹³ configuration in D₂ symmetry: H_cf = Σₖ,ᵩ Bₖq (Cᵩᵏ + C₋ᵩᵏ), acting on the J=7/2 and J=5/2 manifolds. The Hamiltonian is diagonalized to obtain energies and wavefunctions; the Kramers doublet g‑values are then computed from the effective‑spin formalism using the wavefunctions, and relative Raman intensities are calculated within the Axe approximation using unit tensor operator matrix elements and an adjustable ratio R = |α²/α¹|. The overall scheme is a nonlinear least‑squares optimization that simultaneously fits the Bₖq parameters, the free‑ion energy difference ΔE, and R (for YbAG) to the experimental observables:

- ²F₇/₂ energy levels from Raman measurements,
- candidate ²F₅/₂ energies from optical spectra,
- ground‑state g‑values from EPR on structurally analogous lutetium garnets,
- g‑value of the lowest ²F₅/₂ doublet, and
- relative Raman intensities (polarization combinations VH and HH for selected transitions).

A critical part of the procedure is the reassignment test for YbAG: the fitting is repeated while omitting the ²F₇/₂ levels as input and testing different selections among the four candidate ²F₅/₂ lines, to identify which ones are truly electronic. Derivative analysis of the highest‑lying level's energy with respect to each Bₖq helps judge whether its temperature shift is dominated by non‑cubic parameters, challenging a prior vibronic assignment. The same fitting and eigenstate computations yield the magnetic susceptibility constant α from the crystal‑field wavefunctions.

## Reproduction target
Produce a JSON file `/app/outputs/cf_analysis_results.json` that contains:

- For YbAG and YbGG, each as an object with:
  * `Bkq`: an array of nine floats representing the crystal‑field parameters in the order B₂₀, B₂₂, B₄₀, B₄₂, B₄₄, B₆₀, B₆₂, B₆₄, B₆₆ (in cm⁻¹).
  * `R`: the Raman intensity ratio (float) for YbAG; for YbGG set to `null`.
  * `alpha`: the magnetic susceptibility constant α.
- At top level:
  * `reassignment_validated`: a boolean indicating whether the reassignment test confirms that the 10903 cm⁻¹ line is electronic and that among 10640 and 10680 cm⁻¹ the latter gives a better fit.
  * `reassignment_reasoning`: a string explaining the assignment choice.

All parameters are to be obtained by the least‑squares fitting procedure described in the approach, using the published experimental numbers for the levels, g‑values, and Raman intensities.

## Assets

- Electronic Raman Spectra of Yb3+ in YbAG and YbGG: 10.1063/1.1660436
- Optical Spectra of Yb3+ in Garnets: 10.1103/PhysRev.159.245
- CF Parameters for Yb3+ in YAG and YGG: 10.1103/PhysRev.159.251
- EPR g-values for Yb3+ in LuAG and LuGG: 10.1143/JPSJ.17.443
- Relative Raman Intensities for YbAG
- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Data preparation and Hamiltonian implementation
- Role: process
- Action: Gather the experimental energy levels, g-values, and Raman intensities from the references (Argyle 1971, Buchanan 1967, Pearson 1967, Wolf 1962, and the bundled intensity table). Implement the crystal-field Hamiltonian H_cf = sum_{k,q} B_{kq}(C_q^k + C_{-q}^k) for the Yb3+ 4f13 configuration (J=7/2, J=5/2) in D2 symmetry, functions to diagonalize it, compute directional g-values, and compute relative Raman intensities using the Axe approximation (with adjustable ratio R).
- Evidence: `/app/outputs/hamiltonian_tests.log`

### Step 2: Initial least-squares fit for YbAG (original assignments)
- Role: process
- Action: Perform a least-squares fit of the crystal-field parameters B_kq and the free-ion energy difference ΔE for YbAG using the original 2F7/2 levels (Argyle), the original 2F5/2 levels (Buchanan et al.: 10328, 10640, 10680 cm-1), the g-value of the lowest 2F5/2 doublet, and the ground-state g-values from LuAG. This reproduces the anomalous parameters of Pearson et al. and motivates the reassignment.
- Evidence: `/app/outputs/initial_fit.log`

### Step 3: Derivative analysis of the highest 2F5/2 level
- Role: process
- Action: Compute the partial derivatives of the highest 2F5/2 eigenvalue with respect to each crystal-field parameter B_kq. Show that the largest derivatives are with respect to B20 and B22, not the cubic parameters, challenging the earlier vibronic assignment premise.
- Evidence: `/app/outputs/derivatives.json`

### Step 4: Reassignment test for 2F5/2 levels in YbAG
- Role: process
- Action: Repeat the fitting routine for YbAG while omitting the 2F7/2 levels as input data, using different initial guesses and trying various selections among the four candidate lines (10328, 10640, 10680, 10903 cm-1). Determine that 10328 and 10903 cm-1 must be electronic, and that among the two remaining candidates, 10680 cm-1 yields a better fit.
- Evidence: `/app/outputs/reassignment_result.json`

### Step 5: Final fit for YbAG including Raman intensities
- Role: process
- Action: Perform a nonlinear least-squares fit for YbAG using the reassigned 2F5/2 levels (10328, 10680, 10903 cm-1), the 2F7/2 levels (0, 587, 621, 758.5 cm-1), ground-state g-values (LuAG), and the selected Raman intensities (587 and 621 cm-1 transitions, VH and HH combinations). Fit the nine B_kq parameters, ΔE, and the Raman intensity parameter R. Save the best-fit parameters.
- Evidence: `/app/outputs/ybag_fit_params.npz`

### Step 6: Fit for YbGG (without Raman intensities)
- Role: process
- Action: Perform a least-squares fit for YbGG using the experimental 2F7/2 levels (0, 546, 610, 624 cm-1), the 2F5/2 levels (10313, 10619, 10747 cm-1), and ground-state g-values (LuGG). Do not include Raman intensities. Fit the nine B_kq parameters and ΔE.
- Evidence: `/app/outputs/ybgg_fit_params.npz`

### Step 7: Calculation of magnetic susceptibility parameter alpha
- Role: process
- Action: Using the wavefunctions obtained from the YbAG (step 05) and YbGG (step 06) fits, compute the magnetic susceptibility constant α for both materials.
- Evidence: `/app/outputs/alpha_values.txt`

### Step 8: Final results compilation
- Role: scored (load-bearing)
- Action: Aggregate all final fitting results into a single JSON file. Include for YbAG and YbGG: the nine B_kq parameters (ordered B20, B22, B40, B42, B44, B60, B62, B64, B66), the Raman intensity parameter R (only for YbAG; set null for YbGG), and the susceptibility α. Also include a top-level reassignment validation flag (true/false) and a textual reasoning string explaining why 10903 cm-1 is electronic and why 10680 was chosen over 10640.
- Output file: `/app/outputs/cf_analysis_results.json`
- Format: json
- Contract: JSON object with keys: 'YbAG' and 'YbGG' (each an object containing 'Bkq': list of 9 floats, 'R': float or null, 'alpha': float); top-level keys: 'reassignment_validated' (boolean), 'reassignment_reasoning' (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cf_analysis_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cf_analysis_results.json
- path: `/app/outputs/cf_analysis_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Aggregated crystal-field parameters, Raman intensity ratio, magnetic susceptibility constant, and the reassignment verdict with reasoning. All values are compared to reference thresholds from the paper's results.
- schema:
  - `type`: object
  - `properties`:
    - `YbAG`:
      - `type`: object
      - `properties`:
        - `Bkq`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 9
          - `maxItems`: 9
        - `R`:
          - `type`: number
        - `alpha`:
          - `type`: number
      - `required`: `Bkq`, `R`, `alpha`
    - `YbGG`:
      - `type`: object
      - `properties`:
        - `Bkq`:
          - `type`: array
          - `items`:
            - `type`: number
          - `minItems`: 9
          - `maxItems`: 9
        - `R`:
          - `type`: `number`, `null`
        - `alpha`:
          - `type`: number
      - `required`: `Bkq`, `R`, `alpha`
    - `reassignment_validated`:
      - `type`: boolean
    - `reassignment_reasoning`:
      - `type`: string
  - `required`: `YbAG`, `YbGG`, `reassignment_validated`, `reassignment_reasoning`

Notes: The Bkq parameters are in cm⁻¹. Scoring uses threshold-based comparison with tolerances derived from the paper's reported values and expected numerical accuracy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cf_analysis_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "YbAG": {
            "type": "object",
            "properties": {
              "Bkq": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 9,
                "maxItems": 9
              },
              "R": {
                "type": "number"
              },
              "alpha": {
                "type": "number"
              }
            },
            "required": [
              "Bkq",
              "R",
              "alpha"
            ]
          },
          "YbGG": {
            "type": "object",
            "properties": {
              "Bkq": {
                "type": "array",
                "items": {
                  "type": "number"
                },
                "minItems": 9,
                "maxItems": 9
              },
              "R": {
                "type": [
                  "number",
                  "null"
                ]
              },
              "alpha": {
                "type": "number"
              }
            },
            "required": [
              "Bkq",
              "R",
              "alpha"
            ]
          },
          "reassignment_validated": {
            "type": "boolean"
          },
          "reassignment_reasoning": {
            "type": "string"
          }
        },
        "required": [
          "YbAG",
          "YbGG",
          "reassignment_validated",
          "reassignment_reasoning"
        ]
      },
      "description": "Aggregated crystal-field parameters, Raman intensity ratio, magnetic susceptibility constant, and the reassignment verdict with reasoning. All values are compared to reference thresholds from the paper's results."
    }
  ],
  "notes": "The Bkq parameters are in cm⁻¹. Scoring uses threshold-based comparison with tolerances derived from the paper's reported values and expected numerical accuracy."
}
```

## How you are scored
A hidden verifier reads your `cf_analysis_results.json` and compares each quantity to reference values derived from the paper’s best‑fit results. The Bₖq arrays for YbAG and YbGG are checked against the published crystal‑field parameters with tolerances that reflect the typical spread caused by different numerical solvers and initial conditions. The Raman intensity parameter R for YbAG is checked against the paper’s reported value, and the susceptibility α for both materials is compared within an allowed deviation. The reassignment verdict (`reassignment_validated` and `reassignment_reasoning`) is compared to the physically correct electronic assignment, which follows from the experimental data and the crystal‑field analysis. Each of these checks contributes a fraction of the total reward; the final score is a weighted combination of the individual checks, normalized to [0, 1]. Note that reporting a number that accidentally falls within tolerance without genuine computational work is not detectable by the verifier, but the task is designed on the premise that the solving agent performs the required computations honestly.
