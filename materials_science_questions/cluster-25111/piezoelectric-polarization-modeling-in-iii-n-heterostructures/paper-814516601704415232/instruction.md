# Strain-modulated heterojunction electron gas density in III-N heterostructures via self-consistent Schrödinger-Poisson simulation

## Problem background
AlGaN/AlN/GaN heterostructures support a high-density two-dimensional electron gas (heterojunction electron gas, HEG) formed by strong intrinsic spontaneous and piezoelectric polarisation fields. Modulating the HEG sheet density is of great interest for high-electron-mobility transistors and piezotronic devices. Applied mechanical strain along the nonpolar a‑axis alters the piezoelectric polarisation charges at the heterojunction interfaces, thereby modifying the conduction-band profile and the resulting HEG density. Understanding how the HEG sheet density varies with external a‑axis strain enables strain-controlled carrier-density engineering.

## Approach
The approach consists of two stages. First, an analytical polarisation model computes the fixed polarisation charge densities at the AlGaN/AlN and AlN/GaN interfaces as a function of a‑axis strain. The model includes spontaneous polarisation, lattice‑mismatch‑induced piezoelectric polarisation, and strain‑induced piezoelectric polarisation using standard wurtzite III‑nitride material constants. This yields the effective net fixed polarisation charge density σ_int at the heterojunction for each strain value. Second, a one‑dimensional self‑consistent Schrödinger–Poisson solver is implemented along the c‑axis (growth direction) for the heterostructure stack (Al₀.₃Ga₀.₇N 40 nm / AlN 1.6 nm / thick GaN, with the AlGaN surface and GaN backside as boundaries). The solver uses the effective‑mass approximation, includes conduction‑band offset, Hartree and exchange‑correlation potentials, and iteratively solves Poisson’s equation and the single‑band Schrödinger equation until self‑consistency. The electron density distribution n(z) is obtained, and the HEG sheet density is extracted by integrating n(z) over the quantum well. The computation is repeated for several externally applied a‑axis strain values spanning both compressive and tensile regimes.

## Reproduction target
The primary goal is to produce a CSV file `/app/outputs/heg_sheet_density.csv` that reports the computed HEG sheet density (cm⁻²) at the specified a‑axis strain values (in percent). The file must contain two columns: `strain_percent` (negative for compressive, positive for tensile) and `sheet_density_cm2`. The agent must include at least the strain values −1.78, −0.89, 0.0, 0.89, and 1.78, as imposed by the output contract. Use the self‑consistent Schrödinger–Poisson model described above to compute each sheet density.

## Assets

- numpy: numpy
- scipy: scipy

## Material parameters

The following parameters define the wurtzite III-nitride material properties and the heterostructure configuration. Use these values directly in the analytical polarization model (Step 1) and the Schrödinger–Poisson solver (Step 2).

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Spontaneous polarisation (GaN) | Psp,GaN | −0.029 | C m⁻² |
| Spontaneous polarisation (AlN) | Psp,AlN | −0.081 | C m⁻² |
| Spontaneous polarisation (Al0.3Ga0.7N) | Psp,AlGaN | −0.0446 | C m⁻² |
| Piezoelectric coefficient e33 (GaN) | e33,GaN | 0.73 | C m⁻² |
| Piezoelectric coefficient e31 (GaN) | e31,GaN | −0.49 | C m⁻² |
| Piezoelectric coefficient e33 (AlN) | e33,AlN | 1.46 | C m⁻² |
| Piezoelectric coefficient e31 (AlN) | e31,AlN | −0.60 | C m⁻² |
| Elastic constant C13 (GaN) | C13,GaN | 103 | GPa |
| Elastic constant C33 (GaN) | C33,GaN | 405 | GPa |
| Elastic constant C13 (AlN) | C13,AlN | 108 | GPa |
| Elastic constant C33 (AlN) | C33,AlN | 373 | GPa |
| Lattice constant a (GaN) | aGaN | 3.189 | Å |
| Lattice constant a (AlN) | aAlN | 3.112 | Å |
| Lattice constant a (Al0.3Ga0.7N) | aAlGaN | 3.166 | Å (linear interpolation) |
| Band-gap (GaN) | Eg,GaN | 3.42 | eV |
| Band-gap (AlN) | Eg,AlN | 6.2 | eV |
| Conduction-band offset fraction | ΔEc/ΔEg | 0.75 | – |
| Dielectric constant (low-frequency, GaN) | εGaN | 8.9 | ε0 |
| Dielectric constant (low-frequency, AlN) | εAlN | 8.5 | ε0 |
| Donor ionisation energy (AlGaN) | ED | 0.2 | eV below Ec |
| Donor concentration in AlGaN | ND | 1 × 10¹⁸ | cm⁻³ |
| Potential at AlGaN top surface | Vtop | 1.46 | eV (initial guess for surface barrier) |
| Electron effective mass (GaN) | m*GaN | 0.22 | m0 |
| Electron effective mass (Al0.3Ga0.7N) | m*AlGaN | 0.242 | m0 |
| Temperature | T | 300 | K |

The analytical polarisation model for net fixed charge at the heterojunction:
σ_int = (Psp,AlGaN + Plm,AlGaN + Ppz,AlGaN) – Psp,GaN.
Lattice‑mismatch piezoelectric polarisation (Plm) for AlGaN grown on relaxed GaN:
Plm = 2 (e31 – e33 C13/C33) (aGaN – aAlGaN)/aAlGaN, using AlGaN material constants.
Strain‑induced piezoelectric polarisation (Ppz) under external a‑axis strain εa:
εxx = εa, εyy = 0, εzz = –(C13/C33) εxx.
Ppz = e33 εzz + e31 (εxx + εyy).
All AlGaN parameters (piezoelectric, elastic, lattice constant, dielectric, effective mass) are obtained by linear interpolation between GaN and AlN using x = 0.3.

## Workflow steps

### Step 1: Compute polarization charge densities
- Role: process
- Action: Calculate the fixed polarization charge densities at the AlGaN/AlN and AlN/GaN interfaces as a function of a-axis strain using an analytical polarization model. Include spontaneous polarization, lattice-mismatch-induced piezoelectric polarization, and strain-induced piezoelectric polarization from wurtzite III-nitride constants. Compute the effective net fixed polarization charge density for a range of strains (e.g., -1.78% to 1.78%).
- Evidence: `/app/outputs/polarization_charges.csv`

### Step 2: Solve Schrödinger–Poisson and extract HEG sheet density
- Role: scored (load-bearing)
- Action: Implement a 1D self-consistent Schrödinger‑Poisson solver for the AlGaN/AlN/GaN heterostructure along the c-axis using the effective mass approximation, incorporating the strain-dependent polarization charge density from the previous step. Solve Poisson and Schrödinger equations iteratively to obtain electron density n(z). Integrate over the quantum well to compute HEG sheet density for at least five strain values (e.g., -1.78%, -0.89%, 0%, 0.89%, 1.78%). Write the strain and sheet density results to a CSV file.
- Output file: `/app/outputs/heg_sheet_density.csv`
- Format: csv
- Contract: CSV with two columns: 'strain_percent' (float, e.g. -1.78, -0.89, 0.0, 0.89, 1.78) and 'sheet_density_cm2' (float, sheet density in cm⁻²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heg_sheet_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heg_sheet_density.csv
- path: `/app/outputs/heg_sheet_density.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with two columns: strain_percent (external a‑axis strain in percent, negative for compressive, positive for tensile) and sheet_density_cm2 (computed HEG sheet density in cm⁻²). The agent must include rows for at least the strain values -1.78, -0.89, 0.0, 0.89, 1.78. The checker will verify that the reported sheet density values are physically reasonable and follow the expected monotonic trend: sheet density must not increase as tensile strain increases (from 0 to positive strain) and must not decrease as compressive strain magnitude increases (from 0 to negative strain).
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `sheet_density_cm2`
  - `units`:
    - `strain_percent`: percent
    - `sheet_density_cm2`: cm⁻²

Notes: The checker additionally enforces a monotonicity requirement on the strain–density relationship; failure of this trend results in zero credit for this artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heg_sheet_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "sheet_density_cm2"
        ],
        "units": {
          "strain_percent": "percent",
          "sheet_density_cm2": "cm⁻²"
        }
      },
      "description": "CSV file with two columns: strain_percent (external a‑axis strain in percent, negative for compressive, positive for tensile) and sheet_density_cm2 (computed HEG sheet density in cm⁻²). The agent must include rows for at least the strain values -1.78, -0.89, 0.0, 0.89, 1.78. The checker will verify that the reported sheet density values are physically reasonable and follow the expected monotonic trend: sheet density must not increase as tensile strain increases (from 0 to positive strain) and must not decrease as compressive strain magnitude increases (from 0 to negative strain)."
    }
  ],
  "notes": "The checker additionally enforces a monotonicity requirement on the strain–density relationship; failure of this trend results in zero credit for this artifact."
}
```

## How you are scored
A hidden automatic verifier evaluates your submission. It checks that the output CSV is present, correctly formatted, and contains the required columns. The verifier compares your reported sheet density values against hidden reference values derived from the underlying physics, and it additionally verifies that the strain–density relationship satisfies physical plausibility constraints (e.g., monotonicity requirements). The final overall reward is a weighted combination of the per‑artifact scores.
