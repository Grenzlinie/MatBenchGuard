# Non-resonant Raman Spectrum and Band Gap of Single-Wall Carbon Nanotube Dimers via Spectral Moments and Tight-Binding

## Problem background
Single-wall carbon nanotube (SCNT) dimers are model systems for studying van der Waals coupling and charge transfer at the nanoscale. Raman spectroscopy is a key tool for probing their vibrational properties, including low-frequency breathing-like modes (BLM). Computing the non-resonant Raman spectrum of an inhomogeneous dimer and its electronic band structure helps understand how intertube interactions modify vibrational frequencies and electronic gaps. This task addresses the vibrational response of the (15,11)-(16,12) dimer (BLM peaks) and the electronic structure of the (8,6)-(9,7) Sc-Sc dimer (band gap) using spectral moments and tight-binding methods.

## Approach
The workflow combines a classical intertube potential with a vibrational spectral moments method and a tight-binding electronic structure approach. First, the equilibrium intertube configuration of each dimer is found by minimizing a Lennard-Jones potential. The full dynamical matrix is then assembled from intratube force constants (Rubio et al.) and intertube Lennard‑Jones interactions. The ZZ‑polarized non‑resonant Raman spectrum is computed directly from the dynamical matrix using the spectral moments method (SMM) together with a bond‑polarizability model, without explicit diagonalization. For the electronic part, a four‑orbital tight‑binding Hamiltonian is used to compute the band structure and electronic density of states (eDOS) of the Sc‑Sc dimer, from which the band gap is extracted.

## Reproduction target
For the (15,11)-(16,12) SCNT dimer, compute the ZZ‑polarized non‑resonant Raman spectrum in the breathing‑mode region, identify the four breathing‑like mode (BLM) peaks, and report their frequencies (cm⁻¹) as a JSON array. For the (8,6)-(9,7) Sc‑Sc dimer, compute its electronic band gap (eV) and report it as a JSON object containing the band gap value. Both results must be written to the specified output files.

## Assets

- Rubio et al. intratube force constants model: https://doi.org/10.1016/j.ssc.2004.05.016
- Bond-polarizability model parameters from Saito et al.
- Tight-binding parameters for four-orbital carbon nanotube model
- Python scientific computing stack

## Workflow steps

### Step 1: Optimize intertube geometry of dimers
- Role: process
- Action: Determine the equilibrium intertube configuration (separation, relative rotation, translation) of the (15,11)-(16,12) and (8,6)-(9,7) SCNT dimers by minimizing the Lennard-Jones potential U_LJ(r)=4ε[(σ/r)^12−(σ/r)^6] with ε=2.964 meV and σ=0.3407 nm. Output the optimized geometry for each dimer.
- Evidence: `/app/outputs/optimized_geometry.json`

### Step 2: Assemble dynamical matrix for the (15,11)-(16,12) dimer
- Role: process
- Action: Construct the vibrational dynamical matrix D block-by-block for the (15,11)-(16,12) dimer using the optimized geometry. Diagonal blocks are formed from the intratube force constants of Rubio et al., and the off-diagonal block from Lennard-Jones intertube interactions.
- Evidence: `/app/outputs/dynamical_matrix_assembled.json`

### Step 3: Compute ZZ-polarized Raman spectrum via spectral moments method
- Role: process
- Action: Apply the spectral moments method (SMM) with the bond-polarizability model to compute the ZZ-polarized non-resonant Raman spectrum of the (15,11)-(16,12) dimer in the breathing-mode frequency region. Output the spectrum as a frequency-versus-intensity table (raman_spectrum_blm.csv) for subsequent peak extraction.
- Evidence: `/app/outputs/raman_spectrum_blm.csv`

### Step 4: Extract breathing-like mode peak frequencies
- Role: scored (load-bearing)
- Action: Identify the four breathing-like mode (BLM) peaks in the computed Raman spectrum of the (15,11)-(16,12) dimer and record their frequencies. Report the frequencies as a JSON array.
- Output file: `/app/outputs/blm_frequencies.json`
- Format: json
- Contract: JSON array of objects: [{"mode": "string", "frequency_cm1": number}].
- Scoring: scored by hidden verifier

### Step 5: Compute electronic band structure and eDOS of (8,6)-(9,7) dimer
- Role: process
- Action: Using a four-orbital tight-binding Hamiltonian with standard carbon nanotube parameters, calculate the band structure and electronic density of states (eDOS) for the (8,6)-(9,7) Sc-Sc dimer. Output the computed band structure data for subsequent gap extraction.
- Evidence: `/app/outputs/band_structure_edos.csv`

### Step 6: Extract electronic band gap of the (8,6)-(9,7) dimer
- Role: scored (load-bearing)
- Action: From the band structure and eDOS computed for the (8,6)-(9,7) dimer, determine the electronic band gap in eV. Output the result as a JSON object.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: JSON object: {"dimer": "(8,6)-(9,7)", "band_gap_eV": number}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/blm_frequencies.json`
- `/app/outputs/band_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### blm_frequencies.json
- path: `/app/outputs/blm_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored output containing the four BLM peak frequencies (mode identifiers and values in cm^-1). The checker compares each frequency against a hidden paper-derived reference within a tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `mode`, `frequency_cm1`
    - `properties`:
      - `mode`:
        - `type`: string
      - `frequency_cm1`:
        - `type`: number

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored output containing the band gap of the (8,6)-(9,7) dimer. The checker compares the reported gap against a hidden paper-derived reference value within a tolerance.
- schema:
  - `type`: object
  - `required`: `band_gap_eV`
  - `properties`:
    - `dimer`:
      - `type`: string
    - `band_gap_eV`:
      - `type`: number

Notes: All process steps produce intermediate evidence files that may be examined but are not directly scored. The two scored artifacts are the frequencies and the band gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "blm_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "mode",
            "frequency_cm1"
          ],
          "properties": {
            "mode": {
              "type": "string"
            },
            "frequency_cm1": {
              "type": "number"
            }
          }
        }
      },
      "description": "Scored output containing the four BLM peak frequencies (mode identifiers and values in cm^-1). The checker compares each frequency against a hidden paper-derived reference within a tolerance."
    },
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_eV"
        ],
        "properties": {
          "dimer": {
            "type": "string"
          },
          "band_gap_eV": {
            "type": "number"
          }
        }
      },
      "description": "Scored output containing the band gap of the (8,6)-(9,7) dimer. The checker compares the reported gap against a hidden paper-derived reference value within a tolerance."
    }
  ],
  "notes": "All process steps produce intermediate evidence files that may be examined but are not directly scored. The two scored artifacts are the frequencies and the band gap."
}
```

## How you are scored
A hidden verifier independently scores your output files. For `blm_frequencies.json`, it checks that the array contains four mode entries with frequencies that fall within allowed ranges of the expected BLM peaks. For `band_gap.json`, it checks that the reported band gap is close to the expected reference gap. Each scored artifact contributes a weight to the total reward (the weights are not disclosed). The verifier applies tolerances, but you must actually execute the spectrum and band‑structure computations; simply guessing or hardcoding numbers without performing the workflow will not satisfy the checks.
