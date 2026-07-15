# Rutile RuO2 optical properties from first-principles DFT

## Problem background
Rutile RuO₂ is a transition-metal dioxide with metallic conductivity and potential superhard characteristics. Its optical properties—such as the dielectric function, refractive index, and reflectivity—arise from electronic transitions between O 2p and Ru 4d states. Understanding these properties from first principles provides insight into the nature of the bonding and can inform potential applications in optoelectronics and protective coatings. This task targets a first-principles calculation of the linear optical response of rutile RuO₂ in the photon energy range 0–30 eV.

## Approach
The calculation is performed with plane-wave pseudopotential density functional theory (DFT). The exchange‑correlation functional is the GGA‑RPBE, and norm‑conserving pseudopotentials are used for Ru and O. After obtaining the self‑consistent ground‑state charge density and Kohn‑Sham wavefunctions, the frequency‑dependent dielectric function ε(ω)=ε₁(ω)+iε₂(ω) is computed for two orthogonal polarization directions: electric field perpendicular to the crystallographic c‑axis (E⊥c) and parallel to it (E//c). The imaginary part ε₂ is calculated from momentum matrix elements between valence and conduction bands; the real part ε₁ follows from the Kramers–Kronig transformation. From ε(ω) the refractive index n(ω), the extinction coefficient k(ω), and the reflectivity R(ω) are derived. The workflow delivers the static refractive indices n(0), the energy and magnitude of the principal peak in ε₂, and the full reflectivity spectrum up to 30 eV for both polarizations.

## Reproduction target
Run a DFT calculation for rutile RuO₂ (space group P4₂/mnm, lattice parameters a = 4.5149 Å, c = 3.1156 Å, internal parameter u = 0.3057) using GGA‑RPBE and norm‑conserving pseudopotentials. After the SCF step, compute the frequency‑dependent complex dielectric function ε(ω) for the two polarizations E⊥c and E//c from 0 to 30 eV. From ε(ω): (1) evaluate the static refractive indices n(0) for both polarizations; (2) locate the highest peak in ε₂(ω) for each polarization and record its energy (eV) and magnitude; (3) compute the reflectivity spectrum R(ω) for both polarizations over the same energy range and output it as a CSV. Place the extracted summary (static refractive indices and ε₂ peak parameters) in `/app/outputs/optical_summary.json` and the reflectivity data in `/app/outputs/reflectivity_spectrum.csv`.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for Ru and O: https://www.materialscloud.org/discover/sssp
- Rutile RuO2 crystal structure parameters

## Workflow steps

### Step 1: DFT SCF calculation
- Role: process
- Action: Run a DFT self-consistent field (SCF) calculation on rutile RuO2 using GGA-RPBE functional and norm-conserving pseudopotentials to obtain the ground-state charge density and Kohn-Sham wavefunctions. Use the provided crystal structure parameters (a=4.5149 Å, c=3.1156 Å, u=0.3057, space group P4_2/mnm).
- Evidence: `/app/outputs/scf_output.log`

### Step 2: Compute dielectric function ε(ω)
- Role: process
- Action: Using the wavefunctions and band energies from the SCF step, compute the imaginary part ε2(ω) from momentum matrix elements for polarizations E⊥c and E//c over 0–30 eV. Apply the Kramers–Kronig transformation to obtain the real part ε1(ω). Save the full ε1, ε2 data.
- Evidence: `/app/outputs/epsilon_data.csv`

### Step 3: Extract static refractive indices and ε2 peak parameters
- Role: scored (load-bearing)
- Action: From the dielectric function, compute the static refractive indices n(0) for both polarizations using n(0) = sqrt(ε1(0)). Locate the main (highest) peak in ε2 for each polarization: record its energy position (eV) and magnitude. Write these six values to optical_summary.json.
- Output file: `/app/outputs/optical_summary.json`
- Format: json
- Contract: {"n_perp": float, "n_par": float, "epsilon2_peak_perp_position_eV": float, "epsilon2_peak_perp_magnitude": float, "epsilon2_peak_par_position_eV": float, "epsilon2_peak_par_magnitude": float}
- Scoring: scored by hidden verifier

### Step 4: Compute reflectivity spectrum
- Role: scored
- Action: Using the dielectric function, compute the reflectivity R(ω) = |(1 - N(ω))/(1 + N(ω))|^2 with N^2 = ε1 + i ε2 for both polarizations and output the full spectrum from 0 to 30 eV as a CSV with columns energy_eV, R_perp, R_par.
- Output file: `/app/outputs/reflectivity_spectrum.csv`
- Format: csv
- Contract: columns: energy_eV (float), R_perp (float), R_par (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optical_summary.json`
- `/app/outputs/reflectivity_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optical_summary.json
- path: `/app/outputs/optical_summary.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static refractive indices, main ε2 peak parameters, and elastic constants (c11, c33, c44, c66, c12, c13, B0) for rutile RuO2; compared to paper-reported values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `n_perp`: float
    - `n_par`: float
    - `epsilon2_peak_perp_position_eV`: float
    - `epsilon2_peak_perp_magnitude`: float
    - `epsilon2_peak_par_position_eV`: float
    - `epsilon2_peak_par_magnitude`: float
    - `c11_GPa`: float
    - `c33_GPa`: float
    - `c44_GPa`: float
    - `c66_GPa`: float
    - `c12_GPa`: float
    - `c13_GPa`: float
    - `B0_GPa`: float

### reflectivity_spectrum.csv
- path: `/app/outputs/reflectivity_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reflectivity spectrum for structural checks (values in [0,1], qualitative shape consistency).
- schema:
  - `type`: table
  - `required_columns`: `energy_eV`, `R_perp`, `R_par`
  - `units`:
    - `energy_eV`: eV
    - `R_perp`: dimensionless
    - `R_par`: dimensionless

Notes: Optical and elastic properties combined into optical_summary.json; reflectivity_spectrum.csv is a low‑weight structural audit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optical_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "n_perp": "float",
          "n_par": "float",
          "epsilon2_peak_perp_position_eV": "float",
          "epsilon2_peak_perp_magnitude": "float",
          "epsilon2_peak_par_position_eV": "float",
          "epsilon2_peak_par_magnitude": "float",
          "c11_GPa": "float",
          "c33_GPa": "float",
          "c44_GPa": "float",
          "c66_GPa": "float",
          "c12_GPa": "float",
          "c13_GPa": "float",
          "B0_GPa": "float"
        }
      },
      "description": "Static refractive indices, main ε2 peak parameters, and elastic constants (c11, c33, c44, c66, c12, c13, B0) for rutile RuO2; compared to paper-reported values with tolerances."
    },
    {
      "file": "reflectivity_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_eV",
          "R_perp",
          "R_par"
        ],
        "units": {
          "energy_eV": "eV",
          "R_perp": "dimensionless",
          "R_par": "dimensionless"
        }
      },
      "description": "Reflectivity spectrum for structural checks (values in [0,1], qualitative shape consistency)."
    }
  ],
  "notes": "Optical and elastic properties combined into optical_summary.json; reflectivity_spectrum.csv is a low‑weight structural audit."
}
```

## How you are scored
A hidden verifier independently evaluates the artifacts you produce. The `optical_summary.json` is compared to hidden reference values for the static refractive indices and the ε₂ peak parameters; credit is awarded based on agreement within tolerances. The `reflectivity_spectrum.csv` is checked for structural correctness: all reflectivity values must lie between 0 and 1, the low‑energy spectrum should decrease monotonically, and a local minimum near 2.5 eV is expected. The final reward is a weighted combination of the scores on these artifacts. Simply reporting the target numbers without executing the workflow will not pass the verifier.
