JOURNAL OF GEOPHYSICAL RESEARCH, VOL. 109, A04309, doi:10.1029/2003JA010119, 2004

# Quantification of the spreading effect of auroral
proton precipitation

Xiaohua Fang, Michael W. Liemohn, and Janet U. Kozyra
Space Physics Research Laboratory, University of Michigan, Ann Arbor, Michigan, USA

Stanley C. Solomon
High Altitude Observatory, National Center for Atmospheric Research, Boulder, Colorado, USA

Received 3 July 2003; revised 22 January 2004; accepted 24 February 2004; published 24 April 2004.

[i] A three-dimensional Monte Carlo model has been developed to study the transverse beam spreading effect of incident energetic auroral protons during their precipitation in the Earth's upper atmosphere. Energetic protons with an isotropic angular distribution are injected at 700 km altitude. Two types of incident energy spectra, a monoenergetic and a Maxwellian distribution, are considered. Interaction of fast particles with a three-species atmosphere (O, $N_2$, and $O_2$) is included through charge exchange, electron stripping, ionization, excitation, and elastic scattering collisions. A uniform geomagnetic field is assumed in the model. The spreading effect is simulated for both a fine proton beam and a proton arc of longitudinal and latitudinal extent. It is found that the main dispersion region for a fine proton beam is located in the altitude range of around 250–450 km, where the first few charge exchange collisions play a significant role. In the spreading study for a proton arc, we compare the numerical results with previous studies and give a convincing explanation by analyzing atmospheric scale heights and cross-section data. For the purpose of the model validity check, we make a comparison of the Monte Carlo simulation with observations and the results from other models.

INDEX TERMS: 2455
Ionosphere: Particle precipitation; 2407 Ionosphere: Auroral ionosphere (2704); 7843 Space Plasma Physics: Numerical simulation studies; 2736 Magnetospheric Physics: Magnetosphere/ionosphere interactions; 2704 Magnetospheric Physics: Auroral phenomena (2407); KEYWORDS: Monte Carlo simulation, proton aurora

Citation: Fang, X., M. W. Liemohn, J. U. Kozyra, and S. C. Solomon (2004), Quantification of the spreading effect of auroral proton precipitation, J. Geophys. Res., 109, A04309, doi:10.1029/2003JA010119.

## 1. Introduction

[2] Since proton precipitations were detected from ground observations [Vegard, 1948], the proton aurora has been recognized as a significant complement to electron aurora in the study of input energy to the Earth. It was shown that at some latitudinal range in the evening sector the auroral ionization and the optical emissions may be produced mainly by the precipitating protons [Sharber, 1981; Gussenhoven et al., 1987; Hardy et al., 1989]. The transport of energetic protons is more complicated than that of electrons because additional processes, such as charge exchange and electron stripping, are involved. As charged particles, auroral protons penetrate into the atmosphere rotating around the geomagnetic field lines until charge exchange collisions with atmospheric species occur. After picking up electrons from the background atmosphere, particles are not constrained to move along the field lines any more. As energetic neutral hydrogen atoms, they can travel across the magnetic field lines. The hydrogen atoms are reionized in subsequent electron stripping collisions and turn back to protons. As a consequence, an incoming proton beam will diffuse over a wider region in the atmosphere.

[3] An understanding of the spreading effect is of impor- tance for proper interpretation of auroral imaging observa- tions. Typically, proton auroral emission profiles were calculated with transport models [Rees, 1982; Galand et al., 1998], which did not take into account the transverse spreading of particle beams. However, three-dimensional (3-D) calculations showed that horizontal spreading caused significant dispersion of the auroral emissions [Lorentzen, 2000].

[4] The spreading effect of an incident fine proton beam (in contrast to an arc) was first studied numerically by Davidson [1965]. He applied a Monte Carlo method to the spatial dispersion of monoenergetic auroral protons for an isotropic pitch angle distribution. It was found that as a result of repeated charge exchange and electron stripping processes, particles may traverse as far as 300 km away from the incident spot. However, these results are best regarded as qualitative because of the coarse data in atmosphere and collision cross sections used in his model. Moreover, in his simulation the phase angle of a spiraling proton was randomized after capturing an electron, which is not precisely correct.

Copyright 2004 by the American Geophysical Union.
0148-0227/04/2003JA010119

A04309
1 of 13

[5] *Johnstone* [1972] derived an analytic expression for the spreading effect of a fine proton beam. He made an assumption that the particle spreading scale was determined by the first neutral segments, which were the path lengths of protons after the first time they capture an electron. In his analysis the atmospheric density had a constant scale height. *Iglesias and Vondrak* [1974] then extended the model developed by *Johnstone* [1972] to study the angular distribution and intensity diffusion for a uniform auroral proton arc of infinite extent in the east-west direction and of limited width in the north-south direction. The spreading effect was also taken into account in the linear transport theory of auroral proton precipitation [*Jasperse and Basu*, 1982]. They improved the work of *Iglesias and Vondrak* [1974] by involving multiple neutral segments between repeated charge exchange and electron stripping collisions. In their model the energy loss at high altitudes was neglected, and the spreading effect was achieved by applying an estimated correction factor $\varepsilon < 1$ to the central fluxes at the equilibrium height (around 300 km). In the lower altitudes, plane parallel geometry was used, and the north-south variation of particle intensities was excluded. Moreover, this first linear transport theoretical treatment made the assumptions of a single constituent atmosphere and average discrete energy loss, which were removed in the subsequent numerical simulations [*Basu et al.*, 1993]. For the sake of simplification, elastic collisions dropped out from their equations since the energy loss was negligible compared to that of inelastic collisions. In reality, elastic collisions allow particles to be backscattered. In the recent work of *Jasperse* [1997], he applied the method of matched asymptotic expansions [*Van Dyke*, 1964] to the transport equations and obtained the spreading of proton-hydrogen aurora arcs in the altitude range of 280–600 km.

[6] Analytic methods have the merit of supplying a brief and clear picture of physical processes. However, owing to the complicated nature of physical problems, they have to include many assumptions at the same time to simplify the calculations. In this case, the Monte Carlo technique is an attractive alternative, with the advantage of simulating the life histories of a large number of test particles. *Kozelov* [1993] developed a Monte Carlo model and investigated the altitude dependence of the beam spreading in an effective $\text{N}_2$ atmosphere under the influence of a simplified dipolar magnetic field. *Synnes et al.* [1998] performed a Monte Carlo simulation for the auroral arc spreading effect in a nonuniform magnetic field. However, they did not have access to the cross-section data for the collisions between proton/hydrogen and neutral oxygen atoms, and approximated the atmosphere as an effective $\text{N}_2$. Very recently, *Lorentzen* [2000] presented a Monte Carlo calculation of auroral proton latitudinal and longitudinal dispersion in a full three-species ($\text{N}_2$, $\text{O}_2$, O) atmosphere. It was shown in his results that the first few charge exchange collisions determined almost the total spreading effect, which was the foundation of the early analytic work [*Johnstone*, 1972; *Iglesias and Vondrak*, 1974]. However, there was a mistake in Lorentzen's formulation of equation (2) to describe the deviation of hydrogen atoms, which was only valid in the case of nontilted magnetic field. An easy check is to sum the squares of the three direction components there. We can see that the summation is not equal to 1.

[7] In this paper we present a three-dimensional Monte Carlo model to simulate the transverse auroral proton spreading in the full three-species atmosphere. Both inelastic and elastic collisions are included in the interaction of fast particles with the ambient neutrals. Section 2 presents the collision model and describes how a Monte Carlo technique is used in the current work. Subsequently we present numerical simulation results in section 3 using our Monte Carlo method. In section 3.1 the discussion is restricted to a fine proton beam with an injection point at the top, as was performed in previous studies [e.g., *Davidson*, 1965; *Kozelov*, 1993]. Examination of point source calculation yields physical insights into the problem of proton precipitation and spreading. The calculation is carried out with the two types of incident proton energy spectra, i.e., a monoenergetic and a Maxwellian energy distribution. The beam spreading effect is calculated from the downward particle fluxes over horizontal planes at several altitudes. Horizontal profiles of primary ionization rates are presented as well. To the best of our knowledge, the present paper is the first attempt to provide a direct illustration of the beam spreading effect over horizontal planes as it evolves in altitude. The discussion in this paper is mainly concerned with the spreading effect considering vertical field lines. It will be complemented in a forthcoming paper with a particular emphasis on the influence of the tilted magnetic field lines on the asymmetric beam spreading. In section 3.2, calculations are performed to examine the spreading effect for a proton arc with the longitudinal and latitudinal extent at the top of the atmosphere. It will be shown how the flux intensity is diminished as the particles precipitate over a wider region due to charge exchange collisions. Our model has also been validated through a variety of comparisons with previous studies. Finally, a summary and conclusion are provided in section 4.

## 2. Model Description

[8] The Monte Carlo method is a widely used research tool, which traces the lifetimes of a large set of test particles and records the corresponding statistical information along the way that can be converted to other physical quantities. In this section we overview the fundamental Monte Carlo random walk simulation process [see *Cashwell and Everett*, 1959] and discuss its application to the problem of auroral proton transverse beam spreading. The model described here is based on the 1-D Monte Carlo model of *Solomon* [2001]. However, for the purpose of the spreading effect study, it has been completely rewritten in order to handle the 3-D scattering of the precipitating particles.

### 2.1. Monte Carlo Random Walk

[9] To summarize it briefly, the Monte Carlo model monitors the trajectories of incident energetic protons in a collision-by-collision manner down to an assigned low-energy cutoff limit. A variety of effects due to inelastic and elastic collisions are accumulated over the course of the particle traveling in the Earth's atmosphere. As a preliminary analysis, we model the geomagnetic field as uniform, following the linear transport method [*Jasperse and Basu*, 1982; *Basu et al.*, 1987, 1993, 2001]. *Galand*

and Richmond [1999] argued that there is essentially no difference in the low-altitude energy fluxes with and without magnetic mirroring. Therefore the magnetic field nonuniformity can be neglected in the main energy depo- sition region (below 200 km). As a boundary condition, proton injection in an isotropic angular distribution over the downward hemisphere is imposed at an altitude of700 km, corresponding to observation from sounding rockets and satellites [e.g., Søraas et al., 1974; Lundblad et al., 1979; Urban, 1981]. The initial pitch angle with respect to the incident magnetic field line is selected by

$$
\mu=\sqrt{r},\qquad(1)
$$

where $\mu$ is the cosine of the pitch angle and $r$ is a random number uniformly distributed in the range of 0 and 1. The azimuthal angle is randomly selected in $2 \pi$. In our model we adopt the random number generator from Bird [1994]. In each random process, a new random number is produced. A test proton with fully determined initial conditions then undergoes a series of collisions with the ambient neutrals. The target of the beam is a full three-species atmosphere (O, N₂, O₂), simulated by the Mass Spectrometer Incoherent Scatter (MSIS-90) model [Hedin, 1991]. For the sake of simplification, the Monte Carlo model is carried out in a plane-parallel atmosphere as a preliminary simulation. That is, the atmosphere at the same altitude level has the same constituents and densities. The path length traveled to the next collision is derived from an "optical depth" $\tau$, which is given by

$$
\tau=\int \sum_{i} n_{i} \sigma_{i_{\mathrm{tot}}} d l=-\log (r),\qquad(2)
$$

where $l$ is the path length. The variable $n_{i}$ is the number density of the atmospheric species labeled by index $i$, and $\sigma_{i_{\mathrm{tot}}}$ is the corresponding total (inelastic plus elastic) particle impact cross section. The change of the particle location is then calculated. In the next step we decide the exact natureof the collision. The type of collision (charge exchange/ electron stripping, ionization, excitation, or elastic) is determined randomly, weighted by products of cross sections and number densities at the collision point. The type of collision target is then decided among the atmospheric species. The inelastic and elastic cross sections used in these processes are adopted from the surveys by Basu et al. [1987] and Kallio and Barabash [2001], respectively. The transport of secondary electrons createdin ionization and electron stripping collisions are neglected; that is, it is assumed that all of the secondary electron energy goes into local heating. This is a good assumption when studying the impact of proton injection to the ionospheric density because energetic protons ionize more efficiently than electrons do. Subsequently, it is of importance to determine the immediate fate of the particle after a collision, including angular redistribution and energy loss. As justified by McNeal and Birely [1973], the differential cross sections involving protons and H atoms are very strongly peaked in the forward direction for incident energies above a few hundred electron volts, and so the forward scattering approximation has been widely accepted in the previous studies of the auroral proton transport problem. In our model we also make this approximation for inelastic collisions and employ the discrete energy loss model from Basu et al. [1993]. The energy loss in each inelastic process is calculated as a function of the $H^{+} / H$ energy. As for elastic collisions, the angle of deflection and the energy apportionment are calculated following the work by Kallio and Barabash[2001] and Galand et al. [1997], respectively.

[10] Before turning into a neutral hydrogen atom via charge exchange, a proton keeps spiraling along the local magnetic field line and changing its phase angle as well. Rather than randomizing the phase angle as Davidson[1965] did, we calculate the variation explicitly,

$$
\Delta \phi=-\int \Omega \frac{d z / \sin \gamma}{\mu v}=-\frac{\sqrt{1-\mu^{2}}}{\mu} \frac{\Delta z}{r_{\Omega} \sin \gamma},\qquad(3)
$$

where $\phi$ is the phase angle, $\gamma$ is the dip angle, which is the angle that magnetic field lines make with the horizontal, $\Delta z$ is the vertical upward distance traveled by the proton between collisions, $\Omega$ is the gyrofrequency, and r_Ω is the gyroradius. In deriving equation (3), we have assumed that the field lines are oriented downward uniformly. In the calculation we evaluated the gyroradii assuming $r_{\Omega}=0.33 ~km$ for a 10 keV proton, as presented by Jasperse [1997]. In other words, the same magnetic field strength was used.

[11] The collision-by-collision algorithm traces the tra- jectories of incident particles until the simulation boundary(700 km altitude) or the lower cutoff energy limit is reached. Following the work by Solomon [2001], a particle is monitored down to 20 eV. Once lower than this energy limit, particles actually seldom move far from their positions before eventually being thermalized. Accordingly, it is reasonable to contribute the remaining energy to heating the background atmosphere and remove them from the calculation.

### 2.2. Coordinate System

[12] While the motion of protons is constrained to mag- netic field lines, neutral hydrogen atoms move in a straight line in the direction of the velocity they acquired at their creation. This means that an initially narrow incident proton beam can spread out significantly as it penetrates the atmosphere.

[13] A normal Cartesian coordinate system [X, Y, Z] is defined with Z directed vertically upward, X pointing northward, and Y pointing westward for the completion of a right-handed system. The parallel magnetic field lines point downward and lie in the $X-Z$ plane. In order to facilitate the understanding of the transverse beam spread- ing with respect to the magnetic field line through the incident entry point, it is convenient to introduce another set of variables $[\alpha, \beta, Z]$ to record the spatial information of a particle. The coordinate $\alpha$ is the spreading angle between the original magnetic field line and the line connecting the particle location at a given time with the incident entry point. The coordinate $\beta$ is the azimuthal angle, which is the angle swept out by the line connecting the particle location to the intersection of the original magnetic field line with

![](./images/812355273980116992_1.jpg)

Figure 1. Hemispherically averaged downward and upward integrated $H^+$ and H fluxes versus altitude
for magnetic field lines with dip angles (a) $\gamma = 90^\circ$ and (b) $\gamma = 60^\circ$. Solid curves indicate $H^+$ fluxes;
dashed curves indicate H fluxes. The fluxes in the downward and upward directions are indicated near
each of the curves. The incident proton injection has a monoenergetic energy of $E = 10$ keV.

the horizontal plane, measured from the positive $X$ direc-
tion. $Z$ still stands for altitude.

## 3. Results and Discussion
### 3.1. Spreading of a Fine Proton Beam

[14] The Monte Carlo technique explained above was
used to simulate the transport of auroral proton injection
with a variety of initial conditions. Unless specified explic-
itly, the parameters used in calculations were set as follows.
In each calculation case, $2 × 10^6$ test particles with an
isotropic angular distribution were released from 700 km
altitude in the presence of a uniform magnetic field with a
dip angle of $\gamma = 90^\circ$. The initial point of entry was at $65^\circ$N,
$0^\circ$E in geodetic coordinates. Then they were monitored as
they suffered a series of collisions with O, $N_2$, or $O_2$ in the
Earth's atmosphere, which was associated with a low
geomagnetic activity index $Ap = 15$ and a moderate solar
activity index $F_{10.7} = 150$ in the MSIS-90 model. The
atmosphere was appropriate for UT = 0 on 21 March
1999. For the sake of comparison, the simulation results
were scaled to an incident total energy flux of $Q_0 = 1$ erg
cm$^{-2}$ s$^{-1}$. Note that all of our results are from a 3-D
simulation, but sometimes (as noted below) they have been
horizontally integrated for comparison with the results from
1-D models.

#### 3.1.1. Monoenergetic Injection

[15] To give an overall impression of the particle trans-
port, we present in Figure 1 an altitude profile of hemi-
spherically averaged downward and upward proton and
hydrogen atom fluxes integrated in both horizontal location
and energy. Figure 1a is for vertical magnetic field lines ($\gamma =
90^\circ$), while Figure 1b is for a tilted case ($\gamma = 60^\circ$). From the
view of proton precipitation, the atmosphere can be approx-
imately divided into four zones. For $E = 10$ keV, there are
few collisions above $\sim$450 km altitude, where the down-
ward proton flux decreases very gradually and the down-
ward hydrogen atom flux increases when protons capture
electrons from the background neutrals. There is a transition
layer in the altitude range of around 250–450 km, in which
the $H^+$ flux noticeably decreases as charge exchange colli-
sions become more prevalent. Below $\sim$250 km, the ratio of
the total H flux to that of $H^+$ is approximately in quasi-
equilibrium due to frequent charge exchange and electron
stripping collisions. Lower than $\sim$120 km, both fluxes
severely attenuate where most of the energy deposition
takes place. Note that the exact altitudes of the zone
boundaries depend on the incident energies.

[16] As shown in Figure 1, elastic collisions clearly
manifest themselves in the production of upward proton
and hydrogen fluxes specially in the case of $\gamma = 90^\circ$,
because of the forward scattering approximation used for
inelastic collisions. In the vertical magnetic field, small
angular deflection during elastic collisions makes the down-
ward particles with pitch angles near $90^\circ$ scattered in the
backward direction. It is noticeable that the orientation of
the geomagnetic field lines has little effect on the downward
fluxes. In contrast, the upward fluxes vary considerably
with different magnetic field dip angles. It is found that in
the tilted case there are more upward H fluxes but fewer
upward $H^+$ fluxes. This behavior can be explained as
follows. In the presence of tilted magnetic field lines, there
is a higher probability for the neutral hydrogen atoms
created in the charge exchange collisions to have velocity
in the upward direction. However, as charged particles,
protons are bound to the magnetic field lines. Accordingly,

![](./images/812355273980116992_2.jpg)

**Figure 2.** Hemispherically averaged downward $\text{H}^{+}$, H fluxes, and primary ionization rate in the $X-Y$ plane within a 500 km radius from the incident magnetic field line at altitudes of 450, 350, 250, and 120 km. The proton injection has a monoenergetic energy of $E = 10$ keV.

upward protons have to travel a longer path when the field lines are tilted. In other words, there is more probability for them to be lost.

[17] For the $\gamma = 90^\circ$ case, the horizontal profiles of hemispherically averaged downward $\text{H}^{+}$, H fluxes, and the primary ionization rates at altitudes 450, 350, 250, and 120 km are shown in Figure 2 and Figure 3. As noted previously, this calculation of the ionization rate excluded the contribution from secondary electrons. A novel feature of our present paper is the direct illustration of the spreading effect of a precipitating auroral proton beam over horizontal planes, as displayed in Figure 2. It is apparent that for $E = 10$ keV, the main dispersion of the downward proton injection occurs at high altitudes (above $\sim$250 km). As altitude decreases, the primary ionization rate keeps increasing due to the thickening atmosphere until reaching a maximum at around 120 km altitude. Again we see in Figure 3 that the proton intensity at the beam center gradually weakens over the course of penetration. At the same time, the lateral magnitude strengthens as a result of charge exchange and electron stripping collisions, but attenuates below $\sim$120 km altitude because of the denser neutrals. Careful attention should be paid to the proton fluxes at the center, where the intensity is averaged on the scale of $\text{km}^2$. Actually at the high altitudes, most of the protons are constrained to the incident magnetic field line within the original $\text{cm}^2$ beam cross section. For $E = 10$ keV proton precipitation, the drop of the central value from 700 to 300 km is only 1 order of magnitude. Another feature we should point out in Figures 2 and 3 is that symmetric spreading is well demonstrated around the central magnetic field line. Symmetric calculation results are expected in accordance with the symmetry of the model associated with the vertical magnetic field.

![](./images/812355273980116992_3.jpg)

**Figure 3.** The logarithm of hemispherically averaged (a) downward $\text{H}^{+}$ flux, (b) downward H flux, and (c) primary ionization rate versus the distance from the incident central magnetic field line at 450, 350, 250, and 120 km. The quantities are averaged over azimuthal angles $-90^\circ < \beta < 90^\circ$ (right half side) and $90^\circ < \beta < 270^\circ$ (left half side). The results are for monoenergetic injection of $E = 10$ keV.

![](./images/812355273980116992_4.jpg)

Figure 4. Altitude dependence of the effective beam radius in association with (a) downward $H^+$ flux, (b) downward H flux, (c) downward $H^+$ + H fluxes, and (d) primary ionization rate for monoenergetic proton injection of $E = 1, 4, 10, 40, 100$ keV. Outer solid curves show 1-keV results, and inner solid curves show 100-keV results.

[18] To provide a quantitative description of the auroral proton beam spreading, we follow Kozelov [1993] and define effective beam radii, within which 80% of the quantities are confined. As seen in Figure 1, the intensity of upward fluxes is more than 1 order of magnitude lower than that of downward fluxes, except at very high altitudes for H or in the case of very tilted magnetic field lines. Accordingly it is good enough to consider only downward particles when calculating the spreading beam width. In Figure 4 we present the effective beam radius as a function of altitude for downward $H^+$, H, $H^+$ + H, and primary ionization rate, respectively. The calculation was performed for monoenergetic proton injection with $E = 1, 4, 10, 40$, and 100 keV. As the injection energy increases from 1 to 100 keV, the peak values of the effective beam radii for total downward particle fluxes narrow from approximately 255 to 50 km. As shown in Figure 4, an increase in the incident energy leads to the downward movement of the profile and to its thickening. By "thickness" we mean the vertical extent spanning from the top to the minimal penetration depth, which increases with increasing incident $H^+$ energy. In other words, more energetic particles have more capa- bility of penetration. We can see that for proton beam spreading the main dispersion region is located in the transition layer (above $\sim$250 km). Below this layer, there is very little spreading in the quasi-equilibrium zone, where the mean free path of charge exchange/electron stripping collisions becomes small. Below $\sim$120 km the dense atmosphere makes the beams attenuate very rapidly. A remarkable feature of the downward hydrogen beam spreading is the structure of double peaks. The hydrogen beam widths rapidly increase with decreasing altitude and are peaked at around 500-550 km altitude, then shrink below this, down through the transition region. As a result of frequent charge exchange and electron stripping, the hydrogen beam demonstrates a similar structure in the quasi-equilibrium zone as the proton beam with almost the same beam radii. The existence of the peak of the hydrogen beam widths at high altitudes was also pointed out by Jasperse [1997]. It is understandable since there are very few H particles at high altitudes. The isotropic initial condition means there are downward $H^+$ particles with large pitch angles. They are preferentially converted to hydrogen atoms due to their longer path length per unit altitude distance. Thus the downward H atoms at these altitudes are systematically created with large flying angles with respect to vertical, and the beam width rapidly increases. As the transition layer approaches and charge exchange collisions in the primary $H^+$ beam increase, more downward directed H atoms are created close to the incident magnetic field line and the 80% beam radius decreases.

[19] It is hard to make a direct comparison among various approaches due to the difference in geomagnetic field model, cross sections, atmospheric scale heights, boundary conditions, and so on. However, the general agreement between the results of Kozelov [1993] and ours lends credibility to our calculation. It is shown in Figure 4 that our beam widths are roughly 20-80 km larger, which may arise partially from the fact that the converging configura- tion of the magnetic field used in Kozelov's model prevents protons from spreading. An alternative explanation for the discrepancy is that the cross section and the atmospheric scale heights are different between the models (see discus- sion in section 3.2.1 below). Note that the energy depen- dence of the beam width disagrees with the result of Lorentzen [2000], who found no beam width change for particle precipitation in the 10-50 keV energy range.

[20] Figure 5 shows the altitude-dependent probability distribution of the first five charge exchange collisions for an incoming proton with $E = 10$ keV (as an example). It is clear that the first few charge exchange collisions dominate in the 250-450 km height range and play a significant role in the beam spreading there. The peak values of the effective beam radii for downward $H^+$ + H fluxes and the average first neutral segments projected in the $X-Y$ plane

![](./images/812355273980116992_5.jpg)

Figure 5. Probability distribution of the first five charge exchange collisions for an incident 10 keV proton versus altitude.

<table>
<caption>Table 1. Peak Values of the Effective Beam Radii of Downward H⁺ + H Fluxes and the Averaged First Straight Segments Projected in a Horizontal Plane for Monoenergetic Proton Injection</caption>
<thead>
<tr>
<th>E, keV</th>
<th>Peak Value, km</th>
<th>First Straight Segment, km</th>
<th>Percentage</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>255</td>
<td>184</td>
<td>72.2</td>
</tr>
<tr>
<td>4</td>
<td>201</td>
<td>139</td>
<td>69.2</td>
</tr>
<tr>
<td>10</td>
<td>169</td>
<td>115</td>
<td>68.0</td>
</tr>
<tr>
<td>40</td>
<td>114</td>
<td>81</td>
<td>71.1</td>
</tr>
<tr>
<td>100</td>
<td>50</td>
<td>44</td>
<td>88.0</td>
</tr>
</tbody>
</table>

are compared in Table 1. The first segment means the distance, on average, that a particle moves away from the incident magnetic field line after the capture of an electron for the first time. The results show that the average first segments can account for roughly 70% or more of the maximal beam radii. In this way, the first departure of the incident particles from the initial magnetic field line can be used as a coarse estimation of the beam spreading. The correlation also validates the assumption used in theoretical analyses that the first charge exchange collision determines the extent of the dispersion.

[21] Of particular interest in Figure 4 is that the beam widths of the primary ionization rates are more than 2 times larger than those of the downward particle fluxes. It is a bit surprising to discover that 80% of the projectiles (those within the particle beam radius, as defined here) contribute less than 80% of ionizations. As we know, the probability of ionization collisions through a certain altitude bin in the plane-parallel atmosphere is determined by two factors: One is the hot particle fluxes, and the other is the number of target molecules. In Figure 6 the horizontal distributions of the average particle velocity angles (for energetic protons and hydrogen atoms) with respect to the vertical direction are illustrated. It is clearly shown that on average this angle increases away from the incident magnetic field line. In other words, the larger the distance from the incident field line, the higher the average collision probability with atmospheric neutrals because of the longer flight path (that is, more targets) through an altitude bin. This is the reason why the beam radii of the particle fluxes are smaller than those of the ionization rates.

![](./images/812355273980116992_6.jpg)

Figure 6. Average velocity angles of energetic protons and hydrogen atoms with respect to the vertical plotted in the $X-Y$ plane within a 500 km radius from the incident magnetic field line at altitudes of 450, 350, 250, and 120 km. The proton injection has a monoenergetic energy of $E = 10$ keV.

### 3.1.2. Maxwellian Injection

[22] We have considered monoenergetic proton injection for the sake of physical insight and comparison to the previous research. However, satellite observations showed that the energy spectra of ion precipitation in typical diffuse auroras are approximately Maxwellian [Sharber, 1981; Hardy et al., 1989]. Figure 7 shows the horizontal profiles of hemispherically averaged downward H⁺, H fluxes, and primary ionization rates at different altitudes similar to Figure 3 but for incoming protons with a Maxwellian spectrum of the characteristic energy of $E_0 = 10$ keV. They display a similar beam spreading to the monoenergetic input. Note that in a Maxwellian distribution the average particle energy is 2 times larger than the characteristic energy. Consequently it is not surprising to see that the Maxwellian proton injection has less transverse beam divergence. In Figure 8 we present a variety of beam radii in the case of the Maxwellian energy spectra with the characteristic energy of $E_0 = 1, 4, 10, 40$, and 100 keV. Again it shows a structure similar to the monoenergetic input as indicated in Figure 4 but with deeper penetration. Moreover, the peak values are up to 30 km smaller since, on average, particles are more energetic in the Maxwellian distribution

![](./images/812355273980116992_7.jpg)

Figure 7. Similar to Figure 3 but for a Maxwellian distribution with a characteristic energy of $E_0 = 10$ keV.

![](./images/812355273980116992_8.jpg)

Figure 8. Similar to Figure 4 but for a Maxwellian distribution with the characteristic energy $E_0 = 1, 4, 10, 40$, and 100 keV.

than in the monoenergetic spectrum of the same characteristic energy.

[23] It is also interesting to examine the energy loss of the incident particles through a series of collisions. As required by the energy conservation law, the total incident energy at the top is equal to the total energy deposition into the atmosphere and the energy taken away by the particles escaping from the studied region. As identified in Figure 1, the backscattered fluxes carry only negligible energy in the vertical magnetic field. Figure 9 shows the altitude dependence of the horizontally integrated energy deposition rate. It is seen that the neutral atmosphere gains much energy as it is ionized in charge exchange and ionization collisions. Another significant energy loss is transfered to the secondary electrons created as a result of the ionization of a target or a projectile. In addition to these two major energy sinks, there is still some energy obtained by the neutral atmospheric species in excitation collisions. A very small amount of energy is absorbed by the atmosphere in elastic collisions or over the thermalization process when the particle energies drop below the lower cutoff limit. This validates the assumption made by *Jasperse and Basu* [1982] that elastic collisions have a negligible effect on the energy degradation. However, for the albedo problem, elastic collisions are significant in the generation of upward fluxes, as illustrated in Figure 1. For the purpose of comparing to the linear transport model result, we used the same geophysical conditions as described by *Decker et al.* [1996]. We can see that excellent agreement is demonstrated throughout the low-altitude range, with the exception above 350 km altitude. This discrepancy is negligible, however, if taking into account that most of the energy deposition takes place in the low atmosphere. There are more than 2 orders of magnitude enhancement from the energy deposition rates at the high altitudes to the peak value.

[24] Another comparison is given to validate our modeling. We calculated horizontally integrated primary ionization rates as a function of altitude in the case of a Maxwellian distribution with a characteristic energy of $E_0 = 4, 8$, and 20 keV. The results are compared to the work of *Solomon* [2001] and *Galand et al.* [1997] and are presented in Figure 10. In order to facilitate our comparison, we should make the input conditions as identical as possible. As *Solomon* [2001] did, we set $F_{10.7} = 289$, $\langle F_{10.7} \rangle = 209$. For these comparisons the calculation was performed with the incident point of entry at 950 km altitude with geodetic coordinates $65^\circ$N, $160^\circ$W at 0000 UT on 30 January 1985. In addition, for the sake of the comparison, we employed the energy loss model by *Solomon* [2001], in which the energy of secondary electrons is computed explicitly instead of using an average energy loss. We can see that these three sets of results agree remarkably well, and this corroborates the validity of our model.

[25] The transverse proton beam spreading in a tilted magnetic field deserves an additional mention, although more details are beyond the scope of this paper. As a direct comparison with Figure 7, we present in Figure 11 the horizontal profiles of downward $H^+$, $H$, $H^+ + H$, and primary ionization rate in the case of the tilted magnetic field lines with a dip angle of $\gamma = 75^\circ$. The magnetic field lines are parallel to the $X - Z$ plane but tilted toward the positive $X$ direction pointing downward. The calculation was performed for a Maxwellian distribution with a characteristic energy of $E_0 = 10$ keV. It is shown in Figure 11 that asymmetric beam spreading is demonstrated over the horizontal planes due to asymmetric particle scattering. For example, far from the central region, primary ionization rate at 350 km altitude is highly asymmetric. The azimuthally averaged ionization intensity in the positive $X$ direction approaches almost 2 times larger than that in the negative $X$ direction, as far as a radius of 500 km. However, there are different spreading patterns with respect to proton,

![](./images/812355273980116992_9.jpg)

Figure 9. Energy deposition rate from various processes versus altitude: ionization of the neutral atmosphere (solid curve), created secondary electrons (dash-dotted curve), excitation (dashed curve), and heating of the atmosphere in elastic collisions plus the energy absorption when the particle energy is lower than a cutoff limit (dotted curve). The total deposited energy is indicated by a solid line with dots. The result of the linear transport model [*Basu et al.*, 2001] is also shown for comparison (solid curve with circles). The incident proton flux has a Maxwellian characteristic energy of $E_0 = 8$ keV. The total incident energy flux is $Q_0 = 0.5$ erg cm$^{-2}$ s$^{-1}$.

![](./images/812355273980116992_10.jpg)

Figure 10. Comparison of primary ionization rates versus altitude for different methods. Our results are shown as solid curves. The results provided by *Solomon* [2001] are plotted with dashed curves. The results of *Galand et al.* [1997] are shown as dotted curves.

hydrogen fluxes and ionization rate. Asymmetric spreading behavior varies with altitude as well. A detailed discussion will be provided in a future paper.

### 3.2. Spreading of a Proton Arc

[26] The discussion below is devoted to a detailed study of the spreading effect of a proton arc. Rather than being described as a beam of particle precipitation, a proton aurora is better approximated by a two-dimensional spatial distri- bution with longitudinal and latitudinal extent. In this section we extend the numerical simulation in the previous section to meet the challenge particular to the 2-D incident conditions. In practice, the continuous geometric boundary is discretized into a number of entry cells in the east-west direction ($Y$ axis) and in the north-south direction ($X$ axis). The pixel size is small enough so that its viewing angle to any point of interest below is less than the spreading angle bin size $\Delta\alpha$. Thus the precipitating particles in a cell can be regarded to concentrate at the cell center. Then we integrate all of the contribution from the particle input at each cell to calculate the fluxes at the bottom. In this way, the spreading effect acts not only as a loss mechanism along the incident magnetic field line but also as a particle source to a point away from this line. Below we perform the Monte Carlo simulation in two different boundary conditions. First, there is a constant proton precipitation with homogeneous distri- bution and intensities above the atmosphere. Second, we consider the effect of a variation of energy spectra and energy fluxes in the magnetic north-south direction while keeping the boundary conditions constant in the magnetic east-west direction.

#### 3.2.1. Homogeneous Input at the Top

[27] Figure 12 shows the total downward $H^{+}$ and $H$ intensity at 300 km altitude as a function of the distance from the arc center in the north-south direction. Following *Iglesias and Vondrak* [1974], we assumed a proton arc of infinite extent in the east-west direction and of semiwidth $W$ in the north-south direction. In numerical practice, we used a finite value ($\Delta = 1000$ km) to approximate the arc semilength in the east-west direction, which is sufficiently larger than $W$. It is seen in Figure 12 that a significant fraction of the particles spread outside of the original beam

![](./images/812355273980116992_11.jpg)

Figure 11. Similar to Figure 7 but for a tilted magnetic field with a dip angle of $\gamma = 75^\circ$.

![](./images/812355273980116992_12.jpg)

Figure 12. Relative intensity of the total downward $H^{+}$ and $H$ fluxes at 300 km altitude with respect to the homogeneous monoenergetic input of $E = 6$ keV at the top. Different proton arc semewidths $W = 30, 60$, and 120 km are used in the calculation. Our results are shown as solid curves. The results of *Iglesias and Vondrak* [1974] are plotted with dashed curves.

dimensions. In addition, the relative intensity as well as the amount of spreading depends upon $W$.

[28] As illustrated in Figure 12, the difference between our model results and the results from *Iglesias and Vondrak* [1974] becomes smaller inside the arc and a bit larger outside as $W$ increases. However, there exists a significant systematic disagreement; that is, our results show a smaller spreading effect. It seems implausible because we consider all of the particle interactions instead of only the first charge exchange collisions. In other words, their estimate should have set a lower limit to the spreading effect. We will see that such discrepancy results from the different atmosphere models and cross-section data used in these two calculations.

[29] As the starting point in the work of *Iglesias and Vondrak* [1974], the probability that a particle has a first neutral segment of path length $n = l/H$ in a vertical magnetic field is given by [*Johnstone*, 1972]

$$
P(n)=\frac{m \exp (n)}{[m-1+\exp (n)]^{2}}, \tag{4}
$$

where the dimensionless variable $n$ is the path length $l$ normalized by the atmospheric scale height $H$. Here $m$ is the ratio of the charge exchange cross sections of protons to the electron stripping cross sections of hydrogen atoms, namely, $m=\sigma_{10}/\sigma_{01}$. The parameters $m$ and $H$ were assumed to be altitude independent. The average normalized path length $\langle n\rangle$ is obtained as [*Johnstone*, 1972]

$$
\langle n\rangle=\frac{m}{m-1} \log (m). \tag{5}
$$

[30] The horizontal spreading for a particle with an initial pitch angle $\theta$ is $\langle n\rangle H \tan\theta$. Accordingly, the transverse beam spreading effect is determined by cross-section data ($m$), atmospheric scale height ($H$), and pitch angle distribution ($\theta$). For 6 keV protons, the cross-section ratio used by *Iglesias and Vondrak* [1974] was $m = 5$. The scale height of the atmosphere was set to be $H = 60$ km. In our Monte Carlo simulation the corresponding $m$ value can be calculated by means of estimation of the effective cross sections, weighted over the abundance of the three atmospheric constituents. That is, the effective $m$ is given by

$$
m=\sigma_{10}^{\text{eff}}/\sigma_{01}^{\text{eff}}=\frac{\sum_{i}n_{i}\sigma_{i_{10}}}{\sum_{i}n_{i}\sigma_{i_{01}}}, \tag{6}
$$

where $\sigma_{i_{10}}$ and $\sigma_{i_{01}}$ are the charge exchange and electron stripping cross sections for the ambient neutrals labeled by index $i$, respectively. At altitudes between 500 and 300 km where most of the first charge exchange collisions take place, the values of $m$ and $H$ increase from 1.96 to 2.65 and decrease from 66 to 51 km, respectively, as a function of decreasing altitude. Thus $\langle n\rangle H$ ranges from 80 to 91 km. We can see that these values are significantly smaller than $\langle n\rangle H = 121$ km corresponding to the model atmosphere used by *Iglesias and Vondrak* [1974]. Applying the above analysis to account for the spreading effect of a proton arc, we can conclude that our model results should show less spreading than their estimate in the comparison of Figure 12, because of the difference in the model atmosphere.

![](./images/812355273980116992_13.jpg)

Figure 13. Relative intensity of the total downward $\text{H}^{+}$ and H fluxes at 300 km altitude with respect to the homogeneous input at the top. The incident proton fluxes have a Maxwellian distribution with the characteristic energy of $E_{0} = 1$, 4, 8, and 10 keV. The semiwidth of the proton arc is $W = 100$ km.

[31] To determine the dependence of the spreading effect on the incident energy spectra for a proton arc, we repeat the above calculation but apply to a Maxwellian distribution with different characteristic energies while fixing the latitudinal semiwidth $W = 100$ km. As shown in Figure 13, the spreading increases with decreasing incident energy. This result is consistent with that presented in Figure 8 for a fine beam spreading. It is of interest to note that the central intensity at 300 km altitude for $E_{0} = 8$ keV is about 0.77 relative to the precipitating fluxes on the atmosphere from above. As a comparison, the correction factor $\varepsilon$ estimated by *Jasperse and Basu* [1982] was 0.75. We can see that a very close agreement is reached. Recall that a single constituent atmosphere model was adopted in their calculation. Hence it is reasonable to believe that the discrepancy in atmosphere models can also account for this small disagreement in $\varepsilon$.

### 3.2.2. Comparison With Observations

[32] We envisage that the actual particle distribution above the atmosphere is not homogeneous but variable in the invariant-latitudinal direction. To better test the validity of our Monte Carlo modeling, we should include a direct comparison with observations. However, because of the scarcity of simultaneous observations of the particle distribution at the top as well as the resulting ionization rate, it makes the comparison between the model simulation and measurements hard. Furthermore, a case of pure proton precipitation is required to avoid the contamination from electrons. A pure proton aurora may be identified at the low latitudes equatorward of electron precipitation in the evening-midnight sector [*Sharber*, 1981], which poses an additional difficulty for selecting a qualified event. Fortunately, *Basu et al.* [1987] made a convincing correlation between NOAA 6 particle measurements and Chatanika radar electron density profiles for a proton precipitation event on 9 December 1981. In a wide invariant-latitude range, protons carried all of the energy flux. Here we

![](./images/812355273980116992_14.jpg)

Figure 14. (top) Downward energy fluxes and (middle) characteristic energies of the fitted Maxwellian distribution at 800 km altitude, and (bottom) the resulting electron densities generated by the 3-D Monte Carlo model. The vertical dashed lines mark the three invariant-latitudinal locations $\Lambda = 64.42^\circ, 66.78^\circ$, and $67.11^\circ$.

follow their comparison but using our 3-D Monte Carlo model.

[33] The top two panels in Figure 14 represent the approximate proton precipitating conditions at 800 km altitude: downward energy fluxes and characteristic energies of the fitted Maxwellian distribution, respectively. Again, the semilength of the proton arc is set to be $\Delta = 1000$ km. The MSIS-90 atmosphere is modeled with $F_{10.7} = 290$ and $Ap = 150$. The magnetic field lines have a dip angle of $\gamma = 78^\circ$. Shown in the bottom panel is the calculated electron densities as a function of altitude. To infer the electron densities from the ionization production rates, we have adopted the same effective recombination coefficient $\alpha_{\text{eff}}(h) = 2.5 \times 10^{-6} \exp[-h(km)/51.2] (cm^3 s^{-1})$ as *Basu et al.* [1987] used. The interaction between incoming protons and the atmosphere is complicated because of asymmetric spreading in the tilted magnetic field (see the discussion to Figure 11).

[34] In Figure 15 we show the electron density profiles at three invariant latitudes selected from Figure 14 and present a direct comparison with observations and other model simulation results provided by *Basu et al.* [1987]. Note that there is no contribution from the electron precipitation in other places. Ionizations at these locations are completely produced by protons because of their overwhelming energy flux overhead. It is shown that our calculation results are in excellent agreement with the radar measurements above 130 km altitude. In the lower altitudes our model also works fairly well. This is especially true at $\Lambda = 64.42^\circ$, where the Monte Carlo simulation reproduces a better ionization profile with deeper penetration than the linear transport theory of *Jasperse and Basu* [1982] and the semiempirical continuous energy loss method of *Rees* [1982]. We recognize that there are many uncertainties contributing to the discrepancy between the model predictions and the observations (see the discussion by *Basu et al.* [1987]). Keep in mind that there is longitudinal separation between the measurements of the proton precipitation and the electron densities. However, through the comparison of ionization profiles among the three model results, we can at least draw a conclusion that there is significantly closer agreement between our model and the linear transport theory, both in shape and in magnitude. Another emphasis is on the difference between these two methods. Although *Jasperse and Basu* [1982] introduced an approximate correction factor $\varepsilon$ for the spreading effect, the parallel geometry used in their model determined that the particle fluxes in the atmosphere only depended on the overhead incident protons. In other words, in the linear transport theory, the effect of precipitation conditions at different points above the atmosphere are independent of each other. This is an approximation that is not strictly valid. In contrast, there is no such problem in the Monte Carlo method because it traces all of the test particles at the

![](./images/812355273980116992_15.jpg)

Figure 15. Electron density profiles at different invariant-latitudinal locations: (a) $\Lambda = 64.42^\circ$, (b) $\Lambda = 66.78^\circ$, and (c) $\Lambda = 67.11^\circ$. The results of the Monte Carlo simulation are plotted as solid curves. As a comparison, the radar data (dashed curves), the electron densities calculated from the linear transport theory (solid curves with dots) and from the semiempirical continuous energy loss method of Rees (dotted curves) are given by Basu et al. [1987].

top wherever they may go inside the 3-D simulation domain.

## 4. Summary and Conclusion

[35] Three-dimensional simulation studies based on a Monte Carlo technique were made to assess the transverse beam spreading effect of auroral protons in a three-species atmosphere (O, $\text{N}_2$, $\text{O}_2$). Two types of energy spectra, a monoenergetic and a Maxwellian distribution, were used as injection conditions above the atmosphere. An isotropic angular distribution was assumed as well. The spreading effects of both a fine proton beam and a proton arc of longitudinal and latitudinal extent were studied.

[36] From the view of proton precipitation, the atmosphere can be separated into four zones approximately. Above $\sim$450 km altitude, it is nearly collisionless, and little scattering occurs. In the transition layer of around 250–450 km, the main dispersion of the downward proton beam takes place, where the first few charge exchange collisions play significant roles. In the quasi-equilibrium region from $\sim$120 to $\sim$250 km, the ratio of total downward hydrogen flux to that of downward protons is roughly constant. There is virtually no spreading in this layer due to the frequent charge exchange and electron stripping collisions. Below $\sim$120 km the dense ambient neutrals dramatically attenuate the particle fluxes. Note that the exact altitudes of the zone boundaries vary with the incident energies.

[37] As the energy in the monoenergetic injection increases from 1 to 100 keV, the effective particle beam radius for a fine proton beam narrows roughly from 255 to 50 km. At the same time, the increase of the incident energy causes a downward shift and a thickening of the beam radius profile. A remarkable feature of the downward hydrogen beam width is the double peak structure. One is located at around 500–550 km, and the other is in the quasi-equilibrium zone. It is of interest to see that the effective beam radii according to primary ionization rates are more than 2 times larger than those of particle fluxes, since the average angle of the particle velocity with respect to the vertical direction is increasing away from the central region, which makes the ionization probability rise. The transport of an incoming proton beam in the Maxwellian energy distribution is also simulated, which gives nearly the same result as a monoenergetic spectrum of the same characteristic energy but with a narrower beam radius. It is because the average particle energy in a Maxwellian spectrum is 2 times larger than the characteristic energy. A check of energy conservation shows that most of the particle energy loss is transferred to the ambient neutrals in charge exchange, electron stripping, and ionization collisions.

[38] We also investigated the spreading effect for the proton arcs of longitudinal and latitudinal extent. It was shown that flux intensities at 300 km altitude increase as the semividth of a proton arc increases. With the help of the analysis of atmospheric scale heights and cross-section data, a confident explanation was given to understand the differences between the results of our Monte Carlo model and the estimate of Iglesias and Vondrak [1974]. The comparison in turn validated the effectiveness of the assumption that the transverse beam spreading can be principally determined by the first neutral segments. It was also found that less spreading was demonstrated with the increase of the incident energies. Basu et al. [1987] established a convincing correlation between NOAA 6 pure proton precipitation and Chatanika radar electron density profiles. Excellent agree-

ment was illustrated in the comparison of the Monte Carlo simulation with observations. Although there existed many uncertainties contributing to the error in the measurements, the comparison among the Monte Carlo method, the linear transport theory of *Jasperse and Basu* [1982], and the semiempirical continuous energy loss method of *Rees* [1982] at least provided a validity check of our approach.

[39] The study of the transverse beam spreading effect is of importance to more accurately construct the incident energy fluxes above the atmosphere from the observations (for example, electron density profiles). Results from our 3-D Monte Carlo model will be used to better understand auroral observations, such as those from the global ultravi- olet imager (GUVI) instrument on the Thermosphere-Iono-sphere-Mesosphere Energetics and Dynamics (TIMED) satellite. This quantification of the magnetospheric energy input to the lower thermosphere and ionosphere will also help interpret the measurements made by other instruments on TIMED, namely, the TIMED Doppler interferometer (TIDI) and the sounding of the atmosphere using broadband emission radiometry (SABER). The influence of beam spreading on the comparison of observed and calculated emission line profiles will be included in our future work. Furthermore, the magnetic mirroring effect will be taken into account in a more realistic geomagnetic field model.

[40] Acknowledgments. This research was funded by NASA grant NAG 5-5030, NAG 5-11831, and NSF grant ATM-0090165.

[41] Lou-Chuang Lee thanks Finn Søraas and John R. Jasperse for their assistance in evaluating this paper.

### References
Basu, B., J. R. Jasperse, R. M. Robinson, R. R. Vondrak, and D. S. Evans (1987), Linear transport theory of auroral proton precipitation: A com- parison with observations, *J. Geophys. Res.*, 92, 5920.
Basu, B., J. R. Jasperse, D. J. Strickland, and R. E. Daniell Jr. (1993),Transport-theoretic model for the electron-proton-hydrogen atom aurora:1. Theory, *J. Geophys. Res.*, 98, 21,517.
Basu, B., D. T. Decker, and J. R. Jasperse (2001), Proton transport model: A review, *J. Geophys. Res.*, 106, 93.
Bird, G. A. (1994), *Molecular Gas Dynamics and the Direct Simulation of Gas Flows*, Clarendon, Oxford, England.
Cashwell, E. D., and C. J. Everett (1959), *A Practical Manual on the Monte Carlo Method for Random Walk Problems*, Pergamon, New York.
Davidson, G. T. (1965), Expected spatial distribution of low energy protons precipitated in the auroral zones, *J. Geophys. Res.*, 70, 1061.
Decker, D. T., B. V. Kozelov, B. Basu, J. R. Jasperse, and V. E. Ivanov (1996), Collisional degradation of the proton-H atom fluxes in the atmo- sphere: A comparison of theoretical techniques, *J. Geophys. Res.*, 101,26,947.
Galand, M., and A. D. Richmond (1999), Magnetic mirroring in an incident proton beam, *J. Geophys. Res.*, 104, 4447.
Galand, M., J. Lilensten, W. Kofman, and R. B. Sidge (1997), Proton transport model in the ionosphere: 1. Multistream approach of the trans- port equations, *J. Geophys. Res.*, 102, 22,261.
Galand, M., J. Lilensten, W. Kofman, and D. Lummerzheim (1998), Proton transport model in the ionosphere: 2. Influence of magnetic mirroring and collisions on the angular redistribution in a proton beam, *Ann. Geophys.*,16,1308.
Gussenhoven, M. S., D. A. Hardy, and N. Heinemann (1987), The equator- ward boundary of auroral ion precipitation, *J. Geophys. Res.*, 92, 3273.
Hardy, D. A., M. S. Gussenhoven, and D. Brautigam (1989), A statistical model of auroral ion precipitation, *J. Geophys. Res.*, 94, 370.
Hedin, A. E. (1991), Extension of the MSIS thermosphere model into the middle and lower atmosphere, *J. Geophys. Res.*, 96, 1159.
Iglesias, G. E., and R. R. Vondrak (1974), Atmospheric spreading of pro- tons in auroral arcs, *J. Geophys. Res.*, 79, 280.
Jasperse, J. R. (1997), Transport theoretic solutions for the beam-spreading effect in the proton-hydrogen aurora, *Geophys. Res. Lett.*, 24, 1415.
Jasperse, J. R., and B. Basu (1982), Transport-theoretic solutions for auroral proton and H atom fluxes and related quantities, *J. Geophys. Res.*, 87,811.
Johnstone, A. D. (1972), The spreading of a proton beam by the atmo- sphere, *Planet. Space Sci.*, 20, 292.
Kallio, E., and S. Barabash (2001), Atmospheric effects of precipitating energetic hydrogen atoms on the Martian atmosphere, *J. Geophys. Res.*,106,165.
Kozelov, B. V. (1993), Influence of the dipolar magnetic field on transport of proton-H atom fluxes in the atmosphere, *Ann. Geophys.*, 11, 697.
Lorentzen, D. A. (2000), Latitudinal and longitudinal dispersion of ener- getic auroral protons, *Ann. Geophys.*, 18, 81.
Lundblad, J. A., F. Søraas, and K. Aarsnes (1979), Substorm morphology of greater than 100 keV protons, *Planet. Space Sci.*, 27, 841.
McNeal, R. J., and J. H. Birely (1973), Laboratory studies of collisions of energetic $H^{+}$ and hydrogen with atmospheric constituents, *Rev. Geophys.*,11,633.
Rees, M. H. (1982), On the interaction of auroral protons with the Earth's atmosphere, *Planet. Space Sci.*, 30, 463.
Sharber, J. R. (1981), The continuous (diffuse) aurora and auroral-E ioniza- tion, in *Physics of Space Plasma*, vol. 7, edited by T. S. Chang, B. Coppi, and J. R. Jasperse, p. 115, Scientific, Gainesville, Fla.
Solomon, S. C. (2001), Auroral particle transport using Monte Carlo and hybrid methods, *J. Geophys. Res.*, 106, 107.
Søraas, F., H. R. Lindalen, K. Måseide, A. Egeland, T. A. Sten, and D. S. Evans (1974), Proton precipitation and the $H_{\beta}$ emission in a postbreakup auroral glow, *J. Geophys. Res.*, 79, 1851.
Synnes, S. A., F. Søraas, and J. P. Hansen (1998), Monte-Carlo simulations of proton aurora, *J. Atmos. Sol. Terr. Phys.*, 60, 1695.
Urban, A. (1981), Measurements of low energy auroral ions, *Planet. Space Sci.*, 29, 1353.
Van Dyke, M. (1964), *Perturbation Methods in Fluid Mechanics*, Aca- demic, San Diego, Calif.
Vegard, L. (1948), Emission spectra of night sky and aurora: Reports of the Gassiot Committee, *Phys. Soc. London*, 82.

X. Fang, J. U. Kozyra, and M. W. Liemohn, Space Physics Research
Laboratory, University of Michigan, 2455 Hayward Street, Ann Arbor, MI
48109-2143, USA. (xhfang@umich.edu; jukozyra@engin.umich.edu;
liemohn@engin.umich.edu)
S. C. Solomon, High Altitude Observatory, National Center for
Atmospheric Research, 3450 Mitchell Lane, Boulder, CO 80301, USA.
(stans@ucar.edu)

---
13 of 13