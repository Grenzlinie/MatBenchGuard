# Computation of thermodynamic properties and transport coefficients for C6F12O plasma

## Problem background
C₆F₁₂O is a promising environmentally‑friendly insulating gas for high‑voltage equipment. Its thermodynamic properties and transport coefficients (electrical conductivity, thermal conductivity) are needed to evaluate breakdown and interruption performance. This task computes those properties under local thermodynamic equilibrium (LTE) at 0.1 MPa from 300 K to 30 000 K.

## Approach
The computation builds internal partition functions for all particle species that can appear in the plasma (monatomic, diatomic, and polyatomic). The chemical equilibrium is solved by combining the Saha ionization equation, Guldberg‑Waage dissociation equation, Dalton’s law of partial pressures, atomic conservation, and electric neutrality. The resulting nonlinear system is solved with a Newton iteration to give the number density of every species as a function of temperature. From the number densities, standard thermodynamic relations yield the mass density, enthalpy, entropy, specific heat at constant pressure, and sound velocity. Transport coefficients are then computed using the Chapman‑Enskog expansion of the Boltzmann equation. The electrical conductivity of C₆F₁₂O, CO₂, and N₂ is obtained by the third‑order Chapman‑Enskog approximation; the total thermal conductivity of C₆F₁₂O is obtained as the sum of heavy‑particle, electron, internal, and reaction contributions, with the reaction contribution evaluated via Butler‑Brokaw theory. Required spectroscopic data are taken from public databases (NIST, JANAF) and supplemented with DFT calculations for the larger polyatomic species, which provide vibrational frequencies, rotational constants, and Lennard‑Jones parameters.

## Reproduction target
Compute and output the following for C₆F₁₂O at 0.1 MPa over 300–30 000 K:

1. Number densities of all species (composition.csv).
2. Thermodynamic properties: enthalpy, entropy, specific heat, and sound velocity (thermodynamic_properties.csv).
3. Electrical conductivity of C₆F₁₂O, CO₂, and N₂ as functions of temperature (electrical_conductivity.csv).
4. Total thermal conductivity of C₆F₁₂O as a function of temperature (thermal_conductivity.csv).

The verifier will assess structural validity (conductivity ordering and thermal conductivity peak locations) according to the output contract.

## Assets

- NIST Atomic Spectra Database: https://www.nist.gov/pml/atomic-spectra-database
- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Open-source quantum chemistry package (e.g. ORCA, NWChem): https://orcaforum.kofo.mpg.de/ or https://www.nwchem-sw.org/
- Physical constants (electron mass, Boltzmann constant, Planck constant)

## Workflow steps

### Step 1: DFT calculation of missing spectroscopic and collision-integral parameters
- Role: process
- Action: Build molecular geometries for the macromolecules: CF4O, C4F8O, C4F10O, C2F6O, C3F6O, C5F8, C5F10, C5F10O, C6F12O. Perform DFT geometry optimization and vibrational frequency analysis using an open-source quantum chemistry package (e.g., ORCA or NWChem). Compute vibrational frequencies, rotational constants, products of inertia, and Lennard-Jones parameters (epsilon/kb, polarizability). Save the parameters in a structured file.
- Evidence: `/app/outputs/dft_parameters.json`

### Step 2: LTE composition and number densities
- Role: scored
- Action: Using the DFT parameters from step_01, NIST atomic data, and JANAF data, build internal partition functions for all 59 species (monatomic, diatomic, polyatomic particles including C6F12O, CO2, N2 and their decomposition/ionization products). Set up and solve the Saha ionization, Guldberg-Waage dissociation, Dalton's law, atomic conservation, and electric neutrality equations via Newton iteration at 0.1 MPa over 300–30000 K for C6F12O, CO2, and N2. Output the number density of every species vs. temperature in m^-3.
- Output file: `/app/outputs/composition.csv`
- Format: csv
- Contract: Columns: Temperature (K), then one column per species (e.g., C, C+, O, F, C2, ...). Unit: m^-3.
- Scoring: scored by hidden verifier

### Step 3: Thermodynamic properties (enthalpy, entropy, specific heat, sound velocity)
- Role: scored
- Action: From the number densities and partition functions, compute mass density, enthalpy, entropy, specific heat at constant pressure, and sound velocity for C6F12O at 0.1 MPa over 300–30000 K using standard thermodynamic relations. Output the properties vs. temperature.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: Columns: Temperature (K), Enthalpy (kJ/kg), Entropy (kJ/(kg·K)), SpecificHeat (J/(kg·K)), SoundVelocity (m/s).
- Scoring: scored by hidden verifier

### Step 4: Electrical conductivity of C6F12O, CO2, and N2
- Role: scored (load-bearing)
- Action: Using the number densities and collision-integral data (from DFT and literature), compute the electrical conductivity of C6F12O, CO2, and N2 at 0.1 MPa over 300–30000 K using the Chapman-Enskog third-order approximation. Output the three conductivity curves in S/m vs. temperature.
- Output file: `/app/outputs/electrical_conductivity.csv`
- Format: csv
- Contract: Columns: Temperature (K), Conductivity_C6F12O (S/m), Conductivity_CO2 (S/m), Conductivity_N2 (S/m).
- Scoring: scored by hidden verifier

### Step 5: Total thermal conductivity of C6F12O
- Role: scored (load-bearing)
- Action: Using the number densities and collision integrals, compute the total thermal conductivity of C6F12O (sum of heavy-particle, electron, internal, and reaction contributions) at 0.1 MPa over 300–30000 K using the Chapman-Enskog method and Butler-Brokaw theory. Output total thermal conductivity in W/(m·K) vs. temperature.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: Columns: Temperature (K), ThermalConductivity_C6F12O (W/(m·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/composition.csv`
- `/app/outputs/thermodynamic_properties.csv`
- `/app/outputs/electrical_conductivity.csv`
- `/app/outputs/thermal_conductivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### composition.csv
- path: `/app/outputs/composition.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Number densities of all species vs. temperature. Checker validates positivity, elemental conservation, and expected species presence.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`
  - `units`:
    - `Temperature (K)`: K
    - `species`: m^-3

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermodynamic properties of C6F12O vs. temperature. Checker verifies specific heat peaks occur in dissociation/ionization ranges.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `Enthalpy`, `Entropy`, `SpecificHeat`, `SoundVelocity`
  - `units`:
    - `Enthalpy`: kJ/kg
    - `Entropy`: kJ/(kg·K)
    - `SpecificHeat`: J/(kg·K)
    - `SoundVelocity`: m/s

### electrical_conductivity.csv
- path: `/app/outputs/electrical_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Electrical conductivity of C6F12O, CO2, and N2 vs. temperature. Checker verifies that for T < 5000 K, Conductivity_C6F12O > Conductivity_CO2 and > Conductivity_N2.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `Conductivity_C6F12O`, `Conductivity_CO2`, `Conductivity_N2`
  - `units`:
    - `Conductivity_C6F12O`: S/m
    - `Conductivity_CO2`: S/m
    - `Conductivity_N2`: S/m

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total thermal conductivity of C6F12O vs. temperature. Checker locates the three most prominent peaks and verifies they lie within 3500±500 K, 5500±600 K, and 16000±1500 K.
- schema:
  - `type`: table
  - `required_columns`: `Temperature (K)`, `ThermalConductivity_C6F12O`
  - `units`:
    - `ThermalConductivity_C6F12O`: W/(m·K)

Notes: The reproduction requires DFT calculations for several macromolecules; the agent may need to allocate substantial compute resources. Scoring relies on structural trends (ordering of conductivities, locations of thermal conductivity peaks) rather than absolute numerical equality, because results depend on the specific quantum chemistry functional and basis set, as well as on implementation details of the Chapman‑Enskog solver.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)"
        ],
        "units": {
          "Temperature (K)": "K",
          "species": "m^-3"
        }
      },
      "description": "Number densities of all species vs. temperature. Checker validates positivity, elemental conservation, and expected species presence."
    },
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "Enthalpy",
          "Entropy",
          "SpecificHeat",
          "SoundVelocity"
        ],
        "units": {
          "Enthalpy": "kJ/kg",
          "Entropy": "kJ/(kg·K)",
          "SpecificHeat": "J/(kg·K)",
          "SoundVelocity": "m/s"
        }
      },
      "description": "Thermodynamic properties of C6F12O vs. temperature. Checker verifies specific heat peaks occur in dissociation/ionization ranges."
    },
    {
      "file": "electrical_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "Conductivity_C6F12O",
          "Conductivity_CO2",
          "Conductivity_N2"
        ],
        "units": {
          "Conductivity_C6F12O": "S/m",
          "Conductivity_CO2": "S/m",
          "Conductivity_N2": "S/m"
        }
      },
      "description": "Electrical conductivity of C6F12O, CO2, and N2 vs. temperature. Checker verifies that for T < 5000 K, Conductivity_C6F12O > Conductivity_CO2 and > Conductivity_N2."
    },
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature (K)",
          "ThermalConductivity_C6F12O"
        ],
        "units": {
          "ThermalConductivity_C6F12O": "W/(m·K)"
        }
      },
      "description": "Total thermal conductivity of C6F12O vs. temperature. Checker locates the three most prominent peaks and verifies they lie within 3500±500 K, 5500±600 K, and 16000±1500 K."
    }
  ],
  "notes": "The reproduction requires DFT calculations for several macromolecules; the agent may need to allocate substantial compute resources. Scoring relies on structural trends (ordering of conductivities, locations of thermal conductivity peaks) rather than absolute numerical equality, because results depend on the specific quantum chemistry functional and basis set, as well as on implementation details of the Chapman‑Enskog solver."
}
```

## How you are scored
A hidden verifier reads the four CSV files you produce. It first performs a sanity check on composition.csv (all densities positive and elemental conservation holds). It then examines electrical_conductivity.csv to verify that the conductivity of C₆F₁₂O exceeds that of CO₂ and N₂ at low temperatures. For thermal_conductivity.csv it applies a peak‑finding algorithm and checks that the three most prominent peaks lie within expected temperature intervals. Each scored artifact contributes to the total reward according to the weights in the output contract. Reporting the paper’s numbers without running the calculation is not sufficient; the verifier evaluates the actual computed results against hidden structural criteria.
