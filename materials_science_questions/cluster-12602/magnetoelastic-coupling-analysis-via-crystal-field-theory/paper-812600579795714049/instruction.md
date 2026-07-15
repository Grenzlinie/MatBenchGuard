# Compute third-order magnetic susceptibility from crystal-field theory

## Problem background
In cubic rare-earth intermetallic compounds, the magnetization in the paramagnetic regime is influenced not only by the crystal electric field (CEF) and Heisenberg exchange, but also by quadrupolar interactions—magnetoelastic coupling and quadrupolar exchange between the 4f ions. The usual first-order magnetic susceptibility χ_M^(1) is isotropic in the cubic phase and depends only on bilinear exchange, but the third-order susceptibility χ_M^(3), which characterizes the curvature of the magnetization curve, becomes anisotropic and receives a direct contribution from the induced quadrupolar moment. This makes χ_M^(3) a sensitive probe of both tetragonal (G₁) and trigonal (G₂) quadrupolar couplings. In this task you will compute χ_M^(1) and χ_M^(3) from first principles using the analytical mean-field expressions that follow from perturbation theory, for a given set of CEF parameters, bilinear exchange strength, and quadrupolar coefficients.

## Approach
The computation is based on the Lea–Leask–Wolf operator‑equivalent method for a total angular momentum J=6. First, construct the cubic CEF Hamiltonian in the |J,M_J⟩ basis using the parameters W and x, and diagonalize it to obtain the energy eigenvalues E_i and eigenvectors. In the same basis compute the matrix elements of J_z and of the tetragonal quadrupolar operator O_2^0 = 3J_z^2 − J(J+1).

Using the eigenvalues and these matrix elements, evaluate the four pure‑CEF susceptibilities as functions of temperature by summing over eigenstates according to the perturbation‑theory formulas that involve Boltzmann population factors, matrix‑element products, and energy denominators. These are χ₀^(1) (first‑order magnetic), χ₀^(3) (third‑order magnetic), χ₂ (strain), and χ₂^(2) (quadrupolar‑field). The formulas include terms with diagonal matrix elements that give Curie‑like −1/T contributions and off‑diagonal Van‑Vleck contributions that reflect the CEF level scheme.

For the [111] direction, rotate the coordinate system so that [111] becomes the new z‑axis, re‑diagonalize the CEF Hamiltonian in that rotated basis, and compute the corresponding primed susceptibilities χ₀^(3)′, χ₂′, and χ₂^(2)′.

The exchange‑enhanced susceptibilities are built from these CEF‑only quantities. The first‑order susceptibility is enhanced by the bilinear exchange parameter n (or equivalently the paramagnetic Curie temperature Θ^*): χ_M^(1) = χ₀^(1) / (1 − n χ₀^(1)). The total third‑order susceptibility for H∥[001] receives two contributions, both strengthened by bilinear exchange: the intrinsic CEF curvature χ₀^(3) and a quadrupolar term proportional to G₁ and (χ₂^(2))², with a denominator that also involves the strain susceptibility χ₂ and the same quadrupolar coefficient G₁. An analogous expression with G₂ and the primed susceptibilities gives χ_M^(3) for H∥[111].

You must implement this entire pipeline in code, carrying out the matrix diagonalizations, the temperature‑dependent sums, and the final closed‑form enhancement steps to produce numerical tables of the susceptibilities.

## Reproduction target
Produce two CSV files that report the total first‑order magnetic susceptibility χ_M^(1)(T) and the total third‑order magnetic susceptibility χ_M^(3)(T) for both the tetragonal ([001]) and trigonal ([111]) field directions. The computation must be performed for the physical parameters listed in the **Parameters** section below—which correspond to a typical rare‑earth intermetallic compound (Tm³⁺ ion, J=6)—over a temperature grid covering the paramagnetic range (e.g., 5 K to 100 K). The resulting tables are the only scored outputs: chi_M1.csv with columns T, chi_M1, and chi_M3.csv with columns T, chi_M3_001, chi_M3_111.

**Note on fitting:** The original paper also fitted the theoretically computed susceptibility curves to experimental magnetization data to extract the total quadrupolar coefficients G₁ and G₂.  However, that fitting step cannot be reproduced here because the raw magnetization measurements are not publicly available as numerical tables. The task therefore focuses on the forward computation of the susceptibilities from the physical parameters, which is the central analytical contribution of the work.

## Parameters

Use the following physical parameters to compute the susceptibilities:

- Bilinear exchange parameter Θ* = −3.0 K  (ferromagnetic coupling; n = Θ*/C where C = g_J² μ_B² J(J+1)/3)
- CEF parameters  W = 1.4 K,  x = −0.42 (Lea–Leask–Wolf notation)
- Tetragonal quadrupolar coefficient G₁ = 0.0103 K  (10.3 mK)
- Trigonal quadrupolar coefficient G₂ = −0.06 K  (−60 mK)

All susceptibilities are expressed in emu/mol (CGS). The temperature grid should be fine enough to resolve the behaviour of χ_M^(3) near its sign change (if any).

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Diagonalize cubic CEF Hamiltonian for J=6
- Role: process
- Action: Construct the cubic crystal-field Hamiltonian in the |J,M_J> basis using the Lea-Leask-Wolf operator equivalents with given parameters W and x for total angular momentum J=6. Diagonalize to obtain eigenvalues E_i and eigenvectors. Compute matrix elements of J_z and the tetragonal quadrupolar operator O_2^0 between all eigenstates. Save evidence of the diagonalization (energy levels and key matrix elements) as a JSON file.
- Evidence: `/app/outputs/cef_energies.json`

### Step 2: Compute CEF-only susceptibilities
- Role: process
- Action: Using the eigenvalues, eigenvectors, and matrix elements from Step 1, evaluate the four pure CEF susceptibilities χ0^(1), χ0^(3), χ2, χ2^(2) as functions of temperature according to the perturbation-theory formulas (Appendix A of the paper). Perform analogous computations for the [111] direction by rotating to the trigonal coordinate system and rediagonalizing the CEF Hamiltonian in the new basis, yielding χ0^(3)' and χ2', χ2^(2)' as described in Appendix B. Save the temperature-dependent arrays as a numpy archive.
- Evidence: `/app/outputs/cef_susceptibilities.npz`

### Step 3: Total first-order magnetic susceptibility
- Role: scored
- Action: From the CEF-only χ0^(1)(T) and the bilinear exchange parameter n (or Θ*), compute the exchange-enhanced first-order magnetic susceptibility χ_M^(1)(T) using the appropriate analytical expression. Output a CSV file with columns T and chi_M1.
- Output file: `/app/outputs/chi_M1.csv`
- Format: csv
- Contract: Columns: T (float, Kelvin), chi_M1 (float, susceptibility units). Header line expected.
- Scoring: scored by hidden verifier

### Step 4: Total third-order magnetic susceptibility
- Role: scored (load-bearing)
- Action: From the CEF-only susceptibilities and the parameters n, G1, G2, compute the total third-order magnetic susceptibility χ_M^(3)(T) for the [001] and [111] directions using the analytical expressions. Output a CSV file with columns T, chi_M3_001, chi_M3_111.
- Output file: `/app/outputs/chi_M3.csv`
- Format: csv
- Contract: Columns: T (float, Kelvin), chi_M3_001 (float, H||[001]), chi_M3_111 (float, H||[111]). Header line expected.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi_M1.csv`
- `/app/outputs/chi_M3.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi_M1.csv
- path: `/app/outputs/chi_M1.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total first-order magnetic susceptibility χ_M^(1) as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `chi_M1`
  - `units`:
    - `T`: Kelvin
    - `chi_M1`: emu/mol

### chi_M3.csv
- path: `/app/outputs/chi_M3.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total third-order magnetic susceptibility χ_M^(3) for [001] and [111] directions as a function of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `chi_M3_001`, `chi_M3_111`
  - `units`:
    - `T`: Kelvin
    - `chi_M3_001`: emu/mol
    - `chi_M3_111`: emu/mol

Notes: The task computes theoretical susceptibilities for a prescribed set of physical parameters (W, x, Θ*, G1, G2) over a user-defined temperature grid. The fitting to experimental magnetization data is excluded because the original experimental data are not publicly available.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi_M1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "chi_M1"
        ],
        "units": {
          "T": "Kelvin",
          "chi_M1": "emu/mol"
        }
      },
      "description": "Total first-order magnetic susceptibility χ_M^(1) as a function of temperature."
    },
    {
      "file": "chi_M3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "chi_M3_001",
          "chi_M3_111"
        ],
        "units": {
          "T": "Kelvin",
          "chi_M3_001": "emu/mol",
          "chi_M3_111": "emu/mol"
        }
      },
      "description": "Total third-order magnetic susceptibility χ_M^(3) for [001] and [111] directions as a function of temperature."
    }
  ],
  "notes": "The task computes theoretical susceptibilities for a prescribed set of physical parameters (W, x, Θ*, G1, G2) over a user-defined temperature grid. The fitting to experimental magnetization data is excluded because the original experimental data are not publicly available."
}
```

## How you are scored
A hidden verifier will score your submission independently. For each of the scored workflow steps (total first‑order and total third‑order susceptibility files) it will read your CSV tables and compare the susceptibility values against a reference computation that uses the same theoretical framework but with hidden parameter sets and hidden temperature evaluation points. The reward is the weighted sum of the scores from these two steps, with the third‑order susceptibility carrying the larger weight because of its central role. For a directional metric like susceptibility, the comparison rewards values that meet or exceed a quality threshold rather than penalizing small implementation‑dependent differences; the exact thresholds are hidden. Simply reporting a number from the literature is insufficient—the verifier checks the shape and temperature dependence of the computed curves, so you must genuinely execute the diagonalization and susceptibility evaluation pipeline.
