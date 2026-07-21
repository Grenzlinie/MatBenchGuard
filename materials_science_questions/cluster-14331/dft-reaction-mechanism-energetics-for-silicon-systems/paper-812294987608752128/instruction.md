# Computation of Activation Energies for H⁻ Attack on SiH₃F₂⁻

## Problem background
Pentacoordinated silicon anions can undergo nucleophilic attack to form hexacoordinated intermediates, which are important in organosilicon chemistry. Understanding the energetics of these reactions—particularly the activation barriers for attack by a hydride ion and the relative stability of different pentacoordinated isomers—helps clarify ligand substitution mechanisms at silicon centers. This task focuses on computing the activation energies for the reaction of the pentacoordinated anion SiH₃F₂⁻ with a hydride ion (H⁻) and the energy difference between two isomers of the pentacoordinated anion using ab initio molecular orbital theory.

### Molecular structures
For this assignment the following unambiguous structures must be used.

**Isomer 1** (global minimum, D₃ₕ symmetry) – Both fluorine atoms occupy the axial positions; the three hydrogen atoms lie in the equatorial plane.

**Isomer 2** (higher‑energy isomer, Cₛ symmetry) – The axial positions are occupied by one fluorine and one hydrogen atom; the equatorial plane contains the second fluorine atom and the remaining two hydrogen atoms.

**Transition states** – All three saddle points correspond to a backside attack of H⁻ on a pentacoordinated silicon centre in the equatorial plane, i.e. the nucleophile approaches Si from the direction opposite to the equatorial Si–Y bond (Y = H or F) that is being displaced.
- **TS1**: Attack on isomer 1, at the backside of an equatorial **Si–H** bond.
- **TS2**: Attack on isomer 2, at the backside of the equatorial **Si–H** bond.
- **TS3**: Attack on isomer 2, at the backside of the equatorial **Si–F** bond.

## Approach
We employ a two-stage computational protocol:
1. **Geometry optimization** of all species (reactants and transition states) at the restricted Hartree–Fock (RHF) level with the 6‑31++G** basis set. Diffuse and polarization functions are essential for anionic species.
2. **Single-point energy calculations** at the second‑order Møller–Plesset (MP2) level using the same basis set on the optimized geometries.

The studied system is **SiH₃F₂⁻ + H⁻**. Two isomers of the pentacoordinated anion are considered: isomer 1 (both fluorine atoms apical) and isomer 2 (one fluorine apical, one fluorine equatorial). For hydride attack, three distinct transition states are located: **TS1** (attack starting from isomer 1), and **TS2** and **TS3** (both starting from isomer 2). Activation barriers are computed as  

$$\Delta E^\ddagger = E(\text{TS}) - E(\text{isomer}) - E(\mathrm{H^-})$$

and the isomer energy difference as  

$$\Delta E_{2-1} = E(2) - E(1).$$

All energies are obtained as total MP2/6‑31++G** single‑point energies (in hartree) and converted to kcal mol⁻¹ using $1~\text{hartree} = 627.509~\text{kcal mol}^{-1}$. The workflow is implemented with an open‑source quantum chemistry package such as Psi4.

## Reproduction target
Reproduce the activation barriers (in kcal mol⁻¹) for hydride attack on the two isomers of SiH₃F₂⁻ leading to hexacoordinated dianions, and the energy difference between the two isomers, at the MP2/6‑31++G**//RHF/6‑31++G** level of theory, using an open‑source electronic structure code. The raw MP2 total energies (in hartree) for the reactants and transition states, together with the computed barriers and isomer energy difference, must be written to `/app/outputs/results.json` following the output schema described below. The checker will verify the internal consistency of the submitted energies and that the derived barriers satisfy a specific relative ordering, but the target numbers themselves are hidden.

## Assets
- Psi4 (or equivalent open‑source quantum chemistry package): https://psicode.org/
- 6-31++G** basis set

## Workflow steps

### Step 1: Geometry optimization at RHF/6-31++G**
- Role: process
- Action: Construct initial molecular geometries according to the structural descriptions given in **Molecular structures** above. Perform RHF/6‑31++G** geometry optimizations for all species: isomer 1, isomer 2, TS1, TS2, TS3, and the free H⁻ anion. Use a saddle‑point search algorithm for transition states and verify the presence of one imaginary frequency for each TS. Save the optimized Cartesian coordinates in memory or temporary files for use in the next step; no separate output file is required by the verifier.

### Step 2: MP2 energy calculations and barrier determination
- Role: scored (load‑bearing)
- Action: For each optimized geometry from Step 1 (isomer 1, isomer 2, TS1, TS2, TS3, and H⁻), perform a single‑point MP2/6‑31++G** calculation to obtain total energies in hartrees. Then compute the activation barriers: barrier(TS) = (E_TS − E_corresponding_isomer − E_H⁻) × 627.509 kcal mol⁻¹. Compute the isomer energy difference: ΔE = (E_isomer 2 − E_isomer 1) × 627.509 kcal mol⁻¹. Report all energies and computed values in `/app/outputs/results.json` using the schema below.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: `isomer_1_energy_mp2` (float, hartrees), `isomer_2_energy_mp2` (float, hartrees), `E_Hminus_mp2` (float, hartrees), `TS1_energy_mp2` (float, hartrees), `TS2_energy_mp2` (float, hartrees), `TS3_energy_mp2` (float, hartrees), `isomer_energy_difference_kcalmol` (float, kcal/mol), `barrier_TS1_kcalmol` (float, kcal/mol), `barrier_TS2_kcalmol` (float, kcal/mol), `barrier_TS3_kcalmol` (float, kcal/mol), `software_used` (string).
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
- target_policy: metric_recompute
- description: MP2/6‑31++G** single‑point energies of reactants and transition states for H⁻ attack on SiH₃F₂⁻, together with the activation barriers and isomer energy difference.
- schema:
  - `type`: object
  - `required`: `isomer_1_energy_mp2`, `isomer_2_energy_mp2`, `E_Hminus_mp2`, `TS1_energy_mp2`, `TS2_energy_mp2`, `TS3_energy_mp2`, `isomer_energy_difference_kcalmol`, `barrier_TS1_kcalmol`, `barrier_TS2_kcalmol`, `barrier_TS3_kcalmol`, `software_used`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `isomer_1_energy_mp2`: hartrees
    - `isomer_2_energy_mp2`: hartrees
    - `E_Hminus_mp2`: hartrees
    - `TS1_energy_mp2`: hartrees
    - `TS2_energy_mp2`: hartrees
    - `TS3_energy_mp2`: hartrees
    - `isomer_energy_difference_kcalmol`: kcal/mol
    - `barrier_TS1_kcalmol`: kcal/mol
    - `barrier_TS2_kcalmol`: kcal/mol
    - `barrier_TS3_kcalmol`: kcal/mol
    - `software_used`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "isomer_1_energy_mp2",
          "isomer_2_energy_mp2",
          "E_Hminus_mp2",
          "TS1_energy_mp2",
          "TS2_energy_mp2",
          "TS3_energy_mp2",
          "isomer_energy_difference_kcalmol",
          "barrier_TS1_kcalmol",
          "barrier_TS2_kcalmol",
          "barrier_TS3_kcalmol",
          "software_used"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "isomer_1_energy_mp2": "hartrees",
          "isomer_2_energy_mp2": "hartrees",
          "E_Hminus_mp2": "hartrees",
          "TS1_energy_mp2": "hartrees",
          "TS2_energy_mp2": "hartrees",
          "TS3_energy_mp2": "hartrees",
          "isomer_energy_difference_kcalmol": "kcal/mol",
          "barrier_TS1_kcalmol": "kcal/mol",
          "barrier_TS2_kcalmol": "kcal/mol",
          "barrier_TS3_kcalmol": "kcal/mol",
          "software_used": "string"
        }
      },
      "description": "MP2/6‑31++G** single‑point energies of reactants and transition states for H⁻ attack on SiH₃F₂⁻, together with the activation barriers and isomer energy difference."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that reads `/app/outputs/results.json`. The verifier recomputes the activation barriers and isomer energy difference from the raw MP2 energies you provide, and compares them against the expected physical values and the required trend among the barriers without revealing the target numbers. It also checks structural conformance (file format, presence of all required keys, correct units). A correct solution yields the proper barriers and isomer energy difference within a hidden tolerance, and meets the required ordering of barriers (TS2 < TS3 < TS1); full credit is awarded for meeting these criteria. The software tool reported in `software_used` must be a recognised open‑source quantum chemistry package.