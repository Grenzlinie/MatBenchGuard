# DFT energy surface and anharmonic coupling analysis for a layered thiophosphate

## Problem background
CuInP2Se6 undergoes a transition from a paraelectric (PE) parent phase to a ferrielectric (FiE) ground state. The polar distortion that drives this transition involves large displacements of the Cu and In atoms, yet the polar mode on its own yields only a very shallow energy well. This suggests that coupling to non‑polar structural distortions—in particular a fully symmetric Raman‑active mode—may be essential for stabilizing the FiE phase. The goal of this task is to quantify that anharmonic coupling by computing the total‑energy surface as a function of the two relevant mode coordinates and extracting the coupling coefficients.

## Approach
You will use density functional theory (DFT) to map the total energy of CuInP2Se6 on a two‑dimensional grid spanned by the fractional amplitudes of the polar Γ2⁻ mode and the fully symmetric Γ1⁺ mode. Starting from the paraelectric crystal structure (space group P‑31c) and the symmetry‑adapted displacement vectors listed in the paper, you will generate 49 structures covering all combinations of the two amplitudes on a 7×7 grid. For each structure you will run a single‑point DFT calculation at fixed PE lattice constants with the Perdew–Burke–Ernzerhof (PBE) functional and the DFT‑D2 van der Waals correction, collect the total energy, and report the resulting energy surface as a CSV. From this surface the hidden verifier will later fit a polynomial expansion to isolate the anharmonic coupling between the two modes.

## Reproduction target
Produce a CSV file (`step_01_energy_surface.csv`) containing the total energies (in meV per formula unit, relative to the PE phase) for all 49 (Q1, Q2) points on the grid Q1, Q2 ∈ {−1.5, −1.0, −0.5, 0.0, 0.5, 1.0, 1.5}. The hidden verifier will fit a polynomial expansion to these 49 data points, extract the anharmonic coupling coefficients, and evaluate how strongly the coupling term stabilizes the polar phase relative to the harmonic term.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code with PBE+DFT-D2): https://www.quantum-espresso.org/
- PBE pseudopotentials (e.g., SSSP efficiency library): https://www.materialscloud.org/discover/sssp
- Python libraries (numpy, scipy) for structure generation and data handling: pip install numpy scipy

## Workflow steps

### Step 1: Generate the two-mode structure grid
- Role: process
- Action: Construct the paraelectric unit cell of CuInP2Se6 (space group P-31c) using the lattice constants a=6.37 Å, c=13.20 Å and Wyckoff positions (Cu 2d, In 2a, P 4f, Se 12i) from the paper's Table I. Build the displacement vectors for the fully symmetric Γ1⁺ mode and the polar Γ2⁻ mode from the symmetry-adapted mode amplitudes given in Table III. Generate all 49 structures by applying the fractional amplitudes (Q1, Q2) on the grid {-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5} for each mode. Write each structure as a DFT input file (e.g., Quantum ESPRESSO input) in a subdirectory.
- Evidence: `/app/outputs/structures_grid.zip`

### Step 2: Compute DFT total-energy surface and output CSV
- Role: scored (load-bearing)
- Action: For each of the 49 structures, perform a single-point DFT total-energy calculation using the PBE functional with the DFT-D2 van der Waals correction, a plane-wave cutoff of 600 eV, and a Γ-centered Monkhorst-Pack k-point grid of 8×8×4. Use the fixed PE lattice constants. After all calculations, compute the energy of each structure relative to the PE reference energy (in meV per formula unit). Write a CSV file with columns Q1, Q2, energy_mev_per_fu containing the 49 data points.
- Output file: `/app/outputs/step_01_energy_surface.csv`
- Format: csv
- Contract: CSV with exactly 49 rows and 3 columns: Q1 (float, fractional amplitude of Γ1⁺ mode), Q2 (float, fractional amplitude of Γ2⁻ mode), energy_mev_per_fu (float, total energy relative to the PE phase in meV per formula unit).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_energy_surface.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_energy_surface.csv
- path: `/app/outputs/step_01_energy_surface.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed total-energy surface on the two-mode (Q1, Q2) grid relative to the paraelectric reference phase in meV per formula unit.
- schema:
  - `type`: table
  - `required_columns`: `Q1`, `Q2`, `energy_mev_per_fu`
  - `units`: object

Notes: The checker refits the polynomial expansion E = b02 Q2² + b04 Q2⁴ + b06 Q2⁶ + b08 Q2⁸ + c12 Q1 Q2² + c14 Q1 Q2⁴ + a20 Q1² to the submitted energies and compares the fitted coefficients to the paper's reported values. Reward is awarded based on tolerance thresholds for each coefficient and the structural condition that c12 is negative and |c12| > |b02|.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_energy_surface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q1",
          "Q2",
          "energy_mev_per_fu"
        ],
        "units": {}
      },
      "description": "Computed total-energy surface on the two-mode (Q1, Q2) grid relative to the paraelectric reference phase in meV per formula unit."
    }
  ],
  "notes": "The checker refits the polynomial expansion E = b02 Q2² + b04 Q2⁴ + b06 Q2⁶ + b08 Q2⁸ + c12 Q1 Q2² + c14 Q1 Q2⁴ + a20 Q1² to the submitted energies and compares the fitted coefficients to the paper's reported values. Reward is awarded based on tolerance thresholds for each coefficient and the structural condition that c12 is negative and |c12| > |b02|."
}
```

## How you are scored
A hidden verifier reads your `step_01_energy_surface.csv`. It fits a polynomial model that includes harmonic and anharmonic terms for the polar mode and cross terms that couple the polar mode to the fully symmetric mode. The verifier compares the fitted coefficients to a set of reference values using tolerances that account for implementation‑level spread (different DFT code, pseudopotential library, etc.) and checks a structural condition relating the magnitude and sign of the dominant coupling coefficient to other terms. The final reward aggregates agreement across the key coefficients, with the largest weight placed on the primary anharmonic coupling coefficient. Reporting correct energies for the entire grid is essential; no credit is given for simply guessing or self‑reporting a summary number.
