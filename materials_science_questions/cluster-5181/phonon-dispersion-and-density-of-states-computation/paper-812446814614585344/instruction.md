# Electron‑phonon coupling parameter estimation via impurity‑center model for temperature‑dependent absorption

## Problem background
The B820 subunit of the bacterial light‑harvesting antenna LH1 is a bacteriochlorophyll dimer whose optical spectra are strongly influenced by electron–phonon coupling. Understanding how the protein environment modulates the electronic transition is important for modeling the energy transfer dynamics in photosynthesis. However, the key coupling parameters—the Debye–Waller factor (zero‑phonon line weight), the Huang–Rhys factor (strength of electron–phonon coupling), and the width of the inhomogeneous distribution—are difficult to extract directly because the zero‑phonon line is obscured by scattered light. These parameters must therefore be inferred indirectly from the temperature dependence of the absorption and fluorescence spectra, using a theoretical impurity‑center model that incorporates both homogeneous and inhomogeneous broadening.

## Approach
The core idea is to model the B820 dimer as an inhomogeneous ensemble of two‑level electronic systems coupled to a harmonic phonon bath. The homogeneous optical line shape consists of a narrow zero‑phonon line and a broad phonon sideband. The phonon sideband is built from multiphonon processes that are completely determined by a weighted phonon density of states and the temperature‑dependent phonon occupation numbers. The observed inhomogeneous absorption spectrum is the convolution of the homogeneous absorption with a Gaussian inhomogeneous distribution function (IDF), representing the spread of local environments.

The central constraint used to determine the unknown parameters is an experimental observation: the inhomogeneous absorption spectrum of B820 shows virtually no change when the temperature is raised from 4 K to 100 K. This implies that the Debye–Waller factor (which controls the zero‑phonon line strength) and the IDF width must be chosen such that the computed inhomogeneous absorption width remains essentially constant between these two temperatures. To implement this, one assumes a simple analytic form for the zero‑temperature phonon wing, Φ(ω,0) = ω exp(–ω/μ) with μ = 110 cm⁻¹, which has been found to match the 4 K luminescence measurements.

The workflow then proceeds in three stages. First, a grid search over the Debye–Waller factor and the IDF width is performed: for each (α,σ) combination, the inhomogeneous absorption spectrum is computed at 4 K and 100 K, and the pair that minimizes the change in spectral width (e.g., FWHM) is selected. Second, using the best α and the known zero‑temperature phonon wing, an iterative deconvolution extracts the weighted phonon density of states f₀(v). Finally, the Huang–Rhys factor S is obtained by integrating f₀(v)/v over all frequencies, and together with α and σ it constitutes the three headline parameters that characterize the electron–phonon coupling in this system. All steps can be carried out with standard numerical tools; no external experimental data are needed beyond the reported phonon‑wing shape and the temperature‑independence criterion.

## Reproduction target
Your goal is to produce a JSON file, `/app/outputs/estimated_parameters.json`, containing three numbers:

- `debye_waller_factor`: the Debye–Waller factor α (dimensionless)
- `huang_rhys_factor`: the Huang–Rhys factor S (dimensionless)
- `idf_width_cm-1`: the Gaussian inhomogeneous distribution width (in cm⁻¹)

These values must be obtained by enforcing the condition that the modelled inhomogeneous absorption spectrum does not change appreciably between 4 K and 100 K, using the impurity‑center model described in the Approach. You will need to:

- Implement the homogeneous line shape model with the given zero‑temperature phonon wing (Φ(ω,0) = ω exp(–ω/μ), μ = 110 cm⁻¹) and temperature‑dependent phonon wing via phonon occupation numbers.
- Scan over a range of α and IDF width values to find the (α,σ) pair that minimizes the temperature‑induced change in the inhomogeneous absorption width (e.g., FWHM or standard deviation).
- Extract the weighted phonon density of states f₀(v) by iterative deconvolution using the optimal α.
- Compute S = ∫ f₀(v)/v dv.

The final answer must be reported in exactly the specified JSON format; the hidden verifier will judge the correctness of these numbers against a reference derived from the original study. No external datasets need to be fetched—the computation relies solely on the prescribed model and the temperature‑independence constraint.

## Assets

- NumPy: pip install numpy
- SciPy: pip install scipy

## Workflow steps

### Step 1: Implement homogeneous line shape model
- Role: process
- Action: Implement the homogeneous absorption and fluorescence spectra of the impurity‑center model: zero‑temperature phonon wing Φ(ω,0)=ω exp(−ω/μ) with μ=110 cm⁻¹; temperature‑dependent phonon wing obtained by weighting the zero‑temperature phonon wing with Bose–Einstein occupation numbers (for ω>0, multiply by (n(ω,T)+1); for ω<0, multiply by n(|ω|,T)); and the convolution for selectively excited fluorescence and inhomogeneous absorption.
- Evidence: none

### Step 2: Scan Debye‑Waller factor and IDF width for temperature independence
- Role: process
- Action: For a grid of Debye‑Waller factor α and Gaussian inhomogeneous distribution width σ, compute the inhomogeneous absorption spectrum at T=4 K and T=100 K by convolution. Use a broadening metric (FWHM or standard deviation) to find the (α,σ) pair that minimizes the change in absorption width between the two temperatures. Save the grid‑scan results, including the best α and σ, to /app/outputs/broadening_scan.json.
- Evidence: `/app/outputs/broadening_scan.json`

### Step 3: Extract weighted phonon density of states
- Role: process
- Action: Using the best α from step 2 and the known zero‑temperature phonon wing, compute the weighted phonon density of states f₀(v) by iterative deconvolution using the iterative formula f₀(ω) = (Φ(ω,0) / α) − (1/(α ω)) ∫₀^ω Φ(ω−v, 0) v f₀(v) dv. Save the result as a CSV file with columns v (frequency in cm⁻¹) and f0 (weighted phonon density) to /app/outputs/phonon_dos.csv.
- Evidence: `/app/outputs/phonon_dos.csv`

### Step 4: Report estimated parameters
- Role: scored (load-bearing)
- Action: Read the optimal α and σ from broadening_scan.json and the phonon density from phonon_dos.csv. Compute the Huang‑Rhys factor S = ∫ f₀(v)/v dv. Report the three headline quantities—Debye‑Waller factor α, Huang‑Rhys factor S, and inhomogeneous distribution width (σ, in cm⁻¹)—in /app/outputs/estimated_parameters.json.
- Output file: `/app/outputs/estimated_parameters.json`
- Format: json
- Contract: {"debye_waller_factor": float, "huang_rhys_factor": float, "idf_width_cm-1": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/estimated_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### estimated_parameters.json
- path: `/app/outputs/estimated_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The Debye‑Waller factor α, Huang‑Rhys factor S, and the Gaussian inhomogeneous distribution width (cm⁻¹) obtained by enforcing temperature independence of the modelled absorption below 100 K. The checker compares these values to the paper’s reported reference within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `debye_waller_factor`: float
    - `huang_rhys_factor`: float
    - `idf_width_cm-1`: float
  - `units`:
    - `debye_waller_factor`: dimensionless
    - `huang_rhys_factor`: dimensionless
    - `idf_width_cm-1`: cm⁻¹

Notes: The model assumes a phonon wing shape Φ(ω,0)=ω exp(-ω/μ) with μ=110 cm⁻¹ (as reported in the paper). The temperature‑independence condition below 100 K serves as the sole fitting constraint. The Wong‑Rhys factor S is obtained from the integral of f₀(v)/v, not from a simple log‑relation with α. The checker compares the three reported numbers to the hidden reference values; only the correct model yields the correct S.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "estimated_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "debye_waller_factor": "float",
          "huang_rhys_factor": "float",
          "idf_width_cm-1": "float"
        },
        "units": {
          "debye_waller_factor": "dimensionless",
          "huang_rhys_factor": "dimensionless",
          "idf_width_cm-1": "cm⁻¹"
        }
      },
      "description": "The Debye‑Waller factor α, Huang‑Rhys factor S, and the Gaussian inhomogeneous distribution width (cm⁻¹) obtained by enforcing temperature independence of the modelled absorption below 100 K. The checker compares these values to the paper’s reported reference within tolerances."
    }
  ],
  "notes": "The model assumes a phonon wing shape Φ(ω,0)=ω exp(-ω/μ) with μ=110 cm⁻¹ (as reported in the paper). The temperature‑independence condition below 100 K serves as the sole fitting constraint. The Wong‑Rhys factor S is obtained from the integral of f₀(v)/v, not from a simple log‑relation with α. The checker compares the three reported numbers to the hidden reference values; only the correct model yields the correct S."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the artifacts you write under `/app/outputs`. The verifier will:

1. Check that the final output file `/app/outputs/estimated_parameters.json` exists and contains numeric values for all three required fields.
2. Compare the reported Debye‑Waller factor, Huang‑Rhys factor, and IDF width to a hidden set of reference values derived from the original work. The comparison uses tolerances that account for legitimate numerical differences between independent implementations of the model. (The exact tolerances are hidden and part of the verifier; they are set to reward honest reproduction while not requiring bit‑level agreement with the original paper.)
3. The overall reward is determined mainly by how close your final triplet of values is to the reference; reaching all three within tolerance earns full credit, while missing one or more reduces the score. The intermediate artifacts (`broadening_scan.json` and `phonon_dos.csv`) may also be audited for consistency, but the primary scoring weight is on the final `estimated_parameters.json`.

Simply reporting numbers without actually executing the impurity‑center model and parameter scan will not pass, because the verifier can verify that the values are not arbitrary (for example, by cross‑checking consistency with the intermediate scanned grid or by requiring that the numerical values satisfy the internal relationships of the model). You are expected to run the computation and write the true result of your workflow.
