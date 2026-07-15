# Design of 1D Photonic Bandgap Devices using Leaky Mode Propagation

## Problem background
Waveguiding photonic band-gap (WPBG) structures are periodic optical devices that exhibit strongly wavelength-selective reflection and transmission properties. Designing such structures for filtering or resonance at a specific communication wavelength (around 1.55 µm) requires an accurate simulation method that can efficiently compute propagation constants, field distributions, and power flow while accounting for radiation losses. The Leaky Mode Propagation (LMP) method is a numerical approach that models multilayer 1D gratings by expanding electromagnetic fields in Floquet space harmonics and solving Maxwell's equations using Bloch-Floquet phase relations. In this task, you will implement the LMP method to design and analyze two types of WPBG devices: an air-bridge GaAs filter and a Si-on-glass traversing-etched waveguide PBG (TWPBG) resonator. Your goal is to compute their attenuation constants, reflection spectra, and band structures to evaluate whether the devices achieve the desired performance at 1.55 µm.

## Approach
You will implement the LMP method from scratch. The solver represents a planar multilayer structure (cover, top-cladding, periodic grating layer, waveguiding layer, substrate) and expands the electromagnetic field (TE or TM) in Floquet space harmonics. The periodic permittivity in the grating region is expanded in a Fourier series. Substituting these expansions into Maxwell's equations yields a system of differential equations for the harmonic amplitudes; its solution, together with Bloch-Floquet phase relations, determines the complex propagation constants (β₀ + jα) and the harmonic field profiles. The mode amplitude attenuation constant α captures both Bragg reflection and radiation loss. For a finite-length structure of length L, you will apply continuity conditions at the vertical boundaries (input and output planes) to obtain the modal reflection coefficient Rp (power reflection) and transmission coefficient Tp. Power quantities are evaluated via the Poynting vector. The solver must accept as inputs the layer refractive indices, thicknesses, grating period, fill factor, length L, and the operating wavelength and polarisation, and return α, Rp, and the complex propagation constants.

Once the solver is implemented, you will use it to run four parameter sweeps:

1. For the air-bridge GaAs filter (parameters: n_c=1, n_r=3.7, n_f=3.7, n_s=1, t_r=0.0 µm, t_f=0.25 µm, t_g=0.25 µm, Λ=0.25 µm, L=20Λ, TE polarisation), sweep wavelength from 1.4 to 1.7 µm and save the α and Rp spectra.
2. For the Si-on-glass TWPBG resonator (n_c=1, n_r=3.45, n_s=1.57, t_g=0.375 µm, L=5.0 µm, TE polarisation), sweep the grating period Λ from 0.2 to 0.3 µm at λ=1.55 µm and save the α curve.
3. For the same resonator at the designed period Λ=0.249 µm, sweep wavelength from 1.4 to 1.7 µm and save the Rp spectrum.
4. For the resonator, compute the complex propagation constants (β + jα) at various wavelengths to populate a Brillouin diagram (β vs wavelength, along with α).

## Reproduction target
Produce four CSV files that completely characterize the two devices:

- `filter_alpha_rp.csv`: Attenuation constant α (µm⁻¹) and reflection coefficient Rp (dimensionless) as functions of wavelength (µm) for the air-bridge GaAs WPBG filter.
- `resonator_alpha_vs_Lambda.csv`: Attenuation constant α (µm⁻¹) as a function of grating period Λ (µm) for the Si-on-glass TWPBG resonator.
- `resonator_Rp_vs_lambda.csv`: Reflection coefficient Rp (dimensionless) as a function of wavelength (µm) for the resonator at Λ=0.249 µm.
- `brillouin_diagram.csv`: Propagation constant β (µm⁻¹), attenuation constant α (µm⁻¹), and wavelength (µm) for Bloch modes of the resonator, with enough points to resolve the band edges.

These artifacts together describe the spectral selectivity and band structure of the designed devices. From the filter spectra, you can identify the location and width of the pass-band; from the resonator α vs period curve, the band-gap edge; from the resonator Rp spectrum, the presence of a resonance dip; and from the Brillouin diagram, the resonant Bloch mode points. The task does not require you to compare your results to the paper's figures; the hidden verifier will do that automatically.

## Assets

- Python scientific computing environment

## Workflow steps

### Step 1: Implement LMP solver
- Role: process
- Action: Implement the Leaky Mode Propagation method: model the multilayer structure (cover, top-cladding, periodic grating layer, waveguiding layer, substrate), expand fields in Floquet harmonics, assemble and solve the differential equation system dF/dx = M·F using Bloch-Floquet phase relations, determine complex propagation constants (β₀ + jα) and field amplitudes, apply vertical boundary conditions (continuity at z=0 and z=L) to obtain reflection coefficient Rp for finite length L, and compute Poynting-vector-based power quantities. The solver must accept layer refractive indices, thicknesses, grating period, fill factor, length L, and wavelength/polarisation as inputs and return complex propagation constants, α, and Rp.
- Evidence: `/app/outputs/lmp_solver_log.txt`

### Step 2: Compute filter α and Rp spectra
- Role: scored (load-bearing)
- Action: Using the LMP solver, compute the attenuation constant α and reflection coefficient Rp for the air-bridge GaAs WPBG filter with parameters: n_c=1, n_r=3.7, n_f=3.7, n_s=1, t_r=0.0 µm, t_f=0.25 µm, t_g=0.25 µm, Λ=0.25 µm, L=20Λ, TE polarisation, over the wavelength range 1.4–1.7 µm. Save the results column-wise: wavelength (µm), alpha (µm⁻¹), Rp (dimensionless).
- Output file: `/app/outputs/filter_alpha_rp.csv`
- Format: csv
- Contract: CSV with columns: wavelength (µm), alpha (µm^-1), Rp (dimensionless). One row per wavelength point.
- Scoring: scored by hidden verifier

### Step 3: Compute resonator α vs period diagram
- Role: scored (load-bearing)
- Action: Using the LMP solver, compute the attenuation constant α for the Si-on-glass TWPBG resonator structure (parameters: n_c=1, n_r=3.45, n_s=1.57, t_g=0.375 µm, L=5.0 µm, TE polarisation) at λ=1.55 µm while varying the grating period Λ from 0.2 to 0.3 µm. Save the results column-wise: Lambda (µm), alpha (µm⁻¹).
- Output file: `/app/outputs/resonator_alpha_vs_Lambda.csv`
- Format: csv
- Contract: CSV with columns: Lambda (µm), alpha (µm^-1). One row per period value.
- Scoring: scored by hidden verifier

### Step 4: Compute resonator Rp spectrum
- Role: scored (load-bearing)
- Action: Using the LMP solver, compute the reflection coefficient Rp for the Si-on-glass TWPBG resonator with the designed period Λ=0.249 µm (other parameters as above: L=5.0 µm, TE polarisation) over the wavelength range 1.4–1.7 µm. Save the results column-wise: wavelength (µm), Rp (dimensionless).
- Output file: `/app/outputs/resonator_Rp_vs_lambda.csv`
- Format: csv
- Contract: CSV with columns: wavelength (µm), Rp (dimensionless). One row per wavelength point.
- Scoring: scored by hidden verifier

### Step 5: Compute Brillouin diagram for the resonator
- Role: scored (load-bearing)
- Action: Using the LMP solver, compute the complex propagation constants (β + jα) for the Si-on-glass TWPBG resonator structure at various wavelengths to produce the Brillouin diagram data. For each allowed Bloch mode, record the real part β (or equivalent propagation constant), the corresponding attenuation constant α, and the wavelength. Provide enough points to resolve the band edges around the resonance condition. Save the results column-wise: beta (µm⁻¹), alpha (µm⁻¹), wavelength (µm).
- Output file: `/app/outputs/brillouin_diagram.csv`
- Format: csv
- Contract: CSV with columns: beta (µm^-1), alpha (µm^-1), wavelength (µm). One row per mode point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/filter_alpha_rp.csv`
- `/app/outputs/resonator_alpha_vs_Lambda.csv`
- `/app/outputs/resonator_Rp_vs_lambda.csv`
- `/app/outputs/brillouin_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### filter_alpha_rp.csv
- path: `/app/outputs/filter_alpha_rp.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Attenuation constant α and reflection coefficient Rp vs wavelength for the air-bridge GaAs WPBG filter. The checker validates that Rp drops below 0.2 and α is below 0.01 µm⁻¹ at the target pass-band wavelength 1.55±0.01 µm.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `alpha`, `Rp`
  - `units`:
    - `wavelength`: µm
    - `alpha`: µm^-1
    - `Rp`: dimensionless

### resonator_alpha_vs_Lambda.csv
- path: `/app/outputs/resonator_alpha_vs_Lambda.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Attenuation constant α vs grating period Λ for the Si-on-glass TWPBG resonator. The checker verifies that α approaches zero at the designed period Λ ≈ 0.249 µm.
- schema:
  - `type`: table
  - `required_columns`: `Lambda`, `alpha`
  - `units`:
    - `Lambda`: µm
    - `alpha`: µm^-1

### resonator_Rp_vs_lambda.csv
- path: `/app/outputs/resonator_Rp_vs_lambda.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Reflection coefficient Rp vs wavelength for the TWPBG resonator at the designed period Λ=0.249 µm. The checker verifies a transmission dip (Rp < 0.2) at the resonance wavelength 1.55 µm.
- schema:
  - `type`: table
  - `required_columns`: `wavelength`, `Rp`
  - `units`:
    - `wavelength`: µm
    - `Rp`: dimensionless

### brillouin_diagram.csv
- path: `/app/outputs/brillouin_diagram.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Brillouin diagram data for the TWPBG resonator. The checker performs a structural audit to confirm that the data contain a band-edge point where α is near zero at the correct wavelength and propagation constant consistent with the designed resonance at λ=1.55 µm and Λ=0.249 µm.
- schema:
  - `type`: table
  - `required_columns`: `beta`, `alpha`, `wavelength`
  - `units`:
    - `beta`: µm^-1
    - `alpha`: µm^-1
    - `wavelength`: µm

Notes: All CSV files must use a header row. Numerical values should be provided with appropriate significant digits. The hidden checker compares the computed curves against reference thresholds and structural features derived from the paper's figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "filter_alpha_rp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "alpha",
          "Rp"
        ],
        "units": {
          "wavelength": "µm",
          "alpha": "µm^-1",
          "Rp": "dimensionless"
        }
      },
      "description": "Attenuation constant α and reflection coefficient Rp vs wavelength for the air-bridge GaAs WPBG filter. The checker validates that Rp drops below 0.2 and α is below 0.01 µm⁻¹ at the target pass-band wavelength 1.55±0.01 µm."
    },
    {
      "file": "resonator_alpha_vs_Lambda.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Lambda",
          "alpha"
        ],
        "units": {
          "Lambda": "µm",
          "alpha": "µm^-1"
        }
      },
      "description": "Attenuation constant α vs grating period Λ for the Si-on-glass TWPBG resonator. The checker verifies that α approaches zero at the designed period Λ ≈ 0.249 µm."
    },
    {
      "file": "resonator_Rp_vs_lambda.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength",
          "Rp"
        ],
        "units": {
          "wavelength": "µm",
          "Rp": "dimensionless"
        }
      },
      "description": "Reflection coefficient Rp vs wavelength for the TWPBG resonator at the designed period Λ=0.249 µm. The checker verifies a transmission dip (Rp < 0.2) at the resonance wavelength 1.55 µm."
    },
    {
      "file": "brillouin_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "beta",
          "alpha",
          "wavelength"
        ],
        "units": {
          "beta": "µm^-1",
          "alpha": "µm^-1",
          "wavelength": "µm"
        }
      },
      "description": "Brillouin diagram data for the TWPBG resonator. The checker performs a structural audit to confirm that the data contain a band-edge point where α is near zero at the correct wavelength and propagation constant consistent with the designed resonance at λ=1.55 µm and Λ=0.249 µm."
    }
  ],
  "notes": "All CSV files must use a header row. Numerical values should be provided with appropriate significant digits. The hidden checker compares the computed curves against reference thresholds and structural features derived from the paper's figures."
}
```

## How you are scored
A hidden verifier independently evaluates each of the four scored artifacts (`filter_alpha_rp.csv`, `resonator_alpha_vs_Lambda.csv`, `resonator_Rp_vs_lambda.csv`, `brillouin_diagram.csv`) and combines their scores into a single reward in [0,1]. The verifier compares your numerical curves to reference data derived from the paper's published results using an appropriate set of tolerances and threshold checks.

- For the filter, the verifier checks whether the Rp spectrum shows a transmission band (low reflection) near 1.55 µm and whether α is small in that region.
- For the resonator, it verifies that α falls to near zero at the designed period Λ≈0.249 µm and that Rp exhibits a deep dip near 1.55 µm.
- The Brillouin diagram is checked for structural consistency with the band-gap edge and the resonance condition.

The four stages carry different weights; the largest weight is on the filter and resonator spectra. Simply hardcoding or reporting expected numbers without running the actual computations will not satisfy the verifier's tolerances. Your goal is to implement the LMP solver correctly and run the sweeps to produce physically correct curves that agree with the reference within the acceptable margin.
