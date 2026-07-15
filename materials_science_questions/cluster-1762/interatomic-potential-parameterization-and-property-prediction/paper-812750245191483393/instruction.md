# Computation of Electronic Bands and Optical Absorption of Chromium and Iron

## Problem background
Transition metals chromium (Cr) and iron (Fe) in their body-centered cubic (BCC) phase are foundational materials in many technological applications. Their electronic structure and optical absorption properties dictate behavior ranging from mechanical strength to electrochemistry. First-principles electronic structure methods provide a powerful route to predict these properties. The Korringa–Kohn–Rostoker (KKR) method, when combined with the computationally efficient Segall–Yang representation of structure constants, enables accurate determination of energy bands and the subsequent calculation of the imaginary part of the dielectric function \(\varepsilon_2(\omega)\)—the optical absorption spectrum—for these metals. This task reproduces the KKR-based computation of the \(\varepsilon_2\) spectra for BCC Cr and Fe and extracts the characteristic absorption peak positions.

## Approach
The reproduction follows the KKR method within the muffin-tin approximation. First, a crystal potential is constructed for each metal by superimposing atomic charge densities obtained from the Herman–Skillman program, adding Slater exchange via the \(\alpha\)-parameter, and solving Poisson's equation. The radial Schrödinger equation is then solved inside the muffin-tin sphere to obtain energy-dependent logarithmic derivatives. The KKR structure constants are handled using the Segall–Yang technique: a smooth function \(f_{LM}(\mathbf{k},E)\) is fitted with two-dimensional polynomials over energy and \(|\mathbf{k}|\) along symmetry axes, while explicit pole-sum terms capture the remaining contributions. Solving the secular determinant yields the electronic band structure on a dense \(\mathbf{k}\)-point mesh. From the band structure, the imaginary part of the dielectric function \(\varepsilon_2(\omega)\) is computed for photon energies up to 6 eV by integrating the joint density of states with constant transition matrix elements over the Brillouin zone. Finally, local maxima (peaks) of \(\varepsilon_2\) are identified and reported for each metal.

## Reproduction target
Produce the imaginary part of the dielectric function \(\varepsilon_2(\omega)\) for BCC Cr and Fe over the photon energy range 0–6 eV using the KKR method as described. From the resulting spectra, identify the positions (in eV) of the major absorption peaks (local maxima) for each metal. Write these peak positions to the scored output files. The exact values are not supplied; they must be determined by your computation.

## Assets

- Herman–Skillman atomic structure program
- AkaiKKR (Machikaneyama) KKR code: https://kkr.issp.u-tokyo.ac.jp/

## Workflow steps

### Step 1: Construct muffin-tin crystal potentials
- Role: process
- Action: Using the Hartree–Fock–Slater method with the Herman–Skillman atomic program and Löwdin α-expansion, construct muffin-tin potentials for BCC Cr (atomic configuration 3d⁵4s¹, α=0.725) and Fe (3d⁷4s¹, α=1.0). Superpose atomic charge densities, solve Poisson's equation, and add Slater exchange.
- Evidence: `/app/outputs/potential_cr.dat, potential_fe.dat`

### Step 2: Compute logarithmic derivatives
- Role: process
- Action: For each metal, solve the radial Schrödinger equation inside the muffin-tin sphere on an energy grid to obtain energy-dependent logarithmic derivatives L_l(E) for all required angular momenta l.
- Evidence: `/app/outputs/log_derivatives_cr.dat, log_derivatives_fe.dat`

### Step 3: Fit polynomial coefficients for structure constants
- Role: process
- Action: Implement the Segall–Yang representation of KKR structure constants. Using the Davis numerical technique with η=0.25, N_reciprocal=43, N_direct=20, and cutoffs for largest reciprocal/direct vectors squared of 6 and 27, compute the smooth function f_{LM}(k,E) on a grid of energies and |k| along symmetry axes. Fit f_{LM} with two‑dimensional polynomials in E and |k| and store the coefficients.
- Evidence: `/app/outputs/coeff_poly_LM_cr.dat, coeff_poly_LM_fe.dat`

### Step 4: Solve KKR secular determinant to obtain band structures
- Role: process
- Action: Using the fitted polynomial coefficients (for the smooth part), the explicit pole‑sum terms, and the logarithmic derivatives, evaluate the KKR structure constants D_{LM}(k,E). Solve the secular determinant det|...|=0 to find energy eigenvalues E(k) on a dense k‑point mesh along high‑symmetry directions for both Cr and Fe. Store the electronic band structures.
- Evidence: `/app/outputs/bands_cr.dat, bands_fe.dat`

### Step 5: Compute ε₂ optical spectra
- Role: process
- Action: From the converged band structures, calculate the imaginary part of the dielectric function ε₂(ω) for photon energies up to 6 eV. Evaluate the joint density of states using constant transition matrix elements, integrating over the Brillouin zone. Store the full ε₂ spectrum as a function of photon energy for each metal.
- Evidence: `/app/outputs/e2_spectrum_cr.csv, e2_spectrum_fe.csv`

### Step 6: Extract ε₂ peak positions for chromium
- Role: scored (load-bearing)
- Action: From the ε₂ spectrum for Cr (e2_spectrum_cr.csv), identify local maxima (peaks) in the range 0–6 eV. Write the peak positions to cr_e2_peaks.csv.
- Output file: `/app/outputs/cr_e2_peaks.csv`
- Format: csv
- Contract: CSV with columns: peak_id (string), energy_eV (float). Must contain at least three rows for the major absorption peaks.
- Scoring: scored by hidden verifier

### Step 7: Extract ε₂ peak positions for iron
- Role: scored (load-bearing)
- Action: From the ε₂ spectrum for Fe (e2_spectrum_fe.csv), identify local maxima in the range 0–6 eV and write the peak positions to fe_e2_peaks.csv.
- Output file: `/app/outputs/fe_e2_peaks.csv`
- Format: csv
- Contract: CSV with columns: peak_id (string), energy_eV (float). Must contain at least three rows for the major absorption peaks.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cr_e2_peaks.csv`
- `/app/outputs/fe_e2_peaks.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cr_e2_peaks.csv
- path: `/app/outputs/cr_e2_peaks.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: ε₂ peak positions for chromium; the hidden checker recomputes peaks from the agent's raw ε₂ evidence and compares with paper‑reported gold.
- schema:
  - `type`: table
  - `required_columns`: `peak_id`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

### fe_e2_peaks.csv
- path: `/app/outputs/fe_e2_peaks.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: ε₂ peak positions for iron; the hidden checker recomputes peaks from the agent's raw ε₂ evidence and compares with paper‑reported gold.
- schema:
  - `type`: table
  - `required_columns`: `peak_id`, `energy_eV`
  - `units`:
    - `energy_eV`: eV

Notes: The checker will obtain the full ε₂ spectra from the process evidence files (e2_spectrum_cr.csv, e2_spectrum_fe.csv) and independently run a peak‑finding algorithm; the submitted scored peak files must be consistent with those recomputed peaks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cr_e2_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "peak_id",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "ε₂ peak positions for chromium; the hidden checker recomputes peaks from the agent's raw ε₂ evidence and compares with paper‑reported gold."
    },
    {
      "file": "fe_e2_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "peak_id",
          "energy_eV"
        ],
        "units": {
          "energy_eV": "eV"
        }
      },
      "description": "ε₂ peak positions for iron; the hidden checker recomputes peaks from the agent's raw ε₂ evidence and compares with paper‑reported gold."
    }
  ],
  "notes": "The checker will obtain the full ε₂ spectra from the process evidence files (e2_spectrum_cr.csv, e2_spectrum_fe.csv) and independently run a peak‑finding algorithm; the submitted scored peak files must be consistent with those recomputed peaks."
}
```

## How you are scored
A hidden verifier independently recomputes peak positions from your submitted raw \(\varepsilon_2\) evidence files (`e2_spectrum_cr.csv` and `e2_spectrum_fe.csv`) using a standard peak-finding algorithm. The verifier compares those recomputed peaks, as well as your submitted peak files (`cr_e2_peaks.csv` and `fe_e2_peaks.csv`), against a set of hidden reference peaks that represent the correct result of the KKR calculation. Your final reward (a float between 0 and 1) is based on how accurately your peaks match the references for both metals. Simply reporting numbers without generating the full spectrum evidence will not yield credit. The verifier uses a threshold-or-better policy: meeting or exceeding the reference quality earns full credit, and the reward decreases gracefully as results degrade.
