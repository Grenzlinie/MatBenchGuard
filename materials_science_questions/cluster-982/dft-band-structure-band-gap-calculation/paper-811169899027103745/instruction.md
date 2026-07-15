# Electronic Specific Heat Effect on SHI Tracks in Si

## Problem background
Swift heavy ion (SHI) irradiation of semiconductors and insulators creates nanoscale damage tracks. The two-temperature model (TTM) describes energy transfer from the electronic to the ionic subsystem, but the traditional free-electron gas (FEG) specific heat ignores the presence of a bandgap. One way to account for bandgap effects is to replace the constant FEG specific heat with a temperature-dependent electronic specific heat, Ce(Te), calculated ab initio. This reproduction task computes Ce(Te) for silicon using density functional theory (DFT) with a hybrid functional that yields an accurate bandgap, and then uses that Ce(Te) in large-scale two-temperature molecular dynamics (2T-MD) simulations of SHI tracks. The goal is to quantify the resulting ion track damage and compare it with results obtained using the FEG model.

## Approach
The work proceeds in two serial stages.  

**Stage 1 – DFT specific heat.** Finite-temperature DFT with a hybrid exchange-correlation functional (HSE) is used to compute the internal energy U(Te) of silicon at electronic temperatures Te from 0 K to 25000 K. The electronic specific heat Ce = ∂U/∂Te is evaluated as a function of Te and stored in a CSV file.  

**Stage 2 – 2T-MD simulation and damage analysis.** A large silicon supercell (~200 000 atoms, diamond cubic) is simulated with a Tersoff interatomic potential and coupled to an electronic continuum that solves the heat diffusion equation (two-temperature model). The electronic subsystem is parameterised by a temperature-dependent diffusivity model, electron–phonon coupling derived from a fixed relaxation time, and a Gaussian spatial / exponential temporal source term normalised to a fixed electronic stopping power. Two separate 20 ps simulations are performed: one using the DFT-derived Ce(Te) from Stage 1, and one using a constant free-electron‑gas Ce. After 20 ps, the final damage is analysed: the track radius is obtained from the radial atomic density profile via Voronoi cell analysis, and Wigner–Seitz defects (vacancies + interstitials) are counted. The two conditions are compared through their track radii and defect counts.

## Reproduction target
Produce the temperature-dependent electronic specific heat Ce(Te) for silicon using DFT with the HSE functional (0 K to 25000 K in 250 K steps) and output a CSV file. Then run 2T-MD simulations at an electronic stopping power of 25 keV nm⁻¹ with both the HSE-derived specific heat and the free-electron gas specific heat, and report the resulting track radii and total Wigner–Seitz defect counts in a JSON file. The exact output paths and formats are given in the Workflow steps and Output files sections below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LAMMPS: https://lammps.org/
- Silicon PAW pseudopotential for HSE: https://www.quantum-espresso.org/pseudopotentials/
- Silicon Tersoff potential parameters (Kumagai 2007): 10.1016/j.commatsci.2007.01.016
- Electronic diffusivity model (Dufour et al.) and electron–phonon coupling: 10.1088/0022-3727/45/6/065302

## Workflow steps

### Step 1: DFT calculation of electronic specific heat Ce(Te) with HSE
- Role: scored (load-bearing)
- Action: Compute the electronic specific heat Ce(Te) for silicon using DFT with the HSE hybrid functional. Use a diamond‑cubic primitive cell (2 atoms) with Fermi–Dirac smearing. Perform calculations at electronic temperatures from 0 K to 25000 K in increments of 250 K and obtain Ce = ∂U/∂Te. Output a CSV file with two columns: temperature (K) and specific heat (eV/K per atom).
- Output file: `/app/outputs/step_01_Ce_HSE.csv`
- Format: csv
- Contract: CSV with columns T (K) (integer steps of 250 K) and Ce (eV/K/atom) (float).
- Scoring: scored by hidden verifier

### Step 2: 2T‑MD simulation and damage analysis
- Role: scored (load-bearing)
- Action: Using an MD package that supports the two‑temperature model (e.g., LAMMPS), set up a silicon supercell (~200 000 atoms, diamond cubic) with periodic boundaries and the Tersoff potential of Kumagai. For the electronic subsystem use a temperature‑dependent electronic diffusivity (Dufour model), electron–phonon coupling derived from a relaxation time of 0.26 ps, and a SHI source term (spatial Gaussian, temporal exponential) normalised to an electronic stopping power of 25 keV nm⁻¹. Run two separate 20 ps simulations (1 fs timestep): one using the Ce(Te) from step01, and one using a constant free‑electron gas specific heat (Ce = (3/2) kB per electron, one electron per atom). After 20 ps, analyse the damage: compute the track radius from the radial atomic density profile via Voronoi cell analysis, and count the total number of Wigner–Seitz defects (vacancies + interstitials). Write a JSON file containing the four resulting quantities.
- Output file: `/app/outputs/step_02_track_results.json`
- Format: json
- Contract: JSON object with keys: HSE_track_radius_angstrom (float), FEG_track_radius_angstrom (float), HSE_defect_count (int), FEG_defect_count (int).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_Ce_HSE.csv`
- `/app/outputs/step_02_track_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_Ce_HSE.csv
- path: `/app/outputs/step_01_Ce_HSE.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic specific heat Ce(Te) for silicon using the HSE functional. The checker compares Ce values at several temperatures against hidden paper‑derived reference values.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Ce`
  - `units`:
    - `T`: K
    - `Ce`: eV/K/atom

### step_02_track_results.json
- path: `/app/outputs/step_02_track_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Track radii and defect counts from 2T‑MD simulations with HSE and FEG specific heats at Se = 25 keV nm⁻¹. Radii compared to paper‑reported values; structural requirement HSE radius < FEG radius enforced.
- schema:
  - `type`: object
  - `required`:
    - `HSE_track_radius_angstrom`:
      - `type`: number
    - `FEG_track_radius_angstrom`:
      - `type`: number
    - `HSE_defect_count`:
      - `type`: integer
    - `FEG_defect_count`:
      - `type`: integer

Notes: The task reproduces the DFT-derived electronic specific heat and its effect on 2T‑MD damage. Both artifacts are compared against hidden paper‑reported reference values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_Ce_HSE.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Ce"
        ],
        "units": {
          "T": "K",
          "Ce": "eV/K/atom"
        }
      },
      "description": "Electronic specific heat Ce(Te) for silicon using the HSE functional. The checker compares Ce values at several temperatures against hidden paper‑derived reference values."
    },
    {
      "file": "step_02_track_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "HSE_track_radius_angstrom": {
            "type": "number"
          },
          "FEG_track_radius_angstrom": {
            "type": "number"
          },
          "HSE_defect_count": {
            "type": "integer"
          },
          "FEG_defect_count": {
            "type": "integer"
          }
        }
      },
      "description": "Track radii and defect counts from 2T‑MD simulations with HSE and FEG specific heats at Se = 25 keV nm⁻¹. Radii compared to paper‑reported values; structural requirement HSE radius < FEG radius enforced."
    }
  ],
  "notes": "The task reproduces the DFT-derived electronic specific heat and its effect on 2T‑MD damage. Both artifacts are compared against hidden paper‑reported reference values with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. For the specific heat CSV, selected Ce values are compared against reference values derived from the original study. For the track results JSON, the verifier compares the reported track radii to reference values and enforces a structural relation between the two specific‑heat conditions. Defect counts are also checked for consistency. The final reward is a weighted combination of these per‑artifact scores. Simply reporting a number is not sufficient; the workflow steps must be executed and the required output files produced as specified.
