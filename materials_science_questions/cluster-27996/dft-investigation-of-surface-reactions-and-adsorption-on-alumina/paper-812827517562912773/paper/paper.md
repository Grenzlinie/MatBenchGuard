# Porous nanographene formation on $\gamma$-alumina nanoparticles *via* transition-metal-free methane activation†

Masanori Yamamoto, *a Qi Zhao, $^{b}$ Shunsuke Goto, $^{a}$ Yu Gu, $^{c}$ Takaaki Toriyama, $^{d}$ Tomokazu Yamamoto, $^{d}$ Hirotomo Nishihara, $^{a}$ Alex Aziz, $^{b}$ Rachel Crespo-Otero, $^{b}$ Devis Di Tommaso, $^{*b}$ Masazumi Tamura, $^{c}$ Keiichi Tomishige, $^{c}$ Takashi Kyotani $^{a}$ and Kaoru Yamazaki $^{\ddagger *e}$

$\gamma$-Al₂O₃ nanoparticles promote pyrolytic carbon deposition of CH₄ at temperatures higher than 800 °C to give single-walled nanoporous graphene (NPG) materials without the need for transition metals as reaction centers. To accelerate the development of efficient reactions for NPG synthesis, we have investigated early-stage CH₄ activation for NPG formation on $\gamma$-Al₂O₃ nanoparticles *via* reaction kinetics and surface analysis. The formation of NPG was promoted at oxygen vacancies on (100) surfaces of $\gamma$-Al₂O₃ nanoparticles following surface activation by CH₄. The kinetic analysis was well corroborated by a computational study using density functional theory. Surface defects generated as a result of surface activation by CH₄ make it kinetically feasible to obtain single-layered NPG, demonstrating the importance of precise control of oxygen vacancies for carbon growth.

## Introduction
Graphene is a two-dimensional (2D) allotrope of carbon arranged in a planar hexagonal lattice that displays high elasticity and electronic/thermal conductivity.¹ When pentagons are introduced into the hexagonal frameworks, ring closure takes place with a positive curvature to give fullerenes.² When 2D graphene is wrapped into a cylindrical structure, a 1D carbon nanotube could be obtained.³⁻⁵ In contrast, the synthesis of a three-dimensionally and periodically arranged single-walled graphene with a negative curvature has remained a challenge since Mackay and Terrones proposed an ideal 3D minimum-surface graphene structure (Scheme 1) in 1991,⁶ despite the recent advances in organic synthesis realizing small molecules with a few heptagons⁷,⁸ or octagons.⁹,¹⁰

In this regard, chemical vapor deposition (CVD) on templated materials¹¹⁻²⁴ is a prominent strategy for realizing 3D minimum-surface graphene. Especially, CVD on alumina nanoparticles (ANPs) that display high thermal stability²⁵ as the templates gave nanoporous graphene (NPG) materials from CH₄.¹⁴⁻¹⁷ The NPGs have a 3D continuous and seamless

![](./images/812827517562912773_1.jpg)

Scheme 1 (top) Schematic of the minimum-surface graphene analogue originally reported by Mackay and Terrones.⁶ (bottom) Schematic of the synthesis of single-walled nanoporous carbon (NPC) and its conversion to single-walled nanoporous graphene (NPG) by the fusion of edge sites.¹³⁻¹⁶

---
*a*Institute of Multidisciplinary Research for Advanced Materials, Tohoku University, 2-1-1 Katahira, Aoba, Sendai 980-8577, Japan. E-mail: yamamoto@mol-chem.com
*b*Department of Chemistry, Queen Mary University of London, Mile End Road, London E1 4NS, UK. E-mail: d.ditommaso@qmul.ac.uk
*c*Graduate School of Engineering, Tohoku University, 6-6-07 Aramaki, Aoba, Sendai 980-8579, Japan
*d*The Ultramicroscopy Research Center, Kyushu University, Motooka 744, Nishi, Fukuoka 819-0395, Japan
*e*Institute for Materials Research, Tohoku University, 2-1-1 Katahira, Aoba, Sendai 980-8577, Japan
† Electronic supplementary information (ESI) available: Synthetic details and characterisation of materials. See DOI: 10.1039/d1sc06578e
‡ Present address: RIKEN Center for Advanced Photonics, RIKEN, 2-1 Hirosawa, Wako, Saitama 351-0198, Japan, E-mail: kaoru.yamazaki@riken.jp

nanostructure with a large surface area, approaching the ideal value of 2D graphene $(2627\ \text{m}^2\ \text{g}^{-1}).^{26}$ NPGs also have fascinating features including high electrical conductivity, $^{16}$ elastic and flexible nature, $^{15,17}$ and unprecedentedly high electrochemical stability. $^{16,17}$

The typical synthesis of NPG is performed as follows: a uniform carbon coating *via* CVD of $\text{CH}_4$ at $900\ ^\circ\text{C}$ on ANPs is followed by the removal of ANPs by chemical washing, and the subsequent high-temperature annealing at temperatures higher than $1600\ ^\circ\text{C}$ under an inert atmosphere to give a single-walled NPG material (Scheme 1 and Fig. S1$\dagger$). $^{14-17}$ It is essential to use stable $\text{CH}_4$ with a high bond dissociation energy $(439\ \text{kJ}\ \text{mol}^{-1})^{27,28}$ as a carbon source, rather than more reactive unsaturated hydrocarbons such as acetylene and propylene, for high-quality graphene formation by suppressing carbon stacking.

Understanding the type of reaction steps involved in the $\text{CH}_4$-CVD process will represent a breakthrough in the synthesis of sophisticated nanoporous carbon materials, by using tastefully designed templates at lower temperatures *via* $\text{CH}_4$-CVD. We recently reported the radical activation of $\text{CH}_4$ on $\text{MgO},^{24}$ but the reaction mechanism on ANPs may vary owing to the differences in the geometry and electronic structure of the active site. Such a fundamental understanding of $\text{CH}_4$ chemistry on the surfaces of metal oxides could also help us to efficiently activate hydrocarbons $^{29-49}$ by controlling coke deposition at the molecular level.

In this work, we investigated the early-stage $\text{CH}_4$ activation toward the formation of NPGs on $\gamma\text{-Al}_2\text{O}_3$ nanoparticles *via* reaction kinetics using thermogravimetry-mass spectrometry (TG-MS) and density functional theory (DFT), and surface analysis with high-resolution annular dark-field scanning transmission electron microscopy (ADF-STEM), temperature-programmed desorption (TPD) of $\text{H}_2\text{O}$, and *in situ* infrared (IR) spectroscopy. We found that the formation of NPG is promoted at oxygen vacancies on (100) surfaces of $\gamma\text{-Al}_2\text{O}_3$, which are generated at temperatures higher than $800\ ^\circ\text{C}$ in the presence of $\text{CH}_4$. No transition metal reaction center was involved in $\text{CH}_4$-CVD. This process is completely different from conventional methane activation catalysis for graphene $^{50-57}$ and carbon nanotube $^{58-61}$ growth at $1000\ ^\circ\text{C}$, oxidative $^{39-41}$ and non-oxidative $^{42}$ coupling to ethylene, and partial oxidation to methanol, $^{44-49}$ which use transition metal elements as reaction centers. We first discuss the rate-limiting step of NPG formation on ANPs based on reaction kinetics using TG-MS and a reaction pathway search using DFT. We constructed a model (100) $\gamma\text{-Al}_2\text{O}_3$ surface based on high-resolution ADF-STEM, TPD of $\text{H}_2\text{O}$, and *in situ* IR spectroscopy. Next, we discuss the strategy to further enhance the formation of NPG based on the surface activation process monitored by TG-MS and *in situ* IR spectroscopy. Details of the experimental and computational methods are provided in the ESI.$\dagger$

## Results and discussion
### Kinetic analysis
Fig. 1a-d shows the dependence of the rate of $\text{CH}_4$-CVD on the partial pressure of $\text{CH}_4$ and reaction temperature using TG. The vertical axis shows the nominal number of layers of deposited carbon on ANPs calculated by the specific surface area of

![](./images/812827517562912773_2.jpg)

Fig. 1 Kinetic analysis of $\text{CH}_4$-CVD for porous nanographene. (a) Weight changes during $\text{CH}_4$-CVD for various partial pressures of $\text{CH}_4$ at $900\ ^\circ\text{C}$ as monitored by TG. $\text{CH}_4$ was introduced to the reactor at 0 min. (b) Weight changes during $\text{CH}_4$-CVD on $\gamma$-ANPs at various temperatures as monitored by TG. (c) $\text{CH}_4$ partial pressure dependence on the rate of carbon growth $v$ at $900\ ^\circ\text{C}$. (d) Arrhenius plots for the first- and second-layer deposition. $P/P_0 = 0.2$ for $\text{CH}_4$ supply; the total rate of flow was fixed at $100\ \text{mL}\ \text{min}^{-1}$. (e) TG-MS analysis of $\text{CH}_4$-CVD under a steady flow of He $(80\ \text{mL}\ \text{min}^{-1})$ and $\text{CH}_4$ $(20\ \text{mL}\ \text{min}^{-1})$ at $900\ ^\circ\text{C}$ showing gas evolution for $\text{H}_2$, $\text{H}_2\text{O}$, and CO as well as the TG curve (dashed line). (f) Enlarged view of Fig. 1e showing the transient evolution of $\text{H}_2\text{O}$ and CO.

ANPs.¹⁷ The rate of carbon growth was pseudo-first order with respect to the partial pressure of CH₄ for both first- and second-layer depositions (Fig. 1c). The formation of single-layered nanographene at a specific time of reaction was confirmed by the red-shifted strong G'-band¹⁷ of Raman spectra (Fig. S1†). This pseudo-linear dependence of the rate of carbon growth on CH₄ partial pressure suggests that the rate-limiting step of NPG growth may be the initial CH₄ activation⁵²,⁶² on the surface. The rate of carbon growth for the first layer was faster than those for the second and third layers, as shown in Fig. 1a and b. We evaluated the effective activation energies $\Delta E^{\neq}$ for the first- and second-layer carbon growth from the Arrhenius plots as shown in Fig. 1d, and obtained $\Delta E^{\neq}=124$ kJ mol⁻¹ and 308 kJ mol⁻¹, respectively. The latter value is in a good agreement with the activation energy for CH₄ decomposition onto the surface of carbon films (303 kJ mol⁻¹).⁶³ Thus, the initial carbon deposition on the γ-ANP surface was kinetically more favorable than the subsequent carbon deposition on the deposited carbon surface, and this makes it feasible to selectively form single-walled porous nanographene. The carbon deposition proceeded after an induction time of 5–10 min. Transient evolutions of CO, H₂, and H₂O were also observed in the effluent gas of CH₄-CVD reaction during the induction period as shown in Fig. 1e and f. To check the effect of H₂ on the activation of oxide surfaces, we examined H₂ treatment of ANPs at 900 °C for 30 min before CH₄-CVD. However, there was no significant difference observed in the rate of reactions by TG (Fig. S2†). These indicate that CH₄ chemically activated γ-ANPs and resulted in reactive surfaces for CH₄-CVD.

## Surface analysis
To clarify the structure of the reaction center of the NPG growth on γ-ANP (first layer), we next investigated the structure of the reaction sites on γ-ANP by ADF-STEM, TPD of H₂O, and *in situ* IR spectroscopy, and found that the oxygen vacancy sites of the partially hydrated (100) surface of γ-ANP are potential reaction centers.

The high-resolution ADF-STEM images (Fig. 2a, b and S3†) indicate that γ-ANPs had {100} as one of the main facets. The corresponding fast Fourier transformed (FFT) image was consistent with the neutron diffraction pattern for the (100) surface of γ-Al₂O₃.⁶⁴ The γ-ANPs were prepared by hydrothermal synthesis, and the amount of transition metal impurities in the γ-ANPs was negligible according to our elemental analysis (for details, see the ESI†). We did not observe dispersion of any transition metal impurities on the surfaces in the ADF-STEM images.

![](./images/812827517562912773_3.jpg)

Fig. 2 High resolution ADF-STEM image of γ-ANPs. (a) [100] and (b) [110] orientations. The insets of (a) and (b) are the corresponding FFT images.

TG analysis of CH₄-CVD suggests that reaction temperatures above 800 °C are essential for carbon growth from CH₄. We analyzed the effects of temperature on the surface structure of γ-ANPs by IR and TPD (Fig. 3a and b) up to 900 °C. The IR spectra showed desorption of H₂O and depletion of surface-bound hydroxyl groups (3800–3000 cm⁻¹)⁶⁵,⁶⁶ as the operating temperature increased under a steady flow of inert gases. Water desorption became almost negligible after 30 min at 900 °C as shown in the TPD (Fig. 3b), but a sharp absorption band in the IR spectrum centered at 3701 cm⁻¹ originating from “isolated” hydroxyl groups²⁵,⁶⁷ still remained (Fig. 3a). This indicates that terminal μ₁-hydroxyl groups existed even at such high temperature. Although the isolated hydroxyl group was labile toward proton exchange upon exposure to CD₄ at temperatures higher

![](./images/812827517562912773_4.jpg)

Fig. 3 H₂O desorption profile of γ-ANP: (a) Temperature dependence of IR spectra under a steady flow of Ar at 5 mL min⁻¹. (b) TPD profile of H₂O desorption from the surfaces of γ-ANP at 10 K min⁻¹ quantified by GC (TCD). Gas: He flow at 200 mL min⁻¹. The inset shows a schematic of water desorption from two protons and an oxide to give a surface defect. The thermal treatment under inert gas atmosphere was immediately followed by CH₄-CVD (Fig. 1) by introducing CH₄.

than 650 °C (Fig. S4 and S5†), no deposition of carbon occurred at lower temperatures. This supports that further activation of surfaces by the formation of oxygen vacancies,⁶⁸,⁶⁹ as observed by TG-MS (Fig. 1e and f) at higher temperatures in the presence of CH₄, is crucial for carbon growth to take place.

DFT calculations

To further examine the reaction mechanism, we constructed a partially dehydrated γ-Al₂O₃ (100) surface model with an oxygen vacancy. We evaluated the reaction pathway of the initial CH₄ activation on the vacancy site using the plane-wave DFT and climbing-image nudged elastic band methods under periodic boundary conditions. We used the Perdew–Burke–Ernzerhof (PBE) exchange-correlation functional⁷⁰ combined with Grimme's DFT-D3 empirical dispersion correction⁷¹ to account for the van der Waals interactions (PBE-D3). For details of the DFT calculations including the computational methods and structures of the intermediates and transition states involved in the CH₄ activation on γ-Al₂O₃ (100), see Sections S1.4 and S3 of the ESI.†

We found that the dissociative adsorption of CH₄ on the oxygen vacancy is the rate-limiting step, which is in agreement with our experiments, and that the dissociative addition undergoes in terms of the Lewis acid-base mechanism.²⁵,⁷²⁻⁷⁴

We first examined CH₄ activation on a 5-coordinated Al site (Fig. S6†).⁶⁶ Methanol formation is expected on the oxide surface from CH₄, and this is followed by desorption of the molecule to give an oxygen vacancy (4-coordinated Al site), as shown in Fig. S7.† The released methanol will decompose in the gas phase to afford CO and H₂ at the operating temperatures of 800–900 °C,⁷⁵ and this was confirmed by TG-MS analysis (Fig. 1f). With this in mind, we then investigated CH₄ activation on the 4-coordinated Al site.

Fig. 4a shows the calculated potential energy profile of CH₄ activation on the partially dehydrated γ-Al₂O₃ (100) model surface (Fig. S7†), from the physisorption of CH₄ to the formation of surface-bound methylene (CH₂*). The physisorption energy ΔEₐd is –20 kJ mol⁻¹. The subsequent dissociative addition of adsorbed CH₄* gives a surface-bound methyl group (CH₃*) and hydrogen atom (H*) with the activation energy ΔEₐ,TS1 of 140 kJ mol⁻¹. For surface reactions with small ΔEₐd, as in the present case, the effective activation energy ΔE‡ of the overall reaction evaluated as the sum of ΔEₐ,TS1 and ΔEₐd (ref. 76) is 120 kJ mol⁻¹. This theoretical value is in excellent agreement with the experimental value of 124 kJ mol⁻¹ (Fig. 1d).

![](./images/812827517562912773_5.jpg)

Fig. 5 Charge difference profiles and Bader charges of selected atoms/groups on a γ-Al₂O₃ (100) surface with a defect. Green contour: positive charges, pink contour: negative charges.

Bader charges⁷⁷ {q} of the transition state (TS) structure for the dissociative addition (TS1) in Fig. 5 clearly show that this reaction proceeds heterolytically following an acid-base mechanism, as suggested by the surface characterizations. Hᵟ⁺ (q = +0.66) interacts with the oxygen Lewis base site (q = –1.49),

![](./images/812827517562912773_6.jpg)

Fig. 4 (a) Potential energy profile for the sequential C–H bond cleavage from a CH₄ σ complex on a γ-Al₂O₃ (100) surface with a surface defect. The Al atom on the reaction site is set to be 4-coordinate. Activation energies were computed with the PBE-D3 functional and the corresponding structures of the initial, intermediate, and final states. The asterisk indicates the surface-bound species. Geometry for the oxygen defect is also shown in Fig. S7.† (b) Obtained structures of TS1 and TS2. Red: oxygen, steel blue: aluminum, black: carbon, and white: hydrogen atoms, with distances given in Ångströms.

while $\mathrm{CH}_{3}{ }^{\delta-}(q=-0.65)$ is bound to the aluminum Lewis acid site $(q=+2.35)$ at TS1. Pyramidal $\mathrm{CH}_{3}{ }^{\delta-}$ at TS1 also supports the Lewis acid-base mechanism. $^{72-74}$ The expected value for the square of the total spin angular momentum, $< S^{2}>=0.023$ at TS1, indicates significant electron pairing during the dissociative adsorption. The counter plot of the difference charge density in TS1 (Fig. 5) suggests that the large overlap between the doubly occupied 2p orbital at $\mathrm{CH}_{4}$ and the vacant 3p orbital at the bare Al atom promotes the reaction.

After dissociative adsorption, the surface $\mathrm{CH}_{3}^{*}$ is converted to $\mathrm{CH}_{2}^{*}$ with a considerably lower activation energy $(\Delta E_{\mathrm{a}}=88 \mathrm{~kJ} \mathrm{~mol}^{-1})$ via a proton transfer transition state TS2. The formed reactive $\mathrm{CH}_{2}^{*}$ species could then undergo a coupling reaction with another $\mathrm{CH}_{2}^{*}$, which would result in the formation of $\mathrm{C}_{2} \mathrm{H}_{4}^{*}$ and longer hydrocarbons on the surface, as reported in the conversion of surface-bound-methylene to a class of graphene materials on $\mathrm{Al}_{2} \mathrm{O}_{3}$ surfaces. $^{78}$ Although we cannot exclude the possibility that $\mathrm{CH}_{2}^{*}$ will desorb to the gas phase, $^{42,79}$ selective formation of single-layered NPG (Fig. S1 $\dagger$ ) indicates that this surface reaction rather than a gas-phase reaction enhances the first-layer deposition of carbon.

The activation energy for the first step of $\mathrm{CH}_{4}$ activation $(\mathrm{CH}_{4} \rightarrow \mathrm{CH}_{4}^{*} \rightarrow \mathrm{CH}_{3}^{*})$ on a non-defective hydrated $\gamma-\mathrm{Al}_{2} \mathrm{O}_{3}(100)$ surface $(\Delta E^{*})$ was $244 \mathrm{~kJ} \mathrm{~mol}^{-1}$ at an octahedrally coordinated (six-coordinated) Al site (Fig. S8 $\dagger$ ). This value is much higher than $120 \mathrm{~kJ} \mathrm{~mol}^{-1}$ at a tetrahedrally coordinated Al center on a defective surface (Fig. 4a and S7 $\dagger$ ), corroborating that the $\mathrm{CH}_{4}$ activation on non-defective hydrated $\gamma-\mathrm{Al}_{2} \mathrm{O}_{3}$ (100) surfaces is kinetically less favorable than that on oxygen vacancy surfaces.

## Thermal stability and surface activation of templates for ideal 3D minimum-surface graphenes

Thus, TG, IR, and DFT calculations demonstrate that the initial desorption of $\mathrm{H}_{2} \mathrm{O}$ from $\gamma$-ANPs without $\mathrm{CH}_{4}$ (Fig. 3) cannot trigger off the reaction, while the subsequent elimination of surface oxygens with $\mathrm{CH}_{4}$ (Fig. 1e and f) is essential for generating the active surfaces in $\mathrm{CH}_{4}$-CVD. The resultant Lewis acid-base pair at oxygen vacancies can make the formation of single-walled NPG kinetically feasible with a significantly lower activation energy as compared to a radical mechanism. $^{24}$ Interestingly, further desorption of $\mathrm{H}_{2} \mathrm{O}$ from the $\gamma$-ANP surfaces by heating from 900 to $1000{ }^{\circ} \mathrm{C}$ resulted in slower reaction rates (Table S1 $\dagger$ ). This could be explained by the structural changes of $\gamma$-ANP: The specific surface area of $\gamma$-ANPs decreased from $158 \mathrm{~m}^{2} \mathrm{~g}^{-1}$ for pristine to $139 \mathrm{~m}^{2} \mathrm{~g}^{-1}$ upon treatment at $900{ }^{\circ} \mathrm{C}$ for $2 \mathrm{~h}$, and eventually decreased to $124 \mathrm{~m}^{2} \mathrm{~g}^{-1}$ upon annealing at $1000{ }^{\circ} \mathrm{C}$ for $2 \mathrm{~h}$. The structural reorganization during $\mathrm{CH}_{4^{-}}$ CVD was also supported by ${ }^{27} \mathrm{Al}$ nuclear magnetic resonance (NMR), which showed an increase in octahedrally coordinated stable Al centers $\left({ }^{[6]} \mathrm{Al}\right)$ induced by annealing during $\mathrm{CH}_{4}$-CVD (Fig. S9 $\dagger$ ), and XRD (Fig. S10 $\dagger$ ).

Such structural reconstruction hinders the synthesis of three-dimensionally and periodically arranged single-walled graphene materials, even with the use of structurally ordered templates such as mesoporous silica $^{80}$ and zeolites. $^{11}$ Therefore, precise control of oxygen vacancies as well as high thermal stability of templates will be essential for $\mathrm{CH}_{4}$-CVD reactions on various ANPs (Fig. S11 $\dagger$ ) and other oxides. $^{20,23,72}$ Further surface engineering, including activation by gaseous reductants, may be helpful in lowering the operation temperature for more efficient $\mathrm{CH}_{4}$ activation and NPG synthesis in the future.

## Conclusions

In summary, we have investigated the early-stage $\mathrm{CH}_{4}$ activation toward porous nanocarbon formation on $\gamma-\mathrm{Al}_{2} \mathrm{O}_{3}$ nanoparticles via reaction kinetics and surface analysis. We found that oxygen vacancies were formed on the surfaces of $\gamma-\mathrm{Al}_{2} \mathrm{O}_{3}$ nanoparticles upon their reaction with $\mathrm{CH}_{4}$ at temperatures higher than $800{ }^{\circ} \mathrm{C}$. Carbon growth was promoted at the oxygen vacancies without the introduction of transition metal reaction centers. The initial dissociative adsorption of $\mathrm{CH}_{4}$ is the rate-limiting step because the overall rate of carbon growth is pseudo-first order for the $\mathrm{CH}_{4}$ partial pressure, and this is supported by DFT calculations. Surface Al at vacancy sites acts as a Lewis acid, whereas the adjacent surface oxygen acts as a Lewis base for dissociative adsorption to give surface-bound methyl and hydroxyl groups. This is followed by subsequent proton transfer to produce reactive surface-bound methylene species, leading to carbon growth. Carbon deposition from stable $\mathrm{CH}_{4}$ was faster on the surfaces of $\gamma$-ANPs with oxygen defects than on the deposited carbon films, and this makes it kinetically feasible to selectively form single-walled porous nanographene. Our work shows that precise surface engineering for introducing defects while enforcing the thermal stability of templates is crucial for accelerating $\mathrm{CH}_{4}$-CVD for better-quality NPG with fascinating features. $^{15,16}$

## Data availability

All data associated with this study are available in the main text or the ESI. $\dagger$ Further data will be available upon request to the authors.

## Author contributions

M. Y., D. D. T., T. K. and K. Y. conceived and designed the project, and summarized all the data provided by co-authors. T. K. supervised the experiment part. S. G. contributed to thermogravimetry, mass spectrometry, and gas chromatography experiments. S. G. and H. N. contributed to the characterization of nanoporous carbon materials. M. Y., Y. G., M. T., and K. T. contributed to the in situ infrared spectroscopy in the presence of various gases. T. T. and T. Y. contributed to TEM and STEM of $\gamma$-ANPs. Q. Z. and A. A. conducted the quantum chemistry calculations. R. C. O. and D. D. T. supervised the quantum chemistry calculations and provided computational resources. M. Y., Q. Z., D. D. T., and K. Y. wrote the original draft, and contributed to visualization of the presented data. All authors contributed to review and editing.

## Conflicts of interest

There are no conflicts to declare.

### Acknowledgements
This work was supported by Grants-in-Aid (19K15281 and 19H00913) from JSPS, the Ebara-Hatakeyama Memorial Foundation, and Ensemble Grant for Early Career Researchers at Tohoku University. Q. Z. thanks China Scholarship Council for financial support. We thank Tohoku University Molecule and Material Synthesis Platform in the Nanotechnology Platform Project for NMR analysis operated by Mr S. Yoshida at Tohoku University, Japan. The authors acknowledge the kind support of Prof. Dr M. Kakihana and Prof. Dr H. Kato in performing Raman spectroscopy. The authors thank Sumitomo Chemical Co. Ltd for kindly supplying alumina nanoparticles. We thank Prof. Dr A. Muramatsu (Tohoku University), Dr T. Irisawa (Nagoya University), Dr R. Osuga (Tohoku University), and Prof. Dr J. N. Kondo (Tokyo Institute of Technology) for helpful discussions. K. Y. is grateful for the financial support from Building of Consortia for the Development of Human Resources in Science and Technology funded by MEXT and Core Research for Evolutional Science and Technology of the Japan Science and Technology Agency (JST CREST, Grant No. JPMJCR16P3). This research utilized Queen Mary's Apocrita HPC facility, supported by QMUL ITS Research. We are grateful to the UK Materials and Molecular Modeling Hub for computational resources, which were partially funded by EPSRC (EP/P020194/1 and EP/T022213/1).

### References
1 K. S. Novoselov, A. K. Geim, S. V. Morozov, D. Jiang, Y. Zhang, S. V. Dubonos, I. V. Grigorieva and A. A. Firsov, *Science*, 2004, 306, 666-669.
2 H. W. Kroto, J. R. Heath, S. C. O'Brien, R. F. Curl and R. E. Smalley, *Nature*, 1985, 318, 162-163.
3 S. Iijima and T. Ichihashi, *Nature*, 1993, 363, 603-605.
4 S. Iijima, T. Ichihashi and Y. Ando, *Nature*, 1992, 356, 776-778.
5 P. M. Ajayan and S. Iijima, *Nature*, 1992, 358, 23.
6 A. L. Mackay and H. Terrones, *Nature*, 1991, 352, 762.
7 X. Yang, F. Rominger and M. Mastalerz, *Angew. Chem., Int. Ed.*, 2019, 58, 17577-17582.
8 K. Kato, K. Takaba, S. Maki-Yonekura, N. Mitoma, Y. Nakanishi, T. Nishihara, T. Hatakeyama, T. Kawada, Y. Hijikata, J. Pirillo, L. T. Scott, K. Yonekura, Y. Segawa and K. Itami, *J. Am. Chem. Soc.*, 2021, 143, 5465-5469.
9 M. A. Medel, R. Tapia, V. Blanco, D. Miguel, S. P. Morcillo and A. G. Campaña, *Angew. Chem., Int. Ed.*, 2021, 60, 6094-6100.
10 Y. Byun, L. S. Xie, P. Fritz, T. Ashirov, M. Dincă and A. Coskun, *Angew. Chem., Int. Ed.*, 2020, 59, 15166-15170.
11 Z. Ma, T. Kyotani and A. Tomita, *Chem. Commun.*, 2000, 2365-2366.
12 Z. Ma, T. Kyotani, Z. Liu, O. Terasaki and A. Tomita, *Chem. Mater.*, 2001, 13, 4413-4415.
13 T. Kyotani, T. Nagai, S. Inoue and A. Tomita, *Chem. Mater.*, 1997, 9, 609-615.
14 H. Nishihara, T. Simura, S. Kobayashi, K. Nomura, R. Berenguer, M. Ito, M. Uchimura, H. Iden, K. Arihara, A. Ohma, Y. Hayasaka and T. Kyotani, *Adv. Funct. Mater.*, 2016, 26, 6418-6427.
15 K. Nomura, H. Nishihara, M. Yamamoto, A. Gabe, M. Ito, M. Uchimura, Y. Nishina, H. Tanaka, M. T. Miyahara and T. Kyotani, *Nat. Commun.*, 2019, 10, 2559.
16 K. Nomura, H. Nishihara, N. Kobayashi, T. Asada and T. Kyotani, *Energy Environ. Sci.*, 2019, 12, 1542-1549.
17 M. Yamamoto, S. Goto, R. Tang, K. Nomura, Y. Hayasaka, Y. Yoshioka, M. Ito, M. Morooka, H. Nishihara and T. Kyotani, *ACS Appl. Mater. Interfaces*, 2021, 13, 38613-38622.
18 R. Tang, M. Yamamoto, K. Nomura, E. Morallón, D. Cazorla-Amorós, H. Nishihara and T. Kyotani, *J. Power Sources*, 2020, 457, 228042.
19 K. Kim, T. Lee, Y. Kwon, Y. Seo, J. Song, J. K. Park, H. Lee, J. Y. Park, H. Ihee, S. J. Cho and R. Ryoo, *Nature*, 2016, 535, 131-135.
20 D. S. Baek, K. A. Lee, J. Park, J. H. Kim, J. Lee, J. S. Lim, S. Y. Lee, T. J. Shin, H. Y. Jeong, J. S. Son, S. J. Kang, J. Y. Kim and S. H. Joo, *Angew. Chem., Int. Ed.*, 2021, 60, 1441-1449.
21 M. Inagaki, S. Kobayashi, F. Kojin, N. Tanaka, T. Morishita and B. Tryba, *Carbon*, 2004, 42, 3153-3158.
22 T. Morishita, T. Tsumura, M. Toyoda, J. Przepiórski, A. W. Morawski, H. Konno and M. Inagaki, *Carbon*, 2010, 48, 2690-2707.
23 M. Inagaki, M. Toyoda, Y. Soneda, S. Tsujimura and T. Morishita, *Carbon*, 2016, 107, 448-473.
24 S. Sunahiro, K. Nomura, S. Goto, K. Kanamaru, R. Tang, M. Yamamoto, T. Yoshii, J. N. Kondo, Q. Zhao, A. G. Nabi, R. Crespo-Otero, D. Di Tommaso, T. Kyotani and H. Nishihara, *J. Mater. Chem. A*, 2021, 9, 14296-14308.
25 P. Euzen, P. Raybaud, X. Krokidis, H. Toulhoat, J.-L. Le Loarer, J.-P. Jolivet and C. Froidefond, *Alumina*, Wiley-VCH Verlag GmbH, Weinheim, 2002.
26 This is obviously determined by the atomic weight of carbon and the C═C bond length (1.42 $\mathring{\text{A}}$) in the hexagons.
27 Y.-R. Luo, *Handbook of Bond Dissociation Energies in Organic Compounds*, CRC Press, London, 2003.
28 S. J. Blanksby and G. B. Ellison, *Acc. Chem. Res.*, 2003, 36, 255-263.
29 J. Weitkamp, *ChemCatChem*, 2012, 4, 292-306.
30 Z. Liang, T. Li, M. Kim, A. Asthagiri and J. F. Weaver, *Science*, 2017, 356, 299-303.
31 G. Zichittella and J. Pérez-Ramírez, *Chem. Soc. Rev.*, 2021, 50, 2984-3012.
32 Y. Wang, P. Hu, J. Yang, Y.-A. Zhu and D. Chen, *Chem. Soc. Rev.*, 2021, 50, 4299-4358.
33 F. Schüth, *Science*, 2019, 363, 1282-1283.
34 X. Zhang, C. Pei, X. Chang, S. Chen, R. Liu, Z.-J. Zhao, R. Mu and J. Gong, *J. Am. Chem. Soc.*, 2020, 142, 11540-11549.
35 P. Schwach, X. Pan and X. Bao, *Chem. Rev.*, 2017, 117, 8497-8520.
36 Z.-J. Zhao, C.-C. Chiu and J. Gong, *Chem. Sci.*, 2015, 6, 4403-4425.
37 D. Li, Y. Nakagawa and K. Tomishige, *Appl. Catal., A*, 2011, 408, 1-24.

38 J. H. Lunsford, *Catal. Today*, 2000, **63**, 165-174.

39 A. M. Arinaga, M. C. Ziegelski and T. J. Marks, *Angew. Chem., Int. Ed.*, 2021, **60**, 10502-10515.

40 A. Sato, S. Ogo, K. Kamata, Y. Takeno, T. Yabe, T. Yamamoto, S. Matsumura, M. Hara and Y. Sekine, *Chem. Commun.*, 2019, **55**, 4019-4022.

41 S. Arndt, G. Laugel, S. Levchenko, R. Horn, M. Baerns, M. Scheffler, R. Schlögl and R. Schomäcker, *Catal. Rev.*, 2011, **53**, 424-514.

42 X. Guo, G. Fang, G. Li, H. Ma, H. Fan, L. Yu, C. Ma, X. Wu, D. Deng, M. Wei, D. Tan, R. Si, S. Zhang, J. Li, L. Sun, Z. Tang, X. Pan and X. Bao, *Science*, 2014, **344**, 616-619.

43 C. S. Cooper, R. J. Oldman and C. R. A. Catlow, *Chem. Commun.*, 2015, **51**, 5856-5859.

44 A. J. Knorpp, A. B. Pinar, C. Baerlocher, L. B. McCusker, N. Casati, M. A. Newton, S. Checchia, J. Meyet, D. Palagin and J. A. van Bokhoven, *Angew. Chem., Int. Ed.*, 2021, **60**, 5854-5858.

45 J. Meyet, A. Ashuiev, G. Noh, M. A. Newton, D. Klose, K. Searles, A. P. van Bavel, A. D. Horton, G. Jeschke, J. A. van Bokhoven and C. Copéret, *Angew. Chem., Int. Ed.*, 2021, **60**, 16200-16207.

46 Z. Jin, L. Wang, E. Zuidema, K. Mondal, M. Zhang, J. Zhang, C. Wang, X. Meng, H. Yang, C. Mesters and F.-S. Xiao, *Science*, 2020, **367**, 193-197.

47 M. A. Newton, A. J. Knorpp, V. L. Sushkevich, D. Palagin and J. A. van Bokhoven, *Chem. Soc. Rev.*, 2020, **49**, 1449-1486.

48 M. H. Mahyuddin, T. Tanaka, Y. Shiota, A. Staykov and K. Yoshizawa, *ACS Catal.*, 2018, **8**, 1500-1509.

49 B. Ipek, M. J. Wulfers, H. Kim, F. Göltl, I. Hermans, J. P. Smith, K. S. Booksh, C. M. Brown and R. F. Lobo, *ACS Catal.*, 2017, **7**, 4291-4303.

50 X. Li, W. Cai, J. An, S. Kim, J. Nah, D. Yang, R. Piner, A. Velamakanni, I. Jung, E. Tutuc, S. K. Banerjee, L. Colombo and R. S. Ruoff, *Science*, 2009, **324**, 1312-1314.

51 K. S. Kim, Y. Zhao, H. Jang, S. Y. Lee, J. M. Kim, K. S. Kim, J.-H. Ahn, P. Kim, J.-Y. Choi and B. H. Hong, *Nature*, 2009, **457**, 706-710.

52 H. Chen, W. Zhu and Z. Zhang, *Phys. Rev. Lett.*, 2010, **104**, 186101.

53 W. Zhang, P. Wu, Z. Li and J. Yang, *J. Phys. Chem. C*, 2011, **115**, 17782-17787.

54 X. S. Li, C. W. Magnuson, A. Venugopal, J. H. An, J. W. Suk, B. Y. Han, M. Borysiak, W. W. Cai, A. Velamakanni, Y. W. Zhu, L. F. Fu, E. M. Vogel, E. Voelkl, L. Colombo and R. S. Ruoff, *Nano Lett.*, 2010, **10**, 4328-4334.

55 M. Losurdo, M. M. Giangregorio, P. Capezzuto and G. Bruno, *Phys. Chem. Chem. Phys.*, 2011, **13**, 20836-20843.

56 R. Munoz and C. Gomez-Aleixandre, *Chem. Vap. Deposition*, 2013, **19**, 297-322.

57 C. Arya, K. K. H. De Silva and M. Yoshimura, *J. Mater. Sci.: Mater. Electron.*, 2020, **31**, 21821-21831.

58 J. Kong, A. M. Cassell and H. Dai, *Chem. Phys. Lett.*, 1998, **292**, 567-574.

59 F. Yang, M. Wang, D. Zhang, J. Yang, M. Zheng and Y. Li, *Chem. Rev.*, 2020, **120**, 2693-2758.

60 A. M. Cassell, J. A. Raymakers, J. Kong and H. J. Dai, *J. Phys. Chem. B*, 1999, **103**, 6484-6492.

61 V. M. Sivakumar, A. R. Mohamed, A. Z. Abdullah and S. P. Chai, *J. Nanomater.*, 2010, 1-11.

62 A. A. Latimer, A. R. Kulkarni, H. Aljama, J. H. Montoya, J. S. Yoo, C. Tsai, F. Abild-Pedersen, F. Studt and J. K. Nørskov, *Nat. Mater.*, 2017, **16**, 225-229.

63 R. Venkateswaran, M. H. Back and G. Scacchi, *Carbon*, 1994, **32**, 911-919.

64 J.-P. Beaufils and Y. Barbaux, *J. Chim. Phys.*, 1981, **78**, 347-352.

65 G. Socrates, *Infrared and Raman Characteristic Group Frequencies: Tables and Charts*, John Wiley & Sons, Ltd, New York, 3rd edn, 2004.

66 K. Khivantsev, N. R. Jaegers, J.-H. Kwak, J. Szanyi and L. Kovarik, *Angew. Chem., Int. Ed.*, 2021, **60**, 17522-17530.

67 J. G. Larson and W. K. Hall, *J. Phys. Chem.*, 1965, **69**, 3080-3089.

68 Z. Xie, Z. Li, P. Tang, Y. Song, Z. Zhao, L. Kong, X. Fan and X. Xiao, *J. Catal.*, 2021, **397**, 172-182.

69 U. Rodemerck, E. V. Kondratenko, T. Otroshchenko and D. Linke, *Chem. Commun.*, 2016, **52**, 12222-12225.

70 J. P. Perdew, K. Burke and M. Ernzerhof, *Phys. Rev. Lett.*, 1996, **77**, 3865-3868.

71 S. Grimme, J. Antony, S. Ehrlich and H. Krieg, *J. Chem. Phys.*, 2010, **132**, 154104.

72 J. Li, S. Zhou, J. Zhang, M. Schlangen, T. Weiske, D. Usharani, S. Shaik and H. Schwarz, *J. Am. Chem. Soc.*, 2016, **138**, 7973-7981.

73 R. Wischert, P. Laurent, C. Copéret, F. Delbecq and P. Sautet, *J. Am. Chem. Soc.*, 2012, **134**, 14430-14449.

74 R. Wischert, C. Copéret, F. Delbecq and P. Sautet, *Angew. Chem., Int. Ed.*, 2011, **50**, 3202-3205.

75 T. Matsushima and J. M. White, *J. Catal.*, 1976, **44**, 183-196.

76 J. R. H. Ross, *Heterogeneous Catalysis: Fundamentals and Applications*, Elsevier, Amsterdam, 2012.

77 M. Yu and D. R. Trinkle, *J. Chem. Phys.*, 2011, **134**, 064111.

78 A. J. Page, S. Saha, H.-B. Li, S. Irle and K. Morokuma, *J. Am. Chem. Soc.*, 2015, **137**, 9281-9288.

79 T. Kreuger, W. P. M. van Swaaij, A. N. R. Bos and S. R. A. Kersten, *Chem. Eng. J.*, 2022, **427**, 130412.

80 C. T. Kresge, M. E. Leonowicz, W. J. Roth, J. C. Vartuli and J. S. Beck, *Nature*, 1992, **359**, 710-712.