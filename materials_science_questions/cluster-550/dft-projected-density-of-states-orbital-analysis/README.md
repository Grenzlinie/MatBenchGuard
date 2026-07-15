# DFT Projected Density of States Orbital Analysis

This workflow family computes total and projected density of states (DOS/PDOS) from density functional theory (DFT) electronic structure calculations to analyze the orbital character of valence and conduction band edges. The results provide insights into bonding, hybridization, and electronic properties of materials across condensed matter physics, materials science, and computational chemistry.

## Common Computational Pattern

1. **DFT electronic structure calculation**
   - Geometry optimization of the crystal structure using standard exchange‑correlation functionals (GGA, LDA, sometimes hybrid functionals).
   - Self‑consistent field (SCF) calculation to obtain the Kohn–Sham eigenstates and band energies.
   - Often includes spin‑polarization, spin‑orbit coupling, or Hubbard‑U corrections for transition‑metal or rare‑earth systems.

2. **Projected density of states (PDOS) calculation**
   - Projection of the Kohn–Sham wavefunctions onto atomic orbitals (s, p, d, f) at specific atomic sites.
   - Generation of site‑resolved and orbital‑resolved DOS that reveals the contributions of each species to the electronic states near the Fermi level.

3. **Orbital analysis**
   - Identification of the dominant orbital character (e.g., O 2p, Ti 3d, S 2p, Cu 3d) at the valence‑band maximum (VBM) and conduction‑band minimum (CBM).
   - Interpretation of bonding/antibonding character, hybridization, and correlation effects.

## Tools and Resources

The workflow is implemented in various DFT packages; the papers in this family commonly use:
- VASP (plane‑wave PAW)
- CASTEP (plane‑wave pseudopotential)
- Wien2k (full‑potential LAPW)
- FLAPW (full‑potential linearized augmented plane wave)
- LMTO (linear muffin‑tin orbital)
- Quantum ESPRESSO

No specific external datasets are required beyond the crystal structure and atomic coordinates; however, many studies compare the computed DOS/PDOS with experimental X‑ray photoelectron spectroscopy (XPS) or X‑ray absorption spectroscopy (XAS) data for verification.

## Verification

Verification is performed through **multimodal comparison**:
- **Computational**: The calculated DOS/PDOS and orbital assignments are compared to published theoretical results (band gaps, peak positions, orbital characters).
- **Experimental**: The computed PDOS is validated against XPS valence‑band spectra, XAS fine structure, or other spectroscopic data that probe the electronic structure. Agreement between theory and experiment confirms the accuracy of the orbital analysis.
- **Qualitative**: Trends across a family of compounds (e.g., changing B‑site cation in perovskites) are checked for consistency with chemical intuition and known properties.

## Task Organization

Each subdirectory `paper‑*` constitutes a standalone Harbor task. The public file `instruction.md` specifies the computational steps required to reproduce the PDOS analysis for a particular material or series of materials.
