# Dynamical stability analysis of ZrF₂ daughter structures via DFT phonon mode-following

## Problem background
Radioactive decay of ⁹⁰SrF₂ (fluorite) stored in nuclear waste capsules produces ⁹⁰ZrF₂ as a daughter product. The structural and chemical transformation may compromise the waste form. The fluorite ZrF₂ structure is expected to be dynamically unstable; determining whether structurally related daughter phases are dynamically stable and which is lowest-energy is critical for assessing waste form integrity. This task uses density functional theory (DFT) and lattice dynamics to investigate the dynamical stability of ZrF₂ phases accessible from the fluorite parent via soft phonon modes.

## Approach
The core idea is to start from the fluorite ZrF₂ crystal (space group Fm-3m, lattice constant 5.425 Å) and follow the imaginary (unstable) phonon eigenvectors to discover daughter structures. Using an open-source DFT code and a phonon analysis toolkit, you will: (1) relax the parent fluorite structure and compute its full phonon dispersion to identify soft modes at specific high-symmetry points; (2) for each key imaginary mode, displace the atoms along the corresponding eigenvector, relax the distorted structure, and recompute its phonon spectrum; (3) classify each resulting daughter phase as dynamically stable (no imaginary frequencies) or unstable; (4) compute cohesive energies for the dynamically stable phases. The final deliverables are a stability classification map and the cohesive energy ordering of the stable daughters. This approach reproduces the central computational experiment of the original work.

## Reproduction target
Compute the dynamical stability (stable or unstable) of the five ZrF₂ daughter structures (m11, m14, m12, o70, t139) obtained by DFT phonon mode-following from fluorite ZrF₂. For phases found dynamically stable, compute their cohesive energies (eV per formula unit) and verify their relative energetic ordering. The final outputs are a JSON file mapping each daughter label to a boolean stability flag, and a JSON file containing the cohesive energies of the three stable phases. The target is to produce these values from first-principles calculations; the hidden checker will compare the reported booleans and energy ordering against expected results with appropriate numerical tolerances.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT relaxation and phonon of fluorite ZrF₂
- Role: process
- Action: Construct the fluorite ZrF₂ structure (space group Fm-3m, lattice constant 5.425 Å). Perform a DFT geometry relaxation, then compute the phonon dispersion using Phonopy. Identify the imaginary phonon modes at the X, W, and L points and record their eigenvectors.
- Evidence: `/app/outputs/fzr2_phonon_evidence.json`

### Step 2: Mode-following relaxations and phonon calculations
- Role: process
- Action: For each identified imaginary mode (doubly degenerate at X, lower band 1 and upper band 3 at W, doubly degenerate at L), displace the atoms along the corresponding eigenvector, relax the distorted structure with DFT, then compute the phonon spectrum of the relaxed daughter structure. Also compute the cohesive energy for each relaxed phase. Record all results (structures, phonon frequencies, cohesive energies) in a single evidence file.
- Evidence: `/app/outputs/mode_following_data.json`

### Step 3: Dynamical stability classification
- Role: scored (load-bearing)
- Action: From the results of step 2, determine for each daughter phase (m11, m14, m12, o70, t139) whether its phonon spectrum contains any imaginary modes. Write the boolean classification (true = stable, no imaginary modes; false = unstable) to dynamical_stability.json.
- Output file: `/app/outputs/dynamical_stability.json`
- Format: json
- Contract: {"m11": bool, "m14": bool, "m12": bool, "o70": bool, "t139": bool}
- Scoring: scored by hidden verifier

### Step 4: Cohesive energies of stable phases
- Role: scored
- Action: From the same results file, extract the cohesive energies (in eV/f.u.) of the three dynamically stable phases (m14, m12, o70). Write the energies to cohesive_energies.json.
- Output file: `/app/outputs/cohesive_energies.json`
- Format: json
- Contract: {"m14": float (eV/f.u.), "m12": float (eV/f.u.), "o70": float (eV/f.u.)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dynamical_stability.json`
- `/app/outputs/cohesive_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dynamical_stability.json
- path: `/app/outputs/dynamical_stability.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Boolean dynamical stability flags for the five daughter ZrF2 phases (true = no imaginary modes, stable).
- schema:
  - `type`: object
  - `required`:
    - `m11`: boolean
    - `m14`: boolean
    - `m12`: boolean
    - `o70`: boolean
    - `t139`: boolean

### cohesive_energies.json
- path: `/app/outputs/cohesive_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Cohesive energies (eV/f.u.) of the three dynamically stable ZrF2 phases. The energies should be negative and satisfy the inequality m12 < m14 < o70.
- schema:
  - `type`: object
  - `required`:
    - `m14`: float
    - `m12`: float
    - `o70`: float
  - `units`:
    - `m14`: eV/f.u.
    - `m12`: eV/f.u.
    - `o70`: eV/f.u.

Notes: The hidden checker will compare the booleans in dynamical_stability.json to the paper's known stability classification and check that cohesive_energies.json contains negative values ordered as m12 < m14 < o70, with tolerance for code-dependent variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dynamical_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "m11": "boolean",
          "m14": "boolean",
          "m12": "boolean",
          "o70": "boolean",
          "t139": "boolean"
        }
      },
      "description": "Boolean dynamical stability flags for the five daughter ZrF2 phases (true = no imaginary modes, stable)."
    },
    {
      "file": "cohesive_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "m14": "float",
          "m12": "float",
          "o70": "float"
        },
        "units": {
          "m14": "eV/f.u.",
          "m12": "eV/f.u.",
          "o70": "eV/f.u."
        }
      },
      "description": "Cohesive energies (eV/f.u.) of the three dynamically stable ZrF2 phases. The energies should be negative and satisfy the inequality m12 < m14 < o70."
    }
  ],
  "notes": "The hidden checker will compare the booleans in dynamical_stability.json to the paper's known stability classification and check that cohesive_energies.json contains negative values ordered as m12 < m14 < o70, with tolerance for code-dependent variations."
}
```

## How you are scored
A hidden verifier independently reads the two scored output files (`dynamical_stability.json` and `cohesive_energies.json`). For dynamical stability, it checks whether each boolean flag matches the correct classification for the five structures. For cohesive energies, it verifies that the reported energies are negative and satisfy the correct relative ordering among the stable phases (m12, m14, o70). The verifier does not require exact numerical agreement with any reference, but it expects the ordering and sign to be consistent with a valid DFT+phonon calculation. Each artifact contributes a weighted score; the combined reward reflects how well your reproduced results align with the hidden expectations. Note that simply guessing or fabricating numbers will not pass the ordering and consistency checks.
