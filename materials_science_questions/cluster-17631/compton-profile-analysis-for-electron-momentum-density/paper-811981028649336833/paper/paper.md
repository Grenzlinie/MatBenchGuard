![](./images/811981028649336833_1.jpg)

# Philosophical Magazine Part B

ISSN: 1364-2812 (Print) 1463-6417 (Online) Journal homepage: http://www.tandfonline.com/loi/tphb20

## Influence of photon beam aperture on Compton line profiles

Renzo Sartori & Raul T. Mainardi

To cite this article: Renzo Sartori & Raul T. Mainardi (1994) Influence of photon beam aperture on Compton line profiles, Philosophical Magazine Part B, 69:1, 113-120, DOI: 10.1080/13642819408236884

To link to this article: http://dx.doi.org/10.1080/13642819408236884

![](./images/811981028649336833_2.jpg)
Published online: 13 Sep 2006.

---

![](./images/811981028649336833_3.jpg)
Submit your article to this journal ![](./images/811981028649336833_4.jpg)

---

![](./images/811981028649336833_5.jpg)
Article views: 1

---

![](./images/811981028649336833_6.jpg)
View related articles ![](./images/811981028649336833_7.jpg)

---

Full Terms & Conditions of access and use can be found at
http://www.tandfonline.com/action/journalInformation?journalCode=tphb20

Download by: [ECU Libraries]
Date: 12 September 2015, At: 03:48

PHILOSOPHICAL MAGAZINE B, 1994, VOL. 69, No. 1, 113-120

# Influence of photon beam aperture on Compton line profiles

By RENZO SARTORI† and RAUL T. MAINARDI‡

Facultad de Matemática, Astronomía y Física, Universidad Nacional de Córdoba,
Laprida 854-5000 Córdoba, Argentina

[Received 24 July 1992 and accepted 22 June 1993]

## ABSTRACT
A procedure to correct Compton profiles for geometrical effects, related to the solid angles subtended for an X-ray source and detector, has been obtained. The geometrical response function for a given experimental set up is found by a Monte Carlo simulation program and is meant to be used as a histogram for convolution purposes. The main features of this function show that it is not peaked at the angle between collimator axes because the maximum is shifted towards greater values and also increasingly broadens as this angle decreases. This procedure corrects the profile shape as a whole, not only its width as was done in previous methods. We have tested this correction with data taken from an experiment in which 60 keV photons from a $^{241}$Am radioactive source were scattered in a triple-distilled water sample and detected with an intrinsic germanium detector. A Compton profile, measured at an angle of $135^{\circ}$, was compared with a tabulated one convoluted with the distribution function, and thus the result of the correction is clearly seen.

## § 1. INTRODUCTION
Compton profile measurements provide valuable information on the electron momentum distribution of a given material and are powerful tools for solid state physics studies, since they provide a direct measurement of the Fermi surface. Performed with an energy dispersive spectrometer, such measurements yield the spectrum of photons scattered by the sample under study. The spectrum can, in turn, be related to the distribution, $J(p_{z})$, of the electron momentum projection, $p_{z}$, along the scattering vector (see fig. 1). The physical processes involved have been reviewed by Williams (1977) and more recently by Cooper (1985).

The starting purpose of this work was to evaluate the possibility of using comparatively weak radioactive sources (about 100 mCi), which are safer to handle, in Compton spectrometers. To accomplish this goal, wider aperture collimators must be used, both for the source and for the detector, producing a distribution of scattering angles about a mean value, different from the angle between the source and detector collimator axes (see fig. 2). Thus a detailed analysis of the influence of the angular beam apertures on the scattered photon energy spectrum had to be performed. When X-ray tubes with slotted slit collimators are used, these considerations are unnecessary since the beam is highly parallel.

The source-sample-detector geometrical arrangement is important for this type of measurements, since $p_{z}$ is dependent on the scattering angle as well as on the energy of the scattered photon. For incoherent scattering, where photon energy shift is related to the scattering angle, the aperture of the beam produces a widening in energies of the

† Fellowship holder of CONICOR, Argentina.
‡ Member of CONICET, Argentina.

0141-8637/94 $10-00 © 1994 Taylor & Francis Ltd.

Fig. 1

![](./images/811981028649336833_8.jpg)

Geometric representation of the Compton interaction, $\vec{\mathfrak{p}}_{0}$ and $\vec{\mathfrak{p}}$ are the incident and scattered electron moments. $\vec{k}_{0}$ and $\vec{k}$ are those of the photon.

Fig. 2

![](./images/811981028649336833_9.jpg)

Schematic experimental arrangement used in Compton profile measurements as considered in this work.

Compton profile, and this effect must be appropriately taken into account. Previous calculations of Eisenberger and Reed (1972) have indicated that closer agreement of data with theoretical predictions is obtained if a correction for the scattering-angle distribution is introduced.

Throughout the literature, little reference to this correction has been found and, when given (Eisenberger and Reed 1972), it was only as a rough estimation of its influence on the Compton profile width. Recently, Hanson and Gigante (1989) have shown that contours of contant efficiency can be found, and these authors used an entirely geometrical approach to evaluate the contribution to the Compton profile width. With our approach we aim at correcting the whole shape of the Compton profile for this effect. To this end the following steps must be taken.

(a) Generate, by a Monte Carlo simulation, the distribution function of scattering angles for each considered geometrical set-up.

(b) Deconvolute, with a well tested unfolding technique, the measured Compton profile.

In this paper we show how the distribution function of scattering angles is obtained by a numerical simulation. We use it next in a practical case to evaluate its influence on the shape of the Compton profile. To avoid the deconvolution process we resorted instead to a convolution of a tabulated Compton profile, free from geometrical influences.

### §2. THEORY
We develop a straightforward formalism to include these geometrical effects into equations that relate the Compton profile to the scattered photon energy spectrum, provided that corrections for detector response and efficiency, and photon absorption in air paths are applied by the usual methods (Williams 1977).

Let us consider in a first approach a parallel beam geometry for both the incident as well as the scattered beams. We do this in the first order to find an equation to compare later with the non-parallel case. The photon energy distribution will then be (Matscheko and Ribberfors 1987)

$$
\begin{aligned}
N\left(h v_{c}\right)= & N o \int_{E_{\mathrm{b}}+h v_{\mathrm{c}}}^{h v_{\max }} \frac{\mathrm{d}^{2} \sigma}{\mathrm{d} \Omega \mathrm{d} h v_{\mathrm{c}}} \phi(h v) \mathrm{d} h v \\
& \times \frac{1}{V} \int_{V} A\left(h v, h v_{c}\right) \Delta \Omega \mathrm{d} V,
\end{aligned}
$$

where $N(h v_{c})$ is the number of scattered photons with energies between $h v_{c}$ and $h v_{c}+d h v_{c} ; h v_{c}$ is the $h v\{1 /[1+h v(1-\cos \Theta) / m c^{2}]\} ; N o$ is the number of scattering electrons; $h v_{\max }$ is the maximum incident photon energy; $E_{\mathrm{b}}$ is the electron binding energy; $\mathrm{d} \sigma / \mathrm{d} \Omega \mathrm{d} h v_{c}$ is the double differential scattering cross-section; $A(h v, h v_{c})$ is the factor to take into account attenuations in air paths, between source-sample and sample-detector; $\phi(h v)$ is the incident photon energy distribution; $V$ is the sample volume; and $\Delta \Omega$ is the solid angle subtended by the detector from each point in the sample.

The data, as collected in a multichannel analyser, are corrected by detector response and efficiency as done routinely for each measurement taken with our high purity germanium detector.

We consider now an incident mono-energetic photon beam of energy $h\nu_0$ such that
$$
\phi(h\nu)=I_0\delta(h\nu-h\nu_0), \tag{2}
$$
and that the cross-section is as given by Ribberfors (1975)
$$
\frac{\mathrm{d}^2 \sigma}{\mathrm{d}\Omega \mathrm{d}h\nu_c}=\frac{r_0^2 m \nu_c}{2h\nu}\left(\nu_c/\nu+\nu/\nu_c-\sin^2 \Theta\right)\frac{J(p_z)}{q}. \tag{3}
$$

Substituting eqns. (2) and (3) into eqn. (1) we obtain
$$
\begin{aligned}
N(h\nu_c)=&\frac{NoI_0 r_0^2 m \nu_c}{2hq\nu_0}\left(\nu_c/\nu_0+\nu_0/\nu_c-\sin^2 \Theta\right) \\
&\times J(p_z)\frac{1}{V}\int_V A(h\nu_0, h\nu_c)\Delta\Omega dV, \tag{4}
\end{aligned}
$$
where
$$
q=|\mathbf{q}|=\frac{\left[(h\nu_c)^2+(h\nu_0)^2-2h^2 \nu_c \nu_0 \cos \Theta\right]^{1/2}}{c}, \tag{5}
$$
and
$$
p_z=\mathbf{p}\cdot\mathbf{q}/q=\frac{h^2 \nu_c \nu_0(1-\cos \Theta)-mc^2(h\nu_0-h\nu_c)}{c\left[(h\nu_c)^2+(h\nu_0)^2-2h^2 \nu_c \nu_0 \cos \Theta\right]^{1/2}}. \tag{6}
$$

Equation (3) for the double differential cross-section has been derived within the impulse approximation, which assumes that during the interaction there is no change in the field of the atom as seen by the scattering electron, or equivalently that the electron is free but moving in a constant field.

If our experimental set-up, as shown in fig. 2, has instead of a unique value for both the incident and scattered directions a distribution of angles due to the collimator's aperture, of relative weight $n(\Theta)$ between $\Theta$ and $\Theta+\mathrm{d}\Theta$, we can rewrite eqn. (4) in a differential form to obtain
$$
\begin{aligned}
\mathrm{d}N(h\nu_c)=&\frac{NoI_0 r_0^2 m \nu_c}{2h\nu_0}n(\Theta) \\
&\times\left(\nu_c/\nu_0+\nu_0/\nu_c-\sin^2 \Theta\right)\frac{J(p_z)}{q}\mathrm{d}\Theta. \tag{7}
\end{aligned}
$$
$n(\Theta)$ includes attenuation in the sample and the solid angle factors. We now consider all angles allowed by the collimation between a minumum $\Theta_{\min}$ and a maximum $\Theta_{\max}$ by an integration such that
$$
\begin{aligned}
\mathrm{N}(h\nu_c)=&\frac{NoIr_0^2 m \nu_c}{2h\nu_0 q}\int_{\Theta_{\min}}^{\Theta_{\max}}n(\Theta) \\
&\times\left(\nu_c/\nu_0+\nu_0/\nu_c-\sin^2 \Theta\right)J(p_z)\mathrm{d}\Theta. \tag{8}
\end{aligned}
$$

In practice one measures $N(h\nu_0)$: thus to obtain $J(p_z)$, the Compton profile, eqn. (8) must be deconvoluted using the calculated distribution function $n(\Theta)$.

## §3. RESULTS

### 3.1. Monte Carlo simulation

Unable to find a way to derive a functional form for $n(\Theta)$, mainly because detector and source are considered as extended surfaces, we resorted to a Monte Carlo simulation to generate numerically a frequency distribution to be used in a tabular form for convolution purposes. Several starting assumptions are needed.

(1) The radioactive source is flat, homogeneous and mono-energetic.
(2) The attenuation of photons at the sides and edges of the collimators is infinite (i.e. if $\mu=\infty$).
(3) Our sample has a flat surface facing towards both the detector and the source. The normal to this surface lies in the plane of the collimator axes. The scattering volume (see fig. 2) is much smaller than the sample volume.
(4) The detector efficiency is considered 100% throughout the scattering energies range. This is valid for our germanium detector-americium-241 source combination.

The geometrical arrangement considered is the one of fig. 2 and all relevant dimensions are fed into the program. The source-to-sample and detector-to-sample distances were 7 cm and 12 cm, respectively. Distances were measured using a cathetometer, i.e. with an appreciation of one tenth of a millimetre. Both collimators were of diameter 0.5 cm, the source one was 3 cm long with an aperture of $\pm9.5^\circ$ and the detector one 8.5 cm long.

In order to write down trajectories equations, two coordinate systems must be considered: a primary one centred at the radioactive source and a secondary one with its origin at the intersection of the collimators axes. The relationship between coordinate systems must be specified in terms of the angle between collimator's axes.

The numerical Monte Carlo simulation starts assigning initial values randomly to an emission point from the radioactive source. According to the first assumption above, any point being equally probable.

A polar angle is selected next, at random, for the photon trajectory, starting on the emission point. If the photon strikes the source collimator, due to the second assumption the event is discarded and the process starts at the source again. If the trajectory hits the water sample, the photon is allowed to penetrate up to a point in the sample chosen randomly with an exponentially decaying probability, determined by the mass attenuation coefficient at the photon energy and taken from tables (McMaster, Kerr del Grande, Mallett and Hubbell 1969).

At this intersection point the photon can be photoelectrically absorbed or scattered. If absorbed the event is lost and the calculation starts again at the source. If scattered it can be either coherent or incoherently. In the first case we have assumed that the cross-section for coherent scattering is independent of $\Theta$ in an interval a few degrees around the scattering angle. In the second case it is a Klein-Nishina distribution type. Finally, if the scattered photon trajectory strikes the detector it is taken as a successful event and it is stored in terms of its energy in bins 35 eV wide, this value being one third of the channel energy width in the multichannel analyser used in our measurements. The energy of the photon is determined from the angle between the incident and scattered trajectories using the Compton relation.

The results of this simulation are illustrated in fig. 3, for six different values of the angle between collimators axes. It should be noted that the distribution broadens

![](./images/811981028649336833_10.jpg)

Scattering angle distributions, $n(E)=n(\Theta)\mathrm{d}\Theta/\mathrm{d}E$, for different angles between collimators axes as shown on the top of each curve. $E$ is the energy of the scattered photon.

considerably as this angle decreases. The peak also shifts as shown by the difference between the arrows positions and the maximum of the distribution.

Once the fundamentals of this correction procedure are mastered, sample tilt or orientation and finite thickness can be easily incorporated to the simulation code.

### 3.2. Experimental

We measured the Compton profile of a water sample at an angle of $135^{\circ}\ (\pm1^{\circ})$, in the fixed geometrical set-up, described above. The error reported in the angle between collimator axes' value is affected mainly by the positioning of the water sample in relation to both collimators.

The cylindrical intrinsic germanium detector had an area of 25 mm and a thickness of 5 mm, with a resolution of 300 eV at 60 KeV. The 100 mCi circular americium 241 radioactive source had a diameter of 0·72 cm. The triple distilled water sample was contained in a large plastic vial of 5 cm diameter with a thin (0·02 mm) mylar window.

To appreciate the influence of our correction, we avoided deconvolution of data altogether since it is reported in the literature that existing methods of deconvolution introduce different amounts of errors (Paatero, Manninen and Paakkari 1974). A standardized Compton profile of water from Williams (1976), for which the geometrical effect is absent, was convoluted with our numerically generated geometrical distri- bution to obtain a standardized profile artificially influenced for geometrical effects.

It should be kept in mind that the distribution $n(\Theta)$ is to be used to subtract this geometrical effect from measured electron momentum distributions.

Figure 4(a) shows two sets of data, one taken from Williams (1976) and the other from our own spectrometer. In this fig. data is not corrected for geometrical effects, or equivalently we might say that the angular distribution is considered as a delta function.

Figure 4(b) presents the data from Williams (1976) to which the geometrical effects have been artificially added by means of a convolution with our distribution $n(\Theta)$ with the same measured points of fig. 4(a). Two features are important when comparing these figures. The convoluted curve is shifted towards lower energies and is broadened as well. The result is an improved match between both sets of data.

Fig. 4

![](./images/811981028649336833_11.jpg)

(a) Comparison between the relative intensities of a measured Compton spectrum for a water sample and the calculated spectrum from Williams (1976) without taking geometrical effects into account. (b) Same as (a) but now taking into account geometrical effects.

The fitting errors between curves in fig. 4(a) and in fig. 4(b) have been calculated, using the criteria.exposed by Sekine and Baba (1976), where the root mean square deviations between the two distributions are found to be given by

$$
\left(\overline{\Delta^{2}}\right)^{1 / 2}=\Sigma \Delta_{i}^{2} y_{i}^{0} / \Sigma y_{i}^{0},
$$

where

$$
\Delta_{i}=\left(y_{i}-y_{i}^{0}\right) / y_{i}^{0},
$$

and $y_{i}^{0}$ are data from the true or reference spectra and $y_{i}$ the observed data, both at the $i$th channel.

The sums on the above expression are taken over all channels involved in the curves comparison. We have seen that not all the channels depicted in fig. 4 are significant and some on both tails should be suppressed in order to obtain the lowest value of the root mean square deviation.

For the pair of curves of fig. 4(a) the root mean square deviation amounts to $34 \%$, while for the curves in figure 4(b), it reduces to $4.9 \%$. According to the recommendations of Sekine and Baba (1976), this last case is within acceptable limits, while the first clearly is not.

Our measured Compton profile has a full width half maximum (FWHM) of 1500 eV at 50 keV (a 60 keV photon scattered at $135^\circ$). The contribution to the FWHM calculated with our correction consists of a 1260 eV actual Compton width plus a 800 eV geometrical contribution. The standard deviation, $\sigma$, is thus 340 eV.

## §4. CONCLUSIONS
A formalism to subtract geometrical effects from a Compton profile has been developed. In order to be applicable this method relies on a numerical deconvolution through the use of a scattering angle distribution function. This distribution must be found previously by a numerical simulation procedure for each geometrical set-up and includes all the geometrical and physical effects that contribute to the shape of a measured Compton profile.

The contributions to the whole width of the Compton profile curve for different geometrical correction schemes have been found to be equivalent. The equation derived by Eisenberger and Reed (1972) gives an estimated value of 300 eV for the standard deviation, while with eqn. (4) of Hanson and Gigante (1989) we obtain 270 eV. The width contribution obtained with the method proposed here is 340 eV. The differences among these values are probably due to differences in the assumptions and definitions to derive the equations. To this respect we should stress again that our method corrects the shape of the Compton profile for geometrical effects because it performs a deconvolution as a function of energy over the whole peak, while Eisenberger and Reed (1972) and Hanson and Gigante (1989) provide an estimation of the width that should be subtracted in quadrature, as though all distributions were Gaussian, which is seldom the case.

We must finally emphasize the fact that, although the distribution function $n(\Theta)$ for large angles is fairly narrow, for angles closer to $90^\circ$ it widens considerably and corrections will be much more important. To attain a 1% accuracy in the Compton profile taking into account this correction for geometry is unavoidable.

## ACKNOWLEDGMENTS
This work was carried out under a grant from the National Research Council of Argentina (CONICET) and the Research Council of the Province of Cordoba (CONICOR).

Mr Richard E. Trucco (now at GASL, Ronkonkone, NY, USA) started this study while a student of one of us (R.T.M.) at the University of Cordoba. We are deeply indebted to his ground-breaking steps, although on a different approach than this one.

## REFERENCES
COOPER, M. J., 1985, *Rep. Prog. Phys.*, **48**, 415.
EISENBERGER, P., and REED, W. A., 1972, *Phys. Rev. A*, **5**, 2085.
HANSON, A. L., and GIGANTE, G. E., 1989, *Phys. Rev. A*, **40**, 171.
MATSCHEKO, G., and RIBBERFORS, R., 1987, *Phys. Med. Biol.*, **32**, 577.
MCMASTER, W. H., KERR DEL GRANDE, N., MALLETT, J. H., and HUBBELL, J. H., 1969, *Compilation of X-Ray Cross Sections*, Lawrence Radiation Laboratory (Livermore), Report UCRL-50174, Sec. II, Rev. 1.
PAATERO, P., MANNINEN, S., and PAAKKARI, T., 1974, *Phil. Mag.*, **30**, 1281.
RIBBERFORS, R., 1975, *Phys. Rev. B*, **12**, 2067.
SEKINE, T., and BABA, H., 1976, *Nucl. Instrum. Meth.*, **133**, 171.
WILLIAMS, B. G., 1976, *Acta crystallogr. A*, **32**, 513; 1977, *Compton Scattering* (New York: McGraw-Hill).