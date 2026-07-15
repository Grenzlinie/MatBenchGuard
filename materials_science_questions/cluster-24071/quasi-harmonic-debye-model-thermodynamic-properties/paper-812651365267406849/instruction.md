# Quasi-harmonic Debye model thermodynamic properties for MAX phase solid solutions

## Problem background
MAX phase compounds with the (M1-xM'x)n+1AXn formula are candidates for high-temperature structural applications because they can combine metallic and ceramic-like properties. Understanding how partial substitution of one transition metal for another changes the structural, mechanical, electronic, and thermodynamic behaviour is essential for materials design. This task focuses on the hexagonal MAX-phase solid solution (Zr1-xTix)3AlC2 over the full composition range. A first-principles computational study can predict the variation of lattice constants, elastic constants, moduli, hardness, and thermodynamic functions with Ti content, providing a benchmark for this family.

## Approach
Use density-functional theory in the plane-wave pseudopotential framework with the PBE generalized-gradient functional to determine ground-state properties. Perform geometry optimization for the three endpoint/intermediate compositions, scan total energy as a function of volume, and compute reference elemental energies. Apply an energy-strain method to extract the six independent elastic constants of the hexagonal lattice, then derive polycrystalline moduli via the Voigt-Reuss-Hill approximation and estimate Vickers hardness. Electronic structure (band gap and density of states at the Fermi level) is obtained from a self-consistent calculation at the equilibrium geometry. Finally, the quasi-harmonic Debye model is applied to the E(V) data to obtain temperature-dependent bulk modulus, Debye temperature, and heat capacities at selected temperatures under zero pressure.

## Reproduction target
For the three compositions x = 0, 0.5, 1.0, compute and report the following quantities at zero pressure: equilibrium lattice parameters a, c, and cell volume V; formation energy (eV per formula unit); the independent elastic constants C11, C12, C13, C33, C44, C66; polycrystalline bulk modulus B, shear modulus G, Young's modulus E; Poisson's ratio; Vickers hardness; electronic band gap (should be zero, as the compounds are metallic) and the density of states at the Fermi level N(EF); the Debye temperature at 0 K; the heat capacities Cv and Cp at 0 K, 300 K, and 600 K; and the quasi-harmonic bulk modulus at 0 K and 300 K. Collect all results into a single JSON file.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSlibrary pseudopotentials: https://www.quantum-espresso.org/pseudopotentials/pslibrary
- Gibbs code (quasi-harmonic Debye model) or equivalent: https://personal.ua.es/en/francisco.manuel/compchem/gibbs.html

## Workflow steps

### Step 1: DFT ground-state optimization and E(V) generation
- Role: process
- Action: Perform geometry optimization for the three compositions (Zr1-xTix)3AlC2 with x=0, 0.5, 1.0 using a plane-wave DFT code and PBE functional, obtaining equilibrium lattice parameters. Then compute total energy for a series of volumes around equilibrium to generate E(V) data for each composition. Save the E(V) data points in a structured file.
- Evidence: `/app/outputs/E_vs_V.csv`

### Step 2: Reference total energy of pure elements
- Role: process
- Action: Compute the total energy per atom for Zr, Ti, Al, and C in their elemental ground-state crystal structures using the same DFT setup. Save the reference energies.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Formation energy calculation
- Role: process
- Action: Using the total energies from step 0 (equilibrium) and step 1 (pure elements), calculate the formation energy per formula unit for each composition. Save the result.
- Evidence: `/app/outputs/formation_energy.json`

### Step 4: Electronic structure calculation
- Role: process
- Action: Compute the density of states (DOS) for each composition at the equilibrium geometry. Extract the band gap (should be 0 for metallic) and the DOS at the Fermi level (N_EF). Save these values.
- Evidence: `/app/outputs/dos_data.json`

### Step 5: Elastic constants via energy-strain method
- Role: process
- Action: Apply six appropriate strain distortions to the optimized unit cell for each composition, compute the total energy of each distorted cell with DFT, and fit the energy-strain relations to obtain the independent elastic constants C11, C12, C13, C33, C44, C66. Save the elastic constants.
- Evidence: `/app/outputs/elastic_constants.json`

### Step 6: Mechanical moduli and hardness
- Role: process
- Action: From the elastic constants, derive the polycrystalline bulk modulus B, shear modulus G, Young's modulus E (Voigt-Reuss-Hill approximation), Poisson's ratio, Cauchy pressure components, shear anisotropy factors, and Vickers hardness using Chen's formula. Save these results.
- Evidence: `/app/outputs/mechanical_properties.json`

### Step 7: Debye temperature from elastic constants
- Role: process
- Action: Compute the Debye temperature at 0 K, as well as the longitudinal, transverse and average sound velocities, from the elastic constants, density and formula mass. Save the values.
- Evidence: `/app/outputs/debye_0K.json`

### Step 8: Quasi-harmonic Debye model calculations
- Role: process
- Action: Using the E(V) data from step 0, apply the quasi-harmonic Debye model (e.g., Gibbs code or equivalent) to compute the temperature- and pressure-dependent bulk modulus, Debye temperature, and heat capacities Cv and Cp. Extract values at selected temperatures (0 K, 300 K, 600 K) and zero pressure. Save the extracted thermodynamic data.
- Evidence: `/app/outputs/thermo_data.json`

### Step 9: Compile final property summary
- Role: scored (load-bearing)
- Action: Collect all computed quantities for each composition (x=0, 0.5, 1.0) and write a single JSON file with root key 'compositions' containing an array of three objects, each with the following numeric fields: x, a (Å), c (Å), V (Å³), c/a (float, dimensionless), formation_energy (eV/f.u.), C11, C12, C13, C33, C44, C66 (GPa), bulk_modulus_B (GPa), shear_modulus_G (GPa), Young_modulus_E (GPa), Poisson_ratio, B_G_ratio, Cauchy_pressure_x, Cauchy_pressure_y, anisotropy_A1, anisotropy_A2, anisotropy_A3, Vickers_hardness (GPa), band_gap (eV), N_EF (states/eV/cell), Debye_temperature_0K (K), Debye_temperature_300K (K), heat_capacity_Cv_0K, heat_capacity_Cv_300K, heat_capacity_Cv_600K, heat_capacity_Cp_300K, heat_capacity_Cp_600K (J/mol·K), bulk_modulus_0K (GPa), bulk_modulus_300K (GPa).
- Output file: `/app/outputs/properties_summary.json`
- Format: json
- Contract: object with key 'compositions', array of objects each having: x (float), a (float, Å), c (float, Å), V (float, Å³), c/a (float, dimensionless), formation_energy (float, eV/f.u.), C11, C12, C13, C33, C44, C66 (float, GPa), bulk_modulus_B (float, GPa), shear_modulus_G (float, GPa), Young_modulus_E (float, GPa), Poisson_ratio (float), B_G_ratio (float), Cauchy_pressure_x (float, GPa?), Cauchy_pressure_y (float, GPa?), anisotropy_A1 (float), anisotropy_A2 (float), anisotropy_A3 (float), Vickers_hardness (float, GPa), band_gap (float, eV), N_EF (float, states/eV/cell), Debye_temperature_0K (float, K), Debye_temperature_300K (float, K), heat_capacity_Cv_0K (float, J/mol·K), heat_capacity_Cv_300K (float), heat_capacity_Cv_600K (float), heat_capacity_Cp_300K (float), heat_capacity_Cp_600K (float), bulk_modulus_0K (float, GPa), bulk_modulus_300K (float, GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties_summary.json
- path: `/app/outputs/properties_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final summary of all computed properties for the three compositions. Checked against hidden paper-reported reference values with tolerances and trend requirements. Includes the hexagonal lattice ratio c/a as required by the verifier.
- schema:
  - `type`: object
  - `required`:
    - `compositions`: array of three objects, each containing: x (float), a (float, Å), c (float, Å), V (float, Å³), c/a (float, dimensionless), formation_energy (float, eV/f.u.), C11, C12, C13, C33, C44, C66 (float, GPa), bulk_modulus_B (float, GPa), shear_modulus_G (float, GPa), Young_modulus_E (float, GPa), Poisson_ratio (float), B_G_ratio (float), Cauchy_pressure_x (float, GPa?), Cauchy_pressure_y (float, GPa?), anisotropy_A1 (float), anisotropy_A2 (float), anisotropy_A3 (float), Vickers_hardness (float, GPa), band_gap (float, eV), N_EF (float, states/eV/cell), Debye_temperature_0K (float, K), Debye_temperature_300K (float, K), heat_capacity_Cv_0K (float, J/mol·K), heat_capacity_Cv_300K (float), heat_capacity_Cv_600K (float), heat_capacity_Cp_300K (float), heat_capacity_Cp_600K (float), bulk_modulus_0K (float, GPa), bulk_modulus_300K (float, GPa).
  - `units`:
    - `x`: dimensionless
    - `a`: Å
    - `c`: Å
    - `V`: Å³
    - `c/a`: dimensionless
    - `formation_energy`: eV/f.u.
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C66`: GPa
    - `bulk_modulus_B`: GPa
    - `shear_modulus_G`: GPa
    - `Young_modulus_E`: GPa
    - `Poisson_ratio`: dimensionless
    - `B_G_ratio`: dimensionless
    - `Cauchy_pressure_x`: GPa
    - `Cauchy_pressure_y`: GPa
    - `anisotropy_A1`: dimensionless
    - `anisotropy_A2`: dimensionless
    - `anisotropy_A3`: dimensionless
    - `Vickers_hardness`: GPa
    - `band_gap`: eV
    - `N_EF`: states/eV/cell
    - `Debye_temperature_0K`: K
    - `Debye_temperature_300K`: K
    - `heat_capacity_Cv_0K`: J/mol·K
    - `heat_capacity_Cv_300K`: J/mol·K
    - `heat_capacity_Cv_600K`: J/mol·K
    - `heat_capacity_Cp_300K`: J/mol·K
    - `heat_capacity_Cp_600K`: J/mol·K
    - `bulk_modulus_0K`: GPa
    - `bulk_modulus_300K`: GPa

Notes: The hidden checker now expects c/a to be present, consistent with the updated step contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "compositions": "array of three objects, each containing: x (float), a (float, Å), c (float, Å), V (float, Å³), c/a (float, dimensionless), formation_energy (float, eV/f.u.), C11, C12, C13, C33, C44, C66 (float, GPa), bulk_modulus_B (float, GPa), shear_modulus_G (float, GPa), Young_modulus_E (float, GPa), Poisson_ratio (float), B_G_ratio (float), Cauchy_pressure_x (float, GPa?), Cauchy_pressure_y (float, GPa?), anisotropy_A1 (float), anisotropy_A2 (float), anisotropy_A3 (float), Vickers_hardness (float, GPa), band_gap (float, eV), N_EF (float, states/eV/cell), Debye_temperature_0K (float, K), Debye_temperature_300K (float, K), heat_capacity_Cv_0K (float, J/mol·K), heat_capacity_Cv_300K (float), heat_capacity_Cv_600K (float), heat_capacity_Cp_300K (float), heat_capacity_Cp_600K (float), bulk_modulus_0K (float, GPa), bulk_modulus_300K (float, GPa)."
        },
        "units": {
          "x": "dimensionless",
          "a": "Å",
          "c": "Å",
          "V": "Å³",
          "c/a": "dimensionless",
          "formation_energy": "eV/f.u.",
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C66": "GPa",
          "bulk_modulus_B": "GPa",
          "shear_modulus_G": "GPa",
          "Young_modulus_E": "GPa",
          "Poisson_ratio": "dimensionless",
          "B_G_ratio": "dimensionless",
          "Cauchy_pressure_x": "GPa",
          "Cauchy_pressure_y": "GPa",
          "anisotropy_A1": "dimensionless",
          "anisotropy_A2": "dimensionless",
          "anisotropy_A3": "dimensionless",
          "Vickers_hardness": "GPa",
          "band_gap": "eV",
          "N_EF": "states/eV/cell",
          "Debye_temperature_0K": "K",
          "Debye_temperature_300K": "K",
          "heat_capacity_Cv_0K": "J/mol·K",
          "heat_capacity_Cv_300K": "J/mol·K",
          "heat_capacity_Cv_600K": "J/mol·K",
          "heat_capacity_Cp_300K": "J/mol·K",
          "heat_capacity_Cp_600K": "J/mol·K",
          "bulk_modulus_0K": "GPa",
          "bulk_modulus_300K": "GPa"
        }
      },
      "description": "Final summary of all computed properties for the three compositions. Checked against hidden paper-reported reference values with tolerances and trend requirements. Includes the hexagonal lattice ratio c/a as required by the verifier."
    }
  ],
  "notes": "The hidden checker now expects c/a to be present, consistent with the updated step contract."
}
```

## How you are scored
A hidden verifier inspects your final properties_summary.json and compares each numerical entry against a reference set. In addition, the verifier checks several structural requirements: the elastic constants must satisfy the mechanical stability criteria for a hexagonal crystal; the band gap must be exactly 0.0; and certain composition trends (e.g., lattice parameters decreasing with x, moduli increasing with x) must hold. Each satisfied check contributes to your total reward, which is the weighted fraction of passing checks. Running the workflow honestly is essential; reporting paper-derived values without executing the computation will not produce all required intermediate artifacts and will be penalized.
