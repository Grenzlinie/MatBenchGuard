# Phonon symmetry decomposition via group theory

## Problem background
The tetragonal-to-monoclinic phase transition in zirconia (ZrO2) is accompanied by large shear and volume strains and is crucial for the mechanical properties of zirconia-based ceramics. Understanding which phonon modes condense at the transition is key to identifying the order parameter that drives the structural change and to explaining how elastic strains arise. This task aims to reproduce the group-theoretical symmetry analysis that determines the phonon irreducible representations in the tetragonal phase and constructs the symmetry-allowed coupling terms in the Landau free energy expansion.

## Approach
The analysis proceeds via group theory using the crystal structure of tetragonal ZrO2 (space group D4h^15) and standard character tables. First, the vibrational modes at the Brillouin zone center (Γ) and the zone boundary M point are decomposed into irreducible representations for the zirconium and oxygen atoms. Eigenvector patterns are obtained via projection operators to identify the nature of each mode. The irreducible representations of the possible order parameters are then examined to determine which combination can drive the transition to the monoclinic phase while being invariant under the low-temperature space group. Finally, the symmetric squares of the relevant representations are reduced to construct symmetry-invariant polynomial terms in the Landau free energy that couple the primary order parameter to symmetry-adapted elastic strains (volume and shear). The result is a deterministic set of irrep labels and coupling terms.

## Reproduction target
Given the tetragonal crystal structure (Teufer, 1962; atomic positions and lattice parameters) and character tables for space group D4h^15, perform group-theoretical analysis at Γ and M points. Determine the irreducible representations of all phonon modes for Zr and O atoms. Identify the primary order parameter from the zone-boundary modes. Construct the symmetry-invariant Landau free energy expansion, including coupling terms between the primary order parameter and elastic strains (e.g., coupling to volume strains and a quadratic coupling to shear strain). Output the complete results as a JSON file, /app/outputs/phonon_analysis_results.json, containing `gamma_modes` (Zr and O irrep arrays), `M_modes` (same), `primary_order_parameter` (string), `secondary_parameter` (string), and `coupling_terms` (list of invariant term descriptions).

## Assets

- Crystal structure of tetragonal ZrO2 (Teufer 1962): 10.1107/S0365110X62002989
- Character tables for space group D4h^15
- spglib (optional): https://pypi.org/project/spglib/
- phonopy (optional): https://pypi.org/project/phonopy/

## Workflow steps

### Step 1: Phonon symmetry decomposition and free energy expansion
- Role: scored (load-bearing)
- Action: Perform group-theoretical analysis of vibrational modes for tetragonal ZrO2 (space group D4h^15) at the Brillouin zone center Γ and zone-boundary M point. Using character tables and atomic positions, compute the irreducible representations and eigenvectors for Zr and O atoms. Determine the primary order parameter (M1+M2) that drives the tetragonal-to-monoclinic transition. Construct the symmetry-invariant Landau free energy expansion, including coupling terms between the primary order parameter and symmetry-adapted elastic strains (volume and shear). Write the complete analysis results to /app/outputs/phonon_analysis_results.json.
- Output file: `/app/outputs/phonon_analysis_results.json`
- Format: json
- Contract: JSON object with keys: 'gamma_modes' (object with keys 'Zr' and 'O', each an array of irrep strings, e.g. 'A2u'), 'M_modes' (same), 'primary_order_parameter' (string, e.g. 'M1+M2'), 'secondary_parameter' (string, e.g. 'E_g'), 'coupling_terms' (array of strings describing each invariant coupling term found).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_analysis_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_analysis_results.json
- path: `/app/outputs/phonon_analysis_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the irreducible representations of phonon modes at Γ and M points for Zr and O atoms, the primary order parameter representation, the secondary order parameter, and the list of symmetry-allowed coupling terms in the Landau free energy. The irrep labels are compared to the paper's reference (order-insensitive exact match); the coupling_terms are checked to contain a quadratic coupling term between the primary order parameter and shear strain (structural audit).
- schema:
  - `type`: object
  - `required`:
    - `gamma_modes`: object
    - `M_modes`: object
    - `primary_order_parameter`: string
    - `secondary_parameter`: string
    - `coupling_terms`: array of strings
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: Only the underlying group-theoretical symmetry analysis (irreps and coupling invariants) is scored. The qualitative triggered-transition interpretation (Stage 3) and the relation to cubic X-point phonons (Stage 4) are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_analysis_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_modes": "object",
          "M_modes": "object",
          "primary_order_parameter": "string",
          "secondary_parameter": "string",
          "coupling_terms": "array of strings"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Contains the irreducible representations of phonon modes at Γ and M points for Zr and O atoms, the primary order parameter representation, the secondary order parameter, and the list of symmetry-allowed coupling terms in the Landau free energy. The irrep labels are compared to the paper's reference (order-insensitive exact match); the coupling_terms are checked to contain a quadratic coupling term between the primary order parameter and shear strain (structural audit)."
    }
  ],
  "notes": "Only the underlying group-theoretical symmetry analysis (irreps and coupling invariants) is scored. The qualitative triggered-transition interpretation (Stage 3) and the relation to cubic X-point phonons (Stage 4) are not scored."
}
```

## How you are scored
Each scored artifact in the workflow is evaluated independently by a hidden verifier. The verifier compares the submitted irrep labels for Zr and O at Γ and M points to a reference set derived from the published analysis (order‑insensitive exact match). It checks that the `primary_order_parameter` string matches the expected representation. It also audits the `coupling_terms` list to confirm that at least one term representing a quadratic coupling between the primary order parameter and shear strain is present. The reward is a weighted combination of these checks; simply reporting reference numbers without performing the actual group‑theoretical analysis will not pass.
