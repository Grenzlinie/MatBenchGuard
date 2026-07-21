# Adatom Diffusion and Schwoebel Barriers on Si(111) via Stillinger‑Weber Potential

## Problem background
Adatom diffusion and step‑edge (Schwoebel) barriers on the Si(111) surface control growth morphologies and step‑bunching instabilities during epitaxy and sublimation.  Empirical potentials provide a computationally tractable way to probe these barriers before resorting to costlier ab‑initio methods.  This work maps the adatom potential energy V(x,y) on the 1×1 reconstructed Si(111) surface and on two high‑symmetry steps using the Stillinger‑Weber potential, and from those maps extracts the surface diffusion barrier and the extra Schwoebel barriers encountered when an adatom crosses a step edge.

## Approach
The adatom potential energy landscape V(x,y) is computed for three configurations:  (1) the pristine Si(111) surface, (2) a vicinal surface with a  \([\overline{211}]\)  step, and (3) a vicinal surface with a  \([\overline{\Pi2}]\)  step.  In each case a slab of Si(111) bilayers is built, with the bottom bilayers and the in‑plane boundaries held fixed at the positions of the relaxed adatom‑free structure to avoid unwanted shear.  A sampling grid covering the symmetrically distinct region is defined: a triangular grid for the surface (one sixth of the unit cell) and rectangular grids for the step configurations.  An adatom is placed sequentially at each grid point with its (x,y) coordinates constrained; the rest of the system is relaxed using energy minimization (steepest‑descent).  The adatom potential energy at that point is the difference between the minimum potential energy of the adatom‑free system and that of the system with the fixed adatom.

From the collected V(x,y) values the global minimum on the surface (the H₃ site) and the relevant saddle point for H₃↔H₃ diffusion are identified, and the surface diffusion barrier is computed as their difference.  For the step configurations the barrier‑determining saddle points far from the step edge and at the step edge are located, and the Schwoebel barriers are defined as the difference between those saddle energies and the surface saddle energy (s₁).  All energies and barriers are reported in eV.

## Required physical parameters

### Si lattice and surface constants
- Diamond‑structure Si lattice constant:  a₀ = 5.431 Å  
- Si(111) 1×1 surface in‑plane lattice constants:  
  \[
  a_1 = a_2 = \frac{a_0}{\sqrt{2}} \approx 3.840\ \text{Å}
  \]  
  (both primitive vectors of the hexagonal surface mesh have equal length; they are used to define the sampling grids and slab sizes).

### Stillinger–Weber potential for silicon (unit: eV, length: Å)
Two‑body term (\(r < a\sigma\), zero otherwise):  
\[
V_2(r) = \varepsilon\,A\left(B\,r^{-4} - 1\right) \exp\!\left(\frac{1}{r/\sigma - a}\right)
\]  

Three‑body term (sum over triplets with \(r_{ij}, r_{ik} < a\sigma\)):  
\[
V_3(r_{ij}, r_{ik}, \theta_{jik}) = \varepsilon\,\lambda\,
\exp\!\left(\frac{\gamma\sigma}{r_{ij} - a\sigma} + \frac{\gamma\sigma}{r_{ik} - a\sigma}\right)
(\cos\theta_{jik} - \cos\theta_0)^2
\]
with \(\cos\theta_0 = -1/3\).

**Parameter values**

| Parameter | Value | Notes |
|:---|:---|:---|
| \(\varepsilon\) | 2.1683 eV | energy scale |
| \(\sigma\)    | 2.0951 Å | length scale |
| \(A\)        | 7.049556277 | – |
| \(B\)        | 0.6022245584 | – |
| \(a\)        | 1.80 | dimensionless cut‑off parameter |
| \(\lambda\)   | 21.0 | – |
| \(\gamma\)    | 1.20 | – |

The actual cut‑off radius is \(a\sigma \approx 3.771\ \text{Å}\).

### Slab construction and relaxation protocol
- **Bottom fixation:** The three lowest bilayers are frozen at bulk lattice positions throughout all calculations.  
- **Lateral boundaries:** Atoms at the in‑plane (x,y) boundaries are also fixed at the positions of the relaxed adatom‑free configuration.  
- **System size:**  
  - *Surface:* use a slab extending 4 a₁ in x and 4 a₂ in y, with 3 movable bilayers (six atomic layers) in addition to the fixed bottom bilayers.  
  - *[\(\overline{211}\)] step:* lateral size 4 a₁ in x, and in y extended to \(4\frac{2}{3}\) a₂ to accommodate the vicinal step.  
  - *[\(\overline{\Pi2}\)] step:* lateral size 4 a₁ in x, and in y extended to \(4\frac{1}{3}\) a₂.  
- **Relaxation:** For each fixed (x,y) of the adatom, perform steepest‑descent energy minimization (or molecular dynamics with dissipative cooling) until the maximum force component on any atom is smaller than \(1\times10^{-4}\) eV/Å.  
- **Initial adatom height:** Choose the z‑coordinate of the adatom to be that obtained in a previously relaxed configuration at a neighbouring (x,y) point.

### Sampling grids (symmetry‑reduced regions)
- **Free surface:** one‑sixth of the hexagonal unit cell; triangular grid with spacing \(a_2/9\) along the high‑symmetry directions.  
- **[\(\overline{211}\)] step:** rectangular grid; width \(a_1/2\) along x, length \(\frac{5}{3}a_2\) along y; spacing \(a_1/16\) in x and \(a_2/30\) in y.  
- **[\(\overline{\Pi2}\)] step:** rectangular grid; width \(a_1\) along x, length \(\frac{4}{3}a_2\) along y; spacing \(a_1/16\) in x and \(a_2/30\) in y.  

Exploit the three‑fold symmetry on the surface and the reflection symmetry across the step for the two vicinal configurations.

### Barrier extraction from V(x,y)
- **Surface:** locate the global minimum (the H₃ site) and the saddle point s₁ (near the T₄ site) that controls H₃↔H₃ diffusion.  
  \[
  \text{surface diffusion barrier} = V(s_1) - V(\text{H}_3)
  \]  
- **[\(\overline{211}\)] step:** identify the saddle point s₃ that governs crossing from the upper terrace into the step edge.  
  \[
  \text{Schwoebel barrier}\,(211) = V(s_3) - V(s_1)
  \]  
- **[\(\overline{\Pi2}\)] step:** identify the saddle point s₅ that governs crossing from the upper terrace into the step edge.  
  \[
  \text{Schwoebel barrier}\,(\overline{\Pi2}) = V(s_5) - V(s_1)
  \]  
The barriers should be reported in eV, rounded to two decimal places.

## Reproduction target
You must compute the three energy barriers by directly implementing the Stillinger‑Weber potential and the grid‑based mapping described above.  The final results are to be written to a single JSON file.

- Surface diffusion barrier on the 1×1 Si(111) surface,
- Schwoebel barrier for an adatom crossing a \([\overline{211}]\) step,
- Schwoebel barrier for an adatom crossing a \([\overline{\Pi2}]\) step.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_barriers.json`

## Output contract

### computed_barriers.json
- path: `/app/outputs/computed_barriers.json`
- format: json
- purpose: scored
- target_policy: metric_direct_compare
- description: The three energy barriers (in eV) extracted from the potential energy maps.  The hidden verifier compares these values directly against reference values to assign credit.
- schema:
  - `type`: object
  - `required`:
    - `surface_diffusion_barrier_eV`: float (eV)
    - `schwoebel_barrier_211_eV`: float (eV)
    - `schwoebel_barrier_112_eV`: float (eV)

## How you are scored
A hidden verifier reads the file `computed_barriers.json` and compares each barrier value to an expected reference.  Full credit is given for values that fall within a predefined tolerance.  The verifier does not recompute barriers from raw data; it only evaluates the numbers you supply.  Therefore your calculation must be accurate and consistent with the physical model described above.

## Self‑check before finishing (optional, not scored)

Run a small script that checks the shape of every output file under `/app/outputs`: ensure `computed_barriers.json` exists, is valid JSON, and contains the three required numeric fields.  This self‑check only verifies file format, not scientific correctness.

```json
{
  "outputs": [
    {
      "file": "computed_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_direct_compare",
      "schema": {
        "type": "object",
        "required": {
          "surface_diffusion_barrier_eV": "float (eV)",
          "schwoebel_barrier_211_eV": "float (eV)",
          "schwoebel_barrier_112_eV": "float (eV)"
        }
      },
      "description": "The three energy barriers (in eV) extracted from the potential energy maps.  The hidden verifier compares these values directly against reference values to assign credit."
    }
  ],
  "notes": "The verifier compares the supplied barrier values to expected answers.  The agent must provide accurate values from its own calculation."
}
```