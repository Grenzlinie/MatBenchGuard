# First-principles calculation of elastic constants and magnetic moment for Hf-doped Ti3AlC2

## Problem background
MAX phases are a class of ternary layered carbides/nitrides that combine metallic and ceramic properties, making them promising for high-temperature and nuclear applications. Ti3AlC2 is a representative 312 MAX phase. Early experimental studies reported that substitutional doping with transition metals at the Ti site had minimal effect on room-temperature mechanical properties, whereas interstitial doping can substantially degrade stiffness and induce magnetism. A density functional theory (DFT) study investigated these effects systematically. The goal is to compute the structural, magnetic, and elastic properties of pristine Ti3AlC2 and of two Hf-doped variants — substitutional doping at the Ti1 site and interstitial doping at the c-ATi2 site — and to derive the key mechanical moduli and Debye temperature from the raw elastic constants.

## Approach
The calculations use spin-polarized DFT with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional and projector augmented wave (PAW) pseudopotentials, implemented in Quantum ESPRESSO (pw.x). The host is a 2×2×1 supercell (48 atoms) of Ti3AlC2 with the hexagonal P6₃/mmc crystal structure. Three systems are studied: (i) pristine Ti3AlC2, (ii) one Ti1 atom (2a site) replaced by Hf (substitutional doping), and (iii) one Hf atom placed at the c-ATi2 interstitial site (the most stable interstitial location). For each system, the cell shape and atomic positions are fully relaxed. The five independent elastic constants (C11, C33, C44, C12, C13) are obtained by applying small strains and fitting the resulting stress–strain relation. From the relaxed lattice parameters, the density is computed. The hexagonal Voigt–Reuss–Hill (VRH) averaging is then used to derive the bulk modulus, shear modulus, Young's modulus, Poisson's ratio, sound velocities, and Debye temperature. The comparison of these derived quantities between the pristine, substitutional, and interstitial cases reveals how the doping position changes mechanical and thermal behaviour.

## Reproduction target
For each of the three systems (pristine Ti3AlC2, Hf substitutional at Ti1, and Hf interstitial at c-ATi2), produce a CSV file containing the fully relaxed lattice parameters a and c (in Å), the total magnetic moment (in μB), and the five independent elastic constants C11, C33, C44, C12, C13 (in GPa). The files must be named pristine_TAC_results.csv, Hf_substitutional_TAC_results.csv, and Hf_interstitial_TAC_results.csv and placed in /app/outputs. The main reproduction objective is to compute these raw elastic and structural quantities, from which the bulk modulus, shear modulus, Young's modulus, Poisson's ratio, sound velocities, and Debye temperature are derived via the VRH formulas for a hexagonal crystal. The resulting mechanical and thermal properties should capture the distinct behaviour of substitutional versus interstitial Hf doping.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/download/
- SSSP pseudopotentials (PBE, efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Ti3AlC2 crystal structure description

## Workflow steps

### Step 1: Pristine Ti3AlC2 geometry optimization and elastic constants
- Role: scored
- Action: Construct a 2×2×1 supercell (48 atoms) of Ti3AlC2 using the experimental crystal structure (space group P6₃/mmc, atomic positions as given). Perform spin-polarized DFT full relaxation of atomic positions and cell shape. Compute the five independent elastic constants (C11, C33, C44, C12, C13) by applying small strains and fitting the stress-strain relation. Record the relaxed lattice parameters, total magnetic moment, and the elastic constants.
- Output file: `/app/outputs/pristine_TAC_results.csv`
- Format: csv
- Contract: a0_Ang, c0_Ang, mag_moment_muB, C11_GPa, C33_GPa, C44_GPa, C12_GPa, C13_GPa
- Scoring: scored by hidden verifier

### Step 2: Hf substitutional doping (Hf_Ti1) geometry optimization and elastic constants
- Role: scored
- Action: Starting from the pristine supercell, replace one Ti1 atom (2a site) with Hf. Relax the structure fully, then compute the elastic constants as in step 1. Record the relaxed geometry, magnetic moment, and elastic constants.
- Output file: `/app/outputs/Hf_substitutional_TAC_results.csv`
- Format: csv
- Contract: a0_Ang, c0_Ang, mag_moment_muB, C11_GPa, C33_GPa, C44_GPa, C12_GPa, C13_GPa
- Scoring: scored by hidden verifier

### Step 3: Hf interstitial doping (Hf_i) geometry optimization and elastic constants
- Role: scored (load-bearing)
- Action: Starting from the pristine supercell, insert one Hf atom at the c-ATi2 interstitial site (the most stable interstitial site). Relax the structure fully, compute the elastic constants, and record the relaxed geometry, magnetic moment, and elastic constants.
- Output file: `/app/outputs/Hf_interstitial_TAC_results.csv`
- Format: csv
- Contract: a0_Ang, c0_Ang, mag_moment_muB, C11_GPa, C33_GPa, C44_GPa, C12_GPa, C13_GPa
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_TAC_results.csv`
- `/app/outputs/Hf_substitutional_TAC_results.csv`
- `/app/outputs/Hf_interstitial_TAC_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_TAC_results.csv
- path: `/app/outputs/pristine_TAC_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed lattice parameters, total magnetic moment, and five elastic constants of pristine Ti3AlC2.
- schema:
  - `type`: table
  - `required_columns`: `a0_Ang`, `c0_Ang`, `mag_moment_muB`, `C11_GPa`, `C33_GPa`, `C44_GPa`, `C12_GPa`, `C13_GPa`
  - `units`:
    - `a0_Ang`: Angstrom
    - `c0_Ang`: Angstrom
    - `mag_moment_muB`: muB
    - `C11_GPa`: GPa
    - `C33_GPa`: GPa
    - `C44_GPa`: GPa
    - `C12_GPa`: GPa
    - `C13_GPa`: GPa

### Hf_substitutional_TAC_results.csv
- path: `/app/outputs/Hf_substitutional_TAC_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed lattice parameters, magnetic moment, and elastic constants for Hf substitutionally doped at the Ti1 site in Ti3AlC2.
- schema:
  - `type`: table
  - `required_columns`: `a0_Ang`, `c0_Ang`, `mag_moment_muB`, `C11_GPa`, `C33_GPa`, `C44_GPa`, `C12_GPa`, `C13_GPa`
  - `units`:
    - `a0_Ang`: Angstrom
    - `c0_Ang`: Angstrom
    - `mag_moment_muB`: muB
    - `C11_GPa`: GPa
    - `C33_GPa`: GPa
    - `C44_GPa`: GPa
    - `C12_GPa`: GPa
    - `C13_GPa`: GPa

### Hf_interstitial_TAC_results.csv
- path: `/app/outputs/Hf_interstitial_TAC_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed lattice parameters, magnetic moment, and elastic constants for Hf interstitially doped at the c-ATi2 site in Ti3AlC2.
- schema:
  - `type`: table
  - `required_columns`: `a0_Ang`, `c0_Ang`, `mag_moment_muB`, `C11_GPa`, `C33_GPa`, `C44_GPa`, `C12_GPa`, `C13_GPa`
  - `units`:
    - `a0_Ang`: Angstrom
    - `c0_Ang`: Angstrom
    - `mag_moment_muB`: muB
    - `C11_GPa`: GPa
    - `C33_GPa`: GPa
    - `C44_GPa`: GPa
    - `C12_GPa`: GPa
    - `C13_GPa`: GPa

Notes: The checker will recompute bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Debye temperature from the raw elastic constants using the hexagonal Voigt-Reuss-Hill formulas, and will compare against paper-reported values with tolerances. Trend validation will enforce that interstitial doping reduces derived moduli by more than 10% compared to pristine, while substitutional doping remains within 5%.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_TAC_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0_Ang",
          "c0_Ang",
          "mag_moment_muB",
          "C11_GPa",
          "C33_GPa",
          "C44_GPa",
          "C12_GPa",
          "C13_GPa"
        ],
        "units": {
          "a0_Ang": "Angstrom",
          "c0_Ang": "Angstrom",
          "mag_moment_muB": "muB",
          "C11_GPa": "GPa",
          "C33_GPa": "GPa",
          "C44_GPa": "GPa",
          "C12_GPa": "GPa",
          "C13_GPa": "GPa"
        }
      },
      "description": "Relaxed lattice parameters, total magnetic moment, and five elastic constants of pristine Ti3AlC2."
    },
    {
      "file": "Hf_substitutional_TAC_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0_Ang",
          "c0_Ang",
          "mag_moment_muB",
          "C11_GPa",
          "C33_GPa",
          "C44_GPa",
          "C12_GPa",
          "C13_GPa"
        ],
        "units": {
          "a0_Ang": "Angstrom",
          "c0_Ang": "Angstrom",
          "mag_moment_muB": "muB",
          "C11_GPa": "GPa",
          "C33_GPa": "GPa",
          "C44_GPa": "GPa",
          "C12_GPa": "GPa",
          "C13_GPa": "GPa"
        }
      },
      "description": "Relaxed lattice parameters, magnetic moment, and elastic constants for Hf substitutionally doped at the Ti1 site in Ti3AlC2."
    },
    {
      "file": "Hf_interstitial_TAC_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0_Ang",
          "c0_Ang",
          "mag_moment_muB",
          "C11_GPa",
          "C33_GPa",
          "C44_GPa",
          "C12_GPa",
          "C13_GPa"
        ],
        "units": {
          "a0_Ang": "Angstrom",
          "c0_Ang": "Angstrom",
          "mag_moment_muB": "muB",
          "C11_GPa": "GPa",
          "C33_GPa": "GPa",
          "C44_GPa": "GPa",
          "C12_GPa": "GPa",
          "C13_GPa": "GPa"
        }
      },
      "description": "Relaxed lattice parameters, magnetic moment, and elastic constants for Hf interstitially doped at the c-ATi2 site in Ti3AlC2."
    }
  ],
  "notes": "The checker will recompute bulk modulus, shear modulus, Young's modulus, Poisson's ratio, and Debye temperature from the raw elastic constants using the hexagonal Voigt-Reuss-Hill formulas, and will compare against paper-reported values with tolerances. Trend validation will enforce that interstitial doping reduces derived moduli by more than 10% compared to pristine, while substitutional doping remains within 5%."
}
```

## How you are scored
A hidden verifier reads each output CSV, recomputes the density from the reported lattice parameters and atomic masses, and derives the bulk modulus, shear modulus, Young's modulus, Poisson's ratio, sound velocities, and Debye temperature using the hexagonal VRH equations. These derived values are compared against hidden reference data for each phase. Additional checks evaluate the relative trends between the three systems, such as the change in mechanical moduli when going from pristine to substitutionally doped or interstitially doped Ti3AlC2. The final reward is a weighted combination across the three scored artifacts, giving more weight to the fidelity of the raw elastic constants and the derived moduli for the interstitially doped case, which is the signature result. Reporting numbers is not sufficient; the generated artifacts must reflect a properly executed DFT workflow.
