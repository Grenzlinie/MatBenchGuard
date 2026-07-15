# DFT Interband Optical Conductivity of GdPtBi: Linearity Test for Chemical Potential at Triple Point

## Problem background
The half‑Heusler compound GdPtBi displays a nearly linear optical conductivity in the far‑infrared, a feature often associated with three‑dimensional linear electronic bands and band crossings near the chemical potential. First‑principles calculations have identified triple points – band crossings of one doubly degenerate and one non‑degenerate band – in the electronic structure of GdPtBi. The question is whether interband transitions in the vicinity of these triple points can account for the observed low‑energy linear conductivity and whether the best linear behaviour occurs when the chemical potential sits exactly at a triple point. This task reproduces the computational part of that investigation by computing the interband optical conductivity from the band structure, testing the role of the chemical potential position.

## Approach
First, the electronic band structure of GdPtBi is obtained from a density‑functional theory (DFT) calculation including spin‑orbit coupling, using a paramagnetic treatment and the GGA functional. From the resulting Kohn–Sham eigenvalues and wavefunctions, the real part of the interband optical conductivity σ₁(ω) is computed via the Kubo‑Greenwood formula with tetrahedron integration on a dense k‑mesh. The calculation is performed for two different chemical potentials: µ = 0 (Fermi level at the triple point) and µ = +30 meV (Fermi level shifted upward relative to the triple point). The spectra are then compared over the frequency range 50–800 cm⁻¹. The aim is to determine which chemical potential yields the most linear low‑energy conductivity with a near‑zero intercept and without large low‑frequency peaks.

## Reproduction target
Compute the real part of the interband optical conductivity σ₁(ω) of GdPtBi from first‑principles band‑structure data, for both µ = 0 and µ = +30 meV, over the range 0–1000 cm⁻¹. From the two spectra, identify which chemical potential gives the most linear behaviour in the 50–800 cm⁻¹ window with a near‑zero intercept. The deliverables are two CSV files containing the conductivity curves and a one‑line verdict file summarising the outcome.

## Assets

- GdPtBi crystal structure (half‑Heusler F‑43m)
- DFT code supporting spin‑orbit coupling: https://www.quantum-espresso.org/
- Optical conductivity post‑processing tool: boltztrap

## Workflow steps

### Step 1: DFT band structure calculation
- Role: process
- Action: Perform a spin–orbit DFT calculation for GdPtBi (paramagnetic state, GGA functional) to obtain the electronic band structure. Generate Kohn–Sham eigenvalues and wavefunctions over a dense k‑grid. This step produces the band energies and wavefunctions required for the optical conductivity computations.
- Evidence: none

### Step 2: Compute optical conductivity for μ = 0
- Role: scored (load-bearing)
- Action: From the DFT band structure and dipole matrix elements, compute the real part of the interband optical conductivity σ₁(ω) for chemical potential μ = 0 (Fermi level at the triple point). Use the Kubo‑Greenwood formalism with tetrahedron integration on a dense k‑mesh. Cover the frequency range 0–1000 cm⁻¹. Save the spectrum as a two‑column CSV.
- Output file: `/app/outputs/conductivity_mu0.csv`
- Format: csv
- Contract: Columns: frequency_cm-1 (float), sigma1 (float, in 1/Ohm*cm).
- Scoring: scored by hidden verifier

### Step 3: Compute optical conductivity for μ = +30 meV
- Role: scored
- Action: Repeat the σ₁(ω) computation with the chemical potential shifted to μ = +30 meV relative to the triple point. Save the spectrum as a two‑column CSV.
- Output file: `/app/outputs/conductivity_mu30.csv`
- Format: csv
- Contract: Columns: frequency_cm-1 (float), sigma1 (float, in 1/Ohm*cm).
- Scoring: scored by hidden verifier

### Step 4: Identify best chemical potential
- Role: scored
- Action: Compare the two computed conductivity spectra (μ=0 and μ=+30 meV) in the 50–800 cm⁻¹ range. Determine which one yields the most linear behavior with near‑zero intercept. Write the conclusion as a single line to summary.txt.
- Output file: `/app/outputs/summary.txt`
- Format: txt
- Contract: A single line, either 'best_mu=0' or 'best_mu=other', no extra whitespace.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/conductivity_mu0.csv`
- `/app/outputs/conductivity_mu30.csv`
- `/app/outputs/summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### conductivity_mu0.csv
- path: `/app/outputs/conductivity_mu0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real part of the interband optical conductivity for chemical potential μ = 0, covering 0–1000 cm⁻¹. The verifier compares structural features (linearity, intercept, peak presence) with the other condition.
- schema:
  - `type`: table
  - `required_columns`: `frequency_cm-1`, `sigma1`
  - `units`:
    - `frequency_cm-1`: cm^-1
    - `sigma1`: 1/(Ohm*cm)

### conductivity_mu30.csv
- path: `/app/outputs/conductivity_mu30.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Real part of the interband optical conductivity for μ = +30 meV, covering 0–1000 cm⁻¹. The verifier compares structural features (linearity, intercept, peak presence) with the other condition.
- schema:
  - `type`: table
  - `required_columns`: `frequency_cm-1`, `sigma1`
  - `units`:
    - `frequency_cm-1`: cm^-1
    - `sigma1`: 1/(Ohm*cm)

### summary.txt
- path: `/app/outputs/summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Verdict on which chemical potential gives the best linear low‑energy conductivity. The content must be consistent with the structural evaluation of the two CSV files.
- schema:
  - `type`: text

Notes: The verification method is T3 structural: For each CSV, the checker evaluates linearity (slope sign, intercept) and peak presence in the 50–800 cm⁻¹ range. It compares the two conditions and checks that summary.txt is consistent with the observed structural differences. No absolute tolerances or expected outcomes are exposed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "conductivity_mu0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_cm-1",
          "sigma1"
        ],
        "units": {
          "frequency_cm-1": "cm^-1",
          "sigma1": "1/(Ohm*cm)"
        }
      },
      "description": "Real part of the interband optical conductivity for chemical potential μ = 0, covering 0–1000 cm⁻¹. The verifier compares structural features (linearity, intercept, peak presence) with the other condition."
    },
    {
      "file": "conductivity_mu30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_cm-1",
          "sigma1"
        ],
        "units": {
          "frequency_cm-1": "cm^-1",
          "sigma1": "1/(Ohm*cm)"
        }
      },
      "description": "Real part of the interband optical conductivity for μ = +30 meV, covering 0–1000 cm⁻¹. The verifier compares structural features (linearity, intercept, peak presence) with the other condition."
    },
    {
      "file": "summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Verdict on which chemical potential gives the best linear low‑energy conductivity. The content must be consistent with the structural evaluation of the two CSV files."
    }
  ],
  "notes": "The verification method is T3 structural: For each CSV, the checker evaluates linearity (slope sign, intercept) and peak presence in the 50–800 cm⁻¹ range. It compares the two conditions and checks that summary.txt is consistent with the observed structural differences. No absolute tolerances or expected outcomes are exposed to the agent."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines each output artifact independently. For the conductivity CSV files, the verifier performs a structural audit: it fits a straight line to the data in the 50–800 cm⁻¹ range, measures linearity and intercept, and checks for a pronounced peak below 200 cm⁻¹. It then compares the two chemical‑potential conditions and verifies that the summary.txt file is consistent with the observed structural differences. The per‑stage scores are combined into a final reward in the range [0,1]. Because of run‑to‑run variability from different DFT implementations, the audit focuses on robust trends and structural properties rather than exact numerical agreement.
