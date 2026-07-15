# Thermoelectric Properties of Transition Metal Dichalcogenides: From Monolayers to Nanotubes

Kai-Xuan Chen, Xiao-Ming Wang, Dong-Chuan Mo,* and Shu-Shen Lyu*

School of Chemistry and Chemical Engineering, Sun Yat-sen University, Guangzhou 510275, China

Supporting Information

**ABSTRACT:** Thermoelectric material has the unique ability to directly convert waste heat into electricity, and theoretical guidance is an efficient method for exploring high-performance nanostructured thermoelectric materials. By using first-principles method, we systematically present the ballistic thermoelectric properties of four representative series of transition metal dichalcogenides (WSe₂, MoSe₂, WS₂, and MoS₂), each including monolayer, zigzag (10, 0), and armchair (6, 6) nanotubes. Consistent regularity can be seen for each considered series. From monolayer to small nanotubes, degeneration of thermoelectric figure of merit is observed, which indicates that transition metal dichalcogenide monolayers exhibit better thermoelectric performance than the small nanotubes. In addition, it is interesting to find out the divergence pattern with regard to the phononic thermal conductance, which points out that the room-temperature phononic thermal conductance of monolayers is bigger than that of zigzag (10, 0) nanotube but lower than that of armchair (6, 6) nanotube.

![](./images/814580593999216641_1.jpg)

## INTRODUCTION

Thermoelectric material, due to its unique ability to directly convert waste heat into electricity and vice versa, is considered as an effective way to resolve energy issues.¹ To evaluate the performance of thermoelectric materials, a dimensionless thermoelectric figure of merit is generally adopted, defined as $ZT = ((GS^2T)/\sigma)$, where $G$, $S$, $\sigma$, and $T$ are electronic conductance, Seebeck coefficient, thermal conductance, and absolute temperature, respectively. According to the formula, high electronic conductance $G$, high Seebeck coefficient $S$, as well as low thermal conductance $\sigma$ are entirely expected to obtain high ZT.² However, the value of ZT remains relatively low for decades, since the physical factors defining ZT are interdependent. It is difficult to alter one single physical factor while the others remain unaffected. Low-dimensional materials, which are free of such interdependence due to the quantum size effects, are pointed out to provide a new direction of designing high-performance thermoelectric materials.³⁴ Some unexpected properties may always be discovered when it comes to new low-dimensional materials. Recently, nanostructured inorganic semiconductor materials, such as Bi₂Te₃ nanowire,⁵ monolayer phosphorene,⁶ silicene, and germanene,⁷ turn out to exhibit excellent thermoelectric performance. Many more are still under investigation and have tremendous potential to accelerate thermoelectric applications.⁸ Transition metal dichalcogenides (TMDs),⁹¹⁰ a new family of two-dimensional (2D) materials, have attracted a lot of attention in recent years due to their various applications in the field of electrocatalysis,¹¹ optoelectronics,¹²¹³ supercapacitors,¹⁴ batteries,¹⁵ and so on. Transition metal dichalcogenide nanotube (TMDNT)¹⁶ can be imagined as a TMD monolayer rolled up in a specific direction.

A few TMDNTs having been already synthesized experimentally;¹⁷⁻²⁰ nevertheless, no research on the thermoelectric properties of TMDNTs has ever been done to our knowledge. As such, the objective of this research is to reveal the intrinsic ballistic thermoelectric mechanism of TMDs and TMDNTs in order to accelerate their potential application.

## MODEL AND METHODS

TMDs²¹ are a series of materials with the molecular formula of MX₂ (where M = Mo/W; X = S/Se). The TMD monolayer has a graphene-like two-dimensional structure, as shown in Figure 1a and b. Like carbon nanotube, the nomenclature $(n, m)$ can also be applied for single-wall TMDNTs.²² Similarly, $(n, n)$ and $(n, 0)$ represent the armchair and zigzag single-wall TMDNT, respectively, while the tube diameter $d$ can be calculated as $d = (a/\pi)(n^2 + m^2 + nm)^{1/2}$, where $a$ is the lattice constant of TMD monolayer. The cross plane for nanotubes is calculated as $A = d\delta\pi$, where $\delta$ is the distance between layers in TMD bulks. The top view and side view of zigzag (10, 0) and armchair (6, 6) nanotubes are demonstrated in Figure 1c−f. These two achiral nanotubes are chosen for the close nanotube diameter and relatively cheap simulation cost requirement.

In this article, we focus on four representative series of TMD (WSe₂, MoSe₂, WS₂, and MoS₂), each including monolayer and corresponding TMDNTs, namely, zigzag (10, 0) and armchair (6, 6) nanotubes. As we know, the key parameter to separate ballistic and diffusive regime is whether the system length scale

Received: July 13, 2015
Revised: October 1, 2015

![](./images/814580593999216641_2.jpg)

Figure 1. (a) Schematic 2D plane structure of TMD monolayer, where the unit cell is denoted by the red dotted box, which contains one Mo/W atom and two S/Se atoms. (b) Triple-layers sandwich structure of TMD monolayer: each Mo/W atomic plane is sandwiched between two S/Se atomic planes. The top view and side view of single-wall zigzag (10, 0) and armchair (6, 6) nanotubes are shown in (c, e) and (d, f), respectively, with their unit cells denoted by the red dotted box.

is smaller than the electron and phonon mean free path (MFP). As temperature increases, the value of MFP may decrease. However, the ballistic assumption is valid as long as the system size along the transport direction is within the limit of MFP.²³ Thus, the room-temperature transport properties can be effectively described by the ballistic regime. In ballistic framework, coherent transport is fully considered while the interactions of electron−electron, electron−phonon, and phonon−phonon are weak and thus negligible. The non-equilibrium Green's function (NEGF) method is employed, as implemented in the density functional theory (DFT)/density functional perturbation theory (DFPT) framework.²⁴⁻²⁶ The calculations of the Hamiltonian matrix and interatomic force constants (IFCs) are performed using the package code Quantum Espresso.²⁷ In the previous research of Chang et al.²⁸ and Huang et al.,²² it was demonstrated that the electronic band gaps of TMD monolayers calculated within local density approximation (LDA) framework were in good agreement with experiments, rather than the generalized gradient approximation (GGA) framework. Mixed pseudopotentials from the official Quantum Espresso database are adopted within the LDA of Perdew−Zunger. Norm-conserving pseudopotential with the Bachelet−Hamann−Schlueter method is used for W atoms and ultrasoft pseudopotentials with the Rappe−Rabe−Kaxiras−Joannopoulos method for the other atoms. The vacuum region of 15 Å is used. Both energy cutoff and k-points are chosen from the convergence test. The minimum energy (charge density) cutoff is up to 45 Ry (450 Ry), while the value would be a little bigger in some cases. Optimized structures are obtained from the relaxation with dense k-grid.

To be specific, the Monkhorst−Pack k-grids used for the structure relaxation are 21 × 21 × 1, 1 × 1 × 19, 1 × 1 × 19 for monolayers, armchair, and zigzag nanotubes, respectively. After the structure relaxation, coarse k-grids can be used to reduce the resource requirement. For armchair (6, 6) nanotubes, a 1 × 1 × 11 Monkhorst−Pack k-grid is used to sample the first Brillouin zone for self-consistency and a 1 × 1 × 7 Monkhorst−Pack q-grid for phonon calculation to satisfy the nearest-neighbor interaction condition in NEGF process, while the grids are 1 × 1 × 5 and 1 × 1 × 3 for k and q points of zigzag (10, 0) nanotubes, respectively. Once the Hamiltonian matrix and IFCs are obtained, one can work out the physical properties according to the following equations.

For ballistic electron calculation, the retarded Green's function \( G^{\text{r}} \) should be obtained first

$$
G^{\text{r}} = \left[ E S_{\text{C}} - H_{\text{C}} - \Sigma_{\text{L}}^{\text{r}} - \Sigma_{\text{R}}^{\text{r}} \right]^{-1} \tag{1}
$$

where \( E \) is the electron energy and \( H_{\text{C}} \) and \( S_{\text{C}} \) are the Hamiltonian and overlap matrix of the central conductor, respectively. \( \sum_{\beta}^{\text{r}} \) with \( \beta = \text{L, R} \) denotes the self-energy of the semi-infinite leads, which can be obtained through eq 2

$$
\Sigma_{\text{L}}^{\text{r}} = H_{\text{LC}} g_{\text{L}}^{\text{r}} H_{\text{LC}}^{\dagger}, \ \Sigma_{\text{R}}^{\text{r}} = H_{\text{CR}} g_{\text{R}}^{\text{r}} H_{\text{CR}}^{\dagger} \tag{2}
$$

where \( g_{\text{L}}^{\text{r}} \) and \( g_{\text{R}}^{\text{r}} \) are the retarded surface Green's function of the left and right lead, respectively. \( H_{\text{LC}} \) and \( H_{\text{CR}} \) are the Hamiltonian between leads and device, respectively, while \( H_{\text{LC}}^{\dagger} \) and \( H_{\text{CR}}^{\dagger} \) are the corresponding transposed-conjugate matrix. After that, the electron transmittance \( \text{T}(E) \) can be calculated through eq 3

$$
\text{T}(E) = \text{Tr}(G^{\text{r}} \Gamma_{\text{L}} G^{\text{a}} \Gamma_{\text{R}}) \tag{3}
$$

where \( G^{\text{a}} = (G^{\text{r}})^{\dagger} \) is the advanced Green's function and \( \Gamma_{\beta} = i(\sum_{\beta}^{\text{r}} - \sum_{\beta}^{\text{a}}) \) with \( \beta = \text{L, R} \) describes the interaction between the leads and the central conductor.

Next, for convenience, the Lorenz function is introduced to calculate the electronic conductance \( G \), Seebeck coefficient \( S \), and electronic thermal conductance \( \sigma_{\text{el}} \) according to eqs 4−7

$$
L_{\text{n}}(\mu,\ T) = \frac{2}{h} \int \text{d}E \text{T}(E) \times (E - \mu)^{\text{n}} \times \left[ -\frac{\partial f(E,\ \mu,\ T)}{\partial E} \right] \tag{4}
$$

$$
G = q^{2} L_{0} \tag{5}
$$

$$
S = \frac{1}{qT} \times \frac{L_{1}}{L_{0}} \tag{6}
$$

$$
\sigma_{\text{el}} = \frac{1}{T} \times \left( L_{2} - \frac{L_{1}^{2}}{L_{0}} \right) \tag{7}
$$

where \( f(E,\ \mu,\ T) \) is the Fermi−Dirac distribution function, \( \mu \) is the chemical potential, and \( T \) is the absolute temperature. Also, \( h \) is the Planck constant, and \( q \) is the charge of electron.

For ballistic phonon calculation, one just needs to replace the \( E S_{\text{C}} \) with \( (\omega + i\eta)^{2} \) and the \( H_{\text{C}} \) with \( K_{\text{C}} \) in eq 1 to obtain the phonon transmittance \( \text{T}(\omega) \), where \( \omega \) is the phonon frequency and \( \eta \) is an infinitesimal added as the imaginary part of \( \omega \). Therefore, the phononic thermal conductance \( \sigma_{\text{ph}} \) can be calculated through eq 8.

$$
\sigma_{\text{ph}}(T) = \frac{\hbar}{2\pi} \int_{0}^{\infty} \text{T}(\omega)\omega \frac{\partial f(\omega,\ T)}{\partial T} \text{d}\omega \tag{8}
$$


where $f(\omega, T)$ is the Bose-Einstein distribution function and $\hbar$ is the reduced Planck constant.

Finally, the value of ZT can be calculated after obtaining all thermoelectric factors.

$$
ZT = \frac{GS^2 T}{\sigma_{\text{el}} + \sigma_{\text{ph}}}
\tag{9}
$$

## RESULTS AND DISCUSSION

Our investigation begins from these four representative TMD monolayers. It is found out that the monolayers are all semiconductive with direct band gap in the electronic band structures. $^{29,30}$ The specific wide band gaps are 1.69, 1.59, 2.01, and 1.86 eV for WSe$_2$, MoSe$_2$, WS$_2$, and MoS$_2$, respectively, which are consistent with previous research. $^{28,31,32}$ After that, we turn to their thermoelectric performance. The maximum room-temperature ZTs turn out to be 0.91, 0.88, 0.72, and 0.75 for WSe$_2$, MoSe$_2$, WS$_2$, and MoS$_2$, respectively. By employing the generalized gradient approximation, Huang et al. $^{33}$ obtained the maximum room-temperature ZT of 0.58 for MoS$_2$ monolayer, and the value is $\sim$0.7 within local density approximation observed in their follow-up research. $^{22}$ In the work of Wickramaratne et al., $^{34}$ the value becomes 0.87 when a constant phononic thermal conductance of 34.5 Wm$^{-1}$K$^{-1}$ is used in the Boltzman transport equation method. These findings are close to the ZT of 0.75 which we figure out in MoS$_2$ monolayer. It clarifies that our theoretical calculation on these TMD monolayers is reliable, which provides effectiveness for the following prediction work on thermoelectric performance of TMDNTs.

To understand the electronic properties of the TMDNTs intuitively, the demonstration of electronic band structure is adopted. The MoS$_2$ series is illustrated as a representative example. Figure 2a demonstrates the electronic band structure of MoS$_2$ monolayer along the high-symmetry points G-M-K-G. A wide direct band gap, with the value up to 1.86 eV, can be discovered at the K point. The electronic band structures of MoS$_2$ (6, 6) and MoS$_2$ (10, 0) nanotube along the G-X high-symmetry points are plotted in Figure 2b and c, respectively. For MoS$_2$ (10, 0) nanotube, a direct band gap can be seen at the gamma point with the value of 0.36 eV, while for MoS$_2$ (6, 6) nanotube, the band gap becomes indirect and narrower (0.24 eV). One can find out that the monolayer possesses the wider band gap than the nanotubes and that zigzag (10, 0) nanotube possesses the wider band gap than armchair (6, 6) counterpart. Seifert et al. $^{35}$ investigated the electronic properties of MoS$_2$ nanotubes using functional based tight-binding (DFTB) method. It was found that MoS$_2$ zigzag (n, 0) nanotubes exhibit a narrow direct band gap and MoS$_2$ armchair (n, n) tubes possess a nonzero moderate direct gap. Besides, the (n, n) tubes show a small indirect gap similar to the direct gap of (n, 0) nanotubes. In addition, Seifert et al. $^{36}$ continued their research on the WS$_2$ nanotubes and had the conclusion that the (n, n) tubes exhibit an indirect gap of similar size as the direct gap in (n, 0) nanotubes of comparable diameter. Zibouche et al. $^{37}$ studied the transition metal disulfides from layers to nanotubes from first-principles density functional theory. Their result showed that the armchair nanotubes remain indirect gap semiconductors, while the zigzag nanotubes are direct gap materials. Similar behavior can be seen in our work.

![](./images/814580593999216641_3.jpg)

Figure 2. Electronic band structure, transmittance, and density of state (DOS) of (a) MoS$_2$ monolayer, (b) MoS$_2$ (10, 0) nanotube, and (c) MoS$_2$ (6, 6) nanotube, respectively.

Second, we concentrate on the properties of TMDNTs. In this section, we investigate the temperature and chemical potential dependence of thermoelectric factors, where WSe$_2$ series is taken as an example to illustrate the regularity between monolayer and nanotubes. The demonstration of the other three series is presented in the *Supporting Information* where consistent regularity can be observed. Figure 3a and b show the electronic conductance $G$ and electronic thermal conductance $\sigma_{\text{el}}$ as a function of chemical potential at room temperature, respectively. Owing to the same proportionality with the electron transmittance, $G$ and $\sigma_{\text{el}}$ usually share the same variation trend. When the chemical potential $\mu$ is near zero point, the Fermi surface locates between the valence and conduction subbands and few electrons can be excited into the conduction subband, thus leading to a small value in $G$ and $\sigma_{\text{el}}$. As $\mu$ increases, the Fermi surface gradually moves into the conduction subband, and consequently both $G$ and $\sigma_{\text{el}}$ show a dramatic increase. Nevertheless, the ratio of $G$ over $\sigma_{\text{el}}$ almost remains constant due to such variation consistency. Therefore, the contribution of phononic thermal conductance $\sigma_{\text{ph}}$ to the whole thermal conductance matters significantly. $\sigma_{\text{ph}}$ as a function of absolute temperature is plotted in Figure 3d, where an interesting phenomenon can be seen that the room-temperature $\sigma_{\text{ph}}$ of monolayer is bigger than that of zigzag (10, 0) nanotube but lower than that of armchair (6, 6) nanotube. From monolayers to nanotubes, degeneration of band gap can be realized, as demonstrated in Figure 3e. Besides, the zigzag (10, 0) nanotubes possess wider band gaps than the armchair (6, 6) counterpart, and the direct-indirect transition of band

![](./images/814580593999216641_4.jpg)

Figure 3. Themoelectric factors of WSe₂ series: room-temperature (a) electronic conductance $G$, (b) electronic thermal conductance $\sigma_{\text{el}}/A$, (c) Seebeck coefficient $S$ as a function of chemical potential $\mu$, and (d) phononic thermal conductance $\sigma_{\text{ph}}/A$ as a function of absolute temperature. $G_0$ is the quantum conductance $G_0 = 2e^2/h$, where $h$ is the Planck constant and $A$ is the cross area. Besides, the (e) band gaps and (f) room-temperature $\sigma_{\text{ph}}/A$ of all series are also listed for comparison, from which one can find out the consistent regularity in each series separately; that is, for band gap: monolayer > nanotubes and zigzag (10, 0) > armchair (6, 6); for phononic thermal conductance: zigzag (10, 0) < monolayer < armchair (6, 6).

gap is also discovered from monolayers to armchair (6, 6) nanotubes. The variation in electronic properties always consequently affects the thermoelectric factors. For comparison, the room-temperature $\sigma_{\text{ph}}$ values of all series are presented in Figure 3f. In addition, following the variation trend of electronic band gap, the Seebeck coefficient of monolayer is larger than that of the corresponding TMDNTs.

Compared with graphene, wider band gap and lower phononic thermal conductance³⁸ can be found in TMD monolayers, consequently resulting in the larger Seebeck coefficient and thermoelectric figure of merit. The room-temperature ZT of TMD monolayer as a function of chemical potential is plotted in Figure 4a, where maximum value of 0.7−0.95 can be observed. Such high-performance thermoelectric property in TMD monolayer indicates the great potential application in the thermoelectric field.³³ The maximum ZT values of armchair (6, 6) and zigzag (10, 0) nanotubes at room temperature are in the range of 0.2−0.35 and 0.35−0.5, respectively, as shown in Figure 4b and c. The smaller ZT in armchair (6, 6) nanotube is due to the larger phonon thermal conductance, as explained in the previous paragraph. From graphene to carbon nanotubes, enhancement in the thermoelectric properties can be discovered, especially for those with semiconductive properties.²⁴ However, the opposite trend for the TMD series is found in Figure 3d. The ZTs of TMDNTs are much lower than those of corresponding TMD monolayers due to the degeneration of Seebeck coefficient in Figure 3c. Among the four series studied in this work, WSe₂ series possesses the largest ZT, whether in monolayers or nanotubes. The room-temperature ZT of WSe₂ monolayer, zigzag WSe₂ (10, 0), and armchair WSe₂ (6, 6) nanotube can reach the maximum value of 0.91, 0.47, and 0.33, respectively. In previous research, the maximum ZT value of 1.35 is obtained at 300 K for p-type Bi₂Te₃ with layered nanostructure,³⁹ while the value reaches 1.47 for the nanocomposite hot pressed from Bi₂Te₃ and Sb₂Te₃ nanopowders at ∼450 K.⁴⁰ SnSe has been reported to exhibit the unprecedented ZT of $2.6 \pm 0.3$ at 923 K.⁴¹ The first-principles calculation also predicted the highest ZT value for n-type doping to reach 2.7 in SnSe at 750 K.⁴² The TMD monolayers, which possess the room-temperature ZT of 0.7−0.9, could become competitive thermoelectric materials since the definition of ZT has a $T$ in it. The thermoelectric performance may probably be enhanced when the monolayers are reduced to nanoribbons, which would be included in our future work.

![](./images/814580593999216641_5.jpg)

Figure 4. (a)−(c) ZT as a function of chemical potential at room temperature for monolayers, armchair (6, 6), and zigzag (10, 0) nanotubes, respectively. The maximum room-temperature ZT values of all series are listed in (d), from which one can find out the consistent regularity of ZT in each series separately: monolayer > nanotubes and zigzag (10, 0) > armchair (6, 6).

## CONCLUSIONS

In summary, the first-principles method is adopted to investigate the ballistic electronic, phononic, and thermoelectric properties of four series of transition metal dichalcogenide series (WSe₂, MoSe₂, WS₂, and MoS₂), each including monolayer, armchair (6, 6), and zigzag (10, 0) nanotubes. Consistent regularity is observed in each series separately. First, the ZT of monolayer is larger than that of small nanotubes due to the larger Seebeck coefficient, which is totally different with regard to the ZT from graphene to carbon nanotubes. Second, the ZT of zigzag (10, 0) nanotube is larger than that of armchair (6, 6) nanotube due to the lower phononic thermal conductance. Third, the room-temperature phononic thermal conductance of monolayer is bigger than that of zigzag (10, 0) nanotube but lower than that of armchair (6, 6) nanotube. Among the four series studied in this work, the WSe₂ series seem to be superior to the others in thermoelectric performance. The room-temperature ZT of WSe₂ monolayer can reach
D
DOI: 10.1021/acs.jpcc.5b06728
J. Phys. Chem. C XXXX, XXX, XXX−XXX

as high as 0.91, while the value for zigzag $WSe_2$ (10, 0) nanotube is 0.47. Our work reveals the intrinsic thermoelectric mechanism of transition metal dichalcogenide monolayers and nanotubes, which will highlight the theoretical guidance for those researchers who are interested in exploring new high- performance thermoelectric materials.

## ASSOCIATED CONTENT

### Supporting Information
The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jpcc.5b06728.

Demonstration of thermoelectric factors of $MoSe_2$, $WS_2$, and $MoS_2$ series; influence of nanotube size on ZT for $WSe_2$ series (PDF)

## AUTHOR INFORMATION

### Corresponding Authors
*Tel.: +86-020-84113985. E-mail: modongch@mail.sysu.edu.cn.
*Tel.: +86-020-84112151. E-mail: lvshsh@mail.sysu.edu.cn.

### Author Contributions
The manuscript was written through contributions of all authors. All authors have given approval to the final version of the manuscript.

### Notes
The authors declare no competing financial interest.

## ACKNOWLEDGMENTS
Financial support from the National Natural Science Foundation of China (Grant No. 51276202) and the Fundamental Research Funds for the Central Universities are gratefully acknowledged. The simulation work is supported by the National Supercomputer Center in Guangzhou and the high-performance grid computing platform of Sun Yat-sen University.

## ABBREVIATIONS
2D, two-dimensional; DFPT, density functional perturbation theory; DFT, density functional theory; DFTB, density functional based tight-binding; IFCs, interatomic force constants; LDA, local density approximation; MFP, mean free path; NEGF, nonequilibrium Green's function; TMD, transition metal dichalcogenide; TMDNT, transition metal dichalcogenide nanotube; ZT, thermoelectric figure of merit

## REFERENCES
(1) He, M.; Qiu, F.; Lin, Z. Q. Towards High-Performance Polymer- Based Thermoelectric Materials. *Energy Environ. Sci.* **2013**, 6, 1352-1361.
(2) Liu, Y. S.; Chen, Y. R.; Chen, Y. C. Thermoelectric Efficiency in Nanojunctions: A Comparison between Atomic Junctions and Molecular Junctions. *ACS Nano* **2009**, 3, 3497-3504.
(3) Li, J.-F.; Liu, W.-S.; Zhao, L.-D.; Zhou, M. High-Performance Nanostructured Thermoelectric Materials. *NPG Asia Mater.* **2010**, 2, 152-158.
(4) Kanatzidis, M. G. Nanostructured Thermoelectrics: The New Paradigm? *Chem. Mater.* **2010**, 22, 648-659.
(5) Zhang, G.; Kirk, B.; Jauregui, L. A.; Yang, H.; Xu, X.; Chen, Y. P.; Wu, Y. Rational Synthesis of Ultrathin N-Type $Bi_2Te_3$ Nanowires with Enhanced Thermoelectric Properties. *Nano Lett.* **2012**, 12, 56-60.
(6) Fei, R.; Faghaninia, A.; Soklaski, R.; Yan, J. A.; Lo, C.; Yang, L. Enhanced Thermoelectric Efficiency via Orthogonal Electrical and Thermal Conductances in Phosphorene. *Nano Lett.* **2014**, 14, 6393-6399.
(7) Yang, K.; Cahangirov, S.; Cantarero, A.; Rubio, A.; D'Agosta, R. Thermoelectric Properties of Atomically Thin Silicene and Germanene Nanostructures. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2014**, 89, 125403.
(8) Butler, S. Z.; Hollen, S. M.; Cao, L.; Cui, Y.; Gupta, J. A.; Gutierrez, H. R.; Heinz, T. F.; Hong, S. S.; Huang, J.; Ismach, A. F.; et al. Progress, Challenges, and Opportunities in Two-Dimensional Materials Beyond Graphene. *ACS Nano* **2013**, 7, 2898-2926.
(9) Huang, X.; Zeng, Z.; Zhang, H. Metal Dichalcogenide Nanosheets: Preparation, Properties and Applications. *Chem. Soc. Rev.* **2013**, 42, 1934-1946.
(10) Chhowalla, M.; Shin, H. S.; Eda, G.; Li, L. J.; Loh, K. P.; Zhang, H. The Chemistry of Two-Dimensional Layered Transition Metal Dichalcogenide Nanosheets. *Nat. Chem.* **2013**, 5, 263-275.
(11) Smith, A. J.; Chang, Y. H.; Raidongia, K.; Chen, T. Y.; Li, L. J.; Huang, J. Molybdenum Sulfide Supported on Crumpled Graphene Balls for Electrocatalytic Hydrogen Production. *Adv. Energy. Mater.* **2014**, 4.1400398140040310.1002/aem.201400398.
(12) Sun, Y. F.; Sun, Z. H.; Gao, S.; Cheng, H.; Liu, Q. H.; Lei, F. C.; Wei, S. Q.; Xie, Y., All-Surface-Atomic-Metal Chalcogenide Sheets for High-Efficiency Visible-Light Photoelectrochemical Water Splitting. *Adv. Energy. Mater.* **2014**, 4.1300611130062010.1002/aem.201300611.
(13) Choi, W.; Cho, M. Y.; Konar, A.; Lee, J. H.; Cha, G. B.; Hong, S. C.; Kim, S.; Kim, J.; Jena, D.; Joo, J.; et al. High-Detectivity Multilayer $MoS_2$ Phototransistors with Spectral Response from Ultraviolet to Infrared. *Adv. Mater.* **2012**, 24, 5832-5836.
(14) Tang, H.; Wang, J.; Yin, H.; Zhao, H.; Wang, D.; Tang, Z. Growth of Polypyrrole Ultrathin Films on $MoS_2$ Monolayers as High- Performance Supercapacitor Electrodes. *Adv. Mater.* **2015**, 27, 1117-1123.
(15) Liu, H.; Su, D. W.; Zhou, R. F.; Sun, B.; Wang, G. X.; Qiao, S. Z. Highly Ordered Mesoporous $MoS_2$ with Expanded Spacing of the (002) Crystal Plane for Ultrafast Lithium Ion Storage. *Adv. Energy. Mater.* **2012**, 2, 970-975.
(16) Tenne, R.; Margulis, L.; Genut, M.; Hodes, G. Polyhedral and Cylindrical Structures of Tungsten Disulphide. *Nature* **1992**, 360, 444-446.
(17) Nath, M.; Govindaraj, A.; Rao, C. N. R. Simple Synthesis of $MoS_2$ and $WS_2$ Nanotubes. *Adv. Mater.* **2001**, 13, 283-286.
(18) Kreizman, R.; Enyashin, A. N.; Deepak, F. L.; Albu-Yaron, A.; Popovitz-Biro, R.; Seifert, G.; Tenne, R. Synthesis of Core-Shell Inorganic Nanotubes. *Adv. Funct. Mater.* **2010**, 20, 2459-2468.
(19) Chen, J.; Li, S. L.; Xu, Q.; Tanaka, K. Synthesis of Open-Ended $MoS_2$ Nanotubes and the Application as the Catalyst of Methanation. *Chem. Commun.* **2002**, 1722-1723.
(20) Nath, M.; Rao, C. N. $MoSe_2$ and $WSe_2$ Nanotubes and Related Structures. *Chem. Commun. (Cambridge, U. K.)* **2001**, 2236-2237.
(21) Mak, K. F.; Lee, C.; Hone, J.; Shan, J.; Heinz, T. F. Atomically Thin $MoS_2$: A New Direct-Gap Semiconductor. *Phys. Rev. Lett.* **2010**, 105, 136805.
(22) Huang, W.; Luo, X.; Gan, C. K.; Quek, S. Y.; Liang, G. Theoretical Study of Thermoelectric Properties of Few-Layer $MoS_2$ and $WSe_2$. *Phys. Chem. Chem. Phys.* **2014**, 16, 10866-10874.
(23) Tan, Z. W.; Wang, J. S.; Gan, C. K. First-Principles Study of Heat Transport Properties of Graphene Nanoribbons. *Nano Lett.* **2011**, 11, 214-219.
(24) Jiang, J.-W.; Wang, J.-S.; Li, B. A Nonequilibrium Green's Function Study of Thermoelectric Properties in Single-Walled Carbon Nanotubes. *J. Appl. Phys.* **2011**, 109, 014326.
(25) Wang, X. M.; Lu, S. S. Thermoelectric Transport in Graphyne Nanotubes. *J. Phys. Chem. C* **2013**, 117, 19740-19745.
(26) Tan, X. J.; Liu, H. J.; Wen, Y. W.; Lv, H. Y.; Pan, L.; Shi, J.; Tang, X. F. Thermoelectric Properties of Ultrasmall Single-Wall Carbon Nanotubes. *J. Phys. Chem. C* **2011**, 115, 21996-22001.
(27) Giannozzi, P.; Baroni, S.; Bonini, N.; Calandra, M.; Car, R.; Cavazzoni, C.; Ceresoli, D.; Chiarotti, G. L.; Cococcioni, M.; Dabo, I.;

et al. Quantum Espresso: A Modular and Open-Source Software Project for Quantum Simulations of Materials. *J. Phys.: Condens. Matter* **2009**, *21*, 395502.

(28) Chang, C. H.; Fan, X. F.; Lin, S. H.; Kuo, J. L. Orbital Analysis of Electronic Structure and Phonon Dispersion in $MoS_2$, $MoSe_2$, $WS_2$, and $WSe_2$ Monolayers under Strain. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2013**, *88*, 195420.

(29) Bhattacharyya, S.; Pandey, T.; Singh, A. K. Effect of Strain on Electronic and Thermoelectric Properties of Few Layers to Bulk $MoS_2$. *Nanotechnology* **2014**, *25*, 465701.

(30) Cai, Y.; Bai, Z.; Pan, H.; Feng, Y. P.; Yakobson, B. I.; Zhang, Y. W. Constructing Metallic Nanoroads on a $MoS_2$ Monolayer via Hydrogenation. *Nanoscale* **2014**, *6*, 1691−1697.

(31) Ding, Y.; Wang, Y.; Ni, J.; Shi, L.; Shi, S.; Tang, W. First Principles Study of Structural, Vibrational and Electronic Properties of Graphene-Like $MX_2$ (M = Mo, Nb, W, Ta; X = S, Se, Te) Monolayers. *Phys. B* **2011**, *406*, 2254−2260.

(32) Sahin, H.; Tongay, S.; Horzum, S.; Fan, W.; Zhou, J.; Li, J.; Wu, J.; Peeters, F. M. Anomalous Raman Spectra and Thickness-Dependent Electronic Properties of $WSe_2$. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2013**, *87*, 165409.

(33) Huang, W.; Da, H.; Liang, G. Thermoelectric Performance of $MX_2$ (M = Mo,W; X = S,Se) Monolayers. *J. Appl. Phys.* **2013**, *113*, 104304.

(34) Wickramaratne, D.; Zahid, F.; Lake, R. K. Electronic and Thermoelectric Properties of Few-Layer Transition Metal Dichalcogenides. *J. Chem. Phys.* **2014**, *140*, 124710.

(35) Seifert, G.; Terrones, H.; Terrones, M.; Jungnickel, G.; Frauenheim, T. Structure and Electronic Properties of $MoS_2$ Nanotubes. *Phys. Rev. Lett.* **2000**, *85*, 146−149.

(36) Seifert, G.; Terrones, H.; Terrones, M.; Jungnickel, G.; Frauenheim, T. On the Electronic Structure of $WS_2$ Nanotubes. *Solid State Commun.* **2000**, *114*, 245−248.

(37) Zibouche, N.; Kuc, A.; Heine, T. From Layers to Nanotubes: Transition Metal Disulfides $TMS_2$. *Eur. Phys. J. B* **2012**, *85*, 49.

(38) Chen, K. X.; Wang, X. M.; Mo, D. C.; Lyu, S. S. Substrate Effect on Thermal Transport Properties of Graphene on SiC(0001) Surface. *Chem. Phys. Lett.* **2015**, *618*, 231−235.

(39) Tang, X.; Xie, W.; Li, H.; Zhao, W.; Zhang, Q.; Niino, M. Preparation and Thermoelectric Transport Properties of High-Performance p-Type $Bi_2Te_3$ with Layered Nanostructure. *Appl. Phys. Lett.* **2007**, *90*, 012102.

(40) Cao, Y. Q.; Zhao, X. B.; Zhu, T. J.; Zhang, X. B.; Tu, J. P. Syntheses and Thermoelectric Properties of $Bi_2Te_3$/$Sb_2Te_3$ Bulk Nanocomposites with Laminated Nanostructure. *Appl. Phys. Lett.* **2008**, *92*, 143106.

(41) Zhao, L. D.; Lo, S. H.; Zhang, Y.; Sun, H.; Tan, G.; Uher, C.; Wolverton, C.; Dravid, V. P.; Kanatzidis, M. G. Ultralow Thermal Conductivity and High Thermoelectric Figure of Merit in SnSe Crystals. *Nature* **2014**, *508*, 373−377.

(42) Guo, R. Q.; Wang, X. J.; Kuang, Y. D.; Huang, B. L. First-Principles Study of Anisotropic Thermoelectric Transport Properties of IV−VI Semiconductor Compounds SnSe and SnS. *Phys. Rev. B: Condens. Matter Mater. Phys.* **2015**, *92*, 115202.