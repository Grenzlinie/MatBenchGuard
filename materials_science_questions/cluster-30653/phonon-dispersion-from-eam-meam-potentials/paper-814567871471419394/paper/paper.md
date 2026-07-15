# Monte Carlo simulation of elongating metallic nanowires in the presence of surfactants

M. Cecilia Gimenez, Luis Reinaudi¹, and Ezequiel P. M. Leiva

Citation: *J. Chem. Phys.* **143**, 244702 (2015); doi: 10.1063/1.4938409

View online: http://dx.doi.org/10.1063/1.4938409

View Table of Contents: http://aip.scitation.org/toc/jcp/143/24

Published by the American Institute of Physics

---

![](./images/814567871471419394_1.jpg)

# Monte Carlo simulation of elongating metallic nanowires in the presence of surfactants

M. Cecilia Gimenez, $^{1}$ Luis Reinaudi, $^{2,a)}$ and Ezequiel P. M. Leiva $^{2}$

$^{1}$IFEG, FaMAF, Universidad Nacional de Córdoba, Córdoba, Argentina
$^{2}$INFIQC, Departamento de Matemática y Física, Facultad de Ciencias Químicas,
Universidad Nacional de Córdoba, Córdoba, Argentina

(Received 16 September 2015; accepted 9 December 2015; published online 28 December 2015)

Nanowires of different metals undergoing elongation were studied by means of canonical Monte Carlo simulations and the embedded atom method representing the interatomic potentials. The presence of a surfactant medium was emulated by the introduction of an additional stabilization energy, represented by a parameter $Q$. Several values of the parameter $Q$ and temperatures were analyzed. In general, it was observed for all studied metals that, as $Q$ increases, there is a greater elongation before the nanowire breaks. In the case of silver, linear monatomic chains several atoms long formed at intermediate values of $Q$ and low temperatures. Similar observations were made for the case of silver-gold alloys when the medium interacted selectively with Ag. © 2015 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4938409]

## I. INTRODUCTION

The study of wires a few atoms wide or even one atom wide is an interesting topic to be investigated from the point of view of nanotechnology. The formation and structure of these nanowires may be influenced by the presence of surfactants, which can be the solvent or some adsorbate particles, which determine some differences with respect to the system in vacuum.

Ugarte *et al.*$^{1}$ have studied experimentally the formation of linear atomic chains (LACs) of some metals, like copper$^{2}$, gold$^{3}$, alloys of silver and gold$^{4}$ and the atomic arrangement and electrical transport properties of gold and platinum.$^{5}$

There are also several studies of the formation of nanowires by means of computational simulations,$^{6,7,28,8}$ in particular, molecular dynamics.$^{9–14}$ On the other hand, there are also experimental contributions to the study of nanowires.$^{15–18}$

Previously, we have studied the formation of metallic nanowires by means of Monte Carlo simulations and the embedded atom model in vacuum conditions$^{20}$ and the effect of surfactants and temperature on the structure of gold and silver nanoparticles.$^{21}$

Monte Carlo simulations have some advantages with respect to Molecular dynamics simulation. Even though information about time is not well defined in Monte Carlo, we can perform a wide exploration of the configurational space of the system. Thus, we do not predict the exact evolution with time, but we are rather interested in properties of the metallic nanowires wires close to equilibrium.

In this work, we present the study, by means of canonical Monte Carlo simulations, of nanowires of some metals and alloys, starting from a group of atoms between two planes with 100 orientations. An additional stabilization energy, represented by a parameter $Q$, is introduced in the model to account for the stabilizing interaction of external atoms with a surfactant. By external atoms we understand those that are not completely surrounded by other metal atoms. The metals that were considered are silver, gold, palladium, and platinum. Among the alloys studied, the most interesting is the case of gold-silver alloys, and this is the example discussed in this work.

The outline of the paper is as follows: In Section II, we describe the model along with the simulation scheme. In Section III we present the results. Finally, the general conclusions are given in Section IV.

## II. MODEL AND SIMULATION METHOD

### A. The model

The model consists on several parallel planes of mobile atoms of the metal, inserted between two fixed planes of the same metal with (100) orientation, as the initial condition. In the case of bimetallic alloys, the composition of the mobile atoms is 50% of each species and the two fixed planes are made of one of the metals.

Then, a canonical continuum Monte Carlo simulation is performed in order to reach the equilibrium positions of the atoms. Once the equilibrium is reached, the external planes are slightly separated in small steps (0.1 Å in this case) and a new simulation run is performed for this new situation. This procedure is repeated several times, until the rupture of the wire is observed.

Each simulation step consist in an attempt of moving all the internal atoms, according to the Metropolis algorithm. For each separation step between external metal planes, we performed 100 000 Monte Carlo steps.

See Ref. 20 for more details.

$^{a)}$Author to whom correspondence should be addressed. Electronic mail: luis.reinaudi@unc.edu.ar

### B. Energy calculations

In order to calculate the total energy of the system, we employ the Embedded Atom Method (EAM).²²

The EAM is a semi-empirical method that considers the total energy $U_{tot}$ of an arrangement of $N$ particles calculated as the sum of energies $U_i$ corresponding to individual particles,
$$
U_{tot} = \sum_{i=1}^{N} U_i, \tag{1}
$$
where $U_i$ is given by
$$
U_i = F_i(\rho_{h,i}) + \frac{1}{2} \sum_{j \neq i} V_{ij}(r_{ij}), \tag{2}
$$
where $F_i$ is called the embedding function and represents the energy necessary to embed atom $i$ in the electronic density $\rho_{h,i}$ at the position at which this atom is located. On the other hand, the repulsion between ion cores is represented through a pair potential $V_{ij}(r_{ij})$, which depends on the distance between the cores $r_{ij}$.

The embedded atom method was mainly developed for bulk metals and the fitted parameters are adjusted to this situation. In the case of surfaces, it is known that this model underestimates the surface energies and it is reasonable to think that something similar may occur with nanowires. However, the EAM has been of widespread us in the literature to tackle the problem of nanowires,⁷,²⁰,²³⁻²⁷ sometimes with excellent results.²⁸,²⁹

The interaction with the surfactant medium is modelled by means of the introduction of an extra energy term, $Q$, associated to each atom located at the surface of the cluster. Thus, for our model, Equation (1) becomes
$$
U_{tot} = \sum_{i=1}^{N} (U_i - \delta_i Q), \tag{3}
$$
where $U_i$ is the same as in Equation (1), $Q$ is a positive constant whose value is directly related to the strength of the interaction of the surface atoms with the surfactant medium and $\delta_i$ is a factor that takes the value 1 if atom $i$ is located at the surface of the wire and takes the value 0 otherwise. See Ref. 21 for details on the criterion used to identify the surface atoms.

In this work, we use different values of the parameter $Q$ located within the range between 0 and 1 eV. To show that these are reasonable values, we can mention the binding energies per metal atom of methanethiol adsorbed on (111) Cu, Ag, and Au surfaces, which are 0.80 eV, 0.65 eV, and 0.60 eV, respectively.¹⁹

### III. RESULTS AND DISCUSSION

Nanowires of a pure metal were simulated for several temperatures and several values of $Q$. The chosen system sizes were 96 atoms (six initial planes of $4 \times 4$ atoms) and 160 atoms (ten initial planes of $4 \times 4$ atoms). The studied metals were silver, gold, palladium, and platinum. Figure 1 shows 96-atom simulated nanowires of these four metals at $T = 300$ K for the value $Q = 0.4$ eV just before the breaking point.

![](./images/814567871471419394_2.jpg)

FIG. 1. Images of the simulated nanowires just before breaking, for several metals (silver, gold, palladium, and platinum) at $T = 300$ K, for the value $Q = 0.4$ eV. The values of the distance $d$ between external planes for each of these structures are $d_{\text{Ag}} = 26.43$ Å, $d_{\text{Au}} = 23.10$ Å, $d_{\text{Pd}} = 22.83$ Å, and $d_{\text{Pt}} = 22.63$ Å. The total number of atoms is 96.

The total energy as a function of the distance between the two external planes was also analyzed. Figure 2 shows a plot of energy difference with respect to the energy of the starting configuration vs. separation distance for 96-atom wires of the four studied metals, at $T = 300$ K, for several values of $Q$.

Comparison of the behavior of the four metals studied in vacuum (which corresponds to $Q = 0$) shows an overshoot before the final energy plateau is reached after the breaking of the nanowire occurs. For the cases of Pd and Pt, this overshoot is of the order of 15 eV; and for the cases of Ag and Au, this overshoot is about half as much.

In the cases of Ag and Au, for larger values of $Q$, a lowering of the energy can be observed at intermediate elongations of the nanowires. This lowering of the energy is correlated to the rise of the fraction of surface atoms in the nanowires, as shown in Figure 3. After this initial lowering of the energy, the total energy increases as $d$ increases, until the breaking point is reached. At that point, a small jump is observed, as a consequence of having two compact clusters instead of one stretched nanowire.

In the cases of Pd and Pt, the energy, on average, increases as $d$ increases, until the breaking point is reached.

An important observation to make is that, in general, as the value of $Q$ increases, the value of the distance at which the nanowires breaks also increases. This increase is significantly

![](./images/814567871471419394_3.jpg)

FIG. 2. Energy difference (with respect to the energy of the starting configuration) as a function of the distance between the two external planes, for a single simulation of 96-atom nanowires of silver, gold, palladium, and platinum, for different values of $Q$, at $T = 300$ K. The curves are displaced vertically with respect to each other for the sake of visibility.

larger in the case of Ag, reaching up to 8 Å in the case of $Q = 1.0$.

Figure 3 shows the fraction of surface atoms as a function of distance between external planes, for the same cases as those mentioned in Figure 2.

The general observation is that, for each value of $Q$, the fraction of surface atoms initially increases and then remains approximately constant after the nanowire breaks. The other important observation is that, as $Q$ increases, the fraction of surface atoms also increases and tends to 1 for large $Q$ and large distances, whereas it starts near 0.7 for the case of $Q = 0$ eV and the minimal distance between planes.

Figure 4 shows the total energy and the fraction of surface atoms for the case of 96-atom nanowires of silver and platinum at three different temperatures ($T = 100$ K, $T = 300$ K, and $T = 800$ K). In general, the total energy is higher for $T = 800$ K. For silver at $T = 100$ K, there are several peaks until the breaking point is reached, the tendency is not monotonic. For the case of platinum, there are no important differences between the curves of fraction of surface atoms, for different temperatures. For the case of silver and at low separations, the fraction of surface atoms is higher for higher temperatures. On the other hand, at higher distances, the fraction of surface atoms is lower for higher temperatures.

The most noteworthy result found in these simulations is the fact that, for the case of silver nanowires, at low temperatures and intermediate values of $Q$ (around $Q = 0.4$ eV), a relatively large and stable one atom wide chain of atoms forms. This one atom wide chains form only in the case of silver.

Figure 5 shows the monoatomic nanowires of silver, for $T = 100$ K and $Q = 0$ eV, $Q = 0.4$ eV, and $Q = 0.6$ eV for systems made of 160 atoms.

The formation of LACs ("linear atomic chains") or monatomic nanowires of silver was studied systematically by means of averaging 12 simulations for the case of 96 atoms, low temperatures and several values of $Q$. The mean distance at which rupture occurs ($d_{\text{break}}$) as well as the probability

![](./images/814567871471419394_4.jpg)

FIG. 3. Fraction of surface atoms as a function of the distance between the two external planes, for a single simulation of 96-atom nanowires of silver, gold, palladium, and platinum, for different values of $Q$, at $T = 300$ K.

![](./images/814567871471419394_5.jpg)

FIG. 4. Total energy and fraction of surface atoms as a function of the distance between the two external planes, for a single simulation of 96-atom nanowires of silver and platinum, for $Q = 0.4$ eV, at three different temperatures.

$Q = 0.0$ eV
$Q = 0.4$ eV
$Q = 0.6$ eV

![](./images/814567871471419394_6.jpg)

FIG. 5. Images of the simulated nanowires just before breaking, for silver, at $T = 100$ K and three values of $Q$. The total number of atoms is 160.

![](./images/814567871471419394_7.jpg)

FIG. 6. Distance between external planes at which the nanowire breaks ($d_{\text{break}}$) and probability of formation of a LAC ($p_{\text{LAC}}$), averaged over 12 simulations, as a function of $Q$, for silver nanowires of 96 atoms, at different temperatures.

of formation of LACs ($p_{\text{LAC}}$) as a function of $Q$ is shown in Figure 6 for several temperatures. The value of $p_{\text{LAC}}$ is defined for each simulation as 0 if no LAC is observed, 1 is a long LAC is observed and 0.5 if a short LAC (a chain of up to 5 atoms long) is observed. The results are qualitatively similar for the two studied variables. At these low temperatures, as temperature increases, $d_{\text{break}}$ and $p_{\text{LAC}}$ increase. For temperatures around $T = 100$ K, there is a maximum around $Q = 0.4$ eV. For $T = 140$ K there is another maximum around $Q = 0.8$ eV. There is a local minimum at $Q = 0.6$ eV for $T = 100$ K. Figure 7 shows the particular cases for $T = 60$ K and $T = 100$ K, but with the addition of error bars. The addition of error bars shows that the maxima and minima presented by these curves are indeed significant. The error bars for the rest of the cases show a similar behavior.

In the case of nanowires of silver-gold alloys, we can point out two important observations. For the case of $Q_{\text{Au}} = 0$ and $Q_{\text{Ag}} > 0$ we have found the formation of LACs composed mainly by silver atoms. Images of examples of these observations are shown in Figure 8, for systems composed of 160 atoms, where the cases of silver-gold bimetallic nanowires

![](./images/814567871471419394_8.jpg)

FIG. 7. Distance between external planes at which the nanowire breaks ($d_{\text{break}}$) and probability of formation of a LAC ($p_{\text{LAC}}$), averaged over 12 simulations, as a function of $Q$, for silver nanowires of 96 atoms, for $T = 60$ K and $T = 100$ K, with the addition of error bars.

$Q_{\text{Ag}} = 0.0$ eV
$Q_{\text{Ag}} = 0.3$ eV
$Q_{\text{Ag}} = 0.5$ eV

![](./images/814567871471419394_9.jpg)

FIG. 8. Images of the simulated nanowires just before breaking, for silver- gold alloys, at $T = 100$ K and three values of $Q_{\text{Ag}}$ (for $Q_{\text{Au}}=0$). The total number of atoms is 160.

with $Q_{\text{Au}} = 0$ and $Q_{\text{Ag}} = 0, 0.3$, and $0.5$ eV are illustrated just before breaking.

The other important case analysed is that where $Q_{\text{Ag}} = 0$ and $Q_{\text{Au}} > 0$, which means that the surfactant medium interacts selectively with the Au atoms. This is illustrated in Figure 9, which shows the radial distribution of atoms (number of atoms of each species as a function of the distance to the center of the nanowire), for systems composed of 160 atoms, for six different values of $Q_{\text{Au}}$. For $Q_{\text{Au}} = 0$, gold atoms tend to positionate closer to the center position and silver atoms tend to positionate in the outer region. This is due to the smaller surface energy of silver atoms as compared to gold atoms (see Ref. 20). As $Q_{\text{Au}}$ values increase, the consequent lowering of the surface energy of Au tends to overturn the natural tendency of Au atoms to remain at the center of the wire and favors the trend of gold atoms to be at the outer region of the nanowire.

## IV. CONCLUSIONS

Nanowires of different metals and two-metal-alloys were simulated by means of canonical continuous Monte Carlo methods. The embedded atom method was employed for the interatomic potentials.

An additional stabilization energy due to interaction with the medium was added, which takes the form of a parameter $Q$ associated with each surface atom.

Nanowires of Au, Ag, Pd, Pt, and Au-Ag alloys were simulated, for different values of $Q$ and different temperature values ($T = 300$ K, 100 K, and 800 K).

In general, a greater stabilization of the nanowires (that is, a greater elongation before breaking) was observed with increasing values of $Q$ for all metals. In the particular case of silver, at low temperatures and intermediate values of $Q$, the formation of linear atomic chains was found.

For the case of silver-gold alloys, at low temperatures and with $Q_{\text{Au}} = 0$ and $Q_{\text{Ag}} > 0$ (i.e., only the interaction of Ag with the surfactant medium is favored), the formation of linear atomic chains was also found. In this case, the LACs were composed mainly of silver atoms.

For the case of silver-gold alloys, with $Q_{\text{Au}} > 0$ and $Q_{\text{Ag}} = 0$ (i.e., only the interaction of Au with the surfactant

![](./images/814567871471419394_10.jpg)

FIG. 9. Number of atoms of each species as a function of the distance to the central axis of the 160-atom nanowire for the system silver-gold, for six values of $Q_{\text{Au}}$ (for $Q_{\text{Ag}}=0$).

medium is favored), as the value of $Q$ increases, a displacement of Au atoms to the outer region of the nanowire (contrary to the natural tendency in vacuum) was observed.

The present work presents motivation for further experimental work using adsorbates that interact with monatomic nanowires with different strengths. The best candidates are silver nanowires, which present the greater elongation before breaking. On the basis of our simulations, we suggest these experiments to be performed at relatively low temperatures.

## ACKNOWLEDGMENTS
National Council of Scientific and Technological Research of Argentina (Conicet), Secyt UNC, and No. PME 2006-01581 for financial support. CONICET-PIP No. 11220110100992 and Program BID (No. PICT 2012-2324), for computational tools. M.C.G. thanks Alexander von Humboldt Foundation for financial support. We also acknowledge the Ovito program, $^{30}$ used for the obtained images. Wolfgang Schmickler for the initial contributions to the topic.

$^{1}$V. Rodrigues, T. Fuhrer, and D. Ugarte, *Phys. Rev. Lett.* **85**(19), 4124-4127 (2000).

$^{2}$F. Sato, A. S. Moreira, J. Bettini, P. Z. Coura, S. O. Dantas, D. Ugarte, and D. S. Galvão, *Phys. Rev. B* **74**, 193401 (2006).

$^{3}$A. S. Moreira, F. Sato, V. Rodrigues, S. O. Dantas, D. Ugarte, and D. S. Galvão, *Nano Lett.* **4**(7), 1187-1191 (2004).

$^{4}$J. Bettini, F. Sato, P. Z. Coura, S. O. Dantas, D. S. Galvao, and D. Ugarte, *Nat. Nanotechnol.* **1**(3), 182-185 (2006).

$^{5}$V. Rodrigues and D. Ugarte, *Nanotechnology* **13**, 404-408 (2002).

$^{6}$S. V. Kolesnikov, I. N. Kolesnikova, A. L. Klavsyuk, and A. M. Saletsky, *EPL* **103**, 48002 (2013).

$^{7}$J. Diao, K. Gall, and M. L. Dunn, *Nano Lett.* **4**, 1863-1867 (2004).

$^{8}$G. M. Finbow, R. M. Lynden-Bell, and I. R. McDonald, *Mol. Phys.* **92**, 705-714 (1997).

$^{9}$S. K. R. S. Sankaranarayanan, V. R. Bhethanabotla, and B. Joseph, *Phys. Rev. B* **76**, 134117 (2007).

$^{10}$M. R. Sørensen, M. Brandbyge, and K. W. Jacobsen, *Phys. Rev. B* **57**(6), 3283-3294 (1998).

$^{11}$S. K. Deb Nath, *Comput. Mater. Sci.* **87**, 138-144 (2014).

$^{12}$H. Ikeda, Y. Qi, T. Cagin, K. Samwer, W. L. Johnson, and W. A. Goddard III, *Phys. Rev. Lett.* **82**, 2900-2903 (1999).

$^{13}$C.-D. Wu, T.-H. Fang, and C.-C. Wu, *Mol. Simul.* **42**(2), 131-137 (2016).

$^{14}$P. S. Branicio and J. P. Rino, *Phys. Rev. B* **62**, 16950-16955 (2000).

$^{15}$H. Ohnishi, Y. Kondo, and K. Takayanagi, *Nature* **395**(6704), 780-783 (1998).

$^{16}$J. I. Pascual, J. Méndez, J. Gómez-Herrero, A. M. Baró, N. García, and V. T. Binh, *Phys. Rev. Lett.* **71**(12), 1852-1855 (1993).

$^{17}$A. I. Yanson, G. Rubio Bollinger, H. E. Van Den Brom, N. AgraÃft, and J. M. Van Ruitenbeek, *Nature* **395**(6704), 783-785 (1998).

$^{18}$G. Rubio, N. Agraït, and S. Vieira, *Phys. Rev. Lett.* **76**(13), 2302-2305 (1996).

$^{19}$F. P. Cometto, P. A. Paredes-Olivera, V. A. Macagno, and E. M. Patrito, *J. Phys. Chem. B* **109**, 21737-21748 (2005).

$^{20}$M. C. Gimenez and W. Schmickler, *J. Chem. Phys.* **134**, 064707 (2011).

$^{21}$L. Reinaudi and M. Cecilia Gimenez, *J. Comput. Theor. Nanosci.* **10**, 2507-2519 (2013).

$^{22}$S. M. Foiles, M. I. Baskes, and M. S. Daw, *Phys. Rev. B* **33**, 7983 (1986).

$^{23}$H. S. Park and J. A. Zimmerman, *Phys. Rev. B* **72**, 054106 (2005).

$^{24}$G. Zhou and Q. Gao, *Solid State Commun.* **136**, 32 (2005).

$^{25}$Y. Gao, F. Wang, T. Zhu, and J. Zhao, *Comput. Mater. Sci.* **49**, 826 (2010).

$^{26}$Y. Liu and J. Zhao, *Comput. Mater. Sci.* **50**, 1418 (2011).

$^{27}$A. Kobler, T. Beuth, T. Klöffel, R. Prang, M. Moosmann, T. Scherer, S. Walheim, H. Hahn, C. Kübel, B. Meyer, T. Schimmel, and E. Bitzek, *Acta Mater.* **92**, 299 (2015).

$^{28}$J. Diao, K. Gall, and M. L. Dunn, *Nat. Mater.* **2**, 656 (2003).

$^{29}$D. T. Ho, Y. Im, S.-Y. Kwon, Y. Y. Earmm, and S. Y. Kim, *Sci. Rep.* **5**, 11050 (2015).

$^{30}$A. Stukowski, *Modell. Simul. Mater. Sci. Eng.* **18**, 015012 (2010), http://ovito.org.

![](./images/814567871471419394_11.jpg)