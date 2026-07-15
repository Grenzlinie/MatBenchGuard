
# Size-effects on shift-current in layered CuInP_{2}S_{6}

Francesco Delodovici, \( ^{*,\dagger} \)  Brahim Dkhil, \( ^{\dagger} \)  and Charles Paillard \( ^{*,\ddagger} \) 

 \( ^{\dagger} \) Université Paris-Saclay, CentraleSupelec, CNRS, Laboratoire SPMS, 91190,

Gif-sur-Yvette, France

 \( ^{\dagger} \) Smart Ferroic Materials center and Institute for Nanoscience & Engineering, Department

of Physics, University of Arkansas, Fayetteville, Arkansas 72701, USA

E-mail: francesco.delodovici@centralesupelec.fr; paillard@uark.edu

## Abstract

Two-dimensional ferroelectrics have recently emerged as a promising avenue for next-generation optoelectronic and photovoltaic devices. Due to the intrinsic absence of inversion symmetry, 2D ferroelectrics exhibit bulk photovoltaic effect (BPVE), which relies on hot, non-thermalized photo-excited carriers to generate a photo-induced current with enhanced performances thanks to efficient charge separation mechanisms. The absence of a required p-n junction architecture makes these materials particularly attractive for nanoscale energy harvesting. Recent studies have reported enhanced BPVE in nanometer-thick  \( CuInP_{2}S_{6} \)  ferroelectric embedded between two graphene wafers, driven by relatively strong polarization and reduced dimensionality. Short circuit photocurrent density values have been observed to reach up to mA/cm \( ^{2} \) . In this paper, we demonstrate that the shift-current mechanism alone cannot fully account for these high conductivity values, suggesting that additional mechanisms may play a significant role. Furthermore, our work confirms the existence of a strong size effect, which drastically reduces the shift-conductivity response in the bulk limit, in agreement with experimental observations.
 

## 1 Introduction

The bulk photovoltaic effect (BPVE) \( ^{1} \)  is a nonlinear optical phenomenon that enables highly efficient charge generation, potentially exceeding the Schockley–Queisser limit. \( ^{2,3} \)  Unlike conventional photovoltaic mechanisms requiring p-n junction interfaces, BPVE does not require any built-in electric fields, as photocurrent is intrinsically generated in materials that break inversion symmetry. This makes BPVE particularly attractive for next-generation optoelectronic and energy-harvesting technologies. Among materials hosting BPVE, two-dimensional van der Waals ferroelectrics \( ^{4} \)  have recently emerged as a promising platform for novel optoelectronics applications. Besides the theoretical interest for their rich physics, \( ^{5-9} \)  their peculiar atomic arrangements made by strong covalent bonds in-plane and weak bonds out-of-plane, makes them CMOS-compatible and integrable with a vast range of materials, such as common semiconductor substrates such as silicon or gallium arsenide, with limited interfacial issues. In particular in the field of photovoltaic energy conversion, they hold the potential for significant breakthroughs. On the one hand, they can be integrated in modern photovoltaic architectures, such as tandem-cells, \( ^{10,11} \)  to minimize recombination losses and improve overall efficiency. On the other hand, they exhibit a BPVE with remarkably high performances, \( ^{12-14} \)  offering an alternative or complementary route to efficient charge generation beyond conventional semiconductor-based approaches. It is the case, for instance, with CuInP \( _{2} \) S \( _{6} \) , recently recognized for hosting a large photocurrent density, \( ^{15} \)  up to mA/cm \( ^{2} \) , when embedded between two layers of graphene and illuminated by linearly polarized light. However, current synthesis techniques seldom allow for the reproducible growth of perfect 2D ferroelectric monolayers on a large surface area, but rather isolated islands or films with a strong dispersion in thickness. It is thus very important to (1) quantify to what extent the BPVE, and in particular the shift current mechanism, contributes to the large photovoltaic response of CuInP \( _{2} \) S \( _{6} \) , (2) evaluate the role of sample thickness on the BPVE shift response, and determine whether there exists an optimal thickness yielding a maximal shift current output. In this work, we investigate the origin of these large photocurrent responses using a
 

Density Functional Theory based approach, which indicates that the shift-current mechanism alone is insufficient to explain the observed conductivity values. Our findings indicate that additional mechanisms contribute significantly, highlighting the need for further theoretical investigation. Furthermore, we confirm a pronounced size effect, where the shift-current response diminishes in the bulk limit, aligning with experimental observations. \( ^{15} \)  These insights provide a deeper understanding of BPVE in 2D ferroelectrics and its potential for future optoelectronic applications.

## 2 System and methods

CuInP \( _{2} \) S \( _{6} \)  (CIPS) is a van der Waal layered material showing a ferroelectric phase transition at around 315 K. \( ^{16} \)  Following a second-order Jahn-Teller distortion coupling 3d \( ^{10} \)  and 4s \( ^{0} \)  orbitals in Cu and In, the resulting dipole ordering can be described as an antiparallel displacement of Cu \( ^{+} \)  and In \( ^{3+} \)  cations from the center of the surrounding sulfur framework. The asymmetry in the displacements of these ions results in a sizable reversible polarization of about 3.5  \( \mu \) C/cm \( ^{2} \)  at room temperature. \( ^{16-18} \)  We performed density functional theory (DFT) simulations with Quantum Espresso, \( ^{19} \)  using PAW pseudopotential \( ^{20} \)  with PBEsol exchange-correlation functional. \( ^{21} \)  The convergence threshold for the self-consistency is set to 10 \( ^{-8} \)  eV. We relaxed the bulk and few-layers slab configurations (1 to 4 layers, representing 20 to 80 atoms) until the forces are smaller than 10 \( ^{-3} \)  eV/Å sampling the first Brillouin zone with a Monkhorst-Pack mesh having a density of at least 200 kpoint×Å \( ^{3} \) . In order to prevent the nonphysical interaction between periodic images, we truncated the Coulomb interaction in the z direction \( ^{22} \)  and added at least 20 Å of vacuum when simulating CIPS slabs. The effect of semiempirical van der Waals corrections \( ^{23} \)  does not significantly affect the electronic properties of the system for the purpose of this study, as detailed in the Supplementary Information. Therefore, we do not include them in our simulations. We calculate the shift current contribution to the BPVE and optical properties by post-processing maximally-
 

localized Wannier orbitals \( ^{24} \)  obtained through Wannier90. \( ^{25} \) 

## 3 Results

## 3.1 Structure and electronic properties

The relaxed bulk primitive cell, reported in panel a of Fig. 1, is characterized by the monoclinic  \( C_{c} \)  space group with primitive lattice parameters  \( a=6.058\ \AA \) ,  \( b=10.490\ \AA \) ,  \( c=13.930\ \AA \)  and  \( \beta=107.12^{\circ} \) , and an inter-layer distance of 3.3 Å. These values are in good agreement with experimental data at room temperature, \( ^{16} \)  showing errors below 3%. In contrast, the agreement with low-temperature values (around 100 K) is slightly less accurate, \( ^{26} \)  in particular for the c lattice parameter, likely showing the increased relevance of van der Waals interactions in determining the structure at lower temperatures. The bulk phase polarization, calculated using the Berry-phase method, \( ^{27} \)  is 3.41  \( \mu \) C/cm \( ^{2} \) , and it is almost parallel to the z-axis, with a minor in-plane component of  \( P_{x}=-0.19\ \mu \) C/cm \( ^{2} \) . The analysis of the polarization, obtained through the Born effective charges, as a function of the number of layers, reported in panel d of Fig.1, shows how thickness reduction enhances the depolarization field, leading to a gradual, and eventually complete, suppression of  \( P_{z} \)  and a strong reduction of  \( P_{x} \) , as reported in Supplementary material. In parallel, the size reduction and corresponding enhanced electrostatic effects also influence the electronic properties, as can be seen in panels b, c and d of Fig. 1. The bulk material exhibits a direct band gap of 1.51 eV, with both the conduction band minimum and valence band maximum located at the  \( \Gamma \)  point. As the thickness decreases, the band gap initially narrows due to the reduced screening of surface charges, inducing an electrostatic shift in the electron states energies. However, when approaching the monolayer limit, quantum confinement dominates, leading to a band gap larger than the bulk value. \( ^{28} \)  Panel c of Fig.1 clearly illustrates the effects of the depolarizing field, showing the energy shift in the orbital-projected density of states (DOS) within the four-layers slab. The dominant orbital character of the intralayer DOS, mainly indium s and sulfur p states
 

a)

![](2512.05796v1-images/4_0.jpg)

b)

![](2512.05796v1-images/4_1.jpg)

![](2512.05796v1-images/4_2.jpg)

![](2512.05796v1-images/4_3.jpg)

Figure 1: a CuInP \( _{2} \) S \( _{6} \)  monoclinic structure: Cu is reported in blue, In in pink, P in grey, S in yellow. b The electronic band structure of the CIPS monolayer, bi-layer, four-layer, bulk configurations. The direct band gap is localized at  \( \Gamma \) . c The atomic orbital projected DOS of the four layer structure. d Top panel: filled central bars represent the Homo-Lumo band gap: the colored labels report the corresponding values; black-border transparent bars represent the intra-layer averaged band gap: 1.34 eV and 1.48 eV respectively for the 2 and 4 layers slabs; transparent bars represent the optical gap extracted with Tauc analysis: 1.65 eV, 1.27 eV, 0.52 eV, 1.49 eV for 1-layer, 2-layer, 4-layers and bulk configurations. Bottom panel: the z component of the polarization as a function of slab thickness. Bulk phase  \( P_{z} \)  obtained with Berry-phase is reported in black; with Born-effective charges in blue; layer-decomposed  \( P_{z} \) : single-layers in yellow, bi-layer in red, 4 layers in green.
 

near the band edges, remains consistent across all layers. The rigid energy shift is consistent with the direction of the polarization, pointing upward in the reported configuration. The average intralayer band-gap, represented by the black-border bars in panel d of figure 1, confirms how the effect of the depolarizing field is larger in the 4 layer configuration, vanishing with  \( P_{z} \)  when approaching thinner slabs. To accurately capture the electronic features across different thicknesses, we performed non-collinear spin-polarized calculations including spin-orbit coupling at every stage. These simulations indicate the presence of a nontrivial spin texture in the valence bands near  \( \Gamma \) , with more pronounced spin splitting emerging at the  \( K_{\pm} \)  points, while the conduction bands remain less affected. More information can be found in the supplementary material. Although these spin features are noteworthy, \( ^{29,30} \)  a detailed analysis lies beyond the scope of this work.

## 3.2 Optical properties

Starting from the Kohn-Sham orbitals, we extracted the maximally-localized Wannier functions to compute the optical properties of various configurations. To recover the effective optical response of the 2D material, we rescaled the obtained numerical results as previously described in, \( ^{[24,31-33]} \)  see supplementary material. We thus obtain:  \( \sigma_{2D}^{\prime\prime}=c/t\cdot\sigma_{SB}^{\prime\prime} \)  and  \( \sigma_{2D}^{\prime}=c/t(\sigma_{SB}^{\prime}-1)+1 \) , where  \( \sigma^{\prime} \)  and  \( \sigma^{\prime\prime} \)  represent respectively the real and the imaginary part of the tensor,  \( \sigma_{SB} \)  and  \( \sigma_{2D} \)  indicate respectively the conductivity computed in the simulation box including vacuum, and the extrapolated 2D one. c and t represent, respectively, the simulation box thickness and the thickness of the slab. To remove the ambiguity in the definition of the 2D material thickness, we set t as the center-to-center distance between the top and the bottom atomic layers in the bulk, multiplied by the number of layers. In our slab models, this averaged value varies by less than 2%.

As the PBEsol functional systematically underestimates the band gap, yielding a value approximately  \( \approx 1.4 \)  eV lower than the experimental bulk-phase gap of  \( \approx 2.9 \)  eV, \( ^{15,34} \)  we apply a scissor shift to all calculated optical spectra to align them with the experimental
 
![](2512.05796v1-images/6_0.jpg)

Figure 2: The imaginary diagonal components of the permittivity tensor for the single layer (yellow, top left panel), bi-layer (red, top right panel), 4-layers (green, bottom left), bulk (blue, bottom right) configurations. Different components are reported with different line styles.
 
![](2512.05796v1-images/7_0.jpg)

![](2512.05796v1-images/7_1.jpg)

![](2512.05796v1-images/7_2.jpg)

![](2512.05796v1-images/7_3.jpg)

![](2512.05796v1-images/7_4.jpg)

![](2512.05796v1-images/7_5.jpg)

![](2512.05796v1-images/7_6.jpg)

![](2512.05796v1-images/7_7.jpg)

![](2512.05796v1-images/7_8.jpg)

Figure 3: The shift current tensor components (in  \( \mu A \cdot V^{-2} \) ) corresponding to light linearly polarized along the lab reference frame axes for the bulk (blue line), 4-layers (green line), bi-layer (red line), mono layer (orange line) configurations.
 
![](2512.05796v1-images/8_0.jpg)

Figure 4: The weighted, and in-plane averaged, shift current density  \( \hat{J}_{k}=\frac{1}{2}(j_{ixx}+j_{iyy}) \)  along x (top panel), y (central panel) and z (bottom panel) directions, to the solar light spectrum when incident along z direction and penetrating a film of: 1 layer of CIPS, 6.7 nm thick (orange), 2 layers (red), 4 layer (green). The bulk case is reported in dashed blue as a comparison.
 

band gap. Figure 2 shows the diagonal elements of the imaginary part of the permittivity as a function of light energy for the monolayer, bilayer, four-layer, and bulk configurations. The spectral profiles remain overall qualitatively similar across different thicknesses, indicating that structural or electronic rearrangement upon thinning down to a few layers does not majorly affect optical properties. Nevertheless, subtle changes emerge as the system approaches the bulk phase: the in-plane components  \( \left(\epsilon_{xx}, \epsilon_{yy}\right) \)  lose distinct features, such as the peak at 3.8 eV and the sharp onset near 3.2 eV, while the out-of-plane component  \( \left(\epsilon_{zz}\right) \)  shows a gradual increase with increasing thickness. Additionally, owing to the surface states near the bottom of the conduction band in the thin-films, the absorption spectra exhibit characteristic low-energy tails, reported in supplementary materials, that are completely absent in the bulk profile. Regardless of thickness, the systems display a pronounced anisotropic optical response. The out-of-plane component of the permittivity is consistently smaller than its in-plane counterpart. This anisotropy is further supported by the absorption coefficients given in the supplementary material. Despite its limitations for low-dimensional materials, \( ^{35} \)  Tauc plot analysis \( ^{36} \)  can provide additional insights into the optical properties of the system, owing to the clearly direct character of the gap and to the well-defined parabolic behavior of the bands near the edges. Our Tauc plot analysis, detailed in the supplementary material, confirms the presence of a slight anisotropy in the optical band gap. This directional dependence reflects the layered structure of the material, indicating distinct contributions from interlayer and intralayer transitions to the optical absorption behavior, as evidenced for instance by the shifted density of states in Fig.1. The values reported in panel d of Fig.1 indicated by semi-transparent bars and representing the average optical band-gap, are in close agreement with the Homo-Lumo band gap estimate, within the fitting uncertainties (not shown for clarity).

Let us now focus to the shift current tensor in CIPS. Figure 3 displays the shift-current response  \( \sigma_{ikk} \)  to linearly polarized light, in the case of mono-layer, bi-layer, four-layers and bulk CIPS. It is known that the shift current is larger for systems showing strong covalent bonds,
 

highly delocalized orbitals \( ^{37,38} \)  and large anisotropy. In the case of van der Waals materials, due to their weakly interacting layered structure, the shift-current response to electric field polarized along the stacking direction is expected to be small, even vanishing. Our results confirm this interpretation, see e.g.  \( \sigma_{izz} \)  in Fig.3. Some weak contribution appears in  \( \sigma_{izz} \)  for the 4-layers and the bulk configurations, likely produced by constructive interference of intralayer optical transitions. Interestingly, different conductivity components do not evolve in the same way with respect to the thickness. For instance, the elements corresponding to out-of-plane transport produced by in-plane polarized field, i.e.  \( \sigma_{zii} \) , increase with the number of layers well above the bulk value. This suggests the existence of an optimal number of layer maximizing the out-of-plane response of the system. On the other hand, the other components gradually evolve towards the bulk value. To analyze the true solar-harvesting potential of CIPS in photovoltaic applications, we linked the shift conductivity to solar light absorption and to the film thickness by constructing an appropriate figure-of-merit  \( \bar{j} \) . We take the in-plane average of the conductivity weighted by the Planck distribution \( ^{39} \)  and by the light intensity profile as a function of in-film depth, and integrate over the light energy and on film thickness. More details can be found in the supplementary material. Notably, as reported in Figure 4, while the integrated conductivity remains relatively flat in both the mono-layer and bulk configurations, with values barely exceeding a few  \( 10^{-4}A\cdotm^{-2} \) , the bi-layer and, in particular, the four-layer exhibit a markedly enhanced profile. The behavior of a four-layers and bi-layers subjected to an in-plane oscillating electric field, represented by  \( \bar{j}_{z} \) , distinctly stands out from the rest, increasing monotonically from 3.25 eV onward and reaching  \( 10^{-2}A/m^{2} \) . This trend can be deduced from the behavior of the shift conductivity. The conductivity elements associated with transport along the stacking direction exhibit a constant sign as frequency varies, adding up constructively in the integration and producing the linear behavior reported in Figure 4. In contrast, the pronounced oscillations in the  \( \sigma_{ykk} \)  components prevents it from converging to a finite value when integrated. The behavior of  \( \sigma_{xkk} \)  lies in between these two cases. Although they do not exhibit strong oscillations,  \( \sigma_{xxx} \)
 

and  \( \sigma_{xyy} \)  maintain opposite signs across the entire energy range considered. As a result, they interfere destructively when added. As an alternative approach to evaluate the BPVE performances of few-layers CIPS, we computed the Glass coefficient \( ^{37,40} \)  as the frequency-dependent ratio between the shift current and the absorbed light. The results, reported in supplementary, confirm that the few-layer configuration is best suited to effectively converts light into current via the shift-current mechanism.

## 4 Discussion

Our simulations confirm the strong dimensionality effect of BPV response in  \( CuInP_{2}S_{6} \) , in agreement with previous experimental findings. In a real system, this intuitively stems from the fact that the thickness of the device, which corresponds approximately to the distance between the electrodes, is comparable to the carriers mean free-path, estimated \( ^{15} \)  to 40 nm in CIPS, which increases the transport efficiency. In contrast, our work shows that this effect is also present in ideal systems, e.g. surrounded by vacuum, showing that this enhancement is probably also due to intrinsic effects, \( ^{41} \)  ultimately depending on the specificity of the bands structure rather than to the polarization magnitude, as reported in supplementary material. Nonetheless, our simulations show that, although it has a non-negligible contribution to the overall BPVE, the shift current is probably not the main contributor to the reported large photocurrent density. \( ^{15} \)  Indeed, the computed integrated shift-conductivity in the four/bilayers is about one order of magnitude larger than the bulk one, in contrast to the three orders of magnitude increase reported in the literature. The remarkable results observed for bilayer CIPS placed between two graphene electrodes may thus arise from interface-induced band bending, which leads to a conventional (Schottky interface-driven junction) photovoltaic effect rather than a bulk one. To achieve a deeper comprehension and a better control of the BPV effect in CIPS, it would be important to investigate all contributions from the ballistic current too, including phonon-assisted mechanisms, \( ^{42} \)  as well as those arising
 

from quasiparticle \( ^{43} \)  and excitons \( ^{44} \)  effects, although to-date, these effects have not proven to enhance the shift current by two orders of magnitude, to our knowledge. The relevance of the latter in 2D materials is still debated, even though it has proven to be of major importance in some recent work. \( ^{45,46} \)  Moreover,  \( Cu^{+} \) ion migration could also contribute through ionic conduction or charge accumulation at the CIPS-electrode interfaces. Finally, as reported in supplementary material, we find that spin-orbit coupling substantially improves the photovoltaic response of the system, highlighting its critical influence on nonlinear optical properties. This suggests that SOC-driven effects may be leveraged to further optimize BPVE performances. Finally, provided that spin transport is properly defined in SOC systems, few-layer CIPS may constitute a promising platform for investigating spin-BPVE and spintronics phenomena.

## Acknowledgements

C.P. acknowledges support from the Air Force Office of Scientific Research through Award No. FA9550-24-1-0263. F.D. and B.D. thank Agence Nationale de la Recherche for financial support through grant agreement no. ANR-23-CE09-0007 (SOFIANE) and n° ANR-24-CE08-0954-03 (PHOTOTRICS).

## References

(1) Sturman, B. I.; Fridkin, V. M. The Photovoltaic and Photorefractive Effects in Noncentrosymmetric Materials; Gordon and Breach Science Publishers, 1992.

(2) Shockley, W.; Queisser, H. J. Detailed Balance Limit of Efficiency of p-n Junction Solar Cells. J. Appl. Phys. 1961, 32, 510.

(3) Spanier, J. E.; Fridkin, V. M.; Rappe, A. M.; Akbashev, A. R.; Polemi, A.; Qi, Y.; Gu, Z.; Young, S. M.; Hawley, C. J.; Imbrenda, D.; Xiao, G.; Bennett-Jackson, A. L.;
 

Johnson, C. L. Power conversion efficiency exceeding the Shockley–Queisser limit in a ferroelectric insulator. Nature Photonics 2016, 10, 611–616.

(4) Zhang, D.; Schoenherr, P.; Sharma, P.; Seidel, J. Ferroelectric order in van der Waals layered materials. Nat. Rev. Mater. 2023, 8, 25–40.

(5) Xiao, R.-C.; Gao, Y.; Jiang, H.; Gan, W.; Zhang, C.; Li, H. Non-synchronous bulk photovoltaic effect in two-dimensional interlayer-sliding ferroelectrics. npj Computational Materials 2022, 8, 138.

(6) Kim, J.; Kim, K.-W.; Shin, D.; Lee, S.-H.; Sinova, J.; Park, N.; Jin, H. Prediction of ferroelectricity-driven Berry curvature enabling charge-and spin-controllable photocurrent in tin telluride monolayers. Nature communications 2019, 10, 3965.

(7) Swamynadhan, M.; Ghosh, S. Designing multifunctional two-dimensional layered transition metal phosphorous chalcogenides. Phys. Rev. Mater. 2021, 5, 054409.

(8) Liu, F.; You, L.; Seyler, K. L.; Li, X.; Yu, P.; Lin, J.; Wang, X.; Zhou, J.; Wang, H.; He, H.; others Room-temperature ferroelectricity in CuInP2S6 ultrathin flakes. Nat. Commun. 2016, 7, 1–6.

(9) Guan, Z.; Hu, H.; Shen, X.; Xiang, P.; Zhong, N.; Chu, J.; Duan, C. Recent Progress in Two-Dimensional Ferroelectric Materials. Adv. Electro. Mater. 2020, 6, 1900818.

(10) Zhang, T.; Luo, H.; Abdi-Jalebi, M.; Chen, H.; Zuo, L. Perovskite solar cells with ferroelectricity. Information & Functional Materials 2024, 1, 87–107.

(11) Li, H.; Zhang, W. Perovskite tandem solar cells: from fundamentals to commercial deployment. Chemical Reviews 2020, 120, 9835–9950.

(12) Aftab, S.; Iqbal, M. Z.; Haider, Z.; Iqbal, M. W.; Nazir, G.; Shehzad, M. A. Bulk Photovoltaic Effect in 2D Materials for Solar-Power Harvesting. Adv. Opt. Mater. 2022, 10, 2201288.
 

(13) Aftab, S.; Shehzad, M. A.; Salman Ajmal, H. M.; Kabir, F.; Iqbal, M. Z.; Al-Kahtani, A. A. Bulk photovoltaic effect in two-dimensional distorted MoTe \( _{2} \) . ACS nano 2023, 17, 17884–17896.

(14) Qiu, D.; Hou, P.; Wang, J.; Ouyang, X. Bulk photovoltaic and photoconductivity effects in two-dimensional ferroelectric CuInP2S6 based heterojunctions. Appl. Phys. Lett. 2023, 123, 111102.

(15) Li, Y.; Fu, J.; Mao, X.; Chen, C.; Liu, H.; Gong, M.; Zeng, H. Enhanced bulk photovoltaic effect in two-dimensional ferroelectric CuInP2S6. Nature communications 2021, 12, 5896.

(16) Maisonneuve, V.; Cajipe, V. B.; Simon, A.; Von Der Muhll, R.; Ravez, J. Ferrielectric ordering in lamellar CuInP2S6. Phys. Rev. B 1997, 56, 10860–10868.

(17) Brehm, J. A.; Neumayer, S. M.; Tao, L.; O'Hara, A.; Chyasnavichus, M.; Susner, M. A.; McGuire, M. A.; Kalinin, S. V.; Jesse, S.; Ganesh, P.; others Tunable quadruple-well ferroelectric van der Waals crystals. Nat. Mater. 2020, 19, 43–48.

(18) Si, M.; Saha, A. K.; Liao, P.-Y.; Gao, S.; Neumayer, S. M.; Jian, J.; Qin, J.; Balke Wisinger, N.; Wang, H.; Maksymovych, P.; others Room-temperature electrocaloric effect in layered ferroelectric CuInP2S6 for solid-state refrigeration. Acs Nano 2019, 13, 8760–8765.

(19) Giannozzi, P. et al. QUANTUM ESPRESSO: a modular and open-source software project for quantum simulations of materials. J. Condens. Matter Phys. 2009, 21, 395502.

(20) Blöchl, P. E. Projector augmented-wave method. Physical review B 1994, 50, 17953.

(21) Perdew, J. P.; Ruzsinszky, A.; Csonka, G. I.; Vydrov, O. A.; Scuseria, G. E.; Con-
 

stantin, L. A.; Zhou, X.; Burke, K. Restoring the Density-Gradient Expansion for Exchange in Solids and Surfaces. Physical Review Letters 2008, 100, 136406.

(22) Sohier, T.; Calandra, M.; Mauri, F. Density functional perturbation theory for gated two-dimensional heterostructures: Theoretical developments and application to flexural phonons in graphene. Phys. Rev. B 2017, 96, 075448.

(23) Grimme, S.; Antony, J.; Ehrlich, S.; Krieg, H. A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu. J. Chem. Phys. 2010, 132, 154104.

(24) Ibañez Azpiroz, J.; Tsirkin, S. S.; Souza, I. Ab initio calculation of the shift photocurrent by Wannier interpolation. Phys. Rev. B 2018, 97, 245143.

(25) Pizzi, G. et al. Wannier90 as a community code: new features and applications. J. Condens. Matter Phys. 2020, 32, 165902.

(26) Susner, M. A.; Chyasnavichyus, M.; Puretzky, A. A.; He, Q.; Conner, B. S.; Ren, Y.; Cullen, D. A.; Ganesh, P.; Shin, D.; Demir, H.; others Cation–eutectic transition via sublattice melting in CuInP2S6/In4/3P2S6 van der Waals layered crystals. ACS nano 2017, 11, 7060–7073.

(27) King-Smith, R. D.; Vanderbilt, D. Theory of polarization of crystalline solids. Phys. Rev. B 1993, 47, 1651–1654.

(28) Liu, K.; Lu, J.; Picozzi, S.; Bellaiche, L.; Xiang, H. Intrinsic Origin of Enhancement of Ferroelectricity in SnTe Ultrathin Films. Phys. Rev. Lett. 2018, 121, 027601.

(29) Zheng, J.-D.; Zhao, Y.-F.; Hu, H.; Shen, Y.-H.; Tan, Y.-F.; Tong, W.-Y.; Xiang, P.-H.; Zhong, N.; Yue, F.-Y.; Duan, C.-G. Ferroelectric control of pseudospin texture in CuInP2S6 monolayer. J. Phys. Condens. Matter 2022, 34, 204001.
 

(30) Picozzi, S. Ferroelectric Rashba semiconductors as a novel class of multifunctional materials. Frontiers in Physics 2014, 2, 10.

(31) Yang, G.; Gao, S.-P. A method to restore the intrinsic dielectric functions of 2D materials in periodic calculations. Nanoscale 2021, 13, 17057–17067.

(32) Mu, X.; Pan, Y.; Zhou, J. Pure bulk orbital and spin photocurrent in two-dimensional ferroelectric materials. npj Computational Materials 2021, 7, 61.

(33) Jiang, Z.; Xiang, H.; Bellaiche, L.; Paillard, C. Electro-optic properties from ab initio calculations in two-dimensional materials. Phys. Rev. B 2024, 109, 165414.

(34) Studenyak, I.; Mitrovcij, V.; Kovacs, G. S.; Gurzan, M.; Mykajlo, O.; Vysochanskii, Y. M.; Cajipe, V. Disordering effect on optical absorption processes in CuInP2S6 layered ferrielectrics. physica status solidi (b) 2003, 236, 678–686.

(35) Klein, J.; Kampermann, L.; Mockenhaupt, B.; Behrens, M.; Strunk, J.; Bacher, G. Limitations of the Tauc Plot Method. Adv. Funct. Mater. 2023, 33, 2304523.

(36) Tauc, J.; Grigorovici, R.; Vancu, A. Optical Properties and Electronic Structure of Amorphous Germanium. Phys. Stat. Sol. (b) 1966, 15, 627–637.

(37) Tan, L.; Zheng, F.; Young, S. M.; Wang, F.; Liu, S.; Rappe, A. M. Shift current bulk photovoltaic effect in polar materials—hybrid and oxide perovskites and beyond. npj Comput. Mater. 2016, 2, 16026.

(38) Tan, L. Z.; Rappe, A. M. Upper limit on shift current generation in extended systems. Phys. Rev. B 2019, 100, 085102.

(39) Delodovici, F.; Paillard, C. Photogalvanic Shift Currents in BiFeO \( _{3} \) -LaFeO \( _{3} \)  Superlattices. ACS Appl. Energy Mater. 2025, 8, 1716–1721.

(40) Glass, A. M.; von der Linde, D.; Negran, T. J. High-voltage bulk photovoltaic effect and the photorefractive process in  \( LiNbO_{3} \) . Appl. Phys. Lett. 2003, 25, 233–235.
 

(41) Cook, A. M.; M. Fregoso, B.; De Juan, F.; Coh, S.; Moore, J. E. Design principles for shift current photovoltaics. Nature communications 2017, 8, 14176.

(42) Dai, Z.; Schankler, A. M.; Gao, L.; Tan, L. Z.; Rappe, A. M. Phonon-Assisted Ballistic Current from First-Principles Calculations. Phys. Rev. Lett. 2021, 126, 177403.

(43) Fei, R.; Tan, L. Z.; Rappe, A. M. Shift-current bulk photovoltaic effect influenced by quasiparticle and exciton. Phys. Rev. B 2020, 101, 045104.

(44) Dai, Z.; Rappe, A. M. First-principles calculation of ballistic current from electron-hole interaction. Phys. Rev. B 2021, 104, 235203.

(45) Esteve-Paredes, J.; García-Blázquez, M.; Uría-Álvarez, A.; Camarasa-Gómez, M.; Palacios, J. Excitons in nonlinear optical responses: shift current in MoS \( _{2} \)  and GeS monolayers. npj Computational Materials 2025, 11, 13.

(46) Lai, M.; Xuan, F.; Quek, S. Y. The Bulk Photovoltaic Effect: Origin of Shift Currents in the Many-Body Picture. arXiv 2024,

(47) Gjerding, M. N. et al. Recent progress of the Computational 2D Materials Database (C2DB). 2D Mater. 2021, 8, 044002.

(48) Curtarolo, S.; Setyawan, W.; Hart, G. L.; Jahnatek, M.; Chepulskii, R. V.; Taylor, R. H.; Wang, S.; Xue, J.; Yang, K.; Levy, O.; Mehl, M. J.; Stokes, H. T.; Demchenko, D. O.; Morgan, D. AFLOW: An automatic framework for high-throughput materials discovery. Comput. Mater. Sci. 2012, 58, 218–226.

## A Structural and electronic properties

In table 1 we report the effect of the van der Waals semi-empirical corrections on the lengths on the primitive cells, the angle  \( \beta \) , the thickness t of the sulfur cage, and the electronic band
 

gap of the bulk phase. Figure 5 reports the effects of these corrections on the band structure of the bulk phase. The path is chosen in the monoclinic setting. Figures 6, 8 reports the spin-resolved band structure of mono-layer and bulk respectively. The  \( \hat{S}_{z} \)  expected value is represented by the color: 1/2 red, -1/2 blue. The inset reports a zoom around  \( \Gamma \)  to better appreciate the spin-texture forming due to broken inversion symmetry. In this case, as in the bands reported in the main text, the path is taken in an equivalent setting, hexagonal in the x-y plane, \( ^{47,48} \)  defined: by a=b=6.06 Å, c=13.46,  \( \alpha=\beta=94.17^{\circ} \) ,  \( \gamma=120^{\circ} \) .

Table 1: Effect of the van der Waals semi-empirical corrections on the primitive cell vectors, monoclinic angle  \( \beta \) , sulfur-cage thickness t, and electronic band gap  \( \Delta \)  in bulk CIPS.

<table><tr><td></td><td>a [Å]</td><td>b [Å]</td><td>c [Å]</td><td>\( \beta \)  [°]</td><td>t [Å]</td><td>\( \Delta \)  [eV]</td></tr><tr><td>no vdW</td><td>6.06</td><td>10.49</td><td>13.93</td><td>107.12</td><td>3.08</td><td>1.52</td></tr><tr><td>Grimme</td><td>6.03</td><td>10.44</td><td>13.48</td><td>107.42</td><td>3.3</td><td>1.55</td></tr></table>

## A.1 Polarization

For the bulk phase the Born effective charges (BEC) underestimate the modulus of the polarization by less than 1%: P is 3.41  \( \mu \) C/cm \( ^{2} \)  with Berry Phase (BP) method against 3.38  \( \mu \) C/cm \( ^{2} \)  with BEC. Nonetheless, effective charges tend to rotate the polarization towards the x axis: for the bulk phase  \( P_{x}^{BP}=-0.19 \)  against  \( P_{x}^{BEC}=-1.06 \) , whereas  \( P_{z}^{BP}=3.4 \)  but  \( P_{z}^{BEC}=3.21 \)   \( \mu \) C/cm \( ^{2} \) . The evolution of  \( P_{z} \)  and  \( P_{x} \)  with layer thickness is reported in Figure 9. In the layer decomposition, we employed the Born effective charges computed for each slab configuration, and we normalized the polarization to the volume of the single bulk layers. The z-component of P computed with the Berry-phase method for the bulk phase is reported as a comparison.

Figure 10 compares the shift current calculated for bi- and four-layer relaxed structures with that obtained from corresponding configurations with frozen bulk ferroelectric displacements. This comparison is aimed at assessing the sensitivity of the shift current to the magnitude of the polarization, and thus to the strength of the depolarizing field. As evident
 

from the figure, the dependence is rather weak: all tensor components largely preserve their shape and magnitude across the different configurations. This supports the notion \( ^{37} \)  that the shift current response has a non-trivial relationship with polarization, that is not solely governed by its magnitude but is instead deeply connected to the topological features of the electronic band structure.

## B Optical properties

## B.1 Wannier orbitals

Figure 11 reports the bands computed with DFT as implemented in Quantum Espresso and those computed via Wannier interpolation with Wannier90 for the bulk phase. The agreement is good over a range of 3-3.5 eV. With the corresponding Wannier orbitals we computed the optical properties.

## B.2 Absorption spectra and Tauc plot

The diagonal component of the absorption spectra are reported in figure 12. The onset of the absorption spectra around the bottom of the valence band are reported in Figure 13. The absorption is obtained by processing the optical conductivity computed by postw90.x.

Figure 14 reports the Tauc interpolation to extract the optical band gap from the absorption profile. The interpolation of  \( (\alpha \cdot h\nu)^{1/2} \)  is performed over the energy windows [2.93, 2.96] eV, [2.93, 3] eV, and [2.9, 2.96] eV for  \( \alpha_{xx} \) ,  \( \alpha_{yy} \)  and  \( \alpha_{zz} \)  respectively. The Tauc analysis reveals the anisotropic nature of the system optical properties. The optical band gap obtained along x and y is respectively  \( 2.92 \pm 0.28 \)  eV and  \( 2.92 \pm 0.2 \)  eV in good agreement with experimental value  \( \approx 2.9 \)  eV. \( ^{15,34} \)  The extrapolation from  \( \alpha_{zz} \)  lead a slightly smaller, but coherent, value:  \( 2.89 \pm 0.17 \)  eV. This is likely due to the spatial separation of the valence and conduction bands. An example of this spatial separation is reported in Figure 1 of main text, even though in that case the spatial separation is enhanced by the
 

presence of the depolarization field.

## B.3 Vacuum effects

Figure 15 reports the effects of different vacuum thickness in the simulation boxes, of the bi-layer slab, on some selected shift conductivity components corresponding to in-plane polarized light, for whom the effect is more evident. In this case the thin film is electrically in parallel with the vacuum, thus in the static limit the conductivity will transform as equation 6 in, \( ^{33} \)  for optical fields it will transform as reported in the main text, see. \( ^{31} \) 

## B.4 Glass coefficient

Figure 16 reports the Glass coefficient under linearly polarized light  \(  G_{ijj}(\omega) = \frac{1}{2c\epsilon_{0}} \frac{\sigma_{ijj}(\omega)}{\alpha_{j}(\omega)}  \)  for the different studied configurations.

## C Figure of merit

The intensity of the electromagnetic field can be written as:

 \[ I(z)=\frac{\epsilon_{0}c n^{\prime}}{2}|E(z)|^{2}=T I_{0}e^{-\alpha\cdot z} \] 

where  \( n' \)  is the real part of the refraction index, c the speed of light,  \( \epsilon_{0} \)  the vacuum permittivity, T the transmission coefficient from air to film,  \( \alpha \)  the absorption coefficient (reported in Fig.12),  \( I_{0} \)  the light intensity at the film surface, and z represents the depth inside the film, taking as zero reference the top surface. The shift current is then:

 \[ j_{s h i f t}^{i}(z)=\sigma_{i j k}\frac{2}{\epsilon_{0}c n^{\prime}}I(z)e_{j}e_{k}. \quad (1) \]
 

Assuming normal incidence of the light ray, and considering the following Plank distribution as the light intensity  \( I_{0} \) :

 \[ \tilde{B}(E,T)=\frac{1}{\hbar}B(\omega,T) \quad (2) \] 

with dimensions of  \( \frac{W}{m^{2}\cdot J} \) , we define the figure of merit as:

 \[ \begin{aligned}\bar{j}_{i,k}^{shift}&=\int_{0}^{\infty}\int_{0}^{t}\sigma_{ikk}(E)\frac{2}{\epsilon_{0}cn^{\prime}(E)}\tilde{B}(E,T)e^{-\alpha(E)\cdot z}TdzdE=\\&=\frac{2}{\epsilon_{0}c}\int_{0}^{\infty}\frac{\sigma_{ikk}(E)}{\alpha_{zz}(E)}\frac{1}{n^{\prime}(E)}\tilde{B}(E,T)\left(1-e^{-\alpha(E)t}\right)dE=\\&=\frac{2}{\epsilon_{0}c}\int_{0}^{\infty}\frac{\sigma_{ikk}(E)}{\alpha_{kk}(E)}\frac{1}{n^{\prime}(E)}\frac{1}{2\pi^{2}\hbar^{3}c^{2}}\frac{E^{3}}{e^{E/K_{B}T}-1}(1-e^{-\alpha(E)t})dE\end{aligned} \quad (3) \] 

where we assumed a transmission coefficient T of 1. This object has the dimensions of  \( \bar{j}^{shift} = \frac{A}{m^{2}} \) , so it correctly represents a current density. The following quantity, averaged over x and y oscillating electric fields:

 \[ \bar{j}_{i}^{s h i f t}=\frac{1}{2}(\bar{j}_{i,x}^{s h i f t}+\bar{j}_{i,y}^{s h i f t}) \quad (4) \] 

corresponds to the quantity shown in Figure 4 in the main manuscript.

Figure 17 reports the effects obtained by introducing SO-coupling in the calculations.
 
![](2512.05796v1-images/22_0.jpg)

Figure 5: The electronic bands with and without vdW semi-empirical corrections in blue and red, respectively.

![](2512.05796v1-images/22_1.jpg)

Figure 6: The spin-resolved electronic band structure of the CIPS mono layer. Red and blue colors represent the up and down spin components respectively. In the inset, a zoom around the  \( \Gamma \)  point is reported to better show the effect of Rashba spin-momentum locking.
 
![](2512.05796v1-images/23_0.jpg)

Figure 7: The spin-resolved electronic band structure of the CIPS bi layer. Red and blue colors represent the up and down spin components respectively. In the inset, a zoom around the  \( \Gamma \)  point is reported to better show the effect of Rashba spin-momentum locking.

![](2512.05796v1-images/23_1.jpg)

Figure 8: The spin-resolved electronic band structure of the CIPS bulk. Red and blue colors represent the up and down spin components respectively. In the inset, a zoom around the  \( \Gamma \)  point is reported to better show the effect of Rashba spin-momentum locking.
 
![](2512.05796v1-images/24_0.jpg)

Figure 9: The z- and x-components of layer-projected polarization are reported.
 
![](2512.05796v1-images/25_0.jpg)

Figure 10: Top panel: relaxed bi-layer shift current (red) compared with shift current of bi-layer with ferroelectric displacements frozen to bulk value (blue). Bottom panel: relaxed four-layer shift current (red) compared with shift current of four-layer with ferroelectric displacements frozen to bulk value (blue).
 
![](2512.05796v1-images/26_0.jpg)

Figure 11: The electronic bands of the bulk configuration computed with DFT (black) and Wannier interpolation (red dashed).
 
![](2512.05796v1-images/27_0.jpg)

![](2512.05796v1-images/27_1.jpg)

![](2512.05796v1-images/27_2.jpg)

Figure 12: The diagonal components of the absorption tensor for bulk (blue line), four-layers (green), bi-layer (red), mono layer (yellow) configurations.
 
![](2512.05796v1-images/28_0.jpg)

Figure 13: A zoom of the xx component of the absorption tensor around the minimum of the valence bands, for bulk (blue line), four-layers (green), bi-layer (red), mono layer (yellow) configurations. The inset shows the small contribution of the bottom of the conduction bands in the 4-layer slab.

![](2512.05796v1-images/28_1.jpg)

Figure 14: Tauc plot used to extract the optical band-gap for bulk configuration along the three cartesian directions.
 
![](2512.05796v1-images/29_0.jpg)

Figure 15: The effect of the simulation-box size on the shift current making rescaling necessary: 30  \( \mathring{A} \)  (red), 25  \( \mathring{A} \)  (green), 20  \( \mathring{A} \)  (blue) of vacuum.

![](2512.05796v1-images/29_1.jpg)

![](2512.05796v1-images/29_2.jpg)

![](2512.05796v1-images/29_3.jpg)

![](2512.05796v1-images/29_4.jpg)

![](2512.05796v1-images/29_5.jpg)

![](2512.05796v1-images/29_6.jpg)

![](2512.05796v1-images/29_7.jpg)

![](2512.05796v1-images/29_8.jpg)

![](2512.05796v1-images/29_9.jpg)

Figure 16: The glass coefficient for bulk (blue line), four-layers (green), bi-layer (red), mono layer (yellow) configurations
 
![](2512.05796v1-images/30_0.jpg)

![](2512.05796v1-images/30_1.jpg)

![](2512.05796v1-images/30_2.jpg)

![](2512.05796v1-images/30_3.jpg)

![](2512.05796v1-images/30_4.jpg)

![](2512.05796v1-images/30_5.jpg)

Figure 17: The effect of spin-orbit interaction on the proposed FOM: SOC included in the top panels, no SOC included in the bottom panels.
 
