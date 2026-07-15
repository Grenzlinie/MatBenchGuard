# Mott phase in a van der Waals transition-metal halide at single-layer limit
Lang Peng, $^{1}$ Jianzhou Zhao, $^{2}$ Min Cai, $^{1}$ Gui-Yuan Hua, $^{1}$ Zhen-Yu Liu, $^{1}$ Hui-Nan Xia, $^{1}$ Yuan Yuan, $^{1}$ Wen-Hao Zhang $\odot,^{1}$ Gang Xu, $^{1, *}$ Ling-Xiao Zhao, $^{1}$ Zeng-Wei Zhu, $^{1}$ Tao Xiang, $^{3}$ and Ying-Shuang Fu $\odot^{1, \dagger}$

$^{1}$School of Physics and Wuhan National High Magnetic Field Center, Huazhong University of Science and Technology, Wuhan 430074, China
$^{2}$Sichuan Co-Innovation Center for New Energetic Materials, Southwest University of Science and Technology, Mianyang 621010, China
$^{3}$Institute of Physics, Chinese Academy of Sciences, Beijing 100080, China

![](./images/812604905020719105_1.jpg)
(Received 15 July 2019; revised manuscript received 9 April 2020; accepted 8 May 2020; published 2 June 2020)

Two-dimensional materials offer opportunities for unravelling unprecedented ordered states at the single-layer limit. Among such ordered states, the Mott phase is rarely explored. Here we study the Mott phase in van der Waals chromium (II) iodide $(CrI_{2})$ films. High-quality $CrI_{2}$ films with an atomically flat surface and macro size are grown on graphitized 6H-SiC(0001) substrate by molecular beam epitaxy. By *in situ* low-temperature scanning tunneling microscopy and spectroscopy, we reveal that the film has a band gap as large as $\sim$3.2 eV, which is nearly thickness independent. Density functional plus dynamic mean-field theory calculations suggest that $CrI_{2}$ films may be a strong Mott insulator with a ferromagnetically ordered ground state. The Mott phase is corroborated by the spectral band splitting and spectral weight transfer at charge dopants that is consistent with the extended Hubbard model. Our study provides a platform for studying correlated electron states at the single-layer limit.

DOI: 10.1103/PhysRevResearch.2.023264

## I. INTRODUCTION
In low-dimensional electronic systems, correlations among electrons are enhanced due to the quantum confinement effect, which favors the formation of long-range collective ordered states [1,2] that are unprecedented according to the Mermin-Wagner theorem [3]. Recent advances in the studies of single layers of two-dimensional (2D) materials have shown success in the discovery of magnetic order [4,5], charge density waves [6,7], as well as superconductivity [8,9]. The long-range order in the single-layer limit has delivered surprising quantum behaviors that are distinct from their bulk counterpart, such as magnetic-field-enhanced magnetism [5], enhanced charge density wave order [7], and Ising superconductivity [8]. Moreover, the ordered states in 2D materials are readily accessible for manipulations with external means [10–12] such as electric field, optical stimuli, etc., which opens a new paradigm for their study and applications.

In Mott insulators, strong electron-electron Coulomb repulsion overwhelms the kinetic hopping energy, which induces gap opening in an otherwise metallic band [13,14]. The Mott physics not only constitutes an intriguing metal-insulator transition mechanism beyond conventional band theory but also is relevant to exotic physics of high-temperature superconductivity and colossal magnetoresistance. Particularly, the 2D Mott-Hubbard model is widely studied as the basis for generating high-$T_{c}$ superconductivity upon charge doping [15]. While the parent state of cuprate superconductors is a Mott insulator that is considered as 2D identity, there still exists interlayer coupling that prohibits an unambiguous attribution of the property from single layers [15]. In the monolayer limit, the carrier doping of Mott insulators, a crucial parameter for tuning the Coulomb energy, can be controlled with external electrical gating that is devoid of structural or chemical disorder. Moreover, in Mott systems with Jahn-Teller distortion, the Hubbard bands can split under the cooperative Coulomb repulsion [16]. The split Hubbard bands are constrained with orbital selections for optical excitation, which aids the development of strong excitons [17].

To these ends, the exploration of a monolayer Mott insulator with Jahn-Teller effect is highly desirable for in-depth controlled study of rich exotic correlated states and for building functional devices. Existing experimental single-layer Mott systems involve the flat band in magic-angle bilayer graphene [18], the surface reconstruction of Sn on Si(111) or Ge(111) [19–23], and single-layer 1T-NbSe$_2$ or 1T-TaSe$_2$ [24–27]. Interesting Mott physics are revealed with carrier doping via electric field [18] or substrate [20]. Meanwhile, those pioneering Mott systems bear a certain complexity, such as alternative explanations [28,29], other coexisting order [24,27], or essentially quasi-2D stabilized by the substrate [19–23]. In addition, nonlocal Coulomb interaction [30] is not explicitly addressed in those systems.

$CrI_{2}$, as a layered van der Waals crystal, has its Cr ion centered around a Jahn-Teller distorted idiom octahedron. The strong Coulomb energy in $d$ orbitals of Cr makes it a promising system for the realization of a single-layer Mott insulator with degeneracy-lifted Hubbard bands. While this crystal has been synthesized in bulk form, its thin-film layers

$^{*}$gangxu@hust.edu.cn
$^{\dagger}$yfu@hust.edu.cn

Published by the American Physical Society under the terms of the *Creative Commons Attribution 4.0 International* license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

---
2643-1564/2020/2(2)/023264(9)
023264-1
Published by the American Physical Society

![](./images/812604905020719105_2.jpg)

FIG. 1. Crystal structure of $CrI_2$ and its morphology. (a), (b) Top view (a) and side view (b) of the crystal structure of monolayer $CrI_2$. (c) Large-scale STM topographic image $(V_s=3.0\,\text{V},\,I_t=6\,\text{pA})$ of $CrI_2$ film. Line profile (inset) along the green line shows the monolayer step height. (d) STM image $(V_s=0.6\,\text{V},\,I_t=100\,\text{pA})$ showing atomic resolution of 1L $CrI_2$. The top layer of iodine atoms form an isosceles triangle lattice. (e) FFT image of (d). The yellow circles highlight the Bragg peaks of the iodine lattice. (f) STM image $(V_s=-3\,\text{V},\,I_t=10\,\text{pA})$ of a mirror twin boundary on the third layer $CrI_2$. The isosceles triangles marks the iodine atomic lattice directions of $CrI_2$ at the two domains.

have never been achieved so far. Here, we report the growth of $CrI_2$ films with macro size down to the monolayer limit and identify its Mott insulator phase with scanning tunneling spectroscopy (STS) and theoretical calculations, which features a thickness-independent large band gap, characteristic Hubbard band splitting from nonlocal Coulomb repulsion, and spectral weight transfer at charge dopants. We report an orbital-dependent Hubbard band splitting on a single charge defect.

## II. METHODS

The $CrI_2$ films were grown on a graphene-covered 6H-SiC(0001) (nitrogen-doped, $n$-type, $0.03\,\Omega/\text{cm}$ resistivity) substrate with molecular beam epitaxy. The detailed procedure of graphene preparation has been depicted in Ref. [31]. High-purity Cr (99.999%) was thermally evaporated onto the substrate from a homemade tantalum boat under iodine molecular atmosphere of $2\times10^{-6}$ Torr to form $CrI_2$ films at a growth rate of $\sim0.2\,\text{L/min}$. The iodine molecules (99.99%) were introduced directly through a fine leak valve with a tube extending adjacent to the substrate face. The substrate was maintained at about $250^\circ\text{C}$ during the film growth. The scanning tunneling microscopy (STM) measurements [32] were performed at 4.2 K if not specified exclusively. The STS were performed with a lock-in bias modulation of 14.14 mV (rms) at 829 Hz.

The density functional theory (DFT) calculations are carried out using the projector-augmented-wave method implemented in VASP [33,34] within the local density approximation (LDA) and LDA $+U$ functional [35,36]. Experimental crystal parameters are used to construct the freestanding single-layer $CrI_2$ with the vacuum space larger than $15\,\mathring{A}$, and a cutoff energy of 500 eV and $13\times13\times1\ k$ meshes are used in our DFT calculations. The DFT plus dynamical mean-field theory (DFT + DMFT) calculations are performed on the Cr $3d$ projected Wannier orbitals with the hybridization expansion version of the continuous-time quantum Monte Carlo (HYB-CTQMC) method as the impurity solver [37-39]. We use the analytical continuation method introduced by Haule [40] to extract the self-energy $\Sigma(\omega)$ on the real axis from the Matsubara self-energy $\Sigma(i\omega)$.

## III. GROWTH AND SPECTROSCOPY OF $CrI_2$ FILMS

$CrI_2$ is a polymorph of the celebrated ferromagnetic insulator $CrI_3$ [4]. It is a layered van der Waals crystal with monoclinic structure belonging to the C2/$m$ space group [41].

![](./images/812604905020719105_3.jpg)

FIG. 2. Tunneling spectra of CrI₂ films. (a), (b) Tunneling spectroscopy of 1L CrI₂ in linear (a) and logarithmic scale (b) of its conductance, respectively. The red arrows in (b) indicate the band edges. (c) Tunneling spectra of multilayer CrI₂ films from 2L to 6L in logarithmic scale of their conductance. (d) Energy gap of the CrI₂ with different film thicknesses measured from (b) and (c). Set point conditions: $V_s=2.0\,\text{V}$, $I_t=50\,\text{pA}$ for 1L; $V_s=1.25\,\text{V}$, $I_t=10\,\text{pA}$ for 2L and 3L; $V_s=1.4\,\text{V}$, $I_t=10\,\text{pA}$ for 4L; $V_s=1.4\,\text{V}$, $I_t=5\,\text{pA}$ for 5L; $V_s=1.55\,\text{V}$, $I_t=20\,\text{pA}$ for 6L.

Each layer consists of one chromium layer sandwiched by two iodine layers. The top iodine layer forms an isosceles triangle lattice with apex angle of $55^\circ$ [Figs. 1(a) and 1(b)]. The chromium atom is situated at the center of a distorted iodine octahedron. Figure 1(c) shows a typical STM topographic image of the as-grown thin film. The coverage of the film is about one monolayer (1L), and the step edges on the film are inherited from those of the substrate. There exist small residual areas of 2-L film, from which the monolayer height is measured as $\sim6.9\,\text{\AA}$ [Fig. 1(c), inset]. Further growth shows that the film adopts the layer-by-layer mode. Atomic resolution and associated fast Fourier transform [Fig. 1(e)] (FFT) of the film [Fig. 1(d)] reveal an isosceles triangular lattice with the in-plane lattice constants measured as $a_1=3.88\,\text{\AA}$, $a_2=4.23\,\text{\AA}$, and $a_3=4.18\,\text{\AA}$. There are six additional satellite peaks surrounding the center zone as well as each Bragg peak, which stem from a $6\times6$ reconstruction between the graphene/SiC(0001) interface and disappear in film surfaces of higher layers. Since the isosceles triangle lattice is close to a regular one, we have excluded the possibility of inaccuracies in STM topographic acquisition via imaging a twin boundary of the film, where the isosceles triangle lattices of the two domains express strict mirror symmetry to each other [Fig. 1(f)]. The measured in-plane lattice constants and the monolayer height unambiguously demonstrate the film is of CrI₂ instead of its polymorph CrI₃, which has a regular triangular lattice [4].

Next, we characterize the electronic properties of the films. Tunneling spectra, which are proportional to the local density of states, of the monolayer film display a large band gap and two prominent peaks at $-2.6$ and $1.23\,\text{eV}$, respectively [Fig. 2(a)]. The conductance intensity of the 1.23-eV peak

![](./images/812604905020719105_4.jpg)

FIG. 3. LDA and LDA $+ U$ calculations of monolayer CrI₂. (a) LDA-calculated band structures of single-layer CrI₂ in NM phase. (b) The calculated magnetic configuration of CrI₂. They are the top view of the NM phase, the side view the FM order, the side view of two collinear AFM configurations, AFM1 and AFM2, and the top view of the frustrated AFM orders, AFM3 and AFM4. (c) Band structures of single-layer CrI₂ in FM state calculated by LDA. (d) Calculated energy difference $\Delta E$ (left axis) and band gap of FM phase (right axis) vs $U$ by LDA $+ U$ method, where $\Delta E$ is defined $E - E_{\text{AFM4}}$, as demonstrated in the main text. (e) Band structure of CrI₂ in FM phase calculated by LDA $+ U$ method with $U = 12$ eV. In (c) and (e), the red (blue) bands denote the spin-up (spin-down) channel.

drops to zero density at higher energy, resulting in a narrow peak width of 0.9 eV. This implies a large electron mass of the band. Indeed, no standing wave patterns next to impurities or step edges are observed around the associated energy. From the logarithmic scale of the tunneling conductance [Fig. 2(b)], the band edges can be clearly resolved, giving a gap size of 3.2 eV. We have evaluated that the gap size is invariant against different tip sample separation, excluding the extrinsic influence of the tip-induced band bending effect on the tunneling spectra. For thicker films from the 2nd to the 6th layers, the gap size stays the same [Figs. 2(c) and 2(d)], demonstrating that the interlayer coupling is negligible. This resembles the Mott gap in monolayer Bi₂Sr₂CaCu₂O₈₊δ [42], whose Mott gap size is similar to its bulk. But it is distinct from many layered 2D semiconductors, whose band-gap size increases with decreasing film thicknesses due to the quantum confinement effect [43]. The measurements performed at 77 K show no difference in spectral shape and lattice parameters for the films compared to 4 K. The narrow peak width and the associated high peak intensity imply electrons in the bands may be subject to correlation effect.

### IV. CALCULATED BANDS OF MONOLAYER CrI₂

To understand the electronic structure of the films, we perform first-principles calculations for the freestanding single-layer CrI₂ based on LDA(+$U$) and DFT $+$ DMFT methods [44,45]. The spin-orbit coupling effect is negligible for the low-energy bands and thus has been excluded in all calculations. The nonmagnetic (NM) calculations without $U$ show that four $3d$ electrons of Cr occupy six nearly degenerated $t_{2g}$ orbitals, giving a metal state of NM CrI₂ [Fig. 3(a)]. This is obviously contradictory to the large gap observed experimentally. Subsequently, we mainly focus on the mag-

![](./images/812604905020719105_5.jpg)

FIG. 4. DFT + DMFT Calculations of monolayer CrI₂. (a) Density of states of the single-layer CrI₂ in FM (left) and PM (right) phase calculated by DFT + DMFT method with different $U$. (b) DFT + DMFT–calculated momentum-resolved spectra of single-layer CrI₂ with $U = 4.0$ eV in FM phase. (c) Projected density of states of CrI₂ in FM phase calculated by DFT+DFMT method with $U = 4$ eV, where the LHB($d_{z^2}$), LHB($d_{x^2-y^2}$), and UHBs are marked, and the spin-up and spin-down states are colored with orange and gray, respectively. (d) DFT + DMFT–calculated momentum-resolved spectral of single-layer CrI₂ with $U = 4.0$ eV in PM phase. We fix $J/U = 0.2$ in all calculations.

netic calculations, because the stable magnetic state usually accompanies the Cr-based compounds. Five magnetic structures [Fig. 3(b)] are considered in our calculations. When $U$ is not included, all the magnetic structures give a small insulating gap ($\sim$0.1 eV), and a frustrated antiferromagnetic (AFM) configuration, named AFM4 in Fig. 3(b), is the most stable. We plot the ferromagnetic (FM) band structures as an example in Fig. 3(c) to illustrate the electron occupation in the magnetic states. Namely, for each $Cr^{2+}$ ion, three spin-up $t_{2g}$ orbitals and one spin-up $e_g$ orbital are fully occupied, leaving the other spin-up $e_g$ orbital totally unoccupied with a well-separated gap of 0.1 eV due to the Jahn-Teller distortion. All five spin-down orbitals are empty and much higher in energy than the unoccupied spin-up $e_g$ orbital because of the large Hund's rule coupling in $Cr^{2+}$.

Because the Coulomb repulsion $U$ for the $3d$ electrons of the $Cr^{2+}$ is not treated enough, the LDA-calculated band gap is too small to compare with the experiments. To overcome this weakness, we carry out the LDA $+ U$ calculations and study the evolution of the total energy of the magnetic states and their band gaps with $U$. The ground state changes from the AFM4 to the FM phase when $U$ is larger than 5 eV [Fig. 3(d)]. As the band gaps for all five magnetic phases are nearly the same size, we plot only the results of the FM phase in Fig. 3(d). Remarkably, a nominal $U$ of 12 eV is needed to open an experimentally comparable gap of 3.18 eV, whose band structures are shown in Fig. 3(e), indicating that the large band gap of CrI₂ has a Mott origin. Similar calculations on bulk CrI₂ deliver identical results as the monolayer. This demonstrates that the interlayer coupling is negligible, which is consistent with the experiment. However, such $U$ is abnormally large for Cr compounds [46,47]. One possible reason is that the effective $U$ added to the correlated electrons in the LDA $+ U$ method could be severely screened by the other electrons [48,49].

To more reasonably describe the effective $U$, we performed DFT + DMFT calculations on the single-layer CrI₂. We mainly focus on its FM state, which has shown to be the ground state in the LDA $+ U$ ($U > 5$ eV) calculations. Its band gap increases rapidly with $U$ from 1 to 4 eV, as shown in the left panel of Fig. 4(a). A gap of $\sim$3 eV is obtained with $U = 4$ eV, which is a typical value for Cr compounds, demonstrating that the correlation effect in CrI₂ is reasonably captured. The corresponding momentum-resolved spectral [Fig. 4(b)] and projected density of states [Fig. 4(c)] show that the highest valence bands (HVBs) and the lowest conduction bands (LCBs) are both contributed by the spin-up $3d$ orbitals of $Cr^{2+}$ ions with $d_{z^2}$ and $d_{x^2-y^2}$ characters, namely, the lower Hubbard bands (LHBs). Thereafter, the HVBs and the LCBs are denoted as LHB($d_{z^2}$) and LHB($d_{x^2-y^2}$), respectively. The upper Hubbard bands (UHBs) are much higher in energy and are beyond the spectroscopic range of our measurement. Since $d_{z^2}$ is more localized compared to $d_{x^2-y^2}$, its effective Coulomb energy is larger. This renders that the energy

![](./images/812604905020719105_6.jpg)
![](./images/812604905020719105_7.jpg)
![](./images/812604905020719105_8.jpg)
![](./images/812604905020719105_9.jpg)
![](./images/812604905020719105_10.jpg)
![](./images/812604905020719105_11.jpg)
![](./images/812604905020719105_12.jpg)

FIG. 5. Morphology and tunneling spectra of defects. (a) STM image ($V_s = 1.75\,\text{V}$, $I_t = 100\,\text{pA}$) of a defect on the second layer of $\text{CrI}_2$. (b) Tunneling spectra measured at different distances relative to the defect, where the spectroscopic locations are indicated in (a). The spectra are offset vertically for clarity. Spectra set points: $V_s = 3.0\,\text{V}$, $I_t = 50\,\text{pA}$. (c) The spectral curves of (b) have been aligned to the right peak of LCB, corresponding to the $\text{LHB}(d_{x^2-y^2})$. The dashed lines mark the energy splitting for the different Hubbard bands. (d) Schematics showing the energy of Hubbard bands near the Fermi level from $d_{z^2}$ (green lines) and $d_{x^2-y^2}$ (blue lines) orbitals, respectively. At the $p$-type defect site, nearest-neighbor Coulomb interaction ($V$) induces satellite peaks with splitting energy $V$ below the Hubbard bands. The splitting energy for different orbitals are inequivalent. (e) Schematics showing the spectral weight transfer from the UHBs to the LHB ($d_{z^2}$). Note that the spectral weight of $\text{LHB}(d_{x^2-y^2})$ is reserved due to its unoccupied energy. The dotted (solid) curves represent the bands before (after) spectral weight transfer. The shaded orange (gray) color represents spin-up (spin-down) states. (f) Representative spectrum of the defect center, where the spectral weight of the LCBs and HVBs is obtained by fitting with several Gaussian peaks. (g) Relative spectral weight of HVBs for the spectra of (b) versus their spectroscopic locations to the defect center.

splitting between LHBs and UHBs, which is related to the on-site Coulomb energy, is larger for $d_{z^2}$ than that of the $d_{x^2-y^2}$ orbital. The distinct orbital characters of the $\text{CrI}_2$ bands are a result of the cooperative Coulomb repulsion and Jahn-Teller distortion of the $I^-$ octahedra, which is analogous to the perovskites $\text{KCrF}_3$ [50] and $\text{LaMnO}_3$ [51].

Finally, we also calculated the electronic structure of the paramagnetic (PM) phase for single-layer $\text{CrI}_2$ by the DFT + DMFT method. The calculated density of states [Fig. 4(a), right] and the momentum-resolved spectra [Fig. 4(d)] both show an insulating gap of $\sim 3\,\text{eV}$ with $U=4\,\text{eV}$. These demonstrate that a large gap already exists at 300 K, ruling out the possibility of Slater transition. For a Slater insulator, the insulating gap exists only in the magnetic phase, while their PM phase is metallic [52].

## V. EXPERIMENTAL EVIDENCE OF MOTT PHASE

The $\text{CrI}_2$ films have intrinsic defects that are particularly abundant on the monolayer and sparse on higher layers. To avoid influence from adjacent defects, we take the spectra of a single defect on the second-layer film [Fig. 5(a)]. Line spectra [Figs. 5(b) and 5(c)] show a rigid band shift towards higher energies when approaching the defect. This indicates that the defect acts as hole dopant. Intriguingly, there appear two sets of peaks for $\text{LHB}(d_{z^2})$ and $\text{LHB}(d_{x^2-y^2})$ at the defect center, whose intensities are strongly localized within $\sim 2$ atomic lattices. The band gap at the defect site becomes smaller by $\sim 0.37\,\text{eV}$. This behavior is reminiscent of the spectroscopic features for charge dopants in Mott insulators [53]. In low dimensions, reduced screening emphasizes

![](./images/812604905020719105_13.jpg)

FIG. 6. Tunneling spectra of Na cluster and Zn cluster on monolayer CrI₂ films. (a) Three representative $dI/dV$ spectra (top) and $I$-$V$ curves (bottom) taken at the different locations around the Na cluster, as indicated in the inset of the pseudo-three-dimensional image ($V_b=-3.0$ V, $I=10$ pA) by colored dots. The set point of the spectra is $V_b=-3.0$ V and $I=30$ pA. The red arrows mark the gap edges measured on the Na cluster. (b) Same as (a), except for a Zn cluster. Inset image conditions: $V_b=3.0$ V, $I=5$ pA. Spectra set point: $V_b=3.0$ V, $I=50$ pA.

the importance of nonlocal Coulomb interaction. This calls for the extended Hubbard model in which both the on-site Coulomb interaction $U$ and the nearest-neighbor Coulomb repulsion $V$ should be considered. In such cases, charge dopants invoke charged excitons accessible to electron tunneling spectroscopy [54], which induces satellite peaks below the Hubbard bands with splitting energy $V$ [55]. Moreover, since the Hubbard bands arise from multiorbitals in CrI₂ film, corresponding $V$ for the different orbitals are inequivalent [Fig. 5(d)]. From the spectral splitting in Fig. 5(c), values of $V$ are determined as 0.46 and 0.26 eV for $d_{z^2}$ and $d_{x^2-y^2}$ orbitals, respectively. Our study provides a probe for extracting the value of $V$ for each orbital directly from a single charge defect.

The charge defect can also induce spectral weight transfer from the Hubbard bands in Mott insulators [55], an effect which is more prominent with nonlocal Coulomb energy involved [56]. In the current system, spectral weight is expected to transfer from UHBs to LHB ($d_{z^2}$) at around the charge center [Fig. 5(e)]. Because the LHB ($d_{x^2-y^2}$) are unoccupied, spectral weight transfer to this state does not benefit the total energy. To examine this conjecture, we simply need to evaluate whether the spectral weight of the LHB ($d_{z^2}$) increases with the charge defects. For that, we first obtain the spectral weight of the LCBs and HVBs, i.e., the LHB ($d_{x^2-y^2}$) and LHB ($d_{z^2}$), respectively, by fitting them with several Gaussian peaks, as is exemplified in Fig. 5(f). Then, each spectroscopic curve in Fig. 5(b) is normalized according the spectral weight of the LCBs. The spectral weight of the HVBs for all the curves ($w_i$) is compared to that of the bare CrI₂ ($w_0$). As is shown in Fig. 5(g), the relative spectral weight of the HVBs for all the curves $(w_i - w_0)/w_0$ indeed increases around the defect. The spatial distribution of the spectral weight gain is only confined to $\sim4$ lattices. This observation conforms to the theoretical attribution of CrI₂ to the Mott insulator.

The Mott phase in CrI₂ is further examined by doping electrons, where Mott-gap reduction is expected due to locally decreased Coulomb repulsion by the charge dopants. Na and Zn atoms, which lack unfilled $d$ electrons and merely act as charge dopants, are deposited onto the CrI₂ surface at $\sim$30 K, forming clusters. The gap size on clusters of both species becomes significantly smaller and recovers right after leaving the clusters (Fig. 6). Moreover, the gap size decreases with increasing cluster size. This excludes the possibility of

a Coulomb blockade gap, whose gap size would show the opposite trend with cluster size.

## VI. CONCLUSION
In summary, $CrI_2$ films down to the single-layer limit are prepared in a layer-by-layer growth mode. The films have a large band gap of $\sim 3.2$ eV that is nearly independent of the film thickness. LDA $+U$ and DFT $+$ DMFT calculations suggest that the large band gap originates from a Mott phase with out-of-plane ferromagnetization. The correlated state in $CrI_2$ films reveals nonlocal Coulomb repulsions explicitly from the spectra splitting of the Hubbard bands and spectral weight transfer on single charged defects. The $CrI_2$ films envision in-depth further studies, including characterizing their magnetic properties, tuning their properties with external parameters such as electric gating, as well as developing functional devices. Moreover, the orbital character of the Hubbard bands implies constrained selection rules for optical absorption, which provides a candidate system for exploring intriguing physics such as dark excitons and possible half excitonic insulators [17].

## ACKNOWLEDGMENTS
We thank S. W. Wu and J. T. Lü for discussions. This work is funded by the National Key Research and Development Program of China (Grants No. 2017YFA0403501, No. 2018YFA0307000, and No. 2016YFA0401003) and the National Science Foundation of China (Grants No. 11522431, No. 11474112, No. 11774105, No. 11874022, and No. 21873033).

L.P., J.Z., and M.C. contributed equally to this work.

[1] P. Monceau, Electronic crystals: An experimental overview, Adv. Phys. 61, 325 (2012).

[2] P. C. Snijders and H. H. Colloquium, and Weitering: Electronic instabilities in self-assembled atom wires, Rev. Mod. Phys. 82, 307 (2010).

[3] N. D. Mermin and H. Wagner, Absence of Ferromagnetism or Antiferromagnetism in One- or Two-Dimensional Isotropic Heisenberg Models, Phys. Rev. Lett. 17, 1133 (1966).

[4] B. Huang, G. Clark, E. N. Moratalla, D. R. Klein, R. Cheng, K. L. Seyler, D. Zhong, E. Schmidgall, M. A. McGuire, D. H. Cobden et al., Layer-dependent ferromagnetism in a van der Waals crystal down to the monolayer limit, Nature (London) 546, 270 (2017).

[5] C. Gong, L. Li, Z. L. Li, H. W. Li, A. Stern, Y. Xia, T. Cao, W. Bao, C. Z. Wang, Y. Wang et al., Discovery of intrinsic ferromagnetism in two-dimensional van der Waals crystals, Nature (London) 546, 265 (2017).

[6] M. M. Ugeda, A. J. Bradley, Y. Zhang, S. Onishi, Y. Chen, W. Ruan, C. Ojeda-Aristizabal, H. Ryu, M. T. Edmonds, H.-Z. Tsai et al., Characterization of collective ground states in single-layer NbSe₂, Nat. Phys. 12, 92 (2016).

[7] X. X. Xi, L. Zhao, Z. F. Wang, H. Berger, L. Forró, J. Shan, and K. F. Mak, Strongly enhanced charge-density-wave order in monolayer NbSe₂, Nat. Nanotechnol. 10, 765 (2015).

[8] X. Xi, Z. F. Wang, W. W. Zhao, J.-H. Park, K. T. Law, H. Berger, L. Forró, J. Shan, and K. F. Mark, Ising pairing in superconducting NbSe₂ atomic layers, Nat. Phys. 12, 139 (2016).

[9] Q.-Y. Wang, Z. Li, W.-H. Zhang, Z.-C. Zhang, J.-S. Zhang, W. Li, H. Ding, Y.-B. Ou, P. Deng, K. Chang et al., Direct observation of high-temperature superconductivity in one-unit-cell FeSe films, Chin. Phys. Lett. 29, 037402 (2012).

[10] X. D. Xu, W. Yao, D. Xiao, and T. F. Heinz, Spin and pseudospins in layered transition metal dichalcogenides, Nat. Phys. 10, 343 (2014).

[11] C. Gong and X. Zhang, Two-dimensional magnetic crystals and emergent heterostructure devices, Science 363, eaav4450 (2018).

[12] Y. Saito, T. Nojima, and Y. Iwasa, Highly crystalline 2D superconductors, Nat. Rev. Mater. 2, 16094 (2016).

[13] M. Imada, A. Fujimori, and Y. Tokura, Metal-insulator transitions, Rev. Mod. Phys. 70, 1039 (1998).

[14] S. Y. Kim, M.-C. Lee, G. Han, M. Kratochvilova, S. Yun, S. JaeMoon, C. Sohn, J.-G. Park, C. Kim, and T. W. Noh, Spectroscopic studies on the metal-insulator transition mechanism in correlated materials, Adv. Mater. 30, 1704777 (2018).

[15] P. A. Lee, N. Nagaosa, and X. G. Wen, Doping a Mott insulator: Physics of high-temperature superconductivity, Rev. Mod. Phys. 78, 17 (2006).

[16] P. Fazekas, Lecture Notes on Electron Correlation and Magnetism (World Scientific Publishing, Singapore, 1999).

[17] Z. Jiang, Y. Li, W. Duan, and S. Zhang, Half-Excitonic Insulator: A Single-Spin Bose-Einstein Condensate, Phys. Rev. Lett. 122, 236402 (2019).

[18] Y Cao, V. Fatemi, A. Demir, S. Fang, S. L. Tomarken, J. Y. Luo, J. D. Sanchez-Yamagishi, K. Watanabe, T. Taniguchi, E. Kaxiras et al., Correlated insulator behavior at half-filling in magic-angle graphene superlattices, Nature (London) 556, 80 (2018).

[19] R. Cortés, A. Tejeda, J. Lobo, C. Didiot, B. Kierren, D. Malterre, E. G. Michel, and A. Mascaraque, Observation of a Mott Insulating Ground State for Sn/Ge(111) at Low Temperature, Phys. Rev. Lett. 96, 126103 (2006).

[20] S. Modesti, L. Petaccia, G. Ceballos, I. Vobornik, G. Panaccione, G. Rossi, L. Ottaviano, R. Larciprete, S. Lizzit, and A. Goldoni, Insulating Ground State of Sn/Si(111-$\sqrt{3} \times \sqrt{3}$) R30°, Phys. Rev. Lett. 98, 126401 (2007).

[21] G. Profeta and E. Tosatti, Triangular Mott-Hubbard Insulator Phases of Sn/Si(111) and Sn/Ge(111) Surfaces, Phys. Rev. Lett. 98, 086401 (2007).

[22] T. Hirahara, T. Komorida, Y. Gu, F. Nakamura, H. Idzuchi, H. Morikawa, and S. Hasegawa, Insulating conduction in Sn/Si(111): Possibility of a Mott insulating ground state and metallization/localization induced by carrier doping, Phys. Rev. B 80, 235419 (2009).

[23] F. Ming, S. Johnston, D. Mulugeta, T. S. Smith, P. Vilmercati, G. Lee, T. A. Maier, P. C. Snijders, and H. H. Weitering, Realization of a Hole-Doped Mott Insulator on a Triangular Silicon Lattice, Phys. Rev. Lett. 119, 266802 (2017).
023264-8

[24] Y. Nakata, K. Sugawara, R. Shimizu, Y. Okada, P. Han, T. Hitosugi, K. Ueno, T. Sato, and T. Takahashi, Monolayer 1T- NbSe₂ as a Mott Insulator, *NPG Asia Mater.* **8**, e321 (2016).

[25] M. Calandra, Phonon-Assisted Magnetic Mott-Insulating State in the Charge Density Wave Phase of Single-Layer 1T-NbSe₂, *Phys. Rev. Lett.* **121**, 026401 (2018).

[26] D. Pasquier and O. V. Yazyev, Charge density wave phase, Mottness, and ferromagnetism in monolayer 1T-NbSe₂, *Phys. Rev. B* **98**, 045114 (2018).

[27] Y. Chen, W. Ruan, M. Wu, S. Tang, H. Ryu, H.-Z. Tsai, R. Lee, S. Kahn, F. Liou, C. Jia *et al.*, Strong correlations and orbital texture in single-layer 1T-TaSe₂, *Nat. Phys.* **16**, 218 (2020).

[28] B. Padhi, C. Setty, and P. W. Phillips, Doped twisted bilayer graphene near magic angles: Proximity to Wigner crystalliza- tion not Mott insulation, *Nano Lett.* **18**, 6175 (2018).

[29] H. Isobe, Noah F.Q. Yuan, and L. Fu, Unconventional Super- conductivity and Density Waves in Twisted Bilayer Graphene, *Phys. Rev. X* **8**, 041041 (2018).

[30] F. Adler, S. Rachel, M. Laubach, J. Maklar, A. Fleszar, J. Schafer, and R. Claessen, Correlation-Driven Charge Order in a Frustrated Two-Dimensional Atom Lattice, *Phys. Rev. Lett.* **123**, 086401 (2019).

[31] X. Yang, J.-J. Xian, G. Li, N. Nagaosa, W.-H. Zhang, L. Qin, Z.-M. Zhang, J.-T. Lü, and Y.-S. Fu, Possible phason-polaron effect on purely one-dimensional charge order of Mo₆Se₆ nanowires, arXiv:2002.12638.

[32] L. Peng, Y. Yuan, G. Li, X. Yang, J.-J. Xian, C.-J. Yi, Y.-G. Shi, and Y.-S. Fu, Observation of topological states residing at step edges of WTe₂, *Nat. Commun.* **8**, 659 (2017).

[33] G. Kresse and J. Furthmüller, Efficiency of ab-initio total en- ergy calculations for metals and semiconductors using a plane- wave basis set, *Comput. Mater. Sci.* **6**, 15 (1996).

[34] G. Kresse and J. Furthmüller, Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set, *Phys. Rev. B* **54**, 11169 (1996).

[35] V. I. Anisimov, J. Zaanen, and O. K. Andersen, Band theory and Mott insulators: Hubbard U instead of Stoner I, *Phys. Rev. B* **44**, 943 (1991).

[36] S. L. Dudarev, G. A. Botton, S. Y. Savrasov, C. J. Humphreys, and A. P. Sutton, Electron-energy-loss spectra and the structural stability of nickel oxide: An LSDA+U study, *Phys. Rev. B* **57**, 1505 (1998).

[37] E. Gull, A. J. Millis, A. I. Lichtenstein, A. N. Rubtsov, M. Troyer, and P. Werner, Continuous-time Monte Carlo meth- ods for quantum impurity models, *Rev. Mod. Phys.* **83**, 349 (2011).

[38] L. Huang, Y. Wang, Z. Y. Meng, L. Du, P. Werner, and X. Dai, iQIST: An open source continuous-time quantum Monte Carlo impurity solver toolkit, *Comp. Phys. Commun.* **195**, 140 (2015).

[39] A. A. Mostofi, J. R. Yates, G. Pizzi, Y. S. Lee, I. Souza, D. Vanderbilt, and N. Marzari, An updated version of Wannier90: A tool for obtaining maximally-localised Wannier functions, *Comput. Phys. Commun.* **185**, 2309 (2014).

[40] K. Haule, C. H. Yee, and K. Kim, Dynamical mean-field theory within the full-potential methods: Electronic structure of CeIrIn₅, CeCoIn₅, and CeRhIn₅, *Phys. Rev. B* **81**, 195107 (2010).

[41] J. W. Tracy, N. W. Gregory, J. M. Stewart, and E. C. Lingafelter, The crystal structure of chromium(II) iodide, *Acta Cryst.* **15**, 460 (1962).

[42] Y. Yu, L. G. Ma, P. Cai, R. D. Zhong, C. Ye, J. Shen, G. D. Gu, X. H. Chen, and Y. B. Zhang, High-temperature superconduc- tivity in monolayer Bi₂Sr₂CaCu₂O₈+δ, *Nature (London)* **575**, 156 (2019).

[43] F. Bussolotti, H. Kawai, Z. E. Ooi, V. Chellappan, D. Thian, A. L. C. Pang, and K. E. J. Goh, Roadmap on finding chiral valleys: Screening 2D materials for valleytronics, *Nano Futures* **2**, 032001 (2018).

[44] G. Kotliar, S. Y. Savrasov, K. Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti, Electronic structure calculations with dynamical mean-field theory, *Rev. Mod. Phys.* **78**, 865 (2006).

[45] A. Georges, G. Kotliar, W. Krauth, and M. J. Rozenberg, Dynamical mean-field theory of strongly correlated fermion systems and the limit of infinite dimensions, *Rev. Mod. Phys.* **68**, 13 (1996).

[46] N. J. Mosey and E. A. Carter, *Ab initio* evaluation of Coulomb and exchange parameters for DFT+ U calculations, *Phys. Rev. B* **76**, 155123 (2007).

[47] F. Lebreau, M. M. Islam, B. Diawara, and P. Marcus, Structural, magnetic, electronic, defect, and diffusion properties of Cr₂O₃: A DFT+ U study, J. *Phys. Chem. C* **11818133** (2014).

[48] E. Şaşıoğlu, C. Friedrich, and S. Blügel, Effective Coulomb interaction in transition metals from constrained random-phase approximation, *Phys. Rev. B* **83**, 121101(R) (2011).

[49] L. Vaugier, H. Jiang, and S. Biermann, Hubbard U and Hund exchange J in transition metal oxides: Screening versus local- ization trends from constrained random phase approximation, *Phys. Rev. B* **86**, 165105 (2012).

[50] L. V. Pourovskii, Two-site fluctuations and multipolar intersite exchange interactions in strongly correlated systems, *Phys. Rev. B* **94**, 115117 (2016).

[51] E. Pavarini and E. Koch, Origin of Jahn-Teller Distortion and Orbital Order in LaMnO₃, *Phys. Rev. Lett.* **104**, 086402 (2010).

[52] Q. Cui, J.-G. Cheng, W. Fan, A. E. Taylor, S. Calder, M. A. McGuire, J.-Q. Yan, D. Meyers, X. Li, Y. Q. Cai, Y. Y. Jiao, Y. Choi, D. Haskel, H. Gotou, Y. Uwatoko, J. Chakhalian, A. D. Christianson, S. Yunoki, J. B. Goodenough, and J.-S. Zhou, Slater Insulator in Iridate Perovskites with Strong Spin-Orbit Coupling, *Phys. Rev. Lett.* **117**, 176603 (2016).

[53] P. Phillips, Colloquium: Identifying the propagating charge modes in doped Mott insulators, *Rev. Mod. Phys.* **82**, 1719 (2010).

[54] J. V. D. Brink, R. Eder, and G. A. Sawatzky, Charged excitons in doped Hubbard model systems, *Europhys. Lett.* **37**, 471 (1997).

[55] I. Altfeder and D. M. Chen, Anisotropic Charge Ordering on the Gallium Surface, *Phys. Rev. Lett.* **101**, 136405 (2008).

[56] C. Ye, P. Cai, R. Z. Yu, X. D. Zhou, W. Ruan, Q. Q. Liu, C. Q. Jin, and Y. Y. Wang, Visualizing the atomic-scale electronic structure of the Ca₂CuO₂Cl₂ Mott insulator, *Nat. Commun.* **4**, 1365 (2013).