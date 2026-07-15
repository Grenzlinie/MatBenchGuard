# Hydrogen desorption energy calculation in NaAlH4 supercells with DFT

## Problem background
Sodium alanate (NaAlH4) is a candidate material for solid-state hydrogen storage, offering high gravimetric hydrogen capacity. However, the strong chemical bonding in the pristine compound leads to hydrogen desorption temperatures that are too high for practical applications. Experiments have shown that adding titanium-based precursors and the creation of lattice vacancies can lower the desorption temperature significantly. Understanding the energetics of hydrogen removal from pure, Ti-doped, and vacancy-containing NaAlH4 is critical for rationally improving storage performance. This task aims to compute the hydrogen desorption energy from several NaAlH4 supercell configurations using density functional theory (DFT), including pristine, Ti-substituted (at a Na site), Na-vacancy, and Al-vacancy systems.

## Approach
We use plane-wave DFT with the generalized gradient approximation (GGA-PBE) and projector augmented wave (PAW) pseudopotentials, as implemented in Quantum ESPRESSO. A 2×2×1 96‑atom supercell of tetragonal NaAlH4 (space group I41/a) is constructed. Four supercell configurations are studied: pristine Na16Al16H64; Ti substituted at one Na site, (TiNa15)Al16H64; a Na vacancy, Na15Al16H64; and an Al vacancy, Na16Al15H64. For each configuration, the intact supercell is relaxed (atomic positions and cell c/a ratio), and then the hydrogen atom closest to the defect (or a representative H in the pristine case) is removed to create a 95‑atom supercell, which is also relaxed. Finally, the spin-polarized total energy of an isolated H2 molecule is computed in a large simulation box. From the set of total energies, hydrogen desorption energies (Ed and Ed+½ E[H2]) are derived. The central comparison is across the four different chemical environments to assess how doping and vacancies modulate the energy cost of hydrogen removal.

## Reproduction target
Produce the file `total_energies.json` in `/app/outputs/` containing the DFT total energies (in eV) for the eight supercell systems plus the H2 molecule, using the keys: E_total_pristine, E_total_pristine_minus_H, E_total_Ti_Na, E_total_Ti_Na_minus_H, E_total_Na_vacancy, E_total_Na_vacancy_minus_H, E_total_Al_vacancy, E_total_Al_vacancy_minus_H, E_total_H2. The hidden verifier will compute the hydrogen desorption energy ΔE^H = E(removed‑H) − E(intact) and the referenced desorption energy ΔE^H + ½ E[H₂] for each system. Your submission is scored on the accuracy of these derived energies (compared to reference values with appropriate tolerances) and on whether the relative ordering among the four chemical conditions and the sign of the referenced desorption energies match the physical behavior of these materials. The exact ordering and sign criteria are not disclosed, but they follow from a correct DFT treatment of the systems.

## Assets

- Quantum ESPRESSO: conda install -c conda-forge qe
- PAW pseudopotentials (Na, Al, H, Ti, PBE): https://www.quantum-espresso.org/pseudopotentials
- NaAlH4 crystal structure

## Workflow steps

### Step 1: DFT geometry relaxations for all supercells and H2 molecule
- Role: process
- Action: Set up and run DFT geometry relaxations using Quantum ESPRESSO with GGA-PBE functional and PAW pseudopotentials. Build a 2×2×1 96‑atom supercell of NaAlH4 (space group I41/a). Optimise lattice c/a and atomic positions for (i) pristine Na16Al16H64, (ii) Ti substituted at a Na site (TiNa15)Al16H64, (iii) Na vacancy Na15Al16H64, and (iv) Al vacancy Na16Al15H64. For each intact supercell, remove one specific H atom (the one nearest the defect) and re‑relax the resulting 95‑atom structure. Also compute the spin‑polarized total energy of an isolated H2 molecule in a large box. Use appropriate convergence settings for energy cutoff and k‑point grids.
- Evidence: `/app/outputs/qe_run.log`

### Step 2: Collect total DFT energies
- Role: scored (load-bearing)
- Action: Extract the final total energy (in eV) for each supercell and the H2 molecule from the DFT outputs and write them into a JSON file with keys: E_total_pristine, E_total_pristine_minus_H, E_total_Ti_Na, E_total_Ti_Na_minus_H, E_total_Na_vacancy, E_total_Na_vacancy_minus_H, E_total_Al_vacancy, E_total_Al_vacancy_minus_H, E_total_H2.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: JSON object with keys: E_total_pristine, E_total_pristine_minus_H, E_total_Ti_Na, E_total_Ti_Na_minus_H, E_total_Na_vacancy, E_total_Na_vacancy_minus_H, E_total_Al_vacancy, E_total_Al_vacancy_minus_H, E_total_H2. Each value is a float (eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT total energies from which hydrogen desorption energies (ΔE^H) and referenced desorption energies (ΔE^H + 1/2 E[H₂]) are recomputed by the checker.
- schema:
  - `type`: object
  - `required`: `E_total_pristine`, `E_total_pristine_minus_H`, `E_total_Ti_Na`, `E_total_Ti_Na_minus_H`, `E_total_Na_vacancy`, `E_total_Na_vacancy_minus_H`, `E_total_Al_vacancy`, `E_total_Al_vacancy_minus_H`, `E_total_H2`
  - `properties`:
    - `E_total_pristine`:
      - `type`: number
      - `unit`: eV
    - `E_total_pristine_minus_H`:
      - `type`: number
      - `unit`: eV
    - `E_total_Ti_Na`:
      - `type`: number
      - `unit`: eV
    - `E_total_Ti_Na_minus_H`:
      - `type`: number
      - `unit`: eV
    - `E_total_Na_vacancy`:
      - `type`: number
      - `unit`: eV
    - `E_total_Na_vacancy_minus_H`:
      - `type`: number
      - `unit`: eV
    - `E_total_Al_vacancy`:
      - `type`: number
      - `unit`: eV
    - `E_total_Al_vacancy_minus_H`:
      - `type`: number
      - `unit`: eV
    - `E_total_H2`:
      - `type`: number
      - `unit`: eV

Notes: The hidden checker will compute Ed and Ed_ref for each system, compare against paper-reported reference values with tolerances, and enforce the ordering Ed(pristine) > Ed(Ti_Na) > Ed(Al_vacancy) > Ed(Na_vacancy) and the sign conditions on Ed_ref.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "E_total_pristine",
          "E_total_pristine_minus_H",
          "E_total_Ti_Na",
          "E_total_Ti_Na_minus_H",
          "E_total_Na_vacancy",
          "E_total_Na_vacancy_minus_H",
          "E_total_Al_vacancy",
          "E_total_Al_vacancy_minus_H",
          "E_total_H2"
        ],
        "properties": {
          "E_total_pristine": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_pristine_minus_H": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Ti_Na": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Ti_Na_minus_H": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Na_vacancy": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Na_vacancy_minus_H": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Al_vacancy": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_Al_vacancy_minus_H": {
            "type": "number",
            "unit": "eV"
          },
          "E_total_H2": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Raw DFT total energies from which hydrogen desorption energies (ΔE^H) and referenced desorption energies (ΔE^H + 1/2 E[H₂]) are recomputed by the checker."
    }
  ],
  "notes": "The hidden checker will compute Ed and Ed_ref for each system, compare against paper-reported reference values with tolerances, and enforce the ordering Ed(pristine) > Ed(Ti_Na) > Ed(Al_vacancy) > Ed(Na_vacancy) and the sign conditions on Ed_ref."
}
```

## How you are scored
A hidden verifier reads your `total_energies.json` and recomputes the hydrogen desorption energies and referenced desorption energies. The verifier checks these quantities for agreement with expected values and for consistency with known physical trends, using tolerances that account for implementation‑dependent variations. The final reward is a weighted sum of partial scores from each verification step. The majority of the score is based on the magnitude of the derived desorption energies; additional points are awarded for correct relative ordering and sign patterns. Simply submitting literature values without executing the required DFT calculations will not receive a passing score.
