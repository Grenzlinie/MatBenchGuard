# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes

This workflow family implements a predictive computational protocol for estimating the superconducting critical temperature \(T_c\) of materials where the pairing mechanism is mediated by electron–phonon interactions. The core formula is the McMillan (Allen–Dynes) expression:

\[
T_c = \frac{\omega_{\log}}{1.2} \exp\!\left[-\frac{1.04(1+\lambda)}{\lambda - \mu^*(1+0.62\lambda)}\right]
\]

where  
- \(\lambda\) is the electron–phonon coupling constant,  
- \(\omega_{\log}\) is the logarithmic average phonon frequency,  
- \(\mu^*\) is the retarded Coulomb pseudopotential.  

The workflow encompasses the full chain from first‑principles electronic structure to final \(T_c\) estimation, primarily using density functional theory (DFT) and density functional perturbation theory (DFPT) calculations.

## Common Computational Pattern

1. **Structure Determination** – The atomic geometry of the material (often under high pressure or doping) is obtained from experimental data, crystal structure databases, or evolutionary structure searches. Many papers use relaxed structures from DFT total‑energy minimizations.

2. **Electronic Structure Calculation** – Self‑consistent DFT calculations (plane‑wave/pseudopotential, PAW, or LAPW methods, using codes such as Quantum ESPRESSO, VASP, or all‑electron codes) provide the electronic band structure, density of states at the Fermi level \(N(E_F)\), and Fermi surface topology. Exchange‑correlation functionals like PBE‑GGA or LDA are typical.

3. **Phonon and Electron–Phonon Coupling (EPC) Calculation** – DFPT or linear‑response methods are used to compute the phonon dispersion and the electron–phonon matrix elements \(g_{k n, k+q m}^\nu\). From these, the Eliashberg spectral function \(\alpha^2F(\omega)\) is built:

\[
\alpha^2F(\omega) = \frac{1}{2\pi N(E_F)} \sum_{\mathbf{q}\nu} \delta(\omega-\omega_{\mathbf{q}\nu}) \frac{\gamma_{\mathbf{q}\nu}}{\omega_{\mathbf{q}\nu}},
\]
where \(\gamma_{\mathbf{q}\nu}\) is the phonon linewidth. The isotropic EPC constant \(\lambda\) and the logarithmic average frequency \(\omega_{\log}\) are then derived:

\[
\lambda = 2\int_0^\infty \frac{\alpha^2F(\omega)}{\omega} d\omega, \qquad
\omega_{\log} = \exp\!\left[ \frac{2}{\lambda} \int_0^\infty \frac{\alpha^2F(\omega)}{\omega} \ln \omega \, d\omega \right].
\]

4. **Coulomb Pseudopotential** – A value for \(\mu^*\) is adopted (typically in the range 0.1–0.2) or estimated from the electronic structure (e.g., using the Morel–Anderson formula).

5. **Superconducting Temperature** – The McMillan–Allen–Dynes formula is applied to obtain \(T_c\). Some papers also solve the full isotropic Migdal–Eliashberg equations on the imaginary axis for more accurate strong‑coupling estimates, but the family primarily reports \(T_c\) via the MAD formula. Anisotropic and multiband treatments appear when needed (e.g., for iron pnictides or certain hydrides), using approaches like Helmholtz Fermi‑surface harmonics or two‑band Eliashberg.

6. **Post‑processing** – Derived properties such as superconducting gap \(\Delta\), isotope effect exponent \(\alpha\), and specific heat jump \(\Delta C/\gamma T_c\) may be computed from the gap equation or using established BCS/Eliashberg relations.

## Typical Dataset, Model, and Tool Categories

- **Materials datasets**: Binary and ternary hydrides, diborides, carbides, metallic glasses, organic superconductors, transition metals, 2D materials (MoS₂, borophene, etc.) under pressure or doping.  
- **DFT/DFPT codes**: Quantum ESPRESSO (plane‑wave/pseudopotential), VASP (PAW), LAPW codes (WIEN2k, NRL‑LAPW), and linear‑response packages.  
- **Pseudopotentials**: Ultrasoft, norm‑conserving, PAW; frequently PBE or LDA exchange‑correlation.  
- **Superconductivity models**: Isotropic McMillan‑Allen‑Dynes formula; Migdal‑Eliashberg equations on the imaginary axis; anisotropic HFSH‑Eliashberg; rigid‑muffin‑tin approximations (Gaspari‑Gyorffy) for Hopfield parameter.  
- **Post‑processing tools**: McMillan formula inversion to extract \(\lambda\) from heat‑capacity data; BCS gap calculations; Allen‑Dynes corrections.

## Verification Style

The typical verification is **numeric**: the computed \(T_c\) is compared against experimental critical temperatures (e.g., from resistivity, magnetization, or specific heat) using a tolerance‑based alignment. The reproduction is considered successful when the calculated \(T_c\) falls within a pre‑specified relative or absolute error margin of the reference experimental value. For example, the verify_note states “将计算得到的Tc数值与实验Tc进行容差对齐比较，偏差在一定范围内即认为复现成功。” (align computed Tc with experimental Tc within a tolerance range).

## Structure of a FlowForge Task

Each paper’s reproducibility attempt lives as a subdirectory `paper-*`, containing an `instruction.md` that describes the required resources and precise steps. The solving agent retrieves the necessary inputs (crystal structure, pseudopotentials, codes) and executes the workflow to generate outputs for verification. The family is “dry” (lab_type “dry”) – no wet‑lab experiments; all verification is performed via computational results.
