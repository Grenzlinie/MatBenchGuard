# Phonon dispersion and Kohn anomaly identification in fcc Rh

## Problem background
The lattice dynamics of face-centered-cubic rhodium exhibit unexplained features in the phonon dispersion, particularly in the transverse branches along the (110) direction. Understanding whether these features are genuine Kohn anomalies—arising from Fermi-surface nesting and electron–phonon coupling—requires first-principles calculations of the phonon frequencies, elastic constants, and an analysis of the relationship between the phonon eigenvalues and an approximate dynamical-matrix contribution. Reproducing these quantities and verifying the coincidence between a dip in the phonon eigenvalue $m\omega^2$ and a peak in $-D_2^{approx}$ provides a stringent test of the theoretical description.

## Approach
The reproduction uses a plane-wave pseudopotential approach within the local-density approximation (LDA) of density-functional theory. The key computational stages are:

- **DFT self-consistent calculation**: Determine the equilibrium lattice constant, ground-state electronic structure, and Hellmann–Feynman forces for fcc Rh.
- **Elastic constants and zone-boundary phonons**: Compute the elastic constants $C_{11}$, $C_{12}$, $C_{44}$, and bulk modulus via homogeneous cell deformations, and obtain the longitudinal and transverse phonon frequencies at the $X$ point using frozen-phonon supercell calculations.
- **Interplanar force constants along (110)**: Build a supercell elongated along the [110] direction, displace central lattice planes, and extract interplanar force-constant matrices. From these, derive the transverse acoustic phonon frequencies $\omega(q)$ along (110).
- **Electronic structure on the (100) plane**: From the DFT electronic structure, extract band energies $\varepsilon(\mathbf{k})$ on a dense $\mathbf{k}$-grid in the (100) plane and compute electron velocities $v_\alpha = \partial\varepsilon/\partial k_\alpha$. Focus on the dominant band crossing the Fermi level for the anomaly analysis.
- **Anomaly analysis**: Using the force constants and band velocities, compute the transverse phonon eigenvalue $m\omega^2$ and the approximate dynamical-matrix contribution $-D_2^{approx}$ (which accounts for electron-phonon coupling) as functions of the reduced wavevector $q$. Identify the wavevector where $m\omega^2$ reaches a minimum and where $-D_2^{approx}$ reaches a maximum, and verify their coincidence.

## Reproduction target
This reproduction must produce two scored artifacts:

1. **phonon_properties.json** – contain the computed elastic constants ($C_{11}$, $C_{12}$, $C_{44}$, bulk modulus in GPa) and the longitudinal and transverse phonon frequencies at the $X$ point (in THz).
2. **anomaly_data.csv** – a three-column CSV with columns `q` (fractional coordinate along (110) from 0 to 0.5), `momega2` (phonon eigenvalue $m\omega^2$ in N/m²), and `D2approx` (the approximate $-D_2^{approx}$ value in arbitrary units) for the transverse (110) branch.

The hidden verifier will independently evaluate both artifacts against reference expectations.

## Assets

- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org/
- LDA pseudopotential for Rh: https://www.materialscloud.org/discover/sssp/table
- fcc Rh crystal structure

## Workflow steps

### Step 1: DFT self-consistent calculation and structural optimization
- Role: process
- Action: Perform a self-consistent LDA-DFT calculation for fcc Rh using a plane-wave pseudopotential code. Obtain the optimized lattice constant, ground-state electronic structure, and forces.
- Evidence: `/app/outputs/scf_optimization.log`

### Step 2: Elastic constants and X-point frozen-phonon frequencies
- Role: process
- Action: Compute the elastic constants C11, C12, C44 and bulk modulus via homogeneous deformations of the unit cell. Determine the longitudinal and transverse phonon frequencies at the X point using a frozen-phonon supercell calculation.
- Evidence: `/app/outputs/elastic_phonon.log`

### Step 3: Interplanar force constants along (110)
- Role: process
- Action: Construct a supercell elongated along the (110) direction and compute interplanar force-constant matrices by displacing central lattice planes and calculating Hellmann-Feynman forces. Derive the transverse acoustic phonon frequencies ω(q) along (110) from these force constants.
- Evidence: `/app/outputs/force_constants.log`

### Step 4: Electronic band structure and velocities on (100) plane
- Role: process
- Action: From the DFT electronic structure, extract band energies ε(k) for bands crossing the Fermi level on a dense k-grid (≥120×120) in the (100) plane. Compute electron velocities v_α = ∂ε/∂k_α and identify the dominant band for the anomaly analysis.
- Evidence: `/app/outputs/band_velocities.npy`

### Step 5: Scalar properties output
- Role: scored
- Action: Assemble the computed elastic constants and X-point phonon frequencies into a JSON file.
- Output file: `/app/outputs/phonon_properties.json`
- Format: json
- Contract: {"C11_GPa": float, "C12_GPa": float, "C44_GPa": float, "Bulk_modulus_GPa": float, "X_longitudinal_THz": float, "X_transverse_THz": float}
- Scoring: scored by hidden verifier

### Step 6: Anomaly analysis output
- Role: scored (load-bearing)
- Action: Using the interplanar force constants and the band energies/velocities, compute the phonon eigenvalue mω² for the transverse (110) branch and the approximate dynamical-matrix contribution -D₂^approx as a function of wavevector q. Write a CSV file with columns q, momega2, D2approx.
- Output file: `/app/outputs/anomaly_data.csv`
- Format: csv
- Contract: q (float, fractional coordinate 0→0.5), momega2 (float, N/m²), D2approx (float, arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_properties.json`
- `/app/outputs/anomaly_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_properties.json
- path: `/app/outputs/phonon_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants and X-point phonon frequencies; checker compares against hidden paper reference values with tolerances.
- schema:
  - `type`: object
  - `required`: `C11_GPa`, `C12_GPa`, `C44_GPa`, `Bulk_modulus_GPa`, `X_longitudinal_THz`, `X_transverse_THz`
  - `properties`:
    - `C11_GPa`:
      - `type`: number
      - `unit`: GPa
    - `C12_GPa`:
      - `type`: number
      - `unit`: GPa
    - `C44_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Bulk_modulus_GPa`:
      - `type`: number
      - `unit`: GPa
    - `X_longitudinal_THz`:
      - `type`: number
      - `unit`: THz
    - `X_transverse_THz`:
      - `type`: number
      - `unit`: THz

### anomaly_data.csv
- path: `/app/outputs/anomaly_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw data for the transverse (110) branch; checker recomputes the wavevector of the minimum in momeg2 and the maximum in D2approx and verifies their coincidence within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `q`, `momega2`, `D2approx`
  - `columns`:
    - `q`:
      - `type`: number
      - `description`: fractional coordinate along (110) from 0 to 0.5
    - `momega2`:
      - `type`: number
      - `unit`: N/m^2
      - `description`: phonon eigenvalue mω²
    - `D2approx`:
      - `type`: number
      - `unit`: arbitrary
      - `description`: approximate -D₂^approx value

Notes: The task uses a single LDA pseudopotential; the full dispersion curves and empirical force-constant fitting are omitted as per taskability scope. The anomaly verification relies on recomputing the peak/dip coincidence from the raw CSV data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "C11_GPa",
          "C12_GPa",
          "C44_GPa",
          "Bulk_modulus_GPa",
          "X_longitudinal_THz",
          "X_transverse_THz"
        ],
        "properties": {
          "C11_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "C12_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "C44_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Bulk_modulus_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "X_longitudinal_THz": {
            "type": "number",
            "unit": "THz"
          },
          "X_transverse_THz": {
            "type": "number",
            "unit": "THz"
          }
        }
      },
      "description": "Elastic constants and X-point phonon frequencies; checker compares against hidden paper reference values with tolerances."
    },
    {
      "file": "anomaly_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "momega2",
          "D2approx"
        ],
        "columns": {
          "q": {
            "type": "number",
            "description": "fractional coordinate along (110) from 0 to 0.5"
          },
          "momega2": {
            "type": "number",
            "unit": "N/m^2",
            "description": "phonon eigenvalue mω²"
          },
          "D2approx": {
            "type": "number",
            "unit": "arbitrary",
            "description": "approximate -D₂^approx value"
          }
        }
      },
      "description": "Raw data for the transverse (110) branch; checker recomputes the wavevector of the minimum in momeg2 and the maximum in D2approx and verifies their coincidence within a tolerance."
    }
  ],
  "notes": "The task uses a single LDA pseudopotential; the full dispersion curves and empirical force-constant fitting are omitted as per taskability scope. The anomaly verification relies on recomputing the peak/dip coincidence from the raw CSV data."
}
```

## How you are scored
A hidden verifier scores each output artifact independently and combines them into a final reward.

- **phonon_properties.json**: The verifier compares each reported scalar (elastic constants and X‑point frequencies) to reference values using relative tolerances. Correctness within the tolerance yields full credit for this stage.
- **anomaly_data.csv**: The verifier recomputes the wavevectors where $momega2$ reaches a minimum and $D2approx$ reaches a maximum within the $q = 0.1$–$0.5$ interval. The reward is based on the coincidence of the two wavevectors (within a mismatch tolerance) and on the depth of the dip relative to the branch’s maximum $momega2$ exceeding a threshold.

The anomaly analysis (Step 6) carries the larger weight, as it depends on the successful execution of all preceding process steps and captures the main finding. Simply reporting expected numbers is not sufficient—the verifier examines the submitted raw data and recomputes the key quantities to confirm they follow from genuine calculations.
