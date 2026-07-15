# DFT+U Study of Antiferromagnetic Superexchange in Fe-Porphyrin-O-Co Slab

## Problem background
Fe-porphyrin molecules adsorbed directly on ferromagnetic Co or Ni films typically show ferromagnetic coupling. Introducing an atomic oxygen interlayer between the molecule and the substrate is proposed as a way to modify this magnetic interaction. The magnetic alignment between the Fe center and the Co substrate (whether ferromagnetic or antiferromagnetic) and the underlying mechanism are not yet determined; the task is to compute the relative orientation and quantify relevant structural and magnetic parameters (bond lengths, spin moments, energetic ordering of different Fe spin states). First-principles density functional theory with a Hubbard U correction (DFT+U) can provide insight into the nature of the magnetic interaction and quantify these properties.

## Approach
Use DFT+U calculations (U=4 eV, J=1 eV on Fe d orbitals) with an open-source plane-wave code (Quantum ESPRESSO) to model a supercell containing the Fe-octaethylporphyrin molecule, a bridging O atom, and a 3-layer Co(001) slab. Perform full geometry relaxation for two plausible Fe spin states: high-spin (S≈5/2) and intermediate-spin (S≈3/2). Then, from the relaxed structures, extract total energies, atomic magnetic moments on Fe and Co, and Fe-O/Co-O bond lengths. Compare the two spin configurations to determine the relative energetic stability and the alignment of Fe and Co magnetic moments.

## Reproduction target
Compute the DFT+U properties for the Fe-OEP-O-Co(001) system: total energies of the high-spin and intermediate-spin states, energy difference, Fe and Co magnetic moments in both states, Fe-O and Co-O bond lengths, and the relative orientation of the Fe and Co moments (ferromagnetic or antiferromagnetic). Report all results in a single JSON file (results.json) with the schema defined in the output contract.

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- SSSP pseudopotentials (efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry relaxation of Fe-OEP-O-Co(001) in two spin configurations
- Role: process
- Action: Construct a supercell containing Fe-OEP molecule, a bridging O atom, and a 3-layer Co(100) slab (~188 atoms). Using Quantum ESPRESSO with DFT+U (U=4 eV, J=1 eV on Fe d orbitals), perform full geometry relaxation for the high-spin (S≈5/2) and intermediate-spin (S≈3/2) states. Save the relaxed atomic coordinates and output logs.
- Evidence: `/app/outputs/relax_high_spin.out, relax_intermediate_spin.out`

### Step 2: Compute energies, magnetic moments, and bond lengths
- Role: scored (load-bearing)
- Action: From the relaxed geometries of step01, perform single-point DFT+U calculations to extract total energies (in Ry), atomic magnetic moments on Fe and Co (in μB), and Fe-O and Co-O bond lengths (in Å) for both spin configurations. Determine the relative alignment of Fe and Co moments (ferromagnetic or antiferromagnetic). Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"high_spin_energy": float (Ry), "intermediate_spin_energy": float (Ry), "energy_difference": float (Ry), "high_spin_Fe_moment": float (μB), "intermediate_spin_Fe_moment": float (μB), "high_spin_Co_moment": float (μB), "intermediate_spin_Co_moment": float (μB), "Fe_O_bond_length": float (Å), "Co_O_bond_length": float (Å), "coupling_sign": string ("antiferromagnetic" or "ferromagnetic")}
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
- target_policy: reference_match
- description: DFT+U results: total energies, spin magnetic moments, bond lengths, and the sign of Fe-Co magnetic coupling. The numerical values will be compared against reference values from the paper using tolerances; the coupling_sign must be 'antiferromagnetic'.
- schema:
  - `type`: object
  - `required`: `high_spin_energy`, `intermediate_spin_energy`, `energy_difference`, `high_spin_Fe_moment`, `intermediate_spin_Fe_moment`, `high_spin_Co_moment`, `intermediate_spin_Co_moment`, `Fe_O_bond_length`, `Co_O_bond_length`, `coupling_sign`
  - `properties`:
    - `high_spin_energy`:
      - `type`: number
      - `unit`: Ry
    - `intermediate_spin_energy`:
      - `type`: number
      - `unit`: Ry
    - `energy_difference`:
      - `type`: number
      - `unit`: Ry
    - `high_spin_Fe_moment`:
      - `type`: number
      - `unit`: μB
    - `intermediate_spin_Fe_moment`:
      - `type`: number
      - `unit`: μB
    - `high_spin_Co_moment`:
      - `type`: number
      - `unit`: μB
    - `intermediate_spin_Co_moment`:
      - `type`: number
      - `unit`: μB
    - `Fe_O_bond_length`:
      - `type`: number
      - `unit`: Å
    - `Co_O_bond_length`:
      - `type`: number
      - `unit`: Å
    - `coupling_sign`:
      - `type`: string
      - `description`: one of 'antiferromagnetic' or 'ferromagnetic'

Notes: The quantities are compared to the paper-reported values (Fe-O ≈1.92 Å, Co-O ≈1.74 Å, Fe moments ≈4.4 μB high-spin, ≈2.9 μB intermediate-spin, high-spin ground state, antiferromagnetic coupling). No gold values are disclosed in the public contract.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "high_spin_energy",
          "intermediate_spin_energy",
          "energy_difference",
          "high_spin_Fe_moment",
          "intermediate_spin_Fe_moment",
          "high_spin_Co_moment",
          "intermediate_spin_Co_moment",
          "Fe_O_bond_length",
          "Co_O_bond_length",
          "coupling_sign"
        ],
        "properties": {
          "high_spin_energy": {
            "type": "number",
            "unit": "Ry"
          },
          "intermediate_spin_energy": {
            "type": "number",
            "unit": "Ry"
          },
          "energy_difference": {
            "type": "number",
            "unit": "Ry"
          },
          "high_spin_Fe_moment": {
            "type": "number",
            "unit": "μB"
          },
          "intermediate_spin_Fe_moment": {
            "type": "number",
            "unit": "μB"
          },
          "high_spin_Co_moment": {
            "type": "number",
            "unit": "μB"
          },
          "intermediate_spin_Co_moment": {
            "type": "number",
            "unit": "μB"
          },
          "Fe_O_bond_length": {
            "type": "number",
            "unit": "Å"
          },
          "Co_O_bond_length": {
            "type": "number",
            "unit": "Å"
          },
          "coupling_sign": {
            "type": "string",
            "description": "one of 'antiferromagnetic' or 'ferromagnetic'"
          }
        }
      },
      "description": "DFT+U results: total energies, spin magnetic moments, bond lengths, and the sign of Fe-Co magnetic coupling. The numerical values will be compared against reference values from the paper using tolerances; the coupling_sign must be 'antiferromagnetic'."
    }
  ],
  "notes": "The quantities are compared to the paper-reported values (Fe-O ≈1.92 Å, Co-O ≈1.74 Å, Fe moments ≈4.4 μB high-spin, ≈2.9 μB intermediate-spin, high-spin ground state, antiferromagnetic coupling). No gold values are disclosed in the public contract."
}
```

## How you are scored
Your submitted results.json will be evaluated by a hidden verifier that compares your computed quantities against independently determined reference values using appropriate tolerances. Each field is checked: energy ordering, bond lengths, magnetic moments, and coupling sign. The verifier combines the per-field outcomes into a final reward in [0,1]. The exact reference values and tolerances are not disclosed; you must produce physically reasonable numbers by correctly executing the DFT+U workflow. Reporting numbers that are not derived from the required calculations will not pass.
