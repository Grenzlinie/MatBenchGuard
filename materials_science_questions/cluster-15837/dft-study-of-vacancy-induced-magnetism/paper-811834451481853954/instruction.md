# DFT investigation of magnetic properties of CrSi12 clusters deposited on Si(111) surface

## Problem background
Silicon endohedral cages such as CrSi12 are exceptionally stable but the encapsulated Cr atom is nonmagnetic – its spin moment is quenched by strong hybridization with the silicon cage. For silicon-based spintronic applications, it is highly desirable to recover a local magnetic moment on the Cr site. Depositing these clusters on a Si(111) surface may allow the formation of new Si–Si bonds that weaken Cr–Si hybridization, thereby partially restoring the Cr magnetic moment. This task investigates whether a finite local Cr spin moment emerges after deposition and under which adsorption geometries it appears, by computing the formation energies and Cr spin moments for four distinct deposition configurations.

## Approach
We employ spin-polarized density functional theory (DFT) within the generalized gradient approximation (GGA). The Si(111) substrate is modeled by a periodic slab with several atomic layers, with the bottom surface passivated by hydrogen and the upper layers allowed to relax. An isolated CrSi12 cluster (hexagonal biprism structure) is first relaxed separately to provide a reference total energy, as is the bare Si(111) slab. The cluster is then placed above the slab in four different initial orientations—hexagonal or quadrangular cage face toward the surface, at various lateral positions—and each combined supercell is structurally relaxed. For each relaxed configuration the formation energy E_F is computed from the total energies of the isolated cluster, clean slab, and combined system. The local spin magnetic moment on the Cr atom is extracted by projecting the spin density onto atomic spheres.

## Reproduction target
Compute, for each of the four deposition configurations (I, II, III, IV), the formation energy E_F = E[CrSi12] + E[Si(111)] − E_T and the local spin magnetic moment μ(Cr) on the chromium atom. The verifier will assess your computed E_F and μ(Cr) against reference values and will check the formation-energy ordering.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- PSLibrary pseudopotentials (or equivalent PAW/PBE library): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate initial structures
- Role: process
- Action: Construct atomic models for the isolated CrSi12 cluster (hexagonal biprism with Cr between two Si6 hexagons), the clean Si(111) slab (9 layers, 16 Si atoms per layer, bottom passivated by H), and the four initial deposition orientations (I–IV) as described in the paper: hexagonal or quadrangular face of the cage toward the surface at various lateral positions.
- Evidence: none

### Step 2: Relax isolated CrSi12 cluster
- Role: process
- Action: Perform spin-polarized DFT relaxation of the isolated CrSi12 cluster in a large supercell using Gamma-point sampling, plane-wave cutoff 300 eV, and PBE functional. Converge forces below 0.01 eV/Å. Record the total energy E[CrSi12] and verify that the local Cr magnetic moment is quenched.
- Evidence: `/app/outputs/isolated_cluster_info.json`

### Step 3: Relax bare Si(111) slab
- Role: process
- Action: Perform spin-polarized DFT relaxation of the clean Si(111) slab with the bottom layers fixed to bulk positions and the top five layers free to relax. Use the same DFT settings as step_02. Obtain the total energy E[Si(111)].
- Evidence: `/app/outputs/slab_info.json`

### Step 4: Deposition simulations and magnetic moments
- Role: scored (load-bearing)
- Action: For each of the four initial deposition configurations (I–IV): set up the CrSi12/Si(111) combined supercell, relax the system (keeping bottom slab layers fixed) until forces < 0.01 eV/Å, compute the total energy E_T, calculate the formation energy E_F = E[CrSi12] + E[Si(111)] − E_T using the reference energies from steps 02 and 03, and extract the local Cr spin moment μ(Cr) by projecting the spin density onto atomic spheres. Write all results to deposition_results.csv.
- Output file: `/app/outputs/deposition_results.csv`
- Format: csv
- Contract: Columns: Configuration (I,II,III,IV), E_CrSi12 (eV), E_Si111 (eV), E_T (eV), E_F (eV), mu_Cr (μB).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/deposition_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### deposition_results.csv
- path: `/app/outputs/deposition_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Formation energies and Cr magnetic moments for four deposition configurations on Si(111). The file must contain one row per configuration (I, II, III, IV) with all columns filled.
- schema:
  - `type`: table
  - `required_columns`: `Configuration`, `E_CrSi12`, `E_Si111`, `E_T`, `E_F`, `mu_Cr`
  - `units`:
    - `E_CrSi12`: eV
    - `E_Si111`: eV
    - `E_T`: eV
    - `E_F`: eV
    - `mu_Cr`: μB

Notes: The hidden checker verifies internal consistency (E_F = E_CrSi12 + E_Si111 - E_T within 1e-4 eV) and compares each row's E_F and mu_Cr to reference values within predetermined tolerances, while also checking that the formation energy ordering matches the expected pattern.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "deposition_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Configuration",
          "E_CrSi12",
          "E_Si111",
          "E_T",
          "E_F",
          "mu_Cr"
        ],
        "units": {
          "E_CrSi12": "eV",
          "E_Si111": "eV",
          "E_T": "eV",
          "E_F": "eV",
          "mu_Cr": "μB"
        }
      },
      "description": "Formation energies and Cr magnetic moments for four deposition configurations on Si(111). The file must contain one row per configuration (I, II, III, IV) with all columns filled."
    }
  ],
  "notes": "The hidden checker verifies internal consistency (E_F = E_CrSi12 + E_Si111 - E_T within 1e-4 eV) and compares each row's E_F and mu_Cr to reference values within predetermined tolerances, while also checking that the formation energy ordering matches the expected pattern."
}
```

## How you are scored
A hidden verifier reads your deposition_results.csv. It first checks internal consistency: for each row, E_F must equal E_CrSi12 + E_Si111 - E_T to within a tight numerical tolerance. It then compares your computed formation energies E_F and Cr spin moments μ(Cr) to reference values obtained from the original study (hidden from you) using generous tolerances that absorb the expected run-to-run spread from different DFT codes and pseudopotential choices. The verifier also verifies that the formation energy ordering among the four configurations matches the pattern reported in the original work. The final reward is a weighted sum over all verification checks; simply reporting numbers that happen to look plausible is not sufficient—the values must be consistent with a genuine DFT relaxation of each configuration.
