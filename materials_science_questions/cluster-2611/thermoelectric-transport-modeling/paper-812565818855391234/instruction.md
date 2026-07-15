# First-Principles Thermoelectric Transport Properties of Quaternary Heusler Alloys

## Problem background
In spin-caloritronics, the spin-Seebeck effect enables conversion of heat into spin currents in magnetic materials. This task investigates a family of quaternary Heusler alloys with composition CoFeRGa (R = Ti, V, Cr, Mn, Cu, Nb) that can exhibit a range of electronic phases—semiconductor, half-metal, spin-gapless semiconductor, near half-metal, and metal—depending on the R element. Understanding how the chemical composition controls the electronic structure, magnetism, and especially the spin-Seebeck coefficient is key for designing efficient spin-caloritronic devices. Your goal is to compute these properties from first principles, analyze how they vary across the series, and determine which alloy shows the largest spin-Seebeck effect at room temperature.

## Approach
Use spin-polarized density functional theory (DFT) to calculate the electronic structure of each CoFeRGa compound in its ground-state crystal structure. Because accurate band-edge energies are crucial for transport, employ the modified Becke-Johnson (mBJ) potential or the HSE06 hybrid functional to correct the band gap. After obtaining spin-resolved band structures and magnetic moments, run the Boltzmann transport equation within the constant relaxation-time approximation (via BoltzTraP) to compute the spin-up and spin-down Seebeck coefficients. The spin-Seebeck coefficient is then obtained from the spin-resolved conductivities and Seebeck coefficients using a two-current model. As secondary checks, determine the elastic constants (and derived mechanical moduli) and compute the phonon dispersion to confirm dynamical stability (no imaginary phonon frequencies). The workflow compares all six compounds under the same computational conditions to reveal how the R atom influences the thermal spin response.

## Reproduction target
Main target: Compute the spin-Seebeck coefficient at 300 K for every CoFeRGa alloy (Ti, V, Cr, Mn, Cu, Nb) and identify the compound with the largest absolute spin-Seebeck coefficient, reporting its value.

Secondary targets, for all six compounds, to be reported in separate structured output files:
- Total magnetic moment per formula unit and atomic magnetic moments (Co, Fe, R, Ga), together with the lattice constant and electronic phase classification (CS, HM, SGS, nearly-HM, metal).
- Elastic constants c11, c12, c44 and the derived moduli (shear modulus G, bulk modulus B, Young’s modulus Y, Poisson’s ratio ν).
- Minimum phonon frequency across the Brillouin zone, indicating dynamical stability when positive (within a small tolerance).

All results must be generated from scratch using first-principles calculations; no pre-existing output files or intermediate data from the original paper are provided.

## Assets

- Quantum ESPRESSO or equivalent open-source DFT code: https://www.quantum-espresso.org/
- BoltzTraP: https://www.icams.de/content/research/software-development/boltztrap/
- Phonopy: https://phonopy.github.io/phonopy/
- Pseudopotential library (SSSP or PSlibrary): http://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Structural optimization and ground-state identification
- Role: process
- Action: For each CoFeRGa compound (R = Ti, V, Cr, Mn, Cu, Nb), perform spin-polarized DFT structural relaxations in the three possible Wyckoff arrangements (type-I, II, III) to determine the energetically most stable crystal structure and its equilibrium lattice constant. The calculation must be spin-polarized to correctly identify the ground-state magnetic ordering.
- Evidence: `/app/outputs/structure_optimization.log`

### Step 2: Elastic constants and mechanical moduli
- Role: scored
- Action: Using the optimized ground-state structures from step_01, compute the elastic constants c11, c12, c44 (in GPa) via density functional perturbation theory or stress-strain method. Derive the shear modulus G, bulk modulus B, Young's modulus Y, and Poisson's ratio ν using Voigt-Reuss-Hill averaging. Report results for all six CoFeRGa compounds.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"CoFeTiGa": {"c11": <float>, "c12": <float>, "c44": <float>, "G": <float>, "B": <float>, "Y": <float>, "ν": <float>}, "CoFeVGa": {...}, ...}
- Scoring: scored by hidden verifier

### Step 3: Dynamical stability (phonon minimum frequency)
- Role: scored
- Action: Calculate the phonon dispersion of each CoFeRGa compound using DFPT or finite-displacement methods on a supercell. Extract the minimum phonon frequency across the Brillouin zone for each alloy. Report the value in THz; a positive value (within small tolerance) indicates dynamical stability.
- Output file: `/app/outputs/phonon_min_freq.json`
- Format: json
- Contract: {"CoFeTiGa": <float>, "CoFeVGa": <float>, "CoFeCrGa": <float>, "CoFeMnGa": <float>, "CoFeCuGa": <float>, "CoFeNbGa": <float>}
- Scoring: scored by hidden verifier

### Step 4: Spin-polarized electronic structure and magnetic moments
- Role: scored
- Action: Perform a spin-polarized electronic structure calculation for the ground-state structure of each CoFeRGa compound using a functional that accurately predicts band-edge energetics (e.g., mBJ or HSE06). Extract the total magnetic moment per formula unit (μB/f.u.) and site-resolved atomic magnetic moments for Co, Fe, R, and Ga (μB/atom). Classify the electronic phase (CS, HM, SGS, nearly-HM, metal) based on the band structure. Report the data in a CSV file.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: Alloy,Type,a,M_Co,M_Fe,M_R,M_Ga,M_tot,Phase
- Scoring: scored by hidden verifier

### Step 5: Transport properties and spin-Seebeck coefficient
- Role: scored (load-bearing)
- Action: Using the spin-resolved band structure from step_04 as input, run BoltzTraP to compute the spin-up Seebeck coefficient (S_up) and spin-down Seebeck coefficient (S_down) at 300 K for each compound. Compute the spin-Seebeck coefficient S_spin = (σ_up·S_up − σ_down·S_down)/(σ_up+σ_down) using the conductivities from BoltzTraP. Report S_up, S_down, and S_spin (in μV/K) for all six alloys in a CSV file.
- Output file: `/app/outputs/transport_seebeck_300K.csv`
- Format: csv
- Contract: Alloy,S_up,S_down,S_spin
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/phonon_min_freq.json`
- `/app/outputs/magnetic_moments.csv`
- `/app/outputs/transport_seebeck_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed elastic constants and derived mechanical moduli for all six CoFeRGa compounds, serving as a secondary scored target for mechanical stability verification.
- schema:
  - `type`: object
  - `required`:
    - `CoFeTiGa`:
      - `c11`: float (GPa)
      - `c12`: float (GPa)
      - `c44`: float (GPa)
      - `G`: float (GPa)
      - `B`: float (GPa)
      - `Y`: float (GPa)
      - `ν`: float (unitless)
    - `CoFeVGa`: same structure
    - `CoFeCrGa`: same structure
    - `CoFeMnGa`: same structure
    - `CoFeCuGa`: same structure
    - `CoFeNbGa`: same structure
  - `items`: object
  - `required_columns`:
  - `units`:
    - `c11`: GPa
    - `c12`: GPa
    - `c44`: GPa
    - `G`: GPa
    - `B`: GPa
    - `Y`: GPa
    - `ν`: unitless

### phonon_min_freq.json
- path: `/app/outputs/phonon_min_freq.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Minimum phonon frequency for each alloy across the Brillouin zone. A positive value (within small tolerance) confirms dynamical stability, as claimed in the paper.
- schema:
  - `type`: object
  - `required`:
    - `CoFeTiGa`: float (THz)
    - `CoFeVGa`: float (THz)
    - `CoFeCrGa`: float (THz)
    - `CoFeMnGa`: float (THz)
    - `CoFeCuGa`: float (THz)
    - `CoFeNbGa`: float (THz)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: THz

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total and atomic magnetic moments, lattice constant, structure type, and electronic phase classification for all six CoFeRGa compounds, reproducing the data in Table 1.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `Alloy`, `Type`, `a`, `M_Co`, `M_Fe`, `M_R`, `M_Ga`, `M_tot`, `Phase`
  - `units`:
    - `a`: Å
    - `M_Co`: μB/atom
    - `M_Fe`: μB/atom
    - `M_R`: μB/atom
    - `M_Ga`: μB/atom
    - `M_tot`: μB/f.u.

### transport_seebeck_300K.csv
- path: `/app/outputs/transport_seebeck_300K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Spin-up, spin-down, and spin-Seebeck coefficients at 300 K for all six CoFeRGa compounds. The main verifiable claim is that CoFeCrGa exhibits the largest (most negative) spin-Seebeck coefficient and that its value meets the threshold derived from the paper's findings.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `Alloy`, `S_up`, `S_down`, `S_spin`
  - `units`:
    - `S_up`: μV/K
    - `S_down`: μV/K
    - `S_spin`: μV/K

Notes: The task requires the agent to reproduce the computational pipeline using open-source alternatives (e.g., Quantum ESPRESSO for DFT, BoltzTraP for transport). Scored outputs include elastic constants, dynamical stability, magnetic moments, and transport properties, with the spin-Seebeck coefficient of CoFeCrGa as the headline target. The checker compares the agent's results to hidden reference values with tolerances, and for the spin-Seebeck coefficient, a better (more negative) value does not lower the reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "CoFeTiGa": {
            "c11": "float (GPa)",
            "c12": "float (GPa)",
            "c44": "float (GPa)",
            "G": "float (GPa)",
            "B": "float (GPa)",
            "Y": "float (GPa)",
            "ν": "float (unitless)"
          },
          "CoFeVGa": "same structure",
          "CoFeCrGa": "same structure",
          "CoFeMnGa": "same structure",
          "CoFeCuGa": "same structure",
          "CoFeNbGa": "same structure"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "c11": "GPa",
          "c12": "GPa",
          "c44": "GPa",
          "G": "GPa",
          "B": "GPa",
          "Y": "GPa",
          "ν": "unitless"
        }
      },
      "description": "Computed elastic constants and derived mechanical moduli for all six CoFeRGa compounds, serving as a secondary scored target for mechanical stability verification."
    },
    {
      "file": "phonon_min_freq.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "CoFeTiGa": "float (THz)",
          "CoFeVGa": "float (THz)",
          "CoFeCrGa": "float (THz)",
          "CoFeMnGa": "float (THz)",
          "CoFeCuGa": "float (THz)",
          "CoFeNbGa": "float (THz)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "value": "THz"
        }
      },
      "description": "Minimum phonon frequency for each alloy across the Brillouin zone. A positive value (within small tolerance) confirms dynamical stability, as claimed in the paper."
    },
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "Alloy",
          "Type",
          "a",
          "M_Co",
          "M_Fe",
          "M_R",
          "M_Ga",
          "M_tot",
          "Phase"
        ],
        "units": {
          "a": "Å",
          "M_Co": "μB/atom",
          "M_Fe": "μB/atom",
          "M_R": "μB/atom",
          "M_Ga": "μB/atom",
          "M_tot": "μB/f.u."
        }
      },
      "description": "Total and atomic magnetic moments, lattice constant, structure type, and electronic phase classification for all six CoFeRGa compounds, reproducing the data in Table 1."
    },
    {
      "file": "transport_seebeck_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "Alloy",
          "S_up",
          "S_down",
          "S_spin"
        ],
        "units": {
          "S_up": "μV/K",
          "S_down": "μV/K",
          "S_spin": "μV/K"
        }
      },
      "description": "Spin-up, spin-down, and spin-Seebeck coefficients at 300 K for all six CoFeRGa compounds. The main verifiable claim is that CoFeCrGa exhibits the largest (most negative) spin-Seebeck coefficient and that its value meets the threshold derived from the paper's findings."
    }
  ],
  "notes": "The task requires the agent to reproduce the computational pipeline using open-source alternatives (e.g., Quantum ESPRESSO for DFT, BoltzTraP for transport). Scored outputs include elastic constants, dynamical stability, magnetic moments, and transport properties, with the spin-Seebeck coefficient of CoFeCrGa as the headline target. The checker compares the agent's results to hidden reference values with tolerances, and for the spin-Seebeck coefficient, a better (more negative) value does not lower the reward."
}
```

## How you are scored
A hidden verifier independently reads your submitted artifact files and compares each scored quantity to reference values (derived from the paper’s reported data) using tolerances that account for legitimate method- and implementation-dependent spread. For directional metrics, meeting or exceeding the reference earns full credit; credit only diminishes as the result gets worse. Crucially, for the transport step the verifier also checks that the compound with the largest spin-Seebeck coefficient is correctly identified—a relative ordering test. The total reward is the weighted sum of scores from each scored workflow stage, with the highest weight on the spin-Seebeck coefficient. Reporting a number alone is not enough; every quantity must be traceable to the required computational procedure.
