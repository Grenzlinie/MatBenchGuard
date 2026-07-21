# Adsorption of nucleobases on Al-doped coronene under external electric fields: a DFT reproduction

## Problem background
Nucleobases — adenine (A), thymine (T), guanine (G), and cytosine (C) — are the fundamental building blocks of DNA. Developing solid‑state sensing platforms that can detect these molecules with high sensitivity is an important goal in biosensing. Coronene (C₂₄H₁₂), a planar polycyclic aromatic hydrocarbon, has been explored as a potential sensing substrate, and its sensitivity can be tuned by doping with foreign atoms and by applying external electric fields. This investigation uses density functional theory (DFT) calculations to study the adsorption of nucleobases on pristine coronene and on aluminum‑doped coronene (Al‑coronene) in the absence and presence of perpendicular external electric fields. The key quantities of interest are adsorption energy, band gap, and charge transfer, which can serve as signatures of sensor sensitivity.

## Approach
The reproduction employs DFT calculations at the wB97XD/6‑31G(d,p) level of theory, which includes empirical dispersion corrections. The workflow consists of three stages. First, the isolated species — pristine coronene, Al‑coronene (with Al substituted at a non‑edge carbon), and each nucleobase — are fully geometry‑optimized. Second, for each nucleobase the most stable adsorption complex on Al‑coronene is constructed (referred to as the A1, T1, G1, and C1 configurations) and optimized without an external field and under two perpendicular electric fields (1.0×10⁻² a.u. and 2.0×10⁻² a.u. applied in the negative x direction). Third, from the optimized structures, total energies, HOMO/LUMO energies, Mulliken charges, and the shortest Al–N/O distance are extracted. Adsorption energies E_ads are calculated with counterpoise (BSSE) and zero‑point energy (ZPE) corrections, and the percentage change in band gap ΔE_g% is computed relative to isolated Al‑coronene. The calculations may be performed with any open‑source DFT code that supports the required functional and basis set (e.g., ORCA). The precise computational settings that are not specified by the external conditions (functional, basis, field strengths) are left to the agent’s discretion; the output will be judged against reference results with tolerances that account for toolchain variations.

## Reproduction target
Produce a single JSON file, results.json, containing the following quantities for each of the 14 required systems: isolated coronene, isolated Al‑coronene, and the twelve adsorption complexes A1_EF0, T1_EF0, G1_EF0, C1_EF0, A1_EF1e‑2, T1_EF1e‑2, G1_EF1e‑2, C1_EF1e‑2, A1_EF2e‑2, T1_EF2e‑2, G1_EF2e‑2, C1_EF2e‑2. For each system report: E_ads (adsorption energy, kcal/mol; use null for reference systems), Eg (band gap, eV), delta_Eg_percent (percentage change in band gap relative to Al‑coronene; null for reference systems), QT (Mulliken charge transfer, e; null for reference systems), HOMO (eV), LUMO (eV), and d (interaction distance, Å; null for reference systems). The checker will compare your computed values against hidden reference values (the paper’s reported results) using appropriate tolerances, and will also evaluate whether the computed E_ads shows a consistent trend with increasing field strength, whether the band gap changes upon adsorption, and whether the approximate relative ordering of adsorption strengths among the four nucleobases is consistent with the reference. The output must follow the specified JSON schema, and all 14 systems must be present.

## Assets

- Open-source DFT software supporting wB97XD/6-31G(d,p) with external electric field capability (e.g., ORCA): https://orcaforum.kofo.mpg.de/
- Molecular structures of coronene (C24H12) and the nucleobases adenine, thymine, guanine, cytosine: https://pubchem.ncbi.nlm.nih.gov/

## Workflow steps

### Step 1: Geometry optimization of isolated species
- Role: process
- Action: Perform DFT geometry optimization of pristine coronene, Al-coronene (Al substituted at a non-edge carbon), and the four isolated nucleobases (adenine, thymine, guanine, cytosine) using the wB97XD functional and the 6‑31G(d,p) basis set. Convergence criteria: energy 1×10⁻⁶ Ha, force 3×10⁻⁴ Ha/Å, displacement 5×10⁻³ Å. Record optimized coordinates and total energies.
- Evidence: `/app/outputs/step1_opt_logs.txt`

### Step 2: Geometry optimization of adsorption complexes
- Role: process
- Action: For each nucleobase, set up the most stable adsorption configuration on Al-coronene (as denoted A1, T1, G1, C1 in the paper). Perform DFT geometry optimization with no external field, and under perpendicular external electric fields of 1.0×10⁻² a.u. and 2.0×10⁻² a.u. applied in the negative x‑direction. Use the same functional (wB97XD), basis set (6‑31G(d,p)), and convergence criteria as in step 1.
- Evidence: `/app/outputs/step2_opt_logs.txt`

### Step 3: Computation of adsorption energies and electronic properties
- Role: scored (load-bearing)
- Action: From the optimized structures obtained in steps 1 and 2, extract total energies, HOMO, LUMO, band gap E_g, Mulliken charge on the adsorbate Q_T, and the shortest Al–N/O distance d. Compute adsorption energies E_ads with BSSE counterpoise correction and zero‑point energy correction, and calculate the percentage change in band gap ΔE_g% relative to the isolated Al‑coronene. Assemble all results into a single JSON file under /app/outputs/results.json covering the reference systems (coronene, Al‑coronene) and all complexes (A1_EF0, T1_EF0, G1_EF0, C1_EF0, A1_EF1e-2, T1_EF1e-2, G1_EF1e-2, C1_EF1e-2, A1_EF2e-2, T1_EF2e-2, G1_EF2e-2, C1_EF2e-2).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: A JSON array of objects. Each object must have keys: system (string, one of the values listed in the action), E_ads (number or null for reference systems; units: kcal/mol), Eg (number; units: eV), delta_Eg_percent (number or null for reference systems; unitless), QT (number or null for reference systems; in e), HOMO (number; in eV), LUMO (number; in eV), d (number or null for reference systems; in Å).
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
- target_policy: threshold_or_better
- description: The single scored artifact containing the reproduced adsorption energies, band gaps, charge transfers, HOMO/LUMO energies, and interaction distances for all required systems. The checker compares each numeric field to hidden paper gold values using threshold‑or‑better semantics: meeting or exceeding the reference performance earns full credit, and partial credit decreases only when the result is worse. For E_ads lower (more negative) is better; for Eg lower is better; for |QT| higher is better; for |ΔE_g%| higher is better; trends and ordering are also checked. Missing systems or fields result in zero credit for the corresponding checks.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system`, `E_ads`, `Eg`, `delta_Eg_percent`, `QT`, `HOMO`, `LUMO`, `d`
    - `properties`:
      - `system`:
        - `type`: string
      - `E_ads`:
        - `type`: `number`, `null`
        - `units`: kcal/mol
      - `Eg`:
        - `type`: number
        - `units`: eV
      - `delta_Eg_percent`:
        - `type`: `number`, `null`
      - `QT`:
        - `type`: `number`, `null`
        - `units`: e
      - `HOMO`:
        - `type`: number
        - `units`: eV
      - `LUMO`:
        - `type`: number
        - `units`: eV
      - `d`:
        - `type`: `number`, `null`
        - `units`: Å
  - `required_systems`: `coronene`, `Al-coronene`, `A1_EF0`, `T1_EF0`, `G1_EF0`, `C1_EF0`, `A1_EF1e-2`, `T1_EF1e-2`, `G1_EF1e-2`, `C1_EF1e-2`, `A1_EF2e-2`, `T1_EF2e-2`, `G1_EF2e-2`, `C1_EF2e-2`

Notes: The checker verifies that the agent's reported E_ads values become more negative under applied electric fields, that the band gap decreases relative to Al-coronene, and that the relative ordering among nucleobases matches the paper's trends. Tolerances are sized to accommodate toolchain differences (different DFT code but same functional/basis).

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system",
            "E_ads",
            "Eg",
            "delta_Eg_percent",
            "QT",
            "HOMO",
            "LUMO",
            "d"
          ],
          "properties": {
            "system": {
              "type": "string"
            },
            "E_ads": {
              "type": [
                "number",
                "null"
              ],
              "units": "kcal/mol"
            },
            "Eg": {
              "type": "number",
              "units": "eV"
            },
            "delta_Eg_percent": {
              "type": [
                "number",
                "null"
              ]
            },
            "QT": {
              "type": [
                "number",
                "null"
              ],
              "units": "e"
            },
            "HOMO": {
              "type": "number",
              "units": "eV"
            },
            "LUMO": {
              "type": "number",
              "units": "eV"
            },
            "d": {
              "type": [
                "number",
                "null"
              ],
              "units": "Å"
            }
          }
        },
        "required_systems": [
          "coronene",
          "Al-coronene",
          "A1_EF0",
          "T1_EF0",
          "G1_EF0",
          "C1_EF0",
          "A1_EF1e-2",
          "T1_EF1e-2",
          "G1_EF1e-2",
          "C1_EF1e-2",
          "A1_EF2e-2",
          "T1_EF2e-2",
          "G1_EF2e-2",
          "C1_EF2e-2"
        ]
      },
      "description": "The single scored artifact containing the reproduced adsorption energies, band gaps, charge transfers, HOMO/LUMO energies, and interaction distances for all required systems. The checker compares each numeric field to hidden paper gold values using threshold‑or‑better semantics: meeting or exceeding the reference performance earns full credit, and partial credit decreases only when the result is worse. For E_ads lower (more negative) is better; for Eg lower is better; for |QT| higher is better; for |ΔE_g%| higher is better; trends and ordering are also checked. Missing systems or fields result in zero credit for the corresponding checks."
    }
  ],
  "notes": "The checker verifies that the agent's reported E_ads values become more negative under applied electric fields, that the band gap decreases relative to Al-coronene, and that the relative ordering among nucleobases matches the paper's trends. Tolerances are sized to accommodate toolchain differences (different DFT code but same functional/basis)."
}
```

## How you are scored
Your results.json file is the primary scored artifact. The hidden verifier compares each reported value to hidden reference values (the corresponding quantity from the published study) using tolerances that allow for differences in DFT implementations. It also checks that the computed E_ads exhibits a clear trend with increasing field strength, that the band gap decreases significantly relative to the isolated Al‑coronene, and that the relative ordering of adsorption strengths among the nucleobases is consistent with the reference. Additionally, the verifier may verify the presence of the intermediate evidence files step1_opt_logs.txt and step2_opt_logs.txt as proof that the geometry optimizations were completed. The overall reward is a weighted sum of these numeric and trend checks. Simply copying the paper’s published numbers without performing the DFT calculations will not generate the required evidence and will result in a very low score.
