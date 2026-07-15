# Phonon symmetry decomposition via group theory

This workflow family addresses the **group-theoretical decomposition of vibrational modes at high‑symmetry points in crystals**. Papers in this family classify phonons at the Brillouin‑zone centre (and often at other symmetry points) into irreducible representations of the crystal’s space group or point group, then determine their optical activity (Raman‑active, infrared‑active, acoustic, silent, etc.).

The outputs typically include:
- The **full vibrational representation** decomposed into irreps.
- **Mode counts** for each symmetry species.
- **Activity labels** (Raman/IR/silent) and polarisation vectors or Raman tensors.
- Sometimes **Clebsch–Gordan coefficients** or **symmetry‑adapted coordinates**.

## Common core computational pattern

1. **Identify the crystal structure and space group** (e.g., I4/mmm, P6₃/mmc, C₂v, …) and the high‑symmetry **k‑point** of interest (usually Γ).
2. **Represent the displacements**: build the mechanical (or vibrational) representation of the polar vector components acting on the set of atomic positions. This is often done via factor‑group (correlation) analysis or by direct product of the polar‑vector representation with the permutation representation of the Wyckoff positions.
3. **Decompose** the reducible representation into irreducible representations using character tables (space‑group or layer‑group irreps).
4. **Classify activity**: for each irrep, check whether the associated basis functions allow electric‑dipole transitions (IR activity) or symmetric second‑rank tensor components (Raman activity). Identify acoustic modes by their transformation as the polar vector.
5. **Verify numerically**: compare mode counts, degeneracies, and active‑mode numbers with known literature, experimental spectra, or standard databases (e.g., Bilbao Crystallographic Server).

Papers may extend this core with:
- **Kronecker‑product decompositions** and Clebsch–Gordan coefficients for selection rules.
- **Layer‑to‑bulk mapping** to handle polytypes or few‑layer systems.
- **Construction of symmetry‑adapted eigenvectors** or explicit displacement patterns.
- **Nonlinear normal mode (bush) analysis** that classifies invariant manifolds in anharmonic dynamics.

## Typical resources

- **Software tools**: Bilbao Crystallographic Server (LSITESYM, SITESYM), custom scripts for group‑theoretical decompositions.
- **Data sources**: Crystallographic data (space group, Wyckoff positions) from X‑ray diffraction or public databases; character tables from standard references (Kovalev, Bradley & Cracknell, CDML, etc.).
- **Validation references**: previously published irreducible‑representation decompositions, phonon databases, or experimental Raman/IR spectra.

*Note*: Each `paper‑*` subdirectory is a standalone Harbor task whose public entry point is `instruction.md`. The task description names the necessary input data and expected output files; the solving agent gathers the required resources accordingly.

## Verification style

This is a **numeric verification** workflow. The correctness of the decomposition is checked by:
- Comparing the **number of modes** in each irreducible representation against known results (from literature or the Bilbao server).
- Ensuring the **total degree‑of‑freedom count** exactly matches the atomic motion budget.
- Matching **activity classifications** (Raman‑active, IR‑active, silent) to experimental spectra or recognised tables.
- For advanced tasks (CGC or bushes), verifying that the **block‑diagonalisation** or **invariant‑manifold dimensions** agree with symmetry predictions.

Typical verification notes cite the use of standard databases (e.g., Bilbao) and tolerance consistency in numerical comparisons.
