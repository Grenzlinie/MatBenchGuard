# DFT Adsorption and Separation of Gas Molecules on Doped g-C3N4 (001)

## Problem background
During the exploitation of acid gas reservoirs, gas mixtures containing hydrogen sulfide (H₂S), carbon dioxide (CO₂), and water vapour (H₂O) are commonly produced, requiring efficient separation for further processing and environmental protection. The s-triazine-based graphitic carbon nitride (g-C₃N₄) monolayer is a two-dimensional material with potential for gas capture and catalytic applications, but its pristine surface interacts weakly with these gas molecules. This work investigates whether doping the surface with group VIB transition metals (Cr, Mo, W) and applying external electric fields can modify the adsorption behaviour of H₂S, CO₂, and H₂O, aiming to achieve selective separation of these gases.

## Approach
We use density functional theory (DFT) calculations with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and Grimme D2 dispersion correction to model a 3×3 supercell of the s-triazine g-C₃N₄(001) monolayer with a vacuum gap of 15 Å. First, we compute the electronic and energetic properties of the pristine slab and determine the most stable adsorption configurations for H₂O, H₂S, and CO₂ by testing multiple adsorption sites and molecular orientations. Next, we introduce a single transition metal atom (Cr, Mo, or W) at the most favourable hollow site, re-optimize the doped slab, and evaluate the adsorption of the same three gases on each doped surface. Finally, we apply an external electric field perpendicular to the surface (pointing outward) at strengths of 0.002, 0.004, and 0.006 a.u., and recompute the adsorption energies and charge transfers to investigate how the field affects the separation trends among the three gases.

## Reproduction target
Perform the DFT calculations described above and report the computed numerical quantities in three structured JSON files. Specifically:
- For the pristine surface: band gap (after applying a 1.3 eV scissors correction) and total energy of the optimized slab; for each gas molecule (H₂O, H₂S, CO₂), the most stable adsorption configuration (site), adsorption energy, Mulliken charge transfer, and internal bond lengths and bond angle.
- For each doped surface (Cr, Mo, W): band gap and total energy; and for each gas molecule on each doped surface, the same adsorption properties as above.
- For each combination of dopant (Cr, Mo, W), molecule, and electric field strength (0.002, 0.004, 0.006 a.u.): the adsorption energy and Mulliken charge transfer.
All values must be output following the exact JSON schemas provided in the workflow steps. The relative ordering of adsorption energies across gases and the effect of electric field on these energies and charge transfers will be verified against physical expectations.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (standard solid-state pseudopotentials library): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Pristine g-C3N4 slab and gas adsorption
- Role: scored
- Action: Build a 3×3 supercell of s-triazine g-C3N4(001) monolayer with a 15 Å vacuum layer. Optimize the slab geometry using DFT (PBE functional with Grimme D2 dispersion correction, plane-wave basis, k-point sampling). Compute its band gap (corrected with a scissors shift of 1.3 eV) and total energy. Then, for each gas molecule (H2O, H2S, CO2), sample three adsorption sites (including the hollow c site) and two orientations (horizontal h and vertical v). For each configuration, perform geometry optimization; compute the adsorption energy (ΔE_ads = E_slab+gas − E_slab − E_gas), Mulliken charge transfer (from slab to molecule, negative for electron acceptor), and the internal bond lengths and bond angle. Identify the most stable configuration (most negative ΔE_ads) for each molecule and report its site, ΔE_ads, charge transfer, bond lengths, and bond angle.
- Output file: `/app/outputs/pristine_results.json`
- Format: json
- Contract: {"pristine_slab": {"band_gap_eV": float, "total_energy_eV": float}, "adsorption": [{"molecule": "H2O|H2S|CO2", "site": "string (e.g., c-h, c-v)", "E_ads_eV": float, "delta_Q_e": float, "bond_lengths_ang": [float, float], "bond_angle_deg": float}]}
- Scoring: scored by hidden verifier

### Step 2: VIB doped g-C3N4 surfaces and adsorption
- Role: scored
- Action: Place a single transition metal atom (Cr, Mo, or W) at the most favorable hollow site of the pristine slab and re-optimize the doped slab geometry. Compute the band gap and total energy for each doped surface (Cr/g-C3N4, Mo/g-C3N4, W/g-C3N4). Then, for each doped surface, determine the most stable adsorption configuration of H2O, H2S, and CO2 using the same approach as step_01 (sample relevant sites/orientations, optimize geometry, compute adsorption energy, Mulliken charge transfer, and internal bond lengths and bond angle).
- Output file: `/app/outputs/doped_results.json`
- Format: json
- Contract: {"doped_slabs": [{"dopant": "Cr|Mo|W", "band_gap_eV": float, "total_energy_eV": float}], "adsorption": [{"dopant": "Cr|Mo|W", "molecule": "H2O|H2S|CO2", "site": "string", "E_ads_eV": float, "delta_Q_e": float, "bond_lengths_ang": [float, float], "bond_angle_deg": float}]}
- Scoring: scored by hidden verifier

### Step 3: Electric field effect on adsorption
- Role: scored (load-bearing)
- Action: For each combination of dopant (Cr, Mo, W) and gas molecule (H2O, H2S, CO2), apply an external electric field perpendicular to the slab surface (pointing outward) at strengths 0.002, 0.004, and 0.006 a.u. Re-optimize the adsorption structure under each field and compute the adsorption energy and Mulliken charge transfer.
- Output file: `/app/outputs/field_results.json`
- Format: json
- Contract: {"electric_field_adsorption": [{"dopant": "Cr|Mo|W", "molecule": "H2O|H2S|CO2", "field_strength": 0.002|0.004|0.006, "E_ads_eV": float, "delta_Q_e": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_results.json`
- `/app/outputs/doped_results.json`
- `/app/outputs/field_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_results.json
- path: `/app/outputs/pristine_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized pristine slab properties and the most stable adsorption configurations for H2O, H2S, CO2 on pristine g-C3N4. All numeric entries are compared to the paper's Table 1.
- schema:
  - `type`: object
  - `required`:
    - `pristine_slab`:
      - `band_gap_eV`: float
      - `total_energy_eV`: float
  - `items`:
    - `adsorption`:
      - `molecule`: string
      - `site`: string
      - `E_ads_eV`: float
      - `delta_Q_e`: float
      - `bond_lengths_ang`: `float`, `float`
      - `bond_angle_deg`: float

### doped_results.json
- path: `/app/outputs/doped_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps and total energies of Cr, Mo, W doped g-C3N4, and the most stable adsorption configurations for each gas on each doped surface. Numeric values are compared to the paper's Table 2.
- schema:
  - `type`: object
  - `required`:
    - `doped_slabs`:
      - `dopant`: string
      - `band_gap_eV`: float
      - `total_energy_eV`: float
  - `items`:
    - `adsorption`:
      - `dopant`: string
      - `molecule`: string
      - `site`: string
      - `E_ads_eV`: float
      - `delta_Q_e`: float
      - `bond_lengths_ang`: `float`, `float`
      - `bond_angle_deg`: float

### field_results.json
- path: `/app/outputs/field_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies and charge transfers under electric fields (0.002–0.006 a.u.) for each dopant/gas combination. Values are compared to the paper's Figs. 6 and 7.
- schema:
  - `type`: object
  - `required`:
    - `electric_field_adsorption`:
      - `dopant`: string
      - `molecule`: string
      - `field_strength`: float
      - `E_ads_eV`: float
      - `delta_Q_e`: float

Notes: The band gap must be reported after applying the 1.3 eV scissors correction. Charge analysis method may differ from DMol3's Mulliken, so tolerances are set to accommodate typical variation. Thermodynamic properties (S, Cp, H, G) are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pristine_slab": {
            "band_gap_eV": "float",
            "total_energy_eV": "float"
          }
        },
        "items": {
          "adsorption": [
            {
              "molecule": "string",
              "site": "string",
              "E_ads_eV": "float",
              "delta_Q_e": "float",
              "bond_lengths_ang": [
                "float",
                "float"
              ],
              "bond_angle_deg": "float"
            }
          ]
        }
      },
      "description": "Optimized pristine slab properties and the most stable adsorption configurations for H2O, H2S, CO2 on pristine g-C3N4. All numeric entries are compared to the paper's Table 1."
    },
    {
      "file": "doped_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "doped_slabs": [
            {
              "dopant": "string",
              "band_gap_eV": "float",
              "total_energy_eV": "float"
            }
          ]
        },
        "items": {
          "adsorption": [
            {
              "dopant": "string",
              "molecule": "string",
              "site": "string",
              "E_ads_eV": "float",
              "delta_Q_e": "float",
              "bond_lengths_ang": [
                "float",
                "float"
              ],
              "bond_angle_deg": "float"
            }
          ]
        }
      },
      "description": "Band gaps and total energies of Cr, Mo, W doped g-C3N4, and the most stable adsorption configurations for each gas on each doped surface. Numeric values are compared to the paper's Table 2."
    },
    {
      "file": "field_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "electric_field_adsorption": [
            {
              "dopant": "string",
              "molecule": "string",
              "field_strength": "float",
              "E_ads_eV": "float",
              "delta_Q_e": "float"
            }
          ]
        }
      },
      "description": "Adsorption energies and charge transfers under electric fields (0.002–0.006 a.u.) for each dopant/gas combination. Values are compared to the paper's Figs. 6 and 7."
    }
  ],
  "notes": "The band gap must be reported after applying the 1.3 eV scissors correction. Charge analysis method may differ from DMol3's Mulliken, so tolerances are set to accommodate typical variation. Thermodynamic properties (S, Cp, H, G) are not required."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the three JSON output files. For each stage, the verifier compares your reported numerical values (adsorption energies, charge transfers, bond lengths/angles, band gaps) against reference values computed for the same protocol. Absolute tolerances are applied to accommodate legitimate variations due to implementation choices (e.g., pseudopotentials, basis set) while rejecting answers that deviate significantly from the expected physical result. Additionally, the verifier checks key structural relationships: for example, the relative ordering of adsorption energies across gases, the monotonic change of adsorption energies and charge transfers with respect to electric field strength, and specific differences between doped surfaces. Points are awarded proportionally for values within tolerance and for correct trends. The final reward is a weighted combination of the stage scores, with the electric field stage carrying the highest weight because it is sensitive to the accuracy of the entire workflow and cannot be obtained without genuinely running the simulations.
