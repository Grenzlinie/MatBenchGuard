THE JOURNAL OF CHEMICAL PHYSICS 127, 044702 (2007)

# Electromagnetic model and calculations of the surface-enhanced Raman-shifted emission from Langmuir-Blodgett films on metal nanostructures

V. Giannini, $^{a)}$ J. A. Sánchez-Gil, $^{b)}$ and J. V. García-Ramos
Instituto de Estructura de la Materia, Consejo Superior de Investigaciones Científicas, Serrano 121, 28006 Madrid, Spain

E. R. Méndez
Departamento de Óptica, División de Física Aplicada, Centro de Investigación Científica y de Educación Superior de Ensenada, Ensenada, Baja California 22800, Mexico

(Received 17 January 2007; accepted 6 June 2007; published online 25 July 2007)

We present a theoretical study of the electromagnetic contribution to surface-enhanced Raman scattering (SERS) from a Langmuir-Blodgett film close to a metal surface. This macroscopic dipolar model fully accounts for the Raman-shifted emission so that meaningful SERS (electromagnetic) enhancement factors that do not depend only on the local electromagnetic field enhancement at the pump frequency are defined. For a plane metal surface, analytical SERS enhancement factors that are consistent for all pump beam polarization and molecular orientation are obtained. In order to investigate SERS on complex nanostructured metal surfaces, we introduce this model into the formally exact, Green’s theorem surface integral equation formulation of the scattered electromagnetic field. This formulation is thus employed to calculate numerically the near-field and far-field emissions at the Raman-shifted frequency for very rough, random nanostructured surfaces, with emphasis on the impact of collective processes for varying pump frequency and Raman shift. Our results reveal that the widely used $|E|^{4}$ approximation tends to overestimate average SERS enhancement factors. © 2007 American Institute of Physics. [DOI: 10.1063/1.2754678]

## I. INTRODUCTION

In general, Raman scattering is extremely weak; typical cross sections are $10^{-30}cm^{2}$ molecule. A dramatic signal enhancement may occur if the analyte molecule is adsorbed to metal particles or to rough metal surfaces with nanometric structure, then known as surface-enhanced Raman scattering (SERS). $^{1-5}$ Discovered nearly three decades ago, SERS has developed into an extremely sensitive spectroscopy technique with, in some cases, single-molecule resolution. $^{6-9}$ The advances in nanofabrication techniques have generated a new interest in using metal nanoparticles and nanoparticle aggregates in chemical and biological sensing applications $^{9-11}$ based on the SERS effect. Electromagnetic (EM) and chemical enhancements have been widely accepted as the mechanisms underlying SERS, $^{1-4}$ usually the EM counterpart contributing most of the enormous enhancement factors $(10^{4}-10^{7})$ . In the classical description of SERS, the electromagnetic enhancement is caused by an enhancement of the local electric fields due to the coupling between light and surface plasmons. Surface plasmons (SPs) are collective oscillations of the electron plasma of the metal, $^{12,13}$ which manifest themselves as particle resonances or surface-plasmon polaritons (SPPs) (evanescent waves propagating along, or localized on, surfaces).

Numerous electromagnetic models have been developed: quasistatic treatment of an isolated sphere, spheroids embedded in a homogeneous medium uniformly covered by dipoles, dipole on a flat surface, sphere on a plane, small particle aggregates, $^{14-18}$ etc. In general, all these formulations can be used for particles or substrates with simple shape and/or dimensions much smaller than the wavelength of light, but are improper for irregular shapes or dimensions comparable to the wavelength of light. In recent years, a variety of numerical calculations have been reported that rely on rigorous EM scattering formulations. $^{19-26}$ These are no longer restricted by the shape/size of the substrates, but typically applied only to two-dimensional configurations. Nonetheless, a large number of theoretical works on the SERS phenomenon approximate the EM-SERS enhancement factors in the following manner:

$$
\mathcal{G}_{\text{SERS}}^{\text{EM}}\approx\left\langle\sigma(\omega_{0})\sigma(\omega_{R})\right\rangle,\tag{1}
$$

where $\sigma=|E|^{2}/|E_{i}|^{2}$ is the enhancement factor of the local electric field intensity on the surface; $\omega_{0}$ and $\omega_{R}$ are the pump beam and Raman-shifted frequencies, respectively. This expression, based on the optical reciprocity theorem, is actually an approximation to the true enhancement factors, as recently highlighted by Ru and Etchegoin. $^{27}$ It ignores all but the dipole part of the emitted radiation field, $^{28,29}$ and is valid only for small particles. Moreover, this approximation neglects the orientation molecule dependence and molecular emission changes due to the metal surface, as, for example, the nonradiative decay. $^{30-32}$

In this work we present a theoretical EM model of the Raman-shifted emission of a molecular layer (a Langmuir-Blodgett film being the paradigmatic example $^{8}$ ), taking into account collective radiation processes at the Raman-shifted

$^{a)}$Electronic mail: vingenzino@iem.cfmac.csic.es
$^{b)}$Electronic mail: j.sanchez@iem.cfmac.csic.es

0021-9606/2007/127(4)/044702/9/$23.00
127, 044702-1
© 2007 American Institute of Physics

![](./images/811973975843274754_1.jpg)

FIG. 1. (Color online) Illustration of the Langmuir-Blodgett/substrate SERS model. The pump field ($\omega_0$), scattered by the substrate (gray region) surface, is driving the Raman-shifted emission ($\omega_R$) from the LB film (red layer), which is in turn scattered by the substrate into the far field (detection).

frequency emission not restricted by the approximation (1). Thus, in general, the model is specially suited for configura- tions in which the local density of molecules adsorbed on the substrate is large enough so that they cannot be considered isolated from the standpoint of classical electrodynamics. The proposed Raman polarization vector and related conti- nuity conditions are presented in Sec. II, including for the sake of consistence the derivation of the analytical results in the simple case of a planar surface. In order to exploit this model on complex nanostructured substrates, we introduce it into the rigorous classical electromagnetic scattering formu- lation known as the Green's theorem surface integral equa- tions as shown in Sec. III. Near-field and far-field results at Raman-shifted frequencies are numerically obtained for Langmuir-Blodgett films on random metal substrates with strong nanoscale irregularities, from which true SERS en- hancement factors are calculated and compared to Eq. (1); these results are presented in Sec. IV. Section V contains the concluding remarks.

## II. THEORETICAL MODEL

### A. Raman polarization of the Langmuir-Blodgett film

Let us consider a metal surface covered with a thin mo- lecular layer, for example, a Langmuir-Blodgett (LB) film. The molecular layer emits at the ($\omega_R$) Raman-shifted fre- quency when excited at the frequency ($\omega_0$) by a pump field (see Fig. 1). Being the Raman cross section weak with re- spect to the field at the pump frequency, the surface field at $\omega_0$ is assumed not to be modified by the presence of LB film; this approximation is known as the *undepleted pump ap- proximation*. We thus propose that the Raman response be described by a dipole layer contribution to the macroscopic polarization vector, proportional to the surface electric field at the pump frequency, $\mathbf{E}(\mathbf{r}|\omega_0)$, in the following manner:

$$
\mathbf{P}^{(R)}(\mathbf{r}|\omega_0,\omega_R)=\overleftrightarrow{\chi}(\mathbf{r}|\omega_0,\omega_R)\delta(\mathbf{r}-\mathbf{R})\mathbf{E}(\mathbf{r}|\omega_0), \tag{2}
$$

where $\overleftrightarrow{\chi}$ is the Raman surface susceptibility tensor. The Dirac delta function in Eq. (2) imposes that the Raman po- larization is nonzero only across the surface, $\mathbf{R}$ being a point on the surface; this is justified by the fact that the thickness of the LB film is relatively small compared to the character- istic variations of the metallic surface and of the surface EM field at $\omega_0$. Actually, it may be applied as well to other con- figurations relevant to SERS, since it is well known that the main EM contribution to SERS enhancement arises from the molecules immediately adsorbed onto the substrate. Implic- itly assumed in Eq. (2) and throughout this work is the fact that phenomenological electrodynamics is valid, neglecting spatial dispersion and interface continuity (cf., e.g., Ref. 1, Sec. IV). With regard to the surface susceptibility, it can be considered as a sum of contributions from all active modes weighted by their strength and spectral response (center fre- quency and linewidth), appropriately including surface mo- lecular density. For the sake of generality, we leave it as frequency dependent tensor. Incidentally, note that the same model polarization could be employed to describe any col- lective dipolar emission close to a surface, such as fluores- cence, photoluminescence, etc., from dyes, polymers, and monolayers deposited on substrates.

### B. Boundary conditions

Now we analyze the change in the continuity conditions induced by the LB film deposited on a surface separating a semi-infinite dielectric medium (vacuum, water, etc.) from a metal. Upon integrating the Maxwell equations across the interface at $\omega_R$ (Raman-shifted frequency), considering the Raman polarization term (2), the continuity conditions for the tangential electric and magnetic fields are $^{33}$

$$
\mathbf{E}_t^{>}(\mathbf{R}|\omega_R)-\mathbf{E}_t^{<}(\mathbf{R}|\omega_R)=-4\pi\frac{\partial}{\partial \mathbf{t}}\lim_{a\rightarrow0}\int_{-a}^{+a}\frac{P_n^{(r)}(\mathbf{R}|\omega_R)}{\varepsilon(\mathbf{r}|\omega_R)}dl, \tag{3}
$$

$$
\begin{aligned}
&\mathbf{H}_t^{>}(\mathbf{R}|\omega_R)-\mathbf{H}_t^{<}(\mathbf{R}|\omega_R)\\
&\quad=4\pi\frac{i\omega_R}{c}\lim_{a\rightarrow0}\int_{-a}^{+a}\left[\mathbf{n}\times\mathbf{P}_t^{(R)}(\mathbf{r}|\omega_R)\right]dl, \tag{4}
\end{aligned}
$$

where we are using a local coordinate system with origin on the surface $\mathbf{R}$, and the integrals are carried out along the local normal direction $l$; the subscripts $t$ and $n$ denote com- ponents that are tangential and normal to the surface, respec- tively. When $a$ tends to zero, only the singular parts of the polarization will give nonzero contributions to the integral. The superscripts $>$ and $<$ mean inside dielectric and metal, respectively, and $\varepsilon(\mathbf{r}|\omega)$ is the position and frequency depen- dent dielectric constant: $\varepsilon^{>}(\mathbf{r}|\omega)=\varepsilon_d$ and $\varepsilon^{<}(\mathbf{r}|\omega)=\varepsilon(\omega)$. At the pump frequency, where no polarization vector is consid- ered (molecular Rayleigh scattering is neglected), Eqs. (3) and (4) reduce to the well known continuity of the tangential EM fields as follows:

![](./images/811973975843274754_2.jpg)

FIG. 2. Schematics of the scattering geometry.

$$
\mathbf{E}_{t}^{>}\left(\mathbf{R} \mid \omega_{0}\right)=\mathbf{E}_{t}^{<}\left(\mathbf{R} \mid \omega_{0}\right), \quad(5)
$$

$$
\mathbf{H}_{t}^{>}\left(\mathbf{R} \mid \omega_{0}\right)=\mathbf{H}_{t}^{<}\left(\mathbf{R} \mid \omega_{0}\right). \quad(6)
$$

### C. Plane surface: Effective Raman Fresnel coefficients

Next, we apply the above model to obtain the SERS enhancement factors in the simple case of a plane surface that separates a dielectric (above) from a metal (below); see Fig. 2, bearing in mind that the interface is flat. At this time, for the sake of clarity we consider that the Raman surface susceptibility tensor $\overleftrightarrow{\chi}$ has a diagonal form, with only two nonzero components along the normal and tangential directions to the metal surface; that are $\chi^{\perp}$ and $\chi^{\|}$, respectively. Since $\mathbf{P}^{(R)}$ has a singularity at the surface, the integrals of Eqs. (3) and (4) are nonzero, so that the continuity equations acquire the following form:

$$
\begin{aligned}
& \mathbf{E}_{t}^{>}\left(\mathbf{R} \mid \omega_{R}\right)-\mathbf{E}_{t}^{<}\left(\mathbf{R} \mid \omega_{R}\right) \\
& \quad=-4 \pi \chi^{\perp}\left(\omega_{R}\right) \mu\left(\omega_{R}, \omega_{0}\right) \frac{\partial}{\partial \mathbf{n}}\left[\varepsilon_{d} E_{z}^{>}\left(\mathbf{R} \mid \omega_{0}\right)\right], \quad(7)
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{H}_{t}^{>}\left(\mathbf{R} \mid \omega_{R}\right)-\mathbf{H}_{t}^{<}\left(\mathbf{R} \mid \omega_{R}\right)=\frac{4 \pi i \omega_{R}}{c} \chi^{\|}\left(\omega_{R}\right)\left[\mathbf{n} \times \mathbf{E}_{t}\left(\mathbf{R} \mid \omega_{0}\right)\right], & \\
& (8)
\end{aligned}
$$

where $\mu\left(\omega_{0}, \omega_{R}\right)=\left[\varepsilon_{d}^{-2}+\left(\varepsilon\left(\omega_{0}\right) \varepsilon\left(\omega_{R}\right)\right)^{-1}\right] / 2$ is a term arising from the integral in Eq. (3). Equations (7) and (8) show that the tangential components of the fields are discontinuous across the interface, in contrast to the more familiar situation found in linear optics, Eqs. (5) and (6).

We assume for the moment that the emission is coherent, i.e., that there is a deterministic relation between the phase of the pump beam and the emitted field at the shifted frequency. A harmonic plane wave $\left(\omega_{0}\right)$ is incident at an angle $\theta_{0}$ on the planar surface (from the dielectric side) with amplitude 1 and polarization $p$ (transversal magnetic) and $s$ (transversal electric). Upon considering the boundary conditions (7) and (8) at $\omega_{R}$, and imposing the transverse momentum conservation,

$$
k_{0, x}=\sqrt{\varepsilon_{d}} \frac{\omega_{0}}{c} \sin \theta_{0}=\sqrt{\varepsilon_{d}} \frac{\omega_{R}}{c} \sin \theta_{R}=k_{R, x} \equiv q, \quad(9)
$$

it is possible to obtain the coefficients of the harmonic plane waves with frequency $\omega_{R}$ at the angle $\theta_{R}$ as a result of the Raman-shifted emission from the LB film on the plane. We call these coefficients effective Raman Fresnel coefficients; for the choice mentioned above of a diagonal susceptibility, there are two coefficients $\mathrm{R}_{p}^{\|}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)$ and $\mathrm{R}_{p}^{\perp}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)$ for $p$ polarization, and only one $\mathrm{R}_{s}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)$ for $s$ polarization, respectively, which can be written as

$$
\begin{aligned}
& \mathrm{R}_{p}\left(\theta_{0}, \omega_{0}, \omega_{R}\right) \\
& \quad \equiv \mathrm{R}_{p}^{\|}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)+\mathrm{R}_{p}^{\perp}\left(\theta_{0}, \omega_{0}, \omega_{R}\right) \\
&=-4 \pi i \frac{\omega_{R}}{\omega_{0}}\left\{\frac{\alpha_{0}^{(0)}(q) \varepsilon_{d} \alpha_{R}(q)\left[1-R_{p}\left(\theta_{0}, \omega_{0}\right)\right]}{\varepsilon\left(\omega_{R}\right) \alpha_{R}^{(0)}(q)+\varepsilon_{d} \alpha_{R}(q)} \chi^{\|}\right. \\
&\left.\quad-\frac{\varepsilon\left(\omega_{R}\right) \mu\left(\omega_{0}, \omega_{R}\right) q^{2}\left[1+R_{p}\left(\theta_{0}, \omega_{0}\right)\right]}{\varepsilon\left(\omega_{R}\right) \alpha_{R}^{(0)}(q)+\varepsilon_{d} \alpha_{R}(q)} \chi^{\perp}\right\}, \quad(10)
\end{aligned}
$$

$$
\mathrm{R}_{s}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)=4 \pi i \frac{\omega_{0} \omega_{R}}{c^{2}} \frac{\left(1+R_{s}\left(\theta_{0}, \omega_{0}\right)\right)}{\alpha_{R}^{(0)}(q)+\alpha_{R}(q)} \chi^{\|}, \quad(11)
$$

where the perpendicular wave vector components are

$$
\alpha_{0}^{(0)}(q)=\left[\varepsilon_{d} \frac{\omega_{0}^{2}}{c^{2}}-q^{2}\right]^{1 / 2}, \quad \alpha_{R}^{(0)}(q)=\left[\varepsilon_{d} \frac{\omega_{R}^{2}}{c^{2}}-q^{2}\right]^{1 / 2},
$$

$$
\alpha_{0}(q)=\left[\varepsilon\left(\omega_{0}\right) \frac{\omega_{0}^{2}}{c^{2}}-q^{2}\right]^{1 / 2},
$$

$$
\alpha_{R}(q)=\left[\varepsilon\left(\omega_{R}\right) \frac{\omega_{R}^{2}}{c^{2}}-q^{2}\right]^{1 / 2},
$$

and the well known Fresnel coefficients at the pump frequency are

$$
\begin{aligned}
& R_{p}\left(\theta_{0}, \omega_{0}\right)=\frac{\varepsilon\left(\omega_{0}\right) \alpha_{0}^{(0)}(q)-\varepsilon_{d} \alpha_{0}(q)}{\varepsilon\left(\omega_{0}\right) \alpha_{0}^{(0)}(q)+\varepsilon_{d} \alpha_{0}(q)}, \\
& R_{s}\left(\theta_{0}, \omega_{0}\right)=\frac{\alpha_{0}^{(0)}(q)-\alpha_{0}(q)}{\alpha_{0}^{(0)}(q)+\alpha_{0}(q)},
\end{aligned}
$$

(12)

for $p$ and $s$ polarizations, respectively.

Note that the effective Fresnel coefficients in Eqs. (10) and (11) cannot be written in terms of products of $(1 \pm R)$ at $\omega_{0}$ and $\omega_{R}$. We recover a more intuitive expression after properly renormalizing by the resulting coefficients for a freestanding LB layer, ${ }^{34} \mathrm{R}_{p}^{o, \|}, \mathrm{R}_{p}^{o, \perp}$, and $\mathrm{R}_{s}^{o}$,

$$
\begin{aligned}
\mathcal{R}_{p}^{\|}\left(\theta_{0}, \omega_{0}, \omega_{R}\right) & =\frac{\mathrm{R}_{p}^{\|}}{\mathrm{R}_{p}^{o, \|}} \\
& =\frac{\alpha_{0}^{(0)}(q) \varepsilon_{d} \alpha_{R}(q)\left[1-R_{p}\left(\theta_{0}, \omega_{0}\right)\right]}{\varepsilon\left(\omega_{R}\right) \alpha_{R}^{(0)}(q)+\varepsilon_{d} \alpha_{R}(q)} \frac{2}{\alpha_{0}^{(0)}(q)} \\
& =\left[1-R_{p}\left(\omega_{R}, \theta_{R}\right)\right]\left[1-R_{p}\left(\omega_{0}, \theta_{0}\right)\right], \quad(13)
\end{aligned}
$$

$$
\begin{aligned}
\mathcal{R}_{p}^{\perp}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)= & \frac{\mathrm{R}_{p}^{\perp}}{\mathrm{R}_{p}^{o, \perp}}=\frac{\varepsilon\left(\omega_{R}\right) \mu\left(\omega_{0}, \omega_{R}\right) q^{2}\left[1+R_{p}\left(\theta_{0}, \omega_{0}\right)\right]}{\varepsilon\left(\omega_{R}\right) \alpha_{R}^{(0)}(q)+\varepsilon_{d} \alpha_{R}(q)} \\
& \times \frac{2 \alpha_{R}^{(0)}(q)}{q^{2} \mu\left(\omega_{0}, \omega_{R}\right)} \\
= & {\left[1+R_{p}\left(\omega_{R}, \theta_{R}\right)\right]\left[1+R_{p}\left(\omega_{0}, \theta_{0}\right)\right], }
\end{aligned}
$$

$$
\begin{aligned}
\mathcal{R}_{s}\left(\theta_{0}, \omega_{0}, \omega_{R}\right)=\frac{\mathrm{R}_{s}}{\mathrm{R}_{s}^{o}} & =\frac{1+R_{s}\left(\omega_{0}\right)}{\alpha_{0}^{(0)}(q)+\alpha_{R}(q)} 2 \alpha_{0}^{(0)}(q) \\
& =\left[1+R_{s}\left(\omega_{R}, \theta_{R}\right)\right]\left[1+R_{s}\left(\omega_{0}, \theta_{0}\right)\right], \quad(15)
\end{aligned}
$$

where $\theta_{R}=\sin ^{-1}\left[\left(\omega_{0} / \omega_{R}\right) \sin \left(\theta_{0}\right)\right]$. When the argument of the latter expression is bigger than 1, the plane wave emitted at the frequency $\omega_{R}$ becomes indeed evanescent. In other words, this means that there is a horizon in the Raman far field at $\theta_{0}=\theta_{c}=\sin ^{-1}\left(\omega_{R} / \omega_{0}\right)$, so that for $\left|\theta_{0}\right|>\theta_{c}$ the Raman perpendicular wave vector is imaginary, i.e., we cannot detect the Raman-shifted emission in the far field. Moreover, for $\theta_{0}>\theta_{c}\left(\omega_{R}>\omega_{0}\right)$ the effective Fresnel coefficients may present a divergence that corresponds to the SPP dispersion relation (poles of $\mathrm{R}_{p}$ ) at $\omega_{R}$, retrieved for matching transverse wave vector components,

$$
k_{0}=\sqrt{\varepsilon_{d}} \frac{\omega_{0}}{c} \sin \left(\theta_{0}\right)=\frac{\omega_{R}}{c} \sqrt{\frac{\varepsilon_{d} \varepsilon\left(\omega_{R}\right)}{\varepsilon_{d}+\varepsilon\left(\omega_{R}\right)}} \equiv k_{\mathrm{SPP}}\left(\omega_{R}\right). \quad(16)
$$

Essentially, the fact that the frequency of the emitted photon is lower in the Stokes region, along with parallel momentum conservation, makes it possible in principle to excite a Raman-shifted, emitted SPP. This represents a quenching effect for the LB layer on a metal plane in the Stokes region (or a Brewster effect in the dielectric case).

We can see that for $s$ polarization [Eq. (15)], the same result would be obtained by using the approximation (1); in contrast, the thus obtained expression for $p$ polarization would differ from our Eqs. (13) and (14). On the other hand, if we consider a perfect conductor instead of a metal, it can be shown that, for normal incidence,

$$
\left(\mathrm{R}_{p}^{\|}+\mathrm{R}_{p}^{\perp}\right) /\left(\mathrm{R}_{p}^{o, \|}+\mathrm{R}_{p}^{o, \perp}\right)=\mathrm{R}_{p}^{\|} / \mathrm{R}_{p}^{o, \|}=0 .
$$

This is in agreement with the analytic calculation for one dipole $^{2}$ or a dipole layer parallel to the plane, as expected. Likewise, if we now conside grazing incidence $\left(\theta_{0}=90^{\circ}\right)$ in $p$ polarization, we obtain $\left(\mathrm{R}_{p}^{\|}+\mathrm{R}_{p}^{\perp}\right) /\left(\mathrm{R}_{p}^{o, \|}+\mathrm{R}_{p}^{o, \perp}\right)=\mathrm{R}_{p}^{\perp} / \mathrm{R}_{p}^{o, \perp}$ $=4$, which agrees with the result obtained from the analytic calculation for one dipole $^{1,2}$ or a dipole layer normal to the plane (see also Refs. 30 and 31, taking into account that the enhancement of the pump beam is not included therein).

In Fig. 3, we show the angular dependence of the Raman Fresnel coefficients (10) and (11) for a LB film on a vacuum/Ag interface for an incident plane wave at $\lambda_{0}$ $=514.5 \mathrm{~nm}$ and for $\lambda_{0}=826.6 \mathrm{~nm}$. The evanescent region in the blueshift part of the figures is located in the upper right corner delimited by a white (horizon) curve. Recall that the bright band in this region for the $p$ polarization coefficients determines the coupling into the Raman-shifted SPP; as explained above, this coupling does not contribute to the enhancement of the Raman-shifted far field, but rather leads to a nonradiative quenching of the Raman-shifted emission. In Fig. 4, we show the angular dependence of the Raman Fresnel coefficients (13)-(15) in the propagating region for three cases: zero Raman shift, and blue and red Raman shifts. In this region, as expected, the $\mathcal{R}_{s}$ coefficient is overall smaller, and coincides with $\mathcal{R}_{p}^{\|}$for $\theta_{0}=0^{\circ}$. The $\mathcal{R}_{p}^{\perp}$ coefficient is the larger coefficient in the propagating region; for instance, for small angles of incidence, $\left|\mathcal{R}_{p}^{\perp}\right|^{2} \sim 12$ whereas $\left|\mathcal{R}_{p}^{\|}\right|^{2} \sim\left|\mathcal{R}_{s}\right|^{2} \sim 0.1\left(\lambda_{0}=514.5 \mathrm{~nm}\right)$ and $\left|\mathcal{R}_{p}^{\perp}\right|^{2} \sim 15$ whereas $\left|\mathcal{R}_{p}^{\|}\right|^{2} \sim\left|\mathcal{R}_{s}\right|^{2} \sim 0.1\left(\lambda_{0}=826.6 \mathrm{~nm}\right)$.

![](./images/811973975843274754_3.jpg)

FIG. 3. (Color online) Square amplitude of the Raman Fresnel coefficients $\mathrm{R}$, from a Ag surface as a function of both the incident angle and the Raman emission wavelength, for a pump plane wave at $\lambda_{0}=514.5 \mathrm{~nm}$ [(a)-(c)] and at $\lambda_{0}=826.6 \mathrm{~nm}$ [(d)-(f)]. [(a) and (d)] $\log _{10}\left|\mathrm{R}_{p}^{\|}\right|^{2}$, [(b) and (e)] $\log _{10}\left|\mathrm{R}_{p}^{\perp}\right|^{2}$, and [(c) and (f)] $\log _{10}\left|\mathrm{R}_{s}\right|^{2}$.

SERS enhancement factors on planar surfaces as obtained from the above effective Raman Fresnel coefficients are fairly small and irrelevant from the quantitative standpoint, but provide a valuable analytical test for the presented model, in agreement with the appropriate limits with simple

![](./images/811973975843274754_4.jpg)

FIG. 4. (Color online) Square amplitude of the normalized Raman Fresnel coefficients $\mathcal{R}$, from a Ag surface as a function of the incident angle for various Raman shifts. Solid curves: $\left|\mathcal{R}_{p}^{\|}\right|^{2}$; dashed curves: $\left|\mathcal{R}_{p}^{\perp}\right|^{2}$; and dashdotted curves $\left|\mathcal{R}_{s}\right|^{2}$. (a) Incident pump field of wavelength $\lambda_{0}=514.5 \mathrm{~nm}$, $\lambda_{R}=\lambda_{0}$ (black), $\lambda_{R}=614.5 \mathrm{~nm}$ (red), and $\lambda_{R}=414.5 \mathrm{~nm}$ (blue). (b) Incident pump field of wavelength $\lambda_{0}=826.6 \mathrm{~nm}, \lambda_{R}=\lambda_{0}$ (black), $\lambda_{R}=926.6 \mathrm{~nm}$ (red), and $\lambda_{R}=726.6 \mathrm{~nm}$ (blue).

existing models and indeed yielding further physical insight into it. Incidentally, it can be shown that incoherence can be accounted for by modifying only the angular pattern of the far-field Raman-shifted emission, the average SERS enhancement factors being similar.

In order to experimentally test the above model and predictions, a LB film of high density molecules (preferably oriented parallel to each other) deposited on a flat metal surface could be employed. Keep in mind that, since no relevant SERS enhancement occurs in this configuration, the molecule should yield a detectable Raman spectrum, at least for one band. The quenching effect could be observed by measuring the Raman signal of a given vibrational mode (with a reasonably large Raman shift) in the Stokes region as a function of the angle of incidence of the pump beam; the angle of detection is in principle irrelevant due to the inherent incoherence of Raman emission. Actually, incoherence may also blur the abrupt dependence on the angle of incidence. Alternatively, the ratio between anti-Stokes and Stokes intensities could be explored in search of large values (minima of the Stokes band) that indeed deviate from the well known ratio connected to the sample temperature.

### III. SCATTERING FORMULATION
#### A. Scattering equations

We now proceed to introduce the model into rigorous scattering theories in order to explore SERS for LB films on very rough, nanostructured metal substrates. A great variety of theoretical formulations based on Maxwell's equations exist to describe the EM response of metallic nanostructures, with a different level of approximation, validity, and specificity. We make use here of the formally exact formulation for the scattering of EM waves in the form of surface integral equations by means of the Green's theorem. $^{35-37}$ This formulation has been used to investigate the EM field scattered from one-dimensional, randomly rough metal surfaces with arbitrarily large roughness. $^{22,38}$ Furthermore, by invoking the approximation (1), numerical results for the near-field enhancements at the pump frequency have been used to infer SERS enhancement factors. $^{21,39}$

We show elsewhere how to incorporate into the Green's theorem surface integral equations the above model for the Raman-shifted emission of a LB film on an arbitrarily rough substrate. $^{40}$ The formulation is restricted for the sake of simplicity to one-dimensional surfaces, i.e., surfaces that are invariant along the $y$ direction. The semi-infinite metal occupies the lower half-space $z<\zeta(x)$ (see Fig. 2), and the upper semispace is vacuum. This formulation can be extended to the case of isolated metallic particles (multiple scattering domains) or aggregates of particles or to real rough surfaces (i.e., with variations in two dimensions). The one-dimensional surface assumption simplifies considerably the formulation, and the computational effort in the numerical calculations, without posing restriction to the roughness-induced coupling into SPP responsible for the large surface EM fields necessary to drive and enhance the Raman-shifted emission. We consider the case of a $p$-polarized pump beam, since in this configuration only $p$ polarization permits to excite SPPs.

#### B. Surface field enhancement and SERS

With the formalism developed in this paper, we can calculate the EM field scattered at the Raman-shifted frequency, separately from the EM field scattered at the pump frequency, bearing in mind of course that the latter is driving the Raman-shifted emission through an effective incident field. We define the SERS factor in the following manner:
$$
\mathcal{G}_{\mathrm{SERS}}^{\mathrm{EM}}\left(\omega_{R}, \omega_{0}\right)=\frac{\rho_{\mathrm{metal}}\left(\omega_{R}, \omega_{0}\right)}{\rho_{\text {layer }}\left(\omega_{R}, \omega_{0}\right)},
\tag{18}
$$
where $\rho_{\text {metal }}$ is the far-field enhancement of the Ramanshifted signal from a rough metal surface with respect to that from a planar metal surface: $\rho_{\text {metal }}=|\mathrm{R}_{p, s}|^{2}\langle I_{\text {rough }}\rangle/\langle I_{\text {plane }}\rangle$; with $\langle\cdots\rangle$ denoting the average over an ensemble of realizations of $\zeta(x)$. $\rho_{\text {layer }}=|\mathrm{R}_{p, s}^{o}|^{2}$ is a coefficient that accounts for the emission of a freestanding dipole layer (without metal). When we have a flat surface, $\mathcal{G}_{\mathrm{SERS}}^{\mathrm{EM}}(\omega_{R},\omega_{0})$ is the square modulus of the effective Raman Fresnel coefficients, Eqs. (13)-(15). We can obtain the SERS factor for any Raman shift.

For the sake of comparison, it is interesting to calculate also the intensification factors of the surface electric field at the pump frequency, $\sigma_{E}(\Omega)=|\mathbf{E}(x|\Omega)|^{2}/|\mathbf{E}^{(i)}(x|\Omega)|^{2}$, assuming two different pump beams at $\Omega=\omega_{0},\omega_{R}$, in order to obtain the EM contribution to SERS given by the widely used approximation (1); when $\Delta\omega=|\omega_{o}-\omega_{R}|$ is small, as is often the case (since the SP width is typically large compared to the Stokes shift), this approximation is further simplified as $\mathcal{G}_{\mathrm{SERS}}^{\mathrm{EM}}\approx\langle\sigma(\omega_{0})^{2}\rangle$. Such near electric fields are calculated as shown in Ref. 22.

#### C. Random rough surface model

The surface profile function $z=\zeta(x)$ assumed in this paper is a Gaussian random process described by the following statistical properties:

(i) Null mean deviation from $z=0$:
$$
\langle\zeta(z)\rangle=0;
\tag{19}
$$

(ii) Normal statistics with rms deviation $\delta$:
$$
\delta=\sqrt{\langle\zeta(x)^{2}\rangle};
\tag{20}
$$

(iii) Gaussian correlation function $c(\tau)$ whose width defines a correlation length $a$ as
$$
c(\tau)=\frac{1}{\sigma^{2}}\langle\zeta(x)\zeta(x+\tau)\rangle=e^{-\tau^{2}/a^{2}}.
\tag{21}
$$

Gaussian-correlated randomly rough substrates have been shown to yield large SERS enhancement factors [through Eq. (1)], comparable to those found for self-affine fractal substrates, $^{38}$ when strong nanoscale irregularities (small $a$ and large $\delta$) are present. $^{41}$

The surface realizations of length $\mathcal{L}=7\ \mu$m consist of $N_{p}$ sampling points: $\zeta_{n}=\zeta(x_{n})$ where $n=1,\ldots,N_{p}$. The resulting

![](./images/811973975843274754_5.jpg)

FIG. 5. (Color online) Near electric field intensity maps in a $\log_{10}$ scale, from a rough Ag surface with $\delta$=255 nm and $a$=51.5 nm, for normal incidence and $\lambda_{0}$=603 nm in an area of $0.9\times0.9$ $\mu$m$^{2}$. (a) Pump field. [(b)–(d)] SERS field at (b) $\lambda_{R}$=$\lambda_{0}$, (c) Stokes emission at $\lambda_{R}$=670 nm, and (d) anti-Stokes emission at $\lambda_{R}$=548.2 nm.

numerical calculations are accurate enough provided that a sufficiently large $N_{p}$ be considered; typically, $N_{p}\geqslant2000$ according to the surface roughness parameters $a$ and $\delta$ (for very rough surfaces $N_{p}>4000$). Mean SERS factors are calculated by averaging over $N_{r}$=300 surfaces, for which the convergence of the numerical results is verified.

## IV. RESULTS AND DISCUSSION

### A. Near field at Raman-shifted frequency

An important achievement of this formulation is the possibility to study the EM fields at Raman-shifted frequencies, separately from that at the pump frequency. Let us first investigate the near EM field close to a hot spot excited on the surface by the pump beam at $\omega_{0}$, and the subsequent near field generated by a LB film on the substrate at various Raman-shifted frequencies $\omega_{R}$. In Fig. 5 the electric near-field intensity maps in a logarithmic scale are shown in the vicinity of a rough surface for $p$-polarized incident light. The surface profile is extracted from a Gaussian-correlated ensemble of realizations obtained as explained in the previous section, with $\delta$=255 nm and $a$=51 nm. The area shown is $1.5\lambda_{0}\times1.5\lambda_{0}$ ($0.9\times0.9$ $\mu$m$^{2}$), with the total illuminated surface being much longer than shown. The dielectric function of the Ag substrate is obtained from Ref. 42.

Four near-field intensity maps are shown: one is the incident plus scattered pump field at $\lambda_{0}$=603 nm, namely, the local electric field driving the Raman-shifted emission of the LB film, whereas the other three are the resulting Raman-shifted, near electric fields for three different Raman shifts $\Delta\omega$: $\omega_{R}\approx\omega_{0}$ (Raman emission case), Stokes emission ($\Delta\omega=-0.1\omega_{0}$), and anti-Stokes emission ($\Delta\omega=0.1\omega_{0}$). We can see a hot spot located in the deep groove at the center of Fig. 5(a); the intensification factor in the vicinity of the hot spot is $\sigma_{E}\sim10^{3}$. This excitation has a dipolelike behavior due to the opposite charge distribution on either groove wall, as stated in Ref. 43. This fact is important in SERS spectroscopy because it imposes selection rules to the vibrational modes of the adsorbed molecule. The Raman electric field intensities shown in Figs. 5(b)–5(d) are normalized with respect to the Raman Fresnel coefficients from a freestanding dipole layer $|\text{R}_{p}^{o}|^{2}$, obtained by illuminating with the same incident angle. As expected, the local maximum of the electric field at the pump frequency exists at the Raman-shifted emission too, confirming the crucial role of localized optical excitations in driving and enhancing the SERS effect. For negligible Raman shift, at $\lambda_{R}$=603 nm, it is seen in Fig. 5(b) that a pattern similar to that of the near electric field intensity at the pump frequency exists with a maximum local enhancement of $\sim10^{7}$. At the Stokes frequency emission $\lambda_{R}$=670 nm [Fig. 5(c)] and at the anti-Stokes frequency emission $\lambda_{R}$=548.2 nm [Fig. 5(d)], we observe slightly different patterns of the near electric field. Qualitatively, the maxima and minima of the intensity appear to be slightly displaced with regard to those in Fig. 5(b); indeed, a minimum is seen in Fig. 5(d) at the groove bottom where the maximum of the local field occurs in Figs. 5(a) and 5(b). Quantitatively, maximum enhancement in Figs. 5(c) and 5(d) at the hot spot, though large $\sim10^{5}$, are about two orders of magnitude below that found for zero Raman shift.

Essentially, Figs. 5(a)–5(d) are spectrally scanning (through the LB Raman shift) the localized optical excitation at $\omega_{0}$. We have verified, not shown here, that such localized SPP (Refs. 22, 41, and 43) has a center frequency at $\lambda$=603 nm, being thus excited by the pump beam, and has a spectral width smaller than the Raman shifts above. For negligible Raman shifts (much smaller than the localized SPP width), near-field patterns at $\omega_{R}$ similar to that at resonance are expected [see Fig. 5(b)], with maximum total enhancement factors due to both resonant excitation and resonant Raman emission. When the Raman shift is such that the emission is outside the spectral range of the localized SPP [see Figs. 5(c) and 5(d)], differences arise and total enhancement factors diminish (only resonant excitation takes place).

It should be emphasized that, strictly speaking, the approximation (1) yields no near-field intensity maps at the Raman-shifted frequency. It simply relies on the near field at the pump frequency as in Fig. 5(a) (for two different pump frequencies, $\omega_{0}$ and $\omega$) to infer the enhancement factors (assuming a single dipole/molecule and reciprocity). In contrast, Figs. 5(b)–5(d) describe the near-field intensity maps at various Raman-shifted frequencies resulting from the collective emission of a (dense) molecular layer on the Ag substrate. The ability of this theoretical formulation to investigate near electromagnetic fields at Raman-shifted frequencies can no doubt be of interest in light of recent advances in surface Raman imaging with nanometric resolution and in near-field spectroscopy using a sharp metal tip.$^{44}$

### B. Far field: SERS factors

We now apply our formulation to obtain the average far field at the Raman-shifted frequency, in the case of very rough silver surfaces, with statistics similar to that of the SERS substrates employed experimentally. First, we analyze the convergence of the mean scattered intensity with increas-

![](./images/811973975843274754_6.jpg)

FIG. 6. (Color online) (a) Angular dependence of the SERS scattered intensity at $\lambda_R=\lambda_0=620$ nm for a pump field normally incident at $\lambda_0=620$ nm, from Ag rough surfaces with $a$=51 nm with $\delta=5a$ (black curves), $\delta=a$ (red curves), and planar surfaces (blue curves), for a single realization (dashed curves) and averaged over 600 realizations (solid curves). (b) Angular dependence of the SERS scattered intensity for various angles of the incident pump field at $\lambda_0=620$ nm: $\theta_0=0$ (blue curves), $\theta_0=20$ (red curves), and $\theta_0=40$ (black curves). Rough Ag surfaces with $a=\delta=51$ nm (thick curves) and a planar surface (thin curves) are considered: $\omega_R=\omega_0$ (solid curves), anti-Stokes emission with $\Delta\omega=0.05\omega_0$ (dashed curves), and Stokes emission with $\Delta\omega=-0.05\omega_0$ (dash-dotted curves).

ing number of realizations. In Fig. 6(a), we show the scattered intensities at the $\omega_R$ Raman-shifted frequency for a normal incident pump beam as a function of the pump frequency $\omega_0$, from a planar surface and from two rough surfaces, for both a single realization and an average over 600 realizations, the Raman shift being negligible in all cases ($\Delta\omega=0$). We have calculated the Raman emission of the plane surface because it is necessary for the normalization; averaging is also needed in this case due to the fact that small domains of random phase are considered to reproduce the incoherent emission of the LB film. The mean scattered intensity of the flat surface at $\omega_R$ presents a nearly structureless angular pattern between $-60^{\circ}$ and $+60^{\circ}$. This is actually a consequence of the imposed spatial incoherence of the Raman emission process, and therefore there is no preferential emission direction, as expected.

The angular distribution of mean scattered intensities in Fig. 6(a) exhibits a smooth behavior with regard to the speckle pattern for a single realization. This confirms that a good convergence is achieved upon ensemble averaging (actually, 300 realizations typically suffice for the roughness parameters considered herein). The oscillations appearing at grazing angles are possibly due to boundary effects stemming from surface truncation and from phase domains. For this reason we will consider only the mean scattered intensity for $\theta$ in between $-30^{\circ}$ and $+30^{\circ}$ in the calculations of $\mathcal{G}_{\text{SERS}}^{\text{EM}}$. The smooth angular behavior found in Fig. 6(a) is preserved when we vary either the angle of incidence of the pump field or the Raman shift, as we can see in Fig. 6(b). We can see that the Raman scattered intensity increases with increasing $\theta_0$ for the planar surface, but this behavior is not observed for the rough surface. The reason is as follows: when the plane wave impacts perpendicularly to a planar surface of a good conductor (as is silver at this frequency), the surface electric field is only tangential and indeed small. In this manner, it follows from Eq. (2) that we have a small Raman driving excitation. For larger angles of incidence, the electric field component normal to the plane increases, so that there is a larger Raman excitation. Note that, upon normalizing by the result for a freestanding LB layer illuminated at the same angle [see Eqs. (13)-(15)], the angular dependence of the Raman emission is being properly considered.

An interesting feature of this model is that we can calculate $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ for frequencies that differ from the pump frequency including collective effects from the entire LB film. In this manner, we can determine the average EM-SERS enhancement factor of a given Raman emission band. This is done in the inset of Fig. 7(a), where the results of the calculations for $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ are shown for fixed pump frequency ($\lambda=620$ nm) and varying Raman shift up to 10% of the pump frequency, considering several surface roughness parameters as in Ref. 41. The results obtained by means of approximation (1), using our scattering formulation too for calculating local pump field enhancements, are included for the sake of comparison. It is clearly seen that the latter exhibits qualitative and quantitative discrepancies with regard to our collective SERS model. Qualitatively, the decay of

![](./images/811973975843274754_7.jpg)

FIG. 7. (Color online) Spectral dependence of the average SERS enhancement factors (averaged over 200 realizations) for rough silver surfaces as a function of the incident frequency (negligible Raman shift) from (a) our collective model and (b) the approximation (1): $a$=51 nm (circles), $a$=102 nm (squares), $\delta$=255 nm (red solid curves), $\delta$=102 nm (black dashed curves), and $\delta$=51 nm (blue dash-dotted curves). Inset: average SERS enhanced factors for fixed pump field at $\omega_0$=2 eV as a function of the frequency shift, calculated with our collective model (solid curves, filled symbols) and with the approximation (1) (dashed curves, hollow symbols), the latter rescaled by the shown factors: $a$=51 nm with $\delta=5a$ (red circles), $\delta=2a$ (black circles), and $a=2\delta=102$ nm (blue squares).

$\mathcal{G}_{\text{SERS}}^{\text{EM}}$ with increasing Raman shift $\Delta\omega$ is underestimated with approximation (1). Quantitatively, the latter significantly overestimates the SERS enhancement factors resulting from our model, as indicated by the explicit scaling factors shown. [Strictly speaking, this occurs when such factors are significant; for the smoother surfaces with irrelevant enhancement factors, approximation (1) indeed underestimates them.]

This is further explored in Figs. 7(a) and 7(b), where the dependence of $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ on pump wavelength for negligible Raman shift is shown from our collective LB film model [cf. Eq. (18)] and from approximation (1), respectively, for different surface roughness parameters: The values predicted with the model presented in this paper are very large, but smaller than those of the approximate calculation, $^{45}$ and differences are indeed more notorious (up to $10^{2}$) with increasing $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ for rougher substrates. Coming back to the dependence on roughness parameters, the remarkable influence of the surface nanostructure on the calculated values of $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ throughout the spectral region analyzed is evident, as seen in Fig. 7(a) from the strong impact that the correlation length $a$ has on the SERS intensification factors; in fact, when the Ag surfaces exhibit strong irregularities of nanoscale dimensions, the obtained SERS factors are substantially bigger.

## V. CONCLUSIONS
In this work we have presented a theoretical model of the electromagnetic contribution to surface-enhanced Raman scattering from a Langmuir-Blodgett film: the Raman response is reproduced by a term in the macroscopic polarization vector that represents a dipole layer that covers the substrate surface. Since such macroscopic term accounts for a collective emission, the model should be appropriate in the case of a dense distribution of molecules on the substrate. Analytical, intuitive results for planar substrates are obtained in the form of generalized Raman Fresnel coefficients. In order to deal with arbitrarily rough SERS substrates, the model is in turn introduced in the exact Green's theorem integral equation formulation of the light scattering. It should be emphasized that the formalism developed in this paper allows us to calculate the scattered field at the Raman-shifted frequency, separately from the EM field at the pump frequency, rigorously including the effect of scattering from the substrate at both frequencies. The formalism has been employed in the study of the SERS emission from LB films on one-dimensional, randomly rough Ag substrates illuminated with a $p$-polarized pump beam (recall that roughness-induced coupling in this configuration into surface plasmons, responsible for the EM field enhancements, is only allowed in $p$ polarization).

Rigorous calculations of the electromagnetic field at the Raman-shifted frequency have been carried out on nanostructured metal surfaces with similar properties to those exhibited by metal substrates used in SERS spectroscopy, with special emphasis on the impact of collective effects and/or Raman shifts as compared to the results obtained from approximation (1). We have presented near-field maps at various $\omega_R$ close to a hot spot on the Ag surface that reveal the detuning of the emission when the Raman shift is larger than the spectral width of the resonantly excited, localized surface plasmon. In addition to local SERS processes, average (collective) effects have been studied through the spectral dependence of $\mathcal{G}_{\text{SERS}}^{\text{EM}}$ on both the pump frequency (for negligible Raman shift) and the Raman-shifted frequency (for fixed pump frequency), in all cases for different surfaces roughness with strong nanoscale irregularities. Experimental means to test some of the predictions of the collective model have in turn been proposed.

## ACKNOWLEDGMENTS
This work was supported in part by the Spanish “Ministerio de Educación y Ciencia” (Grant Nos. FIS2006-07894 and FIS2004-0108) and “Comunidad de Madrid” [Grant No. S-0505/TIC-0191 and one of the authors’ (V.G.) Ph.D. scholarship].

$^{1}$H. Metiu, Prog. Surf. Sci. 17, 153 (1984).
$^{2}$M. Moskovits, Rev. Mod. Phys. 57, 783 (1985).
$^{3}$Surface-Enhanced Raman Scattering, edited by R. K. Chang and T. E. Furtak (Plenum, New York, 1982).
$^{4}$A. Otto, I. Mrozek, H. Grabhorn, and W. Akemann, J. Phys.: Condens. Matter 4, 1143 (1992).
$^{5}$R. Aroca, Surface-Enhanced Vibrational Spectroscopy (Wiley, New York, 2006).
$^{6}$S. Nie and S. R. Emory, Science 275, 1102 (1997).
$^{7}$K. Kneipp, Y. Wang, H. Kneipp, L. T. Perlman, I. Itzkan, R. R. Dasari, and M. S. Feld, Phys. Rev. Lett. 78, 1667 (1997).
$^{8}$C. J. L. Constantino, T. Lemma, P. Antunes, and R. Aroca, Anal. Chem. 73, 4357 (2001).
$^{9}$C. L. Haynes, A. D. McFarland, and R. P. Van Duyne, Anal. Chem. 77, 338A (2005).
$^{10}$C. R. Yonzon, D. A. Stuart, X. Zhang, A. D. McFarland, C. L. Haynes, and R. P. Van Duyne, Talanta 67, 438 (2005).
$^{11}$G. C. Schatz, J. Mol. Struct.: THEOCHEM 573, 73 (2001).
$^{12}$H. Raether, Surface Polaritons on Smooth and Rough Surfaces and on Gratings (Springer-Verlag, Berlin, 1980).
$^{13}$W. L. Barnes, A. Dereux, and T. W. Ebbesen, Nature (London) 424, 824 (2003).
$^{14}$M. Kerker, Acc. Chem. Res. 17, 271 (1984).
$^{15}$D.-S. Wang, M. Kerker, and H. W. Chew, Appl. Opt. 19, 2315 (1980).
$^{16}$M. Kerker, D.-S. Wang, and H. Chew, Appl. Opt. 19, 3373 (1980).
$^{17}$V. M. Shalaev, Phys. Rep. 272, 61 (1996).
$^{18}$V. M. Shalaev, Nonlinear Optics of Random Media: Fractal Composites and Metal-Dielectric Films, Springer Tracts in Modern Physics Vol. 158 (Springer, Berlin, 2000).
$^{19}$F. J. Garcia-Vidal and J. B. Pendry, Phys. Rev. Lett. 77, 1163 (1996).
$^{20}$J. A. Sánchez-Gil and J. V. García-Ramos, Opt. Commun. 134, 11 (1997).
$^{21}$J. A. Sánchez-Gil and J. V. García-Ramos, J. Chem. Phys. 108, 317 (1998).
$^{22}$J. A. Sánchez-Gil, J. V. García-Ramos, and E. R. Méndez, Phys. Rev. B 62, 10515 (2000).
$^{23}$H. Xu, I. Aizpurua, M. Käll, and P. Apell, Phys. Rev. E 62, 4318 (2000).
$^{24}$J. D. Kottmann, O. J. F. Martin, D. R. Smith, and S. Schultz, Chem. Phys. Lett. 341, 1 (2001).
$^{25}$H. Xu, X.-H. Wang, M. P. Persson, H. Q. Xu, M. Käll, and P. Johansson, Phys. Rev. Lett. 93, 243002 (2004).
$^{26}$K. L. Shuford, M. A. Ratner, and G. C. Schatz, J. Chem. Phys. 123, 114713 (2005).
$^{27}$E. C. L. Ru and P. G. Etchegoin, Chem. Phys. Lett. 423, 63 (2006).
$^{28}$M. Kerker, J. Colloid Interface Sci. 118, 417 (1987).
$^{29}$E. J. Zeman and G. C. Schatz, J. Phys. Chem. 91, 634 (1987).
$^{30}$R. R. Chance, A. Prock, and R. Silbey, Adv. Chem. Phys. 37, 1 (1978).
$^{31}$W. L. Barnes, J. Mod. Opt. 45, 661 (1998).
$^{32}$L. A. Blanco and F. J. García de Abajo, Phys. Rev. B 69, 205414 (2004).
$^{33}$C. I. Valencia, E. R. Méndez, and B. Mendoza, J. Opt. Soc. Am. B 20, 2150 (2003).

$^{34}$We take now into account the fact that the LB layer contributing to the Raman-shifted emission is located on the dielectric side of the interface. Thus, strictly speaking, only the contribution from the dielectric half of the Dirac delta in the polarization vector (2) is considered upon calculating the effective Raman Fresnel coefficients (either with or without metal substrate), so that $\mu=(2\varepsilon_{d})^{-1}$.

$^{35}$A. A. Maradudin, T. Michel, A. R. McGurn, and E. R. Mendéz, Ann. Phys. (N.Y.) $\mathbf{203}$, 255 (1990).

$^{36}$J. A. Sánchez-Gil and M. Nieto-Vesperinas, J. Opt. Soc. Am. A $\mathbf{8}$, 1270 (1991).

$^{37}$M. Nieto-Vesperinas, *Scattering and Diffraction in Physical Optics* (Wiley, New York, 1991).

$^{38}$J. A. Sánchez-Gil, J. V. García-Ramos, and E. R. Méndez, Opt. Lett. $\mathbf{26}$, 1286 (2001).

$^{39}$J. A. Sánchez-Gil and J. V. García-Ramos, Chem. Phys. Lett. $\mathbf{367}$, 361 (2003).

$^{40}$See EPAPS Document No. E-JCPSA6-127-810727 for the detailed scattering formulation based on the Green's theorem surface integral equations with polarization vector (2). This document can be reached through a direct link in the online article's HTML reference section or via the EPAPS homepage (http://www.aip.org/pubservs/epaps.html).

$^{41}$J. A. Sánchez-Gil, J. V. García-Ramos, and E. R. Méndez, Opt. Express $\mathbf{10}$, 879 (2002).

$^{42}$D. W. Lynch and W. R. Hunter, in *Handbook of Optical Constants of Solids*, edited by E. D. Palik (Academic, New York, 1985).

$^{43}$J. A. Sánchez-Gil, Phys. Rev. B $\mathbf{68}$, 113410 (2003).

$^{44}$N. Anderson, P. Anger, A. Hartschuh, and L. Novotny, Nano Lett. $\mathbf{6}$, 744 (2006).

$^{45}$V. Giannini, J. A. Sánchez-Gil, J. V. García-Ramos, and E. R. Méndez, Opt. Pura Apl. $\mathbf{37}$, 97 (2004).

The Journal of Chemical Physics is copyrighted by the American Institute of Physics (AIP).
Redistribution of journal material is subject to the AIP online journal license and/or AIP
copyright. For more information, see http://ojps.aip.org/jcpo/jcpcr/jsp