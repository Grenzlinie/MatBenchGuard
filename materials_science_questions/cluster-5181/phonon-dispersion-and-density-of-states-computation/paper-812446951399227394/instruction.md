# Phonon dispersion and density of states computation for α-Sn

## Problem background
α-Sn (grey tin) is a diamond-structure covalent semiconductor. Accurate knowledge of its lattice dynamics — phonon dispersion, density of states, Debye characteristic temperature, and compressibility — is important for understanding its thermal and mechanical properties. This task requires computing these quantities from first principles using a five-parameter phenomenological lattice-dynamical model that includes central and bond-bending forces. The computed results are compared against experimental data to assess the model.

## Approach
The model employs short-range central forces (radial interactions) and unpaired bond-bending forces to describe the interatomic interactions in the diamond cubic lattice of α-Sn. The crystal structure is diamond cubic with lattice constant 2a = 6.486 Å. The model contains five adjustable parameters. These parameters are determined by fitting to the experimental elastic constants C11, C12 and three critical-point phonon frequencies (νLO/LA(X), νTO(X), νTA(X)) reported by Price et al. (1971). Using the fitted parameters, a 6×6 dynamical matrix is constructed for each wavevector q in the first Brillouin zone. Solving the secular determinant yields the six phonon eigenfrequencies at each q. The full eigenfrequency spectrum is then used to obtain (i) high-symmetry point frequencies, (ii) the phonon density of states histogram, (iii) the Debye characteristic temperature as a function of temperature (10–300 K) via heat capacity calculations, and (iv) the compressibility through the Brout sum rule, which relates the sum of squared frequencies over all branches to the bulk compressibility.

## Reproduction target
Implement the five-parameter model, perform the parameter fitting, and compute the full phonon spectrum for α-Sn. From the spectrum, produce the following scalar and tabular outputs:
- Frequencies at the high‑symmetry points Γ, X, L, K for all six branches.
- The phonon density of states g(ν) as a histogram.
- Debye characteristic temperature θD at temperatures from 10 K to 300 K.
- The compressibility χ of α-Sn derived from the Brout sum rule.
The outputs are submitted in the specified files and evaluated against hidden reference data and structural checks.

## Assets

- Experimental data for α-Sn (Price et al. 1971): 10.1103/PhysRevB.3.1268
- Lattice constant of α-Sn (AIP Handbook 1972)
- Standard Cv vs θD/T table (Saha & Srivastava 1965)

## Workflow steps

### Step 1: Fit five model parameters
- Role: process
- Action: Using the experimental elastic constants C11, C12 and the three critical-point phonon frequencies νLO/LA(X), νTO(X), νTA(X) from Price et al. (1971) for α-Sn, together with the lattice constant, fit the five parameters (α1', α2, γ1', γ2', γ3') of the central plus bond-bending potential model for diamond‑structure crystals (Kushwaha & Kushwaha 1979). The model defines short‑range central and bond‑bending forces; the dynamical matrix follows from these parameters.
- Evidence: `/app/outputs/parameter_fit.json`

### Step 2: Solve phonon eigenfrequencies on q-point grid
- Role: process
- Action: Construct the dynamical matrix for diamond‑structure α-Sn using the fitted parameters. Sample the 48 nonequivalent wavevectors in the first Brillouin zone and further subdivide the zone to obtain a dense mesh (as per the lattice‑dynamical procedure). At each q‑point, solve the secular determinant to obtain the six phonon eigenfrequencies. Store the full eigenfrequency spectrum for subsequent steps.
- Evidence: `/app/outputs/eigenfrequencies.npz`

### Step 3: Extract high‑symmetry point frequencies
- Role: scored (load-bearing)
- Action: From the computed eigenfrequencies, extract the phonon frequencies for the six branches at the high‑symmetry points Γ, X, L, K and write a CSV file.
- Output file: `/app/outputs/frequencies.csv`
- Format: csv
- Contract: CSV with columns: q_point (string: one of Γ, X, L, K), branch_label (string: e.g. TA1,TA2,LA,TO1,TO2,LO), frequency (float, THz).
- Scoring: scored by hidden verifier

### Step 4: Compute phonon density of states
- Role: scored
- Action: From the eigenfrequency spectrum over the whole Brillouin zone, build a histogram g(ν) with bins of width ν_max/100 covering the frequency range up to the maximum phonon frequency. Output the histogram as CSV.
- Output file: `/app/outputs/dos.csv`
- Format: csv
- Contract: CSV with columns: freq_low (float, THz), freq_high (float, THz), g_nu (float, states/THz).
- Scoring: scored by hidden verifier

### Step 5: Calculate Debye temperature vs temperature
- Role: scored
- Action: From the density of states, compute the lattice heat capacity Cv at constant volume for a set of temperatures from 10 to 300 K (using Blackman's sampling technique). Then, using the standard Cv vs θD/T table (or the analytic Debye model), deduce the Debye characteristic temperature θD at each temperature. Output the results as CSV.
- Output file: `/app/outputs/debye_temperatures.csv`
- Format: csv
- Contract: CSV with columns: T (float, K), theta_D (float, K). At least 10 evenly spaced temperatures between 10 K and 300 K.
- Scoring: scored by hidden verifier

### Step 6: Compute compressibility via Brout sum rule
- Role: scored (load-bearing)
- Action: For every q‑point, sum the squared angular frequencies ω_i²(q) over all six branches. Apply the Brout sum rule Σ ω_i²(q) = 16√3 r₀ / (μ χ) using the lattice constant to obtain the nearest‑neighbour distance r₀ and the atomic mass to obtain the reduced mass μ. Solve for the compressibility χ and output the value in units of 10⁻¹² cm²/dyne.
- Output file: `/app/outputs/compressibility.txt`
- Format: txt
- Contract: Single line containing a float representing the compressibility in units of 10^{-12} cm^2/dyne.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequencies.csv`
- `/app/outputs/dos.csv`
- `/app/outputs/debye_temperatures.csv`
- `/app/outputs/compressibility.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequencies.csv
- path: `/app/outputs/frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at high-symmetry points Γ, X, L, K for the six branches of α‑Sn.
- schema:
  - `type`: table
  - `required_columns`: `q_point`, `branch_label`, `frequency`
  - `columns`:
    - `q_point`: string
    - `branch_label`: string
    - `frequency`:
      - `type`: number
      - `unit`: THz

### dos.csv
- path: `/app/outputs/dos.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon density of states histogram g(ν) for α‑Sn. Integral over the histogram should be approximately 6 (the total number of phonon branches).
- schema:
  - `type`: table
  - `required_columns`: `freq_low`, `freq_high`, `g_nu`
  - `columns`:
    - `freq_low`:
      - `type`: number
      - `unit`: THz
    - `freq_high`:
      - `type`: number
      - `unit`: THz
    - `g_nu`:
      - `type`: number
      - `unit`: states/THz

### debye_temperatures.csv
- path: `/app/outputs/debye_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Debye characteristic temperature θD of α‑Sn as a function of temperature from 10 K to 300 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `theta_D`
  - `columns`:
    - `T`:
      - `type`: number
      - `unit`: K
    - `theta_D`:
      - `type`: number
      - `unit`: K

### compressibility.txt
- path: `/app/outputs/compressibility.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Compressibility of α‑Sn computed from the Brout sum rule using the full phonon spectrum.
- schema:
  - `type`: text
  - `content`: A single line containing a float representing the compressibility χ in units of 10^{-12} cm^2/dyne.

Notes: All scored outputs are derived from the same underlying phonon eigenfrequency spectrum. The agent must implement the five‑parameter model and perform the eigenfrequency calculation; the process steps are not scored directly but are enforced by the load‑bearing scored steps (frequencies and compressibility).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q_point",
          "branch_label",
          "frequency"
        ],
        "columns": {
          "q_point": "string",
          "branch_label": "string",
          "frequency": {
            "type": "number",
            "unit": "THz"
          }
        }
      },
      "description": "Phonon frequencies at high-symmetry points Γ, X, L, K for the six branches of α‑Sn."
    },
    {
      "file": "dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "freq_low",
          "freq_high",
          "g_nu"
        ],
        "columns": {
          "freq_low": {
            "type": "number",
            "unit": "THz"
          },
          "freq_high": {
            "type": "number",
            "unit": "THz"
          },
          "g_nu": {
            "type": "number",
            "unit": "states/THz"
          }
        }
      },
      "description": "Phonon density of states histogram g(ν) for α‑Sn. Integral over the histogram should be approximately 6 (the total number of phonon branches)."
    },
    {
      "file": "debye_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "theta_D"
        ],
        "columns": {
          "T": {
            "type": "number",
            "unit": "K"
          },
          "theta_D": {
            "type": "number",
            "unit": "K"
          }
        }
      },
      "description": "Debye characteristic temperature θD of α‑Sn as a function of temperature from 10 K to 300 K."
    },
    {
      "file": "compressibility.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "A single line containing a float representing the compressibility χ in units of 10^{-12} cm^2/dyne."
      },
      "description": "Compressibility of α‑Sn computed from the Brout sum rule using the full phonon spectrum."
    }
  ],
  "notes": "All scored outputs are derived from the same underlying phonon eigenfrequency spectrum. The agent must implement the five‑parameter model and perform the eigenfrequency calculation; the process steps are not scored directly but are enforced by the load‑bearing scored steps (frequencies and compressibility)."
}
```

## How you are scored
A hidden verifier inspects each of your output files. For the frequency table (frequencies.csv) and Debye temperature table (debye_temperatures.csv), your computed values are compared to precision reference values with appropriately chosen tolerances. For the density of states (dos.csv), the verifier performs a structural audit (positive histogram, total integral consistent with the expected number of phonon branches). For the compressibility (compressibility.txt), the derived value is compared to a reference. The final score is a weighted combination of these stage scores. Simply reporting a number without executing the underlying lattice‑dynamical calculation will not yield a high score.
