# Cylindrical topological insulator eigenenergies and optical absorption overlap integrals

## Problem background
Topological insulators are materials that are insulating in the bulk but host conducting surface states. In a cylindrical nanowire geometry, these surface states are modified by quantum confinement, and their energies and wavefunctions depend on the wire radius and total angular momentum. This task investigates a cylindrical topological insulator made of Bi₂Se₃, described by a continuum-model Hamiltonian with hard-wall boundary conditions. The target is to compute the lowest positive-energy eigenstates and evaluate the radial overlap integrals that govern optical absorption dipole matrix elements, which are strongly affected by finite-size effects.

## Model description

We consider an infinitely long cylinder of radius \(R\) whose axis is along \(z\). The bulk topological insulator is described by the four-band **k·p** Hamiltonian (equation (1))

\[
H_0 = \begin{pmatrix}
m(\mathbf{p}) & B p_z & 0 & A p_- \\
B p_z & -m(\mathbf{p}) & A p_- & 0 \\
0 & A p_+ & m(\mathbf{p}) & -B p_z \\
A p_+ & 0 & -B p_z & -m(\mathbf{p})
\end{pmatrix},
\]

with \(m(\mathbf{p}) = m_0 + m_1 p_z^2 + m_2(p_x^2+p_y^2)\) and \(p_\pm = p_x \pm i p_y\).  
The material parameters for Bi₂Se₃ are taken from Table 1:

\[
m_0 = -0.169\ \mathrm{eV},\quad
m_1 = 3.353\ \mathrm{eV\,Å^2},\quad
m_2 = 29.375\ \mathrm{eV\,Å^2},\quad
A = 2.513\ \mathrm{eV\,Å},\quad
B = 1.836\ \mathrm{eV\,Å}.
\]

We work at zero axial momentum, \(k_z = 0\), where the Hamiltonian decouples into two independent \(2\times2\) blocks that correspond to different parity sectors.  The general eigenfunction at \(k_z=0\) can be written as (equation (7))

\[
\Psi(\rho,\varphi,z) = \frac{1}{\sqrt{2\pi}}
\begin{pmatrix}
c_1\,J_{j-\frac12}(\kappa\rho)\,e^{i(j-\frac12)\varphi} \\
c_2\,J_{j-\frac12}(\kappa\rho)\,e^{i(j-\frac12)\varphi} \\
c_3\,J_{j+\frac12}(\kappa\rho)\,e^{i(j+\frac12)\varphi} \\
c_4\,J_{j+\frac12}(\kappa\rho)\,e^{i(j+\frac12)\varphi}
\end{pmatrix},
\]

where \(j\) is a half‑integer (the eigenvalue of the \(z\)-component of the total angular momentum, in units of \(\hbar=1\)) and \(J_n(z)\) is the Bessel function of the first kind.  
The radial wave‑number \(\kappa\) can take two values

\[
\kappa_\pm = \sqrt{-\frac{m_0}{m_2} - \frac{A^2}{2m_2^2}
          \pm \sqrt{\frac{A^4}{4m_2^4} + \frac{E^2}{m_2^2} + \frac{A^2 m_0}{m_2^3}}},
\]

and we define the energy‑dependent denominators

\[
\Delta_\pm = m_2\kappa_\pm^2 + m_0 - E.
\]

The hard‑wall boundary condition \(\Psi(R,\varphi,z)=0\) leads to the secular equation that determines the allowed energies \(E\).  At \(k_z=0\) the problem splits.  The states that belong to the **even‑parity sector** (sometimes called the “\(s=+\)” branch for the positive‑energy surface state) have only the first and fourth spinor components non‑zero.  Their energies are solutions of (equation (12a))

\[
\boxed{\frac{\kappa_+\Delta_-}{\kappa_-\Delta_+}
      = \frac{T_j(\kappa_+R)}{T_j(\kappa_-R)}},
\qquad
T_j(z) \equiv \frac{J_{j+1/2}(z)}{J_{j-1/2}(z)}.
\]

The states that belong to the **odd‑parity sector** (sometimes called the “\(s=-\)” branch) have only the second and third components non‑zero and satisfy equation (12b), but for the specific states required in this task we will use the even‑parity sector as detailed below.

### Surface states needed for this task
For the **lowest positive‑energy surface states** with \(j=0.5\) and \(j=1.5\) we solve equation (12a) for the smallest positive root \(E>0\).  
For the **lowest negative‑energy surface state** with \(j=-0.5\) (the “\(s=-\)” state used in the overlap integrals) we also solve equation (12a) and take the negative root whose absolute value is smallest (the root closest to zero from below).

### Radial wave functions (even‑parity sector)
For a given \(j\) and an energy \(E\) that satisfies (12a), the (un‑normalised) radial components \(\Phi_1(\rho)\) and \(\Phi_4(\rho)\) (the only non‑zero ones; \(\Phi_2=\Phi_3=0\)) are obtained from

\[
\alpha_+ J_{j+1/2}(\kappa_+R) + \alpha_- J_{j+1/2}(\kappa_-R) = 0,
\]

which enforces the hard‑wall condition on the fourth component.  One can set \(\alpha_+ = 1\) and

\[
\alpha_- = -\frac{J_{j+1/2}(\kappa_+R)}{J_{j+1/2}(\kappa_-R)},
\]

and then

\[
\begin{aligned}
\Phi_1(\rho) &= \frac{iA\kappa_+}{\Delta_+} J_{j-1/2}(\kappa_+\rho)
            + \alpha_- \frac{iA\kappa_-}{\Delta_-} J_{j-1/2}(\kappa_-\rho),\\[4pt]
\Phi_4(\rho) &= J_{j+1/2}(\kappa_+\rho)
            + \alpha_- J_{j+1/2}(\kappa_-\rho).
\end{aligned}
\]

The wave function is normalised by the radial integral

\[
\mathcal{N} = \int_0^R \rho\,d\rho\,
\bigl(|\Phi_1(\rho)|^2 + |\Phi_4(\rho)|^2\bigr),
\]

so that the physical (normalised) radials are \(\widetilde{\Phi}_{1,4}(\rho) = \Phi_{1,4}(\rho)/\sqrt{\mathcal{N}}\).

### Overlap integrals \(S_{14}\) and \(S_{23}\)
For the optical‑absorption threshold transition we need the transition between the \(s=-,\;j=-0.5\) state and the \(s=+,\;j=+0.5\) state.  The relevant dimensionless radial overlap integrals are defined as

\[
\boxed{S_{14} = \int_0^R r\,dr\;
\operatorname{Re}\!\Bigl[\,\widetilde{\Phi}_1^{(j=+0.5,\,E>0)}(r)^*\,
\widetilde{\Phi}_4^{(j=-0.5,\,E<0)}(r)\Bigr]},
\qquad
\boxed{S_{23} = 0},
\]

where \(\widetilde{\Phi}_{1,4}^{(j=+0.5,E>0)}\) are the normalised radials of the positive‑energy state with \(j=0.5\) obtained from equation (12a), and \(\widetilde{\Phi}_{4}^{(j=-0.5,E<0)}\) is the normalised fourth component of the negative‑energy state with \(j=-0.5\) obtained from the same secular equation (12a).  The integral \(S_{23}\) vanishes identically because the states considered here have \(\Phi_2=\Phi_3=0\).

## Assets

- scipy: scipy
- numpy: numpy

## Workflow steps

### Step 1: Compute eigenenergies
- Role: scored
- Action: For Bi₂Se₃, using the continuum-model Hamiltonian with hard-wall boundary conditions and the material parameters \(m_0=-0.169\ \mathrm{eV}\), \(m_1=3.353\ \mathrm{eV\,Å^2}\), \(m_2=29.375\ \mathrm{eV\,Å^2}\), \(A=2.513\ \mathrm{eV\,Å}\), \(B=1.836\ \mathrm{eV\,Å}\), solve the cylindrical TI secular equation at zero axial momentum (\(k_z=0\)) for the lowest positive-energy surface states.  Use the even‑parity secular equation (12a) as described in the Model description.  Do this for total angular momentum projections \(j = 0.5\) and \(1.5\), and for cylinder radii \(R = 2R_0, 4R_0, 6R_0, 8R_0, 10R_0\) where \(R_0 = 1.49\ \mathrm{nm}\).  Output the eigenenergies.
- Output file: `/app/outputs/step_01_eigenenergies.csv`
- Format: csv
- Contract: Columns: \(j\) (half-integer), \(R\) (nm), energy (eV).
- Scoring: scored by hidden verifier

### Step 2: Compute overlap integrals for optical absorption
- Role: scored (load-bearing)
- Action: Using the eigenfunctions obtained from the secular equation for the \(s=-,\ j=-0.5\) state (lowest negative‑energy surface state) and the \(s=+,\ j=+0.5\) state (lowest positive‑energy surface state), compute the radial overlap integrals \(S_{14}\) and \(S_{23}\) as defined in the Model description.  Evaluate for each radius \(R\) in the same set as step_01.  Output the overlap integrals.
- Output file: `/app/outputs/step_02_overlap_integrals.csv`
- Format: csv
- Contract: Columns: \(j\) (half-integer, set to \(0.5\) for this transition), \(R\) (nm), \(S_{14}\) (dimensionless), \(S_{23}\) (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_eigenenergies.csv`
- `/app/outputs/step_02_overlap_integrals.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_eigenenergies.csv
- path: `/app/outputs/step_01_eigenenergies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Lowest positive-energy surface state eigenenergies for Bi₂Se₃ cylindrical topological insulator at \(k_z=0\), for \(j=0.5,1.5\) and several radii.
- schema:
  - `type`: table
  - `required_columns`: `j`, `R`, `energy`
  - `units`:
    - `j`: dimensionless (half-integer)
    - `R`: nm
    - `energy`: eV

### step_02_overlap_integrals.csv
- path: `/app/outputs/step_02_overlap_integrals.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Radial overlap integrals \(S_{14}\) and \(S_{23}\) for the absorption threshold transition between \(s=-\), \(j=-0.5\) and \(s=+\), \(j=+0.5\) states.
- schema:
  - `type`: table
  - `required_columns`: `j`, `R`, `S_14`, `S_23`
  - `units`:
    - `j`: dimensionless (half-integer)
    - `R`: nm
    - `S_14`: dimensionless
    - `S_23`: dimensionless

Notes: The hidden checker recomputes eigenenergies and overlap integrals using its own implementation of the secular equation with the same material parameters and compares the submitted values within a suitable tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_eigenenergies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "j",
          "R",
          "energy"
        ],
        "units": {
          "j": "dimensionless (half-integer)",
          "R": "nm",
          "energy": "eV"
        }
      },
      "description": "Lowest positive-energy surface state eigenenergies for Bi2Se3 cylindrical topological insulator at kz=0, for j=0.5,1.5 and several radii."
    },
    {
      "file": "step_02_overlap_integrals.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "j",
          "R",
          "S_14",
          "S_23"
        ],
        "units": {
          "j": "dimensionless (half-integer)",
          "R": "nm",
          "S_14": "dimensionless",
          "S_23": "dimensionless"
        }
      },
      "description": "Radial overlap integrals S14 and S23 for the absorption threshold transition between s=-, j=-0.5 and s=+, j=+0.5 states."
    }
  ],
  "notes": "The hidden checker recomputes eigenenergies and overlap integrals using its own implementation of the secular equation with the same material parameters and compares the submitted values within a suitable tolerance."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that independently solves the same physical model and recomputes the expected eigenenergies and overlap integrals. For each row in your CSV files, the verifier compares your reported values to the reference values within a small tolerance. The final reward is the fraction of matching rows, equally weighted between the two output files. You must genuinely solve the secular equation and compute the integrals; merely guessing or hardcoding numbers will not match the verifier’s independent computation. There is no separate training or holdout split; the verifier checks your computed quantities directly against the correct physics.