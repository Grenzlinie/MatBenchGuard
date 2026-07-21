PHYSICAL REVIEW B 94, 195104 (2016)

# Topological node-line semimetal in compressed black phosphorus

Jianzhou Zhao, $^{1,2}$ Rui Yu, $^{3, *}$ Hongming Weng, $^{1,4, \dagger}$ and Zhong Fang $^{1,4}$

$^{1}$ Beijing National Laboratory for Condensed Matter Physics, and Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China
$^{2}$ Co-Innovation Center for New Energetic Materials, Southwest University of Science and Technology, Mianyang, Sichuan 621010, China
$^{3}$ Department of Physics, Harbin Institute of Technology, Harbin 150001, China
$^{4}$ Collaborative Innovation Center of Quantum Matter, Beijing 100190, China

(Received 18 November 2015; revised manuscript received 2 August 2016; published 2 November 2016)

Based on first-principles calculations and tight-binding model analysis, we propose that black phosphorus (BP) can host a three-dimensional topological node-line semimetal state under pressure when spin-orbit coupling (SOC) is ignored. A closed topological node line exists in the first Brillouin zone (BZ) near the Fermi energy, which is protected by the coexistence of time-reversal and spatial inversion symmetry with band inversion driven by pressure. Drumheadlike surface states have been obtained on the beard (100) surface. Due to the weak intrinsic SOC of a phosphorus atom, a band gap less than 10 meV is opened along the node line in the presence of SOC, and the surface states are almost unaffected by SOC.

DOI: 10.1103/PhysRevB.94.195104

## I. INTRODUCTION

The discovery of topological states of matter has attracted broad interest in recent years. It was ignited by the discovery of two-dimensional (2D) and three-dimensional (3D) topological insulators (TIs) [1–5]. These materials exhibit a bulk energy gap between the valence and conduction bands, similarly to normal insulators, but possess unique gapless boundary states that are protected by the topology of bulk states. Topological states have also been proposed for 3D metals with stable Fermi surface [6], as topological semimetals (TSM). Recently, there has been great research interest for novel 3D metals with nontrivial band topology defined on their compact and continuous Fermi surface, which can be looked at as the counterpart of the whole 2D BZ of insulator [7]. Generally speaking, these 3D metals are topologically stable for their Fermi surfaces enclose nontrivial degenerate band touch points (BTP). Such BTP behaves as the “source” or “sink” of Berry flux and brings quantized Berry flux when passing through the surrounding enclosed Fermi surface [8]. This quantized number can be taken as the topological invariant to identify the band topology of corresponding metals. According to the Fermi-liquid theory, the physical properties of metals are mostly determined by the lower energy part around the Fermi level. Therefore, the closer the Fermi level to the BTP, the better for manifesting the unique properties from the band topology of the Fermi surfaces. The ideal case is that the whole BZ has just the BTP points at the Fermi level. In this ideal case, the density of states at Fermi energy is zero, and that’s why such nontrivial 3D metals are called topological semimetals. Up to now, three types of TSM, namely Weyl semimetal (WSM), Dirac semimetal (DSM), and node-line semimetal (NLS) based on the BTPs’ degeneracy and distribution in BZ, have been proposed. For WSM, the BTPs are double degenerate, having definite chirality and appearing in isolated pairs, which are in fact the quasiparticle of Weyl fermions. For DSM, the BTPs are fourfold degenerate and can be looked at as the “kiss” of two Weyl fermions with opposite chirality in BZ. For NLS [9], the BTPs around the Fermi level form closed loops in BZ. These three type of TSMs constitute the TSM “trio.” The intriguing expected properties characterizing above TSMs include the surface Fermi arc, the nearly flat surface bands, the negative magnetoresistivity due to chiral anomaly and the unique Landau energy level.

Presently, the experimentally extensively studied DSMs are $Na_3Bi$ and $Cd_3As_2$ [10], both of which were predicted theoretically [7,11] and then confirmed by several experiments [12–16]. Starting from DSM, which serves as a singularity point of various topological quantum states, one can obtain WSM by breaking either time-reversal [17,18] or inversion symmetry [19,20]. The prediction of WSM state in the nonmagnetic and noncentrosymmetric TaAs family [21,22] have been verified by experiments [23–28]. For the third member of TSM, the coexistence of time-reversal and inversion symmetry protects NLS in 3D momentum space when SOC is neglected and band inversion happens [29–35]. Based on this, there have been several carbon allotropes re-examined or proposed as host of NLS, including Mackay-Terrones crystal [29], Bernal graphite [36], hyper-honeycomb lattices [37], and the interpenetrated graphene network [38]. It was also shown that mirror symmetry, instead of inversion symmetry, together with time-reversal symmetry can protect NLS when SOC is neglected, like TaAs [21] and $Ca_3P_2$ [34,39]. Due to the correspondence between Dirac line in bulk and surface states at the boundary [9,40], the characteristic surface “drumhead”-like state is demonstrated on the NLS surface [29–31]. Such 2D surface states with nearly zero dispersion are proposed as a route to achieving high-temperature superconductivity [36,41].

In the present work, based on first-principles calculations and tight-binding model Hamiltonian analysis, we predict that BP under pressure is another candidate for NLS. The rest of the paper is organized as follows. In Sec. II, we present the crystal structure and the first-principles calculation

*yurui@hit.edu.cn
†hmweng@iphy.ac.cn

2469-9950/2016/94(19)/195104(5)
195104-1
©2016 American Physical Society

methodology. Then we present the bulk and surface electronic structure of compressed BP form first-principles calculations in Sec. III A. In Sec. III B, a four-bands tight-binding model is constructed and the NL structure, the surface states related to the terminate way on the (100) surface, are studied from the four-bands tight-binding model. Conclusions are given at the end of this paper.

## II. THE CRYSTAL STRUCTURE AND COMPUTATION METHOD

BP is the most stable allotrope of the element of phosphorus at ordinary temperatures and pressure, which was successfully synthesized 100 years ago [42] and has attracted great interest in its monolayers, few-layer, and thin film structure in recent years [43-46]. It has been proposed that the properties of BP can be effectively controlled by strain [47-51]. A uniaxial compressive strain will switch BP from a direct band gap semiconductor to an indirect band gap semiconductor, semimetal, or metal [47]. A moderate hydrostatic pressure effectively suppresses the band gap and induces Lifshitz transition from semiconductor to semimetal accompanied with SdH oscillations and giant magnetoresistance [50,51]. A semiconductor to band-inverted semimetal transition is also reported that can be tuned by a vertical electric field to form dopants in few-layer BP, and the DSM can be achieved at the critical field [52].

The orthorhombic bulk BP belongs to the $Cmce$ space group (No. 64) with a layered structure. Each layer is a 2D hexagonal lattice which is puckered along the armchair direction. These monolayers are stacked along the $z$ direction with van der Waals interactions between them as shown in Fig. 1(a). The first-principle calculations are performed by using the Vienna $ab$ $initio$ simulation package (VASP) based on generalized gradient approximation in Perdew-Burke- Ernzerhof (PBE) [53] type and the projector augmented-wave (PAW) pseudopotential [54]. The energy cutoff is set to 400 eV for the plane-wave basis, and the BZ integration was performed on a regular mesh of $10\times14\times8k$ points. A tight-binding model based on the maximally localized Wannier functions (MLWF) method [55,56] has been constructed in order to investigate the surface states in the (100) direction.

## III. RESULTS AND DISCUSSION

### A. Electronic structure

The volume of the primitive cell for the uncompressed BP is $V_0=85.51$ $\mathring{\text{A}}^3$ with the lattice parameters $a=4.57$ $\mathring{\text{A}}$, $b=5.90$ $\mathring{\text{A}}$, and $c=11.33$ $\mathring{\text{A}}$, and it is a semiconductor with a gap of about 200 meV [45]. For the compressed crystal with volume $V=75.25$ $\mathring{\text{A}}\approx0.88V_0$, where the optimized lattice parameters are $a=4.34$ $\mathring{\text{A}}$, $b=5.50$ $\mathring{\text{A}}$, and $c=10.49$ $\mathring{\text{A}}$ and the crystal keeps the same symmetry as the uncompressed lattice [57], an interesting feature emerges that the energy of valence and conduction bands invert around the $Z$ point in the BZ, and the BP becomes semimetal [50,51,58,59]. The band structure of compressed bulk BP is presented in Fig. 1(d), and the gap at the $Z$ point as a function of volume is shown in Fig. 1(e). Near the Fermi energy, two bands with opposite parity are inverted around the $Z$ point as the volume of the cell is less than the critical values. The intriguing point of the band structure is that the band crossings due to the band inversion form a node ring around the $Z$ point in the $T$-$Z$-$\Gamma$ plane of the BZ as shown in Fig. 1(c), which is protected by the coexistence of time-reversal and inversion symmetry as addressed in Refs. [29,30]. Only one node line is presented in the BZ, which is different from the all-carbon Mackay-Terrones crystal [29] and antiperovskite $Cu_3PdN$ [30,31] where three node lines exist due to the cubic symmetry in these systems. In the presence of SOC, gaps are opened along the node line. It's about 10 meV along the $Z$-$\Gamma$ direction and 2 meV along the $T$-$\Gamma$ direction due to the weak SOC strength of phosphorus atoms. These results show that the influence of SOC can be neglected as the temperature is higher than 100 K. As described in Ref. [33], there are two types of topological numbers for node-line semimetal, the 1D $Z_2$ number and the 2D $Z_2$ number. For the compressed BP, the 1D $Z_2$ number is nonzero for which we can choose a closed loop in the 3D BZ which pierces the node line, and the $Z_2$ number is just the Berry phase along the loop which is quantized to $\pi$. Because the node line can be shrunk to a node point and further gapped out as the band order changes from the inversion order to the normal order by tuning the pressure, the 2D $Z_2$ number is zero for the compressed BP. Though the 2D $Z_2$ index is trivial, the node-line structure is stable as long as the band inversion condition is satisfied.

![](./images/811118436586356737_1.jpg)

FIG. 1. (a) Crystal structure of bulk BP and the hopping parameters $t_{ij}$ of the tight-binding model. The surface in the (100) direction with zigzag type and beard type surface are presented in (a) and (b), respectively. (c) Brillouin zone of the bulk BP. The node line is schematically shown with red color circle which surrounds the $Z$ point and lies on the $T$-$Z$-$\Gamma$ plane. (d) The band structures of BP under hydrostatic pressure are shown with black color. Band structures calculated by using a four-bands tight-binding model are shown with red dashed curves. (e) Energy gap at the $Z$ point as a function of volumes.

The band inversion and the node line in compressed BP indicates that a novel topologically nontrivial surface state can exist on the surface of bulk BP. In order to calculate

![](./images/811118436586356737_2.jpg)

FIG. 2. The surface states of compressed BP on the (a) zigzag type and (b) beard type surface in the (100) direction. The surface states exist outside the node ring for the zigzag type surface and inside the node ring for the beard type surface.

such surface states, we construct a tight-binding Hamiltonian from MLWF method and obtain a thick slab along the (100) direction. There are two types of surface in the (100) direction: the zigzag type and the beard type as shown in Figs. 1(a) and 1(b). For the zigzag surface, the calculated surface states are located outside the node ring as shown in Fig. 2(a). We attach H atoms on the zigzag type surface to form the beard surface. A nearly flat surface state exists inside the node ring as present in Fig. 2(b). The 2D structure of the surface states is presented in Fig. 3(a). The nearly flat dispersion of the surface states is proposed as a route to achieving high-temperature superconductivity [36,41]. In the presence of SOC, the node-line semimetal becomes a topological insulator, and the nearly flat surface states become a Dirac cone. The real space distribution of wave functions at three special k points as indicated in Fig. 2(b) is presented in Fig. 3(b). At the center of the surface state, the wave function is localized on the surface region, with a penetration depth of about five layers (about 2.5 nm). Moving away from the center, the distribution of wave function extends from surface to bulk.

### B. Four-bands tight-binding model

In this section, we analyze the properties of BP by performing a four-bands tight-binding model. The tight-binding model is given as [46]

$$
H=\sum_{i} \epsilon_{i} c_{i}^{\dagger} c_{i}+\sum_{i \neq j} t_{i j} c_{i}^{\dagger} c_{j},
\tag{1}
$$

where the summation $i$ runs over the lattice sites, $c_{i}^{\dagger}(c_{j})$ is the creation (annihilation) operator of electrons at site $i$ ($j$), $\epsilon_{i}$ is the on-site energy parameter, and $t_{i j}$ is the hopping parameter between the $i$th and $j$th sites as shown in Fig. 1(a). The fitted parameters read as $\epsilon=-1.1112$ eV, $t_{1}^{\parallel}=-1.3298$ eV, $t_{2}^{\parallel}=4.2265$ eV, $t_{3}^{\parallel}=-0.3605$ eV, $t_{4}^{\parallel}=-0.1621$ eV, $t_{1}^{\perp}=0.5558$ eV, and $t_{2}^{\perp}=0.2303$ eV.

![](./images/811118436586356737_3.jpg)

FIG. 3. (a) The side view of the surface state nested inside the node ring. (b) The real space distribution of wave function $(|\psi_{nk}(\mathbf{r})|^{2})$ at three different $k$ points [$K_{1}$, $K_{2}$, and $K_{3}$ which are indicated in Fig. 2(b)] on a slab with 80 layers. The surface states are localized on the surface with a penetration depth of about five layers (5 Å each layer).

By performing the Fourier transformation, we obtain the Hamiltonian in momentum space as $H=\sum_{k} c^{\dagger}(k) H(k) c(k)$, with

$$
H(k)=\epsilon+\begin{bmatrix}
0 & h_{12} & h_{13} & h_{14} \\
& 0 & h_{23} & h_{24} \\
& & 0 & h_{34} \\
\dag & & & 0
\end{bmatrix},
\tag{2}
$$

where

$$
\begin{aligned}
h_{12} &=t_{1}^{\parallel}(1+e^{-i k \cdot a_{2}})+t_{3}^{\parallel}(e^{-i k \cdot a_{1}}+e^{-i k \cdot(a_{1}+a_{2})}), \\
h_{13} &=t_{4}^{\parallel}(1+e^{-i k \cdot a_{2}}+e^{-i k \cdot a_{1}}+e^{-i k \cdot(a_{1}+a_{2})}) \\
& \quad +t_{2}^{\perp}(e^{-i k \cdot a_{3}}+e^{-i k \cdot(a_{1}+a_{3})}), \\
h_{14} &=t_{2}^{\parallel} e^{-i k \cdot(a_{1}+a_{2})} \\
& \quad +t_{1}^{\perp}(e^{-i k \cdot(a_{1}+a_{3})}+e^{-i k \cdot(a_{1}+a_{2}+a_{3})}), \\
h_{23} &=t_{2}^{\parallel}+t_{1}^{\perp}(e^{-i k \cdot a_{3}}+e^{i k \cdot(a_{2}-a_{3})}), \\
h_{24} &=h_{13}, \quad h_{34}=h_{12},
\tag{3}
\end{aligned}
$$

where $a_{1,2,3}$ are the lattice axis, and the basis functions $(\phi_{1},\phi_{2},\phi_{3},\phi_{4})$ located on the four P atoms in the unit cell are sketched in Fig. 1(a). The band structure calculated by using the tight-binding model in comparison with the first-principle

bands is shown in Fig. 1(d). One can see that the four-bands model is good enough to describe the low energy band structure of BP. Near the Fermi energy, both the valence and conduction band are well reproduced within the energy region of ±0.25 eV. Beyond that region, the four-bands model does not give a reliable description due to the limit number of basis and also for the basis function with different symmetry compared to the $p$ orbits of phosphorus [46].

As proposed in Ref. [40], the surface states are directly related to the nonzero Berry phase of a one-dimensional system. In the following section, we study the one-dimensional systems parameterized by the in-plane momentum $k_{\parallel}=(k_{2},k_{3})$ for the zigzag and beard type surface and show its relation to the surface states for these two cases.

The Berry phase for the one-dimensional system is defined as
$$
\theta(k_{\parallel})=\sum_{n \in occu.} \int d k_{1} A_{n n}^{1}(k_{\parallel}) \tag{4}
$$
where the summation $n$ runs over occupied states, and $A^{1}(k_{\parallel})$ is the Berry connection matrix which is defined as $A_{m n}^{1}(k_{\parallel})=\langle u_{m}(\mathbf{k})|i \partial_{k_{1}}| u_{n}(\mathbf{k})\rangle$ where $m$ and $n$ are band indices for the occupied states. To calculate the Berry phase numerically, we use the method proposed in Refs. [4,8,60], where the Berry connection $A(k_{\parallel})$ can be calculated discretely by introducing the $F$ matrix which is defined as
$$
F_{m,n}^{i,i+1}(k_{\parallel})=\langle m,k_{1,i},k_{\parallel}|n,k_{1,i+1},k_{\parallel}\rangle \approx e^{-i A_{m,n}^{i,i+1}(k_{\parallel}) \delta k_{1}}, \tag{5}
$$
where $i=0,\dots,N_{1}$ defines the discretized position along the $k_{1}$ direction in the BZ and $\delta k=2\pi/N_{1}a_{1}$. We can define the product of $F_{i,i+1}$s as
$$
D(k_{\parallel})=F_{0,1}F_{1,2}\dots F_{N_{1}-2,N_{1}-1}F_{N_{1}-1,0}. \tag{6}
$$

Substitute Eq. (5) into the above equation, we have that
$$
\begin{aligned}
D(k_{\parallel})&=\prod_{i=0}^{N_{1}-1}F_{i,i+1}=\prod_{i=0}^{N_{1}-1}e^{-i A^{i,i+1}(k_{\parallel}) \delta k} \\
&=\left\{ P\exp \left[ \int_{k_{1}} -i A^{1}(k_{\parallel}) dk \right] \right\}. \tag{7}
\end{aligned}
$$

Then the Berry phase can be obtained as
$$
\theta(k_{\parallel})=\Im\left\{ \log[\det(D(k_{\parallel}))] \right\} \mod 2\pi. \tag{8}
$$

Here, the identical equation $\det[e^{M}]=e^{trM}$ for the square matrix $M$ is used to obtain Eq. (8). The eigenstates for Hamiltonian 2 can be numerically obtained, and the Berry phase can be calculated following Eqs. (5)-(8). The calculated Berry phase for the zigzag type surface equals $\pi$ for $k_{\parallel}$ outside the node ring, while it is zero for $k_{\parallel}$ inside the node ring.

For the beard type surface, the Hamiltonian matrix elements in Eq. (2) are listed as
$$
\begin{aligned}
h_{12}=&t_{2}^{\parallel}+t_{1}^{\perp}\left(e^{i k \cdot a_{3}}+e^{-i k \cdot\left(a_{2}-a_{3}\right)}\right), \\
h_{13}=&t_{4}^{\parallel}\left(1+e^{-i k \cdot a_{2}}+e^{-i k \cdot a_{1}}+e^{-i k \cdot\left(a_{1}+a_{2}\right)}\right) \\
&+t_{2}^{\perp}\left(e^{-i k \cdot\left(a_{2}-a_{3}\right)}+e^{-i k \cdot\left(a_{1}+a_{2}-a_{3}\right)}\right), \\
h_{14}=&t_{1}^{\parallel}\left(e^{-i k \cdot a_{1}}+e^{-i k \cdot\left(a_{1}+a_{2}\right)}\right)+t_{3}^{\parallel}\left(1+e^{-i k \cdot a_{2}}\right), \\
h_{23}=&t_{1}^{\parallel}\left(1+e^{-i k \cdot a_{2}}\right)+t_{3}^{\parallel}\left(e^{-i k \cdot a_{1}}+e^{-i k \cdot\left(a_{1}+a_{2}\right)}\right), \\
h_{24}=&t_{4}^{\parallel}\left(1+e^{-i k \cdot a_{2}}+e^{-i k \cdot a_{1}}+e^{-i k \cdot\left(a_{1}+a_{2}\right)}\right) \\
&+t_{2}^{\perp}\left(e^{-i k \cdot a_{3}}+e^{-i k \cdot\left(a_{1}+a_{3}\right)}\right), \\
h_{34}=&t_{2}^{\parallel}+t_{1}^{\perp}\left(e^{-i k \cdot a_{3}}+e^{i k \cdot\left(a_{2}-a_{3}\right)}\right), \tag{9}
\end{aligned}
$$
where the basis is indicated in Fig. 1(b). The calculated Berry phase for the beard surface is just on the contrary to the zigzag case, which is in agreement with the surface states as shown in Fig. 2.

## IV. CONCLUSION
In summary, we propose that the 3D topological NLS states can be realized in the compressed bulk BP when SOC is ignored. A closed node line is found near the Fermi energy, which is protected by time-reversal and inversion symmetry with the band inverted in the bulk band structure. The two-dimensional surface states are studied in the (100) direction terminated with zigzag and beard type surface. The surface states are nested inside the closed node line on the beard type surface. Its nearly flat energy dispersion is an ideal playground for many interaction induced nontrivial states, such as fractional topological insulator and high-temperature superconductivity.

## ACKNOWLEDGMENTS
This work was supported by the National Natural Science Foundation of China (No. 11274359, No. 11422428, No. 41574076, No. 11604273, and No. 11674077), the 973 program of China (No. 2011CBA00108 and No. 2013CB921700), and the Strategic Priority Research Program (B) of the Chinese Academy of Sciences (No. XDB07020100). R.Y. acknowledges funding from the Fundamental Research Funds for the Central Universities (Grant No. AUGA5710059415) and the National Thousand Young Talents Program.

[1] M. Z. Hasan and C. L. Kane, *Rev. Mod. Phys.* **82**, 3045 (2010).
[2] X.-L. Qi and S.-C. Zhang, *Rev. Mod. Phys.* **83**, 1057 (2011).
[3] B. A. Bernevig and T. L. Hughes, *Topological Insulators and Topological Superconductors* (Princeton University Press, Princeton and Oxford, 2013).
[4] H. Weng, X. Dai, and Z. Fang, *MRS Bulletin* **39**, 849 (2014).
[5] H. Zhang and S.-C. Zhang, *Phys. Status Solidi RRL* **7**, 72 (2013).
[6] P. Hořava, *Phys. Rev. Lett.* **95**, 016405 (2005).
[7] Z. Wang, Y. Sun, X.-Q. Chen, C. Franchini, G. Xu, H. Weng, X. Dai, and Z. Fang, *Phys. Rev. B* **85**, 195320 (2012).
[8] H. Weng, R. Yu, X. Hu, X. Dai, and Z. Fang, *Adv. Phys.* **64**, 227 (2015).
[9] A. A. Burkov, M. D. Hook, and L. Balents, *Phys. Rev. B* **84**, 235126 (2011).
[10] B.-J. Yang and N. Nagaosa, *Nat. Commun.* **5**, 4898 (2014).
[11] Z. Wang, H. Weng, Q. Wu, X. Dai, and Z. Fang, *Phys. Rev. B* **88**, 125427 (2013).

[12] A. Pariari, P. Dutta, and P. Mandal, *Phys. Rev. B* **91**, 155139 (2015).

[13] L. P. He, X. C. Hong, J. K. Dong, J. Pan, Z. Zhang, J. Zhang, and S. Y. Li, *Phys. Rev. Lett.* **113**, 246402 (2014).

[14] M. Neupane, S.-Y. Xu, R. Sankar, N. Alidoust, G. Bian, C. Liu, I. Belopolski, T.-R. Chang, H.-T. Jeng, H. Lin, A. Bansil, F. Chou, and M. Z. Hasan, *Nat. Commun.* **5**, 3786 (2014).

[15] Z. K. Liu, B. Zhou, Y. Zhang, Z. J. Wang, H. M. Weng, D. Prabhakaran, S.-K. Mo, Z. X. Shen, Z. Fang, X. Dai, Z. Hussain, and Y. L. Chen, *Science* **343**, 864 (2014).

[16] Z. K. Liu, J. Jiang, B. Zhou, Z. J. Wang, Y. Zhang, H. M. Weng, D. Prabhakaran, S. K. Mo, H. Peng, P. Dudin, T. Kim, M. Hoesch, Z. Fang, X. Dai, Z. X. Shen, D. L. Feng, Z. Hussain, and Y. L. Chen, *Nat. Mater.* **13**, 677 (2014).

[17] X. Wan, A. M. Turner, A. Vishwanath, and S. Y. Savrasov, *Phys. Rev. B* **83**, 205101 (2011).

[18] G. Xu, H. Weng, Z. Wang, X. Dai, and Z. Fang, *Phys. Rev. Lett.* **107**, 168306 (2011).

[19] G. B. Halász and L. Balents, *Phys. Rev. B* **85**, 035103 (2012).

[20] J. Liu and D. Vanderbilt, *Phys. Rev. B* **90**, 155316 (2014).

[21] H. Weng, C. Fang, Z. Fang, B. A. Bernevig, and X. Dai, *Phys. Rev. X* **5**, 011029 (2015).

[22] S.-M. Huang, S.-Y. Xu, I. Belopolski, C.-C. Lee, G. Chang, B. Wang, N. Alidoust, G. Bian, M. Neupane, C. Zhang, S. Jia, A. Bansil, H. Lin, and M. Z. Hasan, *Nat. Commun.* **6**, 7373 (2015).

[23] B. Q. Lv, H. M. Weng, B. B. Fu, X. P. Wang, H. Miao, J. Ma, P. Richard, X. C. Huang, L. X. Zhao, G. F. Chen, Z. Fang, X. Dai, T. Qian, and H. Ding, *Phys. Rev. X* **5**, 031013 (2015).

[24] X. Huang, L. Zhao, Y. Long, P. Wang, D. Chen, Z. Yang, H. Liang, M. Xue, H. Weng, Z. Fang, X. Dai, and G. Chen, *Phys. Rev. X* **5**, 031023 (2015).

[25] B. Q. Lv, N. Xu, H. M. Weng, J. Z. Ma, P. Richard, X. C. Huang, L. X. Zhao, G. F. Chen, C. E. Matt, F. Bisti, V. N. Strocov, J. Mesot, Z. Fang, X. Dai, T. Qian, M. Shi, and H. Ding, *Nat. Phys.* **11**, 724 (2015).

[26] S.-Y. Xu, I. Belopolski, N. Alidoust, M. Neupane, G. Bian, C. Zhang, R. Sankar, G. Chang, Z. Yuan, C.-C. Lee, S.-M. Huang, H. Zheng, J. Ma, D. S. Sanchez, B. Wang, A. Bansil, F. Chou, P. P. Shibayev, H. Lin, S. Jia, and M. Z. Hasan, *Science* **349**, 613 (2015).

[27] N. Xu, H. M. Weng, B. Q. Lv, C. Matt, J. Park, F. Bisti, V. N. Strocov, D. gawryluk, E. Pomjakushina, K. Conder, N. C. Plumb, M. Radovic, G. Autès, O. V. Yazyev, Z. Fang, X. Dai, G. Aeppli, T. Qian, J. Mesot, H. Ding, and M. Shi, *Nat. Commun.* **7**, 11006 (2016).

[28] B. Q. Lv, S. Muff, T. Qian, Z. D. Song, S. M. Nie, N. Xu, P. Richard, C. E. Matt, N. C. Plumb, L. X. Zhao, G. F. Chen, Z. Fang, X. Dai, J. H. Dil, J. Mesot, M. Shi, H. M. Weng, and H. Ding, *Phys. Rev. Lett.* **115**, 217601 (2015).

[29] H. Weng, Y. Liang, Q. Xu, R. Yu, Z. Fang, X. Dai, and Y. Kawazoe, *Phys. Rev. B* **92**, 045108 (2015).

[30] R. Yu, H. Weng, Z. Fang, X. Dai, and X. Hu, *Phys. Rev. Lett.* **115**, 036807 (2015).

[31] Y. Kim, B. J. Wieder, C. L. Kane, and A. M. Rappe, *Phys. Rev. Lett.* **115**, 036806 (2015).

[32] C.-K. Chiu and A. P. Schnyder, *Phys. Rev. B* **90**, 205136 (2014).

[33] C. Fang, Y. Chen, H.-Y. Kee, and L. Fu, *Phys. Rev. B* **92**, 081201 (2015).

[34] Y.-H. Chan, C.-K. Chiu, M. Y. Chou, and A. P. Schnyder, *Phys. Rev. B* **93**, 205132 (2016).

[35] G. Bian, T.-R. Chang, R. Sankar, S.-Y. Xu, H. Zheng, T. Neupert, C.-K. Chiu, S.-M. Huang, G. Chang, I. Belopolski, D. S. Sanchez, M. Neupane, N. Alidoust, C. Liu, B. Wang, C.-C. Lee, H.-T. Jeng, C. Zhang, Z. Yuan, S. Jia, A. Bansil, F. Chou, H. Lin, and M. Z. Hasan, *Nat. Commun.* **7**, 10556 (2016).

[36] T. T. Heikkilä and G. E. Volovik, Flat bands as a route to high-temperature superconductivity in graphite, in *Basic Physics of Functionalized Graphite*, edited by P. D. Esquinazi (Springer International Publishing, Cham, 2016), pp. 123–143.

[37] K. Mullen, B. Uchoa, and D. T. Glatzhofer, *Phys. Rev. Lett.* **115**, 026403 (2015).

[38] Y. Chen, Y. Xie, S. A. Yang, H. Pan, F. Zhang, M. L. Cohen, and S. Zhang, *Nano Lett.* **15**, 6974 (2015).

[39] L. S. Xie, L. M. Schoop, E. M. Seibel, Q. D. Gibson, W. Xie, and R. J. Cava, *APL Mater.* **3**, 083602 (2015).

[40] S. Ryu and Y. Hatsugai, *Phys. Rev. Lett.* **89**, 077002 (2002).

[41] N. B. Kopnin, T. T. Heikkilä, and G. E. Volovik, *Phys. Rev. B* **83**, 220503 (2011).

[42] P. W. Bridgman, *J. Am. Chem. Soc.* **36**, 1344 (1914).

[43] L. Li, Y. Yu, G. J. Ye, Q. Ge, X. Ou, H. Wu, D. Feng, X. H. Chen, and Y. Zhang, *Nat. Nanotechnol.* **9**, 372 (2014).

[44] X. Ling, H. Wang, S. Huang, F. Xia, and M. S. Dresselhaus, *Proc. Natl. Acad. Sci. USA* **112**, 4523 (2015).

[45] V. Tran, R. Sklaski, Y. Liang, and L. Yang, *Phys. Rev. B* **89**, 235319 (2014).

[46] A. N. Rudenko and M. I. Katsnelson, *Phys. Rev. B* **89**, 201408 (2014).

[47] A. S. Rodin, A. Carvalho, and A. H. Castro Neto, *Phys. Rev. Lett.* **112**, 176801 (2014).

[48] Y. Li, S. Yang, and J. Li, *J. Phys. Chem. C* **118**, 23970 (2014).

[49] X. Peng, Q. Wei, and A. Copple, *Phys. Rev. B* **90**, 085402 (2014).

[50] Z. J. Xiang, G. J. Ye, C. Shang, B. Lei, N. Z. Wang, K. S. Yang, D. Y. Liu, F. B. Meng, X. G. Luo, L. J. Zou, Z. Sun, Y. Zhang, and X. H. Chen, *Phys. Rev. Lett.* **115**, 186403 (2015).

[51] K. Akiba, A. Miyake, Y. Akahama, K. Matsubayashi, Y. Uwatoko, H. Arai, Y. Fuseya, and M. Tokunaga, *J. Phys. Soc. Jpn.* **84**, 073708 (2015).

[52] J. Kim, S. S. Baik, S. H. Ryu, Y. Sohn, S. Park, B.-G. Park, J. Denlinger, Y. Yi, H. J. Choi, and K. S. Kim, *Science* **349**, 723 (2015).

[53] J. P. Perdew, K. Burke, and M. Ernzerhof, *Phys. Rev. Lett.* **77**, 3865 (1996).

[54] P. E. Blöchl, *Phys. Rev. B* **50**, 17953 (1994).

[55] A. A. Mostofi, J. R. Yates, Y.-S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, *Comput. Phys. Commun.* **178**, 685 (2008).

[56] N. Marzari, A. A. Mostofi, J. R. Yates, I. Souza, and D. Vanderbilt, *Rev. Mod. Phys.* **84**, 1419 (2012).

[57] M. Okajima, S. Endo, Y. Akahama, and S.-i. Narita, *Jpn. J. Appl. Phys.* **23**, 15 (1984).

[58] R. Fei, V. Tran, and L. Yang, *Phys. Rev. B* **91**, 195319 (2015).

[59] P.-L. Gong, D.-Y. Liu, K.-S. Yan, Z.-J. Xiang, X. H. Chen, S.-Q. Shen, and L.-J. Zou, *Phys. Rev. B* **93**, 195434 (2016).

[60] R. Yu, X. L. Qi, A. Bernevig, Z. Fang, and X. Dai, *Phys. Rev. B* **84**, 075119 (2011).
