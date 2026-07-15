# Electrochemical-mechanical coupled modeling and parameterization of swelling and ionic transport in lithium-ion batteries

Daniel Sauerteig$^{a,*}$, Nina Hanselmann$^{a}$, Arno Arzberger$^{a}$, Holger Reinshagen$^{a}$, Svetlozar Ivanov$^{b}$, Andreas Bund$^{b}$

$^{a}$ Robert Bosch GmbH, Robert-Bosch-Str. 40, 96050 Bamberg, Germany
$^{b}$ Electrochemistry and Electroplating Group, Technische Universität Ilmenau, Gustav-Kirchhoff-Str. 6, 98693 Ilmenau, Germany

![](./images/813069470263148547_1.jpg)

## HIGHLIGHTS
- Implementation of a fully-coupled electrochemical-mechanical model.
- Swelling induced macroscopic mechanical stress due to external compression.
- Parameterization and implementation of pressure-dependent ionic transport.
- Electrical and mechanical validation using a 10 Ah hard case cell.
- Enhanced heterogeneous lithiation of the anode at elevated stress levels.

---

## ARTICLE INFO
**Keywords:**
Lithium ion battery
Mechanical
Stress
Expansion
Compression
Simulation

## ABSTRACT
The intercalation and aging induced volume changes of lithium-ion battery electrodes lead to significant mechanical pressure or volume changes on cell and module level. As the correlation between electrochemical and mechanical performance of lithium ion batteries at nano and macro scale requires a comprehensive and multidisciplinary approach, physical modeling accounting for chemical and mechanical phenomena during operation is very useful for the battery design. Since the introduced fully-coupled physical model requires proper parameterization, this work also focuses on identifying appropriate mathematical representation of compressibility as well as the ionic transport in the porous electrodes and the separator. The ionic transport is characterized by electrochemical impedance spectroscopy (EIS) using symmetric pouch cells comprising $LiNi_{1/3}Mn_{1/3}Co_{1/3}O_2$ (NMC) cathode, graphite anode and polyethylene separator. The EIS measurements are carried out at various mechanical loads. The observed decrease of the ionic conductivity reveals a significant transport limitation at high pressures. The experimentally obtained data are applied as input to the electrochemical-mechanical model of a prismatic 10 Ah cell. Our computational approach accounts intercalation induced electrode expansion, stress generation caused by mechanical boundaries, compression of the electrodes and the separator, outer expansion of the cell and finally the influence of the ionic transport within the electrolyte.

---

### 1. Introduction

Lithium-ion batteries (LIBs), used in the majority of electronic portable devices, such as cell phones and power tools, are the most attractive energy storage in electric vehicles due to their outstanding performance. During the past few years the development of advanced materials, efficient manufacturing technologies and innovative cell designs further increased the energy densities and simultaneously reduced battery production costs. In most of the host materials for state-of-the-art LIBs Li-ion intercalation induces phase transitions upon charge and discharge. These phenomena lead to intercalation induced volume changes of the active materials finally resulting in swelling of unconstrained cells [1–6] or significant stress formation in cells constrained by rigid casings or module frames [7].

Battery modeling and simulation is a powerful tool for improving LIB design, advance the operating conditions and to get an insight into the internal processes. The first electrochemical-based LIB models were developed by Newman and coworkers [8,9] by applying the concentrated solution and porous electrode theory. Since that time the power of modeling has also been used to understand the mechanical

---
* Corresponding author.
E-mail address: daniel.sauerteig@de.bosch.com (D. Sauerteig).

https://doi.org/10.1016/j.jpowsour.2017.12.044
Received 28 September 2017; Received in revised form 12 December 2017; Accepted 15 December 2017
0378-7753/ © 2017 Elsevier B.V. All rights reserved.

contribution to the LIB aging mechanisms. Starting from the micro- scopic scale, electrochemical-mechanical coupled models were devel- oped to understand stress generation and crack formation within a single active particle during lithiation and delithiation [10-20]. Apart from that there are also models accounting geometry changes in the macroscopic electrode and cell scale existent in literature [5,21-23]. Nevertheless, these models do not involve the dynamic stress genera- tion and the compression of the porous materials, which influences the ionic transport properties.

The focus of this study is the implementation and parameterization of a fully-coupled electrochemical-mechanical model of a Li-ion cell on the macroscopic level. Therefore we firstly introduce in the model a fully-coupled and physically-based description of the electrode expan- sion effects, stress formation and the ionic transport properties in the porous electrodes or the separator. In our theoretical approach the fundamentals of the electrochemical processes follow Newman's dual foil model [8,9] and the electrode dilation is applied according to our previous work [24]. The current study introduces the physical princi- ples of pore structure compression and its coupling with the electro- chemical model. The experimental parameterization focuses on the pressure-dependent electrolyte transport in the electrodes and se- parator. This can be achieved by determining the ionic resistance of the porous structures in symmetric cells and compressibility measurements. Finally, the implemented model is validated and applied to evaluation of the consequences of elevated pressure conditions.

## 2. Model formulation

In this section the principles of the Li-ion battery simulation model are presented. The introduced mathematical approach for description of porous battery electrodes [8,9] is extended by linking its basics with the mechanical model of porous electrochemically active layers. The fully coupled model is implemented into COMSOL Multiphysics, version 5.2 a.

### 2.1. Electrochemical model

For simplification the active material particles of the electrode are assumed to be of a spherical shape with a mean radius $R_{p}$ and homo geneously distributed inside the electrode. This assumption is dis- putable, since the graphite particles do not have a perfect spherical shape. Nevertheless, referring to other works [25-27] this approxima- tion is also used in this study. The subscripts $s$ and $l$ in the equations introduced in this section indicate the solid electrode and liquid elec- trolyte phase, respectively.

The diffusion driven Li concentration in electrochemically active particles follows Fick's second law presented in spherical coordinates (eq. (1)) using the solid state diffusion coefficient $D_{s}$, particle radius $r$ and solid phase concentration $c_{s}$.

$$
\frac{\partial c_{s}}{\partial t}=\frac{1}{r^{2}} \frac{\partial}{\partial r}\left(D_{s} r^{2} \frac{\partial c_{s}}{\partial r}\right)
\tag{1}
$$

The two boundary conditions at the particle surface and the particle center read as

$$
\left.\frac{d c_{s}}{d r}\right|_{r=R_{p}}=-\frac{i_{n}}{D_{s}} \quad\left.\frac{d c_{s}}{d r}\right|_{r=0}=0
\tag{2}
$$

where $F$ is the Faraday constant and $i_{n}$ the molar current density at the particle surface. The latter can be expressed by Butler-Volmer eq. (3), describing $i_{n}$ as a function of applied potential $\varphi$.

$$
F i_{n}=i_{0}\left[\exp \left(\frac{\alpha_{a} F}{R T} \varphi\right)-\exp \left(-\frac{\alpha_{c} F}{R T} \varphi\right)\right]
\tag{3}
$$

$R$ corresponds to the universal gas constant, $T$ to the temperature and $\alpha_{a}$ and $\alpha_{c}$ to the anodic and cathodic charge transfer coefficient.

The exchange current density $i_{0}$ is related to the solid and liquid phase concentrations $c_{s}$ and $c_{l}$ by the anodic and cathodic reaction rate $k_{a}$ and $k_{c}$ (eq. (4)). $c_{s, \max }$ represents the maximum Li concentration within the active material and $c_{l, r e f}=1 \mathrm{~mol} . \mathrm{m}^{-3} . c_{l, r e f}$ is merely necessary to achieve consistent units. Since the charge transfer process occurs at the particle surface, the surface concentration of the active material has to be considered in this case.

$$
i_{0}=F\left(k_{a}\right)^{\alpha_{c}}\left(k_{c}\right)^{\alpha_{a}}\left(c_{s, \max }-c_{s}\right)^{\alpha_{c}}\left(c_{s}\right)^{\alpha_{a}}\left(\frac{c_{l}}{c_{l, r e f}}\right)^{\alpha_{c}}
\tag{4}
$$

The electrical current flow $i_{s}$ in the solid electrode volume fraction follows Ohm's law, where $\varkappa_{s}$ is the electronic conductivity and $\varphi_{s}$ the solid phase electrical potential (eq. (5)).

$$
i_{s}=-\varkappa_{s} \nabla \varphi_{s}
\tag{5}
$$

The mass balance of ions moving in a liquid phase through a porous domain material is expressed by eq. (6) [9] and the boundary condition (eq. (7)) of zero flux at the current collector interface $(x=0)$ and se parator interface $(x=t)$. In this case, $t$ corresponds to the coating thickness of the electrode.

$$
\phi \frac{\partial c_{l}}{\partial t}=\nabla\left(\phi D_{l} \nabla c_{l}\right)+a_{s} i_{n}\left(1-t_{+}^{0}\right)
\tag{6}
$$

$$
\left.\nabla c_{l}\right|_{x=0 \text { and } x=t}=0.
\tag{7}
$$

$\phi$ represents the pore volume fraction of the electrode, $a_{s}$ the active surface area and $t_{+}^{0}$ the transference number of Li ions in the liquid solvent. $t_{+}^{0}$ is assumed to be constant in this work, whereas the diffusion coefficient $D_{l}$ of the electrolyte depends on the concentration [28].

The potential gradient in the electrolyte calculates as [9]

$$
\nabla \varphi_{l}=-\frac{i_{l}}{\varkappa_{l}}+\frac{2 R T}{z F}\left(1-t_{+}^{0}\right)\left(1+\frac{\partial \ln f_{ \pm}}{\partial \ln c_{l}}\right) \nabla \ln c_{l}.
\tag{8}
$$

where the current density in the liquid phase $i_{l}$ follows the principles of charge conservation and is coupled to $i_{s}$ and the particle surface flux:

$$
\nabla i_{l}=-\nabla i_{s}=-F a_{s} i_{n}
\tag{9}
$$

The transport parameters in the liquid phase depend on the porosity and tortuosity. Thereby, the porosity $\phi$ corresponds to the electrolyte volume fraction in the electrode and the tortuosity $\tau$ specifies the re lative elongation of diffusion path perpendicular through the porous structure. Commonly, $\sigma_{l}$ and $D_{l}$ are used as effective transport para meters inside the electrodes and separator. The limitation of the equi librium bulk conductivity $\varkappa_{l, 0}$ and bulk diffusivity $D_{l, 0}$ can be expressed by the ionic transport factor $f$ which includes $\phi$ and $\tau$ as follows:

$$
\varkappa_{l}=f \varkappa_{l, 0}
\tag{10}
$$

$$
D_{l}=f D_{l, 0}
\tag{11}
$$

$$
f=\frac{\phi}{\tau}
\tag{12}
$$

The Bruggeman relation (eq. (13)) connects porosity and tortuosity of porous structures, where the Bruggeman coefficient $\beta$ becomes 0.5 for an electrode containing ideal spherical particles. Eq. (13) represents the most commonly used formulation.

$$
\tau=\phi^{-\beta}
\tag{13}
$$

While the limitation of ionic transport in battery materials has been proven to be significantly higher than predicted by the Bruggeman approximation $(\beta=0.5)[29,30]$, numerous modeling studies using this value can be found in literature [31-33].

### 2.2. Mechanical model

Single particle expansion. Existing theoretical works focusing on the mechanical behavior of Li-ion cells describe the intercalation induced

![](./images/813069470263148547_2.jpg)

Fig. 1. OCP-curves and relative swelling of a) graphite [34] and b) NMC particles used as input parameters for the coupled electrochemical-mechanical model. Principle calculations of the strain and porosity evolution c)+d) and the corresponding g-value and mechanical stress σ e)+f) during active material expansion $\chi_{Li}$ at various case stiffnesses $E_{case}$.

stresses inside the active particles [10,12]. In these models the active particles are assumed to consist of isotropic linear elastic material. Depending on the concentration change of the active species $\Delta c_{s}=c_{s}-c_{s,0}$ stress calculation are performed with respect to the initial stress-free state of the solid $c_{s,0}$. However, for our study the expansion of the single particles is more relevant as we intend to calculate the expansion and the consequential stress development. The relative expansion of the electrodes depends on the concentration of the diffusing species and was investigated in a number of experimental studies [6,34-36]. In the case of full cells, the swelling of both electrodes yields to a superposed swelling of the full cell as one electrode is lithiated while the other is delithiated. For our modeling work the swelling functions shown in Fig. 1a)+b) are used.

Free stack expansion. The mechanical model consists of a solid domain with elastic properties which represents the electrode structure. The wound parts of the jelly roll are neglected in the model since it is assumed that they do not contribute to the expansion and stress generation at the center of the cell. The contact area between the electrodes and the cell case corresponds to the outer flat area of the jelly roll. The total expansion of the electrode layers is calculated by the sum of expansions of all individual layers. As our model applies homogenization within the electrode domain, the integral expansion of the electrode along the thickness direction t has to be multiplied by the active part of the electrode (eq. (14)) [23].

$$
\varepsilon_{L i}=\frac{\phi_{a}}{t_{0}} \int_{0}^{t_{0}} \Omega \overline{c}_{s} d t \tag{14}
$$

$\overline{c}_{s}$ represent the local medium particle concentration related to the initial reference concentration, $\Omega$ is the molar volume of the active material, $\phi_{a}$ is the volumetric part of active material and $t_{0}$ is the initial thickness of an individual electrode coating. Therefore, the relative volume change $\chi_{Li}$ of the active particles can be expressed by the ratio of the particle volume change $\Delta V_{p}$ and the initial particle volume $V_{p,0}$ (eq. (15)). In the equilibrium state eq. (14) can be simplified to eq. (16) [23]. However, this formulation is only valid for porous electrode configurations where the active material volume change is significantly less than the pore volume fraction.

$$
\chi_{L i}=\frac{\Delta V_{p}}{V_{p, 0}}=\Omega \overline{c}_{s} \tag{15}
$$

$$
\varepsilon_{L i}=\phi_{a} \chi_{L i} \tag{16}
$$

The concentration dependent expansion of a full cell $\Delta t_{cell}$ is expressed as the sum of the individual layer expansions of the anode $\Delta t_{a}$ and the cathode $\Delta t_{c}$.

$$
\Delta t_{c e l l}=\Delta t_{a}+\Delta t_{c} \tag{17}
$$

Compression model. The previously presented formulations are only valid for unstrained electrode expansions and will be therefore modified for our application. Eq. (18) is the common formulation of the relation between the strain $\varepsilon$, $\phi$ and $\chi_{Li}$ and therefore also valid in a mechanical strained case. The derivation of eq. (18) is based on the assumption of constant pore volume in the case of unstrained swelling and negligible active material compression since the mechanical stress within the porous domain is low (< 10 MPa) compared to the Young's modulus of active materials (approx. 10 GPa). A detailed derivation of eq. (18) is given in the supplementary material. The initial porosity is represented by $\phi_{0}$ and the initial active volume fraction by $\phi_{a,0}$. While the active material expands by a factor of $\chi_{Li}$ both, $\varepsilon$ and $\phi$ can vary simultaneously.

$$
\varepsilon-\phi=\phi_{a, 0} \chi_{L i}-\frac{\phi_{0}}{\phi_{a, 0} \chi_{L i}+1} \tag{18}
$$

Inspired by the works of Weidner and co-workers [37-39] we also introduce the swelling coefficient g which is defined by the ratio of the actual strain $\varepsilon$ and the theoretical strain $\varepsilon_{Li}$ of the composite electrode in eq. (19) $(0 \leq g \leq 1)$. This definition enables to separate the mathematical description of $\varepsilon$ (in eq. (20)) and $\phi$ (in eq. (21)).

$$
g=\frac{\varepsilon}{\varepsilon_{L i}}. \tag{19}
$$

$$
\varepsilon=g \phi_{a, 0} \chi_{L i} \tag{20}
$$

Considering eqs. (20) and (18), the porosity evolution can be mathematically described by eq. (21).

<table><thead><tr><th colspan="2">Hard case cell</th></tr></thead><tbody><tr><td>Nominal capacity</td><td>10.0 Ah</td></tr><tr><td>Material system</td><td>NMC/graphite</td></tr><tr><td>Thickness</td><td>12.6 mm</td></tr><tr><td>Length</td><td>120.0 mm</td></tr><tr><td>Hight</td><td>85.0 mm</td></tr><tr><td>Operating voltage</td><td>2.7 V - 4.2 V</td></tr><tr><td>Max. charging rate</td><td>C/2</td></tr><tr><td>Max. discharging rate</td><td>3C</td></tr><tr><td>Gravimetric energy density</td><td>135 Whkg−1</td></tr><tr><td>Volumetric energy density</td><td>280 Whl−1</td></tr></tbody></table>

$$
\phi=\phi_{a, 0} \chi_{L i}(g-1)+\frac{\phi_{0}}{\phi_{a, 0} \chi_{L i}+1}
\tag{21}
$$

The mechanical-based definition of $g$ (eq. (22)) is derived by applying Newton's third law. Since the electrode expansion exerts stress on the cell case, the cell case simultaneously responds equally in magnitude on the electrodes. Thus, $\varepsilon$ leads to a deformation of the case with the uniaxial linear elastic modulus $E_{case}$ and the porous electrodes with the elastic modulus $E$ are compressed. Thus, $E_{case}$ can be understood as local uniaxial case stiffness and $E$ as stiffness of the electrolyte-soaked porous electrode. Since a hard case cell usually exhibits void spaces, the electrolyte can be pressed out of the porous components.

$$
g=\frac{E}{E+E_{\text {case }}}
\tag{22}
$$

Fig. 1 shows some principle calculations of $\varepsilon$, $\phi$, $g$ and the corresponding mechanical stress $\sigma$ versus $\chi_{L i}$ at various case elasticities by applying eqs. (20-22). For the computation the electrode stiffness $E=(996\left(\varepsilon_{L i}-\varepsilon\right)+20)\text{MPa}$ [40], $\phi_{0}=0.3$ and $\phi_{a, 0}=0.7$ were defined according to our experimental conditions. While for small $E_{case}$ values the active material expansion is transferred into increasing $\varepsilon$ and $g$-values approaching 1, $\varepsilon$ decreases with $E_{case}$ which corresponds to decreasing $\phi$ and small $g$-values. Thus, also the stress $\sigma$ is enhanced by higher case stiffness. A decrease of porosity is also relevant for $g=1$ due to the fact that the pore volume is constant while the total electrode volume expands.

## 3. Experimental

### 3.1. Preparation of electrodes and cells

The investigated electrodes and cells are manufactured in-house and comprise a graphite negative electrode coated on a copper foil and a $\mathrm{LiNi}_{1 / 3} \mathrm{Mn}_{1 / 3} \mathrm{Co}_{1 / 3} \mathrm{O}_{2}$ (NMC) positive electrode with an aluminum foil as a substrate. A detailed description of the manufacturing process, materials and preparation procedures can be found in our previous work [24]. Porous polyethylene base film with a single side ceramic coating was used as separator. It exhibits a total thickness of $19 \mu \mathrm{m}$ and a porosity of $49 \%$. The following cells were manufactured in a dry-room for the model parameterization and validation:

- **Symmetric cells:** In order to measure the effective ionic transport of the porous electrodes and separator, symmetric single layer pouch cells with identical electrodes (NMC vs. NMC, graphite vs. graphite) and electrode geometric area of $17.9 \mathrm{~cm}^{2}$ were assembled (2a). Two copper foil electrodes (12 $\mu \mathrm{m}$ thick) were used to determine the ionic conductivity in the separator pores. By the variation of the number of separator layers (1, 3 and 5) the contribution of the electronic resistance of the cell setup can be identified, which enables the calculation of the pure ionic part. Electrolyte was filled in a glove box with argon atmosphere after drying the cells for $12 \mathrm{~h}$ at $70{^\circ} \mathrm{C}$ in a vacuum oven. The electrolyte contains a solvent mixture of ethylene carbonate (EC) and ethyl methylene carbonate (EMC) in a ratio of $3: 7$ by wt. with $0.5 \mathrm{M}$ tetrabutylammonium hexafluorophosphate (TBA-PF₆, Alfa Aeser) salt with a conductivity of $0.509 \mathrm{Sm}^{-1}$ at $25{^\circ} \mathrm{C}$. This Li-free electrolyte was used to suppress the charge transfer reaction during the EIS measurement. The amount of electrolyte was set to $0.6 \mathrm{ml}$ for the porous electrode cells and to $0.4 \mathrm{ml}$ for the separator cells. The pouch cells were subsequently closed by vacuum sealing and to ensure complete electrolyte soaking, the EIS measurements were started after $1 \mathrm{~h}$.
- **HEV cell:** For the model validation an in-house manufactured HEV cell with a nominal capacity of $10 \mathrm{Ah}$ is used. The cell consists of an aluminum case and one jelly roll of the previously mentioned material system. The operating voltage window is $2.7 \mathrm{~V}-4.2 \mathrm{~V}$ and the active cathode area is $0.3135 \mathrm{~m}^{2}$. The relevant cell and material properties for the modeling are provided in Table 1.

### 3.2. Measurement techniques

Pressure dependent electrolyte transport. Several methods are described in literature to determine the ionic transport through porous electrode structures. Based on the Bruggeman relation (eq. (13)), the quantification of tortuosity by three-dimensional reconstruction of the porous structure, followed by geometrical calculations or numerical simulations depending on the electrode morphology has been studied [41-46]. Furthermore, a polarization interruption technique using freestanding electrodes was developed [29,47]. The drawbacks of these methods are the preparation of freestanding electrodes and the requirement of further electrolyte properties such as transference number and diffusivity. The calculation of the tortuosity using the pore size distribution of the material and several geometrical assumptions has also been derived by Carniglia [48]. Based on the transmission line model (TLM), Ogihara et al. [49,50] verified the blocking electrode condition with a Li salt electrolyte where the symmetric electrodes are in a fully lithiated or delithiated state. Using this impedance based technique, ion transport through porous battery electrodes or separators with the porosity $\phi$ and the tortuosity $\tau$ can be mathematically described by the limitation of electrolyte bulk conductivity $\varkappa_{l, 0}$. With a sample thickness $t$ and cross sectional area $A$ of the porous material, only the ionic resistance $R_{ion}$ has to be determined. For modeling applications the effective ionic transport factor $f$ can be defined by applying eq. (23) in which $\varkappa_{l}$ represents the actual ionic conductivity of the porous material.

$$
f=\frac{\phi}{\tau}=\frac{\varkappa_{l}}{\varkappa_{l, 0}}=\frac{t}{R_{\text {ion }} A \varkappa_{l, 0}}
\tag{23}
$$

The characteristic parameter $R_{ion}$, which expresses the mobility of $\mathrm{Li}$ ions within the porous structure, can be obtained by using the TLM [30,49,51]. The model describes the AC impedance behavior of ions moving through cylindrical pores. For this approach, blocking electrode or electrolyte conditions are recommended to suppress the charge transfer reaction across the electrode electrolyte interface. The symmetric electrode configuration further avoids impedance contributions arising from the counter electrode. Thus, the system is ideally polarizable and the impedance is expressed by eq. (24).

$$
Z_{T L M}=\sqrt{\frac{R_{i o n}}{Q(j \omega)^{\gamma}}} \operatorname{coth}\left(\sqrt{R_{i o n} Q(j \omega)^{\gamma}}\right)
\tag{24}
$$

In the Nyquist representation $Z_{T L M}$ shows an angle of $45^{\circ}$ to the real axis in the high frequency domain. For low frequencies the TLM transitions to a constant value of $Re\{Z_{T L M}\}$ (eq. (25)).

$$
\operatorname{Re}\left\{Z_{T L M}\right\}_{\omega \rightarrow 0}=\frac{R_{i o n}}{3}
\tag{25}
$$

As electronic resistances of the electrodes, contact resistances and the ionic resistance of the separator are also present, the impedance is shifted by a high frequency contribution $R_{h f}$. Hence the total impedance

![](./images/813069470263148547_3.jpg)

Fig. 2. Schematic drawings of the parameterization and validation setup. a) Symmetric pouch cell with external compression for the ionic transport measurements by means of EIS and b) HEV cell in a modified compression jig with force and displacement sensors.

at low frequencies leads to eq. (26).

$$
Re\{Z\}_{\omega \to 0}=R_{hf}+\frac{R_{ion}}{3} \tag{26}
$$

This value corresponds to the extrapolation of the low frequency branch to the real axes in the Nyquist plot [30].

The complex impedance of porous separators soaked with electrolyte between two blocking electrodes can be described by a serially connected ionic resistance and constant phase element (CPE). The impedance of this equivalent circuit equates to

$$
Z_{sep}=R_{ion}+\frac{1}{Q(j \omega)^{\gamma}} \tag{27}
$$

which allows a simple determination of $R_{ion}$ by using fitting algorithms.

The pressure-dependent electrolyte transport measurements were carried out by using EIS functionality of a Biologic VSP potentiostat/ galvanostat and the compression setup presented in Fig. 2a). The symmetric pouch cells were analyzed with a perturbation amplitude of 10 mV for separators and electrodes. A frequency ranging from 200 kHz to 0.1 kHz for the separator cells and from 100 kHz to 1 Hz for the electrode cells was chosen (10 frequency points per decade and 5 repetitions per frequency for both cases). The EIS for the electrode cells was started right after applying the given pressure. As the separator exhibits strong viscoelastic creeping behavior, a time dependency of the measured impedance is expected particularly at high pressures. For that reason after adjusting the pressure we defined a waiting time of 15 min and then started the EIS measurement. An additional rubber pad between the steel compression plates and the pouch cell is used to compensate irregularities in thickness. The current compression force is measured by C9C (HBM) load cells and an Almemo 2690 (Ahlborn) data logger.

Compression test. For the compression measurements the electrode and separator samples were punched into coins of 18 mm diameter. In order to reduce the measurement error, five layers of electrodes or 100 layers of separators were stacked for one measurement run. All samples were soaked with electrolyte during the compression measurement using a zwicki-Line Z2.5 (Zwick Roell) materials testing machine. A compression force of 50 N was applied prior to the actual measurement to eliminate gaps between the stacked samples. Optimal alteration rate of $5 \mathrm{~N} \mathrm{~s}^{-1}$ was determined by preliminary experiments. At this rate, the stiffening due to the electrolyte flow out of the pores was assumed to be negligible. Furthermore, viscoelastic creeping was as well considered. The sampled data was adjusted by the deformation of the device after a blank measurement. The relative deformation was calculated by normalizing absolute deformation by the total thickness of the separator or the coating thickness of the electrodes respectively. Thus, only the deformation of the porous structures were evaluated. The deformation of the metallic current collector foil and the indentation of the active particles into the collector foil were not considered. The homogenized unidimensional stiffness of the stacks $E$ was calculated as

$$
E=\left(\frac{\omega_{a n}}{E_{a n}}+\frac{\omega_{a n, c c}}{E_{a n, c c}}+\frac{\omega_{c a t}}{E_{c a t}}+\frac{\omega_{c a t, c c}}{E_{c a t, c c}}+\frac{\omega_{s e p}}{E_{s e p}}\right)^{-1} \tag{28}
$$

where $\omega$ is the thickness fraction of each component referring to the total stack thickness (subscripts: an = anode; an, cc = anode current collector; cat = cathode; cat, cc = cathode current collector; sep = separator). This formulation is valid for uniaxial compression without lateral contractions. As the elasticity of both current collector foils (copper and aluminum) are three orders of magnitude higher than the expected moduli of the porous cell components, their contribution to $E$ is insignificant (eq. (29)).

$$
E \approx\left(\frac{\omega_{a n}}{E_{a n}}+\frac{\omega_{c a t}}{E_{c a t}}+\frac{\omega_{s e p}}{E_{s e p}}\right)^{-1} \tag{29}
$$

Validation measurements. A CTS cell tester (BaSyTec) was used to conduct the model validation cycles with the 10 Ah hard case cell. A temperature control unit kept the ambient temperature constant at $25^{\circ} \mathrm{C} \pm 3^{\circ} \mathrm{C}$. During the measurements the cell was fixed in a compression jig (see Fig. 2b)). A compression force was applied by the springs and monitored by C9C load cells (HBM) which were connected to an Almemo 2590-4AS (Ahlborn) data logger. An MT1281 displacement sensor in combination with a Gagechek position display unit (both Dr. Johannes Heidenhain) were used to monitor the thickness changes at the center of the cell. The force and displacement data were sampled while cycling the cell. For the stiff jig configuration the springs were replaced by steel plates.

## 4. Results and discussion

### 4.1. Pressure dependent electrolyte transport in separator

The Nyquist impedance plots of the symmetric cells with copper electrodes measured at different numbers of separator layers and pressures are shown in Fig. 3a), c). The total resistance and the corresponding ionic contribution are extracted from the impedance data and

![](./images/813069470263148547_4.jpg)

Fig. 3. Determination of the pressure dependent ionic transport in the separator between copper electrodes, using a 0.5 M TBA- PF₆ electrolyte: a) Nyquist impedance for different numbers of separators, b) separation of the ionic resistance contribution by linear fitting, c) shift of the impedance response at elevated pressures and d) pressure dependent $R_{ion}$ and transport factor $f$.

presented in Fig. 3b), d). The impedance response for each of the cells shows almost ideal capacitive behavior since the $Re\{Z\}$ is constant resulting in a straight vertical line. The total ohmic resistance $R_{tot}$ is represented by extrapolation of the impedance curve to the real axis. Fig. 3b) displays the increase of $R_{tot}$ with the thickness $t_{sep}$ of the separator layers. Since only the ionic path is varied with this method, a constant resistance contribution originating from the electrical contacts and the ohmic resistance of the electrodes are represented by the y-intercept of the linear fit (eq. (30)). To achieve sufficient accuracy three measurements at each separator thickness are performed, subsequently fitted and the standard deviation is given by the error bars.

$$
R_{tot}=6.54\ \mathrm{m}\Omega\ \mu\mathrm{m}^{-1}t_{sep}+85.8\ \mathrm{m}\Omega \tag{30}
$$

To determine $R_{ion}$, the value $85.8\ \mathrm{m}\Omega$ is subsequently subtracted from the total resistances. The pressure dependence of the impedance is visualized in Fig. 3c) where the standard deviation is indicated by error bars. The capacitive branch shifts to higher real parts which indicates the limitation of the ionic transport by the applied pressure. This is also displayed by an increase of $R_{ion}$ in Fig. 3d) and the decline of the transport factor $f$ derived by eq. (23). It can be seen that at the lowest pressure of 0.36 MPa a medium $f$ of $0.167\pm0.011$ was determined, which corresponds to a tortuosity value of $3.0\pm0.2$ (eq. (12)). Comparison with literature data indicates that the initial tortuosity of the separator is determined in the expected range. Thorat et al. obtained a value of 3.15 for a Celgard 2400 separator which has a lower porosity (0.32) than the separator used in our study [47]. However, also higher tortuosity values for the same separator material of 5.8 and lower values of 2.3 can be found [52,53]. These variances might be provoked by the specific measurement setup, which geometry and principles introduce a systematic error. Landesfeind et al. [30] comprehensively studied the tortuosity of a number of different separator types also by means of AC impedance. The most comparable to our separator in term of material, thickness and porosity reveal a tortuosity in the range of 3-4. The increasing $R_{ion}$ at higher mechanical pressure can be explained by pore compression which correlates with a growing tortuosity according to the Bruggeman relation [54,55]. The transport factor decreases approximately linear with an increasing pressure to a value of $0.102\pm0.007$ at 5.1 Mpa which corresponds to a reduction of 38.7% compared to the initial value. For application of the transport factor in our simulation model, the dashed line is used.

### 4.2. Pressure dependent electrolyte transport in electrodes

The comparison of the pressure dependent ionic transport in the electrodes is shown in Fig. 4. Fig. 4a) and c) represent the EIS spectra of anodes and cathodes, respectively, in a symmetric blocking condition at selected pressures. For better illustration $R_{hf}$ was subtracted from the impedance spectra so that each impedance curve starts at $Re\{Z\}=0$. The ionic transport is represented by a $45^{\circ}$ branch in the high frequency domain. It can be seen that below a characteristic frequency, the impedance transfers into a steep capacitive line. The deviation from an ideal capacitor can be explained by the pore structure which can be described by a constant-phase element [30]. The low frequency shift towards higher resistances upon pressure increase is associated with an elongation of the ionic path. $R_{ion}$ in Fig. 4b) and d) was derived from the pressure dependent EIS measurements by using eq. (26) and the geometric extrapolation of the capacitive branch to the x-axis. The data points in Fig. 4b) and d) represent mean values of three measurements. At a pressure of 0.18 MPa the transport factor accounts for $0.036\pm0.002$ for the anode and $0.105\pm0.004$ for the cathode. These values correspond to an anode tortuosity of $9.1\pm0.5$ and $3.0\pm0.1$ for the cathode.

Landesfeind et al. [30] also investigated different types of electrodes at various porosities, showing that the tortuosity of the flake-type graphite anode exhibits a wide range of 4-7, not significantly depending on porosity. Our result slightly exceeds this value, which can be explained by variation in microstructure properties. For an NMC cathode with a porosity of 0.34 a tortuosity of 3-4 [30] was obtained, which is comparable to our result. As already discussed for the separator, the transport factor decreases with compression since the pore volume fraction is reduced. Compared to the cathode, the ionic transport limitation in the anode with the pressure increase is more

![](./images/813069470263148547_5.jpg)

![](./images/813069470263148547_6.jpg)

![](./images/813069470263148547_7.jpg)

![](./images/813069470263148547_8.jpg)

Fig. 4. Determination of the pressure dependent ionic transport in porous anode and cathode in symmetric cells, using a 0.5 M TBA-PF₆ electrolyte: a) Nyquist impedance of the anode at selected pressures, b) pressure dependent $R_{ion}$ and transport factor $f$ of the anode, c) Nyquist impedance of the anode at selected pressures and d) pressure dependent $R_{ion}$ and transport factor $f$ of the cathode.

significant. A reduction of 31.3% at 5.1 MPa is obtained for the anode in contrast to 12.7% for the cathode. The hindering of ion transport in the porous anode structure resulting from the additional pressure and the low potential vs. $Li/Li^+$ enhance the probability of metallic Li deposition. This leads to an accelerated lithiation of the anode edge which is faced to the separator. The illustrated model functions of $f$ in Fig. 4b) and d) are used in the following simulation study.

### 4.3. Compressibility

Compression measurements were conducted in order to determine the compressibility of the porous electrodes and the separator. Fig. 5 shows the resulting experimental data for the electrode coatings and the separator. While the uncycled electrodes have never been in a functioning cell before (solid black curves), the cycled electrodes were retrieved out of cells after two initial full cycles (dashed bluish curves). At the starting point of zero deformation the compression is initiated until a maximum pressure of 3.0 MPa was reached. In all subsequently following measurements the pressure release curves show visible hysteresis where the recorded signal does not return to the initial zero level of deformation. The porous materials investigated in this study exhibit non-linear stress-strain behavior which is typical for porous polymer layers. Hence, the mechanical behavior that we see is related exclusively to the polymer nature of the separator and electrode binder materials. In contrast to the cathode (Fig. 5b)), the compressibility of the anode (Fig. 5a)) changes significantly after cycling. The observed stiffening effect is important for the practical application since the electrode material in functional cells has already been cycled and might be attributed to the formation electrolyte decomposition products. The stiffness of the materials in Fig. 5d) was obtained by the first derivative of the compression curve. Since the experimental compression curves are non-linear, the mechanical stiffness depends on pressure. A homogenized stiffness of the entire electrode compound was calculated by applying eq. (29).

While the tensile behavior of battery materials and especially the separator is extensively investigated in literature [56-59], there are only a few works on the compression properties. The research on the compression behavior of separators focuses on the influence of strain rates, electrolyte and separator base film types [58,60,61]. The importance of considering poroelastic and viscoelastic effects have been discussed [61,62]. At high strain rates $>10^{-3}s^{-1}$, which corresponds to a full charging of graphite based Li-ion battery in about 100 s and faster, the poroelastic electrolyte flow inside the porous structure plays a dominant role. However, the fastest relevant C-rate in our study is 2C (charging or discharging takes approx. 1800 s) and therefore we do not expect significant electrolyte flow effects. Based on this approximation

![](./images/813069470263148547_9.jpg)

Fig. 5. Compression measurements of a) anodes before and after formation cycles, b) cathodes before and after formation cycles and c) unused 19 μm PE separator. The cycled electrodes were retrieved out of functional cells after two initial full cycles. For disassembling the cells were discharged to SOC 0%. d) Derived element stiffness from the compression measurements of the cathode and anode electrodes after cycling and PE separator. Additionally the homogenized stack stiffness was calculated by mechanical series connection of the components.

we applied the definition of a pressure dependent elasticity for modeling. In contrast, other researches assume values of the compression modulus of Li-ion battery electrodes by using the elastic modulus of active particles which is in the magnitude of 10 GPa [12,63]. Our experimental results show that the stiffness of composite electrodes is in the order of two magnitudes smaller. Under these circumstances it can be assumed that particle deformation is negligible compared to the compression of composite microstructure which causes reduction of pore volume. The observed for our system compression behavior is well supported by the literature. Wierzbicki and co-workers [40,64] derived homogenized mechanical behavior of pouch cells and a cylindrical jellyroll for mechanically abused modeling. The compressive stress-strain curves also show a parabolic shape with a compression modulus of 45 MPa at 1.0 MPa mechanical stress. This value is comparable to the calculated stack stiffness in Fig. 5d). The observed small deviations might be attributed to different separators used in the cells as well as variations of electrode morphologies.

## 5. Simulation study

In this section, the application of the previously introduced electrochemical-mechanical model is demonstrated. While the physical input parameters for the electrodes and the separator are completely measured in-house, the description of the electrolyte bulk conductivity is based on the study carried out by Ding et al. [65]. The authors experimentally completed a full set of temperature, concentration and solvent mixture dependent conductivity functions for an LiPF₆ salt in EC and EMC mixture. Based on this study, the ionic conductivity $\varkappa_{l}$ of LiPF₆ in an ethyl carbonate and ethyl methyl carbonate mixture of 3:7 by weight was derived according to eq. (31) (units: $c_{l}$ in mol.l⁻¹, $T$ in K, $\varkappa_{l}$ in S.m⁻¹).

$$
\varkappa_{l}=c_{l}\left(-1.5262+0.00895 T-9.433 \cdot 10^{-4} T c_{l}+0.636 \exp \left(-2.6915 c_{l}\right)\right)^{2}
\tag{31}
$$

The bulk diffusivity of Li-ions in the electrolyte, required for the electrochemical model, can be calculated by applying the Nernst-Einstein relation (eq. (32)) [66]. The thermodynamic factor for the electrolyte was defined according to the work of Nyman et al. [28] by eq. (33) (unit: $c_{l}$ in mol.l⁻¹).

$$
D_{l}=\frac{\varkappa_{l} k_{B} T}{e^{2} N_{A} c_{l}}
\tag{32}
$$

$$
\left(1+\frac{\partial \ln f_{\pm}}{\partial \ln c_{l}}\right)=0,38766 c_{l}^{2}+1,0092 c_{l}+0,59599
\tag{33}
$$

The geometrical and physical parameters used for the following modeling study are summarized in Table 2. The mechanical validation of our model is performed by cell swelling and jig force measurements in a stiff and soft configurations. Table 3 represents the corresponding jig elasticities.

### 5.1. Validation of electrochemical-mechanical model

The ability of the model to predict the electrical and mechanical response of the 10 Ah hard case cell is demonstrated within this section. Therefore, the completely charged cell has been discharged at C-Rates of C/5, C/2, 1C and 2C in the stiff and in the soft configuration. Prior to the cycling experiment, the cell was constrained to a jig force of 3 kN at SOC 0% (after discharging at C/5) and the swelling was set to zero. Complete voltage and swelling profiles during this experiment under soft configuration are provided within the supplementary material (fig. S2). A constant current charging at C/2 followed by a constant voltage step until a cutoff current corresponding to C/50 was used to charge the cell. This ensures a constant cell thickness in the fully charged state. The discharging was performed at the given C-Rates. In order to perform cell swelling and jig force measurements during cycling, the setup in Fig. 2b) has been used. The comparison between the measured and simulated data (Fig. 6) shows that the model predicts both the electrical and mechanical responses of the cell with good accuracy. The experimentally obtained discharge capacities at constant currents displayed less that 1% deviation from the predicted by the model values. The swelling curves (Fig. 6 c), d)) and the jig force dependencies (Fig. 6 e), f)) reveal that stiff jig configuration leads to significant force increase

### Table 2
Geometrical and physical parameters within the porous electrode and separator domain for the mechanical-electrochemical model at 25 °C.

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Anode (graphite)</th>
<th>Separator</th>
<th>Cathode (NMC111)</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="4"><b>Geometry</b></td>
</tr>
<tr>
<td>Layer thickness $t$</td>
<td>80 μm</td>
<td>19 μm</td>
<td>84 μm</td>
</tr>
<tr>
<td>Medium particle radius $R_p$</td>
<td>11.0 μm</td>
<td></td>
<td>5.5 μm</td>
</tr>
<tr>
<td>Active material volume fraction $\phi_a$</td>
<td>0.630</td>
<td></td>
<td>0.562</td>
</tr>
<tr>
<td>Initial porosity $\phi_0$</td>
<td>0.31</td>
<td>0.49</td>
<td>0.33</td>
</tr>
<tr>
<td>Ionic transport factor $f$</td>
<td>Fig. 4b)</td>
<td>Fig. 3d)</td>
<td>Fig. 4d)</td>
</tr>
<tr>
<td colspan="4"><b>Thermodynamics</b></td>
</tr>
<tr>
<td>Equilibrium potential</td>
<td>Fig. 1a)</td>
<td></td>
<td>Fig. 1b)</td>
</tr>
<tr>
<td>Maximum Li concentration $c_{s,max}$</td>
<td>31374 mol.m⁻³</td>
<td></td>
<td>47408 mol.m⁻³</td>
</tr>
<tr>
<td>Lithiation at cell SOC of 0%</td>
<td>0.028</td>
<td></td>
<td>0.985</td>
</tr>
<tr>
<td colspan="4"><b>Kinetics</b></td>
</tr>
<tr>
<td>Double layer capacity $C_{dl}$</td>
<td>0.02 F.m⁻²</td>
<td></td>
<td>0.2 F.m⁻²</td>
</tr>
<tr>
<td>Reaction rate $k_0$</td>
<td>$2.2 × 10^{-11}$ m. s⁻¹</td>
<td></td>
<td>$9.2^{-11}$ m. s⁻¹</td>
</tr>
<tr>
<td>Charge transfer coefficient $\alpha$</td>
<td>0.5</td>
<td></td>
<td>0.5</td>
</tr>
<tr>
<td colspan="4"><b>Transport in solid phase</b></td>
</tr>
<tr>
<td>Diffusion coefficient $D_s$</td>
<td>$5.0 × 10^{-14}$ m². s⁻¹</td>
<td></td>
<td>$3.0 × 10^{-14}$ m². s⁻¹</td>
</tr>
<tr>
<td>Electrical conductivity $\kappa_s$</td>
<td>2200 S.m⁻¹</td>
<td></td>
<td>57 S.m⁻¹</td>
</tr>
<tr>
<td colspan="4"><b>Electrolyte properties</b></td>
</tr>
<tr>
<td>Equilibrium concentration $c_{l,0}$</td>
<td>1000 mol.m⁻³</td>
<td>1000 mol.m⁻³</td>
<td>1000 mol.m⁻³</td>
</tr>
<tr>
<td>Ionic conductivity $\kappa_l$</td>
<td>Eq. (31)</td>
<td>Eq. (31)</td>
<td>Eq. (31)</td>
</tr>
<tr>
<td>Diffusion coefficient $D_l$</td>
<td>Eq. (32)</td>
<td>Eq. (32)</td>
<td>Eq. (32)</td>
</tr>
<tr>
<td>Li⁺ transference number $t_+^0$</td>
<td>0.26 [28]</td>
<td>0.26 [28]</td>
<td>0.26 [28]</td>
</tr>
<tr>
<td>Thermodynamic factor $\left(1-\frac{\partial \ln f_{\pm}}{\partial \ln c_{l}}\right)$</td>
<td>Eq. (33)</td>
<td>Eq. (33)</td>
<td>Eq. (33)</td>
</tr>
<tr>
<td colspan="4"><b>Mechanics</b></td>
</tr>
<tr>
<td>Swelling</td>
<td>Fig. 1a)</td>
<td></td>
<td>Fig. 1b)</td>
</tr>
<tr>
<td>Mechanical stiffness $E$</td>
<td>Fig. 5</td>
<td>Fig. 5</td>
<td>Fig. 5</td>
</tr>
</tbody>
</table>

### Table 3
Mechanical stiffness of the compression jigs at the center position (where the swelling is measured) and the average elasticity value which is necessary to calculate the jig force evolution. The values a related to the inner thickness of the case.

<table>
<thead>
<tr>
<th>Jig configuration</th>
<th>Center</th>
<th>Average</th>
</tr>
</thead>
<tbody>
<tr>
<td>Stiff</td>
<td>30.0 MPa</td>
<td>12.7 MPa</td>
</tr>
<tr>
<td>Soft</td>
<td>1.2 MPa</td>
<td>1.0 MPa</td>
</tr>
</tbody>
</table>

during charging and a decrease during discharging. Thus, also the compression of the electrode coating in stiff configuration cells changes significantly and the outer swelling of the cell is reduced. While in case of stiff configuration the force change is about 1.5 kN at C/5 between SOC 0% and 100%, the mechanical stress in soft configuration is much smaller (180 N at C/5). This effect results in almost constant compression of the soft constrained cells (Fig. 6d)) which leads to the interesting fact that the actual swelling curve has no significant deviation compared to the unstrained swelling of the electrodes.

As the electrochmical-mechanical coupling plays a important role in automotive applications, also a drive cycle profile is evaluated for the model validation. Therefore, a driving cycle current profile, based on rural application, was interpreted by our model (Fig. 7). The 10 Ah hard case cell was tested in the soft configuration at 0.5 kN jig force. The comparison of the measured and simulated voltage and swelling curves demonstrates the accuracy by a root mean square error of 15 mV and 5 μm respectively.

### 5.2. Consequences of the electrochemical-mechanical coupling

By the mechanical-electrochemical coupling we demonstrate the impact of the pressure on the electrochemical properties of the cell. In order to check the applicability of the validated electrochemical-mechanical model, the battery function was tested during constant current constant voltage charging at 5.0 Å. In order to determine the lithiation behavior of the graphite anode we defined upon charging different constant mechanical loads of 0.4 MPa, 2.0 MPa and 4.0 MPa. The resulting porosities of the components are listed in Table 4. Fig. 8 illustrates the resulting voltage, current and electrode lithiation profiles. While the voltage and current signals are insignificantly influenced by the applied pressure, the lithiation of the anode visibly changes. The time dependence of the anode lithiation is monitored at the separator as well as at the current collector interface (Fig. 8c)). The minor influence of the pressure on the voltage profile can be explained by the dominant role of the electrochemical charge transfer overpotential and solid-state diffusion overpotential compared to those within the electrolyte phase. Nevertheless, the ionic transport in electrolyte is especially limited in the anode due to the complex morphology of the pore structure. Thereby, at these circumstances Li accumulation at the anode surface (separator interface) is becoming additionally accelerated as a consequence of the mechanical pressure and ionic transport limitation. The observed pressure-induced increase of Li concentration at the anode interface has an important safety aspect. This effect enhances the probability of metallic Li deposition if the maximum Li concentration is exceeded and correlates well with observations from other experimental studies related to a coupling between mechanical stress and aging of Li-ion cells [67,68]. Analogical effects were reported when considering SEI growth within the pores of the anode, leading to decreasing porosity and enhanced aging [69].

### 6. Conclusions

In this work the parameterization and application of a fully-coupled 1D + 1D electrochemical-mechanical model of NMC-graphite LIB was presented. The parameterization for the model coupling relations is performed by compression measurements and pressure-dependent ionic transport experiments. The compression measurements reveal a stiffening of the anode by initial cycling which might be attributed to the formation electrolyte decomposition products. While the compressibility of the anode and cathode appear in the same region, the separator compressibility is five times higher compared to the cycled anode.

Apart from the majority of researchers, using porosity and tortuosity or the Bruggeman relation to implement the effective ionic transport

![](./images/813069470263148547_10.jpg)

Fig. 6. Comparison of the measured and simulated HEV cell voltage, swelling and jig force during discharging at 2C, 1C, C/2 and C/5 rates while the cell was strained under a), c), e) stiff configuration and b), d), f) soft configuration. Computational unstrained swelling curves at C/5 are included in c) and d) for comparison.

within porous battery domains, we carried out pressure-dependent measurements to quantify the ionic transport within the electrodes and the separator. Therefore, symmetric cells were constrained at various pressures and the ionic resistance was obtained by means of EIS. The increasing ionic resistance at higher pressures can be attributed to the compression of the pore structure, resulting in porosity decrease and simultaneous tortuosity increase. The difference in the microstructures of anode and cathode induces a three times lower ionic conductivity within the anode in the initial state. The pressure dependence of the ionic transport shows that the limitation is predominant in the separator and anode domains. While the ionic conductivity in the cathode is reduced by 12.7% at 5.1 MPa, the anode (31.3%) and the separator

![](./images/813069470263148547_11.jpg)

Fig. 7. a) Current, voltage and swelling profiles in the soft jig configuration at 0.5 kN jig force for a rural drive cycle profile containing two stopovers and b) enlarged view of the low SOC region. Measurements are printed as dotted line and simulations as solid lines.

<table>
<caption>Table 4
Pressure-dependent pore volume fractions of the anode, cathode and separator, derived from the compression measurements.</caption>
<thead>
<tr>
<th>Pressure/MPa</th>
<th>Anode</th>
<th>Cathode</th>
<th>Separator</th>
</tr>
</thead>
<tbody>
<tr>
<td>w/o pressure</td>
<td>0.310</td>
<td>0.330</td>
<td>0.490</td>
</tr>
<tr>
<td>0.4</td>
<td>0.300</td>
<td>0.321</td>
<td>0.471</td>
</tr>
<tr>
<td>2.0</td>
<td>0.280</td>
<td>0.310</td>
<td>0.434</td>
</tr>
<tr>
<td>4.0</td>
<td>0.260</td>
<td>0.302</td>
<td>0.398</td>
</tr>
</tbody>
</table>

exhibit much stronger limitations (38.7%). These results demonstrate a strong coupling between the mechanical pressure and the electrochemical processes in Li-ion batteries. The intensity of this coupling depends on the mechanical properties and the microstructure of the used materials.

The determined compressibility and ionic conductivity are applied in the introduced electrochemical-mechanical model, which is validated by comparing the electrical and mechanical behavior of a 10 Ah hard case cell with the computational predictions. The real cell was cycled in a stiff and soft mechanical fixations at different swelling and jig force values. The results show very good agreement between the measured and computationally predicted values for the cell potential, swelling and jig force. Since the model validation fulfills the requirements it was further deployed to investigate the pressure-dependent charging dynamics within the electrodes. Due to the decrease of ionic conductivity in the porous structure at high pressure, the intercalation and deintercalation at the separator interface of the electrodes is becoming more accelerated and therefore, the Li concentration gradient within the electrodes increases. This effect enhances the probability of metallic Li deposition (Li plating) on the graphite surface during charging of the cell and offers one possible explanation for a mechanically linked aging behavior of Li-ion batteries.

Our model will be further extended by implementing viscoelastic and poroelastic mechanical properties of the electrodes and the separator. Furthermore, the method has potential to be updated by incorporation of thermal effects on the mechanical and electrical parameters of the system.

### Acknowledgments

The authors acknowledge the funding of this work by Robert Bosch GmbH. We thank our colleagues from the department of lithium ion batteries at the Bosch plant in Bamberg for technical support and helpful discussions.

### List of symbols

| Symbol and description | |
|------------------------|---|
| $A$ | specific active surface, $\text{m}^{-1}$ |
| $A$ | area, $\text{m}^{2}$ |
| $c$ | concentration, $\text{mol m}^{-3}$ |
| $C$ | capacity, $\text{Ah}$ |
| $D$ | diffusion coefficient, $\text{m}^{2}\text{ s}^{-1}$ |
| $E$ | mechanical stiffness, $\text{Pa}$ |
| $f$ | effective ionic transport factor |
| $f_{\pm}$ | activity |
| $F$ | Faraday constant, $\text{As mol}^{-1}$ |
| $g$ | expansion coefficient |
| $i$ | current density, $\text{A m}^{-3}$ |
| $i_{0}$ | exchange current density, $\text{A m}^{-2}$ |
| $i_{n}$ | molar current density, $\text{mol m}^{-2}\text{ s}^{-1}$ |
| $k$ | reaction rate, $\text{m s}^{-1}$ |
| $Q$ | Q-element (constant-phase-element), $\text{s}^{\gamma}\ \Omega^{-1}$ |
| $r$ | particle radius, $\text{m}$ |
| $R$ | universal gas constant, $\text{J mol}^{-1}\text{ K}^{-1}$ |
| $R_{ion}$ | ionic resistance, $\Omega$ |
| $t$ | thickness, $\text{m}$ |
| $t_{+}^{0}$ | transference number |
| $T$ | temperature, $\text{K}$ |
| $V$ | volume, $\text{m}^{3}$ |
| $z$ | number of transferred electrons |
| $Z$ | impedance, $\Omega$ |
| $\alpha$ | symmetry factor |
| $\beta$ | Bruggeman exponent |
| $\gamma$ | coefficient of constant phase element |
| $\varepsilon$ | strain |
| $\varphi$ | overpotential |
| $\phi$ | pore volume fraction |
| $\phi_{a}$ | active material volume fraction |
| $\tau$ | tortuosity |
| $\kappa$ | conductivity |
| $\chi_{Li}$ | volume change due to lithiation |
| $\omega$ | angular frequency, $\text{s}^{-1}$ |

![](./images/813069470263148547_12.jpg)

Fig. 8. Pressure-dependent simulated charging profiles with 5.0 A constant current until 4.2 V followed by constant voltage. a) voltage response, b) current profile and c) anode particle surface lithiation at the separator and current collector interfaces. Cross sectional particle surface lithiation of the anode and cathode at selected charging states at d) 0.5 MPa and e) 4.0 MPa.

Ω
molar volume, $\text{m}^3\text{mol}^{-1}$

### Subscripts
| an | anodic |
|----|--------|
| act | active material |
| an | anode |
| c | cathodic |
| cc | current collector |
| case | case |
| cat | cathode |
| l | liquid |
| p | particle |
| ref | reference |
| s | solid |
| sep | separator |
| 0 | bulk, initial |

## Appendix A. Supplementary data
Supplementary data related to this article can be found at http://dx.
doi.org/10.1016/j.jpowsour.2017.12.044.

## References
[1] J. Barker, In-situ measurement of the thickness changes associated with cycling of prismatic lithium ion batteries based on LiMn2O4 and LiCoO2, Electrochim. Acta 45 (1) (1999) 235–242.
[2] M. Majima, T. Tada, S. Ujiie, E. Yagasaki, S. Inazawa, K. Miyazaki, Design and characteristics of large-scale lithium ion battery, J. Power Sources 81–82 (1999) 877–881.
[3] J.H. Lee, H.M. Lee, S. Ahn, Battery dimensional changes occurring during charge/discharge cycles-thin rectangular lithium ion and polymer cells, J. Power Sources 119–121 (2003) 833–837.
[4] K.-Y. Oh, J.B. Siegel, L. Secondo, S.U. Kim, N.A. Samad, J. Qin, D. Anderson, K. Garikipati, A. Knobloch, B.I. Epureanu, C.W. Monroe, A. Stefanopoulou, Rate dependence of swelling in lithium-ion cells, J. Power Sources 267 (2014) 167–202.
[5] K.-Y. Oh, B. Epureanu, A novel thermal swelling model for a rechargeable lithium-ion battery cell, J. Power Sources 303 (2016) 86–96.
[6] B. Rieger, S. Schlueter, S. Erhard, J. Schmalz, G. Reinhart, A. Jossen, Multi-scale investigation of thickness changes in a commercial pouch type lithium-ion battery, J. Energy Storage 6 (2016) 213–221.
[7] S. Mohan, Y. Kim, J.B. Siegel, N.A. Samad, A.G. Stefanopouloub, A phenomenological model of bulk force in a Li-ion battery pack and its application to state of charge estimation, J. Electrochem. Soc. 161 (2014) A2222–A2231.
[8] M. Doyle, T.F. Fuller, J. Newman, Modeling of galvanostatic charge and discharge of the lithium/polymer/insertion cell, J. Electrochem. Soc. 140 (6) (1993) 1526–1533.
[9] T.F. Fuller, M. Doyle, J. Newman, Simulation and optimization of the dual lithium ion insertion cell, J. Electrochem. Soc. 141 (1994) 1–10.
[10] F. Yang, Interaction between diffusion and chemical stresses, Mater. Sci. Eng. 409 (1–2) (2005) 153–159.
[11] J. Christensen, J. Newman, Stress generation and fracture in lithium insertion materials, J. Solid State Electrochem. 10 (5) (2006) 293–319.
[12] X. Zhang, W. Shyy, A. Marie Sastry, Numerical simulation of intercalation-induced stress in Li-ion battery electrode particles, J. Electrochem. Soc. 154 (10) (2007) A910–A916.
[13] S. Golmon, K. Maute, M.L. Dunn, Numerical modeling of electrochemical-mechanical interactions in lithium polymer batteries, Comput. Struct. 87 (2009) 1567–1579.
[14] M.W. Verbrugge, Y.-T. Cheng, Stress and strain-energy distributions within diffusion-controlled insertion-electrode particles subjected to periodic potential excitations, J. Electrochem. Soc. 156 (11) (2009) A927–A937.
[15] Y.-T. Cheng, M.W. Verbrugge, The influence of surface mechanics on diffusion-induced stresses within spherical nanoparticles, J. Appl. Phys. 104 (8) (2008).
[16] S. Renganathan, G. Sikha, S. Santhanagopalan, R.E. White, Theoretical analysis of stresses in a lithium ion cell, J. Electrochem. Soc. 157 (2) (2010) A155–A163.
[17] Y. Dai, L. Cai, R.E. White, Simulation and analysis of stress in a Li-ion battery with a blended LiMn2O4 and LiNi0.8Co0.15Al0.05O2 cathode, J. Power Sources 247 (2014) 365–376.
[18] M. Klinsmann, D. Rosato, M. Kamlah, R. McMeeking, Modeling crack growth during Li extraction in storage particles using a fracture phase field approach, J. Electrochem. Soc. 163 (2) (2016) A102–A118.
[19] M. Klinsmann, D. Rosato, M. Kamlah, R.M. McMeeking, Modeling crack growth during Li insertion in storage particles using a fracture phase field approach, J. Mech. Phys. Solid. 92 (2016) 313–344.
[20] X.-G. Yang, C. Bauer, C.-Y. Wang, Sinusoidal current and stress evolutions in lithium-ion batteries, J. Power Sources 327 (2016) 414–422.

[21] R. Fu, M. Xiao, S.-Y. Choe, Modeling, validation and analysis of mechanical stress generation and dimension changes of a pouch type high power Li-ion battery, J. Power Sources 224 (2013) 211–224.
[22] K.-Y. Oh, N.A. Samad, Y. Kim, J.B. Siegel, A.G. Stefanopoulou, B.I. Epureanu, A novel phenomenological multi-physics model of Li-ion battery cells, J. Power Sources 326 (2016) 447–458.
[23] B. Rieger, S.V. Erhard, K. Rumpf, A. Jossen, A new method to model the thickness change of a commercial pouch cell during discharge, J. Electrochem. Soc. 163 (8) (2016) A1566–A1575.
[24] D. Sauerteig, S. Ivanov, H. Reinshagen, A. Bund, Reversible and irreversible dilation of lithium-ion battery electrodes investigated by in-situ dilatometry, J. Power Sources 342 (2017) 939–946.
[25] S. Tippmann, D. Walper, L. Balboa, B. Spier, W.G. Bessler, Low-temperature charging of lithium-ion cells part I: electrochemical modeling and experimental investigation of degradation behavior, J. Power Sources 252 (2014) 305–316.
[26] M. Ecker, S. Käbitz, I. Laresgoiti, D.U. Sauer, Parameterization of a physico-chemical model of a lithium-ion battery: II. model validation, J. Electrochem. Soc. 162 (9) (2015) A1849–A1857.
[27] B. Rieger, S.V. Erhard, S. Kosch, M. Venator, A. Rheinfeld, A. Jossen, Multi-dimensional modeling of the influence of cell design on temperature, displacement and stress inhomogeneity in large-format lithium-ion cells, J. Electrochem. Soc. 163 (14) (2016) A3099–A3110.
[28] A. Nyman, M. Behm, G. Lindbergh, Electrochemical characterisation and modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte, Electrochim. Acta 53 (22) (2008) 6356–6365.
[29] N.A. Zacharias, D.R. Nevers, C. Skelton, K. Knackstedt, D.E. Stephenson, D.R. Wheeler, Direct measurements of effective ionic transport in porous Li-ion electrodes, J. Electrochem. Soc. 160 (2) (2013) A306–A311.
[30] J. Landesfeind, J. Hattendorff, A. Ehrl, W.A. Wall, H.A. Gasteiger, Tortuosity determination of battery electrodes and separators by impedance spectroscopy, J. Electrochem. Soc. 163 (7) (2016) A1373–A1387.
[31] B. Suthar, P.W.C. Northrop, D. Rife, V.R. Subramanian, Effect of porosity, thickness and tortuosity on capacity fade of anode, J. Electrochem. Soc. 162 (9) (2015) A1708–A1717.
[32] M. Mastali, M. Farkhondeh, S. Farhad, R.A. Fraser, M. Fowler, Electrochemical modeling of commercial LiFePO4 and graphite electrodes: kinetic and transport properties and their temperature dependence, J. Electrochem. Soc. 163 (13) (2016) A2803–A2816.
[33] S. Pramanik, S. Anwar, Electrochemical model based charge optimization for lithium-ion batteries, J. Power Sources 313 (2016) 164–177.
[34] T. Ohzuku, Y. Iwakoshi, K. Sawai, Formation of lithium-graphite intercalation compounds in nonaqueous electrolytes and their application as a negative electrode for a lithium ion (shuttlecock) cell, J. Electrochem. Soc. 140 (1993) 2490–2498.
[35] D. Billaud, F. Henry, M. Lelaurain, P. Willmann, Revisited structures of dense and dilute stage II lithium-graphite intercalation compounds, J. Phys. Chem. Solid. 57 (6–8) (1996) 775–781.
[36] M. Winter, G.H. Wrodnigg, J.O. Besenhard, W. Biracher, P. Novák, Dilatometric investigations of graphite electrodes in nonaqueous lithium battery electrolytes, J. Electrochem. Soc. 147 (7) (2000) 2427–2431.
[37] P.M. Gomadam, J.W. Weidner, Modeling volume changes in porous electrodes, J. Electrochem. Soc. 153 (1) (2006) A179–A186.
[38] T.R. Garrick, K. Kanneganti, X. Huang, J.W. Weidner, Modeling volume change due to intercalation into porous electrodes, J. Electrochem. Soc. 161 (8) (2014) E3297–E3301.
[39] T.R. Garrick, X. Huang, V. Srinivasan, J.W. Weidner, Modeling volume change in dual insertion electrodes, J. Electrochem. Soc. 164 (11) (2017) E3552–E3558.
[40] T. Wierzbicki, E. Sahraei, Homogenized mechanical properties for the jellyroll of cylindrical lithium-ion cells, J. Power Sources 241 (2013) 467–476.
[41] D.-W. Chung, M. Ebner, D.R. Ely, V. Wood, R. Edwin García, Validity of the Bruggeman relation for porous electrodes, Model. Simulat. Mater. Sci. Eng. 21 (2013).
[42] T. Hutzenlaub, A. Asthana, J. Becker, D.R. Wheeler, R. Zengerle, S. Thiele, FIB/SEM-based calculation of tortuosity in a porous LiCoO2 cathode for a Li-ion battery, Electrochem. Commun. 27 (2013) 77–80.
[43] L. Zielke, T. Hutzenlaub, D.R. Wheeler, I. Manke, T. Arlt, N. Paust, R. Zengerle, S. Thiele, A combination of X-ray tomography and carbon binder modeling: reconstructing the three phases of LiCoO2 Li-ion battery cathodes, Adv. Eng. Mater. 4 (2014).
[44] M. Ebner, D.-W. Chung, R.E. García, V. Wood, Tortuosity anisotropy in lithium-ion battery electrodes, Adv. Eng. Mater. 4 (2014).
[45] M. Ebner, V. Wood, Tool for tortuosity estimation in lithium ion battery porous electrodes, J. Electrochem. Soc. 162 (2) (2015) A3064–A3070.
[46] G. Inoue, M. Kawase, Numerical and experimental evaluation of the relationship between porous electrode structure and effective conductivity of ions and electrons in lithium-ion batteries, J. Power Sources 342 (2017) 476–488.
[47] I.V. Thorat, D.E. Stephenson, N.A. Zacharias, K. Zaghib, J.N. Harb, D.R. Wheeler, Quantifying tortuosity in porous Li-ion battery materials, J. Power Sources 188 (2) (2009) 592–600.
[48] S.C. Carniglia, Construction of the tortuosity factor from porosimetry, J. Catal. 102 (2) (1986) 401–418.
[49] N. Ogihara, S. Kawauchi, C. Okuda, Y. Itou, Y. Takeuchi, Y. Ukyo, Theoretical and experimental analysis of porous electrodes for lithium-ion batteries by electrochemical impedance spectroscopy using a symmetric cell, J. Electrochem. Soc. 159 (7) (2012) A1034–A1039.
[50] N. Ogihara, Y. Itou, T. Sasaki, Y. Takeuchi, Impedance characterization of porous electrodes under different electrode thickness using a symmetric cell

for high-performance lithium-ion batteries, J. Phys. Chem. C 119 (9) (2015) 4612-4619.

[51] A. Lasia, Electrochemical Impedance Spectroscopy and its Applications, (2014).

[52] K.K. Patel, J.M. Paulsen, J. Desilvestro, Numerical simulation of porous networks in relation to battery electrodes and separators, J. Power Sources 122 (2) (2003) 144-152.

[53] D. Djian, F. Alloin, S. Martinet, H. Lignier, J.Y. Sanchez, Lithium-ion batteries with high charge rate capacity: influence of the porous separator, J. Power Sources 172 (1) (2007) 416-421.

[54] D.A.G. Bruggeman, Berechnung verschiedener physikalischer Konstanten von het- erogenen Substanzen. I. Dielektrizittskonstanten und Leitfhigkeiten der Mischkrper aus isotropen Substanzen, Ann. Phys. 416 (8) (1935) 665-679.

[55] J. Cannarella, C.B. Arnold, Ion transport restriction in mechanically strained se- parator membranes, J. Power Sources 226 (2013) 149-155.

[56] A. Sheidaei, X. Xiao, X. Huang, J. Hitt, Mechanical behavior of a battery separator in electrolyte solutions, J. Power Sources 196 (20) (2011) 8728-8734.

[57] J. Xu, L. Wang, J. Guan, S. Yin, Coupled effect of strain rate and solvent on dynamic mechanical behaviors of separators in lithium ion batteries, Mater. Des. 95 (2016) 319-328.

[58] X. Zhang, E. Sahraei, K. Wang, Deformation and failure characteristics of four types of lithium-ion battery separators, J. Power Sources 327 (2016) 693-701.

[59] S. Kalhaus, Y. Wang, J.A. Turner, Mechanical behavior and failure mechanisms of Li-ion battery separators, J. Power Sources 348 (2017) 255-263.

[60] G.Y. Gor, J. Cannarella, C.Z. Leng, A. Vishnyakov, C.B. Arnold, Swelling and soft- ening of lithium-ion battery separators in electrolyte solvents, J. Power Sources 294 (2015) 167-172.

[61] J. Cannarella, X. Liu, C.Z. Leng, P.D. Sinko, G.Y. Gor, C.B. Arnold, Mechanical properties of a battery separator under compression and tension, J. Electrochem. Soc. 161 (11) (2014) F3117-F3122.

[62] G. Gor, J. Cannarella, J. Prévost, C. Arnold, A model for the behavior of battery separators in compression at different strain/charge rates, J. Electrochem. Soc. 161 (11) (2014) F3065-F3071.

[63] W. Wu, X. Xiao, X. Huang, S. Yan, A multiphysics model for the in situ stress analysis of the separator in a lithium-ion battery cell, Comput. Mater. Sci. 83 (2014) 127-136.

[64] E. Sahraei, R. Hill, T. Wierzbicki, Calibration and finite element simulation of pouch lithium-ion batteries for mechanical integrity, J. Power Sources 201 (2012) 307-321.

[65] M.S. Ding, K. Xu, S.S. Zhang, K. Amine, G.L. Henriksen, T.R. Jow, Change of con- ductivity with salt content, solvent composition, and temperature for electrolytes of LiPF6 in ethylene carbonate-ethyl methyl carbonate, J. Electrochem. Soc. 148 (10) (2001) A1196-A1204.

[66] M. Ecker, T.K.D. Tran, P. Dechent, S. Käbitz, A. Warnecke, D.U. Sauer, Parameterization of a physico-chemical model of a lithium-ion battery: I. de- termination of parameters, J. Electrochem. Soc. 162 (9) (2015) A1836-A1848.

[67] J. Cannarella, C.B. Arnold, Stress evolution and capacity fade in constrained li- thium-ion pouch cells, J. Power Sources 245 (2014) 745-751.

[68] T.C. Bach, S.F. Schuster, E. Fleder, J. Müller, M.J. Brand, H. Lorrmann, A. Jossen, G. Sextl, Nonlinear aging of cylindrical lithium-ion cells linked to heterogeneous compression, J. Energy Storage 5 (2016) 212-223.

[69] X.G. Yang, Y. Leng, G. Zhang, S. Ge, C.Y. Wang, Modeling of lithium plating induced aging of lithium-ion batteries: transition from linear to nonlinear aging, J. Power Sources 360 (2017) 28-40.