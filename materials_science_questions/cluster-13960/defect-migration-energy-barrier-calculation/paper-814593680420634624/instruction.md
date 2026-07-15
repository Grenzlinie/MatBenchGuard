# Influence of Dislocation Strain Fields on Fe Impurity Diffusion in Silicon

## Problem background
Interstitial iron impurities in silicon are detrimental to solar cell efficiency because they act as efficient recombination centers for photogenerated charge carriers. Previous work has suggested that mechanical strain, e.g., associated with lattice defects such as dislocations, can modify the diffusion of interstitial Fe atoms. Understanding how dislocation strain fields influence the local migration barriers and effective diffusion of interstitial Fe in crystalline Si is important for predicting impurity gettering and recombination activity in multicrystalline silicon.

## Approach
To determine the influence of strain on Fe migration, we first compute the variation of defect formation energies and elementary migration barriers for Fe jumps between interstitial sites in silicon using density functional theory (DFT) within the generalized-gradient approximation. Supercells of 64 Si atoms are employed with a set of uniform strain modes (hydrostatic, uniaxial along several directions, and shear) at magnitudes of -5%, 0%, and +5%. The minimum-energy paths and corresponding energy barriers are obtained with the nudged-elastic-band (NEB) and climbing-image NEB methods as implemented in Quantum Espresso/ASE. From these barriers, a lattice-based kinetic Monte Carlo (kMC) model is constructed using fixed attempt frequencies to compute the effective diffusion coefficient relative to the unstrained bulk at 100 K and 300 K. The barrier changes are then parameterized as polynomial functions of the relevant strain components. These parameterizations are subsequently applied to the linear-elastic strain fields of four representative dislocations in Si (perfect screw, 60° mixed, 30° partial, and 90° partial dislocations) to obtain spatial maps of local migration barriers for each <111> jump direction, excluding a core region of 5 Å radius. From these maps, the angle-averaged migration-rate ratio λ(r) is computed for the two half-spaces above and below the dislocation glide planes, quantifying the anisotropic modification of diffusion.

## Reproduction target
The goal is to reproduce a series of six quantitative artifacts that characterize the migration of interstitial Fe in strained Si and around dislocations: (1) formation energies of Fe interstitial and substitutional defects and the Si vacancy under uniform strain; (2) migration energy barriers for Fe jumps between tetrahedral and hexagonal interstitial sites under uniform strain; (3) effective relative diffusion coefficients D/D_bulk from kMC for each uniform strain state at 100 K and 300 K; (4) polynomial coefficients that describe the strain-dependence of the normalized migration barrier e_s(ε) for each strain component and migration direction; (5) two-dimensional maps of local migration barriers (eV) around the four dislocation types on a grid spanning ±200 Å from the dislocation core (core region r < 5 Å excluded); (6) angle-averaged migration-rate ratios λ(r) as a function of radial distance for each dislocation type, half-space (above/below glide plane), and temperature (100 K, 300 K).

## Assets

- Quantum Espresso (PWscf): https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
- Ultrasoft pseudopotentials for Si and Fe (PSLibrary): https://www.quantum-espresso.org/pseudopotentials
- NumPy, SciPy, Matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: DFT formation energies under strain
- Role: scored
- Action: Compute total energies of Fe defect configurations (tetrahedral, hexagonal, substitutional) and Si vacancy in a 64-atom Si supercell under hydrostatic, uniaxial ([100], [110], [111], [112]) and shear strains at magnitudes -5%, 0, +5%, using DFT with standard pseudopotentials. Extract formation energies from total energies using appropriate chemical potentials.
- Output file: `/app/outputs/step_01_formation_energies.csv`
- Format: csv
- Contract: CSV columns: strain_type, strain_value, defect_config, formation_energy_eV
- Scoring: scored by hidden verifier

### Step 2: NEB/CI-NEB migration barriers under strain
- Role: scored
- Action: Using the same supercell and strain states as step_01, compute the minimum energy path and energy barrier for Fe jumps between tetrahedral and hexagonal interstitial sites along each of the four <111> migration directions with the NEB and CI-NEB method, as implemented in Quantum Espresso/ASE.
- Output file: `/app/outputs/step_02_migration_barriers_uniform.csv`
- Format: csv
- Contract: CSV columns: strain_type, strain_value, migration_direction, barrier_TET_HEX_eV, barrier_HEX_TET_eV
- Scoring: scored by hidden verifier

### Step 3: kMC effective diffusion coefficients
- Role: scored
- Action: Using the computed migration barriers and fixed frequency factors (30 THz for TET->HEX, 18 THz for HEX->TET), perform lattice-based kinetic Monte Carlo simulations for each uniform strain state to obtain the effective relative diffusion coefficient D/D_bulk at temperatures 100 K and 300 K. Run sufficient kMC steps to reduce stochastic noise below 1%.
- Output file: `/app/outputs/step_03_diffusion_coeffs.csv`
- Format: csv
- Contract: CSV columns: strain_type, temperature_K, D_over_Dbulk
- Scoring: scored by hidden verifier

### Step 4: Polynomial fit of barrier strain-dependence
- Role: scored
- Action: For each strain component needed to describe dislocation strain fields (dilatational and shear components as in the relevant paper figure), fit a polynomial function e_s(epsilon) = Delta E(epsilon)/Delta E_bulk to the migration barriers obtained in step_02 for each of the four <111> migration directions. Provide the polynomial coefficients.
- Output file: `/app/outputs/step_04_barrier_fits.json`
- Format: json
- Contract: JSON object mapping each strain_component to an array of four coefficient arrays (one per migration direction), where each coefficient array represents the polynomial e_s(epsilon) = c0 + c1*epsilon + c2*epsilon^2 + ...
- Scoring: scored by hidden verifier

### Step 5: Local migration barrier maps around dislocations
- Role: scored (load-bearing)
- Action: Apply the parameterized barrier functions from step_04 to the linear-elastic strain fields of perfect screw, 60° mixed, 30° partial, and 90° partial dislocations (using analytical expressions from dislocation theory). For spatial positions (x,y) in the plane perpendicular to the dislocation line, excluding a core region of radius 5 Å, compute the local migration barrier Delta E for each <111> direction using the multiplicative composition rule. Save the resulting barrier values on a grid covering at least ±200 Å.
- Output file: `/app/outputs/step_05_dislocation_barriers.csv`
- Format: csv
- Contract: CSV columns: dislocation_type, x_angstrom, y_angstrom, migration_direction, barrier_eV
- Scoring: scored by hidden verifier

### Step 6: Angle-averaged migration-rate ratios
- Role: scored
- Action: From the local barrier maps of step_05, compute the angle-averaged relative migration-rate ratio lambda(r) and the half-space integrated profiles lambda_a(r) and lambda_b(r) for the upper (a) and lower (b) regions relative to the glide plane for each dislocation type at T=100 K and T=300 K. Use the given bulk migration barrier.
- Output file: `/app/outputs/step_06_lambda_radial.csv`
- Format: csv
- Contract: CSV columns: dislocation_type, radius_angstrom, halfspace, temperature_K, lambda
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.csv`
- `/app/outputs/step_02_migration_barriers_uniform.csv`
- `/app/outputs/step_03_diffusion_coeffs.csv`
- `/app/outputs/step_04_barrier_fits.json`
- `/app/outputs/step_05_dislocation_barriers.csv`
- `/app/outputs/step_06_lambda_radial.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.csv
- path: `/app/outputs/step_01_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies of Fe defects and Si vacancy under various strains.
- schema:
  - `type`: table
  - `required_columns`: `strain_type`, `strain_value`, `defect_config`, `formation_energy_eV`

### step_02_migration_barriers_uniform.csv
- path: `/app/outputs/step_02_migration_barriers_uniform.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Migration barriers for Fe jumps between interstitial sites under strain.
- schema:
  - `type`: table
  - `required_columns`: `strain_type`, `strain_value`, `migration_direction`, `barrier_TET_HEX_eV`, `barrier_HEX_TET_eV`

### step_03_diffusion_coeffs.csv
- path: `/app/outputs/step_03_diffusion_coeffs.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative diffusion coefficients from kMC for uniaxially strained states.
- schema:
  - `type`: table
  - `required_columns`: `strain_type`, `temperature_K`, `D_over_Dbulk`

### step_04_barrier_fits.json
- path: `/app/outputs/step_04_barrier_fits.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Polynomial coefficients for barrier strain-dependence functions e_s(epsilon).
- schema:
  - `type`: object
  - `required`: JSON keys representing strain components (e.g., eps_x, tau_xy), each mapping to an array of four coefficient arrays.

### step_05_dislocation_barriers.csv
- path: `/app/outputs/step_05_dislocation_barriers.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Two-dimensional maps of local migration barriers around dislocations.
- schema:
  - `type`: table
  - `required_columns`: `dislocation_type`, `x_angstrom`, `y_angstrom`, `migration_direction`, `barrier_eV`

### step_06_lambda_radial.csv
- path: `/app/outputs/step_06_lambda_radial.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angle-averaged migration-rate ratios lambda(r) for each dislocation half-space and temperature.
- schema:
  - `type`: table
  - `required_columns`: `dislocation_type`, `radius_angstrom`, `halfspace`, `temperature_K`, `lambda`

Notes: Phonon frequency factors for kMC are taken as given constants (30 THz for TET->HEX, 18 THz for HEX->TET) from the paper's analysis; their separate recomputation is not required. All steps rely on publicly available codes and standard pseudopotentials. The agent is expected to use external compute resources for the DFT+NEB simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_type",
          "strain_value",
          "defect_config",
          "formation_energy_eV"
        ]
      },
      "description": "Formation energies of Fe defects and Si vacancy under various strains."
    },
    {
      "file": "step_02_migration_barriers_uniform.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_type",
          "strain_value",
          "migration_direction",
          "barrier_TET_HEX_eV",
          "barrier_HEX_TET_eV"
        ]
      },
      "description": "Migration barriers for Fe jumps between interstitial sites under strain."
    },
    {
      "file": "step_03_diffusion_coeffs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_type",
          "temperature_K",
          "D_over_Dbulk"
        ]
      },
      "description": "Relative diffusion coefficients from kMC for uniaxially strained states."
    },
    {
      "file": "step_04_barrier_fits.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": "JSON keys representing strain components (e.g., eps_x, tau_xy), each mapping to an array of four coefficient arrays."
      },
      "description": "Polynomial coefficients for barrier strain-dependence functions e_s(epsilon)."
    },
    {
      "file": "step_05_dislocation_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "dislocation_type",
          "x_angstrom",
          "y_angstrom",
          "migration_direction",
          "barrier_eV"
        ]
      },
      "description": "Two-dimensional maps of local migration barriers around dislocations."
    },
    {
      "file": "step_06_lambda_radial.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "dislocation_type",
          "radius_angstrom",
          "halfspace",
          "temperature_K",
          "lambda"
        ]
      },
      "description": "Angle-averaged migration-rate ratios lambda(r) for each dislocation half-space and temperature."
    }
  ],
  "notes": "Phonon frequency factors for kMC are taken as given constants (30 THz for TET->HEX, 18 THz for HEX->TET) from the paper's analysis; their separate recomputation is not required. All steps rely on publicly available codes and standard pseudopotentials. The agent is expected to use external compute resources for the DFT+NEB simulations."
}
```

## How you are scored
Each of the six output artifact files is independently evaluated by a hidden scoring function. The verifier compares your computed quantities to reference values derived from the described procedure and assigns a score per artifact. The final reward is a weighted combination of these individual scores. The evaluation may check both absolute and relative quantities at specified conditions or hidden test points. To obtain the highest reward, you must correctly compute the entire pipeline, from DFT barriers through kMC and polynomial fits to the dislocation-field calculations, producing numerically consistent results that reflect the underlying physics. Copying or guessing reported numbers is insufficient; the scoring emphasizes fidelity to the computational model and procedure.
