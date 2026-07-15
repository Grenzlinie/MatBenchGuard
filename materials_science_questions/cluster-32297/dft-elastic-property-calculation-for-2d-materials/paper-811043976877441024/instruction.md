# First-principles thermoelectric properties of 2D monochalcogenides

## Problem background
Thermoelectric materials convert waste heat into electricity via the Seebeck effect. Their performance is quantified by the dimensionless figure of merit $ZT = \sigma S^2 T / \kappa$, which depends on the electrical conductivity $\sigma$, the Seebeck coefficient $S$, the absolute temperature $T$, and the total thermal conductivity $\kappa = \kappa_e + \kappa_l$ (electronic and lattice contributions). A high $ZT$ requires a large Seebeck coefficient, high electrical conductivity, and low thermal conductivity — properties that are often in conflict.

Reducing dimensionality is a promising route to enhance $ZT$, and two-dimensional IV–VI monochalcogenides (SnSe, SnS, GeSe, GeS) have recently attracted interest because of their potentially superior thermoelectric performance compared to their bulk counterparts. This task evaluates the thermoelectric transport properties and dynamical stability of these four monolayer compounds using first-principles calculations combined with Boltzmann transport theory.

## Approach
The core idea is to compute the electronic and phononic transport properties of each monolayer from density functional theory (DFT) and then combine them into the thermoelectric figure of merit $ZT$. The approach proceeds in several stages:

1. **Crystal structure relaxation:** The monolayer structures are built in the Pmn2₁ space group and relaxed with DFT using a semilocal exchange-correlation functional that includes van der Waals corrections.

2. **Electronic structure and effective masses:** Band structures and densities of states are computed, from which the band gaps and the conduction-band effective masses along the armchair and zigzag directions are extracted.

3. **Deformation potential mobility:** The carrier mobility and the associated relaxation time are obtained from deformation potential theory. This requires computing the two-dimensional elastic constant (from energy‑strain fits) and the deformation potential constant (from the shift of the conduction band edge under uniaxial strain) along both transport directions.

4. **Electron Boltzmann transport:** Using a dense k‑point mesh, the Boltzmann transport equation for electrons is solved within the rigid‑band and constant‑relaxation‑time approximations to obtain the Seebeck coefficient $S$ and the ratios $\sigma/\tau$ and $\kappa_e/\tau$. The results are then scaled by the temperature‑dependent relaxation times to give absolute electrical and electronic thermal conductivities.

5. **Phonon transport and stability:** Harmonic interatomic force constants are computed with density‑functional perturbation theory, yielding phonon dispersions that verify vibrational stability (absence of imaginary frequencies). Third‑order anharmonic force constants are obtained from finite‑displacement DFT calculations. These harmonic and anharmonic constants are fed into a solver of the phonon Boltzmann transport equation to compute the lattice thermal conductivity $\kappa_l$ as a function of temperature and direction.

6. **Figure of merit:** Finally, the electronic transport coefficients from step 4 and the lattice thermal conductivity from step 5 are combined to compute $ZT$ as a function of carrier concentration, and the maximum $ZT$ is reported for each material, direction, and temperature.

## Reproduction target
Produce the following three output artifacts by executing the workflow described in the steps below:

- **ZT table** (`/app/outputs/zt_table.csv`): For each of the four monolayer materials (SnSe, SnS, GeSe, GeS) and for each transport direction (armchair, zigzag), report the maximum value of $ZT$ achieved at temperatures of 300 K, 500 K, and 700 K. The maximum $ZT$ should be identified from a scan over carrier concentration.

- **Room‑temperature lattice thermal conductivity** (`/app/outputs/lattice_thermal_conductivity.csv`): For each material and direction, report the lattice thermal conductivity $\kappa_l$ at 300 K.

- **Dynamical stability** (`/app/outputs/phonon_stability.json`): Indicate whether the monolayers are vibrationally stable by checking that no imaginary phonon frequencies appear anywhere along the high‑symmetry path. Write `{"dynamically_stable": true}` if stable, `false` otherwise.

All results must originate from the computational pipeline; no pre‑existing results or experimental data are used.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- BoltzTraP2: BoltzTraP2
- Phonopy: phonopy
- ShengBTE: https://www.shengbte.net/
- spglib: spglib
- Atomic Simulation Environment (ASE): ase
- SSSP efficiency PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Build monolayer structures of SnSe, SnS, GeSe, and GeS in space group Pmn2₁ using literature lattice parameters. Perform DFT geometry relaxation with the PBE functional and van der Waals correction (vdW‑DF) until forces on each atom are negligible. Include sufficient vacuum in the out‑of‑plane direction.
- Evidence: none

### Step 2: Electronic structure and effective masses
- Role: process
- Action: Compute band structure on the Γ‑X‑S‑Y high‑symmetry path and density of states for each relaxed monolayer. Extract the band gap and the effective masses of the conduction band along armchair and zigzag directions.
- Evidence: none

### Step 3: Dense k‑point SCF for BoltzTraP
- Role: process
- Action: Run a non‑self‑consistent DFT calculation using the relaxed geometry and a dense k‑mesh appropriate for transport calculations. Save the Kohn‑Sham eigenvalues on this mesh as input for BoltzTraP.
- Evidence: none

### Step 4: Strain‑dependent DFT for elastic and deformation potentials
- Role: process
- Action: Apply uniaxial strains along the armchair and zigzag directions to the unit cell. For each strain, compute total energy and the shift of the conduction band minimum. Fit the energy‑strain data to obtain the 2D elastic constant and fit the band‑edge shift to obtain the deformation potential constant.
- Evidence: none

### Step 5: Mobility and relaxation time
- Role: process
- Action: Using deformation potential theory, compute the carrier mobility and the relaxation time at T = 300, 500, and 700 K for each material and each transport direction. Use the effective masses, 2D elastic constant, and deformation potential obtained in earlier steps.
- Evidence: none

### Step 6: BoltzTraP electronic transport
- Role: process
- Action: Feed the dense‑mesh eigenvalues and the temperatures 300, 500, 700 K into BoltzTraP under the rigid‑band and constant‑τ approximations. Obtain the Seebeck coefficient S, σ/τ, and κ_e/τ as functions of carrier concentration for both armchair and zigzag directions.
- Evidence: none

### Step 7: Harmonic IFCs and phonon dispersion
- Role: process
- Action: Build a supercell of appropriate size and compute the second‑order (harmonic) interatomic force constants using density‑functional perturbation theory (DFPT) as implemented in Phonopy. Obtain the phonon dispersion curves along high‑symmetry lines.
- Evidence: none

### Step 8: Third‑order IFC calculation
- Role: process
- Action: Build a supercell of appropriate size and compute the third‑order (anharmonic) interatomic force constants including interactions up to the 15th nearest neighbor, using finite‑displacement DFT calculations with the same functional.
- Evidence: none

### Step 9: ShengBTE lattice thermal conductivity
- Role: process
- Action: Supply the harmonic and third‑order IFCs to ShengBTE to solve the phonon Boltzmann transport equation using both iterative and relaxation‑time approximation methods. Obtain the lattice thermal conductivity κ_l as a function of temperature and direction for each material.
- Evidence: none

### Step 10: Scale electronic conductivities
- Role: process
- Action: Multiply the σ/τ and κ_e/τ curves obtained from BoltzTraP by the temperature‑dependent relaxation time τ(T) computed earlier to obtain absolute electrical conductivity σ and electronic thermal conductivity κ_e.
- Evidence: none

### Step 11: Dynamical stability assertion
- Role: scored
- Action: Examine the phonon dispersion from the harmonic calculation. If there are NO branches with imaginary frequencies anywhere along the high‑symmetry path, write phonon_stability.json with {"dynamically_stable": true}; otherwise write false.
- Output file: `/app/outputs/phonon_stability.json`
- Format: json
- Contract: {"dynamically_stable": <boolean>}
- Scoring: scored by hidden verifier

### Step 12: Room‑temperature lattice thermal conductivity table
- Role: scored (load-bearing)
- Action: From the ShengBTE results, extract the room‑temperature (300 K) lattice thermal conductivity κ_l for each material and each direction. Save as lattice_thermal_conductivity.csv with columns: material, direction, kappa_l.
- Output file: `/app/outputs/lattice_thermal_conductivity.csv`
- Format: csv
- Contract: CSV with columns: material (SnSe,SnS,GeSe,GeS), direction (armchair,zigzag), kappa_l (float, W/mK)
- Scoring: scored by hidden verifier

### Step 13: ZT table
- Role: scored (load-bearing)
- Action: Using the Seebeck coefficient from step 6, absolute electrical and electronic thermal conductivities from step 10, and lattice thermal conductivity from step 9, calculate ZT = σ S² T / (κ_e + κ_l) as a function of carrier concentration. Identify the maximum ZT for each material, transport direction, and temperature (300 K, 500 K, 700 K). Save as zt_table.csv with columns: material, direction, temperature_K, ZT.
- Output file: `/app/outputs/zt_table.csv`
- Format: csv
- Contract: CSV with columns: material (SnSe,SnS,GeSe,GeS), direction (armchair,zigzag), temperature_K (300,500,700), ZT (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_stability.json`
- `/app/outputs/lattice_thermal_conductivity.csv`
- `/app/outputs/zt_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_stability.json
- path: `/app/outputs/phonon_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Indicates whether the monolayers are vibrationally stable (true if no imaginary phonon frequencies).
- schema:
  - `type`: object
  - `required`:
    - `dynamically_stable`: boolean

### lattice_thermal_conductivity.csv
- path: `/app/outputs/lattice_thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Room‑temperature lattice thermal conductivities for each material and direction.
- schema:
  - `type`: table
  - `required_columns`: `material`, `direction`, `kappa_l`
  - `units`:
    - `kappa_l`: W/mK

### zt_table.csv
- path: `/app/outputs/zt_table.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Maximum ZT values for each material, direction, and temperature.
- schema:
  - `type`: table
  - `required_columns`: `material`, `direction`, `temperature_K`, `ZT`
  - `units`:
    - `ZT`: dimensionless

Notes: All outputs are produced from first-principles calculations using the workflow described in the steps; no external experimental data is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "dynamically_stable": "boolean"
        }
      },
      "description": "Indicates whether the monolayers are vibrationally stable (true if no imaginary phonon frequencies)."
    },
    {
      "file": "lattice_thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "direction",
          "kappa_l"
        ],
        "units": {
          "kappa_l": "W/mK"
        }
      },
      "description": "Room‑temperature lattice thermal conductivities for each material and direction."
    },
    {
      "file": "zt_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "direction",
          "temperature_K",
          "ZT"
        ],
        "units": {
          "ZT": "dimensionless"
        }
      },
      "description": "Maximum ZT values for each material, direction, and temperature."
    }
  ],
  "notes": "All outputs are produced from first-principles calculations using the workflow described in the steps; no external experimental data is required."
}
```

## How you are scored
A hidden verifier independently examines each of your three output files. The verifier compares your submitted values for ZT and lattice thermal conductivity to hidden reference values derived from the original study, using tolerances that allow for implementation‑dependent differences (different DFT code, solver settings) while still rejecting random or guessed numbers. The dynamical stability boolean is checked for correctness.

The scores from the three artifacts are combined with predefined weights: the ZT table and the lattice thermal conductivity table carry the primary weight, while the stability assertion has a smaller contribution. Your overall reward is a continuous value between 0 and 1.

Because the tolerances are set to require results that are consistent with those obtained from the actual first‑principles pipeline, merely reporting numbers without executing the full computation will not yield a passing score.
