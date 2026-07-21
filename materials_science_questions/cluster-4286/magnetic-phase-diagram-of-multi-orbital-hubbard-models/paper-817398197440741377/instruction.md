# Magnetic phase diagram of multi-orbital Hubbard models with Hund's coupling

## Problem background
Antiferromagnetic ordering in uranium compounds often involves multiple 5f orbitals with competing intraorbital and interorbital interactions. The underscreened Anderson lattice model (UALM) captures this physics by considering two narrow 5f bands (α and β) that hybridize asymmetrically with a single conduction band, with onsite Coulomb repulsion U and Hund's exchange J coupling electrons in different orbitals. Tuning the bandwidth (e.g., via pressure) can drive transitions between distinct antiferromagnetic (AF) phases. Understanding whether such a model can host multiple AF phases separated by first-order transitions, and the resulting temperature–bandwidth phase diagram, is the open question to be computed here.

## Approach
Use a Hartree–Fock mean-field decoupling of the UALM Hamiltonian on a three-dimensional cubic lattice with a commensurate antiferromagnetic ordering wavevector Q = (π,π,π). The single-band conduction electrons and the two f‑band orbitals (α hybridized, β not) are described by tight‑binding dispersions with given band centers and hopping amplitudes. The interaction is treated by decoupling into intraorbital antiferromagnetic order parameters (staggered magnetizations m_α, m_β) and their spin gaps Δ_α, Δ_β. Solve the coupled self‑consistency equations iteratively at T = 0 and at finite temperature for a range of bandwidth W that controls the hopping amplitudes. Evaluate the Hartree–Fock free energy to determine the thermodynamically stable solution. From the T = 0 solutions, identify the magnetic states (AF1, AF2, paramagnetic) by comparing the sizes of m_α and m_β. Extend to finite temperatures and construct the phase diagram by: (i) locating the second‑order Néel line from the linearized instability condition of the paramagnetic state; (ii) tracking the free‑energy crossing of the AF1 and AF2 solutions to map the first‑order AF1–AF2 boundary; (iii) similarly tracking the AF2–PM boundary, including locating the tricritical point where the transition changes order.

## Reproduction target
Produce two CSV artifacts. First, a file (`step_01_order_params.csv`) containing the zero‑temperature staggered magnetizations m_α and m_β as functions of the bandwidth W (in eV) over the range 0.5–2.0 eV, with sufficient resolution to capture the locations of the first‑order transitions. Second, a file (`step_02_phase_boundaries.csv`) listing the phase boundaries in the (W,T) plane for three boundary types: the second‑order Néel line (label 'Neel'), the first‑order AF1–AF2 transition line (label 'AF1_AF2_first_order'), and the first‑order AF2–PM transition line (label 'AF2_PM_first_order'). Include enough points along each boundary to clearly resolve the critical end point (CEP) on the AF1–AF2 line and the tricritical point (TCP) on the AF2–PM line.

## Assets

- Python scientific computing stack (NumPy, SciPy, matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Hartree-Fock self-consistent calculation of antiferromagnetic order
- Role: process
- Action: Implement the two-orbital underscreened Anderson lattice model with tight‑binding dispersions on a cubic lattice, asymmetric hybridization (Vβ=0), Coulomb U=0.165 eV, Hund's J=U/5, total occupancy Ntot=1.609, and the specified tight‑binding parameters (ε̃f=0.3 eV, t_d=W_d/6, t_f=W_d/20, Vα=1/10 eV, W_f/W_d=0.3). Perform Hartree-Fock mean-field decoupling for intraorbital antiferromagnetic order at Q=(π,π,π). Solve the coupled self‑consistency equations for the staggered magnetizations m_α, m_β and the spin gaps Δα,Δβ as functions of bandwidth W (range 0.5–2.0 eV) and temperature T (range 0 to above TN). Evaluate the free energy to monitor phase stability.
- Evidence: `/app/outputs/hf_solver.log`

### Step 2: Zero-temperature order parameters
- Role: scored (load-bearing)
- Action: From the T=0 self‑consistent solutions, extract the staggered magnetizations m_α and m_β for a dense set of bandwidth values W in [0.5,2.0] (at least 20 points, plus extra points near the two first‑order transitions). Write a CSV with columns W, m_alpha, m_beta.
- Output file: `/app/outputs/step_01_order_params.csv`
- Format: csv
- Contract: CSV with header: W,m_alpha,m_beta. All values are floats. W in eV, m_alpha and m_beta dimensionless.
- Scoring: scored by hidden verifier

### Step 3: Temperature–bandwidth phase diagram
- Role: scored
- Action: Using the finite-temperature self‑consistent solutions and free-energy analysis, determine the phase boundaries: the second‑order Néel line (from the linearized instability condition), the first‑order AF1–AF2 transition line ending at a critical end point, and the first‑order AF2–PM transition line with a tricritical point. Write a CSV with columns W, T, boundary_type, including enough points to clearly locate the CEP and TCP.
- Output file: `/app/outputs/step_02_phase_boundaries.csv`
- Format: csv
- Contract: CSV with header: W,T,boundary_type. W and T are floats (T in eV). boundary_type is one of: 'Neel', 'AF1_AF2_first_order', 'AF2_PM_first_order'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_order_params.csv`
- `/app/outputs/step_02_phase_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_order_params.csv
- path: `/app/outputs/step_01_order_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Numerical values of zero-temperature staggered magnetizations m_α and m_β as functions of bandwidth W. The checker compares ordering relations and specific values against hidden reference data extracted from the paper.
- schema:
  - `type`: table
  - `required_columns`: `W`, `m_alpha`, `m_beta`
  - `units`:
    - `W`: eV
    - `m_alpha`: dimensionless
    - `m_beta`: dimensionless

### step_02_phase_boundaries.csv
- path: `/app/outputs/step_02_phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-field phase boundaries in the (W,T) plane. The checker verifies the presence of the three expected boundary types, locates the critical end point and tricritical point near hidden reference positions, and checks the topological sequence AF1→AF2→PM.
- schema:
  - `type`: table
  - `required_columns`: `W`, `T`, `boundary_type`
  - `units`:
    - `W`: eV
    - `T`: eV

Notes: The hidden gold values are derived from the paper's Figs. 2 and 4. The magnetic-field-dependent phase diagram (Fig. 6) is omitted from the scored outputs because it requires a third scored artifact that exceeds the current pipeline's solve/checker block slots; it is left as a future extension.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_order_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "W",
          "m_alpha",
          "m_beta"
        ],
        "units": {
          "W": "eV",
          "m_alpha": "dimensionless",
          "m_beta": "dimensionless"
        }
      },
      "description": "Numerical values of zero-temperature staggered magnetizations m_α and m_β as functions of bandwidth W. The checker compares ordering relations and specific values against hidden reference data extracted from the paper."
    },
    {
      "file": "step_02_phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "W",
          "T",
          "boundary_type"
        ],
        "units": {
          "W": "eV",
          "T": "eV"
        }
      },
      "description": "Zero-field phase boundaries in the (W,T) plane. The checker verifies the presence of the three expected boundary types, locates the critical end point and tricritical point near hidden reference positions, and checks the topological sequence AF1→AF2→PM."
    }
  ],
  "notes": "The hidden gold values are derived from the paper's Figs. 2 and 4. The magnetic-field-dependent phase diagram (Fig. 6) is omitted from the scored outputs because it requires a third scored artifact that exceeds the current pipeline's solve/checker block slots; it is left as a future extension."
}
```

## How you are scored
A hidden verifier reads your output CSV files and compares them against a hidden reference that encodes the correct physical results (e.g., the discontinuity positions and the ordering of the magnetizations, the topology of the phase diagram and the locations of the multicritical points). The checker assesses each file independently using tolerances that account for normal numerical dispersion; the final score is a weighted sum of the per‑file scores. You do not need to match exact numbers from any publication—the verifier will judge whether your computed results capture the expected phase transitions and their characteristic features. The exact scoring formula and reference values are not disclosed.
