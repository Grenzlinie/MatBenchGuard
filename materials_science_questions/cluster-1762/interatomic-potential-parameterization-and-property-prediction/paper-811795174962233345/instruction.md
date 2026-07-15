# DFT Characterization of Li-Induced Polar Clusters in KTaO3

## Problem background
Li-doped potassium tantalate (K₁₋ₓLiₓTaO₃, or KLT) is a quantum paraelectric material in which substitutional Li impurities introduce local dipoles and can induce a relaxor state. The microscopic arrangement of these Li-induced polar distortions—their direction, magnitude, and spatial extent—is key to understanding the dielectric anomalies and possible relaxor behaviour of KLT. Density-functional theory (DFT) calculations can quantify the off-center displacements of Li, the energy landscape it experiences, the accompanying polarization of the host KTaO₃ lattice, and the interactions between neighbouring Li impurities.

## Approach
This task employs first-principles DFT calculations within the local‑density approximation (LDA) using the open‑source ABINIT code (or an equivalent LDA‑based plane‑wave code). The core idea is to model a single Li impurity and pairs of Li impurities in a periodic supercell of cubic KTaO₃, determine their stable off‑center positions, and extract the resulting energies, polarisation, and local structural distortions. By computing reference properties of pure KTaO₃ (phonon frequencies, dielectric constants), one can calibrate the host matrix and later use its dielectric response to separate the long‑range dipole‑dipole interaction from the short‑range local potential felt by Li. The workflow spans: (1) a reference calculation on pristine KTaO₃; (2) geometry relaxation and Berry‑phase polarisation for one Li in a 3×3×3 supercell along several crystallographic directions; (3) fitting a sixth‑order polynomial local potential; (4) evaluating pair interaction energies for two first‑neighbour Li impurities in three relative off‑centre configurations; (5) extracting the energy barriers for Li hopping between equivalent minima; and (6) analysing the Ta–O bond alternations to estimate the lateral thickness of the polar cluster around a single Li.

## Reproduction target
Compute, from LDA‑DFT, the following quantities for Li‑doped KTaO₃ at a Li concentration corresponding to one K replaced in a 3×3×3 supercell:
- The three lowest transverse‑optical (TO) phonon frequencies at the Γ point of pure cubic KTaO₃, together with the static and electronic dielectric constants.
- The off‑centre energies and displacement amplitudes of a single Li impurity when the Li is forced to move along [001], [110] and [111] directions, including the total spontaneous polarisation and the separate dipole contributions of the Li itself and of the host matrix.
- The coefficients of a sixth‑order local potential fitted to the corrected single‑Li energies.
- The interaction energies between two first‑neighbour Li impurities in three configurations: antiparallel displacements along the bond, parallel displacements perpendicular to the bond, and parallel displacements along the bond.
- The energy barriers for Li hopping from its [001] minimum towards the [111] and [110] saddle points.
- The average polar distortion (Ta–O bond alternation) in the three inequivalent Ta–O chains surrounding the Li impurity and an estimate of the lateral thickness (in lattice constant units) beyond which the distortion becomes negligible.

## Assets

- ABINIT DFT code: https://www.abinit.org
- Troullier-Martins pseudopotentials for K, Ta, Li, O: https://www.abinit.org/downloads/pseudopotentials
- KTaO3 cubic crystal structure (space group Pm-3m, lattice constant 3.983 Å)

## Workflow steps

### Step 1: Pure KTaO3 reference calculation
- Role: scored
- Action: Perform DFT-LDA calculation for cubic KTaO3 (5-atom unit cell) at the experimental lattice constant 3.983 Å. Compute the three lowest TO phonon frequencies at the Γ point and the static and electronic dielectric constants.
- Output file: `/app/outputs/step_00_pure_KTO.json`
- Format: json
- Contract: {"TO1_frequency_cm-1": float, "TO2_frequency_cm-1": float, "TO3_frequency_cm-1": float, "static_dielectric_constant": float, "electronic_dielectric_constant": float}
- Scoring: scored by hidden verifier

### Step 2: Single Li impurity DFT and property extraction
- Role: scored (load-bearing)
- Action: Build a 3×3×3 KTaO3 supercell with one K replaced by Li. Relax with Li displaced along [001], [110], [111] and at the high-symmetry site. Compute total energies relative to the high-symmetry site and Li off-center displacements. For the [001] displacement, perform Berry-phase polarization along the displacement path to obtain total spontaneous polarization and total dipole. Estimate the Li contribution to the dipole via finite-displacement calculation and compute the matrix contribution as the difference. After correcting for periodic-image dipole-dipole interactions (using the static dielectric constant from step_00), fit a sixth-order polynomial local potential to obtain coefficients A1, A11, A12, A111, A112, A123.
- Output file: `/app/outputs/step_01_single_Li.json`
- Format: json
- Contract: {"Li_energy_[001]_eV": float, "Li_displacement_[001]_A": float, "total_polarization_Cm2": float, "total_dipole_eA": float, "Li_dipole_contribution_eA": float, "matrix_dipole_contribution_eA": float, "Li_energy_[110]_eV": float, "Li_displacement_[110]_A": float, "Li_energy_[111]_eV": float, "Li_displacement_[111]_A": float, "A1_eV_per_A2": float, "A11_eV_per_A4": float, "A12_eV_per_A4": float, "A111_eV_per_A6": float, "A112_eV_per_A6": float, "A123_eV_per_A6": float}
- Scoring: scored by hidden verifier

### Step 3: Two-Li nearest-neighbor interaction
- Role: scored
- Action: In the same 3×3×3 supercell, replace two K atoms by Li in first-neighbor positions. Optimize three configurations with different relative off-center displacements (antiparallel along the bond, parallel perpendicular to the bond, parallel along the bond). Compute total energies relative to the configuration with both Li undisplaced, and derive interaction energies (difference from twice the single-Li energy).
- Output file: `/app/outputs/step_02_pair_interaction.json`
- Format: json
- Contract: {"config_a_energy_relative_to_undisplaced_eV": float, "config_b_energy_relative_to_undisplaced_eV": float, "config_c_energy_relative_to_undisplaced_eV": float, "interaction_energy_config_a_eV": float, "interaction_energy_config_b_eV": float, "interaction_energy_config_c_eV": float}
- Scoring: scored by hidden verifier

### Step 4: Li hopping barrier
- Role: scored
- Action: From the energies obtained in step_01, compute the energy difference between the [001] minimum and the saddle points along [111] and [110]. These are the barriers for Li hopping.
- Output file: `/app/outputs/step_03_energy_barrier.json`
- Format: json
- Contract: {"barrier_[111]_path_eV": float, "barrier_[110]_path_eV": float}
- Scoring: scored by hidden verifier

### Step 5: Polar cluster lateral thickness
- Role: scored
- Action: Using the atomic displacement fields from step_01 (Li displaced along [001]), analyze the Ta-O distances along the [001] direction in the three inequivalent Ta-O chains surrounding the Li. Compute the average polar distortion (difference d1-d2, d3-d4, d5-d6) for each chain type, and estimate the lateral thickness (in units of the cubic lattice constant) beyond which the distortion becomes negligible.
- Output file: `/app/outputs/step_04_polar_cluster.json`
- Format: json
- Contract: {"chain1_avg_distortion_A": float, "chain2_avg_distortion_A": float, "chain3_avg_distortion_A": float, "lateral_thickness_lattice_constants": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_00_pure_KTO.json`
- `/app/outputs/step_01_single_Li.json`
- `/app/outputs/step_02_pair_interaction.json`
- `/app/outputs/step_03_energy_barrier.json`
- `/app/outputs/step_04_polar_cluster.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_00_pure_KTO.json
- path: `/app/outputs/step_00_pure_KTO.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Host matrix phonon frequencies and dielectric properties from DFT-LDA.
- schema:
  - `type`: object
  - `required`: `TO1_frequency_cm-1`, `TO2_frequency_cm-1`, `TO3_frequency_cm-1`, `static_dielectric_constant`, `electronic_dielectric_constant`
  - `properties`:
    - `TO1_frequency_cm-1`:
      - `type`: number
    - `TO2_frequency_cm-1`:
      - `type`: number
    - `TO3_frequency_cm-1`:
      - `type`: number
    - `static_dielectric_constant`:
      - `type`: number
    - `electronic_dielectric_constant`:
      - `type`: number

### step_01_single_Li.json
- path: `/app/outputs/step_01_single_Li.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single Li impurity properties: off-center energies, displacements, polarization, dipole contributions, and sixth-order local potential coefficients.
- schema:
  - `type`: object
  - `required`: `Li_energy_[001]_eV`, `Li_displacement_[001]_A`, `total_polarization_Cm2`, `total_dipole_eA`, `Li_dipole_contribution_eA`, `matrix_dipole_contribution_eA`, `Li_energy_[110]_eV`, `Li_displacement_[110]_A`, `Li_energy_[111]_eV`, `Li_displacement_[111]_A`, `A1_eV_per_A2`, `A11_eV_per_A4`, `A12_eV_per_A4`, `A111_eV_per_A6`, `A112_eV_per_A6`, `A123_eV_per_A6`
  - `properties`:
    - `Li_energy_[001]_eV`:
      - `type`: number
    - `Li_displacement_[001]_A`:
      - `type`: number
    - `total_polarization_Cm2`:
      - `type`: number
    - `total_dipole_eA`:
      - `type`: number
    - `Li_dipole_contribution_eA`:
      - `type`: number
    - `matrix_dipole_contribution_eA`:
      - `type`: number
    - `Li_energy_[110]_eV`:
      - `type`: number
    - `Li_displacement_[110]_A`:
      - `type`: number
    - `Li_energy_[111]_eV`:
      - `type`: number
    - `Li_displacement_[111]_A`:
      - `type`: number
    - `A1_eV_per_A2`:
      - `type`: number
    - `A11_eV_per_A4`:
      - `type`: number
    - `A12_eV_per_A4`:
      - `type`: number
    - `A111_eV_per_A6`:
      - `type`: number
    - `A112_eV_per_A6`:
      - `type`: number
    - `A123_eV_per_A6`:
      - `type`: number

### step_02_pair_interaction.json
- path: `/app/outputs/step_02_pair_interaction.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Two-Li nearest-neighbor interaction energies for three configurations.
- schema:
  - `type`: object
  - `required`: `config_a_energy_relative_to_undisplaced_eV`, `config_b_energy_relative_to_undisplaced_eV`, `config_c_energy_relative_to_undisplaced_eV`, `interaction_energy_config_a_eV`, `interaction_energy_config_b_eV`, `interaction_energy_config_c_eV`
  - `properties`:
    - `config_a_energy_relative_to_undisplaced_eV`:
      - `type`: number
    - `config_b_energy_relative_to_undisplaced_eV`:
      - `type`: number
    - `config_c_energy_relative_to_undisplaced_eV`:
      - `type`: number
    - `interaction_energy_config_a_eV`:
      - `type`: number
    - `interaction_energy_config_b_eV`:
      - `type`: number
    - `interaction_energy_config_c_eV`:
      - `type`: number

### step_03_energy_barrier.json
- path: `/app/outputs/step_03_energy_barrier.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Li hopping barriers via [111] and [110] saddle points.
- schema:
  - `type`: object
  - `required`: `barrier_[111]_path_eV`, `barrier_[110]_path_eV`
  - `properties`:
    - `barrier_[111]_path_eV`:
      - `type`: number
    - `barrier_[110]_path_eV`:
      - `type`: number

### step_04_polar_cluster.json
- path: `/app/outputs/step_04_polar_cluster.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polar cluster lateral extent: average Ta-O distortions in three chain types and estimated thickness in lattice constants.
- schema:
  - `type`: object
  - `required`: `chain1_avg_distortion_A`, `chain2_avg_distortion_A`, `chain3_avg_distortion_A`, `lateral_thickness_lattice_constants`
  - `properties`:
    - `chain1_avg_distortion_A`:
      - `type`: number
    - `chain2_avg_distortion_A`:
      - `type`: number
    - `chain3_avg_distortion_A`:
      - `type`: number
    - `lateral_thickness_lattice_constants`:
      - `type`: number

Notes: All scored values are compared against the paper-reported LDA-level results with tolerances and structural checks (energy ordering, barrier ordering, interaction energy sign).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_00_pure_KTO.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "TO1_frequency_cm-1",
          "TO2_frequency_cm-1",
          "TO3_frequency_cm-1",
          "static_dielectric_constant",
          "electronic_dielectric_constant"
        ],
        "properties": {
          "TO1_frequency_cm-1": {
            "type": "number"
          },
          "TO2_frequency_cm-1": {
            "type": "number"
          },
          "TO3_frequency_cm-1": {
            "type": "number"
          },
          "static_dielectric_constant": {
            "type": "number"
          },
          "electronic_dielectric_constant": {
            "type": "number"
          }
        }
      },
      "description": "Host matrix phonon frequencies and dielectric properties from DFT-LDA."
    },
    {
      "file": "step_01_single_Li.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Li_energy_[001]_eV",
          "Li_displacement_[001]_A",
          "total_polarization_Cm2",
          "total_dipole_eA",
          "Li_dipole_contribution_eA",
          "matrix_dipole_contribution_eA",
          "Li_energy_[110]_eV",
          "Li_displacement_[110]_A",
          "Li_energy_[111]_eV",
          "Li_displacement_[111]_A",
          "A1_eV_per_A2",
          "A11_eV_per_A4",
          "A12_eV_per_A4",
          "A111_eV_per_A6",
          "A112_eV_per_A6",
          "A123_eV_per_A6"
        ],
        "properties": {
          "Li_energy_[001]_eV": {
            "type": "number"
          },
          "Li_displacement_[001]_A": {
            "type": "number"
          },
          "total_polarization_Cm2": {
            "type": "number"
          },
          "total_dipole_eA": {
            "type": "number"
          },
          "Li_dipole_contribution_eA": {
            "type": "number"
          },
          "matrix_dipole_contribution_eA": {
            "type": "number"
          },
          "Li_energy_[110]_eV": {
            "type": "number"
          },
          "Li_displacement_[110]_A": {
            "type": "number"
          },
          "Li_energy_[111]_eV": {
            "type": "number"
          },
          "Li_displacement_[111]_A": {
            "type": "number"
          },
          "A1_eV_per_A2": {
            "type": "number"
          },
          "A11_eV_per_A4": {
            "type": "number"
          },
          "A12_eV_per_A4": {
            "type": "number"
          },
          "A111_eV_per_A6": {
            "type": "number"
          },
          "A112_eV_per_A6": {
            "type": "number"
          },
          "A123_eV_per_A6": {
            "type": "number"
          }
        }
      },
      "description": "Single Li impurity properties: off-center energies, displacements, polarization, dipole contributions, and sixth-order local potential coefficients."
    },
    {
      "file": "step_02_pair_interaction.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "config_a_energy_relative_to_undisplaced_eV",
          "config_b_energy_relative_to_undisplaced_eV",
          "config_c_energy_relative_to_undisplaced_eV",
          "interaction_energy_config_a_eV",
          "interaction_energy_config_b_eV",
          "interaction_energy_config_c_eV"
        ],
        "properties": {
          "config_a_energy_relative_to_undisplaced_eV": {
            "type": "number"
          },
          "config_b_energy_relative_to_undisplaced_eV": {
            "type": "number"
          },
          "config_c_energy_relative_to_undisplaced_eV": {
            "type": "number"
          },
          "interaction_energy_config_a_eV": {
            "type": "number"
          },
          "interaction_energy_config_b_eV": {
            "type": "number"
          },
          "interaction_energy_config_c_eV": {
            "type": "number"
          }
        }
      },
      "description": "Two-Li nearest-neighbor interaction energies for three configurations."
    },
    {
      "file": "step_03_energy_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "barrier_[111]_path_eV",
          "barrier_[110]_path_eV"
        ],
        "properties": {
          "barrier_[111]_path_eV": {
            "type": "number"
          },
          "barrier_[110]_path_eV": {
            "type": "number"
          }
        }
      },
      "description": "Li hopping barriers via [111] and [110] saddle points."
    },
    {
      "file": "step_04_polar_cluster.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "chain1_avg_distortion_A",
          "chain2_avg_distortion_A",
          "chain3_avg_distortion_A",
          "lateral_thickness_lattice_constants"
        ],
        "properties": {
          "chain1_avg_distortion_A": {
            "type": "number"
          },
          "chain2_avg_distortion_A": {
            "type": "number"
          },
          "chain3_avg_distortion_A": {
            "type": "number"
          },
          "lateral_thickness_lattice_constants": {
            "type": "number"
          }
        }
      },
      "description": "Polar cluster lateral extent: average Ta-O distortions in three chain types and estimated thickness in lattice constants."
    }
  ],
  "notes": "All scored values are compared against the paper-reported LDA-level results with tolerances and structural checks (energy ordering, barrier ordering, interaction energy sign)."
}
```

## How you are scored
A hidden verifier reads each of the five JSON output files you produce. For every scored stage, it extracts the numerical values according to the declared output schema and compares them against hidden reference criteria. The criteria include both direct comparisons with expected physical quantities and checks of relative ordering or sign relationships among related quantities. The per‑stage scores are combined by weight (the single‑Li results carry the most weight) to yield a final reward between 0 and 1. Simply reporting the paper’s numbers is not sufficient; the verifier assesses whether your computed results satisfy the underlying physical expectations that define a correct reproduction.
