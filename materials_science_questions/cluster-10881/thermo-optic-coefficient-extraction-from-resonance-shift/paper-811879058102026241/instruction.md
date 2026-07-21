# Computation of Cladding Mode Effective Indices in an Optical Fiber with Two Non-Concentric Cores

## Problem background
Fiber devices based on long-period gratings can couple light between cores via cladding modes. In an asymmetric geometry with one core near the fiber axis and a second core off-centre, the true cladding modes differ from those of a simpler coreless (two‑layer) model. This task computes the effective indices and field profiles of several cladding modes using a full dual-core semianalytical approach and compares them with the coreless approximation.

## Mathematical details

### Geometry and parameters
- Core 1: radius \(a_1=3.0\;\mu\text{m}\), refractive index \(n_1=1.4530\), offset distance from fibre centre \(d_1=32\;\mu\text{m}\).
- Core 2: radius \(a_2=3.6\;\mu\text{m}\), refractive index \(n_2=1.4530\), placed at the fibre centre (\(d_2=0\)).
- Cladding: radius \(a_3=62.5\;\mu\text{m}\), refractive index \(n_3=1.4440\).
- Ambient: refractive index \(n_4=1.0\) (air).
- Free-space wavelength \(\lambda=1.550\;\mu\text{m}\).

### Basic definitions
\[
k_0 = \frac{2\pi}{\lambda},\qquad
\kappa_v = k_0\sqrt{n_v^2-n_{\text{eff}}^2}\;(v=1,2,3),\qquad
\gamma = k_0\sqrt{n_{\text{eff}}^2-n_4^2}
\]
where \(n_{\text{eff}}\) is the effective index to be determined. The azimuthal modes are truncated at \(m=-12,\dots,12\) (25 terms). \(J_m\), \(Y_m\), \(K_m\) denote the Bessel, Neumann, and modified Bessel functions; a prime indicates differentiation with respect to the argument.

### Field expansion and boundary conditions
In the cladding region (3) the scalar field \(\varphi\) is expanded as
\[
\varphi_3(r_0,\theta_0) = \Phi_3^T(r_0,\theta_0)\cdot\mathbf{A}
                       + \Pi_3^T(r_1,\theta_1)\cdot\mathbf{B}_1
                       + \Pi_3^T(r_2,\theta_2)\cdot\mathbf{B}_2,
\]
in core 1 (region 1): \(\varphi_1 = \Phi_1^T(r_1,\theta_1)\cdot\mathbf{C}_1\),
in core 2 (region 2): \(\varphi_2 = \Phi_2^T(r_2,\theta_2)\cdot\mathbf{C}_2\),
in ambient (region 4): \(\varphi_4 = \Psi_4^T(r_0,\theta_0)\cdot\mathbf{D}\),

where the column vectors contain the expansion coefficients, e.g. \(\mathbf{A}=[A_m]\), and
\[
\Phi_v(r,\theta) = \big[J_m(\kappa_v r)\,e^{im\theta}\big]_{m=-M}^{M},\qquad
\Pi_3(r,\theta)   = \big[Y_m(\kappa_3 r)\,e^{im\theta}\big]_{m=-M}^{M},\qquad
\Psi_4(r,\theta)  = \big[K_m(\gamma r)\,e^{im\theta}\big]_{m=-M}^{M}.
\]

### Translation matrices
To express fields from one cylindrical coordinate system in another, the addition theorem gives the following infinite‑dimensional matrices (truncated to \(M=12\)):

\[
\begin{aligned}
[\boldsymbol{\alpha}_{12}]_{nm} &= Y_{n-m}(\kappa_3 d), &
[\boldsymbol{\alpha}_{21}]_{nm} &= (-1)^{n-m}Y_{n-m}(\kappa_3 d),\\[2pt]
[\boldsymbol{\eta}_{10}]_{nm} &= J_{n-m}(\kappa_3 d_1), &
[\boldsymbol{\eta}_{01}]_{nm} &= (-1)^{n-m}J_{n-m}(\kappa_3 d_1),
\end{aligned}
\]
where \(d = d_1 = 32\;\mu\text{m}\) is the distance between the two cores. Because \(d_2=0\), \(\boldsymbol{\eta}_{20}=\boldsymbol{\eta}_{02}=\mathbf{I}\) (the identity matrix).

### Scattering matrices at the core interfaces
Each core boundary yields a diagonal matrix:

\[
\begin{aligned}
\big[\mathbf{T}_1\big]_{mm} &=
-\frac{\kappa_3 J_m(\kappa_1 a_1)J_m'(\kappa_3 a_1) - \kappa_1 J_m'(\kappa_1 a_1)J_m(\kappa_3 a_1)}
       {\kappa_3 J_m(\kappa_1 a_1)Y_m'(\kappa_3 a_1) - \kappa_1 J_m'(\kappa_1 a_1)Y_m(\kappa_3 a_1)},\\[4pt]
\big[\mathbf{T}_2\big]_{mm} &=
-\frac{\kappa_3 J_m(\kappa_2 a_2)J_m'(\kappa_3 a_2) - \kappa_2 J_m'(\kappa_2 a_2)J_m(\kappa_3 a_2)}
       {\kappa_3 J_m(\kappa_2 a_2)Y_m'(\kappa_3 a_2) - \kappa_2 J_m'(\kappa_2 a_2)Y_m(\kappa_3 a_2)},\\[4pt]
\big[\mathbf{U}\big]_{mm} &=
\frac{\kappa_3 J_m(\kappa_3 a_1)Y_m'(\kappa_3 a_1) - \kappa_3 J_m'(\kappa_3 a_1)Y_m(\kappa_3 a_1)}
     {\kappa_3 J_m(\kappa_1 a_1)Y_m'(\kappa_3 a_1) - \kappa_1 J_m'(\kappa_1 a_1)Y_m(\kappa_3 a_1)},\\[4pt]
\big[\mathbf{V}\big]_{mm} &=
\frac{\kappa_3 J_m(\kappa_3 a_2)Y_m'(\kappa_3 a_2) - \kappa_3 J_m'(\kappa_3 a_2)Y_m(\kappa_3 a_2)}
     {\kappa_3 J_m(\kappa_2 a_2)Y_m'(\kappa_3 a_2) - \kappa_2 J_m'(\kappa_2 a_2)Y_m(\kappa_3 a_2)}.
\end{aligned}
\]

### Coupling matrices \(\overline{\mathbf{T}}_1\), \(\overline{\mathbf{T}}_2\), \(\overline{\mathbf{T}}_0\)
\[
\begin{aligned}
\overline{\mathbf{T}}_1 &= (\mathbf{I} - \mathbf{T}_1\boldsymbol{\alpha}_{12}\mathbf{T}_2\boldsymbol{\alpha}_{21})^{-1}
                          \mathbf{T}_1\big(\boldsymbol{\eta}_{10} + \boldsymbol{\alpha}_{12}\mathbf{T}_2\boldsymbol{\eta}_{20}\big),\\
\overline{\mathbf{T}}_2 &= (\mathbf{I} - \mathbf{T}_2\boldsymbol{\alpha}_{21}\mathbf{T}_1\boldsymbol{\alpha}_{12})^{-1}
                          \mathbf{T}_2\big(\boldsymbol{\eta}_{20} + \boldsymbol{\alpha}_{21}\mathbf{T}_1\boldsymbol{\eta}_{10}\big),\\
\overline{\mathbf{T}}_0 &= \boldsymbol{\eta}_{01}\overline{\mathbf{T}}_1 + \boldsymbol{\eta}_{02}\overline{\mathbf{T}}_2
                        = \boldsymbol{\eta}_{01}\overline{\mathbf{T}}_1 + \overline{\mathbf{T}}_2 \quad (\text{since }\boldsymbol{\eta}_{02}=\mathbf{I}).
\end{aligned}
\]

### Eigenvalue equation for the dual-core cladding modes
The outer boundary at \(r_0=a_3\) leads to

\[
\det\!\big(\mathbf{F} + \overline{\mathbf{T}}_0\big) = 0,
\]
where \(\mathbf{F}\) is a diagonal matrix with entries

\[
F_{mm} = \frac{J_m'(\kappa_3 a_3)\big[\tilde{K}_m(\gamma a_3) - \tilde{J}_m(\kappa_3 a_3)\big]}
               {Y_m'(\kappa_3 a_3)\big[\tilde{K}_m(\gamma a_3) - \tilde{Y}_m(\kappa_3 a_3)\big]},
\]

and the auxiliary quantities are

\[
\tilde{J}_m(\kappa_3 a_3) = \frac{J_m(\kappa_3 a_3)}{\kappa_3 J_m'(\kappa_3 a_3)},\quad
\tilde{Y}_m(\kappa_3 a_3) = \frac{Y_m(\kappa_3 a_3)}{\kappa_3 Y_m'(\kappa_3 a_3)},\quad
\tilde{K}_m(\gamma a_3)   = \frac{K_m(\gamma a_3)}{\gamma K_m'(\gamma a_3)}.
\]

Roots of the determinant equation give the effective indices \(n_{\text{eff}}\) of the cladding modes. The three roots closest to the coreless LP\(_{0n}\) values correspond to the modes labeled LP\(_{03}'\), LP\(_{04}'\), and LP\(_{06}'\).

### Coreless (two‑layer) effective indices
Ignoring both cores yields a two‑layer fibre (cladding + ambient). In this limit the coupling matrices vanish (\(\overline{\mathbf{T}}_0=\mathbf{0}\)), and the effective indices \(n_{\text{eff}}^{\text{coreless}}\) are obtained from

\[
\det\!\big(\mathbf{F}\big) = 0,
\]

using the same \(\mathbf{F}\) defined above. For each cladding mode, compute the signed difference
\[
\Delta n_{\text{eff}} = n_{\text{eff}} - n_{\text{eff}}^{\text{coreless}}.
\]

### Field profile reconstruction
Once \(n_{\text{eff}}\) is found for a mode, choose the null‑space vector \(\mathbf{A}\) of the matrix \(\mathbf{F}+\overline{\mathbf{T}}_0\) (normalised such that the maximum of \(|\varphi|\) is 1). The field in the cladding region (\(r_0 \le a_3\)) follows from

\[
\varphi_3(r_0,\theta_0) = \Big[\mathbf{\Phi}_3^T(r_0,\theta_0) + \mathbf{\Pi}_3^T(r_0,\theta_0)\,\overline{\mathbf{T}}_0\Big] \mathbf{A},
\]

where the vector functions are evaluated at each observation point. The radial profile at a fixed azimuthal angle \(\theta_0\) is then \(|\varphi_3(r_0,\theta_0)|\).

## Approach
1. Build the matrices \(\mathbf{F}\) and \(\overline{\mathbf{T}}_0\) as functions of \(n_{\text{eff}}\) according to the formulas above.
2. Locate the three desired dual‑core effective indices by root‑finding on \(\det(\mathbf{F}+\overline{\mathbf{T}}_0)\).
3. Compute the corresponding coreless effective indices from \(\det(\mathbf{F})=0\).
4. For the LP\(_{03}'\) mode, reconstruct the normalised radial field along \(\theta_0=0\) and \(\theta_0=\pi\), sampling \(r_0 \in [0, 62.5]\;\mu\text{m}\).

## Workflow steps

### Step 1: Assemble eigenvalue matrices
- Role: process
- Action: Implement the construction of the diagonal matrix \(\mathbf{F}(n_{\text{eff}})\) and the coupling matrix \(\overline{\mathbf{T}}_0(n_{\text{eff}})\) using all formulas from the Mathematical details section. Use the given fibre parameters and truncate azimuthal orders at \(m=\pm12\).
- Evidence: (optional) you may log progress to `/app/outputs/matrix_assembly.log`.

### Step 2: Solve cladding mode effective indices
- Role: scored (load-bearing)
- Action: Numerically locate the roots of \(\det(\mathbf{F}+\overline{\mathbf{T}}_0)=0\) that correspond to LP\(_{03}'\), LP\(_{04}'\), and LP\(_{06}'\) modes. Compute the coreless effective indices for each mode from \(\det(\mathbf{F})=0\). Write the results to a CSV file with the following columns:
  `mode`, `n_eff`, `n_eff_coreless`, `delta_n_eff`.
  Each `n_eff` and `n_eff_coreless` must be given with at least 8 significant digits.
- Output file: `/app/outputs/effective_indices.csv`
- Format: csv
- Contract: 
  - `mode` (str): one of 'LP03\'', 'LP04\'', 'LP06\''
  - `n_eff` (float): effective index from the dual‑core model
  - `n_eff_coreless` (float): effective index from the two‑layer (coreless) model
  - `delta_n_eff` (float): \(\Delta n_{\text{eff}} = n_{\text{eff}} - n_{\text{eff}}^{\text{coreless}}\)
- Scoring: scored by hidden verifier

### Step 3: Compute radial field profile for LP03' mode
- Role: scored
- Action: Using the effective index obtained for LP\(_{03}'\), reconstruct the normalised field amplitude along the radial direction at azimuthal angles \(\theta_0=0\) and \(\theta_0=\pi\). Normalise such that the global maximum of the amplitude is 1. Sample \(r_0\) from 0 to 62.5 µm (inclusive, a fine grid of at least 500 points). Write the data to CSV.
- Output file: `/app/outputs/field_profile_LP03prime.csv`
- Format: csv
- Contract: 
  - `r_um` (float): radial coordinate in µm
  - `amplitude_theta0` (float): normalised field amplitude at \(\theta_0=0\)
  - `amplitude_theta_pi` (float): normalised field amplitude at \(\theta_0=\pi\)
- Scoring: scored by hidden verifier

## Output files
Place all artefacts under `/app/outputs`:
- `/app/outputs/effective_indices.csv`
- `/app/outputs/field_profile_LP03prime.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_indices.csv
- path: `/app/outputs/effective_indices.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective indices of the three cladding modes (dual-core model), the corresponding coreless fiber effective indices, and their signed difference \(\Delta n_{\text{eff}}\) at \(\lambda=1.550\;\mu\text{m}\) for the given fiber parameters.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `n_eff`, `n_eff_coreless`, `delta_n_eff`
  - `units`:
    - `n_eff`: dimensionless (effective index)
    - `n_eff_coreless`: dimensionless (effective index)
    - `delta_n_eff`: dimensionless (difference)

### field_profile_LP03prime.csv
- path: `/app/outputs/field_profile_LP03prime.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Normalized radial field profile of the LP03′ mode along \(\theta_0=0\) and \(\theta_0=\pi\), demonstrating the azimuthally asymmetric intensity distribution.
- schema:
  - `type`: table
  - `required_columns`: `r_um`, `amplitude_theta0`, `amplitude_theta_pi`
  - `units`:
    - `r_um`: µm
    - `amplitude_theta0`: normalized field amplitude
    - `amplitude_theta_pi`: normalized field amplitude

Notes: The task reproduces the effective indices (dual-core and coreless) and the field profile for the given geometry, demonstrating the difference between the two models as highlighted in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_indices.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "n_eff",
          "n_eff_coreless",
          "delta_n_eff"
        ],
        "units": {
          "n_eff": "dimensionless (effective index)",
          "n_eff_coreless": "dimensionless (effective index)",
          "delta_n_eff": "dimensionless (difference)"
        }
      },
      "description": "Effective indices of the three cladding modes (dual-core model), the corresponding coreless fiber effective indices, and their signed difference delta_n_eff = n_eff - n_eff_coreless, at λ=1.550 µm for the given fiber parameters."
    },
    {
      "file": "field_profile_LP03prime.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_um",
          "amplitude_theta0",
          "amplitude_theta_pi"
        ],
        "units": {
          "r_um": "µm",
          "amplitude_theta0": "normalized field amplitude",
          "amplitude_theta_pi": "normalized field amplitude"
        }
      },
      "description": "Normalized radial field profile of the LP03′ mode along θ=0 and θ=π, demonstrating the azimuthally asymmetric intensity distribution."
    }
  ],
  "notes": "The task reproduces the effective indices (dual-core and coreless) and the field profile for the given geometry, demonstrating the difference between the two models as highlighted in the paper."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that does not see your code. The scoring is structured as follows:
- For `effective_indices.csv`, the verifier reads the three mode effective indices, their coreless counterparts, and the differences, and checks whether they lie close to the physically expected values for this geometry (closeness is measured with an appropriate tolerance; exact agreement with any particular prior is not required).
- For `field_profile_LP03prime.csv`, the verifier performs a structural audit: it verifies that the radial profile at θ=0 is not symmetric with that at θ=π, that the maximum field intensity occurs at a non-zero radial coordinate (offset from the fiber axis), and that in the region of the second core (~30–35 µm) there is a local maximum shifted toward the primary core.
Each output stage carries a share of the total reward; you must produce both artifacts to receive full credit. Simply reporting the expected numbers without performing the actual computation will not satisfy the structural audit and will result in a low score.