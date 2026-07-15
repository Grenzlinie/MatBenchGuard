# Strain-Dependent Energy Barrier for Polarization Switching in 2D Ferroelectric

## Problem background
Monolayer α‑In₂Se₃ is a two‑dimensional ferroelectric material whose out‑of‑plane polarization originates from an asymmetric stacking of Se layers. The polarization can be reversed by an in‑plane shift of the central selenium layer, but this switching is gated by an energy barrier. Understanding how uniform in‑plane strain — either compressive or tensile — alters that barrier is essential for strain engineering of 2D ferroelectric devices. In this task you will quantify the relationship between in‑plane strain and the switching barrier by performing first‑principles calculations.

## Approach
The approach relies on density functional theory (DFT) to compute the minimum‑energy path for the in‑plane displacement of the middle Se atom that reverses the out‑of‑plane polarization. For a monolayer α‑In₂Se₃ unit cell, the atomic positions are relaxed at the endpoints and along a set of images connecting the two polarization states (e.g., using the nudged elastic band method). The highest point on this path gives the energy barrier. By repeating this calculation for different uniform in‑plane strains — ranging from compression to tension — you will map how the barrier changes. All DFT calculations are performed with the open‑source Quantum ESPRESSO package using pseudopotentials from the SSSP efficiency library (In and Se).

## Reproduction target
Compute the energy barrier (eV) for polarization switching in monolayer α‑In₂Se₃ at the following uniform in‑plane strains: −3%, −2%, −1%, 0%, +1%, +2%, +3%, +4% (at least these eight points). Store the results in `/app/outputs/energy_barriers.csv` as a two‑column table: `strain` (%, float) and `energy_barrier` (eV, float). The barrier values must be obtained from a converged DFT minimum‑energy path (or equivalent) for each strain.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials (In, Se): https://www.materialscloud.org/discover/sssp/table/efficiency
- Monolayer α-In₂Se₃ crystal structure

## Workflow steps

### Step 1: DFT energy barrier vs. strain
- Role: scored
- Action: Perform density functional theory (DFT) calculations to obtain the minimum energy path and extract the energy barrier for the in-plane shift of the middle Se layer that reverses out-of-plane polarization in monolayer α-In₂Se₃. Calculate the barrier at uniform in-plane strains of −3%, −2%, −1%, 0%, +1%, +2%, +3%, +4% (at least these eight points). Use an open-source DFT code (e.g., Quantum ESPRESSO) with appropriate pseudopotentials (e.g., from the SSSP efficiency library) and standard convergence settings. For each strain, report the energy barrier in eV.
- Output file: `/app/outputs/energy_barriers.csv`
- Format: csv
- Contract: Two columns: strain (float, %), energy_barrier (float, eV). Rows must cover at least the strains −3.0, −2.0, −1.0, 0.0, 1.0, 2.0, 3.0, 4.0 (or equivalent).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_barriers.csv
- path: `/app/outputs/energy_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy barrier for out-of-plane polarization switching in monolayer α-In₂Se₃ under uniform in-plane strain.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `energy_barrier`
  - `units`:
    - `strain`: %
    - `energy_barrier`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "energy_barrier"
        ],
        "units": {
          "strain": "%",
          "energy_barrier": "eV"
        }
      },
      "description": "Energy barrier for out-of-plane polarization switching in monolayer α-In₂Se₃ under uniform in-plane strain."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be automatically evaluated by a hidden verifier. The verifier reads `energy_barriers.csv` and compares the barrier values and their dependence on strain against a hidden reference. It checks for quantitative accuracy (e.g., agreement of the barrier magnitude at each strain) and for physically correct qualitative features (such as the overall trend and monotonicity) within tolerances that account for typical spread between different DFT implementations. The verifier returns a single reward between 0 (completely incorrect) and 1 (fully correct). The details of the reference and the tolerances are not disclosed, so you must perform a genuine DFT calculation; guessing or fabricating numbers that happen to satisfy a simple qualitative rule will not reliably score high.
