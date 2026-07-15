## Problem background

Thermoelectric materials convert waste heat into electricity via the Seebeck effect. Their performance is measured by the dimensionless figure of merit ZT, which requires a high Seebeck coefficient, high electrical conductivity, and low thermal conductivity. Two-dimensional (2D) monochalcogenides — SnSe, SnS, GeSe, and GeS — are promising candidates because they can exhibit higher Seebeck coefficients and lower lattice thermal conductivities than their bulk counterparts. This task investigates the thermoelectric and phonon transport properties of these 2D materials using density functional theory (DFT) combined with Boltzmann transport theory for both electrons and phonons.

## Approach

Compute the electronic structure, lattice dynamics, and transport coefficients for monolayer SnSe, SnS, GeSe, and GeS from first principles. The workflow consists of:
- **Geometry optimization** of each monolayer with DFT (Generalized Gradient Approximation, van der Waals correction).
- **Electronic structure** calculation to obtain band structures and direction-dependent effective masses.
- **Elastic and deformation potential constants** from strain-dependent DFT to parameterise carrier mobility.
- **Carrier mobility and relaxation time** using deformation potential theory for the armchair and zigzag directions at 300, 500, and 700 K.
- **Electronic thermoelectric properties** (Seebeck coefficient, electrical conductivity, electronic thermal conductivity) via the Boltzmann transport equation for electrons, using the constant relaxation time approximation (BoltzTraP).
- **Phonon stability** verified by phonon dispersion computed with density-functional perturbation theory (DFPT).
- **Harmonic (second-order) and anharmonic (third-order) interatomic force constants** from supercell finite-displacement calculations.
- **Lattice thermal conductivity** from the phonon Boltzmann transport equation, solved both iteratively and with the single-mode relaxation time approximation (ShengBTE).
- Finally, combine all coefficients to obtain the figure of merit ZT as a function of carrier concentration and temperature.

## Reproduction target

Using open-source DFT and transport codes, compute for monolayers of SnSe, SnS, GeSe, and GeS:
1. The room-temperature lattice thermal conductivities along the armchair and zigzag directions.
2. The maximum Seebeck coefficient at 300 K.
3. The maximum ZT at 700 K along both directions.

Write these results to the specified CSV files (see Output files). The evaluation will compare your computed values to reference results within appropriate tolerances; a hidden verifier independently scores each output.

## Assets

- **Quantum ESPRESSO** (open-source DFT package) – used for geometry optimization, electronic structure, DFPT, and force calculations. URL: https://www.quantum-espresso.org/
- **BoltzTraP2** (code for solving the electronic Boltzmann transport equation) – used to compute Seebeck coefficient, electrical conductivity, and electronic thermal conductivity. URL: https://bitbucket.org/sousaw/boltz_trap2/
- **Phonopy** (harmonic phonon calculations) – used for second-order interatomic force constants via finite-displacement supercell. URL: https://phonopy.github.io/phonopy/
- **ShengBTE** (solver of the phonon Boltzmann transport equation) – requires harmonic and anharmonic force constants; includes `thirdorder.py` for anharmonic calculations. URL: https://www.shengbte.org/
- **SSSP efficiency pseudopotentials** (PBE for Sn, Se, S, Ge) – public pseudopotential library for Quantum ESPRESSO. URL: https://www.materialscloud.org/discover/sssp/table/efficiency

The above tools and libraries are publicly available. They are not bundled; fetch them at runtime.

## Workflow steps

### Step 1: Geometry optimization of monolayers
- Role: process
- Action: For each monolayer (SnSe, SnS, GeSe, GeS), perform DFT geometry optimization using Quantum ESPRESSO with GGA (PBE) and a van der Waals correction to obtain relaxed lattice parameters and atomic coordinates.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Electronic structure and effective masses
- Role: process
- Action: For each optimized monolayer, perform self-consistent and non-self-consistent band structure calculations on a uniform k-point mesh to obtain electronic eigenvalues and direction-dependent effective masses (armchair/zigzag).
- Evidence: `/app/outputs/bandstructure_data.hdf5`

### Step 3: Elastic constant and deformation potential
- Role: process
- Action: Compute the 2D elastic constant C2D by fitting energy vs. uniaxial strain, and the deformation potential constant E1 from the shift of the conduction band minimum under strain, using DFT.
- Evidence: `/app/outputs/elastic_deformation_params.csv`

### Step 4: Carrier mobility and relaxation time
- Role: process
- Action: Compute carrier mobility μ using deformation potential theory: μ = e ℏ³ C²ᴰ / (kₛ T m* m_d E₁²), where C²ᴰ is the 2D elastic constant, m* is the effective mass along the transport direction, m_d = √(m_x m_y) is the density-of-states effective mass, and E₁ is the deformation potential constant. Then compute relaxation time τ = m* μ / e. Evaluate μ and τ for armchair and zigzag directions at 300 K, 500 K, and 700 K.
- Evidence: `/app/outputs/relaxation_times.csv`

### Step 5: Electronic thermoelectric properties via BoltzTraP
- Role: process
- Action: Run BoltzTraP2 with the electronic eigenvalues and the temperature-dependent relaxation times to obtain Seebeck coefficient (S), electrical conductivity (σ), and electronic thermal conductivity (κe) as functions of carrier concentration and temperature (300–700 K) for both directions.
- Evidence: `/app/outputs/boltztrap_output.hdf5`

### Step 6: Maximum Seebeck coefficient at 300 K
- Role: scored
- Action: From the BoltzTraP output, determine the maximum absolute Seebeck coefficient (over doping and direction) at 300 K for each monolayer and write the value to `seebeck_max_300K.csv`.
- Output file: `/app/outputs/seebeck_max_300K.csv`
- Format: csv
- Contract: Columns: `composition` (string, one of SnSe, SnS, GeSe, GeS), `S_max` (float, μV/K). One row per compound.
- Scoring: scored by hidden verifier against reference values.

### Step 7: Phonon harmonic IFCs and band structure
- Role: process
- Action: Using Phonopy with a supercell (e.g., 5×5×1) and Quantum ESPRESSO forces, compute the second-order interatomic force constants and the phonon dispersions for each monolayer.
- Evidence: `/app/outputs/phonopy_output.yaml`

### Step 8: Phonon stability (no imaginary modes)
- Role: scored
- Action: From the phonon dispersion output, extract the minimum phonon frequency (real/imaginary) for each compound and write to `phonon_stability.csv`. Ensure there are no imaginary frequencies.
- Output file: `/app/outputs/phonon_stability.csv`
- Format: csv
- Contract: Columns: `composition` (string), `min_frequency` (float, THz). One row per compound.
- Scoring: scored by hidden verifier; structural check on dynamical stability.

### Step 9: Anharmonic third-order IFCs
- Role: process
- Action: Compute third-order interatomic force constants using a supercell (e.g., 4×4×1) and interactions up to the 15th nearest neighbour, using the `thirdorder.py` script from ShengBTE.
- Evidence: `/app/outputs/FORCE_CONSTANTS_3RD`

### Step 10: Lattice thermal conductivity via ShengBTE
- Role: process
- Action: Run ShengBTE with the harmonic and anharmonic IFCs to solve the phonon Boltzmann transport equation, obtaining lattice thermal conductivity (iterative and SMRTA) as a function of temperature and direction.
- Evidence: `/app/outputs/shengbte_output.hdf5`

### Step 11: Room-temperature lattice thermal conductivity
- Role: scored
- Action: From the ShengBTE output, extract the lattice thermal conductivity at 300 K for armchair and zigzag directions of each monolayer and write to `lattice_thermal_conductivity.csv`.
- Output file: `/app/outputs/lattice_thermal_conductivity.csv`
- Format: csv
- Contract: Columns: `composition` (string), `direction` (string, one of armchair/zigzag), `kappa_l` (float, W/m/K). Rows for each compound and both directions.
- Scoring: scored by hidden verifier against reference values.

### Step 12: Thermoelectric figure of merit ZT at 700 K
- Role: scored (load-bearing)
- Action: Using the electronic transport properties (S, σ, κe) from BoltzTraP at 700 K and the lattice thermal conductivity κl from ShengBTE at 700 K, compute ZT = (σ S²) / (κe + κl) × T for each material and direction; report the maximum ZT over doping in `zt_700K.csv`.
- Output file: `/app/outputs/zt_700K.csv`
- Format: csv
- Contract: Columns: `composition` (string), `direction` (string, armchair/zigzag), `ZT` (float). Rows for each compound and both directions.
- Scoring: scored by hidden verifier against reference values.

## Output files

- `/app/outputs/optimized_structures.json` (evidence)
- `/app/outputs/bandstructure_data.hdf5` (evidence)
- `/app/outputs/elastic_deformation_params.csv` (evidence)
- `/app/outputs/relaxation_times.csv` (evidence)
- `/app/outputs/boltztrap_output.hdf5` (evidence)
- `/app/outputs/seebeck_max_300K.csv` (scored)
- `/app/outputs/phonopy_output.yaml` (evidence)
- `/app/outputs/phonon_stability.csv` (scored)
- `/app/outputs/FORCE_CONSTANTS_3RD` (evidence)
- `/app/outputs/shengbte_output.hdf5` (evidence)
- `/app/outputs/lattice_thermal_conductivity.csv` (scored)
- `/app/outputs/zt_700K.csv` (scored)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### seebeck_max_300K.csv
- path: `/app/outputs/seebeck_max_300K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum absolute Seebeck coefficient at 300 K for each monolayer.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `S_max`
  - `units`:
    - `S_max`: μV/K

### phonon_stability.csv
- path: `/app/outputs/phonon_stability.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Minimum phonon frequency per compound; must be positive (no imaginary modes).
- schema:
  - `type`: table
  - `required_columns`: `composition`, `min_frequency`
  - `units`:
    - `min_frequency`: THz

### lattice_thermal_conductivity.csv
- path: `/app/outputs/lattice_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Room-temperature lattice thermal conductivity for each monolayer and direction.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `direction`, `kappa_l`
  - `units`:
    - `kappa_l`: W/m/K

### zt_700K.csv
- path: `/app/outputs/zt_700K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum figure of merit ZT at 700 K for each monolayer and direction.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `direction`, `ZT`

Notes: All scored CSV files must follow the exact column specifications. Values for S_max, kappa_l, and ZT will be compared to reference results by a hidden verifier. The phonon stability file is validated by checking that min_frequency > 0 for every compound.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "seebeck_max_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "S_max"
        ],
        "units": {
          "S_max": "μV/K"
        }
      },
      "description": "Maximum absolute Seebeck coefficient at 300 K for each monolayer."
    },
    {
      "file": "phonon_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "min_frequency"
        ],
        "units": {
          "min_frequency": "THz"
        }
      },
      "description": "Minimum phonon frequency per compound; must be positive (no imaginary modes)."
    },
    {
      "file": "lattice_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "direction",
          "kappa_l"
        ],
        "units": {
          "kappa_l": "W/m/K"
        }
      },
      "description": "Room-temperature lattice thermal conductivity for each monolayer and direction."
    },
    {
      "file": "zt_700K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "direction",
          "ZT"
        ]
      },
      "description": "Maximum figure of merit ZT at 700 K for each monolayer and direction."
    }
  ],
  "notes": "All scored CSV files must follow the exact column specifications. Values for S_max, kappa_l, and ZT will be compared to reference results by a hidden verifier. The phonon stability file is validated by checking that min_frequency > 0 for every compound."
}
```

## How you are scored

A hidden verifier will independently examine the scored CSV files you placed under `/app/outputs`. It will compare your reported lattice thermal conductivities, Seebeck coefficients, and ZT values to reference results within appropriate tolerances, and also check the phonon stability (no negative frequencies). Each scored artifact carries a weight, and the final reward is a weighted combination. Simply reporting known numbers without running the required simulations will not satisfy the objective; the verifier may also audit process evidence to ensure the pipeline was genuinely executed.
