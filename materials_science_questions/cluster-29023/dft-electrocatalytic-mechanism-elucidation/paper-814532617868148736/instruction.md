# DFT Water Adsorption on CoCr2O4 (111) Surfaces

## Problem background
Electrocatalytic oxygen evolution reaction (OER) is critical for energy conversion devices like water electrolysers and metal-air batteries. Spinel-type binary metal oxides such as CoCr2O4 are promising earth-abundant OER catalysts, but their performance is often limited by poor electrical conductivity. Anchoring CoCr2O4 nanocrystals on conductive carbon nanosheets (CNS) creates a strongly coupled composite that exhibits superior OER activity. Understanding the origin of this enhancement requires examining how the interaction between CoCr2O4 and CNS alters the surface chemistry, in particular the availability of low-coordinated surface oxygen atoms that can bind water molecules – a key step in OER. This task investigates the water adsorption properties of two CoCr2O4 (111) surface terminations, one rich in low-coordinated O2 atoms and one without, by computing their adsorption energies from first-principles.

## Approach
We use spin-polarised density functional theory (DFT) calculations to compare the binding of a single water molecule on two CoCr2O4 (111) surface models. The first model (with_O2) exposes low-coordinated surface oxygen atoms (O2), while the second model (without_O2) represents a stoichiometric termination lacking those atoms. For each surface, a periodic slab is constructed from the bulk cubic spinel crystal structure. After relaxing the clean slab, one water molecule is adsorbed and the combined system is relaxed. The adsorption energy is computed as E_ads = E(slab+H2O) - E(slab) - E_H2O, where E_H2O is the energy of an isolated water molecule in the same supercell. The calculations employ the open-source plane-wave DFT code Quantum ESPRESSO with pseudopotentials describing core electrons. The resulting adsorption energies quantify the effect of surface oxygen coordination on water binding strength.

## Reproduction target
Compute the adsorption energy of a single water molecule on the two CoCr2O4 (111) surface models described above (with_O2 and without_O2). Output the energies (in eV) in a single JSON file at /app/outputs/adsorption_energies.json containing an object with key "surfaces" that is an array of two objects, each with keys "type" (either "with_O2" or "without_O2") and "E_ads_eV" (the computed adsorption energy as a floating-point number).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for Co, Cr, O, H: http://pseudos.quantum-espresso.org/home
- CoCr2O4 crystal structure (cubic spinel): JCPDS 80-1668
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: DFT water adsorption calculation
- Role: scored (load-bearing)
- Action: Construct periodic slab models of the CoCr2O4 (111) surface with and without low‑coordinated surface O2 atoms from the public bulk crystal structure. For each surface, run spin‑polarized DFT calculations (Quantum ESPRESSO) to obtain the total energy of the clean slab, the slab with one adsorbed H2O molecule, and an isolated H2O molecule in the same supercell. Compute the adsorption energy E_ads = E(slab+H2O) - E(slab) - E_H2O for both surfaces. Write the two energies (in eV) to adsorption_energies.json.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"surfaces": [{"type": "with_O2", "E_ads_eV": float}, {"type": "without_O2", "E_ads_eV": float}]}
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
- target_policy: reference_match
- description: JSON file containing the DFT‑computed water adsorption energies (in eV) for the two CoCr2O4(111) surface models.
- schema:
  - `type`: object
  - `required`: `surfaces`
  - `properties`:
    - `surfaces`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `type`, `E_ads_eV`
        - `properties`:
          - `type`:
            - `type`: string
          - `E_ads_eV`:
            - `type`: number
  - `units`:
    - `E_ads_eV`: eV

Notes: The hidden reference values are the paper‑reported adsorption energies (−0.74 eV for the surface with low‑coordinated O2, −0.54 eV for the surface without). The checker verifies both values within a tolerance, ensures the correct monotonic ordering (more negative for the O2‑terminated surface), and checks that the ratio E_ads(with_O2)/E_ads(without_O2) ≤ 0.8 to confirm the claimed stronger binding.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "surfaces"
        ],
        "properties": {
          "surfaces": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "type",
                "E_ads_eV"
              ],
              "properties": {
                "type": {
                  "type": "string"
                },
                "E_ads_eV": {
                  "type": "number"
                }
              }
            }
          }
        },
        "units": {
          "E_ads_eV": "eV"
        }
      },
      "description": "JSON file containing the DFT‑computed water adsorption energies (in eV) for the two CoCr2O4(111) surface models."
    }
  ],
  "notes": "The hidden reference values are the paper‑reported adsorption energies (−0.74 eV for the surface with low‑coordinated O2, −0.54 eV for the surface without). The checker verifies both values within a tolerance, ensures the correct monotonic ordering (more negative for the O2‑terminated surface), and checks that the ratio E_ads(with_O2)/E_ads(without_O2) ≤ 0.8 to confirm the claimed stronger binding."
}
```

## How you are scored
A hidden verifier will read your adsorption_energies.json and compare the reported adsorption energies against hidden reference values. It will also check that the relative difference between the two surfaces is physically consistent with the expected role of low-coordinated surface oxygen atoms. The score reflects how well your computed energies match the hidden targets (within DFT-related uncertainties) and whether the correct qualitative trend is observed. Providing numbers that happen to match the paper is not sufficient; the verifier expects values consistent with an honest first-principles calculation.
