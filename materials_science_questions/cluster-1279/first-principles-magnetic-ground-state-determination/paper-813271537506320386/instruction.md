# DFT study of small Gd_nO_3 clusters: ground-state structures, stabilities, and magnetic properties

## Problem background
Gadolinium oxide clusters are of great interest for applications in spintronics, optics, and biomedicine. Understanding how the ground-state geometries, relative stabilities, electronic structure (HOMO-LUMO gaps), and magnetic properties (total and local moments) evolve with cluster size is essential for rationalizing their behaviour. This task investigates small Gd_nO_3 clusters (n = 1–5) using first-principles density functional theory (DFT) with the generalized gradient approximation. The goal is to compute, from scratch, the key properties that characterize these clusters: the identity of the lowest-energy structure, its symmetry and average Gd–O bond length, the average binding energy per atom, the HOMO–LUMO gap, the total magnetic moment, the average local magnetic moments on Gd and O, and the relative energies of the next two most stable isomers for each size. Reproducing these quantities provides a benchmark for the predictive power of modern DFT approaches on f-electron oxide clusters.

## Approach
The reproduction is based on spin-polarized DFT calculations using the PW91 exchange-correlation functional and a double-zeta polarized basis set (or equivalent). For each cluster size n = 1–5, you must generate a chemically diverse set of candidate structures (varying atomic arrangements and magnetic orderings) and perform geometry relaxations without symmetry constraints. The calculations yield relaxed geometries, total energies, HOMO/LUMO energies, and spin densities. In addition, compute the total energies of isolated Gd and O atoms, which are needed to derive binding energies. From these raw results, extract for each n: (i) the ground-state symmetry and the average Gd–O bond length; (ii) the average binding energy per atom, defined as E_b = (E_cluster – n·E_Gd – 3·E_O)/(n+3); (iii) the HOMO–LUMO gap; (iv) the total magnetic moment; (v) the average local magnetic moments on Gd and O atoms; and (vi) the relative total energies of the two lowest-energy isomers lying above the ground state. All extracted data are compiled into a single JSON file (`results.json`) under `/app/outputs`.

## Reproduction target
Using spin-polarized DFT with the PW91 functional, compute the ground-state and low-lying isomers of Gd_nO_3 clusters for n = 1, 2, 3, 4, 5. For each cluster size, produce a `results.json` file that reports:
- Ground state: symmetry label, average Gd–O bond length (in nm), average binding energy per atom (in eV/atom), HOMO–LUMO gap (in eV), total magnetic moment (in μ_B), and average local magnetic moments on Gd and on O (in μ_B).
- Two lowest-lying isomers above the ground state: symmetry label and relative energy (in eV, total energy difference from the ground state).

All values must be derived from your own DFT runs; the task does not supply pre-existing geometries or energies. The scoring considers both the accuracy of the reported numbers and the internal consistency of the trends.

### Scientific context from the literature
Gd_nO_3 clusters (n = 1–5) have been systematically studied at the DFT-GGA level. Key findings from the literature that should inform your candidate-structure generation and property interpretation:

1. **Coordination preferences:** Gd atoms prefer three-coordination and O atoms prefer two-coordination. The ground-state structures are dominated by Gd–O bonds; Gd–Gd and O–O bonds are generally absent in the lowest-energy isomers. This preference arises from the atomic valence configurations (Gd: 5d¹ 6s², O: 2s² 2p⁴).

2. **Magnetic ordering:** Ferromagnetic ordering among Gd atoms is generally lower in energy than antiferromagnetic arrangements. The magnetic moments are predominantly carried by the Gd 4f electrons. The total magnetic moment increases monotonically with cluster size n. Local moments on O atoms are small (well below 1 μ_B in most sizes, except possibly for GdO₃ where they can be larger). The coupling between Gd and O sub-lattices is antiferromagnetic.

3. **Stability trends:** Gd₂O₃ and Gd₃O₃ are particularly stable, reflected in high average binding energies. The HOMO-LUMO gaps exhibit an even-odd oscillation with a global maximum at n = 2; Gd₂O₃ is the most chemically stable size.

## Assets

- Open-source DFT software (e.g., Quantum ESPRESSO, GPAW, ABINIT): https://www.quantum-espresso.org/
- Pseudopotentials for Gd and O (e.g., SSSP efficiency library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT calculations for clusters and atoms
- Role: process
- Action: Run spin-polarized DFT calculations using the PW91 functional and a double-zeta polarized basis set. For n=1 to 5, generate chemically diverse initial candidate geometries for Gd_nO_3 clusters (including different structural motifs and magnetic orderings) and perform geometry optimizations without symmetry constraints. Obtain relaxed structures, total energies, HOMO/LUMO energies, and spin densities. Also compute total energies of isolated Gd and O atoms to allow binding energy calculation.

### Step 2: Property extraction and compilation
- Role: scored (load-bearing)
- Action: From the DFT outputs, determine for each n the ground-state geometry (symmetry and average Gd-O bond length), average binding energy per atom (E_b = (E_cluster - n*E_Gd - 3*E_O)/(n+3)), HOMO-LUMO gap, total magnetic moment, and average local magnetic moments on Gd and O atoms. Also compute the relative energies (total energy difference, not per atom) of the two lowest-energy isomers above the ground state. Write all results to a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with key 'clusters': a list of objects, each with fields: 'n' (int), 'ground_state' (object with 'symmetry' string, 'avg_bond_length_nm' float, 'binding_energy_eV_per_atom' float, 'homo_lumo_gap_eV' float, 'total_magnetic_moment_muB' float, 'avg_Gd_moment_muB' float, 'avg_O_moment_muB' float), 'low_lying_isomers' (list of objects with 'symmetry' string, 'relative_energy_eV' float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Self-check before finishing (optional, not scored)

Before you finish, write and run a small script that checks every file under `/app/outputs` against the expected schema: results.json exists, contains a "clusters" array, and each cluster object has the required fields (n, ground_state with all required sub-fields, low_lying_isomers array). This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

## How you are scored
A hidden verifier reads your `results.json` and compares every quantity to reference values derived from the original study. Each property is scored independently with tolerances that account for legitimate toolchain differences. The final reward is a weighted sum of the following components:

- **Binding energies (30%)**: accuracy of per-atom binding energies for the ground states.
- **HOMO–LUMO gaps (15%)**: structural trends of the HOMO–LUMO gaps (global maximum at n=2, local peak at n=4, even-odd oscillation).
- **Magnetic moments (25%)**: monotonic increase and self-consistency of total magnetic moments (relationship between total moment and local Gd/O moments), and accuracy of average local moments on Gd and O.
- **Geometry (15%)**: correctness of symmetry labels and bond lengths.
- **Isomer relative energies (15%)**: accuracy of the relative total energies of the two lowest-lying isomers.

Additionally, the verifier checks structural trends (e.g., monotonic increase of total magnetic moment with n, relative ordering of binding energies, gap trends, expected ranges of local moments) and may penalise results that violate these expected trends even if some individual numbers are close. Reporting numbers directly from the literature without performing the DFT workflow will not pass because the verifier checks consistency across all outputs and with hidden reference data. Only properly computed DFT results can satisfy all checks simultaneously.