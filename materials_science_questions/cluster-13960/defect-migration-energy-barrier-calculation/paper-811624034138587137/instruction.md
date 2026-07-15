# Compute defect energetics and migration barriers for SiC precipitation in Si using DFT

## Problem background
Silicon carbide precipitation in silicon during carbon implantation is of technological importance for forming 3C-SiC thin films. Two competing mechanisms are debated: (1) precipitation by agglomeration of interstitial carbon (C_i) dimers, or (2) successive agglomeration of substitutional carbon (C_s) atoms. The goal of this reproduction is to compute key defect energetics and migration barriers using first‑principles DFT to determine which pathway is more plausible.

## Approach
We use plane‑wave density functional theory (DFT) with the PW91 exchange‑correlation functional and norm‑conserving ultrasoft pseudopotentials. All calculations are performed on a cubic 216‑atom Si supercell with Γ‑point Brillouin‑zone sampling.

1. **Point‑defect formation energies** – Build the supercell for a perfect Si lattice, then introduce the defects (C_s, C_i ⟨100⟩ dumbbell, Si_i ⟨110⟩ dumbbell, vacancy) and perform ionic relaxations. Compute formation energies relative to a SiC reservoir.
2. **Defect‑pair binding energies** – For the most stable Ci‑Ci, Ci‑vacancy, and Cs‑Si_i pairs, relax the combined structure and compute the binding energy as the difference between the formation energy of the complex and the sum of the isolated defect energies.
3. **NEB migration barriers** – Use the nudged elastic band (or climbing‑image NEB) method to determine the minimum‑energy path and barrier height for three transitions: (a) Ci diffusion between two ⟨100⟩ dumbbell orientations, (b) Ci+vacancy → C_s, and (c) C_s+Si_i → C_i.
4. **Ab initio molecular dynamics (AIMD)** – Starting from the C_s+Si_i pair, run AIMD at 900 °C for at least 1 ps and record whether the Si_i separates from C_s by more than 4 neighbour distances.
5. **Report compilation** – Gather all results into a single JSON file.

## Reproduction target
Produce a JSON file `/app/outputs/defect_energies.json` that contains the following quantities:
- **formation_energies** (in eV): formation energies for the point defects `Cs`, `Ci_100_DB`, `Sii_110_DB`, and `V`.
- **binding_energies** (in eV): binding energies for the defect pairs `Ci_Ci` (Ci ⟨100⟩ DB pair with orientation [0 -1 0] at position 1), `Ci_V` (Ci ⟨100⟩ DB next to a vacancy at position 1), and `Cs_Sii` (C_s next to a Si_i ⟨110⟩ DB in configuration I).
- **migration_barriers** (in eV): energy barriers for `Ci_diff` (Ci [0 0 -1] DB → [0 -1 0] DB), `CiV_to_Cs` (Ci+vacancy at position 3 → C_s), and `CsSii_to_Ci` (C_s+Si_i [110] DB → Ci [100] DB).
- **md_result**: string `"separated"` if during the 900 °C AIMD the Si_i moves more than 4 neighbour distances away from C_s, otherwise `"not_separated"`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- C PAW pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- Si PAW pseudopotential: https://www.materialscloud.org/discover/sssp/table/efficiency
- Si crystal structure

## Workflow steps

### Step 1: DFT defect formation energies
- Role: process
- Action: Build a 216-atom cubic diamond Si supercell and compute formation energies for substitutional C (Cs), C interstitial <100> dumbbell (Ci), Si self-interstitial <110> dumbbell (Sii), and vacancy (V) using DFT with Quantum ESPRESSO. Use the PW91 exchange-correlation functional with ultrasoft pseudopotentials and Γ-point sampling.
- Evidence: `/app/outputs/defect_relaxations.log`

### Step 2: DFT binding energies of defect pairs
- Role: process
- Action: Compute binding energies for the most stable Ci-Ci pair (orientation [0 -1 0] at position 1), Ci-vacancy pair (vacancy at position 1), and Cs-Sii pair (configuration I) using DFT relaxations on the 216-atom supercell.
- Evidence: `/app/outputs/binding_energy_calcs.log`

### Step 3: NEB migration barriers
- Role: process
- Action: Perform nudged elastic band (NEB) or climbing-image NEB calculations to determine migration barriers for: (a) Ci diffusion via [0 0 -1] DB to [0 -1 0] DB transition; (b) Ci+vacancy at position 3 transforming to Cs; (c) Cs+Sii [110] DB transforming to Ci [100] DB. Extract the barrier heights in eV.
- Evidence: `/app/outputs/neb_calcs.log`

### Step 4: AIMD separation simulation
- Role: process
- Action: Run ab initio molecular dynamics at 900 °C for at least 1 ps starting from the Cs+Sii configuration I. Record whether the Sii separates from Cs by more than 4 neighbor distances.
- Evidence: `/app/outputs/aimd.log`

### Step 5: Compile final defect energetics report
- Role: scored (load-bearing)
- Action: Compile all computed results into defect_energies.json, containing formation_energies, binding_energies, migration_barriers, and md_result.
- Output file: `/app/outputs/defect_energies.json`
- Format: json
- Contract: formation_energies: object with keys 'Cs', 'Ci_100_DB', 'Sii_110_DB', 'V'; binding_energies: object with keys 'Ci_Ci', 'Ci_V', 'Cs_Sii'; migration_barriers: object with keys 'Ci_diff', 'CiV_to_Cs', 'CsSii_to_Ci'; md_result: string.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_energies.json
- path: `/app/outputs/defect_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing formation_energies, binding_energies, migration_barriers, and md_result; compared to hidden reference values from the paper.
- schema:
  - `type`: object
  - `required_keys`: `formation_energies`, `binding_energies`, `migration_barriers`, `md_result`
  - `formation_energies`:
    - `type`: object
    - `required_keys`: `Cs`, `Ci_100_DB`, `Sii_110_DB`, `V`
  - `binding_energies`:
    - `type`: object
    - `required_keys`: `Ci_Ci`, `Ci_V`, `Cs_Sii`
  - `migration_barriers`:
    - `type`: object
    - `required_keys`: `Ci_diff`, `CiV_to_Cs`, `CsSii_to_Ci`
  - `md_result`:
    - `type`: string
    - `enum`: `separated`, `not_separated`

Notes: All energies and barriers in eV. The md_result must be either 'separated' or 'not_separated'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "formation_energies",
          "binding_energies",
          "migration_barriers",
          "md_result"
        ],
        "formation_energies": {
          "type": "object",
          "required_keys": [
            "Cs",
            "Ci_100_DB",
            "Sii_110_DB",
            "V"
          ]
        },
        "binding_energies": {
          "type": "object",
          "required_keys": [
            "Ci_Ci",
            "Ci_V",
            "Cs_Sii"
          ]
        },
        "migration_barriers": {
          "type": "object",
          "required_keys": [
            "Ci_diff",
            "CiV_to_Cs",
            "CsSii_to_Ci"
          ]
        },
        "md_result": {
          "type": "string",
          "enum": [
            "separated",
            "not_separated"
          ]
        }
      },
      "description": "JSON file containing formation_energies, binding_energies, migration_barriers, and md_result; compared to hidden reference values from the paper."
    }
  ],
  "notes": "All energies and barriers in eV. The md_result must be either 'separated' or 'not_separated'."
}
```

## How you are scored
A hidden verifier reads your `defect_energies.json` and compares each reported value (formation energies, binding energies, migration barriers, and the separation outcome) to independently established reference values. Each quantity is checked for agreement within a preset tolerance. Your final score is the fraction of quantities that fall within their respective tolerances. To obtain full credit, every computed quantity must be within tolerance. The verifier does not require bit‑exact agreement; small deviations due to different computational implementation are expected and accounted for.
