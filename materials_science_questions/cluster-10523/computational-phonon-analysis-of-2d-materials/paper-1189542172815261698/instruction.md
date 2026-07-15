# X-ray Diffraction Analysis of Strain-Induced Diffuse Scattering

## Problem background
The high-temperature superconductor HgBa₂CuO₄₊δ (Hg1201) possesses a tetragonal structure, a single CuO₂ layer per unit cell, and minimal disorder, making it an ideal system to study the intrinsic response of the copper–oxygen plane to external perturbations. Uniaxial strain can break the four-fold rotational symmetry and has previously been shown to induce or reinforce charge order in cuprates such as YBa₂Cu₃O_6.67. In Hg1201, short-range two-dimensional charge-density-wave correlations have been observed at zero strain, but the effect of in-plane compressive strain on the lattice and any emergent electronic modulations remains an open question. This task addresses that question by analysing raw synchrotron X-ray diffraction data collected on a Hg1201 single crystal under varying a‑axis compression. The goal is to quantify the structural response (lattice parameters, Poisson ratios) and to detect, map, and characterise any strain-induced diffuse scattering features, including their wave vector, correlation length, and dependence on strain and temperature.

## Approach
The experiment consists of processing public-domain X‑ray diffraction images measured at the ID15B beamline (ESRF) with an incident photon energy of 30 keV. The dataset contains images for several uniaxial a‑axis strain levels (0 %, 0.05 %, 0.2 %, 0.5 %, 1.1 %) and temperatures (e.g. 30 K, 78 K, 101 K). The computational reproduction proceeds in two main phases:

**Phase 1 – Structural analysis.** For each strain condition, the raw frames are indexed and the orthorhombic unit cell is refined. This yields the lattice constants a, b, c, from which the strains εₐₐ, ε_bₒ, ε_cₑ are calculated. A linear fit of the perpendicular strains ε_bₒ and ε_cₑ against the compressive strain –εₐₐ provides the Poisson ratios ν_ba and ν_ca.

**Phase 2 – Diffuse scattering.** Two‑dimensional intensity maps are reconstructed in the (H 0 L) and (H K 2) reciprocal‑lattice planes. The zero‑strain pattern is subtracted from the strained patterns to highlight strain‑induced changes. Line‑cuts are taken along the H direction through the (412) and (4̄12) Bragg reflections. Any satellite peaks that emerge under strain are fitted with a Lorentzian profile I(q) = A / [(q − q₀)² + κ²] to extract the centre q₀, the width κ, and the correlation length ξ = 1/κ. The strain and temperature dependence of these parameters is examined. The first‑principles phonon simulations that support the interpretation in the original study are not required for this reproduction; the target is the purely experimental diffraction analysis.

All data‑reduction steps can be carried out with open‑source crystallographic tools (e.g. DIALS, pyFAI, xia2) in place of any proprietary software; the Python packages numpy, scipy, matplotlib, fabio and lmfit are suitable for the downstream analysis and fitting.

## Reproduction target
Using the raw diffraction dataset accessible via DOI 10.15151/ESRF‑DC‑1511962937, produce the following quantitative characterisation:

- Lattice parameters a, b, c and the corresponding strains εₐₐ, ε_bₒ, ε_cₑ for every nominal strain condition.
- Poisson ratios ν_ba = −ε_bₒ/εₐₐ and ν_ca = −ε_cₑ/εₐₐ with 1σ uncertainties, obtained from linear regression.
- One‑dimensional intensity cuts along H through the (412) and (4̄12) reflections for all strain and temperature conditions.
- Lorentzian‑fit parameters for any strain‑induced diffuse peaks: in‑plane wave‑vector component q₀, inverse correlation length κ, and real‑space correlation length ξ = 1/κ, with their 1σ uncertainties.
- An analysis of how these fitted quantities vary with strain (0 % to 1.1 %) and temperature (across the superconducting transition, e.g. 30 K, 78 K and 101 K).

All outputs must be derived from the public dataset; no other experimental data should be used.

## Assets

- ESRF Hg1201 strain diffraction dataset: 10.15151/ESRF-DC-1511962937
- Open-source crystallographic data reduction software (e.g. DIALS, xia2, pyFAI)
- Python analysis stack: pip install numpy scipy matplotlib fabio pyFAI lmfit

## Workflow steps

### Step 1: Retrieve raw diffraction data
- Role: process
- Action: Download the full raw X-ray diffraction dataset from ESRF Data Portal (doi:10.15151/ESRF-DC-1511962937) and organize by strain and temperature condition.
- Evidence: `/app/outputs/download_log.txt`

### Step 2: Extract lattice parameters
- Role: scored
- Action: For each strain condition (0%, 0.05%, 0.2%, 0.5%, 1.1%) index diffraction images, refine the orthorhombic unit cell, and record the lattice parameters a, b, c. Calculate ε_aa, ε_bb, ε_cc from fractional changes. Write results to lattice_parameters.csv.
- Output file: `/app/outputs/lattice_parameters.csv`
- Format: csv
- Contract: columns: condition_id, epsilon_aa, a, b, c, epsilon_bb, epsilon_cc (a,b,c in Å; epsilon dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Compute Poisson ratios
- Role: scored
- Action: Perform linear fits of ε_bb vs -ε_aa and ε_cc vs -ε_aa using the lattice parameters from step_02. Derive Poisson ratios ν_ba and ν_ca with 1σ uncertainties. Write results to poisson_ratios.csv.
- Output file: `/app/outputs/poisson_ratios.csv`
- Format: csv
- Contract: columns: ratio, value, uncertainty (1σ); rows: ν_ba, ν_ca
- Scoring: scored by hidden verifier

### Step 4: Prepare diffuse scattering maps and line cuts
- Role: scored
- Action: Reconstruct the 2D diffuse scattering intensity maps in the (H 0 L) and (H K 2) planes for each strain and temperature condition. Extract line-cuts along the H direction through the (412) and (4̄12) Bragg reflections. Output the intensity vs. H for every condition to diffuse_line_cuts.csv.
- Output file: `/app/outputs/diffuse_line_cuts.csv`
- Format: csv
- Contract: columns: condition_id, peak_label (e.g. ‘(412)’ or ‘(4̄12)’), H (r.l.u.), intensity (arb. units)
- Scoring: scored by hidden verifier

### Step 5: Fit strain-induced features and extract correlation parameters
- Role: scored (load-bearing)
- Action: Fit each satellite peak in the line cuts to a Lorentzian I(q) = A/[(q - q0)² + κ²]. Extract q0, κ, and the correlation length ξ = 1/κ with their 1σ uncertainties. Collate results across all conditions and write fitting_results.csv.
- Output file: `/app/outputs/fitting_results.csv`
- Format: csv
- Contract: columns: condition_id, peak_label, q0 (r.l.u.), q0_uncertainty, κ (r.l.u.⁻¹), κ_uncertainty, ξ (unit cells), ξ_uncertainty
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.csv`
- `/app/outputs/poisson_ratios.csv`
- `/app/outputs/diffuse_line_cuts.csv`
- `/app/outputs/fitting_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.csv
- path: `/app/outputs/lattice_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice parameters and strain values for each strain condition.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `epsilon_aa`, `a`, `b`, `c`, `epsilon_bb`, `epsilon_cc`
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `epsilon_aa`: dimensionless
    - `epsilon_bb`: dimensionless
    - `epsilon_cc`: dimensionless

### poisson_ratios.csv
- path: `/app/outputs/poisson_ratios.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Poisson ratios ν_ba and ν_ca with 1σ uncertainties.
- schema:
  - `type`: table
  - `required_columns`: `ratio`, `value`, `uncertainty`
  - `units`:
    - `value`: dimensionless
    - `uncertainty`: 1σ

### diffuse_line_cuts.csv
- path: `/app/outputs/diffuse_line_cuts.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Line cuts in H direction across designated Bragg reflections.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `peak_label`, `H`, `intensity`
  - `units`:
    - `H`: r.l.u.
    - `intensity`: arb. units

### fitting_results.csv
- path: `/app/outputs/fitting_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Fitted Lorentzian peak parameters for strain-induced diffuse scattering peaks.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `peak_label`, `q0`, `q0_uncertainty`, `κ`, `κ_uncertainty`, `ξ`, `ξ_uncertainty`
  - `units`:
    - `q0`: r.l.u.
    - `κ`: r.l.u.⁻¹
    - `ξ`: unit cells

Notes: Scored artifacts cover the complete experimental XRD analysis pipeline. The checker may recompute Poisson ratios from lattice_parameters.csv and may refit Lorentzians from diffuse_line_cuts.csv to verify the reported q0 and correlation length.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "epsilon_aa",
          "a",
          "b",
          "c",
          "epsilon_bb",
          "epsilon_cc"
        ],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "epsilon_aa": "dimensionless",
          "epsilon_bb": "dimensionless",
          "epsilon_cc": "dimensionless"
        }
      },
      "description": "Lattice parameters and strain values for each strain condition."
    },
    {
      "file": "poisson_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ratio",
          "value",
          "uncertainty"
        ],
        "units": {
          "value": "dimensionless",
          "uncertainty": "1σ"
        }
      },
      "description": "Poisson ratios ν_ba and ν_ca with 1σ uncertainties."
    },
    {
      "file": "diffuse_line_cuts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "peak_label",
          "H",
          "intensity"
        ],
        "units": {
          "H": "r.l.u.",
          "intensity": "arb. units"
        }
      },
      "description": "Line cuts in H direction across designated Bragg reflections."
    },
    {
      "file": "fitting_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "peak_label",
          "q0",
          "q0_uncertainty",
          "κ",
          "κ_uncertainty",
          "ξ",
          "ξ_uncertainty"
        ],
        "units": {
          "q0": "r.l.u.",
          "κ": "r.l.u.⁻¹",
          "ξ": "unit cells"
        }
      },
      "description": "Fitted Lorentzian peak parameters for strain-induced diffuse scattering peaks."
    }
  ],
  "notes": "Scored artifacts cover the complete experimental XRD analysis pipeline. The checker may recompute Poisson ratios from lattice_parameters.csv and may refit Lorentzians from diffuse_line_cuts.csv to verify the reported q0 and correlation length."
}
```

## How you are scored
A hidden verifier examines the four output files you produce (lattice_parameters.csv, poisson_ratios.csv, diffuse_line_cuts.csv, fitting_results.csv) and independently evaluates each one. The verifier can recompute Poisson ratios from your lattice‑parameter table, refit the Lorentzian profile to your line‑cut data, and check the consistency of the fitted parameters across conditions. It also assesses the qualitative behaviour (appearance and saturation of the strain‑induced signal, temperature dependence). Every scored artifact contributes a weighted portion to the final reward; no single number dominates. Simply reporting a value that cannot be traced to the submitted raw artifacts will not earn credit. The verifier expects that you have genuinely executed the data‑reduction and analysis pipeline on the specified dataset.
