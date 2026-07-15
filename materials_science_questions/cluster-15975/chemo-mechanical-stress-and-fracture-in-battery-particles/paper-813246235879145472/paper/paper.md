# Electromigration damage mechanics of lead-free solder joints under pulsed DC: A computational model

Wei Yao, Cemal Basaran*

Electronic Packaging Laboratory, State University of New York at Buffalo, NY 14260, United States

---

## ARTICLE INFO

**Article history:**
Received 16 September 2012
Received in revised form 17 November 2012
Accepted 5 January 2013
Available online 14 February 2013

**Keywords:**
Pulsed current electromigration
Thermomigration
SAC solder joint
Duty factor

---

## ABSTRACT

A numerical method for studying migration of voids driven by pulse electric current and thermal gradient in 95.5Sn-4Ag-0.5Cu (SAC405) solder joints is developed. The theoretical model involves coupling electron wind force, chemical potential, joule heating and stress gradient driving mass diffusion processes. Entropy based damage criteria is adopted to characterize the mass transportation mechanism, which utilize irreversible entropy production rate as a measure of material degradation. The pulse current induced EM damage results were compared with DC EM response under otherwise the same conditions. It is observed that increasing duty factor, current density and frequency leads to a faster damage accumulation. A mean time to failure (MTF) equation for solder joints under pulse current loadings is proposed which incorporates both thermomigration (TM) and EM damage. The failure mechanism is verified by our experimental results. It is observed that MTF is inversely proportional to $r^{m}$, $f^{p}$, and $j^{n}$, where duty factor exponent $m$ equals to 1.1, frequency exponent $p$ equals to 1.43 and current density exponent is 1.96. This equation is effective only when pulse period is below thermal relaxation time, commonly in $\mu$s range.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Electromigration (EM) is a mass transportation mechanism driven by electron wind force, thermal gradient, chemical potential and stress gradient. According to Moore's law, number of transistors on integrated circuits (ICs) doubles approximately every 2 years. Moore's law holds true since its introduction in 1970s. This insatiable demand for smaller ICs size, larger integration and higher Input/Output (IO) count of microelectronics has made ball grid array (BGA) the most promising connection type in electronic packaging industry. This trend, however, renders EM reliability of solders joints a major bottleneck to hinder further development of electronics industry. Although EM reliability of metal interconnects under direct current (DC) load has drawn increasing attention in recent years, our current understanding of degradation physics of solder alloys under time varying high current density loading is still quite limited. As a result of broad pulse signals application in IC semiconductors, investigation of pulsed direct current (PDC) EM reliability of flip-chip solder joints and corresponding morphology evolution and failure mechanisms have become an essential topic of study in the electronic packaging reliability field [1-6].

Two types of failure mechanisms are related to the EM process: short-circuit failure induced by anode side mass extrusion and open-circuit induced by void coalescence at cathode side. Under DC loadings, mass transport from cathode side toward the anode side due to scattering of conduction band electrons with ions at grain boundaries, which is referred as electron wind force. During this diffusion process, when steady state is reached, chemical potential and stress gradient driving force retard the mass diffusion by electron wind force [7-9]. For the pulse DC (PDC) loading, the same holds true during on-portion of the pulse. During the load-off period, however, only chemical potential and stress gradient come into play. This back diffusion in absence of an electric field has an opposite effect on electron wind force, and heals part of the damage induced during load-on time, thus interconnects under PDC is expected to have a longer lifetime comparing to those subjected to DC loading under otherwise identical conditions. This damage healing mechanism under PDC loading strongly depends on pulse frequency, current density and duty factor defined as load-on time over one loading period. Some researchers studied pulse DC and AC electromigration in deposited Al or Cu thin films, both experimentally and theoretically [10-19]. It was found that lifetime of conductors under time varying current is times longer than those subjected to DC current under otherwise the same conditions. There is, however, very limited research on EM of solder alloys under PDC loadings. This study is intended to fill in the gap of EM behavior of solder alloys subjected to PDC loading, by

---

* Corresponding author.
E-mail address: cjb@buffalo.edu (C. Basaran).

0927-0256/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.commatsci.2013.01.016

considering both EM and thermomigration (TM) induced damage. In this work, we employ the pulsed current loadings with various duty factors and frequencies on 95.5Sn-4Ag-0.5Cu (SAC405) solder joints. Results of vacancy concentration, volumetric stress and damage evolution with respect to duty factors and frequencies are plotted and compared with those under DC current stressing. For solder joints, Basaran et al. [20-24], proposed a comprehensive mean time to failure (MTF) equation for solder joints. In this study, we extend this model for SAC solder joints subjected to PDC loadings by incorporating current density, duty factor and frequency dependence.

## 2. Governing equations

Basaran group proposed damage mechanics formulation for solder joints subjected to electrical and thermal loadings by coupling vacancy conservation, force equilibrium, heat transfer and electric conduction processes as shown below [25]:

### 2.1. Vacancy conservation equation

Electromigration is a diffusion controlled mass transportation process governed by the following vacancy conservation equations:

$$
C_{\mathrm{v} 0} \frac{\partial c}{\partial t}+\nabla q-G=0
\tag{1}
$$

where $C_{\mathrm{v} 0}$ is the initial thermodynamic equilibrium vacancy concentration in absence of any loadings; $c$ is the normalized vacancy concentration defined as $C_{\mathrm{v}} / C_{\mathrm{v} 0}$ with $C_{\mathrm{v}}$ as vacancy concentration; vacancy flux due to the combined effect of gradient of vacancy concentration, electric wind force, mechanical stress gradient and temperature gradient, respectively, is given by the following equation:

$$
q=-D_{\mathrm{v}} C_{\mathrm{v} 0}\left(\frac{Z^{*} e}{k T}(\nabla \Phi) c+\nabla C+\frac{c f \Omega}{k T} \nabla \sigma^{\mathrm{sp}}+\frac{c}{k T^{2}} Q^{*}\right)
\tag{2}
$$

where $D_{\mathrm{v}}$ is effective vacancy diffusivity; $Z^{*}$ is effective charge number; $e$ is electron charge; $k$ is Boltzmann's constant; $T$ is temperature, $\Phi$ is electrical potential, $f$ is vacancy relaxation ratio defined as ratio of vacancy volume over volume of an atom, $\Omega$ is atomic volume. $\sigma^{\text {sp }}$ is spherical part of stress tensor. $Q^{*}$ is heat of transport defined as heat transmitted by an atom jumping a lattice site less the intrinsic enthalpy. The mass diffusion process is governed by Fick's law of diffusion. In PDC loadings, electron wind forces terms is effective only at load-on time, while vacancy concentration, stress gradient and thermal gradient terms are active during the whole loading history.

In a site of flux divergence, vacancy will accumulate, nucleate or vanish, and this vacancy dynamics is given by:

$$
G=-C_{\mathrm{v} 0} \frac{c-\exp \left[\frac{(1-f) \Omega \sigma^{\mathrm{sp}}}{k T}\right]}{\tau_{\mathrm{s}}}
\tag{3}
$$

where $\tau_{\mathrm{s}}$ is characteristic vacancy generation or annihilation time.

### 2.2. Force equilibrium equation

Mass accumulation at anode side induces a compression stress; while vacancy formation at cathode side generates tensile stress locally. Thus, a stress gradient is created. In absence of body forces, the force equilibrium equation during current loading is given by the static equilibrium equation:

$$
\sigma_{i j, j}=0
\tag{4}
$$

where $\sigma_{i j, j}$ is derivative of stress with respect to degree of $j$.

### 2.3. Heat transfer equation

In flip-chip BGA connections, current crowding happens at Al/Cu interconnecting solder joint corners. Joule heating produces a higher local temperature than the nominal value at center cross-section of solder joints. It induces a thermal gradient, which drives mass diffuse from high temperature to low temperature area [26]. The governing equation of joule heating production and heat transfer is given by:

$$
\rho C_{\mathrm{p}} \frac{\partial T}{\partial t}-\nabla\left(k_{\mathrm{h}} \nabla T\right)-\rho Q=0
\tag{5}
$$

where is material density; $C_{\mathrm{p}}$ is specific heat; $k_{\mathrm{h}}$ is coefficient of heat transfer and $Q \propto I^{2} R$ is joule heating generated within conductor. Since the current density distribution is independent of time varying electric field, thermal gradient driving mass diffusion is in constant direction during PDC loading history.

### 2.4. Electrical conduction equation

The electric field in a conducting material is governed by Maxwell's equation of conservation of charge given by:

$$
\int_{S} J n \mathrm{~d} S=0
\tag{6}
$$

where $S$ is surface of a control volume, $n$ is outward normal to $S, J$ is current density in $\mathrm{A} / \mathrm{cm}^{2}$. Applying the divergence theorem to convert the surface integral into volume integral, we obtain following electrical conduction equation:

$$
\int_{V} \frac{\partial}{\partial x} J \mathrm{~d} V=0
\tag{7}
$$

### 2.5. Entropy based damage evolution model

Statistical thermodynamics provides a general framework for macroscopic description of irreversible microscopic damage processes. Entropy is a macroscopic measure of number of ways atoms or molecules can be arranged in a given volume. It can be decoupled into reversible and irreversible production inside a closed system. The irreversible entropy production in the closed system is a measure of microscopic disorder. Moreover, energy always flows spontaneously from regions of higher temperature to those of lower temperature, thus to reduce the initial state of order and to a higher level of disorder. It has been shown by Basaran [27,28] that the change in disorder parameter in Boltzmann's equation which relates entropy production to system disorder can be used as a metric for material degradation. Boltzmann's equation gives the probability relationship between entropy production and microscopic disorder as follows:

$$
s=k \ln W
\tag{8}
$$

where $k$ is Boltzmann's constant, $W$ is a disorder parameter which gives the number of micro states corresponding to given macrostate. The relationship between entropy per unite mass and the disorder parameter is given by the following equation:

$$
s=\frac{R}{m_{\mathrm{s}}} \ln W=N_{0} k \ln W
\tag{9}
$$

where $R$ is universal gas constant, $m_{\mathrm{s}}$ is specific mass, and $N_{0}$ is Avogadro's constant. By a simple transformation, the disorder function can be written as:

$$
W=e^{\frac{s}{N_{0} k}}
\tag{10}
$$

Degradation metric is further defined as a ratio of change in disorder parameter with respect to an initial disorder state as follows:

$$
D=D_{c r} \frac{W-W_{0}}{W_{0}}=D_{c r} \frac{\Delta W}{W_{0}}=D_{c r}\left(1-e^{\frac{W_{0}-W}{D_{0}^{k}}}\right)
\tag{11}
$$

where $D_{cr}$ is the critical damage used to define failure. The damage parameter $D$ varying from 0 to 1 is a scalar value utilized to map degradation of the material. It can easily be calculated separately for each direction. Zero indicates no damage happened, while 1 corresponds to broken of material. It is used to map degradation of both isotropic and anisotropic material property like elastic modulus, isotropic or kinematic hardening parameters. Detailed derivation and experimental validation of this entropy based damage model has been reported by Basaran et al. [29-39]. $D$ is applied to the elasticity constitutive relationship as [40]:

$$
d \sigma=(1-D) C^{e} d \varepsilon^{e}
\tag{12}
$$

Entropy production during EM process is generated by several factors as shown below:

$$
\Delta s=\int_{t_{0}}^{t}\left\{\frac{1}{t^{2}} c \nabla T: \nabla T+\frac{C_{v} D_{v}}{k T^{2}} F: F+\frac{1}{T \rho} \sigma: \varepsilon^{\prime v p}\right\} \mathrm{dt}
\tag{13}
$$

where $\frac{1}{t^{2}} c \nabla T: \nabla T$ is joule heating generated entropy; $\frac{C_{v} D_{v}}{k T^{2}} F: F$ and $\frac{1}{T \rho} \sigma: \varepsilon^{\prime v p}$ correspond to mass diffusion and viscoplastic deformation produced entropy respectively.

By substituting Eq. (13) into Eq. (11), damage parameter evolution can be given by:

$$
D=D_{c r}\left[1-e^{\frac{-\int_{t_{0}}^{t}\left\{\frac{1}{t^{2}} c \nabla T: \nabla T+\frac{C_{v} D_{v}}{k T^{2}} F: F+\frac{1}{T \rho} \sigma: \varepsilon^{\prime v p}\right\} d t}{k D_{0}}}\right]
\tag{14}
$$

where $F$, is diffusion driving force given by $F_{k}=-\left(Z^{\prime} e \nabla \varphi+f \Omega \nabla \sigma^{\mathrm{sp}}+\frac{Q^{\prime}}{T} \nabla T+\frac{k T}{c} \nabla c\right)$. SAC solders have a $252{^\circ}C$ melting temperature. As a result, it undergoes viscoplasticity, Basaran et al. [41] proposed the following creep rate $\dot{\varepsilon}_{i j}^{v p}=\frac{A d_{o} E b}{k T}\left(\sqrt{ } \frac{V}{E}\right)\left(\frac{b}{d}\right)^{p} e^{-Q / R T} \frac{\partial F}{\partial \sigma_{i j}}$. Where $A$ is a dimensionless material parameter to describe the strain rate sensitivity, $D_{0}$ is a diffusion frequency factor, $E$ is Young's modulus, $b$ is characteristic length of crystal dislocation, $k$ is Boltzmann's constant, $T$ is absolute temperature, $d$ is average phase size, $p$ is phase size exponent, $Q$ is creep activation energy for viscoplastic flow, $R$ is the universal gas constant, $F$ is viscoplastic yield function define as:

$$
F_{n+1}(\xi, \alpha)=\left\|\xi_{n+1}\right\|=(1-D) \sqrt{\frac{2}{3}} \bar{\sigma}\left(\alpha_{n}\right)
\tag{15}
$$

where $\xi$ is effective yield stress given by equation which takes into account of linear and nonlinear kinematic hardening component, and $\bar{\sigma}(\alpha_{n})$ represents isotropic hardening component. $D$ reflects isotropic hardening degradation.

$$
\xi_{n+1}^{\text {trial }}=S_{n+1}^{\text {trial }}=X_{n}
\tag{16}
$$

$X_{n}$ is back stress tensor or kinematic hardening component defined as:

$$
\frac{\partial X}{\partial t}=\frac{2}{3}(1-D) \gamma H^{\prime}(\alpha) \frac{\xi}{\|\xi\|}
\tag{17}
$$

where $H'(\alpha)$ is kinematic hardening modulus; $\alpha$ is equivalent plastic strain given by $\int \sqrt{\frac{2}{3}} \dot{\varepsilon}_{i j}^{p} \dot{\varepsilon}_{i j}^{p} \mathrm{dt}$; $\gamma$ is the consistency parameter which has the following relationship with $\alpha$ as $\dot{\sigma}=\sqrt{\frac{2}{3} \gamma}$. $D$ maps degradation of kinematic hardening. The isotropic hardening model has the following form of:

$$
\bar{\sigma}(\sigma)=\frac{2}{3} \sigma_{y 0}+R_{\infty}\left[1-e^{-c \alpha}\right]
\tag{18}
$$

where $\sigma_{y 0}$ is the initial yield stress at uniaxial tension, and $R_{\infty}$ is the isotropic hardening saturation value.

## 3. Finite element modeling

An ABAQUS UMAT subroutine was developed to conduct EM analysis of lead free SAC405 solder joints under pulse current loading. The program is verified to produce converged stable numerical results in our previous published works [30,33,35,42-45]. Duty factor, frequency and maximum current density are used as control parameters in the simulation. The finite element analysis (FEA) mesh is shown in Fig. 1.

Solder joint has a nominal diameter of $116 \mu \mathrm{m}$ and stand-off height of $100 \mu \mathrm{m}$. The Al interconnect located above the solder joint has thickness of $2 \mu \mathrm{m}$ and $\mathrm{Cu}$ trace below the solder joint has thickness of $10 \mu \mathrm{m}$. Current comes from the top-left $\mathrm{Al}$ thin film, flows through the solder joint, and goes out from the bottom-right $\mathrm{Cu}$ trace. Current distribution is not uniform throughout the whole cross section of the solder joint. Current density at aluminium/copper traces interconnect solder joint corner is much larger than the average current density as shown in Fig. 1, which makes current crowding corners most vulnerable to EM and joule heating induced damages [46,47]. Eight-node user defined thermal-electrical elements with unit thickness are used to mesh $\mathrm{Al} / \mathrm{Cu}$ traces and the solder joint.

Fig. 2 shows PDC current loading applied between left-top and right-bottom of the FEA model. Duty factor $r$ is defined as $2 t / T$. PDC current frequency varies from 0.01 to $20 \mathrm{~Hz}$, duty factors from 0.38 to 1.0 and maximum current densities from $8.1 \times 10^{5} \mathrm{~A} / \mathrm{cm}^{2}$ and $4.8 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$. EM in solder joints subjected to DC (duty factor of 1.0) loadings is studied for comparison purpose. Average operating ambient temperature for most IC devices is about $330.2 \mathrm{~K}$. The vacancy relaxation time for SAC405 is $1.8 \times 10^{-3} \mathrm{~s}$, effective charge number is 10 , grain boundary diffusivity is $2.72 \times 10^{6} \mu \mathrm{m}^{2} / \mathrm{s}$, thermal conductivity is $57.3 \mathrm{~W} /(\mathrm{m} \mathrm{k})$, initial vacancy concentration is $1.1 \times 10^{6} \mu \mathrm{m}^{-3}$, and average vacancy relaxation ratio is 0.2 . Since the working temperature of solder joint is about two third of its melting point in absolute temperature scale, $330 \mathrm{~K} /(273+252)$ $K=0.63$, viscoplastic material behavior is considered in this research. The linear kinematic hardening constant of SAC405 solder alloy is $9.63 \times 10^{9} \mathrm{~kg} \mathrm{~s} / \mathrm{m}$, nonlinear kinematic hardening constant is $7.25 \times 10^{8} \mathrm{~kg} \mathrm{~s} /(\mathrm{K} \mathrm{m})$ and isotropic hardening constant is 383.3 [41,48-51].

## 4. Numerical results and discussion

Current density distribution during load-on time along the diagonal section A-B of solder ball is shown in Fig. 3.

It can be seen that the current density distribution is not uniform along cross-section A-B. Current crowding behavior is

![](./images/813246235879145472_1.jpg)

Fig. 1. Finite element mesh and electric potential gradient distribution of simulated model.

![](./images/813246235879145472_2.jpg)

Fig. 2. Pulse current load applied in simulations.

![](./images/813246235879145472_3.jpg)

Fig. 3. Current density distribution along diagonal cross-section A-B during PDC loading history.

observed at both upper-left corner A and lower-right corner B with $j_A = 1.2 \times 10^6$ A/cm² and $j_B = 1.99 \times 10^6$ A/cm², which are more than 3 times of the average value at center cross-section of the solder ball. Current crowding effect induces a higher than usual temperature locally. In this study, highest temperature of 381 K happens at corner B and lowest temperature of 370 K near bottom of solder bump, which creates a thermal gradient of 1571 K/cm across the solder joint. This thermal gradient is large enough to drive mass transport from high temperature region into low temperature regions [26,52,53]. Depending on direction of thermal gradient, TM may hinder or accelerate the EM process. Both EM and TM driven mass diffusions are considered in this work.

### 4.1. Vacancy concentration evolution in solder joint under PDC current loading

Fig. 4a shows normalized vacancy concentration evolution at anode and cathode sides of the solder joint. It can be seen that voids form at cathode side while mass accumulates at the anode side. Normalized vacancy concentration fluctuates up and down forming a band during current loading history. It grows to 1.068 at cathode side and goes down to 0.957 at the anode side after 6.7 h of PDC current loading. An exponential relationship exists between vacancy concentration and current loading time. Fig. 4b shows vacancy concentration distribution along diagonal cross-section A-B and center cross-section C-D of the solder bump after 6.7 h PDC loading with a frequency of 0.1 Hz and a duty factor of 50%. We can see that mass piles up at corner A, which induces local compression stress. Vacancy concentration then increases along diagonal A-B, and reaches its largest value at corner B which produces tensile stress locally. Stress gradient and vacancy concentration gradient are thus created in the solder joint. The vacancy concentration gradient is often referred to as chemical potential. According to Fick's law, concentration gradient transport mass from high concentration area to the low concentration area, which retard the electron wind force driving mass diffusion. The stress gradient has similar effect. It can also be seen from Fig. 4b that vacancy concentration along center line is not uniform as well, with vacancy accumulating at center and mass piling up at outer surface of the solder joint. This phenomenon is due to the thermal gradient driving mass flux between center of solder joint and the outer skin, which is consistent with experimental observations [54].

Normalized vacancy concentration evolution at anode side of solder joints for various duty factors at a constant PDC frequency of 0.05 Hz is shown in Fig. 5. It can be seen higher duty factor induces a larger vacancy depletion/mass accumulation rate. Vacancy concentration goes up and down continuously forming a fluctuation band that gradually decreases during the current loading history for PDC cases. For DC loading, however, the vacancy concentration is observed to decrease continuously without such band formation, and rate of depletion is much faster than those subjected to PDC loading with the same maximum current density

![](./images/813246235879145472_4.jpg)

Fig. 4. Vacancy concentration evolution history under pulse current loading of 0.1 Hz and duty factor of 0.5: (a) vacancy concentration evolution at corner A and B and (b) vacancy concentration along diagonal cross-section A-B and center cross-section C-D after 6.7 h pulse current loading.

![](./images/813246235879145472_5.jpg)

Fig. 5. Duty factor r dependence of vacancy concentration during current loading history at corner A (anode) of solder bump, with frequency of 0.05 Hz.

![](./images/813246235879145472_6.jpg)

Fig. 6. Frequency dependence of vacancy concentration evolution at corner B (cathode), with maximum current density $j_{a}=2.0 \times 10^{6} \mathrm{~A} / \mathrm{cm}^{2}$ and duty factor of 0.5.

![](./images/813246235879145472_7.jpg)

Fig. 7. Volumetric and shear stress evolution at anode and cathode of solder bump during pulse current loading history of 0.05 Hz, duty factor of 0.5: (a) volumetric stress and (b) shear stress.

and ambient temperature. Frequency dependence of normalized vacancy concentration evolution history at cathode side is shown in Fig. 6.

It can be observed that vacancy concentration grows exponen- tially during loading history. Higher frequency introduces a larger vacancy accumulation rate. At 20 Hz, the vacancy concentration accumulates so fast that fails the solder joint in just 1000 s. High frequency comes with a shortened thermal dissipation time, which introduces more thermal damage to material under tests.

From the above observations, it can be concluded that both TM and EM happen during the pulse current loading history. The mass diffusion mechanism in solder joint is complicate in the sense that four types of driving forces couple with each other: electric wind force, thermal gradient, chemical potential and stress gradient. During the PDC load-on time, the electric wind force drives mass from cathode side to the anode side; depending on thermal gradi- ent direction, thermal gradient may accelerate or impede the EM process; while stress gradient and chemical potential always drives the mass in the opposite direction of electron wind force. During the load-off time, however, only thermal gradient, stress gradient and vacancy concentration come to play, which transport mass backward to cathode side and heal part of damage triggered during loading-on time [18-20]. This material healing effect exhib- its as a fluctuation response in the damage evolution history, and in turn makes lifetime of solder joint under PDC load much longer than those under DC loading. Effectiveness of this damage healing mechanism depends on pulse current frequency, duty factor and ambient temperature. Increasing frequency and duty factor leads to more serious damage in the solder joints.

### 4.2. Stresses in flip-chip solder bumps during pulse current stressing

Volumetric and shear stress evolution history at current crowd- ing corners of the solder ball subjected to PDC with duty factor of 0.5 and frequency of 0.05 Hz is shown in Fig. 7.

It can be seen that compression stress develops at anode side due to the mass pile-up, while tension stress develops at cathode side due to void formation shown above. Exponential relationship exists between stresses development and loading time. After 6.7 h of current loading, both compression and tension stress reaches about 20 MPa. From Fig. 7b, we can see that shear stress develops at both anode and cathode side of the solder joint. After 6.7 h of

![](./images/813246235879145472_8.jpg)

Fig. 8. Volumetric stress evolution at cathode side of the solder joint subjected to 0.05 Hz PDC with maximum current density $j_{B}=2.0\times 10^{6}\ \text{A/cm}^2$: (a) duty factor dependence and (b) frequency dependence.

![](./images/813246235879145472_9.jpg)

Fig. 9. Shear stress evolution at cathode side of the solder joint subjected to to 0.05 Hz PDC with maximum current density $j_{B}=2.0\times 10^{6}\ \text{A/cm}^{2}$: (a) duty factor dependence and (b) frequency dependence.

current loading, shear stress at anode is 9.8 MPa, which is one and half times of that at cathode side, 6.5 MPa. Room temperature yield stress is at 7 MPa. Duty factor and frequency dependence of volumetric stress evolution is shown in Fig. 8.

Volumetric stress growth rate strongly depends on duty factor. Increasing duty factor is associated with a faster volumetric stress accumulation rate. After 3.3 h, the volumetric stress for DC loading, which correspond to duty factor of 1.0, has reached 19 MPa; while it takes 5 h for duty factor of 0.72 PDC loading at the same maximum current density to reach this value. For the duty factor of 0.38, the volumetric stress is only 9 MPa after 6.7 h of current loading, which is a far less than larger duty factor loading induced stress. Fig. 8b is the frequency dependence of volumetric stress evolution. It can be seen that volumetric stress grow exponentially with loading time, and higher frequency causes a larger stress growth rate. However when the frequency is below 1 Hz, stress is no longer frequency dependent. For frequency low enough, thermal fatigue governs the damage process instead of electric current loading. Only when the frequency goes above a threshold value (1 Hz here), volumetric stress growth rate tends to increase dramatically. Duty factor and frequency dependence of shear stress evolution is shown in Fig. 9.

Same as volumetric stress development, higher duty factor and frequency induce a larger shear stress growth rate. The duty factor dependence of shear stress over DC loading cases, however, is smaller than the volumetric stress dependence, and the relation- ship is given by $S_{\text{shear}_{\text{pdc}}}=r'S_{\text{shear}_{\text{dc}}}$ with $r'$ ranging between $r$ and $r^{2}$ based on our statistical analysis. Nonlinear regression results (with $R$-square of 0.9936) indicate that both volumetric stress and shear stress grow exponentially vs. the loading time in hours, and the exponential parameters for volumetric stress and shear stress are 1.03 and 1.8 respectively, as shown in following equation:

$$
S=\alpha \times e^{\beta t} \tag{19}
$$

where $S$ represents volumetric stress or shear stress, $\alpha$ is parameter depending on PDC frequency and duty factor; $\beta$ is stress exponent which is between 1 and 2.

### 4.3. EM damage in solder joints under PDC and DC current stresses

Due to the back-flow healing mechanism at loading-off time, solder joints subjected to PDC loading has a longer lifespan

![](./images/813246235879145472_10.jpg)

Fig. 10. Damage evolutions at cathode and anode sides of the solder joint subjected to 0.05 Hz PDC loading with duty factor of 0.5.

![](./images/813246235879145472_11.jpg)

![](./images/813246235879145472_12.jpg)

Fig. 11. Damage distribution along diagonal cross-section of the solder joint after 6.7 h 0.1 Hz PDC loading at duty factor of 0.5.

compared to those subjected to DC current loading under otherwise the same conditions. Entropy based damage evolution is used to approximate EM induced failure mechanism.

It can be seen from Fig. 10 that damage as designed by Eq. (13) grows exponentially at both anode and cathode sides of the solder joint when subjected to PDC current loading at frequency of

![](./images/813246235879145472_13.jpg)

Fig. 12. Damage at cathode side of the solder joint for various duty factors with pulse frequency of 0.05 Hz: (a) damage evolution history and (b) damage vs. duty factor after 3.3 h of current loadings.

0.05 Hz and duty factor of 0.5. However, the irreversible entropy production at anode side develops much faster than that at the cathode side. This is due to the damage mechanism adopted in this study. Mass accumulation tends to produce more entropy than va- cancy concentration under the same conditions. After 6.7 h current loading, the damage at cathode is 0.012, which is about 8 times lar- ger than that at anode side. The damage distribution along diago- nal and center cross-sections of the solder joint after 6.7 h of PDC loading is shown in Fig. 11. It can be seen that damage first de- creases along diagonal A-B, then increases. For center cross-section C-D, maximum damage happens at outer skin of the solder joint, where compression stress developed locally. The minimum dam- age happens at center of the solder joint.

In modern electronic packaging technology, the following pro- cedures are often used to protect solder joints from short-circuit failures: 1. Minimum clearance between conductors is specified in PC board prevents conducting between neighboring solder joints. Although entropy production at anode side develops much faster than that at the cathode side, only vacancy accumulation induced open-circuit failure is of concern in electronic devices [55-58]. Thus only damage at cathode side is shown in the follow- ing discussions.

Fig. 12 shows the duty factor dependence of damage evolution at cathode side of the solder joint subjected to 0.05 Hz PDC loading. Damage grows exponentially during current loading history. Larger duty factor induces a higher damage growth rate. After 3.3 h of loading, the damage in DC loading has accumulated to 2 times of PDC loading with a duty factor at 0.38, and nearly 1.5 times of damage with duty factor at 0.5. Damage vs. PDC duty factor is pot- ted in Fig. 12b.

For frequency dependence, it is observed that damage accumu- lation is frequency independent when applied PDC signal is below 1 Hz as shown in Fig. 13.

It can be that damage grows faster at higher frequency. This can be explained by the fact that pulse current period used in this study is much larger than the thermal relaxation time (typically

![](./images/813246235879145472_14.jpg)

Fig. 13. Frequency dependence of damage evolution at cathode side of the solder joint subject to PDC loading with duty factor of 0.5.

![](./images/813246235879145472_15.jpg)

Fig. 14. Maximum current density dependence of damage evolution at cathode side of the solder joint subjected to 0.05 Hz PDC loading with duty factor of 0.5.

in order of $10^{-6}$ s for SAC solder alloy). In this frequency range, the solder has more time to relax from the joule heating induced thermal damage than at lower frequencies, thus more damage gets healed. The current density dependence of EM damage evolution is shown in Fig. 14.

Damage accumulates exponentially with loading time. Larger current density causes much more serious EM damage. After 1.3 h of current loading, the damage of the solder joint subjected to a maximum current density of $4.8 \times 10^{6}$ A/cm² has reached $2.3 \times 10^{-3}$, while the one with maximum current density of $81 \times 10^{5}$ A/cm² is only $2.1 \times 10^{-4}$.

Table 1 shows the nonlinear regression results of damage vs. duty factors, frequencies and current densities. With an R-square value (confidence value, which means representative of data points) as large as 99%, it has been found that the duty factor, frequency and maximum current density dependence of electromigration damage follows an exponential relationship when the loading period is larger than the thermal relaxation time:
$$
D = a \times e^{bt} - c \times e^{-dt} \tag{20}
$$
where $D$ is the damage; $a, b, c$ and $d$ are all positive parameters that depend on duty factor, pulse frequency and maximum current density. For a loading period long enough (over 6 h), the second part of Eq. (16) will be only 1% of the first part, thus we can ignore the second parts influence, which will simplify above equation into the following representation:
$$
D = a \times e^{b_{r}b_{f}b_{j}t} \tag{21}
$$
where $a$ is the general parameter that depends on duty factor and frequency, $b_{r}$ is duty factor exponent parameter, $b_{f}$ is frequency exponent parameter, $b_{j}$ is current density parameter and $t$ is current loading times in hours. For a frequency of 0.05 Hz, it has been found that both parameter $a$ and $b_{r}$ grow with increasing duty factor $r$, and the value of $b_{r}$ is approximately $r^{1.1}/9$. For a duty factor of 0.5, it can be seen from Table 1 that with increasing frequency magnitude parameter $a$ decreases, but parameter $b_{f}$ increase quickly. Nonlinear regression gives us the following relationship between parameter $b_{f}$ and pulse frequency $f$ (with $R$-square of 0.999):
$$
b_{f} = 0.161 \times f^{1.431} \tag{22}
$$

<table>
<caption>Table 1 Nonlinear regression results of duty factor, frequency dependences and maximum current density dependence of damage at cathode side of the solder joint.</caption>
<thead>
<tr>
<th>Dependence</th>
<th>Duty factor</th>
<th>Frequency (Hz)</th>
<th>Current density (A/cm²)</th>
<th>Damage vs. time (h)</th>
<th>Adjust R-square</th>
</tr>
</thead>
<tbody>
<tr>
<td>Duty factor</td>
<td>0.38</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0006 × e⁰·⁰⁴ᵗ − 0.0005 × e⁻⁰·⁷ᵗ</td>
<td>0.999</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0009 × e⁰·⁰⁶ᵗ − 0.00075 × e⁻⁰·⁷⁵ᵗ</td>
<td>0.998</td>
</tr>
<tr>
<td></td>
<td>0.72</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.00092 × e⁰·⁰⁸ᵗ − 0.0008 × e⁻⁰·⁹⁵ᵗ</td>
<td>0.998</td>
</tr>
<tr>
<td></td>
<td>1.00</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0011 × e⁰·¹¹ᵗ − 0.00096 × e⁻¹·⁵ᵗ</td>
<td>0.996</td>
</tr>
<tr>
<td>Frequency</td>
<td>0.50</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0009 × e⁰·⁰⁶ᵗ − 0.00075 × e⁻⁰·⁷⁵ᵗ</td>
<td>0.998</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>0.50</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0005 × e⁰·³⁴ᵗ − 0.00038 × e⁻²·⁵ᵗ</td>
<td>0.998</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>5.00</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0003 × e¹·⁵ᵗ − 0.0002 × e⁻²·³ᵗ</td>
<td>0.999</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>20.00</td>
<td>2.0 × 10⁶</td>
<td>D = 0.00013 × e¹¹·⁷ᵗ</td>
<td>0.996</td>
</tr>
<tr>
<td>Current density</td>
<td>0.50</td>
<td>0.05</td>
<td>8.1 × 10⁵</td>
<td>D = 0.0003 × e⁰·⁰¹⁴ᵗ − 0.00024 × e⁻⁰·¹ᵗ</td>
<td>0.920</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>0.05</td>
<td>2.0 × 10⁶</td>
<td>D = 0.0009 × e⁰·⁰⁶ᵗ − 0.00075 × e⁻⁰·⁷⁵ᵗ</td>
<td>0.998</td>
</tr>
<tr>
<td></td>
<td>0.50</td>
<td>0.05</td>
<td>4.8 × 10⁶</td>
<td>D = 0.0014 × e⁰·³⁴ᵗ − 0.0012 × e⁻³·⁷ᵗ</td>
<td>0.997</td>
</tr>
</tbody>
</table>

In the same manner, we obtain the following relationship between $b_j$ and current density $j$ (A/mm²) with confidence value of 0.9998:

$$
b_j = 2.280 \times 10^{-12} \times j^{1.9} \tag{23}
$$

After we put equation $b_j$, $b_f$ and $b_r$ back into Eq. (17), we finally obtain the relationship between damage, duty factor and frequency as follows:

$$
D = a \times e^{b_r r^{1.1} f^{1.43} j^{1.9} t} \tag{24}
$$

We further define mean time to failure (MTTF) as entropy based damage accumulated to a critical value, which is taken as 0.01 in this work for sake of simplicity. Basaran et al. [28] proposed a MTTF equation for solder joint subjected to DC based on intensive laboratory testing of test vehicles with SAC405 solder joints. By introducing duty factor and frequency influence on this equation, the following MTTF equation is obtained:

$$
\text{MTTF} = \frac{\alpha}{r^{1.1} \cdot f^{1.43} \cdot j^{1.9}} \tag{25}
$$

where $\alpha$ is a general parameter. We can see that MTF for PDC case is inversely proportional with duty factor $r^{1.1}$, pulse frequency $f^{1.43}$ and maximum current density $j^{1.9}$. Since the above relationship is obtained at constant ambient temperature, we can incorporate temperature effect by Arrhenius temperature dependence into above equation, which gives us as the modified MTTF equation for pulse current loading cases as follows:

$$
\text{MTTF} = \frac{\alpha}{r^{1.1} \cdot f^{1.43} \cdot j^{1.9}} e^{(\Delta E / k T)} \tag{26}
$$

where $\alpha$ is general parameter that depends on material, geometry, duty factor, frequency and the assumed critical damage value, $\Delta E$ is diffusion activation energy, $k$ is Boltzmann's constant and $T$ is temperature. To verify the computer simulation results, experiments are conducted on solders subjected to pulsed current loading with duty factor, frequency and current density as controlling parameters. The following failure mechanism is obtained:

$$
\text{MTTF} = \frac{\alpha}{r^{1.2} \cdot f^{1.8} \cdot j^{1.7}} e^{\nabla E / k T} \tag{27}
$$

We have less than 10% discrepancy for the current density and duty cycle exponent, 20% discrepancy for the frequency component, which is acceptable considering manufacture induced initial defects in our test vehicle. It can be seen that our program gives a very good approximation to failure mechanism of solder joints under PDC current loadings.

## 5. Conclusions

A fully coupled thermal-electrical-mechanical-chemical damage model is proposed for SAC405 solder joints subjected to pulse current loading. For comparison purpose, DC electromigration study is also conducted. By inspection of the simulation results, the following findings are reported.

During pulse current loading history, vacancy concentration and stress fluctuate up and down in a gradually growing (cathode) or depleting (anode) band. By using irreversible entropy production rate as a metric to quantify material degradation under PDC loading, it is observed that higher frequency induces a faster damage growth rate. This is due to the fact that material has more time to relax from joule heating induced damage at low frequency than at higher frequency. It is further observed that larger duty factor and current density leads to an increased EM damage. An exponential relationship exists between EM/TM damage, duty factor, current density and PDC frequency. After incorporating the entropy based damage model into Basaran's MTTF equation, we propose a modified MTTF equation for lead-free solder joints under pulse current loading, which incorporates both thermomigration and electromigration damages. The finite element simulation results are verified by our experiments.

## Acknowledgments

This research project has been sponsored by the US Navy, Office of Naval Research, Advanced Electrical Power Program under the Direction of Terry Ericsen.

## References

[1] X. Chen et al., Applied Physics Letters 87 (23) (2005) 233506.
[2] R. Frankovic, G.H. Bernstein, J.J. Clement, IEEE Electron Device Letters 17 (5) (1996) 244-246.
[3] M.I. Amir Averbuch, Igor Ravve, Irad Yavneh, Journal of Computational Physics 167 (2) (2001).
[4] C. Basaran, Shidong Li, D.C. Hopkins, Wei Yao, Mean time to failure of SnAgCuNi solder joints under DC, in: Thirteenth IEEE Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), 2012.
[5] Wei Yao, Cemal Basaran, Skin effect and material degradation of lead-free solder joint under AC. in: Thirteenth IEEE Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), 2012.
[6] Yao. Wei, Electronic Materials Letters 8 (5) (2012) 503-505.
[7] J.R. Lloyd, Journal of Physics D: Applied Physics 32(109R)(1999).
[8] R. Peierls, A.K. Das, Journal of Physics C: Solid State Physics, 8(20) (1975).
[9] H.Z. Zhilin Li, Huajian Gao, Journal of Computational Physics 152(1)(1999).
[10] B.K. Liew, N.W. Cheung, C. Hu, Electromigration interconnect lifetime under AC and pulse DC stress. in: Twenty Seventh Annual Proceedings: Reliability Physics, Piscataway, NJ, United States: Publ by IEEE, April 11 1989.
[11] B.K. Liew, N.W. Cheung, C. Hu, Electromigration interconnect failure under pulse test conditions, Japan Soc. Appl. Phys., Tokyo, Japan, 1988.

[12] B.J. Root, S.J. Nagalingam, Electromigration Failure On Fine Line Conductors Under Pulse Test Conditions, IEEE, New York, NY, USA, 1985.

[13] T. Jiang, N.W. Cheung, H. Chenming, IEEE Transactions on Electron Devices 41 (4) (1994) 539-545.

[14] L. Zhihong et al., IEEE Transactions on Electron Devices 46 (1) (1999) 70-77.

[15] L.R. C Pennetta, Gy Trefan, A Scorzoni FFantini, I De Munan, Journal of Physics D: Applied Physics 34 (1421) 2001.

[16] Z. Ya-Xiong, N. Li-Sha, Computational Materials Science 46 (2) (2009) 443-446.

[17] H. Nguyen Van, C. Salm, Computational Materials Science 49 (4) (2010) 235-238.

[18] H.L. Hartnagel, B.R. Sethi, Journal of Physics D: Applied Physics 18(2) 1985.

[19] M.I. Amir Averbuch, Igor Ravve, Journal of Computational Physics 186(2) (2003).

[20] W. Yao, C. Basaran, Journal of Applied Physics 111 (6) (2012) 063703.

[21] C. Basaran, Shidong Li, Douglas C. Hopkins, Damien Veychard, Electromigration Time to Failure of SnAgCuNi Solder Joints, ASME InterPack, 2009.

[22] S. Li, M.F. Abdulhamid, C. Basaran, Simulation 84 (8-9) (2008) 391-401.

[23] S. Li, Michael S. Sellers, Cemal Basaran, Andrew J. Schultz, David A. Kofke, Computational Materials Science 6 (2009) 2798-2808.

[24] Y. Wei, C. Basaran. Damage of SAC405 solder joint under PDC. in: Thirteenth IEEE Intersociety Conference on Thermal and Thermomechanical Phenomena in Electronic Systems (ITherm), 2012.

[25] M. Abdulhamid, C. Basaran, Y. Lai, IEEE Trans. on Advanced Packaging 32 (3) (2009) 627-635.

[26] H. Ye, C. Basaran, D. Hopkins, Applied Physics Letters 82 (7) (2003) 1045-1047.

[27] C. Basaran, S. Nie, International Journal of Solids and Structures 44 (3-4) (2007) 1099-1114.

[28] Y. Lee, C. Basaran, A viscoplasticity model for solder alloys. in: ASME 2010 International Mechanical Engineering Congress & Exposition IMECE, Vancover, British Columbia, Canada, 2010.

[29] C. Basaran, C.Y. Yan, Journal of Electronic Packaging 120 (4) (1998) 379-384.

[30] C. Basaran, L. Minghui, Y. Hua, A Thermodynamic Model For Electrical Current Induced Damage, IEEE, Piscataway, NJ, USA, 2004.

[31] C. Basaran, S. Nie, International Journal of Damage Mechanics 13 (3) (2004) 205-223.

[32] C. Basaran, Y. Zhao, H. Tang, J. Gomez, Journal of Electronic Packaging, 2005.

[33] C. Basaran, Minghui Lin, Shidong Li, Computational Simulation of Electromigration Induced Damage in Copper Interconnects, 2007.

[34] C. Basaran, H. Ye, D.C. Hopkins, D. Frear, J.K. Lin, Journal of Electronic Packaging 127 (2) (2005) 157-163.

[35] C. Basaran, M. Lin, Mechanics of Materials 40 (1-2) (2008) 66-79.

[36] C. Basaran, M. Lin, International Journal of Materials and Structural Integrity 1 (2007) 16-39.

[37] J. Gomez, C. Basaran, International Journal of Solids and Structures 42 (13) (2005) 3744-3772.

[38] H. Ye, C. Basaran, D.C. Hopkins, IEEE Transactions on Components and Packaging Technologies 26(3) (2003) 673-681 (see also IEEE Transactions on Components, Packaging and Manufacturing Technology, Part A: Packaging Technologies).

[39] Y. Zhao, C. Basaran, A. Cartwright, T. Dishongh, Mechanics of Materials 32 (2000) 161-173.

[40] H. Tang, A Thermodynamic Damage Mechanics Theory and Experimental Verification for Thermomechanical Fatigue Life Prediction of Microelectronics Solder Joints, Buffalo, University at Buffalo, The State University of New York, 2002.

[41] C. Basaran, S. Li, M.F. Abdulhamid, Journal of Applied Physics 103 (12) (2008) 123520-123529.

[42] C. Basaran, M. Lin, H. Ye, International Journal of Solids and Structures 40 (26) (2003) 7315-7327.

[43] C. Basaran, et al., Journal of Applied Physics 106(1) (2009) (013707-013707-10).

[44] B. Cemal, Multidiscipline Modeling in Materials and Structures 2 (2007) 309-326.

[45] S. Li, C. Basaran, Mechanics of Materials 41 (3) (2009) 271-278.

[46] K.N. Tu et al., Applied Physics Letters 76 (8) (2000) 988-990.

[47] R. Fei et al., Effect of Electromigration on Mechanical Behavior of Solder Joints, Materials Research Society, Warrendale, PA, USA, 2005.

[48] M.E. Sarychev et al., Journal of Applied Physics 86 (6) (1999) 3068-3075.

[49] M. Lin, C. Basaran, Computational Materials Science 34 (1) (2005) 82-98.

[50] H. Ye, Mechanical Behavior of Microelectronics and Power Electronics Solder Joints under High Current Density: Analytical Modeling and Experimental Investigation, Buffalo, University at Buffalo, State University of New York, 2004.

[51] R. Balzer, H. Sigvaldason, Physica Status Solidi B: Basic Research 92 (1) (1979) 143-147.

[52] M. Abdulhamid, C. Basaran, ASME Journal of Electronic Packaging 131 (12) (2009). 011002.

[53] Y. Dan et al., Journal of Applied Physics 102 (4) (2007). 043502.

[54] S. Li, M.F. Abdulhamid, C. Basaran, IEEE Transactions on Advanced Packaging 32 (2008) 478-485.

[55] J.M. Schoen, Journal of Applied Physics 51 (1) (1980) 508-512.

[56] L. Brooke, Pulsed Current Electromigration Failure Model, IEEE, New York, NY, USA, 1987.

[57] S.L. Cemal Basaran, Douglas C. Hopkins, Damien Veychard, Electromigration Time to Failure of SnAgCuNi Solder Joints. ASME InterPack, 2009.

[58] H. Ye, C. Basaran, Douglas C. Hopkins, International Journal of Solids and Structures 40(15) (2003) 4021-4032.