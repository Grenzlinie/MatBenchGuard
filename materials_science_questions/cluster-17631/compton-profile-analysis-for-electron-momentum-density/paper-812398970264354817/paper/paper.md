![](./images/812398970264354817_1.jpg)

Available online at www.sciencedirect.com

![](./images/812398970264354817_2.jpg)

Nuclear Instruments and Methods in Physics Research A 508 (2003) 394–403

![](./images/812398970264354817_3.jpg)

# Improvements in $\gamma$-ray reconstruction with positive sensitive Ge detectors using the backtracking method

L. Milechina*, B. Cederwall

Department of Physics, Royal Institute of Technology, AlbaNova University Center, Stockholm S-106 91, Sweden

Received 24 September 2002; received in revised form 14 April 2003; accepted 17 April 2003

## Abstract

Gamma-ray tracking, a new detection technique for nuclear spectroscopy, requires efficient algorithms for reconstructing the interaction paths of multiple $\gamma$ rays in a detector volume. In the present work, we discuss the effect of the atomic electron momentum distribution in Ge as well as employment of different types of figure-of-merit within the context of the so called backtracking method.

© 2003 Elsevier B.V. All rights reserved.

PACS: 07.85.Ne; 29.30.Kv; 29.40.Gx

Keywords: Gamma-ray tracking; Gamma-ray spectroscopy; Segmented germanium detectors

## 1. Introduction

High-resolution $\gamma$-ray spectrometers are key instruments for nuclear structure research. Future advancements in the field will be closely connected with the development of radioactive ion beams which allow production of exotic nuclei in the drip-line regions. The study of such highly unstable quantum systems is hampered by adverse experimental conditions. In addition to extremely small production rates one is often faced with Doppler broadening of $\gamma$ lines due to large (relativistic) source velocities, large $\gamma$-ray multiplicities (up to $M_{\gamma} \approx 30$) and severe X-ray/Brems- strahlung background. Gamma-ray spectroscopy under such conditions requires powerful $4\pi$ $\gamma$-ray spectrometer arrays. However, the current state of the art for high-resolution $4\pi$ $\gamma$-detector arrays as represented by *Euroball* [1] and *Gammasphere* [2] has reached its limits in performance. The photopeak efficiency of these arrays is restricted to about $10\%$ for single $\gamma$ rays at $1.3\,\text{MeV}$, primarily by scattered $\gamma$ rays escaping from the Ge detectors and by the solid angle. A relatively high peak-to-total ratio, $P/T$, of about $60\%$, (for the same $\gamma$-ray energy) is achieved by means of escape suppression, rejecting the signals that are in coincidence with the ones from the surrounding bismuth germanate (BGO) shields. These values are, however, reduced sig- nificantly for large $\gamma$-ray multiplicities due to the decrease in "isolated hit probability". For example the calculated efficiency for $\gamma$-ray multiplicity $M_{\gamma}=30$ is $7\%$ [1]. In this case the value of $P/T$ is about $50\%$.

*Corresponding author.
E-mail address: larissa@nuclear.kth.se (L. Milechina).

0168-9002/03/$- see front matter © 2003 Elsevier B.V. All rights reserved.
doi:10.1016/S0168-9002(03)01698-X

In order to increase the efficiency and peak-to-
total ratio, previous developments of the detector
systems have gone in the direction of enlarging the
size of the Ge crystals, minimizing the dead space
between detectors and reducing the impurity
concentrations in the crystals to improve energy
resolution. By introducing electric segmentation of
the Ge crystal contacts, the energy deposition in
even a large detector can be localized to a limited
region, thereby reducing Doppler broadening in
studies of $\gamma$ rays emitted at large source velocities.
Two-fold segmented coaxial detectors were first
introduced in Gammasphere and segmentation
schemes with higher granularity are now imple-
mented in the most recent Ge detector arrays:
Exogam [3], Miniball [4] and Vega [5]. These
detector arrays still include in their design escape
suppression shields.

An obvious drawback with the use of escape
suppression shields is that they limit the high-
resolution part of the sensitive solid angle and
thereby the full-energy efficiency. The develop-
ment of electric segmentation of large germanium
crystals has, however, laid the foundation for an
entirely new concept for a high-resolution $4\pi\gamma$
array based on a shell built entirely from highly
segmented Ge detectors. Instead of suppressing $\gamma$
rays that scatter between detectors, a novel
method where the scattering path of each $\gamma$ ray is
identified and the full energy is recovered is under
development. This technique is called $\gamma$-ray track-
ing and promises a dramatic increase in perfor-
mance compared to existing $\gamma$-detector arrays.
Based on this approach, the detector projects of
MARS [6], GRETA [7] and AGATA [8] have been
initiated.

A crucial requirement for the concept of $\gamma$-ray
tracking is the ability to accurately determine the
energies and positions of the individual interac-
tions in the Ge crystals. The position sensitivity
necessary for a successful implementation of the $\gamma$-
ray tracking scheme is of the order of one up to a
few millimeters. This corresponds to an effective
granularity of tens of thousands of voxels per Ge
detector. Since it is impossible to achieve such a
high degree of granularity by a physical segmenta-
tion of the Ge crystals, another solution to the
problem has been developed. This approach is
based on pulse shape analysis of the signals from
the segment contacts which are induced by the
drift of the charge carriers released by an interac-
tion. Pulse shape analysis techniques have proven
to provide a high degree of position sensitivity as
well as high-resolution energy and timing informa-
tion [9–11].

Another vital ingredient for the $\gamma$-ray tracking
technique is the development of powerful algo-
rithms that may resolve the tracks of multiple,
coincident $\gamma$ rays in the detector system. Such
developments have so far proceeded along two
parallel lines: cluster recognition [12] and back-
tracking [13]. Both methods rely on the kinematics
of Compton scattering for reconstructing valid
interaction paths. The reliability of the reconstruc-
tion process is limited most importantly by the
finite position resolution of the detector system
and to a lesser extent by the energy resolution.
These effects have been included in previous
studies. However, since in a Ge detector the
directions of the recoiling Compton electrons are
not determined, an additional fundamental physi-
cal uncertainty remains. This uncertainty arises
from the fact that when a photon Compton
scatters on a bound atomic electron the momen-
tum transfer from the electron will vary stochas-
tically, depending on the momentum distribution
of the electronic state. This is reflected as an
uncertainty in the scattering angle. In this paper,
the implications of this so called Compton profile
effect for $\gamma$-ray tracking are reported. A compar-
ison between different variations of the back-
tracking scheme is also presented.

## 2. Simulations

The response of a spherical shell of Ge detectors
to $\gamma$ rays emitted from a centrally placed source
was investigated using the Monte Carlo code
GEANT 3.21 [14]. The detector array is approxi-
mated by a solid shell of germanium with an inner
and outer radius of 15 and 24 cm, respectively. The
inner radius is given by the minimum required size
of the scattering chamber in typical nuclear
structure experiments. The thickness of the shell
is determined to give an adequate full-energy

detection efficiency for $\gamma$-ray energies up to around 10 MeV. However, the present study focuses on $\gamma$ rays up to a few MeV which is the energy range of primary interest for nuclear structure studies. In the simulation, the coordinates of the interaction points and their deposited energies for each $\gamma$ ray emitted from the source are recorded for later use in the reconstruction algorithm. Pair production was not included in the simulation since it is negligible for $\gamma$ rays with energies up to a few MeV. However, events involving pair production may be accounted for with high efficiency in the tracking algorithm if the need arises [8].

In order to obtain realistic conditions, electronic and position noise were added to the simulated interaction points. The uncertainty (squared) in the $\gamma$-ray interaction energy detected by a Ge detector can be expressed by the following relation:

$$
\sigma_{\mathrm{res}}^{2}=\sigma_{\mathrm{stat}}^{2}+\sigma_{\mathrm{noise}}^{2}. \tag{1}
$$

The first term reflects the fluctuation of the number of charge carriers released in the germa- nium crystal. For this term the following expression holds:

$$
\sigma_{\text {stat }}^{2}=F u_{\mathrm{Ge}} E^{\text {dep }}. \tag{2}
$$

In Eq. (2) $u_{\mathrm{Ge}}=2.96 \mathrm{eV}$ is the average energy required to produce an electron-hole pair and $E^{\text {dep }}$ is the energy deposited in the Ge crystal. In this work, we assume the Fano factor $F=0.12$ [15] and the electronic noise $\sigma_{\mathrm{el}}$ is taken to be $300 \mathrm{eV}$. With these parameters, we obtained an energy resolution of 2.32 and $1.16 \mathrm{keV}$ for 1332 and $122 \mathrm{keV} \gamma$ rays, respectively, in reasonable agreement with typical experimental resolutions of germanium detectors. To account for the energy threshold associated with the processing of the experimental pulse shapes, interactions with deposited energy less than $1.5 \mathrm{keV}$ are excluded from the tracking procedure. The spatial coordinates of the interaction points for a real detector are determined by means of pulse shape analysis [9-11]. We here assume that the interaction positions in the Ge detector can be determined within an uncertainty, $\sigma_{\text {pos }}$, of the order of $1 \mathrm{~mm}$. However, results for other degrees of position resolution are also presented.

Pulse shape analysis methods usually have difficulty resolving close-lying interaction points within the same crystal region belonging to an electric contact segment. This is especially the case if the interaction points are significantly closer to each other than the segment dimensions. We, therefore, introduce the parameter resolving distance, $d_{\text {res }}$, for which the following relation with the spatial resolution is maintained:

$$
d_{\text {res }}=5 \sigma_{\text {pos }}. \tag{3}
$$

Each interaction point from the simulation is first moved a random distance according to a Gaussian distribution in three dimensions with standard deviation $\sigma_{\text {pos }}$. The interaction points which are situated at a distance less than $d_{\text {res }}$ from each other are then merged into one. The sum of the interaction energies over the merged points and a position coordinate weighted by the deposited energies are awarded to the new point. For each event, i.e. set of $\gamma$ rays emitted simultaneously from the source, the resulting set of interaction points and associated interaction energies provide the input data for our tracking algorithm.

At present, there are two main approaches proposed for reconstructing the path of $\gamma$ rays scattering in a segmented Ge detector; the backtracking [13] and clusterisation methods [12]. In this work we limit ourselves to the backtracking method. Two main features are addressed: first, the tracking performance is quite sensitive to the choice of the formula for the figure-of-merit (the definition will be given below). Different figures-of-merit are therefore investigated in some detail. Second, we investigate the influence of the initial momentum of the Compton scattered electron on the reconstruction results. This is a physical limitation that has previously not been considered in detail in this context, although its effect on Compton imaging has been reported [16].

### 3. Reconstruction algorithm

In the backtracking algorithm the reconstruction of the $\gamma$-ray path starts from the last interaction point, i.e. from the assumed photoeffect point, and then proceeds backwards along

the track, from point to point, until the source position is reached. The first guess for the photoelectric end-point interaction is based on the distributions of individual Compton and photoeffect interaction energies in Ge [13]. The final photoelectric interaction is most probable in the energy range from about 100 to 250 keV, indepen- dently of the initial $\gamma$-ray energy. Therefore, an interaction point with a deposited energy in this interval (or as close to it as possible) is chosen as the starting point for the reconstruction algorithm. The second interaction point is searched for within a distance, $d_{\max }^{\mathrm{ph}}$ (ph denotes photo-effect), limited by assigning a maximum probability limit for the photo-effect to occur, $P_{\max }^{\mathrm{ph}}$. The search distance, $d_{\max }^{\mathrm{ph}}$, therefore depends on the detector material (i.e. Ge) and the final $\gamma$-ray energy which is given by the deposited energy, $E_{1}^{\text {dep }}$, in the assumed final photo-effect point. If a second interaction point is found, a third point is searched for within a distance limited by the probability for Compton scattering $P_{\max }^{\mathrm{cmp}}$, and so on. The parameters $P_{\max }^{\mathrm{ph}}$ and $P_{\max }^{\mathrm{cmp}}$ are chosen to optimize the speed and performance of the reconstruction process.

For every three points in the reconstructed track a figure-of-merit, $w^{\text {step }}$, is evaluated. The value of $w^{\text {step }}$ gauges how well this three-point sequence matches the Compton scattering formula

$$
\cos \theta^{\mathrm{en}}=1-m_{\mathrm{e}} c^{2}\left(\frac{1}{E_{\gamma^{\prime}}}-\frac{1}{E_{\gamma}}\right). \tag{4}
$$

where $m_{\mathrm{e}} c^{2}=0.511 \mathrm{MeV}$ is the electron rest mass and $E_{\gamma}\left(E_{\gamma^{\prime}}\right)$ is the $\gamma$-ray energy before (after) the second interaction. If the value of $w^{\text {step }}$ is acceptable with respect to a predefined limit, $W_{\lim }^{\text {step }}$, the next possible interaction point is searched for within a distance $d_{\text {max,i }}^{\text {cmp }}$. The index i here denotes the current interaction point in the reconstructed track. As soon as two interaction points are chosen, the track is checked for termination, i.e. in the direction of the source position, by calculating the total figure-of-merit, $w^{\text {tot }}$. If this value is better than a predefined limit, $W_{\lim }^{\text {tot }}$, the track is considered as a good candidate and is stored temporarily in a stack. After that, the reconstruction process proceeds with any remaining interaction points in the event. When all interaction points are checked as candidates for a photoelectric interaction the stack is evaluated. The track with the best value of $w^{\text {tot }}$ is chosen as a good one. The interaction points of this track are consequently booked. If a track with the next best value of $w^{\text {tot }}$ has no common interaction points with the previously selected one, this track is also taken as a good one. This procedure continues until all tracks in the stack are checked. At the end of the event reconstruction process, the successfully reconstructed $\gamma$-ray interaction sequences together with their total figures-of-merit, $w^{\text {tot }}$, are stored for later analysis.

## 4. Choice of figure-of-merit

As mentioned above, the reconstruction of a $\gamma$- ray scattering path in the backtracking algorithm starts from the last photo-effect point and proceeds toward the source. For every sequence of three points in the track a "local" figure-of-merit, $w^{\text {step }}$, is calculated. This value gives an estimate of how well this sequence of points matches the physics of the scattering process. When a complete sequence of interaction points has been found, all values of $w^{\text {step }}$ are weighted together to form a total figure-of-merit which can be used to evaluate the likelihood that the interaction sequence was correctly identified.

### 4.1. Choice of local figure-of-merit

The choice of formula for calculating $w^{\text {step }}$ is essential for the reconstruction results. A few different figure-of-merit formulae were, therefore, tested and the results are presented below. A common feature of the different local figures-of-merit, $w^{\text {step }}$, is to compare the energy determination of the scattering angle (Eq. (4)) with the angle deduced from the measured interaction positions:

$$
\cos \theta^{\mathrm{pos}}=\frac{\overrightarrow{12} \cdot \overrightarrow{23}}{|\overrightarrow{12}||\overrightarrow{23}|}. \tag{5}
$$

Here the symbols 1, 2 and 3 represent the spatial coordinates of the three interaction points. In the ideal case, i.e. without energy and position uncertainties and if the Compton electron is

initially at rest, we have $\theta^{\text{en}} = \theta^{\text{pos}}$. For realistic conditions, this will of course rarely happen. However, we may apply our knowledge of the uncertainties in the parameters determining $\theta^{\text{en}}$ and $\theta^{\text{pos}}$ in order to translate the difference between $\theta^{\text{en}}$ and $\theta^{\text{pos}}$ into an estimate of the probability that the true interaction sequence has been found.

The simplest figure-of-merit, $w^{\text{step}}$, that was tested is merely the absolute difference between $\theta^{\text{en}}$ and $\theta^{\text{pos}}$

$$
w_{1}^{\text{step}} = |\theta^{\text{en}} - \theta^{\text{pos}}|. \tag{6}
$$

If for the moment we disregard the effects of the finite electron momentum, only the position resolution and energy resolution of the Ge detector array contribute to the difference between $\theta^{\text{en}}$ and $\theta^{\text{pos}}$ for a correctly identified interaction sequence. In order to take the detailed effect of these uncertainties into account we have introduced a second figure-of-merit which is related to the expected uncertainties for the interaction energies and their positions. Let $\sigma_{\theta^{\text{en}}}$ and $\sigma_{\theta^{\text{pos}}}$ denote the uncertainties for the estimated scattering angles $\theta^{\text{en}}$ and $\theta^{\text{pos}}$, respectively. They are determined from the measurement uncertainties for energy and position, $\sigma_{\text{en}}$ and $\sigma_{\text{pos}}$, and Eqs. (4) and (5). It should be noticed that, in addition to uncertainties in the positions of the interaction points, $\sigma_{\theta^{\text{pos}}}$ also includes an uncertainty in the position of the source. This value was taken to be 0.5 mm, which is reasonable for many experiments involving nuclear reactions. However, since the inner radius of the detector system is 15 cm, the results are not very sensitive to the uncertainty of the source position. The mean values of $\sigma_{\theta^{\text{en}}}$ and $\sigma_{\theta^{\text{pos}}}$ for $\gamma$ rays of energy 1332 keV scattered in a detector array of the chosen geometry are $0.2^{\circ}$ and $7^{\circ}$, respectively, for $\sigma_{\text{pos}} = 1$ mm. We assume that $\theta^{\text{en}}$ and $\theta^{\text{pos}}$ are Gaussian distributed. Then the second figure-of-merit, $w_{2}^{\text{step}}$, is derived from the convolution of these two Gaussian distributions, leading to

$$
w_{2}^{\text{step}} = \frac{|\theta^{\text{en}} - \theta^{\text{pos}}|}{\sigma} \tag{7}
$$

where $\sigma = \sqrt{\sigma_{\theta^{\text{en}}}^{2} + \sigma_{\theta^{\text{pos}}}^{2}}$.

Yet another, more powerful, figure-of-merit is obtained when in addition, the $\gamma$-ray interaction probabilities for the detector material are taken into account. For the first step in the reconstruction sequence, a figure-of-merit based on the relative photo-effect cross-section is calculated

$$
w_{3,1}^{\text{step}} = P_{\text{ph}}(1 - P_{\text{tot}}). \tag{8}
$$

Subsequently, the following figure-of-merit is awarded to each of the following steps:

$$
w_{3,i}^{\text{step}} = \text{e}^{-|\theta^{\text{en}} - \theta^{\text{pos}}|/\sigma}P_{\text{comp}}(1 - P_{\text{tot}}). \tag{9}
$$

Here the index $i$ takes the values $i = 2, ..., N - 1$ out of the $N$ interaction points in the track and the parameters $P_{\text{ph}}$, $P_{\text{comp}}$ and $P_{\text{tot}}$ are the photoelectric, Compton and total absorption probabilities, respectively, evaluated for each distance between two interaction points.

### 4.2. Choice of total figure-of-merit

At the end of each track the total figure-of-merit, $w^{\text{tot}}$, may be calculated in different ways. We have investigated two different formulae for combining the local figures-of-merit, $w^{\text{step}}$, into $w^{\text{tot}}$:

$$
w_{1}^{\text{tot}} = \frac{1}{N - 1} \sum_{i=1}^{N-1} w_{i}^{\text{step}} \tag{10}
$$

and

$$
w_{2}^{\text{tot}} = \sqrt[N-1]{\prod_{i=1}^{N-1} w_{i}^{\text{step}}}. \tag{11}
$$

### 4.3. Reconstruction results for different figures-of-merit

By applying the reconstruction algorithm to a large number of simulated events, we obtain an ensemble of $\gamma$-ray interaction sequences, each represented by its total figure-of-merit and its reconstructed $\gamma$-ray energy, i.e. the sum of the interaction energies for that particular sequence. By varying the cut on the total figure-of-merit, the optimal balance between photopeak efficiency and background rejection may be found. The reconstruction results are determined by producing an energy spectrum containing the total energies of

the $\gamma$-ray tracks that have passed the selection criteria. From this spectrum we extract two performance parameters: the reconstructed photopeak efficiency, $\varepsilon$, and the peak-to-total $P/T$. The reconstruction efficiency, $\varepsilon$, is the ratio between the number of the tracks in the reconstructed photopeak $N_{\gamma}^{\text{ph}}$ and the number of the events in the original Monte-Carlo simulated photopeak. The $P/T$ is the ratio between $N_{\gamma}^{\text{ph}}$ and the total number of reconstructed events. In the original Monte Carlo simulated spectra, the peak-to-total $P/T$ and photopeak efficiency $\varepsilon$ for 1332 keV $\gamma$ rays are 79% and 72%, respectively. The reconstruction results for the described "local" figures-of-merit are shown in Figs. 1 and 2. In addition to $\varepsilon$ and $P/T$ we also plot the values of the product $\varepsilon \cdot P/T$, which may serve as a general performance parameter. Figs. 1 and 2 reveal a considerable

![](./images/812398970264354817_4.jpg)

Fig. 1. Dependence of reconstruction efficiency, $\varepsilon$ and $P/T$ on position uncertainty, $\sigma_{\text{pos}}$, for the different figures-of-merit described in the text. The $\gamma$-ray multiplicity is fixed at $M_{\gamma}=5$ and the $\gamma$-ray energy is 1332 keV.

![](./images/812398970264354817_5.jpg)

Fig. 2. Dependence of reconstruction efficiency, $\varepsilon$ and $P/T$ on $\gamma$-ray multiplicity, $M_{\gamma}$, for the different local figures-of-merit described in the text. The $\gamma$-ray energy is 1332 keV and the position uncertainty, $\sigma_{\text{pos}}=1$ mm.

difference in performance between the different figures-of-merit. The reconstruction efficiency for the simplest figure-of-merit, $w_{1}^{\text{step}}$, is, perhaps surprisingly, competitive for low multiplicity but decreases dramatically as the multiplicity is increased. The performance obtained by using $w_{1}^{\text{step}}$ is also relatively speaking most sensitive to the degree of position resolution. The figure-of-merit $w_{3}^{\text{step}}$, where the most physical information on the scattering process is included, has the best reconstruction results both in terms of photopeak efficiency, $\varepsilon$, and peak-to-total, $P/T$, as well as the product $\varepsilon \cdot P/T$.

The two formulae for calculating the total figure-of-merit for each track are compared in Figs. 3 and 4. It is evident that $w_{2}^{\text{tot}}$ yields the best results. The results presented in Figs. 1 and 2 are obtained by applying $w_{2}^{\text{tot}}$.

![](./images/812398970264354817_6.jpg)

Fig. 3. Comparison between the two formulae for calculating the total figure-of-merit (Eqs. (10) and (11)) as a function of position uncertainty, $\sigma_{\text{pos}}$, for local figure-of-merit $w_{3}^{\text{step}}$. The $\gamma$-ray energy is 1332 keV and $M_{\gamma}=25$.

## 5. Influence of electron momentum

The Compton scattering formula (Eq. (4)) is derived from the energy and momentum conservation laws for $\gamma$-ray scattering on a free electron at rest. But in reality the electron is usually in a bound state of an atom and may have a finite momentum. The momentum is not defined precisely at impact but has a probability distribution depending on the quantum state that it occupies. For a given Compton interaction energy detected in a germanium crystal one may consider the uncertainty in the momentum of the atomic electron as giving rise to an uncertainty in the scattering angle. The effect is important for interactions where the deposited energy is below a few hundred keV.

![](./images/812398970264354817_7.jpg)

Fig. 4. Comparison between the two formulae for calculating the total figure-of-merit (Eqs. (10) and (11)) as a function of $\gamma$-ray multiplicity, $M_{\gamma}$. The $\gamma$-ray energy is 1332 keV, $\sigma_{\text{pos}}=$ 1 mm and for local figure-of-merit $w_{3}^{\text{step}}$.

Let us consider incoherent scattering of a $\gamma$-photon of energy, $E_{\gamma}$ and momentum, $\vec{p}_{\gamma}$, on an electron with energy, $E_{\text{e}}$ and momentum, $\vec{p}_{\text{e}}$. For this process, the energy and momentum conservation laws give the following relation:

$$
Q=\frac{E_{\gamma} E_{\gamma}^{\prime}(1-\cos \theta)-m c^{2}\left(E_{\gamma}-E_{\gamma}^{\prime}\right)}{c^{2} \Delta p_{\gamma}} \tag{12}
$$

or

$$
\begin{aligned}
\cos \theta= & 1-m c^{2}\left(\frac{1}{E_{\gamma}^{\prime}}-\frac{1}{E_{\gamma}}\right) \\
& -\frac{1}{E_{\gamma} E_{\gamma}^{\prime}}\left(Q^{2} c^{2}-Q c\{Q^{2} c^{2}\right. \\
& \left.+2 m c^{2}\left(E_{\gamma}-E_{\gamma}^{\prime}\right)+\left(E_{\gamma}-E_{\gamma}^{\prime}\right)^{2}\right\}^{1 / 2}) \quad(13)
\end{aligned}
$$

where $\Delta p_{\gamma}=(1 / c)\left\{\left(E_{\gamma}-E_{\gamma}^{\prime}\right)^{2}+2 E_{\gamma} E_{\gamma}^{\prime}(1-\cos \theta)\right\}^{1 / 2}$ is the absolute value of the momentum transfer

![](./images/812398970264354817_8.jpg)

Fig. 5. Atomic Compton profile for germanium.

vector $\vec{\Delta}p_{\gamma}=\vec{p}_{\mathrm{e}}-\vec{p}_{\mathrm{e}}^{\prime}$ and $Q=-\vec{p}_{\mathrm{e}} \vec{\Delta}p_{\gamma}/|\vec{\Delta}p_{\gamma}|$ is the initial $\mathrm{e}^{-}$-momentum projected on $\vec{\Delta}p_{\gamma}$. One may note that for $Q=0$, Eq. (13) is reduced to the standard Compton scattering formula. The distribution of $Q$ values (the so called *Compton Profile*) has been calculated for all elements up to nobelium in Ref. [17]. For germanium, these calculations were performed with Mann's numerical nonrelativistic Hartree-Fock wavefunctions. The relevant total atomic Compton Profile $J(Q)$ is illustrated in Fig. 5.

As mentioned above, simulations of the Ge detector system were performed using the code GEANT 3.21 [14]. In the original version of the code, the Compton events are described by the quantum mechanical Klein-Nishina differential cross section which corresponds to $\gamma$-scattering on free electrons at rest. To take into account the influence of the $\mathrm{e}^{-}$-momentum on the photon scattering in the simulation program, the Low-Energy Compton Scattering (GLECS) package [18] was used. For the figures-of-merit $w_{2}^{\text{step}}$ and $w_{3}^{\text{step}}$, the uncertainty due to the $\mathrm{e}^{-}$-momentum was included in $\sigma_{\theta^{\text{en}}}$ by calculating the variance in the value $Q$:

$$
\sigma_{Q}^{2}=2 \int_{0}^{\infty} Q^{2} J(Q) \mathrm{d} Q. \tag{14}
$$

For germanium, $\sigma_{Q}^{2}=7.15(m_{\mathrm{e}}c^{2}/\hbar)$. The influence from the atomic electron momentum distribution in Ge on our reconstruction results is illustrated in Figs. 6 and 7 for the best figure-of-merit, $w_{3}^{\text{step}}$.

![](./images/812398970264354817_9.jpg)

Fig. 6. Dependence of reconstruction efficiency, $\varepsilon$ and $P/T$ on position uncertainty, $\sigma_{\text{pos}}$, for figure-of-merit $w_{3}^{\text{step}}$. Results with and without the effect of the atomic momentum distribution in germanium are shown. The $\gamma$-ray multiplicity is fixed at $M_{\gamma}=25$ and the $\gamma$-ray energy is 1332 keV.

Figs. 6 and 7 reveal a considerable, but not devastating, effect on the reconstruction results due to the atomic Compton profile. It is clearly seen that the effect is most significant for small values of $\sigma_{\text{pos}}$. At a position uncertainty $\sigma_{\text{pos}}=1$ mm the efficiency is reduced from 0.33 to 0.24 and the $P/T$ from 0.50 to 0.35. The general feature is a reduction of the slope in the decrease of the tracking performance as a function of increasing position uncertainty. In other words, the tracking performance becomes less sensitive to the detector position resolution. This may be easily understood since the relative contribution to the angular uncertainty from the atomic electron momentum is less when the angular uncertainty due to a poor position determination is already large.

![](./images/812398970264354817_10.jpg)

Fig. 7. Dependence of reconstruction efficiency, $\varepsilon$ and $P/T$ on $\gamma$-ray multiplicity, $M_{\gamma}$, for figure-of-merit $w_{3}^{\text{step}}$. Results with and without the effect of the atomic momentum distribution in germanium are compared. The $\gamma$-ray energy is 1332 keV and the position uncertainty, $\sigma_{\text{pos}}=1$ mm.

## 6. Conclusions

Gamma-ray tracking is a highly promising new technique for $\gamma$-ray spectroscopy. Its success will ultimately depend on a synergy between different technologies: highly segmented, large high-purity Ge detectors, fast digital signal processing electro- nics, pulse shape analysis and tracking algorithms for efficient event reconstruction. In the present work, we have studied refinements of the so called backtracking algorithm for reconstructing the $\gamma$ rays impinging on a Ge detector array modeled as a solid Ge shell. It has been shown that by including the maximum obtainable knowledge about the physical processes behind the detected interactions, significant improvements in tracking efficiency can be achieved. The effects of the atomic electron momentum distribution in Ge on the tracking efficiency have been evaluated. Although significant, they may also be managed satisfactorily by taking the effect into account for each interaction. It is found that gains in performance can be expected by improving the detector position sensitivity beyond $\sigma_{\text{pos}}=1$ mm, despite the electron momentum effect. Therefore, the electron momentum effect does not seem to disqualify current efforts to improve the position sensitivity in segmented Ge detectors, although the sensitivity of the tracking performance to the detector position sensitivity is reduced compared to an "ideal" situation without finite atomic electron momenta.

## Acknowledgements

We would like to thank D. Bazzacco for helpful discussions and R.M. Kippen for providing access to and help with installing the GLECS computer package. This work was supported by the Göran Gustafsson Foundation, the Swedish Research Council and the Commission of the European Communities within the TMR programme, Con- tract No. ERBFMRXCT97-0123.

## References

[1] J. Simpson, Z. Phys. A 358 (1997) 139.
[2] I.Y. Lee, Nucl. Phys. A 520 (1990) 641.
[3] http://www.ganil.fr/exogam/.
[4] J. Eberth, et al., Progr. Part. Nucl. Phys. 38 (1997) 29.
[5] J. Gerl, et al., VEGA-Proposal, GSI Report, 1998.
[6] Th. Kröll, et al., Proceedings of the International Conference Bologna 2000, World Scientific, Singapore, 2001.
[7] M.A. Deleplanque, et al., Nucl. Instr. and Meth. A 430 (1999) 292.
[8] J. Gerl, W. Korten (Eds.), AGATA Technical Proposal, GSI Report, Darmstadt, 2001.
[9] K. Vetter, et al., Nucl. Instr. and Meth. A 452 (2000) 223.
[10] L. Mihailescu, Ph.D. Thesis, Bonn University, Bonn, Germany, 2001.
[11] Th. Kröll, D. Bazzacco, Nucl. Instr. and Meth. A 463 (2001) 227.
[12] G.J. Schmid, et al., Nucl. Instr. and Meth. A 430 (1999) 69.

[13] J. van der Marel, B. Cederwall, Nucl. Instr. and Meth. A 437 (1999) 538.

[14] GEANT3.21, Detector description and simulation tool, CERN, Geneva, Switzerland, 1994.

[15] H.R. Bilger, Phys. Rev. 163 (1967) 238.

[16] G.J. Schmid, et al., Nucl. Instr. and Meth. A 459 (2001) 565.

[17] Biggs, Mendelsohn, Mann, Atom. Data Nucl. Data Tables 16 (3) (1975) 202.

[18] R.M. Kippen, http://gammaray.msfc.nasa.gov/actsim/.