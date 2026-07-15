# BIOMECHANICS OF SUPERPARAMAGNETIC NANOPARTICLES FOR LASER HYPERTHERMIA

Maryam Fatima\*, Ayesha Sohail\*,**, Khush Bakhat Akram†,
Lubna Sherin‡, Saad Ihsan Butt\*, M. Abid§,¶ and O. Anwar Bég∥

\*Department of Mathematics
COMSATS University Islamabad
Lahore Campus 54000, Pakistan

†National University of Technology (NUTECH)
Main IJP Road, Sector I-12, Islamabad, Pakistan

‡Department of Chemistry
COMSATS University Islamabad
Lahore Campus 54000, Pakistan

§Interdisciplinary Research
COMSATS University Islamabad
Wah Campus, GT Road Wah Cantt, Pakistan

¶Department of Mechanical Engineering
COMSATS University Islamabad
Wah Campus, GT Road Wah Cantt, Pakistan

∥Multi-Physical Engineering Sciences Group
Mechanical Engineering Department, School of Science
Engineering and Environment (SEE), Newton Building
University of Salford, Manchester, M54WT, UK

Accepted 2 December 2019
Published 26 February 2020

## ABSTRACT

Nanoparticle hyperthermia treatment is progressing with the passage of time, and with the development in the field of hybrid nanoparticles synthesis. The transient heat transfer in magnetite–graphene nanocomposite in three dimension under conduction is studied during this research. The proposed model is simulated in finite element solver framework. Novel hybrid nanoparticles were synthesized. Their chemical properties and their heat transfer properties were examined. By mathematical modeling results, the effective hybrid nanoparticle is chosen that can be used as a drug in hyperthermia process. Current developments in nanotechnology have improved the ability to precisely modify the features and properties of MNPs for these biomedical applications. The accurate control on the magnetic properties of the particle is the key in hyperthermia applications. By these magnetic particles, wished temperature can be achieved for laser hyperthermia. In this paper, study is done for understanding the properties and novelty of the new nanoparticles. The merits and demerits of synthesized hybrid nanoparticles are also discussed either the composites can used as a drug or not.

Keywords: Nanohyperthermia; Laser thermal therapy; Heating enhancer.

**Corresponding author: Prof. Ayesha Sohail, Department of Mathematics, Comsats University Islamabad, Lahore Campus 54000, Pakistan. E-mail: asohail@ciitlahore.edu.pk**

M. Fatima et al.

INTRODUCTION

Superparamagnetic nanoparticles have been widely used in medical research because of their unusual magnetic properties and biocompatibility. Investigation on superparamagnetic nanoparticles has been deeply accomplished in drug delivery, chemotherapy, hormonal therapy, radiation therapy, hyperthermia therapy,medical imaging and targeting cancer treatment. $^{1-5}$ Cancer is also known as malignancy which is basically the abnormal growth of cells. Cancer is the second leading cause of death world wide and it is responsible for an estimated 9.6 million deaths in 2018. Cancer can be cured by hyperthermia treatment by using superparamagnetic nanoparticles with the aid of external alternating magnetic field, $^{6}$ radiotherapy $^{7}$ and by laser $^{8}$ Cancer thermotherapy is a method of cancer treatment where cancer cells are killed by flaunting the body tissues to high temperatures. Common approaches of cancer treatment such as old-fashioned surgery method, radiation therapy, chemotherapy, tumor thermotherapy has been shown to have some side effects during and after treatment. $^{7}$ That is why thermotherapy has been widely acknowledged. During hyperthermia treatments, the measurement of the actual temperature distribution in the tumor or immediately adjacent tissue is crucially important to the clinical evaluation of the quality of hyperthermia. In this process, the variety of the target tissue temperature have great influences and effectiveness on body. Moreover, in this procedure heat circulates from the target tissue to the surroundings which causes heat injury to normal tissues. Toxicity of hyperthermia in generally is low. The incidence of (reversible) pain at the treated region varies between $0\pm 60\%$. Burns are a typical hyperthermia associated toxicity with low incidence, that are dependent on correct heating techniques. The combination of local or interstitial hyperthermia with radiotherapy resulted in tissue damage that was not significantly greater than that in radiotherapy-sites alone.

Latest innovation of hyperthermia therapy is implication of lasers, which can be used to control the heating effect in body. Lasers have very effective properties which can help for heat cause. Laser can emit light with high intensity and it is extremely directional, self-colored, and coherent. Wavelength range for visible to infrared light is from 400 nm to 900 nm. The penetrability of light in living tissue increases with the wavelength. $^{9}$ When the laser beam reaches tissues, the heat first acts on the surface of the tissues that are open to the irradiation directly and then slowly spreads to the surrounding of tissues. $^{10}$ This allows continuous heating of the tumor area. Moreover, by regulating the output power of infrared laser instrument, the temperature of hyperthermia procedure can easily be controlled. Because of the simple operation, low cost and efficiency, infrared laser is an ideal heat source for tumor hyperthermia. Magnetic nanoparticles have great importance in laser hyperthermia. Laser's heat circulation have different effects with different superparamagnetic nanoparticles. The heating process is completely induced in the magnetic nanoparticles under alternating magnetic field due to Neel relaxation and Brownian relaxation losses. As there is reduced blood flow in tumor area, containing disorganized blood vessels, the heat dissipation to surrounding area is limited. Therefore, cancer cells are more susceptible for apoptosis at relatively mild heating up to $315.15\,\text{K}\,(42^\circ\text{C})$ as compared to healthy cells. Literature shows that a temperature range of $314.95$-$317.15\,\text{K}\,(41.8$-$44^\circ\text{C})$ is most suitable for the entire body hyperthermia. $^{11}$

During this research, we have focused on novel nanoparticles. Due to biocompatibility and strong inherent magnetic properties, $\text{Fe}_3\text{O}_4$ and synthesized nanohybrids were used. $\text{Fe}_3\text{O}_4$ nanoparticles have strong anisotropic dipolar interactions which causes agglomeration and precipitation, due to which their colloidal solubility is lost, and their activity is reduced, making them vulnerable.

Therefore, it is challenging to incorporate $\text{Fe}_3\text{O}_4$ nanoparticles in both *in vitro* and *in vivo* experiments. To prevent their agglomeration and precipitation, we have developed a support of reduced graphene oxide sheets, for making $\text{Fe}_3\text{O}_4$ nanoparticles immobilized. In this work, thermal reduction method has been used for producing graphene and $\text{Fe}_3\text{O}_4$-graphene nanohybrids. Graphene has gained attention for tremendous applications. Large thermal conductivity of graphene ($\kappa\sim5.3\times 10^3\,\text{Wm}^{-1}$),$^{12}$ high flexibility and strength (elastic stiffness $\sim340\,\text{Nm}^{-1}$, Young modulus $\sim1.0\,\text{TPa}$, and breaking strength $\sim42\,\text{Nm}^{-1}$)$^{13,14}$and excellent biocompatibility lead to remarkable properties for the development of prototype devices for biological applications. From all the temperature measurements gained as temperature vs. time and time-averaged temperatures can be calculated at each monitored site.

MATERIALS AND METHOD

Materials

For the synthesis of $\text{Fe}_3\text{O}_4$-graphene nanohybrids, high quality of expandable graphite powder of mean size

2050007-2

$25\ \mu\text{m}$ (purity 99.99%), $\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$ (purity 99%), $\text{FeCl}_2 \cdot 4\text{H}_2\text{O}$ (purity 99.8%), $\text{HCl}$, $\text{KMnO}_4$ (purity 99%), 32% $\text{NH}_3$ solution and high grade $\text{H}_2\text{SO}_4$ and $\text{H}_2\text{O}_2$ (30 wt.) were used. All reactions were carried out using deionized (DI) water. First, Graphene Oxide was synthesized using graphite powder by modified Hummer method.$^{15}$ A total of 5 g graphite powder was added in $125\ \text{mL}\ \text{H}_2\text{SO}_4$ at $0^\circ\text{C}$ by continuous mixing to avoid agglomeration. Once the powder was well dispersed, 15 g $\text{KMnO}_4$ was added to the mixture slowly, keeping the temperature below $15^\circ\text{C}$. Gradually the mixture was brought to room temperature.$^{16}$ Deionized water (150 ml) was added slowly to the mixture to dilute it after which mixture was washed out and dried at room temperature and Grey colored GO powder remained. Magnetite-graphene oxide $\text{F}_x\text{G}_{100x}$ compositions have been synthesized, where $x=(0,25,45,65,75,85,100)$ refers to the weight percentage of magnetite in the nanohybrid. Note that, the composition with $x=0$ specifies pure graphene and $x=100$ specifies pure magnetite. Appropriate amounts of $\text{FeCl}_3 \cdot 6\text{H}_2\text{O}$, $\text{FeCl}_2 \cdot 4\text{H}_2\text{O}$ and graphene oxide (GO) were weighed for each composition. After the procedure, sample were named according to the weight $\%$ ratio in the compositional formula $\text{F}_x\text{G}_{100x}$ ($x=0,25,45,65,75,85,100$) as G, $\text{F}_{25}\text{G}_{75}$, $\text{F}_{45}\text{G}_{55}$, $\text{F}_{65}\text{G}_{35}$, $\text{F}_{75}\text{G}_{25}$, $\text{F}_{85}\text{G}_{15}$ and F, respectively. For example, $\text{F}_{75}\text{G}_{25}$ refers to the hybrid containing 75 wt.% magnetite and 25 wt.% graphene.

## Mathematical Model

In this model, laser beam is used for heat transfer in various substrates. Basically, the laser beam acts as a heat source. For hyperthermia process, laser is used for heat transfer at subjected area to kill cancer cell. A model is proposed where G, $\text{F}_{25}\text{G}_{75}$, $\text{F}_{45}\text{G}_{55}$, $\text{F}_{65}\text{G}_{35}$, $\text{F}_{75}\text{G}_{25}$, $\text{F}_{85}\text{G}_{15}$ and Fe were used as a substrate one by one. Laser beam is moving over a surface to produce the required localized heating. In this case, each layer of substrate is very thin. The localized transient heating was generated by a laser beam, which was moving in a circular path over the substrate. Beam's penetration's depth can be described by an absorption coefficient $k_{\text{abs}}$, which depends on the ambient temperature. From this model, the penetration depth and the temperature distribution is understandable. The substrate is formed as a three-dimensional object with 1 mm thickness and 10 mm-by-10 mm width. It manages the variation of laser intensity with penetration depth using one-dimensional geometry that represents the substrates thickness. The model is formed by transient heat transfer in 3D geometry by conduction. The transient energy transport equation for heat conduction is

$$
\rho C_p \frac{\partial \mathbb{T}}{\partial t}+\nabla \cdot(-\underline{k} \nabla T)=\zeta. \tag{1}
$$

Here $\rho$ is the density with unit $\text{kg/m}^3$, $C_p$ is the specific heat capacity with unit $\text{J/(kg.K)}$, $\underline{k}$ is the thermal conductivity tensor and $\zeta$ is the heat source which is zero over here. The material properties of substrates are derived. The anisotropic conductivity of $\kappa=(k_{xx},k_{yy},k_{zz})$ with unit $\text{W/((m.K))}$. For the model, an assumption of insulated boundaries is made. In 1D geometry, the weak form, subdomain application mode is used to model the laser penetration. The equation which describes the laser penetration is

$$
\frac{\partial \beth}{\partial \hat{x}}=-k_{\mathrm{abs}} \beth. \tag{2}
$$

Here $\beth$ represents the relative laser intensity, $\hat{x}$ represents the 1D coordinate, and $k_{\text{abs}}$ is the absorption coefficient. The absorption coefficient can depend on the temperature which is

$$
k_{\mathrm{abs}}=8 \cdot 10^{3} \mathrm{m}^{-1}-10(\mathrm{m}. \mathrm{K})^{-1}(T-300 \mathrm{K}). \tag{3}
$$

The volumetric heat source term $\zeta$ in the 3D geometry is

$$
\zeta=P_{\text {in }} k_{\text {abs }} \beth, \tag{4}
$$

where $P_{\text{in}}$ is the total power of the incoming laser beam. Both of these equations are included in the weak form, subdomain application mode, where they work as a equation, which is given as

$$
\beth_{\text {test }}\left(\beth_{x}-k_{\text {abs }} \beth\right)+k_{\text {abs }} \beth P_{\text {in }} T_{\text {test }}. \tag{5}
$$

The first part of this expression describes the penetration equation, and the second part comes from the heat-source term in the 3D heat transfer application mode. At the left boundary, homogeneous Neumann condition is applied and at the right boundary the relative intensity $\beth$ is equal to unity. The total incoming laser power $P_{\text{in}}$ is 50 W. The model implements the heat source's motion when we coupled the 3D temperature variable $\mathbb{T}$ to the 1D equation. It does so with a subdomain extrusion coupling variable using a general transformation. A time-dependent transformation expression results in a moving heat source. This case describes a circular repeating motion using the transformation expressions.

$$
x=c \sin (\omega t),
$$

$$
y=c \cos (\omega t),
$$

$$
z=\hat{x},
$$

where $x, y$ and $z$ are the 3D coordinates and $\dot{x}$ represents the 1D coordinate. $c$ is the radius of circular motion, $\omega$ is the angular velocity and $t$ is time. The parameter values used in model are $c = 0.02$ m and $\omega = 10$ rad/s. For the laser motion, the rough time period is [0,1]. The 3D model is formed by using an extruded triangular mesh, which has a fine resolution close to the laser incident line and is coarse elsewhere. This results in a high-resolution solution with minimum computation requirements. From the schematic diagram, we can see the location of laser beam (i.e. the hotspot). Here the laser beam moves from right to left, and the warm side is on the right-hand side of the peak. The temperature reaches at different points according to the substrate. The substrate types which used in model are explained in table (see Table 6). Mathematical model is shown in figure (see Fig. 5).

# RESULTS
Different materials are taken one by one to understand the nanoparticle's heat flux variation and temperature changes. Because heat plays an important role in hyper- perthermia. These model can help us to understand which nanoparticles are more effective in laser hyper- thermia process and which are harmful for human being.

## Iron(Fe) as a Substrate
Ferrous metals have a high carbon content which generally makes them vulnerable to rust when exposed to moisture. They have magnetic properties. Fe has $3.4$ W/mk thermal conductivity, density $5150 \, \text{kg/m}^3$ and heat capacity $\text{C}_p$ $940 \, \text{J/kgK}$. In Fig. 2, variation of time is 0.08 s, 0.48 s, 0.86 s and 1 s which shows that time is the most important parameter in this model. At $t = 0.08$ s, the stream lines show that the heat flux and the temperature varies from 300 K to 500 K. At $t = 0.46$ s, temperature varies from 350 K to 550 K. At $t = 0.86$ s, temperature varies from 400 K to 600 K. At $t = 1$ s, temperature varies from 300 K to 700 K. We have presented these results in Fig. 2.

![](./images/812671380746141697_1.jpg)

Fig. 1 Model.

## $\mathbf{F_{25}G_{75}}$ as a Substrate
In Fig. 3, $\text{F}_{25}\text{G}_{75}$ is used as a drug. By changing the concentration of atoms, heat transfer effect will definitely change. It is understood that changes occur with respect to time. At $t = 0.08$ s, streamlines show the heat flux changes and temperature varies from 300 K to 306 K. At $t = 0.46$ s, temperature varies from 300.034 K to 307 K. At $t = 0.86$ s, temperature varies from 300.311 K to 312 K. At $t = 1$ s, temperature varies from 300.441 K to 310 K.

## $\mathbf{F_{45}G_{55}}$ as a Substrate
In Fig. 4, $\text{F}_{45}\text{G}_{55}$ is used as a substrate. Temperature increases with respect to time as shown in the figure. At $t = 0.08$ s, streamlines shows the heat flux changes and minimum temperature is 299.997 K and maximum temperature is 308.5 K. At $t = 0.46$ s, minimum temperature is 300.008 K and maximum temperature is 309.249 K. At $t = 0.86$ s, minimum temperature is 300.152 K and maximum temperature is 315.874 K. At $t = 1$ s, minimum temperature is 300.254 K and maximum temperature is 313.359 K.

## $\mathbf{F_{65}G_{35}}$ as a Substrate
In Fig. 5, $\text{F}_{65}\text{G}_{35}$ is used as a substrate. Temperature increases with respect to time as shown in the figure. At $t = 0.08$ s, streamlines shows the heat flux changes and minimum temperature is 299.995 K and maximum temperature is 310 K. At $t = 0.46$ s, minimum temperature is 299.997 K and maximum temperature is 312 K. At $t = 0.86$ s, minimum temperature is 300.025 K and maximum temperature is 314 K. At $t = 1$ s, minimum temperature is 300.069 K and maximum temperature is 318.243 K.

2050007-4

![](./images/812671380746141697_2.jpg)

Fig. 2 Heat transfer: When Fe used as a substrate.

## $\mathbf{F_{75}G_{25}}$ as a Substrate

In Fig. 6, $\text{F}_{75}\text{G}_{25}$ is used as a substrate. Temperature increases with respect to time as shown in the figure. At $t = 0.08$ s, streamlines shows the heat flux changes like in the above figures. Minimum temperature is 299.988 K and maximum temperature is 312 K. At $t = 0.46$ s, minimum temperature is 299.996 K and maximum temperature is 315 K. At $t = 0.86$ s, minimum temperature is 300 K and maximum temperature is 318 K. At $t = 1$ s, minimum temperature is 300.008 K and maximum temperature is 320 K.

## $\mathbf{F_{85}G_{15}}$ as a Substrate

In Fig. 7, $\text{F}_{85}\text{G}_{15}$ is used as a substrate. Temperature increases with respect to time as shown in the figure. At $t = 0.08$ s, streamlines shows the heat flux changes and minimum temperature is 299.953 K and maximum temperature is 310 K. At $t = 0.46$ s, minimum temperature is 299.966 K and maximum temperature is 315 K. At $t = 0.86$ s, minimum temperature is 299.979 K and maximum temperature is 320 K. At $t = 1$ s, minimum temperature is 299.989 K and maximum temperature is 325 K.

2050007-5

![](./images/812671380746141697_3.jpg)

Fig. 3 Heat transfer: When $F_{25}G_{75}$ used as a substrate.

## Graphene(G) as a Substrate

In Fig. 8, Graphene is used as a substrate. Temperature increases with respect to time as shown in the figure. At $t=0.08$s, streamlines shows the heat flux changes and minimum temperature is 300.045 K and maximum temperature is 306 K. At $t=0.46$ s, minimum temperature is 302.943 K and maximum temperature is 311.838 K. At $t=0.86$ s, minimum temperature is 306.65 K and maximum temperature is 316 K. At $t=1$s, minimum temperature is 307.93 K and maximum temperature is 318.227 K.

## DISCUSSION

During this research, we have considered special type of nanoparticles. In the recent literature, studies are available, such as the research group led by Frazi et al.,$^{17}$ provided a documented proof, where the significance of nanoparticles (such as magnetite-graphene nanocomposite), for biological applications was verified. In this paper, the physical properties of the particles were incorporated with a mathematical model. Mathematical results verified that Fe can be never used as a drug in laser hyperthermia because maximum

2050007-6

![](./images/812671380746141697_4.jpg)

Fig. 4 Heat transfer: When $\text{F}_{45}\text{G}_{55}$ as a substrate.

temperature which is gained is 700 K, that can burn the whole body easily. However, Fe has magnetic properties, but it exceeds the limitation of heat flux needed in hy- perthermia treatment. In this study, $\text{F}_{25}\text{G}_{75}$ was the second substrate which was observed. From the math- ematical observation, it is shown that $\text{F}_{25}\text{G}_{75}$ can be used as drug in laser hyperthermia. In hyperthermia, body temperature's range is $314.95\,\text{K}$ to $317.15\,\text{K},^{18}$ So $\text{F}_{25}\text{G}_{75}$ is not harmful for human body. It did not cross the limit of heat flux needed in laser hyperthermia which is acceptable. From heat transfer streamlines and the maximum temperature of $\text{F}_{45}\text{G}_{55}$ which is approximately $316\,\text{K}$, it is proven mathematically that it can be the perfect choice of drug in laser hyperthermia to kill cancer cells. This hybrid nanoparticles have no demerits with respect to heat flux, it is not harmful for human body. By exploring the properties of $\text{F}_{65}\text{G}_{35}$, the maximum temperature obtained is $318.243\,\text{K}$. This is very inappropriate for human body because it can burn it due to high temperature. From these results, this hybrid nanoparticle is not suitable for laser hyperther- mia treatment. $\text{F}_{75}\text{G}_{25}$ also created a great amount of heat and gained the maximum temperature which is $320\,\text{K}$. It exceed the limitation of human body for heat transfer. It can burn the human body which is the biggest drawback of this hybrid nanoparticle. It has

![](./images/812671380746141697_5.jpg)

Fig. 5 Heat transfer: When $\mathrm{F}_{65} \mathrm{G}_{35}$ as a substrate.

![](./images/812671380746141697_6.jpg)

Fig. 6 Heat transfer: When $\mathrm{F}_{75} \mathrm{G}_{25}$ as a substrate.

2050007-8

Biomechanics of Superparamagnetic Nanoparticles for Laser Hyperthermia

![](./images/812671380746141697_7.jpg)

Fig. 6 (Continued)

![](./images/812671380746141697_8.jpg)

Fig. 7 Heat transfer: When $F_{85}G_{15}$ as a substrate.

2050007-9

![](./images/812671380746141697_9.jpg)

Fig. 8 Heat transfer: When graphene as a substrate.

<table>
<thead>
<tr>
<th colspan="9">Table 1. Substrates and Their Properties.</th>
</tr>
<tr>
<th>Substrate</th>
<th>G</th>
<th>F₈₅G₁₅</th>
<th>F₇₅G₂₅</th>
<th>F₆₅G₃₅</th>
<th>F₄₅G₅₅</th>
<th>F₂₅G₇₅</th>
<th>Fe</th>
</tr>
</thead>
<tbody>
<tr>
<td>$\kappa$</td>
<td>5300</td>
<td>802.8</td>
<td>1335.8</td>
<td>1868.8</td>
<td>2934.7</td>
<td>4000.6</td>
<td>3.4</td>
</tr>
<tr>
<td>$\rho$</td>
<td>2200</td>
<td>4700</td>
<td>4400</td>
<td>4100</td>
<td>3500</td>
<td>2900</td>
<td>5150</td>
</tr>
<tr>
<td>$C_p$</td>
<td>1960</td>
<td>1093</td>
<td>1195</td>
<td>1297</td>
<td>1501</td>
<td>1705</td>
<td>940</td>
</tr>
</tbody>
</table>

<table>
<thead>
<tr>
<th colspan="6">Table 2. Substrate's Minimum Temperature with Variation in Time.</th>
</tr>
<tr>
<th rowspan="2">Compound</th>
<th>Minimum</th>
<th rowspan="2">$t_o=0.08$</th>
<th rowspan="2">$t_1=0.46$</th>
<th rowspan="2">$t_2=0.86$</th>
<th rowspan="2">$t_3=1$</th>
</tr>
<tr>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Fe</td>
<td>T</td>
<td>300</td>
<td>350</td>
<td>400</td>
<td>300</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>131.58</td>
<td>125</td>
<td>$-714.285$</td>
</tr>
<tr>
<td rowspan="2">F₂₅G₇₅</td>
<td>T</td>
<td>300</td>
<td>302.034</td>
<td>300.311</td>
<td>300.441</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>0.08</td>
<td>0.69</td>
<td>0.92</td>
</tr>
<tr>
<td rowspan="2">F₄₅G₅₅</td>
<td>T</td>
<td>299.997</td>
<td>300.008</td>
<td>300.152</td>
<td>300.254</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>0.0289</td>
<td>0.36</td>
<td>0.72</td>
</tr>
<tr>
<td rowspan="2">F₆₅G₃₅</td>
<td>T</td>
<td>299.995</td>
<td>299.997</td>
<td>300.025</td>
<td>300.069</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>0.0052</td>
<td>0.07</td>
<td>0.314</td>
</tr>
<tr>
<td rowspan="2">F₇₅G₂₅</td>
<td>T</td>
<td>299.988</td>
<td>299.996</td>
<td>300</td>
<td>300.008</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>0.021</td>
<td>0.01</td>
<td>0.057</td>
</tr>
<tr>
<td rowspan="2">F₈₅G₁₅</td>
<td>T</td>
<td>299.953</td>
<td>299.966</td>
<td></td>
<td>299.989</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>0.579</td>
<td>0.0325</td>
<td>0.0714</td>
</tr>
<tr>
<td rowspan="2">G</td>
<td>T</td>
<td>300</td>
<td>300.09</td>
<td>302</td>
<td>300.682</td>
</tr>
<tr>
<td>$T'$</td>
<td>—</td>
<td>$-0.23$</td>
<td>4.775</td>
<td>$-9.414$</td>
</tr>
</tbody>
</table>

been proved mathematically that $F_{85}G_{15}$ gained maximum temperature which is 325 K. This can never be the choice of drug for laser hyperthermia. Similarly, Graphene can never be treated as a drug in laser hyperthermia. It gained 318.227 K, which is harmful for human body. From Tables 2 and 3, all maximum and minimum values of temperature gained with variation of time the magnetic nanohybrid particles are discussed. From these mathematical results, the merits and demerits of synthesized magnetic nanoparticles are discussed.

2050007-10

**Biomechanics of Superparamagnetic Nanoparticles for Laser Hyperthermia**

Table 3. Substrate's Maximum Temperature with Variation in Time.

| Compound |          | Maximum <br>Temperature | $t_o$=0.08 | $t_1$ = 0.46 | $t_2$ = 0.86 | $t_3$ = 1 |
|----------|----------|-------------------------|------------|--------------|--------------|-----------|
| Fe       | T        |                         | 500        | 550          | 600          | 700       |
|          | $T'$     |                         | ---        | 131.57       | 125          | 714.28    |
| $\text{F}_{25}\text{G}_{75}$ | T |                         | 306        | 307          | 312          | 310       |
|          | $T'$     |                         | ---        | 2.63         | 12.5         | $-$14.28  |
| $\text{F}_{45}\text{G}_{55}$ | T |                         | 308.5      | 309.249      | 315.874      | 313.359   |
|          | $T'$     |                         | ---        | 1.971        | 16.56        | $-$17.96  |
| $\text{F}_{65}\text{G}_{35}$ | T |                         | 310        | 312          | 314          | 318.243   |
|          | $T'$     |                         | ---        | 5.26         | 5            | 30.3      |
| $\text{F}_{75}\text{G}_{25}$ | T |                         | 312        | 315          | 318          | 320       |
|          | $T'$     |                         | ---        | 7.89         | 7.5          | 14.28     |
| $\text{F}_{85}\text{G}_{15}$ | T |                         | 310        | 315          | 320          | 325       |
|          | $T'$     |                         | ---        | 13.15        | 12.5         | 35.7      |
| G        | T        |                         | 304.5      | 305          | 308          | 308.667   |
|          | $T'$     |                         | ---        | 1.32         | 7.5          | 4.76      |

## CONCLUSION

The expansion of MNPs has been significantly enhanced in the past decade by advances in nanotechnology, molecular cell biology, imaging instruments and cancer treatment. Nanoparticles of various shapes have strong photothermal effects. Plethora of preparation of magnetic nanoparticles have been established to identify and treat diseases such as tumor treatment by laser-induced hyperthermia. The synthesized hybrid nano particles have very compatible properties for this therapy. In this work, it is observed that different results are obtained, by changing the ratio of particles. This study can be used in tumor therapy. Some hybrid nanoparticles have great qualities with respect to heat transfer which can show that those particles can be easily used in laser hyperthermia treatment. However, some hybrid nanoparticles were harmful for human body. Hence, those particles are not good choice of drug for laser hyperthermia. With respect to stages of tumor cells, magnetic nanohybrid particle can be choose as drug. The photothermal effect of magnetite–graphene nanocomposite may be well utilized as an efficient strategy in clinical cancer therapies.

## ACKNOWLEDGMENT

The authors would like to acknowledge the funding received from PSF-HIT-TERP Cell (DESCOM).

## REFERENCES

1. Sudhakar, A, History of cancer, ancient and modern treatment methods, *J Cancer Sci Ther*, 1:1, 2009.

2. Zhang L, Xue H, Gao C, Carr L, Wang J, Chu B, Jiang S, Imaging and cell targeting characteristics of magnetic nanoparticles modified by a functionalizable zwitterionic polymer with adhesive 3, 4-dihydroxyphenyl-l-alanine linkages, *Biomaterials* **31**:6582, 2010.

3. Laurent S, Mahmoudi M, Superparamagnetic iron oxide nanoparticles, promises for diagnosis and treatment of cancer, *Int J Mol Epidemiol Genet* **2**:367, 2011.

4. Lee JH, Jang JT, Choi JS, Moon SH, Noh SH, Kim JW, Kim JG, Kim IS, Park KI, Cheon J, Exchange-coupled magnetic nanoparticles for efficient heat induction, *Nat Nanotechnol Nat Nanotechnol* **6**:418, 2011.

5. Yang HW, Hua MY, Liu HL, Huang CY, Tsai RY, Lu YJ, Chen JY, Tang HJ, Hsien HY, Chang YS, Yen TC, Self-protecting core-shell magnetic nanoparticles for targeted, traceable, long half-life delivery of BCNU to gliomas, *Biomaterials* **32**:6523, 2011.

6. Rosensweig RE, Heating magnetic fluid with alternating magnetic field, *J Magn Magn Mater* **252**:370, 2002.

7. Moroz P, Jones SK, Gray BN, Status of hyperthermia in the treatment of advanced liver cancer, *J Surg Oncol* **77**:259, 2001.

8. Chu M, Shao Y, Peng J, Dai X, Li H, Wu Q, Shi D, Near-infrared laser light mediated cancer therapy by photothermal effect of $\text{Fe}_3\text{O}_4$ magnetic nanoparticles, *Biomaterials* **34**:4078, 2013.

9. Wei HJ, Xing D, Wu GY, Jin Y, Gu HM, Optical properties of human normal small intestine tissue determined by Kubelka-Munk method *in vitro*, *World J Gastroenterol* **9**:2068, 2003.

10. Steger AC, Lees WR, Walmsley K, Bown SG, Interstitial laser hyperthermia: A new approach to local destruction of tumours, *BMJ* **299**:362, 1989.

11. Glcl G, Hergt R, Zeisberger M, Dutz S, Nagel S, Weitschies W, The effect of field parameters, nanoparticle properties and immobilization on the specific heating power in magnetic particle hyperthermia, *J Phys Condens Matter* **18**:S2935, 2006.

12. Balandin AA, Ghosh S, Bao W, Calizo I, Teweldebrhan D, Miao F, Lau CN, Superior thermal conductivity of single-layer graphene, *Nano Lett* **8**:902, 2008.

13. Neto AC, Guinea F, Peres NM, Novoselov KS, Geim AK, The electronic properties of graphene *Rev Mod Phys* **81**:109, 2009.

14. Wan W, Zhao Z, Hu H, Gogotsi Y, Qiu J, Highly controllable and green reduction of graphene oxide to flexible graphene film with high strength, *Mater Res Bull* **48**:4797, 2013.

15. Yao Y, Miao S, Liu S, Ma LP, Sun H, Wang S, Synthesis, characterization, and adsorption properties of magnetic $\text{Fe}_3\text{O}_4$ @ graphene nanocomposite, *Chem Eng Trans* **184**:326, 2012.

16. Marcano DC, Kosynkin DV, Berlin JM, Sinitskii A, Sun Z, Slesarev A, Alemany LB, Lu W, Tour JM, Improved synthesis of graphene oxide, *ACS Nano* **4**:4806, 2010.

17. Farazi R, Vaezi MR Molaei, Saeidifar MJ, Behnam-Ghader M, Effect of pH and temperature on doxorubicin hydrochloride release from magnetite/graphene oxide nanocomposites. *Mater Today*, *Proc* **5(7)**:15726, 2018.

18. Thiesen B, Jordan A, Clinical applications of magnetic nanoparticles for hyperthermia, *Int J Hyperthermia* **24**:467, 2008.

2050007-11