# Charge state probabilities from occupation-dependent hopping in atom-surface scattering

## Problem background
When atoms are scattered from metal surfaces, electrons can tunnel between the atom and the surface, leaving the scattered particle as a positive ion, a neutral atom, or a negative ion. A widely used theoretical framework for this process is the time-dependent Anderson model, which includes the intra-atomic Coulomb repulsion between two electrons on the same adsorbate orbital. In the standard implementation, the hopping matrix elements that couple the atom and the metal are assumed to be independent of the occupation of the atom's spin states. However, because charge transfer often occurs at large atom-surface distances where the electron binding energy changes, the hopping amplitude can depend on the occupation of the opposite spin. This introduces a self-consistency that allows a single unified description of positive, neutral, and negative ion production, rather than treating them separately in a one-electron picture. The task is to compute the final charge-state probabilities predicted by this self-consistent two-electron model for a prototype alkali atom (Na) and to compare the results with simpler approximations where the occupation dependence is frozen.

## Model specification
The calculation is carried out within the two-electron Hartree-Fock approximation. All quantities are expressed in atomic units (au) unless otherwise stated. The following formulas, taken from the original paper, define the model completely.

### Trajectory
The atom moves along a classical trajectory perpendicular to the surface with constant speed \(v = 0.01\) au:
\[
z(t) = v\,|t|,
\]
where \(z\) is the atom-surface distance and \(t\) is time. The motion is symmetric: the atom approaches the surface from \(t \to -\infty\), reaches the turning point \(z=0\) at \(t=0\), and recedes for \(t \to \infty\).

### Energy levels with image-potential corrections
The bare adsorbate energy level \(\epsilon_a(z)\) and the intra-atomic Coulomb repulsion \(U(z)\) are modified by the image interaction and depend on distance:
\[
\epsilon_a(z) = -I + \frac{1}{4(z+z_0)}, \qquad
U(z) = I - A - \frac{1}{2(z+z_0)}.
\tag{10,11}
\]
Here \(I = 5.14\) eV is the ionization potential, \(A = 0.55\) eV the electron affinity (for sodium), and \(z_0 = 3\) au is a cutoff parameter that reduces the image shift at small distances.

The instantaneous one-electron energy for spin \(\sigma\) is
\[
E_{a,\sigma}(z) = \epsilon_a(z) + U(z)\,\langle n_{a,-\sigma}(t)\rangle,
\tag{6}
\]
where \(\langle n_{a,\sigma}(t)\rangle\) is the expectation value of the occupation number of the adsorbate orbital with spin \(\sigma\).

### Hopping width and decay parameter
The width function (level broadening) that enters the master equations is
\[
\Delta_\sigma(t) = \Delta_0 \exp[-2\gamma_\sigma\,z(t)], \qquad \Delta_0 = 5\;{\rm eV}.
\tag{14,15}
\]
The decay parameter \(\gamma_\sigma\) depends on the instantaneous occupation of the opposite spin:
\[
\gamma_\sigma = \sqrt{2\,|E_{a,-\sigma}|} = \sqrt{2\big|\epsilon_a(z) + U(z)\,\langle n_{a,\sigma}(t)\rangle\big|}.
\tag{8}
\]

### Semi-classical master equations
The time evolution of the spin occupations is governed by
\[
\frac{d\langle n_{a,\sigma}(t)\rangle}{dt} = 2\,\Delta_{\sigma}(t)\,
\big[N_{a,\sigma}(z(t)) - \langle n_{a,\sigma}(t)\rangle\big],
\qquad \frac{d\langle n_{a,-\sigma}(t)\rangle}{dt} = 2\,\Delta_{-\sigma}(t)\,
\big[N_{a,-\sigma}(z(t)) - \langle n_{a,-\sigma}(t)\rangle\big].
\tag{16,17}
\]

### Equilibrium (static) occupation numbers
\(N_{a,\sigma}(z)\) is the distance-dependent equilibrium occupation for spin \(\sigma\), obtained by solving the static Hartree-Fock self-consistency equation at temperature \(T = 0\):
\[
N_{a,\sigma} = f(E_{a,\sigma} - E_F), \qquad
f(x) = \begin{cases} 1, & x < 0 \\ 0, & x > 0 \end{cases},
\qquad E_{a,\sigma} = \epsilon_a(z) + U(z)\,N_{a,-\sigma}.
\tag{6}
\]
We set the vacuum level to zero as the energy reference, so the Fermi energy is related to the metal work function \(\phi\) by
\[
E_F = -\phi.
\]
Thus, for a given distance \(z\) and work function \(\phi\), one solves the coupled nonlinear equations
\[
N_\uparrow = f\big(\epsilon_a(z) + U(z) N_\downarrow + \phi\big), \qquad
N_\downarrow = f\big(\epsilon_a(z) + U(z) N_\uparrow + \phi\big)
\]
self-consistently (e.g. by iteration). Because the two spins are symmetric, one has \(N_\uparrow = N_\downarrow\), and the equation reduces to
\[
N = f\big(\epsilon_a(z) + U(z) N + \phi\big).
\]

### Limiting cases of the decay parameter
To isolate the effect of the occupation-dependent hopping, the master equations are also solved with two frozen choices of \(\gamma_\sigma\):
- **gamma0**: assumes the opposite spin is always empty, \(\langle n_{a,-\sigma}\rangle = 0\).
  \[
  \gamma_0(z) = \sqrt{2\,|\epsilon_a(z)|}.
  \]
- **gamma1**: assumes the opposite spin is always occupied, \(\langle n_{a,-\sigma}\rangle = 1\).
  \[
  \gamma_1(z) = \sqrt{2\,|\epsilon_a(z) + U(z)|}.
  \]
In these cases the hopping width \(\Delta\) still varies with \(z\) via \(\gamma_0(z)\) or \(\gamma_1(z)\), but no longer depends self-consistently on the instantaneous occupations.

### Charge-state probabilities
The expectation values for producing a positive ion (\(P_+\)), a neutral atom (\(P_0\)), and a negative ion (\(P_-\)) at time \(t\) are given by
\[
\begin{aligned}
P_+(t) &= \big[1 - \langle n_{a,\sigma}(t)\rangle\big]\big[1 - \langle n_{a,-\sigma}(t)\rangle\big], \\
P_0(t) &= \langle n_{a,\sigma}(t)\rangle\big[1 - \langle n_{a,-\sigma}(t)\rangle\big] +
         \langle n_{a,-\sigma}(t)\rangle\big[1 - \langle n_{a,\sigma}(t)\rangle\big], \\
P_-(t) &= \langle n_{a,\sigma}(t)\rangle\,\langle n_{a,-\sigma}(t)\rangle.
\end{aligned}
\tag{18-20}
\]

### Parameter summary
| Parameter | Value | Description |
|-----------|-------|-------------|
| \(I\)     | 5.14 eV | Na ionization potential |
| \(A\)     | 0.55 eV | Na electron affinity |
| \(\Delta_0\) | 5 eV | Half-width at \(z=0\) |
| \(z_0\)    | 3 au   | Image-potential cutoff |
| \(v\)      | 0.01 au | Atom velocity |
| \(\phi\)   | 1.5–6.0 eV (step 0.5 eV) | Metal work function |
| \(T\)      | 0 K    | Temperature (Fermi function is a step) |

## Approach
The calculation proceeds in two stages. First, the static Hartree-Fock equations are solved self-consistently for the chosen atom (Na) to obtain distance‑dependent equilibrium spin occupations \(N_{a,\sigma}(z)\) and adiabatic energies for the range of metal work functions. Second, the semi‑classical master equations are integrated along the trajectory \(z(t)=v|t|\) starting from the initial condition \(\langle n_{a,\sigma}(-\infty)\rangle = N_{a,\sigma}(z_\infty)\) with a suitably large initial distance (e.g. \(z_\infty = 50\) au). From the asymptotic occupations at \(t\to\infty\) the final ion probabilities are computed. To isolate the effect of the occupation‑dependent hopping, the calculation is repeated for three variants of the decay parameter that enters the master equations: the full self‑consistent \(\gamma_\sigma\), and the two limiting cases \(\gamma_0\) (opposite spin empty) and \(\gamma_1\) (opposite spin occupied). The comparison between the three cases reveals how the self-consistency changes the predicted charge‑state fractions.

## Reproduction target
Produce a CSV file containing the asymptotic charge‑state probabilities \(P_+\), \(P_0\), \(P_-\) for a sodium (Na) atom scattering from a metal surface at velocity \(v = 0.01\) au, as a function of the metal work function \(\phi\) ranging from 1.5 eV to 6.0 eV (in steps of 0.5 eV). The probabilities must be computed for three choices of the decay parameter: **gamma_sigma** (the self‑consistent occupation‑dependent expression), **gamma0** (opposite‑spin occupation set to zero), and **gamma1** (opposite‑spin occupation set to one). All calculations must use the two‑electron Hartree‑Fock method with the fixed parameters listed in the model specification. The output file must have exactly five columns: `phi` (eV, numeric), `gamma_type` (string, one of `gamma_sigma`, `gamma0`, `gamma1`), `P_plus` (numeric, dimensionless), `P_zero` (numeric, dimensionless), and `P_minus` (numeric, dimensionless). Rows must be grouped by `gamma_type` and sorted by `phi` ascending within each group; the groups must appear in the order `gamma_sigma`, `gamma0`, `gamma1`.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute equilibrium occupation numbers (intermediate)
- Role: process
- Action: Solve the static two-electron Hartree-Fock equations for Na (I=5.14 eV, A=0.55 eV, Δ0=5 eV, z0=3 au, image potentials as given in the model specification) to obtain the distance-dependent equilibrium spin occupations \(N_{a,\sigma}(z)\) for work functions in the range 1.5–6 eV. A convenient range of distances is \(z = 0\) to \(z_\infty = 50\) au, sampled finely enough to allow accurate integration of the master equations. These quantities are required to drive the subsequent dynamic master equations.
- Evidence: `/app/outputs/eq_occupations.csv` (format not prescribed; it is an intermediate artifact and is not scored, but must be produced by your code).

### Step 2: Compute charge state probabilities for Na scattering
- Role: scored (load-bearing)
- Action: Using the equilibrium occupations from the previous step, solve the coupled semi-classical master equations along the trajectory \(z(t)=v|t|\) with \(v=0.01\) au. For each work function phi (1.5 to 6 eV, step 0.5 eV) obtain the asymptotic occupation numbers at \(t\to +\infty\) and convert them to probabilities \(P_+\), \(P_0\), \(P_-\) via the combinatorial formulas given in the model specification. Perform the calculation for three variants of the decay parameter: `gamma_sigma` (occupation-dependent), `gamma0` (\(\langle n_{a,-\sigma}\rangle=0\)), and `gamma1` (\(\langle n_{a,-\sigma}\rangle=1\)).
- Output file: `/app/outputs/step_02_probabilities.csv`
- Format: csv
- Contract: Columns: `phi` (float, eV), `gamma_type` (string, one of `gamma_sigma`,`gamma0`,`gamma1`), `P_plus` (float), `P_zero` (float), `P_minus` (float). Row order: all rows for `gamma_sigma` sorted by `phi` ascending, then `gamma0`, then `gamma1`.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eq_occupations.csv` (intermediate, not scored)
- `/app/outputs/step_02_probabilities.csv` (scored)

## How you are scored
A hidden verifier will read your submitted CSV file and independently score it. The verifier checks two aspects. (1) For the gamma_sigma variant, it compares your P_plus, P_zero, and P_minus values at each work function to reference values digitized from the published computational study, using a combined absolute and relative tolerance. (2) It verifies that certain expected structural trends hold between the three gamma variants: for work functions above 1.5 eV, P_minus for gamma_sigma should be lower than P_minus for gamma0, and P_plus for gamma_sigma should be higher than P_plus for gamma0. The overall reward is a weighted combination of how well the individual numbers match the reference and how well the trend checks are satisfied. Simply reporting numbers that pass the checks is not sufficient; the numbers must be produced by an actual implementation of the two‑electron Hartree‑Fock master equations described in the workflow steps.