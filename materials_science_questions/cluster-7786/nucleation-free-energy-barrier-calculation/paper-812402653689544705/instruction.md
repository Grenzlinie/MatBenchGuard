# Orientation-resolved α Coefficients for Solid-Liquid Interfaces

## Problem background
The solid-liquid interfacial free energy γ determines crystal nucleation rates and growth morphologies. Predicting γ as a function of crystal structure, orientation, and temperature is a central challenge. One theoretical approach uses a broken-bond model modified to account for the entropy loss of the liquid near the crystal surface. At the melting temperature T = Tₘ the model expresses γ in terms of a dimensionless coefficient α, where

  γ = α · ℋₘ / (N₀¹ᐟ³ v²ᐟ³),

with ℋₘ the molar melting enthalpy, N₀ Avogadro's number, and v the molar volume. The coefficient α depends on the lattice type, the crystallographic orientation of the interface, and the temperature. This task aims to compute the orientation-resolved α statistics for five common crystal structures at the melting point using the broken-bond theory with Turnbull's thermodynamic approximations.

## Approach
The method is a broken‑bond theory: the interfacial free energy γ is expressed as the product of the number of solid‑liquid nearest‑neighbour bonds per unit area on a crystal plane (nₕₖₗ) and a formal bond free energy g_SL that includes an entropy contribution. The bond densities nₕₖₗ are obtained from the analytical formulas of Wolff and Gualtieri for f.c.c., h.c.p., b.c.c., diamond cubic, and simple cubic lattices. At the melting point Tₘ we approximate the molar enthalpy difference ΔH ≈ ℋₘ and the molar entropy difference ΔS ≈ ℋₘ/Tₘ (Turnbull's approximations), which together give the bond free energy g_SL. For each structure we sample a set of crystallographic orientations, compute nₕₖₗ, then the corresponding α = γ · (N₀¹ᐟ³ v²ᐟ³) / ℋₘ. From the orientation‑resolved α values we extract per structure the minimum (α_min), maximum (α_max), and, where possible, the arithmetic mean over orientations (α_a). For h.c.p. the average is not computed.

## Reproduction target
Compute, for planar solid‑liquid interfaces of f.c.c., h.c.p., b.c.c., diamond, and simple cubic structures at the melting point T = Tₘ, the orientation‑resolved dimensionless coefficient α statistics:
- α_min (minimum value over sampled orientations),
- α_max (maximum value),
- α_a (arithmetic mean of α over orientations; omit for h.c.p. – report null).
Write the results into `/app/outputs/alpha_values.json` as an array of five objects, each with keys `structure` (string: `'fcc'`,`'hcp'`,`'bcc'`,`'diamond'`,`'sc'`), `alpha_min` (float), `alpha_max` (float), and `alpha_avg` (float or `null`). The workflow must produce the bond densities as an intermediate step (evidence in `bond_densities.csv`) before computing the α values.

## Assets

- Wolff and Gualtieri (1962) – Bond density formulas for crystal surfaces: https://pubs.geoscienceworld.org/ammin/article/47/5-6/562/540045

## Workflow steps

### Step 1: Compute bond densities n_hkl
- Role: process
- Action: For each of the five crystal structures (fcc, hcp, bcc, diamond, sc), compute the solid-liquid nearest-neighbour bond density n_{hkl} for a representative set of crystallographic orientations using the Wolff–Gualtieri formulas (Am. Miner. 47 (1962) 562). Store the computed n_{hkl} values for later use.
- Evidence: `/app/outputs/bond_densities.csv`

### Step 2: Compute orientation-resolved α coefficients
- Role: scored (load-bearing)
- Action: Using the bond densities from the previous step, compute the interfacial free energy γ for planar surfaces at the melting point Tₘ using Turnbull's thermodynamic approximations (ΔH ≈ ℋₘ, ΔS ≈ ℋₘ/Tₘ) and the broken-bond model. Express γ as γ = α · ℋₘ / (N₀^{1/3} v^{2/3}) and extract the dimensionless coefficient α for each orientation. For each structure, compute the minimum α (α_min), maximum α (α_max), and, where possible, the arithmetic average α_a over orientations. Write the results to alpha_values.json.
- Output file: `/app/outputs/alpha_values.json`
- Format: json
- Contract: Array of 5 objects. Each object has keys: structure (string: 'fcc','hcp','bcc','diamond','sc'), alpha_min (float), alpha_max (float), alpha_avg (float or null). For 'hcp' alpha_avg is null.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_values.json
- path: `/app/outputs/alpha_values.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the computed dimensionless coefficient α statistics for fcc, hcp, bcc, diamond, and sc lattices. Values are compared to the paper's reported numbers within a tolerance.
- schema:
  - `type`: array
  - `required`:
    - `top_level`: array of objects
  - `items`:
    - `structure`: string
    - `alpha_min`: float
    - `alpha_max`: float
    - `alpha_avg`: float or null
  - `required_columns`:
  - `units`: object

Notes: The homogeneous nucleation analysis (Section 3.2) is omitted because it requires element-specific experimental data not available as public inputs. The task focuses on the plane-surface coefficients at the melting point, which is the primary computational claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "required": {
          "top_level": "array of objects"
        },
        "items": {
          "structure": "string",
          "alpha_min": "float",
          "alpha_max": "float",
          "alpha_avg": "float or null"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Contains the computed dimensionless coefficient α statistics for fcc, hcp, bcc, diamond, and sc lattices. Values are compared to the paper's reported numbers within a tolerance."
    }
  ],
  "notes": "The homogeneous nucleation analysis (Section 3.2) is omitted because it requires element-specific experimental data not available as public inputs. The task focuses on the plane-surface coefficients at the melting point, which is the primary computational claim."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the artifact `/app/outputs/alpha_values.json` and compares each reported α_min, α_max, and α_avg (where present) for the five structures against hidden reference values. The comparison uses an absolute tolerance defined on the verifier side. Your reward is the fraction of these 14 numeric values that fall within the tolerance. Reporting numbers alone is not sufficient – the verifier checks that the required numbers are present, correct in format, and close to the expected values. There is no partial credit for cosmetic similarity or shape; only numeric closeness counts.
