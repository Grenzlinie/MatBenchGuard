# Interatomic potential fitting and defect calculations in YAlO3 single crystal using GULP

## Problem background
Yttrium orthoaluminate (YAlO₃, also known as YAP) is a perovskite-like crystal widely employed as a host for laser and scintillator materials. Its optical and electronic performance is sensitive to intrinsic point defects – vacancies, interstitials, and antisite substitutions – that can form during crystal growth or under external stimuli. Experimental identification of the dominant defect types and their energetics is difficult, but atomistic static-lattice simulations using interatomic potentials and Mott-Littleton defect modelling can provide quantitative predictions of defect formation energies, disorder stability, redox behaviour, and oxygen-ion mobility. This task aims to reproduce such a complete set of computed defect-related properties for YAlO₃ using the public GULP simulation code.

## Approach
The work employs the General Utility Lattice Program (GULP) to perform all simulations within a Born-like shell-model framework. The strategy unfolds in several stages.  
First, short-range Buckingham potentials for O²⁻–O²⁻, O²⁻–Al³⁺, and O²⁻–Y³⁺ pairs, together with shell-model parameters (shell charge Y and spring constant k) for oxide, aluminium, and yttrium ions, are derived by a relaxed fitting procedure against experimentally known crystal properties of orthorhombic YAlO₃ (space group Pnma, unit cell dimensions, static and high-frequency dielectric constants, and density).  
With the optimized potentials, a lattice energy minimization of the perfect YAlO₃ unit cell is carried out; the relaxed cell parameters, interatomic distances, dielectric constants, and density serve as validation against the experimental inputs.  
Defect calculations employ the Mott-Littleton method with an inner-region radius of 8.5 Å to obtain formation energies of isolated vacancies and interstitials, from which Frenkel, Schottky, and antisite disorder energies per defect are computed.  
To treat redox reactions, electronic defects are modelled as O⁻ on an O²⁻ site (hole) and Y²⁺ on a Y³⁺ site (electron); the short-range interactions are taken to be the same as those of the host ions, and standard auxiliary thermochemical data (electron affinities, O₂ dissociation energy, ionization potentials) are incorporated to evaluate the energies of oxidation via vacancy filling, oxidation via interstitial oxygen, and reduction.  
Finally, oxygen vacancy migration is investigated by estimating saddle-point energies for the 12 distinct oxygen–oxygen jump paths around the AlO₆ octahedron, yielding activation energies for each pathway.

## Reproduction target
Using the GULP program and the specified experimental crystal data and auxiliary thermodynamic numbers, compute and output the following quantities as structured JSON files:  
1. **Fitted interatomic potential parameters** – the final short-range Buckingham parameters and shell-model parameters obtained after relaxed fitting.  
2. **Perfect crystal properties** – lattice energy, unit cell dimensions, interatomic distances, static and high-frequency dielectric constants, and density computed with the fitted potential.  
3. **Intrinsic defect energies** – formation energies of isolated point defects (vacancies, interstitials, antisites) and derived Frenkel, Schottky, and antisite disorder energies per defect.  
4. **Redox reaction energies** – electronic defect formation energies (hole and electron) and the reaction energies for the three redox processes defined in the workflow.  
5. **Oxygen vacancy migration barriers** – activation energies for all 12 distinct jump paths along the edges of the AlO₆ octahedron.  
All files must be placed in `/app/outputs` with the exact names and schemas given in the output contract.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Experimental YAlO3 crystal properties
- Standard auxiliary thermodynamic data

## Workflow steps

### Step 1: Fit interatomic potentials for YAlO3
- Role: scored
- Action: Fit short-range Buckingham potentials (O²⁻–O²⁻, O²⁻–Al³⁺, O²⁻–Y³⁺) and shell-model parameters (Y, k) for O²⁻, Al³⁺, Y³⁺ to experimental YAlO3 crystal properties (space group Pnma, a=5.33 Å, b=7.375 Å, c=5.18 Å, static dielectric constant 16.00, high-frequency dielectric constant 3.83, density 5.35 g/cm³) using relaxed fitting in GULP. Output the fitted potential parameters to potential_parameters.json.
- Output file: `/app/outputs/potential_parameters.json`
- Format: json
- Contract: JSON object with keys: short_range (array of objects {interaction: string, A: float, rho: float, C: float}), shell (array of objects {species: string, Y: float, k: float})
- Scoring: scored by hidden verifier

### Step 2: Compute perfect crystal properties
- Role: scored
- Action: Using the fitted potential, perform lattice energy minimization of the YAlO3 unit cell and compute lattice energy, unit cell parameters (a,b,c), interatomic distances (Y–Y, Al–Al, Y–Al, Al–O, Y–O), static and high-frequency dielectric constants, and density. Output to perfect_crystal_results.json.
- Output file: `/app/outputs/perfect_crystal_results.json`
- Format: json
- Contract: JSON object with keys: lattice_energy (eV), unit_cell {a, b, c (Å)}, interatomic_distances (array of {pair, distance}), static_dielectric (float), high_frequency_dielectric (float), density (g/cm³)
- Scoring: scored by hidden verifier

### Step 3: Calculate intrinsic defect energies
- Role: scored
- Action: Using the fitted potential and the Mott-Littleton method (region I radius 8.5 Å) in GULP, compute formation energies of isolated point defects (VO, VAl, VY, Oi, Ali, Yi, YAl, AlY). Then calculate Frenkel (oxygen, yttrium, aluminium), Schottky (YAlO3, Al2O3, Y2O3 partial Schottky), and antisite disorder energies per defect. Output to intrinsic_defect_energies.json.
- Output file: `/app/outputs/intrinsic_defect_energies.json`
- Format: json
- Contract: JSON object with keys: isolated (array of {defect, energy}), frenkel (array of {type, energy_per_defect}), schottky (array of {type, energy_per_defect})
- Scoring: scored by hidden verifier

### Step 4: Analyze redox reactions
- Role: scored
- Action: Model electronic defects: hole as O⁻ on an O²⁻ site, electron as Y²⁺ on a Y³⁺ site, using the same short-range interactions as the host ions. Incorporate auxiliary energies: electron affinities of O²⁻ (EA1=1.47 eV, EA2=-8.75 eV), O₂ dissociation energy (5.16 eV), and Y ionization potentials (IP2=12.24 eV, IP3=20.52 eV). Compute formation energies of hole and electron defects, then calculate reaction energies for: oxidation via vacancy filling, oxidation via interstitial oxygen, and reduction. Output to redox_energies.json.
- Output file: `/app/outputs/redox_energies.json`
- Format: json
- Contract: JSON object with keys: electronic_defects {hole_formation, electron_formation, hole_defect_energy, electron_defect_energy}, redox {oxidation_vacancy_filling, oxidation_interstitial_oxygen, reduction}
- Scoring: scored by hidden verifier

### Step 5: Compute oxygen vacancy migration barriers
- Role: scored (load-bearing)
- Action: Compute activation energies for oxygen vacancy migration along 12 distinct pathways (edges of the AlO6 octahedron) by placing an oxygen ion at the saddle point between adjacent oxygen sites and calculating the energy difference relative to the stable vacancy. Output to migration_barriers.json.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: JSON object with key pathways: array of {jump_path, activation_energy}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potential_parameters.json`
- `/app/outputs/perfect_crystal_results.json`
- `/app/outputs/intrinsic_defect_energies.json`
- `/app/outputs/redox_energies.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potential_parameters.json
- path: `/app/outputs/potential_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted short-range Buckingham and shell-model potential parameters for YAlO3.
- schema:
  - `type`: object
  - `required`:
    - `short_range`: array of objects {interaction: string, A: float (eV), rho: float (Å), C: float (eV·Å⁶)}
    - `shell`: array of objects {species: string, Y: float (e), k: float (eV·Å⁻²)}

### perfect_crystal_results.json
- path: `/app/outputs/perfect_crystal_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Perfect crystal properties computed with the fitted potential, benchmarked against experimental data.
- schema:
  - `type`: object
  - `required`:
    - `lattice_energy`: float (eV)
    - `unit_cell`: object {a: float (Å), b: float (Å), c: float (Å)}
    - `interatomic_distances`: array of objects {pair: string, distance: float (Å)}
    - `static_dielectric`: float (unitless)
    - `high_frequency_dielectric`: float (unitless)
    - `density`: float (g/cm³)

### intrinsic_defect_energies.json
- path: `/app/outputs/intrinsic_defect_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation energies of isolated point defects, Frenkel disorder, Schottky disorder, and antisite defects.
- schema:
  - `type`: object
  - `required`:
    - `isolated`: array of objects {defect: string, energy: float (eV)}
    - `frenkel`: array of objects {type: string, energy_per_defect: float (eV)}
    - `schottky`: array of objects {type: string, energy_per_defect: float (eV)}

### redox_energies.json
- path: `/app/outputs/redox_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic defect energies (hole, electron) and redox reaction energies (oxidation and reduction).
- schema:
  - `type`: object
  - `required`:
    - `electronic_defects`: object {hole_formation: float (eV), electron_formation: float (eV), hole_defect_energy: float (eV), electron_defect_energy: float (eV)}
    - `redox`: object {oxidation_vacancy_filling: float (eV), oxidation_interstitial_oxygen: float (eV), reduction: float (eV)}

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Oxygen vacancy migration activation energies along 12 distinct pathways in the AlO6 octahedron.
- schema:
  - `type`: object
  - `required`:
    - `pathways`: array of objects {jump_path: string, activation_energy: float (eV)}

Notes: All numeric values are compared against the paper's reported gold values with appropriate hidden tolerances (absolute for bond lengths/dielectric/density/barriers, percentage for potential parameters). The checker verifies that each required field is present and within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potential_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "short_range": "array of objects {interaction: string, A: float (eV), rho: float (Å), C: float (eV·Å⁶)}",
          "shell": "array of objects {species: string, Y: float (e), k: float (eV·Å⁻²)}"
        }
      },
      "description": "Fitted short-range Buckingham and shell-model potential parameters for YAlO3."
    },
    {
      "file": "perfect_crystal_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_energy": "float (eV)",
          "unit_cell": "object {a: float (Å), b: float (Å), c: float (Å)}",
          "interatomic_distances": "array of objects {pair: string, distance: float (Å)}",
          "static_dielectric": "float (unitless)",
          "high_frequency_dielectric": "float (unitless)",
          "density": "float (g/cm³)"
        }
      },
      "description": "Perfect crystal properties computed with the fitted potential, benchmarked against experimental data."
    },
    {
      "file": "intrinsic_defect_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "isolated": "array of objects {defect: string, energy: float (eV)}",
          "frenkel": "array of objects {type: string, energy_per_defect: float (eV)}",
          "schottky": "array of objects {type: string, energy_per_defect: float (eV)}"
        }
      },
      "description": "Formation energies of isolated point defects, Frenkel disorder, Schottky disorder, and antisite defects."
    },
    {
      "file": "redox_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "electronic_defects": "object {hole_formation: float (eV), electron_formation: float (eV), hole_defect_energy: float (eV), electron_defect_energy: float (eV)}",
          "redox": "object {oxidation_vacancy_filling: float (eV), oxidation_interstitial_oxygen: float (eV), reduction: float (eV)}"
        }
      },
      "description": "Electronic defect energies (hole, electron) and redox reaction energies (oxidation and reduction)."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pathways": "array of objects {jump_path: string, activation_energy: float (eV)}"
        }
      },
      "description": "Oxygen vacancy migration activation energies along 12 distinct pathways in the AlO6 octahedron."
    }
  ],
  "notes": "All numeric values are compared against the paper's reported gold values with appropriate hidden tolerances (absolute for bond lengths/dielectric/density/barriers, percentage for potential parameters). The checker verifies that each required field is present and within tolerance."
}
```

## How you are scored
A hidden verifier independently evaluates each of your five JSON artifacts. For every artifact, it first checks that the required fields and data types are present, then compares your computed numeric values against the reference values produced by a faithful execution of the described workflow. Comparisons are made using tolerances that account for the legitimate run-to-run spread caused by different compilation environments, numerical settings, and minor implementation choices; these tolerances are set so that only a genuine simulation yields values within the acceptable range. The scores from the five stages are weighted equally (each contributing 0.2 to the total reward) and combined into a final score between 0.0 and 1.0. Reporting numbers that are not actually generated by the required calculations will result in a very low score, because the verifier's tolerances distinguish real simulation output from guesses or manually transcribed values.
