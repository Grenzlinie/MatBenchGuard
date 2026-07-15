# Phase-field mapping of interfacial anisotropy for Cu

## Problem background
In cubic metals, the interfacial energy between phases is orientation‑dependent. This anisotropy determines crystal morphologies during growth and phase transformations. Phase‑field models are widely used to simulate microstructure evolution, but they require accurate representations of anisotropic interfacial energy and its mapping to gradient‑energy coefficients. This work addresses that connection: a series expansion for the orientation‑dependent interfacial energy is proposed, based on cubic symmetry, and a closed‑form algebraic relationship is derived that links the coefficients of that expansion to the gradient‑energy coefficients used in phase‑field simulations. The approach is validated against embedded‑atom method calculations. The task is to reproduce this mapping for copper and to verify it through a combination of atomistic surface‑energy calculations, least‑squares fitting, and a phase‑field simulation whose resulting shape is compared with the equilibrium Wulff shape.

## Approach
The conceptual method consists of three stages:

1. **Atomistic surface‑energy computation**: Use molecular dynamics (LAMMPS) with a copper embedded‑atom potential to calculate the relaxed surface energy for four representative orientations: (100), (110), (111), and (210). These four energies are sufficient to determine the four coefficients of the interfacial‑energy expansion.

2. **Fitting and mapping**: Fit the four‑term expansion for interfacial energy to the computed surface energies, obtaining coefficients k0, k1, k2, k3. Then apply the analytically derived mapping that converts these k‑coefficients into gradient‑energy coefficients ε0, ε1, ε2, ε3. The mapping uses a prescribed interface thickness λ (here 14.3 nm) to set the absolute scale and relates ε0 to √k0 and the ratios εi/ε0 to combinations of the k‑coefficients.

3. **Phase‑field simulation and shape comparison**: Implement a two‑dimensional phase‑field model with a double‑well free energy and the orientation‑dependent gradient‑energy coefficient ε(θ) built from the computed ε‑coefficients. Parameters for the chemical free‑energy difference (g0−g1), mobility, and grid resolution are fixed. A circular seed is placed at the domain centre and evolved to a steady shape. The final interface points are extracted, and the equilibrium shape predicted by Wulff’s theorem from the k‑coefficients is constructed. The mean absolute angular deviation between the simulated interface and the Wulff shape is computed as the final quantitative comparison.

## Reproduction target
For copper, using the Mishin Cu EAM potential (publicly available) and LAMMPS, compute the surface energies of the (100), (110), (111), and (210) orientations at 0 K. Fit the four‑term interfacial‑energy expansion to these energies to obtain k0, k1, k2, k3 (erg/cm²). Using the interface thickness λ = 14.3 nm and the fitted k0, compute the gradient‑energy coefficients ε0, ε1, ε2, ε3 (J^{1/2} m^{-1/2}) via the derived algebraic mapping. Implement a 2D phase‑field simulation (fixed parameters g0−g1 = 3.6×10⁸ J m⁻³, Mφ = 100, λ = 14.3 nm, grid spacing Δx = 0.5λ, domain 128×128 grids) with a circular seed and evolve to a steady shape. Extract the interface points and compute the mean absolute angular deviation (degrees) between the simulated shape and the Wulff equilibrium shape predicted from the k‑coefficients. The scored deliverables are the fitted k‑coefficients (fitted_k_coefficients.json), the computed ε‑coefficients (computed_epsilon_coefficients.json), and the angular deviation (phasefield_vs_wulff_deviation.txt).

## Assets

- Mishin Cu EAM potential (2011): https://www.ctcms.nist.gov/potentials/Download/2011-Mishin-Cu-eam.alloy_Cu_mish1.eam.alloy
- LAMMPS Molecular Dynamics Simulator: https://lammps.sandia.gov
- SciPy: scipy
- NumPy: numpy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Compute Cu surface energies with LAMMPS
- Role: process
- Action: Use LAMMPS with the Mishin Cu EAM potential to compute the relaxed surface energy (energy per unit area) for the (100), (110), (111), and (210) surfaces at 0 K. For each orientation create a slab, relax atomic positions, and extract the surface energy. Write the four energies to surface_energies.json.
- Evidence: `/app/outputs/surface_energies.json`

### Step 2: Fit interfacial energy expansion coefficients
- Role: scored
- Action: Perform least-squares fitting of the four-term expansion for interfacial energy σ(hkl) = k0 + k1*(h²k²+...)/(...)^2 + k2*... + k3*... to the four surface energies from surface_energies.json. Obtain the coefficients k0, k1, k2, k3 (units erg/cm²). Write the result to fitted_k_coefficients.json.
- Output file: `/app/outputs/fitted_k_coefficients.json`
- Format: json
- Contract: {"k0": float, "k1": float, "k2": float, "k3": float}
- Scoring: scored by hidden verifier

### Step 3: Map k-coefficients to gradient-energy coefficients
- Role: scored
- Action: Using λ=14.3 nm and the fitted k0 from step_fit_k, compute ε0 via the relation ε0 = sqrt(3λ/1.1) * sqrt(k0). Then compute the normalized ratios ε1/ε0, ε2/ε0, ε3/ε0 from k-coefficients using the algebraic formulas that map k-coefficients to ε-coefficients. Scale back to absolute ε1, ε2, ε3 (all in J^{1/2} m^{-1/2}). Write ε0, ε1, ε2, ε3 to computed_epsilon_coefficients.json.
- Output file: `/app/outputs/computed_epsilon_coefficients.json`
- Format: json
- Contract: {"epsilon0": float, "epsilon1": float, "epsilon2": float, "epsilon3": float}
- Scoring: scored by hidden verifier

### Step 4: 2D phase-field simulation of crystal growth
- Role: process
- Action: Implement a 2D phase-field model for a double‑well free energy with orientation‑dependent gradient‑energy coefficient ε(θ) using the ε coefficients from step_epsilon. Use parameters g0−g1=3.6×10⁸ J m⁻³, Mφ=100, λ=14.3 nm, grid spacing Δx=0.5λ, a domain of 128×128 grids. Initialize a circular seed of radius 4Δx with the standard hyperbolic‑tangent interface profile. Evolve the phase field to equilibrium (or a fixed number of time steps such as 5000) and output the final interface points (r, θ) to phasefield_interface.csv.
- Evidence: `/app/outputs/phasefield_interface.csv`

### Step 5: Compute angular deviation from Wulff shape
- Role: scored (load-bearing)
- Action: Using the interface points from phasefield_interface.csv and the k-coefficients from step_fit_k, construct the Wulff equilibrium shape as the inner envelope of the polar plot σ(θ) (the 2D version of the interfacial energy expansion). Calculate the mean absolute angular deviation (in degrees) between the simulated interface orientation and the Wulff shape orientation. Write the single float to phasefield_vs_wulff_deviation.txt.
- Output file: `/app/outputs/phasefield_vs_wulff_deviation.txt`
- Format: txt
- Contract: single float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_k_coefficients.json`
- `/app/outputs/computed_epsilon_coefficients.json`
- `/app/outputs/phasefield_vs_wulff_deviation.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_k_coefficients.json
- path: `/app/outputs/fitted_k_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted interfacial energy expansion coefficients k0..k3 for Cu, to be verified by recomputing from the agent's surface_energies.json (internal consistency check).
- schema:
  - `type`: object
  - `required`:
    - `k0`: float (erg/cm²)
    - `k1`: float (erg/cm²)
    - `k2`: float (erg/cm²)
    - `k3`: float (erg/cm²)

### computed_epsilon_coefficients.json
- path: `/app/outputs/computed_epsilon_coefficients.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Gradient‑energy coefficients ε0..ε3 derived from the k‑coefficients via the closed‑form mapping, recomputed by the verifier from the submitted k‑coefficients.
- schema:
  - `type`: object
  - `required`:
    - `epsilon0`: float (J^{1/2} m^{-1/2})
    - `epsilon1`: float (J^{1/2} m^{-1/2})
    - `epsilon2`: float (J^{1/2} m^{-1/2})
    - `epsilon3`: float (J^{1/2} m^{-1/2})

### phasefield_vs_wulff_deviation.txt
- path: `/app/outputs/phasefield_vs_wulff_deviation.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Mean absolute angular deviation (degrees) between the phase‑field simulated interface and the Wulff equilibrium shape; lower is better.
- schema:
  - `type`: text
  - `content`: single float

Notes: The k‑coefficients are recomputed from surface_energies.json and checked for internal consistency. The ε‑coefficients are recomputed from the submitted k‑coefficients. The angular deviation is scored by threshold: ≤ some hidden value earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_k_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "k0": "float (erg/cm²)",
          "k1": "float (erg/cm²)",
          "k2": "float (erg/cm²)",
          "k3": "float (erg/cm²)"
        }
      },
      "description": "Fitted interfacial energy expansion coefficients k0..k3 for Cu, to be verified by recomputing from the agent's surface_energies.json (internal consistency check)."
    },
    {
      "file": "computed_epsilon_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "epsilon0": "float (J^{1/2} m^{-1/2})",
          "epsilon1": "float (J^{1/2} m^{-1/2})",
          "epsilon2": "float (J^{1/2} m^{-1/2})",
          "epsilon3": "float (J^{1/2} m^{-1/2})"
        }
      },
      "description": "Gradient‑energy coefficients ε0..ε3 derived from the k‑coefficients via the closed‑form mapping, recomputed by the verifier from the submitted k‑coefficients."
    },
    {
      "file": "phasefield_vs_wulff_deviation.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "content": "single float"
      },
      "description": "Mean absolute angular deviation (degrees) between the phase‑field simulated interface and the Wulff equilibrium shape; lower is better."
    }
  ],
  "notes": "The k‑coefficients are recomputed from surface_energies.json and checked for internal consistency. The ε‑coefficients are recomputed from the submitted k‑coefficients. The angular deviation is scored by threshold: ≤ some hidden value earns full credit."
}
```

## How you are scored
A hidden verifier independently checks your three scored artifacts. For the k‑coefficients and ε‑coefficients, your values are compared against hidden reference values with appropriate tolerances. For the angular deviation, the verifier checks whether the reported number is at or below a hidden threshold (lower is better, reflecting fidelity to the Wulff shape). The three checks are weighted and combined to produce a single reward between 0 and 1. Submitting values that match or surpass the expected quality yields full credit; larger deviations reduce the reward progressively. Empty or missing artifacts score zero.
