PHYSICAL REVIEW B 100, 201103(R) (2019)

Rapid Communications

# Unified picture of lattice instabilities in metallic transition metal dichalcogenides

Diego Pasquier$^{\circledR\ast}$ and Oleg V. Yazyev$^{\circledR\dagger}$

Institute of Physics, Ecole Polytechnique Fédérale de Lausanne (EPFL), CH-1015 Lausanne, Switzerland

![](./images/812710506648305664_1.jpg)
(Received 18 January 2019; revised manuscript received 28 October 2019; published 15 November 2019)

Transition metal dichalcogenides (TMDs) in the $1T$ polymorph are subject to a rich variety of periodic lattice distortions, often referred to as charge-density waves (CDWs) when not too strong. We study from first principles the fermiology and phonon dispersion of three representative single-layer transition metal disulfides with different occupation of the $t_{2g}$ subshell: $TaS_{2}$ ($t_{2g}^{1}$), $WS_{2}$ ($t_{2g}^{2}$), and $ReS_{2}$ ($t_{2g}^{3}$) across a broad range of doping levels. While strong electron-phonon interactions are at the heart of these instabilities, we argue that away from half-filling of the $t_{2g}$ subshell, the doping dependence of the calculated CDW wave vector can be explained from simple fermiology arguments, so that a weak-coupling nesting picture is a useful starting point for understanding. On the other hand, when the $t_{2g}$ subshell is closer to half-filling, we show that nesting is irrelevant, while a real-space strong-coupling picture of bonding Wannier functions is more appropriate and simple bond-counting arguments apply. Our study thus provides a unifying picture of lattice distortions in $1T$ TMDs that bridges the two regimes, while the crossover between these regimes can be attained by tuning the filling of the $t_{2g}$ orbitals.

DOI: 10.1103/PhysRevB.100.201103

Layered transition metal dichalcogenides (TMDs) have been the subject of much attention, to a large extent due to the occurrence of a rich variety of lattice instabilities [1–6]. Two-dimensional TMDs [7,8] of composition $MX_{2}$ consist of a triangular lattice of a transition metal $M$, intercalated between two layers of chalcogen atoms ($X = S$, Se, Te). Two high-symmetry configurations of the three atomic planes are possible, leading to two families of polymorphs, referred to as $1T$ and $1H$, respectively.

With a few exceptions, all metallic TMDs experience some form of lattice distortion of various strength [6]. For group V TMDs ($M = V$, Nb, Ta), characterized by a $d^{1}$ formal electronic configuration of the transition metal ion [9], the distortions in both polymorphs are weak to moderate, and are usually referred to as charge-density-wave (CDW) phases [2]. On the other hand, the distortions in group VI ($M =$ Mo, W) and VII ($M =$ Tc, Re) TMDs with $d^{2}$ and $d^{3}$ formal occupations, in the $1T$ polymorph, are much stronger [10,11].

A Peierls mechanism based on the Fermi surface nesting argument [12,13] was originally proposed for $d^{1}$ TMDs in both polymorphs [1,2], although this point of view has often been challenged in the more recent literature [14], with several authors arguing that anisotropic momentum-dependent electron-phonon interactions are required to explain the phenomenology [15]. Real-space chemical bonding arguments have also been proposed [3,16]. Numerous experimental and theoretical studies of CDWs in $d^{1}$ TMDs have been reported lately [16–39]. It is striking that, while certain authors mention a well-understood nesting mechanism, others consider nesting unimportant [14,15,25,26,39]. Whereas the $1H$ polymorph of $d^{2}$ TMDs is semiconducting and stable, the $1T$ phase is highly unstable and distorts into the metastable $1T'$ phase, with $2 \times 1$ periodicity [3,40]. The $1T'$ phase of $d^{2}$ TMDs was recently the focus of intense attention due to its topological properties [41–45], but the mechanism of the distortion has been less discussed. A Peierls nesting mechanism was also suggested for certain Mo dichalcogenides [46,47], based on the inspection of the Fermi surface that reveals pockets apparently nested by the correct wave vectors [48]. TMDs with $d^{3}$ formal occupation are found in a strongly distorted form of the $1T$ polymorph with $2 \times 2$ periodicity (sometimes referred to as $1T''$), with tetramer clusters of transition metal ions forming diamond chains [10,49]. Kertesz and Hoffman first derived the structure theoretically and stressed the role of the strong interactions between in-plane $d_{xy}$ and $d_{x^{2}-y^{2}}$ electrons in driving the distortion [11]. Whangbo and Canadell suggested a complementary picture of both hidden nesting and local chemical bonding [3], as for the $1T'$ phase in $d^{2}$ TMDs. More recently, it has been proposed that the $1T''$ phase should be understood as a Peierls instability of the $1T'$ phase, due to the existence in this phase of quasi-one-dimensional bands at half-filling for $d^{3}$ ions [50].

In this Rapid Communication, we study, from density functional theory calculations, the doping-dependent fermiology and phonon instabilities in $5d$ $1T$ TMDs with increasing $d$-shell population, taking monolayers of the disulfides $TaS_{2}$, $WS_{2}$, and $ReS_{2}$ as examples. For $TaS_{2}$, the doping dependence of the calculated incommensurate CDW (ICDW) wave vector and its correspondence with the bare susceptibility provide a clean demonstration of the effect of the fermiology on the ICDW. We therefore argue that at $n \approx 1$ $d$ electron (i.e., $TaS_{2}$ or heavily hole-doped $WS_{2}$), a weak-coupling $k$-space nesting picture is still a good starting point for understanding, although no sharp divergence is present in the bare susceptibility. On the other hand, we show that for $n \approx 2$–3 $d$ electrons ($WS_{2}$ and $ReS_{2}$), nesting arguments are not useful, and that a real-space strong-coupling picture of bonding Wannier functions (WFs), splitting strongly the $t_{2g}$ triplet, applies and

* diego.pasquier@epfl.ch
† oleg.yazyev@epfl.ch

2469-9950/2019/100(20)/201103(6)
201103-1
©2019 American Physical Society

![](./images/812710506648305664_2.jpg)

FIG. 1. Band structures calculated from first principles for monolayers of (a) $1T$-TaS₂, (b) $1T$-WS₂, and (c) $1T$-ReS₂. The Fermi level is set to zero. Calculated bare static susceptibility along $\Gamma M$ for (d) $1T$-TaS₂, (e) $1T$-WS₂, and (f) $1T$-ReS₂. Calculated dispersion for the lowest acoustic phonon branch along $\Gamma M$ for (g) $1T$-TaS₂, (h) $1T$-WS₂, and (i) $1T$-ReS₂.

provides a simple physical picture. This suggests a crossover between weak-coupling and strong-coupling regimes as a function of the electronic filling of the $t_{2g}$ subshell.

Figures 1(a)–1(c) show the electronic band structures for undistorted monolayers of $1T$-TaS₂, $1T$-WS₂, and $1T$-ReS₂, calculated from first principles in the generalized gradient approximation [51]. Details of the first-principles calculations are given in the Supplemental Material [52] (see also Refs. [53–59] therein). The three bands close to the Fermi level are very similar for the three materials (except for the position of the Fermi level) and have $t_{2g}$ orbital character, i.e., $d_{xy}$, $d_{xz}$, and $d_{yz}$, with the $z$ axis pointing along an M-S bond. The latter choice of coordinates allows one to almost perfectly decouple the two high-energy and three low-energy $d$ orbital degrees of freedom [60], justifying the denomination $t_{2g}^{1}$ for TaS₂, $t_{2g}^{2}$ for WS₂, and $t_{2g}^{3}$ for ReS₂.

Figures 1(d)–1(i) show the discretized bare static susceptibilities and phonon dispersions along the $\Gamma M$ direction, for the three materials and for undoped and hole-doped cases [61]. For the sake of clarity, we have only shown the lowest-energy acoustic phonon mode, that softens for the three materials for all doping levels considered. To evaluate the bare susceptibility, we have adopted the commonly used constant-matrix-elements approximation (CMA), $\chi _{0}(q)=\frac {1}{N_{k}}\sum_{k,n,n'} \frac {f_{nk+q}-f_{n'k}}{\epsilon_{nk+q}-\epsilon_{n'k}}$, where $N_{k}$ is the number of $k$ points in the discretized Brillouin zone, $\epsilon_{nk}$ is the energy of band $n$ at momentum $k$, and $f$ is the Fermi-Dirac distribution. We have included the three $t_{2g}$-like bands in the summation, and set the electronic temperature to 300 K. Using the CMA, the absolute value of the susceptibility is sensitive to the number of bands included in the summation [62]. However, we have verified that the location of the peak for TaS₂, as well as the absence of peaks at $M$ for WS₂ and ReS₂, are robust with respect to the number of bands considered.

In the theory of weak-coupling charge- and spin-density-wave instabilities, the bare susceptibility is the key quantity. Its enhancement at certain wave vectors favors softening of certain phonon or magnon modes, depending on the dominant microscopic interaction, either electron-phonon or electron-electron [13]. In the limit of perfect nesting, the bare susceptibility exhibits logarithmic divergences at momentum $2k_{F}$, leading to instabilities at infinitesimal coupling constant. In real materials, perfect nesting would require unrealistic fine-tuning, but nesting-derived instabilities can still occur provided the interactions are not too weak.

Figure 1(d) shows that, unlike for most two-dimensional (2D) metals, the bare susceptibility of $1T$-TaS₂ does not achieve its maximum at the $\Gamma$ point, but at an incommensurate wave vector along the $\Gamma M$ direction, corresponding to the momentum $q_{ICDW} \approx 0.29b_{i}$ (where $b_{i}$ are the three primitive vectors of the reciprocal lattice) where the calculated phonon softening is maximal. This is due to the approximate nesting properties of the Fermi surface, shown in Fig. 2. Moreover, the calculated peak of the susceptibility, as well as the calculated $q_{ICDW}$, are found sensitive to the exact position of the Fermi level and both change upon doping. Such behavior is typical of a $2k_{F}$ effect and clearly shows the effect of the change of the Fermi surface area upon doping on the ICDW. Experimentally, Ti-doped bulk $1T$-TaS₂ exhibits an ICDW wave vector that decreases with increasing Ti concentration [1,29,63]. For 2D materials, electrostatic doping allows inducing charge carriers in a way that closely resembles the rigid Fermi level shift in our calculations. It would therefore be interesting to address the change of ICDW periodicity in gated TaS₂ and other similar materials. Bulk TaS₂ (and possibly the monolayer as well [64]) undergoes the so-called lock-in transition, where the CDW adopts a periodicity commensurate with the high-symmetry phase, characterized by a commensurate wave

![](./images/812710506648305664_3.jpg)

FIG. 2. Fermi surface of monolayer $1T$-TaS$_2$ (undoped and hole doped). The shaded area delimits the Brillouin zone. Nesting vectors for the undoped case have been drawn.

vector that corresponds to $\sqrt{13} \times \sqrt{13}$ periodicity [65,66]. We stress that the calculated CDW wave vectors and peaks in the susceptibility correspond to the ICDW periodicity, as the lock-in transition results from anharmonic effects.

As Figs. 1(e) and 1(f) show, the maximum phonon softening for the $t_{2g}^2$ and $t_{2g}^3$ cases occurs at the $M$ point, indicating an instability towards doubling the unit cell. Compared to TaS$_2$, the phonon softening occurs over a wider range of momenta and is much stronger. The phonon softening at the $M$ point is clearly not related to any peak in the bare susceptibility calculated in the CMA. Contrary to closely related MoS$_2$ [47] and MoTe$_2$ [46], the Fermi surface of WS$_2$ does not exhibit nested Fermi pockets, which appear only under electron doping [52] and are therefore not responsible for the instability. For $n_{t_{2g}} \approx 3$ (ReS$_2$) the phonon instability is robust against doping, so that the calculated soft phonon mode is not sensitive to the exact number of electrons, contrary to the $n_{t_{2g}} \approx 1$ case. For WS$_2$, the instability at the $M$ point is sensitive to hole doping, and disappears at $n_{\text{hole}} \approx 0.4$. For heavily hole-doped WS$_2$, a behavior analogous to TaS$_2$ is recovered. Small discommensurations are already present at lower doping, but it is not clear whether these could be observed experimentally because of anharmonic effects. Clearly, the instability at the $M$ point is not associated with a nesting mechanism, since the calculated susceptibility is at its minimum. Nesting arguments are perturbative ones, so they become less relevant as the instability grows stronger, as is the case for WS$_2$ and ReS$_2$.

From the considerations above, it appears that lattice distortions in $1T$ $d^2$ and $d^3$ TMDs should be better understood from a strong-coupling perspective. The strong-coupling qualitative picture of CDWs consists in a real-space picture of chemical bonding [5]. In the following, we shall demonstrate and quantify the bonding mechanism behind the $1T'$ and $1T''$ phases using a Wannier-function approach.

We begin by discussing the $1T'$ phase of $d^2$ TMDs, taking again WS$_2$ as a representative example. The relaxed lattice structure is shown in Fig. 3(a). The calculated energy gain upon distortion is large (0.36 eV per formula unit), and the change of the electronic structure is drastic. We have drawn W-W bonds for which the interatomic distance is significantly reduced (2.78 Å vs 3.21 Å in the undistorted $1T$ phase). Such a large shortening of the W-W distance suggests that $t_{2g}$ states pointing toward these bonds interact strongly with their nearest neighbors, forming bonding and antibonding combinations [3]. To verify this hypothesis, we construct maximally localized Wannier functions (MLWFs) [67] by considering two different sets of bands separately to assess the formation of bonding states (see Supplemental Material [52] for details).

Figure 3(b) shows the aligned ligand field (including electrostatic and $pd$ hybridization effects, as we have discussed in Ref. [60]) and modified ligand field energy diagrams for the $1T$ and $1T'$ phases of WS$_2$, obtained using MLWFs [68]. Our Wannier analysis demonstrates that the main effect of the distortion is to split strongly the $t_{2g}$ states into bonding, nonbonding, and antibonding WFs, while the $e_g$ states are weakly affected, although the lifting of degeneracy within the $e_g$ doublet is somewhat increased (0.36 eV vs 0.05 eV in the $1T$ phase). In Fig. 3(a), we show an isovalue plot of one of the two equivalent bonding $t_{2g}$ WFs, centered on a W-W bond (other WF plots are presented in the Supplemental Material [52]). The on-site energies of the nonbonding $t_{2g}$ states, pointing in the direction of the zigzag chain, are found to be very close ($\sim$0.1 eV difference) to those of the undistorted $1T$ phase. On the other hand, the $t_{2g}$ WFs pointing in the W-W bonds directions are split in energy by 3.34 eV. The calculated energy splitting is significantly larger than the half-bandwidth of the undistorted $1T$ phase ($W/2 \approx 2.23$ eV), which one would obtain by simply doubling the unit cell without distortion. This indicates the formation of strong W-W bonds upon translational symmetry breaking. Moreover, Fig. 3(c) shows that the two bonding $t_{2g}$ WFs contribute mainly to the two occupied bands closest to the Fermi level, and are therefore roughly filled by two electrons. The optimal filling of the two strongly bonding WFs explains why the $1T'$ phase is energetically favorable for $n_{t_{2g}} \approx 2$.

Let us now consider the diamond-chain structure (or the $1T''$ phase) of $d^3$ $1T$ TMDs with $2 \times 2$ periodicity, with ReS$_2$ taken as an example. The relaxed structure in the $2 \times 2$ supercell, shown in Fig. 3(d), is associated with a large energy gain of 1.12 eV/f.u. compared to the undistorted $1T$ phase. We have drawn Re-Re bonds, because the interatomic distance between the corresponding Re atoms is significantly reduced compared to the undistorted phase (2.71-2.9 Å vs 3.1 Å in the $1T$ phase).

As for WS$_2$, we have constructed MLWFs by considering separately two sets of bands [52]. The aligned ligand field and modified ligand field energy diagrams for the $1T$ and $1T''$ phases are represented in Fig. 3(e). The whole $t_{2g}$ subshell is strongly split into bonding and antibonding states in the $1T''$ phase. Indeed, we estimate an energy splitting of 3.34 eV, significantly larger than the half-bandwidth of the undistorted $1T$ phase ($W/2 \approx 2.22$ eV). Since not all the shortened bonds are equal in the $1T''$ phases, there are differences in the on-site energies of the corresponding WFs. The bonding WF on the shortest bond (2.71 Å), plotted in Fig. 3(d), is found 0.24 eV lower in energy compared to that centered on the longest bond (2.9 Å). As Fig. 3(f) shows, the bonding $t_{2g}$ WFs contribute mostly to the top of the occupied-bands manifold. Hence, in the $1T''$ phase at $t_{2g}^3$, all the strongly bonding

![](./images/812710506648305664_4.jpg)

FIG. 3. (a) Ball-and-stick representation of the $1T'$ phase of $WS_2$ with an isovalue plot of one of the two equivalent bonding $t_{2g}$ Wannier functions (WFs). W-W bonds have been drawn to facilitate visualization. Each bond accommodates a bonding $t_{2g}$ WF centered on it. (b) Aligned ligand field and modified ligand field energy diagrams for the $1T$ and $1T'$ phases. The bonding (b), nonbonding (nb), and antibonding (ab) $t_{2g}$ states are labeled. (c) Calculated band structure along high-symmetry directions for $1T'$-$WS_2$. The orbital weights of the bonding and antibonding $t_{2g}$ WFs are color-coded. The Fermi level is set to zero. (d)-(f) Corresponding plots for the $1T''$ phase of $ReS_2$.

$t_{2g}$ WFs are fully occupied, explaining the stability of this phase.

In summary, we report a first-principles study of doping-dependent fermiology and phonon instabilities in 2D $1T$ transition metal disulfides at $d^1$, $d^2$, and $d^3$ occupation of the $d$ shell. When the electron filling of the $t_{2g}$ subshell is well below half-filling, as in $TaS_2$, we find that the dependence of the ICDW wave vector on the doping levels matches that of the peak of the bare susceptibility. This behavior is suggestive of a $2k_F$ effect and supports the view that a $k$-space nesting picture is a good, and necessary, starting point for understanding, even though this point of view has often been challenged. When the electron filling of the $t_{2g}$ subshell is closer to half-filling, as in $WS_2$ and $ReS_2$, the behavior is qualitatively different and nesting appears irrelevant. Our Wannier-function analysis shows that the effect of the distortions is mainly to split strongly the $t_{2g}$ states, and that simple bond-counting arguments are qualitatively correct. Our study thus provides a unifying picture of lattice distortions in $1T$ TMDs that bridges two regimes, while the crossover between these regimes can be attained by tuning the electron filling of the $t_{2g}$ orbitals. Although our study considers monolayer transition metal disulfides as examples, the universality of the electronic structure of TMDs allows one to extend our reasoning to other members of this family of materials, with certain ditellurides as possible exceptions, and to bulk and multilayer materials owing to relatively weak interlayer coupling. The proposed two-step methodology can be applied to other materials or classes of materials. Phonon and susceptibility calculations would be the first step, followed by Wannier bonding analysis in case the weak-coupling scenario is found to be irrelevant.

We acknowledge funding by the European Commission under the Graphene Flagship (Grant Agreement No. 696656). We thank QuanSheng Wu for technical assistance. First-principles calculations were performed at the facilities of Scientific IT and Application Support Center of EPFL.

[1] J. A. Wilson, F. J. Di Salvo, and S. Mahajan, *Phys. Rev. Lett.* 32, 882 (1974).
[2] J. A. Wilson, F. J. Di Salvo, and S. Mahajan, *Adv. Phys.* 24, 117 (1975).

201103-4

[3] M. H. Whangbo and E. Canadell, J. Am. Chem. Soc. 114, 9587 (1992).

[4] A. H. Castro Neto, Phys. Rev. Lett. 86, 4382 (2001).

[5] K. Rossnagel, J. Phys.: Condens. Matter 23, 213001 (2011).

[6] S. Manzeli, D. Ovchinnikov, D. Pasquier, O. V. Yazyev, and A. Kis, Nat. Rev. Mater. 2, 17033 (2017).

[7] Q. H. Wang, K. Kalantar-Zadeh, A. Kis, J. N. Coleman, and M. S. Strano, Nat. Nanotechnol. 7, 699 (2012).

[8] M. Chhowalla, H. S. Shin, G. Eda, L.-J. Li, K. P. Loh, and H. Zhang, Nat. Chem. 5, 263 (2013).

[9] L. F. Mattheiss, Phys. Rev. B 8, 3719 (1973).

[10] J. C. Wildervanck and F. Jellinek, J. Less-Common Met. 24, 73 (1971).

[11] M. Kertesz and R. Hoffmann, J. Am. Chem. Soc. 106, 3453 (1984).

[12] R. E. Peierls, *Quantum Theory of Solids* (Oxford University Press, New York, 1955).

[13] S.-K. Chan and V. Heine, J. Phys. F: Met. Phys. 3, 795 (1973).

[14] M. D. Johannes and I. I. Mazin, Phys. Rev. B 77, 165135 (2008).

[15] X. Zhu, Y. Cao, J. Zhang, E. W. Plummer, and J. Guo, Proc. Natl. Acad. Sci. USA 112, 2367 (2015).

[16] S. Yi, Z. Zhang, and J.-H. Cho, Phys. Rev. B 97, 041413(R) (2018).

[17] M. Calandra, I. I. Mazin, and F. Mauri, Phys. Rev. B 80, 241108(R) (2009).

[18] Y. Ge and A. Y. Liu, Phys. Rev. B 86, 104101 (2012).

[19] F. Weber, S. Rosenkranz, J.-P. Castellan, R. Osborn, R. Hott, R. Heid, K.-P. Bohnen, T. Egami, A. H. Said, and D. Reznik, Phys. Rev. Lett. 107, 107403 (2011).

[20] X. Xi, L. Zhao, Z. Wang, H. Berger, L. Forró, J. Shan, and K. F. Mak, Nat. Nanotechnol. 10, 765 (2015).

[21] M. M. Ugeda, A. J. Bradley, Y. Zhang, S. Onishi, Y. Chen, W. Ruan, C. Ojeda-Aristizabal, H. Ryu, M. T. Edmonds, H.-Z. Tsai, A. Riss, S.-K. Mo, D. Lee, A. Zettl, Z. Hussain, Z.-X. Shen, and M. F. Crommie, Nat. Phys. 12, 92 (2016).

[22] J. Á. Silva-Guillén, P. Ordejón, F. Guinea, and E. Canadell, 2D Mater. 3, 035028 (2016).

[23] O. R. Albertini, A. Y. Liu, and M. Calandra, Phys. Rev. B 95, 235121 (2017).

[24] C. Battaglia, H. Cercellier, F. Clerc, L. Despont, M. G. Garnier, C. Koitzsch, P. Aebi, H. Berger, L. Forró, and C. Ambrosch- Draxl, Phys. Rev. B 72, 195114 (2005).

[25] A. Y. Liu, Phys. Rev. B 79, 220515(R) (2009).

[26] Y. Ge and A. Y. Liu, Phys. Rev. B 82, 155133 (2010).

[27] Q. Zhang, L.-Y. Gan, Y. Cheng, and U. Schwingenschlögl, Phys. Rev. B 90, 081103(R) (2014).

[28] Y. Yu, F. Yang, X. F. Lu, Y. J. Yan, Y.-H. Cho, L. Ma, X. Niu, S. Kim, Y.-W. Son, D. Feng *et al.*, Nat. Nanotechnol. 10, 270 (2015).

[29] X. M. Chen, A. J. Miller, C. Nugroho, G. A. de la Peña, Y. I. Joe, A. Kogar, J. D. Brock, J. Geck, G. J. MacDougall, S. L. Cooper, E. Fradkin, D. J. Van Harlingen, and P. Abbamonte, Phys. Rev. B 91, 245113 (2015).

[30] D. F. Shao, R. C. Xiao, W. J. Lu, H. Y. Lv, J. Y. Li, X. B. Zhu, and Y. P. Sun, Phys. Rev. B 94, 125126 (2016).

[31] D. C. Miller, S. D. Mahanti, and P. M. Duxbury, Phys. Rev. B 97, 045133 (2018).

[32] D. Sakabe, Z. Liu, K. Suenaga, K. Nakatsugawa, and S. Tanda, npj Quantum Mater. 2, 22 (2017).

[33] E. Kamil, J. Berges, G. Schönhoff, M. Rösner, M. Schüler, G. Sangiovanni, and T. Wehling, J. Phys.: Condens. Matter 30, 325601 (2018).

[34] M. Calandra, Phys. Rev. Lett. 121, 026401 (2018).

[35] D. Pasquier and O. V. Yazyev, Phys. Rev. B 98, 045114 (2018).

[36] Á. Pásztor, A. Scarfato, C. Barreteau, E. Giannini, and C. Renner, 2D Mater. 4, 041005 (2017).

[37] D. Zhang, J. Ha, H. Baek, Y.-H. Chan, F. D. Natterer, A. F. Myers, J. D. Schumacher, W. G. Cullen, A. V. Davydov, Y. Kuk, M. Y. Chou, N. B. Zhitenev, and J. A. Stroscio, Phys. Rev. Mater. 1, 024005 (2017).

[38] Y. Umemoto, K. Sugawara, Y. Nakata, T. Takahashi, and T. Sato, Nano Res. 12, 165 (2018).

[39] M. Mulazzi, A. Chainani, N. Katayama, R. Eguchi, M. Matsunami, H. Ohashi, Y. Senba, M. Nohara, M. Uchida, H. Takagi, and S. Shin, Phys. Rev. B 82, 075130 (2010).

[40] K.-A. N. Duerloo, Y. Li, and E. J. Reed, Nat. Commun. 5, 4214 (2014).

[41] X. Qian, J. Liu, L. Fu, and J. Li, Science 346, 1344 (2014).

[42] Z. Fei, T. Palomaki, S. Wu, W. Zhao, X. Cai, B. Sun, P. Nguyen, J. Finney, X. Xu, and D. H. Cobden, Nat. Phys. 13, 677 (2017).

[43] S. Tang, C. Zhang, D. Wong, Z. Pedramrazi, H.-Z. Tsai, C. Jia, B. Moritz, M. Claassen, H. Ryu, S. Kahn *et al.*, Nat. Phys. 13, 683 (2017).

[44] A. Pulkin and O. V. Yazyev, J. Electron. Spectrosc. Relat. Phenom. 219, 72 (2017).

[45] M. M. Ugeda, A. Pulkin, S. Tang, H. Ryu, Q. Wu, Y. Zhang, D. Wong, Z. Pedramrazi, A. Martín-Recio, Y. Chen, F. Wang, Z.-X. Shen, S.-K. Mo, O. V. Yazyev, and M. F. Crommie, Nat. Commun. 9, 3401 (2018).

[46] D. H. Keum, S. Cho, J. H. Kim, D.-H. Choe, H.-J. Sung, M. Kan, H. Kang, J.-Y. Hwang, S. W. Kim, H. Yang, K. J. Chang, and Y. H. Lee, Nat. Phys. 11, 482 (2015).

[47] S. N. Shirodkar and U. V. Waghmare, Phys. Rev. Lett. 112, 157601 (2014).

[48] In Ref. [47], the calculated instability for MoS₂ is maximal at the $K$ point (corresponding to $\sqrt{3} \times \sqrt{3}$ periodicity) instead of the $M$ point. This is due to the use of a too coarse grid of $q$ points for Fourier interpolation. The proposed nesting mechanism in Ref. [47] is to explain the instability at the $K$ point.

[49] S. Tongay, H. Sahin, C. Ko, A. Luce, W. Fan, K. Liu, J. Zhou, Y.-S. Huang, C.-H. Ho, J. Yan *et al.*, Nat. Commun. 5, 3252 (2014).

[50] J.-H. Choi and S.-H. Jhi, J. Phys.: Condens. Matter 30, 105403 (2018).

[51] J. P. Perdew, K. Burke, and M. Ernzerhof, Phys. Rev. Lett. 77, 3865 (1996).

[52] See Supplemental Material at http://link.aps.org/supplemental/10.1103/PhysRevB.100.201103 for details about the methodology and the first-principles calculations, the isovalue plot of other Wannier functions, and for plots of Fermi surfaces.

[53] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G. L. Chiarotti, M. Cococcioni, I. Dabo *et al.*, J. Phys.: Condens. Matter 21, 395502 (2009).

[54] D. R. Hamann, Phys. Rev. B 88, 085117 (2013).

[55] P. Scherpelz, M. Govoni, I. Hamada, and G. Galli, J. Chem. Theory Comput. 12, 3523 (2016).

[56] See http://www.quantum-simulation.org/potentials/sg15_oncv/.

[57] N. Marzari, D. Vanderbilt, A. De Vita, and M. C. Payne, Phys. Rev. Lett. 82, 3296 (1999).

[58] A. A. Mostofi, J. R. Yates, G. Pizzi, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, Comput. Phys. Commun. 185, 2309 (2014).

[59] S. Baroni, S. de Gironcoli, A. Dal Corso, and P. Giannozzi, Rev. Mod. Phys. 73, 515 (2001).

[60] D. Pasquier and O. V. Yazyev, 2D Mater. 6, 025015 (2019).

[61] For definiteness, we study the hole doping to understand the effect of doping in these materials. The electron-doped case is analogous.

[62] C. Heil, H. Sormann, L. Boeri, M. Aichhorn, and W. von der Linden, Phys. Rev. B 90, 115143 (2014).

[63] F. J. Di Salvo, J. A. Wilson, B. G. Bagley, and J. V. Waszczak, Phys. Rev. B 12, 2220 (1975).

[64] O. R. Albertini, R. Zhao, R. L. McCann, S. Feng, M. Terrones, J. K. Freericks, J. A. Robinson, and A. Y. Liu, Phys. Rev. B 93, 214109 (2016).

[65] W. L. McMillan, Phys. Rev. B 12, 1187 (1975).

[66] W. L. McMillan, Phys. Rev. B 14, 1496 (1976).

[67] N. Marzari and D. Vanderbilt, Phys. Rev. B 56, 12847 (1997).

[68] A. Scaramucci, J. Ammann, N. Spaldin, and C. Ederer, J. Phys.: Condens. Matter 27, 175503 (2015).