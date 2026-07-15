# Dy Intrinsic Quadrupole Moment from GDR and Experimental Data

## Problem background
Photon scattering off deformed nuclei exhibits a Giant Dipole Resonance (GDR) that splits into two peaks because of the nuclear deformation. The ratio of the two peak energies reflects the nucleus's shape and can be used to extract its intrinsic quadrupole moment Q0, a measure of how far the nuclear charge distribution departs from spherical symmetry. For natural dysprosium (Dy), no direct GDR measurements exist because of its many stable isotopes. This task exploits the fact that the GDR of Dy is expected to closely resemble that of the neighbouring nucleus 160Gd. By using the known 160Gd GDR peak energies, one can predict Dy's Q0. Separately, published experimental B(E2) and static quadrupole moments for the individual Dy isotopes, weighted by their natural abundances, provide an independent experimental determination of the same quantity. Reproducing both calculations and verifying that the two independent estimates agree constitutes the quantitative core of this work.

## Approach
The computation proceeds along two independent paths that both yield an intrinsic quadrupole moment for natural Dy. In the first path, you use the two GDR peak energies E1 and E2 from 160Gd. The axis ratio d (long axis to short axis) is obtained from the Danos relation, which links the ratio of the GDR peak energies to d. Once d is known, Q0 follows from the standard nuclear quadrupole formula involving the atomic number Z, the mass number A (averaged over the natural isotopic composition of Dy), and the nuclear radius parameter r0. In the second path, you process the tabulated data for each stable Dy isotope. For even-mass isotopes the intrinsic quadrupole moment is derived from the reduced electric quadrupole transition probability B(E2) to the first excited state. For odd-mass isotopes it is derived from the measured static quadrupole moment Q by applying a spin-dependent conversion factor that depends on the ground-state spin I0. Weighting each isotope's intrinsic Q0 by its natural abundance yields the average experimental Q0 for the element. Finally, the two Q0 values are compared to assess whether they are mutually consistent. All necessary numerical inputs (the 160Gd GDR energies and the Dy isotope data) are provided as CSV files; no external literature is needed.

## Reproduction target
Using the provided GDR_parameters_160Gd.csv and Dy_isotope_data.csv, compute and deliver three artifacts under /app/outputs:
1. Q0_GDR.txt – the intrinsic quadrupole moment of natural Dy predicted from the 160Gd GDR parameters.
2. Q0_experimental.txt – the abundance-weighted intrinsic quadrupole moment obtained from the experimental B(E2) and static quadrupole values for the Dy isotopes.
3. comparison_report.txt – a brief report that cites both computed Q0 values and states whether they agree within 0.05 b. The specific format of each output file is described in the workflow steps and output contract.

## Assets

- GDR_parameters_160Gd.csv
- Dy_isotope_data.csv

## Workflow steps

### Step 1: Compute Q0 from GDR parameters
- Role: scored (load-bearing)
- Action: Load the GDR parameters E1 and E2 from GDR_parameters_160Gd.csv. Solve the axis-ratio relation 0.911*d + 0.089 = E2/E1 for d. Compute the intrinsic quadrupole moment Q0 = (2/5) * Z * r0^2 * A^(2/3) * (d^2 - 1) / d^(2/3) with Z=66, A=162.5 (average natural Dy), r0=1.2 fm. Write the resulting value to /app/outputs/Q0_GDR.txt.
- Output file: `/app/outputs/Q0_GDR.txt`
- Format: txt
- Contract: Single line containing the value in the format: Q0 = X.XX b
- Scoring: scored by hidden verifier

### Step 2: Compute Q0 from experimental moments
- Role: scored (load-bearing)
- Action: Load Dy_isotope_data.csv. For each isotope, extract its abundance, ground-state spin I0, and either B(E2) (even A) or static quadrupole moment Q (odd A). Convert to intrinsic Q0: for even A, Q0 = sqrt((16π/5) * (B(E2)/e^2)); for odd A, Q0 = ((I0+1)*(2*I0+3))/(I0*(2*I0-1)) * Q. Compute the abundance-weighted average of these Q0 values. Write the weighted average to /app/outputs/Q0_experimental.txt.
- Output file: `/app/outputs/Q0_experimental.txt`
- Format: txt
- Contract: Single line containing the value in the format: Q0 = X.XX b
- Scoring: scored by hidden verifier

### Step 3: Compare Q0 values and produce report
- Role: scored
- Action: Obtain the two Q0 values (by reading the output files or recomputing). Calculate the absolute difference. Produce a report stating the GDR-derived Q0, the experimental Q0, and a conclusion on whether the difference is within 0.05 b. Write to /app/outputs/comparison_report.txt.
- Output file: `/app/outputs/comparison_report.txt`
- Format: txt
- Contract: Three lines: the first line 'GDR-derived Q0: X.XX b', the second line 'Experimental Q0: X.XX b', and a third line stating the absolute difference and whether the values agree within 0.05 b.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Q0_GDR.txt`
- `/app/outputs/Q0_experimental.txt`
- `/app/outputs/comparison_report.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Q0_GDR.txt
- path: `/app/outputs/Q0_GDR.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed intrinsic quadrupole moment from the 160Gd GDR parameters. The hidden checker will extract the numeric value and compare it against the paper's reported value with tolerance.
- schema:
  - `type`: text
  - `format`: single numeric value with label 'Q0 = X.XX b'

### Q0_experimental.txt
- path: `/app/outputs/Q0_experimental.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed abundance-weighted experimental intrinsic quadrupole moment. The hidden checker will extract the numeric value and compare it against the paper's reported value with tolerance.
- schema:
  - `type`: text
  - `format`: single numeric value with label 'Q0 = X.XX b'

### comparison_report.txt
- path: `/app/outputs/comparison_report.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: A report containing the two Q0 values and a statement of agreement within 0.05 b. The checker will verify that the reported values match the values in the other two files and that the agreement conclusion is correct.
- schema:
  - `type`: text
  - `required_lines`: `GDR-derived Q0:`, `Experimental Q0:`, `difference and agreement statement`

Notes: All outputs must be plain text files with the specified format. The agent should use the provided public CSV data files and apply the deterministic formulas described in the steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Q0_GDR.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single numeric value with label 'Q0 = X.XX b'"
      },
      "description": "The computed intrinsic quadrupole moment from the 160Gd GDR parameters. The hidden checker will extract the numeric value and compare it against the paper's reported value with tolerance."
    },
    {
      "file": "Q0_experimental.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "format": "single numeric value with label 'Q0 = X.XX b'"
      },
      "description": "The computed abundance-weighted experimental intrinsic quadrupole moment. The hidden checker will extract the numeric value and compare it against the paper's reported value with tolerance."
    },
    {
      "file": "comparison_report.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required_lines": [
          "GDR-derived Q0:",
          "Experimental Q0:",
          "difference and agreement statement"
        ]
      },
      "description": "A report containing the two Q0 values and a statement of agreement within 0.05 b. The checker will verify that the reported values match the values in the other two files and that the agreement conclusion is correct."
    }
  ],
  "notes": "All outputs must be plain text files with the specified format. The agent should use the provided public CSV data files and apply the deterministic formulas described in the steps."
}
```

## How you are scored
A hidden verifier independently recomputes the intrinsic quadrupole moments from the same GDR and isotope data, using identical relations. It compares your submitted Q0 values (as read from the output files) against its independently derived values with appropriate tolerances. It also examines the comparison report for correctness: the report must quote the values found in the other two files and correctly judge whether they agree within the specified bound. Your score is the weighted combination of how well your computed values match the hidden independently recomputed values and how accurately you report the agreement conclusion. Simply copying the paper's reported numbers without performing the computation from the data will not yield a passing score.
