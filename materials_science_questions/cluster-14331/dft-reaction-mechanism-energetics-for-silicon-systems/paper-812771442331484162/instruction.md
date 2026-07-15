# DFT Calculation of Vibrational Frequencies for a Rhenium Methylidene Tautomer

## Problem background
Methyltrioxorhenium (CH₃ReO₃) undergoes photochemical tautomerization when isolated in a low-temperature argon matrix, forming a methylidene derivative H₂C=Re(O)₂OH. Identifying this reactive intermediate depends critically on vibrational spectroscopy: experimental infrared spectra must be matched to computed vibrational frequencies and intensities. Reproducing the quantum-chemical frequency calculation provides a direct computational validation of the structural assignment and the vibrational fingerprint of this organorhenium tautomer. The task is to compute the harmonic vibrational frequencies and infrared intensities for H₂C=Re(O)₂OH at a level of theory comparable to the original study, producing a set of unscaled normal‑mode frequencies and relative intensities that can be compared against a reference set of theoretical values.

## Approach
The method uses density functional theory (DFT) with a gradient‑corrected functional to compute harmonic vibrational frequencies and infrared intensities for the methylidene tautomer H₂C=Re(O)₂OH. The molecular structure, which has Cₛ symmetry, is built from the geometry reported in the original work (bond lengths and angles derived from the optimized structure). A geometry optimization is performed followed by a harmonic vibrational frequency analysis. A typical functional choice is a GGA such as PBE or BP86, combined with a basis set that uses an effective core potential (ECP) for rhenium (e.g., Stuttgart/Dresden ECP or LANL2DZ with polarization) and an all‑electron basis (e.g., 6‑31G(d,p)) for the light atoms (C, O, H). Unscaled harmonic frequencies and IR intensities are computed for all normal modes in the range 300–4000 cm⁻¹. The computed spectrum is compared to experimental observations to assign each vibrational mode, and the resulting list of modes with their frequencies, intensities, and symmetry labels forms the core of the reproduction.

## Reproduction target
Compute the harmonic vibrational frequencies and infrared intensities for H₂C=Re(O)₂OH using DFT with a gradient‑corrected functional and a basis set that includes an effective core potential on Re and an all‑electron basis on C, O, H (a setting comparable to the original BPW91/II level of theory). Report the unscaled harmonic frequencies (in cm⁻¹) and relative IR intensities (normalized to the strongest band = 100) for all normal modes in the range 300–4000 cm⁻¹ as a JSON array of objects. Each object must contain a descriptive mode label (string), frequency (float, cm⁻¹), intensity (float, normalized), and symmetry (string, e.g., "a'", "a''"). The result is to be written to the specified output file and will be checked against a hidden reference set of computed frequencies for the same molecule.

## Assets

- Open-source DFT code (e.g., ORCA, NWChem, CP2K): https://nwchemgit.github.io/

## Workflow steps

### Step 1: DFT vibrational frequencies of H2C=Re(O)2OH
- Role: scored (load-bearing)
- Action: Build the molecular structure of H2C=Re(O)2OH with Cs symmetry as described in the paper (bond lengths/angles derived from Figure 4a). Perform a geometry optimization followed by a harmonic vibrational frequency calculation using DFT with a gradient-corrected functional (e.g., PBE, BP86) and a basis set combining an effective core potential for Re (e.g., Stuttgart/Dresden ECP or LANL2DZ with polarization) and an all-electron basis (e.g., 6-31G(d,p)) for C, O, H. Compute unscaled vibrational frequencies and IR intensities. Identify the theoretical normal modes in the range 300–4000 cm⁻¹.
- Output file: `/app/outputs/step_01_vibrational_frequencies.json`
- Format: json
- Contract: JSON array of objects, each with fields: mode (string), frequency (float, cm⁻¹), intensity (float, normalized to strongest band=100), symmetry (string, e.g. "a'", "a''").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_vibrational_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_vibrational_frequencies.json
- path: `/app/outputs/step_01_vibrational_frequencies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Harmonic vibrational frequencies and IR intensities for the methylidene tautomer H2C=Re(O)2OH computed at a level of theory comparable to the paper's BPW91/II. The checker will recompute a deviation metric (e.g., RMSD) between the submitted frequencies and a hidden reference set of calculated frequencies for the same molecule.
- schema:
  - `type`: array
  - `items`:
    - `mode`: string
    - `frequency`: number (cm⁻¹)
    - `intensity`: number (relative to strongest band=100)
    - `symmetry`: string
  - `description`: Array of objects, each describing a vibrational mode.

Notes: The hidden reference consists of the unscaled computed frequencies from the paper's own DFT calculation (BPW91/II). The agent is not required to exactly reproduce those values; the scoring tolerance allows for differences due to functional, basis set, and code choices.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_vibrational_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "mode": "string",
          "frequency": "number (cm⁻¹)",
          "intensity": "number (relative to strongest band=100)",
          "symmetry": "string"
        },
        "description": "Array of objects, each describing a vibrational mode."
      },
      "description": "Harmonic vibrational frequencies and IR intensities for the methylidene tautomer H2C=Re(O)2OH computed at a level of theory comparable to the paper's BPW91/II. The checker will recompute a deviation metric (e.g., RMSD) between the submitted frequencies and a hidden reference set of calculated frequencies for the same molecule."
    }
  ],
  "notes": "The hidden reference consists of the unscaled computed frequencies from the paper's own DFT calculation (BPW91/II). The agent is not required to exactly reproduce those values; the scoring tolerance allows for differences due to functional, basis set, and code choices."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines them into a final reward. For the scored frequency artifact, the verifier compares your submitted harmonic frequencies to a hidden reference set of computed frequencies for H₂C=Re(O)₂OH, obtained at a comparable level of theory. The agreement is measured using a deviation metric (e.g., root‑mean‑square deviation) over all assigned normal modes. Full credit is awarded when the deviation falls within an accepted tolerance; larger deviations result in proportionally reduced reward. The verifier may also check that the intensity ordering is consistent and that the symmetry assignments are plausible. Simply quoting a known literature value does not guarantee credit – the computation must be performed and the results must stem from an actual DFT calculation.
