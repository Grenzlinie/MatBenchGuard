# DFT formation energy and heat of mixing of Zr-Sn-Nb alloys

## Problem background
In zirconium alloys used in nuclear applications, the surface segregation of Sn can influence oxidation and corrosion behavior. Experiments suggest that Nb addition enhances Sn surface segregation, but the thermodynamic origin of this enhancement is not fully understood. First-principles calculations can help clarify the energetic interactions among Sn, Nb, and the Zr matrix by quantifying the heat of mixing of Zr–Sn–Nb alloys.

## Approach
Density functional theory (DFT) with the PBE exchange-correlation functional is used. A 3×3×3 supercell of hexagonal close-packed (hcp) α‑Zr (54 atoms) serves as the base. Substitutional defects are created by replacing one or two Zr atoms with Sn and/or Nb, yielding models for Zr₅₃Sn₁, Zr₅₃Nb₁, and Zr₅₂Sn₁Nb₁. For the ternary case, two configurations are investigated: Sn and Nb as nearest neighbours along the a‑axis and along the c‑axis. Bulk reference phases (β‑Sn and bcc Nb) are also computed. Total energies from DFT are combined using standard heat‑of‑mixing definitions to assess the energetic preference for Sn–Nb clustering in the α‑Zr matrix.

## Reproduction target
Compute the four heat of mixing values (in eV) for the supercells Zr₅₃Sn₁, Zr₅₃Nb₁, and Zr₅₂Sn₁Nb₁ with Sn and Nb as nearest neighbours along the a‑axis and along the c‑axis, using DFT with the PBE functional and a 3×3×3 supercell of hcp α‑Zr. The calculation uses formulas that involve the total energies of the defective supercells and the cohesive energies of β‑Sn and bcc Nb. Output the results in /app/outputs/heat_of_mixing.json with keys 'Zr53Sn1_Em', 'Zr53Nb1_Em', 'Zr52Sn1Nb1_a_Em', 'Zr52Sn1Nb1_c_Em'.

## Assets

- Open‑source DFT software (e.g., Quantum ESPRESSO, GPAW): https://www.quantum-espresso.org/
- PAW pseudopotentials for Zr, Sn, Nb (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency
- Reference crystal structures (α‑Zr, β‑Sn, bcc Nb)

## Workflow steps

### Step 1: Generate DFT input files for all supercells and reference phases
- Role: process
- Action: Build a 3×3×3 hcp α‑Zr supercell (54 atoms). Generate input structures for the defective supercells: Zr₅₃Sn₁ (replace one Zr by Sn), Zr₅₃Nb₁ (replace one Zr by Nb), and Zr₅₂Sn₁Nb₁ with Sn and Nb as nearest neighbours along the a‑axis and along the c‑axis. Also prepare input cells for bulk β‑Sn and bcc Nb. Create appropriate DFT input files for the chosen open‑source code (e.g., Quantum ESPRESSO pw.x input).
- Evidence: none

### Step 2: Run DFT total energy calculations
- Role: process
- Action: Perform DFT total energy calculations for all prepared supercells (Zr₅₄ reference, Zr₅₃Sn₁, Zr₅₃Nb₁, Zr₅₂Sn₁Nb₁ a‑direction, Zr₅₂Sn₁Nb₁ c‑direction) and for the bulk reference phases (β‑Sn and bcc Nb). Use the PBE exchange‑correlation functional, a plane‑wave cutoff of at least 400 eV, and a sufficiently dense k‑point mesh (e.g., equivalent to 5×5×5 for the supercell). Save the final total energy for each system to a JSON file (dft_energies.json) with keys: 'Zr54', 'Zr53Sn1', 'Zr53Nb1', 'Zr52Sn1Nb1_a', 'Zr52Sn1Nb1_c', 'beta_Sn', 'bcc_Nb'.
- Evidence: `/app/outputs/dft_energies.json`

### Step 3: Compute heat of mixing
- Role: scored (load-bearing)
- Action: Read the total energies from the DFT run evidence (dft_energies.json). Compute the four heat of mixing values using the following formulas, where N=54 (total atoms in the perfect supercell) and the keys refer to <code>dft_energies.json</code>:

  - Em(Sn→Zr) = E(Zr53Sn1) - (53/54)*E(Zr54) - E(beta_Sn)
  - Em(Nb→Zr) = E(Zr53Nb1) - (53/54)*E(Zr54) - E(bcc_Nb)
  - Em(Sn,Nb→Zr a) = E(Zr52Sn1Nb1_a) - (52/54)*E(Zr54) - E(beta_Sn) - E(bcc_Nb)
  - Em(Sn,Nb→Zr c) = E(Zr52Sn1Nb1_c) - (52/54)*E(Zr54) - E(beta_Sn) - E(bcc_Nb)

  Write the results to /app/outputs/heat_of_mixing.json with keys 'Zr53Sn1_Em', 'Zr53Nb1_Em', 'Zr52Sn1Nb1_a_Em', 'Zr52Sn1Nb1_c_Em'; each value is a float in eV.
- Output file: `/app/outputs/heat_of_mixing.json`
- Format: json
- Contract: object with keys Zr53Sn1_Em, Zr53Nb1_Em, Zr52Sn1Nb1_a_Em, Zr52Sn1Nb1_c_Em; all values are floats in eV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_of_mixing.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_of_mixing.json
- path: `/app/outputs/heat_of_mixing.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The four heat of mixing values computed from DFT total energies; they are compared directly to hidden reference values.
- schema:
  - `type`: object
  - `required_keys`: `Zr53Sn1_Em`, `Zr53Nb1_Em`, `Zr52Sn1Nb1_a_Em`, `Zr52Sn1Nb1_c_Em`
  - `value_type`: float
  - `unit`: eV

Notes: The hidden checker directly compares the agent's reported heat_of_mixing.json values against hidden reference values. There is no recomputation from raw DFT energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_of_mixing.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "Zr53Sn1_Em",
          "Zr53Nb1_Em",
          "Zr52Sn1Nb1_a_Em",
          "Zr52Sn1Nb1_c_Em"
        ],
        "value_type": "float",
        "unit": "eV"
      },
      "description": "The four heat of mixing values computed from DFT total energies; they are compared directly to hidden reference values."
    }
  ],
  "notes": "The hidden checker directly compares the agent's reported heat_of_mixing.json values against hidden reference values. There is no recomputation from raw DFT energies."
}
```

## How you are scored
A hidden verifier compares the values in `/app/outputs/heat_of_mixing.json` against hidden expected values, within a tolerance. Your score is the fraction of values that fall within the tolerance.
