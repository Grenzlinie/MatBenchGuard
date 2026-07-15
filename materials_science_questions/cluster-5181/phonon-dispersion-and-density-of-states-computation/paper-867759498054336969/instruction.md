# MgB2 electronic density of states and zone‑center phonon frequencies

## Problem background
Magnesium diboride (MgB₂) is a superconductor with a remarkably high critical temperature for a simple intermetallic compound. It crystallises in the hexagonal AlB₂-type structure (space group P6/mmm), with graphitic boron planes separated by magnesium layers. The low-energy electronic states that form the Fermi surface arise primarily from the boron 2p orbitals, and a central question is the balance between two-dimensional σ-bonding states and three-dimensional π-bonding states at the Fermi level. First-principles calculations can resolve these orbital contributions and also provide the zone‑center vibrational frequencies, which are a direct experimental observable. This task reproduces the key electronic and vibrational properties of pristine MgB₂ using density‑functional theory, quantifying the total electronic density of states at the Fermi energy and the B‑pz character, as well as the four independent Γ‑point phonon frequencies.

## Approach
The reproduction uses the local density approximation (LDA) of density‑functional theory, as implemented in open‑source plane‑wave pseudopotential or all‑electron codes. Starting from the experimental lattice constants (a=3.083 Å, c=3.52 Å, space group P6/mmm), a self‑consistent field calculation is performed to obtain the converged ground‑state charge density and Kohn‑Sham eigenvalues. From this converged density, the total electronic density of states and the orbitally‑projected partial density of states (PDOS) are computed on a dense energy grid, decomposing the boron contribution into in‑plane (px+py, σ) and out‑of‑plane (pz, π) components. Separately, density‑functional perturbation theory (linear response) is applied at the Γ point to construct the dynamical matrix and extract the phonon eigenfrequencies for the four distinct zone‑centre modes. The choice of computational parameters (plane‑wave cutoff, k‑point density, smearing) is left to the agent, provided they are sufficient for well‑converged results. The only required inputs are the crystal structure and standard LDA pseudopotentials (or an all‑electron basis) for magnesium and boron.

## Reproduction target
Produce two scored artifacts from the LDA‑DFT workflow applied to MgB₂:

1. A tab‑separated file `pdos.dat` containing the energy (eV), total DOS (states/eV per cell), and the B‑pz partial DOS on a uniform grid with step ≤ 0.01 eV, covering at least the energy window [‑10, 10] eV relative to the Fermi level.
2. A JSON file `phonon_frequencies.json` that lists the Γ‑point phonon frequencies (in cm⁻¹) for the symmetry‑labelled modes E₁u, A₂u, E₂g and B₁g, with degenerate modes given as arrays of length 2.

The checker will recompute the total DOS at the Fermi level and the fraction of B‑pz character from the submitted PDOS, and will compare the reported phonon frequencies against hidden reference values.

## Assets

- ABINIT DFT code: https://www.abinit.org/download
- Troullier‑Martins LDA pseudopotentials for Mg and B: https://www.pseudo-dojo.org/
- MgB2 crystal structure (experimental lattice parameters): 10.1103/PhysRevB.63.220504

## Workflow steps

### Step 1: Self-consistent LDA-DFT calculation for MgB2
- Role: process
- Action: Set up the hexagonal MgB2 crystal (a=3.083 Å, c=3.52 Å, space group P6/mmm) and perform a self-consistent field (SCF) LDA-DFT calculation using a plane‑wave or all‑electron code to obtain the converged charge density and Kohn‑Sham eigenvalues. Use an appropriate k‑point mesh and energy cutoff, with Gaussian smearing. The SCF convergence should be tight enough for subsequent density‑of‑states and phonon calculations.
- Evidence: `/app/outputs/scf_output.log`

### Step 2: Total and partial density of states (PDOS) for MgB2
- Role: scored (load-bearing)
- Action: From the SCF results, compute the total electronic density of states and the orbitally decomposed partial density of states (PDOS) projected onto Mg‑s, Mg‑p, B‑s, B‑pz, and B‑px+py (σ) states. The energy range must cover at least −10 to 10 eV relative to the Fermi level, with an energy step no larger than 0.01 eV. Write a tab‑separated file containing energy and the decomposition columns.
- Output file: `/app/outputs/pdos.dat`
- Format: tsv
- Contract: A TSV file with a header line. Required columns: energy (eV), total_DOS (states/eV per cell), B_pz. Optional columns: B_s, B_px+py_sigma, Mg_s, Mg_p. The Fermi level is at energy=0.0 eV. The data must be provided on a uniform energy grid with step ≤ 0.01 eV.
- Scoring: scored by hidden verifier

### Step 3: Zone‑center phonon frequencies for MgB2
- Role: scored (load-bearing)
- Action: Using density functional perturbation theory (linear response) on top of the SCF charge density, compute the dynamical matrix at the Γ point for MgB2 and obtain the phonon eigenfrequencies for the E1u, A2u, E2g, and B1g modes. Use the same LDA functional and a comparable plane‑wave cutoff and k‑point mesh as the SCF step. Write the frequencies to a JSON file.
- Output file: `/app/outputs/phonon_frequencies.json`
- Format: json
- Contract: JSON object with keys 'E1u', 'A2u', 'E2g', 'B1g'. Values are arrays: 'E1u': [freq, freq], 'A2u': [freq], 'E2g': [freq, freq], 'B1g': [freq]. Frequencies are floating‑point numbers in cm⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pdos.dat`
- `/app/outputs/phonon_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pdos.dat
- path: `/app/outputs/pdos.dat`
- format: tsv
- purpose: scored
- target_policy: metric_recompute
- description: MgB2 projected density of states
- schema:
  - `required_columns`: `energy`, `total_DOS`, `B_pz`
  - `optional_columns`: `B_s`, `B_px+py_sigma`, `Mg_s`, `Mg_p`
  - `type`: table
  - `units`:
    - `energy`: eV
    - `total_DOS`: states/eV per cell
    - `B_pz`: states/eV per cell

### phonon_frequencies.json
- path: `/app/outputs/phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gamma‑point phonon frequencies for MgB2
- schema:
  - `type`: object
  - `required`: `E1u`, `A2u`, `E2g`, `B1g`
  - `properties`:
    - `A2u`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 1
      - `maxItems`: 1
    - `B1g`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 1
      - `maxItems`: 1
    - `E1u`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2
    - `E2g`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 2
      - `maxItems`: 2

Notes: Task targets only MgB2; other compounds studied in the paper are excluded per the approved scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pdos.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "energy",
          "total_DOS",
          "B_pz"
        ],
        "optional_columns": [
          "B_s",
          "B_px+py_sigma",
          "Mg_s",
          "Mg_p"
        ],
        "type": "table",
        "units": {
          "energy": "eV",
          "total_DOS": "states/eV per cell",
          "B_pz": "states/eV per cell"
        }
      },
      "description": "MgB2 projected density of states"
    },
    {
      "file": "phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "E1u",
          "A2u",
          "E2g",
          "B1g"
        ],
        "properties": {
          "A2u": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 1,
            "maxItems": 1
          },
          "B1g": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 1,
            "maxItems": 1
          },
          "E1u": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2
          },
          "E2g": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 2,
            "maxItems": 2
          }
        }
      },
      "description": "Gamma‑point phonon frequencies for MgB2"
    }
  ],
  "notes": "Task targets only MgB2; other compounds studied in the paper are excluded per the approved scope."
}
```

## How you are scored
The hidden verifier evaluates both scored artifacts independently and combines their scores with equal weight (0.5 each) to produce a final reward in [0, 1].

For `pdos.dat`, the verifier reads the table, identifies the row at the Fermi level (energy = 0 eV), recomputes the total DOS and the B‑pz fraction (B‑pz / total DOS). It verifies that the B‑pz fraction is less than 0.5 (a structural consistency requirement) and compares the total DOS to a hidden reference.

For `phonon_frequencies.json`, the verifier checks the JSON structure, extracts the average frequency for each degenerate mode, and compares each mode’s frequency to hidden reference values, assigning credit based on proximity.

The process‑step evidence (`scf_output.log`) is not directly scored, but the SCF calculation is mandatory to produce the two scored artifacts. The final reward reflects how well the two generated outputs match the expected physical results, not whether the numbers exactly reproduce a particular published table.
