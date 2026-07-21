# Phonon-softening model for Tc enhancement in 2D superconductors

## Problem background
Superconductivity in low-dimensional systems is sensitive to phonon softening at surfaces and edges, which can alter the electron‑phonon coupling and, in turn, the superconducting transition temperature. In this task, we investigate how the geometry of a two‑dimensional superconducting layer — flat sheet, hollow sphere, hollow cylinder — influences the average transition temperature relative to the bulk, using a classical spring‑network model of collective lattice vibrations within coherence volumes.

## Approach
The superconducting layer is discretized into a grid of coherence volumes, each assigned a collective spring constant of 1. For each grid point, an effective spring constant is computed by combining the springs of its nearest neighbours according to classical series and parallel rules, both in the 2D plane and in a thick 3D block that serves as a bulk reference. The ratio of the bulk reference stiffness to the 2D stiffness quantifies the local phonon softening. Under the assumption of a position‑independent Debye frequency and BCS proportionality, the local superconducting transition temperature ratio relative to the 3D (bulk) reference is given by \( R(x,y)^{0.25} \), where \( R(x,y) = k^{(3D)}(x,y,400)/k^{(2D)}(x,y) \).

For the curved geometries (hollow sphere, hollow cylinder) the ionic charge is first corrected by the ratio of the Coulomb potential in the curved geometry to that in the flat sheet (\( U_{\text{curved}}/U_{\text{flat}} \)). The local Tc ratio is then multiplied by this charge correction factor, because the electron‑phonon coupling is proportional to the ionic charge. Averaging the local Tc ratios over the surface yields the macroscopic average \( \langle T_c \rangle / T_{c,\text{bulk}} \) ratio for each geometry.

## Reproduction target
Produce a JSON file `tc_ratios.json` containing the five average Tc/Tc_bulk ratios: the entire 800×800 rectangular film (`rectangle_mean`), its four edges (`rectangle_edges`), its four corners (`rectangle_corners`), a hollow sphere of radius 127 coherence lengths and thickness 1 (`sphere`), and a hollow cylinder of length 800, radius 127, thickness 1 (`cylinder`).

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Define 2D grid for flat sheet
- Role: process
- Action: Set up an 800×800 (indices 0..799 in x and y) grid of coherence volumes to represent the 2D rectangular superconducting film. The x axis points to the right, the y axis points upward. Every grid point has local spring constant 1 and is connected to its four nearest in‑plane neighbours (left, right, up, down). Points on the grid boundaries have missing neighbours in the outward direction.
- Evidence: none

### Step 2: Compute effective spring constant \( k^{(2D)}(x,y) \) for the flat sheet
- Role: process
- Action: For each grid point \((x,y)\), compute its net effective spring constant using the classical series/parallel rules together with vector addition, as described in the paper:

  1.  **Series along each direction** – treat all springs along a straight path from the point to the grid boundary (moving only along rows or columns) as connected in series. The reciprocal of the net spring constant of a path is the sum of the reciprocals of the individual spring constants along that path. Because every spring has constant 1, the net spring constant in a given direction is \( 1/N \), where \( N \) is the number of springs in that path. If the point lies on a boundary, the outward path has zero length and contributes a stiffness of 0.
      - Left path:   \( N_{\text{left}}  = x  \)  →  \( k_{\text{left}}  = 1/x  \) (if \(x>0\), else 0)
      - Right path:  \( N_{\text{right}} = 799 - x \)  →  \( k_{\text{right}} = 1/(799-x) \) (if \(x<799\), else 0)
      - Down path:   \( N_{\text{down}}  = y  \)  →  \( k_{\text{down}}  = 1/y  \) (if \(y>0\), else 0)
      - Up path:     \( N_{\text{up}}    = 799 - y \)  →  \( k_{\text{up}}    = 1/(799-y) \) (if \(y<799\), else 0)

  2.  **Parallel combination in x and y** – the paths to the left and to the right act in parallel when the point is displaced horizontally, so the total x‑stiffness is \( k_x = k_{\text{left}} + k_{\text{right}} \). Similarly, \( k_y = k_{\text{down}} + k_{\text{up}} \).

  3.  **Vector addition** – the effective overall spring constant at \((x,y)\) is the magnitude of the two‑dimensional stiffness vector:
      \[
      k^{(2D)}(x,y) = \sqrt{k_x^{2} + k_y^{2}} .
      \]
      (The justification is that displacements are vectors and the restoring force from orthogonal spring sets obeys the Pythagorean relation for isotropic media.)

- Evidence: none

### Step 3: Compute 3D reference spring constant \( k^{(3D)}(x,y,400) \)
- Role: process
- Action: Extend the grid into a 3D block of size 800 × 800 × 400 (indices 0..799 in x, 0..799 in y, 0..399 in z). Each grid point again has spring constant 1 and is connected to its six nearest neighbours (\(\pm x\), \(\pm y\), \(\pm z\)). To obtain the bulk‑like stiffness reference at lateral position \((x,y)\), pick the middle z‑plane, \(z = 199\). Apply the same series/parallel/vector‑addition procedure, now with three orthogonal directions.

  1.  **Series paths** – distances to the block faces (in grid units):
      - Left/right and down/up paths are the same as in the 2D case.
      - Back (\(-z\)) path: \( N_{\text{back}} = 199 \) → \( k_{\text{back}} = 1/199 \)
      - Front (\(+z\)) path: \( N_{\text{front}} = 199 \) → \( k_{\text{front}} = 1/199 \)

  2.  **Parallel combination** –
      \[
      k_x = k_{\text{left}} + k_{\text{right}},\quad
      k_y = k_{\text{down}} + k_{\text{up}},\quad
      k_z = k_{\text{back}} + k_{\text{front}} .
      \]

  3.  **Vector addition** –
      \[
      k^{(3D)}(x,y,400) = \sqrt{k_x^{2} + k_y^{2} + k_z^{2}} .
      \]

- Evidence: none

### Step 4: Compute local stiffness ratio and Tc ratio map for the flat sheet
- Role: process
- Action: Calculate the stiffness ratio
  \[
  R(x,y) = \frac{k^{(3D)}(x,y,400)}{k^{(2D)}(x,y)} .
  \]
  Under the assumption of a position‑independent Debye frequency, the BCS relation (Eq. (15) in the paper) gives the local transition temperature ratio relative to the 3D reference as
  \[
  \frac{T_c(x,y)}{T_{c,\text{bulk}}} = \bigl[ R(x,y) \bigr]^{0.25} .
  \]
  Compute this ratio for every grid point and store the full 800×800 map.

- Evidence: none

### Step 5: Extract mean, edge, and corner averages for the rectangular film
- Role: process
- Action: Using the Tc‑ratio map from Step 4:
  - **Whole rectangle**: average over all 800×800 points → `rectangle_mean`.
  - **Edges**: points that lie on the perimeter but are **not corners**. Formally,
    \[
    \text{Edges} = \{ (x,y) \mid x=0 \text{ or } x=799 \text{ or } y=0 \text{ or } y=799 \}
    \setminus \{ (0,0), (0,799), (799,0), (799,799) \} .
    \]
    Average over these 4×(798) = 3192 points (exact count) → `rectangle_edges`.
  - **Corners**: the four points (0,0), (0,799), (799,0), (799,799). Average → `rectangle_corners`.

- Evidence: none

### Step 6: Compute curvature correction for the hollow sphere
- Role: process
- Action:
  1.  **Coulomb potential sum for a flat sheet** – evaluate the total Coulomb potential at the centre of the 800×800 flat grid (or at any interior point; the centre serves as a representative bulk‑like location). Sum the \(1/r\) contributions from all other grid points:
      \[
      U_{\text{flat}} = \sum_{(x',y')\neq (x_c,y_c)} \frac{1}{\sqrt{(x'-x_c)^2 + (y'-y_c)^2}} .
      \]
      The centre is \( (x_c,y_c) = (399.5, 399.5) \) – a continuous coordinate at the centre of the domain. Use the real‑valued distance; the spring‑network discretisation is irrelevant for this electrostatic calculation. You may sum over integer indices but offset the coordinates to place the centre at (399, 399) or (399.5,399.5); the result scales trivially and the ratio cancels the overall length unit. To avoid infinity, exclude the point itself (small shift, e.g., replace the self‑term by a regularisation of order 1 that drops out in the ratio).

  2.  **Coulomb potential sum for a sphere** – model a hollow sphere of radius \(R_s = 127\) (in units of coherence length) and one coherence length thickness. Treat the sphere surface as a continuum; discretise it with an approximately equal‑area grid of \(N_{\text{sphere}} \approx 640\,000\) points (same total number as the flat sheet, i.e. \(800\times 800\)) using a Fibonacci lattice or an icosahedral mesh to ensure uniform coverage. For a set of points \(\{\mathbf{r}_i\}\) on the unit sphere rescaled by \(R_s\), the potential at any one point (all points are equivalent) is
      \[
      U_{\text{sphere}} = \frac{1}{2}\sum_{j\neq i} \frac{1}{|\mathbf{r}_i - \mathbf{r}_j|} ,
      \]
      where the distance \(|\mathbf{r}_i - \mathbf{r}_j|\) is the straight‑line chord distance (or, equivalently, the arc length up to a constant factor; the ratio is unaffected because the relationship is monotonic). The factor 1/2 avoids double‑counting if the sum is over all pairs, but it cancels in the ratio \(U_{\text{sphere}}/U_{\text{flat}}\) if the flat sum is defined consistently, so it may be omitted. Use the chord distance:
      \[
      |\mathbf{r}_i - \mathbf{r}_j| = 2R_s \sin(\theta_{ij}/2) ,
      \]
      where \(\theta_{ij}\) is the central angle between the points.

  3.  **Curvature correction factor**:
      \[
      f_{\text{sphere}} = \frac{U_{\text{sphere}}}{U_{\text{flat}}} .
      \]

  4.  **Local Tc ratio for the sphere** – because a sphere has no boundaries, the stiffness ratio \(R\) is homogeneous and equal to the bulk (3D)‑to‑2D ratio evaluated under periodic boundary conditions. To a very good approximation, one may use the same \(R\) that would be obtained for a 2‑infinite plane without boundaries, i.e. the limit of large system size. This limiting value can be computed by taking the flat‑sheet \(R\) at the centre \((399,399)\) of the 800×800 grid (which is the farthest from edges). Thus
      \[
      \frac{T_c^{\text{local}}}{T_{c,\text{bulk}}}\Big|_{\text{sphere}} \approx
      \bigl[ R_{\text{centre}} \bigr]^{0.25} \times f_{\text{sphere}} .
      \]
      The average over the sphere surface simply equals this constant value → output `sphere`.

  - Evidence: none

### Step 7: Compute curvature correction for the hollow cylinder
- Role: process
- Action:
  1.  **Coulomb potential sum on a cylinder** – a hollow cylinder of length \(L=800\) and radius \(R_c = 127\), thickness 1 coherence length. Discretise the surface with \(800\times 800\) points, using a regular grid: \(z \in [0, L]\) in steps of 1 (801 points; adjust to exactly 800 points by taking \(z_k = (k+0.5)L/800\) for \(k=0,\dots,799\)), and azimuthal angle \(\phi\) uniform. The potential at a point \((z,\phi)\) is symmetric under translation in \(z\) and rotation, so it depends only on the distance to the nearer end. Compute the potential as a function of \(z\):
      \[
      U_{\text{cyl}}(z) = \sum_{(z',\phi') \neq (z,\phi)} \frac{1}{\sqrt{ (z-z')^2 + 2R_c^2[1-\cos(\phi-\phi')] }} .
      \]
      Then average over all \(z\) (or, because the potential is \(z\)‑dependent and we need the ratio to the flat value, average the per‑point ratio). Obtain the mean ratio
      \[
      f_{\text{cylinder}} = \frac{\langle U_{\text{cyl}} \rangle}{U_{\text{flat}}} .
      \]
      Here \(\langle U_{\text{cyl}} \rangle\) is the spatial average of \(U_{\text{cyl}}(z)\) over the cylinder length.

  2.  **Local Tc ratio for the cylinder** – the cylinder has open ends in the \(z\) direction (like the flat sheet) and periodic boundary in the \(\phi\) direction. Therefore the effective stiffness \(R\) varies only along the axial direction and is identical to the flat‑sheet \(R\) for a strip of width 800 with periodic boundary conditions in the transverse direction. A practical approximation for the present purpose is to use the same centre‑point \(R_{\text{centre}}\) as for the sphere (since the open ends produce only a weak modulation far from the ends). Then the local Tc ratio at axial position \(z\) is
      \[
      \frac{T_c(z)}{T_{c,\text{bulk}}} \approx
      \bigl[ R_{\text{centre}} \bigr]^{0.25} \times \frac{U_{\text{cyl}}(z)}{U_{\text{flat}}} .
      \]
      Average this quantity over all \(z\) (or, equivalently, multiply the average \(f_{\text{cylinder}}\) by \([R_{\text{centre}}]^{0.25}\)) → output `cylinder`.

  - Evidence: none

### Step 8: Write Tc ratios to tc_ratios.json
- Role: scored (load-bearing)
- Action: Collect the five computed average Tc/Tc_bulk ratios:
  - `rectangle_mean` (from Step 5)
  - `rectangle_edges` (from Step 5)
  - `rectangle_corners` (from Step 5)
  - `sphere` (from Step 6)
  - `cylinder` (from Step 7)
  Write these to `/app/outputs/tc_ratios.json` as a JSON object.
- Output file: `/app/outputs/tc_ratios.json`
- Format: json
- Contract: A JSON object with five keys: `rectangle_mean` (float), `rectangle_edges` (float), `rectangle_corners` (float), `sphere` (float), `cylinder` (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_ratios.json
- path: `/app/outputs/tc_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Average superconducting transition temperature ratios for the rectangular film (mean, edges, corners), hollow sphere, and hollow cylinder, relative to bulk Tc.
- schema:
  - `type`: object
  - `required_keys`:
    - `rectangle_mean`: float
    - `rectangle_edges`: float
    - `rectangle_corners`: float
    - `sphere`: float
    - `cylinder`: float

Notes: The ratios are computed from the local Tc distribution derived from the spring-network model. Exact reproduced values depend on the correct implementation of series/parallel rules and curvature corrections; the checker will compare against the paper's reported ratios with an appropriate hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": {
          "rectangle_mean": "float",
          "rectangle_edges": "float",
          "rectangle_corners": "float",
          "sphere": "float",
          "cylinder": "float"
        }
      },
      "description": "Average superconducting transition temperature ratios for the rectangular film (mean, edges, corners), hollow sphere, and hollow cylinder, relative to bulk Tc."
    }
  ],
  "notes": "The ratios are computed from the local Tc distribution derived from the spring-network model. Exact reproduced values depend on the correct implementation of series/parallel rules and curvature corrections; the checker will compare against the paper's reported ratios with an appropriate hidden tolerance."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/tc_ratios.json` and compare each of the five ratio values against independently determined reference values using a hidden tolerance. Your final reward is proportional to the number of ratios that fall within the tolerance (each ratio contributes equally). You must obtain