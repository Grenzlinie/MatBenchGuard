![](./images/813175835753185281_1.jpg)

Effect of plasmonic losses on light emission enhancement in quantum-wells coupled to
metallic gratings

Toufik Sadi, Jani Oksanen, and Jukka Tulkki

Citation: *Journal of Applied Physics* **114**, 223104 (2013); doi: 10.1063/1.4845875
View online: http://dx.doi.org/10.1063/1.4845875
View Table of Contents: http://scitation.aip.org/content/aip/journal/jap/114/22?ver=pdfcov
Published by the AIP Publishing

Articles you may be interested in
[Plasmonic modification of electron-longitudinal-optical phonon coupling in Ag-nanoparticle embedded InGaN/GaN quantum wells](http://)
Appl. Phys. Lett. **105**, 091103 (2014); 10.1063/1.4894371

[Effect of the band structure of InGaN/GaN quantum well on the surface plasmon enhanced light-emitting diodes](http://)
J. Appl. Phys. **116**, 013101 (2014); 10.1063/1.4886223

[Plasmon enhanced light emission from InGaN quantum wells via coupling to chemically synthesized silver nanoparticles](http://)
Appl. Phys. Lett. **95**, 151109 (2009); 10.1063/1.3249579

[Polarization dependent coupling of surface plasmon on a one-dimensional Ag grating with an In Ga N/Ga N dual-quantum-well structure](http://)
Appl. Phys. Lett. **92**, 013108 (2008); 10.1063/1.2829794

[Dependence of resonant coupling between surface plasmons and an InGaN quantum well on metallic structure](http://)
Appl. Phys. Lett. **89**, 203113 (2006); 10.1063/1.2390639

![](./images/813175835753185281_2.jpg)

# Effect of plasmonic losses on light emission enhancement in quantum-wells coupled to metallic gratings

Toufik Sadi, Jani Oksanen, and Jukka Tulkki
Department of Biomedical Engineering and Computational Sciences, Aalto University, P.O. Box 12200, FI-00076 Aalto, Finland

(Received 2 September 2013; accepted 25 November 2013; published online 11 December 2013)

Recent experimental work has shown significant luminescence enhancement from near-surface quantum-well (QW) structures using metallic grating to convert surface plasmon (SP) modes into radiative modes. This work introduces a detailed theoretical study of plasmonic losses and the role of SPs in improving light extraction from grated light-emitting QW structures, using the fluctuational electrodynamics method. The method explains experimental results demonstrating emission enhancement, light scattering, and plasmonic coupling in the structures. We study these effects in angle-resolved reflectometry and luminescence setups in InGaN QW structures with silver grating. In contrast to experiments, our model allows direct calculation of the optical losses. The model predicts that the plasmonic coupling and scattering increases light emission by a factor of up to three compared to a flat semiconductor structure. This corresponds to reducing the absorption losses from approximately 93% in the ungrated metallic structure to 75% in the grated structure. Lower losses are associated with a significant emission enhancement enabled by the SPs of silver/GaN interfaces, which are present in the blue/green wavelength range, and can be optimized by carefully nanostructuring the metal layer and by the positioning of the QW. In general, the enhancement results from the interplay of mode scattering, conversion of SP energy directly into light, and losses in the metallic grating. The reported losses are very high when compared to the losses present in modern light-emitting diodes (LEDs). Albeit, our work provides tools needed for further optimization of plasmonic light extraction, eventually leading to highly efficient LEDs. © 2013 AIP Publishing LLC. [http://dx.doi.org/10.1063/1.4845875]

## I. INTRODUCTION

Surface plasmons (SPs) have recently gained significant attention due to their sub-wavelength localization and strong near-field interactions. $^{1-7}$ One of the most studied applications of these benefits has been the emission enhancement in light-emitting InGaN quantum-well (QW) structures, aimed for use in next-generation light emitting diodes (LEDs). An increase of light output by a factor of up to 15 has been reported in InGaN QW structures, due to plasmonic coupling caused by, e.g., silver gratings, nanoparticles, or other surface treatments. $^{8-16}$ However, there are far fewer reports on the detailed origin of the enhancement, the exact physical role of surface plasmons in the process, and the effect of losses, with possibly the only exception being the work by Sun et al. $^{17}$ Furthermore, the theoretical estimations of the luminescence enhancement is in most cases based on calculating the intensity of the electromagnetic modes or the corresponding coupled mode analysis. $^{17}$ While these methods are often relatively simple and provide valuable insight into the interactions, describing the details of absorption losses in these models typically requires additional assumptions or supporting models.

In this paper, we present a first-principle theoretical model for the description of the interactions of optical fields, plasmons, and light emission in multilayer structures including metallic gratings. The model essentially consists of the vectorial non-homogeneous Helmholtz equation where the nonhomogeneous terms arise from stochastic thermal fluctuations corresponding to spontaneous emission and correlated excitations resulting from the scattering of the light fields. The stochastic light emission model known as the fluctuational electrodynamics (FED) model was originally developed by Rytov in 1950s. $^{18,19}$ Since then, it has been extensively used to study thermal emission and related energy transfer phenomena (e.g., Refs. 20 and 21). Optical scattering in multilayers has also been previously studied in the context of light scattering by dielectric perturbations. $^{16,22,23}$ In distinction to previous work, we (i) combine these two approaches to enable describing light emission and scattering within grated multilayer structures incorporating an emitting QW, (ii) study structures where surface plasmons are present, focusing on plasmonic enhancement and losses, and (iii) develop a recursive solution method based on using the Green's functions for stratified media. $^{20}$

The developed method is applied to study the mode structure, reflectometry patterns, luminescence enhancement, and the contribution of the evanescent SP modes to the enhancement and optical losses in a light emitting $Ag/GaN/In_{0.12}Ga_{0.88}N/GaN/Al_{2}O_{3}$ multilayer structure, as illustrated in Fig. 1. The structure includes a thin grated silver layer that scatters the emitted light and also increases the emission rate of the excited $In_{0.12}Ga_{0.88}N$ quantum well deposited very close to the silver layer. $^{15}$ This paper is organized as follows. The theoretical model to describe the electric fields and their relation to propagating powers in the structure is described in Sec. II. Description starts with formulating the recursive equations for the electric field in real

![](./images/813175835753185281_3.jpg)

FIG. 1. The studied structures, formed by a Ag/GaN/In₀.₁₂Ga₀.₈₈N/ GaN/Al₂O₃ heterostructure, (a) without a grating and (b) with a grating. We assume a one-dimensional squarewave silver grating, including 50% silver and 50% air. It is of note that the figures are not in scale.

space, which is followed by transforming the equations to the Fourier space, solving the fields and calculating the prop- agating powers from Poynting's theorem. In Sec. III, we employ the model to map out the dispersion relations of the structures, and to study the emission enhancement in the grated structures and the energy transfer and loss due to the metallic gratings.

## II. THEORY
### A. Equations in real space
A general semi-classical formulation of light emission and power transfer can be directly derived from Maxwell's equations when it is assumed that thermal emission is described by fluctuating spatially uncorrelated thermal sour- ces each generating uncorrelated electric field components as originally suggested by Rytov. $^{18,19}$ The non-homogeneous Helmholtz equation governing the fields in non-magnetic and isotropic media is then given by
$$\nabla \times \nabla \times \mathbf{E}(\mathbf{r})-k_{0}^{2} \epsilon_{\mathrm{r}}(\mathbf{r}) \mathbf{E}(\mathbf{r})=-i \omega \mu \mathbf{J}(\mathbf{r}), \quad(1)$$
where $E(r)$ is the electric field vector, $J(r)$ represents a fluc tuating current source or an ensemble of correlated current sources generating the field, and $\epsilon_{r}(r)$ is the dielectric con stant at point $r$. Constant $\mu$ is the permeability, $k_{0}=\omega / c$ is the wavenumber in vacuum, $\omega$ is the angular frequency, and $c$ is the speed of light in vacuum. For thermal emission, $J(r)$  is typically a point source of the form $J(r) \propto \delta(r-r_{s})$ with $r_{s}$ being the point source coordinate and the orientation of $J$  being, e.g., along unit vector $u_{x}, u_{y}$ , or $u_{z}$ in the three dimensional real space.

### B. Perturbation equations
In the grated system of Fig. 1(b), the permittivity can be separated into part $\epsilon_{r 0}(z)$ describing the ungrated system of Fig. 1(a) with $z$ -direction chosen to be normal to the layer interfaces, and part $\epsilon_{rs}(r)=\Delta \epsilon_{r}(r)=\epsilon(r)-\epsilon_{r 0}(z)$ describing the permittivity difference between the grated and the ungrated system. Similarly, writing the electric field as $E(r)=E_{0}(r)+E_{s}(r)$ , where $E_{0}(r)$ satisfies Eq. (1) with $\epsilon_{r}(r)=\epsilon_{r 0}(z)$ so that $E_{0}(r)$ represents the unscattered field in the ungrated structure, allows rewriting Eq. (1) as
$$\begin{aligned}
& \nabla \times \nabla \times \mathbf{E}_{\mathrm{s}}(\mathbf{r})-k_{0}^{2} \epsilon_{\mathrm{r} 0}(z) \mathbf{E}_{\mathrm{s}}(\mathbf{r}) \\
& \quad=k_{0}^{2} \Delta \epsilon_{\mathrm{r}}(\mathbf{r})\left\{\mathbf{E}_{0}(\mathbf{r})+\mathbf{E}_{\mathrm{s}}(\mathbf{r})\right\},
\end{aligned}\qquad(2)$$
where the total electric field for the grated structure $E(r)=$  Eo(r)+Es(r) appears as an additional extended source term in the right-hand side of Eq.(2). Equation (2) for the scat- tered field $E_{s}$ can further be transformed to an integral equation
$$\mathbf{E}_{\mathrm{s}}(\mathbf{r})=k_{0}^{2} \int \Delta \epsilon_{\mathrm{r}}\left(\mathbf{r}_{\mathrm{s}}\right) \overleftrightarrow{G}_{0}\left(\mathbf{r}, \mathbf{r}_{\mathrm{s}}\right) \cdot\left\{\mathbf{E}_{0}\left(\mathbf{r}_{\mathrm{s}}\right)+\mathbf{E}_{\mathrm{s}}\left(\mathbf{r}_{\mathrm{s}}\right)\right\} \mathrm{d} \mathbf{r}_{\mathrm{s}}, \quad(3)$$
 when using the well known dyadic Green's function $\overleftrightarrow{G}_{0}(r, r_{s})$ of stratified media $^{20}$ which describes the contribu tion of a source term located at point $r_{s}$ to the field $E_{s}(r)$ . In case of stratified media, the Green's function satisfies thevectorial Helmholtz equation $^{24}$ 
$$\nabla \times \nabla \times \overleftrightarrow{G}_{0}\left(\mathbf{r}, \mathbf{r}_{\mathrm{s}}\right)-k_{0}^{2} \epsilon_{\mathrm{r} 0}(z) \overleftrightarrow{G}_{0}\left(\mathbf{r}, \mathbf{r}_{\mathrm{s}}\right)=\mathbf{I} \delta\left(\mathbf{r}-\mathbf{r}_{\mathrm{s}}\right), \quad(4)$$
 where $I$ is the unit dyadic. The scattered field $E_{s}$ can be determined by using the standard numerical techniques to solve the integral Eq. (3) as discussed, e.g., in Refs. 22 and23. In contrast to previous works, we employ a recursive so- lution method that is more transparent because the fields can be written in a simple closed form.

### C. Recursive solution
Using a recursive approach, the $n$ th order approximation(n >0) for the total electric field can be written as a recur- sive series
$$\mathbf{E}_{n}(\mathbf{r})=\mathbf{E}_{0}(\mathbf{r})+k_{0}^{2} \int \Delta \epsilon_{\mathrm{r}}\left(\mathbf{r}_{\mathrm{s}}\right) \overleftrightarrow{G}_{0}\left(\mathbf{r}, \mathbf{r}_{\mathrm{s}}\right) \cdot \mathbf{E}_{n-1}\left(\mathbf{r}_{\mathrm{s}}\right) \mathrm{d} \mathbf{r}_{\mathrm{s}}, \quad(5)$$
 where the zeroth order term is in general obtained from the response of the ungrated system to a source term describing a thermal source or an incident field, as discussed in Subsections II D-II G. Typically, it is sufficient to consider a few terms (in our work $n=3$ ) of the series described by Eq. (5) for an accurate calculation of the electric field, as will be shown in Sec. III.

### D. Fourier decomposition of the equations
To solve and analyze electric fields in Eq. (5), it is more convenient to use the two-dimensional (2D) Fourier transfor- mations $E_{n}, \Delta \epsilon_{r}$ , and $\overleftrightarrow{G}_{0}$ of the electric fields $E_{n}$ , changes in permittivity $\Delta \epsilon_{r}$ , and the Green's function $\overleftrightarrow{G}_{0}$ , respectively. To this end, we first write Eq. (5) using the 2D Fourier trans- formed expressions as

$$
\begin{aligned}
\mathbf{E}_{n}(\mathbf{r})= & \frac{1}{(2 \pi)^{2}} \int \mathcal{E}_{0}(z, \mathbf{K}) \mathrm{e}^{i \mathbf{K} \cdot \mathbf{R}} \mathrm{d} \mathbf{K} \\
& +\frac{k_{0}^{2}}{(2 \pi)^{6}} \int\left[\int \Delta \varepsilon_{\mathrm{r}}\left(z_{\mathrm{s}}, \mathbf{K}_{\mathrm{p}}\right) \mathrm{e}^{i \mathbf{K}_{\mathrm{p}} \cdot \mathbf{R}_{\mathrm{s}}} \mathrm{d} \mathbf{K}_{\mathrm{p}}\right] \\
& {\left[\int \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right) \mathrm{e}^{i \mathbf{K} \cdot\left(\mathbf{R}-\mathbf{R}_{\mathrm{s}}\right)} \mathrm{d} \mathbf{K}\right] } \\
& \cdot\left[\int \mathcal{E}_{n-1}\left(z_{\mathrm{s}}, \mathbf{K}_{\mathrm{E}}\right) \mathrm{e}^{i \mathbf{K}_{\mathrm{E}} \cdot \mathbf{R}_{\mathrm{s}}} \mathrm{d} \mathbf{K}_{\mathrm{E}}\right] \mathrm{d} \mathbf{r}_{\mathrm{s}},
\end{aligned}
$$

where, in general, the position is written as $\mathbf{r}=x \mathbf{u}_{\mathrm{x}}+y \mathbf{u}_{\mathrm{y}}$ $+z \mathbf{u}_{z}=\mathbf{R}+\mathbf{z}$, and the wavevector as $\mathbf{k}=k_{\mathrm{x}} \mathbf{u}_{\mathrm{x}}+k_{\mathrm{y}} \mathbf{u}_{\mathrm{y}}$ $+k_{\mathrm{z}} \mathbf{u}_{\mathrm{z}}=\mathbf{K}+\mathbf{k}_{\mathrm{z}}$. As a convention, $\mathbf{R}$ and $\mathbf{K}$ indicate the parallel components of the positions and wavevectors (in the $x-y$ plane) while $\mathbf{z}$ and $\mathbf{k}_{\mathrm{z}}$ indicate the perpendicular parts of these vectors. For a given free-space wavenumber $k_{0}$, the wavevector components satisfy $\epsilon_{\mathrm{r}} k_{0}^{2}=k_{\mathrm{x}}^{2}+k_{\mathrm{y}}^{2}+k_{\mathrm{z}}^{2}$. The 2D Fourier transformed version of Eq. (5) is then

$$
\begin{aligned}
\mathcal{E}_{n}(z, \mathbf{K})= & \mathcal{E}_{0}(z, \mathbf{K})+\frac{k_{0}^{2}}{(2 \pi)^{2}} \iint \Delta \varepsilon_{\mathrm{r}}\left(z_{\mathrm{s}}, \mathbf{K}_{\mathrm{p}}\right) \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right) \\
& \cdot \mathcal{E}_{n-1}\left(z_{\mathrm{s}}, \mathbf{K}-\mathbf{K}_{\mathrm{p}}\right) \mathrm{d} \mathbf{K}_{\mathrm{p}} \mathrm{d} z_{\mathrm{s}} .
\end{aligned}
$$

The dyadic $\overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right)$ is the one-dimensional (1D) dyadic Green's function for a simple multilayer structure, which sat- isfies the vectorial Helmholtz equation

$$
\nabla \times \nabla \times \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right)-k_{\mathrm{z}}^{2} \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right)=\mathbf{I} \delta\left(z-z_{\mathrm{s}}\right).
$$

The solution of Eq. (8) in a piecewise homogeneous multi- layer structure is given, e.g., in Refs. 16 and 20 and is not repeated here for the sake of keeping the discussion concise.

Equation (7) essentially shows how the broadening of the Fourier spectrum of the change in permittivity enables the scattering of the electric field. As discussed in Secs. II E-II G, the Fourier-transformed form is very insight- ful, especially for the cases where the change in the dielectric permittivity is periodic and has only a few significant Fourier components present.

### E. Fields in the ungrated structure

The electric field $\mathbf{E}_{0}$ for the ungrated structure is calculated using two alternative forms, depending on whether (i) the field is generated internally by fluctuating current sources in the quantum well (as is the case for studying luminescence enhancement) or (ii) externally by incident fields (as is the case for studying reflectometry patterns). Mathematically, it is convenient to parametrize also the incident field due to external light sources using a source term $\mathbf{J}$. The electric field $\mathbf{E}_{0}$ for the ungrated structure is, in general, related to $\overleftrightarrow{G}_{0}$ by

$$
\mathbf{E}_{0}(\mathbf{r})=i \omega \mu \int \overleftrightarrow{G}_{0}\left(\mathbf{r}, \mathbf{r}_{\mathrm{s}}\right) \cdot \mathbf{J}\left(\mathbf{r}_{\mathrm{s}}\right) \mathrm{d} \mathbf{r}_{\mathrm{s}}
$$

In this work, both types of excitations exhibit a $\delta$-like $z$-dependence (see, e.g., Refs. 20 and 25) which allows to write the Fourier transform of the field simply as

$$
\mathcal{E}_{0}(z, \mathbf{K})=i \omega \mu \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s} 0}, \mathbf{K}\right) \cdot \mathcal{J}\left(z_{\mathrm{s} 0}, \mathbf{K}\right),
$$

where $\mathcal{J}$ is the Fourier transform of $\mathbf{J}$ and $z_{\mathrm{s} 0}$ is the $z$-coordinate of the source or the plane at which the incident power is fixed. The Fourier-transformed current terms $\mathcal{J}$ are given by

$$
\mathcal{J}(z, \mathbf{K})= \begin{cases}\mathbf{u}_{\mathrm{l}}, & \text { for a current source } \\ \mathbf{u}_{\mathrm{in}} \delta\left(\mathbf{K}-\mathbf{K}_{\mathrm{in}}\right) & \text { for an incident plane wave, }\end{cases}
$$

where $\mathbf{u}_{\mathrm{l}}$ is a unit vector in the direction of (i) $z$-axis $\left(\mathbf{u}_{\mathrm{z}}\right)$, (ii) TE polarization vector, or (iii) perpendicular to both of these. In the QW structure studied here, setting $\mathbf{u}_{1}$ along the $y$-axis $\left(\mathbf{u}_{\mathrm{y}}\right)$ produces $s$-polarized (TE) light while the other two choices $\left(\mathbf{u}_{\mathrm{x}}\right.$ or $\mathbf{u}_{\mathrm{z}}$ ) produce $p$-polarized (TM) light. In general, the source term $\mathbf{J}$ also depends on the absorption coefficient, temperature, and excitation of the emitting material, as explained in, e.g., Ref. 26. However, for the purpose of this work we can neglect these dependencies and simply assume the normalized $\mathbf{J}$. Wavevector $\mathbf{u}_{\text {in }}$ is the unit polarization vector of the polarization (e.g., TE or TM) of the incident field, and $\mathbf{K}_{\text {in }}$ is the parallel wavevector of the incident field.

### F. Example: 1st order approximation for a periodic square grating

In this section, we discuss briefly how a periodic grating scatters light in the multilayer structures. For this purpose, we study as an example the first-order scattering term $\mathcal{E}_{1}^{\mathrm{s}}(z, \mathbf{K})=\mathcal{E}_{1}(z, \mathbf{K})-\mathcal{E}_{0}(z, \mathbf{K})$ obtained directly from the integral in Eq. (7). For the square-wave (1D) grating along the $x$-axis shown in Fig. 1(b), the Fourier-transformed change in permittivity is $\Delta \varepsilon_{\mathrm{r}}(z, \mathbf{K})=\Delta \epsilon_{\mathrm{r}}\left\{\sum_{m} a_{m}\right.$ $\left.\delta\left(k_{\mathrm{x}}-m K_{\mathrm{P}}\right)\right\} \delta\left(k_{\mathrm{y}}\right)$, where $\Delta \epsilon_{\mathrm{r}}$ is the difference in the relative permittivities of the two materials forming the grated layer (silver and air in the studied structure), $m$ is an integer, $K_{\mathrm{P}}=2 \pi / L$ is the wavenumber of the period ( $L$ being the grating period), and $a_{m}$ are the Fourier-transform coefficients of the square wave. Therefore, the expression for $\mathcal{E}_{1}^{\mathrm{s}}(z, \mathbf{K})$ reduces to

$$
\begin{aligned}
\mathcal{E}_{1}^{\mathrm{s}}(z, \mathbf{K})= & \frac{k_{0}^{2}}{(2 \pi)^{2}} \Delta \epsilon_{\mathrm{r}} \int_{z_{\mathrm{b}}}^{z_{\mathrm{t}}} \overleftrightarrow{\mathcal{G}}_{0}\left(z, z_{\mathrm{s}}, \mathbf{K}\right) \\
& \cdot\left\{\sum_{m} a_{m} \mathcal{E}_{0}\left(z_{\mathrm{s}}, \mathbf{K}+m K_{\mathrm{P}} \mathbf{u}_{\mathrm{x}}\right)\right\} \mathrm{d} z_{\mathrm{s}},
\end{aligned}
$$

where $z_{\mathrm{b}}$ and $z_{\mathrm{t}}$ are the $z$-coordinates of the bottom and top boundaries of the grated layer. Equation (12) essentially shows that incident light with a wavevector component $k_{\mathrm{x}}$ can generate scattered waves for which

$$
\Delta k_{\mathrm{x}}=m K_{\mathrm{P}}=m \frac{2 \pi}{L} .
$$

Accounting for higher-order terms $\mathcal{E}_{n}$ ( $n=3$ in this work) contributes also qualitatively to the broadening of the scattered modes and quantitatively to the accurate determination of their intensities.

### G. Calculation of the intensity: Poynting's theorem

The intensity and the direction of the power flow are determined using the time-averaged Poynting vector which for harmonic fields is obtained from²⁴

$$
\mathbf{S}(\mathbf{r})=\frac{1}{2} \Re\left(\mathbf{E}(\mathbf{r}) \times \mathbf{H}^{*}(\mathbf{r})\right),\qquad(14)
$$

where $\mathbf{H}(\mathbf{r})$ is the magnetic field vector satisfying $\mathbf{H}(\mathbf{r})=$ $-i(\omega \mu)^{-1} \nabla \times \mathbf{E}(\mathbf{r})$ in real space and $\mathcal{H}(z, \mathbf{K})=-i(\omega \mu)^{-1}$ $(\mathbf{K}+\mathbf{u}_{z} \partial_{z}) \times \mathcal{E}(z, \mathbf{K})$ in Fourier space.

The total power $P_{\text {tot }}(z)$ along $\mathbf{u}_{z}$ (i.e., through a $x$-$y$ plane characterized by coordinate $z$) due to a single source point at coordinates $R_{s 0}$ and $z_{s 0}$, or an incident wave is then obtained from Eq. (14) in terms of the Fourier transformed fields as

$$
\begin{aligned}
P_{\mathrm{tot}}(z) & =\int \mathbf{S}(\mathbf{r}) \cdot \mathbf{u}_{z} \mathrm{~d} \mathbf{R}, \\
& =\frac{1}{32 \pi^{4}} \Re \iint\left[\left[\int \mathcal{E}(z, \mathbf{K}) \mathrm{e}^{i \mathbf{K} \cdot \mathbf{R}} \mathrm{d} \mathbf{K}\right]\right. \\
& \left.\times\left[\int \mathcal{H}^{*}\left(z, \mathbf{K}^{\prime}\right) \mathrm{e}^{-i \mathbf{K}^{\prime} \cdot \mathbf{R}} \mathrm{d} \mathbf{K}^{\prime}\right]\right\} \cdot \mathbf{u}_{z} \mathrm{~d} \mathbf{R}, \\
& =\frac{1}{8 \pi^{2}} \Re \int\left\{\left\{\mathcal{E}(z, \mathbf{K}) \times \mathcal{H}^{*}(z, \mathbf{K})\right\} \cdot \mathbf{u}_{z} \mathrm{dK}.\right.
\end{aligned}
$$

The last equation shows that the total power can be obtained simply by separately summing over the plane wave components. The sum converges to a finite value in the case of a single source point and diverges to infinity in the case of an incident wave. In the following we are, however, more interested in the average intensities $P(z)$ propagating along $\mathbf{u}_{z}$ due to an incident wave or a continuous distribution of point sources in the quantum well rather than the total power.

For periodic structures, the power flow calculations can be simplified as follows. In the case of a continuous distribution of point sources in the quantum well at coordinates $R_{s 0}$ and $z_{s 0}$, we calculate the average intensity $P(z)$ from the total power flow $P_{\text {tot }}(z)$ along $\mathbf{u}_{z}$ by summing over the power emitted by all source points and normalizing by the area of the $x$-$y$ plane, i.e.,

$$
\begin{aligned}
P(z)= & \frac{1}{\int \mathrm{d} \mathbf{R}} \iint P_{\text {tot }} \mathrm{d} \mathbf{R}_{\mathrm{s} 0} \mathrm{~d} z_{\mathrm{s} 0} \\
& =\frac{1}{8 \pi^{2} L} \Re \int_{0}^{L} \int_{z_{\text {bottom }}}^{z_{\text {top }}}\left[\left\{\left\{\mathcal{E}(z, \mathbf{K}) \times \mathcal{H}^{*}(z, \mathbf{K})\right\} \cdot \mathbf{u}_{z} \mathrm{dK}\right] \mathrm{d} x_{\mathrm{s} 0} \mathrm{d} z_{\mathrm{s} 0}\right. \\
& =\int \mathcal{P}(z, \mathbf{K}) \mathrm{d} \mathbf{K},
\end{aligned}
$$

where $L$ is the length of the grating period, and $z_{\text {bottom }}$ and $z_{\text {top }}$ are the lower and upper limiting values of the source point coordinate $z_{s 0}$. In Eq. (16), $\mathcal{P}(z, \mathbf{K})=\frac{1}{8 \pi^{2} L} \Re$ $\left[\int_{0}^{L} \int_{z_{\text {bottom }}}^{z_{\text {top }}}\left\{\mathcal{E}(z, \mathbf{K}) \times \mathcal{H}^{*}(z, \mathbf{K})\right\} \cdot \mathbf{u}_{z} \mathrm{d} x_{\mathrm{s} 0} \mathrm{d} z_{\mathrm{s} 0}\right]$ is the average angle-resolved luminescence intensity. In this case, we have converted the integral over the parallel coordinates to $\int \mathrm{d} \mathbf{R}=\sum_{n} \int \mathrm{d} y \int_{0}^{L} \mathrm{~d} x$ to highlight that numerically it is sufficient to average the intensity over one (grating) period $L$, in a structure with 1D grating along the $x$-axis.

In case of an incident wave, the average intensity is calculated from $P(z)=P_{\text {tot }}(z) / \int \mathrm{d} \mathbf{R}$. By noting that in this case the fields essentially consist of plane waves described by $\delta$-functions in the Fourier spectrum, the average power is obtained from

$$
P(z)=\int \mathcal{P}(z, \mathbf{K}) \mathrm{d} \mathbf{K},\qquad(17)
$$

where $\mathcal{P}(z, \mathbf{K})=\sum_{n} \frac{\delta\left(\mathbf{K}-\mathbf{K}_{n}\right)}{8 \pi^{2}} \Re\left[\left\{\int_{\mathbf{K}_{n}}^{\mathbf{K}_{n}+\mathrm{d} \mathbf{K}} \mathcal{E}\left(z, \mathbf{K}^{\prime}\right) \mathrm{d} \mathbf{K}^{\prime} \times \int_{\mathbf{K}_{n}}^{\mathbf{K}_{n}+\mathrm{d} \mathbf{K}}\right.\right.$ $\left.\mathcal{H}^{*}\left(z, \mathbf{K}^{\prime}\right) \mathrm{d} \mathbf{K}^{\prime}\right\} \cdot \mathbf{u}_{z}$. Despite the complex appearance, this definition of $\mathcal{P}(z, \mathbf{K})$ simply gives the average intensity as a function of the parallel wavevector component $\mathbf{K}$ and the plane wave coefficients for a field made of multiple plane waves with wavevectors $\mathbf{K}_{n}$. For periodic grating, $\mathbf{K}_{n}=\mathbf{K}_{\text {in }}+n \mathbf{K}_{\mathrm{P}}$, where $\mathbf{K}_{\text {in }}$ is the incidence wavevector and $\mathbf{K}_{\mathrm{P}}$ is the grating period vector.

Power propagates along both directions of the $z$-axis and the electric field $\mathcal{E}(z, \mathbf{K})$ generally includes a forward traveling component $\mathcal{E}_{+}$(with a $z$-dependence of the form $\mathrm{e}^{i k_{z} z}$ ) and a backward-traveling component $\mathcal{E}_{-}$(with a $z$-dependence of the form $\mathrm{e}^{-i k_{z} z}$ ). $^{20}$ In a lossless layer (e.g., air in the case of reflectivity), the energy flux $\mathcal{P}(z, \mathbf{K})$ can be separated into a forward propagating power $\mathcal{P}_{+}=\mathcal{E}_{+} \times \mathcal{H}_{+}$ and a backward propagating power $\mathcal{P}_{-}=\mathcal{E}_{-} \times \mathcal{H}_{-}$. These forward and backward propagating components are used to determine, e.g., the reflectivity of the grated multilayers, as needed in reflectometry studies; reflectivity is given by the ratio of the reflected intensity $\mathcal{P}_{-}$to the incident intensity $\mathcal{P}_{+}$.

### III. RESULTS AND DISCUSSION

In this section, we apply the theory developed above to simulate scattering and plasmonic interactions in the commonly used angle-resolved reflectometry and luminescence setups schematically illustrated in Figs. 2(a) and 2(b). The studied structures consist of a multilayer QW light-emitting device with a 1D grating. Like the common experiments, we study emission, angle-resolved reflectometry and scattering in the plane perpendicular to the grating (i.e., the $x$-$z$ plane in Fig. 1). $^{15}$ In the simulations, the one-dimensional silver grating has a periodicity of $200 \mathrm{~nm}$ (i.e., comparable to the wavelength of light) including $50 \%$ silver and $50 \%$ air. Unless stated otherwise, analysis is performed assuming that the thicknesses of the silver, InGaN QW, and GaN buffer layers are $17 \mathrm{~nm}, 2 \mathrm{~nm}$, and $3 \mu \mathrm{m}$, respectively. In this work, we use the GaN and InGaN permittivities provided in Ref. 27 and the Ag permittivity provided in Ref. 28.

#### A. Modes and resonances in the ungrated structure

To understand the properties of the periodically grated structures, it is helpful to first map out the different resonances and modes present in the ungrated metallic structure of Fig. 1(a), using the local density of states (LDOS). By definition, the LDOS describes the coupling strength between e.g. a thermal source and the field and highlights the positions and widths of the various modes and resonances of the structures. Such information is not available when using simpler methods for locating modes and resonances, such as the

![](./images/813175835753185281_4.jpg)

FIG. 2. (a) The experimental angle-resolved reflectometry setup, from which reflectivity is recorded as a function of wavelength (frequency) and the incidence parallel wavevector $\mathbf{K}_{\text{in}}$ or the incidence angle $\theta$ satisfying $\sin(\theta) = K_{\text{in}}/k_0$. (b) Schematic representation of the luminescence enhancement setup to study two structures: (i) a flat semiconductor structure (without a metal) and (ii) a structure with a 17 nm silver layer grated with a 200 nm period. Both structures incorporate a 2 nm-thick $\text{In}_{0.12}\text{Ga}_{0.88}\text{N}$ QW separated from the top surface by the 10 nm GaN barrier layer.

transfer matrix method. $^{16}$ The LDOS is evaluated using the common definition relating this quantity to the imaginary part of the trace of the dyadic Green's function $\omega/(\pi c^{2}) \text{Im}\,\text{Tr}[\overleftrightarrow{G}_{0}(\mathbf{r},\mathbf{r},\omega)].^{21}$ Figs. 3(a) and 3(b) show a typical LDOS map for TM and TE polarizations, respectively, evaluated at the quantum well position $z = z_{s} = z_{s0}$ in the ungrated metallic structure of Fig. 1(a), as a function of wavelength and parallel wavevector. The resonances in Fig. 3(a), from top to bottom, consist of the GaN/Ag surface plasmon, GaN guided modes between the GaN cone line and the sapphire cone line, GaN resonance lines, the air/Ag surface plasmon, and the Fabry-Perot patterns in the air light cone. The light cones for air, sapphire, and GaN are defined by inequation $|\mathbf{K}| < nk_{0}$, where $n$ is the refractive index of each material. The Ag/Air surface plasmon is not visible in the LDOS evaluated at the QW position as its intensity is significantly reduced in the GaN layer. The TE curve features in Fig. 3(b) are similar to those in the TM case, except that the SP modes do not exist. By quantitatively comparing the TE and TM curves, one can observe that the value of the density of states for the TM polarization can be a few orders of magnitude higher than that for TE polarization, due to the presence of the SP modes. By using grating to scatter the SP modes to radiative modes, it is possible to exploit the huge LDOS available from SP modes to enhance luminescence from the structures, as discussed below.

![](./images/813175835753185281_5.jpg)

## B. Angle-resolved reflectometry

Angle-resolved reflectometry measurements are very useful in determining the properties of the grated light-emitting structures, especially in getting information on the optical modes present in the structures experimentally. To compare our results to experiments, $^{15}$ we have simulated the angle-resolved reflectometry using the schematic setup shown in Fig. 2(a). Fig. 4 shows the angle-resolved reflectometry patterns for both the ungrated metallic and grated metallic structures of Fig. 1, for TM polarization and parallel wavevectors in the range $|\mathbf{K}| < k_{0}$ (corresponding to a part of the light cone). The reflectometry patterns for the ungrated structure include only the Fabry-Perot resonances in the light cone while the grated structure also shows additional features due to the scattering of the bound modes and resonances into the light cone. These include a set of lines corresponding to the scattered propagating GaN modes and resonances, and the scattered GaN/Ag surface plasmon

![](./images/813175835753185281_6.jpg)

FIG. 4. Reflectivity as a function of wavelength and the input direction of the incident wave, for (a) the ungrated metallic and (b) grated metallic structures of Fig. 1, for TM polarization.

modes. Fig. 4(b) also demonstrates how the applied method accounts for the broadening of the plasmonic and guided modal lines and the mixing of the modes by the grating. Similar features were directly observed experimentally. $^{15,16}$

### C. Luminescence enhancement
In this section, we study emission enhancement from a quantum well for TM polarization by simulating a setup where the QW is located 10 nm below the GaN/silver interface, as illustrated in Fig. 2(b). We calculate emission separately for current term (J) orientations along $\mathbf{u}_{\mathbf{l}}=\mathbf{u}_{x}$ and $\mathbf{u}_{\mathbf{l}}=\mathbf{u}_{z}$. Both orientations excite TM waves. $^{6,20,21,25}$ The results presented are obtained from intensities averaged equally over both contributions. In typical QW structures, the optical matrix elements for $z$-oriented dipoles are generally smaller than for $x$-oriented dipoles. $^{29}$ The anisotropy in the matrix elements for a given structure can be easily accounted for by adding an orientation dependent weight factor in each component of the current source term $\mathbf{J}$. For simplicity, however, we assume equal current source term components for both dipole orientations and calculate the emitted intensities as a sum of the intensities generated by the $x$- and $z$-oriented current sources. Such assumption does not introduce significant quantitative changes in the results nor affect the qualitative conclusions made in this work.

Figs. 5(a) and 5(b) show angle-resolved luminescence for the planar semiconductor and grated structures, respectively, for TM polarization. While Fabry-Perot resonances are the only features observed in Fig. 5(a), Fig. 5(b) shows the signature of a strong GaN/Ag surface plasmon and additional patterns resulting from weaker GaN propagating modes and resonances. In fact, for a parallel wavevector $\mathbf{K}$ corresponding to the dispersion of the GaN/Ag SP, an enhancement of more than one order of magnitude is observed.

![](./images/813175835753185281_7.jpg)

FIG. 5. The calculated angle-resolved luminescence for (a) the flat semiconductor structure and (b) the silver-grated structure, for TM polarization.

To provide a useful quantitative estimate of the enhancement due to the grating, we also evaluate the maximal total luminescence for both structures by integrating the intensity shown in Fig. 5 over all the wavevector directions within the light cone $(|\mathbf{K}|<k_{0})$ at a given wavelength, as described by Eq. (16). Fig. 6 shows, as a function of wavelength and for different QW positions, the luminescence enhancement factor defined as the ratio of the total power emitted by the studied (grated) structure to the total power emitted by the flat semiconductor (reference) structure (shown in Fig. 2(b)). This definition corresponds to the earlier definitions of luminescence and absorption enhancements. $^{15,30-32}$ The maximal enhancement factor is in this example as high as 2.8, 2.3, and 1.5 for a QW located 1 nm, 10 nm, and 20 nm below the grating, respectively, for a wavelength $\lambda \sim 540$ nm. However, Fig. 6 also indicates a strong dependence of the enhancement on the QW position. The theoretical upper limit of the enhancement for lossless ergodic structures $^{30,31}$ is $2 \epsilon$ (i.e., approximately 15 for GaN based structures), but the intrinsic losses due to the thin QW typically reduce the enhancement to only $2-3.^{31}$ This is comparable to the values observed here as well although the

![](./images/813175835753185281_8.jpg)

FIG. 6. The luminescence enhancement as a function of wavelength, for different QW positions and for TM polarization.

ergodic limit does not directly apply to strongly resonant plasmonic structures where a much larger enhancement is expected to be possible. Despite the large values, the enhancement does not necessarily translate into large values of the internal quantum efficiency (IQE) and does not imply that the IQE could exceed unity (100%).

Fig. 7 shows the variation of the approximate maximal luminescence enhancement (taken at $\lambda \sim 540$ nm) as a function of the QW position. The maximal enhancement decreases dramatically as the distance between the grating and the QW ($D_{\text{QW}}$) is increased, from 2.8 at $D_{\text{QW}} = 1$ nm to around 0.7 when $D_{\text{QW}} > 100$ nm. For enhancements below 1, the silver grating is detrimental to the luminescence due to the added absorption. The strong enhancement from SP, which is consistent with reported values in literature, $^{9,10}$ justifies the strong interest in the physical properties of SPs. With further optimization of the structure and the materials, a much larger enhancement is expected to be possible.

### D. Plasmonic losses

One of the most important but least studied factors in the surface plasmon enhanced light-emitting structures is the additional loss introduced by the metallic layers. In this

![](./images/813175835753185281_9.jpg)

FIG. 7. The variation of the maximal enhancement factor as a function of the QW position for TM polarization.

subsection, we investigate the magnitude of the plasmonic losses and the efficiency of scattering in the presence of planar (ungrated) and grated silver layers. To quantitatively characterize these features, we show in Figs. 8(a) and 8(b) the angle-resolved net energy flux (field intensity) propagating in the z-direction through a plane between the QW and the silver layer, for the ungrated metallic and grated metallic structures of Fig. 1 and for a 17 nm Ag layer. In Figs. 8(a) and 8(b), positive values of intensity above the QW denote that power flows towards the silver layer, i.e., power is absorbed, transmitted (only within the light cone), or outscattered by the silver layer. Negative values of intensity mean that power flows towards the QW, i.e., the silver layer

![](./images/813175835753185281_10.jpg)

FIG. 8. Angle-resolved field intensity in the GaN barrier between the QW and the Ag layer for (a) the ungrated metallic structure and (b) the grated metallic structure, for a 17 nm Ag layer. (c) The absorption losses in the silver layer given by $(P_{\text{GaN}} - P_{\text{air}})/P_{\text{GaN}}$ for both the grated metallic and ungrated metallic structures, as a function of wavelength, and for 17 nm and 35 nm Ag layer thicknesses. In this case, $P_{\text{GaN}}$ is the total intensity above the QW plane, and $P_{\text{air}}$ is the total output intensity outside the grating (in air). The results are for TM polarization.

generates light to these modes, which is only possible if in-scattering of light from the other modes takes place. Fig. 8(a) shows that propagation towards the silver is strongly favored for different $K$ values corresponding to the guided and SP modes. The energy flux related to the plasmonic modes is several orders of magnitude larger than the flux in the light cone, and power flow is always towards the silver. In Fig. 8(b), the scattering by the grating dramatically changes the power flow. In the plasmonic modes, the power still flows towards the silver layer. However, part of the power is scattered into the light cone and results in net power flowing downwards towards the QW as indicated by the large negative values of Fig. 8(b) for $K$ values (within the light cone) corresponding to the scattered plasmonic mode at $\lambda>530$ nm. In the light cone, the negative values also indicate a large in-scattering of the plasmons into radiative modes. This naturally also implies that the scattering to the light cone of modes propagating upwards from the grating is increased, as shown in Fig. 5(b). While the downwards scattered power in the light cone does not contribute directly to the enhancement, a large fraction of this power could be extracted through the bottom of the structure or even through the top surface if a mirror is placed at the bottom of the sapphire substrate, since the single-pass absorption of the QW is small.

To summarize the effect of the losses, Fig. 8(c) shows the absorption loss given by $L R=\left(P_{\mathrm{GaN}}-P_{\text {air }}\right) / P_{\mathrm{GaN}}$ as a function of wavelength and for 17 nm and 35 nm Ag layer thicknesses; in this case, $P_{\mathrm{GaN}}$ is the total net energy flux in the GaN barrier (above the QW), and $P_{\text {air }}$ is the (output) total energy flux in air. Fig. 8(c) shows that only a fraction of the net power flowing towards the grating escapes to the light cone. For a 17 nm Ag layer, 93% of the light is lost in the silver layer in the ungrated structure while the losses are reduced to 77% in the grated structure, for $\lambda \sim 540$ nm where the scattering and SP interactions are strongest. These figures correspond to a (maximum) light extraction efficiency of 7% and 23% for the light emitted towards the silver layer, respectively. The emission downwards from the QW is not accounted for in these figures, but since the layers below the QW are not absorbing, there are no losses associated with the net power propagating downwards. The observed reduction in the losses shows that while the losses may be a significant obstacle for plasmon enhanced light emission, careful engineering could allow reducing the losses to the level where the benefits outweigh the increased losses. It is interesting to point out that by doubling the silver thickness to 35 nm, the losses are more significant giving lower extraction efficiency; 98% of the light is lost in the silver layer in the ungrated structure while the losses are reduced to slightly below 95% in the grated structure, for $\lambda \sim 490$ nm.

## E. Convergence of the electric field recursive equation

As indicated in Sec. II, the scattered fields are calculated from Eq. (5) by considering the terms up to $n=3$ in the recursive solution. To investigate the accuracy of the low order approximations, we show in Fig. 9 a typical example of the reflectometry profiles for wavelength $\lambda=570$ nm for $n=\{0,1,2,3\}$. For the selected wavelength, the field is coupled to a strong surface plasmonic mode. As can be seen, the first-order (first-born) approximation is roughly midway between orders $n=0$ and $n=2$ while the difference between the second- and third-order terms is already extremely small. This shows that in our case, order $n=2$ is in general sufficiently accurate for detailed studies and using order $n=3$ does not significantly improve the accuracy. In addition, the main features of the curves do not vary significantly from the first to the third-order approximations so that even order $n=1$ can be used for a quick inspection of the structures with satisfactory qualitative insight.

![](./images/813175835753185281_11.jpg)

FIG. 9. Reflectivity as a function of the angle for different recursion depths of Eq. (5), for TM polarization and a wavelength of 570 nm. The curve is a 1D profile taken from Fig. 4(b).

As demonstrated in this paper, the FED method enables (i) detailed insight into the physics as it provides simple analytical approximations, (ii) direct calculation of the emission enhancement, and (iii) direct accounting for the modal broadening by the losses and mode-mixing by the grating. Therefore, the FED approach is expected to have several benefits over other well-established modeling techniques, such as the finite-difference time-domain (FDTD) method or the rigorous coupled-wave analysis (RCWA) method. The main disadvantage of the FDTD method is that, as a fully numerical method, it provides limited physical insight compared to analytical or semi-analytical methods such as RCWA and FED. The RCWA method on the other hand has two main disadvantages compared to FED. First, fully accounting for losses or emission in RCWA is less straightforward than in FED, where these effects are inherently accounted for. Second, RCWA becomes increasingly complex in 2D lossy (and therefore non-periodic) structures whereas FED is expected to give good approximations when the recursive solution discussed in this work is used. A common limitation of all the mentioned methods is that they do not directly describe stimulated emission. However, in the studied structures this is not an important limitation because reaching inversion under typical experimental conditions is not likely due to the very fast recombination rates in the plasmonically enhanced QW.

## IV. CONCLUSION

We developed and studied a first principles method based on Maxwell's equations and fluctuational electrody- namics. The method is used to describe the interactions of optical fields, plasmons, and light emission in multilayer structures involving metallic gratings that can be used to enhance light extraction from GaN light-emitting devices. We demonstrated how the method allows detailed investiga- tion of optical properties, such as the reflectivity, lumines- cence, and plasmonic losses in grated multilayer structures. The presented work explains in detail the origin of the inter- ference patterns experimentally observed in GaN light- emitting structures involving periodic silver gratings and how the scattering of optical modes by the grating can result in decreased optical losses and in the enhancement of the emission from a quantum well located in the vicinity of a grated metallic surface. In general, the exact figures for the emission enhancement and the optical losses due to the absorption by the metallic grating depend on material and other practical factors. For the studied test structure, the emission is enhanced approximately by a factor of up to three, but the metal layer also introduces a significant optical loss that can absorb up to 93% of the optical power traveling towards this layer. However, the optical loss can be reduced to $\sim 75\%$ by the grating, and one can assume that with a care ful choice of the geometry and the material composition of the photonic nanostructures, much higher luminescence enhancement and lower losses are achievable, paving the way for practical plasmon-enhanced LEDs.

## ACKNOWLEDGMENTS

The work was in part supported by the Academy of Finland and the Aalto energy efficiency research programme (AEF). We would like to thank Professor Joel Bellessa from Université Lyon 1 for useful discussions.

$^{1}$ C. Bonnand, J. Bellessa, C. Symonds, and J. C. Plenet, Appl. Phys. Lett. 89, 231119 (2006).
$^{2}$ C. Bonnand, J. Bellessa, and J. C. Plenet, J. Non-Cryst. Solids 352, 1683 (2006).
$^{3}$ V. J. Sorger and X. Zhang, Science 333, 709 (2011).
$^{4}$ K. Tanaka, E. Plum, J. Y. Ou, T. Uchino, and N. I. Zheludev, Phys. Rev. Lett. 105, 227403 (2010).
$^{5}$ R. F. Oulton, V. J. Sorger, T. Zentgraf, R.-M. Ma, C. Gladden, L. Dai, G. Bartal, and X. Zhang, Nature 461, 629 (2009).
$^{6}$ J. M. Pitarke, V. M. Silkin, E. V. Chulkov, and P. M. Echenique, Rep. Prog. Phys. 70, 1 (2007).
$^{7}$ W. L. Barnes, A. Dereux, and T. W. Ebbesen, Nature 424, 824 (2003).
$^{8}$ D.-M. Yeh, C.-F. Huang, C.-Y. Chen, Y.-C. Lu, and C. C. Yang, Nanotechnology 19, 345201 (2008).
$^{9}$ K. Okamoto, I. Niki, A. Shvartser, Y. Narukawa, T. Mukai, and A. Scherer, Nature Mater. 3, 601 (2004).
$^{10}$ D. M. Yeh, C. F. Huang, C. Y. Chen, Y.-C. Lu, and C. C. Yang, Appl. Phys. Lett. 91, 171103 (2007).
$^{11}$ K.-C. Shen, C.-Y. Chen, C.-F. Huang, J.-Y. Wang, Y.-C. Lu, Y.-W. Kiang, C. C. Yang, and Y.-J. Yang, Appl. Phys. Lett. 92, 013108 (2008).
$^{12}$ K.-C. Shen, C.-Y. Chen, H.-L. Chen, C.-F. Huang, Y.-W. Kiang, C. C. Yang, and Y.-J. Yang, Appl. Phys. Lett. 93, 231111 (2008).
$^{13}$ J. Henson, E. Dimakis, J. DiMaria, R. Li, S. Minissale, L. D. Negro, T. D. Moustakas, and R. Paiella, Opt. Express 18, 21322 (2010).
$^{14}$ J. Henson, J. DiMaria, E. Dimakis, T. D. Moustakas, and R. Paiella, Opt. Lett. 37, 79 (2012).
$^{15}$ E. Homeyer, P. Mattila, J. Oksanen, T. Sadi, H. Nykänen, S. Suihkonen, C. Symonds, J. Tulkki, F. Tuomisto, M. Sopenan, and J. Bellessa, Appl. Phys. Lett. 102, 081110 (2013).
$^{16}$ T. Sadi, J. Oksanen, J. Tulkki, P. Mattila, and J. Bellessa, IEEE J. Sel. Top. Quantum Electron. 19, 7800209 (2013).
$^{17}$ G. Sun, J. B. Khurgin, and R. A. Soref, Appl. Phys. Lett. 90, 111107 (2007).
$^{18}$ S. M. Rytov, Sov. Phys. JETP 6, 130 (1958).
$^{19}$ S. M. Rytov, Y. A. Kravtsov, and V. I. Tatarskii, Principles of Statistical Radiophysics III: Elements of Random Fields (Springer-Verlag, 1987).
$^{20}$ J. E. Sipe, J. Opt. Soc. Am. B 4, 481 (1987).
$^{21}$ K. Joulain, R. Carminati, J.-P. Mulet, and J.-J. Greffet, Phys. Rev. B 68, 245405 (2003).
$^{22}$ B. Gallinet, A. M. Kern, and O. J. F. Martin, J. Opt. Soc. Am. A 27, 2261 (2010).
$^{23}$ S. G. Johnson, M. L. Povinelli, P. Bienstman, M. Skorobogatiy, E. L. M. Soljačić, M. Ibanescu, and J. D. Joannopoulos, in Proceedings of 2003 5th International Conference on Transparent Optical Networks (2003), pp. 103–109.
$^{24}$ Z. M. Zhang, Nano/Microscale Heat Transfer (McGraw-Hill, 2007).
$^{25}$ D. Polder and M. V. Hove, Phys. Rev. B 4, 3303 (1971).
$^{26}$ M. Francoeur and M. P. Mengüç, J. Quant. Spectrosc. Radiat. Transf. 109, 280 (2008).
$^{27}$ M. M. Y. Leung, A. B. Djurišić, and E. H. Li, J. Appl. Phys. 84, 6312 (1998).
$^{28}$ D. W. Lynch and W. R. Hunter, Handbook of Optical Constants of Solids, edited by E. D. Palik (Academic Press, 1985).
$^{29}$ S. H. Park, D. Ahn, and S. L. Chuang, IEEE J. Quantum Electron. 43, 1175 (2007).
$^{30}$ E. Yablonovitch, J. Opt. Soc. Am. 72, 899 (1982).
$^{31}$ O. Heikkilä, J. Oksanen, and J. Tulkki, Appl. Phys. Lett. 99, 161110 (2011).
$^{32}$ O. Heikkilä, J. Oksanen, and J. Tulkki, Appl. Phys. Lett. 102, 111111 (2013).