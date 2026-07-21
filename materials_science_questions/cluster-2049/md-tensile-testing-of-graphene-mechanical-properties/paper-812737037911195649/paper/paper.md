# Evaporation-driven crumpling and assembling of two-dimensional (2D) materials: A rotational spring - mechanical slider model

Qingchang Liu $^{a}$, Jiaxing Huang $^{b}$, Baoxing Xu $^{a,*}$

$^{a}$ Department of Mechanical and Aerospace Engineering, University of Virginia, Charlottesville, VA 22904, USA
$^{b}$ Department of Materials Science and Engineering, Northwestern University, Evanston, IL 60208, USA

---

## ARTICLE INFO

**Article history:**
Received 16 June 2019
Revised 9 August 2019
Accepted 10 September 2019
Available online 10 September 2019

**Keywords:**
Aerosol-like evaporation
2D materials
Crumpling
Self-assembling
Spring-slider model
Coarse-grained modeling

---

## ABSTRACT

Crumpling of suspended two-dimensional (2D) materials by droplet evaporation creates a new form of aggregation-resistant ultrafine particles with more scalable properties such as high specific surface areas. However, the underpinned fundamental mechanics theory that addresses large deformation, severe instability and self-assembly of 2D sheets under dynamic solid-liquid interactions during liquid evaporation is lacking. In the present study, we propose a theoretical mechanics framework to quantitatively describe the simultaneous process of crumpling and self-assembling of 2D materials and their competition during droplet evaporation. In this theory, a rotational spring is developed to describe the out-of-plane deformation of crumpling sheets, and a mechanical slider is implemented to describe the interactive binding energy in self-folding of a single sheet or overlapping of neighboring sheets. The spring-slider mechanics model is calibrated with the energy-based continuum mechanics analysis by crumpling a single sheet, and is further extended to a network model to characterize the crumpling and assembling of multiple sheets in the droplet. An equivalent pressure model is developed to unify the resultant forces associated with liquid evaporation including capillary force, vapor pressure, gas pressure, vapor recoil pressure and capillary flow-induced force. A coarse-grained model of 2D materials is developed and its dynamic interaction with liquid molecules during evaporation is mimicked by proposing a controllable virtual van der Waal force field. Molecular dynamics simulation results show remarkable agreement with theoretical predictions, from crumpling and assembling energies of graphene during liquid evaporation to overall size and accessible area of the crumpled particles after the complete evaporation of liquid. Besides, both theoretical predictions and simulation results agree well with independent experiments. The effect of concentration, size, shape, number and size distribution of 2D material graphene sheets in liquid droplets on crumpling and self-assembling energy and shape, size and surface morphology of crumpled particles is also discussed. The mechanics theories and coarse-grained modeling established here are expected to offer immediate and quantitative application guidance to control the crumpling and self-assembling process of 2D materials by liquid solution evaporation processing to fine tune particle size and morphology. More importantly, the fundamental understanding of large deformation, instability, and self-assembly of 2D materials in such dynamic liquid environments could be extended to aerosol-like processing of a broad scope of other low-dimensional nanomaterials such as lipid membranes, nanowires, nanotubes, nanofibers and nanoparticles, for their emerging applications including ultrafine particle manufacturing and various printing processes.

© 2019 Elsevier Ltd. All rights reserved.

---

https://doi.org/10.1016/j.jmps.2019.103722
0022-5096/© 2019 Elsevier Ltd. All rights reserved.

### 1. Introduction

Two-dimensional (2D) materials, such as graphene, boron nitride and molybdenum disulfide, have attracted tremendous attention over the past few years for their exceptional electronic, mechanical and thermal properties underpinned by their extremely large specific surface area (Akinwande et al., 2017), often demonstrated at the single layer level. However, a bulk form of these 2D materials, either as powders or a monolith is necessary for most applications such as high-performance electrodes in energy storage (Cao et al., 2014; Fan et al., 2015; Shehzad et al., 2016), filters for waste water/gas treatments in environmental systems (Lim et al., 2017; Sudeep et al., 2013), and lightweight structures (Qin et al., 2017; Qiu et al.,2012; Wu et al., 2015). A significant thrust in recent years is to assemble these atomically thin materials into some bulk, three-dimensional (3D) forms in the hope that the excellent properties at single layer level can be scaled up as much as possible (Luo et al., 2015). The major issue in the assembly is that the 2D nanomaterials tend to aggregate/restack due to strong van der Waals attraction between them such as restacking of 2D flat graphene sheets, which not only results in a tremendous reduction of their accessible surface area and poor mass/ion transport (Yavari et al., 2011; Zhang et al., 2013; Zou and Kim, 2014), but also degrades with processing and/or application environments such as mechanical loadings, hence adversely affecting their properties and subsequent applications (Li et al., 2015; Luo et al., 2013b; Yang et al., 2013). Several manufacturing techniques have been developed to obtain the 2D nanomaterials based 3D structures including mechanical folding by applying an external mechanical loading (Diamant and Witten, 2011; Jambon-Puillet et al., 2016; Jin et al., 2015), and chemical folding by decorating functional groups (Zheng et al., 2010) or defects (Warner et al., 2012). For example, releasing pre-strain applied to the substrate prior has been designed to achieve wrinkled graphene patterns (Zhang and Arroyo, 2014) and has also been used to pop up 3D graphene porous structures (Ling et al., 2018). Similar to this mechanical controlling means, thermally generated strain (Bao et al., 2009), hydrogenation (Reddy and Zhang, 2014) and irradiation to surface atoms (Warner et al., 2013) have been developed to regulate 2D structures of graphene into various geometrical configurations. These manufacturing techniques are currently challenged by mass productions of 2D nanomaterials based 3D structures with a low cost to meet requirements for broad applications.

As an alternative manufacturing approach, an aerosol-assisted fabrication of crumpled graphene balls has been developed that can convert suspended 2D materials into crumpled paper ball-like structure. (Luo et al., 2015, 2011; Xu and Rogers, 2016). Fig. 1a depicts the schematic illustration of a typical experimental setup of the aerosol-assisted, evaporation-driven manufacturing technique (Hao et al., 2018; Luo et al., 2011, 2012; Mao et al., 2012; Yang et al., 2016). The aerosol droplets with suspended 2D materials are first nebulized from a bulk dispersion, and then sent through a pre-heated furnace via a carrier gas. At the end of the fly path, evaporation of the aerosol droplets is complete and dried particles are collected. By adjusting concentration of 2D sheets and/or the furnace temperature, the size and morphology of assembled particles can be tuned (Jiang et al., 2016; Kavadiya et al., 2017; Luo et al., 2015, 2011; Nie et al., 2017; Parviz et al., 2015), as shown in the representative electron microscopy images of crumpled graphene balls in Fig. 1b. The crumpled graphene balls could exhibit both high free volume and high compressive strength, and can pack tightly without significant reduction of the original accessible area of graphene (Luo et al., 2011). For example, unlike a tight restacking of flat graphene sheets, $\sim$60% of the accessible surface area ($>1500$ m²/g) is maintained in the crumpled graphene sheets (Cranford and Buehler, 2011). The crumpled graphene-assembled structures can even maintain 45% of its original surface area under mechanical compression of 55 MPa, while the regular flat graphene sheets turn into chunks with a drastic reduction of surface area by 84% (Luo et al., 2013a). The excellent inherence of large surface areas and robust deformation resistance in crumpled graphene 3D structures have been leveraged in supercapacitors and show five times higher of energy density than that of flat graphene sheet powder and a stable specific capacitance with the increase of mass loading (Tao et al., 2013). More importantly, 2D sheets such as those made of graphene, are usually hard to disperse in solvents due to their strong tendency to restack. However, for their crumpled version, the uneven surface morphology, coupled with strain-hardening property leads to unusual aggregation-resistant properties, allowing them to be processed in nearly arbitrary solvents without the need for dispersing agents (Luo et al., 2013b). Crumpled graphene balls were found to self-disperse in lubricant oil for improved tribological performance and wear protection (Dou et al., 2016). The scalable surface areas in crumpled graphene balls have exhibited more scalable performance in ultracapacitors (Ha et al., 2019; Luo et al., 2013a; Zang et al., 2014). Their uneven surface morphology and aggregation-resistant packing behavior have been leveraged to reduce the reflection of light for solar heating and distillation purposes (Hao et al., 2018). The 3D porous spaces have also been employed as a scaffold to enhance the sensitivity of sensors (Chen et al., 2017b) and catalytic performance (Zhou et al., 2016) with rapid diffusion of atoms/ions and mass transfer. In addition, the 3D spatial networks facilitate the interlocking and interactions with host matrixes in Li-metal batteries (Liu et al., 2018) and manufacturing of 2D nanomaterial-reinforced composites and enhance overall physical and mechanical properties (Deng and Berry, 2016; Ramanathan et al., 2008). Crumpled graphene balls can also act as breathable shells to encapsulate and protect expandable particles from reactive environments, which has been leveraged for applications in energy storage devices such as Li-ion battery (Choi et al., 2014; Luo et al., 2012; Mao et al., 2012; Park et al., 2015; Parviz et al., 2015). Recently, the liquid evaporation-driven manufacturing technique has been applied in the crumpling and assembly of other 2D materials such as MoS₂ flakes (Chen et al., 2017a).

* Corresponding author.
E-mail address: bx4c@virginia.edu (B. Xu).

![](./images/812737037911195649_1.jpg)

Fig. 1. Liquid evaporation-driven crumpling and assembling of two-dimensional (2D) deformable nanomaterials. (a) Schematics of the popular experimental setup for the liquid evaporation-induced crumpling and assembling of 2D nanomaterials to bulk forms (Hao et al., 2018; Luo et al., 2011, 2012; Mao et al., 2012; Yang et al., 2016). The liquid droplets consisting of 2D materials and solvent liquid solution are generated by atomization and sent into the high-temperature furnace with the help of carrier gas for liquid evaporation. The assembled solid particles are collected at the outlet of the furnace. (b) Electron microscopy images of four assembled graphene oxide particles at different concentration of graphene oxide ($C_m$) and furnace temperature ($T_f$). (I) $C_m$=0.2 mg/ml,$T_f$=100°C (Luo et al., 2011)and (II) $C_m$=1 mg/ml ,$T_f$=100°C (Luo et al., 2011), (III) $C_m$=2 mg/ml, $T_f$=350°C and (IV) $C_m$=2 mg/ml, $T_f$=750°C (Yang et al., 2016). (c) Schematic illustrations of the crumpling and assembling process of 2D material sheet by liquid evaporation. (I) uniform distribution of multiple 2D sheets suspended in the liquid droplet after atomization. (II) 2D sheets immigrate to the surface of liquid droplet with the initial evaporation of liquid due to the capillary flow and/or amphiphilicity. (III) 2D sheets crumple and assemble with the continuous evaporation of liquid. (IV) 2D sheets further assemble and self-fold until the complete evaporation of liquid, and a solid particle is generated.

In fundamental, this liquid evaporation manufacturing technique is similar to self-assembly of nanoparticles in the synthesis of colloidal crystals, nevertheless, nanoparticles are commonly rigid and only aggregation is expected by inter-particle attraction to achieve dense-packed assembly of nanoparticles (Lauga and Brenner, 2004; Vogel et al., 2015). By contrast, the 2D materials are prone to occur an out-of-plane deformation due to an atomic thickness. It is hypothesized that 2D nanomaterials will experience large deformation and severe instability under evaporation-induced compression to create spacing when assembled, thereby minimizing restacking and retaining the large surface areas of 2D nanomaterials in the assembled 3D structures, which is closely underpinned by mechanics. Besides, from energy variation point of view, the ultimate morphology of assembled 3D particles is expected to be determined by the energy competition between crumpling (geometric frustration including wrinkling and self-folding) and assembling (compaction) of 2D materials and could be tuned by changing the concentration, size and shape of 2D materials and external environment (e.g. furnace temperature or evaporation rate, and flow speed of carrier gas), which is highly needed in the exploration of controllable manufacturing through key material and systemic parameters. Fig. 1c illustrates the schematics of crumpling and assembling process of 2D materials by liquid evaporation. We should note that the accumulated distribution of 2D materials in the surface of droplets is led by the evaporation-induced capillary flow (Deegan et al., 1997; Kim et al., 2010; Shim et al., 2014; Tarasevich, 2005) in the high-temperature furnace, and/or amphiphilicity of the sheets (Kim et al., 2010; Krueger et al., 2011) that can be adjusted by controlling the pH of solution or the size distribution of the sheets (Kim et al., 2010). However, the traditional self-assembly

mechanics in colloid science that focuses on aggregation among non-deformable rigid 1D nanoparticles is limited to un- derstanding the large deformation, instability and assembly of 2D deformable materials during liquid evaporation, and the mutual competitions and coordination between deformation and assembly under dynamically-constrained boundary condi- tions cannot be captured by traditional colloid theory.

In the present study, we will ascertain and establish a theoretical mechanics framework for the liquid evaporation-driven crumpling and assembling of 2D deformable materials suspended in a free-standing liquid droplet, as illustrated in Fig. 1a for the experiment setup, and further develop a coarse-grained modeling to conduct large-scale molecular dynamics sim- ulations and validate the proposed mechanics theory, in parallel with comparison of theoretical and computational results with experimental results. The details of the theoretical framework are given in Section 2. An equivalent pressure model is first developed to unify the driving forces of crumpling and assembling 2D materials including capillary force, carrier gas pressure, vapor pressure, vapor recoil pressure and capillary flow-induced shear force. Then, a rotational spring-mechanical slider model is proposed to describe mechanical deformation and self-folding of individual 2D sheets and their self-assembly during evaporation. The resultant energies are derived to quantitatively elucidate the energy competition between crum- pling and self-assembly of 2D materials. By minimizing the ultimate energy state after complete evaporation of liquid, the morphology and size of assembled 3D particles are also predicted in theory. A high-efficiency coarse-grained modeling is developed to conduct large-scale molecular dynamics simulations and validate the proposed theoretical model in Section 3. Graphene is taken as a representative of 2D deformable materials and is modeled by a coarse-grained model. A controllable virtual spherical force field that exerts on graphene is developed to mimic the liquid evaporation-induced pressure, thereby significantly reducing computational cost yet with high accuracy. The quantitative comparison between simulations and the- oretical predictions are presented in Section 4, including deformation, crumpling and assembling energies of graphene with liquid evaporation and morphology evolution of assembled graphene. The size and accessible area of assembled particles from both theoretical and simulations results are obtained with excellent agreement with each other and also agree well with experiments in literatures. The extension of the proposed theory that takes into account the numbers, size distribu- tion and geometric shapes of graphene sheets in the droplet is further discussed in Section 5 and the results show good consistency with simulations and experiments. The concluding remarks are given in Section 6.

## 2. Theoretical framework

### 2.1. Equivalent evaporation pressure model of liquid evaporation-induced forces

As illustrated in Fig. 1c, the liquid droplet of solution suspension is first generated by atomization (Fig. 1c (I)) and once the liquid evaporation occurs at an elevated temperature in the furnace, the 2D sheets will be gradually in contact with the vapor air and immigrate to the surface of droplet due to intrinsic amphiphilicity of 2D sheets (Fig. 1c (II)) (Kim et al., 2010; Okuyama and Wuled Lenggoro, 2003). Besides, these 2D sheets at solid-liquid interface will lead to certain constraints to other 2D sheets inside the droplet, similar to the pin effect of substrate to nanoparticles in coffee-ring phe- nomena (Deegan et al., 1997), which generates a capillary flow with evaporation, and in turn, promotes immigration of 2D sheets to the surface of the droplet. As a consequence, the evaporation of liquid molecules will result in a recoil force at the liquid-vapor interface and it is perpendicular to the interface squeezing the interface toward the liquid side (Nikolayev et al., 2006). This recoil force will bend the 2D sheets around the center of liquid droplet and influences the deformation and as- sembly of the 2D sheets. At the same time, similar to a pressure increase led by the heated carrier gas in the relatively sealed tube furnace, the liquid vapor will lead to an increase of the pressure, and in turn promotes the deformation and self-assembly of 2D sheets. Besides, the dynamics flow of liquid around 2D sheets, often referred to as capillary flow, will lead to a shear force exerting on the contact surface of 2D sheets with liquid droplet (Schmatko et al., 2005). In addition, the capillary force along the tangential direction of liquid at the contact line between solid and liquid will further promote the deformation of 2D sheets (Hure and Audoly, 2013; Liu and Xu, 2018; Paulsen et al., 2015). Fig. 2a (I) illustrates the directions and locations of these forces which are all led by liquid evaporation. Under these forces, the 2D sheets will be crumpled till to the complete evaporation of liquid. In our analysis, these driving pressures and forces will be unified to a generalized equivalent pressure to describe the crumpling and self-assembly of 2D sheets.

Specifically, once the liquid droplet is sent to the high-temperature furnace by a carrier gas, the carrier gas will be heated, leading to an increase of pressure ($P_g$) in the furnace. Based on the ideal gas law, the gas pressure is (Vincenti and Kruger, 1965)

$$
P_{g}=\frac{P_{0} T_{f}}{T_{0}} \tag{1}
$$

where $P_0$ and $T_0$ are the pressure and temperature of the carrier gas at the inlet of furnace, respectively, and $T_f$ is the furnace temperature. For the liquid droplet, when flying through the high-temperature furnace, the liquid phase will be changed into the vapor phase by direct vaporization to liquid on the surface of droplet and possibly by cavitation to liquid near the 2D sheets inside the droplet at very high temperature of evaporation (e.g. $T_f \gg T_b$), and leads to an increase of the vapor pressure in the furnace. Besides, the resultant instant pressure or dynamic impact to the suspended 2D sheets due

![](./images/812737037911195649_2.jpg)

Fig. 2. Equivalent model of evaporation pressure for assembling and crumpling of 2D nanomaterials by liquid evaporation. (a) Schematic illustrations of the various resultant forces (including both direction and location) exerted on a 2D sheet by liquid evaporation (I) and its total equivalent pressure (II). The gas pressure of thermally expanded carrier gas ($P_g$) and vapor pressure ($P_v$) act on the surface of 2D sheet, and their direction both are perpendicular to the surface of 2D sheet; The capillary force ($F_c$) acts on the boundary of 2D sheet pointing to the tangential direction of the liquid surface; The vapor recoil pressure ($P_r$) acts on the boundary of solid, and it is perpendicular to the tangential direction of the liquid surface; The shear stress ($P_s$) acts on the inner side of 2D sheet, and it is parallel to the surface of 2D sheet. In the total equivalent pressure ($P_t$) model, it acts on the surface of solid in perpendicular to the surface of 2D sheet. (b) Variation of various resultant forces exerted on a square 2D sheet with area $A_g = 0.1\ \mu m^2$ as a function of furnace temperature ($T_f$). Both $P_r$ and $P_s$ are at least three orders of magnitude lower than $P_g$, $P_v$ and $P_c$ and are not included in the following analysis of $P_t$. (c) Total equivalent evaporation pressure exerted on square 2D sheet with different areas $A_g$ versus furnace temperature ($T_f$).

to breakage of cavitation can be neglected due to the good flexibility of 2D sheets and their free motion inside the liquid. Assuming all the liquid in the droplet is vaporized, the resultant vapor pressure ($P_v$) can be calculated using the ideal gas law, similar to $P_g$ in Eq. (1), and it is

$$
P_{v}= \begin{cases}\frac{n R T_{f}}{V}, & \left(T_{f} \geq T_{b}\right) \\ 0, & \left(T_{f}<T_{b}\right)\end{cases} \tag{2}
$$

where $n$ is the amount of vapor, $R$ is the ideal gas constant, $V$ is the volumetric capacity of furnace, and $T_b$ is the boiling point of solution liquid. We should note that the droplet size generated by atomization is usually at the microscale and the enhancement of vapor pressure due to the curvature of liquid droplet surface, usually named as Kelvin effect (Thomson, 1872), can be neglected because such effect becomes significant only when the radius of droplet ($R_d$) is less than 10 nm. In addition to $P_v$, the generation of liquid vapor will lead to a vapor recoil pressure ($P_r$) that exerts on the boundary of 2D sheets. The vapor recoil pressure $P_r$ depends on both droplet size and furnace temperature and can be

determined by (Nikolayev et al., 2006)

$$
P_{r}=q^{2}\left(\frac{1}{\rho_{v}}-\frac{1}{\rho_{l}}\right)
\tag{3}
$$

where $q=m_{d}/A_{d}t_{e}$ represents the mass evaporation rate of liquid, $m_{d}$ is the mass of liquid droplet, $A_{d}$ is the total surface area of liquid droplet, and $t_{e}$ is the evaporation time. $\rho_{v}$ and $\rho_{l}$ are the density of vapor and liquid, respectively.

Unlike the constant loading direction of gas and vapor pressure that vertically exerts on the surface of 2D materials, the capillary force $(F_{c})$ that appears at the solid-vapor-liquid interface changes its direction dynamically due to free suspension of 2D sheets in the droplet and its contribution to deformation of 2D sheets can be evaluated by an equivalent pressure $(P_{c})$. For a free-standing deformable sheet suspended in a liquid droplet, its centroid will not deform and can be taken as a constraint reference point. Consider an entire 2D sheet composed of infinite numbers of cantilever beams with the fixed centroid, with the principle of deflection of beam, the capillary force applied at the free ends can be equivalent to a pressure exerted on the surface (Li et al., 2010) (Fig. A1). For example, for a cantilever beam of rectangular shaped 2D materials with a length $l$ and width $w$, the capillary force $(F_{c}=\gamma_{l}w)$ that acts at the free end of 2D sheet due to the receding of liquid by evaporation will generate a deflection $\delta_{F}=F_{c}l^{3}/3EI$ (Hibbeler, 2011; Li et al., 2010), where $E$ is Young's modulus and $I$ is the moment of inertia of the cross section of 2D sheets. For comparison, when a uniform pressure $P_{c}$ is applied to the beam, the beam will have a deflection at the free end, $\delta_{P}=P_{c}wl^{4}/8EI$. $\delta_{F}=\delta_{P}$ will yield $P_{c}=8F_{c}/3lw$, which leads to an equivalence between capillary force and uniform pressure for the mechanical deformation of beam. Similarly, we can have $P_{c}=16\gamma_{l}/3L_{g}$, $P_{c}=32\gamma_{l}/3\sqrt[4]{3}L_{g}$, and $P_{c}=16\gamma_{l}/3L_{g}$ for a square, and triangular, and circular 2D sheets, respectively, where $\gamma_{l}$ is the surface tension of liquid and $L_{g}$ is the size of 2D material (i.e. length of square and equilateral triangular, and diameter of circular shaped 2D sheets). As a result, the equivalent pressure that could be used to replace the capillary force can be summarized as $P_{c}=16S\gamma_{l}/3L_{g}$, where $S$ is a dimensionless geometric factor of 2D sheets ($S$=1 for square and circular 2D sheets, $S=2/\sqrt[4]{3}$ for triangular 2D sheets). Further, the surface tension of liquid solution in the droplet usually is a function of temperature (Freire et al., 2007; Sugden, 1924), and for example, the surface tension of water is $\gamma_{w}(T)=$ $94.74+1.87 \times 10^{-3}T-2.63 \times 10^{-4}T^{2}$ (mN/m) between 273 and 373 K (Chen and Smith, 2007). Therefore, the equivalent pressure to the capillary force for driving deformation of 2D sheet by liquid evaporation can be written as

$$
P_{c}=
\begin{cases}
S\frac{16\gamma_{l}(T_{f})}{3L_{g}}, & T_{f} \leq T_{b} \\
S\frac{16\gamma_{l}(T_{b})}{3L_{g}}, & T_{f} > T_{b}
\end{cases}
\tag{4}
$$

Besides the capillary force, the dynamic interaction between 2D sheets and liquid during liquid evaporation will generate a capillary flow along the surface of 2D sheets. The convection of liquid between the inside and on the surface of droplet will lead to a capillary flow and exert a shear stress to the 2D sheets in contact with the liquid droplet. The capillary flow-induced shear stress is (Liu and Xu, 2016)

$$
P_{s}=\mu v_{l}
\tag{5}
$$

where $\mu$ is the friction coefficient between 2D sheets and liquid, and $v_{l}$ is the velocity of liquid flow on the surface of 2D sheets. For a given liquid and 2D sheets, $\mu$ can be determined from the solid-liquid interaction (Tocci et al., 2014) and $v_{l}$ can be estimated via the evaporation rate of liquid (Deegan et al., 1997; Hu and Larson, 2005).

With these analyses in Eqs. (1)-(5), the total equivalent evaporation pressure that could drive crumpling and assembly of 2D sheets by liquid evaporation can be summarized to

$$
P_{t}=P_{g}+P_{v}+P_{r}+P_{c}+P_{s}
\tag{6}
$$

Take a square 2D graphene sheet with an area $A_{g}=0.1\ \mathrm{\mu m^{2}}$ and liquid water as an example, and set $T_{0}$=300 K and $P_{0}$=1 atm, $n$=0.01 mol, $V=3 \times 10^{-4}\ \mathrm{m^{3}}$ and $R_{d}=1.45\ \mathrm{\mu m}$, Fig. 2b shows these forces as a function of the furnace temperature $(T_{f})$ and all of them are temperature dependent. Compared with $P_{g}$, $P_{v}$ and $P_{c}$, both $P_{r}$ and $P_{s}$ are at least three orders of magnitude lower, and thus will not be included in the following discussion unless otherwise stated; that is, Eq. (6) reduces to

$$
P_{t}=P_{g}+P_{v}+P_{c}
\tag{7}
$$

In addition, both $P_{g}$ and $P_{v}$ increase with the furnace temperature, and $P_{c}$ remains constant because the temperature has exceeded the boiling point of liquid water ($T_{b}$=100 °C) and the temperature of liquid water will not change. Fig. 2b further shows that the evaporation pressure $(P_{t})$ increases with the increase of furnace temperature, indicating that a high temperature will benefit the crumpling and assembling of 2D materials (Wang et al., 2012). When the size of 2D materials changes, Fig. 2c shows the variation of the evaporation pressure $(P_{t})$ with the furnace temperature, and crumpling a smaller 2D material requires a higher evaporation pressure. It should be noted that when the 2D sheets are highly hydrophilic or the liquid solution of 2D sheets is highly diluted, all 2D sheets might stay inside the droplet (Kim et al., 2009) during early stage of evaporation, and the evaporation will condense the solution droplet, which could lead to the crumpling and self-assembly of 2D sheets by self-constraint each other due to the incompressibility of liquid, similar to the forced crumpling of elastic sheets in an impenetrable rigid cylinder (Vliegenthart and Gompper, 2006). As the evaporation continues, once 2D sheets are in partial contact with vapor air, the driving force will be dominated by pressures such as capillary force as shown in

![](./images/812737037911195649_3.jpg)

Fig. 3. Evolution of deformation morphology of a single 2D sheet by liquid evaporation. (a) Schematic illustrations of typical deformation of a single 2D sheet on the surface of liquid droplet with the evaporation of liquid (represented by a decreased radius of liquid droplet $(R_d)$ with the evaporation time). The evaporation of liquid will drive the deformation of the 2D sheet on the liquid droplet. (b) Deformation transition of 2D sheet from (I) the initial fully conformal state with only in-plane compression within the sheet (inset), to (II) the local out-of-plane wrinkling deformation (highlighted in red and can be described by a cosinusoidal wave function with wavelength $\lambda_{w}$ and amplitude $A_{w}$, inset) state in the sheet along the axisymmetric axis and to (III) the final local self-folding deformation highlighted in red. With the help of geometric analysis (inset), it can be well defined with geometric parameters via arc radius and angles $R_{1}, R_{2}, R_{3}, \theta_{1}, \theta_{2}, \theta_{3}$, and the interlayer distance $(h)$ and overlapping length $(l_{b})$ are used to describe the deformed profile state at wrinkled locations. .

Fig. 2a, which could lead to formation of intensely crumpled solid-like balls or restacking of 2D sheets after complete evaporation of liquid. In addition, at elevated temperatures, the evaporation rate will become high, but we assume that there still is enough time to allow 2D materials to be crumpled and assembled during liquid evaporation.

### 2.2. Energy-based continuum mechanics model for crumpling a single 2D sheet

When planar 2D sheets are in contact with surface of the liquid droplet, their curvature mismatch will lead to energy competition between mechanical deformation of 2D sheets and solid-liquid interaction. As a consequence, the deformation of 2D sheets such as local wrinkling will occur, as illustrated in Fig. 3a (King et al., 2012; Zhou et al., 2015) and may eventually transform to folding with the continuous evaporation of liquid. Take a single square 2D sheet with length $L_g$ in the liquid droplet with a radius $R_d$ as an example, and consider the evaporation-induced pressure of $P_r$, the compressive hoop strain in the 2D sheet is axisymmetric and can be estimated via

$$
\varepsilon_{\theta \theta}(r)=\frac{R_{d} \sin \left(r / R_{d}\right)-r}{r}, \quad r \in\left[0, L_{g} / 2\right] \tag{8}
$$

where $r$ is the local radial coordinate on the 2D sheet (Fig. A2c). Note that there is no radial strain in the 2D sheet because of the free boundary in the radial direction. With Eq. (8), for the 2D sheet, the strain energy of a fully conformal thin torus

with the width $dr$ in the position $r$ (Fig. A2c) is

$$
E_{s}^{I}=\pi E t \varepsilon_{\theta \theta}^{2} r d r+\frac{B \pi}{R_{d}^{2}} r d r
\tag{9}
$$

where the first term on the right hand is the in-plane compressive energy and the second term is the bending energy. $t$ is the thickness, and $B$ is the bending stiffness of 2D sheet. Consider the center of liquid droplet as a reference point, the potential energy of the thin torus under $P_{t}$ is

$$
E_{p}^{I}=2 \pi P_{t} R_{d} r d r
\tag{10}
$$

with Eqs. (9) and (10), the total energy that is required to keep a fully conformal torus for 2D sheet at the position $r$ is $E_{t}^{I}=E_{s}^{I}+E_{p}^{I}$.

With the liquid evaporation (i.e. a smaller $R_{d}$), $|\varepsilon_{\theta \theta}|$ will increase and wrinkles in the 2D sheet will occur, primarily along the symmetric axis in a square 2D sheet, as highlighted in red in Fig. 3b. Once the wrinkles appear, the compressive strain will be released by the out-of-plane wrinkling deformation (King et al., 2012), and the morphology of the wrinkled parts can be described by a cosinusoidal wave function with the wavelength $\lambda_{w}$ and amplitude $A_{w}$ (Brau et al., 2013; Oshri et al., 2015; Zhang and Yin, 2018), $f(x)=A_{w} \cos (\frac{2 \pi}{\lambda_{w}} x)+A_{w}$, where $x$ is the local coordinate on the surface of liquid droplet (Fig. 3b) and the conservation of length of torus at the position $r$ requires $4 \int_{-\lambda_{w} / 2}^{\lambda_{w} / 2} \sqrt{1+(d f / d x)^{2}} d x+2 \pi R_{d} \sin (r / R_{d})-4 \lambda_{w}=2 \pi r$. Thus, we can calculate the strain energy within the torus via

$$
E_{s}^{I I}=2 B\left[\int_{-\lambda_{w} / 2}^{\lambda_{w} / 2} \kappa^{2}(x) \sqrt{1+(d f / d x)^{2}} d x+\left(2 \pi R_{d} \sin \left(r / R_{d}\right)-4 \lambda_{w}\right) / 4 R_{d}^{2}\right] d r
\tag{11}
$$

where $\kappa(x)=|d f^{2} / d x^{2}| /(1+(d f / d x)^{2})^{3 / 2}$ is the local curvature of wrinkles. Similar to Eq. (10), the potential energy due to wrinkle can be obtained via

$$
E_{p}^{I I}=P_{t}\left[4 \int_{-\lambda_{w} / 2}^{\lambda_{w} / 2}\left(f(x)+R_{d}\right) \sqrt{1+(d f / d x)^{2}} d x+\left(2 \pi R_{d} \sin \left(r / R_{d}\right)-4 \lambda_{w}\right) R_{d}\right] d r
\tag{12}
$$

Therefore, the total energy for the wrinkling deformation is $E_{t}^{I I}=E_{s}^{I I}+E_{p}^{I I}$ and is a function of $\lambda_{w}$. The minimization of $E_{t}^{I I}$ can be used to determine $\lambda_{w}, A_{w}, E_{s}^{I I}$ and $E_{p}^{I I}$.

With the further evaporation of liquid, $|\varepsilon_{\theta \theta}|$ and the amplitude of wrinkles $A_{w}$ will continue to increase (Diamant and Witten, 2011). Beyond a critically high enough $|\varepsilon_{\theta \theta}|$, the wrinkles will transit to folds, and the deformed 2D sheet becomes close enough till to being in contact with each other (Brau et al., 2013; Ciarletta, 2014; Holmes and Crosby, 2010). Such contact will lead to the binding energy and changes the local curvature within the fold (Fig. 3b). Assume the overlap length $l_{b}$ and equilibrium distance $h$, local radius of curvature $R_{1}, R_{2}$ and $R_{3}$ and arc angle $\theta_{1}, \theta_{2}$ and $\theta_{3}$ in the folded configuration (Zhu et al., 2012), the conservation of length of torus will yield $8[R_{3} \theta_{3}+l_{b}+R_{2} \theta_{2}+R_{1} \theta_{1}]+2 \pi R_{d} \sin (r / R_{d})-4(2 R_{3}+h)=2 \pi r$, and the strain energy in the folds is

$$
E_{s}^{I I I}=B\left[4\left(\theta_{1} / R_{1}+\theta_{2} / R_{2}+\theta_{3} / R_{3}\right)+\left[2 \pi R_{d} \sin \left(r / R_{d}\right)-4\left(2 R_{3}+h\right)\right] / 2 R_{d}^{2}\right] d r
\tag{13}
$$

Similar to Eqs. (10) or (12), we can calculate the potential energy via

$$
\begin{aligned}
E_{p}^{I I I} & =8 P_{t}\left[\int_{-\theta_{3}}^{0}\left(R_{d}+R_{3}+R_{3} \sin \theta\right) R_{3} d \theta+\int_{R_{3}}^{R_{3}+l_{b}}\left(y+R_{d}\right) d y+\int_{0}^{\theta_{2}}\left(R_{d}+R_{3}+l_{b}+R_{2} \sin \theta\right) R_{2} d \theta\right. \\
& \left.+\int_{\pi / 2}^{\pi / 2+\theta_{1}}\left(R_{d}+R_{3}+l_{b}+R_{2} \sin \theta_{2}+R_{1} \sin \left(\theta_{1}-\pi / 2\right)+R_{1} \sin \theta\right) R_{1} d \theta\right] d r \\
& +P_{t}\left[2 \pi R_{d} \sin \left(r / R_{d}\right)-4\left(2 R_{3}+h\right)\right] R_{d} d r
\end{aligned}
\tag{14}
$$

In this folding stage, in addition to the strain energy and potential energy, the binding energy in the overlaps of the folds needs to be taken into account and it is

$$
E_{b}^{I I I}=4 \Gamma_{b} l_{b} d r
\tag{15}
$$

where $\Gamma_{b}$ is the binding energy density of the 2D sheet. Therefore, the total energy of the folding deformation state is $E_{t}^{I I I}=E_{s}^{I I I}+E_{p}^{I I I}+E_{b}^{I I I}$.

These three stages of conformal, wrinkling and folding states of 2D sheet in droplet would emerge in a sequence with the increase of $|\varepsilon_{\theta \theta}|$ and liquid evaporation (Diamant and Witten, 2011; King et al., 2012). The transition point between them can be determined by minimizing their corresponding energy at the position $r$, i.e.

$$
E_{t}^{\min }=\min \left[E_{t}^{I}, E_{t}^{I I}, E_{t}^{I I I}\right]
\tag{16}
$$

With Eq. (16), the local curvature $\kappa$ can be determined by $\kappa=f(E_{t}^{min})$. For example, when there is a conformal contact between 2D sheet and liquid droplet, we will have $E_{t}^{min}=E_{t}^{I}$, and $\kappa(\theta)=1/R_{d} \ (0 \leq \theta \leq 2\pi)$ in the polar coordinate system (Fig. A2); when the 2D sheet wrinkles, we will have $E_{t}^{min}=E_{t}^{II}$, and $\kappa(\theta)=$

![](./images/812737037911195649_4.jpg)

Fig. 4. The rotational spring-mechanical slider mechanics model of crumpling a single 2D sheet by liquid evaporation. (a) Out-of-plane deformation of 2D sheet modeled by rotational spring located at the axisymmetric axis connecting two rigid planes with the rotational angle of $\theta_{t}$ and the binding interaction modeled by mechanical slider when the two rigid planes are close enough with the evaporation of liquid (top) and the simplification of this rotational spring-mechanical slider system into a 2D model due to its symmetry (bottom). The critical moment for introducing the mechanical slider to the rotational spring model is referred to the critical rotational angle $\theta_{t}^{c}$ and depends on liquid evaporation. (b) Variation of rotational angle $\theta_{t}$ and critical rotational angle $\theta_{t}^{c}$ with the liquid evaporation (plotted by an increase of liquid droplet curvature $\kappa_{d}(=1/R_{d})$ ). When $\theta_{t}>\theta_{t}^{c}$, the mechanical slider will not effective, and when $\theta_{t} \leq \theta_{t}^{c}$, the mechanical slider starts to take effect to represent the binding energy in the folded deformation. The inserts show the deformed states of 2D sheet and their corresponding state of the spring-slider mechanics model. .

$$
\begin{cases}
\frac{\left|d f^{2} / d x^{2}\right|}{\left(1+(d f / d x)^{2}\right)^{\frac{3}{2}}},|x| \leq \lambda_{w} / 2 \\
1 / R_{d},|x|>\lambda_{w} / 2
\end{cases}
$$
, where $\theta=(\int_{0}^{x} \sqrt{1+(d f / d x)^{2}} d x) / r$; when 2D sheet folds, we will have $E_{t}^{min}=E_{t}^{III}$ and $\kappa(\theta)=$

$$
\begin{cases}
1 / R_{1}, & |\theta| \leq \theta_{1} R_{1} / r \\
1 / R_{2}, & \theta_{1} R_{1} / r<|\theta| \leq\left(\theta_{2} R_{2}+\theta_{1} R_{1}\right) / r \\
0, & \left(\theta_{2} R_{2}+\theta_{1} R_{1}\right) / r<|\theta| \leq\left(\theta_{2} R_{2}+\theta_{1} R_{1}+l_{b}\right) / r \\
1 / R_{3}, & \left(\theta_{2} R_{2}+\theta_{1} R_{1}+l_{b}\right) / r<|\theta| \leq\left(\theta_{2} R_{2}+\theta_{1} R_{1}+l_{b}+\theta_{3} R_{3}\right) / r \\
1 / R_{d}, & |\theta|>\left(\theta_{2} R_{2}+\theta_{1} R_{1}+l_{b}+\theta_{3} R_{3}\right) / r
\end{cases}
$$

. Specifically, for graphene sheet, the geometric parameters are $R_{0}=0.68$ nm, $R_{1}=0.967 R_{0}$, $R_{2}=3.401 R_{0}$, $R_{3}=\sqrt{2 \pi /(2+\pi)} R_{0}$, $\theta_{1}=0.685 \pi$, $\theta_{2}=0.185 \pi$, $\theta_{3}=0.5 \pi$, and $h=0.34$ nm (Zhu et al., 2012), and the material parameters are $B=2.38 \mathrm{e}-19$ J, $E=1$ TPa, $t=0.34$ nm and $\Gamma_{b}=-0.232$ J/m² (Liu and Xu, 2018). Fig. A3a and b plots the curvature distribution of $\kappa(\theta)$ in the 2D sheet (graphene) at these three different stages of liquid evaporation. Once the local curvature is obtained, the strain energy, potential energy and binding energy in the deformed 2D sheet can be determined. More importantly, define the deformed area in the 2D sheet as "ridge", similar to that of crumpling thin elastic sheet in a confined hollow sphere (Cerda et al., 1999; Matan et al., 2002; Vliegenthart and Gompper, 2006), the strain energy stored in the ridges can be written as (Mora and Boudaoud, 2002)

$$
E_{s}=B \xi \varphi\left(\theta_{t}-\pi\right)^{2} \tag{17}
$$

where $\xi$ and $\varphi$ are dimensionless geometry factors, and $\xi$ is often referred to as the Föppl-von Kármán number. Our analysis on crumpling 2D sheet by liquid evaporation shows that $\xi = A_g/t^2$ and $\varphi = \sqrt{P_t/E}$ (See Fig. A3). $A_g$ is the original surface area of 2D sheet. $\theta_t$ is the angle between the two planes of the ridge and $\theta_t - \pi$ represents the degree of deformation relative to a flat 2D sheet without deformation.

### 2.3. Rotational spring-mechanical slider model of crumpling a single 2D sheet

As analyzed in Section 2.2, both local wrinkles and folds reflect the out-of-plane mechanical deformation of 2D sheets centered about a symmetric line (marked in red in Fig. 3b), and contribute to the strain energy and potential energy due to their high local curvature compared to the other parts of the 2D sheet with negligible deformation. More importantly, with the evaporation of liquid droplet, the out-of-plane deformation will increase and these negligible deformation parts are packed more closely. The packing of negligible deformation parts about symmetric lines in the 2D sheets is analogous with the folding process of origami structures along a flexible axis or reference point (Faber et al., 2018). With this analogy, the crumpling deformation of one single 2D sheet can be modeled by a rotational spring connected with two planes that cannot be crumpled and are considered to be rigid, as illustrated in Fig. 4a (I). The associated out-of-plane deformation energy can be characterized by the energy storage of the deformed rotational spring. When the interactive binding energy between folded rigid parts needs to be taken into account, it can be described by introducing a mechanical slider between two rigid planar sheets, as illustrated in Fig. 4a (III). With this 2D rotational spring- mechanical slider mechanics model, the crumpling of a single 2D sheet now can be characterized through the energy analysis.

The energy stored in the rotational spring that corresponds to the total compressive, wrinkling and self-folding deformation in the 2D sheet can be defined as
$$
E_s^{spring} = \frac{1}{2}k_s(\theta_t - \pi)^2 \tag{18}
$$
where $k_s$ is the constant of rotational spring and $\theta_t$ is the rotational angle (Fig. 4a (I)). $k_s$ can be determined from the continuum mechanics model of compression, wrinkling and self-folding deformation of a single 2D sheet in Section 2.2. That is, the energy from this rotational spring model should be equal to that from continuum model analysis in Eq. (17), which is, $E_s^{spring} = E_s$ and it yields to $k_s = 2B\frac{A_g}{t^2}\sqrt{\frac{P_t}{E}}$.

With the continuous deformation of 2D sheet, the gap between local wrinkled sheets will decrease, and the interactive binding energy will emerge. Different from the out-of-plane deformation, it reflects the van der Waals interactions, and will further promote the wrinkling toward the appearance of self-folding of 2D sheets. The interactive binding energy depends on both gap distance and area of overlapped rigid parts and can be defined as
$$
E_b^{slider} = k_bA_{def}[\sin (\theta_t^c/2) - \sin (\theta_t/2)]H(\theta_t^c - \theta_t) \tag{19}
$$
where $k_b$ is the constant of the mechanical slider, $A_{def}$ is the area contributed to the out-of-plane deformation. $\theta_t^c$ is the critical angle between the two connected rigid plates, and when $\theta_t < \theta_t^c$, the two rigid plates are considered to be close enough and the resultant binding energy needs to be considered (Holmes and Crosby, 2010). $H(\theta_t^c - \theta_t)$ is the Heaviside function and $H(\theta_t^c - \theta_t) = 0$ when $\theta_t \geq \theta_t^c$ and $H(\theta_t^c - \theta_t) = 1$ when $\theta_t < \theta_t^c$ (Haberman, 2012). Since the binding energy only occurs between two overlaps in 2D sheet, we have $k_b = \Gamma_b/2$.

Similar to the definition of projected area $(A_s = 2\pi R_d^2[1 - \cos(L_g/2R_d)])$ on the surface of liquid droplet for a planar 2D sheet (Fig. A2), we define the projection of out-of-plane deformed area of 2D sheet $A_{def}$ on the surface of liquid droplet as $A_{pr}$, and $A_{def} = A_{pr} + \pi A_g/4 - A_s$. The overall nominal compressive strain in the 2D sheet can be written as $\varepsilon_s = (A_{pr} - A_{def})/A_{def}$. Apparently, $\varepsilon_s < 0$, and we have $\theta_t = \pi(1 + \varepsilon_s)$. For example, consider the bending stiffness $(B)$ and size $(L_g)$ of a square 2D sheet, under the radius of liquid droplet $(R_d)$ and evaporation pressure $(P_t)$, $A_{pr}$ can be determined via (Holmes and Crosby, 2010) $A_{pr} = (BR_d/P_t)^{\frac{1}{4}}\pi L_g/2$ and $\theta_t^c = \pi/(1 + (E/P_tA_{pr}^2)^{1/9}t^{4/9})$. Fig. 4b plots the variations of $\theta_t$ and $\theta_t^c$ with the increase of curvature of liquid droplet $\kappa_d$ $(=1/R_d$, which reflects the liquid evaporation process). When the curvature is zero, the 2D sheet is a flat surface and $\theta_t = \pi$. The 2D sheet is in a fully conformal contact with the liquid surface and there is no out-of-plane deformation. With the increase of curvature $(\kappa_d)$ during evaporation, the strain energy of 2D sheet increases, and $\theta_t$ decreases accordingly but is larger than $\theta_t^c$. By contrast, $\theta_t^c$ remains approximately the same. Beyond a critical curvature, $\theta_t$ is smaller than $\theta_t^c$, indicating the distance between two rigid plates in the spring model is close enough and the binding energy will appear, where the slider will play a role in the spring-slider mechanics model and needs to be considered, as illustrated in the inset.

In addition to the strain energy $E_s^{spring}$ and binding energy $E_b^{slider}$, the evaporation pressure will deform 2D sheet. Take the center of liquid droplet as the reference point, its induced mechanical deformation of 2D sheet can be described by a potential energy $E_p$ to the reference point, which is
$$
E_p = P_t\left[A_{def}\left(R_d + \sqrt{A_{def}}\cos(\theta_t/2)/2\right) + A_sR_d\right] \tag{20}
$$
where the first term reflects the contribution by the out-of-plane deformation of 2D sheet. Eq. (20) shows that the potential energy of a single 2D sheet during liquid evaporation is a function of the curvature of liquid droplet $(\kappa_d$, see Appendix A),

![](./images/812737037911195649_5.jpg)

Fig. 5. Energy variation of a single 2D material graphene sheet with liquid evaporation from the spring-slider mechanics model. Various energy variation during liquid evaporation in the forms of both liquid droplet curvature $\kappa_d$ and rotational spring angle $\theta_t$ for a square graphene sheet with (a) $L_g$=40 nm under $P_t$=10 atm, (b) $L_g$=40 nm under $P_t$=40 atm and (c) $L_g$=100 nm under $P_t$=10 atm. The point when $E_b^{slider}$ starts to emerge and $dE_{tot}/d\kappa_d = 0$ correspond to $\theta_t = \theta_t^c$ and $\kappa_d^G$ and $\kappa_d^E$, respectively. .

similar to that in Eqs. (18) and (19). With Eqs. (18)-(20), the total energy of crumpling 2D sheet can be written as

$$
E_{tot} = E_s^{spring} + E_b^{slider} + E_p
\tag{21}
$$

$dE_{tot}/d\kappa_d < 0$ is favorable of folding process of 2D sheets by evaporation and $dE_{tot}/d\kappa_d$ will increase as the evaporation continues, leading to a continuous folding of 2D sheets till to $dE_{tot}/d\kappa_d = 0$. Besides, when the folding stops ($dE_{tot}/d\kappa_d = 0$), if $\theta_t < \theta_t^c$, the 2D sheet could be folded into a stable pattern due to the attractive van der Waals interaction between rigid parts by the liquid evaporation. Otherwise, the deformed 2D sheet will bounce back into its planar form. As an example, Fig. 5a plots the variation of $E_{tot}$, $E_s^{spring}$, $E_b^{slider}$, $E_p$, and rotational angle ($\theta_t$) in the spring-slider model with the increase of liquid droplet curvature $\kappa_d$ for a square graphene sheet, where for the 2D sheet (graphene), $B$=2.38e$-$19 $J$, $E$=1 TPa, $t$=0.34 nm and $\Gamma_b=-0.232$ J/m$^2$ (Liu and Xu, 2018), $L_g$=40 nm and $P_t$=10 atm. With the evaporation of liquid, $\theta_t$ decreases, and $E_s^{spring}$ increases. When $\kappa_d$ is large enough, $\theta_t \leq \theta_t^c$ and $E_b^{slider}$ starts to emerge and increase (magnitude). At the same time, $E_p$ will decrease due to the decrease of the radius of liquid droplet and deformation of the 2D sheet. When $dE_{tot}/d\kappa_d = 0$ appears earlier than $\theta_t = \theta_t^c$ (i.e. $\kappa_d^E$<$\kappa_d^G$, and $\theta_t > \theta_t^c$, see Appendix A for the definition of $\kappa_d^E$ and $\kappa_d^G$), the folding will stop without van der Waals attractive energy and the deformed 2D sheet will recover. At a higher evaporation pressure of $P_t$=40 atm, Fig. 5b shows that $E_p$ decreases more rapidly and $E_b^{slider}$ emerges earlier. This synergistic effect delays the emergence of $dE_{tot}/d\kappa_d = 0$, and when the folding stops, $\theta_t < \theta_t^c$ ($\kappa_d^E$>$\kappa_d^G$), which leads to a folded 2D sheet stabilized by the van der Waals attractive energy. Similarly, by increasing the size of 2D sheet to $L_g$=100 nm (Fig. 5c), a stabilized folded graphene by van der Waals attractive energy can also be obtained due to $\theta_t < \theta_t^c$ ($\kappa_d^E$>$\kappa_d^G$) at $dE_{tot}/d\kappa_d = 0$. This demonstration indicates that the size and evaporation pressure play the crucial role in the folding of 2D sheet and their relationship can be obtained by analyzing Eq. (21).

Further, given the bending stiffness $B$ of 2D sheet and liquid evaporation pressure $P_t$, a critical area of 2D sheet $A_g^c$ can be approximately written as (See Appendix A)

$$
A_g^c = \eta\left(\frac{B}{P_t}\right)^{\frac{2}{3}}
\tag{22}
$$

where $\eta$ reflects the deformation homogeneity and intensity of 2D sheet. For example, the non-uniformly deformed 2D sheets with highly localized wrinkles and folds, and the equivalence of Eqs. (22) and (21) leads to $\eta$=98.82 (See Appendix A). In particular, when the 2D sheet experiences uniform deformation, the 2D sheet remains a conformal contact with the liquid droplet and pertains a constant radius of curvature, where the rotational angle $\theta_t = \pi - \theta_b/2$, and the bending angle of the 2D sheet $\theta_b = L_g/R_d$ (Liu et al., 2016; Liu and Xu, 2018). Eq. (21) will become $E_{tot} = E_s^{spring} + E_p$, where $E_s^{spring} = 2B/(\theta_t - \pi)^2$, and $E_p = P_tA_gL_g/(2\pi - 2\theta_t)$. $dE_{tot}/d\kappa_d$=0 at $\kappa_d = 2\pi /L_g$ will yield $A_g^c = 4\pi^2(B/P_t)^{\frac{2}{3}}$, where $\eta = 4\pi^2$, which agrees well with self-folding of one single graphene sheet by liquid evaporation (Liu and Xu, 2018).

### 2.4. Spring-slider network mechanics model of crumpling and assembly of multiple 2D sheets

When there are multiple 2D sheets in the droplet, in addition to the mechanical deformation of individual 2D sheets, because the surface area of droplet will decrease with the liquid evaporation, and 2D sheets will be packed and assembled closely. This assembly of individual 2D sheet will lead to an emergence of interactive energy between 2D sheets, which is similar to the binding energy of the folded parts in a single 2D sheet and can also be described by a mechanical slider with the same as that in folded parts, referred to as inter-layer slider. Fig. 6 shows the illustration of a network distribution of rotational spring-slider mechanics models for the crumpling and assembly of multiple 2D sheets in solution droplet by liquid evaporation.

Consider $n_l$ ($n_l$$\geq$2) 2D sheets in a liquid droplet, each 2D sheet has the area $A_g^{(i)}$($i = 1,2,3 \ldots \ldots n_l$), and the total area is $A_g^t = \sum_{i=1}^{n_l} A_g^{(i)}$. Given $A_g^t \leq A_d(=4\pi R_d^2)$ at the beginning of evaporation, the surface of droplet is not fully covered by the 2D

![](./images/812737037911195649_6.jpg)

Fig. 6. Crumpling and assembling multiple 2D material sheets by liquid evaporation (left) and its rotational spring-mechanical slider network mechanics model (right). The intra-layer (orange) and inter-layer (purple) slider reflect the van der Waals interaction in the self-folding deformation of individual 2D sheet and self-assembly of adjacent individual 2D sheet, respectively.

sheets, and there is no overlap between 2D sheets. As a consequence, the assembly energy between individual 2D sheets can be neglected and the total deformation energy is

$$
E_{s}^{spring}=\sum_{i=1}^{n_{l}} E_{s}^{spring(i)}=\frac{1}{2} \sum_{i=1}^{n_{l}} k_{s}^{(i)}\left(\theta_{t}^{(i)}-\pi\right)^{2}
\tag{23}
$$

where $E_{s}^{spring(i)}$ is the deformation energy of the $i^{th}$ 2D sheet, $k_{s}^{(i)}=2 B \frac{A_{g}^{(i)}}{t^{2}} \sqrt{\frac{P_{t}}{E}}, \theta_{t}^{(i)}=\pi\left(1+\varepsilon_{s}^{(i)}\right)$ and $\varepsilon_{s}^{(i)}=\left(A_{p r}^{(i)}-A_{d e f}^{(i)}\right) / A_{d e f}^{(i)}$. Similarly, the total binding energy in 2D sheets can be obtained by

$$
E_{b}^{s l i d e r}=\sum_{i=1}^{n_{l}} E_{b}^{s l i d e r(i)}=\sum_{i=1}^{n_{l}} k_{b}^{(i)} A_{d e f}^{(i)}\left[\sin \left(\theta_{t}^{c(i)} / 2\right)-\sin \left(\theta_{t}^{(i)} / 2\right)\right] H\left(\theta_{t}^{c(i)}-\theta_{t}^{(i)}\right)
\tag{24}
$$

where $k_{b}^{(i)}=\Gamma_{b} / 2$ and $\theta_{t}^{c(i)}=\pi /\left(1+\left(E / P_{t} A_{p r}^{(i) 2}\right)^{1 / 9} t^{4 / 9}\right)$. And the total potential energy contributed by evaporation pressure is

$$
E_{p}=\sum_{i=1}^{n_{l}} E_{p}^{(i)}=\sum_{i=1}^{n_{l}} P_{t}\left[A_{d e f}^{(i)}\left(R_{d}+\sqrt{A_{d e f}^{(i)}} \cos \left(\theta_{t}^{(i)} / 2\right) / 2\right)+A_{s}^{(i)} R_{d}\right]
\tag{25}
$$

Thus, the total energy without assembling among multiple 2D sheets by liquid evaporation is

$$
E_{t o t}=E_{s}^{s p r i n g}+E_{b}^{s l i d e r}+E_{p}
\tag{26}
$$

With the evaporation of liquid, the surface area of liquid droplet will decrease, eventually leading to $A_{g}^{t} \geq A_{d}$. After that, the 2D sheets start to assemble (Fig. 1c) and the assembly energy emerges. Unlike the layer by layer stacking of planar 2D sheets, the assembled 2D sheets will stuck at the boundaries on the liquid droplet due to the out-of-plane deformation of wrinkling and self-folding (Mendoza-Sanchez and Gogotsi, 2016; Qin et al., 2017). Besides, these boundary inter-lockings between 2D sheets will lead to both hoop and radial compressive strain within a single 2D sheet, similar to that of the deformation in granular particles (Gonzalez and Cuitiño, 2012), and the total deformation energy characterized by Eq. (23) at $A_{g}^{t}<A_{d}$ will becomes

$$
E_{s}^{spring}=\sum_{i=1}^{n_{l}} E_{s}^{spring(i)}=\sum_{i=1}^{n_{l}} k_{s}^{(i)}\left(\theta_{t}^{(i)}-\pi\right)^{2}
\tag{27}
$$

When the assembly between different 2D sheet starts, the out-of-plane deformation will not be constrained in the intra-layer wrinkling and self-folding, and the inter-layer assembly will also partially occupy the deformed area. As a result, $A_{d e f}^{(i)}=A_{b i n d}^{(i)}+A_{a s m}^{(i)}$, where $A_{b i n d}^{(i)}$ represents the deformed area of wrinkling and self-folding and $A_{a s m}^{(i)}$ represents the assembled area in the ith 2D sheet. Therefore, the binding energy becomes

$$
E_{b}^{s l i d e r}=\sum_{i=1}^{n_{l}} E_{b}^{s l i d e r(i)}=\sum_{i=1}^{n_{l}} k_{b}^{(i)} A_{b i n d}^{(i)}\left[\sin \left(\theta_{t}^{c(i)} / 2\right)-\sin \left(\theta_{t}^{(i)} / 2\right)\right] H\left(\theta_{t}^{c(i)}-\theta_{t}^{(i)}\right)
\tag{28}
$$

![](./images/812737037911195649_7.jpg)

Fig. 7. Energy variation of multiple 2D material graphene sheets with liquid evaporation from the spring-slider network mechanics model. (a) Energy variation as a function of liquid droplet curvature $\kappa_{d}$. $A_{g}^{(i)}$=10,000 nm², $n_{l}$=5 and $P_{t}$=10 atm. $dE_{tot}/d\kappa_{d}$=0 corresponds to the stopping of the crumpling and assembling. (b) Normalized crumpling energy $E_{s}^{spring}+E_{b}^{slider}$ by the assembling energy $E_{asm}$ in the particles after complete evaporation of liquid (in red) and normalized self-folding area ($A_{bind}$) by the assembling area ($A_{asm}$) (in blue) with the increase of pressure.

The assembly energy due to the van der Waals interaction between individual 2D sheets can be calculated by

$$
E_{asm}=\sum_{i=1}^{n_{l}} E_{asm}^{(i)}=\sum_{i=1}^{n_{l}} k_{a}^{(i)} A_{asm}^{(i)} \tag{29}
$$

where $k_{a}^{(i)}=\Gamma_{b}/2$ is the assembly coefficient and is the same with $k_{b}^{(i)}$ in Eq. (28). The potential energy that will crumple and assemble multiple 2D sheets by the evaporation pressure can be calculated via

$$
E_{p}=\sum_{i=1}^{n_{l}} E_{p}^{(i)}=P_{t} \sum_{i=1}^{n_{l}}\left[A_{bind}^{(i)}\left(R_{d}+\sqrt{A_{bind}^{(i)}} \cos \left(\theta_{t}^{(i)} / 2\right)\right)+A_{asm}^{(i)}\left(R_{d}+\sqrt{A_{asm}^{(i)}} / 2\right)+A_{s}^{(i)} R_{d}\right] \tag{30}
$$

With Eqs. (27)-(30), the total energy of crumpling and assembling multiple 2D sheets by liquid evaporation is

$$
E_{tot}=E_{s}^{spring}+E_{b}^{slider}+E_{asm}+E_{p} \tag{31}
$$

Similar to Eq. (21), Eq. (31) can be solved numerically. For example, take $A_{g}^{(i)}$=10,000 nm², $n_{l}$=5 ($A_{g}^{t}$=50,000 nm²) and $P_{t}$=10 atm, Fig. 7a shows the deformation energy $E_{s}^{spring}$, binding energy $E_{b}^{slider}$, assembly energy $E_{asm}$, potential energy $E_{p}$ as well as the total energy $E_{tot}$ as the liquid evaporates. During the liquid evaporation, $dE_{tot}/d\kappa_{d}$ will increase as the evaporation continues, leading to a continuous crumpling and assembly of 2D sheets till to $dE_{tot}/d\kappa_{d}=0$. When the crumpling and assembly stop ($dE_{tot}/d\kappa_{d}=0$), the multiple 2D sheets will be crumpled into a particle stabilized by the van der Waals energy of adhesive self-folding and assembly.

After the complete evaporation of liquid, Fig. 7b plots the normalized crumpling energy $E_{s}^{spring}$+$E_{b}^{slider}$ by the assembly energy $E_{asm}$ with the increase of pressure $P_{t}$. It increases (magnitude) with the increase of $P_{t}$, indicating a higher pressure will promote the self-folding of 2D sheets. Further, we define

$$
\zeta=A_{bind}/A_{asm} \tag{32}
$$

where $A_{bind}$ and $A_{asm}$ can be used to characterize the surface morphology and the overall structure of the particle. $\zeta=0$ indicates there is no deformation of individual 2D sheet and only self-assembly of 2D sheets occurs by liquid evaporation. As a consequence, a bulk form of restacking of 2D sheets will be obtained. These areas can be determined from energy analysis, where $A_{bind}=\sum_{i=1}^{n_{l}} A_{bind}^{(i)}$, $A_{bind}^{(i)}=E_{b}^{slider(i)}/(k_{b}^{(i)}[\sin(\theta_{t}^{c(i)}/2)-\sin(\theta_{t}^{(i)}/2)])$and $A_{asm}=\sum_{i=1}^{n_{l}} A_{asm}^{(i)}$, and $A_{asm}^{(i)}=E_{asm}^{(i)}/k_{a}^{(i)}$. Apparently, a large $\zeta$ suggests a dominative role of the crumpling energy over the assembly energy, and promotes local deformation of individual 2D sheets including ridges. These local ridges will prevent direct restacking of 2D sheets and lead to "porous" structures of assembled particles. Fig. 7b shows a monotonic variation of $A_{bind}/A_{asm}$ with the pressure, which agrees well with that of energy variations. In particular, when the surface area of each 2D sheet is the same, we will have $E_{s}^{spring}=n_{l}E_{s}^{spring(i)}$, $E_{b}^{slider}=n_{l}E_{b}^{slider(i)}$, $E_{asm}=n_{l}E_{asm}^{(i)}$ and $E_{p}=n_{l}E_{p}^{(i)}$, and as a result, $A_{bind}=n_{l}A_{bind}^{(i)}$, $A_{asm}=n_{l}A_{asm}^{(i)}$, and $A_{g}^{t}=n_{l}A_{g}^{(i)}$. $\zeta=0$ will lead to $A_{bind}$=0 and $E_{b}^{slider}=E_{b}^{slider(i)}=0$, and there will be no permanent deformation in each 2D sheet due to the lack of van der Waals energy, which is the same as that of unfolded 2D sheet in the crumpling of a single 2D sheet in Section 2.3. Therefore, the critical area of each 2D sheet will be $A_{g}^{c(i)}=\eta(B/P_{t})^{\frac{2}{3}}$, and consider $A_{g}^{t}=n_{l}A_{g}^{(i)}$, the critical total area of multiple 2D sheets will be

$$
A_{g}^{tc}=n_{l}\eta\left(\frac{B}{P_{t}}\right)^{2/3} \tag{33}
$$

![](./images/812737037911195649_8.jpg)

Fig. 8. Coarse-grained (CG) model of 2D material graphene. (a) Full-atom lattice (left) and coarse-grained (CG) lattice (right) models of graphene. The highlighted triangle area indicates coarse-grained scaling of 16:1; i.e., one bead in the CG model represents 16 atoms in the full-atom model. As a consequence, with the bond length of $d_0$ in the full-atom model, and the bond length in CG model is $d_0^{cg}$=$4d_0$. Comparison of (b) the stress-strain curve of graphene sheet under a tensile test, (c) the deformation energy of graphene sheet under a bending load and (d) the binding energy of two parallel graphene sheets between full-atom and coarse-grained model. The insets illustrate the loading conditions.

If $A_g^t \leq A_g^{tc}$, there will be no deformation within each 2D sheet and only assembly of 2D sheets among each other, which is the same as the assembly process of colloidal particles (Vogel et al., 2015). When $A_g^t > A_g^{tc}$, both self-folding and assembly will appear and $\zeta$ will be larger than zero.

More importantly, once the total energy of assembled particle after the complete evaporation of liquid is determined, and if we assume the local curvature and central angle in the fold are constant (Zhu et al., 2012), the density of fold (ridge) can be calculated and it is

$$
D_{r}=\frac{E_{s}^{\text {spring }}}{B A_{g}^{t}}\left[\frac{R_{1}}{\theta_{1}}+\frac{R_{2}}{\theta_{2}}+\frac{R_{3}}{\theta_{3}}\right] \tag{34}
$$

Similarly, the radius of gyration $(r_g)$ can be employed to approximately estimate the size of assembled particles after the complete evaporation of liquid, and $R_g$ is

$$
R_{g}=\frac{E_{p}}{P_{t} A_{g}^{t}} \tag{35}
$$

We should note that when there is no deformation in 2D sheets, $E_p$ will be the same with the potential energy of assembled particles in colloidal science and Eq. (35) will reduce to the radius of assembled hollow spheres by rigid particles (Hsu et al., 2005). In addition, the accessible area of assembled particle (Luo et al., 2011) (i.e. the surface area of particle that is accessible to air) can be obtained by excluding the stacked areas within a particle from the total surface area of 2D materials and it is

$$
A_{a c c}=2\left[A_{g}^{t}-(\zeta+1) A_{a s m}\right] \tag{36}
$$

### 3. Computational modeling and methods

Large numbers of atoms will be involved so as to model the crumpling and assembly of 2D sheets by liquid evaporation and validate the theoretical mechanical model in Section 2. For example, take 2D material graphene suspended in a water

droplet as an example, consider the typical size of the solution liquid droplet of $R_d = 1.45\ \mu\text{m}$ in experiments, and the concertation of graphene $C_m$=$1 mg/mL$ (Yang et al., 2016), one liquid droplet will contain $4.27 \times 10^{11}$ water molecules and $6.39 \times 10^8$ carbon atoms, largely beyond the capacity of current computational cost. In this section, we will present a high-efficiency simulation procedure by coarse-graining graphene sheets and mimicking solid-liquid interaction using a virtual spherical interactive force field.

Graphene will be modeled by a coarse-grained (CG) model, as illustrated in Fig. 8a. Similar to the intrinsic lattice structure of full-atom graphene model, this graphene CG model is a hexagonal lattice, and each CG bead represents a certain number of carbon atoms in the full-atom model. The total energy of this CG model $E_{CG}$ includes bond stretching energy $E_{bond}$, angular bending energy $E_{angle}$, dihedral torsional energy $E_{dih}$ and non-bonded van der Waals energy $E_{vdW}$, and is

$$
E_{CG}=E_{bond}+E_{angle}+E_{dih}+E_{vdW} \tag{37}
$$

For graphene-like 2D nanomaterials that will experience a large deformation, these energies of bonded interaction between CG beads can be expressed as $E_{bond}=\sum_{i=1}^{n_{bond}}D_0[1-e^{-\alpha(d-d_0^{CG})}]^2$, $E_{angle}=\sum_{i=1}^{n_{angle}}k_\theta(\theta-\theta_0)^2$, and $E_{dih}=\sum_{i=1}^{n_{dih}}k_\emptyset[1-\cos(2\emptyset)]$ (Ruiz et al., 2015), where $D_0$ and $\alpha$ are parameters of the potential well depth of bonds and $d_0^{CG}$ is the equilibrium distance of the CG bond, $k_\theta$, $\theta_0$, and $k_\emptyset$ are the constant of bead angle, equilibrium angle and constant of dihedral in the CG model, respectively. $n_{bond}$, $n_{angle}$, and $n_{dih}$ are the number of bond, angle and dihedral in the CG model, respectively. $d_0^{CG}$ and $\theta_0$ determine the geometrical and scaling features of the CG model. For example, for the CG model with hexagonal lattice structure and 16:1 coarse-graining mapping, $d_0^{CG}=0.56$ nm and $\theta_0=120^\circ$. On the other hand, the continuum mechanics analysis to graphene-like 2D nanomaterials will lead to $\alpha=log2/(\varepsilon_f d_0^{CG})$, where $\varepsilon_f$ is the maximum failure strain of the 2D material; $D_0=\sqrt{3}hEG/\alpha^2(4G-E)$ and $k_\theta=\sqrt{3}(d_0^{CG})^2hEG/(3E-4G)$ (Gillis, 1984), where $G$ is the in-plane shear modulus of graphene and $h$ is the interlayer distance and is 0.34 nm for graphene. Similarly, the parameters of CG model in the torsional energy $E_{dih}$ can be obtained by considering a pure bending deformation of 2D materials in continuum mechanics. For a rectangular 2D sheet in length $L_g$ and width $W_g$ with a radius of curvature $R_b$ (insets in Fig. 8c), based on the continuum mechanics analysis, the bending energy $E_{bend}=BL_gW_g/2R_b^2$ (Liu and Xu, 2018). $E_{bend}=E_{dih}$ will lead to a linear correlation between $k_\emptyset$ and $B$, $k_\emptyset=\beta B$, where $\beta$ depends on the coarse-graining scale in the CG model. For example, it is $\beta=0.0758$ for 16:1 coarse-grained mapping and $\beta=0.1125$ for 4:1 coarse-grained mapping (Ruiz et al., 2015).

For non-bonded van der Waals energy $E_{vdW}$ in the CG model, similar to the full atomic model, it can be described by 12-6 Lennard-Jones (L-J) potential, and $E_{vdW}=\sum_{i=1}^{n_{bead}-1}\sum_{j=i+1}^{n_{bead}}4\epsilon[(\frac{\sigma}{d})^{12}-(\frac{\sigma}{d})^6]$, where $\epsilon$ is the potential well depth of CG beads and $\sigma=0.346$ nm is the parameter associated with the equilibrium distance between two non-bonded CG beads. $n_{bead}$ is the number of bead in the CG model and $d$ is the distance between two beads. For two layers of materials with an overlap area $A_b$ (inset in Fig. 8d), the binding energy is $E_{bind}=\Gamma_b A_b$, and $E_{bind}=E_{vdW}$, i.e. $\Gamma_b A_b=\sum_{i=1}^{n_{bead}-1}\sum_{j=i+1}^{n_{bead}}4\epsilon[(\frac{\sigma}{d})^{12}-(\frac{\sigma}{d})^6]$ leads to a linear correlation between $\epsilon$ and $\Gamma_b$ via $\epsilon=\vartheta\Gamma_b$. Similar to $\beta$, $\vartheta$ also depends on the coarse-graining scale in the CG model, and it is $\vartheta$=$2.1892 \times 10^{-20}\ m^2$ and $\vartheta=1.84 \times 10^{-19}\ m^2$ for 4:1 and 16:1 coarse-grained mapping, respectively (Ruiz et al., 2015).

For a well-defined coarse-graining scale of 16:1 in 2D material graphene, the potential parameters $D_0$, $\alpha$, $k_\theta$, $k_\emptyset$ and $\epsilon$ in its CG model can be determined. For graphene, take $E=1\ TPa$, $G=450\ GPa$, $\varepsilon_f=0.16$ (Ruiz et al., 2015), $B$=$2.38 \times 10^{-19}J$ and $\Gamma_b$=$-0.232J/m^2$, we can obtain $D_0$=$797.4283 kcal/mole$, $\alpha$=$0.7736\ \text{\AA}^{-1}$, $k_\theta$=$1662.9 kcal/mole$, $k_\emptyset$=$2.6 kcal/mole$ and $\epsilon$=$6.15 kcal/mole$ by following above analysis. With these parameters in the CG mode, we performed both coarse-grained molecular dynamics (CGMD) and full-atom molecular dynamics (MD) simulations to validate our CG model. All the simulations were performed in LAMMPS (Plimpton et al., 2007). Fig. 8b and c show the comparison of the proposed CG model and full-scale atom model in tension and bending deformation, respectively. Both Young's modulus and maximum tensile strength of graphene are well reproduced by the proposed CG model. Further, under a relatively broad range of bending angle $\theta_b$, good agreement of the bending deformation is obtained between the CG model and full-atom model, which validates the CG model for the study of crumpling 2D graphene. Fig. 8d shows that the non-bonded interaction between graphene sheet from CGMD simulations agrees well with that in full-atom MD simulations, indicating that the CG model can also be used to study the interactive binding energy of self-folding and assembly of graphene sheets.

Once the CG model of graphene is validated, we will introduce a computational method to mimic the interactions of liquid molecules to graphene by employing a virtual spherical L-J force field. The simulation procedure consists of three steps: In the first step, the liquid droplet was replaced by a virtual sphere with radius $R_d=R_i$. The initial positions of graphene were uniformly distributed on the outside surface of the sphere to mimic a uniform distribution of graphene in liquid droplet. The initial radius of sphere ($R_i$) was determined based on the number of graphene sheets and area of each sheet to ensure no overlap between individuals and no self-folding within a single sheet. The interaction between graphene and surface of the virtual sphere was modeled by a 12-6 L-J potential to mimic interaction between liquid droplet and graphene. By setting up the cut-off radius of the L-J potential $2^{1/6}\sigma$ between graphene sheets and the sphere surface, there would be only repulsive for the sphere surface to the graphene and this setting would also not allow penetration of graphene sheet into the sphere. A constant force pointing to the center of the virtual sphere was added on each CG bead to provide a driving force for crumpling and assembling graphene, and the magnitude of force was determined by $F_b=\frac{P_t A_t^g}{n_{bead}}$. Such the force depends on the evaporation pressure and reflects the influence of temperature on the liquid evaporation. After that, the system was equilibrated at 300 K for 2.0 ns with NVT ensemble under Nose/Hoover thermostat. In the second step, all

![](./images/812737037911195649_9.jpg)

Fig. 9. Comparison of energy and morphology evolution of a single graphene sheet during the liquid evaporation between the theoretical predictions and simulations. Comparison of energy variation of a single graphene sheet with a size of (a) $L_g$=40 nm and (c) $L_g$=100 nm between theoretical and simulation results with liquid droplet curvature $\kappa_d$. Morphology evolution of a square graphene sheet with (b) $L_g$=40 nm and (d) $L_g$=100 nm with liquid droplet curvature $\kappa_d$ under evaporation pressure $P_t$=10 atm and 40 atm. $\kappa$ is the local curvature in the deformed sheet.

the settings in the first step would remain the same except that the radius of the virtual sphere decreased with time by following a well-defined function to mimic the evaporation process of liquid droplet (Holyst et al., 2013; Yang et al., 2012), which is $R_d = R_i + (R_e - R_i)(t_s - t_i)/t_e$, ($t_i < t_s \leq t_i + t_e$), where $t_s$ is the instantaneous time step during simulation, $t_i$ is the time period required for equilibrium of the system in the first step, and $t_e$ is the time period for the radius of sphere that changes from $R_i$ (initial radius of sphere) to $R_e$ (final radius of sphere). The evaporation rate is taken into account by the decreasing rate of radius of the virtual sphere $|R_e - R_i|/t_e$ and was taken $\sim$50 nm/ns to ensure both stability of simulations and independence of assembled and self-folded morphology with the shrinking rate of the virtual sphere. Afterward, the NVT ensemble under Nose/Hoover thermostat that mimics a constant temperature of high-temperature furnace during evaporation in experiments was employed to monitor the crumpling and assembly of graphene sheets. In the third step, the applied force pointing to the center of sphere was removed at $R_d = R_e$. Another 2 ns was performed under NVT ensemble to monitor the final morphology of assembled graphene sheets. The strain energy, binding energy, assembling energy and radius of gyration of assembled particle were documented every 0.01 ns during simulations to ensure sufficient data recorded. This simulation method has been validated with the excellent agreement of graphene deformation with full-scale modeling of graphene and water molecules (see Appendix B). Further, we validate the combination of virtual sphere and equivalent evaporation pressure model by performing full-scale MD simulations and the good agreement of graphene deformation between the virtual sphere force field and full driving evaporation pressure model is obtained (see Appendix C).

## 4. Results

Fig. 9a shows comparison of energy variation of a single square graphene sheet with a size of $L_g$=40 nm between theoretical and simulation results during the liquid evaporation. The radius of liquid droplet $R_d$ decreases from $R_i$=100 nm to $R_e$=1 nm, and the evaporation-induced pressure is taken $P_t$=10 atm and $P_t$=40 atm, respectively. With the increase of curvature of liquid droplet ($\kappa_d$=$1/R_d$), both the deformation energy $E_{def}$ (i.e. $E_s^{spring}$ in the mechanics model, Eq. (18)) and binding energy $E_{bind}$ (i.e. $E_b^{slider}$ in the mechanics model, Eq. (19)) under $P_t$=10 atm remain zero, indicating there is no self-folding in the graphene, in good agreement with snapshots in Fig. 9b. This unfolding is caused by the absence of binding energy

![](./images/812737037911195649_10.jpg)

Fig. 10. Comparison of the deformation energy $E_{def}$ and binding energy $E_{bind}$ of the single layer graphene after the complete evaporation of liquid between the theoretical predictions and simulations under evaporation pressure (a) $P_{t}$=10 atm and (b) $P_{t}$=40 atm. The inset highlights at the small area where if both of the energies are zero, graphene cannot be folded by the liquid evaporation. .

$E_{bind}$ which will prevent the "bouncing back" of initial bending deformation, and is well predicted by Eq. (22), where a small graphene sheet cannot be folded by a weak driving force for graphene $L_{g}$=40 nm ( < critical $L_{g}^{c}=\sqrt{A_{g}^{c}}$=61.34 nm when $P_{t}$=10 atm from Eq. (22)) or pressure of $P_{t}$=10 atm ( < critical $P_{t}^{c}$=36.05 atm when $A_{g}$=1600 $nm^{2}$ from Eq. (22)). At a higher pressure, $P_{t}$=40 atm, both $E_{def}$ and $E_{bind}$ increase after a critical evaporation time, and a folded graphene is obtained, as shown in snapshots in Fig. 9b. Besides, the good agreement of these energies between simulation and theoretical predictions indicates that deformation and self-folding can be well captured by our rotational spring-mechanical slider mechanics model. For a larger graphene sheet ($L_{g}$=100 nm), both $E_{def}$ and $E_{bind}$ (Fig. 9c) show non-zero magnitudes with the evaporation of liquid, and a higher pressure leads to higher magnitudes. As a consequence, successful folded patterns of graphene are obtained with a higher crumpling density at a higher pressure, as indicated in Fig. 9d. More importantly, the good agreement between theoretical predictions and simulations remains.

Both the pressure and graphene sheet size can affect the final folded morphology as well as the deformation energy and binding energy after complete evaporation of liquid. The equilibrated energy of graphene sheet during simulation is extracted and compared with the theoretical predictions. Fig. 10a plots the comparison of equilibrated energy of graphene after complete evaporation of liquid between the theoretical predictions and simulations. Both the deformation energy and binding energy increase (magnitude) linearly with the increase of graphene area $A_{g}$, suggesting a favorable crumpling process for large graphene. More importantly, the energies show good agreement between simulations and theoretical predictions. In particular, zero deformation and binding energies in the extremely small graphene that correspond to an unsuccessful folding under the evaporation pressure $P_{t}$=10 atm are well captured by our theoretical model Eq. (22). For a higher pressure $P_{t}$=40 atm, the good agreement between theoretical prediction and simulations still remains (Fig. 10b). The minimum size of graphene sheet for a successful folding decrease and the magnitude of deformation energy $E_{def}$ increases, while the binding energy $E_{bind}$ remains approximately the same. These different responses to pressure are dependent of intrinsic deformation nature that $E_{def}$ is sensitive to local curvature of bending deformation and $E_{bind}$ is determined by overlap area in graphene (Zhu et al., 2012), and also agree with the spring constant and slider constant in Eqs. (18) and ((19). These different crumpling energies in these graphene sizes and evaporation pressures reflect different crumpling morphologies. In particular, if the graphene is large enough, the size of first folded graphene may be larger than the critical length to be folded and multiple foldings are expected.

To illustrate the multiple folding of graphene by liquid evaporation, simulations on series of a single graphene sheet with different sizes were performed. Fig. 11 shows the map of folded graphene as the variation of pressure after complete evaporation of liquid water, where the local curvature distribution on the folded graphene is given to highlight the folding density and locations. When the graphene size is small and the evaporation pressure is low, the graphene sheet cannot be folded and is referred to the "unfold" region. When either the pressure or graphene size increases, a successful folding such as "racket-like" pattern is observed, referred to as a "racket-like" region in the map, similar to the folding pattern of graphene nanoribbon (Liu et al., 2016; Liu and Xu, 2018; Ortolani et al., 2012). In particular, when the graphene size or pressure continues to increase, folding becomes intense and multiple foldings are observed. Besides, higher pressure or larger graphene size is, the stronger folding with larger folding curvature will be, which echoes well with higher deformation and binding energies in Fig. 10. The folded pattern with intense folding, in particular with multiple foldings, is similar to a shape of spatial particle, referred to as a "particle" region and its size decreases with the increase of evaporation pressure. With the definition of these three deformation regions, their transition can be further predicted through the theoretical analysis by Eq. (22). The good agreement between theoretical predictions and simulations in Fig. 11 further validates the energy analysis through the proposed rotational spring-mechanical slider mechanics model.

![](./images/812737037911195649_11.jpg)

Fig. 11. Morphology and size map of folded graphene with highlights of local curvature after complete evaporation of liquid. Three patterning regions are identified, referred to as "unfold", "racket-like" patterns and "particle" with the increase of evaporation pressure or/and total area of 2D graphene sheet.

When there are multiple graphene sheets in liquid droplet, similar simulations were performed, and 5 pieces of square graphene sheets with size of $L_g$=100 nm were taken as an example. In the simulations, the initial radius of liquid droplet was $R_i$=100 nm to ensure no overlap between each graphene sheets at the equilibrium, and the final radius of liquid droplet after complete evaporation of liquid was set to be $R_e$=1 nm to make sure the droplet is small enough for a sufficient crumpling and assembly of graphene sheets. Figs. 12a and b shows the comparison of energy variation between theoretical predictions via Eqs. (23)-(31) and simulations for their assembling and self-folding with liquid evaporation under the evaporation pressure of 10 atm and 40 atm, respectively. The deformation energy $E_{def}$ (i.e. $E_s^{spring}$ in Eqs. (23) and (27)), binding energy $E_{bind}$ (i.e. $E_b^{slider}$ in Eqs. (24) and (28)) and assembling energy $E_{asm}$ (i.e. $E_{asm}$ in Eq. (29)) all increase (magnitude) rapidly at the onset of liquid evaporation and then reach a plateau when the size of droplet is small enough ($\kappa_d$>0.1 $nm^{-1}$). Similar to that in a single graphene sheet in Fig. 9, the increase of $E_{def}$ and $E_{bind}$ (magnitude) with evaporation reflects the crumpling or self-folding of graphene associated with generation and propagation of folded ridges, and higher pressure leads to larger $E_{def}$ and $E_{bind}$. The appearance and increase of $E_{asm}$ with evaporation represents the assembly of multiple graphene sheets and higher pressure leads to lower $E_{asm}$ (magnitude). The final stable stage of these energies suggests the arrival of crumpled and assembled graphene with a stable pattern. Besides, higher pressures lead to higher $E_{def}$, $E_{bind}$, and lower $E_{asm}$, promoting crumpling and suppressing self-assembly of graphene sheets. In parallel, the variation of energies with evaporation (i.e. radius of liquid droplet) can be predicted by Eq. (31) and the results show excellent agreement with the simulation results for both evaporation pressures, as shown in Fig. 12a and b, which validates the proposed network mechanics model of rotational spring-mechanical slider for multiple graphene sheets.

In order to monitor the evolution of morphology and size of the folded particles during the liquid evaporation, Fig. 12c and d give the mass distribution of coarse-grained carbon beads $n_r/n_{bead}$ along the radial direction, where $n_r$ and $n_{bead}$ is the number of beads at the position of $r$ and total number of beads in the graphene particle, respectively. We should mention that the centroid of assembled graphene particle may not the same as the center of liquid sphere and the starting point of each distribution could be smaller than the instantaneous $R_d$ of liquid droplet radius. At the beginning of evaporation ($\kappa_d$=0.01 $nm^{-1}$), most of the beads are distributed on the surface of sphere, which corresponds to uniform distribution of graphene sheet (see inset), resulting in the distribution limited to a narrow region with an extremely high peak. With the liquid evaporation, the peak becomes lower and the distribution region of beads becomes wider, which is led by the out-of-plane deformation in crumpling and assembly of graphene. After complete liquid evaporation ($\kappa_d$=1 $nm^{-1}$), the mass shows a normal distribution spanning across the entire particle, leading to a "ball-like" particle of assembled graphene. The insets further illustrate the evolution of morphology of graphene sheets. When the evaporation pressure increases from 10 atm to 40 atm, similar mass evolution with liquid evaporation is also observed, but is more concentrated with a higher peak after complete liquid evaporation, in good agreement with a denser assembly of graphene in a higher evaporation pressure.

Fig. 13a and b give the simulation snapshots of graphene sheets with liquid evaporation and the ridge distribution in one of the representative graphene sheets (marked in blue and numbered as (I)) under these two different pressures. At the beginning of evaporation ($\kappa_d$=0.01 $nm^{-1}$), graphene sheets were distributed uniformly without any overlap between each other on the surface of liquid sphere and the small curvature in the graphene results from the deformation due to the conformal contact between graphene and liquid droplet. This conformal contact with small deformation in each individual

![](./images/812737037911195649_12.jpg)

Fig. 12. Energy and mass variation of crumpling and assembling multiple 2D material graphene sheets by the liquid evaporation. Comparison of the deformation energy $E_{def}$, binding energy $E_{bind}$ and assembling energy $E_{asm}$ of 5 square graphene sheets with each size of $L_g$=100 nm between the theoretical predictions and simulations under (a) $P_t$=10 atm and (b) $P_t$=40 atm. Mass distribution of the graphene in the droplet during liquid evaporation under (c) $P_t$=10 atm and (d) $P_t$=40 atm. The inserts show the evolution of assembled morphologies of the crumpled graphene sheets with liquid evaporation.

graphene but without assembly continues with the evaporation till the $\kappa_d \sim 0.033\ nm^{-1}$. Afterward, graphene sheets start to contact with each other, in consistence with the appearance of self-assembly energy $E_{asm}$ in Fig. 12a. Once self-assembly begins, graphene will be subjected to a biaxial compression strain due to interaction with adjacent ones. As a consequence, folding ridges increase and propagate and more importantly, they bifurcate beyond the main folding axis of symmetry, which in turn accelerates a rapid increase of $E_{asm}$ as obtained in Fig. 12a. With further evaporation, $\kappa_d$$>$$0.1\ nm^{-1}$, the crumpled and assembled pattern becomes stable and the ridges will not increase with approximately stable local curvatures in the graphene sheets, also in good agreement with the arrival of the stable energies in Fig. 12a. When the evaporation pressure increases from 10 atm to 40 atm, similar evolutions of crumpling and assembly but intense local ridges in both size and curvature in the representative graphene sheet are observed. Besides, more numbers and larger sizes of ridges are obtained and an assembled particle with more intense crumpling is obtained, which also agrees with higher energies in Fig. 12b. To compare the crumpling morphology of each graphene sheet in the assembled graphene particle after complete evaporation of liquid, Fig. 14 gives morphology of the particles and the density of ridges with local deformation curvatures in these five graphene sheets under these two different evaporation pressures. The higher density of ridges under higher pressure is further confirmed. We further calculate the ridge density $(D_r)$ by the image processing algorithm (Liang et al., 2017) (Fig. A6), as given in Fig. 14c and d. Under the same evaporation pressure, although the distribution of ridges is different among each individual sheets, their total ridge density is approximately the same, suggesting the equality of crumpling and assembly in each graphene sheet by evaporation pressure.

Figs. 15a and b shows the comparison of crumping and assembly energy in the final folded particle with the total area of graphene between the theoretical predictions and simulations under these two evaporation pressures. Similar to that in a single graphene sheet in Fig. 10, the deformation energy $E_{def}$, binding energy $E_{bind}$ and assembling energy $E_{asm}$ increase (magnitude) with the increase of total area of graphene, and higher pressures lead to larger energies. The larger $E_{bind}$ indicates an intense deformation, in good consistence with a larger $E_{def}$; a larger $E_{asm}$ indicates a closer packing of each deformed graphene. Good agreement between simulations and theoretical results is obtained. More importantly, given the total area of graphene sheets, this agreement is independent of numbers of graphene sheets.

Fig. 16a shows the effect of evaporation pressure on the mass distribution in assembled particles after complete evap- oration of liquid. Higher pressure will lead to a higher peak with narrower distribution, indicating that the increase of the pressure will promote the crumpling of graphene and will also enhance the geometric regularity of assembled particles

![](./images/812737037911195649_13.jpg)

Fig. 13. CGMD simulated morphology evolution of 5 square graphene sheets with each $L_g$=100 nm with liquid evaporation (liquid droplet curvature $\kappa_d$) under (a) $P_t$=10 atm and (b) $P_t$=40 atm (top) and distribution of folded ridges in one of the representative graphene sheet marked as (I) in blue (bottom).

![](./images/812737037911195649_14.jpg)

Fig. 14. Overall morphology of the assembled graphene particle after complete evaporation of liquid and comparison of crumpled morphology among their individual graphene sheet under (a) and (c) $P_t$=10 atm and (b) and (d) $P_t$=40 atm. Graphene is a square shape with the size of $L_g$=100 nm.

![](./images/812737037911195649_15.jpg)

Fig. 15. Comparison of energy of the assembled particles after complete evaporation of liquid between the theoretical predictions and simulations under (a)$P_t$=10 atm and (b)$P_t$=40 atm.

![](./images/812737037911195649_16.jpg)

Fig. 16. Mass distribution and the ridge density evolution of assembled graphene during the liquid evaporation. The effect of (a) evaporation pressure and (b) total area of graphene sheets on the mass distribution of the assembled particles after complete evaporation of liquid. (c) Comparison of the ridge density with the liquid evaporation (liquid droplet curvature $\kappa_d$) between theoretical predictions and simulations. (d) Comparison of the ridge density in the assembled particles between theoretical predictions and simulations after complete evaporation of liquid.

toward a "ball-like" shape. However, the location of peaks is nearly the same, implying the averaged size of assembled par- ticles is insensitive to evaporation pressure. When the total area of graphene $A_g^t$ increases, Fig. 16b shows that the location of peaks shifts to a high position and larger particles will be assembled, which agrees well with experimental measurements (Luo et al., 2011; Ma et al., 2012) (Fig. 1b). In addition to the size of particles, the surface roughness of particles is directly related to the out-of-plane deformation of 2D sheets, which is controlled by the total area and evaporation pressure. Fig. 16c gives the comparison of the ridge density $(D_r)$ between theoretical predictions (Eq. (34)) and simulations in all the graphene layers within a single particle. As the liquid evaporates, the density of ridges shows a rapid increase at the beginning and then arrives at a stable stage. Besides, higher pressures lead to large densities. Note that in the image processing algorithm to simulation results, the wrinkles with small curvatures at the initial stage of liquid evaporation are not considered as folds, leading to a small overestimate of the ridge density over theoretical predictions. Fig. 16d further shows comparison of

![](./images/812737037911195649_17.jpg)

Fig. 17. Morphology and size map of crumpled and assembled graphene with highlights of local curvature in each individual sheet after complete evaporation of liquid. The ratio of the crumpled area to assembled area, $\zeta=A_{bind}/A_{asm}$ and the radius $R_g$(in nanometer) in each particle are given, denoted as $(\zeta, R_g)$. At a low evaporation pressure and small total area of graphene sheet, self-folding in individual sheet is very small and can be neglected, leading to $\zeta <0.1$; At a high evaporation pressure and large total area of graphene sheet, each graphene will be self-folded intensively and assembled after complete evaporation of liquid ($\zeta >0.5$).

ridge density in the final folded particle between the theoretical predictions and simulations with the evaporation pressure. The ridge density increases with the increase of pressure. Both the evolutions of crumpling and assembly of graphene with liquid evaporation and the effect of pressure are well consistent with variations of energies in Fig. 12. More importantly, they are captured by the theoretical prediction with good agreement with simulations.

Fig. 17 summarizes the assembled particles by square graphene sheets ($n_l$=10) with the same size as a function of the total area and evaporation pressure. The curvature is given to illustrate the local deformation and morphologies of particles. The ratio between the crumpled area and assembled area $\zeta=A_{bind}/A_{asm}$ and the radius $R_g$(in nanometer) of each particle is also given, denoted as $(\zeta, R_g)$. At a small evaporation pressure and total area of graphene (e.g. $A_g^t$<20,000$nm^2$ and $P_t$<20 atm), these multiple graphene sheets will experience assembly with very limited deformation on individual graphene during evaporation, similar to that unfolded region I for a single graphene sheet in Fig. 11, where this region is "assembly dominant" ($\zeta <0.1$). Increasing evaporation pressure or the total area of graphene, crumpling deformation in individual graphene occurs, and local ridges with large curvatures will appear on the surface of particles, where this region reflects the competition between assembly and crumpling. The transition of regions between the "assembly dominant" and "assembly & crumpling" ($0.5 \leq \zeta \leq 0.1$) can be predicted well through our theoretical model via Eq. (32). At both high pressure and large total area of graphene sheets, crumpling in individual sheets will become intense associated with increased local ridges and high local curvatures, where it is referred to as crumpling dominant region ($\zeta >0.5$). Similarly, the transition between "assembly & crumpling" and "crumpling dominant" region can also be predicted in theory via Eq. (32) with good agreement each other. This deformation map further confirms that the overall size of the assembled particles is independent of evaporation pressure, but their overall profile in geometry are close to be spherical at high pressure. To demonstrate the role of graphene assembly in the formation of particles by liquid evaporation, Fig. 18 highlights the regions where individual crumpled graphene sheet is closer enough in the assembled particles and the assembly energy needs to be taken into account. The assembled areas over the total area will decrease with the increase of evaporation pressure, in line with the intense ridge densities that will reduce the deformed area of graphene in assembly. In contrast, it remains approximately the same with the increase total area of graphene, although the total assembly area increases.

In addition to the theoretical prediction to the morphology evolution and energy variations of crumpling and assembling graphene sheets by liquid evaporation, the energy of assembled particles after complete evaporation of liquid can be employed to estimate the overall size and accessible area of assembled ball-like particles as demonstrated in Eq. (35). Fig. 19a gives the comparison of the overall radius of particles $R_g$ between simulations and theoretical analyses. The experimental results available from the works of literatures are also included. Our theoretical predictions show remarkable agreement with both simulations and experimental results. The independent of evaporation pressure is also consistent with mass distribution in Fig. 16a. With Eq. (36), the accessible area of the assembled particle can also be predicted and show good agreement with simulations, as shown in Fig. 19b. More importantly, the slope in their linear relationship is 0.6239 for $P_t$=10 atm

![](./images/812737037911195649_18.jpg)

Fig. 18. Morphology and size map of crumpled and assembled graphene with highlights of local assembled regions in each individual sheet after complete evaporation of liquid. The assembled regions and fraction of the assembled area among the whole particle are reflected by assembling energy distribution. $(\zeta, R_{g})$ is the same as that in Fig. 17.

![](./images/812737037911195649_19.jpg)

Fig. 19. Comparison of (a) dimension size and (b) accessible area of assembled particles after complete evaporation of liquid under different evaporation pressures, shapes and total areas of graphene sheets among theoretical predictions, CGMD simulations and available experiments.

and 0.6155 for $P_{t}$=40 atm, insensitive to evaporation pressure, which are also close to 0.586 reported in the simulations (Cranford and Buehler, 2011) and experiments (Luo et al., 2011).

## 5. Discussion

In experiments, given the same concentration of graphene in liquid solutions, graphene sheets may have variations of shapes, sizes, and numbers (Jiang et al., 2016; Luo et al., 2010; Zhang et al., 2009). These parameters may influence the crumpling and assembly process during evaporation and the eventual morphology and size of assembled particles. Take the squared graphene as an example, given a series of total area of graphene in solvent solution, Fig. 20 shows the map of sizes and morphologies of the assembled particles by different numbers of graphene sheets after complete liquid evaporation under evaporation pressure of 20 atm. Similar to that in Fig. 17, the local curvature distribution $\kappa$, and the ratio between the crumpled area and assembled area $\zeta$=$A_{bind}$/$A_{asm}$ and the radius $R_{g}$(in nanometer) of each particle, $(\zeta, R_{g})$ are highlighted. When the total area of graphene sheets is kept the same, the overall size $(R_{g})$ of assembled particles show no significantly difference while $\zeta$ decreases with the increase of $n_{l}$. This different response is because the area of individual sheet will decrease with the increase of $n_{l}$, leading to the $A_{g}^{(i)}$ close to $A_{g}^{c}$ (Eq. (22)) and suppressing the self-folding of graphene sheets. Larger $n_{l}$ will require larger total areas of 2D sheets to self-folding deformation in the 2D sheet, as shown in Eq. (33). At

![](./images/812737037911195649_20.jpg)

Fig. 20. Effect of graphene sheet numbers on the size and morphologies of the assembled particles after complete evaporation of liquid under $P_t$=20 atm. $(\zeta, R_g)$ is the same as that in Fig. 17.

![](./images/812737037911195649_21.jpg)

Fig. 21. Effect of size distribution of square graphene sheet on the size and morphologies of the assembled particles after complete evaporation of liquid under $P_t$=20 atm. $(\zeta, R_g)$ is the same as that in Fig. 17.

the same time, both the overall size and density of ridges will increase with the increase of total area of graphene sheets, similar to the results in Fig. 17.

Further, we consider the size distribution of graphene sheets in liquid solutions in experiments. As observed in the synthesis of graphene (Zhang et al., 2009), the normal distribution is employed to take into account the area variation of graphene sheets via $n(A_g) = \frac{1}{\sqrt{2\pi}} \exp(-\frac{(A_g-A_\mu)^2}{2A_\sigma^2})$, where $A_g$ is the area of graphene sheet and $n(A_g)$is the number of sheets at this area. $A_\mu$ is the median area and $A_\sigma$ is the standard deviation. Consider the total area $A_g^t$ and number of graphene sheets $n_l$ in the liquid solution, we define the standard median as $A_\mu = A_g^t/n_l$, and the standard deviation can be determined by $A_\sigma = A_\mu/m$ (m is integer and $m \geq 3$ to ensure $A_g > 0$). In our simulations, five cases at $n_l$=10 with $A_\mu - 2A_\sigma$, $A_\mu - A_\sigma$,$A_\mu$, $A_\mu + A_\sigma$ and $A_\mu + 2A_\sigma$ under evaporation pressure of 20 atm are studied and graphene remains a squared shape. Fig. 21 gives the map of sizes and morphologies of particles as a function of standard deviation of the area. The difference of size among individual graphene sheet only slightly causes a small change in both size and morphology of assembled particles. In addition, by taking four different shapes of graphene sheets, square, rectangle with an aspect ratio of

![](./images/812737037911195649_22.jpg)

Fig. 22. Effect of graphene sheet shapes on the size and morphologies of the assembled particles after complete evaporation of liquid under $P_{r}$=20 atm. $(\zeta,R_{g})$ is the same as that in Fig. 17.

![](./images/812737037911195649_23.jpg)

Fig. 23. The effect of (a) graphene sheet number and (b) size distribution of graphene sheet and (c) graphene sheet shape on the mass distribution of the assembled particles after complete evaporation of liquid.

2, circle and equilateral triangle, we performed the simulations on the effect of graphene geometry on assembled particles after complete evaporation of liquid. Fig. 22 gives the map of assembled particles. Significant change of the overall particle size and morphology is not observed, similar to that effect of graphene number and shape size in Figs. 20 and 21. The strong dependence of the total area of graphene sheets, but very insensitive to individual graphene number, shape geometry and size suggests the importance of graphene concentration in the crumpling and assembly process of graphene sheets into particles, which also agrees well with experiments.

As a quantitative characterization of these effects, Fig. 23 plots the effect of number, size distribution and shape of graphene sheets on the mass distribution in assembled particles after complete evaporation of liquid. Moreover, the overall size and accessible area in these assembled particles are also collected and are plotted in Fig. 19. These data show good agreement with theoretical predictions, which further indicates their insensitivities to these size and geometric factors of individual graphene sheets and also confirms the robustness of our proposed rotational spring-mechanical slider mechanics model.

We should mention that these 2D graphene sheets before deformation by liquid in above analyses are conducted on the basis of pristine graphene that can be considered a homogeneous thin film in continuum mechanics, and the effect of defects, edge configurations and chirality, and the resultant initial deformation morphologies that may influence the crumpling and assembling process during evaporation are not considered. For example, the edge stress may exist due to different bonding configurations of atoms at the edge of free standing 2D materials such as graphene (Lu and Huang, 2010; Shenoy et al., 2008). Such stress will lead to local wrinkling of edge and even curling deformation in graphene sheets, in particular, in graphene nanoribbons with a large aspect ratio (Shenoy et al., 2008, 2010), and the 2D sheet will not remain a planar form. When these edge stressed 2D sheets are in contact with the surface of liquid droplet, the edge stress is expected to increase the compressive hoop strain (Eq. (8)) near the edges and leads to a higher energy for the fully conformal contact, which will benefit the subsequent wrinkling or buckling of 2D sheet near the edge.

In addition, once 2D materials are immersed in the liquid solution, we assume a homogenous distribution of 2D sheets is achieved in the liquid solution with full exfoliation of 2D materials prior and no overlapped multiple layers exist. By contrast, when the proposed theoretical models are extended to study the crumpling and assembling process of 2D layered materials such as 2D heterostructures, where the mechanical properties including Young's modulus, bending stiffness and binding energy density that are needed in the models needs to be calibrated for the 2D layered materials as a whole rather than their individual layer components, it is expected that the shear stress led by evaporation is usually very small and cannot lead to delamination of the layered materials. For example, delaminating a multiple layered graphene structure with sole weak van der Waal interactions will require the shear stress as high as 0.4 GPa (Chen et al., 2015), while our calculation in Eq. (5) show that the shear stress ($P_s$) by the capillary flow exerted on the surface of 2D sheet is only 5.69 Pa at the evaporation temperature of 900 °C, eight orders of magnitude lower than that of the required delamination stress (0.4 GPa). The wrinkling and folding in 2D layered materials may be different from that of a 2D material planar sheet because of a small local deformation gradient may exist along the thickness direction (Ye et al., 2012), but local delamination is also not expected under such small deformation. As a result, the 2D layered materials as a whole will experience mechanical deformation such as wrinkling and folding and the local deformation gradient can be taken into account by introducing a local strain or stress into the continuum mechanics model via Eq. (8).

## 6. Concluding remarks

We have proposed a theoretical mechanics framework of the rotational spring-mechanical slider model to quantitatively describe the crumpling and self-assembling of 2D material sheets suspended in liquid droplets prior by liquid evaporation. An equivalent evaporation pressure model that takes account of capillary force, vapor pressure, gas pressure, vapor recoil pressure and capillary flow-induced force is developed to unify the driving force of crumpling and assembling 2D materials by liquid evaporation. In the theoretical model of rotational spring-mechanical slider, the rotational spring model is intro- duced to describe the out-of-plane large deformation of 2D material sheets and the mechanical slider is developed to take account of van der Waal binding energy in overlaps of both self-folding deformation of individual sheets and self-assembly among multiple sheets. Both of them are correlated with the continuum mechanics model of self-folding deformation of a single 2D sheet and the associated parameters are determined with the help of energy analysis. Further, the extended net- work mechanics model composed multiple pairs of rotational spring-mechanical slider and inter-layer mechanical slider is developed to understand the energy competition between crumpling and self-assembling deformation and is used to deter- mine the critical evaporation conditions and geometric features of 2D sheets toward successful assembly of stable particles after complete evaporation of liquid. Besides, the energy of final assembled particles after complete evaporation of liquid is formulated to predict the surface morphology and size.

To validate the proposed theoretical model, we have developed a coarse-grained molecular dynamics (CGMD) model for 2D material sheets and also proposed a computational procedure to simulate dynamic solid-liquid interactions through a vir- tual spherical force field. The CG model of 2D materials is well calibrated by comparing with the full-scale atomistic model including stretching, bending and adhesive deformation with a focus on their corresponding energy. The virtual spherical force field is applied to the CG model of 2D materials through the well-defined decreasing rate of spherical radius to mimic an evaporation process of liquid at an elevated temperature and is confirmed with good agreement with full-scale simula- tions on solid-liquid interactions. Comprehensive CGMD simulations were performed to reveal the effect of geometric shape, number, size and area of 2D material sheets on their evolution of energy and morphology during crumpling and assembling by liquid evaporation and show remarkable agreement with theoretical predictions. In particular, the transition between crumpling and assembling deformation when evaporation conditions and geometric features of 2D materials change are well captured by the theoretical analysis of the proposed rotational spring-mechanical slider model. More importantly, good agreement between simulations and theoretical predictions on both overall size and accessible area of assembled stable particle after complete evaporation of liquid is obtained, and both of them are also in a good consistency with independent experimental results in literatures.

It is envisioned that the developed mechanics scheme of rotational spring-mechanical slider model will advance our un- derstanding of large deformation, instabilities and self-assembly of 2D nanomaterials under dynamic solid-liquid interaction environments, and could also be extended to study liquid evaporation-induced deformation of a broad variety of nanoma- terial such as lipid members, nanowires, and nanofibers and beyond 2D nanomaterials. In addition, the theoretical model and computational procedure at the large scale are expected to shed immediate light on controlling the overall size and morphology of 2D nanomaterials-based crumpled particles made by aerosol-like processing. It should also be useful for guiding the printing process of 2D materials for applications in high-performance electrodes, supercapacitors and sensors, where large deformation, instabilities and self-assembly of 2D nanomaterials are expected by liquid evaporation of droplet on substrates.

## Acknowledgment

This work is supported by NSF-CMMI-1728149 and the start-up funds at the University of Virginia. J.H. thanks earlier support from the Office of Naval Research (ONR N000141612838).

### Appendix A. Theoretical correlation among $A_g$, $B$ and $P_t$

Before the emergence of binding energy, the total energy for a liquid evaporation-driven folding of a single 2D sheet is

$$
E_{\mathrm{tot}}=E_{s}^{\mathrm{spring}}+E_{p} \tag{A1}
$$

The self-folding deformation of 2D sheets stops at $d E_{tot}/d \kappa_d$=0 , i.e. $d E_{s}^{\mathrm{spring}}/d \kappa_d$+$d E_p/d \kappa_d$=0. From Eq. (18), $E_{s}^{\mathrm{spring}}=1/2 k_s (\theta_t - \pi)^2$ and $\theta_t=\pi A_{pr}/(A_{pr}+\pi A_g/4 - A_s)$ where $A_{pr}=(B R_d/P_t)^{\frac{1}{4}} \pi L_g/2$, $A_s=2 \pi R_d^2[1-\cos(L_g/2 R_d)]$ and $\kappa_d=1/R_d$.
We can further write $E_{s}^{\mathrm{spring}}$ as a function of $\kappa_d$,

$$
E_{s}^{\mathrm{spring}}=B \pi^{2} \frac{A_{g}}{t^{2}} \sqrt{\frac{P_{t}}{E}}\left(\frac{D}{C}\right)^{2} \tag{A2}
$$

where $C=2(B/P_t)^{\frac{1}{4}} L_g \kappa_d^{\frac{7}{4}}+A_g \kappa_d^2-8+8 \cos(L_g \kappa_d/2)$, and $D=8-8 \cos(L_g \kappa_d/2)-A_g \kappa_d^2$.

Similarly, the potential energy $E_p$ can also be expressed as a function of $\kappa_d$, which is

$$
E_{p}=P_{\mathrm{t}}[F+M H+J] \tag{A3}
$$

where $F=(B/P_t)^{\frac{1}{4}} \pi L_g \kappa_d^{-\frac{5}{4}}/2+A_g/\kappa_d-2 \pi/\kappa_d^3+2 \pi \cos(L_g \kappa_d/2)/\kappa_d^3$, $M=[\pi (B/P_t)^{\frac{1}{4}} L_g \kappa_d^{-\frac{1}{4}}/2+A_g-2 \pi/\kappa_d^2+2 \pi \cos(L_g \kappa_d/2)/\kappa_d^2]^{\frac{3}{2}}/2$, $H=\cos(\pi L_g (B/P_t)^{\frac{1}{4}} \kappa_d^{\frac{7}{4}}/C)$ and $J=2 \pi/\kappa_d^3-2 \pi \cos(L_g \kappa_d/2)/\kappa_d^3$.

![](./images/812737037911195649_24.jpg)

Fig. A1. Schematics illustrations of the capillary force exerts on the free end of 2D sheet and the deflection $\delta_F$ and the equivalent pressure exert on the surface of 2D sheet and the deflection $\delta_p$. (a) and (b), rectangular sheet. (c) and (d), triangular sheet. (e) and (f), circular sheet.

![](./images/812737037911195649_25.jpg)

Fig. A2. (a) Schematic illustrations of the undeformed planar area (Ag) of the 2D sheet, and the projected area (As) in the surface of the droplet. Rd is the radius of liquid droplet. (b) The morphology illustration of a 2D sheet in contact with the surface of the liquid droplet. (c) The polar coordinate on the undeformed planar 2D sheet with the radial distance r and polar angle θ.

$dE_s^{spring}/d\kappa_d+dE_p/d\kappa_d=0$ yields

$$
2B\pi^2\frac{A_g}{t^2}\sqrt{\frac{P_t}{E}}\left[\frac{DD'C-D^2C'}{C^3}\right]+P_t\left[F'+M'H+MH'+J'\right]=0 \tag{A4}
$$

When $A_g$, $B$ and $P_t$ are given, the solution to Eq. (A4) can be solved numerically, referred to as $\kappa_d^E$, and it will depend on the energy competition between self-folding deformation of 2D sheets and evaporation pressure.

In parallel, when we write $\theta_t$ as a function of $\kappa_d$, we will have

$$
\theta_t=\frac{2\pi A_g^\frac{1}{2}\left(\frac{B}{P_t}\right)^\frac{1}{4}\kappa_d^\frac{7}{4}}{C} \tag{A5}
$$

When the binding energy needs to be considered, the critical angle $\theta_t^c$ can also be expressed as

$$
\theta_t^c=\frac{\pi}{1+\left(\frac{4E\kappa_d^\frac{1}{2}}{\pi^2A_gP_t^\frac{1}{2}B^\frac{1}{2}}\right)^{1/9}t^{4/9}} \tag{A6}
$$

$\theta_t=\theta_t^c$ yields

$$
\frac{2\pi A_g^\frac{1}{2}\left(\frac{B}{P_t}\right)^\frac{1}{4}\kappa_d^\frac{7}{4}}{2A_g^\frac{1}{2}\left(\frac{B}{P_t}\right)^\frac{1}{4}\kappa_d^\frac{7}{4}+A_g\kappa_d^2-8\left(1-\cos\left(\frac{L_g}{2}\kappa_d\right)\right)}-\frac{\pi}{1+\left(\frac{4E\kappa_d^\frac{1}{2}}{\pi^2A_gP_t^\frac{1}{2}B^\frac{1}{2}}\right)^\frac{1}{9}t^\frac{4}{9}}=0 \tag{A7}
$$

Similar to Eq. (A4), we can numerically solve Eq. (A7) and its solution, referred to as $\kappa_d^G$, depends on the geometrical analysis.

Given $A_g$, $B$ and $P_t$, if $\kappa_d^E>\kappa_d^G$, the folding will stop without adhesive van der Waals energy and the deformed 2D sheet will recover; $\kappa_d^E<\kappa_d^G$ will suggest that the folding stops after the emergence of van der Waals energy, and the deformed 2D sheet will be obtained with a stable folded pattern; $\kappa_d^E=\kappa_d^G$ corresponds to the critical condition. Take the 2D material graphene as an example, Fig. A4a plots the variation of $\kappa_d^E$ and $\kappa_d^G$ with the area of 2D sheets under different pressures. At $P_t$=10 atm, small graphene sheets cannot be folded, in good consistence with $\kappa_d^E$<$\kappa_d^G$. With the increase of graphene sheet area, both $\kappa_d^E$ and $\kappa_d^G$ decrease, and after a critical large area of graphene sheet, $\kappa_d^E>\kappa_d^G$, indicating a successful self-folding of graphene by liquid evaporation. Define the graphene area as critical area $A_g^c$ at $\kappa_d^E=\kappa_d^G$. It decreases with the increase of evaporation pressure, suggesting that higher evaporation pressure promote the self-folding of graphene. Fig. A4b further gives the plots of $\kappa_d^E$ and $\kappa_d^G$ as a function of the evaporation pressure. At $A_g$=800 $nm^2$ and a low evaporation pressure, we always have $\kappa_d^E$<$\kappa_d^G$. With the increase of evaporation pressure, $\kappa_d^G$ decreases, and $\kappa_d^E$ increases, eventually leading to $\kappa_d^E>\kappa_d^G$. Beyond this, the self-folding of graphene will happen. Similar to the definition of $A_g^c$, we define the critical evaporation pressure as $P_t^c$ at $\kappa_d^E=\kappa_d^G$. Smaller $P_t^c$ is obtained for large areas of graphene sheet, indicating larger

![](./images/812737037911195649_26.jpg)

Fig. A3. Continuum mechanics analysis on evolution of local curvature and strain energy with the evaporation pressure for different areas of a single 2D sheet. (a) The local curvature distribution in a 2D sheet with $L_g$=100 nm under different pressures at $R_d$=50 nm. (b) The local curvature distribution in a 2D sheets with different size under the same pressure $P_t$=20 atm. The ratio of 2D sheet size to the radius of droplet is kept the same, $L_g/R_d$=2, to make sure the degree of deformation in each 2D sheet is the same. (c) Normalized strain energy $E_s/B$ by bending stiffness of 2D sheet versus the normalized pressure $\sqrt{P_t/E}$ by Young's modulus of 2D materials. The perfect linear relationship between them is obtained and remains for different sizes of 2D sheet. (d) Normalized strain energy $E_s/B$ by bending stiffness of 2D sheet versus normalized area $A_g/t^2$ with the thickness of 2D sheet. The perfect linear relationship between them is also obtained and is independent of evaporation pressures.

graphene is easier to be folded than smaller one by liquid evaporation. Further, Fig. A4c illustrates $A_g^c$ increases with the increase of layer numbers of graphene sheet (i.e. the bending stiffness, $B$) under the same evaporation pressure, indicating the 2D sheet with a lower bending stiffness is much easier to be folded. When the evaporation pressure changes, similar results are also obtained in Fig. A4d.

Based on these analyses and with the help of the dimensional analysis, we can summarize the relationship among the critical area $A_g^c$ of 2D sheets, the bending stiffness $B$ and the evaporation pressure $P_t$ and it can be written as

$$
A_g^c = \eta\left(\frac{B}{P_t}\right)^{\frac{2}{3}} \tag{A8}
$$

Eq. (A8) is confirmed by substituting it into Eqs. (A4) and (A7) with the same solutions between them. Fig. A5 shows the linear relationship between $A_g^c$ and $(B/P_t)^{2/3}$, which further validates the expression of Eq. (A8). Note that the $\eta$ =98.82 can be obtained by the best linear fit of the numerical solutions to Fig. A5, independent of bending stiffness of graphene and areas. We note that when the 2D sheet experiences uniform deformation, theoretical analysis shows $\eta=4\pi^2$ which has also been plotted in Fig. A5.

### Appendix B. Validation of solid-liquid interaction using a virtual spherical L-J force field and approach

The full-atom simulation system consisted of 4200 SPC/E water molecules (Mark and Nilsson, 2001) (corresponding the volume of water droplet $V$=125.55 nm³) and a graphene ribbon with the dimension of 20 nm × 2 nm. The AIREBO force

![](./images/812737037911195649_27.jpg)

Fig. A4. Variation of $\kappa_d^G$ and $\kappa_d^E$ with the area of graphene $A_g$ (a) under different evaporation pressure $P_t$ and (c) with different numbers of layers of graphene sheet (bending stiffness). Variation of $\kappa_d^G$ and $\kappa_d^E$ with the evaporation pressure $P_t$ for (b) different areas of graphene and (d) different numbers of layers of graphene sheet (bending stiffness). Both critical area $A_g^c$ and critical pressure $P_t^c$ are defined at $\kappa_d^G$=$\kappa_d^E$.

![](./images/812737037911195649_28.jpg)

Fig. A5. Relationship between the critical area $A_g^c$ and $(B/P_t)^{2/3}$. The points are extracted from the parameters of the numerical solutions of Eqs. (A4) and (A7) at $\kappa_d^E$=$\kappa_d^G$. All the points can be well linearly fitted with a slope of $\eta$=98.82. The relationship when the deformation is uniform ($\eta$=$4\pi^2$) can be derived in theory and is also included.

![](./images/812737037911195649_29.jpg)

Fig. A6. Determination of ridge density using the image processing procedure. (a) Local curvature distribution of the raw image from CGMD simulations.
(b) Image after converting the colored image to grayscale. (c) Image after the skeletonization to calculate the ridge density. .

![](./images/812737037911195649_30.jpg)

Fig. A7. Validation of the virtual sphere force field method. (a) Comparison of deformation energy ($E_{def}$) and binding energy ($E_{bind}$) of a single graphene
nanoribbon obtained by the full-atom water/graphene simulations and virtual spherical force field/full-atom graphene. (b) Snapshots of crumpled morphol-
ogy of graphene during simulations.

field was employed to model the flexible neutral graphene sheet (Brenner et al., 2002; Stuart et al., 2000). The 12–6 pairwise
Lennard-Jones potential $V(d)=4\epsilon(\sigma^{12}/d^{12}-\sigma^{6}/d^{6})$ was used to model the water-water and carbon-water non-bonded in-
teractions (Werder et al., 2003), where $\epsilon$ is the potential well depth, $\rho$ was the parameters associated with the equilibrium
distance and $d$ was the distance between two atoms. $\sigma_{O-O}$=0.3166 nm, $\epsilon_{C-O}$=0.0937 kcal/mole and $\sigma_{C-O}$=0.319 nm were
chosen to model the interaction between water molecules and graphene sheet. The simulation procedure includes three
steps: First, after energy minimization of the water and graphene sheet, NVT ensemble with Nose/Hoover thermostat was
employed for 1.0 ns with a time step of 1.0 fs to equilibrate the system at $300K$ and 1.0 atm. Secondly, 11 water molecules
were removed from the system for every 1000 time steps until all the water molecules were completely removed. During
these processes, the energy and position of water molecules and graphene sheet were monitored every 1000 time steps
to ensure the sufficient data recorded. Thirdly, after all the water molecules were evaporated, another 1.0 ns under NVE
ensemble was run to make sure the deformed graphene sheet reached the stable folded pattern.

When a virtual spherical force field was used in the simulations, all water molecules were replaced by a virtual sphere
with an initial radius of $R_{i}$=3.106 nm that is the same as the water droplet size of 4200 water molecules and the graphene
ribbon was kept the same. At the same time, Eq. (7) was used to calculate the overall pressure exerted on the graphene by
liquid evaporation and $P_{t}$=188.2 atm. This pressure was applied as a force to on each carbon atoms, i.e. $F_{b}$=0.0067 kcal/mole-
Å. In the simulations, First, after energy minimization of the graphene sheet, NVT ensemble with Nose/Hoover thermostat
was employed for 1.0 ns with a time step of 1.0 fs to equilibrate the system at $300K$ and 1.0 atm. Afterward, the radius of
sphere was decreased by following the law of $R_{d}$=$R_{i}-\frac{R_{i}}{0.381ns}(t-1ns)$ to ensure that the volume of sphere equals the volume
of water in the full-atom simulations at the same time steps of liquid evaporation. During this process, the variation of
energy, position of water molecules and graphene sheet were monitored every 1000 time steps to ensure the data recorded
sufficiently. In the last step, $R_{d}$=0 was set to run another 1.0 ns under NVE ensemble to make sure that the folded graphene
sheet reached a stable stage.

Fig. A7a plots the comparison of deformation energy ($E_{def}$) and binding energy ($E_{bind}$) of graphene ribbon between sim-
ulations by the full-atom water and graphene and the virtual sphere and full-atom graphene systems. Excellent agreement
between them is obtained. Note that the bit early emergence and consequent quick decrease of binding energy in the full-

![](./images/812737037911195649_31.jpg)

Fig. A8. Energy and morphology variation of a single layer graphene during the liquid evaporation. (a) Comparison of the deformation energy $E_{def}$ and binding energy $E_{bind}$ at $T_{f}$=300 K between the full driving force model and equivalent pressure model for a square graphene with $L_{g}$=100 nm during liquid evaporation. (b) Snapshots of the crumpled graphene under different driving force models.

atom simulations than that in the virtual spherical simulations is expected to result from the early partial contact of water liquid with the edge tips of graphene, and the consequent squeezing out of water liquid by the folded section of graphene, as shown in Fig. A7b. However, both final energies and morphologies of folded graphene after complete liquid evaporation or removal of virtual spheres agree with each other, which validates the employment of a virtual spherical force model in the simulations.

### Appendix C. Validation of the equivalent evaporation pressure model

To validate the proposed equivalent evaporation pressure model in Section 2.1, two parallel CGMD simulation on crum- pling a single graphene sheet via a virtual sphere were performed. The modeling and simulation procedure follows Section 3. Only the driving forces were different between the two simulations. For the full driving force model, a constant force point- ing to the center of sphere was added on each CG bead to represent the contribution of gas pressure ($P_{g}$) and vapor pressure ($P_{v}$). At the same time, another force with constant magnitude was added on each CG bead at the boundary of graphene to represent the capillary force ($F_{c}$). The direction of force is always perpendicular to the initial orientation of the bound- ary after it was added and is also always tangential to the surface of sphere. For the equivalent evaporation driving force model, a constant force pointing to the center of sphere was added on each CG bead of the graphene to represent the total equivalent pressure ($P_{t}$). The length of graphene was $L_{g}$=100 nm, and the initial radius of sphere was $R_{i}$=100 nm and the final radius of sphere was $R_{e}$=1 nm. The time of equilibrium was $t_{i}$=1 ns, and the time of evaporation was $t_{e}$=2 ns. After the evaporation, another 1 ns was following to make sure the final folded pattern was stable.

Fig. A8a plots the variation of deformation energy $E_{def}$ and binding energy $E_{bind}$ during the folding. $E_{def}$ increases slowly at the beginning of evaporation, followed by a quick increase after a critical evaporation time. After that, it arrives at an approximate stable stage. By contrast, $E_{bind}$ remains zero at the beginning, followed by a quick decrease at the moment when there is a significant increase of $E_{def}$ and then reaches a stable stage. More importantly, both $E_{def}$ and $E_{bind}$ have been well predicted by the equivalent evaporation pressure model (Eq. (7)), with good agreement with those from full- force model. The non-zero of $E_{bind}$ indicates the occurrence of self-folding in the graphene, which is also consistent with a quick increase of $E_{def}$. The final non-zero stable $E_{def}$ and $E_{bind}$ suggest that the deformed graphene by evaporation of liquid possess a stable morphology. Fig. A8b shows the snapshots of simulations, and the deformation evolution of graphene with evaporation time, ranging from the initial bending deformation, to self-folding and to a final stable crumpled pattern, is observed, which corresponds well with variation of $E_{def}$ and $E_{bind}$. Besides, good agreement of these deformation patterns with approximately the same curvature from the equivalent pressure model (Eq. (7)) and full force model is obtained.

### References

Akinwande, D., Brennan, C.J., Bunch, J.S., Egberts, P., Felts, J.R., Gao, H., Huang, R., Kim, J.-S., Li, T., Li, Y., Liechti, K.M., Lu, N., Park, H.S., Reed, E.J., Wang, P., Yakobson, B.I., Zhang, T., Zhang, Y.-W., Zhou, Y., Zhu, Y., 2017. A review on mechanics and mechanical properties of 2D materials-Graphene and beyond. Extreme Mech. Lett. 13, 42-77.

Bao, W., Miao, F., Chen, Z., Zhang, H., Jang, W., Dames, C., Lau, C.N., 2009. Controlled ripple texturing of suspended graphene and ultrathin graphite mem- branes. Nat. Nanotechnol. 4, 562-566.

Brau, F., Damman, P., Diamant, H., Witten, T.A., 2013. Wrinkle to fold transition: influence of the substrate response. Soft Matter 9, 8177.

Brenner, D.W., Shenderova, O.A., Harrison, J.A., Stuart, S.J., Ni, B., Sinnott, S.B., 2002. A second-generation reactive empirical bond order (REBO) potential energy expression for hydrocarbons. J. Phys. Condens. Matter 14, 783.

Cao, X., Yin, Z., Zhang, H., 2014. Three-dimensional graphene materials: preparation, structures and application in supercapacitors. Energy Environ. Sci. 7, 1850-1865.

Cerda, E., Chaieb, S., Melo, F., Mahadevan, L., 1999. Conical dislocations in crumpling. Nature 401, 46.

Chen, F., Smith, P.E., 2007. Simulated surface tensions of common water models. J. Chem. Phys. 126, 221101.

Chen, X., Yi, C., Ke, C., 2015. Bending stiffness and interlayer shear modulus of few-layer graphene. Appl. Phys. Lett. 106, 101907.

Chen, Y.-C., Lu, A.-Y., Lu, P., Yang, X., Jiang, C.-M., Mariano, M., Kaehr, B., Lin, O., Taylor, A., Sharp, I.D., Li, L.-J., Chou, S.S., Tung, V., 2017a. Structurally deformed mos2 for electrochemically stable, thermally resistant, and highly efficient hydrogen evolution reaction. Adv. Mater. 29, 1703863.

Chen, Z., Wang, J., Umar, A., Wang, Y., Li, H., Zhou, G., 2017b. Three-Dimensional crumpled graphene-based nanosheets with ultrahigh NO₂ gas sensibility. ACS Appl. Mater. Inter. 9, 11819-11827.

Choi, S.H., Ko, Y.N., Lee, J.-K., Kang, Y.C., 2014. Rapid continuous synthesis of spherical reduced graphene ball-Nickel oxide composite for lithium ion batteries. Sci. Rep. 4, 5786.

Ciarletta, P., 2014. Wrinkle-to-fold transition in soft layers under equi-biaxial strain: a weakly nonlinear analysis. J. Mech. Phys. Solids 73, 118-133.

Cranford, S.W., Buehler, M.J., 2011. Packing efficiency and accessible surface area of crumpled graphene. Phys. Rev. B 84, 205451.

Deegan, R.D., Bakajin, O., Dupont, T.F., Huber, G., Nagel, S.R., Witten, T.A., 1997. Capillary flow as the cause of ring stains from dried liquid drops. Nature 389, 827.

Deng, S., Berry, V., 2016. Wrinkled, rippled and crumpled graphene: an overview of formation mechanism, electronic properties, and applications. Mater. Today 19, 197-212.

Diamant, H., Witten, T.A., 2011. Compression induced folding of a sheet: an integrable system. Phys. Rev. Lett. 107, 164302.

Dou, X., Koltonow, A.R., He, X., Jang, H.D., Wang, Q., Chung, Y.-W., Huang, J., 2016. Self-dispersed crumpled graphene balls in oil for friction and wear reduction. Proc. Natl. Acad. Sci. 113, 1528-1533.

Faber, J.A., Arrieta, A.F., Studart, A.R., 2018. Bioinspired spring origami. Science 359, 1386-1391.

Fan, X., Chen, X., Dai, L., 2015. 3D graphene based materials for energy storage. Curr. Opin. Coll. Interface Sci. 20, 429-438.

Freire, M.G., Carvalho, P.J., Fernandes, A.M., Marrucho, I.M., Queimada, A.J., Coutinho, J.A., 2007. Surface tensions of imidazolium based ionic liquids: anion, cation, temperature and water effect. J. Colloid Interface Sci. 314, 621-630.

Gillis, P.P., 1984. Calculating the elastic constants of graphite. Carbon 22, 387-391.

Gonzalez, M., Cuitiño, A.M., 2012. A nonlocal contact formulation for confined granular systems. J. Mech. Phys. Solids 60, 333-350.

Ha, T., Kim, S.K., Choi, J.-W., Chang, H., Jang, H.D., 2019. pH controlled synthesis of porous graphene sphere and application to supercapacitors. Adv. Powder Technol. 30, 18-22.

Haberman, R., 2012. Applied Partial Differential Equations With Fourier Series and Boundary Value Problems. Pearson Higher Ed.

Hao, W., Chiou, K., Qiao, Y., Liu, Y., Song, C., Deng, T., Huang, J., 2018. Crumpled graphene ball-based broadband solar absorbers. Nanoscale 10, 6306-6312.

Hibbeler, R., 2011. Mechanical Properties of Materials. Mechanics of Materials. Prentice Hall, pp. 81-117.

Holmes, D.P., Crosby, A.J., 2010. Draping films: a wrinkle to fold transition. Phys. Rev. Lett. 105, 038303.

Holyst, R., Litniewski, M., Jakubczyk, D., Kolwas, K., Kolwas, M., Kowalski, K., Migacz, S., Palesa, S., Zientara, M., 2013. Evaporation of freely suspended single droplets: experimental, theoretical and computational simulations. Rep. Prog. Phys. Soc. 76, 034601.

Hsu, M.F., Nikolaides, M.G., Dinsmore, A.D., Bausch, A.R., Gordon, V.D., Chen, X., Hutchinson, J.W., Weitz, D.A., Marquez, M., 2005. Self-assembled shells composed of colloidal particles: fabrication and characterization. Langmuir 21, 2963-2970.

Hu, H., Larson, R.G., 2005. Analysis of the microfluid flow in an evaporating sessile droplet. Langmuir 21, 3963-3971.

Hure, J., Audoly, B., 2013. Capillary buckling of a thin film adhering to a sphere. J. Mech. Solids 61, 450-471.

Jambon-Puillet, E., Vella, D., Protiere, S., 2016. The compression of a heavy floating elastic film. Soft Matter 12, 9289-9296.

Jiang, Y., Raliya, R., Fortner, J.D., Biswas, P., 2016. Graphene oxides in water: correlating morphology and surface chemistry with aggregation behavior. Environ Sci. Technol. 50, 6964-6973.

Jin, L., Takei, A., Hutchinson, J.W., 2015. Mechanics of wrinkle/ridge transitions in thin film/substrate systems. J. Mech. Phys. Solids 81, 22-40.

Kavadiya, S., Raliya, R., Schrock, M., Biswas, P., 2017. Crumpling of graphene oxide through evaporative confinement in nanodroplets produced by electrohydrodynamic aerosolization. J. Nanopart. Res. 19, 43.

Kim, J., Cote, L.J., Kim, F., Huang, J., 2009. Visualizing graphene based sheets by fluorescence quenching microscopy. J. Am. Chem. Soc. 132, 260-267.

Kim, J., Cote, L.J., Kim, F., Yuan, W., Shull, K.R., Huang, J., 2010. Graphene oxide sheets at interfaces. J. Am. Chem. Soc. 132, 8180-8186.

King, H., Schroll, R.D., Davidovitch, B., Menon, N., 2012. Elastic sheet on a liquid drop reveals wrinkling and crumpling as distinct symmetry-breaking instabilities. Proc. Natl. Acad. Sci. 109, 9716-9720.

Krueger, M., Berg, S., Stone, D.A., Strelcov, E., Dikin, D.A., Kim, J., Cote, L.J., Huang, J., Kolmakov, A., 2011. Drop-casted self-assembling graphene oxide membranes for scanning electron microscopy on wet and dense gaseous samples. ACS Nano 5, 10047-10054.

Lauga, E., Brenner, M.P., 2004. Evaporation-driven assembly of colloidal particles. Phys. Rev. Lett. 93, 238301.

Li, H., Guo, X., Nuzzo, R.G., Jimmy Hsia, K., 2010. Capillary induced self-assembly of thin foils into 3Dstructures. J. Mech. Solids 58, 2033-2042.

Li, H., Tao, Y., Zheng, X., Li, Z., Liu, D., Xu, Z., Luo, C., Luo, J., Kang, F., Yang, Q.-H., 2015. Compressed porous graphene particles for use as supercapacitor electrodes with excellent volumetric performance. Nanoscale 7, 18459-18463.

Liang, H., Acton, S.T., Weller, D.S., 2017. Content-aware neuron image enhancement. In: 2017 IEEE International Conference on Image Processing (ICIP). IEEE, pp. 3510-3514.

Lim, T., Lee, J., Lee, J., Ju, S., 2017. Detection of chemicals in water using a three-dimensional graphene porous structure as liquid-vapor separation filter. Nano Res. 10, 971-979.

Ling, Y., Zhuang, X., Xu, Z., Xie, Y., Zhu, X., Xu, Y., Sun, B., Lin, J., Zhang, Y., Yan, Z., 2018. Mechanically assembled, three-dimensional hierarchical structures of cellular graphene with programmed geometries and outstanding electromechanical properties.. ACS Nano 12, 12456-12463.

Liu, Q., Gao, Y., Xu, B., 2016. Liquid evaporation-driven folding of graphene sheets. Appl. Phys. Lett. 108, 141906.

Liu, Q., Xu, B., 2016. A unified mechanics model of wettability gradient-driven motion of water droplet on solid surfaces. Extreme Mech. Lett. 9, 304-309.

Liu, Q., Xu, B., 2018. Two- and three-dimensional self-folding of free-standing graphene by liquid evaporation. Soft Matter 14, 5968-5976.

Liu, S., Wang, A., Li, Q., Wu, J., Chiou, K., Huang, J., Luo, J., 2018. Crumpled graphene balls stabilized dendrite-free lithium metal anodes. Joule 2, 184-193.

Lu, Q., Huang, R., 2010. Excess energy and deformation along free edges of graphene nanoribbons. Phys. Rev. B 81, 155410.

Luo, J., Cote, L.J., Tung, V.C., Tan, A.T., Goins, P.E., Wu, J., Huang, J., 2010. Graphene oxide nanocolloids. J. Am. Chem. Soc. 132, 17667-17669.

Luo, J., Gao, J., Wang, A., Huang, J., 2015. Bulk nanostructured materials based on two-dimensional building blocks: a roadmap. ACS Nano 9, 9432-9436.

Luo, J., Jang, H.D., Huang, J., 2013a. Effect of sheet morphology on the scalability of graphene-based ultracapacitors. ACS Nano 7, 1464-1471.

Luo, J., Jang, H.D., Sun, T., Xiao, L., He, Z., Katsoulidis, A.P., Kanatzidis, M.G., Gibson, J.M., Huang, J., 2011. Compression and aggregation-resistant particles of crumpled soft sheets. ACS Nano 5, 8943-8949.

Luo, J., Kim, J., Huang, J., 2013b. Material processing of chemically modified graphene: some challenges and solutions. Acc. Chem. Res. 46, 2225-2234.

Luo, J., Zhao, X., Wu, J., Jang, H.D., Kung, H.H., Huang, J., 2012. Crumpled graphene-encapsulated si nanoparticles for lithium ion battery anodes. J. Phys. Chem. Lett. 3, 1824-1829.

Ma, X., Zachariah, M.R., Zangmeister, C.D., 2012. Crumpled nanopaper from graphene oxide. Nano Lett. 12, 486-489.

Mao, S., Wen, Z., Kim, H., Lu, G., Hurley, P., Chen, J., 2012. A general approach to one-pot fabrication of crumpled graphene-based nanohybrids for energy applications. ACS Nano 6, 7505-7513.

Mark, P., Nilsson, L., 2001. Structure and dynamics of the TIP3P, SPC, and spc/e water models at 298 K. J. Phys. Chem. A 105, 9954-9960.

Matan, K., Williams, R.B., Witten, T.A., Nagel, S.R., 2002. Crumpling a thin sheet. Phys. Rev. Lett. 88, 076101.

Mendoza-Sanchez, B., Gogotsi, Y., 2016. Synthesis of two-dimensional materials for capacitive energy storage. Adv. Mater. 28, 6104-6135.

Mora, T., Boudaoud, A., 2002. Thin elastic plates: on the core of developable cones. EPL (Europhys. Lett.) 59, 41.

Nie, Y., Wang, Y., Biswas, P., 2017. Mobility and bipolar diffusion charging characteristics of crumpled reduced graphene oxide nanoparticles synthesized in a furnace aerosol reactor. J. Phys. Chem. C 121, 10529-10537.

Nikolayev, V.S., Chatain, D., Garrabos, Y., Beysens, D., 2006. Experimental evidence of the vapor recoil mechanism in the boiling crisis. Phys. Rev. Lett. 97, 184503.

Okuyama, K., Wuled Lenggoro, I., 2003. Preparation of nanoparticles via spray route. Chem. Eng. Sci. 58, 537-547.

Ortolani, L., Cadelano, E., Veronese, G.P., Boschi, C.D., Snoeck, E., Colombo, L., Morandi, V., 2012. Folded graphene membranes: mapping curvature at the nanoscale. Nano Lett. 12, 5207-5212.

Oshri, O., Brau, F., Diamant, H., 2015. Wrinkles and folds in a fluid-supported sheet of finite size. Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 91, 052408.

Park, S.-H., Kim, H.-K., Yoon, S.-B., Lee, C.-W., Ahn, D., Lee, S.-I., Roh, K.C., Kim, K.-B., 2015. Spray-assisted deep-frying process for the in situ spherical assembly of graphene for energy-storage devices. Chem. Mater. 27, 457-465.

Parviz, D., Metzler, S.D., Das, S., Irin, F., Green, M.J., 2015. Tailored crumpling and unfolding of spray-dried pristine graphene and graphene oxide sheets. Small 11, 2661-2668.

Paulsen, J.D., Demery, V., Santangelo, C.D., Russell, T.P., Davidovitch, B., Menon, N., 2015. Optimal wrapping of liquid droplets with ultrathin sheets. Nat. Mater. 14, 1206-1209.

Plimpton, S., Crozier, P., Thompson, A., 2007. LAMMPS-large-scale atomic/molecular massively parallel simulator. Sandia Natl. Lab. 18, 43.

Qin, Z., Jung, G.S., Kang, M.J., Buehler, M.J., 2017. The mechanics and design of a lightweight three-dimensional graphene assembly. Sci. Adv. 3, e1601536.

Qiu, L., Liu, J.Z., Chang, S.L.Y., Wu, Y., Li, D., 2012. Biomimetic superelastic graphene-based cellular monoliths. Nat. Commun. 3, 1241.

Ramanathan, T., Abdala, A.A., Stankovich, Dikin, D.A., Herrera Alonso, M., Piner, R.D., Adamson, D.H., Schniepp, H.C., Chen, X., Ruoff, R.S., Nguyen, S.T., Aksay, I.A., Prud'Homme, R.K., Brinson, L.C., 2008. Functionalized graphene sheets for polymer nanocomposites. Nat. Nanotechnol. 3, 327-331.

Reddy, C.D., Zhang, Y.-W., 2014. Structure manipulation of graphene by hydrogenation. Carbon 69, 86-91.

Ruiz, L., Xia, W., Meng, Z., Keten, S., 2015. A coarse-grained model for the mechanical behavior of multi-layer graphene. Carbon 82, 103-115.

Schmatko, T., Hervet, H., Leger, L., 2005. Friction and slip at simple fluid-solid interfaces: the roles of the molecular shape and the solid-liquid interaction. Phys. Rev. Lett. 94.

Shehzad, K., Xu, Y., Gao, C., Duan, X., 2016. Three-dimensional macro-structures of two-dimensional nanomaterials. Chem. Soc. Rev. 45, 5541-5588.

Shenoy, V.B., Reddy, C.D., Ramasubramaniam, A., Zhang, Y.W., 2008. Edge-stress-induced warping of graphene sheets and nanoribbons. Phys. Rev. Lett. 101, 245501.

Shenoy, V.B., Reddy, C.D., Zhang, Y.-W., 2010. Spontaneous curling of graphene sheets with reconstructed edges. ACS Nano 4, 4840-4844.

Shim, J., Yun, J.M., Yun, T., Kim, P., Lee, K.E., Lee, W.J., Ryoo, R., Pine, D.J., Yi, G.R., Kim, S.O., 2014. Two-minute assembly of pristine large-area graphene based films. Nano Lett. 14, 1388-1393.

Stuart, S.J., Tutein, A.B., Harrison, J.A., 2000. A reactive potential for hydrocarbons with intermolecular interactions. J. Chem. Phys. 112, 6472-6486.

Sudeep, P.M., Narayanan, T.N., Ganesan, A., Shaijumon, M.M., Yang, H., Ozden, S., Patra, P.K., Pasquali, M., Vajtai, R., Ganguli, S., Roy, A.K., Anantharaman, M.R., Ajayan, P.M., 2013. Covalently interconnected three-dimensional graphene oxide solids. ACS Nano 7, 7034-7040.

Sugden, S., 1924. VI.—The variation of surface tension with temperature and some related functions. J. Chem. Soc. Trans. 125, 32-41.

Tao, Y., Xie, X., Lv, W., Tang, D.-M., Kong, D., Huang, Z., Nishihara, H., Ishii, T., Li, B., Golberg, D., Kang, F., Kyotani, T., Yang, Q.-H., 2013. Towards ultrahigh volumetric capacitance: graphene derived highly dense but porous carbons for supercapacitors. Sci. Rep. 3, 2975.

Tarasevich, Y.Y., 2005. Simple analytical model of capillary flow in an evaporating sessile drop. Phys. Rev. E Stat. Nonlin. Soft Matter Phys. 71, 027301.

Thomson, W., 1872. 4. On the equilibrium of vapour at a curved surface of liquid. Proc. R. Soc. Edinb. 7, 63-68.

Tocci, G., Joly, L., Michaelides, A., 2014. Friction of water on graphene and hexagonal boron nitride from ab initio methods: very different slippage despite very similar interface structures. Nano Lett. 14, 6872-6877.

Vincenti, W.G., Kruger, C.H., 1965. Introduction to Physical Gas Dynamics. Wiley, New York.

Vliegenthart, G.A., Gompper, G., 2006. Forced crumpling of self-avoiding elastic sheets. Nat. Mater. 5, 216-221.

Vogel, N., Retsch, M., Fustin, C.A., Del Campo, A., Jonas, U., 2015. Advances in colloidal assembly: the design of structure and hierarchy in two and three dimensions. Chem. Rev. 115, 6265-6311.

Wang, W.N., Jiang, Y., Biswas, P., 2012. Evaporation-Induced crumpling of graphene oxide nanosheets in aerosolized droplets: confinement force relationship. J. Phys. Chem. Lett. 3, 3228-3233.

Warner, J.H., Fan, Y., Robertson, A.W., He, K., Yoon, E., Lee, G.D., 2013. Rippling graphene at the nanoscale through dislocation addition. Nano Lett. 13, 4937-4944.

Warner, J.H., Margine, E.R., Mukai, M., Robertson, A.W., Giustino, F., Kirkland, A.I., 2012. Dislocation-driven deformations in graphene. Science 337, 209-212.

Werder, T., Walther, J.H., Jaffe, R., Halicioglu, T., Koumoutsakos, P., 2003. On the water- carbon interaction for use in molecular dynamics simulations of graphite and carbon nanotubes. J. Phys. Chem. B 107, 1345-1352.

Wu, Y., Yi, N., Huang, L., Zhang, T., Fang, S., Chang, H., Li, N., Oh, J., Lee, J.A., Kozlov, M., Chipara, A.C., Terrones, H., Xiao, P., Long, G., Huang, Y., Zhang, F., Zhang, L., Lepró, X., Haines, C., Lima, M.D., Lopez, N.P., Rajukumar, L.P., Elias, A.L., Feng, S., Kim, S.J., Narayanan, N.T., Ajayan, P.M., Terrones, M., Aliev, A., Chu, P., Zhang, Z., Baughman, R.H., Chen, Y., 2015. Three-dimensionally bonded spongy graphene material with super compressive elastic- ity and near-zero Poisson's ratio. Nat. Commun. 6, 6141.

Xu, B., Rogers, J.A., 2016. Mechanics-driven approaches to manufacturing-A perspective. Extreme Mech. Lett. 7, 44-48.

Yang, H., Wang, Y., Song, Y., Qiu, L., Zhang, S., Li, D., Zhang, X., 2012. Assembling of graphene oxide in an isolated dissolving droplet. Soft Matter 8, 11249.

Yang, J., Sun, H., Liang, H., Ji, H., Song, L., Gao, C., Xu, H., 2016. A highly efficient metal-free oxygen reduction electrocatalyst assembled from carbon nanotubes and graphene. Adv. Mater. 28, 4606-4613.

Yang, X., Cheng, C., Wang, Y., Qiu, L., Li, D., 2013. Liquid-Mediated dense integration of graphene materials for compact capacitive energy storage. Science 341, 534-537.

Yavari, F., Chen, Z., Thomas, A.V., Ren, W., Cheng, H.-.M., Koratkar, N., 2011. High sensitivity gas detection using a macroscopic three-dimensional graphene foam network. Sci. Rep. 1, 166.

Ye, Z., Tang, C., Dong, Y., Martini, A., 2012. Role of wrinkle height in friction variation with number of graphene layers. J. Appl. Phys. 112, 116102.

Zang, J., Cao, C., Feng, Y., Liu, J., Zhao, X., 2014. Stretchable and high-performance supercapacitors with crumpled graphene papers. Sci. Rep. 4, 6492.

Zhang, K., Arroyo, M., 2014. Understanding and strain-engineering wrinkle networks in supported graphene through simulations. J. Mech. Phys. Solids 72, 61-74.

Zhang, L., Liang, J., Huang, Y., Ma, Y., Wang, Y., Chen, Y., 2009. Size-controlled synthesis of graphene oxide sheets on a large scale using chemical exfoliation. Carbon 47, 3365-3368.

Zhang, L., Zhang, F., Yang, X., Long, G., Wu, Y., Zhang, T., Leng, K., Huang, Y., Ma, Y., Yu, A., Chen, Y., 2013. Porous 3D graphene-based bulk materials with exceptional high surface area and excellent conductivity for supercapacitors. Sci. Rep. 3, 1408.

Zhang, Q., Yin, J., 2018. Spontaneous buckling-driven periodic delamination of thin films on soft substrates under large compression. J. Mech. Phys. Solids 118, 40-57.

Zheng, Q., Geng, Y., Wang, S., Li, Z., Kim, J.-K., 2010. Effects of functional groups on the mechanical and wrinkling properties of graphene sheets. Carbon 48, 4315-4322.

Zhou, Y., Chen, Y., Liu, B., Wang, S., Yang, Z., Hu, M., 2015. Mechanics of nanoscale wrinkling of graphene on a non-developable surface. Carbon 84, 263-271.

Zhou, Y., Hu, X.-C., Fan, Q., Wen, H.-R., 2016. Three-dimensional crumpled graphene as an electro-catalyst support for formic acid electro-oxidation. J. Mater. Chem. A 4, 4587-4591.

Zhu, W., Low, T., Perebeinos, V., Bol, A.A., Zhu, Y., Yan, H., Tersoff, J., Avouris, P., 2012. Structure and electronic transport in graphene wrinkles. Nano Lett. 12, 3431-3436.

Zou, J., Kim, F., 2014. Diffusion driven layer-by-layer assembly of graphene oxide nanosheets into porous three-dimensional macrostructures. Nat. Commun. 5, 5254.