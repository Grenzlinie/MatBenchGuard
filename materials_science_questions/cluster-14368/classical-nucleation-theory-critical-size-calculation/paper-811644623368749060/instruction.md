# Plasma-Assisted Nanowire Nucleation: Droplet Temperature, Energy Barrier, and Critical Diameter

## Problem background
Plasma-enhanced chemical vapor deposition (PECVD) offers a path toward synthesizing thin silicon nanowires at low substrate temperatures, but the nucleation of very thin nanowires is impeded by the Gibbs–Thomson effect, which increases the energy barrier for nucleation as the catalyst nanoparticle size decreases.  Understanding how plasma-generated species (ions, radicals) heat the catalyst nanoparticle and create silicon building units (BUs) is crucial for predicting nucleation characteristics—droplet temperature, the monolayer nucleation energy barrier, the early-stage growth rate, and the Gibbs–Thomson critical diameter.  In this task you will implement a coupled set of numerical models that link plasma sheath parameters to nanowire nucleation and compute these four quantities for a single well‑specified PECVD condition.

## Approach
The workflow combines four interdependent submodels that must be solved sequentially:

1. **Plasma sheath model** – Solve the one‑dimensional fluid equations (continuity, momentum, Poisson) for a multi‑species plasma (Ar⁺, SiH₃⁺, H⁺, and electrons) to obtain the fluxes and kinetic energies of ions and neutrals arriving at the substrate surface.  Inputs are the bulk plasma parameters: electron density, electron temperature, ion temperature, gas pressure, gas composition, and the substrate bias potential.

2. **Surface mass‑balance model** – Using the sheath‑derived fluxes, write the steady‑state balance equations for Si, SiH₃, and H adatoms on the hemispherical catalyst nanoparticle surface.  Solve the resulting angular diffusion equation for the Si adatom concentration, which yields the bulk‑diffusion and surface‑diffusion fluxes of silicon into the droplet.

3. **Heat‑transfer model** – Balance the heating channels (ion bombardment, recombination, neutral chemisorption) against the cooling channels (thermal dissociation, desorption, evaporation) to obtain the heat flux density into the nanoparticle.  With the substrate holder temperature fixed, the droplet temperature is found by root‑finding (bisection) from the steady‑state heat‑conduction equation through the silicon substrate.

4. **Nucleation model** – From the Si fluxes and the droplet temperature, compute the supersaturation of the liquid Au–Si alloy, the Gibbs–Thomson‑corrected chemical‑potential difference between the liquid and solid phases, the monolayer nucleation energy barrier ΔH_N*, the Gibbs–Thomson critical diameter d_c, and the early‑stage growth rate R_t.

The four submodels are coupled: the sheath provides ion/neutral fluxes that drive the surface mass balance, which together with the heat transfer determines the droplet temperature, and the temperature together with the Si fluxes feeds the nucleation calculation.  You must implement and solve this full chain numerically.

## Reproduction target
Implement the four‑submodel pipeline described above and compute the following four quantities for the specific PECVD input parameter set listed below, with the Gibbs‑Thomson effect included:

- Droplet temperature T_d (K)
- Monolayer nucleation energy barrier ΔH_N* (J)
- Early‑stage growth rate R_t (cm s⁻¹)
- Gibbs‑Thomson critical diameter d_c (nm)

Input parameters:
- n_e0 = 5 × 10¹² cm⁻³
- T_e = 1.5 eV
- T_i = 0.05 eV
- p_0 = 50 mTorr
- r_d = 5 nm
- φ_s = −100 V
- Gas composition: r_Ar = 70 %, r_SiH = 20 %, r_H = 10 %
- Substrate holder temperature T_h = 500 °C

Write the four values to the file `/app/outputs/results.json` as a JSON object with the exact keys `T_d`, `Delta_H_N_star`, `R_t`, and `d_c` (floating‑point numbers in the specified units).

## Assets

- Python scientific computing environment (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Plasma Sheath Simulation
- Role: process
- Action: Solve the fluid sheath equations (continuity, momentum, Poisson) for the given plasma parameters (electron temperature, electron density, ion temperature, gas pressure, gas composition, substrate potential) to obtain ion fluxes and energies (Ar+, SiH3+, H+) and neutral fluxes at the substrate surface. Use the results as inputs for the subsequent surface mass/heat balance.
- Evidence: none

### Step 2: Compute Nucleation Characteristics
- Role: scored (load-bearing)
- Action: Using the ion/neutral fluxes from step_0, solve the surface mass‑balance differential equation for Si adatom concentration, then solve the heat‑balance equation to find the droplet temperature T_d. From T_d and the Si fluxes, compute supersaturation, the GT‑corrected chemical potential difference, the monolayer nucleation energy barrier ΔH_N*, the GT critical diameter d_c, and the early‑stage growth rate R_t for a single set of input parameters (n_e0 = 5×10^12 cm⁻³, T_e = 1.5 eV, T_i = 0.05 eV, p_0 = 50 mTorr, r_d = 5 nm, φ_s = −100 V, gas composition r_Ar=70%, r_SiH=20%, r_H=10%, and substrate holder temperature T_h = 500 °C) with the Gibbs‑Thomson effect included. Write the four values to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'T_d' (float, K), 'Delta_H_N_star' (float, J), 'R_t' (float, cm/s), 'd_c' (float, nm).
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
- target_policy: reference_match
- description: Computed droplet temperature (T_d), monolayer nucleation energy barrier (ΔH_N*), early-stage growth rate (R_t), and Gibbs‑Thomson critical diameter (d_c) for the specified PECVD input parameters.
- schema:
  - `type`: object
  - `required`: `T_d`, `Delta_H_N_star`, `R_t`, `d_c`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `T_d`: K
    - `Delta_H_N_star`: J
    - `R_t`: cm/s
    - `d_c`: nm

Notes: All four values are compared to the paper’s computed results for the identical parameter set using hidden relative tolerances. The agent must produce these values by running the full coupled submodels (sheath → surface/heat → nucleation) as described in the public instruction.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "T_d",
          "Delta_H_N_star",
          "R_t",
          "d_c"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "T_d": "K",
          "Delta_H_N_star": "J",
          "R_t": "cm/s",
          "d_c": "nm"
        }
      },
      "description": "Computed droplet temperature (T_d), monolayer nucleation energy barrier (ΔH_N*), early-stage growth rate (R_t), and Gibbs‑Thomson critical diameter (d_c) for the specified PECVD input parameters."
    }
  ],
  "notes": "All four values are compared to the paper’s computed results for the identical parameter set using hidden relative tolerances. The agent must produce these values by running the full coupled submodels (sheath → surface/heat → nucleation) as described in the public instruction."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/results.json` and compare each of the four computed quantities against reference values obtained for exactly the same input parameters.  Each quantity is compared with a hidden relative tolerance; your reward increases with the number of quantities that fall within the allowed tolerance.  You must genuinely execute the coupled physical models (sheath → surface mass balance → heat balance → nucleation) — simply guessing or reporting an approximate value is unlikely to match the hidden reference.  The final score is a float between 0 and 1 that reflects the fraction of quantities within tolerance.
