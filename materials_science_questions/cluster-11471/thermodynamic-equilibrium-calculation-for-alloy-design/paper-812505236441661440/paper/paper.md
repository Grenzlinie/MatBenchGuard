ORIGINAL RESEARCH ARTICLE

# A Thermo-metallurgical Model for Laser Surface Engineering Treatment of Nodular Cast Iron

![](./images/812505236441661440_1.jpg)

A.D. BOCCARDO, N. CATALÁN, D.J. CELENTANO, and E. RAMOS-MOORE

Heat treatments are frequently used to modify the microstructure of cast irons according to experimental parameters. Among these, laser surface engineering (LSE) has become relevant for being a highly localized treatment with rapid heating and cooling of the irradiated area resulting in minimal distortion of the workpiece. This work presents and experimentally validates a thermo-metallurgical model able to predict the phase transformations occurring during the LSE treatment of nodular cast iron when it is subjected to different laser beam powers and scanning velocities. For this purpose, an experimental characterization of the thermal history and final microstructure is performed for several operating scenarios. In particular, significant changes in the microstructure can be seen at high powers and low scanning velocity where the matrix is transformed into ledeburite and martensite. The final phase volume fractions predicted by the proposed model along the depth of the sample are compared with the corresponding experimental measurements. The results obtained in the simulation are in good agreement with the experimental measurements. This work highlights the use of our model to be systematically applied for the design and optimization of LSE treatments on cast irons.

https://doi.org/10.1007/s11663-021-02058-0
© The Minerals, Metals & Materials Society and ASM International 2021

## I. INTRODUCTION

DEPENDING on the production process, there are several types of Fe-C alloys, with gray (or lamellar, GCI) and nodular (or ductile, NCI) cast irons being some of the most frequent. While the graphite is present in the form of flakes in the GCI, the graphite is spherically distributed in the NCI due to the nodulizing action of, *e.g.*, Mg. In particular, the use of NCI has been increased in the last century due to its mechanical properties, such as high machinability and ductility, and its low production cost compared to other metal alloys and steels. In heavy or high-demand industries, such as automobile and mining, nodular iron is used in the manufacture of axles, pistons, gears and connecting rods. $^{[1]}$

In general, these alloys should be heat treated to improve their hardness and resistance to wear, erosion and fatigue, among others, and thus avoid early failures in their operation. Various conventional heat treatments have been applied to metallic materials, such as normalized, annealed and tempered. In these processes, the sample is heated in an oven and then cooled to different rates, which changes the microstructure of the material as a whole. In many applications, it is not required to alter the microstructure and properties of the entire piece. As a result, localized thermal treatments have been developed in recent decades, which allow hardening and improving the surface resistance of the material, keeping the rest of the sample intact. Recent technologies developed to this end encompass the tungsten inert gas arc, the electron beam, the plasma-transferred arc, and the laser surface transformation also referred to as laser surface engineering (LSE). The LSE processes can be classified in laser surface melting (LSM) and laser surface hardening (LSH) treatments depending on whether fusion or a solid transformation in the base material occurs, as shown in the pioneering work of Bergmann. $^{[2]}$

A.D. BOCCARDO is with the Instituto de Estudios Avanzados en Ingeniería y Tecnología, IDIT, CONICET-Universidad Nacional de Córdoba, Vélez Sarsfield 1611, X5000 Córdoba, Argentina and Grupo de Investigación y Desarrollo en Mecánica Aplicada, GIDMA, Facultad Regional Córdoba, Universidad Tecnológica Nacional, Maestro M. López esq. Cruz Roja Argentina, X5000 Córdoba, Argentina. Contact e-mail: aboccardo@frc.utn.edu.ar N. CATALÁN is with the Departamento de Ingeniería Mecánica y Metalúrgica, Pontificia Universidad Católica de Chile, Av. Vicuña Mackenna 4860, 7820436 Macul, Santiago de Chile, Chile. D.J. CELENTANO is with the Departamento de Ingeniería Mecánica y Metalúrgica, Pontificia Universidad Católica de Chile and Centro de Investigación en Nanotecnología y Materiales Avanzados (CIEN-UC), Pontificia Universidad Católica de Chile, Av. Vicuña Mackenna 4860, 7820436 Macul, Santiago, Chile. E. RAMOS-MOORE is with the Instituto de Física, Facultad de Física, Pontificia Universidad Católica de Chile and also with the Centro de Investigación en Nanotecnología y Materiales Avanzados (CIEN-UC), Pontificia Universidad Católica de Chile, Casilla 306, Av. Vicuña Mackenna 4860, 7820436 Macul, Santiago, Chile.

Manuscript submitted October 2, 2020; accepted December 18, 2020.
Article published online February 8, 2021.

854—VOLUME 52B, APRIL 2021
METALLURGICAL AND MATERIALS TRANSACTIONS B

The LSE treatment has received particular attention because it has relevant advantages such as high energy density, minimal distortion of the treated sample, highly localized application, direct control of the procedure variables (laser scan speed and power, among others) and absence of quenching media. In this treatment, a laser beam travels along a path defined on the surface of the piece, transferring high amounts of energy that raise its temperature to the point where either the transformation of the base matrix begins (which can be ferrite, pearlite, austenite or a combination of them) or its fusion occurs. As the rest of the material is not affected by the laser as is maintained at room temperature, rapid self-cooling of the heated zone occurs, typically at rates in the order of 1000 °C/s, through which the microstructure reaches its final state. $^{[3-5]}$ Mainly experimental works have been carried out in the last decades for laser surface treatments in both GCI and NCI, the latter encompassing pearlitic, austempered (ADI) and ferritic structures. These works generally focused on the study of the influence of LSE treatments on the microstructure and its effects on the hardness and wear performance. To the best of our knowledge, few works are devoted to the understanding of such effects through modeling and numerical simulation of LSE treatments on these three alloys. In this regard, a brief synthesis of the main theoretical works is described herein.

Gadag et al. $^{[6]}$ analyzed the effect of the operating parameters of a LSE treatment on the microstructure of hypereutectic pearlitic NCI samples obtaining, from microscopic observation, that the microstructure as a function of the depth has three parts: a region of fusion with a homogeneous microstructure consisting mainly of ledeburite, eutectic austenite and cementite, an area whose microstructure varies between martensite and fine pearlite, and a small area where the microstructure changes rapidly towards that present in the material outside the region affected by the laser. In addition, the authors performed a numerical simulation of the evolution of the temperature during the treatment that allows establishing an evaluation of the depth and shape of the affected areas obtained in terms of the isotherms corresponding to the equilibrium liquidus, critical transformation and solidus temperatures.

Roy and Manna $^{[7]}$ developed an analytical model to predict the temperature in the vicinity of graphite nodules in ADI samples treated with a $CO_2$ continuous wave laser with Gaussian distribution profile such that the temperature profile is used to determine, according to Fick's law, the carbon diffusion from the graphite nodules. The carbon concentration is in turn considered to estimate, from the Fe-C-Si phase diagram, if melting occurs for a specific set of laser operating parameters. From these results, the authors concluded that when the fusion area is negligible with respect to the distribution of nodules in the matrix, the microstructure is predominantly martensitic.

The first modeling of the transformations in ferritic NCIs has been reported by Grum and Sturm $^{[8]}$, where a low-power $CO_2$ laser treatment is carried out with overlapping to ensure the melting of the surface of the samples. Three regions with well-differentiated microstructure are originated after the treatment: the fusion zone, the hardened zone and an intermediate transition zone. In the region where the liquidus temperature is exceeded, the predominantly ferritic matrix melts, and the graphite nodules diffuse towards the melted surface. This causes a strong dissolution of the carbon in the liquid matrix, whose rapid solidification transforms it into dendrites of austenite and ledeburite. The intermediate zone is characterized by a highly localized fusion process around the graphite nodules which, depending on the magnitude of the carbon diffusion towards their edges, can generate a ring of ledeburite and martensite. The differences between the transition and hardening zones are that although the matrix becomes austenite during heat transfer and it is enriched in carbon product of diffusion from the graphite nodules, this is not enough to decrease the melting point locally around them, whereby the matrix becomes a martensitic type with residual austenite. In addition, due to the heterogeneous distribution of the nodules, there are areas with low carbon content where the austenite is transformed back to ferrite during the cooling.

In a later work by Grum and Sturm $^{[9]}$, the analysis of the LSM treatment in ferritic NCIs is completed by comparing, experimentally and numerically, the thickness of the layers of martensite and ledeburite surrounding the graphite nodules in the transition and hardening zones. As described by Roy and Manna $^{[7]}$, based on simplified temperature models during the heating and cooling cycle together with diffusion equations based on the Fick's law, the authors determined, at different depths, whether the temperature reached around the nodule is sufficient to produce melting (and the formation of ledeburite when cooled), in addition to calculating the magnitude of the outwards radial diffusion of carbon atoms. The simulation accurately adjusts the experimentally observed thicknesses of the ledeburite and martensite layers formed around the graphite nodules.

Pagano et al. $^{[10]}$ reported a complete analysis of the effects of the LSM technique on ferritic NCIs by means of a Nd-YAG laser of circular shape and Gaussian distribution. In the area where melting occurs, the microstructure becomes a network of dendrites of austenite and ledeburite, with a small portion of martensite. Then, a transition region is established with fusion located around the graphite nodules that did not melt. Moreover, a hardened area can also be seen, where the graphite spheres are surrounded by a layer of martensite and immersed in a matrix of ferrite and residual austenite. These results corroborate the work of Grum and Sturm. $^{[8]}$ In addition, a thermal model is used to simulate the temperature profiles along the sample depth during the treatment, with the aim of predicting and assessing, from the austenization temperature of the material, the depth of the LSM transformed zone.

Although the mentioned works presented novel ideas to model the laser surface heat treatment of cast irons, the prediction of the thermal history considering parts of infinite length $^{[6]-[9]}$ and the non-computation of solid state phase changes during the heating up and cooling

down limit their application when small samples are treated or detailed information of the microstructure at the end of the heat treatment is required.

This work presents a unidirectional coupled thermo-metallurgical model to predict during the LSE treatment the microstructure of NCIs whose metallic matrix can be initially constituted by ferrite, fer-rite-pearlite, or pearlite. Throughout the treatment, the temperature evolution of finite size parts is computed at the macroscale by means of a thermal model that is solved with the finite element method. The domain temperature is passed to the metallurgical model in order to compute the phase evolutions by taking into account the solid-solid, solid-liquid, and liquid-solid phase transformations that commonly occur in the process. The heat treatment model is presented in Section 2, paying special attention to the metallurgical model that allows to take into account the different phase changes that take place during the process. Section 3 presents the studied cases, results and their discussion where, in particular, the predicted results of temperature evolution and final phase volume fractions, at different domain positions, are compared with experimental results. In this study, the proposed model is specifically applied and experimentally validated to simulate the LSE of ferritic and pearlitic-ferritic NCI samples irradiated with lasers having a rectangular beam with different spatial energy distributions. The analyzed cases take into account different laser operating scenarios, such as different combinations of laser power and scanning velocity.

## II. DEVELOPMENT OF THE HEAT TREATMENT MODEL

A thermo-metallurgical model with unidirectional coupling is employed to simulate the laser surface heat treatment on NCI. The thermal model computes the temperature evolution during the process while the metallurgical model predicts the phase evolution as a function of the temperature. Both models are separately described below.

The thermo-metallurgical model was computationally implemented in standard finite element program extensively used and experimentally validated in many casting and heat treatment applications, as described by Urrutia et al. $^{[11]}$ and Boccardo et al. $^{[12]}$ and references therein. Although simplified analytical expressions of the thermal model have been reported, it has been long recognized that they do not provide an accurate description of the temperature field developed in LSE treatments $^{[13]}$, thus justifying the numerical solution approach adopted in the present work.

At first, the thermal history is obtained by solving numerically the thermal model with the finite element method. The solution of the metallurgical model for each time step is obtained by solving the ordinary differential equations with the one-step Euler's numerical method. The metallurgical model was coupled to the thermal one by means of Fortran subroutines.

### A. Thermal Model for LSE Treatment

The temperature evolution is governed by the energy balance equation expressed as

$$
\rho c \dot{T}=\operatorname{div}[\boldsymbol{K} \operatorname{grad}(T)] \tag{1}
$$

where $T$ is the temperature, $\rho$ is the density, $c$ is the tangent specific heat, $\boldsymbol{K}$ is the isotropic conductivity second order tensor ($\boldsymbol{K}=k_{T} \boldsymbol{I}$, begin $k_{T}$ the conductivity coefficient and $\boldsymbol{I}$ the identity second order tensor) and the superposed dot indicates time derivative. The material coefficients $c$ and $k_{T}$ are in general temperature-dependent.

The boundary condition imposed at the part/environment interface is a thermal Newton type law given by

$$
\bar{q}=q_{l}-h_{c / r}\left(T-T_{e n v}\right) \tag{2}
$$

where $\bar{q}$ is the normal heat flux, $q_{l}$ is the heat flux provided by the moving laser beam, $h_{c / r}$ is the heat transfer coefficient comprising both convection and radiation effect and $T_{e n v}$ is the environmental temperature. Due to the high temperature rates experimented during the heating up and cooling down of the analyzed process, it was tested that the latent heat by phase change does not have a significant effect in the thermal history. For this reason, it is not considered in the above equation.

The thermal effect of the laser depends on the laser power, shape, dimension and spatial energy distribution of the laser beam, and scanning velocity. A fraction of the laser power is absorbed by the material and it is computed as $^{[14]}$: $p_{t o t}=\eta * p_{i n c}$ where $p_{t o t}$ and $p_{i n c}$ are the absorbed power and incident laser power, respectively, and $\eta$ is the absorptivity of the workpiece material. In solid metals, the absorptivity is mainly modified by the physical constants of metals, laser wavelength, incident angle of the laser, surface temperature, and the roughness of the metal. $^{[15]}$ When the laser irradiates a molten metal, the laser absorption is a complex process where the interaction between laser-surface is affected by the liquid motion. $^{[16]}$ The strategy used to model the absorptivity is described in Section 3.

The chosen initial condition is a homogeneously distributed temperature in the domain and it is equal to $T_{0}=T_{e n v}$.

### B. Development of the Metallurgical Model for NCI

The phase transformations occurring for each material point of the analyzed domain, during the laser surface heat treatment, depend mainly on the temperature evolution, and the chemical composition and the initial microstructure of the nodular cast iron.

At the beginning of the heat treatment, the model considers that each point of the part is formed by an NCI with a microstructure composed by graphite nodules embedded into a metallic matrix constituted by ferrite, ferrite-pearlite, or pearlite. Whether the microstructure contains products of a ductile iron, it is represented by an index IM that is equal to 1.

856-VOLUME 52B, APRIL 2021

METALLURGICAL AND MATERIALS TRANSACTIONS B

The modeled phase transformations are presented in the flow diagram of Figure 1 and separately described below. During the heating stage, the ferrite and pearlite are transformed into austenite and graphite by means of the reverse eutectoid transformation (RET) if the temperature is higher or equal than the temperature $T_{RE}$ at which the RET is assumed to begin. Once this transformation ends, the homogenization of the austenite carbon content (HA) occurs. When the temperature is higher than the melting temperature $T_M$, the ductile iron is transformed into liquid by means of the melting transformation (MT). The index IM is set equal to two because this liquid then solidifies and forms ledeburite that is a microconstituent of a white iron. During the cooling down stage, the phase transformations take place in the material represented with both values of the IM index. Regarding to the material that remains in solid state at the heating stage ($\text{IM}=1$), the austenite is transformed into ferrite and pearlite by means of the eutectoid transformation (ET) when the temperature is within the interval $T_A < T < T_{RE}$, where $T_A$ is the temperature at which the ausferritic transformation starts. The ausferritic transformation is not considered by this metallurgical model because the cooling rate is large enough to avoid it. The austenite is also transformed into martensite (MDT) when the temperature is smaller than $T_{MD}$. Regarding to the liquid material ($\text{IM}=2$), it is transformed into ledeburite by means of the solid transformation (ST) when the temperature is lower than the solidification temperature $T_S$. The model considers that the austenite of the ledeburite is able to transform only into martensite, because the cooling rate is high enough to avoid other solid-solid phase transformations. The martensitic transformation (MWT) starts when the ledeburite gets the temperature $T_{MW}$.

Figure 2 presents the phase transformations occurring in an NCI for three different examples of temperature evolution. In curve 1 the melting occurs, therefore, ledeburite is obtained at the end of the heat treatment ($\text{IM}=2$). In curve 2 the material gets a maximum temperature between $T_{RE}$ and $T_M$, only experiencing solid state transformations at high temperature and keeping the NCI microstructure at the end of the process ($\text{IM}=1$). In curve 3, the NCI is subjected to a thermal cycle with a maximum temperature less than $T_{RE}$ and, consequently, there is no phase transformation.

### 1. Reverse eutectoid transformation
During the reverse eutectoid transformation, the ferrite is transformed into austenite and graphite (stable reverse eutectoid transformation) and the pearlite is transformed into austenite (metastable reverse eutectoid transformation), as it is stated by Ghergu et al. $^{[17]}$ The stable and metastable transformations start when the temperature is higher or equal than $T_{\alpha_o}$ and $T_{p_o}$, respectively. Then, $T_{RE}=T_{p_o}$ because $T_{p_o}<T_{\alpha_o}$. These temperatures are computed, in $^\circ$C, as in Ghergu et al. $^{[17]}$:

$$
\begin{aligned}
T_{\alpha_{o}}=&\ 739+31.5\mathrm{W_{Si}}-7.7\mathrm{W_{Cu}}-18.7\mathrm{W_{Mn}}+3.3\mathrm{W_{Mo}}\\
&-10.7\mathrm{W_{Cr}}-26\mathrm{W_{Ni}}
\end{aligned}
\tag{3}
$$

$$
\begin{aligned}
T_{p_{o}}=&\ 727+30.07\mathrm{W_{Si}}-1.98(\mathrm{W_{Si}})^2-10.7\mathrm{W_{Cu}}\\
&-13.7\mathrm{W_{Mn}}+9.3\mathrm{W_{Mo}}+24.3\mathrm{W_{Cr}}-12\mathrm{W_{Ni}}
\end{aligned}
\tag{4}
$$

where $\mathrm{W}_i$ are the alloy element concentrations in the NCI in weight per cent (wt pct).

![](./images/812505236441661440_2.jpg)

Fig. 1—Flow diagram of the metallurgical model. The ferrite, pearlite, and austenite volume fractions are denoted by $f_\alpha$, $f_p$, and $f_\gamma$, respectively.

![](./images/812505236441661440_3.jpg)

Fig. 2—Phase changes during the heat treatment for different examples of temperature evolution.

For the stable reverse eutectoid transformation, the graphite nodules are grouped in sets according to their sizes. A spherical domain is employed for each set, in which the initial microstructure is represented by a spherical core of graphite and an outer halo of ferrite. The transformation starts with the nucleation of an austenite halo at graphite-ferrite interface, which grows by means of carbon diffusion (see Boccardo et al.⁽¹⁸⁾).

The evolutions of graphite, ferrite, and austenite volume fractions during the transformation are computed as follows:

$$
f_{G r}=\frac{4 \pi}{3} \sum_{i=1}^{n s e t s g}\left(N_{g_{i}} r_{G r_{i}}^{3}\right)
\tag{5}
$$

$$
f_{\alpha}=\frac{4 \pi}{3} \sum_{i=1}^{n s e t s g}\left[N_{g_{i}}\left(r_{\alpha_{i}}^{3}-r_{\gamma_{i}}^{3}\right)\right]
\tag{6}
$$

$$
f_{\gamma_{s}}=\frac{4 \pi}{3} \sum_{i=1}^{n s e t s g}\left[N_{g_{i}}\left(r_{\gamma_{i}}^{3}-r_{G r_{i}}^{3}\right)\right]
\tag{7}
$$

where $r_{G r_{i}}$ is the radius of graphite nodule, $r_{\gamma_{i}}$ is the outer radius of austenite halo, $r_{\alpha_{i}}$ is the radius of the spherical domain, all the radii in $m$, and $N_{g_{i}}$ is the number of nodules per unit of volume, all of them for a set $i$. Moreover, $nsetsg$ is the number of sets. The initial radius of graphite nodule is computed as $r_{G r_{i_{o}}}=\left[3 f_{s e t_{i}} f_{G r_{o}} /\left(4 \pi N_{g_{i}}\right)\right]^{1 / 3}$, where $f_{G r_{o}}$ is the initial volume fraction of graphite nodule and $f_{s e t_{i}}$ is the initial volume fraction of graphite nodule, for the set $i$, normalized with respect to $f_{G r_{o}}$ being $\sum_{i=1}^{n s e t s g}\left(f_{s e t_{i}}\right)=1$. The radius of the spherical domain is calculated as $r_{\alpha_{i}}=r_{G r_{i_{o}}}\left(1+f_{\alpha_{o}} / f_{G r_{o}}\right)^{1 / 3}$, where $f_{\alpha_{o}}$ is the initial volume fraction of ferrite.

The changes of $r_{G r_{i}}$ and $r_{\gamma_{i}}$ are obtained by solving the following system of ordinary differential equations employed by Boccardo et al.⁽¹⁸⁾, in which $r_{G r_{i}}(0)=r_{G r_{i_{o}}}$ and $r_{\gamma_{i}}(0)=1.01 r_{G r_{i_{o}}}$:

$$
\left\{
\begin{aligned}
\dot{r_{G r_{i}}} &=\frac{D_{\gamma} \rho_{\gamma} r_{\gamma_{i}}}{r_{G r_{i}}\left(r_{\gamma_{i}}-r_{G r_{i}}\right)} \frac{\left(c_{\gamma / \alpha}-c_{\gamma / G r}\right)}{\left(c_{G r} \rho_{G r}-c_{\gamma / G r} \rho_{\gamma}\right)} \\
\dot{r_{\gamma_{i}}} &=G I_{E}\left[\frac{D_{\alpha} \rho_{\alpha} r_{\alpha_{i}}}{r_{\gamma_{i}}\left(r_{\alpha_{i}}-r_{\gamma_{i}}\right)} \frac{\left(c_{\alpha_{s}}-c_{\alpha / \gamma}\right)}{\left(c_{\gamma / \alpha} \rho_{\gamma}-c_{\alpha / \gamma} \rho_{\alpha}\right)}-\frac{D_{\gamma} \rho_{\gamma} r_{G r_{i}}}{r_{\gamma_{i}}\left(r_{\gamma_{i}}-r_{G r_{i}}\right)} \frac{\left(c_{\gamma / \alpha}-c_{\gamma / G r}\right)}{\left(c_{\gamma / \alpha} \rho_{\gamma}-c_{\alpha / \gamma} \rho_{\alpha}\right)}\right]
\end{aligned}
\right.
\tag{8}
$$

where $D_{\alpha}$ and $D_{\gamma}$, in $m^{2} / s$, are the diffusion coefficients of carbon in ferrite and austenite, respectively. $\rho_{G r}, \rho_{\alpha}$, and $\rho_{\gamma}$, in $kg / m^{3}$, are the graphite, ferrite, and austenite densities, respectively. $c_{G r}, c_{\alpha / \gamma}, c_{\alpha_{s}}, c_{\gamma / G r}$, and $c_{\gamma / \alpha}$, in wt pct, are the carbon concentrations in graphite, ferrite in contact with austenite, ferrite placed at $r_{\alpha_{i}}$, austenite in contact with graphite, and austenite in contact with ferrite, respectively. The concentration $c_{\alpha_{s}}$ is calculated by taking into account the carbon mass conservation in the spherical domain while the rest of the carbon concentrations are calculated as in the work of Boccardo et al.⁽¹⁸⁾ The nonlinear coefficient $G I_{E}$ considers the interaction between the neighboring halos of austenite when they are growing. It is calculated as follows:

$$
G I_{E}=\left\{
\begin{aligned}
1 & \text { for }\left(f_{G r}+f_{\gamma_{s}}\right)<f_{c o n} \\
{\left[\frac{1-\left(f_{G r}+f_{\gamma_{s}}\right)}{1-f_{c o n}}\right]^{2 / 3} } & \text { for }\left(f_{G r}+f_{\gamma_{s}}\right) \geq f_{c o n}
\end{aligned}
\right.
\tag{9}
$$

where $f_{c o n}$ represents the sum of $f_{G r}$ and $f_{\gamma_{s}}$ when the neighboring halos of austenite begin to be in contact and it is set as $f_{c o n}=0.5$.

For the metastable reverse eutectoid transformation, the pearlite colonies are grouped in sets according to their interlaminar spacing. A unidimensional domain is employed for each set, in which the initial microstructure is represented by a half layer of cementite and a half layer of ferrite. The transformation starts with the nucleation of an austenite layer at cementite-ferrite interface, which grows by means of carbon diffusion.

The evolutions of cementite, ferrite, austenite, and pearlite volume fractions are respectively computed as follows:

$$
f_{\theta}=\sum_{j=1}^{n s e t s c}\left(f_{p_{j}} \frac{x_{\theta_{j}}}{x_{\alpha_{j}}}\right)
$$

$$
f_{\alpha_{m}}=\sum_{j=1}^{n s e t s c}\left[f_{p_{j}} \frac{\left(x_{\alpha_{j}}-x_{\gamma_{j}}\right)}{x_{\alpha_{j}}}\right]
$$

$$
f_{\gamma_{m}}=\sum_{j=1}^{n s e t s c}\left[f_{p_{j}} \frac{\left(x_{\gamma_{j}}-x_{\theta_{j}}\right)}{x_{\alpha_{j}}}\right]
$$

$$
f_{p}=\sum_{j=1}^{n s e t s c}\left\{f_{p_{j}}\left[1-\frac{\left(x_{\gamma_{j}}-x_{\theta_{j}}\right)}{x_{\alpha_{j}}}\right]\right\}
$$

where $x_{\theta_{j}}$ is the coordinate of cementite-austenite interface, $x_{\gamma_{j}}$ is the coordinate of austenite-ferrite interface, $x_{\alpha_{j}}$ is the length of the domain, all the coordinates and length in $m$, and $f_{p_{j}}$ is the pearlite volume fraction, all of them for a set $j$. Moreover, $nsetsc$ is the number of sets and the initial pearlite volume fraction is $f_{p_{o}}=\sum_{j=1}^{n s e t s c}\left(f_{p_{j}}\right)$. The initial value of $x_{\theta_{j}}$ is computed as $x_{\theta_{j o}}=x_{\alpha_{j}} f_{\theta / p}$, where $f_{\theta / p}$ is the initial volume fraction of cementite in pearlite $(f_{\theta / p}=0.12)$. The domain length is computed as $x_{\alpha_{j}}=i p s_{j} / 2$, where $i p s_{j}$ is the interlaminar spacing.

The changes of $x_{\theta_{j}}$ and $x_{\gamma_{j}}$ are obtained by solving the following system of ordinary differential equations employed by Boccardo et al. $^{[18]}$, in which $x_{\theta_{j}}(0)=x_{\theta_{j o}}$ and $x_{\gamma_{j}}(0)=1.01 x_{\theta_{j o}}$ :

$$
\left\{\begin{aligned}
\dot{x_{\theta_{j}}} & =\frac{D_{\gamma} \rho_{\gamma}}{\left(x_{\gamma_{j}}-x_{\theta_{j}}\right)} \frac{\left(c_{\gamma / \alpha}-c_{\gamma / \theta}\right)}{\left(c_{\theta} \rho_{\theta}-c_{\gamma / \theta} \rho_{\gamma}\right)} \\
\dot{x_{\gamma_{j}}} & =\frac{D_{\alpha} \rho_{\alpha}}{\left(x_{\alpha_{j}}-x_{\gamma_{j}}\right)} \frac{\left(c_{\alpha_{m}}-c_{\alpha / \gamma}\right)}{\left(c_{\gamma / \alpha} \rho_{\gamma}-c_{\alpha / \gamma} \rho_{\alpha}\right)}-\frac{D_{\gamma} \rho_{\gamma}}{\left(x_{\gamma_{j}}-x_{\theta_{j}}\right)} \frac{\left(c_{\gamma / \alpha}-c_{\gamma / \theta}\right)}{\left(c_{\gamma / \alpha} \rho_{\gamma}-c_{\alpha / \gamma} \rho_{\alpha}\right)}
\end{aligned}\right.
$$

where $\rho_{\theta}$ is the cementite density, and $c_{\alpha_{m}}, c_{\theta}$, and $c_{\gamma / \theta}$ are the carbon concentrations in ferrite placed at $x_{\alpha_{j}}$, cementite, and austenite in contact with cementite. These parameters are calculated by Boccardo et al. $^{[18]}$, and $c_{\alpha_{m}}$ is calculated by taking into account the carbon mass conservation in the unidimensional domain.

The total austenite volume fraction formed during the reverse eutectoid transformation is calculated as:

$$
f_{\gamma}=f_{\gamma_{s}}+f_{\gamma_{m}}
$$

### 2. Homogenization of the austenite carbon content

Once the initial microstructure was completely transformed into austenite and graphite, the ductile iron experiences a process in which the austenite carbon content is uniformly distributed in the matrix. The carbon concentration in austenite depends on the temperature, because the temperature modifies the equilibrium carbon concentration in austenite. Due to the carbon diffusion involved in this process, the graphite and austenite volume fractions are varied.

In order to model the carbon homogenization process, and for each graphite nodule set, a spherical domain is employed that contains a spherical core of graphite and an outer halo of austenite that represents the austenite formed during the reverse eutectoid transformation. The evolutions of graphite and austenite volume fractions are computed as follows:

$$
f_{G r}=\frac{4 \pi}{3} \sum_{i=1}^{n s e t s g}\left(N_{g_{i}} r_{G r_{i}}^{3}\right)
$$

$$
f_{\gamma}=\frac{4 \pi}{3} \sum_{i=1}^{n s e t s g}\left[N_{g_{i}}\left(r_{s h e l l_{i}}^{3}-r_{G r_{i}}^{3}\right)\right]
$$

where $r_{s h e l l_{i}}=\left[3 f_{s e t_{i}} /\left(4 \pi N_{g_{i}}\right)\right]^{1 / 3}$ is the outer radius of the spherical domain.

The change of $r_{G r_{i}}$ is calculated by solving the following differential equation employed by Boccardo et al. $^{[19]}$, in which $r_{G r_{i}}(0)=r_{G r_{i_{b}}}$ where $r_{G r_{i_{b}}}$ is the radius of the graphite nodule at the beginning of the homogenization process:

$$
\dot{r_{G r_{i}}}=\frac{D_{\gamma} \rho_{\gamma} r_{s h e l l_{i}}}{r_{G r_{i}}\left(r_{s h e l l_{i}}-r_{G r_{i}}\right)} \frac{\left(c_{\gamma_{s h e l l}}-c_{\gamma / G r}\right)}{\left(c_{G r} \rho_{G r}-c_{\gamma / G r} \rho_{\gamma}\right)}
$$

where $c_{\gamma_{s h e l l}}$ is the austenite carbon concentration at $r_{s h e l l_{i}}$ that is calculated by taking into account the carbon mass conservation in the spherical domain.

### 3. Melting transformation

During the melting process the NCI is transformed into liquid. According to the model, during this phase change part of graphite nodules and metallic matrix are transformed into liquid with the aim to simulate the liquid formation at the graphite nodule-matrix interfaces. The evolutions of liquid and solid phases are proposed to be computed as a linear function of the temperature, as follows:

$$
f_{l}=\left(\frac{T-T_{L_{s}}}{T_{L_{e}}-T_{L_{s}}}\right)
$$

$$
f_{s}=1-f_{l}
$$

where $T_{L_{s}}=T_{M}$ and $T_{L_{e}}$ are the temperatures at which the melting transformation starts and ends, respectively. They are proposed, in ${ }^{\circ} \mathrm{C}$, as $T_{L_{s}}=T_{L S}+10^{\circ} \mathrm{C}$ and $T_{L_{e}}=T_{L S}+50^{\circ} \mathrm{C}$ in order to consider the superheating. The $T_{L S}$ is calculated as in the work of Urrutia et al. ${ }^{[11]}$ :

$$
T_{L S}=1147.2-6.93 W_{S i}-1.717\left(W_{S i}\right)^{2}
$$


Roy and Manna⁽⁷⁾ considered in their model that melting transformation starts once the temperature exceeds $T_{LS}$ by $50^\circ$C, being reasonable the temperature values here proposed.

The evolutions of graphite, austenite, ferrite, and pearlite volume fractions during the transformation are computed as follows:

$$f_{k}=f_{k_{b}}f_{s}\tag{22}$$

where $k = Gr$, $\gamma$, $\alpha$, and $p$, and $f_{k_{b}}$ is the volume fraction of the mentioned microconstituents at the beginning of the melting transformation.

### 4. Eutectoid transformation
During the eutectoid transformation of the ductile iron, the austenite is transformed into graphite and ferrite (stable eutectoid transformation) and pearlite (metastable eutectoid transformation), as is stated in Ghergu *et al.*⁽¹⁷⁾ The stable and metastable transformations, which compete each other, start when the temperature is smaller or equal than $T_{\alpha}$ and $T_{p}$, respectively. It is proposed that ET is interrupted when the temperature is smaller or equal than $T_{A}$. These temperatures are computed, in $^\circ$C, as in Ghergu *et al.*⁽¹⁷⁾ and Bhadeshia⁽²⁰⁾:

$$
\begin{aligned}
T_{\alpha} &= 739 + 18.4\text{W}_{\text{Si}} + 2(\text{W}_{\text{Si}})^2 - 14\text{W}_{\text{Cu}} - 45\text{W}_{\text{Mn}} \\
&\quad + 2\text{W}_{\text{Mo}} - 24\text{W}_{\text{Cr}} - 27.5\text{W}_{\text{Ni}}
\tag{23}
\end{aligned}
$$

$$
\begin{aligned}
T_{p} &= 727 + 21.6\text{W}_{\text{Si}} + 0.023(\text{W}_{\text{Si}})^2 + 8\text{W}_{\text{Mo}} + 13\text{W}_{\text{Cr}} \\
&\quad - 21\text{W}_{\text{Cu}} - 25\text{W}_{\text{Mn}} - 33\text{W}_{\text{Ni}}
\tag{24}
\end{aligned}
$$

$$T_{A}=830 - 270W_{C_{\gamma}} - 90W_{Mn} - 37W_{Ni} - 70W_{Cr} - 83\tag{25}$$

where $\text{W}_{i}$ are the alloy element concentrations in the NCI and $W_{C_{\gamma}}$ is the austenite carbon concentration, in wt pct.

The stable eutectoid transformation is modeled by taking into account a spherical domain for each set of graphite nodule. If there is residual ferrite from RET, at the beginning of the transformation the microstructure is represented by a spherical core of graphite that is surrounded by a ferrite halo, being this halo surrounded by an austenite halo. If ferrite is completely transformed into austenite during RET, the microstructure is represented by a spherical core of graphite and an outer halo of austenite as in Carazo *et al.*⁽²¹⁾ For the last microstructure representation, the transformation starts with the nucleation of a ferrite halo at the graphite-austenite interface. During the ET, ferrite grows by means of carbon diffusion.

The evolutions of graphite, ferrite, and austenite volume fractions during the transformation are computed as follows:

$$f_{Gr}=\frac{4\pi}{3}\sum_{i=1}^{nsetsg}\left(N_{g_{i}}r_{Gr_{i}}^{3}\right)\tag{26}$$

$$f_{\alpha}=\frac{4\pi}{3}\sum_{i=1}^{nsetsg}\left[N_{g_{i}}\left(r_{\alpha_{i}}^{3}-r_{Gr_{i}}^{3}\right)\right]\tag{27}$$

$$f_{\gamma_{s}}=\frac{4\pi}{3}\sum_{i=1}^{nsetsg}\left[N_{g_{i}}\left(r_{\gamma_{i}}^{3}-r_{\alpha_{i}}^{3}\right)\right]\tag{28}$$

where $r_{\gamma_{i}}$ is the radius of the spherical domain that is calculated as a function of the pearlite volume fraction as $r_{\gamma_{i}}=r_{shell_{i}}(1 - f_{p})^{1/3}$.

The changes of $r_{Gr_{i}}$ and $r_{\alpha_{i}}$ are obtained by solving the system of ordinary differential equations employed in Carazo *et al.*⁽²¹⁾, in which $r_{Gr_{i}}(0)=r_{Gr_{i_{b}}}$, where $r_{Gr_{i_{b}}}$ is the radius of graphite nodule at the beginning of the ET transformation. If at the beginning of the transformation there is residual ferrite from RET, $r_{\alpha_{i}}(0)=r_{\alpha_{i_{b}}}$, where $r_{\alpha_{i_{b}}}$ is the external radius of the equivalent ferrite halo that is placed between the graphite core and the austenite halo. The volume fraction of this equivalent halo is equal to the volume fraction of the residual ferrite. If at the beginning of the transformation there is not residual ferrite, $r_{\alpha_{i}}(0)=1.01r_{Gr_{i_{b}}}$.

$$
\left\{
\begin{aligned}
\dot{r_{Gr_{i}}}&=\frac{D_{\alpha}\rho_{\alpha}r_{\alpha_{i}}}{r_{Gr_{i}}(r_{\alpha_{i}}-r_{Gr_{i}})}\frac{\left(c_{\alpha/\gamma}-c_{\alpha/Gr}\right)}{\rho_{Gr}\left(c_{Gr}-c_{\alpha/Gr}\right)} \\
\dot{r_{\alpha_{i}}}&=GI_{E}\left[\frac{D_{\alpha}r_{Gr_{i}}}{r_{\alpha_{i}}(r_{\alpha_{i}}-r_{Gr_{i}})}\frac{\left(c_{\alpha/\gamma}-c_{\alpha/Gr}\right)}{\left(c_{\gamma/\alpha}-c_{\alpha/\gamma}\right)}+\frac{D_{\gamma}\rho_{\gamma}}{\rho_{\alpha}r_{\alpha_{i}}'}\frac{\left(c_{\gamma/\alpha}-c_{\gamma c}\right)}{\left(c_{\gamma/\alpha}-c_{\alpha/\gamma}\right)}\right]
\end{aligned}
\right.\tag{29}
$$

where $c_{\gamma c}$ is the austenite carbon concentration at $r_{\gamma_{i}}+\delta_{\gamma_{i}}$, $\delta_{\gamma_{i}}$ is the thickness of an austenite halo placed next to the austenite-ferrite interface in which the gradient of carbon concentration takes place, and $r_{\alpha_{i}}'=r_{\alpha_{i}}\delta_{\gamma_{i}}/(r_{\alpha_{i}}+\delta_{\gamma_{i}})$. As in Carazo *et al.*⁽²¹⁾, the austenite halo thickness is equal to $\delta_{\gamma_{i}}=2D_{\gamma}/\dot{r_{\alpha_{i}}}$. Moreover, $GI_{E}$ is a nonlinear coefficient that considers the interaction between the neighboring halos of ferrite when they are growing. In this work it is proposed as follows:

$$GI_{E}=\left\{
\begin{aligned}
1 &\text{ for }(f_{Gr}+f_{\alpha})<f_{con} \\
\left[\frac{1-(f_{Gr}+f_{\alpha})}{1-f_{con}}\right]^{2/3} &\text{ for }(f_{Gr}+f_{\alpha})\geq f_{con}
\end{aligned}
\right.\tag{30}
$$

where $f_{con}$ is the sum of $f_{Gr}$ and $f_{\alpha}$ when the neighboring halos of ferrite begin to be in contact and it is set as $f_{con}=0.5$.

The metastable eutectoid transformation model takes into account the nucleation and growth of spherical colonies/grains of pearlite, which are grouped in sets according to their sizes. The number of sets $nsetsc$ increases with the transformation time.

The number of colonies per unit of volume and time is computed as in Carazo *et al.*⁽²²⁾:

$$\dot{N_{c}}=n_{n} \mu_{p}\left(T_{p}-T\right)^{\left(n_{n}-1\right)} \dot{T}\qquad[31]$$

where $n_{n}=2$, $\mu_{p}$ is a parameter to be fitted, and $\dot{T}$ is the cooling rate.

The evolution of the pearlite volume fraction is calculated with the following equation:

$$f_{f}=f_{p_{R E T}}+\frac{4 \pi}{3} \sum_{j=1}^{n s e t s c}\left(N_{c_{j}} r_{p_{j}}^{3}\right)\qquad[32]$$

where $r_{p_{j}}$ is the radius of pearlite colonies of a set $j$, and $f_{p_{R E T}}$ is the residual pearlite volume fraction from RET.

Considering that the carbon diffusion occurs in the volume of austenite, the change in $r_{p_{j}}$ is calculated by solving the following differential equation employed in Carazo et al. $^{[21]}$, in which $r_{p_{j}}(0)=1 \times 10^{-6} m$:

$$\dot{r_{p_{j}}}=k_{p} f_{\gamma n} \exp \left(\frac{-Q_{v}}{R(T+273)}\right)\left(T_{p}-T\right)^{n_{g}}\qquad[33]$$

where $k_{p}$ is the pearlite growth coefficient that depends on the chemical composition and $Q_{v}$ is the activation energy for carbon diffusion at austenite/pearlite, $f_{\gamma n}=$ $f_{\gamma} /\left(1-f_{G r}\right)$ is the austenite volume fraction with respect to the matrix volume fraction and it allows to consider the reduction of pearlite growth when the eutectic transformation advances, $R$ is the universal gas constant, and $n_{g}=2$. The values of pearlite growth coefficient and activation energy for carbon diffusion at austenite/pearlite are the employed by Carazo et al. $^{[21]} k_{p}=1.03 \times 10^{-3} \mathrm{~m} /\left(\mathrm{s}^{0} \mathrm{C}^{2}\right)$ and $Q_{v}=1.25 \times$ $10^{5} \mathrm{~J} / \mathrm{mol}$.

The austenite volume fraction is computed as follows:

$$f_{\gamma}=1-\left(f_{G r}+f_{\alpha}+f_{p}\right)\qquad[34]$$

### 5. Solidification

During the solidification, the liquid is transformed into ledeburite because of the high value of the cooling rate. The evolutions of the liquid and solid phases are proposed to be computed as a linear function of the temperature, as follows:

$$f_{l}=\left(\frac{T-T_{S_{e}}}{T_{S_{s}}-T_{S_{e}}}\right)\qquad[35]$$

$$f_{s}=1-f_{l}\qquad[36]$$

where $T_{S_{s}}=T_{S}$ and $T_{S_{e}}$ are the temperatures at which the solidification transformation starts and ends, respectively. They are proposed, in $^{\circ} \mathrm{C}$, as $T_{S_{s}}=$ $T_{L S}-10^{\circ} \mathrm{C}$ and $T_{S_{e}}=T_{L S}-100^{\circ} \mathrm{C}$ in order to obtain a smooth solidification during the cooling down and take into account the large undercooling as a consequence of high cooling rate (around $3000^{\circ} \mathrm{C} / \mathrm{s}$ ). These temperature values are reasonable taking into account that Kapturkiewicz et al. $^{[23]}$ identified a undercooling of $65{ }^{\circ} \mathrm{C}$ for cooling rates of $30^{\circ} \mathrm{C} / \mathrm{s}-40^{\circ} \mathrm{C} / \mathrm{s}$. It is important to notice that small variations in the proposed temperature values do not modify the phase volume fractions predicted by the model at the end of the solidification.

The volume fraction of ledeburite is calculated as $f_{l d}=f_{s}$, and the volume fractions of austenite and cementite that formed the ledeburite are computed as follows:

$$f_{\gamma_{w}}=f_{l d}\left(\frac{c_{\theta}-c_{e}}{c_{\theta}-c_{\gamma_{w}}}\right)\qquad[37]$$

$$f_{\theta_{w}}=f_{l d}\left(\frac{c_{e}-c_{\gamma_{w}}}{c_{\theta}-c_{\gamma_{w}}}\right)\qquad[38]$$

where $c_{\gamma_{w}}$ is the carbon concentration in austenite that forms the ledeburite and $c_{e}$ is the equivalent carbon concentration in the ledeburite. These carbon concentrations are computed, in wt pct, as $c_{\gamma_{w}}=2.2-$ $0.26 W_{S i}-0.01\left(W_{S i}\right)^{2}$ and $c_{e}=W_{C}+W_{S i} / 3$, where $W_{i}$ is the alloy element concentrations in the NCI, in wt pct, see Urrutia et al. $^{[11]}$

### 6. Martensitic transformations

For NCI, the austenite is transformed into martensite when the temperature is smaller or equal than $T_{M D}$. For ledeburite, the austenite is transformed into martensite when the temperature is smaller or equal than $T_{M W}$. These temperatures depend on the austenite carbon concentration and are computed, in ${ }^{\circ} \mathrm{C}$, with the equation proposed in Nehrenberg $^{[24]}$:

$$\begin{aligned}
\mathrm{T}_{\mathrm{Mk}}= & 772-300 W_{C_{k}}-33.3 \mathrm{~W}_{\mathrm{Mn}}-11.1 \mathrm{~W}_{\mathrm{Si}}-22.2 \mathrm{~W}_{\mathrm{Cr}} \\
& -16.7 \mathrm{~W}_{\mathrm{Ni}}-11.1 \mathrm{~W}_{\mathrm{Mo}}-273
\end{aligned}\qquad[39]$$

where $k=D$ and $W$, and $W_{i}$ are the alloy element concentrations in austenite, in wt pct.

The evolutions of martensite volume fractions for nodular cast iron $f_{m_{d}}$ and ledeburite $f_{m_{w}}$ are computed as follows:

$$f_{m_{d}}=f_{(\gamma \rightarrow m)_{d}} f_{\gamma_{b}}\qquad[40]$$

$$f_{m_{w}}=f_{(\gamma \rightarrow m)_{w}} f_{\gamma_{w_{b}}}\qquad[41]$$

where $f_{\gamma_{b}}$ and $f_{\gamma_{w_{b}}}$ are the austenite volume fractions at the beginning of the transformation for NCI and ledeburite, respectively. Moreover, $f_{(\gamma \rightarrow m)_{d}}$ and $f_{(\gamma \rightarrow m)_{w}}$ are the volume fractions of austenite that transform into martensite normalized with respect to $f_{\gamma_{b}}$ and $f_{\gamma_{w_{b}}}$, respectively. These volume fractions are computed

with the Khan-Bhadeshia's model⁽²⁵⁾:

$$
\frac{-\ln \left[1-f_{(\gamma \rightarrow m)_{d}}\right]}{f_{(\gamma \rightarrow m)_{d}}}=1+k_{D}\left(T_{M D}-T\right)
\tag{42}
$$

$$
\frac{-\ln \left[1-f_{(\gamma \rightarrow m)_{w}}\right]}{f_{(\gamma \rightarrow m)_{w}}}=1+k_{W}\left(T_{M W}-T\right)
\tag{43}
$$

where $k_D$ and $k_W$ are constants to be fitted.

The retained austenite is computed as:

$$
f_{\gamma_{r}}=f_{\gamma_{b}}\left[1-f_{(\gamma \rightarrow m)_{d}}\right]
\tag{44}
$$

$$
f_{\gamma_{w_{r}}}=f_{\gamma_{w_{b}}}\left[1-f_{(\gamma \rightarrow m)_{w}}\right]
$$

## III. RESULTS AND DISCUSSION

In order to test the model performance, the simulation results are compared with experimental results obtained for samples irradiated with constant and variable laser powers. Both cases are separately described below.

### A. Comparison of the Model with Experimental Results at Constant Laser Power

The experimental results obtained by Janicki *et al.*⁽²⁶⁾ in samples irradiated with constant laser power are used in the present work to extend the validation range of the predictions computed with the proposed model. Pearlitic-ferritic NCI samples with shape of slab, shown in Figure 3, and chemical composition 3.6C-2.51Si-0.78Cu-0.25Mn-0.02Cr-0.04Ni-0.008S-0.016P-Fe in wt pct are treated by using a Rofin-Sinar DL 020 2.0 kW continuous-wave high-power direct diode laser.

![](./images/812505236441661440_4.jpg)

Fig. 3—Geometry of treated samples with constant laser power. All the dimensions are in mm.

During the experiments, the laser is moved along the x axis, see Figure 3. The laser has a rectangular beam (6.6 mm x 1.5 mm) with a near Gaussian spatial energy distribution in the x axis and a uniform spatial energy distribution in the y axis. Three cases were studied with different combinations of laser power and scanning velocity (sv), as it is shown in Table I. Argon gas is employed to prevent oxidation. The temperature at the irradiated surface was measured by means of an infrared FLIR A600-Series camera with a measurement temperature range from 600 °C to 2200 °C.

### B. Comparison of the Model with Experimental Results at Variable Laser Power

As part of this research, ferritic NCI samples with the shape of slab, shown in Figure 4, are heat treated by employing a fiber delivery diode laser Laserline LDF 4.000-100 in the multimode wavelength mode in the 980 nm -1024 nm range using a 100 $\mu$m diameter optical fiber with a numerical aperture of 0.1 $\mu$m.

The chemical composition of the NCI is 3.63C-2.7Si-0.25Mn-0.049Cr-Fe in wt pct and the features of the as cast microstructure are full ferritic matrix, graphite volume fraction 0.1165, and graphite nodule count $1.0635^{13}nodule/m^3$ that were determined by standard image analysis of optical micrography.⁽²⁷⁾

During the heat treatment, the laser is moved along the x axis, as is shown in Figure 4. Four cases are studied by taking into account different combinations of laser power and scanning velocity, as it is shown in Table II. The laser power varies from an initial value (at x=5mm) to a final value (at x=92mm) with a linear function of the position. The laser has a rectangular beam (23 mm x 2 mm) with a uniform spatial energy distribution. Graphite coating was not employed because the obtained absorptivity of the laser beam in the material is sufficiently high.

The temperature evolution was measured during the heat treatment at four points of the analyzed section with K-type thermocouples (Ni-Cr/Ni-Al), as it is shown in Figure 4. The microstructure obtained after the treatment was observed by means of optical microscopy and the phase volume fractions at different regions were computed by performing an image analysis with a custom software. The software divides an image of the microstructure into a given number of slices, being each slice related to a depth. After that, the phase volume fractions are computed for each slice in a standard form. Finally, the relation phase volume fraction-depth of the analyzed micrograph is obtained by gathering the processed information.

### C. Considerations and Input Data to Perform the Numerical Simulations

Taking into account the symmetry plane, half of the samples are modeled as a 3D geometry discretized with nearly 2460 hexahedral, 615 wedge, and 12100 tetrahedral linear elements for cases C1-C3, and 10900 hexahedral, 5750 wedge, and 18300 tetrahedral linear

<table><thead><tr><th>Case</th><th>Power [W]</th><th>Scanning Velocity [mm/min]</th><th>Average Linear Energy [J/mm]</th></tr></thead><tbody><tr><td>C1</td><td>2000</td><td>200</td><td>600</td></tr><tr><td>C2</td><td>1000</td><td>100</td><td>600</td></tr><tr><td>C3</td><td>1500</td><td>75</td><td>1200</td></tr></tbody></table>

![](./images/812505236441661440_5.jpg)

Fig. 4—Geometry of treated samples with variable laser power and position of thermocouples T1, T2, T3, and T4 at the analyzed section. All the dimensions are in mm.

<table><thead><tr><th>Case</th><th>Initial Power [W]</th><th>Final Power [W]</th><th>Scanning Velocity [mm/min]</th><th>Average Linear Energy [J/mm]</th></tr></thead><tbody><tr><td>V1</td><td>1500</td><td>2500</td><td>1000</td><td>120</td></tr><tr><td>V2</td><td>2500</td><td>3500</td><td>1000</td><td>180</td></tr><tr><td>V3</td><td>1500</td><td>2500</td><td>600</td><td>200</td></tr><tr><td>V4</td><td>2500</td><td>3500</td><td>600</td><td>300</td></tr></tbody></table>

![](./images/812505236441661440_6.jpg)

Fig. 5—Modeled geometries and finite element meshes.

elements for cases V1-V4, as it is shown in Figure 5. These numbers of elements were defined after a conver- gence study aimed at ensuring a trade-off between accuracy in the results and computational time. A refinement is considered at the near-surface region in order to capture the expected high temperature and phase fraction gradients developed in this zone. The environmental temperature is 22 °C and convection-ra- diation conditions are adopted for all sample boundaries except for the symmetry planes in which a zero normal flux is applied as boundary condition. The employed thermal properties are those reported in Boccardoet al.[18] and Carazoet al.[21]

For cases V1-V4, the initial microstructure is com- posed by $f_{Gr_{o}}=0.1165$, $f_{\alpha_{o}}=0.8835$, and $f_{p_{o}}=0$. It is considered that all graphite nodules have the same size $(nsetsg=1,\ f_{set_{1}}=1,\ \text{and}\ N_{g_{1}}=1.0635^{13}nodule/m^{3})$. The parameters of the phase change models are fitted as $\mu_{p}=5\times10^{10}\ \text{grain}/(m^{3\circ}\text{C}^{2})$ (pearlite model), and $k_{D}=6\times10^{-3\circ}\text{C}$ and $k_{W}=3\times10^{-3\circ}\text{C}$ (martensite model) in order to reproduce the small pearlite and martensite volume fractions observed in the experiment. Because the Janicki's experiments are employed to compare the temperature field and the ledeburite

thickness, it is assumed for cases C1-C3 an initial microstructure formed by $f_{Gr_{o}}=0.105$, $f_{\alpha_{o}}=0.4475$, and $f_{p_{o}}=0.4475$ with pearlite colinies having the same interlaminar spacing ($nsetsc=1$, $f_{p_{1}}=0.45$, and $ips_{1}=5\times10^{-7}m$). The rest of the metallurgical model parameters used in cases C1-C3 are those of cases V1-V4.

Because the laser power and scanning velocity are modified during the heat treatment, the average absorptivity could be computed by using the empirical equation proposed by Zeng et al.$^{[28]}$:

$$
\eta = c_1 p_{inc}^{c_2} sv^{c_3} \tag{45}
$$

where $c_i$ are fitting coefficients. In order to determine these coefficients, several cases were solved with the proposed model for different absorptivity values with constant laser powers and scanning velocities. Then, the absorptivity values that allow to correctly predict the temperature field for cases C1-C3 and the final microstructure for cases V1-V4 are chosen as the data base to compute the coefficients by using the least square method. The obtained coefficients are $c_1=8.41min^{0.05088}/(W^{-0.4499}mm^{0.05088})$, $c_2=-0.4499$ and $c_3=0.05088$ with a R-square 1.0 for cases C1-C3 and $c_1=16.95min^{0.07035}/(W^{-0.4665}mm^{0.07035})$, $c_2=-0.4665$ and $c_3=0.07035$ with a R-square 0.9265 for cases V1-V4.

In order to obtain a better fit of the absorptivity for cases V1-V4, particularly at high laser power, the next equation is proposed:

$$
\eta = k_1 p_{inc} + k_2 sv + k_3 p_{inc} sv + k_4 \tag{46}
$$

where the coefficients $k_i$ were fitted by using the above mentioned data base resulting in $k_1=-2.268\times10^{-4}/W$, $k_2=-9.0967\times10^{-5}min/mm$, $k_3=7.3033\times10^{-8}min/(Wmm)$, and $k_4=1.227$ with a R-square 0.9566.

![](./images/812505236441661440_7.jpg)

Fig. 6—Temperature distribution along the midline of the samples for cases C1-C3.

## D. Comparison of Temperature Field

For both the analyzed cases (i.e., constant and variable laser powers), it is observed that the absorptivity increases with the decrement of the laser power and the increment of the scanning velocity, the influence of the last variable being important for large values of laser power. The same behavior was observed by Zeng et al.$^{[28]}$ for steel. The absorptivity for cases C1-C3 is lower than for cases V1-V4 probably because the samples of cases C1-C3 were ground to an average roughness of $0.5\ \mu m$ previously to the heat treatment.

The cases C1-C3 correspond to high average linear energy. For this reason, the obtained maximum temperature at the irradiated surface is above $1600\ ^{\circ}\text{C}$ in comparison with the cases V1-V4 that are below 1300 $^{\circ}\text{C}$. Figure 6 compares the computed and experimental temperature distributions along the midline of the samples corresponding to cases C1-C3, see Figure 3. An increment of the maximum temperature at the irradiated surface with the laser power increment is observed despite the average linear energy is equal for cases C1 and C2. For each case with constant laser power, the maximum temperature and its distribution around the maximum temperature do not change with the position implying, therefore, that steady-state conditions are achieved during the process.

For cases V1-V4, the temperature evolutions measured with thermocouples T1, T2, T3 and T4 were compared with the temperatures computed with the proposed model. Figure 7 presents the obtained results for case V2. Because the thermocouples T1, T2 and T3 measure the temperature in a region with a high temperature gradient, their measurements are compared with the simulated temperatures close to the thermocouple positions where it is seen that they exhibit a good agreement. The thermocouple T4 was irradiated by the laser and although it reached a maximum temperature of $826\ ^{\circ}\text{C}$, the sample surface at this location was melted, as it is observed in Figure 12, indicating

![](./images/812505236441661440_8.jpg)

Fig. 7—Evolution of temperature computed with the model and measured from experiments for case V2.

864-VOLUME 52B, APRIL 2021

METALLURGICAL AND MATERIALS TRANSACTIONS B

therefore that its temperature was at least 300 °C higher as it is suggested by the simulation. This result could be explained by the lower thermocouple absorptivity in comparison with that of the sample due to its smaller surface roughness. $^{[15]}$ For cases V1, V3, and V4, the results present the same behavior, but the temperature at T4 for case V4 could not be compared because the thermocouple was melted during the experiment.

Due to the variable laser power employed in cases V1-V4, different temperature evolutions and final microstructures are obtained within each sample. The simulated temperature evolutions at the surface of regions A-D are presented in Figure 8 for case V3. As was observed for cases C1-C3, the maximum temperature registered during the process increases with the increment of the laser power. Solid transformations are the main ones that occur at the irradiated surface of region A because the maximum temperature is close to $T_{L_{s}}$, meanwhile the material is completely melted at regions B-D because $T_{L_{e}} < T_{\text{max}}$. The influence of the laser power on the phase fractions at the irradiated surface for case V3 can also be observed in Figure 13.

![](./images/812505236441661440_9.jpg)

Fig. 8—Evolution of temperature computed with the model at the surface of regions A-D for case V3.

The simulated temperature distribution for region B, at different depth with respect to the irradiated surface, is shown in Figure 9 for case V2. As it is expected, the maximum temperature during the process takes place at the surface and it decreases with the increment of depth. According to the presented metallurgical model, the material is completely melted near the surface because the maximum temperature is $T_{L_{e}} < T_{\text{max}}$. For a depth of 100 $\mu$m, the material is partially melted $(T_{L_{s}} < T_{\text{max}} < T_{L_{e}})$, and for depths 200 $\mu$m, only solid phase transformations occur $(T_{\alpha_{o}} < T_{\text{max}} < T_{L_{s}})$. For depths bigger than 300 $\mu$m, there is no phase transformation $(T_{\text{max}} < T_{\alpha_{o}})$. The simulation allows to explain the experimental results presented in this work and the observations reported by Alabeedi *et al.*$^{[5]}$ and Grum and Sturm$^{[8,9]}$ related to the remarkable variation of the microstructure with the depth for NCI with an initial ferritic matrix.

### E. Comparison of Final Volume Fraction

At the end of the laser heat treatment, the obtained microstructure for cases V1-V4 is formed by a layer mainly composed of a mixture of ledeburite and a small amount of martensite next to the irradiated surface. When the depth increases, a transition layer formed by ledeburite-martensite and as cast microstructure (graphite and ferrite) appears. The phase composition of this transition layer is not uniform, increasing the volume fractions of the base material with the increment of the depth. When the laser power is reduced and the scanning velocity is increased, for example from case V4 to case V1, the transition layer is placed next to the surface or even it could disappear. Figure 10 shows the obtained microstructure at the end of the experiment and the ledeburite volume fraction contours computed by the model, both of them for the case V2 at region B. It could be observed how the model represents the mentioned layers into the microstructure. In the experimental results, a region that could be defined as the base material/transition layer with a small transformed volume around the graphite nodules is observed. The extension of this region, identified as the near base

![](./images/812505236441661440_10.jpg)

Fig. 9—Left: Optical microscope image of the resulted microstructure after the LSE treatment. Right: Computed temperature distribution for case V2 at region B and time 2.05s.

METALLURGICAL AND MATERIALS TRANSACTIONS B

VOLUME 52B, APRIL 2021—865

![](./images/812505236441661440_11.jpg)

Fig. 10—Left: Microstructure after the LSE treatment. Right: Computed ledeburite volume fraction for case V2 at region B.

![](./images/812505236441661440_12.jpg)

Fig. 11—Comparison between the simulated and experimental (exp) phase volume fractions as a function of the depth for case V1.

material, depends strongly on the random graphite nodule positions into the metallic matrix. Because the metallurgical model does not take into account these random positions, it only considers the region as formed by the base material.

According to the model, the microstructure of the transition layer for cases C1-C3, which is different from that observed for cases V1-V4, is formed by ledeburite, as cast microstructure (graphite, ferrite, and pearlite), and a high amount of martensite (volume fraction around 0.75). The maximum martensite volume fraction is placed close to the center of the transition layer, region where almost all the pearlite was transformed into austenite during the heating up and then transformed into martensite during the cooling down. These results are similar to those reported by Grum and Sturm⁽⁸⁾ for a pearlitic-ferritic NCI.

In the experiments presented in this work, as in those reported by Alabeedi *et al.*⁽⁵⁾ and Grum and Sturm,⁽⁸⁻⁹⁾ it is observed that the final microstructure is highly affected by the laser power and scanning velocity, obtaining microstructures close to the original one for low laser power and high scanning velocity and, in addition, microstructures with 200 to 1400 $\mu$m layer thickness of ledeburite for high laser power and low scanning velocity.

The comparison between the simulated and experimental results of the phase volume fractions for different values of depth is presented in Figures 11, 12, 13, and 14 for cases V1-V4, respectively. The experimental measurements were performed in two or three points of each region. When the laser power is increased and the scanning velocity is kept constant, *i.e.*, case V1 to case V2 and case V3 to case V4 that represent increments of 50 pct in the average linear energy, the volume fraction of ledeburite close to the surface is increased, which is of interest to improve the wear resistance performance of the material. The same behavior is observed when the scanning velocity is decreased and the laser power is kept constant, *i.e.*, case V1 to case V3 and case V2 to case V4 that represent increments of 75 pct in the average linear energy. As it is expected, the maximum ledeburite volume fraction is obtained by increasing the laser power and reducing the scanning velocity (case V4)

![](./images/812505236441661440_13.jpg)

Fig. 12—Comparison between the simulated and experimental (exp) phase volume fractions as a function of the depth for case V2.

![](./images/812505236441661440_14.jpg)

Fig. 13—Comparison between the simulated and experimental (exp) phase volume fractions as a function of the depth for case V3.

or, equivalently, by increasing the linear energy emitted by the laser. The increment of this volume fraction occurs because the material is subjected to a higher linear energy that generates a higher temperature in the treated part. When cases V2 and V3 are compared, which have very different values of power laser and scanning velocity but only a 17 pct of difference between the average linear energies, it is observed that the obtained volume fractions of ledeburite close to the surface are very similar. These behaviors are well represented by the proposed thermo-metallurgical model. The absorptivity decrement with the laser power increment is observed in case V4, where a 20 pct laser power increment (regions B and D) does not produce too many changes in the ledeburite layer thickness.

In all cases V1-V4, the model and experimental results show that the ledeburite volume fraction is decreased by the depth increment and the graphite and ferrite volume fractions are increased, which are related to the temperature decrement with the depth increment. Although, the martensite volume fraction was not experimentally measured because it is small, the model predicts that a small martensite volume fraction (less than 0.03) is formed into the ledeburite and the transition layer. Moreover, after the fitting process, the model computes a small pearlite volume fraction (less than 0.035) at the transition layer, being this phase not observed in the experiment.

In the experiments, a strong correlation between the thickness of the ledeburite-martensite layer and the linear energy emitted by the laser is observed, where such thickness increases with the increment of the linear energy. Figure 15 compares the ledeburite-martensite layer thicknesses measured from the experiments (which were indirectly obtained in the present work from the hardness profiles in the melted zone reported by Janicki et al.[²⁶]) and computed with the model for regions presenting at least a 0.9 ledeburite volume fraction. A good correlation between the model and experimental results can be appreciated. For the thicker layers, it is

![](./images/812505236441661440_15.jpg)

Fig. 14—Comparison between the simulated and experimental (exp) phase volume fractions as a function of the depth for case V4.

seen that the model reasonably captures the trend observed in the experiments where all the predictions consistently overestimate the thickness for cases C1, C2 and C3.

## IV. CONCLUSIONS
A thermo-metallurgical model able to predict the phase transformations occurring during the LSE treatment of NCI has been presented and validated. The possibilities and limitations of this model have been specifically assessed for several laser operating scenarios for ferritic and pearlitic-ferritic NCIs. The obtained results show:

1.  The laser absorptivity could be properly calibrated by employing empirical equations in order to reproduce the thermal history and the final microstructure. The maximum simulated temperature during the LSE treatment is reached at the surface of the samples.

![](./images/812505236441661440_16.jpg)

Fig. 15—Comparison between measured and computed thicknesses of ledeburite-martensite layer for all cases (C1-C3 and V1-V4).


This value is increased with the increment of the laser power and the decrement of the scanning velocity.

2. The type and amount of microconstituents at the end of the LSE treatment depend on the thermal history and initial microstructure. For the studied cases, a lager variety of microstructures was found. High la- ser power and low scanning velocity (high linear en- ergy) allow to form ledeburite and martensite at the sample surface, which enhances wear resistance.

3. The thickness of ledeburite-martensite layer depends on the laser operating scenarios and it is increased with the increment of the laser power and the decrement of scanning velocity, in other words, with the increment of the linear energy. The results ob- tained in the simulation are in good agreement with the experimental measurements.

4. The proposed model could be useful in the design of the LSE treatment, but it is important to notice that some microstructural features such as the dimensions of dendrites in ledeburite and the interlaminar spac- ing of pearlite colonies were not modeled. Moreover, the metallurgical model has constants to be fitted with experimental results.

The presented thermo-metallurgical model could be extended to other materials, such as steel, by modifying the phase change model to consider the phase transfor- mations occurring in these materials.

## ACKNOWLEDGMENTS

A. Boccardo is a member of the research staff of CONICET and he acknowledges the financial support received of the ASUTNCO0007785 Grant from Univer- sidad Tecnológica Nacional. D. Celentano thanks the financial support of ANID-Chile through the project Grant FONDECYT 1180591. E. Ramos-Moore thanks the financial support of ANID-Chile through the pro- ject Grant FONDECYT 1180564.

## REFERENCES

1. J.R. Davis: *ASM specialty handbook: Cast irons*, ASM Interna- tional, New York, 1996.

2. H.W. Bergmann: *Surf. Eng.*, 1985, vol. 1, pp. 137–55.

3. C.H. Chen, C.P. Ju, and J.M. Rigsbee: *Mater. Sci. Technol.* (United Kingdom), 1988, vol. 4, pp. 161–66.

4. C.P. Ju, C.H. Chen, and J.M. Rigsbee: *Mater. Sci. Technol.* (United Kingdom), 1988, vol. 4, pp. 167–72.

5. K.F. Alabeedi, J.H. Abboud, and K.Y. Benyounis: *Wear*, 2009, vol. 266, pp. 925–33.

6. S.P. Gadag, M.N. Srinivasan, and B.L. Mordike: *Mater. Sci. Eng. A*, 1995, vol. 196, pp. 145–54.

7. A. Roy and I. Manna: *Opt. Lasers Eng.*, 2000, vol. 34, pp. 369–83.

8. J. Grum and R. Šturm: *Mater. Charact.*, 1996, vol. 37, pp. 81–88.

9. J. Grum and R. Šturm: *Appl. Surf. Sci.*, 2002, vol. 187, pp. 116–23.

10. N. Pagano, V. Angelini, L. Ceschini, and G. Campana: *Procedia CIRP*, 2016, vol. 41, pp. 987–91.

11. A. Urrutia, D.J. Celentano, and D.R. Gunasegaram: *Metals* (Basel), 2017, vol. 7, pp. 1–17.

12. A.D. Boccardo, P.M. Dardati, L.A. Godoy, and J.J. Lopensino: *Lat. Am. J. Solids. Stru.*, 2018, vol. 15, p. e50.

13. P.A. Molian and A.K. Mathur: *J. Eng. Mater. Technol. Trans. ASME*, 1986, vol. 108, pp. 233–39.

14. R. Singh, M.J. Alberts, and S.N. Melkote: *J. Mach. Tools Manuf.*, 2008, vol. 48, pp. 994–1004.

15. Y. Li, Z. Zhang, C. Zhao, X. Hao, N. Dong, W. Yin, and Z. Pang: *Appl. Therm. Eng.*, 2020, vol. 174, p. 115276.

16. M. Matthews, J. Trapp, G. Guss, and A. Rubenchik: *J. Laser Appl.*, 2018, vol. 30, p. 032302.

17. R.M. Ghergu, J. Sertucha, Y. Thebault, and J. Lacaze: *ISIJ Int.*, 2012, vol. 52, pp. 2036–41.

18. A.D. Boccardo, P.M. Dardati, D.J. Celentano, L.A. Godoy, M. Górny, and E. Tyrała: *Metall. Mater. Trans. B*, 2016, vol. 47, pp. 566–75.

19. A.D. Boccardo, P.M. Dardati, D.J. Celentano, and L.A. Godoy: *Finite Elem. Anal. Des.*, 2017, vol. 134, pp. 82–91.

20. H. Bhadeshia: *Bainite in steels*, 3rd ed., Maney Publishing, UK, 2015, p. 142.

21. F.D. Carazo, P.M. Dardati, D.J. Celentano, and L.A. Godoy: *Metall. Mater. Trans. B*, 2012, vol. 43B, pp. 1579–95.

22. F.D. Carazo, L.N. García, and D.J. Celentano: *Metals (Basel)*., 2018, vol. 8, 550, pp. 1-15.

23. W. Kapturkiewicz, A. Burbelko, and M. Górny: *ISIJ Interna- tional*, 2014, vol. 54, pp. 288–93.

24. A.E. Nehrenberg: *Met. Technol. (N.Y.)*, 1946, vol XIII, pp. 33-43.

25. S.A. Khan and H.K.D.H. Bhadeshia: *Mater. Sci. Eng. A*, 1990, vol. 129, pp. 257–72.

26. D. Janicki, J. Górka, W. Kwaśny, W. Pakieła, and K. Matus: *Materials*, 2020, vol. 13, p. 1174.

27. N. Catalán: *Analysis of the effect of laser surface treatment on the microstructure, hardness and wear of a ferritic nodular cast iron* (in Spanish), MsD Thesis, Pontificia Universidad Católica de Chile, Chile, 2020.

28. H. Zeng, R. Yan, W. Wang, H. Zhang, J. Yan, and F. Peng: *J. Adv. Manuf. Technol.*, 2020, vol. 109, pp. 2481–90.

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.