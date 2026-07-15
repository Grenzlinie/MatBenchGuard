# Bond Reactivity Reversal of Si-H and Si-Si on SiO2 Surface

## Problem background
Silane (SiH₄) and disilane (Si₂H₆) are important precursor gases for the chemical vapor deposition (CVD) of silicon films on oxidized silicon surfaces, a key process in semiconductor device fabrication. The detailed decomposition mechanisms on amorphous SiO₂ surfaces are not fully characterized. A central question is whether the intrinsic bond strengths (e.g., Si–H versus Si–Si) as measured by gas-phase bond dissociation enthalpies predict the relative ease of bond cleavage on the surface. The goal is to determine if surface interactions change the reactivity order, i.e., whether a bond that is stronger in the gas phase becomes easier to break on the SiO₂ surface.

## Approach
The approach uses first-principles quantum chemistry to model the surface reaction. A minimal cluster model for the SiO₂ surface is constructed (SiH₃–O–SiH₃, with terminal hydrogens) to represent the reactive site. The decomposition of disilane on this surface is studied by locating transition states (TS) for the two competing bond cleavages: Si–H bond breaking (TS2a) and Si–Si bond breaking (TS2b). In parallel, the gas-phase bond dissociation enthalpies are computed for the Si–H bond (from SiH₄ → SiH₃ + H) and the Si–Si bond (Si₂H₆ → 2 SiH₃) at the same theoretical level to serve as a reference. The computational workflow consists of: (1) building initial geometries; (2) geometry optimization and harmonic vibrational frequency calculations at the Hartree–Fock level with the 6-31G** basis set; (3) single-point energy refinement at the MP2(FC)/6-31G** level on the HF-optimized geometries; (4) applying a zero-point energy (ZPE) correction with a standard scaling factor. From the resulting total energies, activation barriers for the two surface pathways and gas-phase bond dissociation energies are obtained, allowing a direct comparison of the surface reactivity order with the gas-phase bond strength order.

## Reproduction target
Compute the surface activation energies for Si–H cleavage (TS2a) and Si–Si cleavage (TS2b) of disilane on the SiH₃–O–SiH₃ surface model at the MP2/6-31G**//HF/6-31G** level, including zero-point energy correction (ZPE scaled by 0.89), and report the raw (electronic) barriers as well. Compute the gas-phase bond dissociation enthalpies for the Si–H bond (from SiH₄ → SiH₃ + H) and the Si–Si bond (from Si₂H₆ → 2 SiH₃) at the same level. Package all numerical results in a single JSON file (energies.json). Determine whether the ordering of bond‑breaking preference on the surface (which bond is broken more easily) follows the same order as the gas‑phase bond strengths, or whether the order is reversed.

## Assets

- ORCA quantum chemistry package: https://www.faccts.de/orca/
- Python 3: python3
- 6-31G** basis set

## Workflow steps

### Step 1: Build initial geometries
- Role: process
- Action: Construct initial molecular geometries for the SiO2 surface model (SiH3-O-SiH3 with H termination), disilane (Si2H6), transition states TS2a (Si-H cleavage) and TS2b (Si-Si cleavage), product SiH3-O-SiH2-SiH3, and gas-phase species SiH4, SiH3, H. Use standard bond lengths and the paper's description of the surface model to generate starting coordinates.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: HF/6-31G** optimization and frequency calculation
- Role: process
- Action: Perform Hartree-Fock geometry optimization with the 6-31G** basis set for all species. Run harmonic frequency calculations on the optimized structures to verify stationary points (minima: zero imaginary frequencies; TS: exactly one imaginary frequency). Collect zero-point vibrational energies (ZPE) from the frequency output, applying a scaling factor of 0.89.
- Evidence: `/app/outputs/hf_opt_freq.log`

### Step 3: Single-point MP2 energy calculation
- Role: process
- Action: Run single-point energy calculations using MP2(FC)/6-31G** on the HF-optimized geometries for all species. Extract the MP2 total energy for each species.
- Evidence: `/app/outputs/mp2_energies.log`

### Step 4: Compute activation energies and bond enthalpies
- Role: scored (load-bearing)
- Action: From the MP2 total energies and ZPEs, compute: (1) surface activation energies for Si-H cleavage (TS2a) and Si-Si cleavage (TS2b) both raw MP2 and ZPE-corrected; (2) gas-phase bond dissociation enthalpies for Si-H bond (from SiH4 -> SiH3 + H) and Si-Si bond (from Si2H6 -> 2SiH3). Package all computed values into energies.json.
- Output file: `/app/outputs/energies.json`
- Format: json
- Contract: {
  "surface": {
    "ts2a_raw_MP2_energy_hartree": float,
    "ts2b_raw_MP2_energy_hartree": float,
    "reactants_sum_raw_MP2_energy_hartree": float,
    "ts2a_MP2_Ea_kcal_mol_raw": float,
    "ts2b_MP2_Ea_kcal_mol_raw": float,
    "ts2a_MP2_Ea_kcal_mol_with_ZPE": float,
    "ts2b_MP2_Ea_kcal_mol_with_ZPE": float
  },
  "gas_phase": {
    "SiH4_MP2_energy_hartree": float,
    "SiH3_MP2_energy_hartree": float,
    "H_MP2_energy_hartree": float,
    "Si2H6_MP2_energy_hartree": float,
    "SiH_bond_enthalpy_kcal_mol": float,
    "SiSi_bond_enthalpy_kcal_mol": float
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energies.json
- path: `/app/outputs/energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed surface activation energies and gas-phase bond enthalpies for verification of bond reactivity reversal.
- schema:
  - `type`: object
  - `required`: `surface`, `gas_phase`
  - `properties`:
    - `surface`:
      - `type`: object
      - `required`: `ts2a_raw_MP2_energy_hartree`, `ts2b_raw_MP2_energy_hartree`, `reactants_sum_raw_MP2_energy_hartree`, `ts2a_MP2_Ea_kcal_mol_raw`, `ts2b_MP2_Ea_kcal_mol_raw`, `ts2a_MP2_Ea_kcal_mol_with_ZPE`, `ts2b_MP2_Ea_kcal_mol_with_ZPE`
      - `properties`:
        - `ts2a_raw_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `ts2b_raw_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `reactants_sum_raw_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `ts2a_MP2_Ea_kcal_mol_raw`:
          - `type`: number
          - `units`: kcal/mol
        - `ts2b_MP2_Ea_kcal_mol_raw`:
          - `type`: number
          - `units`: kcal/mol
        - `ts2a_MP2_Ea_kcal_mol_with_ZPE`:
          - `type`: number
          - `units`: kcal/mol
        - `ts2b_MP2_Ea_kcal_mol_with_ZPE`:
          - `type`: number
          - `units`: kcal/mol
    - `gas_phase`:
      - `type`: object
      - `required`: `SiH4_MP2_energy_hartree`, `SiH3_MP2_energy_hartree`, `H_MP2_energy_hartree`, `Si2H6_MP2_energy_hartree`, `SiH_bond_enthalpy_kcal_mol`, `SiSi_bond_enthalpy_kcal_mol`
      - `properties`:
        - `SiH4_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `SiH3_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `H_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `Si2H6_MP2_energy_hartree`:
          - `type`: number
          - `units`: hartree
        - `SiH_bond_enthalpy_kcal_mol`:
          - `type`: number
          - `units`: kcal/mol
        - `SiSi_bond_enthalpy_kcal_mol`:
          - `type`: number
          - `units`: kcal/mol

Notes: All quantities are computed at MP2/6-31G**//HF/6-31G** level with ZPE scaled by 0.89.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "surface",
          "gas_phase"
        ],
        "properties": {
          "surface": {
            "type": "object",
            "required": [
              "ts2a_raw_MP2_energy_hartree",
              "ts2b_raw_MP2_energy_hartree",
              "reactants_sum_raw_MP2_energy_hartree",
              "ts2a_MP2_Ea_kcal_mol_raw",
              "ts2b_MP2_Ea_kcal_mol_raw",
              "ts2a_MP2_Ea_kcal_mol_with_ZPE",
              "ts2b_MP2_Ea_kcal_mol_with_ZPE"
            ],
            "properties": {
              "ts2a_raw_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "ts2b_raw_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "reactants_sum_raw_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "ts2a_MP2_Ea_kcal_mol_raw": {
                "type": "number",
                "units": "kcal/mol"
              },
              "ts2b_MP2_Ea_kcal_mol_raw": {
                "type": "number",
                "units": "kcal/mol"
              },
              "ts2a_MP2_Ea_kcal_mol_with_ZPE": {
                "type": "number",
                "units": "kcal/mol"
              },
              "ts2b_MP2_Ea_kcal_mol_with_ZPE": {
                "type": "number",
                "units": "kcal/mol"
              }
            }
          },
          "gas_phase": {
            "type": "object",
            "required": [
              "SiH4_MP2_energy_hartree",
              "SiH3_MP2_energy_hartree",
              "H_MP2_energy_hartree",
              "Si2H6_MP2_energy_hartree",
              "SiH_bond_enthalpy_kcal_mol",
              "SiSi_bond_enthalpy_kcal_mol"
            ],
            "properties": {
              "SiH4_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "SiH3_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "H_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "Si2H6_MP2_energy_hartree": {
                "type": "number",
                "units": "hartree"
              },
              "SiH_bond_enthalpy_kcal_mol": {
                "type": "number",
                "units": "kcal/mol"
              },
              "SiSi_bond_enthalpy_kcal_mol": {
                "type": "number",
                "units": "kcal/mol"
              }
            }
          }
        }
      },
      "description": "Computed surface activation energies and gas-phase bond enthalpies for verification of bond reactivity reversal."
    }
  ],
  "notes": "All quantities are computed at MP2/6-31G**//HF/6-31G** level with ZPE scaled by 0.89."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the `energies.json` output file. The verifier independently compares your computed activation barriers and bond enthalpies against reference results obtained from the original study (same theory level, same molecular models) using appropriate tolerances. It also checks whether the relative ordering of the surface activation energies (which bond breaks more easily) and the ordering of the gas‑phase bond dissociation enthalpies (which bond is stronger) are consistent with the paper's main finding. Each component (surface barriers raw and ZPE‑corrected, gas‑phase bond enthalpies, ordering correctness) contributes to a weighted score. Simply reporting numbers is not sufficient; evidence that the required calculations were actually performed is validated by the verifier, which may cross‑check intermediate energies or enforce structural consistency. The final reward is a single floating‑point number between 0.0 (no credit) and 1.0 (full reproduction).
