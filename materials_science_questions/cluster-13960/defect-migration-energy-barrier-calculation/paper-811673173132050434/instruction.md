# Chromium Migration Barriers on Gamma and Eta Alumina via DFT-NEB

## Problem background
γ-alumina and η-alumina are widely used catalytic support materials. In chromia/alumina catalysts, the deactivation is linked to chromium atoms migrating from the surface into the bulk. Experimental evidence shows that under identical conditions, the catalyst supported on γ‑alumina degrades much faster than the one on η‑alumina. Understanding the atomic‑scale mechanism requires quantifying the energetic barriers that control this migration. This task aims to compute the activation barriers for a single Cr atom moving from the reactive surface site into a subsurface octahedral interstitial on the (110C) surfaces of both γ‑ and η‑alumina.

## Approach
We use first‑principles density‑functional theory (DFT) with the generalized‑gradient approximation (GGA) for exchange‑correlation and plane‑wave pseudopotentials. Periodic slab models of γ‑Al₂O₃ (70‑atom supercell) and η‑Al₂O₃ (72‑atom supercell) are built from published atomic coordinates, exposing the (110C) surface and adding at least 10 Å of vacuum. A single Cr atom is placed first at the surface site where it is coordinated to one Al and two O atoms, and then in the subsurface octahedral interstitial. Full ionic relaxations are performed for each end‑point configuration. The minimum‑energy path and forward activation barrier for Cr migration from the surface to the subsurface site are obtained using climbing‑image nudged elastic band (CI‑NEB) calculations. Open‑source DFT codes with NEB capabilities serve as the computational engine.

## Reproduction target
Produce the following three scored artifacts:

1. `/app/outputs/barriers.json` – a JSON object with keys `gamma_alumina_barrier` and `eta_alumina_barrier`, each a floating‑point number giving the forward activation barrier (in eV) for Cr migration from the surface into the subsurface on that alumina polytype.

2. `/app/outputs/neb_gamma_alumina.xyz` – standard XYZ file containing the atomic coordinates of all images along the converged NEB path for γ‑alumina.

3. `/app/outputs/neb_eta_alumina.xyz` – same format for η‑alumina.

The computed barriers must be consistent with the expected physical trend between the two polytypes.

## Assets

- Slab structures of γ- and η-alumina from Sohlberg et al. (1999): 10.1021/ja9920388
- Open-source plane-wave DFT code with NEB support: https://www.quantum-espresso.org/
- GGA pseudopotentials for Al, O, Cr: https://materialscloud.org/sssp/

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Construct periodic slab models of γ-Al₂O₃ (70-atom supercell) and η-Al₂O₃ (72-atom supercell) with the (110C) surface exposed, using the atomic positions from the Sohlberg et al. (1999) reference, and add a vacuum region of at least 10 Å to separate periodic images.
- Evidence: `/app/outputs/structure_log.txt`

### Step 2: DFT relaxations of Cr surface and subsurface configurations
- Role: process
- Action: Using an open-source DFT code with GGA and pseudopotentials, relax the geometry of a single Cr atom placed at the reactive surface site (coordinated to one Al and two O) and in the subsurface octahedral interstitial site for both γ- and η-alumina slabs. Perform full ionic relaxations with appropriate k‑point sampling and kinetic‑energy cutoffs.
- Evidence: `/app/outputs/relaxed_geometries.log`

### Step 3: NEB calculations for Cr migration
- Role: process
- Action: Using the relaxed end‑point structures, perform climbing‑image nudged elastic band (CI‑NEB) calculations to determine the minimum‑energy path and the forward activation barrier for Cr moving from the surface into the subsurface site. Run separate NEB calculations for γ‑alumina and η‑alumina. Record the energy profile along the converged path.
- Evidence: `/app/outputs/neb_raw.log`

### Step 4: Collect activation barriers
- Role: scored (load-bearing)
- Action: Extract the forward energy barriers (in eV) from the NEB calculations and write them to /app/outputs/barriers.json as a JSON object with keys 'gamma_alumina_barrier' and 'eta_alumina_barrier'. The values must be floating‑point numbers in eV.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"gamma_alumina_barrier": <float>, "eta_alumina_barrier": <float>}
- Scoring: scored by hidden verifier

### Step 5: Export NEB path for γ-alumina to XYZ
- Role: scored
- Action: Export the atomic coordinates of all images along the converged NEB path for γ‑alumina to /app/outputs/neb_gamma_alumina.xyz in standard XYZ format (first line: number of atoms, second line: comment, then repeated atomic coordinates).
- Output file: `/app/outputs/neb_gamma_alumina.xyz`
- Format: other
- Contract: Standard XYZ format with all NEB images; first line number of atoms, second line comment, then atomic coordinates.
- Scoring: scored by hidden verifier

### Step 6: Export NEB path for η-alumina to XYZ
- Role: scored
- Action: Export the atomic coordinates of all images along the converged NEB path for η‑alumina to /app/outputs/neb_eta_alumina.xyz in standard XYZ format.
- Output file: `/app/outputs/neb_eta_alumina.xyz`
- Format: other
- Contract: Standard XYZ format with all NEB images; first line number of atoms, second line comment, then atomic coordinates.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.json`
- `/app/outputs/neb_gamma_alumina.xyz`
- `/app/outputs/neb_eta_alumina.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Activation barrier energies for Cr migration from surface to subsurface interstitial on γ‑ and η‑alumina.
- schema:
  - `type`: object
  - `required`:
    - `gamma_alumina_barrier`: number (eV)
    - `eta_alumina_barrier`: number (eV)

### neb_gamma_alumina.xyz
- path: `/app/outputs/neb_gamma_alumina.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Minimum-energy path atomic coordinates for γ-alumina.
- schema:
  - `type`: text
  - `description`: standard XYZ format with all NEB images

### neb_eta_alumina.xyz
- path: `/app/outputs/neb_eta_alumina.xyz`
- format: other
- purpose: scored
- target_policy: structural_audit
- description: Minimum-energy path atomic coordinates for η-alumina.
- schema:
  - `type`: text
  - `description`: standard XYZ format with all NEB images

Notes: The NEB path XYZ files are required as process evidence of a complete calculation and are audited structurally; the main scored quantity is the barrier values in barriers.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_alumina_barrier": "number (eV)",
          "eta_alumina_barrier": "number (eV)"
        }
      },
      "description": "Activation barrier energies for Cr migration from surface to subsurface interstitial on γ‑ and η‑alumina."
    },
    {
      "file": "neb_gamma_alumina.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "standard XYZ format with all NEB images"
      },
      "description": "Minimum-energy path atomic coordinates for γ-alumina."
    },
    {
      "file": "neb_eta_alumina.xyz",
      "format": "other",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "standard XYZ format with all NEB images"
      },
      "description": "Minimum-energy path atomic coordinates for η-alumina."
    }
  ],
  "notes": "The NEB path XYZ files are required as process evidence of a complete calculation and are audited structurally; the main scored quantity is the barrier values in barriers.json."
}
```

## How you are scored
A hidden verifier independently inspects each required workflow artifact and combines the results into a single score between 0.0 and 1.0. The main reward comes from `barriers.json`: the verifier compares the reported barrier values for γ‑ and η‑alumina against hidden reference values using appropriate tolerances, and it also checks that the two barriers satisfy the correct physical inequality (one must be substantially larger than the other). The XYZ files are audited for structural completeness (consistent atom counts, presence of Al/O/Cr, reasonable coordinates) and contribute a small additional weight. Simply printing the paper’s numbers is not sufficient; the verifier expects values that result from a genuine computational workflow.
