# Surface effective mass calculation in the Hubbard model using DMFT

## Problem background
Strongly correlated electron systems can exhibit Fermi-liquid behavior where the effective mass \(m^*\) is renormalized by interactions. In a semi-infinite lattice, the surface has different coordination than the bulk, which may alter correlation effects and produce a surface effective mass distinct from the interior. The Hubbard model on a simple-cubic lattice provides a minimal setting to study this possibility. Dynamical mean-field theory (DMFT) treats the correlations non-perturbatively and can resolve the layer-dependent self-energies from which effective masses are extracted. A surface layer with an effective mass sufficiently different from the bulk can give rise to a purely correlation-driven one-electron surface mode that splits off from the bulk continuum. This task aims to quantify the layer-resolved effective masses and to determine for which electron fillings such a surface mode emerges.

## Approach
The method is DMFT for a film geometry with 15 atomic layers of a simple-cubic (100) lattice. The layers are numbered from the surface inward: \(\alpha = 1\) (topmost surface) to \(\alpha = 15\) (bottommost). The hopping amplitude is \(t = 1\) between nearest neighbours, and the on-site Hubbard interaction is \(U = 24|t| = 2W\) (\(W\) is the non-interacting bandwidth). DMFT maps the lattice problem onto 15 coupled single-impurity Anderson models (SIAMs), one per layer. Each SIAM is solved by exact diagonalisation (ED) using \(n_s = 8\) sites. The iterative loop starts from an initial guess for the layer-dependent self-energies \(\Sigma_\alpha(E)\) (\(\alpha = 1,\ldots,15\)). The lattice Dyson equation yields the on-site Green’s function, and the DMFT self-consistency condition gives the free impurity Green’s function \(G_0^{(\alpha)}(E)\). The ED solver then returns an updated \(\Sigma_\alpha(E)\), and the cycle repeats until self-consistency.

To target a specific filling \(n\) (the average number of electrons per site), you must adjust the chemical potential \(\mu\). A practical approach is to treat \(\mu\) as an outer loop: for each trial \(\mu\), run the DMFT loop to convergence and compute the resulting total density; then update \(\mu\) using a bisection or similar root-finding method until the density matches the target \(n\) within a chosen tolerance.

From the converged self-energies, the layer-resolved effective mass is
\[
m_\alpha^* = 1 - \frac{d\Sigma_\alpha(0)}{dE}.
\]
The bulk effective mass \(m_b^*\) is defined as the mass of the film centre, where bulk behaviour is recovered. For the 15-layer film this is layer \(\alpha = 8\). The surface mass \(m_s^*\) is the mass of the topmost layer, \(\alpha = 1\). The calculation is carried out for a range of fillings \(n\) from 0.5 to nearly half‑filling (0.99).

In the second stage, the existence of a surface mode at a given wave vector \(\mathbf{k}_\parallel\) in the two-dimensional surface Brillouin zone is determined by an analytic condition involving the layer masses and the zero‑frequency self‑energy offsets \(a_\alpha = \Sigma_\alpha(0)\). The criterion is derived under the assumption that the surface effective mass is larger than the bulk one, i.e. \(r^2 = m_b^*/m_s^* < 1\). For the high-symmetry points \((0,0)\) and \((\pi,\pi)\), the surface mode condition reads
\[
\left| \frac{\varepsilon_\parallel(\mathbf{k}_\parallel) - \mu + a_s}{\varepsilon_\perp} + \frac{a_b - a_s}{(1 - r^2)\varepsilon_\perp} \right| > \frac{2 - r^2}{1 - r^2},
\]
where \(r^2 = m_b^* / m_s^*\), \(\varepsilon_\parallel(\mathbf{k}_\parallel) = 2t(\cos k_x + \cos k_y)\), \(\varepsilon_\perp = |t|\), \(a_s = a_{\alpha=1}\), \(a_b = a_{\alpha=8}\), and \(\mu\) is the chemical potential corresponding to the filling \(n\). The lowest filling \(n\) for which this inequality holds defines the surface-mode threshold.

## Reproduction target
Produce two comma-separated value (CSV) files:
1. **effective_masses.csv** – for fillings \(n\) ranging from 0.5 to 0.99 (including \(n = 0.99\)), report the surface effective mass \(m_{\text{surface}}\), the bulk effective mass \(m_{\text{bulk}}\), and their ratio \(m_{\text{surface}} / m_{\text{bulk}}\).
2. **surface_mode_thresholds.csv** – for the two wave vectors \((0,0)\) and \((\pi,\pi)\), report the lowest filling \(n\) (to the resolution of your filling grid) at which the surface-mode criterion is satisfied.

## Assets
No external datasets, models, or pre‑trained weights are needed. All physical parameters (lattice geometry, hopping, interaction strength, temperature = 0) are given in the approach description. The agent must implement the DMFT+ED solver from scratch. A standard scientific Python environment (numpy, scipy) is recommended for numerical linear algebra and the exact diagonalisation routine, though any language may be used as long as the required CSV files are produced.

## Workflow steps

### Step 1: DMFT effective mass calculation
- Role: scored (load-bearing)
- Action: Implement DMFT for a 15-layer (100) Hubbard film (\(U=2W=24|t|\), \(t=1\)) using exact diagonalization as the impurity solver (\(n_s=8\) sites). For each target filling from 0.5 to 0.99, determine the chemical potential \(\mu\) (e.g., via bisection) that yields that filling within your DMFT loop, then obtain the converged layer-dependent self-energies. Compute effective masses \(m_\alpha^* = 1 - d\Sigma_\alpha(0)/dE\). The surface mass \(m_{\text{surface}}\) is taken from layer \(\alpha=1\); the bulk mass \(m_{\text{bulk}}\) is taken from the central layer \(\alpha=8\). Write the surface mass, bulk mass, and mass ratio for each filling to `effective_masses.csv`.
- Output file: `/app/outputs/effective_masses.csv`
- Format: csv
- Contract: columns: `n` (float), `m_surface` (float), `m_bulk` (float), `ratio` (float); one row per filling, must include `n=0.99`
- Scoring: scored by hidden verifier

### Step 2: Surface mode threshold determination
- Role: scored
- Action: Using the layer-dependent effective masses from step 1, evaluate the analytic criterion for a surface mode at the \((0,0)\) and \((\pi,\pi)\) points of the surface Brillouin zone. The required self-energy offsets \(a_s\) and \(a_b\) are \(\Sigma_{\alpha=1}(0)\) and \(\Sigma_{\alpha=8}(0)\), respectively. Determine the lowest filling \(n\) where the criterion is satisfied at each point. Write the two critical fillings to `surface_mode_thresholds.csv`.
- Output file: `/app/outputs/surface_mode_thresholds.csv`
- Format: csv
- Contract: columns: `k_point` (str, either `'(0,0)'` or `'(pi,pi)'`), `threshold_n` (float); one row per k-point
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/effective_masses.csv`
- `/app/outputs/surface_mode_thresholds.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_masses.csv
- path: `/app/outputs/effective_masses.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with layer-resolved effective masses; checker recomputes mass ratio from m_surface and m_bulk columns.
- schema:
  - `type`: table
  - `required_columns`: `n`, `m_surface`, `m_bulk`, `ratio`

### surface_mode_thresholds.csv
- path: `/app/outputs/surface_mode_thresholds.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical filling values at which a surface mode appears at (0,0) and (π,π) points.
- schema:
  - `type`: table
  - `required_columns`: `k_point`, `threshold_n`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_masses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "m_surface",
          "m_bulk",
          "ratio"
        ]
      },
      "description": "CSV with layer-resolved effective masses; checker recomputes mass ratio from m_surface and m_bulk columns."
    },
    {
      "file": "surface_mode_thresholds.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_point",
          "threshold_n"
        ]
      },
      "description": "Critical filling values at which a surface mode appears at (0,0) and (π,π) points."
    }
  ]
}
```

## How you are scored
A hidden verifier independently checks both output files.
- For `effective_masses.csv`, the verifier will recompute the ratio \(m_{\text{surface}} / m_{\text{bulk}}\) at the filling \(n = 0.99\) using the columns you provide, and compare it to an expected value with an appropriate tolerance.
- For `surface_mode_thresholds.csv`, the verifier will check that the reported threshold fillings for \((0,0)\) and \((\pi,\pi)\) each lie within a small absolute tolerance of the expected values.
Each artifact carries a certain weight, and your final reward is a weighted sum of the two scores. You must use the exact column names and file formats specified (see the output contract); the verifier will not accept alternative naming.