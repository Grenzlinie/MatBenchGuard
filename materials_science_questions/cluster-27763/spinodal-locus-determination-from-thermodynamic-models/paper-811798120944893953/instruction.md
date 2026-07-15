# Coarse-Grained Soft-Core Potentials and Mesoscale Simulation of Binary Polymer Mixtures

## Problem background
Understanding the large‑scale structure and phase behavior of binary polymer mixtures is crucial for materials design. As a polymer blend approaches spinodal decomposition, concentration‑fluctuation length scales diverge, making fully atomistic simulations prohibitively expensive. An effective strategy is to coarse‑grain each polymer chain into a single soft colloidal particle and derive effective interaction potentials from liquid‑state theory. This task implements such a formalism and uses it to compute center‑of‑mass pair correlation functions and the concentration‑fluctuation structure factor for a prototypical blend, thereby testing the predictive power of the analytical coarse‑graining approach.

## Approach
The method has two main parts: an analytical theory and a mesoscopic molecular dynamics (MD) simulation. First, monomer‑level structure is described by the thread PRISM model, which provides analytical monomer‑monomer total correlation functions. A generalized Ornstein–Zernike equation connects these to center‑of‑mass (com) correlation functions using a Gaussian com‑monomer form factor and the Debye intramolecular structure factor, yielding reciprocal‑space com total pair correlation functions that are Fourier‑transformed to real space. Second, the hypernetted‑chain (HNC) closure together with the Ornstein–Zernike relations for a binary soft‑sphere liquid converts the com correlation functions into effective pair potentials v(r) in units of k_B T. Third, the analytical formalism is evaluated for the hhPP/PE blend (parameters provided below) at several reduced temperatures: athermal (χ = 0) and χ/χ_s = 0.1, 0.5, 0.7. Fourth, the athermal v(r) is used in a mesoscopic NVE MD simulation of 5324 soft particles to directly obtain com total correlation functions from trajectories. Finally, the concentration‑fluctuation structure factor S^{φφ}(k) is computed from the analytical h(r) via the Bhatia–Thornton transformation. All results are to be output as numerically tabulated curves.

## Reproduction target
For the hhPP/PE blend (N_A = N_B = 96, R_gA = 12.32 Å, γ = 1.34, ρ = 0.0332 sites/Å³, volume fraction φ = 0.5), compute the center‑of‑mass total pair correlation functions h_cc(r) (AA, AB, BB) at four thermodynamic conditions: athermal (χ = 0), χ/χ_s = 0.1, χ/χ_s = 0.5, and χ/χ_s = 0.7. From these, derive the effective pair potentials v_cc(r) (in k_B T units) for the same conditions using the HNC closure. Perform one mesoscopic MD simulation for the athermal case (χ = 0) with 5324 particles, a cubic box of side 2×8.549 R_g⁻¹, and φ = 0.5, and extract the com total correlation functions from the equilibrium trajectory. Lastly, compute the concentration‑fluctuation structure factor S^{φφ}(k) from the analytical h_cc(r) for all four conditions. Provide all results as ordered CSV files under /app/outputs.

## Assets

- hhPP/PE blend parameters
- LAMMPS molecular dynamics simulator: https://www.lammps.org/

## Workflow steps

### Step 1: Analytical center-of-mass pair correlation functions
- Role: scored
- Action: Implement the mapping from monomer-level structure to center-of-mass total pair correlation functions. First, compute the monomer-monomer total correlation functions in real space, h_{\alpha\beta}^{mm}(r), using the thread PRISM expressions for a binary blend: h_{AA}^{mm}(r) = \frac{3}{\pi \rho r \sigma_{AB}^2} \left[ \frac{1-\phi}{\phi} e^{-r/\xi_\phi} + \gamma^2 e^{-r/\xi_{\rho_{AA}}} - \frac{1}{\phi} \frac{\sigma_{AB}^2}{\sigma_A^2} e^{-r/\xi_{cA}} \right], h_{BB}^{mm}(r) = \frac{3}{\pi \rho r \sigma_{AB}^2} \left[ \frac{\phi}{1-\phi} e^{-r/\xi_\phi} + \gamma^{-2} e^{-r/\xi_{\rho_{BB}}} - \frac{1}{1-\phi} \frac{\sigma_{AB}^2}{\sigma_B^2} e^{-r/\xi_{cB}} \right], h_{AB}^{mm}(r) = \frac{3}{\pi \rho r \sigma_{AB}^2} \left[ -e^{-r/\xi_\phi} + e^{-r/\xi_{\rho_{AB}}} \right]. The length scales: \xi_\phi = \frac{\sigma_{AB}}{\sqrt{24 \phi(1-\phi) \chi_s (1 - \chi/\chi_s)}}, \xi_{c\alpha} = R_{g\alpha}/\sqrt{2}, \xi_{\rho\alpha\beta}^{-1} = \frac{\pi \rho \sigma_{\alpha\beta}^2}{3} + \xi_{c\alpha\beta}^{-1}, with \xi_{c\alpha\beta} = \sqrt{(R_{g\alpha}^2+R_{g\beta}^2)/4}, \sigma_{\alpha\beta}^2 = \phi_\beta \sigma_\alpha^2 + \phi_\alpha \sigma_\beta^2, and \sigma_\alpha = (6/N_\alpha)^{1/2} R_{g\alpha}. Parameters: N_A=N_B=96, R_{gA}=12.32 Å, R_{gB}=γ R_{gA} with γ=1.34, ρ=0.0332 sites/Å³, φ=0.5, χ_s = 1/(2N_A φ)+1/(2N_B(1-φ)). For each condition, set χ accordingly: athermal χ=0, or χ = χ_s * (χ/χ_s) for 0.1, 0.5, 0.7. Fourier transform h_{\alpha\beta}^{mm}(r) to get h_{\alpha\beta}^{mm}(k). Use Debye form factor: ω_{\alpha\alpha}^{mm}(k) = \frac{2 N_\alpha}{k^4 R_{g\alpha}^4} [ e^{-k^2 R_{g\alpha}^2} - 1 + k^2 R_{g\alpha}^2 ]. Use Gaussian com-monomer form factor: ω_{\alpha\alpha}^{cm}(k) = N_\alpha \exp(-k^2 R_{g\alpha}^2 / 6). Then compute h_{\alpha\beta}^{cc}(k) = \frac{\omega_{\alpha\alpha}^{cm}(k) \omega_{\beta\beta}^{cm}(k)}{\omega_{\alpha\alpha}^{cm}(k) \omega_{\beta\beta}^{mm}(k)} h_{\alpha\beta}^{mm}(k). Inverse Fourier transform to real space to obtain h_{\alpha\beta}^{cc}(r). Output h_{AA}, h_{AB}, h_{BB} for each condition.
- Output file: `/app/outputs/analytical_hcc.csv`
- Format: csv
- Contract: Columns: r (Å), condition (label: 'athermal', 'chi0.1', 'chi0.5', 'chi0.7'), h_AA (float), h_AB (float), h_BB (float).
- Scoring: scored by hidden verifier

### Step 2: Effective soft-core potentials via HNC closure
- Role: scored
- Action: Using h_{\alpha\beta}^{cc}(r) from step 1, derive effective pair potential v_{\alpha\beta}^{cc}(r) (in k_B T units). 1. Fourier transform h_{\alpha\beta}^{cc}(r) to reciprocal space to obtain h_{\alpha\beta}^{cc}(k). 2. Compute partial static structure factors of the coarse-grained liquid: S_{AA}(k) = \phi + \phi^2 \rho_{ch} h_{AA}^{cc}(k), S_{BB}(k) = 1-\phi + (1-\phi)^2 \rho_{ch} h_{BB}^{cc}(k), S_{AB}(k) = \phi (1-\phi) \rho_{ch} h_{AB}^{cc}(k), where \rho_{ch} = \rho / N (N=96). 3. Direct correlation functions from OZ relations for a binary mixture: |S_{cc}(k)| = S_{AA}(k) S_{BB}(k) - [S_{AB}(k)]^2, c_{AA}^{cc}(k) = 1/\rho_{c,A} - S_{BB}(k) / ((\rho_{c,A}+\rho_{c,B}) |S_{cc}(k)|), c_{BB}^{cc}(k) = 1/\rho_{c,B} - S_{AA}(k) / ((\rho_{c,A}+\rho_{c,B}) |S_{cc}(k)|), c_{AB}^{cc}(k) = S_{AB}(k) / ((\rho_{c,A}+\rho_{c,B}) |S_{cc}(k)|), with \rho_{c,A} = \phi \rho / N, \rho_{c,B} = (1-\phi) \rho / N. 4. Inverse Fourier transform c_{\alpha\beta}^{cc}(k) to real space to get c_{\alpha\beta}^{cc}(r). 5. Apply HNC closure: v_{\alpha\beta}^{cc}(r) = h_{\alpha\beta}^{cc}(r) - \ln[1 + h_{\alpha\beta}^{cc}(r)] - c_{\alpha\beta}^{cc}(r). Output v_{AA}, v_{AB}, v_{BB} for each condition.
- Output file: `/app/outputs/effective_potentials.csv`
- Format: csv
- Contract: Columns: r (Å), condition (label as above), v_AA (float, dimensionless (k_B T units)), v_AB (float), v_BB (float).
- Scoring: scored by hidden verifier

### Step 3: Mesoscopic MD simulation and h_cc extraction (athermal)
- Role: scored (load-bearing)
- Action: Run a classical MD simulation in the NVE ensemble using the effective potential obtained for the athermal case (χ=0) from the previous step. Use 5324 soft colloidal particles, a periodic cubic box of side length 2×8.549 R_g⁻¹ (≈17.098 R_g), and volume fraction φ=0.5. Equilibrate, then collect equilibrium trajectories. From the trajectory, compute the center-of-mass radial distribution functions and output the total correlation functions h_cc(r) for AA, AB, and BB interactions.
- Output file: `/app/outputs/simulation_hcc.csv`
- Format: csv
- Contract: Columns: r (Å), h_AA_sim (float), h_AB_sim (float), h_BB_sim (float).
- Scoring: scored by hidden verifier

### Step 4: Concentration fluctuation structure factor
- Role: scored
- Action: From analytical h_{\alpha\beta}^{cc}(r) for each condition, compute concentration fluctuation structure factor S^{φφ}(k). 1. Compute partial static structure factors by Fourier transform of real-space correlations: S_{AA}(k) = \phi + 4\pi \phi^2 \rho_{ch} \int_0^\infty r^2 \frac{\sin(kr)}{kr} h_{AA}^{cc}(r) dr, S_{BB}(k) = 1-\phi + 4\pi (1-\phi)^2 \rho_{ch} \int_0^\infty r^2 \frac{\sin(kr)}{kr} h_{BB}^{cc}(r) dr, S_{AB}(k) = 4\pi \phi(1-\phi) \rho_{ch} \int_0^\infty r^2 \frac{\sin(kr)}{kr} h_{AB}^{cc}(r) dr, with \rho_{ch} = \rho / N. 2. Concentration–concentration structure factor: S^{φφ}(k) = (1-\phi)^2 S_{AA}(k) + \phi^2 S_{BB}(k) - 2\phi(1-\phi) S_{AB}(k). Output S^{φφ}(k) for each condition.
- Output file: `/app/outputs/structure_factor_analytical.csv`
- Format: csv
- Contract: Columns: k (Å⁻¹), condition (label as above), S_phi_phi (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/analytical_hcc.csv`
- `/app/outputs/effective_potentials.csv`
- `/app/outputs/simulation_hcc.csv`
- `/app/outputs/structure_factor_analytical.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### analytical_hcc.csv
- path: `/app/outputs/analytical_hcc.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Centers-of-mass total pair correlation functions, recomputed by the checker from the analytical formalism; compared within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `r`, `condition`, `h_AA`, `h_AB`, `h_BB`
  - `units`:
    - `r`: Å
    - `condition`: string
    - `h_AA`: dimensionless
    - `h_AB`: dimensionless
    - `h_BB`: dimensionless

### effective_potentials.csv
- path: `/app/outputs/effective_potentials.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Effective soft-core pair potentials derived via HNC closure, recomputed and compared by the checker.
- schema:
  - `type`: table
  - `required_columns`: `r`, `condition`, `v_AA`, `v_AB`, `v_BB`
  - `units`:
    - `r`: Å
    - `condition`: string
    - `v_AA`: k_B T
    - `v_AB`: k_B T
    - `v_BB`: k_B T

### simulation_hcc.csv
- path: `/app/outputs/simulation_hcc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pair correlation functions from mesoscopic MD; consistency checked against the analytical athermal curve within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `r`, `h_AA_sim`, `h_AB_sim`, `h_BB_sim`
  - `units`:
    - `r`: Å
    - `h_AA_sim`: dimensionless
    - `h_AB_sim`: dimensionless
    - `h_BB_sim`: dimensionless

### structure_factor_analytical.csv
- path: `/app/outputs/structure_factor_analytical.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Concentration fluctuation structure factor recomputed by the checker from the submitted analytical h_cc.
- schema:
  - `type`: table
  - `required_columns`: `k`, `condition`, `S_phi_phi`
  - `units`:
    - `k`: Å⁻¹
    - `condition`: string
    - `S_phi_phi`: dimensionless

Notes: All numerical values are unitless or in specified SI/derived units. The checker recomputes analytical h_cc, v_cc, and S^ϕϕ from the same public parameters and compares within tolerances not disclosed here. The simulation h_cc must be consistent with the analytical athermal curve; the reference is recomputed internally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "analytical_hcc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "condition",
          "h_AA",
          "h_AB",
          "h_BB"
        ],
        "units": {
          "r": "Å",
          "condition": "string",
          "h_AA": "dimensionless",
          "h_AB": "dimensionless",
          "h_BB": "dimensionless"
        }
      },
      "description": "Centers-of-mass total pair correlation functions, recomputed by the checker from the analytical formalism; compared within tolerance."
    },
    {
      "file": "effective_potentials.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "condition",
          "v_AA",
          "v_AB",
          "v_BB"
        ],
        "units": {
          "r": "Å",
          "condition": "string",
          "v_AA": "k_B T",
          "v_AB": "k_B T",
          "v_BB": "k_B T"
        }
      },
      "description": "Effective soft-core pair potentials derived via HNC closure, recomputed and compared by the checker."
    },
    {
      "file": "simulation_hcc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "h_AA_sim",
          "h_AB_sim",
          "h_BB_sim"
        ],
        "units": {
          "r": "Å",
          "h_AA_sim": "dimensionless",
          "h_AB_sim": "dimensionless",
          "h_BB_sim": "dimensionless"
        }
      },
      "description": "Pair correlation functions from mesoscopic MD; consistency checked against the analytical athermal curve within tolerance."
    },
    {
      "file": "structure_factor_analytical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "k",
          "condition",
          "S_phi_phi"
        ],
        "units": {
          "k": "Å⁻¹",
          "condition": "string",
          "S_phi_phi": "dimensionless"
        }
      },
      "description": "Concentration fluctuation structure factor recomputed by the checker from the submitted analytical h_cc."
    }
  ],
  "notes": "All numerical values are unitless or in specified SI/derived units. The checker recomputes analytical h_cc, v_cc, and S^ϕϕ from the same public parameters and compares within tolerances not disclosed here. The simulation h_cc must be consistent with the analytical athermal curve; the reference is recomputed internally."
}
```

## How you are scored
A hidden verifier independently re-derives the expected results for each of the four scored artifacts and compares them to your submitted files. For the analytical artifacts (h_cc, effective potentials, structure factor), the checker recomputes the same quantities from the public parameters using a trusted implementation and checks agreement within appropriate tolerances. The simulation h_cc is checked for consistency with the analytical athermal curve (the checker recomputes that reference). The verifier combines weighted scores from all stages into a final reward in [0, 1]; simply reporting numbers is not sufficient — your submitted data must be the output of your own computation. The exact tolerance thresholds and stage weights are not disclosed.
