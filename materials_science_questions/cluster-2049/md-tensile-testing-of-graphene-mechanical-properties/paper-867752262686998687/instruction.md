# DFT Geometry Optimization and Formation Energy of Graphene and Graphane

## Problem background
Graphene, a single layer of carbon atoms arranged in a honeycomb lattice, exhibits exceptional mechanical and electronic properties. Chemical functionalization through hydrogenation can dramatically alter these properties and is promising for hydrogen storage, chemical sensing, and tunable electronics. When hydrogen atoms bond to both carbon atoms in the unit cell, a fully hydrogenated sheet—graphane—can form in two distinct phases. In the symmetric (boat-like) phase, hydrogen atoms attach on the same side of the graphene plane, preserving the planar geometry. In the anti-symmetric (chair-like) phase, hydrogen atoms bind on opposite sides, causing out-of-plane puckering and a transition from sp² to sp³ hybridization. External mechanical strain applied to the graphene sheet can modulate the binding strength of hydrogen, offering a route to controllable and reversible hydrogenation. Understanding the quantitative relationship between strain and the structural parameters and formation energies of graphane is the central question this task addresses.

## Approach
First-principles density functional theory (DFT) calculations within the local density approximation (LDA) are used to optimize the atomic structures and compute total energies. The workflow uses the PWSCF code of the Quantum ESPRESSO suite with standard Perdew–Zunger LDA pseudopotentials for carbon and hydrogen. A unit cell containing two carbon atoms (pristine graphene) or two carbon and two hydrogen atoms (graphane) is employed. Variable-cell geometry optimizations are performed for pristine graphene, symmetric graphane, and anti-symmetric graphane, yielding equilibrium in-plane lattice constants and total energies. For the anti-symmetric phase, the relaxation also determines the out-of-plane corrugation, carbon–carbon bond length, and bond angles. To quantify the effect of strain, a fixed-cell optimization is carried out on symmetric graphane with the lattice constant held at a value corresponding to 10% biaxial tensile strain relative to graphene’s equilibrium value. The formation energy (binding energy per carbon–hydrogen pair) is then computed as E_form = E(graphane) - E(graphene) - E(H), where E(H) is the known energy of an isolated hydrogen atom, evaluated at both zero strain and the strained condition.

## Reproduction target
Using DFT geometry optimizations as described, produce the following quantities: (1) the optimized in-plane lattice constant of pristine graphene, symmetric graphane, and anti-symmetric graphane; (2) for anti-symmetric graphane, the out-of-plane corrugation (the vertical displacement between the two carbon atoms), the C–C bond length, the C–C–C bond angle, and the H–C–C bond angle; (3) the formation energy per C–H pair for symmetric graphane at its equilibrium lattice constant and for anti-symmetric graphane at its equilibrium lattice constant; and (4) the formation energy per C–H pair for symmetric graphane at a fixed in-plane lattice constant of 2.69 Å (corresponding to 10% biaxial tensile strain relative to graphene). All geometric parameters must be reported in Å and degrees, formation energies in eV per C–H pair.

## Assets

- Quantum ESPRESSO (PWSCF): https://www.quantum-espresso.org
- Perdew–Zunger LDA pseudopotentials for C and H: QE pseudopotential library (e.g., C.pz-vbc.UPF, H.pz-vbc.UPF)

## Workflow steps

### Step 1: Geometry optimization of pristine graphene
- Role: process
- Action: Run variable-cell DFT geometry optimization of a graphene unit cell (two carbon atoms) using Quantum ESPRESSO with LDA exchange-correlation functional to obtain the equilibrium in-plane lattice constant and total energy.
- Evidence: `/app/outputs/graphene_opt.out`

### Step 2: Geometry optimization of symmetric graphane
- Role: process
- Action: Run variable-cell DFT geometry optimization of a symmetric graphane unit cell (two carbon atoms, two hydrogen atoms on the same side) using the same DFT methodology to obtain the equilibrium lattice constant, planar atomic coordinates, and total energy.
- Evidence: `/app/outputs/sym_graphane_opt.out`

### Step 3: Geometry optimization of anti-symmetric graphane
- Role: process
- Action: Run variable-cell DFT geometry optimization of an anti-symmetric graphane unit cell (two carbon atoms, two hydrogen atoms on opposite sides) using the same DFT methodology to obtain the equilibrium lattice constant, out-of-plane corrugation, and total energy.
- Evidence: `/app/outputs/asym_graphane_opt.out`

### Step 4: Fixed-cell optimization of symmetric graphane at a=2.69 Å
- Role: process
- Action: Perform a fixed-cell DFT geometry relaxation of the symmetric graphane unit cell with the in-plane lattice constant fixed at a=2.69 Å (10% biaxial tensile strain relative to graphene) to obtain the total energy at that strain.
- Evidence: `/app/outputs/sym_graphane_strained.out`

### Step 5: Collect geometric parameters
- Role: scored (load-bearing)
- Action: From the optimized structures of steps 1–3, extract the following quantities: lattice constant a of pristine graphene (Å), symmetric graphane (Å), and anti-symmetric graphane (Å); for anti-symmetric graphane also the out-of-plane corrugation (Å), C–C bond length (Å), C–C–C bond angle (°), and H–C–C bond angle (°). Write all values to geometric_parameters.json.
- Output file: `/app/outputs/geometric_parameters.json`
- Format: json
- Contract: JSON object with keys a_graphene (Å), a_sym (Å), a_asym (Å), corrugation_asym (Å), bond_length_C_C (Å), bond_angle_C_C_C (degrees), bond_angle_H_C_C (degrees).
- Scoring: scored by hidden verifier

### Step 6: Compute formation energies
- Role: scored (load-bearing)
- Action: Compute the formation energy E_f = E(graphane) - E(graphene) - E(H) per C–H pair for each graphane phase, using the total energies from steps 1–4 and the reference energy of an isolated hydrogen atom. Report E_f for symmetric graphane at zero strain, anti-symmetric graphane at zero strain, and symmetric graphane at the strained condition (a=2.69 Å). Write these to formation_energies.json.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: JSON object with keys E_f_sym_0 (eV/CH), E_f_asym_0 (eV/CH), E_f_sym_strained (eV/CH).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometric_parameters.json`
- `/app/outputs/formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometric_parameters.json
- path: `/app/outputs/geometric_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized geometric parameters of pristine graphene and symmetric/anti-symmetric graphane phases.
- schema:
  - `type`: object
  - `required`:
    - `a_graphene`: number (Å)
    - `a_sym`: number (Å)
    - `a_asym`: number (Å)
    - `corrugation_asym`: number (Å)
    - `bond_length_C_C`: number (Å)
    - `bond_angle_C_C_C`: number (degrees)
    - `bond_angle_H_C_C`: number (degrees)

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Formation energies of graphane phases at zero strain and at 10% biaxial tensile strain.
- schema:
  - `type`: object
  - `required`:
    - `E_f_sym_0`: number (eV/CH)
    - `E_f_asym_0`: number (eV/CH)
    - `E_f_sym_strained`: number (eV/CH)
    - `E_f_asym_strained`: number (eV/CH)

Notes: Check compares agent-reported values to paper-reported gold values with tolerances; all values are compared as absolute differences within predefined thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometric_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a_graphene": "number (Å)",
          "a_sym": "number (Å)",
          "a_asym": "number (Å)",
          "corrugation_asym": "number (Å)",
          "bond_length_C_C": "number (Å)",
          "bond_angle_C_C_C": "number (degrees)",
          "bond_angle_H_C_C": "number (degrees)"
        }
      },
      "description": "Optimized geometric parameters of pristine graphene and symmetric/anti-symmetric graphane phases."
    },
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "E_f_sym_0": "number (eV/CH)",
          "E_f_asym_0": "number (eV/CH)",
          "E_f_sym_strained": "number (eV/CH)",
          "E_f_asym_strained": "number (eV/CH)"
        }
      },
      "description": "Formation energies of graphane phases at zero strain and at 10% biaxial tensile strain."
    }
  ],
  "notes": "Check compares agent-reported values to paper-reported gold values with tolerances; all values are compared as absolute differences within predefined thresholds."
}
```

## How you are scored
Your work is evaluated by a hidden verifier that independently checks the JSON files you produce. The verifier compares the geometric parameters and formation energies you report against reference values derived from the original study. Each quantity is compared using predefined tolerances that account for legitimate differences between independent DFT implementations and numerical settings. The overall reward is a weighted sum of individual scores across all quantities, with the formation energies carrying the largest share and the strained formation energy being particularly important. Reporting correct values that fall within the expected range will yield a high score; merely quoting numbers from memory or unrelated sources will not pass. The verifier does not access any external resources; it scores only the contents of your output directory.
