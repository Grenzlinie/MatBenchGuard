# Half-metallic phase and first-order transition in the ionic Hubbard model via DMFT

## Problem background
The ionic Hubbard model on a bipartite lattice, with a staggered on-site potential Δ, an on-site Hubbard repulsion U, and nearest-neighbor hopping t, is a minimal model for a correlated band insulator. At half-filling the non-interacting system is a band insulator. When U is turned on, strong correlations are expected to drive a transition from a paramagnetic band insulator to an antiferromagnetic Mott insulator. Upon introducing holes (doping away from half-filling), the interplay of the staggered potential and magnetism can lead to a phase in which one spin channel is conducting while the other is insulating — a half-metallic state. Understanding the magnetic behavior and the emergence of half-metallicity in this model is of fundamental interest for correlated electron systems and for potential spintronic applications. In this task you will compute the key magnetic properties at zero temperature for a fixed Δ=1.0t: the staggered magnetization at half-filling, and the uniform magnetization together with the spin-resolved density of states at the Fermi level for a hole doping of x=0.17.

## Approach
We use dynamical mean-field theory (DMFT) on the Bethe lattice of infinite coordination, combined with an iterated perturbation theory (IPT) impurity solver at zero temperature. The DMFT approach maps the lattice problem onto a single-site impurity hybridizing with a self-consistently determined bath. The self-consistency loop proceeds as follows. Start from an initial guess for the sublattice self-energies and occupancies. Compute the local sublattice Green's functions using the analytic bare density of states of the Bethe lattice, which simplifies the momentum integration. From these, the impurity 'host' Green's functions are extracted via the Dyson equation. The IPT solver then provides new self-energies. The procedure is iterated until convergence. For the half-filled case, the chemical potential is fixed to achieve average filling n=1. For the doped case (x=0.17, target filling n=0.83), the chemical potential must be adjusted during the self-consistency loop to obtain the prescribed density. Once converged solutions are obtained for a set of U/t values, the magnetic order parameters (sublattice magnetizations, staggered and uniform magnetizations) and the spin-resolved single-particle density of states at the Fermi level are computed.

## Reproduction target
Produce two scored CSV files:
- `half_filling_ms.csv` with columns U_t (float) and m_s (float), containing the staggered magnetization m_s as a function of U/t for the half-filled system with Δ=1.0t.
- `doped_mF_dos.csv` with columns U_t (float), m_F (float), rho_up_0 (float), rho_down_0 (float), containing the uniform magnetization and spin-resolved density of states at the Fermi level as functions of U/t for hole doping x=0.17 (filling n=0.83) and Δ=1.0t.
These files will be scored by a hidden verifier against reference data. The expected physical behavior is not disclosed.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: DMFT simulation: half-filling
- Role: process
- Action: Implement the T=0 DMFT self-consistency loop with the IPT impurity solver for the ionic Hubbard model on the Bethe lattice. Use the bare DOS ρ0(ε)=√(4t²−ε²)/(2πt²). For fixed Δ=1.0t, perform the iteration at half-filling (n=1) for a dense set of U/t values covering the first-order transition region. Store the converged sublattice Green's functions and self-energies for each U/t point as an internal intermediate dataset.
- Evidence: none

### Step 2: DMFT simulation: doped case x=0.17
- Role: process
- Action: Repeat the DMFT simulation for a hole doping x=0.17 (target filling n=0.83) with the same Δ=1.0t, adjusting the chemical potential μ to achieve the prescribed density. Perform the self-consistent loop for a range of U/t values crossing the half-metallic regime. Save converged Green's functions, self-energies, and chemical potentials.
- Evidence: none

### Step 3: Half-filling staggered magnetization curve
- Role: scored (load-bearing)
- Action: From the half-filling converged data, compute at each U/t the sublattice occupancies n↑α, n↓α, then the sublattice magnetizations m_zα = n↑α - n↓α, and the staggered magnetization m_s = (m_zB - m_zA)/2. Write a CSV file `half_filling_ms.csv` with columns U_t and m_s.
- Output file: `/app/outputs/half_filling_ms.csv`
- Format: csv
- Contract: columns: U_t (float), m_s (float)
- Scoring: scored by hidden verifier

### Step 4: Doped magnetization and Fermi-level DOS
- Role: scored (load-bearing)
- Action: From the doped converged data, compute the uniform magnetization m_F = (n↑ - n↓) and the spin-resolved density of states at the Fermi level ρ↑(ω=0) and ρ↓(ω=0) for each U/t value. Write a CSV file `doped_mF_dos.csv` with columns U_t, m_F, rho_up_0, rho_down_0.
- Output file: `/app/outputs/doped_mF_dos.csv`
- Format: csv
- Contract: columns: U_t (float), m_F (float), rho_up_0 (float), rho_down_0 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/half_filling_ms.csv`
- `/app/outputs/doped_mF_dos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### half_filling_ms.csv
- path: `/app/outputs/half_filling_ms.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Staggered magnetization m_s vs interaction strength U/t at half-filling for Δ=1.0t.
- schema:
  - `type`: table
  - `required_columns`: `U_t`, `m_s`
  - `units`:
    - `U_t`: dimensionless, normalized by hopping parameter t
    - `m_s`: dimensionless staggered magnetization

### doped_mF_dos.csv
- path: `/app/outputs/doped_mF_dos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Uniform magnetization m_F and spin-resolved DOS at Fermi level vs U/t for doping x=0.17 and Δ=1.0t.
- schema:
  - `type`: table
  - `required_columns`: `U_t`, `m_F`, `rho_up_0`, `rho_down_0`
  - `units`:
    - `U_t`: dimensionless, normalized by t
    - `m_F`: uniform magnetization
    - `rho_up_0`: density of states at Fermi level (arbitrary units)
    - `rho_down_0`: density of states at Fermi level (arbitrary units)

Notes: The checker compares the computed values against reference data from the paper within tolerances. The gold reference data is hidden from the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "half_filling_ms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_t",
          "m_s"
        ],
        "units": {
          "U_t": "dimensionless, normalized by hopping parameter t",
          "m_s": "dimensionless staggered magnetization"
        }
      },
      "description": "Staggered magnetization m_s vs interaction strength U/t at half-filling for Δ=1.0t."
    },
    {
      "file": "doped_mF_dos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "U_t",
          "m_F",
          "rho_up_0",
          "rho_down_0"
        ],
        "units": {
          "U_t": "dimensionless, normalized by t",
          "m_F": "uniform magnetization",
          "rho_up_0": "density of states at Fermi level (arbitrary units)",
          "rho_down_0": "density of states at Fermi level (arbitrary units)"
        }
      },
      "description": "Uniform magnetization m_F and spin-resolved DOS at Fermi level vs U/t for doping x=0.17 and Δ=1.0t."
    }
  ],
  "notes": "The checker compares the computed values against reference data from the paper within tolerances. The gold reference data is hidden from the agent."
}
```

## How you are scored
A hidden verifier will independently assess each scored artifact by comparing the agent's computed values against reference data from the literature. The comparison uses numerical tolerances that account for implementation differences. The verifier does not disclose the expected physical behavior; it only checks quantitative agreement. Each artifact's score is combined by weight to produce your final reward.
