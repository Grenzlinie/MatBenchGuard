## Problem background

The reconstructed Si(100)2×1 surface consists of rows of surface dimers, each Si atom having a dangling bond, making the surface reactive. Understanding Si–H bond strengths and H₂ recombinative desorption energies is important for modeling hydrogen atom diffusion and desorption mechanisms on this surface. Finite cluster models provide a computationally tractable approach to estimate these energies using density functional theory (DFT).

## Approach

This task reproduces DFT-based reaction energies for hydrogen dissociation and recombinative desorption on a Si(100) surface dimer cluster. The method uses finite cluster models to represent the surface:
- Si₉H₁₂ is the bare surface dimer with hydrogen atoms terminating subsurface silicon bonds.
- Si₉H₁₃ is the monohydride, obtained by adding one surface hydrogen to Si₉H₁₂.
- Si₉H₁₄ is the dihydride, obtained by adding a second surface hydrogen.

Geometries of all three clusters are optimized in the local density approximation (LDA), using the Dirac exchange functional and the Vosko–Wilk–Nusair (VWN) correlation functional. During optimization, deeper-layer silicon atoms (layers three and four) and all terminating hydrogen atoms are held fixed; the four Si atoms in the second layer are allowed to move only in the x and z directions; surface Si atoms and any attached surface H atoms are fully relaxed.

Single-point electronic energies are then computed at the LDA-optimized geometries using a nonlocal-corrected density functional known as VWN+BP. This functional uses the VWN local spin-density reference plus gradient-corrected Becke exchange and Perdew correlation, applied perturbatively. The basis set is triple-zeta plus polarization (TZVPP), for which cc-pVTZ serves as a practical surrogate. Total energies are calculated for all three clusters, the H atom, and the H₂ molecule.

From these total energies, three reaction energies (in kcal/mol) are evaluated:
1. Si₉H₁₄ → Si₉H₁₃ + H  (dissociation of one surface H)
2. Si₉H₁₃ → Si₉H₁₂ + H  (dissociation of the remaining surface H)
3. Si₉H₁₄ → Si₉H₁₂ + H₂ (recombinative desorption)

## Reproduction target

Produce the three reaction energies listed above at the VWN+BP/TZVPP level on LDA-optimized geometries. The result must be written to `/app/outputs/reaction_energies.json` in kcal/mol.

## Assets

- **Open-source DFT code** (e.g., GPAW, NWChem, Quantum ESPRESSO) capable of LDA geometry optimization and nonlocal-corrected single-point energy calculations. Access hint: https://wiki.fysik.dtu.dk/gpaw/
- **cc-pVTZ basis set** for Si and H, obtained from the Basis Set Exchange: https://www.basissetexchange.org/basis/cc-pvtz/

## Workflow steps

### Step 1: Build cluster models and optimize geometries at LDA level
- Role: process
- Action: Construct the Si₉H₁₂, Si₉H₁₃, and Si₉H₁₄ cluster models as finite representations of the Si(100) surface dimer with hydrogen termination of subsurface atoms. Apply the constraints described in the Approach section. Optimize the geometries of all three clusters at the LDA level (Dirac exchange + VWN correlation).
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 2: Compute single-point energies at VWN+BP/TZVPP level
- Role: process
- Action: Using the LDA-optimized geometries from Step 1, perform single-point energy calculations with the nonlocal-corrected VWN+BP functional and the cc-pVTZ basis set (as a surrogate for TZVPP). Compute total energies for Si₉H₁₄, Si₉H₁₃, Si₉H₁₂, the H atom, and the H₂ molecule.
- Evidence: `/app/outputs/total_energies.json`

### Step 3: Calculate and output reaction energies
- Role: scored (load-bearing)
- Action: From the total energies obtained in Step 2, calculate the three reaction energies: (1) E(Si₉H₁₄→Si₉H₁₃+H) = E(Si₉H₁₃) + E(H) − E(Si₉H₁₄), (2) E(Si₉H₁₃→Si₉H₁₂+H) = E(Si₉H₁₂) + E(H) − E(Si₉H₁₃), (3) E(Si₉H₁₄→Si₉H₁₂+H₂) = E(Si₉H₁₂) + E(H₂) − E(Si₉H₁₄). Convert the results to kcal/mol (1 Hartree = 627.5095 kcal/mol). Write the three values together with the unit to the output file.
- Output file: `/app/outputs/reaction_energies.json`
- Format: json
- Contract: A JSON object with keys `E1`, `E2`, `E3` (numeric reaction energies) and `unit` (string `"kcal/mol"`).
- Scoring: scored by hidden verifier

## Output files

All artifacts are written under `/app/outputs/`:
- `optimized_geometries.xyz` (optional process evidence)
- `total_energies.json` (optional process evidence)
- `reaction_energies.json` (required scored output)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reaction_energies.json
- path: `/app/outputs/reaction_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The three headline DFT reaction energies (kcal/mol) computed at the VWN+BP/TZVPP level on LDA-optimized geometries. The hidden verifier compares each value to a fixed reference with an absolute tolerance.
- schema:
  - `type`: object
  - `required`:
    - `E1`: number
    - `E2`: number
    - `E3`: number
    - `unit`: string

Notes: Only the reaction energies are scored. The process evidence artifacts (optimized_geometries.xyz, total_energies.json) are not part of the output contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reaction_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E1": "number",
          "E2": "number",
          "E3": "number",
          "unit": "string"
        }
      },
      "description": "The three headline DFT reaction energies (kcal/mol) computed at the VWN+BP/TZVPP level on LDA-optimized geometries. The hidden verifier compares each value to a fixed reference with an absolute tolerance."
    }
  ],
  "notes": "Only the reaction energies are scored. The process evidence artifacts (optimized_geometries.xyz, total_energies.json) are not part of the output contract."
}
```

## How you are scored

A hidden verifier independently evaluates your `reaction_energies.json`. It compares your reported energies to a known reference using an absolute tolerance. The reward is based on how close each of the three values is to the reference; you earn full credit when all differences fall within the tolerance. Reporting the correct values from the paper alone is not sufficient – the verifier expects the energies to be produced by the described DFT workflow, and the scored step is load-bearing, meaning its result cannot be supplied without genuinely executing the preceding process steps.
