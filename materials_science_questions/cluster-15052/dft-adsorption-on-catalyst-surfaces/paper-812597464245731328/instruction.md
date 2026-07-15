# DFT Reproduction of Sodium-Promoted NO Adsorption on Char Surfaces

## Problem background
In coal combustion, sodium present in high-alkali coal can influence the heterogeneous reduction of NO by char. Understanding how sodium atoms affect the adsorption of NO molecules on char surfaces is important for developing clean combustion technologies. This task reproduces a computational study that uses density functional theory (DFT) to compute the adsorption energies of NO on several char surface models decorated with sodium atoms. The objective is to determine whether sodium promotes or alters the adsorption, and to classify each adsorption as physisorption or chemisorption based on the computed energies.

## Approach
The method relies on spin-polarized DFT calculations with the GGA-PBE exchange-correlation functional and a DFT-D dispersion correction. Three char structure models are used: a saturated graphene flake (G) and two unsaturated edge models with armchair (A) and zigzag (Z) terminations, all hydrogen-terminated. First, the total energies of an isolated Na atom, an isolated NO molecule, and the three clean char substrates are computed. Then a single Na atom is placed on the hollow site of each char model and the systems are optimized to obtain the Na-adsorbed complex energies. Next, NO is adsorbed on the bare char models at the most stable site (side-on hollow for A and Z; the lowest-energy orientation is selected for G), yielding the NO-char complex energies. Finally, NO is adsorbed on the Na-loaded char models at the most stable site (N-down on top of Na for G@Na; side-on hollow for A@Na and Z@Na, with the lowest-energy ortho position chosen for the edge models) to obtain the energies of the fully loaded complexes. Adsorption energies are then derived as the difference between the complex energy and the sum of the isolated component energies. By examining how the adsorption energies change when sodium is present and comparing them to a standard energy threshold, one can determine whether each adsorption is physisorption or chemisorption and assess the catalytic role of sodium.

## Reproduction target
Compute the total energies (including zero-point energy correction) of the 13 systems specified in the output contract: isolated Na, isolated NO, clean G, A, Z, Na-adsorbed G, A, Z, NO on bare G, A, Z, and NO on Na-loaded G, A, Z. Assemble these total energies in kJ/mol into the JSON file `/app/outputs/total_energies.json` following the key naming and schema defined in the output contract. The hidden verifier will use these total energies to calculate all relevant adsorption energies and to classify each adsorption as physisorption or chemisorption. It will then assess the correctness of the derived values and classifications by comparing them to reference expectations and by checking whether qualitative trends that distinguish the role of sodium and the differences between char edge types are reproduced.

## Assets

- Quantum ESPRESSO (DFT code): https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials (efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build char models
- Role: process
- Action: Construct the three char models: saturated graphene G (C54H18), armchair edge A (C24H8), and zigzag edge Z (C22H9). Generate hydrogen-terminated atomic coordinates and save them in a format suitable for DFT input (e.g., XYZ).
- Evidence: `/app/outputs/char_models.xyz`

### Step 2: Compute energies of isolated species and clean substrates
- Role: process
- Action: Perform spin-polarized DFT geometry optimization (GGA-PBE with dispersion correction) for an isolated Na atom, an isolated NO molecule, and the three clean char substrates G, A, Z. Extract total energies including zero-point energy correction.
- Evidence: `/app/outputs/isolate_energies_temp.json`

### Step 3: Na doping on hollow sites
- Role: process
- Action: Place a single Na atom on the hollow site of each char model (G, A, Z) and perform full geometry optimization. Record total energies (including ZPE) of the Na-doped complexes G@Na, A@Na, Z@Na.
- Evidence: `/app/outputs/na_doped_energies_temp.json`

### Step 4: NO adsorption on bare char
- Role: process
- Action: For the bare char models G, A, Z, optimize NO adsorption at the most stable site (side-on hollow for A and Z; for G test N-down, O-down, side-on and choose the lowest energy). Record total energies (with ZPE) of the NO-char complexes G-NO, A-NO, Z-NO.
- Evidence: `/app/outputs/no_bare_energies_temp.json`

### Step 5: NO adsorption on Na-loaded char
- Role: process
- Action: For the Na-loaded char models G@Na, A@Na, Z@Na, optimize NO adsorption at the most stable site (N-down on top of Na for G@Na; side-on hollow for A@Na and Z@Na, choosing the ortho position with lowest energy). Record total energies (with ZPE) of the complexes G@Na-NO, A@Na-NO, Z@Na-NO.
- Evidence: `/app/outputs/no_naloaded_energies_temp.json`

### Step 6: Assemble total energies for scoring
- Role: scored (load-bearing)
- Action: Collect all total energies (including ZPE) from the preceding calculations and write them into /app/outputs/total_energies.json. The JSON must contain the total energy (kJ/mol) for each of the 13 systems: Na, NO, G, A, Z, G_Na, A_Na, Z_Na, G_NO, A_NO, Z_NO, G_Na_NO, A_Na_NO, Z_Na_NO.
- Output file: `/app/outputs/total_energies.json`
- Format: json
- Contract: {
  "type": "object",
  "properties": {
    "Na": {"type": "number", "description": "Total energy (kJ/mol) of isolated Na atom including ZPE"},
    "NO": {"type": "number", "description": "Total energy (kJ/mol) of isolated NO molecule including ZPE"},
    "G": {"type": "number", "description": "Total energy (kJ/mol) of clean G substrate including ZPE"},
    "A": {"type": "number", "description": "Total energy (kJ/mol) of clean A substrate including ZPE"},
    "Z": {"type": "number", "description": "Total energy (kJ/mol) of clean Z substrate including ZPE"},
    "G_Na": {"type": "number", "description": "Total energy of G with Na at hollow site"},
    "A_Na": {"type": "number", "description": "Total energy of A with Na at hollow site"},
    "Z_Na": {"type": "number", "description": "Total energy of Z with Na at hollow site"},
    "G_NO": {"type": "number", "description": "Total energy of G with NO at most stable site"},
    "A_NO": {"type": "number", "description": "Total energy of A with NO at hollow side-on site"},
    "Z_NO": {"type": "number", "description": "Total energy of Z with NO at hollow side-on site"},
    "G_Na_NO": {"type": "number", "description": "Total energy of G@Na with NO at most stable site"},
    "A_Na_NO": {"type": "number", "description": "Total energy of A@Na with NO at hollow side-on site"},
    "Z_Na_NO": {"type": "number", "description": "Total energy of Z@Na with NO at hollow side-on site"}
  },
  "required": ["Na","NO","G","A","Z","G_Na","A_Na","Z_Na","G_NO","A_NO","Z_NO","G_Na_NO","A_Na_NO","Z_Na_NO"]
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.json
- path: `/app/outputs/total_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Aggregated total energies (kJ/mol, including ZPE) for all 13 systems used to derive adsorption energies and classify the adsorption type. The checker will recompute adsorption energies from these values and compare them to the paper's reference values with tolerances to assess correctness.
- schema:
  - `type`: object
  - `properties`:
    - `Na`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of isolated Na atom including ZPE
    - `NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of isolated NO molecule including ZPE
    - `G`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of clean G substrate including ZPE
    - `A`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of clean A substrate including ZPE
    - `Z`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of clean Z substrate including ZPE
    - `G_Na`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of G with Na at hollow site
    - `A_Na`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of A with Na at hollow site
    - `Z_Na`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of Z with Na at hollow site
    - `G_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of G with NO at most stable site
    - `A_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of A with NO at hollow side-on site
    - `Z_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of Z with NO at hollow side-on site
    - `G_Na_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of G@Na with NO at most stable site
    - `A_Na_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of A@Na with NO at hollow side-on site
    - `Z_Na_NO`:
      - `type`: number
      - `unit`: kJ/mol
      - `description`: Total energy of Z@Na with NO at hollow side-on site
  - `required`: `Na`, `NO`, `G`, `A`, `Z`, `G_Na`, `A_Na`, `Z_Na`, `G_NO`, `A_NO`, `Z_NO`, `G_Na_NO`, `A_Na_NO`, `Z_Na_NO`

Notes: The task uses T0 result-level comparison: the agent reports total energies, and the hidden checker derives adsorption energies E_ads = E(AB) - E(A) - E(B) and compares them against the paper's reported values (with tolerances). Trend and classification checks are also performed. The agent must compute the total energies using DFT with settings equivalent to GGA-PBE with dispersion correction. The solving agent may need substantial external compute resources to run the 13 geometry optimizations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "Na": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of isolated Na atom including ZPE"
          },
          "NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of isolated NO molecule including ZPE"
          },
          "G": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of clean G substrate including ZPE"
          },
          "A": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of clean A substrate including ZPE"
          },
          "Z": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of clean Z substrate including ZPE"
          },
          "G_Na": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of G with Na at hollow site"
          },
          "A_Na": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of A with Na at hollow site"
          },
          "Z_Na": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of Z with Na at hollow site"
          },
          "G_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of G with NO at most stable site"
          },
          "A_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of A with NO at hollow side-on site"
          },
          "Z_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of Z with NO at hollow side-on site"
          },
          "G_Na_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of G@Na with NO at most stable site"
          },
          "A_Na_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of A@Na with NO at hollow side-on site"
          },
          "Z_Na_NO": {
            "type": "number",
            "unit": "kJ/mol",
            "description": "Total energy of Z@Na with NO at hollow side-on site"
          }
        },
        "required": [
          "Na",
          "NO",
          "G",
          "A",
          "Z",
          "G_Na",
          "A_Na",
          "Z_Na",
          "G_NO",
          "A_NO",
          "Z_NO",
          "G_Na_NO",
          "A_Na_NO",
          "Z_Na_NO"
        ]
      },
      "description": "Aggregated total energies (kJ/mol, including ZPE) for all 13 systems used to derive adsorption energies and classify the adsorption type. The checker will recompute adsorption energies from these values and compare them to the paper's reference values with tolerances to assess correctness."
    }
  ],
  "notes": "The task uses T0 result-level comparison: the agent reports total energies, and the hidden checker derives adsorption energies E_ads = E(AB) - E(A) - E(B) and compares them against the paper's reported values (with tolerances). Trend and classification checks are also performed. The agent must compute the total energies using DFT with settings equivalent to GGA-PBE with dispersion correction. The solving agent may need substantial external compute resources to run the 13 geometry optimizations."
}
```

## How you are scored
Your submitted `/app/outputs/total_energies.json` is read by a hidden verifier that independently computes all adsorption energies from your reported total energies. These derived adsorption energies are compared against hidden reference values using tolerances that account for typical differences between DFT implementations. In addition, the verifier checks whether the computed adsorption energies satisfy expected qualitative trends: the relative ordering of adsorption strengths across different char models, whether each adsorption is classified as physisorption or chemisorption according to a standard energy criterion, and whether the presence of sodium significantly alters the adsorption behavior on each char type. The overall reward is a weighted combination of these absolute-value and trend/classification checks, with the main emphasis on the adsorption energy values and the classification outcomes. The verifier does not simply approve a self-reported number; it re-derives the quantities it scores from your raw total energies.
