# Lattice Constants and Metallicity of Cubic TCNE and Its Alkali-Metal Insertion Compounds

## Problem background
Tetracyanoethylene (TCNE) forms a cubic molecular crystal (space group Im3) whose structure contains large, empty cavities. Insertion of alkali-metal atoms (such as sodium or potassium) into these cavities could lead to charge transfer, a change in the unit cell dimensions, and possibly a transition from insulating to metallic electronic behaviour. Understanding whether the lattice contracts and whether the density of states at the Fermi level becomes non‑zero is the central question of this computational study. It provides a rigorous test of periodic Hartree–Fock methods applied to molecular crystals.

## Approach
We use periodic Hartree–Fock (HF) theory implemented in CP2K, an open‑source quantum‑chemistry code. The starting point is the experimentally known cubic TCNE crystal structure (space group Im3, three mutually perpendicular molecules per primitive cell). We perform variable‑cell geometry optimisations for three systems: pure TCNE, K(TCNE)₃, and Na(TCNE)₃. In the insertion compounds the alkali atom sits at the cavity centre, preserving the Im3 symmetry. All calculations employ the 6‑31G* basis set for C, N, and Na, and a modified 6‑31G* basis for K. After optimisation, a static HF calculation is run on the optimised geometry to obtain the electronic band energies and the density of states (DOS). From the DOS we decide whether the Fermi level lies in a non‑zero density (metallic) or in a gap (insulating). The key outputs are the optimised cell parameter a and the metallicity verdict for each compound.

## Reproduction target
Determine the optimised lattice parameter a (in Å) for pure TCNE, K(TCNE)₃, and Na(TCNE)₃ using periodic Hartree‑Fock. For each compound, also determine whether the density of states at the Fermi level is non‑zero. The results must be written to two JSON files under /app/outputs (see Workflow steps for the exact format).

## Assets

- CP2K: https://www.cp2k.org/
- Basis sets (6‑31G* for C,N,Na; modified 6‑31G* for K): https://www.basissetexchange.org/
- Cubic TCNE crystal structure

## Workflow steps

### Step 1: Optimize pure cubic TCNE and compute DOS
- Role: process
- Action: Using CP2K, perform a variable-cell Hartree-Fock geometry optimization for pure cubic TCNE (space group Im3, three molecules per cell) starting from the experimental structure (a = 9.736 Å) with the following molecular internal coordinates: C−C single bond = 1.433 Å, C=C double bond = 1.357 Å, C≡N triple bond = 1.166 Å, in‑plane C−C−C angle = 116.2°, in‑plane C−C≡N angle = 178.1°. Use the 6‑31G* basis set for C and N. After optimization, run a static HF calculation on the optimized geometry to obtain band energies and density of states (DOS). Save the optimization output and the DOS data.
- Evidence: `/app/outputs/pure_tcne_opt_and_dos.log`

### Step 2: Optimize K(TCNE)₃ crystal and compute DOS
- Role: process
- Action: Perform a variable-cell HF geometry optimization for K(TCNE)₃ (K atom placed at the cavity center, space group Im3 maintained). Use the same optimized TCNE molecular geometry and 6‑31G* basis for C,N, and the modified 6‑31G* basis for K (Ricart et al. 1995). Optimize the cell parameter. Then perform a static HF calculation on the optimized geometry to obtain band energies and DOS. Save outputs.
- Evidence: `/app/outputs/k_tcne3_opt_and_dos.log`

### Step 3: Optimize Na(TCNE)₃ crystal and compute DOS
- Role: process
- Action: Perform a variable-cell HF geometry optimization for Na(TCNE)₃ (Na atom at cavity center). Use the 6‑31G* basis for C,N,Na. Optimize the cell parameter. Then run a static HF calculation on the optimized geometry to obtain band energies and DOS. Save outputs.
- Evidence: `/app/outputs/na_tcne3_opt_and_dos.log`

### Step 4: Extract optimized lattice constants
- Role: scored (load-bearing)
- Action: From the optimization output of steps process_01–03, extract the optimized cell parameter a (in Å) for each compound. Write a JSON file with keys "pure_TCNE", "K_TCNE3", "Na_TCNE3" mapping to the respective float values.
- Output file: `/app/outputs/optimized_lattice_constants.json`
- Format: json
- Contract: {"pure_TCNE": "float", "K_TCNE3": "float", "Na_TCNE3": "float"}
- Scoring: scored by hidden verifier

### Step 5: Determine metallicity
- Role: scored
- Action: From the electronic structure outputs of steps process_01–03, determine whether the density of states at the Fermi level is greater than zero for each compound. Write a JSON file with keys "pure_TCNE", "K_TCNE3", "Na_TCNE3" mapping to booleans (true if DOS(EF) > 0, else false).
- Output file: `/app/outputs/metallicity.json`
- Format: json
- Contract: {"pure_TCNE": "boolean", "K_TCNE3": "boolean", "Na_TCNE3": "boolean"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lattice_constants.json`
- `/app/outputs/metallicity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lattice_constants.json
- path: `/app/outputs/optimized_lattice_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized cell parameters from Hartree-Fock calculations for pure TCNE, K(TCNE)3, and Na(TCNE)3.
- schema:
  - `type`: object
  - `required`:
    - `pure_TCNE`: float
    - `K_TCNE3`: float
    - `Na_TCNE3`: float
  - `units`:
    - `pure_TCNE`: angstrom
    - `K_TCNE3`: angstrom
    - `Na_TCNE3`: angstrom

### metallicity.json
- path: `/app/outputs/metallicity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Boolean indicators of whether the density of states at the Fermi level is non-zero for each compound.
- schema:
  - `type`: object
  - `required`:
    - `pure_TCNE`: boolean
    - `K_TCNE3`: boolean
    - `Na_TCNE3`: boolean

Notes: The checker validates the output files against hidden reference values. Lattice constants are compared within a tolerance; metallicity booleans are compared exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lattice_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pure_TCNE": "float",
          "K_TCNE3": "float",
          "Na_TCNE3": "float"
        },
        "units": {
          "pure_TCNE": "angstrom",
          "K_TCNE3": "angstrom",
          "Na_TCNE3": "angstrom"
        }
      },
      "description": "Optimized cell parameters from Hartree-Fock calculations for pure TCNE, K(TCNE)3, and Na(TCNE)3."
    },
    {
      "file": "metallicity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pure_TCNE": "boolean",
          "K_TCNE3": "boolean",
          "Na_TCNE3": "boolean"
        }
      },
      "description": "Boolean indicators of whether the density of states at the Fermi level is non-zero for each compound."
    }
  ],
  "notes": "The checker validates the output files against hidden reference values. Lattice constants are compared within a tolerance; metallicity booleans are compared exactly."
}
```

## How you are scored
A hidden verifier checks the contents of `optimized_lattice_constants.json` and `metallicity.json`. The lattice constants are compared to a hidden reference with a tolerance that accounts for differences in implementation and numerical settings; the metallicity booleans are compared exactly. Both files must be produced by running the workflow described above. Self‑reporting numbers without executing the Hartree‑Fock calculations will not pass.
