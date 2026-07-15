# Adsorption of Group-IVA Atoms on Graphene: DFT Reproducibility Task

## Problem background
Graphene's exceptional electronic properties can be tailored by adsorbing individual atoms. The adsorption of group-IVA atoms (C, Si, Ge, Sn, Pb) is of particular interest because these atoms span from non-metals to metals and may induce magnetic moments, modify the graphene structure, and change its electronic character. This task investigates how the adsorption energy, local geometry distortion, bond length, and magnetic moment depend on the adsorbate species and the adsorption site (top, bridge, hollow) using first-principles calculations. The goal is to determine quantitative adsorption properties that can guide experimental efforts to functionalize graphene.

## Approach
The approach employs density functional theory (DFT) within the generalized gradient approximation (GGA) using the PBE exchange-correlation functional and the projector augmented wave (PAW) method. The core protocol involves three sets of calculations: (i) isolated atom calculations for each group-IVA adsorbate to obtain reference total energies E_a; (ii) a pristine graphene supercell calculation to obtain its total energy E_g; and (iii) for each atom and each high-symmetry adsorption site (top, bridge, hollow), spin-polarized geometry relaxations of the adsorbate+graphene system to obtain the total energy E_ag and the relaxed geometry. The adsorption energy is defined as E_ad = E_ag - (E_a + E_g). From the relaxed configurations, the graphene height distortion Δh (maximum minus minimum z-coordinate of all graphene carbon atoms), the nearest adsorbate–carbon bond length d_ac, and the total magnetic moment M are extracted. The calculations are performed using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with pseudopotentials from public libraries. All results are aggregated into a single JSON file that reports the four quantities for every atom/site combination.

## Reproduction target
Compute the adsorption energy E_ad (eV), the graphene height distortion Δh (Å), the adsorbate–carbon bond length d_ac (Å), and the total magnetic moment M (μ_B) for every combination of group-IVA atom (C, Si, Ge, Sn, Pb) and adsorption site (top, bridge, hollow). Report all values in a single JSON file named `adsorption_results.json` under `/app/outputs`, following the nested JSON schema described in the output contract. The calculations must follow the spin-polarized DFT protocol described in the workflow steps, using an open-source plane-wave DFT code and publicly available PBE PAW pseudopotentials. The output must contain exactly these four quantities per combination; no other artifacts or plots are required.

## Assets

- Quantum ESPRESSO plane-wave DFT code: https://www.quantum-espresso.org/
- PBE PAW pseudopotentials for C, Si, Ge, Sn, Pb: https://www.materialscloud.org/discover/sssp/table/efficiency
- Graphene primitive cell structure

## Workflow steps

### Step 1: Build graphene supercell
- Role: process
- Action: Construct a 4×4×1 supercell of graphene from the primitive cell with in-plane lattice constant 9.88 Å and out-of-plane vacuum 15.00 Å. Output the atomic coordinates in a format suitable for the chosen DFT code.
- Evidence: `/app/outputs/supercell_structure.txt`

### Step 2: Reference isolated atom energies E_a
- Role: process
- Action: For each adsorbate element (C, Si, Ge, Sn, Pb), perform a spin-polarized DFT single-point energy calculation in a cubic supercell of side length 15 Å, sampling only the Γ point. Use the PBE functional and the corresponding PAW pseudopotential. Record the total energy E_a for each atom.
- Evidence: `/app/outputs/isolated_atom_energies.txt`

### Step 3: Reference graphene total energy E_g
- Role: process
- Action: Perform a spin-polarized DFT single-point energy calculation on the relaxed pristine graphene supercell using the same PBE-PAW pseudopotentials. Use a k-point mesh appropriate for the supercell. Record the total energy E_g.
- Evidence: `/app/outputs/graphene_energy.txt`

### Step 4: Relax all adsorbate–graphene configurations
- Role: process
- Action: For each IVA atom (C, Si, Ge, Sn, Pb) and each adsorption site (top, bridge, hollow), set up an initial geometry with the adsorbate placed 2.0 Å above the site on the graphene supercell. Perform a spin-polarized DFT geometry relaxation using the PBE-PAW setup until forces on all atoms are below the standard convergence threshold. Save the relaxed structure and total energy E_ag for every configuration.
- Evidence: none

### Step 5: Compile and output adsorption results
- Role: scored (load-bearing)
- Action: For each atom/site combination, compute: (1) adsorption energy E_ad = E_ag - (E_a + E_g); (2) graphene height distortion Δh = max(z_C) - min(z_C) among all graphene carbon atoms; (3) adsorbate–carbon bond length d_ac = distance between adsorbate and its nearest carbon atom; (4) total magnetic moment M (in μ_B). Collect all values and write a JSON file with the schema specified in the output contract.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: { "C": { "T": { "E_ad": <float>, "delta_h": <float>, "d_ac": <float>, "M": <float> }, "B": {...}, "H": {...} }, "Si": {...}, "Ge": {...}, "Sn": {...}, "Pb": {...} }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains the computed adsorption energy E_ad (eV), graphene height distortion Δh (Å), adsorbate–carbon bond length d_ac (Å), and total magnetic moment M (μ_B) for each combination of group-IVA atom (C, Si, Ge, Sn, Pb) and adsorption site (T, B, H).
- schema:
  - `type`: object
  - `required`:
    - `C`: object
    - `Si`: object
    - `Ge`: object
    - `Sn`: object
    - `Pb`: object
  - `items`: object

Notes: Only the numerical values in this JSON file are scored; DOS and spin-density figures are not required. The checker compares the agent's reported values to the paper's published reference using per-quantity tolerances and also verifies qualitative adsorption-site trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C": "object",
          "Si": "object",
          "Ge": "object",
          "Sn": "object",
          "Pb": "object"
        },
        "items": {}
      },
      "description": "Contains the computed adsorption energy E_ad (eV), graphene height distortion Δh (Å), adsorbate–carbon bond length d_ac (Å), and total magnetic moment M (μ_B) for each combination of group-IVA atom (C, Si, Ge, Sn, Pb) and adsorption site (T, B, H)."
    }
  ],
  "notes": "Only the numerical values in this JSON file are scored; DOS and spin-density figures are not required. The checker compares the agent's reported values to the paper's published reference using per-quantity tolerances and also verifies qualitative adsorption-site trends."
}
```

## How you are scored
A hidden verifier reads your `adsorption_results.json` and compares each reported quantity (E_ad, delta_h, d_ac, M) against reference values derived from a correct execution of the same DFT protocol. The comparison uses tolerance-based checks that accept small numerical differences between implementations. Additionally, the verifier checks that the relative ordering of adsorption energies among the top, bridge, and hollow sites for each atom species matches the expected system-specific trends. The scoring weights are highest for the adsorption energy, with the other three quantities contributing equal but smaller shares. The final reward is a weighted sum of the per-quantity and per-system scores, expressed as a value between 0 and 1.
