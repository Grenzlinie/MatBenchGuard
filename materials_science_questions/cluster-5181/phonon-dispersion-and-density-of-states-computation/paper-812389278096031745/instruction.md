# WDA Implementation for Ferroelectric Perovskites: Lattice Constants and Ferroelectric Instability

## Problem background
The local density approximation (LDA) to density functional theory (DFT) systematically underestimates the equilibrium volumes of ferroelectric perovskite crystals, which makes many predicted ferroelectric properties unreliable. The weighted density approximation (WDA) is a non-local exchange-correlation functional that replaces the true pair-distribution function of an inhomogeneous electron gas with that of a homogeneous gas evaluated at a weighted density, offering a route to more accurate volumes. This task implements the WDA in a plane‑wave pseudopotential framework with shell partitioning and the Perdew–Wang pair‑distribution function, and tests its performance on five common ferroelectric perovskites.

## Approach
The WDA functional is implemented inside an open‑source plane‑wave DFT code. The implementation uses Troullier–Martins norm‑conserving pseudopotentials, treats core and semi‑core electrons with the LDA while applying the WDA only to valence electrons (shell partitioning), and adopts the Perdew–Wang parametrization of the homogeneous‑gas pair‑distribution function G. The weighted density at each point is determined self‑consistently by a sum rule that guarantees the xc hole integrates to −1. Two forms of the sum rule are studied: the original version that integrates only the valence density, and a corrected version that includes the core density in the integration. As a baseline, the same calculations are also performed with the pure LDA. The workflow consists of (i) computing equilibrium cubic lattice constants for five materials (KNbO3, KTaO3, SrTiO3, BaTiO3, PbTiO3) by scanning lattice parameters and locating the energy minimum for each functional, and (ii) constructing frozen‑phonon energy‑displacement curves for three materials (KNbO3, BaTiO3, PbTiO3) at the experimental lattice parameters/volumes using both WDA sum‑rule variants.

## Reproduction target
Implement the WDA functional as described, then produce two scored output files:

1. **Equilibrium cubic lattice constants** (`lattice_constants.csv`): For KNbO3, KTaO3, SrTiO3, BaTiO3, and PbTiO3, report the lattice constant (in Å) that minimizes the total energy for the LDA, the original WDA, and the new‑sum‑rule WDA. Obtain the numbers from a scan of cubic lattice parameters around the experimental values.

2. **Frozen‑phonon energy curves** (`frozen_phonon_results.csv`): For KNbO3, BaTiO3, and PbTiO3, report the total energy (in mRy) as a function of the soft‑mode atomic displacement (as a fraction of the experimental distortion) for the original WDA and the new‑sum‑rule WDA. The displacements should cover a range from zero to at least 1.2 × the experimental amplitude. Use the experimental lattice parameters/volumes specified in the workflow steps.

The verifier will check that the submitted data follow the expected physical behavior and are consistent with reference results.

## Assets

- Cubic perovskite crystal structures (KNbO3, KTaO3, SrTiO3, BaTiO3, PbTiO3): https://materialsproject.org/
- Troullier-Martins norm-conserving pseudopotentials (K, Nb, O, Ta, Sr, Ti, Ba, Pb): https://www.pseudo-dojo.org/
- Plane-wave DFT code (e.g., ABINIT): https://www.abinit.org/

## Workflow steps

### Step 1: Setup structures and pseudopotentials
- Role: process
- Action: Obtain cubic perovskite crystal structures for KNbO3, KTaO3, SrTiO3, BaTiO3, PbTiO3 with experimental lattice parameters. Obtain or generate Troullier-Martins norm-conserving pseudopotentials for K, Nb, O, Ta, Sr, Ti, Ba, Pb. Configure a plane-wave DFT code to perform LDA calculations.
- Evidence: none

### Step 2: Implement WDA with original sum rule
- Role: process
- Action: Implement the WDA exchange-correlation functional within the chosen DFT code. Use the Perdew-Wang homogeneous-gas pair-distribution function G, shell partitioning (valence-valence WDA, core and semi-core LDA, oxygen 2s with LDA), three-point logarithmic interpolation for the weighted density, and the original sum rule that integrates over the valence density.
- Evidence: none

### Step 3: Implement WDA with new sum rule
- Role: process
- Action: Modify the WDA sum rule to the corrected sum rule that includes the core density, while preserving shell partitioning. Retain the same P-W G and interpolation scheme.
- Evidence: none

### Step 4: Compute equilibrium cubic lattice constants
- Role: scored (load-bearing)
- Action: For each of the five materials, perform a series of total energy calculations at different cubic lattice constants using LDA, WDA-original, and WDA-new functionals. Determine the equilibrium lattice constant (energy minimum) for each method and compile the results in a CSV file.
- Output file: `/app/outputs/lattice_constants.csv`
- Format: csv
- Contract: Columns: material (string), LDA_lattice_constant (float, Å), WDA_original_lattice_constant (float, Å), WDA_new_lattice_constant (float, Å). One row per material (KNbO3, KTaO3, SrTiO3, BaTiO3, PbTiO3).
- Scoring: scored by hidden verifier

### Step 5: Prepare frozen-phonon displaced structures
- Role: process
- Action: For KNbO3, BaTiO3, and PbTiO3, construct atomic configurations displaced along the experimental ferroelectric soft-mode directions (rhombohedral for KNbO3 and BaTiO3; tetragonal for PbTiO3). Use the experimental lattice parameters/volumes: cubic 4.016 Å for KNbO3, 4.000 Å for BaTiO3; tetragonal with c/a=1.0635 and volume 63.28 Å³ for PbTiO3. Displacement amplitudes should cover a range from zero to at least 1.2 times the experimental soft-mode amplitude.
- Evidence: none

### Step 6: Compute frozen-phonon energy curves
- Role: scored
- Action: Perform total energy calculations for each displaced configuration using the WDA-original and WDA-new functionals. Compile the results in a CSV file with columns for material, method, displacement, and total energy.
- Output file: `/app/outputs/frozen_phonon_results.csv`
- Format: csv
- Contract: Columns: material (string), method (string, values 'WDA_original' or 'WDA_new'), displacement (float, fraction of experimental soft-mode displacement), total_energy (float, mRy). Multiple rows per material and method covering the displacement range.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.csv`
- `/app/outputs/frozen_phonon_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.csv
- path: `/app/outputs/lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium cubic lattice constants for five perovskite ferroelectrics computed with LDA and two variants of the WDA functional. The checker compares the WDA values to hidden reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `material`, `LDA_lattice_constant`, `WDA_original_lattice_constant`, `WDA_new_lattice_constant`
  - `units`:
    - `LDA_lattice_constant`: Å
    - `WDA_original_lattice_constant`: Å
    - `WDA_new_lattice_constant`: Å

### frozen_phonon_results.csv
- path: `/app/outputs/frozen_phonon_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Frozen-phonon energy versus displacement curves for three ferroelectric materials with the two WDA sum rules. The checker verifies structural properties (e.g., ferroelectric instability overestimation and its correction) relative to hidden LDA reference curves.
- schema:
  - `type`: table
  - `required_columns`: `material`, `method`, `displacement`, `total_energy`
  - `units`:
    - `displacement`: fraction of experimental soft-mode displacement
    - `total_energy`: mRy

Notes: The task reproduces the headline lattice constant improvements and the correction of ferroelectric instability from a plane-wave WDA implementation. The agent must implement the WDA functional from scratch using an open-source plane-wave DFT code. The LDA frozen-phonon reference curves are hidden gold used by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "LDA_lattice_constant",
          "WDA_original_lattice_constant",
          "WDA_new_lattice_constant"
        ],
        "units": {
          "LDA_lattice_constant": "Å",
          "WDA_original_lattice_constant": "Å",
          "WDA_new_lattice_constant": "Å"
        }
      },
      "description": "Equilibrium cubic lattice constants for five perovskite ferroelectrics computed with LDA and two variants of the WDA functional. The checker compares the WDA values to hidden reference values within tolerances."
    },
    {
      "file": "frozen_phonon_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "method",
          "displacement",
          "total_energy"
        ],
        "units": {
          "displacement": "fraction of experimental soft-mode displacement",
          "total_energy": "mRy"
        }
      },
      "description": "Frozen-phonon energy versus displacement curves for three ferroelectric materials with the two WDA sum rules. The checker verifies structural properties (e.g., ferroelectric instability overestimation and its correction) relative to hidden LDA reference curves."
    }
  ],
  "notes": "The task reproduces the headline lattice constant improvements and the correction of ferroelectric instability from a plane-wave WDA implementation. The agent must implement the WDA functional from scratch using an open-source plane-wave DFT code. The LDA frozen-phonon reference curves are hidden gold used by the checker."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file.

- For `lattice_constants.csv`, the verifier compares the computed WDA lattice constants against reference expectations within a physically motivated tolerance, and checks that the LDA baseline is sensible.
- For `frozen_phonon_results.csv`, the verifier examines the shape of the energy‑displacement curves, the relative well depths and curvatures, and the qualitative trends across materials and sum‑rule choices. It verifies that the curves exhibit the correct structural features without requiring exact numerical agreement.

The final reward is a weighted sum of the scores from the two artifacts. Reporting the paper's numbers without running the actual computation will not satisfy the verifier's structural checks.
