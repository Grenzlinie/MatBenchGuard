# First-Principles Study of Oxygen-Terminated Chevron Graphene Nanoribbon Properties

## Problem background
Graphene nanoribbons (GNRs) are narrow stripes of graphene whose electronic and magnetic properties are strongly influenced by their edge geometry and termination. Chevron-type zigzag-edge GNRs (CZGNRs) contain alternating kink angles (120° or 60°) and are promising for carbon-based nanoelectronics and spintronics. When the edges are passivated by oxygen, the interplay of ribbon width, length, and kink geometry can lead to a variety of ground-state magnetic orderings and electronic characters—semiconducting or metallic—different from the commonly studied hydrogen-terminated case. Predicting which magnetic configuration (nonmagnetic, ferromagnetic, or antiferromagnetic ordering) is most stable and whether the system becomes a semiconductor or a metal, as well as how much magnetization resides on the oxygen atoms, requires first-principles spin-polarised density functional theory (DFT) calculations. This task reproduces that series of calculations for two representative O-terminated CZGNR structures.

## Approach
Use first-principles DFT in the spin-polarised generalised gradient approximation with the Perdew-Burke-Ernzerhof (PBE) functional, implemented in the open-source Quantum ESPRESSO package, together with SSSP PBE pseudopotentials for carbon and oxygen. Both the ionic positions and the lattice constant along the ribbon axis are relaxed until forces are small; a tetragonal supercell with sufficient vacuum isolates the quasi-one-dimensional ribbon. For each structure, several initial magnetic configurations must be set up and relaxed to convergence: nonmagnetic (NM), ferromagnetic (FM), and the antiferromagnetic configurations relevant to the ribbon geometry—AFM-G for the ZO(3,6) structure and AFM-S for ZA(3,8). The total energies of the converged configurations are compared to identify the ground state. For that ground state, compute the band structure along a representative high-symmetry k‑path and extract the band gap in meV, marking the system as metallic when the gap vanishes. Use Bader charge analysis on the ground‑state charge density to obtain local magnetic moments on oxygen atoms (for ZO(3,6)) or the total magnetization per unit cell (for ZA(3,8)).

## Reproduction target
Construct atomic geometries for O-terminated ZO(3,6) and ZA(3,8) chevron GNRs as defined by their (n,m) parameters and 120° or 60° kink angles, terminating all edge carbon dangling bonds with oxygen. For each structure, perform spin-polarised DFT relaxation and total-energy calculations for the relevant magnetic configurations (NM, FM, AFM‑G for ZO(3,6); NM, FM, AFM‑S for ZA(3,8)). Identify the ground state as the configuration with the lowest total energy. For the ground state, compute the electronic band structure and extract the band gap in meV (or report 0 if metallic). Perform Bader charge analysis on the ground‑state charge density. Write the results to two JSON files:
- `ZO36_results.json`: keys "structure" ("ZO(3,6)"), "ground_state" (string), "energy_NM", "energy_FM", "energy_AFMG" (numbers, energies expressed relative to NM=0), "band_gap_meV" (number), "oxygen_moment_min", "oxygen_moment_max" (numbers).
- `ZA38_results.json`: keys "structure" ("ZA(3,8)"), "ground_state" (string), "energy_NM", "energy_FM", "energy_AFMS" (numbers, relative to NM=0), "band_gap_meV" (number; use 0 for metallic), "total_magnetization_muB" (number).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE Pseudopotential Library: https://www.materialscloud.org/discover/sssp/table/efficiency
- Bader Charge Analysis: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Construct atomic geometries
- Role: process
- Action: Generate the atomic structures for O-terminated ZO(3,6) and ZA(3,8) chevron GNRs: (n,m)=(3,6) with 120° kink for ZO and (n,m)=(3,8) with 60° kink for ZA. Terminate all edge carbon dangling bonds with oxygen atoms. Build periodic supercells along the ribbon axis with sufficient vacuum in perpendicular directions.
- Evidence: `/app/outputs/geometry_check.txt`

### Step 2: Spin-polarized DFT total-energy calculations
- Role: process
- Action: For each structure, set up the required initial magnetic configurations: NM, FM, and AFM-G for ZO(3,6); NM, FM, and AFM-S for ZA(3,8). Run spin-polarized DFT geometry relaxation and total-energy calculation using Quantum ESPRESSO (PBE functional, SSSP pseudopotentials). Save the converged total energies and final magnetic states.
- Evidence: `/app/outputs/dft_calculations.log`

### Step 3: Scored analysis: ZO(3,6) results
- Role: scored (load-bearing)
- Action: From the DFT results for ZO(3,6), identify the ground state as the spin configuration with the lowest total energy among the converged states. For the ground state, compute the band structure along a suitable k-path and extract the band gap (in meV). Perform Bader charge analysis on the ground-state charge density to obtain the minimum and maximum absolute local magnetic moments on oxygen atoms. Write all results to ZO36_results.json.
- Output file: `/app/outputs/ZO36_results.json`
- Format: json
- Contract: {"structure": "ZO(3,6)", "ground_state": string, "energy_NM": number, "energy_FM": number, "energy_AFMG": number, "band_gap_meV": number, "oxygen_moment_min": number, "oxygen_moment_max": number}
- Scoring: scored by hidden verifier

### Step 4: Scored analysis: ZA(3,8) results
- Role: scored (load-bearing)
- Action: From the DFT results for ZA(3,8), identify the ground state as the spin configuration with the lowest total energy among NM, FM, and AFM-S. For the ground state, compute the band structure and determine whether it is semiconducting (report gap in meV) or metallic (report 0). Perform Bader charge analysis on the ground-state charge density to obtain the total magnetization in the unit cell. Write results to ZA38_results.json.
- Output file: `/app/outputs/ZA38_results.json`
- Format: json
- Contract: {"structure": "ZA(3,8)", "ground_state": string, "energy_NM": number, "energy_FM": number, "energy_AFMS": number, "band_gap_meV": number, "total_magnetization_muB": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ZO36_results.json`
- `/app/outputs/ZA38_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ZO36_results.json
- path: `/app/outputs/ZO36_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored results for O-terminated ZO(3,6). Contains the identified magnetic ground state, total energies relative to NM, the band gap, and the range of oxygen local magnetic moments.
- schema:
  - `type`: object
  - `required`:
    - `structure`: string
    - `ground_state`: string
    - `energy_NM`: number
    - `energy_FM`: number
    - `energy_AFMG`: number
    - `band_gap_meV`: number
    - `oxygen_moment_min`: number
    - `oxygen_moment_max`: number

### ZA38_results.json
- path: `/app/outputs/ZA38_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored results for O-terminated ZA(3,8). Contains the identified magnetic ground state, total energies relative to NM, band gap (0 denotes metallic), and total magnetization per unit cell.
- schema:
  - `type`: object
  - `required`:
    - `structure`: string
    - `ground_state`: string
    - `energy_NM`: number
    - `energy_FM`: number
    - `energy_AFMS`: number
    - `band_gap_meV`: number
    - `total_magnetization_muB`: number

Notes: No gold values or tolerances are revealed. The checker verifies the ground-state string, energy ordering, band-gap magnitude, and magnetic moment range against paper-reported references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ZO36_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "structure": "string",
          "ground_state": "string",
          "energy_NM": "number",
          "energy_FM": "number",
          "energy_AFMG": "number",
          "band_gap_meV": "number",
          "oxygen_moment_min": "number",
          "oxygen_moment_max": "number"
        }
      },
      "description": "Scored results for O-terminated ZO(3,6). Contains the identified magnetic ground state, total energies relative to NM, the band gap, and the range of oxygen local magnetic moments."
    },
    {
      "file": "ZA38_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "structure": "string",
          "ground_state": "string",
          "energy_NM": "number",
          "energy_FM": "number",
          "energy_AFMS": "number",
          "band_gap_meV": "number",
          "total_magnetization_muB": "number"
        }
      },
      "description": "Scored results for O-terminated ZA(3,8). Contains the identified magnetic ground state, total energies relative to NM, band gap (0 denotes metallic), and total magnetization per unit cell."
    }
  ],
  "notes": "No gold values or tolerances are revealed. The checker verifies the ground-state string, energy ordering, band-gap magnitude, and magnetic moment range against paper-reported references."
}
```

## How you are scored
A hidden verifier will read the two output JSON files. It will check, for each structure, whether the reported ground state label matches the expected one, whether the ground state energy is indeed lower than the other reported energies (energy ordering condition), whether the band gap falls in the appropriate range for the claimed semiconductor/metallic character, and whether the oxygen magnetic moment range or total magnetization lies in a physically reasonable interval. The final score is a weighted combination of partial credits awarded for each condition satisfied. You must produce the artifacts exactly as described; reporting a number is not enough—the verifier compares your computed values against the paper’s confidential reference results.
