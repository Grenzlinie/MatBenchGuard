# Cladding Mode Eigenvalue and Field Analysis for Asymmetric Dual-Core Fiber

## Problem background
Cladding modes in asymmetric dual-core fibers play a key role in long-period grating (LPG) based devices that couple light between cores through the cladding. Simple coreless fiber approximations are often used, but they may fail to capture the true modal properties when two cores are present. This work addresses the question: how do the effective indices and field distributions of cladding modes differ from those predicted by a coreless model, for a fiber with one core near the axis and the other off-axis? The reproduction computes these quantities through a semianalytical eigenvalue approach, demonstrating the influence of the asymmetric dual-core geometry on the modal characteristics.

## Approach
The method uses a scalar wave analysis suitable for large-diameter fibers. The optical field in the cladding region is expanded in terms of cylindrical Bessel and Neumann functions for the fiber axis and the two local core coordinate systems, while the core regions use Bessel functions and the ambient region uses modified Bessel functions. By applying boundary conditions at core and cladding interfaces and employing translation matrices to convert between coordinate systems, the unknown amplitude coefficients are expressed in terms of a set of coefficients for the central field. Imposing continuity at the outer cladding boundary yields a determinant equation whose roots are the effective indices of the cladding modes. The expansion is truncated at a sufficiently high azimuthal order to ensure convergence. Once an effective index is found, the corresponding field distribution is reconstructed using the same basis expansion, normalized appropriately, and sampled along chosen radial directions to reveal the azimuthal asymmetry induced by the offset cores.

## Reproduction target
For a dual-core fiber with parameters: a1 = 3.0 µm, a2 = 3.6 µm, a3 = 62.5 µm, n1 = n2 = 1.4530, n3 = 1.4440, n4 = 1.0, core center distances d1 = 32 µm and d2 = 0, at a wavelength λ = 1.550 µm, compute:
(1) the effective indices n_eff of the LP03′, LP04′, and LP06′ cladding modes by solving the determinant equation numerically;
(2) the normalized radial field profile of the LP03′ mode along the azimuthal directions θ = 0 and θ = π, over the radial range r = 0 to 62.5 µm.
The results must be written to the specified CSV files with the given schemas.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Assemble eigenvalue matrix functions
- Role: process
- Action: Implement the construction of the diagonal matrix F(neff) and the full coupling matrix T0(neff) using cylindrical Bessel, Neumann, and modified Bessel functions, translation matrices, and the given fiber parameters. This implements the determinant equation |F+T0|=0 from the paper’s semianalytical derivation, truncating the azimuthal expansions at m=±12.
- Evidence: `/app/outputs/matrix_assembly.log`

### Step 2: Solve cladding mode effective indices
- Role: scored (load-bearing)
- Action: Numerically search for roots of det(F(neff)+T0(neff))=0 to locate the effective indices corresponding to LP03′, LP04′, and LP06′ modes. Write the mode identifiers and the computed n_eff values to CSV with six decimal places.
- Output file: `/app/outputs/effective_indices.csv`
- Format: csv
- Contract: mode (str): LP03', LP04', LP06'; n_eff (float): effective index (6 decimal places)
- Scoring: scored by hidden verifier

### Step 3: Compute radial field profile for LP03' mode
- Role: scored
- Action: Using the effective index obtained for the LP03′ mode, reconstruct the normalized field amplitude along the radial direction at azimuthal angles θ=0 and θ=π. Normalize the field appropriately and sample r from 0 to 62.5 µm. Write the data to CSV.
- Output file: `/app/outputs/field_profile_LP03prime.csv`
- Format: csv
- Contract: r_um (float): radial coordinate in µm; amplitude_theta0 (float): normalized field amplitude at θ=0; amplitude_theta_pi (float): normalized field amplitude at θ=π
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_indices.csv`
- `/app/outputs/field_profile_LP03prime.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_indices.csv
- path: `/app/outputs/effective_indices.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective indices of the three cladding modes (dual-core model), the corresponding coreless fiber effective indices, and their signed difference delta_n_eff = n_eff - n_eff_coreless, at λ=1.550 µm for the given fiber parameters.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `n_eff`, `n_eff_coreless`, `delta_n_eff`
  - `units`:
    - `n_eff`: dimensionless (effective index)
    - `n_eff_coreless`: dimensionless (effective index)
    - `delta_n_eff`: dimensionless (difference)

### field_profile_LP03prime.csv
- path: `/app/outputs/field_profile_LP03prime.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized radial field profile of the LP03′ mode along θ=0 and θ=π, demonstrating the azimuthally asymmetric intensity distribution.
- schema:
  - `type`: table
  - `required_columns`: `r_um`, `amplitude_theta0`, `amplitude_theta_pi`
  - `units`:
    - `r_um`: µm
    - `amplitude_theta0`: normalized field amplitude
    - `amplitude_theta_pi`: normalized field amplitude

Notes: The task reproduces the effective indices (dual-core and coreless) and the field profile for the given geometry, demonstrating the difference between the two models as highlighted in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_indices.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "n_eff",
          "n_eff_coreless",
          "delta_n_eff"
        ],
        "units": {
          "n_eff": "dimensionless (effective index)",
          "n_eff_coreless": "dimensionless (effective index)",
          "delta_n_eff": "dimensionless (difference)"
        }
      },
      "description": "Effective indices of the three cladding modes (dual-core model), the corresponding coreless fiber effective indices, and their signed difference delta_n_eff = n_eff - n_eff_coreless, at λ=1.550 µm for the given fiber parameters."
    },
    {
      "file": "field_profile_LP03prime.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_um",
          "amplitude_theta0",
          "amplitude_theta_pi"
        ],
        "units": {
          "r_um": "µm",
          "amplitude_theta0": "normalized field amplitude",
          "amplitude_theta_pi": "normalized field amplitude"
        }
      },
      "description": "Normalized radial field profile of the LP03′ mode along θ=0 and θ=π, demonstrating the azimuthally asymmetric intensity distribution."
    }
  ],
  "notes": "The task reproduces the effective indices (dual-core and coreless) and the field profile for the given geometry, demonstrating the difference between the two models as highlighted in the paper."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that does not see your code. The scoring is structured as follows:
- For `effective_indices.csv`, the verifier reads the three mode effective indices and checks whether they lie close to the physically expected values for this geometry (closeness is measured with an appropriate tolerance; exact agreement with any particular prior is not required).
- For `field_profile_LP03prime.csv`, the verifier performs a structural audit: it verifies that the radial profile at θ=0 is not symmetric with that at θ=π, that the maximum field intensity occurs at a non-zero radial coordinate (offset from the fiber axis), and that in the region of the second core (~30–35 µm) there is a local maximum shifted toward the primary core.
Each output stage carries a share of the total reward; you must produce both artifacts to receive full credit. Simply reporting the expected numbers without performing the actual computation will not satisfy the structural audit and will result in a low score.
