# DFT equation-of-state and bulk modulus of orthorhombic η-Ta₂N₃

## Problem background
Orthorhombic η‑Ta₂N₃ is a high‑pressure phase of tantalum nitride that is notable for its high incompressibility. Its equation of state and anisotropic compressibilities can be characterised by first‑principles density functional theory (DFT) calculations. In this task you will compute the pressure–volume behaviour of η‑Ta₂N₃ using DFT with the PBE functional. From the computed data you will generate a set of points from which zero‑pressure lattice parameters and the bulk modulus can be derived.

## Approach
Plane‑wave DFT with the PBE exchange‑correlation functional is used. Starting from the provided crystal structure, you will fully relax the cell and atomic positions at zero pressure using a plane‑wave cutoff and k‑point sampling that meet the convergence criteria below. After relaxation, you will perform a series of static calculations at a range of cell volumes (or hydrostatic pressures) spanning 0–30 GPa. For each configuration, record the calculated hydrostatic pressure, volume, and lattice parameters a, b, c. These data are written to a CSV file. The resulting pressure–volume points can be fitted to a Birch–Murnaghan equation of state to extract the equilibrium volume, bulk modulus, and zero‑pressure lattice parameters. Any open‑source DFT code supporting PBE and periodic boundary conditions (e.g., Quantum ESPRESSO, GPAW) may be used.

## Reproduction target
Perform DFT calculations on the η‑Ta₂N₃ structure (provided as `/app/eta-Ta2N3.cif`, orthorhombic, space group Pbnm). Use the PBE functional, a plane‑wave cutoff that achieves convergence, and a k‑point spacing no larger than 0.03 Å⁻¹. Ensure forces are converged to 0.005 eV/Å and stress components to 0.005 GPa.

First, relax the cell and atomic positions at zero pressure. Then, at a series of at least five different volumes (or hydrostatic pressures) spanning roughly 0 to 30 GPa, compute the energy and stress tensor. For each point, derive the hydrostatic pressure (e.g., from the trace of the stress tensor), volume, and lattice parameters a, b, c. Write all results to a CSV file with columns `pressure_GPa`, `volume_A3`, `a_A`, `b_A`, `c_A`.

A hidden verifier will fit a 2nd‑order Birch–Murnaghan equation of state (B′ fixed to 4) to the pressure–volume data you provide, extract the bulk modulus and zero‑pressure lattice parameters, and compare them to hidden reference values.

## Assets

- η-Ta₂N₃ crystal structure (CIF)
- Open-source plane-wave DFT code: https://www.quantum-espresso.org/
- PBE pseudopotentials for Ta and N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT equation-of-state and pressure-volume data generation
- Role: scored (load-bearing)
- Action: Perform DFT geometry relaxation of the η-Ta₂N₃ structure (from /app/eta-Ta2N3.cif) at zero pressure using the PBE functional, a plane-wave cutoff energy meeting the convergence criteria, and a k-point spacing ≤ 0.03 Å⁻¹. After full relaxation, run static calculations at a series of cell volumes (or hydrostatic pressures) spanning 0 to 30 GPa (at least five data points), recording the total energy, stress tensor, and lattice vectors. For each point compute the derived hydrostatic pressure, volume, and lattice parameters a, b, c. Write all points to a CSV file.
- Output file: `/app/outputs/eta_Ta2N3_PV.csv`
- Format: csv
- Contract: Columns: pressure_GPa (float), volume_A3 (float), a_A (float), b_A (float), c_A (float). At least 5 rows covering pressures from approximately 0 to 30 GPa. The first row (lowest pressure) provides the zero-pressure lattice parameters.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eta_Ta2N3_PV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eta_Ta2N3_PV.csv
- path: `/app/outputs/eta_Ta2N3_PV.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Raw pressure-volume-lattice data points for η-Ta₂N₃ obtained from DFT calculations. The hidden checker will fit a 2nd-order Birch-Murnaghan equation of state (B′ fixed to 4) to these data, extract the bulk modulus and zero-pressure lattice parameters, and compare them to a hidden reference for scoring.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `volume_A3`, `a_A`, `b_A`, `c_A`
  - `units`:
    - `pressure_GPa`: GPa
    - `volume_A3`: Å³
    - `a_A`: Å
    - `b_A`: Å
    - `c_A`: Å

Notes: The agent must produce at least five data points covering a pressure range from roughly 0 to 30 GPa. The hidden checker will verify that volume decreases monotonically with pressure and that the CSV contains enough points before performing the EOS fit. No tolerances are given in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eta_Ta2N3_PV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "volume_A3",
          "a_A",
          "b_A",
          "c_A"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "volume_A3": "Å³",
          "a_A": "Å",
          "b_A": "Å",
          "c_A": "Å"
        }
      },
      "description": "Raw pressure-volume-lattice data points for η-Ta₂N₃ obtained from DFT calculations. The hidden checker will fit a 2nd-order Birch-Murnaghan equation of state (B′ fixed to 4) to these data, extract the bulk modulus and zero-pressure lattice parameters, and compare them to a hidden reference for scoring."
    }
  ],
  "notes": "The agent must produce at least five data points covering a pressure range from roughly 0 to 30 GPa. The hidden checker will verify that volume decreases monotonically with pressure and that the CSV contains enough points before performing the EOS fit. No tolerances are given in the public contract."
}
```

## How you are scored
Your solution will be scored by a hidden verifier that inspects the CSV file you produce.

First, the verifier confirms that the CSV contains at least five rows covering pressures from approximately 0 to 30 GPa and that the volume decreases monotonically with increasing pressure.

Next, it fits a 2nd‑order Birch–Murnaghan equation of state (B′ fixed to 4) to the pressure–volume data, recomputes the bulk modulus, and compares that value to a hidden reference. It also compares the zero‑pressure lattice parameters (from the first row of the CSV) to hidden reference lattice parameters. The bulk modulus match accounts for 80% of the total score, and the lattice parameter match for the remaining 20%.

The final reward is a weighted combination of these checks. Reporting a number without the corresponding data in the CSV is not sufficient; the verifier requires the raw pressure–volume points to recompute the quantities.
