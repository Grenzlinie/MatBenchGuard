PHYSICAL REVIEW RESEARCH 6, 023253 (2024)

# Spatial distribution of local elastic moduli in nanocrystalline metals

Menahem Krief* and Yinon Ashkenazy
Racah Institute of Physics, The Hebrew University, 9190401 Jerusalem, Israel

![](./images/1006014889635872775_1.jpg)
(Received 16 November 2023; revised 27 March 2024; accepted 2 May 2024; published 6 June 2024)

Elastoplastic properties of nanocrystalline metals are nonuniform on the scale of the grain size, and this nonuniformity affects macroscopic quantities as, in these systems, a significant part of the material is at or adjacent to a grain boundary. We use molecular dynamics simulations to study the spatial distributions of local elastic moduli in nanograined pure metals and analyze their dependence on grain size. Calculations are performed for copper and tantalum with grain sizes ranging from 5 to 20 nm. Shear-modulus distributions for grain and grain-boundary atoms were calculated. It is shown that the noncrystalline grain boundary has a wide shear-modulus distribution, which is grain-size independent, while grains have a peaked distribution, which becomes sharper with increasing grain size. Average elastic moduli of the bulk, grains, and grain boundary are calculated as a function of grain size. The atomistic simulations show that the reduction of total elastic moduli with decreasing grain size is mainly due to a resulting larger grain-boundary atoms fraction, and that the total elastic moduli can be approximated by a simple weighted average of larger grain elastic moduli and a lower grain-boundary elastic moduli.

DOI: 10.1103/PhysRevResearch.6.023253

## I. INTRODUCTION

Understanding the elastic properties of metals plays a key role in the analysis and modeling of the response to defor- mation under varying conditions. The local elastic properties in polycrystalline metals depend on the local structure, which varies from crystalline to grain boundaries and heterophase interfaces [1–8]. The local variation of elastic properties plays a key role in tailoring of the macroscopic effective material properties, specifically in cases where grain refinement is used [6]. Similarly, local properties control strengthening in com- posite materials, whether produced by additive manufacturing [9] or via self-organized segregation (e.g., [10]), as well as in developing models for structure evolution [11]. In order to develop an understanding of global response functions for composite materials, it is necessary to describe detailed dis- tributions of local properties in addition to global averages. Since local elastic properties are not accessible experimentally for a wide range of systems, it is beneficial to study surrogate model systems, which allow reliable numerical evaluation of these. Such simulations play a key role in developing effective models for composite materials.

In Ref. [12] we demonstrated the feasibility, robustness, and accuracy of calculating bulk elastic constants using molecular dynamics simulations in the NVT ensemble (where the number of particles, volume, and temperature are kept constant). This method is generalized in this work to include the calculation of local elastic properties. The main advantage of this approach is that all components of the elasticity tensor are obtained in a single consistent molecular-dynamics simu- lation as opposed to the standard explicit deformation method, which requires several simulations under different deforma- tions and is limited to evaluating global average values. Using NVT local evaluators, calculations are inherently local and immediate, so localized averaging leading to spatial and tem- poral distributions is trivial. In addition, while special care needs to be taken in the direct drive method to avoid strain-rate and defect formation effects, the NVT local evaluation does not rely on forcing deformation. It thus is not affected by these potential problems. Moreover, in the standard deformation method, a non-negligible deformation of the simulation box is required in order to create a measurable variation in local stress. In inhomogeneous systems where elastic properties vary locally, such deformations lead to strain localization, which in many cases results in local yield [7,13] that prevents the calculation of elastic moduli.

Previously, direct calculations of local elastic constants by atomistic simulations were performed in Refs. [14,15] for copper and gold, in Refs. [16,17] for amorphous polymeric glasses, in Ref. [18] for a lipid bilayer, and in Ref. [19] for ionic liquids. In Ref. [20] an experimental correlative approach was used to extract the local elastic properties of titanium.

In this paper we present and analyze the distribution of lo- cal elastic constants in nanocrystalline copper and tantalum, as calculated using molecular dynamics simulations employing realistic many-body potentials. We extract the distributions of elastic moduli within polycrystalline systems and study their dependence on grain size in the range of 5–20 nm. In addition, we study the grain-size dependence of the average

*menahem.krief@mail.huji.ac.il

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article’s title, journal citation, and DOI.

2643-1564/2024/6(2)/023253(8)
023253-1
Published by the American Physical Society

elastic moduli of the total system, in grains and grain boundary, and show explicitly that average global values agree with mean-field models that were used in the literature [21–26]. We note that existing models for the calculation of grain-boundary elastic properties of nanocrystalline metals usually rely on such effective mean-field models, which assume a grain-size- independent grain-boundary moduli [27]. Such methods only allow the calculation of global averages. The method which we employ in this work gives a direct evaluation of local elastic properties without relying on some of the major as- sumptions which were previously made, i.e., the description of the elastic properties of the grain-boundary atoms using a single average value, or the independence of local properties on interface curvature. The method enables the calculation of new observables such as the distributions of elastic properties, which can play a crucial role in developing stochastic models addressing the response under nondeterministic drive condi- tions [11,28].

## II. LOCAL ELASTICITY

In this section we outline the method for the calculation of local elastic constants using molecular dynamics simulations in the NVT ensemble.

It was shown in previous works [12,15,16,18,29–34] that in the NVT ensemble the elasticity tensor can be written as a sum of three contributions: (i) a purely configurational part known as the Born term, which is given by a canonical average of the second-order derivative of the potential energy with respect to the Lagrangian strain tensor, (ii) a stress fluctuation term that vanishes at zero temperature, and (iii) a kinetic ideal gas contribution, which also vanishes at zero temperature. As a result, the low-temperature limit for the total elasticity tensor can be written on a per-atom basis [34,35] in the form

$$
C_{\alpha \beta \gamma \delta}=\left\langle\frac{1}{V} \sum_{i} V_{i} C_{i, \alpha \beta \gamma \delta}^{B}\right\rangle,
\tag{1}
$$

where $\alpha, \beta, \gamma, \delta$ are the directional tensor indices, $\langle\cdot\rangle$ repre sents ensemble average, $C_{i, \alpha \beta \gamma \delta}^{B}$ is the local, per-atom Born elasticity tensor, $V$ is the total system volume, and $V_{i}$ is the volume of atom $i$, defined such that $V=\sum_{i} V_{i}$. Following Refs. [34,35], we define the local volume of a specific atom as the volume of the Voronoi cell associated with it. In this work calculations were performed for copper and tantalum, mod- eled by embedded-atom-model (EAM) potentials [36]. These potentials are defined by a pair potential function $v=v(r)$, an embedding function $F=F(\rho)$, and a local density function $\rho=\rho(r)$, so that the potential energy takes the form

$$
E\left(\boldsymbol{r}_{1}, \ldots, \boldsymbol{r}_{N}\right)=\sum_{i} F\left(\rho_{i}\right)+\sum_{i<j} v\left(r_{i j}\right),
\tag{2}
$$

where $\boldsymbol{r}_{i}$ is the position of atom $i$, $r_{i j}=\boldsymbol{r}_{i}-\boldsymbol{r}_{j}$, and $\rho_{i}=$ $\sum_{j \neq i} \rho(r_{i j})$ is the density around atom $i$. It can be shown that for an EAM potential, the per-atom Born elasticity tensor takes the form [12,15,30,34,37,38]

$$
V_{i} C_{i, \alpha \beta \gamma \delta}^{B}=\frac{1}{2} \sum_{j \neq i} X_{i j} \frac{r_{i j, \alpha} r_{i j, \beta} r_{i j, \gamma} r_{i j, \delta}}{r_{i j}^{2}}+F^{\prime \prime}\left(\rho_{i}\right) g_{i, \alpha \beta} g_{i, \gamma \delta},
\tag{3}
$$

where

$$
\begin{aligned}
X_{i j} & =v^{\prime \prime}\left(r_{i j}\right)-\frac{1}{r_{i j}} v^{\prime}\left(r_{i j}\right) \\
& +\left(F^{\prime}\left(\rho_{i}\right)+F^{\prime}\left(\rho_{j}\right)\right)\left(\rho^{\prime \prime}\left(r_{i j}\right)-\frac{1}{r_{i j}} \rho^{\prime}\left(r_{i j}\right)\right),
\end{aligned}
\tag{4}
$$

and

$$
g_{i, \alpha \beta}=\sum_{j \neq i} \rho^{\prime}\left(r_{i j}\right) \frac{r_{i j, \alpha} r_{i j, \beta}}{r_{i j}}.
\tag{5}
$$

Various local elastic moduli can be obtained directly from the local elasticity tensor (3) by employing local Voigt averages [39–41], which results in the following expressions for the local bulk modulus:

$$
9 B=C_{11}+C_{22}+C_{33}+2\left(C_{12}+C_{23}+C_{31}\right),
\tag{6}
$$

the local shear modulus:

$$
\begin{aligned}
15 G= & C_{11}+C_{22}+C_{33}-\left(C_{12}+C_{23}+C_{31}\right) \\
& +3\left(C_{44}+C_{55}+C_{66}\right),
\end{aligned}
\tag{7}
$$

the local Young's modulus:

$$
\frac{1}{E}=\frac{1}{3 G}+\frac{1}{9 B},
\tag{8}
$$

and the local Poisson's ratio:

$$
v=\frac{1}{2}\left(1-\frac{3 G}{3 B+G}\right).
\tag{9}
$$

The Voigt notation for tensor indices was used in Eqs. (6) and (7).

## III. RESULTS

Simulations were performed using the state-of-the-art molecular dynamics code LAMMPS (Large-Scale Atomic Molecular Massively Parallel Simulator) [42], to which we added a parallel implementation of the calculation of the local elasticity tensor for EAM potentials [Eqs. (3)–(5)]. Results are reported for nanocrystalline copper and tantalum with grain sizes of $d=5,8,10,12,15,18,20$ nm and a corresponding number of atoms in the range of $2 \times 10^{5}-1.5 \times 10^{7}$. Copper was simulated using EAM potential by Mishin *et al.* [43] for an fcc lattice structure with $a=3.615$ A, and tantalum was simulated using EAM potential by Ravelo *et al.* [44] for a bcc lattice with $a=3.304$ A. Initial configurations were generated by randomly assigning fcc and bcc crystallites on a grain-size superlattice and defining interfaces between grains using Voronoi tessellation. These initial configurations were relaxed using varying box-size NPT molecular dynamics sim- ulations with a target pressure of zero for a duration of 200 ps (with a 2-fs time step), as shown in Fig. 1. It is evident that as the system reaches the state of equilibrium, the instantaneous pressure oscillates indefinitely with a well-defined frequency and amplitude, while the cumulative temporal average pres- sure decays to zero. This behavior of the pressure fluctuations is expected from a molecular dynamics simulation in the NVT ensemble (as shown in detail in Ref. [12], and in the references therein).


![](./images/1006014889635872775_2.jpg)

FIG. 1. Demonstration of the equilibration process for nanocrystalline tantalum with grain size $d = 100$ nm. The box size is relaxed in the $NPT$ ensemble, until the total pressure is zero. Shown are the total instantaneous pressure (blue solid line, left $y$ axis) and the average pressure (red dashed line, right $y$ axis), which is calculated over a window of $10^4$ times steps (with a time step of 2 fs).

![](./images/1006014889635872775_3.jpg)

FIG. 2. Atomistic visualizations of simulated nanocrystalline copper (fcc, upper panes) and tantalum (bcc, lower panes), with grain sizes $d = 8$ nm (left panes), 15 nm (middle panes), and 20 nm (right panes). The corresponding box size $L$ is also listed in each pane. Color indicates the local average centrosymmetry parameter. It is evident that the number of grains is kept constant for different grain sizes.

Final relaxed configurations of several simulation boxes, visualized with OVITO [45], are shown in Fig. 2, where atom colors are assigned according to the local average centrosymmetry parameter [46,47], distinctively separating grain and grain-boundary atoms [48]. In Fig. 3 planar slices are shown with atoms colored according to the per-atom shear modulus [Eq. (7)].

It is evident that the shear modulus varies considerably within grain-boundary regions, in contrast with a significantly lower variation in the intergrain regions. This behavior is observed for all elastic moduli [defined in Eqs. (6)-(9)] and is expected due to the contrast between the amorphous and crystalline atomic arrangements. Histograms for the per-atom shear modulus of grain and grain-boundary atoms are shown in Fig. 4 for various grain sizes. The distributions for intragrain moduli have a width to average ratio of $\sim$5%, while the grain-boundary moduli distributions have a ratio close to unity. While this variation is expected, we further examined the dependence of these distributions on grain size. Here we found that while intragrain moduli distributions became sharper (lower width over mean) with increasing grain size,

![](./images/1006014889635872775_4.jpg)

FIG. 3. Atomistic view of (111) planar slices of simulated nanocrystalline copper (upper panes) and tantalum (lower panes), with grain sizes $d = 8$ nm (left panes), 15 nm (middle panes), and 20 nm (right panes). The corresponding simulation box size $L$ is also listed in each pane. The spatial distribution of the local shear modulus $G$ is indicated by color. The lack of spatial correlation between the widely distributed values within the grain-boundary atoms is evident. In contrast, deviations from the average in the grain are significantly smaller, as expected. It is also seen that the grain atoms have a larger value on average. These results are consistent with Fig. 4. We note that the parallel lines in some of the grains are due to image shading and are artificial.

such variation was not observed in grain-boundary moduli distributions. Similar behavior is observed for the stress distributions as seen in Fig. 5. We note that even though the average grain-boundary shear modulus is lower than the average grain shear modulus (as expected), it is seen in Fig. 4 that some grain-boundary local values are larger than local grain values. This is a result of the highly frustrated local amorphous configuration, which results in some grain-boundary local values that are higher than those of the ordered phase.

We now discuss the uncertainty in the results. We expect the main variation to be due to the structure of interfaces and triple junctions formed during the Voronoi tessellation process. In order to quantify this uncertainty, we divided the simulation box into eight different octants and compared the resulting moduli distributions in the various octants, which contain different grains, interfaces, and junctions. We found that the different distributions are very similar, with the average value varying up to $2\%$, which can serve as a measure of the uncertainty of the average elasticity values. This variation does not depend strongly on grain size. This is demonstrated in Fig. 6, where we compare the grain and grain-boundary shear-modulus distributions in eight different octants and in the entire simulation box, for $d = 10$ nm nanocrystalline copper.

In Fig. 7 the atomic fraction of grain and grain-boundary atoms are plotted as a function of grain size. It is evident that the grain-boundary atoms fraction has a strong decreasing dependence on grain size, as expected [48,49]. In fact, the number of grain-boundary atoms must scale as the inverse of grain size; that is, if we denote by $x_g$ and $x_{gb}$ the grain and grain-boundary atomic fractions, respectively, then

$$
x_{gb}(d)=\frac{d_0}{d}, \quad x_{g}(d)=1-\frac{d_0}{d}, \tag{10}
$$

where $d_0$ is a constant length scale that depends on the lattice symmetry and is given by $d_0 \approx \frac{n_{gb}}{n_g} \Delta_{gb}$, where $\Delta_{gb}$ is the typical grain-boundary width and $n_{gb}$, $n_g$ are, respectively, the grain and grain-boundary atom density. These results can be derived from a simplistic spherical grain-boundary model for which $x_{gb} = \frac{4\pi d^2 \Delta_{gb} n_{gb}}{\frac{4}{3}\pi d^3 n_g}$. From the data presented in Fig. 7, we find that for copper $d_0 \approx 1.5$ nm and for tantalum $d_0 \approx 1.7$ nm. The scaling law (10) is also plotted in Fig. 7, which shows that it perfectly matches the simulation values.

![](./images/1006014889635872775_5.jpg)

FIG. 4. Shear-modulus probability densities for grain and grain-boundary atoms in nanocrystalline copper (upper pane) and tantalum (lower pane) and for various grain sizes $d$ (as listed in the legend).

![](./images/1006014889635872775_6.jpg)

FIG. 5. Grain and grain-boundary local pressure distributions in relaxed nanocrystalline tantalum for various grain sizes $d$ (as listed in the legend).

![](./images/1006014889635872775_7.jpg)

FIG. 6. A comparison of the shear-modulus distributions in eight different octants of the simulation box (colorful dashed lines) and in the entire system (black dotted lines). The results are shown for grain (upper pane) and grain-boundary (lower pane) atoms of nanocrystalline copper with grain size $d = 10$ nm.

Finally, we also note that the decrease of grain-boundary atomic fraction with grain size $d$ can also be seen visually in Figs. 2 and 3.

Figure 8 presents the grain-size dependence of various elastic moduli, namely, the shear modulus $G$, Young's modulus $E$, and bulk modulus $B$, as well as the Poisson's ratio $v$. These moduli are plotted separately for grain and grain-boundary atoms and for the entire system (that is, all atoms in the simulations), resulting in the respective total bulk moduli.

It is evident that the total elastic moduli increases with grain size, in accordance with the results of Refs. [23,24,26,50]. In order to analyze this behavior, we write the total elastic moduli as a sum of grain and grain-boundary moduli:

$$
\mathcal{M}_{\text{total}}(d)=x_{g b}(d) \mathcal{M}_{g b}(d)+x_{g}(d) \mathcal{M}_{g}(d), \tag{11}
$$

where $\mathcal{M}$ represents one of the considered moduli $G$, $E$, $B$, $v$, and $\mathcal{M}_{\text{total}}$, $\mathcal{M}_{g}$, and $\mathcal{M}_{g b}$ are, respectively, the total, grain, and grain-boundary elastic moduli. The results in

![](./images/1006014889635872775_8.jpg)

FIG. 7. The fractional number of grain (in blue) and grain-boundary (in red) atoms as a function of grain size in nanocrystalline copper (upper pane) and tantalum (lower pane). The points are the atomic fractions in the simulations (see Fig. 2), and the dashed lines are obtained from a $1/d$ fit [according to the scaling relation (10), as discussed in the text].

Fig. 8 indicate that the grains have elastic moduli $\mathcal{M}_g$ that are about 10% larger than the grain-boundary values $\mathcal{M}_{gb}$. This is to be expected, since it is well known that the grain boundary has an amorphous structure [1,3,4], a result that is consistent with our simulations and with Fig. 4, which shows wide elastic modulus distributions for grain-boundary atoms. Moreover, it is evident that $\mathcal{M}_g(d)$ and $\mathcal{M}_{gb}(d)$ both have a relatively weak dependence on the grain size $d$. Therefore we define a "mean-field" model, assuming grain-size-independent grain and grain-boundary elastic moduli $\mathcal{M}_g(d) \approx \overline{\mathcal{M}_g}$, $\mathcal{M}_{gb}(d) \approx \overline{\mathcal{M}_{gb}}$, where $\overline{\mathcal{M}}$ represents an arbitrary average of the elastic modulus over grain size $d$. We take the arithmetic average over the grain sizes considered. Using the $1/d$ scaling of the grain-boundary atoms fraction [Eq. (10)], we obtain a simple approximate mean-field model for the exact elastic moduli in Eq. (11) as a function of grain size:

$$
\mathcal{M}_{\text{total}}^{\text{Mean-Field}}(d) = \frac{d_0}{d}\overline{\mathcal{M}_{gb}} + \left(1 - \frac{d_0}{d}\right)\overline{\mathcal{M}_g}. \tag{12}
$$

The results of this simple mean-field model are also shown in Fig. 8, offering a very good qualitative and even quantitative agreement with the exact results obtained from the simulations. Therefore, we deduce that the grain-size dependence of the total elastic moduli $\mathcal{M}_{tot}(d)$ is mainly due to the strong grain-size dependence of the grain and grain-boundary atom fraction [via. Eq. (10)], while the effect of the grain-size dependence of the grain and grain-boundary elastic moduli is only a second-order effect.

## IV. SUMMARY

Local elastic moduli of nanocrystalline copper and tantalum were calculated using molecular dynamics simulations. The resulting moduli distributions within the polycrystals were calculated and analyzed as a function of grain size in the range of 5–20 nm. The shear-modulus distribution in the amorphous grain boundary is extended and grain-size independent, while the shear-modulus distribution for atoms within the grains is significantly narrower and becomes sharper with increasing grain size. Even though local

![](./images/1006014889635872775_9.jpg)

FIG. 8. Elastic moduli for grain-boundary (red circles), grain (blue squares), and all (black diamonds) atoms, as a function of grain size, for nanocrystalline copper (upper figures) and tantalum (lower figures). From left to right, the shear modulus $G$, Young's modulus $E$, bulk modulus $B$, and Poisson's ratio $v$ are shown. The dashed black line represents the mean-field model with $1/d$ scaling of the grain-boundary contribution [Eq. (12)], with $d_0 \approx 1.5$ nm for copper and $d_0 \approx 1.7$ nm for tantalum.

properties do not depend on grain size, global average elastic moduli do show grain-size dependence in accordance with previous observations [16,17,51,52].

This effect is shown explicitly to be denominated by the variation in relative numbers of crystalline versus grain-boundary atoms. We show for the simulated system that the average global elastic moduli can be approximated by a weighted average of the larger grain elastic moduli and the lower grain-boundary elastic moduli, an approximation which was assumed in several previous works [21,23,50,53,54].

Moreover, by employing the simple inverse relation between the grain-boundary atom fraction and grain size $d$, we suggest a simple but accurate mean-field formula for the grain-size dependence of various bulk atomic moduli (shear modulus, Young's modulus, bulk modulus, and Poisson's ratio).

[1] H. Gleiter, Nanostructured materials: Basic concepts and microstructure, Acta Mater. 48, 1 (2000).

[2] J. Schiøtz and K. W. Jacobsen, A maximum in the strength of nanocrystalline copper, Science 301, 1357 (2003).

[3] D. Wolf, V. Yamakov, S. R. Phillpot, A. Mukherjee, and H. Gleiter, Deformation of nanocrystalline materials by molecular-dynamics simulation: Relationship to experiments? Acta Mater. 53, 1 (2005).

[4] P. Keblinski, D. Wolf, S. R. Phillpot, and H. Gleiter, Structure of grain boundaries in nanocrystalline palladium by molecular dynamics simulation, Scr. Mater. 41, 631 (1999).

[5] S. D. Antolovich and R. W. Armstrong, Plastic strain localization in metals: Origins and consequences, Prog. Mater. Sci. 59, 1 (2014).

[6] S. N. Mathaudhu, Building on Gleiter: The foundations and future of deformation processing of nanocrystalline metals, Metall. Mater. Trans. A 51, 6020 (2020).

[7] L. A. Zepeda-Ruiz, A. Stukowski, T. Oppelstrup, and V. V. Bulatov, Probing the limits of metal plasticity with molecular dynamics simulations, Nature (London) 550, 492 (2017).

[8] K. Liu and M. H. F. Sluiter, Stresses at grain boundaries: The maximum incompatibility stress in an infinitely extended elastic bicrystal under uniaxial loading, Scr. Mater. 234, 115570 (2023).

[9] X. Zhang, A. Shang, B. Stegman, K. Choy, T. Niu, C. Shen, Z. Shang, X. Sheng, J. Lopez, L. Hoppenrath et al., Additive manufacturing of an ultrastrong, deformable Al alloy with nanoscale intermetallics, Research Square (2023).

[10] S. E. Kim, N. Verma, S. Özerinç, S. Jana, S. Das, P. Bellon, and R. S. Averback, Strengthening of nanocrystalline Al using grain boundary solute additions: Effects of thermal annealing and ion irradiation, Materialia 26, 101564 (2022).

[11] N. Pant, S. Das, P. Bellon, R. S. Averback, M. Krief, and Y. Ashkenazy, Role of interfaces on phase formation during severe plastic deformation, Acta Mater. 240, 118333 (2022).

[12] M. Krief and Y. Ashkenazy, Calculation of elastic constants of embedded-atom-model potentials in the NVT ensemble, Phys. Rev. E 103, 063307 (2021).

[13] F. Shimizu, S. Ogata, and J. Li, Theory of shear banding in metallic glasses and molecular dynamics calculations, Mater. Trans. 48, 2923 (2007).

[14] M. D. Kluge, D. Wolf, J. F. Lutsko, and S. R. Phillpot, Formalism for the calculation of local elastic constants at grain boundaries by means of atomistic simulation, J. Appl. Phys. 67, 2370 (1990).

[15] J. F. Lutsko, Generalized expressions for the calculation of elastic constants by computer simulation, J. Appl. Phys. 65, 2991 (1989).

[16] K. Yoshimoto, T. S. Jain, K. Van Workum, P. F. Nealey, and J. J. de Pablo, Mechanical heterogeneities in model polymer glasses at small length scales, Phys. Rev. Lett. 93, 175501 (2004).

[17] M. Tsamados, A. Tanguy, C. Goldenberg, and J.-L. Barrat, Local elasticity map and plasticity in a model Lennard-Jones glass, Phys. Rev. E 80, 026112 (2009).

[18] D. Lips and P. Maass, Stress-stress fluctuation formula for elastic constants in the NPT ensemble, Phys. Rev. E 97, 053002 (2018).

[19] A. A. Veldhorst and M. C. C. Ribeiro, Mechanical heterogeneity in ionic liquids, J. Chem. Phys. 148, 193803 (2018).

[20] C. M. Magazzeni, H. M. Gardner, I. Howe, P. Gopon, J. C. Waite, D. Rugg, D. EJ Armstrong, and A. J. Wilkinson, Nanoindentation in multi-modal map combinations: A correlative approach to local mechanical property assessment, J. Mater. Res. 36, 2235 (2021).

[21] T. D. Shen, C. C. Koch, T. Y. Tsui, and G. M. Pharr, On the elastic moduli of nanocrystalline Fe, Cu, Ni, and Cu-Ni alloys prepared by mechanical milling/alloying, J. Mater. Res. 10, 2892 (1995).

[22] J. Schiøtz, F. D. Di Tolla, and K. W. Jacobsen, Softening of nanocrystalline metals at very small grain sizes, Nature (London) 391, 561 (1998).

[23] A. Latapie and D. Farkas, Effect of grain size on the elastic properties of nanocrystalline $\alpha$-iron, Scr. Mater. 48, 611 (2003).

[24] Z. Pan, Y. Li, and Q. Wei, Tensile properties of nanocrystalline tantalum from molecular dynamics simulations, Acta Mater. 56, 3470 (2008).

[25] B. Chen, H. Zhang, K. A. Dunphy-Guzman, D. Spagnoli, M. B. Kruger, D. V. S. Muthu, M. Kunz, S. Fakra, J. Z. Hu, Q. Z. Guo et al., Size-dependent elasticity of nanocrystalline titania, Phys. Rev. B 79, 125406 (2009).

[26] P. Valat-Villain, J. Durinck, and P. O. Renault, Grain size dependence of elastic moduli in nanocrystalline tungsten, J. Nanomater. 2017 (2017).

[27] G.-J. J. Gao, Y.-J. Wang, and S. Ogata, Studying the elastic properties of nanocrystalline copper using a model of randomly packed uniform grains, Comput. Mater. Sci. 79, 56 (2013).

[28] E. Z. Engelberg, Y. Ashkenazy, and M. Assaf, Stochastic model of breakdown nucleation under intense electric fields, Phys. Rev. Lett. 120, 124801 (2018).

[29] D. R. Squire, A. C. Holt, and W. G. Hoover, Isothermal elastic constants for argon, Theory and Monte Carlo calculations, Physica 42, 388 (1969).

[30] T. Çağın, G. Dereli, M. Uludoğan, and M. Tomak, Thermal and mechanical properties of some fcc transition metals, Phys. Rev. B 59, 3468 (1999).

[31] K. Van Workum, K. Yoshimoto, J. J. de Pablo, and J. F. Douglas, Isothermal stress and elasticity tensors for ions and

point dipoles using Ewald summations, *Phys. Rev.* **E 71**, 061102 (2005).

[32] J.-L. Barrat, Microscopic elasticity of complex systems, in *Computer Simulations in Condensed Matter Systems: From Materials to Chemical Biology Vol. 2* (Springer, New York, 2006), pp. 287–307.

[33] G. Clavier, N. Desbiens, E. Bourrasseau, V. Lachet, N. Brusselle-Dupend, and B. Rousseau, Computation of elastic constants of solids using molecular simulation: Comparison of constant volume and constant pressure ensemble methods, *Mol. Simul.* **43**, 1413 (2017).

[34] E. B. Tadmor and R. E. Miller, *Modeling Materials: Continuum, Atomistic and Multiscale Techniques* (Cambridge University Press, Cambridge, UK, 2011).

[35] I. Alber, J. L. Bassani, M. Khantha, V. Vitek, and G. J. Wang, Grain boundaries as heterogeneous systems: Atomic and continuum elastic properties, *Philos. Trans. R. Soc. London, Ser. A* **339**, 555 (1992).

[36] M. S. Daw and M. I. Baskes, Embedded-atom method: Derivation and application to impurities, surfaces, and other defects in metals, *Phys. Rev. B* **29**, 6443 (1984).

[37] R. J. Wolf, K. A. Mansour, M. W. Lee, and J. R. Ray, Temperature dependence of elastic constants of embedded-atom models of palladium, *Phys. Rev. B* **46**, 8027 (1992).

[38] S. Chantasiriwan and F. Milstein, Higher-order elasticity of cubic metals in the embedded-atom method, *Phys. Rev. B* **53**, 14080 (1996).

[39] R. Hill, The elastic behaviour of a crystalline aggregate, *Proc. Phys. Soc. London, Sect. A* **65**, 349 (1952).

[40] J. F. Nye *et al.*, *Physical Properties of Crystals: Their Representation by Tensors and Matrices* (Oxford University Press, Oxford, England, 1985).

[41] R. E. Newnham, *Properties of Materials: Anisotropy, Symmetry, Structure* (Oxford University Press on Demand, 2005).

[42] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, *J. Comput. Phys.* **117**, 1 (1995).

[43] Y. Mishin, M. J. Mehl, D. A. Papaconstantopoulos, A. F. Voter, and J. D. Kress, Structural stability and lattice defects in copper: *Ab initio*, tight-binding, and embedded-atom calculations, *Phys. Rev. B* **63**, 224106 (2001).

[44] R. Ravelo, T. C. Germann, O. Guerrero, Q. An, and B. L. Holian, Shock-induced plasticity in tantalum single crystals: Interatomic potentials and large-scale molecular-dynamics simulations, *Phys. Rev. B* **88**, 134101 (2013).

[45] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITO—The open visualization tool, *Modell. Simul. Mater. Sci. Eng.* **18**, 015012 (2009).

[46] C. L. Kelchner, S. J. Plimpton, and J. C. Hamilton, Dislocation nucleation and defect structure during surface indentation, *Phys. Rev. B* **58**, 11085 (1998).

[47] V. Bulatov and W. Cai, *Computer Simulations of Dislocations* (Oxford University Press, Oxford, England, 2006), Vol. 3.

[48] E. N. Hahn and M. A. Meyers, Grain-size dependent mechanical behavior of nanocrystalline metals, *Mater. Sci. Eng., A* **646**, 101 (2015).

[49] J. Schiøtz, T. Vegge, F. D. Di Tolla, and K. W. Jacobsen, Atomic-scale simulations of the mechanical deformation of nanocrystalline metals, *Phys. Rev. B* **60**, 11971 (1999).

[50] K. Kowalczyk-Gajewska and M. Maździarz, Elastic properties of nanocrystalline materials of hexagonal symmetry: The core-shell model and atomistic estimates, *Int. J. Eng. Sci.* **157**, 103393 (2020).

[51] G. J. Papakonstantopoulos, K. Yoshimoto, M. Doxastakis, P. F. Nealey, and J. J. de Pablo, Local mechanical properties of polymeric nanocomposites, *Phys. Rev. E* **72**, 031801 (2005).

[52] H. Mizuno, S. Mossa, and J.-L. Barrat, Measuring spatial distribution of the local elastic modulus in glasses, *Phys. Rev. E* **87**, 042306 (2013).

[53] H. S. Kim and M. B. Bush, The effects of grain size and porosity on the elastic modulus of nanocrystalline materials, *Nanostruct. Mater.* **11**, 361 (1999).

[54] J. Lian, S.-W. Lee, L. Valdevit, M. I. Baskes, and J. R. Greer, Emergence of film-thickness-and grain-size-dependent elastic properties in nanocrystalline thin films, *Scr. Mater.* **68**, 261 (2013).