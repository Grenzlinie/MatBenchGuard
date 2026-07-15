# Compton Profile of TiC from RFA Model

## Problem background
Transition-metal carbides such as TiC exhibit complex electronic structure, with band‑structure calculations predicting opposing directions of charge transfer between Ti and C. Compton scattering, being sensitive to the momentum distribution of valence electrons, can help distinguish between the two proposed charge configurations. The renormalised‑free‑atom (RFA) model provides a tractable way to compute spherically averaged Compton profiles from free‑atom wavefunctions, incorporating the effects of the lattice and electron occupation. This task reproduces the RFA Compton profiles of TiC for two different valence charge configurations, enabling a comparison of the resulting momentum‑space signatures.

## Approach
The RFA model truncates free‑atom radial wavefunctions at the Wigner–Seitz sphere around each atom and renormalises them to unity inside the sphere, giving an RFA wavefunction \(\varphi_0\). The TiC face‑centred cubic lattice (lattice constant \(a = 8.176\) au) is treated as two interpenetrating FCC sublattices (Ti and C). The Compton profile of each ion is built from the contributions of its valence orbitals according to the chosen charge configuration, with core‑electron contributions added from Biggs et al (1975). The total profile is normalised to 12.10 electrons over the interval \(q = 0\)–5 au by a global rescaling. The Fermi momentum \(p_{\mathrm{F}}\) is derived from the eight valence electrons per formula unit and the unit cell volume.

**s‑electron Compton profile**

The spherically averaged Compton profile for an s electron is

\[
J(q) = 4\pi \sum_{n=0}^{\infty} |\psi_0(K_n)|^2 \, G_n(q)
\]

where \(\psi_0(K_n)\) is the Fourier transform of the RFA wavefunction evaluated at the reciprocal‑lattice vector magnitude \(K_n\), and the functions \(G_n(q)\) encode the Fermi‑surface geometry. For a cubic lattice:

\[
G_0(q) = \tfrac{1}{2}(p_{\mathrm{F}}^2 - q^2)
\]

and for \(n \neq 0\),

\[
G_n(q) = 
\begin{cases}
0 & q > K_n + p_{\mathrm{F}},\\[2pt]
\displaystyle
\frac{N_n}{4K_n}\Big[ (p_{\mathrm{F}}^2 - K_n^2)(K_n + p_{\mathrm{F}} - q) - \tfrac{1}{3}\big((K_n + p_{\mathrm{F}})^3 - q^3\big) + K_n\big((K_n + p_{\mathrm{F}})^2 - q^2\big) \Big], & K_n - p_{\mathrm{F}} \le q \le K_n + p_{\mathrm{F}},\\[6pt]
G_n(K_n - p_{\mathrm{F}}) & q < K_n - p_{\mathrm{F}}.
\end{cases}
\]

Here \(N_n\) is the number of reciprocal‑lattice points in the \(n\)-th cell and \(K_n\) is the distance from the origin to those points.

**p and d electron Compton profile**

For p and d electrons we use a tight‑binding limit with spherical averaging. After constructing a Bloch sum from atomic orbitals \(\chi_l\) centred on lattice sites, the momentum density per atom for orbital angular momentum \(l\) is

\[
\rho_l(p) = 2\,\frac{2l+1}{4\pi}\,|R_l(p)|^2\, Q(p),
\]

where the radial Fourier transform is

\[
R_l(p) = \sqrt{\frac{2}{\pi}} \int_0^\infty r^2 R_l(r)\, j_l(pr)\, dr,
\]

\(R_l(r)\) is the normalised radial part of the RFA wavefunction, and \(Q(p) = \sum_{n=0}^\infty F_n(p)\). The auxiliary functions \(F_n(p)\) are

\[
F_0(p) = \begin{cases} 1 & p \le p_{\mathrm{F}},\\ 0 & \text{otherwise,} \end{cases}
\]

\[
F_n(p) = N_n\,\frac{p_{\mathrm{F}}^2 - (K_n - p)^2}{4K_n p} \qquad (n \ge 1).
\]

The contribution to the Compton profile from electrons of angular momentum \(l\) is then

\[
J_l(q) = 2\,\frac{2l+1}{4\pi} \sum_{n=0}^\infty \int_{p_1}^{p_2} |R_l(p)|^2\, F_n(p)\, p\, dp,
\]

with integration limits

\[
p_2 = K_n + p_{\mathrm{F}},\quad
p_1 = \begin{cases}
q, & |q - K_n| \le p_{\mathrm{F}},\\
K_n - p_{\mathrm{F}}, & q < K_n - p_{\mathrm{F}}.
\end{cases}
\]

**Charge configurations**

Two valence charge configurations are considered:

- **Neckel et al (donor)**: Ti → C, Ti: \(3d^{2.35}\,4s^0\), C: \(2s^{1.99}\,2p^{3.66}\).  
- **Lye–Logothesis (acceptor)**: Ti ← C, C: \(2s^2\,2p^{0.75}\), Ti: \(3d^4\,4s^{0.75}\,4p^{0.5}\).

**Convolution with instrumental resolution**

To compare with experiment, the theoretical profile must be convolved with the residual instrumental function of the spectrometer. According to Manninen et al (1974) this function is a Gaussian with a full width at half maximum (FWHM) of 0.41 atomic units. Convolve each raw J(q) profile with this Gaussian before output.

## Reproduction target
Compute the spherically averaged Compton profile values J(q) for TiC, for momentum transfer q = 0.0, 0.1, 0.2, …, 5.0 au, using the RFA framework with the two charge configurations described above. Output a CSV file named `compton_profile_TiC.csv` with columns `q`, `J_RFA_Neckel` (donor configuration), and `J_RFA_Lye` (acceptor configuration). Each profile must be normalised to 12.10 electrons over the interval q ∈ [0,5] au.

## Assets

- Clementi & Roetti (1974) free-atom radial wavefunctions: 10.1016/0092-640X(74)90053-6
- Biggs et al (1975) core Compton profile tables: 10.1016/0092-640X(75)90013-0
- Manninen et al (1974) residual instrumental function: Gaussian with FWHM = 0.41 au (Phil. Mag. 29, 167; DOI: 10.1080/14786437408218556)
- Python standard scientific libraries: numpy,scipy

## Workflow steps

### Step 1: Compute raw RFA Compton profiles
- Role: process
- Action: Implement the renormalised free-atom (RFA) model for TiC, modelled as an FCC lattice with lattice constant a=8.176 au. Use free-atom radial wavefunctions from Clementi & Roetti (1974) and core Compton profile contributions from Biggs et al (1975). Compute spherically averaged Compton profiles J(q) for the two valence charge configurations (Neckel et al donor and Lye‑Logothesis acceptor) following the equations in the Approach section. Normalize each profile to 12.10 electrons over [0,5] au. Do **not** apply convolution yet. Write the raw (unconvolved) profiles to a temporary file.
- Evidence: `/app/outputs/raw_compton_profile.csv`
- Format: csv
- Contract: (temporary internal file) CSV with columns: q, J_RFA_Neckel_raw, J_RFA_Lye_raw for q = 0.0, 0.1, …, 5.0 au.

### Step 2: Convolve with instrumental resolution and produce final output
- Role: scored (load‑bearing)
- Action: Convolve each raw J(q) profile with a Gaussian of FWHM = 0.41 au (the residual instrumental function from Manninen et al 1974). Re‑normalize to 12.10 electrons over [0,5] au if necessary. Write the convolved profiles for q = 0.0, 0.1, …, 5.0 au to the final CSV.
- Output file: `/app/outputs/compton_profile_TiC.csv`
- Format: csv
- Contract: CSV with columns: q (float, momentum in au), J_RFA_Neckel (float, CP value for Neckel donor config after convolution), J_RFA_Lye (float, CP value for Lye‑Logothesis acceptor config after convolution). Rows for q = 0.0, 0.1, …, 5.0 au.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/compton_profile_TiC.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### compton_profile_TiC.csv
- path: `/app/outputs/compton_profile_TiC.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Compton profile values J(q) for TiC computed with the RFA model, convoluted with the instrumental resolution function (Gaussian, FWHM=0.41 au), for two charge configurations, normalized to 12.10 electrons over [0,5] au. Values for q=0.0,0.1,...,5.0 au.
- schema:
  - `type`: table
  - `required_columns`: `q`, `J_RFA_Neckel`, `J_RFA_Lye`
  - `items`: object
  - `units`: object

Notes: Convolution step added to match the gold values from the paper's Table 1.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "compton_profile_TiC.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "q",
          "J_RFA_Neckel",
          "J_RFA_Lye"
        ],
        "items": {},
        "units": {}
      },
      "description": "Compton profile values J(q) for TiC computed with the RFA model, convoluted with the instrumental resolution function (Gaussian, FWHM=0.41 au), for two charge configurations, normalized to 12.10 electrons over [0,5] au. Values for q=0.0,0.1,...,5.0 au."
    }
  ],
  "notes": "Convolution step added to match the gold values from the paper's Table 1."
}
```

## How you are scored
Your submitted output file will be checked by a hidden verifier that compares your computed J_RFA_Neckel and J_RFA_Lye values at each q point against reference values. Points that match the reference within a per‑point absolute tolerance count as correct; the overall reward is the fraction of correct points across both configurations, combined into a single score. The evaluation requires no manual inspection—only the data in your CSV file are considered.
