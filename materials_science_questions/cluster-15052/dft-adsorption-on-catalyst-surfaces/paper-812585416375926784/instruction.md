# DFT adsorption energies on graphitic carbon nitride

## Problem background
The photocatalytic oxidative cleavage of C–C bonds in 1,2-diols is a key transformation for producing carbonyl compounds. A heterogeneous metal-free photocatalytic system based on mesoporous graphitic carbon nitride (mpg‑C₃N₄) has been proposed for this reaction. To understand the interaction between the catalyst surface and substrate molecules and to support a radical mechanism, Density Functional Theory (DFT) calculations are performed to investigate the adsorption of substrates on the catalyst surface. The strength and manner of adsorption determine whether electron transfer can occur efficiently, which is critical for the catalytic activity. This task focuses on computing those adsorption energies using an open-source quantum chemistry package.

## Approach
The computational approach uses a three-layer ONIOM method to model the catalyst–substrate system. A 4×4 sheet of tri‑s‑triazine‑based graphitic carbon nitride is built with a corrugated conformation, which is the most stable structure. Two substrate molecules are considered: 1,2‑diphenylethane‑1,2‑diol (substrate 1a) and benzil (substrate 1y). Their geometries are obtained from public compound databases. For each substrate, the system is divided into three layers: the substrate and the directly interacting catalyst atoms are treated at the high level (B3LYP/6‑31G*), the neighboring catalyst atoms at a medium level (HF/6‑31G*), and the remainder of the slab at a low level (PM6 semi‑empirical). Geometry optimizations are performed for the free substrate, the free catalyst, and the adsorbed complex in three distinct adsorption patterns: (A) the hydrogen atom of a hydroxyl group in 1a approaching an edge nitrogen atom of the catalyst surface; (B) the oxygen atom of the hydroxyl group of 1a approaching a central nitrogen atom; (C) the carbonyl oxygen of benzil (1y) approaching a central nitrogen atom. The adsorption energy is calculated as E_ads = E(complex) – E(free substrate) – E(free catalyst). The resulting energies quantify the strength of the interaction.

## Reproduction target
Compute the adsorption energies (in eV) for the three adsorption patterns described above using an open‑source quantum chemistry package capable of ONIOM or equivalent layered calculations (e.g., ORCA, NWChem, Quantum ESPRESSO). Export the results as a JSON file with three numeric fields: pattern_a_energy_eV, pattern_b_energy_eV, and pattern_c_energy_eV. The target is to produce adsorption energies that reflect the relative stability of the different adsorption modes on the catalyst surface, as assessed by a hidden verifier.

## Assets

- Open-source quantum chemistry package (e.g., ORCA): https://orcaforum.kofo.mpg.de/
- PubChem CID 10397 (1,2-diphenylethane-1,2-diol): https://pubchem.ncbi.nlm.nih.gov/compound/10397
- PubChem CID 8651 (benzil): https://pubchem.ncbi.nlm.nih.gov/compound/8651

## Workflow steps

### Step 1: Compute DFT adsorption energies
- Role: scored (load-bearing)
- Action: Construct a 4×4 tri‑s‑triazine‑based g‑C₃N₄ corrugated sheet model. Obtain molecular structures of 1,2‑diphenylethane‑1,2‑diol (from PubChem CID 10397) and benzil (PubChem CID 8651). Perform geometry optimizations and adsorption energy calculations using the ONIOM method with high layer B3LYP/6-31G*, medium layer HF/6-31G*, low layer PM6. Compute the adsorption energy E_ads = E(complex) – E(free substrate) – E(free catalyst) for three adsorption patterns: (A) hydroxyl H of substrate 1a approaching edge nitrogen atom on the catalyst surface, (B) hydroxyl O of substrate 1a approaching central nitrogen atom, (C) carbonyl O of benzil (1y) approaching central nitrogen atom. Export the final adsorption energies in eV as a JSON file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with exactly three numeric keys: "pattern_a_energy_eV", "pattern_b_energy_eV", "pattern_c_energy_eV" (float, units eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: DFT adsorption energies for the three patterns: adsorption energy in eV for the specified adsorption configurations on the catalyst surface.
- schema:
  - `type`: object
  - `required`:
    - `pattern_a_energy_eV`: number
    - `pattern_b_energy_eV`: number
    - `pattern_c_energy_eV`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `pattern_a_energy_eV`: eV
    - `pattern_b_energy_eV`: eV
    - `pattern_c_energy_eV`: eV

Notes: The checker will verify each value against a hidden reference with a tolerance and check the relative ordering (more negative is stronger adsorption). No gold values are revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "pattern_a_energy_eV": "number",
          "pattern_b_energy_eV": "number",
          "pattern_c_energy_eV": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "pattern_a_energy_eV": "eV",
          "pattern_b_energy_eV": "eV",
          "pattern_c_energy_eV": "eV"
        }
      },
      "description": "DFT adsorption energies for the three patterns: adsorption energy in eV for the specified adsorption configurations on the catalyst surface."
    }
  ],
  "notes": "The checker will verify each value against a hidden reference with a tolerance and check the relative ordering (more negative is stronger adsorption). No gold values are revealed."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads your `adsorption_energies.json` and compares the reported adsorption energies to reference values derived from the original study, using a tolerance that accounts for legitimate differences between computational implementations. Additionally, the verifier checks that the relative ordering of the adsorption strengths across the three patterns is consistent with the expected physical trend. Meeting the reference criteria within tolerance earns full credit; results that are too far from the expected range or that violate the ordering receive partial or no credit. The final score is a weighted combination of the checks on the individual energies and the ordering.
