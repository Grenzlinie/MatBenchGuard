ORIGINAL PAPER

# Monte Carlo study of medium-energy electron penetration in aluminium and silver

Asuman Aydın,
Ali Peker

Abstract. Monte Carlo simulations are very useful for many physical processes. The transport of particles was simulated by Monte Carlo calculating the basic parameters such as probabilities of transmitted-reflected and angular-energy distributions after interaction with matter. Monte Carlo simulations of electron scattering based on the single scattering model were presented in the medium-energy region for aluminium and silver matters. Two basic equations are required the elastic scattering cross section and the energy loss. The Rutherford equation for the different screening parameters is investigated. This scattering model is accurate in the energy range from a few keV up to about 0.50 MeV. The reliability of the simulation method is analysed by comparing experimental data from transmission measurements.

Key words: angular distribution • electron • energy spectra • penetration • transmission

A. Aydın
Faculty of Arts and Sciences,
Balikesir University,
10145 Balikesir, Turkey,
Tel.: +90266 612 1000, Fax: +90266 612 1215,
E-mail: aydina@balikesir.edu.tr

A. Peker
Institute of Science and Technology,
Department of Physics,
Balikesir University,
10145 Balikesir, Turkey

Received: 15 July 2014
Accepted: 26 January 2015

## Introduction

Modelling of the motion of charged particles through solids is important in many areas of surface science and microelectronics. The electron microscopic and spectroscopic techniques are extensively used for surface and bulk analysis of materials. These tools use the various types of electron signals emitted from the sample irradiated by a beam of mono-energetic primary electrons for imaging of surface and struc- tural characterisation. These signals are secondary electrons (SEs) and backscattered electrons (BSEs) for scanning electron microscopy, Auger electrons for Auger electron spectroscopy and scanning Auger microscopy, elastic scattered electrons for elastic peak electron spectroscopy, inelastic scattered elec- trons for electron energy loss spectroscopy (EELS) and reflection EELS, and analytical electron micros- copy [1].

The study of electron transport is very important for a detailed understanding of a variety of physical processes involved in the electron solid interaction. Materials like aluminium are often used as foil win- dows or beam spreading foils. In such cases, it is necessary to know the transmission, reflection and absorption coefficients and the range distribution of electrons. Many researchers investigated earlier vari- ous aspects of electron penetration [2-4]. A lot of data are available [5-9] on transmission, reflection and absorption of electrons in materials.

The solid aim of Monte Carlo modelling of electron-
-solid interaction is to simulate the scattering pro-
cesses as accurately as possible in the medium-energy
range. In this study, the transmission, reflection and
absorption coefficients in a few hundred keV energy
regions are calculated using Monte Carlo methods
for aluminium and silver films. The calculations are
discussed in a comparison experimental result such
as the electron transmitted-reflected probabilities and
energy-angular distributions. Since the upper limit of
incoming electron energy is 0.50 MeV, we completely
ignore contributions coming from the bremsstrahlung
radiation, thus only elastic and inelastic atomic col-
lision processes are taken into account.

### Theoretical methods

#### Elastic scattering models

In the present study, the Rutherford elastic scatter-
ing with the different screening parameters on the
Monte Carlo simulation of electron beam penetra-
tion in aluminium and silver films for various thick-
ness and energies are investigated.

The screened Rutherford's cross sections based
on the Wentzel model, were frequently used in
Monte Carlo simulations due to its simplicity, it
is valid only for T > 10 keV energy electrons [10]
because it was derived from the first Born approxi-
mation. The relativistically corrected screened total
Rutherford elastic scattering cross section $\sigma_{e}$, is given
by the Eq. (1) [11]

$$
(1)\quad \sigma_{e}\left[\mathrm{cm}^{2}\right]=5.21 × 10^{-21} \frac{Z^{2}}{\mathrm{~T}^{2}} \frac{4 \pi}{\eta(1+\eta)}\left(\frac{\mathrm{T}+511}{\mathrm{~T}+1024}\right)^{2}
$$

where T is the electron kinetic energy in keV,
Z atomic number of the material, $\eta$ the screening
correction.

The screening parameter $\eta$ is difficult to predict
a value for theoretically and it can be determined
by different methods. For electron, it was calculated
by Molière [12] using the small-angle approxima-
tion, Nigam [13] using the first and second Born
approximation later modified by Bishop [14],
Thomas-Fermi [15]. For the present purposes, the
total Rutherford elastic scattering cross sections are
calculated by using each of the screening parameters,
which can be listed as follows:

Molière approximation,

$$
\begin{aligned}
&(2)\quad \eta_{\mathrm{M}}=\frac{Z^{2 / 3}}{4}\left(\frac{\alpha}{0.885}\right)^{2} \frac{1-\beta^{2}}{\beta^{2}}\left[1.13+3.76\left(\frac{\alpha Z}{\beta}\right)^{2}\right] \\
&\alpha=1 / 137, \quad \beta=v / c
\end{aligned}
$$

$$
(3)\quad \eta=k \frac{Z^{2 / 3}}{\mathrm{~T}}
$$

Bishop, $\eta_{\mathrm{B}}$ ($k = 3.46$); Thomas-Fermi, $\eta_{\mathrm{T-F}}$ ($k =$
4.34); Nigam, $\eta_{\mathrm{N}}$ ($k = 5.43$). Molière suggests the
use of Eq. (1) be restricted to energies above about
above $0.1\ Z^{4/3}$ keV. The screening parameters given

![](./images/814633767011352576_1.jpg)

Fig. 1. The screening parameters given in Eqs. (2) and (3)
as functions of energy.

in Eqs. (2) and (3) as functions of energy are shown
in Fig. 1.

The total Rutherford elastic scattering cross sec-
tion given in Eq. (1) are used. In this way, reasonable
angular distribution for the elastic scattering was
obtained. Figure 2a shows the variation of total elastic
scattering cross sections as a function of incident elec-
tron energy calculated by using Rutherford formula
with the above screening parameters for atomic silver.

We need an expression of the total elastic scatter-
ing cross section as a function of T in the range 50 eV
to 0.50 MeV. The total elastic scattering cross section
is a fast varying function of T, but the logarithm of
it is well behaving and can be expressed as a simple
power expansion. The expression is found as:

$$
(4)\quad \mu_{e}=e^{\sum_{i=1}^{5} p_{i} \ln (\mathrm{T})^{i-1}}
$$

where $\mu_{e}$; the macroscopic total elastic scattering
cross section [cm⁻¹], doing an accurate fit over (ln T,
$\ln \mu_{e}$) points and $p_{i}$ parameters.

Fits to the macroscopic total elastic scattering
cross section from Mayol & Salvat [16] and National
Institute of Standards and Technology (NIST) [17]
data were made by Monte Carlo simulation in Eq. (4).
These fits are also presented in Fig. 2b for compari-
son. Further, the total elastic scattering cross sections
are calculated using Rutherford scattering model with
$\eta_{\mathrm{N}}$ the screening parameter and are shown in Fig. 2b
along with the results reported by Mayol & Salvat
and NIST. It can be seen in Fig. 2b, for example,
the total elastic scattering cross section of 15 keV
energetic electrons impinging on silver is found to be
$\mu_{e}=2.0443 × 10^{6}\ \mathrm{cm}^{-1}$ from Eq. (1), $\mu_{e}=2.7793 ×$
$10^{6}\ \mathrm{cm}^{-1}$ from NIST, while the calculation of Mayol
& Salvat was $\mu_{e}=2.8210 × 10^{6}\ \mathrm{cm}^{-1}$.

#### Inelastic scattering models

Inelastic collisions are treated on the basis of gen-
eralised oscillator strength Liljequist model [18],
which gives inelastic mean free paths and stopping
powers in a good agreement with the experimental

![](./images/814633767011352576_2.jpg)

Fig. 2. Total cross sections for elastic electron scattering with silver atoms as a function of electron energy. (a) Calculations are based on the Rutherford Eq. (1) formula using Bishop's, Thomas-Fermi, Nigam's and Molière's screening parameters. (b) The present results are obtained based on the Mayol & Salvat model [16] and on the database of the National Institute of Standards and Technology (NIST) [17].

data. Gryzinski's semi-empirical expression [19] is used to simulate the energy loss due to inelastic scattering, and Liljequist model to calculate the total inelastic scattering cross section. The detailed description of the Monte Carlo code and the calculation of cross sections were reported elsewhere [20-23]. The model is based on the combined use of Gryzinski's inner-shell electron excitation function in inelastic scattering processes. Then the energy loss in the inelastic scattering process using Gryzinski's excitation function was sampled.

In this study, the macroscopic total inelastic scattering cross section values are calculated with the Liljequist models, for several values of T in the range 80 eV - 100 keV. The expression given in Eq. (4) is used to calculate for the macroscopic total inelastic scattering cross sections. Figure 3 shows the variation of total inelastic scattering cross sections as a function of incident electron energy calculated using Liljequist models in comparison with the results of Tanuma *et al.* from optical data [24], Jablonski [24] and Dolinski [24] experimental data, Powell &

![](./images/814633767011352576_3.jpg)

Fig. 3. Total inelastic scattering cross sections as a function of incident electron energy.

Jablonski [24] for inelastic scattering using. Inset of Fig. 3 shows the variation of total inelastic scattering cross sections calculated using Liljequist models are compared to the results of Penn [25].

In summary, the Monte Carlo simulation of the scattering processes of penetrating electrons in solids was described. We investigated the influence of fundamental models of electron elastic collision, that is, the Rutherford formula and the screening parameters, Mayol & Salvat and NIST on the Monte Carlo simulation of medium-energy electron transport in aluminium and silver. Using the Monte Carlo code constructed in this study, the systematic calculations of both the distributions of energy depositions and the transmitted-reflected probabilities for medium-energy electrons in aluminium and silver at different thicknesses are performed.

Treatment of the elastic and inelastic collisions, which were explained above, contains several approximations. As a result, the macroscopic total cross sections given by Eq. (4) could have uncertainties, which are estimated to be of the order of 10-20%. These uncertainties give us the freedom to optimise the total cross section values to obtain results, which are as close as possible to the experimental values.

Elastic and inelastic scattering are assumed to produce angular distributions. The computer codes were written for films of various thicknesses and mono-energetic electron beams irradiated to solid target in the positive z direction. All results presented in each simulation run are obtained with normal incidence of electrons. The electrons in films of various thicknesses were followed until they were transmitted or slowed down below 50 eV. Typically, 10 000 such electron trajectories are followed to produce a statistically reasonable transmission rate for incident energy.

## Results and discussions
### Transmission rate

The transmissions of mono-energetic beams of electron and positron with energies up to 960 keV were

measured in Al, Sn, Ag, Au and Pb by Seliger [26]. To examine the present Monte Carlo approach, the experimental data of Seliger were used. No experi- mental and/or theoretical treatments of the energy and angular distributions of transmitted-reflected electrons in a few hundred kiloelectron-volts energy regions for aluminium and silver have been found in the literature yet.

We compared the screening parameters for the best shape of the angular distribution of elastically scattered electrons. The angular dependence of the screened Rutherford cross section is given by the fac- tor $\lambda/(1-\cos\theta+2\eta)^2$. We also obtained reasonable results with Nigam parameter ($\eta_{\mathrm{N}},k=5.43$) for silver film in the a few hundred kiloelectron-volts energy region. For example, the transmission probability was found to be 0.748 and 0.683 by using Molière and Ni- gam the angular distribution screenings, respectively, while the measurement of Seliger [26] was 0.690 for silver $5\ \mathrm{mg{\cdot}cm^{-2}}$ thickness at 159 keV energy.

![](./images/814633767011352576_4.jpg)

Fig. 4. (a), (b) The calculated transmission probabilities for various energies and foil thicknesses are shown to- gether with Seliger's experimental results for Al and Ag. (c) Relative proportions electrons transmitted (full curve) and reflected (dashed curve) as a function of thicknesses for Al film.

Monte Carlo calculations for the transmission rate of 159–336 keV electrons in thin aluminium and silver films were performed for comparing the total Rutherford elastic scattering cross sections in Eq. (1), Mayol & Salvat [16] and NIST [17] and the experimental results already published Seliger [26]. The results calculated from the Monte Carlo code are shown in Fig. 4(a,b) for aluminium and silver films, respectively. Relative proportions at 159 keV energy transmitted and reflected for the various thicknesses aluminium films are shown in Fig. 4c. The calculated transmission probabilities with Mayol & Salvat [16] and NIST [17], the total elastic scattering cross sections in aluminium and silver films are in good agreement with those of Seliger [26]. For instance, in this figure, the cal- culated transmission probability was found to be 0.193 and 0.217 Mayol & Salvat and NIST the total elastic scattering cross section, respectively, while the measurements of Seliger was 0.180 for silver $55\ \mathrm{mg{\cdot}cm^{-2}}$ thickness at 336 keV energy. The calcu- lated transmission probabilities are not very close to the results of Seliger when used Eq. (1) for the total Rutherford elastic scattering cross section.

## Energy and angular distributions

The energy and angular distributions of the transmit- ted and reflected electrons for various thicknesses of aluminium and silver films were calculated for the first time in medium-energy region. Figure 5 shows typical energy distribution of the transmitted and reflected electrons in thin aluminium film at 159 keV energy. Figure 6 shows typical dependence of trans- mitted energy distribution on silver film thicknesses at 336 keV electron energy. In Fig. 6, it is noticed that half widths of the theoretical distributions. Figure 7 shows comparison of the energy spectra of transmitted electrons in aluminium and silver films for $250\ \mathrm{keV}$ energy and $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness.

The angular distribution of transmitted and re- flected electrons was also calculated in the present Monte Carlo calculation for thin aluminium and silver films. In practice, the computer program has provided both angular and energy spectra of the transmitted and reflected electrons. Figure 8 gives the angular distribution of transmitted and reflected electrons for $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness aluminium film at 159 keV energy. In addition, the theoretical angular distributions of transmitted electrons for various thicknesses of silver films at 336 keV are indicated in Fig. 9. Figure 10 shows comparison of the angular distribution of transmitted electrons in aluminium

and silver films for 250 keV energy and $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness.

![](./images/814633767011352576_5.jpg)

Fig. 5. Energy spectra of the transmitted and reflected electrons in $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness Al film at 159 keV energy.

![](./images/814633767011352576_6.jpg)

Fig. 6. Energy spectra of transmitted electrons for Ag films of various thicknesses at 336 keV.

![](./images/814633767011352576_7.jpg)

Fig. 7. Energy spectra of transmitted electrons in Al and Ag films for 250 keV energy and $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness.

![](./images/814633767011352576_8.jpg)

Fig. 8. The angular distributions of transmitted and reflected electrons in $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness Al film at 159 keV energy.

![](./images/814633767011352576_9.jpg)

Fig. 9. The angular distributions of transmitted electrons in Ag films at 15, 30 and $60\ \mathrm{mg{\cdot}cm^{-2}}$ thicknesses at 336 keV energy.

![](./images/814633767011352576_10.jpg)

Fig. 10. Comparison of the angular distribution of transmitted electrons in Al and Ag films for 250 keV energy and $20\ \mathrm{mg{\cdot}cm^{-2}}$ thickness.

## Conclusions

The present approach describes the penetration of the primary electrons for aluminium and silver films with considerable success. A comparatively simple model gives a reasonable description of electron scattering for energies ranging from several tens electron-volt to a few hundred kiloelectron-volts. The scattering processes involve elastic and inelastic scattering. The calculation provided the energy spectra and angular distributions of transmitted and reflected electrons for aluminium and silver by Monte Carlo approach. Simulation results for transmission experiments are presented and compared with experimental data for different electron energies. Such a Monte Carlo procedure can be efficiently used to simulate the experimental conditions encountered in surface electron spectroscopy.

## References

1. Reimer, L. (2000). Scanning electron microscopy: Physics of image formation and microanalysis. Meas. Sci. Technol., 11, 1826. DOI: 10.1088/0957-0233/11/12/703.
2. Spencer, L. V. (1955). Theory of electron penetration. Phys. Rev., 98(6), 1597-1615.
3. Kanaya, K., & Okayama, S. (1972). Penetration and energy-loss theory of electrons in solid targets. J. Phys. D-Appl. Phys., 5, 43-58.
4. Shimizu, R., Kataoka, Y., Ikuta, T., Koshikawat, T., & Hashimoto, H. (1976). A Monte Carlo approach to the direct simulation of electron penetration in solids. J. Phys. D-Appl. Phys., 9, 101-114.
5. Adesida, I., Shimizu, R., & Everhart, T. E. (1980). A study of electron penetration in solids using a direct Monte Carlo approach. J. Appl. Phys., 51(11), 5962-5969.
6. Dep, P., & Nundy, U. (1988) A study of the penetration of electrons in compounds by Monte Carlo calculations. J. Phys. D-Appl. Phys., 21, 763-767.
7. Shimizu, R., & Ze-Jun, D. (1992). Monte Carlo modeling of electron-solid interactions. Rep. Prog. Phys., 55, 487-531.
8. Ivin, V. V., Silakov, M. V., Babushkin, G. A., Lu, B., Mangat, P. J., Nordquist, K. J., & Resnick, D. J. (2003). Modeling and simulation issues in Monte Carlo calculation of electron interaction with solid targets. Microelectron. Eng., 69, 594-605.
9. Ding, Z. J., Salma, K., Li, H. M., Zhang, Z. M., Tokesi, K., Varga, D., Toth, J., Goto, K., & Shimizu, R. (2006). Monte Carlo simulation study of electron interaction with solids and surfaces. Surf. Interface Anal., 38, 657-663.

10. Dapor, M. (1992). Monte Carlo simulation of backscattered electrons and energy from thick targets and surface films. Phys. Rev. B, 46(2), 618-625.
11. Joy, D. C. (1991). An introduction to Monte Carlo simulations. Scanning Microscopy, 5(2), 329-337.
12. Molière, G. (1947). Theory of scattering of fast charged particles. I. Single scattering in a screened Coulomb field. Z. Naturforsch. A, 2, 133-145.
13. Nigam, B. P., Sundaresan, M. K., & Wu, T. Y. (1959). Theory of multiple scattering second Born approximation and corrections to Moliere's work. Phys. Rev., 115, 491-502.
14. Joy, D. C. (1955). Monte Carlo modeling for electron microscopy and microanalysis. New York: Oxford University Press.
15. Kyriakou, I., Emfietzoglou, D., Nojeh, A., & Moscovitch, M. (2013). Monte Carlo study of electron-beam penetration and backscattering in multi-walled carbon nanotube materials: The effect of different scattering models. J. Appl. Phys., 113, 084303-11.
16. Mayol, R., & Salvat, F. (1997). Total and transport cross sections for elastic scattering of electrons by atoms. Atom. Data Nucl. Data Tables, 65, 55-154.
17. Jablonski, A., Salvat, F., & Powell, C. J. (2010). NIST electron elastic-scattering cross-section database - Version 3.2. National Institute of Standards and Technology Standard Reference Data Program. Gaithersburg, MD: National Institute of Standards and Technology.
18. Liljequist, D. (1983). A simple calculation of inelastic mean free path and stopping power for 50 eV-50 keV electrons in solids. J. Phys. D-Appl. Phys., 16, 1567-1582.
19. Gryzinski, M. (1965). Two-particle collisions. I. General relations for collisions in the laboratory system, two-particle collisions. II. Coulomb collisions in the laboratory system of coordinates, classical theory of atomic collisions. I. Theory of inelastic collisions. Phys. Rev., 138, A305, A322, A336.
20. Ozmutlu, E. N., & Aydin, A. (1994). Monte-Carlo calculations of 50 eV-1 MeV positrons in aluminum. Appl. Radiat. Isot., 45, 963-971.
21. Aydın, A. (2000). Monte Carlo calculations of positron implantation profiles in silver and gold. Radiat. Phys. Chem., 59, 277-280.
22. Aydın, A. (2005). Monte Carlo calculations of low energy positrons in silicon. Nukleonika, 50(1), 37-42.
23. Aydın, A. (2009). Monte Carlo calculations of electrons in aluminum. Appl. Radiat. Isot., 67, 281-286.
24. Powell, C. J., & Jablonski, A. (2010). NIST electron inelastic mean free path database. Version 1.2. Gaithersburg, MD: National Institute of Standards and Technology. (SRD 71).
25. Penn, D. R. (1987). Electron mean free path calculations using a model dielectric function. Phys. Rev. B, 35, 482-486.
26. Seliger, H. H. (1955). Transmission of positrons and electrons. Phys. Rev., 100(4), 1029-1037.