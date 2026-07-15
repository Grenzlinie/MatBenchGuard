# First-principles point defect characterization

## Problem background
Persistent luminescence (PL) materials can emit light long after excitation stops and are used in displays, bioimaging, and information storage. Most known PL mechanisms rely on electron traps, but hole-trap-dominated PL is not well understood. This work explores whether transition-metal dopants in carbon allotropes can introduce suitable defect levels that enable a hole-dominated PL mechanism, with a particular focus on Fe doping in lonsdaleite (hexagonal diamond) and the role of other impurities as hole traps.

## Approach
First-principles density functional theory (DFT) calculations are used to compute the electronic structure of perfect and doped lonsdaleite and cubic diamond. The Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation functional is employed for all systems. For Fe-doped lonsdaleite, an additional GGA+U calculation with U = 1 eV is performed to better describe localized Fe 3d states. A hybrid functional (HSE06) is used on the primitive cell of perfect lonsdaleite to provide a more accurate band gap reference.

The workflow examines: (i) the band gap of perfect lonsdaleite; (ii) the position and energy separation of Fe-induced defect levels in the band gap of Fe-doped lonsdaleite; and (iii) the occupied defect level positions introduced by a set of other dopants (K, Ca, Zn, Cr, Mn) and a carbon vacancy in lonsdaleite, as well as Fe in cubic diamond, all evaluated at the PBE level. All calculations use a plane‑wave basis, PAW pseudopotentials, and an open‑source DFT code (Quantum ESPRESSO). Ionic positions are relaxed, and band structures are analyzed to extract the quantities defined in the reproduction target.

## Reproduction target
Compute and report the following quantities in three structured JSON files:

- For perfect lonsdaleite: the PBE band gap (from a 4×4×3 supercell) and the HSE06 band gap (from the primitive cell).
- For Fe-doped lonsdaleite (4×4×3 supercell, one Fe substitution): the energy separation between occupied and unoccupied Fe 3d defect levels, and the position of the occupied Fe 3d level relative to the valence band maximum (VBM), both under PBE and under GGA+U (U = 1 eV).
- For each of the following systems (all at the PBE level, supercell with one substitutional impurity): K in lonsdaleite, Ca in lonsdaleite, Zn in lonsdaleite, Cr in lonsdaleite, Mn in lonsdaleite, a carbon vacancy in lonsdaleite, and Fe substitution in cubic diamond. For each system, report the occupied defect level position relative to VBM and, if both occupied and unoccupied defect levels are present in the band gap, the energy gap between them.

All energy values are in electron‑volts (eV) and are to be reported to two decimal places.

## Assets

- lonsdaleite (hexagonal diamond) crystal structure: https://next-gen.materialsproject.org/materials/mp-985585
- cubic diamond crystal structure: https://next-gen.materialsproject.org/materials/mp-66
- PAW pseudopotentials (PBE): https://pseudopotentials.quantum-espresso.org/legacy_tables/ps-library
- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Perfect lonsdaleite reference calculation
- Role: scored
- Action: Perform DFT calculations on perfect lonsdaleite using a plane‑wave code (e.g. Quantum ESPRESSO) with PBE functional and PAW pseudopotentials on a 4×4×3 supercell, and with the HSE06 hybrid functional on the primitive unit cell. Ionic positions are relaxed. Extract the PBE band gap from the supercell band structure and the HSE06 band gap from the primitive cell calculation. Write the two values to perfect_lonsdaleite.json.
- Output file: `/app/outputs/perfect_lonsdaleite.json`
- Format: json
- Contract: JSON object with keys: pbe_bg (float, PBE band gap in eV), hse06_bg (float, HSE06 band gap in eV). Values to two decimal places.
- Scoring: scored by hidden verifier

### Step 2: Fe‑doped lonsdaleite defect calculation
- Role: scored
- Action: Perform DFT calculations on a lonsdaleite 4×4×3 supercell with one Fe substitution, using both PBE and GGA+U (U=1 eV) functionals. Ionic positions are relaxed. From the band structures, identify the Fe 3d defect levels in the gap. Extract the energy separation between occupied and unoccupied Fe 3d defect levels, and the position of the occupied Fe 3d level relative to the valence band maximum (VBM), for both functionals. Write the four values to fe_doped.json.
- Output file: `/app/outputs/fe_doped.json`
- Format: json
- Contract: JSON object with keys: pbe_occ_unocc_gap (float, eV), pbe_occ_above_vbm (float, eV), ggau1_occ_unocc_gap (float, eV), ggau1_occ_above_vbm (float, eV). Values to two decimal places.
- Scoring: scored by hidden verifier

### Step 3: Additional dopant and impurity calculations
- Role: scored
- Action: Perform PBE DFT calculations on lonsdaleite 4×4×3 supercells with a single substitutional impurity: K, Ca, Zn, Cr, Mn, and a carbon vacancy (V_C). Also compute Fe substitution in a cubic diamond supercell of equivalent size. Ionic positions are relaxed. For each system, extract the occupied defect level position relative to VBM, and the energy gap between occupied and unoccupied defect levels if both are present. Write a JSON object with an entry for each system to additional_dopants.json.
- Output file: `/app/outputs/additional_dopants.json`
- Format: json
- Contract: JSON object where keys are system identifiers: 'K_lonsdaleite', 'Ca_lonsdaleite', 'Zn_lonsdaleite', 'C_vacancy_lonsdaleite', 'Cr_lonsdaleite', 'Mn_lonsdaleite', 'Fe_cubic_diamond'. Each value is an object with keys: 'occ_level_above_vbm_pbe' (float, eV) and 'occ_unocc_gap_pbe' (float or null, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/perfect_lonsdaleite.json`
- `/app/outputs/fe_doped.json`
- `/app/outputs/additional_dopants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### perfect_lonsdaleite.json
- path: `/app/outputs/perfect_lonsdaleite.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap of perfect lonsdaleite from PBE (supercell) and HSE06 (primitive cell). The checker compares these values to the paper's reported band gaps within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `pbe_bg`: float (eV)
    - `hse06_bg`: float (eV)

### fe_doped.json
- path: `/app/outputs/fe_doped.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Defect level properties of Fe‑doped lonsdaleite under PBE and GGA+U (U=1 eV). The checker compares these four numbers to the paper's reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `pbe_occ_unocc_gap`: float (eV)
    - `pbe_occ_above_vbm`: float (eV)
    - `ggau1_occ_unocc_gap`: float (eV)
    - `ggau1_occ_above_vbm`: float (eV)

### additional_dopants.json
- path: `/app/outputs/additional_dopants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Occupied defect level positions and occ‑unocc gaps for a set of dopants/impurities in lonsdaleite and Fe in cubic diamond, computed at PBE level. The checker compares each value to the paper's reported reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `K_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `Ca_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `Zn_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `C_vacancy_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `Cr_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `Mn_lonsdaleite`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)
    - `Fe_cubic_diamond`:
      - `occ_level_above_vbm_pbe`: float (eV)
      - `occ_unocc_gap_pbe`: float|null (eV)

Notes: All numerical values must be reported to two decimal places. Units are electron‑volts (eV). 'occ_unocc_gap_pbe' can be null when only occupied defect levels exist in the band gap (no empty levels within the gap). The hidden checker compares each quantity to the paper‑reported value using tolerances appropriate for the chosen functional.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "perfect_lonsdaleite.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pbe_bg": "float (eV)",
          "hse06_bg": "float (eV)"
        }
      },
      "description": "Band gap of perfect lonsdaleite from PBE (supercell) and HSE06 (primitive cell). The checker compares these values to the paper's reported band gaps within tolerances."
    },
    {
      "file": "fe_doped.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pbe_occ_unocc_gap": "float (eV)",
          "pbe_occ_above_vbm": "float (eV)",
          "ggau1_occ_unocc_gap": "float (eV)",
          "ggau1_occ_above_vbm": "float (eV)"
        }
      },
      "description": "Defect level properties of Fe‑doped lonsdaleite under PBE and GGA+U (U=1 eV). The checker compares these four numbers to the paper's reported values with tolerances."
    },
    {
      "file": "additional_dopants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "K_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "Ca_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "Zn_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "C_vacancy_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "Cr_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "Mn_lonsdaleite": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          },
          "Fe_cubic_diamond": {
            "occ_level_above_vbm_pbe": "float (eV)",
            "occ_unocc_gap_pbe": "float|null (eV)"
          }
        }
      },
      "description": "Occupied defect level positions and occ‑unocc gaps for a set of dopants/impurities in lonsdaleite and Fe in cubic diamond, computed at PBE level. The checker compares each value to the paper's reported reference values with tolerances."
    }
  ],
  "notes": "All numerical values must be reported to two decimal places. Units are electron‑volts (eV). 'occ_unocc_gap_pbe' can be null when only occupied defect levels exist in the band gap (no empty levels within the gap). The hidden checker compares each quantity to the paper‑reported value using tolerances appropriate for the chosen functional."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage. For every output file, the verifier reads the numeric values you provide and compares them against independently established reference expectations. The final reward is a weighted combination of the scores from the three stages, where the band gaps of perfect lonsdaleite and the Fe-doped defect levels carry higher weight than the additional dopant results. Simply reporting any number is insufficient to earn full credit; only values that faithfully reproduce the target electronic structure properties, as produced by an honest DFT calculation on the specified systems, will yield a high score. No paper-specific targets, tolerances, or reference numbers are stated here; the verifier's criteria are hidden.
