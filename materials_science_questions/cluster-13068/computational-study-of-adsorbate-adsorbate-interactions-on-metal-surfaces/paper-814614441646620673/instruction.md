# Atomic total energies and cohesive energy of sodium from spin-density functional theory

## Problem background
The local-density (LD) approximation of Kohn–Sham density functional theory has been widely applied to metals, but it systematically overestimates the cohesive energy of simple metals such as sodium. One suspected source of the discrepancy is the inadequate description of the isolated atom: the outermost electron has an unpaired spin, yet the LD approximation treats exchange and correlation using a spin‑compensated (paramagnetic) electron liquid as the reference. The local‑spin‑density (LSD) approximation generalizes the approach by allowing spin polarization and uses the spin‑polarized homogeneous electron liquid as the local model. By implementing a self‑consistent Kohn–Sham solver that incorporates this spin dependence, we can compute more accurate atomic total energies and assess how the spin‑polarization correction affects the calculated cohesive energy of sodium.

## Physical model and Kohn–Sham equations
You must implement a self‑consistent spherical Kohn–Sham solver for isolated atoms. The equations below are to be solved in atomic units (energies in Rydbergs, \(\hbar = 1\), \(m_e = 1/2\), \(e^2 = 2\), Bohr radius \(a_0 = 1\)).

### Unit conversion
When converting between energy units, use the following conversion factor throughout this problem:
- **1 Rydberg (Ry) = 13.6 electron‑volts (eV).**

### Radial Kohn–Sham equations
For each spin channel \(s \in \{+, -\}\) and each occupied orbital \(i\), the radial wavefunction \(P_{i,s}(r) = r \, \psi_{i,s}(r)\) obeys
\[
-\frac{1}{2} \frac{d^2 P_{i,s}}{dr^2} + \left[ \frac{l(l+1)}{2r^2} + V_{\text{eff}}^s(r) \right] P_{i,s}(r) = \epsilon_{i,s} \, P_{i,s}(r),
\]
where \(l\) is the orbital angular momentum quantum number.

### Effective potential
\[
V_{\text{eff}}^s(r) = -\frac{Z}{r} + V_H(r) + \mu_s^{\text{xc}}(r),
\]
with \(Z\) the nuclear charge, \(V_H(r)\) the Hartree (electrostatic) potential, and \(\mu_s^{\text{xc}}(r)\) the exchange‑correlation potential for spin \(s\) given by Eq. (3) in the Approach section.

### Electron densities and spin polarization
The electron density for spin \(s\) is built from the occupied orbitals using the occupation numbers \(f_{i,s}\):
\[
n_s(r) = \frac{1}{4\pi r^2} \sum_i f_{i,s} \, |P_{i,s}(r)|^2 .
\]
The total density is \(n(r) = n_+(r) + n_-(r)\); the spin density is \(m(r) = n_+(r) - n_-(r)\). The Wigner‑Seitz radius \(r_s(r)\) is defined by \(\frac{4\pi}{3} r_s^3\, n = 1\), and the fractional spin polarization is \(\zeta(r) = m(r) / n(r)\).

### Hartree potential
\[
V_H(r) = \frac{1}{r} \int_0^r 4\pi r'^2 n(r') dr' + \int_r^\infty 4\pi r' n(r') dr' .
\]

### Total atomic energy
After self‑consistency is reached, the total energy (in Rydbergs) is
\[
E_{\text{tot}} = \sum_s \sum_i f_{i,s}\, \epsilon_{i,s} \;-\; \frac{1}{2}\int V_H(r)\, n(r)\, d^3r \;+\; \int \Big[\epsilon^{\text{xc}}(r_s,\zeta) - \sum_s \mu_s^{\text{xc}}(r)\, \frac{n_s(r)}{n(r)}\Big] n(r)\, d^3r,
\]
where \(\epsilon^{\text{xc}}\) and \(\mu_s^{\text{xc}}\) are given by the interpolation formulas in the Approach section.

### Electron configurations and spin occupation
- **Hydrogen (\(Z=1\))**: one electron in the 1s orbital (\(l=0\)). In the LSD approximation the electron is spin‑up, so \(n_+ = n\), \(n_- = 0\) and \(\zeta = 1\) everywhere. In the LD approximation you must force \(\zeta = 0\) at every iteration.
- **Sodium (\(Z=11\))**: electron configuration \(1s^2 2s^2 2p^6 3s^1\). The core orbitals (1s, 2s, 2p) are completely filled and spin‑paired; the 3s orbital is half‑filled and spin‑up. In LSD this natural spin arrangement should emerge from self‑consistency (you assign occupation numbers accordingly: for the core, one electron of each spin in each orbital; for 3s, one spin‑up electron, zero spin‑down). In LD you force \(\zeta = 0\) to simulate the spin‑compensated approximation.

## Approach
You will implement a self‑consistent spherical Kohn–Sham solver for atoms. The exchange‑correlation functional is treated in the local‑density (LD) or local‑spin‑density (LSD) approximation. In both cases the exchange‑correlation energy per particle and the spin‑dependent potentials are obtained from interpolation formulas for the homogeneous electron liquid, parametrized by the Wigner‑Seitz radius \(r_s\) and the fractional spin polarization \(\zeta\).

The exchange‑correlation energy per particle (in Rydbergs) is:

\[
\epsilon^{\mathrm{xc}}(r_s,\zeta) = \epsilon_P^{\mathrm{xc}} + (\epsilon_F^{\mathrm{xc}} - \epsilon_P^{\mathrm{xc}})\, f(\zeta),
\]
\[
f(\zeta) = \frac{(1+\zeta)^{4/3} + (1-\zeta)^{4/3} - 2}{2^{4/3} - 2},
\]
with the paramagnetic (\(P\)) and ferromagnetic (\(F\)) limits given by
\[
\epsilon_i^{\mathrm{xc}} = \epsilon_i^{x} - c_i\Big[(1+x_i^3)\ln(1+1/x_i) + \tfrac12 x_i - x_i^2 - \tfrac13\Big], \; i=P,F,
\]
where \(x_i = r_s / r_i\), \(\epsilon_P^{x} = -\frac{3}{2\pi\alpha\, r_s}\), \(\alpha = (4/9\pi)^{1/3}\), \(\epsilon_F^{x} = 2^{1/3}\epsilon_P^{x}\), and the constants are \(c_P = 0.0666\), \(c_F = 0.0406\), \(r_P = 11.4\), \(r_F = 15.9\).

The exchange‑correlation potentials for spin‑up (\(+\)) and spin‑down (\(-\)) electrons (in Rydbergs) are
\[
\mu_{\pm}^{\mathrm{xc}}(r_s,\zeta) = -\frac{2}{\pi\alpha\, r_s}
\Bigl( \beta \pm \frac13\frac{\delta\,\zeta}{1 \pm \gamma\,\zeta} \Bigr),
\]
with
\[
\beta = 1 + 0.0545\, r_s \ln(1 + 11.4/r_s),
\]
\[
\delta = 1 - 0.036\, r_s - \frac{1.36\, r_s}{1 + 10\, r_s},
\]
\[
\gamma = 0.297.
\]

You will run the solver for two systems: the hydrogen atom (\(Z=1\)) and the sodium atom (\(Z=11\)). For each atom you will perform two calculations – one with self‑consistent spin polarization (LSD; \(\zeta\) from the local spin density) and one with the polarization locked to zero (LD; \(\zeta=0\)). From the sodium results you will then compute an improved LSD cohesive energy by combining Tong’s published LD cohesive energy of sodium metal, 1.39 eV/atom, with the difference between the LD and LSD atomic total energies and a small correlation‑interpolation correction of 0.07 eV.

## Physical consistency checks (scored)
Your computed energies will be evaluated against the following physical criteria, which arise from the known behaviour of the exact and approximate functionals:
- For the hydrogen atom, the LSD total energy must be **lower** (more negative) than the LD total energy, because spin polarisation improves the exchange‑correlation description.
- The LSD hydrogen energy must lie within **0.272 eV** of the exact non‑relativistic hydrogen ground‑state energy, \(-13.6\,\text{eV}\), i.e. it must satisfy \( |E_{\text{LSD}} + 13.6| \le 0.272\,\text{eV} \).
- For the sodium atom, the LSD total energy must be **lower** (more negative) than the LD total energy.

These checks are part of the reward computation; failing them reduces your score. The hidden verifier also compares your absolute energies to the physically correct values within tight tolerances.

## Reproduction target
Your goal is to produce three artifacts by running the above calculations:

1. **Hydrogen atom total energies** — the total energy of the hydrogen atom in both the LSD and LD approximations, reported in electron‑volts (eV). Use the conversion factor given above.
2. **Sodium atom total energies** — the total energy of the sodium atom in both the LSD and LD approximations, reported in Rydbergs (Ry).
3. **Sodium cohesive energy** — the LSD cohesive energy of sodium, computed as  
   \(E_{\mathrm{coh}}^{\mathrm{LSD}} = 1.39\,\mathrm{eV} + (E_{\mathrm{atom}}^{\mathrm{LD}} - E_{\mathrm{atom}}^{\mathrm{LSD}}) + 0.07\,\mathrm{eV}\),  
   where \(E_{\mathrm{atom}}^{\mathrm{LD}}\) and \(E_{\mathrm{atom}}^{\mathrm{LSD}}\) are the sodium total energies from step 2 converted to eV (using 1 Ry = 13.6 eV). The result must be written in eV.

All energies must be obtained from a self‑consistent solution of the Kohn–Sham equations with the exchange‑correlation formulas above, using your own numerical solver; you may not use pre‑computed atomic data or tabulated energies.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Hydrogen atom total energies
- Role: scored
- Action: Implement the self‑consistent spherical Kohn–Sham solver described above. Compute the total energy of the hydrogen atom (\(Z=1\)) in the LSD (spin polarised) and LD (paramagnetic, \(\zeta=0\)) approximations. Write a CSV file with two rows.
- Output file: `/app/outputs/step_01_hydrogen_energies.csv`
- Format: csv
- Contract: Two rows. Columns: method (string, either 'LSD' or 'LD'), total_energy_eV (float, negative, in eV).
- Scoring: checked against paper gold values and against the physical consistency checks listed in “Physical consistency checks”.

### Step 2: Sodium atom total energies
- Role: scored
- Action: Using the same Kohn–Sham solver, compute the total energy of the sodium atom (\(Z=11\)) in the LSD and LD approximations. Write a CSV file with two rows, reporting energies in Rydbergs.
- Output file: `/app/outputs/step_02_sodium_energies.csv`
- Format: csv
- Contract: Two rows. Columns: method (string, either 'LSD' or 'LD'), total_energy_Ry (float, negative, in Rydbergs).
- Scoring: checked against paper gold values and against the physical ordering requirement (LSD < LD).

### Step 3: Sodium cohesive energy
- Role: scored (load-bearing)
- Action: Read the sodium atom energies from step_02. Compute the improved LSD cohesive energy of sodium using Tong's published LD cohesive energy (1.39 eV/atom) and a correlation‑energy interpolation correction (0.07 eV) as: \(E_{\text{coh}}^{\text{LSD}} = 1.39\,\text{eV} + (E_{\text{atom}}^{\text{LD}} - E_{\text{atom}}^{\text{LSD}}) + 0.07\,\text{eV}\), where \(E_{\text{atom}}^{\text{LD}}\) and \(E_{\text{atom}}^{\text{LSD}}\) are the total energies from step_02 converted to eV using 1 Ry = 13.6 eV. Write the resulting value in eV to a text file.
- Output file: `/app/outputs/step_03_sodium_cohesive_energy.txt`
- Format: txt
- Contract: Single floating-point number (in eV, positive) in plain text.
- Scoring: compared to the expected value with a tolerance.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_hydrogen_energies.csv`
- `/app/outputs/step_02_sodium_energies.csv`
- `/app/outputs/step_03_sodium_cohesive_energy.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_hydrogen_energies.csv
- path: `/app/outputs/step_01_hydrogen_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total energies of the hydrogen atom in LSD and LD approximations.
- schema:
  - `type`: table
  - `required_columns`: `method`, `total_energy_eV`
  - `units`:
    - `total_energy_eV`: eV

### step_02_sodium_energies.csv
- path: `/app/outputs/step_02_sodium_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total energies of the sodium atom in LSD and LD approximations, in Rydbergs.
- schema:
  - `type`: table
  - `required_columns`: `method`, `total_energy_Ry`
  - `units`:
    - `total_energy_Ry`: Rydbergs

### step_03_sodium_cohesive_energy.txt
- path: `/app/outputs/step_03_sodium_cohesive_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Improved LSD cohesive energy of sodium, combining atom energies with Tong's reference value and a correlation correction.
- schema:
  - `type`: text
  - `content_type`: single_float
  - `units`: eV

Notes: All outputs are fixed physical quantities; the checker compares the agent's reported values to hidden paper gold numbers within tolerances. Units are as declared. The agent must compute the Kohn–Sham atom energies from scratch using the provided exchange‑correlation interpolation formulas.

## How you are scored
Each workflow stage produces a required artifact. A hidden verifier independently checks every artifact after your run finishes:
- For the hydrogen total energies (step 1), the verifier checks: (i) both LSD and LD values exist, (ii) they are within a tight tolerance of the correct physical values, (iii) the LSD energy is lower (more negative) than the LD energy, and (iv) the LSD energy lies within 0.272 eV of the exact non‑relativistic hydrogen energy (\(-13.6\,\text{eV}\)).
- For the sodium total energies (step 2), the verifier checks: (i) both LSD and LD values exist, (ii) they are within tolerance, and (iii) the LSD energy is lower than the LD energy.
- For the cohesive energy (step 3), the verifier checks that the submitted number matches the expected value within a tolerance.

The final reward (0 to 1) is a weighted sum of the scores from the three stages. Failure to meet the ordering or proximity conditions described above will reduce your score.