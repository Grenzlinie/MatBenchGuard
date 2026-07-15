# DFT dielectric function calculation from electronic structure

This workflow family covers **420 tasks** drawn from **307 publications** in materials science, condensed matter physics, computational physics, and optical materials. Its common goal is to compute the frequency‑dependent complex dielectric function (real and imaginary parts) starting from a density‑functional theory (DFT) electronic structure, and to report static dielectric constants together with characteristic spectral features.

The workflow is entirely computational (`dry`), and results are verified by **multimodal comparison**: computed dielectric spectra are visually matched against experimental or high‑precision theoretical reference spectra, with attention to peak positions, line shapes, and static dielectric values.

## Common computational pattern

All tasks in this family share the following core sequence:

1.  **Geometry optimisation** – Where required, the crystal structure is relaxed using DFT with a suitable exchange‑correlation functional (typically LDA, GGA‑PBE/PBEsol, or hybrid).
2.  **Electronic structure calculation** – Self‑consistent DFT yields Kohn‑Sham eigenvalues and wavefunctions. The electronic band structure and density of states are computed along high‑symmetry paths.
3.  **Interband transition matrix elements** – Momentum (dipole) matrix elements between valence and conduction states are evaluated on a dense regular **k**‑point mesh or via linear‑analytic tetrahedron integration.
4.  **Imaginary dielectric function $\varepsilon_2(\omega)$** – The independent‑particle (or random‑phase) approximation is used to sum over all direct allowed transitions:
    $$\varepsilon_{2}^{\alpha\beta}(\omega)=\frac{4\pi^{2}e^{2}}{m^{2}\omega^{2}}\sum_{v,c}\int_{\mathrm{BZ}}\!d^{3}k\, \langle \psi_{c\mathbf{k}}|p^{\alpha}|\psi_{v\mathbf{k}}\rangle\langle \psi_{v\mathbf{k}}|p^{\beta}|\psi_{c\mathbf{k}}\rangle\,\delta(E_{c\mathbf{k}}-E_{v\mathbf{k}}-\hbar\omega).$$
    A scissor operator (rigid shift of conduction bands) is often applied to correct the DFT band‑gap underestimation.
5.  **Real dielectric function $\varepsilon_1(\omega)$** – Obtained from $\varepsilon_2(\omega)$ via the Kramers‑Kronig transform.
6.  **Derived optical constants** – Absorption coefficient, refractive index, reflectivity, and electron energy‑loss function are computed from $\varepsilon(\omega)$.
7.  **Static dielectric constants** – $\varepsilon_1(0)$ and, where applicable, the ionic contribution to the static constant are extracted.

Advanced approaches (GW, BSE, hybrid functionals, density‑functional perturbation theory for phonon contributions) appear in some tasks but the independent‑particle DFT + Kramers‑Kronig workflow is the common denominator.

## Resource categories

- **Computational method** – Density functional theory (DFT) with exchange‑correlation functionals including LDA, GGA (PBE, PBEsol, WC), mBJ, and full‑range or dielectric‑dependent hybrids.
- **Basis sets** – Plane‑wave pseudopotential (CASTEP, Quantum ESPRESSO, VASP) or full‑potential linearised augmented plane wave (FP‑LAPW, WIEN2k).
- **Optical response** – Independent‑particle interband transitions, often with a scissor correction; Kramers‑Kronig transformation; additional optical constants derived from the complex dielectric function.
- **Input data** – Crystal structures are supplied directly in the task instructions; no external databases are required.

## Verification style

Results are verified by **multimodal visual comparison**:
- The computed $\varepsilon_1(\omega)$ and $\varepsilon_2(\omega)$ spectra (and other derived optical spectra) are plotted together with experimental measurements (ellipsometry, reflectivity, absorption) or with high‑precision theoretical spectra (e.g., from BSE).
- Agreement is judged on the basis of peak positions, relative intensities, spectral shape, and the static dielectric constant.

## Repository structure

Each `paper‑*` subdirectory corresponds to a standalone Harbor task. The public entry point is `instruction.md`, which contains:
- The specific DFT code, functional, and numerical parameters.
- The crystal structure and any scissor shifts.
- The required output quantities and verification instructions.

All resources needed to execute the workflow (input files, pseudopotentials, basis sets) are specified in `instruction.md` and bundled with the task; no additional external resources are required.
