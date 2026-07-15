# First-principles DFT study of interstitial hydrogen in quartz SiO₂: geometries and charge transition level

## Problem background
Interstitial hydrogen in wide band gap oxides plays a key role in determining electronic properties, such as introducing deep gap states or acting as a shallow donor. In quartz SiO₂, hydrogen can occupy different charge states (negative, neutral, positive) and is predicted to exhibit negative‑U behaviour: the neutral charge state is never the most stable, and the two oppositely charged states have a characteristic (+/−) transition level within the band gap. This transition level—along with the large atomic relaxations that accompany it—directly influences the reliability of SiO₂‑based electronic devices. This task reproduces the first‑principles hybrid‑DFT calculations that reveal the location of that transition level and the relaxed atomic geometries of interstitial hydrogen in quartz SiO₂.

## Approach
Use the HSE06 screened hybrid functional to simultaneously correct the band gap error and relax the geometry of interstitial hydrogen in a quartz SiO₂ supercell. The fraction of Hartree‑Fock exchange is adjusted so that the computed band gap matches the experimental value of quartz SiO₂ (9.0 eV). Starting from the experimental crystal structure, one hydrogen atom is placed at an interstitial site; internal atomic coordinates are relaxed while the lattice parameters are held fixed. This is done for three charge states: H⁻, H⁰, and H⁺. From the total energies of the perfect and defect supercells, formation energies are computed as a function of the Fermi level (referenced to the valence‑band maximum). Because H⁰ is expected to be unstable, the key quantity is the Fermi energy at which the formation energies of H⁺ and H⁻ are equal—the (+/−) transition level. The work is carried out with open‑source plane‑wave DFT tools and standard pseudopotentials, following the same computational protocol as the original study but using a publicly available implementation.

## Reproduction target
Carry out HSE06 DFT calculations for interstitial hydrogen in a quartz SiO₂ supercell and produce the following three scored artifacts:
1. The relaxed bond lengths (Si–H for H⁻, distance to the nearest oxygen for H⁰, and O–H for H⁺).
2. The defect formation energies of the three charge states as a function of the Fermi energy (relative to the VBM) across the band gap.
3. The (+/−) charge transition level, reported both with respect to the VBM and with respect to the CBM.

## Assets

- Quartz SiO2 crystal structure: https://www.crystallography.net/cod/1011135.html
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk SiO2 HSE06 calculation
- Role: process
- Action: Perform HSE06 hybrid functional DFT calculation for a quartz SiO₂ supercell using experimental lattice parameters. Tune the fraction of Hartree-Fock exchange to match the experimental band gap of 9.0 eV, obtaining the valence band maximum (VBM) and conduction band minimum (CBM) energies.
- Evidence: `/app/outputs/bulk_results.json`

### Step 2: Defect supercell geometry relaxations
- Role: process
- Action: For each charge state (H⁻, H⁰, H⁺), place one H interstitial at an open site in the SiO₂ supercell, keep experimental lattice parameters fixed, relax internal coordinates using HSE06 with the tuned exchange fraction, and record total energies and relaxed atomic coordinates for both the defect supercells and the perfect supercell.
- Evidence: `/app/outputs/defect_energies_and_coords.json`

### Step 3: Relaxed geometries and bond lengths
- Role: scored
- Action: From the relaxed defect structures, extract the following bond lengths: for H⁻, the Si–H bond length; for H⁰, the distance to the nearest oxygen; for H⁺, the O–H bond length. Write to relaxed_geometries.json.
- Output file: `/app/outputs/relaxed_geometries.json`
- Format: json
- Contract: JSON object with keys 'H_minus', 'H_zero', 'H_plus'. Each value is a dict: for H_minus {'Si_H_bond_length_angstrom': float, 'description': string}; for H_zero {'distance_to_nearest_oxygen_angstrom': float, 'description': string}; for H_plus {'O_H_bond_length_angstrom': float, 'description': string}. All lengths in Å.
- Scoring: scored by hidden verifier

### Step 4: Defect formation energies vs Fermi energy
- Role: scored
- Action: Using the total energies from the defect and perfect supercells and the VBM from the bulk calculation, compute defect formation energies for each charge state as a function of Fermi energy (referenced to VBM) across the band gap. Output as CSV.
- Output file: `/app/outputs/formation_energies_Fermi_level.csv`
- Format: csv
- Contract: CSV with columns: 'Fermi_energy_eV' (float), 'Ef_H_minus_eV' (float), 'Ef_H_zero_eV' (float), 'Ef_H_plus_eV' (float). Fermi energy values from VBM=0 to CBM=band_gap, step ≤ 0.5 eV. Energies in eV.
- Scoring: scored by hidden verifier

### Step 5: (+/-) charge transition level
- Role: scored (load-bearing)
- Action: From the formation energy curves, determine the Fermi energy at which the formation energies of H⁺ and H⁻ are equal (the (+/−) transition level, since H⁰ is never stable). Report this energy relative to VBM and relative to CBM.
- Output file: `/app/outputs/charge_transition_levels.json`
- Format: json
- Contract: JSON object with keys 'transition_energy_above_VBM_eV': float, 'transition_energy_below_CBM_eV': float. Values in eV, truncated to 1 decimal place.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_geometries.json`
- `/app/outputs/formation_energies_Fermi_level.csv`
- `/app/outputs/charge_transition_levels.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_geometries.json
- path: `/app/outputs/relaxed_geometries.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Relaxed bond lengths for the three charge states of interstitial hydrogen in quartz SiO₂.
- schema:
  - `type`: object
  - `required`:
    - `H_minus`:
      - `type`: object
      - `required`:
        - `Si_H_bond_length_angstrom`: number
        - `description`: string
    - `H_zero`:
      - `type`: object
      - `required`:
        - `distance_to_nearest_oxygen_angstrom`: number
        - `description`: string
    - `H_plus`:
      - `type`: object
      - `required`:
        - `O_H_bond_length_angstrom`: number
        - `description`: string

### formation_energies_Fermi_level.csv
- path: `/app/outputs/formation_energies_Fermi_level.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Formation energies of H⁻, H⁰, and H⁺ as a function of Fermi energy relative to VBM.
- schema:
  - `type`: table
  - `required_columns`: `Fermi_energy_eV`, `Ef_H_minus_eV`, `Ef_H_zero_eV`, `Ef_H_plus_eV`
  - `units`:
    - `Fermi_energy_eV`: eV
    - `Ef_H_minus_eV`: eV
    - `Ef_H_zero_eV`: eV
    - `Ef_H_plus_eV`: eV

### charge_transition_levels.json
- path: `/app/outputs/charge_transition_levels.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The (+/−) charge transition level position relative to the valence band maximum and conduction band minimum.
- schema:
  - `type`: object
  - `required`:
    - `transition_energy_above_VBM_eV`: number
    - `transition_energy_below_CBM_eV`: number

Notes: The checker will recompute the (+/−) transition level from the formation_energies_Fermi_level.csv by locating the Fermi energy where Ef(H⁻)=Ef(H⁺). The reported charge_transition_levels.json is used for cross-verification but the primary scoring relies on the CSV-derived value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_geometries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "H_minus": {
            "type": "object",
            "required": {
              "Si_H_bond_length_angstrom": "number",
              "description": "string"
            }
          },
          "H_zero": {
            "type": "object",
            "required": {
              "distance_to_nearest_oxygen_angstrom": "number",
              "description": "string"
            }
          },
          "H_plus": {
            "type": "object",
            "required": {
              "O_H_bond_length_angstrom": "number",
              "description": "string"
            }
          }
        }
      },
      "description": "Relaxed bond lengths for the three charge states of interstitial hydrogen in quartz SiO₂."
    },
    {
      "file": "formation_energies_Fermi_level.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Fermi_energy_eV",
          "Ef_H_minus_eV",
          "Ef_H_zero_eV",
          "Ef_H_plus_eV"
        ],
        "units": {
          "Fermi_energy_eV": "eV",
          "Ef_H_minus_eV": "eV",
          "Ef_H_zero_eV": "eV",
          "Ef_H_plus_eV": "eV"
        }
      },
      "description": "Formation energies of H⁻, H⁰, and H⁺ as a function of Fermi energy relative to VBM."
    },
    {
      "file": "charge_transition_levels.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "transition_energy_above_VBM_eV": "number",
          "transition_energy_below_CBM_eV": "number"
        }
      },
      "description": "The (+/−) charge transition level position relative to the valence band maximum and conduction band minimum."
    }
  ],
  "notes": "The checker will recompute the (+/−) transition level from the formation_energies_Fermi_level.csv by locating the Fermi energy where Ef(H⁻)=Ef(H⁺). The reported charge_transition_levels.json is used for cross-verification but the primary scoring relies on the CSV-derived value."
}
```

## How you are scored
A hidden verifier evaluates your submission after the task finishes. It scores each scored artifact independently and combines the results into an overall reward (0 to 1). For the geometry output it checks whether the reported bond lengths are present and are physically reasonable, comparing them to a hidden reference. For the formation‑energy CSV it verifies the file structure and then recomputes the (+/−) transition level; the recomputed value is compared to a hidden reference with a tolerance that allows for numerical differences between codes. The self‑reported transition level is also checked for consistency with the CSV. Simply writing down expected numbers without actually running the DFT workflow will not produce a valid score; only artifacts generated by a genuine computation that follow the requested protocol will satisfy the verifier.
