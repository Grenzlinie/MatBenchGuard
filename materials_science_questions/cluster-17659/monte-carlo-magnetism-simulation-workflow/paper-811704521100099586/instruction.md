# Monte Carlo simulation of dynamic magnetization hysteresis in magnetic microspheres

## Problem background
Magnetic microspheres (MMS) – non-magnetic cores coated with a layer of magnetic nanoparticles – are promising for hyperthermia applications, where an AC magnetic field drives magnetization dynamics that generate heat. Characterising the dynamic hysteresis behaviour of a single MMS is challenging experimentally, so computer simulation provides a high-resolution alternative. The target is to compute the magnetization response of such a microsphere under an AC field for both non-interacting and dipole-dipole interacting particle ensembles, using a Monte Carlo–Metropolis protocol.

## Approach
Model the microsphere as a dilute monolayer of identical uniaxially anisotropic single-domain nanoparticles placed at random non-overlapping positions on a spherical surface, with randomly oriented easy axes. The magnetic state is defined by the orientations of the particle moments. Three dimensionless parameters govern the physics: the field strength ξ=μH/kT, the anisotropy barrier σ=E_A/kT, and the dipolar coupling λ=μ²/(kT a³), where a is the mean interparticle distance. The AC driving field is approximated by a sequence of constant-field stages; at each stage, a fixed number of Monte Carlo sweeps is performed. Each sweep proposes a random rotation (uniform in [−Δ, Δ]) for every particle’s moment and accepts/rejects it via the Metropolis criterion, using the total energy that includes Zeeman, uniaxial anisotropy, and optionally dipole-dipole terms. After equilibration, the ensemble-averaged magnetization projection ⟨μ_z⟩/μ is recorded at each field stage to construct the hysteresis loop. Simulations are carried out for two scenarios: (i) non-interacting particles, where dipole-dipole energies are omitted, and (ii) interacting particles, where the full dipolar coupling is included.

## Reproduction target
You will generate the required nanoparticle configurations, then run the Monte Carlo protocol to produce two hysteresis datasets:

1. **Non-interacting case**: using a configuration of 1000 particles, compute the dynamic hysteresis loops for anisotropy parameters σ = 2, 5, and 15. The AC drive is modelled with m = 80 field stages, trial-amplitude Δ = 0.25, and the number of MC steps per stage n as given: 100 (σ=2), 45 (σ=5), 16 (σ=15). The peak field is set to ξ₀ = 2σ.

2. **Interacting case**: using separate configurations with particle counts N = 100, 500, and 1000, compute the hysteresis loops with dipole-dipole interactions included. Use the maghemite material parameters (M_s = 400 G, K = 2×10⁵ erg/cm³, T = 28 K, particle diameter 8 nm) and core diameter 200 nm to derive the dimensionless parameters σ and λ. Run the same protocol (m = 80, Δ = 0.25) with a fixed number of MC steps per stage (choose e.g. n = 100).

For both cases, output CSV files containing dimensionless field ξ and magnetisation ⟨μ_z⟩/μ at each field stage.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate microsphere nanoparticle configurations
- Role: process
- Action: For a core diameter of 200 nm and nanoparticle diameter of 8 nm, generate random non-overlapping positions on the sphere surface and assign random easy-axis orientations for particle counts N=100, 500, and 1000. Save the configurations to files for use in simulations.
- Evidence: `/app/outputs/config_generation.log`

### Step 2: Simulate non-interacting dynamic hysteresis
- Role: scored (load-bearing)
- Action: Using the N=1000 configuration, run stepwise AC-driven Monte Carlo simulation for non-interacting particles at anisotropy parameters sigma = 2, 5, 15 with field discretization m=80, trial amplitude Delta=0.25, peak field amplitude xi0 = 2*sigma, and MC steps per stage n as specified in the protocol (100 for sigma=2, 45 for sigma=5, 16 for sigma=15). At each field stage compute the ensemble magnetization projection <mu_z>/mu and output the hysteresis loop data.
- Output file: `/app/outputs/hysteresis_noninteracting.csv`
- Format: csv
- Contract: CSV with columns: sigma (int), field (float), magnetization (float). One row per field stage for each sigma.
- Scoring: scored by hidden verifier

### Step 3: Simulate interacting dynamic hysteresis
- Role: scored (load-bearing)
- Action: For each particle count N = 100, 500, 1000, use the corresponding configuration. Compute dimensionless parameters sigma and lambda from the given maghemite material properties (Ms=400 G, K=2e5 erg/cm^3, T=28 K, particle diameter 8 nm) and core geometry (200 nm sphere diameter). Run the same MC protocol (m=80, trial amplitude Delta=0.25) with dipole-dipole interactions included, using a fixed number of MC steps per stage (e.g., n=100). Output the hysteresis loop data.
- Output file: `/app/outputs/hysteresis_interacting.csv`
- Format: csv
- Contract: CSV with columns: num_particles (int), field (float), magnetization (float). One row per field stage for each N.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hysteresis_noninteracting.csv`
- `/app/outputs/hysteresis_interacting.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hysteresis_noninteracting.csv
- path: `/app/outputs/hysteresis_noninteracting.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw hysteresis data for the non-interacting case; the checker performs a structural audit on loop metrics (monotonic increase of area and coercivity with sigma, saturation).
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `field`, `magnetization`

### hysteresis_interacting.csv
- path: `/app/outputs/hysteresis_interacting.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw hysteresis data for the interacting case; the checker verifies structural trends (loop width increases with particle count N) and that each interacting loop is wider than the corresponding non-interacting case.
- schema:
  - `type`: table
  - `required_columns`: `num_particles`, `field`, `magnetization`

Notes: The MC-step-to-real-time calibration is not required; the agent uses the given n values directly. The simulations are lightweight and do not require GPU acceleration.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hysteresis_noninteracting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "field",
          "magnetization"
        ]
      },
      "description": "Raw hysteresis data for the non-interacting case; the checker performs a structural audit on loop metrics (monotonic increase of area and coercivity with sigma, saturation)."
    },
    {
      "file": "hysteresis_interacting.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "num_particles",
          "field",
          "magnetization"
        ]
      },
      "description": "Raw hysteresis data for the interacting case; the checker verifies structural trends (loop width increases with particle count N) and that each interacting loop is wider than the corresponding non-interacting case."
    }
  ],
  "notes": "The MC-step-to-real-time calibration is not required; the agent uses the given n values directly. The simulations are lightweight and do not require GPU acceleration."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage and combine the scores. For the non-interacting case, the verifier will read your submitted CSV, recompute quantities such as the loop area (energy loss) and the coercive field, and compare them against reference values derived from the physical model; credit is earned for agreement within prescribed tolerances. For the interacting case, the verifier will perform a structural audit: it will check that the hysteresis loop width (area and/or coercivity) increases monotonically with particle count and that each interacting loop is wider than a comparable non-interacting benchmark. Only the raw CSV data you produce is inspected; simply reporting a final number without the corresponding hysteresis loop trace will not earn credit.
