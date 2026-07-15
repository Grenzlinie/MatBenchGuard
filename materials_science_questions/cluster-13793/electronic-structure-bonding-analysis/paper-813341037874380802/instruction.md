# Elastic and Electronic Properties of L1₂-Al₃(Sc₀.₅TM₀.₅) Random Alloys from DFT

## Problem background
L1₂-Al₃Sc is a lightweight intermetallic compound that is structurally stable but brittle at room temperature, limiting its aerospace applications. Partial substitution of Sc by transition metals (TM) is a promising strategy to improve ductility and reduce material cost. This work explores a series of pseudo‑binary L1₂‑Al₃(Sc₀.₅TM₀.₅) random alloys where TM atoms substitute on the Sc sublattice. The central problem is to understand how the choice of TM influences the structural stability, elastic behaviour, and electronic structure, and to reveal the electronic‑level mechanism linking TM atomic radius to the observed mechanical trends.

## Approach
The random distribution of TM on the Sc sublattice is modelled with special quasi‑random structures (SQS). A cubic 32‑atom SQS supercell is generated for each alloy using the ATAT toolkit's gensqs code, ensuring that pair and multisite correlation functions match the random alloy as closely as possible.

First‑principles density functional theory (DFT) calculations are then performed with the generalized gradient approximation (GGA‑PBE) and projector‑augmented wave (PAW) pseudo‑potentials that explicitly treat semi‑core states. The workflow consists of:

1. Geometry optimisation of each SQS supercell to obtain equilibrium lattice constants and total energies. Formation energies are derived using elemental reference energies (fcc Al, hcp Sc, and the ground‑state crystal structures of the TMs).
2. Elastic constants C₁₁, C₁₂, C₄₄ are computed by applying small strains to the relaxed cells and fitting the resulting energy‑strain curves. Polycrystalline moduli (bulk, shear, Young’s modulus) are obtained by Voigt‑Reuss‑Hill averaging. Ductility indicators — the B/G ratio and Cauchy pressure (C₁₂ – C₄₄) — as well as Poisson's ratio and the elastic anisotropy factor A are evaluated.
3. Total and site‑projected partial density of states (DOS) are calculated to examine the electronic structure, particularly the hybridisation between Al p states and transition‑metal d states near the Fermi level.
4. Valence charge density is extracted on the (001) plane for selected alloys to visualise the bonding charge overlap between Al and the Sc/TM atoms.

The series covers seven TMs (Y, Ti, Zr, Hf, V, Nb, Ta). By systematically comparing alloys within the same Period of the periodic table, the influence of TM atomic radius on stability, elastic isotropy, and ductility can be evaluated.

## Reproduction target
The goal is to compute the structural and elastic properties of L1₂‑Al₃Sc and the seven L1₂‑Al₃(Sc₀.₅TM₀.₅) alloys (TM = Y, Ti, Zr, Hf, V, Nb, Ta). Specifically, produce:

- For all eight alloys: lattice constant a, formation energy ΔH per atom, the elastic constants C₁₁, C₁₂, C₄₄, and the derived polycrystalline moduli (B, G, E, B/G, C₁₂ – C₄₄, Poisson's ratio v, and anisotropy factor A). These are assembled in a scored CSV file (`properties.csv`).
- Density of states: total and partial DOS for at least the alloys Al₃Sc, Al₃(Sc₀.₅Ti₀.₅), Al₃(Sc₀.₅V₀.₅), Al₃(Sc₀.₅Zr₀.₅), Al₃(Sc₀.₅Nb₀.₅). The data should span −10 eV to 5 eV relative to the Fermi level and be written to `dos_data.csv`.
- Charge density on the (001) plane for Al₃Sc, Al₃(Sc₀.₅Y₀.₅), Al₃(Sc₀.₅Zr₀.₅), and Al₃(Sc₀.₅Nb₀.₅). The 2D maps are saved as `charge_density_001.json`.

Using these results, examine the relationship between the computed ductility indicators (B/G ratio and Cauchy pressure) and the atomic radius of the substitution element within each Period, and analyse any systematic shifts in the electronic structure (DOS features and charge density overlap) that accompany the TM substitution.

## Assets

- ATAT (Alloy Theoretic Automated Toolkit): https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- SSSP pseudopotentials (efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific stack: numpy, scipy, ase, matplotlib

## Workflow steps

### Step 1: Generate SQS-32 supercells
- Role: process
- Action: Use ATAT gensqs to generate cubic 32-atom SQS supercells for L1₂-Al₃Sc and L1₂-Al₃(Sc₀.₅TM₀.₅) (TM = Y, Ti, Zr, Hf, V, Nb, Ta) with optimal pair and multisite correlation functions. Output the unrelaxed structures in a format readable by QE (e.g., cif or POSCAR).
- Evidence: `/app/outputs/sqs_structures_manifest.txt`

### Step 2: DFT reference energies for elemental solids
- Role: process
- Action: Perform DFT total energy calculations for the elemental solids: fcc Al, hcp Sc, hcp Y, hcp Ti, hcp Zr, hcp Hf, bcc V, bcc Nb, bcc Ta. Use an open-source DFT code (e.g., Quantum ESPRESSO) with SSSP pseudopotentials, converging total energies to better than 1 meV/atom.
- Evidence: `/app/outputs/element_ref_energies.csv`

### Step 3: DFT geometry optimization of alloy supercells
- Role: process
- Action: For each alloy supercell, perform full variable-cell relaxation (cell shape, volume, atomic positions) with QE. Record the optimised lattice parameters and total energies. Optionally fit the energy-volume curve to a Birch-Murnaghan equation of state to obtain the equilibrium lattice constant and bulk modulus B_EOS.
- Evidence: `/app/outputs/relaxed_alloys_info.csv`

### Step 4: DFT elastic constant calculations
- Role: process
- Action: Apply small strains to the relaxed unit cells of each alloy according to the standard scheme for cubic symmetry to obtain C₁₁, C₁₂, C₄₄. Compute the total energy for each strained configuration with QE, keeping the plane-wave cut-off and k-point mesh identical to the relaxation step.
- Evidence: `/app/outputs/elastic_strain_data.json`

### Step 5: Compute properties table
- Role: scored (load-bearing)
- Action: From the outputs of steps 02, 03 and 04: (1) calculate formation energies ΔH per atom using the formula ΔH = (E_total_alloy - N_Al*E_Al_fcc - N_Sc*E_Sc_hcp - N_TM*E_TM_solid) / (N_Al+N_Sc+N_TM). (2) Fit the strain-energy data to quadratic forms to extract C₁₁, C₁₂, C₄₄. (3) Derive polycrystalline moduli (B, G, E, v) by Voigt-Reuss-Hill averaging, the B/G ratio, Cauchy pressure C₁₂−C₄₄, and anisotropy factor A. (4) Assemble all quantities into a CSV file.
- Output file: `/app/outputs/properties.csv`
- Format: csv
- Contract: CSV with columns: alloy (string), lattice_constant_a (Å), formation_energy_deltaH (eV/atom), C11 (GPa), C12 (GPa), C44 (GPa), bulk_modulus_B (GPa), shear_modulus_G (GPa), young_modulus_E (GPa), B_G_ratio (unitless), cauchy_pressure_C12_minus_C44 (GPa), poisson_ratio_v (unitless), anisotropy_factor_A (unitless). Eight rows: Al3Sc, Al3(Sc0.5Y0.5), Al3(Sc0.5Ti0.5), Al3(Sc0.5Zr0.5), Al3(Sc0.5Hf0.5), Al3(Sc0.5V0.5), Al3(Sc0.5Nb0.5), Al3(Sc0.5Ta0.5).
- Scoring: scored by hidden verifier

### Step 6: DFT density of states (DOS) calculation
- Role: process
- Action: For each alloy, perform a static DFT calculation on the relaxed structure using a denser k‑point mesh. Compute the total DOS and site‑projected partial DOS (Al s, Al p, Sc d, TM d). Extract the Fermi level as energy zero.
- Evidence: `/app/outputs/dos_calc.log`

### Step 7: Export DOS data
- Role: scored
- Action: From the raw DOS output of step_06, produce a single CSV file with total and partial DOS for the alloys required by the checker: Al3Sc, Al3(Sc0.5Ti0.5), Al3(Sc0.5V0.5), Al3(Sc0.5Zr0.5), Al3(Sc0.5Nb0.5). Energy range from -10 to 5 eV with step ≤0.1 eV; Fermi level at 0 eV.
- Output file: `/app/outputs/dos_data.csv`
- Format: csv
- Contract: CSV with columns: alloy (string), energy_eV (float), total_DOS (states/eV/unit_cell), partial_Al_s (ratio), partial_Al_p (ratio), partial_TM_d (ratio), partial_Sc_d (ratio). Fermi level at 0 eV. Energy range -10 to 5 eV, step ≤0.1 eV. One row per energy point per alloy.
- Scoring: scored by hidden verifier

### Step 8: DFT charge density calculation
- Role: process
- Action: For the four alloys Al3Sc, Al3(Sc0.5Y0.5), Al3(Sc0.5Zr0.5), Al3(Sc0.5Nb0.5), perform a self‑consistent DFT calculation on the relaxed structures and extract the valence charge density on a 3D grid.
- Evidence: `/app/outputs/charge_density_calc.log`

### Step 9: Export charge density on (001) plane
- Role: scored
- Action: For each of the four alloys, slice the 3D charge density at z=0 to obtain the (001) plane. Create a uniform grid covering one unit cell with spacing ≤0.1 Å. Write a JSON object with keys per alloy, each containing x_grid (Å), y_grid (Å) and the 2D density array (e/Å³).
- Output file: `/app/outputs/charge_density_001.json`
- Format: json
- Contract: JSON with keys 'Al3Sc', 'Al3(Sc0.5Y0.5)', 'Al3(Sc0.5Zr0.5)', 'Al3(Sc0.5Nb0.5)'. Each value is an object {x_grid: [float], y_grid: [float], density: [[float]]} where density[i][j] corresponds to (x_grid[i], y_grid[j]) on the (001) plane.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/properties.csv`
- `/app/outputs/dos_data.csv`
- `/app/outputs/charge_density_001.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### properties.csv
- path: `/app/outputs/properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Key structural and elastic properties of L1₂-Al₃Sc and seven L1₂-Al₃(Sc₀.₅TM₀.₅) alloys. Checked against paper-reported values with tolerances, and monitored monotonic trends in B/G and Cauchy pressure.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `lattice_constant_a`, `formation_energy_deltaH`, `C11`, `C12`, `C44`, `bulk_modulus_B`, `shear_modulus_G`, `young_modulus_E`, `B_G_ratio`, `cauchy_pressure_C12_minus_C44`, `poisson_ratio_v`, `anisotropy_factor_A`
  - `units`:
    - `lattice_constant_a`: Å
    - `formation_energy_deltaH`: eV/atom
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `bulk_modulus_B`: GPa
    - `shear_modulus_G`: GPa
    - `young_modulus_E`: GPa
    - `B_G_ratio`: unitless
    - `cauchy_pressure_C12_minus_C44`: GPa
    - `poisson_ratio_v`: unitless
    - `anisotropy_factor_A`: unitless

### dos_data.csv
- path: `/app/outputs/dos_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total and partial DOS for selected alloys. Verified for existence of a pseudo-gap near the Fermi level and the shift of the Fermi level relative to the pseudo-gap with TM substitution.
- schema:
  - `type`: table
  - `required_columns`: `alloy`, `energy_eV`, `total_DOS`, `partial_Al_s`, `partial_Al_p`, `partial_TM_d`, `partial_Sc_d`
  - `units`:
    - `energy_eV`: eV
    - `total_DOS`: states/eV/unit_cell
    - `partial_Al_s`: ratio
    - `partial_Al_p`: ratio
    - `partial_TM_d`: ratio
    - `partial_Sc_d`: ratio

### charge_density_001.json
- path: `/app/outputs/charge_density_001.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Charge density on the (001) plane for four alloys, used to verify the reduction of covalent bonding overlap between Al and Sc/TM as the TM atomic radius decreases.
- schema:
  - `type`: object
  - `required`:
    - `Al3Sc`: object
    - `Al3(Sc0.5Y0.5)`: object
    - `Al3(Sc0.5Zr0.5)`: object
    - `Al3(Sc0.5Nb0.5)`: object
  - `items`:
    - `x_grid`: [float]
    - `y_grid`: [float]
    - `density`: [[float]]
  - `units`:
    - `x_grid`: Å
    - `y_grid`: Å
    - `density`: e/Å³

Notes: Scoring compares each value in properties.csv to hidden paper-reported reference values with tolerances, and checks monotonic trends in B/G and Cauchy pressure across alloy series. DOS data is audited for pseudo-gap features and Fermi level shifts. Charge density maps are checked for the decreasing trend in maximum bond charge at the Al-TM midpoint.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "lattice_constant_a",
          "formation_energy_deltaH",
          "C11",
          "C12",
          "C44",
          "bulk_modulus_B",
          "shear_modulus_G",
          "young_modulus_E",
          "B_G_ratio",
          "cauchy_pressure_C12_minus_C44",
          "poisson_ratio_v",
          "anisotropy_factor_A"
        ],
        "units": {
          "lattice_constant_a": "Å",
          "formation_energy_deltaH": "eV/atom",
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "bulk_modulus_B": "GPa",
          "shear_modulus_G": "GPa",
          "young_modulus_E": "GPa",
          "B_G_ratio": "unitless",
          "cauchy_pressure_C12_minus_C44": "GPa",
          "poisson_ratio_v": "unitless",
          "anisotropy_factor_A": "unitless"
        }
      },
      "description": "Key structural and elastic properties of L1₂-Al₃Sc and seven L1₂-Al₃(Sc₀.₅TM₀.₅) alloys. Checked against paper-reported values with tolerances, and monitored monotonic trends in B/G and Cauchy pressure."
    },
    {
      "file": "dos_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alloy",
          "energy_eV",
          "total_DOS",
          "partial_Al_s",
          "partial_Al_p",
          "partial_TM_d",
          "partial_Sc_d"
        ],
        "units": {
          "energy_eV": "eV",
          "total_DOS": "states/eV/unit_cell",
          "partial_Al_s": "ratio",
          "partial_Al_p": "ratio",
          "partial_TM_d": "ratio",
          "partial_Sc_d": "ratio"
        }
      },
      "description": "Total and partial DOS for selected alloys. Verified for existence of a pseudo-gap near the Fermi level and the shift of the Fermi level relative to the pseudo-gap with TM substitution."
    },
    {
      "file": "charge_density_001.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "Al3Sc": "object",
          "Al3(Sc0.5Y0.5)": "object",
          "Al3(Sc0.5Zr0.5)": "object",
          "Al3(Sc0.5Nb0.5)": "object"
        },
        "items": {
          "x_grid": "[float]",
          "y_grid": "[float]",
          "density": "[[float]]"
        },
        "units": {
          "x_grid": "Å",
          "y_grid": "Å",
          "density": "e/Å³"
        }
      },
      "description": "Charge density on the (001) plane for four alloys, used to verify the reduction of covalent bonding overlap between Al and Sc/TM as the TM atomic radius decreases."
    }
  ],
  "notes": "Scoring compares each value in properties.csv to hidden paper-reported reference values with tolerances, and checks monotonic trends in B/G and Cauchy pressure across alloy series. DOS data is audited for pseudo-gap features and Fermi level shifts. Charge density maps are checked for the decreasing trend in maximum bond charge at the Al-TM midpoint."
}
```

## How you are scored
A hidden verifier independently evaluates the three scored output files. The scoring weights are approximately: `properties.csv` – 70%, `dos_data.csv` – 15%, `charge_density_001.json` – 15%.

- `properties.csv`: The verifier compares each computed quantity (lattice constant, formation energy, elastic constants, moduli, B/G, Cauchy pressure, etc.) against reference values with tolerances representative of DFT‑to‑DFT variability. It also checks that the B/G ratio and Cauchy pressure vary monotonically with the atomic radius of the TM within each Period (Y→Zr→Nb and Ti→V).
- `dos_data.csv`: The verifier confirms the existence of a pseudo‑gap (local minimum in total DOS) within 1 eV of the Fermi level for each required alloy, and verifies that the Fermi level shifts systematically relative to the pseudo‑gap across the alloy series.
- `charge_density_001.json`: The verifier checks that the maximum charge density at the Al–TM (or Al–Sc) midpoint on the (001) plane follows a systematic trend across the four alloys (Al₃Sc, Al₃(Sc₀.₅Y₀.₅), Al₃(Sc₀.₅Zr₀.₅), Al₃(Sc₀.₅Nb₀.₅)).

Your submission is scored on the correctness of the produced values and the fulfilment of these structural/trend criteria. The reference numbers and exact tolerances are not disclosed; they are derived from the paper’s reported results.
