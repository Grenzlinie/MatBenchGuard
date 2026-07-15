# Oxygen Vacancy Formation and Diffusion in SrTiO3/Ruddlesden-Popper Oxides

## Problem background
Oxygen vacancies in SrTiO3 (STO) act as n‑type dopants and can create high‑mobility electron layers when confined near an interface. Controlling the creation, preservation, and removal of these vacancies is essential for rewritable electronic devices. A promising strategy is to cap the STO with a Ruddlesden‑Popper (RP) layered perovskite of the same elemental family (Sr<sub>n+1</sub>Ti<sub>n</sub>O<sub>3n+1</sub>), which is expected to exhibit different oxygen‑vacancy energetics due to its built‑in rock‑salt SrO–SrO layers. To understand whether such a capping layer can act as an effective oxygen‑vacancy valve, one needs to quantify the formation energy of an oxygen vacancy and the energy barrier for its migration along the crystal c‑axis in both STO and RP phases. This task requires you to compute those quantities from first‑principles density functional theory (DFT) for the n=2 RP phase Sr<sub>3</sub>Ti<sub>2</sub>O<sub>7</sub> and cubic STO, with optional calculations for n=1 (Sr<sub>2</sub>TiO<sub>4</sub>) and n=3 (Sr<sub>4</sub>Ti<sub>3</sub>O<sub>10</sub>).

## Approach
The approach uses plane‑wave DFT with the PBE exchange‑correlation functional, as implemented in the open‑source Quantum ESPRESSO suite, employing accurate pseudopotentials from the SSSP efficiency library. For each material you will build supercells containing a single oxygen vacancy, compute total energies of the perfect and defective cells, and obtain the formation energy from the energy balance involving an isolated O<sub>2</sub> molecule. The diffusion barrier along the c‑axis is then determined by climbing‑image nudged elastic band (CI‑NEB) calculations, which require a set of intermediate images connecting the initial and final vacancy positions. The workflow therefore comprises four stages: (1) constructing the atomic structures, (2) running total‑energy self‑consistent field (SCF) calculations for perfect and defective supercells as well as for O<sub>2</sub>, (3) evaluating the formation energies, and (4) performing CI‑NEB barrier calculations. No external dataset is needed; the crystal structures of STO (cubic, a≈3.905 Å) and the RP phases (tetragonal, with in‑plane a fixed to 3.905 Å) are defined by well‑known space‑group symmetries, and all required computational tools are publicly available.

## Reproduction target
Compute, for cubic SrTiO<sub>3</sub> and for the n=2 Ruddlesden‑Popper phase Sr<sub>3</sub>Ti<sub>2</sub>O<sub>7</sub>, the oxygen‑vacancy formation energy (ΔH in eV) and the CI‑NEB diffusion barrier (in eV) for vacancy migration along the c‑axis. Optionally, extend the calculations to n=1 (Sr<sub>2</sub>TiO<sub>4</sub>) and n=3 (Sr<sub>4</sub>Ti<sub>3</sub>O<sub>10</sub>) to provide a more complete picture. Report the formation energies in a JSON file `/app/outputs/step_01_formation_energies.json` and the barriers in `/app/outputs/step_02_diffusion_barriers.json`. The required fields and their format are described in the output contract section below. The verifier will extract these values and assess them against hidden criteria that reflect the physical plausibility and relative ordering expected from the structural differences among the phases.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build supercell models
- Role: process
- Action: Construct 3x3x3 supercells of cubic SrTiO3 (a=3.905 Å, space group Pm-3m) and 3x3x1 supercells of tetragonal Sr3Ti2O7 (I4/mmm, in-plane a=3.905 Å) from publicly available crystal structures. Optionally build supercells for Sr2TiO4 (n=1) and Sr4Ti3O10 (n=3). Generate Quantum ESPRESSO input files with the structures.
- Evidence: none

### Step 2: Compute total energies of perfect and defective supercells and O2 molecule
- Role: process
- Action: Using Quantum ESPRESSO with PBE functional and SSSP pseudopotentials, compute total energies of: (a) perfect supercells of SrTiO3 and each RP phase, (b) isolated O2 molecule, (c) defective supercells with one oxygen vacancy removed and atomic positions relaxed. Use a plane-wave cutoff of ~520 eV and appropriate k-point sampling. Record the total energy values in a JSON file for traceability.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Calculate formation energies
- Role: scored
- Action: From the total energies computed in step_02, calculate the formation energy ΔH = E_def - E_perf + 0.5*E_O2 for each system (STO, Sr3Ti2O7; optionally Sr2TiO4, Sr4Ti3O10). Output the results in a JSON file with keys for each material.
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: Object: keys STO, Sr3Ti2O7 required (float, eV); Sr2TiO4, Sr4Ti3O10 optional (float, eV).
- Scoring: scored by hidden verifier

### Step 4: CI-NEB diffusion barrier calculations
- Role: scored
- Action: For each system where a formation energy was computed, determine the oxygen vacancy migration barrier along the c-axis using climbing-image nudged elastic band (CI-NEB) with Quantum ESPRESSO. Identify the energy barrier E_b as the difference between the highest image and the initial state. Output the barriers as a JSON file.
- Output file: `/app/outputs/step_02_diffusion_barriers.json`
- Format: json
- Contract: Object: keys STO, Sr3Ti2O7 required (float, eV); Sr2TiO4, Sr4Ti3O10 optional (float, eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.json`
- `/app/outputs/step_02_diffusion_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Oxygen vacancy formation energies (ΔH) in eV for SrTiO3 and Sr3Ti2O7 (required), and optionally for Sr2TiO4 and Sr4Ti3O10. The checker verifies structural plausibility and required relative ordering among the materials.
- schema:
  - `type`: object
  - `required`:
    - `STO`: float, eV
    - `Sr3Ti2O7`: float, eV
  - `optional`:
    - `Sr2TiO4`: float, eV
    - `Sr4Ti3O10`: float, eV

### step_02_diffusion_barriers.json
- path: `/app/outputs/step_02_diffusion_barriers.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Oxygen vacancy diffusion barriers (eV) for migration along the c-axis in SrTiO3 and Sr3Ti2O7 (required), and optionally for Sr2TiO4 and Sr4Ti3O10. The checker verifies structural plausibility and required trends among the materials, including monotonicity across the n-series if provided.
- schema:
  - `type`: object
  - `required`:
    - `STO`: float, eV
    - `Sr3Ti2O7`: float, eV
  - `optional`:
    - `Sr2TiO4`: float, eV
    - `Sr4Ti3O10`: float, eV

Notes: The formation energies and diffusion barriers should be computed using DFT with PBE functional and open-source Quantum ESPRESSO. The checker will verify structural ordering and magnitude thresholds; no specific direction is disclosed. Absolute values may differ slightly due to different DFT implementations; scoring focuses on relative trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "STO": "float, eV",
          "Sr3Ti2O7": "float, eV"
        },
        "optional": {
          "Sr2TiO4": "float, eV",
          "Sr4Ti3O10": "float, eV"
        }
      },
      "description": "Oxygen vacancy formation energies (ΔH) in eV for SrTiO3 and Sr3Ti2O7 (required), and optionally for Sr2TiO4 and Sr4Ti3O10. The checker verifies structural plausibility and required relative ordering among the materials."
    },
    {
      "file": "step_02_diffusion_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "STO": "float, eV",
          "Sr3Ti2O7": "float, eV"
        },
        "optional": {
          "Sr2TiO4": "float, eV",
          "Sr4Ti3O10": "float, eV"
        }
      },
      "description": "Oxygen vacancy diffusion barriers (eV) for migration along the c-axis in SrTiO3 and Sr3Ti2O7 (required), and optionally for Sr2TiO4 and Sr4Ti3O10. The checker verifies structural plausibility and required trends among the materials, including monotonicity across the n-series if provided."
    }
  ],
  "notes": "The formation energies and diffusion barriers should be computed using DFT with PBE functional and open-source Quantum ESPRESSO. The checker will verify structural ordering and magnitude thresholds; no specific direction is disclosed. Absolute values may differ slightly due to different DFT implementations; scoring focuses on relative trends."
}
```

## How you are scored
A hidden checker will read your two output JSON files and compute a score. The checker evaluates whether the reported formation energies and diffusion barriers satisfy quantitative and relational criteria that are derived from the underlying physics (e.g., positivity, internal consistency, and relative magnitudes between the different materials). Each scored artifact contributes a weight to the final reward, and the total reward lies between 0 and 1. Because the checker already possesses the reference information it needs, no network fetch is required during grading. The evaluation is structural and quantitative; it does not simply check that a file is present or has the expected shape, but instead verifies that the numerical content is physically meaningful and meets the required objectives.
