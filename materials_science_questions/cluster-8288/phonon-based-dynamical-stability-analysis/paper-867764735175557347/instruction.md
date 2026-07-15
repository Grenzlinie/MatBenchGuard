# Phonon-based thermodynamic stability analysis of calcium peroxide under high pressure

## Problem background
Calcium peroxide (CaO₂) is a compound of calcium and oxygen in the peroxide oxidation state, known at ambient pressure but with limited high-pressure study. The question addressed is whether CaO₂ is thermodynamically stable against decomposition into CaO and molecular oxygen over a pressure range of 0–200 GPa, both at static conditions and at the high temperatures found in planetary mantles. You will use density functional theory (DFT) and quasiharmonic phonon calculations to investigate the relative stability of competing crystal structures of CaO₂, CaO, and O₂, determine the decomposition enthalpy and Gibbs free energy, map the phase transitions, and examine the electronic band gap of a key high-pressure phase.

## Approach
You will perform plane‑wave DFT calculations with the PBE exchange‑correlation functional to compute static‑lattice enthalpies for all relevant phases (provided crystal structures for CaO₂, rocksalt/CsCl CaO, and the lowest‑enthalpy O₂ phases) on a pressure grid from 0 to 200 GPa. From these enthalpies you will extract the static decomposition enthalpy for CaO₂ → CaO + ½O₂. To include temperature effects, you will compute phonon dispersions via the finite‑displacement supercell method within the quasiharmonic approximation, yielding Gibbs free energies. By comparing the free energies of the competing phases you will construct the pressure‑temperature phase diagram and obtain the decomposition Gibbs free energy at mantle conditions (65 GPa, 2500 K). Finally, you will calculate the electronic band structure and density of states for the P2₁/c‑L CaO₂ phase at 50 GPa to determine its thermal and optical band gaps. All calculations use open‑source tools (Quantum ESPRESSO, PhonoPy) and the provided structural data.

## Reproduction target
Your concrete objectives are:
- Compute the static‑lattice decomposition enthalpy ΔH for CaO₂ → CaO + ½O₂ at 65 GPa.
- Compute the Gibbs free energy change ΔG for the same reaction at 65 GPa and 2500 K.
- Determine the sequence of lowest‑enthalpy (0 K) and lowest‑free‑energy (300 K) CaO₂ phases as a function of pressure, yielding the phase transition pressures.
- Report the thermal and optical band gaps of the P2₁/c‑L CaO₂ phase at 50 GPa.
All outputs must be written to the files described in the workflow steps below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PhonoPy: phonopy
- PBE pseudopotentials for Ca and O: https://www.pseudo-dojo.org/
- Crystal structure data for CaO₂, CaO, and O₂ phases

## Workflow steps

### Step 1: Build structures and set DFT parameters
- Role: process
- Action: Construct primitive cells for all required phases (CaO₂ candidates, CaO reference phases, O₂ reference phases) using the provided lattice constants and atomic coordinates. Set up DFT convergence parameters: PBE exchange-correlation, plane-wave cutoff, k‑point sampling. Write a structure manifest file.
- Evidence: `/app/outputs/structure_manifest.txt`

### Step 2: Run static-lattice DFT relaxations
- Role: process
- Action: For each phase, perform variable‑cell geometry relaxation and total‑energy calculations at a grid of pressures: 0, 10, 20, 30, 38, 50, 65, 100, 150, 200 GPa using Quantum ESPRESSO. Record the final enthalpy and volume for each run.
- Evidence: none

### Step 3: Compile static enthalpies
- Role: scored (load-bearing)
- Action: Aggregate the computed static‑lattice enthalpies into a single table. Write /app/outputs/static_enthalpies.csv with one row per (pressure, phase).
- Output file: `/app/outputs/static_enthalpies.csv`
- Format: csv
- Contract: pressure(GPa):float, phase:string, enthalpy(eV/f.u.):float
- Scoring: scored by hidden verifier

### Step 4: Perform quasiharmonic phonon calculations
- Role: process
- Action: For the six CaO₂ phases (C2/c‑I, C2/c‑II, Pna2₁, I4/mcm, P2₁/c‑L, P2₁/c‑H) and the reference phases (rocksalt CaO, CsCl CaO, lowest‑enthalpy O₂ phase at each pressure), construct supercells and compute phonon frequencies via finite‑displacement using Quantum ESPRESSO + PhonoPy at pressures 0, 20, 30, 38, 50, 65, 100 GPa. Use the quasiharmonic approximation to obtain the Gibbs free energy at temperatures 0, 300, 600, 1000 K, and at 2500 K for the mantle condition (65 GPa).
- Evidence: none

### Step 5: Compile Gibbs free energies
- Role: scored (load-bearing)
- Action: Assemble the Gibbs free energies into a table. Write /app/outputs/gibbs_free_energies.csv with one row per (pressure, temperature, phase).
- Output file: `/app/outputs/gibbs_free_energies.csv`
- Format: csv
- Contract: pressure(GPa):float, temperature(K):int, phase:string, gibbs_free_energy(eV/f.u.):float
- Scoring: scored by hidden verifier

### Step 6: Electronic bandgap of P2₁/c‑L at 50 GPa
- Role: scored
- Action: For the relaxed P2₁/c‑L structure at 50 GPa, compute the band structure and density of states with Quantum ESPRESSO, and extract the thermal and optical bandgaps. Write /app/outputs/bandgap.json containing the two values.
- Output file: `/app/outputs/bandgap.json`
- Format: json
- Contract: {thermal_bandgap_eV: number, optical_bandgap_eV: number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_enthalpies.csv`
- `/app/outputs/gibbs_free_energies.csv`
- `/app/outputs/bandgap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_enthalpies.csv
- path: `/app/outputs/static_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Decomposition enthalpy ΔH at 65 GPa and positivity across the pressure range will be recomputed from these data.
- schema:
  - `type`: table
  - `required_columns`: `pressure(GPa)`, `phase`, `enthalpy(eV/f.u.)`

### gibbs_free_energies.csv
- path: `/app/outputs/gibbs_free_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Decomposition Gibbs free energy ΔG at 65 GPa and 2500 K will be recomputed from these data.
- schema:
  - `type`: table
  - `required_columns`: `pressure(GPa)`, `temperature(K)`, `phase`, `gibbs_free_energy(eV/f.u.)`

### bandgap.json
- path: `/app/outputs/bandgap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermal and optical bandgaps compared to the computed reference values.
- schema:
  - `type`: object
  - `required`:
    - `thermal_bandgap_eV`: number
    - `optical_bandgap_eV`: number

Notes: All output files are read by the hidden checker. The checker recomputes decomposition enthalpy and Gibbs free energy from the tables using the known reference phases, and compares bandgaps within tolerance. No gold values are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure(GPa)",
          "phase",
          "enthalpy(eV/f.u.)"
        ]
      },
      "description": "Decomposition enthalpy ΔH at 65 GPa and positivity across the pressure range will be recomputed from these data."
    },
    {
      "file": "gibbs_free_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure(GPa)",
          "temperature(K)",
          "phase",
          "gibbs_free_energy(eV/f.u.)"
        ]
      },
      "description": "Decomposition Gibbs free energy ΔG at 65 GPa and 2500 K will be recomputed from these data."
    },
    {
      "file": "bandgap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "thermal_bandgap_eV": "number",
          "optical_bandgap_eV": "number"
        }
      },
      "description": "Thermal and optical bandgaps compared to the computed reference values."
    }
  ],
  "notes": "All output files are read by the hidden checker. The checker recomputes decomposition enthalpy and Gibbs free energy from the tables using the known reference phases, and compares bandgaps within tolerance. No gold values are exposed."
}
```

## How you are scored
A hidden verifier reads the files you produce under /app/outputs and independently recomputes the key quantities:
- From `static_enthalpies.csv` it computes the decomposition enthalpy at each pressure and verifies that the decomposition reaction is thermodynamically favourable or unfavourable according to the physics you were asked to reproduce.
- From `gibbs_free_energies.csv` it computes the decomposition Gibbs free energy at the specified mantle conditions and checks the phase stability ordering across pressures and temperatures.
- From `bandgap.json` it compares your reported thermal and optical gaps to a hidden reference.
Each scored artifact contributes a weighted portion to your total reward, which is a single float between 0 and 1. The verifier does not require you to match a particular published number with arbitrarily small tolerance; it expects physically reasonable results that are consistent with the underlying theory and the input data. The final reward is based on how correctly your computations capture the relative stability and electronic properties, not on reporting any specific values.
