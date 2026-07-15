# Optical absorption in doped InAs substrates

## Problem background
The mid‑infrared band (3–5 μm) is important for gas spectroscopy, stand‑off explosive detection, and medical diagnostics. Light‑emitting diode (LED) heterostructures with an indium arsenide (InAs) active layer are promising sources in this range. The optical absorption of the heavily doped n‑type InAs substrate plays a key role: it modifies the electroluminescence spectrum that reaches the detector, making it essential to quantify how absorption varies with doping and photon energy. This task investigates the doping‑dependent optical absorption of InAs substrates by implementing a semi‑analytical absorption model.

## Approach
The absorption coefficient α(ω) is obtained from the imaginary part of the dielectric permittivity χ″(ω,0). The model separately considers transitions that involve heavy holes and light holes, with the occupation of electronic states governed by Fermi–Dirac statistics. The permittivity is converted to absorption using the relation α = (ω/(c√χ∞)) χ″, where χ∞ is the high‑frequency permittivity and c is the speed of light. All material parameters for InAs (electron effective mass, hole masses, bandgap at 300 K, permittivity, etc.) are taken from the public Vurgaftman–Meyer–Ram‑Mohan compilation. The calculation is carried out for two free‑electron concentrations, n = 2×10¹⁸ cm⁻³ and n = 5×10¹⁸ cm⁻³, at room temperature (T = 300 K), over a photon energy range from approximately 0.3 eV to 0.6 eV. The absorption edge is operationally defined as the photon energy where α reaches 100 cm⁻¹.

## Reproduction target
Compute the absorption coefficient α(ω) of n‑type InAs substrates for the two doping levels given above, on a dense grid of photon energies between 0.3 eV and 0.6 eV, and save the resulting spectra as `absorption_spectra.csv`. Then, from those spectra, faithfully extract the photon energies where the absorption coefficient equals 100 cm⁻¹ for each doping level and store them in `absorption_edges.json`. The target is to produce physically correct absorption curves and edge energies that reflect the behavior of degenerate InAs.

## Assets

- InAs material parameters (Vurgaftman, Meyer, Ram-Mohan 2001): 10.1063/1.1368156

## Workflow steps

### Step 1: Calculate absorption spectra
- Role: scored (load-bearing)
- Action: Implement the analytical permittivity model χ″(ω,0) and the absorption-coefficient relation α = (ω/(c√χ∞))χ″ as described in the paper, using InAs material parameters from the Vurgaftman compilation. Compute the absorption coefficient α(ω) over photon energies from 0.3 eV to 0.6 eV for electron densities n = 2×10^18 cm⁻³ and n = 5×10^18 cm⁻³ at T = 300 K. Save the resulting curves as a CSV file.
- Output file: `/app/outputs/absorption_spectra.csv`
- Format: csv
- Contract: CSV with columns: photon_energy_eV (float, photon energy in eV), alpha_n2e18_cm_minus1 (float, absorption coefficient in cm⁻¹ for n=2×10^18 cm⁻³), alpha_n5e18_cm_minus1 (float, absorption coefficient in cm⁻¹ for n=5×10^18 cm⁻³).
- Scoring: scored by hidden verifier

### Step 2: Determine absorption edges
- Role: scored
- Action: From absorption_spectra.csv, interpolate to find the photon energies where the absorption coefficient equals 100 cm⁻¹ for both doping levels. Save the two edge energies as a JSON file.
- Output file: `/app/outputs/absorption_edges.json`
- Format: json
- Contract: JSON object with keys: n2e18_edge_eV (float, edge energy for n=2×10^18 cm⁻³) and n5e18_edge_eV (float, edge energy for n=5×10^18 cm⁻³).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_spectra.csv`
- `/app/outputs/absorption_edges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_spectra.csv
- path: `/app/outputs/absorption_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed absorption coefficient α(ω) of InAs substrates at T=300 K as a function of photon energy for electron densities 2×10^18 cm⁻³ and 5×10^18 cm⁻³.
- schema:
  - `type`: table
  - `required_columns`: `photon_energy_eV`, `alpha_n2e18_cm_minus1`, `alpha_n5e18_cm_minus1`
  - `units`:
    - `photon_energy_eV`: eV
    - `alpha_n2e18_cm_minus1`: cm^-1
    - `alpha_n5e18_cm_minus1`: cm^-1

### absorption_edges.json
- path: `/app/outputs/absorption_edges.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Photon energies at which the absorption coefficient equals 100 cm⁻¹ for each doping level, extracted from the CSV.
- schema:
  - `type`: object
  - `required`: `n2e18_edge_eV`, `n5e18_edge_eV`
  - `properties`:
    - `n2e18_edge_eV`:
      - `type`: number
      - `unit`: eV
    - `n5e18_edge_eV`:
      - `type`: number
      - `unit`: eV

Notes: The checker will recompute absorption edge energies from absorption_spectra.csv, compare them to hidden gold values (±5 meV), and verify the Moss–Burstein shift (edge for n=5×10^18 > n=2×10^18 by ≥5 meV). The absorption_edges.json values are checked for consistency with the CSV-based recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "photon_energy_eV",
          "alpha_n2e18_cm_minus1",
          "alpha_n5e18_cm_minus1"
        ],
        "units": {
          "photon_energy_eV": "eV",
          "alpha_n2e18_cm_minus1": "cm^-1",
          "alpha_n5e18_cm_minus1": "cm^-1"
        }
      },
      "description": "Computed absorption coefficient α(ω) of InAs substrates at T=300 K as a function of photon energy for electron densities 2×10^18 cm⁻³ and 5×10^18 cm⁻³."
    },
    {
      "file": "absorption_edges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "n2e18_edge_eV",
          "n5e18_edge_eV"
        ],
        "properties": {
          "n2e18_edge_eV": {
            "type": "number",
            "unit": "eV"
          },
          "n5e18_edge_eV": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Photon energies at which the absorption coefficient equals 100 cm⁻¹ for each doping level, extracted from the CSV."
    }
  ],
  "notes": "The checker will recompute absorption edge energies from absorption_spectra.csv, compare them to hidden gold values (±5 meV), and verify the Moss–Burstein shift (edge for n=5×10^18 > n=2×10^18 by ≥5 meV). The absorption_edges.json values are checked for consistency with the CSV-based recomputation."
}
```

## How you are scored
A hidden verifier inspects your submitted artifacts. It independently recomputes the absorption edge energies from `absorption_spectra.csv` (by interpolation at the α = 100 cm⁻¹ level) and checks that the absorption coefficient is non‑negative and physically reasonable. It reads `absorption_edges.json` and verifies that the reported edge energies are consistent with the values derived from the CSV. In addition, the verifier examines whether the two edge energies (one for each doping level) follow the qualitative trend expected from the physics of heavily doped semiconductors. Each step contributes to the final score, with the primary weight on the correctness of the absorption curves and the derived edge energies. You do not need to match any pre‑fixed number, but your results must be physically sound, internally consistent, and obtained from a faithful implementation of the described model.
