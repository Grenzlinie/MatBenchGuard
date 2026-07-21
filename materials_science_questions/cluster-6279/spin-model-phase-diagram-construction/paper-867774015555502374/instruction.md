# Critical Exponent and Pattern Densities for a Spin-1 Triangular Ising Antiferromagnet

## Problem background
Spin-1 Ising antiferromagnets on a triangular lattice are profoundly influenced by geometrical frustration, which prevents conventional long‑range magnetic order. The addition of a single‑ion anisotropy D (parametrised as D/|J|) can, in principle, alter the ground‑state structure and the nature of the low‑temperature phases. In particular, a negative anisotropy (D<0) may lift the ground‑state degeneracy and stabilise a partially ordered antiferromagnetic phase within a certain range, while a positive D might drive the system to behave like a spin‑1/2 model. Whether such a partially ordered phase exists, and how the correlation decay exponent η and the local spin pattern densities evolve with temperature and D, are the central questions to be investigated by Monte Carlo simulations.

## Approach
Implement a Metropolis Monte Carlo simulation of the spin‑1 triangular Ising antiferromagnet described by the Hamiltonian H = -J ∑_{⟨i,j⟩} S_i S_j - D ∑_i S_i^2, where S_i ∈ {±1,0}, J<0 (antiferromagnetic), and D is the single‑ion anisotropy. Simulate triangular lattices with periodic boundary conditions at multiple linear sizes L (L=48 for thermodynamic averages, and L=24,48,72,96,120 for finite‑size scaling) using three anisotropy values D/|J| = -1, 0, +1. After thermalisation, record sublattice magnetisations, the staggered magnetisation, the sum of squared sublattice magnetisations Y, internal energy, and spin configurations across a wide temperature range.
From the finite‑size data, extract the correlation decay exponent η as a function of temperature for D/|J| = 0 and -1 by performing log‑log fits to the scaling relations that link the staggered magnetisation m_s and the quantity Y to the linear system size L. Also, count the relative frequencies of all 27 distinct triangular spin patterns (up to sign reversal) at the lowest simulated temperature to obtain pattern densities for each D/|J|. Finally, analyse the ground‑state energies of the Hamiltonian as a function of D/|J| to summarise the ground‑state regimes in a text file.

## Reproduction target
Compute the temperature‑dependent correlation exponent η for D/|J| = 0 and -1 using finite‑size scaling of the Monte Carlo data. Measure the densities of all local triangular spin patterns at the lowest simulated temperature for D/|J| = 1, 0, and -1. Provide a plain‑text summary listing the ground‑state regimes and their corresponding D/|J| intervals.

## Assets

- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Monte Carlo simulations
- Role: process
- Action: Implement Metropolis Monte Carlo for the spin-1 triangular Ising antiferromagnet Hamiltonian H = -J∑_{⟨i,j⟩} S_i S_j - D∑_i S_i^2, with S_i = ±1,0 and J<0. Simulate triangular lattices with periodic boundary conditions for sizes L=48 (for thermodynamic averages) and L=24,48,72,96,120 (for finite-size scaling), using D/|J| = -1, 0, and 1. Perform 2×10^5 Monte Carlo sweeps after thermalization over a temperature range from high to low with step Δt = 0.02. Record sublattice magnetizations, internal energy, Y quantity, staggered magnetization, specific heat, staggered susceptibility, and spin configurations.
- Evidence: `/app/outputs/mc_data.npz`

### Step 2: Finite-size scaling analysis for η
- Role: scored (load-bearing)
- Action: From the MC data for multiple L, compute the staggered magnetization m_s and the quantity Y as defined in the paper. Perform log-log fits to scaling relations to extract the correlation decay exponent η as a function of temperature. Output a CSV with columns: D_over_abs_J, temperature, eta, eta_error.
- Output file: `/app/outputs/eta_vs_temperature.csv`
- Format: csv
- Contract: Columns: D_over_abs_J (float), temperature (float), eta (float), eta_error (float).
- Scoring: scored by hidden verifier

### Step 3: Local pattern density analysis
- Role: scored
- Action: From spin configurations at the lowest simulated temperature, compute the relative frequencies of the 27 distinct triangular spin patterns. The 27 patterns are the triples (S_j,S_k,S_l) with S_i ∈ {+1,0,-1}. For convenience they are labelled by base IDs p1 through p14 and their sign-reversed variants -p2 through -p14 (p1 is its own negative). The mapping from pattern_id to spin triple is defined in the table below. Use these labels for the pattern_id column.

| pattern_id | (S_j, S_k, S_l) |
|------------|------------------|
| p1         | (0,0,0) |
| p2         | (1,1,1) |
| -p2        | (-1,-1,-1) |
| p3         | (1,1,-1) |
| -p3        | (-1,-1,1) |
| p7         | (1,-1,1) |
| -p7        | (-1,1,-1) |
| p9         | (-1,1,1) |
| -p9        | (1,-1,-1) |
| p4         | (1,1,0) |
| -p4        | (-1,-1,0) |
| p5         | (1,0,1) |
| -p5        | (-1,0,-1) |
| p10        | (0,1,1) |
| -p10       | (0,-1,-1) |
| p6         | (0,1,-1) |
| -p6        | (0,-1,1) |
| p8         | (1,0,-1) |
| -p8        | (-1,0,1) |
| p12        | (1,-1,0) |
| -p12       | (-1,1,0) |
| p11        | (1,0,0) |
| -p11       | (-1,0,0) |
| p13        | (0,1,0) |
| -p13       | (0,-1,0) |
| p14        | (0,0,1) |
| -p14       | (0,0,-1) |
- Output file: `/app/outputs/pattern_densities_low_temperature.csv`
- Format: csv
- Contract: Columns: D_over_abs_J (float), temperature (float), pattern_id (string, one of the IDs defined in the table above), density (float).
- Scoring: scored by hidden verifier

### Step 4: Ground-state regime summary
- Role: scored
- Action: Based on the MC results and analysis of the Hamiltonian ground-state energies, determine the ground-state phases as a function of D/|J|. Write a text file listing the regimes and their D/|J| ranges.
- Output file: `/app/outputs/ground_state_regimes.txt`
- Format: txt
- Contract: Plain text with human-readable lines describing the regimes.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eta_vs_temperature.csv`
- `/app/outputs/pattern_densities_low_temperature.csv`
- `/app/outputs/ground_state_regimes.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eta_vs_temperature.csv
- path: `/app/outputs/eta_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Correlation exponent η as a function of temperature for D/|J| = 0 and -1, extracted via finite-size scaling of MC data.
- schema:
  - `type`: table
  - `required_columns`: `D_over_abs_J`, `temperature`, `eta`, `eta_error`
  - `units`: object

### pattern_densities_low_temperature.csv
- path: `/app/outputs/pattern_densities_low_temperature.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Densities of local triangular spin patterns at low temperature for D/|J| = 1, 0, and -1.
- schema:
  - `type`: table
  - `required_columns`: `D_over_abs_J`, `temperature`, `pattern_id`, `density`
  - `units`: object

### ground_state_regimes.txt
- path: `/app/outputs/ground_state_regimes.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Text file listing ground-state phases and their D/|J| ranges.
- schema:
  - `type`: text

Notes: The Monte Carlo simulation step writes evidence mc_data.npz, which is not directly scored but required to produce the scored artifacts. All scored artifacts are derived from this simulation data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eta_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_over_abs_J",
          "temperature",
          "eta",
          "eta_error"
        ],
        "units": {}
      },
      "description": "Correlation exponent η as a function of temperature for D/|J| = 0 and -1, extracted via finite-size scaling of MC data."
    },
    {
      "file": "pattern_densities_low_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_over_abs_J",
          "temperature",
          "pattern_id",
          "density"
        ],
        "units": {}
      },
      "description": "Densities of local triangular spin patterns at low temperature for D/|J| = 1, 0, and -1."
    },
    {
      "file": "ground_state_regimes.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Text file listing ground-state phases and their D/|J| ranges."
    }
  ],
  "notes": "The Monte Carlo simulation step writes evidence mc_data.npz, which is not directly scored but required to produce the scored artifacts. All scored artifacts are derived from this simulation data."
}
```

## How you are scored
A hidden verifier independently inspects each output artifact (eta_vs_temperature.csv, pattern_densities_low_temperature.csv, ground_state_regimes.txt). The verifier checks the computed η values against reference criteria with tolerances, evaluates the pattern density distributions for consistency with the expected structural features, and audits the ground‑state regime listing for correctness. The final reward is a weighted combination of the scores from these checks; simply reporting numbers is not sufficient — the artefacts must be produced by the prescribed workflow.
