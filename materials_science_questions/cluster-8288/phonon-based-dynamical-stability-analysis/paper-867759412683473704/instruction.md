# Electric-field control of spin splitting in bilayer MoSi2N4

## Problem background
Monolayer MoSi2N4 is a two-dimensional semiconductor with a hexagonal crystal structure (space group D₃h). In the monolayer, inversion symmetry is absent, and spin-orbit coupling (SOC) lifts the spin degeneracy of the electronic states at the K and K' points in the Brillouin zone, producing spin-split bands with an out-of-plane spin texture. When two such layers are stacked in a 2H bilayer, the combined structure recovers an inversion centre, suppressing the spin splitting. An out-of-plane external electric field can break this symmetry, inducing tunable spin splitting in the bilayer. The task is to quantify this electric-field-controlled spin splitting in MoSi2N4 by computing the spin-resolved band structure of monolayer and bilayer under various field strengths.

## Approach
Use density functional theory (DFT) with spin-orbit coupling to model the electronic structure. First, perform geometry optimizations of the monolayer and bilayer MoSi2N4 primitive cells (using GGA functionals, plane-wave basis sets, and appropriate convergence criteria) to obtain relaxed lattice constants and atomic positions. Then, compute the band structure of the optimized monolayer including SOC and extract the energy splitting between the topmost valence bands at the K point (Δ_SOC) and the indirect bandgap. For the bilayer, apply an out-of-plane electric field across the slab; repeat the SOC calculation for a set of field strengths (covering zero and several non-zero values). At each field, analyse the four highest valence bands around K to identify their spin and layer composition. From these bands, define two splitting quantities: Δ_intra, the energy separation between the spin-up and spin-down states belonging to the same layer, and Δ_inter, the separation between the spin-up state of one layer and the spin-down state of the other. The results are collected as a function of field strength.

## Reproduction target
Compute the spin splitting at the K point for monolayer MoSi2N4 and report its value (in meV) together with the indirect bandgap (in eV). For bilayer MoSi2N4, compute Δ_intra and Δ_inter for a series of out-of-plane electric fields (listed in the workflow steps) and report them as a table. From the bilayer data, characterise the field dependence: test whether Δ_inter follows a systematic trend (e.g., linear) and whether Δ_intra remains nearly constant, and determine the field strength (if any) where the two components become comparable (crossover). The goal is to verify whether the electric field can controllably tune the spin splitting and to locate the crossover regime.

## Assets

- Quantum ESPRESSO (open-source DFT code with SOC support): https://www.quantum-espresso.org/
- SSSP precision pseudopotentials (PBE or PBEsol) for Mo, Si, N: https://www.materialscloud.org/discover/sssp/table/precision
- NumPy: numpy
- Pymatgen: pymatgen
- PyProcar: pyprocar

## Workflow steps

### Step 1: Geometry optimization of monolayer MoSi2N4
- Role: process
- Action: Perform DFT structural relaxation for the monolayer MoSi2N4 primitive cell using GGA functional, plane-wave basis, and appropriate k-point sampling. Obtain optimized lattice constant and atomic positions.
- Evidence: `/app/outputs/monolayer_relaxed.cif`

### Step 2: Geometry optimization of bilayer MoSi2N4
- Role: process
- Action: Perform DFT structural relaxation for the bilayer MoSi2N4 (2H stacked) primitive cell using GGA functional, plane-wave basis, and appropriate k-point sampling. Optimize lattice constant and interlayer distance.
- Evidence: `/app/outputs/bilayer_relaxed.cif`

### Step 3: Monolayer spin splitting and bandgap
- Role: scored (load-bearing)
- Action: Run a DFT+SOC self-consistent calculation on the optimized monolayer structure, then compute the band structure along a high-symmetry path including the K point. Extract the energy difference between the two topmost valence bands at K (Δ_SOC, in meV) and the indirect bandgap (eV).
- Output file: `/app/outputs/monolayer_spin_splitting.json`
- Format: json
- Contract: JSON object with keys: 'delta_soc_mev' (float), 'band_gap_indirect_ev' (float).
- Scoring: scored by hidden verifier

### Step 4: Bilayer field-dependent spin splitting components
- Role: scored (load-bearing)
- Action: Using the optimized bilayer structure, perform DFT+SOC calculations with an applied out-of-plane electric field for the following Ez values: 0, 0.005, 0.01, 0.012, 0.015, 0.02, 0.025, 0.03 eV/Å. For each field, compute the band structure near K, identify the top four valence band energies and their spin and layer characters. Derive the intra-layer splitting Δ_intra (energy difference between spin-up and spin-down states from the same layer) and the inter-layer splitting Δ_inter (energy difference between first-layer spin-up and second-layer spin-down states). Output the results as a CSV.
- Output file: `/app/outputs/bilayer_ez_splitting.csv`
- Format: csv
- Contract: CSV with columns: Ez (eV/Angstrom), Delta_intra (meV), Delta_inter (meV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/monolayer_spin_splitting.json`
- `/app/outputs/bilayer_ez_splitting.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### monolayer_spin_splitting.json
- path: `/app/outputs/monolayer_spin_splitting.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Monolayer spin splitting at K and indirect bandgap.
- schema:
  - `type`: object
  - `required`:
    - `delta_soc_mev`: float, unit: meV
    - `band_gap_indirect_ev`: float, unit: eV

### bilayer_ez_splitting.csv
- path: `/app/outputs/bilayer_ez_splitting.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Electric-field-dependent intra- and inter-layer spin splitting components.
- schema:
  - `type`: table
  - `required_columns`: `Ez`, `Delta_intra`, `Delta_inter`
  - `units`:
    - `Ez`: eV/Angstrom
    - `Delta_intra`: meV
    - `Delta_inter`: meV

Notes: The checker will recompute the linear trend of Δ_inter vs E_z and verify the slope and intercept, and check that Δ_intra is nearly constant. It will also compute the crossover field from the fitted line and verify it lies within a narrow range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "monolayer_spin_splitting.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_soc_mev": "float, unit: meV",
          "band_gap_indirect_ev": "float, unit: eV"
        }
      },
      "description": "Monolayer spin splitting at K and indirect bandgap."
    },
    {
      "file": "bilayer_ez_splitting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ez",
          "Delta_intra",
          "Delta_inter"
        ],
        "units": {
          "Ez": "eV/Angstrom",
          "Delta_intra": "meV",
          "Delta_inter": "meV"
        }
      },
      "description": "Electric-field-dependent intra- and inter-layer spin splitting components."
    }
  ],
  "notes": "The checker will recompute the linear trend of Δ_inter vs E_z and verify the slope and intercept, and check that Δ_intra is nearly constant. It will also compute the crossover field from the fitted line and verify it lies within a narrow range."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. For the monolayer JSON, the verifier compares your reported Δ_SOC and bandgap to reference values derived from the same theoretical approach, applying a tolerance that accounts for implementation- and pseudopotential-induced spread. For the bilayer CSV, the verifier fits a linear model to Δ_inter vs Ez and checks the quality of the fit (e.g., R²) and whether the slope has the expected sign, while also testing that Δ_intra is approximately field-independent; it then computes the crossover field from the fitted line and compares it to the reference. The final reward is a weighted combination of the monolayer and bilayer scores.
