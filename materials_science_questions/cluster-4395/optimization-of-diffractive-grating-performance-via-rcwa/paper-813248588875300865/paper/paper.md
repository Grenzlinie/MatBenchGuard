# Metal-dielectric bi-atomic structure for angular-tolerant spectral filtering

Emilie Sakat,¹² Sébastien Héron,¹ Patrick Bouchon,¹ Grégory Vincent,¹ Fabrice Pardo,² Stéphane Collin,² Jean-Luc Pelouard,² and Riad Haïdar¹,*

¹ONERA—The French Aerospace Lab, Palaiseau F-91760, France
²Laboratoire de Photonique et de Nanostructures (LPN-CNRS), Route de Nozay, Marcoussis F-91460, France
*Corresponding author: riad.haidar@onera.fr

Received October 31, 2012; accepted January 4, 2013;
posted January 9, 2013 (Doc. ID 178944); published February 7, 2013

We theoretically study metal-dielectric structures made of bi-atomic metallic gratings coupled to a guided-mode dielectric resonator. The bi-atomic pattern grating allows tailoring of the Fourier spectrum of the inverse grating permittivity in order to adapt the frequency gap and obtain a flat dispersion band over a wide angular range. A significant enhancement (two-fold) of the angular tolerance as compared to a simply periodic structure is obtained. © 2013 Optical Society of America

OCIS codes: 230.7408, 050.6624, 310.2790, 130.3060, 230.1950.

Guided-mode resonance filters have been intensively studied because of their spectral properties: symmetrical peak shape, high rejection efficiency, and high quality factor [1–5]. These structures are basically composed of stacks of dielectric layers, including one or several gratings introducing periodic modulation of refractive indices. Their basic resonance mechanism relies on the coupling of incoming light with eigenmodes of the dielectric waveguiding layers via the diffraction gratings. Various dielectric grating-based structures have been proposed for bandpass filtering in the last 15 years [6–8]. More recently, a new kind of bandpass guided-mode resonance filter based on a metallic grating deposited on a single free-standing dielectric layer has been studied [9,10]. These filters are particularly well suited for infrared multispectral imaging applications [11,12] in terms of mechanical robustness, rejection efficiency, and quality factor. However, guided-mode resonance structures cannot be employed in applications that require a large field of view because of their poor angular tolerance. It has been shown on simple dielectric grating-based structures that the angular bandwidth is proportional to the spectral bandwidth [13,14]; it is thus impossible to increase the angular tolerance while keeping a narrow spectral bandwidth. To circumvent this problem in the case of all-dielectric guided-mode resonance structures, Lemarchand *et al.* have introduced a *bi-atomic* structure and demonstrated an increase of the angular tolerance without modifying the spectral lineshape [13,15]. However, this concept cannot be directly transposed to the metal-dielectric structures of the papers [9,10]. Indeed, in this latter case, the nonradiative losses dominate and limit the influence of the grating shape. In particular, the spectral bandwidth is limited by the dissipation in the metal. Moreover, the metallic grating is designed to transmit light only when the magnetic field is parallel to the one-dimensional slits (transverse magnetic polarization) [9].

In this Letter, we investigate the bi-atom pattern grating in the case of metal-dielectric structures, which is noticeably different from the study of Lemarchand *et al.* It is used to open a large frequency gap at the center of the Brillouin zone (corresponding to the normal incidence), thus leading to a flat dispersion band over a wide angular range. A detailed numerical study evidences a two-fold enhancement of the angular tolerance as compared to the simply periodic case.

We first consider a structure composed of two identical simply periodic subwavelength metallic gratings (SPGs) deposited on each side of a dielectric free-standing layer [Fig. 1(a)]. The period $d$ is chosen to fulfill two conditions: no diffracted order in free-space and a coupling between the first-order diffracted waves and the eigenmode of the dielectric waveguide layer at resonance wavelength $\lambda_R$. Figure 1(b) shows the transmission spectrum computed with a B-splines modal method [16]. (In our calculations the refractive index of $\text{SiN}_x$ is fixed

![](./images/813248588875300865_1.jpg)

Fig. 1. (Color online) (a) Guided-mode resonance filter with two metallic SPGs deposited on each side of a free-standing dielectric layer. (b) Normal incidence spectra of guided-mode resonance filters with a metallic SPG on both sides (dark) and on one side (dashed green) of the dielectric layer. Geometric parameters are $d = 2.11\ \mu\text{m}$, $t_d = 700\ \text{nm}$, $t_m = 100\ \text{nm}$, $a = 250\ \text{nm}$. (c) Bi-atomic metallic grating-based structure: insertion in the SPG of period $d$ and slits $a$ of perturbed $a + l$ slits spaced at a $d/2$ period. (d) Blue: unperturbed guided-mode dispersion relation; red: perturbed guided-mode dispersion relation; opening of a gap and flattening of the band at normal incidence.

at two; a Drude model is used for the refractive index of gold: $\varepsilon_{m}(\lambda)=1-[(\lambda_{p}/\lambda+i\gamma)\lambda_{p}/\lambda]^{-1}$ with $\lambda_{p}=159$ nm and $\gamma=0.0077)$ It is compared to the transmission spectrum of a similar structure with only one grating on one side of the waveguide layer [9,10]. The rejection efficiency of the two-grating structure [Fig. 1(b)] is greatly enhanced, thanks to a perfect extinction mechanism [17]. The spectral shift between the two transmission peaks is due to the slight modification of the eigenmode $k_{g}$ in the $SiN_{x}$ layer, which alters the phase-matching condition $k_{x}^{( \pm 1)}=k_{g}$. However, both structures have a low angular tolerance, as shown in [9,10] and below.

At normal incidence, two counterpropagating waves are excited by the incident beam (corresponding to the excitation of a waveguide eigenmode by the +1 or -1 diffracted orders). These two modes couple to each other in a symmetrical or in an antisymmetrical way with respect to the $O$-$y$-$z$ plane of symmetry. This leads to two standing-wave solutions of different frequencies, which results in a gap opening and the flattening of the dispersion band at the center of the Brillouin zone. Within a certain limit, the flattening increases with the gap. In the case of all-dielectric guided-mode resonance structures, the dispersion relation has been determined by a perturbative approach (see [15]). To engineer the frequency gap, the grating permittivity is decomposed as
$$
\epsilon(x)=\sum_{q=-\infty}^{q=+\infty} u\left(q K_{x}\right) \exp \left(i q K_{x} x\right),\qquad(1)
$$
with $K_{x}=2 \pi / d$. It has been shown that the imaginary part of the resonant wavevector (which governs the leakage of the mode and thus the spectral bandwidth) is proportional to $|u(K_{x})|^{2}$ and the frequency gap (which governs the angular tolerance) is proportional to $|u(2K_{x})|$ [Fig. 1(d)] [15]. In the case of structures with a metallic grating, these statements should be modified. The spectral bandwidth is less related to $u(K_{x})$ because the nonradiative losses in the metal need to be added to the radiative losses of the structure. Besides, as the structure transmits only the transverse-magnetic polarized waves, the electric field inside the grating is mainly oriented along the $x$ axis, and one should consider the relative Fourier coefficients of $1/\epsilon(x)$ instead of $\epsilon(x)$ [18].

The bi-atom pattern grating consists in a first grating of period $d$ and slit width $a$, and additional slits of width $a+l$. The distance between the two kind of slits is $d/2$ [Fig. 1(c)]. The additional slit pattern allows reinforcing the $u(2K_{x})$ component: if $l=0$, the grating period is $d/2$. The angular tolerance can thus be increased. The parameter $l$ has to be different from zero to keep nonzero $u(K_{x})$ and ensure the coupling.

We achieved numerical simulations on bi-atomic structures. The relative Fourier coefficients of $1/\epsilon(x)$ for these bi-atomic gratings are
$$
u(qK_{x})=\frac{1/\epsilon_{m}-1}{q\pi}\left[\sin\left(\frac{q\pi}{2}\left(1-\frac{2a+l}{d}\right)\right)\cos\left(\frac{q\pi}{2}\left(1+\frac{l}{d}\right)\right)\right].\qquad(2)
$$
When $l\ll d$, $u(2K_{x})\approx((1-1/\epsilon_{m})/(2\pi))\sin((\pi(a+l/2))/(d/2))$; thus at a given period $d$, structures of the same frequency gap $\sigma_{g}$ follow the law $a+l/2=C$, with $C$ a constant. Figure 2 represents the spectral shift between the resonance wavelength $\lambda_{R}$ at $0^{\circ}$ and $10^{\circ}$ [$\Delta\lambda=\lambda_{R}(0^{\circ})-\lambda_{R}(10^{\circ})$] as a function of parameters $a$ and $l$. Figure 2 can be divided into different areas, which are distinguished by the sign of the spectral shift $\Delta\lambda$. The solid blue lines drawn on this figure represent structures with $\Delta\lambda=0$. The green dashed curve connects the points of the higher negative-spectral-shift scattergraph. All these curves follow the previous law: $a+l/2$ constant. It shows that this law still stands when $l/d$ is not negligible. It also confirms that the lines of equal $\Delta\lambda$ correspond to the lines of equal frequency gap [or $u(2K_{x})$]. It is thus possible to optimize the frequency gap with the mean value of the bi-atomic slit width $(a+l/2)$ in order to obtain a better angular tolerance. This is illustrated in the diagrams of Fig. 3: they represent the absolute transmission intensity of two different structures in the plane $(\sigma,k_{x})$ with $\sigma$ being the wavenumber and $k_{x}$ the incident wavevector. Figure 3(a) represents the transmission of a structure with $a=200$ nm and $l=500$ nm (structure A;

![](./images/813248588875300865_2.jpg)

Fig. 2. (Color online) Spectral shift between the resonance wavelength at $0^{\circ}$ and $10^{\circ}$ [$\Delta\lambda=\lambda_{R}(0^{\circ})-\lambda_{R}(10^{\circ})$] of bi-atomic structures as a function of parameters $a$ and $l$; $d=3$ $\mu$m, $t_{d}=700$ nm, $t_{m}=100$ nm. Solid blue lines: structures with $a$ and $l$ such as $\Delta\lambda=0$; dashed green lines: structures that exhibit the higher negative spectral shift.

![](./images/813248588875300865_3.jpg)

Fig. 3. (Color online) Calculated angle-resolved transmission diagrams as a function of the wavenumber $\sigma$ and of the incident wavevector $k_{x}^{(0)}=2\pi\sin(\theta_{x})/\lambda$ for two bi-atomic structures; $d=3$ $\mu$m, $t_{d}=700$ nm, $t_{m}=100$ nm. (a) Structure A: $a=200$ nm and $l=500$ nm. (b) Structure B: $a=300$ nm and $l=600$ nm.

![](./images/813248588875300865_4.jpg)

Fig. 4. (Color online) (a) Transmission at $\lambda_R = 4.02\ \mu$m as a function of the incidence angle for one SPG structure ($d = 2.48\ \mu$m, $a = 350$ nm, $t_m = 100$ nm, $t_d = 700$ nm) and one bi-atomic structure ($d = 3\ \mu$m, $a = 200$ nm, $l = 500$ nm, $t_m = 100$ nm, $t_d = 700$ nm). Transmission spectra at different incidence angle for (b) the SPG structure and for (c) the bi-atomic structure.

see cross in Fig. 2), while Fig. 3(b) represents a structure with $a = 300$ nm and $l = 600$ nm (structure B; see cross in Fig. 2). For structure B, $u(2K_x)$ is higher than in structure A, so the frequency gap is also higher. In structure B, $u(2K_x)$ is so high that the high-frequency mode exceeds $\sigma_g^{(0)}$ [frequency corresponding to the crossing of the bands, Fig. 3(b)]. Thus, at oblique incidence, the transmission band follows the dispersion band, which shifts toward the low wavenumbers ($\Delta\lambda$ is negative). On the contrary, structure A has a value of $u(2K_x)$ which leads to a much flatter transmission band [Fig. 3(a)].

More generally, the structures that are close to the lowest solid blue line in Fig. 2 exhibit the larger angular bandwidth $\Delta\theta$ defined as the half-width at half-maximum of a transmission peak at $\lambda_R$ as a function of the incidence angle. Figure 4(a) represents the angular bandwidth $\Delta\theta$ of two structures that have the same $\lambda_R$ ($\sim4\ \mu$m): one SPG structure with $d = 2.48\ \mu$m, $a = 350$ nm, and one bi-atomic structure [structure A in Fig. 2]. The bi-atomic structure is almost twice as angularly tolerant ($\Delta\theta = 17^\circ$) than the SPG structure ($\Delta\theta = 9.5^\circ$). Figures 4(b) and 4(c) highlight this difference of angular tolerance by comparing their spectra for various incidence angles.

In conclusion, guided-mode-resonance metal-dielectric filters are promising for applications such as infrared multispectral imaging thanks to their good spectral properties (high efficiency and quality factor, and symmetrical shape of the peak). In this Letter, we have shown that the main drawbacks of these filters (rejection efficiency and angular tolerance) can be circumvented by a simple design rule. The rejection is improved by the addition of a second metallic grating under the dielectric layer. Besides, the metallic bi-atomic grating-based structure allows driving the gap aperture and increasing the angular tolerance.

## References
1. S. S. Wang, R. Magnusson, J. S. Bagby, and M. G. Moharam, J. Opt. Soc. Am. A **7**, 1470 (1990).
2. R. Magnusson and S. Wang, Appl. Phys. Lett. **61**, 1022 (1992).
3. A. L. Fehrembach, D. Maystre, and A. Sentenac, J. Opt. Soc. Am. A **19**, 1136 (2002).
4. M. L. Wu, C. L. Hsu, H. C. Lan, H. I. Huang, Y. C. Liu, Z. R. Tu, C. C. Lee, J. S. Lin, C. C. Su, and J. Y. Chang, Opt. Lett. **32**, 1614 (2007).
5. F. Q. Wu, D. Z. Han, X. Li, X. H. Liu, and J. Zi, Opt. Express **16**, 6619 (2008).
6. R. Magnusson and S. S. Wang, Appl. Opt. **34**, 8106 (1995).
7. S. Tibuleac and R. Magnusson, Opt. Lett. **26**, 584 (2001).
8. Y. Ding and R. Magnusson, Opt. Lett. **29**, 1135 (2004).
9. E. Sakat, G. Vincent, P. Ghenuche, N. Bardou, S. Collin, F. Pardo, J.-L. Pelouard, and R. Haïdar, Opt. Lett. **36**, 3054 (2011).
10. E. Sakat, G. Vincent, P. Ghenuche, N. Bardou, C. Dupuis, S. Collin, F. Pardo, R. Haïdar, and J.-L. Pelouard, Opt. Express **20**, 13082 (2012).
11. R. Haïdar, G. Vincent, S. Collin, N. Bardou, N. Guérineau, J. Deschamps, and J. Pelouard, Appl. Phys. Lett. **96**, 221104 (2010).
12. E. Sakat, G. Vincent, P. Ghenuche, N. Bardou, S. Collin, F. Pardo, J.-L. Pelouard, and R. Haïdar, Proc. SPIE **8424**, 842414 (2012).
13. F. Lemarchand, A. Sentenac, and H. Giovannini, Opt. Lett. **23**, 1149 (1998).
14. A. Sentenac and A. L. Fehrembach, J. Opt. Soc. Am. A **22**, 475 (2005).
15. F. Lemarchand, A. Sentenac, E. Cambril, and H. Giovannini, J. Opt. A **1**, 545 (1999).
16. P. Bouchon, F. Pardo, R. Haïdar, and J.-L. Pelouard, J. Opt. Soc. Am. A **27**, 696 (2010).
17. T. Estruch, J. Jaeck, F. Pardo, S. Derelle, J. Primot, J.-L. Pelouard, and R. Haïdar, Opt. Lett. **36**, 3160 (2011).
18. M. Born and E. Wolf, *Principles of Optics: Electromagnetic Theory of Propagation, Interference and Diffraction of Light* (Cambridge University, 1999).