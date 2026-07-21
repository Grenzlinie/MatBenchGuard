# Step tension and stiffness in adsorbate-coupled RSOS model via PWFRG

## Problem background
Vicinal surfaces below the roughening temperature are often described by the GMPT universal class, where the surface free energy expands as \( f(p) = f(0) + \gamma p + B p^3 + \dots \) with step tension \(\gamma\) and step interaction coefficient \(B\). Adsorption of atoms on the surface can couple to step energetics and may alter this expansion, potentially leading to a temperature where \(B\) vanishes. This task studies a restricted solid-on-solid (RSOS) model on a square lattice coupled to an Ising model representing adsorbate atoms. The goal is to compute the step tension \(\gamma\) and step stiffness \(\tilde{\gamma}\) as functions of temperature for a particular set of coupling parameters, and to determine the temperature dependence of the coefficient \(B\) (via the quadratic fitting coefficient \(A_2\)).

## Model Hamiltonian
The RSOS-Ising coupled model is defined by the Hamiltonian

\[
\mathcal{H} = \sum_{\langle i,j\rangle} \epsilon \bigl(1 - \alpha \sigma_{b(i,j)}\bigr) |h_i - h_j| \;-\; J \sum_{\langle b,b'\rangle} \sigma_b \sigma_{b'},
\]

where:
- \(h_i \in \mathbb{Z}\) is the surface height at site \(i\) of a square lattice; the RSOS condition restricts \(|h_i - h_j| \le 1\) for all nearest-neighbour (nn) pairs \(\langle i,j\rangle\).
- \(\epsilon\) is the bare ledge energy; we work in units of \(\epsilon\) and set \(\epsilon = 1\).
- \(\alpha\) is the adsorption-induced modification parameter. We fix \(\alpha = 0.5\).
- \(\sigma_{b(i,j)} \in \{+1,-1\}\) is an Ising spin variable located on the bond \(b(i,j)\) that connects sites \(i\) and \(j\). The Ising spins therefore live on the bonds of the original square lattice, forming a \(45^\circ\)-rotated square lattice.
- \(J\) is the ferromagnetic Ising coupling (attractive interaction in the lattice-gas picture). We take \(J = 0.15\) (in units where \(\epsilon=1\)).
- The first sum runs over all nn site pairs; the second sum runs over all nn bond pairs \(\langle b,b'\rangle\) on the rotated Ising lattice.

The Boltzmann factor is \(e^{-\beta \mathcal{H}}\) with \(\beta = 1/(k_B T)\). We use energy units where \(k_B = 1\) and \(\epsilon = 1\), so temperatures are given as \(T\) (i.e. \(k_B T/\epsilon\)).

## Transfer-matrix / vertex-model mapping
To analyse the model we construct a transfer matrix. Following the standard mapping of the RSOS model to a 6-state vertex model and its extension to a decorated vertex model with Ising spins, we define a vertex at each elementary square. Each vertex involves four heights \(h_1, h_2, h_3, h_4\) (in cyclic order) and four Ising spins \(\sigma_{12}, \sigma_{23}, \sigma_{34}, \sigma_{14}\) located on the four edges of the square.

The local energy contributed by one vertex is **one half** of the energy of each of its four edges, because every edge is shared by two adjacent vertices. The total Hamiltonian can be written as a sum of vertex contributions
\[
\mathcal{H} = \sum_{\text{vertices } v} E_v,
\]
where
\[
E_v = \frac{\epsilon}{2} \sum_{k=1}^{4} (1 - \alpha \sigma_k) |\Delta h_k|
      - \frac{J}{2} \bigl( \sigma_{12}\sigma_{23} + \sigma_{23}\sigma_{34} + \sigma_{34}\sigma_{14} + \sigma_{14}\sigma_{12} \bigr).
\]
Here \(\Delta h_k\) are the height differences along the four edges (with the convention that positive orientation gives the absolute value). The four Ising spins on the vertex edges are denoted \(\sigma_{12}\) (between sites 1 and 2), \(\sigma_{23}\) (between 2 and 3), \(\sigma_{34}\) (between 3 and 4) and \(\sigma_{14}\) (between 1 and 4). The Ising term sums the products of the four nearest-neighbour spin pairs belonging to this vertex (each bond between two adjacent spins is shared by two vertices, hence the factor \(1/2\)).

A vertex configuration is specified by \((h_1,h_2,h_3,h_4; \sigma_{12},\sigma_{23},\sigma_{34},\sigma_{14})\). The RSOS condition constrains \(|h_i - h_j| \le 1\) on every edge, which yields 19 possible height configurations (up to an overall shift). Combined with \(2^4 = 16\) spin configurations, there are \(19 \times 16 = 304\) non-zero vertex weights. The local Boltzmann weight is
\[
W(v) = \exp\bigl[-\beta E_v\bigr].
\]
These weights form the elements of the transfer matrix. When building the transfer matrix, adjacent vertices share one edge (height and spin), so the product of weights along a row correctly reconstructs the total Boltzmann factor up to boundary terms.

In the actual computation you should represent the transfer matrix as a matrix acting on a product space of a left block and a right block, but the fundamental building block is this 304-weight vertex model.

## Tilted system: Andreev field \(\eta\)
To tilt the surface we impose a gradient along the \(x\)-direction. This is done by adding an “Andreev field” term to the Hamiltonian:
\[
\mathcal{H}_\eta = -\eta \sum_{m,n} (h_{(m+1,n)} - h_{(m,n)}),
\]
where \((m,n)\) indexes the lattice sites. In the vertex representation this adds, for each vertex, a contribution
\[
E_v^\eta = E_v - \frac{\eta}{2} \Bigl[ (h_{(m+1,n)} - h_{(m,n)}) + (h_{(m+1,n+1)} - h_{(m,n+1)}) \Bigr],
\]
where we label the four heights such that \(h_1 = h_{(m,n)}\), \(h_2 = h_{(m+1,n)}\), \(h_3 = h_{(m+1,n+1)}\), \(h_4 = h_{(m,n+1)}\). Thus the vertex weight becomes
\[
W_\eta(v) = \exp\bigl[-\beta E_v^\eta\bigr].
\]
The surface gradient \(p\) (along \(x\)) is the thermodynamic expectation value of the height difference per step:
\[
p = \langle h_{(m+1,n)} - h_{(m,n)} \rangle.
\]
In the vertex-model language this is the thermal average of the “vertical” edge variable (the edge connecting \(h_1\) and \(h_2\)). Given the fixed-point wavefunction (the dominant eigenvector of the transfer matrix for infinite length), \(p\) is computed as
\[
p = \frac{ \langle \Psi | \hat{p} | \Psi \rangle }{ \langle \Psi | \Psi \rangle },
\]
where \(\hat{p}\) acts diagonally on the vertex configurations: for a configuration with height difference \(\Delta h_x = h_2 - h_1\), the eigenvalue is \(\Delta h_x\). Alternatively, you can average the vertical height difference over the vertex states weighted by \(|\Psi|^2\).

## PWFRG algorithm
We use the product-wavefunction renormalisation group (PWFRG) method, which is an infinite-system DMRG variant designed to efficiently find the fixed point (thermodynamic limit) of a one-dimensional transfer matrix. The algorithm proceeds as follows:

1. **Initialisation**: Start with a “system” block (left) and an “environment” block (right), each represented by a small number of lattice columns (e.g., one column). Construct the initial block transfer matrices from the vertex weights.
2. **Superblock construction**: Combine the system block, a single central vertex column, and the environment block to form a superblock. The superblock transfer matrix acts on the product space of the block states and the vertex degrees of freedom.
3. **Diagonalisation**: Compute the dominant eigenvalue and the corresponding right eigenvector \(|\Psi\rangle\) of the superblock transfer matrix (or of the symmetrised version, depending on implementation).
4. **Density matrix**: Form the reduced density matrix by tracing out the environment degrees of freedom: \(\rho = \mathrm{Tr}_E |\Psi\rangle \langle \Psi|\).
5. **Truncation**: Diagonalise \(\rho\) and retain the \(m\) largest eigenvalues and their eigenstates. These form the new optimised basis for the system block. A typical value is \(m = 32\)–\(64\); larger \(m\) improves accuracy. The PWFRG method retains the bases for both the system and the environment in a symmetric way (or uses the product wavefunction ansatz).
6. **Block extension**: Construct the new, enlarged system block by adding one central column and projecting onto the retained basis. Similarly update the environment block.
7. **Iteration**: Repeat steps 2–6, gradually increasing the system length. The process converges to a fixed point where the block transfer matrices and the dominant eigenvector no longer change (within tolerance).
8. **Fixed-point wavefunction**: The final superblock eigenvector is the fixed-point wavefunction. The number of iterations needed is typically a few hundred. Monitor the convergence of the dominant eigenvalue or the wavefunction overlap.

The PWFRG fixed-point wavefunction contains the full information about the thermodynamic state. For each value of the Andreev field \(\eta\) and temperature \(T\), you run the PWFRG to convergence and then extract \(p\) as described above.

## Extraction of step tension and stiffness
For a given temperature \(T\), run the PWFRG for a set of \(\eta\) values (e.g. a grid from negative to positive sufficient to obtain \(p\) values roughly in the range \([-0.3, 0.3]\)). Record the data pairs \((\eta, p)\). Next, fit the \(\eta\) vs. \(p\) data to a polynomial (theoretical form for the Andreev field):
\[
\eta = A_0 + A_2 p^2 + A_3 p^3 + A_4 p^4.
\]
Use ordinary least squares. The step tension is then \(\gamma = A_0\). The step stiffness for the direction \(\theta=0\) is obtained from the relation
\[
\tilde{\gamma}(0) = \frac{\pi^2 (k_B T)^2}{2 A_2}.
\]
Note: \(k_B = 1\) in our units.

Perform this analysis for five temperatures: \(T = 0.3, 0.35, 0.4, 0.45, 0.5\). The extracted \(\gamma\), \(A_2\) and \(\tilde{\gamma}\) are the scored outputs.

## Reproduction target
Produce a CSV file `step_properties.csv` containing the computed step tension \(\gamma\) (gamma), quadratic coefficient \(A_2\), and step stiffness \(\tilde{\gamma}\) (gamma_tilde) for the five temperatures \(T = 0.3, 0.35, 0.4, 0.45, 0.5\). All computations must follow the PWFRG procedure described above.

## Assets

- Python 3 (>=3.8): https://www.python.org
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Map RSOS-Ising model to vertex model
- Role: process
- Action: Implement the construction of the vertex weights as described in the “Transfer-matrix / vertex-model mapping” section. Loop over all 304 non-zero configurations, compute \(E_v\) (and \(E_v^\eta\) when the Andreev field is non-zero), and store the weights. Save a summary description of the vertex model.
- Evidence: `/app/outputs/vertex_model_description.json` – a JSON file with at least the keys `"model_type"` (value `"decorated_6-state_vertex_model"`), `"nonzero_weights"` (value 304), and `"parameters"` (object containing `"epsilon": 1.0, "alpha": 0.5, "J": 0.15`).

### Step 2: Run PWFRG to obtain fixed-point wavefunctions
- Role: process
- Action: Implement the PWFRG algorithm as described. For each of the five temperatures \(T = 0.3, 0.35, 0.4, 0.45, 0.5\) and for a suitable set of \(\eta\) values (e.g. a dense grid covering \(-0.5 \le \eta \le 1.5\)), iterate the transfer matrix to convergence and obtain the fixed-point wavefunction. Choose a retained basis size \(m\) (e.g. 32 or 64) and record convergence information.
- Evidence: `/app/outputs/pwfrg_fixedpoint_info.log` – a plain text log containing, for each \((T,\eta)\), the number of iterations until convergence and the final retained basis size.

### Step 3: Compute p(η) curves
- Role: process
- Action: For each temperature and η value, compute the expectation value \(p\) from the fixed-point wavefunction as described (average of vertical height difference). Save all data points \((T, \eta, p)\).
- Evidence: `/app/outputs/p_eta_curves.csv` – CSV with columns `temperature`, `eta`, `p`.

### Step 4: Fit η(p) and extract step properties
- Role: scored (load-bearing)
- Action: For each temperature, fit the \((p, \eta)\) data to \(\eta = A_0 + A_2 p^2 + A_3 p^3 + A_4 p^4\) using least squares. Set \(\gamma = A_0\) and compute \(\tilde{\gamma}(0) = \pi^2 T^2 / (2 A_2)\). Write the results to `step_properties.csv`.
- Output file: `/app/outputs/step_properties.csv`
- Format: csv
- Contract: Header: `temperature,gamma,A2,gamma_tilde`. `temperature`: float (units \(k_B T/\epsilon\)); `gamma`: float (units \(\epsilon\)); `A2`: float (coefficient in \(\eta(p)\) polynomial); `gamma_tilde`: float (units \(\epsilon\)). Rows for temperatures \(0.3, 0.35, 0.4, 0.45, 0.5\).

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vertex_model_description.json` (evidence)
- `/app/outputs/pwfrg_fixedpoint_info.log` (evidence)
- `/app/outputs/p_eta_curves.csv` (evidence)
- `/app/outputs/step_properties.csv` (scored)

## Output contract
Every output file must be placed under `/app/outputs` and follow the schema exactly.

### vertex_model_description.json
- path: `/app/outputs/vertex_model_description.json`
- format: json
- purpose: process
- schema:
  - `type`: object
  - `required`: ["model_type", "nonzero_weights", "parameters"]
  - description: Summary of the vertex model after mapping. Must contain `model_type` (string), `nonzero_weights` (integer 304), and `parameters` (object with `epsilon`, `alpha`, `J`).

### pwfrg_fixedpoint_info.log
- path: `/app/outputs/pwfrg_fixedpoint_info.log`
- format: txt
- purpose: process
- schema: (any text; contains convergence information)

### p_eta_curves.csv
- path: `/app/outputs/p_eta_curves.csv`
- format: csv
- purpose: process
- schema:
  - `type`: table
  - `required_columns`: ["temperature", "eta", "p"]

### step_properties.csv
- path: `/app/outputs/step_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- schema:
  - `type`: table
  - `required_columns`: ["temperature", "gamma", "A2", "gamma_tilde"]
  - `units`:
    - `temperature`: \(k_B T/\epsilon\)
    - `gamma`: \(\epsilon\)
    - `A2`: \(\epsilon\)
    - `gamma_tilde`: \(\epsilon\)

## Self-check before finishing (optional, not scored)
A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV files contain the required columns. Fix any mismatch before finishing.

```json
{
  "outputs": [
    {
      "file": "vertex_model_description.json",
      "format": "json",
      "purpose": "process",
      "schema": {
        "type": "object",
        "required": ["model_type", "nonzero_weights", "parameters"]
      }
    },
    {
      "file": "pwfrg_fixedpoint_info.log",
      "format": "txt",
      "purpose": "process",
      "schema": {}
    },
    {
      "file": "p_eta_curves.csv",
      "format": "csv",
      "purpose": "process",
      "schema": {
        "type": "table",
        "required_columns": ["temperature", "eta", "p"]
      }
    },
    {
      "file": "step_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": ["temperature", "gamma", "A2", "gamma_tilde"],
        "units": {
          "temperature": "k_B T/ε",
          "gamma": "ε",
          "A2": "ε",
          "gamma_tilde": "ε"
        }
      }
    }
  ]
}
```

## How you are scored
Your submitted `step_properties.csv` will be evaluated automatically against reference values and structural checks. The final score is a weighted combination of these checks.
```