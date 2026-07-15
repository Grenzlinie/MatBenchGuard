# Phonon Frequencies and Grüneisen Parameter of Atomically Thin Boron Nitride via Density Functional Theory

## Problem background
Atomically thin boron nitride (hBN) is a wide‑bandgap two‑dimensional material with exceptional thermal and mechanical properties. Its Raman spectrum provides a key fingerprint for thickness and strain characterization, yet there is ongoing discussion about how the intrinsic Raman‑active E2g phonon frequency changes with the number of layers. Density functional theory (DFT) calculations can predict the vibrational properties and disentangle intrinsic effects from substrate‑induced strain. This task focuses on the first‑principles computational side of that investigation: computing the E2g phonon frequencies for monolayer, few‑layer, and bulk hBN, and determining the Grüneisen parameter that links Raman shifts to applied strain.

## Approach
Use density functional theory with a range‑separated hybrid functional (HSE06) that includes a fraction of exact Hartree‑Fock exchange and van der Waals corrections. For each system—monolayer (1L), bilayer (2L), trilayer (3L), and bulk hBN—perform structural relaxation, then compute the phonon frequencies at the Γ point. Extract the doubly‑degenerate E2g mode frequency. To obtain the Grüneisen parameter for the LO/TO mode at Γ, apply small isotropic strains to monolayer BN, recalculate the E2g frequency, and derive the parameter γ = −(1/ω₀)·(dω/dε). All calculations are performed with open‑source tools: an open‑source DFT code supporting hybrid functionals and a phonon post‑processing package.

## Reproduction target
Compute the Γ‑point E2g phonon frequency (in cm⁻¹) for monolayer, bilayer, trilayer, and bulk hexagonal boron nitride via DFT with the HSE06 hybrid functional and van der Waals corrections. Compute the Grüneisen parameter of the LO/TO mode at Γ from the strain‑dependent frequency shift of monolayer BN. Write the four E2g frequencies to `/app/outputs/E2g_frequencies.csv` (columns: system, frequency_cm1) and the Grüneisen parameter to `/app/outputs/Gruneisen_parameter.txt` (a single floating‑point number on the first line).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Hexagonal boron nitride crystal structure

## Workflow steps

### Step 1: Generate BN structures
- Role: process
- Action: Generate atomic structures for monolayer (1L), bilayer (2L), trilayer (3L), and bulk hexagonal boron nitride using standard lattice parameters. For 2D systems, include sufficient vacuum (>20 Å).
- Evidence: `/app/outputs/structures.log`

### Step 2: DFT relaxation and Γ-point phonon calculation
- Role: process
- Action: For each BN system, perform DFT self-consistent field and structural relaxation using a range-separated hybrid functional (e.g., HSE06 with default mixing) and van der Waals corrections. Then compute phonon frequencies at the Γ point using finite displacements or DFPT, extracting the E2g mode frequency.
- Evidence: `/app/outputs/phonon_calc.log`

### Step 3: Compute Grüneisen parameter
- Role: process
- Action: For monolayer BN, apply small isotropic strain (e.g., ±0.5%) and recalculate the E2g phonon frequency; compute the derivative dω/dε and derive the Grüneisen parameter γ_LO/TO(Γ) = −(1/ω₀)·(dω/dε).
- Evidence: `/app/outputs/gruneisen.log`

### Step 4: Report E2g frequencies
- Role: scored (load-bearing)
- Action: Collect the computed E2g frequencies for 1L, 2L, 3L, and bulk BN and write them to E2g_frequencies.csv with columns 'system' (string) and 'frequency_cm1' (float).
- Output file: `/app/outputs/E2g_frequencies.csv`
- Format: csv
- Contract: Columns: system (string), frequency_cm1 (float)
- Scoring: scored by hidden verifier

### Step 5: Report Grüneisen parameter
- Role: scored (load-bearing)
- Action: Write the computed Grüneisen parameter for the LO/TO mode at Γ to Gruneisen_parameter.txt as a single floating-point number on the first line.
- Output file: `/app/outputs/Gruneisen_parameter.txt`
- Format: txt
- Contract: Single float on the first line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/E2g_frequencies.csv`
- `/app/outputs/Gruneisen_parameter.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### E2g_frequencies.csv
- path: `/app/outputs/E2g_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed E2g phonon frequencies for monolayer, bilayer, trilayer, and bulk BN. The checker compares each frequency against hidden paper-reported HSE06 reference values and verifies that the frequency range across layers is small.
- schema:
  - `type`: table
  - `required_columns`: `system`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm⁻¹

### Gruneisen_parameter.txt
- path: `/app/outputs/Gruneisen_parameter.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Grüneisen parameter for the LO/TO mode at the Γ point, compared to the paper-reported value within a tolerance.
- schema:
  - `type`: text
  - `required`:
    - `first_line`: float
  - `units`:
    - `first_line`: dimensionless

Notes: Reproduction targets only the DFT calculations; experimental Raman and AFM measurements are omitted. The original code (VASP) is proprietary; the task is rescoped to open-source alternatives (Quantum ESPRESSO + Phonopy). The checker compares the computed frequencies and Grüneisen parameter to hidden reference values from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "E2g_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹"
        }
      },
      "description": "Computed E2g phonon frequencies for monolayer, bilayer, trilayer, and bulk BN. The checker compares each frequency against hidden paper-reported HSE06 reference values and verifies that the frequency range across layers is small."
    },
    {
      "file": "Gruneisen_parameter.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {
          "first_line": "float"
        },
        "units": {
          "first_line": "dimensionless"
        }
      },
      "description": "Grüneisen parameter for the LO/TO mode at the Γ point, compared to the paper-reported value within a tolerance."
    }
  ],
  "notes": "Reproduction targets only the DFT calculations; experimental Raman and AFM measurements are omitted. The original code (VASP) is proprietary; the task is rescoped to open-source alternatives (Quantum ESPRESSO + Phonopy). The checker compares the computed frequencies and Grüneisen parameter to hidden reference values from the paper."
}
```

## How you are scored
A hidden verifier examines the output files you produce. For `E2g_frequencies.csv`, the verifier checks that the reported frequencies are consistent with no systematic dependence on layer number and compares them against reference values from published HSE06 calculations. For `Gruneisen_parameter.txt`, the verifier compares your reported value to a reference. Each scored artifact contributes a weighted portion to the final reward, which is a number between 0 and 1. Simply reporting a number without executing the required DFT and phonon steps will not earn full credit.
