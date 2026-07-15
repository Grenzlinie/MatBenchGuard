# DFT binding energies of Zn on anatase TiO₂ and zinc metal surfaces

## Problem background
Rechargeable aqueous zinc-ion batteries suffer from uncontrolled dendrite growth on Zn anodes, causing short circuits and poor cycle life. One strategy is to apply a protective layer of TiO₂ that restricts dendrite growth. The effectiveness depends on the Zn affinity of the TiO₂ surface, which varies with crystal orientation. Understanding how Zn binds to different TiO₂ facets is essential for designing such layers. The task is to compute, using density functional theory (DFT), the binding energies of a Zn adatom on important low-index surfaces of anatase TiO₂ and on Zn metal surfaces, to assess the role of facet orientation in Zn affinity.

## Approach
Perform plane-wave DFT calculations using the GGA-PBE exchange-correlation functional with Grimme DFT-D dispersion correction (as applied in the paper's original calculations). Build five-layer 3×3 supercell slabs for anatase TiO₂ (001), (100), (101) and metallic Zn (001), (100). Relax the top three layers of each slab, then place one Zn adatom at the most stable adsorption site on each surface and relax again. Compute total energies for the clean slab (E_sub), isolated Zn atom (E_Zn), and slab+Zn (E_total). The binding energy is obtained as Eb = E_total − E_sub − E_Zn. The workflow must output these five binding energies, which quantify Zn affinity on each surface. The calculations can be performed with an open-source plane-wave DFT code such as Quantum ESPRESSO, using SSSP efficiency pseudopotentials for Ti, O, and Zn.

## Reproduction target
Your goal is to produce the five binding energies of a Zn adatom on the following surfaces: anatase TiO₂ (001), TiO₂ (100), TiO₂ (101), Zn (001), and Zn (100). Write the results to the file `/app/outputs/binding_energies.json` as a JSON object with keys `TiO2_001`, `TiO2_100`, `TiO2_101`, `Zn_001`, `Zn_100`, each value being a floating-point number in eV. This is a self-contained computational task; no external experimental data is needed. The task covers only the DFT binding energies; other experimental aspects of the paper (synthesis, electrochemical testing) are not part of the reproduction.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Anatase TiO2 lattice parameters
- Zinc metal lattice parameters

## Workflow steps

### Step 1: DFT calculation of Zn binding energies
- Role: scored (load-bearing)
- Action: Build 5-layer 3×3 supercell slabs for anatase TiO₂ (001), (100), (101) and metallic Zn (001), (100). Relax the top three layers of each slab. Place one Zn adatom at the most stable adsorption site on each surface and relax again. Use the GGA-PBE exchange-correlation functional with Grimme DFT-D dispersion correction to compute total energies (using an open-source plane-wave DFT code such as Quantum ESPRESSO). Extract the binding energy as Eb = E_total - E_sub - E_Zn for each surface. Output the five binding energies in eV.
- Output file: `/app/outputs/binding_energies.json`
- Format: json
- Contract: JSON object with keys: TiO2_001, TiO2_100, TiO2_101, Zn_001, Zn_100; each value is a float (binding energy in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/binding_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### binding_energies.json
- path: `/app/outputs/binding_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed binding energy of Zn on each surface.
- schema:
  - `type`: object
  - `required`:
    - `TiO2_001`: float
    - `TiO2_100`: float
    - `TiO2_101`: float
    - `Zn_001`: float
    - `Zn_100`: float
  - `description`: Binding energy values in eV.

Notes: The checker compares the submitted binding energies to reference values and validates the relative ordering trend (Zn affinity higher on (100) than on Zn surfaces, which in turn are higher than on (001) and (101)).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "TiO2_001": "float",
          "TiO2_100": "float",
          "TiO2_101": "float",
          "Zn_001": "float",
          "Zn_100": "float"
        },
        "description": "Binding energy values in eV."
      },
      "description": "Computed binding energy of Zn on each surface."
    }
  ],
  "notes": "The checker compares the submitted binding energies to reference values and validates the relative ordering trend (Zn affinity higher on (100) than on Zn surfaces, which in turn are higher than on (001) and (101))."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/binding_energies.json`. It first checks that the file is a valid JSON with the required structure (all five keys present, each value a float). Then it compares each binding energy to hidden reference values (derived from the paper's reported numbers) with an allowed tolerance. In addition, it verifies that the computed energies satisfy a specific relative ordering among the surfaces (e.g., some facets must show higher Zn affinity than others, and some must be lower than the Zn surfaces). The verifier does not reveal the reference values or the tolerance; it only evaluates whether your submitted numbers are physically consistent and within the expected range. The final score is computed from these comparisons. To succeed, you must faithfully execute the described DFT protocol; simply reporting arbitrary numbers will not pass the structural trend check.
