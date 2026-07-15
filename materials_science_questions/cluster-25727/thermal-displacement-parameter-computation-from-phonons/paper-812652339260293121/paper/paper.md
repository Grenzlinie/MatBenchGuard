PHYSICAL REVIEW RESEARCH 2, 023034 (2020)

# High pressure melt curve of iron from atom-in-jellium calculations

Damian C. Swift, Thomas Lockard, Raymond F. Smith, Christine J. Wu, and Lorin X. Benedict

Lawrence Livermore National Laboratory, 7000 East Avenue, Livermore, California 94551, USA

![](./images/812652339260293121_1.jpg)
(Received 13 June 2019; accepted 6 January 2020; published 10 April 2020)

Although usually considered as a technique for predicting electron states in dense plasmas, atom-in-jellium calculations can be used to predict the mean displacement of the ion from its equilibrium position in colder matter as a function of compression and temperature. The Lindemann criterion of a critical displacement for melting can then be employed to predict the melt curve, normalizing, for instance, to the observed melt temperature or to more direct simulations, such as molecular dynamics (MD). This approach reproduces the high pressure melting behavior of Al as calculated using the Lindemann model and thermal vibrations in the solid. Applied to Fe, we find that it reproduces the limited-range melt curve of a multiphase equation of state (EOS) and the results of ab initio MD simulations and agrees less well with a Lindemann construction using an older EOS. The resulting melt curve lies significantly above the older melt curve for pressures above 1.5 TPa but is closer to recent ab initio MD results and extrapolations of an analytic fit to them. This paper confirms the importance of core freezing in massive exoplanets, predicting that a slightly smaller range of exoplanets than previously assessed would be likely to exhibit dynamo generation of magnetic fields by convection in the liquid portion of the core.

DOI: 10.1103/PhysRevResearch.2.023034

## I. INTRODUCTION

Thousands of exoplanets have been discovered [1], most around stars of different types than the sun and with orbits and mean mass density of a much wider variety than the planets of the solar system. These observations lead to questions about the uniqueness of the solar system and the earth, including whether other planets can support life.

All known forms of life require liquid water (although extremophiles can survive frozen or even in vacuum when dormant [2]), and almost none can tolerate ionizing radiation at the levels typical of the solar wind and flares. Earth's magnetic field shields the atmosphere from energetic charged particles, and so a magnetic field is usually considered a prerequisite for life [3].

Earth's magnetic field is believed to be induced by convection in the liquid Fe outer core [4], therefore, an important indication of the habitability of rocky "superearth" exoplanets is whether the core is likely to possess a liquid layer. This depends on the circumstances of each particular exoplanet, including its composition—influencing the specific Fe alloys in the core as well as the proportion of silicates to Fe—and history, which depends on the type of star it orbits and interactions with other exoplanets in the system, but the relevent material physics property is the melt curve of Fe.

A large number of exoplanets have been observed with mass and radius indicating rocky structures analogous to earth [5], and there is an increasing body of research predicting whether they are likely to contain liquid Fe in the core, assuming compositions similar to earth [6–9]. Even neglecting the variation and uncertainty in composition, different studies have reached inconsistent conclusions because of our uncertain knowledge of the properties of Fe at elevated pressures and temperatures, in particular, the relationship between the planetary temperature profile and the melt curves of the core and mantle [7,10]. The temperature profile in the earth's core crosses the melt curve of Fe at $\sim$330 GPa [11,12]. The magnetodynamo is thought to be driven by the latent heat of solidification as the inner core grows [13] and may be affected by the expulsion of lighter impurity elements, such as Si and S, from the solid; the impurity composition is thought to vary even between the rocky planets of our solar system [14,15]. Conclusions vary between inferring that planets larger than earth would have a completely solid core and, hence, no magnetic field [6] to predictions that a liquid outer core could be present in planets up to five times the mass of the earth [7]. Theoretical predictions of the melt curve of Fe [16,17] lie significantly higher than Lindemann law extrapolations from low-pressure data [6], suggesting a smaller possible population of superearths with a magnetic field. However, these conclusions depend on the temperature profile, which depends also on the properties of the mantle [9]. As well as indicating a wider range of occurrence of liquid Fe, it has been suggested that convection in the core could be driven alternatively by convection in the mantle [9].

The melt curve is defined most rigorously by thermodynamic construction, matching the Gibbs free energy of the liquid and solid phases. The equation of state (EOS) of solid phases can be determined theoretically using electronic structure to infer the free energy as a function of mass density and temperature, which may be decomposed as a cold compression curve plus phonon modes and possibly

*dswift@llnl.gov

Published by the American Physical Society under the terms of the Creative Commons Attribution 4.0 International license. Further distribution of this work must maintain attribution to the author(s) and the published article's title, journal citation, and DOI.

2643-1564/2020/2(2)/023034(5)
023034-1
Published by the American Physical Society

electron excitations. These contributions can be calculated from static lattice simulations, although, in some cases, it has been shown that the phonon and electron excitations may in- teract significantly, necessitating temperature-dependent cor- rections, such as anharmonic phonons [18]. The equivalent calculations for the free energy of the fluid require quantum molecular dynamics (QMD) in which the kinetic motion of an ensemble of atoms is simulated with the instantaneous forces on the ions found from electronic structure calculations [19]. QMD can also be used to calculate the EOS of the solid directly, which automatically incorporates interactions between electronic and ionic excitations, but, since the ion motion is classical, makes it more difficult to account for zero-point motion of the ions. QMD can be used to deduce the melt curve directly by performing simulations comprising regions of solid and fluid in contact. In such simulations, one phase grows at the expense of the other, and each point on the melt curve is identified by adjusting the state until the interface is approximately stationary. The state in the simulation can be adjusted until the phases remain in equilibrium, identifying a point on the melt curve. Either procedure is computationally expensive, requiring $o(10^{16})$ or more floating-point operations to identify a state on the melt curve, equivalent to thousands of CPU hours per state. These calculations are typically more expensive at lower compressions, and it is common for studies to focus only on a narrow range of pressures.

As melt curves are challenging to predict theoretically, particularly, over a wide pressure range, many studies rely on melt curves deduced much more simply, such as by the Lin- demann criterion applied to wide-range semiempirical EOS [20–23]. Typically, an EOS is constructed using adjustable models of the cold curve and ion-thermal excitations, and the melt curve is constructed from the Lindemann law with the displacement criterion chosen to pass through available melting data, such as the observed melt temperature at 1 atm. In practice, the Lindemann law is solved as a first-order differential equation in mass density, relating the melt temper- ature to the ion-thermal Grüneisen parameter [24,25]. Usually, the highest-compression data available lie along the principal shock Hugoniot. The split between cold and thermal pressure is not constrained, and the melt curve at high pressures, therefore, depends on the extrapolation of empirical functions for the cold curve, Debye temperature, and Grüneisen pa- rameter. It is also possible to estimate the ion-thermal free energy from the cold curve, for instance, by estimating the Debye temperature from the bulk modulus [26], although this approach has been found to become less accurate as pressure increases; the melt curve can then be estimated again using the Lindemann criterion [20]. Such EOS and melt curves are used in the design and interpretation of expensive high energy density experiments, such as those at the National Ignition Facility, which often rely on predictions of whether or not components melt [27].

Recent QMD and path-integral Monte Carlo results have indicated that the simpler approach of calculating the elec- tron states for a single atom in a spherical cavity within a uniform charge density of ions and electrons, representing the surrounding atoms, reproduces their more rigorous EOS for dense plasmas [28,29]. This atom-in-jellium approach [30] was developed originally to predict the electron-thermal energy of matter at high temperatures and compressions [21] as an advance over the primitive electronic models neglecting any treatment of shell structure as in Thomas-Fermi and related approaches [31]. A development of atom-in-jellium method was used to predict ion-thermal properties [32] and seems to give reasonable EOS in the fluid regime down, at least, as far as the melt curve, for a wide range of elements [33]. In a further development of the method, we have used Hellmann-Feynman calculations of the restoring force for per- turbations of the ion from its equilibrium position to predict the transition from bound to free ions, resulting in a reduc- tion in the ion-thermal heat capacity from $3k_{B}$ per atom to $3k_{B}/2$ per atom, by considering the mean displacement of the ions [34].

In this paper, we use the atom-in-jellium displacement model developed previously to estimate the melt curve of elements efficiently over a wide range of pressures and assess the astrophysical implications compared with previous melt curve calculations for Fe.

## II. ATOM-IN-JELLIUM IONIC DISPLACEMENT MODEL

In the ion-thermal model developed for use with atom- in-jellium calculations [32], perturbation theory was used to calculate the Hellmann-Feynman force on the ion when dis- placed from the center of the cavity in the jellium. Given the force constant $k=-\partial f/\partial r$, the Einstein vibration frequency $\nu_{e}=\sqrt{k/m_{a}}$ was determined, where $m_{a}$ is the atomic mass, and, hence, the Einstein temperature $\theta_{E}=\hbar\nu_{e}/k_{B}$. The Debye temperature $\theta_{D}$ was inferred from $\theta_{E}$ by equating either the ion-thermal energy or the mean displacement $u$. We used the mean fractional displacement with respect to the Wigner-Seitz radius $u_{f}\equiv u/r_{WS}$ as a measure of ionic freedom, describing the decrease in ionic heat capacity from 3 to $\frac{3}{2}k_{B}$ per atom as the ions become free as temperature increases in the fluid [34].

Predictions of the variation of $\theta_{D}$ with temperature as well as density are unusual compared with the normal use in constructing EOS. This behavior adds generality and is likely to make a Debye-based EOS construction valid over a wider range of states. The treatment of ionic freedom extended the atom-in-jellium technique to describe the variation of the ion-thermal heat capacity into regimes where the electronic treatment is more appropriate.

The use of fractional displacements to predict ionic free- dom is reminiscent of the semiempirical Lindemann melting criterion [24], which holds that melting occurs when the mean displacement of the atoms reaches some fixed fraction of the interatomic spacing. This fraction is approximately constant for a given material but varies somewhat with composition; the value is found to vary between around 0.1 and around 0.3. The variation in fractional density change from solid to liquid is much less than this range, so it is reasonable to perform the same calculation using the interatomic spacing in the liquid rather than in the solid.

With such a wide variation in fractional displacements inferred to induce melting, this method is not predictive by itself. For substances with a simple phase diagram, melting at one atmosphere could be used to constrain the critical value of $u_{f}$. For substances that exhibit multiple solid phases with significant volume changes, the melt curve is typically
023034-2

![](./images/812652339260293121_2.jpg)

FIG. 1. Contours of mean fractional displacement and melt curves for aluminum extracted from EOS models [20,37]. Melt curves and one atmosphere melting are indicated. The other curves are contours of mean fractional displacement with relevant values marked. Localized extrema and perturbations in the contours reflect sensitivity to numerical convergence in the Hellmann-Feynman force calculation.

perturbed by the free-energy variations in the solid. Thus, we would anticipate that the atom-in-jellium displacement tech- nique could capture the variation in the melt curve for melting from each solid phase away from the phase boundaries but would require normalization for each solid phase, e.g., to QMD simulations.

However, the atom-in-jellium calculations are much faster than QMD, so a relatively small number of QMD simula- tions could be used to constrain finely resolved and wide- ranging atom-in-jellium calculations. Furthermore, the atom- in-jellium calculations are fast enough that all electrons can be treated explicitly under all circumstances, in contrast to QMD simulations where the inner electrons are typically subsumed into a pseudopotential; atom-in-jellium calculations can be used to extrapolate to much lower and higher densities than are tractable with QMD.

### III. MELT CURVE OF ALUMINUM

At atmospheric pressure, Al melts at 933.47 K with a liquid density of $2.375\ \text{g/cm}^3$ [35,36]. Modified Lindemann melt curves have been developed to be consistent with an analytic Grüneisen EOS [20] and a wider-ranging tabular EOS [37]; the melt curves were consistent with each other. Atom- in-jellium calculations were performed for $10^{-4}$-$10^3\rho_0$ with 20 points per decade and $10^{-3}$-$10^5$ eV with ten points per decade. A nonimaginary Einstein frequency was calculated for $\rho > 1.3\ \text{g/cm}^3$, indicating that the atoms were not free, allowing the melt curve to be estimated in this range. The melt curves corresponded to $u_f \simeq 0.1$ for one atmosphere melting, rising to $\simeq 0.13$ at $5\ \text{g/cm}^3$ (1 eV) and then following within 0.01 of this displacement contour to the maximum density considered (Fig. 1).

This result suggests that fractional displacements $u_f$ de- rived from atom-in-jellium calculations can be used to predict the melt curve with deviation from a constant $u_f$ becoming significant around ambient density where the inaccuracies in atom-in-jellium electronic states result also in significant inaccuracies in the EOS.

![](./images/812652339260293121_3.jpg)

FIG. 2. Contours of mean fractional displacement, melt curves for iron extracted from EOS models [38,39], and QMD melting predictions [16]. The bold contour is the atom-in-jellium curve at mean fractional displacement of 0.12, proposed as the improved high pressure melt curve.

### IV. MELT CURVE OF IRON

Because of the solid-solid phase transitions in Fe, we would not expect the atom-in-jellium fractional displacements to be constant between and around the triple points with the liquid. A wide-ranging Lindemann melt curve was de- veloped to be consistent with a tabular EOS that did not treat the solid phase transitions [38]. A multiphase EOS was developed describing and extrapolating from experimental measurements and treating solid phases $\alpha$, $\gamma$, $\epsilon$, and $\delta$ as well as the liquid/vapor region [39]. Phase boundaries were extracted from this tabular EOS by locating anomalies in heat capacity and Grüneisen parameter; the melt transition was evident up to a density around $20\ \text{g/cm}^3$. QMD studies of the melt curve have also been performed at $13$-$20\ \text{g/cm}^3$ [16]. The multiphase melt curve was similar to the QMD results; the older melt curve passed through the others around $20\ \text{g/cm}^3$ but varied significantly more slowly with com- pression. Atom-in-jellium calculations were performed over the same compression and temperature range as for Al and predicted a physical Einstein temperature for $\rho > 4\ \text{g/cm}^3$. One atmosphere melting corresponds to $u_f \simeq 0.17$. Above $12\ \text{g/cm}^3$, the multiphase and QMD simulations were very close to the $u_f = 0.12$ contour. Thus, we propose the $u_f = 0.12$ contour as an improved melt curve to higher pressure (Fig. 2).

Multiatom electronic structure calculations have been used to predict solid phase stability in Fe at high pres- sure [18]. These indicated a transition from hcp to fcc at $33.9\ \text{g/cm}^3$ (6 TPa) and fcc to bcc at $66.7\ \text{g/cm}^3$ (38.3 TPa). The energy difference between hcp and fcc is relatively small, so this transition is unlikely to affect the melt curve much. The transition to bcc could be associated with an increase in the slope of the melt curve.

![](./images/812652339260293121_4.jpg)

FIG. 3. Melt curves for iron as a function of pressure also showing heated diamond-anvil cell (DAC) measurements at low pressures [40].

Taking the set of $\{\rho, T\}$ points along the contour, thermodynamic quantities were calculated for the melt curve by interpolation from the atom-in-jellium EOS. Again, because of the relative inaccuracy of the atom-in-jellium method at densities near ambient, one would not expect the pressure to be accurate in this regime. However, the pressure was found to match the QMD simulations to within $10\%$ and is likely to be, at least, as accurate at higher pressures. The atom-in-jellium melt curve is significantly higher than a Lindemann-based prediction using plane-wave pseudopotential calculations of vibrational frequencies [18] but is reasonably consistent with the same researcher's Simon fit to the QMD curve [9]. The latter extrapolates from the QMD calculations, which define four points ranging $\sim$0.35-1.5 TPa with uncertainties in temperature which, strictly, give a significant variation in the extrapolation to higher pressures. The atom-in-jellium calculation provides some validation of this extrapolated melt curve but rises above it by $10\%$ at a pressure of 10 TPa, suggesting that a slightly smaller proportion of exoplanets is likely to possess a magnetic field induced by convection in the core (Fig. 3).

The atom-in-jellium melt curve could not be fit over its full range using a function of the Lindemann or Simon type. Over the range of 1-100 TPa, thought to be most relevant to giant exoplanets [18], the melt curve could be reproduced to within $3\%$ by the Simon equation [41] with parameters as follows:

$$
T_{m}=6279 \mathrm{~K}\left(\frac{p}{346 \mathrm{GPa}}\right)^{0.552}. \tag{1}
$$

The range of the fit can be broadened to 0.5-650 TPa by modifying the exponent,

$$
T_{m}=494 \mathrm{~K}\left(\frac{p}{3 \mathrm{GPa}}\right)^{0.543-p /\left(4 \times 10^{7} \mathrm{GPa}\right)}. \tag{2}
$$

## V. DISCUSSION

The atom-in-jellium model was developed for application to warm dense matter, and it is surprising that it can be used to predict melt curves. To emphasize, this is a generalization of the Lindemann model, based on the empirical observation that melting occurs at a roughly constant mean displacement of the ions from equilibrium, rather than any more rigorous a representation of the free-energy difference between the solid and the liquid. As used here, predicted melt curves are also subject to the inherent approximations of the average-atom treatment and of the first-order perturbation approach to calculating the Einstein temperature. However, the procedure used here for calculating the melt curve is significantly different than previous approaches: rather than integrating an equation involving the ion-thermal Grüneisen parameter (which was not even calculated in constructing the atom-in-jellium EOS, although it can be deduced from the ionic component of the EOS by differentiation), the mean amplitude of vibrations used in computing the Debye frequency was used directly to determine the melt curve with no integration required and, thus, no accumulation of error with increasing compression. The atom-in-jellium melt curves agree encouragingly well with experimental measurements and more rigorous calculations over the narrower ranges where they exist and are likely to be more accurate than extrapolations of empirical EOS or melt constructions and so should be useful for high pressure situations including massive exoplanets, white and brown dwarfs, and high-energy density experiments.

The melt curve proposed here supports the previous conclusion [9] that the size of the frozen core of Fe planets should grow monotonically with planetary mass, at least, for planets of broadly constant composition. The frozen core would grow much less and possibly shrink depending on the scenario assumed using the earlier melt curve for Fe [38]. This observation highlights the potential importance of convection in the mantle as a mechanism for generating magnetic fields in massive or silicate-rich exoplanets. This modified melt curve is important in assessing whether specific detailed scenarios of planetary formation and evolution are potentially compatible with the occurrence of extraterrestrial life.

## VI. CONCLUSIONS

The Einstein oscillator estimates from the atom-in-jellium model of warm dense matter were used to calculate the mean thermal displacement of ions as a function of mass density and temperature. Expressed as a fraction of the Wigner-Seitz radius as a measure of interatomic spacing, contours of this fractional displacement were found to reproduce experimental measurements and more rigorous calculations of the melt curve of Al and Fe except near solid-solid phase transitions. Having established the mean fractional displacement corresponding to melting, the calculated contour can be used to predict the melt curve to much higher pressures with a sounder physical basis than extrapolations based on empirical fits to the EOS of the solid and liquid phases or to the melt curve itself, which are the methods generally used.

For Fe, the atom-in-jellium melt curve broadly confirms and refines a recent prediction based on an empirical extrapolation of QMD calculations. This result shows the importance of the high pressure melt curve to the range of conditions in which convection can occur in the core of massive exoplanets and, therefore, in which magnetic fields can be generated by the core dynamo process with implications for the population of candidate life-bearing planets.

## ACKNOWLEDGMENTS

The authors would like to thank R. Kraus for useful discussions. J. D. Johnson and S. Crockett provided copies of the SESAME equation of state library. G. I. Kerley provided his equation of state for Fe. This work was performed under the auspices of the US Department of Energy under Contract No. DE-AC52-07NA27344.

[1] *The Extrasolar Planets Encyclopedia*, edited by J. Schneider et al. http://exoplanet.eu.

[2] L. J. Rothschild and R. L. Mancinelli, *Nature* (London) **409**, 1092 (2001).

[3] D. Sasselov *The Life of Super-Earths* (Basic, New York, 2011).

[4] V. Dehant *et al.*, *Space Sci. Rev.* **129**, 279 (2007).

[5] D. D. Sasselov, D. Valencia, and R. J. O’Connell, *Phys. Scr.* **T130**, 014035 (2008).

[6] D. Valencia, R. O’Connell, and O. Sasselov, *Icarus* **181**, 545 (2006).

[7] C. Sotin, O. Grasset, and A. Mocquet, *Icarus* **191**, 337 (2007).

[8] E. Gaidos, C. P. Conrad, M. Manga, and J. Hernlund, *Astrophys. J.* **718**, 596 (2010).

[9] L. Stixrude, *Philos. Trans. R. Soc.*, A **372**, 20130076 (2014).

[10] D. Valencia, R. J. O’Connell, and D. Sasselov, *Astrophys. Space Sci.* **322**, 135 (2009).

[11] A. M. Dziewonski and F. Gilbert, *Nature* (London) **234**, 465 (1971).

[12] A. M. Dziewonski and O. L. Anderson, *Phys. Earth Planet Inter.* **25**, 297 (1981).

[13] D. Gubbins, B. Sreenivasan, J. Mound, and S. Rost, *Nature* (London) **473**, 361 (2011).

[14] S. J. Weidenschilling, *Icarus* **35**, 99 (1987).

[15] A. Treiman, M. Drake, M. Janssens, R. Wolf, and M. Ebihara, *Geochim. Cosmochim. Acta* **50**, 1071 (1986).

[16] G. Morard, J. Bouchet, D. Valencia, S. Mazevet, and F. Guyot, *High Energy Density Phys.* **7**, 141 (2011).

[17] J. Bouchet, S. Mazevet, G. Morard, F. Guyot, and R. Musella, *Phys. Rev. B* **87**, 094102 (2013).

[18] L. Stixrude, *Phys. Rev. Lett.* **108**, 055505 (2012).

[19] L. Collins, I. Kwon, J. Kress, N. Troullier, and D. Lynch, *Phys. Rev. E* **52**, 6202 (1995).

[20] D. J. Steinberg, Lawrence Livermore National Laboratory Report No. UCRL-MA-106439 change 1, 1996 (unpublished).

[21] S. P. Lyon and J. D. Johnson, Los Alamos National Laboratory Report No. LA-UR-92-3407, 1992 (unpublished).

[22] R. M. More, K. H. Warren, D. A. Young, and G. B. Zimmerman, *Phys. Fluids* **31**, 3059 (1988).

[23] For example, P. A. Sterne *et al.*, *J. Phys.: Conf. Ser.* **717**, 012082 (2016).

[24] F. A. Lindemann, *Phys. Z.* **11**, 609 (1910).

[25] J. J. Gilvarry, *Phys. Rev.* **102**, 308 (1956).

[26] V. L. Moruzzi, J. F. Janak, and K. Schwarz, *Phys. Rev. B* **37**, 790 (1988).

[27] For example, R. Rygg *et al.* [Rev. Sci. Instrum. (to be published)]; J. McNaney *et al.* (unpublished); A. Krygier *et al.*, *Phys. Rev. Lett.* **123**, 205701 (2019).

[28] L. X. Benedict, K. P. Driver, S. Hamel, B. Militzer, T. Qi, A. A. Correa, A. Saul, and E. Schwengler, *Phys. Rev. B* **89**, 224109 (2014).

[29] K. P. Driver and B. Militzer, *Phys. Rev. E* **95**, 043205 (2017).

[30] D. A. Liberman, *Phys. Rev. B* **20**, 4981 (1979).

[31] L. H. Thomas, *Proc. Cambridge Philos. Soc.* **23**, 542 (1927); E. Fermi, *Rend. Accad. Naz. Lincei.* **6**, 602 (1927).

[32] D. A. Liberman and B. I. Bennett, *Phys. Rev. B* **42**, 2475 (1990).

[33] D. C. Swift, T. Lockard, R. G. Kraus, L. X. Benedict, P. A. Sterne, M. Bethkenhagen, S. Hamel, and B. I. Bennett, *Phys. Rev. E* **99**, 063210 (2019).

[34] D. C. Swift, M. Bethkenhagen, A. A. Correa, T. Lockard, S. Hamel, L. X. Benedict, P. A. Sterne, and B. I. Bennett, arXiv:1905.08911 [Phys. Rev. E (to be published)].

[35] *CRC Handbook of Chemistry and Physics*, 92nd ed., edited by W. H. Haynes (CRC, Boca Raton, FL, 2011).

[36] *CRC Handbook of Chemistry and Physics*, 84th ed., edited by D. R. Lide (CRC, Boca Raton, FL, 2003).

[37] W. Slattery, Los Alamos National Laboratory report, 1990 (unpublished).

[38] G. Straub and W. Slattery, (Los Alamos National Laboratory report, 1990 (unpublished).

[39] G. I. Kerley, Sandia National Laboratories Report No. SAND93-0227, 1993 (unpublished).

[40] S. Anzellini, A. Dewaele, M. Mezouar, P. Loubeyre, and G. Morard, *Science* **340**, 464 (2013).

[41] F. E. Simon and G. Glatzel, *Z. Anorg. Allg. Chem.* **178**, 309 (1929).
023034-5