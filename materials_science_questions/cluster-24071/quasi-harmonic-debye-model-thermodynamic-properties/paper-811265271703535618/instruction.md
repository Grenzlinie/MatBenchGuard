# First-principles elastic and thermal properties of vanadium silicide compounds via DFT and quasi-harmonic Debye model

## Problem background
Vanadium silicide compounds V3Si, VSi2, V5Si3, and V6Si5 are promising candidates for high-temperature structural applications. Reliable knowledge of their mechanical (elastic) and thermal behaviour is critical for materials selection and design. First‑principles density functional theory (DFT) combined with the quasi‑harmonic Debye model can predict these properties accurately, yielding data that is otherwise challenging to obtain experimentally.

## Approach
Use plane‑wave DFT with the GGA‑PBE exchange‑correlation functional and ultrasoft pseudopotentials to model electron‑ion interactions. First, optimise the crystal structures of the four compounds and compute the total energies of elemental vanadium and silicon in their ground states to obtain formation enthalpies. Next, compute the single‑crystal elastic constants via the stress‑strain method (finite distortions) and derive polycrystalline elastic moduli (bulk, shear, Young’s) and sound velocities using the Voigt‑Reuss‑Hill averaging scheme and Navier’s equations. Finally, generate energy‑versus‑volume data around the equilibrium volumes, fit an equation of state, and apply the quasi‑harmonic Debye model (e.g. the Gibbs2 code) to evaluate thermodynamic properties at the reference condition T = 300 K and P = 0 GPa.

## Reproduction target
For each compound, compute and report:
- Equilibrium lattice parameters a, b, c (Å) and formation enthalpy per atom Ef (kJ/mol).
- Full set of symmetry‑relevant single‑crystal elastic constants Cij (GPa) and, from them, the polycrystalline bulk modulus B, shear modulus G, Young’s modulus E, Poisson’s ratio σ, and the compressional, shear, and average sound velocities Vp, Vs, Vm.
- Thermodynamic quantities at T = 300 K and P = 0 GPa: internal energy U, constant‑volume and constant‑pressure heat capacities Cv and Cp, Helmholtz free energy A, entropy S, Debye temperature Θ, Grüneisen parameter γ, and thermal expansion coefficient α.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Gibbs2 code: https://github.com/branaa/gibbs2
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Initial crystal structures of V-Si compounds and elemental V, Si

## Workflow steps

### Step 1: Structural optimization and formation enthalpy
- Role: scored (load-bearing)
- Action: Optimize the crystal structures of V3Si, VSi2, V5Si3, V6Si5, and compute the total energies of elemental V and Si in their ground states using DFT with GGA-PBE functional and ultrasoft pseudopotentials. Determine converged plane-wave cutoff and k-point grids. Calculate the formation enthalpy per atom for each compound. Report the equilibrium lattice parameters (a, b, c in Å) and formation enthalpy (Ef, kJ/mol).
- Output file: `/app/outputs/structural_properties.csv`
- Format: csv
- Contract: CSV with columns: compound, a(Å), b(Å), c(Å), Ef(kJ/mol). One row per compound. For V3Si and V5Si3, b is empty. Units must match column headers.
- Scoring: scored by hidden verifier

### Step 2: Elastic constants and polycrystalline moduli
- Role: scored (load-bearing)
- Action: Compute the single-crystal elastic constants Cij for V3Si, VSi2, V5Si3, V6Si5 using DFT with the stress-strain method (finite distortions). From the elastic constants, calculate polycrystalline bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio σ, and sound velocities Vp, Vs, Vm using the Voigt-Reuss-Hill approximation and Navier's equations. Report all elastic constants and derived properties.
- Output file: `/app/outputs/elastic_properties.csv`
- Format: csv
- Contract: CSV with columns: compound, C11, C12, C13, C22, C23, C33, C44, C55, C66 (all GPa), B(GPa), G(GPa), E(GPa), sigma, Vp(m/s), Vs(m/s), Vm(m/s). Symmetry-independent constants not applicable to a compound are left empty.
- Scoring: scored by hidden verifier

### Step 3: Energy-volume curve and quasi-harmonic Debye thermodynamics
- Role: scored (load-bearing)
- Action: Perform DFT total-energy calculations for each compound at several volumes around the equilibrium volume to obtain E-V data points. Fit an equation of state. Use the Gibbs2 code (or equivalent quasi-harmonic Debye model) to compute thermodynamic properties at temperature T=300 K and pressure P=0 GPa: internal energy U, heat capacities Cv and Cp, Helmholtz free energy A, entropy S, Debye temperature Θ, Grüneisen parameter γ, and thermal expansion coefficient α.
- Output file: `/app/outputs/thermal_properties.csv`
- Format: csv
- Contract: CSV with columns: compound, U(kJ/mol), Cv(J/mol*K), Cp(J/mol*K), A(kJ/mol), S(J/mol*K), Theta(K), gamma, alpha(10^-5/K). One row per compound, units must match.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_properties.csv`
- `/app/outputs/elastic_properties.csv`
- `/app/outputs/thermal_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_properties.csv
- path: `/app/outputs/structural_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice parameters and formation enthalpy per atom. The b column may be empty for cubic/tetragonal systems.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `a(Å)`, `b(Å)`, `c(Å)`, `Ef(kJ/mol)`
  - `units`:
    - `a(Å)`: angstrom
    - `b(Å)`: angstrom
    - `c(Å)`: angstrom
    - `Ef(kJ/mol)`: kJ/mol

### elastic_properties.csv
- path: `/app/outputs/elastic_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic constants and polycrystalline elastic moduli and sound velocities. Missing symmetry-related elastic constants are left empty.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `C11`, `C12`, `C13`, `C22`, `C23`, `C33`, `C44`, `C55`, `C66`, `B(GPa)`, `G(GPa)`, `E(GPa)`, `sigma`, `Vp(m/s)`, `Vs(m/s)`, `Vm(m/s)`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C13`: GPa
    - `C22`: GPa
    - `C23`: GPa
    - `C33`: GPa
    - `C44`: GPa
    - `C55`: GPa
    - `C66`: GPa
    - `B(GPa)`: GPa
    - `G(GPa)`: GPa
    - `E(GPa)`: GPa
    - `sigma`: dimensionless
    - `Vp(m/s)`: m/s
    - `Vs(m/s)`: m/s
    - `Vm(m/s)`: m/s

### thermal_properties.csv
- path: `/app/outputs/thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic properties computed at T=300 K and P=0 GPa from the quasi-harmonic Debye model.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `U(kJ/mol)`, `Cv(J/mol*K)`, `Cp(J/mol*K)`, `A(kJ/mol)`, `S(J/mol*K)`, `Theta(K)`, `gamma`, `alpha(10^-5/K)`
  - `units`:
    - `U(kJ/mol)`: kJ/mol
    - `Cv(J/mol*K)`: J/(mol K)
    - `Cp(J/mol*K)`: J/(mol K)
    - `A(kJ/mol)`: kJ/mol
    - `S(J/mol*K)`: J/(mol K)
    - `Theta(K)`: K
    - `gamma`: dimensionless
    - `alpha(10^-5/K)`: 10^-5 K^-1

Notes: All output files must be placed in /app/outputs. Tolerances and gold values are defined in the hidden checker; the agent only sees the schema and format requirements.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "a(Å)",
          "b(Å)",
          "c(Å)",
          "Ef(kJ/mol)"
        ],
        "units": {
          "a(Å)": "angstrom",
          "b(Å)": "angstrom",
          "c(Å)": "angstrom",
          "Ef(kJ/mol)": "kJ/mol"
        }
      },
      "description": "Equilibrium lattice parameters and formation enthalpy per atom. The b column may be empty for cubic/tetragonal systems."
    },
    {
      "file": "elastic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "C11",
          "C12",
          "C13",
          "C22",
          "C23",
          "C33",
          "C44",
          "C55",
          "C66",
          "B(GPa)",
          "G(GPa)",
          "E(GPa)",
          "sigma",
          "Vp(m/s)",
          "Vs(m/s)",
          "Vm(m/s)"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C13": "GPa",
          "C22": "GPa",
          "C23": "GPa",
          "C33": "GPa",
          "C44": "GPa",
          "C55": "GPa",
          "C66": "GPa",
          "B(GPa)": "GPa",
          "G(GPa)": "GPa",
          "E(GPa)": "GPa",
          "sigma": "dimensionless",
          "Vp(m/s)": "m/s",
          "Vs(m/s)": "m/s",
          "Vm(m/s)": "m/s"
        }
      },
      "description": "Single-crystal elastic constants and polycrystalline elastic moduli and sound velocities. Missing symmetry-related elastic constants are left empty."
    },
    {
      "file": "thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "U(kJ/mol)",
          "Cv(J/mol*K)",
          "Cp(J/mol*K)",
          "A(kJ/mol)",
          "S(J/mol*K)",
          "Theta(K)",
          "gamma",
          "alpha(10^-5/K)"
        ],
        "units": {
          "U(kJ/mol)": "kJ/mol",
          "Cv(J/mol*K)": "J/(mol K)",
          "Cp(J/mol*K)": "J/(mol K)",
          "A(kJ/mol)": "kJ/mol",
          "S(J/mol*K)": "J/(mol K)",
          "Theta(K)": "K",
          "gamma": "dimensionless",
          "alpha(10^-5/K)": "10^-5 K^-1"
        }
      },
      "description": "Thermodynamic properties computed at T=300 K and P=0 GPa from the quasi-harmonic Debye model."
    }
  ],
  "notes": "All output files must be placed in /app/outputs. Tolerances and gold values are defined in the hidden checker; the agent only sees the schema and format requirements."
}
```

## How you are scored
A hidden verifier reads each output CSV file and compares your reported numeric values to the expected reference values for these compounds (with per‑quantity tolerances). Each workflow stage carries a share of the total reward. Meeting the required output format and providing values within tolerance earns full credit for that stage; larger deviations receive partial credit. The verifier does not re‑run your DFT calculations; it only evaluates the final numbers you submit, so accurate execution of every step is essential.
