# DFT Electronic and Phonon Properties of Cu2Se-Doped PbSe

## Problem background
Thermoelectric materials can convert waste heat into electricity. PbSe is considered an attractive, tellurium-free alternative to PbTe, but n‑type PbSe has historically underperformed due to the lack of a second conduction band for Seebeck enhancement. Recent research proposes that doping PbSe with Cu₂Se can simultaneously modify the electronic band structure—flattening the conduction band edge and increasing the effective mass—and soften acoustic phonons, thereby improving both charge transport and thermal properties. This computational reproduction task focuses on verifying those band‑structure and phonon modifications using first‑principles calculations.

## Approach
The core idea is to use plane‑wave density functional theory (DFT) to compute electronic band structures and phonon dispersions for pristine PbSe and for PbSe doped with 1%, 2%, and 3% Cu₂Se. Supercell models are built by removing one Pb atom and inserting two Cu atoms at interstitial random positions, mimicking the random distribution reported. Structural relaxations and band structure calculations are performed with the PBE exchange‑correlation functional. The band gap and electron effective mass at the conduction‑band minimum are extracted for each composition. Additionally, density‑functional perturbation theory (DFPT) is used to calculate the phonon dispersion for pristine and for the 3%‑doped case (using the configuration where Cu atoms are near the Pb vacancy). The softening of acoustic phonon modes (longitudinal and transverse acoustic) near the high‑symmetry M and R points is assessed.

## Reproduction target
Produce a JSON file `results.json` containing the following computed quantities: band gap (eV) for pristine, 1%, 2%, and 3% Cu₂Se‑doped PbSe; electron effective mass (in units of the free‑electron mass mₑ) for the same four systems; and a textual description that states whether the acoustic phonon modes (LA and TA) near the M and R points are softened in the 3%‑doped case compared to pristine PbSe.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate supercell models for DFT calculations
- Role: process
- Action: Generate atomic configurations for pristine PbSe (rock-salt, Fm-3m, lattice parameter ~6.12 Å) and for PbSe-x%Cu2Se (x = 1, 2, 3). For each doped supercell, remove one Pb atom and place two interstitial Cu atoms at random positions, reflecting the random distribution. Save the coordinates in a structured file supercells.json.
- Evidence: `/app/outputs/supercells.json`

### Step 2: DFT electronic structure and phonon calculations
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with PBE functional: (i) perform structural relaxation and electronic band structure calculations for pristine and 1%, 2%, 3% Cu2Se-doped PbSe; extract the band gap (eV) and electron effective mass (in units of m_e) for each composition. (ii) Run density-functional perturbation theory (DFPT) phonon calculations for the pristine and 3%-doped cases (control configuration with Cu near Pb vacancy) and determine whether acoustic phonon modes (LA, TA) near the M and R points are softened relative to pristine. Write all computed quantities and a description of the phonon softening to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: band_gap_pristine (eV), band_gap_1pct (eV), band_gap_2pct (eV), band_gap_3pct (eV), effective_mass_pristine (m_e), effective_mass_1pct (m_e), effective_mass_2pct (m_e), effective_mass_3pct (m_e), phonon_softening_description (string).
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
- description: Scored artifact containing DFT-computed band gaps, effective masses, and a description of acoustic phonon softening for pristine PbSe and Cu2Se-doped PbSe.
- schema:
  - `type`: object
  - `required`: `band_gap_pristine`, `band_gap_1pct`, `band_gap_2pct`, `band_gap_3pct`, `effective_mass_pristine`, `effective_mass_1pct`, `effective_mass_2pct`, `effective_mass_3pct`, `phonon_softening_description`
  - `properties`:
    - `band_gap_pristine`:
      - `type`: number
      - `unit`: eV
    - `band_gap_1pct`:
      - `type`: number
      - `unit`: eV
    - `band_gap_2pct`:
      - `type`: number
      - `unit`: eV
    - `band_gap_3pct`:
      - `type`: number
      - `unit`: eV
    - `effective_mass_pristine`:
      - `type`: number
      - `unit`: m_e
    - `effective_mass_1pct`:
      - `type`: number
      - `unit`: m_e
    - `effective_mass_2pct`:
      - `type`: number
      - `unit`: m_e
    - `effective_mass_3pct`:
      - `type`: number
      - `unit`: m_e
    - `phonon_softening_description`:
      - `type`: string

Notes: Band gaps and effective masses are compared against paper-reported values with appropriate tolerances to account for functional/pseudopotential differences. The phonon softening description is checked for structural keywords indicating softening of acoustic modes near M and R points in doped case relative to pristine.

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
        "required": [
          "band_gap_pristine",
          "band_gap_1pct",
          "band_gap_2pct",
          "band_gap_3pct",
          "effective_mass_pristine",
          "effective_mass_1pct",
          "effective_mass_2pct",
          "effective_mass_3pct",
          "phonon_softening_description"
        ],
        "properties": {
          "band_gap_pristine": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_1pct": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_2pct": {
            "type": "number",
            "unit": "eV"
          },
          "band_gap_3pct": {
            "type": "number",
            "unit": "eV"
          },
          "effective_mass_pristine": {
            "type": "number",
            "unit": "m_e"
          },
          "effective_mass_1pct": {
            "type": "number",
            "unit": "m_e"
          },
          "effective_mass_2pct": {
            "type": "number",
            "unit": "m_e"
          },
          "effective_mass_3pct": {
            "type": "number",
            "unit": "m_e"
          },
          "phonon_softening_description": {
            "type": "string"
          }
        }
      },
      "description": "Scored artifact containing DFT-computed band gaps, effective masses, and a description of acoustic phonon softening for pristine PbSe and Cu2Se-doped PbSe."
    }
  ],
  "notes": "Band gaps and effective masses are compared against paper-reported values with appropriate tolerances to account for functional/pseudopotential differences. The phonon softening description is checked for structural keywords indicating softening of acoustic modes near M and R points in doped case relative to pristine."
}
```

## How you are scored
After the task completes, a hidden verifier reads `results.json`. It compares your reported band‑gap and effective‑mass values to reference data derived from the original study, awarding credit when they lie within pre‑set tolerances. The phonon‑softening description is checked for the presence of key phrases indicating softening of LA/TA modes near the M and R points. Each scored quantity carries a weight, and the total reward is a float between 0 and 1.
