# LSDA+U+SO Electronic Structure for RE5Ge3 Intermetallics

## Problem background
Rare-earth intermetallic compounds RE5Ge3 (RE = La, Ce, Pr, Nd) crystallize in the hexagonal Mn5Si3-type structure (space group P6_3/mcm) and display complex magnetic behaviour originating from the 4f electrons. First-principles electronic-structure calculations can elucidate the structural and magnetic properties of these materials, but a faithful description requires going beyond standard local density approximations: Hubbard U corrections capture on-site correlation of the 4f states, and spin-orbit coupling (SOC) is needed to account for relativistic effects. This reproduction task computes equilibrium lattice constants and magnetic moments for the whole series using an open-source DFT framework, providing a quantitative test of whether LSDA+U+SO calculations can describe the ground-state properties of these intermetallics.

## Approach
We use density functional theory (DFT) with the LSDA+U approach to treat the strong correlation of the rare-earth 4f electrons. For each compound, the initial hexagonal crystal structure (space group P6_3/mcm) with atomic positions for the two RE sites (4d and 6g) and the Ge site (6g) can be obtained from the Crystallography Open Database or from published crystal data. First, a variable-cell structural relaxation is performed within LSDA+U without spin-orbit coupling to determine the equilibrium lattice parameters a and c. Next, starting from the relaxed geometry, a self-consistent LSDA+U+SO calculation is run (same Hubbard U values) to obtain the ground-state electronic structure, from which the total spin magnetic moment is extracted. The Hubbard U parameters (in eV) are fixed to the following values:
  - La (5d): 0.531
  - Ce (4f): 1.619
  - Pr (4f): 2.332
  - Nd (4f): 2.403
All calculations are carried out with the open-source Quantum ESPRESSO code.

## Reproduction target
Produce a single JSON file `results.json` containing the following quantities for each of the four compounds (La5Ge3, Ce5Ge3, Pr5Ge3, Nd5Ge3):
- `name`: compound identifier string.
- `a`: equilibrium lattice parameter a in angstroms (from the LSDA+U relaxation).
- `c`: equilibrium lattice parameter c in angstroms (from the LSDA+U relaxation).
- `total_magnetic_moment`: total spin magnetic moment in μB per formula unit (from the LSDA+U+SO self-consistent calculation). For the nonmagnetic La5Ge3, this value must be 0.0.
All values must be derived from your first-principles workflow; the verifier compares them to a hidden reference.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Crystallography Open Database: https://www.crystallography.net/cod/

## Workflow steps

### Step 1: LSDA+U structural relaxation
- Role: process
- Action: For each compound (La5Ge3, Ce5Ge3, Pr5Ge3, Nd5Ge3), using the Hubbard U values provided in the instructions and initial crystal structure with space group P6_3/mcm, perform a variable-cell relaxation with LSDA+U (no spin-orbit coupling) to obtain equilibrium lattice constants a and c.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: LSDA+U+SO magnetic moments and compiled results
- Role: scored (load-bearing)
- Action: For each compound, using the relaxed structure from the 'relax' step, run an LSDA+U+SO self-consistent calculation with the same Hubbard U and compute the total spin magnetic moment. Write a single results.json containing for each compound: name, equilibrium lattice constants a and c (from the relaxation), and total_magnetic_moment (from LSDA+U+SO). La5Ge3 is expected to be nonmagnetic (moment 0.0).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"compounds": [{"name": "string", "a": float, "c": float, "total_magnetic_moment": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored artifact: equilibrium lattice parameters a, c from LSDA+U relaxation, and total spin magnetic moment from LSDA+U+SO for each compound. Checker compares a and c to paper reference within 2% relative tolerance, magnetic moments within absolute tolerances and monotonic trend Ce<Pr<Nd.
- schema:
  - `type`: object
  - `required`:
    - `compounds`: array of per-compound objects
  - `items`:
    - `name`: string
    - `a`: number (Å)
    - `c`: number (Å)
    - `total_magnetic_moment`: number (μB)
  - `units`:
    - `a`: Å
    - `c`: Å
    - `total_magnetic_moment`: μB

Notes: All values must be derived from the described first-principles workflow; no external lookup of reference numbers is required or intended. The checker will perform a result-level comparison using hidden gold values from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "compounds": "array of per-compound objects"
        },
        "items": {
          "name": "string",
          "a": "number (Å)",
          "c": "number (Å)",
          "total_magnetic_moment": "number (μB)"
        },
        "units": {
          "a": "Å",
          "c": "Å",
          "total_magnetic_moment": "μB"
        }
      },
      "description": "Scored artifact: equilibrium lattice parameters a, c from LSDA+U relaxation, and total spin magnetic moment from LSDA+U+SO for each compound. Checker compares a and c to paper reference within 2% relative tolerance, magnetic moments within absolute tolerances and monotonic trend Ce<Pr<Nd."
    }
  ],
  "notes": "All values must be derived from the described first-principles workflow; no external lookup of reference numbers is required or intended. The checker will perform a result-level comparison using hidden gold values from the paper."
}
```

## How you are scored
An automated verifier checks the submitted `results.json` against a hidden reference. For each compound, the lattice parameters a and c are compared within a relative tolerance, and the total magnetic moments within an absolute tolerance. Additionally, the verifier verifies that the magnetic moments across the three magnetic compounds follow a monotonic trend (Ce < Pr < Nd). Partial credit is awarded based on the fraction of checks that pass.
