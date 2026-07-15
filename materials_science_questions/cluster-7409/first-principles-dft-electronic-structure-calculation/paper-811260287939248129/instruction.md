# DFT calculation of cubic CaHfO₃ (001) surface properties

## Problem background
Cubic CaHfO₃ is a perovskite oxide that can serve as a buffer layer or gate dielectric in electronic devices. Its (001) surface can exhibit either CaO or HfO₂ termination, leading to different structural and electronic properties. Understanding the surface rumpling, bandgaps, and relative stability of these two terminations is important for assessing the material's suitability in applications. This task requires you to compute these properties from first‑principles density functional theory (DFT).

## Approach
Use a plane‑wave pseudopotential DFT code (e.g., Quantum ESPRESSO) with PAW pseudopotentials (GGA‑PBE for Ca, Hf, O). The reproduction protocol proceeds in this order:

1. Optimize the lattice constant of cubic bulk CaHfO₃.
2. Compute the bulk band structure along the high‑symmetry path Γ‑X‑M‑Γ‑R‑X and extract the indirect bandgap.
3. Construct 11‑layer slab models for the CaO‑terminated and HfO₂‑terminated (001) surfaces, each with a 12 Å vacuum gap.
4. Relax the atomic positions (in‑plane fixed, out‑of‑plane free) for both slabs.
5. Compute the band structures of the relaxed surfaces along the same high‑symmetry path and extract the indirect bandgaps. Also calculate the surface rumpling parameter (outward displacement of surface O relative to the surface metal, expressed as a percentage of the lattice constant) from the relaxed coordinates.
6. Calculate the surface energies for both terminations using the standard cleavage‑plus‑relaxation formula, which combines unrelaxed and relaxed slab energies with the bulk unit‑cell energy.
7. Assemble all results into a single JSON file.

## Reproduction target
Produce a JSON file named `results.json` containing the following seven computed quantities, all obtained from your DFT workflow:

- `bulk_bandgap` (eV): indirect bandgap of bulk cubic CaHfO₃.
- `cao_bandgap` (eV): indirect bandgap of the CaO‑terminated surface.
- `hfo2_bandgap` (eV): indirect bandgap of the HfO₂‑terminated surface.
- `cao_surface_energy` (J/m²): surface energy of the CaO‑terminated surface.
- `hfo2_surface_energy` (J/m²): surface energy of the HfO₂‑terminated surface.
- `cao_rumpling` (% of lattice constant): surface rumpling parameter for the CaO‑terminated surface.
- `hfo2_rumpling` (% of lattice constant): surface rumpling parameter for the HfO₂‑terminated surface.

All quantities must be derived from the same consistent DFT setup. The file format is strict JSON; numeric values should be plain numbers (not strings).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PAW pseudopotentials for Ca, Hf, O (GGA‑PBE): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Bulk lattice constant optimization
- Role: process
- Action: Optimize the cubic lattice parameter of CaHfO₃ using DFT relaxation with a 12×12×12 k‑point mesh and a plane‑wave cutoff of 500 eV. Record the relaxed lattice constant and total energy.
- Evidence: none

### Step 2: Bulk electronic structure calculation
- Role: process
- Action: Compute the band structure of the optimized bulk CaHfO₃ along the high‑symmetry path Γ‑X‑M‑Γ‑R‑X. Extract the indirect bandgap (VBM at R, CBM at Γ) and keep the total energy.
- Evidence: none

### Step 3: Surface slab relaxations
- Role: process
- Action: Build 11‑layer CaO‑ and HfO₂‑terminated slab models with 12 Å vacuum, using the optimized lattice constant. Relax atomic positions (in‑plane fixed, out‑of‑plane free) with a 12×12×1 k‑point grid. Record the unrelaxed and relaxed total energies and the relaxed atomic coordinates.
- Evidence: none

### Step 4: Surface band structures and rumpling
- Role: process
- Action: Compute band structures for the relaxed CaO‑ and HfO₂‑terminated surfaces along the same symmetry path as for the bulk. Identify the VBM/CBM k‑points and extract the indirect bandgaps. From the relaxed coordinates calculate the surface rumpling parameter s (outward displacement of O relative to the surface metal) for each termination.
- Evidence: none

### Step 5: Surface energy calculation
- Role: process
- Action: Compute surface energies for CaO and HfO₂ terminations using the standard cleavage‑plus‑relaxation formula: E_surf = E_cle + E_rel(X). Combine unrelaxed/relaxed slab energies and the bulk unit‑cell energy.
- Evidence: none

### Step 6: Assemble and write final results
- Role: scored (load-bearing)
- Action: Collect all computed quantities into a JSON file named results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type":"object","required":["bulk_bandgap","cao_bandgap","hfo2_bandgap","cao_surface_energy","hfo2_surface_energy","cao_rumpling","hfo2_rumpling"],"properties":{"bulk_bandgap":{"type":"number","unit":"eV"},"cao_bandgap":{"type":"number","unit":"eV"},"hfo2_bandgap":{"type":"number","unit":"eV"},"cao_surface_energy":{"type":"number","unit":"J/m^2"},"hfo2_surface_energy":{"type":"number","unit":"J/m^2"},"cao_rumpling":{"type":"number","unit":"% of lattice constant"},"hfo2_rumpling":{"type":"number","unit":"% of lattice constant"}}}
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
- target_policy: exact_match
- description: Aggregated file containing the seven computed DFT quantities. The hidden checker reads this file and compares each numeric field to the paper‑reported gold using absolute tolerances.
- schema:
  - `type`: object
  - `required`: `bulk_bandgap`, `cao_bandgap`, `hfo2_bandgap`, `cao_surface_energy`, `hfo2_surface_energy`, `cao_rumpling`, `hfo2_rumpling`
  - `properties`:
    - `bulk_bandgap`:
      - `type`: number
      - `unit`: eV
    - `cao_bandgap`:
      - `type`: number
      - `unit`: eV
    - `hfo2_bandgap`:
      - `type`: number
      - `unit`: eV
    - `cao_surface_energy`:
      - `type`: number
      - `unit`: J/m^2
    - `hfo2_surface_energy`:
      - `type`: number
      - `unit`: J/m^2
    - `cao_rumpling`:
      - `type`: number
      - `unit`: % of lattice constant
    - `hfo2_rumpling`:
      - `type`: number
      - `unit`: % of lattice constant

Notes: The task uses Quantum ESPRESSO, an open‑source DFT code. The solver must choose appropriate PAW pseudopotentials for Ca, Hf, O (GGA‑PBE). All intermediate DFT artefacts (optimised bulk geometry, slab coordinates, band‑structure data, total energies) are needed by the process steps and must be produced by the agent; they are not provided as pre‑computed resources.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "bulk_bandgap",
          "cao_bandgap",
          "hfo2_bandgap",
          "cao_surface_energy",
          "hfo2_surface_energy",
          "cao_rumpling",
          "hfo2_rumpling"
        ],
        "properties": {
          "bulk_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "cao_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "hfo2_bandgap": {
            "type": "number",
            "unit": "eV"
          },
          "cao_surface_energy": {
            "type": "number",
            "unit": "J/m^2"
          },
          "hfo2_surface_energy": {
            "type": "number",
            "unit": "J/m^2"
          },
          "cao_rumpling": {
            "type": "number",
            "unit": "% of lattice constant"
          },
          "hfo2_rumpling": {
            "type": "number",
            "unit": "% of lattice constant"
          }
        }
      },
      "description": "Aggregated file containing the seven computed DFT quantities. The hidden checker reads this file and compares each numeric field to the paper‑reported gold using absolute tolerances."
    }
  ],
  "notes": "The task uses Quantum ESPRESSO, an open‑source DFT code. The solver must choose appropriate PAW pseudopotentials for Ca, Hf, O (GGA‑PBE). All intermediate DFT artefacts (optimised bulk geometry, slab coordinates, band‑structure data, total energies) are needed by the process steps and must be produced by the agent; they are not provided as pre‑computed resources."
}
```

## How you are scored
A hidden verifier reads `results.json` and compares every numeric field against the correct reference values (obtained independently from the original study). The reward is 1.0 (full credit) if all seven quantities are within the required agreement; otherwise the reward is 0.0. The verification is fully automatic; you do not need to provide intermediate checks or interpret the appearance of the file. There is no partial credit.
