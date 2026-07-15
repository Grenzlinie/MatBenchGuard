# First-principles electron-phonon coupling and superconducting properties of a decorated graphene system

## Problem background
Li-decorated graphene is a candidate phonon-mediated superconductor. The strength of the electron-phonon coupling and the resulting superconducting transition temperature can be influenced by the choice of substrate. This work investigates how a hexagonal boron nitride (h-BN) substrate affects the electron-phonon coupling and superconducting properties of Li-decorated graphene, using first-principles density functional theory and density functional perturbation theory. The central question is whether and by how much the presence of an h-BN substrate changes the electron-phonon coupling constant λ, the logarithmic average frequency ⟨ω⟩_log, the superconducting transition temperature Tc, and the superconducting gap Δ_sc relative to the same system in free-standing (suspended) form.

## Approach
You will perform a first-principles computational workflow to determine the electron-phonon coupling and superconducting properties for two atomic configurations: (i) suspended Li-decorated graphene, and (ii) the same Li-decorated monolayer supported by an h-BN substrate. The calculations are carried out within density functional theory (DFT) using the local density approximation (LDA) with the Grimme D2 van der Waals correction. The crystal structures are modelled as √3×√3R30° supercells. For the suspended system, the in‑plane lattice constant is a=b=4.26 Å and the vacuum spacing is c=15 Å, with the Li atom placed at the hollow site above the center of a C hexagon. For the supported system, the supercell has a=b=4.32 Å, c=15 Å; the graphene layer (laterally strained to 4.32 Å) is placed on top of an h‑BN monolayer in the Bernal stacking registry (carbon sublattices above B and N sites), and the Li atom occupies the hollow site above a C hexagon. 

The workflow consists of two main stages. First, the atomic positions and lattice parameters are relaxed through DFT geometry optimization. Second, using the relaxed structures, the phonon dispersions and electron-phonon matrix elements are computed within density functional perturbation theory (DFPT) on a fine wave vector grid. From the DFPT results, the isotropic Eliashberg function α²F(ω) is constructed. The electron-phonon coupling constant λ is then obtained by integrating α²F(ω)/ω, and the logarithmic average frequency ⟨ω⟩_log is calculated from the same spectrum. Using these quantities, the superconducting transition temperature Tc is evaluated with the Allen-Dynes formula, employing a Coulomb pseudopotential μ* = 0.115. Finally, the superconducting gap is estimated via the BCS relation Δ_sc = 1.75 k_B Tc. 

The same scheme is applied to both the suspended and the h-BN-supported systems, and the resulting λ, ⟨ω⟩_log, Tc, and Δ_sc are compared to reveal the effect of the substrate.

## Reproduction target
Produce a single JSON file named `results.json` that contains the raw Eliashberg spectral data and the derived superconducting quantities for both structural configurations. The file must have two top-level keys: `suspended` and `supported`. For each configuration, store the following fields:
  - `omega`: list of frequencies (in cm⁻¹) on which α²F(ω) is evaluated,
  - `alpha2F`: list of the corresponding α²F(ω) values,
  - `lambda`: the electron-phonon coupling constant (dimensionless),
  - `log_avg_freq`: the logarithmic average frequency (in cm⁻¹),
  - `Tc`: the superconducting transition temperature (in K) computed with the Allen-Dynes formula (μ* = 0.115),
  - `delta_sc`: the superconducting gap (in meV) computed as 1.75 k_B T_c.

All values must be derived from your own DFT and DFPT calculations. The goal is to faithfully reproduce the electron-phonon coupling and superconducting properties of the two systems.

## Assets

- QuantumESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for C, Li, B, N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform DFT structural relaxation (LDA + Grimme D2 van der Waals, plane-wave cutoff 70 Ryd, 32×32×1 Monkhorst–Pack k‑mesh, energy convergence 10⁻⁷ eV, force convergence 0.002 eV/Å) for the suspended Li‑decorated graphene √3×√3R30° supercell and the h‑BN‑supported supercell using QuantumESPRESSO pw.x. Obtain optimized atomic coordinates and lattice parameters.
- Evidence: `/app/outputs/optimization.log`

### Step 2: DFPT phonon and electron‑phonon coupling calculation
- Role: process
- Action: Run DFPT phonon dispersion calculation on a 24×24×1 q‑grid and evaluate electron‑phonon matrix elements for both systems using QuantumESPRESSO ph.x and related tools (q2r.x, matdyn.x, lambda.x). Generate the dynamical matrices and the electron‑phonon coupling data needed to construct α²F(ω).
- Evidence: `/app/outputs/eph_output.tar.gz`

### Step 3: Compute Eliashberg function, λ, ω_log, T_c, and Δ_sc
- Role: scored (load-bearing)
- Action: From the completed phonon and electron‑phonon calculations, construct the isotropic Eliashberg function α²F(ω) and compute the electron‑phonon coupling constant λ = 2 ∫ α²F(ω)/ω dω, the logarithmic average frequency ⟨ω⟩_log, the superconducting transition temperature T_c using the Allen‑Dynes formula (μ* = 0.115), and the superconducting gap Δ_sc = 1.75 k_B T_c. Output omega (cm⁻¹), alpha2F, lambda, log_avg_freq (cm⁻¹), Tc (K), and delta_sc (meV) for the suspended and the supported systems.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Top-level keys: 'suspended' and 'supported'. Each value is an object with fields: 'omega' (list of floats, cm⁻¹), 'alpha2F' (list of floats), 'lambda' (float), 'log_avg_freq' (float, cm⁻¹), 'Tc' (float, K), 'delta_sc' (float, meV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Scored artifact containing the raw α²F(ω) arrays and the derived superconducting quantities λ, ⟨ω⟩_log, Tc, Δ_sc for both suspended and h-BN-supported systems.
- schema:
  - `type`: object
  - `required`: `suspended`, `supported`
  - `items`:
    - `omega`: list of float
    - `alpha2F`: list of float
    - `lambda`: float
    - `log_avg_freq`: float
    - `Tc`: float
    - `delta_sc`: float
  - `units`:
    - `omega`: cm⁻¹
    - `log_avg_freq`: cm⁻¹
    - `Tc`: K
    - `delta_sc`: meV

Notes: The checker recomputes λ and ⟨ω⟩_log from the provided omega and alpha2F arrays, performs consistency checks, and then compares the agent’s reported λ, ⟨ω⟩_log, Tc, and Δ_sc to hidden paper gold values with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "suspended",
          "supported"
        ],
        "items": {
          "omega": "list of float",
          "alpha2F": "list of float",
          "lambda": "float",
          "log_avg_freq": "float",
          "Tc": "float",
          "delta_sc": "float"
        },
        "units": {
          "omega": "cm⁻¹",
          "log_avg_freq": "cm⁻¹",
          "Tc": "K",
          "delta_sc": "meV"
        }
      },
      "description": "Scored artifact containing the raw α²F(ω) arrays and the derived superconducting quantities λ, ⟨ω⟩_log, Tc, Δ_sc for both suspended and h-BN-supported systems."
    }
  ],
  "notes": "The checker recomputes λ and ⟨ω⟩_log from the provided omega and alpha2F arrays, performs consistency checks, and then compares the agent’s reported λ, ⟨ω⟩_log, Tc, and Δ_sc to hidden paper gold values with appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your `results.json` and independently recomputes λ and ⟨ω⟩_log by numerical integration of the α²F(ω)/ω data you provided. It checks that your reported λ and ⟨ω⟩_log are consistent with the raw arrays. It then compares your final values for λ, ⟨ω⟩_log, Tc, and Δ_sc against confidential reference benchmarks, using tolerances that account for legitimate differences between DFT implementations. Both systems are scored separately, and the per-stage scores are combined by weight into a single final reward in the range [0, 1]. Providing the correct spectral arrays and derived quantities as described is essential; simply reporting numbers without the underlying α²F(ω) data will receive no credit.
