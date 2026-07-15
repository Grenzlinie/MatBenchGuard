# DFT Bulk Modulus of Silicon and Germanium Fullerenes

## Problem background
The elastic properties of nanoscale fullerene‑like structures of silicon and germanium are of fundamental interest. In particular, the bulk modulus — a measure of resistance to uniform compression — of Si60 and Ge60 fullerenes of different symmetries has been predicted theoretically but is not known experimentally. This task aims to compute from first principles the bulk moduli of Si60 and Ge60 in three symmetry groups: Ih (icosahedral), C2h, and C1 (lowest symmetry), and to compare them with the bulk moduli of crystalline Si and Ge in the diamond structure, thereby examining the influence of symmetry and geometry on mechanical stiffness.

## Approach
Use density functional theory (DFT) calculations with Quantum ESPRESSO and projector augmented‑wave (PAW) pseudopotentials. Two exchange‑correlation functionals are employed: the local density approximation (LDA) and the generalized gradient approximation (GGA‑PBE). For each fullerene system and for bulk Si/Ge, perform full geometry optimization until forces converge. Initial atomic geometries are obtained as follows: the Ih structure by isotropically scaling the C60 truncated icosahedron according to bond‑length ratios; the C2h structure from literature coordinates; the C1 structure by relaxing the Ih starting point without symmetry constraints. Fullerene volume is determined numerically using a Monte Carlo convex‑hull integration program with high sampling statistics. Once the equilibrium geometry is found, carry out a set of single‑point energy calculations at 5–7 isotropically scaled volumes around equilibrium. Fit the total energy versus volume data to a quadratic polynomial; the bulk modulus is extracted from the curvature at the minimum. Record all energy‑volume pairs in a CSV file for downstream verification.

## Reproduction target
Compute the bulk modulus (in GPa) for each of the following material/symmetry/exchange‑correlation functional combinations from a set of DFT total‑energy‑versus‑volume data points:

- Si60 (Ih, C2h, C1) with LDA and GGA‑PBE
- Bulk Si (diamond) with LDA and GGA‑PBE
- Ge60 (Ih: LDA only; C2h and C1: LDA and GGA‑PBE)
- Bulk Ge (diamond) with LDA and GGA‑PBE

The bulk modulus for each combination must be derived by fitting a quadratic polynomial E(V) to the corresponding rows in `e_v_data.csv`. The CSV file must contain columns `material`, `symmetry`, `xc`, `volume_ang3`, and `total_energy_eV`, with all 5–7 volume points per combination. The verifier will perform the quadratic fits and compute the bulk moduli; the raw CSV is the primary scored artifact.

## Assets

- Quantum ESPRESSO (version ≥7.0): https://www.quantum-espresso.org/
- PAW pseudopotentials for Si and Ge (LDA and GGA-PBE): https://www.quantum-espresso.org/pseudopotentials
- C60 icosahedral coordinates (truncated icosahedron): http://www.ccl.net/chemistry/resources/data/fullerenes/index.shtml
- Si60 C2h initial geometry (from Li et al., Phys. Rev. B 61, 1685): 10.1103/PhysRevB.61.1685
- numpy, scipy: numpy scipy

## Workflow steps

### Step 1: Monte Carlo convex polyhedron volume program
- Role: process
- Action: Implement a Python script that reads atomic positions (XYZ format) and computes the volume of the convex hull via Monte Carlo integration with 10^7 points, averaging over 100 runs to achieve <0.01% error.
- Evidence: `/app/outputs/volume_test.log`

### Step 2: DFT energy-volume calculations
- Role: scored (load-bearing)
- Action: Using Quantum ESPRESSO with PAW pseudopotentials (LDA and GGA-PBE), perform geometry optimizations for bulk Si, bulk Ge, and for the fullerene structures Si60(Ih), Si60(C2h), Si60(C1), Ge60(Ih), Ge60(C2h), Ge60(C1). For each optimized structure, compute total energies at 5-7 different volumes around equilibrium by isotropically scaling the simulation box, employing the Monte Carlo volume program to compute the molecular volume. Record all (material, symmetry, xc, volume_ang3, total_energy_eV) rows in e_v_data.csv.
- Output file: `/app/outputs/e_v_data.csv`
- Format: csv
- Contract: CSV with header material,symmetry,xc,volume_ang3,total_energy_eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/e_v_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### e_v_data.csv
- path: `/app/outputs/e_v_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw total energy vs volume data for bulk modulus recomputation. The checker will fit E(V) quadratic, compute bulk modulus, and compare against hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `material`, `symmetry`, `xc`, `volume_ang3`, `total_energy_eV`
  - `units`:
    - `volume_ang3`: Angstrom^3
    - `total_energy_eV`: eV

Notes: The hidden checker will group data by (material, symmetry, xc), fit a quadratic E(V) for each group, compute bulk modulus B = V0 * 2c, and compare the computed moduli against reference values and verify monotonic ordering of moduli by symmetry.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "e_v_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "symmetry",
          "xc",
          "volume_ang3",
          "total_energy_eV"
        ],
        "units": {
          "volume_ang3": "Angstrom^3",
          "total_energy_eV": "eV"
        }
      },
      "description": "Raw total energy vs volume data for bulk modulus recomputation. The checker will fit E(V) quadratic, compute bulk modulus, and compare against hidden reference values."
    }
  ],
  "notes": "The hidden checker will group data by (material, symmetry, xc), fit a quadratic E(V) for each group, compute bulk modulus B = V0 * 2c, and compare the computed moduli against reference values and verify monotonic ordering of moduli by symmetry."
}
```

## How you are scored
A hidden verifier reads `e_v_data.csv` and independently performs the following for each (material, symmetry, xc) group present in the file:

1. Fits the total energy vs. volume data to a quadratic polynomial E(V) = a + b·V + c·V².
2. Determines the equilibrium volume V₀ = −b/(2c) and the bulk modulus B = V₀ · 2c.

Each computed bulk modulus is compared against reference values. Additionally, the verifier checks whether the moduli obey the expected monotonic trend with respect to symmetry. The final reward is a weighted combination of the fraction of bulk moduli that fall within acceptable tolerance and the correctness of the observed ordering. Providing the raw volume‑energy CSV is required; self‑reported bulk moduli alone will not be accepted.
