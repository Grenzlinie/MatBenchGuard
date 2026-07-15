# DFT Investigation of Surface Reactions and Adsorption on Alumina

## Overview
This workflow family uses density functional theory (DFT) to model chemical reactions and adsorption on alumina surfaces and related oxide materials. The tasks span a wide range of computational chemistry studies in surface science, materials science, and catalysis, focusing on adsorption energetics, reaction mechanisms, transition-state structures, and electronic properties. The family includes 109 workflow instances derived from 73 published papers, all of which are dry-lab (purely computational) and verified through numeric comparison of computed quantities (adsorption energies, activation barriers, etc.) with literature or experimental values.

## Common Computational Pattern

While individual papers may employ different methodological details, a typical workflow in this family follows these steps:

1. **Surface model construction** – Build a representative model of the alumina (or related oxide) surface, most often a periodic slab or a finite cluster. The model may include surface hydroxyl groups, oxygen vacancies, dopants, or supported metal clusters as needed.
2. **Adsorption geometry optimization** – Place the adsorbate molecule at relevant sites and perform a structural relaxation using DFT to locate one or more stable adsorption minima.
3. **Transition-state search** – For reaction steps, locate saddle points using methods such as the climbing-image nudged elastic band (CI-NEB) or dimer algorithm, ensuring the nature of the stationary point via vibrational frequency analysis.
4. **Energetic evaluation** – Calculate adsorption energies, activation barriers, and reaction energies using the chosen electronic structure method, often with zero-point energy and thermal corrections.
5. **Electronic structure analysis** – Perform charge analysis (Mulliken, Bader, NBO), density-of-states, or molecular orbital visualization to characterize the nature of bonding and the reaction mechanism.

Optional extensions include microkinetic modeling, bond-order conservation Morse-potential (BOC-MP) analysis, or force-field corrections for dispersion interactions.

## Typical Computational Resources

The tasks rely on a variety of quantum chemistry codes and models. Common examples (as seen in the selected papers) include:
- **Codes:** Gaussian-03/16, VASP, ORCA
- **Functionals:** PBE, PW91, B3LYP (often with dispersion corrections such as D3 or D)
- **Basis sets:** Pople-style basis sets (6-31G*, 6-31+G(d), etc.), plane-wave basis with PAW pseudopotentials
- **Surface models:** Periodic slabs (e.g., γ-Al₂O₃(110), (100)), finite clusters (3T, 4T, 46T zeolite models; Al(OH)H₂; Ga₁₄O₂₁), and supported metal clusters (e.g., Cu₄/γ-Al₂O₃)

Note that every paper-* subdirectory contains a self-contained Harbor task with a detailed `instruction.md` file that specifies the exact model, method, target quantities, and verification criteria. The task does not require the solver to pre-package code or models; instructions describe the required resources.

## Verification Style
This workflow family uses **numeric verification**. The expected quantities (adsorption energies, activation barriers, bond lengths, etc.) are compared against reference values from the paper or established literature. A task is considered correctly solved when the computed numbers fall within the tolerance specified in the instruction.

## Workflow Structure
Each paper from the cluster is mapped to a separate subdirectory (e.g., `paper-811047913265299457/`). Inside that directory:
- `instruction.md` – the public task specification that describes the computational experiment, required resources, and expected outputs.
- Other supporting files (geometry inputs, parameter details) may be provided by the solving agent based on the instruction.

This family covers a broad spectrum of alumina‑related surface chemistry, making it a valuable benchmark for computational surface science workflows.
