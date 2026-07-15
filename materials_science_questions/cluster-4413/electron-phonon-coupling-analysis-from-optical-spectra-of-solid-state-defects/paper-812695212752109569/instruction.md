# Exciton-Acoustic-Phonon Coupling Constant and Emission Line Shape Reproduction

## Problem background
In solid-state quantum dots (QDs), the elastic interaction between a confined exciton and acoustic phonons leads to a homogeneous emission line shape that is not a simple Lorentzian. At elevated temperatures, low-energy acoustic-phonon sidebands appear around the zero-phonon line, and the exciton dephasing mechanism cannot be captured by a single Markovian rate. Understanding this coupling is essential for predicting the optical coherence properties of single QDs. This task focuses on a theoretical description of this effect using a lattice‑relaxation (Huang‑Rhys) model that treats the coupled exciton‑phonon eigenstates.

## Approach
The model diagonalizes the exciton‑phonon Hamiltonian in the limit where off‑diagonal matrix elements are ignored, leading to a polaron shift and a coupling constant g(q) for each phonon mode. Using a quasi‑2D exciton wave function (Gaussian center‑of‑mass with localization length ξ and exponential in‑plane electron‑hole correlation) and bulk deformation‑potential coupling to longitudinal acoustic phonons, you will compute the direction‑integrated coupling constant g(q) as a function of phonon energy. To reproduce the emission spectrum, the continuum of acoustic phonons is discretised into a finite set of effective modes that conserve the total integrated coupling. Transition probabilities for 0‑, 1‑, and 2‑phonon processes are calculated for each mode, and the resulting spectral shape is obtained as the convolution of these discrete lines with a temperature‑dependent Lorentzian representing the zero‑phonon line (whose full width at half‑maximum increases linearly with temperature). The final line shape is the sum over all allowed phonon occupation changes.

## Reproduction target
Produce two scored artifacts:

1. **gq_vs_energy.csv** – coupling constant g(q) for a localization length ξ = 4 nm over the phonon energy range 0–4 meV (step 0.1 meV).
2. **line_shapes.csv** – normalized photoluminescence line shapes at temperatures 5, 30, and 50 K for the same ξ, over an energy‑offset range from –3 to +3 meV relative to the zero‑phonon line, using a discretisation of N = 12 effective phonon modes that conserves the total integrated coupling. The emission spectrum must include contributions from 0‑, 1‑, and 2‑phonon processes, convolved with the temperature‑dependent Lorentzian zero‑phonon linewidth.

The hidden verifier will compare your submitted artifacts against reference data to assess agreement. Your goal is to achieve this agreement by faithfully implementing the described model.

## Assets

- Takagahara 1985: Exciton wave function model and matrix element expression (Phys. Rev. B 31, 6552): 10.1103/PhysRevB.31.6552
- Van de Walle 1989: Deformation potentials (Phys. Rev. B 39, 1871): 10.1103/PhysRevB.39.1871
- Rudin et al 1990: Material constants (Phys. Rev. B 42, 11218): 10.1103/PhysRevB.42.11218

## Workflow steps

### Step 1: Compute direction-integrated coupling constant g(q)
- Role: scored
- Action: Implement the exciton-acoustic-phonon coupling model using a quasi-2D exciton wave function (Gaussian center-of-mass localization length ξ=4 nm, exponential in-plane electron-hole correlation with parameter λ0=42 Å) and the given material parameters (deformation potentials Dc=-5 eV, Dv=1 eV; mass density ρ=5.51 g/cm³; sound velocity u_s=4.0×10³ m/s). Compute the direction-integrated coupling constant g(q) as a function of phonon energy for energies from 0 to 4 meV and save the results.
- Output file: `/app/outputs/gq_vs_energy.csv`
- Format: csv
- Contract: Columns: phonon_energy_meV (float, units: meV), g (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 2: Simulate temperature-dependent emission line shapes
- Role: scored (load-bearing)
- Action: Using the g(q) from the previous step, construct N=12 effective phonon modes that conserve the total integrated coupling, compute transition probabilities for 0, 1, and 2 phonon processes, convolve with a Lorentzian of temperature-dependent zero-phonon linewidth (FWHM(µeV) = 180 + 1.5 × T(K)), and produce normalized emission spectra for temperatures T=5, 30, and 50 K.
- Output file: `/app/outputs/line_shapes.csv`
- Format: csv
- Contract: Columns: temperature_K (int), energy_offset_meV (float, relative to zero-phonon line), intensity (float, normalized to peak).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gq_vs_energy.csv`
- `/app/outputs/line_shapes.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gq_vs_energy.csv
- path: `/app/outputs/gq_vs_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Direction-integrated exciton-acoustic-phonon coupling constant as a function of phonon energy computed from the lattice-relaxation model for a fixed localization length.
- schema:
  - `type`: table
  - `required_columns`: `phonon_energy_meV`, `g`
  - `units`:
    - `phonon_energy_meV`: meV
    - `g`: dimensionless

### line_shapes.csv
- path: `/app/outputs/line_shapes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized emission line shapes simulated at three temperatures using the discretized phonon-mode lattice-relaxation model.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `energy_offset_meV`, `intensity`
  - `units`:
    - `temperature_K`: K
    - `energy_offset_meV`: meV
    - `intensity`: normalized

Notes: The checker will compare the submitted artifacts against digitized reference data from the paper's theoretical curves using appropriate error norms. The zero-phonon linewidth formula and all required material parameters are given in the workflow steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gq_vs_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phonon_energy_meV",
          "g"
        ],
        "units": {
          "phonon_energy_meV": "meV",
          "g": "dimensionless"
        }
      },
      "description": "Direction-integrated exciton-acoustic-phonon coupling constant as a function of phonon energy computed from the lattice-relaxation model for a fixed localization length."
    },
    {
      "file": "line_shapes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "energy_offset_meV",
          "intensity"
        ],
        "units": {
          "temperature_K": "K",
          "energy_offset_meV": "meV",
          "intensity": "normalized"
        }
      },
      "description": "Normalized emission line shapes simulated at three temperatures using the discretized phonon-mode lattice-relaxation model."
    }
  ],
  "notes": "The checker will compare the submitted artifacts against digitized reference data from the paper's theoretical curves using appropriate error norms. The zero-phonon linewidth formula and all required material parameters are given in the workflow steps."
}
```

## How you are scored
Your submission is evaluated by a hidden, deterministic verifier that scores each workflow stage separately. For the g(q) artifact, the verifier compares your computed coupling constant values to reference data over the full energy range; for the line shapes, it compares your normalized intensity curves at the three temperatures to reference curves using an appropriate error measure. The scores from each stage are combined with predetermined weights to yield a final reward between 0 and 1. Simply reporting the expected numbers without a correct implementation of the lattice‑relaxation model will result in a low score, because the verifier checks internal consistency and the shape of the produced curves. No partial credit is given for incomplete steps; the final reward reflects the overall quality of the reproduction.
