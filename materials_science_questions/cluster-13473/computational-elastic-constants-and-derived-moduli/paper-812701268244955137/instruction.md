# Stability-Dependent Local Elastic Heterogeneity in a Polydisperse Glass Former

## Problem background
Amorphous solids display heterogeneous local elasticity that is thought to influence their anomalous vibrational and thermal properties. The spatial variation of elastic constants can depend on the stability of the glass, which is controlled by the temperature from which the glass is prepared (the parent temperature). This task reproduces computational measurements of local shear and bulk moduli in a model polydisperse glass former. The objective is to compute the distributions of local elastic moduli for several coarse-graining box sizes and a range of parent temperatures, and to examine the dependence of the widths of these distributions on the parent temperature and box size, as well as the spatial correlations among the local moduli. Understanding this behavior sheds light on the origin of sound attenuation and the boson peak in glasses.

## Approach
The investigation is performed with classical molecular dynamics (MD) on a system of polydisperse repulsive particles interacting via a truncated and tapered power-law potential. The protocol involves three main stages:

1. **Preparation of equilibrium configurations**: starting from a random packing of 48 000 particles at number density ρ = 1, configurations are equilibrated at several parent temperatures T<sub>p</sub> ∈ {0.062, 0.085, 0.200} using swap Monte Carlo (an advanced Monte Carlo method that combines conventional translational moves with particle-swap moves to accelerate equilibration in deeply supercooled liquids).

2. **Quenching and low-temperature production**: each equilibrated configuration is quenched to its zero-temperature inherent structure via conjugate-gradient minimization. Subsequently, a long NVT MD simulation is run at a very low temperature (T = 10<sup>−5</sup> ε/k<sub>B</sub>) to sample the energy landscape. The production run length is Δt = 3×10<sup>5</sup> (reduced time units) with a time step dt = 0.02, corresponding to 1.5×10<sup>7</sup> time steps. Particle positions and the global stress tensor are recorded at regular intervals over the production run, excluding any initial transient period; collect at least 10 equally spaced snapshots for the subsequent analysis.

3. **Local elastic modulus analysis**: at each saved MD snapshot, the simulation box is subdivided into cubic cells (coarse-graining boxes) of sizes w = 12.114, 6.057, 4.543, and 3.303. For each cell, the fully-local stress tensor is computed using the bond-length-weighted line-sharing scheme, and the local elastic constant tensor C<sub>αβγδ</sub> is evaluated from its affine (Born + stress + kinetic) and non-affine (fluctuation) contributions. The local moduli are obtained as linear combinations of C<sub>αβγδ</sub>, yielding five shear moduli G<sub>1</sub>…G<sub>5</sub> and the bulk modulus K per cell per snapshot. As the coarse-graining box size w increases, the moduli are averaged over larger volumes and their variance is expected to decrease. Global moduli obtained from homogeneous deformations at zero temperature should equal the spatial average of the local moduli and can be used for internal consistency checks.

The raw per-cell moduli are collected over all snapshots, all box sizes, and all parent temperatures.

## Mathematical definitions

### 1. Interaction potential
Particles interact via a truncated and smoothed inverse‑power‑law pair potential:

$$
U(r_{ij}) =
\begin{cases}
\varepsilon \left(\frac{\sigma_{ij}}{r_{ij}}\right)^{12} + v(r_{ij}), & \frac{\sigma_{ij}}{r_{ij}} < r_{\mathrm{cut}} \\[4pt]
0, & \frac{\sigma_{ij}}{r_{ij}} \ge r_{\mathrm{cut}}
\end{cases}
$$

with the tapering polynomial

$$
v(r_{ij}) = c_{0} + c_{2}\left(\frac{r_{ij}}{\sigma_{ij}}\right)^{2} + c_{4}\left(\frac{r_{ij}}{\sigma_{ij}}\right)^{4}.
$$

Distance between particles \(i\) and \(j\): \(r_{ij} = |\mathbf{r}_i - \mathbf{r}_j|\).  
The interaction radius is \(\sigma_{ij} = \frac{\sigma_i + \sigma_j}{2}\,(1 - e|\sigma_i - \sigma_j|)\) with non‑additive mixing parameter \(e = 0.2\).  
Individual particle sizes are drawn from the distribution

$$
P(\sigma) = \frac{A}{\sigma^3}, \quad \sigma \in [0.73,\, 1.63],
$$

and \(A\) is the normalization constant.  

The cutoff distance is \(r_{\mathrm{cut}} = 1.25\). The coefficients \(c_0, c_2, c_4\) are determined by requiring that the potential and its first two derivatives be continuous at \(r_{ij} = r_{\mathrm{cut}}\,\sigma_{ij}\).

All quantities are expressed in reduced units: energy unit \(\varepsilon\), length unit \(\sigma_0\) (the average of \(\sigma\)), and mass unit \(m\), giving a time unit \(\tau = \sqrt{m\sigma_0^2/\varepsilon}\).

### 2. Local stress tensor
For a cubic cell \(m\) of side length \(w\), the volume‑averaged stress tensor is

$$
\sigma_{\alpha\beta}^{m} = -\rho^{m} T \delta_{\alpha\beta} + \frac{1}{w^{3}} \sum_{i<j} \frac{\partial U(r_{ij})}{\partial r_{ij}} \frac{r_{\alpha}^{ij} r_{\beta}^{ij}}{r_{ij}} \frac{q_{m}^{ij}}{r_{ij}},
$$

where \(\rho^{m}\) is the local number density, \(T\) is the temperature, \(\delta_{\alpha\beta}\) is the Kronecker delta, and \(q_{m}^{ij}\) is the length of the segment of the line joining \(\mathbf{r}_i\) and \(\mathbf{r}_j\) that lies inside cell \(m\). Greek subscripts denote Cartesian components \((x,y,z)\); Roman superscripts label particles.

### 3. Local elastic constant tensor
The local fourth‑rank elastic constant tensor for cell \(m\) is defined as

$$
C_{\alpha\beta\gamma\delta}^{m} = C_{\alpha\beta\gamma\delta}^{A m} - C_{\alpha\beta\gamma\delta}^{N m},
$$

where the affine part consists of three terms:

- Born term:  
  $$
  C_{\alpha\beta\gamma\delta}^{B m} = \frac{1}{w^{3}} \Big\langle \sum_{i<j} \Big( \frac{\partial^{2} U}{\partial r_{ij}^{2}} - \frac{1}{r_{ij}}\frac{\partial U}{\partial r_{ij}} \Big) \frac{r_{\alpha}^{ij} r_{\beta}^{ij} r_{\gamma}^{ij} r_{\delta}^{ij}}{r_{ij}^{2}} \frac{q_{m}^{ij}}{r_{ij}} \Big\rangle
  $$

- Stress term:  
  $$
  \begin{aligned}
  C_{\alpha\beta\gamma\delta}^{C m} = -\frac{1}{2}\Big[ & 2\langle\sigma_{\alpha\beta}^{m}\rangle \delta_{\gamma\delta} - \langle\sigma_{\alpha\gamma}^{m}\rangle \delta_{\beta\delta} \\
  & - \langle\sigma_{\alpha\delta}^{m}\rangle \delta_{\beta\gamma} - \langle\sigma_{\beta\gamma}^{m}\rangle \delta_{\alpha\delta} - \langle\sigma_{\beta\delta}^{m}\rangle \delta_{\alpha\gamma} \Big]
  \end{aligned}
  $$

- Kinetic term:  
  $$
  C_{\alpha\beta\gamma\delta}^{K m} = 2\langle\hat{\rho}^{m}\rangle T \big( \delta_{\alpha\gamma}\delta_{\beta\delta} + \delta_{\alpha\delta}\delta_{\beta\gamma} \big)
  $$

The non‑affine (fluctuation) contribution is

$$
C_{\alpha\beta\gamma\delta}^{N m} = \frac{V}{T} \big( \langle\sigma_{\alpha\beta}^{m} \sigma_{\gamma\delta}^{m}\rangle - \langle\sigma_{\alpha\beta}^{m}\rangle\langle\sigma_{\gamma\delta}^{m}\rangle \big).
$$

Angle brackets \(\langle\cdot\rangle\) denote an ensemble average over snapshots. \(V\) is the total volume of the simulation box.

### 4. Local moduli
The local bulk modulus \(K^{m}\) and the five local shear moduli \(G_{1}^{m},\dots,G_{5}^{m}\) are obtained as linear combinations of the components of \(C_{\alpha\beta\gamma\delta}^{m}\):

$$
\begin{aligned}
K^{m} &= \frac{1}{9}\big( C_{xxxx}^{m} + C_{yyyy}^{m} + C_{zzzz}^{m} + C_{xxyy}^{m} + C_{yyxx}^{m} + C_{xxzz}^{m} + C_{zzxx}^{m} + C_{yyzz}^{m} + C_{zzyy}^{m} \big), \\[4pt]
G_{1}^{m} &= \frac{1}{4}\big( C_{xxxx}^{m} + C_{yyyy}^{m} - C_{xxyy}^{m} - C_{yyxx}^{m} \big), \\[4pt]
G_{2}^{m} &= \frac{1}{4\sqrt{3}}\big( C_{xxxx}^{m} + C_{yyyy}^{m} + 4C_{zzzz}^{m} + C_{xxyy}^{m} + C_{yyxx}^{m} \\
         &\qquad\qquad - 2(C_{xxzz}^{m} + C_{zzxx}^{m} + C_{yyzz}^{m} + C_{zzyy}^{m}) \big), \\[4pt]
G_{3}^{m} &= \frac{1}{4}\big( C_{xyxy}^{m} + C_{xyyx}^{m} + C_{yxxy}^{m} + C_{yxyx}^{m} \big), \\[4pt]
G_{4}^{m} &= \frac{1}{4}\big( C_{xzxz}^{m} + C_{xzzx}^{m} + C_{zxxz}^{m} + C_{zxzx}^{m} \big), \\[4pt]
G_{5}^{m} &= \frac{1}{4}\big( C_{yzyz}^{m} + C_{yzzy}^{m} + C_{zyyz}^{m} + C_{zyzy}^{m} \big).
\end{aligned}
$$

These formulas are taken from the fully‑local approach of Mizuno, Mossa, and Barrat (Soft Matter, 2019).

## Reproduction target
Produce a CSV file `local_moduli_raw.csv` that contains the local shear and bulk moduli for every coarse-graining box and every analyzed snapshot, covering all four box sizes and the three parent temperatures. The file must have the columns: snapshot (int), w (float), Tp (float), box_id (int), center_x (float), center_y (float), center_z (float), G1, G2, G3, G4, G5, and K (all float). A hidden verifier will use this CSV to compute the standard deviations of the local shear and bulk moduli for each parent temperature and box size, and to compute nearest-neighbor correlation parameters of the moduli. The verifier checks whether your data exhibits the physically expected dependence on parent temperature and box size, and whether the spatial correlations are consistent with the known behavior of this model glass former. You do not need to perform the statistical analysis yourself; only the raw moduli CSV is required.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://lammps.org
- Polydisperse repulsive pair potential (all parameters defined in this instruction)

## Workflow steps

### Step 1: Generate initial configuration
- Role: process
- Action: Create an initial configuration of N=48000 polydisperse particles with the size distribution P(σ) ∝ 1/σ³, σ∈[0.73,1.63] and number density ρ=1 in a cubic box with periodic boundaries.
- Evidence: none

### Step 2: Equilibrate at parent temperatures
- Role: process
- Action: Equilibrate the initial configuration at each parent temperature Tp ∈ {0.062, 0.085, 0.200} using swap Monte Carlo to obtain well-equilibrated liquid/glass configurations.
- Evidence: none

### Step 3: Quench to inherent structures
- Role: process
- Action: Quench each equilibrated configuration to its zero-temperature inherent structure via conjugate gradient minimization.
- Evidence: none

### Step 4: Low-temperature NVT MD production
- Role: process
- Action: Run a low-temperature NVT MD simulation (T = 10⁻⁵ ε/k_B) on each inherent structure using a timestep dt=0.02 for a production length of at least 1.5×10⁷ steps (Δt = 3×10⁵ in reduced time units). Record particle positions and the global stress tensor at regular intervals such that at least 10 independent, equally spaced snapshots are collected over the production run, after discarding any initial transient period.
- Evidence: none

### Step 5: Compute local elastic moduli and export raw CSV
- Role: scored (load-bearing)
- Action: From the saved MD snapshots, for each snapshot and for each coarse-graining box of sizes w = {12.114, 6.057, 4.543, 3.303}, compute the five local shear moduli (G1..G5) and the local bulk modulus K using the fully‑local stress and elastic‑constant formulae given in the Mathematical definitions section. Write a CSV file with one row per box per snapshot, including snapshot index, box size, parent temperature, box center coordinates, and the computed moduli.
- Output file: `/app/outputs/local_moduli_raw.csv`
- Format: csv
- Contract: CSV with columns: snapshot (int), w (float), Tp (float), box_id (int), center_x (float), center_y (float), center_z (float), G1 (float), G2 (float), G3 (float), G4 (float), G5 (float), K (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/local_moduli_raw.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### local_moduli_raw.csv
- path: `/app/outputs/local_moduli_raw.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw local moduli per coarse-graining box and snapshot for all parent temperatures and box sizes. The checker will group by Tp and box size, compute standard deviations of the local moduli and nearest-neighbor correlation parameters, and verify that the data follows the expected physical trends for this glass former.
- schema:
  - `type`: table
  - `required_columns`: `snapshot`, `w`, `Tp`, `box_id`, `center_x`, `center_y`, `center_z`, `G1`, `G2`, `G3`, `G4`, `G5`, `K`
  - `description`: Per-box per-snapshot local shear (five components) and bulk moduli, with parent temperature.

Notes: The scorer performs a structural audit that evaluates whether the variance of local moduli changes systematically with parent temperature and box size, and whether the nearest-neighbor correlations are consistent with the reference study.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "local_moduli_raw.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "snapshot",
          "w",
          "Tp",
          "box_id",
          "center_x",
          "center_y",
          "center_z",
          "G1",
          "G2",
          "G3",
          "G4",
          "G5",
          "K"
        ],
        "description": "Per-box per-snapshot local shear (five components) and bulk moduli, with parent temperature."
      },
      "description": "Raw local moduli per coarse-graining box and snapshot for all parent temperatures and box sizes. The checker will group by Tp and box size, compute standard deviations of the local moduli and nearest-neighbor correlation parameters, and verify that the data follows the expected physical trends for this glass former."
    }
  ],
  "notes": "The scorer performs a structural audit that evaluates whether the variance of local moduli changes systematically with parent temperature and box size, and whether the nearest-neighbor correlations are consistent with the reference study."
}
```

## How you are scored
Your submission is scored by a hidden verifier that runs after your agent finishes. The verifier reads your `local_moduli_raw.csv`, groups the data by parent temperature and box size, and computes summary statistics (standard deviations of the five shear moduli and of the bulk modulus, and the nearest-neighbor correlation parameters Ψ<sub>G</sub> and Ψ<sub>K</sub>). The verifier evaluates whether these statistics exhibit the expected dependencies on parent temperature and box size, and whether the spatial correlations are consistent with the known behavior of the model glass former. Each scored workflow step contributes a weight to the overall reward. The verifier does not compare your numbers to any single “correct” value; the scoring is designed to reward honest computational reproduction of the described protocol.