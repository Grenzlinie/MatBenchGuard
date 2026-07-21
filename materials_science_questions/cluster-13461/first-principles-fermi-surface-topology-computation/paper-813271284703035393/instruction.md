# Band structure of helical atomic chains using tight-binding

## Problem background
Atoms confined in nanoscale channels can self‑assemble into helical chains. Computing the electronic band structure of such structures helps explain conductivity changes in host materials. This task implements an empirical tight‑binding model that exploits the screw symmetry of a helical chain, reducing the problem to a single atom with a 4×4 Hamiltonian. The goal is to obtain the energy bands as a function of wave vector for three different chain geometries and to observe how twisting alters the dispersion of the p‑derived bands.

## Approach

### Helix geometry and atomic coordinates
A helical chain is defined by a radius `R`, an interatomic distance `d = 2.9 Å`, and a screw angle `θ`. The translation step along the chain axis (pitch per atom) is  

```
h = sqrt(d² − 4 R² sin²(θ/2))
```

For the linear chain (`R = 0` or `θ = 0`), `h = d`.  
The Cartesian coordinates of atom `n` (n = 0, ±1, ±2, …) are  

```
r_n = ( R cos(nθ),  R sin(nθ),  n h )
```

### Basis and Slater–Koster integrals
The tight‑binding basis consists of Löwdin orbitals `s`, `p_x`, `p_y`, `p_z` (the `p_η`, `p_τ` orbitals of the screw‑symmetry approach are rotated versions of `p_x`, `p_y`; the Hamiltonian is written directly in the Cartesian `p_x`, `p_y` basis).  

The Slater–Koster overlap parameters for the first and second neighbours are:

| neighbour order | V_ssσ (eV) | V_spσ (eV) | V_ppσ (eV) | V_ppπ (eV) |
|----------------|------------|------------|------------|------------|
| I              | −0.648     | 1.327      | 2.282      | −0.549     |
| II             | −0.089     | 0.133      | 0.343      | 0.052      |

Orbital energies: `E_s = −17.239 eV`, `E_p = −6.857 eV`.

For a bond vector connecting atom 0 to atom n (`n = 1` for first neighbour, `n = 2` for second neighbour), the direction cosines are  

```
dx = R (cos(nθ) − 1)
dy = R sin(nθ)
dz = n h
d_n = sqrt(dx² + dy² + dz²)
l = dx / d_n,   m = dy / d_n,   n = dz / d_n
```

The Slater–Koster hopping integrals for that bond are then:

```
E_ss = V_ssσ
E_sx = l·V_spσ
E_sy = m·V_spσ
E_sz = n·V_spσ

E_xx = l²·V_ppσ + (1 − l²)·V_ppπ
E_yy = m²·V_ppσ + (1 − m²)·V_ppπ
E_zz = n²·V_ppσ + (1 − n²)·V_ppπ
E_xy = l·m·(V_ppσ − V_ppπ)
E_xz = l·n·(V_ppσ − V_ppπ)
E_yz = m·n·(V_ppσ − V_ppπ)
```

For the **first neighbour** (`n = 1`), the parameters `V_ssσ, V_spσ, V_ppσ, V_ppπ` are taken directly from the “I” row above.  
For the **second neighbour** (`n = 2`), the tabulated “II” values must be scaled to account for the different bond length in the actual helix geometry. The scaling rule is  

```
V^(2) = V^(II) · (d_ref / d_2)²
```

where `d_ref = 2d = 5.8 Å` is the second‑neighbour distance in the linear chain. All four Slater–Koster parameters of the second neighbour are multiplied by the same factor `(2d / d_2)²`. (For the linear chain this factor equals 1; for helical geometries `d_2` differs from 2d and the parameters are adjusted accordingly.)

### 4×4 Hamiltonian matrix
The tight‑binding Hamiltonian is expressed in the Bloch‑sum basis for orbitals `(s, p_x, p_y, p_z)` but written in the rotated normal/tangential representation that diagonalises the angular part. The following explicit matrix elements are for the **reduced** (p_η, p_τ, p_z, s) basis. *(These expressions are already in the basis where the angular dependence is absorbed; the Cartesian Slater–Koster integrals `E_xx, E_xy, …` are computed as above for the two neighbours.)*

Let `E_{ij}^{(n)}` denote the Slater–Koster integrals for neighbour `n` (with the scaled parameters for `n = 2`). Then, with `k` the reduced wave vector (dimensionless, −½ < k ≤ ½), we have:

```
H11 = E_p + 2 cos(2πk)·( cos(θ)·E_xx^(1) + sin(θ)·E_xy^(1) 
                      + cos(2θ)·E_xx^(2) + sin(2θ)·E_xy^(2) )

H22 = E_p − 2 cos(2πk)·( sin(θ)·E_xy^(1) − cos(θ)·E_yy^(1) 
                      + sin(2θ)·E_xy^(2) − cos(2θ)·E_yy^(2) )

H33 = E_p + 2 cos(2πk)·( E_zz^(1) + E_zz^(2) )

H44 = E_s + 2 cos(2πk)·( E_ss^(1) + E_ss^(2) )

H12 = −2i sin(2πk)·( sin(θ)·E_xx^(1) − cos(θ)·E_xy^(1) 
                    + sin(2θ)·E_xx^(2) − cos(2θ)·E_xy^(2) )

H13 = −2i sin(2πk)·( E_xz^(1) + E_xz^(2) )

H14 = −2 cos(2πk)·( E_sx^(1) + E_sx^(2) )

H23 =  2 cos(2πk)·( E_yz^(1) + E_yz^(2) )

H24 = −2i sin(2πk)·( E_sy^(1) + E_sy^(2) )

H34 = −2i sin(2πk)·( E_sz^(1) + E_sz^(2) )
```

The remaining matrix elements follow from Hermiticity:

```
H21 = H12*,   H31 = H13*,   H32 = H23*
H41 = H14*,   H42 = H24*,   H43 = H34*
```

Thus the complete 4×4 Hamiltonian is:

```
H(k) = [ [H11,  H12,  H13,  H14],
         [H12*, H22,  H23,  H24],
         [H13*, H23*, H33,  H34],
         [H14*, H24*, H34*, H44] ]
```

### Band energies
For each wave vector `k` and geometry, construct `H(k)`, diagonalise it, and sort the **real** eigenvalues in ascending order. Assign the band indices `0,1,2,3` from lowest to highest energy. The three geometries to evaluate are:

1. Linear chain: `R = 0 Å`, `θ = 0`.
2. Helix with pitch 125 Å: `R = 3.25 Å`, `θ = 0.1439 rad`.
3. Helix with pitch 50 Å: `R = 3.25 Å`, `θ = 0.3375 rad`.

Sample at least 200 equally spaced `k` points in the interval `[−0.5, 0.5]` for each geometry.

## Reproduction target
Your primary output is a CSV file containing the band energies for all four bands and all three geometries. The file must have the columns: `k` (the wave vector value), `band` (integer 0–3 indexing the four bands, sorted ascending in energy), `E` (band energy in eV), and `geometry` (one of `'linear'`, `'helix125'`, `'helix50'`). Provide at least 200 k‑points per geometry.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute tight-binding band structures
- Role: scored (load-bearing)
- Action: Implement the 4×4 tight-binding Hamiltonian for a helical atomic chain using the formulas and parameters given above. For each of the three geometries, construct the Hamiltonian matrix for at least 200 uniformly spaced k in [-0.5, 0.5], diagonalise, sort eigenvalues (lowest = band 0), and output the band energies.
- Output file: `/app/outputs/band_energies.csv`
- Format: csv
- Contract: CSV file with columns: `k` (float, the k-point value), `band` (int, 0-3 indexing the four bands), `E` (float, band energy in eV), `geometry` (string: 'linear', 'helix125', 'helix50'). Must contain at least 200 k-points per geometry and all four bands.
- Scoring: scored by structural checker

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_energies.csv`

## Output contract

Every file the verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_energies.csv
- path: `/app/outputs/band_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed electronic band energies for all four bands and three geometries (linear, helix125, helix50).
- schema:
  - `type`: table
  - `required_columns`: `k`, `band`, `E`, `geometry`
  - `units`:
    - `E`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k",
          "band",
          "E",
          "geometry"
        ],
        "units": {
          "E": "eV"
        }
      },
      "description": "Computed electronic band energies for all four bands and three geometries (linear, helix125, helix50)."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a structural checker that verifies the following physical features of the computed band structure:

1. **k‑point sufficiency** – Each geometry has at least 200 unique k points. *(weight 10%)*
2. **Linear chain degeneracy** – For the linear chain (`R=0, θ=0`), the two middle bands (bands 1 and 2) are degenerate at every k point (within a tolerance of 1e‑4 eV). *(weight 30%)*
3. **125 Å helix splitting** – For the helix125 geometry, the two p‑derived bands (bands 1 and 2) exhibit a small but non‑zero splitting at k≈0. The checker verifies that the splitting is consistent with the helical coupling expected from the model. *(weight 30%)*
4. **50 Å helix larger splitting** – At k ≈ 0 for the helix50 geometry, the splitting between the same two bands is larger than the corresponding splitting of helix125. *(weight 30%)*

The total reward is the weighted sum of these four sub‑scores (each in [0,1]). A total of 0.6 or above is considered a pass. The checker does **not** compare your absolute energies to a reference; it only examines the structural properties listed above. Therefore, concentrate on correctly implementing the Hamiltonian and the scaling rule so that the required degeneracies and splittings emerge naturally.