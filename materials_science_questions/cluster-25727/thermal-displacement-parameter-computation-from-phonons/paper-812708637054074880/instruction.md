# Temperature-dependent band gap of PbTe and SnTe from empirical pseudopotential method with Debye-Waller factors

## Problem background
PbTe and SnTe are narrow-gap IV-VI semiconductors with the rock-salt structure. The temperature dependence of their fundamental direct gaps at the L point of the Brillouin zone is unusual: in PbTe the gap increases with temperature, contrary to the negative coefficient observed in most semiconductors, while SnTe exhibits a sign reversal near the minimum gap. A reliable finite-temperature band-structure procedure is needed to understand these effects and to test whether the empirical pseudopotential method (EPM) can capture such temperature trends. The original work performed an EPM calculation that incorporates both lattice expansion and Debye-Waller factors to compute the gap as a function of temperature, and your task is to reproduce that computational study for both materials.

## Approach
The empirical pseudopotential method models the crystal potential as the sum of atomic pseudopotentials multiplied by structure factors. At finite temperature, two principal corrections must be applied: (i) lattice expansion, which changes the lattice constant a(T) and thereby rescales the form factors and kinetic energy terms; (ii) Debye-Waller damping, which modifies the structure factors by a factor exp(-G²⟨δRα²⟩_av/2) for each atomic species, using the mean-squared ionic displacements. Starting from a set of zero-temperature symmetric and antisymmetric form factors that reproduce the band structure, the finite-temperature pseudopotentials are constructed by: (a) cubically interpolating the zero-temperature form factors in q = |G| (in units of 2π/a) to obtain values at the G-vectors required at each temperature, (b) scaling each form factor by a³(0)/a³(T), and (c) applying the Debye-Waller factors. The resulting form factors are used to assemble the Hamiltonian matrix at the L point of the Brillouin zone. Diagonalizing this matrix yields the conduction- and valence-band energies at L, from which the direct gap is computed. This procedure is carried out for both PbTe and SnTe at five temperatures: 0, 100, 200, 300, and 400 K.

## Reproduction target
Compute the direct energy gap at the L point of the Brillouin zone for PbTe and for SnTe at the temperatures 0, 100, 200, 300, and 400 K, using the described finite-temperature empirical pseudopotential method. You must output two CSV files, one per material, each with columns `temperature_K` (integer) and `gap_L_eV` (float). The gap must be obtained from a proper implementation of the pseudopotential construction (interpolation, volume scaling, Debye-Waller damping) and Hamiltonian diagonalization at L; simply reporting reference numbers is not sufficient.

## Assets
The following inputs are extracted from the original work and are provided inline. No external file downloads are required.

**Lattice constants a(T) (Å) for PbTe and SnTe**

| Temperature (K) | SnTe a(T) (Å) | PbTe a(T) (Å) |
|-----------------|----------------|----------------|
| 0               | 6.3130         | 6.454          |
| 20              | 6.3134         | 6.4543         |
| 40              | 6.3145         | 6.4556         |
| 80              | 6.3184         | 6.4595         |
| 100             | 6.3207         | 6.4624         |
| 140             | 6.3253         | 6.4675         |
| 200             | 6.3328         | 6.4751         |
| 240             | 6.3380         | 6.4802         |
| 300             | 6.3458         | 6.4879         |
| 340             | 6.3510         | 6.4929         |
| 400             | 6.3588         | 6.5006         |

**Mean‑squared ionic displacements ⟨δRα²⟩_av (Å²) for PbTe and SnTe**

| Temperature (K) | Pb in PbTe | Te in PbTe | Sn in SnTe | Te in SnTe |
|-----------------|------------|------------|------------|------------|
| 0               | 0          | 0          | 0          | 0          |
| 20              | 0.0006     | 0.0002     | –          | –          |
| 40              | 0.002      | 0.008      | 0.008      | 0.007      |
| 80              | –          | –          | 0.0026     | 0.0021     |
| 100             | 0.007      | 0.0036     | 0.0036     | 0.0030     |
| 140             | 0.0105     | 0.0056     | –          | –          |
| 200             | 0.0157     | 0.0086     | 0.0089     | 0.0072     |
| 240             | 0.0192     | 0.0107     | –          | –          |
| 300             | 0.0244     | 0.0138     | 0.0142     | 0.0116     |
| 340             | 0.0279     | 0.0159     | –          | –          |
| 400             | 0.0332     | 0.0189     | 0.0196     | 0.0160     |

For intermediate temperatures not listed, you may linearly interpolate (e.g., to obtain values at 100 K when missing, you may interpolate between 80 and 140 K if necessary; the tables provide sufficient coverage).

**Zero‑temperature pseudopotential form factors (in Ry)**

The symmetric and antisymmetric form factors are:

- V^S(G²=4) = −0.241
- V^S(G²=8) = −0.0352
- V^S(G²=12) = 0.017
- V^A(G²=3) = 0.052
- V^A(G²=11) = 0.021

For interpolation, assume that V^S(16) = 0 and V^A(16) = 0.

When constructing the finite‑temperature potential, you will also need V^S at G²=3,11 and V^A at G²=4,8,12; obtain these by the cubic interpolation scheme described in the approach.

## Workflow steps

### Step 1: Prepare temperature-dependent pseudopotentials
- Role: process
- Action: Using the zero-temperature symmetric and antisymmetric form factors V^S(G^2=4,8,12) and V^A(G^2=3,11) (in Ry), the experimental lattice constants a(T) from Table I for PbTe and SnTe, and the mean-squared ionic displacements from Table II for both compounds, construct temperature-dependent pseudopotential form factors for each temperature of interest (0, 100, 200, 300, 400 K). This involves: (a) cubic interpolation of the zero-temperature form factors to obtain V^S and V^A at the G^2 values required at each T, (b) scaling each form factor by a^3(0)/a^3(T) to account for lattice expansion, (c) modifying the structure factors with Debye-Waller factors exp(-G^2<δR_α^2>_av/2) for each atomic species. The result is the full set of temperature-dependent form factors needed for the Hamiltonian at the L point.
- Evidence: `/app/outputs/pseudopotential_preparation.log`

### Step 2: Compute PbTe L-point gap vs temperature
- Role: scored (load-bearing)
- Action: For PbTe, using the temperature-dependent pseudopotential form factors, construct the empirical pseudopotential Hamiltonian at the L point of the Brillouin zone for each temperature (0, 100, 200, 300, 400 K). Diagonalize the secular equation, identify the conduction band minimum and valence band maximum at L, and compute the direct energy gap E_g. Write the results to a CSV file.
- Output file: `/app/outputs/pbte_gap_vs_t.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (integer), gap_L_eV (float). Values at 0, 100, 200, 300, 400 K.
- Scoring: scored by hidden verifier

### Step 3: Compute SnTe L-point gap vs temperature
- Role: scored (load-bearing)
- Action: For SnTe, using the temperature-dependent pseudopotential form factors, construct the empirical pseudopotential Hamiltonian at the L point of the Brillouin zone for each temperature (0, 100, 200, 300, 400 K). Diagonalize the secular equation, identify the conduction band minimum and valence band maximum at L, and compute the direct energy gap E_g. Write the results to a CSV file.
- Output file: `/app/outputs/snte_gap_vs_t.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (integer), gap_L_eV (float). Values at 0, 100, 200, 300, 400 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pbte_gap_vs_t.csv`
- `/app/outputs/snte_gap_vs_t.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pbte_gap_vs_t.csv
- path: `/app/outputs/pbte_gap_vs_t.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct energy gap at L point of PbTe for temperatures 0, 100, 200, 300, 400 K. Compared to the paper's reported gaps with tolerance, and the linear coefficient over 100-300 K is also checked.
- schema:
  - `required_columns`: `temperature_K`, `gap_L_eV`
  - `units`:
    - `temperature_K`: K
    - `gap_L_eV`: eV

### snte_gap_vs_t.csv
- path: `/app/outputs/snte_gap_vs_t.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direct energy gap at L point of SnTe for temperatures 0, 100, 200, 300, 400 K. Compared to the paper's reported gaps with tolerance, and the linear coefficient over 100-300 K is also checked.
- schema:
  - `required_columns`: `temperature_K`, `gap_L_eV`
  - `units`:
    - `temperature_K`: K
    - `gap_L_eV`: eV

Notes: The checker compares the agent's computed gaps to the paper's reference values; it also extracts the linear temperature coefficient between 100 K and 300 K and compares to the paper's reported coefficients. All reference values are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pbte_gap_vs_t.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "temperature_K",
          "gap_L_eV"
        ],
        "units": {
          "temperature_K": "K",
          "gap_L_eV": "eV"
        }
      },
      "description": "Direct energy gap at L point of PbTe for temperatures 0, 100, 200, 300, 400 K. Compared to the paper's reported gaps with tolerance, and the linear coefficient over 100-300 K is also checked."
    },
    {
      "file": "snte_gap_vs_t.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "temperature_K",
          "gap_L_eV"
        ],
        "units": {
          "temperature_K": "K",
          "gap_L_eV": "eV"
        }
      },
      "description": "Direct energy gap at L point of SnTe for temperatures 0, 100, 200, 300, 400 K. Compared to the paper's reported gaps with tolerance, and the linear coefficient over 100-300 K is also checked."
    }
  ],
  "notes": "The checker compares the agent's computed gaps to the paper's reference values; it also extracts the linear temperature coefficient between 100 K and 300 K and compares to the paper's reported coefficients. All reference values are hidden."
}
```

## How you are scored
A hidden verifier reads the two CSV files you produce. For each compound, it compares your reported gap at each of the five temperatures against hidden reference values derived from the original work. Credit is awarded based on how many of the five temperature points agree within a hidden tolerance. In addition, the verifier computes the linear temperature coefficient of the gap over the range 100–300 K from your data and checks it against a hidden reference coefficient. The final reward is a weighted combination of these pointwise and slope checks. All reference values and tolerances are concealed; you must implement the correct physics to succeed.
