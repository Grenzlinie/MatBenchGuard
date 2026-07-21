# Surface dielectric response in a local representation: induced charge density calculation

## Problem background
The dielectric response of a surface to an external perturbation is central to many surface phenomena, including chemisorption, work-function changes, and surface excitations. For systems with tightly bound electrons, simple jellium models that neglect lattice-potential effects break down. This work develops a local LCAO/Wannier representation that allows a practical self-consistent calculation of the nonlocal RPA dielectric response of a thin film, fully including local-field and surface-state effects. The model system studied is an 8-layer fcc(001) metal thin film described by a one-orbital s-type tight-binding Hamiltonian. The task is to compute the layer-resolved induced charge density that arises when an external localized perturbation is placed at the surface layer (layer index n=0) or at the second layer (n=1). Two regimes are examined: one that includes only the geometric cutoff at the surface (no surface-state effects), and one that additionally incorporates surface-state effects—differences in effective atomic potentials and orbital decays at the surface layers. The resulting density profiles provide insight into how surface effects modify screening in the surface region.

## Assets

- NumPy: numpy
- SciPy: scipy

## Mathematical formulation

### 1. Electronic structure of the slab

The wave functions of the 8‑layer film are expanded in LCAO’s (or Wannier functions) according to

\[
\psi_{\mathbf{k},k_z}(\mathbf{r}) = \frac{1}{\sqrt{N M}} \sum_{n=0}^{7} \sum_{\mathbf{R}} c_n(\mathbf{k},k_z)\, e^{i\mathbf{k}\cdot\mathbf{R}} \, a(\mathbf{r}-\mathbf{R} - \mathbf{R}_z(n)) ,
\tag{3}
\]

where \(\mathbf{k} = (k_x,k_y)\) is the two‑dimensional wave vector, \(M\) the number of unit cells in each layer and \(a\) a Gaussian orbital

\[
a(\mathbf{r}) = \left(\frac{2\alpha}{\pi}\right)^{3/4} e^{-\alpha r^2} .
\]

For a given \(\mathbf{k}\) the one‑particle Schrödinger equation reduces to an \(8\times8\) eigenvalue problem

\[
\sum_{n'} H_{nn'}(\mathbf{k})\, c_{n'}(\mathbf{k}) = E(\mathbf{k})\, c_n(\mathbf{k}) .
\]

In the model the on‑site energy of a bulk layer is taken as zero ( \(\langle a|H|a\rangle = 0\) ), the nearest‑neighbour hopping is

\[
t \equiv \langle a|H|a'\rangle = -0.272\ \text{eV},
\]

and the band width is \(W = 4.35\ \text{eV}\).  The tight‑binding Hamiltonian of the slab with surfaces at \(n=0\) and \(n=7\) is built as follows (the in‑plane lattice constant is set to \(a_0 = 1\)):

\[
\begin{aligned}
H_{nn}(\mathbf{k}) &= \varepsilon_n + 2t\bigl[\cos(k_x) + \cos(k_y)\bigr], \\[2mm]
H_{n,n+1}(\mathbf{k}) &= H_{n+1,n}(\mathbf{k}) = t \qquad (0\le n \le 6).
\end{aligned}
\]

All other matrix elements are zero.  Diagonalizing \(H(\mathbf{k})\) for each sampled \(\mathbf{k}\) yields the eigenvalues \(E_{\nu}(\mathbf{k})\) and eigenvectors \(c_n^{(\nu)}(\mathbf{k})\).

The **geometric‑only** model uses the bulk on‑site energies for all layers, \(\varepsilon_n = 0\).
The **full surface** model shifts the surface‑layer on‑site energies by \(\Delta\varepsilon = -0.68\ \text{eV}\), i.e.
\(\varepsilon_0 = \varepsilon_7 = -0.68\ \text{eV}\), while the interior layers keep \(\varepsilon_n = 0\).  This shift is the only “surface‑state” effect in the Hamiltonian; the hopping matrix elements remain unchanged.

The slab is half‑filled (Fermi energy at the centre of the band).  To obtain converged results the two‑dimensional Brillouin zone is sampled on a uniform \(N_k\times N_k\) mesh with \(N_k = 256\).

### 2. Form factors (generalised density waves)

The form factor of a local density wave, centred at layer \(n\), is defined as

\[
A_n(\mathbf{q};z) = \int d^2\mathbf{r}\,
a^*\bigl(\mathbf{r};z - R_z(n)\bigr)\,
e^{-i\mathbf{q}\cdot\mathbf{r}}\,
a\bigl(\mathbf{r};z - R_z(n)\bigr) .
\tag{5}
\]

The Gaussian form of the orbital gives an explicit expression:

\[
A_n(\mathbf{q};z) = \left(\frac{2\alpha_n}{\pi}\right)^{3/2}
                 \exp\!\Bigl[-\alpha_n (z - R_z(n))^2\Bigr]
                 \exp\!\Bigl[-\frac{q^2}{4\alpha_n}\Bigr] .
\]

For the **geometric‑only** model all layers have the same decay parameter \(\alpha_n = 0.27\).
For the **full surface** model the surface layers take \(\alpha_0 = \alpha_7 = 0.21\) while interior layers keep \(\alpha_n = 0.27\).

### 3. Proper polarizability matrix \(N\)

In the local representation (RPA, \(\mathbf{G}=\mathbf{G}'=0\), and restricting the index \(s\) to a single layer index \(n\)) the proper polarizability matrix is

\[
N_{nn'}(\mathbf{q}) = \frac{1}{M} \sum_{\mathbf{k},\nu,\nu'}
 \frac{f(E_\nu(\mathbf{k})) - f(E_{\nu'}(\mathbf{k}+\mathbf{q}))}
      {E_\nu(\mathbf{k}) - E_{\nu'}(\mathbf{k}+\mathbf{q}) + i\eta}
 \, c_n^{(\nu)*}(\mathbf{k})\, c_n^{(\nu')}(\mathbf{k}+\mathbf{q})
 \, c_{n'}^{(\nu')*}(\mathbf{k}+\mathbf{q})\, c_{n'}^{(\nu)}(\mathbf{k}) .
\]

Here \(f\) is the zero‑temperature Fermi function, \(\eta\) is an infinitesimal broadening (use \(\eta = 0.01\ \text{eV}\)), and the sum runs over the occupied bands \(\nu\) and unoccupied bands \(\nu'\).  
This formula follows directly from the factorised form (Eq. 4) and the wave‑function expansion (Eq. 3).

### 4. Density‑interaction matrix \(V\)

The Coulomb interaction between two density waves (layers \(n\) and \(n'\)) is

\[
V_{nn'}(\mathbf{q}) = \int dz\int dz'\,
 A_n^*(\mathbf{q};z)\, v(\mathbf{q};|z-z'|)\, A_{n'}(\mathbf{q};z'),
\tag{8}
\]

where the two‑dimensional Fourier transform of the Coulomb potential is

\[
v(\mathbf{q};|z-z'|) = \frac{2\pi}{q}\, e^{-q|z-z'|},
\qquad q = |\mathbf{q}|.
\]

The integrations over \(z\) and \(z'\) can be performed analytically with the Gaussian form factors given above.

### 5. Self‑consistent response and induced charge density

The RPA density‑response function in the factorised representation is

\[
\chi_{\omega}(\mathbf{q};z,z') = \sum_{n,n'} A_n(\mathbf{q};z)\, S^{-1}_{nn'}(\mathbf{q})\, A_{n'}^*(\mathbf{q};z'),
\qquad
S^{-1} = N\,(1 - V N)^{-1}.
\tag{7}
\]

The external perturbation is taken as a δ‑function in the \(z\) direction localised at layer \(n_{\rm pert}\):

\[
V_{\rm ext}(\mathbf{r}) = \delta\bigl(z - R_z(n_{\rm pert})\bigr)\, e^{-i\mathbf{q}\cdot\mathbf{r}} .
\]

Projecting this external potential onto the density‑wave basis gives the induced charge density

\[
\rho^{\rm ind}(\mathbf{q},z) =
\sum_{n,n'} A_n(\mathbf{q};z)\, S^{-1}_{nn'}(\mathbf{q})\, \bar A_{n'}(n_{\rm pert}) ,
\]

where

\[
\bar A_{n'}(n_{\rm pert}) =
\int dz'\, A_{n'}^*(\mathbf{q};z')\, \delta(z' - R_z(n_{\rm pert})) .
\]

Because the δ‑function picks out the value of the form factor at the layer position, the layer‑resolved induced density (integrated or sampled at the layer position \(z = R_z(m)\)) reduces to

\[
\rho^{\rm ind}_m = \sum_{n} A_n(\mathbf{q};R_z(m))\,
                  \bigl[ S^{-1} \bigr]_{n,\,n_{\rm pert}} .
\]

In practice it is sufficient to evaluate \(\rho^{\rm ind}_m\) at the layer positions, i.e. at \(z = R_z(m)\), for \(m = 0,\dots,7\).  
For the task the fixed wave‑vector is

\[
\mathbf{q} = \Bigl(\frac{\pi}{32}, 0\Bigr) .
\]

### 6. Normalisation

All four induced‑density profiles (geometric / full, perturbations at \(n_{\rm pert}=0\) and \(n_{\rm pert}=1\)) must be placed on a common relative scale.  Set the normalisation factor so that **the induced density at the surface layer (layer 0) for the geometric‑only model with the perturbation at the surface layer (\(n_{\rm pert}=0\)) is exactly 1.0**.  Apply the same factor to all other profiles.

## Reproduction target

Compute the layer‑resolved induced charge density for an 8‑layer fcc(001) metal thin film under four distinct scenarios and write the results to a CSV file. The four scenarios are:
- geometric‑only model, perturbation at the surface layer (n = 0),
- geometric‑only model, perturbation at the second layer (n = 1),
- full surface model (including on‑site shift and orbital changes), perturbation at the surface layer (n = 0),
- full surface model, perturbation at the second layer (n = 1).

The final artifact must be a file named `induced_density.csv` containing 8 rows (layers 0 through 7) and the columns: `layer` (int), `rho_geo_n0` (float), `rho_full_n0` (float), `rho_geo_n1` (float), `rho_full_n1` (float).

## Workflow steps

### Step 1: Tight‑binding eigenstates for full surface model
- Role: process
- Action: Solve the tight‑binding Hamiltonian for the 8‑layer slab using the full surface‑state parameters: surface on‑site shift –0.68 eV, Gaussian decay \(\alpha_s=0.21\) for surface layers and \(\alpha=0.27\) for interior layers. Use a one‑orbital s‑type model with half‑filled band of width \(W=4.35\ \mathrm{eV}\) and nearest‑neighbour hopping \(t = -0.272\ \mathrm{eV}\). Sample the 2D Brillouin zone uniformly on a \(256\times 256\) grid. Store the eigen‑energies and wave‑function coefficients internally.

### Step 2: Form factors \(A_n\) for full model
- Role: process
- Action: Compute the form factors \(A_n(\mathbf{q};z)\) using the Gaussian Wannier functions with decay parameters \(\alpha_s=0.21\) (surfaces) and \(\alpha=0.27\) (interior). Use the one‑site overlap formula given in the Mathematical formulation and the fixed wave‑vector \(\mathbf{q} = (\pi/32, 0)\).

### Step 3: Polarizability matrix \(N\) (full model)
- Role: process
- Action: Construct the proper polarizability matrix \(N_{nn'}(\mathbf{q})\) by performing the k‑space integration over the \(256\times 256\) mesh using the Fermi occupation (Fermi level at half‑filling) and the energies/coefficients from step 1.

### Step 4: Density‑interaction matrix \(V\) (full model)
- Role: process
- Action: Compute the density‑interaction matrix \(V_{nn'}(\mathbf{q})\) by evaluating the integrals over \(z\) and \(z'\) with the Coulomb interaction \(2\pi/q\, e^{-q|z-z'|}\) and the form factors from step 2.

### Step 5: Induced charge density profiles (full model)
- Role: process
- Action: Form the matrix \(S^{-1} = N\,(1 - V N)^{-1}\) and calculate the layer‑resolved induced charge densities for perturbations at \(n_{\rm pert}=0\) and \(n_{\rm pert}=1\) according to the formula for \(\rho^{\rm ind}_m\) given in the Mathematical formulation.

### Step 6: Tight‑binding eigenstates for geometric‑only model
- Role: process
- Action: Repeat the tight‑binding solve of step 1 but with surface‑state effects turned off: set the surface on‑site shift to zero and use the same decay parameter \(\alpha_n = 0.27\) for all layers. All other bulk parameters remain identical.

### Step 7: Form factors \(A_n\) for geometric‑only model
- Role: process
- Action: Recompute the form factors using \(\alpha=0.27\) for every layer, with the same wave‑vector \(\mathbf{q} = (\pi/32, 0)\).

### Step 8: Polarizability matrix \(N\) (geometric‑only)
- Role: process
- Action: Reconstruct \(N_{nn'}(\mathbf{q})\) using the geometric‑only eigenstates and the same k‑space integration procedure as step 3.

### Step 9: Density‑interaction matrix \(V\) (geometric‑only)
- Role: process
- Action: Reconstruct \(V_{nn'}(\mathbf{q})\) using the geometric‑only form factors.

### Step 10: Induced charge density profiles (geometric‑only)
- Role: process
- Action: Compute the induced charge densities for perturbations at \(n_{\rm pert}=0\) and \(n_{\rm pert}=1\) using the geometric‑only \(N\), \(V\) and form factors, analogous to step 5.

### Step 11: Write scored CSV
- Role: scored (load‑bearing)
- Action: Assemble the four induced charge density profiles (geometric and full for \(n_{\rm pert}=0\) and \(n_{\rm pert}=1\)) into a CSV file `induced_density.csv`. Normalise all profiles to the scale defined in the Mathematical formulation (geometric‑only, perturbation on layer 0 → layer 0 density = 1.0). The CSV must have 8 rows (layers 0–7) and columns: `layer` (int), `rho_geo_n0` (float), `rho_full_n0` (float), `rho_geo_n1` (float), `rho_full_n1` (float).
- Output file: `/app/outputs/induced_density.csv`
- Format: csv
- Contract: 8 rows, columns: layer (int), rho_geo_n0 (float), rho_full_n0 (float), rho_geo_n1 (float), rho_full_n1 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/induced_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### induced_density.csv
- path: `/app/outputs/induced_density.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Layer‑resolved induced charge densities for an 8‑layer slab under four scenarios: perturbation at surface layer (n=0) and second layer (n=1), with geometric‑only and full surface effects. Values are normalised to a relative scale where the geometric‑only, n=0 perturbation gives a surface‑layer density of 1.0.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `rho_geo_n0`, `rho_full_n0`, `rho_geo_n1`, `rho_full_n1`
  - `items`:
    - `layer`: int
    - `rho_geo_n0`: float
    - `rho_full_n0`: float
    - `rho_geo_n1`: float
    - `rho_full_n1`: float

Notes: The densities are normalised to a common scale such that the geometric‑only model with perturbation on layer 0 yields exactly 1.0 at layer 0. The checker will compare the submitted values to hidden reference values digitised from the paper’s Fig. 1 and verify the trend that surface effects reduce the induced density at the surface.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "induced_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "rho_geo_n0",
          "rho_full_n0",
          "rho_geo_n1",
          "rho_full_n1"
        ],
        "items": {
          "layer": "int",
          "rho_geo_n0": "float",
          "rho_full_n0": "float",
          "rho_geo_n1": "float",
          "rho_full_n1": "float"
        }
      },
      "description": "Layer‑resolved induced charge densities for an 8‑layer slab under four scenarios: perturbation at surface layer (n=0) and second layer (n=1), with geometric‑only and full surface effects. Values are normalised to a relative scale."
    }
  ],
  "notes": "The densities are normalised such that the geometric-only n=0 perturbation gives 1.0 at layer 0. The checker will compare the submitted values to hidden reference values digitised from that figure and verify the trend that surface effects reduce the induced density at the surface."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that reads `induced_density.csv`. The verifier compares the layer‑resolved induced charge densities you report to hidden reference values (digitised from the published figure) using an appropriate tolerance on the normalised scale. In addition, the verifier checks that the inclusion of surface‑state effects reduces the induced charge density at the surface layer relative to the geometric‑only case—a structural trend that the correct physics must satisfy. The overall reward is a weighted combination of per‑scenario comparisons and the trend check. Simply reporting expected numbers without performing the genuine calculation will not achieve a high score. The verifier runs in a separate environment and has no access to your code.