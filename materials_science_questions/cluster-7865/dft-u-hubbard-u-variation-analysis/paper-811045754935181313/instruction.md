## Problem background

Magnesium oxide (MgO) is a wide‑band‑gap insulator used in spintronics and optoelectronics. Doping MgO with a transition metal like manganese (Mn) can induce magnetism and, under a strong crystal field (low‑spin configuration), half‑metallic behaviour. This work studies how the low‑spin (S=1/2) configuration affects the electronic structure, magnetic moments, and optical response of Mn‑doped MgO compared with the usual high‑spin (S=5/2) configuration, using first‑principles DFT calculations with and without a Hubbard U correction. The central idea is to compute spin‑resolved band gaps, exchange coupling parameters, site‑projected magnetic moments, and spin‑polarised optical band gaps derived from the frequency‑dependent dielectric function. The task evaluates whether the low‑spin state indeed leads to half‑metallic ferromagnetism and a measurable reduction of the optical band gap relative to the high‑spin state.

## Approach

A 2×2×2 rocksalt MgO supercell (32 atoms) is built and one Mg atom is replaced by Mn (12.5 % doping). The lattice parameter is optimised by DFT. Spin‑polarised electronic structure calculations are then performed with the local spin density approximation (LSDA) and LSDA+U (effective U = 6 eV) for two initial spin configurations: weak‑field (high‑spin, S=5/2) and strong‑field (low‑spin, S=1/2). The calculations yield charge densities, band structures, density of states, and total and site‑projected magnetic moments. From the band edges, spin splittings of the valence and conduction bands are computed, which are used to derive the s‑d exchange parameter Nα and the p‑d exchange parameter Nβ via the mean‑field formulas. Using the DFT wavefunctions, the complex frequency‑dependent dielectric function ε(ω) = ε₁(ω) + iε₂(ω) is calculated. The absorption coefficient α(ω) is obtained from ε₁ and ε₂, and spin‑resolved optical band gaps are extracted by constructing Tauc plots of (αhν)² against photon energy hν and linearly extrapolating to zero. The percentage reduction of the optical gap in the strong‑field case relative to the weak‑field case is then computed for each spin channel at U = 0 eV and U = 6 eV.

## Reproduction target

For Mn‑doped MgO in both the weak‑field (high‑spin) and strong‑field (low‑spin) configurations, and for LSDA (U = 0 eV) and LSDA+U (U = 6 eV), produce the following quantities:
- Majority‑spin and minority‑spin electronic band gaps, valence‑band and conduction‑band spin splittings, and the exchange parameters Nα and Nβ.
- Total magnetic moment and site‑projected moments on Mg, Mn, O, and the interstitial region.
- Spin‑up and spin‑down optical band gaps (from Tauc plots) for all four condition combinations, and the resulting percentage reduction of the optical gap in the strong‑field case relative to weak‑field for each spin and each U value.

## Assets

- **Quantum ESPRESSO** – open‑source plane‑wave DFT code (version 6.x or later). Access: https://www.quantum‑espresso.org/
- **SSSP pseudopotentials for Mg, O, and Mn** – norm‑conserving or PAW pseudopotentials from the SSSP library (efficiency 1.3 or later). Access: https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Structure preparation and lattice optimization
- Role: process
- Action: Build a 2×2×2 rocksalt MgO supercell (32 atoms), substitute one Mg with Mn (12.5% doping). Optimize the lattice constant by DFT, starting from the experimental lattice parameter a = 4.213 Å, to obtain the equilibrium lattice parameter.
- Evidence: `/app/outputs/relax.out`

### Step 2: DFT electronic structure calculations
- Role: process
- Action: Perform spin‑polarised DFT calculations for the optimised supercell using LSDA and LSDA+U (Ueff = 6 eV). Compute self‑consistent charge densities for both the weak‑field (S=5/2, high‑spin) and strong‑field (S=1/2, low‑spin) initial spin configurations. Obtain band structures, density of states, and total and site‑projected magnetic moments for all four cases: (U=0, weak), (U=0, strong), (U=6, weak), (U=6, strong).
- Evidence: `none`

### Step 3: Extract electronic properties
- Role: scored
- Action: From the computed band structures, extract the majority‑spin (E_g↑) and minority‑spin (E_g↓) energy gaps. Determine the spin splittings of the valence band (ΔE_v) and conduction band (ΔE_c). Compute the s‑d exchange parameter Nα and the p‑d exchange parameter Nβ using Nα = ΔE_c / (x⟨S⟩) and Nβ = ΔE_v / (x⟨S⟩), where x is the Mn concentration and ⟨S⟩ is the mean local spin. Report results for U = 0 eV and U = 6 eV.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: A JSON object with keys "U" (0 or 6), "E_g_up" (eV, float), "E_g_down" (eV, float), "delta_E_c" (meV, float), "delta_E_v" (meV, float), "N_alpha" (eV, float), "N_beta" (eV, float).
- Scoring: scored by hidden verifier

### Step 4: Extract magnetic moments
- Role: scored
- Action: Extract the total magnetic moment and the site‑projected moments on Mg, Mn, O, and the interstitial region from the self‑consistent calculations. Report values for U = 0 eV and U = 6 eV.
- Output file: `/app/outputs/magnetic_moments.json`
- Format: json
- Contract: A JSON object with keys "U" (0 or 6), "Total" (μB, float), "Mn" (μB, float), "O" (μB, float), "Interstitial" (μB, float). Note that the Mg moment is negligible; include "Mg" (μB, float) as well for completeness.
- Scoring: scored by hidden verifier

### Step 5: Calculate optical properties
- Role: process
- Action: Using the DFT wavefunctions and momentum matrix elements, compute the frequency‑dependent complex dielectric function ε(ω) = ε₁(ω) + iε₂(ω) for each of the four cases. Apply the Kramers‑Kronig relation to obtain ε₁(ω) from ε₂(ω). Derive the spin‑resolved absorption coefficient α(ω) from ε₁ and ε₂ via α(ω) = 2ω √[ (√(ε₁² − ε₂²) − ε₁) / 2 ].
- Evidence: `none`

### Step 6: Extract optical band gaps (load-bearing)
- Role: scored (load-bearing)
- Action: For each of the four configurations (U=0 weak, U=0 strong, U=6 weak, U=6 strong), construct spin‑resolved Tauc plots of (αhν)² vs photon energy hν. Obtain the optical band gap for spin‑up and spin‑down by linear extrapolation to zero. Compute the percentage reduction of the optical gap in the strong‑field case relative to weak‑field for each spin channel: reduction_up_U0, reduction_down_U0, reduction_up_U6, reduction_down_U6 (as percentages).
- Output file: `/app/outputs/optical_band_gaps.json`
- Format: json
- Contract: An array of case objects, each containing "U" (0 or 6), "ligand_field" ("weak" or "strong"), "E_g_up" (eV, float), "E_g_down" (eV, float). After the array, include a final object with keys "reduction_up_U0", "reduction_down_U0", "reduction_up_U6", "reduction_down_U6" (unit: %, float).
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/electronic_properties.json`
- `/app/outputs/magnetic_moments.json`
- `/app/outputs/optical_band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Spin‑resolved electronic band gaps, spin splittings, and s‑d/p‑d exchange parameters for U=0 and U=6 eV.
- schema:
  - `type`: object
  - `required`:
    - `U`: integer (0 or 6)
    - `E_g_up`: float (eV)
    - `E_g_down`: float (eV)
    - `delta_E_c`: float (meV)
    - `delta_E_v`: float (meV)
    - `N_alpha`: float (eV)
    - `N_beta`: float (eV)

### magnetic_moments.json
- path: `/app/outputs/magnetic_moments.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Total and site‑projected magnetic moments from LSDA and LSDA+U calculations.
- schema:
  - `type`: object
  - `required`:
    - `U`: integer (0 or 6)
    - `Total`: float (μB)
    - `Mg`: float (μB)
    - `Mn`: float (μB)
    - `O`: float (μB)
    - `Interstitial`: float (μB)

### optical_band_gaps.json
- path: `/app/outputs/optical_band_gaps.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Spin‑resolved optical band gaps from Tauc extrapolation and percentage reduction of the gap in the strong‑field case relative to weak‑field.
- schema:
  - `type`: array
  - `items`:
    - `U`: integer (0 or 6)
    - `ligand_field`: string ("weak" or "strong")
    - `E_g_up`: float (eV)
    - `E_g_down`: float (eV)
  - `final_object`:
    - `reduction_up_U0`: float (%)
    - `reduction_down_U0`: float (%)
    - `reduction_up_U6`: float (%)
    - `reduction_down_U6`: float (%)

Notes: All values must be in the specified units. The reductions are computed from the reported optical gaps. The verifier also checks internal consistency (optical gap ≥ electronic gap).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "U": "integer (0 or 6)",
          "E_g_up": "float (eV)",
          "E_g_down": "float (eV)",
          "delta_E_c": "float (meV)",
          "delta_E_v": "float (meV)",
          "N_alpha": "float (eV)",
          "N_beta": "float (eV)"
        }
      },
      "description": "Spin‑resolved electronic band gaps, spin splittings, and s‑d/p‑d exchange parameters for U=0 and U=6 eV."
    },
    {
      "file": "magnetic_moments.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "U": "integer (0 or 6)",
          "Total": "float (μB)",
          "Mg": "float (μB)",
          "Mn": "float (μB)",
          "O": "float (μB)",
          "Interstitial": "float (μB)"
        }
      },
      "description": "Total and site‑projected magnetic moments from LSDA and LSDA+U calculations."
    },
    {
      "file": "optical_band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "U": "integer (0 or 6)",
          "ligand_field": "string (\"weak\" or \"strong\")",
          "E_g_up": "float (eV)",
          "E_g_down": "float (eV)"
        },
        "final_object": {
          "reduction_up_U0": "float (%)",
          "reduction_down_U0": "float (%)",
          "reduction_up_U6": "float (%)",
          "reduction_down_U6": "float (%)"
        }
      },
      "description": "Spin‑resolved optical band gaps from Tauc extrapolation and percentage reduction of the gap in the strong‑field case relative to weak‑field."
    }
  ],
  "notes": "All values must be in the specified units. The reductions are computed from the reported optical gaps. The verifier also checks internal consistency (optical gap ≥ electronic gap)."
}
```

## How you are scored

A hidden verifier will read your submitted artifacts and compare each reported quantity against reference values (derived from the original study) with physically motivated tolerances. The three scored stages carry roughly equal weight: electronic properties, magnetic moments, and optical band gaps together define the main reproduction target. Partial credit is awarded; missing or malformed artifacts receive zero weight for that stage. The verifier recomputes the percentage reductions from your optical gaps and checks internal consistency (optical gap ≥ electronic gap). You must not simply look up and report the paper's numbers — honest computation is expected. The final reward is a weighted combination of the stage scores.
