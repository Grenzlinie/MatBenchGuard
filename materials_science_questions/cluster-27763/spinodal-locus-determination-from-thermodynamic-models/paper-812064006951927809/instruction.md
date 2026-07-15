# Mechanical Stability and Electron Density of Al Lattices from DFT Calculations

## Problem background
In the “anions in metallic matrices” (AMM) model, the crystal structures of inorganic compounds containing metallic elements are viewed as a host metallic matrix with nonmetallic atoms occupying regions of charge accumulation. This task investigates the Al host lattices that appear, often slightly distorted, as sublattices in AlX₃ (X = F, Cl, OH) crystals. Understanding the mechanical stability, equilibrium and spinodal equation-of-state parameters, elastic constants, and electron density topology of these Al structures is essential for quantifying the role of the metallic skeleton and the nonmetallic guest atoms. The objective is to compute, from first-principles density‑functional theory, the zero-pressure equilibrium volumes, bulk moduli, pressure derivatives, spinodal volumes and pressures for a set of seven Al lattices (fcc, bcc, hcp, simple cubic, spinel, eclipsed graphitic, and monoclinic), the volume‑dependent elastic constants for two representative lattices, and the bond, ring and cage critical points of the electron density for selected structures at their equilibrium geometries.

## Approach
The computational strategy combines plane‑wave density‑functional theory (DFT) with the generalized gradient approximation (GGA) for total energy calculations, equation‑of‑state fitting, strain‑energy evaluation of elastic constants, and topological analysis of the electron density within Bader’s atoms‑in‑molecules (AIM) formalism. The Al crystal structures are built from the symmetry and atomic positions described in the literature (space groups and fractional coordinates are public knowledge). For each lattice, total energies are computed for a range of unit‑cell volumes while fully relaxing internal degrees of freedom. The resulting energy‑volume curves are fitted to an appropriate equation of state (e.g., Vinet) to extract equilibrium and spinodal parameters. For the simple cubic and hexagonal eclipsed‑graphitic structures, small homogeneous strains are applied at a series of volumes, and the elastic constants are derived from the second derivatives of the strain energy. Mechanical stability is assessed via the pressure‑adjusted Born criteria. For the topological analysis, the ground‑state electron density is generated at the equilibrium zero‑pressure geometries using an all‑electron or PAW‑reconstructed approach, and bond, ring and cage critical points are located. The final deliverables are four structured CSV files that contain the computed parameters, elastic constants, and critical point properties.

## Reproduction target
Produce the following four scored artifacts under /app/outputs:
1. **eos_parameters.csv** – for each of the seven Al lattices (fcc, bcc, hcp, sc, spinel, gra-e1, gra‑e), report the zero‑pressure equilibrium volume V₀ (Å³), bulk modulus B₀ (GPa), pressure derivative B₀′, spinodal volume V_sp (Å³), and spinodal pressure p_sp (GPa).
2. **elastic_constants_sc.csv** – for the simple cubic Al lattice, as a function of volume, provide volume (Å³), pressure (GPa), C₁₁, C₁₂, C₄₄ (GPa), the derived bulk modulus B (GPa), and the absolute value of C₁₁ − C₁₂ (GPa).
3. **elastic_constants_grae1.csv** – for the hexagonal gra‑e1 Al lattice, as a function of volume, provide volume (Å³), pressure (GPa), C₁₁, C₁₂, C₃₃, C₄₄, C₁₃ (GPa).
4. **critical_points.csv** – for the five lattices fcc, sc, spinel, gra‑e1 and gra‑a at their equilibrium zero‑pressure volumes, list every bond (BP), ring (RP) and cage (CP) critical point with its lattice label, type, fractional coordinates (x,y,z), electron density ρ (e/bohr³), and Laplacian ∇²ρ (e/bohr⁵) (leave Laplacian as NaN for non‑bond points).

## Assets

- Al lattice crystal structures (fcc, bcc, hcp, sc, spinel, gra-e1, gra-e, gra-a)
- Plane-wave DFT code (e.g., Quantum ESPRESSO, VASP, ABINIT): https://www.quantum-espresso.org
- Equation-of-state fitting tool (GIBBS or self-developed script): https://github.com/
- AIM topological analysis code (e.g., Henkelman's Bader, AIMAll, CRITIC): https://theory.cm.utexas.edu/henkelman/code/bader/
- All-electron or PAW-reconstructed DFT wavefunction generator: https://www.quantum-espresso.org

## Workflow steps

### Step 1: DFT total energy calculations for Al lattices
- Role: process
- Action: Perform DFT total energy calculations for fcc, bcc, hcp, sc, spinel, hexagonal eclipsed graphitic P6/mmm (gra-e1), and monoclinic P2_1/n (gra-e) Al lattices. For each lattice, compute total energies at a set of volumes spanning roughly 0.8 to 1.5 times the expected equilibrium volume, fully relaxing all structural degrees of freedom. Use a plane-wave DFT code with GGA functional.
- Evidence: `/app/outputs/ev_curves.csv`

### Step 2: EOS fitting and extraction of equilibrium/spinodal parameters
- Role: scored
- Action: Fit each lattice’s energy-volume curve to a Vinet (or Birch) equation of state. Extract the zero-pressure equilibrium volume V0, bulk modulus B0, its pressure derivative B0', and determine the spinodal condition where B(V)=0 to obtain Vsp and psp. Write all parameters to eos_parameters.csv.
- Output file: `/app/outputs/eos_parameters.csv`
- Format: csv
- Contract: Columns: lattice (string), V0_ang3 (float), B0_GPa (float), B0_prime (float), Vsp_ang3 (float), psp_GPa (float). One row per lattice.
- Scoring: scored by hidden verifier

### Step 3: Strain energy calculations for elastic constants
- Role: process
- Action: For the simple cubic (sc) and hexagonal gra-e1 Al lattices, perform DFT total energy calculations at multiple volumes under a set of small homogeneous strain deformations. Apply the strain scheme to obtain energy vs strain parameter gamma from -0.04 to +0.04 in steps of 0.01. Store the raw energy-strain data.
- Evidence: `/app/outputs/strain_energy_data.zip`

### Step 4: Elastic constant determination and stability assessment (sc)
- Role: scored (load-bearing)
- Action: Process the strain energy data to obtain the second derivative of energy with respect to gamma for each strain. Solve for the independent elastic constants C11, C12, C44 as functions of volume. Compute pressure-adjusted constants tilde Cij. For the sc lattice, output volume, pressure, C11, C12, C44, and derived B and C11_minus_C12_abs. Write to elastic_constants_sc.csv.
- Output file: `/app/outputs/elastic_constants_sc.csv`
- Format: csv
- Contract: Columns: volume_A3 (float), pressure_GPa (float), C11_GPa (float), C12_GPa (float), C44_GPa (float), B_GPa (float), C11_minus_C12_abs_GPa (float). One row per volume point.
- Scoring: scored by hidden verifier

### Step 5: Elastic constant determination for gra-e1 lattice
- Role: scored (load-bearing)
- Action: Same as s4 but for the hexagonal gra-e1 structure. Output volume, pressure, C11, C12, C33, C44, C13. Write to elastic_constants_grae1.csv.
- Output file: `/app/outputs/elastic_constants_grae1.csv`
- Format: csv
- Contract: Columns: volume_A3 (float), pressure_GPa (float), C11_GPa (float), C12_GPa (float), C33_GPa (float), C44_GPa (float), C13_GPa (float). One row per volume point.
- Scoring: scored by hidden verifier

### Step 6: All-electron wavefunction generation at equilibrium volumes
- Role: process
- Action: For the fcc, sc, spinel, gra-e1, and alternated graphitic (gra-a, R-3) Al lattices at their zero-pressure equilibrium geometries (obtained from the EOS), perform all-electron DFT calculations or pseudopotential+PAW reconstruction to generate the ground-state electron density suitable for AIM analysis.
- Evidence: none

### Step 7: AIM topological analysis and critical point extraction
- Role: scored
- Action: Perform AIM topological analysis on the electron densities of the five lattices (fcc, sc, spinel, gra-e1, gra-a). Locate all bond (BCP), ring (RCP), and cage (CCP) critical points. For each BCP, record its crystallographic coordinates, the electron density rho (e/bohr^3) and the Laplacian (e/bohr^5). For RCP and CCP, record coordinates and rho. Compile the data into critical_points.csv.
- Output file: `/app/outputs/critical_points.csv`
- Format: csv
- Contract: Columns: lattice (string), cp_type (string, one of BP,RP,CP), x (fractional coordinate, float), y (float), z (float), rho_e_per_bohr3 (float), laplacian_e_per_bohr5 (float, NaN for non-BP). One row per critical point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_parameters.csv`
- `/app/outputs/elastic_constants_sc.csv`
- `/app/outputs/elastic_constants_grae1.csv`
- `/app/outputs/critical_points.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_parameters.csv
- path: `/app/outputs/eos_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equation-of-state and spinodal parameters for each Al lattice.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `V0_ang3`, `B0_GPa`, `B0_prime`, `Vsp_ang3`, `psp_GPa`
  - `units`:
    - `V0_ang3`: Å³
    - `B0_GPa`: GPa
    - `B0_prime`: dimensionless
    - `Vsp_ang3`: Å³
    - `psp_GPa`: GPa

### elastic_constants_sc.csv
- path: `/app/outputs/elastic_constants_sc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants and stability indicators for simple cubic Al as a function of volume.
- schema:
  - `type`: table
  - `required_columns`: `volume_A3`, `pressure_GPa`, `C11_GPa`, `C12_GPa`, `C44_GPa`, `B_GPa`, `C11_minus_C12_abs_GPa`
  - `units`:
    - `volume_A3`: Å³
    - `pressure_GPa`: GPa
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa
    - `B_GPa`: GPa
    - `C11_minus_C12_abs_GPa`: GPa

### elastic_constants_grae1.csv
- path: `/app/outputs/elastic_constants_grae1.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants for hexagonal gra-e1 Al as a function of volume.
- schema:
  - `type`: table
  - `required_columns`: `volume_A3`, `pressure_GPa`, `C11_GPa`, `C12_GPa`, `C33_GPa`, `C44_GPa`, `C13_GPa`
  - `units`:
    - `volume_A3`: Å³
    - `pressure_GPa`: GPa
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C33_GPa`: GPa
    - `C44_GPa`: GPa
    - `C13_GPa`: GPa

### critical_points.csv
- path: `/app/outputs/critical_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical point positions and properties for selected Al lattices at equilibrium.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `cp_type`, `x`, `y`, `z`, `rho_e_per_bohr3`, `laplacian_e_per_bohr5`
  - `units`:
    - `rho_e_per_bohr3`: e/bohr³
    - `laplacian_e_per_bohr5`: e/bohr⁵

Notes: All artifacts are produced by the solver and scored against hidden reference values from the paper. Elastic constants are load-bearing to ensure the strain-energy process steps are actually executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "V0_ang3",
          "B0_GPa",
          "B0_prime",
          "Vsp_ang3",
          "psp_GPa"
        ],
        "units": {
          "V0_ang3": "Å³",
          "B0_GPa": "GPa",
          "B0_prime": "dimensionless",
          "Vsp_ang3": "Å³",
          "psp_GPa": "GPa"
        }
      },
      "description": "Equation-of-state and spinodal parameters for each Al lattice."
    },
    {
      "file": "elastic_constants_sc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_A3",
          "pressure_GPa",
          "C11_GPa",
          "C12_GPa",
          "C44_GPa",
          "B_GPa",
          "C11_minus_C12_abs_GPa"
        ],
        "units": {
          "volume_A3": "Å³",
          "pressure_GPa": "GPa",
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa",
          "B_GPa": "GPa",
          "C11_minus_C12_abs_GPa": "GPa"
        }
      },
      "description": "Elastic constants and stability indicators for simple cubic Al as a function of volume."
    },
    {
      "file": "elastic_constants_grae1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "volume_A3",
          "pressure_GPa",
          "C11_GPa",
          "C12_GPa",
          "C33_GPa",
          "C44_GPa",
          "C13_GPa"
        ],
        "units": {
          "volume_A3": "Å³",
          "pressure_GPa": "GPa",
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C33_GPa": "GPa",
          "C44_GPa": "GPa",
          "C13_GPa": "GPa"
        }
      },
      "description": "Elastic constants for hexagonal gra-e1 Al as a function of volume."
    },
    {
      "file": "critical_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "cp_type",
          "x",
          "y",
          "z",
          "rho_e_per_bohr3",
          "laplacian_e_per_bohr5"
        ],
        "units": {
          "rho_e_per_bohr3": "e/bohr³",
          "laplacian_e_per_bohr5": "e/bohr⁵"
        }
      },
      "description": "Critical point positions and properties for selected Al lattices at equilibrium."
    }
  ],
  "notes": "All artifacts are produced by the solver and scored against hidden reference values from the paper. Elastic constants are load-bearing to ensure the strain-energy process steps are actually executed."
}
```

## How you are scored
A hidden verifier reads each of the scored output files and compares your reported values to independently established reference data for these Al lattices. The comparison uses appropriate tolerances that account for the expected spread between different DFT codes and implementations. For the equation‑of‑state parameters, the verifier checks the numerical values; for the elastic constants, it evaluates both the individual Cᵢⱼ values and the satisfaction of the mechanical stability criteria at the relevant volumes; for the critical points, it compares positions, electron densities and Laplacians. The total reward is a weighted sum over all scored stages, with the largest weight on the headline EOS and elastic‑constant results. Simply producing the required files is not sufficient — your computed quantities must be physically reasonable and consistent with the underlying strain‑energy data. The verifier does not access your intermediate calculation files except those explicitly listed as evidence; it scores only the final declared artifacts.
