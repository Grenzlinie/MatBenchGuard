# DFT Effective Masses of Mixed-Metal Perovskites

## Problem background
Hybrid halide perovskites like methylammonium lead iodide (MAPbI3) are leading materials for high-efficiency solar cells. Partial substitution of the Pb2+ cation by other divalent metals offers a route to tune optoelectronic properties. One critical factor for photovoltaic performance is the balance of electron and hole transport, which is directly linked to the effective masses of charge carriers. This task investigates how replacing 6.25% of lead with manganese modifies the effective masses. Using density functional theory (DFT), we compute the electron and hole effective masses in pure MAPbI3 and in the mixed-metal perovskite MAPb0.9375Mn0.0625I3. The resulting masses provide insight into whether Mn substitution leads to unbalanced charge transport that could limit device efficiency.

## Approach
The calculations are performed with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional including spin-orbit coupling, as implemented in the open-source code Quantum ESPRESSO. We construct a cubic unit cell of MAPbI3 with a lattice constant of approximately 6.33 Å. A 192-atom supercell is then built for the Mn-substituted composition, replacing one of the Pb atoms by Mn. For each system, a geometry optimization is performed to relax the atomic positions, followed by a band structure calculation along high-symmetry k-point paths. From the resulting band structures, effective masses are extracted by parabolic fitting of the energy dispersion near the valence band maximum (for holes) and the conduction band minimum (for electrons). All effective masses are reported in units of the free-electron mass m0.

## Reproduction target
Produce a JSON file containing the effective masses for both compositions. The file must include exactly four numerical keys: MAPbI3_eff_mass_electron, MAPbI3_eff_mass_hole, MAPbMn_eff_mass_electron, and MAPbMn_eff_mass_hole. All values must be positive and correspond to the masses along the direction where the band curvature is smallest (i.e., the lightest effective mass for the electron and the lightest effective mass for the hole from the fitted bands). The masses should be reported relative to the free-electron mass. No other outputs are required for scoring.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP Efficiency Pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare crystal structures
- Role: process
- Action: Construct the cubic MAPbI3 unit cell (lattice constant ~6.33 Å) and a 192-atom supercell for MAPb0.9375Mn0.0625I3 with one Pb replaced by Mn, generating Quantum ESPRESSO input files.
- Evidence: `/app/outputs/structure_files.json`

### Step 2: Run DFT calculations
- Role: process
- Action: Perform DFT geometry optimization and band structure calculation for both systems using Quantum ESPRESSO with PBE functional, spin-orbit coupling, and SSSP pseudopotentials. Produce band structure data.
- Evidence: `/app/outputs/dft_output.log`

### Step 3: Extract effective masses
- Role: scored (load-bearing)
- Action: From the computed band structures, perform parabolic fitting of the band edges near the VBM and CBM to obtain the electron and hole effective masses (in units of free electron mass m0). Write the results to effective_masses.json.
- Output file: `/app/outputs/effective_masses.json`
- Format: json
- Contract: JSON object with keys MAPbI3_eff_mass_electron, MAPbI3_eff_mass_hole, MAPbMn_eff_mass_electron, MAPbMn_eff_mass_hole (positive numbers).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_masses.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_masses.json
- path: `/app/outputs/effective_masses.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Effective masses of electron and hole for MAPbI3 and MAPb0.9375Mn0.0625I3, in units of free electron mass m0. All values must be positive.
- schema:
  - `type`: object
  - `required`:
    - `MAPbI3_eff_mass_electron`: number
    - `MAPbI3_eff_mass_hole`: number
    - `MAPbMn_eff_mass_electron`: number
    - `MAPbMn_eff_mass_hole`: number

Notes: The checker validates that the hole/electron effective mass ratio for the Mn-substituted system is greater than 2.5, while the pure MAPbI3 ratio remains roughly balanced (1–2). All masses must be positive. A generous tolerance on absolute values accommodates toolchain variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_masses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "MAPbI3_eff_mass_electron": "number",
          "MAPbI3_eff_mass_hole": "number",
          "MAPbMn_eff_mass_electron": "number",
          "MAPbMn_eff_mass_hole": "number"
        }
      },
      "description": "Effective masses of electron and hole for MAPbI3 and MAPb0.9375Mn0.0625I3, in units of free electron mass m0. All values must be positive."
    }
  ],
  "notes": "The checker validates that the hole/electron effective mass ratio for the Mn-substituted system is greater than 2.5, while the pure MAPbI3 ratio remains roughly balanced (1–2). All masses must be positive. A generous tolerance on absolute values accommodates toolchain variations."
}
```

## How you are scored
A hidden verifier will read your `effective_masses.json` and apply a set of independent checks. It first confirms that all entries are positive numbers. It then evaluates the effective masses against physical constraints: for the Mn-substituted system, a specific relationship between the hole and electron masses must be observed (e.g., a minimum ratio between them). If your computed masses satisfy that relationship and pass the positivity check, you receive full credit. The reward is calculated as a weighted score; partial credit may be awarded if only some criteria are met. The exact thresholds and criteria are not disclosed.
