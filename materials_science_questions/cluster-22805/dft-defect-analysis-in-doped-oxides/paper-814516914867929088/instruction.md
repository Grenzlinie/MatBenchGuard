# DFT study of Ti-Ce co-doped AlN: structural and magnetic properties

## Problem background
Diluted magnetic semiconductors (DMS) based on III-nitrides co-doped with transition metals (TM) and rare earth (RE) elements are promising for spintronic devices. The exchange interactions between localized 3d and 4f electrons can induce high-temperature ferromagnetism, but their nature is not well understood. AlN is a wide-bandgap semiconductor with a stable wurtzite structure; Ti ‑Ce co‑doping introduces 3d¹ and 4f¹ electrons, making it a model system to study 3d‑4f coupling. The main experimental quantities of interest are formation energies, relaxed lattice constants, magnetic moments, and the relative stability of ferromagnetic (FM) versus antiferromagnetic (AFM) spin ordering for different dopant separations and concentrations. Computing these quantities from first principles provides insight into both the thermodynamic stability and the magnetic ground state.

## Approach
The method uses spin-polarized density functional theory (DFT) with the GGA‑PBE exchange‑correlation functional and on‑site Hubbard U corrections (U_Ti = 4.4 eV, U_Ce = 5.4 eV) to describe strongly correlated 3d and 4f states. Three supercell models are built from the wurtzite AlN primitive cell (experimental lattice constants a = 3.11 Å, c = 4.98 Å, space group P6₃mc): two 32‑atom cells (Al₁₄Ti₁Ce₁N₁₆) with Ti–Ce inter‑dopant distances of 2.923 Å and 5.697 Å, and one 64‑atom cell (Al₃₀Ti₁Ce₁N₃₂) with the nearest‑neighbor distance 2.923 Å. Each supercell is fully relaxed (ions, cell shape, and volume) in both the FM and AFM spin configurations. From the relaxed structures and total energies, the formation energy, final lattice parameters a and c, exchange energy ΔE = E_AFM − E_FM, and total magnetic moment are extracted. The sign of ΔE indicates the magnetic ground state; the relative magnitude of the formation energies indicates thermodynamic preference among configurations.

## Reproduction target
Using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and GGA‑PBE pseudopotentials with the Hubbard U values above, perform the DFT relaxations for the three supercell configurations, then compile the results into `/app/outputs/results.json`. The JSON file must contain an array of three objects, one per configuration, with keys: `structure` (string identifying the configuration as “Al14Ti1Ce1N16_d2.923”, “Al14Ti1Ce1N16_d5.697”, or “Al30Ti1Ce1N32_d2.923”), `E_f` (formation energy in eV), `a` and `c` (relaxed lattice constants in Å), `delta_E` (exchange energy ΔE in eV), and `M_total` (total magnetic moment in μ_B). The values must be derived from your own DFT calculations; do not simply copy reference numbers.

## Assets

- Wurtzite AlN crystal structure and experimental lattice constants: 10.1016/0038-1098(77)91340-0
- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials for Al, N, Ti, Ce: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Build doped supercell structures
- Role: process
- Action: Construct the initial (unrelaxed) wurtzite AlN supercells for the three Ti-Ce co-doped configurations: (i) a 32-atom supercell Al14Ti1Ce1N16 with Ti and Ce at nearest-neighbor Al sites (d=2.923 Å), (ii) the same 32-atom cell with next-nearest separation (d=5.697 Å), and (iii) a 64-atom supercell Al30Ti1Ce1N32 with nearest-neighbor separation (d=2.923 Å). Use the experimental lattice constants a=3.11 Å and c=4.98 Å as starting parameters.
- Evidence: `/app/outputs/supercell_structures.json`

### Step 2: Run DFT structure relaxation and total energy calculations
- Role: process
- Action: For each of the three supercells, perform spin-polarized DFT calculations using GGA-PBE with Hubbard U corrections (U_Ti=4.4 eV, U_Ce=5.4 eV). Run full structural relaxations (ions, cell shape, and volume) for both ferromagnetic (FM) and antiferromagnetic (AFM) spin alignments. Compute the total energies, relaxed lattice constants (a, c), and total magnetic moments for each configuration. Additionally, compute the total energy of the pure (undoped) AlN supercell of the same size (Al16N16 for the 32‑atom cell and Al32N32 for the 64‑atom cell) and the total energies of elemental bulk Ti and Ce (hcp Ti and γ‑Ce) using identical DFT parameters, to obtain the reference energies needed for the formation energy definition.
- Evidence: none

### Step 3: Extract and report target quantities
- Role: scored (load-bearing)
- Action: From the DFT outputs, extract for each of the three co-doped configurations the formation energy E_f (eV), relaxed lattice parameters a and c (Å), exchange energy ΔE = E_AFM − E_FM (eV), and total magnetic moment M_total (μ_B). The formation energy is defined as E_f = E_total(doped) − E_total(pure AlN supercell of the same size) − μ_Ti − μ_Ce + 2μ_Al, where μ_Ti and μ_Ce are the total energies per atom of Ti and Ce in their bulk reference phases (hcp Ti and γ‑Ce), and μ_Al is the total energy per Al atom in bulk fcc Al. Compile these values into a JSON file as specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of three objects. Each object has keys: 'structure' (string), 'E_f' (number, eV), 'a' (number, Å), 'c' (number, Å), 'delta_E' (number, eV), 'M_total' (number, μ_B).
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
- target_policy: exact_match
- description: Array of three objects, one per co-doped configuration, reporting formation energy, relaxed lattice constants, exchange energy, and total magnetic moment, all computed from the DFT calculations. The hidden checker compares these values to the paper's reference numbers using specified tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `structure`, `E_f`, `a`, `c`, `delta_E`, `M_total`
    - `properties`:
      - `structure`:
        - `type`: string
      - `E_f`:
        - `type`: number
        - `unit`: eV
      - `a`:
        - `type`: number
        - `unit`: Å
      - `c`:
        - `type`: number
        - `unit`: Å
      - `delta_E`:
        - `type`: number
        - `unit`: eV
      - `M_total`:
        - `type`: number
        - `unit`: μ_B

Notes: The reported values are derived from DFT; tolerances absorb legitimate implementation differences. Structure strings must exactly match the listed names in the description.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "structure",
            "E_f",
            "a",
            "c",
            "delta_E",
            "M_total"
          ],
          "properties": {
            "structure": {
              "type": "string"
            },
            "E_f": {
              "type": "number",
              "unit": "eV"
            },
            "a": {
              "type": "number",
              "unit": "Å"
            },
            "c": {
              "type": "number",
              "unit": "Å"
            },
            "delta_E": {
              "type": "number",
              "unit": "eV"
            },
            "M_total": {
              "type": "number",
              "unit": "μ_B"
            }
          }
        }
      },
      "description": "Array of three objects, one per co-doped configuration, reporting formation energy, relaxed lattice constants, exchange energy, and total magnetic moment, all computed from the DFT calculations. The hidden checker compares these values to the paper's reference numbers using specified tolerances."
    }
  ],
  "notes": "The reported values are derived from DFT; tolerances absorb legitimate implementation differences. Structure strings must exactly match the listed names in the description."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `/app/outputs/results.json` and compares each reported quantity (formation energies, lattice constants, exchange energies, magnetic moments) against a set of reference values. The verifier also checks the relative ordering of the formation energies among the three configurations. Each field contributes to the final score; partial credit is possible. The reward is a weighted sum across all scored criteria. To earn full credit, your DFT calculations must accurately follow the specified protocol and produce results that fall within the verifier’s acceptance windows. Simply reporting numbers that happen to match without performing the computations will not succeed because the verifier’s tolerances are calibrated to the spread of correct re‑runs.
