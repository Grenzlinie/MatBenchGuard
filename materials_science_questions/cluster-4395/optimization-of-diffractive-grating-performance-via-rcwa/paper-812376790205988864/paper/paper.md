# Optimal Design of 1-D Photonic Band-Gap Devices by Using the Leaky Mode Propagation Method

Agostino Giorgio, Anna Gina Perri, Mario N. Armenise
Politecnico di Bari; Via Re David 200, 70126 Bari, Italy
Phone +39 – 80 - 5963492 Fax: +39 – 80 – 5963315; e-mail: armenise@poliba.it

## ABSTRACT
A model based on the Leaky Mode Propagation Method has been implemented in a computer program to design 1-D waveguiding Photonic Band-Gap (PBG) devices.

A complete analysis of the propagation characteristics, including the determination of modal propagation constants, electromagnetic field harmonics and total field distribution, transmission and reflection coefficients, total forward and backward power flow in the structure, guided and radiated power, and total losses, can be determined in a few seconds, so enabling the optimized design.

The design of a PBG filter and of a resonant device have been carried out to demonstrate the easy of use of our model.

**Keywords**: Photonic Band-Gap, optical filter, modelling and design

## 1. INTRODUCTION
PBG structures are of considerable interest for their strongly dispersive and wavelength-selective properties [1]. The design of spectral filters, wavelength-division multiplexers, microresonators, switches, and other devices based on PBG structures has been proposed for telecommunication applications [1-3].

To model Bulk PBG (BPBG) configurations a number of algorithms were proposed, such as the Plane Wave expansion Method (PWM) [4], the Transfer Matrix Method (TMM) [5], the Finite Difference Time Domain (FDTD) method [2], and the Bloch Wave Method (BWM) [6].

The waveguiding PBG configuration shown in Fig. 1, where a transversal resonance condition is created for the light, seems to be of great inteterst for a wide range of applications.

![](./images/812376790205988864_1.jpg)

Figure 1 – 3-D view of the basic WPBG structure.

The main issues in the modelling of WPBG devices are represented by the radiation loss at the interfaces between the sandwiched layers and by a great number of numerical problems arising when very deep grooves in the etched layer and a rather strong refractive index contrast among the structure layers occurs.

In this paper we pay attention to a fully general one-dimensional multilayer WPBG configuration (Fig. 1), due to both the great interest stirred up because of its potential for realization of novel optical devices and the possibility of deriving the operation conditions also for Traversing etched Waveguide PBG (TWPBG) configurations [7] (i.e. structures having the grating etched down to substrate).

Materials and Devices for Photonic Circuits II, Mario N. Armenise, Editor,
Proceedings of SPIE Vol. 4453 (2001) © 2001 SPIE · 0277-786X/01/$15.00

The analogy between the electronic band structure and the photonic band structure allows the BWM mixed with the TMM be commonly used to determine the photonic band structure of BPBG, by using the Bloch theorem. Unfortunately, to model PBG devices with the BWM, a number of approximations are made due to the use of the TMM; besides, the assumption of a normal incidence of the laser beam is generally made [8].

To overcome these severe limitations, numerical models are available based on different algorithms such as the FDTD method and the Bi-directional mode Expansion and Propagation (BEP) method [9].

In particular, the FDTD method is a direct discretization of Maxwell's differential equations and it allows the determination of the electromagnetic field time evolution, without any a priori assumptions on the solution form. However, in practical implementations, there may be some limitations on the number of spatial dimensions and on the materials to be modeled. The FDTD requires a number of calculations proportional to the product of the total number of discrete points in the space and the number of time steps. The distance between adjacent points in space should be of the order of 1/10 of the wavelength or smaller, and the time step should be almost equal to the spatial interval divided by the speed of light, resulting in at least 10 time steps per period of the electromagnetic wave.

The BEP method was demonstrated to be accurate and useful to analyze structures having deep perturbation. The perturbed waveguide is considered as a sequence of two waveguide sections: the groove section and the original unetched waveguiding layer (including the input and output waveguide sections). Then, Maxwell's equations are solved in these longitudinally uniform waveguide sections and for each section the propagation constants and mode distribution functions are obtained. The solutions in each uniform section are coupled by using the transfer matrix technique. The BEP method requires a number of matrix operations and inversions for each grating period; therefore, care must be taken in conditioning the matrices to avoid numerical instabilities. Moreover, a complete characterization of devices such those in Fig.1 by using the BEP method requires a large amount of calculations to evaluate the radiation losses, power flow and the other figures of merit associated with the field distribution.

Therefore, rigorous and accurate numerical models result, in general, in a large time consumption and difficult implementation. They also show significant difficulty in obtaining physical insight since they do not allow a quick look at the physical behaviour of the structure. Furthermore, numerical instabilities can occur, depending on the specific structure considered.

To avoid both the disadvantages due to the rigorous numerical methods and the limitations due to the BWM we have already proposed a new and very powerful model of the WPBG and TWPBG based on the Leaky Mode Propagation (LMP) method [10, 11]. The model is based also on the Bloch theorem but, differently from the BWM, the field propagating into the structure is expressed by using a Floquet space harmonic expansion which is valid for any section. Also, all the main loss mechanisms are taken into account. The model allows to determine both the permitted modes propagating into the structure, and the not allowed modes, whose propagation constant is in the band gap. These last modes are viewed as leaky modes that vanishes in a distance related to the dominant loss mechanism that cause the bandgap.

The model theory is inherently accurate and does not require any a priori assumption.

We can investigate the propagating characteristics of a 1-D WPBG or TWPBG (with finite-length, finite-thickness and without any top-cladding layer and waveguiding layer structure) by taking into account also the radiation loss.

On the whole, the LMP method is faster than other accurate numerical methods, does not introduce any analytical approximations and represents a powerful method to understand how critical is the influence of all physical and geometrical parameters on the structure performance.

The LMP method has been implemented in a very fast code able to provide all the parameter values in a few seconds. Then, our computer program is able to carry out very quickly both spectral analysis and investigation of the structure behaviour depending on the technological parameters. Because of the accuracy and quickness our code is well oriented to the design optimization of WPBG and TWPBG devices.

In this paper the code has been applied to design some PBG devices for filtering applications.

In Section 2 an overview on the mathematical formulation of the model is given; in Section 3 results of the design of two PBG devices are given. The first is an air bridge GaAs WPBG filter design based on the principle of shaping the band-gap spectrum, and having the aim of reducing the radiation loss. The second device is a TWPBG resonator and we will demonstrate the capability of our model to determine the resonance condition to optimize the design. Final remarks and conclusions are in Section 4.

## 2. MODEL DESCRIPTION

Referring to the structure in Fig.1, we assume: i) an arbitrary profile of the periodic perturbation with period $\Lambda$ and length L; ii) isotropic and homogeneous unperturbed layers; iii) a finite length along the z propagation direction and infinite length

along y direction.

It is a general 1-D PBG structure having a top-cladding layer placed on a planar waveguide with a different refraction index, and both, the PBG structure and slab waveguide are enclosed between a cover and a substrate. This structure can be easily transformed into a 1-D TWPBG, by eliminating the top-cladding and the guiding layer under the etched region, i.e. the core is etched down to the substrate.

A rectangular etching profile is typically considered for such structures but the model we have developed allows in principle any shape i.e. sinusoidal, triangular, and more generally trapezoidal, to be chosen.

The procedure followed to develop the model equations is divided in two main steps. In the first step, we have determined the complex propagation constants and the field amplitudes of the Bloch-Floquet modes, for both TE and TM polarizations, in infinitely long WPBG and TWPBG structures. To impose the appropriate continuity conditions at the interface between the different layers, we have adopted the harmonic expansion also in the homogeneous layers.

Then, we have modelled the finite-length structures and we have calculated the reflection and transmission coefficients by using a linear combination of two linearly independent solutions obtained in the first step and by imposing the field continuity conditions at the sections z = 0 and z = L (see Fig. 1).

In the model definition we consider the discrete Fourier transform of the permittivity function, ε(x,z), to facilitate the mathematical development of the model itself.

The transversal field solution of the scalar wave equation in the homogeneous layers is formally assumed as follows:

$$
\mathrm{F}^{(\mathrm{o})}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}} \mathrm{C}_{\mathrm{n}}{ }^{(+)} \exp \left(\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{o})} \mathrm{x}\right) \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \quad \mathrm{x} \geq \mathrm{t}_{\mathrm{g}} \tag{1a}
$$

$$
\mathrm{F}^{(\mathrm{r})}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}}\left(\mathrm{B}_{\mathrm{n}}{ }^{(-)} \exp \left(-\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{r})} \mathrm{x}\right)+\mathrm{B}_{\mathrm{n}}{ }^{(+)} \exp \left(\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{r})} \mathrm{x}\right)\right) \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \quad -\mathrm{t}_{\mathrm{r}} \leq \mathrm{x} \leq 0 \tag{1b}
$$

$$
\mathrm{F}^{(\mathrm{f})}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}}\left\lfloor\mathrm{A}_{\mathrm{n}}{ }^{(-)} \exp \left(-\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{f})} \mathrm{x}\right)+\mathrm{A}_{\mathrm{n}}{ }^{(+)} \exp \left(\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{f})} \mathrm{x}\right)\right\rfloor \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \quad -\mathrm{t}_{\mathrm{f}}-\mathrm{t}_{\mathrm{r}} \leq \mathrm{x} \leq-\mathrm{t}_{\mathrm{r}} \tag{1c}
$$

$$
\mathrm{F}^{(\mathrm{s})}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}} \mathrm{D}_{\mathrm{n}}{ }^{(-)} \exp \left(-\mathrm{jk}_{\mathrm{xn}}^{(\mathrm{s})} \mathrm{x}\right) \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \quad \mathrm{x} \leq-\mathrm{t}_{\mathrm{f}}-\mathrm{t}_{\mathrm{r}} \tag{1d}
$$

where $\mathrm{C}_{\mathrm{n}}{ }^{(+)}, \mathrm{B}_{\mathrm{n}}{ }^{(-)}, \mathrm{B}_{\mathrm{n}}{ }^{(+)}, \mathrm{A}_{\mathrm{n}}{ }^{(-)}, \mathrm{A}_{\mathrm{n}}{ }^{(+)}, \mathrm{D}_{\mathrm{n}}{ }^{(-)}$, are amplitude coefficients and $\mathrm{k}_{\mathrm{xn}}^{(\mathrm{i})}$ and $\mathrm{k}_{\mathrm{zn}}$ are the wave-vector components along x and z direction, respectively, of the $\mathrm{n}^{\text {th }}$ harmonic $(\mathrm{n}=0, \pm 1, \pm 2, \pm 3 \ldots$.). Moreover, $\mathrm{F}^{(\mathrm{i})}(\mathrm{x}, \mathrm{z})$ is the appropriate electromagnetic field component (i.e. $\mathrm{E}_{\mathrm{y}}$ for TE and $\mathrm{H}_{\mathrm{y}}$ for TM polarization), in the generic i-th homogeneous layer (i designates the generic homogeneous layer, i.e. i = o, r, f, s respectively for cover, top-cladding, waveguiding and substrate layer); j means $\sqrt{ }-1$ and $\mathrm{n}_{\mathrm{i}}$ is the refractive index of the i-th layer.

Moreover, being $\mathrm{k}_{0}$ the free space wave number, it is:

$$
\left[\mathrm{k}_{\mathrm{xn}}^{(\mathrm{i})}\right]^{2}+\mathrm{k}_{\mathrm{zn}}^{2}=\left[\mathrm{k}^{(\mathrm{i})}\right]^{2}=\mathrm{k}_{\mathrm{o}}^{2} \mathrm{n}_{\mathrm{i}}^{2} \tag{2}
$$

The wave equation in the perturbed region has the following solution, obtained according to the Floquet space harmonic expansion:

$$
\mathrm{F}_{\mathrm{PBG}}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}} \mathrm{f}_{\mathrm{n}}(\mathrm{x}) \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \tag{3a}
$$

$$
0 \leq \mathrm{x} \leq \mathrm{t}_{\mathrm{g}}
$$

$$
\mathrm{G}_{\mathrm{PBG}}(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{n}} \mathrm{g}_{\mathrm{n}}(\mathrm{x}) \exp \left(\mathrm{jk}_{\mathrm{zn}} \mathrm{z}\right) \tag{3b}
$$

where: $\mathrm{F}_{\mathrm{PBG}}$ is the transversal field component (i.e. $\mathrm{E}_{\mathrm{y}} / \mathrm{H}_{\mathrm{y}}$ for TE/TM modes respectively), whose n-th harmonic is $\mathrm{f}_{\mathrm{n}}(\mathrm{x})$, an appropriate function of the depth x; $\mathrm{G}_{\mathrm{PBG}}$ is the longitudinal field component (i.e. $\mathrm{H}_{\mathrm{z}} / \mathrm{E}_{\mathrm{z}}$ for TE/TM modes respectively) and $\mathrm{g}_{\mathrm{n}}(\mathrm{x})$ is the n-th harmonic.

The n-th $\mathrm{k}_{\mathrm{zn}}$ component of the wave vector is related to $\mathrm{k}_{\mathrm{z} 0}$, corresponding to the n=0 fundamental harmonic, by the Bloch-Floquet phase relationship:

$$
\mathrm{k}_{\mathrm{zn}}=\mathrm{k}_{\mathrm{z} 0}+\frac{2 \mathrm{n} \pi}{\Lambda} \tag{4}
$$

The optical losses occurring in the infinitely long structure are taken into account by defining a complex value for $\mathrm{k}_{\mathrm{zn}}$, i.e.

$$
\mathrm{k}_{\mathrm{zn}}=\beta_{\mathrm{o}}+2 \mathrm{n} \pi / \Lambda+\mathrm{j} \alpha=\beta_{\mathrm{n}}+\mathrm{j} \alpha
$$

where $\alpha(>0)$ is the mode amplitude attenuation constant, and $\beta_{\mathrm{n}}=\beta_{\mathrm{o}}+2 \mathrm{n} \pi / \Lambda$

Therefore we can write:

$$
\mathrm{k}_{\mathrm{xn}}^{(\mathrm{i})}= \pm \sqrt{\mathrm{k}^{(\mathrm{i}) 2}-\mathrm{k}_{\mathrm{zn}}^{2}}= \pm \sqrt{\mathrm{k}^{(\mathrm{i}) 2}-\left(\beta_{0}+\frac{2 \mathrm{n} \pi}{\Lambda}+\mathrm{j} \alpha\right)^{2}}=\mathrm{k}_{\mathrm{xn}}^{(\mathrm{i})}=\operatorname{Re}\left(\mathrm{k}_{\mathrm{xn}}\right)+\mathrm{j} \operatorname{Im}\left(\mathrm{k}_{\mathrm{xn}}\right)
$$

where $\mathrm{k}_{\mathrm{xn}}{ }^{(\mathrm{i})}$ can assume either positive or negative imaginary (Im) part, depending on n. In fact the square-root sign in Eq. (6) must be selected to satisfy the following condition [12], [13]:
$$
\operatorname{Im}\left(\mathrm{k}_{\mathrm{xn}}\right)>0 \text { for } \beta_{\mathrm{n}}>0 \text { or } \operatorname{Im}\left(\mathrm{k}_{\mathrm{xn}}\right)<0 \text { for } \beta_{\mathrm{n}}<0
$$

Because of the complex nature of $\mathrm{k}_{\mathrm{xn}}{ }^{(\mathrm{i})}$, guided waves in periodic structures behave like leaky waves since some power is scattered out of the guiding layer.
$\alpha$ takes into account two main mechanisms of loss: Bragg reflection and power radiation. When a finite-length structure has to be considered, the out-of-plane losses $\mathrm{L}_{\mathrm{p}}$ are evaluated as due to the scattering effect at the vertical interfaces. It results:
$$
\mathrm{L}_{\mathrm{p}}=1-\mathrm{R}_{\mathrm{p}}-\mathrm{T}_{\mathrm{p}}
$$
being $\mathrm{R}_{\mathrm{p}}$ and $\mathrm{T}_{\mathrm{p}}$ the reflection and transmission coefficients, respectively.

We have derived the differential equations to be solved to evaluate the electromagnetic field distribution in the structure by using the initial values obtained by imposing the boundary conditions at each interface between layers. Therefore, by substituting Eqs. (3a-b) into Maxwell's equations we obtain two separate partial differential equation systems for TE and TM polarizations that can be also expressed in a matrix form:

$$
\frac{\mathrm{dF}}{\mathrm{dx}}=\mathbf{M} \cdot \mathbf{F}
$$

where: $\mathbf{M}=\left(\begin{array}{ll}\mathbf{0} & \mathbf{Q} \\ \mathbf{P} & \mathbf{0}\end{array}\right) ; \quad \mathbf{F}=\left(\begin{array}{l}\mathbf{f} \\ \mathbf{g}\end{array}\right) ; \quad \frac{\mathrm{dF}}{\mathrm{dx}}=\left(\begin{array}{l}\frac{\mathrm{df}}{\mathrm{dx}} \\ \frac{\mathrm{dg}}{\mathrm{dx}}\end{array}\right)$

being $\mathbf{f}, \mathbf{g}, \mathrm{df} / \mathrm{dx}, \mathrm{dg} / \mathrm{dx}$ column vectors whose elements are the field harmonics; $\mathbf{P}$ and $\mathbf{Q}$ are matrices depending on $\mathrm{x}$ whose elements are:

$$
\left.\begin{array}{l}
\mathrm{p}_{\mathrm{mn}}(\mathrm{x})=\mathrm{j} \omega \varepsilon_{\mathrm{o}}\left[\left(\frac{\mathrm{k}_{\mathrm{zn}}}{\mathrm{k}_{\mathrm{o}}}\right)^{2} \delta_{\mathrm{mn}}-\varepsilon_{\mathrm{m}-\mathrm{n}}(\mathrm{x})\right] \\
\mathrm{q}_{\mathrm{mn}}(\mathrm{x})=-\mathrm{j} \omega \mu_{\mathrm{o}} \delta_{\mathrm{mn}}
\end{array}\right\} \quad \text { for TE modes }
$$

$$
\left.\begin{array}{l}
\mathrm{p}_{\mathrm{mn}}(\mathrm{x})=\mathrm{j} \omega \mu_{\mathrm{o}}\left[\delta_{\mathrm{mn}}-\left(\frac{\mathrm{k}_{\mathrm{zn}} \mathrm{k}_{\mathrm{zn}}}{\mathrm{k}_{\mathrm{o}}^{2}}\right) \cdot \xi_{\mathrm{m}-\mathrm{n}}(\mathrm{x})\right] \\
\mathrm{q}_{\mathrm{mn}}(\mathrm{x})=\mathrm{j} \omega \varepsilon_{\mathrm{o}} \xi_{\mathrm{m}-\mathrm{n}}(\mathrm{x})
\end{array}\right\} \quad \text { for TM modes }
$$

where $\delta_{\mathrm{mn}}$ is the Dirac delta function, $\varepsilon^{(\mathrm{i})}=\mathrm{n}^{(\mathrm{i}) 2}$ is the relative permittivity for each i-th homogeneous layer. In the perturbed region we use the Fourier series development of the permittivity function:

$$
\varepsilon(\mathrm{x}, \mathrm{z})=\sum_{\mathrm{l}} \varepsilon_{\mathrm{l}}(\mathrm{x}) \exp \left(\mathrm{j} \frac{2 \pi \mathrm{lz}}{\Lambda}\right)
\tag{10}
$$

where l denotes the space harmonic order, and also the Fourier series development of $1/\varepsilon$

$$
[\varepsilon(\mathrm{x}, \mathrm{z})]^{-1}=\sum_{\mathrm{l}} \xi_{\mathrm{l}}(\mathrm{x}) \exp \left(\mathrm{j} \frac{2 \pi \mathrm{lz}}{\Lambda}\right)
\tag{11}
$$

l and n can assume either positive or negative values ranging from $-\propto$ to $+\propto$. Moreover, the position m = n - l applies.
By solving a determinantal equation to get no trivial solutions for the differential equation system (7), we obtain the complex propagation constant $(\beta_0 + j\alpha)$. The remaining propagation constants are related to the fundamental one, $\beta_0$, through the Floquet theorem (see Eq. 5).
Once the complex constants are determined, the amplitude of each harmonic, i.e. the vector $\mathbf{f}(0)$, for the $\mathrm{E_y}$ (TE) or $\mathrm{H_y}$ (TM) field component in the PBG region, is derived.
Also $\mathbf{g}(0)$, $\mathbf{f}(\mathrm{t_g})$ and $\mathbf{g}(\mathrm{t_g})$ can be calculated, together with the amplitude and phase of all harmonics in each homogeneous layer.
In addition to mode propagation constants, harmonics and total field distribution, transmission and reflection coefficients, Poynting vector, forward and backward power flow, guided power and total losses (i.e. the mode amplitude attenuation constant, the radiated power, the angle of radiation and the radiation efficiency in the cover and substrate), for both TE and TM modes can also be evaluated by our model, to fully characterize the structure.
The power calculations are performed by determining and integrating the Poynting vector in each layer. We can determine the total forward and backward power flow by distinguishing the forward and backward field.
The angle of radiation with respect to the x - axis, for each radiating harmonic in the cover, $\vartheta_n^{(cover)}$, and in the substrate, $\vartheta_n^{(substrate)}$, is calculated once the propagation constants and the transverse eigenvalues of the radiating harmonics are determined
The cover (substrate) radiation efficiency is simply obtained as the ratio of the power radiated in the cover (substrate) and the total radiated power.
A key point of the model is the approach to evaluate the reflection and transmission coefficients, that can be determined once complex propagation constants and field amplitudes and phases have been calculated.
We have developed a general model of transmittivity and reflectivity, useful for both WPBG and TWPBG, accounting for any arbitrary number of field harmonics.
It should be remembered that the structure has a finite-length and, also, that the continuity conditions at the vertical boundaries at positions z = 0 and z = L have to be imposed. An incident field $\mathrm{F_{inc}}$ at the position z = 0 generates a reflected field $\mathrm{F_{ref}}$ at the z = 0 position, and a transmitted field $\mathrm{F_{tr}}$ at z = L (see Fig.1).
Due to the mirror-like simmetry of the infinitely long structure with respect to the x-axis the propagating characteristics of the structure along the +z and -z direction the solution of Maxwell's equations can be expressed as a linear combination of two linearly independent solutions by means of arbitrary coefficients, $\mathrm{c_1}$ and $\mathrm{c_2}$. The first solution is assumed to be:

$$
\mathrm{F}^{+}=\sum_{\mathrm{n}} \mathrm{f}_{\mathrm{n}}(\mathrm{x}) \exp (\mathrm{jk}_{\mathrm{zn}} \mathrm{z}) \quad \text { ("a" solution) }
\tag{12}
$$

that is a "forward" solution, named "a" solution. As second solution we assume:

$$
\mathrm{F}^{-}=\sum_{\mathrm{n}} \mathrm{f}_{\mathrm{n}}(\mathrm{x}) \exp (-\mathrm{jk}_{\mathrm{zn}} \mathrm{z}) \quad \text { ("b" solution) }
\tag{13}
$$

that is a backward one, named "b" solution.
Since n ranges from $-\propto$ to $+\propto$, $\mathrm{k_{zn}}$ can be either positive or negative and, then, genuinely forward and backward harmonics exist for both "a" and "b" solutions. Therefore, the total forward traveling field is:

$$
\mathrm{F}_{\mathrm{a}}=\mathrm{c}_{1} * \mathrm{F}_{\mathrm{Ta}}+\mathrm{c}_{2} * \mathrm{F}_{\mathrm{Tb}}
\tag{14}
$$

where $\mathrm{F_{Ta}}$ denotes the contribution to the forward traveling field, due to the "a" solution, and $\mathrm{F_{Tb}}$ denotes the contribution to the forward traveling field, due to the "b" solution. The total backward traveling field is:

$$\mathrm{F}_{\mathrm{b}}=\mathrm{c}_{1} * \mathrm{F}_{\mathrm{Ra}}+\mathrm{c}_{2} * \mathrm{F}_{\mathrm{Rb}} \tag{15}$$

where $\mathrm{F}_{\mathrm{Ra}}$ denotes the contribution to the backward traveling field due to the "a" solution and $\mathrm{F}_{\mathrm{Rb}}$ the contribution to the backward traveling field due to the "b" solution. Then, we obtain:

$$\mathrm{F}=\mathrm{F}_{\mathrm{a}}+\mathrm{F}_{\mathrm{b}}=\mathrm{c}_{1} * \mathrm{F}_{\mathrm{Ta}}+\mathrm{c}_{2} * \mathrm{F}_{\mathrm{Tb}}+\mathrm{c}_{1} * \mathrm{F}_{\mathrm{Ra}}+\mathrm{c}_{2} * \mathrm{F}_{\mathrm{Rb}} \tag{16}$$

The field propagating in the slab waveguides at the boundary sections is:

$$\mathrm{F}_{\mathrm{inc}}=\mathrm{F}_{\mathrm{slab}}(\mathrm{x}) \exp \left(\mathrm{j} \beta_{\mathrm{slab}} \mathrm{z}\right) \tag{17}$$

$$\mathrm{F}_{\mathrm{ref}}=\rho \mathrm{F}_{\mathrm{slab}}(\mathrm{x}) \exp \left(-\mathrm{j} \beta_{\mathrm{slab}} \mathrm{z}\right) \tag{18}$$

$$\mathrm{F}_{\mathrm{tr}}=\tau \mathrm{F}_{\mathrm{slab}}(\mathrm{x}) \exp \left(\mathrm{j} \beta_{\mathrm{slab}} \mathrm{z}\right) \tag{19}$$

where: $\mathrm{F}_{\text{slab}}(\mathrm{x})$ and $\beta_{\text{slab}}$ are the field amplitude and the propagation constant of the propagating mode in the input/output multilayer slab waveguide, respectively; $\rho$ and $\tau$ are the field transmission and reflection coefficients, respectively.
The continuity conditions applied at $z=0$ and $z=L$ provide the following linear system in four unknowns: $c_{1}, c_{2}, \rho$ and $\tau$ which allows to obtain the modal reflection coefficient $\mathrm{R}_{\mathrm{P}}=|\rho|^{2}$ and the modal transmission coefficient $\mathrm{T}_{\mathrm{P}}=|\tau|^{2}$. The obtained system is:

$$
\begin{cases}
\mathrm{F}_{\text {slab }}(\mathrm{x})=\left.\mathrm{c}_{1} \mathrm{F}_{\mathrm{Ta}}\right|_{\mathrm{z}=0}+\left.\mathrm{c}_{2} \mathrm{F}_{\mathrm{Tb}}\right|_{\mathrm{z}=0} \tag{20a} \\
\varrho \mathrm{F}_{\text {slab }}(\mathrm{x})=\left.\mathrm{c}_{1} \mathrm{F}_{\mathrm{Ra}}\right|_{\mathrm{z}=0}+\left.\mathrm{c}_{2} \mathrm{F}_{\mathrm{Rb}}\right|_{\mathrm{z}=0} \tag{20b}
\end{cases}
\quad \text{for } z=0
$$

$$
\begin{cases}
\tau \mathrm{F}_{\text {slab }}(\mathrm{x}) \exp \left(\mathrm{j} \beta_{\text {slab }} \mathrm{L}\right)=\left.\mathrm{c}_{1} \mathrm{F}_{\mathrm{Ta}}\right|_{\mathrm{z}=\mathrm{L}}+\left.\mathrm{c}_{2} \mathrm{F}_{\mathrm{Tb}}\right|_{\mathrm{z}=\mathrm{L}} \tag{20c} \\
\left.\mathrm{c}_{1} \mathrm{F}_{\mathrm{Ra}}\right|_{\mathrm{z}=\mathrm{L}}+\left.\mathrm{c}_{2} \mathrm{F}_{\mathrm{Rb}}\right|_{\mathrm{z}=\mathrm{L}}=0 \tag{20d}
\end{cases}
\quad \text{for } z=L
$$

To conclude this section we observe that our approach possesses such an intrinsic flexibility that it can be extended also to model cascaded structures, i.e. gratings separated by slab waveguides, which can be considered as a single device having irregularities in the periodicity of the grating.

A computer program in FORTRAN 77 language has been implemented on a 500 MHz PC; it performs all calculations to completely characterize the structure in a few seconds (about 5s). An analysis scanning a range of 100 operating wavelengths is completed in a few minutes (4 to 5 min).

### 3. DESIGN OF WPBG AND TWPBG DEVICES

To compare our model with the existing literature we have analysed a structure which has been investigated in Ref. [12].
The results are in good agreement with those calculated in [12] by using a vectorial model, the maximum percentage relative difference being of $0.01 \%$ in the $\beta_{\mathrm{n}}$ calculation and $0.1 \%$ in the $\alpha$ calculation, for both TE and TM modes.
Moreover, a maximum percentage relative error of $1.9 \%$ (for WPBG structure) and $0.3 \%$ (for TWPBG structure), in the band gap determination was found comparing calculations performed by our model with the BEP algorithm.

After the comparison the model, the code has been used to design some 1-D WPBG devices.

First of all we would like to design a filter having a transmission band around $\lambda=1.55 \mu \mathrm{m}$ with negligible radiation loss.

There are three main principles of optical filtering corresponding to three main approaches to design filters.
The first approach lies in shaping the photonic band structure of the device in order to obtain one or more pass-bands between two or more stop-bands [8]. The design must be optimized by accounting for Fabry-Perot like round-trips that gives oscillations in the pass-band. These oscillations must be reduced in order to avoid the presence of ripples in the transmission coefficient spectrum.
The second approach is based on the resonance principle: the device must be designed to filter a single wavelength. Details are given later in this section.
The third approach to obtain a filtering effect is to introduce a defect, i.e. an irregularity, in the periodicity of the structure.
The model allows all the three design techniques to be adopted although in this paper we refer to the first and to the second one, starting by the first.
In order to enlarge the stop-band, and then making as narrow as possible the pass-band, a high index contrast must be used, and then, we choose the GaAs as material having a refractive index n equal to 3.7. Moreover, to obtain the alternative presence of pass-band and stop-band a ridge-type device should be considered [8]. Then, we choose the WPBG structure as in Fig. 1. The substrate is generally fabricated with $Al_xGa_{1-x}As$ having n > 3.5 depending on the value of x. This means that high radiation losses we will expect by such a structure. To overcome this inconvenience we have designed an air-bridge configuration, i.e. a filter having air as a cover and as a substrate. The characteristics are those in Table I

Table I - Parameters of the WPBG GaAs air-bridge filter.

<table>
  <tr>
    <td>$n_c$</td>
    <td>1</td>
  </tr>
  <tr>
    <td>$n_r$</td>
    <td>3.7</td>
  </tr>
  <tr>
    <td>$n_f$</td>
    <td>3.7</td>
  </tr>
  <tr>
    <td>$n_s$</td>
    <td>1.</td>
  </tr>
  <tr>
    <td>$t_r [\mu m]$</td>
    <td>0.00</td>
  </tr>
  <tr>
    <td>$t_f [\mu m]$</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>$t_g [\mu m]$</td>
    <td>0.25</td>
  </tr>
  <tr>
    <td>$\Lambda [\mu m]$</td>
    <td>0.25</td>
  </tr>
</table>

In Fig. 2 are drown the $\alpha$ and $R_p$ spectra ($\alpha$ is expressed in $\mu m^{-1}$).

![](./images/812376790205988864_2.jpg)

Figure 2 – $\alpha$ vs $\lambda$ and $R_p$ vs l for the air bridge GaAs filter on WPBG.

The best L value to obtain a drop of $R_p$ at $\lambda = 1.55$ $\mu m$ is L = 20 $\Lambda$. This implies a number of periods N = 20. In fact, for N < 20 we obtain a reduction of Fabry-Perot oscillations in the transmission band, but also the $R_p$ values are higher.
Calculations show that no radiation occurs in the considered range of operating wavelength, due to the particular air-bridge configuration considered.
We have also simulated the same filter realized in Si (n = 3.45), having a period $\Lambda = 0.28$ $\mu m$ and we have found a quite larger pass-band perfectly centered around $\lambda = 1.55$ $\mu m$. This confirms the importance of the index contrast to widen the

stop-band.

The second designed device is a resonator based on the TWPBG structure.

The aim of the design is to find a device structure giving the exact resonance condition at $\lambda = 1.55$ $\mu$m. This time, we choose a Si on glass structure, etched down to substrate.

The resonance condition implies that the Bloch wave group velocity in the guiding plane, i.e. in the direction parallel to the substrate, vanishes. These Bloch waves are then stationary modes. Being the group velocity given by $\mathbf{v}_g = 
abla\omega(\mathbf{k})$, it is oriented normal to the curves in the $\omega$ vs k diagram, in the direction of increasing frequencies. Then, the propagation constants of the resonant Bloch modes are placed on a maximum or a minimum point of the band structure (Brillouin diagram). The resonant modes having a zero group velocity in the direction parallel to the substrate are fully confined within the etched layer. These modes will interact very strongly with a dipole of the correct (resonant) frequency if it is incorporated into the waveguide. At the resonant frequency, spontaneous emission will be enhanced and low threshold highly efficient lasing can be achieved.

A number of simulations shows that the larger is the etched region, the higher is the period of the structure useful to achieve the resonance condition. Therefore, in order to reduce the device lenght, i.e. the device period, we choose that $d_2 = 0.8\ \Lambda$.

By the Brillouin diagram shown in Fig. 3 we notice the circled points as resonant Bloch modes. The modes whose propagation constants lie on dashed bands are excited by the zero-th order mode propagating into the input slab waveguide. The others are excited by the first order mode.

![](./images/812376790205988864_3.jpg)

Figure 3 – Brillouin diagram relevant to the Bloch modes excited by the zero-th order mode (dashed line) and first order mode (bold faced line) of the input coupling waveguide. The circles indicate the resonant Bloch modes.

We assume a resonance condition in corrispondence of the Q point, at $\lambda = 1.55$ $\mu$m. This means $\Lambda = 0.249$ $\mu$m.

The designed device has the parameters reported in Table II. Fig. 4 shows the $\alpha$ vs $\Lambda$ diagram, confirming that for the designed period there is the band-gap edge and the losses drop to zero.

Table II – Parameters of the resonant device.

<table>
  <tr>
    <th>$n_c$</th>
    <td>1</td>
  </tr>
  <tr>
    <th>$n_r$</th>
    <td>3.45</td>
  </tr>
  <tr>
    <th>$n_s$</th>
    <td>1.57</td>
  </tr>
  <tr>
    <th>$t_g\ [\mu\text{m}]$</th>
    <td>0.375</td>
  </tr>
  <tr>
    <th>$L\ [\mu\text{m}]$</th>
    <td>5.0</td>
  </tr>
  <tr>
    <th>$\Lambda\ [\mu\text{m}]$</th>
    <td>0.249</td>
  </tr>
</table>

![](./images/812376790205988864_4.jpg)

Figure 4 – $\alpha$ vs $\Lambda$ diagram for the TWPBG resonator. The dashed line is relevant to the modes excited by the zero-th order mode propagating into the input slab waveguide; the other graph is relevant to the mode excited by the first order mode propagating into the input slab waveguide.

The same conclusion raises observing the $R_p$ spectrum shown in Fig. 5 in which a sudden drop in corrispondence of $\lambda = 1.55\ \mu$m occurs.

![](./images/812376790205988864_5.jpg)

Figure 5 – $R_p$ vs $\lambda$ for the designed resonant TWPBG device in Table II.

Fig. 6 show the field distribution into the structure at resonance.

![](./images/812376790205988864_6.jpg)

Figure 6 - Propagation of resonant frequency Bloch mode.

It can be observed that the field is concentrated in the high refraction index regions, as we expect having choosen the resonance mode in the lower band edge. Moreover, it is clear that the field propagates into the PBG region, as the resonance condition requires.

## 4. CONCLUSIONS
In the paper a new, very fast and accurate model based on the Floquet theorem for the analysis of waveguide 1-D PBG devices has been described and used to design two PBG devices.
A GaAs WPBG filter, having an air bridge configuration, was designed and simulated. The filter has no radiation losses and a very narrow pass-band was obtained between two stop-bands for the operating wavelength $\lambda=1.55\ \mu$m.
Moreover, a resonant, Si on glass, TWPBG device has been designed to obtain the resonance condition at the operating wavelength $\lambda=1.55\ \mu$m. The design was performed by the Brillouin diagram and by the $\alpha$ vs $\Lambda$ diagram.
The model allows the evaluation of all propagating characteristics of a fully general multilayer 1-D waveguiding PBG structure, i.e.: mode propagation constants, harmonics and total field distribution, transmission coefficient, reflection coefficient, total forward and backward power flow, guided power flow, total losses including: mode amplitude attenuation constant, out-of-plane losses, radiated power, radiation angle and radiation efficiency both in the cover and substrate.
Also, fast and accurate determination of the bandgap position is allowed. Gratings with arbitrary profiles and finite length can be investigated. Traversing etched configurations can also be simulated and designed.
The code has been implemented in FORTRAN 77 language on a 500 MHz PC. One hundred simulations are performed in a few minutes.
The main advantages of the model are the absence of any a priori assumptions and approximations, the quickness and stability of the numerical convergence, and the large amount of information and figures of merit it allows to determine in a few seconds. The real behaviour of PBG devices can be succesfully predicted by our model which enables the designer to have a complete view of the physical and geometrical device features, and to draw very easily design rules for optimizing the waveguide PBG device design.

## REFERENCES
[1] E. Yablonovitch, "Photonic Band Gap structures", *Optical Society of America B*, vol. 10, no. 2, pp. 283-295, Feb. 1993.
[2] R. Ziolkowsky, M. Tanaka, "FDTD analysis of PBG waveguides, power splitters and switches", *Opt. and Quant. Elect.*, vol 31, pp. 843-855, 1999.
[3] F. Yang, R. Coccioli, Y. Qian, T. Itoh, "Planar PBG structures: basic properties and applications", *IEICE Tran. on*

Electronics, vol. E83, n. 5, pp. 687-695, May 2000.

[4] K. Sakoda, "Transmittance and Bragg reflectivity of two dimensional photonic lattices", *Phys. Review B*, pp. 8992-9002, Sept. 1995.

[5] J. B. Pendry, "Calculating Photonic Band structure", *Journal of Physics Condensed Matter*, vol. 8, n. 9, pp. 1085-1108, 1996.

[6] P. Sk. Russell, T. Birks, D. Lucas, *Confined Electrons and Photons*, New York: Plenum Press, 1995, pp. 585-633.

[7] D. Atkin, P. Sk. Russell, T. Birks, "Photonic band structure of guided Bloch modes in high index films fully etched through with periodic microstructures", *Journal of Modern Optics*, vol. 43, n. 5, pp. 1035-1053, 1996.

[8] C. F. Lam, R. B. Vrijen, P. P. L. Chang-Chien, D. F. Sievenpiper, E. Yablonovitch, "A Tunable Wavelength Demultiplexer Using Logarithmic Filter Chains", *IEEE - OSA Journal of Lightwave Technology*, vol. 16, no. 19, September 1998.

[9] J. Ctyroky, S. Pregla, "Analysis of a deep waveguide Bragg grating", *Optical and Quantum Electronics*, vol. 30, pp. 343-358, 1998.

[10] A. Giorgio, A. G. Perri, M. N. Armenise, " Fast Modelling of Deeply and Fully Etched Gratings Based on the Bloch-Floquet Theorem ", to be published on *International Journal of Numerical Modelling*.

[11] A. Giorgio, A. G. Perri, M. N. Armenise, "Modelling Waveguiding Photonic Band-Gap Structures by Leaky Mode Propagation Method", to be published on *Electronics Letters*.

[12] C. S. Peng, T. Tamir, H. L. Bertoni, "Theory of periodic dielectric waveguides", *IEEE Trans. on MTT*, vol. MTT-23, no.1, pp. 123-133, 1975.

[13] R. E. Collins, F. J. Zucker, *Antenna Theory*, New York: McGraw-Hill, 1969, sec. 19.10, p. 203.