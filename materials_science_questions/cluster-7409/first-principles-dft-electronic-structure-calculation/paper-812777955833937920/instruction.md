# First-principles DFT calculation of magnetic properties of Ni-doped SnO₂ (110) surface

## Problem background
Dilute magnetic semiconductors (DMS) based on oxide hosts such as SnO₂ are promising for spintronic applications. Ni-doped SnO₂ has been reported to exhibit room-temperature ferromagnetism, but the origin of this magnetism and the role of intrinsic point defects—particularly oxygen vacancies (V_O)—remain debated. First-principles density functional theory (DFT) calculations can probe the local magnetic moment induced by Ni substitution on the SnO₂ (110) surface, the magnetic coupling between Ni atoms, and how the introduction of oxygen vacancies influences that coupling.

## Approach
Use hybrid DFT (HSE) with a plane-wave basis and projector augmented wave (PAW) pseudopotentials to model the rutile SnO₂ (110) surface. Build a supercell slab with vacuum, and substitute one or two Sn atoms with Ni. Investigate the magnetic moment of a single isolated Ni dopant, and compute the energy difference between ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments for several distinct configurations of two Ni atoms on the surface. Then introduce a nearest-neighbor oxygen vacancy adjacent to each Ni and repeat the two‑Ni calculations for the same set of configurations. By comparing the FM–AFM energy differences and magnetic moments with and without vacancies, you can assess the effect of oxygen vacancies on the magnetic interaction.

## Reproduction target
Produce `/app/outputs/results.json` containing:

1. The local magnetic moment (in μ_B) of a single substitutional Ni atom on the SnO₂ (110) surface.
2. A table (table1) with six entries for two‑Ni configurations **without** oxygen vacancies, each giving: the relaxed Ni–Ni distance (Å), ΔE = E_AFM − E_FM (meV), the total magnetic moment in the FM state (μ_B), and the magnetic coupling type ("FM" if ΔE > 0, "AFM" otherwise).
3. A second table (table2) with six entries for the corresponding configurations **with** nearest-neighbor oxygen vacancies, containing the same quantities.

From the computed data, determine whether the introduction of oxygen vacancies strengthens or weakens the ferromagnetic coupling.

## Assets

- Plane-wave DFT code supporting HSE hybrid functionals (e.g., Quantum ESPRESSO, VASP): https://www.quantum-espresso.org
- PAW pseudopotentials for Sn, Ni, O: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build structural models
- Role: process
- Action: Construct supercell models of the rutile SnO₂ (110) surface using lattice parameters a=4.714 Å, c=3.192 Å. Build a 2×2×2 supercell with 10 Å vacuum. Create models for: perfect surface, single Ni substitution at Sn₅c and Sn₆c, the six two-Ni configurations without oxygen vacancies, and the corresponding six configurations with nearest-neighbor oxygen vacancies.
- Evidence: `/app/outputs/models_summary.json`

### Step 2: Reference DFT on perfect surface
- Role: process
- Action: Perform a DFT calculation on the perfect SnO₂ (110) surface using the HSE hybrid functional, PAW pseudopotentials, appropriate energy cutoff and k-point sampling. Verify that the computed band gap (~3.59 eV) and non‑magnetic DOS match expectations, confirming the computational setup is correct.
- Evidence: `/app/outputs/perfect_dos.json`

### Step 3: Compute magnetic properties and generate results
- Role: scored (load-bearing)
- Action: Using the validated DFT protocol, perform structure relaxations and total-energy calculations for: (a) a single Ni substitution at the more stable site, (b) all six two‑Ni configurations without oxygen vacancies, and (c) all six two‑Ni configurations with nearest‑neighbor oxygen vacancies. For each system compute FM and AFM spin states. Record Ni–Ni distance after relaxation, ΔE = E_AFM − E_FM (meV), total magnetic moment in the FM state (μB), and magnetic coupling (FM if ΔE>0, AFM if ΔE<0). Write the results into /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"single_ni_magnetic_moment": float (μB), "table1": [{"config": string, "ni_ni_distance": float (Å), "delta_E": float (meV), "m_tot": float (μB), "coupling": string}], "table2": [{"case": string, "ni_ni_distance": float (Å), "delta_E": float (meV), "m_tot": float (μB), "coupling": string}]}
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
- target_policy: reference_match
- description: DFT-computed magnetic moment and coupling data for Ni-doped SnO₂ (110) surface; the checked values are the single-Ni magnetic moment and the ΔE, magnetic moments, and coupling types for the two-Ni configurations without and with oxygen vacancies.
- schema:
  - `type`: object
  - `required`: `single_ni_magnetic_moment`, `table1`, `table2`
  - `properties`:
    - `single_ni_magnetic_moment`:
      - `type`: number
      - `description`: Local magnetic moment of a single Ni dopant in μB
    - `table1`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `config`, `ni_ni_distance`, `delta_E`, `m_tot`, `coupling`
        - `properties`:
          - `config`:
            - `type`: string
          - `ni_ni_distance`:
            - `type`: number
            - `description`: Ni-Ni distance after relaxation in Å
          - `delta_E`:
            - `type`: number
            - `description`: E_AFM - E_FM in meV
          - `m_tot`:
            - `type`: number
            - `description`: total magnetic moment in μB
          - `coupling`:
            - `type`: string
            - `enum`: `FM`, `AFM`
    - `table2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `case`, `ni_ni_distance`, `delta_E`, `m_tot`, `coupling`
        - `properties`:
          - `case`:
            - `type`: string
          - `ni_ni_distance`:
            - `type`: number
            - `description`: Ni-Ni distance after relaxation in Å
          - `delta_E`:
            - `type`: number
            - `description`: E_AFM - E_FM in meV
          - `m_tot`:
            - `type`: number
            - `description`: total magnetic moment in μB
          - `coupling`:
            - `type`: string
            - `enum`: `FM`, `AFM`

Notes: The hidden gold consists of the paper-reported magnetic moment and coupling energies, compared with tolerances. The checker also evaluates the trend that oxygen vacancies weaken ferromagnetism by comparing the two tables.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "single_ni_magnetic_moment",
          "table1",
          "table2"
        ],
        "properties": {
          "single_ni_magnetic_moment": {
            "type": "number",
            "description": "Local magnetic moment of a single Ni dopant in μB"
          },
          "table1": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "config",
                "ni_ni_distance",
                "delta_E",
                "m_tot",
                "coupling"
              ],
              "properties": {
                "config": {
                  "type": "string"
                },
                "ni_ni_distance": {
                  "type": "number",
                  "description": "Ni-Ni distance after relaxation in Å"
                },
                "delta_E": {
                  "type": "number",
                  "description": "E_AFM - E_FM in meV"
                },
                "m_tot": {
                  "type": "number",
                  "description": "total magnetic moment in μB"
                },
                "coupling": {
                  "type": "string",
                  "enum": [
                    "FM",
                    "AFM"
                  ]
                }
              }
            }
          },
          "table2": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "case",
                "ni_ni_distance",
                "delta_E",
                "m_tot",
                "coupling"
              ],
              "properties": {
                "case": {
                  "type": "string"
                },
                "ni_ni_distance": {
                  "type": "number",
                  "description": "Ni-Ni distance after relaxation in Å"
                },
                "delta_E": {
                  "type": "number",
                  "description": "E_AFM - E_FM in meV"
                },
                "m_tot": {
                  "type": "number",
                  "description": "total magnetic moment in μB"
                },
                "coupling": {
                  "type": "string",
                  "enum": [
                    "FM",
                    "AFM"
                  ]
                }
              }
            }
          }
        }
      },
      "description": "DFT-computed magnetic moment and coupling data for Ni-doped SnO₂ (110) surface; the checked values are the single-Ni magnetic moment and the ΔE, magnetic moments, and coupling types for the two-Ni configurations without and with oxygen vacancies."
    }
  ],
  "notes": "The hidden gold consists of the paper-reported magnetic moment and coupling energies, compared with tolerances. The checker also evaluates the trend that oxygen vacancies weaken ferromagnetism by comparing the two tables."
}
```

## How you are scored
A hidden verifier reads your `results.json`. It compares your computed magnetic moment, the ΔE values, the magnetic moments, and the coupling types for each two‑Ni configuration against a hidden gold set, using appropriate tolerances. It also evaluates whether your results consistently show a particular trend for the effect of oxygen vacancies on the magnetic coupling across the configurations. The verifier combines these checks into a final score between 0 and 1, weighting the tables and the trend. Mere reporting of numbers that point in the right direction is not sufficient; your computed quantities must be accurate against the gold reference.
