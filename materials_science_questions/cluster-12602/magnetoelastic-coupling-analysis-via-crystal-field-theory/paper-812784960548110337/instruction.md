# Hyper-polarizable bond model for mapping SHG tensor elements to normal mode distortions in CrSiTe3

## Problem background
Layered ferromagnetic semiconductors like CrSiTe3 can evade the Mermin–Wagner theorem and establish long-range magnetic order even in the two-dimensional limit. A key mechanism involves magneto-elastic distortions driven by short-range spin correlations, which are detectable through the electric-quadrupole second-harmonic generation (SHG) susceptibility tensor. For the R\overline{3} point group, this tensor has eight independent elements. To interpret temperature-dependent SHG polarimetry data and attribute changes in these elements to specific lattice distortions, one must model how totally symmetric normal mode displacements alter each tensor component.

## Approach
The approach is based on a hyper-polarizable bond model that treats each chemical bond as an anharmonic oscillator whose nonlinear polarizability contributes to the bulk EQ SHG susceptibility. The susceptibility tensor \( \chi \) is given by a sum over bonds \( n \): \( \chi \propto \sum \alpha_\omega \alpha_{2\omega} (\hat{b}_n \otimes \hat{b}_n \otimes \hat{b}_n \otimes \hat{b}_n) \), where \( \hat{b}_n \) is a unit vector along the bond direction, and \( \alpha_\omega, \alpha_{2\omega} \) are the bond hyper-polarizabilities. The model is applied to CrSiTe3 using the nearest-neighbor intralayer Cr–Te bonds and the interlayer Cr–Cr bonds, assuming equal bond polarizabilities for all bonds. The four totally symmetric normal modes (\( A_g^1, A_g^2, A_g^3, A_g^4 \)) are simulated by introducing small structural distortions: for \( A_g^1 \), \( A_g^3 \), and \( A_g^4 \), the bond vectors are adjusted according to the displacement pattern; for \( A_g^2 \), which involves a pure out-of-plane displacement of Cr atoms that does not change the direction of the Cr–Cr bond, the polarizability \( \alpha \) of the interlayer Cr–Cr bond is tuned as a proxy for the bond-length change. For each distortion type and a range of displacement amplitudes \( \delta \), the eight independent tensor elements are computed, and their relative changes \( \Delta\chi_{ijkl}(\delta) \) with respect to the undistorted structure are recorded.

## Reproduction target
The goal is to compute the relative change \( \Delta\chi_{ijkl}(\delta) \) for each of the eight independent tensor elements (`xxxz`, `xxyy`, `xzzz`, `yxxx`, `yyyz`, `zzxx`, `zzxy`, `zzzz`) under distortions along each of the four \( A_g \) normal modes, covering a small displacement range (e.g., \( \delta = 0 \) to 0.05 Å). The results are to be written to a CSV file, `bond_model_results.csv`, with columns: `distortion_type`, `tensor_element`, `delta`, `delta_chi`. The computation should capture how each normal mode selectively affects the tensor elements and quantify these changes as a function of the distortion amplitude.

## Assets

- CrSiTe3 crystal structure

## Workflow steps

### Step 1: Hyper-polarizable bond model computation
- Role: scored (load-bearing)
- Action: Obtain the CrSiTe3 crystal structure from a public database. Implement the hyper-polarizable bond model χ ∝ Σ α_ω α_2ω (b̂_n ⊗ b̂_n ⊗ b̂_n ⊗ b̂_n) using nearest-neighbor intralayer Cr–Te bonds and interlayer Cr–Cr bonds, assuming equal bond hyper-polarizabilities. For each A_g normal mode (A_g^1, A_g^2, A_g^3, A_g^4) parameterized by a small displacement δ (range e.g. 0 to 0.05 Å), update bond vectors (or polarizabilities for A_g^2) and compute the relative change Δχ_{ijkl}(δ) of each of the eight independent tensor elements relative to the undistorted structure. Write results to a CSV file.
- Output file: `/app/outputs/bond_model_results.csv`
- Format: csv
- Contract: CSV with columns: distortion_type (one of Ag1, Ag2, Ag3, Ag4), tensor_element (one of xxxz, xxyy, xzzz, yxxx, yyyz, zzxx, zzxy, zzzz), delta (float, displacement amplitude), delta_chi (float, relative change in normalized χ). One row per (distortion, element, delta) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bond_model_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bond_model_results.csv
- path: `/app/outputs/bond_model_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Relative changes of the eight independent SHG susceptibility tensor elements under distortions along the four A_g normal modes, used to verify element selectivity and quantitative agreement with published Fig. 4 digitized curves.
- schema:
  - `type`: table
  - `required_columns`: `distortion_type`, `tensor_element`, `delta`, `delta_chi`
  - `columns`:
    - `distortion_type`: string (Ag1|Ag2|Ag3|Ag4)
    - `tensor_element`: string (xxxz|xxyy|xzzz|yxxx|yyyz|zzxx|zzxy|zzzz)
    - `delta`: float
    - `delta_chi`: float

Notes: The checker verifies that only the expected tensor elements change for each mode (selectivity) and that the non-zero Δχ(δ) curves have correlation ≥ 0.9 with digitized reference data from the paper's Fig. 4.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bond_model_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distortion_type",
          "tensor_element",
          "delta",
          "delta_chi"
        ],
        "columns": {
          "distortion_type": "string (Ag1|Ag2|Ag3|Ag4)",
          "tensor_element": "string (xxxz|xxyy|xzzz|yxxx|yyyz|zzxx|zzxy|zzzz)",
          "delta": "float",
          "delta_chi": "float"
        }
      },
      "description": "Relative changes of the eight independent SHG susceptibility tensor elements under distortions along the four A_g normal modes, used to verify element selectivity and quantitative agreement with published Fig. 4 digitized curves."
    }
  ],
  "notes": "The checker verifies that only the expected tensor elements change for each mode (selectivity) and that the non-zero Δχ(δ) curves have correlation ≥ 0.9 with digitized reference data from the paper's Fig. 4."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the `bond_model_results.csv` file you produce. The verifier checks two aspects: (1) mode selectivity — it independently determines which tensor elements should be affected by each normal mode and verifies that your computed \( \Delta\chi \) values match this pattern; (2) quantitative agreement — for the elements that are expected to change, the verifier compares your \( \Delta\chi(\delta) \) curves against reference data and assigns a score based on the agreement. The final reward (0 to 1) is a weighted combination of these checks. Meeting or exceeding the expected accuracy earns full credit; you are not penalized for a better-than-reference result provided the selectivity pattern is correct.
