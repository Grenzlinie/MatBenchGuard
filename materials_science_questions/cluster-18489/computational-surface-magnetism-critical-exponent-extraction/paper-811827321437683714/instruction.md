# Numerical Insensitivity of Surface Specific Heat to Surface Exchange Modifications in a Ferromagnetic Film

## Problem background
In a ferromagnetic film, the low-temperature specific heat receives a surface contribution that modifies the bulk behavior. A theoretical analysis argued that this surface specific heat is insensitive to changes in the exchange interactions within the surface layers and can be expressed solely in terms of the bulk spin-wave stiffness constants. This reproduction numerically tests that prediction by implementing the spin-wave model for a simple cubic ferromagnet with a (100) surface and nearest‑neighbour exchange.

## Approach
We model a thin ferromagnetic film of N atomic layers with a simple cubic lattice and (100) free surfaces. The spin-wave spectrum is obtained by constructing and diagonalising the dynamical matrix for each wavevector k_parallel parallel to the surface, using the Heisenberg Hamiltonian with nearest‑neighbour exchange J and a possible surface exchange modification ΔJ. The mode spectrum comprises a surface branch and a continuum of bulk modes; the boundary conditions shift the bulk mode distribution, characterised by a phase angle φ_B derived from scattering theory. Sum rules fix the phase jumps at the band edges. The total surface‑correction specific heat is built from three contributions: (i) the surface‑mode internal energy integrated over the two‑dimensional Brillouin zone in the long‑wavelength limit, (ii) a δ‑function contribution from the bottom of the bulk band, and (iii) a smooth contribution from the redistribution of bulk modes inside the continuum. The sum of these three yields the final C_s^(TOT). The computed result is compared against the analytic formula that depends only on the bulk stiffness constants D_x and D_y. To test insensitivity, the whole calculation is repeated after varying the surface exchange by ±0.5J while keeping all other parameters fixed.

## Reproduction target
Numerically compute the total low‑temperature surface specific heat C_s^TOT for a ferromagnetic film with the following parameters: simple cubic lattice, (100) surfaces, N=100 atomic layers, nearest‑neighbour exchange J=1 (units: k_B=ħ=a=1), total surface area S=1 (both surfaces), and temperature T=0.1 J/k_B. Report your computed C_s, the analytic value (using D_x_D_y = 2J a^2) and the relative error. In a separate run, change the surface exchange constant by ±0.5J (i.e., ΔJ = +0.5J and ΔJ = –0.5J), recompute C_s^TOT, and record the two resulting values. The hidden verifier will compare your computed specific heat against the analytic expression and will check that the specific heat remains essentially unchanged under the surface exchange modifications; detailed tolerances are used for the pass/fail decision.

## Model equations
We consider a simple cubic lattice with lattice constant \(a=1\). The Heisenberg exchange is nearest-neighbour only, with bulk exchange constant \(J\) and a possible modification \(\Delta J\) for intra-plane exchange within the two surface layers (\(l_z=1\) and \(l_z=N\)). The spin magnitude is taken as \(S_{\text{spin}}=1\) (units \(\hbar=1\)). The dynamical matrix \(D(\mathbf{k}_{||})\) for a wavevector \(\mathbf{k}_{||}=(k_x,k_y)\) is defined by the equations of motion [Eqs. (2.2) of Mills (1969)] and has the following explicit form.

Define:
\[
b_0(\mathbf{k}_{||}) = 2J(\cos k_x + \cos k_y),\qquad
b_1 = J \quad(\text{constant}),
\]
\[
\Delta b_0(\mathbf{k}_{||}) = 2\Delta J(\cos k_x + \cos k_y).
\]

Then for interior layers \(l_z=2,\dots,N-1\):
\[
D_{l_z,l_z} = b_0(0)+2b_1 - b_0(\mathbf{k}_{||}) = 6J - b_0(\mathbf{k}_{||}),\qquad
D_{l_z,l_z\pm 1} = -b_1 = -J,
\]
and for the surface layer \(l_z=1\):
\[
D_{1,1} = b_0(0)+b_1 - b_0(\mathbf{k}_{||}) - [\Delta b_0(0)-\Delta b_0(\mathbf{k}_{||})]
      = 5J - b_0(\mathbf{k}_{||}) - (4\Delta J - \Delta b_0(\mathbf{k}_{||})),\qquad
D_{1,2} = -J,
\]
and similarly for \(l_z=N\) with \(D_{N,N}=D_{1,1}\), \(D_{N,N-1}=-J\).

The parameter \(\gamma(\mathbf{k}_{||})\) that characterises the surface mode existence is
\[
\gamma(\mathbf{k}_{||}) = \frac{b_1}{b_1 + \Delta b_0(0)-\Delta b_0(\mathbf{k}_{||})}
                      = \frac{J}{J + 4\Delta J - \Delta b_0(\mathbf{k}_{||})}.
\]

For a given \(\mathbf{k}_{||}\) the bulk spin-wave dispersion is
\[
\Omega_B(\mathbf{k}_{||},k_z) = A(\mathbf{k}_{||}) - 2J\cos(k_z),\qquad
A(\mathbf{k}_{||}) = 6J - b_0(\mathbf{k}_{||}).
\]
The bottom of the bulk band is \(\Omega_m(\mathbf{k}_{||}) = A - 2J = 4J - b_0(\mathbf{k}_{||})\); the top is \(\Omega_M = A + 2J\).

The phase angle for bulk modes, defined in Eq. (2.16), becomes
\[
\varphi_B(\mathbf{k}_{||},\Omega) = 
\tan^{-1}\!\left(\frac{\sqrt{1 - \big(\frac{A-\Omega}{2J}\big)^2}\;(1-\gamma^2)}
                {2\gamma - (1+\gamma^2)\big(\frac{A-\Omega}{2J}\big)}\right),
\]
valid for \(\Omega_m\leq\Omega\leq\Omega_M\). (The branch of \(\tan^{-1}\) is chosen so that \(\varphi_B=0\) at \(k_z=0\), i.e. \(\Omega=\Omega_m\).)

The full phase \(\varphi(\Omega)\) used for the density-of-states correction is piecewise constant/linear as described in the paper, with sum‑rule constants \(\varphi_1=3\pi/2\), \(\varphi_2=0\), and jumps of \(-\pi/2\) at \(\Omega_m\) and \(\Omega_M\).

The surface magnon contribution to the internal energy is computed by replacing the surface‑mode frequency by \(\Omega_m(\mathbf{k}_{||})\) (long‑wavelength limit) and integrating over the 2D Brillouin zone:
\[
U_S(T) = 2\frac{S}{(2\pi)^2} \int_{BZ} d^2k_{||}\,
        \hbar\,\Omega_m(\mathbf{k}_{||})\,n[\Omega_m(\mathbf{k}_{||})],
\]
with \(n(\Omega)= (e^{\hbar\Omega/k_B T}-1)^{-1}\). The resulting surface specific heat is
\[
C_S(T) = \frac{dU_S}{dT}.
\]
After adding the two bulk‑redistribution contributions (the \(\delta\)‑function piece and the continuum piece), the total surface correction simplifies to
\[
C_s^{\mathrm{TOT}}(T) = \frac{1}{4}C_S(T).
\]

The analytic low‑temperature formula, expressed through the bulk spin‑wave stiffness constants \(D_x = D_y = 2 J a^2\), is
\[
C_s^{\mathrm{analytic}} = \frac{S}{8\pi}\,\zeta(2)\,\frac{k_B T}{\hbar\sqrt{D_x D_y}}.
\]
Here \(\zeta(2)=\pi^2/6\) and \(S\) is the total surface area (both surfaces).

## Assets
- Python 3 with standard scientific libraries: numpy, scipy (for numerical integration, linear algebra, and special functions).

## Workflow steps

### Step 1: Model and film geometry setup
- Role: process
- Action: Define a simple cubic lattice with (100) surfaces, N=100 atomic layers, nearest-neighbor exchange J=1, and a surface exchange modification ΔJ (default 0). Compute the bulk spin-wave stiffness constants D_x = D_y = 2J a^2. Set physical constants k_B=1, ħ=1, lattice constant a=1, and total surface area S=1 (both surfaces). The target temperature for the specific heat is T = 0.1 J/k_B.
- Evidence: none

### Step 2: Compute spin-wave spectrum for each k_parallel
- Role: process
- Action: For a fine grid of wavevectors k_parallel in the two-dimensional Brillouin zone, construct the N×N dynamical matrix D(k_parallel) from the spin-wave equations of motion. Diagonalize to obtain all eigenfrequencies. Identify the surface mode(s) and the bulk band edges Ω_m and Ω_M. Compute the parameter γ(k_parallel) and the phase angle φ_B(k_parallel, Ω) using the paper's formulas.
- Evidence: none

### Step 3: Compute surface magnon contribution to specific heat
- Role: process
- Action: Numerically integrate the surface magnon internal energy over the two-dimensional Brillouin zone using the Bose-Einstein distribution at T=0.1. Replace the surface mode frequency by Ω_B(k_parallel,0) in the long-wavelength limit. Obtain the surface specific heat C_S = dU_S/dT.
- Evidence: none

### Step 4: Compute bulk-mode redistribution contribution
- Role: process
- Action: Using the density-of-states correction Δρ_B and the piecewise-defined phase angle φ(Ω) with sum-rule constants φ1=3π/2, φ2=0, evaluate the two bulk-mode contributions: ΔU_B^(1) from the δ-function at Ω_m and ΔU_B^(2) from the continuous part by numerical integration over k_parallel and Ω. Combine with the surface magnon result to obtain the total surface correction to the specific heat, C_s^(TOT) = (1/4) C_S.
- Evidence: none

### Step 5: Generate final surface specific heat results and verify insensitivity
- Role: scored (load-bearing)
- Action: Compute the analytic surface specific heat using the formula \(C_s^{\mathrm{analytic}} = \frac{S}{8\pi}\,\zeta(2)\,\frac{k_B T}{\hbar\sqrt{D_x D_y}}\) with \(\zeta(2)=\pi^2/6\) and the given parameters (T=0.1, S=1, J=1, D_x=D_y=2). Assemble the final JSON with temperature T, surface area S, exchange J, stiffness constants D_x, D_y, the computed C_s_computed (from step 04), the analytic C_s_analytic, and the relative error. Then re-run the calculation pipeline (steps 02–04) with surface exchange modifications ΔJ = +0.5J and ΔJ = -0.5J while keeping other parameters fixed, and record the respective C_s_computed values in the insensitivity_checks field. Verify that the relative change from the ΔJ=0 case is ≤1%.
- Output file: `/app/outputs/surface_specific_heat_results.json`
- Format: json
- Contract: JSON object with keys: T (float), S (float), J (float), D_x (float), D_y (float), C_s_computed (float), C_s_analytic (float), relative_error (float), insensitivity_checks (object with keys '+0.5J' and '-0.5J', each value a float for C_s_computed).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_specific_heat_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_specific_heat_results.json
- path: `/app/outputs/surface_specific_heat_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The computed surface specific heat, the analytic value, the relative error, and the insensitivity check values for varied surface exchange. The verifier recomputes the analytic target and checks that the relative error ≤ 0.05 and insensitivity changes ≤ 0.01.
- schema:
  - `type`: object
  - `required`:
    - `T`: float
    - `S`: float
    - `J`: float
    - `D_x`: float
    - `D_y`: float
    - `C_s_computed`: float
    - `C_s_analytic`: float
    - `relative_error`: float
    - `insensitivity_checks`:
      - `+0.5J`:
        - `C_s_computed`: float
      - `-0.5J`:
        - `C_s_computed`: float

Notes: All physical constants are in units where k_B=ħ=a=1 and J=1. The analytic formula is derived in the paper and depends only on D_x, D_y. The insensitivity check requires re-running the full diagonalization and integration for ΔJ=±0.5J.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_specific_heat_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "T": "float",
          "S": "float",
          "J": "float",
          "D_x": "float",
          "D_y": "float",
          "C_s_computed": "float",
          "C_s_analytic": "float",
          "relative_error": "float",
          "insensitivity_checks": {
            "+0.5J": {
              "C_s_computed": "float"
            },
            "-0.5J": {
              "C_s_computed": "float"
            }
          }
        }
      },
      "description": "The computed surface specific heat, the analytic value, the relative error, and the insensitivity check values for varied surface exchange. The verifier recomputes the analytic target and checks that the relative error ≤ 0.05 and insensitivity changes ≤ 0.01."
    }
  ],
  "notes": "All physical constants are in units where k_B=ħ=a=1 and J=1. The analytic formula is derived in the paper and depends only on D_x, D_y. The insensitivity check requires re-running the full diagonalization and integration for ΔJ=±0.5J."
}
```

## How you are scored
Your submitted `surface_specific_heat_results.json` will be read by a hidden verifier. The verifier recomputes the analytic specific heat from the parameters you report (T, S, J, D_x, D_y) and compares it to your C_s_computed using a relative tolerance; a small error is required for credit. It also checks that the relative change of C_s under ΔJ = ±0.5J from the unperturbed (ΔJ=0) case stays below a threshold. The final reward is the average of the two pass/fail scores (equal weight) for the two checks. You must report all quantities truthfully; the verifier may also inspect internal consistency and file format.
