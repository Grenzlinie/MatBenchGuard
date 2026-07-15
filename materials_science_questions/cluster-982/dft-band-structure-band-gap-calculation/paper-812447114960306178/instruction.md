# First-Principles Density of States Peak Calculation for SnS₂

## Problem background
SnS₂ is a layered semiconductor that crystallises in the CdI₂-type hexagonal structure (space group P-3m1). Understanding its electronic density of states (DOS) across a wide energy range — encompassing both the valence and conduction bands — provides insight into the chemical bonding character, optical absorption, and transport properties of this material. First-principles electronic-structure calculations can produce a theoretical DOS curve from which characteristic peak positions are identified; comparing these computed peak energies against experimental photoemission data tests the predictive power of the theoretical model.

## Approach
Perform a plane-wave pseudopotential density-functional-theory (DFT) calculation for bulk SnS₂. Begin from the experimental hexagonal crystal structure, then carry out a self-consistent field (SCF) ground-state calculation followed by a non-self-consistent band-structure and density-of-states computation over a wide energy window that spans the valence bands and the lower conduction bands. From the resulting DOS curve, apply a peak-finding procedure to locate the dominant maxima. Assign labels to the valence-band peaks (A, B, C, D, ordered from the valence-band maximum downward to higher binding energy) and to the conduction-band peaks (d, e, f, g, h, ordered by increasing energy above the valence-band maximum). The calculation uses only publicly available inputs — the crystal structure from standard databases and pseudopotentials from a standard solid-state library — and any mainstream open-source plane-wave DFT package.

## Reproduction target
Compute the electronic density of states of SnS₂ over an energy range spanning at least −10 eV to +20 eV relative to the valence-band maximum and save the raw DOS curve. From this curve, identify the energies (in eV, relative to the valence-band maximum) of the four main valence-band DOS peaks — labelled A, B, C, D with A closest to the valence-band maximum — and of the six main conduction-band DOS peaks — labelled d through h in order of increasing energy. Report the identified peak labels and their energies, and provide the full raw DOS curve so that the peaks can be independently re-derived.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SnS₂ crystal structure: https://materialsproject.org/materials/mp-2295
- Pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT calculation of SnS₂ DOS
- Role: scored (load-bearing)
- Action: Set up the SnS₂ crystal structure (hexagonal, space group P-3m1, lattice parameters a≈3.648 Å, c≈5.899 Å). Using an open-source plane-wave pseudopotential DFT code, perform a self-consistent field calculation followed by a non-self-consistent band-structure and density-of-states computation covering at least -10 eV to +20 eV relative to the valence-band maximum. Compute the DOS and save the raw curve as a CSV file.
- Output file: `/app/outputs/dos_curve.csv`
- Format: csv
- Contract: Two columns: energy_eV (eV relative to VBM) and dos (arbitrary units).
- Scoring: scored by hidden verifier

### Step 2: Peak identification
- Role: scored
- Action: From the DOS curve, identify the energies of the valence-band density-of-states maxima (A, B, C, D, binding energies, negative values) and the conduction-band maxima (d, e, f, g, h, positive values). Use a peak-finding method and assign labels according to expected energy ordering: A uppermost valence, D deepest valence; conduction peaks in increasing energy. Write the assignments and energies as a JSON array.
- Output file: `/app/outputs/dos_peaks.json`
- Format: json
- Contract: Array of objects: {"peak": "A|B|C|D|d|e|f|g|h", "energy_eV": <float>}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_curve.csv`
- `/app/outputs/dos_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_curve.csv
- path: `/app/outputs/dos_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw density of states curve. The hidden checker refits dominant peaks and compares their energies and ordering to the paper's theoretical values.
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `dos`
  - `items`: object
  - `units`:
    - `energy_eV`: eV relative to VBM
    - `dos`: arbitrary

### dos_peaks.json
- path: `/app/outputs/dos_peaks.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Identified peak labels and energies. Checker verifies correct relative ordering and consistency with the refitted peaks from dos_curve.csv.
- schema:
  - `type`: array
  - `required`: object
  - `items`:
    - `peak`: string
    - `energy_eV`: number
  - `required_columns`:
  - `units`:
    - `energy_eV`: eV relative to VBM

Notes: No specific convergence parameters are mandated; the solving agent selects k‑point mesh, energy cutoffs, and smearing. The checker tolerances are designed to absorb legitimate implementation spread while requiring a qualitatively correct DOS.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dos_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "dos"
        ],
        "items": {},
        "units": {
          "energy_eV": "eV relative to VBM",
          "dos": "arbitrary"
        }
      },
      "description": "Raw density of states curve. The hidden checker refits dominant peaks and compares their energies and ordering to the paper's theoretical values."
    },
    {
      "file": "dos_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "required": {},
        "items": {
          "peak": "string",
          "energy_eV": "number"
        },
        "required_columns": [],
        "units": {
          "energy_eV": "eV relative to VBM"
        }
      },
      "description": "Identified peak labels and energies. Checker verifies correct relative ordering and consistency with the refitted peaks from dos_curve.csv."
    }
  ],
  "notes": "No specific convergence parameters are mandated; the solving agent selects k‑point mesh, energy cutoffs, and smearing. The checker tolerances are designed to absorb legitimate implementation spread while requiring a qualitatively correct DOS."
}
```

## How you are scored
A hidden verifier independently checks your two scored outputs. For the raw DOS curve, the verifier refits the dominant peaks from your data and compares their energies and ordering to expected reference values. For your identified peak list, the verifier checks that the labels follow the correct energy ordering (A < B < C < D for the valence peaks, all at negative energies relative to the valence-band maximum; d < e < f < g < h for the conduction peaks, all at positive energies) and that the listed energies are consistent with the peaks the verifier independently refits from your DOS curve. The final reward is a weighted combination of peak-energy accuracy and correct relative ordering; reporting a number is not enough — your raw curve must support your claimed peaks.
