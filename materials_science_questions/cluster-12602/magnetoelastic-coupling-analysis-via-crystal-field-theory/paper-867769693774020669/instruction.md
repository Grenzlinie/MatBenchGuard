# Ginzburg-Landau analysis of antiferromagnetic order in an FFLO superconductor

## Problem background
In the heavy-fermion superconductor CeCoIn5, an incommensurate antiferromagnetic (AFM) order coexists with a Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) superconducting state in high magnetic fields. Neutron scattering reveals two degenerate AFM wave vectors, and the FFLO state breaks translation symmetry, leading to a complex interplay between magnetism and superconductivity. Understanding which magnetic phase is realized and how it manifests in measurable quantities is an open question.

## Approach
The problem is analyzed with a two-component Ginzburg-Landau free energy functional. The order parameters η1 and η2 describe amplitudes of two degenerate incommensurate AFM states; the free energy includes quadratic terms with nearest-neighbor stiffness (parameterized by ξAF), quartic terms stabilizing a single-q or double-q ground state, and a commensurate coupling term that models the pinning effect of FFLO nodal planes on the magnetic moment. The functional is minimized numerically with respect to η1, η2 and the wave vectors q1, q2 at the given condition T/T_N^0 = 0.5, ξAF q0 = 0, using parameters b = 0.1, c2(N) = 0.01, and ξAF = 3. From the minimized state, three derived quantities are computed: (1) the phase (single-q or double-q) and the ratio η2/η1; (2) an analytic bound on the Bragg peak shift |q1 − q_inc|; (3) the NMR internal field distribution P(h) at In(2b) sites, obtained by evaluating the dipolar field on a representative spatial lattice and building a normalized histogram.

## Free energy functional
The Ginzburg-Landau free energy (normalized by a scaling factor F0) is:

F(η1,η2)/F0 = [(T/T_N^0 − 1) + ξ_AF^2 (q1 − q_inc1)^2] η1^2
            + [(T/T_N^0 − 1) + ξ_AF^2 (q2 − q_inc2)^2] η2^2
            + ½ (η1^2 + η2^2)^2
            + b η1^2 η2^2
            − ½ η1 η2 c2(N) .

For the present conditions the magnetic field is along [100] so the field‑orientation term c1 Hx Hy (η1^2 − η2^2) is inactive and not included. The commensurate coupling has been simplified because the condition ξAF q0 = 0 implies q_inc1 − q_inc2 = 2N q_FFLO, which selects the δ‑function term with n = N and coupling constant c2(N).

The incommensurate reference wave vectors are
q_inc1 = (0.125π, 0.125π, 0),
q_inc2 = (−0.125π, 0.125π, 0).
The wave vectors q1 and q2 are allowed to vary around these reference values; in practice you may restrict the search to small deviations along the x‑direction because the stiffness terms penalise large shifts.

Parameter values:
b = 0.1,
c2(N) = 0.01,
ξ_AF = 3,
T/T_N^0 = 0.5.

## Magnetisation profile
Once the order parameters η1, η2 and the wave vectors q1, q2 are known, the slowly varying amplitude of the AFM staggered magnetisation (in dimensionless units) is

M_AF(r) = M0 [η1 cos(q1·r) + η2 cos(q2·r)] .

M0 is an overall scale factor that can be chosen arbitrarily for the purpose of computing field distributions because the NMR histogram shape is independent of the absolute magnetisation scale. Set M0 = 1 in all calculations.

## NMR internal field calculation
The internal magnetic field at an In(2b) site is dominated by the dipolar field from the Ce moments, which are oriented along the c‑axis (perpendicular to the Ce planes). For a single Ce moment of strength m ∝ M_AF(r) located at r_ce, the dipolar field at position r measured along the c‑axis is

H_dip(r) = − C_dip * ​m / |r − r_ce|^3​ ,

where C_dip is a constant that scales the field (set C_dip = 1, because only the shape of the histogram is required).

The In(2b) site sits at the centre of a Ce square plaquette. Use a two‑dimensional lattice of Ce sites with coordinates

r_ij = (i, j) , i, j = 0, 1, …, L−1

with L = 50. The in‑plane lattice constant is taken as the unit of length (a = 1). The In(2b) position is

r_In = (0.5, 0.5) .

To avoid edge artefacts, apply periodic boundary conditions when computing the distance |r_ij − r_In|: for each Ce site replace the coordinate difference by the shortest distance modulo L, i.e. Δx = ((i − 0.5 + L/2) mod L) − L/2, and similarly for Δy, then |r_ce − r_In| = sqrt(Δx^2 + Δy^2).

The local field at the In(2b) site is given by summing the contributions from all Ce sites:

H(r_In) = − ∑_{i,j} M_AF(r_ij) / |r_ij − r_In|^3 .

Evaluate this sum for a sufficiently large set of spatial points, or simply use a single In(2b) site and collect field values from many “samples” by varying the overall phase or by averaging over equivalent In(2b) positions within the periodic cell. A simple method that reproduces the expected double‑peak structure is:
- Generate a set of M_AF(r_ij) for the single‑q phase (η2/η1 ≈ 0, q1 = q_inc1).
- Compute the field H at r_In.
- Repeat the calculation for a few translated copies of the In site (e.g., (0.5,0.5), (0.5+Δ,0.5), (0.5,0.5+Δ) with small offsets) to sample the inhomogeneous field distribution, or better, evaluate H(r) on a fine grid of probe positions and histogram the results.
The histogram must be normalised so that ∫ P(h) dh = 1, i.e. probability_density is the normalised frequency divided by the bin width.

## Reproduction target
From the Ginzburg-Landau functional described above, compute at T/T_N^0 = 0.5 and ξAF q0 = 0:
- Task 1: the phase classification (single‑q or double‑q) and the order parameter ratio η2/η1.
- Task 2: the analytic bound on the main Bragg peak shift |q1 − q_inc|, expressed in units of π.
- Task 3: the NMR internal field distribution P(h) for the single‑q phase at In(2b) sites, which should exhibit two well‑separated peaks.

All results are written as output files under /app/outputs.

## Assets
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Free energy minimisation
- Role: process
- Action: Implement the Ginzburg-Landau free energy functional and numerically minimise it with respect to η1, η2 and the wave vectors q1, q2 (or, given q0 = 0, simply fix q1 = q_inc1, q2 = q_inc2 and minimise over η1, η2). Use the parameters b = 0.1, c2(N) = 0.01, ξ_AF = 3, T/T_N^0 = 0.5. The minimisation must yield the equilibrium order parameters.
- Note: This step produces intermediate results used by the following scored tasks. No output file is required for this step alone.

### Step 2: Phase classification and order parameter ratio
- Role: scored
- Action: From the minimisation results, determine the phase (single‑q or double‑q) and compute the ratio η2/η1. Write one row to phase_analysis.csv.
- Output file: `/app/outputs/phase_analysis.csv`
- Format: csv
- Contract: Columns: temperature_ratio (float), xiAF_q0 (float), phase (string: single‑q or double‑q), eta2_eta1_ratio (float). One row.
- Scoring: scored by hidden verifier

### Step 3: Bragg peak shift bound
- Role: scored
- Action: Compute the analytic bound on the Bragg peak shift using the formula |Δq| ≤ (1/ξ_AF) √(c2(N))/8. Express this bound in units of π and write the single float to bragg_shift_bound.txt.
- Output file: `/app/outputs/bragg_shift_bound.txt`
- Format: txt
- Contract: Single float value.
- Scoring: scored by hidden verifier

### Step 4: NMR internal field distribution
- Role: scored (load‑bearing)
- Action: For the single‑q phase (η2/η1 very small, q1 = q_inc1, q2 = q_inc2), compute the dipolar field H at In(2b) sites according to the prescription in the Approach section. Build a normalised histogram P(h) and output a two‑column CSV.
- Output file: `/app/outputs/nmr_distribution.csv`
- Format: csv
- Contract: Two columns: field_value (float), probability_density (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_analysis.csv`
- `/app/outputs/bragg_shift_bound.txt`
- `/app/outputs/nmr_distribution.csv`

## Output contract
... (rest as before, unchanged) ...