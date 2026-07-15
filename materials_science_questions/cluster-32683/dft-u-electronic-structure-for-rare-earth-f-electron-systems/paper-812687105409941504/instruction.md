# LDA Electronic Structure Calculation for Layered Borocarbide Superconductor

## Problem background
Layered rare-earth borocarbide superconductors such as LaPt2B2C combine quasi-two-dimensional crystal structures with three-dimensional electronic properties. Density functional calculations in the local density approximation (LDA) provide a first-principles route to the electronic density of states (DOS), which is central to understanding superconducting properties, because the DOS at the Fermi level N(E_F) directly influences the critical temperature T_c. The key open questions for LaPt2B2C are: what is the total DOS profile near the Fermi energy, what is the value of N(E_F), and where does E_F lie with respect to the nearest peak in the DOS? Answering these questions is essential for assessing whether electron doping could raise T_c.

## Approach
Use an open-source plane-wave pseudopotential DFT code to perform a self-consistent LDA calculation for LaPt2B2C. Employ the experimental crystal structure (space group I4/mmm) and standard LDA pseudopotentials for La, Pt, B, and C. A widely used choice is the Hedin-Lundqvist exchange-correlation functional, but any standard LDA functional is acceptable. After converging the charge density, compute the total electronic DOS on a fine energy grid covering at least −0.5 to +0.5 Ry around the Fermi level. Extract N(E_F) directly from the DOS. The results will be compared against the known value for the chemically related superconductor LuNi2B2C (N(E_F) ≈ 65.3 states/(Ry·f.u.)) to assess how the DOS differs between the two materials. Additionally, analyze the DOS curve to determine whether E_F sits at a maximum or on the low-energy side of a peak.

## Reproduction target
Produce two artifacts from your LDA calculation for LaPt2B2C: 
- `dos_curve.csv`: a CSV file with two columns, `energy_relative` (Ry, relative to E_F) and `dos_total` (states/(Ry·f.u.)), covering at least −0.5 to +0.5 Ry with an energy step no larger than 0.001 Ry. The curve must have sufficient resolution to clearly locate any DOS peak near E_F.
- `n_ef.txt`: a plain-text file containing a single floating-point number, the total DOS at E_F (N(E_F)), in units of states/(Ry·f.u.).
The DOS curve will be inspected for the relative position of E_F with respect to the nearest maximum. Your computed N(E_F) should be substantially lower than the published LuNi2B2C value of 65.3 states/(Ry·f.u.). Do NOT run a separate calculation for LuNi2B2C; only LaPt2B2C is required for this task.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org
- LDA pseudopotentials for La, Pt, B, C: https://www.quantum-espresso.org/pseudopotentials
- Crystal structure of LaPt2B2C: 10.1038/367252a0

## Workflow steps

### Step 1: Prepare crystal structure input
- Role: process
- Action: Obtain the experimental crystal structure of LaPt2B2C (space group I4/mmm) from a public database or literature reference and generate the input file for a DFT calculation.
- Evidence: `/app/outputs/structure_input.txt`

### Step 2: Self-consistent LDA calculation
- Role: process
- Action: Run a self-consistent LDA calculation using an open-source DFT code (e.g., Quantum ESPRESSO) with the prepared crystal structure and appropriate LDA pseudopotentials. Converge the charge density to obtain the Kohn-Sham potential.
- Evidence: `/app/outputs/scf_log.txt`

### Step 3: Compute total DOS curve
- Role: scored (load-bearing)
- Action: Using the self-consistent Kohn-Sham potential, compute the total density of states (DOS) on a fine energy grid covering at least -0.5 to +0.5 Ry around the Fermi level. Save the result as a CSV file.
- Output file: `/app/outputs/dos_curve.csv`
- Format: csv
- Contract: CSV with header: energy_relative (float, Ry relative to EF), dos_total (float, states/(Ry per formula unit)). The energy grid must cover at least -0.5 to +0.5 Ry with a step no coarser than 0.001 Ry.
- Scoring: scored by hidden verifier

### Step 4: Extract N(EF)
- Role: scored
- Action: From the total DOS curve, extract the value of the density of states at the Fermi energy (energy_relative = 0) and write it to a text file.
- Output file: `/app/outputs/n_ef.txt`
- Format: txt
- Contract: A single floating-point number as text (e.g., 33.9). No units inside the file; understood as states/(Ry·f.u.).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dos_curve.csv`
- `/app/outputs/n_ef.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dos_curve.csv
- path: `/app/outputs/dos_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total density of states curve. The checker will verify that the Fermi energy lies on the low-energy side of a DOS peak and that N(EF) is lower than the peak maximum within 0.1 Ry above EF.
- schema:
  - `type`: table
  - `required_columns`: `energy_relative`, `dos_total`
  - `units`:
    - `energy_relative`: Ry (relative to EF)
    - `dos_total`: states/(Ry per formula unit)

### n_ef.txt
- path: `/app/outputs/n_ef.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Density of states at the Fermi level. The value will be compared to the paper's reported gold and must be consistent with the DOS curve (self-consistency check).
- schema:
  - `type`: text
  - `required`: None

Notes: The dos_curve.csv must have sufficient resolution (step ≤ 0.001 Ry) to reliably locate the DOS peak. The n_ef.txt value must match the DOS value at energy_relative=0 within numerical precision.

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
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_relative",
          "dos_total"
        ],
        "units": {
          "energy_relative": "Ry (relative to EF)",
          "dos_total": "states/(Ry per formula unit)"
        }
      },
      "description": "Total density of states curve. The checker will verify that the Fermi energy lies on the low-energy side of a DOS peak and that N(EF) is lower than the peak maximum within 0.1 Ry above EF."
    },
    {
      "file": "n_ef.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": null
      },
      "description": "Density of states at the Fermi level. The value will be compared to the paper's reported gold and must be consistent with the DOS curve (self-consistency check)."
    }
  ],
  "notes": "The dos_curve.csv must have sufficient resolution (step ≤ 0.001 Ry) to reliably locate the DOS peak. The n_ef.txt value must match the DOS value at energy_relative=0 within numerical precision."
}
```

## How you are scored
A hidden verifier reads your `dos_curve.csv` and `n_ef.txt`. It performs several independent checks, each contributing to a combined reward score:
- It extracts N(E_F) from `n_ef.txt` and verifies numerical self-consistency with the DOS value at `energy_relative = 0`.
- It compares your N(E_F) against a hidden reference value derived from the original paper (the gold is not disclosed in the task instructions). The comparison uses a tolerance that accounts for legitimate spread due to different pseudopotentials and DFT codes; an honest re-run of the prescribed LDA procedure is expected to fall within the tolerance.
- It verifies that your N(E_F) is substantially smaller than the LuNi2B2C baseline (65.3 states/(Ry·f.u.)) by a predefined margin.
- It examines the DOS curve to confirm that E_F lies on the low-energy side of a peak: within a small energy window above E_F the DOS increases, and N(E_F) is less than the maximum DOS in that window.
All checks must be satisfied to obtain full credit; the N(E_F) comparison carries the largest weight. Simply printing a guessed number is unlikely to pass all structural and self-consistency criteria.
