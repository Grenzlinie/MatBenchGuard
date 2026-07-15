# A simple local expression for the prefactor in transition state theory

Cite as: J. Chem. Phys. 150, 144105 (2019); https://doi.org/10.1063/1.5086746
Submitted: 22 December 2018 . Accepted: 19 March 2019 . Published Online: 08 April 2019

S. Kadkhodaei, and A. van de Walle

![](./images/812786606523023361_1.jpg)
![](./images/812786606523023361_2.jpg)
![](./images/812786606523023361_3.jpg)

## ARTICLES YOU MAY BE INTERESTED IN

### Microscopic calculation of absorption spectra of macromolecules: An analytic approach
The Journal of Chemical Physics 150, 144103 (2019); https://doi.org/10.1063/1.5084120

### Boundary conditions derived from a microscopic theory of hydrodynamics near solids
The Journal of Chemical Physics 150, 144104 (2019); https://doi.org/10.1063/1.5088354

### Sparse non-orthogonal wave function expansions from the extension of the generalized Pauli constraints to the two-electron reduced density matrix
The Journal of Chemical Physics 150, 144102 (2019); https://doi.org/10.1063/1.5085056

![](./images/812786606523023361_4.jpg)

J. Chem. Phys. 150, 144105 (2019); https://doi.org/10.1063/1.5086746
150, 144105

© 2019 Author(s).

# A simple local expression for the prefactor in transition state theory

Cite as: J. Chem. Phys. 150, 144105 (2019); doi: 10.1063/1.5086746
Submitted: 22 December 2018 · Accepted: 19 March 2019 ·
Published Online: 8 April 2019

![](./images/812786606523023361_5.jpg) ![](./images/812786606523023361_6.jpg) ![](./images/812786606523023361_7.jpg)

S. Kadkhodaei⁽ᵃ⁾ and A. van de Walle

## AFFILIATIONS
School of Engineering, Brown University, Providence, Rhode Island 02912, USA

⁽ᵃ⁾Also at: Civil and Materials Engineering, University of Illinois, Chicago, Illinois 60607-7023, USA.
Electronic mail: sara_kadkhodaei@brown.edu.

## ABSTRACT
We present a simple and accurate computational technique to determine the frequency prefactor in harmonic transition state theory without necessitating full phonon density of states (DOS) calculations. The atoms in the system are partitioned into an "active region," where the kinetic process takes place, and an "environment" surrounding the active region. It is shown that the prefactor can be obtained by a partial phonon DOS calculation of the active region with a simple correction term accounting for the environment, under reasonable assumptions regarding atomic interactions. Convergence with respect to the size of the active region is investigated for different systems, as well as the reduction in computational costs when compared to full phonon DOS calculation. Additionally, we provide an open source implementation of the algorithm that can be added as an extension to Large-scale Atomic/Molecular Massively Parallel Simulator software.

Published under license by AIP Publishing. https://doi.org/10.1063/1.5086746

## I. INTRODUCTION

Kinetic processes play a major role in structure formation, microstructure development, and materials properties, and diffusion is the underlying phenomenon in many of kinetic processes. The significant progress of atomic level simulations based on first-principles approaches and empirical interatomic potentials paved the way towards determining diffusivities by the use of computer simulations. Additionally, atomic level simulations provide fundamental insight into the atomic mechanisms in diffusion processes, and without relying on fitting to experimental data, they have predictive power for tuning of diffusion rate properties.

A number of previous studies have used electronic structure calculations, model potential, or a combination of both to obtain the diffusion coefficient from atomic level simulations. In general, interstitial or point defect jump frequency, which is the dominating mechanics for diffusion in most elemental crystals, is expressed by the equation

$$
\Gamma = \nu^{*} \exp\left(\frac{-\Delta E}{k_B T}\right), \tag{1}
$$

where $k_B$ is Boltzmann's constant, $T$ is temperature, $\Delta E$ represents the potential energy change needed to carry a defect from an initial equilibrium position to a transition state, and $\nu^{*}$ is the effective frequency associated with the vibration of the defect along the transition path. The atomic migration energy barrier calculation is more straightforward and can be obtained by using static total energy calculations. On the other hand, calculating the jump frequency needs more effort and depends on the change in the entropy associated with lattice vibration ($\Delta S$), which is due to the constriction or expansion of the diffusing atom's path during diffusion. One approach is to evaluate the diffusion rate directly from an analysis of the mean squared displacement of the diffusing atom during a molecular dynamics simulation.¹² While this method can deliver the pre-exponential factor in Eq. (1), it is only practical at temperatures close to the melting point. Otherwise, the diffusion events are too rare to be observed in the molecular dynamics simulation. Milman *et al.* combined *ab initio* molecular dynamics and thermodynamic integration to obtain the diffusion entropy change ($\Delta S$) for interstitial diffusion in silicon.³ Other studies⁴⁻⁷ used the harmonic approximation within the transition state theory (TST) and expressed the effective jump frequency as the ratio of the product of normal

vibration frequencies of the initial state of atomic migration to that of the non-imaginary normal frequencies of the transition state⁸

$$
v^{*}=\frac{\prod_{i=1}^{3 N} v_{i}^{B}}{\prod_{i=2}^{3 N} v_{i}^{A}}, \tag{2}
$$

where $v_{i}^{B}$ and $v_{i}^{A}$ are the normal vibrational frequencies (with $v_{1}^{A}$ denoting the omitted imaginary frequency associated with the unstable mode) in the initial basin and in the activated state, respectively, for a system of $N$ atoms. (This expression assumes that the center of mass of the system is held by a fictitious spring. This has the effect of assigning a fixed stiffness to the rigid translation modes whose associated frequencies are then the same in the basin and in the activated states, and thus, cancel out in the prefactor expression.)

The common approach to calculate the normal vibrational frequencies in Eq. (2) has been the use of direct force-constant calculation,⁹ where the computation cost scales cubically with the number of atoms in the system. This fact limited the previous atomic level simulations of lattice diffusion in solids based on first-principles calculations to system with at most a hundred of atoms,⁴⁻⁷ which make it difficult to study more complex processes, such as grain boundary diffusion. Relying only on empirical potential models in order to investigate diffusion processes in larger system (thousands of atoms) may not always be a viable alternative, due to complex multi-body bonding behavior. Deploying semi-empirical interatomic potential models by fitting to zero-temperature ab initio data has been performed by Mendelev and Mishin,² but it requires the task of developing a potential model for various systems. Huang et al.¹⁰ developed an ingeniously linearly scalable approach by approximating the phonon density of states (DOS) by the kernel polynomial method as an expansion in terms of Chebyshev polynomials to reduce the computational cost of the direct force-constant method.

Here, we use an approach that facilitates transition rate calculations in large-scale systems by replacing the computation and diagonalization of the Hessian of the whole system by the formally equivalent calculation of a much smaller local effective Hessian. For this purpose, we assume that the entire system of atoms can be partitioned into an "active region," where the kinetic process takes place, and an "environment" surrounding the active region, whose elastic behavior is independent of the atomic geometry of the active region. Our approach is perhaps most related, in its mathematical formalism, to the one of Ref. 11, although their primary aim is to handle coarse-grained systems rather than fully atomistic simulations. Therefore, our approach entails different methods for calculating the various input quantities needed for the rate calculations.

In this paper, we benchmark this local force-constant approach by applying it to a number of different kinetic processes using realistic energy models [ab initio Hamiltonian, reactive force field (ReaxFF), or embedded atom (EAM) potentials]: self-diffusion in bulk elemental phases of silver and aluminum, lithium interstitial diffusion in diamond cubic phase of silicon, and oxygen adsorbate surface diffusion on Pt(111) slab.

## II. THEORY

The partitioning of the system into an "active region"and an "environment" (see Fig. 1) implies that the system's Hessian (after suitable re-ordering of the atoms) can be partitioned in block form as well

$$
H^{A}=\left[\begin{array}{cc}
A & C^{T} \\
C & E
\end{array}\right] \text { and } H^{B}=\left[\begin{array}{cc}
B & D^{T} \\
D & E
\end{array}\right], \tag{3}
$$

where $H^{A}$ and $H^{B}$ denote the Hessian in the activated state and in a stable basin, respectively. The block $A$ and $B$ denote the respective Hessians of the active region while block $E$ is the Hessian of the atoms in the environment, assumed to be independent of the configuration in the active region. The $C$ and $D$ blocks represent the coupling between these two regions and can differ in the basin and activated state.

As noted in earlier work,¹¹ a standard block-matrix determinant identity implies that

$$
\begin{aligned}
\operatorname{det} H^{A} & =\operatorname{det}\left(A-C^{T} E^{-1} C\right) \operatorname{det}(E), \\
\operatorname{det} H^{B} & =\operatorname{det}\left(B-D^{T} E^{-1} D\right) \operatorname{det}(E)
\end{aligned}
$$

(a result shown in the Appendix for completeness). After introducing the mass matrix $M$, we can then write the prefactor as

![](./images/812786606523023361_8.jpg)

FIG. 1. (a) Partitioning the atoms in a system into an "active region," where the kinetic process takes place, and an "environment" surrounding the active region. (b) In the "relaxed environment" approach, the atoms in the environment are relaxed during force-constant calculation of active region atoms. (c) In the "fixed environment" approach, no special treatment of environment atoms is conducted during the force-constant calculation of active region atoms.

$$
\begin{aligned}
v^{*} & =v_{1}^{A} \frac{\prod_{i=1}^{3 N} v_{i}^{B}}{\prod_{i=1}^{3 N} v_{i}^{A}}=v_{1}^{A}\left(\frac{\operatorname{det}\left(M^{-1 / 2} H^{B} M^{-1 / 2}\right)}{\operatorname{det}\left(M^{-1 / 2} H^{A} M^{-1 / 2}\right)}\right)^{1 / 2} \\
& =\left(\left(v_{1}^{A}\right)^{2} \frac{\operatorname{det}\left(H^{B}\right)}{\operatorname{det}\left(H^{A}\right)}\right)^{1 / 2}=\left(\left(v_{1}^{A}\right)^{2} \frac{\operatorname{det}\left(B-D^{T} E^{-1} D\right)}{\operatorname{det}\left(A-C^{T} E^{-1} C\right)}\right)^{1 / 2},
\end{aligned}
$$

where $v_{1}^{A}$ is the imaginary frequency associated with the unstable mode in the activated state. Terms of the form $B-D^{T} E^{-1} D$ and $A-C^{T} E^{-1} C$ can be interpreted as the local effective Hessian of the active region, calculated while allowing the atoms in the environment to relax until they experience no force (rather than being held fixed). These steps closely follow earlier work, $^{11}$ except for the specific way the terms $\left(v_{1}^{A}\right)^{2}, D^{T} E^{-1} D$, and $C^{T} E^{-1} C$ will be computed in what follows.

In Ref. 11, the authors seek to obtain a coarse-grained description of the system in which the environment is removed but accounted for via a correction term $-D^{T} E^{-1} D$, which is computed once and then kept fixed throughout the simulation (thus, requiring $C=D$ ). They also aim to approximate $\left(v_{1}^{A}\right)^{2}$ only using the coarsegrained representation of the system. In contrast, we do not seek to entirely remove the atoms of the environment, which offers two advantages. First, it allows us to circumvent the requirement that $\left(v_{1}^{A}\right)^{2}$ be well-approximated in a coarse-grained system. Instead, we simply obtain $\left(v_{1}^{A}\right)^{2}$ from

$$
\left(v_{1}^{A}\right)^{2}=\min _{\|u\|=1} u^{T} M^{-1 / 2} \tilde{H}^{A} M^{-1 / 2} u=\min _{\left\|M^{1 / 2} v\right\|=1} v^{T} \tilde{H}^{A} v,
$$

a quantity that is closely related to what is already needed to find the saddle point via, say, the Nudged Elastic Band ${ }^{12-14}$ or the dimer $^{15}$ method, again without requiring the calculation of the full Hessian.

A second advantage is to allow us to relax the constraint $C=D$. Relaxing this constraint does not take significantly more computational time because one can use the relaxed environment geometry obtained in the calculation of, say, $H^{B}$ as the starting point for the calculation of $H^{A}$. In a system where $C=D$ is a good approximation, the second calculation will converge much faster.

The approach of Ref. 11 is most useful when the same partitioning between the active region and the environment can be used for all the transitions of interest while ours is most useful when the transition events can occur anywhere in the system so that the partitioning must be transition-dependent.

In Secs. III and IV, we show that the prefactor rates obtained by the above approach agree well with direct force-constant (full Hessian) calculation results, even for small sizes of the active region. Therefore, the use of the aforementioned approach significantly reduces the computation cost by limiting the number of degrees of freedom in force-constant calculations, while delivering accurate results comparable to direct force-constant calculation results. The additional cost of relaxing the atoms in the environment is much less that the burden of full Hessian calculations thanks to the high efficiency of modern conjugate gradient methods in high dimensions. Additionally, the cubically scaling cost of diagonalization of force-constant, which is the computational bottleneck in interatomic potential models, is significantly reduced by narrowing force-constant calculations efforts to atoms in the small active region.

## III. COMPUTATIONAL DETAILS

To test the applicability of the local force-constant method, we employ first-principles calculations in the framework of density functional theory (DFT) for vacancy hopping in bulk aluminum, for which there exist previous $a b$ initio calculations. $^{6}$ However, the finite size effects cannot be excluded in the system sizes that are computationally accessible via DFT, i.e., at most tens of atoms. Therefore, we test the applicability of the model to systems with thousands of atoms by employing interatomic potential models for vacancy hopping in bulk silver, lithium diffusion in diamond cubic silicon, and oxygen surface diffusion on $\mathrm{Pt}(111)$ slab. To this end, we have implemented a C++ module in the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) framework to add the functionality of local force-constant calculations for any interatomic potential. The source code of this module is open access and is available on the web. $^{16}$ To invoke this new functionality, one has to simply put our C++ module code in the LAMMPS src directory and re-build it according to the LAMMPS website instructions. $^{17}$

For our first-principles calculations, we used the projector augmented wave (PAW) method, ${ }^{18,19}$ as implemented in highly efficient Vienna $A b$ initio Simulation Package (VASP), ${ }^{20-23}$ with energy cutoff of $300 \mathrm{eV}$. The generalized gradient approximation (GGA) $)^{24}$ is used for exchange-correlation functional. The Brillouin zone integration is performed using a Monkhorst-Pack $k$-mesh of $11 \times 11 \times 11$ for a 31-supercell of fcc aluminum. Tests indicate that this choice of first-principles calculation parameters ensures an energy accuracy of $0.1 \mathrm{meV} /$ atom.

For our interatomic potential calculations, we use an embedded atom (EAM) potential taken from Ref. 25 to describe atomic interactions for silver and a reactive force field (ReaxFF) with parameters taken from Ref. 26 to describe interatomic interactions of lithium and silicon. For the ReaxFF potential, we use the parameters derived in Ref. 26, where they are optimized against a DFT training set consisting of bulk c- $\mathrm{Li}_{x} \mathrm{Si}$ and a- $\mathrm{Li}_{x} \mathrm{Si}$ phases. A ReaxFF potential with optimized parameters to describe Pt-O system, taken from Ref. 27, is used for oxygen diffusion on $\mathrm{Pt}(111)$ surface.

The number of atoms in our examples are limited to a couple of thousands atoms for the purpose of comparing our results against the direct force-constant calculation results, while the usage of our method is most advantageous where the number of atoms are in the order of millions and direct force-constant calculations are infeasible.

## IV. RESULTS

### A. Vacancy diffusion

We first demonstrate the local force-constant method by computing the effective jump frequency (pre-exponential factor), $v^{*}$, for vacancy hopping in bulk aluminum using DFT calculations. The minimum and saddle point configurations are obtained using the nudged elastic band method as implemented in VASP. ${ }^{12,13}$ The energy barrier we obtained is 0.52 , and when a correction value of 0.05 for the "internal surface" effect $^{28}$ is added to it, the final value

![](./images/812786606523023361_9.jpg)

FIG. 2. Vacancy diffusion energy profile (DFT calculation) and the initial and saddle point configurations obtained using the nudged elastic band method. The vacancy is represented by a small sphere with different color than other atoms in the unit cell of fcc Al. The vacancy migrates from its initial position at $[\frac{a}{2},0,\frac{a}{2}]$ along the saddle point configuration to the final position on [0 0 0], where a is the lattice constant and equals $4.09\ \mathring{A}$ in our calculations. In other words, the atom positioned at [0 0 0] in the initial composition migrates to $[\frac{a}{2},0,\frac{a}{2}]$ position, passing through saddle point configuration. Only atoms in fcc unit cell are represented for the purpose of clarity.

of 0.57 eV is in agreement with the vacancy migration energy of 0.57 eV reported in Ref. 6. Figure 2 represents the vacancy migration and its energy profile in fcc aluminum. The atomic configurations are visualized using the Visualization of Electronic and STructural Analysis (VESTA) software. $^{29}$ Having the minimum and saddle point configurations, we calculated the prefactor for different number of atoms in the active region employing the proposed method, as illustrated in Fig. 3. Active region is defined as a sphere originated at the position of migrating atom in the saddle point configuration, as visualized by the Open Visualization Tool (OVITO) software $^{30}$ and represented in Fig. 3. A linear increase in the radius of the active region results in a cubic increase in the number of atoms inside the active region. As shown in Fig. 3, our results are compared with a crude local approximation of force-constant,

![](./images/812786606523023361_10.jpg)

FIG. 3. (a) Effective jump frequency of vacancy hopping in aluminum obtained by a partial Hessian calculation using DFT. The x-axis indicates the number of atoms included in the active region, which is a sphere originated at the position of migrating atom in the saddle point configuration. The blue squares are the prefactor values obtained by our method, where the atoms in the environment are relaxed during the force constant calculation. The red triangles are the prefactor rates obtained by a crude local force-constant calculation, where the atoms in the environment are fixed. The prefactor value reported in Ref. 6 using the full Hessian calculation is represented by a black diamond. (b) Minimum and saddle point configurations in a $2\times2\times2$ supercell of fcc Al. The active region is indicated as a sphere that encompasses atoms that are included in the force-constant calculations.

where the effect of atoms in the environment is not accounted for. In other words, in this crude approximation the force-constant calculation is conducted for atoms in the active region, while other atoms in the system are fixed. We call this approach the "fixed environment" method, as compared to the proposed method of "relaxed environment." The results of the "relaxed environment" method indicate a better convergence compared to the "fixed environment" local force-constant calculation. The calculated prefactor value considering all atoms in the active region is are in perfect agreement with the value reported in Ref. 6 that is obtained using the direct force-constant calculation.

Next, we demonstrate our method by computing the effective jump frequency for vacancy hopping in a larger system, a $7 \times 7 \times 7$ supercell of the conventional cubic cell of fcc silver with a vacancy consisting of 1371 atoms, using the EAM potential model. We used nudged elastic band method, as implemented in LAMMPS $^{31,32}$ to obtain the minimum and transition state configurations. The initial and saddle point configurations for vacancy diffusion in Ag are visualized using VESTA software $^{29}$ and are illustrated in Fig. 4. The energy barrier obtained from our calculations is 0.66 eV, in good agreement with the value of 0.65 eV reported in Ref. 10. As presented in Fig. 4, we calculated the prefactor rate using our method of local force-constant calculation, where the atoms in the environment are relaxed during force-constant calculation of active region atoms. We compared our method with the case of fixing atoms in the environment during force-constant calculations. This comparison indicates that the "fixed environment" approach results happen, in this case, to converge faster due to fortuitous cancellation of errors. As discussed in the supplementary material, while the partial Hessian calculated in the "fixed environment" approach [A and $B$ in Eq. (3)] does not include the effect of atoms in environment, the ratio of partial Hessian determinants $(\frac{\operatorname{det}(B)}{\operatorname{det}(A)})$ happens to be in a good agreement with effective Hessian determinants ratio $(\frac{\operatorname{det}(H^{B})}{\operatorname{det}(H^{A})})$ (see the supplementary material for a detailed discussion). This case is rather exceptional, however, and the remaining examples we consider below indicate that "relaxed environment" approach more typically performs better. As shown in Fig. 4, even for small sizes of active region, the error magnitude is still fairly small (less than a factor 2), which is typically smaller than errors arising from other sources (such the use of empirical potential models). This fact enables the use of our method for small sizes of active region, which significantly reduces the computational costs involved in vibration frequency calculations.

## B. Interstitial diffusion
Here, we demonstrate the effective jump frequency for diffusion of a single Li atom through a diamond cubic supercell of 1728 Si atoms, corresponding to a $6 \times 6 \times 6$ supercell of 8-atom unitcell, using the ReaxFF potential model. The thermodynamically favorable site for Li atom insertion in cubic diamond Si is a tetrahedral site $(T_{d})$ at $b_{0}$ distance away from a Si atom in the opposite direction of Si nearest neighbor, where $b_{0}$ is the bond length in a cubic Si structure. The diffusion process consists of a Li atom moving between two adjacent interstitial $T_{d}$ sites passing through the hexagonal (Hex) interstitial position. Our calculation results in a lattice constant of $5.46\ \mathring{A}$ for c-Si (and a corresponding $b_{0}$ value of $2.37\ \mathring{A}$), in good agreement with values reported in Refs. 33 and 34, using both DFT and ReaxFF calculations. We calculated the energy of Li atom in $T_{d}$ and Hex positions and the energy difference is 0.63 eV, in good agreement with previous energy barrier values reported in the literature. $^{33,34}$ Li interstitial at $T_{d}$ and Hex positions are indicated in Fig. 5 using VESTA. The prefactor rates are calculated with our method and compared with the "fixed environment" approach and the direct force constant calculation results. As indicated in Fig. 5, the discrepancy between our results and full Hessian calculation results remains relevantly small, even for small number of atoms in the active region, confirming the validity of our approach and its effectiveness on reducing the computational cost. We also observe that the "fixed environment" results are very similar to the "relaxed environment" results, slightly underperforming relative to the "relaxed environment" approach.

![](./images/812786606523023361_11.jpg)

![](./images/812786606523023361_12.jpg)

FIG. 4. (a) Effective jump frequency of vacancy hopping in silver obtained by our method using EAM potential. The x-axis indicates the number of atoms included in the active region, which is a sphere originated at the position of migrating atom in the saddle point configuration. The red squares are the prefactor values obtained by our method, where the atoms in the environment are relaxed during the force constant calculation. The black diamonds are the prefactor rates obtained by the "fixed environment" local force-constant calculation, where the atoms in the environment are fixed. The prefactor value reported in Ref. 10 is represented by a blue circle. (b) Minimum and saddle point configurations for vacancy jump indicated in a unit cell of fcc Ag.

![](./images/812786606523023361_13.jpg)

FIG. 5. (a) Effective jump frequency of lithium interstitial diffusion in cubic diamond silicon, obtained by a our method using ReaxFF potential. The x-axis indicates the number of atoms included in the active region, which is a sphere originated at the mean position of Li atom in the minimum and saddle point configurations. The red squares are the prefactor values obtained by our method, where the atoms in the environment are relaxed during the force constant calculation. The black diamonds are the prefactor rates obtained by the "fixed environment" local force-constant calculation, where the atoms in the environment are fixed. (b) Representation of minimum and saddle point configurations of Li diffusion in an 8-atom cubic diamond unit cell of Si. The tetrahedral ($T_d$) and hexagonal (Hex) interstitial positions are depicted, corresponding to minimum and saddle point configurations, respectively. In the lower plot, the 6 nearest neighbor atoms for Hex interstitial are represented by a different color for the purpose of clarity.

## C. Surface diffusion

We finally represent the effective jump frequency rates for oxygen adsorbate diffusion on platinum (111) surface. We use a 7-layer thick Pt(111) surface with each layer consisting of $4 \times 4$ atoms, including 112 platinum atoms in total. This simulation cell size is chosen since there exist previous studies for the diffusion profile for this system size using ReaxFF. $^{27}$ The high symmetry

![](./images/812786606523023361_14.jpg)

FIG. 6. (a) Effective jump frequency of oxygen adsorbate diffusion on platinum (111) surface, obtained by a our method using ReaxFF potential. The x-axis indicates the number of atoms included in the active region, which is a sphere originated at the bridge site position. The red squares are the prefactor values obtained by our method, where the atoms in the environment are relaxed during the force constant calculation. The black diamonds are the prefactor rates obtained by the "fixed environment" local force-constant calculation, where the atoms in the environment are fixed. (b) Representation of fcc, bridge, and hcp adsorption site on Pt(111) surface. (c) Energy profile for oxygen bridge-diffusion on Pt(111) surface. The x-axis is the diffusion coordinate distance in $\mathring{A}$ and the y-axis is the energy in eV.

adsorption site on a fcc(111) surface include the fcc, hcp, top, and bridge sits, as indicated in Fig. 6. We calculate the prefactor rates for the bridge-diffusion, which consists of an adsorbate moving from an fcc site to the nearby hcp site, passing through the bridge site. To isolate the oxygen adsorbate from the adjacent simulation cells, we included a $30$ Å vacuum region in the simulation cell. We conducted nudged elastic band calculations in LAMMPS to obtain the bridge-diffusion path for oxygen surface diffusion on Pt(111). The diffusion energy profile along with the initial, transition and final states are represented in Fig. 6, visualized by OVITO. The calculated forward (fcc-to-hcp) and backward (hcp-to-fcc) energy barriers are $0.65$ eV and $0.48$ eV, in good agreement with values reported in Ref. 27. The prefactor rates are then calculated for different number of atom in the active region, which is a sphere originated at bridge site position. Our results indicate very good convergence to the full Hessian calculation results and the range of error remains as small as 20%. The "fixed environment" results slightly underperform relative to our approach, although both methods give reliable results.

## V. DISCUSSION

Our results bring out two key messages. First, one can rigorously define the harmonic TST prefactor in terms of local effective Hessians, where the effect of the environment enters via a simple correction term associated with static elastic relaxations of the environment. Second, we find, through numerical simulations in a wide range of systems, that the corrections due to relaxing the environment tend to be similar in the stable and saddle point configurations, thus, justifying an even simpler "fixed environment" approach. This partial error cancellation (that occur beyond what our theoretical model predicts) is analyzed in more detail the supplementary material.

These observations open the way to simple, local approaches to computing the TST prefactor. Although we do not explore this possibility in detail here, our observations also suggest efficient hybrid schemes using three different regions: (i) an "active" region whose Hessian is explicitly calculated; (ii) an intermediate region surrounding it where atoms are relaxed during the computation of the effective Hessian of the active region; and (iii) an environment where all atoms are fixed.

## VI. CONCLUSION

In this paper, we examined an approach based on a local force-constant calculation in the vicinity of where a kinetic process takes place to obtain the prefactor in transition state theory. While the standard force constant calculation procedure is performed on an "active region," the overall effect of "environment" atoms is accounted for by relaxing them during this procedure. We demonstrated that the effective jump frequencies obtain using the proposed method rapidly converges to the full force-constant calculation results for a number of diffusion processes, validating the theory employed herein. We also found empirically that a faster and easier local force-constant approach, where the overall effect of atoms in the "environment" is disregarded by fixing them during the local force-constant process, results in very similar prefactor rates due to the cancellation of errors. The proposed approach significantly reduce the computation efforts involved in force-constant calculation by restricting the number of atoms to the vicinity of the kinetic event.

## SUPPLEMENTARY MATERIAL

See supplementary material for a detailed discussion on the cancellation of errors in frequency prefactor calculation for the "fixed environment" method.

## ACKNOWLEDGMENTS

This work was supported by the Office of Naval Research under Grant No. N00014-17-1-2202 and by Brown University through the use of the facilities of its Center for Computation and Visualization. This work used the Extreme Science and Engineering Discovery Environment (XSEDE), which is supported by the National Science Foundation Grant No. ACI-1548562.

## APPENDIX: SIMPLE DERIVATION OF A BLOCK MATRIX DETERMINANT IDENTITY

First, observe that
$$
\det\left(\begin{bmatrix}
I & 0 \\
X & L
\end{bmatrix}\right) = \det(L),
$$
where $I$ is the identity matrix, $0$ is a matrix of zeros, while $X$ and $L$ are conformable arbitrary matrices. We can then write (in the notation of Sec. II)
$$
\begin{aligned}
\det(H_A) &= \det\left(\begin{bmatrix}
A & C^T \\
C & E
\end{bmatrix}\right)\det(E^{-1})\det(E) \\
&= \det\left(\begin{bmatrix}
A & C^T \\
C & E
\end{bmatrix}\right)\det\left(\begin{bmatrix}
I & 0 \\
-E^{-1}C & E^{-1}
\end{bmatrix}\right)\det(E) \\
&= \det\left(\begin{bmatrix}
A & C^T \\
C & E
\end{bmatrix}\begin{bmatrix}
I & 0 \\
-E^{-1}C & E^{-1}
\end{bmatrix}\right)\det(E) \\
&= \det\left(\begin{bmatrix}
A - C^T E^{-1}C & C^T E^{-1} \\
0 & I
\end{bmatrix}\right)\det(E) \\
&= \det\left(A - C^T E^{-1}C\right)\det(E).
\end{aligned}
$$

Similarly, $\det(H_B) = \det\left(B - D^T E^{-1}D\right)\det(E)$.

## REFERENCES

$^1$M. Tang, L. Colombo, J. Zhu, and T. Diaz de la Rubia, *Phys. Rev. B* **55**, 14279 (1997).
$^2$M. I. Mendelev and Y. Mishin, *Phys. Rev. B* **80**, 144111 (2009).
$^3$V. Milman, M. C. Payne, V. Heine, R. J. Needs, J. S. Lin, and M. H. Lee, *Phys. Rev. Lett.* **70**, 2928 (1993).
$^4$W. Frank, U. Breier, C. Elsässer, and M. Fähnle, *Phys. Rev. Lett.* **77**, 518 (1996).
$^5$N. Sandberg, B. Magyari-Köpe, and T. R. Mattsson, *Phys. Rev. Lett.* **89**, 065901 (2002).
$^6$M. Mantina, Y. Wang, R. Arroyave, L. Q. Chen, Z. K. Liu, and C. Wolverton, *Phys. Rev. Lett.* **100**, 215901 (2008).
$^7$M. Mantina, Y. Wang, L. Chen, Z. Liu, and C. Wolverton, *Acta Mater.* **57**, 4102 (2009).
$^8$G. H. Vineyard, *J. Phys. Chem. Solids* **3**, 121 (1957).
$^9$S. Wei and M. Y. Chou, *Phys. Rev. Lett.* **69**, 2799 (1992).

$^{10}$C. Huang, A. F. Voter, and D. Perez, *Phys. Rev. B* **87**, 214106 (2013).

$^{11}$A. Binder, M. Luskin, D. Perez, and A. Voter, *Multiscale Model. Simul.* **13**, 890 (2015).

$^{12}$G. Henkelman and H. Jónsson, *J. Chem. Phys.* **113**, 9978 (2000).

$^{13}$G. Henkelman, B. P. Uberuaga, and H. Jónsson, *J. Chem. Phys.* **113**, 9901 (2000).

$^{14}$D. Sheppard, P. Xiao, W. Chemelewski, D. D. Johnson, and G. Henkelman, *J. Chem. Phys.* **136**, 074103 (2012).

$^{15}$G. Henkelman and H. Jónsson, *J. Chem. Phys.* **111**, 7010 (1999).

$^{16}$S. Kadkhodaei, LAMMPS-local_hessian package: A package for LAMMPS software, 2018, https://go.uic.edu/lammps_local_hessian.

$^{17}$See https://lammps.sandia.gov/doc/Build_package.html for LAMMPS documentation: Include packages in build, 8 Feb 2019.

$^{18}$P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

$^{19}$G. Kresse and D. Joubert, *Phys. Rev. B* **59**, 1758 (1999).

$^{20}$G. Kresse and J. Hafner, *Phys. Rev. B* **47**, 558 (1993).

$^{21}$G. Kresse and J. Hafner, *Phys. Rev. B* **49**, 14251 (1994).

$^{22}$G. Kresse and J. Furthmüller, *Comput. Mater. Sci.* **6**, 15 (1996).

$^{23}$G. Kresse and J. Furthmüller, *Phys. Rev. B* **54**, 11169 (1996).

$^{24}$J. P. Perdew, *Phys. Lett. A* **165**, 79 (1992).

$^{25}$P. L. Williams, Y. Mishin, and J. C. Hamilton, *Modell. Simul. Mater. Sci. Eng.* **14**, 817 (2006).

$^{26}$F. Fan, S. Huang, H. Yang, M. Raju, D. Datta, V. B. Shenoy, A. C. T. van Duin, S. Zhang, and T. Zhu, *Modell. Simul. Mater. Sci. Eng.* **21**, 074002 (2013).

$^{27}$D. Fantauzzi, J. Bandlow, L. Sabo, J. E. Mueller, A. C. T. van Duin, and T. Jacob, *Phys. Chem. Chem. Phys.* **16**, 23118 (2014).

$^{28}$K. Carling, G. Wahnström, T. R. Mattsson, A. E. Mattsson, N. Sandberg, and G. Grimvall, *Phys. Rev. Lett.* **85**, 3862 (2000).

$^{29}$K. Momma and F. Izumi, *J. Appl. Crystallogr.* **44**, 1272 (2011).

$^{30}$A. Stukowski, *Modell. Simul. Mater. Sci. Eng.* **18**, 015012 (2010).

$^{31}$A. Nakano, *Comput. Phys. Commun.* **178**, 280 (2008).

$^{32}$E. Maras, O. Trushin, A. Stukowski, T. Ala-Nissila, and H. Jónsson, *Comput. Phys. Commun.* **205**, 13 (2016).

$^{33}$G. A. Tritsaris, K. Zhao, O. U. Okeke, and E. Kaxiras, *J. Phys. Chem. C* **116**, 22212 (2012).

$^{34}$A. Ostadhossein, E. D. Cubuk, G. A. Tritsaris, E. Kaxiras, S. Zhang, and A. C. T. van Duin, *Phys. Chem. Chem. Phys.* **17**, 3832 (2015).

---

J. Chem. Phys. **150**, 144105 (2019); doi: 10.1063/1.5086746
Published under license by AIP Publishing

150, 144105-8
