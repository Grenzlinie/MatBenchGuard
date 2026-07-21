# Compute vacancy formation and migration activation energies near a twist grain boundary in copper

## Problem background
Grain boundaries play a critical role in materials properties such as grain growth, deformation, and fracture, and atomic diffusion along boundaries is central to these phenomena. Understanding how vacancies form and migrate near a grain boundary is essential for predicting diffusion behavior and vacancy accumulation. This task investigates the energetic landscape of a single vacancy in the vicinity of a copper Σ=5 [001] twist grain boundary by computing the formation energies at different positions and the migration activation barriers for intra- and inter-layer hops using molecular dynamics with a modified analytical embedded-atom method (MAEAM) potential.

## Approach
The atomic interactions are described by a modified analytical embedded-atom method (MAEAM) potential for Cu, whose functional forms and all parameter values are fully specified in this instruction. The grain boundary is modeled as a Σ=5 [001] twist boundary with a supercell containing two grains, each of thickness 5a (where a is the lattice constant), periodic in the boundary plane, and a surrounding mantle of fixed atoms. The MAEAM energy and forces are computed from the pairwise and embedding terms, and the system is relaxed using a predictor–corrector molecular dynamics algorithm. Vacancy formation energies are obtained by comparing the total energy of the perfect cell with that of a cell containing a single vacancy, plus the cohesion energy. Migration activation energies are determined by mapping the minimum-energy path for vacancy hops within a layer or between adjacent layers, identifying the saddle-point energy relative to the initial equilibrium site. The computation is performed for the three inequivalent coincident-site-lattice (CSL) sites in each of the first four atomic layers on one side of the boundary, plus a bulk reference, and for the nearest-neighbor migration paths defined in the instruction.

## Reproduction target
Compute the vacancy formation energy for each inequivalent CSL site (coincident and un-coincident) in layers 1–4 and in bulk Cu, and compute the activation energy for every intra-layer migration path in layers 1–4 and every inter-layer migration path including the cross-boundary jump to the rotating grain (1L–1LR). The output must be two JSON files: one containing the formation energies in eV following the schema in Step 2, and one containing the activation energies in eV following the schema in Step 3. All energies must be obtained by molecular dynamics relaxations using the provided MAEAM potential and the grain boundary supercell built in Step 1.

## Assets
This task does not require any external datasets or pre-trained models. All needed components are either provided in this instruction or are standard Python libraries. The MAEAM potential functional forms and all parameter values for copper are reproduced in the instruction. You may use Python 3 with NumPy for numerical operations. Molecular dynamics integration and energy minimization can be implemented from scratch or using a general-purpose optimization library, but no specific MD package is mandated.

## Workflow steps

### Step 1: Build Σ=5 [001] twist grain boundary supercell and identify vacancy sites
- Role: process
- Action: Construct the atomic supercell for a Cu Σ=5 [001] twist grain boundary with the following specifications.
  - **Crystal structure**: Cu is face-centered cubic (FCC) with lattice constant a = 0.36147 nm (see Table 1). The unit cell vectors in the unrotated reference are along [100], [010], [001] with length a.
  - **Twist boundary geometry**: A Σ=5 [001] twist boundary is formed by rotating one grain with respect to the other by an angle θ about the common [001] axis (z-axis). Use θ = 36.87° (tanθ = 3/4), which generates a Σ=5 coincidence site lattice. The CSL unit cell in the boundary plane is spanned by vectors **v₁** = a*(2,1,0) and **v₂** = a*(-1,2,0) of length √5 a.
  - **Supercell dimensions**: The computational cell comprises two grains (unrotated and rotated) stacked along z. Each grain extends 5a along the z-direction, giving a total supercell thickness of 10a. The in‑plane dimensions are 5a × 5a, which accommodates one CSL unit cell. The supercell is thus a 5a × 5a × 10a block (5a × 5a × 5a for each grain). Surround the free‑atom region with a mantle of atoms fixed at their perfect lattice positions (at least one unit cell thick) to maintain the boundary structure.
  - **Layer structure and site identification**:
    - In each grain, (001) atomic planes are spaced by a/2 along z. The unrotated grain occupies the lower half (z = 0 to z = 5a) and the rotated grain the upper half (z = 5a to z = 10a). Layer indices increase from the boundary plane outward: odd layers (2n−1) and even layers (2n) have distinct in‑plane registry. In the unrotated grain, odd layers contain sites labelled by numbers 1 to 5, even layers by letters a to e (see Fig. 1). In the rotated grain the same labelling is used with the subscript 'R' (e.g., a_R, 1_R).
    - Due to the two‑fold rotation axis through the CSL unit cell centre, sites 4 and 5 are equivalent to 2 and 3, and sites d and e are equivalent to b and c. Therefore, only three inequivalent sites per layer need to be considered: site 1 (coincident) and sites 2 and 3 (un‑coincident) for odd layers; site a (coincident) and sites b and c (un‑coincident) for even layers.
    - To assign site labels without relying on the original figure, use the following **reference positions** in the CSL plane (given in units of the lattice constant a, for the unrotated grain). For an **odd layer** (2n−1)L, the five atom sites and their (x, y) coordinates are:
      - 1: (0, 0)
      - 2: (1, 0.5)
      - 3: (–0.5, 1)
      - 4: (–1, –0.5)
      - 5: (0.5, –1)
    - For an **even layer** (2n)L, the five atom sites are offset by (a/2, a/2) in the (001) plane; their coordinates are:
      - a: (0.5, 0.5)
      - b: (1.5, 1.0)
      - c: (0.0, 1.5)
      - d: (–0.5, 0.0)
      - e: (1.0, –0.5)
    - During construction, take each atom in the unrotated grain, compute its projection (x, y) modulo the CSL vectors v₁, v₂ (i.e., express (x,y) in the CSL coordinate frame and keep the fractional parts 0≤u<1, 0≤v<1), and match it to the nearest reference site from the lists above to determine its label (1–5 or a–e). The same procedure applies to the rotated grain after applying the 36.87° rotation to the coordinates.
    - Store **only the atoms in the free‑atom region** (the mantle atoms are fixed and not part of the energy calculations). Save the labelled supercell for later steps.
  - **Bulk reference**: For the bulk formation energy, create a separate perfect bulk FCC cell of the same free‑atom dimensions (5a × 5a × 10a) with periodic boundaries in all directions. In this cell all sites are equivalent; the vacancy formation energy should be identical for any atom.
- Evidence: `/app/outputs/gb_supercell.data`

### Step 2: Vacancy formation energies
- Role: scored (load-bearing)
- Action: Implement the MAEAM interatomic potential for Cu using the functional forms and parameter values given in the Appendix. For each inequivalent site (coincident and un-coincident) in layers 1–4 of the unrotated grain and for a site in bulk, create a single vacancy by removing the corresponding atom and relax the system using molecular dynamics with MAEAM forces (detailed in the Appendix). Compute the formation energy E_f = E(N−1,1) − E(N,0) + E_c, where E(N−1,1) is the energy of the cell with a vacancy, E(N,0) is the energy of the perfect cell, and E_c = 3.49 eV is the cohesion energy. Collect all formation energies (in eV) in a structured JSON file.
- Output file: `/app/outputs/step_01_formation_energies.json`
- Format: json
- Contract: A JSON object with key `"bulk_formation_energy"` (float) and for each of the first four layers a key `"layer1"`, `"layer2"`, `"layer3"`, `"layer4"`. Each layer value is an object with keys `"site1"`, `"site2"`, `"site3"` mapping to the formation energy in eV (float). The energies must be the computed values; **do not include any placeholder or example numbers**.
- **Expected physical trends** (these follow from the physics and can serve as a self‑check): the un‑coincident sites in layer1 (`site2` and `site3`) should have negative formation energies; the coincident site1 formation energy should increase progressively from layer1 to layer4 (and approach the bulk value).
- Scoring: scored by hidden verifier

### Step 3: Vacancy migration activation energies
- Role: scored (load-bearing)
- Action: For each of the migration paths listed below, determine the activation energy Q_v = E_sad − E_eq + E_f, where E_sad is the saddle‑point energy, E_eq the energy of the initial vacancy site, and E_f its formation energy (from Step 2). All paths are first‑nearest‑neighbour jumps within a layer or between adjacent layers. Use the site labels defined in Step 1; the rotating grain sites carry an 'R' subscript.

  **Saddle‑point search algorithm**: For a given path, identify the initial and final positions of the jumping atom (the vacancy). Create a series of N intermediate images (e.g., N = 10) by linearly interpolating the jumping atom’s coordinates between the initial and final sites. For each image, fix the jumping atom at the interpolated position and relax all other free atoms using the same MD relaxation procedure as in Step 2 (damped dynamics, force tolerance 1e-4 eV/Å). The fixed mantle atoms remain immobile. Record the total energy of the system after relaxation at each image. The saddle‑point energy E_sad is the maximum value among these energies along the path. (This constraint‑relaxation method maps the minimum‑energy path and captures the energy barrier.)

  **Paths to compute**:
  - **Intra‑layer paths** (all in the unrotated grain):
    - Layer 1L (odd): `1_to_2`, `1_to_3`, `2_to_3`, `2_to_4`, `3_to_5`
    - Layer 2L (even): `a_to_b`, `a_to_c`, `b_to_c`, `b_to_d`, `c_to_e`
    - Layer 3L (odd): `1_to_2`, `1_to_3`, `2_to_3`, `2_to_4`, `3_to_5`
    - Layer 4L (even): `a_to_b`, `a_to_c`, `b_to_c`, `b_to_d`, `c_to_e`
  - **Inter‑layer paths** (from the unrotated grain toward the boundary, except the last path which goes into the rotated grain):
    - `inter_1L‑1LR`: `2_to_cR`, `3_to_bR`
    - `inter_2L‑1L`: `a_to_2`, `b_to_2`, `c_to_2`
    - `inter_3L‑2L`: `1_to_a`, `2_to_a`, `3_to_a`
    - `inter_4L‑3L`: `a_to_1`, `b_to_1`, `c_to_1`
    - `inter_5L‑4L`: `1_to_a`, `2_to_a`, `3_to_a`
  (Paths for layers 5L/6L etc. beyond the fourth layer are not required; only the listed ones must be computed.)

- Output file: `/app/outputs/step_02_activation_energies.json`
- Format: json
- Contract: A JSON object with top-level keys exactly as in the above list: `"intra_1L"`, `"intra_2L"`, `"intra_3L"`, `"intra_4L"`, `"inter_1L-1LR"`, `"inter_2L-1L"`, `"inter_3L-2L"`, `"inter_4L-3L"`, `"inter_5L-4L"`. Each value is an object whose keys are the given source‑to‑target strings and whose values are the computed activation energy in eV (float). **Do not use any placeholder numbers.**
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gb_supercell.data` (plain text, supercell coordinates)
- `/app/outputs/step_01_formation_energies.json`
- `/app/outputs/step_02_activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gb_supercell.data
- path: `/app/outputs/gb_supercell.data`
- format: plain text
- purpose: evidence
- target_policy: ignore
- description: Atomic coordinates of the Σ=5 [001] twist GB supercell, stored as a simple text file. The exact format is at your discretion; it is not scored but must be present to demonstrate correct supercell construction.

### step_01_formation_energies.json
- path: `/app/outputs/step_01_formation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Layer- and site-resolved vacancy formation energies computed via MD/MAEAM. All energies are in eV. The JSON must contain exactly the specified keys.
- schema:
  - `type`: object
  - `required`:
    - `bulk_formation_energy`: float (eV)
    - `layer1`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer2`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer3`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)
    - `layer4`:
      - `site1`: float (eV)
      - `site2`: float (eV)
      - `site3`: float (eV)

### step_02_activation_energies.json
- path: `/app/outputs/step_02_activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Vacancy migration activation energies for intra- and inter-layer paths. All energies in eV. The JSON must contain entries for every path listed, using the correct site labels from the paper.
- schema:
  - `type`: object
  - `required`:
    - `intra_1L`: object with keys `1_to_2`, `1_to_3`, `2_to_3`, `2_to_4`, `3_to_5` mapping to float activation energy (eV)
    - `intra_2L`: object with keys `a_to_b`, `a_to_c`, `b_to_c`, `b_to_d`, `c_to_e`
    - `intra_3L`: object with keys `1_to_2`, `1_to_3`, `2_to_3`, `2_to_4`, `3_to_5`
    - `intra_4L`: object with keys `a_to_b`, `a_to_c`, `b_to_c`, `b_to_d`, `c_to_e`
    - `inter_1L-1LR`: object with keys `2_to_cR`, `3_to_bR`
    - `inter_2L-1L`: object with keys `a_to_2`, `b_to_2`, `c_to_2`
    - `inter_3L-2L`: object with keys `1_to_a`, `2_to_a`, `3_to_a`
    - `inter_4L-3L`: object with keys `a_to_1`, `b_to_1`, `c_to_1`
    - `inter_5L-4L`: object with keys `1_to_a`, `2_to_a`, `3_to_a`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gb_supercell.data",
      "format": "text",
      "purpose": "evidence",
      "target_policy": "ignore",
      "schema": {},
      "description": "Atomic coordinates of the Σ=5 [001] twist GB supercell, stored as a simple text file. The exact format is at your discretion; it is not scored but must be present to demonstrate correct supercell construction."
    },
    {
      "file": "step_01_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_formation_energy": "float (eV)",
          "layer1": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer2": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer3": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          },
          "layer4": {
            "site1": "float (eV)",
            "site2": "float (eV)",
            "site3": "float (eV)"
          }
        }
      },
      "description": "Layer- and site-resolved vacancy formation energies computed via MD/MAEAM. All energies are in eV. The JSON must contain exactly the specified keys."
    },
    {
      "file": "step_02_activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "intra_1L": "object with keys '1_to_2', '2_to_3', etc. mapping to float activation energy (eV)",
          "intra_2L": "object with keys like 'a_to_b', 'b_to_c', etc.",
          "intra_3L": "object with keys like '1_to_2', '2_to_3', etc.",
          "intra_4L": "object with keys like 'a_to_b', 'b_to_c', etc.",
          "inter_1L-1LR": "object with keys like '2_to_cR', '3_to_bR', etc.",
          "inter_2L-1L": "object with keys like 'a_to_2', 'b_to_2', etc.",
          "inter_3L-2L": "object with keys like '1_to_a', '2_to_a', etc.",
          "inter_4L-3L": "object with keys like 'a_to_1', 'b_to_1', etc.",
          "inter_5L-4L": "object with keys like '1_to_a', '2_to_a', etc."
        }
      },
      "description": "Vacancy migration activation energies for intra- and inter-layer paths. All energies in eV. The JSON must contain entries for every path listed, using the correct site labels from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently score each of the scored workflow stages (vacancy formation energies and vacancy migration activation energies) by comparing your submitted JSON artifacts against reference values. The verifier combines the scores from the individual stages into a final reward between 0 and 1. You must produce outputs that follow exactly the required format and contain physically correct energies computed from the specified potential and geometry. Reporting numbers without performing the required molecular dynamics relaxations will not succeed, as the verifier checks both the values and their consistency.

---

# Appendix: MAEAM potential for copper

## Functional forms
Total energy:
```
E_t = Σ_i F(ρ_i) + ½ Σ_i Σ_{j≠i} φ(r_ij) + Σ_i M(P_i)
```
where
```
ρ_i = Σ_{j≠i} f(r_ij)
P_i = Σ_{j≠i} f²(r_ij)
```

Embedding function:
```
F(ρ_i) = −F₀ [ 1 − n ln(ρ_i/ρ_e) ] (ρ_i/ρ_e)^n
```

Pair potential (r_ij in units of r_{1e}):
```
φ(r_ij) = k₀ + k₁ (r_ij/r_{1e})² + k₂ (r_ij/r_{1e})⁴ + k₃ (r_{1e}/r_ij)¹²
```
with cut‑off at r_ce = r_{2e} + 0.75 (r_{3e} − r_{2e}) (the distance where φ and dφ/dr vanish).

Modified term:
```
M(P_i) = α (P_i/P_e − 1)² exp( −(P_i/P_e − 1)² )
```

Atomic electron density:
```
f(r_ij) = f_e (r_{1e} / r_ij)⁶
```

**Reference density values (equilibrium state)**
The equilibrium electron density ρ_e and the equilibrium squared‑density sum P_e are required to evaluate the embedding function F(ρ_i) and the modified term M(P_i). In a perfect FCC crystal at equilibrium, each atom is surrounded by 12 first‑nearest neighbors at distance r_{1e}. Using the atomic electron density function f(r) evaluated at the nearest‑neighbor distance:
```
f(r_{1e}) = f_e
```
the reference densities are given by:
```
ρ_e = 12 × f_e
P_e = 12 × f_e²
```
Compute f_e from the formula below, then calculate ρ_e and P_e; both are positive constants.

**Atomic mass**
The mass of a copper atom is needed for the MD predictor–corrector integration.
- m = 63.546 u = 1.055 × 10⁻²⁵ kg
- In MD units convenient for this problem (energies in eV, lengths in Å, time in fs):
  m ≈ 6586 eV·fs²/Å². Use this value to convert forces to accelerations.

## Parameters (all in eV and nm unless stated otherwise)
| Symbol | Value | Symbol | Value |
|--------|-------|--------|-------|
| a (lattice constant) | 0.36147 nm | E_c (cohesion) | 3.49 eV |
| E_{1v}^f (isolated vacancy) | 1.17 eV | C₁₁ | 1050 eV nm⁻³ |
| C₁₂ | 760 eV nm⁻³ | C₄₄ | 470 eV nm⁻³ |
| n | 0.2722 | F₀ | 2.32 eV |
| α | 0.0855 eV | k₀ | −0.6011 eV |
| k₁ | 0.4265 eV | k₂ | −0.0721 eV |
| k₃ | 0.0695 eV | f_e | [ (E_c − E_{1v}^f) / Ω ]^{3/5} |
| Ω (atomic volume) | a³ / 4 | r_{1e} (1st nn distance) | a / √2 |
| r_{2e} (2nd nn distance) | a | r_{3e} (3rd nn distance) | √2 a |

The electron density scale factor f_e can be computed from the formula, and r_{1e}, r_{2e}, r_{3e} follow from the FCC lattice.

## Forces
The force on atom i is the negative gradient of the total energy. For the MAEAM potential the α‑component (α = x, y, z) of the force is:

```
f_i^α = − ∂E_t / ∂r_i^α
       = − Σ_{j≠i} [ F'(ρ_i) f'(r_ij) + ½ φ'(r_ij) + 2 M'(P_i) f(r_ij) f'(r_ij) ] · (r_ij^α / r_ij)
```
where r_ij = |**r**_j − **r**_i| and r_ij^α = r_j^α − r_i^α.

The necessary derivatives are:
```
F'(ρ) = −F₀ [ (ρ/ρ_e)^{n-1} / ρ_e ] · { n [1 − n ln(ρ/ρ_e)] − n }   (for ρ > 0)
      = −n F₀ ρ^{-1} (ρ/ρ_e)^{n} [ 1 − n ln(ρ/ρ_e) − 1/n ]   (equivalent form)
```
A simpler, numerically stable form:
```
F'(ρ) = −F₀ · n · (ρ/ρ_e)^n · [ 1/(ρ) − (1/ρ) + ... ]   (derived below)
```
Better to provide the explicit derivative:
```
F'(ρ) = −F₀ [ n ρ^{n-1} ρ_e^{-n} (1 − n ln(ρ/ρ_e)) − (ρ^n ρ_e^{-n}) · (n·ρ_e/ρ)·(1/ρ_e) ]
       = −F₀ n (ρ/ρ_e)^n · [ (1/ρ)(1 − n ln(ρ/ρ_e)) − 1/ρ ]
       = −F₀ n (ρ/ρ_e)^n · [ − n ln(ρ/ρ_e) / ρ ]
       =  F₀ n² (ρ/ρ_e)^n · (ln(ρ/ρ_e)) / ρ
```
However, to avoid confusion, directly implement:
```
F'(ρ) = −F₀ * n * (ρ/ρ_e)^n * ( 1 − n*ln(ρ/ρ_e) − 1 ) / ρ
      =  F₀ * n² * (ρ/ρ_e)^n * ln(ρ/ρ_e) / ρ
```
Use the last expression for compactness, with the convention that F'(ρ) → 0 as ρ → 0 (treat ln(0) as −∞ but the product (ρ)^n ln(ρ) → 0 for n>0, so the limit is 0). Compute carefully.

```
f'(r) = −6 f_e r_{1e}^6 / r^7
```

```
φ'(r) = 2 k₁ r / r_{1e}^2 + 4 k₂ r^3 / r_{1e}^4 − 12 k₃ r_{1e}^{12} / r^{13}
```

```
M'(P) = 2 α (P/P_e − 1) [1 − (P/P_e − 1)^2] exp( −(P/P_e − 1)^2 ) / P_e
```

If a pair distance exceeds the cut‑off r_ce, both φ(r_ij) and its derivative are set to zero; similarly, f(r_ij) and f'(r_ij) are zero for r_ij > r_ce. The sums run only over atoms within the cut‑off.

## MD relaxation (predictor–corrector with damping)
The system is relaxed using a predictor–corrector algorithm derived from Eq. (18) of the paper, augmented with a damping step to quench kinetic energy.

**Integration step** (time step Δt = 1 fs):

1. **Predictor** (advance positions):
   ```
   r_i^p(t+Δt) = r_i(t) + v_i(t) Δt + ½ (f_i(t) / m) Δt²
   ```
   where f_i(t) is the force vector on atom i at time t, and m is the atomic mass (6586 eV·fs²/Å²).

2. **Force evaluation** at predicted positions:
   Compute the force f_i^p = −∇E |_{**r**^p} using the analytical force expression above.

3. **Corrector** (update positions and velocities):
   ```
   r_i(t+Δt) = r_i(t) + v_i(t) Δt + ½ (f_i^p / m) Δt²
   v_i(t+Δt) = v_i(t) + ½ (f_i(t) + f_i^p) / m Δt
   ```
   This is a velocity‑Verlet‑like corrector consistent with the predictor step.

4. **Damping** (to simulate quenched dynamics):
   After each full step, scale all velocities by a damping factor λ, 0 < λ < 1 (e.g., λ = 0.8). This removes kinetic energy and drives the system toward a local energy minimum.

5. **Boundary conditions**: Atoms in the mantle (fixed layer) are never moved; their positions and velocities are held at zero throughout the relaxation.

6. **Convergence**: The relaxation is considered converged when the maximum magnitude of the force on any free atom drops below 1 × 10⁻⁴ eV/Å. At convergence, record the total energy E_t of the free‑atom system (excluding fixed atoms).

Repeat the relaxation for every defect configuration (perfect cell, cell with vacancy, and each intermediate image in the saddle‑point search). The same time step and convergence tolerance must be used throughout.