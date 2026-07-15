# DFT spin-state & electronic structure analysis of Fe complexes

## Overview

This workflow family contains computational studies of iron-containing molecular complexes using density functional theory (DFT) to determine ground-state spin, electronic configuration, geometric structure, and often to compare with experimental spectroscopic and structural data. The tasks are **dry-lab** (purely computational) and verified by comparing computed numerical metrics (energy differences, bond-length RMSD, spin densities, etc.) against experimental or literature reference values.

## Common Computational Pattern

Across the representative papers, the main workflow follows these steps:

1. **Model construction** – Build a molecular model of the iron complex, often starting from a SMILES string, X-ray coordinates, or known ligand set. Ligands may be truncated (e.g., porphyrin side chains replaced by hydrogens, cysteinate modelled as methylthiolate) to balance accuracy and cost.
2. **Method and basis selection** – Choose a DFT functional (B3LYP, BP86, TPSSh, etc.) and basis set (commonly LANL2DZ with effective core potential for iron, 6-31G* or def2-TZVP for light atoms). Some studies also use high-level wavefunction methods (CASSCF, CCSD(T)) for calibration or for multi-reference cases.
3. **Geometry optimization** – Perform spin-unrestricted DFT geometry optimizations for the candidate spin states (e.g., high-spin vs low-spin). Broken-symmetry approaches are used when antiferromagnetic coupling is relevant.
4. **Electronic structure analysis** – Compute properties such as:
   - Relative energies of different spin states to identify ground-state multiplicity.
   - Mulliken or natural population analysis spin densities.
   - Bond distances, angles, and dihedrals.
   - Mössbauer parameters (quadrupole splitting, isomer shift) via electric field gradient calculations.
   - Magnetic exchange couplings (from broken-symmetry energies) and zero-field splitting parameters.
   - Bond dissociation energies, vertical excitation energies (TD-DFT) for UV-Vis spectra, and vibrational frequencies.
5. **Numeric verification** – Compare the computed observables with experimental data (crystallographic bond lengths, Mössbauer spectra, magnetic moments, redox potentials, etc.) using tolerances appropriate for the method (e.g., energy differences within a few kcal/mol, bond lengths within ~0.01 Å). The verification note states: “通过比较能量差、键长RMSD和自旋密度等数值指标与实验或文献值的容差对齐来验证。”

## Data, Models, and Tools

Based on the represented papers, the following categories of resources are commonly employed:

- **Molecular systems**  
  - Iron porphyrins (heme models) and related macrocycles.  
  - Bis(arene), cyclopentadienyl, and carbonyl complexes.  
  - Iron‑sulfur clusters (cubanes, [2Fe], [4Fe‑4S]).  
  - Di‑ and polynuclear Fe complexes with bridging ligands (oxo, carboxylate, cyanide, triazole).  
  - Zeolite‑embedded Fe species (Fe/ZSM‑5).  
  - Metallo‑organic frameworks and tape‑porphyrins.  
  - Dinitrosyl iron complexes (DNICs).  
  - Carbene complexes ((CO)₄FeCF₂).  
  - Metal‑metal dimers (Fe₂, FeCo, etc.).  
  - Pincer ligand complexes (terpyridine analogues).  
  - Hydroperoxo‑iron(III) intermediates.  

- **DFT programs** – Gaussian, Jaguar, VASP, NWChem, Q‑CHEM, DGAUSS, OPEC.  

- **Basis sets**  
  - Fe: LANL2DZ (with ECP), Ahlrichs VTZ, Wachters basis, etc.  
  - Light atoms: 6‑31G*, 6‑311+G(d), def2‑TZVP, cc‑pVTZ, 6‑31G**.  

- **Functionals** – B3LYP, BP86, TPSS, TPSSh, M06‑2X, B2PLYP, OPBE, etc. (hybrid, GGA, meta‑GGA, double‑hybrid).  

- **Post‑Hartree‑Fock methods** – CASSCF/NEVPT2, CCSD(T) (used for calibration of challenging spin‑state gaps or bond energies).  

- **Analysis toolkits** – Mulliken, Natural Bond Orbital (NBO), Atoms‑in‑Molecules (AIM/Bader), Mayer bond orders, QTAIM.  

- **Spectroscopic predictions** – TD‑DFT for absorption spectra, electric field gradient calculations for Mössbauer, vibrational analysis for IR/Raman/NRVS.  

## Typical Verification Style

Verification is **numeric**: a task is considered successful when the computed energies (spin‑state gaps, bond dissociation energies, reaction energies), key bond distances, spin densities, and/or Mössbauer parameters fall within pre‑defined tolerances of experimental or literature reference data. The tasks are pure computational exercises; no experimental execution is required. The lab‑type is dry because the workflow relies solely on DFT calculations and data analysis and can be reproduced without any real‑world experiment.

## Harbor Task Structure

Each `paper‑*` subdirectory is a standalone Harbor task. Its public entry point is `instruction.md` (not `TASK.md`), which describes:

- The target iron complex (by name, formula, or structural scaffold).
- The specific objective (e.g., optimize geometry, determine ground spin state, compute Mössbauer quadrupole splitting, calculate Fe–ligand bond dissociation energy).
- The expected level of theory (functional, basis set) either as a requirement or as a suggestion to reproduce a particular published result.
- The expected numeric outputs and the tolerance applied for verification.

The solving agent reads `instruction.md`, performs the calculations, and returns the results for numeric comparison.

## Representative Applications

- Determination of ground‑state spin and electronic configuration of Fe(II)/Fe(III) porphyrin systems, with Mössbauer parameter prediction.
- Investigation of spin‑crossover behaviour in Fe(II) pincer complexes and triazole polymers.
- Computation of magnetic exchange coupling constants in iron‑sulfur and oxo‑centred clusters (broken‑symmetry DFT).
- Modeling oxygen activation and Fe–O bond energies in cytochrome P450 and methane monooxygenase mimics.
- Analysis of nitrosyl/dinitrosyl iron complex spin states and redox properties.
- Ligand‑field theory augmented with DFT for d‑d transitions and zero‑field splitting of Fe³⁺ in crystals.
- Prediction of reaction pathways and spin‑forbidden processes (e.g., CO recombination, O₂ binding) using coupled‑cluster and CASPT2 calibration.

This README is intended to guide both human users and automated agents in understanding the scope, computational pattern, and verification strategy of the workflow family, enabling consistent and reproducible execution of the tasks.
