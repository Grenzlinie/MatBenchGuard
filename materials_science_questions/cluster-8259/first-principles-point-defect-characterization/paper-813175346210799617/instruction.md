# Hybrid DFT reproduction of H and O₂ impurity deep trap states in metal phthalocyanine crystals

## Problem background
Metal phthalocyanines (MPcs) are promising organic semiconductors for light‑conversion and flexible electronics. Their performance is known to be sensitive to ambient impurities, especially hydrogen and oxygen. Understanding how H adatoms and intercalated O₂ molecules introduce deep carrier‑trap states in the band gap is critical for improving device stability. This task reproduces hybrid‑DFT calculations that quantify the positions of impurity‑induced trap states and the associated changes in magnetic moments for zinc (ZnPc) and copper (CuPc) phthalocyanine crystals.

## Approach
We use spin‑polarized density‑functional theory with a hybrid functional (PBE0) to study the β‑phase primitive unit cells of ZnPc and CuPc, each containing two molecules. A single H adatom is placed on a pyridinic N site (giving a high, 50% defect concentration), and a single O₂ molecule is intercalated between the molecular layers. For each pristine and impurity‑doped structure, we relax the atomic positions and then compute the density of states (DOS). From the pristine DOS we determine the valence‑band maximum (VBM) and conduction‑band minimum (CBM); from the impurity DOS we locate the impurity‑related gap peak and measure its energy relative to the appropriate band edge. The total magnetic moment of the H‑doped cells is obtained from the spin‑polarized charge density. The required crystal structures are taken from the published literature (β‑polymorph of ZnPc and CuPc) and any open‑source DFT code supporting hybrid functionals and PAW pseudopotentials can be used.

## Reproduction target
Using hybrid‑DFT (PBE0) on the β‑phase primitive unit cells of ZnPc and CuPc, produce the following quantities for a single impurity per cell (50% defective concentration):
- Pristine band gaps of ZnPc and CuPc (eV).
- H‑induced deep trap state energy (eV above the VBM) for ZnPc and CuPc.
- O₂‑induced trap state energy (eV below the CBM) for ZnPc and CuPc.
- Magnetic moment (μB) of the H‑doped ZnPc and CuPc systems.
All energies in eV, magnetic moments in μB; the VBM is set to 0 for each system. Write results to `/app/outputs/results.json`.

## Assets

- β‑phase ZnPc crystal structure (lattice parameters, atomic coordinates): 10.1039/DT9790000676
- β‑phase CuPc crystal structure (lattice parameters, atomic coordinates): 10.1039/DT9790000676
- PAW pseudopotentials for Zn, Cu, C, N, H, O: https://www.quantum-espresso.org/pseudopotentials
- Open‑source DFT code with hybrid functional support (e.g., Quantum ESPRESSO ≥ 7.2): https://www.quantum-espresso.org/download

## Workflow steps

### Step 1: Prepare and relax pristine crystal structures
- Role: process
- Action: Construct the primitive unit cells of β‑phase ZnPc and CuPc (two molecules per cell) from the published crystallographic data. Perform spin‑polarized DFT relaxation of atomic positions using a hybrid functional (PBE0) and a plane‑wave basis. Retain the relaxed structures.
- Evidence: `/app/outputs/pristine_relax.log`

### Step 2: Introduce H impurity on pyridinic N and relax
- Role: process
- Action: For both ZnPc and CuPc primitive cells, place a single H adatom on a pyridinic N site (one impurity per cell, 50% defective concentration). Relax the ionic positions with the same hybrid functional and plane‑wave cutoff as in step 1. Save the relaxed structures.
- Evidence: `/app/outputs/H_relaxation.log`

### Step 3: Introduce intercalated O₂ impurity and relax
- Role: process
- Action: For both ZnPc and CuPc primitive cells, insert an O₂ molecule in the interlayer space (one O₂ per cell). Relax the ionic positions using the same hybrid functional settings as before. Save the relaxed structures.
- Evidence: `/app/outputs/O2_relaxation.log`

### Step 4: Compute PBE0 DOS and extract target quantities
- Role: scored (load-bearing)
- Action: Using the relaxed structures from steps 1–3, run spin‑polarized PBE0 density‑of‑states (DOS) calculations for the pristine, H‑doped, and O₂‑doped systems of ZnPc and CuPc. Determine the valence‑band maximum (VBM) and conduction‑band minimum (CBM) from the pristine DOS. Locate the H‑related gap peak and measure its energy relative to the VBM; locate the O₂‑related gap peak and measure its energy relative to the CBM. Compute the total magnetic moment of the H‑doped cells from the spin‑polarized charge density. Write all results to /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"pristine_gaps": {"ZnPc": <float>, "CuPc": <float>}, "H_trap_energy": {"ZnPc": <float>, "CuPc": <float>}, "O2_trap_energy": {"ZnPc": <float>, "CuPc": <float>}, "magnetic_moments": {"H_ZnPc": <float>, "H_CuPc": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All four target quantity groups as floats. VBM is set to 0 for each system. The checker compares each field to the paper‑reported reference values with a tolerance of 0.1 eV for energies and 0.2 μB for magnetic moments, and applies a threshold check for magnetic moments (≥ expected value).
- schema:
  - `type`: object
  - `required`:
    - `pristine_gaps`: object with keys ZnPc and CuPc (each a float, units eV)
    - `H_trap_energy`: object with keys ZnPc and CuPc (each a float, units eV, measured from VBM)
    - `O2_trap_energy`: object with keys ZnPc and CuPc (each a float, units eV, measured from CBM)
    - `magnetic_moments`: object with keys H_ZnPc and H_CuPc (each a float, units μB)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `pristine_gaps.ZnPc`: eV
    - `pristine_gaps.CuPc`: eV
    - `H_trap_energy.ZnPc`: eV
    - `H_trap_energy.CuPc`: eV
    - `O2_trap_energy.ZnPc`: eV
    - `O2_trap_energy.CuPc`: eV
    - `magnetic_moments.H_ZnPc`: μB
    - `magnetic_moments.H_CuPc`: μB

Notes: The checker recomputes nothing; it directly reads the reported numbers and compares against the hidden reference. This is an acceptable T0 result‑level comparison because recomputing from raw DOS data is not feasible in the verifier sandbox.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine_gaps": "object with keys ZnPc and CuPc (each a float, units eV)",
          "H_trap_energy": "object with keys ZnPc and CuPc (each a float, units eV, measured from VBM)",
          "O2_trap_energy": "object with keys ZnPc and CuPc (each a float, units eV, measured from CBM)",
          "magnetic_moments": "object with keys H_ZnPc and H_CuPc (each a float, units μB)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "pristine_gaps.ZnPc": "eV",
          "pristine_gaps.CuPc": "eV",
          "H_trap_energy.ZnPc": "eV",
          "H_trap_energy.CuPc": "eV",
          "O2_trap_energy.ZnPc": "eV",
          "O2_trap_energy.CuPc": "eV",
          "magnetic_moments.H_ZnPc": "μB",
          "magnetic_moments.H_CuPc": "μB"
        }
      },
      "description": "All four target quantity groups as floats. VBM is set to 0 for each system. The checker compares each field to the paper‑reported reference values with a tolerance of 0.1 eV for energies and 0.2 μB for magnetic moments, and applies a threshold check for magnetic moments (≥ expected value)."
    }
  ],
  "notes": "The checker recomputes nothing; it directly reads the reported numbers and compares against the hidden reference. This is an acceptable T0 result‑level comparison because recomputing from raw DOS data is not feasible in the verifier sandbox."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/results.json` and compares each numeric field to a hidden reference. For directional quantities (band gaps, trap depths) a threshold‑or‑better policy is applied: meeting or exceeding the reference earns full credit, and the score degrades only as the result gets worse. The magnetic moments are checked against minimum expected values using the same threshold‑or‑better logic. The verifier uses tolerances that account for the expected spread between different DFT implementations, so a correct re‑run with similar but not identical settings can still achieve high scores. The final reward is a weighted sum of the individual comparisons; simply printing a number is not enough—the entire workflow must be executed and the required evidence artifacts must be present.
