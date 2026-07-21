# Spin-wave specific heat calculation for MnF2, FeF2, CoF2 and NiF2

## Problem background
The low-temperature specific heat of antiferromagnetic crystals contains a magnetic contribution from thermally excited spin waves (magnons). This work computes the spin-wave specific heat C<sub>M</sub>(T) of the rutile-structure antiferromagnets MnF<sub>2</sub>, FeF<sub>2</sub>, CoF<sub>2</sub>, and NiF<sub>2</sub>, using measured magnon dispersion relations and published exchange constants. The calculation provides a quantitative test of spin-wave theory and probes the accuracy of the dispersion relations in the 0–50 K range.

## Approach
The specific heat is obtained from the magnon density of states g(ν) via the integral

C<sub>M</sub>(T) = R ∫<sub>0</sub><sup>∞</sup> x<sup>2</sup> e<sup>x</sup> g(ν) / (e<sup>x</sup> − 1)<sup>2</sup> dν, with x = hν / k T.

First, the magnon dispersion ν(**k**) is evaluated on a dense mesh of wavevectors **k** inside the Brillouin zone for each material, using analytical formulas that depend on material-specific exchange constants and anisotropy fields. From these frequencies a histogram/density of states g(ν) is constructed. In a second step, the integral is evaluated numerically at every required temperature to yield C<sub>M</sub>(T).

**Dispersion formulas and material parameters to be hard‑coded:**

- For MnF<sub>2</sub> and FeF<sub>2</sub>:
  (ℏ ω(**k**))<sup>2</sup> = (E<sub>0</sub> + V<sub>1</sub>(**k**))<sup>2</sup> − V<sub>2</sub>(**k**)<sup>2</sup>,
  where
  V<sub>1</sub>(**k**) = 2 V<sub>1</sub> cos(c k<sub>z</sub>) + 2 V<sub>3</sub> (cos(a k<sub>x</sub>) + cos(a k<sub>y</sub>)),
  V<sub>2</sub>(**k**) = 8 V<sub>2</sub> cos(½ a k<sub>x</sub>) cos(½ a k<sub>y</sub>) cos(½ c k<sub>z</sub>),
  V<sub>1</sub> = −2 J<sub>1</sub> S, V<sub>2</sub> = +2 J<sub>2</sub> S, V<sub>3</sub> = −2 J<sub>3</sub> S, E<sub>0</sub> = g β H<sub>A</sub>.
  The wavevector components **k** = (k<sub>x</sub>, k<sub>y</sub>, k<sub>z</sub>) are in the reciprocal lattice basis,
  and a, c are the lattice constants of the tetragonal cell.
  - MnF<sub>2</sub>: J<sub>1</sub> = 0.236 cm<sup>−1</sup>, J<sub>2</sub> = 1.209 cm<sup>−1</sup>, J<sub>3</sub> = 0.034 cm<sup>−1</sup>, gβ H<sub>A</sub> = 0.730 cm<sup>−1</sup>, S = 5/2.
  - FeF<sub>2</sub>: J<sub>1</sub> = 0.024 cm<sup>−1</sup>, J<sub>2</sub> = 1.84 cm<sup>−1</sup>, J<sub>3</sub> = 0.097 cm<sup>−1</sup>, gβ H<sub>A</sub> = 19.93 cm<sup>−1</sup>, S = 2.

- For CoF<sub>2</sub> (only the lowest magnon branch):
  (ℏ ω(**k**))<sup>2</sup> = S { a(ξ<sub>z</sub>) b(ξ<sub>z</sub>) − c<sup>2</sup>(ξ) } ,
  with
  a(ξ<sub>z</sub>) = R p (R + T/S) + J<sub>1</sub>′ z<sub>1</sub> P<sup>2</sup> cos(2π ξ<sub>z</sub>),
  b(ξ<sub>z</sub>) = R p (R + T/S) + J<sub>1</sub>′ z<sub>1</sub> Q<sup>2</sup> cos(2π ξ<sub>z</sub>),
  c(ξ) = J<sub>2</sub>′ z<sub>2</sub> P Q cos(π ξ<sub>x</sub>) cos(π ξ<sub>y</sub>) cos(π ξ<sub>z</sub>),
  and ξ = (ξ<sub>x</sub>, ξ<sub>y</sub>, ξ<sub>z</sub>) are dimensionless wavevector components in units of the reciprocal lattice.
  p = z<sub>2</sub> J<sub>2</sub>′ − z<sub>1</sub> J<sub>1</sub>′; the integer coordination numbers are z<sub>1</sub> = 2, z<sub>2</sub> = 8.
  Parameters: P = 0.99, Q = 2.38, R = 1.42, T = 0.38, S = 1/2,
  J<sub>1</sub>′ = −0.617 cm<sup>−1</sup>, J<sub>2</sub>′ = 3.362 cm<sup>−1</sup>.

- For NiF<sub>2</sub>:
  ν<sub>±</sub>(**k**) = 125.0 [ ( 1.01569 − (1−γ<sub>2k</sub>) J<sub>2</sub>/62.2 − (1−γ<sub>3k</sub>) J<sub>3</sub>/31.1 )<sup>2</sup> − ( γ<sub>1k</sub> ± 0.01534 )<sup>2</sup> ]<sup>1/2</sup> ,
  where γ<sub>nk</sub> are the geometrical structure factors for the nth neighbour shell (as defined in the standard Moriya dispersion model for the rutile lattice),
  and J<sub>2</sub> = 3.952 cm<sup>−1</sup>, J<sub>3</sub> = 3.118 cm<sup>−1</sup>.  The remaining parameters entering the model (J<sub>1</sub>, canting angle, etc.) are those that reproduce the frequencies given in the literature; the exact numerical values of the γ factors follow from the lattice symmetry and can be looked up in standard references on the rutile antiferromagnet.

## Reproduction target
Compute the spin‑wave contribution to the specific heat, C<sub>M</sub>(T), in units of J K<sup>−1</sup> mole<sup>−1</sup> for all four materials at the temperatures listed below.  Write the results to the output CSV file with columns: Material (string), Temperature_K (float), C_M_J_per_K_per_mole (float).

The full set of temperatures is:
- NiF<sub>2</sub>: 0.36 K
- All materials: 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0, 35.0 K
- Additionally for MnF<sub>2</sub>, FeF<sub>2</sub>, NiF<sub>2</sub>: 40.0, 45.0, 50.0 K

Only the lowest magnon branch needs to be included (as in the original study).  The computed C<sub>M</sub> values should be derived from the numerical integration described in the workflow steps and must obey the monotonic increase with temperature that is expected from the physics.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute magnon density of states
- Role: process
- Action: For each material (MnF2, FeF2, CoF2, NiF2), evaluate the magnon dispersion relations on a dense mesh of wave vectors inside the Brillouin zone using the analytical formulas and the exchange parameters provided in the instruction, and construct the magnon density of states g(ν).
- Evidence: `/app/outputs/magnon_dos.npy`

### Step 2: Calculate spin‑wave specific heat
- Role: scored (load-bearing)
- Action: Using the density of states g(ν) from the previous step, evaluate the integral for the spin‑wave contribution C_M(T) for each material at every required temperature. Write the results to a CSV file.
- Output file: `/app/outputs/spin_wave_specific_heat.csv`
- Format: csv
- Contract: Columns: Material (string), Temperature_K (float), C_M_J_per_K_per_mole (float). Rows for: NiF2 at 0.36 K; all materials at 2.5, 5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0, 30.0, 35.0 K; additionally MnF2, FeF2, NiF2 at 40.0, 45.0, 50.0 K. Values as floats, scientific notation where appropriate.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spin_wave_specific_heat.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spin_wave_specific_heat.csv
- path: `/app/outputs/spin_wave_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spin‑wave specific heat C_M(T) for the four antiferromagnetic difluorides. The checker compares each (Material, Temperature) value against the hidden paper‑calculated gold with a relative‑error tolerance and verifies that C_M increases monotonically with temperature for each material.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Temperature_K`, `C_M_J_per_K_per_mole`
  - `units`:
    - `Temperature_K`: K
    - `C_M_J_per_K_per_mole`: J K^-1 mole^-1

Notes: Only the calculated C_M values are scored; the experimental column from the paper is not required. The agent may implement either the density‑of‑states integration method or the Houston interpolation method; the output format is identical. The exact temperature list must be followed (including 0.36 K for NiF2). Values must be in J K^-1 mole^-1.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spin_wave_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Temperature_K",
          "C_M_J_per_K_per_mole"
        ],
        "units": {
          "Temperature_K": "K",
          "C_M_J_per_K_per_mole": "J K^-1 mole^-1"
        }
      },
      "description": "Spin‑wave specific heat C_M(T) for the four antiferromagnetic difluorides. The checker compares each (Material, Temperature) value against the hidden paper‑calculated gold with a relative‑error tolerance and verifies that C_M increases monotonically with temperature for each material."
    }
  ],
  "notes": "Only the calculated C_M values are scored; the experimental column from the paper is not required. The agent may implement either the density‑of‑states integration method or the Houston interpolation method; the output format is identical. The exact temperature list must be followed (including 0.36 K for NiF2). Values must be in J K^-1 mole^-1."
}
```

## How you are scored
A hidden verifier reads your output CSV.  For each (Material, Temperature) entry it checks whether the reported C<sub>M</sub> value agrees with the expected correct value (obtained from a faithful numerical reproduction of the same model) within a tolerance that accounts for legitimate differences between implementations.  Additionally, for every material the verifier confirms that C<sub>M</sub> rises strictly monotonically with temperature.  The reward is the fraction of material–temperature points that satisfy both checks.  No points are awarded for simply reporting a number without having performed the genuine computation; the tolerance is set to reward correct computation, not guesswork.
