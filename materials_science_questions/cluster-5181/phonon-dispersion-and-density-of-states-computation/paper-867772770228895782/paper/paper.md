
# Semi-metals as potential thermoelectric materials: case of HgTe

Maxime Markov \( ^{1} \) , Xixiao Hu \( ^{2} \) , Han-Chun Liu \( ^{1} \) , Naiming Liu \( ^{3} \) , Joseph Poon \( ^{2} \) , Keivan Esfarjani \( ^{2,3,4} \) , and Mona Zebarjadi \( ^{1,3} \) 

 \( ^{1} \) Department of Electrical and Computer Engineering, University of Virginia, Charlottesville, Virginia 22904, USA

 \( ^{2} \) Department of Physics, University of Virginia, Charlottesville, Virginia 22904, USA

 \( ^{3} \) Department of Materials Science and Engineering, University of Virginia, Charlottesville, Virginia 22904, USA

 \( ^{4} \) Department of Mechanical and Aerospace Engineering, University of Virginia, Charlottesville, Virginia 22904, USA

## Abstract

The best thermoelectric materials are believed to be heavily doped semiconductors. The presence of a bandgap is assumed to be essential to achieve large thermoelectric power factor and figure of merit. In this work, we study HgTe as an example semimetal with competitive thermoelectric properties. We employ ab initio calculations with hybrid exchange-correlation functional to accurately describe the electronic band structure in conjunction with the Boltzmann Transport theory to investigate the electronic transport properties. We show that intrinsic HgTe, a semimetal with large disparity in its electron and hole masses, has a high thermoelectric power factor that is comparable to the best known thermoelectric materials. We also calculate the lattice thermal conductivity using first principles calculations and evaluate the overall figure of merit. Finally, we prepare semi-metallic HgTe samples and we characterize their transport properties. We show that our theoretical calculations agree well with the experimental data.
 

## 1 Introduction

Since its discovery in 1821, thermoelectricity remains in the center of interests of the scientific community. Thermoelectric effect (Seebeck effect) refers to direct conversion of thermal to electrical energy in solids and can be used for power generation and waste heat recovery.  \( [1, 2, 3, 4] \) . Despite their clean, environmentally friendly and reliable performances, thermoelectric modules are only used in niche applications such as in powering space probes. The main obstacle preventing thermoelectric technology to be widely used on a mass market today is its relatively low efficiency  \( [5] \) .

The thermoelectric efficiency is an increasing function of the material's dimensionless figure of merit  \( ZT = \frac{S^{2}\sigma}{k} T \)  where S is the Seebeck coefficient,  \( \sigma \)  is the electrical conductivity,  \( \kappa \)  is the thermal conductivity, and T is the absolute temperature. The first two quantities can be combined together into the thermoelectric power factor  \( P_{F} = S^{2}\sigma \)  describing electronic transport, in contrast to the thermal conductivity,  \( \kappa \) , related to thermal transport. The power factor is often used as a guide to preselect the class of potential thermoelectric materials. Indeed, metals have highest electrical conductivity but suffer from a low Seebeck coefficient. The reason for their low Seebeck coefficient is the symmetry of the density of states around the chemical potential. The number of hot electrons above the chemical potential in a metal is roughly the same as the number of cold empty states below the chemical potential. As a result under a temperature gradient, the number of electrons diffusing from the hot side to the cold side, is approximately equal to the number of cold electrons diffusing from the cold side to the hot side. The same problem does not exist in semiconductors due to the presence of a band gap allowing only one type of the carriers to diffuse. Typical Seebeck coefficient of semiconductors is two orders of magnitude larger than metals. Ioffe first noticed this advantage of semiconductors [6] and paved the way for many successful demonstration of doped semiconductors with high ZT values. Later, several research groups including Chasmar & Stratton [7] and Sofo & Mahan [8] studied the effect of band gap on thermoelectric properties of materials employing two-band toy models for electronic structure and reached the conclusion that best thermoelectrics must have band gap greater than at least  \( 6k_{B}T \) . Today, this criteria has become a golden rule and heavily doped semiconductors are the main focus of the thermoelectric society [9]. While opening a band gap is a proven way of increasing the Seebeck coefficient, in this article we show that to have a large Seebeck coefficient, a band gap is not a must. What needed is an asymmetric density of states which could be achieved also in semi-metals with slight overlap of electrons and holes bands but with large asymmetry in the electron and hole effective
 

masses.

We turn our attention to semi-metallic HgTe whose properties are in the transition region between semiconductors and metals. HgTe has a very high electron/hole effective mass ratio  \( m_{e}/m_{h} \simeq 0.1 \)  [10] which results in large values of the Seebeck coefficient between -90  \( \mu V/K \)  [11] and -135  \( \mu V / K \)  [12] at room temperatures which is similar to the Seebeck coefficient of heavily doped semiconductors with a bandgap. The carrier concentration of intrinsic HgTe is only  \( 10^{16} - 10^{17} cm^{-3} \)  which is much smaller than a metal or a typical good heavily-doped semiconductor thermoelectric. However, the large electron mobility in HgTe ( \( \mu > 10^{4} cm^{2}/V \cdot s \) ) [10] makes up for its low carrier concentration and as a result, the electrical conductivity of an intrinsic sample is relatively large and is about  \( \sigma = 1700 S/cm \)  [12, 11] at room temperatures. The large electron mobility is partly due to the small effective mass of the electrons and partly because of the absence of dopants. The mobility of a heavily doped semiconductor is limited by ionized impurity scattering which is not the case in an intrinsic semi-metal. The experiment reveals that intrinsic HgTe is a high power factor material with  \( P_{F} = 14 - 31 \mu W cm^{-1} K^{-2} \)  at T = 300 K [12, 11] that is comparable to well-known thermoelectric materials such as SnSe ( \( P_{F} \simeq 10 \mu W cm^{-1} K^{-2} \) ),  \( PbTe_{1-x}Se_{x} \)  ( \( P_{F} \simeq 25 \mu W cm^{-1} K^{-2} \) ) and  \( Bi_{2}Te_{3} \)  ( \( P_{F} \simeq 50 \mu W cm^{-1} K^{-2} \) ) at their ZT maximum [13]. Apart from having a good electrical transport properties, mercury telluride is a good thermal insulator with  \( \kappa = 2.1 W/mK \)  [11, 14] at T = 300 K. The overall ZT of intrinsic single crystal without any optimization is between 0.4 to 0.5 and is comparable with most good thermoelectric materials at room temperature.

The most recent theoretical study of HgTe concludes that semimetallic HgTe (zinc-blende phase) is a poor thermoelectric material with room temperature ZT values close to zero in intrinsic samples  \( [15] \)  and emphasize the superior thermoelectric performance of a high pressure semiconducting cinnabar phase.  \( [15, 16] \)  However, these studies rely on a standard GGA-PBE exchange-correlation functional to describe the electronic structure of a semimetallic HgTe which fails to reproduce the asymmetry in the density of states near the Fermi level. Moreover, the use of the same constant relaxation time at different doping concentrations results in an erroneous conclusion that the electrical conductivity always grows with the increase of doping. On the contrary, the experimental data shows the drastic decrease of the electrical conductivity with doping in p-type samples of HgTe  \( [11] \) .

In this work, we perform a combined theoretical and experimental study of thermoelectric properties of HgTe at high temperatures. To address the above mentioned issues, we employ ab initio calculations with hybrid exchange-correlation functional in conjunction with the Boltzmann Transport theory.
 

with energy dependent relaxation times obtained from the fitting of experimental electrical conductivity. We do not attempt to optimize the thermoelectric properties of  \( HgTe \)  using nanostructuring, alloying or slight doping. Instead, we attempt to develop a platform based on first principles calculations to study its transport properties and to make a case for semi-metals as potential candidates for thermoelectric applications.

## 2 Results and discussion

## 2.1 Electrical transport

The electronic band structure of zinc-blende  \( HgTe \)  has been extensively studied over the past decade. [17, 18, 19, 20] It has been shown that ab initio calculations with standard LDA and GGA exchange-correlation functionals can not accurately describe the band structure of  \( HgTe \) . To achieve a good agreement with experiment, one must perform either GW calculations [18, 19] or use a hybrid functional [17, 20] where a portion of exact Fock exchange interaction is introduced into a standard exchange-correlation functional.

![](./images/867772770228895782_1.jpg)

![](./images/867772770228895782_2.jpg)

Figure 1: Electronic band structure (panel a), density of states  \( g(E) \)  (panel b) and differential conductivity  \( \sigma_{xx}(E) \)  (panel c) calculated using PBE (black curves) and HSE06 (red curves) exchange-correlation functionals. Energy levels from the latter calculation are labeled according to their symmetries.
 

<table><tr><td></td><td>GGA-PBE</td><td>HSE06</td><td>Expt.</td></tr><tr><td>\( E_{\Gamma} = \mathrm{E}(\Gamma_{6}) - \mathrm{E}(\Gamma_8) \)</td><td>-0.93</td><td>-0.27</td><td>-0.29 [21], -0.30 [22]</td></tr><tr><td>\( \Delta_{\Gamma} = \mathrm{E}(\Gamma_8) - \mathrm{E}(\Gamma_{7}) \)</td><td>0.76</td><td>0.89</td><td>0.91 [21]</td></tr><tr><td>\( E_{L} = \mathrm{E}(L_{6}^{c}) - \mathrm{E}(L_{\mathrm{4,5}}) \)</td><td>1.45</td><td>2.19</td><td>2.25 [22]</td></tr><tr><td>\( \Delta_{L} = \mathrm{E}(L_{\mathrm{4,5}}) - \mathrm{E}(L_{6}^{v}) \)</td><td>0.54</td><td>0.56</td><td>0.62 [22], 0.75 [23]</td></tr><tr><td>\( E_{X} = \mathrm{E}(X_{6}^{c}) - \mathrm{E}(X_{\mathrm{7}}) \)</td><td>4.15</td><td>5.02</td><td>5.00 [23]</td></tr><tr><td>\( \Delta_{X} = \mathrm{E}(X_{7}) - \mathrm{E}(X_{\mathrm{6}}^{v}) \)</td><td>0.19</td><td>0.22</td><td>0.1-0.2 [23]</td></tr></table>

Table 1: Energy band edges, E, and spin-orbit splittings,  \( \Delta \) , at  \( \Gamma \) , L and X high symmetry points calculated with the GGA-PBE and hybrid-HSE06 functionals. Experimental results from the literature are shown.

In Fig. 1 (a), we compare the electronic band structures calculated using GGA-PBE [24] (black curves) and hybrid-HSE06 [25] (red curves) exchange-correlation functionals and summarize the theoretical and experimental band edges, E, and spin-orbit splittings,  \( \Delta \) , at  \( \Gamma \) , L and X high symmetry points in Table 1. First, we note that the HSE06 calculation predicts the correct level ordering  \( \Gamma_{7} \) ,  \( \Gamma_{6} \) ,  \( {\Gamma}_{8} \)  [18, 20] that is consistent with experiment [21] in contrast to the GGA-PBE calculation where the  \( \Gamma_{6} \)  and  \( \Gamma_{7} \)  bands are reversed. Second, the band energies obtained with the hybrid functional are in excellent agreement with experiment. For instance, the inverted band gap  \( E_{g}=E_{\Gamma_{6}}-E_{\Gamma_{8}}=-0.27 \)  eV and spin-orbit splitting  \( \Delta_{0}=E_{\Gamma_{8}}-E_{\Gamma_{7}}=0.89 \)  eV at  \( \Gamma \)  differ from their experimental values only by 0.02 eV. Third, the effective mass of the lowest conduction band is significantly reduced from  \( m_{e}=0.18 \)   \( m_{0} \)  in GGA-PBE to  \( m_{e}=0.04 \)   \( m_{0} \)  in HSE06 in the [100] direction, whereas the effective mass of the top valence bands remains essentially unchanged  \( m_{h}=0.29 \)   \( m_{0} \)  in GGA-PBE to  \( m_{h}=0.33 \)   \( m_{0} \)  in HSE06. Thus, HgTe is a material with a very high electron-hole effective mass ratio.

Finally, the electronic properties of HgTe near the Fermi level are defined by the region of the Brillouin zone close to the  \( \Gamma \)  point, where the bands have a low degeneracy. This low degeneracy in combination with a small electron effective mass in HSE06 calculation results in a small density of states of conduction bands. The asymmetry between the conduction and valence bands is clearly seen in both, the density of states  \( g(E) \)  and the differential conductivity  \( \sigma_{xx}(E) \) , as can be seen in Fig. 1 (b) and (c) respectively.

In Fig. 2 (a), we show the Seebeck coefficient as a function of doping concentration for p- and n-types of doping at T = 290 K calculated using the constant relaxation time approximation. Our results with the GGA-PBE functional agree well with the previous calculation of Chen et al. [15] done with the same exchange-correlation potential. As it is expected from the band structure calculations, one can see a noticeable change in the magnitude.
 
![](./images/867772770228895782_3.jpg)

![](./images/867772770228895782_4.jpg)

Figure 2: The Seebeck coefficient (panel (a)) and the electrical conductivity (panel (b)) as a function of carrier concentration for p-type and n-type samples at  \( T = 290 \, K \)  calculated with GGA-PBE (black dashed line) and hybrid-HSE06 (solid red line) functionals. Experimental data from Whittsett et al. [11] is shown by a blue circle and experimental data measured in this work is shown by black square.

of the Seebeck coefficient due to the increase of the electron-hole effective mass ratio in HSE06 calculation. For instance, the maximum of the Seebeck coefficient is increased from 142  \( \mu \) V/K to 202  \( \mu \) W/K and is slightly shifted towards the lower doping concentrations from  \( 2 \cdot 10^{19} \)  cm \( ^{-3} \)  to  \( 9 \cdot 10^{18} \)  cm \( ^{-3} \) . In intrinsic and low doped samples (up to  \( 10^{17} \)  cm \( ^{-3} \) ), the Seebeck coefficient remains constant but also has a sufficiently higher magnitude of -81  \( \mu \) W/K with HSE06 instead of -31  \( \mu \) V/K with GGA-PBE. Our HSE06 result is in good agreement with experimental result -91  \( \mu \) W/K (blue circle) reported by Whittsett et al [11] for p-type sample. However, our measurements in n-type HgTe sample with  \( n = 3.5 \cdot 10^{17} \)  cm \( ^{-3} \)  doping concentration show much larger values of the Seebeck coefficient of -136  \( \mu \) W/K (black square).

The constant relaxation time theory, does not allow to compute the electrical conductivity but only its ratio to the unknown relaxation time  \( \frac{\sigma}{\tau} \) . As can be seen in Fig. 2 (b), this ratio varies slowly at low doping concentrations and grows rapidly at high doping concentrations. However, one would expect a different behavior for the electrical conductivity at least in the high doping concentration region where a strong charged carrier scattering limits the mobilities. Thus, to further investigate the behavior of the electrical conductivity and the Seebeck coefficient, we introduce the phenomenological scattering rates and fit them to reproduce our experimental electrical conductivity data in n-type sample.

Fig. 3 (a) show our experimental data obtained using the four-terminal
 
![](./images/867772770228895782_5.jpg)

![](./images/867772770228895782_6.jpg)

Figure 3: Panel (a): Temperature variation of the electrical conductivity  \( \sigma \)  measured in the experiment in n-type samples before (violet circles) and after (red and green squares) annealing. The fitting curves are shown by dashed blue and solid black lines respectively. Panel (b): Temperature variation of the Seebeck coefficient S for n-type samples measured in experiment (violet circles and green squares). The theoretical Seebeck coefficients calculated in the CRTA and in the ERTA are shown by black solid and red dashed dotted lines respectively. We have used ZEM and PPMS systems for the measurements.

probe method [26] in the samples prepared using the spark plasma sintering (SPS) technique. Two sets of measurements before (violet circles) and after (red and green squares) annealing have been performed. As expected, annealing improves the electrical conductivity [27, 11] which reaches its maximum value of  \( \sigma = 1036 \, (\Omega \, \text{cm})^{-1} \)  at T = 350 K and then starts monotonically decreasing at higher temperatures. We notice that our results are much lower than the electrical conductivity  \( \sigma = 1700 \, \Omega^{-1} \, cm^{-1} \)  measured in the intrinsic samples at T = 300 K [12, 11]. These intrinsic samples were prepared by multiple annealing of the originally p-type samples in the presence of Hg gas [12, 11]. However, in this work we do not follow this procedure due to the extreme toxicity of mercury.

We fit the measured electrical conductivity using ab initio data for the differential conductivity  \( \sigma_{xx}(E) \)  and the density of states  \( g(E) \)  obtained with the hybrid-HSE06 functional and phenomenological energy dependent scattering rates accounting for the acoustic deformation potential, polar optical and ionized impurity scattering rates. [3] Details of the considered scattering rates are described in Supplementary information. We then recalculate the Seebeck coefficient using the obtained scattering rates and find that its magnitude is increased about 2 times with respect to the constant relaxation time approximation (CRTA). The energy dependent relaxation time
 

approximation (ERTA) results in Seebeck coefficient values that are closer to the experimentally measured ones. Therefore we conclude that the difference between the CRTA calculations (Fig. 2a) and experimental values is a result of the energy dependence of the scattering rates. Although the Seebeck coefficient is not as sensitive as the conductivity to the relaxation times, this example demonstrates that CRTA results could be misleading even in calculation of the Seebeck coefficient.

The temperature variation of the Seebeck coefficient calculated in the CRTA (black solid lines), the ERTA (red dashed dotted line) and measured in experiment are shown in Fig. 3 (b). As one can see, both the theoretical and experimental Seebeck coefficients remain almost temperature independent in the studied temperature range between 300 and 500 K.

Our study reveals that for the accurate description of the electrical transport properties of HgTe, one needs to accurately reproduce the electron-hole effective mass ratio that can not be achieved using standard LDA or GGA exchange-correlation functionals. Moreover, we find that the inclusion of energy dependent scattering rates changes the magnitude of the Seebeck coefficient drastically. The latter has been unexpected since, according to the common believe  \( [29] \) , the CRTA reproduces well the behavior of the diffusion part of the Seebeck coefficient. The magnitude of the Seebeck coefficients of HgTe is an order of magnitude higher than the one in typical metals and close to the typical values of narrow-gap semiconductors. That is explained by the low effective mass and low degeneracy of the conduction band near the Fermi level. We then conclude that the presence of a bandgap is not essential for obtaining large Seebeck coefficient values.

## 2.2 Thermal transport

Now, we turn our attention to the thermal transport properties of HgTe. First, we investigate the lattice dynamics by calculating the phonon spectrum along the high symmetry directions. The phonon dispersion is shown in Fig. 4 and is in an excellent agreement with previous theoretical results  \( [30, 16, 31] \)  as well as with available data from the inelastic neutron scattering experiments  \( [32, 33] \)  (green circles). In our calculations we do not take into account the non-analytical correction to split the optical phonons at  \( \Gamma \)  point. However, this correction should not strongly affect the thermal conductivity since the contribution is usually small due to the low group velocities of optical phonons. Our theoretical frequencies for optical phonons  \( \omega_{O}(\Gamma) = 118 \)  cm \( ^{-1} \)  agree well with the Raman spectroscopy data for the transverse optical phonons  \( \omega_{TO}(\Gamma) = 116 \)  cm \( ^{-1} \)  [34].

To further validate the vibration spectrum, we calculated the elastic con-
 
![](./images/867772770228895782_7.jpg)

Figure 4: Theoretical phonon dispersion calculated using DFPT in this work (black curves) compared to the inelastic neutron scattering data (green circles) [32, 33].

<table><tr><td></td><td>\( C_{11} \) , GPa</td><td>\( C_{12} \) , GPa</td><td>C44, GPa</td></tr><tr><td>Present</td><td>57.3</td><td>41.0</td><td>22.0</td></tr><tr><td>Experiment</td><td>59.7 [35]</td><td>41.5 [35]</td><td>22.6 [35]</td></tr><tr><td>Other</td><td>56.3 [36]</td><td>37.9 [36]</td><td>21.2 [36]</td></tr><tr><td></td><td>67.4 [37]</td><td>45.7 [37]</td><td>30.0 [37]</td></tr></table>

Table 2: Elastic constants  \( C_{ij} \)  (GPa) calculated in the present work and compared with other theoretical calculations [36, 37] and experiment [35].

stants  \( C_{ij} \) . As shown in Table 2, the difference between our theoretical results and experiment does not exceed 4%. Then, we compare the sound velocities in [100] direction obtained from the elastic constants, from the slopes of acoustic branches near the  \( \Gamma \)  point and experimental data in Table 3. The largest differences with the experiment, 7.1% and 2.5% for the transverse (TA) and longitudinal (LA) sound velocities respectively, are found for the evaluation of sound velocities from the slopes of acoustic phonons.

Figure 5 summarizes the theoretical and experimental thermal conductivity obtained in this work as well as those reported by other groups. We perform the lattice thermal conductivity calculations by exactly solving the Boltzmann Transport Equation (BTE). First, we include only the intrinsic three-phonon anharmonic scattering (dotted black curve). We obtain the lattice thermal conductivity that is much lower than the previous ab initio
 

<table><tr><td></td><td>\( v_{L} \) , m/s</td><td>\( v_{T} \) , m/s</td></tr><tr><td>Elastic constant</td><td>2655</td><td>1645</td></tr><tr><td>Slope</td><td>2747</td><td>1504</td></tr><tr><td>Experiment</td><td>2680</td><td>1620</td></tr></table>

Table 3: The longitudinal  \( v_{L} \)  and transverse  \( v_{T} \)  sound velocities (m/s) in [100] direction calculated in the present work from the elastic constants, slopes of acoustic phonons and experiment.

![](./images/867772770228895782_8.jpg)

![](./images/867772770228895782_9.jpg)

Figure 5: Panal (a): Temperature dependence of the thermal conductivity calculated with account for anharmonic three-phonon processes only (black dashed line) and with addition of isotopic disorder scattering (black solid line); green squares - experimental data from Whitsett et al [11]; blue circles - our experimental data; dashed red curve - previous computational result from Refs [16, 31]. Panal (b): Accumulated thermal conductivity as a function of phonon mean free path  \( \Lambda \)  at T = 100 K (blue curve), 300K (black curve) and 500K (red curve). Horizontal dotted line denotes 50 % thermal conductivity reduction.

calculations (red dashed curve) [16]. For instance, we get  \( \kappa_{L}=5.48~W/mK \)  instead of  \( \kappa_{L}=10.46~W/mK \)  in Ref. [16]. Our theoretical values are still higher than ones measured in experiment  \( \kappa_{L}=2.9~W/mK \)  (this work) or  \( \kappa_{L}=2.14~W/mK \)  (Ref. [11]). This discrepancy can not be attributed to the extrinsic sources of scattering such as the impurity scattering since the experimental data for the p-type samples with doping concentration between  \( 10^{16}-10^{18}~cm^{-3} \)  show essentially the same thermal conductivity [11]. The addition of isotopic disorder scattering significantly decreases the thermal conductivity mainly at low temperatures (black solid curve) whereas at high temperatures the isotopic scattering plays a minor role. At room temperature we get  \( \kappa_{L}=4.68~W/mK \)  that is still higher than experimental values.
 
![](./images/867772770228895782_10.jpg)

![](./images/867772770228895782_11.jpg)

Figure 6: Temperature variation of the power factor  \( PFT = S^{2}\sigma T \)  (panel a) and thermoelectric figure of merit ZT (panel b) measured in the experiment (green squares) and calculated in the CRTA (black solid line) and in the ERTA (red dashed dotted line).

While we capture the low temperature trend, we attribute the disagreement between experiment and theory at higher temperatures to some intrinsic scattering mechanism which has not been taken into account in our calculations. We assume that four-phonon anharmonic processes or higher order three phonons are important because of the deviations of  \( \kappa(T) \)  from the 1/T behavior. Thus, the lattice thermal conductivity of HgTe should be subject to further investigation.

In Fig. 5 b, we analyze the accumulated lattice thermal conductivity  \( \kappa_{L}(\Lambda) \)  as a function of phonon mean free path  \( \Lambda \)  (see supplementary material for details) at three different temperatures T = 100 K (blue curve), 300 K (black curve), 500 K (red curve). As one can see, the thermal conductivity is mainly cumulated below 1 micron and the mean free paths become shorter when temperature is increased. The accumulated function can be used to predict the effective size L of a nanostructure necessary to reduce the thermal conductivity and, thus, increase the thermoelectric performance of a material. Indeed, phonons with mean free paths larger than L are scattered by sample boundaries and their contribution to the thermal conductivity is suppressed. The horizontal dotted line denotes a 50% reduction of thermal conductivity. It is found to be L = 136 nm at T = 100 K, L = 42 nm at T = 300 K and L = 25 nm at T = 500 K.

## 2.3 Thermoelectric performance

Finally, we evaluate the overall thermoelectric power factor  \( PFT = S^{2}\sigma T \)  based on our experimental and theoretical data in Fig. 6 (a). As one can see,
 

HgTe possess a high power factor which grows with temperature linearly from  \( 0.8 \, W m^{-1} \, K^{-1} \)  at  \( T = 310 \, K \)  to  \( 0.9 \, W m^{-1} \, K^{-1} \)  at  \( T = 475 \, K \) . Our theoretical values obtained in the ERTA slightly overestimate the experimental power factor but show the same temperature dependence reaching  \( 1.0 \, W m^{-1} \, K^{-1} \)  at  \( T = 500 \, K \) . The CRTA underestimates the magnitude of the Seebeck coefficient and results in a low power factor around  \( 0.2 \, W m^{-1} \, K^{-1} \) . The figure of merit also increases linearly since thermal conductivity is relatively unchanged in this temperature range.

While ZT values reported here are small. We would like to emphasize that this is not an optimized sample. One can increase the ZT values by many different techniques. For example, further increase in the electrical conductivity (a factor of two) is expected after annealing in Hg gas with relatively unchanged Seebeck coefficient and thermal conductivity values  \( [12, 11] \) . As mentioned earlier we avoid this process due to both toxicity of Hg gas and the fact that optimization of the thermoelectric properties of HgTe is not the subject of this work. One can also implement nanostructuring to further reduce the thermal conductivity, a technique that is routinely performed to optimize the thermoelectric figure of merit. Similarly, slight doping (tunning of the chemical potential) and slight alloying could be used to further optimize the performance of semimetallic HgTe. For example, alloying with cadmium could lower the thermal conductivity and still preserves the semimetallic nature of the HgTe for small molar fractions of cadmium  \( (x < 0.1) \) .

## 3 Methods

## 3.1 Theoretical methods

Our theoretical calculations are based on density functional theory (DFT). For the electrical transport calculations, we use Vienna Ab-initio Simulation Package (VASP)  \( [38, 39] \)  combined with Boltzmann Transport Theory as implemented in Boltztrap code  \( [29] \) . We use pseudopotentials based on the projector augmented wave method  \( [40] \)  from VASP library with the generalized gradient approximation by Perdew, Burke and Ernzehof (GGA-PBE)  \( [24] \)  and with a hybrid Heyd-Scuseria-Ernzehof (HSE06)  \( [25] \)  exchange-correlation functionals. A plane wave kinetic cut-off of  \( E_{cut} = 350 \)  eV and  \( \Gamma \) -centered k-point mesh of 8x8x8 were found to be enough to converge the total energy up to 5 meV  \( [20, 41] \) . We use a tetrahedron method for the Brillouin zone integration and the experimental lattice parameter  \( a = 6.460 \AA \)  in both calculations. In our calculations, we take into account the spin-orbit coupling which is important to accurately reproduce the electronic band structure of
 

HgTe. To ensure the convergence of transport integrals in Boltzmann, we use 20 times denser interpolated grid than we do in our ab initio calculations.

For the thermal transport calculations, we use Quantum Espresso  \( [42] \)  package combined with D3Q code to calculate third-order anharmonic force constants using "2n+1" theorem  \( [43] \)  and to solve the Boltzmann Transport equation for phonons variationally  \( [2] \) . We use the norm-conserving pseudopotentials with the exchange-correlation part treated in the local density approximation by Perdew and Zunger (LDA-PZ)  \( [45] \) . We use a cut-off energy of  \( E^{cut} = 1360 \, eV \)  (100 Ry), 8x8x8 k-points mesh to sample the Brillouin zone with Methfessel-Paxton smearing of  \( \sigma = 0.068 \, eV \)  (0.005 Ry). The equilibrium lattice parameter is found to be 6.431 Å. Spin-orbit coupling is not included in the calculations since it has a weak effect on vibrational properties of HgTe as has been pointed out by M. Cardona et al.  \( [30] \) . Phonon frequencies and group velocities are calculated using the density functional perturbation theory (DFPT)  \( [46] \)  on a 8x8x8 q-point grid centered at  \( \Gamma \) . The third-order anharmonic constants are calculated on a 4x4x4 q-point grid in the Brillouin zone that amounts to 42 irreducible triplets. Both phonon harmonic and anharmonic constants are then interpolated on a dense 24x24x24 q-point grid necessary to converge the thermal conductivity calculations.

The detailed information about the charged carrier scattering rates obtained from the electrical conductivity fit and about the isotopic disorder scattering rates used in the lattice thermal conductivity calculation is reported in the supplementary material.

## 3.2 Experimental methods

A 99.99% purity of HgTe ingot was purchased from 1717 CheMall Corporation for HgTe sample preparation and the density of the ingot was  \( 7.82 \pm 0.04 \, g/cm^{3} \)  obtained by Archimedes' principle. We crashed the ingot and milled it with a mortar and pestle for about 10 minutes to obtain fine powders. Later, they were consolidated into a  \( 0.5'' \) -diameter compact disk by using spark plasma sintering (SPS) method at 783K, 50MPa for 15 minutes. After SPS process, the density of the HgTe disk is increased to  \( 7.98 \pm 0.17 \, g/cm^{3} \) , which is quite close to the theoretical fully-dense value of the HgTe density  \( 8.13 \, g/cm^{3} \) . For annealing preparation, the compact HgTe sample was sealed in an evacuated capsule, and it was situated in the middle of a furnace at 523 K for 5 days.

For the ingot samples, we used the machine to cut it into a rectangular-bar-shaped sample with the dimension of  \( 2 \times 4 \times 8 \, mm^{3} \) . For the SPS samples, due to their fragility, we hand-polished the disk into a rectangular-shaped bar of the same size as the ingot one instead of cutting them in the machine. The
 
![](./images/867772770228895782_12.jpg)

Figure 7: The comparison of the x-ray diffraction (XRD) results between (a) ingot, (b) SPS, and (c) SPS-annealing samples. The excess Te peaks in the ingot samples are highlighted by red color.
 

four-probe electrical conductivity and Seebeck coefficient measurements were performed in the helium atmosphere with a ZEM-3 equipment from Ulvac Tech., Inc. The Hall coefficient measurements were conducted in Quantum Design Versa-Lab. The thermal diffusivity experiments were carried out with a LFA 467 HyperFlash equipment from NETZSCH. The measured thermal diffusivity was then multiplied by the theoretical heat capacity  \( [1] \)   \( C_{p}(T) = C_{V}(T) + 1.01 \cdot 10^{-2}T \)  where  \( C_{V}(T) \)  was obtained from the Debye model.

X-ray diffraction data are shown in fig. 7. Figure. 7(a) shows the original ingot contains single-phase HgTe with excess tellurium. After the SPS process, in additional to the original HgTe phase, a new crystal phase,  \( Hg_{x}Te_{z} \) , emerges (see panel (b)), and the excess Te peaks, i.e., Te (101) and Te (102), disappear. Panel (c) shows that the SPS-annealing sample is a single-phase HgTe crystal without the excess of Te. Note that the phase of  \( Hg_{x}Te_{z} \)  vanishes after annealing.

Additional information about the Hall coefficient measurements is provided with the supplementary material.

## 4 Conclusions

In conclusion, we have investigated, both experimentally and theoretically, the electrical and thermal transport properties of HgTe at high-temperatures between 300 and 500 K. We have found that HgTe is a good thermoelectric material in a low pressure semi-metallic zinc-blende phase as it has a high Seebeck coefficient and a low thermal conductivity. To explain the experimental data for the Seebeck coefficient, we accurately reproduce the electron-hole effective mass ratio by performing ab initio calculations with the hybrid-HSE06 exchange-correlation functional and take into account the phenomenological scattering rates extracted from a fit to electrical conductivity. Finally, we perform the lattice thermal conductivity calculations by exactly solving the Boltzmann Transport Equation (BTE). We include three-phonon anharmonic scattering and isotopic disorder scattering processes. We attribute the disagreement between experiment and theory to some intrinsic scattering mechanism which has not been taken into account in our calculations. Our work demonstrates that large thermoelectric power factors could be achieved even in the absence of an energy bandgap.
 

## Acknowledgements

M.M., H.L and M.Z acknowledges support from Air Force Young Investigator Award (Grant FA9550-14-1-0316). M.Z. acknowledges support from National Space Grant College and Fellowship Program (SPACE Grant) Training Grant 2015-2018, grant number NNX15A120H. We acknowledge the SEAS for the computational time on Rivanna HPC cluster.

## Conflict of interest

There are no conflicts to declare.

## References

[1] S. B. Riffat and X. Ma. Thermoelectrics: a review of present and potential applications. Appl. Therm. Eng., 23:913, 2003.

[2] M. Zebarjadi, K. Esfarjani, M. S. Dresselhaus, Z.F. Ren, and G. Chen. Perspectives on thermoelectrics: from fundamentals to device applications. Energy Environ. Sci., 5:5147, 2012.

[3] D. Champier. Thermoelectric generators: a review of applications. Energy Convers. Manag., 140:167, 2017.

[4] D. Zhao and G. Tan. A review of thermoelectric cooling: Materials, modeling and applications. Applied Thermal Engineering, 66:15, 2014.

[5] M.C. Davis, B. P. Banney, P.T. Clarke, B. R. Manners, and R. M. Weymouth. Handbook of Thermoelectrics: Macro to Nano, edited by D. M. Rowe. CRC Press, Boca Raton, Florida, 2006.

[6] A. F. Ioffe. The problem of new energy sources. The socialist reconstruction and science, 1:23, 1932.

[7] R. Chasmar and R. Stratton. The thermoelectric figure of merit and its relation to thermoelectric generators. J. Electron. Control, 7:52, 1959.

[8] J. O. Sofo and J. D. Mahan. Optimum band gap of a thermoelectric material. Phys. Rev. B, 49:4565, 1994.

[9] A. M. Dehkordi, M. Zebarjadi, J. He, and T. M. Tritt. Thermoelectric power factor: Enhancement mechanisms and strategies for higher performance thermoelectric materials. Mat. Sci. Eng. R, 97:1, 2015.
 

[10] L.I. Berger. Semiconductor materials. CRC Press, Boca Raton, Florida, 1997.

[11] C. R. Whitsett and D. A. Nelson. Lattice thermal conductivity of p-type mercury telluride. Physical Review B, 5:3125, 1972.

[12] Z. Dziuba and Zakrzewski T. The electrical and thermoelectrical properties of HgTe in the temperature range of intrinsic conductivity. Physica Status Solidi, 7:1019, 1964.

[13] M. Beekman, D. T. Morelli, and G. S. Nolas. Better thermoelectrics through glass-like crystals. Nature Mat., 14:1182, 2015.

[14] G. A. Slack. Thermal conductivity of ii-vi compounds and phonon scattering by  \( Fe^{2+} \)  impurities. Phys. Rev. B, 6:3791, 1972.

[15] X. Chen, Y. Wang, T. Cui, Y. Ma, G. Zou, and T. Iitaka. HgTe: A potential thermoelectric material in the cinnabar phase. The Journal of Chemical Physics, 128:194713, 2008.

[16] T. Ouyang and M. Hu. First-principles study on lattice thermal conductivity of thermoelectrics HgTe in different phases. Journal of Applied Physics, 117:245101, 2015.

[17] Feng W., D. Xiao, Y. Zhang, and Y. Yao. Half-Heusler topological insulators: A first-principles study with the Tran-Blaha modified Becke-Johnson density functional. Phys. Rev. B, 82:235121, 2010.

[18] A. Svane, N. E. Christensen, M. Cardona, A. N. Chantis, M. van Schilfgaarde, and T. Kotani. Quasiparticle band structures of  \( \beta \) -HgS, HgSe, and HgTe. Physical Review B, 84:205205, 2011.

[19] R. Sakuma, C. Friedrich, T. Miyake, S. Blügel, and F. Aryasetiawan. GW calculations including spin-orbit coupling: Application to Hg chalcogenides. Physical Review B, 84:085144, 2011.

[20] J. W. Nicklas and J. W. Wilkins. Accurate electronic properties for  \( (\mathrm{Hg},\mathrm{Cd})\mathrm{Te} \)  systems using hybrid density functional theory. Physical Review B, 84:121308(R), 2011.

[21] N. Orlowski, J. Augustin, Z. Goacki, C. Janowitz, and R. Manzke. Direct evidence for the inverted band structure of hgte. Physical Review B, 61:5058(R), 2000.
 

[22] D. J. Chadi, J. P. Walter, M. L. Cohen, Y. Petroff, and M. Balkanski. Reflectivities and electronic band structures of CdTe and HgTe. Physical Review B, 5:3058, 1972.

[23] W. J. Scouler and G. B. Wright. Reflectivity of HgSe and HgTe from 4 to 12 ev at 12 and 300 k. Physical Review B, 133:A736, 1964.

[24] J. P. Perdew, K. Burke, and M. Ernzerhof. Generalized gradient approximation made simple. Phys. Rev. Lett., 77:3865, 1996.

[25] J. Heyd, G. E. Scuseria, and M. Ernzerhof. Hybrid functionals based on a screened Coulomb potential. J. Chem. Phys., 118:8207, 2003.

[26] F. M. Smits. Measurement of sheet resistivities with the four-point probe. Bell Syst. Tech. J., 37:711, 1958.

[27] T. Okazaki and K. Shogenji. Effects of annealing on the electrical properties of HgTe crystals. J. Phys. Chem. Solids, 36:439, 1975.

[28] M. Lundstrom. Fundamentals of carrier transport. Cambridge University Press, New York, 2000.

[29] G. K. H. Madsen and D. J. Singh. Bolztrap. a code for calculating band-structure dependent quantities. Computer Physics Communications, 175:67, 2006.

[30] M. Cardona, R. K. Kremer, R. Lauck, G. Siegle, A. Muoz, and A. H. Romero. Electronic, vibrational, and thermodynamic properties of metacinnabar  \( \beta \) -HgS, HgSe, and HgTe. Physical Review B, 80:195204, 2009.

[31] T. Ouyang and M. Hu. Competing mechanism driving diverse pressure dependence of thermal conductivity of XTe (X = Hg, Cd, and Zn). Physical Review B, 92:235204, 2015.

[32] H. Kepa, W. Gebicki, and T. Giebultowicz. A neutron study of phonon dispersion relations in hgte. Solid State Commun., 34:211, 1980.

[33] H. Kepa, T. Giebultowicz, B. Buras, B. Lebech, and K. Clausen. A neutron scattering study of lattice dynamics of HgTe and HgSe. Phys. Scr., 25:807, 1982.

[34] A. Mooradian and T. C. Harman. The physics of semimetals and narrow gap semiconductors, Proc. Conf. Dallas edited by D. L. Carter and T. Bate. Pergamon Press, Oxford, 1970.
 

[35] O. Madelung, M. Schulz, and H. Weiss. Landolt-Bornstein - Group III, Condensed Matter Numerical Data and Functional Relationships in Science and Technology vol. 41B. Springer-Verlag, Berlin, 1982.

[36] B. D. Rajput and D. A. Browne. Lattice dynamics of II-VI materials using the adiabatic bond-charge model. Phys. Rev. B, 53:9052, 1996.

[37] J. Tan, G. Ji, X. Chen, L. Zhang, and Y. Wen. The high-pressure phase transitions and vibrational properties of zinc-blende XTe (X = Zn, Cd, Hg): Performance of local-density-approximation density functional theory. Comput. Mat. Science, 48:796, 2010.

[38] G. Kresse and J. Hafner. Efficiency of ab-initio total energy calculations for metals and semiconductors using a plane-wave basis set. J. Phys. Cond. Matter, 6:15, 1996.

[39] G. Kresse and J. Furthmüller. Efficient iterative schemes for ab initio total-energy calculation using a plane-wave basis set. Phys. Rev. B, 54:11169, 1996.

[40] P. E. Blochl. Projector augmented-wave method. Physical Review B, 50:17953, 1994.

[41] J. W. Nicklas. Methods for accurately modeling complex materials. Electronic Thesis or Dissertation. Ohio State University, 2013.

[42] P. Giannozzi, S. Baroni, N. Bonini, M. Calandra, R. Car, C. Cavazzoni, D. Ceresoli, G.L. Chiarotti, M. Cococcioni, I. Dabo, A. Dal Corso, S. De Gironcoli, S. Fabris, G. Fratesi, R. Gebauer, U. Gerstmann, C. Gougoussis, A. Kokalj, M. Lazzeri, L. Martin-Samos, N. Marzari, F. Mauri, R. Mazzarello, S. Paolini, A. Pasquarello, L. Paulatto, C. Sbraccia, S. Scandolo, G. Sclauzero, A.P. Seitsonen, A. Smogunov, Umari P., and R.M. Wentzcovitch. QUANTUM ESPRESSO: A modular and open-source software project for quantum simulations of materials. J. Phys.: Condens. Matter, 21:395502, 2009.

[43] L. Paulatto, F. Mauri, and M. Lazzeri. Anharmonic properties from a generalized third-order ab initio approach: Theory and applications to graphite and graphene. Phys. Rev. B, 87:214303, 2013.

[44] G. Fugallo, M. Lazzeri, L. Paulatto, and F. Mauri. Ab initio variational approach for evaluating lattice thermal conductivity. Phys. Rev. B, 88:045430, 2013.
 

[45] J. P. Perdew and K. Zunger. Self-interaction correction to density-functional approximations for many-electron systems. Phys. Rev. B, 23:5048, 1981.

[46] S. Baroni, S. de Gironcoli, and A. Dal Corso. Phonons and related crystal properties from density-functional perturbation theory. Rev. Mod. Phys., 73:515, 2001.

[47] V. M. Glazov and L. M. Pavlova. Rus. J. Phys. Chem., 70:441, 1996.
 

# Supplementary material
for

# "Semi-metals as potential thermoelectric materials: case of HgTe"

In this supplementary material, we provide the supporting information about the Hall coefficient measurements, the electrical conductivity fitting, the lattice thermal conductivity calculations and measurements.

## 4.1 Hall coefficient measurements.

In Fig. S1, we show the experimental data for the Hall effect resistance  \( R_{xy} \)  as a function of an applied external magnetic field B in the temperature range  \( 200 K \leq T \leq 400 K \) . The Hall coefficient  \( R_{H} \)  can be extracted from the slope of the  \( R_{xy}(B) \)  curve as

 \[ R_{H}(T)=\frac{R_{xy}(T)}{B}l \quad (S.1) \] 

where l is the sample thickness. The net carrier concentration and electron mobilities can be found from the Hall coefficient data as

 \[ n(T)=\frac{1}{eR_{H}(T)} \quad (S.2) \] 

 \[ \mu_{e}(T)=\frac{R_{H}(T)}{R l} \quad (S.3) \] 

and are shown in Fig. S2 and Fig. S3 respectively. Here e is an elementary charge, R is the resistance of the sample without magnetic field.

## 4.2 Electrical conductivity fitting.

The electrical conductivity can be found using the following expression

 \[ \sigma(T,\mu)=\frac{1}{V_{cell}}\int\sigma(E)\left[-\frac{\partial f_{\mu}(T,E)}{\partial E}\right]dE \quad (S.4) \] 

where  \( V_{cell} \)  is a unit cell volume, E is energy,  \( \mu \)  is the chemical potential,  \( f_{\mu} \)  is the Fermi-Dirac distribution function and  \( \sigma(E) \)  is the differential conductivity

 \[ \sigma(E)=e^{2}\tau(E)g(E)v_{g}^{2}(E) \quad (S.5) \]
 

where  \(  g(E)  \)  is the density of states,  \(  v_{g}(E)  \)  is a group velocity and  \(  \tau(E) = 1 / \Gamma(E)  \)  is the total relaxation time that is inversely proportional to the total scattering rate  \(  \Gamma(E)  \) . In our calculations we use  \(  g(E)  \)  and  \( v_{g} \)  obtained with the HSE06 exchange-correlation functional. In the constant relaxation time approximation (CRTA), one assumes that  \(  \tau(E)  \)  is constant and energy independent.

In this work, we consider the energy dependent scattering rates. We consider 3 types of carrier scattering including acoustic deformation potential scattering  \( \Gamma^{ac}(E) \) , ionized impurity scattering  \( \Gamma^{\text{imp}}(E) \)  and polar optical scattering  \( \Gamma^{pop}(E) \)  [3]. As follows from the Matthiessen's rule, the total scattering rate  \( \Gamma(E) \)  is a sum of all three contributions. Overall, we have 4 fitting parameters  \( A_{1} \) ,  \( A_{2} \) ,  \( \bar{A}_{3} \)  and phonon energy  \( \hbar\omega \) .

Acoustic deformation potential scattering rate is

 \[ \Gamma^{a c}(E)=A_{1}g(E) \quad (S.6) \] 

Ionized impurity scattering rate is

 \[ \Gamma^{i m p}(E)=A_{2}n_{C}T E^{-3/2} \quad (S.7) \] 

where  \( n_{C} \)  is the net carrier concentration obtained from the Hall coefficient measurements (see Fig. S2)

 \[ n_{C}(T)=n_{0}\exp(-T_{d}/T) \quad (S.8) \] 

where  \( T_{d} = 450.9 \)  K and  \( n_{0} = 16.01 \cdot 10^{17} \)  cm \( ^{-3} \) .

Polar optical scattering rate is

 \[ \Gamma^{p o p}(E)=A_{3}\frac{\hbar\omega}{v_{g}}\left[n_{B E}\sqrt{1+\frac{\hbar\omega}{E}}-n_{B E}\frac{\hbar\omega}{B}\sinh^{-1}\left(\sqrt{\frac{E}{\hbar\omega}}\right)+\right. \] 

 \[ +(n_{B E}+1)\sqrt{1-\frac{\hbar\omega}{E}}+(n_{B E}+1)\frac{\hbar\omega}{B}\sinh^{-1}\left(\sqrt{\frac{E}{\hbar\omega}-1}\right)\Bigg] \quad (S.9) \] 

where  \( n_{BE} \)  is the Bose-Einstein distribution function,  \( v_{g} \)  is the group velocity. The first two terms represent the polar-optical absorption while the last two terms describe the emission.

The energy dependent scattering rates obtained from the fitting to experimental electrical conductivity for the samples before and after annealing are shown in Fig. S4.
 

## 4.3 Thermal conductivity measurements.

To obtain the thermal conductivity  \( \kappa \) , we use the following formula

 \[ \kappa(T)=\rho c_{p}(T)D(T) \quad (S.10) \] 

where  \( \rho \)  is the measured density of a sample,  \( D(T) \)  is the measured thermal diffusivity and  \( c_{p}(T) \)  is the theoretical specific heat capacity. The measured thermal diffusivity for the original ingot sample and the sample after the SPS is shown in Fig. S5. The ingot sample has an excess of Te atoms, and a lower density,  \( \rho=7.82\pm0.04~g/cm^{3} \) , comparing to  \( \rho=7.98\pm0.17~g/cm^{3} \)  after the SPS. The thermal diffusivity is higher for the ingot samples (black circles) than in the SPS samples (blue triangles), but does not change after the annealing of the SPS sample. The theoretical heat capacity is

 \[ c_{p}=c_{v}+V\frac{\alpha^{2}}{\beta_{T}}T \quad (S.11) \] 

where  \( \alpha \)  is the coefficient of thermal expansion,  \( \beta_{T} \)  is the isothermal diffusivity,  \( c_{V} \)  can be found from the Debye model

 \[ c_{v}=9N_{A}k_{B}\left(\frac{T}{T_{D}}\right)^{3}\int_{0}^{x_{D}}d x\frac{x^{4}e^{x}}{(e^{x}-1)^{2}} \quad (S.12) \] 

where  \( T_{D}=140 \)  K is the Debye temperature. For the second term in Eq. S.11, we use the experimental values from Ref. [1] and get the following expression for the specific heat

 \[ c_{p}(T)=c_{V}(T)+1.01\cdot10^{-2}T \quad (S.13) \] 

The obtained heat capacity  \( c_{p}(T) \)  linearly changes from  \( 0.158\ JK^{-1}g^{-1} \)  at T = 250 K to  \( 0.171\ JK^{-1}g^{-1} \)  at T = 700 K

## 4.4 Isotopic scattering for phonons.

In this work, we perform ab initio calculations solving the Boltzmann Transport Equation (BTE). The algorithm we use is described in details in Ref. [2]. Apart from the intrinsic three-phonon scattering processes, we include the isotopic disorder scattering processes with rates given by

 \[ P_{\mathbf{q}j}^{i s o}=\frac{\pi}{2N_{\mathbf{q}}}\omega_{\mathbf{q}j}\omega_{\mathbf{q}^{\prime}j^{\prime}}\delta\big(\hbar\omega_{\mathbf{q}j}-\hbar\omega_{\mathbf{q}^{\prime}j^{\prime}}\big)\left[n_{\mathbf{q}j}n_{\mathbf{q}^{\prime}j^{\prime}}+\frac{n_{\mathbf{q}j}+n_{\mathbf{q}^{\prime}j^{\prime}}}{2}\right]\sum_{s}g_{2}^{s}\left|\sum_{\alpha}z_{\mathbf{q}j}^{s\alpha}z_{\mathbf{q}^{\prime}j^{\prime}}^{s\alpha}\right|^{2} \quad (S.14) \]
 

where q - phonon wave vector, j - phonon branch index,  \( \omega_{qj} \)  - frequency of phonon  \( (\mathbf{q}, j) \) ,  \( n_{qj} \)  - Bose-Einstein distribution function,  \( \alpha \)  - Cartesian coordinate, s - atom type,  \( z_{q}^{s\alpha} \)  - phonon eigenmode,  \( g_{2}^{s} \)  - isotopic fluctuation parameter

 \[ g_{2}^{s}=\frac{\sum_{i}c_{i}M_{i}^{2}-(\sum_{i}c_{ i}M_{i})^{2}}{(\sum_{i}c _{i}M_{i})^{ 2}} \quad (S.15) \] 

We use the natural isotopic composition of Hg and Te as summarized in Table 4. The resulting isotopic fluctuation parameters are  \( g_{2}^{s} = 6.5 \cdot 10^{-5} \)  for Hg and  \( g_{2}^{s} = 28.4 \cdot 10^{-5} \)  for Te.

<table><tr><td>\( M_{Hg} \) , amu</td><td>%</td><td>\( M_{Te} \) , amu</td><td>%B</td></tr><tr><td>195.966</td><td>0.15</td><td>119.904</td><td>0.09</td></tr><tr><td>197.967</td><td>9.97</td><td>121.903</td><td>2.55</td></tr><tr><td>198.968</td><td>16.87</td><td>122.904</td><td>0.89</td></tr><tr><td>199.968</td><td>23.10</td><td>123.903</td><td>4.74</td></tr><tr><td>200.970</td><td>13.18</td><td>124.904</td><td>7.07</td></tr><tr><td>201.971</td><td>29.86</td><td>125.903</td><td>18.84</td></tr><tr><td>203.973</td><td>6.87</td><td>127.904</td><td>31.74</td></tr><tr><td></td><td></td><td>129.906</td><td>34.08</td></tr></table>

Table 4: List of natural isotopes of Hg and Te.

## 4.5 Accumulated thermal conductivity.

The lattice thermal conductivity can be written as

 \[ \kappa_{L}=\frac{1}{k_{B}T^{2}V_{cell}N_{q}}\sum_{\nu}n_{\nu}(1+n_{\nu})\omega_{\nu}^{2}c_{\nu}F_{\nu} \quad (S.16) \] 

where  \( V_{cell} \)  is the unit cell volume,  \( \nu = \{q, j\} \) ,  \( c_{\nu} \)  is the group velocity,  \( F_{\nu} \)  and the linear deviation of the out-of-equilibrium phonon distribution  \( n_{\nu}^{out} \)  from its equilibrium value  \( n_{\nu} \) 

 \[ n_{\nu}^{out}=n_{\nu}-\mathbf{F}_{\nu}\cdot\nabla T\frac{\partial n_{\nu}}{\partial T} \quad (S.17) \] 

It can be found from the solution of the Boltzmann Trasport Equation. In the relaxation time approximation (RTA)  \( F_{\nu}^{RTA} = \Lambda_{\nu}^{RTA}= \tau_{\nu} c_{\nu} \) . In the exact solution it plays a role of a vectorial mean free-path dispacement. To find a scalar mean-free path  \( \Lambda_{\nu}^{exact} \) , one needs to project it onto velocity direction

 \[ \Lambda_{\nu}^{e x a c t}=\frac{\mathbf{F}_{\nu}\cdot\mathbf{c}_{\nu}}{|\mathbf{c}_{\nu}|} \quad (S.18) \]
 

The lattice thermal conductivity can be rewritten as a function of one single variable  \( \Lambda \)  as

 \[ \kappa_{L}=\sum_{\nu}\kappa_{L}(\Lambda_{\nu})=\int d\Lambda\kappa_{L}^{a c c}(\Lambda) \quad (S.19) \] 

where the accumulated thermal conductivity is defined as

 \[ \kappa_{L}^{a c c}(\Lambda)=\sum_{\nu}\kappa_{L}(\Lambda)\delta(\Lambda-\Lambda_{\nu}) \quad (S.20) \] 

In Fig. S6 we show the difference in the accumulated thermal conductivities in the two approaches discussed above. As one can see, the mean free path distribution in the exact approach is shifted toward the longer values.

## References

[S1] V. M. Glazov and L. M. Pavlova. Rus. J. Phys. Chem., 70:441, 1996.

[S2] G. Fugallo, M. Lazzeri, L. Paulatto, and F. Mauri. Ab initio variational approach for evaluating lattice thermal conductivity. Phys. Rev. B, 88:045430, 2013.

[S3] M. Lundstrom. Fundamentals of carrier transport. Cambridge University Press, New York, 2000.
 
![](./images/867772770228895782_13.jpg)

Figure S1: The Hall effect resistance  \( R_{xy} \)  measured as a function of magnetic field B at different temperatures.
 
![](./images/867772770228895782_14.jpg)

Figure S2: The net carrier concentration obtained from the Hall coefficient measurements as a function of temperature for the samples before (blue diamonds) and after (red diamonds) annealing. The samples are found to be n-type.
 
![](./images/867772770228895782_15.jpg)

Figure S3: The experimental carrier mobilities as a function of temperature for the samples before (blue diamonds) and after (red diamonds) annealing. The mobilities are improved after annealing. In both samples, the mobilities decrease with temperature.
 
![](./images/867772770228895782_16.jpg)

![](./images/867772770228895782_17.jpg)

Figure S4: Acoustic deformation potential (yellow curves), polar optical (maroon curves) and charged impurity (blue curves) scattering rates obtained from the fitting of experimental electrical conductivities in the samples before (top panel) and after (bottom panel) annealing.
 
![](./images/867772770228895782_18.jpg)

Figure S5: The temperature-dependent thermal diffusivity of HgTe ingot and SPS samples. The thermal diffusivity decreases after the SPS process, and both of ingot and SPS samples thermal diffusivity reduce with increased temperature.
 
![](./images/867772770228895782_19.jpg)

Figure S6: Accumulated thermal conductivity calculated within the RTA (dashed lines) and from the exact solution of the BTE (solid lines).
 
