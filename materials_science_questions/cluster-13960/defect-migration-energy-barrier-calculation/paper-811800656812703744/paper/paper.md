PHYSICAL REVIEW B 81, 125425 (2010)

# Migration of gold atoms in graphene ribbons: Role of the edges

Wei Zhang, $^{1}$ Litao Sun, $^{2, *}$ Zijian Xu, $^{1}$ Arkady V. Krasheninnikov, $^{3,4}$ Ping Huai, $^{1}$ Zhiyuan Zhu, $^{1}$ and F. Banhart $^{5}$

$^{1}$ Shanghai Institute of Applied Physics, Chinese Academy of Sciences, 201800 Shanghai, China
$^{2}$ SEU-FEI Nano-Pico Center, Key Laboratory of MEMS of Ministry of Education, and State Key Laboratory of Bioelectronics, Southeast University, 210096 Nanjing, China
$^{3}$ Division of Materials Physics, University of Helsinki, FI-00014 Helsinki, Finland
$^{4}$ Laboratory of Physics, Helsinki University of Technology, FI-02015 Helsinki, Finland
$^{5}$ Institut de Physique et Chimie des Matériaux, UMR 7504, University of Strasbourg, 67034 Strasbourg, France

(Received 12 October 2009; revised manuscript received 24 January 2010; published 22 March 2010)

The migration of gold atoms attached to single vacancies near the edges of graphene ribbons is studied using density-functional theory calculations. The stable position for a single gold atom is found to be on top of a vacancy, as in an infinite graphene sheet. An energy of 5 eV is needed for the Au atom to move through the vacancy to the other side of the sheet, but the Au atom can migrate in lateral direction together with the vacancy, with a migration barrier of about 2.2 eV. The sites near the edges of the graphene layer are energetically more favorable for gold-atom-vacancy pairs than sites in the middle of extended graphene layers. The migration barriers for different pathways show that it is easier for the gold atom to move toward the edge where it can be captured. When the gold atom reaches the edge, it can migrate along the edge with an energy barrier of only 1.4 eV. Our results explain recent experimental observations [Y. Gan et al., Small 4, 587 (2008)] and provide information on the dynamics of metal atoms on substitutional sites in graphene as well as on their agglomeration at defects and at edges of graphene ribbons.

DOI: 10.1103/PhysRevB.81.125425
PACS number(s): 61.48.-c, 61.72.-y

## I. INTRODUCTION

Graphene has attracted enormous attention $^{1,2}$ since it was found to exist as a free-standing two-dimensional material. $^{3,4}$ Charge carriers in graphene have characteristics of relativistic particles and can be described with the Dirac equation. $^{3}$ Theoretically predicted anomalous plateaus in the quantum Hall effect have been observed in graphene as well. $^{5-8}$ A finite supercurrent can flow at zero charge density, showing a universal minimum of conductivity. $^{9}$ These properties make graphene an excellent platform for studying quantum phenomena and a promising material for future applications in nanoelectronics.

The structure and electronic properties of graphene can be tailored by chemical adsorption of metal atoms on the layer or by incorporation of metal atoms into its structure. $^{10-13}$ Experiments have shown that in bilayer graphene it is possible to create a gap at the K point by doping with potassium. $^{14}$ Doping of graphene with transition metal atoms has also received considerable attention due to strong bonding between metal and carbon atoms and interesting magnetic properties of metal-vacancy complexes. $^{15}$

Therefore, understanding the interaction between metal atoms and graphene at the microscopic level is highly important for optimizing the electronic properties and fabricating nanoelectronic devices. A few papers have studied the interaction between gold adatoms and a graphitic surface. $^{15-22}$ The gold atoms diffuse rapidly on a perfect graphitic surface with a remarkably low-energy barrier of $0.05eV.^{16}$ Since noble metal atoms are weakly adsorbed on graphene sheets, point defects have been suggested to be used as pinning centers for metal atoms. Akola and Hakkinen $^{20}$ have used first-principles calculations to investigate the possibility of bonding atoms and small clusters to a graphitic surface with surface vacancies and pyridinelike defects. Recently, the migration of individual heavy-metal atoms in graphenic structures have been studied in situ using high-resolution transmission electron microscopy (HRTEM). $^{23}$ Au and Pt atoms are found to diffuse laterally in the graphene lattice with a diffusion coefficient of $D=(0.6-2)×10^{-21}m^{2}s^{-1}$ for Au and $D=(0.4-1)×10^{-21}m^{2}s^{-1}$ for Pt. The diffusion coefficients are obtained from the measured migration distances within certain time intervals. The diffusion barrier $E_{a}$ is related to the diffusion coefficient D by

$$
D=g a^{2} v_{0} \exp \left(-\frac{E_{a}}{k_{B} T}\right),
$$

where g is a geometrical factor, a is the lattice constant, and $v_{0}$ is an attempt frequency. Further details of the experiments and estimates can be found in Ref. 23. Based on the experimental values of the diffusion barrier, it was assumed that metal atoms were located at single or double vacancies in a position slightly off the layer and migrate together with the vacancies. Later calculations $^{15,21}$ confirmed this assumption. It was also reported that metal-atom-vacancy pairs prefer positions at the edges of graphene sheets. Usually once the metal-atom-vacancy pair reaches the edge, it is effectively captured at the dangling bonds at the edge but it can diffuse along the edge.

In order to understand the experimental results, and, in particular, the effects of the edges on the migration of gold atoms over graphene sheets, we have studied in this work the properties and diffusion mechanisms of a Au-vacancy pair using first-principles simulations. We considered Au atoms on an infinite graphene sheet as well as in the proximity of the edge, and studied the interaction of Au atoms with the edges.

1098-0121/2010/81(12)/125425(5)
125425-1
©2010 The American Physical Society

## II. METHODS

All calculations were performed using the plane-wave code PWSCF of the QUANTUM-ESPRESSO package. $^{24}$ For the exchange and correlation functional we used the generalized gradient approximation (GGA) of Perdew-Wang. $^{25}$ Local density approximation could provide the right $c$-axis lattice constant of graphite, but usually overestimates the binding energy. This overestimation of the binding energy can be reduced by GGA. GGA is known to provide better accuracy for surface adsorption and diffusion. Nuclei and core electrons were described by an ultrasoft pseudopotential. $k$-point sampling was selected by the Monkhorst-Pack scheme. The energy cutoffs of the plane-wave basis and electron density were 35 Ry and 200 Ry, respectively. Brillouin zone integrations were performed with the Gaussian-spreading special-point technique $^{26,27}$ with a smearing parameter of 0.02 Ry. Structures were relaxed until the forces acting on the atoms were less than $0.026\ \text{eV}/\mathring{\text{A}}$. The energy barriers were calculated using the climbing-image nudged elastic band (NEB) method implemented in PWSCF. $^{28}$ The NEB method is very useful in finding the minimum-energy path between a given initial and final states of a transition. The NEB method gives a continuous path even when multiple minimum-energy paths exist. However, because the saddle points are unstable, searching for their direct locations is a rather difficult task. Thus one cannot exclude that there is a path with a lower activation barrier. Nevertheless, the NEB method normally gives physically correct results, as shown in thousands of papers on diffusion in solids.

To explore the energetically stable structure of the Au-vacancy pair, geometry optimizations were performed by constructing a piece of graphene sheet composed of 79 atoms with a vacancy defect, and putting the Au atom in or on top of the vacancy. The periodic boundary conditions were used in the two directions of the graphene plane. The length of the supercell along the $c$ axis was set to $12\ \mathring{\text{A}}$ to prevent interaction between adjacent images. Calculations were performed with Brillouin zone sampling using a Monkhorst-Pack $^{26}$ $k$-point mesh of $4\times4\times1$.

## III. RESULTS AND DISCUSSION

### A. Structure and migration of a Au-vacancy pair in an infinite graphene sheet

In previous experimental work, $^{23}$ the Au-atom-doped graphene was investigated by HRTEM. From a view in the direction along the graphene layer, the metal atoms appeared to be located in the plane of the graphene layer, probably in single or multiple vacancies. It was not possible to decide from the TEM images if the metal atom was on a single or double vacancy. Although previous calculations showed that Au atoms attached to single vacancies are slightly off the plane, the Au atom could, in principle, oscillate at high experimental temperatures between two equivalent positions on different sides of the sheet by passing through the vacancy, thus appearing on an average position in the plane of the layer.

To study this hypothetic mechanism and to compare our results to the already published data, we first simulated Au atoms on vacancies in infinite graphene sheets. By putting the Au atom at the vacancy, in or off the graphene plane, we searched for the minimum energy of the Au-vacancy system, and found the stable structure, as in previous work. $^{15,21}$ Figure 1(a) shows that the Au atom is on top of the vacancy, forming three bonds with the nearest carbon atoms, and the C-Au bond length is $2.01\ \mathring{\text{A}}$. This length is smaller than the equilibrium distance of $2.44\ \mathring{\text{A}}$ between Au and C atoms where a Au atom is adsorbed on a nondefective graphene sheet. $^{29}$ From the inset in Fig. 1(b), it can be seen that there is a low electron density between the Au and C atoms, showing that the interaction is covalent, but weak. The formation energy is calculated as $E_f=E_{\text{system}}-E_{\text{system with a vacancy}}-E_{\text{Au}}$. We also calculated the energy of a perfectly flat configuration, which can be interpreted as the saddle point between two equivalent configurations with the Au atoms positioned on different sides of the plane. The formation energy of the in-plane and off-plane structures is 2.42 eV and -2.51 eV, respectively. Comparing the formation energies of two structures, the off-plane structure is energetically clearly favored. The high-energy difference of nearly 5 eV indicates that the Au atom cannot oscillate at the experimental temperatures (about $500\ {^\circ}\text{C}$). The binding energy of the [Fig. 1(a)] structure is in accordance with previous calculations. $^{20}$

![](./images/811800656812703744_1.jpg)

FIG. 1. (Color online) Possible positions for a Au atom in (a) a single vacancy and (b) a double vacancy in a graphene sheet. The inset in (a) shows an electron-density slice through the Au atom (white means high electron density).

For the Au atom in a double vacancy, the minimum-energy configuration was obtained as shown in Fig. 1(b). The Au atom is located in the plane of the sheet. The binding energy is 4.53 eV. The formation-energy and migration-energy barriers for a double vacancy are quite high, $^{30}$ so it is impossible for the Au-atom-double-vacancy complex to migrate at the experimental temperatures of $600\ {^\circ}\text{C}$.

Having found the stable positions, we considered the migration of the Au atom in the graphene layer, namely, the migration of a Au-single-vacancy pair. At first we studied the migration of a single vacancy in graphene using a system of 23 atoms. The formation energy is 7.8 eV. The migration barrier is 1.46 eV. This is very close to the results of previous calculations. $^{30}$ As for the migration of a Au-vacancy pair, the above-mentioned off-plane structure is taken as the initial and final structures. The Au-vacancy pair moves to a neighboring site, as shown in the insets of Fig. 2. The migration path is found using the NEB method. The path of the Au-vacancy pair is similar to the path of an isolated single vacancy as described in Ref. 31. One carbon bond breaks first and a pentagon forms during the migration. The Au atom

![](./images/811800656812703744_2.jpg)

FIG. 2. (Color online) The energy profile for the diffusion of the Au-vacancy pair.

moves on top of the sheet toward the opposite direction. The activation energy is approximately 2.2 eV, which is close to the experimental value of 2.5 eV.

### B. Migration of the Au-vacancy pair in narrow graphene ribbons

In the experiment, the metal atoms preferred edge sites rather than inner sites. The metal atoms finally moved to the boundary of the graphene sheet and diffused along the edge with lower activation energy. In order to investigate the edge effect on the migration of the Au-vacancy pair, we consid- ered the system of graphene ribbons with zigzag, armchair, and reczag $^{32}$ edges, respectively. The reczag edge is a recently suggested edge reconstructed from the zigzag edge. It is chemically less reactive than the zigzag edge. The distance between the two edges of the two images of the ribbon was set to be larger than $6~\mathring{A}$ to prevent the interactions. The Au-vacancy pair was placed at different sites in the ribbon and the structures were optimized. The sites in three types of edges are shown in Fig. 3. The width of the ribbon is around $16~\mathring{A}$. As an example, the optimized structures for the zigzag ribbon are shown in Fig. 4. It can be seen that the graphene sheet is deformed due to the interaction with the Au atom. For positions A, B, and C, a notable structural deformation was found at both edges of the ribbon. The Au atom induces local hillocks in the graphene sheet. The influence of the hillocks extends to the edges, which resulted in a wavy shape of the edge. For positions D and F, the left edge did not show noticeable deformation. The Au atom goes into the plane of the sheet at the F site. We also optimized those structures with the edge passivated with hydrogen atoms. In this case, the atomic structure of the edges of the ribbon is less influenced by the Au atom. The hillock introduces a little bending into the ribbon. Only when the Au atom approaches the edge at F site, the right edge shows deformation.

The total energies of these structures are given in Fig. 3. From the inner sites to the edge, the total energy of three types of ribbons decreases. The passivated cases are different from the nonpassivated cases for the zigzag and armchair edges. However, for the reczag edge there is little difference except the drop of 0.6 eV at the F site. In all cases, the

![](./images/811800656812703744_3.jpg)

FIG. 3. Configurations of the Au-vacancy pair at different sites on the graphene ribbons with (a) zigzag, (b) armchair, and (c) reczag edges. The total energy of optimized structures of the graphene ribbon with Au at different sites is shown right with (solid squares) and without (open squares) hydrogen passivation. The energy of the Au metal in the middle of the ribbon is set to zero. The lines are drawn to guide the eyes.

![](./images/811800656812703744_4.jpg)

FIG. 4. (Color online) Optimized structures of the zigzag graphene ribbon with Au at A-F sites as shown in Fig. 3. In the right column the edges are passivated by hydrogen atoms.

![](./images/811800656812703744_5.jpg)

FIG. 5. (Color online) The migration path for the Au atom at the edge site, as found by the NEB method.

variation in energies shows that the sites near the edge are more stable. In other words, the Au-vacancy pair is attracted by the edge. We also carried out structural optimization with spin-polarized density-functional theory for several sites of the zigzag ribbon, the same trend is found although the energy difference is reduced.

Now for the zigzag ribbon, we calculate the energy barriers for the migration of a Au-vacancy pair along the routes $A\rightarrow A'$ ($A'$ is the mirror-symmetric image of A), $A\rightarrow B$, $B\rightarrow C$, and $C\rightarrow D$. The Au-vacancy pair shows similar behavior during the migration with the same path as in the infinite graphene sheet. The activation energy for these routes is 2.20 eV, 1.98 eV, 2.16 eV, and 1.36 eV, respectively. The comparison of the total and activation energies for $A\rightarrow A'$ and $B\rightarrow C$, $A\rightarrow B$ and $C\rightarrow D$ paths indicates that it is favorable for the Au-vacancy complex to move toward the edge. The activation energies of $A\rightarrow B$ and $C\rightarrow D$ are lower than the other two paths, indicating that the Au atom moves more easily along the edge of a ribbon than in a perpendicular direction.

If the Au atom is at the apex site of the zigzag edge, the total energy of the system is approximately 3.6 eV lower than at the F site. The Au atom is only bonded to two neighbor C atoms with a bond length of $1.97\ \mathring{A}$, which is shorter by $0.13\ \mathring{A}$ than the Au-C bond length in the F site. When the gold atom reaches the edge, it can be captured by the edge and then may move by jumping between the apexes of the zigzag edge. The migration path is shown in Fig. 5. The carbon atom at the neighboring apex site moves first toward the apex site. Then the Au atom goes to the vacant site. The activation energy is 1.37 eV. This is very close to the activation energy of path $C\rightarrow D$. However, the value is lower than the experimental value. This may be attributed to the interaction between the graphene edge and the substrate (there is a 1-2 layer graphene sheet under the graphene edge$^{23}$). Also, in the experiments, the effects of electron irradiation which may have increase the diffusion rate, should be considered.

A larger defect concentration can be achieved by irradiation with a higher electron dose but the reconstruction after vacancy formation is rapid and would lead to strong and clearly visible curvature effects (warping and cagelike structures). Unlike carbon atoms, the heavy metal atoms can hardly be displaced by knocks from the electrons. Therefore, electron irradiation should have only minor influence on the migration of metal atoms although a certain contribution of radiation-enhanced diffusion might be taken into account.

## IV. CONCLUSION

To conclude, we have studied the migration of gold atoms attached to single vacancies near the edges of graphene ribbons within the framework of density-functional theory. The stable position for a single gold atom is found to be on top of a vacancy, as in an infinite graphene sheet. It cost about 5 eV for the Au atom to move through the vacancy to the other side of the sheet, but the Au atom can migrate together with the vacancy with a migration barrier of about 2.2 eV. The sites near the edges are energetically more favorable for gold-atom-vacancy pairs, so that there is a long-range attraction of Au-vacancy complexes to the edges of the ribbon. The migration barriers for different paths show that it is easier for the gold atom to move toward the edge, and it can be captured by the edge. When the gold atom reaches the edge, it can migrate along the edge with a lower energy barrier of 1.4 eV. Our results explain recent experimental observations$^{23}$ and provide information on the dynamics of metal atoms on graphene and their agglomeration at defects and edges, which can be used for defect-mediated engineering of the atomic and electronic structures of carbon nanosystems.$^{33}$

## ACKNOWLEDGMENTS

This work was supported by the Key Project of the Knowledge Innovation Programme of the Chinese Academy of Sciences (Grant No. KJCX3-SYW-N10), the National Basic Research Programme of China (Grant No. 2006CB300404), the National Natural Science Foundation of China (Grant Nos. 60976003 and 10874197) and the National High-Tech Research and Development Programme of China (Grant No. 2007AA04Z301). We are grateful to the Shanghai Supercomputer Center for the use of the Dawning 4000 A supercomputer. A.V.K. also acknowledges the support from the Academy of Finland through several projects.

*Corresponding author; slt@seu.edu.cn

$^{1}$A. H. Castro Neto, F. Guinea, N. M. R. Peres, K. S. Novoselov, and A. K. Geim, Rev. Mod. Phys. 81, 109 (2009).

$^{2}$A. K. Geim and K. S. Novoselov, Nature Mater. 6, 183 (2007).

$^{3}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva, and A. A. Firsov, Science 306, 666 (2004).

$^{4}$J. C. Meyer, A. K. Geim, M. I. Katsnelson, K. S. Novoselov, T. J. Booth, and S. Roth, Nature (London) 446, 60 (2007).

$^{5}$N. M. R. Peres, A. H. Castro Neto, and F. Guinea, Phys. Rev. B 73, 195411 (2006).

$^{6}$V. P. Gusynin and S. G. Sharapov, Phys. Rev. Lett. 95, 146801 (2005).

$^{7}$K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, M. I. Katsnelson, I. V. Grigorieva, S. V. Dubonos, and A. A. Firsov, Nature (London) 438, 197 (2005).

125425-4

$^{8}$Y. Zhang, Y. Tan, H. L. Stormer, and P. Kim, Nature (London) **438**, 201 (2005).

$^{9}$H. B. Heersche, P. Jarillo-Herrero, J. B. Oostinga, L. M. K. Vandersypen, and A. F. Morpurgo, Nature (London) **446**, 56 (2007).

$^{10}$F. Cervantes-Sodi, G. Csanyi, S. Piscanec, and A. C. Ferrari, Phys. Rev. B **77**, 165427 (2008).

$^{11}$K. T. Chan, J. B. Neaton, and M. L. Cohen, Phys. Rev. B **77**, 235430 (2008).

$^{12}$B. Uchoa, C. Y. Lin, and A. H. Castro Neto, Phys. Rev. B **77**, 035420 (2008).

$^{13}$R. S. Sundaram, C. Gómez-Navarro, K. Balasubramanian, M. Burghard, and K. Kern, Adv. Mater. **20**, 3050 (2008).

$^{14}$T. Ohta, A. Bostwick, T. Seyller, K. Horn, and E. Rotenberg, Science **313**, 951 (2006).

$^{15}$A. V. Krasheninnikov, P. O. Lehtinen, A. S. Foster, P. Pyykko, and R. M. Nieminen, Phys. Rev. Lett. **102**, 126807 (2009).

$^{16}$P. Jensen, X. Blase, and P. Ordejón, Surf. Sci. **564**, 173 (2004).

$^{17}$P. Jensen and X. Blase, Phys. Rev. B **70**, 165402 (2004).

$^{18}$G. M. Wang, J. J. BelBruno, S. D. Kenny, and R. Smith, Phys. Rev. B **69**, 195412 (2004).

$^{19}$G. M. Wang, J. J. BelBruno, S. D. Kenny, and R. Smith, Surf. Sci. **576**, 107 (2005).

$^{20}$J. Akola and H. Hakkinen, Phys. Rev. B **74**, 165404 (2006).

$^{21}$S. Malola, H. Häkkinen, and P. Koskinen, Appl. Phys. Lett. **94**, 043106 (2009).

$^{22}$B. Yoon, W. D. Luedtke, J. Gao, and U. Landman, J. Phys. Chem. B **107**, 5882 (2003).

$^{23}$Y. Gan, L. Sun, and F. Banhart, Small **4**, 587 (2008).

$^{24}$S. Baroni, A. Dal Corso, S. de Gironcoli, P. Giannozzi, C. Cavazzoni, G. Ballabio, S. Scandolo, G. Chiarotti, P. Focher, A. Pasquarello, K. Laasonen, A. Trave, R. Car, N. Marzari, and A. Kokalj, http://www.pwscf.org/

$^{25}$Y. Wang and J. P. Perdew, Phys. Rev. B **44**, 13298 (1991).

$^{26}$H. J. Monkhorst and J. D. Pack, Phys. Rev. B **13**, 5188 (1976).

$^{27}$M. Methfessel and A. T. Paxton, Phys. Rev. B **40**, 3616 (1989).

$^{28}$G. Henkelman and H. Jonsson, J. Chem. Phys. **113**, 9978 (2000).

$^{29}$R. Varns and P. Strange, J. Phys.: Condens. Matter **20**, 225005 (2008).

$^{30}$A. V. Krasheninnikov, P. O. Lehtinen, A. S. Foster, and R. M. Nieminen, Chem. Phys. Lett. **418**, 132 (2006).

$^{31}$A. A. El-Barbary, R. H. Telling, C. P. Ewels, M. I. Heggie, and P. R. Briddon, Phys. Rev. B **68**, 144107 (2003).

$^{32}$P. Koskinen, S. Malola, and H. Hakkinen, Phys. Rev. B **80**, 073401 (2009).

$^{33}$A. V. Krasheninnikov and F. Banhart, Nature Mater. **6**, 723 (2007).