Accepted Manuscript

Understanding Mechanisms of Carbon Dioxide Conversion into Methane for
Designing Enhanced Catalysts from First-Principles

Dong Yun Shin, Jun Ho Jo, Jai-Young Lee, Dong-Hee Lim

<table>
  <tr>
    <td>PII:</td>
    <td>S2210-271X(16)30069-X</td>
  </tr>
  <tr>
    <td>DOI:</td>
    <td>http://dx.doi.org/10.1016/j.comptc.2016.03.011</td>
  </tr>
  <tr>
    <td>Reference:</td>
    <td>COMPTC 2081</td>
  </tr>
  <tr>
    <td>To appear in:</td>
    <td>Computational & Theoretical Chemistry</td>
  </tr>
  <tr>
    <td>Received Date:</td>
    <td>22 February 2016</td>
  </tr>
  <tr>
    <td>Accepted Date:</td>
    <td>12 March 2016</td>
  </tr>
</table>

![](./images/814544343959339010_1.jpg)

Please cite this article as: D.Y. Shin, J.H. Jo, J-Y. Lee, D-H. Lim, Understanding Mechanisms of Carbon Dioxide
Conversion into Methane for Designing Enhanced Catalysts from First-Principles, Computational & Theoretical
Chemistry (2016), doi: http://dx.doi.org/10.1016/j.comptc.2016.03.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers
we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and
review of the resulting proof before it is published in its final form. Please note that during the production process
errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Understanding Mechanisms of Carbon Dioxide Conversion into Methane for Designing Enhanced Catalysts from First-Principles

Dong Yun Shin, $^{\mathrm{a}}$ Jun Ho Jo, $^{\mathrm{b}}$ Jai-Young Lee, $^{\mathrm{c},*}$ and Dong-Hee Lim $^{\mathrm{a},*}$

$^{\mathrm{a}}$Department of Environmental Engineering, Chungbuk National University,
Chungdae-ro 1, Seowon-gu, Cheongju, Chungbuk, 28644, Republic of Korea

$^{\mathrm{b}}$Korea Institute of Civil Engineering and Building Technology,
283 Goyangdae-ro, Ilsanseo-gu, Goyang-si, Gyeonggi-do, 30147, Republic of Korea

$^{\mathrm{c}}$Department of Environmental Engineering, University of Seoul,
163 Seoulsiripdaero, Dongdaemun-gu, Seoul, 02504, Republic of Korea

*Corresponding Authors: Dong-Hee Lim and Jai-Young Lee

Email: limkr@cbnu.ac.kr (D.-H. Lim), leejy@uos.ac.kr (J.-Y. Lee)

Phone: +82-43-261-2467, Fax: +82-43-264-2465

Supplementary Information available:

Supplementary information for this article is available.

### Abstract

Conversion of carbon dioxide ($\text{CO}_2$) into methane ($\text{CH}_4$) on copper (Cu) surfaces were investigated to understand the fundamental mechanism of $\text{CO}_2$ reduction, and to suggest a key factor for designing promising catalysts for $\text{CO}_2$ conversion into hydrocarbon fuels. The density functional theory calculations revealed the lowest-energy reaction pathways on Cu(100), Cu(110), and Cu(111) planes, and determined that the potential limiting step for $\text{CO}_2$ reduction lies between the reaction intermediates $\text{CO}^*$ and $\text{CHO}^*$ (* denotes the state adsorbed on the catalyst surface). The energy barrier to the potential limiting step is lowered in the following order: $\text{Cu(110)} < \text{Cu(100)} < \text{Cu(111)}$. A key factor for obtaining the lowest energy barrier on Cu(110) may be the largest interatomic distance on the Cu(110) surface among the three surfaces, which enhances the interaction between the key intermediate CHO and the Cu surface, compared to that between CO and the surface. This finding may be applied to developing promising catalysts for $\text{CO}_2$ reduction by designing a Cu thin film on a supporting material with larger lattice constant than Cu. To demonstrate this, we evaluated the energy barriers to the potential limiting step on a single Cu thin layer supported on both palladium (Pd) and silver (Ag), and confirmed that the Pd supporting material can enlarge the interatomic distance of the single Cu(111) layer by 8.7 % and thereby lower the energy barrier from 0.97 to 0.63 eV.

### Graphical Abstract

![](./images/814544343959339010_2.jpg)

### 1. Introduction

Environmental problems, such as globally increasing average temperatures, melting glaciers and ice caps, rising sea levels, and accelerating desertification are major global concerns. According to the Intergovernmental Panel on Climate Change (IPCC), greenhouse gases (GHGs) are primarily responsible for the greenhouse effect. $^{[1,\ 2]}$ It was reported that the major aggravating factor contributing to long-term global warming is the $CO_2$ emission that occupies the largest portion of GHGs. $^{[2]}$ Specifically, fossil fuel use is the primary source of constantly increasing anthropogenic $CO_2$ emissions. $^{[1,2]}$ Therefore, there is an urgent need for reducing the amount of $CO_2$ released to the atmosphere.

A variety of technologies for reducing GHGs have been researched and presented at a global level. Among them, the carbon capture and storage (CCS) technique is one among many for reducing $CO_2$ emissions and for stabilizing GHG concentrations while maintaining the fossil fuel consumption. $^{[3,4]}$ Specifically, $CO_2$ fuelization is of great importance for its double benefit of solving the global warming issue by reducing GHGs and fossil fuel consumptions, and by recycling carbon resources. The most urgent task associated with CCS technology is the development of catalysts for efficient $CO_2$ conversion into useable hydrocarbon fuels, because it requires additional energy due to the high thermodynamic stability of $CO_2$. $^{[5]}$

Generation of hydrocarbon fuels through the electrochemical $CO_2$ reduction takes place directly on the electrodes in liquid phase. This reaction should be supported by an externally applied energy and should be able to compete with hydrogen evolution reaction (HER). Therefore, a catalyst is required to suppress HER and to obtain the desired products, and extensive research has been conducted using various materials to this end. $^{[6-16]}$ In particular, intensive studies have been conducted using Cu-based catalysts as electrodes; $^{[5,\ 17-19]}$ *Hori et al.*, for example, reported the electrochemical conversion of $CO_2$ into various organic compounds, such as $CO$, $CH_4$, $C_2H_4$, $C_2H_5OH$, and $HCOOH$, using Cu electrodes. $^{[20-23]}$ These studies analyzed the various products of $CO_2$ conversion using single-crystal Cu electrodes, and confirmed that the nature of the products vary according to the crystal orientation of the used Cu catalysts. $^{[22]}$ Despite much effort, a mass

production of hydrocarbon fuels from $CO_2$ conversion using Cu catalysts is still a great challenge due to relatively high overpotential for the electrochemical reduction of $CO_2$,$^{[19,24]}$ and continuous research is underway to enhance the $CO_2$ conversion efficiency.$^{[25-27]}$ In order to develop a promising catalytic material for efficient $CO_2$ conversion into hydrocarbons as a useful energy resource, it is essential to understand the fundamental mechanism of electrochemical $CO_2$ reduction in relation to various properties of catalytic surfaces. A thorough understanding of the $CO_2$ conversion mechanism will contribute to determining a key factor for enhancing the conversion efficiency and applying it for designing a new catalytic material.

With this background, a fundamental research into the properties of various catalytic materials was performed in the current study by analyzing the mechanism of $CO_2$ reduction on the surfaces [Cu(100), Cu(110), Cu(111)] of Cu catalysts using density functional theory (DFT)-based modeling. The optimal reaction pathways of converting $CO_2$ into methane ($CH_4$) were analyzed based on the free energies derived from the DFT calculations and thermodynamics modeling. Based on the analyses, we identified the key factor for enhancing $CO_2$ conversion efficiency by determining the potential limiting step and by analyzing the adsorption energies and physicochemical properties of the intermediates of the individual steps of $CO_2$ reduction. We applied the key factor thus detected for optimizing the structure of a new catalytic material for efficiently accelerating the $CO_2$ reduction and verified its efficacy with DFT calculations.

## 2. Computational Methodology

DFT calculations were performed using the Vienna *ab initio* Simulation Package (VASP)$^{[28,}$ $^{29]}$ with the projector-augmented wave (PAW)$^{[29,30]}$ method. The Perdew, Burke, and Ernzerhof (PBE)$^{[31]}$ generalized gradient approximation (GGA) exchange-correlation functional was used. A kinetic energy cutoff of 400 eV was used with a plane-wave basis set. The integration of the Brillouin zone was conducted using a $2 \times 2 \times 1$ Monkhorst-Pack grid$^{[32]}$ and the first-order Methfessel-Paxton smearing$^{[33]}$ with a width of 0.1 eV. The geometries were optimized until the forces were reduced below $10^{-2}$ eV/Å. Spin polarization was not incorporated since Cu is non-

magnetic. The spin polarization calculation did not significantly change the relative energy profiles
as demonstrated in our previous study. $^{[25]}$

The Cu(100)–p(3×3), Cu(110)–p(3×3), and Cu(111)–p(4×4) surfaces were represented as a
four-layer slab where the two bottom layers were fixed at the equilibrium lattice constant of 3.637 Å
(experimental value $3.615$ Å$^{[34]}$). The vacuum spaces for the systems are larger than 25.7 Å as shown
in Figure 1. The gas-phase molecules were optimized in a 12.0 Å cubic supercell in which the
Brillouin zone integration was carried out for the $\Gamma$-point only, and calculated by using a Fermi-level
smearing of 0.01 eV. The adsorption energy ($E_{ads}$) of an adsorbate is defined as:

$$
E_{ads} = E_{substrate+adsorbate} - E_{substrate} - E_{adsorbate} \tag{1}
$$

where $E_{substrate+adsorbate}$, $E_{substrate}$, and $E_{adsorbate}$ are the total energies of a substrate and adsorbate (e.g.,
Cu(111)–CO₂), a substrate (Cu(111)), and a gas phase adsorbate (e.g., CO₂), respectively. Negative
adsorption energy indicates that adsorption is exothermic (stable) with respect to the free gas-phase
adsorbate. The work function ($\Phi$) (i.e., the minimum energy required to remove an electron from the
bulk of a material through a surface to a point outside the material) is defined as:

$$
\Phi = V_{vacuum} - E_{F} \tag{2}
$$

where $V_{vacuum}$ and $E_{F}$ are the potential in the vacuum (at a point outside the material) and the
Fermi energy of the material, respectively.

The free energies of the electrochemical CO₂ reduction intermediates were calculated based
on the computational hydrogen electrode (CHE) model suggested by Nørskov *et al.*$^{[24,35]}$ in which a
proton/electron ($\text{H}^{+} + \text{e}^{-}$) in solution can be indirectly treated and a bias can be applied by shifting
$\Delta G$ by $+neU$, where $n$ is the number of proton–electron pairs transferred, $e$ is the elementary positive
charge, and $U$ is the applied potential. The free energy change ($\Delta G$) is defined as:


$$\Delta G=\Delta E+\Delta ZPE - T\Delta S \tag{3}$$

where $\Delta E$ is the total energy change directly obtained from DFT calculations, $\Delta ZPE$ is the change in zero-point energies, $T$ is temperature, and $\Delta S$ is the change in entropy. The enthalpic temperature correction $(\int C_pdT)$ is neglected for adsorbate-surface systems due to its relatively negligible contribution (approximately $0.005$~$0.10$ eV$^{[24]}$) but it is included for gas-phase molecules. Temperature is set to $18.5\ \mathrm{^\circ C}$ to compare current DFT results with the experimental data of Hori et $al.^{[36]}$ The details of free energy calculation data including chemical potentials of gas-phase molecules and the solvation energy corrections are described in Section 1 of the Supplementary Information (SI).

![](./images/814544343959339010_3.jpg)

Figure 1. (A) Top views of Cu(100)-(3×3), Cu(110)-(6×3), Cu(111)-(4×4) surface models consisting of four layers. (B) Side view of the Cu(111)-(4×4) model. Brown and light brown colors represent the top Cu surface and the subsurface, respectively.

## 3. Results and Discussion

### 3.1. Physical properties of bulk copper

As a preliminary study, we performed the optimization of bulk Cu structure. The optimized

lattice constant and bulk modulus derived from DFT calculations were 3.637 Å and 136.5 GPa, respectively. These are in good agreement with reported values determined by DFT calculations (lattice constant: $3.63\ \text{Å}^{[27]}$ bulk modulus: $138\ \text{GPa}^{[37]}$) and by experiments (lattice constant: 3.615 $\text{Å}^{[34]}$, bulk modulus: $142\ \text{GPa}^{[38]}$).

With the optimized lattice constant as the standard, we constructed Cu(100), Cu(110), and Cu(111) surfaces and calculated their surface energies ($\sigma$) to be 1.46, 1.56, and $1.33\ \text{J/m}^2$, respectively, using the four-layer slab model. These values were verified to have the same order of $\text{Cu(110)} > \text{Cu(100)} > \text{Cu(111)}$ as that demonstrated in previous studies. $^{[39,40]}$ With a surface energy of $1.33\ \text{J/m}^2$, Cu(111) is the closest-packed surface and has the highest thermodynamic stability among the three surfaces. $^{[41]}$ Details of the calculation process are described in SI Section 1.

### 3.2. Free energy diagrams of $\text{CO}_2$ reduction

Peterson et al. $^{[24]}$ proposed the lowest-energy reaction pathway for the conversion of $\text{CO}_2$ to $\text{CH}_4$ on a Cu(211) surface by conducting DFT calculations. As protons ($\text{H}^+$) and electrons ($\text{e}^-$) are added to $\text{CO}_2$, the following intermediates are produced along the suggested $\text{CO}_2$ reduction reaction pathway: $\text{CO}_2 \rightarrow \text{COOH}^* \rightarrow \text{CO}^* \rightarrow \text{CHO}^* \rightarrow \text{CH}_2\text{O}^* \rightarrow \text{CH}_3\text{O}^* \rightarrow \text{O}^* \rightarrow \text{OH}^*$, where * denotes the state adsorbed on the catalyst surface. Note that Nie et al. $^{[42,43]}$ examined alternative $\text{CO}_2$ conversion pathways by taking into account water solvation and calculating activation barriers, and found that $\text{CH}_4$ was produced from the reduction of $\text{CO}^* \rightarrow \text{COH}^*$ (where O–H bond is formed in $\text{COH}) \rightarrow \text{C}^*$ and then sequential hydrogenation. Since the current study focused on understanding key factors of catalyst surface geometry by examining three different copper facets without water solvation, the Peterson et al.'s pathway$^{[24]}$ was adapted for the $\text{CO}_2$ conversion to $\text{CH}_4$.

Drawing on this reaction pathway, we constructed three different adsorption models for each intermediate produced on the Cu(100), Cu(110), and Cu(111) surfaces and calculated their respective free energies. Figure 2(A) shows the reaction pathway on the Cu(110) surface that was revealed the most stable pathway from the computational results. The diagrams in Figure 2(B) depict the energy barriers (i.e., the required energy to overcome the potential limitation of a pathway) calculated from

the free energies of the individual steps relative to the computationally obtained free energy of the step 1 (i.e., the gas-phase $CO_2$ and each surface).

The zero potential reactions (denoted by filled rectangles) in Figure 2(B), which represents the reaction when no external potential is applied, reveals that each surface forms the highest energy barrier in the step $3 \rightarrow 4$ ($CO^* \rightarrow CHO^*$), with Cu(100) = 0.92 eV, Cu(110) = 0.62 eV, and Cu(111) = 0.97 eV. Additionally the external potential to be applied to enable the $CO_2$ reduction reaction on each surface, which is defined as the "applied energy" required for eliminating the energy barrier, can be predicted. The predicted applied energies are Cu(100) = $-0.92$ V, Cu(110) = $-0.62$ V, and Cu(111) = $-0.97$ V (*vs.* RHE), where the negative sign denotes a reduction reaction. This implies that the rates of reaction pathways with external potentials applied, represented by the empty rectangles, are in the order of Cu(110) > Cu(100) > Cu(111). This observation agrees well with another DFT study of electrochemical $CO_2$ reduction in that the key intermediates of $CO^*$ and $CHO^*$ are stabilized by the copper surfaces in the order (100) > (111).$^{[44]}$

The consistency of the potentials required to convert $CO_2$ into $CH_4$ on the Cu(100) and Cu(111) surfaces could be verified to a large extent with the experimental results with Cu electrodes, according to which $CH_4$ began to be produced at $18.5\ ^\circ C$ between approximately $-0.8$ and $-1.0$ V (*vs.* RHE)$^{[5,24]}$. Additionally, the potential limiting step of the $CO_2$ reduction reaction ($3 \rightarrow 4$: $CO^*$ $\rightarrow CHO^*$) determined in this study is consistent with the computationally confirmed potential limiting step on the Cu(211) surface.$^{[24]}$ The only difference was that the energy barrier of the Cu(211) surface, $0.74\ eV,^{[24]}$ was lower than those of the Cu(100) and Cu(111) surfaces. It is presumably because flat-surface models are used in the current study in contrast to the step-surface model for the Cu(211) surface; the superior surface activation of the latter lends itself well to the formation of intermediates. In this regard, it is noteworthy that the energy barrier of the Cu(110) surface is lower than that of the Cu(211) surface. Peterson *et al.*$^{[24]}$ postulated that if $CHO^*$ is adsorbed on a Cu surface better than $CO^*$ during $CO_2$ reduction, the energy barrier for $CH_4$ production and the overpotential of $CO_2$ become lower, thereby improving catalytic performance. In the case of the Cu(110) surface, the mean Cu-Cu distance on the surface is $3.55\ \text{\AA}$, which is larger

than that of Cu(100) (2.93 Å) and Cu(111) (2.57 Å) by 0.62 and 0.98 Å, respectively. This is attributed to the conditions that allow a better interaction between the CHO species and Cu atoms during the adsorption of the former on the Cu(110) surface. These results are consistent with the results presented in the study of graphene-supported Cu nanoparticles conducted by Lim et al., $^{[25]}$ according to which $CO_2$ reduction performed in a structure favorable for Cu-Cu distance change can yield reduction products more efficiently. Details of the calculation steps for the free energy diagrams are described in SI Section 2.

![](./images/814544343959339010_4.jpg)

Figure 2. (A) The lowest energy pathway of $CO_2$ reduction on $Cu(100), Cu(110)$, and $Cu(111)^{a)}$ with gas products at Step 3 ($H_2O$), Step 7 ($CH_4$), and Step 9 ($H_2O$). (B) Relative free energy diagrams without (black) and with (white) applied potential for $CO_2$ reduction on the copper surfaces. The black pathway represents the free energy at 0 V (vs. RHE). Gray, red, small white and brown spheres represent C, O, H, and Cu, respectively. $^{a)}$Data obtained from Lim et al.$^{[25]}$.

### 3.3. Adsorption energy of $CO_2$ reduction intermediates and work function of copper surfaces

To understand why the Cu(110) surface exhibits the lowest energy barrier in the potential limiting step of the electrochemical reduction of $CO_2$ to $CH_4$, we calculated the adsorption energies of the intermediates and the work function (i.e., the minimum energy required for removing an

electron from a surface of a material, more specifically, from the Fermi level). Adsorption energies were calculated on the Cu(100), Cu(110), and Cu(111) surfaces of the three different adsorption models for each intermediate species for the assessment of the adsorption behaviors of the major intermediates (COOH, CO, and CHO) involved in the potential limiting step of the $CO_2$ reduction. The lowest energy (more exothermic) exhibited by the three adsorption models was used as the representative value of the respective surfaces. The adsorption energies thus determined and the work function values are presented in Table 1. The calculated work function values of Cu(100), Cu(110), and Cu(111) are 4.66, 4.46, and 4.68 eV, respectively, and support the well-known fact that work function varies according to the facets of a solid surface and in particular, the fact that work function values increase in proportion to the increase in the surface layer atomic density, i.e., layer packing (e.g., (110) < (100) < (111) of Face-centered cubic (FCC) metals such as Pd, Pt, Au, and Cu).$^{[45]}$ SI Section 3 summaries the adsorption energies of $CO_2$ reduction intermediates on Cu surfaces.

Table 1. Surface energies ($\sigma$) and work function ($\Phi$) of Cu(100), Cu(110), and Cu(111) and the adsorption energies ($E_{ads}$) of COOH, CO, and CHO on each Cu surface. $E_{ads}$ is calculated by using the total energy directly obtained from DFT calculations without correction of ZPE, entropy, and temperature.

<table>
<thead>
<tr>
<th rowspan="2"></th>
<th rowspan="2">$\sigma$ ($\text{J/m}^2$)</th>
<th rowspan="2">$\Phi$ (eV)</th>
<th colspan="3">$E_{ads}$ (eV)</th>
</tr>
<tr>
<th>COOH</th>
<th>CO</th>
<th>CHO</th>
</tr>
</thead>
<tbody>
<tr>
<td>Cu(110)</td>
<td>1.56</td>
<td>4.46</td>
<td>–2.53</td>
<td>–0.88</td>
<td>–1.92</td>
</tr>
<tr>
<td>Cu(100)</td>
<td>1.46</td>
<td>4.66</td>
<td>–2.49</td>
<td>–1.24</td>
<td>–2.18</td>
</tr>
<tr>
<td>Cu(111)</td>
<td>1.33</td>
<td>4.68</td>
<td>–2.35</td>
<td>–1.12</td>
<td>–1.93</td>
</tr>
</tbody>
</table>

The work function of a solid surface is an important physical parameter for the charge transfer from the solid surface to vacuum.$^{[46]}$ The lower the work function is, the higher is the

electron mobility. In other words, high electron mobility from a solid surface may imply a strong interaction between adsorbate and surface. The data presented in Table 1 demonstrate that work function values increase in the order Cu(110) < Cu(100) < Cu(111), which is consistent with the results of previous studies. $^{[47,48]}$ While the value of the Cu-surface-dependent work function is inversely proportional to the adsorption energy of the COOH species, the adsorption energies of the intermediate species CO and CHO do not follow such trends. This implies that adsorption behavior can vary according to the structure difference in the atomic arrays of the adsorbate and the surface.

The calculation results reveal that while the Cu(110) surface does not adsorb each intermediate species (CO and CHO) strongly in the potential limiting step, it contributed to lowering the energy barrier of the potential limiting step by adsorbing CHO more strongly than CO compared to the two other Cu surfaces. This is consistent with the result of a study by Peterson et al. $^{[24]}$ that in CO₂ reduction the property of a catalytic surface to adsorb CHO species more strongly than CO species can improve CH₄ production. The reason for the relatively weak adsorption of CO on Cu(110) compared to on other surfaces may be attributed to the less number of neighboring bonds that CO can form on the Cu(111) surface. To verify this, the adsorption energies of single atomic oxygen on the same adsorption sites where CO is adsorbed were calculated and it confirms that the adsorption strength increases (Cu(110) < Cu(111) < Cu(100)) as the number of neighboring bonding that the adsorbate can form on the surfaces increases. Details of these data are summarized in SI section 3.

Given that the correlation between adsorption strength and work function as determined in this study does not agree well with the generally known tendency, i.e., they are inversely proportional, their correlation is insufficient for explaining the reason for the lower energy barrier of the potential limiting step exhibited by the Cu(110) surface than the other Cu surfaces. Therefore, in addition to the electronic property of the Cu surfaces, surface atomic arrangement, i.e., surface geometry, can be considered an important factor in the potential limiting step of the CO₂ reduction reaction.

### 3.4. Strain effect

In order to determine whether the surface geometry is responsible for the low energy barrier of the $CO_2$ reduction potential limiting step exhibited by the Cu(110) surface, we measured the changes in the energy barrier of the potential limiting step by applying compressive and tensile strain on the Cu surfaces. The Cu(110) surface that has the lowest energy barrier and the Cu(111) surface that has the highest energy barrier of the $CO_2$ reduction potential limiting step were compared.

Figure 1(A) shows the surface Cu–Cu distances on the top layers of the Cu(110) and Cu(111) surfaces, wherein the Cu(110) surface has the largest surface Cu–Cu distance (3.64 Å) and the Cu(111) surface has the smallest surface Cu–Cu distance (2.58 Å). Based on this result, we applied compressive strain on the Cu(110) surface and tensile strain on the Cu(111) surface, thereby calculating the changes of the energy barrier.

Figure 3(A) shows that on the Cu(110) surface, the energy barrier gradually increases from 0.62 eV to 0.71 eV and 0.83 eV as the Cu–Cu distance becomes compressed by 3 % and 6 %, respectively, from the baseline interatomic distance (0 % compressive strain). When the interatomic distance was compressed by a 9 % strain, the energy barrier considerably decreased, but it was excluded from comparison because the surface atomic arrangement was deformed and dissipated under the excessive strain. In contrast, Figure 3(B) shows that the energy barrier on the Cu(111) surface gradually decreased from the initial 0.97 eV to 0.83, 0.80, and 0.72 eV as the interatomic distance becomes extended by 3 %, 6 %, and 9 %, respectively (SI Section 4 describes the calculations in detail with additional illustrations). These results demonstrate that the energy barrier of the $CO_2$ reduction potential limiting step decreases as the Cu–Cu bond distance is extended to an optimal point under the maximum possible strain for maintaining the surface configuration. This may be explained by the different adsorption behaviors of CO and CHO species that limit the $CO_2$ reduction, in which the CHO moieties, larger than CO species, are adsorbed more strongly on the Cu surface as the Cu–Cu distance increases, thus lowering the energy barrier. This computationally confirmed phenomenon that the adsorption strength of the CHO species increases proportionally with the increase in the interatomic distance on a Cu surface is consistent with the results of a study

conducted by Sakong and Groß. $^{[49]}$ This is attributable to the tendency of the $d$-band centers of surface atoms moving towards the Fermi level with the increase in the Cu–Cu distance under the applied tensile strain, which in turn induces the antibonding orbitals on the catalytic surface to move towards high-energy side, thereby hampering electron filling into the antibonding orbitals and thus resulting in the strengthening of adsorption. $^{[50,51]}$

Furthermore, according to the results of the experiments on the Cu-catalyzed CO₂ conversion into hydrocarbon fuels conducted by Hori et al. $^{[23]}$ and Takahashi et al., $^{[22]}$ CO₂ reduction is selective to its products, depending on single-surface structures. For example, the major products on Cu(100), Cu(110), and Cu(111) surfaces are C₂H₄, CH₃COOH, and CH₄, respectively. The geometry of a catalytic surface is hence a determinant for electrochemical reactions. The results of the current study can be used for exploring the methods for improving the Cu-catalyzed CO₂ fuelization efficiency. Specifically, if an adequate method can be found to expand the Cu–Cu distance to an optimal extent artificially, by applying tensile strain, the energy barrier of the CO₂ reduction potential limiting step can be lowered, resulting in the increase in CH₄ production efficiency.

![](./images/814544343959339010_5.jpg)

Figure 3. Relative free energies of adsorbed CO and CHO on Cu(110) (A) and Cu(111) (B) and energy barriers of the $CO_2$ reduction potential limiting step (CO* $\rightarrow$ CHO*) depending on strain percentage. The energy barriers are marked as arrows with numbers and were determined by the relative free energy difference between adsorbed CO (white rectangles) and CHO (black rectangles).

### 3.5. Alternative materials

The reduced energy barrier of the $CO_2$ reduction potential limiting step as presented in Figure 3 were obtained by artificially transforming the geometry of the Cu catalytic surface. The $CH_4$ production efficiency of $CO_2$ reduction can be increased by designing a novel catalyst capable of implementing the same strain effect. Such a design can be implemented by developing a catalyst-supporting material using a material that has a FCC structure like Cu and a lattice constant greater than that of Cu, thus allowing the formation of a Cu thin film on its surface. The lattice constant of the supporting material will induce the lattice expansion by increasing the Cu–Cu distance through

lattice mismatch. The structure of such a Cu thin film is depicted in detail in SI Section 5.

As materials to supporting the Cu thin film, we, for example, selected silver (Ag) and palladium (Pd) that have lattice constants larger than that of Cu (although these materials may not be as economically attractive as traditional Cu catalysts in industrial applications, we selected them to confirm the tensile strain effect). The optimization of bulk Ag and Pd structures were carried out under the same conditions of bulk Cu structure optimization; the lattice constants for Ag and Pd were determined to be 4.165 and 3.953 Å, respectively. When catalyst-supporting materials were made with Ag and Pd, and Cu thin films were formed on their surfaces as described previously, the Cu–Cu distances were found to have increased by approximately 14.5 % and 8.7 %, respectively, relative to the FCC crystalline structure of Cu.

Using the models thus constructed, the energy barriers of the CO₂ reduction potential limiting step (CO* → CHO*), were calculated to be 0.44 eV for Cu/Ag(111) and 0.63 eV for Cu/Pd(111). The calculation results verified that the energy barriers exhibited on the Cu/Ag(111) and Cu/Pd(111) surfaces were lower than that of the pure Cu(111) surface (0.97 eV). Both Cu/Ag(111) and Cu/Pd(111) surfaces showed a similar inverse relationship between Cu–Cu distance and energy barrier. In particular, the Cu/Pd(111) surface demonstrated the energy barrier of 0.63 eV similar to that obtained through an artificial 9 % expansion of the Cu(111) surface (0.72 eV in Figure 3(B)). This result proves that the Cu–Cu distance on the Cu surface, i.e., the geometric structure of the Cu surface, on which reactions take place plays a pivotal role in CO₂.

Although the Cu/Ag(111) surface yielded a lower energy barrier, the surface were found to be dissipated to the extent that a Cu thin film cannot be formed when the intermediate species adsorbed. It was posited that the lattice constant of Ag, which is disproportionately larger than that of Cu, induces a non-ideal expansion of interatomic distance and results in failure to form a Cu thin film. We calculated the surface formation energies ($E_{form}$) of the Cu/Ag(111) and Cu/Pd(111) surfaces to prove this assumption, which yielded 9.12 and −0.43 eV, respectively. A negative value of $E_{form}$ is a proof that the surface can be formed on Pd support, and a positive value implies that a surface layer cannot be formed on the Ag supporting material (refer to SI Section 5). This verifies

that it is practically impossible to form a Cu/Ag(111) surface and a Cu/Pd(111) surface can be formed.

![](./images/814544343959339010_6.jpg)

Figure 4. Top views of a single copper layer supported on Ag (A) and Pd (B) supporting materials consisting of four layers. Brown, gray, and blue colors represent Cu, Ag, and Pd, respectively.

Additionally, the current results are drawn based on the absence of water effect. The presence of water may have substantial effect on a favorable pathway in the $CO_2$ reduction to $CH_4$, which may conclude different key intermediates other than CO* and CHO*. For example, Nie et $al.^{[42,43]}$ investigating the electrochemical $CO_2$ reduction to $CH_4$ on Cu(111) with the presence of water suggested that CO* is more favorably reduced to COH* due to proton shuttling through water molecules and the key step with the highest activation barrier is from COH* to C*. Future work is needed to explore the interaction between the surface geometry of catalysts and various key intermediates in the $CO_2$ reduction pathways.

## 4. Conclusions

In summary, we analyzed the mechanism of $CO_2$ reduction on the Cu(100), Cu(110), and Cu(111) surfaces selected from among many Cu surfaces. Based on the analysis, we proposed a catalyst design capable of accelerating the $CH_4$ production from the $CO_2$ reduction. To improve the $CH_4$ production efficiency, it is important to maintain an optimal interatomic distance on a Cu surface to induce a relatively stronger Cu interaction with CHO* species than CO* species in the


$CO_2$ reduction potential limiting step. This may be implemented by forming a Cu thin film on a catalyst-supporting material using an element with a lattice constant larger than that of Cu, thus expanding the interatomic distance of the Cu thin film layer, resulting in the acceleration of $CH_4$ production. However, if an element material with a lattice constant disproportionately larger than that of Cu is used as a catalyst-supporting material, a Cu thin film layer cannot be formed due to the dissipation of the atomic arrangement. This problem will have to be addressed in a follow-up study focusing on the optimal lattice mismatch percentage between Cu thin film layer and its supporting material.

## Acknowledgements
The current work is supported by Basic Science Research Program through the National Research Foundation (NRF) of Korea funded by the Ministry of Education, Science and Technology (NRF-2012R1A6A3A04040490) and by the research grant of Chungbuk National University in 2014.

## References
[1] Bernstein, L.; Bosch, P.; Canziani, O.; Chen, Z.; Christ, R.; Davidson, O.; Hare, W.; Huq, S.; Karoly, D.; Kattsov, V., Climate change 2007: synthesis report. *Intergovernmental Panel on Climate Change* **2007**, *20*, 2011.

[2] Stocker, T. F.; Qin, D.; Plattner, G.-K.; Tignor, M.; Allen, S. K.; Boschung, J.; Nauels, A.; Xia, Y.; Bex, V.; Midgley, P. M., Climate change 2013: The physical science basis. *Intergovernmental Panel on Climate Change, Working Group I Contribution to the IPCC Fifth Assessment Report (AR5)* (Cambridge Univ Press, New York) **2013**.

[3] Figueroa, J. D.; Fout, T.; Plasynski, S.; McIlvried, H.; Srivastava, R. D., Advances in $CO_2$ capture technology—The US Department of Energy's carbon sequestration program. *International Journal of Greenhouse Gas Control* **2008**, *2*, (1), 9-20.

[4] Pevida, C.; Plaza, M.; Arias, B.; Fermoso, J.; Rubiera, F.; Pis, J., Surface modification of activated carbons for $CO_2$ capture. *Applied Surface Science* **2008**, *254*, (22), 7165-7172.

[5] Hori, Y.; Murata, A.; Takahashi, R., Formation of hydrocarbons in the electrochemical reduction of carbon dioxide at a copper electrode in aqueous solution. *Journal of the Chemical Society, Faraday Transactions 1: Physical Chemistry in Condensed Phases* **1989**, *85*, (8), 2309-2326.

[6] Azuma, M.; Hashimoto, K.; Hiramoto, M.; Watanabe, M.; Sakata, T., Electrochemical reduction of carbon dioxide on various metal electrodes in low-temperature Aqueous $KHCO_3$ Media. *Journal of the Electrochemical Society* **1990**, *137*, (6), 1772-1778.

[7] DeWulf, D. W.; Jin, T.; Bard, A. J., Electrochemical and surface studies of carbon dioxide reduction to methane and ethylene at copper electrodes in aqueous solutions. *Journal of The Electrochemical Society* **1989**, *136*, (6), 1686-1691.

[8] De Jesús-Cardona, H.; del Moral, C.; Cabrera, C. R., Voltammetric study of $CO_2$ reduction at $Cu$ electrodes under different $KHCO_3$ concentrations, temperatures and $CO_2$ pressures. *Journal of Electroanalytical Chemistry* **2001**, *513*, (1), 45-51.

[9] Takahashi, H.; Liu, L. H.; Yashiro, Y.; Ioku, K.; Bignall, G.; Yamasaki, N.; Kori, T., $CO_2$ reduction using hydrothermal method for the selective formation of organic compounds. *Journal of Materials Science* **2006**, *41*, (5), 1585-1589.

[10] Stevens, G. B.; Reda, T.; Raguse, B., Energy storage by the electrochemical reduction of $CO_2$ to $CO$ at a porous $Au$ film. *Journal of Electroanalytical Chemistry* **2002**, *526*, (1-2), 125-133.

[11] Ohmori, T.; Nakayama, A.; Mametsuka, H.; Suzuki, E., Influence of sputtering parameters on electrochemical $CO_2$ reduction in sputtered $Au$ electrode. *Journal of Electroanalytical Chemistry* **2001**, *514*, (1-2), 51-55.

[12] Guan, G.; Kida, T.; Ma, T.; Kimura, K.; Abe, E.; Yoshida, A., Reduction of aqueous $CO_2$ at ambient temperature using zero-valent iron-based composites. *Green Chemistry* **2003**, *5*, (5), 630-634.

[13] Kerbach, I.; Climent, V.; Feliu, J. M., Reduction of $CO_2$ on bismuth modified $Pt(1\ 1\ 0)$ single-crystal surfaces. Effect of bismuth and poisoning intermediates on the rate of hydrogen evolution. *Electrochimica Acta* **2011**, *56*, (12), 4451-4456.

[14] Pearce, D. J.; Pletcher, D., A study of the mechanism for the electrocatalysis of carbon dioxide reduction by nickel and cobalt square planar complexes in solution. *Journal of Electroanalytical Chemistry and Interfacial Electrochemistry* **1986**, *197*, (1-2), 317-330.

[15] Sun, S.-G.; Zhou, Z.-Y., Surface processes and kinetics of $CO_2$ reduction on $Pt(100)$ electrodes of different surface structure in sulfuric acid solutions. *Physical Chemistry Chemical Physics* **2001**, *3*, (16), 3277-3283.

[16] Lee, Eun Y.; Hong, D.; Park, Han W.; Suh, Myunghyun P., Synthesis, properties, and reactions of trinuclear macrocyclic nickel(II) and nickel(I) complexes: Electrocatalytic reduction of $CO_2$ by nickel(II) complex. *European Journal of Inorganic Chemistry* **2003**, *2003*, (17), 3242-3249.

[17] Jitaru, M., Electrochemical carbon dioxide reduction-fundamental and applied topics. *Journal of the University of chemical Technology and Metallurgy* **2007**, *42*, (4), 333-344.

[18] Gattrell, M.; Gupta, N.; Co, A., A review of the aqueous electrochemical reduction of $CO_2$ to hydrocarbons at copper. *Journal of Electroanalytical Chemistry* **2006**, *594*, (1), 1-19.

[19] Hori, Y.; Wakebe, H.; Tsukamoto, T.; Koga, O., Electrocatalytic process of $CO$ selectivity in electrochemical reduction of $CO_2$ at metal electrodes in aqueous media. *Electrochimica Acta* **1994**, *39*, (11), 1833-1839.

[20] Hori, Y.; Takahashi, I.; Koga, O.; Hoshi, N., Electrochemical reduction of carbon dioxide at various series of copper single crystal electrodes. *Journal of Molecular Catalysis A: Chemical* **2003**, *199*, (1), 39-47.

[21] Hori, Y.; Kikuchi, K.; Murata, A.; Suzuki, S., Production of methane and ethylene in electrochemical reduction of carbon dioxide at copper electrode in aqueous hydrogencarbonate

solution. *Chemistry Letters* **1986**, (6), 897-898.

[22] Takahashi, I.; Koga, O.; Hoshi, N.; Hori, Y., Electrochemical reduction of CO₂ at copper single crystal Cu (S)-[n(111)×(111)] and Cu (S)-[n(110)×(100)] electrodes. *Journal of Electroanalytical Chemistry* **2002**, *533*, (1), 135-143.

[23] Hori, Y.; Wakebe, H.; Tsukamoto, T.; Koga, O., Adsorption of CO accompanied with simultaneous charge transfer on copper single crystal electrodes related with electrochemical reduction of CO₂ to hydrocarbons. *Surface science* **1995**, *335*, 258-263.

[24] Peterson, A. A.; Abild-Pedersen, F.; Studt, F.; Rossmeisl, J.; Nørskov, J. K., How copper catalyzes the electroreduction of carbon dioxide into hydrocarbon fuels. *Energy & Environmental Science* **2010**, *3*, (9), 1311-1315.

[25] Lim, D.-H.; Jo, J. H.; Shin, D. Y.; Wilcox, J.; Ham, H. C.; Nam, S. W., Carbon dioxide conversion into hydrocarbon fuels on defective graphene-supported Cu nanoparticles from first principles. *Nanoscale* **2014**, *6*, (10), 5087-5092.

[26] Peterson, A. A.; Nørskov, J. K., Activity descriptors for CO₂ electroreduction to methane on transition-metal catalysts. *The Journal of Physical Chemistry Letters* **2012**, *3*, (2), 251-258.

[27] Hirunsit, P., Electroreduction of carbon dioxide to methane on copper, copper–silver, and copper–gold catalysts: a DFT study. *The Journal of Physical Chemistry C* **2013**, *117*, (16), 8262-8268.

[28] Kresse, G.; Furthmüller, J., Efficient iterative schemes for \textit{ab initio} total-energy calculations using a plane-wave basis set. *Physical Review B* **1996**, *54*, (16), 11169-11186.

[29] Kresse, G.; Joubert, D., From ultrasoft pseudopotentials to the projector augmented-wave method. *Physical Review B* **1999**, *59*, (3), 1758-1775.

[30] Blöchl, P. E., Projector augmented-wave method. *Physical Review B* **1994**, *50*, (24), 17953-17979.

[31] Perdew, J. P.; Burke, K.; Ernzerhof, M., Generalized gradient approximation made simple. *Physical Review Letters* **1996**, *77*, (18), 3865-3868.

[32] Monkhorst, H. J.; Pack, J. D., Special points for Brillouin-zone integrations. *Physical Review B* **1976**, *13*, (12), 5188-5192.

[33] Methfessel, M.; Paxton, A. T., High-precision sampling for Brillouin-zone integration in metals. *Physical Review B* **1989**, *40*, (6), 3616-3621.

[34] Straumanis, M.; Yu, L., Lattice parameters, densities, expansion coefficients and perfection of structure of Cu and of Cu-In phase. *Acta Crystallographica Section A: Crystal Physics, Diffraction, Theoretical and General Crystallography* **1969**, *25*, (6), 676-682.

[35] Nørskov, J. K.; Rossmeisl, J.; Logadottir, A.; Lindqvist, L.; Kitchin, J. R.; Bligaard, T.; Jónsson, H., Origin of the overpotential for oxygen reduction at a fuel-cell cathode. *Journal of Physical Chemistry B* **2004**, *108*, (46), 17886-17892.

[36] Hori, Y.; Murata, A.; Takahashi, R., Formation of Hydrocarbons in the Electrochemical Reduction of Carbon-Dioxide at a Copper Electrode in Aqueous-Solution. *Journal of the Chemical Society-Faraday Transactions I* **1989**, *85*, 2309-2326.

[37] Mishin, Y.; Mehl, M. J.; Papaconstantopoulos, D. A.; Voter, A. F.; Kress, J. D., Structural stability and lattice defects in copper: $\textit{Ab initio}$ , tight-binding, and embedded-atom calculations. *Physical Review B* **2001**, *63*, (22), 224106.

[38] Janak, J. F.; Moruzzi, V. L.; Williams, A. R., Ground-state thermomechanical properties of some cubic elements in the local-density formalism. *Physical Review B* **1975**, *12*, (4), 1257-1261.

[39] Heino, P., Microstructure and shear strength of a Cu-Ta interface. *Computational materials science* **2001**, *20*, (2), 157-167.

[40] Vitos, L.; Ruban, A.; Skriver, H. L.; Kollar, J., The surface energy of metals. *Surface Science* **1998**, *411*, (1), 186-202.

[41] Häkkinen, H.; Manninen, M., Computer simulation of disordering and premelting of low-index faces of copper. *Physical Review B* **1992**, *46*, (3), 1725-1742.

[42] Nie, X.; Esopi, M. R.; Janik, M. J.; Asthagiri, A., Selectivity of CO₂ reduction on copper electrodes: the role of the kinetics of elementary steps. *Angewandte Chemie International Edition* **2013**, *52*, (9), 2459-2462.

[43] Nie, X.; Luo, W.; Janik, M. J.; Asthagiri, A., Reaction mechanisms of CO₂ electrochemical reduction on Cu(1 1 1) determined with density functional theory. *Journal of Catalysis* **2014**, *312*, 108-122.

[44] Durand, W. J.; Peterson, A. A.; Studt, F.; Abild-Pedersen, F.; Nørskov, J. K., Structure effects on the energetics of the electrochemical reduction of CO₂ by copper surfaces. *Surface Science* **2011**, *605*, (15-16), 1354-1359.

[45] Singh-Miller, N. E.; Marzari, N., Surface energies, work functions, and surface relaxations of low-index metallic surfaces from first principles. *Physical Review B* **2009**, *80*, (23), 235407.

[46] Butler, K. T.; Buckeridge, J.; Catlow, C. R. A.; Walsh, A., Crystal electron binding energy and surface work function control of tin dioxide. *Physical Review B* **2014**, *89*, (11), 115320.

[47] Gartland, P.; Berge, S.; Slagsvold, B., Photoelectric work function of a copper single crystal for the (100),(110),(111), and (112) faces. *Physical Review Letters* **1972**, *28*, (12), 738.

[48] Skriver, H. L.; Rosengaard, N., Surface energy and work function of elemental metals. *Physical Review B* **1992**, *46*, (11), 7157.

[49] Sakong, S.; Groß, A., Dissociative adsorption of hydrogen on strained Cu surfaces. *Surface science* **2003**, *525*, (1), 107-118.

[50] Hammer, B.; Nørskov, J. K., Electronic factors determining the reactivity of metal surfaces. *Surface Science* **1995**, *343*, (3), 211-220.

[51] Hammer, B.; Nørskov, J. K., Theoretical surface science and catalysis—calculations and concepts. In *Advances in Catalysis*, Bruce C. Gates, H. K., Ed. Academic Press: 2000; Vol. Volume 45, pp 71-129.

### Highlights

- Potential limiting step for $CO_2$ reduction lies between CO* and CHO* intermediates

- Energy barrier to the potential limiting step is lowered: Cu(110) < Cu(100) < Cu(111)

- The lowest energy barrier is attributed to the largest surface Cu-Cu distance

  - Pd supporting material can enlarge the Cu-Cu distance, lowering the energy barrier