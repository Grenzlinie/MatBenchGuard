# DFT prediction of stable pentagonal BxNy monolayers, mechanical properties, and strain-tunable band gap transition

## Problem background
Two-dimensional pentagonal materials, such as penta-graphene, exhibit interesting mechanical and electronic properties. This task concerns the search for stable pentagonal boron nitride (B_xN_y) monolayers with varying stoichiometries. By constructing all possible atomic arrangements on the pentagonal lattice, we can assess their relative stability, identify the dynamically stable configurations, and compute their strain-dependent mechanical response and electronic band behavior. The core computational goal is to answer: which of the candidate pentagonal B_xN_y structures are both energetically and dynamically stable, and how do their mechanical properties (Young's modulus, intrinsic strength, fracture strain) and electronic properties (band gap, direct vs indirect character) evolve under tensile deformation?

## Approach
The reproduction is performed entirely with first-principles density functional theory (DFT) using the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and norm-conserving or PAW pseudopotentials. The conceptual workflow proceeds as follows:

1. **Structure construction** – Generate the 16 unrelaxed candidate B_xN_y monolayers by systematically placing B and N atoms on the sp² and sp³ sites of the known pentagonal network, covering stoichiometric ratios 1:5, 5:1, 1:2, 2:1, and 1:1.
2. **Relaxation and energy ranking** – Fully optimize the geometry of each candidate and collect the relaxed total energy. Among configurations of the same B:N ratio, the one with the lowest energy is considered energetically preferred.
3. **Phonon stability analysis** – For the lowest-energy configurations (and any structures that undergo a structural transition), compute finite-displacement phonon dispersions. A structure is dynamically stable if its phonon spectrum contains no imaginary modes.
4. **Stable structure identification** – Cross-reference the energetic ranking and phonon stability to select the structures that are both lowest in energy for their stoichiometry and free of soft modes.
5. **Tensile strain simulations** – For each stable structure, apply incremental biaxial and uniaxial (X- and Y-direction) tensile strain in 1% steps until fracture. At each strain step extract the stress tensor and the Kohn-Sham eigenvalues.
6. **Mechanical property extraction** – From the stress-strain curves, compute the 3D Young's modulus (E) using the supercell volume and an effective thickness d = layer thickness + van der Waals gap, the 2D Young's modulus (Y = E × d), the intrinsic strength τ_c, and the fracture strain ε_c.
7. **Band gap evolution under uniaxial strain** – For any stable semiconductor, determine the band gap magnitude and its character (direct or indirect) at each uniaxial strain increment.

All calculations are carried out with an open-source DFT code (e.g. Quantum ESPRESSO) and a phonon analysis package (e.g. Phonopy). The workflow compares alternative structures within each stoichiometry and contrasts the mechanical/electronic response between the stable monolayers and between different strain directions, thereby evaluating the anisotropy and strain-tunability of these materials.

## Reproduction target
The objective is to compute and report the following quantities, strictly following the step sequence defined in the workflow:

- **Candidate energies** (`/app/outputs/candidate_energies.json`): The relaxed total energy (eV per unit cell) for each of the 16 candidate penta-B_xN_y structures, labelled by stoichiometry and configuration (e.g. B1N5-I, B1N5-II, … B3N3-III).
- **Phonon stability** (`/app/outputs/phonon_summary.json`): A dynamical stability verdict (stable/unstable) for each tested structure based on its phonon dispersion.
- **Stable structure list** (`/app/outputs/stable_structures.txt`): The names of the pentagonal B_xN_y configurations that are both energetically preferred (within their stoichiometry) and dynamically stable.
- **Mechanical properties** (`/app/outputs/mechanical_properties.json`): For each stable structure, under biaxial, X-axial, and Y-axial tensile loading, report the 3D Young's modulus E (GPa), the 2D Young's modulus Y (N/m), the intrinsic strength τ_c (GPa), and the fracture strain ε_c (as a decimal). Use the effective thickness d = (layer thickness + 3.4 Å) to convert between E and Y.
- **Band gap under strain** (`/app/outputs/band_gap_strain.csv`): For any stable semiconducting monolayer, record the band gap (eV) and band type (direct or indirect) at each integer strain percent under uniaxial tension, from 0% up to the fracture strain.

No precomputed energies, phonon results, or structural data are provided; everything must be generated from the initial atomic configurations using the described computational protocol.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Pseudopotential library (SSSP efficiency / GBRV): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Construct candidate structures
- Role: process
- Action: Generate all unrelaxed atomic configurations for pentagonal BxNy monolayers with stoichiometries 1:5, 5:1, 1:2, 2:1, 1:1 by placing B and N atoms on sp² and sp³ sites of the known pentagonal lattice, producing the 16 candidate structures (e.g., B1N5-I, B2N4-I, B3N3-I, etc.).
- Evidence: none

### Step 2: DFT relaxation and energy collection
- Role: scored
- Action: Perform full geometry optimization for each candidate structure using DFT (GGA-PBE functional, PAW pseudopotentials, plane-wave cutoff and k-point mesh ensuring convergence, with vacuum to avoid periodic interaction) until forces and total energies converge. Record the relaxed total energy per unit cell for each structure.
- Output file: `/app/outputs/candidate_energies.json`
- Format: json
- Contract: JSON object with keys like B1N5-I, B1N5-II, ... B3N3-III, each value a float energy in eV.
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion calculations
- Role: process
- Action: For the lowest-energy configurations that retain the pentagonal network and any structures that underwent structural transition, perform finite-displacement phonon calculations using Phonopy with appropriate supercells and q‑grid to obtain phonon dispersions.
- Evidence: none

### Step 4: Phonon stability summary
- Role: scored
- Action: Analyze the computed phonon dispersions. For each tested structure, record whether it is dynamically stable (no imaginary modes) or unstable (presence of soft modes). Write the stability assessment to phonon_summary.json.
- Output file: `/app/outputs/phonon_summary.json`
- Format: json
- Contract: JSON object mapping structure name (e.g., B2N4-I) to an object with a key 'stable' (boolean) or a list of imaginary modes.
- Scoring: scored by hidden verifier

### Step 5: Stable structure identification
- Role: scored
- Action: From the lowest-energy structures per stoichiometry and the phonon stability results, identify the configurations that are both energetically preferred (by energy comparison from step s2) and dynamically stable. Write the names of the stable pentagonal BxNy configurations to stable_structures.txt, one per line.
- Output file: `/app/outputs/stable_structures.txt`
- Format: txt
- Contract: Text file with one stable structure name per line (e.g., B2N4-I).
- Scoring: scored by hidden verifier

### Step 6: Strain DFT simulations
- Role: process
- Action: For the identified stable structures B2N4-I and B3N3-I, apply incremental uniaxial (along X and Y) and biaxial tensile strain in steps of 1% from equilibrium until fracture. At each strain step run DFT to obtain stress tensors and Kohn-Sham eigenvalues.
- Evidence: none

### Step 7: Mechanical properties extraction
- Role: scored (load-bearing)
- Action: From the stress-strain data, compute the 3D Young's modulus E (GPa) using the supercell volume and effective thickness d = (layer thickness + 3.4 Å), 2D Young's modulus Y (N/m) = E × d, intrinsic strength τ_c (GPa) and fracture strain ε_c (decimal) for each strain direction (biaxial, X-axial, Y-axial). Output the results for B2N4-I and B3N3-I.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: JSON object with keys B2N4-I and B3N3-I. Each value is a dict with keys 'biaxial', 'X-axial', 'Y-axial'. Each direction maps to an object with fields E_GPa (float), Y_N_m (float), tau_c_GPa (float), epsilon_c (float decimal).
- Scoring: scored by hidden verifier

### Step 8: Band gap analysis under strain
- Role: scored (load-bearing)
- Action: Using the Kohn-Sham eigenvalues from the uniaxial strain simulations of B3N3-I, determine the band gap (eV) and band type (direct or indirect) at each strain increment. Write the results to band_gap_strain.csv.
- Output file: `/app/outputs/band_gap_strain.csv`
- Format: csv
- Contract: CSV with columns strain_percent (int), band_gap_eV (float, 3 decimal places), band_type (string: 'direct' or 'indirect').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/candidate_energies.json`
- `/app/outputs/phonon_summary.json`
- `/app/outputs/stable_structures.txt`
- `/app/outputs/mechanical_properties.json`
- `/app/outputs/band_gap_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### candidate_energies.json
- path: `/app/outputs/candidate_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed total energies per unit cell for all 16 candidate pentagonal BxNy structures. The checker will compare energy differences between competing configurations for each stoichiometry (e.g., (B1N5-I - B1N5-II)) to hidden reference differences and verify that the lowest-energy structure per ratio matches the paper.
- schema:
  - `type`: object
  - `required`:
    - `B1N5-I`: float (energy in eV)
    - `B1N5-II`: float (energy in eV)
    - `B5N1-I`: float (energy in eV)
    - `B5N1-II`: float (energy in eV)
    - `B2N4-I`: float (energy in eV)
    - `B2N4-II`: float (energy in eV)
    - `B2N4-III`: float (energy in eV)
    - `B2N4-IV`: float (energy in eV)
    - `B4N2-I`: float (energy in eV)
    - `B4N2-II`: float (energy in eV)
    - `B4N2-III`: float (energy in eV)
    - `B4N2-IV`: float (energy in eV)
    - `B3N3-I`: float (energy in eV)
    - `B3N3-II`: float (energy in eV)
    - `B3N3-III`: float (energy in eV)

### phonon_summary.json
- path: `/app/outputs/phonon_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon stability assessment for each tested structure, containing a boolean 'stable' flag or information about imaginary modes.
- schema:
  - `type`: object
  - `required`:
    - `B1N5-I`: object
    - `B5N1-II`: object
    - `B2N4-I`: object
    - `B4N2-I`: object
    - `B4N2-III`: object
    - `B4N2-IV`: object
    - `B3N3-I`: object

### stable_structures.txt
- path: `/app/outputs/stable_structures.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: List of the dynamically stable pentagonal BxNy configurations expected to contain B2N4-I and B3N3-I.
- schema:
  - `type`: text
  - `pattern`: One stable structure name per line (e.g., B2N4-I).

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed 3D/2D Young's moduli, intrinsic strength, and fracture strain for B2N4-I and B3N3-I under biaxial and uniaxial strain. The checker will compare each value to paper‑reported references with relative tolerances (E, Y ±15%, τ_c ±20%, ε_c ±2pp absolute); a result that meets or exceeds the reference (i.e., within tolerance) earns full credit.
- schema:
  - `type`: object
  - `required`:
    - `B2N4-I`:
      - `biaxial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float
      - `X-axial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float
      - `Y-axial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float
    - `B3N3-I`:
      - `biaxial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float
      - `X-axial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float
      - `Y-axial`:
        - `E_GPa`: float
        - `Y_N_m`: float
        - `tau_c_GPa`: float
        - `epsilon_c`: float

### band_gap_strain.csv
- path: `/app/outputs/band_gap_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Band gap (eV) and direct/indirect character for B3N3-I under uniaxial tensile strain at each 1% strain step. The checker will verify that the band gap increases monotonically, the gap at 0% is near 0.06 eV and at 8% near 0.57 eV, and that band_type transitions from 'direct' to 'indirect' at a strain between 4% and 6%.
- schema:
  - `type`: table
  - `required_columns`: `strain_percent`, `band_gap_eV`, `band_type`

Notes: All scored artifacts are derived from the DFT workflow. The exact values of total energies and mechanical properties depend on the implementation, so tolerances are applied. The identification of stable structures is deterministic and checked by exact names.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "candidate_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B1N5-I": "float (energy in eV)",
          "B1N5-II": "float (energy in eV)",
          "B5N1-I": "float (energy in eV)",
          "B5N1-II": "float (energy in eV)",
          "B2N4-I": "float (energy in eV)",
          "B2N4-II": "float (energy in eV)",
          "B2N4-III": "float (energy in eV)",
          "B2N4-IV": "float (energy in eV)",
          "B4N2-I": "float (energy in eV)",
          "B4N2-II": "float (energy in eV)",
          "B4N2-III": "float (energy in eV)",
          "B4N2-IV": "float (energy in eV)",
          "B3N3-I": "float (energy in eV)",
          "B3N3-II": "float (energy in eV)",
          "B3N3-III": "float (energy in eV)"
        }
      },
      "description": "Relaxed total energies per unit cell for all 16 candidate pentagonal BxNy structures. The checker will compare energy differences between competing configurations for each stoichiometry (e.g., (B1N5-I - B1N5-II)) to hidden reference differences and verify that the lowest-energy structure per ratio matches the paper."
    },
    {
      "file": "phonon_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "B1N5-I": "object",
          "B5N1-II": "object",
          "B2N4-I": "object",
          "B4N2-I": "object",
          "B4N2-III": "object",
          "B4N2-IV": "object",
          "B3N3-I": "object"
        }
      },
      "description": "Phonon stability assessment for each tested structure, containing a boolean 'stable' flag or information about imaginary modes."
    },
    {
      "file": "stable_structures.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "pattern": "One stable structure name per line (e.g., B2N4-I)."
      },
      "description": "List of the dynamically stable pentagonal BxNy configurations expected to contain B2N4-I and B3N3-I."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "B2N4-I": {
            "biaxial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            },
            "X-axial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            },
            "Y-axial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            }
          },
          "B3N3-I": {
            "biaxial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            },
            "X-axial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            },
            "Y-axial": {
              "E_GPa": "float",
              "Y_N_m": "float",
              "tau_c_GPa": "float",
              "epsilon_c": "float"
            }
          }
        }
      },
      "description": "Computed 3D/2D Young's moduli, intrinsic strength, and fracture strain for B2N4-I and B3N3-I under biaxial and uniaxial strain. The checker will compare each value to paper‑reported references with relative tolerances (E, Y ±15%, τ_c ±20%, ε_c ±2pp absolute); a result that meets or exceeds the reference (i.e., within tolerance) earns full credit."
    },
    {
      "file": "band_gap_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_percent",
          "band_gap_eV",
          "band_type"
        ]
      },
      "description": "Band gap (eV) and direct/indirect character for B3N3-I under uniaxial tensile strain at each 1% strain step. The checker will verify that the band gap increases monotonically, the gap at 0% is near 0.06 eV and at 8% near 0.57 eV, and that band_type transitions from 'direct' to 'indirect' at a strain between 4% and 6%."
    }
  ],
  "notes": "All scored artifacts are derived from the DFT workflow. The exact values of total energies and mechanical properties depend on the implementation, so tolerances are applied. The identification of stable structures is deterministic and checked by exact names."
}
```

## How you are scored
A hidden verifier independently scores each of the five output artifacts listed in the output contract. The verifier compares your submitted files against a hidden gold standard derived from the original study, applying tolerances and structural checks appropriate for the nature of each quantity.

- **candidate_energies.json** – The energy differences between competing configurations within each stoichiometry are evaluated; the lowest-energy structure for each B:N ratio must be correctly identified.
- **phonon_summary.json** – The stability conclusions for the tested structures are compared to the expected set of dynamically stable monolayers.
- **stable_structures.txt** – The listed names are checked for exact match against the verified stable configurations.
- **mechanical_properties.json** – Each reported value (E, Y, τ_c, ε_c) for each structure and strain direction is compared to the reference with tolerances that account for differences in DFT implementation; better-than-reference performance is never penalized.
- **band_gap_strain.csv** – The verifier checks that the band gap increases monotonically with strain, that the gap at the endpoints lies within expected ranges, and that the band type transitions from direct to indirect at a strain consistent with the original report.

The five artifacts are assigned different weights reflecting their relative importance; the final reward is a weighted combination across all scored stages. Submitting a plausible-looking number without actually executing the full DFT pipeline will not satisfy the hidden checks.
