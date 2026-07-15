ORIGINAL PAPER

# A computational study on the microstructural evolution in near-surface copper grain boundary structures due to femtosecond laser processing

Mohammad Rezaul Karim¹ · Micheal Kattoura² · Seetha R. Mannava² ·
Vijay K. Vasudevan² · Arif S. Malik¹ · Dong Qian¹

Received: 30 November 2016 / Accepted: 14 July 2017
© Springer-Verlag GmbH Germany 2017

## Abstract
A multiscale simulation method is established to study the microstructural responses of near-surface grain boundary structures of copper subjected to ultrashort femtosecond laser pulse. By integrating a two-temperature model with molecular dynamics, the presented approach allows for incorporation of both laser processing parameters and microstructures, enabling systematic simulation studies on the process-properties link. Following a brief introduction of the simulation methodology, a detailed modeling study on the ultrashort laser-material interaction is presented. In particular, we highlight the effects of laser process parameters on the near-surface response and corresponding phase change, formation of voids and their growth, and mechanism of dislocation nucleating and propagating from grain boundary.

**Keywords** Femtosecond laser · Two-temperature model · Multiscale simulation · Molecular dynamics · Grain boundary

## 1 Introduction
With the recent advances in laser-based manufacturing, there is a continuing interest in exploring fundamental mechanisms of laser-material interaction to improve mechanical performance of diverse engineering applications. The unique spatial and temporal profiles of lasers provide a wide range of capabilities for material processing and device fabrication. As an example, ultrashort pulsed lasers have been employed to meet the demands of applications such as drilling, ablation, volume structuring, etc. In those applications, the pulse is applied for a very short time period, e.g., a few hundred femtoseconds (fs) to several picosecond (ps), which contributes to unique thermomechanical responses compared to conventional continuous wave laser or nanosecond pulse laser.

When laser is applied to the surface of a metal, energy is first absorbed by the conduction band electrons and quickly equilibrated among electrons. A non-equilibrium condition is established with electrons and phonons having different temperatures. Consequently, thermal energy is transferred from the electrons to the lattice. The transferred energy is controlled by electron–phonon coupling, and there is a heat flow from the surface to the bulk of the material. Depending on the specific spatial and temporal profiles, ultrafast laser heating on materials may involve irradiation, ablation, evaporation, phase transformation, etc. A number of experimental and numerical investigations have been made on ultrafast laser processed materials. For example, computational studies of short pulse laser melting of metals such as nickel (Ni) and gold (Au) were presented in Refs. [1–4]. Homogeneous and heterogeneous melting mechanisms upon laser heating were discussed with a combined atomistic-continuum model, and it was shown that melting started from the grain boundaries in nanocrystalline materials. Effects of grain boundary on laser melting of nanocrystalline Au was studied in Lin et al. [5] using molecular dynamics. Karim et al. [6] conducted atomistic simulation of ultrashort laser pulse on target materials under the condition of transparent overlay. It was concluded that a transparent overlay on the target material helped to increase both depth of melting and resolidification time. Atomic level simulation of 1 ps laser pulse [7] was carried out on bulk Ni target for exploring interactions

Correspondence: Dong Qian
dong.qian@utdallas.edu

1 Department of Mechanical Engineering, University of Texas at Dallas, 800 West Campbell Road, Richardson, TX 75080, USA
2 Department of Mechanical and Materials Engineering, University of Cincinnati, Cincinnati, OH 45221, USA

![](./images/813114049398046721_1.jpg)

Fig. 2 Schematic of the simulation set up for the TTM-MD model showing TTM grid, coupling TTM-MD domain and non-reflective boundary layer

boundary condition is imposed at the interface when TTM-MD is transitioning into TTM continuum simulation. Details will be described next. The top surface along the Y direction is kept free while a periodic boundary condition is applied along both the X and Z directions.

When laser pulse irradiates on the top surface in Fig. 2, it generates a strong stress wave. When stress wave reaches the interface of TTM-MD/TTM continuum, proper interface condition must be imposed to avoid spurious wave reflection. The corresponding computational implementation is generally referred to as "non-reflective boundary condition" in the context of multiscale simulation [21]. In this paper, a simple yet effective approach is adopted from [22,23]. In this implementation, a terminating force is applied along Y direction at interface. The terminating force is calculated by the following equation

$$
F_{s}=-\rho v_{y} c \frac{A}{N} \tag{9}
$$

where $\rho$ is the density of TTM-MD layer at the interface, $v_{y}$ is the average velocity of TTM-MD layer at the interface, $c$ is the speed of the stress wave along Y direction, $A$ is the cross sectional area and $N$ is the number of atoms in the TTM-MD layer at the interface. The speed of the stress wave is evaluated based on the stress wave profiles obtained from simulation. Since the location of the wave front can be obtained from such a profile at different time, the speed can then be calculated by dividing the distance that the wave front travelled by the time interval.

The system is initially maintained at a temperature of 300 K. Laser is then applied from the top Y surface as a heat source by introducing a Gaussian profile [10]

$$
S(Y, t)=C_{0} \exp \left[-\frac{\left(Y_{0}-Y\right)}{h}-2.77\left(\frac{t-2 \tau}{\tau}\right)^{2}\right] \tag{10}
$$

where $C_{0}$ is the absorbed laser power density and calculated by $C_{0}=\frac{I_{0}}{h} . I_{0}$ is the absorbed laser peak intensity and $h$ is the laser penetration depth. $Y_{0}$ denotes the top irradiated surface and $\tau$ is pulse duration, given as the full width of laser pulse at the half maximum intensity (FWHM). In the present case, a 200 fs laser pulse duration is employed and the laser penetration depth of 12 nm is used. The use of 200 fs pulse width is representative of the fs laser used in the manufacturing process. The laser penetration depth $h$ is derived from $h=\frac{1}{\alpha}$, where $\alpha$ is the absorption coefficient [24]. The absorption coefficient for copper is $8.36 \times 10^{5} \mathrm{~cm}^{-1}$ [24]. Laser intensity values of 597,797 and $996 \mathrm{GW} / \mathrm{cm}^{2}$ are applied in this study, representing the low, medium and high intensity cases. A linear temperature dependence of electron heat capacity [25] is employed in this model, i.e., $C_{e}=\gamma T_{e}$, where $\gamma=96.8 \mathrm{Jm}^{-3} \mathrm{~K}^{-2}$ is the electron heat capacity constant. Other parameters used in this model include electron-phonon coupling constant, $G=1 \times 10^{17} \mathrm{Wm}^{-3} \mathrm{~K}^{-1}$ [26]. Electron heat conductivity is dependent on the lattice and electronic temperatures. The expression for thermal conductivity can be written as [26]

$$
K_{e}=K_{0} \frac{\left(\theta_{e}^{2}+0.16\right)^{\frac{5}{4}}\left(\theta_{e}^{2}+0.44\right) \theta_{e}}{\left(\theta_{e}^{2}+0.092\right)^{\frac{1}{2}}\left(\theta_{e}^{2}+\beta \theta_{l}\right)} \tag{11}
$$

where $\theta_{e}=\frac{T_{e}}{T_{F}}, \theta_{l}=\frac{T_{l}}{T_{F}}$ and $T_{F}=8.12 \times 10^{4} \mathrm{~K}$ is the Fermi temperature of copper. The other two parameters have been set to $K_{0}=377 \mathrm{JK}^{-1} \mathrm{~m}^{-1} \mathrm{~s}^{-1}$ and $\beta=0.139$ [26].

## 5 Results and discussion

Before the details of the results are presented and discussed, we first provide an overall picture on the general observations from the simulation, as shown in Fig. 3. Laser pulse is applied from the top and initially the electrons absorb the energy. The electron-phonon coupling leads to transfer of energy from hot electrons to lattices within 30-40 ps. The affected surface atoms start to evaporate rapidly, which leads to high compressive stress. As the time goes on, absorbed energy penetrates deep into the target materials in which the temperature may exceed the equilibrium melting temperature of copper. As a result of this, melting front propagates from the surface. When surface temperature drops below equi-

![](./images/813114049398046721_2.jpg)

Fig. 3 A general picture of femtosecond laser-processed material responses at 70 ps, with 12 nm penetration depth and laser pulse intensity of 797 GW/cm² (atoms are colored with their centro-symmetry parameter, the plot on the lower left employs a different color scheme to indicate the phase change based on the degrees of crystallinity from the dislocation extraction algorithm analysis [27]. Light grey and dark grey colors represent melting zone and liquid-solid zone, respectively)

librium melting temperature, resolidification starts and part of the melting zone turns into heterogeneous solid-liquid phase. Zones of melting and solid-liquid phase are shown in Fig. 3 and they are colored based on the degrees of crystallinity. Rapid increase of temperature also builds up high pressure within the irradiated surface of the target materials. The compressive stress wave travels through the material, and a tensile stress wave is formed as a rarefaction wave following the compressive stress wave. The non-reflective boundary condition applied at the bottom of the target materials is confirmed by the observations that both tensile and compressive stress wave propagate without any visible reflections from the bottom side. As wave travels, dislocations nucleate and propagate under melted subsurface and from grain boundary, interact with each other within the target materials. In melted zone we observe void nucleation, growth and coalescence phenomena. The detailed results will be discussed in the following sections.

### 5.1 Thermal responses

At the beginning of the TTM-MD process, deposited laser energy leads to a rise in the electronic temperature at the front surface. The electronic thermal energy quickly redistributes towards the rear surface of the material by electron-phonon coupling and heat conduction. These two mechanisms are manifested in Fig. 4. Figure 4a shows the spatial-temporal profile of the lattice temperature for $\sum 13$ (510) grain boundary structure subjected to laser intensity of 996 GW/cm². At the top layer, the instantaneous electronic temperature at t = 0.5 ps is 35,414 K. Due to electron-phonon coupling, lattice temperature starts to rise quickly. A 4255 K increase in the lattice temperature is observed for the first 35 ps at the top layer. Figure 4b shows the history of the electronic and lattice temperature at the top layer.

The near surface response to the laser is a mixture of evaporation and melting. First, some atoms in the surface quickly vaporize and evaporate, owing to the overflow of high deposition energy. We did not observe evaporation until 18 ps. Lattice temperature at the top layer reached 4976 K during that time, which is enough to accelerate evaporation at 18 ps. Random distribution of atoms in Fig. 5 shows the vaporization zone. The whole vaporization zone acts like gas. Evaporation and vaporization mechanisms are observed right after the peak pressure zone at around 18 ps. Figure 6 plots the number of evaporated atoms per unit surface area as a function of time. We define $\Omega_N$ as number of evaporated atoms per unit surface area. It shows high evaporation rate between $t = 18$ and 42 ps. After $t = 42$ ps, the evaporation stabilizes and a maximum amount of evaporation is reached.

Energy transfer from excited electrons to atoms leads to superheating of the top surface. By 15 ps, the top surface layer of 42 nm thickness is superheated where temperature is 40% above the equilibrium melting temperature. The superheated zone undergoes rapid homogeneous melting and propagates by the collapsing of crystal lattice within few picoseconds. The rapid homogeneous melting forms a melting front and moves deeper into the material. It reaches a maximum melting depth of 90 nm by the time of 70 ps. Meanwhile, some of the laser energy is consumed due to latent heat of melting, leading to a drop in temperature and a sharp temperature gradient is observed in Fig. 4a. The temperature of the solid-liquid interface falls below equilibrium melting temperature at 75 ps and melting turns into solidification stage. A cooling rate of $3.5 \times 10^{12}$ K/s is calculated in this simulation during dropdown of temperature.

### 5.2 Laser-induced pressure and void nucleation and growth

Rapid expansion of the material under laser pulse may lead to high pressure, which can also be examined from the simulation. The pressure is evaluated as the volume average of the volumetric component of the stress, i.e.,
$$
P = -\frac{(\sigma_{XX}+\sigma_{YY}+\sigma_{ZZ})}{3}
$$
. Pressure profile for 12 nm laser penetration depth and 996 GW/cm² absorbed intensity is presented in Fig. 7a. In this case, the maximum pressure

![](./images/813114049398046721_3.jpg)

![](./images/813114049398046721_4.jpg)

Fig. 4 a Spatial-temporal contour plot of lattice temperature for 12 nm penetration depth and 996 GW/cm² laser pulse intensity. b Time histories of the electronic and lattice temperature at the top layer of the grain boundary structure

![](./images/813114049398046721_5.jpg)

![](./images/813114049398046721_6.jpg)

Fig. 6 Pressure and number of evaporated atoms per unit surface area as a function of time for 12 nm penetration depth and 996 GW/cm² laser intensity

is 2.3 GPa. The peak pressure is observed to increase with laser intensity. For instance, maximum pressures are 1.6, 1.9 and 2.3 GPa for absorbed laser intensities of 597, 797 and 996 GW/cm² and 12 nm penetration depth respectively. A curve fit of the relation between the peak pressures and the corresponding intensity is shown in Fig. 7b. It follows a power relationship of $P \sim I_{0}^{0.704}$, where $P$ (GPa) is the peak pressure and $I_{0}$ (GW/cm²) is the absorbed intensity. Figure 7c shows the stress wave profile $(\sigma_{YY})$ along the depth direction at different time, in which the rarefaction tensile wave is observed to follow the propagating compressive wave front.

As the peak compressive pressure relaxes in Fig. 7c, materials are seen to expand with the generation of rarefaction tensile stress wave at the free surface. The tensile stresses are strong enough to induce multiple voids under melted subsurface where material expansion and rapid temperature increase make the melted subsurface region a place for substantial nucleation of multiple voids. At first, void nucleation occurs heterogeneously at sites of melted zone. We use the lattice constant of 3.615 Å as the minimum cutoff distance to identify individual void. If an atom has no neighbors within the cutoff distance then void is formed. Therefore, minimum volume of void is calculated as 0.047 nm³. A plot of number of voids per unit volume $(N_{V})$ and void volume fraction $(V_{V}$, defined as the ratio of volume of voids to the total volume)

![](./images/813114049398046721_7.jpg)

Fig. 7 a Pressure (GPa) versus time (ps) for 12 nm laser penetration depth and 996 GW/cm² absorbed intensity. b Peak pressure (GPa) versus intensity (GW/cm²). c Spatial profile of $\sigma_{\gamma\gamma}$ along the depth direction for laser intensity of 996 GW/cm² at $t = 33, 51, 66$ and 75 ps

![](./images/813114049398046721_8.jpg)

Fig. 8 Evolution of the total number of voids per unit volume and void volume fraction (volume of voids/total volume) during laser irradiation time. The insets show only the top part of the simulated system, down to a depth of 130 nm from the initial surface. It describes void nucleation, growth and coalescence at 12 nm laser depth and 996 GW/cm² absorbed intensity for $\sum 13$ (510) grain boundary structure. Atoms are colored with centro-symmetry parameter and only atoms responsible for forming voids are shown

is presented in Fig. 8. First, we observe a rapid increase of small voids under subsurface melted region between 0 and 30 ps; the time when rarefaction tensile wave starts to travel into the structure. We define this stage as void nucleation phase and a snapshot at 18 ps in shown in Fig. 8. Second, number of voids starts to decrease between 30 and 100 ps and the volume of voids increases steadily. This process is characterized by growth and coalescence of large voids and reduction of smaller number of voids. A snapshot at 60 ps showing void growth is presented in Fig. 8. Before coalescence, voids grow in size progressively and become spherical in shape. Eventually, two neighboring voids meet, merge into a large one and become ellipsoidal in shape. After 100 ps, we do not observe any new void nucleation and number of voids become stable. However, there is still a steady volume increase of voids, but the rate of volume increase is slower than the earlier rate. At the end of this stage, we measure 11 large voids, while others are in small spheroidal shape. The maximum diameter of the void is measured as 47.6 nm at 198 ps and a snapshot is shown in Fig. 8.

In details, void coalescence snapshot is shown in Fig. 9 corresponding to spatial profile of $\sigma_{\gamma\gamma}$ profile in Fig. 7c. At 33 ps we observe large number of spherical voids generated under melted subsurface heterogeneously. By 51 ps, voids are growing larger in volume and come closer. At 66 ps two nearest voids start merging into a single void of ellipsoidal shape, which is clearly visualized at 75 ps, where tensile rarefaction wave also reaches its maximum value. Finally, after coalescence, voids become larger and elliptical in shape. By the time when liquid melting front reaches the grain boundary region at 45 ps, a new void nucleation site is generated along grain boundary region. Multiple voids are found to nucleate at the grain boundary at 51 ps as shown in Fig. 9. We observe total 33 voids nucleated along grain boundary. Their nucleation, growth and coalescence also follow similar mechanism as discussed earlier. Our simulation shows void with maximum size of 35.7 nm in diameter is developed along grain boundary. In general, void nucleates at sites where local free energy exceeds the intragranular cohesive energy. The simulation results suggest that the misorientation [28] plays an important role in void nucleation. $\sum 13$ (510) grain boundary structure has a misorientation angle of $22.6^\circ$. High stresses can arise from misorientation sites into grain boundary structure which act to increase the local free energy. As such, there is a high chance for nucleation of voids along grain boundary structure. This conclusion is supported by the cohesive energy of $-3.54$ eV/atom in copper and a local free energy of $-3.23$ eV/atom obtained from simulation.

![](./images/813114049398046721_9.jpg)

Fig. 10 (Left) Dislocations including stacking fault from MD simulation and (right) network of dislocations at 198 ps for $597\ \text{GW/cm}^2$. Only part including dislocations under melted subsurface is shown here

![](./images/813114049398046721_10.jpg)

![](./images/813114049398046721_11.jpg)

Fig. 11 Dislocation densities of different dislocation families with respect to simulation time for laser intensity of $597\ \text{GW/cm}^2$. Only top part of the simulated system down to a depth of 150 nm below the initial surface is shown in the snapshots at 30 and 51 ps

profile verifies generation of Stair-rod and Hirth dislocations after reactions between Shockley partials dislocations. We observe another kind of dislocation named as Frank dislocation which is generated after 60 ps. We will explain those later.

It is observed that initially dislocations nucleate under irradiated melting zone. As the Burgers vectors of those dislocations are not a lattice vector, they form stacking fault leaving behind imperfect crystals. The boundary of the stacking fault separating disordered crystals from the perfect one

![](./images/813114049398046721_12.jpg)

![](./images/813114049398046721_13.jpg)

Fig. 12 Formation of perfect dislocation from Frank partial disloca- tion. a Snapshot is taken at 198 ps and 85 nm below the initial top surface, b dislocation segment corresponding to snapshot in a where green, aqua and navy blue color relates to Shockley, Frank and perfect dislocations, c Thompson tetrahedral notation representing reaction of Shockley and Frank partial dislocation

is the partial dislocation. One of the partial dislocations that nucleate under irradiated melting zone is Shockley partial dislocations and propagate along close packed {111} atomic slip plane. At 45 ps, pre-existing perfect dislocation disso- ciate into two Shockley partial dislocations; the one that generated earlier is called leading partial dislocations and following one is called trailing partial dislocations. As an example for our system, we observe a perfect dislocation of Burgers vector $\frac{1}{2}[101]$ splits into two Shockley partial dis locations with Burgers vector of $\frac{1}{6}[112]$ and $\frac{1}{6}[2 \overline{1} 1]$ along $(11 \overline{1})$ slip plane, i.e.,

$$
\left.
\begin{aligned}
\frac{1}{2}[101] & =\frac{1}{6}[112]+\frac{1}{6}[2 \overline{1} 1] \\
0.5 \mathrm{a}^{2} & >0.333 \mathrm{a}^{2}
\end{aligned}
\right\} \tag{12}
$$

The second set of Eq. (12) shows the application of Frank's rule for checking the favorability of the perfect dislocation dissociation. Here a is the lattice parameter and the two terms are proportional to the corresponding dislocation energies. It can be seen that perfect dislocation energy is greater than sum of Shockley partial dislocations. Therefore, the dissociation is energetically favorable. Location of Shockley dislocation generation is shown in Fig. 10, pointed by box 1. Both Shock- ley partial dislocations form $60^{\circ}$ angle between them and repels each other due to elastic interaction. After 60 ps, we observe that Shockley partials continue propagating by leav- ing behind perfect dislocation, explained in Fig. 11. These newly generated perfect dislocation forms a constriction and can glide on other planes. Figure 11 verifies increase of per- fect dislocation density after 60 ps. There is another kind of partial dislocation that is generated at the end of stacking fault boundary. This partial dislocation is known as Frank partial dislocation, which start to generate after 70 ps. Box2 in Fig. 10 shows Frank partial dislocation. A possible rea- son to form Frank partial is an insertion or removal of faulted{111} planes. Its Burgers vector is normal to the {111} faulted plane. Therefore, it cannot glide along {111} plane. Such dis- locations are called sessile. It is observed that one Shockley partial meet with Frank partial and forms perfect dislocation. A Shockley partial of Burgers vector $\frac{1}{6}[\overline{1} 2 \overline{1}]$ on $(\overline{1} \overline{1} \overline{1})$ inter acts with Frank partial of Burgers vector $\frac{1}{3}[\overline{1} \overline{1} \overline{1}]$ to form a perfect dislocation of Burgers vector $\frac{1}{2}[\overline{1} 0 \overline{1}]$ . In Thom son's notation, Frank partial $\delta D$ is normal to the $A B C$ plane as shown in Fig. 12. It reacts with Shockley partial $A \delta$ and form perfect dislocation of $A D$ . The favorability of the reac tion is explained by stacking fault energy. Frank dislocations consist of stacking fault and formation of perfect dislocations remove stacking fault. Therefore, energy of Frank dislocation is higher than newly generated perfect dislocations.

![](./images/813114049398046721_14.jpg)

![](./images/813114049398046721_15.jpg)

Fig. 14 Hirth partial dislocation formation. a Snapshots are taken at 198 ps and 169 nm below the initial top surface, b dislocation network where yellow and green denoting Hirth and Shockley partial dislocations, respectively, c Sketch of Hirth dislocation generation

plane. These two glided Shockley partials form Hirth par-
tial, $\frac{1}{3}[00\overline{1}]$. A schematic diagram is drawn in Fig. 14. From
Thompson tetrahedral notation, partial dislocation $A\delta$, along
$ABC$ plane interacts with other partial dislocation $B\gamma$ along
$ABD$ plane. The product is Hirth partial of $\frac{\gamma\delta}{BA}$. Following a
similar comparison of the dislocation energies, it is also con-
cluded that the reaction is energetically favorable by Frank’s
rule and the product is sessile.

$$
\left.
\begin{aligned}
\frac{1}{6}[\overline{1}2\overline{1}](11\overline{1}) + \frac{1}{6}[\overline{1}2\overline{1}](\overline{1}\overline{1}\overline{1}) &= \frac{1}{3}[00\overline{1}] \\
B\gamma + A\delta &= \frac{\gamma\delta}{BA} \\
0.333\mathrm{a}^2 &> 0.111\mathrm{a}^2
\end{aligned}
\right\} \tag{15}
$$

## 6 Summary

In summary, we have presented a computational study
on the microstructural responses of copper grain bound-
ary structure due to the application of femtosecond laser
pulse. The computational model is based on a multiscale
approach that integrates the two-temperature model with the
molecular dynamics. This model allows for incorporation of
mechanisms such as laser excitation, electronic heat conduc-
tion, electron–phonon coupling, and thermal energy transfer,
which are essential for studying the material responses sub-
jected to ultrashort femtosecond pulse lasers.

During the application of laser pulse, an exchange of
energy occurs between electrons and atoms: the electrons
provide almost instantaneous temperature rise in response to
the applied laser pulse, while it takes 30–40 ps for the lat-
tice to achieve close to thermally equilibrated temperature.
Laser-material interaction leads to rapid material evapora-
tion and introduces compressive stress waves propagating
into the materials. In the case of high laser intensity, melting
starts to develop from the top irradiated surface. Some of the
temperature losses take place due to latent heat of melting
and lead to resolidification.

Under the irradiated surface, voids and dislocation nucle-
ation points are identified. An important observation is that
voids are generated in the melting zone due to the rar-
efaction tensile wave. Some of the nucleated voids grow,
coalescence with neighboring ones and become larger in
volume. Furthermore, dislocation nucleation point acts as
a good source for dislocation propagation. Some of the
dislocations propagate from grain boundary region and
form stacking fault. It is observed that Shockley partial
dislocations propagate from grain boundary regions along
(111) plane from pre-existing perfect dislocations. Later
on, movement of Shockley partial dislocation is stopped

![](./images/813114049398046721_16.jpg)

by forming Lomer-Cottrell lock and Hirth partial dislo- cation. Therefore, it introduces strain hardening in the material.

The extensive simulation studies presented here provide a comprehensive picture on the link among the laser process- ing parameters, microstructural evolution and thermal energy transfer. Future efforts are directed towards understanding the effects of microstructural evolution on the continuum mate- rial responses such as residual stress, strain and hardening effects.

Acknowledgements The authors gratefully acknowledge the support from the National Science Foundation (Grant Nos. # DMR-0706161, CMMI-1335204, 1334538). Any opinions, findings, conclusions, or recommendations expressed in these documents are those of the authors and do not necessarily reflect the views of the NSF. This work was also supported in part by the start-up fund from the University of Texas at Dallas and an allocation of computing time from the Ohio Supercom- puter Center and Texas Advanced Computing Center.

### References

1. Ivanov DS, Zhigilei LV (2003) Combined atomistic-continuum modeling of short-pulse laser melting and disintegration of metal films. Physi Rev B 68(6):064114

2. Ivanov DS, Zhigilei LV (2004) Combined atomistic-continuum model for simulation of laser interaction with metals: application in the calculation of melting thresholds in Ni targets of varying thickness. Appl Phys A 79(4–6):977–981

3. Koči L, Bringa EM, Ivanov DS, Hawreliak J, McNaney J, Higgin- botham A, Zhigilei LV, Belonoshko AB, Remington BA, Ahuja R (2006) Simulation of shock-induced melting of Ni using molec- ular dynamics coupled to a two-temperature model. Phys Rev B Condens Matter Mater Phys 74(1):012101

4. Duff WH, Zhigilei LV (2007) Computational study of cooling rates and recrystallization kinetics in short pulse laser quenching of metal targets. J Phys Conf Ser 59(1):413–417

5. Lin Z, Leveugle E, Bringa EM, Zhigilei LV (2009) Molecular dynamics simulation of laser melting of nanocrystalline Au†. J Phys Chem C 114(12):5686–5699

6. Karim ET, Shugaev M, Wu C, Lin Z, Hainsey RF, Zhigilei LV (2014) Atomistic simulation study of short pulse laser interactions with a metal target under conditions of spatial confinement by a transparent overlayer. J Appl Phys 115(18):183501

7. Zhigilei LV, Lin Z, Ivanov DS (2009) Atomistic modeling of short pulse laser ablation of metals: connections between melting, spalla- tion, and phase explosion†. J Phys Chem C 113(27):11892–11906

8. Cheng C, Xu X (2005) Mechanisms of decomposition of metal during femtosecond laser ablation. Phys Rev B 72(16):165415

9. Li X, Jiang L, Tsai H-L (2009) Phase change mechanisms during femtosecond laser pulse train ablation of nickel thin films. J Appl Phys 106(6):064906

10. Shen Y, Gan Y, Qi W, Shen Y, Chen Z (2015) Effect of the hot electron blast force on ultrafast laser ablation of nickel thin film. Appl Opt 54(7):1737–1742

11. Gan Y,Chen J (2010) Thermomechanical wave propagation in gold films induced by ultrashort laser pulses. Mech Mater 42(4):491–501

12. Ivanov DS, Rethfeld B, O’Connor GM, Glynn TJ, Volkov AN, Zhigilei LV (2008) The mechanism of nanobump formation in fem- tosecond pulse laser nanostructuring of thin metal films. Appl Phys A 92(4):791–796

13. Lin Z, Johnson RA, Zhigilei LV (2008) Computational study of the generation of crystal defects in a bcc metal target irradiated by short laser pulses. Phys Rev B 77(21):214108

14. Kaganov MI, Lifshitz IM, Tanatarov LV (1956) Relaxation between electrons and crystalline lattices. Zh Eksp Teor Fiz 31:232–237

15. Anisimov S, Kapeliovich B, Perelman T (1974) Electron emission from metal surfaces exposed to ultrashort laser pulses. Zh Eksp Teor Fiz 66(2):375–377

16. Chen G (2005) Nanoscale energy transport and conversion. Oxford University Press, New York

17. Jones RE, Templeton JA, Wagner GJ, Olmsted D, Modine NA (2010) Electron transport enhanced molecular dynamics for metals and semi-metals. Int J Numer Methods Eng 83(8–9):940–967

18. Plimpton S (1995) Fast parallel algorithms for short-range molec- ular dynamics. J Comput Phys 117(1):1–19

19. Tschopp M, McDowell D (2007) Asymmetric tilt grain bound- ary structure and energy in copper and aluminium. Philos Mag 87(25):3871–3892

20. Bonny G, Pasianot RC, Castin N, Malerba L (2009) Ternary Fe–Cu–Ni many-body potential to model reactor pressure vessel steels: first validation by simulated thermal annealing. Philos Mag 89(34–36):3531–3546

21. Liu WK, Qian D, Gonella S, Li SF, Chen W, Chirputkar S (2010) Multiscale methods for mechanical science of complex materials: bridging from quantum to stochastic multiresolution continuum. Int J Numer Methods Eng 83(8–9):1039–1080

22. Zhang L, Wang X (2008) Hybrid atomistic-macroscale modeling of long-time phase change in nanosecond laser-material interaction. Appl Surf Sci 255(5):3097–3103

23. Zhigilei LV, Garrison BJ (1998) Pressure waves in microscopic simulations of laser ablation leonid. In: MRS Proceedings. Cam- bridge University Press

24. Hirayama Y, Obara M (2005) Heat-affected zone and ablation rate of copper ablated with femtosecond laser. J Appl Phys 97(6):064903

25. Lin Z, Zhigilei LV, Celli V (2008) Electron–phonon coupling and electron heat capacity of metals under conditions of strong electron–phonon nonequilibrium. Phys Rev B 77(7):075133

26. Schäfer C, Urbassek HM, Zhigilei LV (2002) Metal ablation by picosecond laser pulses: a hybrid simulation. Phys Rev B 66(11):115404

27. Stukowski A, Albe K (2010) Dislocation detection algorithm for atomistic simulations. Model Simul Mater Sci Eng 18(2):025016

28. Lillo T, Cole J, Frary M, Schlegel S (2009) Influence of grain boundary character on creep void formation in alloy 617. Metall Mater Trans A 40(12):2803–2811

29. Hull D, Bacon DJ (2011) Introduction to dislocations, 5th edn. Butterworth-Heinemann, London

![](./images/813114049398046721_17.jpg)