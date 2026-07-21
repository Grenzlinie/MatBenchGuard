# 2D Heisenberg Easy-Plane Spin Wave Normalization Reproduce

## Problem background
The 2D classical Heisenberg model with easy-plane anisotropy (interaction ratio η = J''/J⊥) exhibits spin wave renormalization in the low-temperature phase. This work investigates the temperature dependence of spin wave energies measured via Langevin spin dynamics. The key quantity is the normalized spin wave frequency ω_ck(T)/ω_ck(0), where ω_ck(0) is the zero-temperature reference computed from the Bloch equation. The goal is to compute these normalized frequencies for several anisotropy values η and wave vectors k across a range of temperatures and to examine their k-dependence.

## Approach
A 2D square-lattice ferromagnet with anisotropic nearest-neighbor interactions is simulated using Langevin dynamics. An oscillating external magnetic field along the z-direction, h_i(t) = (0,0, δh cos(k·r_i − ωt)), is applied to probe the spin wave response. The z-component magnetization time series M_z(t) is recorded, and the response function G_zz(k,ω) is computed. The spin wave frequency ω_ck(T) is identified as the frequency at which the imaginary part Im G_zz peaks. To obtain normalized frequencies, the Bloch equation provides the zero-temperature reference ω_ck(0). The simulation is performed at various temperatures T/J from 0.1 to 0.8 for representative wave vectors k and anisotropy parameters η (0, 0.6, 0.9).

## Reproduction target
Implement the Langevin simulation described and produce a CSV file `normalized_frequencies.csv` containing the normalized spin wave frequencies ω_ck(T)/ω_ck(0) for all specified combinations of η, wave vector k (as detailed in the workflow steps), and temperatures 0.1J ≤ T ≤ 0.8J in steps of 0.1J. The zero-temperature reference must be computed from the Bloch equation. Intermediate raw frequencies must be saved in `raw_frequencies.csv`. The reproduced data should allow assessment of the k-dependence of the normalized frequencies.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Langevin dynamics simulation
- Role: process
- Action: Implement Langevin spin dynamics for the 2D classical Heisenberg model with easy-plane anisotropy on a 16x16 square lattice and periodic boundary conditions, using the published parameters (J_ij^⊥=J, J_ij''=ηJ for η=0,0.6,0.9, C=0.1/J, u=80J, γ/Γ0=20, (Γ0Δt)^{-1}=400). For each η and each temperature T/J = 0.1 to 0.8, for each specified wave vector k, apply an oscillating z-field h_i(t)=(0,0,δh cos(k·r_i - ωt)) spanning a range of frequencies. Equilibrate the system and record the z-component magnetization time series M_z(t). Save a simulation log as evidence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Extract raw spin wave frequencies
- Role: scored
- Action: For each simulation run, compute the z-response function G_zz(k,ω) from the magnetization time series (e.g., via Fourier analysis or lock-in method). Determine the spin wave frequency ω_ck(T) as the frequency at which Im G_zz peaks. Write a CSV file raw_frequencies.csv with columns: eta, kx, ky, T_J, omega_ck.
- Output file: `/app/outputs/raw_frequencies.csv`
- Format: csv
- Contract: eta (float), kx (float, units 1/a), ky (float), T_J (float), omega_ck (float). Header row required.
- Scoring: scored by hidden verifier

### Step 3: Normalize spin wave frequencies
- Role: scored (load-bearing)
- Action: For each row in raw_frequencies.csv compute the zero-temperature reference ω_ck(0) from the Bloch equation: (ω_ck(0)/γ)^2 = (4J)^2 (1 - ĝ(k)) (1 - η ĝ(k)) with ĝ(k) = (cos(k_x a) + cos(k_y a))/2, setting a=1 and γ=1. Compute normalized frequency = omega_ck / ω_ck(0). Write normalized_frequencies.csv with columns: eta, kx, ky, T_J, normalized_freq.
- Output file: `/app/outputs/normalized_frequencies.csv`
- Format: csv
- Contract: eta (float), kx (float, units 1/a), ky (float), T_J (float), normalized_freq (float, dimensionless). Header row required.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raw_frequencies.csv`
- `/app/outputs/normalized_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raw_frequencies.csv
- path: `/app/outputs/raw_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw spin wave frequencies extracted from Langevin simulations for various η, k, and T. Used by the verifier to recompute normalized frequencies and check for consistency.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `kx`, `ky`, `T_J`, `omega_ck`
  - `units`:
    - `eta`: dimensionless
    - `kx`: 1/a
    - `ky`: 1/a
    - `T_J`: J/k_B
    - `omega_ck`: J

### normalized_frequencies.csv
- path: `/app/outputs/normalized_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized spin wave frequencies ω_ck(T)/ω_ck(0). The verifier checks consistency with raw frequencies via recomputation using the Bloch equation, then evaluates the structural claim of k-independence (within each η, for each T, the spread of normalized frequencies across k must be small) and monotonic decrease with T.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `kx`, `ky`, `T_J`, `normalized_freq`
  - `units`:
    - `eta`: dimensionless
    - `kx`: 1/a
    - `ky`: 1/a
    - `T_J`: J/k_B
    - `normalized_freq`: dimensionless

Notes: The verifier will recompute normalized frequencies from raw_frequencies.csv using the Bloch equation, compare to submitted normalized_frequencies.csv, perform k-independence and monotonic structural checks. The SRO similarity observation from the paper is a qualitative supplementary finding, not a co-equal quantitative headline, and is excluded from the scored contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raw_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "kx",
          "ky",
          "T_J",
          "omega_ck"
        ],
        "units": {
          "eta": "dimensionless",
          "kx": "1/a",
          "ky": "1/a",
          "T_J": "J/k_B",
          "omega_ck": "J"
        }
      },
      "description": "Raw spin wave frequencies extracted from Langevin simulations for various η, k, and T. Used by the verifier to recompute normalized frequencies and check for consistency."
    },
    {
      "file": "normalized_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "kx",
          "ky",
          "T_J",
          "normalized_freq"
        ],
        "units": {
          "eta": "dimensionless",
          "kx": "1/a",
          "ky": "1/a",
          "T_J": "J/k_B",
          "normalized_freq": "dimensionless"
        }
      },
      "description": "Normalized spin wave frequencies ω_ck(T)/ω_ck(0). The verifier checks consistency with raw frequencies via recomputation using the Bloch equation, then evaluates the structural claim of k-independence (within each η, for each T, the spread of normalized frequencies across k must be small) and monotonic decrease with T."
    }
  ],
  "notes": "The verifier will recompute normalized frequencies from raw_frequencies.csv using the Bloch equation, compare to submitted normalized_frequencies.csv, perform k-independence and monotonic structural checks. The SRO similarity observation from the paper is a qualitative supplementary finding, not a co-equal quantitative headline, and is excluded from the scored contract."
}
```

## How you are scored
A hidden verifier checks each workflow stage independently and combines the scores. It recomputes normalized frequencies from your raw_frequencies.csv using the Bloch equation and compares them against your submitted normalized_frequencies.csv. It further inspects structural properties: for each η and temperature, the spread of normalized frequencies across different k vectors is evaluated, and the temperature trend for each (η, k) is checked for monotonic behaviour. Consistency of raw_frequencies.csv is also verified. The final reward is a weighted sum of these checks; simply reporting a number without correct intermediate data will not earn full credit.
