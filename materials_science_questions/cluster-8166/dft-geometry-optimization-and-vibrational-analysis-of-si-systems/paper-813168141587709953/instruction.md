# Na insertion and diffusion in layered silicon structures by DFT

## Problem background
Silicon-based anodes offer high capacity for Li-ion batteries, but bulk crystalline Si is unsuitable for Na-ion batteries because of slow Na diffusion and energetically unfavorable Na insertion, largely due to the large ionic radius of Na. Layered Si structures—polysilane (a layered Si₆H₆ material) and single-layer H-passivated silicene—could provide larger interstitial spaces and lower diffusion barriers, potentially enabling Na storage and fast transport. In this task, we investigate whether Na binding and diffusion are improved in these layered systems relative to bulk Si by computing Na binding energies and diffusion barriers from first principles.

## Approach
We use density functional theory (DFT) calculations with the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional and ultrasoft pseudopotentials. For layered polysilane, van der Waals corrections (DFT‑D) are applied to account for interlayer interactions. All electronic-structure and total-energy calculations are performed with Quantum ESPRESSO. Na binding energies are obtained from the total energies of the empty host, the host with one inserted Na atom, and an isolated Na atom. Na diffusion barriers are computed via the climbing-image nudged elastic band (CI‑NEB) method. The three host systems are: a 64‑atom cubic cell of bulk diamond Si, a polysilane supercell (Si₆H₆), and a single‑layer H‑passivated silicene supercell with vacuum. The task compares Na insertion and migration behavior across these three architectures.

## Reproduction target
Produce a single JSON file containing the computed Na binding energies (Eb) in bulk Si, layered polysilane, and H‑passivated silicene, and the Na diffusion barriers in bulk Si and polysilane. All values must be in electronvolts (eV) and obtained from the DFT‑PBE(+vdW) protocol described above. The file must be written to /app/outputs/na_insertion_data.json and must contain exactly the following top‑level keys (each a float):
- bulk_Si_Na_Eb
- polysilane_Na_Eb
- silicene_Na_Eb
- bulk_Si_Na_barrier
- polysilane_Na_barrier

The binding energy is defined as Eb = E(Na–Si) – E(Si) – E(Na), where E(Na–Si) is the total energy of the host with one Na atom at its most favorable insertion site, E(Si) is the total energy of the pristine host, and E(Na) is the energy of an isolated Na atom.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Ultrasoft pseudopotentials for Si, H, Na: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Geometry optimization of host structures
- Role: process
- Action: Perform DFT geometry optimization of pristine bulk Si (diamond, 64-atom supercell), layered polysilane (Si6H6), and single-layer H-passivated silicene, using PBE functional with van der Waals corrections (DFT-D) for polysilane. Output relaxed atomic coordinates and lattice parameters.
- Evidence: `/app/outputs/host_optimizations.log`

### Step 2: Na insertion site optimization and reference energy calculation
- Role: process
- Action: Place one Na atom in each optimized host at the most favorable site: tetrahedral interstitial for bulk Si, hollow site for polysilane and silicene. Perform geometry optimization to obtain total energies E(Na-Si) for each system. Also compute total energy of an isolated Na atom in a large vacuum box as E(Na).
- Evidence: `/app/outputs/insertion_energies.txt`

### Step 3: NEB diffusion barrier calculations
- Role: process
- Action: Using climbing-image nudged elastic band (CI-NEB) method, compute the energy barrier for Na diffusion in bulk Si (Td → Hex → Td path) and in layered polysilane (H → B → H path). Use the optimized insertion geometries as initial and final points. Extract the barrier heights.
- Evidence: `/app/outputs/neb_barriers.txt`

### Step 4: Compute binding energies and assemble results
- Role: scored (load-bearing)
- Action: Calculate Na binding energies using the formula Eb = [E(Na-Si) - E(Si) - E(Na)] for each host, then compile the binding energies and the NEB barriers into a single JSON file: /app/outputs/na_insertion_data.json. The file must contain the fields: bulk_Si_Na_Eb (eV), polysilane_Na_Eb (eV), silicene_Na_Eb (eV), bulk_Si_Na_barrier (eV), polysilane_Na_barrier (eV).
- Output file: `/app/outputs/na_insertion_data.json`
- Format: json
- Contract: object with fields bulk_Si_Na_Eb, polysilane_Na_Eb, silicene_Na_Eb, bulk_Si_Na_barrier, polysilane_Na_barrier (all floats, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/na_insertion_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### na_insertion_data.json
- path: `/app/outputs/na_insertion_data.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Na binding energies (Eb) for Na in bulk Si, layered polysilane, and single-layer H-passivated silicene, and Na diffusion barriers in bulk Si and layered polysilane. All values in eV.
- schema:
  - `type`: object
  - `required`: `bulk_Si_Na_Eb`, `polysilane_Na_Eb`, `silicene_Na_Eb`, `bulk_Si_Na_barrier`, `polysilane_Na_barrier`
  - `properties`:
    - `bulk_Si_Na_Eb`:
      - `type`: number
      - `unit`: eV
    - `polysilane_Na_Eb`:
      - `type`: number
      - `unit`: eV
    - `silicene_Na_Eb`:
      - `type`: number
      - `unit`: eV
    - `bulk_Si_Na_barrier`:
      - `type`: number
      - `unit`: eV
    - `polysilane_Na_barrier`:
      - `type`: number
      - `unit`: eV

Notes: Binding energies are defined per Na atom as Eb = [E(Na-Si) - E(Si) - E(Na)]. Diffusion barriers are obtained via CI-NEB. Scoring is per-field with independent thresholds and tolerances; more negative binding energies and lower barriers earn full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "na_insertion_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "bulk_Si_Na_Eb",
          "polysilane_Na_Eb",
          "silicene_Na_Eb",
          "bulk_Si_Na_barrier",
          "polysilane_Na_barrier"
        ],
        "properties": {
          "bulk_Si_Na_Eb": {
            "type": "number",
            "unit": "eV"
          },
          "polysilane_Na_Eb": {
            "type": "number",
            "unit": "eV"
          },
          "silicene_Na_Eb": {
            "type": "number",
            "unit": "eV"
          },
          "bulk_Si_Na_barrier": {
            "type": "number",
            "unit": "eV"
          },
          "polysilane_Na_barrier": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Na binding energies (Eb) for Na in bulk Si, layered polysilane, and single-layer H-passivated silicene, and Na diffusion barriers in bulk Si and layered polysilane. All values in eV."
    }
  ],
  "notes": "Binding energies are defined per Na atom as Eb = [E(Na-Si) - E(Si) - E(Na)]. Diffusion barriers are obtained via CI-NEB. Scoring is per-field with independent thresholds and tolerances; more negative binding energies and lower barriers earn full credit."
}
```

## How you are scored
Your solution is scored by a hidden verifier that reads /app/outputs/na_insertion_data.json and compares each field to independently held reference values using per‑field thresholds and appropriate directional tolerances. For binding energies, more negative (more favorable) values earn full credit; for diffusion barriers, lower values earn full credit. Each field is scored independently with equal weight, and the final reward is the average of the per‑field scores. The verifier does not inspect intermediate log files, but those files serve as evidence that the required DFT geometry optimizations and NEB calculations were executed.
