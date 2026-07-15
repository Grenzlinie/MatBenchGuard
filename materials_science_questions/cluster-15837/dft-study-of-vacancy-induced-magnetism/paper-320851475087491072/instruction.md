# DFT Reproduction of Vacancy-Induced Ferromagnetism in Si-Mn Alloys

## Problem background
Non-stoichiometric Si_{1-x}Mn_x films with a slight excess of Mn (x ≈ 0.5) display dramatically different magnetic properties from stoichiometric MnSi, whose Curie temperature is only about 29 K. One proposed mechanism attributes the altered magnetism to silicon vacancies, which could create defects with localized magnetic moments whose indirect exchange enhances ferromagnetic ordering. First-principles electronic structure calculations can probe this hypothesis directly by modeling the vacancy defect supercell and computing the resulting magnetic moment distribution and electronic density of states — quantities that reveal whether the vacancy model can support strong localized magnetic moments and a half-metallic electronic structure.

## Approach
The computational investigation uses spin-polarized density functional theory (DFT) within the generalized gradient approximation (GGA), including spin-orbit coupling. A (2×2×2) supercell of the B20 MnSi crystal structure is constructed, and a specific number of Si atoms are removed from selected Wyckoff positions to model the off-stoichiometric composition near x ≈ 0.52. The defect supercell is first relaxed — both atomic positions and cell parameters are optimized — and then a self-consistent field calculation is performed with non-collinear magnetism to obtain the ground-state electronic structure. From the SCF output, two quantities are extracted: the average magnetic moment on the Mn atoms and the spin-polarized density of states around the Fermi level. The key physical question is whether silicon vacancies can give rise to substantial localized magnetic moments and whether the majority-spin channel develops a gap at the Fermi energy, characteristic of half-metallic behavior.

## Reproduction target
Construct a (2×2×2) supercell of the cubic B20 MnSi crystal, remove three Si atoms from Si-III Wyckoff positions to achieve a composition of approximately x ≈ 0.52, and perform a spin-polarized DFT geometry relaxation followed by a self-consistent field calculation with spin-orbit coupling. From the completed DFT run, produce two scored results: (1) the average magnetic moment per Mn atom (in μB) written as a single floating-point number to magnetic_moment.txt, and (2) the spin-polarized electronic density of states written to dos.dat as a three-column TSV file (energy in eV, majority-spin DOS, minority-spin DOS) spanning at least −2 to +2 eV relative to the Fermi level with at least 100 data points.

## Assets

- MnSi B20 crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Mn and Si (GGA with spin-orbit coupling): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct a (2×2×2) supercell of the B20 MnSi crystal structure and remove three Si atoms from specific Si-III Wyckoff positions to achieve a composition corresponding to x≈0.52.
- Evidence: `/app/outputs/supercell.pwi`

### Step 2: Geometry relaxation
- Role: process
- Action: Perform spin-polarized DFT geometry relaxation of the defect supercell using the GGA functional, optimizing both atomic positions and cell parameters.
- Evidence: `/app/outputs/relax.out`

### Step 3: Self-consistent field calculation with spin-orbit coupling
- Role: process
- Action: Run a spin-polarized self-consistent field (SCF) calculation on the relaxed structure using Quantum Espresso with spin-orbit coupling. Save the output file containing total energy, atomic magnetic moments, and the density of states data.
- Evidence: `/app/outputs/scf.out`

### Step 4: Extract average magnetic moment
- Role: scored (load-bearing)
- Action: Parse the SCF output to read the magnetic moment of each Mn atom. Compute the average magnetic moment per Mn atom (total moment / number of Mn atoms) and write the result as a single floating-point number to magnetic_moment.txt.
- Output file: `/app/outputs/magnetic_moment.txt`
- Format: txt
- Contract: A single line containing a decimal number (float) representing the average magnetic moment per Mn atom in units of Bohr magneton (μB). Example: 1.234
- Scoring: scored by hidden verifier

### Step 5: Extract spin-polarized density of states
- Role: scored
- Action: From the SCF output, extract the spin-polarized density of states (DOS) data: energy, majority-spin DOS, minority-spin DOS. Write the data to dos.dat as a TSV file with three columns. Ensure the energy grid covers at least -2 to +2 eV around the Fermi level (E=0).
- Output file: `/app/outputs/dos.dat`
- Format: tsv
- Contract: TSV file with three columns: energy (eV), majority-spin DOS (states/eV), minority-spin DOS (states/eV). The first line may be a header. Energy values are relative to the Fermi level (E=0). At least 100 data points spanning from -2 to +2 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moment.txt`
- `/app/outputs/dos.dat`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moment.txt
- path: `/app/outputs/magnetic_moment.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed average magnetic moment per Mn atom in the Si-vacancy supercell. Checked against the paper's DFT reported range.
- schema:
  - `type`: text
  - `units`:
    - `value`: μB

### dos.dat
- path: `/app/outputs/dos.dat`
- format: tsv
- purpose: scored
- target_policy: structural_audit
- description: Spin-polarized density of states. Checked for half-metallic gap in the majority-spin channel at the Fermi level.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `majority_dos`, `minority_dos`
  - `units`:
    - `energy`: eV
    - `majority_dos`: states/eV
    - `minority_dos`: states/eV

Notes: The DFT simulation stages (supercell, relaxation, SCF) are not directly scored but are required preconditions for the scored outputs. The average magnetic moment is compared to the paper's DFT range (1.1-1.5 μB) with tolerance. The DOS is checked for half-metallicity by verifying the majority-spin DOS near E_F is below a threshold and minority-spin DOS above a threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moment.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "units": {
          "value": "μB"
        }
      },
      "description": "Computed average magnetic moment per Mn atom in the Si-vacancy supercell. Checked against the paper's DFT reported range."
    },
    {
      "file": "dos.dat",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "majority_dos",
          "minority_dos"
        ],
        "units": {
          "energy": "eV",
          "majority_dos": "states/eV",
          "minority_dos": "states/eV"
        }
      },
      "description": "Spin-polarized density of states. Checked for half-metallic gap in the majority-spin channel at the Fermi level."
    }
  ],
  "notes": "The DFT simulation stages (supercell, relaxation, SCF) are not directly scored but are required preconditions for the scored outputs. The average magnetic moment is compared to the paper's DFT range (1.1-1.5 μB) with tolerance. The DOS is checked for half-metallicity by verifying the majority-spin DOS near E_F is below a threshold and minority-spin DOS above a threshold."
}
```

## How you are scored
A hidden verifier reads every scored artifact your workflow produces under /app/outputs and scores each one independently against a hidden reference derived from the published computational results. The average magnetic moment in magnetic_moment.txt is compared to a hidden acceptable range; the density-of-states file dos.dat is audited for the presence or absence of a gap in each spin channel at the Fermi level. Each scored stage carries a specific weight, and the final reward — a float between 0 and 1 — is the weighted sum across all scored stages. Reporting a plausible number without genuinely executing the DFT workflow steps will not suffice; the artifacts must be internally consistent with having come from a converged DFT simulation, and the verifier may cross-check structural properties of the outputs.
