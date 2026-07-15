# DFT Phonon Calculation of the T Peak in Partially Hydrogenated Multilayer Graphene

## Problem background
Partially hydrogenated few-layer graphene (diamanoids) exhibits a sharp Raman peak, the so‑called T peak, in the range 1050–1100 cm⁻¹. Its vibrational mode and origin were previously not well understood. Density functional theory (DFT) phonon calculations on a structurally explicit model can reveal the nature of this mode. In this task, you will perform such a calculation and determine the frequency of the T‑peak mode.

## Approach
Build the atomic model of a partially hydrogenated four‑layer slab with ABBA stacking: the top layer is fully hydrogenated (all C sp³, half bonded to H), the second layer is partially hydrogenated (half sp³ with a dangling pz orbital), while the bottom two layers remain pure sp²‑hybridized graphene. All operations are performed with plane‑wave DFT using the PBE functional and a van der Waals correction. First, relax the slab geometry until the forces are converged. Then compute the phonon dispersion at the Γ point using density functional perturbation theory (DFPT) with the same functional and pseudopotentials. Analyze the resulting phonon eigenvectors to identify the Raman‑active normal mode that corresponds to the T peak—it is expected to involve significant atomic motions in the hydrogenated and interface layers. Extract and report its frequency.

## Reproduction target
Compute the phonon frequency (in cm⁻¹) of the Raman‑active mode that corresponds to the T peak in the ABBA‑stacked partially hydrogenated four‑layer model, obtained from a DFPT calculation at the Γ point using the PBE functional with van der Waals correction. Report the frequency in the file `/app/outputs/t_peak_frequency.json` under the key `"t_peak_frequency_cm-1"`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct ABBA four-layer model
- Role: process
- Action: Build the atomic structure of the partially hydrogenated four-layer model with ABBA stacking (L1 fully hydrogenated, L2 partially hydrogenated, L3 and L4 graphene). Set a vacuum of at least 20 Å normal to the slab. Prepare a DFT input file (e.g., QE pw.x input) with the correct atomic species and initial coordinates.
- Evidence: `/app/outputs/initial_structure.xyz`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization of the ABBA slab using the PBE functional with van der Waals correction (e.g., Grimme's D3). Relax all atomic positions until forces are converged, keeping the cell dimensions fixed. Output the relaxed structure.
- Evidence: `/app/outputs/relaxed_structure.pwo`

### Step 3: DFPT phonon calculation at Gamma
- Role: process
- Action: Using the relaxed structure, perform a density-functional perturbation theory (DFPT) phonon calculation (e.g., ph.x in Quantum ESPRESSO) to compute the dynamical matrix at the Gamma point. Obtain phonon eigenvalues and eigenvectors. Alternatively, use Phonopy with finite displacements; ensure the calculation yields Gamma-point frequencies.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 4: Extract T peak frequency
- Role: scored (load-bearing)
- Action: From the phonon eigenvalues, identify the Raman-active mode corresponding to the T peak: a normal mode with mixed sp³-C bond stretching and out-of-plane (ZO) graphene motion, anticipated in the region 1050–1100 cm⁻¹. Report its frequency in cm⁻¹. Write the value to /app/outputs/t_peak_frequency.json.
- Output file: `/app/outputs/t_peak_frequency.json`
- Format: json
- Contract: {"type": "object", "required": {"t_peak_frequency_cm-1": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/t_peak_frequency.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### t_peak_frequency.json
- path: `/app/outputs/t_peak_frequency.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFPT-computed phonon frequency of the Raman T peak mode, reported in cm⁻¹. The hidden checker compares this value to the paper-reported DFPT result with a tolerance to account for differences in DFT code, pseudopotentials, and convergence settings.
- schema:
  - `type`: object
  - `required`:
    - `t_peak_frequency_cm-1`: number

Notes: The scored artifact is the frequency of the Raman-active mode that corresponds to the T peak in the ABBA-stacked partially hydrogenated four-layer model. The checker uses a tolerance-based comparison (T0 result-level) against the hidden gold value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "t_peak_frequency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "t_peak_frequency_cm-1": "number"
        }
      },
      "description": "DFPT-computed phonon frequency of the Raman T peak mode, reported in cm⁻¹. The hidden checker compares this value to the paper-reported DFPT result with a tolerance to account for differences in DFT code, pseudopotentials, and convergence settings."
    }
  ],
  "notes": "The scored artifact is the frequency of the Raman-active mode that corresponds to the T peak in the ABBA-stacked partially hydrogenated four-layer model. The checker uses a tolerance-based comparison (T0 result-level) against the hidden gold value."
}
```

## How you are scored
The hidden verifier will evaluate each required step’s artifact. The main scoring weight is on the extracted T peak frequency. The verifier compares your reported frequency to the expected value (derived from the original study) using a tolerance that accommodates genuine differences in DFT implementations, pseudopotentials, and convergence parameters. A result within the acceptable tolerance earns full credit; larger deviations yield proportionally lower scores. Simply supplying a plausible number without actually performing the calculation is very unlikely to fall within the tolerance. Process‑step evidence (initial structure, relaxed structure, phonon output) may also be audited for consistency, but carries minimal weight compared to the scored frequency.
