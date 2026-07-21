# Hyper-polarizable bond model for mapping SHG tensor elements to normal mode distortions in CrSiTe3

## Problem background
Layered ferromagnetic semiconductors like CrSiTe3 can evade the Mermin–Wagner theorem and establish long-range magnetic order because magneto-elastic distortions driven by short-range spin correlations provide a route to three-dimensional ordering. These distortions are detectable through the electric-quadrupole second-harmonic generation (SHG) susceptibility tensor. For the R‾3 point group, this tensor has eight independent elements: `xxxz`, `xxyy`, `xzzz`, `yxxx`, `yyyz`, `zzxx`, `zzxy`, `zzzz`. Temperature-dependent SHG polarimetry reveals that distinct totally symmetric (A_g) normal modes selectively affect subsets of these tensor elements. To interpret the data, one must model how each A_g distortion modifies all eight tensor elements.

## Approach
The hyper-polarizable bond model treats each chemical bond as an anharmonic oscillator whose nonlinear polarizability contributes to the bulk EQ SHG susceptibility through

\[
\chi_{ijkl} \propto \sum_{n} \alpha_\omega^{(n)} \alpha_{2\omega}^{(n)} (\hat{b}_n \otimes \hat{b}_n \otimes \hat{b}_n \otimes \hat{b}_n)_{ijkl},
\]

where \(\hat{b}_n\) is a unit vector along bond \(n\), and \(\alpha_\omega^{(n)},\alpha_{2\omega}^{(n)}\) are the bond hyper-polarizabilities. For CrSiTe3 we include:
- all nearest-neighbor intralayer Cr–Te bonds,
- the interlayer Cr–Cr bonds that connect adjacent layers.

All bonds are initially assigned equal bare polarizability products \(\alpha_\omega \alpha_{2\omega} = 1\). When a bond length changes as a result of an atomic displacement, the polarizability product is assumed to change linearly with the bond length. For a small change \(\Delta l\) in a bond’s length we set

\[
\alpha_\omega^{(n)} \alpha_{2\omega}^{(n)} = 1 + \gamma \, \Delta l,
\]

with \(\gamma = 1\,\text{Å}^{-1}\). This rule must be applied to every bond whose length changes; bonds that only reorient without changing length retain \(\alpha_\omega \alpha_{2\omega}=1\).

The four totally symmetric normal modes (Ag1, Ag2, Ag3, Ag4) are simulated by applying small atomic displacements parameterized by a single amplitude δ (0 ≤ δ ≤ 0.05 Å). For each mode and each δ, we update the atomic positions, recompute the bond vectors, apply the polarizability rule above, and evaluate the eight independent tensor elements \(\chi_{ijkl}\). The relative change with respect to the undistorted structure is recorded, normalized as defined below.

## Normal mode displacement patterns (how to update bonds)

Below is a detailed prescription for each A_g mode. Use the CrSiTe3 crystal structure (space group R‾3, conventionally with Cr at (0,0,0) etc.) to identify the relevant bonds and apply the described displacements.

### Ag1 – In-plane symmetric stretching of Cr–Te bonds
- All Cr–Te bonds change their length while preserving direction. Because the bond length changes, the hyper-polarizability product must be updated.
- Implementation: for every Cr–Te bond, displace the Cr and Te atoms along the bond direction **oppositely** by ±δ/2. That is, if \(\mathbf{r}_{\text{Cr}}\) and \(\mathbf{r}_{\text{Te}}\) are their positions,
  \[
  \mathbf{r}_{\text{Cr}} \to \mathbf{r}_{\text{Cr}} + \frac{\delta}{2}\,\hat{b},\qquad \mathbf{r}_{\text{Te}} \to \mathbf{r}_{\text{Te}} - \frac{\delta}{2}\,\hat{b},
  \]
  where \(\hat{b} = (\mathbf{r}_{\text{Te}} - \mathbf{r}_{\text{Cr}})/\|\mathbf{r}_{\text{Te}} - \mathbf{r}_{\text{Cr}}\|\).
  The bond length increases by \(\Delta l = \delta\); therefore set \(\alpha_\omega \alpha_{2\omega} = 1 + \delta\) for each Cr–Te bond.
- No atoms move along the c-axis; the interlayer Cr–Cr bonds are unchanged.

### Ag2 – Pure out-of-plane Cr displacement (Cr–Cr bond length modulation)
- All Cr atoms are displaced by δ along the crystallographic c-axis; all other atoms (Si, Te) remain fixed.
- The interlayer Cr–Cr bonds change length by δ. Because the bond vector remains parallel to the c-axis, the effect on χ comes only from the polarizability change. For every interlayer Cr–Cr bond, set \(\alpha_\omega \alpha_{2\omega} = 1 + \delta\).
- Intralayer Cr–Te bonds are **not** moved.

### Ag3 – Mixed displacement (mainly Cr along c and Te expanding in-plane)
- Cr atoms are displaced by δ along the c-axis (same sign as Ag2).
- Te atoms are displaced radially outward in the ab-plane by δ; the direction of each Te displacement points **away** from the nearest Cr atom (three-fold symmetry preserved).
- Si atoms may be held fixed.
- This mode alters both the length and the direction of Cr–Te bonds and slightly changes the Cr–Cr interlayer bond. As a result, **all eight tensor elements are affected** and should exhibit a linear increase with δ.

### Ag4 – Mixed displacement (mainly Cr in-plane and Te along c)
- Cr atoms are displaced radially outward in the ab-plane by δ; the direction of each Cr displacement points **away** from the center of its coordination octahedron.
- Te atoms are displaced by δ along the c-axis (same sign for all Te).
- Si atoms may be held fixed.
- This mode affects all bonds to some degree, and from the paper’s observations **all eight tensor elements are affected**, showing a linear increase with δ.

The detailed displacement vectors for Ag3 and Ag4 can be extracted from a full lattice-dynamics calculation, but the simplified descriptions above are sufficient to produce the correct selectivity pattern in the bond model when combined with the expected selectivity information below.

## Expected tensor element selectivity

Based on the experimental observations reported in the paper (Figure 4), the four A_g modes selectively modify the following tensor elements:

| Distortion type | Affected tensor elements        | Unaffected elements            |
|-----------------|---------------------------------|--------------------------------|
| Ag1             | xxxz, yyyz                      | all others                     |
| Ag2             | zzzz                            | all others                     |
| Ag3             | all eight (xxxz, xxyy, xzzz, yxxx, yyyz, zzxx, zzxy, zzzz) | none |
| Ag4             | all eight (xxxz, xxyy, xzzz, yxxx, yyyz, zzxx, zzxy, zzzz) | none |

For each mode, the normalized relative change Δχ(δ) of an affected element should be **proportional to δ** (approximately a straight line with slope 1 under the normalization convention defined below). The unaffected elements must remain zero within numerical tolerance for all δ > 0. Your computed curves must reproduce this selectivity pattern and linear trend to pass the verifier.

> **Note:** If your bond‑model implementation produces a slightly different slope or small numerical artifacts, the verifier still accepts the result provided the Pearson correlation with a linear reference (Δχ ∝ δ for affected elements, Δχ = 0 for unaffected ones) is at least 0.9 for each element.

## Normalization convention
After computing the raw susceptibility tensor \(\tilde{\chi}_{ijkl}(\delta)\) from the sum over bonds, define the normalized relative change for each element as

\[
\Delta\chi_{ijkl}(\delta) = \frac{\tilde{\chi}_{ijkl}(\delta) - \tilde{\chi}_{ijkl}(0)}{\max_{mnop} |\tilde{\chi}_{mnop}(0)|}.
\]

This makes \(\Delta\chi\) dimensionless and of order 1 for small δ. All results must be written following this rule.

## Workflow steps

### Step 1: Hyper-polarizable bond model computation
- Role: scored (load-bearing)
- Action: Obtain the CrSiTe3 crystal structure from a public database (Materials Project, ICSD, COD; space group R-3, 148). Identify all nearest-neighbor Cr–Te intralayer bonds and interlayer Cr–Cr bonds. Set the initial polarizability product \(\alpha_\omega \alpha_{2\omega} = 1\) for every bond.
- For each normal mode `Ag1`, `Ag2`, `Ag3`, `Ag4`:
  - Define a grid of displacement amplitudes δ: [0, 0.005, 0.01, …, 0.05] Å.
  - Apply the atomic displacements described in the section "Normal mode displacement patterns" above.
  - After updating the atomic positions, recompute the bond vectors and their lengths. For every bond whose length changed by \(\Delta l\), update its polarizability product to \(1 + \Delta l\).
  - Evaluate the susceptibility tensor \(\tilde{\chi}_{ijkl}(\delta)\).
  - Compute \(\Delta\chi_{ijkl}(\delta)\) using the normalization convention above.
- Output file: `/app/outputs/bond_model_results.csv`
- Format: csv
- Contract: CSV with columns: `distortion_type`, `tensor_element`, `delta`, `delta_chi`. One row per (distortion, element, delta) combination.
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
- description: Relative changes of the eight independent SHG susceptibility tensor elements under distortions along the four A_g normal modes. The verifier checks that only the physically expected tensor elements change for each mode and that the non-zero Δχ(δ) curves follow the linear trend observed in the published data.
- schema:
  - `type`: table
  - `required_columns`: `distortion_type`, `tensor_element`, `delta`, `delta_chi`
  - `columns`:
    - `distortion_type`: string (Ag1|Ag2|Ag3|Ag4)
    - `tensor_element`: string (xxxz|xxyy|xzzz|yxxx|yyyz|zzxx|zzxy|zzzz)
    - `delta`: float (displacement amplitude in Å)
    - `delta_chi`: float (normalised relative change)

Notes: The verifier compares your Δχ(δ) curves against a linear model (Δχ ∝ δ for the correct elements, zero otherwise) that reproduces the trends shown in the paper’s Figure 4. A Pearson correlation ≥ 0.9 for each affected element is required to pass. Unaffected elements must remain zero within numerical tolerance.

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
      "description": "Relative changes of the eight independent SHG susceptibility tensor elements under distortions along the four A_g normal modes, used to verify element selectivity and quantitative agreement with the expected linear trend from the paper."
    }
  ],
  "notes": "The verifier checks that only the expected tensor elements change for each mode and that the non-zero Δχ(δ) curves are highly correlated with a linear reference derived from the paper’s observations."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the `bond_model_results.csv` file you produce. The verifier checks two aspects:
1. **Mode selectivity** – it verifies that only the tensor elements expected to change for each A_g mode show a non-zero Δχ(δ), while the others remain zero.
2. **Quantitative agreement** – for the elements that do change, the verifier compares your Δχ(δ) curves against a linear reference (Δχ ∝ δ) derived from the trends reported in the paper, using the Pearson correlation coefficient. A correlation ≥ 0.9 is required for full credit.

The final reward (0 to 1) is a weighted combination of selectivity and correlation scores. Meeting or exceeding the accuracy threshold earns full credit; you are not penalised for a better-than-reference result provided the selectivity pattern is correct.