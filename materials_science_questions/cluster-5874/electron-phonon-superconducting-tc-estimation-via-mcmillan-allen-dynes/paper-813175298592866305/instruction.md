# Estimation of Superconducting Properties from First-Principles Electron-Phonon Calculations

## Problem background
Li-decorated graphene is a candidate superconducting material, and its properties can potentially be modified by placing it on a substrate. This task concerns the effect of a hexagonal boron nitride (h-BN) substrate on the electron-phonon coupling and superconducting transition temperature. Using first-principles density functional theory calculations, we compute the optimized geometries, electronic structures, phonon dispersions, and Eliashberg functions for both suspended and h-BN supported Li-decorated graphene. From these, the electron-phonon coupling constant $\lambda$, logarithmic average frequency $\omega_{\log}$, superconducting critical temperature $T_c$ (via the Allen-Dynes formula), and superconducting gap $\Delta_{sc}$ are evaluated. By comparing the results for the suspended and supported systems, one can assess the role of the substrate in the superconductivity of this graphene-based material.

## Approach
The calculations employ density functional theory (DFT) in the local density approximation (LDA) with van der Waals corrections (Grimme's scheme) to obtain reliable interlayer distances. Geometry optimizations are performed for two models: a $\sqrt{3}\times\sqrt{3}R30^\circ$ Li-decorated graphene supercell (suspended), and the same supercell placed on a h-BN substrate with a small lattice mismatch. After relaxation, electronic band structures are computed along high-symmetry paths. Phonon dispersions and the Eliashberg function $\alpha^2F(\omega)$ are obtained via density functional perturbation theory (DFPT). Finally, the electron-phonon coupling constant $\lambda$ is calculated from the integral of $\alpha^2F(\omega)/\omega$, the logarithmic average frequency $\omega_{\log}$ is derived, and the superconducting transition temperature $T_c$ is evaluated using the Allen-Dynes formula with a fixed Coulomb pseudopotential $\mu^* = 0.115$. The superconducting gap $\Delta_{sc}$ is estimated from $T_c$ via the BCS relation $\Delta_{sc} = 1.75 \, k_B T_c$. The entire procedure is repeated identically for the suspended and the supported systems to enable a direct comparison of the superconducting properties under the two conditions.

## Reproduction target
Run the full DFT/DFPT workflow described in the steps below for both suspended and h-BN supported Li-decorated graphene. From the computed Eliashberg functions, extract the following quantities for each system: the electron-phonon coupling constant $\lambda$, the logarithmic average phonon frequency $\omega_{\log}$ (in cm$^{-1}$), the superconducting critical temperature $T_c$ (in Kelvin), and the superconducting gap $\Delta_{sc}$ (in meV). Report all eight numbers in a single JSON file (`superconducting_properties.json`) according to the output contract. The objective is to obtain these superconducting parameters through first-principles calculations, not by looking up known values.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials (C, Li, B, N): http://www.pseudo-dojo.org/
- Grimme's van der Waals correction (DFT-D3): dftd3 (included with Quantum ESPRESSO distribution)

## Workflow steps

### Step 1: DFT geometry optimization of suspended Li-decorated graphene
- Role: process
- Action: Build the atomic model for the suspended Li-decorated graphene system: a √3×√3R30° supercell with a=2.26 Å, containing 6 C atoms and 1 Li atom placed above a hollow site. Perform DFT geometry relaxation using LDA + Grimme's VDW correction with a plane-wave cutoff of 70 Ryd, k-mesh 32×32×1, energy convergence 10⁻⁷ eV and force convergence 0.002 eV/Å. Obtain the relaxed lattice parameters and atomic positions (including the Li–graphene perpendicular distance).
- Evidence: `/app/outputs/suspended_relaxed_structure.txt`

### Step 2: DFT geometry optimization of supported Li-decorated graphene on h-BN
- Role: process
- Action: Build the supported model: the relaxed Li-decorated graphene supercell placed on top of a hexagonal boron nitride substrate, with supercell lattice parameters a=b=4.32 Å, c=15 Å. Relax the entire system using the same DFT parameters as for the suspended case. Obtain the relaxed geometry (Li–graphene distance, graphene–h-BN separation).
- Evidence: `/app/outputs/supported_relaxed_structure.txt`

### Step 3: Electronic band structure for suspended system
- Role: process
- Action: Using the optimized suspended geometry, run a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation along the high-symmetry k-path Γ–M–K–Γ. Save the band energies.
- Evidence: `/app/outputs/suspended_band_structure.dat`

### Step 4: Electronic band structure for supported system
- Role: process
- Action: Using the optimized supported geometry, compute the electronic band structure along the same high-symmetry path. Save the band energies.
- Evidence: `/app/outputs/supported_band_structure.dat`

### Step 5: Phonon and electron-phonon coupling for suspended system
- Role: process
- Action: Using density functional perturbation theory (DFPT) with the optimized suspended geometry, compute the phonon dispersion on a 24×24×1 q-grid and the Eliashberg function α²F(ω). Save the α²F(ω) data as a two-column file (frequency in cm⁻¹, α²F).
- Evidence: `/app/outputs/suspended_alpha2F.dat`

### Step 6: Phonon and electron-phonon coupling for supported system
- Role: process
- Action: Perform DFPT for the optimized supported geometry, using the same 24×24×1 q-grid, to obtain the phonon dispersion and Eliashberg function. Save the α²F(ω) data.
- Evidence: `/app/outputs/supported_alpha2F.dat`

### Step 7: Calculate superconducting properties via Allen-Dynes formula
- Role: scored
- Action: For each system (suspended and supported), read the α²F(ω) data and compute the electron-phonon coupling constant λ using the integral λ = 2 ∫₀^∞ (α²F(ω)/ω) dω, the logarithmic average frequency ω_log, and then the critical temperature Tc via the Allen-Dynes formula (with Coulomb pseudopotential μ* = 0.115). Also compute the superconducting gap Δ_sc = 1.75 kB Tc. Write all eight quantities (λ, ω_log [cm⁻¹], Tc [K], gap [meV] for both systems) to a single JSON file.
- Output file: `/app/outputs/superconducting_properties.json`
- Format: json
- Contract: {
  "suspended": {
    "lambda": <number>,
    "omega_log_cm-1": <number>,
    "Tc_K": <number>,
    "gap_meV": <number>
  },
  "supported": {
    "lambda": <number>,
    "omega_log_cm-1": <number>,
    "Tc_K": <number>,
    "gap_meV": <number>
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/superconducting_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### superconducting_properties.json
- path: `/app/outputs/superconducting_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the eight superconducting quantities for both systems, computed from the Eliashberg functions and the Allen-Dynes formula. The checker compares each value to the paper's reported values within prescribed tolerances.
- schema:
  - `type`: object
  - `required`:
    - `suspended`:
      - `lambda`: number (dimensionless, electron-phonon coupling constant)
      - `omega_log_cm-1`: number (logarithmic average frequency in cm⁻¹)
      - `Tc_K`: number (critical temperature in Kelvin)
      - `gap_meV`: number (superconducting gap in meV)
    - `supported`:
      - `lambda`: number
      - `omega_log_cm-1`: number
      - `Tc_K`: number
      - `gap_meV`: number
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The process steps (geometry optimizations, band structures, phonon calculations) produce intermediate artifacts that are not directly scored but are necessary to derive the final superconducting properties. The scoring is result-level (T0) and uses exact-match with tolerances because the target values are fixed by the computational setup and the paper's reported results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "superconducting_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "suspended": {
            "lambda": "number (dimensionless, electron-phonon coupling constant)",
            "omega_log_cm-1": "number (logarithmic average frequency in cm⁻¹)",
            "Tc_K": "number (critical temperature in Kelvin)",
            "gap_meV": "number (superconducting gap in meV)"
          },
          "supported": {
            "lambda": "number",
            "omega_log_cm-1": "number",
            "Tc_K": "number",
            "gap_meV": "number"
          }
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Contains the eight superconducting quantities for both systems, computed from the Eliashberg functions and the Allen-Dynes formula. The checker compares each value to the paper's reported values within prescribed tolerances."
    }
  ],
  "notes": "The process steps (geometry optimizations, band structures, phonon calculations) produce intermediate artifacts that are not directly scored but are necessary to derive the final superconducting properties. The scoring is result-level (T0) and uses exact-match with tolerances because the target values are fixed by the computational setup and the paper's reported results."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores each required artifact. For the scored `superconducting_properties.json`, the verifier compares your eight computed quantities ($\lambda$, $\omega_{\log}$, $T_c$, $\Delta_{sc}$ for suspended and supported cases) against reference values (with suitable tolerances) and assigns a score based on how many are within tolerance. Additional process evidence (relaxed structures, band structure data, Eliashberg function files) may be checked for consistency but carries minimal weight. You must execute the full computational pipeline; simply reporting the expected numbers without genuine DFT/DFPT calculations will not produce a valid result. The total reward is a float between 0 and 1.
