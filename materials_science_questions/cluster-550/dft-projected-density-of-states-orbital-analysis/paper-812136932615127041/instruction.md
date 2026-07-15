# DFT-based LDOS analysis of Si-doped carbon nanotube caps

## Problem background
Carbon nanotubes (CNTs) exhibit excellent field emission properties, which are sensitive to the electronic structure at their caps. The local density of states (LDOS) near the Fermi level and the effective work function are key quantities that govern emission performance. Introducing heteroatoms such as silicon into the CNT cap is predicted to modify the electronic structure, potentially altering the LDOS and the effective work function. This task investigates how substituting a single carbon atom with a silicon atom at the cap of a (5,5) CNT influences the electronic properties by directly computing them from first‑principles DFT.

## Approach
Use density functional theory (DFT) with a generalized gradient approximation (GGA; e.g., PBE) as implemented in an open‑source code such as Quantum ESPRESSO. Construct atomic models of a pristine (5,5) capped CNT (the bottom atoms are fixed with hydrogen termination) and a doped model in which one carbon atom at the topmost pentagon is replaced by silicon. Relax both geometries, then perform a single‑point SCF calculation to obtain total energies, Kohn‑Sham eigenvalues (HOMO and LUMO, setting the Fermi level to zero), and the total density of states (DOS). Compute the formation energy of the doped system using the relaxed total energies together with the per‑atom total energy of bulk Si (calculated with the same functional) and the per‑atom total energy of the pure CNT. From the SCF results determine the effective work function as the magnitude of the LUMO energy. Extract the total DOS arrays (energy grid and DOS values) for both systems; from these locate the highest anti‑bonding peak in the region above the Fermi level and compute the LDOS at the Fermi level. Package all results in a single JSON file as described in the workflow steps.

## Reproduction target
For the (5,5) CNT cap in both its pristine form and with a single Si substitution at the topmost pentagon, compute the following quantities from the DFT workflow and write them to a file `results.json`:
- formation energy (eV)
- HOMO and LUMO energies (eV)
- effective work function (eV)
- total DOS arrays (energy in eV and total DOS in states/eV) for each system
- energy location of the highest anti‑bonding peak above the Fermi level (eV above E_F) for each system
- LDOS at the Fermi level
Produce these results by executing the steps described under Workflow steps; the output format must match the contract defined in Output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Build CNT cap models
- Role: process
- Action: Construct atomic coordinates for a pure (5,5) capped carbon nanotube (bottom fixed via hydrogen termination) and a Si-doped model with a single substitution at the topmost pentagon, using ASE or a similar builder. Produce initial structure files readable by Quantum ESPRESSO.
- Evidence: `/app/outputs/model_construction_log.txt`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform full geometry relaxation for both undoped and Si-doped models using Quantum ESPRESSO (pw.x) with a GGA-PBE functional and a suitable k-point mesh. Fix the bottom carbon atoms. Converge total energy to < 1e-5 Ry and forces to < 1e-3 Ry/Bohr. Obtain optimized coordinates and total energies.
- Evidence: `/app/outputs/optimization_log.txt`

### Step 3: Electronic structure and property extraction
- Role: scored (load-bearing)
- Action: Run a final SCF calculation on the relaxed structures with Quantum ESPRESSO (pw.x). Compute the density of states (DOS) using dos.x. From the SCF output determine HOMO and LUMO energies (Fermi level set to zero) and compute the effective work functions. From the total energies of the pure and doped systems, along with the per‑atom total energy of bulk Si (computed with the same functional) and the per‑atom total energy of the undoped CNT, calculate the formation energy: (E_doped - E_undoped) - (mu_Si - mu_C). Extract the total DOS arrays (energy grid and DOS values) for both systems, locate the highest anti‑bonding peak in the [0, 1.5] eV range above the Fermi level for each, and compute the LDOS at the Fermi level. Package all results into results.json as described in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: formation_energy (float, eV), HOMO_undoped (float, eV), HOMO_doped (float, eV), LUMO_undoped (float, eV), LUMO_doped (float, eV), effective_work_function_undoped (float, eV), effective_work_function_doped (float, eV), ldos_undoped (object with 'energy' array-of-floats and 'total_dos' array-of-floats), ldos_doped (same structure), anti_bonding_peak_undoped (float, eV above EF), anti_bonding_peak_doped (float, eV above EF).
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
- target_policy: metric_recompute
- description: Full reproduction output for the (5,5) Si-doped CNT: formation energy, electronic eigenvalues, effective work functions, and energy-resolved LDOS arrays enabling recomputation of the anti-bonding peak location and LDOS at the Fermi level.
- schema:
  - `type`: object
  - `required`: `formation_energy`, `HOMO_undoped`, `HOMO_doped`, `LUMO_undoped`, `LUMO_doped`, `effective_work_function_undoped`, `effective_work_function_doped`, `ldos_undoped`, `ldos_doped`, `anti_bonding_peak_undoped`, `anti_bonding_peak_doped`
  - `properties`:
    - `formation_energy`:
      - `type`: number
      - `unit`: eV
    - `HOMO_undoped`:
      - `type`: number
      - `unit`: eV
    - `HOMO_doped`:
      - `type`: number
      - `unit`: eV
    - `LUMO_undoped`:
      - `type`: number
      - `unit`: eV
    - `LUMO_doped`:
      - `type`: number
      - `unit`: eV
    - `effective_work_function_undoped`:
      - `type`: number
      - `unit`: eV
    - `effective_work_function_doped`:
      - `type`: number
      - `unit`: eV
    - `ldos_undoped`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: array
          - `items`: number
          - `unit`: eV
        - `total_dos`:
          - `type`: array
          - `items`: number
          - `unit`: states/eV
    - `ldos_doped`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: array
          - `items`: number
          - `unit`: eV
        - `total_dos`:
          - `type`: array
          - `items`: number
          - `unit`: states/eV
    - `anti_bonding_peak_undoped`:
      - `type`: number
      - `unit`: eV above EF
    - `anti_bonding_peak_doped`:
      - `type`: number
      - `unit`: eV above EF

Notes: Only the (5,5) single Si doping case is required. The agent must compute bulk Si reference energy for the formation energy. Field names and units are enforced by the checker.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "formation_energy",
          "HOMO_undoped",
          "HOMO_doped",
          "LUMO_undoped",
          "LUMO_doped",
          "effective_work_function_undoped",
          "effective_work_function_doped",
          "ldos_undoped",
          "ldos_doped",
          "anti_bonding_peak_undoped",
          "anti_bonding_peak_doped"
        ],
        "properties": {
          "formation_energy": {
            "type": "number",
            "unit": "eV"
          },
          "HOMO_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "HOMO_doped": {
            "type": "number",
            "unit": "eV"
          },
          "LUMO_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "LUMO_doped": {
            "type": "number",
            "unit": "eV"
          },
          "effective_work_function_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "effective_work_function_doped": {
            "type": "number",
            "unit": "eV"
          },
          "ldos_undoped": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "array",
                "items": "number",
                "unit": "eV"
              },
              "total_dos": {
                "type": "array",
                "items": "number",
                "unit": "states/eV"
              }
            }
          },
          "ldos_doped": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "array",
                "items": "number",
                "unit": "eV"
              },
              "total_dos": {
                "type": "array",
                "items": "number",
                "unit": "states/eV"
              }
            }
          },
          "anti_bonding_peak_undoped": {
            "type": "number",
            "unit": "eV above EF"
          },
          "anti_bonding_peak_doped": {
            "type": "number",
            "unit": "eV above EF"
          }
        }
      },
      "description": "Full reproduction output for the (5,5) Si-doped CNT: formation energy, electronic eigenvalues, effective work functions, and energy-resolved LDOS arrays enabling recomputation of the anti-bonding peak location and LDOS at the Fermi level."
    }
  ],
  "notes": "Only the (5,5) single Si doping case is required. The agent must compute bulk Si reference energy for the formation energy. Field names and units are enforced by the checker."
}
```

## How you are scored
A hidden verifier will inspect the `results.json` file you produce. It will check that the reported quantities are physically plausible and internally consistent with the protocol. For key quantities (e.g., the anti‑bonding peak location, the LDOS at E_F, the formation energy, and the effective work function) the verifier may recompute from the raw DOS arrays or compare to a reference derived from the standard DFT procedure. Simply quoting a value without performing the genuine computation will not yield a high score. The final reward (a float between 0 and 1) reflects the agreement between your computed artifact and the expected reproduction result.
