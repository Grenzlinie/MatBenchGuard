This article was downloaded by: [University of Kent]
On: 30 November 2014, At: 09:28
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House,
37-41 Mortimer Street, London W1T 3JH, UK

![](./images/811645823480758274_1.jpg)

# Molecular Simulation
Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/gmos20

## Wetting characteristics of nanoscale water droplet on silicon substrates with effects of surface morphology
Tsu-Hsu Yen $^{a}$

$^{a}$ Department of Electrical Engineering, Chinese Naval Academy, Kaohsiung, 81300, Taiwan, ROC
Published online: 04 Jul 2011.

To cite this article: Tsu-Hsu Yen (2011) Wetting characteristics of nanoscale water droplet on silicon substrates with effects of surface morphology, Molecular Simulation, 37:9, 766-778

To link to this article: http://dx.doi.org/10.1080/08927022.2010.547855

PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the "Content") contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# Wetting characteristics of nanoscale water droplet on silicon substrates with effects of surface morphology

Tsu-Hsu Yen*

Department of Electrical Engineering, Chinese Naval Academy, Kaohsiung 81300, Taiwan, ROC

(Received 11 September 2010; final version received 30 November 2010)

The objective of the present study is to explore the wettability of a nanoscale water droplet on silicon (Si) substrates of various surface morphologies by using molecular dynamics simulation. Three diamond lattice planes, i.e. Si(111), Si(100) and Si(110), of the Si substrates with microstructures of square column arrays of various heights and spacing are considered in this study. The wettability of water droplet on such substrates is characterised by contact angle. The distributions of water density and average hydrogen bond number are visualised with the simulation results. In addition, the volume of vapour trapped in the cavities of the surface microstructure is explored. The present results disclose interesting physics about the influences of wall lattice and surface microstructure.

**Keywords:** word; molecular dynamics simulation; wetting; contact angle; nanoscale droplet

## Nomenclature

| | | | |
|----|----|----|----|
| $A_p$ | cavity amplitude of microstructure | $\sigma$ | reference L-J diameter, $\sigma = \sigma_{\text{ff}} = 0.3169$ nm |
| $e$ | unit of electric charge, $e = 4.803 \times 10^{-10}$ electrostatic unit | $\rho$ | number density of fluid (water) |
| $\text{err}$ | error | $\rho_{\text{HB}}$ | density of hydrogen bond (water) |
| $g(r)$ | radial distribution function | $\tau$ | molecular time scale, $\tau = (m\sigma^2/\varepsilon)^{1/2}$ |
| $k_{\text{B}}$ | Boltzmann constant | $\lambda$ | period of microstructure |
| $m$ | weight of water molecular, $m = 18$ g/mol | $\lambda/r_{\text{B}}$ | dimensionless period of microstructure |
| $N$ | number of particle | $\theta$ | contact angle |
| $n_{\text{HB}}$ | average number of hydrogen bond per water molecule | $\theta_{\text{Y}}$ | contact angle calculated from Young's equation |
| $q$ | charge | $\gamma_{\text{s}}$ | surface energy of solid |
| $R$ | the distance between the atoms belonging to different water molecules to determine hydrogen bond formed | $\gamma_{\text{l}}$ | surface energy of liquid |
| $r$ | distance between two particles $[\sigma]$ or radial direction | $\gamma_{\text{sv}}, \gamma_{\text{sl}}, \gamma_{\text{lv}}$ | the interfacial tensions of solid–vapour, solid–liquid and liquid–vapour |
| $r_{\text{B}}$ | base radius $[\sigma]$ of droplet | $\phi$ | hydrogen bond angle |
| $r, z$ | coordinates $[\sigma]$ | | |
| $u$ | potential | | |
| $T$ | temperature [K] | | |
| $V$ | volume $[\sigma^3]$ | | |
| $x, y, z$ | coordinates $[\sigma]$ | | |

### Greek symbols

| | |
|----|----|
| $\delta$ | depletion layer width between the wall surface and the water |
| $\varepsilon$ | the reference energy parameter |

### Subscripts

| | |
|----|----|
| $c$ | cut-off distance |
| $f$ | fluid |
| $\text{HB}$ | hydrogen bond |
| $\text{wf}$ | between wall and fluid molecules |
| $\text{CO}$ | between carbon and oxygen molecules |
| $\text{OO}$ | between oxygen and oxygen molecules |
| $\text{OH}$ | between oxygen and hydrogen molecules |
| $\text{cav}$ | inside the cavity |

### Superscripts

| | |
|----|----|
| $c$ | critical value |

*Email: g960403@gmail.com

ISSN 0892-7022 print/ISSN 1029-0435 online
© 2011 Taylor & Francis
DOI: 10.1080/08927022.2010.547855
http://www.informaworld.com

## 1. Introduction
Wetting is an interfacial phenomenon describing the condition of how liquid behaves as it comes in contact with a solid surface. Understanding the nanoscale wetting phenomena is useful in many areas, e.g. microfluidic devices [1,2], bio-nano-electro-mechanical-systems [3] and membrane channels [4]. Wettability of a surface can be influenced by a number of factors such as the properties of and the interactions between liquid and solid, surface roughness, pressure and temperature. Among them, the surface roughness is the most noteworthy in the analysis of the surface wettability characteristics. Surface roughness can be artificially fabricated, formed by surface absorption of macromolecule, or of molecular level with surface atomistic layout. The surface elements could be of length scales from the order of angstroms to microns [5]. Bocquet and Barrat [6] reviewed the slippage of flow past solid at different length scales. As to the roughness of molecular scale, the study of crystal plane effects on nanofluidics in our recent work [7] is a most typical example. The topographical surface may substantially change the wettability such as hydrophobicity and hydrophilicity. Extrand et al. [8] studied the superwetting of structured surfaces both experimentally and theoretically. Voronov et al. [9] reviewed the characteristics of hydrophobicity and its relationship with the slip length. Krupenkin et al. [10] demonstrated a dynamic electrical control of wetting behaviour on nanostructured sufaces. McHale et al. [11] studied the superwetting droplets on surfaces having lithographically produced pillars. For electroosmotic flow, a molecular dynamics study [12] demonstrated that the molecular-scaled periodic roughness influences electric double layer remarkably.

Numerous molecular dynamics simulations (MDS) have been performed on the subject of wettability or contact angle at solid-water interface. Bocquet and Barrat [13] demonstrated that the boundary condition drastically changes when the contact angle is large enough. Voronov et al. [14] provided the correlation of the contact angle with the slip length. They found that the slip length is functionally dependent of the wall-fluid interaction energy, $\varepsilon_{\mathrm{wf}}$, and wall-fluid interaction length, $\sigma_{\mathrm{wf}}$. Werder et al. employed MDS to explore the contact angles of water droplet confined inside a carbon nanotube [15] and on graphite surface and determined the solid-liquid interaction energy scale $(\varepsilon_{\mathrm{CO}})$ and length scale $(\sigma_{\mathrm{CO}})$ [16]. Lundgren et al. [17] investigated the wettability of water droplets at pillar surfaces of various heights of pillars. They found that the surface orientation of graphite has significant effects on wetting properties of the top and side surfaces of the pillars and in turn influences the contact angle at the pillar surfaces. Yang et al. [18,19] adopted hydrocarbons' polymer structure to examine the contact angle on superhydrophobic surfaces. Their results revealed that the contact angle is significantly influenced by the root-mean-square roughness surface amplitude but almost irrelevant to the period of the roughness elements. Servantie and Müller [20] studied the rolling and sliding motion of droplets on roughened substrate. By using MD simulation, Huang et al. [21] investigated the slippage of water at various hydrophobic surfaces. They proposed a quasi-universal relationship between contact angle and slip length. Chai et al. [22] studied the wetting of water on an amorphous silica surface.

Two models, Wenzel and Cassie, are used to explain the increase in contact angle with the presence of the surface microstructure. In the Wenzel model, the microstructure is regarded as a mechanism for increasing liquid-solid interface area and thus the effective free energy, which raises the contact angle. On the other hand, Cassie model attributes the increase in contact angle to the gas trapped in the cavities of surface microstructure at the solid-liquid interface. Quéré [23,24] reviewed the effects of surface roughness on the wettability, especially the apparent contact angle and the contact angle hysteresis. Dorrer and Rühe [25] discussed the transition from Wenzel state to Cassie state through condensation.

In the above brief introduction of the background, we can find that there are numerous interesting issues in this area which are worthwhile for further investigation. Water is the most common liquid in nature and is the most important fluid in scientific and engineering applications [26]. Furthermore, silicon (Si) is a very important material in micro/nano fabrications. In this study, we take water droplet on silicon surface as the model to investigate the influences of surface morphology on contact angle at various conditions. The effects of surface lattice and the artificial roughness elements are both studied.

First of all, simulations are performed for contact angle under various conditions of surface orientation and wall-fluid interaction energy without artificial microstructure. Then, the effects of the wall-fluid interaction energy and the surface morphology on contact angle and hydrogen bond distribution are studied. In addition, the vapour trapped inside the cavity of interface is estimated to manifest the mechanisms of variation in contact angle.

## 2. Methodology
### 2.1 Molecular dynamics simulation
The model system consists of water molecules and solid atoms. The solid boundary lies at xy-plane, where periodic boundary conditions are posed in both x- and y-directions. The TIP4P model [27] is employed for simulation of water molecules. Considering the dipole moment effect, cut-off distance of $r_{\mathrm{c}}=4.5\sigma$ is adopted in the simulations. The model is based on four interaction sites located at one plane, sites M and O are associated with oxygen atom, and the other two represent H atoms. The LJ potential in the

![](./images/811645823480758274_2.jpg)

Figure 1. (a) Droplet profiles in terms of density contours fitted by circular form at $\rho\sigma^{3}=0.35-0.45, 0.45-0.65, 0.65-0.75$ and $0.75-$ 0.85. (The parameters of simulation case chosen as surface orientation Si(100), particle number 5008) and (b) A typical projection of the droplet for verification of its circular approximation.

form of $u(r)=4\varepsilon[(\sigma/r)^{12}-(\sigma/r)^{6}]$ is taken to measure interaction forces between two O atoms and between O and solid atoms. The negative charge of water molecule shifts to M site. The Coulomb potential is applied to evaluate the interaction between charges. The parameter $r$ is the separation distance of the interacting molecules and atoms, $\varepsilon$ is an energy scale characterising the strength of the interaction and $\sigma$ denotes a molecular length scale. The geometric parameters of TIP4P model are $r_{OH}=0.975$ Å, $r_{OM}=0.15$ Å and $\angle HOH=104.5^{\circ}$. The TIP4P potential has the form of

$$
u_{ij}=\sum_{\mu \in i} \sum_{v \in j}\left(q_{\mu} q_{v} e^{2} / r_{i \mu, j v}+A_{\mu v} / r_{i \mu, j v}^{12}-C_{\mu v} / r_{i \mu, j v}^{6}\right),
$$

where $q_{\mathrm{H}}=0.52 \mathrm{e}, q_{O}=0, q_{\mathrm{M}}=-2 q_{\mathrm{H}} ; A_{\mu v}=4 \sigma^{12} \varepsilon$, $c_{\mu v}=4 \sigma^{6} \varepsilon$. In this study, the conventional units in molecular dynamics, i.e. $\sigma$ for length, $\varepsilon$ for energy and $\tau=(m\sigma^{2}/\varepsilon)^{1/2}$ for time, and thus $\varepsilon/k_{\mathrm{B}}T$ for temperature, are used. For water, $e=4.803 \times 10^{-10}$ esu, electrostatic unit, $\sigma \equiv \sigma_{\mathrm{OO}}=3.154$ Å, $\varepsilon=0.155 \mathrm{kcal} / \mathrm{mol}$ and $\tau=$ $1.66 \times 10^{-12}$ s. Hereafter, the physical properties are presented based on the reduced units.

Newton's equations of particle motion are solved by using predictor-corrector algorithm with time step $5 \times 10^{-4}\tau$. Initially, the water molecules are stacked regularly as a cuboid on the wall. The system temperature is set as 150 K and unchanged until 5000 time steps. The temperature is raised up to 300 K at 10,000th time step and then kept at 300 K. The Nosé-Hoover thermostat is employed for temperature control of the water molecules.

Data sampling is carried out in the period of $300-$ $550\tau$, which corresponds to 0.5-0.9 ns. To obtain statistically meaningful results, the computational domain is divided into a number of bins that are the square rings with cross-sectional area of $0.2\sigma \times 0.2\sigma$. The statistical means of the computational results are taken as the properties at the centre of these concentric rings. Since the inner rings are too small to obtain sufficient statistical information, in the present calculations of the contact angle, the area in the inner region of $r \leq 2\sigma$ is not taken into account. In addition, to avoid the water molecules drifting out of the computational domain, in the region $z>40\sigma$, a downward force was applied to suppress the molecules of potential to escape.

There are three criteria to decide if a hydrogen bond is formed between two water molecules [28]: (a) The distance $R_{\mathrm{OO}}$ between the oxygen atoms of two molecules is smaller than $R_{\mathrm{OO}}^{\mathrm{c}}$; (b) The distance $R_{\mathrm{OH}}$ between the hydrogen atom of the donor molecule and the oxygen atom of the acceptor is less than $R_{\mathrm{OH}}^{\mathrm{c}}$; (c) The bond angle $\phi$ between the $\mathrm{O-O}$ direction and the molecular $\mathrm{O-H}$ direction of the donor has to be less than a critical value $\phi^{\mathrm{c}}$, where H is the hydrogen which forms the bonds. The values of the critical parameters are $R_{\mathrm{OO}}^{\mathrm{c}}=3.6$ Å, $R_{\mathrm{OH}}^{\mathrm{c}}=$ $2.4$ Å and $\phi^{\mathrm{c}}=30^{\circ}$.

Figure 1(a) shows the calculations of contact angle on substrate Si(100). The value of contact angle is the angle between the solid surface base line and the tangent to the droplet profile on substrate, where the base line is defined as the position of $0.5\sigma$ above the most upper level of solid atoms, and the circular form is fitted by particular density profile. An inspection of the density contours indicates that the contour shapes and contact angles are not significantly changed for a liquid density range of 0.35-0.85. The density data within 0.45-0.65 are employed to calculate the contact angle in this study.

In general, the shape of a droplet is approximated as a part of sphere. The droplet lies on the $x-y$-plane. However, in the case of long-period microstructure, there may be an anisotropic effect in radial direction on $xy$-plane. To avoid the anisotropy, we use the snapshot distribution of

fluid particle number per unit area $\Delta x\Delta y$ with $\Delta x = \Delta y = 1.5\sigma$ and a time step of 0.5 ns. The contours of dimensionless number of water molecule, $N_f^* = N_f/N_{f,\text{max}}$, are used to measure the isotropy degree. The axis is the distance from the centre of the circle to the contour $N_f^* = 0.3-0.35$; and the centre of the circle is defined as the mass centre of droplet on $xy$-plane. The profile of the droplet is approximately regarded as a sphere when the radius error is less than a critical value: $\text{err}_\text{r} \leq \text{err}_\text{r}^\text{c}$, where the radius error, $\text{err}_\text{r}$, is set as: $(r_{\text{max}} - r_{\text{min}})/r_{\text{B}}$ and the critical value, $\text{err}_\text{r}^\text{c}$, is set as 0.34. The value of 0.34 comes from $(\sqrt{2}r_{\text{min}} - r_{\text{min}})/[(r_{\text{min}} + \sqrt{2}r_{\text{min}})/2]$, in which $r_{\text{B}} \approx (r_{\text{min}} + r_{\text{max}})/2$ and the critical value for minimum and maximum radius is set as: $\sqrt{2}r_{\text{min}}^\text{c} \approx r_{\text{max}}^\text{c}$. Figure 1(b) shows a typical projection of droplet geometry onto $xy$-plane for examining the deviation of the shape from a sphere. The anisotropic results limit the investigation for long microstructure period effects. In this study, it is found that the anisotropy of the droplet geometry in $xy$-plane appears at conditions such as longer period of microstructure, smaller fluid number and higher number density for every single solid level and stronger wall–fluid interaction energy.

### 2.2 Solid surface models
The wall lattice structures of Si(111), Si(100) and Si(110) are employed as models in the present MD simulations. From a microscopic point of view, these surfaces have roughness of atomic level. In addition, we also consider surface microstructures formed with array of square-column blocks. Using Si(111) as an illustrative example, Figure 2(a) defines the period $(\lambda)$ and amplitude $(A_p)$ of the block array, Figure 2(b) shows substrates of Si(111) with periodic square column array of amplitude $A_p = 3\sigma$ and periods (wavelengths) $\lambda = 2\sigma, 4\sigma, 8\sigma$ and $12\sigma$. To retain isotropic nature of the microstructures, the periods in both $x$- and $y$-directions are the same.

![](./images/811645823480758274_3.jpg)

Figure 2. Schematic diagram of surface morphology with Si(111). (a) Definitions of period, $\lambda$, and amplitude, $A_p$, of the surface microstructure and (b) substrate of lattice Si(111) with periodic microstructure of $A_p = 3\sigma$ and $\lambda = 2\sigma, 4\sigma, 8\sigma$ and $12\sigma$.

## 3. Results and discussion
The simulation code was verified by examining the radial distribution function, $g(r)$ of pure water and the reproducibility. Figure 3(a) shows the $g(r)$ of the present study, which is consistent with the ice-like structure correlations known to occur in liquid water. Based on the similar procedures of previous study by Werder et al. [16], we performed a simulation of water droplet on graphite by applying a carbon–oxygen Lennard-Jones potential with the parameters $\sigma_{\text{co}}/\sigma = 1.012$ and $\varepsilon_{\text{CO}}/\varepsilon = 0.6773$. The results of density profiles and hydrogen bond distributions for water droplet on graphite are shown in Figure 3(b) and (c). The insets are results of the previous study [16]. The present density contours show that the profiles are very close to the previous ones and the prediction of contact angle $86.7^\circ$ is very close to the previous result $86^\circ$. The average value of the present hydrogen bond distribution shown in Figure 3(d) is about 3.5, which is smaller than the previous MD prediction 3.7 [16], and measurement 3.9 [29], but lies within the reasonable range. The inset is the hydrogen bond number and density profile at the solid–liquid interface. These comparisons validate the adequacy of the present methodology.

### 3.1 Predictions of water droplet on silicon surface without microstructure
The interaction energy parameter $\varepsilon_{\text{wf}}/\varepsilon = 2.0$, which was used in the previous study by Qiao and Aluru [30], is adopted in the major part of the simulations; while other values such as $\varepsilon_{\text{wf}}/\varepsilon = 1.6$ are also taken for comparison. Surface orientations Si(111), Si(100) and Si(110) are studied. Molecular dynamics predictions depicted in Figure 4 show the variations of contact angle $\theta$ with base radius $r_{\text{B}}\sigma^{-1}$ of the droplet. In some simulation cases, the contact angle $\theta$ reduces with the increase in size of the droplet.

![](./images/811645823480758274_4.jpg)

![](./images/811645823480758274_5.jpg)

![](./images/811645823480758274_6.jpg)

![](./images/811645823480758274_7.jpg)

Figure 3. Verification of the present simulations with (a) radial distribution function of pure water; (b) density profiles; (c) hydrogen bond distributions for water droplet on graphite and (d) hydrogen bond distribution along z. The insets in 3(b) and 3(c) are the results of Werder et al. [16] and the inset in 3(d) is the close-up view of density and hydrogen bond number near the solid-water interface.

Wettability is usually characterised by Young's equation: $\cos \theta_{\mathrm{Y}}=(\gamma_{\mathrm{sv}}-\gamma_{\mathrm{sl}})/\gamma_{\mathrm{lv}}$, where $\theta_{\mathrm{Y}}$ is the contact angle obtained from Young's equation, and $\gamma_{\mathrm{sv}}$, $\gamma_{\mathrm{sl}}$ and $\gamma_{\mathrm{lv}}$ are the solid-vapour, solid-liquid and liquid-vapour interfacial tensions, respectively. However, the contact angle may be influenced by drop sizes at microscales and nanoscales. A modified Young's equation which considers the effect of contact line tension (CLT) is provided as: $\cos \theta=\cos \theta_{\mathrm{Y}}-\mathrm{CLT}/r_{\mathrm{B}} \gamma_{\mathrm{lv}}$ [31]. Figure 4 shows that the slope of the contact angle variation depends not only on the size of the droplet, but also on the contact angle itself. Marmur [32] proposed an analytic expression of contact angle and CLT, i.e. $\mathrm{CLT} \approx 4 \sigma_{\mathrm{wf}} \sqrt{\gamma_{\mathrm{s}} \gamma_{\mathrm{l}} \cot \theta}$, where $\sigma_{\mathrm{wf}}$ is the distance between a pair of a solid and a liquid molecule, $\gamma_{\mathrm{s}}$ and $\gamma_{\mathrm{l}}$ represent surface energies of solid and liquid, respectively. It is noted that the slope of contact angle variation is proportional to $\sqrt{\cot \theta}$. The droplet size effects gradually vanish when the contact angle is close to 90 degree in present simulation cases.

Both for $\varepsilon_{\mathrm{wf}}/\varepsilon=2.0$ and $\varepsilon_{\mathrm{wf}}/\varepsilon=1.6$, the level of hydrophobicity and the peak of the first epitaxial layer (as the inset in Figure 4 shows) are both in the order of $\mathrm{Si}(111)>\mathrm{Si}(110)>\mathrm{Si}(100)$. Because the epitaxial ordering is induced near the wall by wall-fluid interaction [9,33], it is implied that the epitaxial layer is closely related to the wettability. The atomic roughness is demonstrated depending on the number density of wall atoms at interface [7]. The peak value in the first epitaxial layer increases with decreased surface atomic roughness. Furthermore, reduction in $\varepsilon_{\mathrm{wf}}/\varepsilon$ or degradation of wall-fluid interaction enhances hydrophobicity of the surface. It is also noted that, among the three different lattice structures, the lattice $\mathrm{Si}(111)$ leads to a largest increment of contact angle with a reduction in interaction energy $\varepsilon_{\mathrm{wf}}/\varepsilon$.

Figure 5 shows the density profile and average hydrogen bond number adjacent to the silicon-water interface for three surface orientations and different interaction energy without surface microstructure. The results of $\mathrm{Si}(111)$ have the most noticeable layering phenomenon among the three surface orientations. Previous studies [9,34] have concluded that both higher slip length and hydrophobicity occurred with higher depletion length at nanoscales. The width of depletion layer, $\delta$, is defined as the distance between the position of the first solid layer and the location where the water density is half of its bulk value. They also concluded that the inverse square of the depletion width, $\delta$ has a linear dependence of $\cos \theta$. In Figure 5, however, we have almost consistent depletion layer width, $\delta \approx 0.22$ nm, at various contact angles. As shown in the inset of Figure 4, the contact angle is not only affected by the depletion

![](./images/811645823480758274_8.jpg)

<table>
  <thead>
    <tr>
      <th colspan="2">Surface orientations</th>
      <th>$\varepsilon_{wf}/\varepsilon$</th>
      <th>$N_f$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Si(111)</td>
      <td>$\bigcirc$</td>
      <td>1.6</td>
      <td>2896, 3536, 4240, 5008</td>
    </tr>
    <tr>
      <td>Si(100)</td>
      <td>$\square$</td>
      <td>1.6</td>
      <td>2896, 3536, 4240</td>
    </tr>
    <tr>
      <td>Si(110)</td>
      <td>$\bigtriangleup$</td>
      <td>1.6</td>
      <td>2896, 3536, 4240</td>
    </tr>
    <tr>
      <td>Si(111)</td>
      <td>$\bullet$</td>
      <td>2.0</td>
      <td>3536, 4240, 5008</td>
    </tr>
    <tr>
      <td>Si(100)</td>
      <td>$\blacksquare$</td>
      <td>2.0</td>
      <td>2896, 4240, 5008</td>
    </tr>
    <tr>
      <td>Si(110)</td>
      <td>$\blacktriangle$</td>
      <td>2.0</td>
      <td>2896, 3536, 4240</td>
    </tr>
  </tbody>
</table>

Figure 4. Contact angle as function of base radius of droplet at various conditions of surface orientation and solid-water interaction energy.

width, but also influenced by the layering density of fluid. Three different surface orientations, Si(111), Si(100) and Si(110), have nearly the same depletion width, therefore, the higher layering effect on smoother atomic surface has higher probability of solid-fluid momentum exchange and this, in turn, enhances the hydrophilicity. In this situation, although the smoother surface may be of larger slip length and more obvious layering phenomena as concluded in the previous studies [7,34], the level of hydrophobicity has a reverse relation with surface atomic roughness. Voronov et al. [14] investigated the relation between the contact angle and the surface roughness with various wall-fluid interaction length, $\sigma_{wf}$, but with the solid atomic arrangement unchanged. On the contrary, the present study changes the solid atomic arrangements on each layer, but keeps the value of $\sigma_{wf}$ fixed. Both studies showed the similar trend that the smoother surface leads to more remarkable epitaxial layering phenomenon near the solid-fluid region and thus decreases the contact angle.

Since the hydrogen bond is weaker than the ionic bond but stronger than van der Waals interaction, a change in wall-fluid interaction energy ($\varepsilon_{wf}/\varepsilon=1.6$ and 2.0) has only minor influences on the density layering and the hydrogen bond distribution. However, it is interesting to note that the layering or fluctuating profiles of the number density of water molecules, $\rho\sigma^{3}$, and the hydrogen bond, $n_{HB}$, have a phase difference. The presence of the fluid layering phenomena decreases the hydrogen bonds, because it limits both translational and rotational move- ment of water molecule. Therefore, the density layering and the number of hydrogen bond both have influences on the wettability characteristics at the wall-fluid interface.

### 3.2 Effects of microstructure on wettability
Figure 6 shows snapshots of a water droplet on silicon substrate (a) without and (b) with the microstructure of artificial roughness array. From the resultant droplet profiles, the change in wettability due to the presence of the microstructure can be observed. Microstructures with various amplitudes and periods on three surface lattices are considered to explore the contact angles of water droplet on a silicon substrate of various surface morphologies. The details of the cases studied are summarised in Table 1.

![](./images/811645823480758274_9.jpg)

Figure 5. Number density profile and average hydrogen bond in the near wall region of the silicon-water interface without surface microstructure.

![](./images/811645823480758274_10.jpg)

Figure 6. Snapshot of a water droplet on silicon surfaces (a) without artificial roughness and (b) with microstructure of artificial roughness array of $A_{p}=3 \sigma$ and $\lambda=6 \sigma$. The parameters are the number of water molecule $N_{f}=5008$, wall-fluid interaction energy $\varepsilon_{\mathrm{wf}} / \varepsilon=2.0$ for both cases.

To examine whether the gas is trapped in the cavities formed in the artificial surface microstructures, a coarse average fluid number density under the base line of the wall-fluid interface is defined, i.e. $\rho_{\mathrm{cav}} \sigma^{3}=\left\langle N_{f, \mathrm{cav}}\right\rangle /$ $V_{\text {cav }} \sigma^{-3}$, where $\left\langle N_{f, \text { cav }}\right\rangle$ is the ensemble average of fluid number inside the cavity and $V_{\text {cav }} \sigma^{-3}$ is the dimensionless volume of the cavity. Since the solid wall is composed of soft molecules, the exact location of the wall-fluid interface is not clearly defined and in turn the volume of the cavity is hard to calculate precisely. Herein, the cavity volume is estimated as a half of the volume between the baseline and the topmost level of cavity bottom.

### 3.2.1 Droplet shape and distributions of water density and hydrogen bond

Figure 7 shows the contours of water number density and the corresponding distribution of average number of hydrogen bonds per water molecule on Si(111) surface with $\varepsilon_{\mathrm{wf}} / \varepsilon=2.0$, the surface microstructures of amplitude $3 \sigma$ and periods 2,8 , and $12 \sigma$. The smooth surface is employed as a basis for comparison. With the shorter period, the water density in cavity is obviously lower. When the period approaches the base radius of the solid-liquid interface area, it possesses more hydrogen bonds per water molecule. In the Cassie model, the cavity is assumed to have little liquid in it, while in the Wenzel model, the cavity is assumed to be of sufficiently high liquid density. Here, in this analysis, we use the liquid density $\rho_{\mathrm{cav}} \sigma^{3}=0.2$ in the cavity as a rough criterion for the identification of the Cassie $(\rho_{\mathrm{cav}} \sigma^{3}<0.2)$ and the Wenzel model $(\rho_{\mathrm{cav}} \sigma^{3}>0.2)$. It can be inferred that, in the case of shorter period $(2 \sigma)$, the surface roughness effect is more likely the proposition of the Cassie model, but in the case of a longer period, the Wenzel model is more appropriate. In Figure 8, the results for droplets on the smooth Si(100) surface at the similar conditions of amplitude $3.5 \sigma$ and periods of $2 \sigma, 8 \sigma$ and $12 \sigma$ are presented. On Si(100) without microstructure, the droplet has a higher contact angle than that on Si(111). Both contact angles increase in the presence of microstructures.

### 3.2.2 Contact angle and water molecule trapped in cavities

Figures 9-11 for the results of Si(111), Si(100) and Si(110) surfaces, respectively, show the variations of contact angle $\theta$ and water trapped in cavities, $\rho_{\mathrm{cav}} \sigma^{3}$, at various conditions of number of water molecules, period of microstructure $(\lambda / r_{\mathrm{B}})$ and amplitude of cavity $(A_{p} \sigma^{-1})$. The parameter $\rho_{\mathrm{cav}} \sigma^{3}$ denotes the number density of water trapped in cavities between the droplet and the column array of the surface microstructure. Figure 9 shows that the contact angle $\theta$ of a water droplet on Si(111) wall with $\varepsilon_{\mathrm{wf}} / \varepsilon=2$ is about $63^{\circ}-70^{\circ}$ for a smooth surface with $\lambda / r_{\mathrm{B}}=0$. At $\lambda / r_{\mathrm{B}}=0.2$, the contact angle reaches a maximum and the water trapped in the cavities is of small

Table 1. Model parameters of the simulations.

<table>
<thead>
<tr>
<th colspan="4">Si(111)</th>
<th colspan="4">Si(100)</th>
</tr>
<tr>
<th>Case</th>
<th>$N_{f}$</th>
<th>$\varepsilon_{\mathrm{wf}}/\varepsilon$</th>
<th>$A_{P}/\sigma$</th>
<th>$\lambda/\sigma$</th>
<th>Case</th>
<th>$N_{f}$</th>
<th>$\varepsilon_{\mathrm{wf}}/\varepsilon$</th>
<th>$A_{P}/\sigma$</th>
<th>$\lambda/\sigma$</th>
</tr>
</thead>
<tbody>
<tr>
<td>1-1</td>
<td>2896</td>
<td>2.0</td>
<td>3</td>
<td>2, 4, 6</td>
<td>2-1</td>
<td>2896</td>
<td>2.0</td>
<td>3.5</td>
<td>2, 4, 6, 8</td>
</tr>
<tr>
<td>1-2</td>
<td>4240</td>
<td>2.0</td>
<td>3</td>
<td>2, 4, 6, 8, 12</td>
<td>2-2</td>
<td>3536</td>
<td>2.0</td>
<td>3.5</td>
<td>3, 4, 6, 12</td>
</tr>
<tr>
<td>1-3</td>
<td>5008</td>
<td>2.0</td>
<td>3</td>
<td>2, 4, 6, 8, 10</td>
<td>2-3</td>
<td>5008</td>
<td>2.0</td>
<td>2.5</td>
<td>2, 4, 6, 12</td>
</tr>
<tr>
<td>1-4</td>
<td>5008</td>
<td>2.0</td>
<td>5</td>
<td>2, 4, 6, 8</td>
<td>2-4</td>
<td>5008</td>
<td>2.0</td>
<td>3.5</td>
<td>2, 4, 6, 8, 12</td>
</tr>
<tr>
<td>1-5</td>
<td>5008</td>
<td>1, 1.2, 1.6, 2</td>
<td>3</td>
<td>2</td>
<td>2-5</td>
<td>5008</td>
<td>2.0</td>
<td>4.5</td>
<td>2, 4, 6, 8, 12</td>
</tr>
<tr>
<th colspan="4">Si(110)</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<th>Case</th>
<th>$N_{f}$</th>
<th>$\varepsilon_{\mathrm{wf}}/\varepsilon$</th>
<th>$A_{P}/\sigma$</th>
<th>$\lambda/\sigma$</th>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>3-1</td>
<td>2896</td>
<td>2.0</td>
<td>$3.\sigma$</td>
<td>2, 3, 4, 10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>3-2</td>
<td>4240</td>
<td>2.0</td>
<td>$3.\sigma$</td>
<td>2, 4, 6, 8</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Notes: Si, silicon; $N_{f}$, number of water molecule; $\varepsilon_{\mathrm{wf}}/\varepsilon$, wall-fluid interaction energy; $A_{P}/\sigma$, amplitude of microstructure and $\lambda/\sigma$, period of microstructure.

![](./images/811645823480758274_11.jpg)

Figure 7. MD results of (a) density, $\rho\sigma^{3}$ and (b) average number of hydrogen bonds per water molecule, $n_{\text{HB}}$ contours on surface Si(111) with $\varepsilon_{\text{wf}}/\varepsilon=2.0$, surface microstructures of $A_{p}=3\sigma$ and various periods. The upmost plot shows the results for the plain surface and then, from top to down, the plots show the results of surface microstructures with $\lambda=2\sigma$, $8\sigma$ and $10\sigma$.

amount. Further increasing $\lambda/r_{\text{B}}$ leads to a reduction in $\theta$ with increase in the amount of water trapped in cavities, $\rho_{\text{cav}}\sigma^{3}$. It is also revealed that the values of $\theta$ and $\rho_{\text{cav}}\sigma^{3}$ vary only a little with changes in the amplitude $(A_{p}\sigma^{-1}=3$ and 5) and the number of water molecules $(2896\leq N_{f}\leq5008)$. There is just one result beyond $\lambda/r_{\text{B}}>0.8$ for the anisotropy characteristics of the droplet on surface. The observations on the above results demonstrate that the contact angle is closely related to the period parameter $\lambda/r_{\text{B}}$ of the column array of the surface microstructure and the number density of water trapped in the cavities as well.

Figures 10 and 11 show the simulation results of the contact angle $\theta$ and the water number density in cavities $\rho_{\text{cav}}\sigma^{3}$ versus the period parameter $\lambda/r_{\text{B}}$ for a droplet on the substrate of lattice structures Si(100) and Si(110), respectively. For the parameter $\lambda/r_{\text{B}}$ in the range of $\lambda/r_{\text{B}}\leq0.2$, the comparison shows that the enhancement in hydrophobicity with increase in contact angle for Si(111) is the highest among the three lattice structures. It can be attributed to the most packed atoms in each layer of Si(111). Relative to the other two lattices, to form the surface cavities the largest number of solid atoms has to be removed, which leads to the most noticeable enhancement in hydrophobicity.

Similar to the predictions for Si(111), the values of $\rho_{\text{cav}}\sigma^{3}$ for Si(100) and Si(110) increase and the contact angle decreases in the range of $0.2\leq\lambda/r_{\text{B}}\leq0.6$ and the

![](./images/811645823480758274_12.jpg)

Figure 8. MD results of (a) density, $\rho\sigma^{3}$ and (b) average number of hydrogen bonds per water molecule, $n_{\text{HB}}$ contours on surface Si(100) with $\varepsilon_{\text{wf}}/\varepsilon=2.0$, surface microstructures of $A_{p}=3.5\sigma$ and various periods. The upmost plot shows the results for the smooth surface and then, from top to down, the plots show the results of surface microstructures with $\lambda=2\sigma$, $8\sigma$, and $12\sigma$.

contact angle reaches a local minimum at a certain $\lambda/r_{\text{B}}$ between 0.6 and 0.8, then turns to an ascending trend with $\rho_{\text{cav}}\sigma^{3}$ changing very slowly or maintaining approximately a constant value. In the region of $\lambda/r_{\text{B}}>0.8$, the level of $\rho_{\text{cav}}\sigma^{3}$ is about 0.5 for Si(100), which is obviously higher than the values of 0.2 and 0.4 for Si(111) and Si(110), respectively. Since the strength of epitaxial layering on the three substrates without microstructure is in the order of $\text{Si(111)}>\text{Si(110)}>\text{Si(100)}$, it implies that Si(100) has the most rough surface and the most smooth perpendicular walls among the three substrates, more fluid molecules accumulate in cavities. Relatively lower $\rho_{\text{cav}}\sigma^{3}$ is beneficial to promote the hydrophobicity and the case is most likely the Cassie model in the wetting characteristics.

On the other hand, higher fluid density inside the cavity enhances wall-fluid momentum exchange and the hydro- philicity as well. This case is the so-called Wenzel model.

Beyond the minimal contact angle, the results in Figures 9 and 10 indicate that although $\rho_{\text{cav}}\sigma^{3}$ is ascending or maintained at a high level, the hydrophilicity has no promotion and it even reduces. This phenomenon implies that there are still other contrary effects with larger period of microstructure. In Figures 9 and 10, the symbols marked with (*) and ($\Delta$), respectively, represent the maximum and the minimum contact angles for relatively longer period of microstructure. These cases are to be discussed later with the results shown in Figure 12.

![](./images/811645823480758274_13.jpg)

Figure 9. Variations of contact angle $\theta$ and water density inside cavities $\rho\sigma^{3}$ with period parameter $\lambda/r_{\text{B}}$ and cavity amplitude $A_{p}\sigma^{-1}$ of microstructure on the surface Si(111). The interaction energy parameter is $\varepsilon_{\text{wf}}/\varepsilon = 2.0$ and the number of fluid molecules $N_{f}=2896 - 5008$.

![](./images/811645823480758274_14.jpg)

Figure 10. Variations of contact angle $\theta$ and water density inside cavities $\rho\sigma^{3}$ with period parameter $\lambda/r_{\text{B}}$ and cavity amplitude $A_{p}\sigma^{-1}$ of microstructure on the surface Si(100). The interaction energy parameter is $\varepsilon_{\text{wf}}/\varepsilon = 2.0$.

Figure 12 shows the number density and hydrogen bond density contours for maximum and minimum contact angle when $\rho_{\text{cav}}\sigma^{3}$ maintains about a higher constant value. To investigate the influences of hydrogen bond on the wettability in the Wenzel mode, the number density of hydrogen bond inside the cavities is defined as $\rho_{\text{HB}}\sigma^{3}=n_{\text{HB}}\rho\sigma^{3}$, and the tangential plane is defined as the $xy$-plane at $z\sim0.5\sigma$ which is considered as the wall–fluid interface. Figure 12 presents the contours of the number density of water molecules $\rho\sigma^{3}$ and hydrogen bond $\rho_{\text{HB}}\sigma^{3}$ at max–min contact angles and specific conditions of longer period $\lambda/r_{\text{B}}$. Figure 12(a) and (b), respectively, correspond to the cases selected from Figures 9 and 10. In the left part of Figure 12, some lower density distributions appear in the first epitaxial layer and the higher hydrogen bond density around the corresponding positions but, in contrast, there are consistent values in the first epitaxial layer and lower hydrogen bond density on the tangential plane depicted on the right side of Figure 12.

### 3.2.3 Qualitative trend of wettability with the period parameter $\lambda/r_{B}$

Although it has been well known that the surface microstructure may lead to the so-called ‘lotus effect’ [24], how the surface microstructure affects the wettability is still an open issue [35]. From the results shown in Figures 9–11, we have found that, without surface modification $(\lambda/r_{\text{B}} = 0)$, the hydrophobic characteristics based on contact angles of the three surface are in the order of $\text{Si}(100)>\text{Si}(110)>\text{Si}(111)$. Besides the quantitative consideration, the results for the three surface lattice structures have very similar qualitative trends. The qualitative trends of the variations $\theta\sim\lambda/r_{\text{B}}$ and $\rho_{\text{cav}}\sigma^{3}\sim\lambda/r_{\text{B}}$ for various surface orientations have common features and are schematically illustrated by the curve patterns presented in Figure 13. The $\theta\sim\lambda/r_{\text{B}}$ curve shows that the contact angle first increases with $\lambda/r_{\text{B}}$, after it reaches a maximum it drops to a local minimum and then ascends again.

Three regions are therefore classified. In region I, the water number density in cavities $\rho_{\text{cav}}\sigma^{3}$ has a very low level at small values of $\lambda/r_{\text{B}}(<0.2)$. With small $\lambda/r_{\text{B}}$, it is hard for the water molecules to penetrate into the cavity in the presence of surface repelling effect inside the cavity. In this low-$\lambda/r_{\text{B}}$ region, the contact angle ascends with increasing $\lambda/r_{\text{B}}$, which corresponds to the Cassie model. In the region II of intermediate $\lambda/r_{\text{B}}$ $(0.2<\lambda/r_{\text{B}}<0.8)$, the cavities are wetted by the water molecules and, therefore, the contact angle reduces. This fact demonstrates that the wetting model transfers from the Cassie to

![](./images/811645823480758274_15.jpg)

Figure 11. Variations of contact angle $\theta$ and water density inside cavities $\rho\sigma^{3}$ with period parameter $\lambda/r_{B}$ of microstructure on the surface Si(110). The interaction energy parameter is $\varepsilon_{wf}/\varepsilon=2.0$.

the Wenzel model. Beyond the value of $\lambda/r_{B}$ for minimum contact angle, the water molecules in cavities $\rho_{cav}\sigma^{3}$ approximately approach a constant of higher level, the contact angle behaves in an ascending trend again. In region III, $\lambda/r_{B}>0.8$. In this region, a longer period $\lambda/r_{B}$ reduces the epitaxial layer at some local position, where more hydrogen bonds appear. The large amount of hydrogen bonds also leads to a decrease in the layer density. The contact angle is raised due to less fluid molecules interacting with the solid atoms. In the previous works [17,18], the role of the cavity amplitude in determining the contact angle has been disclosed. Herein, the significance of the period of cavity to the wettability is demonstrated. However, different from the solid material of graphite adopted in [17] and the liquid model of hydrocarbons polymer in [18], the liquid and solid materials considered in the present study are water and silicon. The differences in the results of the studies mentioned above reveal that the wettability behaviour is highly dependent of the solid and liquid properties.

### 3.2.4 Effects of wall-fluid interaction energy $\varepsilon_{wf}/\varepsilon$

One of the methods to change the hydrophobicity of a surface in simulations is tuning the wall-fluid interaction energy and keeping the wall-fluid interaction distance a

![](./images/811645823480758274_16.jpg)

Figure 12. The density distribution and hydrogen bond density contour for maximum and minimum contact angle with relative longer period of microstructure. The contours in (a) and (b) correspond to Figures 9 and 10, respectively.

![](./images/811645823480758274_17.jpg)

Figure 13. Qualitative natures of the curves $\theta\sim\lambda/r_{B}$ and $\rho_{cav}\sigma^{3}\sim\lambda/r_{B}$.

![](./images/811645823480758274_18.jpg)

Figure 14. (a) Water density laying distribution, $\rho\sigma^3$, and the average number of hydrogen bond, $n_{\text{HB}}$, distributions with various values of wall-fluid interaction energy parameter and (b) the relationship between contact angle and wall-fluid interaction energy.

constant [9,14,33]. To investigate the effects of wall-fluid interaction energy under artificial microstructure, we test the contact angle of water droplet on surface of Si(111) lattice with the microstructure $\lambda=2\sigma$, and $A_p=3\sigma$ and the values of $\varepsilon_{\text{wf}}/\varepsilon=1$, 1.2, 1.6 and 2.0. Figure 14(a) shows the water density distributions with layering phenomenon degraded and the average number of hydrogen bond shifting away from the wall-fluid interface followed by the decrease in wall-fluid interaction energy. Predictions at various values of $\varepsilon_{\text{wf}}/\varepsilon$ in Figure 14(b) disclose that the contact angle behaves approximately in a mode inversely proportional to wall-fluid interaction energy with the presence of a microstructure.

## 4. Concluding remarks

In the present study of MDS, wettability characteristics of water droplet on the Si(111), Si(100) and Si(110) surfaces without and with microstructures have been analysed. Based on the present analysis, the following conclusions can be drawn.

(1) With only atomistic roughness of lattice structures, widths of the depletion layers are almost consistent for different contact angles with various surface orientations. The result reveals that the contact angle is not only affected by the depletion width, but also influenced by the fluid density layering. The stronger layering effect caused by smoother atomic surface has higher probability of solid-fluid momentum exchange and this, in turn, enhances the hydrophilicity. In this aspect, even with the same solid material, a smoother surface may become more hydrophilic.

(2) The qualitative natures of the contact angle depend- ing on $\lambda/r_{\text{B}}$ and $\rho_{\text{cav}}\sigma^3$ are provided in the present study. Three regimes with different values of $\lambda/r_{\text{B}}$ are identified and employed to address various wetting mechanisms of water on silicon surfaces. In the regime of low $\lambda/r_{\text{B}}$, only a few water molecules enter the cavities, this non-wetting condition implies that the presence of surface microstructure with cavities enhances the hydrophobicity. In the regime of intermediate $\lambda/r_{\text{B}}$, the wetting characteristic is transferred from the Cassie to the Wenzel model with the repelling effect of the surfaces inside cavities. In the regime of high $\lambda/r_{\text{B}}$, the longer period $\lambda/r_{\text{B}}$ reduces the epitaxial layer density and increases the hydrogen bond at some locations thus making the contact angle promoted.

## Acknowledgements

This study was supported by the National Science Council of the Republic of China (Taiwan) through the grant NSC-97-2218-E-012-002-MY2.

## References

[1] H.A. Stone, A.D. Stroock, and A. Ajdari, *Engineering flows in small devices - Microfluidics toward a lab-on-a chip*, Annu. Rev. Fluid Mech. 36 (2004), pp. 381-411.

[2] T.M. Squires and S.R. Quake, *Microfluidics: Fluid physics at the nanoliter scale*, Rev. Modern Phys. 77 (2005), pp. 977-1026.

[3] D.J. Harrison, K. Fluri, K. Seiler, Z. Fan, C.S. Effenhauser, and A. Manz, *Micromachining a miniaturized capillary electrophoresis-based chemical analysis system on a chip*, Science 261 (1993), pp. 895-897.

[4] B.L. de Groot and H. Grubmüller, *The dynamics and energetics of water permeation and proton exclusion in aquaporins*, Curr. Opin. Struct. Biol. 15 (2005), pp. 176-183.

[5] D. Bonn, J. Eggers, J. Indekeu, J. Meunier, and E. Rolley, *Wetting and spreading*, Rev. Modern Phys. 81 (2009), pp. 739-805.

[6] L. Bocquet and J.-L. Barrat, *Flow boundary conditions from nano- to micro-scales*, Soft Matter 3 (2007), pp. 685-693.

778  T.-H. Yen

[7] C.Y. Soong, T.H. Yen, and P.Y. Tzeng, *Molecular dynamics simulation of nanochannel flows with effects of wall lattice–fluid interactions*, Phys. Rev. E 76 (2007), 036303.

[8] C.W. Extrand, S.I. Moon, P. Hall, and D. Schmidt, *Superwetting of structured surfaces*, Langmuir 23 (2007), pp. 8882–8890.

[9] R.S. Voronov, D.V. Papavassiliou, and L.L. Lee, *Review of fluid slip over superhydrophobic surface and its dependence on the contact angle*, Ind. Eng. Chem. Res. 47 (2008), pp. 2455–2477.

[10] T.N. Krupenkin, J.A. Taylor, T.M. Schneider, and S. Yang, *From rolling ball to complete wetting: The dynamic tuning of liquids on nanostructured surfaces*, Langmuir 20 (2004), pp. 3824–3827.

[11] G. McHale, N.J. Shirtcliffe, S. Aqil, C.C. Perry, and M.I. Newton, *Topography driven spreading*, Phys. Rev. Lett. 93 (2004), 036102.

[12] R. Qiao, *Effects of molecular level surface roughness on electroosmotic flow*, Micorfluid Nanofluid 3 (2007), pp. 33–38.

[13] L. Bocquet and J.-L. Barrat, *Large slip effect at a nonwetting fluid–solid interface*, Phys. Rev. Lett. 82 (1999), pp. 4671–4674.

[14] R.S. Voronov, D.V. Papavassiliou, and L.L. Lee, *Boundary slip and wetting properties of interfaces: Correlation of the contact angle with the slip length*, J. Chem. Phys. 124 (2006), 204701.

[15] T. Werder, J.H. Walther, R.L. Jaffe, T. Halicioglu, F. Noca, and P. Koumoutsakos, *Molecular dynamics simulation of contact angles of water droplets in carbon nanotubes*, Nano Lett. 1 (2001), pp. 691–702.

[16] T. Werder, J.H. Walther, R.L. Jaffe, T. Halicioglu, and P. Koumoutsakos, *On the water–carbon interaction for use in molecular dynamics simulations of graphite and carbon nanotubes*, J. Phys. Chem. B 107 (2003), pp. 1345–1352.

[17] M. Lundgren, N.L. Allan, and T. Cosgrove, *Molecular dynamics study of wetting of a pillar surface*, Langmuir 19 (2003), pp. 7127–7129.

[18] C. Yang, U. Tartaglion, and B.N.J. Persson, *Influence of surface roughness on superhydrophobicity*, Phys. Rev. Lett. 97 (2006), 116103.

[19] C. Yang, U. Tartaglion, and B.N.J. Persson, *Nanodroplets on rough hydrophilic and hydrophobic surface*, Eur. Phys. J. E 25 (2008), pp. 139–152.

[20] J. Servantie and M. Müller, *Statics and dynamics of a cylindrical droplet under and external body force*, J. Chem. Phys. 128 (2008), 014709.

[21] D.M. Huang, C. Sendner, D. Horinek, R.R. Netz, and L. Bocquet, *Water slippage versus contact angle: A quasiuniversal relationship*, Phys. Rev. Lett. 101 (2008), 226101.

[22] J. Chai, S. Liu, and X. Yang, *Molecular dynamics simulation of wetting on modified amorphous silica surface*, Appl. Surf. Sci. 225 (2009), pp. 9078–9084.

[23] D. Quéré, *Wetting and roughness*, Annu. Rev. Mater. Res. 38 (2008), pp. 71–99.

[24] D. Quéré, *Non-sticking drops*, Rep. Prog. Phys. 68 (2005), pp. 2495–2532.

[25] C. Dorrer and J. Rühe, *Condensation and wetting transitions on microstructured ultrahydrophobic surfaces*, Langmuir 23 (2007), pp. 3820–3824.

[26] F. Sedlmeier, J. Janecek, C. Sendner, L. Bocquet, R.R. Netz, and D. Horinek, *Water at polar and nonpolar solid walls (review)*, Biointerphases 3(3) (2008), pp. FC23–FC39.

[27] D.C. Repaport, *The Art of Molecular Dynamics Simulation*, Cambridge University Press, Cambridge, UK, 2001.

[28] J. Marti, *Analysis of the hydrogen bonding and vibrational spectra of supercritical model water by molecular dynamics simulations*, J. Chem. Phys. 110(14) (1999), pp. 6876–6886.

[29] N. Matubayasi, C. Wakai, and M. Nakahara, *Structural study of supercritical water. I. Nuclear magnetic resonance spectroscopy*, J. Chem. Phys. 107(21) (1997), pp. 9133–9140.

[30] R. Qiao and N.R. Aluru, *Ion concentration and velocity profiles in nanochannel electroosmotic flows*, J. Chem. Phys. 118(10) (2003), pp. 4692–4701.

[31] D. Li, *Drop size dependence of contact angles and line tensions of solid–liquid systems*, Colloid Surf. A: Physicochem. Eng. Aspects 116 (1996), pp. 1–23.

[32] A. Marmur, *Line tension and the intrinsic contact angle in solid–liquid–fluid systems*, J. Colloid Interface Sci. 186 (1997), pp. 462–466.

[33] P.A. Thompson and M.O. Robbins, *Shear flow near solids: Epitaxial order and flow boundary conditions*, Phys. Rev. A 41 (1990), pp. 6830–6837.

[34] C. Sendner, D. Horinek, L. Bocquet, and R.R. Netz, *Interfacial water at hydrophobic and hydrophilic surfaces: Slip, viscosity, and diffusion*, Langmuir 25(18) (2009), pp. 10768–10781.

[35] Y.-T. Cheng and D.E. Rodak, *Is the lotus leaf superhydrophobic?* Appl. Phys. Lett. 86 (2005), 144101.