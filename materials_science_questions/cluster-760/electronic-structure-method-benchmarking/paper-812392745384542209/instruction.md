# Pt coordination effect on nitrone-nitrile cycloaddition mechanism

## Problem background
The 1,3-dipolar cycloaddition of nitrones to nitriles is a valuable synthetic method, but free nitriles often exhibit low reactivity. Ligation of nitriles to platinum centers has been experimentally observed to promote the reaction, with different efficiency for Pt(II) and Pt(IV) complexes. The mechanistic details and the origin of this activation remain to be quantified. This task focuses on the model reaction of N‑methyl nitrone (H₂C=N(CH₃)O) with free acetonitrile (CH₃CN) and with the platinum‑bound nitriles in trans‑[PtCl₂(NCCH₃)₂] (complex 1) and trans‑[PtCl₄(NCCH₃)₂] (complex 2). The objective is to compute key quantum‑chemical quantities that probe the transition‑state geometry, electronic structure, and energetics, thereby revealing how the metal oxidation state alters the concerted cycloaddition pathway.

## Approach
The reaction is studied at the B3LYP/6‑31G* level of density functional theory. For platinum, a Stuttgart/Dresden effective core potential is used to account for relativistic effects. The computational workflow consists of: (i) full geometry optimization of all reactants (nitrone, free CH₃CN, complexes 1 and 2) and the cycloaddition products; (ii) location of the orientation complexes that precede the transition states on the reaction coordinate; (iii) optimization of the concerted transition states TS1 (free CH₃CN), TS2 (complex 1), and TS3 (complex 2); (iv) harmonic vibrational frequency analysis on every stationary point to confirm the nature of minima and transition states (all minima must have zero imaginary frequencies, each TS must have exactly one) and to obtain thermodynamic corrections; (v) Natural Bond Orbital (NBO) analysis on the transition‑state wavefunctions to extract Wiberg bond indices for the forming C2–O5 and N1–C6 bonds and Natural Population Analysis (NPA) charges on the β‑carbon of the nitrile; (vi) Atoms‑in‑Molecules (AIM) topological analysis on the wavefunctions of TS1 and TS3 to locate bond critical points and obtain the electron density ρ(r_b); and (vii) computation of electronic activation energies (relative to the separated reactants and relative to the orientation complexes) and the synchronicity parameter Sy from bond‑length differences or reciprocal bond orders.

## Reproduction target
Produce a single JSON file named `reproduced_results.json` containing the following computed quantities for the three systems (free CH₃CN, complex 1, complex 2):
- Activation energies Ea (kcal/mol) for TS1, TS2, TS3, each given both relative to the separated reactants and relative to the respective orientation complex.
- Synchronicity parameter Sy for TS1, TS2, and TS3.
- Wiberg bond indices for the two forming contacts (C2–O5 and N1–C6) in each transition state.
- NPA atomic charge on the β‑carbon of the nitrile in free CH₃CN, in complex 1, and in complex 2.
- Electron density ρ(r_b) at the bond critical points of the C2–O5 and N1–C6 contacts in TS1 and in TS3.
The file must strictly follow the schema defined in the output contract. All energy values are in kcal/mol, charges in electrons, and electron densities in e/Å³.

## Assets

- Open-source quantum chemistry package
- NBO analysis tool or built-in population analysis
- AIM topological analysis tool

## Workflow steps

### Step 1: Geometry optimization of reactants and products
- Role: process
- Action: Perform full geometry optimization of N-methyl nitrone (H2C=N(CH3)O), acetonitrile (CH3CN), Pt(II) complex trans-[PtCl2(NCCH3)2] (1), Pt(IV) complex trans-[PtCl4(NCCH3)2] (2), and the cycloaddition products 3, 4, 5 at the B3LYP/6-31G* level. Use an appropriate Stuttgart/Dresden effective core potential for platinum.
- Evidence: `/app/outputs/step_01_optimization.log`

### Step 2: Transition state and orientation complex optimization
- Role: process
- Action: Locate the concerted transition states TS1 (free CH3CN), TS2 (complex 1), TS3 (complex 2) and optimize the orientation complexes OC1, OC2, OC3 at the same level of theory. Confirm each TS has exactly one imaginary vibrational frequency corresponding to the reaction coordinate.
- Evidence: `/app/outputs/step_02_ts_oc.log`

### Step 3: Vibrational frequency analysis and thermodynamic corrections
- Role: process
- Action: Compute harmonic vibrational frequencies for all optimized stationary points (reactants, products, TSs, OCs) at the B3LYP level. Extract zero-point energy corrections, thermal enthalpy, and Gibbs free energy corrections at 298 K. Verify all minima have no imaginary frequencies and each TS has exactly one imaginary frequency.
- Evidence: `/app/outputs/step_03_frequencies.log`

### Step 4: NBO analysis of transition states
- Role: process
- Action: Perform Natural Bond Orbital (NBO) analysis on the wavefunctions of TS1, TS2, and TS3. Extract NPA atomic charges (specifically the β-carbon of the nitrile) and compute Wiberg bond indices for the forming C2-O5 and N1-C6 contacts.
- Evidence: `/app/outputs/step_04_nbo_output.txt`

### Step 5: AIM topological analysis of TS1 and TS3
- Role: process
- Action: Generate wavefunction files for TS1 and TS3 at the B3LYP level. Use an AIM analysis tool to locate bond critical points (BCPs) for the C2-O5 and N1-C6 contacts and extract the electron density ρ(r_b) at each BCP.
- Evidence: `/app/outputs/step_05_aim_output.txt`

### Step 6: Aggregate and report target quantities
- Role: scored (load-bearing)
- Action: Compute electronic activation energies (Ea) relative to the separated reactants and relative to the orientation complexes for the reactions with CH3CN, 1, and 2. Compute the synchronicity parameter Sy for TS1, TS2, TS3 using bond length differences or reciprocal bond orders. Collect the Wiberg bond indices, NPA charges on the nitrile β-carbon, and electron densities at BCPs. Write all values into a single JSON file.
- Output file: `/app/outputs/reproduced_results.json`
- Format: json
- Contract: {"activation_energies":{"TS1":{"Ea_reactant":"float","Ea_OC":"float"},"TS2":{"Ea_reactant":"float","Ea_OC":"float"},"TS3":{"Ea_reactant":"float","Ea_OC":"float"}},"synchronicity_Sy":{"TS1":"float","TS2":"float","TS3":"float"},"Wiberg_indices":{"TS1":{"C2O5":"float","N1C6":"float"},"TS2":{"C2O5":"float","N1C6":"float"},"TS3":{"C2O5":"float","N1C6":"float"}},"NPA_charges_beta_C":{"free_CH3CN":"float","complex1":"float","complex2":"float"},"electron_density_BCP":{"TS1":{"C2O5":"float","N1C6":"float"},"TS3":{"C2O5":"float","N1C6":"float"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_results.json
- path: `/app/outputs/reproduced_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Aggregated reproduction results: activation energies (kcal/mol), synchronicity Sy, Wiberg bond indices, NPA charges (e), and electron densities (e/Å³). Values are compared to the paper’s hidden reference with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `activation_energies`:
      - `TS1`:
        - `Ea_reactant`: float
        - `Ea_OC`: float
      - `TS2`:
        - `Ea_reactant`: float
        - `Ea_OC`: float
      - `TS3`:
        - `Ea_reactant`: float
        - `Ea_OC`: float
    - `synchronicity_Sy`:
      - `TS1`: float
      - `TS2`: float
      - `TS3`: float
    - `Wiberg_indices`:
      - `TS1`:
        - `C2O5`: float
        - `N1C6`: float
      - `TS2`:
        - `C2O5`: float
        - `N1C6`: float
      - `TS3`:
        - `C2O5`: float
        - `N1C6`: float
    - `NPA_charges_beta_C`:
      - `free_CH3CN`: float
      - `complex1`: float
      - `complex2`: float
    - `electron_density_BCP`:
      - `TS1`:
        - `C2O5`: float
        - `N1C6`: float
      - `TS3`:
        - `C2O5`: float
        - `N1C6`: float

Notes: All energy values are in kcal/mol. NPA charges are in electrons. Electron densities are in e/Å³. The synchronicity parameter Sy is unitless.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "activation_energies": {
            "TS1": {
              "Ea_reactant": "float",
              "Ea_OC": "float"
            },
            "TS2": {
              "Ea_reactant": "float",
              "Ea_OC": "float"
            },
            "TS3": {
              "Ea_reactant": "float",
              "Ea_OC": "float"
            }
          },
          "synchronicity_Sy": {
            "TS1": "float",
            "TS2": "float",
            "TS3": "float"
          },
          "Wiberg_indices": {
            "TS1": {
              "C2O5": "float",
              "N1C6": "float"
            },
            "TS2": {
              "C2O5": "float",
              "N1C6": "float"
            },
            "TS3": {
              "C2O5": "float",
              "N1C6": "float"
            }
          },
          "NPA_charges_beta_C": {
            "free_CH3CN": "float",
            "complex1": "float",
            "complex2": "float"
          },
          "electron_density_BCP": {
            "TS1": {
              "C2O5": "float",
              "N1C6": "float"
            },
            "TS3": {
              "C2O5": "float",
              "N1C6": "float"
            }
          }
        }
      },
      "description": "Aggregated reproduction results: activation energies (kcal/mol), synchronicity Sy, Wiberg bond indices, NPA charges (e), and electron densities (e/Å³). Values are compared to the paper’s hidden reference with tolerances."
    }
  ],
  "notes": "All energy values are in kcal/mol. NPA charges are in electrons. Electron densities are in e/Å³. The synchronicity parameter Sy is unitless."
}
```

## How you are scored
Your submitted results will be evaluated by a hidden verifier. The verifier reads the `reproduced_results.json` file and compares each reported value to a set of reference values that correspond to the correct outcome of the computational protocol. Each quantity is checked against a tolerance; meeting the tolerance earns full credit for that item, and larger deviations reduce the score monotonically (i.e., a result that is better than the reference is never penalised). The verifier also checks qualitative trends that must hold for a genuine computation: the activation energies must follow the ordering free CH₃CN > complex 1 > complex 2, and the synchronicity parameter must decrease in the order TS1 > TS2 > TS3. The final reward is a weighted combination of the individual comparisons. Simply reporting numbers without executing the required workflow steps will fail these internal consistency and trend checks.
