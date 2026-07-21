# Monte Carlo Surface Tension Calculation via Free Energy Method

## Problem background
Surface tension of liquids is a fundamental thermodynamic property. A computational method that directly computes the Helmholtz free energy required to create a surface can yield lower statistical uncertainty than mechanical stress calculations. The method is demonstrated for the Lennard‑Jones 6:12 fluid at temperature and density conditions close to the argon triple point.

## Approach
The free energy of surface creation is computed by reversibly converting a bulk liquid with periodic boundary conditions into a slab of liquid held together by its own cohesion. This is accomplished in five stages:

1. **Bulk tail correction** – numerically integrate the Lennard‑Jones potential tail beyond the truncation radius (2.5 σ) for a uniform bulk liquid.
2. **Slab separation** – using Monte Carlo simulations and Bennett's acceptance ratio method, gradually increase the slab separation parameter Δ from 0 to beyond the interaction cut‑off, recording the cumulative free energy change.
3. **Cut‑off distance increase** – using Bennett's method, compute the free energy difference between the slab system with a cut‑off of 2.5 σ and one with a cut‑off of 5.0 σ.
4. **Surface relaxation** – relax the hard walls outward symmetrically while sampling the density at the walls via Monte Carlo; integrate the force (kT × density) along the wall position to obtain the relaxation free energy.
5. **Free surface tail correction** – compute the long‑range correction for the potential tail beyond 5.0 σ for the final free‑surface slab.

The total free energy of surface creation is the sum of these five contributions. The macroscopic surface tension and excess internal energy are then obtained by dividing by the total surface area and converting to cgs units using the argon parameters (ε / k = 119.8 K, σ = 3.405 Å).

## Reproduction target
Implement the five‑stage free‑energy calculation for a system of N = 216 Lennard‑Jones 12:6 particles at reduced temperature T* = 0.7 and reduced density ρ* = 0.85. Perform the required Monte Carlo runs with the specified cut‑off distances (2.5 σ and 5.0 σ) and Bennett’s acceptance ratio method. Compute all five free‑energy differences (Fb−Fa, Fc−Fb, Fd−Fc, Fe−Fd, Ff−Fe). From the total free energy of surface creation, calculate the surface tension γ in dyn/cm and the excess internal energy U_s in erg/cm². Write all intermediate and final results to `/app/outputs/results.json` according to the output contract. The objective is to produce a correct reproduction of the surface properties; a hidden verifier will compare your numbers to reference values that would be obtained from a faithful implementation of the described procedure.

## Assets
This task requires only public knowledge:
- Lennard‑Jones 12:6 pair potential (standard analytic form)
- Bennett acceptance ratio algorithm
- Argon parameters: ε / k = 119.8 K, σ = 3.405 Å (these are fixed physical constants for the conversion to macroscopic units).
No external datasets, models, or proprietary software are needed.

## Detailed simulation parameters
The following Monte Carlo parameters must be used, as specified in the method description.

### General Monte Carlo settings
- Number of particles: N = 216
- Box dimensions: Lx = Ly = (N/(2 ρ*))^{1/3} σ, Lz = 2 Lx (because two cubic boxes each containing 108 molecules are combined). This gives Lx ≈ 5.36 σ.
- Temperature: T* = 0.7 (T = 0.7 ε/k)
- Density: ρ* = 0.85
- Potential cut‑off during slab separation: R_max = 2.5 σ
- “Nearly non‑truncated” cut‑off used after separation and during relaxation: R_max = 5.0 σ
- Metropolis algorithm is used with a maximum trial displacement adjusted at the start of each run to achieve an acceptance ratio of approximately 0.5, and kept fixed thereafter.
- For all Monte Carlo runs the standard periodic boundary conditions in x and y are maintained; in the z‑direction the slab separation Δ is introduced by modifying the periodic images as described in Eq. (2).

### Slab separation (stage b → c)
The separation parameter Δ is increased from 0 to 2.5 σ in the following sequence:
- from Δ = 0.0 to Δ = 0.5 σ: increments of 0.1 σ
- from Δ = 0.5 to Δ = 1.0 σ: increments of 0.25 σ
- from Δ = 1.0 to Δ = 2.5 σ: increments of 0.5 σ

At each Δ value, **two independent Monte Carlo runs** are required (one for the current state with potential U(Δ_i) and one for the next state with potential U(Δ_{i+1})). Each run consists of:
- **Equilibration**: 5×10⁴ attempted moves per particle (total of N × 5×10⁴ = 1.08×10⁷ trial moves)
- **Production**: 1.5×10⁵ attempted moves per particle, during which the energy difference U(Δ_{i+1}) − U(Δ_i) is sampled.

The free energy difference for each step is obtained via Bennett’s formula using the Fermi function form, with the parameter C chosen so that the two acceptance averages are equal (Eq. 7 and Eq. 8).

The cumulative free energy Fc − Fb is the sum over all Δ steps.

### Cut‑off increase (stage c → d)
A single Bennett calculation is performed between the slab system with R_max = 2.5 σ (state c) and the otherwise identical system with R_max = 5.0 σ (state d). The same run lengths as above (5×10⁴ equilibration, 1.5×10⁵ production) are used for each of the two potentials.

### Surface relaxation (stage d → e)
One slab (with two hard walls at z = 0 and z = Lz) is taken from state d. The walls are moved outward **symmetrically** in steps. At each wall position, a Monte Carlo run is performed to measure the equilibrium density at the walls. The free energy change is obtained from the reversible work of moving the walls:
- Starting wall separation: Lz
- Increment per move: 0.05 σ per wall (so the total slab thickness increases by 0.1 σ per step)
- Final wall separation: Lz + 5.0 σ (until the density at the walls is negligibly small, e.g. < 0.01 ρ_bulk)
- At each wall position:
  - Equilibration: 2×10⁴ moves per particle
  - Production: 3×10⁴ moves per particle, sampling the density at the two walls.
The force on a wall at position z_w is ρ(z_w) kT (pressure). The work done when moving the walls from separation Lz to Lz + w is ΔF = −2 * kT * ∫_{Lz/2}^{(Lz+w)/2} ρ(z) dz (integration over half‑slab due to symmetry). A simple trapezoidal integration using the measured wall densities at each step is sufficient.

### Bulk tail correction (stage a → b)
For a uniform liquid at ρ* = 0.85, the free energy difference between the full Lennard‑Jones potential and the potential truncated at R_max = 2.5 σ is computed by integrating the tail correction assuming g(r) = 1 for r ≥ R_max:
Fb − Fa = (1/2) N ρ ∫_{R_max}^{∞} 4π r² u(r) dr
where u(r) = 4ε[(σ/r)^12 − (σ/r)^6]. The integral can be evaluated analytically.

### Free surface tail correction (stage e → f)
Similarly, for the final slab with free surfaces and potential cut‑off 5.0 σ, the tail correction is computed using the same uniform‑density assumption (g(r) = 1) but now for a slab geometry. The correction accounts only for the missing long‑range attractions beyond 5.0 σ within the liquid slab and is applied to the potential energy of the slab; the corresponding free energy difference Ff − Fe is to be obtained by integrating the tail contribution to the energy, assuming the same structure as in the uniform liquid. This correction is small and can be approximated by the same analytical formula as in the bulk, taking into account that the slab has two surfaces and density is zero outside. Compute this correction analytically.

## Workflow steps

### Step 1: Bulk liquid tail correction
- Role: process
- Action: Compute the free energy difference between the full Lennard-Jones potential and the truncated potential (cut-off 2.5σ) for the uniform bulk liquid using numerical integration of the potential tail, assuming uniform radial distribution function. Use the analytical integral of u(r) from R_max to infinity with ρ = ρ* / σ³, N = 216.
- Evidence: `/app/outputs/evidence_bulk_tail.txt`

### Step 2: Monte Carlo slab separation free energy
- Role: process
- Action: Using Monte Carlo simulations and Bennett's acceptance ratio method, gradually separate the bulk liquid into slabs with hard walls by increasing the slab separation parameter Δ from 0 to beyond the cut-off distance, as described in the detailed parameters. Record the cumulative free energy change Fc - Fb.
- Evidence: `/app/outputs/evidence_slab_separation.json`

### Step 3: Cut-off distance increase free energy
- Role: process
- Action: Using Bennett's method, compute the free energy difference between the slab system with potential cut-off 2.5σ and with cut-off 5.0σ, following the run lengths above.
- Evidence: `/app/outputs/evidence_cutoff_increase.txt`

### Step 4: Surface relaxation free energy
- Role: process
- Action: Relax the hard walls by moving them outward symmetrically, sample the density at the walls via Monte Carlo, and integrate the force (kT times density) to obtain the relaxation free energy Fe - Fd, as detailed.
- Evidence: `/app/outputs/evidence_relaxation.json`

### Step 5: Free surface tail correction
- Role: process
- Action: Compute the free energy correction from the potential tail beyond 5.0σ to infinity for the free-surface slab, assuming uniform density. Use the analytical tail integration for the slab geometry (or the same bulk formula as a good approximation).
- Evidence: `/app/outputs/evidence_surface_tail.txt`

### Step 6: Surface tension and excess internal energy
- Role: scored (load-bearing)
- Action: Sum all free energy contributions (Fb-Fa, Fc-Fb, Fd-Fc, Fe-Fd, Ff-Fe) to obtain total free energy of surface creation. Compute the total surface area = 2 * Lx * Ly. Calculate surface tension γ = ΔF_total / (2 * Lx * Ly) and convert to dyn/cm using argon parameters (ε/k = 119.8 K, σ = 3.405 Å, k = 1.380649e-16 erg/K). Compute excess internal energy Us from the average potential energies of the bulk and free-surface states and convert to erg/cm². Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: total_free_energy (float, units of ε), surface_tension (float, dyn/cm), excess_internal_energy (float, erg/cm²), stages : { Fb_minus_Fa: float, Fc_minus_Fb: float, Fd_minus_Fc: float, Fe_minus_Fd: float, Ff_minus_Fe: float }.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/evidence_bulk_tail.txt`
- `/app/outputs/evidence_slab_separation.json`
- `/app/outputs/evidence_cutoff_increase.txt`
- `/app/outputs/evidence_relaxation.json`
- `/app/outputs/evidence_surface_tail.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final aggregated results: total free energy of surface creation, surface tension, excess internal energy, and the five stage free energy differences. The checker compares these to reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `total_free_energy`: number (units of ε)
    - `surface_tension`: number (dyn/cm)
    - `excess_internal_energy`: number (erg/cm²)
    - `stages`:
      - `type`: object
      - `required`:
        - `Fb_minus_Fa`: number (units of ε)
        - `Fc_minus_Fb`: number (units of ε)
        - `Fd_minus_Fc`: number (units of ε)
        - `Fe_minus_Fd`: number (units of ε)
        - `Ff_minus_Fe`: number (units of ε)

### evidence_bulk_tail.txt
- path: `/app/outputs/evidence_bulk_tail.txt`
- format: text
- purpose: intermediate
- schema: `` (free-form text)

### evidence_slab_separation.json
- path: `/app/outputs/evidence_slab_separation.json`
- format: json
- purpose: intermediate
- schema: `` (any valid JSON)

### evidence_cutoff_increase.txt
- path: `/app/outputs/evidence_cutoff_increase.txt`
- format: text
- purpose: intermediate
- schema: `` (free-form text)

### evidence_relaxation.json
- path: `/app/outputs/evidence_relaxation.json`
- format: json
- purpose: intermediate
- schema: `` (any valid JSON)

### evidence_surface_tail.txt
- path: `/app/outputs/evidence_surface_tail.txt`
- format: text
- purpose: intermediate
- schema: `` (free-form text)

Notes: The perturbation theory correction (BFW+ATM) is not required for this core reproduction.

## How you are scored
A hidden verifier reads your `results.json` and independently checks each reported free‑energy difference and the final surface tension and excess internal energy against reference values derived from a faithful implementation. The score is a weighted combination of the closeness of each stage and the final macroscopic properties; meeting or exceeding the reference quality within expected reproduction tolerances earns full credit. Simply printing expected numbers is not sufficient – the workflow must be executed and the evidence of intermediate computations must be consistent with the final results.