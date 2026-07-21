# A thermal modelling of displacement cascades in uranium dioxide

G. Martin $^{a,*}$, P. Garcia $^{a}$, C. Sabathier $^{a}$, F. Devynck $^{b}$, M. Krack $^{b}$, S. Maillard $^{a}$

$^{a}$ CEA - DEN/DEC/SESC/LLCC, Bât. 352, 13108 Saint-Paul-Lez-Durance Cedex, France
$^{b}$ Laboratory for Reactor Physics and Systems Behaviour, Paul Scherrer Institute, CH-5232 Villigen PSI, Switzerland

---

## ARTICLE INFO

**Article history:**
Received 28 June 2013
Received in revised form 3 September 2013
Accepted 11 September 2013
Available online 6 February 2014

**Keywords:**
Irradiation
Cascade
Thermal spike
Molecular dynamics
Uranium dioxide

---

## ABSTRACT

The space and time dependent temperature distribution was studied in uranium dioxide during displacement cascades simulated by classical molecular dynamics (MD). The energy for each simulated radiation event ranged between 0.2 keV and 20 keV in cells at initial temperatures of 700 K or 1400 K. Spheres into which atomic velocities were rescaled (thermal spikes) have also been simulated by MD to simulate the thermal excitation induced by displacement cascades. Equipartition of energy was shown to occur in displacement cascades, half of the kinetic energy of the primary knock-on atom being converted after a few tenths of picoseconds into potential energy. The kinetic and potential parts of the system energy are however subjected to little variations during dedicated thermal spike simulations. This is probably due to the velocity rescaling process, which impacts a large number of atoms in this case and would drive the system away from a dynamical equilibrium. This result makes questionable MD simulations of thermal spikes carried out up to now (early 2014). The thermal history of cascades was compared to the heat equation solution of a punctual thermal excitation in $\mathrm{UO}_2$. The maximum volume brought to a temperature above the melting temperature during the simulated cascade events is well reproduced by this simple model. This volume eventually constitutes a relevant estimate of the volume affected by a displacement cascade in $\mathrm{UO}_2$. This definition of the cascade volume could also make sense in other materials, like iron.

---

© 2014 Elsevier B.V. All rights reserved.

---

## 1. Introduction

In pile the nuclear fuel is submitted to high temperatures and irradiation doses which lead to its structural and chemical evolution. In this process, irradiation-induced defects play a major role. In uranium dioxide, which is the fuel the most used worldwide, the mechanisms of defects production under irradiation have been investigated experimentally as theoretically. First of all the electronic energy loss of a nucleus is likely to induce a thermal excitation of the surrounding matter, which is reputed to induce fission gas resolution in the uranium dioxide lattice for instance [1]. Such an excitation is usually referred to as a thermal spike, often described by the two temperatures model (TTM) [2]. The formation of ion tracks induced by swift heavy ions was also studied experimentally in $\mathrm{UO}_2$, namely by transmission electron microscopy [3].

Displacement cascades resulting from atomic collisions under a nuclear energy loss regime were early described by binary collision approximation (BCA) models such as the one proposed by Kinchin and Pease [4]. Radiation damage estimates were derived from such simple descriptions of radiation events, the most famous probably being the Norgett, Robinson and Torrens (NRT) law [5] which considers that 80% of atomic displacements lead to defect formation. A more precise description of displacement cascades in materials was later provided by molecular dynamics (MD) simulations [6]. In uranium dioxide, most of defects induced by displacement events were shown to recombine [7]. The number of created defects in $\mathrm{UO}_2$ was however found to lie within a factor of two relatively to the NRT law. The displacement threshold energy usually considered for this law does not account for the displacements during the simulation of an energetic cascade event, and its overestimation in this former case appeared to partially compensate for the underestimation of the recombined defect fraction [8].

BCA concepts such as the displacement threshold energy $E_d$ fail indeed in describing high energy cascades which induce a collective motion of atoms. At high energy in $\mathrm{UO}_2$, after balistic collisions occurs a stage which involves the formation of a highly disordered volume, appearing as a melt of atoms in the solid. The high temperature gradient inside the disordered volume was shown to have an effect on the defect formation, for instance via the direct formation of vacancy clusters in uranium dioxide [9] through the vacancy sweeping mechanism [10]. Dislocation loops can also directly be formed under irradiation which corroborates transmission electron microscopy observations of irradiated fuel samples (see for

---

* Corresponding author. Tel.: +33 442 252 731.
E-mail address: guillaume.martin@cea.fr (G. Martin).

http://dx.doi.org/10.1016/j.nimb.2013.09.043
0168-583X/© 2014 Elsevier B.V. All rights reserved.

![](./images/813164475619213313_1.jpg)
![](./images/813164475619213313_2.jpg)
![](./images/813164475619213313_3.jpg)

instance [11]). The displacement threshold energy is one order of magnitude lower in this disordered volume relatively to values derived from binary collisions [12].

This paper focuses on the thermal history of a displacement cascade. This was carried out by comparing classical molecular dynamics simulations of full displacement cascades and thermal spikes with the solution of the heat equation solution of an initial point-shaped thermal excitation.

### 2. Modelling

Displacement cascades were simulated using the program CP2K [13,14] and the calculation conditions applied in [12], involving an equilibration step of UO₂ single crystals before a uranium primary knock-on atom (PKA) is accelerated. The Morelon potentials were used [15] to model the uranium dioxide lattice and those of Ziegler, Biersack and Littmark (ZBL) [16] for ballistic collisions. In addition to previous calculations, atom velocities were regularly stored to provide an estimate of the atomic agitation inside the simulation cell.

Spherical thermal spikes were also simulated for further comparison with displacement cascades. The kinetic energy was distributed amongst atoms contained inside a sphere. It was either distributed equally between all atoms or adjusted to follow the radial distribution given by the heat equation solution (Eq. 1 below). The direction of each rescaled atom was either random or kept unchanged after the end of the cell equilibration step. In all cases the maximum amount of energy given to an atom inside the sphere was kept below 20 eV, the minimum displacement threshold energy within the UO₂ lattice [17,18]. These calculations were performed in a NVE ensemble with in most cases a thermostat (velocity rescaling) applied to the first raws at the edges of the simulation box, this having no visible effect on subsequent results since the amount of energy dissipated at boundaries remained relatively low. The energy $E_0$ of PKA and thermal excitations were comprised for this study between 0.2 keV and 20 keV, and the temperature $T_{eq}$ of the equilibrated simulation cells was initially either 700 K or 1400 K. Three similar calculations were each time carried out to provide a raw estimate of the dispersion of results. For sake of clarity are only presented in this paper the thermal spikes initiated according to a velocity distribution in agreement with the heat equation solution (Eq. 1), along with vector directions corresponding to those of the equilibrated simulation box. Results indeed appeared to be quantitatively similar whatever the initial conditions applied, notably when they were similar to those applied in [19].

The heat equation $\dot{T} - D_T \Delta T = 0$ was finally used to simulate the thermal dissipation which follows a punctual energy deposition, $T$ being the local temperature function and $D_T$ the thermal diffusivity of the considered medium. The mean kinetic energy $e_c$ of each atom was here assumed to be given by $e_c = 1.5 k_B T$ although the studied systems are far from thermodynamic equilibrium (with $k_B$ the Boltzmann constant). The Eq. 1 derived from the heat equation for an excitation of energy $E_i$ shows that the kinetic energy of atoms follows a peaked radial distribution which flattens as the time $t$ goes. The density $\rho$ of UO₂ was calculated from [20] at the equilibrium temperature $T_{eq}$ of the material before the thermal excitation occurs (at $t=0$).

$$
e_{c}(r, t)=\frac{E_{i}}{\rho \times\left(4 \pi D_{T} t\right)^{3 / 2}} \exp \left(\frac{-r^{2}}{4 D_{T} t}\right) \tag{1}
$$

The volume of material above the melting temperature is assumed to constitute an estimate of the volume affected by a displacement cascade. In UO₂, the melting temperature $T_m$ is near 3120 K [20]. This volume $V$, called here disordered volume, was calculated from MD results by decomposing the simulation box into $1.5a \times 1.5a \times 1.5a$ cubes, some of them containing atoms of mean kinetic energy above $1.5 k_B T_m$. $a$ is the dimension of an elementary UO₂ cell of 12 atoms. Local temperature and density functions were defined considering little cubes of similar dimension.

$V$ can also be calculated from the heat equation solution described above. It is in this case given by the Eq. 2, with $D_T$ the thermal diffusivity in the solid near $T_m$ ($5.76 \times 10^{-7}$ m² s⁻¹ [20]). The differences between the experimentally measured UO₂ properties and their equivalent in the MD modelled material (see [21]) were here assumed to be negligible.

$$
V=\frac{32 \pi}{3}\left[D_{T} t \ln \left(\frac{E_{i}}{1.5 k_{B}\left(T_{m}-T_{e q}\right) \rho\left(4 \pi D_{T} t\right)^{3 / 2}}\right)\right]^{3 / 2} \tag{2}
$$

### 3. Disordered volume

The Fig. 1 shows the evolution of the volume $V$, into which the values of the local temperature function (as defined in the previous section) are above $T_m$. Displacement cascades initiated with a uranium PKA of 20 keV are compared to spherical thermal spikes initiated at same energy $E_0$. The maximum value of the disordered volume is approximately the same for cascades and spherical thermal spikes. However the lifetime of this volume is almost 10 ps for the thermal spike whereas it barely reaches 3 ps during the full cascade simulation: it behaves as if it was excessively isolated from the surrounding material.

The evolution of $V$ from the heat equation according to Eq. 2 is also reported for a thermal excitation of energy $E_i$ equal to 10 keV. The maximum disordered volume is indeed the same as in 20 keV cascade and thermal spike simulations when $E_i = 10$ keV in this case. This can be explained by the equipartition theorem. Indeed the energy increment $E_0$ should distribute equally into a kinetic and a potential contribution when the simulation cell is been driving to its thermodynamic equilibrium. In Fig. 2a 10 keV of kinetic energy is converted into potential energy after 0.35 ps 20 keV cascades were initiated (results averaged over 3 cascades). Half of the energy $E_0$ converts into potential energy after around 0.35 ps for cascade simulations.

Similar curves were obtained for various $T_{eq}$ and $E_0$. Besides for all initial conditions (temperature, cascade energy and initial $pK_a$ position and direction), the volume $V$ appeared to be maximum at approximately the same time, between 0.3 and 0.4 ps (around 0.32 ps for 20 keV cascades in a simulation cell at 700K as shown

![](./images/813164475619213313_4.jpg)

Fig. 1. Volume $V$ at $T \geqslant T_m$ during a 20 keV cascade simulation (blue), a thermal spike simulation of same energy $E_0$ (red) and calculated from Eq. 2 with $E_i = 10$ keV (black), in a UO₂ medium at $T_{eq}=700$ K.

![](./images/813164475619213313_5.jpg)

Fig. 2. Total kinetic (red) and potential (blue) energy of MD simulated systems respectively normalised at $t=0$ to $E_0$ and 0 in the case of 20 keV cascades (a) and thermal spikes (b).

in Fig. 1). Therefore when the disordered volume is maximum, approximately only half $E_0$ is still in the form of kinetic energy, explaining the correspondence with Eq. 2 applied with $E_i=E_0/2$.

The main difference in the thermal history of a displacement cascade and the thermal modelling from heat equation lies mainly in the kinetics of the growth and shrinkage of the disordered volume. Since energetic atoms can fly over tens of nm during the balistic stage of the cascade, the energy propagation is indeed faster initially in comparison to thermal diffusion processes described via the thermal diffusivity of the material. The expansion of the disordered volume was indeed shown to be supersonic in iron [22] and this is also the case here $(\approx 9000\ \text{m s}^{-1})$.

The Fig. 2b shows that the energy introduced in the system remains mainly under a kinetic form during the MD simulations of thermal spikes. The system stays therefore far from its thermodynamic equilibrium. This probably comes from the process of velocity rescaling which initially puts the simulation cell in a state into which atomic positions and velocities are not correlated. The system would be far from a dynamical equilibrium and would remain in a metastable state. This result makes therefore questionable the relevance of MD simulations of thermal spikes as they were implemented hitherto.

The defect production could notably be largely impacted because as a consequence of this the quenching rate of the hot disordered volume is probably too low, as mentioned above. Indeed in $\text{UO}_2$ the direct formation of defect clusters under irradiation, via notably the vacancy sweeping mechanism [10], is expected to rely on a high recrystallisation rate of the disordered volume. This could explain why far less defects are produced during such thermal spike simulations in $\text{UO}_2$ in comparison to displacement cascades of same energy as stated in [19].

## 4. Cascade

Under irradiation, some material modifications, for instance amorphisation [23] or nanovoid formation [8], require the overlap of several radiation events to occur. The evaluation of the number of cascade overlaps in a material requires an estimate of the volume affected by each cascade event. The volume of a displacement cascade is therefore a valuable parameter although its heterogeneity and fractal nature [24] makes it difficult to define. The damaged volume as defined in [8] agrees the fractal nature of the cascade but seems not relevant since the fraction of undamaged material inside it should increase with the cascade energy $E_0$.

Fig. 3 shows a 10 keV cascade visualised between two parallel planes after 0.35 ps of MD simulation at 700 K, when the disordered volume $V$ is maximum. A high atomic disorder is visible at the cascade core (Fig. 3a). This disorder is better revealed in Fig. 3b which shows crystalline defects determined according to the procedure described in [9]. The associated temperature gradient is visible in Fig. 3c. It causes a depletion at the cascade core (Fig. 3d). This lack of atoms can lead to nanovoid formation in $\text{UO}_2$ [9]. Excepted for the relative density, all representations provide a similar shape of the cascade event. Note that images based on defect density, or on an analysis of the radial distribution function or of atomic coordination numbers are likely to show similar shapes. However since results obtained by these means actually depend strongly on how the disordered material is defined at the atomic scale as discussed in [25], they are not presented here.

![](./images/813164475619213313_6.jpg)

Fig. 3. MD simulation of a 10 keV cascade initiated at 700 K shown between two appropriate planes after 0.35 ps: atoms (a), crystalline defects (b), local temperature (c) and local density relatively to $\rho$ at 700 K (d). (For interpretation of the references to colour in this figure legends, the reader is referred to the web version of this article.)

The material can however be damaged outside the cascade core as shown in Figs. 3a, b and c, since for instance the emission of interstitial defects (and even loop punching when interstitial defects are already present at the cascade periphery [9]) sometimes occurs just after the disordered volume has reached its maximum.

![](./images/813164475619213313_7.jpg)

Fig. 4. Crystalline defects during a 10 keV cascade initiated at 700 K (the same as in Fig. 3) after 0.53 ps and 20 ps of MD simulation.

![](./images/813164475619213313_8.jpg)

Fig. 5. Maximum disordered volume from MD cascade simulations and given by Eq. 3.

The defects analysis of the 10 keV cascade at 0.53 ps shows indeed a disordered area at the bottom right of the cascade core (see Fig. 4a) which led to the formation of interstitial defects at the end of the MD simulation (Fig. 4b). Interstitial defects were also seen to be created within the disordered region, as observed in iron [22].

If subcascades are assumed to significantly interact when the disordered volumes associated to them are connected, as suggested by the study of Calder et al. [22], the maximum disordered volume can nevertheless be considered as a relevant conservative estimate of the volume affected by an energetic cascade in uranium dioxide. This volume $V_{max}$ can be calculated applying Eq. 3 derived from Eq. 2 with $E_{i}=E_{0}/2$. It does not depend on the thermal diffusivity $D_{T}$ of the material. Although it was derived here from the heat equation, it also constitutes a viable approximated solution of conservation equations applied to kinetic energy assuming low spatial variations of energy transfer kinetics in the medium. This makes the Eq. 3 relevant for describing displacement cascades although radiation events are basically more than thermal excitations.

$$
V_{max}=\sqrt{\frac{3}{2\pi\exp(3)}}\times\frac{E_{0}}{\rho\,1.5k_{B}(T_{m}-T_{eq})}\tag{3}
$$

Fig. 5 illustrates that this Eq. 3 reproduces well MD results. This linear relation should be further applicable at energies above 20 keV since above an energy around 25 keV [8,26], the energetic cascade should decompose linearly into less energetic subcascades in $\mathrm{UO}_{2}$.

Furthermore the fact that this volume is proportional to the PKA energy is in agreement with the results obtained in iron by considering the maximum disordered volume as a spaghetti zone formed by chains of atoms displaced from their original sites [22]. The Eq. 3 applied in 300 K iron leads however to volumes almost 60% superior to the ones deduced from the spaghetti analysis. This is probably mainly due to the fact that this analysis follows very closely the region of high defect density at its maximum expansion while the estimate proposed here does not assume that all the volume impacted by the cascade has to be highly defective.

The final number of defects inside the volume impacted by displacement cascades at the end of MD simulations is indeed likely to depend on their formation mechanism and the lattice stability under irradiation within the considered material. The definition proposed here is based on the simple idea according to which atomic disorder can more easily occur when the mean kinetic energy of atoms goes beyond the melting temperature, possibly leading to defect formation and favouring subcascade interaction. This should therefore be consistent in other materials than $\mathrm{UO}_{2}$.

## 5. Conclusion

The conversion of half the kinetic energy into a potential form takes place after a few tenths of picoseconds during displacement cascade simulated by MD whereas energy equipartition does not occur during thermal spike simulations. This first result makes questionable the physical relevance of the MD simulations of thermal spikes carried out up to now.

Displacement cascades are far from a simple heat diffusion process since the flight of energetic atoms during the balistic stage of cascades makes the energy propagation faster in comparison to what is predicted by the heat equation applied with the thermal diffusivity of solid $\mathrm{UO}_{2}$. However such a thermal model gives a good estimate of the maximum volume brought above the melting temperature during the cascade event because this volume essentially relies on the conservation of kinetic energy. This estimate constitutes a relevant definition of the volume impacted by a radiation event in a nuclear energy loss regime. It could also be used to evaluate the dimension of subcascades in $\mathrm{UO}_{2}$. Atomic displacements are indeed likely to occur more easily in such a volume and could favour defect formation and subcascade interaction.

It should be extendable to other materials than $\mathrm{UO}_{2}$, but specific studies have *a priori* to be performed to identify damage mechanisms occurring in the various interesting materials under irradiation to complete this approach. In parallel to such studies on radiation damage processes, this work nevertheless contributes to the integration of MD results at higher scales, the volume impacted by an energetic cascade being a valuable parameter to this aim, in $\mathrm{UO}_{2}$ in particular.

## Acknowledgements

The authors are grateful to AREVA and EDF for their support to this work through the GEN2&3 research program. The Basic Research branch (DSOE/RB) of the Nuclear Energy Division also funded parts of this work.

## References

[1] H. Blank, H. Matzke, The effect of fission spikes on fission gas resolution, Radiat. Eff. 17 (1973) 57-64.
[2] M. Toulemonde, C. Dufour, Z. Wang, E. Paumier, Atomic and cluster ion bombardment in the electronic stopping power regime: a thermal spike description, Nucl. Instrum. Methods B 112 (1996) 26-29.
[3] T. Sonoda, M. Kinoshita, N. Ishikawa, M. Sataka, A. Iwase, K. Yasunaga, Clarification of high density electronic excitation effects on the microstructural evolution in $\mathrm{UO}_{2}$, Nucl. Instrum. Methods B 268 (2010) 3277-3281.
[4] G. Kinchin, R. Pease, The displacement of atoms in solids by radiation, Rep. Prog. Phys. 18 (1955) 1-51.

[5] M.J. Norgett, M.T. Robinson, I.M. Torrens, A proposed method of calculating displacement dose rates, Nucl. Eng. Des. 33 (1975) 50-54.

[6] D.J. Bacon, A.F. Calder, F. Gao, V.G. Kapinos, S.J. Wooding, Computer simulation of defect production by displacement cascades in metals, Nucl. Instrum. Methods B 102 (1995) 37-46.

[7] R. Devanathan, J. Yu, W. Weber, Energetic recoils in $\mathrm{UO}_{2}$ simulated using five different potentials, J. Chem. Phys. 130 (2009) 174502.

[8] G. Martin, P. Garcia, L.V. Brutzel, B. Dorado, S. Maillard, Effect of the cascade energy on defect production in uranium dioxide, Nucl. Instrum. Methods B 269 (2011) 1727-1730.

[9] G. Martin, P. Garcia, C. Sabathier, L.V. Brutzel, B. Dorado, F. Garrido, S. Maillard, Irradiation-induced heterogeneous nucleation in uranium dioxide, Phys. Lett. A 374 (2010) 3038-3041.

[10] V.G. Kapinos, D.J. Bacon, A model for the formation mechanism of depleted zones with a high concentration of vacancies in displacement cascades in metals, Philos. Mag. A 68 (1993) 1165-1181.

[11] L.F. He, M. Gupta, C.A. Yablinsky, J. Gan, M.A. Kirk, X.M. Bai, J. Pakarinen, T.R. Allen, In situ TEM observation of dislocation evolution in Kr-irradiated $\mathrm{UO}_{2}$ single crystal, J. Nucl. Mater. 443 (2013) 71-77.

[12] G. Martin, S. Maillard, L.V. Brutzel, P. Garcia, B. Dorado, C. Valot, A molecular dynamics study of radiation induced diffusion in uranium dioxide, J. Nucl. Mater. 385 (2009) 351-357.

[13] F. Devynck, M. Iannuzzi, M. Krack, Frenkel pair recombinations in $\mathrm{UO}_{2}$: importance of explicit description of polarizability in core-shell moleculardynamics simulations, Phys. Rev. B 85 (2012) 184103. doi:10.1103/PhysRevB.85.184103.

[14] CP2K developers group (2000-2012). <http://www.cp2k.org>.

[15] N. Morelon, D. Ghaleb, J. Delaye, L.V. Brutzel, A new empirical potential for simulating the formation of defects and their mobility in uranium dioxide, Philos. Mag. 83 (2003) 1533-1550.

[16] J.F. Ziegler, J.P. Biersack, U. Littmark, The Stopping and Range of Ions in Solids, Pergamon Press, New York, 1985.

[17] J. Soullard, High voltage electron microscope observations of $\mathrm{UO}_{2}$, J. Nucl. Mater. 135 (1985) 190-196.

[18] C. Meis, A. Chartier, Calculation of the threshold displacement energies in $\mathrm{UO}_{2}$ using ionic potentials, J. Nucl. Mater. 341 (2005) 25-30.

[19] J. Crocombette, Can thermal spike calculations reproduce displacement cascades?, Nucl Instrum. Methods B 267 (2009) 3152-3154.

[20] J.K. Fink, Thermophysical properties of uranium dioxide, J. Nucl. Mater. 279 (2000) 1-18.

[21] K. Govers, S. Lemehov, M. Hou, M. Verwerft, Comparison of interatomic potentials for $\mathrm{UO}_{2}$. Part ii: Molecular dynamics simulations, J. Nucl. Mater. 376 (2008) 66-77.

[22] A.F. Calder, D.J. Bacon, A.V. Barashev, Y.N. Osetsky, On the origin of large interstitial clusters in displacement cascades, Philos. Mag. 90 (2010) 863-884.

[23] G. Carter, R. Webb, The accumulation of amorphousness as a function of irradiation fluence in a composite model of disorder production, Radiat. Eff. Lett. 43 (1979) 19-24.

[24] D. Simeone, L. Luneville, Cascade structure in ion beam experiments: a fractal approach, Phys. Rev. E 82 (2010) 011122.

[25] F. Ribeiro, E. Castelier, M. Bertolus, M. Defranceschi, Molecular dynamics as a tool to interpret macroscopic amorphization-induced swelling in silicon carbide, Eur. Phys. J. B 52 (2006) 163-170.

[26] P. Garcia, G. Martin, C. Sabathier, G. Carlot, A. Michel, P. Martin, B. Dorado, M. Freyss, M. Bertolus, R. Skorek, J. Noirot, L. Noirot, O. Kaitasov, S. Maillard, Nucleation and growth of intragranular defect and insoluble atom clusters in nuclear oxide fuels, Nucl. Instrum. Methods B 277 (2012) 98-108.