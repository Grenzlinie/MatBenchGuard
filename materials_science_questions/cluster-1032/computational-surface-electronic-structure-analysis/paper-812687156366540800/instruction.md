# DFT band dispersion of nitrogen-induced surface state on Rh(110)

## Problem background
Nitrogen adsorbed on Rh(110) forms a (2×1) missing‑row reconstruction where N atoms occupy long‑bridge sites, creating Rh–N–Rh chains along the [001] direction. Ultraviolet photoemission spectroscopy (UPS) reveals a nitrogen‑induced valence band that is expected to show strong dispersion along the chain direction but negligible dispersion perpendicular to it, attributed to a N p y‑derived band. This electronic structure can be computed via first‑principles DFT slab calculations to characterize the anisotropic dispersion.

## Structural model parameters

The (2×1) missing‑row reconstruction of N/Rh(110) has been determined by LEED I‑V analysis (structural parameters taken from published experimental results). The structure consists of Rh–N–Rh chains along the [001] direction with every second [001] row of Rh atoms missing. Nitrogen atoms occupy the long‑bridge sites between two Rh atoms in the remaining chain.

The following parameters were determined by the experimental analysis:

| Parameter | Value (Å) | Description |
|-----------|-----------|-------------|
| Z₀ | 0.00 ± 0.08 | Vertical distance between N atoms and the first Rh layer |
| d₁₂ | 1.33 ± 0.08 | Interlayer spacing between first and second Rh layers |
| d₂₃ | 1.27 ± 0.10 | Interlayer spacing between second and third Rh layers |
| δ | 0.00 ± 0.10 | Lateral displacement of second‑layer Rh atoms along [1‾10] |
| Rh–N bond (1st layer) | 1.87 ± 0.08 | Distance from N to the nearest first‑layer Rh atom |
| Rh–N bond (2nd layer) | 1.94 ± 0.08 | Distance from N to the nearest second‑layer Rh atom |

The Rh(110) surface lattice constants are derived from bulk fcc Rh (a₀ = 3.804 Å):
- along [1‾10]: a = a₀/√2 ≈ 2.690 Å
- along [001]: b = a₀ ≈ 3.804 Å

The (2×1) unit cell therefore has dimensions (2a) × b, i.e., 5.380 Å × 3.804 Å.

Build a slab containing at least five Rh layers. Fix the bottom two layers at their bulk positions. Add a vacuum region of at least 12 Å. Use the values from the table above (the central values, ignoring the error bars) to set the initial geometry, and relax all atoms except the fixed bottom layers until forces are below 0.02 eV/Å.

## Approach
Construct a slab model of the (2×1) missing‑row N/Rh(110) surface using the structural parameters provided above. Perform DFT calculations (SCF followed by non‑self‑consistent band structure) using a plane‑wave pseudopotential code (e.g., Quantum ESPRESSO). Extract the Kohn–Sham eigenvalues along high‑symmetry lines of the surface Brillouin zone: Γ̄–Ȳ (the chain direction) and Γ̄–X̄ (the perpendicular direction). From the computed band structure, identify the band dominated by N p y character and tabulate its binding energy as a function of parallel momentum for both azimuths. The final output is a CSV file containing the dispersion data.

## Reproduction target
Produce a CSV file (`step_01_dispersion.csv`) with columns: `azimuth` (`'GammaY'` or `'GammaX'`), `k_parallel` (float, units 1/Å), and `binding_energy` (float, units eV). The file must report the binding energy of the nitrogen‑derived band at a set of k‑points covering the full Γ̄–Ȳ and Γ̄–X̄ paths. The submitted data must capture the anisotropic dispersion expected from the Rh–N–Rh chain model: the band should show strong dispersion along Γ̄–Ȳ and be nearly flat along Γ̄–X̄. The hidden verifier will check the magnitude and trend of the dispersion.

## Assets

- Quantum ESPRESSO (or equivalent plane‑wave DFT code): https://www.quantum-espresso.org/
- Rhodium pseudopotential: https://www.quantum-espresso.org/pseudopotentials
- Nitrogen pseudopotential: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Slab model construction and SCF calculation
- Role: process
- Action: Construct a slab model of the (2×1) missing‑row N/Rh(110) surface using the structural parameters provided in the “Structural model parameters” section (N in long‑bridge sites, Rh–N bond lengths, interlayer distances, vacuum region). Perform a self‑consistent field (SCF) DFT calculation to obtain the ground‑state charge density. Ensure convergence with respect to k‑point sampling, plane‑wave cutoff, and slab thickness.

### Step 2: Band structure calculation
- Role: process
- Action: Using the SCF charge density, perform a non‑self‑consistent band structure calculation along the surface Brillouin‑zone paths Γ̄–Ȳ (chain direction) and Γ̄–X̄ (perpendicular direction). Extract the Kohn–Sham eigenvalues along these high‑symmetry lines.

### Step 3: Nitrogen‑derived band dispersion
- Role: scored (load-bearing)
- Action: Identify the band with dominant N p_y character (strong dispersion along Γ̄–Ȳ). Tabulate its binding energy (negative eigenvalue relative to the Fermi level) as a function of parallel momentum k_∥ along both Γ̄–Ȳ and Γ̄–X̄ azimuths. Output one row per k‑point per azimuth.
- Output file: `/app/outputs/step_01_dispersion.csv`
- Format: csv
- Contract: Columns: azimuth (string, 'GammaY' or 'GammaX'), k_parallel (float, units 1/Å), binding_energy (float, units eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_dispersion.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_dispersion.csv
- path: `/app/outputs/step_01_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Binding energy of the nitrogen-derived surface band as a function of parallel momentum along Γ̄-Ȳ and Γ̄-X̄. The band is expected to show strong dispersion along Γ̄-Ȳ (increasing binding energy with k_parallel) and nearly flat dispersion along Γ̄-X̄.
- schema:
  - `type`: table
  - `required_columns`: `azimuth`, `k_parallel`, `binding_energy`
  - `units`:
    - `k_parallel`: 1/Å
    - `binding_energy`: eV

Notes: The structural model parameters (missing‑row, N site, bond lengths, interlayer distances) are provided in the instruction. The checker only scores the dispersion trend and magnitude; exact agreement with a specific DFT functional is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "azimuth",
          "k_parallel",
          "binding_energy"
        ],
        "units": {
          "k_parallel": "1/Å",
          "binding_energy": "eV"
        }
      },
      "description": "Binding energy of the nitrogen-derived surface band as a function of parallel momentum along Γ̄-Ȳ and Γ̄-X̄. The band is expected to show strong dispersion along Γ̄-Ȳ (increasing binding energy with k_parallel) and nearly flat dispersion along Γ̄-X̄."
    }
  ],
  "notes": "The structural model parameters (missing‑row, N site, bond lengths, interlayer distances) are provided in the instruction. The checker only scores the dispersion trend and magnitude; exact agreement with a specific DFT functional is not required."
}
```

## How you are scored
After you submit your output, a hidden verifier inspects the CSV and independently evaluates the dispersion trend along each azimuth. It computes the total variation of binding energy along Γ̄–Ȳ and Γ̄–X̄ and assigns a continuous reward between 0 and 1. Full reward requires that the dispersion along the chain direction is substantial and follows the expected qualitative trend, while the dispersion perpendicular to the chains is negligible. The verifier uses tolerances that accommodate differences due to DFT functional and pseudopotential choice. The better your computed dispersion matches the physical picture of anisotropic band behavior, the higher the score.