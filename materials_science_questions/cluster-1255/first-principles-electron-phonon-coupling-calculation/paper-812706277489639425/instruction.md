# Electron Spectral Functions and Mobility in Large-Polaron Materials via Retarded Cumulant Approach

## Problem background
Understanding charge transport in materials with strong electron-phonon ($e$-ph) coupling is a major challenge in condensed matter physics. When the coupling is intermediate, electrons form large polarons, and the standard quasiparticle (QP) scattering picture — on which the Boltzmann transport equation (BTE) is based — often fails. The cubic perovskite SrTiO$_3$ is a prototypical large-polaron material where experimental mobility and optical conductivity deviate from QP predictions, yet the microscopic transport mechanisms and the transition from bandlike to incoherent transport are not well understood. This work addresses charge transport in SrTiO$_3$ from first principles by going beyond the QP approximation and directly computing the electron spectral function, which encompasses both coherent and incoherent many-body effects.

## Approach
The approach combines $ab$ $initio$ density functional theory (DFT), anharmonic phonon calculations, and a finite-temperature retarded cumulant expansion. First, the electronic structure of cubic SrTiO$_3$ (lattice parameter 3.9 Å) is obtained within the PBE functional using norm-conserving pseudopotentials with spin-orbit coupling, yielding Kohn–Sham wavefunctions and band energies. Temperature-dependent phonon frequencies and eigenvectors are computed with the Temperature Dependent Effective Potential (TDEP) method to correctly include soft-mode anharmonicity. Coarse-grid electron-phonon matrix elements among the Ti-$t_{2g}$ conduction bands are evaluated via density functional perturbation theory (DFPT) and then interpolated to ultrafine Brillouin-zone grids using maximally-localized Wannier functions, with a long-range dipole correction for polar LO modes. The lowest-order $e$-ph self-energy is computed off-shell on a dense energy mesh and on-shell at the DFT eigenvalues.

The central theoretical step is the finite-temperature retarded cumulant formalism, which constructs the retarded Green’s function from the self-energy via an exponential ansatz in the time domain. Fourier transformation yields the spectral function $A_{n\mathbf{k}}(\omega)$ for each electronic state, capturing both the QP peak and phonon satellite replicas that signal polaron physics. With the spectral functions as input, the frequency-dependent conductivity $\sigma(\omega)$ is evaluated using the Kubo formula (neglecting vertex corrections). The dc mobility is obtained from $\sigma(0)$ and the carrier concentration for light $n$-doping ($\sim10^{17}$ cm$^{-3}$). The normalized optical conductivity is computed directly from $\sigma(\omega)$. The effective transport scattering rate is extracted via the extended Drude model, and the incoherent fraction is defined as the ratio of the conductivity integrated over energies above the QP peak to the total dc conductivity.

All stages are computationally linked: the DFT and TDEP outputs are required for DFPT and Wannier interpolation, which in turn provide the self-energy needed for the cumulant spectral functions; the spectral functions then feed into the conductivity, mobility, and derived quantities.

## Reproduction target
The objective is to produce the following independent artifacts, all generated from the first-principles pipeline described above:

1. Spectral function at the Γ point of the lowest conduction band for temperatures 110, 150, and 300 K (output: spectral_function_gamma.json).
2. Temperature-dependent electron mobility between 150 and 300 K (step 25 K) at light n-doping (output: mobility_vs_temperature.csv).
3. Normalized optical conductivity at 300 K over 0–0.2 eV (output: optical_conductivity_300K.csv).
4. Effective transport scattering rate at 300 K in meV (output: effective_scattering_rate_300K.txt).
5. Ratio of incoherent to total dc conductivity at 300 K (output: incoherent_ratio_300K.txt).

The spectral function must show a well-defined quasiparticle peak and at least two phonon satellite peaks; the mobility should capture the temperature trend over the indicated range; the optical conductivity must exhibit a Drude peak at zero frequency and an incoherent shoulder; the scattering rate should be compared to the Planckian limit $k_{\mathrm{B}}T$ at 300 K (≈26 meV); and the incoherent ratio quantifies the beyond‑QP contribution.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- Wannier90: https://wannier.org
- PseudoDojo norm-conserving pseudopotentials (Sr, Ti, O): http://www.pseudo-dojo.org
- Temperature Dependent Effective Potential (TDEP): https://github.com/tdep-developers/tdep

## Workflow steps

### Step 1: DFT ground-state calculation
- Role: process
- Action: Perform density functional theory (DFT) ground-state calculation for cubic SrTiO3 (lattice parameter 3.9 Å) using PBE functional and norm-conserving pseudopotentials with spin-orbit coupling. Compute Kohn-Sham wavefunctions and band energies on a coarse k-point grid.
- Evidence: none

### Step 2: Anharmonic phonon calculation via TDEP
- Role: process
- Action: Use the temperature-dependent effective potential (TDEP) method to compute temperature-dependent phonon frequencies and eigenvectors for cubic SrTiO3, including the ferroelectric soft mode, using DFT forces from supercell calculations.
- Evidence: none

### Step 3: Coarse-grid e-ph matrix elements via DFPT
- Role: process
- Action: Compute the electron-phonon matrix elements on coarse k- and q-point grids using density functional perturbation theory (DFPT) and Wannier functions for the Ti-t2g bands, with input from DFT and TDEP eigenvectors.
- Evidence: none

### Step 4: Wannier interpolation to fine grids
- Role: process
- Action: Interpolate the coarse-grid e-ph matrix elements to ultrafine Brillouin-zone grids using maximally-localized Wannier functions, including the long-range dipole Fröhlich correction for polar LO modes.
- Evidence: none

### Step 5: Lowest-order e-ph self-energy calculation
- Role: process
- Action: Compute the off-shell imaginary part of the self-energy on a dense energy grid and the on-shell real part at the DFT energy using the fine-grid e-ph matrix elements, temperature-dependent phonon frequencies, and occupation factors.
- Evidence: none

### Step 6: Finite-temperature retarded cumulant spectral function
- Role: scored (load-bearing)
- Action: Implement the finite-temperature retarded cumulant formalism to compute the electron spectral function for the lowest conduction band, using the previously computed self-energy as input. Output the spectral function at the Gamma point for temperatures 110, 150, and 300 K.
- Output file: `/app/outputs/spectral_function_gamma.json`
- Format: json
- Contract: JSON object with keys '110','150','300', each an array of {omega: float(eV), A: float}
- Scoring: scored by hidden verifier

### Step 7: Electron mobility from Kubo formula
- Role: scored
- Action: Using the computed spectral functions, band velocities, and a light n-doping concentration (~10^17 cm^-3), compute the temperature-dependent electron mobility via the Kubo formula without vertex corrections, and output a CSV of temperature vs mobility between 150 and 300 K.
- Output file: `/app/outputs/mobility_vs_temperature.csv`
- Format: csv
- Contract: CSV columns: temperature_K, mobility_cm2_Vs (float)
- Scoring: scored by hidden verifier

### Step 8: Optical conductivity at 300 K
- Role: scored
- Action: Compute the optical conductivity at 300 K using the Kubo formula and output the normalized conductivity (integral=1) for frequencies 0-0.2 eV.
- Output file: `/app/outputs/optical_conductivity_300K.csv`
- Format: csv
- Contract: CSV columns: omega_eV (float), sigma_norm (float)
- Scoring: scored by hidden verifier

### Step 9: Effective transport scattering rate
- Role: scored
- Action: Apply the extended Drude analysis to extract the effective transport scattering rate from the computed optical conductivity at 300 K. Output a single float value in meV.
- Output file: `/app/outputs/effective_scattering_rate_300K.txt`
- Format: txt
- Contract: single float (meV)
- Scoring: scored by hidden verifier

### Step 10: Incoherent contribution fraction
- Role: scored
- Action: Integrate the transport distribution function above the QP peak energy to obtain the incoherent dc conductivity and compute its ratio to total conductivity at 300 K. Output a single float.
- Output file: `/app/outputs/incoherent_ratio_300K.txt`
- Format: txt
- Contract: single float (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectral_function_gamma.json`
- `/app/outputs/mobility_vs_temperature.csv`
- `/app/outputs/optical_conductivity_300K.csv`
- `/app/outputs/effective_scattering_rate_300K.txt`
- `/app/outputs/incoherent_ratio_300K.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectral_function_gamma.json
- path: `/app/outputs/spectral_function_gamma.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Electron spectral function at the Gamma point for three temperatures, used to locate QP and satellite peaks.
- schema:
  - `type`: object
  - `required`:
    - `110`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `omega`:
            - `type`: number
            - `units`: eV
          - `A`:
            - `type`: number
            - `units`: dimensionless
    - `150`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `omega`:
            - `type`: number
            - `units`: eV
          - `A`:
            - `type`: number
            - `units`: dimensionless
    - `300`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `omega`:
            - `type`: number
            - `units`: eV
          - `A`:
            - `type`: number
            - `units`: dimensionless
  - `units`: object

### mobility_vs_temperature.csv
- path: `/app/outputs/mobility_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed electron mobility as a function of temperature, compared to paper values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `mobility_cm2_Vs`
  - `units`:
    - `temperature_K`: K
    - `mobility_cm2_Vs`: cm^2/V·s

### optical_conductivity_300K.csv
- path: `/app/outputs/optical_conductivity_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized optical conductivity at 300 K; audited for Drude peak and shoulder.
- schema:
  - `type`: table
  - `required_columns`: `omega_eV`, `sigma_norm`
  - `units`:
    - `omega_eV`: eV
    - `sigma_norm`: dimensionless

### effective_scattering_rate_300K.txt
- path: `/app/outputs/effective_scattering_rate_300K.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Effective transport scattering rate at 300 K; must exceed Planckian limit.
- schema:
  - `type`: text
  - `required`:
    - `value`: float (meV)
  - `units`:
    - `value`: meV

### incoherent_ratio_300K.txt
- path: `/app/outputs/incoherent_ratio_300K.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Fraction of incoherent contribution to dc conductivity at 300 K; expected in 0.3-0.5 range.
- schema:
  - `type`: text
  - `required`:
    - `value`: float
  - `units`:
    - `value`: dimensionless

Notes: All scored artifacts follow the plan's required_outputs and verification_method. Process steps (00-04) produce intermediate data consumed by scored steps and are forced by the load-bearing step_05.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectral_function_gamma.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "110": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "omega": {
                  "type": "number",
                  "units": "eV"
                },
                "A": {
                  "type": "number",
                  "units": "dimensionless"
                }
              }
            }
          },
          "150": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "omega": {
                  "type": "number",
                  "units": "eV"
                },
                "A": {
                  "type": "number",
                  "units": "dimensionless"
                }
              }
            }
          },
          "300": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "omega": {
                  "type": "number",
                  "units": "eV"
                },
                "A": {
                  "type": "number",
                  "units": "dimensionless"
                }
              }
            }
          }
        },
        "units": {}
      },
      "description": "Electron spectral function at the Gamma point for three temperatures, used to locate QP and satellite peaks."
    },
    {
      "file": "mobility_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "mobility_cm2_Vs"
        ],
        "units": {
          "temperature_K": "K",
          "mobility_cm2_Vs": "cm^2/V·s"
        }
      },
      "description": "Computed electron mobility as a function of temperature, compared to paper values within tolerance."
    },
    {
      "file": "optical_conductivity_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_eV",
          "sigma_norm"
        ],
        "units": {
          "omega_eV": "eV",
          "sigma_norm": "dimensionless"
        }
      },
      "description": "Normalized optical conductivity at 300 K; audited for Drude peak and shoulder."
    },
    {
      "file": "effective_scattering_rate_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "required": {
          "value": "float (meV)"
        },
        "units": {
          "value": "meV"
        }
      },
      "description": "Effective transport scattering rate at 300 K; must exceed Planckian limit."
    },
    {
      "file": "incoherent_ratio_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "required": {
          "value": "float"
        },
        "units": {
          "value": "dimensionless"
        }
      },
      "description": "Fraction of incoherent contribution to dc conductivity at 300 K; expected in 0.3-0.5 range."
    }
  ],
  "notes": "All scored artifacts follow the plan's required_outputs and verification_method. Process steps (00-04) produce intermediate data consumed by scored steps and are forced by the load-bearing step_05."
}
```

## How you are scored
Each output file is checked independently by a hidden verifier that compares your results against robust criteria derived from the scientific claims. The checks are as follows:

- **Spectral function** – The verifier locates the QP peak and the main satellite peaks and verifies that their relative energies lie within expected ranges (structural audit).
- **Mobility** – The mobility values at each temperature are compared to hidden reference values using a tolerance that accounts for legitimate numerical spread from reimplementation (result‑level compare).
- **Optical conductivity** – The presence of a Drude peak at ω = 0 and a shoulder feature is validated by examining the second derivative (structural audit).
- **Scattering rate** – The reported number is verified to exceed a fixed threshold (threshold‑or‑better check).
- **Incoherent ratio** – The ratio is checked to fall within a predetermined numerical interval (structural audit).

The final score is a weighted combination of these stage checks; simply reporting a number that matches a reference without performing the actual computation will fail the structural audits. All artifacts must be written exactly to the paths specified below.
