# DFT verification of Bi-Li ionic pair formation in doped SrTiO3

## Problem background
Bi³⁺–Li⁺ co‑doping in SrTiO₃ thin films has been proposed as a route to induce room‑temperature ferroelectricity. The idea is that a Bi³⁺ donor and a Li⁺ acceptor substituting adjacent Sr²⁺ sites along the [001] direction may form an ionic pair, generating a local dipole moment, an intrinsic electric field, and a lattice distortion that breaks the centrosymmetry of the paraelectric host. The formation of an ionic pair would leave a signature in the three independent Bi–Li distances that can be examined after geometry relaxation. In this task, you will use density functional theory (DFT) to relax a co‑doped SrTiO₃ supercell and extract those distances.

## Approach
The conceptual approach is a first‑principles DFT geometry optimization of a Bi‑Li co‑doped SrTiO₃ supercell. You will build a 3×3×3 supercell of cubic SrTiO₃ (space group Pm‑3m, lattice constant 3.905 Å), replace two adjacent Sr atoms along the [001] direction with Bi and Li, and then perform a full atomic relaxation using a spin‑polarized GGA‑PBE exchange‑correlation functional with ultrasoft pseudopotentials. The plane‑wave cutoff is set to 500 eV and a 3×3×3 Monkhorst–Pack k‑point mesh is used for Brillouin‑zone integration. After the relaxation converges, you will extract the three distinct interatomic Bi–Li distances: Z₂ (the distance along the [001] direction) and Z₁, Z₃ (the distances through alternative paths). Reporting these three numbers is the main output; the structural relation among them is the information that the hidden verifier uses to evaluate ionic‑pair formation.

## Reproduction target
The goal is to produce a JSON file containing the three Bi–Li distances in angstroms. The file must be named `step_03_ionic_pair_distances.json` and must contain three floating‑point keys: `"Z1"`, `"Z2"`, `"Z3"`. The scoring verifier will read these three numbers and evaluate whether their structural relationship is consistent with the formation of a Bi³⁺‑Li⁺ ionic pair. No additional outputs are needed, but you must perform the full DFT relaxation before extracting the distances; intermediate artifacts (supercell input, relaxation log) should be saved as evidence.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, ABINIT, GPAW): https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials for Sr, Ti, O, Bi, Li: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Build the Bi-Li doped SrTiO3 supercell
- Role: process
- Action: Construct a 3×3×3 supercell of cubic SrTiO3 (space group Pm-3m, lattice constant a=3.905 Å). Replace two adjacent Sr atoms along the [001] direction with Bi and Li, respectively. Save the input structure in a format suitable for the chosen DFT code.
- Evidence: none

### Step 2: DFT geometry relaxation of doped supercell
- Role: process
- Action: Using the chosen open-source DFT code, perform a spin-polarized GGA-PBE geometry optimization of the Bi-Li co-doped supercell. Use ultrasoft pseudopotentials for all elements, a plane-wave energy cutoff of 500 eV, and a 3×3×3 Monkhorst-Pack k-point grid. Relax atomic positions and optionally the cell until residual forces converge to a tight threshold. Save the relaxation log.
- Evidence: `/app/outputs/relax.log`

### Step 3: Extract Bi-Li interatomic distances
- Role: scored (load-bearing)
- Action: From the relaxed atomic positions, compute the three distances between the Bi and Li atoms: Z2 is the nearest neighbor distance along [001]; Z1 and Z3 are the two second-nearest distances through other paths. Report all distances in Å.
- Output file: `/app/outputs/step_03_ionic_pair_distances.json`
- Format: json
- Contract: {"Z1": number, "Z2": number, "Z3": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_ionic_pair_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_ionic_pair_distances.json
- path: `/app/outputs/step_03_ionic_pair_distances.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Bi-Li interatomic distances in Å, where Z2 is the nearest neighbor along [001], and Z1, Z3 are second-nearest distances. The checker verifies that Z2 < Z1 and Z2 < Z3 with a minimum absolute difference to absorb numerical noise.
- schema:
  - `type`: object
  - `required`:
    - `Z1`: number
    - `Z2`: number
    - `Z3`: number
  - `units`:
    - `Z1`: Å
    - `Z2`: Å
    - `Z3`: Å

Notes: The verification relies on structural ordering, not a specific numeric target, making it robust across different DFT implementations and pseudopotentials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_ionic_pair_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Z1": "number",
          "Z2": "number",
          "Z3": "number"
        },
        "units": {
          "Z1": "Å",
          "Z2": "Å",
          "Z3": "Å"
        }
      },
      "description": "Bi-Li interatomic distances in Å, where Z2 is the nearest neighbor along [001], and Z1, Z3 are second-nearest distances. The checker verifies that Z2 < Z1 and Z2 < Z3 with a minimum absolute difference to absorb numerical noise."
    }
  ],
  "notes": "The verification relies on structural ordering, not a specific numeric target, making it robust across different DFT implementations and pseudopotentials."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that inspects each scored workflow artifact and combines the per‑step rewards into a final reward between 0 and 1. The only scored artifact is `step_03_ionic_pair_distances.json`, which carries full weight. The verifier will first validate that the file is a well‑formed JSON containing exactly the three numeric keys `"Z1"`, `"Z2"`, `"Z3"`. It will then evaluate the relationship among Z1, Z2, and Z3 against a criterion derived from the ionic‑pair hypothesis—specifically, whether the distances satisfy a particular structural ordering. No exact numeric target is required; the scoring is based on the pattern of the three numbers, with a tolerance that absorbs numerical noise from different DFT implementations. You do not need to reproduce a specific published value, and reporting distances that do not exhibit the correct structural relation will not receive full credit. Importantly, you must genuinely run the DFT relaxation: the pattern you report will only be accepted if it emerges from a physically sound electronic‑structure calculation, and a trivial assignment of numbers without physics will not pass the structural check.
