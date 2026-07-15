# Constructing the Fulde–Ferrell–Larkin–Ovchinnikov state in antiferromagnetic insulator CrOCl

Yifan Ding, $^{1,2, *}$ Jiadian He, $^{1,2, *}$ Shihao Zhang, $^{1,3, *}$ Huakun Zuo, $^{4, *}$ Pingfan Gu, $^{5}$ Jiliang Cai, $^{1,2}$ Xiaohui Zeng, $^{1,2}$ Pu Yan, $^{1}$ Kecheng Cao, $^{1}$ Kenji Watanabe, $^{6}$ Takashi Taniguchi, $^{7}$ Peng Dong, $^{1,2}$ Yiwen Zhang, $^{1,2}$ Yueshen Wu, $^{1,2}$ Xiang Zhou, $^{1,2}$ Jinghui Wang, $^{1,2, \dagger}$ Yulin Chen, $^{1,2,8}$ Yu Ye, $^{5, \ddagger}$ Jianpeng Liu, $^{1,2, \S}$ and Jun Li$^{1,2, \upharpoonleft}$

$^{1}$School of Physical Science and Technology, ShanghaiTech University, Shanghai 201210, China
$^{2}$ShanghaiTech Laboratory for Topological Physics, ShanghaiTech University, Shanghai 201210, China
$^{3}$School of Physics and Electronics, Hunan University, Changsha 410082, China
$^{4}$Wuhan National High Magnetic Field Center, Huazhong University of Science and Technology, Wuhan 430074, China
$^{5}$State Key Laboratory for Mesoscopic Physics, Nanooptoelectronics Frontier Center of the Ministry of Education, School of Physics, Peking University, Beijing 100871, China
$^{6}$Research Center for Functional Materials, National Institute for Materials Science, Tsukuba 305-0044, Japan
$^{7}$International Center for Materials Nanoarchitectonics, National Institute for Materials Science, Tsukuba 305-0044, Japan
$^{8}$Department of Physics, Clarendon Laboratory, University of Oxford, Oxford OX1 3PU, UK

(Dated: November 2, 2023)

Time reversal symmetry breaking in superconductors, resulting from external magnetic fields or spontaneous magnetization, often leads to unconventional superconducting properties. In this way, a conventional Fulde-Ferrell-Larkin-Ovchinnikov (FFLO) state, characterized by the Cooper pairs with nonzero total momentum, may be realized by the Zeeman effect caused from external magnetic fields. Here, we report the observation of superconductivity in a few-layer antiferromagnetic insulator CrOCl by utilizing superconducting proximity effect with NbSe₂ flakes. The superconductivity demonstrates a considerably weak gap of about 0.12 meV and the in-plane upper critical field reveals as behavior of the FFLO state at low temperature. Our first-principles calculations indicate that the proximitized superconductivity may exist in the CrOCl layer with Cr vacancies or line-defects. Moreover, the FFLO state could be induced by the inherent larger spin splitting in the CrOCl layer. Our findings not only demonstrate the fascinating interaction between superconductivity and magnetism, but also provide a possible path to construct FFLO state by intrinsic time reversal symmetry breaking and superconducting proximity effect.

## I. INTRODUCTION

Symmetry breaking, one of the core problems in condensed matter physics in recent decades, plays an important role in the development of unconventional superconductivity [1, 2]. For a conventional superconductor, spatial inversion and time reversal symmetries are preserved, and the wave function of Cooper pairs follows the traditional Bardeen-Cooper-Schrieffer (BCS) mechanism (Fig. 1a) [3]. On the one hand, for the case of time reversal symmetry breaking, the external magnetic field causes the Zeeman effect (Fig. 1b). In this case, the conventional FFLO state can be realized in a clean limit superconductor [4–8], which is often observed in the layered organic materials [9, 10], heavy-fermion superconductors [11–13], iron-based superconductors [14–16], transition metal dichalcogenides [17] and Sr₂RuO₄ [18]. There, the order parameter of the finite-momentum Cooper pairs can be periodic modulated in real space at low temperatures. On the other hand, for the case of spatial inversion symmetry breaking, the presence of Rashba-type or Ising-type spin-orbital coupling (SOC) in a superconductor can enhances the in-plane upper critical field beyond Pauli limit $B_p$=$1.86\ T_c$ (Fig. 1c) [19–21]. Besides, for the case of simultaneously breaking the spatial inversion and time reversal symmetries, Rashba-type or Ising-type FFLO state has also been studied (Fig. 1d) [22–25]. Therefore, it is commonly believed that time reversal symmetry breaking represents a crucial prerequisite for achieving unconventional superconductivity and a robust spin structure is necessary for the FFLO state.

Recently, a van der Waals (vdW) insulator CrOCl has attracted significant attention due to its novel antiferromagnetic (AFM) order [26–30]. The antiferromagnetism transition of CrOCl occurs at $T_N$=$13.5$ K as confirmed by magnetic susceptibility measurements, and such first-order transition is also accompanied by an orthorhombic to monoclinic lattice distortion [31]. In addition, the ground state of CrOCl is found as an unconventional spin-density wave (SDW) state along the short axis, namely, a stripy AFM order (Fig. 1e) [28]. Although CrOCl behaves as an insulator with a giant band gap [32], the structural distortion, magnetic and electronic ordering resemble the parent compound of iron-based superconductors. Therefore, it is highly possible to observe exotic superconducting state by inducing carrier doping into CrOCl. Despite significant efforts in chemical doping, CrOCl remains a challenging material due

---
* These authors contributed equally to this work.
† wangjh2@shanghaitech.edu.cn
‡ ye_yu@pku.edu.cn
§ liujp@shanghaitech.edu.cn
$\upharpoonleft$ lijun3@shanghaitech.edu.cn

to the large electronegativity of $Cl^-$ ions, which poses a considerable obstacle in terms of carrier trapping or exclusion [33]. Moreover, modifying the band structure of chlorides to achieve a conducting state through high pressure or electric field gating seems to be a difficult task [34]. Thus, we focus on the realization of superconductivity in CrOCl by the superconducting proximity effect.

Superconducting proximity effect has been widely studied in recent decades and shown great significance in the area of topological superconductivity [35]. When a superconducting material and a non-superconducting material come into contact with each other, the superconducting wave function can be induced from an even-parity $s$-wave superconductor to a non-superconducting state within a characterization coherence length $\xi_N$. Particularly, when the non-superconducting side behaves as magnetism, unconventional superconductivity or even odd-parity superconductivity may occur due to the spontaneous time reversal symmetry breaking properties [36-39]. Such interplay between the time reversal symmetry breaking and the spin-singlet superconductivity may induce novel quantum phenomena, including the spin-triplet superconductivity, the time reversal invariant topological superconductors, and Majorana fermions [36-41].

It is worth noting that by measuring the tunneling current through a vdW heterostructure of graphite/CrOCl/graphite, the magnetic transitions of few-layer CrOCl are similar to that of bulk [28]. Since the electron wave function can be correlated into CrOCl for more than 12 layers [28], it may be a promising way to penetrate Cooper pairs into CrOCl by superconducting proximity effect as well. In the magnetism/superconductivity heterostructure, the large spin splitting is inherent for magnetic system and the carrier doping is coming from the superconductor. For the case of CrOCl, the in-plane magnetic field will break the Kramers degeneracy between the energy bands of opposite spins in CrOCl layer, and induce remarkable spin splitting. In this way, the time reversal symmetry is destroyed and conventional FFLO state may emerge. The quasi-classical picture of FFLO state reveals that the large spin splitting and slight carrier doping is necessary for the emergence of FFLO state [8], where the electrons from two spin channel may form the Cooper pair with nonzero total momentum as shown in Fig.1(g).

In this work, we studied the proximity-effect-induced superconductivity with FFLO state in few-layer AFM insulator CrOCl by preparing the $CrOCl/NbSe_2$ vdW heterostructure. The device was in a specialized design to characterize transport properties of the insulator CrOCl directly. Quantum transport measurements revealed its two-dimensional (2D) superconducting properties of few-layer CrOCl. Moreover, the FFLO state was observed when the magnetic field was applied along in-plane direction. The differential resistance spectra clearly showed the proximity-effect-induced superconducting gap in the CrOCl layers. Combing the experimental results and first-principles calculations, we uncovered the origin of FFLO state in the few-layer AFM insulator CrOCl. Our work provides a possible scheme for constructing FFLO state and paves the way for exploring the interaction between antiferromagnetism and superconductivity.

## II. SUPERCONDUCTING CHARACTERIZATIONS OF DEVICE

The sample was designed as a vdW heterostructure device of $BN/NbSe_2/CrOCl$ as shown in the optical image in Fig. 2(a), and the layer directly in contact with the electrode was CrOCl. First of all, Ti/Au electrodes were embedded into the $SiO_2/Si$ substrates as illustrated in Fig. 2(b) and the cross-sectional view is shown in Fig. 2(c). In this way, the CrOCl and $NbSe_2$ layers can be stacked onto a flat substrate to avoid the cracking problem which often exists at the edge steps of the electrodes in a conventional method. Otherwise, the problem of shortage cannot be circumvented easily in monolayer CrOCl, as introduced in the Supplementary Information. More importantly, the monolayer CrOCl can be well restricted from atmosphere linking through the edge steps. In this vdW heterostructure device, the interfaces between Ti/Au electrodes, CrOCl, $NbSe_2$, and $h$-BN play a key role on the electrical transport properties. In Fig. 2(d) and 2(e), the scanning transmission electron microscopy (STEM) and the energy dispersive x-ray reveal the high quality interfaces of Au-CrOCl, CrOCl-$NbSe_2$, and also $NbSe_2$-BN, for which the interfaces are in good vdW contact, and any bubble or degradation have been eliminated. Particularly, when we enlarge the interface region for $CrOCl/NbSe_2$ (see Fig. 2(f)), the atomic layers of both CrOCl and $NbSe_2$ can be well identified, and the as-studied CrOCl consists of three atomic layers. Thus, within the specifically structured device, the abstracted circuit can be demonstrated as shown in Fig. S7, where the current flows through both CrOCl and $NbSe_2$. Since the interface between the insulating CrOCl and the metallic $NbSe_2$ behaves as a Schottky barrier, the contact resistance $R_c$ should be considerably large. Furthermore, as mentioned above, although CrOCl exhibits large resistance as an insulator especially at low temperature, few layers of CrOCl can exhibit good electrical conductivity properties via charge or Cooper pair transfer [28].

Fig. 3(a) gives the temperature dependence of normalized resistance for CrOCl with different thicknesses of one and four unit cells (UCs), and the superconductivity of intrinsic $NbSe_2$ is also measured as illustrated in Fig. 3(a). The critical temperature $(T_c)$ of the monolayer-$CrOCl/NbSe_2$ is comparable with that of the intrinsic $NbSe_2$. While as the thickness of CrOCl is up to 4 UCs, the $R$-$T$ curve demonstrates an obvious insulating behavior. The thickness of $NbSe_2$ flake in our experiments is about 15 nm ($\sim$ 22 UCs) as confirmed from the TEM measurements or atomic force microscopy, and the temperature dependence of $NbSe_2$'s resistance behaves as a bulk crystal as well studied in previous work [42]. Therefore, the superconducting transition in the CrOCl layer

should be correlated to the $NbSe_2$ flake based on the charge transfer and superconducting proximity effects.

Basically, the superconducting wave function from $NbSe_2$ reveals a $s$-wave pairing symmetry, in which the paired electrons carry the opposite spins, resulting in a so-called singlet Cooper pairs. When the superconductor is coupled with a normal metal, a supercurrent can flow into the metal within a distance less than a coherence length $\xi_N = \sqrt{\hbar D/k_B T}$, where $D$ is the diffusion coefficient, $\hbar$ is the Planck's constant, and $k_B$ is the Boltzmann's constant [43]. Normally, the $\xi_N$ can be up to even tens of nanometers. For a magnetic material, however, the superconducting coherence length in magnetic state ($\xi_M$) turns to be $\xi_M = \sqrt{\hbar D/k_B T_M}$, where $T_M$ is the magnetic transition temperature. As a result, the $\xi_M$ is dramatically small as about 1 nm even less for a strongly coupling ferromagnetic state, and the superconducting wave function decays exponentially $\Delta \sim \exp(D_M/\xi_M)$ [43]. The major reason is that the spin polarization in the magnetic materials will easily destroy singlet Cooper pairs. Nevertheless, the superconducting coherence length of AFM state is between that of normal metals and ferromagnetic materials. For the AFM CrOCl in the present case, the diffusive penetration depth seems likely to be about 2.7 nm (3 UCs). In addition, the superconducting current flowing through the CrOCl between two $NbSe_2$ layers can be present at 6 UCs, that is, the critical thickness of Josephson coupling is about 6 UCs as provided in the Supplementary Information Fig. S11. Therefore, we can basically conclude that the diffusive penetration depth of CrOCl is about 3 UCs as $\sim$2.7 nm, in which such proximity-effect-induced superconductivity should indicate low-dimensional nature.

To investigate the possible two-dimensional superconductivity, we then studied the angular dependence of upper critical fields ($H_{c2}$) in monolayer-CrOCl/NbSe$_2$ as shown in Fig.3(b). The $H_{c2}$ along the $ab$-plane ($H_{c2}^{ab}$ $\sim$6 T at 5.5 K) is dramatically larger than that of $c$-axis $H_{c2}^{c}$ ($\sim$0.2 T at 5.5 K). And particularly, the angular dependence of $H_{c2}$ around $ab$-plane ($\phi$$=$$90^\circ$) reveals as a 2D Tinkham model rather than the 3D anisotropic Ginzburg-Landau (GL) model, indicating that the proximity-induced superconductivity behaves as a 2D superconductor, being well consistent with field-effected $MoS_2$ [44, 45], $1T_d$-MoTe$_2$ [46], and heterointerface of $NbSe_2$ and $CrCl_3$ [47]. In contrast, the angular dependence of $H_{c2}$ in $NbSe_2$ obeys the 3D anisotropic Ginzburg-Landau model.

We also studied the magnetoresistance of monolayer-CrOCl/NbSe$_2$ along out-of-plane and in-plane field. When the magnetic field is applied along out-of-plane direction (see Fig. 3(c) and 3(d)), the proximity-induced superconductivity can be suppressed by a considerably weak magnetic field as $\sim$ 0.2 T at 2 K which corresponds to the $H_{c2}^{zero}$, and it is far more less than that of intrinsic $NbSe_2$ ($\sim$ 2 T at 2 K). However, when an in-plane magnetic field is applied (see Fig. 3(e)), both proximity-induced superconductivity of CrOCl and intrinsic superconductivity of $NbSe_2$ indicate a strong diamagnetism, for which we applied pulsed high magnetic fields up to 30 T to evaluate the $H_{c2}$ as given in Fig. S9. Particularly, the $H_{c2}^{ab}$ of monolayer CrOCl is large as $\sim$ 18.23 T at 1.6 K, which is even beyond the Pauli paramagnetic limit ($H_{c2}^p=13.7$ T), and the $H_{c2}^{ab}$ shows an obvious upturn profile at the low temperature regions, resulting in a kink at 3.5 K. Such temperature dependence behavior of $H_{c2}^{ab}$ is a hallmark of FFLO state, which is different from the Ginzburg-Landau formula for the conventional superconductors [17, 20, 48]. In this FFLO state, the observed coherence length ($\xi$) can be estimated to be about 2 nm from the $H_{c2}$ results based on the 2D Tinkham's model. Thus, this small coherence length contributes the formation of FFLO state [8].

Although strong SOC in few-layer $NbSe_2$ or interface from SOC-like monolayer-MoS$_2$/NbSe$_2$ could also induce the 2D Ising superconductivity transition [42, 49, 50], the $NbSe_2$ layer in our present study is up to 22 UCs, which should play as a bulk crystal as well studied in previous work [42]. For comparing, we also studied the temperature dependence of $H_{c2}^{ab}$ of the 22-UCs $NbSe_2$ as given in Fig. 3(f). Although the value of $H_{c2}^{ab}$ is comparable to that of CrOCl, the low temperatures upturn phenomenon is absent, but obeys a 3D superconductivity as the Wethamer-Helfand-Hohenberg (WHH) model, where
$$
H_{c2}^{ab}(0)=-0.697T_c(\frac{dH_{c2}^{ab}(T)}{dT})_{T\sim T_c}.
$$

## III. DIFFERENTIAL RESISTANCE SPECTRA

We further studied differential resistance ($dV/dI$) for the monolayer-CrOCl/NbSe$_2$ at various temperatures and magnetic fields as shown in Fig. 4. For the $dV/dI$ spectrum at 2 K, a pair of major peaks are observed at $V_0=1.16$ mV which can basically considered as the superconducting gap of $NbSe_2$ ($\Delta_0$), and the gap gradually disappears above 6.3 K. Interestingly, the differential resistance has not yet reach to zero, but drops to completely zero at a considerably low $V_1=0.12$ mV, indicating a subgap ($\Delta_1$) in the heterostructure. Fig.4(b) shows the temperature dependence of both gaps as estimated from the peaks in Fig. 4(a). Obviously, the temperature dependence of $\Delta_0$ obeys a typical $s$-wave superconductivity for intrinsic $NbSe_2$ based on the BCS model. For the temperature dependence of subgap, however, it is less than those of $NbSe_2$ for one order of magnitude, and vanishes at about 5.5 K which is less than the $T_c$ of $NbSe_2$ as well. The subgap should correspond to the proximity-induced superconducting gap as discussed above, which has also been reported in previous studies [51, 52].

As applying magnetic fields, both $\Delta_0$ and $\Delta_1$ are enhanced by fields below 0.2 T as shown in Fig. 4(c) and 4(d). Surprisingly, when the field is above 0.2 T, the subgap is completely suppressed, but the $\Delta_0$ is gradually restricted by the magnetic field. The anomalous enhancement of superconductivity is probably owing to the coupling between CrOCl and $NbSe_2$. Thus, we further investigate the subgap under low-magnetic fields from -0.2 to 0.2 T as shown in the $dV/dI$-$V$ spectra in Fig.4(e).

In the presence of low magnetic fields, the subgap exhibits a notable dependence on such fields, which may be contributed by field polarization of local magnetic moments. Under a small external magnetic field, the exchange-scattering time $\tau_B \sim \mu/2\pi J^2$ ($\mu$ is chemical potential) is reduced because the exchange parameter $J$ is enhanced which weakens the impurity scattering and increases the subgap [53]. Furthermore, the application of a magnetic field leads to a broadening of the subgap rather than a direct suppression.

Based on these results, we can basically conclude that the existence of proximity-effect-induced superconductivity within monolayer CrOCl. A direct argument on the induced superconductivity is the signal from tunneling junction as described in Fig. S7. However, once the supercurrent from tunneling junction dominates the measurement, one can observe that the superconductivity should be related to the intrinsic NbSe₂ completely, because the supercurrent will flow cross the junction and NbSe₂ layer, rather than the CrOCl layer. In this case, we can only observe a large superconducting gap related to the intrinsic NbSe₂, and the considerably small subgap should vanish (see Fig. S6). On the other hand, once a current electrode is connected to NbSe₂ directly, the supercurrent will just flow through NbSe₂ as well. As a result, the critical current and $dV/dI$-$V$ spectra are consistent with the intrinsic properties of NbSe₂ (see Fig. S6). Actually, we have studied more than 100 samples for the CrOCl/NbSe₂ heterostructure, among which the subgap does not always exist owing to this shortage or interface problem caused by the burrs at the electrode as introduced in the Supplementary Information. After all, the CrOCl crystals are in atomic layers, all these layers should be extremely sensitive to the substrate.

## IV. THE ORIGIN OF PROXIMITIZED SUPERCONDUCTIVITY

To understand the superconducting proximity effect in the CrOCl/NbSe₂ heterostructure, we carried out first-principles calculations with the slab model. Compared to the vacuum level, the Fermi level of NbSe₂ layers is located at the $-5.5\,\text{eV}$ , which is lying in the gap of CrOCl monolayer. Thus, only the strain or defect may tune the electronic structure of CrOCl to achieve the overlap between CrOCl's energy bands and NbSe₂'s conducting bands. Our calculations reveal that it is very difficult to achieve proximity-effect-induced superconductivity by in-plane strain within $\pm5\%$ magnitude. So we focus on the defect's influence about the electronic structure of the CrOCl. We note that there are two possible types of defect in the CrOCl, including Cl vacancy and Cr vacancy, and the first-principles results are present in the Fig.5 and Fig.S12. It indicates that the Cl vacancy will induce two localized energy bands as shown in the Fig.S12. These in-gap defect states have been observed in the previous experiments [54], which is indeed close to the conducting bands of NbSe₂. But the possible proximitized superconductivity based on the localized Cl vacancy is difficult to be detected in the experiments. As for the Cr vacancy, this type of defect has been reported in the similar CrSBr system [55]. Our calculated electronic bands as shown in the Fig.5 reveal that the highest valence bands of CrOCl are tuned to the Fermi level of NbSe₂ due to two Cr vacancies. The case of Cr-vacancy line-defect has the similar electronic phenomenon. In summary, the Cr vacancy defect can make the CrOCl's electron close to the Fermi surface of NbSe₂ to realize the proximitized superconductivity.

## V. CONCLUSION

In this paper, by constructing the breaking of time reversal symmetry in magnetic insulator and s-wave superconductor CrOCl/NbSe₂ device, we have observed the superconductivity through the proximity effect. Multiple superconducting gaps have been found below the transition temperature of NbSe₂. Moreover, the unconventional dependence of temperature and in-plane magnetic field in induced superconductivity is also studied. The in-plane magnetic field breaks the Kramers degeneracy and FFLO state was observed which came from the spin splitting. First-principles calculations systematically illustrated the origin of proximitized superconductivity. Our results reveal the proximity-effect-induced superconductivity with FFLO state in 2D van der Waals heterostructures and shed lights on the fascinating interaction between superconductivity and magnetism.

## VI. METHODS

**Crystal Synthesis.** The CrOCl crystals were synthesized by a solid growth technique as introduced in previous paper[28]. A mixture of powdered CrCl₃ and Cr₂O₃ with a molar ratio of 1:1 and a total mass of 1.5 g were sealed in an evacuated quartz ampule. The ampule was then placed in a two-zone furnace, where the source and sink temperatures for the growth were set to 940 °C and 800 °C, respectively, and kept for two weeks. Subsequently, the furnace was slowly cooled to room temperature, and high-quality CrOCl crystals were obtained. The single crystals were also ground and studied by a powder XRD method, and the results is well consistent with previous work [28].

**Device Fabrication.** The vdW heterostructure devices were fabricated using the dry transfer technique in a vacuum condition. Thin pieces of $h$-BN, NbSe₂ and few-layers CrOCl were exfoliated from high-quality single crystals of $h$-BN, NbSe₂ and CrOCl, respectively. The NbSe₂ and CrOCl flakes were then picked up by polydimethylsiloxane (PDMS)/polyvinyl alcohol (PVA) polymer stacks at 85 °C, transferred and aligned on the substrates in order. The $h$-BN flake was covered on the top of the heterostructure to prevent any degradation. The circuit pattern was written onto the SiO₂/Si substrates

by Laser Direct-Write lithography system (Microwriter ML3) within standard lithography process. Next, the electrode patterns were etched by 25 nm using reaction ion etching system (RIE), 5 nm of Ti and 20 nm of Au were then grown by electron beam (E-beam) deposition technique.

Since CrOCl is the thin flake of few atomic layers, it is extremely sensitive to substrate surface quality. Es- pecially at side of the electrodes in which some burrs often exist during the lift-off technique as discussed in Supplementary Information Fig. S5, resulting in a short pass through the $NbSe_2$ directly. To avoid this seri- ous problem, we polished and totally cleaned the as- prepared Ti/Au electrodes. The atomic force microscope and transmission electron microscope analysis indicated that the electrodes are considerable flat, as seen in Sup- plementary Information Fig. S5 and Fig. S10, respec- tively.

STEM Characterization. The double Cs-corrected scanning transmission electron microscopy (STEM, Grand JEM-ARM300F) was applied to analysis the atomic structure, the microscopy was equipped with a cold field-emission gun and operated at the accelerat- ing voltage of 300 kV. We cut the device by a focused ion beam (FIB, Grand JIB-4700F) to explore the inter- faces from the cross-section view. Here the thickness of the thin specimens is around 50-100 nm. The energy- dispersive X-Ray spectroscopy (EDS) mapping was ap- plied for the element distribution study.

Density Functional Theory Calculations. We carried out first principles calculations within the frame- work of the generalized gradient approximation func- tional [56] of the density functional theory through em-ploying the Vienna ab initio simulation package (VASP)[57] with projector augmented wave method [58]. The DFT-D2 method of Grimme [59] is used to describe the interlayer interaction between CrOCl and $NbSe_2$ sub- strate.

## VII. ACKNOWLEDGEMENT

This research was supported in part by the Min- istry of Science and Technology (MOST) of China (No.2022YFA1603903), the National Natural Science Foun- dation of China (Grants No. 12004251, 12104302,12104303, 12304217), the Science and Technology Com- mission of Shanghai Municipality, the Shanghai Sailing Program (Grant No. 21YF1429200), the start-up fund- ing from ShanghaiTech University, and Beijing National Laboratory for Condensed Matter Physics, the Interdisci- plinary Program of Wuhan National High Magnetic Field Center (WHMFC202124). Growth of hexagonal boron nitride crystals was supported by the Elemental Strategy Initiative conducted by the MEXT, Japan, Grant Num- ber JPMXP0112101001, JSPS KAKENHI Grant Num- ber JP20H00354 and A3 Foresight by JSPS.

[1] X. Qi and S. Zhang, Topological insulators and super- conductors, Rev. Mod. Phys. 83, 1057 (2011).
[2] J. Hu, Iron-based superconductors as odd-parity super- conductors, Phys. Rev. X 3 (2013).
[3] M. Sigrist and K. Ueda, Phenomenological theory of un- conventional superconductivity, Rev. Mod. Phys. 63, 239(1991).
[4] P. Fulde and R. A. Ferrell, Superconductivity in a strong spin-exchange field, Phys. Rev. 135, A550 (1964).
[5] A. I. Larkin and Y. N. Ovchinnikov, Nonuniform state of superconductors, Sov. Phys. JETP 20, 762 (1965).
[6] L. G. Aslamazov, Influence of impurities on the existence of an inhomogeneous state in a ferromagnetic supercon- ductor, Sov. Phys. JETP 28, 773 (1969).
[7] S. Takada, Superconductivity in a molecular field. II:stability of Filde-Ferrel phase, Prog. Theor. Phys. 43,27 (1970).
[8] K. W. Song and A. E. Koshelev, Quantum FFLO statein clean layered superconductors, Phys. Rev. X 9, 021025(2019).
[9] H. Shimahara, Fulde-Ferrell state in quasi-two- dimensional superconductors, Phys. Rev. B Condens. Matter 50, 12760 (1994).
[10] J. Wosnitza, FFLO states in layered organic supercon- ductors, Ann. Phys. 530, 1700282 (2018).
[11] A. Bianchi, R. Movshovich, C. Capan, P. G. Pagliuso, and J. L. Sarrao, Possible Fulde-Ferrell-Larkin- Ovchinnikov superconducting state in $CeCoIn_{5}$ , Phys. Rev. Lett. 91, 187004 (2003).
[12] Y. Matsuda and H. Shimahara, Fulde-Ferrell- Larkin-Ovchinnikov state in heavy fermion super- conductors, J. Phys. Soc. Jpn. 76, 051005 (2007).
[13] S. Kittaka, Y. Kono, K. Tsunashima, D. Kimoto, M. Yokoyama, Y. Shimizu, T. Sakakibara, M. Yamashita, and K. Machida, Modulation vector of the Fulde-Ferrell- Larkin-Ovchinnikov state in $CeCoIn_{5}$ revealed by high resolution magnetostriction measurements, Phys. Rev. B107, L220505 (2023).
[14] C. W. Cho, J. H. Yang, N. F. Q. Yuan, J. Shen, T. Wolf, and R. Lortz, Thermodynamic evidence for the Fulde- Ferrell-Larkin-Ovchinnikov state in the $KFe_{2} As_{2}$ super conductor, Phys. Rev. Lett. 119, 217002 (2017).
[15] S. Kasahara, Y. Sato, S. Licciardello, M. Culo, S. Arseni- jevic, T. Ottenbros, T. Tominaga, J. Boker, I. Eremin, T. Shibauchi, J. Wosnitza, N. E. Hussey, and Y. Mat- suda, Evidence for an Fulde-Ferrell-Larkin-Ovchinnikov state with segmented vortices in the BCS-BEC-crossover superconductor FeSe, Phys. Rev. Lett. 124, 107001(2020).
[16] S. Kasahara, H. Suzuki, T. Machida, Y. Sato, Y. Ukai, H. Murayama, S. Suetsugu, Y. Kasahara, T. Shibauchi, T. Hanaguri, and Y. Matsuda, Quasiparticle nodal plane in the Fulde-Ferrell-Larkin-Ovchinnikov state of FeSe, Phys. Rev. Lett. 127, 257001 (2021).
[17] C. W. Cho, J. Lyu, C. Y. Ng, J. J. He, K. T. Lo, D. Cha- reev, T. A. Abdel-Baset, M. Abdel-Hafiez, and R. Lortz,

Evidence for the Fulde-Ferrell-Larkin-Ovchinnikov state in bulk NbS₂, Nat. Commun. 12, 3676 (2021).

[18] K. Kinjo, M. Manago, S. Kitagawa, Z. Q. Mao, S. Yonezawa, Y. Maeno, and K. Ishida, Superconducting spincticity evidencing the Fulde-Ferrell-Larkin- Ovchinnikov state in Sr₂RuO₄, Science 376, 397 (2022).

[19] M. Smidman, M. B. Salamon, H. Q. Yuan, and D. F. Agterberg, Superconductivity and spin-orbit coupling in non-centrosymmetric materials: a review, Rep. Prog. Phys. 80, 036501 (2017).

[20] J. Falson, Y. Xu, M. Liao, Y. Zang, K. Zhu, C. Wang, Z. Zhang, H. Liu, W. Duan, K. He, H. Liu, J. H. Smet, D. Zhang, and Q. K. Xue, Type-II Ising pairing in few-layer stanene, Science 367, 1454 (2020).

[21] H. Yi, L. H. Hu, Y. Wang, R. Xiao, J. Cai, D. R. Hickey, C. Dong, Y. F. Zhao, L. J. Zhou, R. Zhang, A. R. Richardella, N. Alem, J. A. Robinson, M. H. W. Chan, X. Xu, N. Samarth, C. X. Liu, and C. Z. Chang, Crossover from Ising- to Rashba-type superconductivity in epitaxial Bi₂Se₃/monolayer NbSe₂ heterostructures, Nat. Mater. 21, 1366 (2022).

[22] N. F. Q. Yuan and L. Fu, Topological metals and finite-momentum superconductors, Proc. Natl. Acad. Sci. USA 118, e2019063118 (2021).

[23] P. Wan, O. Zheliuk, N. F. Q. Yuan, X. Peng, L. Zhang, M. Liang, U. Zeitler, S. Wiedmann, N. E. Hussey, T. T. M. Palstra, and J. Ye, Orbital Fulde-Ferrell-Larkin- Ovchinnikov state in an Ising superconductor, Nature 619, 46 (2023).

[24] X. Zhang and F. Liu, Fulde-Ferrell-Larkin-Ovchinnikov pairing induced by a Weyl nodal line in an Ising superconductor with a high critical field, Phys. Rev. B 105, 024505 (2022).

[25] A. Akbari and P. Thalmeier, Fermi surface segmentation in the helical state of a Rashba superconductor, Phys. Rev. Research 4, 023096 (2022).

[26] A. N. Christensen, T. Johansson, and S. Quézel, Preparation and magnetic properties of CrOCl, Acta. Chem. Scand. Ser. A 28, 1171 (1975).

[27] T. Zhang, Y. Wang, H. Li, F. Zhong, J. Shi, M. Wu, Z. Sun, W. Shen, B. Wei, W. Hu, X. Liu, L. Huang, C. Hu, Z. Wang, C. Jiang, S. Yang, Q. M. Zhang, and Z. Qu, Magnetism and optical anisotropy in van der Waals antiferromagnetic insulator CrOCl, ACS Nano 13, 11353 (2019).

[28] P. Gu, Y. Sun, C. Wang, Y. Peng, Y. Zhu, X. Cheng, K. Yuan, C. Lyu, X. Liu, Q. Tan, Q. Zhang, L. Gu, Z. Wang, H. Wang, Z. Han, K. Watanabe, T. Taniguchi, J. Yang, J. Zhang, W. Ji, P. H. Tan, and Y. Ye, Magnetic phase transitions and magnetoelastic coupling in a two-dimensional stripy antiferromagnet, Nano. Lett. 22, 1233 (2022).

[29] Y. Wang, X. Gao, K. Yang, P. Gu, X. Lu, S. Zhang, Y. Gao, N. Ren, B. Dong, Y. Jiang, K. Watanabe, T. Taniguchi, J. Kang, W. Lou, J. Mao, J. Liu, Y. Ye, Z. Han, K. Chang, J. Zhang, and Z. Zhang, Quantum Hall phase in graphene engineered by interfacial charge coupling, Nat. Nanotechnol. 17, 1272 (2022).

[30] K. Yang, X. Gao, Y. Wang, T. Zhang, Y. Gao, X. Lu, S. Zhang, J. Liu, P. Gu, Z. Luo, R. Zheng, S. Cao, H. Wang, X. Sun, K. Watanabe, T. Taniguchi, X. Li, J. Zhang, X. Dai, J. H. Chen, Y. Ye, and Z. Han, Unconventional correlated insulator in CrOCl-interfaced Bernal bilayer graphene, Nat. Commun. 14, 2136 (2023).

[31] J. Angelkort, A. Wölfel, A. Schönleber, S. van Smaalen, and R. K. Kremer, Observation of strong magnetoelastic coupling in a first-order phase transition of CrOCl, Phys. Rev. B 80, 144416 (2009).

[32] S. W. Jang, D. H. Kiem, J. Lee, Y.-G. Kang, H. Yoon, and M. J. Han, Hund's physics and the magnetic ground state of CrOX(X=Cl,Br), Phys. Rev. Mater. 5 (2021).

[33] P. Lampen-Kelley, A. Banerjee, A. A. Aczel, H. B. Cao, M. B. Stone, C. A. Bridges, J. Q. Yan, S. E. Nagler, and D. Mandrus, Destabilization of magnetic order in a dilute Kitaev spin liquid candidate, Phys. Rev. Lett. 119, 237203 (2017).

[34] Y. Cui, J. Zheng, K. Ran, J. Wen, Z.-X. Liu, B. Liu, W. Guo, and W. Yu, High-pressure magnetization and NMR studies of α-RuCl₃, Phys. Rev. B 96, 205147 (2017).

[35] L. Fu and C. L. Kane, Superconducting proximity effect and Majorana fermions at the surface of a topological insulator, Phys. Rev. Lett. 100, 096407 (2008).

[36] R. S. Keizer, S. T. B. Goennenwein, T. M. Klapwijk, G. Miao, G. Xiao, and A. Gupta, A spin triplet supercurrent through the half-metallic ferromagnet CrO₂, Nature 439, 825 (2006).

[37] J. W. A. Robinson, J. D. S. Witt, and M. G. Blamire, Controlled injection of spin-triplet supercurrents into a strong ferromagnet, Science 329, 59 (2010).

[38] M. S. Anwar, S. R. Lee, R. Ishiguro, Y. Sugimoto, Y. Tano, S. J. Kang, Y. J. Shin, S. Yonezawa, D. Manske, H. Takayanagi, T. W. Noh, and Y. Maeno, Direct penetration of spin-triplet superconductivity into a ferromagnet in Au/SrRuO₃/Sr₂RuO₄ junctions, Nat. Commun. 7, 13220 (2016).

[39] R. Cai, Y. Yao, P. Lv, Y. Ma, W. Xing, B. Li, Y. Ji, H. Zhou, C. Shen, S. Jia, X. C. Xie, I. Žutić, Q.-F. Sun, and W. Han, Evidence for anisotropic spin-triplet Andreev reflection at the 2D van der Waals ferromagnet/superconductor interface, Nat. Commun. 12, 6725 (2021).

[40] C. W. J. Beenakker, Random-matrix theory of Majorana fermions and topological superconductors, Rev. Mod. Phys. 87, 1037 (2015).

[41] J.-P. Xu, C. Liu, M.-X. Wang, J. Ge, Z.-L. Liu, X. Yang, Y. Chen, Y. Liu, Z.-A. Xu, C.-L. Gao, D. Qian, F.-C. Zhang, and J.-F. Jia, Artificial topological superconductor by the proximity effect, Phys. Rev. Lett. 112, 217001 (2014).

[42] X. Xi, Z. Wang, W. Zhao, J.-H. Park, K. T. Law, H. Berger, L. Forró, J. Shan, and K. F. Mak, Ising pairing in superconducting NbSe₂ atomic layers, Nat. Phys. 12, 139 (2015).

[43] A. I. Buzdin, Proximity effects in superconductor-ferromagnet heterostructures, Rev. Mod. Phys. 77, 935 (2005).

[44] Y. Saito, Y. Kasahara, J. Ye, Y. Iwasa, and T. Nojima, Metallic ground state in an ion-gated two-dimensional superconductor, Science 350, 409 (2015).

[45] Y. Saito, Y. Nakamura, M. S. Bahramy, Y. Kohama, J. Ye, Y. Kasahara, Y. Nakagawa, M. Onga, M. Tokunaga, T. Nojima, Y. Yanase, and Y. Iwasa, Superconductivity protected by spin-valley locking in ion-gated MoS₂, Nat. Phys. 12, 144 (2015).

[46] J. Cui, P. Li, J. Zhou, W. Y. He, X. Huang, J. Yi, J. Fan, Z. Ji, X. Jing, F. Qu, Z. G. Cheng, C. Yang, L. Lu, K. Suenaga, J. Liu, K. T. Law, J. Lin, Z. Liu, and G. Liu, Transport evidence of asymmetric spin-orbit

coupling in few-layer superconducting $1T_d$-MoTe$_2$, Nat. Commun. 10, 2044 (2019).

[47] D. Jiang, T. Yuan, Y. Wu, X. Wei, G. Mu, Z. An, and W. Li, Strong in-plane magnetic field-induced reemergent superconductivity in the van der Waals heterointerface of NbSe$_2$ and CrCl$_3$, ACS Appl. Mater. Interfaces 12, 49252 (2020).

[48] T. Kotte, H. Kühne, J. A. Schlueter, G. Zwick- nagl, and J. Wosnitza, Orbital-induced crossover of the Fulde-Ferrell-Larkin-Ovchinnikov phase into Abrikosov- like states, Phys. Rev. B 106, L060503 (2022).

[49] E. Sohn, X. Xi, W. Y. He, S. Jiang, Z. Wang, K. Kang, J. H. Park, H. Berger, L. Forro, K. T. Law, J. Shan, and K. F. Mak, An unusual continuous paramagnetic- limited superconducting phase transition in 2D NbSe$_2$, Nat. Mater. 17, 504 (2018).

[50] P. Baidya, D. Sahani, H. K. Kundu, S. Kaur, P. Tiwari, V. Bagwe, J. Jesudasan, A. Narayan, P. Raychaudhuri, and A. Bid, Transition from three- to two-dimensional Ising superconductivity in few-layer NbSe$_2$ by proximity effect from van der Waals heterostacking, Phys. Rev. B 104 (2021).

[51] Q. Li, C. He, Y. Wang, E. Liu, M. Wang, Y. Wang, J. Zeng, Z. Ma, T. Cao, C. Yi, N. Wang, K. Watan- abe, T. Taniguchi, L. Shao, Y. Shi, X. Chen, S. J. Liang, Q. H. Wang, and F. Miao, Proximity-induced supercon- ductivity with subgap anomaly in type II Weyl semi- metal WTe$_2$, Nano. Lett. 18, 7962 (2018).

[52] P. Zareapour, A. Hayat, S. Y. Zhao, M. Kreshchuk, A. Jain, D. C. Kwok, N. Lee, S. W. Cheong, Z. Xu, A. Yang, G. D. Gu, S. Jia, R. J. Cava, and K. S. Burch, Proximity-induced high-temperature superconductivity in the topological insulators Bi$_2$Se$_3$ and Bi$_2$Te$_3$, Nat. Commun. 3, 1056 (2012).

[53] W.-Z. Xu, C.-G. Chu, Z.-C. Pan, J.-J. Chen, A.-Q. Wang, Z.-B. Tan, P.-F. Zhu, X.-G. Ye, D.-P. Yu, and Z.-M. Liao, Proximity-induced superconducting gap in the intrinsic magnetic topological insulator MnBi$_2$Te$_4$, Phys. Rev. B 105 (2022).

[54] S. Li, J. Zhang, Y. Li, K. Zhang, L. Zhu, W. Gao, J. Li, and N. Huo, Anti-ambipolar and polarization- resolved behavior in MoTe$_2$ channel sensitized with low- symmetric CrOCl, Appl. Phys. Lett. 122, 083503 (2023).

[55] J. Klein, T. Pham, J. D. Thomsen, J. B. Curtis, T. Den- neulin, M. Lorke, M. Florian, A. Steinhoff, R. A. Wis- cons, J. Luxa, Z. Sofer, F. Jahnke, P. Narang, and F. M. Ross, Control of structure and spin texture in the van der Waals layered magnet CrSBr, Nat. Commun. 13, 5420 (2022).

[56] J. P. Perdew, K. Burke, and M. Ernzerhof, Generalized gradient approximation made simple, Phys. Rev. Lett. 77, 3865 (1996).

[57] G. Kresse and J. Hafner, Ab initio molecular dynamics for liquid metals, Phys. Rev. B 47, 558 (1993).

[58] P. E. Blöchl, Projector augmented-wave method, Phys. Rev. B 50, 17953 (1994).

[59] S. Grimme, Semiempirical GGA-type density functional constructed with a long-range dispersion correction, J. Comput. Chem. 27, 1787 (2006).

![](./images/926901324413403624_1.jpg)

FIG. 1. Symmetry breaking and pairing states in superconductors. (a) A traditional BCS pairing without symmetry breaking. (b) A conventional FFLO state with time reversal symmetry breaking. (c) Rashba-type SOC or Ising-type SOC with spatial inversion symmetry breaking. (d) Unconventional FFLO state in Rashba-type SOC or Ising-type SOC with both breaking the spatial inversion and time reversal symmetries. (e) The stripy AFM order of CrOCl, leads to the intrinsic time reversal symmetry breaking. (f) Schematic of the pairing symmetry in a NbSe₂ flake. The properties of the NbSe₂ flake are close to that of bulk, which can be considered that the spatial inversion symmetry is preserved. (g) The simplified illustration of FFLO state formation in few-layer CrOCl, where the in-plane magnetic field splits the spin degeneracy at Γ point.

![](./images/926901324413403624_2.jpg)

FIG. 2. Structure of CrOCl/NbSe₂ device. (a) Optical image of the device. The electrodes can be connected in different configurations for current flowing and voltage measurements to compare the electrical properties of intrinsic NbSe₂ (V₀) and CrOCl/NbSe₂ (V). The CrOCl, NbSe₂, and h-BN flakes are labeled in white, blue, and orange dot lines, respectively. (b) Schematic image of the stacking order of h-BN, NbSe₂, and CrOCl flakes. Thus, the electrodes are attached to the CrOCl layer instead of NbSe₂. (c) Cross-sectional view of the CrOCl/NbSe₂ heterostructure. (d) Transmission electron microscopy (TEM) image of the cross-section of the heterostructure, and the corresponding elemental mapping of Cr by energy dispersive x-ray analysis. A few atomic layers of Cr distribution can be observed as the green dot concentration region. The scale bar is 20 nm. (e) The high-resolution TEM image of the heterostructure demonstrates the layered structure of CrOCl and NbSe₂ crystals, and (f) the enlarged view of the interface region. The white dash line reveals the interface between CrOCl and NbSe₂. The thickness of CrOCl is about 2.3 nm, which corresponds to 3 atomic layers.

![](./images/926901324413403624_3.jpg)

![](./images/926901324413403624_4.jpg)

![](./images/926901324413403624_5.jpg)

FIG. 3. Superconducting characterizations of CrOCl/NbSe₂. (a) Temperature dependence of resistance in CrOCl/NbSe₂, where CrOCl varies in different thickness at 1 UCs and 4 UCs. The inset shows the resistance ($R/R_{SK}$) in the range from 2 K to 8 K, where $T_c^{onset}$ marks the onset of superconducting transition of CrOCl. (b) The angular dependence of $H_{c2}$ with fields rotating along out-of-plane. Here $\phi$ demonstrates the angle between $H$ and $ab$-plane. The $H_{c2}$ is defined as the half of normal resistance. The $H_{c2}$-$\phi$ is fitted by both 2D Tinkham model (red) and 3D anisotropic Ginzburg-Landau model (blue), respectively. (c) Resistance of monolayer-CrOCl/NbSe₂ as a function of temperature for the out-of-plane magnetic fields, varying from 0 T to 4 T. (d) Color mapping of the out-of-plane magnetoresistance for the monolayer-CrOCl/NbSe₂. Here, the $H_{c2}$ is considerably larger than that of $H_{c2}^{zero}$, namely, the $H_{c2}$ at completely zero resistance corresponding to the proximity-induced superconductivity of monolayer CrOCl. (e) The in-plane magnetoresistance color mapping for the monolayer-CrOCl/NbSe₂. The $H_{c2}$ data points in black solid line are fitted obeying a superconductor in the FFLO state. (f) Color mapping of in-plane magnetoresistance for 22-UC NbSe₂. Black solid line demonstrates the Ginzburg-Landau fitting for the $H_{c2}$.

![](./images/926901324413403624_6.jpg)

FIG. 4. Differential resistance (dV/dI) spectra with respect to temperature and magnetic field. (a) The dV/dI spectra with temperature. Several main peaks emerge below the superconducting transition temperature of NbSe₂. (b) Dependence of superconducting gaps $\Delta_0$ and $\Delta_1$ with temperatures, extracted as the peak positions from the dV/dI curves. Here, $\Delta_0$ can be fitted by the BCS model as shown in the black dash line, and the $\Delta_0$ is about 1.16 meV which is consistent with the intrinsic gap of NbSe₂. (c) The dV/dI spectra with magnetic field from 0 to 3 T at 2 K. Several main peaks emerge similarly. (d) Dependence of superconducting gaps of $\Delta_0$ and $\Delta_1$ with magnetic fields, extracted as the peak positions from the dV/dI curves. Note that the $\Delta_1$ is undetectable with field up to 0.2 T. (e) The dV/dI spectra under low magnetic field from -0.2 to 0.2 T at 2 K. (f) The contour mapped dV/dI after subtracting the 2000 Oe magnetic field background.

![](./images/926901324413403624_7.jpg)

FIG. 5. The origin of proximitized superconductivity in CrOCl.(a) The top view of CrOCl/NbSe₂ heterostructure with two Cr vacancies remarked by circles. The brown, yellow, blue, red, and green balls represent Nb, Se, Cr, O, and Cl atoms, respectively. (b) The top view of CrOCl/NbSe₂ heterostructure with Cr vacancy line-defect. (c) The energy bands of CrOCl/NbSe₂ heterostructure with two Cr vacancies in the CrOCl layer. The removed Cr atoms carry opposite spins to keep the antiferromagnetism of CrOCl layer. (d) The energy bands of CrOCl/NbSe₂ heterostructure with Cr vacancy line-defect in the CrOCl layer.