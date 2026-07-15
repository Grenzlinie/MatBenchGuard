# Hot-Electron Transport Simulation with Intersubband Coulomb Interaction

## Problem background
In GaAs-based quantum wells and quantum wires with two occupied subbands, hot-electron transport is influenced by intersubband Coulomb interactions. The Lei-Ting balance-equation approach for two types of carriers (TTCM) treats electrons in each subband as having their own drift velocity, electron temperature, and chemical potential. The key open question is whether intersubband Coulomb scattering is strong enough to thermalize electrons between subbands under an applied electric field, causing the subband electron temperatures and drift velocities to become nearly equal. If so, a simplified one-type-of-carriers model (OTCM) would be sufficient; otherwise, the full two-type model is required. This task investigates this question for quasi-2D and quasi-1D GaAs systems at two different carrier densities.

## Approach
The core method is the Lei-Ting force, energy, and particle-number balance equations for two types of carriers. The equations are solved for a GaAs quantum well of width 50 nm and for a cylindrical quantum wire of radius 9 nm, both at a lattice temperature of 80 K. The scattering mechanisms included are: electron-impurity scattering; intra- and inter-subband electron-phonon scattering (polar-optical, deformation potential, and piezoelectric couplings); and the intersubband Coulomb interaction, using only first- and second-class matrix elements (the intrasubband terms V_{00,00} and V_{11,11} and the intersubband term V_{00,11}) because the third-class terms are negligible for these geometries. The total electron density is fixed for each case (the specific low and high values are given in the workflow steps). The coupled nonlinear equations are solved for steady-state conditions at a grid of uniform electric fields applied along the transport direction, ranging from 0.1 to 2.0 kV/cm. The main output quantities are the drift velocities, electron temperatures, chemical potentials, and populations of the ground subband (0) and the first excited subband (1, including its degenerate partner for the wire).

## Model equations

### Balance equations for quasi-2D systems

In a uniform electric field \(E\) applied along the plane, the steady-state force, energy, and particle-number balance equations for subbands 0 and 1 are:

\[
N_0 e E + F_0(v_0) + F_p^{01}(v_0, v_1) + F_{01}(v_0 - v_1) = 0 \qquad (1)
\]
\[
N_1 e E + F_1(v_1) + F_p^{10}(v_0, v_1) - F_{01}(v_0 - v_1) = 0 \qquad (2)
\]
\[
v_0 \cdot F_0(v_0) + W_0(v_0) + W_p^{01}(v_0, v_1) + W_{01}(v_0 - v_1) = 0 \qquad (3)
\]
\[
v_1 \cdot F_1(v_1) + (v_0 - v_1) \cdot F_{01}(v_0 - v_1) + W_1(v_1) + W_p^{10}(v_0, v_1) - W_{01}(v_0 - v_1) = 0 \qquad (4)
\]
\[
X(v_0, T_{0e}, \mu_0, v_1, T_{1e}, \mu_1) = 0 \qquad (5)
\]
with total sheet density \(N_s = N_0 + N_1\). The subband populations are related to the chemical potentials via \(N_i = \sum_{k\sigma} f((\varepsilon_{ik} - \mu_i)/T_{ie})\), where \(f\) is the Fermi‑Dirac distribution.

### Intersubband Coulomb contributions (2D)

The force \(F_{01}\) and energy‑loss rate \(W_{01}\) due to intersubband Coulomb interaction (matrix element \(V_{00,11}\)) are:

\[
F_{01}^{2D} = \sum_q |V_{00,11}(q)|^2 q \int_{-\infty}^{\infty} \frac{d\omega}{\pi}
 \left[ n\!\left(\frac{\omega}{T_{0e}}\right) - n\!\left(\frac{\omega-\omega_{01}}{T_{1e}}\right) \right]
 \Pi_2^{(0)}(q,\omega) \, \Pi_2^{(1)}(q,\omega-\omega_{01})
\]
\[
W_{01}^{2D} = \sum_q |V_{00,11}(q)|^2 \int_{-\infty}^{\infty} \frac{d\omega}{\pi}\, \omega
 \left[ n\!\left(\frac{\omega}{T_{0e}}\right) - n\!\left(\frac{\omega-\omega_{01}}{T_{1e}}\right) \right]
 \Pi_2^{(0)}(q,\omega) \, \Pi_2^{(1)}(q,\omega-\omega_{01})
\]
with \(\omega_{01} = q \cdot (v_0 - v_1)\), \(n(x) = 1/(e^x - 1)\) the Bose function, and \(\Pi_2^{(i)}\) the imaginary part of the electron density‑density correlation function for subband \(i\) in 2D (Lindhard‑type). The Coulomb matrix element reads
\[
V_{00,11}(q) = \frac{e^2}{2\epsilon_0 \kappa q} H_{00,11}(q),
\]
\[
H_{00,11}(q) = \int_0^d \!\! \int_0^d dz_1 dz_2 \,
\zeta_0(z_1) \zeta_0(z_1) \zeta_1(z_2) \zeta_1(z_2)\, e^{-q|z_1-z_2|},
\]
where \(\zeta_n(z) = \sqrt{2/d}\, \sin((n+1)\pi z/d)\) for the infinite well of width \(d\).

### Balance equations for quasi-1D systems

For a cylindrical quantum wire with ground subband 0 and a pair of degenerate subbands (1 and −1), the equations become:

\[
N_0 e E + F_0(v_0) + 2 F_p^{01}(v_0, v_1) + 2 F_{01}(v_0 - v_1) = 0 \qquad (6)
\]
\[
2 N_1 e E + 2 F_1(v_1) + 2 F_p^{10}(v_0, v_1) - 2 F_{01}(v_0 - v_1) = 0 \qquad (7)
\]
\[
v_0 \cdot F_0(v_0) + W_0(v_0) + 2 W_p^{01}(v_0, v_1) + 2 W_{01}(v_0 - v_1) = 0 \qquad (8)
\]
\[
v_1 \cdot 2 F_1(v_1) + (v_0 - v_1) \cdot 2 F_{01}(v_0 - v_1) + 2 W_1(v_1) + 2 W_p^{10}(v_0, v_1) - 2 W_{01}(v_0 - v_1) = 0 \qquad (9)
\]
\[
X(v_0, T_{0e}, \mu_0, v_1, T_{1e}, \mu_1) = 0 \qquad (10)
\]
with total line density \(N_l = N_0 + 2 N_1\).

### Intersubband Coulomb contributions (1D)

\[
F_{01}^{1D} = \sum_{q_z} |K_{00,11}(|q_z|)|^2 q_z \int_{-\infty}^{\infty} \frac{d\omega}{\pi}
 \left[ n\!\left(\frac{\omega}{T_{0e}}\right) - n\!\left(\frac{\omega-\omega_{01}}{T_{1e}}\right) \right]
 \Pi_2^{(0)}(q_z,\omega) \, \Pi_2^{(1)}(q_z,\omega-\omega_{01})
\]
\[
W_{01}^{1D} = \sum_{q_z} |K_{00,11}(|q_z|)|^2 \int_{-\infty}^{\infty} \frac{d\omega}{\pi}\, \omega
 \left[ n\!\left(\frac{\omega}{T_{0e}}\right) - n\!\left(\frac{\omega-\omega_{01}}{T_{1e}}\right) \right]
 \Pi_2^{(0)}(q_z,\omega) \, \Pi_2^{(1)}(q_z,\omega-\omega_{01})
\]
with \(\omega_{01} = q_z (v_0 - v_1)\). The Coulomb matrix element \(K_{00,11}\) is
\[
K_{00,11}(|q_z|) = \frac{e^2}{4\pi\epsilon_0 \kappa}
 \int d\mathbf{r}_\parallel \int d\mathbf{r}_\parallel' \,
 \zeta_0^*(\mathbf{r}_\parallel) \zeta_0(\mathbf{r}_\parallel)
 \zeta_1^*(\mathbf{r}_\parallel') \zeta_1(\mathbf{r}_\parallel')
 K_0(|q_z| |\mathbf{r}_\parallel - \mathbf{r}_\parallel'|),
\]
\(K_0\) is the modified Bessel function. The wavefunctions are \(\zeta_{01}(r_\parallel) = C_1^0 J_0(x_1^0 r_\parallel/\rho)\) and \(\zeta_{\pm 11}(r_\parallel) = \pm C_1^{\pm 1} J_1(x_1^1 r_\parallel/\rho) e^{\pm i\phi}\), with \(x_1^0 \approx 2.4048\), \(x_1^1 \approx 3.8317\), normalization factors \(C_m^n = 1/(\sqrt{\pi} y_m^n \rho)\) and \(y_m^n = J_{|n|+1}(x_m^{|n|})\). The subband energies are \(\varepsilon_{nm} = (x_m^{|n|})^2/(2 m^* \rho^2)\). The implementation may use Python with SciPy for the iterative solution; the scattering-rate integrals and Coulomb matrix elements must be computed numerically from the given GaAs material parameters.

## Reproduction target
Implement the TTCM balance equations as described for the four specified systems: a quasi-2D quantum well at low and high sheet densities, and a quasi-1D quantum wire at low and high line densities. For each system, compute the steady-state subband drift velocities (v0, v1), electron temperatures (T0e, T1e), chemical potentials (μ0, μ1), and subband populations (N0, N1 for 2D cases, and line densities N0, N1 for 1D cases) at every electric field value in the grid. Save the results in four CSV files with the exact columns listed in the workflow steps. The files are the primary deliverables; no further aggregation is required. The hidden verifier will analyze these files directly to assess the degree of inter-subband thermalization.

## Assets

- GaAs material parameters
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Simulate quasi-2D quantum well at low density
- Role: scored
- Action: For a GaAs quantum well of width 50 nm at lattice temperature 80 K, solve the Lei-Ting balance equations for two types of carriers (TTCM) at a sheet carrier density of Ns = 0.1 × 10^11 cm⁻² over a grid of uniform electric fields from 0.1 to 2.0 kV/cm. Include intrasubband and intersubband scattering (electron-impurity, intra- and inter-subband electron-phonon: polar-optical, deformation potential, piezoelectric) and intersubband Coulomb interaction using only first- and second-class matrix elements. Output the steady-state subband drift velocities, electron temperatures, chemical potentials, and subband populations.
- Output file: `/app/outputs/2D_low_density.csv`
- Format: csv
- Contract: Columns: electric_field_kVcm, v0_cms, v1_cms, T0e_K, T1e_K, mu0_meV, mu1_meV, N0_1cm2, N1_1cm2.
- Scoring: scored by hidden verifier

### Step 2: Simulate quasi-2D quantum well at high density
- Role: scored (load-bearing)
- Action: For a GaAs quantum well of width 50 nm at lattice temperature 80 K, solve the TTCM balance equations at a sheet carrier density of Ns = 5.0 × 10^11 cm⁻² over the same electric field grid, using the same scattering mechanisms and Coulomb interactions as in the low-density step. Output the steady-state subband drift velocities, electron temperatures, chemical potentials, and subband populations.
- Output file: `/app/outputs/2D_high_density.csv`
- Format: csv
- Contract: Columns: electric_field_kVcm, v0_cms, v1_cms, T0e_K, T1e_K, mu0_meV, mu1_meV, N0_1cm2, N1_1cm2.
- Scoring: scored by hidden verifier

### Step 3: Simulate quasi-1D quantum wire at low density
- Role: scored
- Action: For a GaAs cylindrical quantum wire of radius 9 nm at lattice temperature 80 K, solve the TTCM balance equations (including the degenerate subbands) at a line carrier density of Nl = 2.0 × 10^6 cm⁻¹ over a grid of electric fields from 0.1 to 2.0 kV/cm. Use the same scattering mechanisms and intersubband Coulomb interaction. Output the steady-state subband drift velocities, electron temperatures, chemical potentials, and line densities.
- Output file: `/app/outputs/1D_low_density.csv`
- Format: csv
- Contract: Columns: electric_field_kVcm, v0_cms, v1_cms, T0e_K, T1e_K, mu0_meV, mu1_meV, N0_1cm, N1_1cm.
- Scoring: scored by hidden verifier

### Step 4: Simulate quasi-1D quantum wire at high density
- Role: scored (load-bearing)
- Action: For a GaAs cylindrical quantum wire of radius 9 nm at lattice temperature 80 K, solve the TTCM balance equations at a line carrier density of Nl = 5.0 × 10^6 cm⁻¹ over the same electric field grid. Output the steady-state subband drift velocities, electron temperatures, chemical potentials, and line densities.
- Output file: `/app/outputs/1D_high_density.csv`
- Format: csv
- Contract: Columns: electric_field_kVcm, v0_cms, v1_cms, T0e_K, T1e_K, mu0_meV, mu1_meV, N0_1cm, N1_1cm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/2D_low_density.csv`
- `/app/outputs/2D_high_density.csv`
- `/app/outputs/1D_low_density.csv`
- `/app/outputs/1D_high_density.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### 2D_low_density.csv
- path: `/app/outputs/2D_low_density.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Low-density quasi-2D transport data used to verify that subband temperatures and drift velocities remain disparate (no thermalization).
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v0_cms`, `v1_cms`, `T0e_K`, `T1e_K`, `mu0_meV`, `mu1_meV`, `N0_1cm2`, `N1_1cm2`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v0_cms`: cm/s
    - `v1_cms`: cm/s
    - `T0e_K`: K
    - `T1e_K`: K
    - `mu0_meV`: meV
    - `mu1_meV`: meV
    - `N0_1cm2`: cm^{-2}
    - `N1_1cm2`: cm^{-2}

### 2D_high_density.csv
- path: `/app/outputs/2D_high_density.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: High-density quasi-2D transport data used to verify that intersubband thermalization occurs (T0e≈T1e, v0≈v1), validating the one-type-of-carriers model.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v0_cms`, `v1_cms`, `T0e_K`, `T1e_K`, `mu0_meV`, `mu1_meV`, `N0_1cm2`, `N1_1cm2`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v0_cms`: cm/s
    - `v1_cms`: cm/s
    - `T0e_K`: K
    - `T1e_K`: K
    - `mu0_meV`: meV
    - `mu1_meV`: meV
    - `N0_1cm2`: cm^{-2}
    - `N1_1cm2`: cm^{-2}

### 1D_low_density.csv
- path: `/app/outputs/1D_low_density.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Low-density quasi-1D transport data used to verify the absence of strong intersubband thermalization.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v0_cms`, `v1_cms`, `T0e_K`, `T1e_K`, `mu0_meV`, `mu1_meV`, `N0_1cm`, `N1_1cm`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v0_cms`: cm/s
    - `v1_cms`: cm/s
    - `T0e_K`: K
    - `T1e_K`: K
    - `mu0_meV`: meV
    - `mu1_meV`: meV
    - `N0_1cm`: cm^{-1}
    - `N1_1cm`: cm^{-1}

### 1D_high_density.csv
- path: `/app/outputs/1D_high_density.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: High-density quasi-1D transport data used to verify that intersubband thermalization occurs in quantum wires, validating the OTCM.
- schema:
  - `type`: table
  - `required_columns`: `electric_field_kVcm`, `v0_cms`, `v1_cms`, `T0e_K`, `T1e_K`, `mu0_meV`, `mu1_meV`, `N0_1cm`, `N1_1cm`
  - `units`:
    - `electric_field_kVcm`: kV/cm
    - `v0_cms`: cm/s
    - `v1_cms`: cm/s
    - `T0e_K`: K
    - `T1e_K`: K
    - `mu0_meV`: meV
    - `mu1_meV`: meV
    - `N0_1cm`: cm^{-1}
    - `N1_1cm`: cm^{-1}

Notes: Scoring compares average relative subband temperature and velocity differences against publicly undisclosed thresholds to determine whether each system exhibits the expected thermalization (high density) or non-thermalization (low density). The contract does not disclose the threshold values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "2D_low_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v0_cms",
          "v1_cms",
          "T0e_K",
          "T1e_K",
          "mu0_meV",
          "mu1_meV",
          "N0_1cm2",
          "N1_1cm2"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v0_cms": "cm/s",
          "v1_cms": "cm/s",
          "T0e_K": "K",
          "T1e_K": "K",
          "mu0_meV": "meV",
          "mu1_meV": "meV",
          "N0_1cm2": "cm^{-2}",
          "N1_1cm2": "cm^{-2}"
        }
      },
      "description": "Low-density quasi-2D transport data used to verify that subband temperatures and drift velocities remain disparate (no thermalization)."
    },
    {
      "file": "2D_high_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v0_cms",
          "v1_cms",
          "T0e_K",
          "T1e_K",
          "mu0_meV",
          "mu1_meV",
          "N0_1cm2",
          "N1_1cm2"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v0_cms": "cm/s",
          "v1_cms": "cm/s",
          "T0e_K": "K",
          "T1e_K": "K",
          "mu0_meV": "meV",
          "mu1_meV": "meV",
          "N0_1cm2": "cm^{-2}",
          "N1_1cm2": "cm^{-2}"
        }
      },
      "description": "High-density quasi-2D transport data used to verify that intersubband thermalization occurs (T0e≈T1e, v0≈v1), validating the one-type-of-carriers model."
    },
    {
      "file": "1D_low_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v0_cms",
          "v1_cms",
          "T0e_K",
          "T1e_K",
          "mu0_meV",
          "mu1_meV",
          "N0_1cm",
          "N1_1cm"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v0_cms": "cm/s",
          "v1_cms": "cm/s",
          "T0e_K": "K",
          "T1e_K": "K",
          "mu0_meV": "meV",
          "mu1_meV": "meV",
          "N0_1cm": "cm^{-1}",
          "N1_1cm": "cm^{-1}"
        }
      },
      "description": "Low-density quasi-1D transport data used to verify the absence of strong intersubband thermalization."
    },
    {
      "file": "1D_high_density.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "electric_field_kVcm",
          "v0_cms",
          "v1_cms",
          "T0e_K",
          "T1e_K",
          "mu0_meV",
          "mu1_meV",
          "N0_1cm",
          "N1_1cm"
        ],
        "units": {
          "electric_field_kVcm": "kV/cm",
          "v0_cms": "cm/s",
          "v1_cms": "cm/s",
          "T0e_K": "K",
          "T1e_K": "K",
          "mu0_meV": "meV",
          "mu1_meV": "meV",
          "N0_1cm": "cm^{-1}",
          "N1_1cm": "cm^{-1}"
        }
      },
      "description": "High-density quasi-1D transport data used to verify that intersubband thermalization occurs in quantum wires, validating the OTCM."
    }
  ],
  "notes": "Scoring compares average relative subband temperature and velocity differences against publicly undisclosed thresholds to determine whether each system exhibits the expected thermalization (high density) or non-thermalization (low density). The contract does not disclose the threshold values."
}
```

## How you are scored
A hidden verifier reads each of your four CSV files independently. For each file, it computes the average relative differences between the subband electron temperatures and between the subband drift velocities over the electric-field range. The verifier compares these averages against undisclosed thresholds to determine whether the results exhibit the physically expected carrier‑density‑dependent thermalization behavior. Each of the four cases (high‑density 2D, high‑density 1D, low‑density 2D, low‑density 1D) that satisfies the expected trend earns a fraction of the total reward, with the highest weight given to the high‑density cases. The final score is the sum of the partial rewards. Submitting the correct CSV files from an accurate solution of the TTCM equations is sufficient; the verifier does not require the paper’s own numerical values.
