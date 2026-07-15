# Monte Carlo Simulation of Coupled Charge Layers in Insulators

## Problem background
When a focused electron beam irradiates an insulating material such as SiO₂, primary electrons penetrate and generate secondary electrons, leaving behind a complex spatial distribution of trapped positive and negative charges. Understanding this nanoscale trapped‑charge distribution is important for scanning electron microscopy and dielectric reliability. In this work, a comprehensive time‑stepping Monte Carlo simulation that couples electron transport, electric‑field effects, charge drift, trapping/detrapping, and field‑assisted detrapping is used to predict the steady‑state trapped‑charge profile and the evolution of the surface potential. Your task is to re‑implement this coupled charging model and compute the resulting trapped‑charge density along the beam axis and the surface‑potential time series for two primary electron energies.

## Approach
Implement the full time‑stepping Monte Carlo simulation for electron‑beam‑induced charging in semi‑infinite SiO₂. Electron transport is treated with Mott elastic scattering (Thomas‑Fermi‑Dirac potential, partial‑wave expansion), dielectric‑function‑based inelastic scattering (Lorentz oscillators with a band‑gap cutoff of 8.9 eV), and LO‑phonon interactions (energies 0.063 eV and 0.153 eV) for low‑energy electrons. Electric‑field effects on particle trajectories and kinetic energies are included. Deposited electrons and holes drift under the local electric field: electron drift velocity is linear with mobility μₑ = 20 cm²/V·s up to 0.7 MV/cm, then saturates at 1.4×10⁷ cm/s; hole drift uses a constant mobility μₕ = 2×10⁻⁵ cm²/V·s. Charged particles may be trapped at sites with a Gaussian trap‑depth distribution (mean 1.5 eV, σ = 1.0 eV) and uniform spatial density. Trapping cross sections are σₑ₀ = 10⁻¹⁴ cm² (electron on empty), σₑₕ = 5×10⁻¹³ cm² for fields below 0.5 MV/cm or a field‑dependent formula above, σₕ₀ = 3×10⁻¹⁴ cm², σₕₑ = 3×10⁻¹³ cm². Secondary electrons in the near‑surface region (depth < 15 nm, energy < 3.5 eV) trap with cross sections σₑ₀* = 5×10⁻¹⁵ cm² and σₑₕ* = 10⁻¹³ cm². Field‑assisted detrapping is modeled via a barrier‑lowering formula with the relative dielectric constant εᵣ = 3.9. The electrostatic potential is computed by the mono‑image‑charge method on a non‑uniform grid over a cuboid centered at the beam spot. The simulation uses known SiO₂ properties: electron affinity 0.9 eV, static dielectric constant 3.9, optical dielectric constant 2.25. Run the model with a primary beam current of 0.1 nA, beam diameter 0.1 μm, trap density 2×10⁹ cm⁻³, and primary energies of 5 keV and 10 keV, each until the surface potential reaches steady state. The computed outputs are the steady‑state trapped‑charge density along the beam axis (x = y = 0) and the full surface‑potential time series for both energies.

## Reproduction target
Run the Monte Carlo simulation for primary energies 5 keV and 10 keV with the parameters above, until the surface potential stops changing (steady state). For each energy, save two CSV files: (1) the steady‑state net trapped‑charge density along the beam axis (columns: depth in nanometres `z_nm`, negative inside the sample, and `net_charge_density` in arbitrary units); (2) the evolution of the surface potential (columns: `time_ms` in milliseconds and `surface_potential_V` in volts). The trapped‑charge profile must exhibit multiple alternating sign layers (at least five distinct layers) with the first layer being positive. The surface‑potential time series must converge to a saturated negative value, consistent with the deceleration of incoming primary electrons by the negative surface field.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement the coupled Monte Carlo charging model
- Role: process
- Action: Code the full time-stepping Monte Carlo simulation for electron-beam-induced charging in a semi-infinite SiO₂ sample. The model must include: electron transport with Mott elastic scattering, dielectric-function-based inelastic scattering (Lorentz oscillators, bandgap cutoff 8.9 eV), LO-phonon interactions for low-energy electrons; electric-field effects on particle trajectories and energies; charge drift of deposited electrons and holes under the local field using field-dependent electron drift velocity and constant hole mobility; trapping into sites with a Gaussian trap-depth distribution (mean 1.5 eV, σ=1.0 eV) using the specified cross sections (including field-dependent cross section for drift electrons onto hole-occupied traps); secondary-electron trapping in the near-surface region; field-assisted detrapping; potential update via the mono-image-charge method on a non-uniform grid. Use known SiO₂ properties: electron affinity 0.9 eV, static dielectric constant 3.9, optical dielectric constant 2.25, phonon energies 0.063 eV and 0.153 eV. The simulation must accept beam energy, current, diameter, and trap density as inputs.
- Evidence: none

### Step 2: Run 5 keV simulation to steady state
- Role: process
- Action: Execute the implemented Monte Carlo simulation for a primary electron beam of 5 keV, beam current 0.1 nA, beam diameter 0.1 μm, trap density 2×10⁹ cm⁻³, and all other parameters as specified in the model. Run until the surface potential reaches a steady state (gradient negligible). Store the simulation outputs (including the final trapped charge distribution and the surface potential time series) for subsequent extraction.
- Evidence: none

### Step 3: Extract trapped charge profile for 5 keV
- Role: scored (load-bearing)
- Action: From the steady-state simulation of step2, extract the net trapped charge density along the beam axis (x=y=0) and save it as trapped_charge_profile_5keV.csv.
- Output file: `/app/outputs/trapped_charge_profile_5keV.csv`
- Format: csv
- Contract: CSV with two columns: z_nm (float, depth in nanometres, negative inside the sample), net_charge_density (float, net trapped charge density in arbitrary units).
- Scoring: scored by hidden verifier

### Step 4: Extract surface potential time series for 5 keV
- Role: scored
- Action: From the 5 keV simulation of step2, extract the full surface potential evolution and save it as surface_potential_time_series_5keV.csv.
- Output file: `/app/outputs/surface_potential_time_series_5keV.csv`
- Format: csv
- Contract: CSV with two columns: time_ms (float, time in milliseconds), surface_potential_V (float, surface potential in volts).
- Scoring: scored by hidden verifier

### Step 5: Run 10 keV simulation to steady state
- Role: process
- Action: Repeat the Monte Carlo simulation for primary energy 10 keV, using otherwise identical parameters, until the surface potential reaches a steady state. Store the simulation outputs.
- Evidence: none

### Step 6: Extract trapped charge profile for 10 keV
- Role: scored (load-bearing)
- Action: From the steady-state simulation of step5, extract the net trapped charge density along the beam axis and save as trapped_charge_profile_10keV.csv.
- Output file: `/app/outputs/trapped_charge_profile_10keV.csv`
- Format: csv
- Contract: CSV with two columns: z_nm (float, depth in nanometres, negative inside the sample), net_charge_density (float, net trapped charge density in arbitrary units).
- Scoring: scored by hidden verifier

### Step 7: Extract surface potential time series for 10 keV
- Role: scored
- Action: From the 10 keV simulation of step5, extract the full surface potential evolution and save as surface_potential_time_series_10keV.csv.
- Output file: `/app/outputs/surface_potential_time_series_10keV.csv`
- Format: csv
- Contract: CSV with two columns: time_ms (float, time in milliseconds), surface_potential_V (float, surface potential in volts).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trapped_charge_profile_5keV.csv`
- `/app/outputs/surface_potential_time_series_5keV.csv`
- `/app/outputs/trapped_charge_profile_10keV.csv`
- `/app/outputs/surface_potential_time_series_10keV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trapped_charge_profile_5keV.csv
- path: `/app/outputs/trapped_charge_profile_5keV.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady-state net trapped charge density along the beam incidence axis (x=y=0) for 5 keV primary electrons.
- schema:
  - `type`: table
  - `required_columns`: `z_nm`, `net_charge_density`
  - `units`:
    - `z_nm`: nanometres
    - `net_charge_density`: arbitrary units

### surface_potential_time_series_5keV.csv
- path: `/app/outputs/surface_potential_time_series_5keV.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Evolution of the sample surface potential under 5 keV electron irradiation until steady state.
- schema:
  - `type`: table
  - `required_columns`: `time_ms`, `surface_potential_V`
  - `units`:
    - `time_ms`: milliseconds
    - `surface_potential_V`: volts

### trapped_charge_profile_10keV.csv
- path: `/app/outputs/trapped_charge_profile_10keV.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady-state net trapped charge density along the beam axis for 10 keV primary electrons.
- schema:
  - `type`: table
  - `required_columns`: `z_nm`, `net_charge_density`
  - `units`:
    - `z_nm`: nanometres
    - `net_charge_density`: arbitrary units

### surface_potential_time_series_10keV.csv
- path: `/app/outputs/surface_potential_time_series_10keV.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Evolution of the sample surface potential under 10 keV electron irradiation until steady state.
- schema:
  - `type`: table
  - `required_columns`: `time_ms`, `surface_potential_V`
  - `units`:
    - `time_ms`: milliseconds
    - `surface_potential_V`: volts

Notes: The checker will verify the alternating charge layer structure (counting sign changes) for the trapped charge profiles and check that the final surface potential falls within expected ranges and that the potential has saturated.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trapped_charge_profile_5keV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_nm",
          "net_charge_density"
        ],
        "units": {
          "z_nm": "nanometres",
          "net_charge_density": "arbitrary units"
        }
      },
      "description": "Steady-state net trapped charge density along the beam incidence axis (x=y=0) for 5 keV primary electrons."
    },
    {
      "file": "surface_potential_time_series_5keV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ms",
          "surface_potential_V"
        ],
        "units": {
          "time_ms": "milliseconds",
          "surface_potential_V": "volts"
        }
      },
      "description": "Evolution of the sample surface potential under 5 keV electron irradiation until steady state."
    },
    {
      "file": "trapped_charge_profile_10keV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "z_nm",
          "net_charge_density"
        ],
        "units": {
          "z_nm": "nanometres",
          "net_charge_density": "arbitrary units"
        }
      },
      "description": "Steady-state net trapped charge density along the beam axis for 10 keV primary electrons."
    },
    {
      "file": "surface_potential_time_series_10keV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ms",
          "surface_potential_V"
        ],
        "units": {
          "time_ms": "milliseconds",
          "surface_potential_V": "volts"
        }
      },
      "description": "Evolution of the sample surface potential under 10 keV electron irradiation until steady state."
    }
  ],
  "notes": "The checker will verify the alternating charge layer structure (counting sign changes) for the trapped charge profiles and check that the final surface potential falls within expected ranges and that the potential has saturated."
}
```

## How you are scored
Your outputs will be evaluated by a hidden verifier that checks each required CSV file. For the trapped‑charge profiles, the verifier counts sign changes in the net charge density along depth to verify the alternating‑layer structure (the first layer must be positive, and several sign reversals must be present). For the surface‑potential time series, it confirms that the potential has converged (the gradient over the last portion is small) and that the final value lies in the expected negative range. The final reward is a weighted combination of these checks; both energies contribute, with the layer‑structure analysis carrying the largest weight.
