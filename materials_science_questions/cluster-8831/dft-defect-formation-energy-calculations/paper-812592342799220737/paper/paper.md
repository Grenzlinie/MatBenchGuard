# Influence of point defects on the electronic and topological properties of monolayer WTe₂
Lukas Muechler, $^{1, *}$ Wei Hu, $^{2,3}$ Lin Lin, $^{4,3}$ Chao Yang, $^{3}$ and Roberto Car $^{5}$

$^{1}$Center for Computational Quantum Physics, The Flatiron Institute, New York, New York 10010, USA
$^{2}$Hefei National Laboratory for Physical Sciences at Microscale, University of Science and Technology of China, Hefei, Anhui 230026, China
$^{3}$Computational Research Division, Lawrence Berkeley National Laboratory, Berkeley, California 94720, USA
$^{4}$Department of Mathematics, University of California, Berkeley, California 94720, USA
$^{5}$Department of Chemistry, Princeton University, Princeton, New Jersey 08544, USA

![](./images/812592342799220737_1.jpg)
(Received 5 January 2020; accepted 16 June 2020; published 6 July 2020)

In some topological insulators such as monolayers of WTe₂ or graphene with spin-orbit coupling, band inversion originates from chemical bonding and space group symmetry, in contrast to materials such as Bi₂Se₃, where the band inversion derives from relativistic effects in the atoms. In the former, band inversion is susceptible to changes of the chemical environment, e.g., by defects, while the latter are less affected by defects due to the larger energy scale associated with atomic relativistic effects. Motivated by recent experiments, we study the effect of Te vacancies and Te adatoms on the electronic properties of WTe₂. We find that the Te vacancies have a formation energy of 2.21 eV, while the formation energy of the Te adatoms is much lower with 0.72 eV. The vacancies strongly influence the band structure and we present evidence that band inversion is already reversed at the nominal composition of WTe₁.₉₇. In contrast, we show that the adatoms do not change the electronic structure in the vicinity of the Fermi level and thus the topological properties.

DOI: 10.1103/PhysRevB.102.041103

## I. INTRODUCTION
The advent of topological band theory led to the discovery of a plethora of new topological phases in three-dimensional (3D) materials, facilitated by the extensive databases available from experiment [1–5]. In contrast, stable two-dimensional (2D) topological materials are still largely unexplored as the available databases are comparatively much smaller. In recent years, monolayers of transition metal dichalcogenides (TMDs) have attracted significant interest due to their di- verse electronic and optical properties that can be used in technological applications [6–10]. For example, group VI dichalcogenides of the general formula $MX_{2}$, such as WTe₂ and MoTe₂, have been theoretically predicted to be 2D topological insulators (TIs) as monolayers, while they have been predicted to be type-II Weyl semimetals in the bulk [11–17]. Shortly after the theoretical prediction, many groups have reported the fabrication of thin films of WTe₂ [18–22] and found experimental evidence for topologically protected edge states in monolayer devices [23–27]. Monolayers of WTe₂ are ideal model materials to study 2D topological phases due to their large band gap. In addition, the interplay of spin-orbit coupling (SOC), low crystal symmetry, and high electron mobilities gives rise to other phenomena of interest such as large spin-orbit torques that could be used in spintronic devices [28–31].

Defects are important tools to study the interplay of topology and electronic structure. For example, higher-dimensional defects such as dislocations host topological bound states that can be used to classify and characterize the bulk topology [32–34]. General topological arguments suggest that a TI should not be affected by defects and disorder as long as the inversion between valence and conduction bands is maintained and a bulk band gap exists, while time-reversal symmetry (TRS) is preserved on average [35]. This statement is expected to hold for TIs in which the band inversion is due to *atomic* relativistic effects, which are only weakly dependent on the crystal structure and the chemical environment, as is the case with HgTe, Bi₂Se₃, and KHgSb [36–40]. In contrast, there is another class of TIs in which the band inversion depends on the chemical bonding and crystal symmetry, which we will call *preinverted* TIs [12,41]. Material examples are graphene, monolayers of Bi and monolayers of WTe₂, SrZnSb₂, LaSbTe, and LiCaBi [1–3,42,43]. In these materials, defects disrupting the chemical bonding are expected to have a strong effect on the topological properties of the material, as they can potentially reverse the band inversion at already low concentrations. This distinction is more precise in the language of elementary band representations (EBRs) introduced by Bradlyn *et al.* [1]: A set of energy bands $\{\varepsilon(\boldsymbol{k})\}$ is an EBR if it derives from a given collection of localized Wannier functions and cannot be decomposed into a set of other band representations. For example, the set of bands making up the Dirac cone in graphene represents an EBR induced by the carbon $p_{z}$ orbitals. A disconnected set of bands, i.e., a set of bands that is separated from other bands by a gap, is topological, if it cannot be derived from an EBR, i.e., a set of localized Wannier functions. In “preinverted” TIs such as WTe₂, the valence and conduction bands form a connected EBR that decomposes into a disconnected one once SOC, even infinitesimal, is considered [Fig. 1(a)]. While the sum of both valence and conduction bands is an EBR, neither the valence band nor the conduction band alone are an EBR. Therefore,

*lmuechler@flatironinstitute.org


![](./images/812592342799220737_2.jpg)

FIG. 1. (a) Schematic band structure of a preinverted TI such as WTe₂. Without SOC, the material is a topological semimetal with a Dirac crossing, i.e., the band structure forms a connected EBR. Upon inclusion of SOC, the Dirac cone gaps and the bands split into two disconnected sets. All four bands form a disconnected EBR, while none of the pairs alone does. If only one of the disconnected sets is occupied, the material is a TI. (b) Schematic band structure of an atomic TI, such as HgTe or Bi₂Se₃, that derives from a band inversion between two different EBRs. When scalar relativistic effects such as the Darwin term are above a threshold, two EBRs can overlap and the band structure is metallic, forming a composite EBR. Including SOC, the band crossings gap out and an insulator is formed. All four bands still form a composite EBR, while none of the pairs is an EBR. The band structure is topological if only one set of bands is occupied.

if only the lower set of bands is occupied, the system has to be a TI.

In contrast, "atomic TIs" are gapped without SOC, as the valence and conduction bands form a composite band representation [Fig. 1(b)] [44]. In these compounds, scalar relativistic effects such as the Darwin term are strong and EBRs invert to form a composite, metallic EBR. Once SOC is considered, a gap opens while the EBR remains composite. However, the disconnected components are topological [37].

In preinverted TIs such as WTe₂, changes of the local bonding due to defects can reverse the band inversion and drive the material into a topological trivial state. The energy scale associated with this transition is expected to be small compared to the energy scale of atomic relativistic effects. For example, in the simplest model of a preinverted TI, the Kane-Mele model, the energy scale of the phase transition to a topologically trivial insulator is of the order of the next-nearest-neighbor hopping term [35]. For this particular class of materials it is essential to understand the influence of defects on the bulk electronic structure [22,45,46].

Here, we study the effect of Te vacancies and Te adatoms on the topological and electronic properties of monolayer WTe₂. Recent experiments have shown that Te vacancies have drastic effects on the properties of thin WTe₂ films, such as a much lower mobility and increased scattering rates [47], while recent calculations have highlighted the importance of edge disorder and termination on the edge states [13,48]. We find that Te vacancies could drive the system into a trivial state, while the effect of Te adatoms can be considered as a weak perturbation to the 2D TI state. In contrast, a recent scanning tunneling microscopy (STM) study of the step edges of bulk WTe₂ showed the existence of topological edges states on the step edges of WTe₂, despite the presence of unidentified defects [49]. We therefore propose that these defects are Te adatoms which possess a low defect formation energy of 0.72 eV in Te-rich conditions. These findings are supported by the fact that monolayers of WTe₂ are usually obtained from bulk crystals of WTe₂ grown in a Te-rich environment [26,50].

![](./images/812592342799220737_3.jpg)

FIG. 2. (a) Top and side view of a WTe₂ monolayer in the 1T′ structure and Brillouin zone with high-symmetry points. (b) Band structure of WTe₂ monolayers with and without SOC. (c) Orbital contributions to the band structure of WTe₂ around the Fermi energy.

## II. MONOLAYER WTe₂

TMDs with heavy elements such as WTe₂ occur in distorted 1T structures. This distortion can be attributed to relativistic effects that determine the relative level alignment of the p and d orbitals [51]. In the case of WTe₂, the structure distorts from the 1T to the orthorhombic 1T′ structure in which the W atoms form linear chains [Fig. 2(a)]. In the absence of SOC, a monolayer of WTe₂ in the 1T′ structure is a topological Dirac semimetal with two Dirac crossings along XΓX, protected by a glide symmetry along the W-chain direction, i.e., the band structure is already inverted. Upon inclusion of SOC, the Dirac cones gap and the system becomes a 2D TI [Fig. 2(b)] [11–13]. In contrast to other TMDs such as MoS₂, where the band gap is between filled M-d orbitals and unoccupied X-p orbitals, the W-d states are strongly hybridized with the Te-p states around the Fermi energy ($E_F$) in WTe₂, due to the small difference in electronegativity between W and Te [Fig. 2(c)] [52].

## III. EFFECT ON THE ELECTRONIC STRUCTURE

We now discuss the influence of two experimentally relevant Te defects, namely Te adatoms and Te vacancies, on the electronic structure and topological properties of WTe₂. These defects have been chosen since they are relevant for ongoing experimental work, e.g., Te vacancies have been shown to influence the transport properties of thin WTe₂ films

![](./images/812592342799220737_4.jpg)

FIG. 3. Band structure of a $5\times 3$ supercell (no SOC) with (a) no defect. (b) Te vacancy. The sizes of the circles indicate the contribution of the W atoms next to the vacancy. (c) Te adatom. The sizes of the circles indicate the contribution of the adatom states to the band structure. Green circles represent $p_z$, blue, and red $p_y$ states. The labels $B1$ and $B2$ are referred to in the text.

significantly [47]. To understand the influence of these defects on the band inversion, we calculated the band structures without SOC for a fully relaxed $5\times 3$ supercell of (i) pristine WTe$_2$, (ii) a Te vacancy with a formation energy of $E(V) = 2.21$ eV, and (iii) a Te adatom with a formation energy of $E(A) = 0.72$ eV [53]. The calculations are based on the SIESTA package in conjunction with the PEXSI (pole expansion and selected inversion) algorithm and VASP in the framework of the generalized gradient approximation (GGA) [54–62]. These vacancy formation energies are within $\sim$0.2 eV of recent calculations of defect formation energies in monolayers of TMDs such as MoS$_2$ crystallizing in the $1$-$H$ structure, which similarly possess strong covalent bonds between transition metal atoms and chalcogenides [63,64] and general agreement with previously reported values in WTe$_2$ [65]. The formation energy of adatoms on WTe$_2$ is lower by about 0.3 eV compared to MoS$_2$ and its relatives. This difference could be explained by the different structures of these TMDs, as MoS$_2$ crystallizes in the $1$-$H$ structure. Due to the distorted $1T'$ structure, the Te layer in WTe$_2$ is stretched with respect to the $1$-$H$ structure, leading to a larger adsorption site and lower adsorption energy for adatoms.

We now turn towards the effect of the defects on the electronic structure. In the pristine supercell, band backfolding leads to the appearance of two Dirac crossings along $\Gamma$X close to $E_F$, while a large gap separates valence and conduction bands in the rest of the Brillouin zone [Fig. 3(a)]. By removing a Te atom, the band structure changes dramatically [Fig. 3(b)]. The Dirac crossings disappear and a gap is opened along the $\Gamma$X line with almost flat bands close to $E_F$. By plotting the atomic weights of the W atoms surrounding the vacancy, we see a large contribution of these atoms to the flat bands close to $E_F$, indicating a localized set of states that does not disperse. This suggests that the W-$d$ states around the vacancies form nonbonding dangling bond states, consistent with the large formation energy of this defect. The formation of a vacancy disrupts the network of strong covalent, almost metallic bonds. Since the Dirac crossings stem from both W-$d$ and Te-$p$ states, a vacancy cannot considered to be a weak perturbation, as it significantly and qualitatively alters the electronic structure close to $E_F$.

In contrast, the electronic structure of WTe$_2$ with a Te adatom is changed only slightly close to $E_F$ [Fig. 3(c)]. The interaction of the adatom with the layer leads to a splitting of the atomically degenerate $p$ orbitals. Due to the 2D nature of the monolayer, the in-plane $p_x$ and $p_y$ orbitals of the adatom interact differently with the monolayer and are lower in energy with respect to the out-of-plane $p_z$ orbital. A neutral Te atom possesses four $p$ electrons and we therefore expect the two $p_x$ and $p_y$ adatom states to be occupied and the $p_z$ states to be unoccupied. This is reflected in the atomic weights of the adatom states in Fig. 3(c), where the $p_x$, $p_y$ states are clearly separated from the unoccupied $p_z$ states by over 1.5 eV. Due to the large splitting between the in- and out-of-plane orbitals, the adatom states do not contribute to the states close to $E_F$ and the band crossing remains largely unaffected. The main effect of the adatom is the breaking of the translational symmetries $\{E|\frac{1}{5}00\}$ and $\{E|0\frac{1}{3}0\}$, which are the trivial translational symmetries obtained by creating a $5\times 3$ supercell. These symmetries lead to nonsymmorphic degeneracies at high-symmetry points due to the backfolding of the bands in the supercell. Breaking of this symmetry slightly gaps the degeneracies induced by the band folding, but does not significantly change the band crossings close to $E_F$. The bands contributing to the Dirac cone in WTe$_2$ stem from strong in-plane bonds. An adatom that perturbs the bonding perpendicular to the plane can therefore be treated as a weak perturbation to the band structure, in contrast to the Te vacancy, which strongly disrupts the in-plane bonding and the states close to $E_F$.

We confirm these conclusions by calculating the spectral functions of the supercells, which have been backfolded into the primitive Brillouin zone (BZ) along the $\Gamma$-$X$ direction using the BANDUP code [66,67]. The spectral function is given by $\mathcal{A}(\boldsymbol{k},\omega) = \sum_n P_{n\boldsymbol{K}}(\boldsymbol{k})\delta[\omega - \varepsilon_n(\boldsymbol{k})]$, where the spectral weight $P_{n\boldsymbol{K}}(\boldsymbol{k}) = \sum_m |\langle m\boldsymbol{K}|n\boldsymbol{k}\rangle|^2$ is defined via the overlap of a state $|m\boldsymbol{K}\rangle$ of the supercell with the state $|n\boldsymbol{k}\rangle$ at energy $\varepsilon_n(\boldsymbol{k})$ of the primitive cell; the $\boldsymbol{k}$ vectors $\boldsymbol{K}$ of the supercell are related to the $\boldsymbol{k}$ vectors $\boldsymbol{k}$ of the primitive cell by a unique folding vector $\boldsymbol{G}$ via $\boldsymbol{K} = \boldsymbol{k} - \boldsymbol{G}$. The backfolding of the spectral function of the pristine supercell [Fig. 4(a)] into the primitive BZ reproduces the well-known band structure of WTe$_2$. A Te vacancy strongly perturbs the band structure and leads to a suppression of spectral weight for a large range of energies [Fig. 4(b)]. The band crossings are absent, indicating that the Te vacancy drives the system into a topologically trivial state that is not perturbatively connected to the pristine band structure. In the case of the Te adatom [Fig. 4(c)], the spectral function close to the Fermi level changes slightly relative to the pristine material due to a small band splitting that generates a pocket near the $\Gamma$ point. However, the Dirac crossing is left unperturbed and the system should be a 2D TI upon inclusion of SOC. The band splitting is due to the symmetry breaking induced by the adatom. We have highlighted two supercell bands denoted by $B1$ and $B2$ in Figs. 3(a) and 3(c), which fold into the less dispersive band of the Dirac cone in the primitive BZ. Without an adatom, these two bands are degenerate at $X$ and $\Gamma$ and therefore fold back into the same band. In the presence of the adatom, the degeneracies are lifted

![](./images/812592342799220737_5.jpg)

FIG. 4. Spectral function of the (a) pristine $5 \times 3$ supercell, (b) $5 \times 3$ vacancy supercell, and (c) $5 \times 3$ adatom supercell folded back to the primitive unit cell. The effect of SOC on the states close to the Fermi level are shown in the insets for a window of $\pm 0.25$ eV around the $E_F$. Spectral functions of a ribbon constructed from $N = 15$ supercells $(4 \times 2)$ with Te adatoms projected on (d) the bulk states and (e) on an edge with a Te termination, calculated from a Wannier interpolation with SOC.

and the bands do not fold back into one unique band in the supercell, leading to a splitting of spectral weight between the two now inequivalent bands. Upon consideration of SOC [Fig. 4(d)], we find that the Dirac cone gaps. The states close to $E_F$ remain broadened due to the symmetry breaking effect of the adatom discussed above. A spectral gap between the valence and conduction band remains in which we expect topological edge states to appear.

## IV. TOPOLOGICAL PROPERTIES

A monolayer of WTe$_2$ without SOC possesses an inverted band structure with two Dirac cones along $X\Gamma X$, which guarantees the 2D TI phase upon inclusion of SOC due to the presence of the in-plane glide symmetry [12]. Point defects destroy the glide symmetry and a gap opening via SOC does not guarantee a 2D TI state in the presence of defects. Perturbative changes to the band structure without SOC, that leave band inversions and Dirac cones intact, are not expected to change the topological invariant of WTe$_2$. To confirm this hypothesis, we calculated the edge spectral function of a ribbon periodic in the $\hat{x}$ direction, constructed from $N = 15$ supercells $(4 \times 2)$ with one Te adatom per supercell. The spectral function has been calculated from a tight-binding model that we obtained from a Wannier interpo- lation of the density functional theory (DFT) band structure with SOC [68]. Figure 4(d) shows the bulk projection of the spectral function which displays a well-defined bulk band gap. As expected, a surface state connecting valence and con- duction bands can be observed clearly in Fig. 4(e), proving that the adatoms do not change the topological nature of the slab. Strong perturbations that gap the Dirac cones, on the other hand, may lead to a transition to a topologically trivial state. Our calculation shows that a vacancy concentra- tion of about 1% could already be sufficient to destroy the topological state.

It is expected that the adatom defects will not serve as strong scattering centers, since they leave the states close to $E_F$ almost unchanged. Vacancies, on the other hand, are ex- pected to scatter the conduction electrons strongly. Our find- ings suggest that a systematic study of electron mobilities as a function of adatom and vacancy defect concentration could be of great interest in this material, which can be induced by changing the growth conditions or ion bombardment [47].

## ACKNOWLEDGMENTS

We acknowledge fruitful discussions with B. Bradlyn, Z. J. Wang, and C. Dreyer. R.C. was supported by DOE Grant No. DE-SC0017865. This material is based upon work supported by the US Department of Energy, Office of Science, Office of Advanced Scientific Computing Research and Office of Basic Energy Science, Scientific Discovery through Ad- vanced Computing (SciDAC) program. The Flatiron Institute is a division of the Simons Foundation.

[1] B. Bradlyn, L. Elcoro, J. Cano, M. G. Vergniory, Z. Wang, C. Felser, M. I. Aroyo, and B. A. Bernevig, *Nature* (London) **547**, 298 (2017).

[2] T. Zhang, Y. Jiang, Z. Song, H. Huang, Y. He, Z. Fang, H. Weng, and C. Fang, *Nature* (London) **566**, 475 (2019).

[3] M. Vergniory, L. Elcoro, C. Felser, N. Regnault, B. A. Bernevig, and Z. Wang, *Nature* (London) **566**, 480 (2019).

[4] H. Po, A. Vishwanath, and H. Watanabe, *Nat. Commun.* **8**, 50 (2017).

[5] J. Kruthoff, J. de Boer, J. van Wezel, C. L. Kane, and R.-J. Slager, *Phys. Rev. X* **7**, 041069 (2017).

[6] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, *Nat. Nanotechnol.* **7**, 699 (2012).

[7] S. Manzeli, D. Ovchinnikov, D. Pasquier, O. V. Yazyev, and A. Kis, *Nat. Rev. Mater.* **2**, 17033 (2017).

[8] X. Xu, W. Yao, D. Xiao, and T. F. Heinz, *Nat. Phys.* **10**, 343 (2014).

[9] A. Autere, H. Jussila, Y. Dai, Y. Wang, H. Lipsanen, and Z. Sun, *Adv. Mater.* **30**, 1705963 (2018).

[10] M. Gibertini, M. Koperski, A. Morpurgo, and K. Novoselov, *Nat. Nanotechnol.* **14**, 408 (2019).

[11] X. Qian, J. Liu, L. Fu, and J. Li, *Science* **346**, 1344 (2014).

[12] L. Muechler, A. Alexandradinata, T. Neupert, and R. Car, *Phys. Rev. X* **6**, 041069 (2016).

[13] S. Ok, L. Muechler, D. Di Sante, G. Sangiovanni, R. Thomale, and T. Neupert, *Phys. Rev. B* **99**, 121105(R) (2019).

[14] A. A. Soluyanov, D. Gresch, Z. Wang, Q. Wu, M. Troyer, X. Dai, and B. A. Bernevig, *Nature* (London) **527**, 495 (2015).

[15] Y. Sun, S. C. Wu, M. N. Ali, C. Felser, and B. Yan, *Phys. Rev. B* **92**, 161107(R) (2015).

[16] K. Deng, G. Wan, P. Deng, K. Zhang, S. Ding, E. Wang, M. Yan, H. Huang, H. Zhang, Z. Xu *et al.*, *Nat. Phys.* **12**, 1105 (2016).

[17] F. Y. Bruno, A. Tamai, Q. S. Wu, I. Cucchi, C. Barreteau, A. de la Torre, S. McKeown Walker, S. Riccò, Z. Wang, T. K. Kim, M. Hoesch, M. Shi, N. C. Plumb, E. Giannini, A. A. Soluyanov, and F. Baumberger, *Phys. Rev. B* **94**, 121112(R) (2016).

[18] J. Zhou, F. Liu, J. Lin, X. Huang, J. Xia, B. Zhang, Q. Zeng, H. Wang, C. Zhu, L. Niu, X. Wang, W. Fu, P. Yu, T. Chang, C. Hsu, D. Wu, H. Jeng, Y. Huang, H. Lin, Z. Shen, C. Yang, L. Lu, K. Suenaga, W. Zhou, S. Pantelides, G. Liu, and Z. Liu, *Adv. Mater.* **29**, 1603471 (2016).

[19] Y. Zhou, H. Jang, J. Woods, Y. Xie, P. Kumaravadivel, G. Pan, J. Liu, Y. Liu, D. Cahill, and J. Cha, *Adv. Funct. Mater.* **27**, 1605928 (2017).

[20] K. Chen, Z. Chen, X. Wan, Z. Zheng, F. Xie, W. Chen, X. Gui, H. Chen, W. Xie, and J. Xu, *Adv. Mater.* **29**, 1700704 (2017).

[21] J. Na, A. Hoyer, L. Schoop, D. Weber, B. Lotsch, M. Burghard, and K. Kern, *Nanoscale* **8**, 18703 (2016).

[22] V. Fatemi, Q. D. Gibson, K. Watanabe, T. Taniguchi, R. J. Cava, and P. Jarillo-Herrero, *Phys. Rev. B* **95**, 041410(R) (2017).

[23] S. Tang, C. Zhang, D. Wong, Z. Pedramrazi, H. Tsai, C. Jia, B. Moritz, M. Claassen, H. Ryu, S. Kahn, J. Jiang, H. Yan, M. Hashimoto, D. Lu, R. Moore, C. Hwang, C. Hwang, Z. Hussain, Y. Chen, M. Ugeda *et al.*, *Nat. Phys.* **13**, 683 (2017).

[24] Z. Fei, T. Palomaki, S. Wu, W. Zhao, X. Cai, B. Sun, P. Nguyen, J. Finney, X. Xu, and D. Cobden, *Nat. Phys.* **13**, 677 (2017).

[25] Z.-Y. Jia, Y.-H. Song, X.-B. Li, K. Ran, P. Lu, H.-J. Zheng, X.-Y. Zhu, Z.-Q. Shi, J. Sun, J. Wen, D. Xing, and S.-C. Li, *Phys. Rev. B* **96**, 041108(R) (2017).

[26] S. Wu, V. Fatemi, Q. D. Gibson, K. Watanabe, T. Taniguchi, R. J. Cava, and P. Jarillo-Herrero, *Science* **359**, 76 (2018).

[27] Y. Shi, J. Kahn, B. Niu, Z. Fei, B. Sun, X. Cai, B. A. Francisco, D. Wu, Z.-X. Shen, X. Xu *et al.*, *Sci. Adv.* **5**, eaat8799 (2019).

[28] D. MacNeill, G. M. Stiehl, M. H. D. Guimaraes, R. A. Buhrman, J. Park, and D. C. Ralph, *Nat. Phys.* **13**, 300 (2016).

[29] D. MacNeill, G. M. Stiehl, M. H. D. Guimarães, N. D. Reynolds, R. A. Buhrman, and D. C. Ralph, *Phys. Rev. B* **96**, 054450 (2017).

[30] S.-Y. Xu, Q. Ma, H. Shen, V. Fatemi, S. Wu, T.-R. Chang, G. Chang, A. M. M. Valdivia, C.-K. Chan, Q. D. Gibson *et al.*, *Nat. Phys.* **14**, 900 (2018).

[31] A. Kononov, G. Abulizi, K. Qu, J. Yan, D. Mandrus, K. Watanabe, T. Taniguchi, and C. Schönenberger, *Nano Lett.* **20**, 4228 (2020).

[32] Y. Ran, Y. Zhang, and A. Vishwanath, *Nat. Phys.* **5**, 298 (2009).

[33] R.-J. Slager, L. Rademaker, J. Zaanen, and L. Balents, *Phys. Rev. B* **92**, 085126 (2015).

[34] R. Queiroz, I. C. Fulga, N. Avraham, H. Beidenkopf, and J. Cano, *Phys. Rev. Lett.* **123**, 266802 (2019).

[35] S. Rachel, J. Phys.: Condens. Matter **28**, 405502 (2016).

[36] S. Chadov, J. Kiss, J. Kübler, and C. Felser, *Phys. Status Solidi RRL* **7**, 82 (2013).

[37] Z. Zhu, Y. Cheng, and U. Schwingenschlögl, *Phys. Rev. B* **85**, 235401 (2012).

[38] L. Muechler, H. Zhang, S. Chadov, B. Yan, F. Casper, J. Kübler, S.-C. Zhang, and C. Felser, *Angew. Chem., Int. Ed.* **51**, 7221 (2012).

[39] H. Zhang, C.-X. Liu, X.-L. Qi, X. Dai, Z. Fang, and S.-C. Zhang, *Nat. Phys.* **5**, 438 (2009).

[40] Z. Wang, A. Alexandradinata, R. J. Cava, and B. A. Bernevig, *Nature* (London) **532**, 189 (2016).

[41] Q. D. Gibson, L. M. Schoop, L. Muechler, L. S. Xie, M. Hirschberger, N. P. Ong, R. Car, and R. J. Cava, *Phys. Rev. B* **91**, 205128 (2015).

[42] C. L. Kane and E. J. Mele, *Phys. Rev. Lett.* **95**, 226801 (2005).

[43] F. Reis, G. Li, L. Dudy, M. Bauernfeind, S. Glass, W. Hanke, R. Thomale, J. Schäfer, and R. Claessen, *Science* **357**, 287 (2017).

[44] L. M. Schoop, F. Pielnhofer, and B. V. Lotsch, *Chem. Mater.* **30**, 3155 (2018).

[45] W. L. Liu, M. L. Chen, X. X. Li, S. Dubey, T. Xiong, Z. M. Dai, J. Yin, W. L. Guo, J. L. Ma, Y. N. Chen, J. Tan, D. Li, Z. H. Wang, W. Li, V. Bouchiat, D. M. Sun, Z. Han, and Z. D. Zhang, *2D Mater.* **4**, 011011 (2017).

[46] C. Naylor, W. Parkin, Z. Gao, H. Kang, M. Noyan, R. B. Wexler, L. Z. Tan, Y. Kim, C. E. Kehayias, F. Streller, Y. Zhou, R. Carpick, Z. Luo, Y. Park, A. M. Rappe, M. Drndić, J. M. Kikkawa, and A. T. C. Johnson, *2D Mater.* **4**, 021008 (2017).

[47] M. Gao, M. Zhang, W. Niu, Y. Chen, M. Gu, H. Wang, F. Song, P. Wang, S. Yan, F. Wang, X. Wang, X. Wang, Y. Xu, and R. Zhang, *Appl. Phys. Lett.* **111**, 031906 (2017).

[48] A. Lau, R. Ray, D. Varjas, and A. R. Akhmerov, *Phys. Rev. Mater.* **3**, 054206 (2019).

[49] L. Peng, Y. Yuan, G. Li, X. Yang, J. J. Xian, C. J. Yi, Y. G. Shi, and Y. S. Fu, *Nat. Commun.* **8**, 659 (2017).

[50] M. N. Ali, L. Schoop, J. Xiong, S. Flynn, Q. Gibson, M. Hirschberger, N. Ong, and R. Cava, *Europhys. Lett.* **110**, 67002 (2015).

[51] M. Kertesz and R. Hoffmann, *J. Am. Chem. Soc.* **106**, 3453 (1984).

[52] D.-H. Choe, H.-J. Sung, and K. J. Chang, *Phys. Rev. B* **93**, 125109 (2016).

[53] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.102.041103 for additional details of the calculations.

[54] J. M. Soler, E. Artacho, J. D. Gale, A. García, J. Junquera, P. Ordejón, and D. Sánchez-Portal, J. Phys.: Condens. Matter 14, 2745 (2002).

[55] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[56] T. Auckenthaler, V. Blum, H.-J. Bungartz, T. Huckle, R. Johanni, L. Krämer, B. Lang, H. Lederer, and P. R. Willems, Parallel Comput. 37, 783 (2011).

[57] L. Lin, J. Lu, L. Ying, R. Car, E. Weinan et al., Commun. Math. Sci. 7, 755 (2009).

[58] L. Lin, M. Chen, C. Yang, and L. He, J. Phys.: Condens. Matter 25, 295501 (2013).

[59] L. Lin, A. García, G. Huhs, and C. Yang, J. Phys.: Condens. Matter 26, 305503 (2014).

[60] W. Hu, L. Lin, and C. Yang, J. Chem. Phys. 143, 124110 (2015).

[61] G. Kresse and J. Furthmüller, Phys. Rev. B 54, 11169 (1996).

[62] G. Kresse and J. Furthmüller, Comput. Mater. Sci. 6, 15 (1996).

[63] S. Haldar, H. Vovusha, M. K. Yadav, O. Eriksson, and B. Sanyal, Phys. Rev. B 92, 235408 (2015).

[64] M. Pandey, F. A. Rasmussen, K. Kuhar, T. Olsen, K. W. Jacobsen, and K. S. Thygesen, Nano Lett. 16, 2234 (2016).

[65] H.-Y. Song and J.-T. Lü, AIP Adv. 8, 125323 (2018).

[66] P. V. C. Medeiros, S. Stafström, and J. Björk, Phys. Rev. B 89, 041407(R) (2014).

[67] P. V. C. Medeiros, S. S. Tsirkin, S. Stafström, and J. Björk, Phys. Rev. B 91, 041116(R) (2015).

[68] We chose a $4 \times 2$ supercell since we could not obtain a Wannier Hamiltonian for the $5 \times 3$ supercell.