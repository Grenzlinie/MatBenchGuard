# Strain-dependent phase diagram and multiferroic properties from first-principles

## Problem background
Perovskite oxide superlattices composed of alternating layers with complementary properties offer a rich platform for engineering multiferroic materials that simultaneously exhibit ferroelectricity, ferromagnetism, and strong magnetoelectric coupling. The (SrCoO3)1/(SrTiO3)1 superlattice is a promising candidate: SrCoO3 undergoes spin-state transitions and Jahn-Teller distortions, while SrTiO3 is near a ferroelectric instability. Epitaxial strain imposed by a substrate can tune the subtle balance between structural distortions, magnetic order, and electronic properties, potentially stabilizing phases with large polarization and magnetization. A first-principles investigation of this system across a range of epitaxial strains is required to understand the sequence of ground-state structural symmetries and magnetic orderings, and to quantify the multiferroic performance of any emergent ferroelectric ferromagnetic phase.

## Approach
The calculation employs density functional theory with the generalized gradient approximation (GGA) plus an on-site Hubbard U correction (GGA+U) applied to the Co 3d states, using an open-source plane-wave code. Candidate crystal structures derived from oxygen-octahedron tilting and polar-distortion patterns are considered: high-symmetry P4mm and the distorted symmetries Pbam, P21/c, C2/m, and Pc. For each symmetry, both ferromagnetic and A-type antiferromagnetic spin configurations are examined. A √2×√2×1 supercell of the perovskite unit cell (20 atoms) is used. To simulate epitaxial strain, the in-plane lattice constant a is fixed to a0(1+e) with a0 = 3.940 Å (the equilibrium lattice constant of SrTiO3) across a strain grid from e = -5.6% to +5.89%, while the out-of-plane lattice constant c and all internal coordinates are fully relaxed. Total energies are collected and used to construct a phase diagram showing the lowest-energy structural symmetry and magnetic character at each strain. For the candidate multiferroic Pc phase at a specific tensile strain, advanced properties are computed: the ferroelectric polarization is obtained via Berry-phase calculation relative to a nonpolar reference; the magnetocrystalline anisotropy energy (MAE) is evaluated from spin-orbit coupling calculations in two high-symmetry planes; and the magnetoelectric constant α is estimated using the Íñiguez method, which involves scanning the polar-mode distortion amplitude between the paraelectric and ferroelectric structures and extracting the linear response of polarization, magnetization, and total energy.

## Reproduction target
Produce two output artifacts. (1) An epitaxial strain phase diagram table containing, for each strain value on a grid covering -5.6% to +5.89%, the ground-state structural symmetry (one of P4mm, Pbam, P21/c, C2/m, Pc) and magnetic character (FM or AFM). (2) A multiferroic properties table for the Pc phase at e = 2.3%, reporting the smallest band gap (eV), total magnetic moment per unit cell (μB), three Cartesian components of the electric polarization vector (μC/cm²), the magnetocrystalline anisotropy energy in the (001) plane (meV/Co) and in the (100) plane (meV/Co), and the magnetoelectric constant α (Gaussian units).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Generate superlattice structural models and DFT input files
- Role: process
- Action: Generate the √2×√2×1 supercell structures of the (SrCoO3)1/(SrTiO3)1 superlattice for each candidate symmetry (P4mm, Pbam, P21/c, C2/m, Pc) with ferromagnetic (FM) and A‑type antiferromagnetic (AFM) spin orderings. Prepare Quantum ESPRESSO input files for each structure on a grid of epitaxial strain values from -5.6% to 5.89% (step ~0.5%). Apply the GGA+U approach with an on‑site Coulomb parameter Ueff = 1.9 eV on Co 3d.
- Evidence: `/app/outputs/input_files_summary.txt`

### Step 2: DFT+U structural relaxations across strains and symmetries
- Role: process
- Action: For every candidate symmetry, magnetic ordering, and strain value, perform a full ionic relaxation with Quantum ESPRESSO (pw.x). Fix the in‑plane lattice constant a to the strain‑imposed value (a = a0(1+e), a0=3.940 Å) and relax the out‑of‑plane lattice constant c and all internal coordinates. Collect total energies, relaxed geometries, and basic electronic properties (spin‑up/spin‑down band gaps, magnetic moments).
- Evidence: `/app/outputs/relax_log.txt`

### Step 3: Extract epitaxial strain phase diagram
- Role: scored (load-bearing)
- Action: From the total energies computed in step_02, identify the lowest‑energy symmetry and magnetic order at each strain point. Produce a phase diagram as a CSV file.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: columns: strain (numeric, percent), ground_state_symmetry (string, one of P4mm, Pbam, P21/c, C2/m, Pc), magnetic_character (string, FM or AFM)
- Scoring: scored by hidden verifier

### Step 4: Compute advanced multiferroic properties for Pc phase
- Role: process
- Action: Using the relaxed Pc structure at e=2.3% from step_02, perform: (a) a Berry‑phase calculation to obtain the electric polarization components relative to the P21/c reference; (b) spin‑orbit coupling calculations to compute the magnetocrystalline anisotropy energy (MAE) in the (001) and (100) planes; (c) estimate the magnetoelectric constant α by scanning the polar‑mode amplitude between the P21/c and Pc structures, fitting the polarization, magnetization and total energy to obtain the linear coefficients. Store detailed intermediate results in a JSON file.
- Evidence: `/app/outputs/multiferroic_raw_results.json`

### Step 5: Compile multiferroic properties table
- Role: scored (load-bearing)
- Action: Gather the computed properties for the Pc multiferroic state at e=2.3%: smallest band gap between spin‑up and spin‑down (eV), total magnetic moment per unit cell (μB), polarization components Px, Py, Pz (μC/cm²), MAE in the (001) and (100) planes (meV/Co), and magnetoelectric constant α (Gaussian units). Write the consolidated results to a CSV file.
- Output file: `/app/outputs/multiferroic_properties.csv`
- Format: csv
- Contract: columns: strain (numeric, 2.3), band_gap_eV (numeric), total_magnetic_moment_mu_B (numeric), Px_muC_cm2 (numeric), Py_muC_cm2 (numeric), Pz_muC_cm2 (numeric), MAE_001_meV_per_Co (numeric), MAE_100_meV_per_Co (numeric), alpha_gaussian_unit (numeric)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`
- `/app/outputs/multiferroic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Epitaxial strain phase diagram: the ground‑state structural symmetry and magnetic ordering identified at each strain value.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `ground_state_symmetry`, `magnetic_character`
  - `units`:
    - `strain`: percent
    - `ground_state_symmetry`: string, one of P4mm, Pbam, P21/c, C2/m, Pc
    - `magnetic_character`: string, FM or AFM

### multiferroic_properties.csv
- path: `/app/outputs/multiferroic_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Multiferroic properties of the Pc phase at e=2.3%: electronic band gap, total magnetic moment, electric polarization components, magnetocrystalline anisotropy energies, and magnetoelectric constant α.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `band_gap_eV`, `total_magnetic_moment_mu_B`, `Px_muC_cm2`, `Py_muC_cm2`, `Pz_muC_cm2`, `MAE_001_meV_per_Co`, `MAE_100_meV_per_Co`, `alpha_gaussian_unit`
  - `units`:
    - `strain`: percent
    - `band_gap_eV`: eV
    - `total_magnetic_moment_mu_B`: μB
    - `Px_muC_cm2`: μC/cm²
    - `Py_muC_cm2`: μC/cm²
    - `Pz_muC_cm2`: μC/cm²
    - `MAE_001_meV_per_Co`: meV/Co
    - `MAE_100_meV_per_Co`: meV/Co
    - `alpha_gaussian_unit`: dimensionless (Gaussian units)

Notes: The phase diagram is compared against the reference sequence reported in the paper; each row's ground_state_symmetry and magnetic_character must match within the tolerance on the strain boundary position. The multiferroic properties are compared numerically with appropriate tolerances to account for differences between Quantum ESPRESSO and the paper's original VASP calculations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "ground_state_symmetry",
          "magnetic_character"
        ],
        "units": {
          "strain": "percent",
          "ground_state_symmetry": "string, one of P4mm, Pbam, P21/c, C2/m, Pc",
          "magnetic_character": "string, FM or AFM"
        }
      },
      "description": "Epitaxial strain phase diagram: the ground‑state structural symmetry and magnetic ordering identified at each strain value."
    },
    {
      "file": "multiferroic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "band_gap_eV",
          "total_magnetic_moment_mu_B",
          "Px_muC_cm2",
          "Py_muC_cm2",
          "Pz_muC_cm2",
          "MAE_001_meV_per_Co",
          "MAE_100_meV_per_Co",
          "alpha_gaussian_unit"
        ],
        "units": {
          "strain": "percent",
          "band_gap_eV": "eV",
          "total_magnetic_moment_mu_B": "μB",
          "Px_muC_cm2": "μC/cm²",
          "Py_muC_cm2": "μC/cm²",
          "Pz_muC_cm2": "μC/cm²",
          "MAE_001_meV_per_Co": "meV/Co",
          "MAE_100_meV_per_Co": "meV/Co",
          "alpha_gaussian_unit": "dimensionless (Gaussian units)"
        }
      },
      "description": "Multiferroic properties of the Pc phase at e=2.3%: electronic band gap, total magnetic moment, electric polarization components, magnetocrystalline anisotropy energies, and magnetoelectric constant α."
    }
  ],
  "notes": "The phase diagram is compared against the reference sequence reported in the paper; each row's ground_state_symmetry and magnetic_character must match within the tolerance on the strain boundary position. The multiferroic properties are compared numerically with appropriate tolerances to account for differences between Quantum ESPRESSO and the paper's original VASP calculations."
}
```

## How you are scored
A hidden verifier program independently evaluates each output file. For the phase diagram, the verifier compares the reported ground-state symmetry and magnetic character at each strain to a known reference sequence and awards credit based on the fraction of correctly identified phases, accounting for acceptable shifts in strain boundaries. For the multiferroic properties, each numeric value is compared to a reference with appropriate tolerances that absorb the expected differences between different DFT implementations. The total reward is a weighted sum of the scores from both artifacts; the multiferroic properties and the main phase boundaries carry the largest weights. Merely reporting numbers that happen to match the reference without executing the required DFT workflow is not sufficient—the verifier may also check for consistency and completeness of the workflow evidence.
