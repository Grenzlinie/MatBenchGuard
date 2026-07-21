# Scalar Elasto-Plastic Model with Rejuvenation: Stress-Strain, Yield Stress Evolution, and Localization

## Problem background
Amorphous solids such as glasses deform plastically via localized rearrangements known as shear transformations. These rearrangements interact through long-range elastic fields, leading to complex collective behavior including strain hardening, yield stress evolution, and shear band localization. Mesoscopic elasto-plastic models (EPMs) aim to capture these phenomena with a reduced description in which the material is discretized into cells that yield when local stress exceeds a threshold. A key challenge is connecting such mesoscopic models to the underlying atomistic disorder: what distributions of yield thresholds and post-yield slip increments, and what renewal rule for thresholds after a plastic event, reproduce the plastic behavior observed in atomistic simulations? This task explores a simple scalar EPM in which the renewal distribution is taken from a “rejuvenated” glass quenched near the mode-coupling transition, and the slip increment mean depends quadratically on the local threshold. The objective is to assess whether this approach can reproduce the strain-induced evolution of mean yield stress and the localization dynamics observed in atomistic simulations of a well-annealed glass.

## Model details
Implement a scalar elasto-plastic model on a periodic square lattice of size N×N (use N = 64). Lattice cells are indexed by (i,j) with 0 ≤ i,j < N. Each cell carries a scalar shear stress σ_ij and a local yield threshold σc_ij. The macroscopic applied strain is γ.

**Elastic propagator**  
When a cell (k,l) undergoes a plastic strain increment Δε_pl,kl, the stress change induced at cell (i,j) is Δσ_ij = G(Δx,Δy) Δε_pl,kl, where Δx = (i−k) mod N (minimum image), Δy = (j−l) mod N. The kernel G(r) = G(Δx,Δy) is the standard 2D Eshelby kernel for scalar elasticity:
- For r ≠ 0: G(r) = (1/π)·(cos 4θ)/r²,  with r = √(Δx²+Δy²) and θ = atan2(Δy,Δx).
- For r = 0: G(0) = −∑_{r≠0} G(r) (the sum runs over all other cells of the lattice) to ensure zero mean.

In practice the convolution ∑_kl G(i−k,j−l) ε_pl,kl is computed by FFT: transform the plastic strain field, multiply by the Fourier transform of G, and transform back. The Fourier kernel is
Ĝ(qx,qy) = (qx² − qy²)² / q⁴   for q ≠ 0, with Ĝ(0,0) = 0,
where q = √(qx² + qy²), qx = 2π·kx/N, qy = 2π·ky/N (kx,ky integers). Use FFT libraries (e.g. numpy.fft) to implement this efficiently.

**Yield criterion and plastic slip**  
A cell yields when σ_ij ≥ σc_ij. Upon yielding the plastic strain increment Δε_pl,ij is drawn from an exponential distribution P(Δε) = (1/ε₀) exp(−Δε/ε₀) whose mean ε₀ depends on the current threshold:
ε₀(σc_ij) = c₀ + c₁·σc_ij²,
where c₀ and c₁ are dimensionless parameters to be calibrated.

**Post-yield updates**  
When yielding occurs:
1. The plastic strain ε_pl,ij is incremented by Δε_pl,ij.
2. The stress σ_ij is reset to 0 (the local stress after rearrangement).
3. The yield threshold σc_ij is renewed by drawing a new value from the MCT distribution (see below).

**Athermal quasistatic (AQS) loading protocol**  
Starting from strain γ = 0:
- Increment strain by Δγ = 0.001 and add μ·Δγ to every σ_ij (shear modulus μ = 1).
- Repeatedly identify all cells with σ_ij ≥ σc_ij. For each such cell:
  - draw Δε_pl,ij,
  - update the plastic strain field and the stress field using the elastic propagator,
  - reset the cell’s stress to 0 and renew its threshold.
  Continue until no cells satisfy σ_ij ≥ σc_ij (i.e. the system has relaxed).
- Record the macroscopic stress Σ = (1/N²) ∑_ij σ_ij, the spatial mean yield stress ⟨σc⟩ = (1/N²) ∑_ij σc_ij, and the localization index LOC = ∑_ij ε_pl,ij⁴ / (∑_ij ε_pl,ij²)².
- Repeat until γ reaches 5.

**Initial conditions**  
Each cell’s initial stress is set to 0. Its initial yield threshold σc_ij is drawn from the GQ distribution (see below).

**Yield stress distributions**  
From the paper, extract the following approximate distributions (values in LJ units). The GQ (gradually quenched) glass distribution is used for initial thresholds; the MCT glass distribution is used for renewal after each plastic event.

- GQ distribution: truncated normal with mean 1.05, standard deviation 0.15, clipped to the interval [0.5, 1.8].
- MCT distribution: truncated normal with mean 0.85, standard deviation 0.12, clipped to the interval [0.4, 1.5].

If any drawn value falls outside the clipping bounds, redraw. These distributions are simplifications of the digitized curves from Fig. 2a of the paper and are sufficient to reproduce the qualitative trends.

**Calibration of c₀ and c₁**  
The parameters c₀, c₁ must be chosen so that the stress–strain curve of the GQ glass simulated with the above rules (GQ initial thresholds, MCT renewal) reproduces two target values from the atomistic reference (Fig. 1a, GQ curve):
- Peak stress σ_peak = 1.20 ± 0.05
- Flow stress (plateau after large strain) σ_flow = 0.90 ± 0.05

Search over reasonable values (e.g. c₀ ∈ [0, 0.2], c₁ ∈ [0, 0.05]) by running the model up to γ = 5 for each candidate (c₀,c₁), computing the peak stress and the average stress over the last 20% of the strain range (plateau), and selecting the pair that brings both quantities within the given tolerances. Record the chosen c₀ and c₁ in a JSON file (see Step 2).

## Reproduction target
Produce three CSV files from the calibrated rejuvenation EPM simulation (i.e., after c₀,c₁ have been fixed) for the GQ glass, spanning shear strain from 0 to 5:

- `/app/outputs/stage1_stress_strain.csv`: two columns, strain and stress, capturing the macroscopic stress-strain curve.
- `/app/outputs/stage2_mean_yield_stress.csv`: two columns, strain and mean_threshold, capturing the evolution of the spatially averaged local yield stress.
- `/app/outputs/stage3_localization_index.csv`: two columns, strain and LOC, capturing the localization index.

In addition, save the intermediate artifacts from step 1 and step 2 (see Workflow steps). These are required for completeness but are not used for scoring.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare yield stress distributions and elastic moduli
- Role: process
- Action: Prepare the two yield stress distributions (GQ, MCT) described in the **Yield stress distributions** section, and record the mean shear modulus μ = 1. Save the distribution parameters and modulus into a CSV file for reproducibility.
- Evidence: `/app/outputs/step01_yield_stress_data.csv`
  - CSV with columns: `distribution` (GQ or MCT), `mean`, `std`, `clip_min`, `clip_max`, `mu`.

### Step 2: Calibrate c₀ and c₁
- Role: process
- Action: Implement the scalar EPM as specified. Run the model with the GQ initial distribution and MCT renewal, scanning over (c₀,c₁) values as described in the **Calibration** section. After each run compute the stress–strain curve, extract peak and plateau stresses, and select the pair that satisfies the target tolerances.
- Evidence: `/app/outputs/step02_fitted_parameters.json`
  - JSON object: `{"c0": <value>, "c1": <value>, "peak_stress": <value>, "flow_stress": <value>}`

### Step 3: Macroscopic stress-strain curve from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: Using the calibrated (c₀,c₁) and the distributions from step 1, run the EPM with GQ initial thresholds and MCT renewal up to strain = 5. Record the macroscopic stress Σ at every sampled strain (the values after each AQS step where convergence is reached). Write a two-column CSV (strain, stress).
- Output file: `/app/outputs/stage1_stress_strain.csv`
- Format: csv
- Contract: Two-column CSV: `strain` (float, shear strain γ), `stress` (float, macroscopic shear stress Σ)
- Scoring: scored by hidden verifier (qualitative structural audit: peak existence, post-peak behaviour, plateau range).

### Step 4: Mean local yield stress evolution from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: From the same EPM simulation as step 3, compute the spatially averaged local yield stress ⟨σc⟩ at the same strain values. Write a two-column CSV (strain, mean_threshold).
- Output file: `/app/outputs/stage2_mean_yield_stress.csv`
- Format: csv
- Contract: Two-column CSV: `strain` (float), `mean_threshold` (float, spatial average of cell local yield stress)
- Scoring: scored by hidden verifier (qualitative structural audit: initial increase then decrease, max position range, start > end).

### Step 5: Localization index evolution from rejuvenation EPM simulation
- Role: scored (load-bearing)
- Action: From the same EPM simulation, compute the localization index LOC(γ) = Σ ε_pl,ij⁴ / (Σ ε_pl,ij²)² at the same strain values. Write a two-column CSV (strain, LOC). **All LOC values must lie in [0, 1]; if any value falls outside this interval the localization score will be zero.**
- Output file: `/app/outputs/stage3_localization_index.csv`
- Format: csv
- Contract: Two-column CSV: `strain` (float), `LOC` (float, localization index)
- Scoring: scored by hidden verifier (qualitative structural audit: peak existence and position range, final value < peak, max LOC range; all values in [0,1]).

## Output files
Write all artifacts under `/app/outputs`:

- `/app/outputs/step01_yield_stress_data.csv`
- `/app/outputs/step02_fitted_parameters.json`
- `/app/outputs/stage1_stress_strain.csv`
- `/app/outputs/stage2_mean_yield_stress.csv`
- `/app/outputs/stage3_localization_index.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_yield_stress_data.csv
- path: `/app/outputs/step01_yield_stress_data.csv`
- format: csv
- purpose: unscored (evidence)
- target_policy: none
- description: Record of the distribution parameters (mean, std, clipping) for GQ and MCT, and the shear modulus μ.
- schema:
  - `type`: table
  - `required_columns`: `distribution`, `mean`, `std`, `clip_min`, `clip_max`, `mu`

### step02_fitted_parameters.json
- path: `/app/outputs/step02_fitted_parameters.json`
- format: json
- purpose: unscored (evidence)
- target_policy: none
- description: Fitted values of c₀ and c₁ obtained by matching the stress–strain curve to the reference peak and plateau.
- schema:
  - `type`: object
  - `required`: `c0`, `c1`, `peak_stress`, `flow_stress`

### stage1_stress_strain.csv
- path: `/app/outputs/stage1_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Macroscopic stress-strain curve Σ(γ) for the GQ glass with rejuvenation. Scored by qualitative checks: peak stress occurs between strain 0.02 and 0.6 with value above 1.03×plateau, post-peak stresses do not exceed 1.02×peak, plateau average lies between 0.3 and 2.0.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: LJ units

### stage2_mean_yield_stress.csv
- path: `/app/outputs/stage2_mean_yield_stress.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Evolution of the spatially averaged local yield stress ⟨σc⟩(γ). Scored by qualitative checks: positive early slope (strain 0–0.5), negative late slope (strain 3–5), final value below 0.995×initial, maximum occurs between strain 0.05 and 1.5.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `mean_threshold`
  - `units`:
    - `strain`: dimensionless
    - `mean_threshold`: LJ units

### stage3_localization_index.csv
- path: `/app/outputs/stage3_localization_index.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Localization index LOC(γ) for the GQ glass. Scored by qualitative checks: peak strain between 0.1 and 2.0, final LOC < peak LOC, peak LOC between 0.08 and 0.8. **All LOC values must be between 0 and 1; if any value is outside this interval the whole localization score becomes zero.**
- schema:
  - `type`: table
  - `required_columns`: `strain`, `LOC`
  - `units`:
    - `strain`: dimensionless
    - `LOC`: dimensionless

Notes: Steps 1 and 2 produce intermediate artifacts that are not scored but are required. The three scored artifacts come from a single EPM run after calibration. The hidden checker performs qualitative structural audits (no RMSE computation).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_yield_stress_data.csv",
      "format": "csv",
      "purpose": "unscored",
      "target_policy": "none",
      "schema": {
        "type": "table",
        "required_columns": ["distribution", "mean", "std", "clip_min", "clip_max", "mu"]
      },
      "description": "Record of distribution parameters (GQ, MCT) and shear modulus."
    },
    {
      "file": "step02_fitted_parameters.json",
      "format": "json",
      "purpose": "unscored",
      "target_policy": "none",
      "schema": {
        "type": "object",
        "required": ["c0", "c1", "peak_stress", "flow_stress"]
      },
      "description": "Fitted c0 and c1."
    },
    {
      "file": "stage1_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["strain", "stress"],
        "units": { "strain": "dimensionless", "stress": "LJ units" }
      },
      "description": "Macroscopic stress-strain curve. Qualitative checks: peak strain [0.02,0.6], peak>1.03*plateau, post-peak <1.02*peak, plateau average [0.3,2.0]."
    },
    {
      "file": "stage2_mean_yield_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["strain", "mean_threshold"],
        "units": { "strain": "dimensionless", "mean_threshold": "LJ units" }
      },
      "description": "Mean yield stress evolution. Qualitative checks: early slope >0, late slope <0, final <0.995*initial, max strain [0.05,1.5]."
    },
    {
      "file": "stage3_localization_index.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": ["strain", "LOC"],
        "units": { "strain": "dimensionless", "LOC": "dimensionless" }
      },
      "description": "Localization index. Qualitative checks: peak strain [0.1,2.0], final<peak, peak LOC [0.08,0.8], all LOC in [0,1]."
    }
  ],
  "notes": "The three scored artifacts are produced by a single EPM simulation run; they are separated for scoring clarity. The hidden checker performs qualitative structural audits (no RMSE computation)."
}
```

## How you are scored
Each of the three scored artifacts will be evaluated by a hidden verifier that performs qualitative structural checks. For the stress–strain curve it checks for a well‑defined peak, post‑peak behaviour, and plateau range. For the mean yield stress it checks the increasing‑then‑decreasing trend. For the localization index it checks the peak, decay, value range, and that every LOC value lies in [0,1]. Scores from the three components are weighted and combined into a final reward between 0 and 1. The verifier does **not** compute an RMSE against a hidden reference curve; only the qualitative features described above are evaluated.