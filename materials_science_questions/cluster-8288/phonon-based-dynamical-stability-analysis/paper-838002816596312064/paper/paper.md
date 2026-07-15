Article
https://doi.org/10.1038/s41467-023-36802-8

# Magnesium oxide-water compounds at megabar pressure and implications on planetary interiors

Received: 8 November 2022

Accepted: 15 February 2023

Published online: 01 March 2023

![](./images/838002816596312064_1.jpg)

Shuning Pan $^{1,5}$ , Tianheng Huang $^{1,5}$ , Allona Vazan $^{2}$ , Zhixin Liang $^{1}$ , Cong Liu $^{1}$ ,
Junjie Wang $^{1}$ , Chris J. Pickard $^{3,4}$ , Hui-Tian Wang $^{1}$ , Dingyu Xing $^{1}$ &
Jian Sun $^{1}$ 

Magnesium Oxide (MgO) and water ($\text{H}_2\text{O}$) are abundant in the interior of planets. Their properties, and in particular their interaction, significantly affect the planet interior structure and thermal evolution. Here, using crystal structure predictions and ab initio molecular dynamics simulations, we find that MgO and $\text{H}_2\text{O}$ can react again at ultrahigh pressure, although $\text{Mg(OH)}_2$ decomposes at low pressure. The reemergent MgO-$\text{H}_2\text{O}$ compounds are: $\text{Mg}_2\text{O}_3\text{H}_2$ above 400 GPa, $\text{MgO}_3\text{H}_4$ above 600 GPa, and $\text{MgO}_4\text{H}_6$ in the pressure range of 270–600 GPa. Importantly, $\text{MgO}_4\text{H}_6$ contains 57.3 wt % of water, which is a much higher water content than any reported hydrous mineral. Our results suggest that a substantial amount of water can be stored in MgO rock in the deep interiors of Earth to Neptune mass planets. Based on molecular dynamics simulations we show that these three compounds exhibit superionic behavior at the pressure-temperature conditions as in the interiors of Uranus and Neptune. Moreover, the water-rich compound $\text{MgO}_4\text{H}_6$ could be stable inside the early Earth and therefore may serve as a possible early Earth water reservoir. Our findings, in the poorly explored megabar pressure regime, provide constraints for interior and evolution models of wet planets in our solar system and beyond.

Understanding the reaction between water and rock-forming minerals is of fundamental importance in planetary astrophysics, since rocks and ices are abundant in the interiors of planets, in our solar system, and extrasolar planets $^{1-7}$. The distribution of elements within planetary interiors can have several effects on the observed properties of planets. Hidden elements, usually gases or volatiles, that are locked in refractories in the deep interiors have implications on the short- and long-term evolution of planets, and therefore on their observed properties of radius-mass relation and atmospheric composition $^{8-11}$. In our solar system Uranus and Neptune, the so-called "ice giants", may contain significant amounts of icy materials, by virtue of their distance from the Sun $^{7}$. Mysteries around the ice giants, such as the non-dipolar and non-axisymmetric magnetic fields $^{12}$ and the low luminosity of Uranus $^{13}$, highlight the need for more information about the composition and its properties in the interior conditions.

Water is expected to be abundant in exoplanets that were formed beyond the water ice-line $^{14}$. The processes of migration of planets inwards in the protoplanetary disk phase suggest that some of the observed close-in planets contain a substantial amount of water $^{15}$. Thus, the water-rock interaction and its properties are not only

$^{1}$National Laboratory of Solid State Microstructures, School of Physics and Collaborative Innovation Center of Advanced Microstructures, Nanjing University, 210093 Nanjing, China. $^{2}$Astrophysics Research Center of the Open University (ARCO), The Open University of Israel, 4353701 Raanana, Israel. $^{3}$Theory of Condensed Matter Group, Cavendish Laboratory, J. J. Thomson Avenue, Cambridge CB3 OHE, UK. $^{4}$Advanced Institute for Materials Research, Tohoku University 2-1-1 Katahira, Aoba, Sendai 980-8577, Japan. $^{5}$These authors contributed equally: Shuning Pan, Tianheng Huang. $\otimes$ e-mail: jiansun@nju.edu.cn

Nature Communications | (2023)14:1165

applicable to Uranus and Neptune, but also to the hundreds of intermediate-mass exoplanets that may have water-rich interiors. A classical model for water-rich intermediate-mass planets, like Uranus and Neptune, is usually structured in three layers³: a gas envelope consisting of hydrogen and helium; an ice (volatiles, mostly water) layer beneath it, and a rocky core of heavier (refractory) elements in the center. Newer models suggest interior structures with a gradual compositional distribution, based on formation models¹⁶⁻¹⁹ in agreement with Uranus and Neptune measurements²⁰ˢ²¹. However, all the models lack sufficient knowledge of composition interaction at high pressure. In practice, it is still unclear whether the transitions between different elements are sharp or continuous⁷ˢ²²ˢ²³. The recent prediction of He-H₂O compounds²⁴, H₃O²⁵, and SiO₂-H₂O compounds²⁶ indicate that the composition of these layers is much more complex than in the simple layered models. Therefore, improved planetary interior models require better knowledge of chemical interactions between interior elements, which is a key for long-term composition distribution in interiors.

The study of conductivity of water-rock compounds is an important parameter for the thermal evolution of the solar system ice-giants, as well as for wet exoplanets. In terrestrial planets the thermal conductivity of the lower mantle determines the rate at which heat flows across the core-mantle boundary, thus consequently influencing the evolution of both the mantle and the core²⁷. As an end-member of the (Mg,Fe)O ferropericlase and an effective heat conductor, MgO has been widely considered as a model mineral for estimating the thermal conductivity of the Earth's mantle²⁸. However, the thermal transport properties of the MgO-H₂O compounds at extreme conditions have not been investigated yet. To the best of our knowledge, this is the first simulation report on the thermal conductivities of the MgO-H₂O compounds in planetary interior conditions.

Further, it has been reported that the amount of water in the Earth's mantle is at least two times the mass of the ocean²⁹, as a consequence of the high water storage capacity of minerals³⁰ˢ³¹. However, according to models of Solar System the existence of so much water on Earth is abnormal³², as water is in a vapor form in the inner solar system. Many models are proposed to explain the abundance of water in the Earth, among them Enstatite chondrites³² and carbonaceous chondrites³³ as the carrier of water into the young Earth. Measurement of the D/H ratio in lava samples revealed that the water in the Earth's deep mantle may originate from protosolar nebula, being stored in the rock³⁴. Understanding the origin, transportation, and storage of water in the deep Earth requires the study of hydrous minerals, such as brucite (Mg(OH)₂), serpentine (Mg₃Si₂O₉H₄), chondrodite (Mg₅Si₂O₁₀H₂) and phase B (Mg₁₂Si₄O₂₁H₂). It was suggested that δ-AlOOH³⁵ and Mg(OH)₂³⁶ within the subduction slab can deliver water into the Earth's interior. A recent study³⁷ finds two olivine-water compounds at the Earth's core condition, which could host much of Earth's water in the first 50-100 million years of its history.

MgO is one of the most abundant rocks in the interiors of planets³⁸⁻⁴⁴. Interestingly, MgO exhibits high solubility in water (200-400 g/l) between 24-38 GPa, which decreases after 55 GPa⁴⁵. At ambient conditions, MgO and H₂O combine to form brucite (Mg(OH)₂), which has a layered structure with space group symmetry P3m1. Upon compression, the protons become disordered⁴⁶ and its symmetry reduces to $P\overline{3}$⁴⁷. At 18 GPa, brucite transforms to a $P4_12_12$

![](./images/838002816596312064_2.jpg)

![](./images/838002816596312064_3.jpg)

![](./images/838002816596312064_4.jpg)

![](./images/838002816596312064_5.jpg)

![](./images/838002816596312064_6.jpg)

Fig. 1 | Formation enthalpy and crystal structure of MgO-H₂O compounds.
a Convex hull of formation enthalpy at 300-900 GPa. The circle symbols represent stable compositions. The x symbols represent the compositions that decompose. The zero-point energy of phonons is considered in this figure. For MgO, we consider its B1 and B2 phases. For water, we consider all the stable phases mentioned in Ref. ⁷⁴ including ice X, Pbcm, Pbca, and P3₁21 phase. b The formation enthalpy of MgO₄H₆ at 250-300 GPa. With ZPE, MgO₄H₆ becomes stable at 270 GPa. c-e The crystal structure of Mg₂O₃H₂, MgO₃H₄, and MgO₄H₆, respectively. The orange, red and white spheres correspond to Mg, O, and H atoms.

phase³⁶ with a three-dimensional network structure. When pressure reaches 27 GPa, brucite decomposes into MgO and ice-VII³⁶. It is yet unclear whether there are other stable MgO–H₂O compounds at a higher pressure of hundreds of GPa in planetary interiors.

In this study, with crystal structure predictions, we find three new MgO–H₂O compounds at ultrahigh pressure: Mg₂O₃H₂ above 400 GPa, MgO₃H₄ above 600 GPa, and MgO₄H₆ in the pressure range of 270–600 GPa. Ab initio and machine-learning molecular dynamics simulations reveal their superionic behavior at the pressure-temperature conditions as in the interiors of Uranus and Neptune. Furthermore, we calculate their thermal conductivity and electronic conductivity, which may have effects on the magnetic field and luminosity of Uranus and Neptune.

## Results
### Prediction of new structures
Here, we perform variable-composition structure predictions on MgO–H₂O binary system at 200, 300, 500, and 1000 GPa. Our structure prediction calculations show three stable MgO–H₂O compounds: Mg₂O₃H₂, MgO₃H₄, and MgO₄H₆ (Fig. 1c–e). According to the convex hull of normalized formation enthalpies, these compounds are stable at above 400 GPa, above 600 GPa, and between 270 and 600 GPa, respectively (Fig. 1a, b). The detailed structure parameters are provided in the supplementary material. We also confirmed the convex hull using other calculation methods, as shown in Fig. S2. The inclusion of zero-point energy only slightly changes the stable pressure of MgO₄H₆ from 270 GPa to about 280 GPa (Fig. 1b), indicating that the influence from the nuclei quantum effect on the stability of these compounds is small. Phonon calculations show that all three phases are dynamically stable, exhibiting no imaginary phonon modes. Electronic structure calculations show that all three phases are insulators with large band gaps, as shown in Fig. S3.

In all three phases, H atoms form two symmetrized bonds with O atoms. The symmetrization of H bonds is common in high-pressure ice phases, such as ice-VII⁴⁸ and ice-X⁴⁹. Note that the Mg atoms in MgO₃H₄ are nine-fold coordinated by O atoms, which is a rare phenomenon. The coordination numbers of MgO-B1 and MgO-B2 phases are six and eight, respectively. According to Li et al.³⁷, the only nine-fold coordinated Mg found in minerals is in β-Mg₂SiO₅H₂. The high coordination of MgO₃H₄ confirms their hypothesis³⁷ that hydration can increase the coordination of Mg.

The water-rich phase MgO₄H₆ predicted in this work has an extremely high water storage capacity. It contains 57.3 wt % of water, which is far higher than any reported hydrous minerals, including recently found 11.4 wt % in Mg₂SiO₅H₂³⁷, ~15 wt % in δ-AlO₂H and MgSiO₄H₂. In Fig. S4 we show the pressure-density relationship. The densities of all three phases are between those of MgO and H₂O. As expected, their densities increase with their MgO ratio. A comparison of the density of each compound to an equivalent MgO-water mixture according to the Additive Volume Law (AVL) shows differences of up to 4% in density, where AVL is usually higher than the reported density.

### Superionic behavior in MgO–H₂O compounds
We carried out ab initio molecular dynamics to explore the state of these phases under high temperature, corresponding to the interior of super-Earth to Neptune mass planets. We follow the mean square displacement (MSD) of the MD trajectories (Fig. 2a–c). All three phases exhibit similar behavior: at low temperature, the MSD slopes for all the atoms are zero, which means that they stay near their equilibrium positions and the sample is in the solid state. On increasing the temperature, the slope of MSDs of the Mg and O atoms remains zero, while the MSD slope of the H atoms becomes none-zero, which means that H atoms leave their equilibrium positions and diffuse like a liquid in the sublattice form by Mg and O atoms. The snapshots of the MD trajec-

![](./images/838002816596312064_7.jpg)

Fig. 2 | The dynamic properties of MgO–H₂O compounds from molecular dynamics simulations. a The mean square displacement (MSD) of Mg₂O₃H₂ at 400 GPa, 6000 K (the isentropic condition of Uranus). b The MSD of MgO₃H₄ at 700 GPa, 5000 K (the isentropic condition of Neptune). c The MSD of MgO₄H₆ at 500 GPa, 5000 K (the isentropic condition of Uranus). d–f The snapshots of MD trajectories. The orange and red spheres correspond to Mg and O atoms. The blue points represent H atoms. The position of H atoms from 1000 frames is shown in the picture. We use magenta spheres to highlight the trajectory of a single H atom.

![](./images/838002816596312064_8.jpg)

Fig. 3 | The phase diagrams of MgO–H₂O compounds. a Mg₂O₃H₂, b MgO₃H₄ and c MgO₄H₆. The purple and blue lines represent the isentropic lines of Uranus and Neptune. The solid and dashed purple line corresponds to U1 and U2 models. The solid and dashed blue line corresponds to N1 and N2b models. The data of models are from ref. ³. The diamonds represent the condition of the core-mantle boundary.

tories (Fig. 2d–f) show that the spatial distribution of different H atoms overlaps. Such a state is known as the 'superionic state'⁵⁰, which is common in hydrates under high pressure. More discussion about the definition of superionic state is available in the supplementary information. The proton diffusion rate is the highest in MgO₄H₆ and the lowest in Mg₂O₃H₂, indicating that the diffusion rate increases with H₂O content. At higher temperatures, the MSD of all the atoms becomes nonzero, and the sample becomes liquid. The radius distribution function (RDF) and vibrational density of state (VDOS) are shown in Figs. S5–6.

The phase diagrams of the three compounds are shown in Fig. 3a–c, together with the isentropic interior profiles of Uranus and Neptune from Nettelmann et al.³. The phase diagrams show that Mg₂O₃H₂ and MgO₄H₆ are superionic in interiors of Uranus and Neptune, while MgO₃H₄ is not superionic in one (N2b) Neptune model³. Non-isentropic models of Uranus and Neptune have much hotter deep interiors and slightly colder outer envelopes, due to slower cooling⁵¹⁵². The deep interiors in non-isentropic models lay above the superionic phase, in the liquid phase. In these models, the stably stratified region below the convective envelope accounts for the magnetic field generator¹².

Mg₂O₃H₂, MgO₃H₄ and MgO₄H₆ have distinct superionic temperature and melting point. These properties are closely related to the geometry of crystalline cage formed by Mg–O polyhedral, as shown in Fig. 1c–e. In MgO₄H₆, Mg-O polyhedral forms one-dimensional chains. Different chains are interconnected by O–H–O bonds. In MgO₃H₄, Mg-O polyhedral forms two-dimensional layer structure. O–H–O bonds connect different layers. In contrast, the Mg–O polyhedral in Mg₂O₃H₂ connects to all its neighbors by Mg–O bonds. In superionic phase, the O–H bonds can be broken, affecting the stability of chain/layer structures at high temperature. But Mg–O bonds stay intact in superionic phase. Thus, Mg₂O₃H₂ has higher melting point than the other two compounds.

In Fig. 4a–c, we project the mean square displacement (MSD) of protons into the x, y, and z direction. All three compounds show some degree of anisotropy. In MgO₃H₄, the preferable diffusion directions are a and b direction, because it is more difficult for protons to move across Mg–O layers. The preferable diffusion direction in MgO₄H₆ is the c direction, since the diffusion perpendicular to Mg–O chains is hindered. The preferable diffusion direction in Mg₂O₃H₂ is the b direction. However, even in the b direction the diffusion path is blocked by Mg–O polyhedral, which indicates a large energy barrier. This is why Mg₂O₃H₂ has higher solid-superionic temperature and low diffusion rate, compared with MgO₃H₄ and MgO₄H₆.

The solid-superionic temperature can also be affected by the degree of localization of protons. In all three compounds, each proton connects to two O atoms, forming (possibly nonsymmetric) O–H–O bonds. We use the three-body analysis in reference⁵³ to analyze the O–H–O bonds. We find all O–H–O triplets by first find the closest oxygen (Oₐ) and second oxygen (Oᵦ) of each H atom. At zero temperature, the difference of two H-O bonds in length (HOᵦ–HOₐ) is 0.07 Å in Mg₂O₃H₂ (800 GPa), 0.07–0.18 Å in MgO₃H₄ (800 GPa), 0–0.02 Å in MgO₄H₆ (600 GPa). Among them, the O–H–O bonds are the most nonsymmetric in MgO₃H₄, and most symmetric in MgO₄H₆. At finite temperature, the spatial distribution of protons in Fig. 4d–f shows that the protons in MgO₃H₄ have higher degree of delocalization compared with MgO₄H₆. Thus, the protons in MgO₃H₄ are less confined to a O–H–O triplet, making solid-superionic temperature lower.

The proton flow of the superionic phase can generate electrical transport. We employed the Nernst-Einstein equation to calculate the ionic electrical conductivity of MgO–H₂O compounds under the core-mantle boundary condition of Uranus and Neptune. As is shown in Fig. 5b, in the temperature range from 1000 K to 6000 K at 600 GPa, the electrical conductivity of Mg₂O₃H₂ is 0.36–11.07/Ω cm in Mg₂O₃H₂, 26–93/Ω cm for MgO₃H₄, and 26–137/Ω cm for MgO₄H₆. The electrical conductivity of Mg₂O₃H₂ is much lower than H₂O (120–350/Ω cm)². In MgO₃H₄ and MgO₄H₆, the electrical conductivities are also lower than H₂O, but they are in the same order of magnitude. More details concerning these calculations are provided in the supplementary material.

![](./images/838002816596312064_9.jpg)

![](./images/838002816596312064_10.jpg)

### Thermal conductivity
The distribution of the three compounds in the interior depends on their density. Since stable $MgO_4H_6$ has a high water ratio and thus lower density than the other two compounds, as is shown in Fig. S2, it is located near the pure ice layer. On the contrary, $Mg_2O_3H_2$ is stable above 400 GPa pressure and has a lower water ratio, and thus is more favorable in the deeper region near the rocky core. The compounds we found indicate that rocky core erosion is supported by the ice-rock interaction with the surrounding ice layer, forming a composition gradient. In Fig. 6 we present such possible structures for Uranus and Neptune, based on the models of Nettelmann et al.³

Composition distribution has implications for heat transport. The composition gradients shown in Fig. 6 are of decreasing outwards mean molecular weight, which may suppress heat transport by large-scale convection⁵⁴,⁵⁵. The low luminosity (surface heat flux) of Uranus means that its surface is very cold. So, either all its heat has been lost, or the heat is captured inside. It has been hypothesized that some form of thermal boundary slows down the cooling process. One explanation for the low luminosity of Uranus is a composition gradient between the metal-rich (ice/rock) interior to the gas envelope, which suppresses convection, hence the heat is trapped in the deep interior while the surface is cold⁵¹,⁵². Here we suggest a compositional gradient between a rock-rich deep interior and an ice-rich upper layer. Although this scenario requires some further investigation, under certain conditions it may perform as a barrier for heat transport to explain Uranus' low luminosity. The exact composition gradient and its effect on heat transport is beyond the scope of this paper, more details can be found in dedicated works⁴⁵,⁵¹,⁵²,⁵⁴⁻⁵⁶.

When convection is suppressed by a composition gradient in the interior, the heat transport is via layered convection⁵¹ and/or conduction. We thus investigated the thermal conductivities of the MgO–H₂O

![](./images/838002816596312064_11.jpg)

Fig. 6 | Suggested interior models for internal structure models of Uranus and Neptune based on the data from the U2 and N1 models in Ref. ³. The blue-brown gradual change region is where MgO-H₂O compounds can exist.

compounds in the temperature range from 1000 K to 6000 K and compared them with the thermal conductivities of the B2 phase MgO. As shown in Fig. 5a, the thermal conductivities of Mg₂O₃H₂, MgO₃H₄ and MgO₄H₆ at 600 GPa and 3000 K are 13.439, 21.323, and 23.590 W m⁻¹ K⁻¹, respectively, positively related to the water content. These values are evidently lower than the thermal conductivities of the MgO under the same conditions. In addition, all three compounds have a distinct property that their thermal conductivities do not change much with increasing temperature in the range from 3000 K to 6000 K, in which these compounds remain in a superionic state. The states of the MgO-H₂O compounds significantly affect their thermal conductivities. Figure 5a shows that in the range from 1000 K to 2000 K the thermal conductivities of all three compounds decrease with the increasing temperature, which is consistent with other solids but different from their behavior in the superionic state.

## Discussion
The abundance of different compositions in planets are still an open question. The ice to rock ratio in interior models of Uranus and Neptune is degenerated, varying from rock dominated to ice dominated models⁵⁷. Based on planet formation models, abundances of rocks and ices are expected to be similar in mass exterior to the ice-line (water condensation line). Interior models of planets suggest that rocky composition mainly consist of Mg, Si, and Fe compounds³⁸, where MgO and SiO₂ are the most basic compounds. From the abundance of chemical elements in the universe⁵⁸, we can see that the abundance of Mg, Si and Fe are very similar. MgO is also the main topic in some recent studies²²˴⁴⁵ about planet models. As a result, we can safely assume that MgO as one of the main components of the rocky core. H₂O is the most abundant ice, and the first to condense in the protoplanetary disk, thus it is expected to be main components of "hot ice" layer.

The superionic behavior of rock compounds with water was reported in several systems and isn't unique to MgO rock. Silica and water may form superionic Si₂O₅H₂ at conditions as of the core-mantle boundary of Uranus and Neptune²⁴. Under a hydrogen-rich environment, water forms H₃O and still has superionic behavior²⁵. As recent experimental work⁴⁵ showed that MgO is highly soluble in water at 10 GPa conditions such as in the upper layers of Uranus and Neptune, the MgO-H₂O ionization phases at higher pressure have to be explored. In this research, we find that all three stable MgO-H₂O compounds exhibit superionic behavior at the condition in interiors of super-Earths and Neptunes. We infer that the superionic behavior of water is consistent with compositional inhomogeneity, such as the enrichment of SiO₂, MgO, and H.

In Fig. 6 we sketched the internal structure models of Uranus and Neptune based on the predicted MgO-H₂O compounds, on top of the data from the U2 and N1 model in Nettelmann et al.³. In traditional three-layer model³, there is a boundary between rock core and ice layer and the density profile is discontinuous at the boundary. It was shown that a gradual transition model should be able to explain the observational results⁵⁹. Our prediction of MgO-H₂O compounds indicates that the ice layer can erode the MgO rock in the core and results in a "fuzzier" boundary. This is in favor of the gradual transition model. However, the structures shown in Fig. 6 are suggestions, and the exact composition distribution in Uranus and Neptune are beyond the scope of this paper and requires further investigation.

The superionic state of the MgO-H₂O compounds has lower electrical conductivity in comparison to pure water at the same conditions. However, the compounds found in this work are stable at higher pressure, i.e., much deeper in the interior than the predicted location of the magnetic field generator in Uranus and Neptune¹². In this case, as is emphasized in Fig. 5, the magnetic field is generated in an upper pure water layer.

In addition to playing a central role in the evolution of the ice giants, the MgO-H₂O compounds found here are relevant also for water-rich exoplanets. The deep interiors of exoplanets in the mass range of super-Earths to Neptunes are found to be similar for further out planets and their planetary twins that have migrated inwards²³. Therefore, the compound found here are relevant also for migrating in water-rich exoplanets. Interior models of exoplanets with mixed ice and rock were recently suggested¹¹˴²³, but lack of knowledge on ice-rock interaction at 100 s GPa pressure. The three compounds found here indicate that high water content, of up to 57.3 wt%, is possible in the deep interiors of wet planets in the super-Earth to Neptune mass range. Such planets may have surface oceans or steam atmospheres caused by the ice-rock separation at low pressures²³, and fit the recent discovery of exoplanets around M dwarfs with densities of 50% rock and 50% water¹⁵.

Furthermore, the water-rich compound MgO₄H₆ may help explain the origin of water on the Earth. Magnesium hydrosilicate compounds are found to be able to store a large amount of water (up to 8 times the mass of the ocean) in the Earth's depths³⁷. Similarly, the MgO₄H₆ we find in this study is stable above 270 GPa, suggesting that water could be stored in the central region of the early Earth in the form of MgO₄H₆. According to this scenario, the dense iron alloys that sunk to the Earth's core moved up the MgO₄H₆ to a shallower region, where it decomposed and released the water: $MgO_4H_6 \rightarrow MgO + 3H_2O$.

In summary, we find three new sable MgO-H₂O compounds at megabar pressures. One of the compounds has the highest reported water content of 57.3 wt%. All three phases exhibit superionic behavior under the P-T conditions corresponding to the interior of planets and are consistent with the properties of Uranus and Neptune. The MgO₄H₆ compound may also serve as one of the Earth's early water reservoirs. We conclude that MgO-water mixtures are likely in deep interiors of water-rich super-Earth to Neptune mass planets, where a large fraction of the water can be locked in MgO rocks in the deep interior. The existence of various compounds supports gradual composition distribution in planetary interiors.

## Methods
### Structure prediction
The structures of the $(MgO)_x\text{(H}_2\text{O)}_y$, ($x$=1-4, $y$=1-4) system are searched by Magus code$^{60,61}$ with up to 40 atoms per unit cell. Each generation contains 30 structures, and we run over 60 generations until the result converges. The 40% outcome structures with the lowest enthalpy were used as the seeds for the evolution of the next generation and the left structures in each generation were randomly produced. We also performed some other more complex variable-composition structure predictions on the Mg-O-H ternary system to check the results. The results were cross-checked using the AIRSS$^{62,63}$ code.

### Ab initio calculations
The ab initio calculations are performed by the VASP code$^{64}$. We use the standard projector augmented-wave (PAW) method$^{65}$ and the Perdew-Burke-Ernzerhof exchange-correlation functional$^{66}$ in the generalized gradient approximation. We treat $2s^22p^63s^2$, $2s^22p^4$, and $1s^1$ electrons as valence elections for Mg, O and H atoms. We used a plane-wave energy cutoff of 1050 eV and the k-point sample resolution of $2\pi$ × 0.025 Å⁻¹ for the ab initio calculations. The result of the convergence test is provided in the supplementary material (Fig. S1). The results were cross-checked using CASTEP$^{67,68}$ code with similar parameters. The phonon and zero-point energy (ZPE) calculations were performed with the PHONOPY code$^{69}$.

### Molecular dynamics (MD) simulations
The MD simulation was performed with an NVT ensemble using the Nosé-Hoover thermostat$^{70}$ implemented in VASP. For AIMD simulation, we used gamma point for k-point sampling, 600 eV for plane-wave energy cutoff, and standard pseudopotentials. The timestep was set to 0.5 fs to treat the fast-moving protons. The total simulation time was 10 ps. As for the MD with machine-learning neural network potential, we used GPUMD$^{71}$ with periodic boundary conditions and a time step of 0.25 fs. The total time of a simulation was at least 1 ns.

### Electrical conductivity
We use Nernst-Einstein equation ($\sigma=DNq^2/k_BT$) to calculate electrical conductivity. In the equation, $q$ is the carrier electric charge (1e for H atoms), $D$ is the carrier diffusion coefficient, $N$ is the carrier density, and $T$ is the temperature. All these values can be extracted from the MD trajectories.

### Thermal conductivity
We used the Green-Kubo formula together with Onsager's phenomenological approach to calculate thermal conductivity, as implemented in Sportrans$^{72,73}$. In this approach the interactions among different conserved fluxes are explicitly accounted for by Onsager's phenomenological relations:

$$
J_i = \sum_j \Lambda_{ij} f_j \tag{1}
$$

$J$ is a generic conversed flux and $f$ is a thermodynamic affinity. $\Lambda_{ij}$ coefficients are expressed as integrals of the relevant fluxes:

$$
\Lambda_{ij} = \frac{\Omega}{k_B} \int_0^\infty \left\langle \mathscr{I}_i(t) \mathscr{I}_j(0) \right\rangle \mathrm{d}t \tag{2}
$$

$\mathscr{I}_i(t)$ is the time series of the $i$th flux and can be obtained from the MD simulation. $\Omega$ is the volume of the system and $k_B$ is the Boltzmann constant. Theoretically, $i$th flux represent all the flux which should be considered. In this study, since all three MgO-H₂O compounds are insulator, we did not take electronic thermal flux into consideration.

Another reason for us to ignore the electronic thermal flux is that we used more than 6000 atoms to run the MD simulations, making it impossible to get electron wave functions. So, in this paper $i$th flux represent ionic thermal flux and the lattice thermal flux.

### Machine-Learning neural network potential
We trained a machine-learning neural network potential for the Mg-O-H system using the NEP and GPUMD$^{71}$ method, which directly uses relative atomic coordinates to describe local atomic environments to obtain atomic energies, while forces are obtained by taking the derivatives of the energies. Our dataset was built by choosing 16,000 configures in the trajectories from AIMD in the NVT ensemble in the pressure range from 300 GPa to 800 GPa with a temperature step of 1000 K from 3000 to 7000 K.

## Data availability
All data that support the conclusions of this study are included in the article and the Supplementary Information file. These data are available from the corresponding author upon request.

## References
1. Rogers, L. A. & Seager, S. A framework for quantifying the degeneracies of exoplanet interior compositions. *Astrophys. J.* **712**, 974-991 (2010).
2. Redmer, R., Mattsson, T. R., Nettelmann, N. & French, M. The phase diagram of water and the magnetic fields of Uranus and Neptune. *Icarus* **211**, 798-803 (2011).
3. Nettelmann, N., Helled, R., Fortney, J. J. & Redmer, R. New indication for a dichotomy in the interior structure of Uranus and Neptune from the application of modified shape and rotation data. *Planet. Space Sci.* **77**, 143-151 (2013).
4. Noack, L. et al. Water-rich planets: How habitable is a water layer deeper than on Earth? *Icarus* **277**, 215-236 (2016).
5. Dorn, C. et al. A generalized Bayesian inference method for constraining the interiors of super Earths and sub-Neptunes. *Astron. Astrophys.* **597**, 1-16 (2017).
6. Soubiran, F. & Militzer, B. Anharmonicity and phase diagram of magnesium oxide in the megabar regime. *Phys. Rev. Lett.* **125**, 175701 (2020).
7. Helled, R., Nettelmann, N. & Guillot, T. Uranus and Neptune: origin, evolution and internal structure. *Space Sci. Rev.* **216**, 38 (2020).
8. Hori, Y. & Ikoma, M. Gas giant formation with small cores triggered by envelope pollution by icy planetesimals. *Mon. Not. R. Astron. Soc.* **416**, 1419-1429 (2011).
9. Chachan, Y. & Stevenson, D. J. On the role of dissolved gases in the atmosphere retention of low-mass low-density planets. *Astrophys. J.* **854**, 21 (2018).
10. Kite, E. S., Bruce, F. Jr., Schaefer, L. & Ford, E. B. Superabundance of exoplanet sub-neptunes explained by fugacity crisis. *Astrophys. J.* **887**, L33 (2019).
11. Dorn, C. & Lichtenberg, T. Hidden water in magma ocean exoplanets. *Astrophys. J. Lett.* **922**, L4 (2021).
12. Stanley, S. & Bloxham, J. Numerical dynamo models of Uranus' and Neptune's magnetic fields. *Icarus* **184**, 556-572 (2006).
13. Guillot, T. & Gautier, D. in *Treatise Geophys* 2nd edn, (ed Schubert, G.) (Elsevier, 2015).
14. Lodders, K. Solar system abundances and condensation temperatures of the elements. *Astrophys. J.* **591**, 1220 (2003).
15. Luque, R. & Pallé, E. Density, not radius, separates rocky and water-rich small planets orbiting M dwarf stars. *Science* **377**, 1211-1214 (2022).
16. Bodenheimer, P., Stevenson, D. J., Lissauer, J. J. & D'Angelo, G. New formation models for the Kepler-36 system. *Astrophys. J.* **868**, 138 (2018).

17. Brouwers, M. G., Vazan, A. & Ormel, C. W. How cores grow by pebble accretion: I. Direct core growth. Astron. Astrophys. **611**, 1-12 (2018).

18. Valletta, C. & Helled, R. Giant planet formation models with a self-consistent treatment of the heavy elements. Astrophys. J. **900**, 133 (2020).

19. Ormel, C. W., Vazan, A. & Brouwers, M. G. How planets grow by pebble accretion: III. Emergence of an interior composition gradient. Astron. Astrophys. **647** (2021).

20. Marley, M. S., Gomez, P. & Podolak, M. Monte Carlo interior models for Uranus and Neptune. J. Geophys. Res. **100**, 349-353 (1995).

21. Podolak, M., Podolak, J. I. & Marley, M. S. Further investigations of random models of Uranus and Neptune. Planet. Space Sci. **48**, 143-151 (2000).

22. Nettelmann, N. Stardust in the deep interior of low-mass planets. Nat. Astron. **5**, 744-745 (2021).

23. Vazan, A., Sari, R. & Kessel, A. A new perspective on the interiors of ice-rich planets: ice-rock mixture instead of ice on top of rock. Astrophys. J. **926**, 150 (2022).

24. Liu, C. et al. Multiple superionic states in helium-water compounds. Nat. Phys. **15**, 1065-1070 (2019).

25. Huang, P. et al. Stability of $\mathrm{H_2O}$ at extreme conditions and implications for the magnetic fields of Uranus and Neptune. Proc. Natl Acad. Sci. USA **117**, 5638-5643 (2020).

26. Gao, H. et al. Superionic silica-water and silica-hydrogen compounds in the deep interiors of Uranus and Neptune. Phys. Rev. Lett. **128**, 35702 (2022).

27. Sakuraba, A. & Roberts, P. H. Generation of a strong magnetic field using uniform heat flux at the surface of the core. Nat. Geosci. **2**, 802-805 (2009).

28. Hofmeister, A. M. Thermal diffusivity and thermal conductivity of single-crystal MgO and $\mathrm{Al_2O_3}$ and related compounds as a function of temperature. Phys. Chem. Miner. **41**, 361-371 (2014).

29. Ahrens, T. J. Water storage in the mantle. Nature **342**, 122-123 (1989).

30. Pearson, D. G. et al. Hydrous mantle transition zone indicated by ringwoodite included within diamond. Nature **507**, 221-224 (2014).

31. Schmandt, B., Jacobsen, S. D., Becker, T. W., Liu, Z. & Dueker, K. G. Dehydration melting at the top of the lower mantle. Science **344**, 1265-1268 (2014).

32. Peslier, A. H. The origins of water. Science **369**, 1058 (2020).

33. Warren, P. H. Stable-isotopic anomalies and the accretionary assemblage of the Earth and Mars: a subordinate role for carbonaceous chondrites. Earth Planet. Sci. Lett. **311**, 93-100 (2011).

34. Hallis, L. J. et al. Evidence for primordial water in Earth's deep mantle. Science **350**, 795-797 (2015).

35. Sano, A. et al. Aluminous hydrous mineral $\delta$-AlOOH as a carrier of hydrogen into the core-mantle boundary. Geophys. Res. Lett. **35**, 1-5 (2008).

36. Hermann, A. & Mookherjee, M. High-pressure phase of brucite stable at Earth's mantle transition zone and lower mantle conditions. Proc. Natl Acad. Sci. USA **113**, 13971-13976 (2016).

37. Li, H.-F. et al. Ultrahigh-pressure magnesium hydrosilicates as reservoirs of water in early Earth. Phys. Rev. Lett. **128**, 035703 (2022).

38. Hubbard, W. B. Interiors of the giant planets. Science **214**, 145-149 (1981).

39. Umemoto, K., Wentzcovitch, R. M. & Allen, P. B. Dissociation of $\mathrm{MgSiO_3}$ in the cores of gas giants and terrestrial exoplanets. Science **311**, 983-986 (2006).

40. Wilson, H. F. & Militzer, B. Rocky core solubility in Jupiter and giant exoplanets. Phys. Rev. Lett. **108**, 1-4 (2012).

41. McWilliams, R. S. et al. Phase transformations and metallization of magnesium oxide at high pressure and temperature. Science **338**, 1330-1333 (2012).

42. Root, S. et al. Shock response and phase transitions of MgO at planetary impact conditions. Phys. Rev. Lett. **115**, 1-6 (2015).

43. Dorn, C. et al. Can we constrain the interior structure of rocky exoplanets from mass and radius measurements? Astron. Astrophys. **577**, A83 (2015).

44. Unterborn, C. T. & Panero, W. R. The pressure and temperature limits of likely rocky exoplanets. J. Geophys. Res. Planets **124**, 1704-1716 (2019).

45. Kim, T. et al. Atomic-scale mixing between MgO and $\mathrm{H_2O}$ in the deep interiors of water-rich planets. Nat. Astron. **5**, 815-821 (2021).

46. Duffy, T. S., Meade, C., Fei, Y., Mao, H. & Hemley, R. J. High-pressure phase transition in brucite, $\mathrm{Mg(OH)_2}$. American Minralogist **80**, 222-230 (1995).

47. Mookherjee, M. & Stixrude, L. High-pressure proton disorder in brucite. Am. Mineral. **91**, 127-134 (2006).

48. Guthrie, M. et al. Structure and disorder in ice VII on the approach to hydrogen-bond symmetrization. Phys. Rev. B **99**, 184112 (2019).

49. Telxelira, J. High-pressure physics: the double identity of ice X. Nature **392**, 232-233 (1998).

50. Millot, M. et al. Nanosecond X-ray diffraction of shock-compressed superionic water ice. Nature **569**, 251-255 (2019).

51. Vazan, A. & Helled, R. Explaining the low luminosity of Uranus: a self-consistent thermal and structural evolution. Astron. Astrophys. **633**, 1-10 (2020).

52. Scheibe, L., Nettelmann, N. & Redmer, R. Thermal evolution of Uranus and Neptune: II. Deep thermal boundary layer. Astron. Astrophys. **650**, 1-12 (2021).

53. Hernandez, J. A. & Caracas, R. Superionic-superionic phase transitions in body-centered cubic $\mathrm{H_2O}$ ice. Phys. Rev. Lett. **117**, 1-5 (2016).

54. Rosenblum, E., Garaud, P., Traxler, A. & Stellmach, S. Erratum: turbulent mixing and layer formation in double-diffusive convection: three-dimensional numerical simulations and theory (Astrophysical Journal (2011) 731 (66)). Astrophys. J. **742**, 96768 (2011).

55. Vazan, A., Helled, R., Kovetz, A. & Podolak, M. Convection and mixing in giant planet evolution. Astrophys. J. **803**, 32 (2015).

56. Fortney, J. J. & Nettelmann, N. The interior structure, composition, and evolution of giant planets. Space Sci. Rev. **152**, 423-447 (2010).

57. Teanby, N. A., Irwin, P. G. J., Moses, J. I. & Helled, R. Neptune and Uranus: Ice or rock giants. Philos. Trans. R. Soc. A: Math. Phys. Eng. Sci. **378**, (2020).

58. Trimble, V. The origin and abundances of the chemical elements. Rev. Mod. Phys. **47**, 877-976 (1975).

59. Helled, R., Anderson, J. D., Podolak, M. & Schubert, G. Interior models of Uranus and Neptune. Astrophys. J. **726** (2011).

60. Xia, K. et al. A novel superhard tungsten nitride predicted by machine-learning accelerated crystal structure search. Sci. Bull. **63**, 817-824 (2018).

61. Gao, H., Wang, J., Han, Y. & Sun, J. Enhancing crystal structure prediction by decomposition and evolution schemes based on graph theory. Fundam. Res. **1**, 466-471 (2021).

62. Pickard, C. J. & Needs, R. J. High-pressure phases of silane. Phys. Rev. Lett. **97**, 1-4 (2006).

63. Pickard, C. J. & Needs, R. J. Ab initio random structure searching. J. Phys. Condens. Matter **23**, (2011).

64. Kresse, G. & Furthmüller, J. Efficient iterative schemes for ab initio total-energy calculations using a plane-wave basis set. Phys. Rev. B —Condens. Matter Mater. Phys. **54**, 11169-11186 (1996).

65. Joubert, D. From ultrasoft pseudopotentials to the projector augmented-wave method. Phys. Rev. B—Condens. Matter Mater. Phys. **59**, 1758-1775 (1999).

66. Perdew, J. P., Burke, K. & Ernzerhof, M. Generalized gradient approximation made simple. Phys. Rev. Lett. **77**, 3865-3868 (1996).

67. Segall, M. D. et al. First-principles simulation: Ideas, illustrations and the CASTEP code. J. Phys. Condens. Matter **14**, 2717-2744 (2002).

68. Clark, S. J. et al. First principles methods using CASTEP. Z. Krist. 220, 567–570 (2005).

69. Togo, A. & Tanaka, I. First principles phonon calculations in mate- rials science. Scr. Mater. 108, 1–5 (2015).

70. Nose, S. Constant temperature molecular dynamics methods lim- itations in simulations in the microcanonical ensemble. Prog. Theor. Phys. Suppl. 103, 1–46 (1991).

71. Fan, Z. et al. GPUMD: A package for constructing accurate machine- learned potentials and performing highly efficient atomistic simu- lations. J. Chem. Phys. 157, 114801 (2022).

72. Bertossa, R., Grasselli, F., Ercole, L. & Baroni, S. Theory and numerical simulation of heat transport in multicomponent systems. Phys. Rev. Lett. 122, 255901 (2019).

73. Grasselli, F., Stixrude, L. & Baroni, S. Heat and charge transport in H₂O at ice-giant conditions from ab initio molecular dynamics simulations. Nat. Commun. 11, 1–7 (2020).

74. Pickard, C. J., Martinez-Canales, M. & Needs, R. J. Decom- position and terapascal phases of water ice. Phys. Rev. Lett. 110, 1–5 (2013).

## Acknowledgements
J.S. gratefully acknowledges the financial support from the National Key R&D Program of China (grant nos. 2022YFA1403201), the National Nat- ural Science Foundation of China (grant nos. 12125404, 11974162, and 11834006), and the Fundamental Research Funds for the Central Uni- versities. C.J.P is supported by the EPSRC through grants EP/P022596/1, and EP/S021981/1; A.V. acknowledges support by the ISF through grants 770/21 and 773/21. The calculations were carried out using super- computers at the High Performance Computing Center of Collaborative Innovation Center of Advanced Microstructures, the high-performance supercomputing center of Nanjing University.

## Author contributions
J.S. conceived and led the project. S.P., T.H., Z.L., J.W., and C.J.P. performed the calculations. S.P., T.H., J.S., A.V., C.L., and C.J.P. ana- lyzed the data. S.P., T.H., A.V., J.S., C.J.P., H.-T.W., and D.X. wrote the manuscript. All authors discussed the results and commented on the manuscript.

## Competing interests
C.J.P. is an author of the CASTEP code, and receives royalty payments from its commercial sales by Dassault Systèmes. The remaining authors declare no competing interests.

## Additional information
Supplementary information The online version contains supplementary material available at
https://doi.org/10.1038/s41467-023-36802-8.

Correspondence and requests for materials should be addressed to Jian Sun.

Peer review information Nature Communications thanks the anon- ymous reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.

Reprints and permissions information is available at
http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jur- isdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2023