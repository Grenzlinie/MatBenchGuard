# Thermoelectric transport modeling of a layered chalcogenide semiconductor

## Problem background
Bi₂MnTe₄ is a newly discovered layered chalcogenide semiconductor with a rhombohedral R-3m structure, formed by septuple monoatomic layers stacked along the c-axis. Its electronic structure and thermoelectric transport properties are of fundamental and practical interest. First-principles electronic structure calculations and Boltzmann transport theory predictions are used to understand its carrier behavior and quantify key transport figures of merit such as the Seebeck coefficient and electrical conductivity. This task reproduces the core computational workflow to compute the spin-polarized density of states and the room-temperature transport coefficients from the known crystal structure.

## Approach
We employ spin-polarized density functional theory (DFT) within the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation. Starting from the publicly available crystal structure (CIF file), the atomic positions are relaxed, and the self-consistent charge density, wavefunctions, and band structure are obtained using an open-source plane-wave DFT code (Quantum ESPRESSO). From the converged charge density, the spin-resolved density of states (DOS) is computed and the DOS at the Fermi level for majority (up) and minority (down) spin channels is extracted, along with the band gap of the minority spin channel. The DFT band energies are then fed into the Boltzmann transport code BoltzTrap2, which solves the semiclassical Boltzmann equation in the constant relaxation time approximation. The Seebeck coefficient and electrical conductivity divided by relaxation time are evaluated as functions of chemical potential at 300 K. Finally, we record the values at the Fermi level, the maximum Seebeck coefficient, and the chemical potential (relative to the Fermi level) at which that maximum occurs.

## Reproduction target
Using the publicly available crystal structure of Bi₂MnTe₄ (CCDC 933860), perform spin‑polarized DFT calculations with a PBE exchange‑correlation functional to produce the self‑consistent charge density and band structure. Compute the spin‑polarized density of states at the Fermi level for both majority and minority spin channels and write the results to a CSV file. Determine the minority spin band gap and record it as a single number in a text file. From the DFT band energies, apply Boltzmann transport theory via BoltzTrap2 to calculate the Seebeck coefficient and electrical conductivity per relaxation time as functions of chemical potential at 300 K. Extract the values at the Fermi level, the maximum Seebeck coefficient, and the chemical potential at which the maximum occurs, and output them as a JSON object. All outputs must adhere exactly to the output contract specified below.

## Assets

- Bi₂MnTe₄ crystal structure (CIF): https://doi.org/10.1039/c3ce40643a
- Quantum ESPRESSO: https://www.quantum-espresso.org
- BoltzTrap2: https://gitlab.com/sousaw/BoltzTrap2
- SSSP pseudopotentials (PBE): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT spin-polarized self-consistent calculation
- Role: process
- Action: Perform a spin-polarized DFT calculation with PBE exchange-correlation functional to relax the atomic positions and obtain the self-consistent charge density, wavefunctions, and band structure for Bi₂MnTe₄. Use the publicly available CIF file as the starting structure.
- Evidence: `/app/outputs/dft_log.txt`

### Step 2: Compute spin-polarized DOS at Fermi level
- Role: scored
- Action: From the DFT self-consistent output, compute the spin-polarized density of states and extract the DOS value at the Fermi level for both majority (up) and minority (down) spin channels.
- Output file: `/app/outputs/step_03_dos_at_ef.csv`
- Format: csv
- Contract: CSV with headers: spin, dos_f. Two rows: up, down. dos_f is a floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Compute minority spin band gap
- Role: scored
- Action: From the DFT band structure or DOS, determine the band gap (eV) for the minority spin channel.
- Output file: `/app/outputs/step_03_bandgap.txt`
- Format: txt
- Contract: Single floating-point number, e.g., '0.40'.
- Scoring: scored by hidden verifier

### Step 4: Compute Boltzmann transport properties
- Role: scored (load-bearing)
- Action: Using BoltzTrap2, compute the Seebeck coefficient and electrical conductivity per relaxation time as functions of chemical potential at 300 K from the DFT band energies. Extract the values at the Fermi level (Seebeck_at_EF, sigma_over_tau_at_EF), the maximum Seebeck coefficient and the chemical potential (relative to Fermi level) at which it occurs.
- Output file: `/app/outputs/step_04_transport_at_ef.json`
- Format: json
- Contract: JSON object with keys: Seebeck_at_EF (float, µV/K), sigma_over_tau_at_EF (float, S/(cm·s)), Seebeck_max (float, µV/K), Seebeck_max_mu (float, eV relative to Fermi level).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_dos_at_ef.csv`
- `/app/outputs/step_03_bandgap.txt`
- `/app/outputs/step_04_transport_at_ef.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_dos_at_ef.csv
- path: `/app/outputs/step_03_dos_at_ef.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Spin-polarized density of states at the Fermi level. Majority spin should be non-zero; minority spin should be near zero.
- schema:
  - `type`: table
  - `required_columns`: `spin`, `dos_f`
  - `items`:
    - `spin`: string (up or down)
    - `dos_f`: float (states/eV/spin)

### step_03_bandgap.txt
- path: `/app/outputs/step_03_bandgap.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Band gap (eV) for the minority spin channel.
- schema:
  - `type`: text
  - `content`: single floating-point number in eV

### step_04_transport_at_ef.json
- path: `/app/outputs/step_04_transport_at_ef.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Transport coefficients at 300 K: Seebeck coefficient and electrical conductivity per relaxation time at the Fermi level, maximum Seebeck coefficient and its chemical potential location.
- schema:
  - `type`: object
  - `required`: `Seebeck_at_EF`, `sigma_over_tau_at_EF`, `Seebeck_max`, `Seebeck_max_mu`
  - `units`:
    - `Seebeck_at_EF`: µV/K
    - `sigma_over_tau_at_EF`: S/(cm·s)
    - `Seebeck_max`: µV/K
    - `Seebeck_max_mu`: eV

Notes: All output files must be placed under /app/outputs. The DFT process step must be executed by the agent; no precomputed charge density is provided. Verifier will check structural properties (sign, approximate magnitude) for DOS and gap, and compare transport values to hidden references.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_dos_at_ef.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "spin",
          "dos_f"
        ],
        "items": {
          "spin": "string (up or down)",
          "dos_f": "float (states/eV/spin)"
        }
      },
      "description": "Spin-polarized density of states at the Fermi level. Majority spin should be non-zero; minority spin should be near zero."
    },
    {
      "file": "step_03_bandgap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "content": "single floating-point number in eV"
      },
      "description": "Band gap (eV) for the minority spin channel."
    },
    {
      "file": "step_04_transport_at_ef.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Seebeck_at_EF",
          "sigma_over_tau_at_EF",
          "Seebeck_max",
          "Seebeck_max_mu"
        ],
        "units": {
          "Seebeck_at_EF": "µV/K",
          "sigma_over_tau_at_EF": "S/(cm·s)",
          "Seebeck_max": "µV/K",
          "Seebeck_max_mu": "eV"
        }
      },
      "description": "Transport coefficients at 300 K: Seebeck coefficient and electrical conductivity per relaxation time at the Fermi level, maximum Seebeck coefficient and its chemical potential location."
    }
  ],
  "notes": "All output files must be placed under /app/outputs. The DFT process step must be executed by the agent; no precomputed charge density is provided. Verifier will check structural properties (sign, approximate magnitude) for DOS and gap, and compare transport values to hidden references."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the output files you placed under `/app/outputs`. Each of the three scored artifacts is checked independently:  
- The spin‑polarized DOS at the Fermi level is checked for correct structural features (majority spin DOS non‑zero, minority spin DOS negligible).  
- The minority spin band gap is compared against a physically plausible reference range.  
- The transport quantities (Seebeck at EF, σ/τ at EF, maximum Seebeck, and its location) are compared to hidden reference values using generous tolerances that accommodate differences in DFT implementations, pseudopotentials, and k‑point sampling.  
The final reward is a weighted combination of the scores from these three stages. Merely reporting the paper’s published numbers without re‑executing the calculations will not yield a passing score; you must genuinely run the DFT and Boltzmann transport workflow and submit the outputs of your own computation.
