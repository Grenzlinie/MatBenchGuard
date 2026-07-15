# Long-Wavelength ($\lambda = 10\ \mu\text{m}$) Quadrupolar-Shaped GaAs–AlGaAs Microlasers

S. Gianordoli, L. Hvozdara, G. Strasser, W. Schrenk, J. Faist, and E. Gornik

**Abstract**—In this paper, we present experimental results of our investigations on deformed GaAs-AlGaAs microlasers emitting around $\lambda = 10\ \mu\text{m}$. These quantum cascade lasers exhibit interesting features regarding the threshold current densities, optical output, and far-field pattern. A slight aberration from a circular cross section decreases the threshold current density for microlasers (which have a radius of $50\ \mu\text{m}$). For larger deformations $\epsilon$, the threshold starts to increase because of the increasing mirror losses. For smaller microlasers (radii between 22 and $34\ \mu\text{m}$), the threshold current density increases already for slight deformations due to the increase of the mirror losses. The experimental results can be fitted very well with the mirror losses as a fitting parameter using a well-known and simple model. Threshold currents as low as 170 mA are measured for a cylindrical microlaser with a radius of $22\ \mu\text{m}$. The peak optical output is increasing quasi-exponentially with rising deformation. Lasing emission from slightly concave resonator shapes is detected. The bow-tie mode and other modes—different from Whispering-gallery modes—are responsible for highly directed emission along the diagonal axis and along the short axis, respectively, of the microlasers. Single-mode emission with a side-mode suppression ratio larger than 25 dB is shown over the entire drive current range for a highly deformed microlaser. The laser line can be temperature tuned with $\Delta\nu/T = -0.027\ \text{cm}^{-1}/\text{K}$. A dual mode switching depending on the drive current with a mode spacing of $\Delta\nu = 8.1\ \text{cm}^{-1}$ between 999 and $1007.1\ \text{cm}^{-1}$ is observed for a less deformed microlaser.

Index Terms—Microresonators, mid-infrared, unipolar semiconductor lasers.

## I. INTRODUCTION
R ECENTLY, a novel concept of optical microresonators is making possible the exploration of quantum electrodynamics phenomena in condensed matter [1]. These microcavity lasers excel in their performance as spectrally narrow, low-threshold, and low-noise sources for optoelectronic systems. Micro-disk or -cylinder lasers [2]–[4] are based on the so-called "Whispering-gallery modes" (WGM). The advantage of these modes are the minute losses caused by evanescent leakage [5], [6] and scattering from surface roughness. Besides applications in optical computing and networking, these special lasers are of great interest for studying problems of cavity quantum electrodynamics such as resonator-enhanced spontaneous emission lasers [7], [8].

Although these WGM-based microlasers exhibit a high performance (low-threshold current density and low noise), they suffer from small output power and no directional but omnidirectional emission because of the high-reflectivity mirrors and the circular geometry. Gratings on the disk edge improve the directionality slightly [9]. A more promising concept is the "asymmetric resonant cavity" (ARC) treated theoretically in [10]. Using a ray-optics model, it was found that from a certain deformation of an ARC the isotropic emission of light (typical for WGM) switches to highly anisotropic emission. These ARC's are shown experimentally and explained theoretically in [11]. The so-called "bow-tie" mode (an optical mode which appears at a certain deformation of an ARC and which has the feature of highly directional emission with four main emission lobes in the far-field) was first observed in [11]: the gain region is built up from a quantum-cascade laser active material based on the GaInAs–AlInAs material system grown by molecular beam epitaxy (MBE) matched to an InP substrate.

Quantum-cascade lasers (QCL's) [12] are well suited for investigations of complex resonator shapes like quadrupolar cylinders. The quadrupolar deformation of the cross section (from the investigated microlasers) used in this paper describes a simple two-dimensional (2-D) ARC like those of [10], [11], and [13]. The unipolar character of QCL's excludes nonradiative recombination of electrons and holes which is a problem of common diode lasers processed as microlasers. The transverse magnetic (TM) polarization of the QCL's results in no laser light lost vertically to the laser plane. In addition, the laser emission wavelength around $10\ \mu\text{m}$ (in the mid-infrared spectral region) reduces the roughness scattering [14], [15].

The first GaAs–AlGaAs intersubband QCL's were introduced in 1998 [16] and the first interminiband QCL's [17] in 1999. These steps make it possible to investigate the behavior of this well-known material in the mid-infrared for different resonator shapes. Microcylinder GaAs–AlGaAs QCL's emitting at $10\ \mu\text{m}$ exhibit superior performance compared to conventional ridge waveguide lasers [18] because of their lower threshold current density and comparably high operation temperatures. Single-mode emission can be obtained without a grating as used normally for distributed feedback (DFB) lasers [19]. In this paper, quadrupolar-shaped GaAs–AlGaAs microlasers (shaped in a manner similar to the microlasers in [11]) with the same gain region and the same cladding layers as for the microcylinder lasers in [18] are investigated. Different sized and deformed microlasers are analyzed regarding the threshold current density, optical output, far-field pattern, and

Manuscript received September 9, 1999; revised December 23, 1999. This work was supported in part by a Brite Euram III project (UNISEL: BE97-4072), by the FWF Austria, and by the Society for Microelectronics (GMe, Austria).

S. Gianordoli, L. Hvozdara, G. Strasser, W. Schrenk and E. Gornik are with the Institute of Solid State Electronics, Vienna University of Technology, A-1040 Vienna, Austria.

J. Faist is with the Institute of Physics, University of Neuchâtel, CH-2000 Neuchâtel, Switzerland.

Publisher Item Identifier S 0018-9197(00)02698-1.

0018–9197/00$10.00 © 2000 IEEE

spectral behavior of the laser emission. Threshold currents as small as 170 mA are reported together with highly directional optical output. Also, lasing was achieved for slightly concave resonators, and single-mode or double-mode emission spectra are obtained depending on the deformation of the microlasers. The last is an important feature which can find an interesting application in target spectroscopy or gas sensing since the laser wavelength can be tuned continuously by the operating temperature.

The paper is organized as follows. Section II describes the geometry of the resonators and the technological realization, as well as the experimental setup for measuring the microlasers. In Section III, the threshold current density together with the maximum optical output of the lasers are investigated as a function of the size and deformation of the microlasers. Section IV describes different far-field patterns of the deformed microlasers. Section V is devoted to the spectral behavior of these lasers with single-mode emission or with switching from single-mode to double-mode emission depending on the driving current. Finally, the temperature behavior of the laser wavelength is studied.

## II. QUADRUPOLAR-SHAPED LASERS
The samples presented here are based on a unipolar GaAs-Al₀.₃₀Ga₀.₇₀As heterostructure grown by MBE on GaAs n⁺-substrates. The active material consists of 30 periods of graded injectors and active cells typical for a QCL: electrons are injected into the highest of three subband levels of a triple quantum well. They (radiatively) relax by emitting photons into the second level; the second level is emptied via LO-phonons to the first level so that the second level is free from electrons to maintain a population inversion between levels three and two. The active material is based on the design of the first GaAs-AlGaAs QCL [16] except for a smaller Al content of 30% in order to increase the emission wavelength from 9.4 to 10 μm.

From this material, deformed microlasers are fabricated. Starting from a circular cross section, the boundary is deformed step-wise to a stadium-like cross section. In [10], it was shown that, from partially chaotic WGM in these deformed resonators, directional emission can be obtained because an incident ray on the deformed boundary can be trapped by total internal reflection and escape when the incidence angle falls below the critical angle. Following the shape in that work, as well as [20] and [11], the boundary of the quadrupolar microlasers is given in polar coordinates $(r,\phi)$, with $R$ as the largest radius of the resonator

$$
r(\phi)=\frac{R}{\sqrt{1+2\epsilon}}\sqrt{1+2\epsilon\cos(2\phi)}. \tag{1}
$$

The large radius $R$ is kept constant and the deformation factor is changed from $\epsilon=0$ to $\epsilon=0.24$ in steps of 0.02. In this way, the shorter radius is decreased with increasing deformation while the larger radius is kept constant. Six different sizes of the microlasers are fabricated with $R=10\ \mu\text{m}, 22\ \mu\text{m}, 34.5\ \mu\text{m}, 50\ \mu\text{m}, 60\ \mu\text{m}$, and $70\ \mu\text{m}$. The area $A$ for the different microlasers can be calculated with $A=\pi R^{2}/(1+2\epsilon)$.

![](./images/812459640104157185_1.jpg)

Fig. 1. Side-view and top-view scanning electron microscope picture of a typical microlaser. The etched depth is around $10\ \mu\text{m}$. For the depicted quadrupolar-shaped laser, the larger radius has a value $R=60\ \mu\text{m}$, the smallest value for the radius is $41.7\ \mu\text{m}$, and the deformation is $\epsilon=0.22$. This results in an active area of $7854\ \mu\text{m}^{2}$. For this large deformation, the resonator gets concave. In spite of this fact, a resonant mode exists and the laser is operating. The distance between the shaped top Au contact and the resonator edge is 20 $\mu\text{m}$. The bonding wire is clearly seen on both views. For a deformation of $\epsilon=0.22$, the shape of the microlaser rim starts to get concave as expected from the calculations following (1). This displays the excellent quality of the used technology.

Unlike [11], where the quadrupolar shape was obtained from a resist pattern which was composed of two semicircles connected by a rectangle, we used directly the quadrupolar-shaped pattern given by (1). For $\epsilon$ values larger than 0.20, the shape of the boundary starts to get concave (as one can see in Fig. 1), which agrees well with the theoretical shape. The quadrupolar pattern of the mask is used to form the Ti/Au (nonalloyed) top contact and afterwards to form the 1-$\mu\text{m}$-thick SiN-etching mask. The cylinders are etched using a mixture of $\text{SiCl}_{4}$ and Ar in a reactive ion etching chamber. The side-flanks of the cylinders are perpendicular with a maximum deviation of $1^{\circ}$. In Fig. 1, a side view and a top view for a typical quadrupolar microlaser with a deformation of $\epsilon=0.2$ and a large radius of $R=60\ \mu\text{m}$ are depicted. For the three larger lasers $(R=50, 60$, and $70\ \mu\text{m})$, the top contact is centered—20 $\mu\text{m}$ from the edge—in the middle of the lasers. For the three smaller samples $(R=10, 22, 34.5\ \mu\text{m})$, the top contact is only $3\ \mu\text{m}$ from the resonator edge.

After the SiN mask is removed, the back side of the sample is ground and a Ge/Au/Ni/Au-contact is deposited on it. The

back contact is alloyed (at 430 °C). For the measurement of the optical output and the far-field pattern from the samples with areas of the different sizes and deformations of resonators, single microlasers are cleaved, wire bonded, and mounted onto a He flow-cryostat. The three microlaser sizes with $R = 10, 22$, and $34.5\,\mu$m are not bonded but contacted from the top by a probe manipulator.

## III. THRESHOLD CURRENT AND OPTICAL OUTPUT DEPENDING ON DEFORMATION AND SIZE

For the threshold current density and the optical output measurements, the mid-infrared beam from the laser is collected with a f/0.75 ZnSe lens and a liquid nitrogen ($\text{LN}_2$) cooled mercury cadmium telluride (MCT) detector. The temperature of the sample holder is stabilized at 12 K. In Fig. 2, a typical light output and voltage versus current characteristic of two $R = 22$ $\mu$m microlasers is shown. The smallest threshold current is obtained from the circular ($\epsilon = 0$) resonator. The quadrupolar deformed laser with $\epsilon = 0.1$ is the smallest one that shows lasing emission. Resonators of this size ($R = 22\,\mu$m) but with a deformation larger than $\epsilon = 0.1$ do not lase any more. Also, the smallest fabricated $R = 10\,\mu$m resonators do not show any evidence of stimulated emission. The microlasers are driven at a repetition rate of 94 kHz and a pulsewidth of 100 ns.

For the evaluation of the threshold current density, we assume that the carrier distribution is homogeneous in the active medium because the measured differential resistance multiplied by the geometrical area $A$ is constant [18]. From Fig. 2, one can already see that, with larger deformation, the threshold current density and the differential slope efficiency ($dP/dI$) increase. To compare this observation with the other sizes and deformations of the sample, the threshold current densities depending on the area of the gain region are plotted in Fig. 3. The microcylinder laser with a circular cross section ($\epsilon = 0$) and $R = 70\,\mu$m has the largest (gain) area. All five resonator sizes are depicted in Fig. 3 and labeled by different symbols. With increasing deformation, the short radius $R_0$ decreases whereas the large radius $R$ is kept constant. The active area of the resonators decreasing with increasing deformation. The smallest area for a given value of $R$ is therefore always the one with the largest deformation $\epsilon$ for which the laser is still working. For $R = 60$ and $70\,\mu$m, this is $\epsilon = 0.22$ which has, in part, a concave boundary as described before (see Fig. 1). The smaller the radius of the lasers, the smaller is the highest deformation for which the lasers still work: for $R = 50\,\mu$m, the largest value is $\epsilon = 0.18$; for $R = 35\,\mu$m and $R = 22\,\mu$m, it is $\epsilon = 0.10$. This behavior can be explained using the well-known relation between threshold current density $J_{\text{th}}$, the waveguide- and mirror (scattering) losses $\alpha_W + \alpha_M$, the gain coefficient $g$, and the confinement factor $\Gamma$:

$$
J_{\text{th}} = \frac{\alpha_W + \alpha_M}{g\Gamma}. \tag{2}
$$

The values, obtained by the calculation of the TM mode in the slab waveguide, are $\alpha_W = 16\,\text{cm}^{-1}$ and $\Gamma = 27\%$. The measured gain coefficient for a similar gain material is $g = 16$ $\text{cm}^{-1}/(\text{kA}/\text{cm}^2)$ [21], [22].

![](./images/812459640104157185_2.jpg)

Fig. 2. Light output and voltage versus current characteristics of a circular ($\epsilon = 0$) and a quadrupolar ($\epsilon = 0.10$) cylinder with $R = 22\,\mu$m for the larger radius. The threshold current of the circular and deformed resonators is 170 and 200 mA, respectively. The light output curves are normalized to their maximum. The differential resistance of the deformed laser is larger than that for the circular resonator because the active area of the deformed resonator is $1267\,\mu\text{m}^2$ smaller compared to $1500\,\mu\text{m}^2$ for the circular laser.

![](./images/812459640104157185_3.jpg)

Fig. 3. Threshold current density $J_{\text{th}}$ as a function of the deformation $\epsilon$ and the cavity area. The symbols denote microlasers with different deformations for a constant value of $R$. The largest deformation for each value of $R$ (where lasing is achieved) is pointed out in the figure. The area of the microlasers with the largest deformation is the smallest for each microlaser with the same value of $R$. The threshold current density for nondeformed microlasers starts to increase from resonators with $R = 50\,\mu$m. The values for the circular ($\epsilon = 0$) and the deformed ($\epsilon = 0.1$) lasers are fitted using (2) with the intensity reflection coefficient and the length of the optical cavity mode as fitting parameters.

The factors $\alpha_W$, $g$, and $\Gamma$ are, to a first approximation, the same for all sizes and deformations. In contrast to those, mirror losses $\alpha_M$ depend on the size and therefore also on the deformation, as one can see from the equation for the mirror losses (for Fabry–Perot lasers, see [23]):

$$
\alpha_M = -\frac{\sum_m \ln \mathcal{R}_m}{L}. \tag{3}
$$

The factor $\mathcal{R}_m$ is the intensity reflection coefficient. The path length of the optical cavity mode $L$ (a single turn of the light in the resonator) of a lasing mode can be estimated for a WGM and compared to the value of $L$ for a bow-tie mode. The length $L$ for a WGM in a circle with $R = 70\,\mu$m is around $420\,\mu$m.

To estimate the length for a bow-tie mode and in order to describe the threshold behavior of the microlasers [see Figs. 3 and Fig. 4(a)] with a deformation larger than $\epsilon = 0.10$, we tried to find the bow-tie modes in the different cavities using ray-tracing. Ray optics should be an appropriate method to describe

![](./images/812459640104157185_4.jpg)

Fig. 4. (a) Threshold current density $J_{\text{th}}$ depending on the deformation $\epsilon$ for microlasers with $R = 22$, $50$, $60$, and $70\ \mu\text{m}$. The values are interpolated to get the shown curves. For the $R = 50$ and and $60\ \mu\text{m}$ microlasers, the threshold starts to increase dramatically at a deformation around $\epsilon = 0.10$, whereas for the $R = 22\ \mu\text{m}$ microlaser the increase starts at $\epsilon = 0$. It is interesting to note a decrease of the threshold from $\epsilon = 0$ up to $\epsilon = 0.1$. (b) Semi-logarithmic plot of the maximum peak optical output depending on the deformation $\epsilon$ for microlasers with $R = 50$ and $60\ \mu\text{m}$. The measured values are scaled to their maxima and set to 100 for both resonator sizes. The measured points are fitted and a maximum around $\epsilon = 0.15$ for the $R = 50\ \mu\text{m}$ microlasers and at $\epsilon = 0.2$ for the $R = 60\ \mu\text{m}$ microlaser is noticeable and decreases for larger deformation, probably due to gain saturation.

the modes in our case because we fulfill the condition $kR\gg1$ ($k = 2\pi/\lambda, kR\sim50$) [10].

The lower part of Fig. 5 describes the orientation of the polar coordinate system so that $\Phi = 90^{\circ}$ indicates the direction of the minor axis (small radius) and $\Phi = 0^{\circ}$ denotes the direction along the major axis in the first quadrant. The estimated values of $L$ for a bow-tie mode impinging at angles of $\Phi = 35^{\circ}$, $45^{\circ}$, or $55^{\circ}$ on the rim of a $R = 70\ \mu\text{m}$ and $\epsilon = 0.16$ cavity are $466\ \mu\text{m}$, $416\ \mu\text{m}$, and $361\ \mu\text{m}$, respectively, which are comparable to values of $L$ for the WGM's. (The length $L$ of the bow-tie mode is estimated to be the sum of $4r(\phi))$ and $4r(\phi)\cos(\phi)$.) To compare the threshold current density of an undeformed or slightly deformed resonator with a strongly deformed one of the same size, the decisive magnitude is the sum over $\ln\ \mathcal{R}_{m}$. The factor $\mathcal{R}_{m}$ is a measure of the refractive loss of a ray impinging on the boundary of the resonators. The sum in (3) includes all numbers of refractions of the ray after one circle. For example, for a bow-tie mode, we get a sum over four refractions. Using the simple geometrical ray model of the bow-tie mode, we calculated for microlasers having $\epsilon = 0.16$ and $R = 50, 60$, and $70\ \mu\text{m}$ threshold current densities of $J_{\text{th}} = 9\ \text{kA/cm}^2$ (measured $11\ \text{kA/cm}^2$), $8.4\ \text{kA/cm}^2$ and $7.9\ \text{kA/cm}^2$ (measured $7.7\ \text{kA/cm}^2$), respectively. The ray of the bow-tie modes in these cases always impinges the rim of the cavity at an angle $\chi$ which lies around the critical angle $\chi_{c} = 18.2^{\circ}$ (given by $\sin(\chi) = 1/n_{\text{eff}}$). Therefore, we used a value of $\mathcal{R}_{m}$ of $0.9$ in (3) to calculate the threshold and $\alpha_{W} = 19\ \text{cm}^{-1}$ and $g = 16\ \text{cm}^{-1}/(\text{kA/cm}^2)$.

![](./images/812459640104157185_5.jpg)

Fig. 5. Far-field pattern of a microlaser with $R = 60\ \mu\text{m}$ and deformation $\epsilon = 0.2$. The threshold current density for this deformation is $10\ \text{kA/cm}^2$. This far-field pattern is typical for a bow-tie mode with highly directional emission at a far-field angle $\phi = 45^{\circ}$. The depicted measurement is not perfectly symmetric because already small irregularities on the side walls (mirrors) of the microlasers can influence the emitted intensity pattern. The lower part of the figure shows the polar coordinates used in this paper with the polar angle $\Phi$.

Naturally, the WGM's have no refraction losses but only evanescent and scattering losses whereas the highly deformed lasers exhibit refraction losses when a ray of the lasing mode in the resonator impinges on the boundary below the critical angle. This behavior becomes progressively more dominant as the microlaser and $L$ are made smaller. The largest resonators with $R = 70\ \mu\text{m}$ have the weakest dependence of the threshold on different deformations and the threshold for the most deformed ($\epsilon = 0.22$) large resonators is still small compared to the one of the resonators with smaller sizes. The threshold of the smallest microlasers with $R = 22\ \mu\text{m}$, on the other hand, depend very strongly on the deformation. Following these considerations, the data points in Fig. 3 of the nondeformed microlasers are fitted using (2) with the factors given above, except that $\alpha_{W} = 19\ \text{cm}^{-1}$ (instead of the calculated $\alpha_{W} = 16\ \text{cm}^{-1}$) and $g = 10\ \text{cm}^{-1}/(\text{kA/cm}^2)$. The mirror losses are given by

$$
\alpha_{M} = \frac{-\ln(P1)}{2[(A\pi)^{1/2} - P2(A\pi)^{1/2}]}.
$$

The fitting parameters are $P1 = 0.92$ and $P2 = 0.0014$. The parameter $P1$ (the intensity reflection coefficient) is very close to unity, which can be explained by the nature of the evanescent leakage of the WGM's as radiation loss. The second parameter, $P2$, is a correction term for the length of a WGM which is smaller than the circumference of the microlaser given by: $2(A\pi)^{1/2}$. Also, the datapoints in Fig. 3 of the slightly deformed ($\epsilon = 0.10$) microlasers are fitted using the same factors as for the fit of the nondeformed microlasers. The fitting parameters here are $P1 = 0.85$ and $P2 = 0.2$. The fit parameter $P1$ is, in the case of these deformations, further away from unity, as was the situation for the circular case. This fact represents the nature of ARC's with their typical refractive escape as the radiation loss mechanism [13]. The discrepancy of the two fitting curves with

![](./images/812459640104157185_6.jpg)

Fig. 6. (a) Highly directional emission along the minor resonator axis ($\Phi = 90^\circ$) of a quadrupolar-shaped microlaser with $R = 60\ \mu$m and deformation $\epsilon = 0.12$. The main peak at $\phi = 90^\circ$ has an angular width of $33^\circ$. Two side peaks at $\phi = 29^\circ$ and $\phi = 157^\circ$ can be clearly seen. (b) Semi-logarithmic plot of the single-mode spectrum at the driving current at which the far-field pattern is measured. (c) Light output versus current characteristic of these microlasers. The threshold current density is $7\ \text{kA/cm}^2$.

the measured data of the $R = 22\ \mu$m resonators arises from the fact that, with a decrease of the radius $R$, the influence of the depleted side walls of the microlasers increases.

For the investigation of the maximum optical output, the emission along the short axis $\Phi = 90^\circ$ or at $\Phi = 45^\circ$ (depending on the size and deformation of the microlasers, the emission maximum is at $\Phi = 90^\circ$ or at $\Phi = 45^\circ$, see Figs. 5 and 6) is recorded for the different deformations with the measurement setup as described in Section IV. In Fig. 4, the results of these measurements are shown together with the threshold current density for $R = 22\ \mu$m, $R = 50\ \mu$m, $R = 60\ \mu$m, and $R = 70\ \mu$m microlasers. The optical output for both sizes increases steadily with increasing deformation. On the other hand, the threshold current density slightly decreases up to a deformation of $\epsilon = 0.08$–$0.10$, which is comparable to the results of the InGaAs–InAlAs microlasers [11]. In this regime, the mirror losses have not risen too much compared to the losses of a circle with ideal WGM’s. In contrast to nondeformed cavities in this regime, a small increase of the spontaneous emission coefficient $\beta$ [1], [15] could be the reason for the slight decrease of the threshold [24]. At this point, one should consider that there are still several issues which complicate the interpretation of the threshold data: there is still a reduction in current spreading next to the edges of the cylinders due to a finite lateral current spreading resistance. The threshold current density for a certain mode depends on its spatial distribution in the resonator. Nevertheless beyond a deformation of $\epsilon = 0.10$, the threshold current density and the maximum optical output rise dramatically with increasing deformation, probably due to the larger mirror losses. The angle of incidence of the modes above $\epsilon = 0.10$ is smaller than the critical angle $\chi_c = 18.2^\circ$. The threshold for the $R = 60\ \mu$m microlaser is not ascending as steep as for the smaller ones, in good agreement with the nature of the mirror losses given in (3). Although the threshold for highly deformed microlasers is decreasing with increasing resonator size, it is still higher than the values for slightly deformed microlasers, in contrast to the observation of [11] where the threshold decreased also for highly deformed resonators. For the microlasers with $R = 50\ \mu$m and a deformation of $\epsilon = 0.14$, the maximum optical output is more than 35 times larger than that for the microlaser with $\epsilon = 0.02$. Beyond a deformation of $\epsilon = 0.14$, the maximum optical output of the smaller microlaser in Fig. 4 does not increase any more. In contrast, the optical output of the larger $(60\ \mu$m) microlaser in Fig. 4 increases steadily till a deformation of $\epsilon = 0.2$ is reached and declines only for $\epsilon = 0.22$. For a deformation of $\epsilon = 0.24$, no lasing is achieved.

At this point, it is interesting to look at the maximum working temperature of these chaotic microlasers. In [18], for a circular microcylinder laser, a maximum working temperature of $T = 165$ K was found for this particular gain material. For highly deformed microlasers, it decreases to 130 K. To explain this, the light versus current characteristic in Fig. 2 should be considered: the maximum in the optical output is achieved at around 2.6 times the threshold current for the circular laser and at 1.7 times the threshold current for the deformed laser. Circular lasers, can therefore, exhibit lasing over a larger current range than the deformed lasers, which is important for high working temperatures. The reason for the larger current range for the circular cavities could be the fact that the electrons in the upper lasing level of the intersubband lasers have a lower temperature than do those for the deformed lasers where more electrons (and, therefore, also hotter electrons) have to be injected (higher threshold) in order to achieve lasing.

## IV. FAR-FIELD CHARACTERISTICS

For measuring the far-field pattern, the mid-infrared laser beam is collected with a f/2.9 ZnSe-lens onto an $\text{LN}_2$ cooled MCT. This setup has a collecting angle of $19^\circ$. The samples in the flow cryostat are turned in steps of $\Phi = 11^\circ$ in order to record the emitted intensity for different angles $\Phi$. For the measurement of the far-field pattern, the microlasers are driven in single-mode operation which is guaranteed for some microlasers over all the lasing current range and, for others, the lasing spectrum becomes multimode for higher driving currents. For deformations larger than $\epsilon = 0.10$, the far-field pattern of a bow-tie mode is expected following the measured results of the InGaAs–InAlAs microlasers [11]. In fact, we have found far-field patterns arising from a bow-tie mode, as shown, for example, in Fig. 5. At a far-field angle $\tilde{\phi} = 45^\circ$ and symmetrically at $\tilde{\phi} = 135^\circ$, the far-field pattern has maxima which are the main feature of the bow-tie mode. Also others, different far-field patterns like the one shown in Fig. 6 and some which look like a superposition of a bow-tie mode and the one depicted in Fig. 6 have been found.

As an additional proof for the existence of a bow-tie mode, the mode spacing of the emission spectrum can be measured and compared to the theoretically predicted value. Therefore, we want to discuss briefly the laser spectra concerning the mode spacing of a bow-tie mode. Because of the long wavelength of the microlasers ($\lambda = 10\ \mu$m), the spectra show mostly

![](./images/812459640104157185_7.jpg)

Fig. 7. Laser emission at different temperatures (19 K, 100 K, and 130 K) for a $R = 50\ \mu$m and $\epsilon = 0.18$ laser. The driving current is 1.5 A and the pulsing frequency is 32 kHz with a pulse duration of 200 ns. The laser spectrum at 130 K shows an offset compared to the two other spectra because the laser peak is smaller compared to the the black body background than for lower temperatures where the gain is higher. For these temperatures, a tuning range of $3\ \text{cm}^{-1}$ (32 nm) is obtained. In the inset, a logarithmic plot of a single-mode emission spectrum is shown. A single mode is detected over the total drive current range where the laser is working. A side mode suppression of more than 25 dB is resolved.

single-mode emission over the entire pumping current range, as mentioned before. Some microlasers do, however, exhibit multimode emission under high driving currents. For example, for the $R = 70\ \mu$m and $\epsilon = 0.16$ microlasers, a mode spacing of $\Delta\nu = 8.2\ \text{cm}^{-1}$ can be resolved; the calculated value is $\Delta\nu = 8.16\ \text{cm}^{-1}$ as given by the equation

$$
\Delta\nu = \left\{[4r + 4r\cos(\phi)]n_{\text{eff}}\right\}^{-1} \tag{4}
$$

for an angle $\Phi = 50^\circ$ (this angle should be the point of contact for the bow-tie mode for this deformation, following the geometrical ray -optics approach), $n_{\text{eff}} = 3.15$ [19], and $r$ defined as in (1) for $\Phi = 50^\circ$. This equation is derived from the simple ray-tracing model of a bow-tie mode that we have already used in the discussion of the threshold current densities. The mode spacing $\Delta\nu$ is $1/(Ln_{\text{eff}})$. For the mode spacing of the mode shown in Fig. 6, a mode spacing of $\Delta\nu = 14.6\ \text{cm}^{-1}$ is measured. We did not find any agreement for this mode spacing with the simple ray model we used. Following [11], there can exist stable modes with a higher transverse part of the mode or it could be a WGM because of the relatively low threshold current density of $7\ \text{kA/cm}^2$. To explain the far-field pattern in Fig. 6, a more detailed analysis of the mode would be appropriate.

## V. SPECTRAL BEHAVIOR

Laser emission measurements are performed using a Fourier-transform spectrometer. In this section, two typical microlasers are described for the spectral behavior of these chaotic resonators.

A single-mode microlaser spectrum is shown in the inset of Fig. 7. For all driving currents, this laser exhibits single-mode behavior with a side mode suppression better than 25 dB. No additional side modes are identifiable in the spectrum. The background shift is caused by the blackbody radiation of the cold finger. For a constant injection current of 1.5 A, the temperature shift of the wavelength is investigated. As shown in Fig. 7, the laser spectrum (measured in the rapid scan mode) for the $R = 50\ \mu$m and $\epsilon = 0.18$ microlaser is single mode over a temperature range of 19 K to 130 K (maximum working temperature for this laser). The laser is continuously wavelength tunable (from 9.93 to $10.01\ \mu$m) by changing the operating temperature. This thermal red shift is caused by the temperature dependence of the refractive indices in the material. A tuning coefficient of $-0.027\ \text{cm}^{-1}/\text{K}$ (0.288 nm/K) is obtained.

![](./images/812459640104157185_8.jpg)

Fig. 8. Emission spectrum of a microlaser with $R = 50\ \mu$m and $\epsilon = 0.12$. Depending on the drive current, the laser emission wavelength flips between the two values $1007.1\ \text{cm}^{-1}$ and $999\ \text{cm}^{-1}$. Near the threshold current, the laser emission wavelength is suited to $999\ \text{cm}^{-1}$ and at double the threshold current at $1007.1\ \text{cm}^{-1}$. The resulting mode spacing is $\Delta\nu = 8.1\ \text{cm}^{-1}$.

The second interesting feature in the spectral behavior of these chaotic microcavities is the possibility of switching from one mode to the other by changing the drive current. In Fig. 8, the laser spectra are shown at four different driving currents of the microlaser. Slightly above the threshold current (Fig. 8, part A), the laser spectra show single-mode emission at $1007.1\ \text{cm}^{-1}$. With increasing current, a second mode shows up at $999\ \text{cm}^{-1}$ (Fig. 8, part B), and, finally, the microlaser switches at high driving currents (Fig. 8, parts C and D) to single-mode emission at $999\ \text{cm}^{-1}$. This red-shift can be explained by the increased heating of the sample with increasing pump-current and, therefore, the increase of the refractive index of the material which shifts the laser line toward the red.

In the mid-infrared band, all chemical species have vibrational spectra which make these microlasers interesting as a low-current coherent source for laser spectroscopy. The mode switching for different currents and the temperature tunability of the laser emission are important for an application of this device in target gas sensing or spectroscopy.

## ACKNOWLEDGMENT

The authors would like to acknowledge the help of H. Schenold for building up the measurement setup and of N. Finger for theoretical discussions.

## REFERENCES

[1] Y. Yamamoto and R. E. Slusher, "Optical processes in microcavities," *Phys. Today*, vol. 46, pp. 66-73, June 1997.

[2] S. L. McCall, A. F. J. Levi, R. E. Slusher, S. J. Pearton, and R. A. Logan, "Whispering-gallery mode micro disk lasers," *Appl. Phys. Lett.*, vol. 60, no. 3, p. 289, 1992.

[3] U. Mohideen, W. S. Hobson, S. J. Pearton, F. Ren, and R. E. Slusher, "GaAs/AlGaAs mikrodisk lasers," *Appl. Phys. Lett.*, vol. 64, no. 15, p. 1911, 1994.

[4] A. F. J. Levi, R. E. Slusher, S. L. McCall, S. J. Pearton, and W. S. Hobson, "Room-temperature lasing action in InGaP/InGaAs microcylinder laser diodes," Appl. Phys. Lett., vol. 62, no. 17, pp. 2021-2023, 1993.

[5] N. C. Frateschi and A. F. J. Levi, "The spectrum of microdisk lasers," J. Appl. Phys., vol. 80, no. 2, pp. 644-653, 1996.

[6] L. Djaloshiski and M. Orenstein, "Disk and ring microcavity lasers and their concentric coupling," IEEE J. Quantum Electron., vol. 35, pp. 737-744, May 1999.

[7] R. E. Slusher, A. F. J. Levi, U. Mohideen, S. L. McCall, S. J. Pearton, and R. A. Logan, "Threshold characteristics of semiconductor microdisk lasers," Appl. Phys. Lett., vol. 63, no. 10, pp. 1310-1312, 1993.

[8] J. P. Zhang, D. Y. Chu, S. L. Wu, S. T. Ho, W. G. Bi, C. W. Tu, and R. C. Tiberio, "Photonic-wire laser," Phys. Rev. Lett., vol. 75, no. 14, pp. 2678-2681, 1995.

[9] A. F. J. Levi, R. E. Slusher, S. L. McCall, J. L. Glass, S. J. Pearton, and R. A. Logan, "Directional light coupling from microdisk lasers," Appl. Phys. Lett., vol. 62, no. 6, pp. 561-563, 1993.

[10] J. U. Nöckel and A. D. Stone, "Ray and wave chaos in asymmetric resonant optical cavities," Nature, vol. 385, p. 45, 1997.

[11] C. Gmachl, F. Capasso, E. E. Narimanov, J. U. Nöck4l, A. D. Stone, J. Faist, D. L. Sivco, and A. Y. Cho, "High-power directional emission from microlasers with chaotic resonators," Science, vol. 280, no. 5369, pp. 1556-1564, 1998.

[12] J. Faist, F. Capasso, D. L. Sivco, C. Sirtori, A. L. Hutchinson, and A. Y. Cho, "Quantum cascade laser," Science, vol. 264, pp. 553-556, 1994.

[13] J. U. Nöckel, A. D. Stone, G. Chen, H. L. Grossman, and R. K. Chang, "Directional emission from asymmetric resonant cavities," Opt. Lett., vol. 21, pp. 1609-1611, 1996.

[14] J. Faist, C. Gmachl, M. Striccoli, C. Sirtori, F. Capasso, D. L. Sivco, and A. Y. Cho, "Quantum cascade disk lasers," Appl. Phys. Lett., vol. 69, no. 17, p. 2456, 1996.

[15] C. Gmachl, J. Faist, F. Capasso, C. Sirtori, D. L. Sivco, and A. Y. Cho, "Long wavelength (9.5-11.5 $\mu$m) microdisk quantum-cascade lasers," IEEE J. Quantum Electron., vol. 33, pp. 1567-1572, Sept. 1997.

[16] C. Sirtori, P. Kruck, S. Barbieri, P. Collot, J. Nagle, M. Beck, J. Faist, and U. Oesterle, "GaAs/AlGaAs quantum cascade lasers," Appl. Phys. Lett., vol. 73, no. 24, pp. 3486-3488, 1994.

[17] G. Strasser, S. Gianordoli, L. Hvozdara, W. Schrenk, K. Unterrainer, and E. Gornik, "GaAs/AlGaAs superlattice quantum cascade lasers at $\lambda = 13 \mu$m," Appl. Phys. Lett., vol. 76, no. 10, pp. 1345-1347, 1999.

[18] S. Gianordoli, L. Hvozdara, G. Strasser, W. Schrenk, K. Unterrainer, and E. Gornik, "GaAs/AlGaAs-based microcylinder lasers emitting at $10 \mu$m," Appl. Phys. Lett., vol. 75, no. 8, pp. 1045-1047, 1999.

[19] W. Schrenk, L. Hvozdara, S. Gianordoli, G. Strasser, K. Unterrainer, and E. Gornik, "GaAs/AlGaAs distributed feedback quantum cascade lasers," Appl. Phys. Lett., vol. 76, no. 3, pp. 253-255, 2000.

[20] A. Mekis, J. U. Nöckel, G. Chen, A. D. Stone, and R. K. Chang, "Ray chaos and q spoiling in lasing droplets," Phys. Rev. Lett., vol. 75, no. 14, pp. 2682-2685, 1995.

[21] C. Sirtori, P. Kruck, S. Barbieri, H. Page, J. Nagle, M. Beck, J. Faist, and U. Oesterle, "Low-loss Al-free waveguides for unipolar semiconductor lasers," Appl. Phys. Lett., vol. 75, no. 25, pp. 3911-3913, 1999.

[22] H. Page, C. Sirtori, S. Barbieri, P. Kruck, M. Stellmacher, M. Beck, J. Faist, and J. Nagle, "GaAs quantum cascade lasers," in Proc. LEOS '99, vol. 1, 1999, pp. 7-8.

[23] C. Sirtori, J. Faist, F. Capasso, D. L. Sivco, A. L. Hutchinson, and A. Y. Cho, "Pulsed and continuous-wave operation pf long wavelength infrared ($\lambda = 9.3 \mu$m) quantum cascade lasers," IEEE J. Quantum Electron., vol. 33, pp. 89-92, Jan. 1997.

[24] S. A. Backes, J. R. A. Cleaver, A. P. Heberle, J. J. Baumberg, and K. Köhler, "Threshold reduction in pierced microdisk lasers," Appl. Phys. Lett., vol. 74, no. 2, pp. 176-178, 1999.

S. Gianordoli, photograph and biography not available at the time of publication.

L. Hvozdara, photograph and biography not available at the time of publication.

G. Strasser, photograph and biography not available at the time of publication.

W. Schrenk, photograph and biography not available at the time of publication.

J. Faist, photograph and biography not available at the time of publication.

E. Gornik, photograph and biography not available at the time of publication.