Accepted Manuscript

Indentation modeling study of temperature-dependent fracture toughness of brittle coating on ductile substrate based on microcrack formation theory

Yichen Gu, Kuiying Chen, Rong Liu, Matthew X. Yao, Rachel Collier

![](./images/811102799034056704_1.jpg)

<table>
<tr>
<td>PII:</td>
<td>S0257-8972(16)31304-4</td>
</tr>
<tr>
<td>DOI:</td>
<td>doi: 10.1016/j.surfcoat.2016.12.016</td>
</tr>
<tr>
<td>Reference:</td>
<td>SCT 21873</td>
</tr>
<tr>
<td>To appear in:</td>
<td>Surface & Coatings Technology</td>
</tr>
<tr>
<td>Received date:</td>
<td>24 June 2016</td>
</tr>
<tr>
<td>Revised date:</td>
<td>2 December 2016</td>
</tr>
<tr>
<td>Accepted date:</td>
<td>4 December 2016</td>
</tr>
</table>

Please cite this article as: Yichen Gu, Kuiying Chen, Rong Liu, Matthew X. Yao, Rachel Collier , Indentation modeling study of temperature-dependent fracture toughness of brittle coating on ductile substrate based on microcrack formation theory. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Sct(2016), doi: 10.1016/j.surfcoat.2016.12.016

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Indentation modeling study of temperature-dependent fracture toughness of brittle coating on ductile substrate based on microcrack formation theory

Yichen Gu $^{a}$ , Kuiying Chen $^{b}$ , Rong Liu $^{a, *}$ , Matthew X. Yao $^{c}$ , Rachel Collier $^{c}$

$^{a}$ Department of Mechanical and Aerospace Engineering, Carleton University,
1125 Colonel By Drive, Ottawa, Ontario, Canada K1S 5B6
$^{b}$ Institute for Aerospace Research, National Research Council Canada,
1200 Montreal Road, Ottawa, Ontario, Canada K1A 0R6
$^{c}$ Kennametal Stellite Inc., 471 Dundas St E, Belleville, Ontario, Canada K8N 5C4

## ABSTRACT
A temperature-dependent fracture toughness model for brittle coating/ductile substrate systems under indentation is proposed based on microcrack formation theory. Numerous microcracks are generated from each corner of indentation impression and merge together to form radial cracks due to the tension of residual stresses in the coating/substrate system during the unloading period. The fracture toughness of the coating/substrate systems is determined such that the crack tip opening displacement (CTOD) is used to measure the total growth of a microcrack in tensile direction and the dislocation movement is associated with the crack propagation. The temperature effect is modeled in terms of the Arrhenius-type equation and rate controlling theory. Both the basic indentation pressure and composite hardness approaches are used to obtain the model parameters but the latter provides more reasonable results. The WC-10Co4Cr coating/1018 steel substrate system, prepared via high velocity oxygen fuel (HVOF) spraying, is analyzed using this model and the obtained fracture toughness shows increasing with temperature in a nonlinear manner.

Keywords: Brittle coating, Ductile substrate, Microcrack formation, Indentation, Temperature

* Corresponding author. Tel.: +1-613-5202600 ext. 8397; fax: +1-613-5205715.

E-mail address: Rong.Liu@carleton.ca (R. Liu)

### 1. Introduction

Coating technology is undergoing a rapid development, since materials are required to exhibit better mechanical properties and corrosion/oxidation resistance when they are employed in tough environments. Thermal spray processes, such as air plasma spraying (APS) and high velocity oxygen fuel (HVOF) spraying, are deposition technologies that apply metallic or nonmetallic coatings to a substrate. The quantification of interfacial fracture toughness of thermal spray coatings is important for the following reasons: quality assurance of thermal spraying, product design and performance assessment of coatings, quantitative understanding of adhesion degradation in service, and lifetime assessment of the coated components [1].

The methodologies currently employed to analyze the fracture toughness of brittle coatings include indentation, bending, buckling, and scratching tests [2-5]. Among these approaches, indentation test provides simplicity and convenience allowing for a straightforward experimental assessment of fracture toughness using a small number of specimens. Indentation-based coating fracture toughness evaluation methods are commonly associated with microfracture mechanics, considering the behavior of the cracks generated

under the point load [6-12]. Lawn et al. developed a quantitative relationship to correlate the fracture toughness with the radial/median (half-penny) crack size and the indentation load applied on brittle materials [6]. They used the analog of a spherical cavity under internal pressure developed by Hill [13] to relate the relative plastic zone radius to the hardness-to-modulus ratio and the indenter angle. This approach was applied on glass-ceramic (C9606), soda-lime glass, $Al_2O_3$ and $Si_3N_4$ and the obtained fracture toughness values for these materials were verified by independent experiments using the double cantilever technique [14]. Li et al. [7] utilized the same concept to determine the fracture toughness of HVOF sprayed hydroxyapatite (HA) and HA/titania ($TiO_2$) coatings on titanium alloy substrates. They assumed that a well-developed crack generated by the Vickers indenter developed into a median (half-penny) shape and found that the fracture toughness increased with the amount of $TiO_2$ in the HA coating. Kodali et al. [8] investigated the fracture toughness of amorphous diamond-like carbon (DLC) coatings deposited on a silicon substrate. The fracture response of the DLC-Si system was studied using the Vickers indentation test at loads ranging from 25 to 1000 g. For this coating/substrate system, the radial/median cracks were selected based on the criterion that the radial/median (half-penny) crack size was greater than the indenter diagonal. The fracture toughness values they obtained were compared with those derived for polycrystalline diamond coating on a silicon substrate by Mecholsky et al. [9], which showed good agreement. Marshall and Lawn [10] proposed a fracture mechanics model for measuring stresses in the tempered surfaces of bulk glass materials. This approach was based on the indentation fracture mechanics principle where the

scale of microcracking around an impression, generated by a diamond Vickers indenter, provided a measure of resistance to crack extension. Malzbender et al. [11] analyzed the fracture toughness of organic-inorganic hybrid coating deposited on a glass substrate via the spinning technique. Since the hardness to Young's modulus ratios of the coating and substrate were similar, the stress field in the coating/substrate system was assumed to be equivalent to that of the substrate material. Then they speculated that the well-developed crack profile was half-penny and incorporated an empirical crack shape factor into the fracture toughness formulation. The fracture toughness of brittle coatings was also estimated using finite element method (FEM), combined with indentation test [15-17]. This approach utilized energy balance concept and allowed thermal stress included in the modeling, leading to a quantitative evaluation of the threshold load for indentation fracture, and an improved method for the evaluation of material toughness from the indentation load, crack size, hardness, elastic constants, and indenter geometry.

For the applications of coatings, in many cases, high-temperature environment is inevitable, since apparatuses are required to operate at high temperatures in various industries, especially in energy, aerospace, automotive, chemical and manufacturing industries, while the mechanical properties, including fracture toughness, of bulk materials and coating/substrate systems could be significantly influenced by temperature variation. However, due to the limitations of testing facilities and methodologies, the high-temperature properties of coatings have been rarely studied. Although many experimental and modeling

approaches to determining the fracture toughness of coatings have been applied, as discussed above, they are only applicable to coatings in room-temperature environment. To meet the requirements of coating design and application in high-temperature conditions, the present research is aimed to develop a temperature-dependent fracture toughness model for brittle coating deposited on ductile substrate systems. The formulation of the problem is established at microscopic level for the coating/substrate systems under indentation, based on the Arrhenius-type equation and rate controlling theory, concerning microcrack formation at each corner of indentation impression. The brittle coating/ductile substrate system of WC-10Co4Cr on 1018 low carbon steel is selected to demonstrate the model development procedures because of the following reasons: First, it is a typical brittle coating/ductile substrate system. Second, this coating is widely used for resisting severe wear in various fields. Third, this coating/substrate system has been extensively studied in the room-temperature condition so that the required properties of the coating and substrate materials and the experimental/simulation results of this system are available for model parameters and for results comparison.

## 2. Model formulation

### 2.1. Microcrack formation theory

Consider a brittle coating deposited on a ductile substrate under indentation loading, for 2D radial crack extension in the unloading process, numerous microcracks are generated from each corner of indentation impression and merge together to form macrocracks as radial

cracks under tensile residual stresses [10,18], and the radial cracks extend along the indentation diagonals, as illustrated in Fig. 1. Ortiz [19] indicated that, in brittle materials, the microcracks can be assumed to be evenly spaced and have the same length during the crack extension. As shown in Fig. 2, the microcracks have a characteristic length $L$ at the tip zone of the macrocrack in the tensile stress configuration. Although there are gaps between each microcrack, the size of the gaps is too small to take into account when compared with the length of the microcracks. Meanwhile, the microcrack opening displacement $\zeta$ increases from 0 to $\delta$ during the crack propagation process, since the microcracks in the front of the macrocrack tip become the new crack tip one after another when they merge into the macrocrack. Therefore, the crack tip opening displacement (CTOD) $\delta$ can be used to measure the total growth of a microcrack in tensile direction. Under this assumption, the dislocation movement can be associated with the crack propagation process. The amount of CTOD $\delta$ for brittle materials can be assessed based on material properties, and one of the general expressions for CTOD calculation is given as [20]

$$
\delta=\frac{G_{\varepsilon}}{2 \tau_{c}} \tag{1}
$$

where $G_{\varepsilon}$ is strain energy release rate, $\tau_{c}$ is the shear yield stress of coating, $\sigma_{c}=\sqrt{3} \tau_{c}$, $\sigma_{c}$ is the yield stress of coating. This equation has been validated for WC-Co composite, which has similar chemical composition and microstructure to the material being studied, in Murray's work [21]. In this case, the total growth of a microcrack in tensile direction approximately equals the size of CTOD $(\zeta \approx \delta)$.

### 2.2. Dislocation movement theory

The microcracks formed in a coating are caused by the dislocation movement of atoms in the deformation zone, as illustrated in Fig. 3. The magnitude and direction of dislocation movement can be described by Burgers vector $b$ [22]. Therefore, the fracture toughness of brittle materials under indentation loading can also be evaluated with microcrack density and the energy for microcrack formation. The total amount of energy change during the fracture process can be described at microscopic level using strain energy release rate, surface energy, energy barrier and stacking fault energy [22]. The dislocation movement of atoms in this process can be depicted through Burgers vector and the slip system of the material under certain load type. When deformation occurs in the material, the atoms in certain area may deviate from their equilibrium position. During the atomic deviation process, energy change takes place in the bonds between atoms. The bonds are broken when the force or the energy exceeds a critical value [23]. Microcracks are initiated and propagate due to the atomic deviation and the absence of connection between atoms. Although this concept is based on 2D profile and much simpler than real situation, it can be applied to the microcrack formation and the fracture toughness modeling on micromechanics scale. In terms of this concept, the size of microcracks formed during crack propagation and the magnitude of dislocation movement in terms of Burgers vector can be approximately related by a parameter $m$ with $mb = \delta$ [24].

### 2.3. Formulation of fracture toughness

For a brittle coating deposited on a ductile substrate, the energy release rate $G_{\varepsilon}$ for the propagation of cracks whose lengths are much greater than the coating thickness could be determined by the coating thickness rather than the crack length [25]. Furthermore, for steady-state cracking in coatings, the total strain energy change is determined by the coating thickness $t$ and independent of crack profiles, thus the energy release rate can be derived from the total strain energy change $\Delta U_{\varepsilon}$ as [25]

$$
G_{\varepsilon}=\frac{\Delta U_{\varepsilon}}{t} \tag{2}
$$

$$
\Delta U_{\varepsilon}=-\frac{\pi F(\Sigma) \sigma^{2} t^{2}}{E_{c}} \tag{3}
$$

where $\Sigma$ is the elastic modulus ratio with $\Sigma=E_{c}/E_{s}$, $E_{c}$ and $E_{s}$,are the Young's modulus of the brittle coating and ductile substrate, respectively. $F(\Sigma)$ is a function about the elastic modulus ratio $\Sigma$ and can be defined as [25]

$$
F(\Sigma)=\int_{0}^{1} \alpha g(\alpha, \Sigma) \mathrm{d} \alpha \tag{4}
$$

where $\mathrm{g}(\alpha, \Sigma)$ is a function of the ratio of crack depth $d$, defined in Fig. 4, to coating thickness $t$, and $\alpha=d/t$. Some values of the elastic modulus related function $F(\Sigma)$ were obtained and are presented in Table 1 [25]. $\sigma$ is the total stress, defined as [26]

$$
\sigma=\sigma_{0}+\sigma_{\infty} \frac{E_{c}}{E_{s}} \tag{5}
$$

where $\sigma_{\infty}$ is the applied tension; $\sigma_{0}$ is the residual stress in the coating induced during deposition process. Finally, the stress intensity factor of the coating/substrate system can be described as [26]

$$
K_{s}=\sqrt{G_{\varepsilon} E_{c}} \tag{6}
$$

From Eq. (2) and Eq. (3), the stress intensity factor can be further described as

$$
K_{s}=\sigma \sqrt{\pi F(\Sigma)} \tag{7}
$$

For through-thickness cracks, however, the interface sliding in certain areas between the coating and substrate should be considered. For a coating whose thickness is much smaller than that of substrates suffer a constant shear stress $\tau$ in the interface sliding region, as schematically shown in Fig. 5, which can be determined by the yield strength of the substrate material for the case that either sliding or yielding occurs in the coating near the interface. Therefore, the strain energy change in Eq. (2) is replaced by the total energy variation $\Delta U$, which includes the energy dissipation caused by the interface sliding, as expressed below [26]:

$$
\Delta U=\Delta W+\Delta W_{d}+\Delta U_{s}+\Delta U_{\varepsilon} \tag{8}
$$

where $\Delta W$ is the total work done by the applied load, $\Delta W_{d}$ is the dissipated energy caused by interface sliding, $\Delta U_{s}$ is the strain energy variation due to interface sliding. These terms were derived by Evans et al. [27] and Marshall et al. [28] in terms of fracture mechanics:

$$
\Delta W=-\frac{\sigma^{3} t^{2}}{\tau E_{c}} \tag{9}
$$

$$
\Delta W_{d}=\frac{\sigma^{3} t^{2}}{3 \tau E_{c}} \tag{10}
$$

$$
\Delta U_{s}=\frac{\sigma^{3} t^{2}}{3 \tau E_{c}} \tag{11}
$$

Then
$$
\Delta U=-\frac{\sigma^{2} t^{2}}{E_{c}}\left(\frac{\sigma}{3 \tau}+\pi F(\Sigma)\right) \tag{12}
$$

The strain energy release rate in this case is expressed as [26]

$$
G_{\varepsilon}=-\frac{\Delta U}{t}=\frac{\sigma^{2} t}{E_{c}}\left(\frac{\sigma}{3 \tau}+\pi F(\Sigma)\right)
\tag{13}
$$

From Eq. (6), the stress intensity factor of the coating/substrate system can be obtained as

$$
K_{s}=\left[\sigma^{2} t\left(\frac{\sigma}{\sqrt{3} Y}+\pi F(\Sigma)\right)\right]^{1 / 2}
\tag{14}
$$

where $Y$ is the yield strength of the substrate material and $Y=\sqrt{3} \tau$ based on Von Mises yield criterion [29].

### 2.4. Formulation of temperature effect

Based on the Arrhenius-type equation and rate controlling theory using $J$ expression, the temperature effect is incorporated into the fracture toughness of a materials as [22]

$$
K_{I C}=\sqrt{\frac{E\left(J_{s}+J_{d}\right)}{1-v^{2}}}
\tag{15}
$$

$$
J_{d}=J_{0} \exp \left[-\frac{b^{2}\left(\gamma_{F}+U_{P-N}\right)}{k T}\right]
\tag{16}
$$

$$
J_{0}=\rho \pi h^{2}\left(\frac{k T}{b^{2}}\right)
\tag{17}
$$

where $J_{s}$ is elastic work which equals to $2 \gamma_{s}$ and $\gamma_{s}$ is surface energy, $J_{d}$ is plastic dissipation energy for per unit area of newly created crack, $b$ is Burgers vector, $\gamma_{F}$ is generalized stacking fault energy, $h$ is the dimension of plastic zone, defined in Fig. 4. $U_{P-N}$ is (P-N) barrier energy, $E$ and $v$ are Young's modulus and Poisson's ratio of the material, respectively, $\rho$ is the dislocation density, $T$ is absolute temperature, and $k$ is the Boltzmann constant.

The brittle coating/ductile substrate system studied in this research consists of a composite (WC-10Co4Cr) coated on AISI 1018 low carbon steel substrate. The coating was fabricated via the high velocity oxygen fuel (HVOF) process by mixing WC and CoCr alloy powders. The chemical composition of the composite coating material is 86% WC, 10% Co and 4% Cr (in weight), corresponding to the volume ratio 76.42% WC, 15.77% Co and 7.81% Cr, and the stoichiometric formula of WC powder is 6.13 wt.% C and 93.87 wt.% W. The SEM image of cross section of the coating specimen can be found in Fig. 6. The light region is $\delta$-WC phase and the dark region is $\alpha$-Co phase. The coating thickness $t$ is measured to be 45 $\mu$m. From the indentation test observation on this coating/substrate system under a load ranging between 196 to 720 N at room temperature, the fully developed radial cracks at each corner are all through-thickness cracks, but they all stop at the interface and do not go into the substrate, as shown in Fig. 7 [12]. Therefore, the area of the plastic zone can be approximated as $ht$ and Eq. (17) is modified as

$$
J_{0}=2 \rho h t\left(\frac{k T}{b^{2}}\right) \tag{18}
$$

In the present research, based on the microcrack formation and dislocation movement theories discussed above, the temperature-dependent fracture toughness model for brittle coating/ductile substrate systems under indentation loading is proposed as follows, in terms of strain energy release rate and in consistence with the $J$ expression of Eq. (16) and Eq. (18).

$$
G_{d}=G_{0} \exp \left(-\frac{\frac{G_{e}}{n}\left(\frac{\delta}{m}\right)^{2}}{k T}\right)
\tag{19}
$$

$$
G_{0}=m A \rho_{c} \frac{k T}{\left(\frac{\delta}{m}\right)^{2}}
\tag{20}
$$

$$
K_{s}=\sqrt{G_{d} E_{c}}
\tag{21}
$$

The strain energy release rate $G_{d}$ of Eq. (19) has the same meaning with the $J$ expression of Eq. (16). In Eq. (20) $\rho_{c}$ is microcrack areal density. Since the microcracks that merge together to form radial cracks are generated due to the residual stresses stored in the plastic zone, the parameter $A$ can be determined as the radial crack area and expressed as $A=2 c t$, where $c$ is radial crack length, as indicated in Fig. 4. The term $G_{0}$ can be interpreted as the maximum plastic work per unit area of crack extension, where $G_{0} / m A \rho_{c}$ stands for the energy needed to overcome by the atoms moving a single characteristic length in terms of Burgers vector. $G_{\varepsilon}$ is the strain energy release rate at room temperature, which can be obtained from Eq. (13). It describes the energy dissipation during the crack propagation process, and only if the dislocation motion can overcome the energy barrier would microcracks be generated in the plastic deformation zone.

The scale-linking parameter $n$ is introduced to relate the macro strain energy release rate for crack extension to the micro-level energy which must be overcome by the dislocation motion of atoms such that the strain energy release rate at room temperature evaluated from Eq. (13) on macro scale should be equivalent to the strain energy release rate evaluated using

Eq. (19) for room temperature on micro scale. This link has the same concept with the relationship between the size of microcracks in terms of CTOD $\delta$ and the magnitude of Burgers vector $b$, with $mb = \delta$, as discussed above. The microcrack areal density $\rho_{c}$ for coatings is given as [30]

$$
\rho_{c}=\frac{1}{t D} \tag{22}
$$

where $D$ is crack spacing, which can be estimated by shear lag analysis [31] and crack density versus applied strain relation [32]. However, this parameter is calculated in terms of the interface shear stress and plastic zone residual stress theory [33] in the present research, because this theory is consistent with the entire model formulation, which can be interpreted as the reciprocal of liner density and is expressed for brittle coating/ductile substrate systems as

$$
D=\frac{2 t \sigma_{r}}{\tau} \tag{23}
$$

Based on the Lawn's theory [6], for a well-developed median/radial crack, the action of the residual plastic zone can be considered as a point force $P_{r}$ acting at the crack center, as shown in Fig. 8. The residual stresses $\sigma_{r}$ stored in the plastic zone during the loading period can be estimated as [34]

$$
\sigma_{r}=p\left\{\frac{3\left[\ln \left(\frac{r}{a_{c}}\right)+\frac{1}{2}\right]}{1+3 \ln f}-1-\frac{1}{2\left(\frac{r}{a_{c}}\right)^{3}}\right\} \quad\left(1<r / a_{c}<f\right) \tag{24}
$$

where $p$ stands for the indentation pressure, $r$ is the distance from cavity center, $f$ is the ratio between the radius of plastic zone $h$ (Fig. 4) and the half diagonal of indentation impression $a_c$ (Fig. 4), as expressed below

$$
f=\frac{h}{a_{c}}=\sqrt{\frac{E_{c}}{H_{c.}}} \cdot(\cos \psi)^{1 / 3} \tag{25}
$$

By assuming the stress in plastic zone constant, Eq. (24) can be modified as

$$
\sigma_{r}=p\left\{\frac{3\left[\ln f+\frac{1}{2}\right]}{1+3 \ln f}-1-\frac{1}{2 f^{3}}\right\} \tag{26}
$$

### 2.5. Two approaches for indentation pressure

By the definition of indentation pressure, it can be determined by the following equation

$$
p=\frac{P}{2 a_{c}^{2}} \tag{27}
$$

where $P$ is the applied indentation load. Alternatively, by recognizing that the expressions of indentation pressure and Vickers hardness have the same form, and further taking into account the effect of substrate, the indentation pressure can be the composite hardness $H_m$ of the coating/substrate system, given by Demidova [12] and Ichimura et al. [35]

$$
H_{m}=3\left(\frac{t}{2 a_{c}}\right)\left(\frac{H_{c}}{E_{c}}\right)^{1 / 2} \cdot\left(H_{c}-H_{s}\right)(\tan \psi)^{1 / 3}+H_{s} \tag{28}
$$

where $H_s$ is the hardness of substrate. In this study, both the basic indentation pressure (approach 1) and the composite hardness (approach 2) are used to determine the residual stress thus the corresponding model parameters.

### 2.6. Solution procedure of temperature-dependent fracture toughness

To obtain the temperature-dependent fracture toughness using Eq. (21) based on the microcrack formation theory, the strain energy release rate $G_d$ needs to be determined first from Eq. (19). Then the Burgers vector $b=\frac{\delta}{m}$ for the WC-10Co4Cr composite coating should be calculated in terms of the Burgers vectors of $\delta$-WC phase and $\alpha$-Co phase. The strain energy release rate at room temperature $G_{\varepsilon}$ can be computed from Eq. (13). The scale-linking parameter $n$ is determined by equaling the strain energy release rate at room temperature evaluated using Eq. (13) to the strain energy release rate evaluated using Eq. (19) for room temperature. Once the $G_{\varepsilon}$ value is available, the CTOD $\delta$ can be obtained using Eq. (1). With the $b$ and $\delta$ values, the $m$ value can be calculated from $m=\frac{\delta}{b}$. The microcrack areal density $\rho_c$ in Eq. (20) is related to the residual stress stored in the plastic zone during the loading period, which is determined using the basic pressure approach and the composite hardness approach, respectively.

## 3. Results and discussion

### 3.1. Model parameters

To calculate the $m$ value, the CTOD $\delta$ and the Burgers vector $b$ for the WC-10Co4Cr composite coating must be determined. Since slip system can only be

identified in single-phase crystal structure, the Burgers vector of dislocation for WC-10Co4Cr composite cannot be obtained directly. In $\delta$-WC phase, the Burgers vector $1/3[1\overline{2}10]$ is observed on the prismatic slip plane [36]. On the prismatic slip plane, the dislocation type contains both edge and screw dislocations, and the ratio of edge dislocation to screw dislocation is 3:1 based on the slip angle on this specific plane for WC [37]. For FCC $\alpha$-Co phase, similar to the dislocation in $\delta$-WC phase, it consists of both screw and edge dislocations under indentation loading. The Burgers vector of $1/2[110]$ on the slip plane $\{111\}$ could point to either edge dislocation or screw dislocation [38], and one of its partial dislocations, the Burgers vector of $1/6[11\overline{2}]$, which corresponds to the edge dislocation [39]. For WC-10Co4Cr composite the magnitudes of the Burgers vectors of $\delta$-WC phase and $\alpha$-Co phase were analyzed and calculated to be 0.2906 nm and 0.2519 nm, respectively [40]. The Burgers vector magnitude of WC-10Co4Cr composite should be between these two values. In fact, this magnitude does not have an exact physical meaning and it is only for the solution of Eq. (19) which requires the value within the order of Burgers vector. Since the unconstrained mixture model for composite fracture toughness [41] takes into account the effect of volume fraction of brittle phase, while this ratio is associated with the plastic deformation resistance thus also with the Burgers vector of the composite, it may be applied to obtain the Burgers vector magnitude $b$ of WC-10Co4Cr composite from that of brittle $\delta$-WC phase $b_b$ and that of ductile $\alpha$-Co phase $b_d$ as

$$
b=b_{b}\left[1+\frac{2}{\sqrt{\pi}} \sqrt{1-V_{f}}\left(\left(\frac{b_{d}}{b_{b}}\right)^{2}-1\right)\right]^{1 / 2} \tag{29}
$$

where $V_f$ is the volume fraction of brittle phase (δ-WC phase). Thus $b$ is calculated to be 0.2701 nm.

Based on the mechanical properties of WC-10Co4Cr coating and 1018 low carbon steel substrate materials in Table 2 [12], the elastic modulus ratio $\Sigma$ for this coating/substrate system is calculated to be 1.24. Then the value of function $F(\Sigma)$ is determined to be 0.64 from the graph of $F(\Sigma)$ versus the elastic modulus ratio $\Sigma$ in Fig. 9.

The CTOD $\delta$ is determined based on the basic properties of the coating material and independent of indentation load, as demonstrated by Eq. (1) and Eq. (13). The yield stress $Y$ of 1018 low carbon steel is 380 MPa [42], giving $\tau=Y / \sqrt{3} \approx 220 \mathrm{MPa}$, the stress $\sigma$ in Eq. (13) can be assumed approximately equal to the tensile strength (~223 MPa) [43] of the coating when concerning the extreme case — the cracks propagate, which is governed by the fracture toughness of the coating/substrate system. The yield stress $\sigma_{c}$ of the WC-10Co4Cr coating is reported 210 MPa [44], thus $\tau_{c}=\sigma_{c} / \sqrt{3}=121 \mathrm{MPa}$. Using Eq. (1) and Eq. (13) with these values and $F(\Sigma)=0.64$, $\delta$ is calculated to be 32 nm. Accordingly, $m=\delta / b=$ 118.47.

### 3.2. Temperature-dependent fracture toughness

Approach 1 uses the basic pressure definition Eq. (27) to calculate the pressure $p$ and thereby the residual stress $\sigma_{r}$. To determine the value of the microcrack areal density $\rho_{c}$,

the crack geometry data are needed, which were obtainable from the Vickers indentation tests on the HVOF WC-10Co4Cr coating/1018 low carbon steel substrate system at different loads of 196, 294, 392, 490, and 720 N by Demidova et al. [12]. The half angle ($\psi$) of indenter is $68^\circ$. To ensure non-interference of the residual fields generated by the Vickers indenter, the indentation marks were made at least 2.5 times Vickers diagonals away from each other and the specimen edges. At least three indentation marks were generated at each load. The radial crack lengths and indentation diagonal lengths under each indentation load as well as the calculated pressure are reported in Table 3 and Table 4. The errors of the indentation test data should be analyzed before they are used for the fracture toughness calculation. The average diagonal length (mean of two diagonal lengths) for each indentation impression ranges from 616.6 to $737.5\ \mu\text{m}$ under the indentation load of 196 N. The maximum error is about $29\ \mu\text{m}$ for other indentation loads. In order to select proper indentation diagonal length data for the fracture toughness calculation, the average and maximum values of three pairs of indentation diagonal length under each indentation load are used, respectively. Then the microcrack density $\rho_c$, the parameter $n$, the strain energy release $G_s$, and the fracture toughness $K_s$ at room temperature, are calculated using MATLAB 2010b and the results are presented in Table 5. It is shown that the microcrack density decreases with increasing indentation load. This should be due to the effect of ductile substrate when the load is higher. The indenter goes deeper into the coating with the applied indentation load, which aggravates the substrate effect. The fracture toughness values of the WC-10Co4Cr coating/1018 low carbon steel

substrate system calculated for a temperature range between 298 K and 1000 K from approach 1 are summarized in Table 6.

Approach 2 replaces the pressure $p$ of Eq. (27) by using the composite hardness $H_{m}$ of Eq. (28). The same indentation test data are used to determine the composite hardness and other model parameters. The calculated composite hardness values for each indentation load are reported in Table 4 and the values of microcrack density $\rho_{c}$, the parameter $n$, the strain energy release $G_{\varepsilon}$, and the fracture toughness $K_{s}$ at room temperature, calculated using approach 2 are reported in Table 7. The fracture toughness of the WC-10Co4Cr coating/1018 low carbon steel substrate system for a range of temperature is finally calculated and the results are presented in Table 8.

### 3.3. Discussion

From the fracture toughness results in Table 6 and Table 8, for each temperature the fracture toughness of the WC-10Co4Cr coating on 1018 low carbon steel substrate system, calculated from approach 1 exhibits consistently load-independent characteristic, which coincides with the attribute of fracture toughness, because it is a material property and should be independent of load. However, the fracture toughness for elevated temperatures calculated from approach 2 shows slightly increasing trend with indentation load. With the view of material property point, approach 1 is more applicable than approach 2. In Eq. (27) $a_{c}$ is load-dependent thus the ratio — the load $P$ to the half indentation diagonal $a_{c}$ may be

load-independent, but for the composite hardness $H_m$, in Eq. (28) only $a_c$ is load-dependent,
which would lead to the variation of $H_m$ with indentation load.

In addition, although the error between the average and maximum indentation
diagonal length does exist, the calculated fracture toughness using these two values does not
show distinct deviation, as seen in Table 6 and Table 8. For the fracture toughness
determined using approach 1, at each temperature, not only the values calculated with the
average and maximum indentation diagonal length but also the values calculated for different
indentation loads are all very close, thus the average value of fracture toughness for each
temperature is plotted against temperature in Fig. 10. The standard deviations of the fracture
toughness values for each temperature are calculated for error analysis and are reported in
Table 6. It is found that the errors are very small but increase with the temperature rising.

For the fracture toughness obtained using approach 2, although the difference in the
fracture toughness values calculated with the average and maximum indentation diagonal
length is trivial, these values do exhibit variation with indentation load. Therefore, for this
approach, at each indentation load the average fracture toughness calculated with the average
and maximum indentation diagonal length is plotted against temperature in Fig. 11. It is seen
that the fracture toughness of the WC-10Co4Cr coating/1018 steel substrate system increases
with temperature rising, showing a nonlinear relationship, and the two approaches yield
consistent results.

However, as mentioned earlier, due to the complicity of high-temperature tests and the limitation of testing facilities, the proposed model is not validated by experimental data. For room-temperature fracture toughness of the WC-10Co4Cr coating/1018 steel substrate system, Demidova's model derives the value of $1.21$ MPa m$^{1/2}$ and the proposed model $2.14$ MPa m$^{1/2}$, which are in the same order. Additionally, as demonstrated by Eq. (19) to Eq. (21), the fracture toughness is a continuous function of the variable temperature, thus the consistency of the room-temperature fracture toughness can suggest similar expectation for the high-temperature fracture toughness. Moreover, the crack profiles of the WC-10Co4Cr coating/1018 steel substrate system used to obtain the crack dimensions for the model were determined under indentation test at room temperature, therefore it would definitely cause errors in the results when using them for high-temperature fracture toughness assessment. Nevertheless, according to the results from the proposed model, the fracture toughness of the WC-10Co4Cr coating/1018 steel substrate system increases with temperature. This means that using the room-temperature experimental data for the high-temperature fracture toughness analysis would give conservative or safe results. For accurate evaluating the fracture toughness of brittle coating/ductile substrate systems using the proposed model, of course, high-temperature indentation test is needed.

### 4. Conclusions

A temperature-dependent fracture toughness model is proposed for brittle coating/ductile substrate systems in terms of microcrack formation theory. The model requires
the radial crack dimensions which must be obtained from indentation test.

The temperature effect is modeled based on the Arrhenius-type equation and rate controlling theory. A scale-linking parameter $n$ is introduced in the stain energy release rate equation of the model, which can be determined by equaling the stain energy release at room temperature to that calculated from the conventional energy release rate equation for a brittle coating deposited on a ductile substrate under indentation.

Both the basic indentation pressure and composite hardness approaches, taking into account the substrate effect, are used to determine the model parameters. The temperature-dependent fracture toughness evaluated using the former is more reasonable than that using the latter with respect to the nature of material property, but both approaches demonstrate that the fracture toughness of the WC-10Co4Cr coating/1018 steel substrate system increases with temperature in a nonlinear relation.

### Acknowledgement

The authors are grateful for the financial support from Natural Science & Engineering Research Council of Canada (NSERC), the in-kind support from National Research Council Canada (NRC) and both financial and in-kind support from Kennametal Stellite Inc.

### References

[1] Y. Yamazaki, M. Arai, Y. Miyashita, H. Waki, M. Suzuki, Determination of interfacial fracture toughness of thermal spray coatings by indentation, J. Therm. Spray Technol. 22 (8) (2013) 1358–1365.

[2] S. Smith, R. Scattergood, Crack-shape effects for indentation fracture toughness measurements, J. Am. Ceram. Soc. 75 (2) (1992) 305-315.

[3] O.M. Abdelhadi, L. Ladani, J. Razmi, Fracture toughness of bonds using interfacial stresses in four-point bending test, Mech. Mater. 43 (12) (2011) 885-900.

[4] Z. Chen, Z.H. Gan, Fracture toughness measurement of thin films on compliant substrate using controlled buckling test, Thin Solid Films 515 (6) (2007) 3305-3309.

[5] A.T. Akono, F.J. Ulm, Scratch test model for the determination of fracture toughness, Eng. Frac. Mech. 78 (2) (2011) 334-342.

[6] B.R. Lawn, A.G. Evans, D.B. Marshall, Elastic/plastic indentation damage in ceramics: The median/radial crack system, J. Am. Ceram. Soc. 63 (1980) 574-581.

[7] H. Li, K.A. Khor, P. Cheang, Young's modulus and fracture toughness determination of high velocity oxygen fuel sprayed bioceramic coatings, Surf. Coat. Technol. 155 (2002) 21-32.

[8] P. Kodali, K.C. Walter, M. Nastasi, Investigation of mechanical and tribological properties of amorphous diamond-like carbon coatings, Tribol. Inter. 30 (8) (1997) 591-598.

[9] J. Mecholsky, Y. Tsai, W. Drawl, Fracture studies of diamond films on silicon, J. Appl. Phys. 71 (1992) 4875-4881.

[10] D.B. Marshall, B.R. Lawn, An indentation technique for measuring stresses in tempered glass surfaces, J. Am. Ceram. Soc. 60 (1-2) (2006) 86-87.

[11] J. Malzbender, G. de With, J.M.J. den Toonder, Elastic modulus, indentation pressure and fracture toughness of hybrid coatings on glass, Thin Solid Films 366 (2000) 139-149.

[12] N.V. Demidova, X.J. Wu, R. Liu, A fracture toughness model for brittle coating on ductile substrate under indentation loading, Eng. Frac. Mech. 82 (2012) 17-28.

[13] R. Hill, The Mathematical Theory of Plasticity, Oxford University Press Inc., New York, 1950.

[14] G. Anstis, P. Chantikul, B. Lawn, D. Marshall, A critical evaluation of indentation techniques for measuring fracture toughness: I, Direct crack measurements, J. Am. Ceram. Soc. l.64 (9) (1981) 533-538.

[15] Z. Xia, W.A. Curtin, B.W. Sheldon, A new method to evaluate the fracture toughness of thin films, Acta Mater. 52 (2004) 3507-3517.

[16] J.H. Lee, Y.F. Gao, K.E. Johanns, G.M. Pharr, Cohesive interface simulations of indentation cracking as a fracture toughness measurement method for brittle materials, Acta Materialia 60 (2012) 5448-5467.

[17] H.C. Hyun, F. Rickhey, J.H. Lee, M. Kim, H. Lee, Evaluation of indentation fracture toughness for brittle materials based on the cohesive zone finite element method, Eng. Frac. Mech. 134 (2015) 304-316.

[18] B.R. Lawn, M.V. Swain, Microfracture beneath point indentations in brittle solids, J. Mater. Sci. 10 (1975) 113-122.

[19] M. Ortiz, Microcrack coalescence and macroscopic crack growth initiation in brittle solids, Inter. J. Solid. Struc. 24 (1988) 231-250.

[20] T.L. Anderson, Fracture Mechanics: Fundamentals and Applications, CRC Press, Boca Raton, 1994.

[21] M.J. Murray, Fracture of WC-Co alloys: An example of spatially constrained crack tip opening displacement, Proceedings of the Royal Society of London A: Mathematical, Physical and Engineering Sciences 356 (1977) 483-508.

[22] K.S. Chan, Relationships of fracture toughness and dislocation mobility in intermetallics. Metall. Mater. Trans. A 34 (10) (2003) 2315-2328.

[23] W.D. Callister Jr, D.G. Rethwisch, Materials Science and Engineering — An Introduction: Atomic Structure and Interatomic Bonding, John Wiley & Sons, Inc., New York, 2010.

[24] J. Weertman, Dislocation Based Fracture Mechanics, World Scientific Publishing Co. Pte. Ltd, Singapore, 1996.

[25] M.S. Hu, A.G. Evans, The cracking and decohesion of thin films on ductile substrates, Acta Metallurgica 37 (1989) 917-925.

[26] J.L. Beuth, N.W. Klingbeil, Cracking of thin films bonded to elastic-plastic substrates, J. Mech. Phys. Solid. 44 (1996) 1411-1428.

[27] A.G. Evans, M.D. Drory, M.S. Hu, The cracking and decohesion of thin films, J. Mater. Res. 3 (1988) 1043-1049.

[28] D.B. Marshall, B.N. Cox, A.G. Evans, The mechanics of matrix cracking in brittle-matrix fiber composites, Acta Metallurgica 33 (1985) 2013-2021.

[29] Y. Wang, A. Hamza, E. Ma, Temperature-dependent strain rate sensitivity and activation volume of nanocrystalline Ni, Acta Materialia 54 (2006) 2715-2726.

[30] S. Liu, J.A. Nairn, Fracture mechanics analysis of composite microcracking: Experimental results in fatigue, Proceedings of the 5th Technical Conference on Composite Materials, American Society of Composites (1990) 287-295.

[31] M. Yanaka, Y. Tsukahara, N. Nakaso, N. Takeda, Cracking phenomena of brittle films in nanostructure composites analysed by a modified shear lag model with residual strain, J. Mater. Sci. 33 (1998) 2111-2119.

[32] C.H. Hsueha, A.A. Wereszczak, Multiple cracking of brittle coatings on strained substrates, J. Appl. Phys. 96 (6) (2004) 3501-3506.

[33] M.M. Nagl, W.T. Evans, The mechanical failure of oxide scales under tensile or compressive load, J. Mater. Sci. 28 (1993) 6247-6260.

[34] S.S. Chiang, D.B. Marshall, A.G. Evans, The response of solids to elastic/plastic indentation, I. Stresses and residual stresses, J. Appl. Phys. 53 (1982) 298-311.

[35] H. Ichimura, F.M. Rodriguez, A. Rodrigo, The composite and film hardness of TiN coatings prepared by cathodic arc evaporation, Surf. Coat. Technol. 127 (2-3) (2000) 138-143.

[36] F.L. Zhang, C.Y. Wang, M. Zhu, Nanostructured WC/Co composite powder prepared by high energy ball milling, Scripta Materialia 49 (2003) 1123-1128.

[37] T. Ungár, A. Borbély, G.R. Goren-Muginstein, S. Berger, A.R. Rosen, Particle-size, size distribution and dislocations in nanocrystalline tungsten-carbide, Nanostruc. Mater. 11 (1999) 103-113.

[38] R. Bauer, E.A. Jägle, W. Baumann, E.J. Mittemeijer, Kinetics of the allotropic hcp-fcc phase transformation in cobalt, Philoso. Maga. 91 (2011) 435-457.

[39] W.A. Jesser, J.W. Matthews, Growth of F.C.C. cobalt on nickel, Acta Metall. 16 (1968) 1307-1311.

[40] Y.C. Gu, Temperature-Dependent Fracture Toughness Evaluation of WC-10Co4Cr Coating/1018 Low Carbon Steel Substrate System, Master Thesis, Carleton University, Ottawa, Canada, 2015.

[41] A.F. Bower, M. Ortiz, A three-dimensional analysis of crack trapping and bridging by Tough Particles, J. Mech. Phys. Solid. 39 (6) (1991) 815-858.

[42] H. Suzuki, A.J. McEvily, Microstructure effects on fatigue crack growth in a low carbon steel, Metall. Trans. A — Phys. Metall. Mater. Sci. 10 (4) (1979) 475-481.

[43] S.P. Lu, O.Y. Kwon, Y. Guo, Wear behavior of brazed WC/NiCrBSi(Co) composite coatings, Wear 254 (2003) 421–428.

[44] V.A. Ivensen, O.N. Éiduk, V.A. Chistyakova, Dependence of the yield strength of WC-Co hard alloys on their cobalt content and tungsten carbide grain size, Soviet Powd. Metall. Metal Cera. 13 (1974) 413-415.

![](./images/811102799034056704_2.jpg)

Fig. 1. Schematic illustration of radial cracks in a brittle coating under Vickers indentation.

![](./images/811102799034056704_3.jpg)

Fig. 2. Schematic illustration of microcrack and macrocrack formation in brittle materials under Vickers indentation.

![](./images/811102799034056704_4.jpg)

Fig. 3. Schematic illustration of microcrack formation and the movement of atoms.

![](./images/811102799034056704_5.jpg)

Fig. 4. Schematic crack profiles in a solid body under Vickers indentation loading: (a)
median/radial crack system, (b) indentation and plastic zone geometry.

### Through-thickness crack

![](./images/811102799034056704_6.jpg)

Fig. 5. A constant shear stress at the coating/substrate interface.

![](./images/811102799034056704_7.jpg)

Fig. 6. SEM image of cross section of WC-10Co4Cr coating on AISI 1018 low carbon steel substrate prepared via the HVOF process.

![](./images/811102799034056704_8.jpg)

Fig. 7. Focused ion beam images of crack profiles in WC-10Co4Cr coating/1018 steel substrate system under a Vickers indentation load of 196 N:
(a) top view, (b) cross-sectional view [12].

![](./images/811102799034056704_9.jpg)

Fig. 8. Illustration of the effect of the residual plastic zone.

![](./images/811102799034056704_10.jpg)

<table>
  <tr>
    <td>576</td>
    <td>1.2323</td>
    <td>0.64381</td>
  </tr>
  <tr>
    <td>577</td>
    <td>1.2345</td>
    <td>0.644</td>
  </tr>
  <tr>
    <td>578</td>
    <td>1.2367</td>
    <td>0.64419</td>
  </tr>
  <tr>
    <td>579</td>
    <td>1.2389</td>
    <td>0.64438</td>
  </tr>
  <tr>
    <td>580</td>
    <td>1.2411</td>
    <td>0.64457</td>
  </tr>
  <tr>
    <td>581</td>
    <td>1.2433</td>
    <td>0.64476</td>
  </tr>
  <tr>
    <td>582</td>
    <td>1.24551</td>
    <td>0.64495</td>
  </tr>
  <tr>
    <td>583</td>
    <td>1.24771</td>
    <td>0.64514</td>
  </tr>
  <tr>
    <td>584</td>
    <td>1.24991</td>
    <td>0.64533</td>
  </tr>
</table>

Fig. 9. $F(\Sigma)$ versus the elastic modulus ratio $\Sigma$: (a) graph, (b) polynomial fitting data.

![](./images/811102799034056704_11.jpg)

Fig. 10. Average fracture toughness of WC-10Co4Cr coating/1018 steel substrate system versus temperature from different indentation loads using approach 1.

![](./images/811102799034056704_12.jpg)

Fig. 11. Fracture toughness of WC-10Co4Cr coating/1018 steel substrate system versus temperature using approach 2.

Table 1 Values of function $F(\Sigma)$ corresponding to different elastic modulus ratios [24].

<table>
<thead>
<tr>
<th>$\Sigma$</th>
<th>$F(\Sigma)$</th>
</tr>
</thead>
<tbody>
<tr>
<td>4</td>
<td>0.79</td>
</tr>
<tr>
<td>3</td>
<td>0.75</td>
</tr>
<tr>
<td>2</td>
<td>0.70</td>
</tr>
<tr>
<td>1</td>
<td>0.62</td>
</tr>
<tr>
<td>1/2</td>
<td>0.57</td>
</tr>
<tr>
<td>1/3</td>
<td>0.54</td>
</tr>
</tbody>
</table>

Table 2 Mechanical properties of WC-10Co4Cr coating and 1018 low carbon steel substrate materials [12].

<table>
<thead>
<tr>
<th>Material</th>
<th>$E$ (GPa)</th>
<th>$H$ (GPa)</th>
<th>$\boldsymbol{\nu}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>WC-10Co4Cr</td>
<td>310</td>
<td>10.4</td>
<td>0.3</td>
</tr>
<tr>
<td>1018 low carbon steel</td>
<td>250</td>
<td>1.05</td>
<td>-</td>
</tr>
</tbody>
</table>

Table 3 Radial crack length $c$ under each indentation load [12].

<table>
  <thead>
    <tr>
      <th>Indentation mark #</th>
      <th>Load $P$ (N)</th>
      <th>Radial crack length $c$ (μm)</th>
      <th>Average value $c_{avg}$ (μm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td rowspan="5">196</td>
      <td>433.0</td>
      <td rowspan="5">497.700</td>
    </tr>
    <tr>
      <td>2</td>
      <td>474.5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>508.5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>521.5</td>
    </tr>
    <tr>
      <td>5</td>
      <td>551.0</td>
    </tr>
    <tr>
      <td>6</td>
      <td rowspan="6">294</td>
      <td>581.0</td>
      <td rowspan="6">622.330</td>
    </tr>
    <tr>
      <td>7</td>
      <td>610.5</td>
    </tr>
    <tr>
      <td>8</td>
      <td>621.5</td>
    </tr>
    <tr>
      <td>9</td>
      <td>641.5</td>
    </tr>
    <tr>
      <td>10</td>
      <td>646.5</td>
    </tr>
    <tr>
      <td>11</td>
      <td>633.0</td>
    </tr>
    <tr>
      <td>12</td>
      <td rowspan="4">392</td>
      <td>653.5</td>
      <td rowspan="4">686.625</td>
    </tr>
    <tr>
      <td>13</td>
      <td>678.5</td>
    </tr>
    <tr>
      <td>14</td>
      <td>684.0</td>
    </tr>
    <tr>
      <td>15</td>
      <td>730.5</td>
    </tr>
    <tr>
      <td>16</td>
      <td rowspan="4">490</td>
      <td>696.0</td>
      <td rowspan="4">727.875</td>
    </tr>
    <tr>
      <td>17</td>
      <td>715.5</td>
    </tr>
    <tr>
      <td>18</td>
      <td>718.5</td>
    </tr>
    <tr>
      <td>19</td>
      <td>781.5</td>
    </tr>
    <tr>
      <td>21</td>
      <td rowspan="4">720</td>
      <td>872.5</td>
      <td rowspan="4">859.100</td>
    </tr>
    <tr>
      <td>22</td>
      <td>868.5</td>
    </tr>
    <tr>
      <td>23</td>
      <td>785.5</td>
    </tr>
    <tr>
      <td>24</td>
      <td>864.0</td>
    </tr>
  </tbody>
</table>

Table 4 Indentation diagonal $2a_c$ [12] and calculated model parameters
under each indentation load.

<table>
  <thead>
    <tr>
      <th>Indentation<br>mark #</th>
      <th>Load $P$ (N)</th>
      <th>Indentation diagonal<br>$2a_c$ (µm)</th>
      <th>Pressure<br>$p$ (GPa)</th>
      <th>Composite hardness<br>$H_m$ (GPa)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td rowspan="3">196</td>
      <td>616.6</td>
      <td>1.0310</td>
      <td>1.5572</td>
    </tr>
    <tr>
      <td>2</td>
      <td>737.5</td>
      <td>0.7207</td>
      <td>1.4740</td>
    </tr>
    <tr>
      <td>3</td>
      <td>628.5</td>
      <td>0.9924</td>
      <td>1.5476</td>
    </tr>
    <tr>
      <td>4</td>
      <td rowspan="3">294</td>
      <td>813</td>
      <td>0.8896</td>
      <td>1.4347</td>
    </tr>
    <tr>
      <td>5</td>
      <td>831.5</td>
      <td>0.8505</td>
      <td>1.4261</td>
    </tr>
    <tr>
      <td>6</td>
      <td>831</td>
      <td>0.8515</td>
      <td>1.4263</td>
    </tr>
    <tr>
      <td>7</td>
      <td rowspan="3">392</td>
      <td>852.5</td>
      <td>1.0788</td>
      <td>1.4168</td>
    </tr>
    <tr>
      <td>8</td>
      <td>881.5</td>
      <td>1.0090</td>
      <td>1.4048</td>
    </tr>
    <tr>
      <td>9</td>
      <td>877</td>
      <td>1.0193</td>
      <td>1.4066</td>
    </tr>
    <tr>
      <td>10</td>
      <td rowspan="3">490</td>
      <td>918</td>
      <td>1.1629</td>
      <td>1.3907</td>
    </tr>
    <tr>
      <td>11</td>
      <td>921.5</td>
      <td>1.1541</td>
      <td>1.3894</td>
    </tr>
    <tr>
      <td>12</td>
      <td>916.5</td>
      <td>1.1667</td>
      <td>1.3912</td>
    </tr>
    <tr>
      <td>13</td>
      <td rowspan="3">720</td>
      <td>956.5</td>
      <td>1.5740</td>
      <td>1.3770</td>
    </tr>
    <tr>
      <td>14</td>
      <td>949</td>
      <td>1.5989</td>
      <td>1.3795</td>
    </tr>
    <tr>
      <td>15</td>
      <td>959.5</td>
      <td>1.5641</td>
      <td>1.3759</td>
    </tr>
  </tbody>
</table>

Table 5 Calculated model parameters and room-temperature fracture toughness from the basic indentation pressure approach.

<table>
  <thead>
    <tr>
      <th>Average indentation diagonal $2a_c$ ($\mu$m)</th>
      <th>$n$</th>
      <th>Microcrack density $\rho_c$ ($1/m^2$)</th>
      <th>Strain energy release rate $G_\varepsilon$ ($J/m^2$)</th>
      <th>Fracture toughness $K_s$ ($MPa\cdot m^{1/2}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>616.6</td>
      <td>92.22</td>
      <td>5.9596e+008</td>
      <td>13.4395</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>737.5</td>
      <td>81.00</td>
      <td>8.5257e+008</td>
      <td>13.4395</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>628.5</td>
      <td>90.87</td>
      <td>6.1918e+008</td>
      <td>13.4371</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>813</td>
      <td>80.64</td>
      <td>6.9071e+008</td>
      <td>13.4368</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>831.5</td>
      <td>79.43</td>
      <td>7.2250e+008</td>
      <td>13.4363</td>
      <td>2.1394</td>
    </tr>
    <tr>
      <td>831</td>
      <td>79.47</td>
      <td>7.2163e+008</td>
      <td>13.4405</td>
      <td>2.1398</td>
    </tr>
    <tr>
      <td>852.5</td>
      <td>83.31</td>
      <td>5.6959e+008</td>
      <td>13.4404</td>
      <td>2.1398</td>
    </tr>
    <tr>
      <td>881.5</td>
      <td>81.40</td>
      <td>6.0901e+008</td>
      <td>13.4372</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>877</td>
      <td>81.69</td>
      <td>6.0280e+008</td>
      <td>13.4393</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>918</td>
      <td>83.80</td>
      <td>5.2839e+008</td>
      <td>13.4401</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>921.5</td>
      <td>83.57</td>
      <td>5.3242e+008</td>
      <td>13.4372</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>916.5</td>
      <td>83.89</td>
      <td>5.2666e+008</td>
      <td>13.4372</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>956.5</td>
      <td>88.03</td>
      <td>3.9039e+008</td>
      <td>13.4371</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>949</td>
      <td>88.55</td>
      <td>3.8429e+008</td>
      <td>13.4393</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>959.5</td>
      <td>87.83</td>
      <td>3.9284e+008</td>
      <td>13.4384</td>
      <td>2.1396</td>
    </tr>
  </tbody>
</table>


Table 6 Calculated fracture toughness $K_{s}$ ($\text{MPa} \cdot \text{m}^{1/2}$) for different temperatures
from the basic indentation pressure approach.

<table>
  <thead>
    <tr>
      <th colspan="2">Temperature</th>
      <th>298 K</th>
      <th>400 K</th>
      <th>600 K</th>
      <th>800 K</th>
      <th>1000 K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">196<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.5083</td>
      <td>6.0260</td>
      <td>8.2402</td>
      <td>10.1978</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1397</td>
      <td>3.6078</td>
      <td>6.3680</td>
      <td>8.8273</td>
      <td>11.0135</td>
    </tr>
    <tr>
      <td rowspan="2">294<br>N</td>
      <td>Mean</td>
      <td>2.1397</td>
      <td>3.6275</td>
      <td>6.4368</td>
      <td>8.9464</td>
      <td>11.1796</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1394</td>
      <td>3.6343</td>
      <td>6.4612</td>
      <td>8.9889</td>
      <td>11.2399</td>
    </tr>
    <tr>
      <td rowspan="2">392<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.5893</td>
      <td>6.3038</td>
      <td>8.7166</td>
      <td>10.8585</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1395</td>
      <td>3.6009</td>
      <td>6.3443</td>
      <td>8.7866</td>
      <td>10.9566</td>
    </tr>
    <tr>
      <td rowspan="2">490<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.5634</td>
      <td>6.2146</td>
      <td>8.5632</td>
      <td>10.6458</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1395</td>
      <td>3.5661</td>
      <td>6.2241</td>
      <td>8.5794</td>
      <td>10.6688</td>
    </tr>
    <tr>
      <td rowspan="2">720<br>N</td>
      <td>Mean</td>
      <td>2.1398</td>
      <td>3.4999</td>
      <td>5.9974</td>
      <td>8.1914</td>
      <td>10.1297</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1396</td>
      <td>3.5039</td>
      <td>6.0113</td>
      <td>8.2154</td>
      <td>10.1624</td>
    </tr>
    <tr>
      <td colspan="2">Standard<br>Deviation</td>
      <td>~ 0</td>
      <td>0.0482</td>
      <td>0.1664</td>
      <td>0.2858</td>
      <td>0.3976</td>
    </tr>
  </tbody>
</table>

Table 7 Calculated model parameters and room-temperature fracture toughness from the composite hardness approach.

<table>
  <thead>
    <tr>
      <th>Average<br>indentation<br>diagonal $2a_c$ ($\mu$m)</th>
      <th>$n$</th>
      <th>Microcrack<br>density $\rho_c$<br>($1/m^2$)</th>
      <th>Strain energy<br>release rate $G_\varepsilon$<br>($J/m^2$)</th>
      <th>Fracture toughness<br>$K_s$ ($\text{MPa} \cdot \text{m}^{1/2}$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>616.6</td>
      <td>109.72</td>
      <td>3.9459e+008</td>
      <td>13.4395</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>737.5</td>
      <td>107.01</td>
      <td>4.1686e+008</td>
      <td>13.4380</td>
      <td>2.1396</td>
    </tr>
    <tr>
      <td>628.5</td>
      <td>109.41</td>
      <td>3.9704e+008</td>
      <td>13.4399</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>813</td>
      <td>96.20</td>
      <td>4.2828e+008</td>
      <td>13.4401</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>831.5</td>
      <td>95.96</td>
      <td>4.3087e+008</td>
      <td>13.4376</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>831</td>
      <td>95.97</td>
      <td>4.3081e+008</td>
      <td>13.4392</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>852.5</td>
      <td>92.08</td>
      <td>4.3369e+008</td>
      <td>13.4399</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>881.5</td>
      <td>91.78</td>
      <td>4.3740e+008</td>
      <td>13.4405</td>
      <td>2.1398</td>
    </tr>
    <tr>
      <td>877</td>
      <td>91.82</td>
      <td>4.3684e+008</td>
      <td>13.4385</td>
      <td>2.1396</td>
    </tr>
    <tr>
      <td>918</td>
      <td>89.42</td>
      <td>4.4183e+008</td>
      <td>13.4388</td>
      <td>2.1396</td>
    </tr>
    <tr>
      <td>921.5</td>
      <td>89.39</td>
      <td>4.4225e+008</td>
      <td>13.4394</td>
      <td>2.1397</td>
    </tr>
    <tr>
      <td>916.5</td>
      <td>89.43</td>
      <td>4.4168e+008</td>
      <td>13.4380</td>
      <td>2.1396</td>
    </tr>
    <tr>
      <td>956.5</td>
      <td>83.89</td>
      <td>4.4623e+008</td>
      <td>13.4376</td>
      <td>2.1395</td>
    </tr>
    <tr>
      <td>949</td>
      <td>83.95</td>
      <td>4.4542e+008</td>
      <td>13.4405</td>
      <td>2.1398</td>
    </tr>
    <tr>
      <td>959.5</td>
      <td>83.87</td>
      <td>4.4659e+008</td>
      <td>13.4393</td>
      <td>2.1397</td>
    </tr>
  </tbody>
</table>


Table 8 Calculated fracture toughness $K_{s}$ ($\text{MPa} \cdot \text{m}^{1/2}$) for different temperatures from the composite hardness approach.

<table>
  <thead>
    <tr>
      <th colspan="2">Temperature</th>
      <th>298 K</th>
      <th>400 K</th>
      <th>600 K</th>
      <th>800 K</th>
      <th>1000 K</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">196<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.2794</td>
      <td>5.2747</td>
      <td>6.9800</td>
      <td>8.4687</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1396</td>
      <td>3.2931</td>
      <td>5.3185</td>
      <td>7.0523</td>
      <td>8.5669</td>
    </tr>
    <tr>
      <td rowspan="2">294<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.4017</td>
      <td>5.6703</td>
      <td>7.6384</td>
      <td>9.3673</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1395</td>
      <td>3.4026</td>
      <td>5.6731</td>
      <td>7.6432</td>
      <td>9.3740</td>
    </tr>
    <tr>
      <td rowspan="2">392<br>N</td>
      <td>Mean</td>
      <td>2.1397</td>
      <td>3.4509</td>
      <td>5.8328</td>
      <td>7.9122</td>
      <td>9.7437</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1398</td>
      <td>3.4524</td>
      <td>5.8376</td>
      <td>7.9203</td>
      <td>9.7548</td>
    </tr>
    <tr>
      <td rowspan="2">490<br>N</td>
      <td>Mean</td>
      <td>2.1396</td>
      <td>3.4825</td>
      <td>5.9391</td>
      <td>8.0924</td>
      <td>9.9924</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1397</td>
      <td>3.4830</td>
      <td>5.9403</td>
      <td>8.0944</td>
      <td>9.9951</td>
    </tr>
    <tr>
      <td rowspan="2">720<br>N</td>
      <td>Mean</td>
      <td>2.1395</td>
      <td>3.5610</td>
      <td>6.2065</td>
      <td>8.5493</td>
      <td>10.6265</td>
    </tr>
    <tr>
      <td>Max</td>
      <td>2.1397</td>
      <td>3.5618</td>
      <td>6.2086</td>
      <td>8.5527</td>
      <td>10.6308</td>
    </tr>
  </tbody>
</table>

### Highlights

- Temperature-dependent fracture toughness modeling for brittle coating/ductile substrate systems
- Utilize the Arrhenius-type equation and rate controlling theory to model the temperature effect
- Use indentation approach based on microcrack formation theory
- Use crack tip opening displacement (CTOD) to measure the total growth of a microcrack in tensile direction and the dislocation movement