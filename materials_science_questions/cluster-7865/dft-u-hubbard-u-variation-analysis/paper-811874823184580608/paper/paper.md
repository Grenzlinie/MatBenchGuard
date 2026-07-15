![](./images/811874823184580608_1.jpg)

Energy levels of oxygen vacancies in BiFeO3 by screened exchange

S. J. Clark and J. Robertson

Citation: *Appl. Phys. Lett.* 94, 022902 (2009); doi: 10.1063/1.3070532
View online: http://dx.doi.org/10.1063/1.3070532
View Table of Contents: http://apl.aip.org/resource/1/APPLAB/v94/i2
Published by the AIP Publishing LLC.

---

Additional information on Appl. Phys. Lett.
Journal Homepage: http://apl.aip.org/
Journal Information: http://apl.aip.org/about/about_the_journal
Top downloads: http://apl.aip.org/features/most_downloaded
Information for Authors: http://apl.aip.org/authors

ADVERTISEMENT

![](./images/811874823184580608_2.jpg)

APPLIED PHYSICS LETTERS 94, 022902 (2009)

# Energy levels of oxygen vacancies in $BiFeO_{3}$ by screened exchange

S. J. Clark$^{1,a)}$ and J. Robertson$^{2,b)}$
$^{1}$Department of Physics, University of Durham, South Road, Durham DH1 3LE, United Kingdom
$^{2}$Department of Engineering, Cambridge University, Cambridge CB2 1PZ, United Kingdom

(Received 29 October 2008; accepted 20 December 2008; published online 13 January 2009)

The oxygen vacancy in $BiFeO_{3}$ is calculated to be a double donor with states 0.6 eV below the conduction band edge, consistent with cathodoluminescence and electronic conductivity data. The atomic configurations were relaxed using the local density approximation plus Hubbard $U$ (LDA $+U$) to the electron-correlation energy for each defect charge state to ensure that the oxide had a nonzero band gap. The defect formation energies were calculated using the screened exchange (sX) functional. © 2009 American Institute of Physics. [DOI: 10.1063/1.3070532]

There is increasing interest in materials that display simultaneous ferroelectric and magnetic properties, the multiferroics, $^{1-4}$ of which $BiFeO_{3}$ (BFO) is the best known example. BFO has both its Néel temperature and Curie temperature well above room temperature. It has a very large remnant polarization of $\sim 90\ \mu C/cm^{2}$ of interest for ferroelectric nonvolatile memories. However, BFO can show rather high electrical leakage currents, which mask the measurement of the ferroelectric polarization curve and could short circuit ferroelectric storage capacitors. $^{5-7}$ It is therefore important to know if the leakage is intrinsic or extrinsic.

We previously calculated the band gap of BFO and its Schottky barrier heights and concluded that the leakage currents were extrinsic in origin. $^{8}$ This is consistent with experiment data, which shows that leakage can be reduced by optimizing growth conditions and aliovalent doping. $^{6}$ The leakage current has been attributed to oxygen vacancies, which is equivalent to a valence change of Fe from 3+ to $2+.^{9}$ We calculate here the energy levels of the oxygen vacancy and find they are 0.6 eV below the conduction band edge and consistent with them being the cause of leakage.

The antiferromagnetism of BFO arises from the partial filled Fe $3d$ band, and its band gap arises from the ferroelectric lattice distortion $and$ the on-site correlation energy of the Fe $3d$ electrons. $^{10}$ This causes certain difficulties in accurate band structure calculations. The standard method to calculate band structures uses the local spin density approximation (LSDA) or generalized gradient approximation functional to represent the valence electron's exchange-correlation energy. $^{10,11}$ This functional provides an accurate description of ground state properties such as lattice constants. However, it does not give band gaps correctly due to a discontinuity in the derivative of the exchange-correlation energy versus particle number across the gap. The incorrect band gap is often worse in correlated electron systems (a classic example being NiO, where the simple LDA gives a metal, rather than a 4.2 eV gap semiconductor). There are ways to fix this problem at varying computational cost. GW is one of the most accurate methods but it is very expensive and hence difficult to perform calculations of defect properties in materials.

The calculation of defect levels requires the use of a supercell of 50-200 atoms containing the defect, in which the atomic coordinates are then relaxed to minimize the total energy. This requires the use of an efficient but accurate functional. The usual method of calculating defect levels while giving a good band gap is to relax the atomic structure in LSDA and then apply a more accurate but expensive method as postprocessing to that LSDA atomic structure. $^{12-15}$ This method is dangerous for BFO, as the LSDA gives a small band gap, so it could give the incorrect defect structure. We need a functional that is efficient enough to treat large supercells and give the right band gap. The simplest of these is $LDA+U$. This method supplements the LDA functional by an on-site correlation energy $U$ for the Fe $3d$ electrons. $^{16}$ The $LDA+U$ method is appropriate for fixing band gaps in open shell systems such as NiO or BFO. $LDA+U$ was previously used by Neaton $et$ $al.^{10}$ to calculate the band structure of BFO. Another way is to relax the structure using a local orbital basis set and a hybrid functional such as B3LYP. $^{17}$ This is suitable for localized deep levels. However, a more complete basis set of plane waves is more appropriate for near shallow levels. This paper represents a calculation of defect geometries in large supercells using the $LDA+U$ method.

In the present calculation, we use the plane wave, total energy pseudopotential code CASTEP. $^{18}$ The electron-ion interactions are described by nonlocal norm-conserving pseudopotentials. The valence electron wave functions are expanded in a plane-wave basis set to a kinetic energy cutoff of 800 eV, which converges total energy differences to better that 1 meV/atom. Integrations over the Brillouin zone used the $k$-point sampling method of Monkhorst and Pack with a grid that converges the energies to a similar accuracy. The $U$ is an empirical parameter in the $LDA+U$ scheme and is fitted to the band gap and average valence band width of our screened exchange band structure $^{8}$ of bulk BFO, we find $U$ =4.7 eV. Geometry optimizations are performed self-consistently using a minimization scheme and the Hellmann-Feynman forces. Geometries are converged when forces are below 0.01 eV/Å.

An oxygen vacancy is introduced into a 120 atom supercell of BFO. The lattice parameters of this $3×2\sqrt{2}×2\sqrt{2}$ cell are fixed to that of the calculated bulk cell. The internal atomic positions are then relaxed separately in $LDA+U$ for the three possible charge states $q$=0, +1, and +2 of the vacancy (other charge states do not occur for the defect). For the supercell we use a single $k$-point (1/4,1/4,1/4) for Brillouin zone integrations, which converges the quantities faster than the $\Gamma$ point with respect to the supercell size. $^{19}$ The total energy $(E_{q})$ is calculated for the defect cell of charge $q$, the

$^{a)}$Electronic mail: s.j.clark@durham.ac.uk.
$^{b)}$Electronic mail: jr@eng.cam.ac.uk.

0003-6951/2009/94(2)/022902/3/$23.00
94, 022902-1
© 2009 American Institute of Physics

perfect cell $(E_{H})$ of charge $q$, and a perfect cell of charge 0. This allows us to calculate the defect formation energy, $H_{q}$, as a function of the relative Fermi energy $(\Delta E_{F})$ from the valence band edge $E_{V}$ and the relative chemical potential $(\Delta \mu)$ of element $\alpha,^{20}$

$$
\begin{aligned}
H_{q}(E_{F}, \mu)=& {\left[E_{q}-E_{H}\right]+q(E_{V}+\Delta E_{F}) } \\
&+\sum_{\alpha} n_{\alpha}(\mu_{\alpha}^{0}+\Delta \mu_{\alpha}),
\end{aligned}
$$

where $qE_{V}$ is the change in energy of the Fermi level when charge $q$ is added. Essentially, this is the shift in the average electrostatic potential due to the change in charge of the system with respect to the uncharged system. The oxygen chemical potential $(\mu^{0})$ is referred to that of the $O_{2}$ molecule, taken as zero, and $n_{\alpha}$ is the number of $\alpha$ atoms.

The total energy of the three cells is then also calculated by screened exchange on the structures found by LDA+$U$. These values are used, as these have more physical basis than those from LDA+$U$. The screened exchange method $^{8,21,22}$ is a generalized Kohn–Sham functional, where the single particle orbitals are used to construct the nonlocal exchange operator while introducing an exponential screening term. This improves the physical description of electron exchange and correlation beyond LDA and gives accurate total energies and correct band gaps at moderate cost.

Antiferromagnetic (AF) BFO has the $R3c$ structure, a distortion of the cubic perovskite lattice, in which the $FeO_{6}$ octahedra are tilted and the Fe and Bi ions move toward each other along $\langle 111 \rangle$ so that the O site becomes fourfold coordinated by two Fe and two Bi. Figure 1(a) shows the standard LSDA band structure of the AF $R3c$ BFO. We see that there is a small band gap of 0.43 eV in LSDA. Figure 1(b) shows the band structure of AF $R3c$ BFO calculated with by screened exchange. The band gap is calculated to be 2.8 eV. This agrees well with subsequent measurements of the optimal gap of 2.6–2.8 eV. $^{23,24}$ For reference, we show in Fig. 1(c) the band structure of the cubic BFO in the screened exchange method. This verifies that there is no band gap in the cubic polytype even with a method that is capable of giving it. Note that the cubic phase corresponds to the metallic phase well above the Néel temperature, where we assume that there is still some local order, so that spins along $\langle 111 \rangle$ still tend to lie antiparallel, so we show the band structure for a cell of two cubic cells along $\langle 111 \rangle$.

Figure 2 shows the O vacancy formation energy from screened exchange as a function of the Fermi energy for oxygen-rich conditions, where the O chemical potential is that of the $O_{2}$ molecule. Figure 2(b) shows the formation energy for oxygen-poor conditions of $\mu(\text{O})$=$-1.97$ eV corresponding to the $Bi_{2}O_{3}$/Bi equilibrium. A formation energy of 2.6 eV for the neutral vacancy in O-poor conditions is rather low compared to $SrTiO_{3}$, and it accounts for the ease of forming vacancies at high temperatures.

We see that the oxygen vacancy gives rise to +/2+ and 0/+ transitions at 0.6 eV below the conduction band edge. The energy level is borderline deep. The energy level is the same for the 0/+ and the +/2+ transitions. This equality does not mean that the level is effective masslike, as the +/2+ level would then be twice as deep. It means that the level shift due to a slight lattice relaxation balances the extra attraction in the 2+ state. The ions around the vacancy relax outward by 0.092 Å for the 2+ state. The vacancy state eigenvalues lie $\sim$0.4 eV below the conduction band, Fig. 2(c). These are consistent with the formation energies.

![](./images/811874823184580608_3.jpg)

FIG. 1. Band structure of AF BFO in $R3c$ structure (a) in LSDA, (b) in screened exchange, and in the (c) band structure of cubic BFO in screened exchange, for reference.

Figure 3(a) shows the charge density for the defect state in the Fe–O–Fe plane. The white ball represents the oxygen vacancy site. The defect state is seen to be mainly localized on the $d$ states of the two Fe atoms adjacent to the vacancy, rather than inside the vacancy itself, and rather delocalized onto adjacent cells with a Bohr radius of $\sim$4.3 Å. Figure 3(b) shows the charge density in the plane of the vacancy and its Bi neighbors. We see that the defect state is not lo-

![](./images/811874823184580608_4.jpg)

FIG. 2. (Color online) Formation energy of the O vacancy vs Fermi energy for (a) O-rich conditions ($\mu_O$=0 eV) and (b) O-poor conditions ($\mu_O$=-1.97 eV). (c) Eigenvalues of vacancy levels for each charge state 0, +1, and +2.

![](./images/811874823184580608_5.jpg)

FIG. 3. (Color online) Charge density of the O vacancy defect level (a) through a plane containing Fe atoms and (b) a plane containing the vacancy and Bi atoms. White sphere is the vacancy. Fe=gray, Bi=yellow, O=red.

calized on Bi states. This is consistent with the bulk band structure where the conduction band minimum is formed mainly of Fe states and Bi states lie higher.

The presence of a moderately shallow oxygen vacancy state is consistent with experimental observations. $^{24-28}$ Hauser et al. $^{24}$ found a transition in cathodoluminescence at $\sim$0.3 eV below the conduction band edge, whose properties are consistent with the oxygen vacancy. A calculated level depth of 0.6 eV is similar to a trap depth of 0.65-0.8 eV found by Pabst et al. $^{26}$ and 0.68 eV from the temperature dependence of the conductivity. $^{27}$ The ability to compensate self-doping and oxygen deficiency by aliovalent metals is consistent with a moderately shallow defect. $^{6,25-28}$

In summary, we calculated the formation energy of oxy- gen vacancy in BFO and found it to create a marginally deep level 0.6 eV below the conduction band edge. We used the LDA+$U$ method to give the atomic geometry and screened exchange to give the formation energies.

$^{1}$J. Wang, J. B. Neaton, H. Zheng, V. Nagarajan, S. B. Ogale, B. Liu, D. Viehland, V. Vaithyanathan, D. G. Schlom, U. V. Waghare, N. A. Spaldin, K. M. Rabe, M. Wuttig, and R. Ramesh, Science 299, 1719 (2003).
$^{2}$R. Ramesh and N. Spaldin, Nature Mater. 6, 21 (2007).
$^{3}$N. A. Hill, J. Phys. Chem. B 104, 6694 (2000).
$^{4}$R. Palai, R. S. Katiyar, H. Schmid, P. Tissot, S. J. Clark, J. Robertson, S. A. T. Redfern, G. Catalan, and J. F. Scott, Phys. Rev. B 77, 014110 (2008).
$^{5}$K. Y. Yun, D. Ricinschi, T. Kanashima, and M. Okuyama, Appl. Phys. Lett. 89, 192902 (2006).
$^{6}$S. K. Singh and H. Ishiwara, Jpn. J. Appl. Phys., Part 2 44, L734 (2005); S. K. Singh, H. Ishiwara, and K. Maruyama, Appl. Phys. Lett. 88, 262908 (2006).
$^{7}$D. Lebeugle, D. Colson, A. Forget, and M. Viret, Appl. Phys. Lett. 91, 022907 (2007).
$^{8}$S. J. Clark and J. Robertson, Appl. Phys. Lett. 90, 132903 (2007).
$^{9}$C. Ederer and N. A. Spaldin, Phys. Rev. B 71, 224103 (2005).
$^{10}$J. B. Neaton, C. Ederer, U. V. Waghmare, N. A. Spaldin, and K. M. Rabe, Phys. Rev. B 71, 014113 (2005).
$^{11}$P. Ravindran, R. Vidya, A. Kjekshus, H. Fjellvag, and O. Eriksson, Phys. Rev. B 74, 224412 (2006).
$^{12}$K. Xiong, J. Robertson, M. C. Gibson, and S. J. Clark, Appl. Phys. Lett. 87, 183505 (2005).
$^{13}$P. Broqvist and A. Pasquarello, Appl. Phys. Lett. 89, 262904 (2006).
$^{14}$K. Xiong, J. Robertson, and S. J. Clark, J. Appl. Phys. 102, 083710 (2007).
$^{15}$F. Oba, A. Togo, I. Tanaka, J. Paier, and G. Kresse, Phys. Rev. B 77, 245202 (2008).
$^{16}$V. I. Anisimov, J. Zaanen, and O. K. Andersen, Phys. Rev. B 44, 943 (1991).
$^{17}$C. Di Valentin, G. Pacchioni, and A. Selloni, Phys. Rev. Lett. 97, 166803 (2006).
$^{18}$M. D. Segall, P. J. D. Lindan, M. J. Probert, C. J. Pickard, P. J. Hasnip, S. J. Clark, and M. C. Payne, J. Phys.: Condens. Matter 14, 2717 (2002).
$^{19}$M. I. J. Probert and M. C. Payne, Phys. Rev. B 67, 075204 (2003).
$^{20}$S. Lany and A. Zunger, Phys. Rev. B 78, 235104 (2008).
$^{21}$B. M. Bylander and L. Kleinman, Phys. Rev. B 41, 7868 (1990).
$^{22}$J. Robertson, K. Xiong, and S. J. Clark, Phys. Status Solidi B 243, 2054 (2006).
$^{23}$S. R. Basu, L. W. Martin, Y. H. Chu, M. Gajek, R. Ramesh, R. C. Rai, X. Xu, J. L. Musfeldt, Appl. Phys. Lett. 92, 091905 (2008).
$^{24}$A. J. Hauser, J. Zhang, L. Meier, R. A. Ricciardo, P. M. Woodward, T. L. Gustafson, L. J. Brillson, and F. Y. Yang, Appl. Phys. Lett. 92, 222901 (2008).
$^{25}$C. Wang, T. Hidetoshi, H. Fujino, X. Zhao, E. Kume, T. Horiuchi, and S. Sakai, J. Appl. Phys. 99, 054104 (2006).
$^{26}$G. W. Pabst, L. W. Martin, Y. H. Chu, and R. Ramesh, Appl. Phys. Lett. 90, 072902 (2007).
$^{27}$H. Yang, M. Jain, N. Suvorova, H. Zhou, H. M. Luo, D. M. Feldman, P. C. Dowden, R. F. DePaula, S. R. Foltyn, and Q. X. Jia, Appl. Phys. Lett. 91, 072911 (2007).
$^{28}$H. W. Jang, S. H. Baek, C. B. Eom, and R. Ramesh, Appl. Phys. Lett. 92, 062910 (2008).