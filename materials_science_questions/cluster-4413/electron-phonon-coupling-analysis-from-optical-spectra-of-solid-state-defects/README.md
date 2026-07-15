# Electron-phonon coupling analysis from optical spectra of solid-state defects

This workflow family contains computational analyses that quantify electron–phonon coupling in point defects or impurity centers by extracting key parameters from low‑temperature photoluminescence, absorption, or excitation spectra.

## Main computational pattern

The core pattern across tasks is:

1. **Identify and locate the zero‑phonon line (ZPL)** – the narrow electronic transition without phonon participation – from measured optical spectra.
2. **Analyze phonon‑assisted sidebands** – measure the energy positions and intensities of vibronic replicas relative to the ZPL.
3. **Model the electron‑phonon interaction** using appropriate physical frameworks:
   - Poisson distribution fitting of vibronic intensity profiles (Huang–Rhys model)
   - Configuration‑coordinate diagrams with harmonic parabolas
   - Multi‑mode effective‑phonon approximations
   - More fine‑grained models (crystal‑field Hamiltonians, Jahn–Teller coupling, etc. where necessary)
4. **Extract coupling constants** – Huang–Rhys factor \(S\), dominant phonon energy \(\hbar\omega\), stabilization energy (relaxation energy) \(S\hbar\omega\), and where relevant, crystal‑field parameters, activation barriers, or exciton‑phonon matrix elements.
5. **Validate** numerically by comparing extracted parameters against reference data or by checking the internal consistency of the spectral reconstruction.

The workflow is *dry lab* – it requires only pre‑existing digitized spectral data; no new experiments are performed. Tasks typically provide a set of optical spectra (e.g., ZPL positions, band widths, Stokes shifts) and ask to compute the coupling parameters using the models described in the respective papers.

## Typical resources

- **Input data:** low‑temperature PL, absorption, or excitation spectra in the form of tabulated peaks, linewidths, and relative intensities. Often taken directly from published tables or figures.
- **Models:** the chosen paper’s equations for electron‑phonon coupling (e.g., Poisson distribution for multiphonon transitions, configuration‑coordinate model, crystal‑field Hamiltonian). The implementation is self‑contained within the task.
- **Tools:** Numerical optimization routines (least squares, Nelder–Mead simplex, etc.) for parameter fitting; linear algebra for diagonalizations; custom scripts in Python/MATLAB/C/Fortran as used in the original papers. The task’s `instruction.md` lists any required external libraries.

No external datasets beyond the compiled spectral values are needed; all necessary physical constants and reference values are provided within each task.

## Verification style

Verification is **numeric**: the extracted parameters (Huang‑Rhys factor \(S\), ZPL energy, phonon energy \(\hbar\omega\), etc.) are compared against previously reported values or values obtained from independent methods, using absolute or relative tolerances. The verify note states: “通过比较提取的参数（如ZPL能量、Huang-Rhys因子S、主导声子能量）与参考值或独立方法的数值容差进行验证。”  
Thus, a task typically checks that the solver’s output numerical values match the expected ones within a prescribed error margin.

## Harbor task structure

The family contains 164 papers (245 individual tasks). Each paper resides in a directory named `paper-<paper_id>`. Inside each `paper-*` folder, the public‑facing entry is `instruction.md` which specifies:
- The relevant spectral data and goal
- The specific computational procedure to follow
- The expected output parameters and tolerances

No `TASK.md` is used; the solver interfaces only with `instruction.md`.

This README provides an overview; for detailed running instructions, consult each `instruction.md`.
