# TRACK NANODOSIMETRY OF AN ALPHA PARTICLE

L. De Nardo†, P. Colautti‡, W. Y. Baek§, B. Grosswendt§, A. Alkaa∥, P. Ségur∥ and G. Tornielli†

†Dipartimento di Fisica dell'Università di Padova, via Marzolo 8, I-35100 Padova, Italy
‡INFN Laboratori Nazionali di Legnaro, Via Romea 4, I-35020 Legnaro, Padova, Italy
§Physikalisch-Technische Bundesanstalt, Bundesallee 100, D-38116 Braunschweig, Germany
∥Centre de Physique des Plasmas et de leurs Applications de Toulouse
U.M.R. du CNRS n° 5002, Université Paul Sabatier, 118 Route de Narbonne, 31052
Toulouse Cedex 04, France

**Abstract** — Experimental measurements and calculations are described of ionisation distributions in propane wall-less gas cavities of about 20 nm simulated size, performed at different distances from a ²⁴⁴Cm alpha particle track. Ionisation events are detected one by one by collecting electrons from the sensitive volume and by separating them with a drift column. Experimental results and Monte Carlo calculations indicate that, in the delta ray cloud, conditional probability curves, average cluster size and the ratio of second moment above first moment of the cluster distribution are invariant with track distance.

## INTRODUCTION

Effects of radiation are primarily determined by what happens in individual small volumes representative of DNA segments. Such sites are so small that the interactions due to the radiation are very few and it is necessary to consider the stochastics of the number and nature of primary interactions and of secondary processes in order to understand the subsequent biological effects. Track nanodosimetry has the objective of investigating the stochastic aspect of energy deposition in particle tracks, by measuring the ionisation distributions induced by a charged particle in nanometric volumes of tissue-equivalent matter, positioned at different distances from the track. This paper is concerned with measurements and Monte Carlo calculations of ionisation distributions produced in a site of about 20 nm by a ²⁴⁴Cm alpha particle.

## APPARATUS AND TECHNIQUES

The detector consists essentially of an electron collector and a single electron counter (SEC). A schematic diagram of the apparatus is presented in Figure 1. The electron collector is a system of electrodes that encloses an almost wall-less cylindrical volume whose height equals its diameter. Electrons created inside this volume, the sensitive volume (SV) of the counter, are transferred into the drift column of the SEC and are detected one by one, by using a multi-step avalanche chamber (MSAC). Two collimators positioned in front of a solid-state detector (SSD) define the alpha particle track, with respect to which the detector can be moved using a micrometric screw. More details about the apparatus can be found elsewhere⁽¹·²⁾. Measurements have been performed from 0 to 70 nm aside the track. The SSD signal triggers the counter acquisition system.

The whole detection system is immersed in the counting gas at a given pressure. Measurements have been performed at 300 and 350 Pa of propane, corresponding to simulated diameters of the SV (at 20°C) of 19 nm and 22.5 nm, respectively. The detector efficiency has been calculated, with a Monte Carlo code, by transporting electrons throughout the counter. Calculations point to an efficiency of about 25% at 300 Pa and of about 30% at 350 Pa.

The background consists of spurious pulses occurring in coincidence with the SSD signal due to ionisation background inside the SEC and to delta rays that escape from the SV and enter inside the SEC. The measured cluster distribution m(n) (where n represents the number of ionisations detected in each event) can therefore be considered the sum of i(n), the distribution due to ionisations generated inside the SV, and b(n), the 'back-

![](./images/813336301246873600_1.jpg)

Figure 1. Schematic representation of the experimental set-up for track-nanodosimetry measurements (not to scale). See text for explanations.

---
Contact author E-mail: DENARDO@LNL.INFN.IT

L. DE NARDO, P. COLAUTTI, W. Y. BAEK, B. GROSSWENDT, A. ALKAA, P. SÉGUR and G. TORNIELLI

ground' distribution. Therefore m(n) is the result of a convolution operation:

$$
\mathrm{m}(\mathrm{n})=\sum_{\mathrm{n}^{\prime}=0}^{\mathrm{n}} \mathrm{i}\left(\mathrm{n}-\mathrm{n}^{\prime}\right) \mathrm{b}\left(\mathrm{n}^{\prime}\right) \tag{1}
$$

The total detection efficiency of electrons generated inside the SV, $\epsilon$, can be considered the product of two factors: the transfer efficiency of electrons from the SV inside the detector, $\epsilon_{\mathrm{sv}}$, and the detection efficiency of electrons that are inside the detector, $\epsilon_{\mathrm{I}}$:

$$
\epsilon=\epsilon_{\mathrm{sv}} \epsilon_{\mathrm{I}} \tag{2}
$$

i(n) and b(n), being due to electrons generated inside the SV and inside the detector respectively, are measured with different efficiencies: i(n) with efficiency $\epsilon$ and b(n) with efficiency $\epsilon_{\mathrm{I}}$. The background contribution can be evaluated by performing measurements with $\epsilon_{\mathrm{sv}}=0$, in which case i(n) reduces to the Dirac delta function and m(n) coincides with b(n).

Background distribution measurements were performed changing the voltage set of the electrodes defining the SV, inverting the electric field inside the SV with respect to the situation adopted for track-nanodosimetry measurements. The value of $\epsilon_{\mathrm{sv}}$ in these inverted-field measurements was about 1% and therefore very close to the requirement $\epsilon_{\mathrm{sv}}=0$. The value of $\epsilon_{\mathrm{I}}$ was the same during direct-field and inverted-field measurements and therefore background distributions were measured with the same efficiency as in track-nanodosimetry measurements. Semi-invariants are simple combinations of the moments of a distribution: the first semi-invariant is the mean, $\mathrm{m}_{1}$, and the second is the variance, $\sigma^{2}=\mathrm{m}_{2}-\left(\mathrm{m}_{1}\right)^{2}$. They add in a convolution and therefore it is possible to calculate the mean and the variance of the i(n) distribution after evaluation of the corresponding quantities for the m(n) (obtained during track-nanodosimetry measurements) and b(n) distribution (obtained during background measurements).

To test the reliability of experimental results, a Monte Carlo code was developed able to simulate both the production of secondary electrons by impact ionisation of alpha particles in propane at low gas pressure and the histories of these electrons down to 10 eV. For the alpha particles, this code is based on experimental ionisation cross sections of Rudd et $a l^{(3)}$ for protons at the same velocity, scaled by the square of the atomic number of the projectiles, and for electrons on experimental electron interaction cross sections as regards elastic scattering, impact excitation and impact ionisation. The simulation of the energy and angular distributions of electrons liberated by impact ionisation of the alpha particles is performed within the framework of the HKS model $^{(4)}$. To calculate the probability distribution of cluster size, the number of electrons with energies less or equal to 10 eV within the sensitive target volume are counted (for a detailed description of the code, see Reference 5).

# RESULTS AND DISCUSSION

Ionisation frequency distributions measured at different impact parameters d (distance between the track and the centre of the SV) point out a change in shape for d larger than the radius of the site, with a transition from asymmetric bell-shaped curves (with long tails on the high ionisation side) to monotonically decreasing ones (see Figure 2). This is the consequence of the fact that for d smaller than about 10 nm the fraction of alpha particles that produce measurable ionisation inside the SV is essentially equal to 1, whereas this fraction decreases rapidly beyond this distance. The cluster distributions of volumes that have experienced at least one event of ionisation (called critical volumes in microdosimetry) have been calculated. It was found that these conditional cluster distributions, for d larger than 20 nm, have a similar shape, regardless of distance from the site (Figure 3).

The first moment $\mathrm{m}_{1}$ (mean ionisation value), the ratio of the second moment to the first moment $\mathrm{m}_{2} / \mathrm{m}_{1}$ (formally equal to dose-mean lineal energy) of cluster distributions, and the first moment of conditional cluster distributions $\mathrm{m}_{1}{ }^{*}$ (conditional mean value) have been calculated. Both $\mathrm{m}_{1}$ and $\mathrm{m}_{2} / \mathrm{m}_{1}$ were calculated after subtracting the influence of background, which was possible due to the additive properties of semi-invariants in convolution. The same was not possible for the quantity $\mathrm{m}_{1}{ }^{*}$. The quantity $\mathrm{m}_{2} / \mathrm{m}_{1}$ is the same for conditional and normal distributions. Measurements at 300 Pa are compared with calculated values obtained at the same pressure in a 22 nm diameter sphere and assuming a detection efficiency of 25%.

Experimental and calculated $\mathrm{m}_{1}$ values have been plotted in Figure 4 as a function of d. The agreement between experimental and calculated data at 300 Pa is good apart for measurements performed for d less than

![](./images/813336301246873600_2.jpg)

Figure 2. Ionisation distributions for a 22.5 nm diameter site collected at different impact parameters, d, from the alpha particle track. Thick lines correspond to alpha tracks crossing the sensitive volume, thin lines to alpha tracks outside the sensitive volume.

# TRACK-NANODOSIMETRY OF AN ALPHA PARTICLE

10 nm. This is probably due to the fact that the capa- bility of the detector to resolve single electrons decreases with increasing size of the electron cluster.

In Figure 5 experimental values of $m_{2}/m_{1}$ and $m_{1}*$ as a function of d have been plotted. Just beyond the edge of the site both quantities go through a minimum. Beyond the minimum they become approximately independent of d. Monte Carlo calculations confirm the presence of this plateau region and of the minimum, but not in such a distinct form as the measurements. The reason for this might be the spatial resolution of the calculations. The minimum can be due to the fact that, at this distance from the track, several low energy sec- ondaries are detected which produce only a few ionis- ations into the site. Farther from the track, only a few more energetic secondaries can interact, producing a larger quantity of ionisations. In this region, the mean ionisation and its fluctuation in a critical volume appear to be independent of the energy of the delta ray inter- acting with the site.

![](./images/813336301246873600_3.jpg)

Figure 3. Conditional cluster distributions at 350 Pa collected at different impact parameters, d. Lines are smoothed best fit of experimental data. Error bars are the square root of the num- ber of events of a given cluster size, for data collected at $d=33$ nm.

![](./images/813336301246873600_4.jpg)

Figure 4. Mean ionisation value, $m_{1}$, as a function of the impact parameter, d. Open triangles: measurements at 350 Pa; solid triangles: measurements at 300 Pa; continuous line: Monte Carlo calculations at 300 Pa.

## CONCLUSIONS

Experimental data and Monte Carlo calculations sug- gest that ionisation fluctuations in nanometric volumes inside the delta ray cloud of an alpha particle are inde- pendent of the distance from the track. The experimental set-up is being modified to fit the accelerator beam line to be able in the future to perform track nanodosimetric measurements with particles of different charges and velocities.

## ACKNOWLEDGEMENTS

This research has been supported by the European Union with contracts FI3P-CT92-0041 and FI4P- CT96-0044 (Nuclear Fission Program).

![](./images/813336301246873600_5.jpg)

Figure 5. Mean parameters for conditional distributions, $m_{1}*$ (circles) and $m_{2}/m_{1}$ (triangles). Full symbols: measurements at 300 Pa; open symbols: measurements at 350 Pa; solid lines: Monte Carlo calculations at 300 Pa.

## REFERENCES

1. De Nardo, L., Alkaa, A., Khamphan, C., Conte, V., Colautti, P., Donà, G., Ségur, P. and Tornielli, G., *A Single-Electron Counter for Track-Nanodosimetry*. LNL-INFN (REP) 174/2001, 1–27 (2001).
2. De Nardo, L. , Alkaa, A., Khamphan, C., Conte, V., Colautti, P., Ségur, P. and Tornielli, G. *A Detector for Track-Nanodosimetry* (to be published) Nucl. Instrum. Methods a.
3. Rudd, M. E., Kim, Y. K., Madison, D. H. and Gallagher, J. W. *Electron Production in Proton Collisions: Total Cross Sections*. Rev. Mod. Phys. **57**, 965–994 (1985).

L. DE NARDO, P. COLAUTTI, W. Y. BAEK, B. GROSSWENDT, A. ALKAA, P. SÉGUR and G. TORNIELLI

4. ICRU. *Secondary Electron Spectra from Charged Particle Interactions*. ICRU Report 55 (Bethesda, MD: International Commission on Radiation Units and Measurements) (1996).

5. De Nardo, L., Conte, V., Baek, W. Y., Grosswendt, B., Colautti, P. and Tornielli, G. *Measurements and Calculations of Ionisation Cluster Distributions in 20 nm Size Site*, LNL-INFN (REP) 175/2001 (2001).

358