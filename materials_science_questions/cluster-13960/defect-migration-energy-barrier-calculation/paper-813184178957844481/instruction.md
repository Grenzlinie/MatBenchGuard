# Hydrogen trapping and diffusion in Ti3SiC2: a first-principles study

## Problem background
Ti3SiC2 is a MAX phase ceramic that combines metallic and ceramic properties, making it a candidate for structural components in advanced nuclear reactors. Under neutron irradiation, hydrogen (H) impurities are produced and can be trapped by vacancy defects in the material, potentially degrading mechanical properties through embrittlement. Understanding how H interacts with vacancies in Ti3SiC2—how many H atoms a silicon vacancy can accommodate and the energy required for H to migrate from its trapped site—is essential for assessing the material’s performance in service. This task aims to quantify these trapping and migration properties by performing first-principles calculations.

## Approach
The reproduction uses plane-wave density functional theory (DFT) with the GGA-PW91 exchange–correlation functional and projector augmented-wave (PAW) pseudopotentials. A 2×2×1 supercell of Ti3SiC2 is built from the known hexagonal crystal structure. The reference energies needed for the analysis are obtained by (i) relaxing the perfect supercell, (ii) relaxing a single H atom at the most stable interstitial site (I-SiC, a tetrahedral site surrounded by three Si and one C atom), and (iii) removing one Si atom to create a vacancy and relaxing that supercell. Zero-point energy (ZPE) corrections are computed from the harmonic vibrational frequencies of the H atoms.

To determine trapping energies, H atoms are added sequentially near the Si vacancy: the first H is placed 1.01 Å below the vacancy center, the second on the opposite side forming a dumbbell, the third through fifth are positioned 2.02 Å above Ti(2) atoms in a triangular arrangement, and a sixth H is added similarly. For each n (1 to 6), the atomic positions are relaxed while keeping the cell fixed, the total energy E(nH, V+ref) and ZPE correction are recorded. The ZPE-corrected trapping energy for the nth H atom is calculated as
E_trap(n) = E(nH, V+ref) – E((n-1)H, V+ref) – E(H+I-SiC) + E(bulk)
where E(H+I-SiC) is the energy of one H at the I-SiC interstitial site and E(bulk) is the energy of the perfect supercell.

The diffusion barrier for H migration from its most stable trapped site inside the vacancy (the 1.01 Å below site) to the I-SiC interstitial site is obtained using the climbing-image nudged elastic band (CI-NEB) method. The difference between the saddle-point energy and the initial-image energy gives the barrier.

## Reproduction target
Compute and report the ZPE-corrected trapping energies for n = 1 through 6 H atoms trapped at a Si vacancy in Ti3SiC2. For each n, output the trapping energy (eV), the applied ZPE correction (eV), and the total energy of the V+nH supercell (eV). Additionally, compute the diffusion barrier (in eV) for a H atom migrating from the trapped state inside the vacancy to the I-SiC interstitial site. The results must be written to the specified output files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- GBRV pseudopotential library (PAW for GGA-PW91): https://www.physics.rutgers.edu/gbrv/
- Ti3SiC2 crystal structure

## Workflow steps

### Step 1: Relax perfect Ti3SiC2 supercell
- Role: process
- Action: Build a 2×2×1 supercell of Ti3SiC2 using the published hexagonal crystal structure. Relax the cell shape, volume, and all atomic positions with DFT (Quantum ESPRESSO, GGA-PW91 functional, PAW pseudopotentials) until forces are converged. Record the final total energy and relaxed geometry.
- Evidence: `/app/outputs/perfect_relaxed.log`

### Step 2: Compute single H interstitial energy at I-SiC
- Role: process
- Action: Place one H atom at the I-SiC interstitial site (tetrahedral site surrounded by three Si and one C atom) in the relaxed perfect supercell. Relax the atomic positions (keeping cell fixed) and compute the total energy E(H+ref). Compute the ZPE correction via the harmonic vibrational frequencies of the H atom.
- Evidence: `/app/outputs/H_interstitial.log`

### Step 3: Create and relax Si vacancy supercell
- Role: process
- Action: Remove one Si atom from the relaxed perfect supercell to create a Si vacancy. Relax the cell shape, volume, and atomic positions using the same DFT settings as step_01. Record the total energy of the vacancy supercell E(V+ref).
- Evidence: `/app/outputs/vacancy_relaxed.log`

### Step 4: Multi‑H trapping energies
- Role: scored (load-bearing)
- Action: For n = 1 to 6, place n H atoms near the Si vacancy according to the positions described in the method: first H 1.01 Å below the vacancy, second H on the opposite side forming a dumbbell, third to fifth H 2.02 Å above Ti(2) atoms in a regular triangle arrangement, sixth H added similarly. For each n, relax the atomic positions (keeping cell fixed) and compute the total energy E(nH,V+ref) and the ZPE correction (vibrational frequencies). Compute the ZPE-corrected trapping energy as E_trap(n) = E(nH,V+ref) – E((n-1)H,V+ref) – E(H+ref) + E(ref), using E(0H,V+ref)=E(V+ref) from step_03, E(H+ref) from step_02, and E(ref) from step_01. Compile the results into a JSON file.
- Output file: `/app/outputs/trapping_energies.json`
- Format: json
- Contract: A JSON array of objects, each with keys: n (integer), trapping_energy (number in eV, ZPE-corrected), zpe_correction (number in eV), E_total (number in eV, total energy of the V+ nH supercell).
- Scoring: scored by hidden verifier

### Step 5: Diffusion barrier from vacancy to I-SiC
- Role: scored
- Action: Using the relaxed V_Si + 1H structure (the most stable site, 1.01 Å below vacancy) as the initial image and the H at I-SiC interstitial site (from step_02) as the final image, perform a climbing-image nudged elastic band (CI‑NEB) calculation to find the minimum energy path. Extract the diffusion barrier (the difference in total energy between the saddle point and the initial state). Report the barrier in eV.
- Output file: `/app/outputs/diffusion_barrier.txt`
- Format: txt
- Contract: A single floating-point number representing the barrier in eV (e.g., a positive floating-point number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trapping_energies.json`
- `/app/outputs/diffusion_barrier.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trapping_energies.json
- path: `/app/outputs/trapping_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed ZPE-corrected trapping energies for n=1..6 H atoms in a Si vacancy, along with the ZPE correction and total energy of each configuration.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `n`, `trapping_energy`, `zpe_correction`, `E_total`
    - `properties`:
      - `n`:
        - `type`: integer
      - `trapping_energy`:
        - `type`: number
        - `units`: eV
      - `zpe_correction`:
        - `type`: number
        - `units`: eV
      - `E_total`:
        - `type`: number
        - `units`: eV

### diffusion_barrier.txt
- path: `/app/outputs/diffusion_barrier.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Energy barrier for H detrapping from the vacancy, computed via CI-NEB.
- schema:
  - `type`: number
  - `units`: eV
  - `description`: The diffusion barrier for H migration from the trapped state in the Si vacancy to the I-SiC interstitial site.

Notes: T0 scoring: the checker compares agent-reported trapping energies (n=1..5) and diffusion barrier to paper-reported values with tolerances; for n=6 the trapping energy must be positive. No raw total energy recompute is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trapping_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "n",
            "trapping_energy",
            "zpe_correction",
            "E_total"
          ],
          "properties": {
            "n": {
              "type": "integer"
            },
            "trapping_energy": {
              "type": "number",
              "units": "eV"
            },
            "zpe_correction": {
              "type": "number",
              "units": "eV"
            },
            "E_total": {
              "type": "number",
              "units": "eV"
            }
          }
        }
      },
      "description": "Computed ZPE-corrected trapping energies for n=1..6 H atoms in a Si vacancy, along with the ZPE correction and total energy of each configuration."
    },
    {
      "file": "diffusion_barrier.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "number",
        "units": "eV",
        "description": "The diffusion barrier for H migration from the trapped state in the Si vacancy to the I-SiC interstitial site."
      },
      "description": "Energy barrier for H detrapping from the vacancy, computed via CI-NEB."
    }
  ],
  "notes": "T0 scoring: the checker compares agent-reported trapping energies (n=1..5) and diffusion barrier to paper-reported values with tolerances; for n=6 the trapping energy must be positive. No raw total energy recompute is required."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted artifacts. For the trapping energies, each value is compared to reference data within tolerances that account for the typical spread of DFT results obtained with different codes and pseudopotentials. The diffusion barrier is compared to a reference value with an appropriate margin. The total reward is a weighted sum of the scores for each artifact. Simply reporting literature numbers without executing the full DFT workflow will result in a low score because the verifier checks internal consistency and expects physically meaningful values generated by your calculations. The exact tolerances and reference values are kept hidden.
