# Kinetic Monte Carlo Simulation of MBE Growth on V-Grooved Substrates

## Problem background
Molecular-beam epitaxy (MBE) overgrowth on V-grooved GaAs(001) substrates exhibits facet-dependent growth kinetics. At elevated temperatures, surface diffusion of adatoms between facets can lead to strongly non-uniform growth rates and changing surface morphology; at lower temperatures, the growth is expected to be more shape-preserving. Understanding how the choice of hopping barrier parameters (which encode facet-dependent adatom mobility) and substrate temperature control the effective growth-rate profile across the patterned surface is central to designing controlled nanostructure fabrication. This task targets a quantitative simulation of these kinetics to determine the emergent growth-rate pattern under two distinct mobility scenarios at two temperatures.

## Approach
The model is a solid-on-solid kinetic Monte Carlo (KMC) simulation on a simple cubic lattice with no vacancies or overhangs. Deposition occurs through random site selection with uniform probability; adatoms on the surface migrate via isotropic nearest-neighbor hopping governed by an Arrhenius rate \(k(E,T)=k_0 \exp(-E/k_B T)\) with attempt frequency \(k_0 = 2k_B T / h\). The hopping barrier \(E\) depends on the local environment:

\[
E = E_S + n E_N + m E_{2N}
\]

where \(n\) is the number of in-plane nearest neighbors and \(m\) is the number of out-of-plane next-nearest neighbors. The precise counting rules are as follows.

### Nearest neighbor and next-nearest neighbor counting
In the simple cubic lattice, each atom has six nearest neighbors at distance \(a\) (along ±x, ±y, ±z) and twelve next-nearest neighbors at distance \(\sqrt{2}\,a\) (along the face diagonals). When evaluating the barrier for an adatom before a hop, identify the local surface normal \(\hat{n}\) of the facet to which the adatom belongs:

- For the planar (001) terrace: \(\hat{n} = \hat{z}\) (pointing upward).
- For the 45° diagonal V‑groove facet: \(\hat{n} = (\hat{x} + \hat{z})/\sqrt{2}\) (pointing outward from the groove into vacuum).

Now consider all occupied neighbor sites (substrate atoms or other deposited atoms).

1. **In-plane nearest neighbors (\(n\)):** Among the six nearest-neighbor directions, select those whose vector from the adatom is perpendicular to \(\hat{n}\) (i.e., lies entirely in the local surface plane). Count how many of these sites are occupied. These contribute to \(n\).

2. **Out-of-plane next-nearest neighbors (\(m\)):** Among the twelve next-nearest-neighbor directions, select those whose vector has a non‑zero component along \(\hat{n}\) (i.e., is **not** entirely in the surface plane). Count how many of these sites are occupied. These contribute to \(m\).

The substrate atom directly beneath the adatom (the nearest neighbor along \(-\hat{n}\)) is considered part of the substrate contribution \(E_S\) and is **not** included in \(n\) or \(m\).

#### Typical isolated adatom values
- On the planar (001) surface, an isolated adatom (no other deposited atoms nearby) has:
  - \(n = 0\) (no occupied in-plane nearest neighbor),
  - \(m = 4\) (four occupied next-nearest neighbors below the surface, at diagonal positions).
- On the 45° diagonal surface, an isolated adatom has:
  - \(n = 2\) (the two nearest neighbors along the groove direction, the y‑axis, which lie in the facet plane),
  - \(m = 2\) (two occupied next-nearest neighbors with a component normal to the facet).

These typical values underlie the opposite mobility trends in the two parameter sets (see below). The counting rule can be applied dynamically during simulation for any adatom, accounting for additional neighbors that appear as growth proceeds.

### Simulation setup
Simulations are performed on a \(200 \times 200\) lattice containing a V-groove at \(45^\circ\) relative to the planar (001) surface, with periodic boundary conditions.

**Initial surface geometry (V-groove).** The initial surface profile along the lateral dimension (which becomes the x‑axis after projection) must contain two flat (001) terraces and a diagonal V‑groove facet. The regions are defined as:

- **Flat terrace:** lateral positions \(x = 0\) through \(49\) and \(x = 150\) through \(199\).
- **Diagonal V‑groove facet:** lateral positions \(x = 50\) through \(149\).

In the three‑dimensional lattice, set the surface height to a constant reference level (e.g., \(0\)) in the flat terrace regions. In the groove region, let the height decrease linearly from the terrace level to a minimum near the centre of the groove (\(x \approx 100\)) and then increase back to the terrace level, forming a symmetric V‑shape with \(45^\circ\) inclination relative to the (001) plane. The exact depth of the groove is not prescribed, but the projected 1D profile must exhibit the above spatial division between flat terrace and diagonal facet; the checker will compute statistics separately for the two regions using exactly the \(x\) ranges given above.

Two parameter sets are used:
- Set 1: \(E_{2N}=0.1\,\text{eV}, E_S=1.0\,\text{eV}, E_N=0.3\,\text{eV}\)
- Set 2: \(E_{2N}=0.38\,\text{eV}, E_S=0.3\,\text{eV}, E_N=0.1\,\text{eV}\)

For each set, the simulation is run at substrate temperatures \(T = 700\,\text{K}\) and \(T = 850\,\text{K}\) with an incident flux of 1 monolayer per second. 500 monolayers are deposited. After the KMC runs, the final height profile is projected by averaging over one lateral dimension (averaging along the y‑axis of the 200×200 lattice to obtain a 1D profile as a function of the x‑position), and the effective growth rate is obtained as the projected height minus the number of monolayers grown.

## Reproduction target
Produce the effective growth rate as a function of lateral position for every simulation condition — two parameter sets × two temperatures — and write the results to `effective_growth_rates.csv`. The checker will then verify whether the combined profiles fulfill a hidden structural relationship: specifically, whether the effective growth rate on the flat terrace and on the diagonal facet exhibits a particular ordering at high temperature, and whether the growth rate is approximately uniform across the surface at low temperature. Satisfying this structural relationship constitutes a successful reproduction.

## Assets

- numpy: pip: numpy

## Workflow steps

### Step 1: KMC simulation of MBE growth
- Role: process
- Action: Implement the solid-on-solid kinetic Monte Carlo model: simple cubic lattice with no vacancies/overhangs, random deposition with uniform probability per site, isotropic nearest-neighbor hopping with Arrhenius rate \(k = k_0 \exp(-E/k_B T)\) where \(k_0 = 2k_B T / h\), and hopping barrier \(E = E_S + n E_N + m E_{2N}\) counted according to the rules in Approach. Simulate on a 200×200 lattice with a V-groove at 45° and periodic boundary conditions. Set up the initial surface according to the geometry described above (flat terrace at x=0–49,150–199, diagonal groove at 50–149). Run four simulations: parameter set1 (E2N=0.1 eV, ES=1.0 eV, EN=0.3 eV) and set2 (E2N=0.38 eV, ES=0.3 eV, EN=0.1 eV) at substrate temperatures T=700 K and T=850 K, with incident flux of 1 monolayer per second. Deposit 500 monolayers for each simulation. Keep the final surface height profile for each condition.

### Step 2: Compute projected effective growth rates
- Role: scored (load-bearing)
- Action: From the raw height profiles produced in step_01, average over one lateral substrate dimension (the y‑axis) to obtain a 1D surface profile. Subtract the number of deposited monolayers (500) to obtain the effective growth rate. For each of the four simulation conditions, output the effective growth rate as a function of lateral position.
- Output file: `/app/outputs/effective_growth_rates.csv`
- Format: csv
- Contract: Columns: parameter_set (integer, 1 or 2), temperature (integer, 700 or 850), position (integer, 0..199), effective_growth_rate (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_growth_rates.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_growth_rates.csv
- path: `/app/outputs/effective_growth_rates.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Effective growth rate distribution used to assess temperature-dependent growth mode: high temperature shows facet-dependent rate ordering, low temperature shows shape-preserving growth.
- schema:
  - `type`: table
  - `required_columns`: `parameter_set`, `temperature`, `position`, `effective_growth_rate`
  - `units`:
    - `effective_growth_rate`: monolayers

## How you are scored
A hidden verifier independently examines the artifacts you produce under `/app/outputs`. It loads the mandatory scored file `effective_growth_rates.csv`, computes mean effective growth rates on the expected flat-terrace (positions 0–49 and 150–199) and diagonal-facet (positions 50–149) regions, and checks that the data are consistent with the qualitative behavior described in the paper: at 850 K the average growth rate on the flat terrace is distinctly lower/higher than on the diagonal facet depending on the parameter set; at 700 K the growth rate profile is nearly uniform across the surface. The verifier combines the stage rewards (each in [0,1]) into a final overall score. Simply reporting a number that matches some published value is insufficient — you must generate the complete required CSV, and the verifier will evaluate it against its own hidden criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_growth_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter_set",
          "temperature",
          "position",
          "effective_growth_rate"
        ],
        "units": {
          "effective_growth_rate": "monolayers"
        }
      },
      "description": "Effective growth rate distribution used to assess temperature-dependent growth mode: high temperature shows facet-dependent rate ordering, low temperature shows shape-preserving growth."
    }
  ],
  "notes": "The checker will verify structural trends: at 850 K the growth rate profiles show a clear difference between flat terrace and diagonal facet; at 700 K the profile is nearly uniform. No exact numerical targets are required."
}
```