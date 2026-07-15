# DFT Calculation of Electronic and Topological Properties of NbC and TaC

## Problem background
Rocksalt-type carbides NbC and TaC are superconducting materials with transition temperatures around 11 K. They are of interest because their electronic band structure may harbor nontrivial topological features, such as closed nodal lines, which could lead to topological superconductivity. Determining key electronic properties — the density of states at the Fermi level, the spin-orbit coupling (SOC) splitting, and the presence of nodal loops — is essential for assessing their potential as topological superconductors. This task focuses on computing these quantities from first principles.

## Approach
The work will be carried out using density functional theory (DFT) within the generalized gradient approximation (GGA-PBE) and with spin-orbit coupling included via a scalar relativistic treatment. The calculations will be performed for the rocksalt crystal structure (space group Fm-3m, with Nb/Ta at 4a and C at 4b) using experimental lattice parameters. The band structure and density of states will be computed both with and without SOC. From these, the total DOS at the Fermi level, the maximum SOC-induced band splitting along the Γ-X high-symmetry line, and the existence of three closed nodal loops in the mirror planes (when SOC is turned off) will be extracted. The computational work will be implemented with any standard open-source DFT code and publicly available pseudopotentials.

## Reproduction target
Using the DFT setup described in the workflow steps (including the specified crystal structures, functional, k-point mesh, and energy cutoff), compute the electronic structure of NbC and TaC. From the results, extract and report in a JSON file (dft_results.json) for each compound: (a) the total density of states at the Fermi level (states/eV per formula unit) from the SOC calculation, (b) the maximum band splitting due to spin-orbit coupling along the Γ-X direction (meV), and (c) a boolean indicating whether three closed nodal loops are present in the planes kx=0, ky=0, kz=0 when spin-orbit coupling is not considered.

## Assets

- Open-source DFT software (e.g., Quantum ESPRESSO, ABINIT, GPAW): https://www.quantum-espresso.org
- Pseudopotential library for Nb, Ta, C (PBE PAW or norm-conserving): http://www.pseudo-dojo.org

## Workflow steps

### Step 1: DFT calculation and topological analysis for NbC and TaC
- Role: scored (load-bearing)
- Action: Run DFT calculations for NbC and TaC using an open-source code with the GGA-PBE functional and spin-orbit coupling. Use the experimental rocksalt crystal structures (space group Fm-3m, Nb/Ta at 4a, C at 4b) with appropriate lattice constants. Compute the electronic band structure and density of states both with and without SOC. From the results, extract: (a) the total density of states at the Fermi level (states/eV f.u.) from the SOC calculation; (b) the maximum band splitting due to SOC along the Γ-X direction (meV); (c) a boolean indicating whether three closed nodal loops are present in the planes kx=0, ky=0, kz=0 when SOC is turned off. Save all results to /app/outputs/dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"type": "object", "required": ["NbC", "TaC"], "properties": {"NbC": {"type": "object", "required": ["dos_at_fermi", "soc_splitting_meV", "nodal_loops_present_without_soc"], "properties": {"dos_at_fermi": {"type": "number", "description": "DOS at Fermi level in states/eV f.u."}, "soc_splitting_meV": {"type": "number", "description": "Maximum SOC band splitting along Γ-X in meV"}, "nodal_loops_present_without_soc": {"type": "boolean", "description": "True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC"}}}, "TaC": {"type": "object", "required": ["dos_at_fermi", "soc_splitting_meV", "nodal_loops_present_without_soc"], "properties": {"dos_at_fermi": {"type": "number", "description": "DOS at Fermi level in states/eV f.u."}, "soc_splitting_meV": {"type": "number", "description": "Maximum SOC band splitting along Γ-X in meV"}, "nodal_loops_present_without_soc": {"type": "boolean", "description": "True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC"}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the DFT-computed electronic structure quantities for NbC and TaC: Fermi-level DOS, SOC splitting, and nodal loop presence.
- schema:
  - `type`: object
  - `required`: `NbC`, `TaC`
  - `properties`:
    - `NbC`:
      - `type`: object
      - `required`: `dos_at_fermi`, `soc_splitting_meV`, `nodal_loops_present_without_soc`
      - `properties`:
        - `dos_at_fermi`:
          - `type`: number
          - `description`: DOS at Fermi level in states/eV f.u.
        - `soc_splitting_meV`:
          - `type`: number
          - `description`: Maximum SOC band splitting along Γ-X in meV
        - `nodal_loops_present_without_soc`:
          - `type`: boolean
          - `description`: True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC
    - `TaC`:
      - `type`: object
      - `required`: `dos_at_fermi`, `soc_splitting_meV`, `nodal_loops_present_without_soc`
      - `properties`:
        - `dos_at_fermi`:
          - `type`: number
          - `description`: DOS at Fermi level in states/eV f.u.
        - `soc_splitting_meV`:
          - `type`: number
          - `description`: Maximum SOC band splitting along Γ-X in meV
        - `nodal_loops_present_without_soc`:
          - `type`: boolean
          - `description`: True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC

Notes: The checker compares each numeric value against paper-reported values with hidden tolerances and checks the boolean flags. The target_policy is exact_match because the quantities are fixed physical properties with no notion of 'better'.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "NbC",
          "TaC"
        ],
        "properties": {
          "NbC": {
            "type": "object",
            "required": [
              "dos_at_fermi",
              "soc_splitting_meV",
              "nodal_loops_present_without_soc"
            ],
            "properties": {
              "dos_at_fermi": {
                "type": "number",
                "description": "DOS at Fermi level in states/eV f.u."
              },
              "soc_splitting_meV": {
                "type": "number",
                "description": "Maximum SOC band splitting along Γ-X in meV"
              },
              "nodal_loops_present_without_soc": {
                "type": "boolean",
                "description": "True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC"
              }
            }
          },
          "TaC": {
            "type": "object",
            "required": [
              "dos_at_fermi",
              "soc_splitting_meV",
              "nodal_loops_present_without_soc"
            ],
            "properties": {
              "dos_at_fermi": {
                "type": "number",
                "description": "DOS at Fermi level in states/eV f.u."
              },
              "soc_splitting_meV": {
                "type": "number",
                "description": "Maximum SOC band splitting along Γ-X in meV"
              },
              "nodal_loops_present_without_soc": {
                "type": "boolean",
                "description": "True if three closed nodal loops exist in kx=0, ky=0, kz=0 planes without SOC"
              }
            }
          }
        }
      },
      "description": "Scored artifact containing the DFT-computed electronic structure quantities for NbC and TaC: Fermi-level DOS, SOC splitting, and nodal loop presence."
    }
  ],
  "notes": "The checker compares each numeric value against paper-reported values with hidden tolerances and checks the boolean flags. The target_policy is exact_match because the quantities are fixed physical properties with no notion of 'better'."
}
```

## How you are scored
A hidden verifier will read your dft_results.json file and compare each of the six reported quantities (two compounds × three properties) against hidden reference values. Numeric values are checked with tolerances that allow for the legitimate spread between different DFT codes and pseudopotentials; the boolean flags are checked for correctness. Your total reward is a float between 0 and 1, proportional to the number of checks that pass. The verifier does not re-run any DFT calculations; it relies entirely on the accuracy of the numbers you report. You must therefore perform the full DFT calculations honestly and report the results as they come out of your computation.
