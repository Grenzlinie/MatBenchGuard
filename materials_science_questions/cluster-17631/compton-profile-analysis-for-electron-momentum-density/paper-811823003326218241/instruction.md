# Compute correlated Compton profiles of bcc lithium using quantum Monte Carlo with scaled LDA reference

## Problem background
High-resolution Compton scattering experiments on solid lithium have revealed significant discrepancies with conventional band-theoretical calculations performed within the local density approximation (LDA). The valence Compton profiles, which are integrals of the electronic momentum distribution over planes perpendicular to a scattering direction, are sensitive to electron-electron correlation effects. The task is to compute the contribution of electronic correlation to the directional Compton profiles of bcc lithium using first-principles pseudopotential quantum Monte Carlo (QMC) and a scaled-reference method. This will determine the correlation-induced corrections to the LDA results and provide a benchmark for understanding the origin of the experimental discrepancies.

## Approach
The QMC Compton profile is constructed as a superposition of a scaled all-electron LDA reference profile and a correction term: J_QMC = α·J_LDA(full-core) + ΔJ. The all-electron LDA profile J_LDA(full-core) properly accounts for core–valence orthogonality and serves as a highly accurate reference. The QMC momentum distribution n_QMC is obtained from variational Monte Carlo simulations on large periodic cells with multiple k‑point samplings (Γ, X, M, R) to achieve high resolution in momentum space. A corresponding LDA momentum distribution n_LDA is computed from a plane‑wave pseudopotential calculation. The scaling factor α is determined by minimizing a cost function that measures the discontinuity in the difference Δn^α = n_QMC − α·n_LDA; an optimal α yields a smooth correction function that is less sensitive to finite‑size errors. The correction ΔJ is then obtained by integrating Δn^α over planes corresponding to the [100], [110], and [111] directions using the linear tetrahedron method, which accurately handles the band‑structure discontinuities. The final profiles are reported on a regular momentum grid.

## Reproduction target
The objective is to compute the optimal scaling factor α that minimizes the discontinuity cost function for the difference Δn^α, and to produce the corresponding directional valence Compton profiles J(p) for bcc lithium along the [100], [110], and [111] crystallographic directions. The results must be written to two files:
- alpha.json: contains the determined α as a JSON object with key "alpha".
- compton_profiles_qmc.csv: a CSV file with columns p (momentum in atomic units), J_100, J_110, and J_111 (Compton profile intensities in atomic units). The momentum grid must cover at least the range 0 to 2 a.u. with a spacing ≤ 0.05 a.u.

## Assets

- Quantum ESPRESSO (or equivalent open-source plane-wave DFT code): https://www.quantum-espresso.org/
- QMCPACK (or equivalent open-source quantum Monte Carlo code): https://qmcpack.org/
- Troullier-Martins pseudopotential for Li (s and p components, cutoff radius 2.4 a.u.): https://www.quantum-espresso.org/pseudopotentials/
- BCC lithium crystal structure

## Workflow steps

### Step 1: LDA pseudopotential calculation
- Role: process
- Action: Perform a plane-wave LDA-DFT calculation for bcc lithium using the Troullier-Martins pseudopotential. Compute the LDA momentum distribution n_LDA(p) on a fine k-point grid (unfolded to a sphere of ~2 a.u. radius) and extract the single-particle orbitals φ_LDA(r) (plane-wave coefficients) that will be used to build the QMC trial wavefunction.
- Evidence: `/app/outputs/lda_pseudo_momentum.nc`

### Step 2: LDA full-core (all-electron) calculation
- Role: process
- Action: Perform an all-electron LDA-DFT calculation for bcc lithium using the unscreened −3/r potential and a high plane-wave cutoff (≥400 Ry). Compute the full-core valence Compton profiles J_LDA(p) in the [100], [110], and [111] directions via the linear tetrahedron method. These profiles serve as the accurate reference for core-valence orthogonality in the final composition.
- Evidence: `/app/outputs/fullcore_lda_profile_JLDA.csv`

### Step 3: QMC wavefunction optimisation on 54-atom cell
- Role: process
- Action: Using a 54-atom bcc lithium simulation cell with periodic boundary conditions, optimise the Jastrow factor coefficients of the Slater-Jastrow trial wavefunction (built from LDA orbitals and the Troullier-Martins pseudopotential) via variance minimisation. Output the optimised single-body Jastrow star coefficients χ_s to be used in subsequent production runs.
- Evidence: `/app/outputs/jastrow_optimised_params.json`

### Step 4: QMC momentum distribution on 250-atom cell with multiple k-point samplings
- Role: process
- Action: Run variational Monte Carlo (VMC) on a 250-atom bcc lithium cell with four boundary-condition shifts corresponding to Γ, X, M, and R k-point samplings. Use the optimised wavefunction from step_03 and the nonlocal pseudopotential. Accumulate the correlated momentum distribution n_QMC(p) on the combined grid (averaged over symmetry-related points). A 250-atom cell is sufficient; a 686-atom cell may be used if preferred.
- Evidence: `/app/outputs/qmc_momentum_grid.h5`

### Step 5: Determine optimal scaling factor alpha
- Role: scored (load-bearing)
- Action: Using n_QMC(p) from step_04 and n_LDA(p) from step_01, compute the difference Δn^α(p)=n_QMC−α·n_LDA and minimise the cost function that penalises discontinuities in Δn^α (sum over grid points of squared differences between neighbouring grid values weighted by n_QMC²) over α. Output the found optimal α.
- Output file: `/app/outputs/alpha.json`
- Format: json
- Contract: {"alpha": "float, positive number between 0 and 1"}
- Scoring: scored by hidden verifier

### Step 6: Correction profile integration (linear tetrahedron method)
- Role: process
- Action: Form Δn^α(p)=n_QMC(p)−α·n_LDA(p) on the combined four-sampling grid using the α from step_05. Integrate Δn^α(p) using the linear tetrahedron method to obtain the directional correction Compton profiles ΔJ^α(p) in [100], [110], and [111] directions. The integration follows the standard linear tetrahedron approach (division into cubes, tetrahedra, linear interpolation, surface intersection).
- Evidence: `/app/outputs/deltaJ_alpha_directional.csv`

### Step 7: Final QMC Compton profile composition
- Role: scored
- Action: Combine the scaled full-core LDA profile from step_02 with the correction from step_06: J_QMC(p)=α·J_LDA(full-core)(p) + ΔJ^α(p). Compute the final valence Compton profiles in the [100], [110], [111] directions on a regular momentum grid.
- Output file: `/app/outputs/compton_profiles_qmc.csv`
- Format: csv
- Contract: CSV with columns: p (float, atomic units), J_100 (float), J_110 (float), J_111 (float). p values cover at least the range 0 to 2 a.u. with spacing ≤0.05 a.u.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha.json`
- `/app/outputs/compton_profiles_qmc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha.json
- path: `/app/outputs/alpha.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimal scaling factor α obtained by minimising the discontinuity cost function for Δn^α. Evaluated using reference_match: your α must be within a hidden tolerance of the reference.
- schema:
  - `type`: object
  - `required`:
    - `alpha`: float
  - `items`: object
  - `required_columns`:
  - `units`: object

### compton_profiles_qmc.csv
- path: `/app/outputs/compton_profiles_qmc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Directional valence Compton profiles J(p) in the [100], [110], [111] crystallographic directions. Evaluated using reference_match: at selected momentum points, absolute deviation from the hidden reference must be within tolerance.
- schema:
  - `type`: table
  - `required`:
    - `p`: float (atomic units)
    - `J_100`: float (atomic units)
    - `J_110`: float (atomic units)
    - `J_111`: float (atomic units)
  - `items`: object
  - `required_columns`: `p`, `J_100`, `J_110`, `J_111`
  - `units`:
    - `p`: atomic units
    - `J_100`: atomic units
    - `J_110`: atomic units
    - `J_111`: atomic units

Notes: Both scored artifacts use reference_match (closeness within a tolerance window). The verifier first validates format/schema; missing or ill‑formed files receive zero reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "alpha": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Optimal scaling factor α obtained by minimising the discontinuity cost function for Δn^α. Evaluated using reference_match: your α must be within a hidden tolerance of the reference."
    },
    {
      "file": "compton_profiles_qmc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {
          "p": "float (atomic units)",
          "J_100": "float (atomic units)",
          "J_110": "float (atomic units)",
          "J_111": "float (atomic units)"
        },
        "items": {},
        "required_columns": [
          "p",
          "J_100",
          "J_110",
          "J_111"
        ],
        "units": {
          "p": "atomic units",
          "J_100": "atomic units",
          "J_110": "atomic units",
          "J_111": "atomic units"
        }
      },
      "description": "Directional valence Compton profiles J(p) in the [100], [110], [111] crystallographic directions. Evaluated using reference_match: at selected momentum points, absolute deviation from the hidden reference must be within tolerance."
    }
  ],
  "notes": "Both scored artifacts use reference_match (closeness within a tolerance window). The verifier first validates format/schema; missing or ill‑formed files receive zero reward."
}
```

## How you are scored
A hidden automated verifier independently evaluates each submitted artifact (alpha.json and compton_profiles_qmc.csv). Both artifacts are scored using a reference_match policy: your computed value must lie within a fixed tolerance window around a hidden reference value (two‑sided closeness match). The verifier first validates that the output files conform to the required format and schema; ill‑formed or missing files receive zero reward. The scores from the two artifacts are combined into a single overall reward in [0,1]. Reporting the paper’s numbers without having executed the computational pipeline is not sufficient—the verifier expects artifacts produced by a genuine run of the specified workflow.
