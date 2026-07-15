# DFT Calculation of SiH3 Dissociative Adsorption on H-terminated Si(001)-(2x1)

## Problem background
Hydrogenated amorphous silicon (a-Si:H) films deposited by plasma-enhanced chemical vapor deposition (PECVD) are crucial for electronic and photovoltaic devices. The silyl (SiH3) radical is believed to be the dominant growth precursor, but the detailed surface chemistry of its adsorption on hydrogen-terminated silicon surfaces is not fully resolved. One proposed reaction pathway is the dissociative adsorption of SiH3 via insertion into the Si–Si dimer bond of the H-terminated Si(001)-(2×1) surface, leading to the formation of surface dihydride species. Understanding the mechanism requires the energy landscape of this reaction — specifically, the energies of intermediates and transition states along the insertion pathway relative to the separated radical and surface. This task reproduces these energetics using first-principles density functional theory (DFT) on a cluster model.

## Approach
The reaction is studied on a Si9H12 cluster model of the Si(001)-(2×1):H surface, terminated with H atoms to saturate bulk bonds. Six stationary points are computed: the reference state (RS, consisting of a free SiH3 radical far from the surface), the insertion transition state (A), the three-electron insertion intermediate (B), a singly-bonded intermediate (C), the H-transfer transition state (D), and the final product with two surface dihydride species (E). For each configuration a geometry optimization is performed at the B3LYP/CEP-31G(d) level on Si and 6-31G on H using an open-source quantum chemistry package (PySCF, ORCA, or NWChem). The total energy of each optimized configuration is recorded in Hartree. The relative energies (in eV) with respect to RS are then computed from these total energies, using the conversion 1 Hartree = 27.2114 eV.

## Reproduction target
Your goal is to compute and report the DFT total energies (Hartree) and relative energies (eV) for the five stationary configurations A, B, C, D, and E, referenced to RS (whose relative energy is 0 eV). The energies must be obtained by geometry optimizations on the Si9H12 cluster model at the B3LYP/CEP-31G(d) (Si) and 6-31G (H) level, or an equivalent open-source DFT implementation. You will output a single JSON file, dft_energies.json, containing an array of configuration objects with the name, total_energy_Hartree, and relative_energy_eV for each configuration. The pathway must be correctly reproduced: configurations A, B, C, D, E correspond to the order along the dissociative adsorption reaction coordinate.

## Assets

- Open-source DFT package (PySCF, ORCA, or NWChem): https://pyscf.org

## Workflow steps

### Step 1: Build cluster model and prepare initial geometries
- Role: process
- Action: Construct the Si9H12 cluster model of the Si(001)-(2x1):H surface: two Si atoms in the top layer, four, two, and one Si atoms in the second, third, and fourth layers, with Si-H bonds of 1.50 Å to terminate bulk bonds. Prepare initial geometry guess files for the six stationary points: RS (reference state with free SiH3 far from the surface), A (transition state for dimer insertion), B (insertion intermediate), C (singly bonded intermediate), D (H-transfer transition state), E (final product with two dihydride species).
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT geometry optimizations
- Role: process
- Action: Perform DFT geometry optimization for each of the six configurations (RS, A, B, C, D, E) at the B3LYP/CEP-31G(d) level on Si and 6-31G on H. Record the final optimized geometry and the converged total energy (in Hartree) for each configuration. Ensure convergence criteria are met.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 3: Report relative DFT energies
- Role: scored (load-bearing)
- Action: From the converged DFT total energies, compute the relative energies (in eV) of configurations A, B, C, D, E with respect to the reference state (RS). Write a JSON file containing the total and relative energies.
- Output file: `/app/outputs/dft_energies.json`
- Format: json
- Contract: {"configurations": [{"name": "string", "total_energy_Hartree": number, "relative_energy_eV": number}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_energies.json
- path: `/app/outputs/dft_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Reported total DFT energies (Hartree) and relative energies (eV) compared to RS for the five stationary points A through E. The checker recomputes relative energies and compares to paper values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `configurations`: array
  - `items`:
    - `name`: string
    - `total_energy_Hartree`: number
    - `relative_energy_eV`: number

Notes: Relative energies are computed with 1 Hartree = 27.2114 eV and are referenced to configuration RS (relative_energy_eV = 0). The 'configurations' array must include entries for A, B, C, D, E, and optionally RS; only the relative energies of A–E are scored. The agent must not precompute relative energies from a known paper value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "configurations": "array"
        },
        "items": {
          "name": "string",
          "total_energy_Hartree": "number",
          "relative_energy_eV": "number"
        }
      },
      "description": "Reported total DFT energies (Hartree) and relative energies (eV) compared to RS for the five stationary points A through E. The checker recomputes relative energies and compares to paper values within a tolerance."
    }
  ],
  "notes": "Relative energies are computed with 1 Hartree = 27.2114 eV and are referenced to configuration RS (relative_energy_eV = 0). The 'configurations' array must include entries for A, B, C, D, E, and optionally RS; only the relative energies of A–E are scored. The agent must not precompute relative energies from a known paper value."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks the content of dft_energies.json. First, the verifier validates the JSON structure. Then, it recomputes the relative energies from your reported total energies (using 1 Hartree = 27.2114 eV) and compares them for configurations A–E against hidden reference values derived from the computational literature. An absolute error is calculated for each configuration; all five must fall within a predefined tolerance to pass. The final score is based on the number of configurations that meet the tolerance, with full credit awarded only when all five pass. There is no partial credit for simply reporting numbers that look plausible; the verifier expects results consistent with an honest re-run of the specified DFT protocol.
