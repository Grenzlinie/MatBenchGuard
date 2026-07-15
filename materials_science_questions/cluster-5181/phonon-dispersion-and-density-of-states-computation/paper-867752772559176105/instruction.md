# Lattice thermal conductivity of doped graphene with isotopic defects

## Problem background
Graphene exhibits exceptionally high lattice thermal conductivity at room temperature, making it promising for thermal management applications. In real samples, phonon transport is limited by intrinsic Umklapp (phonon-phonon) scattering, edge-boundary scattering from finite flake dimensions, and scattering by isotopic substitutional defects. The degree to which heavy versus light substitutional atoms reduce the thermal conductivity of a finite graphene flake is not trivially predicted by simple mass-perturbation arguments. This task investigates the lattice thermal conductivity of an ideal square graphene flake and that of flakes doped with heavy and light isotopic defects, all under the same temperature and size conditions, to quantify the effect of mass disparity on heat transport.

## Approach
The lattice thermal conductivity is computed from first principles using the phonon Boltzmann transport equation in the relaxation-time approximation. The phonon dispersion of graphene is obtained from a harmonic nearest-neighbor force-constant model with three distinct force constants. Group velocities are derived from the dispersion. Three scattering mechanisms are treated independently: (i) Umklapp scattering modeled by a Klemens-like expression involving mode-dependent Grüneisen parameters and Debye frequencies; (ii) edge-boundary scattering using a ballistic mean-free-path determined by the flake area and a form factor; (iii) isotopic-defect scattering handled via the T-matrix (Green's function) formalism, which gives the relaxation time as a function of the mass difference Δm/m and defect concentration n. The total relaxation time for each phonon mode is obtained via Matthiessen's rule. The thermal conductivity is then evaluated as a sum over all phonon branches and wavevectors in the first Brillouin zone. The calculation is performed for an ideal (defect-free) flake and for two doped scenarios: one with heavy (Al-like, Δm/m=1.25) and one with light (N-like, Δm/m=0.1667) defects, both at concentration n=0.01. All simulations are carried out at a fixed temperature T=300 K for a square flake of side L=10 μm.

## Reproduction target
Compute the lattice thermal conductivity κ (in W/(m·K)) of a square graphene flake of side length 10 μm at temperature 300 K for the following three conditions:
- Ideal graphene (no isotopic defects, Δm/m = 0, n = 0)
- Doped with aluminium-like isotopic defects (Δm/m = 1.25, concentration n = 0.01)
- Doped with nitrogen-like isotopic defects (Δm/m = 0.1667, n = 0.01)
Report the three κ values in the output file thermal_conductivity_results.csv as described in the output contract.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Phonon dispersion and group velocities
- Role: process
- Action: Implement the harmonic nearest-neighbor force-constant model for graphene using force constants J1=135, J2=245, J3=83.9 J/m². Build the 6×6 dynamical matrix at each k-point on a dense Monkhorst-Pack mesh covering the Brillouin zone. Diagonalize to obtain phonon frequencies ω_s(k) (six branches) and compute group velocities v_s(k) = ∇_k ω_s(k) via finite differences. Save the phonon spectra for downstream use.
- Evidence: `/app/outputs/phonon_dispersion.npz`

### Step 2: Umklapp relaxation times
- Role: process
- Action: Compute the Umklapp relaxation time for each phonon mode using the Klemens-like expression: τ^U_{k,s} = [m v̄_s² / γ_s²] · [1/(k_B T)] · [ω_{D,s} / ω_s²(k)], where m is the carbon atom mass, v̄_s are sound velocities (v_LA=18.4 km/s, v_TA=16.5 km/s, v_ZA=9.2 km/s), γ_s are Grüneisen parameters (γ_LA=1.8, γ_TA=0.75, γ_ZA=-1.4), ω_{D,s} are Debye frequencies (ω_{D,1}=2.66×10¹⁴, ω_{D,2}=2.38×10¹⁴, ω_{D,3}=1.32×10¹⁴ rad/s), and T=300 K. Store τ^U for each (k,s).
- Evidence: `/app/outputs/umklapp_tau.npz`

### Step 3: Edge scattering relaxation times
- Role: process
- Action: Compute the edge-boundary scattering relaxation time for each mode as τ^{edge}_{k,s} = f √S / v_{k,s}, where S = (10 μm)² is the flake area. Determine the form factor f for a square flake through analytical ray-tracing or Monte Carlo integration (a resulting value near 0.47–0.48). Store τ^{edge} for every (k,s).
- Evidence: `/app/outputs/edge_tau.npz`

### Step 4: Defect scattering relaxation times (T-matrix)
- Role: process
- Action: Implement the T-matrix formalism for isotopic defects on the graphene lattice. For each phonon mode compute the site‑diagonal Green’s function G_{0,0}^{i,j}(q, ω²+i0) from the ideal dynamical matrix, build the Q(ω²+i0) matrix, invert it, and evaluate the imaginary part of the T-matrix element to obtain τ^{def}_{k,s}. Perform the calculation for three defect scenarios: (a) ideal (Δm/m = 0, n = 0), (b) Al defect (Δm/m = 1.25, n = 0.01), and (c) N defect (Δm/m = 0.1667, n = 0.01). Store τ^{def} arrays.
- Evidence: `/app/outputs/defect_tau.npz`

### Step 5: Total lattice thermal conductivity
- Role: scored (load-bearing)
- Action: For each of the three conditions (ideal, doped_Al, doped_N), combine the relaxation times via Matthiessen’s rule (1/τ = 1/τ^U + 1/τ^{def} + 1/τ^{edge}). Compute the mode specific heat and evaluate the thermal conductivity κ = ½ Σ_{k,s} c_{k,s} v_{k,s}² τ_{k,s} at T=300 K. Sum over the full Brillouin zone mesh. Write the three κ values to a CSV file.
- Output file: `/app/outputs/thermal_conductivity_results.csv`
- Format: csv
- Contract: CSV with columns: condition (string), kappa_W_mK (float). Entries: ideal, doped_Al, doped_N.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_results.csv
- path: `/app/outputs/thermal_conductivity_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity for ideal and doped graphene. The checker will independently recompute the same phonon model and compare the agent's κ values within 10% relative tolerance, and verify the ordering ideal > doped_Al > doped_N.
- schema:
  - `type`: table
  - `required_columns`: `condition`, `kappa_W_mK`

Notes: The scored CSV must contain exactly three rows with conditions 'ideal', 'doped_Al', 'doped_N' and corresponding κ in W/(m·K). No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition",
          "kappa_W_mK"
        ]
      },
      "description": "Lattice thermal conductivity for ideal and doped graphene. The checker will independently recompute the same phonon model and compare the agent's κ values within 10% relative tolerance, and verify the ordering ideal > doped_Al > doped_N."
    }
  ],
  "notes": "The scored CSV must contain exactly three rows with conditions 'ideal', 'doped_Al', 'doped_N' and corresponding κ in W/(m·K). No gold values are disclosed here."
}
```

## How you are scored
Your submitted thermal_conductivity_results.csv is scored by a hidden verifier that independently implements the same physical model (phonon dispersion, Umklapp scattering, edge scattering, T-matrix defect scattering) and recomputes the thermal conductivity for each condition. The verifier compares your reported κ values to its recomputed results within a pre-defined tolerance that accounts for legitimate numerical and implementation differences. It also checks that the relative trend among the three conditions (ideal, Al-doped, N-doped) matches the expected physical ordering. A result that merely repeats a known number without a faithful re-implementation will fail the comparison. The final reward is a weighted combination of the agreement of each condition’s value and the correctness of the overall trend. Only the thermal conductivity values in the scored CSV directly influence the reward; intermediate evidence artifacts are used for consistency but carry no weight in the score.
