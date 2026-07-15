# DFT Electronic Structure of Ti0.5Zr0.5NiSn Half-Heusler

## Problem background
Half-Heusler compounds are promising thermoelectric materials. Isovalent substitution at the X site (e.g., Ti<sub>x</sub>Zr<sub>1−x</sub>NiSn) can modify the electronic band structure, potentially increasing conduction band degeneracy and turning an indirect gap into a direct one at Γ, which may enhance the thermoelectric power factor. First‑principles density functional theory (DFT) calculations allow the screening of such compositions before synthesis. This task investigates the electronic band structure of the 50% X‑site substituted compound Ti<sub>0.5</sub>Zr<sub>0.5</sub>NiSn by a self‑consistent DFT workflow, producing the band eigenvalues needed to determine the nature of the band gap and the relative energy of conduction band edges at high‑symmetry points.

## Approach
The electronic structure of Ti<sub>0.5</sub>Zr<sub>0.5</sub>NiSn is calculated with plane‑wave density functional theory using the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation (GGA) for exchange and correlation. The compound is modeled by its 6‑atom primitive cell in the tetragonal space group P‑4‾m2 (No. 115). The workflow consists of three stages: (1) a variable‑cell structural relaxation to converge ionic forces and cell parameters, (2) a self‑consistent field (SCF) calculation on a dense k‑point mesh to obtain the ground‑state charge density, and (3) a non‑self‑consistent band structure run along a high‑symmetry path that includes the Γ (k = (0,0,0)) and M (k = (0.5,0.5,0)) points. Band eigenvalues, k‑point coordinates, k‑point labels, and the Fermi energy are collected and written to a JSON file. From these data one can locate the conduction and valence band edges at Γ and M and compute the direct band gap and the energy spacing between the conduction band minima at Γ and M.

## Reproduction target
Perform a fully self‑consistent GGA‑PBE DFT calculation on the 6‑atom primitive cell of Ti<sub>0.5</sub>Zr<sub>0.5</sub>NiSn (space group P‑4‾m2). After relaxing the cell, compute the electronic band structure along a high‑symmetry path that passes through Γ and M. Produce a JSON file (`band_structure.json`) that contains the band eigenvalues at every k‑point, k‑point coordinates and labels, and the Fermi energy. The two target quantities that will be evaluated from this file are: (1) the direct band gap at Γ, and (2) the energy difference between the lowest conduction band energies at Γ and at M. You do not need to report these numbers separately; the hidden verifier will compute them from your submitted JSON.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (PBE) for Ti, Zr, Ni, Sn: https://www.materialscloud.org/discover/sssp/table/presets/efficiency

## Workflow steps

### Step 1: Structural relaxation of Ti0.5Zr0.5NiSn primitive cell
- Role: process
- Action: Construct the 6-atom primitive cell of Ti0.5Zr0.5NiSn in space group P-4m2 (No. 115). Perform variable-cell relaxation using GGA-PBE DFT until forces are converged.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Self-consistent field (SCF) calculation
- Role: process
- Action: Run a converged SCF calculation on the relaxed structure using a dense k-point mesh to obtain the ground-state charge density.
- Evidence: `/app/outputs/scf.out`

### Step 3: Band structure calculation and eigenvalue extraction
- Role: scored (load-bearing)
- Action: Perform a non-self-consistent band structure calculation along a high-symmetry path that includes Γ (k=(0,0,0)) and M (k=(0.5,0.5,0)). Extract the band eigenvalues, k-point coordinates, labels, and Fermi energy, and write the result to band_structure.json.
- Output file: `/app/outputs/band_structure.json`
- Format: json
- Contract: JSON object with keys: 'k_points' (array of objects, each with 'label' (string), 'k_coords' (list of 3 floats)), 'eigenvalues' (array of arrays, shape (n_bands, n_kpoints)), 'fermi_energy' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure.json
- path: `/app/outputs/band_structure.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Band structure eigenvalues along a high-symmetry path. The checker recomputes two quantities: (1) direct band gap at Γ (energy difference between the highest valence and lowest conduction band at k=(0,0,0)), and (2) absolute energy difference between the conduction band minima at Γ and M (k=(0.5,0.5,0)).
- schema:
  - `type`: object
  - `required`:
    - `k_points`: array of objects
    - `eigenvalues`: array of arrays
    - `fermi_energy`: float
  - `items`:
    - `k_points[ ]`: object with keys: label (string), k_coords (list of 3 floats)
    - `eigenvalues`: list of bands, each band is a list of eigenenergies (float) at each k-point

Notes: The agent must use GGA-PBE exchange-correlation. The primitive cell belongs to space group P-4m2 (No. 115) with six atoms. The specific pseudopotentials (SSSP efficiency) are recommended.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "k_points": "array of objects",
          "eigenvalues": "array of arrays",
          "fermi_energy": "float"
        },
        "items": {
          "k_points[ ]": "object with keys: label (string), k_coords (list of 3 floats)",
          "eigenvalues": "list of bands, each band is a list of eigenenergies (float) at each k-point"
        }
      },
      "description": "Band structure eigenvalues along a high-symmetry path. The checker recomputes two quantities: (1) direct band gap at Γ (energy difference between the highest valence and lowest conduction band at k=(0,0,0)), and (2) absolute energy difference between the conduction band minima at Γ and M (k=(0.5,0.5,0))."
    }
  ],
  "notes": "The agent must use GGA-PBE exchange-correlation. The primitive cell belongs to space group P-4m2 (No. 115) with six atoms. The specific pseudopotentials (SSSP efficiency) are recommended."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow step’s artifact and combines the results by weight into a final reward between 0 and 1. For the band structure step, the verifier reads your `band_structure.json`, locates the valence band maximum and the lowest conduction band at Γ and at M, recomputes the direct gap and the Γ–M conduction‑band‑energy difference, and compares these values to hidden reference values with tolerances that account for legitimate spread among DFT implementations and pseudopotentials. Meeting or exceeding the expected agreement earns full credit for that step; reward degrades only as the result deviates further. The final reward is the weighted combination of the scores from all scored steps (here predominantly this step). Reporting numbers alone is not sufficient—the submited JSON artifact must pass shape and content validation.
