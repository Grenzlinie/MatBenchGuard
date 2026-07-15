# DFT spin-state and electronic structure analysis of Fe complexes

## Problem background
The electronic structure and spin state energetics of an iron-nitrosyl {FeNO}8 complex influence its reactivity. This task targets the computational determination of the ground-state spin and key vibrational property of the complex [Fe(NO)(N3PyS)]. By computing the relative energies of the singlet (S=0) and triplet (S=1) states, as well as the N–O stretching frequency of the triplet state, one can assess whether the complex prefers a high-spin configuration and how the nitrosyl ligand is activated. The result provides insight into the relationship between spin state and electronic structure for this class of nonheme iron complexes.

## Approach
Density functional theory (DFT) calculations are performed to compare the singlet and triplet spin states of [Fe(NO)(N3PyS)]. Starting from provided initial guess coordinates, geometry optimizations are carried out for both spin states using a GGA functional with dispersion correction. A mixed basis set is employed: triple-zeta quality for the heavy atoms (Fe, S, N, O) and double-zeta for C and H. After optimization, analytical harmonic frequency calculations yield the N–O stretching mode. Single-point energies are then recomputed on the optimized geometries using a hybrid functional with a triple-zeta basis set on all atoms. The singlet–triplet energy difference is obtained from these single-point energies. The protocol is implemented in a quantum chemistry package such as ORCA or PySCF.

## Reproduction target
Compute the N–O stretching frequency (cm⁻¹) of the triplet state and the energy difference (kcal/mol) between the singlet and triplet states of [Fe(NO)(N3PyS)]. The triplet state is optimized from a linear initial guess (IGA) and the singlet state from a bent initial guess (IGB). Write the optimized triplet geometry to `optimized_triplet.xyz`, the optimized singlet geometry to `optimized_singlet.xyz`, and a JSON file `results.json` containing two numbers: `v_no_triplet_cm-1` and `relative_energy_kcal_per_mol`. The latter is defined as E(singlet) − E(triplet) at the hybrid functional level.

## Assets

- Initial guess coordinates for DFT optimization
- ORCA: https://orcaforum.kofo.mpg.de
- PySCF: pyscf
- Basis set exchange: https://www.basissetexchange.org/

## Workflow steps

### Step 1: Triplet geometry optimization and frequency analysis
- Role: scored
- Action: Perform DFT geometry optimization of the {FeNO}8 complex [Fe(NO)(N3PyS)] in the triplet (S=1) spin state using BP86 functional with D3 dispersion, def2-TZVP basis for Fe,S,N,O and def2-SVP for C,H, RI approximation. Start from the IGA (linear) initial guess from /app/inputs/initial_guesses.xyz. Compute analytical harmonic frequencies and extract the N-O stretching mode frequency. Write the optimized geometry to the output file.
- Output file: `/app/outputs/optimized_triplet.xyz`
- Format: other
- Contract: Standard XYZ format with 58 atoms; atomic symbols and coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 2: Singlet geometry optimization and frequency analysis
- Role: scored
- Action: Perform DFT geometry optimization of the {FeNO}8 complex in the singlet (S=0) spin state using the same BP86/D3/def2 basis set protocol, starting from a bent initial guess (e.g., IGB from /app/inputs/initial_guesses.xyz). Compute analytical harmonic frequencies to confirm the stationary point. Write the optimized geometry to the output file.
- Output file: `/app/outputs/optimized_singlet.xyz`
- Format: other
- Contract: Standard XYZ format with 58 atoms; atomic symbols and coordinates in Angstrom.
- Scoring: scored by hidden verifier

### Step 3: Compute relative energy and compile results
- Role: scored (load-bearing)
- Action: Using the optimized geometries from Step 1 and Step 2, perform B3LYP single-point energy calculations with def2-TZVP basis on all atoms. Extract the N-O stretching frequency from the triplet harmonic frequency calculation (or recompute if needed). Compute the relative energy as E(singlet) - E(triplet) and convert to kcal/mol. Write results.json containing v_no_triplet_cm-1 and relative_energy_kcal_per_mol.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"v_no_triplet_cm-1": <float>, "relative_energy_kcal_per_mol": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_triplet.xyz`
- `/app/outputs/optimized_singlet.xyz`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_triplet.xyz
- path: `/app/outputs/optimized_triplet.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Optimized geometry of the triplet state of the {FeNO}8 complex. Verified by structural audit (existence, 58 atoms, Fe-N-O angle in plausible range).
- schema:
  - `type`: other
  - `description`: XYZ file containing 58 atoms with atomic symbols and coordinates in Angstrom.

### optimized_singlet.xyz
- path: `/app/outputs/optimized_singlet.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Optimized geometry of the singlet state of the {FeNO}8 complex. Verified by structural audit (existence, 58 atoms, Fe-N-O angle in plausible range).
- schema:
  - `type`: other
  - `description`: XYZ file containing 58 atoms with atomic symbols and coordinates in Angstrom.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed N-O stretching frequency (cm⁻¹) of the triplet state and the singlet-triplet energy difference (kcal/mol) from B3LYP single-point calculations.
- schema:
  - `type`: object
  - `required`:
    - `v_no_triplet_cm-1`: float
    - `relative_energy_kcal_per_mol`: float

Notes: The key scored artifacts are the vibrational frequency and energy difference; geometry files are scored only for structural sanity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_triplet.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "XYZ file containing 58 atoms with atomic symbols and coordinates in Angstrom."
      },
      "description": "Optimized geometry of the triplet state of the {FeNO}8 complex. Verified by structural audit (existence, 58 atoms, Fe-N-O angle in plausible range)."
    },
    {
      "file": "optimized_singlet.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "description": "XYZ file containing 58 atoms with atomic symbols and coordinates in Angstrom."
      },
      "description": "Optimized geometry of the singlet state of the {FeNO}8 complex. Verified by structural audit (existence, 58 atoms, Fe-N-O angle in plausible range)."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "v_no_triplet_cm-1": "float",
          "relative_energy_kcal_per_mol": "float"
        }
      },
      "description": "Computed N-O stretching frequency (cm⁻¹) of the triplet state and the singlet-triplet energy difference (kcal/mol) from B3LYP single-point calculations."
    }
  ],
  "notes": "The key scored artifacts are the vibrational frequency and energy difference; geometry files are scored only for structural sanity."
}
```

## How you are scored
A hidden verifier independently scores each of the three output artifacts and combines them by weight into a final reward (0–1). The scoring works as follows:
- `optimized_triplet.xyz` and `optimized_singlet.xyz` are checked by structural audit: the file must exist, contain exactly 58 atoms, and have a plausible Fe–N–O angle range.
- `results.json` is checked by reference match: the verifier compares your computed `v_no_triplet_cm-1` and `relative_energy_kcal_per_mol` to hidden reference values. Both must fall within an allowed range.
Reporting the paper's numbers without actually running the workflow will not pass, because the verifier checks the file contents and the computed quantities against its own criteria. The exact reference values and tolerance ranges are hidden and are not needed to attempt the task.
