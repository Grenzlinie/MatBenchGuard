# Phonon symmetry decomposition via group theory

## Problem background
The linear-chain compound (TaSe4)2I exhibits a Peierls transition at lower temperatures, but in its room-temperature phase it crystallizes in a tetragonal structure (space group I422, point group D4) with 22 atoms per primitive cell. The resulting 66 vibrational degrees of freedom at the Brillouin-zone centre give rise to a complex Raman and infrared spectrum. To interpret these spectra, it is essential to know the symmetry decomposition of the zone-centre phonons: the irreducible representations they span, which modes are acoustic or optical, which are Raman-active and/or infrared-active, and the polarizability tensor forms that govern the Raman selection rules. This task addresses that open computation: using the known crystal structure and site symmetries, determine the complete group-theoretical breakdown of the Γ-point lattice vibrations.


## Approach
The analysis uses the correlation (factor-group) method, a standard group-theoretical tool that relates the point symmetries of individual atomic sites to the irreducible representations of the crystal's factor group. Starting from the crystal structure, one identifies the site symmetry of each distinct atom (Ta on D2 sites, I on C4, Se on C1). The total vibrational representation is built from the mechanical character contributed by each site under the operations of point group D4. Reducing this representation with the D4 character table yields the multiplicities of the A1, A2, B1, B2, and E irreps. The three acoustic modes are then identified (one A2 translation along the c axis and one doubly-degenerate E mode for translations in the basal plane). The remaining 63 optical modes are separated into purely infrared-active (A2) and Raman-active representations (A1, B1, B2, E; note that E is also infrared-active). Finally, for each Raman-active irrep the expected polarizability tensor form—proportional to the non-zero matrix elements allowed by symmetry—is provided in the crystallographic (x, y, z) axis system.


## Reproduction target
Using the room-temperature crystal structure of (TaSe4)2I as the sole structural input, compute the irreducible representation decomposition of the zone-centre vibrational modes by the correlation method. Specifically:
- Produce the integer multiplicities for A1, A2, B1, B2, and E.
- Confirm that the total number of modes sums to 66.
- Identify the acoustic modes (one A2 and one doubly-degenerate E).
- Classify the optical modes into those that are purely IR-active (A2 symmetry) and those that are Raman-active (A1, B1, B2, E), noting that the E modes are also IR-active.
- Output the Raman polarizability tensor forms (3×3 matrices proportional to the symmetry-allowed non-zero elements) for each Raman-active representation; for E, supply the two required matrices.
The result must be written to `/app/outputs/decomposition_results.json` following the exact schema defined in the output contract.


## Assets

- Crystal structure of (TaSe4)2I (Gressier et al. 1982): 10.1107/S0567740882009995
- Bilbao Crystallographic Server: https://www.cryst.ehu.es/

## Workflow steps

### Step 1: Group-theoretical decomposition of zone-centre phonon modes
- Role: scored (load-bearing)
- Action: Given the room-temperature crystal structure of (TaSe4)2I (tetragonal, space group I422, point group D4, 22 atoms per primitive cell, atomic site symmetries: Ta at D2, I at C4, Se at C1), use the correlation (factor-group) method and the D4 character table to decompose the total vibrational representation at the Brillouin-zone centre into irreducible representations. Compute the multiplicities for A1, A2, B1, B2, E. Identify the three acoustic modes (one A2 and one doubly-degenerate E) and classify the remaining 63 optical modes into purely infrared-active A2 modes and Raman-active representations A1, B1, B2, E (with E also infrared-active). Provide the Raman polarizability tensor forms for each Raman-active representation as given by the symmetry representations (diagonal/off-diagonal proportional matrices).
- Output file: `/app/outputs/decomposition_results.json`
- Format: json
- Contract: JSON object with keys: 'irrep_decomposition' (object with integer counts for A1, A2, B1, B2, E), 'total_modes' (integer, must be 66), 'acoustic_modes' (object with integer counts for A2=1 and E=2), 'optical_modes' (object with 'IR_active' = {A2: integer count}, 'Raman_active' = {A1, B1, B2, E integer counts}, and a boolean 'E_also_IR_active' = true), 'raman_tensor_forms' (object with keys 'A1', 'B1', 'B2', 'E' where each value is a 3×3 array of numbers representing the proportional tensor matrix; 'E' is an array of two 3×3 matrices).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/decomposition_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### decomposition_results.json
- path: `/app/outputs/decomposition_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Scored artifact containing the full group-theoretical decomposition and Raman tensor forms.
- schema:
  - `type`: object
  - `required`:
    - `irrep_decomposition`:
      - `type`: object
      - `description`: Multiplicities of irreducible representations A1, A2, B1, B2, E
    - `total_modes`:
      - `type`: integer
      - `description`: Total number of vibrational degrees of freedom (66)
    - `acoustic_modes`:
      - `type`: object
      - `description`: Acoustic mode irreps with degeneracies (A2=1, E=2)
    - `optical_modes`:
      - `type`: object
      - `description`: Optical mode classification including IR_active (A2 count), Raman_active (A1, B1, B2, E counts), and boolean note E_also_IR_active
    - `raman_tensor_forms`:
      - `type`: object
      - `description`: Raman polarizability tensor forms for A1, B1, B2, E (E has two matrices)
  - `notes`: The checker will recompute the decomposition from the public structural information and compare the integer multiplicities exactly and the Raman tensor forms for structural pattern correctness.

Notes: The agent must produce the decomposition from first principles using the correlation method; the checker will independently recompute the decomposition and verify integer counts and tensor patterns. No numeric convergence tolerances apply to integer counts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "decomposition_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "irrep_decomposition": {
            "type": "object",
            "description": "Multiplicities of irreducible representations A1, A2, B1, B2, E"
          },
          "total_modes": {
            "type": "integer",
            "description": "Total number of vibrational degrees of freedom (66)"
          },
          "acoustic_modes": {
            "type": "object",
            "description": "Acoustic mode irreps with degeneracies (A2=1, E=2)"
          },
          "optical_modes": {
            "type": "object",
            "description": "Optical mode classification including IR_active (A2 count), Raman_active (A1, B1, B2, E counts), and boolean note E_also_IR_active"
          },
          "raman_tensor_forms": {
            "type": "object",
            "description": "Raman polarizability tensor forms for A1, B1, B2, E (E has two matrices)"
          }
        },
        "notes": "The checker will recompute the decomposition from the public structural information and compare the integer multiplicities exactly and the Raman tensor forms for structural pattern correctness."
      },
      "description": "Scored artifact containing the full group-theoretical decomposition and Raman tensor forms."
    }
  ],
  "notes": "The agent must produce the decomposition from first principles using the correlation method; the checker will independently recompute the decomposition and verify integer counts and tensor patterns. No numeric convergence tolerances apply to integer counts."
}
```

## How you are scored
A hidden verifier independently recomputes the group-theoretical decomposition from the same public structural information and compares your output. The verifier checks:
- Exact integer match for the irreducible representation multiplicities.
- Correct identification of the acoustic modes (A2 and E counts).
- Correct split of the optical modes into IR-active and Raman-active representations, including that E is also IR-active.
- Structural correctness of the Raman tensor forms (the pattern of zero and non-zero matrix elements; proportional constants are not compared).
The verifier combines these checks into a final score between 0 and 1. Reporting numbers alone is not sufficient; the submitted JSON must be consistent with a properly executed group-theoretical analysis.
