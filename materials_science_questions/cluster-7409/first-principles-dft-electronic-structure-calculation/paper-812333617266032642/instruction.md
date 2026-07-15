# First-principles DFT of InTaO4 with oxygen vacancies and Ni doping: electronic structure and gap states

## Problem background
InTaO4 is a promising oxide semiconductor for photocatalytic water splitting, but its wide band gap limits activity under visible light. Introducing defects such as oxygen vacancies or doping with transition metals can alter its electronic structure, potentially creating in-gap states and narrowing the band gap to enable visible-light absorption. Understanding these modifications quantitatively is essential for designing efficient photocatalysts. This task investigates whether oxygen vacancies induce occupied states within the gap and whether Ni doping further reduces the effective band gap by computing the relevant energy levels from first-principles density functional theory (DFT).

## Approach
Perform spin-polarized DFT calculations on a 2×2×1 supercell of wolframite InTaO4 (space group P2/a) using the generalized gradient approximation (GGA) and an appropriate pseudopotential set. Three configurations are modeled: (i) pristine InTaO4, (ii) a supercell with a single O(1) oxygen vacancy, and (iii) a supercell where one In atom is replaced by Ni (nominally In0.875Ni0.125TaO4). For each configuration, relax the atomic positions and compute the total density of states (TDOS). From the TDOS, extract (a) the pristine band gap as the energy difference between the valence band maximum and conduction band minimum, (b) for the oxygen vacancy system, the energy difference between the highest occupied gap state and the conduction band minimum, and (c) for the Ni-doped system, the effective band gap. These values determine the role of vacancies and doping in modifying the electronic structure.

## Reproduction target
Compute and report three energy values (all in eV) derived from the DFT total density of states for the three supercell configurations:  
1. **Pristine band gap** — the energy gap between the valence band maximum and conduction band minimum of pristine InTaO4.  
2. **Oxygen vacancy gap‑state‑to‑CB transition energy** — the energy difference between the highest occupied oxygen‑vacancy‑induced gap state and the conduction band minimum.  
3. **Ni‑doped effective band gap** — the smallest gap involving the new doping‑induced states in Ni‑doped InTaO4.  
Additionally, ensure the computed values satisfy the ordering: pristine band gap > oxygen vacancy transition energy, and pristine band gap > Ni‑doped effective band gap. Write these three values (floats, in eV) as a JSON object with keys `pristine_band_gap_eV`, `ovacancy_GS_to_CB_eV`, `Nidoped_band_gap_eV` to `/app/outputs/results.json`.

## Assets

- Wolframite InTaO4 crystal structure (space group P2/a): 10.1016/S0022-3697(02)00007-7
- Plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org
- Ultrasoft/PAW pseudopotentials for In, Ta, O, Ni: https://pseudopotentials.quantum-espresso.org

## Workflow steps

### Step 1: Structure preparation
- Role: process
- Action: Construct a 2x2x1 supercell of wolframite InTaO4 (space group P2/a) using known lattice parameters from the literature. Save the pristine supercell in a format readable by the chosen DFT code (e.g., CIF, POSCAR).
- Evidence: `/app/outputs/pristine_supercell.cif`

### Step 2: Pristine DFT calculation
- Role: process
- Action: Perform spin-polarized DFT structural relaxation and total density-of-states (TDOS) calculation on the pristine supercell using the GGA functional and a chosen pseudopotential set. Save the TDOS data and total energy.
- Evidence: `/app/outputs/pristine_dos.dat`

### Step 3: Oxygen vacancy calculation
- Role: process
- Action: Create a supercell with a single O(1) oxygen vacancy (remove one O from the 16 O(1) sites). Relax atomic positions using the same DFT settings, then compute the TDOS.
- Evidence: `/app/outputs/ovacancy_dos.dat`

### Step 4: Ni-doped calculation
- Role: process
- Action: Create a supercell where one In atom is replaced by Ni (corresponding to In0.875Ni0.125TaO4). Relax atomic positions and compute the TDOS.
- Evidence: `/app/outputs/nidoped_dos.dat`

### Step 5: Extract key energy values from DOS
- Role: scored (load-bearing)
- Action: From the computed TDOS: (a) determine pristine band gap as the energy difference between valence band maximum and conduction band minimum; (b) for the O-vacancy system, identify the highest occupied gap state energy and the conduction band minimum energy, and compute their difference; (c) for the Ni-doped system, determine the effective band gap. Write a JSON file with keys pristine_band_gap_eV, ovacancy_GS_to_CB_eV, Nidoped_band_gap_eV (all floats in units of eV) to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"pristine_band_gap_eV": <float>, "ovacancy_GS_to_CB_eV": <float>, "Nidoped_band_gap_eV": <float>}
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
- description: Energy values from DFT calculations: pristine band gap, oxygen vacancy gap-to-CB transition energy, Ni-doped effective band gap. The checker also verifies the ordering pristine_band_gap_eV > ovacancy_GS_to_CB_eV and pristine_band_gap_eV > Nidoped_band_gap_eV.
- schema:
  - `type`: object
  - `required`: `pristine_band_gap_eV`, `ovacancy_GS_to_CB_eV`, `Nidoped_band_gap_eV`
  - `properties`:
    - `pristine_band_gap_eV`:
      - `type`: number
      - `unit`: eV
    - `ovacancy_GS_to_CB_eV`:
      - `type`: number
      - `unit`: eV
    - `Nidoped_band_gap_eV`:
      - `type`: number
      - `unit`: eV

Notes: The three energy values must be extracted from the DFT-computed DOS. The checker uses hidden paper-reported reference values with tolerances and verifies the required ordering.

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
          "pristine_band_gap_eV",
          "ovacancy_GS_to_CB_eV",
          "Nidoped_band_gap_eV"
        ],
        "properties": {
          "pristine_band_gap_eV": {
            "type": "number",
            "unit": "eV"
          },
          "ovacancy_GS_to_CB_eV": {
            "type": "number",
            "unit": "eV"
          },
          "Nidoped_band_gap_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Energy values from DFT calculations: pristine band gap, oxygen vacancy gap-to-CB transition energy, Ni-doped effective band gap. The checker also verifies the ordering pristine_band_gap_eV > ovacancy_GS_to_CB_eV and pristine_band_gap_eV > Nidoped_band_gap_eV."
    }
  ],
  "notes": "The three energy values must be extracted from the DFT-computed DOS. The checker uses hidden paper-reported reference values with tolerances and verifies the required ordering."
}
```

## How you are scored
A hidden verifier independently checks your submitted `results.json`. It compares your three energy values against reference benchmarks (not disclosed to you) and verifies the required ordering (pristine gap > the other two energies). Meeting or exceeding the benchmark within a predetermined tolerance yields full credit for that value; values that deviate farther receive reduced credit. The final reward is the weighted combination of the scores for each value. Reporting plausible numbers that satisfy the ordering is not sufficient — the energies must be extracted from a genuine DFT calculation of the three supercell configurations, as described in the workflow steps.
