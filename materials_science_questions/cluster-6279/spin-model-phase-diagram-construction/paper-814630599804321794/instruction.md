# Mean-Field Phase Diagram of a Uniaxial Spin-1 Magnet with Anisotropic Exchange

## Problem background
Spin-1 magnetic systems can exhibit quadrupole ordering when tensor interactions—single-ion anisotropy (SIA) and biquadratic exchange interaction (BEI)—are comparable to the Heisenberg exchange. One such ordered state is the axial quadrupole phase (QP1Z), where spins align along the uniaxial symmetry axis but with zero net magnetization at zero field. Understanding how this phase evolves under an external longitudinal magnetic field is important for describing the magnetic phase diagram. This task concerns a uniaxial spin‑1 magnet with the most general form of SIA and anisotropic BEI. The goal is to determine, within mean-field theory, the temperature and field dependence of the order parameters, the boundary between the QP1Z phase and the ferromagnetic phase, and the influence of the BEI anisotropy constants on the critical temperature of the transition to an angular phase.

## Approach
The system is described by a Heisenberg Hamiltonian that includes exchange, single‑ion anisotropy, and anisotropic biquadratic exchange, plus a longitudinal magnetic field. In the mean-field approximation, the Hamiltonian reduces to a single‑particle form in a new basis obtained by a unitary transformation. The self-consistent values of the diagonal order parameters σ = ⟨S̃^z⟩ and λ = ⟨Q̃^0⟩ are found by solving the Gibbs‑measure equations for a set of fixed dimensionless parameters. From σ and λ, the physical order‑parameter components ⟨S^z⟩, ⟨Q⁰⟩, and ⟨Q²⟩ are evaluated. The QP1Z–ferromagnetic phase boundary is located by the vanishing of ⟨Q²⟩. Additionally, the stability of the spin excitation spectrum is used to determine the critical temperature for the QP1Z→angular phase transition: the long‑wavelength spectrum must soften, i.e., ω₁(0)=0. The critical temperature is computed as a function of the BEI anisotropy constants η and ζ at selected fixed fields. All quantities are expressed in dimensionless units scaled by the exchange constant J₀.

## Reproduction target
Using the fixed Hamiltonian parameters J0 = 1.0, ξ = 1.0, D = 1.2, K0 = 1.25, η = 2.0, ζ = 3.0, carry out the following computational tasks:

1. Solve the mean-field self‑consistency equations numerically to obtain σ and λ on a dense grid of dimensionless temperature θ̃ = T/J₀ and field h̃ = h/J₀.
2. From σ and λ, compute the order parameters ⟨S^z⟩, ⟨Q⁰⟩, ⟨Q²⟩ and produce a CSV file containing their values for the conditions:
   - ⟨Q⁰⟩ vs temperature at h̃ = 4.5
   - ⟨Q²⟩ vs temperature at h̃ = 4.7, 5.0, 5.3
3. Determine the QP1Z–ferromagnetic phase boundary by finding, for a range of h̃, the critical temperature θ̃_c where ⟨Q²⟩ vanishes (within a small numerical tolerance). Output these (h̃, θ̃_c) pairs.
4. For the fixed fields h̃ = 2.5, 3.2, 3.8, compute the critical temperature θ̃* of the QP1Z→angular phase transition from the spectrum softening condition ω₁(0)=0. Vary η while keeping ζ=3.0, and vary ζ while keeping η=2.0. Save the results in a CSV with columns for η, ζ, h̃, and θ̃*.

All output files must follow the schema and format described in the workflow steps and output contract.

## Assets

- Python 3.x
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Solve self-consistent mean-field equations
- Role: process
- Action: Implement a mean-field self-consistency solver for the uniaxial spin-1 Hamiltonian with given exchange (J0, ξ), single-ion anisotropy (D), and biquadratic exchange (K0, η, ζ) constants. Solve for the self-consistent values of σ = ⟨S̃^z⟩ and λ = ⟨Q̃^0⟩ across a dense grid of dimensionless temperature θ̃ = T/J0 and magnetic field h̃ = h/J0. Save the complete solution arrays for later use.
- Evidence: `/app/outputs/self_consistent_solution.npz`

### Step 2: Compute order parameters for Figures 1 and 2
- Role: scored (load-bearing)
- Action: From the self-consistent σ and λ, evaluate the order parameter components ⟨S^z⟩, ⟨Q⁰⟩, and ⟨Q²⟩ using the relations derived from the mean-field Hamiltonian diagonalization. Generate temperature-dependent data for ⟨Q⁰⟩ at fixed dimensionless field h̃=4.5, and for ⟨Q²⟩ at h̃=4.7, 5.0, 5.3. Write a CSV file with columns for field, temperature, and the three order parameters.
- Output file: `/app/outputs/order_parameters.csv`
- Format: csv
- Contract: CSV with columns: field (float, dimensionless h/J0), temperature (float, dimensionless θ/J0), S_z (float), Q0 (float), Q2 (float). Rows must cover the curves shown in Fig.1 (h=4.5) and Fig.2 (h=4.7, 5.0, 5.3).
- Scoring: scored by hidden verifier

### Step 3: Determine QP1Z–ferromagnetic phase boundary
- Role: scored
- Action: For a range of magnetic fields h̃, find the critical temperature θ̃_c at which ⟨Q²⟩ = 0 (within a small numerical tolerance). This defines the phase boundary between the QP1Z and ferromagnetic (FMP) phases. Output a CSV with (h̃, θ̃_c) pairs corresponding to Figure 3.
- Output file: `/app/outputs/phase_boundary.csv`
- Format: csv
- Contract: CSV with columns: field (float, dimensionless h/J0), critical_temperature (float, dimensionless θ_c/J0). Should cover the curve shown in Fig.3.
- Scoring: scored by hidden verifier

### Step 4: Critical temperature dependence on BEI anisotropy constants
- Role: scored
- Action: Using the spin excitation spectrum stability condition ω₁(0)=0, compute the critical temperature θ̃* for the QP1Z→angular phase transition. For fixed fields h̃=2.5, 3.2, 3.8, evaluate θ̃* while varying η (with ζ=3.0) and varying ζ (with η=2.0) to reproduce Figure 4. Output a CSV with the anisotropy constants, field, and critical temperature.
- Output file: `/app/outputs/critical_temp_anisotropy.csv`
- Format: csv
- Contract: CSV with columns: eta (float, dimensionless), zeta (float, dimensionless), field (float, dimensionless h/J0), critical_temperature (float, dimensionless θ*/J0). Must include data for η=2.0 with varying ζ and ζ=3.0 with varying η, at fields 2.5, 3.2, 3.8.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_parameters.csv`
- `/app/outputs/phase_boundary.csv`
- `/app/outputs/critical_temp_anisotropy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_parameters.csv
- path: `/app/outputs/order_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature dependence of order parameters ⟨S^z⟩, ⟨Q⁰⟩, ⟨Q²⟩ at specified fields. Corresponds to Figures 1 and 2.
- schema:
  - `type`: table
  - `required_columns`: `field`, `temperature`, `S_z`, `Q0`, `Q2`
  - `units`:
    - `field`: dimensionless h/J0
    - `temperature`: dimensionless θ/J0
    - `S_z`: dimensionless
    - `Q0`: dimensionless
    - `Q2`: dimensionless

### phase_boundary.csv
- path: `/app/outputs/phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phase boundary between QP1Z and ferromagnetic phases (Figure 3).
- schema:
  - `type`: table
  - `required_columns`: `field`, `critical_temperature`
  - `units`:
    - `field`: dimensionless h/J0
    - `critical_temperature`: dimensionless θ_c/J0

### critical_temp_anisotropy.csv
- path: `/app/outputs/critical_temp_anisotropy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Critical temperature of QP1Z-angular phase transition vs. anisotropy constants (Figure 4).
- schema:
  - `type`: table
  - `required_columns`: `eta`, `zeta`, `field`, `critical_temperature`
  - `units`:
    - `eta`: dimensionless
    - `zeta`: dimensionless
    - `field`: dimensionless h/J0
    - `critical_temperature`: dimensionless θ*/J0

Notes: All outputs are in dimensionless units. The solver must use the fixed Hamiltonian parameters: J0=1.0, ξ=1.0, D=1.2, K0=1.25, η=2.0, ζ=3.0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field",
          "temperature",
          "S_z",
          "Q0",
          "Q2"
        ],
        "units": {
          "field": "dimensionless h/J0",
          "temperature": "dimensionless θ/J0",
          "S_z": "dimensionless",
          "Q0": "dimensionless",
          "Q2": "dimensionless"
        }
      },
      "description": "Temperature dependence of order parameters ⟨S^z⟩, ⟨Q⁰⟩, ⟨Q²⟩ at specified fields. Corresponds to Figures 1 and 2."
    },
    {
      "file": "phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field",
          "critical_temperature"
        ],
        "units": {
          "field": "dimensionless h/J0",
          "critical_temperature": "dimensionless θ_c/J0"
        }
      },
      "description": "Phase boundary between QP1Z and ferromagnetic phases (Figure 3)."
    },
    {
      "file": "critical_temp_anisotropy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "zeta",
          "field",
          "critical_temperature"
        ],
        "units": {
          "eta": "dimensionless",
          "zeta": "dimensionless",
          "field": "dimensionless h/J0",
          "critical_temperature": "dimensionless θ*/J0"
        }
      },
      "description": "Critical temperature of QP1Z-angular phase transition vs. anisotropy constants (Figure 4)."
    }
  ],
  "notes": "All outputs are in dimensionless units. The solver must use the fixed Hamiltonian parameters: J0=1.0, ξ=1.0, D=1.2, K0=1.25, η=2.0, ζ=3.0."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently checks each of the scored output files. The verifier implements the same mean‑field equations and spectrum condition, recomputes the expected values for the (field, temperature) rows you provide, and compares your submitted numbers within a small dimensionless tolerance. For the order‑parameter file, it recomputes σ and λ and verifies ⟨S^z⟩, ⟨Q⁰⟩, ⟨Q²⟩; for the phase‑boundary file, it checks that at each (h̃, θ̃_c) the recomputed ⟨Q²⟩ is zero within tolerance; for the critical‑temperature file, it recomputes ω₁(0) and confirms that it vanishes at the reported θ̃* within tolerance. Each scored stage contributes a weighted portion to the final reward. You must produce the exact CSV files described in the steps; simply reporting final numbers without the required data will not suffice.
