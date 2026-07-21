# Magnetization reversal times of finite-size atomic chains using improved kinetic Monte Carlo models

## Problem background
Finite-size atomic chains are promising candidates for spintronics and information storage because their magnetic properties can be controlled at the atomic scale. The magnetic reversal time (magnetization lifetime) is the key property that determines the stability and usability of an atomic chain as a bit. The magnetic interactions are usually described by the classical Heisenberg Hamiltonian with uniaxial anisotropy. Simple kinetic Monte Carlo (kMC) models of reversal assume that each magnetic moment is collinear with the easy axis and that its rotation does not affect other moments, which may overestimate the reversal time. Improved kMC models account for noncollinear relaxation of the spins and compute diffusion barriers on the fly using the geodesic nudged elastic band (GNEB) method, providing more accurate predictions of the reversal time. An analytical single domain-wall approximation can also give rapid estimates.

## Approach
We implement the classical Heisenberg model for finite chains with an XY‑model reduction (spins rotatable in a plane) to speed up relaxation and barrier calculations. For the Fe chain (antiferromagnetic, J≪K), we apply improved kMC model I: the metastable states are the same collinear ‘up’/‘down’ configurations as in the simple kMC, but the diffusion barriers for single‑spin‑flip events are obtained via GNEB. For the Co chain (ferromagnetic, J≳K), we apply improved kMC model II: four etalon domain‑wall states (CDW, ACDW, CADW, ACADW) are constructed and relaxed; these are used to identify all metastable states of a finite chain, and GNEB yields barriers for domain‑wall formation, disappearance, and motion. For both systems we also run the simple collinear kMC baseline and evaluate the analytical single domain‑wall formula. Reversal times are computed over a grid of temperatures and chain lengths specified in the reproduction target.

## Reproduction target
Implement the simple kMC, improved kMC I (Fe), and improved kMC II (Co) models, along with the analytical approximation. Compute magnetization reversal times τ (in seconds) and key diffusion barriers for two systems:
- Fe chain: J=1.3 meV, K=3.0 meV. Conditions: temperature 4,5,6,7 K at chain length N=10, and temperature 4 K at N=5,10,15,20,30,40.
- Co chain: J=7.5 meV, K=2.0 meV. Conditions: temperature 10 K at N=20,30,40,50,60, and N=40 at temperatures 4,10,20,30 K.
All kMC simulations must average over 1000 remagnetisation events.
Produce the following artifacts:
- `barriers.json`: an object with keys 'Fe' and 'Co', each containing numeric fields E1, E2, E3 (units meV) for the diffusion barriers.
- `fe_reversal_times.csv`: columns temperature_K, chain_length_N, tau_simple, tau_improvedI, tau_analytical.
- `co_reversal_times.csv`: columns temperature_K, chain_length_N, tau_simple, tau_improvedII, tau_analytical.

## Assets
No external datasets or pre‑trained models are required. The workflow uses only a Python environment with standard scientific libraries (numpy, scipy, and the built‑in csv and json modules). All physical parameters are given in the instruction.

## Workflow steps

### Step 1: Run simple kMC baseline simulations
- Role: process
- Action: Implement the simple kMC model (Li-Liu) for collinear spins using analytical rate formulas. For both Fe (J=1.3 meV, K=3.0 meV) and Co (J=7.5 meV, K=2.0 meV) chains, compute magnetization reversal times at all required temperature and length combinations by stochastic simulation, averaging over 1000 remagnetisations. Store tau_simple for later use.
- Evidence: `/app/outputs/simple_kMC_log.txt`

### Step 2: Fe chain relaxation and GNEB barrier calculation (Improved Model I)
- Role: process
- Action: For Fe chains (J=1.3 meV, K=3.0 meV): perform energy minimization under XY-model reduction (θ_i only, φ_i=0) to find relaxed metastable spin configurations corresponding to single-spin-flip states as in the simple kMC. Then compute diffusion barriers for edge spin flip and interior spin flips using the geodesic nudged elastic band (GNEB) method on the XY manifold. Save the barriers.
- Evidence: `/app/outputs/fe_barriers_raw.json`

### Step 3: Run improved kMC I simulations for Fe chains
- Role: process
- Action: Using the GNEB barriers from the previous step, perform improved kMC I simulations (Arrhenius rates) for Fe chains at all specified (T,N) points. Each simulation averages over 1000 remagnetisations to obtain the reversal time tau_improvedI. Save the traces.
- Evidence: `/app/outputs/fe_improvedI_traces.json`

### Step 4: Co chain etalon states and GNEB barrier calculation (Improved Model II)
- Role: process
- Action: For Co chains (J=7.5 meV, K=2.0 meV): generate the four etalon domain-wall states (CDW, ACDW, CADW, ACADW) by relaxing an infinite chain under XY-model reduction. Map these onto finite chains to construct all metastable states. For a reference chain of N=20, compute diffusion barriers for domain-wall formation, disappearance, and motion using GNEB. Cache these barriers.
- Evidence: `/app/outputs/co_barriers_raw.json`

### Step 5: Run improved kMC II simulations for Co chains
- Role: process
- Action: Using the GNEB barriers and etalon-state event rates, perform improved kMC II simulations for Co chains at all specified (T,N) points, averaging over 1000 remagnetisations. Compute tau_improvedII. Use effective chain length N_eff = N - 10 for Co due to domain-wall thickness.
- Evidence: `/app/outputs/co_improvedII_traces.json`

### Step 6: Compute analytical reversal times
- Role: process
- Action: Using the single domain-wall approximation with the computed diffusion barriers (E1^D, E2^D, E3^D) for both Fe and Co, appropriate degeneracy factors (n=2 for Fe, n=4 for Co) and N_eff=N-10 for Co, calculate the analytical reversal times tau_analytical at all required (T,N) conditions.
- Evidence: `/app/outputs/analytical_tau.json`

### Step 7: Write barriers.json
- Role: scored (load-bearing)
- Action: Collect the key diffusion barriers: for Fe, the values E1^D (edge formation), E2^D (disappearance), E3^D (motion); for Co, E1^D, E2^D, E3^D. Output as JSON file barriers.json.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: JSON object: keys 'Fe' and 'Co'. Each value is an object with numeric fields 'E1', 'E2', 'E3' in units of meV.
- Scoring: scored by hidden verifier

### Step 8: Write fe_reversal_times.csv
- Role: scored
- Action: Compile reversal times for Fe chains. Rows cover temperature_K=4,5,6,7 for N=10, and for T=4K, N=5,10,15,20,30,40. Columns: temperature_K (float), chain_length_N (int), tau_simple (float, seconds), tau_improvedI (float, seconds), tau_analytical (float, seconds). Write to CSV.
- Output file: `/app/outputs/fe_reversal_times.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), chain_length_N (int), tau_simple (float, seconds), tau_improvedI (float, seconds), tau_analytical (float, seconds).
- Scoring: scored by hidden verifier

### Step 9: Write co_reversal_times.csv
- Role: scored
- Action: Compile reversal times for Co chains. Rows cover T=10K for N=20,30,40,50,60, and T=4,10,20,30K for N=40. Columns: temperature_K (float), chain_length_N (int), tau_simple (float, seconds), tau_improvedII (float, seconds), tau_analytical (float, seconds). Write to CSV.
- Output file: `/app/outputs/co_reversal_times.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), chain_length_N (int), tau_simple (float, seconds), tau_improvedII (float, seconds), tau_analytical (float, seconds).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.json`
- `/app/outputs/fe_reversal_times.csv`
- `/app/outputs/co_reversal_times.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Diffusion barriers for Fe and Co chains from GNEB calculations.
- schema:
  - `type`: object
  - `required`:
    - `Fe`: object
    - `Co`: object
  - `items`:
    - `E1`: number (meV)
    - `E2`: number (meV)
    - `E3`: number (meV)

### fe_reversal_times.csv
- path: `/app/outputs/fe_reversal_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization reversal times for Fe chains.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `chain_length_N`, `tau_simple`, `tau_improvedI`, `tau_analytical`
  - `units`:
    - `temperature_K`: kelvin
    - `chain_length_N`: atoms
    - `tau_simple`: seconds
    - `tau_improvedI`: seconds
    - `tau_analytical`: seconds

### co_reversal_times.csv
- path: `/app/outputs/co_reversal_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization reversal times for Co chains.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `chain_length_N`, `tau_simple`, `tau_improvedII`, `tau_analytical`
  - `units`:
    - `temperature_K`: kelvin
    - `chain_length_N`: atoms
    - `tau_simple`: seconds
    - `tau_improvedII`: seconds
    - `tau_analytical`: seconds

Notes: The checker will compare barriers to reference values within tolerance and reversal times to expected values with appropriate tolerances, including trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe": "object",
          "Co": "object"
        },
        "items": {
          "E1": "number (meV)",
          "E2": "number (meV)",
          "E3": "number (meV)"
        }
      },
      "description": "Diffusion barriers for Fe and Co chains from GNEB calculations."
    },
    {
      "file": "fe_reversal_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "chain_length_N",
          "tau_simple",
          "tau_improvedI",
          "tau_analytical"
        ],
        "units": {
          "temperature_K": "kelvin",
          "chain_length_N": "atoms",
          "tau_simple": "seconds",
          "tau_improvedI": "seconds",
          "tau_analytical": "seconds"
        }
      },
      "description": "Magnetization reversal times for Fe chains."
    },
    {
      "file": "co_reversal_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "chain_length_N",
          "tau_simple",
          "tau_improvedII",
          "tau_analytical"
        ],
        "units": {
          "temperature_K": "kelvin",
          "chain_length_N": "atoms",
          "tau_simple": "seconds",
          "tau_improvedII": "seconds",
          "tau_analytical": "seconds"
        }
      },
      "description": "Magnetization reversal times for Co chains."
    }
  ],
  "notes": "The checker will compare barriers to reference values within tolerance and reversal times to expected values with appropriate tolerances, including trend checks."
}
```

## How you are scored
A hidden verifier will independently score each output artifact. For `barriers.json` it will compare your computed barrier values against reference values with appropriate tolerances. For the two CSV files it will compare your reversal times to reference expectations and check required qualitative relationships among the columns. The total reward is a weighted sum of the stage scores; reporting numbers without executing the required simulations will not suffice.
