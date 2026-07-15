
# Sampling the diffusion paths of a neutral vacancy in Silicon with SIEST-A-RT

Fedwa El-Mellouhi, \( ^{1,*} \)  Normand Mousseau, \( ^{1,\dagger} \)  and Pablo Ordejón \( ^{2} \) 

 \( ^{1} \) Département de physique and Regroupement québécois sur les matériaux de pointe,

Université de Montréal, C.P. 6128, succ. Centre-ville, Montréal (Québec) H3C 3J7, Canada

 \( ^{2} \) Institut de Ciência de Materiales de Barcelona (CSIC),

Campus de la Université Autónoma de Barcelona, Bellaterra, E-08193, Barcelona, Spain. (Dated: October 30, 2018)

We report a first-principles study of vacancy-induced self-diffusion in crystalline silicon. Starting form a fully relaxed configuration with a neutral vacancy, we proceed to search for local diffusion paths. The diffusion of the vacancy proceeds by hops to first nearest neighbor with an energy barrier of 0.40 eV in agreement with experimental results. Competing mechanisms are identified, like the reorientation, and the recombination of dangling bonds by Wooten-Winer-Weaire process.

PACS numbers: 61.72.Ji, 71.15.Mb, 71.15.Pd, 71.55.Cn,

## I. INTRODUCTION

Self-diffusion in homogeneous solids is a fundamental process of mass transport, in addition, it is responsible for the annealing of implantation damage, crystal to amorphous transition and the nucleation of extended defects. The native defects, such as vacancies and self-interstitial, have been identified as the prime entities controlling the self-diffusion, as well as the diffusion of impurities in semiconductor lattices. For example, in silicon, antimony impurities are vacancy diffusers and phosphorus are interstitial diffusers \( ^{1} \) . Therefore, self-diffusion in Si has been extensively investigated by experiments \( ^{1,2,3,4,5} \)  and simulations \( ^{6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34} \) .

In covalently bonded silicon, the neutral vacancy is the most stable charge state near room temperature  \( {}^{3,34} \) . While the diffusion mechanism and the barrier for silicon have been experimentally determined decades ago  \( {}^{4,5} \) , we still lack a detailed knowledge of the various activated mechanisms associated with the neutral vacancy. With standard ab initio molecular dynamics methods, the number of events generated is always insufficient to give reliable data for migration energies. Accordingly, most of the focus has been on formation energies, distortion and reorientation geometries  \( {}^{31} \) . Few papers reported a calculated activation energy and a migration path that are in agreement with the experimental data  \( {}^{29,35} \) . Until now, the only studies available for exploring the energy landscape were that of Munro and Wales  \( {}^{24} \)  who examined the dynamics of a vacancy, among others, using a tight-binding approach, and the work of Kumeda et al.  \( {}^{14} \)  using first-principles calculations. They identified the migration barrier and the underlying mechanism. However, a complete study for the topology of the landscape around a stable minimum is still needed.

The principal goal of this study is to give a complete description of the diffusion mechanism in elementary semiconductors. As such, the SIEST-A-RT method is built up to develop an entire methodology for quantum mechanically precise and reasonably fast energy landscape exploration method. Our simulations are performed on supercells containing 215 atoms. This supercell size is computationally tractable and constitutes a reasonable size to simulate the host crystal. We generate the diffusion paths using the activation-relaxation technique (ART) \( ^{36,37} \) , which can sample efficiently the energy landscape of complex systems. The forces and energies are evaluated using SIESTA \( ^{38,39} \) , a self-consistent density functional method using standard norm-conserving pseudo-potentials and a flexible numerical linear combination of atomic orbital basis set. Combining these two methods allows us to identify very efficiently diffusion paths of various energy height.

This paper is constructed as follows. In the next section,  \( \phi_{ijg,3,3} \)  use discuss the SIEST-A-RT method; simulation details are given in section III. We apply the method to the vacancy in silicon, the corresponding activated dynamics are detailed and discussed in section IV. Finally we emphasize the capability of the method in identifying competing events in silicon and its possible extension for future applications.

## II. METHOD: SIEST-A-RT

In order to sample the diffusion paths associated with a vacancy in bulk Si, we integrate the activation-relaxation technique (ART nouveau) \( ^{37,40} \)  to the ab-initio program SIESTA. This approach is similar to the integration of the hybrid eigenvector-following method to a tight-binding and an ab-initio code as performed by Munro, Kumeda and Wales \( ^{14,24} \)  as well as the dimer-method \( ^{41} \)  which was coupled with VASP \( ^{42} \)  by Henkelman and Jönsson \( ^{23} \) .

As both ART nouveau and SIESTA are described elsewhere in the literature \( ^{39,40} \) , we review these methods only briefly.

## A. ART nouveau

The activation-relaxation technique is a method for sampling efficiently the energy landscape of activated sys-
 

tems. \( ^{36,37} \)  Instead of following in details the thermal fluctuations, it searches directly for transition states; these are characterized as first-order saddle points in the energy landscape. This method was refined recently to ensure a controlled convergence to the saddle point (ART nouveau). \( ^{40} \)  An ART event can be decomposed into the following steps. Activation: (1) Starting from a local minimum, push the configuration in a direction chosen randomly in the 3N-dimensional space; stop when the lowest eigenvalue becomes negative or when the configuration is far enough from the initial configuration. (2) Follow the eigendirection corresponding to this negative eigenvalue while minimizing the energy in the perpendicular directions; stop when the total force (parallel and perpendicular to the eigendirection) falls below a given threshold (0.1 eV/Å). This is the transition state. Relaxation: After pushing over the saddle point, minimize the energy using any standard minimization algorithm.

In order to sample only the activated mechanisms associated with the vacancy, we restrict the initial random projection for each event to the atoms surrounding the defect. Except for this initial selection, all atoms are allowed to move during the ART event.

ART uses the Lanczos \( ^{43} \)  algorithm to extract the lowest eigenvalue and its corresponding eigenvector; 16 to 20 force evaluations are sufficient, irrespective of the size of the system, to extract a stable eigenvalue value and eigenvector. Recent unpublished tests indicate that the number of force evaluations needed to reach a saddle point is about the same for the dimer method and ART nouveau \( ^{41} \) , indicating no significant difference between the various activation-relaxation methods.

## B. Siesta

Forces and energies are evaluated using SIESTA \( ^{38,39} \) , a self-consistent density functional method using standard norm-conserving pseudo-potentials of Troullier-Martins \( ^{44} \)  factorized in the Kleiman-Baylander form \( ^{45} \) . Matrix elements are evaluated on a 3D grid in real space. The one-particle problem is solved using linear combination of pseudo-atomic orbitals (PAO) basis set of finite range. The quality of the basis can be improved by radial flexibilization, add more than one radial function within the same angular momentum (Multiple- \( \zeta \) ), and angular flexibilization or polarization, add shells of different atomic symmetry (different l).

Because ART requires a numerical derivative of the force to compute the curvature of the energy landscape, it is essential to obtain highly converged forces. The various parameters used are discussed below.

## C. Optimization of the parameters

The introduction of a vacancy in the crystal affects considerably the relaxation of the simulation cell. Previ-

![](./images/867768638382277387_1.jpg)

FIG. 1: "(Color on line)" Convergence tests for the energy per atoms as a function of Brillouin zone sampling for 64, 216 and 512 cubic supercells. The lines are guide to the eye. (see the text).

ous studies of the silicon vacancy using supercells ranging from 32 to 216 atoms with various Brillouin zone sampling techniques \( ^{11,14,15,19,22,25,26,27,33} \)  show a broad spread of formation energies (from 2.6 to 4.6 eV) and structural relaxation with  \( (D_{2d}, C_{2v}, C_{3v}, T_{d}) \)  symmetries. This scattering in mainly due to various convergence problems like basis set size, Brillouin zone sampling and supercell size. A recent work of Probert and Payne \( ^{27} \)  propose a systematic methodology for accurate calculations of defect structure in supercells. We proceed in a similar way in using supercells with up to 512-atoms.

## 1. Mesh cut-off and the basis set

With the presence of a defect, the single- \( \zeta \)  basis (SZ), i.e., a single orbital per occupied state, is unsatisfactory: both the formation energy and reconstruction surrounding the vacancy are far from experimental value. Moreover, we find that the lack of overlap between the PAO induced discontinuities in the force, causing serious problems to the application of ART. It is possible to address these problems by using the optimized basis generated using the procedure of Anglada et al. \( ^{46} \)  (SZ-optimized). Although much improved, the discontinuity in the force remains due to the presence of an underlying grid for the integration in real space which causes breaking of the translational symmetry. While the energy is converged with a real-space grid of about 0.03 Å (a mesh cut-off of 35-40 Ry), we find that we need a grid space of at most 0.02 Å (mesh cut-off of 50 Ry) to stabilize the force derivative; this spacing is comparable to the typical atomic displacement during the dynamics monitored by
 

ART.

## 2. Brillouin zone sampling

Because the defect is highly localized even in large supercells, we need to have fully converged forces and total energies for the system. In order to isolate Brillouin zone sampling effects, we study force and energy convergence with respect to the density of k-points. We use a Monkhorst and Pack \( ^{47} \)  mesh to sample the Brillouin zone. Uniform meshes of  \( q^{3} \)  shifted by  \( (k_{0}, k_{0}, k_{Q}) \)  are used, with q going from 1 to 4 and  \( k_{0} = 0 \)  or 0.5. For q=1 no offsets are used ( \( k_{0} = 0 \) ) to sample the  \( \Gamma \)  point. Offsets of  \( k_{0} = 0.5 \)  are used for q = 2, 3, 4 for each cubic supercell size.

Figure 1 displays the total energy per atom embedded in differently sized supercells with respect to q. The total energy is converged to  \( 1meV/atom \)  at a mesh of  \( 3^{3} \)  for the 64 supercell, this corresponds to a density of  \( 0.031\ \AA^{-1} \)  calculated using our LDA lattice parameter 5.39 Å. As discussed by Probert and Payne \( ^{27} \)  this density is sufficient to converge the total energy for larger systems. It is equivalent to a mesh of  \( 2^{3} \)  for 216 and 512 cells with densities of  \( 0.031\ \AA^{-1} \)  and  \( 0.023\ \AA^{-1 } \)  respectively. Comparing the forces for unrelaxed vacancy using different meshes and supercells of 63, 215 and 511 atoms, we find that atomic forces converge faster than the total energy as a function of k-point sampling: convergence to  \( 1\ meV/\AA \)  per degree of freedom is reached with a  \( 2^{3} \)  mesh for the 63 cell and with the  \( \Gamma \)  point for larger cells.

## 3. Supercell calculations

As reported by Puska et al. \( ^{25} \) , supercell method has obvious drawback because of the interaction of the defect and its periodic replicas. If the defect-defect distance is not large enough, the electronic structure of an isolated defect is distorted because the deep levels in the band gap form energy bands with a finite dispersion. The size of the supercell restricts also the ionic relaxation. The relaxation pattern is truncated midway between the defect and its nearest image.

In order to identify the smallest cell-size acceptable for the simulation of diffusion mechanisms with negligible size effects, we study the structural relaxation and the formation energies with respect to supercell size by employing supercells as large as 511 ionic sites.

Formation energies are calculated for fully converged supercells with respect to the basis set and Brillouin zone sampling as detailed in sections II C1, II C2. Results for 63 and 215 atoms supercells are overestimated compared to the 511-cell results by 9 % and 2% respectively as shown in table I. This error on vacancy formation energy for small supercell was previously reported by Puska et al. \( ^{[11]} \)  as due to the interaction of the vacancy with its periodic images and reflects a repulsive component of the defect-defect interaction, this component tends to vanish for the 215 supercell.

Structural relaxation is also of a major importance, it informs us about the correctness of the atomic forces. The 63-atom supercell shows a wrong relaxation pattern. Tetrahedral ( \( T_{d} \) ) symmetry is a metastable minimum irrespective of the density of k points used with a formation energy of 3.99 eV (see the second line on in table I). Symmetry need to be broken artificially to get a Jahn-Teller distortion leading to a  \( D_{2d} \)  symmetry with lower formation energy (3.59 eV). This is misleading and shows that size effects are important for supercells of 63 ionic sites and smaller. This size is insufficient to represent the system and the diffusion pattern correctly as discussed in more details in section IV D.

For larger system, size effects tend to have minor effects on the relaxation geometry. Already at 215 cells,  \( D_{2d} \)  symmetry is obtained even for low density of k-points ( \( \Gamma \)  only). The formation energy using  \( \Gamma \)  point for the 215 supercell is underestimated by 6% compared to the best converged results we got with the 511 supercell, it tends to converge to the formation energy of larger models relaxed with  \( \Gamma \) -point only.

We conclude, in agreement with previous works \( ^{[11,25,27]} \)  that a supercell of 215-atoms with  \( \Gamma \) -point is the minimal size and sampling we can use in order to ensure that both energy and forces are sufficiently accurate to provide results of a quality at least equal to experimental precision.

## III. DETAILS OF THE SIMULATION

We perform first-principles electronic structure calculations based on the density functional theory within the local-density approximation (LDA) \( ^{48,49} \)  for the exchange-correlation energy. The static zero-temperature calculations for energies and forces are computed from SIESTA. Forces on the atoms are computed using the Hellman-Feynman theorem. The nuclear positions are optimized by using a conjugate gradient algorithm (CG) to minimize the total energy. Using the unit cell of two atoms and increasing the number of k points the equilibrium lattice constant of bulk Si converges to 5.39 Å. The cell volume and shape are kept fixed during the simulation. The crystalline 216 supercell is relaxed until the largest force component is of about 0.002 eV/Å. One conjugate gradient (CG) step is necessary to relax the structure with vanishingly small force components. To create the starting configuration with a defect, one atom is removed from the ideal crystalline cell. The obtained structure contains a mono-vacancy characterized by a vacancy-vacancy distance of 16.17 Å, with tetrahedral symmetry ( \( T_{d} \) ). The structure is then allowed to relax at constant volume. All the events are generated starting from a fully relaxed 215-atom unit-cell with a single vacancy displaying an expected Jahn-Teller distortion: the four atoms around the vacancy are paired two by two with  \( D_{2d} \)  symmetry,
 

TABLE I: Converged formation energies for  \( (E_{f}) \)  for different supercells and k-points meshes compared with various ab-initio calculations. For each work we specify the DFT functionals used: local density approximation (LDA), screened-exchange LDA (sx-LDA) and conjugate gradient approximation (GGA) with the corresponding plane-wave (PW) energy cutoff when applicable. (TB-EF) denotes tight binding calculations with eigenvalue following method. In the  \( D_{2d} \)  symmetry or the pairing mode, the distorted tetrahedron formed by atoms around the vacant site has two short bonds for atoms belonging to the same pair (atom-atom) distance and four long bonds between atoms from different pairs (pair-pair). The resulting symmetries of the defect are reported as well. Experimentally, Watkins et al. \( ^{4} \)  measured a formation energy of  \( 3.6 \pm 0.5 \)  eV and Dannefaer et al. \( ^{5} \)   \( 3.6 \pm 0.2 \)  eV

<table><tr><td>Authors</td><td>Method</td><td>Cell-size</td><td>k-points</td><td>Ef(eV)</td><td colspan="2">Distances (Å)</td><td>Symmetry</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>pair - pair</td><td>atom - atom</td><td></td></tr><tr><td rowspan="5">This work</td><td rowspan="5" colspan="2">LDA</td><td>63</td><td>3³</td><td>3.6</td><td>3.34</td><td>2.79</td></tr><tr><td></td><td></td><td>3³</td><td>3.95</td><td>3.19</td><td>3.19</td></tr><tr><td></td><td>215</td><td>Γ</td><td>3.1</td><td>3.34</td><td>2.89</td></tr><tr><td></td><td></td><td>2³</td><td>3.36</td><td>3.35</td><td>2.9</td></tr><tr><td>511</td><td>2³</td><td>3.29</td><td>3.35</td><td>2.9</td><td>2.9</td></tr><tr><td rowspan="4">Lento and Nieminen33</td><td rowspan="2">LDA</td><td>32</td><td>(1/4,1/4,1)</td><td></td><td>3.608</td><td>3.084</td><td>D2d</td></tr><tr><td>256</td><td>(1/4,1/4,1)</td><td>3.6</td><td>3.490</td><td>2.950</td><td>D2d</td></tr><tr><td rowspan="2">pw (15 Ry)</td><td rowspan="2" colspan="2">256</td><td rowspan="3">(1/4,1/4,1)</td><td rowspan="3">3.515</td><td rowspan="2"></td><td rowspan="3">D2d-outward</td></tr><tr></tr><tr><td rowspan="2">Probert et al.27</td><td>GGA</td><td>256</td><td>2³</td><td>3.17</td><td>3.72</td><td>3.1</td></tr><tr><td>PW (12Ry)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">Puska et al.11</td><td rowspan="2">LDA</td><td>63</td><td>Γ</td><td>2.86</td><td></td><td></td><td>C2v</td></tr><tr><td>PW (15 Ry)</td><td></td><td>2³</td><td>3.41</td><td>3.42</td><td>3.40</td></tr><tr><td rowspan="2"></td><td rowspan="2" colspan="2">215</td><td rowspan="3">Γ</td><td rowspan="2">3.27</td><td rowspan="3">3.38</td><td rowspan="2">2.89</td></tr><tr></tr><tr><td rowspan="2" colspan="2">Mercer et al.26</td><td>LDA</td><td>127</td><td>2³</td><td>3.63</td><td>3.50</td><td>2.89</td></tr><tr><td>PW (12-20 Ry)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Kumeda et al.14</td><td>LDA</td><td>63</td><td>Γ</td><td>3.32</td><td></td><td></td><td></td></tr><tr><td>PW(12 Ry)</td><td>215</td><td>Γ</td><td>3.902</td><td></td><td></td><td></td></tr><tr><td>GGA</td><td>215</td><td>Γ</td><td>3.336</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Seong and Lewis10</td><td>LDA</td><td>63</td><td>Γ</td><td>3.65</td><td>3.53</td><td>3.00</td><td>D2d</td></tr><tr><td>PW (10 Ry)</td><td>511</td><td>Γ</td><td>4.12</td><td></td><td></td><td></td></tr><tr><td rowspan="2">Munro and Wales 24</td><td rowspan="2" colspan="2">TB-EF</td><td>63</td><td>Γ</td><td>3.73</td><td></td><td></td></tr><tr><td>215</td><td>Γ</td><td>3.902</td><td></td><td></td></tr><tr><td rowspan="2">Antonelli et al.12</td><td>LDA</td><td>63</td><td>2³</td><td>3.49</td><td>3.53</td><td>3.01</td><td>D2d</td></tr><tr><td>PW(16 Ry)</td><td></td><td></td><td></td><td>3.52</td><td>3.40</td><td>D2d</td></tr></table>

as described in section IV A. More than 120 events were started from this geometry, each launched in a different random direction, providing an extensive sampling of the energy landscape around the vacancy. The results from this search confirm a posteriori that this is indeed the minimum-energy configuration for the isolated vacancy. Using the set of parameters detailed in this section, one event with SIEST-A-RT requires about 700 force evaluations and takes about 3 days of CPU times on a single IBM Power 4 processor.
 

## IV. RESULTS

## A. Neutral vacancy relaxation

The details of the relaxation around the vacancy depend on the local charge \( ^{3,50} \) . Since there is one electron per dangling bond for the neutral charge state  \( (V^{0}) \) , it is expected to undergo a Jahn-Teller distortion \( ^{3,50} \)  by forming two pairs out of the four dangling bonds of the vacancy. This is what we see. During the relaxation of the 215-atom cell, the total energy of the system is reduced by about 1.71 eV, due to the distortion of the lattice and the relaxation of the atoms around the vacancy. This relaxation energy is larger than the 0.36 eV as obtained from a study on 63-atom cell by Seong et Lewis \( ^{10} \)  and the 0.9 eV calculated on a HF cluster calculation \( ^{30} \)  and compared to values from a more recent study \( ^{27} \)  1.186 eV using GGA on a 256 supercell.

The relaxation can be described as follows. The vacancy nearest neighbors (NN) first move away from each other by pair along the  \( <110> \)  axis \( ^{10} \) . The net local displacement of 0.39 Å per atom result into a tetragonal symmetry configuration ( \( D_{2d} \) ). The distorted tetrahedron formed by the atoms has four long bonds of 3.35 Å and two short bonds of 2.9 Å as shown in Fig. 3(A). The formation of bonds between the two pairs weakens the back bonds which are then significantly stretched \( ^{12} \) , up to 2.49 Å. The range of perturbation introduced by the defect in the 215 supercell affects up to 5 surrounding shells: the average amplitude of relaxation falls progressively from 0.39 Å for the first shell to 0.074 Å for the fifth shell which is of the order of atomic vibrations at room temperature.

The amplitude and the type of displacement compare very well with the previous results using DFT \( ^{11,14,15,19,22,25,26,27} \) . The LDA results appear to be at odds with recent screened-exchange LDA calculations on partially relaxed neutral Si vacancy, it indicates that the relaxation could be outward \( ^{33} \) . More work remains to establish if LDA really fails here. Our results on the pairing mode are compared with some of these results in table I.

The formation energy  \( E_{f} \)  is calculated by taking into account the distortion of the lattice, using the expression:

 \[ E_{f}=E_{N-1}-\frac{N-1}{N}E_{N} \quad (1) \] 

Where N is the number of atoms and  \( E_{N} \)  is the relaxed total energy of the ideal structure.  \( E_{N-1} \)  is the total energy of the distorted system containing the defect. Within SIESTA, the formation energy of the monovacancy is 3.36 eV, which is in agreement with previous LDA and experimental studies. On the simulation side, Kelly et al. \( ^{51} \)  calculated 3.5 eV, Blöchl et al. \( ^{52} \)  4.1 eV, Mercer et al. \( ^{26} \)  3.63 eV and Kumeda et al. \( ^{14} \)  3.32 eV. Experimentally, Watkins et al. \( ^{4} \)  measured  \( 3.6 \pm 0.5 \)  eV and Dannefaer et al. \( ^{5} \)   \( 3.6 \pm 0.2 \)  eV. A complete comparison in reported in table I.

![](./images/867768638382277387_2.jpg)

FIG. 2: "(Color online)" Top: (a) The total minimum-energy path for the simple diffusion. The saddle points identified in various ART events are indicated by the same labels (B,C and D) as in Table II. The path is generated by previous knowledge of the initial, the saddle point and final states, then the overall configuration is relaxed using the nudged-elastic-band method \( ^{28} \) . The contributions from different moving atoms are decomposed in two: (b) The path followed by the diffusing atom; (c) Diffusion of the other atoms around the defect. Here The assymetry is due to reconstruction.

A

![](./images/867768638382277387_3.jpg)

![](./images/867768638382277387_4.jpg)

FIG. 3: "(Color online)" The vacant site is visible in the snapshots A and C. A is the initial minimum and C is the ideal split vacancy site, the arrow shows the direction of the diffusion.

The energy of 511 supercell,  \( E_{f}^{511} \) , is found to be 3.29 eV after a full convergence of the energy. Previous works by Wang et al. \( ^{[19]} \)  and Seong and Lewis \( ^{[10]} \)  reported  \( E_{f}^{511}=4.12 \)  eV and 4.10, respectively. A recent study by Probert et al. give GGA results of a fully converged calculation for a vacancy in BCC silicon lattice with 256 atoms, they obtain a formation energy of 3.17 eV.
 

TABLE II: Interatomic distances along the minimum energy path for a simple diffusion. The positions correspond to the labels in Fig. 2(a). A corresponds to the initial minimum with a relaxed vacancy: the active atom (1) is bonded to four neighbors, B,C and D are transition states. During the migration bonds are stretched progressively until all the distances becomes equal at the configuration C.

<table><tr><td>Distance( \( \textup{\AA} \) )</td><td>\( d_{1-2} \)</td><td>\( d_{2-3} \)</td><td>\(  d_{1-4}  \)</td><td>\(   \( d_{1-5}  \)</td><td> \(  d_{1-6}  \)</td><td>\(  d_{1-7}  \)</td></tr><tr><td>A</td><td>2.49</td><td>2.39</td><td>2.39</td><td>\( 2.89  \)</td><td>\( 3.34  \)</td><td>\(  3.34  \)</td></tr><tr><td>B</td><td>2.67</td><td>2.67</td><td>\( 2.65  \)</td><td>\( 2,65  \)</td><td>2.76</td><td>2.73</td></tr><tr><td>C</td><td>2.68</td><td>2.68</td><td>\( 2,68  \)</td><td>\( 2.68  \)</td><td>2.68</td><td>2.68</td></tr><tr><td>D</td><td>2.68</td><td>\( 2.87  \)</td><td>\( 2,61  \)</td><td>\(  2,69  \)</td><td>\( 2,61  \)</td><td>\(  2,69  \)</td></tr></table>

## B. Simple diffusion paths

Even a defect as simple as a neutral vacancy can be associated with many activated mechanisms, some of which leading to migration: among the generated events, 60 % are simple diffusion mechanisms, while 15 % are reorientation and the remaining are more complex events involving a pair or more of active atoms.

## 1. Nearest neighbor diffusion

The simplest migration process involves hopping of the vacancy to a nearest-neighbor site as shown in Fig. 2(a): a nearest-neighbor of the vacancy moves along the <111> direction toward the vacant site (shown in Fig. 3A) and passes the metastable split-vacancy site before falling in the tetrahedral site previously formed by the vacancy. The energy barrier for this mechanism is  \( 0.40 \pm 0.02 \)  eV. The error estimate comes from the convergence criterion to the saddle point as explained in section II A. This result for the migration energy is in good agreement with the experimental findings of Watkins et al. \( ^{3} \)  who measured  \( 0.45 \pm 0.04 \)  eV. In a work similar to this one, but using the CPMD code with GGA (BLYP) functional, Kumeda et al. \( ^{14} \)  found a barrier of 0.58 eV.

The diffusion path is reconstructed in detail using the nudged-elastic band method \( ^{28} \)  and relaxed until the total force is of 0.2 eV/ \( \AA \) . This path shows an unusually long transition plateau — ranging from  \( d_{r}=0.7 \)  to 1.2  \( \AA \) —with a slight energy minimum at the split-vacancy site. At this point, the 3 back bonds are stretched and the diffusing atom forms weak bonds (length 2.685 \( \AA \) ) with the surrounding atoms of the six membered ring. From this site, a small displacement of 0.11  \( \AA \)  is sufficient to overcome the barrier of 0.04 eV and complete the jump to the new minimum (see table II). This value is of the order of the precision of the method; in addition, at room temperature this minimum would be smeared out by thermal vibrations. Because of a lack of a better approximation, we use Vineyard’s quasiharmonic approximations \( ^{53} \)  to get a rough estimate of the attempt frequency (see section IV B3), approximating the transition plateau by a single barrier.

Although the total diffusion path in Fig. 2(a) is asymmetric, after separating the contribution coming from different moving atoms, we find that diffusion path is symmetric for the diffusing atom as shown in figure (Fig. 2(b)). The asymmetry in the path shown in Fig. 2(c) is due to the reconstruction: with four atoms reconstructing two-by-two, there are three possible orientations. Here, the orientation is different for the initial and final state. This should average out as the vacancy moves around.

A comparison of the formation energies using the Stillinger-Weber \( ^{35} \)  and the MEAM \( ^{54} \)  potentials for the vacancy and the split vacancy gives a migration energy of 0.43 and 0.37 eV, respectively. Although the formation energies for the vacancy are not well represented by empirical potentials the energy difference is in agreement with experiment and with our results. The minimum-energy path, however, is not well described by these potential and the local minima identified by Maroudas et al. \( ^{35} \)  during the migration are absent in our case.

## 2. Reorientation process

In addition to finding diffusion mechanisms associated with the vacancy, we also identify the trajectories responsible for atomic rearrangement in the reconstructed configuration. As there are three pairing possibilities for the  \( D_{2d} \)  symmetry, it is possible for the configuration to hop from one of these states to either of the two others.

SIEST-A-RT generates easily this reorientation of the paired atoms. As illustrated in Fig. 4, starting with the reconstructed pairs formed initially — 1-4 and 2-3—, atom “3” moves away form its neighbor along the <111> direction, breaks the weak bond with “2” and reaches the transition state, which is in the trigonal symmetry  \( (C_{3v}) \) . The relaxation continues until new bonds form between the pairs 1-2 and 3-4. The activation energy for the reorientation of the neutral vacancy between two tetragonal orientations is 0.2 eV. Roberson et al. \( ^{29} \)  in a HF calculation scheme performed calculation on small clusters (44 silicon atoms) and found 0.37 eV; another cluster calculation, by Öğüt et al. \( ^{30} \)  found 0.32 eV.

The deformation to the  \( C_{3v} \)  can be observed experimentally. The experiment consists of applying a stress at high temperature in the dark, then cooling down to about 20K, relieving the stress, illuminating the sample and monitoring the resulting vacancy species. The barrier measured from this alignment experiment is at 0.23 eV, in excellent agreement with our calculations \( ^{3} \) .

Our simulations also show that the pairing mode can change during the migration of the vacancy. For the simple diffusion plus reorientation, we find an overall energy barrier of 0.47 eV and a total displacement of 0.68 Å at the saddle point.
 
![](./images/867768638382277387_5.jpg)

FIG. 4: "(Color on line)" The reorientation path passing over the saddle point configuration.  \( (I \rightarrow S \rightarrow F) \) , the tetragonal axis is fixed throughout this process. At the saddle point the local atomic coordinates of the distorted lattice shows a trigonal symmetry. The pairing mode changes to one of the equivalent modes.

## 3. Diffusion constants and diffusion rate

The diffusion is a two step process, consisting of the creation and the subsequent migration of a vacancy. Assuming that both processes are thermally activated, the activation energy  \( E_{a} \)  for diffusion is the sum of the formation energy  \( E_{f} \)  and the migration energy  \( E_{m} \) . By collecting our data from the previous sections we get an activation energy of  \( E_{a} = 3.5 \, eV \) , which is in good agreement with  \( E_{a} = 4.14 \, eV \)  recently measured by Bracht et al. \( ^{[55]} \) , and with the activation enthalpy for self-diffusion  \( H_{V} = 4.07 \pm 0.2 \, eV \)  obtained by Tang et al. \( ^{[20]} \)  using tight-binding MD.

It is well known that there is a strong competition between the interstitial and the vacancy-mediated mechanisms of self-diffusion. These two contributions were separated in a metal-diffusion experiment \( ^{55} \)  and the vacancy contribution to the self-diffusion was measured to be

 \[ C_{V}^{e q}(T)d_{v}(T)=0.92e x p\frac{(-4.14e V)}{k_{B}T}c m^{2}s^{-1} \quad (2) \] 

Other experimental data \( ^{56} \)  shows that

 \[ C_{V}^{e q}(T)d_{v}(T)=0.6e x p\frac{(-4.03e V)}{k_{B}T}c m^{2}s^{-1} \quad (3) \] 

Both data sets predict a self-diffusion dominated by vacancies at low temperature, where  \( C_{V}^{eq}(T) \)  is the concentration of vacancies at a certain temperature.
Experiments under thermal equilibrium concentrations of native point defects have shown that the Si self-diffusion coefficient  \( D_{Si}^{eq} \)  exhibits Arrhenius behavior,

 \[ D_{S i}^{e q}(T)=D_{0}e^{-H_{a}/k_{b}T}, \quad (4) \] 

where  \( H_{a} \)  is a single activation enthalpy,  \( D_{0} \)  is the prefactor in a certain temperature range, T denotes the absolute temperature, and  \( k_{B} \)  is the Boltzmann's constant. Under the assumption that the diffusion proceeds through discrete jumps of equal length r — the distance between nearest neighbor equilibrium sites, in diamond cubic lattices  \( r = a\sqrt{3}/4 \) , where a is the lattice parameter the prefactor is written as \( ^{34} \) 

 \[ D_{0}=\frac{z}{6}\Gamma_{0}r^{2} \quad (5) \] 

with  \( \Gamma_{0} \)  the jump, or attempt, frequency of the point defect from one equilibrium site to another, z denotes the number of neighbor sites, in the diamond lattice a vacancy can jump to one of the four neighbors. In the harmonic approximation, this attempt frequency is defined as \( ^{53,57} \) 

 \[ \Gamma_{0}=\frac{\displaystyle\prod_{i=1}^{3N}\nu_{i}^{(i)}}{\displaystyle\prod_{i=1}^{3N-1}\nu_{i}^{(s)}} \quad (6) \] 

where  \( \nu_{i}^{(i)} \)  and  \( \nu_{j}^{(S)} \)  are the normal mode frequencies at the minimum and the saddle point respectively and the product does not include the imaginary frequency at the saddle point. The eigenvalues are computed by diagonalizing the Hessian, obtained by numerical derivation with a step of 0.01 Å.

Accordingly, the migration entropy defined as the entropy difference between the saddle point and the equilibrium point configuration at low temperature can be written as

 \[ \Delta S=S_{V}^{m}=k_{B}\ln\left[\frac{\prod\limits_{i=1}^{3N-1}\nu_{i}^{(i)}}{\prod\limits_{i=1}^{3N-1}\nu_{i}^{(s)}}\right] \quad (7) \] 

The phonon frequency corresponding the direction of the jump is removed from the numerator. In addition the self diffusion entropy evaluated experimentally is the sum of the diffusion entropy and the formation entropy  \( S_{V}^{SD} = S_{V}^{f} + S_{V}^{m} \) . Using the experimental  \( S_{V}^{SD} = 5.5k_{B} \)  by Bracht et al. \( ^{55} \)  and a  \( S_{v}^{f} = (5 \pm 2)k_{B} \)  as calculated by Blöchl et al. \( ^{52} \)  and Dobson et al. \( ^{9} \) , migration entropy is expected to lie within  \( 1k_{B} \)  and  \( 2.5k_{B} \) , our calculated data  \( \Delta S = 3.036k_{B} \) .

The corresponding attempt frequency  \( \Gamma_{0}=8.65\times10^{12}s^{-1} \)  is similar to the result of Maroudas et al. \( ^{35} \)
 

 \( (1.0539 \times 10^{13}s^{-1}) \) , obtained with the Stillinger-Weber potential. The corresponding diffusion prefactor is  \( D_{0} = 3.141 \times 10^{-3}cm^{2}s^{-1} \) . Our diffusion constant can be compared with results from Maroudas et al. \( ^{35} \)  by taking into account the z factor that had been omitted, the resulting prefactor  \( D_{0} = 3.88 \times 10^{-3}cm^{2}s^{-1} \)  is in agreement with our results. Tang et al. \( ^{8,20} \)  report  \( D_{0} = 1.18 \times 10^{-4}cm^{2}s^{-1} \)  using TB-MD and thermodynamical integration, their migration energy ( \( E_{m} \) ) is of 0.1 eV.

Our numerical estimate of the diffusion rate  \( \Gamma = \Gamma_{0}e^{E_{m}/k_{B}T} \)  at room temperature gives a characteristic time for diffusion ( \( \tau = 1/\Gamma \) ) of the order of microseconds. This timescale is not directly accessible to ab-initio molecular dynamics, so simulations must generally be run at temperatures close to the melting point. With SIEST-A-RT, we can study the activated mechanisms from the local energy minimum, allowing us to identify accurately subtle mechanisms such as that associated with the split-vacancy site.

## C. Complex diffusion paths

The SIEST-A-RT sampling of the energy landscape around the vacancy also identifies a number of high-energy barrier events which involve a complex atomistic rearrangements. Two types of such events occur. The first one can be described as a diffusion event mediated by bond exchange. In this case, the overall result is a simple vacancy hop but with a more complex transition state and a barrier of 2.4 eV.

The second type of events involves what has been dubbed spectator events \( ^{14} \)  (see Fig. 5) where the diamond network surrounding the vacancy is altered. These spectator events all correspond basically to the bond-switching mechanisms proposed many years ago by Wooten, Winer and Weaire as mechanism for amorphization \( ^{58} \) . In recent years, the WWW mechanism has also been identified as the bond defect \( ^{59} \)  and the four fold coordinated defect (FFCD) \( ^{16} \) .

Two types of spectator events are identified. In one of these events, two of the direct neighbors of the vacancy are pushed toward each other, leading to the saturation of the dangling bonds; as a consequence one of the long covalent bonds between the NN of the vacancy transform to a real bond in a form very similar to the bond defect complex identified by Marqués et al \( ^{17} \) . The lowest barrier we found is 2.63 eV for a process involving a direct neighbor of the vacancy (one of the bonds is already weak), the final configuration is 2.16 eV higher than the initial minimum. Kumeda et al. found the single spectator WWW barrier of 1.719 eV using LDA and 1.867 eV using BLYP functional \( ^{14} \) .

The second type, atoms far from the vacant site are involved. The effect of the vacancy on the WWW event barrier is less strong for complex events located far from the vacancy without involving a direct neighbor. As the lattice distortion increases, so does the energy barrier.

![](./images/867768638382277387_6.jpg)

FIG. 5: "(Color on line)" A spectator WWW process involving atoms far from the vacant site. Left panel: atoms in grey are the atoms involved in the exchange, the direction of the exchange is illustrated by the arrows. Right panel: the final configuration is a stable minimum by which a disorder in the crystalline lattice is introduced.

For this mechanism, for example, the barrier ranges from 3.31-3.8 eV, a value which can be compared to the I-V recombination process identified to be responsible for the amorphization of crystalline silicon of Marqués et al \( ^{17} \)  the barrier is estimated to be between 4.58 and 4.75 eV using ab initio calculation \( ^{59} \) . One can estimate the effect of the vacancy to lower the barrier by about 1.27 eV. Since the barrier is very high, this kind of events is unlikely to play any significant role in crystals at room temperature.

## D. Size effects

As discussed, previously, it is necessary to use a large simulation cell in order to minimize the interaction between the images of the vacancy. This is particularly noticeable in a 63-atom supercell, even though the defect-defect separation is larger than 4 inter-atomic distances. It is this interaction that cause the unrealistic relaxation pattern identified in previous studies \( ^{15,26} \) , allowing the vacancy to relax both with a  \( T_{2d} \)  and a  \( D_{2d} \) , symmetries.

Relaxing a 63-atom supercell with SIESTA and the parameters described above, we find that two stable minima: the  \( D_{2d} \)  (tetragonal) relaxation described previously as well as a  \( T_{d} \)  (tetrahedral) configuration, a symmetry which is unstable in cells of 215 and 511 atoms. Within the later symmetry, all atoms relax inward, conserving the tetrahedral symmetry of the system at equal distance of 3.4 Å. The  \( T_{2d} \)  structure can be reached with a single jump from the  \( D_{2d} \)  site during a reorientation mechanism similar to that described in section IV B2, crossing a small barrier of 94 meV with an overall displacement of 0.64 Å. The energy difference between the two symmetries is estimated to be 83 meV compared to
 

20 meV as obtained by Mercer et al. in a simulation also on a 63-atom cell \( ^{26} \) . We obtain qualitatively similar results with  \( 2^{3} \)  k-points mesh.

The interaction between images also affects the barrier for the simple diffusion and the reorientation, which is underestimated by 50 % compared to the 215 cell results. Interestingly, this underestimation is compensated by a higher formation energy, leading to very similar activation energies for the two size systems.

The underestimation of the diffusion barrier in the 63-atom cell makes it easier for the vacancy to jump to the second-neighbor position. Although we saw many such events in the small cell, this mechanism was not generated in the 215-atom box; there does not appear to be any direct path for second-neighbor diffusion in silicon.

## V. DISCUSSION AND CONCLUSIONS

In this paper, we report on the study of the activated dynamics associated with a neutral vacancy in bulk crystalline silicon. Following the work of Munro, Kumeda and Wales \( ^{14,24} \) , we couple an ab initio code, SIESTA, with the activation-relaxation technique, ART nouveau, in order to sample the various activated mechanisms taking place around the vacancy accurately and efficiently. Defining moves directly in the energy landscape, it is as easy to generate the diffusion trajectory responsible for the high-energy bond-switching mechanisms than it is to find the path associated with the jump reorientation of the reconstructed state ( \( D_{2d} \rightarrow D_{2d} \) ).

Simulating more than 120 activated trajectories, we find a number of different diffusion mechanisms associated with the vacancy. In particular, we recover the basic vacancy hopping diffusion mechanism and show that the path associated with it includes a very metastable state at the split-vacancy site. Moreover, we can reproduce without difficulty the jump between the symmetrically equivalent reconstructed states. We also generate a number of higher-energy diffusion mechanisms which reminiscent of those found in amorphous silicon as well as at the crystalline-amorphous interface.

Because we obtain, with good accuracy, the transition state associated with each of these mechanisms, we also compute the transition rate in the harmonic approximation. The result obtained is in good agreement with experiment as well as previous high-temperature TB-MD simulation \( ^{20} \) .

Overall, various barrier and relaxation energies computed here are in agreement with results obtained previously both experimentally and numerically. Using a large simulation cell and an extensive sampling of the energy landscape around the vacancy, we could also show that some of the previously obtained mechanisms were artifact due to the small size of the cell used. These results establish the validity of the SIEST-A-RT approach as a unique tool for the study of the diffusion and relaxation mechanisms of defects in crystalline materials. This method can be easily extended to study semiconductor compounds, adatom diffusion, interlayer diffusion, all systems with a landscape too complicated for high-temperature molecular dynamics. Even in system as simple as a vacancy in c-Si, we found a number of activated mechanism associated with non-trivial transition paths. The situation promises to be more complex in binary semiconductors, such as GaAs and GaN, where the bonding character and chemical composition are much more complex than for Si.

## VI. ACKNOWLEDGMENTS

This work is funded in part by NSERC and NATEQ. NM is a Cottrell Scholar of the Research Corporation. Most of the simulations were run on the computers of the Réseau québécois de calcul de haute performance (RQCHP) whose support is gratefully acknowledged.

 \( ^{*} \)  Electronic address: f.el.mellouhi@umontreal.ca

 \( ^{\dagger} \)  Electronic address: Normand.Mousseau@umontreal.ca

 \( ^{1} \)  A. Ural, P. B. Griffin, and J. D. Plummer, Phys. Rev. Lett. 83, 3454 (1999).

 \( ^{2} \)  A. L. Lagna and S. Coffa, Phys. Rev. Lett. 82, 1720 (1999).

 \( ^{3} \)  G. D. Watkins, Deep Centers in semiconductors, edited by S. T. Pantelides (Gordon and Breach, New York, 1992), chap. 3.

 \( ^{4} \)  G. Watkins and J. Corbett, Phys. Rev. 134, A1389 (1964).

 \( ^{5} \)  S. Dannefaer, P. Mascher, and D. Kerr, Phys. Rev. Lett. 56, 2195 (1986).

 \( ^{6} \)  S. V. Ghaisas, Phys. Rev. B 43, 1808 (1991).

 \( ^{7} \)  S. Oğüt and J. R. Chelikowsky, Phys. Rev. Lett. 83, 3852 (1999).

 \( ^{8} \)  A. Jääskeläinen., L. Colombo, and R. Nieminen, Phys. Rev. B 64, 233203 (2001).

 \( ^{9} \)  T. W. Dobson, J. F. Wager, and J. A. Van Vechten, Phys. Rev. B 40, 2962 (1989).

 \( ^{10} \)  H. Seong and L. J. Lewis, Phys. Rev. B 53, 9791 (1996).

 \( ^{11} \)  M. J. Puska, S. Pöykkö, M. Pesola, and R. M. Nieminen, Phys. Rev. B 58, 1318 (1998).

 \( ^{12} \)  A. Antonelli, E. Kaxiras, and D. J. Chadi, Phys. Rev. Lett. 81, 2088 (1998).

 \( ^{13} \)  Y. Bar-Yam and J. D. Joannopoulos, Phys. Rev. B 30, 2216 (1984).

 \( ^{14} \)  Y. Kumeda, D. J. Wales, and L. J. Munro, Chem. Phys. Lett. 341, 185 (2001).

 \( ^{15} \)  R. Virkkunen, M. Alatalo, M. Puska, and R. M. Nieminen, Comp. Mat. Sc. 1, 151 (1993).

 \( ^{16} \)  S. Goedecker, L. Billard, and T. Deutch, Phys. Rev. Lett. 88, 235501 (2002).

 \( ^{17} \)  L. Marques, L. Pelaz, J. Hernandez, J. Barbolla, and G. H. Gilmer, Phys. Rev. B 64, 045214 (2001).

 \( ^{18} \)  J. Kim, F. Kirchhoff, J. Watkins, and F. S. Khan, Phys. Rev. Lett. 84, 503 (2000).

 \( ^{19} \)  C. Z. Wang, C. T. Chan, and K. M. Ho, Phys. Rev. Lett.
 

66, 189 (1991).

 \( ^{20} \)  M. Tang, L. Colombo, J. Zhu, and T. D. de la Rubia, Phys. Rev. Lett. 55, 14279 (1997).

 \( ^{21} \)  W. K. Leung, R. J. Needs, and G. Rajogopal, Phys. Rev. Lett. 83, 2351 (1999).

 \( ^{22} \)  S. K. Estreicher, Phys. Stat. sol. (b) 217, 513 (2000).

 \( ^{23} \)  G. Henkelman, B. Uberuaga, S. Dunham, and H. Jónsson, Phys. Stat. sol. (b) 233, 24 (2002).

 \( ^{24} \)  L. J. Munro and D. Wales, Phys. Rev. B 59, 3969 (1999).

 \( ^{25} \)  M. J. Puska, Comp. Mat. Sc. 17, 365 (2000).

 \( ^{26} \)  J. L. Mercer, J. S. Nelson, A. F. Wright, and E. B. Stechel, Modelling. Simul. Mater. Sci. Eng. 6, 1 (1998).

 \( ^{27} \)  M. I. J. Probert and M. C. Payne, Phys. Rev. B 67, 075204 (2003).

 \( ^{28} \)  G. Henkelman, B. P. Uberuaga, and H. Jónsson, J. Chem. Phys. 113, 9901 (2000).

 \( ^{29} \)  M. A. Roberson and S. K. Estreicher, Phys. Rev. B 49, 17040 (1994).

 \( ^{30} \)  S. Öğüt, H. Kim, and J. Chelikowsky, Phys. Rev. B 56, R11 353 (1997).

 \( ^{31} \)  F. Anderson, F. S. Ham, and G. Grossmann, Phys. Rev. B 53, 7205 (1996).

 \( ^{32} \)  S. J. Clarck and G. J. Ackland, Phys. Rev. B 56, 47 (1997).

 \( ^{33} \)  J. Lento and R. M. Nieminen, J. Phys.: Condens. Matter 15, 4387 (2003).

 \( ^{34} \)  F. Agullo-Lopez, C. Catlow, and P. Townsend, Point Defects in Materials (Academic Press, 1988).

 \( ^{35} \)  D. Maroudas and R. A. Brown, Phys. Rev. B 47, 15562 (1993).

 \( ^{36} \)  N. Mousseau and G. T. Barkema, Phys. Rev. E 57, 2419 (1998).

 \( ^{37} \)  G. T. Barkema and N. Mousseau, Phys. Rev. Lett. 77, 4358 (1996).

 \( ^{38} \)  D. Sánchez-Portal, P. Ordejón, E. Artacho, and J. M. Soler, Int. J. Quant. Chem. 65, 453 (1997).

 \( ^{39} \)  J. M. Soler, E. Artacho, J. Gale, A. García, J. Junquera,

and P. Ordejón, J. Phys. Condens. Matter 14, 2745 (2002).

 \( ^{40} \)  R. Malek and N. Mousseau, Phys. Rev. E 62, 7723 (2000).

 \( ^{41} \)  G. Henkelman and J. Jónsson, J. Chem. Phys. 111, 7010 (1999).

 \( ^{42} \)  G. Kresse and J. Hafner, Phys. Rev. B 47, 558 (1993).

 \( ^{43} \)  C. Lanczós, Applied Analysis (Dover, New York, 1988).

 \( ^{44} \)  N. Troullier and J. L. Martins, Phys. Rev. B 43, 1993 (1991).

 \( ^{45} \)  L. Kleiman and D. M. Bylander, Phys. Rev. Lett. 48, 1425 (1982).

 \( ^{46} \)  E. Anglada, J. M. Soler, J. Junquera, and E. Artacho, Phys. Rev. B 66, 205101 (2002).

 \( ^{47} \)  H. J. Monkhorst and J. D. Pack, Phys. Rev. B 13, 5188 (1976).

 \( ^{48} \)  D. M. Ceperley and B. J. Alder, Phys. Rev. Lett. 45, 566 (1980).

 \( ^{49} \)  J. P. Perdew and A. Zunger, Phys. Rev. B 23, 5048 (1981).

 \( ^{50} \)  J. Bourgoin and M. Lanoo, Point defects is Semiconductors I and II (Springer, Berlin, 1981).

 \( ^{51} \)  P. Kelly and R. Car, Phys. Rev. B 45, 6543 (1992).

 \( ^{52} \)  P. Blöchl, E. Smargiassi, R. Car, D. B. Laks, W. Andreoni, and S. Pantelides, Phys. Rev. Lett. 70, 2435 (1993).

 \( ^{53} \)  H. Vineyard, J. Phys. Chem. Solids 3, 121 (1957).

 \( ^{54} \)  M. I. Baskes, J. S. Nelson, and A. F. Wright, Phys. Rev. B 40, 6085 (1989).

 \( ^{55} \)  H. Bracht, E. E. Haller, and R. Clark-Phelps, Phys. Rev. Lett. 81, 393 (1998).

 \( ^{56} \)  T. Y. Tan and U. Gösele, Appl. Phys. A: Solids Surf. 37, 1 (1985).

 \( ^{57} \)  R. Phillips, crystals, Defects and Microstructures, Modelling a cross Scales (Cambridge university press, 2001).

 \( ^{58} \)  F. Wooten, K. Winer, and D. Weaire, Phys. Rev. Lett. 54, 1392 (1985).

 \( ^{59} \)  F. Cargnoni, C. Gatti, and L. Colombo, Phys. Rev. B 57, 170 (1998).
 
