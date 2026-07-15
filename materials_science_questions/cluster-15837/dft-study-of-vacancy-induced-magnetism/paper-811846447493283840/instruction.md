# DFT study of vacancy-induced magnetism in GaN surfaces

## Problem background
Room-temperature ferromagnetism has been experimentally observed in undoped GaN nanoparticles, with evidence pointing towards intrinsic point defects confined to the nanoparticle surfaces as a possible origin. However, the specific type of defect and the surface orientation that could induce magnetic order remain open questions. First-principles spin-polarised density functional theory (DFT) can directly probe the electronic and magnetic properties of surface defects. This task investigates whether neutral gallium and nitrogen vacancies at the (100) and (101) surfaces of cubic GaN can produce net magnetic moments and, if so, what type of magnetic coupling—ferromagnetic (FM) or antiferromagnetic (AFM)—emerges among the defect-induced spins.

## Approach
The approach uses spin-polarised DFT with the GGA-PBE exchange-correlation functional and projector augmented-wave (PAW) pseudopotentials, as implemented in the Quantum ESPRESSO package. Three-dimensional periodic slab models are constructed for the Ga-ended (100), N-ended (100), and (101) surfaces of cubic GaN, separated by a ~10 Å vacuum layer. The lattice constant is obtained from a prior bulk cubic GaN relaxation. After fully relaxing each slab, the following six surface configurations are examined: (i) the ideal relaxed Ga-ended (100) surface; (ii) the ideal relaxed (101) surface; (iii) the reconstructed Ga-ended (100) surface that forms when the N-ended (100) slab is relaxed; (iv) the Ga-ended (100) surface with two neutral Ga vacancies (removing the most stable pair of surface Ga atoms); (v) the (101) surface with two neutral N vacancies; and (vi) the (101) surface with two neutral Ga vacancies. For each configuration, after further relaxation (if defects are present), a static spin-polarised calculation is carried out to obtain the total energy and total magnetic moment for the ferromagnetic spin alignment. For configurations (iii), (iv), and (vi), an additional static calculation is performed with an antiferromagnetic alignment of the local moments. The sign of the energy difference ΔE = E_AFM − E_FM (when computed) indicates whether FM or AFM coupling is energetically favoured.

## Reproduction target
For the six surface configurations listed above, run the described DFT calculations after full structural relaxation and report the total energy (in eV) and total magnetic moment (in μB) for the ferromagnetic spin configuration. For configurations (iii), (iv), and (vi), also report the total energy for the antiferromagnetic spin configuration. The results must be written as a JSON array to `/app/outputs/simulation_results.json`, using the schema specified under “Output contract”. The target is to produce a complete and internally consistent set of energies and moments from which the magnetic character (non-magnetic, ferromagnetic, or antiferromagnetic) of each surface can be deduced.

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- SSSP PAW pseudopotentials (efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Bulk cubic GaN relaxation
- Role: process
- Action: Relax a 2×2×2 supercell of cubic GaN (space group F4-3m) using DFT with PAW pseudopotentials to obtain the equilibrium lattice constant.
- Evidence: `/app/outputs/bulk_lattice.json`

### Step 2: Surface slab construction and relaxation
- Role: process
- Action: Using the equilibrium lattice constant, construct slab models for the Ga-ended (100), N-ended (100), and (101) surfaces, each with ~10 Å vacuum and the atom counts described in the paper. Fully relax all three slabs; the unstable N-ended (100) surface will reconstruct into a Ga-ended surface.
- Evidence: none

### Step 3: Spin‑polarised DFT calculations for all six surface configurations
- Role: scored (load-bearing)
- Action: Set up and run spin‑polarised DFT calculations for the six required systems: (1) ideal relaxed Ga‑ended (100); (2) ideal relaxed (101); (3) the reconstructed Ga‑ended (100) surface obtained from the N‑ended (100) relaxation; (4) Ga‑ended (100) with two neutral Ga vacancies (11.11%, removing the energetically favourable pair Ga1+Ga5); (5) (101) surface with two neutral N vacancies (12.5%, removing N1+N2); (6) (101) surface with two neutral Ga vacancies (12.5%, removing the favourable pair Ga1+Ga2). For each system, after full relaxation, compute the total energy and total magnetic moment for the ferromagnetic (FM) spin configuration. For systems (3), (4), and (6), additionally compute the total energy for an antiferromagnetic (AFM) alignment. Report all values in simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: array of objects with keys: system (string), vacancies (string), total_energy_FM (number, eV), total_energy_AFM (number|null, eV), total_magnetic_moment_FM (number, mu_B)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: The agent's computed total energies (FM and, where applicable, AFM) and total magnetic moment (FM) for each of the six surface configurations. The verifier checks qualitative trends: ideal surfaces must be nonmagnetic (|moment| < 0.01 μB); reconstructed (100) and Ga-vacancy (100) must have a positive moment and FM lower energy than AFM; N-vacancy (101) must be nonmagnetic; Ga-vacancy (101) must have AFM lower energy than FM (moment is not checked).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `vacancies`, `total_energy_FM`, `total_magnetic_moment_FM`
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `ideal_100_Ga-ended`, `ideal_101`, `reconstructed_100`, `Ga_vacancy_100`, `N_vacancy_101`, `Ga_vacancy_101`
        - `description`: Must be one of the six predefined system identifiers.
      - `vacancies`:
        - `type`: string
      - `total_energy_FM`:
        - `type`: number
        - `units`: eV
      - `total_energy_AFM`:
        - `type`: `number`, `null`
        - `units`: eV
      - `total_magnetic_moment_FM`:
        - `type`: number
        - `units`: mu_B

Notes: Only qualitative trends are scored; exact reproduction of the paper's reported magnetic moments (e.g., 2.77 μB) and energy differences (e.g., 5.4 eV) is not required, as absolute values depend on the chosen code and pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "vacancies",
            "total_energy_FM",
            "total_magnetic_moment_FM"
          ],
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "ideal_100_Ga-ended",
                "ideal_101",
                "reconstructed_100",
                "Ga_vacancy_100",
                "N_vacancy_101",
                "Ga_vacancy_101"
              ],
              "description": "Must be one of the six predefined system identifiers."
            },
            "vacancies": {
              "type": "string"
            },
            "total_energy_FM": {
              "type": "number",
              "units": "eV"
            },
            "total_energy_AFM": {
              "type": [
                "number",
                "null"
              ],
              "units": "eV"
            },
            "total_magnetic_moment_FM": {
              "type": "number",
              "units": "mu_B"
            }
          }
        }
      },
      "description": "The agent's computed total energies (FM and, where applicable, AFM) and total magnetic moment (FM) for each of the six surface configurations. The verifier checks qualitative trends: ideal surfaces must be nonmagnetic (|moment| < 0.01 μB); reconstructed (100) and Ga-vacancy (100) must have a positive moment and FM lower energy than AFM; N-vacancy (101) must be nonmagnetic; Ga-vacancy (101) must have AFM lower energy than FM (moment is not checked)."
    }
  ],
  "notes": "Only qualitative trends are scored; exact reproduction of the paper's reported magnetic moments (e.g., 2.77 μB) and energy differences (e.g., 5.4 eV) is not required, as absolute values depend on the chosen code and pseudopotentials."
}
```

## How you are scored
A hidden verifier will independently inspect the contents of `simulation_results.json`. For each surface configuration it checks whether the reported total magnetic moment and, where applicable, the sign of the energy difference (E_AFM − E_FM) are consistent with the expected qualitative magnetic behaviour. The expected behaviour is: a vanishingly small magnetic moment for a non‑magnetic surface; a non‑zero moment with FM more stable than AFM for a ferromagnetic system; and an AFM‑favoured energy difference (E_AFM < E_FM) for an antiferromagnetic system, possibly accompanied by a near‑zero total moment. Scoring is based on how many of these qualitative trend checks pass; exact numerical agreement with any reference values is not required, because absolute moments and energy differences can shift depending on the computational setup (code, pseudopotential, convergence parameters). The final reward is the fraction of checks that are satisfied. No single check dominates; the task rewards a self-consistent set of calculations that captures the correct physical trend for each surface.
