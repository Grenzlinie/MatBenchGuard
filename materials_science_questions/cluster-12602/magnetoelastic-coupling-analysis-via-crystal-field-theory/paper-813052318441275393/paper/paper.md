Accepted Manuscript

Atomic-scale distorted distorted lattice in chemically disordered equimolar complex alloys

Y.F. Ye, Y.H. Zhang, Q.F. He, Y. Zhuang, S. Wang, S.Q. Shi, A. Hu, J. Fan, Y. Yang

![](./images/813052318441275393_1.jpg)

PII: S1359-6454(18)30187-3

DOI: 10.1016/j.actamat.2018.03.008

Reference: AM 14426

To appear in: Acta Materialia

Received Date: 3 February 2018

Accepted Date: 1 March 2018

Please cite this article as: Y.F. Ye, Y.H. Zhang, Q.F. He, Y. Zhuang, S. Wang, S.Q. Shi, A. Hu, J.
Fan, Y. Yang, Atomic-scale distorted lattice in chemically disordered equimolar complex alloys, Acta
Materialia (2018), doi: 10.1016/j.actamat.2018.03.008.

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to
our customers we are providing this early version of the manuscript. The manuscript will undergo
copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please
note that during the production process errors may be discovered which could affect the content, and all
legal disclaimers that apply to the journal pertain.

![](./images/813052318441275393_2.jpg)

# Atomic-Scale Distorted Lattice in Chemically Disordered Equimolar Complex Alloys

Y.F. Ye$^{\text{a, b, c, 1, *}}$, Y.H. Zhang$^{\text{b, 1}}$, Q.F. He$^{\text{a, b}}$, Y. Zhuang$^{\text{b}}$, S. Wang$^{\text{a, b}}$, S.Q. Shi$^{\text{c}}$, A. Hu$^{\text{b, *}}$, J. Fan$^{\text{d}}$, Y. Yang$^{\text{a, b, *}}$

$^{\text{a}}$ Centre for Advanced Structural Materials, College of Science and Engineering, City University of Hong Kong, Tat Chee Avenue, Kowloon Tong, Kowloon, Hong Kong SAR, China

$^{\text{b}}$ Department of Mechanical and Biomedical Engineering, City University of Hong Kong, Tat Chee Avenue, Kowloon Tong, Kowloon, Hong Kong SAR, China

$^{\text{c}}$ Department of Mechanical Engineering, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong SAR, China

$^{\text{d}}$ Department of Physics and Materials Science, Center for Advanced Nuclear Safety and Sustainable Development, City University of Hong Kong, Tat Chee Avenue, Kowloon Tong, Kowloon, Hong Kong SAR, China

$^{1}$ Y.F.Y. and Y.H.Z. contribute equally to this work.

* Corresponding authors. (Y.F. Ye) yifanye@cityu.edu.hk, (A. Hu) alicehu@cityu.edu.hk and (Y. Yang) yonyang@cityu.edu.hk

## Abstract
It is a longstanding notion that alloying different sized elements can cause lattice distortion and phase transition in chemically complex alloys. However, a quantitative understanding of it remains difficult for traditional alloys, and becomes even more challenging for equimolar multicomponent alloys, also known as "high entropy alloys", which recently emerged as a promising structural/functional material and have been attracting tremendous research interest due to their unique properties. In this work, we carried out extensive first-principles calculations on a series of equimolar complex alloys with a chemically disordered crystalline structure, and characterized their atomic-scale lattice distortions in terms of the local residual strains. Albeit the confounding chemical/geometric complexities, we are able to show that the average attributes of such an atomic-scale distorted lattice, such as the lattice constant and the overall magnitude of the distortion induced residual strains, can be predicted very well by a simple physical model taking into account the efficient packing of different sized atoms interacting in an effective elastic medium. The findings of our current research unveils the details of locally distorted atomic packing in chemically disordered complex alloys, which sheds quantitative insights into the unusual strengthening mechanism as recently discovered in high entropy alloys.


**Keywords:** High entropy alloys; Analytical modeling; Ab initio calculations; Metal and alloys; Distortion

### 1. Introduction
Lattice distortion is a long-standing notion that can be dated back to the discovery of solid-solution strengthening in conventional alloys [1-3]. In principle, this strengthening effect stems from the interaction between dislocations and the elastic strain field induced by inhomogeneities, i.e. atomic size misfit and/or elastic modulus misfit, which generally result in lattice distortions[4-6]. In theory, such a strain field comprises both volumetric strain and shear strain, where the latter is usually omitted for its complexity despite its considerable strengthening effect[7]. By assuming that volumetric strains dominate lattice distortion in various solid solution models[4-6, 8], mean-field approaches, such as those based on the classic Eshelby theory [9], were widely used to calculate the local volumetric strain field. Such models are featured by picturing the solute atoms as an isolated unsheared "inclusion" embedded in an elastic "matrix" made up of the solvent atoms. The limitations of the mean-field approach, which usually neglects residual shear strains due to deformation asymmetry in a sheared elastic "matrix", has been long recognized, however, the theoretical results so obtained enabled quantitative knowledge of lattice distortion in terms of the average volumetric strains [4-6, 8]. In physical metallurgy, such knowledge was of great importance, which played an essential role in the understanding and early design of the best-performing solute-strengthened dilute alloys, such as Al alloys[10], Ti alloys[11], and Ni-based superalloys[12].

In sharp contrast to the conventional alloy design paradigm, which is usually based on one principal element, a new alloy design strategy, known as "high entropy alloy" (HEA)[13-19], was recently proposed to obtain complex multicomponent alloys with outstanding properties.

Unlike traditional alloys, HEAs are defined comprising at least five elements mixed in an equal or near-equal atomic fraction [14, 15]. In doing so, it was expected that the configurational entropy of mixing in these alloys can be maximized, thereby stabilizing a random solid solution phase against others, such as intermetallic compounds [13-17]. According to the recent works[20-23], many solid-solution HEAs display extraordinary mechanical properties unparalleled by traditional alloys, such as FeCoNiCrMn[21], $Fe_{32}Mn_{30}Ni_{30}Co_6Cr_2$[22], $Fe_{50}Mn_{30}Co_{10}Cr_{10}$[20], $Al_{20}Li_{20}Mg_{10}Sc_{20}Ti_{30}$[23]. To rationalize these findings, it was often proposed that severe lattice distortion might be present in the HEAs due to the mixing of numerous different sized elements, which leads to the impediment of dislocation movements, sluggish diffusion kinetics and precipitation of nano-sized coherent secondary phases[16, 17, 24, 25]. Nevertheless, it still remains elusive with the nature of lattice distortion in the HEAs. Unlike traditional alloys, there lacks a clear distinction between solvent and solute elements in these alloys; therefore, the use of the traditional ways, such as the Elshelby theory, to quantify the lattice distortion in HEAs could be questionable. More importantly, there is an increasing and open debate recently [26-29] about the lattice distortion experimentally detected in HEAs. Controversial results reported from different groups have been brought into question, such as those obtained from X-ray diffraction [25, 30-32], which are either not conclusive or usually do not agree with the transmission electron microscopy observations [33, 34] or atomistic simulations [29]. Therefore, despite the fundamental importance, the issue of lattice distortion in HEAs still remains open. In this work, through first-principle calculations combined with theoretical modeling, we intend to carry out a detailed investigation of the local strain field in equiatomic HEAs. Unlike the previous works [4-6, 8, 35], we will take into account not only the volumetric strains but also the shear strains, the latter of which might play a much more

important role to the dislocation strengthening mechanisms in HEAs, as suggested in Ref[7]. For this purpose, a series of equimolar complex alloys, ranging from binary, ternary, quaternary to quinary alloys, with a chemically disordered face centered cubic (FCC) structure were constructed using the elements of Fe, Co, Ni, Cr and Mn, which were chosen as the model systems for a systematic study of the lattice distortion in these chemically disordered equimolar complex alloys.

2. Methods: DFT Calculations

In the present study, density functional theory (DFT) calculations are performed by using the Vienna *ab initio* simulation package (VASP)[36, 37] with the projector augmented wave (PAW) method[38, 39] and generalized gradient approximation (GGA) parameterized by Perdew, Burke and Ernzerhof (PBE)[40]. The exchange-correlation functional for elements Fe, Cr, Ni, Co, and Mn includes semicore $p$ states as valence electrons. Plane-wave energy cutoff of 600 eV and Monkhorst–Pack $k$-point mesh[41] density of 0.2 $\text{\AA}^{-1}$ are used, which have been tested to ensure an energy accuracy of 1 meV/atom. The convergence of energy and force is set to $1.0{\times}10^{-7}$ eV and $1.0{\times}10^{-3}$ eV$\text{\AA}^{-1}$, respectively.

To model the random solid solution and quantify the local relaxation effects, special quasi-random structures (SQSs)[42] are generated using the mcsqs tool in the alloy theoretic automated toolkit (ATAT)[43]. For binary, ternary, quaternary and quinary FCC alloys, SQSs with 32, 108, 108 and 120 atoms, respectively, are constructed. Thereafter, the structure optimization is done in a two-step way. Firstly, an initial calculation of the volume-energy relationship is performed for each alloy structure, with atomic positions and cell shape fixed. The derived volume-energy data are fitted by the third-order Birch-Murnaghan equation of state[44, 45] to obtain the equilibrium lattice constant of the pristine structure. Thereafter, a further

relaxation of atomic positions, cell volume and shape was executed. Thereby, the residual stresses due to the atomic mismatch in pristine HEAs were relieved to explore the local lattice distortion. Here, the quasi-Newton algorithm with a smearing parameter of 0.1 eV was adopted to relax the ions into their instantaneous ground state.

Various elastic constants, including bulk modulus (B), shear modulus (G) and Poisson ratio (v), can be deduced for the HEAs from our studies. The direction dependent elastic constants of $c_{11}$ and $c_{12}$ were calculated from the standard energy-strain method, in line with the previous investigations on HEAs [46, 47]. After that, the bulk modulus (B) was extracted from the third-order Birch-Murnaghan equation of state and the shear modulus (G) was derived through the arithmetic Hill average of the Voigt and Reuss bounds [48]. The Poisson ratio (v) was then computed via $v=(3B-2G)/2(3B+G)$. The lattice constants, elastic constants and the lattice distortion of distorted structures, as well as those for pristine structures, are summarized in Table 1. As our first attempt, non-spin polarized calculations were performed for simplicity. After that, four equiatomic complex alloys, including FeCoNiCrMn, FeCoNiCr, FeCoNi and FeCrNi, were selected to study the effect of magnetism on lattice distortion. Following Refs [46, 49-54], ferromagnetic (FM) structure was constructed for FeNiCo, and paramagnetic (PM) structures for FeCoNi, FeCrNi, and FeCoNiCrMn, at T = 0 K. In general, the PM state of an alloy is presented by its spin-up and spin-down counterparts distributed randomly on the underlying sublattice, while for the FM setup, the Mn and Cr spins were set to be aligned anti-parallel to the Fe, Co and Ni spins.

## 3. Results of DFT Calculations

To model a random solid solution structure, the special quasi-random structure (SQS) approach, which was well established for simulating chemically disordered structures[42, 55], was

employed in our first-principles calculations based on density-functional-theory (DFT). First, a pristine structure with an ideal FCC symmetry was constructed, of which the lattice constant was determined at the local energy minimum that corresponded to an ideal or un-distorted random solid-solution configuration. Subsequently, the pristine FCC structure was energetically relaxed by allowing the atoms to stray away from their ideal positions in the pristine FCC lattice. As a result, this generated local atomic strains and a more energetically favorable but distorted random solid solution structure (see **Section 2**). During the DFT calculations, the temperature was set at 0 K to eliminate the effect of thermal fluctuation on lattice distortion. As an example, **Figs. 1 (a)-(b)** show the simulated results for the 3-D atomic configurations of the FeCoNiCr alloy before and after the local distortion. Remarkably, the local distortions are discernible at various sites, as marked in **Figs. 1(a)-(b)**, in the distorted atomic structure with comparison to the pristine lattice without local shear deformation. Furthermore, we calculated the X-ray diffraction (XRD) spectra of the pristine and distorted atomic structure. As shown in **Fig. 1(c)**, the pristine structure exhibits sharp diffraction peaks, conforming to ideal FCC structure as one expects. By comparison, the distorted structure displays similar FCC diffraction peaks; however, the peak profiles are seen widening, notable at the high diffraction angles but insignificant at the low diffraction angles. Interestingly, splitting of the (311) peak can be observed in the distorted structure. On average, the lattice constant decreases from 3.4998 Å to 3.4984 Å as a result of the lattice distortion. However, no peak splitting can be observed on the simulated XRD pattern of the individual element (see **Figs. 2(a)-(e)**). Similar results were also obtained for other alloys, as seen in **Supplementary Figs. S2-11**. In the HEA literatures [28, 56], a similar phenomenon of peak splitting was reported based on the experimental data obtained from apparent single phased alloys, which was then attributed to either lattice distortion or the emergence of a secondary

phase. Based on our current work, in which the alloys retained the single-phase FCC structure throughout the simulations, we conclude that the peak splitting we observed is due to the lattice distortion rather than the formation of a secondary phase.

To further characterize the local lattice distortions, we calculated the density distribution of the valence electrons with the partial electron density (PED) function. In theory, PED is derived by transforming the eigenfunctions with an energy window just below the Fermi level (energy level ranging from -1 eV up to the Fermi energy)[57], which provides the detailed information about the shape of frontier orbitals in real space. A denser *k* point sampling (*k* spacing of $0.14\ \mathrm{\AA}^{-1}$) were used for the calculation of PED. The contour plots of PED in the (001) plane of FeCoNiCr are shown in **Fig. 3(a)-(b)**. Through the PEDs, one can see that chemical bonding is anisotropic and asymmetric in the pristine structure, the intensity of which becomes even stronger after the distortion, as highlighted in Fig. 3(b). Similar results can be found in **Supplementary Figs. S2-11** for other alloys. This is in sharp contrast to the chemical bonding in pure metals, which exhibits a perfect 4-fold symmetry in 2D (see **Supplementary Fig. S1**).

To quantitatively characterize the local lattice distortions, here we calculated the local strain tensor around each atom. Following the previous work [58], the local deformation gradient tensor for each atom can be calculated via $$\mathbf{J}_{i}=\left(\sum_{j \in N_{i}^{0}} \mathbf{r}_{j i}^{0 T} \mathbf{r}_{j i}^{0}\right)^{-1}\left(\sum_{j \in N_{i}^{0}} \mathbf{r}_{j i}^{0 T} \mathbf{r}_{j i}\right),$$ where $\boldsymbol{r}_{j i}$ is the vector between atom $j$ and $i$ with $j$ being one of the neighboring atom of the central atom $i$; $N_{i}^{0}$ is the total number of the nearest neighbors of atom $i$ and superscript "0" means the reference or undistorted configuration (see **Appendix A**). **Fig. 4(a)-(d)** show the contour plots of the components of the strain tensor in the basal plane of (001) for FeCoNiCr. In addition to the shear

strains, we also computed the local atomic hydrostatic strain via $\varepsilon_{i}^{m}=\frac{1}{6}(Tr \mathbf{J}_{i}^{T} \mathbf{J}_{i}-3)$ [58, 59]. As
we can see in **Fig. 4(a)-(d)**, although their averages are small, the local value of each strain
component is highly fluctuating and varies from one atom to another, breaking the symmetry and
smoothness of a regular strain field one could obtain for a dilute solution. As a result, the local
strain components around the individual atoms depend strongly on the local packing
environment, not just determined by the species of the chemical elements alone. According to the
distribution of each strain component as shown in **Fig. 5(a)-(d)**, the average residual volumetric
strain is finite while the average residual shear strain approaches zero. By comparison, the
fluctuation of the residual shear strains is prominent, ranging from -0.01 to 0.01.

### 4. Theoretical Modeling
In general, local lattice distortion generates both volumetric and shear residual strains, which
raises the elastic energy stored in the alloys. For the volumetric strain, the elastic energy density
is given by $u_{v}=\frac{3}{2}\left(C_{11}+2 C_{12}\right) \sum_{i=1, n}\left(\varepsilon_{i}^{m}\right)^{2} / n$, where n is the total number of particles, $C_{11}$ and $C_{12}$
are the elastic constants in Voigt notation [59]; while for the shear strain, the elastic energy
density is given by
$$
u_{d}=\frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left(\gamma_{i}^{\text {Mises }}\right)^{2} / n+\left[2 C_{44}-\left(C_{11}-C_{12}\right)\right] \sum_{i=1, n}\left[\left(\varepsilon_{i}^{x y}\right)^{2}+\left(\varepsilon_{i}^{x z}\right)^{2}+\left(\varepsilon_{i}^{y z}\right)^{2}\right] / n
$$
where
$\gamma_{i}^{\text {Mises }}=\sqrt{\frac{2}{3} \operatorname{Tr}\left(\mathbf{F}_{i}-\varepsilon_{i}^{m} \mathbf{I}\right)}$ is the *von Mises* equivalent atomic shear strain, $\mathbf{F}_{i}$ is the local
Lagrangian strain tensor at atom $i$ and $\mathbf{I}$ is the identity strain tensor [58, 59] (see **Appendix A**).

Since the second term of $u_{d}$ is negligibly small relative to the first term for most metallic alloys,
we can approximately take $u_{d} \approx \frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left(\gamma_{i}^{\text {Mises }}\right)^{2} / n$ for simplicity (see **Appendix A**). As

a result, the total lattice distortion induced elastic energy density is
$$
u_{p}=u_{v}+u_{d} \approx \frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left[\frac{2\left(C_{11}+2 C_{12}\right)}{\left(C_{11}-C_{12}\right)}\left(\varepsilon_{i}^{m}\right)^{2}+\left(\gamma_{i}^{M i s e s}\right)^{2}\right] / n
$$
As an analogy to the equivalent von Mises strain [59], we here define an effective strain $\gamma_{i}^{e q}$ for atom $i$ to quantify the local effect of the lattice distortion, which can be expressed as:

$$
\gamma_{i}^{e q}=\sqrt{\frac{2\left(C_{11}+2 C_{12}\right)}{\left(C_{11}-C_{12}\right)}\left(\varepsilon_{i}^{m}\right)^{2}+\left(\gamma_{i}^{M i s e s}\right)^{2}} \tag{1}
$$

With this newly defined $\gamma_{i}^{e q}$, the total energy density can be re-written as $u_{p}=\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2}$,
where $\gamma=\sqrt{\sum_{i=1, n}\left(\gamma_{i}^{e q}\right)^{2} / n}$ is the average equivalent strain (see Appendix A). As demonstrated in Fig. 6(a), in the pristine structure, there is no local distortion and hence $\gamma_{i}^{e q}=0$ everywhere in the lattice. After the distortion, local shear and volumetric strains are developed around the individual atoms. As seen in Fig. 6(b), the magnitude of $\gamma_{i}^{e q}$ mainly ranges from 0.01 and 0.025 on the (001) plane, suggestive of highly fluctuating local lattice distortions. For the whole alloy,
we compute an average equivalent strain $\gamma=\sqrt{\sum_{i=1, n}\left(\gamma_{i}^{e q}\right)^{2} / n}$ , to quantify the overall lattice distortion.

Table 1 lists the important properties and attributes of the pristine and distorted structure extracted from our DFT simulations for the 11 types of FCC equimolar alloys. These include the simulated lattice constants $a^{D F T}$ of the pristine and distorted structures, and the simulated equivalent strain $\gamma^{D F T}$ in the distorted structures. To understand these results in a quantitative manner, we herein develop a simple physical model, which takes into account the efficient packing of different sized atoms interacting through an effective elastic medium. The basic idea

can be illustrated in **Fig. 7**. From a thermodynamic viewpoint, the pristine structure corresponds to a fictitious mean lattice at the local energy minimum $E_{l}$ in the energy well without any local distortions; while the distorted structure corresponds to the local energy minimum $E_{2}$ in the energy well that allows both dilatations and shear distortions. Following the method in Froyen's work [60], the fictitious pristine lattice can act as a reference lattice, from which atomic displacements can result. In theory, lattice distortion is energetically favorable only when $\Delta E = E_{2}-E_{l}<0$. For the simulated atomic configurations, $\Delta E$ is mainly due to the change in the elastic energy storage. From a structural perspective, this is only possible if local shearing can relax part of the radial strains developed around the individual atoms in the pristine structure, due to the atomic size misfit as seen in **Fig. 7**. According to Ref. [26], the elastic energy stored per unit volume in the pristine structure can be expressed as $u_{1}=\frac{3}{2}(C_{11}+2C_{12})(\varepsilon^{fluc})^{2}$ (see **Appendix A**), while that in the distorted structure can be derived as $u_{2}=\frac{3}{2}(C_{11}+2C_{12})(\varepsilon^{fluc*})^{2}+u_{p}$ (see **Appendix A**), where $\varepsilon^{fluc}$ and $\varepsilon^{fluc*}$ denote the standard deviation of the residual radial strains in the pristine and distorted structure, respectively; $u_{p}$ denotes the additional energy increase due to the lattice distortion. Thus, the driving force $\Delta u=u_{2}-u_{1}$ for the distortion can be expressed as:

$$
\Delta u=\frac{3}{2}\left(C_{11}+2 C_{12}\right)\left[\left(\varepsilon^{f l u c^{*}}\right)^{2}-\left(\varepsilon^{f l u c}\right)^{2}\right]+\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2} \tag{2}
$$

Note that $\varepsilon^{fluc*}$ and $\varepsilon^{fluc}$ are related theoretically, the relation of which may be generally written as $\varepsilon^{fluc*}=\varepsilon^{fluc}(\gamma)$. Now we seek a first-order approximation of the above relation, which is $\varepsilon^{fluc*}=\varepsilon^{fluc}-\alpha\gamma$ with $\alpha$ a parameter yet to be determined. Substituting this equation into (2) gives $\Delta u=\frac{3}{2}\left(C_{11}+2 C_{12}\right)\left[\left(\varepsilon^{f l u c}-\alpha \gamma\right)^{2}-\left(\varepsilon^{f l u c}\right)^{2}\right]+\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2}$. Minimizing the energy

difference $\Delta u$ requires $\partial \Delta u / \partial \gamma=0$, which yields:

$$
\gamma=\left(\frac{2\left(C_{11}+2 C_{12}\right) \alpha}{\left(C_{11}-C_{12}\right)+2\left(C_{11}+2 C_{12}\right) \alpha^{2}}\right) \varepsilon^{f l u c} \tag{3}
$$

Eq. (3) is important and provides the critical condition under which distortion becomes energetically favorable. Here, we further propose that, among all admissible distorted lattice configurations as predicted by Eq. (3), the real distorted lattice should take on the configuration that maximizes the overall atomic displacement or the effective average strain $\gamma$. This is consistent with the idea that lattice distortion is generally in favor of phase transition [9]. Following the above thinking that $\gamma$ should be maximized, we have $\partial \gamma / \partial \alpha=0$ which yields $\alpha=\sqrt{\left(C_{11}-C_{12}\right) / 2\left(C_{11}+2 C_{12}\right)}$. For an isotropic system, $\frac{\left(C_{11}-C_{12}\right)}{\left(C_{11}+2 C_{12}\right)}=\frac{(1-2 v)}{(1+v)}$, in which $v$ is the Poisson's ratio. Substituting this expression into Eq. (3), we thereby obtain the critical equivalent strain $\gamma^{th}=\frac{1}{2} \sqrt{\frac{2(1+v)}{(1-2 v)}} \varepsilon^{fluc}$ (see Appendix A).

To verify the above analyses, we calculated $\gamma^{th}$ for the pristine structures of the 11 FCC equimolar alloys with $\varepsilon^{fluc}$ determined via the method detailed in Ref. [26]. Afterwards we compared them with the DFT derived ones, which can be computed via $\gamma^{D F T}=\sqrt{\sum_{i=1, n}\left(\gamma_{i}^{e q}\right)^{2} / n}$. As shown in Fig. 8(a), one can see a general trend that $\gamma^{D F T}$ correlates well with $\gamma^{th }$. This delivers a clear message that our theoretical model captures the equivalent strain $\gamma$ very well. Based on the above results, we can further derive that the elastic driving force to be $\Delta u=-\frac{3}{2}\left(C_{11}-C_{12}\right) \gamma^{2}$ with $\varepsilon^{f l u c *}=\varepsilon^{f l u c}-\frac{1}{2} \varepsilon^{f l u c}=\frac{1}{2} \varepsilon^{f l u c}$. According to Eq. (2), one can infer that the change in the

elastic energies should be $\Delta u=\frac{3}{2}(C_{11}+2 C_{12})\left\lfloor(\varepsilon^{fluc*})^{2}-(\varepsilon^{fluc})^{2}\right\rfloor$ in the presence of only atomic contraction and expansion. Therefore, our results indicate that, in order to offset the elastic energy resulting from lattice distortion, a maximum of 75% of the elastic energy stored in the pristine structure could be released out. More importantly, one can infer from the data, as shown in Fig. 8(a), that the lattice distortion does not generally follow the proposition that lattice distortion would increase with the number of elements, as early proposed in the HEA literature
[26]. Since $\varepsilon^{fluc}$ is correlated with the atomic size difference $\delta=\sqrt{\sum_{i=1}^{n} c_{i}(1-r_{i} / \sum_{j=1}^{n} c_{j} r_{j})^{2}}$ [16] and $\varepsilon^{fluc} \approx 0.97 \delta$ [26, 61], the equivalent strain $\gamma$ can be expressed as $\gamma=f(v) \delta$ , where
$f(v)=0.485 \sqrt{\frac{2(1+v)}{(1-2 v)}}$ . The above expression suggests that the lattice distortion induced residual strain in the chemically complex alloys depends on not only the atomic size misfit, as quantified by $\delta$ , but also on the attribute of the chemical bonding reflected by the Poisson's ratio. As shown in Fig. 8(b), by mixing different sized elements in a multicomponent alloy, such as FeCoNiCr or FeCoNiCrMn, one can reduce the atomic size difference without significantly altering the Poisson ratio, and thus partly relax the elastic energy induced by the large lattice distortion in the binary system being composed of the largest and smallest elements, such as FeCr.

Furthermore, we evaluated the lattice constants of the pristine and distorted structures for the equimolar alloys we considered. In general, the lattice constant of an alloy can be expressed as[26]: $a=\sum_{i=1}^{n} c_{i} a_{i}(1+\varepsilon_{i})$ , where $a_{i}$ is the lattice constant of the FCC lattice made up of only the $i^{th }$ element. On the basis of our theoretical model (Eqs. (2) - (3)), it can be shown that a complete set of equations can be developed to solve for the radial strains $\varepsilon_{i}$ around the constituent

elements in the pristine and distorted structures (see Appendix B). As a result, we obtained the lattice constant $a^{th}$ of the alloys in their pristine and distorted structures respectively, as tabulated in Table 1. Evidently, shear distortion does not significantly change the lattice constant of the alloys, which is within our expectation because of the decoupling between shear and volumetric strains. To justify our theoretical results, we compare the lattice constant $a^{DFT}$ derived from the DFT calculations with the theoretical value $a^{th}$. As seen in Fig. 9 and the inset, the theoretical predictions agree remarkably well with the DFT calculations.

## 5. Discussions

### 5.1 Solid solution strengthening

As noted in the recent works [35, 62], the fluctuation of local residual strains is important to the mechanical properties of equimolar complex alloys or HEAs even though the average residual strain in them may be small. According to the solid-solution strengthening model [4, 6, 7], the critical shear stress $\tau_{0}(T=0K)\sim \Delta E_{p}^{4/3}$ , where $\Delta E_{p}$ is the binding energy of a dislocation to a local region which can be associated with the standard deviation of the energy difference when a dislocation segment moves over a distance of $\omega$. In theory, this binding energy is closely related to the elastic field around solute atoms [7]. In the presence of atomic size difference and lattice distortion, this elastic field can be intensified, thereby leading to solute strengthening [3]. According to Labusch [3], solute strengthening comes about owing to two types of misfit: one is the volumetric misfit and the other is the shear misfit. In our model, the equivalent strain $\gamma_{i}^{eq}$ quantifies both the volumetric and shear misfits between a central atom $i$ and its surroundings.

Therefore, we may speculate that
$$\Delta E_{p} \propto \sqrt{\sum_{i=1, n}\left(c_{11}-c_{12}\right)\left(\gamma_{i}^{e q}\right)^{2} / n}$$
or
$$\tau_{0}(T=0 K) \propto\left[\left(c_{11}-c_{12}\right) \gamma^{2}\right]^{2 / 3}.$$

To verify the above speculation, we plot $\sigma_{alloy}^{\text{exp.}}$ vs. $\left[\left(c_{11}-c_{12}\right)\left(\gamma^{DFT}\right)^{2}\right]^{2/3}$, where $\sigma_{alloy}^{\text{exp.}}$ can be viewed as an equivalent of $\tau_{0}$ (T=0K) and was extracted from previous experiments [6] after subtraction of other strengthening effects, such as the Hall-Patch effect. Evidently, $\sigma_{alloy}^{\text{exp.}}$ is in a good linear correlation with $\left[\left(c_{11}-c_{12}\right)\left(\gamma^{DFT}\right)^{2}\right]^{2/3}$ as shown in Fig. 10. This is encouraging and suggests that further investigation is worthwhile to explore the strengthening mechanisms in the chemically complex solid-solution alloys by linking the generalized residual strain of a highly fluctuation residual strain field to dislocation movements in it.

### 5.2 Magnetic effect
Before moving to the Summary, we would like to stress that all the above calculations were based on non-spin polarized formulation of DFT. However, some recent works [35, 49, 63] already showed that there might be a magnetic effect on the local lattice distortions in HEAs at a finite temperature. To have a further check, we performed additional DFT simulations on four equimolar alloys, as mentioned earlier, by switching on magnetic calculations and, compared the magnitude of $\gamma_{i}^{eq}$ around each atom computed before and after taking magnetism into consideration. As seen in **Fig. 11**, the distribution of $\gamma_{i}^{eq}$ for the four model alloys only varies a little after switching on the magnetism option, which is consistent with the previous results [35]. To be specific, a small peak shift can be observed (left for FeCoNi, FeCrNi and FeCoNiCrMn, while right for FeCoNiCr) although the curve of the overall distribution remains almost unchanged. Such a peak shift indicates that magnetism could either relax or intensify the overall residual strain caused by lattice distortion.

Given the results in **Fig. 11**, an updated $\gamma^{DFT}$ is expected after considering magnetism. As shown in **Fig. 8(a)**, the values of $\gamma^{DFT}$ of the magnetic systems become slightly different from

those of their non-magnetic counterparts. However, it can be clearly observed that these $\gamma^{DFT}$'s still have a good correlation with the theoretically predicted values [**Fig. 8(a)**], if the updated Poisson's ratios of these magnetic systems were used in $\gamma^{th} = \frac{1}{2} \sqrt{\frac{2\left(1+\nu_{mag.}\right)}{\left(1-2\nu_{mag.}\right)}} \varepsilon^{fluc}$. Since $\gamma^{DFT}$ is an equivalent strain which quantifies the lattice distortion, the relative change of $\gamma^{DFT}$, either positive or negative, thereby suggests that the magnetic effect is quite diversified with respect to lattice distortion and thus solute strengthening in different alloys. Seemingly, this may add additional difficulties for the understanding of lattice distortion in a magnetic field. Nevertheless, since the magnetic effect also manifests itself in the alloy elastic properties, such as the Poisson's ratio, our results suggest that the theoretical modeling laid out in the present work still gives a very good prediction of the lattice distortion with the updated elastic properties.

## 6. Summary
In summary, through the first-principles calculations, we reveal the details of a non-symmetric residual strain field with atomic scale fluctuations in a series of equimolar complex alloys, which results from atomic scale lattice distortion and would be impossible to study via the conventional experimental means. Subsequently, we develop a simple theory to quantitatively understand our simulation results by considering the efficient packing of different sized atoms interacting in an effective elastic medium. It is shown that our theory captures the general trend of the lattice constants and the magnitude of the distortion induced effective strain very well, either with or without considering the magnetism. Since dislocation strengthening in these complex alloys is closely related to the distribution of the residual strain field, we envision that our current findings should be valuable to further our understanding of plasticity enhancement in chemically complex alloys, such as HEAs.


### Acknowledgements

The research of YY is supported by the City University of Hong Kong with the project Nos 9610366 and 7004597. AH is supported by City University of Hong Kong internal grant 9610336 and National Natural Science Foundation of China grant No 11605148. The present research is also supported by the PolyU Post-Dr Research Grant No G-YW2Q. This research has also used computing resources supported by Special Program for Applied Research on Super Computation of the NSFC-Guangdong Joint Fund (the second phase) to JF.

### Appendix A: The equivalent strain due to the shear induced energy penalty

According to the previous works [26, 64], when incorporating different sized atoms to form an alloy with a simple lattice structure, the radii of the constituent elements need to be adjusted in order to accommodate the atomic size differences. Therefore, the resultant sizes can be very different from those in the corresponding simple metallic form, leading to the development of the intrinsic residual strain [26]. For the perfect pristine structure without any shear, all bond lengths are equal, and the local residual strains are purely volumetric. According to Ref. [26], in this case, the residual radial strain surrounding element $i$ can be derived as $\varepsilon_{i}=\sum_{j=1}^{n} \omega_{i j} c_{j} / \sum_{k=1}^{n} A_{i k} c_{k}-4 \pi \bar{\eta} /\left(N_{i} \sum_{k=1}^{n} A_{i k} c_{k}\right)$, where $\omega_{i j}$ is the solid angle subtended by atom $j$ around atom $i$; $c_{i}$ is the atomic fraction of element $i$; $N_{i}$ is the coordinate number of
element $i$; $\bar{\eta}=\frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} c_{j} c_{i} N_{i}\left[1-\frac{\sqrt{x_{i j}\left(x_{i j}+2\right)}}{x_{i j}+1}\right]$ and $A_{i j}=\frac{2 \pi x_{i j}}{\left(x_{i j}+1\right)^{2} \sqrt{x_{i j}\left(x_{i j}+2\right)}}$ in which $x_{i j}=r_{i} / r_{j}$
and $r_{i}$ is the radius of element $i$. To compute the residual radial strains for a given alloy, one simply needs to know the atomic radius of the constituent element before mixing. For this purpose, we also carried out additional DFT simulations on the pure metals to obtain their respective radius at 0K, as listed in **Table 1**. Once $\varepsilon_{i}$ was obtained, it can be shown that the

average radial strain $\bar{\varepsilon}$ is zero in absence of residual shear strains [26]. In such a case, the fluctuation of these local radial strains, in terms of the standard deviation of their distribution, can be simply computed as $\varepsilon^{fluc} = \sqrt{\sum c_{i} \varepsilon_{i}^{2}}$. According to Ye et al. [26], this radial strain fluctuation is strongly correlated with the atomic size misfit in a multicomponent alloy, which can be used further as a metric to gage the lattice stability.

Following the assumptions in previous works [29, 35], the above model was built without considering the existence of shear strains. However, recent work shows shear strains might also play a very important role in solute strengthening effect[7]. Hence it is necessary for us to revisit the formula of residual strains. First, let's start from a thermodynamic viewpoint. In theory, without outside stimuli, distortions occur only when the energy state after distortion is lower than that of the pristine configuration. According to Ref. [26], when applying the continuum elastic theory to HEAs, the strain energy density in the pristine structure can be expressed as $u_{1} = \frac{3}{2}(C_{11} + 2C_{12})(\varepsilon^{fluc})^{2}$, in which $C_{11}$ and $C_{12}$ are elastic constants and $\varepsilon^{fluc}$ the standard deviation of residual radial strains in the pristine structure. While the strain energy density in the distorted structure can be derived as $u_{2} = \frac{3}{2}(C_{11} + 2C_{12})(\varepsilon^{fluc^{*}})^{2} + u_{p}$ , where $u_{p}$ is the energy penalty due to the lattice distortion, $\varepsilon^{fluc^{*}}$ denote the corresponding standard deviation in the distorted structure, respectively. In theory, lattice distortion will cause two parts of energy penalty: one is the distortion induced hydrostatic strain energy $u_{v}$ and the other is the distortional shear strain energy $u_{d}$. Following the previous work [58], with the relative displacements of the particle's neighbors $\mathbf{r}_{ji}$, where atom $j$ is one of atoms $i$'s nearest neighbors, the local deformation gradient tensor $\mathbf{J}_{i}$ for each particle can be derived by minimizing $\sum_{j \in N_{i}^{0}} \left| \mathbf{r}_{ji}^{0} \mathbf{J}_{i} - \mathbf{r}_{ji} \right|^{2}$, which yields

$$
\mathbf{J}_{i}=\left(\sum_{j \in N_{i}^{0}} \mathbf{r}_{j i}^{0 T} \mathbf{r}_{j i}^{0}\right)^{-1}\left(\sum_{j \in N_{i}^{0}} \mathbf{r}_{j i}^{0 T} \mathbf{r}_{j i}\right)
$$
Here $N_{i}^{0}$ is the total number of nearest neighbors of atom $i$ and superscript "0" refers the reference configuration[58]. As the local Lagrangian strain at atom $i$ is
$$
\mathbf{F}_{i}=\frac{1}{2}\left(\mathbf{J}_{i}^{T} \mathbf{J}_{i}-\mathbf{I}\right)
$$
, the local hydrostatic strain can be calculated via $\varepsilon_{i}^{m}=\frac{1}{3} \operatorname{Tr}\left(\mathbf{F}_{i}\right)$, and the local
shear strain invariant is $\gamma_{i}^{Mises}=\sqrt{\frac{2}{3} \operatorname{Tr}\left(\mathbf{F}_{i}-\varepsilon_{i}^{m} \mathbf{I}\right)}[58,59]$. For a cubic system, the hydrostatic
strain energy density can be calculated via $u_{v}=\frac{3}{2}\left(C_{11}+2 C_{12}\right) \sum_{i=1, n}\left(\varepsilon_{i}^{m}\right)^{2} / n$, while the distortional
strain energy density is
$$
u_{d}=\frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left(\gamma_{i}^{\text {Mises }}\right)^{2} / n+\left[2 C_{44}-\left(C_{11}-C_{12}\right)\right] \sum_{i=1, n}\left[\left(\varepsilon_{i}^{x y}\right)^{2}+\left(\varepsilon_{i}^{x z}\right)^{2}+\left(\varepsilon_{i}^{y z}\right)^{2}\right] / n
$$
, where n is the total number of particles. Hence the total shear induced energy penalty is:
$$
\begin{aligned}
& u_{p}=u_{v}+u_{d} \\
& =\frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left\{\frac{2\left(C_{11}+2 C_{12}\right)}{\left(C_{11}-C_{12}\right)}\left(\varepsilon_{i}^{m}\right)^{2}+\left(\gamma_{i}^{\text {Mises }}\right)^{2}+\frac{4\left[2 C_{44}-\left(C_{11}-C_{12}\right)\right]}{3\left(C_{11}-C_{12}\right)}\left[\left(\varepsilon_{i}^{x y}\right)^{2}+\left(\varepsilon_{i}^{x z}\right)^{2}+\left(\varepsilon_{i}^{y z}\right)^{2}\right]\right\} / n
\end{aligned}
$$
(A.1)

As an analogy of the definition of the equivalent Von Mises strain [59], here we define an equivalent strain $\gamma_{i}^{e q}$ to be:
$$
\gamma_{i}^{e q}=\sqrt{\frac{2\left(C_{11}+2 C_{12}\right)}{\left(C_{11}-C_{12}\right)}\left(\varepsilon_{i}^{m}\right)^{2}+\left(\gamma_{i}^{\text {Mises }}\right)^{2}+\frac{4\left[2 C_{44}-\left(C_{11}-C_{12}\right)\right]}{3\left(C_{11}-C_{12}\right)}\left[\left(\varepsilon_{i}^{x y}\right)^{2}+\left(\varepsilon_{i}^{x z}\right)^{2}+\left(\varepsilon_{i}^{y z}\right)^{2}\right]} \quad \text { (A.2) }
$$

Thus Eq. (A.1) can be simplified into
$$
u_{p}=\frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left(\gamma_{i}^{e q}\right)^{2} / n=\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2}
$$
(A.3)

For metallic alloys, the second term in the expression of $u_{d}$ is relatively small compared to the
first term, we can approximately take $u_{d} \approx \frac{3}{4}\left(C_{11}-C_{12}\right) \sum_{i=1, n}\left(\gamma_{i}^{\text {Mises }}\right)^{2} / n$ and hence

$$
\gamma_{i}^{e q} \approx \sqrt{\frac{2\left(C_{11}+2 C_{12}\right)}{\left(C_{11}-C_{12}\right)}\left(\varepsilon_{i}^{m}\right)^{2}+\left(\gamma_{i}^{M i s e s}\right)^{2}}
$$
From the energy viewpoint, distortions occur when:

$$
\Delta u=u_{2}-u_{1}=\frac{3}{2}\left(C_{11}+2 C_{12}\right)\left[\left(\varepsilon^{\text {fluc }}\right)^{2}-\left(\varepsilon^{\text {fluc* }}\right)^{2}\right]+\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2}<0 \tag{A.4}
$$

Conceptually, $\varepsilon^{fluc*}$ and $\varepsilon^{fluc}$ are related, the relation of which may be generally written as $\varepsilon^{fluc*}=\varepsilon^{fluc}(\gamma)$. For a first order approximation, assuming that $\varepsilon^{fluc*}=\varepsilon^{fluc}-\alpha \gamma$ with $\alpha$ a parameter yet to be determined, Eq. (A.4) can be rewritten as

$$
\Delta u=u_{2}-u_{1}=\frac{3}{2}\left(C_{11}+2 C_{12}\right)\left[\left(\varepsilon^{\text {fluc }}-\alpha \gamma\right)^{2}-\left(\varepsilon^{\text {fluc }}\right)^{2}\right]+\frac{3}{4}\left(C_{11}-C_{12}\right) \gamma^{2}<0
$$

Minimizing the energy difference $\Delta u$ requires $\partial \Delta u / \partial \gamma=0$, which yields:

$$
\gamma=\left(\frac{2\left(C_{11}+2 C_{12}\right) \alpha}{\left(C_{11}-C_{12}\right)+2\left(C_{11}+2 C_{12}\right) \alpha^{2}}\right) \varepsilon^{\text {fluc }} \tag{A.5}
$$

In theory, the above expression gives all $\gamma$'s which are energetically favorable. In general, in a size-mismatched disordered system, atoms will be driven to move away from their ideal lattice positions, leading to a sustainable increase of lattice distortion if there is no further energy barrier [9]. Following this thinking, it is natural for one to assume that $\gamma$ will be pushed to reach a critical value, where the reduced energy can no longer balance the energy penalty due to the large distortion. In such case, $\gamma$ will be maximized requiring $\partial \gamma / \partial \alpha=0$ which yields that $\alpha=\sqrt{\left(C_{11}-C_{12}\right) / 2\left(C_{11}+2 C_{12}\right)}$. For an isotropic cubic system, $\frac{\left(C_{11}-C_{12}\right)}{\left(C_{11}+2 C_{12}\right)}=\frac{(1-2 v)}{(1+v)}$, in which $v$ is the poisson's ratio, hence an expression of $\alpha$ that weakly depends on the Poisson's ratio of an alloy can be thereby derived. Substituting this expression into Eq. (A.5), we thereby have the critical equivalent strain $\gamma^{t h}=\frac{1}{2} \sqrt{\frac{2(1+v)}{(1-2 v)}} \varepsilon^{f l u c}$, and consequently the energy difference is

$$\Delta u=-\frac{3}{2}\left(C_{11}-C_{12}\right) \gamma^{2} \text {, and } \varepsilon^{f l u c^{*}}=\varepsilon^{f l u c}-\frac{1}{2} \varepsilon^{f l u c}=\frac{1}{2} \varepsilon^{f l u c}.$$

## Appendix B: Residual Radial Strains in the Distorted Lattice
Since the shear strain is decoupled with the volumetric strain and given that the lattice still retains a FCC structure after adjustment, the lattice constant can be generally expressed as:
$a=\sum_{i=1}^{n} c_{i} a_{i}\left(1+\varepsilon_{i}\right)$, where $a_{i}$ is the constant of the FCC lattice made up of the pure $i$th element.

According to Ref. [26], since the average residual radial strain is finite and none-zero in the distorted structure, the residual radial strain of element $i$ can be generally rewritten as:
$$
\varepsilon_{i}=\frac{\sum_{j=1}^{n} \omega_{i j} c_{j}}{\sum_{k=1}^{n} A_{i k} c_{k}}-\frac{4 \pi \bar{\eta}}{N \sum_{k=1}^{n} A_{i k} c_{k}}+\frac{\sum_{j=1}^{n} c_{j} A_{i j} \varepsilon_{j}}{\sum_{k=1}^{n} A_{i k} c_{k}}
\tag{B.1}
$$

In theory, by solving a complete set of Eq. (B.1) with the constraint condition $\varepsilon^{f l u c^{*}}=\frac{1}{2} \varepsilon^{f l u c}$, one can mathematically work out the residual radial strain $\varepsilon_{i}^{*}$ for each element and the equilibrium packing efficiency $\bar{\eta}^{*}$ in the distorted structure.

## References
[1] P. Haasen, Mechanical Properties of Solid Solutions, in: R.I. Jaffee, B.A. Wilcox (Eds.), Fundamental Aspects of Structural Alloy Design, Springer US, Boston, MA, 1977, pp. 3-25.

[2] F.R.N. Nabarro, The mechanical properties of metallic solid solutions, Proceedings of the Physical Society 58(6) (1946) 669.

[3] R. Labusch, A Statistical Theory of Solid Solution Hardening, physica status solidi (b) 41(2) (1970) 659-669.

[4] I. Toda-Caraballo, P.E.J. Rivera-Díaz-del-Castillo, Modelling solid solution hardening in high entropy alloys, Acta Mater. 85 (2015) 14-23.

[5] C. Varvenne, G.P.M. Leyson, M. Ghazisaeidi, W.A. Curtin, Solute strengthening in random

alloys, Acta Mater. (2016).

[6] C. Varvenne, A. Luque, W.A. Curtin, Theory of strengthening in fcc high entropy alloys, Acta Mater. 118 (2016) 164-176.

[7] D. Ma, M. Friák, J. von Pezold, D. Raabe, J. Neugebauer, Computationally efficient and quantitatively accurate multiscale simulation of solid-solution strengthening by ab initio calculation, Acta Mater. 85 (2015) 53-66.

[8] I. Toda-Caraballo, A general formulation for solid solution hardening effect in multicomponent alloys, Scr. Mater. 127 (2017) 113-117.

[9] J.D. Eshelby, The Continuum Theory of Lattice Defects, in: S. Frederick, T. David (Eds.), Solid State Physics, Academic Press1956, pp. 79-144.

[10] Ø. Ryen, B. Holmedal, O. Nijs, E. Nes, E. Sjölander, H.-E. Ekström, Strengthening mechanisms in solid solution aluminum alloys, Metallurgical and Materials Transactions A 37(6) (2006) 1999-2006.

[11] G. Welsch, R. Boyer, E.W. Collings, Materials Properties Handbook: Titanium Alloys, ASM International1993.

[12] J.R. Davis, A.S.M.I.H. Committee, ASM Specialty Handbook: Heat-Resistant Materials, ASM International1997.

[13] B. Cantor, Multicomponent and High Entropy Alloys, Entropy 16(9) (2014) 4749.

[14] B. Cantor, I.T.H. Chang, P. Knight, A.J.B. Vincent, Microstructural development in equiatomic multicomponent alloys, Mat Sci Eng a-Struct 375 (2004) 213-218.

[15] J.W. Yeh, S.K. Chen, S.J. Lin, J.Y. Gan, T.S. Chin, T.T. Shun, C.H. Tsau, S.Y. Chang, Nanostructured High-Entropy Alloys with Multiple Principal Elements: Novel Alloy Design Concepts and Outcomes, Adv. Eng. Mater. 6(5) (2004) 299-303.


[16] Y. Zhang, T.T. Zuo, Z. Tang, M.C. Gao, K.A. Dahmen, P.K. Liaw, Z.P. Lu, Microstructures and properties of high-entropy alloys, Prog. Mater Sci. 61(0) (2014) 1-93.

[17] M.H. Tsai, J.W. Yeh, High-Entropy Alloys: A Critical Review, Mater. Res. Lett. 2(3) (2014) 107-123.

[18] Y. Ye, Q. Wang, J. Lu, C. Liu, Y. Yang, High-entropy alloy: challenges and prospects, Materials Today 19(6) (2016) 349-362.

[19] Q. He, Z. Ding, Y. Ye, Y. Yang, Design of High-Entropy Alloy: A Perspective from Nonideal Mixing, Jom-Us 69(11) (2017) 2092-2098.

[20] Z. Li, K.G. Pradeep, Y. Deng, D. Raabe, C.C. Tasan, Metastable high-entropy dual-phase alloys overcome the strength-ductility trade-off, Nature 534(7606) (2016) 227-30.

[21] B. Gludovatz, A. Hohenwarter, D. Catoor, E.H. Chang, E.P. George, R.O. Ritchie, A fracture-resistant high-entropy alloy for cryogenic applications, Science 345(6201) (2014) 1153-1158.

[22] Y. Deng, C.C. Tasan, K.G. Pradeep, H. Springer, A. Kostka, D. Raabe, Design of a twinning-induced plasticity high entropy alloy, Acta Mater. 94(0) (2015) 124-133.

[23] K.M. Youssef, A.J. Zaddach, C. Niu, D.L. Irving, C.C. Koch, A Novel Low-Density, High- Hardness, High-entropy Alloy with Close-packed Single-phase Nanocrystalline Structures, Mater. Res. Lett. 3(2) (2014) 95-99.

[24] J.-W. Yeh, Overview of High-Entropy Alloys, in: C.M. Gao, J.-W. Yeh, K.P. Liaw, Y. Zhang (Eds.), High-Entropy Alloys: Fundamentals and Applications, Springer International Publishing, Cham, 2016, pp. 1-19.

[25] J.W. Yeh, S.Y. Chang, Y.D. Hong, S.K. Chen, S.J. Lin, Anomalous decrease in X-ray diffraction intensities of Cu-Ni-Al-Co-Cr-Fe-Si alloy systems with multi-principal elements,

Mater. Chem. Phys. 103(1) (2007) 41-46.

[26] Y.F. Ye, C.T. Liu, Y. Yang, A geometric model for intrinsic residual strain and phase stability in high entropy alloys, Acta Mater. 94 (2015) 152-161.

[27] E.J. Pickering, N.G. Jones, High-entropy alloys: a critical assessment of their founding principles and future prospects, Int. Mater. Rev. (2016) 1-20.

[28] U. Dahlborg, J. Cornide, M. Calvo-Dahlborg, T.C. Hansen, A. Fitch, Z. Leong, S. Chambreland, R. Goodall, Structure of some CoCrFeNi and CoCrFeNiPd multicomponent HEA alloys by diffraction techniques, J. Alloys Compd. 681 (2016) 330-341.

[29] I. Toda-Caraballo, J.S. Wróbel, S.L. Dudarev, D. Nguyen-Manh, P.E.J. Rivera-Díaz-del- Castillo, Interatomic spacing distribution in multicomponent alloys, Acta Mater. 97 (2015) 156-169.

[30] C.J. Tong, Y.L. Chen, S.K. Chen, J.W. Yeh, T.T. Shun, C.H. Tsau, S.J. Lin, S.Y. Chang, Microstructure characterization of AlxCoCrCuFeNi high-entropy alloy system with multiprincipal elements, Metall. Mater. Trans. A 36(4) (2005) 881-893.

[31] C.W. Tsai, M.H. Tsai, J.W. Yeh, C.C. Yang, Effect of temperature on mechanical properties of Al0.5CoCrCuFeNi wrought alloy, J. Alloys Compd. 490(1-2) (2010) 160-165.

[32] J.W. Yeh, S.K. Chen, J.Y. Gan, S.J. Lin, T.S. Chin, T.T. Shun, C.H. Tsau, S.Y. Chang, Formation of simple crystal structures in Cu-Co-Ni-Cr-Al-Fe-Ti-V alloys with multiprincipal metallic elements, Metall Mater Trans A 35 A(8) (2004) 2533-2536.

[33] Y. Zou, S. Maiti, W. Steurer, R. Spolenak, Size-dependent plasticity in an Nb25Mo25Ta25W25 refractory high-entropy alloy, Acta Mater. 65 (2014) 85-97.

[34] L.J. Santodonato, Y. Zhang, M. Feygenson, C.M. Parish, M.C. Gao, R.J. Weber, J.C. Neuefeind, Z. Tang, P.K. Liaw, Deviation from high-entropy configurations in the atomic

distributions of a multi-principal-element alloy, Nat. Commun. 6 (2015) 5964.

[35] H. Oh, D. Ma, G. Leyson, B. Grabowski, E. Park, F. Körmann, D. Raabe, Lattice Distortions in the FeCoNiCrMn High Entropy Alloy Studied by Theory and Experiment, Entropy 18(9) (2016) 321.

[36] G. Kresse, J. Furthmüller, Efficient iterative schemes for *ab initio* total-energy calculations using a plane-wave basis set, Physical Review B 54(16) (1996) 11169-11186.

[37] G. Kresse, J. Hafner, *Ab initio* molecular dynamics for liquid metals, Physical Review B 47(1) (1993) 558-561.

[38] G. Kresse, D. Joubert, From ultrasoft pseudopotentials to the projector augmented-wave method, Physical Review B 59(3) (1999) 1758-1775.

[39] P.E. Blöchl, Projector augmented-wave method, Physical Review B 50(24) (1994) 17953-17979.

[40] J.P. Perdew, K. Burke, M. Ernzerhof, Generalized Gradient Approximation Made Simple, Phys. Rev. Lett. 77(18) (1996) 3865-3868.

[41] H.J. Monkhorst, J.D. Pack, Special points for Brillouin-zone integrations, Phys.Rev.B 13 (1976) 5188-5192.

[42] A. Zunger, S.H. Wei, L.G. Ferreira, J.E. Bernard, Special quasirandom structures, Phys. Rev. Lett. 65(3) (1990) 353-356.

[43] A. van de Walle, P. Tiwary, M. de Jong, D.L. Olmsted, M. Asta, A. Dick, D. Shin, Y. Wang, L.Q. Chen, Z.K. Liu, Efficient stochastic generation of special quasirandom structures, Calphad 42 (2013) 13-18.

[44] F. Birch, Finite Elastic Strain of Cubic Crystals, Physical Review 71(11) (1947) 809-824.

[45] F.D. Murnaghan, Am. J. Math. 49 (1937) 235.

[46] F.Y. Tian, L.K. Varga, N.X. Chen, L. Delczeg, L. Vitos, Ab initio investigation of high-entropy alloys of 3d elements, Physical Review B 87(7) (2013) 075144.

[47] A.J. Zaddach, C. Niu, C.C. Koch, D.L. Irving, Mechanical Properties and Stacking Fault Energies of NiFeCrCoMn High-Entropy Alloy, JOM 65(12) (2013) 1780-1789.

[48] G. Grimvall, CHAPTER 3 - ELASTICITY. BASIC RELATIONS, Thermophysical Properties of Materials, Elsevier Science B.V., Amsterdam, 1999, pp. 27-45.

[49] D. Ma, B. Grabowski, F. Körmann, J. Neugebauer, D. Raabe, Ab initio thermodynamics of the CoCrFeMnNi high entropy alloy: Importance of entropy contributions beyond the configurational one, Acta Mater. 100 (2015) 90-97.

[50] G. Laplanche, P. Gadaud, O. Horst, F. Otto, G. Eggeler, E.P. George, Temperature dependencies of the elastic moduli and thermal expansion coefficient of an equiatomic, single-phase CoCrFeMnNi high-entropy alloy, J. Alloys Compd. 623 (2015) 348-353.

[51] M.S. Lucas, L. Mauger, J.A. Muñoz, Y. Xiao, A.O. Sheets, S.L. Semiatin, J. Horwath, Z. Turgut, Magnetic and vibrational properties of high-entropy alloys, J. Appl. Phys. 109(7) (2011) 07E307.

[52] M.S. Lucas, D. Belyea, C. Bauer, N. Bryant, E. Michel, Z. Turgut, S.O. Leontsev, J. Horwath, S.L. Semiatin, M.E. McHenry, C.W. Miller, Thermomagnetic analysis of FeCoCrxNi alloys: Magnetic entropy of high-entropy alloys, J. Appl. Phys. 113(17) (2013) 17A923.

[53] L.A.A. Warnes, H.W. King, The low temperature magnetic properties of austenitic Fe-Cr-Ni alloys: 2. The prediction of Néel temperatures and maximum susceptibilities, Cryogenics 16(11) (1976) 659-667.

[54] Y. Zhang, T.T. Zuo, Y. Cheng, P.K. Liaw, High-entropy Alloys with High Saturation Magnetization, Electrical Resistivity, and Malleability, Sci. Rep. 3 (2013) 1455.

[55] C. Jiang, B.P. Uberuaga, Efficient Ab initio Modeling of Random Multicomponent Alloys,
Phys. Rev. Lett. 116(10) (2016) 105501.

[56] F. Otto, A. Dlouhý, K.G. Pradeep, M. Kuběňová, D. Raabe, G. Eggeler, E.P. George,
Decomposition of the single-phase high-entropy alloy CrMnFeCoNi after prolonged anneals at
intermediate temperatures, Acta Mater. 112 (2016) 40-52.

[57] T.F. Fässler, U. Häussermann, R. Nesper, Visualization of Tight-Binding Calculations–The
Electronic Structure and Electron Localization of the Si(100) Surface, Chemistry – A European
Journal 1(9) (1995) 625-633.

[58] F. Shimizu, S. Ogata, J. Li, Theory of Shear Banding in Metallic Glasses and Molecular
Dynamics Calculations, MATERIALS TRANSACTIONS 48(11) (2007) 2923-2927.

[59] L.M. Kachanov, Fundamentals of the Theory of Plasticity, Dover Publications2004.

[60] S. Froyen, C. Herring, Distribution of interatomic spacings in random alloys, J. Appl. Phys.
52(12) (1981) 7165-7173.

[61] Y.F. Ye, X.D. Liu, S. Wang, C.T. Liu, Y. Yang, The general effect of atomic size misfit on
glass formation in conventional and high-entropy alloys, Intermetallics 78 (2016) 30-41.

[62] L.R. Owen, E.J. Pickering, H.Y. Playford, H.J. Stone, M.G. Tucker, N.G. Jones, An
assessment of the lattice strain in the CrMnFeCoNi high-entropy alloy, Acta Mater. 122 (2017)
11-18.

[63] C. Niu, A.J. Zaddach, A.A. Oni, X. Sang, J.W. Hurt, J.M. LeBeau, C.C. Koch, D.L. Irving,
Spin-driven ordering of Cr in the equiatomic high entropy alloy NiFeCrCo, Appl. Phys. Lett.
106(16) (2015) 161906.

[64] V. Ozoliņš, C. Wolverton, A. Zunger, Cu-Au, Ag-Au, Cu-Ag, and Ni-Au intermetallics:
First-principles study of temperature-composition phase diagrams and structures, Physical

Review B 57(11) (1998) 6427-6443.

[65] Q. Peng, W. Ji, S. De, First-principles study of the effects of mechanical strains on the radiation hardness of hexagonal boron nitride monolayers, Nanoscale 5(2) (2013) 695-703.

### List of Table Captions

Table 1 The lattice constants, elastic constants, polycrystalline Poisson's ratio $v$ as well as the effective strain $\gamma$ for the various alloys and pure elements obtained from the DFT simulations at T = 0 K compared with those obtained from our elastic theory. The pristine lattice refers to the ideal reference FCC structure without distortion while the distorted one refers to the distorted FCC structure after relaxation.

# List of Figure Captions

Figure 1. The results of the DFT simulation on the FCC FeCoNiCr alloy. (a) atoms of the pristine structure occupies the ideal lattice positions, which subsequently stray from their ideal positions after lattice distortion in (b). In the 3D configurations, white balls stand for Fe, blue ones for Co, red ones for Ni and yellow ones for Cr. The simulated XRD results of the pristine structure (black dash line) as well as the distorted structure (red solid line) are shown in (c).

Figure 2. Theoretical XRD of (a) Fe (b) Cr (c) Ni (d) Co and (e) Mn with FCC structure.

Figure 3. (a) and (b) show the contour plots of the partial electron density (PED) of the pristine structure and the distorted structure, respectively. The black circles in (b) highlight the distorted electron cloud frontiers. Note the colors in the center of each atom are only used to lable different elements, which do not provide any PED information. All are derived from the (001) plane in FCC FeCoNiCr.

Figure 4. The contour plots of the local atomic strain tensor components derived from the (001) plane in the FCC FeCoNiCr. Here the contour images were plotted following the way in Ref. [65].

Figure 5. The distributions of the local atomic strain tensor components in FCC FeCoNiCr.

Figure 6. (a) and (b) show the $\gamma_i^{eq}$ contour map of the pristine structure and the distorted structure, respectively. All are derived from the (001) plane in FCC FeCoNiCr and the contour images were plotted following the method in Ref. [65].

Figure 7. The schematics demonstrates the transition of a pristine structure to a distorted structure. In principle, the pristine structure corresponds to the configuration with the lowest energy state with local shear being prohibited. Distortion becomes energetically favorable only when local shear relaxes part of the radial strains developed in the pristine structure.

Figure 8. (a) The equivalent strain $\gamma^{DFT}$ obtained through the simulations for the distorted atomic structure can be well predicted by our theoretical model, with or without considering magnetism. (b) $\gamma^{DFT}$ is in good correlation with $f(v)\delta$, where $f(v)$ is the function of Poisson's ratio as defined in the main text.

Figure 9. The DFT derived lattice constant can be well predicted by our theoretical model.

Figure 10. The correlation between the experimentally derived lattice friction and the lattice distortion characterized by the product of elastic constants and equivalent strain.

Figure 11. The comparison of the distribution of $\gamma_{i}^{eq}$ around each atom with and without considering the magnetic effect. The solid line is the visual guide for the $\gamma_{i}^{eq}$ distribution considering magnetism while the dash line is for the $\gamma_{i}^{eq}$ distribution without considering magnetism.

Table 1 The lattice constants, elastic constants, polycrystalline Poisson's ratio $v$ as well as the effective strain $\gamma$ for the various alloys and pure elements obtained from the DFT simulations at T = 0 K compared with those obtained from our elastic theory. The pristine lattice refers to the ideal reference FCC structure without distortion while the distorted one refers to the distorted FCC structure after relaxation.

<table>
<thead>
<tr>
<th rowspan="2">Composition</th>
<th colspan="6">DFT Simulation @$T=0$ K</th>
<th colspan="3">Continuum<br>Elastic Theory</th>
</tr>
<tr>
<th>$a^{DFT}$<br>(Å)<br>pristine</th>
<th>$a^{DFT}$ (Å)<br>distorted</th>
<th>$c_{11}$<br>(GPa)</th>
<th>$c_{12}$<br>(GPa)</th>
<th>$v$</th>
<th>$\gamma^{DFT}$</th>
<th>$a^{th}$ (Å)<br>pristine</th>
<th>$a^{th}$ (Å)<br>distorted</th>
<th>$\gamma^{th}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Fe</td>
<td>3.4476</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Cr</td>
<td>3.6189</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Ni</td>
<td>3.5031</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Co</td>
<td>3.4549</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>Mn</td>
<td>3.5023</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
</tr>
<tr>
<td>FeNi</td>
<td>3.4775</td>
<td>3.4751</td>
<td>249</td>
<td>72</td>
<td>0.21</td>
<td>0.0161</td>
<td>3.4715</td>
<td>3.4716</td>
<td>0.0079</td>
</tr>
<tr>
<td>FeCr</td>
<td>3.5294</td>
<td>3.5292</td>
<td>208</td>
<td>113</td>
<td>0.35</td>
<td>0.0367</td>
<td>3.5278</td>
<td>3.5281</td>
<td>0.0369</td>
</tr>
<tr>
<td>FeCo</td>
<td>3.4499</td>
<td>3.4495</td>
<td>283</td>
<td>38</td>
<td>0.19</td>
<td>0.0054</td>
<td>3.4493</td>
<td>3.4493</td>
<td>0.0012</td>
</tr>
<tr>
<td>CoNi</td>
<td>3.4848</td>
<td>3.4805</td>
<td>231</td>
<td>89</td>
<td>0.22</td>
<td>0.0147</td>
<td>3.4759</td>
<td>3.4759</td>
<td>0.0068</td>
</tr>
<tr>
<td>CoCr</td>
<td>3.5272</td>
<td>3.5262</td>
<td>216</td>
<td>104</td>
<td>0.24</td>
<td>0.0232</td>
<td>3.5324</td>
<td>3.5327</td>
<td>0.0254</td>
</tr>
<tr>
<td>FeCoNi</td>
<td>3.4704</td>
<td>3.4684</td>
<td>252</td>
<td>68</td>
<td>0.21</td>
<td>0.0153</td>
<td>3.4655</td>
<td>3.4655</td>
<td>0.0069</td>
</tr>
<tr>
<td>FeCoCr</td>
<td>3.5003</td>
<td>3.4999</td>
<td>236</td>
<td>84</td>
<td>0.22</td>
<td>0.0194</td>
<td>3.5024</td>
<td>3.5026</td>
<td>0.0238</td>
</tr>
<tr>
<td>FeCrNi</td>
<td>3.5173</td>
<td>3.5157</td>
<td>220</td>
<td>100</td>
<td>0.23</td>
<td>0.0213</td>
<td>3.5180</td>
<td>3.5182</td>
<td>0.0220</td>
</tr>
<tr>
<td>CoNiCr</td>
<td>3.5179</td>
<td>3.5153</td>
<td>221</td>
<td>100</td>
<td>0.23</td>
<td>0.0237</td>
<td>3.5210</td>
<td>3.5212</td>
<td>0.0210</td>
</tr>
<tr>
<td>FeCoNiCr</td>
<td>3.4998</td>
<td>3.4984</td>
<td>240</td>
<td>81</td>
<td>0.22</td>
<td>0.0170</td>
<td>3.5015</td>
<td>3.5016</td>
<td>0.0204</td>
</tr>
<tr>
<td>FeCoNiCrMn</td>
<td>3.4993</td>
<td>3.4981</td>
<td>222</td>
<td>98</td>
<td>0.21</td>
<td>0.0167</td>
<td>3.5015</td>
<td>3.5020</td>
<td>0.0179</td>
</tr>
</tbody>
</table>

<table>
<tr>
<td>FeCoNi<br>(mag.)*</td>
<td>3.5521</td>
<td>3.5473</td>
<td>210</td>
<td>111</td>
<td>0.24</td>
<td>0.0139</td>
<td>3.4655</td>
<td>3.4655</td>
<td>0.0074</td>
</tr>
<tr>
<td>FeCrNi<br>(mag.)*</td>
<td>3.5467</td>
<td>3.5443</td>
<td>201</td>
<td>120</td>
<td>0.22</td>
<td>0.0198</td>
<td>3.5180</td>
<td>3.5182</td>
<td>0.0215</td>
</tr>
<tr>
<td>FeCoNiCr<br>(mag.)*</td>
<td>3.5296</td>
<td>3.5276</td>
<td>216</td>
<td>104</td>
<td>0.21</td>
<td>0.0177</td>
<td>3.5015</td>
<td>3.5016</td>
<td>0.0200</td>
</tr>
<tr>
<td>FeCoNiCrMn<br>(mag.)*</td>
<td>3.5304</td>
<td>3.5292</td>
<td>204</td>
<td>116</td>
<td>0.19</td>
<td>0.0165</td>
<td>3.5015</td>
<td>3.5020</td>
<td>0.0172</td>
</tr>
</table>

*For these alloys, magnetism effect was taken into consideration.

![](./images/813052318441275393_3.jpg)

![](./images/813052318441275393_4.jpg)

Figure 1. The results of the DFT simulation on the FCC FeCoNiCr alloy. (a) atoms of the pristine structure occupies the ideal lattice positions, which subsequently stray from their ideal positions after lattice distortion in (b). In the 3D configurations, white balls stand for Fe, blue ones for Co, red ones for Ni and yellow ones for Cr. The simulated XRD results of the pristine structure (black dash line) as well as the distorted structure (red solid line) are shown in (c).

![](./images/813052318441275393_5.jpg)

Figure 2. Theoretical XRD of (a) Fe (b) Cr (c) Ni (d) Co and (e) Mn with FCC structure.

![](./images/813052318441275393_6.jpg)

Figure 3. (a) and (b) show the contour plots of the partial electron density (PED) of the pristine structure and the distorted structure, respectively. The black circles in (b) highlight the distorted electron cloud frontiers. Note the colors in the center of each atom are only used to lable different elements, which do not provide any PED information. All are derived from the (001) plane in FCC FeCoNiCr.

![](./images/813052318441275393_7.jpg)

Figure 4. The contour plots of the local atomic strain tensor components derived from
the (001) plane in the FCC FeCoNiCr. Here the contour images were plotted
following the way in Ref. [65].

![](./images/813052318441275393_8.jpg)

Figure 5. The distributions of the local atomic strain tensor components in FCC FeCoNiCr.

![](./images/813052318441275393_9.jpg)

Figure 6. (a) and (b) show the $\gamma_i^{eq}$ contour map of the pristine structure and the
distorted structure, respectively. All are derived from the (001) plane in FCC
FeCoNiCr and the contour images were plotted following the method in Ref. [65].

![](./images/813052318441275393_10.jpg)

Figure 7. The schematics demonstrates the transition of a pristine structure to a distorted structure. In principle, the pristine structure corresponds to the configuration with the lowest energy state with local shear being prohibited. Distortion becomes energetically favorable only when local shear relaxes part of the radial strains developed in the pristine structure.

![](./images/813052318441275393_11.jpg)

Figure 8. (a) The equivalent strain $\gamma^{DFT}$ obtained through the simulations for the distorted atomic structure can be well predicted by our theoretical model, with or without considering magnetism. (b) $\gamma^{DFT}$ is in good correlation with $f(v)\delta$, where $f(v)$ is the function of Poisson's ratio as defined in the main text.

![](./images/813052318441275393_12.jpg)

Figure 9. The DFT derived lattice constant can be well predicted by our theoretical model.

![](./images/813052318441275393_13.jpg)

Figure 10. The correlation between the experimentally derived lattice friction and the lattice distortion characterized by the product of elastic constants and equivalent strain.

![](./images/813052318441275393_14.jpg)

Figure 11. The comparison of the distribution of $\gamma_{i}^{eq}$ around each atom with and without considering the magnetic effect. The solid line is the visual guide for the $\gamma_{i}^{eq}$ distribution considering magnetism while the dash line is for the $\gamma_{i}^{eq}$ distribution without considering magnetism.