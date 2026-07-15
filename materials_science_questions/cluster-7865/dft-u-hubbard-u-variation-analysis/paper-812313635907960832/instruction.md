# Self-Consistent Hubbard U and Lithium Intercalation Voltage from DFT+U

## Problem background
Standard density functional theory (DFT) within the local density approximation (LDA) or generalized gradient approximation (GGA) systematically underestimates the redox potential of lithium intercalation in transition metal compounds. This error is believed to originate from the poor description of electron self-interaction on localized transition metal d states. The DFT+U method, which adds a Hubbard-like on-site Coulomb repulsion U to the functional, offers a way to treat these correlation effects. This task investigates whether using GGA+U with self-consistently computed Hubbard U values from linear response can yield more accurate lithium intercalation voltages. The goal is to compute the Hubbard U parameters for Mn, Fe, Co, and Ni in different oxidation states and crystal environments (olivine, layered, spinel) and then use those U values to calculate average lithium intercalation voltages, which can be compared to experimental measurements.

## Approach
The reproduction follows a multi-stage computational protocol. First, spin-polarized GGA reference calculations are performed for all end-member compounds to obtain relaxed structures and d-orbital occupation matrices. Next, the self-consistent Hubbard U for each transition metal ion is determined via the linear-response method: a localized perturbation is applied to the d-orbital potential, and the screened and bare response matrices are calculated from the induced occupation changes; U is then given by the difference of the inverse matrices. Using the computed U values, GGA+U total energy calculations are carried out for all lithiated and delithiated phases, including full structural relaxation. Finally, the average lithium intercalation voltage for each redox couple is obtained from the total energy differences using the standard electrochemical formula. The computed voltages are to be compared against the experimental values to evaluate the improvement over pure GGA. The computational workflow is implementable with an open-source DFT package employing pseudopotentials and a linear-response module.

## Reproduction target
Produce two scored output files. The first, `computed_U_values.json`, must contain the self-consistent Hubbard U parameters (in eV) for every transition metal ion, oxidation state, and crystal structure combination listed in the study: olivine LiMPO4/MPO4 (M = Mn, Fe, Co, Ni) for M2+/M3+ (plus M4+ where applicable, e.g., Co4+ in spinel); layered LiMO2/MO2 (M = Co, Ni) for M3+/M4+; and spinel LiM2O4/M2O4 and Li2M2O4/LiM2O4 (M = Mn, Co) for M3+/M4+. The second file, `computed_voltages.csv`, must list the average lithium intercalation voltage (in V) for every redox couple: LiMnPO4/MnPO4, LiFePO4/FePO4, LiCoPO4/CoPO4, LiNiPO4/NiPO4, LiCoO2/CoO2, LiNiO2/NiO2, plus the two distinct voltage plateaus for LiMn2O4 (0 < x < 1 and 1 < x < 2) and the 1 < x < 2 plateau for LiCo2O4. The voltages are calculated from the total energies of the lithiated and delithiated end-members and the energy of metallic Li. The file may optionally include experimental reference voltages, but the scoring is based solely on the computed voltage column.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials (SSSP or QE library): https://www.quantum-espresso.org/pseudopotentials
- Crystal structure definitions for LiMPO4 (olivine), LiMO2 (layered), LiM2O4 (spinel) in lithiated/delithiated states

## Workflow steps

### Step 1: GGA reference calculations
- Role: process
- Action: Run spin-polarized GGA calculations for all lithiated and delithiated TM compounds: olivine LiMPO4 (M=Mn,Fe,Co,Ni), layered LiMO2 (M=Co,Ni), and spinel LiM2O4 (M=Mn,Co). Perform full structural relaxation, obtain total energies and d-orbital occupation matrices (U=0 reference). Use high-spin states and the magnetic orderings consistent with the paper (AFM for olivines, FM for layered/spinel).
- Evidence: `/app/outputs/gga_reference.log`

### Step 2: Compute Hubbard U values via linear response
- Role: scored
- Action: Using the GGA reference structures and occupation matrices from step1, apply the linear-response method (e.g., hp.x in Quantum ESPRESSO) to calculate the self-consistent Hubbard U parameter for each TM ion in each valence and crystal environment. For each site, apply a local perturbation dV = α P_d, compute the screened (χ) and bare (χ0) response matrices from d-manifold occupation changes, and obtain U = (χ0⁻¹ - χ⁻¹)ᵢᵢ. Converge in supercell size. Compile all resulting U values (in eV) into a JSON file.
- Output file: `/app/outputs/computed_U_values.json`
- Format: json
- Contract: JSON object: keys are compound identifiers like "Mn2+_olivine", "Fe3+_spinel", etc.; values are floating-point numbers (U in eV). Includes all entries from Table II.
- Scoring: scored by hidden verifier

### Step 3: DFT+U total energy calculations
- Role: process
- Action: Perform spin-polarized GGA+U calculations for all lithiated/delithiated end-member phases using the U values from step2. Include full structural relaxation. Use high-spin states and the same magnetic orderings as in step1. Compute also the total energy of metallic Li (bcc) with the same functional and pseudopotentials.
- Evidence: `/app/outputs/dft_u_total_energies.txt`

### Step 4: Compute average lithium intercalation voltages
- Role: scored (load-bearing)
- Action: Calculate the average lithium intercalation voltage for each redox couple from the DFT+U total energies of step3. Use the formula ⟨V⟩ = -[E(Liₓ₂MOy) - E(Liₓ₁MOy) - (x₂-x₁)E(Li metal)]/((x₂-x₁)F), with x₁=0 and x₂=1 unless otherwise noted. For spinel LiₓM₂O₄, compute separate voltages for the 0<x<1 and 1<x<2 plateaus. Produce a CSV file.
- Output file: `/app/outputs/computed_voltages.csv`
- Format: csv
- Contract: Columns: compound (string), computed_voltage (float, V), experimental_voltage (float, V). The experimental column may be filled with literature values or left blank; scoring uses only computed_voltage.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_U_values.json`
- `/app/outputs/computed_voltages.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_U_values.json
- path: `/app/outputs/computed_U_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON dictionary of self-consistent Hubbard U values (eV). Keys like "Mn2+_olivine", values are floats.
- schema:
  - `type`: object
  - `required`: object
  - `items`:
    - `compound_identifier`: float
  - `description`: Self-consistent Hubbard U parameters (eV) for each TM ion/valence/environment combination listed in the paper's Table II.

### computed_voltages.csv
- path: `/app/outputs/computed_voltages.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of average lithium intercalation voltages for all redox couples, including optional experimental reference. Scoring uses the computed_voltage column.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `computed_voltage`, `experimental_voltage`
  - `units`:
    - `computed_voltage`: V
    - `experimental_voltage`: V

Notes: The checker compares the agent's computed U values and voltages to the paper-reported gold values within hidden tolerances. Voltage comparison uses the paper's GGA+U calculated values and/or experimental voltages; the agent must produce all entries from the paper's full dataset.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_U_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {},
        "items": {
          "compound_identifier": "float"
        },
        "description": "Self-consistent Hubbard U parameters (eV) for each TM ion/valence/environment combination listed in the paper's Table II."
      },
      "description": "JSON dictionary of self-consistent Hubbard U values (eV). Keys like \"Mn2+_olivine\", values are floats."
    },
    {
      "file": "computed_voltages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "computed_voltage",
          "experimental_voltage"
        ],
        "units": {
          "computed_voltage": "V",
          "experimental_voltage": "V"
        }
      },
      "description": "CSV table of average lithium intercalation voltages for all redox couples, including optional experimental reference. Scoring uses the computed_voltage column."
    }
  ],
  "notes": "The checker compares the agent's computed U values and voltages to the paper-reported gold values within hidden tolerances. Voltage comparison uses the paper's GGA+U calculated values and/or experimental voltages; the agent must produce all entries from the paper's full dataset."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. For `computed_U_values.json`, the verifier compares your submitted Hubbard U values to reference values (the paper's reported self-consistent U values) within a numerical tolerance, and also checks that physical trends hold: U increases with higher oxidation state, and U is larger in olivine than in close-packed oxides for the same valence. For `computed_voltages.csv`, the verifier compares your computed voltages to reference values (the paper's GGA+U voltages or the experimental voltages) within a tolerance. The reward is the fraction of values that fall within the allowed tolerance and that satisfy the structural trend checks. Each scored stage carries a weight; the final overall reward is a weighted sum. Simply reporting numbers copied from the literature will not pass—the verifier expects that a genuine DFT+U pipeline was executed, and the agreement with the reference must arise from that computation. No gold values or tolerances are disclosed here.
