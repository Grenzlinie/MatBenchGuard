![](./images/812270245568839683_1.jpg)

Topography simulations for contact formation involving reactive ion etching,
sputtering and chemical vapor deposition

S. Takagi, S. Onoue, K. Iyanagi, K. Nishitani, and T. Shinmura

Citation: *Journal of Vacuum Science & Technology B* **23**, 1076 (2005); doi: 10.1116/1.1924609

View online: http://dx.doi.org/10.1116/1.1924609

View Table of Contents: http://scitation.aip.org/content/avs/journal/jvstb/23/3?ver=pdfcov

Published by the AVS: Science & Technology of Materials, Interfaces, and Processing

Articles you may be interested in

[Infinitely high etch selectivity during CH 2 F 2 / H 2 dual-frequency capacitively coupled plasma etching of silicon
nitride to chemical vapor-deposited a -C](http://)
J. Vac. Sci. Technol. A **28**, 755 (2010); 10.1116/1.3430551

[TiSiN films produced by chemical vapor deposition as diffusion barriers for Cu metallization](http://)
J. Vac. Sci. Technol. B **20**, 1471 (2002); 10.1116/1.1494068

[Microscopic mapping of specific contact resistances and long-term reliability tests on 4H-silicon carbide using
sputtered titanium tungsten contacts for high temperature device applications](http://)
J. Appl. Phys. **92**, 253 (2002); 10.1063/1.1481201

[Particle formation during low-pressure chemical vapor deposition from silane and oxygen: Measurement,
modeling, and film properties](http://)
J. Vac. Sci. Technol. A **20**, 413 (2002); 10.1116/1.1448506

[Full simulation of silicon chemical vapor deposition process](http://)
AIP Conf. Proc. **585**, 206 (2001); 10.1063/1.1407564

![](./images/812270245568839683_2.jpg)

# Topography simulations for contact formation involving reactive ion etching, sputtering and chemical vapor deposition

S. Takagi, $^{\text{a)}}$ S. Onoue, K. Iyanagi, K. Nishitani, and T. Shinmura
Corporate Manufacturing Engineering Center, Toshiba Corporation, 33 Shin-Isogo-cho, Isogo-ku, Yokohama, Kanagawa, Japan

(Received 26 July 2004; accepted 4 April 2005; published 2 June 2005)

With the shrinking design rule of semiconductor devices, the aspect ratios of contact holes that connect transistor electrodes to wirings have exceeded 10 at a design rule less than $0.15\ \mu\text{m}$. The contact is formed through sequential processes of reactive ion etching (RIE), TiN sputtering, and tungsten chemical vapor deposition (W–CVD). In such a formation process, a contact hole with a large bottom diameter is required to reduce contact resistance. We developed a contact simulation method for optimizing contact formation. This contact simulation involves sequential simulations of RIE, TiN sputtering, and W–CVD processes, which adopt a particle model based on the Monte Carlo method. These topography simulations were calibrated using experimental results, and each simulation was combined in order to calculate these sequential simulations. We calculated the dependences of etching and W–CVD filling profiles on contact hole depth. The simulation profiles of etching and W–CVD filling were in agreement with the experimental results. The sequential simulations showed that W disconnection occurs at over $2.5\ \mu\text{m}$ contact depth with a aspect ratio of 19.2 and the contact resistance increases markedly. © 2005 *American Vacuum Society*.

[DOI: 10.1116/1.1924609]

## I. INTRODUCTION

The miniaturization of semiconductor elements is advancing rapidly in line with the increasing level of integration and speed of semiconductor devices. Mass-production technology for devices of the 90 nm design rule has already been developed, and the development of technology for next-generation devices of the 65–45 nm design rule is underway.

With the shrinkage of the design rule, the diameters of contact holes that connect transistors to the first metal layer also decrease. On the other hand, the thickness of the insulator between transistors and the first metal layer cannot be reduced without degrading the insulation capability. Consequently, the aspect ratio of a contact hole increases rapidly. In particular, the contact hole that connects the gate electrode of a metal–oxide–semiconductor transistor to the first metal layer has an aspect ratio of more than 10 at the design rule less than $0.15\ \mu\text{m}.^{1,2}$

In the formation of a contact, the contact hole is first etched onto an insulator $\text{SiO}_{2}$ film. A liner/barrier metal is deposited on the surface of the contact hole by Ti/TiN sputtering, and finally, tungsten (W) is deposited on the surface of the barrier metal. $^{3,4}$ If the bottom diameter of the contact hole decreases, contact resistance increases due to the reduction of the contact area. If the etching diameter increases in the middle of a contact hole during reactive ion etching (RIE) (Bowing), $^{2}$ disconnection between the transistor electrode and the wiring occurs due to a large void generated during chemical vapor deposition (CVD) and subsequent chemical mechanical polishing.

For the optimization of contact formation, we must develop a sequential process of RIE, sputtering, and CVD. Since it is expected that the aspect ratio of next-generation devices will increase, effective development of the contact formation process is required. In the process development, topography simulation is considered to be effective. If the sequential processes of etching, sputtering, and CVD can be modeled, the etching profile suitable for achieving the desired contact resistance and the limitation of aspect ratio for filling with the contact hole can be determined by simulation. Therefore, the number of experiments can be reduced markedly.

However, so far, no topography simulation has accurately reproduced contact formation. In the etching process using fluorocarbon such as $\text{CF}_{4}$, $\text{C}_{4}\text{F}_{8}$, and $\text{C}_{5}\text{F}_{8}$, a polymer of $\text{CF}_{x}$ is deposited by the radicals such as $\text{CF}_{3}$, $\text{CF}_{2}$, and $\text{CF}_{2}$, and ion-enhanced etching of $\text{SiO}_{2}$ film is generated by the ions such as $\text{CF}_{3}^{+}$, $\text{CF}_{2}^{+}$, and $\text{CF}^{+}.^{1}$ The anisotropy of the etching profile is dependent on the balance between this deposition and etching. Therefore, it was very difficult to develop a simulation model including the surface reaction in etching. Moreover, to correlate process conditions and the etching profile, it is necessary to analyze the plasma and the surface reaction simulations simultaneously. It is even more difficult to calculate a sequential RIE, sputtering, and CVD process in contact formation.

We combined plasma, sheath, and surface reaction simulations, and calculated the etching profile corresponding to the process conditions. $^{5,6}$ For sputtering, we developed a model that can be used to calculate the generation of Ar plasma, emission of sputtered particles, and transport and

$^{\text{a)}}$Electronic mail: shigeyuki.takagi@toshiba.co.jp

---
1076 J. Vac. Sci. Technol. B 23(3), May/Jun 2005 0734-211X/2005/23(3)/1076/8/$22.00 ©2005 American Vacuum Society 1076

![](./images/812270245568839683_3.jpg)

FIG. 1. Processes for forming tungsten contact between a transistor and a wire. Contact hole is formed in SiO₂ film by etching, and Ti is deposited by sputtering on the contact hole surface. Finally, the contact hole is filled with tungsten.

deposition of the sputtered particles on the wafer surface.⁷
Moreover, we adopted a simple Monte Carlo model for analyzing CVD.⁸

In this study, the above topography simulations were applied to contact formation. The topography simulations for hole etching, sputtering of the barrier metal and W-CVD were calibrated using experimental results, and each simulation was combined in order to calculate these sequential processes. We evaluated the relationship between the contact depth and the etching profile, and confirmed that the simulated results agreed with the experimental results. Moreover, the gap-filling profile of W-CVD was evaluated in relation to etching depth using the simulation. Consequently, contact formation was reproduced by the sequential simulations of RIE, sputtering, and CVD.

## II. EXPERIMENT

Figure 1 shows contact formation using tungsten. First, the contact hole with a high aspect ratio is etched into an oxide film, and the photoresist mask for the etching is removed by the ashing process. In this process, there is little critical dimension (CD) loss and profile change due to use of an oxygen plasma excited by an inductively coupled plasma source. Next, sputtered TiN is deposited on the surface of the underlying SiO₂. Finally, tungsten (W) is deposited on the surface of the TiN film at a high temperature. The evaluated samples were thin films of photoresist, SiO₂ and SiN deposited on Si wafers. The thickness of the SiO₂ film was changed from 1.7 μm under the baseline conditions to 3.0 μm. Circular holes with diameters of 0.13 μm and taper angles of 89° were patterned on the photoresist film with a thickness of 300 nm.

A capacitively coupled 8 in. wafer plasma reactor was used for SiO₂ etching. A magnetic field was applied to the etching chamber. A power supply with a frequency of 13.56 MHz was connected to a rf electrode with a 266 mm diameter. The baseline conditions of etching were a rf power of 1500 W, and a mixture of C₅F₈, O₂, CO, and Ar gases. When SiO₂ film was etched under these conditions, the CD loss of 21.0 nm occurred at the bottom of the photoresist.

![](./images/812270245568839683_4.jpg)

FIG. 2. Flowchart of simulations for contact formation.

Long-throw sputtering (LTS) with a distance (L) of 300 mm between the target and the wafer was used.⁹ In this equipment, dc power is supplied only to the target and bias power is not applied to the wafer. Moreover, the sputtered particles are not excited midway between the target and the wafer, unlike in i physical vapor deposition equipment. The sputtered particles reached the wafer at near normal angle (parallel to the contact hole) via transport through a distance of 300 mm. The sputtered particles reached the bottom of the hole, and thereby the hole-filling capability was improved. Under the baseline conditions, the power input into the target of Ti was 6000 W. We deposited TiN with a thickness of 10 nm using a gas mixture of Ar/N₂ and a gas pressure of 0.5 Pa.

The W film was deposited with a thickness of 100 nm at a high temperature.¹⁰ Under the baseline conditions, we used a mixture of Ar, WF₆, SiH₄, and H₂ gases, a gas pressure of 5320 Pa, and a wafer temperature of 415 °C.

## III. SIMULATION MODEL

Figure 2 shows the flowchart of simulations. RIE, sputtering, and CVD simulations are performed sequentially corresponding to the actual process. The Monte Carlo method using the particle model is adopted in each topography simulation.⁷,⁸,¹¹⁻¹³ Both RIE and sputtering simulations include equipment and surface reaction simulations, and the profile change with the change of process conditions can be calculated. Each simulation model is explained in detail below.

### A. RIE simulation model

The RIE simulation model has been reported in detail in Refs. 5 and 6. We describe the outline of the simulation in this article. The RIE simulation consists of plasma, sheath,

![](./images/812270245568839683_5.jpg)

FIG. 3. Reaction model of SiO₂ etching. CF₂ generates a C-F polymer layer on SiO₂ film and an active layer in the SiO₂ film. The active layer is etched by ion-enhanced etching with C₄F₆⁺.

and surface reaction simulations. When the process conditions are input to the plasma simulation, plasma parameters, such as the densities of ions and radicals and $V_{\text{dc}}$ generated on the wafer, are calculated by the plasma simulation.⁵,⁶ The fluxes of ions and radicals are calculated from the products of the densities and the velocities at which they collide on the wafer. The radicals move at thermal energy of room temperature. The ions are accelerated within the sheath by $V_{\text{dc}}$. The etching profile will be simulated on the basis of these plasma parameters.

Next, we describe the surface reaction simulation. Figure 3 shows the surface reaction model. We adopted the ion-enhanced reaction reported by Tatsumi *et al.* as the surface reaction model.¹ In this reaction model, there are two layers, namely, a reactive ion layer and a C-F polymer layer. The etching reaction occurs in the reactive ion layer, and the C-F polymer layer consists of fluorocarbons on the reactive ion layer. Ion energy propagates through the C-F polymer layer. The propagation rate $E_{\text{rt}}$ of ion energy is approximated by the following equation when $E_{\text{rt}}$ is set to 1.0 without the C-F polymer layer¹,¹⁴

$$
E_{\text{rt}} = \exp(-A * T_h), \tag{1}
$$

where $A$ is a constant dependent on the types of etched film and process gas used, and $T_h$ is the thickness of the C-F polymer layer.

In the simulation, we assumed that CF₂, C₄F₆⁺, and O mainly cause the deposition, ion-enhanced etching, and polymer etching, respectively, due to the higher deposition rate of CF₂ and the higher density of C₄F₆⁺. As shown in Fig. 3, the surface reaction is modeled as follows:

(1) the adherence of CF₂ to the SiO₂ surface causes the simultaneous formation of the C-F polymer layer and reactive layer in an oxide film;

(2) O reacts with the C-F polymer layer and removes carbon from the polymer; and

(3) C₄F₆⁺ ion loses motion energy in proportion to the thickness of the C-F polymer layer, and etches SiO₂ film in the reactive layer.

The deposition rate (DR) is calculated from the fluxes of CF₂ and O using

$$
\text{DR} = \alpha_1 * \Gamma_{r\text{CF}_2} - \alpha_2 * \Gamma_{r\text{O}}, \tag{2}
$$

where $\Gamma_{r\text{CF}_2}$ and $\Gamma_{r\text{O}}$ are the radical fluxes of CF₂ and O, and $\alpha_1$ and $\alpha_2$ are the reaction rates of CF₂ and O, respectively.

The etching rate (ER) is calculated by

$$
\text{ER} = \beta(E_{\text{rt}} * E, \Gamma_{R\text{CF}2}/\Gamma_{i\text{C}_4\text{F}_6}) * \Gamma_{i\text{C}_4\text{F}_6}, \tag{3}
$$

where $\Gamma_{i\text{C}_4\text{F}_6}$ and $E$ are the ion flux and the motion energy of C₄F₆⁺, respectively, $\beta$ is a reaction constant and a function of $E_{\text{rt}}*E$, and $\Gamma_{R\text{CF}2}/\Gamma_{i\text{C}_4\text{F}_6}$.

In the SiO₂ etching process, CF₂ generates a polymer deposition on the photoresist surface, and the O₂⁺ bombardment causes the ion-enhanced etching of the photoresist. Therefore, we applied the same simulation model as oxide etching for calculation of the photoresist profile. In the photoresist model, the reaction constants were changed so that they were suitable for the photoresist etching.

![](./images/812270245568839683_6.jpg)

FIG. 4. Simulated results of SiO₂ etching: (middle) simulated and experimental results under the baseline conditions; (right) results under the condition of increasing O₂ gas flow rate; and (left) results under the condition of increasing C₅F₈.

The simulated results corresponding to the actual etching profile are shown in Fig. 4. In the central figure, the photoresist taper shape, the bowing profile below the photoresist, and the taper shape of the bottom are reproduced. The right figure is the simulated result in the case of adding 3 sccm C₅F₈ to the baseline conditions, and the left figure is the simulated result in the case of adding 2.5 sccm O₂. In the right figure, etching stopped due to an increase in the thickness of the C-F polymer layer. In the left figure, bowing

under the photoresist became greater than in the central fig- ure since the removal of the polymer by O radicals was en- hanced. We confirmed that these simulated results are in good agreement with the experimental results.

## B. Sputtering simulation model
We used the simple LTS equipment in which only dc power is supplied to the target, as described in Sec. II. In the sputtering process using this equipment, Ti metal is used as the target and TiN is generated by the reaction between the sputtered Ti and N on the target surface (reactive magnetron sputtering). $^{15,16}$ The TiN on the target surface is bombarded by positive ions such as $Ar^{+}$ and $N_{2}^{+}$ , and Ti atoms and N atoms are emitted from the TiN target surface. It is assumed that the Ti atoms emitted from the target change into TiN molecules by the reaction in the gas phase or on the wafer surface. As for the reaction in the gas phase, the mean free path between Ti and $N_{2}$ is estimated to be on the mm to cm order under the condition of a gas pressure of 0.5 Pa. It is considered that TiN is generated near the target surface due to the high reactivity between Ti and N and is transported to the wafer surface. In the equipment for TiN sputtering, the wafer is located at a distance $(L)$ of $300 ~mm$ from the target, and this distance $(L)$ is larger than the mean free path. In the case of the surface reaction on the wafer, Ti transport is calculated by changing the mass of TiN to that of Ti in Eqs.(4)-(7) as described below, and it is estimated that the move- ment of $Ti$ is almost the same as that of TiN. Therefore, in both cases of Ti reactions in the gas phase and on the wafer surface, we assumed that TiN was emitted from the target in the simulation.

The energy of emitted TiN is assumed to follow the Max-wellian distribution with an average energy $E_{0}$ of $10 eV.^{17}$  The sputtered TiN is emitted at the angular distribution fol-lowing a cosine law. $^{17}$ The velocity components $(c_{x}, c_{y}, c_{z})$  are given by
$$C_{z}=\left(-E_{0} \ln U / m_{\mathrm{TiN}}\right)^{1 / 2},\qquad(4)$$

$$C_{x}=C_{r} \cos \theta,\qquad(5)$$

$$C_{y}=C_{r} \cos \theta,\qquad(6)$$
 where $m_{TiN}$ is the mass of a TiN molecule and $\theta$ is $2 \pi U$ . U is an independent uniform random number and $E_{0}$ is the average kinetic energy of the sputtered atoms. The $Z$ axis corresponds to the axis perpendicular to the wafer. The com- ponent $C_{r}$ is given by
$$C_{z}=\left(-E_{0} \ln U / m_{\mathrm{TiN}}\right)^{1 / 2}.\qquad(7)$$

In an actual sputtering process, TiN particles are emitted in proportion to the amount of ions colliding with the target, and they are transported from the target to the wafer mainly colliding with $Ar$ atoms. In the simulation, the TiN particles are emitted in proportion to the distribution of the colliding ions calculated by the plasma simulation. The TiN particles and $Ar$ atoms are assumed to be rigid spheres, and the occur rence of collision between them is judged using the Monte Carlo method. The sticking coefficient of TiN to the surface of the oxide film is set to be 0.93 referring to another experi-ment and simulation of $Cu$ sputtering. $^{7}$

![](./images/812270245568839683_7.jpg)

FIG. 5. Simulated and experimental results of sputtering process.

Figure 5 shows the experimental and the simulation re- sults. In the actual process, most of the sputtered atoms ad- hered near the entrance of the contact hole and the bottom of the hole, and few sputtered atoms are deposited on the side- wall of the contact hole. These tendencies are reproduced in the simulated result, and this suggests that the simulation model is not incorrect. Moreover, the simulated results of the LTS indicate that the angular distribution of TiN perpendicu- lar to the wafer increases by $35.6 \%$ compared with the TiN emitted from the target, and the average energy of the sput- tered TiN transported from the target to the wafer decreases from 10.0 to $0.53 eV$ .

## C. CVD model
For the W-CVD process, some types of simulation mod- els have been reported. One is the simulation model com- posed of many chemical reactions generated in gas phase and on the wafer. $^{18,19}$ The simulation is applied mainly to calcu lating the deposition rates under the various process condi- tions. Another is simple Monte Carlo simulation reported by Akiyama et al. $^{8}$ The latter is used mainly to calculate the filling profile using the sticking coefficient of $W$ . We adopted the simple Monte Carlo simulation for calculating the W filling profile. In this method, three parameters, namely, the sticking coefficient $\alpha$ , Knudsen number $K_{n}$ , and aspect ratio $A_{s}$ , are used to calculate the CVD profile. $A_{s}$ is the ratio of hole depth to the diameter of the opening, and is determined from the contact hole profile. The Knudsen number $K_{n}$ is determined using

$$
K_{n}=\frac{\lambda}{W}, \tag{8}
$$

where $\lambda$ is the mean free path, $W$ is the opening diameter of the contact hole, and $L$ is the depth of the contact hole. $K_{n}$ is 28.5 in the case where $W$ is $0.13\ \mu$m and the gas pressure is 5320 Pa.

The sticking coefficients of W to TiN, W, and $\mathrm{SiO}_{2}$ are necessary for the W-CVD simulation. In the case where W is deposited on the $\mathrm{SiO}_{2}$ film due to insufficient TiN deposition, as shown in Sec. V B, the sticking coefficient of $\mathrm{SiO}_{2}$ is used. We confirmed experimentally that the thickness of W film on TiN is proportional to the process time. On the basis of this result, the sticking coefficient of W to the TiN surface was assumed to be the same as the sticking coefficient of W. The sticking coefficients of W to the surfaces of TiN and W were determined so that the simulated profile is the same as the filling profile in the experiment. In this experiment, the sticking coefficients of W to the surfaces of TiN and W were estimated to be $2.5\times 10^{-3}$. Akiyama *et al.*$^{8}$ reported that the sticking coefficient of W is on the order of $10^{-3}$. This suggests that the value of $2.5\times 10^{-3}$ is appropriate for the sticking coefficient of W.

Next, the sticking coefficient of W to the $\mathrm{SiO}_{2}$ surface was estimated as follows. We investigated the relationship between the thickness of W film and the process time by experiment. The W film began to deposit on $\mathrm{SiO}_{2}$ after 40 s, and it was deposited at the same rate as in the case of the underlying TiN film. The onset time of 40 s is defined as the incubation time (or induction time).$^{20,21}$ It is considered that the much smaller sticking coefficient of W to the $\mathrm{SiO}_{2}$ surface than that of W to the TiN surface causes the incubation time.

It takes 40 s for the radicals that are to be deposited to collide with the $\mathrm{SiO}_{2}$ surface and one layer of W is deposited on the $\mathrm{SiO}_{2}$. During this process, the number of radicals entering the $\mathrm{SiO}_{2}$ surface per area and time is calculated by

$$
n_{r}=\frac{1}{4}nv, \tag{9}
$$

where $n$ is the density of $\mathrm{WF}_{6}$, and $v$ is the average velocity of the radical. The radical density is assumed to be the same as the density of $\mathrm{WF}_{6}$ because, at a high temperature, $\mathrm{WF}_{6}$ is decomposed into the radicals to be depositted. The number of W atoms ($n_{u}$) was calculated from the diameter of the W atom in the case of one-layer deposition. The diameter of the W atom is assumed to be $2.82\ \mathring{\mathrm{A}}.^{22}$ The sticking coefficient of W to the $\mathrm{SiO}_{2}$ surface was estimated to be about $10^{-8}$ by dividing Nu by $n_{r}$. The sticking coefficients are correlated to the chemical reactions in the W-CVD process as follows. In the actual process of W-CVD, $\mathrm{WF}_{6}$ is dissociated to $\mathrm{WF}_{5}$ and $\mathrm{WF}_{4}$ in the gas phase.$^{18,19}$ $\mathrm{WF}_{6}$, $\mathrm{WF}_{5}$, and $\mathrm{WF}_{4}$ are absorbed on the surfaces of TiN, W, and $\mathrm{SiO}_{2},^{18,19}$ and are reduced at the same reaction rate in every position. Therefore, it is considered that the sticking coefficients represent the total absorption coefficients of $\mathrm{WF}_{6}$, $\mathrm{WF}_{5}$, and $\mathrm{WF}_{4}$ to the surfaces of TiN, W, and $\mathrm{SiO}_{2}$.

![](./images/812270245568839683_8.jpg)

FIG. 6. Simulated and experimental results of CVD process.

In the actual process, the radicals for deposition are generated by heating and move thermally in the chamber. In the simulation, it is assumed that the particles for deposition move thermally corresponding to the wafer temperature $415\ ^{\circ}\text{C}$. Figure 6 shows the scanning electron microscope (SEM) image of W deposition on the underlying TiN film using the sticking coefficients of W to the surfaces of TiN and W. In this experiment, we used the evaluated samples with $0.18\ \mu$m diameters of the hole tops and $0.75\ \mu$m depths of the holes. The filling profile in the simulation is in good agreement with that in the experiment.

### D. Simulation parameters

For simulations of each of RIE, sputtering, and CVD, the calibrated parameters based on the experimental results are summarized in Table I. In the RIE simulation, $\alpha_{1}$ of Eq. (2) was determined using data from Ref. 23 and the experimental results. Next, $\alpha_{2}$ in Eq. (2) was fixed by the dependence of the $\mathrm{O}_{2}$ flow rate on the etching profile. The amount of $\mathrm{SiO}_{2}$ etched by one ion (etching yield) was also determined using date from Ref. 24 and the experimental results. Furthermore, in order to correlate the etching time in the actual process to the etching time in the simulation, the etching rate in the simulation was calibrated. The other parameters for the fluxes of $\mathrm{CF}_{2}$, O, and $\mathrm{C}_{4}\mathrm{F}_{6}^{+}$ and the ion incidence energy were calculated by the plasma simulation. The constant of $A$ in Eq. (1) was determined using data from Ref. 14.

In the sputtering simulation, the sticking coefficient of TiN to the $\mathrm{SiO}_{2}$ surface was set to be 0.93 referring to the results of the previous experiment. Similarly to the RIE simulation, the deposition rate in the simulation was calibrated in order to correlate the sputtering time in the actual process to the sputtering time in the simulation. In the W-CVD, the sticking coefficients of W to the surfaces of TiN, W, and $\mathrm{SiO}_{2}$ and the deposition rate were calibrated on the basis of the experimental results.

The applicabilities of these calibrated parameters to other processes are summarized in Table I. $\bigcirc$ shows that the calibrated parameter is applicable to the other processes. $\bigtriangleup$ denotes that the calibrated parameter is partially applicable to other processes or the parameter can be easily calibrated by the experimental result. $\times$ indicates that the parameter must be calibrated when applying it to other processes. In RIE and

<table><caption>Table I. Calibrated simulation parameters and their applicabilities to other processes: ($\bigcirc$) shows that the calibrated parameter is applicable to other processes, ($\bigtriangleup$) denotes that the calibrated parameter is partially applicable to other processes; ($\times$) indicates that the parameter must be calibrated when applying it to other processes.</caption>
<thead>
<tr>
<th>Simulation</th>
<th>Calibrated parameter</th>
<th>Applicability</th>
</tr>
</thead>
<tbody>
<tr>
<td>RIE simulation</td>
<td>Deposition rate of CF₂: $\alpha_1$</td>
<td>$\bigcirc$</td>
</tr>
<tr>
<td></td>
<td>Reaction rate of O: $\alpha_2$</td>
<td>$\bigcirc$</td>
</tr>
<tr>
<td></td>
<td>Etching yield of ion</td>
<td>$\bigcirc$</td>
</tr>
<tr>
<td></td>
<td>Etching rate</td>
<td>$\bigtriangleup$</td>
</tr>
<tr>
<td>TiN sputtering
simulation</td>
<td>Sticking coefficient of TiN: 0.93</td>
<td>$\bigcirc$</td>
</tr>
<tr>
<td></td>
<td>Deposition rate of TiN</td>
<td>$\bigtriangleup$</td>
</tr>
<tr>
<td>W–CVD
simulation</td>
<td>Sticking coefficient of W to TiN and W surfaces: $2.5{\times}10^{-3}$</td>
<td>$\times$</td>
</tr>
<tr>
<td></td>
<td>Sticking coefficient of W to SiO₂ surface: $10^{-8}$</td>
<td>$\times$</td>
</tr>
<tr>
<td></td>
<td>Deposition rate of W</td>
<td>$\bigtriangleup$</td>
</tr>
</tbody>
</table>

sputtering simulations, the change of the profile with process change can be predicted using the parameters calculated by the plasma simulation. On the other hand, in CVD simulation, since the deposition profile is determined by the sticking coefficient, a sticking coefficient suitable for other processes must be investigated experimentally.

## IV. SIMULATED RESULTS

Figure 7 shows the results of the contact formation simulation obtained by the sequential calculations of RIE, TiN sputter, and W–CVD. Each simulation is calculated under the baseline conditions in the case of SiO₂ of $1.7\ \mu\text{m}$ thickness. In the sputter simulation, most of the sputtered TiN is considered to be deposited on the wafer surface and the upper part of the contact hole. On the sidewall from the middle of the contact hole to the bottom, the sputtered TiN is deposited separately.

In the CVD process, W is deposited on the TiN faster than on the SiO₂ due to the difference in the sticking coefficients.

![](./images/812270245568839683_9.jpg)

FIG. 7. Simulated results of contact formation process. Etching, sputtering, and CVD were calculated sequentially.

The W film on TiN is thicker than that on SiO₂. In the sputter process, most of the TiN is deposited on the top surface of the wafer and the upper part of the contact hole. W is also deposited on the upper part of the contact hole, and the contact hole is closed at the top. Consequently, little W is deposited on the sidewall of the contact hole.

On the right-hand side of Fig. 7, the SEM image after the contact formation is shown; it corresponds to the simulated result. In the SEM image, W is deposited mainly on the upper and bottom parts of the hole. The deposition in the middle of the hole is less than that in the upper and bottom parts. This tendency is observed in both the simulation and the SEM image, suggesting that the simulation models of contact formation have high accuracy. Even if a void exists inside the W contact, as shown in Fig. 7, the contact resistance does not increase markedly, and a contact plug with a void is also used in the mass product. On the other hand, when W disconnection occurs between the top and bottom of the contact, the contact resistance increases markedly, as discussed in Sec. V B. It is more important to prevent the disconnection in an actual product.

To evaluate the accuracy of the simulation, we compared the thicknesses of the deposited tungsten layer in the simulation and experiment. The thicknesses were obtained at three points corresponding to $0.25\ \mu\text{m}$ below the hole top (upper point), $0.25\ \mu\text{m}$ above the bottom (lower point), and the hole bottom, as shown in Fig. 4. The thicknesses obtained in the simulation are 0.049, 0.031, and $0.025\ \mu\text{m}$ from the upper point to the bottom, while those in the experiment are 0.050, 0.33, and $0.026\ \mu\text{m}$ from the upper point to the bottom. It was confirmed that the accuracy of the simulated results was within $\pm 6\%$ of the experimental results.

## V. DEPENDENCE OF CONTACT PROFILE ON CONTACT DEPTH

### A. Depth dependence of RIE

The change of the etching profile relative to etching time was investigated in the case of the SiO₂ film of $3.0\ \mu\text{m}$ thickness, by topography simulation. The result is shown in

![](./images/812270245568839683_10.jpg)

FIG. 8. Dependence of etching profiles on etching depth. Simulated and experimental results at $T$=210 and 380 s.

Fig. 8. At $T$=25 s, SiO$_2$ film is etched at almost the same angle as the photoresist taper angle. On the other hand, bowing begins to occur in the lower part of the photoresist at a depth of more than $0.5\ \mu$m at $T$=75 s. However, there is a flat portion at the bottom of the etching hole after the diameter of the bottom decreases at $T$=210 s.

The etch depth is $1.22\ \mu$m at $T$=210 s in the simulation and $1.13\ \mu$m in the experiment. Although the bottom diameter decreases, the flat part remains at the etching hole bottom. Furthermore, the flat portion at the hole bottom begins to disappear at $T$=250 s in the simulation. The etched depth is $2.12\ \mu$m at $T$=380 s in the simulation and $2.05\ \mu$m in the experiment. The bottom diameter and the tendency for the bottom diameter to decrease are also in good agreement with the experimental results.

Next, we estimated the diameter of the etched bottom in the simulation using actual samples of the SiN/SiO$_2$/photoresist film on Si. The bottom diameter is an important parameter for determining contact resistance. The etching profile was calculated under the etching condition of 120% over etching time. The diameter of the bottom of the etched hole decreases as the SiO$_2$ film becomes thicker. Figure 9 shows the results of the bottom diameters. Two points of $\blacklozenge$ in Fig. 9 are the experimental results for the $2.8\ \mu$m thick SiO$_2$ film. In Fig. 9, the simulated results and the experimental results include errors of $\pm$5% in measuring the bottom diameter of the contact hole from both results. The experimental results are in agreement with the simulated results. This suggests that the etching profiles and the quantitative evaluations of the hole depth and bottom diameter can be predicted by the simulations.

## B. Dependence of W-CVD filling profile on hole depth

We simulated the filling profiles of TiN sputtering and W-CVD sequentially using the etching profile calculated in Sec. V A. The relationship between hole depth and filling profile was calculated under the baseline conditions of W-CVD. Figure 10 shows the simulated results of W-CVD for 2.0, 2.5, and $3.0\ \mu$m thick SiO$_2$ films.

![](./images/812270245568839683_11.jpg)

FIG. 9. Dependence of the bottom diameter on the etching time.

In all cases, the upper part of the contact hole was closed before the inside hole was buried completely, and a large void was generated. A magnification of the bottom profile is shown on the right-hand side of the simulated results. W deposition is observed at the bottom of the contact hole, and the W plug contacts the surface of the SiN. On the other hand, deposition on the sidewall in the middle part of the

![](./images/812270245568839683_12.jpg)

FIG. 10. Dependence of the CVD profiles on contact hole depths. Magnifications of the CVD profiles in contact bottoms and at the sides are also shown on the right.

![](./images/812270245568839683_13.jpg)

FIG. 11. Dependence of the connection ratio on the side wall on the etching depth.

contact hole decreases as the thickness of $SiO_2$ increases. In particular, disconnection occurs on the sidewall when the $SiO_2$ thickness is more than $2.5\ \mu$m.

We investigated the connection of the W film from the upper part to the bottom part. The connection is evaluated using the connection ratio $R_c$ determined using

$$
R_c = \frac{M_c}{M_t} \times 100\ \%, \tag{10}
$$

where $M_t$ is the total mesh number of vertical-direction meshes from the top of the contact hole to the bottom and $M_c$ is the number of vertical meshes filled with W particles. $R_c$ $=100\%$ and $R_c < 100\%$ indicated qualitatively that W was connected from the top of the contact hole to the bottom, respectively.

Figure 11 shows the results of $R_c$. In Fig. 11, since the Monte Carlo method was used, disconnection ratios are different between the right-hand side and left-hand side walls in the contact hole. The error bars corresponding to the different disconnection ratios are shown, and the average disconnection ratios are plotted. The average disconnection of $100\%$ is plotted at a bottom diameter of less than $2.0\ \mu$m since the disconnection ratios between the right-hand side and left-hand side walls are the same value of $100\%$. W is connected from the top to the bottom with $100\%$ $R_c$ at a $SiO_2$ film thickness of less than $2.0\ \mu$m. On the other hand, $R_c$ decreases at a $SiO_2$ film thickness of more than $2.5\ \mu$m, and disconnection occurs. This suggests that contact resistance increases markedly at a $SiO_2$ film thickness of more than $2.5\ \mu$m. The contact process under the baseline conditions is limited to the region of less than $2.0\ \mu$m thickness of $SiO_2$ film, according to the simulated results.

## VI. CONCLUSION

We applied sequential simulations of RIE, TiN sputtering, and W-CVD to contact formation. The Monte Carlo method using a particle model is adopted in each topography simulation. RIE and sputtering simulations include apparatus simulation and surface reaction simulation, and the profile changes due to the process condition changes can be calculated. Each topography simulation of hole etching, sputtering of the barrier metal, and W-CVD was calibrated using experimental results, and then they were combined in order to calculate these processes sequentially. We investigated the relationship between contact depth and etching profile using RIE simulation, and evaluated the filling profile using contact formation simulation. In RIE simulation, it was confirmed that simulated results agree with experimental results for $SiO_2$ thicknesses between 1.7 and $3.0\ \mu$m. In contact formation, disconnection occurs at a $SiO_2$ film thickness of more than $2.5\ \mu$m, and contact resistance increases markedly. It was found that contact formation under the baseline conditions is limited to the region of less than $2.0\ \mu$m thick $SiO_2$ film, according to the simulated results. Furthermore, in all the simulations of RIE, sputtering and W-CVD for contact formation was adopted for particle models using the Monte Carlo method, and they are applicable to the newest process in which the diameter of the contact hole is smaller.

## ACKNOWLEDGMENTS

The authors thank Dr. Y. Kataoka, Dr. M. Kano, and Dr. O. Yamazaki for useful comments and discussions.

$^{1}$T. Tatsumi, M. Matsui, M. Okigawa, and M. Sekine, J. Vac. Sci. Technol. B 18, 1897 (2000).
$^{2}$K. Yonekura, H. Matsuno, N. Fujiwara, and H. Miyatake, Proceedings Symposium on Dry Process, Tokyo 2001, p. 285.
$^{3}$S. Iwabuchi et al., Proceedings VLSI Symposium 1986, p. 55.
$^{4}$S. Mehta, Proceedings VLSI Multi-level Interconnection Conference, 1986, p. 419.
$^{5}$S. Takagi, K. Iyanagi, S. Onoue, T. Shinmura, and M. Fujino, Jpn. J. Appl. Phys., Part 1 41, 3974 (2002).
$^{6}$S. Takagi et al., Plasma Sources Sci. Technol. 12, S64 (2003).
$^{7}$O. Yamazaki, K. Iyanagi, S. Takagi, and K. Nanbu, Jpn. J. Appl. Phys., Part 1 41, 1230 (2002).
$^{8}$Y. Akiyama, S. Matsumur, and N. Imaishi, Jpn. J. Appl. Phys., Part 1 34, 6171 (1995).
$^{9}$N. Motegi, Y. Kashimoto, K. Nagatani, S. Takahashi, T. Kondo, Y. Miazusawa, and I. Nakayama, J. Vac. Sci. Technol. B 13, 1906 (1995).
$^{10}$T. E. Clark, M. Chang, and C. Leung, J. Vac. Sci. Technol. B 9, 1478 (1991).
$^{11}$D. Zhang and M. J. Kushner, J. Vac. Sci. Technol. A 19, 524 (2001).
$^{12}$B. Kim, Y. Akiyama, N. Imaishi, and H. Park, Jpn. J. Appl. Phys., Part 1 38, 2881 (1999).
$^{13}$I. Ulaciaf and J. P. Mcvittlie, J. Appl. Phys. 65, 1484 (1989).
$^{14}$T. Tatsumi, T. Matsui, M. Okigawa, and M. Sekine, J. Vac. Sci. Technol. A 17, 1562 (1999).
$^{15}$M. Suzuki, T. Tanaka, and K. Kawabata, J. Vac. Sci. Technol. A 16, 3142 (1998).
$^{16}$S. Berg, T. Larsson, C. Nender, and H. Blom, J. Appl. Phys. 63, 887 (1988).
$^{17}$V. V. Serikov and K. Nanbu, J. Vac. Sci. Technol. A 14, 3108 (1996).
$^{18}$R. Arora and R. Pollard, J. Electrochem. Soc. 138, 1523 (1991).
$^{19}$K. J. Kuijlaars, C. R. Kleijn, and H. E. A. van den Akker, Thin Solid Films 270, 455 (1995).
$^{20}$H. Itoh, N. Kaji, T. Watanabe, and H. Okano, Jpn. J. Appl. Phys., Part 1 30, 1525 (1991).
$^{21}$K. Kim, J. H. Sone, S. O. Kim, J. S. Park, and H. J. Kim, J. Vac. Sci. Technol. A 14, 19 (1996).
$^{22}$D. E. Gray, *American Institute of Physics Handbook* (McGraw-Hill, New York, 1989).
$^{23}$K. Miyata, M. Hori, and T. Goto, Jpn. J. Appl. Phys., Part 1 36, 5340 (1997).
$^{24}$T. Shibano, N. Fujiwara, M. Hirayama, H. Nagata, and K. Demizu, Appl. Phys. Lett. 63, 2336 (1993).