PHYSICAL REVIEW B 96, 125407 (2017)

# Tunable wideband-directive thermal emission from SiC surface using bundled graphene sheets

Sandeep Inampudi and Hossein Mosallaei

Electrical and Computer Engineering Department, Northeastern University, 360 Huntington Ave., Boston, Massachusetts 02115, USA
(Received 29 June 2017; published 7 September 2017)

Coherent thermal radiation emitters based on diffraction gratings inscribed on surface of a polar material, such as silicon carbide, always possess high angular dispersion resulting in wideband-dispersive or monochromatic-directive emission. In this paper, we identify roots of the high angular dispersion as the rapid surface phonon polariton (SPhP) resonance of the material surface and the misalignment of the dispersion curve of the diffraction orders of the grating with respect to light line. We minimize the rapid variation of SPhP resonance by compensating the material dispersion using bundled graphene sheets and mitigate the misalignment by a proper choice of the grating design. Utilizing a modified form of rigorous coupled wave analysis to simultaneously incorporate atomic-scale graphene sheets and bulk diffraction gratings, we accurately compute the emissivity profiles of the composite structure and demonstrate reduction in the angular dispersion of thermal emission from as high as $30^\circ$ to as low as $4^\circ$ in the SPhP dominant wavelength range of 11-12 $\mu$m. In addition, we demonstrate that the graphene sheets via their tunable optical properties allow a fringe benefit of dynamical variation of the angular dispersion to a wide range.

DOI: 10.1103/PhysRevB.96.125407

## I. INTRODUCTION

Thermal radiation is a spontaneous process from a hot material surface. Precise control of its electromagnetic properties is challenging but highly aspired in many research and industrial applications such as solar energy harvesting [1-3], thermophotovoltaics [4-6], mid-infrared incandescent light emitters [7-9], spectroscopy [10], and imaging [11]. Over the past decades, extreme control over spectral selectivity [8,12-20], emissivity [21-24], and directionality [25-31] of thermal radiation have been achieved using microstructures and nanostructures on top of hot surfaces [32]. For example, one-dimensional [18,33,34] and two-dimensional photonic crystals [35], nanoscale gaps [36-38], hyperbolic metamaterials [37], and polar materials with surface phonon polariton (SPhP) resonance [24,26,39,40] have been utilized to manipulate one or more electromagnetic properties of thermal radiation from a hot surface simultaneously [32]. Particularly, polar materials with SPhP resonance, such as the silicon carbide (SiC), are found to be of extreme interest because of their ability to hold orders of magnitude high intensity thermal radiation on their surface with increased coherence length in comparison to an ideal black body at room temperature [26,41-44]. One-dimensional diffraction gratings inscribed on the surface have been utilized to radiate the near-field localized thermal radiation into far-field propagation spectrum leveraging the increased coherence length of SPhPs [26]. The addition of diffraction gratings with specific periodicity and depth has undoubtedly increased the emissivity and directionality of each wavelength in the SPhP regime of SiC. However, the combination of rapid SPhP resonance and the periodicity of the grating has undesirably increased angular dispersion (change of emission angle with frequency) of the thermal radiation [26,27,45]. As a consequence of the high angular dispersion, even though the emission from each wavelength is directional in an angle $\theta$, due to the broadband nature of the source each wavelength emits into a different angle increasing the overall angular range ($\Delta\theta$) of the radiation as shown in Fig. 1(a). Hence, most of the existing SPhP-based thermal emitters either present wideband-dispersive emission or monochromatic-directive emission [26,27]. Here, we identify the root causes of the increased angular dispersion and minimize it by coupling the SiC surface to bundled graphene sheets. By a proper choice of periodicity of the grating, we present wideband-directive thermal emission with an order of magnitude reduction in the angular dispersion in the SPhP wavelength regime of SiC (11-12 $\mu$m).

## II. ANGULAR DISPERSION OF THERMAL RADIATION FROM SIC SURFACE GRATINGS

The angular dispersion is a key property of diffraction gratings in spectroscopy applications that helps to distribute light from different wavelengths to different angles [46,47]. For a diffraction grating with periodicity ($\Lambda$) and a polychromatic source incident at a fixed angle $\theta_i$, the angular dispersion of $m$th diffraction order at an angle ($\theta$) can be computed by differentiating the grating equation $k_0\sin\theta = k_0\sin\theta_i + m\frac{2\pi}{\Lambda}$ as

$$
\frac{d\theta}{dk_0} = \frac{\sin\theta_i - \sin\theta}{k_0\cos\theta}, \tag{1}
$$

where $k_0 = \omega/c = 2\pi/\lambda_0$ is the free-space wave number. Note that the material parameters do not affect the angular dispersion in general.

In case of thermal radiation from SiC in SPhP regime, where the source spectrum is distributed into surface waves at each frequency [represented by the parallel wave-vector component $k_{x;\text{SPhP}} = k_0\sqrt{\epsilon_{\text{SiC}}/(\epsilon_{\text{SiC}} + 1)}$], the grating equation is modified as

$$
k_{x;\theta} = k_0\sin\theta = \text{Re}(k_{x;\text{SPhP}}) + m\frac{2\pi}{\Lambda}. \tag{2}
$$

The angular dispersion of the SiC surface gratings is then given by differentiating Eq. (2) as

$$
\frac{d\theta}{dk_0} = \frac{\frac{d\text{Re}(k_{x;\text{SPhP}})}{dk_0} - \sin\theta}{k_0\cos\theta}. \tag{3}
$$

2469-9950/2017/96(12)/125407(7)
125407-1
©2017 American Physical Society

![](./images/813105314915155969_1.jpg)

FIG. 1. (a) Schematic geometry of SiC slab with grating scattering the heat into different directions. (b) SPhP dispersion curves of planar SiC layers (red color) between wavelengths 11–12 μm and respective thermal emission dispersion curves with a grating (green and blue solid lines) corresponding to a periodicity of $\Lambda = 6.52$ μm. Green and blue dashed lines represent the ideal emission curves given by $k_0 \sin \pm\theta$. Black dashed lines represent the light lines. Note the misalignment in the orientation of emission dispersion curve and ideal emission curves. The wiggled arrows represent counterpropagating SPhPs on the surface.

The increase in angular dispersion of the thermal radiation from SiC surface grating [Eq. (3)] in comparison to a diffraction spectrometer [Eq. (1)] is mainly for two reasons. (i) As seen from Eq. (3), the material dispersion now implicitly contributes to the angular dispersion which is proportional to the term $d\text{Re}(k_{x;\text{SPhP}})/dk_0$. The term $d\text{Re}(k_{x;\text{SPhP}})/dk_0$ diverges with $k_0$ due to rapid dispersion of SPhPs, as shown in Fig. 1(b) and increases the angular dispersion. (ii) In order to emit the radiation from each wavelength to only one angle (or in order to limit the number of propagation diffraction orders of $k_{x;\text{SPhP}}$ to one), the periodicity of the grating is chosen to be of subwavelength order. The choice $(\Lambda < \lambda)$ encourages a good emissivity but simultaneously increases the distance between $k_{x;\text{SPhP}}$ and $k_{x;\theta}$ pushing the $k_{x;\theta}$ to the negative side of the spectrum (green arrow) and $-k_{x;\theta}$ to the positive side (blue arrow), as shown in Fig. 1(b). Note that $\pm k_{x;\theta}$ represent the dispersion curves of diffraction orders of $\pm k_{x;\text{SPhP}}$. Assuming an ideal grating performance and utilizing Eq. (2), the $\pm k_{x;\theta}$ are computed as parallel lines to $\pm k_{x;\text{SPhP}}$ with a shift of $'m2\pi/\Lambda'$. This shift of the emission angle reverses the sign of the slope of the emission dispersion curve with respect to the ideal emission dispersion curves (dotted lines) at respective angles or the light lines, further increasing the angular dispersion. Mathematically, since Eq. (3) is asymmetric with $\pm\theta$, the choice of coupling wave with $+k_{x;\text{SPP}}$ to an angle $-\theta$ has higher angular dispersion in comparison to $+\theta$, where $\theta > 0$.

In the following sections of this paper, we demonstrate methods to minimize the angular dispersion of thermal radiation caused by the above two factors. We utilize bundled graphene sheets to compensate the dispersion of SPhPs on the surface and then properly design the length and the internal structure of the unit cell to eliminate the misalignments between emission dispersion curve and the light line. We demonstrate that addition of graphene sheets not only reduces the angular dispersion, but also provides tunability to dynamically control the dispersion.

### III. SPHP DISPERSION COMPENSATION USING BUNDLED GRAPHENE SHEETS

As discussed above, one of the contributing factors for the angular dispersion of thermal radiation from SiC gratings is the growing ratio of $dk_{x;\text{SPhP}}/dk_0$ on SiC surface with frequency as shown in Fig. 1(b). The rapid growth in ratio is due to the rapid variation of the permittivity of SiC between 11–12 μm wavelength. Addition of any dielectric layers on top would increase the change in $k_{x;\text{SPhP}}$ with respect to $k_0$. To minimize the ratio, we utilize a set of 30 graphene layers on top of SiC surface with 10-nm separation from each other filled with dielectric spacer layers of $\epsilon = 2.25$ in-between, as shown in Fig. 2(a). The net thickness of the bundle is equal to 300 nm and effectively demonstrates anisotropy with hyperbolic dispersion. Fabrication of hundreds of layers of such dielectric and graphene sheet combination is a feasible task using state-of-the techniques such as epitaxial growth [48] and chemical vapor deposition (CVD) transfer [49,50]. For the interested wavelength regime, since the black-body emission peak happens at room temperature, the system is assumed to be in equilibrium at 315 K. While SiC is known to withstand higher temperatures, the stability of graphene at higher temperatures is discussed in [50].

The effective anisotropic permittivity of added graphene bundle is shown in Fig. 3(a). In addition to hyperbolic nature, more importantly, the graphene bundle presents a slow variation of permittivity of both of its components in comparison to SiC. The slow variation can be attributed to the extended tail of Drude model permittivity of the graphene layer into the THz regime whose plasma frequency is tunable from near-IR to mid-IR range [51]. The extended tail of the Drude model into lower frequencies demonstrates relatively slow variation of the permittivity in the SPhP frequency regime of SiC, where the permittivity of SiC is given by rapidly varying Lorentz model.

The total thickness of the graphene bundle being very much smaller than the free-space wavelength, the overall system retains the surface waves but its presence at the surface dramatically alters SPhP dispersion. The $k_{x;\text{SPhP}}$ of the surface waves in the composite system is shown in Fig. 2(b). Evidently, in the interested wavelength regime the curvature of the $(k_{x;\text{SPhP}})$ of the composite surface wave (CSW) is minimized and is observed to be nearly parallel to the light line. Hence, as a consequence, the curvature in its respective diffraction order in the propagation regime also reduces, decreasing the angular dispersion of emission between the respective wavelengths. Note that the anisotropic permittivity of the graphene bundle (as a consequence of the alternating graphene/dielectric layers) does not play a crucial role in reducing the curvature. If available, an isotropic layer with such slow variation of permittivity presents similar performance.

![](./images/813105314915155969_2.jpg)

![](./images/813105314915155969_3.jpg)

![](./images/813105314915155969_4.jpg)

FIG. 2. (a) Schematic geometry of SiC slab with graphene bundle and dielectric gratings of periodicity $\Lambda < \lambda$. (b) Dispersion of composite surface waves (red color) almost parallel to light line. Green and blues lines have the same definitions as in Fig. 1(a). (c) Emissivity spectrum of SiC gratings on top of SiC layer with periodicity of $\Lambda = 6.52\ \mu$m. (d) Emissivity spectrum of the same system with graphene bundle placed in-between the SiC layer and the grating with periodicity of $\Lambda = 6.68\ \mu$m. The periodicity in both cases is chosen such that the radiation at wavelength of $11.5\ \mu$m emits into $45^\circ$. The grating height in both cases is 400 nm with a duty cycle of 65%. The optical parameters of graphene are obtained from Kubo formula with Fermi level $\mu_c = 0.7$ eV and the scattering constant $\tau = 20$ fs.

![](./images/813105314915155969_5.jpg)

FIG. 3. (a) Permittivity of SiC and effective anisotropic permit- tivities of graphene bundle for comparison. Note the slow variation in parameters of graphene bundle in comparison to SiC. (b) The calculated angular dispersion $\Delta\theta$ between 11–12 $\mu$m wavelength. The $x$ axis represents the emission angle of the central wavelength $\lambda_0 = 11.5\ \mu$m. The required periodicity at each emission angle is given by Eq. (2). Note that addition of graphene bundle reduces at least $10^\circ$ of angular dispersion.

Figure 3(b) presents a quantitative description of the reduction in the angular dispersion. The solid blue line in Fig. 3(b) represents the calculated total angular dispersion ($\Delta\theta$) of thermal emission with one-dimensional grating pattern on SiC surface as a function of central emission angle ($\theta$) (shown in Fig. 1). The periodicity ($\Lambda$) of the pattern is chosen using Eq. (2) such that the central wavelength (11.5 $\mu$m) emits at the angle $\theta$ and the $\Delta\theta$ is computed as the difference between the expected emission angle at $\lambda_{\text{min}} = 11\ \mu$m and $\lambda_{\text{max}} = 12\ \mu$m, for SPhP wave propagating along $+x$ direction. The red solid line in Fig. 3(a) represents the angular dispersion ($\Delta\theta$) as a function of emission angle ($\theta$) computed for the composite system. A minimum of $10^\circ$ decrease in the angular separation ($\Delta\theta$) can be observed for all emission angles when the grating is placed on the composite surface in comparison to the SiC surface.

While the above calculations are analytical assuming an ideal grating with one-to-one coupling between SPhP or com- posite wave to the emission direction, to witness the reduction in angular bandwidth more appropriately we compute here the emissivity pattern from the structures as a function of angle and frequency. The emissivity is computed using Kirchhoff’s law [52] as $(1 - P_{\text{ref}})$, where $P_{\text{ref}}$ is the sum of reflection coefficients of all propagating diffraction orders of the system. In order to compute the total reflected intensity accurately including the graphene sheets (not with effective parameters), we developed a slightly modified form of rigorous coupled wave analysis (RCWA) technique [53,54] as described in the Appendix.

The computed emissivity using the modified RCWA for- mulation of transverse magnetic (TM) polarized light from a grating on a bare SiC surface and the composite surface are shown in Figs. 2(c) and 2(d), respectively. The periodicity is chosen such that the SPhP (or CSW) wave at $\lambda_0 = 11.5\ \mu$m propagating along $+x$ ($-x$) direction couples to an emission angle of $-45^\circ$ ($+45^\circ$). As expected, the emissivity of the SiC layer plus grating system [Fig. 2(c)] demonstrates an angular dispersion of $\Delta\theta \approx 30^\circ$, similar to measurements in experiment [26]. The angular bandwidth decreases to $\Delta\theta \approx 16^\circ$ when graphene bundle is inserted in-between the base SiC layer and SiC grating. Note that the computed angular bandwidths of both the systems shown in Figs. 2(c) and 2(d) are higher than the theoretically predicted values in Fig. 3(b) because of the shift in resonance of the SPhPs and CSW due to the presence of grating of finite height (400 nm). Better agreement between predicted and computed angular bandwidths is observed when the grating thickness is reduced to the order of 100 nm, however, at the cost of reduced emissivity due to inefficient diffraction.

In order to verify that the low angular dispersion is a consequence of the CSW but not any higher-order SPhP modes between the SiC base and the grating, we computed the emissivity of the system without the graphene layers but with the dielectric spacer of identical height. The computed emissivity shown in Fig. 4(a) primarily demonstrates a central emissivity curve corresponding to the diffraction order of SPhP resonance. The angular dispersion of the curve is high and similar to the system with grating on SiC substrate shown in Fig. 2(c). In addition, additional horizontal emissivity bands

![](./images/813105314915155969_6.jpg)

FIG. 4. (a) Emissivity spectrum of same system as in Fig. 2(d) without graphene layers but with dielectric spacer layers. Many horizontal emission bands arise due to gap modes inside the grating gaps. (b) Comparison of emissivity of TE and TM polarized waves of the system with graphene layers at three different frequency positions.

arise as a consequence of the gap modes inside the grating gaps that are observed to change their frequency position with respect to filling fraction of the grating. Therefore, the performance of the graphene bundle as a thin metallic layer assists in both minimizing the SPhP dispersion and eliminating the gap-mode resonances.

Certainly, the addition of graphene bundle leads to more absorption loss in the system. As a result, the background emissivity of the system has raised from the order of 0 in Fig. 2(c) to the order of 0.15 in Fig. 2(d). The additional absorption loss also results into nonzero but smaller emissivity values for transverse electric (TE) polarized light as shown in Fig. 4(b). However, due to the absence of surface waves, the emission from TE polarization does not contribute to the angular dispersion.

### IV. ALIGNMENT OF THE DIFFRACTION ANGLE WITH LIGHT LINE

Next, we focus on minimizing the angular dispersion due to misalignment of the emission angle curve and the light line. One of the features to observe from the $\Delta\theta$ curves in Fig. 3(b) is the asymmetric shape which demonstrates that the angular dispersion heavily depends on the sign of the emission angle. Note that since the surface waves symmetrically propagate in both $(+x)$ and $(-x)$ directions, the periodicity $\Lambda$ for a given central wavelength $\lambda_0$ and desired emission angle $\theta$ has two choices. The $\Lambda$ can be chosen such that the surface wave along $+x$ couple to a negative angle (say $-45^\circ$) and vice versa, as described in Figs. 1 and 2, where the periodicity turns out to be $\Lambda < \lambda_0$, or it can be chosen such that the wave along $+x$ couples to $+45^\circ$ and vice versa where the periodicity will be $\Lambda > \lambda_0$. In both cases, the thermal radiation symmetrically emits in to $\pm45^\circ$. However, the former case has high angular dispersion while the latter case has low angular dispersion since the difference between the incident wave vector of the source $(\pm k_{x;\text{SPhP}})$ and the wave vector of the emission curve $\pm k_{x;\theta}$ is minimum in the latter case.

The disadvantage of the latter case $(\Lambda > \lambda_0)$ is the possible leakage of thermal radiation into other diffraction orders that inevitably fall into the propagation regime. However, since by nature of a binary diffraction grating the first diffraction orders $(\pm1)$ have more coupling strengths than the higher orders, a proper choice of periodicity such that

![](./images/813105314915155969_7.jpg)

FIG. 5. (a) Schematic geometry of SiC slab with graphene bundle and dielectric gratings of periodicity $\Lambda > \lambda$. (b) Dispersion of composite surface waves (red color) with the demonstration of six diffraction orders in the propagation regime. The periodicity is assumed to be $\Lambda = 37.51\ \mu\text{m}$. (c) Corresponding computed emissivity spectrum where the grating is assumed to be made of Si $(\epsilon = 12.1)$ to minimize the absorption loss. Only the first diffraction order gets maximum coupling with SPhP. Notice the change in slope of the emission dispersion curve in comparison to Fig. 2. The magnitude of emissivity is less because of high loss factor $(\tau = 20\ \text{fs})$ in the increased graphene bundle volume. The grating height is considered as 235 nm with a duty cycle of 39%.

$$k_0 \sin(\pm\theta) = \pm k_{\text{SPP}} \mp 2\pi/\Lambda$$

will minimize the emission into higher diffraction orders.

Figure 5 presents the dispersion (b) and emissivity (c) of the composite system patterned by such a grating with optimized periodicity. Figure 5(b) shows that the chosen periodicity brings six diffraction orders of both $\pm k_{x;\text{SPhP}}$ into the propagation regime. The analytically computed angular dispersion $\Delta\theta$ of the closest diffraction orders (represented by $m = \pm1$) in this case is around $2.79^\circ$. The computed emissivity pattern using the modified RCWA formulation demonstrates angular dispersion of around $4.2^\circ$ which is nearly an order of magnitude decrease in comparison to the system in Fig. 2(c). Here, to minimize the high absorption losses due to large volumes of grating ridges, the diffraction gratings are considered to be made of a high index dielectric materials such as silicon $(\epsilon = 12.1)$. A major difference that can be observed from Figs. 2(c) and 5(c) is the change in the sign of slope of the emission dispersion curve, which is a necessary and sufficient condition to prove that $+k_{x;\text{SPhP}}$ $(-k_{x;\text{SPhP}})$ radiates at an angle of $+45^\circ$ $(-45^\circ)$ for large period $(\Lambda > \lambda)$ systems.


![](./images/813105314915155969_8.jpg)

FIG. 6. Emissivity profiles of the same system as in Fig. 5(b) with higher scattering time (lower loss factor) of (a) $\tau=200$ fs, and (b) $\tau=500$ fs demonstrating high-emission intensity and contrast.

Even though Fig. 5 demonstrates lower angular dispersion as expected (with the use of dielectric gratings), one can observe a clear decrement both in the magnitude of the emissivity peak and its contrast with the background emission. The decrement is due to the increase of volume of the lossy graphene bundle due to the increase in periodicity. Here, we used $\tau=20$ fs as the scattering constant [55] in the Kubo formula to obtain the optical parameters of graphene which is on the higher end of the abortion loss. Since graphene is a complex material whose optical properties also evidently depend on the other factors (such as substrates, etc.), higher scattering constants such as $\tau=200$ [56] and 500 fs [57] have also been reported in various experiments. To reinforce our argument about the decrement of the quality of emissivity due to high loss, we computed the same quantity with higher scattering times and reported in Fig. 6. Figure 6 clearly shows an increase in both the magnitude and contrast of the emissivity pattern and also demonstrates a lower angular dispersion of $3.77^\circ$, which is closer to the ideal predicted value of $2.79^\circ$.

Finally, we demonstrate the effect of the highly applauded optical property of the graphene sheets which is the dynamical tunability of its Fermi level utilizing external gate bias voltage sources. Although, in this paper we aim on minimizing the angular dispersion of thermal radiation, dynamical control on the dispersion is an added advantage brought by the presence of graphene layers. Figure 7 demonstrates the effect of variation of the Fermi level of the bundled graphene layers. An extreme control on the angular dispersion from a range of $\Delta\theta\approx30^\circ$ to $4^\circ$ is evidently possible by the dynamical tunability of the Fermi level of the graphene sheets.

![](./images/813105314915155969_9.jpg)

FIG. 7. Emissivity profiles of the same system as in Fig. 5(b) by tuning the Fermi level of graphene from (a) 0.2 eV, (b) 0.3 eV, (c) 0.4 eV, and (d) 0.5 eV. The scattering time is considered at the higher loss end as $\tau=20$ fs.

## V. CONCLUSION

In conclusion, we demonstrated extremely reduced angular dispersion (from $30^\circ$ to as low as $4^\circ$) of a wideband coherent thermal radiation emitter in the mid-IR frequency regime made from a polar material. We identified two main contributions for the angular dispersion and provided simple solutions to minimize it using a homogeneous graphene bundle and an optimal one-dimensional diffraction grating. We developed a modified form of rigorous coupled wave analysis formulation to appropriately incorporate atomic-scale graphene sheets between bulk diffraction gratings, and accurately computed the emissivity profiles of the composite systems to demonstrate the minimized angular dispersion. In addition, we demonstrate that by actively controlling the Fermi level of the graphene sheets using gate bias voltage, the angular dispersion of the system can be dynamically varied. While existing surface-phonon-resonance-based thermal emitters are either wideband dispersive or monochromatic directional, the incorporation of graphene bundle paves a way to design wideband-directive thermal emitters.

## ACKNOWLEDGMENTS

This work is supported in part by Air Force Office of Scientific Research (AFOSR) (Grant No. FA9550-14-1-0349) and in part by MURI Army Research Office (ARO) (Grant No. W911NF-14- 0247).

## APPENDIX: RIGOROUS COUPLED WAVE ANALYSIS (RCWA) WITH PATTERNED GRAPHENE SHEETS AS CONDUCTING BOUNDARIES

RCWA is a well-known technique to accurately and efficiently compute light propagation through periodic diffraction gratings at less computational cost. The formulation is based on the scattering matrix method where the electromagnetic fields inside the gratings layers are computed using eigenmode expansion. The incorporation of atomic-scale two-dimensional materials, such as graphene, into this formulation is often carried out by assuming a small thickness and an effective permittivity to the layer [9]. On the other hand, a closely related formulation has been developed to compute light propagation through patterned graphene sheets where graphene is more appropriately assumed as an interface with spatial-dependent surface conductivity and zero thickness separating two homogeneous layers [11,58]. Here, we developed and utilized a combination of the above two techniques to compute electromagnetic wave propagation in a system containing bulk diffraction gratings as layers with nonzero thickness and patterned graphene sheets as conducting interfaces with zero thickness separating the bulk layers. For simplicity, we utilize only one-dimensional gratings and transverse magnetic (TM) polarized light appropriate to the current context, while


![](./images/813105314915155969_10.jpg)

FIG. 8. Schematic geometry of the developed modified RCWA formulation of the composite system with bulk homogeneous layers and diffraction gratings separated by conducting interfaces.

the extension to transverse electric (TE) polarization and two-dimensional gratings is straightforward.

To begin with, solving the Maxwell's equations with plane-wave expansions of electromagnetic fields in Cartesian coordinates, the tangential electric $E_x$ and magnetic $H_y$ field components in a given region of the graphene plus gratings system schematically, shown in Fig. 8, can be expressed as
$$
\begin{aligned}
{\left[\begin{array}{c}
E_{x ; p} \\
H_{y ; p}
\end{array}\right] }=\left[\begin{array}{cc}
\Phi_{x} & 0 \\
0 & \Phi_{x}
\end{array}\right]\left[\begin{array}{cc}
W_{p} & -W_{p} \\
V_{p} & V_{p}
\end{array}\right]\left[\begin{array}{cc}
\Phi_{z ; p}^{+} & 0 \\
0 & \Phi_{z ; p}^{-}
\end{array}\right]\left[\begin{array}{c}
C_{p}^{+} \\
C_{p}^{-}
\end{array}\right], \\
\text { (A1) }
\end{aligned}
$$
where $\Phi_{x}$ is a diagonal matrix whose elements are phase factors along the tangential direction defined as $\Phi_{x}^{(n, n)}=$ $\exp \left(i k_{x}^{(n)} x\right)$ with $k_{x}^{(n)}=k_{x 0}+n 2 \pi / \Lambda$. $k_{x 0}$ represent the incident angle as $k_{x 0}=k_{0} \sin (\theta)$. The quantity $\Phi_{z ; p}^{ \pm}$are also diagonal matrices that represent the phase factor along the propagation direction in the $p$ th region, whose elements are defined as $\Phi_{z ; p}^{+,(n, n)}=\exp \left[+i k_{z ; p}^{(n)}\left(z-z_{p-1}\right)\right]$ and $\Phi_{z ; p}^{-,(n, n)}=$ $\exp \left[-i k_{z ; p}^{(n)}\left(z-z_{p}\right)\right]$. If the $p$ th region is a homogeneous layer, $k_{z ; p}^{(n)}=\sqrt{k_{0}^{2} \epsilon_{p}-\left(k_{x}^{(n)}\right)^{2}}$. If the $p$ th region is an inhomogeneous layer, then $k_{z ; p}^{(n)}$'s are the square root of the eigenvalues of the matrix $A$, defined as [53,54],
$$
A=k_{0}^{2} \mathcal{E}-K_{x} \mathcal{E}^{-1} K_{x} \mathcal{E}, \quad \text { (A2) }
$$
where $K_{x}$ is a diagonal matrix with $K_{x}^{(n, n)}=k_{x}^{(n)}$ and $\mathcal{E}$ is a Toeplitz matrix of Fourier coefficients of spatial permittivity $\epsilon_{p}(x)$ of the inhomogeneous layer, defined as $\mathcal{E}^{(m, n)}=\mathcal{E}_{m-n}$. $\left[\mathcal{E}_{n}=\int_{-\Lambda / 2}^{\Lambda / 2} \epsilon_{p}(x) \exp (i n 2 \pi / \Lambda) d x\right]$.

Similarly, if the $p$ th layer is homogeneous, the quantities $W_{p}$ and $V_{p}$ are diagonal matrices with $W_{p}^{(n, n)}=-k_{z ; p}^{(n)} / k_{0} \epsilon_{p}$ and $V_{p}^{(n, n)}=1$, else $W_{p}$ represent a matrix whose columns are the eigenvectors of the matrix $A$ and $V_{p}$ is a matrix defined as
$$
V_{p}=k_{0} \mathcal{E} W_{p} K_{z ; p}^{-1}. \quad \text { (A3) }
$$

The quantities $C_{p}^{ \pm}$are column vectors representing the amplitude coefficients of the eigenmodes that are determined by the boundary conditions. While above steps are similar to RCWA of diffraction gratings [53,54], the incorporation of the surface conductivity of graphene sheets at the interface is carried into the boundary conditions, at the $p$ th interface as $H_{y ; p+1}\left(x, z_{p}\right)=H_{y ; p}\left(x, z_{p}\right)-\sigma_{p}(x) E_{x ; p+1}\left(x, z_{p}\right)$ and $E_{x ; p+1}\left(x, z_{p}\right)=E_{x ; p}\left(x, z_{p}\right)$. Inserting Eq. (A1) into the boundary conditions and by applying convolution to the product $\sigma_{p}(x) E_{x ; p}\left(x, z_{p}\right)$, the boundary conditions can be translated into matrix form as
$$
\begin{aligned}
& {\left[\begin{array}{cc}
W_{p+1} & -W_{p+1} \\
V_{p+1}^{+} & V_{p+1}^{-}
\end{array}\right]\left[\begin{array}{cc}
I & 0 \\
0 & \Phi_{z ; p+1}^{-}
\end{array}\right]\left[\begin{array}{l}
C_{p+1}^{+} \\
C_{p+1}^{-}
\end{array}\right]} \\
& \quad=\left[\begin{array}{cc}
W_{p} & -W_{p} \\
V_{p} & V_{p}
\end{array}\right]\left[\begin{array}{cc}
\Phi_{z ; p}^{+} & 0 \\
0 & I
\end{array}\right]\left[\begin{array}{l}
C_{p}^{+} \\
C_{p}^{-}
\end{array}\right], \quad \text { (A4) }
\end{aligned}
$$
where $V_{p+1}^{ \pm}=V_{p+1} \pm \Xi W_{p+1}$. $\Xi$ is a Toeplitz matrix of Fourier coefficients of the spatial profile of the surface conductivity $\sigma_{p}(x)$ of the interface, defined as $\Xi^{(m, n)}=\xi_{m-n}$. $\left[\xi_{n}=\int_{-\Lambda / 2}^{\Lambda / 2} \sigma_{p}(x) \exp (i n 2 \pi / \Lambda) d x\right]$.

Further simplifying, Eq. (A4) can be reduced to a scattering matrix equation as
$$
\left[\begin{array}{c}
C_{p}^{-} \\
C_{p+1}^{+}
\end{array}\right]=\left[\begin{array}{cc}
R_{p}^{+} & T_{p}^{-} \\
T_{p}^{+} & R_{p}^{-}
\end{array}\right]\left[\begin{array}{c}
C_{p}^{+} \\
C_{p+1}^{-}
\end{array}\right], \quad \text { (A5) }
$$
where
$$
\begin{aligned}
& R_{p}^{+}=\left(W_{p+1}^{-1} W_{p}+V_{p+1}^{+-1} V_{p}\right)^{-1}\left(W_{p+1}^{-1} W_{p}-V_{p+1}^{+-1} V_{p}\right), \\
& T_{p}^{-}=\left(W_{p+1}^{-1} W_{p}+V_{p+1}^{+-1} V_{p}\right)^{-1}\left(V_{p+1}^{+-1} V_{p+1}^{-}+I\right), \\
& T_{p}^{+}=\left(W_{p}^{-1} W_{p+1}+V_{p}^{-1} V_{p+1}^{+}\right)^{-1}(2 I), \\
& R_{p}^{-}=\left(W_{p}^{-1} W_{p+1}+V_{p}^{-1} V_{p+1}^{+}\right)^{-1}\left(W_{p}^{-1} W_{p+1}-V_{p}^{-1} V_{p+1}^{-}\right).
\end{aligned}
$$

The matrices $R_{p}^{ \pm}$and $T_{p}^{ \pm}$could be individually computed at each interface and iteratively multiplied from the last interface using the formulas
$$
\begin{aligned}
T_{p} & =\left(I-R_{p}^{-} \Phi_{z_{p+1} ; p+1}^{-} R_{p+1}\right)^{-1}\left(T^{+} \Phi_{z ; p}^{+}\right), \\
R_{p} & =R^{+} \Phi_{z ; p}^{+}+T_{p}^{-} \Phi_{z_{p+1} ; p+1}^{-} R_{p+1} T_{p}
\end{aligned}
$$
to obtain the net reflection matrix of the system $R_{1}$. Finally, the matrix of reflectance coefficients of the system $R_{s}$ can be computed as $R_{s}=K_{z: 1}\left|R_{1}\right|^{2} K_{z: 1}^{-1}$. The total reflected intensity $P_{\text {ref }}$ for a given incident angle is given by sum of the elements in corresponding column of the matrix $R_{s}$ and the emissivity is defined as $1-P_{\text {ref }}$. Note that even though the formulation considers $\sigma$ as $\sigma(x)$ for generalization, all the results presented in this paper have homogeneous graphene sheets with no spatial dependence.

[1] K. X. Wang, Z. Yu, V. Liu, Y. Cui, and S. Fan, Nano Lett. 12, 1616 (2012).

[2] V. Raghunathan, A. Kansal, J. Hsu, J. Friedman, and M. Srivastava, in Proceedings of the 4th International Symposium on Information Processing in Sensor Networks (IEEE, Piscataway, NJ, 2005), p. 64.

[3] C. X. Guo, H. B. Yang, Z. M. Sheng, Z. S. Lu, Q. L. Song, and C. M. Li, Angew. Chem., Int. Ed. 49, 3014 (2010).

[4] E. Rephaeli and S. Fan, *Opt. Express* **17**, 15145 (2009).

[5] H. Sai and H. Yugami, *Appl. Phys. Lett.* **85**, 3399 (2004).

[6] S. Molesky, C. J. Dewalt, and Z. Jacob, *Opt. Express* **21**, A96 (2013).

[7] T. Inoue, M. De Zoysa, T. Asano, and S. Noda, *Appl. Phys. Lett.* **102**, 191110 (2013).

[8] H. Miyazaki, T. Kasaya, M. Iwanaga, B. Choi, Y. Sugimoto, and K. Sakoda, *Appl. Phys. Lett.* **105**, 121107 (2014).

[9] H. Wang, Y. Yang, and L. Wang, *J. Opt.* **17**, 045104 (2015).

[10] A. L. Smith, *Applied Infrared Spectroscopy: Fundamentals, Techniques, and Analytical Problem Solving* (Wiley, New York, 1979).

[11] S. Inampudi, J. Cheng, and H. Mosallaei, *Appl. Opt.* **56**, 3132 (2017).

[12] T. Inoue, T. Asano, and S. Noda, *Phys. Rev. B* **95**, 125307 (2017).

[13] J. A. Schuller, T. Taubner, and M. L. Brongersma, *Nat. Photon.* **3**, 658 (2009).

[14] I. Celanovic, D. Perreault, and J. Kassakian, *Phys. Rev. B* **72**, 075127 (2005).

[15] A. Battula and S. C. Chen, *Phys. Rev. B* **74**, 245407 (2006).

[16] I. Puscasu and W. L. Schaich, *Appl. Phys. Lett.* **92**, 233102 (2008).

[17] X. Liu, T. Tyler, T. Starr, A. F. Starr, N. M. Jokerst, and W. J. Padilla, *Phys. Rev. Lett.* **107**, 045901 (2011).

[18] A. W. Rodriguez, O. Ilic, P. Bermel, I. Celanovic, J. D. Joannopoulos, M. Soljačić, and S. G. Johnson, *Phys. Rev. Lett.* **107**, 114302 (2011).

[19] Y. Guo and S. Fan, *Opt. Express* **24**, 29896 (2016).

[20] P. N. Dyachenko, S. Molesky, A. Yu Petrov, M. Störmer, T. Krekeler, S. Lang, M. Ritter, Z. Jacob, and M. Eich, *Nat. Commun.* **7**, 11809 (2016).

[21] S.-Y. Lin, J. G. Fleming, E. Chow, J. Bur, K. K. Choi, and A. Goldberg, *Phys. Rev. B* **62**, R2243(R) (2000).

[22] J.-P. Mulet, K. Joulain, R. Carminati, and J.-J. Greffet, *Microscale Thermophys. Eng.* **6**, 209 (2002).

[23] Z. Yu, N. P. Sergeant, T. Skauli, G. Zhang, H. Wang, and S. Fan, *Nat. Commun.* **4**, 1730 (2013).

[24] Y. Guo and Z. Jacob, *Opt. Express* **21**, 15014 (2013).

[25] N. Dahan, A. Niv, G. Biener, Y. Gorodetski, V. Kleiner, and E. Hasman, *Phys. Rev. B* **76**, 045427 (2007).

[26] J.-J. Greffet, R. Carminati, K. Joulain, J.-P. Mulet, S. Mainguy, and Y. Chen, *Nature (London)* **416**, 61 (2002).

[27] M. Laroche, C. Arnold, F. Marquier, R. Carminati, J.-J. Greffet, S. Collin, N. Bardou, and J.-L. Pelouard, *Opt. Lett.* **30**, 2623 (2005).

[28] S. Han and D. Norris, *Opt. Express* **18**, 4829 (2010).

[29] D. Costantini, A. Lefebvre, A.-L. Coutrot, I. Moldovan-Doyen, J.-P. Hugonin, S. Boutami, F. Marquier, H. Benisty, and J.-J. Greffet, *Phys. Rev. Appl.* **4**, 014023 (2015).

[30] K. Ito and H. Iizuka, *J. Appl. Phys.* **120**, 163105 (2016).

[31] K. Ito, T. Matsui, and H. Iizuka, *Appl. Phys. Lett.* **104**, 051127 (2014).

[32] B. Song, A. Fiorino, E. Meyhofer, and P. Reddy, *AIP Adv.* **5**, 053503 (2015).

[33] A. Narayanaswamy and G. Chen, *Phys. Rev. B* **70**, 125101 (2004).

[34] C. Luo, A. Narayanaswamy, G. Chen, and J. D. Joannopoulos, *Phys. Rev. Lett.* **93**, 213905 (2004).

[35] O. Ilic and M. Soljačić, *Nat. Mater.* **13**, 920 (2014).

[36] S. Shen, A. Mavrokefalos, P. Sambegoro, and G. Chen, *Appl. Phys. Lett.* **100**, 233114 (2012).

[37] J. Shi, B. Liu, P. Li, L. Y. Ng, and S. Shen, *Nano Lett.* **15**, 1217 (2015).

[38] A. Narayanaswamy, S. Shen, L. Hu, X. Chen, and G. Chen, *Appl. Phys. A* **96**, 357 (2009).

[39] D.-Z. A. Chen, A. Narayanaswamy, and G. Chen, *Phys. Rev. B* **72**, 155435 (2005).

[40] R. Messina, W. Jin, and A. W. Rodriguez, *Phys. Rev. B* **94**, 205438 (2016).

[41] K. Joulain, J.-P. Mulet, F. Marquier, R. Carminati, and J.-J. Greffet, *Surf. Sci. Rep.* **57**, 59 (2005).

[42] F. Marquier, K. Joulain, J.-P. Mulet, R. Carminati, J.-J. Greffet, and Y. Chen, *Phys. Rev. B* **69**, 155412 (2004).

[43] R. Carminati and J.-J. Greffet, *Phys. Rev. Lett.* **82**, 1660 (1999).

[44] C. Henkel, K. Joulain, R. Carminati, and J.-J. Greffet, *Opt. Commun.* **186**, 57 (2000).

[45] T. Ribaudo, D. W. Peters, A. R. Ellis, P. S. Davids, and E. A. Shaner, *Opt. Express* **21**, 6837 (2013).

[46] C. Palmer and E. Loewen, *Diffraction Grating Handbook* (Newport Corporation, New York, 2005).

[47] E. G. Loewen and E. Popov, *Diffraction Gratings and Applications* (CRC Press, Boca Raton, FL, 1997).

[48] C. Berger, Z. Song, X. Li, X. Wu, N. Brown, C. Naud, D. Mayou, T. Li, J. Hass, A. N. Marchenkov *et al.*, *Science* **312**, 1191 (2006).

[49] X. Li, W. Cai, J. An, S. Kim, J. Nah, D. Yang, R. Piner, A. Velamakanni, I. Jung, E. Tutuc *et al.*, *Science* **324**, 1312 (2009).

[50] V. W. Brar, M. C. Sherrott, M. S. Jang, S. Kim, L. Kim, M. Choi, L. A. Sweatlock, and H. A. Atwater, *Nat. Commun.* **6**, 7032 (2014).

[51] L. Falkovsky, in *Journal of Physics: Conference Series*, Vol. 129 (IOP Publishing, Bristol, 2008), p. 012004.

[52] J.-J. Greffet and M. Nieto-Vesperinas, *J. Opt. Soc. Am. A* **15**, 2735 (1998).

[53] M. Moharam, T. Gaylord, E. B. Grann, and D. A. Pommet, *J. Opt. Soc. Am. A* **12**, 1068 (1995).

[54] M. Moharam, T. Gaylord, D. A. Pommet, and E. B. Grann, *J. Opt. Soc. Am. A* **12**, 1077 (1995).

[55] M. C. Sherrott, P. W. Hon, K. T. Fountaine, J. C. Garcia, S. M. Ponti, V. W. Brar, L. A. Sweatlock, and H. A. Atwater, *Nano Lett.* **17**, 3027 (2017).

[56] M. Jablan, H. Buljan, and M. Soljačić, *Phys. Rev. B* **80**, 245435 (2009).

[57] A. Woessner, M. B. Lundeberg, Y. Gao, A. Principi, P. Alonso-González, M. Carrega, K. Watanabe, T. Taniguchi, G. Vignale, M. Polini *et al.*, *Nat. Mater.* **14**, 421 (2015).

[58] R.-B. Hwang, *IEEE Trans. Antennas Propag.* **62**, 4736 (2014).
