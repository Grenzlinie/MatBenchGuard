# Exciton-phonon coupling and phonon-assisted photoluminescence in strained MoS2 monolayer from first principles

## Problem background
Excitons in monolayer MoS₂ exhibit weak phonon-assisted photoluminescence (PL) because certain exciton-phonon coupling channels are symmetry-forbidden. Biaxial tensile strain has been proposed as a means to activate these channels and thereby enhance indirect emission. The underlying coupling parameters, relaxation times, linewidths, and the resulting PL spectrum remain to be quantified for strained MoS₂ from first principles. This task requires computing these properties using a fully ab-initio computational pipeline.

## Approach
The computational approach combines density functional theory (DFT), GW quasiparticle corrections, density-functional perturbation theory (DFPT) for phonons, and the Bethe-Salpeter equation (BSE) for finite-momentum excitons, all performed with the open‑source codes Quantum Espresso and Yambo. Norm-conserving pseudopotentials are used. The workflow proceeds as follows:

1. Compute the electronic ground state, phonon dispersions, and electron-phonon matrix elements for monolayer MoS₂ under +1% biaxial tensile strain.
2. Obtain quasiparticle-corrected band energies via G₀W₀ and solve the BSE for the five lowest excitons across the Brillouin zone.
3. Perform a group-theoretic symmetry analysis to identify which phonon modes (A′ symmetry) are allowed to couple to the excitons.
4. Assemble exciton-phonon coupling strengths from the BSE coefficients and electron-phonon matrix elements.
5. Calculate temperature-dependent scattering rates and relaxation times for excitons 1–5 at Γ using Fermi’s golden rule.
6. Fit the computed linewidths of exciton 1 to the Toyozawa strong‑coupling model and those of exciton 5 to an empirical weak‑coupling form, extracting the best‑fit parameters.
7. Simulate the phonon-assisted PL spectrum at cryogenic temperature (10 K), including exciton‑phonon scattering with a finite damping and virtual exciton states.

The final outputs are the relaxation times, the fitted linewidth parameters, and the PL intensity as a function of energy.

## Reproduction target
Produce the following three scored artifacts from the ab-initio pipeline under +1% biaxial tensile strain:

- `step_06_relaxation_times.csv`: a table of exciton relaxation times (ps) as a function of temperature (K) for excitons 1–5 at Γ.
- `step_07_linewidth_params.json`: a JSON object containing the best-fit linewidth parameters for exciton 1 (Toyozawa model) and exciton 5 (weak‑coupling model), with all quantities in meV.
- `step_08_pl_spectrum.csv`: a table of energy (eV) vs. PL intensity (arbitrary units) at 10 K, covering the bright exciton line and its phonon replica region.

Each file must conform to the schema described in the output contract, and the values must be derived from the computational steps detailed in the workflow.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org
- Yambo: https://www.yambo-code.eu
- Norm-conserving pseudopotentials for Mo and S (ONCVPSP): http://www.quantum-simulation.org/potentials/sg15_oncv/
- Monolayer MoS2 hexagonal crystal structure

## Workflow steps

### Step 1: DFT and GW quasiparticle corrections
- Role: process
- Action: Perform ground-state DFT and G0W0 quasiparticle corrections for monolayer MoS2 under +1% biaxial tensile strain. Use norm-conserving pseudopotentials. Obtain quasiparticle-corrected electronic band structure, wavefunctions, and energies.
- Evidence: none

### Step 2: DFPT phonon calculation
- Role: process
- Action: Perform density-functional perturbation theory (DFPT) phonon calculation to obtain phonon frequencies, eigenvectors, and electron-phonon matrix elements g_{mn,ν}(k,q) on a fine q-grid.
- Evidence: none

### Step 3: Bethe-Salpeter equation for finite-momentum excitons
- Role: process
- Action: Solve the finite-momentum Bethe-Salpeter equation (BSE) for the five lowest excitons across the Brillouin zone using the quasiparticle energies and screened Coulomb interaction.
- Evidence: none

### Step 4: Group-theoretic symmetry analysis
- Role: process
- Action: Using exciton and phonon irreducible representations, identify the symmetry-allowed A' phonon modes that can couple to the lowest excitons. Filter out forbidden A'' modes.
- Evidence: `/app/outputs/allowed_modes.json`

### Step 5: Exciton-phonon coupling strengths
- Role: process
- Action: Compute the exciton-phonon coupling matrix elements |G_{nmν}(Q,q)|^2 using the BSE coefficients and electron-phonon matrix elements for the symmetry-allowed A' modes.
- Evidence: none

### Step 6: Exciton relaxation times
- Role: scored (load-bearing)
- Action: Compute the temperature-dependent exciton-phonon scattering rates and relaxation times for the five lowest excitons at Γ using the Fermi golden‑rule expression with the coupling strengths, exciton energies, and phonon occupations. Output a CSV table of relaxation times vs temperature.
- Output file: `/app/outputs/step_06_relaxation_times.csv`
- Format: csv
- Contract: columns: temperature (K), exciton_index (int 1..5), relaxation_time (ps). Rows cover temperatures from 0 to 300 K.
- Scoring: scored by hidden verifier

### Step 7: Linewidth fitting parameters
- Role: scored
- Action: Fit the computed temperature-dependent linewidths for exciton 1 to the Toyozawa strong‑coupling model (Δ = sqrt(Δ_A^2 + Δ_O^2)) and for exciton 5 to the empirical weak‑coupling form (γ = γ0 + aT + b[exp(E_O/kT)-1]⁻¹). Output the best‑fit parameters as JSON.
- Output file: `/app/outputs/step_07_linewidth_params.json`
- Format: json
- Contract: {"exciton1": {"SA": number (meV), "SO": number (meV), "EA": number (meV), "EO": number (meV)}, "exciton5": {"gamma0": number (meV), "a": number (meV/K), "b": number (meV)}}
- Scoring: scored by hidden verifier

### Step 8: Phonon-assisted PL spectrum
- Role: scored
- Action: Simulate the photoluminescence intensity as a function of energy for monolayer MoS2 at 10 K under +1% biaxial strain, including exciton-phonon scattering with a finite damping and virtual exciton states. Output a CSV of energy vs. intensity.
- Output file: `/app/outputs/step_08_pl_spectrum.csv`
- Format: csv
- Contract: columns: energy (eV), intensity (arbitrary units). Energy range covering the bright exciton line and the phonon replica region (shift from ~-0.1 eV to 0 eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_06_relaxation_times.csv`
- `/app/outputs/step_07_linewidth_params.json`
- `/app/outputs/step_08_pl_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_06_relaxation_times.csv
- path: `/app/outputs/step_06_relaxation_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent exciton relaxation times for excitons 1–5 at +1% strain, compared to paper-reported values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `exciton_index`, `relaxation_time`
  - `units`:
    - `temperature`: K
    - `relaxation_time`: ps

### step_07_linewidth_params.json
- path: `/app/outputs/step_07_linewidth_params.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted linewidth parameters for excitons 1 and 5 at +1% strain, compared to paper-reported values within tolerance.
- schema:
  - `type`: object
  - `required`: `exciton1`, `exciton5`
  - `items`:
    - `SA`: meV
    - `SO`: meV
    - `EA`: meV
    - `EO`: meV
    - `gamma0`: meV
    - `a`: meV/K
    - `b`: meV

### step_08_pl_spectrum.csv
- path: `/app/outputs/step_08_pl_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon-assisted PL spectrum at 10 K and +1% strain; structure and peak positions compared to paper.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `intensity`
  - `units`:
    - `energy`: eV
    - `intensity`: arbitrary units

Notes: Scored outputs provide the key numerical results: relaxation times, linewidth parameters, and PL spectrum. The verifier compares them to the paper-reported values using tolerances that account for computational differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_06_relaxation_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "exciton_index",
          "relaxation_time"
        ],
        "units": {
          "temperature": "K",
          "relaxation_time": "ps"
        }
      },
      "description": "Temperature-dependent exciton relaxation times for excitons 1–5 at +1% strain, compared to paper-reported values with tolerance."
    },
    {
      "file": "step_07_linewidth_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "exciton1",
          "exciton5"
        ],
        "items": {
          "SA": "meV",
          "SO": "meV",
          "EA": "meV",
          "EO": "meV",
          "gamma0": "meV",
          "a": "meV/K",
          "b": "meV"
        }
      },
      "description": "Fitted linewidth parameters for excitons 1 and 5 at +1% strain, compared to paper-reported values within tolerance."
    },
    {
      "file": "step_08_pl_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "intensity"
        ],
        "units": {
          "energy": "eV",
          "intensity": "arbitrary units"
        }
      },
      "description": "Phonon-assisted PL spectrum at 10 K and +1% strain; structure and peak positions compared to paper."
    }
  ],
  "notes": "Scored outputs provide the key numerical results: relaxation times, linewidth parameters, and PL spectrum. The verifier compares them to the paper-reported values using tolerances that account for computational differences."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output files. The verifier compares your submitted values to reference results obtained from a correct execution of the computational pipeline, using tolerances that account for typical toolchain-related variability. The final score is a weighted combination of the individual artifact scores. Note that simply reporting numbers without faithfully executing the required computations will be detected; the verifier checks structural consistency and may perform additional checks beyond the reported scalars where feasible.
