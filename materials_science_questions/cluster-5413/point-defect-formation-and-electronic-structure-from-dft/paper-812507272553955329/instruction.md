# DFT calculation of hydrogen trapping in vacancy-oxygen complexes of Ti3AlC2

## Problem background
In nuclear fusion environments, structural materials like Ti3AlC2 must withstand simultaneous irradiation and high-temperature oxidation. Irradiation generates hydrogen (H) and helium (He) impurities as well as lattice vacancies; soluble oxygen (O) impurities from oxidation interact strongly with these defects. Understanding how O modifies the ability of Al vacancies to trap H atoms is critical for predicting hydrogen embrittlement and swelling. Density functional theory (DFT) calculations can quantify the maximum number of H atoms that different vacancy‑O complexes can accommodate before the energy penalty for adding another H becomes positive. This task reproduces that key calculation.

## Approach
The method uses plane‑wave DFT with the PBE exchange‑correlation functional and PAW pseudopotentials. Starting from the published crystal structure of Ti3AlC2, a 3×3×1 supercell is built and relaxed. Reference energies are computed for the perfect bulk supercell and for one isolated H interstitial placed at its most stable site. Four vacancy‑O complexes are then constructed by introducing the required number of Al vacancies (V_Al and 2V_Al‑Al) and placing O atoms at the preferred interstitial sites near the vacancies; one complex also includes a He atom. For each complex, H atoms are added one by one. After each addition the structure is relaxed and the total energy is recorded. The trapping energy of the n‑th H is defined as the difference between the energy of the complex containing n H atoms and that containing n−1 H atoms, relative to the energy of an isolated H interstitial and the energy of the perfect supercell. The process continues as long as the trapping energy remains negative; the largest n for which this holds is the maximum trapping capacity for that complex. The entire workflow is carried out with the open‑source Quantum ESPRESSO code and publicly available pseudopotentials.

## Reproduction target
Produce a JSON file `/app/outputs/h_trapping_maxima.json` that contains four integers: the maximum number of H atoms that can be trapped (i.e., the last n for which the trapping energy is negative) for each of the four vacancy‑O complexes, using exactly the keys `"V-O"`, `"2V-O"`, `"2V-2O"`, and `"2V-O-He"`. The calculation must be performed with Quantum ESPRESSO using the PBE functional and PAW pseudopotentials from the SSSP library.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Pseudopotential Library (PBE PAW): https://www.materialscloud.org/discover/sssp
- Ti3AlC2 crystal structure

## Workflow steps

### Step 1: Reference calculations: bulk Ti3AlC2 and isolated H interstitial
- Role: process
- Action: Construct a 3×3×1 supercell of Ti3AlC2 using the published lattice constants. Fully relax the atomic positions and cell parameters using DFT with PBE functional. Record the total energy E(ref) of the perfect supercell. Additionally, place one H atom at its most stable interstitial site (I_tetr-2) in the supercell, relax, and obtain the energy E(H_int) to be used as reference for trapping energy calculations.
- Evidence: `/app/outputs/reference_energies.txt`

### Step 2: Construct vacancy-O complexes
- Role: process
- Action: Create supercells containing the required Al vacancies (V_Al and 2V_Al-Al). For each target complex (V-O, 2V-O, 2V-2O, 2V-O-He), place O atoms at the determined most favorable interstitial sites (I_tetr-2) and, for the He-containing complex, also place a He atom at a suitable site. Relax the geometry of each complex to obtain the base energy without H.
- Evidence: `/app/outputs/complexes.log`

### Step 3: Sequential H addition and trapping energy calculation
- Role: process
- Action: For each of the four complexes, add H atoms one by one. After adding each H atom, relax the structure and record the total energy E(nH,complex). Compute the trapping energy of the n‑th H atom using E_trap(nH) = E(nH,complex) - E[(n-1)H,complex] - E(H_int) + E(ref). Continue until the trapping energy becomes positive. Save all trapping energies per complex in a file trapping_energies.json for auditing.
- Evidence: `/app/outputs/trapping_energies.json`

### Step 4: Output H trapping maxima
- Role: scored (load-bearing)
- Action: From the computed trapping energies, determine the largest number of H atoms that can be trapped (i.e., the last n for which E_trap remains negative) for each of the four complexes. Write a JSON file containing these four integers.
- Output file: `/app/outputs/h_trapping_maxima.json`
- Format: json
- Contract: {"V-O": int, "2V-O": int, "2V-2O": int, "2V-O-He": int}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/h_trapping_maxima.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### h_trapping_maxima.json
- path: `/app/outputs/h_trapping_maxima.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Maximum number of H atoms that can be trapped by each vacancy‑O complex before the trapping energy turns positive. All four integers must exactly match the hidden reference.
- schema:
  - `type`: object
  - `required`:
    - `V-O`: integer
    - `2V-O`: integer
    - `2V-2O`: integer
    - `2V-O-He`: integer

Notes: The hidden checker will compare the agent's four integers to the paper's reported values. Exact match for each integer is required; any discrepancy results in zero credit for the affected entry. The optional trapping_energies.json evidence file is not scored but may be used for a consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "h_trapping_maxima.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V-O": "integer",
          "2V-O": "integer",
          "2V-2O": "integer",
          "2V-O-He": "integer"
        }
      },
      "description": "Maximum number of H atoms that can be trapped by each vacancy‑O complex before the trapping energy turns positive. All four integers must exactly match the hidden reference."
    }
  ],
  "notes": "The hidden checker will compare the agent's four integers to the paper's reported values. Exact match for each integer is required; any discrepancy results in zero credit for the affected entry. The optional trapping_energies.json evidence file is not scored but may be used for a consistency check."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your `h_trapping_maxima.json` and compares each integer against the correct reference maximum for that complex. Each of the four integers carries equal weight; a fully correct set earns full credit, while any discrepancy reduces the score proportionally. Additionally, the optional `trapping_energies.json` may be inspected for consistency (e.g., trapping energy is negative for the reported n and positive for n+1), but the final score is determined by the four maxima integers.
