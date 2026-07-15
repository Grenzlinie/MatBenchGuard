# Thermoelectric ZT of SnSe hybrids and layered CsPbI3 from DFT

## Problem background
Thermoelectric materials convert heat into electricity and vice versa; improving their efficiency (measured by the figure of merit ZT) is an active research area. This work computationally explores the electronic thermoelectric performance (ZT_elec) of two types of nanostructured systems: (1) hybrid compounds formed by tin selenide (SnSe) with either hexagonal boron nitride (h-BN) or cesium lead iodide (CsPbI₃), and (2) layered α‑CsPbI₃ slabs with one to four layers. The electronic-only ZT is calculated from first-principles density functional theory (DFT) and semi‑classical Boltzmann transport theory, providing insight into the potential of these materials for thermoelectric applications.

## Approach
Use density functional theory (PBE functional with vdW‑DFT3 van der Waals correction) as implemented in Quantum ESPRESSO to relax the initial crystal structures of the SnSe‑hBN and SnSe‑CsPbI₃ hybrids, as well as monolayer, bilayer, three‑layer, and four‑layer α‑CsPbI₃. From the relaxed geometries, perform a self‑consistent field (SCF) calculation to obtain the charge density and Kohn–Sham eigenvalues on a coarse k‑mesh. Then run a non‑self‑consistent (NSCF) calculation on a dense k‑point mesh to produce fine eigenvalues suitable for transport. Apply the BoltzTraP2 code under the constant scattering time approximation (CSTA) to compute the electronic transport coefficients σ/τ, S, and κ₀/τ. From these, determine the electronic figure of merit ZT_elec = S²σT/κ₀ at temperatures from 100 K to 1000 K. For the layered CsPbI₃, additionally identify the maximum ZT_elec and the temperature where it occurs for each layer count. All initial atomic coordinates are provided in a publicly available dataset; the agent fetches them and produces the final scored JSON artifacts. Band structure and projected density of states are optional and not required for scoring.

## Reproduction target
Produce two JSON files under `/app/outputs`:

1. `hybrid_zt.json` – an object with keys `"SnSe-hBN"` and `"SnSe-CsPbI3"`. Each key maps to an array of objects, each containing `"temperature_K"` (integer) and `"ZTelec"` (float), covering the temperatures 100,200,300,400,500,600,700,800,900,1000 K.

2. `layered_cspbi3_zt.json` – an object with keys `"monolayer"`, `"bilayer"`, `"three-layer"`, `"four-layer"`. Each key maps to an object with `"ZTelec_max"` (float) and `"temperature_K"` (integer) representing the peak electronic figure of merit and the temperature at which it occurs for that layer count.

The ZT_elec values must be derived from the full DFT + BoltzTraP workflow; the shape and content of the output files are validated by a hidden verifier.

## Assets

- Mendeley dataset (py638t2nmg) containing initial crystal structures: https://data.mendeley.com/datasets/py638t2nmg/1
- Quantum ESPRESSO: https://www.quantum-espresso.org
- BoltzTraP2: https://www.boltztrap.org
- SSSP efficiency pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Fetch initial structures
- Role: process
- Action: Download the Mendeley dataset (py638t2nmg) and extract input files (atomic coordinates and cell parameters) for SnSe-hBN, SnSe-CsPbI3 hybrids and monolayer, bilayer, three-layer, four-layer CsPbI3.
- Evidence: `/app/outputs/structures_manifest.txt`

### Step 2: DFT geometry relaxation for hybrid compounds
- Role: process
- Action: Run Quantum ESPRESSO pw.x with PBE+vdW-DFT3 functional to relax atomic positions of SnSe-hBN and SnSe-CsPbI3 until forces are below convergence threshold.
- Evidence: `/app/outputs/relax_hybrids.out`

### Step 3: SCF calculation for hybrids (coarse k-mesh)
- Role: process
- Action: Perform self-consistent field calculation for the relaxed hybrids to obtain charge density and Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/scf_hybrids.out`

### Step 4: Fine k-mesh NSCF calculation for hybrids
- Role: process
- Action: Run a non-self-consistent field calculation on a dense k-point mesh for both hybrids using the SCF charge density to obtain eigenvalues suitable for transport calculations.
- Evidence: `/app/outputs/nscf_hybrids.out`

### Step 5: Band structure and PDOS for hybrids
- Role: process
- Action: Compute electronic band structure along high-symmetry lines and atom-projected density of states for both hybrids using bands.x and projwfc.x.
- Evidence: `/app/outputs/bands_hybrids.dat, pdos_hybrids.dat`

### Step 6: Calculate ZT_elec for hybrids and write hybrid_zt.json
- Role: scored (load-bearing)
- Action: Use BoltzTraP2 to process the fine k-mesh eigenvalues for SnSe-hBN and SnSe-CsPbI3. For each compound, determine the maximum ZT_elec at temperatures 100,200,...,1000 K. Write the results to 'hybrid_zt.json' as a JSON object with keys 'SnSe-hBN' and 'SnSe-CsPbI3', each containing an array of objects with 'temperature_K' (integer) and 'ZTelec' (float).
- Output file: `/app/outputs/hybrid_zt.json`
- Format: json
- Contract: {'SnSe-hBN': [{'temperature_K': integer, 'ZTelec': float}], 'SnSe-CsPbI3': [{'temperature_K': integer, 'ZTelec': float}]}
- Scoring: scored by hidden verifier

### Step 7: Geometry relaxation for layered CsPbI3
- Role: process
- Action: Run Quantum ESPRESSO pw.x to relax monolayer, bilayer, three-layer, and four-layer CsPbI3 slabs using PBE+vdW-DFT3.
- Evidence: `/app/outputs/relax_cspbi3.out`

### Step 8: SCF and fine k-mesh NSCF for layered CsPbI3
- Role: process
- Action: Perform SCF and subsequent non-self-consistent field calculation on a dense k-point mesh for each relaxed CsPbI3 layer configuration.
- Evidence: `/app/outputs/scf_nscf_cspbi3.out`

### Step 9: Band structure and PDOS for layered CsPbI3
- Role: process
- Action: Compute band structure and projected density of states for each layered CsPbI3 using bands.x and projwfc.x.
- Evidence: `/app/outputs/bands_cspbi3.dat, pdos_cspbi3.dat`

### Step 10: Calculate ZT_elec for layered CsPbI3 and write layered_cspbi3_zt.json
- Role: scored (load-bearing)
- Action: Run BoltzTraP2 for each layer configuration. For each, find the maximum ZT_elec value and the temperature at which it occurs. Output 'layered_cspbi3_zt.json' with keys 'monolayer','bilayer','three-layer','four-layer', each containing {'ZTelec_max': float, 'temperature_K': int}.
- Output file: `/app/outputs/layered_cspbi3_zt.json`
- Format: json
- Contract: {'monolayer': {'ZTelec_max': float, 'temperature_K': int}, 'bilayer': {'ZTelec_max': float, 'temperature_K': int}, 'three-layer': {'ZTelec_max': float, 'temperature_K': int}, 'four-layer': {'ZTelec_max': float, 'temperature_K': int}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hybrid_zt.json`
- `/app/outputs/layered_cspbi3_zt.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hybrid_zt.json
- path: `/app/outputs/hybrid_zt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Electronic-only figure of merit for the two hybrid compounds at 10 temperatures.
- schema:
  - `type`: object
  - `required`:
    - `SnSe-hBN`: array of objects with integer 'temperature_K' and float 'ZTelec' for temperatures 100,200,...,1000 K
    - `SnSe-CsPbI3`: array of objects with integer 'temperature_K' and float 'ZTelec' for temperatures 100,200,...,1000 K

### layered_cspbi3_zt.json
- path: `/app/outputs/layered_cspbi3_zt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Maximum ZT_elec and the temperature where it occurs for each CsPbI3 layer count.
- schema:
  - `type`: object
  - `required`:
    - `monolayer`: object with float 'ZTelec_max' and integer 'temperature_K'
    - `bilayer`: object with float 'ZTelec_max' and integer 'temperature_K'
    - `three-layer`: object with float 'ZTelec_max' and integer 'temperature_K'
    - `four-layer`: object with float 'ZTelec_max' and integer 'temperature_K'

Notes: The agent must run the full DFT geometry relaxation, SCF, and dense k-mesh NSCF for all structures before computing ZT_elec with BoltzTraP2. Band structure/PDOS are optional and not required for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hybrid_zt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "SnSe-hBN": "array of objects with integer 'temperature_K' and float 'ZTelec' for temperatures 100,200,...,1000 K",
          "SnSe-CsPbI3": "array of objects with integer 'temperature_K' and float 'ZTelec' for temperatures 100,200,...,1000 K"
        }
      },
      "description": "Electronic-only figure of merit for the two hybrid compounds at 10 temperatures."
    },
    {
      "file": "layered_cspbi3_zt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "monolayer": "object with float 'ZTelec_max' and integer 'temperature_K'",
          "bilayer": "object with float 'ZTelec_max' and integer 'temperature_K'",
          "three-layer": "object with float 'ZTelec_max' and integer 'temperature_K'",
          "four-layer": "object with float 'ZTelec_max' and integer 'temperature_K'"
        }
      },
      "description": "Maximum ZT_elec and the temperature where it occurs for each CsPbI3 layer count."
    }
  ],
  "notes": "The agent must run the full DFT geometry relaxation, SCF, and dense k-mesh NSCF for all structures before computing ZT_elec with BoltzTraP2. Band structure/PDOS are optional and not required for scoring."
}
```

## How you are scored
A hidden verifier reads your two output JSON files and independently compares them against reference values that represent a faithful reproduction of the paper's computational protocol. Each ZT_elec value (or peak location) is assessed with appropriate numerical tolerances, giving partial credit for close agreement. The final reward (0.0–1.0) is a weighted combination of the scores from both output files, with roughly equal weight. The verifier does not reveal the reference numbers; you must obtain the results by running the DFT calculations and BoltzTraP post‑processing, not by guessing or looking up reported values.
