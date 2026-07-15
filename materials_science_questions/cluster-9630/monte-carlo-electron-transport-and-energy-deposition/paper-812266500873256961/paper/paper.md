![](./images/812266500873256961_1.jpg)

Available online at www.sciencedirect.com

![](./images/812266500873256961_2.jpg)

Advances in Space Research 37 (2006) 1597-1601

ADVANCES IN
SPACE
RESEARCH
(a COSPAR publication)

www.elsevier.com/locate/asr

# Energetic particles in the atmosphere: A Monte-carlo simulation

J. Schröter, B. Heber *, F. Steinhilber, M.B. Kallenrode

Fachbereich Physik, University of Osnabrück, Barbarastrasse 7, 49076 Osnabrück, Germany

Received 1 November 2004; received in revised form 19 May 2005; accepted 19 May 2005

## Abstract

Precipitating solar energetic particles (SEPs) ionize the atmosphere. They produce $NO_x$ and $HO_x$ which in turn destroy ozone. Here, we present Monte-Carlo simulations of the SEP interaction with the atmosphere. Compared to continuous energy loss models, the Monte-Carlo method leads to a shift of ionization to lower altitudes because secondaries, in particular X-rays produced by electron bremsstrahlung, are considered. In addition, the inclusion of ionization by solar electrons leads to modifications in ion production profiles with the magnitude of the effect depending on the properties of the parent solar event. Implications of our results for atmospheric chemistry modeling are briefly sketched.

© 2005 COSPAR. Published by Elsevier Ltd. All rights reserved.

**Keywords**: Atmosphere; Ionization; Solar energetic particles; Monte-Carlo simulation

---

## 1. Introduction

In the 1970s, solar energetic particle (SEP) events have been identified as sources of ozone loss in the middle atmosphere (Crutzen et al., 1975; Heath et al., 1977): precipitating energetic particles ionize and dissociate the neutral atmosphere, creating $NO_x$ (N, NO, $NO_2$) (Crutzen et al., 1975; Porter et al., 1976) and $HO_x$ (Solomon et al., 1981). These reactive species destroy ozone. Conventionally, ionization rates are determined using continuous energy loss models (Callis et al., 1998; Jackman et al., 2000) in which the energy input into the atmosphere is assumed to occur when (and where) the primary loses energy. In this paper, we will employ a Monte-Carlo simulation based on the GEANT 4 package (Agostinelli et al., 2003; Geant4, 2003) which also tracks the secondaries. As a consequence, energy input and ion pair production are shifted to lower altitudes. Results of this simulation were used in atmospheric chemistry model, e.g., Rohen et al. (2005).

## 2. The model

### 2.1. Geometry and composition

It is sufficient to use a plane-parallel model atmosphere because the height of the atmosphere is small compared to Earth's radius. Up to a height of 100 km, it is divided into 29 equidistant layers; its remaining mass is condensed into a 30th layer, 10-km thick: thus details of the energy deposit above 100 km are lost.

The composition of the atmosphere is homogeneous with $23.3\ \text{wt}\%\ \text{O}_2$, $75.5\ \text{wt}\%\ \text{N}_2$ and $1.3\ \text{wt}\%\ \text{Ar}$. For numerical studies, pressure, density and temperature height profiles are taken from the equatorial June atmosphere in the SLIMCAT/TOMCAT model (Chipperfield, 1996). This approach ignores the pronounced seasonal variability of the polar atmosphere and gives an average ionization profile instead (Quack et al.,

* Corresponding author.
E-mail address: bheber@uni-osnabrueck.de (B. Heber).

0273-1177/$30 © 2005 COSPAR. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.asr.2005.05.085

2001). For individual SEP events, corresponding polar atmospheres are used.

### 2.2. SEP event properties

During a SEP event protons, electrons, and $\alpha$-particles are accelerated (for a recent summary see, e.g., Kallenrode (2003)). Electron to proton ratios as well as energy spectra depend on the parent flare, in particular whether it is impulsive or gradual, the properties of the coronal mass ejection, and the geometrical relation between observer and solar activity.

Particle precipitation is assumed to be isotropic from the upper hemisphere: particle distributions in interplanetary space tend to be isotropic for electrons (Hucke et al., 1992) and become isotropic for protons during the time course of the event (e.g., examples in Kallenrode (1997)). Observations by the MEPED (Medium Energy Proton and Electron Detector) instrument on board POES (Polar Orbiting Environmental Satellite) even suggest a slight preference for larger pitch angles inside the polar cap at altitudes of 900 km (Bornebusch, private communication).

Energy spectra of precipitating SEPs can be described by a broken power law (Gosling et al., 1981; Forman and Webb, 1985; Jones and Ellison, 1991): $I(E)=I_{0} \cdot (E/E_{0})^{-\gamma}$, with $I_{0}$ being the differential intensity at a reference energy $E_{0}$, $E$ the energy, and $\gamma$ the spectral index. Around some 100 MeV, the spectrum flattens and intensities increase due to the background of galactic cosmic rays (Goeckler, 1984). Observed spectra are fitted simultaneously by up to three power-laws; the breaks between the power laws are not at fixed energies but are determined such that the best fit over the entire spectrum results.

### 2.3. Interaction

GEANT 4 allows for a multitude of interactions between the precipitating particle and the absorbing atmosphere. Our model considers as subset of particles protons, electrons, positrons, $\alpha$s, and photons. Interactions are limited to electromagnetic ones: multiple scattering, Compton-scattering, ionization, photo electric effect, gamma conversion, annihilation, pair production, and production of bremsstrahlung. Secondaries produced in such interactions are tracked up to a 1-m cut-off length of particle propagation. If particle energies are lower, the model switches to continuous energy loss.

Precipitating particles have an angular distribution and an energy spectrum. The Monte-Carlo simulation itself is performed for mono-energetic pencil-beams of 100 particles; angles of incidence vary between $0^\circ$ and $80^\circ$ in steps of $10^\circ$. The energies range from 1 to 500 MeV in 109 logarithmic equidistant steps for protons and 1 to 50 MeV in 340 steps for electrons. Statistics are tested by increasing the number of incident particles by a factor of 10 – the results are essentially the same.

The total energy input into each layer is the sum of the energy depositions of the individual particles; a division by the layer's thickness yields the linear energy transfer (LET) d$E$/d$x$. Thus, the primary result of the simulation is the LET as function of altitude, initial kinetic energy and impact angle.

Ion pair production rates for individual particle events are obtained by folding the LETs with the observed particle spectrum and angular distribution and assuming a mean ionization energy of 35 eV per ion pair (Porter et al., 1976).

## 3. Numerical studies

Fig. 1 shows sample tracks for a 300-MeV proton (left) and a 50-MeV electron (right). Production of secondaries is marked by dots, at the lines continuous energy losses occur with the line styles dashed, solid and dashed–doted indicating photons and negatively or positively charged particles, respectively.

The proton trajectory is basically a straight line. Only in the extremely rarefied upper atmosphere a trace of a secondary electron with significant path length is visible. Such long tracks occasionally occur in the upper atmosphere, because a low density implies a small interaction probability between the secondary and the atmosphere, leading to a long track. At lower altitudes secondary electrons are quickly stopped by the dense atmosphere and do not show up as separate tracks.

The straight path of the primary proton combined with the short range of the secondaries yields energy loss distributions comparable to those acquired in the conventional way without consideration of secondaries. Fig. 2 shows energy losses for particle spectra with four different power law indices $\gamma$ with (dots) and without (line) consideration of the secondaries. With increasing $\gamma$, the spectrum steepens and the ion production rate at lower altitudes decreases. Note that $\gamma=0$ implies that the particle intensity is independent of energy while $\gamma=2$ represents a SEP spectrum fairy well.

The situation is quite different for electrons, see left-hand side of Fig. 1: instead of a straight line the path is randomly twisted because the primary's mass is the same as that of the shell electron and thus deflection occurs during interaction. This multiple-scattering is not considered in a continuous loss model based on the Bethe–Bloch equation; thus such models underestimate the LET and consequently overestimates penetration depth.

In addition, not all secondaries keep close to the track of the primary: aside from the secondary electrons produced during ionization, a primary electron also

![](./images/812266500873256961_3.jpg)

Fig. 1. GEANT 4 simulation of a 300-MeV proton track (left) and a 50-MeV electron track (right) in the atmosphere. Dots denote production of secondaries; lines describe the particle traces (see also text).

![](./images/812266500873256961_4.jpg)

Fig. 2. Energy deposition of isotropically precipitating energetic protons in the range 1–500 MeV with (dots) and without (solid line) consideration of secondaries. The particle spectra are described by a power law with spectral index $\gamma$.

produces bremsstrahlung (dashed lines). These X-rays propagate large distances before depositing their energy due to Compton scattering and photo-ionization in denser layers of the atmosphere. Ionization, thus, can be shifted by several kilometers below the end of the primary track. The resulting energy transmission to altitudes less than 20 km with (dots) and without (lines) consideration of the secondaries is shown in Fig. 3, again for four different power law spectra and $\gamma=2$ being a fair representative for SEP spectra.

## 4. Ion production rate during SEPEs

To demonstrate the implications of the Monte-Carlo simulation for ion production, two different events are analyzed: one prominent event (October 22, 1989) and for comparison a large impulsive event (June 14, 1989). Electron spectra in the range 0.5–2.5 MeV are obtained from the CPME (Charged Particle Measurement Experiment, Decker and Mitchel (2001)) on board IMP (Interplanetary Monitoring Platform). Comparison with the higher energy electron instrument on IMP shows that in both events the electron spectrum can be extended down to 5 MeV. For the June event, proton spectra in the range 0.29–440 MeV are obtained from the same instrument; for the October event proton spectra in the range 0.8–500 MeV were taken from GOES (Geostationary Operations Environmental Satellite) because IMP measurements are less reliable due to failure of the anticoincidence scintillator.

The left-hand side of Fig. 4 shows the modeled ion pair production rates due to protons (dotted), electrons

![](./images/812266500873256961_5.jpg)

Fig. 3. Same as Fig. 2, but for energetic electrons in the range 1-50 MeV.

![](./images/812266500873256961_6.jpg)

Fig. 4. Ion pair production caused by protons in the range 1-500 MeV (dotted) and electrons in the range 1-5 MeV (dashed) for the event on October 22, 1989 (left), and the event on June 14, 1989 (right).

(dashed) as well as the sum of both (solid line) during the October event for 6 h containing the high energy maximum; at later times the instrument is saturated. Ionization of the electrons can amount to up to about 1/3 of that of protons in the height range 50-70 km, at lower altitudes electron contribution is insignificant - which is partly due to our abrupt cut off of the electron spectrum at 5 MeV.

The ion pair production rates for the main phase (1 day) of the impulsive June event are shown on the right-hand side of Fig. 4. Again the contribution of electrons is visible only above 50 km, however, around 70 km the ion pair production by electrons even exceeds that of the protons.

## 5. Conclusions

The main results of this paper are:

R1: for 1-500 MeV protons, ionization rates are essentially the same in the Monte-Carlo simulation and in a continuous energy loss model.

R2: for 1-50 MeV electrons, the consideration of bremsstrahlung shifts the ionization well beyond the Bragg peak to lower altitudes.

R3: electrons in SEP events contribute to ion pair production rates in the height range 50-70 km; the amount depends on whether the particle event originated in an impulsive or a gradual flare.

As a consequence of R1, the consideration of second-aries in the Monte-Carlo simulation cannot explain the difference between the observed and modeled electron densities in the October 1989 event as suggested by Ver-ronen et al. (2002). Instead, R3 suggests that the inclu-sion of electrons in the analysis of SEP events might explain such differences. It should be noted that implica-tions of R3 depend on the focus of research: in the very large events electron contributions are more or less a 10% effect and thus might be neglected as suggested by Jackman and McPeters (1985). For long term studies, such as variations over the solar cycle or possible climate impacts, however, also the much larger number of elec-tron-rich impulsive SEPs has to be considered and thus ionization rates (and atmospheric consequences of pre-cipitating particles) can be evaluated only if also elec-trons are considered.

R2 also has implications for modeling atmospheric effects of precipitating electrons. So far, magnetospheric electrons have been considered as a source of $NO_x$ which, owing to its long lifetime, sinks down from the meso-sphere into the stratosphere and affects ozone chemistry (Callis et al., 1996a,b). Our results suggest a modification to their model in such that part of the ionization is directly transferred downwards by Bremsstrahlung. However, a proper assessment of consequences for $NO_x$ and ozone modeling requires an atmospheric chemistry model, and is beyond the scope of this paper.

## Acknowledgments

This work has been supported by the Deutsche Forschungsgemeinschaft under contract DFG-Ka1297/2-3. Bernd Heber acknowledges support from DFG enabling him to participate in the 35th COSPAR Assembly in Paris, July 2004, where this work was presented.

## References

Agostinelli, S. et al. Geant4 – a simulation toolkit. Nucl. Instrum. Meth. Phys. Res. A, 250–303, 2003.

Callis, L.B., Boughner, R.E., Baker, D.N., et al. Precipitating electrons: evidence for effects on mesospheric odd nitrogen. Geophys. Res. Lett. 23, 1901, 1996a.

Callis, L.B., Baker, D.N., Natarajan, M., et al. A 2-D model simulation of downward transport of $NO_y$ into the stratosphere: effects on the austral spring $O_3$ and $NO_y$. Geophys. Res. Lett. 23, 1905, 1996b.

Callis, L.B., Natarajan, M., Lambeth, J.D., Baker, D.N. Solar atmospheric coupling by electrons (SOLACE), 2. calculated stratospheric effects of precipitating electrons, 1979–1988. J. Geophys. Res. 103, 28421, 1998.

Chipperfield, M. The TOMCAT offline chemical transport model. UGAMP International Report 44a, 1996. Available from: <http://www.env.leeds.ac.uk/martyn/slimcat.html>.

Crutzen, P.J., Isaksen, I.S., Reid, G.C. Solar proton events: strato-spheric sources of nitric oxide. Science 189, 457–458, 1975.

Decker, R.B., Mitchel, D.G. IMP-8 charged particle measurement experiment (CPME) and energetic particle experiment, 2001. Avail-able from: <http://sd-www.jhuapl.edu/IMP/imp_index.html>.

Forman, M.A., Webb, G.M. Acceleration of energetic particles, in: Stone, R.G., Tsurutani, B.T. (Eds.), Collisionless Shocks in the Heliosphere. AGU Geophysical Monograph, p. 34, 1985.

Geant4, 2003. Available from: <http://wwwasd.web.cern.ch/wwwasd/geant4/geant4.html>.

Goeckler, G. Characteristics of solar and heliospheric ion populations observed near Earth. Adv. Space Res. 4 (2–3), 127, 1984.

Gosling, J., Asbridge, J.R., Bame, S.J., et al. Interplanetary ions during an energetic storm particle event. J. Geophys. Res. 86, 547, 1981.

Heath, D.F., Krüger, A.J., Crutzen, P.J. Solar proton event: influences on stratospheric ozone. Science 197, 886, 1977.

Hucke, S., Kallenrode, M.-B., Wibberenz, G. Interplanetary type III radio bursts and relativistic electrons. Sol. Phys. 142, 143–155, 1992.

Jackman, C.H., McPeters, R.D. The response of ozone to solar proton events during solar cycle 21: a theoretical interpretation. J. Geophys. Res. 90, 7955–7966, 1985.

Jackman, C.H., Fleming, E.L., Vitt, F.M. Influence of extremely large solar proton events in a changing stratosphere. J. Geophys. Res. 105, 11659–11670, 2000.

Jones, F.C., Ellison, D.C. The plasma physics of shock acceleration. Space Sci. Rev. 58, 259, 1991.

Kallenrode, M.-B. The temporal and spatial development of MeV proton acceleration at interplanetary shocks. J. Geophys. Res. 102, 22347–22363, 1997.

Kallenrode, M.-B. Current views on impulsive and gradual solar energetic particle events. J. Phys. G 29, 965–981, 2003.

Porter, H.S., Jackman, C.H., Green, A.E.S. Efficiencies for production of atomic nitrogen and oxygen by relativistic proton impact in air. J. Chem. Phys. 167, 154–167, 1976.

Quack, M., Kallenrode, M.-B., von König, M., et al. Ground level events and consequences for stratospheric chemistry. Proceedings of ICRC 2, 4023–4026, 2001.

Rohen, G., von Savigny, C., Sinnhuber, M., et al. Ozone depletion during the solar proton events of Oct./Nov. 2003 as seen by SCIAMACHY. J. Geophys. Res., in press, doi:10.1029/2004JA010984, 2005.

Solomon, S., Rusch, D.W., Gerard, J.-C., et al. The effect od particle precipitation events on the neutral and ion chemistry of the middle atmosphere II: odd hydrogen. Planet. Space Sci. 29, 885–892, 1981.

Verronen, P.T., Turunen, E., Ulich, T., Kyrölä, E. Modelling the effects of the October 1989 solar proton event on mesospheric odd nitrogen using a detailed ion and neutral chemistry model. Ann. Gepophys. 20, 1967–1976, 2002.