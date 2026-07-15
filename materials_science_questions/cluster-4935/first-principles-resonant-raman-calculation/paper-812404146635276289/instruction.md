# Two-Electron Mesoscopic Ring: Persistent Current and Optical Spectra

## Problem background
Two electrons confined in a narrow-width mesoscopic ring form a Wigner molecule due to the interplay between Coulomb repulsion and radial confinement. In the presence of an Aharonov–Bohm flux threading the ring, the two-electron energy bands give rise to an equilibrium persistent current. The same energy band structure governs the optical absorption and resonant inelastic light scattering (Raman) spectra, with specific selection rules for different polarization configurations. Reproducing these three quantities—persistent current, absorption power, and Raman cross-section—demonstrates the consistency between the electronic structure and the spectroscopic properties of the ring.

## Approach
The approach relies on an adiabatic decoupling of radial and angular motions in a finite-width mesoscopic ring. Under the assumption that the radial confinement is much stronger than the angular interactions, the radial eigenstates are computed first, followed by a numerical solution of the one-dimensional relative-angular Schrödinger equation that includes the Coulomb repulsion between the electrons. The relative-angular motion is treated in a tight-binding-like approximation, yielding oscillation energies and wavefunctions. Finally, the rotational energy of the two-electron system as a whole is quantized as a function of the magnetic flux. Together these give the full two-electron eigenenergy spectrum.

The persistent current at zero temperature is then obtained as the derivative of the total occupied energy with respect to flux. For optical absorption, the dipole matrix elements and the selection rules (parity unchanged, radial indices unchanged, relative-phase index change of ±½, relative-angular vibrational index change by an odd integer, rotational index change by ±1, total spin unchanged) are used to compute the absorption power spectrum for an initial occupation of the lowest para state. For resonant Raman scattering, the scattering operators in the split-off valence band limit are employed, and separate spectra are computed for the polarized (supports the same transitions as absorption) and depolarized (includes intra-ortho and para-ortho transitions) configurations, assuming the incident photon energy is tuned to be resonant with a typical transition. All calculations use the specified ring parameters (mean radius R=100 nm, radial width W=10 nm, effective mass m_e=0.067 m_0, static dielectric constant ε_s=12.9) and fundamental constants.

## Reproduction target
For a two-electron mesoscopic ring with the given parameters, compute the persistent current as a function of the Aharonov–Bohm flux ratio Φ/Φ₀ from –2 to 2, the optical absorption power spectrum over the frequency range 0–10 meV, and the resonant Raman differential cross-section in both polarized and depolarized configurations over the same frequency range. Output three CSV files:
- `persistent_current.csv`: flux (dimensionless) and current (nA)
- `absorption_spectrum.csv`: frequency (meV) and normalized absorption power
- `raman_cross_section.csv`: frequency (meV), normalized cross-section, and polarization label ('polarized' or 'depolarized')
The persistent current must be derived from the eigenenergies; the absorption and Raman spectra must follow the selection rules described below and be normalized to a maximum of 1.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement the two-electron energy band model
- Role: process
- Action: Implement the two-electron model for a finite-width mesoscopic ring: compute radial eigenenergies for the given radial confinement potential, solve the relative-angular Schrödinger equation numerically (e.g., finite-difference) to obtain relative-angular oscillation energies j_osc and wavefunctions, and derive the rotational energies rot() as a function of flux. Also compute the necessary dipole matrix elements (for absorption) and scattering operator matrix elements (for Raman, including the operators from the resonant split-off valence band theory) for later spectrum calculations. Use the specified parameters: mean radius R=100 nm, radial width W=10 nm, effective mass m_e=0.067 m_0, static dielectric constant s=12.9, and the physical constants (hbar, e, 0). This step is required to generate the energy bands and matrix elements used by all downstream steps.
- Evidence: `/app/outputs/model_energy_bands.log`

### Step 2: Compute persistent current vs flux
- Role: scored (load-bearing)
- Action: From the eigenenergies computed in step_0, calculate the persistent current I = -dE/d for a flux range /0 from -2 to 2 in steps of 0.01. Sum the contributions from the occupied states (lowest J, para and ortho states) at zero temperature. Output the flux (dimensionless) and the current in nanoamperes (use the conversion 1 e/(2m_e R^2)  1.83E-3 nA for the given R and m_e).
- Output file: `/app/outputs/persistent_current.csv`
- Format: csv
- Contract: Two columns: 'flux' (float, /0, dimensionless), 'current_nA' (float, current in nanoamperes). Rows for flux values from -2.0 to 2.0 in steps of 0.01.
- Scoring: scored by hidden verifier

### Step 3: Compute optical absorption spectrum
- Role: scored
- Action: Using the dipole matrix elements and the selection rules (parity unchanged, radial indices unchanged, relative-phase index changes by 1/2, relative-angular vibrational index changes by an odd integer, rotational index changes by 1, total spin unchanged), compute the absorption power _abs() for frequencies from 0 to 10 meV in steps of 0.02 meV. Assume initial occupation of the lowest para state and sum over all allowed final states. Normalize the spectrum to a maximum of 1. Output the frequency in meV and the normalized absorption power.
- Output file: `/app/outputs/absorption_spectrum.csv`
- Format: csv
- Contract: Two columns: 'frequency_meV' (float, photon energy in meV), 'absorption_power' (float, normalized to maximum of 1). Rows for frequencies from 0.0 to 10.0 meV in steps of 0.02 meV.
- Scoring: scored by hidden verifier

### Step 4: Compute resonant Raman scattering cross section
- Role: scored
- Action: Compute the differential Raman cross-section d^2/dd in the resonant regime (split-off valence band limit) for both polarized (e_L·e_S* = 1, e_Le_S* = 0) and depolarized (e_L·e_S* = 0, e_Le_S*  0) configurations. Use the scattering operators from the paper's resonant theory (spin-independent, spin-dependent terms) and apply the selection rules derived for each polarization: for polarized, identical to absorption; for depolarized, include transitions within ortho states (same spin, J=1, j odd) and between para and ortho states (S=1, j even). Assume incident photon energy resonant with a typical transition (e.g., 5 meV above the lowest absorption peak). Output scattering frequency (in meV), normalized cross-section (max=1), and a label 'polarized' or 'depolarized' for each configuration. Provide results for frequencies from 0 to 10 meV in steps of 0.02 meV for both polarizations.
- Output file: `/app/outputs/raman_cross_section.csv`
- Format: csv
- Contract: Three columns: 'frequency_meV' (float, scattering photon energy in meV), 'cross_section' (float, normalized to 1), 'polarization' (string, either 'polarized' or 'depolarized'). Rows for frequencies from 0.0 to 10.0 meV in steps of 0.02 meV for each polarization, resulting in 1002 rows total (501 per polarization).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/persistent_current.csv`
- `/app/outputs/absorption_spectrum.csv`
- `/app/outputs/raman_cross_section.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### persistent_current.csv
- path: `/app/outputs/persistent_current.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Persistent current as a function of the Aharonov-Bohm flux ratio. Checker recomputes the expected curve using the same model and compares pointwise.
- schema:
  - `type`: table
  - `required_columns`: `flux`, `current_nA`
  - `units`:
    - `flux`: dimensionless (/0)
    - `current_nA`: nanoamperes

### absorption_spectrum.csv
- path: `/app/outputs/absorption_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Optical absorption power spectrum. Checker recomputes the spectrum using the same model and selection rules, compares pointwise and verifies peak positions.
- schema:
  - `type`: table
  - `required_columns`: `frequency_meV`, `absorption_power`
  - `units`:
    - `frequency_meV`: meV
    - `absorption_power`: dimensionless (normalized to max 1)

### raman_cross_section.csv
- path: `/app/outputs/raman_cross_section.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Resonant Raman differential cross-section for both polarizations. Checker recomputes the spectra for each configuration and compares pointwise.
- schema:
  - `type`: table
  - `required_columns`: `frequency_meV`, `cross_section`, `polarization`
  - `units`:
    - `frequency_meV`: meV
    - `cross_section`: dimensionless (normalized to 1)
    - `polarization`: string ('polarized' or 'depolarized')

Notes: The checker implements the same analytical model (energy bands, dipole and Raman operators) with the identical parameters (R=100 nm, W=10 nm, m_e=0.067 m_0, s=12.9) and recomputes the expected persistent current, absorption spectrum, and Raman cross-section. Comparisons use pre-defined tolerances to verify correct reproduction. The outputs must be generated from the agent's own implementation of the model; direct copying of the paper's figures is insufficient.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "persistent_current.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "flux",
          "current_nA"
        ],
        "units": {
          "flux": "dimensionless (/0)",
          "current_nA": "nanoamperes"
        }
      },
      "description": "Persistent current as a function of the Aharonov-Bohm flux ratio. Checker recomputes the expected curve using the same model and compares pointwise."
    },
    {
      "file": "absorption_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_meV",
          "absorption_power"
        ],
        "units": {
          "frequency_meV": "meV",
          "absorption_power": "dimensionless (normalized to max 1)"
        }
      },
      "description": "Optical absorption power spectrum. Checker recomputes the spectrum using the same model and selection rules, compares pointwise and verifies peak positions."
    },
    {
      "file": "raman_cross_section.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_meV",
          "cross_section",
          "polarization"
        ],
        "units": {
          "frequency_meV": "meV",
          "cross_section": "dimensionless (normalized to 1)",
          "polarization": "string ('polarized' or 'depolarized')"
        }
      },
      "description": "Resonant Raman differential cross-section for both polarizations. Checker recomputes the spectra for each configuration and compares pointwise."
    }
  ],
  "notes": "The checker implements the same analytical model (energy bands, dipole and Raman operators) with the identical parameters (R=100 nm, W=10 nm, m_e=0.067 m_0, s=12.9) and recomputes the expected persistent current, absorption spectrum, and Raman cross-section. Comparisons use pre-defined tolerances to verify correct reproduction. The outputs must be generated from the agent's own implementation of the model; direct copying of the paper's figures is insufficient."
}
```

## How you are scored
A hidden verifier independently implements the same model and selection rules, recomputes the expected persistent current curve, absorption spectrum, and Raman cross-sections, and compares your output files pointwise. The verifier also checks that peak positions match the allowed transitions and that the spectra obey the polarization-dependent selection rules. The reward for each scored artifact is combined by weight to give the final score. Simply reporting the paper's published values is not sufficient; your own implementation must produce the correct results within the verifier's tolerance.
