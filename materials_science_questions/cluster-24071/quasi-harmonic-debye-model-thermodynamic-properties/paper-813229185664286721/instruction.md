# Computation of ζ and B₀″ from quantum-statistical model and modified Vinet equation

## Problem background
Equations of state (EOS) relate a solid’s volume to the applied pressure and are essential for understanding material behavior from low to ultra-high pressures. This reproduction task focuses on a new EOS that extends the Vinet form with a quantum‑statistical model (QSM) correction. The task is to compute, for four monatomic solids (Ne, Ar, Al, Cu), the material‑dependent parameter ζ and the second pressure derivative of the bulk modulus B₀″ by matching the new EOS to the QSM reference pressure at a fixed compression. The required zero‑pressure parameters V₀ (volume), B₀ (bulk modulus), B₀′ (pressure derivative of the bulk modulus), and atomic number Z are taken from published theoretical calculations and are given in the table below.

| Solid | V₀ (au³) | B₀ (GPa) | B₀′ | Z |
|-------|----------|----------|-----|---|
| Ne | 102.128 | 6.36 | 7.61 | 10 |
| Ar | 210.517 | 6.28 | 7.07 | 18 |
| Al | 109.600 | 72.6 | 4.85 | 13 |
| Cu | 78.137 | 135 | 5.93 | 29 |

These parameters define the starting point of the computation; no external dataset download is needed.

## Approach
The computation combines two components: a quantum‑statistical model (QSM) that provides an ab‑initio reference pressure for a monatomic solid, and a modified Vinet equation of state that contains an unknown dimensionless parameter ζ.

**Quantum‑statistical model pressure.** For a monatomic solid of atomic number Z, the electron density in the QSM is approximated by

ρ(r) = (Z / V) · exp(−α r − β r²)

with the atomic radius r = (3V/(4π))^{1/3}, volume V, and

α = 0.1935 · Z^{0.495 − 0.039 log₁₀(Z)}
β = 0.068 + [0.078 − 0.086 log₁₀(Z)] · log₁₀(Z).

The pressure follows from

P_QSM = (1/5)(3π²)^{2/3} ρ^{5/3} − (13/36)(3/π)^{1/3} ρ^{4/3},

where all quantities are in atomic units.

**Modified Vinet equation (new EOS).** The proposed equation generalizes the Vinet form to ultra‑high pressures and is given by

P(x) = 3 B₀ · x^{−5} · (1 − x) · exp{ (η − 3)(1 − x) + (ζ − 3/2)(1 − x)² }

where x = (V/V₀)^{1/3} and η = (3/2)(B₀′ − 1). The parameter ζ is material‑dependent and is the main unknown.

**Determining ζ.** The QSM is evaluated at the compression x = 0.20 (i.e. V/V₀ = 0.008) using the supplied V₀ and Z, yielding a reference pressure P_ref. The value of ζ is then obtained by numerically solving for the ζ that makes the new EOS produce the same pressure at x = 0.20, i.e. P(x=0.20; ζ) = P_ref.

**Computing B₀″.** Once ζ is known, the second pressure derivative of the bulk modulus is calculated analytically from

B₀″ = −( η² + 6 η − 6 ζ + 2 ) / (9 B₀).

No other data or baselines are required; the comparison is between the QSM‑fitted EOS and the derived values.

## Reproduction target
Using the input parameters for Ne, Ar, Al, and Cu, implement the QSM pressure model and the modified Vinet equation. For each solid, compute ζ by matching the QSM pressure at x = 0.20 as described, then calculate B₀″. Output a CSV table with one row per solid listing the solid name, the computed ζ, and the computed B₀″. The hidden verifier will compare your computed values against established reference results for these quantities.

## Assets

- Input parameters for monatomic solids (V₀, B₀, B₀′, Z)

## Workflow steps

### Step 1: Compute ζ and B₀″ for monatomic solids
- Role: scored (load-bearing)
- Action: Implement the quantum-statistical model pressure formula from the Kalitkin–Kuz'mina model (electron density and pressure) and the proposed equation of state (the modified Vinet form with QSM correction). For each solid (Ne, Ar, Al, Cu), use the supplied zero-pressure parameters and atomic number to compute the QSM pressure at x = 0.20, then numerically determine ζ such that the new EOS yields the same pressure at that compression. Compute the second pressure derivative of the bulk modulus B₀″ = −(η² + 6η − 6ζ + 2) / (9 B₀) with η = (3/2)(B₀′ − 1). Write a CSV table with columns Solid, zeta_computed, B0pp_computed; one row per solid.
- Output file: `/app/outputs/zeta_B0pp_table.csv`
- Format: csv
- Contract: Header: Solid, zeta_computed, B0pp_computed. Each row contains the solid name (Ne, Ar, Al, Cu) and the corresponding numeric values in decimal or scientific notation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zeta_B0pp_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zeta_B0pp_table.csv
- path: `/app/outputs/zeta_B0pp_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The computed ζ parameter and second pressure derivative of the bulk modulus for Ne, Ar, Al, Cu, obtained by matching the new EOS to the QSM pressure at x=0.20.
- schema:
  - `type`: table
  - `required_columns`: `Solid`, `zeta_computed`, `B0pp_computed`
  - `units`:
    - `zeta_computed`: dimensionless
    - `B0pp_computed`: GPa⁻¹

Notes: The hidden checker compares the computed values to the paper's reported ones with appropriate absolute tolerances. All four solids must pass both checks for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zeta_B0pp_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Solid",
          "zeta_computed",
          "B0pp_computed"
        ],
        "units": {
          "zeta_computed": "dimensionless",
          "B0pp_computed": "GPa⁻¹"
        }
      },
      "description": "The computed ζ parameter and second pressure derivative of the bulk modulus for Ne, Ar, Al, Cu, obtained by matching the new EOS to the QSM pressure at x=0.20."
    }
  ],
  "notes": "The hidden checker compares the computed values to the paper's reported ones with appropriate absolute tolerances. All four solids must pass both checks for full credit."
}
```

## How you are scored
A hidden verifier inspects your `/app/outputs/zeta_B0pp_table.csv`. It extracts the computed ζ and B₀″ for each solid and compares them to hidden reference values using pre‑set absolute tolerances. The reward is the fraction of solids for which both ζ and B₀″ lie within the required tolerance. Only producing the correct CSV file with the right format and values that match the hidden references within tolerance earns full credit. The tolerances are not disclosed, so your implementation must faithfully follow the specified method to achieve the needed accuracy.
