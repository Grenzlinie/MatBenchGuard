# DFT-based Free-Energy Barriers for CO₂ Reduction on Copper Surfaces

## Problem background
Electrochemical reduction of CO₂ to hydrocarbon fuels on copper catalysts is a promising route for carbon recycling, but the reaction mechanism and the role of different Cu surface facets remain not fully understood. A critical step in the conversion of CO₂ to CH₄ is the hydrogenation of adsorbed CO to CHO (CO* → CHO*), which often limits the overall rate. This task investigates how the free‑energy barrier of this key step depends on the surface structure of copper — specifically on the low‑index Cu(100), Cu(110), and Cu(111) facets — and explores whether expanding the Cu lattice by supporting a single Cu layer on Pd(111) can affect the barrier. Determining these barriers from first‑principles provides insight into designing more efficient catalysts for CO₂ reduction.

## Approach
The approach is a plane‑wave density functional theory (DFT) study combined with the computational hydrogen electrode (CHE) model. Using an open‑source DFT code (Quantum ESPRESSO) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and projector‑augmented wave (PAW) pseudopotentials, the following workflow is executed:

1. Construction of four‑layer slab models for Cu(100), Cu(110), and Cu(111) with adequate vacuum, and optimization of the bulk Cu lattice constant.
2. DFT optimisation of gas‑phase molecules (CO₂, H₂, H₂O, CH₄, CO) to obtain reference total energies.
3. Adsorption of the intermediates CO* and CHO* on each Cu facet, full geometry relaxation, and vibrational frequency calculations to extract zero‑point energies and entropies.
4. Construction of a heterostructure consisting of a single Cu(111) layer on top of a four‑layer Pd(111) slab, relaxation of the system, and subsequent adsorption and vibrational analysis of CO* and CHO* on the Cu overlayer.
5. Application of the CHE model at 18.5 °C, including standard solvation energy corrections, to convert the DFT total energies, zero‑point energies, and entropies into free energies. The free‑energy barrier for CO* → CHO* on each surface is computed as ΔG(CHO*) − ΔG(CO*).

## Reproduction target
Compute the free‑energy barriers (in eV) for the potential‑limiting step CO* → CHO* on four surfaces:
- Cu(100)
- Cu(110)
- Cu(111)
- a single Cu layer on Pd(111) (denoted CuPd(111)).

All four barriers must be positive numbers and must be written to a JSON file `/app/outputs/barriers.json` with exactly the keys `"Cu(100)"`, `"Cu(110)"`, `"Cu(111)"`, and `"CuPd(111)"`. Each value is a float representing the barrier in eV. The barriers should be derived from the DFT‑CHE protocol described in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary pseudopotentials (PBE, PAW) for Cu, Pd, O, C, H: https://www.quantum-espresso.org/pseudopotentials
- Supplementary Information for the article: https://ars.els-cdn.com/content/image/1-s2.0-S2210271X1630069X-mmc1.pdf

## Workflow steps

### Step 1: Prepare Cu bulk and surface slab models
- Role: process
- Action: Construct four-layer slab models of Cu(100)-p(3×3), Cu(110)-p(3×3), and Cu(111)-p(4×4) surfaces with vacuum > 25.7 Å. Fix the bottom two layers. Optimize the bulk lattice constant and relax the clean surfaces.
- Evidence: `/app/outputs/surface_models.log`

### Step 2: Optimize gas-phase molecules
- Role: process
- Action: Perform DFT optimization of gas-phase CO2, H2, H2O, CH4, CO in cubic boxes; obtain total energies.
- Evidence: `/app/outputs/gas_energies.log`

### Step 3: Adsorb CO* and CHO* on Cu surfaces
- Role: process
- Action: Construct adsorption structures for CO* and CHO* on each Cu facet. Optimize geometries. Perform vibrational frequency calculations to obtain zero-point energies and entropies.
- Evidence: `/app/outputs/adsorb_cu_frequencies.log`

### Step 4: Build and optimize Cu monolayer on Pd(111) and adsorb intermediates
- Role: process
- Action: Construct a single Cu(111) layer on top of a four-layer Pd(111) slab. Relax the heterostructure. Adsorb CO* and CHO* on the Cu layer, optimize and compute vibrational frequencies.
- Evidence: `/app/outputs/cupd_frequencies.log`

### Step 5: Compute and output free-energy barriers
- Role: scored (load-bearing)
- Action: Using the total energies, zero-point energies, and entropies from previous steps, apply the computational hydrogen electrode (CHE) model at 18.5°C. Include solvation energy corrections for the adsorbates as per standard practice (or from the supplementary information). Compute the free-energy change ΔG for CO* → CHO* on each surface as ΔG(CHO*) - ΔG(CO*). Output the four barriers (positive numbers, in eV) to a JSON file.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"Cu(100)": <float>, "Cu(110)": <float>, "Cu(111)": <float>, "CuPd(111)": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Free-energy barriers for the CO* → CHO* step on the four surfaces. Each value is a nonnegative float in eV.
- schema:
  - `type`: object
  - `required`:
    - `Cu(100)`: number
    - `Cu(110)`: number
    - `Cu(111)`: number
    - `CuPd(111)`: number
  - `units`:
    - `Cu(100)`: eV
    - `Cu(110)`: eV
    - `Cu(111)`: eV
    - `CuPd(111)`: eV

Notes: The hidden checker will compare the reported barriers to reference values with an appropriate tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cu(100)": "number",
          "Cu(110)": "number",
          "Cu(111)": "number",
          "CuPd(111)": "number"
        },
        "units": {
          "Cu(100)": "eV",
          "Cu(110)": "eV",
          "Cu(111)": "eV",
          "CuPd(111)": "eV"
        }
      },
      "description": "Free-energy barriers for the CO* → CHO* step on the four surfaces. Each value is a nonnegative float in eV."
    }
  ],
  "notes": "The hidden checker will compare the reported barriers to reference values with an appropriate tolerance."
}
```

## How you are scored
A hidden verifier will read your `barriers.json` and compare each barrier to reference values determined from the published study, accepting a reasonable tolerance that accounts for the use of a different DFT code (Quantum ESPRESSO versus the paper’s VASP) and pseudopotential details while being strict enough that a guess is unlikely to succeed. The final reward is based on the agreement of the barrier values with the reference values. Simply reporting numbers without obtaining them from the described DFT workflow will not yield full credit.
