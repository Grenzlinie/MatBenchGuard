# Calcium FCC and BCC Electronic Properties under Compression

## Problem background
Alkaline-earth metals such as calcium can undergo structural phase transitions and significant changes in electronic properties under high pressure. Understanding how compression affects the density of states at the Fermi level, the plasma frequency, and the band gap in different crystal structures is important for interpreting electrical resistivity measurements. First-principles density functional theory (DFT) can predict these electronic properties, providing insight into whether a material remains metallic or becomes semiconducting under compression.

## Approach
Perform full-potential linearized augmented plane wave (FP-LAPW) DFT calculations for calcium in the face-centered cubic (FCC) and body-centered cubic (BCC) phases. For each phase, systematically vary the specific volume ratio V/V0 (where V0 is the ambient-pressure volume) to simulate compression. At each volume, compute the electronic density of states at the Fermi level N(EF), the plasma frequency ω_pl, and the band gap. Use an open-source FP-LAPW code (Elk or exciting) as a substitute for the proprietary code referenced in the original study. The results for each phase and volume ratio are to be aggregated and compared to explore how the electronic structure evolves under compression.

## Reproduction target
Using an open-source FP-LAPW implementation, calculate N(EF), ω_pl, and the band gap for FCC and BCC calcium at a series of specific volumes spanning the compression range reported in the literature. Produce a CSV file containing the computed values for each phase and volume ratio. Ensure that the calculations cover a sufficient number of compression states to capture the evolution of the electronic properties.

## Assets

- Open-source FP-LAPW code (Elk or exciting): https://elk.sourceforge.net/
- FCC and BCC calcium crystal structure parameters

## Workflow steps

### Step 1: DFT electronic structure calculations
- Role: scored (load-bearing)
- Action: Use an open-source FP-LAPW code (Elk or exciting) to compute the electronic structure of FCC and BCC calcium at a set of specific volume ratios V/V0 spanning the relevant compression range. For each phase and each V/V0, calculate the density of states at the Fermi level N(EF), the plasma frequency ω_pl, and the band gap. Record all results in a CSV file.
- Output file: `/app/outputs/electronic_properties.csv`
- Format: csv
- Contract: CSV with columns: phase (string, 'FCC' or 'BCC'), V_over_V0 (float), N_EF (float, states/eV/unit cell), plasma_frequency (float, eV), band_gap (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.csv
- path: `/app/outputs/electronic_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electronic properties for FCC and BCC Ca at multiple compression ratios. The hidden checker will evaluate structural trends (e.g., monotonicity, band gap opening) without revealing expected outcomes.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `V_over_V0`, `N_EF`, `plasma_frequency`, `band_gap`
  - `units`:
    - `N_EF`: states/eV/unit cell
    - `plasma_frequency`: eV
    - `band_gap`: eV

Notes: The hidden grading verifies the qualitative trends rather than exact numeric values, consistent with the paper's structural transition analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "V_over_V0",
          "N_EF",
          "plasma_frequency",
          "band_gap"
        ],
        "units": {
          "N_EF": "states/eV/unit cell",
          "plasma_frequency": "eV",
          "band_gap": "eV"
        }
      },
      "description": "Electronic properties for FCC and BCC Ca at multiple compression ratios. The hidden checker will evaluate structural trends (e.g., monotonicity, band gap opening) without revealing expected outcomes."
    }
  ],
  "notes": "The hidden grading verifies the qualitative trends rather than exact numeric values, consistent with the paper's structural transition analysis."
}
```

## How you are scored
The submission will be evaluated by a hidden verifier that reads your electronic_properties.csv and checks the computed trends. The verifier will compare your results against expected physical behavior and consistency checks (e.g., monotonicity of certain quantities, onset of band gap). Your overall reward is based solely on the correctness of the computed properties as determined by these checks. Merely reporting plausible numbers without running the actual calculations will not suffice; the hidden verifier assesses the underlying physical trends that can only be obtained from a proper DFT simulation.
