# DFT Investigation of Methanol Adsorption and Formaldehyde Desorption on Vanadia/Ceria

## Problem background
The partial oxidation of methanol to formaldehyde over supported vanadia catalysts is a model system for understanding support effects in heterogeneous catalysis. Ceria (CeO₂) is a particularly active support, and experimental temperature-programmed desorption (TPD) studies on VO₂/CeO₂(111) model catalysts show distinct formaldehyde desorption peaks. Density functional theory (DFT) can provide mechanistic insight by computing the adsorption energies of methanol on different surface sites and the intrinsic barriers for hydrogen-transfer steps that lead to formaldehyde release. The key question is which surface sites participate in the initial chemisorption and in the redox hydrogen-transfer step, and how these steps translate into observable desorption temperatures.

## Approach
We use periodic DFT calculations at the PBE+U+D level (with U on Ce 4f states and a DFT-D2 dispersion correction) to model a VO₂ monomer deposited on a CeO₂(111) slab. The work focuses on two methanol adsorption configurations: (i) methoxide bonded to a vanadium atom at a V–O–Ce interphase site (structure A3), and (ii) methoxide filling a pseudo‑vacancy on the ceria surface (structure A4). For each, we locate the lowest‑energy hydrogen‑transfer transition state (TS2 for A3, TS4 for A4) that leads to formaldehyde. Harmonic vibrational frequencies are computed to obtain zero‑point energy corrections and pre‑exponential factors. The desorption temperature of formaldehyde is simulated by numerically solving the first‑order Polanyi–Wigner desorption equation using a heating rate of 3 K/s, starting from the computed adsorption and barrier energies. The comparison reveals how different active sites and the redox role of ceria control the temperature of the formaldehyde desorption peaks.

## Reproduction target
Compute and report the PBE+U+D zero‑point‑vibration‑corrected adsorption energies (ΔE₀) for methanol on the VO₂/CeO₂(111) surface in the vanadium‑bonded methoxide structure A3 and in the pseudo‑vacancy structure A4. Locate the transition states TS2 and TS4 for the hydrogen‑transfer steps that initiate formaldehyde formation from A3 and A4, and compute the corresponding intrinsic barriers (ΔE‡) including ZPVE corrections. From the vibrational data, derive pre‑exponential factors and use the Polanyi–Wigner equation with a constant heating rate of 3 K/s to determine the formaldehyde desorption temperatures for both pathways. The final deliverables are the two adsorption energies (in eV), the two intrinsic barriers (in eV), and the two desorption temperatures (in K). The relative ordering of the two desorption temperatures is a required trend.

## Assets

- Quantum ESPRESSO (open-source DFT package with DFT+U and dispersion capabilities): https://www.quantum-espresso.org/
- Standard solid-state pseudopotentials (e.g., SSSP efficiency library) for Ce, V, O, H: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct the VO₂·CeO₂(111) periodic slab model
- Role: process
- Action: Build a p(4×4) CeO₂(111) slab of 9 atomic layers (Ce₄₈O₉₆) from bulk CeO₂. Deposit a monomeric VO₂ species on the surface in the configuration described in the paper. Freeze the bottom trilayer atoms. Set vacuum spacing to 10 Å and use an initial cell vector corresponding to the PBE+U lattice constant (15.518 Å).
- Evidence: `/app/outputs/slab_geometry.txt`

### Step 2: Reference calculations for gas‑phase CH₃OH and clean VO₂·CeO₂(111)
- Role: process
- Action: Perform DFT geometry optimization (PBE+U+D, U_eff=4.5 eV, D2 with s₆=0.75) and harmonic vibrational frequency calculations for isolated CH₃OH and for the clean VO₂·CeO₂(111) slab. Obtain total energies and zero‑point vibrational energy (ZPVE) corrections.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Optimize adsorption structures and compute PBE+U+D ZPVE‑corrected adsorption energies for A3 and A4
- Role: scored
- Action: Starting from the clean surface and methanol reference, build initial guesses for adsorption structures A3 (vanadium‑bonded methoxide) and A4 (methoxide in pseudo‑vacancy). Relax geometries at PBE+U+D level; confirm minima by absence of imaginary frequencies. Compute ΔE₀ = E(adsorbed) − E(clean surface) − E(CH₃OH) including ZPVE corrections from the vibrational analysis.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys 'A3_deltaE0' (float, eV) and 'A4_deltaE0' (float, eV).
- Scoring: scored by hidden verifier

### Step 4: Locate transition states TS2 and TS4 and compute vibrational frequencies
- Role: process
- Action: Use the adsorbed structures A3 and A4 as reactants. For TS2: perform NEB and dimer refinement along the H‑transfer path from A3 to a surface oxygen atom (leading to intermediate I6). For TS4: locate the hydrogen transfer from A4 to the closer V–O–Ce interphase oxygen atom (leading to I7). Confirm each TS by a single imaginary frequency. Compute harmonic frequencies for the TS and for the reactant (A3, A4) and product (I6, I7) minima, treating the bottom trilayer as frozen.
- Evidence: `/app/outputs/ts_data.json`

### Step 5: Compute intrinsic barriers and simulated desorption temperatures
- Role: scored (load-bearing)
- Action: From the computed total energies and ZPVE of A3, TS2, I6, A4, TS4, I7, calculate ZPVE‑corrected intrinsic barriers ΔE‡ = E(TS) − E(reactant). Obtain pre‑exponential factors A from the vibrational partition functions of reactant and TS. Then solve the first‑order Polanyi–Wigner desorption equation with a heating rate of 3 K/s to determine the formaldehyde desorption temperatures T_des for the two pathways.
- Output file: `/app/outputs/barriers_and_temperatures.json`
- Format: json
- Contract: JSON object with keys 'TS2_DeltaEdd' (float, eV), 'TS4_DeltaEdd' (float, eV), 'T_des_TS2' (float, K), 'T_des_TS4' (float, K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/barriers_and_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: PBE+U+D ZPVE-corrected adsorption energies ΔE₀ for methanol on VO₂·CeO₂(111) in structures A3 (vanadium‑bonded methoxide) and A4 (methoxide in pseudovacancy).
- schema:
  - `type`: object
  - `required`:
    - `A3_deltaE0`: float (eV)
    - `A4_deltaE0`: float (eV)
  - `units`:
    - `A3_deltaE0`: eV
    - `A4_deltaE0`: eV

### barriers_and_temperatures.json
- path: `/app/outputs/barriers_and_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: ZPVE-corrected intrinsic barriers ΔE‡ (eV) and simulated formaldehyde desorption temperatures T_des (K) for the two low‑energy hydrogen‑transfer pathways (TS2 and TS4) on VO₂·CeO₂(111) at the PBE+U+D level.
- schema:
  - `type`: object
  - `required`:
    - `TS2_DeltaEdd`: float (eV)
    - `TS4_DeltaEdd`: float (eV)
    - `T_des_TS2`: float (K)
    - `T_des_TS4`: float (K)
  - `units`:
    - `TS2_DeltaEdd`: eV
    - `TS4_DeltaEdd`: eV
    - `T_des_TS2`: K
    - `T_des_TS4`: K

Notes: All energies are evaluated at the PBE+U+D level (U_eff=4.5 eV on Ce 4f, D2 with s₆=0.75) and include ZPVE corrections from harmonic vibrational frequencies. The desorption temperatures are obtained by solving the first‑order Polanyi–Wigner equation with a heating rate of 3 K/s. The checker will compare the reported values against the hidden paper‑reported PBE+U+D values with absolute tolerances and verify the relative trend T_des(TS4) < T_des(TS2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A3_deltaE0": "float (eV)",
          "A4_deltaE0": "float (eV)"
        },
        "units": {
          "A3_deltaE0": "eV",
          "A4_deltaE0": "eV"
        }
      },
      "description": "PBE+U+D ZPVE-corrected adsorption energies ΔE₀ for methanol on VO₂·CeO₂(111) in structures A3 (vanadium‑bonded methoxide) and A4 (methoxide in pseudovacancy)."
    },
    {
      "file": "barriers_and_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "TS2_DeltaEdd": "float (eV)",
          "TS4_DeltaEdd": "float (eV)",
          "T_des_TS2": "float (K)",
          "T_des_TS4": "float (K)"
        },
        "units": {
          "TS2_DeltaEdd": "eV",
          "TS4_DeltaEdd": "eV",
          "T_des_TS2": "K",
          "T_des_TS4": "K"
        }
      },
      "description": "ZPVE-corrected intrinsic barriers ΔE‡ (eV) and simulated formaldehyde desorption temperatures T_des (K) for the two low‑energy hydrogen‑transfer pathways (TS2 and TS4) on VO₂·CeO₂(111) at the PBE+U+D level."
    }
  ],
  "notes": "All energies are evaluated at the PBE+U+D level (U_eff=4.5 eV on Ce 4f, D2 with s₆=0.75) and include ZPVE corrections from harmonic vibrational frequencies. The desorption temperatures are obtained by solving the first‑order Polanyi–Wigner equation with a heating rate of 3 K/s. The checker will compare the reported values against the hidden paper‑reported PBE+U+D values with absolute tolerances and verify the relative trend T_des(TS4) < T_des(TS2)."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier. For the scored outputs (adsorption energies, barriers, and desorption temperatures), the verifier compares your reported numbers against reference values using appropriate tolerances that account for typical variations between different DFT implementations and computational setups. It also checks a structural consistency requirement: the desorption temperature associated with TS4 must be lower than that for TS2. Partial credit is awarded based on how closely your results meet the reference values and the required trend. The final score is a weighted combination across all scored stages, with the main barriers and temperatures carrying the highest weight. Reporting the paper's published numbers without actually performing the computations will not pass the verification checks.
