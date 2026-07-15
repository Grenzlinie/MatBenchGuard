# Structural, elastic, electronic, and phonon properties of FeSi and CoSi in the B2 structure

## Problem background
The intermetallic compounds FeSi and CoSi in the B2 (CsCl) crystal structure are of interest for their potential applications in thermoelectrics, spintronics, and other areas. Their mechanical stability, electronic behavior, and vibrational properties are governed by the crystal structure and chemical bonding. First-principles calculations using density functional theory (DFT) and density functional perturbation theory (DFPT) can predict these properties. This task computes the equilibrium structural parameters, elastic constants, electronic density of states and orbital contributions, and phonon frequencies and stability for both FeSi and CoSi in the B2 phase, providing quantitative benchmarks for experimental and theoretical studies.

## Approach
The calculations are performed within the local density approximation (LDA) of DFT, using the Ceperley-Alder correlation as parametrized by Perdew-Zunger. The electronic ground state is obtained with plane-wave pseudopotential methods as implemented in the Quantum-ESPRESSO package. Norm-conserving LDA pseudopotentials are chosen for Fe, Co, and Si from the Quantum-ESPRESSO pseudopotential library. The workflow proceeds in four stages:\n\n(1) Equation of state: total-energy calculations at a series of unit-cell volumes are performed and fitted to the Murnaghan equation of state to extract the equilibrium lattice constant, bulk modulus, and its pressure derivative.\n\n(2) Elastic constants: using the equilibrium lattice constant, volume-conserving strains (orthorhombic and triaxial shear) are applied and the resulting energy-strain curves are fitted to quadratic forms to obtain C11, C12, and C44.\n\n(3) Electronic density of states: a self-consistent field calculation is followed by a non-self-consistent calculation on a dense k-point mesh to compute the total and atom-projected density of states; the total DOS at the Fermi level and the fractional contribution from the transition-metal 3d orbitals are extracted.\n\n(4) Phonon properties: dynamical matrices are computed on a q-point mesh using density functional perturbation theory, from which the phonon dispersion and density of states are obtained. The zone-centre transverse optical frequency and selected high-symmetry-point frequencies are extracted, and dynamical stability is assessed by checking that all phonon frequencies are positive.

## Reproduction target
For FeSi and CoSi in the B2 (CsCl) structure, compute and output the following quantities in the specified JSON files:\n\n- `step_01_equilibrium_properties.json`: equilibrium lattice constant a (Å), bulk modulus B (GPa), pressure derivative B'.\n- `step_02_elastic_constants.json`: independent elastic constants C11, C12, C44 (GPa).\n- `step_03_electronic_dos.json`: total electronic density of states at the Fermi level N(EF) (states/eV·cell) and the percentage contribution from the transition-metal 3d orbitals (Fe 3d% for FeSi, Co 3d% for CoSi).\n- `step_04_phonon_frequencies.json`: zone-centre transverse optical phonon frequency TO(Γ) (THz) for both compounds; for FeSi additionally the TA, LA, TO, LO frequencies at the X point and the acoustic (A) and optical (O) frequencies at the R point; and for both materials the boolean flag `all_positive` indicating whether all computed phonon modes are positive (dynamical stability).

## Assets

- Quantum‑ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotentials for Fe, Co, Si: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Equilibrium properties from Murnaghan equation of state fitting
- Role: scored
- Action: Perform total‑energy DFT calculations for FeSi and CoSi in the B2 (CsCl) structure at several volumes near equilibrium, fit the energies to the Murnaghan equation of state, and extract the equilibrium lattice constant a, bulk modulus B, and pressure derivative B'.
- Output file: `/app/outputs/step_01_equilibrium_properties.json`
- Format: json
- Contract: {"FeSi": {"a": float, "B": float, "Bprime": float}, "CoSi": {"a": float, "B": float, "Bprime": float}}
- Scoring: scored by hidden verifier

### Step 2: Elastic constants from volume‑conserving strains
- Role: scored
- Action: At the equilibrium lattice constants obtained in step_0, compute the three independent elastic constants C11, C12, C44 for each compound by applying volume‑conserving strains and fitting the total energy vs strain curves to quadratic forms.
- Output file: `/app/outputs/step_02_elastic_constants.json`
- Format: json
- Contract: {"FeSi": {"C11": float, "C12": float, "C44": float}, "CoSi": {"C11": float, "C12": float, "C44": float}}
- Scoring: scored by hidden verifier

### Step 3: Electronic density of states at the Fermi level
- Role: scored
- Action: Using the equilibrium structures, perform a self‑consistent field (SCF) calculation followed by a non‑SCF calculation on a dense k‑mesh to compute the total and atom‑projected density of states. Extract the total DOS at the Fermi level N(EF) and the percentage contribution from the transition‑metal 3d orbitals at EF.
- Output file: `/app/outputs/step_03_electronic_dos.json`
- Format: json
- Contract: {"FeSi": {"N_EF": float, "Fe_3d_percent": float}, "CoSi": {"N_EF": float, "Co_3d_percent": float}}
- Scoring: scored by hidden verifier

### Step 4: Phonon dispersion and zone‑centre frequencies
- Role: scored (load-bearing)
- Action: Using density functional perturbation theory with the equilibrium structures, compute dynamical matrices on a q‑point mesh and obtain the phonon dispersion and density of states. Extract the zone‑centre transverse optical phonon frequency (TO at Γ), the acoustic and optical frequencies at X and R for FeSi, and the TO frequency at Γ for CoSi. Verify that all computed phonon frequencies are positive and set the all_positive flag accordingly.
- Output file: `/app/outputs/step_04_phonon_frequencies.json`
- Format: json
- Contract: {"FeSi": {"TO_Gamma": float, "TA_X": float, "LA_X": float, "TO_X": float, "LO_X": float, "A_R": float, "O_R": float, "all_positive": bool}, "CoSi": {"TO_Gamma": float, "all_positive": bool}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_equilibrium_properties.json`
- `/app/outputs/step_02_elastic_constants.json`
- `/app/outputs/step_03_electronic_dos.json`
- `/app/outputs/step_04_phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_equilibrium_properties.json
- path: `/app/outputs/step_01_equilibrium_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constant a (Å), bulk modulus B (GPa), and pressure derivative B' for FeSi and CoSi in the B2 structure.
- schema:
  - `type`: object
  - `required`:
    - `FeSi`:
      - `a`: float
      - `B`: float
      - `Bprime`: float
    - `CoSi`:
      - `a`: float
      - `B`: float
      - `Bprime`: float

### step_02_elastic_constants.json
- path: `/app/outputs/step_02_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic constants C11, C12, C44 (GPa) for FeSi and CoSi in the B2 cubic phase.
- schema:
  - `type`: object
  - `required`:
    - `FeSi`:
      - `C11`: float
      - `C12`: float
      - `C44`: float
    - `CoSi`:
      - `C11`: float
      - `C12`: float
      - `C44`: float

### step_03_electronic_dos.json
- path: `/app/outputs/step_03_electronic_dos.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total electronic density of states at the Fermi level N(EF) (states/eV·cell) and transition‑metal 3d contribution (%) for FeSi and CoSi.
- schema:
  - `type`: object
  - `required`:
    - `FeSi`:
      - `N_EF`: float
      - `Fe_3d_percent`: float
    - `CoSi`:
      - `N_EF`: float
      - `Co_3d_percent`: float

### step_04_phonon_frequencies.json
- path: `/app/outputs/step_04_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Zone‑centre TO phonon frequency (THz), high‑symmetry‑point frequencies (THz) for FeSi, and all‑positive flags for dynamical stability.
- schema:
  - `type`: object
  - `required`:
    - `FeSi`:
      - `TO_Gamma`: float
      - `TA_X`: float
      - `LA_X`: float
      - `TO_X`: float
      - `LO_X`: float
      - `A_R`: float
      - `O_R`: float
      - `all_positive`: bool
    - `CoSi`:
      - `TO_Gamma`: float
      - `all_positive`: bool

Notes: All quantities are to be computed using LDA‑DFT and DFPT with Quantum‑ESPRESSO and the LDA pseudopotentials described in the resources. The checker compares each numeric value against the corresponding hidden paper‑reported value using an appropriate relative/absolute tolerance; meeting the tolerance earns full credit. The all_positive flags must be true for both materials.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_equilibrium_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "FeSi": {
            "a": "float",
            "B": "float",
            "Bprime": "float"
          },
          "CoSi": {
            "a": "float",
            "B": "float",
            "Bprime": "float"
          }
        }
      },
      "description": "Equilibrium lattice constant a (Å), bulk modulus B (GPa), and pressure derivative B' for FeSi and CoSi in the B2 structure."
    },
    {
      "file": "step_02_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "FeSi": {
            "C11": "float",
            "C12": "float",
            "C44": "float"
          },
          "CoSi": {
            "C11": "float",
            "C12": "float",
            "C44": "float"
          }
        }
      },
      "description": "Elastic constants C11, C12, C44 (GPa) for FeSi and CoSi in the B2 cubic phase."
    },
    {
      "file": "step_03_electronic_dos.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "FeSi": {
            "N_EF": "float",
            "Fe_3d_percent": "float"
          },
          "CoSi": {
            "N_EF": "float",
            "Co_3d_percent": "float"
          }
        }
      },
      "description": "Total electronic density of states at the Fermi level N(EF) (states/eV·cell) and transition‑metal 3d contribution (%) for FeSi and CoSi."
    },
    {
      "file": "step_04_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "FeSi": {
            "TO_Gamma": "float",
            "TA_X": "float",
            "LA_X": "float",
            "TO_X": "float",
            "LO_X": "float",
            "A_R": "float",
            "O_R": "float",
            "all_positive": "bool"
          },
          "CoSi": {
            "TO_Gamma": "float",
            "all_positive": "bool"
          }
        }
      },
      "description": "Zone‑centre TO phonon frequency (THz), high‑symmetry‑point frequencies (THz) for FeSi, and all‑positive flags for dynamical stability."
    }
  ],
  "notes": "All quantities are to be computed using LDA‑DFT and DFPT with Quantum‑ESPRESSO and the LDA pseudopotentials described in the resources. The checker compares each numeric value against the corresponding hidden paper‑reported value using an appropriate relative/absolute tolerance; meeting the tolerance earns full credit. The all_positive flags must be true for both materials."
}
```

## How you are scored
Each output JSON file will be examined by an automated verifier. The verifier compares your reported numeric results against reference values using appropriate tolerances. For each file, the verifier checks the agreement of each required field; fields that meet the tolerance earn full credit for that item, and the file score is the fraction of items passing. The final reward is a weighted average of the file scores. In addition to the numerical checks, the verifier confirms that the `all_positive` flags in the phonon output are true. The verifier does not inspect or grade the intermediate calculations; only the content of the output files matters.
