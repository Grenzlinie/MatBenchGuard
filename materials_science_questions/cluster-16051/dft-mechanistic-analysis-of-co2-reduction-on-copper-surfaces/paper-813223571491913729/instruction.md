# DFT-based Limiting Potential for Methanediol Reduction on Cu(211)

## Problem background
The electroreduction of CO₂ on copper yields a variety of products, and earlier computational work proposed that adsorbed formaldehyde (CH₂O*) is an intermediate leading to methane. However, experiments indicate that formaldehyde reduction produces methanol instead. Because formaldehyde is predominantly hydrated to methanediol (H₂C(OH)₂) in aqueous solution, investigating the reduction of methanediol rather than formaldehyde is crucial for reconciling these observations. This task computes the thermodynamic onset — the limiting potential (UL) — for the reduction of methanediol to methanol on a stepped Cu(211) surface using density functional theory (DFT) and the computational hydrogen electrode (CHE) model. The result provides a mechanistic estimate of the potential required for methanol formation via this route.

## Approach
The approach uses the computational hydrogen electrode (CHE) model, which relates electrochemical free energies to gas-phase chemical potentials. First, DFT calculations (using the RPBE functional) on a Cu(211) slab yield optimized geometries and free energy corrections (zero-point energy and entropy) for the clean surface and for the CH₂OH* and OH* adsorbates. Second, the free energy of aqueous methanediol relative to the RHE reference is derived from standard experimental thermodynamic data (e.g., the CRC Handbook) and the equilibrium constant for formaldehyde hydration (K ≈ 2×10³). Finally, the CHE framework constructs free energy diagrams at 0 V vs RHE, and the limiting potential — the potential where the last endergonic step becomes exergonic — is determined for two distinct reduction pathways: (1) * + H₂C(OH)₂ + H⁺ + e⁻ → CH₂OH* + H₂O, and (2) * + H₂C(OH)₂ + H⁺ + e⁻ → CH₃OH + OH* followed by OH* + H⁺ + e⁻ → * + H₂O.

## Reproduction target
Produce a JSON file named `limiting_potentials.json` containing the computed limiting potentials (in V versus the reversible hydrogen electrode) for the two pathways of methanediol reduction to methanol on Cu(211). The two values, under the keys `pathway1_UL` and `pathway2_UL`, must correspond to the pathways described above. The hidden verifier will compare these reported values to a reference; therefore, accurate computation using the described methodology and the specified inputs is essential.

## Assets

- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- Dacapo DFT code: https://wiki.fysik.dtu.dk/dacapo/
- Vanderbilt ultrasoft pseudopotentials (RPBE)
- Cu(211) surface structure
- Standard thermodynamic data (CRC Handbook of Chemistry and Physics): 10.1201/9781315380476

## Workflow steps

### Step 1: DFT Calculations of Surface Intermediates
- Role: process
- Action: Perform DFT calculations using the RPBE functional and Vanderbilt ultrasoft pseudopotentials on a Cu(211) slab to obtain optimized geometries and free energies (including zero-point energy and entropy corrections) for the clean surface and the adsorbates CH2OH* and OH*.
- Evidence: `/app/outputs/dft_output.log`

### Step 2: Derive Free Energy of Aqueous Methanediol
- Role: process
- Action: Using standard experimental thermodynamic data and the equilibrium constant for formaldehyde hydration (K ≈ 2×10^3), compute the standard free energy of H2C(OH)2(aq) relative to the RHE reference, applying the computational hydrogen electrode methodology.
- Evidence: none

### Step 3: Compute Limiting Potentials for Methanediol Reduction
- Role: scored (load-bearing)
- Action: Combine the DFT free energies of intermediates, the derived free energy of methanediol(aq), and standard chemical potentials of H2O(l) and H2(g) to construct CHE free energy diagrams at 0 V vs RHE. Determine the limiting potential (UL) for the two pathways: (1) * + H2C(OH)2 + H+ + e- → CH2OH* + H2O, and (2) * + H2C(OH)2 + H+ + e- → CH3OH + OH* followed by OH* + H+ + e- → * + H2O. Write the UL values (in V vs RHE) to limiting_potentials.json.
- Output file: `/app/outputs/limiting_potentials.json`
- Format: json
- Contract: Object with keys 'pathway1_UL' (float, V vs RHE) and 'pathway2_UL' (float, V vs RHE).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/limiting_potentials.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### limiting_potentials.json
- path: `/app/outputs/limiting_potentials.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Limiting potentials for methanediol reduction to methanol on Cu(211) via two distinct pathways computed with the CHE model.
- schema:
  - `type`: object
  - `required`:
    - `pathway1_UL`: number (float, V vs RHE)
    - `pathway2_UL`: number (float, V vs RHE)

Notes: The checker validates the reported limiting potentials against reference values derived from the paper's reported results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "limiting_potentials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pathway1_UL": "number (float, V vs RHE)",
          "pathway2_UL": "number (float, V vs RHE)"
        }
      },
      "description": "Limiting potentials for methanediol reduction to methanol on Cu(211) via two distinct pathways computed with the CHE model."
    }
  ],
  "notes": "The checker validates the reported limiting potentials against reference values derived from the paper's reported results."
}
```

## How you are scored
A hidden verifier reads your `limiting_potentials.json` and independently compares each reported limiting potential to a hidden reference. The final reward is a weighted combination of the two pathway scores, with each contributing equally. Full credit is earned when both reported UL values fall within a pre-defined tolerance of the reference; the reward decreases as the values deviate further from the expected range. The tolerance accounts for legitimate differences between DFT implementations while excluding values that are clearly incorrect.
