## Problem background

CO oxidation on oxide-supported single-atom catalysts (SACs) is a model reaction for understanding atomic-scale catalytic mechanisms and for developing low-temperature exhaust purification. The Ir1/FeOx SAC, with single iridium atoms dispersed on iron oxide, has been studied for its activity in CO oxidation and water-gas-shift reactions. Understanding the microscopic reaction pathway — whether CO2 formation proceeds via a Langmuir–Hinshelwood (L–H) mechanism between co-adsorbed species or an Eley–Rideal (E–R) mechanism with gas-phase CO — is critical to rationalising catalytic performance. The rate-determining step and the associated activation barriers determine the overall catalytic activity.

## Approach

Use plane-wave density functional theory (DFT) with the PBE exchange-correlation functional and DFT+U corrections for the Fe 3d electrons. Model the catalyst as an Ir single atom substituting a surface Fe atom on an O3-terminated α-Fe2O3(0001) slab, with an adjacent surface oxygen vacancy to represent the partially reduced support. Apply antiferromagnetic ordering on the Fe atoms.

The workflow proceeds by first constructing and relaxing this Ir1/FeOx slab model. Then calculate the adsorption energetics of O2 in both molecular and dissociative configurations on the reduced surface. From the dissociative adsorption geometry, locate transition states and compute activation barriers for three distinct pathways leading to the first CO2 molecule:
- L–H mechanism on the high-valent Ir site (three-fold O coordination)
- L–H mechanism on a low-valent Ir site (two-fold O coordination after vacancy creation)
- E–R mechanism with gas-phase CO reacting directly with a vertically adsorbed O atom on Ir
After desorption of the first CO2, adsorb a second CO molecule and locate the transition state for the rate-determining second CO2 formation (also L–H).
Transition states are located using the climbing-image nudged elastic band (NEB) or dimer method. The activation barrier for each pathway is the energy difference between the transition state and the corresponding initial co-adsorbed state.

## Reproduction target

Compute the four activation barriers (in eV) for CO oxidation on the Ir1/FeOx slab model described above and write them to a JSON file. The hidden verifier will independently compare each computed barrier to a reference and check the internal consistency of the results.

## Assets

The following publicly available resources are required. Obtain them at runtime:

- **α-Fe2O3 (hematite) bulk crystal structure** — used to construct the (0001) slab model. Available from the Materials Project (mp-24972, https://next-gen.materialsproject.org/materials/mp-24972) or the Crystallography Open Database (COD ID 1000032).
- **Quantum ESPRESSO** — open-source plane-wave DFT code supporting DFT+U calculations, geometry optimization, and NEB transition-state searches. Available at https://www.quantum-espresso.org/.
- **PBE pseudopotentials for Fe, O, Ir, and C** — standard pseudopotential library (e.g., SSSP efficiency library at https://www.materialscloud.org/discover/sssp/table/efficiency) providing PAW/PBE pseudopotentials for all required elements.

## Workflow steps

Follow these steps in order. The DFT calculations are compute-intensive; you may use appropriate external or remote compute resources and bring the final artifacts back to /app/outputs.

### Step 1: Slab model construction and relaxation
- Role: process
- Action: Obtain the bulk α-Fe2O3 (hematite) crystal structure. Construct an O3-terminated (0001) slab model with 12 Fe layers and sufficient vacuum (~12 Å). Substitute one surface Fe atom by an Ir atom. Create an adjacent surface oxygen vacancy. Perform DFT+U geometry optimization (relaxing the top layers) with the antiferromagnetic ordering of Fe atoms.
- Evidence: none

### Step 2: O2 adsorption and dissociative configuration
- Role: process
- Action: On the relaxed Ir1/FeOx slab from Step 1, place an O2 molecule near the Ir site and oxygen vacancy. Perform separate DFT+U geometry optimizations for: (a) intact molecular O2 adsorption, and (b) dissociative O2 adsorption (one O atom adsorbed on Ir, the other healing the oxygen vacancy). Confirm that dissociative adsorption is energetically preferred and record the dissociated geometry.
- Evidence: none

### Step 3: Transition state and barrier — L–H first CO2 on high-valent Ir
- Role: process
- Action: Using the dissociative O2 geometry from Step 2 (high-valent Ir site with three-fold O coordination), co-adsorb a CO molecule on the Ir atom together with the O atom bound to Ir (OB). Locate the transition state for the reaction CO(ad) + OB → CO2 using NEB or the dimer method. Compute the activation barrier as E(TS) − E(initial co-adsorbed state).
- Evidence: none

### Step 4: Transition state and barrier — L–H first CO2 on low-valent Ir
- Role: process
- Action: Starting from an Ir site with two-fold O coordination (low-valent Ir, where the oxygen vacancy reduces the Ir coordination), co-adsorb CO and an O atom on Ir. Locate the transition state for CO(ad) + O → CO2 and compute the activation barrier.
- Evidence: none

### Step 5: Transition state and barrier — Eley–Rideal first CO2
- Role: process
- Action: From the dissociative O2 geometry, model the direct reaction of gas-phase CO with the vertically adsorbed O atom (OB) on Ir. Locate the transition state for CO(gas) + OB → CO2 and compute the activation barrier.
- Evidence: none

### Step 6: Rate-determining second CO2 formation
- Role: process
- Action: After desorption of the first CO2 from the surface, adsorb a second CO molecule on the Ir atom. Locate the transition state for the reaction of adsorbed CO with the remaining O atom (OC) healing the oxygen vacancy: CO(ad) + OC → CO2. This is the rate-determining step of the catalytic cycle. Compute its activation barrier.
- Evidence: none

### Step 7: Record computed activation barriers
- Role: scored (load-bearing)
- Action: Collect the four activation barriers computed in Steps 3–6 and write them to a JSON file.
- Output file: `/app/outputs/activation_barriers.json`
- Format: json
- Contract: JSON object with exactly four keys — `L_H_high_valent`, `L_H_low_valent`, `E_R`, `second_CO2` — each mapped to a floating-point number representing the activation barrier in eV.
- Scoring: scored by hidden verifier

## Output files

The only required output is:
- `/app/outputs/activation_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_barriers.json
- path: `/app/outputs/activation_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Four DFT-computed activation barriers for CO oxidation pathways on Ir1/FeOx. All values in eV.
- schema:
  - `type`: object
  - `required`:
    - `L_H_high_valent`: number (eV)
    - `L_H_low_valent`: number (eV)
    - `E_R`: number (eV)
    - `second_CO2`: number (eV)

Notes: The verifier independently compares each barrier to a hidden reference tolerance window and checks structural consistency among the reported barriers. The agent must run the stated DFT workflow to produce these values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "L_H_high_valent": "number (eV)",
          "L_H_low_valent": "number (eV)",
          "E_R": "number (eV)",
          "second_CO2": "number (eV)"
        }
      },
      "description": "Four DFT-computed activation barriers for CO oxidation pathways on Ir1/FeOx. All values in eV."
    }
  ],
  "notes": "The verifier independently compares each barrier to a hidden reference tolerance window and checks structural consistency among the reported barriers. The agent must run the stated DFT workflow to produce these values."
}
```

## How you are scored

A hidden verifier independently reads your `/app/outputs/activation_barriers.json` and compares each barrier value to an independently obtained reference. The verifier also checks internal consistency among the reported barriers. Your final reward is a weighted combination of per-barrier scores. Simply reporting a known literature value without running the DFT computation is not sufficient to pass all checks — the verifier enforces structural relationships that only genuine computations can satisfy.
