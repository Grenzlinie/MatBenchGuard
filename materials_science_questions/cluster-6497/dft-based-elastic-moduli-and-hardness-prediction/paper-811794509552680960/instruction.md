# DFT structural and mechanical properties of PdN

## Problem background
Palladium mononitride (PdN) is a hypothetical 4d transition-metal nitride that has not been synthesized experimentally to date. Its ground-state crystal structure and mechanical behavior are not yet known from experiment, so first-principles predictions play a central role in guiding future synthesis and in understanding the material's potential for hard-coating or other applications. This task aims to determine, from density-functional theory calculations, which of four candidate crystal structures (zinc-blende, rock-salt, cesium chloride, wurtzite) is the lowest-energy phase of PdN, and to fully characterize the elastic and mechanical properties of that most stable phase.

## Approach
Use density-functional theory (DFT) within the local density approximation (LDA) as implemented in the Siesta code. Start by generating norm-conserving pseudopotentials for palladium and nitrogen. Compute reference total energies for isolated Pd and N atoms in spin-polarized supercells, which are required to evaluate cohesive energies. For each of the four crystal structures (zinc-blende, rock-salt, cesium chloride, wurtzite), perform a series of total-energy calculations at several volumes around the expected equilibrium. Fit the resulting energy–volume data to the Murnaghan equation of state to extract the equilibrium lattice constants (and, for wurtzite, the internal parameters c, u, and the c/a ratio), the bulk modulus, and its pressure derivative. The cohesive energy of each phase is obtained from the equilibrium total energy and the atomic reference energies. Once the most stable phase is determined from the total-energy calculations, compute its elastic constants (C11, C12, C44) using the volume-conserving strain approach. From the elastic constants, derive the polycrystalline mechanical properties via Voigt–Reuss–Hill averaging: isotropic shear modulus, Young's modulus, Poisson's ratio, Zener anisotropy factor, Kleinman parameter, and Lamé constants. Finally, compute the longitudinal, transverse, and average sound velocities, and the Debye temperature, all for that phase.

## Reproduction target
Produce two CSV files containing the computed quantities. The first file must report, for all four PdN phases, the equilibrium structural parameters (a, and for wurtzite also c, u, c/a), bulk modulus, its pressure derivative, and the cohesive energy. The second file must report, for the most stable PdN phase (determined from the cohesive energies in step_01_structural.csv), the three elastic constants C11, C12, C44 and all derived mechanical properties: shear modulus G, Young's modulus E, Poisson's ratio ν, Zener anisotropy factor A, Kleinman parameter ζ, Lamé constants λ and μ, the three sound velocities (vl, vt, vm), and the Debye temperature θ_D. The exact column schema and units are given in the workflow steps and output contract.

## Assets

- Siesta DFT code: https://departments.icmab.es/leem/siesta/

## Workflow steps

### Step 1: Generate pseudopotentials for Pd and N
- Role: process
- Action: Using the Siesta/ATOM utility, generate norm-conserving Troullier–Martins pseudopotentials for Pd and N with appropriate atomic configurations and cut-off radii. These pseudopotentials will be used in all subsequent DFT steps.
- Evidence: `/app/outputs/pseudopotential_generation.log`

### Step 2: Compute atomic reference energies
- Role: process
- Action: Calculate the total energies of isolated Pd and N atoms using spin-polarized DFT supercells in Siesta with the generated pseudopotentials. The atomic reference energies are required for cohesive energy evaluation.
- Evidence: `/app/outputs/atomic_energies.txt`

### Step 3: Structural properties and cohesive energies for all phases
- Role: scored (load-bearing)
- Action: For each of the four crystal structures (zinc-blende ZB, rock-salt RS, cesium chloride CsCl, wurtzite WZ), perform DFT total-energy calculations at multiple volumes around the equilibrium. Fit the resulting energy–volume points to the Murnaghan equation of state to extract equilibrium lattice constants (a, and for wurtzite c, u, c/a), bulk modulus B, and pressure derivative B'. Compute cohesive energy from the equilibrium total energies and the atomic reference energies. Output all results in step_01_structural.csv.
- Output file: `/app/outputs/step_01_structural.csv`
- Format: csv
- Contract: phase (string), a (float, Å), c (float, Å, only for WZ, empty otherwise), u (float, only for WZ, empty otherwise), c_a (float, only for WZ, empty otherwise), B (float, GPa), B_prime (float), E_coh (float, eV/atom). Exactly four data rows.
- Scoring: scored by hidden verifier

### Step 4: Elastic and mechanical properties for the most stable PdN phase
- Role: scored (load-bearing)
- Action: Using the equilibrium lattice constant of the most stable PdN phase (as determined from Step 3), compute the elastic constants C11, C12, C44 via the volume-conserving strain method in DFT. Derive the polycrystalline mechanical properties via Voigt–Reuss–Hill averaging: isotropic shear modulus G, Young's modulus E, Poisson's ratio ν, Zener anisotropy factor A, Kleinman parameter ζ, Lamé constants λ and μ. Also compute sound velocities (longitudinal, transverse, average) and Debye temperature θ_D. Output all quantities in step_02_elastic.csv.
- Output file: `/app/outputs/step_02_elastic.csv`
- Format: csv
- Contract: C11 (float, GPa), C12 (float, GPa), C44 (float, GPa), G (float, GPa), E (float, GPa), nu (float, dimensionless), A (float, dimensionless), zeta (float, dimensionless), lambda (float, GPa), mu (float, GPa), vl (float, m/s), vt (float, m/s), vm (float, m/s), theta_D (float, K). Exactly one data row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural.csv`
- `/app/outputs/step_02_elastic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural.csv
- path: `/app/outputs/step_01_structural.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural parameters and cohesive energies for the four PdN phases (ZB, RS, CsCl, WZ). The checker compares these values against hidden paper-reported references within tolerances, and also verifies the relative total-energy ordering (ZB < WZ < RS < CsCl) from the submitted data.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `a`, `c`, `u`, `c_a`, `B`, `B_prime`, `E_coh`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `u`: dimensionless
    - `c_a`: dimensionless
    - `B`: GPa
    - `B_prime`: dimensionless
    - `E_coh`: eV/atom

### step_02_elastic.csv
- path: `/app/outputs/step_02_elastic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants and derived mechanical properties for the most stable PdN phase, as identified from the cohesive energies in step_01_structural.csv.
- schema:
  - `type`: table
  - `required_columns`: `C11`, `C12`, `C44`, `G`, `E`, `nu`, `A`, `zeta`, `lambda`, `mu`, `vl`, `vt`, `vm`, `theta_D`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `G`: GPa
    - `E`: GPa
    - `nu`: dimensionless
    - `A`: dimensionless
    - `zeta`: dimensionless
    - `lambda`: GPa
    - `mu`: GPa
    - `vl`: m/s
    - `vt`: m/s
    - `vm`: m/s
    - `theta_D`: K

Notes: Scoring uses reference_match (T0) with hidden paper-reported values as gold. Tolerances are generous for quantities sensitive to DFT implementation (e.g., C44, anisotropy factor) while tighter for structural parameters. The energy ordering check is part of scoring the structural CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "a",
          "c",
          "u",
          "c_a",
          "B",
          "B_prime",
          "E_coh"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "u": "dimensionless",
          "c_a": "dimensionless",
          "B": "GPa",
          "B_prime": "dimensionless",
          "E_coh": "eV/atom"
        }
      },
      "description": "Equilibrium structural parameters and cohesive energies for the four PdN phases (ZB, RS, CsCl, WZ). The checker compares these values against hidden paper-reported references within tolerances, and also verifies the relative total-energy ordering (ZB < WZ < RS < CsCl) from the submitted data."
    },
    {
      "file": "step_02_elastic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11",
          "C12",
          "C44",
          "G",
          "E",
          "nu",
          "A",
          "zeta",
          "lambda",
          "mu",
          "vl",
          "vt",
          "vm",
          "theta_D"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "G": "GPa",
          "E": "GPa",
          "nu": "dimensionless",
          "A": "dimensionless",
          "zeta": "dimensionless",
          "lambda": "GPa",
          "mu": "GPa",
          "vl": "m/s",
          "vt": "m/s",
          "vm": "m/s",
          "theta_D": "K"
        }
      },
      "description": "Elastic constants and derived mechanical properties for the most stable PdN phase, as identified from the cohesive energies in step_01_structural.csv."
    }
  ],
  "notes": "Scoring uses reference_match (T0) with hidden paper-reported values as gold. Tolerances are generous for quantities sensitive to DFT implementation (e.g., C44, anisotropy factor) while tighter for structural parameters. The energy ordering check is part of scoring the structural CSV."
}
```

## How you are scored
A hidden verifier reads your two submitted CSV files. It compares each numeric field to expected reference values derived from the first-principles study that this task is based on, using tolerances appropriate for DFT-LDA reproducibility. For quantities that represent a performance measure (e.g., errors, stability ordering), meeting or beating the reference earns full credit, while results worse than the reference receive reduced credit. In addition, the verifier checks that the relative energetic ordering of the four phases (determined from the submitted cohesive energies) is consistent with the expected ground-state sequence. You are not required to match the original publication's numbers exactly; the verifier accounts for legitimate code‑to‑code variability. The final reward is a weighted combination of the scores from the two artifacts.
