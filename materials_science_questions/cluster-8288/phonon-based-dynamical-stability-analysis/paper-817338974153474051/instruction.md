# Half-Heusler ScRhTe thermoelectric and optical properties under pressure

## Problem background
Half-Heusler compounds are a class of ternary intermetallic phases with good thermoelectric potential for converting waste heat into electricity. ScRhTe is an 18-valence-electron half-Heusler whose structural, electronic, thermoelectric and optical properties, and their response to hydrostatic pressure, are not well established. First-principles calculations can predict these properties, and this task re-computes them to verify whether ScRhTe can serve as a high-performance thermoelectric or optoelectronic material.

## Approach
The core methodology is density functional theory (DFT) with the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation for structural optimization, and a band-gap-corrected exchange-correlation functional (e.g., modified Becke-Johnson) for accurate electronic structure. Spin-orbit coupling (SOC) is included in production band structure calculations. Thermoelectric transport properties are evaluated using the semi-classical Boltzmann transport equation within the constant scattering time approximation, providing the Seebeck coefficient, electrical conductivity per relaxation time, power factor, and electronic thermal conductivity as functions of carrier concentration and temperature. Phonon dispersion curves are computed with a finite-displacement or density-functional perturbation theory approach to judge dynamical stability. Hydrostatic pressure is modeled by isotropically scaling the equilibrium lattice constant; tensile and compressive strain values from -4% to +4% are applied. Optical properties (frequency-dependent dielectric function and absorption coefficient) are obtained from the DFT electronic structure. The workflow builds from one reference geometry optimization, proceeds through equilibrium band-structure and transport calculations, and then systematically explores the property variations under pressure.

## Reproduction target
Compute the following quantities for ScRhTe: (1) equilibrium lattice constant; (2) direct band gap without SOC and with SOC; (3) maximum n-type Seebeck coefficient at 900 K and the carrier concentration at which it occurs; (4) electronic figure of merit ZT_e at a fixed carrier concentration of 10^19 cm^-3. Under hydrostatic pressure (strain values ε = -4%, -2%, 0%, +2%, +4%): determine (5) dynamical stability from phonons (stable/unstable per strain); (6) band gap (eV) and gap type (direct/indirect) for each strain; (7) Seebeck coefficient and ZT_e for n-type doping at 10^19 cm^-3 at 300 K for each strain. Finally, (8) for ε = 0% and ε = +4%, extract the absorption coefficient at 307 nm. Write the compiled results to /app/outputs/results_summary.json and the stability summary to /app/outputs/phonon_stability.txt as detailed in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP: https://www.boltzTrap.org/
- Phonopy: https://phonopy.github.io/phonopy/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Perform structural relaxation of ScRhTe in the cubic F-43m space group (Wyckoff positions: Sc 4c (0.25,0.25,0.25), Rh 4b (0.5,0.5,0.5), Te 4a (0.0,0.0,0.0)) using a DFT planewave/pseudopotential code with PBE-GGA. Determine the equilibrium lattice constant via total-energy minimization.
- Evidence: `/app/outputs/lattice_opt.log`

### Step 2: Band structure without SOC
- Role: process
- Action: Using the optimized lattice constant, compute the band structure and projected density of states with a band-gap-corrected exchange-correlation functional (e.g., mBJ or equivalent) without spin-orbit coupling. Record the direct band gap at the Gamma point.
- Evidence: `/app/outputs/band_noSOC.dat`

### Step 3: Band structure with SOC
- Role: process
- Action: Repeat the band structure calculation including spin-orbit coupling (SOC). Determine the SOC-corrected band gap and the spin-orbit splitting at the valence band maximum.
- Evidence: `/app/outputs/band_SOC.dat`

### Step 4: Thermoelectric properties at equilibrium
- Role: process
- Action: Using the SOC band structure, run a Boltzmann transport code (e.g., BoltzTraP) under constant scattering time approximation. Compute Seebeck coefficient, electrical conductivity per relaxation time, power factor, and electronic ZT for n-type doping as functions of carrier concentration (10^18 to 10^21 cm^-3) and temperature (300, 600, 900, 1200 K). Extract the maximum n-type Seebeck coefficient at 900 K and its corresponding carrier concentration, and the ZT_e at 10^19 cm^-3.
- Evidence: `/app/outputs/te_equilibrium.dat`

### Step 5: Phonon stability under pressure
- Role: scored
- Action: For strains ε = -4%, -2%, 0%, 2%, 4% (lattice constant scaled accordingly), compute phonon dispersion curves using a finite-displacement or DFPT method (e.g., Phonopy). Determine dynamical stability by checking for imaginary modes. Write a file phonon_stability.txt containing one line per strain in the format 'ε = <strain>%: stable' if no imaginary modes, else 'unstable'.
- Output file: `/app/outputs/phonon_stability.txt`
- Format: txt
- Contract: One line per strain, e.g., 'ε = -4%: stable'
- Scoring: scored by hidden verifier

### Step 6: Electronic structure under pressure
- Role: process
- Action: For each strain ε = -4%, -2%, 0%, 2%, 4%, compute the band structure using the SOC-corrected method. Determine the band gap (eV) and whether the gap is direct or indirect.
- Evidence: `/app/outputs/band_gaps_pressure.dat`

### Step 7: Thermoelectric properties under pressure
- Role: process
- Action: For each strain, compute the Seebeck coefficient and ZT_e for n-type doping at a fixed carrier concentration of 10^19 cm^-3 (using Boltzmann transport on the pressure-dependent band structures).
- Evidence: `/app/outputs/te_pressure.dat`

### Step 8: Optical properties under pressure
- Role: process
- Action: For ε = 0% and ε = +4%, compute the frequency-dependent dielectric function and absorption coefficient using an optics module of the DFT code. Extract the absorption coefficient at 307 nm.
- Evidence: `/app/outputs/optical_data.dat`

### Step 9: Compile final results
- Role: scored (load-bearing)
- Action: Gather all required quantities from the previous calculations and write a JSON file results_summary.json with fields: lattice_constant_A (float), bandgap_noSOC_eV (float), bandgap_SOC_eV (float), max_Seebeck_n900K_uVK (float), optimal_carrier_concentration_cm3 (float), ZT_e_at_1e19_cm3 (float), and pressure_results (array of objects, one per strain ε = '-4%','-2%','0%','2%','4%'), each with fields strain, bandgap_eV, bandgap_type ('direct' or 'indirect'), Seebeck_n1e19_300K_uVK (float), ZT_e (float), absorption_307nm_cm1 (float; null for strains where not computed). Ensure correct units.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: {"lattice_constant_A": float, "bandgap_noSOC_eV": float, "bandgap_SOC_eV": float, "max_Seebeck_n900K_uVK": float, "optimal_carrier_concentration_cm3": float, "ZT_e_at_1e19_cm3": float, "pressure_results": [{"strain": string, "bandgap_eV": float, "bandgap_type": string, "Seebeck_n1e19_300K_uVK": float, "ZT_e": float, "absorption_307nm_cm1": float|null}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_stability.txt`
- `/app/outputs/results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_stability.txt
- path: `/app/outputs/phonon_stability.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Declares the dynamical stability of ScRhTe at each applied strain based on the absence of imaginary phonon modes.
- schema:
  - `type`: text
  - `description`: One line per strain in format 'ε = <strain>%: stable' or 'unstable'

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated key properties of ScRhTe at equilibrium and under pressure, to be compared against paper-reported values with tolerances and trend checks.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: float
    - `bandgap_noSOC_eV`: float
    - `bandgap_SOC_eV`: float
    - `max_Seebeck_n900K_uVK`: float
    - `optimal_carrier_concentration_cm3`: float
    - `ZT_e_at_1e19_cm3`: float
    - `pressure_results`: array of objects
  - `items`:
    - `pressure_results`:
      - `strain`: string
      - `bandgap_eV`: float
      - `bandgap_type`: string
      - `Seebeck_n1e19_300K_uVK`: float
      - `ZT_e`: float
      - `absorption_307nm_cm1`: float or null

Notes: The checker compares the phonon_stability.txt lines to expected stability (all strains stable). For results_summary.json, each field is compared to the hidden gold with appropriate tolerances; the absorption coefficient at +4% must be larger than at 0% (trend).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_stability.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "One line per strain in format 'ε = <strain>%: stable' or 'unstable'"
      },
      "description": "Declares the dynamical stability of ScRhTe at each applied strain based on the absence of imaginary phonon modes."
    },
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "float",
          "bandgap_noSOC_eV": "float",
          "bandgap_SOC_eV": "float",
          "max_Seebeck_n900K_uVK": "float",
          "optimal_carrier_concentration_cm3": "float",
          "ZT_e_at_1e19_cm3": "float",
          "pressure_results": "array of objects"
        },
        "items": {
          "pressure_results": {
            "strain": "string",
            "bandgap_eV": "float",
            "bandgap_type": "string",
            "Seebeck_n1e19_300K_uVK": "float",
            "ZT_e": "float",
            "absorption_307nm_cm1": "float or null"
          }
        }
      },
      "description": "Aggregated key properties of ScRhTe at equilibrium and under pressure, to be compared against paper-reported values with tolerances and trend checks."
    }
  ],
  "notes": "The checker compares the phonon_stability.txt lines to expected stability (all strains stable). For results_summary.json, each field is compared to the hidden gold with appropriate tolerances; the absorption coefficient at +4% must be larger than at 0% (trend)."
}
```

## How you are scored
A hidden verifier scores your submission by comparing phonon_stability.txt and results_summary.json to reference results derived from the original study. Each numerical entry is checked with tolerances appropriate for a reproduction performed with a different DFT package and transport code. Relative trends between strains (e.g., band gap monotonicity, absorption coefficient change between 0% and +4% strain) are verified. The stability conclusions are compared to expected behavior. The total reward (0 to 1) is a weighted sum of partial scores from the individual contracts, with the main equilibrium properties and the pressure-dependent results each carrying substantial weight. Simply reporting values that match the paper's reported numbers without running the actual calculations is insufficient.
