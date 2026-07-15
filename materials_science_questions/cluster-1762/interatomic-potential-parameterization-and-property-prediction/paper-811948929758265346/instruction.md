# Parameterization of 6-exp Potential for Orthorhombic Sulfur and Lattice Dynamics

## Problem background
Understanding the intermolecular forces in crystalline sulfur is essential for predicting its static and dynamical properties. The orthorhombic phase of sulfur consists of S8 ring molecules held together by weak van der Waals interactions. A widely used model for nonbonded interactions is the 6-exp potential, where the energy between two atoms at distance r is given by V(r) = -A/r^6 + B exp(-αr). The parameters A, B, and the inverse length α are not directly measurable and must be determined from experimental data. This task addresses the question of whether a physically consistent set of parameters can be derived solely from the equilibrium crystal structure and the known cohesive energy, and whether such a potential can reproduce the crystal's relaxed structure and its lattice vibrational frequencies at the zone center.

## Approach
To determine the potential, the total crystal potential Φ is written as a sum over all nonbonded atom pairs: Φ = -aA + bB, where a = Σ 1/r_i^6 and b = Σ exp(-α r_i) are lattice sums that depend on α and the crystal geometry. For a given α, these sums are evaluated using the published orthorhombic structure (space group Fddd). The crystal is required to satisfy the condition of zero stress under a homogeneous scaling, which yields 6Aa = Bβ, with β = α Σ r_i exp(-α r_i). Together with the experimental cohesive energy Φ₀ = -25.2 kcal mol⁻¹, the parameters A and B are solved for each α. This defines a family of potentials parametrized by α.

For each α, a static energy minimization is performed: the unit cell vectors and the rigid-body rotation and translation of the S8 molecule within the cell are varied to lower the total potential until a minimum is found. This yields the equilibrium lattice parameters, the small changes in cell volume, the reduction in potential energy, and the displacement of the molecule.

Using the minimized structure and the fitted potential, the lattice dynamical matrix is constructed at the Γ point (zero wave vector). Diagonalization gives the normal-mode frequencies, which are classified according to the irreducible representations of the space group Fddd (Γ₁⁺ through Γ₄⁻). The entire procedure is carried out for α ranging from 2.8 to 4.0 Å⁻¹ in steps of 0.1 Å⁻¹.

## Reproduction target
Run the above pipeline for each α = 2.8, 2.9, ..., 4.0 Å⁻¹ and produce two output files under /app/outputs:

- static_results.csv: one row per α, with the columns: alpha (Å⁻¹), A (kcal mol⁻¹ Å⁶), B (kcal mol⁻¹), cell_volume_change (Å³), phi_reduction (kcal mol⁻¹), a (Å), delta_a_percent (%), b (Å), delta_b_percent (%), c (Å), delta_c_percent (%), molecular_rotation (degrees), molecular_translation (Å). These columns correspond to the fitted 6-exp parameters, the volume expansion and potential reduction during minimization, the optimized unit cell parameters and their relative changes, and the rigid-body displacement of the S8 molecule.

- lattice_frequencies.csv: one row per α and per irreducible representation, with columns: alpha (Å⁻¹), representation (string, e.g., "Gamma1+", "Gamma2+", …), frequency_cm-1 (cm⁻¹). Report the nonzero Γ-point lattice frequencies for all symmetry representations appearing in the dynamics.

## Assets

- Crystal structure of orthorhombic sulfur (S8, space group Fddd): 10.1107/S0365110X55001690

## Workflow steps

### Step 1: Compute static lattice properties and potential parameters
- Role: scored
- Action: For each α from 2.8 to 4.0 Å⁻¹ (step 0.1 Å⁻¹): (1) generate the list of nonbonded atom pairs from the orthorhombic S8 crystal structure; (2) compute the lattice sums a(α), b(α), β(α) over all nonbonded pairs; (3) use the equilibrium condition 6Aa = Bβ and experimental cohesive energy Φ₀ = -25.2 kcal mol⁻¹ to solve for A(α) and B(α); (4) perform static energy minimization by varying unit-cell parameters and rigid-body rotation and translation of the S8 molecule; (5) record the optimized unit-cell parameters, volume change, potential reduction, molecular rotation angle, and translation shift. Report all results in a single CSV file.
- Output file: `/app/outputs/static_results.csv`
- Format: csv
- Contract: Columns: alpha (Å⁻¹), A (kcal mol⁻¹ Å⁶), B (kcal mol⁻¹), cell_volume_change (Å³), phi_reduction (kcal mol⁻¹), a (Å), delta_a_percent (%), b (Å), delta_b_percent (%), c (Å), delta_c_percent (%), molecular_rotation (degrees), molecular_translation (Å)
- Scoring: scored by hidden verifier

### Step 2: Compute zero-wave-vector lattice frequencies
- Role: scored
- Action: Using the fitted potential parameters A(α), B(α) and the minimized crystal structure from step 1, perform a lattice dynamical calculation at the Γ point (zero wave vector) for each α. Diagonalize the dynamical matrix and extract the frequencies for each irreducible representation (Γ₁⁺ through Γ₄⁻). Report the frequencies for all representations.
- Output file: `/app/outputs/lattice_frequencies.csv`
- Format: csv
- Contract: Columns: alpha (Å⁻¹), representation (e.g., Gamma1+, Gamma2+, ...), frequency_cm-1
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_results.csv`
- `/app/outputs/lattice_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_results.csv
- path: `/app/outputs/static_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Static results from 6-exp potential fit and structure minimization. Contains one row per α value.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `A`, `B`, `cell_volume_change`, `phi_reduction`, `a`, `delta_a_percent`, `b`, `delta_b_percent`, `c`, `delta_c_percent`, `molecular_rotation`, `molecular_translation`
  - `units`:
    - `alpha`: Å⁻¹
    - `A`: kcal mol⁻¹ Å⁶
    - `B`: kcal mol⁻¹
    - `cell_volume_change`: Å³
    - `phi_reduction`: kcal mol⁻¹
    - `a`: Å
    - `delta_a_percent`: %
    - `b`: Å
    - `delta_b_percent`: %
    - `c`: Å
    - `delta_c_percent`: %
    - `molecular_rotation`: degrees
    - `molecular_translation`: Å

### lattice_frequencies.csv
- path: `/app/outputs/lattice_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Zero-wave-vector lattice frequencies for each irreducible representation. One row per α and representation.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `representation`, `frequency_cm-1`
  - `units`:
    - `alpha`: Å⁻¹
    - `frequency_cm-1`: cm⁻¹

Notes: Scoring compares agent-reported values to paper-reported reference values with tolerances; ordering of frequencies by representation is also checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "A",
          "B",
          "cell_volume_change",
          "phi_reduction",
          "a",
          "delta_a_percent",
          "b",
          "delta_b_percent",
          "c",
          "delta_c_percent",
          "molecular_rotation",
          "molecular_translation"
        ],
        "units": {
          "alpha": "Å⁻¹",
          "A": "kcal mol⁻¹ Å⁶",
          "B": "kcal mol⁻¹",
          "cell_volume_change": "Å³",
          "phi_reduction": "kcal mol⁻¹",
          "a": "Å",
          "delta_a_percent": "%",
          "b": "Å",
          "delta_b_percent": "%",
          "c": "Å",
          "delta_c_percent": "%",
          "molecular_rotation": "degrees",
          "molecular_translation": "Å"
        }
      },
      "description": "Static results from 6-exp potential fit and structure minimization. Contains one row per α value."
    },
    {
      "file": "lattice_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "representation",
          "frequency_cm-1"
        ],
        "units": {
          "alpha": "Å⁻¹",
          "frequency_cm-1": "cm⁻¹"
        }
      },
      "description": "Zero-wave-vector lattice frequencies for each irreducible representation. One row per α and representation."
    }
  ],
  "notes": "Scoring compares agent-reported values to paper-reported reference values with tolerances; ordering of frequencies by representation is also checked."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. It reads both CSV files and compares the values you report to a set of hidden reference values that encode the expected physics. The verifier independently checks each workflow stage: the static fit and minimization results (step1) and the lattice frequencies (step2). It combines the scores from the two stages by their relative weight (with the main emphasis on the correct potential parameters, structure changes, and phonon frequencies) to produce a final reward between 0 and 1. The checker verifies both the numerical accuracy of the reported values (within reasonable tolerances that account for legitimate differences in numerical implementation) and the correct ordering and grouping of frequencies by representation. To succeed, you must implement and execute the entire computational pipeline faithfully; merely copying numbers from a publication without performing the calculations will not yield a correct result.
