# Monte Carlo simulation of electron beam lithography exposure in PMMA and ZEP resists

## Problem background
Electron beam lithography (EBL) uses focused electron beams to pattern nanoscale features in radiation-sensitive polymer resists. In positive-tone resists such as polymethylmethacrylate (PMMA) and the copolymer ZEP (a 1:1 copolymer of α‑chloromethacrylate and α‑methylstyrene), exposure causes main‑chain scission; the fragmented material is then dissolved in a developer. Understanding the three‑dimensional distribution of main‑chain scission probability is essential for predicting resist sensitivity, contrast, and line edge roughness at the nanoscale. This task implements a numerical model that directly computes main‑chain scission yields for PMMA and for two alternative exposure models of ZEP, enabling a quantitative comparison of their predicted sensitivity under identical electron beam exposure conditions.

## Approach
The simulation proceeds in two stages, combining a Monte Carlo electron‑transport model with a convolution‑based exposure pattern broadening.

**Stage 1 – Radial scission probability.** A Monte Carlo simulation tracks primary electrons and all generations of secondary electrons as they undergo elastic and inelastic collisions in a resist. Elastic scattering is described by a screened Rutherford cross section; inelastic collisions employ the Gryzinsky cross section. Electrons in the resist are categorised by shell and ionisation energy, with specific groups responsible for main‑chain scission. For PMMA, only collisions with valence electrons in main‑chain C‑C bonds produce scissions. For ZEP, two models are explored:

- **Model 1** assumes that inelastic collisions with valence electrons in the phenyl and chlorine side groups can also induce remote main‑chain scissions, yielding enhanced scission.
- **Model 2** assumes no such enhancement; only direct collisions with main‑chain C‑C bond electrons lead to scission, analogous to PMMA.

The resist parameters for inelastic collisions are listed below. The simulation is executed for point electron sources with initial energies of 3 keV, 10 keV, and 30 keV for each resist model (PMMA, ZEP Model 1, ZEP Model 2). The resulting radial distributions of the main‑chain scission probability per monomer, f(ρ,E), are saved as an npz archive.

**Stage 2 – Grating exposure convolution.** The radial scission probabilities are convolved with an elastic‑scattering broadening kernel and with the pattern of a 70 nm pitch grating. The kernel for a point source that has travelled a depth z before experiencing lateral coordinate ρ is

$$
P(z,\rho) = \frac{3\lambda}{z^3} \exp\!\left(-\frac{3\lambda\rho^2}{2z^3}\right),
$$

where λ is the elastic transport mean free path. The convolution yields the full three‑dimensional distribution of main‑chain scission yield per monomer for a 55 nm thick resist layer on a silicon substrate, from which scission yields at half‑depth are extracted.

---

### Resist parameters for inelastic collisions

**Table I – PMMA**

| Elementary collision process | Number of electrons per monomer, $k_i$ | Ionisation energy $U_i$ (eV) |
|-------------------------------|----------------------------------------|------------------------------|
| Oxygen core 1s electrons | 4 | 538 |
| Carbon core 1s electrons | 10 | 228 |
| Valence electrons in main‑chain C‑C bonds (scission) | 4 | 3.5 |
| Other valence electrons | 36 | 16.52 |

**Table II – ZEP Model 1**

| Elementary collision process | Number of electrons per monomer, $k_i$ | Ionisation energy $U_i$ (eV) |
|-------------------------------|----------------------------------------|------------------------------|
| Oxygen core 1s electrons | 4 | 538 |
| Carbon core 1s electrons | 26 | 228 |
| Chlorine core 1s electrons | 2 | 2808 |
| Chlorine core 2s electrons | 2 | 286 |
| Chlorine core 2p electrons | 6 | 219 |
| Valence electrons in main‑chain C‑C bonds (scission) | 8 | 3.5 |
| Valence electrons in side groups inducing remote scissions | 38 | 3.5 |
| Other valence electrons | 40 | 16 |

**Table III – ZEP Model 2**

| Elementary collision process | Number of electrons per monomer, $k_i$ | Ionisation energy $U_i$ (eV) |
|-------------------------------|----------------------------------------|------------------------------|
| Oxygen core 1s electrons | 4 | 538 |
| Carbon core 1s electrons | 26 | 228 |
| Chlorine core 1s electrons | 2 | 2808 |
| Chlorine core 2s electrons | 2 | 286 |
| Chlorine core 2p electrons | 6 | 219 |
| Valence electrons in main‑chain C‑C bonds (scission) | 8 | 3.5 |
| Other valence electrons | 78 | 16 |

For elastic scattering, use the resist density, composition, and appropriate values of the elastic transport mean free path λ (e.g., from Liljequist *et al.*, J. Appl. Phys. **65**, 2431, 1989).

## Reproduction target
Implement the Monte Carlo simulation and the convolution procedure described above. Using the radial scission distributions obtained in the first stage, compute the three‑dimensional main‑chain scission yield per monomer for a 70 nm‑pitch grating exposure on a 55 nm thick resist layer on a silicon substrate. Perform the computation for PMMA, ZEP Model 1, and ZEP Model 2 at electron‑beam energies of 3 keV, 10 keV, and 30 keV. Use the following doses: 40 pC/cm at 3 keV, 90 pC/cm at 10 keV, and 350 pC/cm at 30 keV. For each condition extract the scission yield at the half‑depth of the resist:
- at the centre of a line (ρ = 0)
- at the edge of a line (ρ = 35 nm).

For the two ZEP models, also compute the ratio ZEP Model 1 / ZEP Model 2 at each of these positions. Store all results in `/app/outputs/scission_yields.json` following the structure described in the workflow steps.

## Assets

- Python 3 scientific computing environment: python

## Workflow steps

### Step 1: Monte Carlo simulation of electron transport and scission probability
- Role: process
- Action: Implement a Monte Carlo electron transport simulation for PMMA and ZEP resists using screened Rutherford elastic cross section and Gryzinsky inelastic cross section, with resist parameters from provided tables. For point electron sources at energies 3 keV, 10 keV, and 30 keV, simulate primary and secondary cascades to compute the radial distribution of main-chain scission probability per monomer f(ρ,E) for each resist model (PMMA, ZEP Model 1, ZEP Model 2). Save the radial functions to an npz archive.
- Evidence: `/app/outputs/radial_scission_functions.npz`

### Step 2: Compute grating exposure scission yields
- Role: scored (load-bearing)
- Action: Using the radial scission probability distributions from the previous step, convolve with the elastic scattering broadening kernel and the grating exposure pattern (70 nm pitch, 55 nm thick resist on Si) to obtain the 3D distribution of main-chain scission yield per monomer. At energies 3 keV (dose 40 pC/cm), 10 keV (dose 90 pC/cm), and 30 keV (dose 350 pC/cm), extract the yield at half-depth at the line center (ρ=0) and line edge (ρ=35 nm) for PMMA, ZEP Model 1, and ZEP Model 2. Also compute the ratio ZEP-1/ZEP-2 at these positions. Output the results in scission_yields.json.
- Output file: `/app/outputs/scission_yields.json`
- Format: json
- Contract: JSON object with key 'yields' (array of objects: {resist, voltage_keV, dose_pC_per_cm, position, scission_yield}) and key 'ratios' (array of objects: {voltage_keV, position, ratio}).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scission_yields.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scission_yields.json
- path: `/app/outputs/scission_yields.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scission yields at half-depth of 55 nm resist for 70 nm pitch grating at center and edge; doses: 3 keV/40 pC/cm, 10 keV/90 pC/cm, 30 keV/350 pC/cm.
- schema:
  - `type`: object
  - `required`: `yields`, `ratios`
  - `yields`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `resist`, `voltage_keV`, `dose_pC_per_cm`, `position`, `scission_yield`
      - `properties`:
        - `resist`:
          - `type`: string
        - `voltage_keV`:
          - `type`: integer
        - `dose_pC_per_cm`:
          - `type`: number
        - `position`:
          - `type`: string
          - `enum`: `center`, `edge`
        - `scission_yield`:
          - `type`: number
  - `ratios`:
    - `type`: array
    - `items`:
      - `type`: object
      - `required`: `voltage_keV`, `position`, `ratio`
      - `properties`:
        - `voltage_keV`:
          - `type`: integer
        - `position`:
          - `type`: string
          - `enum`: `center`, `edge`
        - `ratio`:
          - `type`: number

Notes: Only the specified energies, doses, and positions are scored. The yields are dimensionless scissions per monomer. The ratio ZEP-1/ZEP-2 is also provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scission_yields.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "yields",
          "ratios"
        ],
        "yields": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "resist",
              "voltage_keV",
              "dose_pC_per_cm",
              "position",
              "scission_yield"
            ],
            "properties": {
              "resist": {
                "type": "string"
              },
              "voltage_keV": {
                "type": "integer"
              },
              "dose_pC_per_cm": {
                "type": "number"
              },
              "position": {
                "type": "string",
                "enum": [
                  "center",
                  "edge"
                ]
              },
              "scission_yield": {
                "type": "number"
              }
            }
          }
        },
        "ratios": {
          "type": "array",
          "items": {
            "type": "object",
            "required": [
              "voltage_keV",
              "position",
              "ratio"
            ],
            "properties": {
              "voltage_keV": {
                "type": "integer"
              },
              "position": {
                "type": "string",
                "enum": [
                  "center",
                  "edge"
                ]
              },
              "ratio": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Scission yields at half-depth of 55 nm resist for 70 nm pitch grating at center and edge; doses: 3 keV/40 pC/cm, 10 keV/90 pC/cm, 30 keV/350 pC/cm."
    }
  ],
  "notes": "Only the specified energies, doses, and positions are scored. The yields are dimensionless scissions per monomer. The ratio ZEP-1/ZEP-2 is also provided."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier that reads `scission_yields.json`. The verifier compares the yields and ratios you report against hidden reference values obtained from the original study, allowing for the spread that is natural when a complex Monte Carlo simulation is re‑implemented independently. In addition, the verifier checks that the relative ordering of the scission yields across the three resist models follows the physically expected trend for each exposure condition. The final reward is a weighted combination of the agreement with the reference values and the ordering checks; the majority of the score comes from the main‑chain scission yields.
