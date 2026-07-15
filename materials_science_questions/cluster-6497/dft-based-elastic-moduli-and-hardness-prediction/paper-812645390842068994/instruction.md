# DFT Bulk Modulus of Orthorhombic Cr₃C₂ via Energy‑Volume Calculations

## Problem background
Chromium carbide Cr₃C₂ is a refractory transition-metal carbide with exceptional hardness, wear resistance, and high-temperature stability, making it attractive for extreme applications such as aircraft engines. Understanding its mechanical response under pressure is essential for predicting its performance in high-stress environments. The equation of state — the relationship between pressure and volume — is characterized by the bulk modulus K₀ and its pressure derivative K₀′. This task focuses on the first-principles computational determination of the bulk modulus of orthorhombic Cr₃C₂ (space group Pnam). Using density functional theory (DFT), the original study predicted the bulk modulus; your job is to independently re-compute the energy-volume relationship and derive K₀ from the resulting data.

## Approach
The approach is to perform a series of DFT calculations on the orthorhombic unit cell of Cr₃C₂. Using a plane-wave basis and the Perdew‑Burke‑Ernzerhof (PBE) exchange-correlation functional, total energies are computed for a range of volumes by applying isotropic strains to the equilibrium lattice parameters a=5.4767 Å, b=11.4621 Å, c=2.7882 Å. At each volume, the atomic positions and cell shape are relaxed within the symmetry constraints. The resulting sets of (volume, total energy) are then fitted to the third-order Birch‑Murnaghan equation of state:

P(V) = 1.5 K₀ [(V₀/V)^(7/3) − (V₀/V)^(5/3)] { 1 + (3/4)(K₀′−4)[(V₀/V)^(2/3)−1] }.

The fitting yields the bulk modulus K₀ and its pressure derivative K₀′. This is a standard workflow in computational condensed‑matter physics. The DFT calculations can be carried out with any open‑source or commercial plane‑wave code; Quantum ESPRESSO with PAW pseudopotentials from a public library (SSSP) is a suitable, fully open‑source choice. The final output is a CSV file containing the computed volume-energy pairs.

## Reproduction target
Produce a CSV file named `volume_energy.csv` that contains at least six (volume, total_energy) data points for orthorhombic Cr₃C₂, computed from variable-cell DFT relaxations spanning approximately ±5% around the equilibrium volume. The columns are `volume` (in Å³) and `total_energy` (in eV). The hidden verifier will read this file, fit the data to the Birch‑Murnaghan equation of state to obtain the bulk modulus K₀, and compare your derived value to the expected value from the literature. The goal is to correctly reproduce the bulk modulus through your DFT calculations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP Precision PAW pseudopotentials (PBE) for Cr and C: https://www.materialscloud.org/discover/sssp/table/precision
- Crystal structure of orthorhombic Cr₃C₂ (space group Pnam)

## Workflow steps

### Step 1: DFT energy‑volume calculations
- Role: scored (load-bearing)
- Action: Set up and run first‑principles DFT calculations for orthorhombic Cr₃C₂ (space group Pnam) using an open‑source plane‑wave code (e.g., Quantum ESPRESSO) with PAW pseudopotentials and the PBE exchange‑correlation functional. Use the lattice parameters a=5.4767 Å, b=11.4621 Å, c=2.7882 Å as the starting point and perform variable‑cell relaxations at a range of volumes (at least 6 points spanning approximately ±5 % around the equilibrium volume). Extract the converged total energy and the final cell volume for each calculation and compile them into a CSV file.
- Output file: `/app/outputs/volume_energy.csv`
- Format: csv
- Contract: CSV with two columns: volume (float, unit: Å³) and total_energy (float, unit: eV). At least 6 rows covering a range around the equilibrium volume.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/volume_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### volume_energy.csv
- path: `/app/outputs/volume_energy.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Comma‑separated values file containing pairs of unit‑cell volume (Å³) and corresponding total DFT energy (eV). The hidden checker fits the third‑order Birch‑Murnaghan equation of state to these points, derives the bulk modulus K₀, and compares it to the paper‑reported value within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `volume`, `total_energy`
  - `units`:
    - `volume`: Å³
    - `total_energy`: eV

Notes: Only the DFT‑computed bulk modulus is reproduced; the experimental XRD results and the electronic structure analysis are excluded. The agent must execute the DFT calculations itself; the paper’s own DFT output is not provided as a resource.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "volume_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume",
          "total_energy"
        ],
        "units": {
          "volume": "Å³",
          "total_energy": "eV"
        }
      },
      "description": "Comma‑separated values file containing pairs of unit‑cell volume (Å³) and corresponding total DFT energy (eV). The hidden checker fits the third‑order Birch‑Murnaghan equation of state to these points, derives the bulk modulus K₀, and compares it to the paper‑reported value within a hidden tolerance."
    }
  ],
  "notes": "Only the DFT‑computed bulk modulus is reproduced; the experimental XRD results and the electronic structure analysis are excluded. The agent must execute the DFT calculations itself; the paper’s own DFT output is not provided as a resource."
}
```

## How you are scored
Your sole submission is the `volume_energy.csv` file. The hidden verifier will:
1. Read your CSV and verify it contains the required columns and a minimum number of rows.
2. Fit the third‑order Birch‑Murnaghan equation of state to your (volume, total_energy) points using a standard non‑linear least‑squares algorithm (e.g., SciPy's `curve_fit`). This yields your derived bulk modulus K₀.
3. Compare your derived K₀ to a hidden reference value (the paper's DFT prediction) with a hidden tolerance ±δ. If |K₀_derived − K₀_reference| ≤ δ, you receive full credit (reward 1.0); otherwise, reward 0.0.

You must perform the actual DFT calculations. Simply writing the paper's reported K₀ into the CSV as a single row or fabricating energy points that approximate the known value will not produce a set of energy-volume points that satisfy the Birch‑Murnaghan fit within tolerance; the verifier acts only on the data you provide. No partial credit is given for incomplete data or incorrect formatting.
