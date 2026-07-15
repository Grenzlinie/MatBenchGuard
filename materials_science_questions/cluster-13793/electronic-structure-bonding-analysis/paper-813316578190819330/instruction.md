# Macroscopic Transverse Effective Charges and Force Constants in LiZnP

## Problem background
LiZnP is a filled tetrahedral semiconductor with the antifluorite structure (space group \(F\overline{4}3m\)). The crystal lacks inversion symmetry, so the zone-centre longitudinal-optical (LO) and transverse-optical (TO) phonon modes are non-degenerate for each cation–anion pair. Raman scattering accesses these modes, and their frequencies can be used to quantify bonding character via the macroscopic transverse effective charge \(e_T^*\) and the force constant \(C\) of the nearest-neighbor bonds. Two distinct cation–anion bonds exist in this compound: Li–P and Zn–P. Computing \(e_T^*\) and \(C\) for each bond from the measured phonon frequencies and known crystal/dielectric constants provides the numerical basis for comparing the ionicity and covalency of the Li–P and Zn–P bonds.

## Approach
The equations that relate phonon frequencies to effective charges and force constants are given in CGS-ESU units.  For a zinc-blende-type material, the long-wavelength splitting of the LO and TO phonon branches is related to the macroscopic transverse effective charge by

\[e_T^{*2} = \frac{\varepsilon_\infty a_0^3 \mu}{16\pi}\left(\Omega_{\mathrm{LO}}^2 - \Omega_{\mathrm{TO}}^2\right)\]

where \(\varepsilon_\infty\) is the optical dielectric constant (dimensionless), \(a_0\) the cubic lattice constant, \(\mu\) the reduced mass of the cation–anion pair, and \(\Omega_{\mathrm{LO}}\), \(\Omega_{\mathrm{TO}}\) the LO and TO **angular** frequencies (rad s⁻¹).  The phonon frequencies reported in the paper and provided below are **wavenumbers** \(\nu\) in cm⁻¹.  To use the above formula you must convert them to angular frequencies:

\[\Omega = 2\pi c \nu, \qquad c = 2.99792458\times 10^{10}\ \mathrm{cm\,s^{-1}}.\]

The lattice constant is given in Å; convert to cm with \(1\ \mathrm{Å} = 10^{-8}\ \mathrm{cm}\).  Reduced masses are given in atomic mass units (u); convert to grams via \(1\ \mathrm{u} = 1.66053906660\times 10^{-24}\ \mathrm{g}\).  The result of Eq. (1) is the squared effective charge in **esu²**; convert \(e_T^*\) to elementary charge (\(e\)) by dividing by the esu value of the electron charge:

\[e = 4.8032047\times 10^{-10}\ \mathrm{esu}.\]

The same harmonic-oscillator model gives the angular TO frequency as \(\Omega_{\mathrm{TO}} = \sqrt{C/\mu}\), where \(C\) is the force constant.  Therefore

\[C = \mu\,\Omega_{\mathrm{TO}}^2 \quad(\mathrm{dyn\,cm^{-1}}),\]

using \(\mu\) in g and \(\Omega_{\mathrm{TO}} = 2\pi c\,\nu_{\mathrm{TO}}\) with \(\nu_{\mathrm{TO}}\) in cm⁻¹.

All necessary input constants are numeric values stated below.  The computation is deterministic and can be carried out in a short script.

## Reproduction target
Compute the macroscopic transverse effective charges \(e_T^*\) (in units of elementary charge) for the Li–P and Zn–P pairs, and the force constants \(C\) (in dyn/cm) for the same pairs, using the following inputs:

- Lattice constant: \(a_0 = 5.765\ \text{Å}\)
- Optical dielectric constant: \(\varepsilon_\infty = 9.6\)
- Reduced masses: \(\mu_{\mathrm{LiP}} = 5.7\ \mathrm{u}\), \(\mu_{\mathrm{ZnP}} = 21.0\ \mathrm{u}\)
- Phonon frequencies (Li–P): \(\omega_{\mathrm{LO1}} = 421\ \mathrm{cm}^{-1}\), \(\omega_{\mathrm{TO1}} = 363\ \mathrm{cm}^{-1}\)
- Phonon frequencies (Zn–P): \(\omega_{\mathrm{LO2}} = 265\ \mathrm{cm}^{-1}\), \(\omega_{\mathrm{TO2}} = 230\ \mathrm{cm}^{-1}\)

Write the four results into the output file `/app/outputs/results.json`.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute Effective Charges and Force Constants
- Role: scored (load-bearing)
- Action: First, convert all inputs to CGS-ESU units: a0 from Å to cm (×10⁻⁸), each reduced mass μ from u to g (×1.66053906660×10⁻²⁴), each phonon wavenumber ν (cm⁻¹) to angular frequency Ω = 2πc ν with c = 2.99792458×10¹⁰ cm s⁻¹. Then compute the squared effective charge in esu² using Eq. (1): e_T*² = (ε∞ a0³ μ / (16π)) (Ω_LO² – Ω_TO²). Take the square root and convert e_T* to elementary charge by dividing by e = 4.8032047×10⁻¹⁰ esu. Compute the force constant C = μ Ω_TO² for each bond; the result is in dyn cm⁻¹. Write the four numeric results (e_T*_LiP, e_T*_ZnP, C_LiP, C_ZnP) into /app/outputs/results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"type": "object", "required": ["eT_star_LiP", "eT_star_ZnP", "C_LiP_dyn_per_cm", "C_ZnP_dyn_per_cm"], "properties": {"eT_star_LiP": {"type": "number", "unit": "elementary charge"}, "eT_star_ZnP": {"type": "number", "unit": "elementary charge"}, "C_LiP_dyn_per_cm": {"type": "number", "unit": "dyn/cm"}, "C_ZnP_dyn_per_cm": {"type": "number", "unit": "dyn/cm"}}}
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
- description: Macroscopic transverse effective charges (in units of elementary charge) and force constants (in dyn/cm) for Li-P and Zn-P bonds, computed from the given analytical relations and input constants.
- schema:
  - `type`: object
  - `required`: `eT_star_LiP`, `eT_star_ZnP`, `C_LiP_dyn_per_cm`, `C_ZnP_dyn_per_cm`
  - `properties`:
    - `eT_star_LiP`:
      - `type`: number
      - `unit`: elementary charge
    - `eT_star_ZnP`:
      - `type`: number
      - `unit`: elementary charge
    - `C_LiP_dyn_per_cm`:
      - `type`: number
      - `unit`: dyn/cm
    - `C_ZnP_dyn_per_cm`:
      - `type`: number
      - `unit`: dyn/cm

Notes: All inputs are deterministic numeric constants provided in the task instruction. Unit conversions (cm/Å, g/u, cm⁻¹→rad/s, esu→e) are now explicitly given, making the target values reachable without guessing implicit conventions.

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
          "eT_star_LiP",
          "eT_star_ZnP",
          "C_LiP_dyn_per_cm",
          "C_ZnP_dyn_per_cm"
        ],
        "properties": {
          "eT_star_LiP": {
            "type": "number",
            "unit": "elementary charge"
          },
          "eT_star_ZnP": {
            "type": "number",
            "unit": "elementary charge"
          },
          "C_LiP_dyn_per_cm": {
            "type": "number",
            "unit": "dyn/cm"
          },
          "C_ZnP_dyn_per_cm": {
            "type": "number",
            "unit": "dyn/cm"
          }
        }
      },
      "description": "Macroscopic transverse effective charges (in units of elementary charge) and force constants (in dyn/cm) for Li-P and Zn-P bonds, computed from the given analytical relations and input constants."
    }
  ],
  "notes": "All inputs are deterministic numeric constants provided in the task instruction. Unit conversions (cm/Å, g/u, cm⁻¹→rad/s, esu→e) are now explicitly given, making the target values reachable without guessing implicit conventions."
}
```

## How you are scored
A hidden verifier inspects your `results.json` and compares the four numeric fields against a reference that was derived from the same inputs using the same formulas.  Each field is compared with a tolerance appropriate for this deterministic numerical calculation.  The overall reward (a float between 0 and 1) is a weighted combination of the per-field scores.  Simply self-reporting numbers that match the reference is not sufficient; the verifier expects the output to be generated by your own computation from the given inputs.
