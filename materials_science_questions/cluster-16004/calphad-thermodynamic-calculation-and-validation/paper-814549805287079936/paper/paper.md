# Automating impurity-enhanced antiphase boundary energy calculations from ab initio Monte Carlo

R. Sun*, A. van de Walle

School of Engineering, Brown University, Providence, RI 02912, United States

---

## ARTICLE INFO

**Article history:**
Received 9 February 2016
Accepted 24 February 2016

**Keywords:**
Antiphase boundary
Cluster expansion
Monte Carlo
Ab initio calculation

---

## ABSTRACT

The effect of impurities on antiphase boundary (APB) energies is studied using cluster expansion and Monte Carlo (MC) techniques from first-principles total-energy calculations. We present a code that automates the generation of APB structures for MC sampling within the Alloy Theoretic Automated Toolkit software package. The functionalities of the code is demonstrated by a case study on Ni₃Al with Ti impurities.

© 2016 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

---

## 1. Introduction

An antiphase boundary (APB) is a planar defect in a crystalline material that can be created by the motion of a dislocation along the slip plane. The word antiphase derives from the $180^\circ$ phase change in the concentration wave across the APB. Various aspects of APBs have been recently investigated from first-principles computational methods: modeling of diffuse [1] and thermally equilibrated APB [2], mechanical stability of APB [3], effects of magnetism [4], partial ordering [5], and ternary additions [6] on the APB energy. The planar defect energy of an APB is an important quantity that gives a measure of the resistance to dislocation motion: a lower APB energy on a certain slip plane implies that dislocation motion is more likely to occur along that plane than on a plane with a higher APB energy. Therefore, enhancing the APB energy is a viable strategy for strengthening. One possible way to achieve this is through the addition of impurity solutes. The substitution of host atoms by impurities leads to a change in the local stress field and, in most cases, an increase in the APB energy. From a first-principles computational approach, while it is relatively simple to obtain the APB energy of a single configuration of a pure material, an accurate modeling of the effect of impurities on the APB energy poses several challenges:

1. Impurities cannot be placed a priori only at the nearest layers to an APB because such a structural model is not physical. Even if one were able to prepare such a sample experimentally, a dislocation could still avoid the energetically unfavorable layer.
2. As a result, many configurations of impurities and possible antisite defects within the host must be considered.
3. To study the effect of low impurity concentrations, a large number of atoms needs to be included.
4. For physical applications, the behavior at high temperatures may be relevant. However, a single total-energy calculation is performed at 0 K.

Therefore, to accurately sample the APB energy with low impurity concentration, one would need to compute the total energy of many structures that each contains thousands of atoms, which is not feasible from a brute-force first-principles approach. To tackle this problem, we present a method that is based on cluster expansion and Monte Carlo. In particular, the unequilibrated APB is investigated since it represents the instantaneous energy cost for bond breaking along the slip plane, and atomic diffusion for compositional rearrangement, which is required to form an equilibrated APB, is assumed to be slow [2]. The code is included in the Alloy Theoretic Automated Toolkit (ATAT).

## 2. Theoretical overview

The workflow of computing APB energies with impurities is shown in Fig. 1, which consists of four steps: density-functional theory (DFT) total-energy calculation, cluster expansion (CE), Monte Carlo (MC), and obtaining the APB energy. The details of each step is presented in the following subsections.

### 2.1. Density-functional theory

The first step is to compute the total energy of a few dozen structures that have the same crystal structure as the host material

---

*Corresponding author.
E-mail address: ruoshi@alum.mit.edu (R. Sun).

http://dx.doi.org/10.1016/j.calphad.2016.02.005
0364-5916/© 2016 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

![](./images/814549805287079936_1.jpg)
![](./images/814549805287079936_2.jpg)
![](./images/814549805287079936_3.jpg)

![](./images/814549805287079936_4.jpg)

Fig. 1. Workflow of computing APB energies. The names of various codes used in this work are enclosed in brackets. The mmaps, memc2, and apb codes are contained in ATAT.

from density-functional theory [7,8]. Sometimes a structure can relax so far away from its unrelaxed counterpart that it becomes questionable whether the structure should be mapped onto the assumed underlying lattice. This problem can often be mitigated by performing relaxations under a constant cell shape while al- lowing the ionic positions to relax freely and the cell volume to relax isotropically. These constraints can be implemented within the Vienna Ab initio Simulation Package (VASP) [9-12] by editing the code. (See Appendix for details.) A general solution to this is- sue, based on an analysis of the curvature of the energy surface in phase space, has been suggested in Ref. [13].

Structures can be automatically generated by the mmaps com- mand in the Alloy Theoretic Automated Toolkit (ATAT) with multi- component additions [14,15]. Since an APB can only exist in ma- terials with at least 2 elements, it is necessary to use the multi- component version when impurity atoms are present.

Subsequent steps involve various commands in ATAT.

### 2.2. Cluster expansion
Next, a cluster expansion is performed to express the total energy as a linear combination of occupation variables:

$$
E(\sigma)=\sum_{\alpha} m_{\alpha} J_{\alpha} \rho_{\alpha}(\sigma), \tag{1}
$$

where $\alpha$ is a cluster, $m_{\alpha}$ the multiplicity of the cluster $\alpha$ by sym metry, $J_{\alpha}$ the effective cluster interaction (ECI), and $\rho_{\alpha}(\sigma)$ the cluster correlation function conveniently chosen to form an or- thonormal basis [16]. The goodness of fit is indicated by the cross- validation (CV) score:

$$
\mathrm{CV}=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(E_{i}-\hat{E}_{i}\right)^{2}}, \tag{2}
$$

where $n$ is the total number of fitting structures, $E_{i}$ the calculated energy of structure $i$, and $\hat{E}_{i}$ the predicted energy of structure $i$ from the least-squares fit to the $n-1$ other energies.

This step is also performed using mmaps.

### 2.3. Monte Carlo
The initial structure is oriented such that the cross product of the first two translation vectors $\mathbf{T}_{1} \times \mathbf{T}_{2}$ defines the slip plane. Figure 2 shows the necessity for this re-orientation procedure. Assuming periodic boundary conditions on the left and right sides of the cell, multiple images of the APB are needed to construct such a structure. [Except for low index surfaces such as (11) in Fig. 2.] It is obvious that at least two APBs are formed per cell and that the minimal case is guaranteed by the correct orientation.

![](./images/814549805287079936_5.jpg)

Fig. 2. Schematic of an APB structure (APB in dotted lines) under periodic boundary conditions (bold lines). For clarity, periodic boundary conditions are imposed on the left and right sides only. (a) An impossible structure. (b) Due to periodic boundary conditions, multiple images of the APB must be mapped back into the cell.

To obey the laws of statistical thermodynamics, Monte Carlo sampling is performed using the metropolis algorithm. When a configuration $\sigma$ is modified into $\sigma^{\prime}$, the associated energy differ ence, denoted as $\Delta E_{\sigma \to \sigma^{\prime}}$, can be conveniently obtained through the ECIs. If $\Delta E_{\sigma \to \sigma^{\prime}} \leq 0$, the new configuration is accepted. Otherwise, it is accepted with probability $\exp \left(-\beta \Delta E_{\sigma \to \sigma^{\prime}}\right)$.

The standard error of the mean is given by $s / \sqrt{N}$, where $s$ is the sample standard deviation and $N$ the number of averaging passes, assuming the snapshot energies are uncorrelated (i.e., sufficiently distant in time). At convergence, it is necessary that the standard error be within the desired accuracy [e.g., $O(0.1)$ mJ/m² for planar defect energies]. Correlation can be verified by the block averaging method as described in Ref. [17]. Typically, a few thousand passes are needed to reach convergence.

The memc2 command is used in this step.

### 2.4. APB energy
For each structure generated from metropolis Monte Carlo, with total energy $E_{0}$, the APB structure is created by duplicating the original structure along $\mathbf{T}_{3}$ and translating the upper half of the supercell by the slip vector. The total energy of the defective structure is denoted as $E$.

The APB energy is given by

$$
\gamma=\frac{E-2 E_{0}}{2\left\|\mathbf{T}_{1} \times \mathbf{T}_{2}\right\|}=\frac{N\left(e-e_{0}\right)}{\left\|\mathbf{T}_{1} \times \mathbf{T}_{2}\right\|}, \tag{3}
$$

where $N$ is the total number of atoms, and $e_{0}$ and $e$ are in units of energy per atom. The APB energy obtained this way is called the unequilibrated APB energy, with a step function order parameter profile across the APB [2].

## 3. The apb code
To streamline the process of performing MC and calculating APB energies as described in the previous section, we have de- veloped the apb code in C++ within the ATAT software package. Here we provide a working example of the binary alloy host ma- terial $Ni_{3} Al$ with Ti impurities to illustrate the features of the code and the specific procedure.

### 3.1. Setting up input structure files
Before creating an APB, the user needs to set up the lattice file and structure file such that the structure is correctly oriented into the relevant slip plane. Using the face-centered cubic (fcc) $Ni_{3} Al$ as an example, the first three lines in the lat.in and str.out files should be:

```
 a 0 0
 0 a 0
 0 0 a
```

where $a$ is the lattice constant. The next three lines of these structure files define the translation vectors. For the conventional fcc unit cell, they are simply

```
 1 0 0
 0 1 0
 0 0 1
```

In the (1 1 1) orientation, the cell defined by the vectors

```
-1  0 -1
 0 -1  1
 1  1  1
```

is 3 times the volume of the conventional cell. Translation vectors $\mathbf{T}_{1}$ and $\mathbf{T}_{2}$ are the shortest linearly independent lattice vectors that lie on the (1 1 1) slip plane. The third translation vector $\mathbf{T}_{3}$ is typically chosen to be perpendicular to the plane. It should be noted that the orthogonality condition is unnecessary and, in fact, cannot be guaranteed for non-cubic systems. The remainder of the `lat.in` is:

```
 1.000000      1.000000      1.000000      Ni,Al,Ti
 0.000000     -0.500000      0.500000      Ni,Al,Ti
-0.500000      0.000000      0.500000      Ni,Al,Ti
-0.500000     -0.500000      1.000000      Ni,Al,Ti
 0.500000      0.000000      0.500000      Ni,Al,Ti
 0.500000     -0.500000      1.000000      Ni,Al,Ti
 0.000000      0.000000      1.000000      Ni,Al,Ti
 0.000000     -0.500000      1.500000      Ni,Al,Ti
 1.000000      0.000000      1.500000      Ni,Al,Ti
 1.000000     -0.500000      1.500000      Ni,Al,Ti
 0.500000      0.000000      2.000000      Ni,Al,Ti
 0.500000     -0.500000      2.000000      Ni,Al,Ti
```

where the fourth entry defines the possible atomic species for that occupancy. The configuration here allows for disordering at every lattice site. Note that the user can first create a simple supercell with the correct volume ratio using the `cellcvrt -uss` command and then map all atoms into the defined cell using the `cellcvrt -wi` command. Supercells of this minimal cell in the (1 1 1) orientation can now be generated. A specific configuration of atomic positions is written in the `str.out` file, where the fourth entry on each line should be either Ni, Al, or Ti. Here we choose a $6 \times 6 \times 5$ cell with 2160 atoms so that the APBs are sufficiently separated apart from each other and that a wide range of impurity concentrations can be studied.

### 3.2. Creating an APB

An APB is uniquely defined by its slip plane $(hkl)$ and slip vector [uvw]. To study the $\left\langle 0 \frac{1}{2} \frac{1}{2}\right\rangle\{111\}$ APB of $\mathrm{Ni}_{3} \mathrm{Al}$, we conveniently choose $\left[0 \frac{1}{2} \frac{1}{2}\right]$ as the slip vector, which is parallel to $\mathbf{T}_{2}$. To create an APB, the user executes the following command:

```
apb -1=lat.in -s=str.out -sx=0
   -sy=-0.5 -sz=0.5 -f
```

The lattice file is specified through the `-1` flag, structure file through the `-s` flag, and the $x$-, $y$-, and $z$-component of the slip vector through the `-sx`, `-sy`, and `-sz` flags, respectively. The code then writes the APB structure by duplicating the atomic positions along $\mathbf{T}_{3}$ and translating the duplicated atoms by the slip vector. The file name of the output structure is by default `str_apb.out`, but can be customized through the `-o` flag. The `-f` flag in the above command indicates that the code exits immediately after writing the APB structure. The omission of this flag allows the code to compute the APB energy, as described next.

### 3.3. Calculating the APB energy

The APB energy, defined by Eq. (3), is calculated from a cluster expansion. The `apb` code checks if the `clusters.out` and `eci.out` files are present in the current working directory and exits if not. The total energy is obtained through the `memc2` code. Specifically, the command

```
memc2   -is=str.out    -n=0    -eq=0    -g2c    -q
```

is executed, where the `-g2c` flag specifies a canonical ensemble instead of the default grand canonical ensemble. The total energy quantity, $E_{\mathrm{mc}}$, is read from the output `mc.out` file. The above procedure is performed for both the defect-free structure and the defective structure to yield the quantities $e_{0}$ and $e$, respectively, in Eq. (3). The total number of atoms and the cross-sectional area of the supercell are also easily obtained. Hence, all the necessary quantities are now available to compute the APB energy.

### 3.4. Monte Carlo sampling of the APB energy

A MC simulation can be performed automatically through the `-mc` flag in the `apb` code. The essential parameters are the number of equilibration passes (`-eq`), the number of averaging passes (`-n`),

![](./images/814549805287079936_6.jpg)

![](./images/814549805287079936_7.jpg)

Fig. 3. Effective cluster interaction $J$ as a function of cluster diameter $d$ normalized by the nearest neighbor distance $d_{\mathrm{nn}}$ for (a) Ni-Al and (b) Ni-Al-Ti systems.
```

and temperature (-T). The code calls memc2 to perform the MC simulation and produces snapshots of the output structure through the -opss flag. Typically, a few thousand passes are sufficient to reach convergence and, therefore, the file name of the accepted configurations is of the form str????.out, where the question marks are 4-digit numbers. The associated structure with APBs is written to str????_apb.out. After the MC simulation is complete, the code computes the APB energy for all the structures and writes the output to gamma_apb.out, whose name can be customized by the -og flag.

![](./images/814549805287079936_8.jpg)

Fig. 4. Effect of 0.1%, 1%, and 10% Ti on the mean APB energy of Ni₃Al as a function of temperature. Error bars represent the standard error of the mean APB energy, which is insignificant compared to the size of the data point.

It is straightforward to calculate the mean APB energy and the standard error of the mean.

### 4. Method
We use Ni₃Al with Ti impurities as an example. DFT calculations were performed within the Perdew-Burke-Ernzerhof (PBE) [18,19] generalized gradient approximation (GGA) using projector augmented wave (PAW) potentials [20,21] with a plane-wave cutoff energy of 368 eV. Spin polarization was applied to Ni atoms since it is shown to be important for the phase stability of the Ni-Al system [22]. Total energies were converged to within $10^{-6}$ and $10^{-4}$ eV for each self-consistent loop and ionic relaxation step, respectively, using 4000 Monkhorst-Pack k-points [23] per reciprocal atom. Each structure was relaxed twice, followed by a static calculation using the tetrahedron method with Blöchl corrections [24].

For the cluster expansion step, 71 structures were considered in the Ni-Al binary system and an additional 71 structures in the Ni-Al-Ti ternary system. In the Monte Carlo simulation, 1000 equilibration steps and 2500 averaging steps were used.

### 5. Results and discussion
The computed equilibrium lattice constant of Ni₃Al is 3.570 Å, in good agreement with experiment [25]. The ECIs for the binary Ni-Al and ternary Ni-Al-Ti systems are plotted as a function of the cluster diameter in Fig. 3, where the CV score is 23.6 meV and 30.4 meV, respectively. The APB energy of pure Ni₃Al obtained from cluster expansion is 318 mJ/m², which is comparable to the value of 300 mJ/m² obtained from an unrelaxed first-principles calculation in Ref. [5].

The effect of impurities on the APB energy can be expressed as $\Delta \gamma(x) = \gamma(x) - \gamma(0)$, where $x$ is the impurity concentration. For

![](./images/814549805287079936_9.jpg)

Fig. 5. Top row: Change in APB energy as a function of the Monte Carlo trajectory for (a) 0.1% Ti and (b) 1% Ti, both at 400 K. Bottom row: Corresponding running average of the change in APB energy for (c) 0.1% Ti and (d) 1% Ti. In (a), although many structures are symmetrically distinct, their APB energies are degenerate because the clusters are relatively local in a practical cluster expansion.

error cancellation, the ECIs for the ternary system is used to compute the APB energy of the binary. The change in the APB energy is plotted as a function of temperature from 400 K to 1600 K in Fig. 4. At 0.1 at %, the increase in the APB energy is negligible. At 1 at %, the APB energy rises by about $10\ \text{mJ/m}^2$ compared to the pure host. The maximum enhancement is achieved at 10 at % at low temperature, where $\Delta\gamma$ is above $60\ \text{mJ/m}^2$. A decline in the enhancement is observed as temperature increases. This is expected due to the counter-effect of disordering, which is more prominent at higher temperatures. Figure 4 clearly illustrates the fact that zero-temperature APB energies can be seriously misleading.

Although we have demonstrated the capability of studying the effect of a wide range of impurity concentrations on the APB energy, one must be cautious about calculations at extremely low impurity concentrations. For instance, at 0.1% impurity concentration, the supercell only contains 2 impurity atoms. While combinatorics shows that there are still many unique configurations, i.e., $\binom{2160}{2}$ reduced by a factor of symmetry, most of their APB energies are nearly degenerate due to the local nature of the clusters. This is demonstrated in Fig. 5, where degenerate bands are clearly present in the 0.1% case but not in the 1% case.

Finally, we remark that the code does not impose any restrictions on the input slip vectors. It can readily be used for generalized stacking faults in addition to APBs. Although the CE method cannot be applied directly to obtain the interfacial energy and $ab$ initio methods must be used instead, the CE is still useful to generate equilibrium solution configurations prior to interface formation.

## 6. Conclusions

We have developed the `apb` code that automates the process of APB structure generation and APB energy calculation via Monte Carlo sampling, based on the cluster expansion formalism. A case study on $\text{Ni}_3\text{Al}$ with Ti impurities shows that 10% Ti addition can increase the APB energy by over $60\ \text{mJ/m}^2$ compared to pure $\text{Ni}_3\text{Al}$. The code has been incorporated to the `atat` software package, and can be readily used to study other types of planar defects.

## Acknowledgments

This work was supported by the Air Force Research Laboratory via UES, Inc. award numbers 901-1D2-0001 and S-992-009-004. Computational resources were provided by the Center for Computation and Visualization at Brown University and the Extreme Science and Engineering Discovery Environment (XSEDE) from the National Science Foundation under grant number ACI-1053575.

## Appendix A. Constant cell shape relaxation in `vasp`

In the source file `main.F`, insert `.OR. DYN%ISIF==8` to the cases `DYN%ISIF < 5` and `DYN%ISIF==7`. Set `ISIF=8` in the `INCAR` file.

## References

[1] A. Walle, M. Asta, First-principles investigation of perfect and diffuse anti-phase boundaries in HCP-based Ti-Al alloys, Metall. Mater. Trans. A 33 (13) (2002) 735-741, http://dx.doi.org/10.1007/s11661-002-0139-9.

[2] M. Asta, A.A. Quong, The concentration and temperature dependences of an-tiphase-boundary energies in $\gamma$-TiAl: a first-principles study, Philos. Mag. Lett. 76 (5) (1997) 331-340, http://dx.doi.org/10.1080/095008397178931.

[3] J. Ehmann, M. Fähnle, Generalized stacking-fault energies for TiAl: mechanical instability of the (111) antiphase boundary, Philos. Mag. A 77 (3) (1998) 701-714, http://dx.doi.org/10.1080/01418619808224078.

[4] V.R. Manga, J.E. Saal, Y. Wang, V.H. Crespi, Z.-K. Liu, Magnetic perturbation and associated energies of the antiphase boundaries in ordered $\text{Ni}_3\text{Al}$, J. Appl. Phys. 108, 103509 (2010), http://dx.doi.org/10.1063/1.3513988.

[5] M. Sluiter, Y. Hashi, Y. Kawazoe, The effect of segregation and partial order on the thermodynamics of (1 1 1) antiphase boundaries in $\text{Ni}_3\text{Al}$, Comput. Mater. Sci. 14 (1-4) (1999) 283-290, http://dx.doi.org/10.1016/S0927-0256(98)00120-7.

[6] C. Woodward, J. MacLaren, Planar fault energies and sessile dislocation configurations in substitutionally disordered Ti-Al with Nb and Cr ternary additions, Philos. Mag. A 74 (2) (1996) 337-357, http://dx.doi.org/10.1080/01418619608242147.

[7] P. Hohenberg, W. Kohn, Inhomogeneous electron gas, Phys. Rev. 136 (3B) (1964) B864-B871, http://dx.doi.org/10.1103/PhysRev.136.B864.

[8] W. Kohn, L.J. Sham, Self-consistent equations including exchange and correlation effects, Phys. Rev. 140 (4A) (1965) A1133-A1138, http://dx.doi.org/10.1103/PhysRev.140.A1133.

[9] G. Kresse, J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47 (1993) 558, http://dx.doi.org/10.1103/PhysRevB.47.558.

[10] G. Kresse, J. Hafner, Ab initio molecular-dynamics simulation of the liquid-metal-amorphous-semiconductor transition in germanium, Phys. Rev. B 49 (1994) 14251, http://dx.doi.org/10.1103/PhysRevB.49.14251.

[11] G. Kresse, J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, Phys. Rev. B 54 (16) (1996) 11169-11186, http://dx.doi.org/10.1103/PhysRevB.54.11169.

[12] G. Kresse, J. Furthmüller, Efficiency of ab initio total energy calculations for metals and semiconductors using a plane-wave basis set, Comput. Mater. Sci. 6 (1) (1996) 15-50, http://dx.doi.org/10.1016/0927-0256(96)00008-0.

[13] A. van de Walle, Q. Hong, S. Kadkhodaei, R. Sun, The free energy of mechanically unstable phases, Nat. Commun. 6 (2015) 7559, http://dx.doi.org/10.1038/ncomms8559.

[14] A. van de Walle, M. Asta, G. Ceder, The alloy theoretic automated toolkit: a user guide, Calphad 26 (4) (2002) 539-553, http://dx.doi.org/10.1016/S0364-5916(02)80006-2.

[15] A. van de Walle, Multicomponent multisublattice alloys, nonconfigurational entropy and other additions to the alloy theoretic automated toolkit, Calphad 33 (2) (2009) 266-278, http://dx.doi.org/10.1016/j.calphad.2008.12.005.

[16] J. Sanchez, F. Ducastelle, D. Gratias, Generalized cluster description of multicomponent systems, Physica A 128 (1-2) (1984) 334-350, http://dx.doi.org/10.1016/0378-4371(84)90096-7.

[17] D. Frenkel, B. Smit, Understanding Molecular Simulation: From Algorithms to Applications, 2nd edition, Academic Press, San Diego, 2001.

[18] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77 (1996) 3865, http://dx.doi.org/10.1103/PhysRevLett.77.3865.

[19] J.P. Perdew, K. Burke, M. Ernzerhof, Erratum: generalized gradient approximation made simple, Phys. Rev. Lett. 78 (1997) 1396, http://dx.doi.org/10.1103/PhysRevLett.78.1396.

[20] P.E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50 (1994) 17953, http://dx.doi.org/10.1103/PhysRevB.50.17953.

[21] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Phys. Rev. B 59 (1999) 1758, http://dx.doi.org/10.1103/PhysRevB.59.1758.

[22] C. Wolverton, A. Zunger, Magnetic destabilization of $\text{Ni}_7\text{Al}$, Phys. Rev. B 59 (1999) 12165-12168, http://dx.doi.org/10.1103/PhysRevB.59.12165.

[23] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations, Phys. Rev. B 13 (12) (1976) 5188-5192, http://dx.doi.org/10.1103/PhysRevB.13.5188.

[24] P.E. Blöchl, O. Jepsen, O.K. Andersen, Improved tetrahedron method for Brillouin-zone integrations, Phys. Rev. B 49 (1994) 16223-16233, http://dx.doi.org/10.1103/PhysRevB.49.16223.

[25] F.X. Kayser, C. Stassis, The elastic constants of $\text{Ni}_3\text{Al}$ at 0 and 23.5 °C, Phys. Status Solidi A 64 (1) (1981) 335-342, http://dx.doi.org/10.1002/pssa.2210640136.