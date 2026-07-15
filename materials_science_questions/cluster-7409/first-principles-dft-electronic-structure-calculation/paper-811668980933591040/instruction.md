# Electronic structure and defect formation energies of Pb(ZrTiNb)O3 (PZTN) perovskites from DFT

## Problem background
Perovskite ferroelectric thin films, such as lead zirconate titanate (PZT), suffer from leakage current that degrades device reliability. One proposed mechanism is that oxygen vacancies form during fabrication due to high Pb vapor pressure; these vacancies narrow the electronic band gap, thereby increasing leakage. Substituting Nb at the B site of the perovskite has been suggested as a way to suppress oxygen vacancy formation, potentially maintaining a wide band gap and reducing leakage current in Pb(ZrTiNb)O₃ (PZTN) systems. This task reproduces the first‑principles electronic‑structure and defect‑formation‑energy calculations that quantify how Nb substitution affects the band gap and the relative stability of different defect configurations in these perovskites.

## Approach
Use density‑functional theory (DFT) with the local density approximation (LDA) and the full‑potential linearised augmented‑plane‑wave (FLAPW) method, as implemented in the open‑source Elk code. Build 2×2×2 cubic perovskite supercells for several compositions: stoichiometric PZT and PZTN, as well as defective configurations with a Pb deficiency or a combined Pb‑O Schottky deficiency. For each model, optimise the lattice constant by total‑energy minimisation, perform a self‑consistent electronic‑structure calculation, and extract the band gap (Eg). Compute the band gap difference δEg relative to stoichiometric PZT. Additionally, calculate total energies of reference systems (fcc Pb metal and PbO in the B10 structure) to evaluate defect formation energies ε_v for all configurations. The full workflow comprises model construction, lattice optimisation, self‑consistent DFT runs, band gap analysis, reference energy calculations, and formation energy evaluation.

## Reproduction target
Produce two scored JSON files that summarise the computed quantities:

1. **`/app/outputs/bandgap_data.json`** – containing the band gap (in eV) and the band gap difference δEg (relative to stoichiometric PZT) for the five compositions: `PZT_stoich`, `PZTN_stoich`, `PZT_Pb_def`, `PZT_PbO_def`, `PZTN_Pb_def`. Each entry includes the keys `bandgap_eV` and `delta_Eg_eV`.

2. **`/app/outputs/formation_energies.json`** – containing the defect formation energy per supercell (in eV) for the six compositions: `PZT_stoich`, `PZT_Pb_def`, `PZT_PbO_def`, `PZTN_stoich`, `PZTN_Pb_def`, `PZTN_PbO_def`. Each entry includes the key `formation_energy_eV_per_supercell`.

These quantities must be obtained by re‑running the DFT procedure described in the workflow steps. The hidden verifier compares the reported values against reference criteria (quantitative thresholds and relative ordering) that are consistent with the expected behaviour of the system.

## Assets

- Elk FP-LAPW DFT code: https://elk.sourceforge.net/

## Workflow steps

### Step 1: Supercell model construction
- Role: process
- Action: Construct 2×2×2 cubic perovskite supercells for six compositions: stoichiometric PZT (Pb(Zr₀.₂₅Ti₀.₇₅)O₃), stoichiometric PZTN (Pb(Zr₀.₂₅Ti₀.₅₀Nb₀.₂₅)O₃), PZT with a 12.5% Pb deficit, PZT with a Pb‑O Schottky deficit, PZTN with a 12.5% Pb deficit, and PZTN with a Pb‑O Schottky deficit. Use checkerboard‑like B‑site cation patterns, with atoms at paraelectric neutral positions (ideal cubic coordinates, no relaxation).
- Evidence: none

### Step 2: Lattice constant optimisation
- Role: process
- Action: For each supercell, perform DFT‑LDA‑FLAPW total‑energy calculations with Elk to optimise the lattice constant by minimisation, keeping internal positions fixed. Use a plane‑wave cutoff of 204 eV, tetrahedron method for Brillouin‑zone integration, and the valence states: Pb(5d,6s,6p), Ti(3s,3p,3d), Zr(4s,4p,4d), Nb(4s,4p,4d), O(2s,2p).
- Evidence: `/app/outputs/lattice_optimisation_summary.txt`

### Step 3: Self‑consistent electronic structure calculation
- Role: process
- Action: Run self‑consistent DFT calculations at the optimised lattice constants for each model, using the same Elk settings. Output total energies and Kohn‑Sham eigenvalues.
- Evidence: `/app/outputs/scf_energies.txt`

### Step 4: Band gap extraction and δEg analysis
- Role: scored (load-bearing)
- Action: Determine the band gap (Eg) from the SCF eigenvalues for each of the five models (PZT_stoich, PZTN_stoich, PZT_Pb_def, PZT_PbO_def, PZTN_Pb_def). Compute the bandgap differences δEg relative to the stoichiometric PZT bandgap. Write the results to /app/outputs/bandgap_data.json.
- Output file: `/app/outputs/bandgap_data.json`
- Format: json
- Contract: JSON object with keys PZT_stoich, PZTN_stoich, PZT_Pb_def, PZT_PbO_def, PZTN_Pb_def. Each value is an object containing 'bandgap_eV' (float) and 'delta_Eg_eV' (float).
- Scoring: scored by hidden verifier

### Step 5: Reference energy calculations for Pb and PbO
- Role: process
- Action: Calculate total energies of fcc Pb metal and of PbO in the B10 (P4/nmm) structure with the same Elk DFT settings (LDA, FLAPW, cutoff 204 eV, tetrahedron method, same valence states). These energies are necessary to form defect formation energies.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 6: Defect formation energy calculation
- Role: scored (load-bearing)
- Action: Compute defect formation energies ε_v (eV per supercell) for all six compositions using the supercell total energies and the reference energies of fcc Pb and PbO. Write the results to /app/outputs/formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object with keys PZT_stoich, PZT_Pb_def, PZT_PbO_def, PZTN_stoich, PZTN_Pb_def, PZTN_PbO_def. Each value is an object containing 'formation_energy_eV_per_supercell' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap_data.json`
- `/app/outputs/formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap_data.json
- path: `/app/outputs/bandgap_data.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Bandgap and bandgap differences for the five main compositions; structural threshold checks are performed by the verifier.
- schema:
  - `type`: object
  - `required`:
    - `PZT_stoich`: object
    - `PZTN_stoich`: object
    - `PZT_Pb_def`: object
    - `PZT_PbO_def`: object
    - `PZTN_Pb_def`: object
  - `items`:
    - `bandgap_eV`: float
    - `delta_Eg_eV`: float

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Defect formation energies for all six models; structural ordering checks are performed by the verifier.
- schema:
  - `type`: object
  - `required`:
    - `PZT_stoich`: object
    - `PZT_Pb_def`: object
    - `PZT_PbO_def`: object
    - `PZTN_stoich`: object
    - `PZTN_Pb_def`: object
    - `PZTN_PbO_def`: object
  - `items`:
    - `formation_energy_eV_per_supercell`: float

Notes: All outputs are scored via the T3 structural scoring method: δEg thresholds and formation energy ordering, consistent with the paper’s main quantitative claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "PZT_stoich": "object",
          "PZTN_stoich": "object",
          "PZT_Pb_def": "object",
          "PZT_PbO_def": "object",
          "PZTN_Pb_def": "object"
        },
        "items": {
          "bandgap_eV": "float",
          "delta_Eg_eV": "float"
        }
      },
      "description": "Bandgap and bandgap differences for the five main compositions; structural threshold checks are performed by the verifier."
    },
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "PZT_stoich": "object",
          "PZT_Pb_def": "object",
          "PZT_PbO_def": "object",
          "PZTN_stoich": "object",
          "PZTN_Pb_def": "object",
          "PZTN_PbO_def": "object"
        },
        "items": {
          "formation_energy_eV_per_supercell": "float"
        }
      },
      "description": "Defect formation energies for all six models; structural ordering checks are performed by the verifier."
    }
  ],
  "notes": "All outputs are scored via the T3 structural scoring method: δEg thresholds and formation energy ordering, consistent with the paper’s main quantitative claims."
}
```

## How you are scored
A hidden checker independently examines each scored output file. For `bandgap_data.json`, it verifies that the band gap differences satisfy certain quantitative thresholds for specific defect configurations. For `formation_energies.json`, it checks that the formation energies for the PZTN compositions exhibit a required relative stability ordering. Reward for each artifact is proportional to the number of these criteria that are met; the overall reward is the weighted sum across both scored artifacts, with the main weight coming from the band gap and formation energy comparisons. Scoring does not require exact numerical agreement but evaluates whether the computed values fall within acceptable tolerances and respect the specified structural relations. No gold values or tolerances are provided to you — you must obtain them by physically performing the calculations.
