# Homogenization distance calculation for C-Mn steels

## Problem background
In the welding of C‑Mn steels, the heat‑affected zone (HAZ) near the fusion line experiences a rapid thermal cycle that causes carbon to migrate from pearlite into ferrite. Incomplete carbon homogenization can leave regions with elevated carbon content, increasing local hardenability and the susceptibility to hydrogen‑assisted cracking (HAC). The extent of homogenization depends on the initial microstructural geometry, which differs between normalized and hot‑rolled plate. The key unknown is the characteristic diffusion distance √(Dt) required to reach a nearly uniform carbon distribution in each microstructure.

## Approach
Two idealized diffusion models capture the essential physics:

- **Normalized steel** is approximated as a sphere of ferrite (radius a = 10 µm) surrounded by a thin shell of pearlite. Carbon diffuses from the pearlite reservoir into the ferrite sphere. The applicable solution is that of diffusion into a sphere from a well‑stirred volume of limited capacity. The result is expressed as a series expansion that gives the concentration inside the sphere as a function of dimensionless time τ = Dt/a². We are interested in the dimensionless time at which the fractional approach to equilibrium (i.e. the average carbon concentration in the sphere divided by the equilibrium concentration) reaches 0.95. The homogenization distance is then √(Dt) = a·√τ.

- **Hot‑rolled steel** exhibits a banded structure: alternating layers of ferrite (~60 µm) and pearlite (~20 µm). The diffusion problem reduces to a one‑dimensional finite slab whose symmetry element has length L = 40 µm (from the centre of a pearlite band to the centre of the adjacent ferrite band). Initially, carbon is confined to the pearlite half‑width p = 10 µm with concentration C₀, while the rest of the slab is essentially carbon‑free. The concentration profile is built from error‑function solutions modified by reflection at the zero‑flux boundaries (x = 0 and x = L). The model is used to find the √(Dt) at which the carbon distribution becomes “essentially uniform”, defined quantitatively below.

## Model specifications

### 1. Normalized microstructure (spherical geometry)

#### Geometry parameters
- Ferrite sphere radius: a = 10 µm  
- Pearlite shell outer radius: r_out = 10.8 µm (the appropriate shell size for a 0.2 wt% C steel)

#### Volume factor K
The well‑stirred finite‑volume solution uses the parameter  

```
K = 3 V_shell / (4 π a²)
```
where the shell volume is  

```
V_shell = (4/3) π (r_out³ − a³)
```

Compute K in µm with the given radii.

#### Concentration profile
The solution inside the sphere (r ≤ a) is given by Crank as

```
C(r, t) = ────── 1   +  Σ   ──────── 6 K   ────── · ────── sin(α_i ξ) ────── · exp( − α_i² τ )
             1+K       i=1   3K(3K+3) + α_i²             sin(α_i)
```

with  
- τ = D t / a²   (dimensionless time)  
- ξ = r / a  
- α_i  = positive roots of the eigenvalue equation  

```
α cot α − (1 + α² / (3K)) = 0
```

The roots α_i must be found numerically (e.g. via root‑finding in SciPy). Sufficient roots (typically the first 10–20) should be included so that the series converges.

#### Fractional approach to equilibrium
Let C_eq = C₀ / (1+K) be the uniform equilibrium concentration (C₀ is the initial carbon concentration in the pearlite, which can be taken as 1 for the purpose of computing fractions).  
The average concentration inside the sphere is

```
C_avg(τ) = (3 / a³) ∫_0^a C(r,t) r² dr
```

The fractional approach to equilibrium is  

```
F(τ) = C_avg(τ) / C_eq
```

The goal is to find τ_95 such that F(τ_95) = 0.95. The homogenization distance is then

```
√(Dt)_normalized = a √τ_95    [µm]
```

### 2. Hot‑rolled microstructure (one‑dimensional finite slab)

#### Geometry parameters
- Ferrite band width = 60 µm, pearlite band width = 20 µm  
- Repeat distance r = 80 µm  
- Symmetry element length: L = 40 µm (from the centre of a pearlite band to the centre of an adjacent ferrite band)  
- Initial pearlite half‑width: p = 10 µm (0.125 · r)

#### Concentration profile – reflection method
In an infinite medium, a region of solute C₀ over length p produces the profile (Stefan)

```
C_inf(x, t) = (C₀/2) [ erf((p+x)/(2√(Dt))) + erf((p−x)/(2√(Dt))) ]
```

For the finite slab 0 ≤ x ≤ L with zero‑flux boundaries, the solution is obtained by the method of images, summing over an infinite set of reflected sources:

```
C(x,t) = (C₀/2) ·  Σ  [ erf( (p + x - 2nL) / (2√(Dt)) ) − erf( (−p + x - 2nL) / (2√(Dt)) ) ]
                  n=-∞
```

In practice the sum is truncated when the contribution of additional terms becomes negligible (e.g. |n| ≤ 10 or until the added erf difference < 1e‑12).

#### Quantitative uniformity criterion
The carbon distribution is considered **essentially uniform** when the difference between the maximum and minimum concentration in the slab falls below 1 % of C₀:

```
max C(x,t) − min C(x,t)  ≤ 0.01 C₀
```

Find the smallest √(Dt) (in µm) that satisfies this criterion.

## Reproduction target
Implement the two diffusion models described above and compute the homogenization distances:

1. For the normalized microstructure, find the √(Dt) (in micrometres) at which 95 % homogenization is achieved.  
2. For the hot‑rolled microstructure, find the √(Dt) (in micrometres) at which the carbon distribution is essentially uniform (as defined above).

Write both values to a single JSON file at `/app/outputs/homogenization_distances.json` using the keys `normalized_steel_95pct_sqrtDt_micrometers` and `hot_rolled_steel_sqrtDt_essentially_complete_micrometers`.

## Assets

- NumPy: numpy  
- SciPy: scipy

## Workflow steps

### Step 1: Compute homogenization distances
- **Role**: scored (load‑bearing)
- **Action**:
  - **Normalized case**: compute K from the given radii; find the roots α_i of the eigenvalue equation; compute the series for C(r,t) and integrate to obtain F(τ); solve for τ where F(τ)=0.95; calculate √(Dt) = a·√τ.
  - **Hot‑rolled case**: use the reflection formula with L=40 µm and p=10 µm; sweep √(Dt) to find the smallest value for which max−min concentration difference ≤ 0.01·C₀.
- **Output file**: `/app/outputs/homogenization_distances.json`
- **Format**: json
- **Contract**: JSON object with keys `normalized_steel_95pct_sqrtDt_micrometers` (float) and `hot_rolled_steel_sqrtDt_essentially_complete_micrometers` (float).
- **Scoring**: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogenization_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogenization_distances.json
- **path**: `/app/outputs/homogenization_distances.json`
- **format**: json
- **purpose**: scored
- **target_policy**: reference_match
- **description**: Computed √(Dt) homogenization distances for the normalized and hot‑rolled steel microstructures. The checked values are compared to hidden reference values with an appropriate tolerance.
- **schema**:
  - `type`: object
  - `required`:
    - `normalized_steel_95pct_sqrtDt_micrometers`: float (micrometers)
    - `hot_rolled_steel_sqrtDt_essentially_complete_micrometers`: float (micrometers)
  - `items`: object
  - `required_columns`: []
  - `units`: object

Notes: The task reproduces the two headline homogenization distances reported in the paper. Only the computed distances are scored.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogenization_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "normalized_steel_95pct_sqrtDt_micrometers": "float (micrometers)",
          "hot_rolled_steel_sqrtDt_essentially_complete_micrometers": "float (micrometers)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Computed √(Dt) homogenization distances for the normalized and hot-rolled steel microstructures. The checked values are compared to hidden reference values with an appropriate tolerance."
    }
  ],
  "notes": "The task reproduces the two headline homogenization distances reported in the paper. The first step parameterizes the microstructural dimensions; the second step computes the distances. Only the computed distances are scored."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/homogenization_distances.json` and compare the two numeric values against predetermined reference results. Each distance is checked independently; the final reward is proportional to the number of values that fall within an accepted tolerance band around the reference. Simply reporting a number without running the required diffusion calculations will not succeed. Ensure your output file follows the required JSON format exactly.