# Kitaev‑J3 Spin Liquid Dynamical Structure Factor and Raman Spectrum

## Problem background
The Kitaev honeycomb model is an exactly solvable example of a quantum spin liquid that hosts fractionalized excitations: itinerant matter Majorana fermions and static Z2 gauge fluxes (visons). Real candidate materials, however, often contain additional non-Kitaev interactions. This task focuses on the effect of a third-nearest-neighbor Heisenberg exchange J3 on the ferromagnetic Kitaev model (K = -1). Such a coupling is believed to be significant in several honeycomb iridates and cobaltates. The objective is to compute how J3 modifies the spin dynamical structure factor and Raman scattering response, quantifying the emergence of low-energy collective modes and their evolution with J3, as well as the distinct vison and Majorana contributions to inelastic light scattering.

## Approach
The dynamical structure factor S(ω,q) is calculated within a self-consistent parton mean-field theory that expresses spins as bilinears of Majorana fermions and solves the resulting saddle-point equations iteratively. For each value of J3 between 0 and 0.1, the converged mean-field Green's functions feed into a random-phase approximation (RPA) that resums the residual interactions to yield the full spin susceptibility. The diagonal DSF is evaluated along a high-symmetry path through the Brillouin zone, and the lowest-energy peak at the M point is identified as a paramagnon-like collective mode; its gap is recorded as a function of J3. Separately, the Raman response is computed perturbatively starting from the exact Kitaev ground state. The Loudon–Fleury Raman operator is constructed with both incoming and outgoing polarization vectors along the b crystallographic axis. The J3 vertex contribution is decomposed into channels involving two visons and four visons, and the total intensity I(ω) is obtained by summing the pure Kitaev two-fermion continuum and the J3-induced contributions.

## Reproduction target
The agent must implement the above framework and deliver: (1) a CSV file `dsf_gap_vs_J3.csv` containing the energy gap of the lowest M‑point collective mode (in units of |K|) for at least ten equally spaced J3 values from 0 to 0.1, together with a companion NPZ file `dsf_M_curves.npz` that stores the full raw S(ω,M) curves used to extract those gaps; (2) a CSV file `raman_intensity.csv` covering the frequency range 0–10 |K| with columns for ω, I_total, I_2v, and I_4v, computed for the pure Kitaev model with a J3 perturbation of strength g = J3/K = 0.05 and with both incoming and outgoing polarization vectors along b. The results must demonstrate the softening of the collective mode with increasing J3 and characterize the two-vison and four-vison spectral features.

## Assets
The required external resources are open-source scientific Python packages: numpy, scipy (for linear algebra, integration, and special functions). No external datasets, pretrained models, or proprietary tools are needed. The mean-field and RPA codes, as well as the exact Kitaev Raman calculation, are to be re‑implemented from scratch following the approach described above.

## Workflow steps

### Step 1: Self‑consistent parton mean‑field solution
- Role: process
- Action: Implement the self‑consistent parton mean‑field theory for the Kitaev‑J3 model on the honeycomb lattice. For each J3 value (at least 10 equally spaced points from 0 to 0.1), iterate the mean‑field equations to convergence, construct the 8‑band Hamiltonian in momentum space, and diagonalize it to obtain the quasiparticle dispersions and single‑particle Green’s functions. Save convergence diagnostics (the converged mean‑field parameters) to mf_diagnostics.json.
- Evidence: `/app/outputs/mf_diagnostics.json`

### Step 2: RPA‑corrected spin dynamical structure factor and M‑point gap extraction
- Role: scored (load-bearing)
- Action: Using the converged mean‑field Green’s functions, construct the interaction matrix U(q), evaluate the RPA susceptibility and compute the diagonal spin dynamical structure factor S(ω,q) along a momentum path that includes the M point. For each J3, locate the lowest‑energy peak in S(ω,q) at the M point and record its centre frequency as the paramagnon gap. Save the gap values vs J3 to dsf_gap_vs_J3.csv. Additionally, save the raw DSF intensity curves S(ω,M) for every J3 to dsf_M_curves.npz to allow the checker to re‑extract the gaps.
- Output file: `/app/outputs/dsf_gap_vs_J3.csv`
- Format: csv
- Contract: CSV with columns: J3 (float, units of |K|), gap_energy (float, units of |K|). The NPZ file contains keys 'J3_vals' (list of floats) and 'curves' (list of dictionaries, each with keys 'omega', 'S').
- Scoring: scored by hidden verifier

### Step 3: Raman scattering intensity of the J3‑perturbed Kitaev spin liquid
- Role: scored (load-bearing)
- Action: For the pure Kitaev model (K = −1) with a small J3 perturbation g = J3/K = 0.05, construct the Raman operator using the Loudon–Fleury approximation with both incoming and outgoing polarisation vectors along the b crystallographic axis. Evaluate the Raman correlators using the exact eigenstates of the Kitaev Hamiltonian. Decompose the J3 vertex contribution into two‑vison (I₂v) and four‑vison (I₄v) channels, and compute the total intensity I_total = I_K + I_J3 as functions of frequency ω. Save the spectra to raman_intensity.csv.
- Output file: `/app/outputs/raman_intensity.csv`
- Format: csv
- Contract: CSV with columns: omega (float, units of |K|), I_total (float), I_2v (float), I_4v (float). Frequency range covering [0, 10|K|] with sufficient resolution.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dsf_gap_vs_J3.csv`
- `/app/outputs/dsf_M_curves.npz`
- `/app/outputs/raman_intensity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dsf_gap_vs_J3.csv
- path: `/app/outputs/dsf_gap_vs_J3.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Paramagnon gap at the M point vs third‑NN Heisenberg coupling J3. The checker will recompute the gaps from dsf_M_curves.npz and compare.
- schema:
  - `type`: table
  - `required_columns`: `J3`, `gap_energy`
  - `units`:
    - `J3`: |K|
    - `gap_energy`: |K|

### raman_intensity.csv
- path: `/app/outputs/raman_intensity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raman scattering intensity for the Kitaev model with J3 perturbation (g=0.05). The checker will verify the location of the four‑vison peak and the characteristic shape of the two‑vison continuum.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `I_total`, `I_2v`, `I_4v`
  - `units`:
    - `omega`: |K|
    - `I_total`: arb. units
    - `I_2v`: arb. units
    - `I_4v`: arb. units

Notes: The dsf_M_curves.npz is an essential artifact required by the checker to recompute the M‑point gap. All spectral features (peak positions, onsets, and monotonicity) are verified with hidden tolerances; no gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dsf_gap_vs_J3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "J3",
          "gap_energy"
        ],
        "units": {
          "J3": "|K|",
          "gap_energy": "|K|"
        }
      },
      "description": "Paramagnon gap at the M point vs third‑NN Heisenberg coupling J3. The checker will recompute the gaps from dsf_M_curves.npz and compare."
    },
    {
      "file": "raman_intensity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "I_total",
          "I_2v",
          "I_4v"
        ],
        "units": {
          "omega": "|K|",
          "I_total": "arb. units",
          "I_2v": "arb. units",
          "I_4v": "arb. units"
        }
      },
      "description": "Raman scattering intensity for the Kitaev model with J3 perturbation (g=0.05). The checker will verify the location of the four‑vison peak and the characteristic shape of the two‑vison continuum."
    }
  ],
  "notes": "The dsf_M_curves.npz is an essential artifact required by the checker to recompute the M‑point gap. All spectral features (peak positions, onsets, and monotonicity) are verified with hidden tolerances; no gold values are disclosed here."
}
```

## How you are scored
A hidden verifier checks each workflow stage’s output independently. For the DSF stage, it reads the raw NPZ curves, re‑extracts the M‑point gap for every J3, and compares the extracted gaps to those in `dsf_gap_vs_J3.csv`, verifying that the gap decreases monotonically with increasing J3 and that a gap closure occurs at a specific J3. For the Raman stage, it reads `raman_intensity.csv` and identifies the frequency of the strongest peak in the I_4v channel and the onset and characteristic shape of the I_2v continuum, checking these structural features against expected behavior. The final reward is a weighted combination of these per‑stage scores. Reporting numbers that match the hidden gold is insufficient; the raw artifact must support the recomputation and the spectral shape must satisfy the structural checks. Tolerance ranges are hidden.
