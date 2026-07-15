# Reproduce structural, electronic, magnetic anisotropy, and valley polarization properties of Janus 2H-GdIBr monolayer via DFT+SOC calculations

## Problem background
Two-dimensional intrinsic ferromagnetic semiconductors with robust magnetic anisotropy and strong valley polarization are sought for next-generation spintronic and valleytronic devices. Introducing rare-earth elements with $4f$ electrons offers a promising route to large magnetic moments and high magnetic ordering temperatures. The Janus 2H-GdIBr monolayer is a candidate material with a trigonal prismatic coordination and broken mirror symmetry. It is of interest to establish from first principles whether this monolayer is dynamically and thermally stable, what its electronic and magnetic ground-state properties are, how its magnetic anisotropy and spontaneous valley polarization evolve under biaxial strain, and whether strain and charge doping can effectively tune its Curie temperature and anomalous Hall response.

## Approach
The reproduction uses density functional theory (DFT) with the PBE exchange-correlation functional, a Hubbard $U$ correction on Gd $4f$ states, and spin-orbit coupling (SOC). Calculations are performed with a plane-wave basis and an open-source DFT code. The structural model is built from a known 2H-GdI$_2$ prototype by replacing one halogen layer with Br. The workflow proceeds through structural relaxation, exfoliation energy and stability assessments (phonon dispersion and ab initio molecular dynamics), electronic structure without SOC, magnetic anisotropy energy (MAE) versus biaxial strain, spontaneous valley polarization versus strain, extraction of Heisenberg exchange parameters from ferromagnetic and antiferromagnetic supercell energies, Monte Carlo simulation for Curie temperature and its modulation, construction of maximally localized Wannier functions from the SOC band structure, and computation of Berry curvature and intrinsic anomalous Hall conductivity using Wannier interpolation. Post-processing tools for phonons, Wannier functions, topological analysis, and Monte Carlo simulations are employed.

## Reproduction target
Compute the following quantities for the Janus 2H-GdIBr monolayer and write them to the specified output files:

1. Relaxed in-plane lattice constants, exfoliation energy, and stability checks (true/false for AIMD thermal stability and absence of imaginary phonon modes).
2. Electronic indirect band gap and total magnetic moment per formula unit (without SOC).
3. Magnetic anisotropy energy (in µeV/f.u.) for biaxial strains from -8% to +8% in 2% steps.
4. Spontaneous valley polarization (energy difference between K and K′ valence band edges, in meV) for the same strain range.
5. Curie temperature (in K) at equilibrium strain, obtained from a Monte Carlo simulation of the Heisenberg model with exchange parameters fitted from DFT.
6. Curie temperature (in K) under selected strain and doping conditions: (−8%, 0), (0%, 0), (+8%, 0), (0%, −0.3 e/f.u.), (0%, +0.3 e/f.u.).
7. Berry curvature (in atomic units) and anomalous Hall conductivity (in S/cm) at the K and K′ points, obtained from the Wannier Hamiltonian.

All outputs must follow the specified file formats and schemas exactly.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- Wannier90: https://wannier.org/
- WannierTools: https://www.wanniertools.com/
- MCSOLVER: https://github.com/liuliu/MCSOLVER
- Standard pseudopotentials (Gd, Br, I): SSSP library for QE

## Workflow steps

### Step 1: Construct initial Janus 2H-GdIBr structure
- Role: process
- Action: Build the three-layer hexagonal unit cell of Janus 2H-GdIBr from the 2H-GdI2 prototype, replacing the top I layer with Br. Output the starting atomic positions and cell vectors in a format suitable for DFT input.
- Evidence: `/app/outputs/initial_structure.txt`

### Step 2: DFT structural relaxation
- Role: process
- Action: Perform spin-polarized DFT relaxation using PBE+U with SOC, vacuum spacing adequate for monolayer, and converged k-mesh and cutoff. The relaxation target convergence criteria for energy and forces are typical for high-accuracy structural optimization.
- Evidence: `/app/outputs/relaxed_structure.txt`

### Step 3: Stability assessment and exfoliation energy
- Role: scored (load-bearing)
- Action: Using the relaxed geometry, compute: (i) cleavage/exfoliation energy by calculating total energy of slab models with varying interlayer separation until convergence; (ii) ab-initio molecular dynamics (AIMD) in NVT ensemble at 300 K for 10 ps to check thermal stability; (iii) phonon dispersion via DFPT on a supercell and verify absence of imaginary frequencies. Collect the lattice constants, exfoliation energy at convergence, and stability booleans.
- Output file: `/app/outputs/structure_and_stability.csv`
- Format: csv
- Contract: property (string), value (float or bool), unit (string)
- Scoring: scored by hidden verifier

### Step 4: Electronic properties without SOC
- Role: scored
- Action: Perform spin-polarized DFT calculation (without SOC) on the relaxed structure using a denser k-mesh. Extract the indirect band gap and total magnetic moment.
- Output file: `/app/outputs/electronic_properties.csv`
- Format: csv
- Contract: property (string), value (float), unit (string)
- Scoring: scored by hidden verifier

### Step 5: Magnetic anisotropy energy vs strain
- Role: scored (load-bearing)
- Action: For biaxial strains from -8% to +8% in 2% increments, compute total energy with SOC for magnetization along [100] and [001]. Calculate MAE = E[001] - E[100] (μeV/f.u.) and report the results.
- Output file: `/app/outputs/mae_vs_strain.csv`
- Format: csv
- Contract: strain (float), MAE (float)
- Scoring: scored by hidden verifier

### Step 6: Valley polarization vs strain
- Role: scored (load-bearing)
- Action: For the same strain range, compute the band structure with SOC using a dense k-mesh. Identify the VBM at K and K' valleys and record the energy difference (valley polarization) in meV.
- Output file: `/app/outputs/valley_polarization_vs_strain.csv`
- Format: csv
- Contract: strain (float), valley_polarization (float)
- Scoring: scored by hidden verifier

### Step 7: Extract magnetic exchange parameters
- Role: process
- Action: From DFT total energies of FM and AFM configurations in a 2×2×1 supercell with SOC, calculate the nearest-neighbor exchange coupling J and single-ion anisotropy D using the energy mapping of the Heisenberg model.
- Evidence: `/app/outputs/exchange_params.txt`

### Step 8: Curie temperature at equilibrium
- Role: scored (load-bearing)
- Action: Using the extracted J and D, run a Monte Carlo simulation (Wolff algorithm, Heisenberg model) and determine the Curie temperature from the specific heat peak. Report Tc in K.
- Output file: `/app/outputs/curie_temperature.txt`
- Format: txt
- Contract: text
- Scoring: scored by hidden verifier

### Step 9: Curie temperature modulation by strain and doping
- Role: scored (load-bearing)
- Action: Repeat the exchange parameter extraction and Monte Carlo simulation for representative strains (-8%, 0%, +8%) and carrier doping levels (-0.3, 0.0, +0.3 e/f.u.). Report the resulting Tc (K) for each condition.
- Output file: `/app/outputs/curie_temperature_modulation.csv`
- Format: csv
- Contract: condition (string), strain (float), doping (float), Tc (float)
- Scoring: scored by hidden verifier

### Step 10: Construct Wannier functions
- Role: process
- Action: From the DFT+SOC band structure of the equilibrium monolayer, use Wannier90 to build maximally localized Wannier functions for the relevant bands. Output the Wannier Hamiltonian.
- Evidence: `/app/outputs/wannier_hr.dat`

### Step 11: Berry curvature and anomalous Hall conductivity
- Role: scored (load-bearing)
- Action: Using WannierTools with the Wannier Hamiltonian, compute the Berry curvature over the Brillouin zone and the intrinsic anomalous Hall conductivity σ_xy. Report values at the K and K' points.
- Output file: `/app/outputs/berry_and_ahc.csv`
- Format: csv
- Contract: kpoint (string), berry_curvature (float), anomalous_hall_conductivity (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structure_and_stability.csv`
- `/app/outputs/electronic_properties.csv`
- `/app/outputs/mae_vs_strain.csv`
- `/app/outputs/valley_polarization_vs_strain.csv`
- `/app/outputs/curie_temperature.txt`
- `/app/outputs/curie_temperature_modulation.csv`
- `/app/outputs/berry_and_ahc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structure_and_stability.csv
- path: `/app/outputs/structure_and_stability.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Structural stability and exfoliation energy of the Janus 2H-GdIBr monolayer.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`, `unit`
  - `units`:
    - `value`: as specified in unit column

### electronic_properties.csv
- path: `/app/outputs/electronic_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Electronic band gap and magnetic moment without SOC.
- schema:
  - `type`: table
  - `required_columns`: `property`, `value`, `unit`
  - `units`:
    - `value`: as specified in unit column

### mae_vs_strain.csv
- path: `/app/outputs/mae_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Magnetic anisotropy energy as a function of biaxial strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `MAE`
  - `units`:
    - `strain`: %
    - `MAE`: μeV/f.u.

### valley_polarization_vs_strain.csv
- path: `/app/outputs/valley_polarization_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Valley polarization (energy difference between K and K' valence band edges) as a function of strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `valley_polarization`
  - `units`:
    - `strain`: %
    - `valley_polarization`: meV

### curie_temperature.txt
- path: `/app/outputs/curie_temperature.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium Curie temperature from Monte Carlo simulation.
- schema:
  - `type`: text

### curie_temperature_modulation.csv
- path: `/app/outputs/curie_temperature_modulation.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Curie temperature under strain and carrier doping.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `strain`, `doping`, `Tc`
  - `units`:
    - `strain`: %
    - `doping`: e/f.u.
    - `Tc`: K

### berry_and_ahc.csv
- path: `/app/outputs/berry_and_ahc.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Berry curvature and anomalous Hall conductivity at high-symmetry K and K' points.
- schema:
  - `type`: table
  - `required_columns`: `kpoint`, `berry_curvature`, `anomalous_hall_conductivity`
  - `units`:
    - `berry_curvature`: atomic units
    - `anomalous_hall_conductivity`: S/cm

Notes: All scored artifacts are compared against hidden reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structure_and_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value",
          "unit"
        ],
        "units": {
          "value": "as specified in unit column"
        }
      },
      "description": "Structural stability and exfoliation energy of the Janus 2H-GdIBr monolayer."
    },
    {
      "file": "electronic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "property",
          "value",
          "unit"
        ],
        "units": {
          "value": "as specified in unit column"
        }
      },
      "description": "Electronic band gap and magnetic moment without SOC."
    },
    {
      "file": "mae_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "MAE"
        ],
        "units": {
          "strain": "%",
          "MAE": "μeV/f.u."
        }
      },
      "description": "Magnetic anisotropy energy as a function of biaxial strain."
    },
    {
      "file": "valley_polarization_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "valley_polarization"
        ],
        "units": {
          "strain": "%",
          "valley_polarization": "meV"
        }
      },
      "description": "Valley polarization (energy difference between K and K' valence band edges) as a function of strain."
    },
    {
      "file": "curie_temperature.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Equilibrium Curie temperature from Monte Carlo simulation."
    },
    {
      "file": "curie_temperature_modulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "strain",
          "doping",
          "Tc"
        ],
        "units": {
          "strain": "%",
          "doping": "e/f.u.",
          "Tc": "K"
        }
      },
      "description": "Curie temperature under strain and carrier doping."
    },
    {
      "file": "berry_and_ahc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kpoint",
          "berry_curvature",
          "anomalous_hall_conductivity"
        ],
        "units": {
          "berry_curvature": "atomic units",
          "anomalous_hall_conductivity": "S/cm"
        }
      },
      "description": "Berry curvature and anomalous Hall conductivity at high-symmetry K and K' points."
    }
  ],
  "notes": "All scored artifacts are compared against hidden reference values with appropriate tolerances."
}
```

## How you are scored
An automated hidden verifier will read each output file you produce and compare the reported quantities against a hidden reference. Scoring is weighted across all scored artifacts. For fixed numerical quantities, the verifier checks consistency within pre-defined tolerances; for strain-dependent quantities, it also checks that the overall trend (monotonicity or direction) is correct; for stability checks, it verifies the boolean value. The final reward is a weighted sum over all scored stages, scaled to [0,1]. To earn full credit you must execute the computational workflow as described and generate valid, well-formed output files; simply writing expected numbers without running the workflow will not pass.
