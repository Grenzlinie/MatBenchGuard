# Thermoelectric Transport Modeling of Doped β-Zn₄Sb₃: Seebeck Enhancement via Resonant DOS

## Problem background
Thermoelectric materials convert waste heat into electricity, and their efficiency is measured by the dimensionless figure of merit ZT = S²σT / λ. β‑Zn₄Sb₃ is a promising mid‑temperature thermoelectric with ZT ≈ 1.3 at 670 K, but its relatively low Seebeck coefficient (around 100 μV/K at room temperature) limits performance. Doping with 3d transition elements (Fe, Co, Ni) is hypothesized to introduce sharp resonant peaks in the electronic density of states near the band edges, which could dramatically increase the Seebeck coefficient via the Mott formula. This computational study investigates the electronic structure and thermoelectric transport properties of Fe‑, Co‑, and Ni‑doped β‑Zn₄Sb₃ to quantify the achievable Seebeck enhancement and the resulting improvement in the thermoelectric figure of merit.

## Approach
The approach combines first‑principles electronic structure calculations with Boltzmann transport theory. Density functional theory (DFT) calculations are performed on a Zn₃₆Sb₃₀ supercell (undoped host) and on three doped supercells where one Zn is substituted by Fe, Co, or Ni (MZn₃₅Sb₃₀). The total density of states g(E) is obtained, and the DOS of the doped systems is aligned to that of the undoped host by matching core bands, so that resonant features introduced by the 3d states can be identified. Using the DFT‑computed g(E), the Boltzmann transport equation is solved within the relaxation‑time approximation. The relaxation time τ(E) is constructed via Matthiessen’s rule from contributions due to polar optical phonon scattering, optical deformation potential scattering, and acoustic deformation potential scattering; the required material parameters (deformation potentials, effective mass, permittivities, phonon frequency, etc.) are taken from literature values. The transport kernels L^(a) are integrated over energy at a range of Fermi levels spanning the band edges, yielding the Seebeck coefficient S, electrical conductivity σ, and carrier thermal conductivity λ_C as functions of carrier concentration n at 300 K. The power factor PF = S²σ and the thermoelectric figure of merit ZT = S²σT / (λ_C + λ_L) are then evaluated, assuming a constant lattice thermal conductivity λ_L = 0.6 W/m·K. The complete transport curves for all four systems are compared to extract the enhancement factors relative to the undoped case.

## Reproduction target
Compute the room‑temperature (T = 300 K) thermoelectric transport quantities — Seebeck coefficient S, electrical conductivity σ, carrier thermal conductivity λ_C, power factor PF, and figure of merit ZT — as functions of carrier concentration n for the undoped Zn₃₆Sb₃₀ host and for the Fe‑, Co‑, and Ni‑doped MZn₃₅Sb₃₀ systems. From these curves, extract for each dopant: the maximum Seebeck coefficient value and the carrier concentration at which it occurs; the Seebeck enhancement factor, defined as the ratio of the maximum doped Seebeck coefficient to the undoped Seebeck coefficient at a comparable carrier concentration; the peak ZT value; and the ZT enhancement factor relative to the undoped maximum ZT. Also report the undoped peak ZT. Additionally, examine whether the Seebeck coefficient changes sign at low carrier concentrations for each doped system, and determine the relative ordering of the Seebeck enhancements among the dopants.

## Assets

- Quantum ESPRESSO (or ABINIT): https://www.quantum-espresso.org/
- PBE PAW pseudopotentials: https://www.quantum-espresso.org/pseudopotentials/
- Crystal structure of Zn₃₆Sb₃₀ (Cargnoni model): 10.1002/chem.200400050
- Literature experimental transport data of pristine β-Zn₄Sb₃ (optional): 10.1016/S0022-3697(96)00228-4
- Python scientific stack: numpy scipy matplotlib
- BoltzTraP2 (optional BTE solver): https://www.boltztrap.org/

## Workflow steps

### Step 1: DFT electronic structure and DOS computation
- Role: process
- Action: Perform density functional theory electronic structure calculations for the Zn₃₆Sb₃₀ supercell (undoped) and for the three doped supercells MZn₃₅Sb₃₀ (M=Fe, Co, Ni). Use an open-source DFT code (e.g., Quantum ESPRESSO) with PBE PAW pseudopotentials. Relax the structures and compute the total density of states g(E) and band structure. Align the DOS of the doped systems to the undoped host by matching core bands and identify the resonant DOS peaks introduced by the transition-metal d-states. Output the processed DOS for each system.
- Evidence: `/app/outputs/dos_data_summary.json`

### Step 2: Obtain relaxation-time scattering parameters
- Role: process
- Action: Obtain the material-specific scattering parameters needed for the relaxation time approximation. Use the published values from the paper's Table 1 directly (deformation potentials E_ac = 30 eV, E_oc = 30 eV; elastic constant C_l = 8.1968×10¹⁰ N/m²; density-of-states effective mass m* = 0.9 m_e; static permittivity ε_0 = 25.6410×ε₀; optical phonon frequency ω_0 = 2.06×10¹³ s⁻¹; and literature values for band gap E_g = 1.2 eV, lattice constant a = 12.231 Å, density ρ = 6077 kg/m³, high-frequency permittivity ε_∞ = 21×ε₀). The agent may optionally refit these parameters to published experimental transport data of pristine β-Zn₄Sb₃, but using the listed values directly is acceptable. Store the final parameter set for use in the transport calculation.
- Evidence: `/app/outputs/scattering_parameters.json`

### Step 3: Boltzmann transport simulation — transport curves
- Role: scored (load-bearing)
- Action: Compute the room-temperature (T=300 K) Seebeck coefficient S, electrical conductivity σ, carrier thermal conductivity λ_C as functions of carrier concentration n for the undoped Zn₃₆Sb₃₀ system and for the Fe-, Co-, and Ni-doped MZn₃₅Sb₃₀ systems. Use the Boltzmann transport equation within the relaxation time approximation, combining the DFT-computed density of states g(E) for each system with the relaxation time τ(E) obtained from Matthiessen's rule applied to the three scattering mechanisms (polar optical phonon, optical deformation potential, acoustic deformation potential). Integrate the transport kernels L^(a) over energy to obtain S, σ, and λ_C at a range of Fermi energies spanning the band edges; convert to carrier concentration n. Compute the power factor PF = S²σ and the thermoelectric figure of merit ZT = S²σT/(λ_C + λ_L) assuming a constant lattice thermal conductivity λ_L = 0.6 W/m·K. Output the full S(n), σ(n), λ_C(n), PF(n), and ZT(n) curves for all four systems at a sufficiently dense set of carrier concentrations to resolve the peak features.
- Output file: `/app/outputs/transport_results.csv`
- Format: csv
- Contract: CSV with columns: system (string, one of: undoped, Fe, Co, Ni), carrier_concentration (float, m⁻³), Seebeck_coefficient (float, μV/K), electrical_conductivity (float, S/m), power_factor (float, W/m·K²), carrier_thermal_conductivity (float, W/m·K), ZT (float, dimensionless). One row per carrier concentration per system.
- Scoring: scored by hidden verifier

### Step 4: Extract doping enhancement factors and key metrics
- Role: scored
- Action: From the transport_results.csv curves, extract for each doped system (Fe, Co, Ni): the maximum Seebeck coefficient value and the carrier concentration at which it occurs; the Seebeck enhancement factor defined as the ratio of the maximum doped Seebeck coefficient to the undoped Seebeck coefficient at the same carrier concentration (or the ratio of maximum values if the peaks do not coincide); the peak power factor value; the maximum ZT value and the carrier concentration at which it occurs; and the ZT enhancement factor relative to the undoped maximum ZT. Also report the undoped peak ZT value for reference.
- Output file: `/app/outputs/enhancement_factors.json`
- Format: json
- Contract: JSON object with keys: 'undoped' (containing peak_ZT: float), and for each dopant 'Fe', 'Co', 'Ni' containing: max_Seebeck_raw (float, μV/K), carrier_concentration_at_max_S (float, m⁻³), max_Seebeck_enhancement (float, dimensionless ratio relative to undoped at comparable n), peak_ZT (float), ZT_enhancement (float, ratio relative to undoped peak_ZT).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transport_results.csv`
- `/app/outputs/enhancement_factors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transport_results.csv
- path: `/app/outputs/transport_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Full transport curves (S, σ, λ_C, PF, ZT) vs. carrier concentration for undoped, Fe, Co, Ni at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `system`, `carrier_concentration`, `Seebeck_coefficient`, `electrical_conductivity`, `power_factor`, `carrier_thermal_conductivity`, `ZT`
  - `units`:
    - `carrier_concentration`: m^-3
    - `Seebeck_coefficient`: μV/K
    - `electrical_conductivity`: S/m
    - `power_factor`: W/m·K^2
    - `carrier_thermal_conductivity`: W/m·K
    - `ZT`: dimensionless
  - `rows_per_system`: at least 50

### enhancement_factors.json
- path: `/app/outputs/enhancement_factors.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extracted maximum Seebeck enhancement factors and ZT improvements for each dopant, compared to paper-reported hidden gold values.
- schema:
  - `type`: object
  - `required`: `undoped`, `Fe`, `Co`, `Ni`
  - `properties`:
    - `undoped`:
      - `type`: object
      - `required`: `peak_ZT`
    - `Fe`:
      - `type`: object
      - `required`: `max_Seebeck_raw`, `carrier_concentration_at_max_S`, `max_Seebeck_enhancement`, `peak_ZT`, `ZT_enhancement`
    - `Co`:
      - `type`: object
      - `required`: `max_Seebeck_raw`, `carrier_concentration_at_max_S`, `max_Seebeck_enhancement`, `peak_ZT`, `ZT_enhancement`
    - `Ni`:
      - `type`: object
      - `required`: `max_Seebeck_raw`, `carrier_concentration_at_max_S`, `max_Seebeck_enhancement`, `peak_ZT`, `ZT_enhancement`
  - `units`:
    - `max_Seebeck_raw`: μV/K
    - `carrier_concentration_at_max_S`: m^-3
    - `max_Seebeck_enhancement`: dimensionless
    - `peak_ZT`: dimensionless
    - `ZT_enhancement`: dimensionless

Notes: The checker recomputes enhancement factors and trends from transport_results.csv and compares them to hidden gold values (paper-reported numbers) with tolerances. The enhancement_factors.json provides the agent's self-reported factors for reference match (T0), but the primary scoring uses the recomputed quantities (T1).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transport_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "carrier_concentration",
          "Seebeck_coefficient",
          "electrical_conductivity",
          "power_factor",
          "carrier_thermal_conductivity",
          "ZT"
        ],
        "units": {
          "carrier_concentration": "m^-3",
          "Seebeck_coefficient": "μV/K",
          "electrical_conductivity": "S/m",
          "power_factor": "W/m·K^2",
          "carrier_thermal_conductivity": "W/m·K",
          "ZT": "dimensionless"
        },
        "rows_per_system": "at least 50"
      },
      "description": "Full transport curves (S, σ, λ_C, PF, ZT) vs. carrier concentration for undoped, Fe, Co, Ni at 300 K."
    },
    {
      "file": "enhancement_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "undoped",
          "Fe",
          "Co",
          "Ni"
        ],
        "properties": {
          "undoped": {
            "type": "object",
            "required": [
              "peak_ZT"
            ]
          },
          "Fe": {
            "type": "object",
            "required": [
              "max_Seebeck_raw",
              "carrier_concentration_at_max_S",
              "max_Seebeck_enhancement",
              "peak_ZT",
              "ZT_enhancement"
            ]
          },
          "Co": {
            "type": "object",
            "required": [
              "max_Seebeck_raw",
              "carrier_concentration_at_max_S",
              "max_Seebeck_enhancement",
              "peak_ZT",
              "ZT_enhancement"
            ]
          },
          "Ni": {
            "type": "object",
            "required": [
              "max_Seebeck_raw",
              "carrier_concentration_at_max_S",
              "max_Seebeck_enhancement",
              "peak_ZT",
              "ZT_enhancement"
            ]
          }
        },
        "units": {
          "max_Seebeck_raw": "μV/K",
          "carrier_concentration_at_max_S": "m^-3",
          "max_Seebeck_enhancement": "dimensionless",
          "peak_ZT": "dimensionless",
          "ZT_enhancement": "dimensionless"
        }
      },
      "description": "Extracted maximum Seebeck enhancement factors and ZT improvements for each dopant, compared to paper-reported hidden gold values."
    }
  ],
  "notes": "The checker recomputes enhancement factors and trends from transport_results.csv and compares them to hidden gold values (paper-reported numbers) with tolerances. The enhancement_factors.json provides the agent's self-reported factors for reference match (T0), but the primary scoring uses the recomputed quantities (T1)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that processes the two scored artifacts. For `/app/outputs/transport_results.csv`, the verifier recomputes the Seebeck enhancement factors, ZT enhancement factors, and the carrier concentration ranges where S changes sign directly from the tabulated curves. These recomputed quantities, as well as the values reported in `/app/outputs/enhancement_factors.json`, are compared against hidden reference values from the published study, with tolerances that accommodate legitimate differences due to DFT implementation and numerical discretization. The verifier also checks that the enhancement factors extracted from the CSV are internally consistent with the JSON summary, and that qualitative trends (e.g., the ordering of enhancements among Fe, Co, and Ni, and the sign‑change behavior) are physically plausible. The overall reward is the weighted sum of the scores from each artifact, with the transport curves carrying the majority of the weight. Simply reporting a number that matches a reference without a coherent transport curve will not yield a high score.
