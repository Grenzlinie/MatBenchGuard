# Model Pseudopotential and Phonon Dispersion for Gold

## Problem background
Understanding the electron-ion interaction in noble metals is challenging because the tightly bound d-electrons strongly influence the conduction electrons. A simple model pseudopotential that captures both the repulsive core and the attractive d-electron region can provide physical insight into key metallic properties. This task implements such a model for gold and computes three quantities: the screened pseudopotential form factor, the liquid metal resistivity, and the phonon dispersion curves along high-symmetry directions. The target result demonstrates the ability of a simple analytical potential to reproduce experimental trends in these properties.

## Approach
The approach constructs a bare electron-ion pseudopotential in q‑space from a three‑region real‑space potential: a repulsive pseudocore, an attractive d‑electron shell, and a Coulomb tail. Two parameters—a pseudocore radius and an effective core‑plus‑d‑electron radius—are determined from atomic data. The bare potential is screened with the Vashishta‑Singwi dielectric function to obtain the form factor.

Liquid metal resistivity is computed using Ziman’s formula, which averages the squared screened form factor weighted by the liquid structure factor over the momentum transfer range. The structure factor is taken from a published source for liquid gold.

Phonon frequencies are obtained from the dynamical matrix, which is separated into three contributions: a Coulomb part from Ewald summation, a repulsive overlap-exchange part, and a band‑structure part that depends on the bare pseudopotential and dielectric function. The total squared frequency is the sum of Coulomb and repulsive parts minus the band‑structure part. Frequencies are evaluated at several points along the [00ζ], [0ζζ], and [ζζζ] symmetry directions and compared with experimental data.

## Reproduction target
Produce three artifacts from the computational pipeline described in the workflow steps:

- A CSV file of the screened form factor v(q) on a q‑grid from 0 to 2k_F (in atomic units), with the form factor values in Rydbergs.
- A single scalar file containing the liquid metal resistivity of gold in μΩ·cm, computed with Ziman’s formula and the provided liquid structure factor.
- A CSV file of phonon frequencies (in THz) along the high‑symmetry directions [00ζ], [0ζζ], [ζζζ], listing direction, ζ value, branch type (L, T1, T2), and frequency.

The form factor and resistivity should be compared against experimental references; phonon frequencies should be compared against measured dispersion data for gold.

## Assets

- Liquid structure factor a(K) for gold from Moriarty (1970): 10.1103/PhysRevB.1.1363

## Workflow steps

### Step 1: Derive model potential parameters
- Role: process
- Action: Using atomic data for gold (atomic radius R_a, core radius R_c, effective valence parameter α_eff, chemical valence z), determine the pseudocore radius R_ps and the core-plus-d-electron radius R_c+d from the relations in the paper. Save the determined parameters for subsequent steps.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute bare and screened form factor
- Role: scored (load-bearing)
- Action: Compute the bare pseudopotential V_b(q) using the model potential expression with the parameters from step 1 on a q-grid from 0 to 2k_F (k_F=0.637 a.u., Ω0=114.6 a.u.). Then compute the screened form factor v(q) = V_b(q)/ε*(q) using the Vashishta-Singwi dielectric function. Output a CSV with columns q (atomic units) and v_screened (Rydbergs).
- Output file: `/app/outputs/form_factor.csv`
- Format: csv
- Contract: q (float, atomic units), v_screened (float, Rydbergs)
- Scoring: scored by hidden verifier

### Step 3: Calculate liquid metal resistivity
- Role: scored
- Action: Using the screened form factor from step 2, the liquid structure factor a(K) for gold from Moriarty (1970), the Fermi energy derived from k_F, and Ziman's resistivity formula, compute the liquid metal resistivity ρ in μΩ·cm. Output a single float number.
- Output file: `/app/outputs/resistivity.txt`
- Format: txt
- Contract: float (μΩ·cm)
- Scoring: scored by hidden verifier

### Step 4: Compute repulsive contribution to dynamical matrix
- Role: process
- Action: Compute the repulsive part ω_R^2(q) of the dynamical matrix for gold along the q-paths [00ζ], [0ζζ], [ζζζ] following the procedure of Moriarty for core-overlap exchange. Use the ionic radius R_c+d and the fcc lattice constant.
- Evidence: `/app/outputs/repulsive_contrib.json`

### Step 5: Compute Coulomb contribution
- Role: process
- Action: Compute the Coulomb part ω_C^2(q) for the fcc gold lattice along the same symmetry directions using standard Ewald summation (or equivalently, tabulated values from Animalu et al., 1966).
- Evidence: `/app/outputs/coulomb_contrib.json`

### Step 6: Compute band-structure contribution
- Role: process
- Action: For each q along the symmetry directions, evaluate the band-structure part ω_E^2(q) using the lattice-sum formula with the bare pseudopotential V_b(q) (from step 2) and the dielectric function ε*(q). Sum over reciprocal lattice vectors H until convergence.
- Evidence: `/app/outputs/band_structure_contrib.json`

### Step 7: Compute phonon dispersion curves
- Role: scored
- Action: Combine the Coulomb, repulsive, and band-structure contributions to obtain total ω²(q) = ω_C² + ω_R² - ω_E². Convert to frequency ν = ω/(2π) in THz. Output a CSV with columns: direction (string: '100','110','111'), zeta (float between 0 and 1), branch (string: 'L','T1','T2'), frequency (float, THz).
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: direction (string), zeta (float, 0-1), branch (string: 'L','T1','T2'), frequency (float, THz)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/form_factor.csv`
- `/app/outputs/resistivity.txt`
- `/app/outputs/phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### form_factor.csv
- path: `/app/outputs/form_factor.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Screened pseudopotential form factor on a q-grid; the checker compares v_screened at hidden q-points to digitized reference values and scores a relative error metric (lower is better).
- schema:
  - `type`: table
  - `required_columns`: `q`, `v_screened`
  - `units`:
    - `q`: atomic units
    - `v_screened`: Rydbergs

### resistivity.txt
- path: `/app/outputs/resistivity.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Single-value liquid metal resistivity of gold; the checker compares the reported value to a hidden reference with a tolerance (closer to reference is better).
- schema:
  - `type`: scalar
  - `unit`: μΩ·cm

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Phonon frequencies at sampled points along principal symmetry directions; the checker computes mean absolute percentage error (MAPE) against hidden experimental data (lower MAPE is better) and scores against a threshold.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `zeta`, `branch`, `frequency`
  - `units`:
    - `frequency`: THz

Notes: The checker will compare the agent's numeric outputs to reference data (digitized form factor, experimental resistivity, experimental phonon frequencies) using relative error or MAPE. Scores are monotonic in quality: better-than-reference earns full credit, and credit degrades as the result worsens.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "form_factor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "v_screened"
        ],
        "units": {
          "q": "atomic units",
          "v_screened": "Rydbergs"
        }
      },
      "description": "Screened pseudopotential form factor on a q-grid; the checker compares v_screened at hidden q-points to digitized reference values and scores a relative error metric (lower is better)."
    },
    {
      "file": "resistivity.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "scalar",
        "unit": "μΩ·cm"
      },
      "description": "Single-value liquid metal resistivity of gold; the checker compares the reported value to a hidden reference with a tolerance (closer to reference is better)."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "zeta",
          "branch",
          "frequency"
        ],
        "units": {
          "frequency": "THz"
        }
      },
      "description": "Phonon frequencies at sampled points along principal symmetry directions; the checker computes mean absolute percentage error (MAPE) against hidden experimental data (lower MAPE is better) and scores against a threshold."
    }
  ],
  "notes": "The checker will compare the agent's numeric outputs to reference data (digitized form factor, experimental resistivity, experimental phonon frequencies) using relative error or MAPE. Scores are monotonic in quality: better-than-reference earns full credit, and credit degrades as the result worsens."
}
```

## How you are scored
A hidden verifier will independently inspect each output file and compare your computed values to reference data. For the form factor, it samples v(q) at specific q‑points and scores the relative error. The resistivity is compared to a reference value with a tolerance, and phonon frequencies are compared against experimental dispersion data using a mean percentage error metric. Each artifact is scored separately and combined by weight into a final reward—better agreement earns a higher score. The verifier only knows your submitted files; reporting the reference numbers without actual computation yields a low reward.
