# Odd−Even Effects in Self-Assembled Monolayers of ω-(Biphenyl-4-yl)alkanethiols: A First-Principles Study

Georg Heimel, $^{*, \dagger, \ddagger}$ Lorenz Romaner, $^{\S}$ Jean-Luc Brédas, $^{\dagger}$ and Egbert Zojer $^{\S}$

School of Chemistry and Biochemistry and Center for Organic Photonics and Electronics, Georgia Institute of Technology, Atlanta, Georgia 30332-0400, Department of Material Science and Engineering, Massachusetts Institute of Technology, Cambridge, Massachusetts 02139-4307, and Institute of Solid State Physics, Graz University of Technology, Petersgasse 16, A-8010 Graz, Austria

Received August 2, 2007. In Final Form: October 12, 2007

Conjugated molecules with a saturated alkyl linker between a thiol docking group and the $\pi$-conjugated core have been shown to form self-assembled monolayers (SAMs) with a high degree of long-range order and uniformity. Additionally, pronounced odd−even effects have been observed in a number of properties characterizing these SAMs. We focus on $\omega$-(biphenyl-4-yl)alkanethiols with $n = 0-6$ $-(CH_2)_n-$ units deposited on Au(111) and investigate the microscopic origin of these odd−even effects in terms of the local sulfur−gold bonding geometry by employing first-principles calculations. An additional structural parameter, the torsion angle between the two phenyl rings in the biphenyl moiety, is identified and its relation to the experimentally observed odd−even effects is discussed. More importantly, we address relevant quantities for the application of these SAMs in molecular electronic devices, in particular, the modification of the work function of the underlying metal substrate and the energetic alignment of the molecular orbitals in the SAM with the Fermi level. While no clear trend emerges for the former, we find pronounced odd−even effects for the latter. Furthermore, the insertion of a single methylene unit between the biphenyl core and the thiol appears to largely decouple the valence electronic systems of the $\pi$-conjugated segment and the gold substrate. Our results thus provide a solid theoretical basis for the interface energetics in this important class of systems.

## Introduction

Self-assembled monolayers (SAMs) of organic molecules on a variety of substrates, in particular thiols chemisorbed on (noble) metal surfaces, have been the focus of intense multidisciplinary research for many years. $^{1-6}$ A number of applications for such SAMs has been explored, including nanolithography and chemical sensing. $^{7-15}$ Notably, SAMs have been employed in organic electronic devices to modify the work function $(\Phi)$ of the electrodes. $^{16-25}$ The latter is directly related to the barriers for charge-carrier injection at the electrode-organic interface, $^{26,27}$ i.e., the energetic alignment of the Fermi energy $(E_F)$ of the electrode with the conducting states in the active organic layer. $^{26,27}$ Moreover, SAMs play a central role in the field of single-molecule electronics, $^{28-34}$ where the energetic alignment of $E_F$ with the conducting states of the molecules that *form* the SAM is a key parameter. $^{35,36}$

* Corrsponding author. E-mail: georg.heimel@physik.hu-berlin.de.
† Georgia Institute of Technology.
‡ Massachusetts Institute of Technology.
§ Graz University of Technology.

(1) Love, J. C.; Estroff, L. A.; Kriebel, J. K.; Nuzzo, R. G.; Whitesides, G. M. *Chem. Rev.* 2005, 105, 1103−1169.
(2) Poirier, G. E. *Chem. Rev.* 1997, 97, 1117−1127.
(3) Schreiber, F. *Prog. Surf. Sci.* 2000, 65, 151−256.
(4) Schreiber, F. J. *Phys.: Condens. Matter* 2004, 16, R881−R900.
(5) Schwartz, D. K. *Annu. Rev. Phys. Chem.* 2001, 52, 107−137.
(6) Ulman, A. *Chem. Rev.* 1996, 96, 1533−1554.
(7) Eck, W.; Stadler, V.; Geyer, W.; Zharnikov, M.; Gölzhäuser, A.; Grunze, M. *Adv. Mater.* 2000, 12, 805−808.
(8) Felgenhauer, T.; Yan, C.; Geyer, W.; Rong, H. T.; Gölzhäuser, A.; Buck, M. *Appl. Phys. Lett.* 2001, 79, 3323−3325.
(9) Genzer, J.; Efimenko, K. *Science* 2000, 290, 2130−2133.
(10) Geyer, W.; Stadler, V.; Eck, W.; Zharnikov, M.; Gölzhäuser, A.; Grunze, M. *Appl. Phys. Lett.* 1999, 75, 2401−2403.
(11) Gooding, J. J.; Mearns, F.; Yang, W. R.; Liu, J. Q. *Electroanal.* 2003, 15, 81−96.
(12) Jennings, G. K.; Laibinis, P. E. *Colloids Surf. A* 1996, 116, 105−114.
(13) Kleineberg, U.; Brechling, A.; Sundermann, M.; Heinzmann, U. *Adv. Funct. Mater.* 2001, 11, 208−212.
(14) Kobayashi, S.; Nishikawa, T.; Takenobu, T.; Mori, S.; Shimoda, T.; Mitani, T.; Shimotani, H.; Yoshimoto, N.; Ogawa, S.; Iwasa, Y. *Nat. Mater.* 2004, 3, 317−322.
(15) Halik, M.; Klauk, H.; Zschieschang, U.; Schmid, G.; Dehm, C.; Schütz, M.; Maisch, S.; Effenberger, F.; Brunnbauer, M.; Stellacci, F. *Nature* 2004, 431, 963−966.
(16) Campbell, I. H.; Kress, J. D.; Martin, R. L.; Smith, D. L.; Barashkov, N. N.; Ferraris, J. P. *Appl. Phys. Lett.* 1997, 71, 3528−3530.
(17) Campbell, I. H.; Rubin, S.; Zawodzinski, T. A.; Kress, J. D.; Martin, R. L.; Smith, D. L.; Barashkov, N. N.; Ferraris, J. P. *Phys. Rev. B* 1996, 54, 14321−14324.
(18) de Boer, B.; Hadipour, A.; Mandoc, M. M.; van Woudenbergh, T.; Blom, P. W. M. *Adv. Mater.* 2005, 17, 621−625.
(19) Ganzorig, C.; Kwak, K. J.; Yagi, K.; Fujihira, M. *Appl. Phys. Lett.* 2001, 79, 272−274.
(20) Hatton, R. A.; Day, S. R.; Chesters, M. A.; Willis, M. R. *Thin Solid Films* 2001, 394, 292−297.
(21) Yan, H.; Huang, Q. L.; Cui, J.; Veinot, J. G. C.; Kern, M. M.; Marks, T. J. *Adv. Mater.* 2003, 15, 835−838.
(22) Zehner, R. W.; Parsons, B. F.; Hsung, R. P.; Sita, L. R. *Langmuir* 1999, 15, 1121−1127.
(23) Zuppiroli, L.; Si-Ahmed, L.; Kamaras, K.; Nüesch, F.; Bussac, M. N.; Ades, D.; Siove, A.; Moons, E.; Grätzel, M. *Eur. J. Phys. B* 1999, 11, 505−512.
(24) Alloway, D. M.; Hofmann, M.; Smith, D. L.; Gruhn, N. E.; Graham, A. L.; Colorado, R.; Wysocki, V. H.; Lee, T. R.; Lee, P. A.; Armstrong, N. R. J. *Phys. Chem. B* 2003, 107, 11690−11699.
(25) Ihm, K.; Kim, B.; Kang, T. H.; Kim, K. J.; Joo, M. H.; Kim, T. H.; Yoon, S. S.; Chung, S. *Appl. Phys. Lett.* 2006, 89, 033504.
(26) Ishii, H.; Sugiyama, K.; Ito, E.; Seki, K. *Adv. Mater.* 1999, 11, 605−625.
(27) Kahn, A.; Koch, N.; Gao, W. Y. J. *Polym. Sci., Part B* 2003, 41, 2529−2548.
(28) Bumm, L. A.; Arnold, J. J.; Cygan, M. T.; Dunbar, T. D.; Burgin, T. P.; Jones, L.; Allara, D. L.; Tour, J. M.; Weiss, P. S. *Science* 1996, 271, 1705−1707.
(29) Chen, J.; Reed, M. A.; Rawlett, A. M.; Tour, J. M. *Science* 1999, 286, 1550−1552.
(30) Elbling, M.; Ochs, R.; Koentopp, M.; Fischer, M.; von Hänisch, C.; Weigend, F.; Evers, F.; Weber, H. B.; Mayor, M. *Proc. Natl. Acad. Sci.* 2005, 102, 8815−8820.
(31) Jiang, P.; Morales, G. M.; You, W.; Yu, L. P. *Angew. Chem., Int. Ed.* 2004, 43, 4471−4475.
(32) Kushmerick, J. G.; Holt, D. B.; Yang, J. C.; Naciri, J.; Moore, M. H.; Shashidhar, R. *Phys. Rev. Lett.* 2002, 89, 086802.
(33) Park, J.; Pasupathy, A. N.; Goldsmith, J. I.; Chang, C.; Yaish, Y.; Petta, J. R.; Rinkoski, M.; Sethna, J. P.; Abruna, H. D.; McEuen, P. L.; Ralph, D. C. *Nature* 2002, 417, 722−725.
(34) Reed, M. A.; Chen, J.; Rawlett, A. M.; Price, D. W.; Tour, J. M. *Appl. Phys. Lett.* 2001, 78, 3735−3737.
(35) Vondrak, T.; Wang, H.; Winget, P.; Cramer, C. J.; Zhu, X. Y. *J. Am. Chem. Soc.* 2000, 122, 4700−4707.

10.1021/la7023814 CCC: $40.75
© 2008 American Chemical Society
Published on Web 12/12/2007

SAM of $\omega$-(Biphenyl-4-yl)alkanethiols
Langmuir, Vol. 24, No. 2, 2008 475

Because the interfacial electronic structure in SAMs is quite sensitive to the local fluctuations of the geometry on an atomic scale, $^{37-46}$ a high degree of long-range order and uniformity in the SAMs is desirable for both applications and fundamental studies. While pure alkylthiols are known to form SAMs that exhibit order on a large scale, $^{47-55}$ $\pi$-conjugated thiols seem to be a better choice for applications in organic- and single-molecule electronics because of their intrinsic semiconducting properties. It appears, however, that the competition between the most favorable hybridization of the sulfur docking groups and the intermolecular packing forces between the $\pi$-conjugated back-bones often leads to a large number of defects in these SAMs. $^{55-61}$

This problem has been addressed by inserting one or more methylene linkers $(-CH_{2}-$ groups) between the thiol and the $\pi$-conjugated core. $^{55,59-62}$ In particular, biphenyls with an alkyl linker to the thiol docking group, i.e., $\omega$-(biphenyl-4-yl)-alkanethiols, form SAMs of superior order and quality. $^{63,64}$ Moreover, varying the length of the alkyl spacer between $-SH$ and the conjugated core leads to intriguing odd-even effects with the number $(n)$ of $-CH_{2}-$ groups. These odd-even effects have been observed in the packing density, core-level shifts in X-ray photoelectron spectroscopy (XPS), contact-angle measurements, reflection-absorption infrared spectroscopy (RAIRS), near-edge X-ray absorption fine-structure spectroscopy (NEX-AFS), ellipsometry, and many more. $^{65-74}$

(36) Xue, Y. Q.; Datta, S.; Ratner, M. A. J. Chem. Phys. 2001, 115, 4292-4299.
(37) Donhauser, Z. J.; Mantooth, B. A.; Kelly, K. F.; Bumm, L. A.; Monnell, J. D.; Stapleton, J. J.; Price, D. W.; Rawlett, A. M.; Allara, D. L.; Tour, J. M.; Weiss, P. S. Science 2001, 292, 2303-2307.
(38) Lewis, P. A.; Inman, C. E.; Maya, F.; Tour, J. M.; Hutchison, J. E.; Weiss, P. S. J. Am. Chem. Soc. 2005, 127, 17421-17426.
(39) Patrone, L.; Palacin, S.; Charlier, J.; Armand, F.; Bourgoin, J. P.; Tang, H.; Gauthier, S. Phys. Rev. Lett. 2003, 91, 096802.
(40) Venkataraman, L.; Klare, J. E.; Tam, I. W.; Nuckolls, C.; Hybertsen, M. S.; Steigerwald, M. L. Nano Lett. 2006, 6, 458-462.
(41) Xu, B. Q.; Tao, N. J. J. Science 2003, 301, 1221-1223.
(42) Xu, B. Q.; Xiao, X. Y.; Tao, N. J. J. Am. Chem. Soc. 2003, 125, 16164-16165.
(43) Xu, B. Q. Q.; Li, X. L. L.; Xiao, X. Y. Y.; Sakaguchi, H.; Tao, N. J. J. Nano Lett. 2005, 5, 1491-1495.
(44) Xue, Y. Q.; Ratner, M. A. Phys. Rev. B 2003, 68, 115407.
(45) Yaliraki, S. N.; Kemp, M.; Ratner, M. A. J. Am. Chem. Soc. 1999, 121, 3428-3434.
(46) Yasuda, S.; Yoshida, S.; Sasaki, J.; Okutsu, Y.; Nakamura, T.; Taninaka, A.; Takeuchi, O.; Shigekawa, H. J. Am. Chem. Soc. 2006, 128, 7746-7747.
(47) Arce, F. T.; Vela, M. E.; Salvarezza, R. C.; Arvia, A. J. J. Chem. Phys. 1998, 109, 5703-5706.
(48) Arce, F. T.; Vela, M. E.; Salvarezza, R. C.; Arvia, A. J. Langmuir 1998, 14, 7203-7212.
(49) Delamarche, E.; Michel, B.; Gerber, C.; Anselmetti, D.; Guntherodt, H. J.; Wolf, H.; Ringsdorf, H. Langmuir 1994, 10, 2869-2871.
(50) Kondoh, H.; Kodama, C.; Sumida, H.; Nozoye, H. J. Chem. Phys. 1999, 111, 1175-1184.
(51) Poirier, G. E. Langmuir 1999, 15, 1167-1175.
(52) Poirier, G. E.; Pylant, E. D. Science 1996, 272, 1145-1148.
(53) Poirier, G. E.; Tarlov, M. J. Langmuir 1994, 10, 2853-2856.
(54) Riposan, A.; Liu, G. Y. J. Phys. Chem. B 2006, 110, 23926-23937.
(55) Yang, G. H.; Liu, G. Y. J. Phys. Chem. B 2003, 107, 8746-8759.
(56) Dhirani, A. A.; Zehner, R. W.; Hsung, R. P.; Guyot-Sionnest, P.; Sita, L. R. J. Am. Chem. Soc. 1996, 118, 3319-3320.
(57) Duan, L.; Garrett, S. J. J. Phys. Chem. B 2001, 105, 9812-9816.
(58) Ishida, T.; Mizutani, W.; Azehara, H.; Sato, F.; Choi, N.; Akiba, U.; Fujihira, M.; Tokumoto, H. Langmuir 2001, 17, 7459-7463.
(59) Fuxen, C.; Azzam, W.; Arnold, R.; Witte, G.; Terfort, A.; Wöll, C. Langmuir 2001, 17, 3689-3695.
(60) Ishida, T.; Mizutani, W.; Choi, N.; Akiba, U.; Fujihira, M.; Tokumoto, H. J. Phys. Chem. B 2000, 104, 11680-11688.
(61) Tao, Y. T.; Wu, C. C.; Eu, J. Y.; Lin, W. L.; Wu, K. C.; Chen, C. H. Langmuir 1997, 13, 4018-4023.
(62) Ishida, T.; Mizutani, W.; Akiba, U.; Umemura, K.; Inoue, A.; Choi, N.; Fujihira, M.; Tokumoto, H. J. Phys. Chem. B 1999, 103, 1686-1690.
(63) Azzam, W.; Cyganik, P.; Witte, G.; Buck, M.; Wöll, C. Langmuir 2003, 19, 8262-8270.
(64) Cyganik, P.; Buck, M.; Azzam, W.; Wöll, C. J. Phys. Chem. B 2004, 108, 4989-4996.
(65) Shaporenko, A.; Elbing, M.; Blaszczyk, A.; von Hänisch, C.; Mayor, M.; Zharnikov, M. J. Phys. Chem. B 2006, 110, 4307-4317.

In this contribution, we focus on the consequences of the structural odd-even effects for the most important parameters in the application of this class of SAMs for molecular electronics, i.e., the modification of the substrate work function $(\Delta \Phi)$, the energetic alignment $(\Delta E)$ between the molecular orbitals of the SAM molecules with the electrode $E_{\text{F}}$, and the degree of electronic coupling between metal and molecules. We focus on SAMs of $\omega$-(biphenyl-4-yl)alkanethiols on Au(111) with an alkyl spacer containing $n=0-6$ methylene groups between the biphenyl core and the $-SH$ docking group. Employing density-functional theory (DFT), we investigate the local bonding geometry at the sulfur-gold interface as well as the orientation of the molecules on the surface. We relate our findings to experimental XPS and RAIRS data, suggesting the torsion angle between the two phenyl rings in the biphenyl moiety be considered as an additional internal structural parameter. Subsequently, we study the impact of the length of the alkyl spacer on $\Delta \Phi$ and $\Delta E$ and discuss potential odd-even effects of these two quantities. Importantly, we find that the insertion of a single methylene unit already significantly reduces the perturbation of the molecular electronic structure by the metal.

### Methodology

The basic structure of the systems investigated in the present study is shown in Figure 1a. A gold (111) surface is covered by a monolayer of $\omega$-(biphenyl-4-yl)alkanethiols, where the $\pi$-conjugated core (biphenyl) is separated from the thiol $(-SH)$ docking group by a short chain of $n=0-6$ methylene $(-CH_{2}-)$ linkers (denoted as BPnT). The thiols are assumed to adsorb upon hydrogen removal. Note that, in the present study, we consider an atomically perfect Au(111) surface where the sulfur is located between the fcc-hollow and the bridge site. $^{75-82}$ While different adsorption models have been proposed, some of which involve considerable reconstruction of the Au(111) surface, $^{83-89}$ their inclusion in the present work would

(66) Heister, K.; Rong, H. T.; Buck, M.; Zharnikov, M.; Grunze, M.; Johansson, L. S. O. J. Phys. Chem. B 2001, 105, 6888-6894.
(67) Long, Y. T.; Rong, H. T.; Buck, M.; Grunze, M. J. Electroanal. Chem. 2002, 524, 62-67.
(68) Rong, H. T.; Frey, S.; Yang, Y. J.; Zharnikov, M.; Buck, M.; Wuhn, M.; Wöll, C.; Helmchen, G. Langmuir 2001, 17, 1582-1593.
(69) Shaporenko, A.; Brunnbauer, M.; Terfort, A.; Grunze, M.; Zharnikov, M. J. Phys. Chem. B 2004, 108, 14462-14469.
(70) Shaporenko, A.; Brunnbauer, M.; Terfort, A.; Johansson, L. S. O.; Grunze, M.; Zharnikov, M. Langmuir 2005, 21, 4370-4375.
(71) Tao, F.; Bernasek, S. L. Chem. Rev. 2007, 107, 1408-1453.
(72) Thom, I.; Buck, M. Surf. Sci. 2005, 581, 33-46.
(73) Lee, S.; Puck, A.; Graupe, M.; Colorado, R.; Shon, Y. S.; Lee, T. R.; Perry, S. S. Langmuir 2001, 17, 7364-7370.
(74) Zharnikov, M.; Frey, S.; Rong, H.; Yang, Y. J.; Heister, K.; Buck, M.; Grunze, M. Phys. Chem. Chem. Phys. 2000, 2, 3359-3362.
(75) Bilic, A.; Reimers, J. R.; Hush, N. S. J. Chem. Phys. 2005, 122, 094708.
(76) Cao, Y. P.; Ge, Q. F.; Dyer, D. J.; Wang, L. C. J. Phys. Chem. B 2003, 107, 3803-3807.
(77) Gottschalck, J.; Hammer, B. J. Chem. Phys. 2002, 116, 784-790.
(78) Hayashi, T.; Morikawa, Y.; Nozoye, H. J. Chem. Phys. 2001, 114, 7615-7621.
(79) Morikawa, Y.; Hayashi, T.; Liew, C. C.; Nozoye, H. Surf. Sci. 2002, 507, 46-50.
(80) Nara, J.; Higai, S.; Morikawa, Y.; Ohno, T. J. Chem. Phys. 2004, 120, 6705-6711.
(81) Vargas, M. C.; Giannozzi, P.; Selloni, A.; Scoles, G. J. Phys. Chem. B 2001, 105, 9509-9513.
(82) Yourdshahyan, Y.; Rappe, A. M. J. Chem. Phys. 2002, 117, 825-833.
(83) Fenter, P.; Schreiber, F.; Berman, L.; Scoles, G.; Eisenberger, P.; Bedzyk, M. J. Surf. Sci. 1998, 413, 213-235.
(84) Kondoh, H.; Iwasaki, M.; Shimada, T.; Amemiya, K.; Yokoyama, T.; Ohta, T.; Shimomura, M.; Kono, S. Phys. Rev. Lett. 2003, 90, 066102.
(85) Mazzarello, R.; Cossaro, A.; Verdini, A.; Rousseau, R.; Casalis, L.; Danisman, M. F.; Floreano, L.; Scandolo, S.; Morgante, A.; Scoles, G. Phys. Rev. Lett. 2007, 98, 016102.
(86) Molina, L. M.; Hammer, B. Chem. Phys. Lett. 2002, 360, 264-271.
(87) Morikawa, Y.; Liew, C. C.; Nozoye, H. Surf. Sci. 2002, 514, 389-393.
(88) Yeganeh, M. S.; Dougal, S. M.; Polizzotti, R. S.; Rabinowitz, P. Phys. Rev. Lett. 1995, 74, 1811-1814.
(89) Roper, M. G.; Skegg, M. P.; Fisher, C. J.; Lee, J. J.; Dhanak, V. R.; Woodruff, D. P.; Jones, R. G. Chem. Phys. Lett. 2004, 389, 87-91.

![](./images/811952089566543874_1.jpg)

Figure 1. Schematic side view of the systems under investigation (a). The lateral surface unit cells are indicated by the contours for the high-coverage (b) and low-coverage (c) regime applying to $n =$ 0, 1, 3, 5 methylene segments and $n =$ 2, 4, 6 methylene segments, respectively. The white circles mark the position of the gold atoms in the first (largest diameter), second (intermediate diameter), and third (smallest diameter) layer.

add unnecessary complexity to the discussion and obscure the underlying mechanism we seek to explore here. The angle $\varphi$ ($\theta$) denotes how much the S$-$C axis (the long axis of the $\pi$-conjugated core) is inclined with respect to the surface normal. It has been found that the surface unit cell in the SAM is $p(\sqrt{3} \times 3)$ containing $Z = 2$ molecules for odd numbers $n = 1, 3, 5$ (see Figure 1b) and $p(5\sqrt{3} \times 3)$ containing $Z = 8$ molecules for even numbers $n = 2$, 4, $6^{63,64}$ The packing density thus shows an odd$-$even effect of 20%. As the sheer size of the $p(5\sqrt{3} \times 3)$ surface unit cell renders a treatment on the DFT level computationally impossible, we consider a $p(2\sqrt{3} \times 2)$ unit cell containing $Z = 2$ molecules (see Figure 1c) for even numbers $n = 2, 4, 6$ instead. This packing is very similar to the experimentally observed $p(5\sqrt{3} \times 3)$ $Z = 8$ structure and fully maintains the proposed packing motif, the typical herring-bone structure (see Figure 1). In our calculations, the coverage thus oscillates by 25% between odd and even numbers $n$. In the following, we will refer to the high coverage for odd numbers $n$ as H-coverage and to the low coverage for even numbers $n$ as L-coverage.

It is to be noted that the system with $n = 0$, 4-mercaptobiphenyl (BP0T), exhibits a number of different structural phases in the SAMof which only the H-structure is relevant for the present work. $^{90}$ From a packing point of view, this would place BP0T in the series of odd numbers $n$. However, for the sake of comparison, also the L-coverage for BP0T and the H-coverage for even $n = 2, 4, 6$ were considered.

The theoretical methodology has been extensively described and benchmarked elsewhere. $^{91}$ Here, only a short summary is given. We employed the repeated-slab approach, where the Au(111) surface was modeled by five layers of gold atoms (primitive lattice constant calculated to be $2.952\,\text{\AA}$). We performed DFT calculations employing the PW91 exchange-correlation functional with a plane-wave basis set (cutoff 20 Ryd) for the valence electrons and the projector augmented-wave approach $^{92,93}$ for the treatment of the valence$-$core interactions. A Monkhorst$-$Pack grid $^{94}$ of $8 \times 5 \times 1$ $k$-points was used for the H-coverage and $7 \times 4 \times 1$ for the L-coverage together with a Methfessel$-$Paxton occupation scheme (broadening $0.2\,\text{eV}$). $^{95}$ For a more accurate representation of the density of states (DOS), subsequent, non-self-consistent calculations were performed on a denser $k$-mesh of $12 \times 5 \times 1$ ($9 \times 6 \times 1$) for the H-coverage (L-coverage) together with a tetrahedron scheme for Brillouin-zone integration. $^{96}$ For the sake of clarity, the DOS was then convoluted with a Gaussian (fwhm $= 0.2\,\text{eV}$). With the lateral unit cell dimension as the only input from experiment, $^{63,64}$ all atoms in the molecules and the top two layers of gold were allowed to fully relax toward their equilibrium positions (remaining forces $< 0.01\,\text{eV}/\text{\AA}$); all other gold atoms were kept fixed at their bulk positions. Vibrational frequencies and normal modes were obtained by subsequently displacing all atoms of the molecules along all three spatial coordinates by $\pm 0.02\,\text{\AA}$ and diagonalizing the corresponding Hessian matrix. IR intensities were then evaluated as the square of the derivative of the dipole moment along the surface normal of the slab with respect to each normal mode of vibration. Due to excessive computational requirements, RAIRS spectra were only calculated for two representative molecules from the middle of the series, BP3T (H-packing) and BP4T (L-packing). XPS core-level energies were calculated in the final-state approximation, thus taking into account core$-$hole screening. $^{79,97,98}$ As within this approach only relative core-level shifts can be evaluated, we chose atomic sulfur adsorbed on Au(111) in submonolayer coverage (S $2\text{p}_{3/2}$ peak at a binding energy of $\sim 161.0\,\text{eV}$)$^{99-102}$ as a reference system relative to which the core-level shifts are calculated in order to obtain absolute values.

(90) Azzam, W.; Fuxen, C.; Birkner, A.; Rong, H. T.; Buck, M.; Wöll, C. Langmuir 2003, 19, 4958$-$4968.

(91) Heimel, G.; Romaner, L.; Bredas, J. L.; Zojer, E. Surf. Sci. 2006, 600, 4548$-$4562.

(92) Blöchl, P. E. Phys. Rev. B 1994, 50, 17953$-$17979.

(93) Kresse, G.; Joubert, D. Phys. Rev. B 1999, 59, 1758$-$1775.

(94) Monkhorst, H. J.; Pack, J. D. Phys. Rev. B 1976, 13, 5188$-$5192.

(95) Methfessel, M.; Paxton, A. T. Phys. Rev. B 1989, 40, 3616$-$3621.

(96) Blöchl, P. E.; Jepsen, O.; Andersen, O. K. Phys. Rev. B 1994, 49, 16223$-$16233.

(97) Methfessel, M.; Fiorentini, V.; Oppo, S. Phys. Rev. B 2000, 61, 5229$-$5236.

(98) Vackar, J.; Hyt'ha, M.; Simunek, A. Phys. Rev. B 1998, 58, 12712$-$12720.

(99) Ishida, T.; Choi, N.; Mizutani, W.; Tokumoto, H.; Kojima, I.; Azehara, H.; Hokari, H.; Akiba, U.; Fujihira, M. Langmuir 1995, 15, 6799$-$6806.

(100) Rodriguez, J. A.; Dvorak, J.; Jirsak, T.; Liu, G.; Hrbek, J.; Aray, Y.; Gonzalez, C. J. Am. Chem. Soc. 2003, 125, 276$-$285.

(101) Vericat, C.; Vela, M. E.; Andreasen, G.; Salvarezza, R. C.; Vazquez, L.; Martin-Gago, J. A. Langmuir 2001, 17, 4919$-$4924.

(102) Zhong, C. J.; Brush, R. C.; Anderegg, J.; Porter, M. D. Langmuir 1999, 15, 518$-$525.

SAM of $\omega$-(Biphenyl-4-yl)alkanethiols
Langmuir, Vol. 24, No. 2, 2008 477

![](./images/811952089566543874_2.jpg)

Figure 2. Calculated (left axis) and experimental (right axis) binding energy of the sulfur S $p_{3/2}$ core level (in eV) as a function of the number, $n$, of methylene linkers. Squares show the data for alternating packing density (H-coverage for $n = 1, 3, 5$ and L-coverage for $n = 0, 2, 4, 6$) and circles indicate data points for H-coverage only ($n = 0-6$). For $n = 0$, only the H-coverage has been observed experimentally. For comparative reasons, however, also the value for L-coverage is given (in parentheses). Experimental values extracted from ref 66 are shown as stars.

All calculations were performed with the VASP code; $^{103-106}$ graphics were produced using XCrysDen. $^{107}$

## Results and Discussion

XPS Core-Level Shifts. Before discussing the interfacial electronic structure, we will assess the appropriateness of the (approximate) structural model for the L-coverage and compare our findings to available experimental data. In Figure 2, the calculated XPS core-level energies for the stronger S $2p_{3/2}$ peak of the sulfur species are shown for the H-packing and, for even $n$, also for the L-structures. In good agreement with experiment (also shown in Figure 2), $^{66}$ we observe pronounced odd-even effects in the binding energy. Note that these odd-even effects are also present if we assume H-packing for alkyl spacer lengths $n = 1-4$ (the range for which experimental data is available; see stars in Figure 2); $^{66}$ however, the core-level energies then oscillate in the wrong way (i.e., even $n$ at higher and odd $n$ at lower binding energies, in contrast to experiment). The experimentally observed trend (even $n$ at lower and odd $n$ at higher binding energies) $^{66}$ can only be reproduced if the packing density is allowed to oscillate between even and odd numbered BP$n$Ts.

The excellent agreement of our calculated core-level energies with experimental literature data $^{66}$ in both trend and absolute values supports our structural model for the L-coverage. We thus feel confident in further discussing the origin of the observed odd-even effects in XPS and their relation to the local bonding geometry at the sulfur-gold interface.

Local Au-S-C Geometry. While the experimental determination of the sulfur adsorption site on the surface is not straightforward and remains controversial, $^{83-85,88,89}$ DFT calculations have found the most stable position to be located between the bridge and the fcc-hollow site (Figure 3a). $^{75-82}$ This site can be characterized by two different Au-S distances (Figure 3a): one between the sulfur and the closest two Au atoms ($\text{S-Au}_{1,2}$) and another between the sulfur and a third gold atom ($\text{S-Au}_{3}$); note that both lengths denote interatomic distances in three-dimensional space (Figure 3b) and not just in the (2D) plane of the drawing in Figure 3a. Both $\text{S-Au}_{1,2}$ and $\text{S-Au}_{3}$ are shown in Figure 3d as a function of $n$ (alternating H- and L-coverage for odd and even $n$, respectively; H-packing for $n = 0$). Interestingly, $\text{S-Au}_{1,2}$ stays constant at $\sim 2.5$ Å across the whole series, while $\text{S-Au}_{3}$ shows a pronounced odd-even effect, oscillating between ca. 2.7 and 3.3 Å. These changes in local bonding geometry can be better understood in terms of the evolution of angle $\varphi$ (defined in Figure 3b) between the S-C axis and the surface normal (shown in Figure 3e). The observed odd-even effect in $\varphi$ together with the trends for $\text{S-Au}_{1,2}$ and $\text{S-Au}_{3}$ (Figure 3d) manifest the following evolution in SAM geometry: The sulfur docking group and the adjacent part of the molecule rotate (indicated by the arrows in Figure 3b) around the axis (cross in Figure 3b) defined by the two bridge gold atoms ($\text{Au}_{1,2}$) when changing the number of $-\text{CH}_{2}-$ groups. This means that, for an odd number $n$, the adsorption site is closer to the bridge and it becomes closer to the fcc-hollow for an even number $n$.

It appears that, within the adsorption model assumed in the present work [atomically flat and perfect Au(111)], the sulfur is bound more strongly to the two closer gold atoms ($\text{Au}_{1,2}$) than to the third ($\text{Au}_{3}$). $^{80}$ These two atoms together with the carbon on the first methylene unit (Figure 3) span the (triangular) base of a tetrahedron with the sulfur at its center, indicative of $\text{sp}^{3}$-hybridized sulfur throughout the entire series of the BP$n$Ts. Note that, for a different adsorption scenario involving, e.g., gold adatoms in the topmost layer, the hybridization of the sulfur might be different (e.g., sp). $^{61,66-70}$ Together, the alternating changes in the local bonding geometry are likely to be the cause for the odd-even effects in the XPS signal (Figure 2) as the core-hole screening efficiency is affected by the slightly modulated electron-density distribution around the sulfur atoms.

Molecular Orientation. As $\varphi$ cannot be easily accessed experimentally, the more relevant question is how changes in $\varphi$ propagate across the alkyl spacer to the biphenyl moiety whose inclination to the surface normal, $\theta$, has been experimentally assessed using NEXAFS and RAIRS. $^{68,69}$ As previously suggested, $^{60,61,63,64,66-70}$ the alternating changes in the local bonding geometry around the sulfur-gold interface have their origin in the competition between the energetically most favorable hybridization of the sulfur atom and the intermolecular packing forces between the conjugated backbones. In the absence of the latter, i.e., at coverages lower even than in the L-structures, the preferred angle of the S-C axis with respect to the surface normal was found to be about $\varphi = \theta \approx 60^{\circ}$ for benzenethiol ($n = 0$). $^{75,80}$ The preferred $\theta$ of the biphenyl moieties can be estimated from their bulk crystal structure, $^{108,109}$ where a value of $\theta \approx 18^{\circ}$ is found at a packing density very close to the H-structure. In the case of BP0T, where the rigidity of the molecular backbone forces $\varphi$ and $\theta$ to be (almost) the same, this mismatch between the preferential $\varphi$- and $\theta$-values leads to considerable lateral stress in the SAMs and, thus, to many defects. $^{55-61}$ The average $\varphi = \theta$ in BP0T SAMs was experimentally found to be around $\varphi = \theta \approx 20^{\circ}$ (in the H-packing), $^{110-113}$ indicating that the intermolecular forces prevail over the preferential adsorption geometry of the sulfur. In the case of BP1T, however, both $\varphi$ and $\theta$ can approach their preferred values as the methylene linker introduces a kink between the S-C bond and the long molecular

(103) Kresse, G.; Furthmüller, J. Comp. Mater. Sci. 1996, 6, 15-50.
(104) Kresse, G.; Furthmüller, J. Phys. Rev. B 1996, 54, 11169-11186.
(105) Kresse, G.; Hafner, J. Phys. Rev. B 1993, 47, 558-561.
(106) Kresse, G.; Hafner, J. Phys. Rev. B 1994, 49, 14251-14269.
(107) Kokalj, A. Comp. Mater. Sci. 2003, 28, 155-168.

(108) Hargreaves, A.; Rizvi, S. H. Acta Crystallogr. 1962, 15, 365-373.
(109) Trotter, J. Acta Crystallogr. 1961, 14, 1135-1140.
(110) Frey, S.; Stadler, V.; Heister, K.; Eck, W.; Zharnikov, M.; Grunze, M.; Zeysing, B.; Terfort, A. Langmuir 2001, 17, 2408-2415.
(111) Kang, J. F.; Ulman, A.; Liao, S.; Jordan, R.; Yang, G. H.; Liu, G. Y. Langmuir 2001, 17, 95-106.
(112) Leung, T. Y. B.; Schwartz, P.; Scoles, G.; Schreiber, F.; Ulman, A. Surf. Sci. 2000, 458, 34-52.
(113) Shaporenko, A.; Heister, K.; Ulman, A.; Grunze, M.; Zharnikov, M. J. Phys. Chem. B 2005, 109, 4096-4103.

![](./images/811952089566543874_3.jpg)

![](./images/811952089566543874_4.jpg)

![](./images/811952089566543874_5.jpg)

![](./images/811952089566543874_6.jpg)

![](./images/811952089566543874_7.jpg)

Figure 3. (a) Top view of the sulfur adsorption site that is characterized by two different bond lengths (interatomic distances in three dimensions), $S-Au_{1,2}$ and $S-Au_{3}$. (b) Side view of the local $Au-S-C$ bonding geometry along the $Au_{1}-Au_{2}$ axis (cross) indicating the angle $\varphi$ between the $S-C$ bond and the surface normal. (c) Schematic representation of the odd-even alternation of the angle $\theta$ between the long molecular axis and the surface normal. (d) $S-Au_{1,2}$ (circles) and $S-Au_{3}$ (squares) as a function of the number of methylene spacer groups, $n$. (e) Angles $\varphi$ (squares) and $\theta$ (circles) as a function of $n$.

axis;60,61,63,64,66−70 minimal lateral stress in the SAM favors the formation of highly ordered monolayers maintaining the H-packing. Introducing yet another $-CH_{2}-$ unit in BP2T, the same situation as in BP0T is, in principle, encountered. In this case, however, the SAM relaxes by reducing the packing density (L-structure), thus leading again to high uniformity over large domains.63,64,66,67,69,70

Experimental evidence, including RAIRS, suggests that, subsequently, all odd numbered BP$n$Ts have the biphenyl core standing close to upright (smaller $\theta$), whereas it is more inclined (larger $\theta$) for all even numbered BP$n$Ts, resulting in odd-even effects for the absolute value of $\theta$.68,69,73 Interestingly, we do not observe such odd-even effects in our calculations (see Figure 3e). Rather, $\theta$ oscillates between ca. $+15^{\circ}$ and $-15^{\circ}$ (arrows in Figure 3c), i.e., $|\theta| \approx$ const. (Figure 3e), with the exception of BP1T, where we find only $|\theta| = 5^{\circ}$. While we cannot exclude that the absence of odd-even effects in $|\theta|$ is due to inherent shortcomings in the level of theory/accuracy employed in the present work, and/or the approximate structure for the L-coverage, we tentatively offer an alternate explanation below.

The Inter-Ring Torsion Angle. DFT calculations on molecular crystals of oligo($p$-phenylene)s and similar compounds have been shown to accurately reproduce the orientation of the molecules within the unit cell, the compressibility of the molecular crystals, as well as changes in the molecular orientation upon applying hydrostatic pressure to the crystals;114,115 this is in spite of the well-known inability of local functional based DFT to describe van der Waals interactions.116 We therefore suggest that the apparent discrepancy regarding $\theta$ between experiment and our results is due to an additional structural parameter, the torsion angle $\omega$ between the two phenyl rings.

For oligo($p$-phenylene)s, in general, the molecules in the crystal appear planar *on average* in X-ray diffraction as conformations with $+\omega$ and $-\omega$ are equally probed in the course of the measurement.108,109 The average for the *absolute value of $\omega$*, however, is *nonzero* $(|\omega| \approx 15^{\circ})$ at room temperature,117−121 i.e., any instantaneous event, such as an optical transition, is more likely to happen at a *nonplanar* conformation of the molecules. Moreover, the average $|\omega|$ critically depends on the environment (i.e., the packing density) of the molecules: in the gas phase, a value of $|\omega| = 40 \pm 5^{\circ}$ has been found,122,123 $|\omega| \approx 30^{\circ}$ in solution and melt,124−127 while, in the solid state, hydrostatic pressure was shown to further decrease $|\omega|$ from $\sim$15° to a fully planar conformation at elevated pressure.128−130

(114) Hummer, K.; Puschnig, P.; Ambrosch-Draxl, C. *Phys. Rev. B* 2003, 67, 184105.

(115) Puschnig, P.; Hummer, K.; Ambrosch-Draxl, C.; Heimel, G.; Oehzelt, M.; Resel, R. *Phys. Rev. B* 2003, 67, 235321.

(116) Tsuzuki, S.; Lüthi, H. P. *J. Chem. Phys.* 2001, 114, 3949−3957.

(117) Cailleau, H.; Baudour, J. L.; Meinnel, J.; Dworkin, A.; Moussa, F.; Zeyen, C. M. E. *Faraday Discuss. Chem. Soc.* 1980, 69, 7−18.

(118) Baudour, J. L. *Acta Crystallogr., Sect. B* 1991, 47, 935−949.

(119) Baudour, J. L.; Cailleau, H.; Yelon, W. B. *Acta Crystallogr., Sect. B* 1977, 33, 1773−1780.

(120) Bordat, P.; Brown, R. *Chem. Phys.* 1999, 246, 323−334.

(121) Rietveld, H. M.; Maslen, E. N.; Clews, C. B. *J. Acta Crystallogr., Sect. B* 1970, 26, 693−706.

(122) Almenningen, A.; Bastiansen, O.; Fernholt, L.; Cyvin, B. N.; Cyvin, S. J.; Samdal, S. *J. Mol. Struct.* 1985, 128, 59−76.

(123) Bastiansen, O. *Acta Chem. Scand.* 1949, 3, 408−414.

(124) Eaton, V. J.; Steele, D. J. *Chem. Soc., Faraday Trans. 2* 1973, 69, 1601−1608.

(125) Ghanem, A.; Bokobza, L.; Noel, C.; Marchon, B. *J. Mol. Struct.* 1987, 159, 47−63.

(126) Proutiere, A.; Legoff, D.; Chabanel, M.; Megnassan, E. *J. Mol. Struct.* 1988, 178, 49−61.

(127) Akiyama, M. *Spectrochim. Acta, Part A* 1984, 40, 367−371.

![](./images/811952089566543874_8.jpg)

Figure 4. Inter-ring torsion angle in SAMs of BPnT on Au(111) as a function of the number, n, of methylene spacer units.

![](./images/811952089566543874_9.jpg)

Figure 5. Calculated RAIRS spectra for BP3T (dotted black line) and BP4T (solid gray line). The strongest bands (marked as $\nu_{\mathrm{a}}$, $\nu_{\mathrm{b}}$, $\nu_{\mathrm{c}}$, and $\nu_{\mathrm{d}}$) show differences in both intensity and wavenumber.

From the present calculations, we find that the inter-ring torsion angle in the biphenyl core is around $5^{\circ}$ for the H-coverage (where the packing density and the unit cell dimensions are very similar to the molecular crystal) $^{108,109}$ and around $30^{\circ}$ in the L-coverage, where intermolecular packing forces are significantly reduced (see Figure 4); the lower packing density allows the intramolecular geometry to relax, leading to higher values of $|\omega|$. The footprint of the molecules in SAMs of BPnTs with even $n=2,4,6$ would thus naturally increase without the need to invoke a higher $|\theta|$ value, i.e., different molecular orientation. It is well-established that the vibrational spectra of oligo(p-phenylene)s are very sensitive to the inter-ring torsion angle. $^{131-138}$ In Figure 5, the calculated RAIRS spectra for BP3T and BP4T are shown and they exhibit marked differences in both intensities and frequencies of the major bands. $^{68}$ For the strongest modes below $1600 \mathrm{~cm}^{-1}$ (marked $\nu_{\mathrm{a}}, \nu_{\mathrm{b}}, \nu_{\mathrm{c}}$, and $\nu_{\mathrm{d}}$ in Figure 5), $^{68}$ the intensities change by 21,156,7, and $7 \%$, respectively, while the frequencies shift by 2,21,27, and $3 \mathrm{~cm}^{-1}$. While achieving fully quantitative agreement between first-principles calculations and experiment $^{68}$ is challenging for both frequencies and intensities, the spectra shown in Figure 5 clearly suggest the following: As a consequence of the oscillating inter-ring torsion angle $|\omega|$, pronounced odd-even effects in the RAIRS spectra of BPnT SAMs could be observed, even if the inclination of the long molecular axis to the surface normal $(|\theta|)$ were not to change across the series $n$ $=0-6$.

Interface Energetics. We now turn our attention to quantities relevant for potential applications of BPnT SAMs in molecular electronics, i.e., the work-function modification, $\Delta \Phi$, of the underlying metal substrate and the alignment, $\Delta E$, of the molecular orbitals with the substrate Fermi level, $E_{\mathrm{F}}$. The work-function modification can be decomposed into two contributions: $^{16-18,24,91,139,140}$ (i) As the BPnTs are noncentrosymmetric, they possess an intrinsic dipole moment; aligning the molecular dipoles in a two-dimensional layer leads, by virtue of the Helmholtz equation, to a step in the electrostatic potential across the layer, $\Delta V_{\text {vac }}$, which is extracted from a calculation of the isolated molecular layer (no metal present and sulfurs still saturated with hydrogen atoms). $^{91,139,140}$ (ii) The charge rearrangements occurring upon SAM adsorption (i.e., replacement of the $\mathrm{S}-\mathrm{H}$ bond with the $\mathrm{S}-\mathrm{Au}$ bonds and the push-back of the electron cloud leading out of the pristine metal surface into the vacuum $^{141-145}$ ) give rise to an additional potential step, the bond-dipole (BD). $^{91,139,140}$

$$
\Delta \Phi=\mathrm{BD}+\Delta V_{\text {vac }} \quad(1)
$$

The energy barrier, $\Delta E$, between the highest occupied molecular orbitals and $E_{\mathrm{F}}$ can be written as $^{91,139,140}$

$$
\Delta E=\Phi_{\mathrm{Au}(111)}-\mathrm{IP}_{\text {left }}+\mathrm{BD}+E_{\text {corr }}
$$

Here, $\Phi_{\mathrm{Au}(111)}$ is the work function of the clean gold substrate (calculated to be $5.2 \mathrm{eV}$ ); $\mathrm{IP}_{\text {left }}$ is the ionization potential of the molecular layer (in the absence of the metal surface) for removing an electron over the $-\mathrm{SH}$ side of the layer, i.e., the energy difference between the highest occupied $\pi$-states (HOPS) $^{140}$ of the biphenyl moiety and the vacuum level on the $-\mathrm{SH}$ side of the isolated molecular layer; and $E_{\text {corr }}$ is a corrective term accounting for the perturbation of the molecular electronic structure by the metal-molecule bond formation. $^{91,139,140}$ Note that, in this contribution, we focus on the occupied manifold of molecular states as these are (a) more easily accessible in experiments and (b) more relevant for single-molecule transport where the levels closest to $E_{\mathrm{F}}$ are dominant in resonant tunneling processes through the molecular entity; in thiol-bonded compounds, the HOPS are energetically closer to $E_{\mathrm{F}}$ than the lowest lying unoccupied states. $^{36,39,44,146-151}$

(128) Kirin, D.; Chaplot, S. L.; Mackenzie, G. A.; Pawley, G. S. Chem. Phys. Lett. 1983, 102, 105-108.

(129) Murugan, N. A.; Yashonath, S. J. Phys. Chem. B 2005, 109, 14331440.

(130) Puschnig, P.; Ambrosch-Draxl, C.; Heimel, G.; Zojer, E.; Resel, R.; Leising, G.; Kriechbaum, M.; Graupner, W. Synth. Met. 2001, 116, 327-331.

(131) Chandrasekhar, M.; Guha, S.; Graupner, W. Adv. Mater. 2001, 13, 613617.

(132) Guha, S.; Graupner, W.; Resel, R.; Chandrasekhar, M.; Chandrasekhar, H. R.; Glaser, R.; Leising, G. Synth. Met. 1999, 101, 180-181.

(133) Guha, S.; Graupner, W.; Resel, R.; Chandrasekhar, M.; Chandrasekhar, H. R.; Glaser, R.; Leising, G. Phys. Rev. Lett. 1999, 82, 3625-3628.

(134) Guha, S.; Graupner, W.; Resel, R.; Chandrasekhar, M.; Chandrasekhar, H. R.; Glaser, R.; Leising, G. J. Phys. Chem. A 2001, 105, 6203-6211.

(135) Heimel, G.; Cai, Q.; Martin, C.; Puschnig, P.; Guha, S.; Graupner, W.; Ambrosch-Draxl, C.; Chandrasekhar, M.; Leising, G. Synth. Met. 2001, 119, 371-372.

(136) Heimel, G.; Puschnig, P.; Cai, Q.; Martin, C.; Zojer, E.; Graupner, W.; Chandrasekhar, M.; Chandrasekhar, H. R.; Ambrosch-Draxl, C.; Leising, G. Synth. Met. 2001, 116, 163-166.

(137) Heimel, G.; Somitsch, D.; Knoll, P.; Bredas, J. L.; Zojer, E. J. Chem. Phys. 2005, 122, 114511.

(138) Heimel, G.; Somitsch, D.; Knoll, P.; Zojer, E. J. Chem. Phys. 2002, 116, 10921-10931.

(139) Heimel, G.; Romaner, L.; Bredas, J. L.; Zojer, E. Phys. Rev. Lett. 2006, 96, 196806.

(140) Heimel, G.; Romaner, L.; Zojer, E.; Bredas, J. L. Nano Lett. 2007, 7, 932-940.

(141) Chen, Y. C.; Cunningham, J. E.; Flynn, C. P. Phys. Rev. B 1984, 30, 7317-7319.

(142) Ishi, S.; Viswanathan, B. Thin Solid Films 1991, 201, 373-402.

(143) Lang, N. D. Phys. Rev. Lett. 1981, 46, 842-845.

(144) Lang, N. D.; Kohn, W. Phys. Rev. B 1971, 3, 1215-1223.

(145) Lang, N. D.; Norskov, J. K. Phys. Rev. B 1983, 27, 4612-4616.

(146) Kim, B.; Beebe, J. M.; Jun, Y.; Zhu, X.-Y.; Frisbie, C. D. J. Am. Chem. Soc. 2006, 128, 4970-4971.

(147) Zangmeister, C. D.; Robey, S. W.; van Zee, R. D.; Yao, Y.; Tour, J. M. J. Phys. Chem. B 2004, 108, 16187-16193.

(148) Zangmeister, C. D.; Robey, S. W.; van Zee, R. D.; Yao, Y. X.; Tour, J. M. J. Am. Chem. Soc. 2004, 126, 3420-3421.

(149) Crljen, Z.; Grigoriev, A.; Wendin, G.; Stokbro, K. Phys. Rev. B 2005, 71,165316.

![](./images/811952089566543874_10.jpg)

Figure 6. Potential energy step $\Delta V_{vac}$ across an isolated monolayer of BP$n$T molecules (no metal surface present, sulfur saturated with H-atoms) as a function of the number, $n$, of methylene spacer segments (left axis) and potential energy step BD at the gold−sulfur interface reflecting charge rearrangements upon bond formation (right axis).

Work-Function Modification. In Figure 6, we show $\Delta V_{vac}$ and BD as a function of the number of $-\mathrm{CH}_{2}-$ units, $n$, between the biphenyl core and the thiol docking group. Pronounced odd−even effects are seen for both. As the (small) molecular dipole moment is confined to the spatial region around the S−C bond, $^{91,139,140}$ the odd−even effect for $\Delta V_{vac}$ can be understood in terms of the alternating orientation, $\varphi$, of the S−C bond with respect to the surface normal and thus the projection of the dipole moment onto the latter. The odd−even effect in BD can be rationalized in terms of the alternating bonding geometry of the sulfur docking group on the Au surface. Note that the oscillating packing density alone cannot account for the odd−even effects in $\Delta V_{vac}$ and BD as they persist in similar magnitude (and ordering) when keeping the same packing density across the entire series of BP$n$Ts.

As the oscillations of BD and $\Delta V_{vac}$ are out of phase, they (almost) cancel each other and no clear trend emerges for $\Delta \Phi$. We find an average value of $\Delta \Phi=-1.35 \pm 0.10$ eV for $n=$ 1−6. In the absence of experimental data on BP$n$Ts, this value can be compared to experimental results from photoelectron emission spectroscopy (PES) on SAMs of pure alkylthiols, $^{24}$ where $\Delta \Phi \approx-1.4$ eV has been reported. $^{24}$ This comparison is justified, as both the molecular dipole moment and BD are localized in the spatial region close to the Au−S interface, $^{91,139,140,152}$ where BP$n$Ts and alkylthiols are structurally and electronically similar.

Level Alignment. In order to understand the energetic alignment of the HOPS with $E_{\mathrm{F}}$, $\mathrm{IP}_{\text {left }}$ and $E_{\text {corr }}$ need to be evaluated first; their dependence on $n$ is shown in Figure 7. Due to oscillations in the projection of the molecular dipole moment (located around the $-\mathrm{SH}$ group) onto the layer normal (odd−even effects in $\varphi$), we observe pronounced odd−even effects in $\mathrm{IP}_{\text {left }}$ (Figure 7). At the same time, $E_{\text {corr }}$ rapidly decreases upon increasing $n$ (Figure 7); this constitutes the first indication of a strongly reduced electronic coupling between metal and $\pi$-conjugated core already for $n=1$. Together, these trends lead to the final level alignment shown in Figure 8a. We observe odd−even effects up to a magnitude of 0.3 eV in the alignment of the HOPS of the biphenyl core (indicated by solid vertical lines in Figure 8a) with $E_{\mathrm{F}}$. The electronic states of the alkyl spacer develop at around 4.0 eV below $E_{\mathrm{F}}$ and are shown as the dark shaded areas in Figure 8a. As expected, their relative contributions increase with increasing $n$ and their energetic position compares favorably with experimental PES results on SAMs of pure alkylthiols, which places these states around 4.3 eV below $E_{\mathrm{F}}.^{24}$

![](./images/811952089566543874_11.jpg)

Figure 7. DFT-calculated ionization potential, $\mathrm{IP}_{\text {left }}$, on the sulfur side of a monolayer of BP$n$T molecules (no metal surface present, sulfur saturated with H-atoms) as a function of the number, $n$, of alkyl spacer segments (left axis) and energetic modification, $E_{\text {corr }}$, of the molecular ionization potential upon binding to the metal substrate as a function of $n$ (right axis). See the text for additional details.

To better understand the electronic coupling between the molecular HOPS and the metal, a zoom of the total DOS projected onto the $\pi$-conjugated core (PDOS) is shown in Figure 8b for $n=0,1$, and 2. To be able to compare the electronic structure of the SAM on the metal (shaded areas) to that of the free-standing molecular layer (dark-gray lines; no metal present and sulfur saturated with hydrogen), the origin of the energy scale in Figure 8b is set to the vacuum level above the SAM on the biphenyl side, $V_{\text {vac }}^{\text {right }} \cdot{ }^{91,139,140}$ For BP0T, the electronic structure is heavily perturbed upon bonding of the SAM to the metal. This is manifested in a significant broadening of the PDOS upon adsorption and an energetic shift, consistent with the relatively high value $(\sim 0.2 \mathrm{eV})$ for $E_{\text {corr }}$ (Figure 7). Just a single $-\mathrm{CH}_{2}-$ spacer largely decouples the electronic subsystems of the $\pi$-conjugated core and the metal. For $n=2$, the PDOS of the free-standing molecular layer is virtually identical to that of the SAM on the metal; no additional broadening and no shift in energy are observed, consistent with the vanishing $E_{\text {corr }}$ for $n \geq$ 1 (Figure 7).

It is important to note that, in the absence of the alkyl spacer $(n=0)$, the sulfur $\mathrm{p}_{z}$-orbitals are incorporated into the HOPS; i.e., the $\pi$-electron system is delocalized over the core and the sulfur. $^{91}$ This is illustrated in the bottom plot in Figure 8c, where we show again the PDOS for $n=0,1$, and 2 together with the contribution of the sulfur states to the total DOS. As the aromatic $\pi$-system and the sulfur $\mathrm{p}_{z}$-orbitals are part of one and the same molecular orbital in the isolated BP0T molecule, their respective contributions must appear in the same energy range in the DOS of BP0T on Au(111). Upon inserting one or more alkyl spacer units, the sulfur orbitals are electronically decoupled from the HOPS (center and upper panel in Figure 8c). Starting with BP1T, the sulfur states and the HOPS appear at different binding energies $(\sim 1.1 \mathrm{eV}$ below $E_{\mathrm{F}}$ compared to $\sim 1.5 \mathrm{eV}$ ). The energetic position of the sulfur states now is dictated only by the sulfur−gold bonding. Such gold−sulfur states have, in fact, been experimentally observed for SAMs of pure alkylthiols at around 1.4 eV below $E_{\mathrm{F}},{ }^{24,153}$ in good agreement with our calculations.

Character of the Electronic States. While the case of BP0T can be seen as a metal−semiconductor junction, $^{91,139,140}$ the

(150) Sikes, H. D.; Sun, Y.; Dudek, S. P.; Chidsey, C. E. D.; Pianetta, P. J. Phys. Chem. B 2003, 107, 1170−1173.

(151) Xue, Y. Q.; Ratner, M. A. Phys. Rev. B 2003, 68, 115406.

(152) De Renzi, V.; Rousseau, R.; Marchetto, D.; Biagi, R.; Scandolo, S.; del Pennino, U. Phys. Rev. Lett. 2005, 95, 046804.

(153) Kera, S.; Setoyama, H.; Kimura, K.; Iwasaki, A.; Okudaira, K. K.; Harada, Y.; Ueno, N. Surf. Sci. 2001, 482, 1192−1198.

![](./images/811952089566543874_12.jpg)

Figure 8. (a) Density of states projected onto the $\pi$-conjugated biphenyl core (PDOS) as a function of the number, $n$, of methylene linker units. The gray areas represent the PDOS broadened with a fwhm = 0.2 eV Gaussian. Comparison with the unbroadened PDOS (white areas) shows that the peak widths are not an artifact of this broadening. The dark gray area represents the PDOS of the alkyl spacer segments evolving around 4 eV below the Fermi energy ($E_{\text{F}}$). The solid vertical lines highlight the odd$-$even effects in the energetic position of the highest occupied molecular $\pi$-states. In panel b, the PDOS of the SAM (gray areas) is compared to that of the corresponding isolated molecular layer, where no metal surface is present and each sulfur is saturated with an H-atom (dark-gray lines); the origin of the energy scale is the vacuum level above the biphenyl side of the SAM. (c) PDOS of the sulfur (black area) and the $\pi$-conjugated core (gray area) for $n = 0-2$; the vertical dotted lines indicate the respective peak positions.

![](./images/811952089566543874_13.jpg)

Figure 9. Schematic energy level diagram for the BP6T SAM. Also shown are the plane-averaged charge densities arising from the electronic states around $E_{\text{F}}$ (top), the highest occupied molecular $\pi$-states (center), and the $\sigma$-states on the alkyl segment (bottom). In the right panels, isosurface plots of the respective electron-density distributions are shown in a 3D representation.

situation for long alkyl spacers, is reminiscent of a metal$-$insulator$-$semiconductor junction, where the metal is separated from the $\pi$-core (semiconductor) by a larger band gap insulator (alkyl spacer). This becomes evident in Figure 9, where a schematic energy level diagram is shown for BP6T as a representative for the series of the BP$n$Ts. The horizontal lines indicate the energetic position of the most relevant electronic states in the SAM ($\sigma$-states on the alkyl segment and HOPS) and the Fermi level. Plane-averaged electron wave functions (squared) in a $\pm 0.1$ eV energetic window around $E_{\text{F}}$, the HOPS ($\sim 1.5$ eV below $E_{\text{F}}$), and the alkyl states at $\sim 4.0$ eV below $E_{\text{F}}$ are also shown. To better understand the nature of these electronic states, the corresponding 3D representations are displayed in the right panel of Figure 9. Around $E_{\text{F}}$, we find electron density only on the metal; in the molecular region, the electron density rapidly decays with increasing distance from the metal surface, thus showing effective contributions only on the sulfur atoms (see also PDOS in Figure 8c);$^{91,154}$ the gold$-$sulfur states around 1.1 eV below $E_{\text{F}}$ (see Figure 8c) for $n > 0$ look identical. In the energetic region of the HOPS, electron density is found on both metal (rapidly decaying on the alkyl segment) and $\pi$-core; on the latter, the characteristic shape of the HOMO wave function of biphenyl can be recognized.$^{91,137}$ No density is present on the alkyl spacer, visually confirming the decoupling of the electronic subsystems of metal and conjugated segment and, furthermore, suggesting the appearance of an effective barrier for electron (or hole) transfer between metal and $\pi$-conjugated core. Only at $\sim 4.0$ eV below $E_{\text{F}}$ do we find continuous electron density on all parts of the system (see Figure 1): metal, sulfur, alkyl spacer ($\sigma$-states), and biphenyl moiety (also $\sigma$-states).

### Conclusion

On the basis of density-functional theory calculations, we have investigated the structural and electronic properties of SAMs of $\omega$-(biphenyl-4-yl)alkanethiols with $n = 0-6$ methylene spacer units on Au(111). We have discussed experimental findings, in particular XPS core-level shifts and RAIRS spectra, in the light of our computational results. In agreement with previously published experimental studies, we find the competition between the preferential hybridization of the sulfur docking group at the S$-$Au interface and the intermolecular interactions between the conjugated segments to be the driving force for odd$-$even effects in the structure and packing of these SAMs. In contrast to prior findings, however, we find no evidence for odd$-$even effects in the inclination of the long molecular axes to the surface normal. We therefore suggest that an additional structural parameter, the torsion angle between the two phenyl rings in the biphenyl moiety, might lead to the experimentally observed odd$-$even effects in RAIRS.

(154) Sun, Q.; Selloni, A.; Scoles, G. *J. Phys. Chem. B* **2006**, 110, 3493$-$3498.

Focusing on the interface energetics relevant for the application of these SAMs in organic electronic devices, we find pronounced odd−even effects in the energetic alignment of the highest occupied molecular orbitals of the $\pi$-conjugated biphenyl core with the metal Fermi level. The work function of the gold substrate, on the other hand, is significantly reduced but does not exhibit clear odd−even effects. The insertion of alkyl spacers between the metal−sulfur interface and the $\pi$-core leads to a decoupling of the electronic states of the two respective subsystems and the formation of a (tunnel) barrier between them, which is reminiscent of conventional metal−insulator−semiconductor junctions.

Acknowledgment. This work has been conducted under the INSANE project (Marie-Curie OIF contract no. 021511). The financial support of the Austrian Science Foundation (FWF) through the Austrian Nano Initiative (Project N-702-SENSPHYS) and of the European Commission through the project "IControl" (EC-STREP-033197) is gratefully acknowledged. The work at Georgia Tech has been partly supported by the Office of Naval Research and the National Science Foundation (under the CRIF program, award CHE-0443564). The authors wish to thank D. Käfer for helpful discussions.

LA7023814