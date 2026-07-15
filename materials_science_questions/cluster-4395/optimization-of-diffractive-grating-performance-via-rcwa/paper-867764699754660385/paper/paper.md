# Coupled Optoelectronic Simulation and Optimization of Thin-Film Photovoltaic Solar Cells

Tom H. Anderson, Benjamin J. Civiletti, Peter B. Monk

University of Delaware, Department of Mathematical Sciences, Newark, DE 19716, USA Akhlesh Lakhtakia
Pennsylvania State University, Department of Engineering Science and Mechanics, University Park, PA
16802, USA

## Abstract

A design tool was formulated for optimizing the efficiency of inorganic, thin-film, photovoltaic solar cells. The solar cell can have multiple semiconductor layers in addition to antireflection coatings, passi- vation layers, and buffer layers. The solar cell is backed by a metallic grating which is periodic along a fixed direction. The rigorous coupled-wave approach is used to calculate the electron-hole-pair generation rate. The hybridizable discontinuous Galerkin method is used to solve the drift-diffusion equations that govern charge-carrier transport in the semiconductor layers. The chief output is the solar-cell efficiency which is maximized using the differential evolution algorithm to determine the optimal dimensions and bandgaps of the semiconductor layers.

## 1 Introduction

The simulation of thin-film photovoltaic solar cells requires the coupling of (i) an optical model capable of capturing the absorption of photons with (ii) an electrical model capable of simulating the transport of charge carriers throughout the solar cell [1, 2]. To optimize solar cell designs, both models needed to be tailored to be rapidly computable, accurate, and robust across the relevant parameter space. To this end, we have developed a coupled optoelectronic simulation technique for thin-film photovoltaic solar cells containing periodic structures, and we have used this simulation technique together with the differential evolution algorithm (DEA) [3, 4] to optimize device performance.

The solar cell is assumed to be infinitely extended in the $xy$-plane, periodic in the $x$-direction, translation invariant in the $y$-direction, and of finite extent in the $z$-direction. These assumptions allow the simulation to be limited to two-dimensional (2D) space. However, we emphasize that our approach will work in three- dimensional (3D) space at the cost of greater computational complexity and cost.

The first step of the coupled optoelectronic simulation involves modeling the photonic characteristics of the solar cell. In the photonic step, the rigorous coupled-wave approach (RCWA) [5, 6, 7] is used to determine the electromagnetic fields in the solar cell due to incident solar radiation. The RCWA is an efficient computational technique to solve the frequency-domain Maxwell equations and determine the electric field in a representative subsection of the periodic (2D or 3D) domain. The frequency-domain electric field is used to determine the photon absorption rate, and therefore the generation rate of electron-hole pairs, throughout the solar cell. Rapid calculation across the solar spectrum [8, 9] is possible due to RCWA being a pseudo-spectral method, i.e., it avoids spatial meshing in the periodic dimensions.

The second step of the coupled optoelectronic simulation involves modeling the electronic characteristics of the solar cell. In the electronic step, the electron-hole-pair generation rate is used as the input to a drift- diffusion electronic (DDE) model in order to calculate the current-voltage curve of the solar cell and, hence, the efficiency of the solar cell. Because of the cost of solving the DDE model, we average the generation rate across one period in the $xy$-plane and implement the DDE model for variations of the electric potential and charge-carrier transport along the $z$-axis. The resulting one-dimensional (1D) DDE model consists of six coupled differential equations. The nonlinear Shockley-Read-Hall, Auger, and radiative terms are included to model electron-hole recombination [1, 2]. A hybridizable discontinuous Galerkin (HDG) method [10, 11, 12, 13] is developed, and the Newton-Raphson method [14] is used to find a solution of the resulting nonlinear system.

A version of the HDG method has already been used to simulate organic solar cells [10], based on the work of Lehrenfeld [11]. We use a similar scheme based on the classical HDG method [12], following Fu *et al.* [13] who have analyzed the method for a linear convection-diffusion system. Our study points to the

advantages of this method in simulating inorganic solar cells having a spatially variable electron-hole-pair generation rate in the presence of semiconductor heterojunctions.

Anderson et al. [15] recently reported a coupled optoelectronic simulation of a Schottky-barrier thin-film solar cell, with the finite-element method (FEM) [16] used for both the photonic and the electronic steps of the simulation. Later, Anderson et al. [17] used the RCWA for the photonic step and the standard FEM for the electronic step for simulating the same Schottky-barrier thin-film solar cell (which is not considered in this paper). Other researchers have also developed techniques for optoelectronic simulation [18, 19, 20].

Our emphasis in this paper is different in two ways: first, our simulations lead to optimization of thin-film photovoltaic solar cells containing periodic structures; second, we concentrate on understanding the numerical performance of each of the two steps in the coupled optoelectronic simulation. For example, we investigate the convergence rate of RCWA for two model problems. We also propose, test, and use a high-order HDG scheme using fifth-degree polynomials for the DDE model, quite possibly the first time that such a high-order scheme has been used. Since the use of DEA for optimization of solar cells has been investigated elsewhere by us [8, 17], we devote little space to it in this paper.

The photonic and electronic steps described in this paper are closely related to components of the Solcore software package described recently by Alonso-Álvarez et al. [20]. That software package includes an RCWA solver as well as a 1D DD solver based on quasi-Fermi levels. In contrast, our DD solver uses the density of holes and electrons and is based on a high-order HDG scheme.

The ultimate goal is to maximize the efficiency of the solar cell, and this goal distinguishes our work from that of Alonso-Álvarez et al. [20]. Because of the presence of local minima, we use the DEA [3, 4] for optimization. This requires the evaluation of the efficiency of solar-cell designs from all regions of the multi-dimensional space encompassing appropriate parameters, which thus necessitates the development of a robust and efficient solver. See https://www.pvlighthouse.com.au for a list of other available photovoltaic-design software. Our work here should be seen as a complement to those efforts by extending the use of coupled optoelectronic simulation to the optimal design of solar cells as well as testing new simulation techniques.

In this paper, we assume that the solar cell occupies the region
$$
\mathcal{X}:\{\underline{r} \equiv(x, y, z) \mid-\infty<x<\infty,-\infty<y<\infty,-L_{\mathrm{m}}<z<L_{\mathrm{t}}\}
\tag{1}
$$
in $\mathbb{R}^{3}$, with air occupying the region $\mathbb{R}^{3} \backslash \mathcal{X}$. As stated previously, the device is assumed to be periodic along the $x$-direction with period $L_{\mathrm{x}}$ and translation invariant along the $y$-direction. Solely for illustrating various simulation issues, we performed calculations for the device shown Fig. 1(a). The current-generating region of this device comprises a thin layer of $p$-type semiconductor, a thicker layer of $i$-type semiconductor, and a thin layer of $n$-type semiconductor [1,2]. The plane $z=0$ is taken to be the bottom face of the $n$-type semiconductor and the plane $z=L_{\mathrm{z}}$ is taken to be the top face of the $p$-type semiconductor. Below the plane $z=0$ is a grating formed by infinitely long strips of a metal and a dielectric material, the grating period being $L_{\mathrm{x}}$. Below the grating is a metal layer that is sufficiently thick to prevent light from escaping into air below it. Above the $p$-type semiconductor is an antireflection coating. The plane $z=L_{\mathrm{t}}$ is the top face of the antireflection coating and the plane $z=-L_{\mathrm{m}}$ is the bottom face of the metal layer below the grating. The grating shape in Fig. 1(a) is an academic example. A triangular grating used to test RCWA is shown in Fig. 1(b).

The layout of the paper is as follows. In Section 2, we start by describing the optical model solved in the photonic step, summarize the 2D RCWA, and define the charge-carrier generation rate that is used as the input to the DDE model solved in the electronic step. In Section 2.2 we show two examples of RCWA convergence to illustrate the advantages and drawbacks of this approach for solar cells. Section 3 is devoted to the electronic step. The DDE model is described in Section 3.1. The boundary conditions derived from local quasi-thermal equilibrium (LQTE) are discussed in Section 3.2, while the electron-hole recombination terms are presented in Section 3.3. We discuss heterojunctions in Section 3.4, and summarize a non-dimensionalized DDE model in Section 3.5. Then we proceed to describe the HDG method in Section 4, starting with the formulation of a generalized transport system in Section 4.1, followed by the discretization of 1D space (along the $z$ axis) in Section 4.2 and implementational aspects of the convection term in Section 4.3. Next, in Section 4.4, we present the upwinding strategy needed to stabilize the DDE model, followed in Section 4.5 by the interpolation method for implementing the non-linear recombination terms. The implementation of jump conditions is presented in Section 4.6. The numerical model is completed by discussing the homotopy (or continuation) method for solving the nonlinear system in Section 4.7. A numerical test is presented in

![](./images/867764699754660385_1.jpg)

Figure 1: (a) An academic model of a metal-backed $p$-$i$-$n$ solar cell used as an example throughout this paper. The dimensions shown are simply for illustration. (b) A triangular metal grating in air used to test RCWA (of course, this is not a solar cell). Figures are not to scale.

Section 5. Together, the photonic and electronic steps provide information used by the DEA optimization scheme, which is described briefly in Section 6. The paper culminates in a presentation of results for the model solar cell presented in Fig. 1(a). We end with some conclusions in Section 8.

A note about notation: Underlined quantities represent vectors, with $\hat{\underline{x}}$, $\hat{\underline{y}}$ and $\hat{\underline{z}}$ being the unit vectors along the $x$-, $y$-, and $z$-axes. The $\check{}$ mark is used to denote quantities emerging from the implementation of the spatial Fourier transform [21] with respect to $x$. For the frequency-domain calculations carried out in the photonic step (Section 2), electromagnetic fields are taken to vary with time $t$ harmonically as $\exp(-i\omega t)$, where $\omega$ is the angular frequency and $i = \sqrt{-1}$. Air is assumed to have the same electromagnetic properties as free space or vacuum. The wavenumber in air is denoted by $k_0 = \omega/c_0$ where $c_0$ is the speed of light in air, and $\lambda_0 = 2\pi/k_0$ is the wavelength of light in air. The permittivity and permeability of free space are denoted, respectively, by $\varepsilon_0 = 8.854188 \times 10^{-12}$ F m$^{-1}$ and $\mu_0 = 4\pi \times 10^{-7}$ H m$^{-1}$, and $\eta_0 = \sqrt{\mu_0/\varepsilon_0}$ is the intrinsic impedance of free space.

## 2 Photonic Step

In this section, first we summarize the RCWA for solving the frequency-domain Maxwell equations, and then we present some numerical results to quantify the performance of RCWA, which is the workhorse for computational investigations of optical gratings [22, 23]. The adequacy of this approach for solar cells has been established by comparison to other approaches [24, 25, 26]. Oddly, the numerical convergence of this method has not been investigated before; hence, a part of this section is devoted to a numerical investigation of RCWA convergence.

### 2.1 RCWA Formulation

The solar cell is taken to be illuminated from the half space $z > L_{\text{t}}$ by a normally incident plane wave whose electric field phasor is denoted by

$$
\underline{E}_{\text{inc}}(x, z, \lambda_0) = E_0 \frac{a_{\text{p}} \hat{\underline{x}} + a_{\text{s}} \hat{\underline{y}}}{\sqrt{a_{\text{p}}^2 + a_{\text{s}}^2}} \exp(-i k_0 z). \tag{2}
$$

The parameters $a_{\mathrm{s}}$ and $a_{\mathrm{p}}$ determine the polarization state of the incident light; thus, $a_{\mathrm{p}} = 1$ and $a_{\mathrm{s}} = 0$ for $p$-polarized light, but $a_{\mathrm{s}} = 1$ and $a_{\mathrm{p}} = 0$ for $s$-polarized light. For solar-cell calculations, we set $a_{\mathrm{p}} = a_{\mathrm{s}} = 1$ because direct sunlight can be assumed to be unpolarized.

Due to the periodicity of the solar cell in the $x$-direction, the optical relative permittivity $\varepsilon_{\mathrm{rel}}(x, z, \lambda_0)$ is represented everywhere by the Fourier series

$$
\varepsilon_{\mathrm{rel}}(x, z, \lambda_0) = \sum_{\ell=-\infty}^{\infty} \varepsilon_{\mathrm{rel}}^{(\ell)}(z, \lambda_0) \exp\left(i\kappa^{(\ell)}x\right), \quad |z| < \infty, \quad |x| < \infty,
\tag{3}
$$

where $\varepsilon_{\mathrm{rel}}^{(\ell)}(z, \lambda_0)$ are Fourier coefficients and $\kappa^{(\ell)} = 2\pi\ell/L_{\mathrm{x}}$.In a similar way, the optical relative impermittivity $\beta_{\mathrm{rel}}(x, z, \lambda_0) = 1/\varepsilon_{\mathrm{rel}}(x, z, \lambda_0)$ is repesented everywhere by the Fourier series

$$
\beta_{\mathrm{rel}}(x, z, \lambda_0) = \sum_{\ell=-\infty}^{\infty} \beta_{\mathrm{rel}}^{(\ell)}(z, \lambda_0) \exp\left(i\kappa^{(\ell)}x\right), \quad |z| < \infty, \quad |x| < \infty,
\tag{4}
$$

where $\beta_{\mathrm{rel}}^{(\ell)}(z, \lambda_0)$ are Fourier coefficients. We can also express the $x$-dependences of the electric and magnetic field phasors by their Fourier series as

$$
\underline{E}(x, z, \lambda_0) = \sum_{\ell=-\infty}^{\infty} \underline{e}^{(\ell)}(z, \lambda_0) \exp\left(i\kappa^{(\ell)}x\right), \quad |z| < \infty, \quad |x| < \infty,
\tag{5}
$$

$$
\underline{H}(x, z, \lambda_0) = \sum_{\ell=-\infty}^{\infty} \underline{h}^{(\ell)}(z, \lambda_0) \exp\left(i\kappa^{(\ell)}x\right), \quad |z| < \infty, \quad |x| < \infty,
\tag{6}
$$

where $\underline{e}^{(\ell)} \equiv e_x^{(\ell)}\hat{\underline{x}} + e_y^{(\ell)}\hat{\underline{y}} + e_z^{(\ell)}\hat{\underline{z}}$ and $\underline{h}^{(\ell)} \equiv h_x^{(\ell)}\hat{\underline{x}} + h_y^{(\ell)}\hat{\underline{y}} + h_z^{(\ell)}\hat{\underline{z}}$ are Fourier coefficients and normal incidence is implicit.

For computational tractability, all four of the foregoing series are truncated to include only $\ell \in \{-N_{\mathrm{t}}, ..., N_{\mathrm{t}}\}$, $N_{\mathrm{t}} \geq 0$. The Fourier coefficients are collected in the $(2N_{\mathrm{t}}+1)$-column vectors

$$
\breve{\varepsilon}_{\mathrm{rel}}(z, \lambda_0) = \left[\varepsilon_{\mathrm{rel}}^{(-N_{\mathrm{t}})}(z, \lambda_0), \varepsilon_{\mathrm{rel}}^{(-N_{\mathrm{t}}+1)}(z, \lambda_0), ..., \varepsilon_{\mathrm{rel}}^{(N_{\mathrm{t}}-1)}(z, \lambda_0), \varepsilon_{\mathrm{rel}}^{(N_{\mathrm{t}})}(z, \lambda_0)\right]^T,
\tag{7}
$$

$$
\breve{\beta}_{\mathrm{rel}}(z, \lambda_0) = \left[\beta_{\mathrm{rel}}^{(-N_{\mathrm{t}})}(z, \lambda_0), \beta_{\mathrm{rel}}^{(-N_{\mathrm{t}}+1)}(z, \lambda_0), ..., \beta_{\mathrm{rel}}^{(N_{\mathrm{t}}-1)}(z, \lambda_0), \beta_{\mathrm{rel}}^{(N_{\mathrm{t}})}(z, \lambda_0)\right]^T,
\tag{8}
$$

$$
\breve{e}_{\sigma}(z, \lambda_0) = \left[e_{\sigma}^{(-N_{\mathrm{t}})}(z, \lambda_0), e_{\sigma}^{(-N_{\mathrm{t}}+1)}(z, \lambda_0), ..., e_{\sigma}^{(N_{\mathrm{t}}-1)}(z, \lambda_0), e_{\sigma}^{(N_{\mathrm{t}})}(z, \lambda_0)\right]^T,
$$
$$
\sigma \in \{x, y, z\},
\tag{9}
$$

$$
\breve{h}_{\sigma}(z, \lambda_0) = \left[h_{\sigma}^{(-N_{\mathrm{t}})}(z, \lambda_0), h_{\sigma}^{(-N_{\mathrm{t}}+1)}(z, \lambda_0), ..., h_{\sigma}^{(N_{\mathrm{t}}-1)}(z, \lambda_0), h_{\sigma}^{(N_{\mathrm{t}})}(z, \lambda_0)\right]^T
$$
$$
\sigma \in \{x, y, z\},
\tag{10}
$$

where the superscript $T$ denotes the transpose. Furthermore, the $(2N_{\mathrm{t}}+1) \times (2N_{\mathrm{t}}+1)$ matrix

$$
\breve{K} = \mathrm{diag}\left[\kappa^{(-N_{\mathrm{t}})}, \kappa^{(-N_{\mathrm{t}}+1)}, ..., \kappa^{(N_{\mathrm{t}}-1)}, \kappa^{(N_{\mathrm{t}})}\right]
\tag{11}
$$

is defined for convenience. Finally, the Toeplitz matrix of the Fourier coefficients $\{\xi^{(\ell)}\}_{\ell=-\infty}^{\infty}$ of a periodic function $\xi(x) = \xi(x \pm L_{\mathrm{x}})$ is defined as

$$
\mathcal{T}_{N_{\mathrm{t}}}(\xi) = \begin{bmatrix}
\xi^{(0)} & \xi^{(-1)} & ... & \xi^{(-2N_{\mathrm{t}}+1)} & \xi^{(-2N_{\mathrm{t}})} \\
\xi^{(1)} & \xi^{(0)} & ... & \xi^{(-2N_{\mathrm{t}}+2)} & \xi^{(-2N_{\mathrm{t}}+1)} \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\xi^{(2N_{\mathrm{t}}-1)} & \xi^{(2N_{\mathrm{t}}-2,\lambda_0)} & ... & \xi^{(0)} & \xi^{(-1)} \\
\xi^{(2N_{\mathrm{t}})} & \xi^{(2N_{\mathrm{t}}-1)} & ... & \xi^{(1)} & \xi^{(0)}
\end{bmatrix}.
\tag{12}
$$


Substitution of the four Fourier series into the frequency-domain Maxwell curl equations yields two matrix ordinary differential equations [7, Sec. 2.3.4]. The equation

$$
\begin{aligned}
& \frac{d}{d z}\left[\begin{array}{l}
\breve{e}_{x}\left(z, \lambda_{0}\right) \\
\breve{h}_{y}\left(z, \lambda_{0}\right)
\end{array}\right]= \\
& i\left[\begin{array}{cc}
\breve{0} & \omega \mu_{0} \breve{I}-\left(\omega \varepsilon_{0}\right)^{-1} \breve{K} \breve{N}\left(z, \lambda_{0}\right) \breve{K} \\
\omega \varepsilon_{0} \breve{M}\left(z, \lambda_{0}\right) & \breve{0}
\end{array}\right]\left[\begin{array}{l}
\breve{e}_{x}\left(z, \lambda_{0}\right) \\
\breve{h}_{y}\left(z, \lambda_{0}\right)
\end{array}\right]
\end{aligned}
\label{eq13} \tag{13}
$$

must be solved if $a_{\mathrm{p}} \neq 0$, and the equation

$$
\begin{aligned}
& \frac{d}{d z}\left[\begin{array}{l}
\breve{e}_{y}\left(z, \lambda_{0}\right) \\
\breve{h}_{x}\left(z, \lambda_{0}\right)
\end{array}\right]= \\
& -i\left[\begin{array}{cc}
\breve{0} & \omega \mu_{0} \breve{I} \\
\omega \varepsilon_{0} \breve{M}\left(z, \lambda_{0}\right)-\left(\omega \mu_{0}\right)^{-1} \breve{K}^{2} & \breve{0}
\end{array}\right]\left[\begin{array}{l}
\breve{e}_{y}\left(z, \lambda_{0}\right) \\
\breve{h}_{x}\left(z, \lambda_{0}\right)
\end{array}\right]
\end{aligned}
\label{eq14} \tag{14}
$$

if $a_{\mathrm{s}} \neq 0$. In these equations, $\breve{0}$ is the $(2 N_{\mathrm{t}}+1) \times(2 N_{\mathrm{t}}+1)$ null matrix, and $\breve{I}$ is the $(2 N_{\mathrm{t}}+1) \times(2 N_{\mathrm{t}}+1)$ identity matrix. As a corollary to the mutual independence of Eqs. (13) and (14), $p$-polarized light does not interact with $s$-polarized light and vice versa.

We solved both Eqs. (13) and (14) because direct sunlight can be assumed to be unpolarized. Thereafter, the Fourier coefficients of the $z$-components of the electric and magnetic field phasors were obtained as

$$
\left.\begin{array}{l}
\breve{e}_{z}\left(z, \lambda_{0}\right)=-\left(\omega \varepsilon_{0}\right)^{-1} \breve{N}\left(z, \lambda_{0}\right) \breve{K} \breve{h}_{y}\left(z, \lambda_{0}\right) \\
\breve{h}_{z}\left(z, \lambda_{0}\right)=\left(\omega \mu_{0}\right)^{-1} \breve{K} \breve{e}_{y}\left(z, \lambda_{0}\right)
\end{array}\right\}.
\label{eq15} \tag{15}
$$

The matrices $\breve{M}$ and $\breve{N}$ in Eqs. (13) and (14) encode the Fourier series provided in Eqs. (3) and (4) for $\varepsilon_{\text {rel }}$ and $\beta_{\text {rel }}$. There are four choices possible for the combination of $\breve{M}$ and $\breve{N}$, the best choice depending on the polarization state of the incident plane wave [27]. Following Lalanne and Morris [5], we first define the Toeplitz matrices

$$
\breve{E}\left(z, \lambda_{0}\right)=\mathcal{T}_{N_{\mathrm{t}}}\left[\breve{\varepsilon}_{\mathrm{rel}}\left(z, \lambda_{0}\right)\right]
\label{eq16} \tag{16}
$$

and

$$
\breve{B}\left(z, \lambda_{0}\right)=\mathcal{T}_{N_{\mathrm{t}}}\left[\breve{\beta}_{\mathrm{rel}}\left(z, \lambda_{0}\right)\right].
\label{eq17} \tag{17}
$$

Then the four possible choices are identified as follows:

Choice 1: The most direct choice is for $\breve{M}$ to encode $\varepsilon_{\text {rel }}$ and $\breve{N}$ to encode $\varepsilon_{\text {rel }}^{-1}$ so that $\breve{M}=\breve{E}$ and $\breve{N}=\breve{B}$.

Choice 2: We can write $\varepsilon_{\text {rel }}=1 / \beta_{\text {rel }}$ and arrive at the choice $\breve{M}=\breve{B}^{-1}$ and $\breve{N}=\breve{B}$.

Choice 3: In contrast to Choice 2, we can write $\beta_{\text {rel }}=1 / \varepsilon_{\text {rel }}$ to choose $\breve{M}=\breve{E}$ and $\breve{N}=\breve{E}^{-1}$.

Choice 4: The final choice is $\breve{M}=\breve{B}^{-1}$ and $\breve{N}=\breve{E}^{-1}$, in direct contrast to Choice 1.

Choices 1 and 3 are identical on the one hand, and Choice 2 is the same as Choice 4 on the other, for $s$-polarized illumination. All four choices are distinct for $p$-polarized illumination.

In order to solve Eqs. (13) and (14), it is usual to discretize in the $z$-direction by subdividing the solar cell into thin slices of infinite extent in the $xy$-plane [7]. In each slice, $\varepsilon_{\text {rel }}$ is uniform in the $z$-direction, but it is either uniform or piecewise uniform in the $x$-direction. Depending on the profile of the grating, this may require piecewise-uniform approximations of $\varepsilon_{\text {rel }}$ and $\beta_{\text {rel }}$. Equations (13) and (14) can then be solved exactly in each slice using a stabilized stepping algorithm [7,23] akin to Gaussian elimination without pivoting [14], so that $\breve{e}_{x}$, $\breve{e}_{y}$ , $\breve{h}_{x}$, and $\breve{h}_{y}$ are determined everywhere in the solar cell. Equations (15) then let us determine $\breve{e}_{z}$ and $\breve{h}_{z}$ throughout the solar cell.


The convergence rates for the Fourier series of $\varepsilon_{\text{rel}}$ and $\beta_{\text{rel}}$ are limited by the discontinuities in the relative permittivity in the slices in the grating region. Additionally, approximating the interfaces of general grating profiles using stairstepping can also give low-order convergence with respect to the slice thickness. However, if the grating is in fact a superposition of a finite number of square waves, the only approximation is due to the truncation of the Fourier series.

### 2.1.1 Electron-Hole-Pair Generation Rate
With the assumption that the absorption of every photon in any semiconductor layer excites an electron-hole pair, the electron-hole-pair generation rate in the semiconductor region $\{|x| < L_x/2, 0 < z < L_z\}$ can be calculated as

$$
G(x, z)=\frac{1}{\hbar c_{0}} \int_{\lambda_{0_{m i n}}}^{\lambda_{0_{m a x}}} \operatorname{Im}\left\{\varepsilon_{\mathrm{rel}}\left(x, z, \lambda_{0}\right)\right\}\left|\frac{\underline{E}\left(x, z, \lambda_{0}\right)}{E_{o}}\right|^{2} S\left(\lambda_{0}\right) \mathrm{d} \lambda_{0}, \tag{18}
$$

where $\hbar$ is the reduced Planck constant and $S(\lambda_0)$ is the incident power spectrum. We chose $S(\lambda_0)$ to be the standard AM1.5G spectrum [28]. As $S(\lambda_0)$ falls off rapidly at shorter free-space wavelengths, $\lambda_{0_{min}} = 350$ nm was fixed. Once the free-space wavelength becomes too large, the energy in a photon is not capable of exciting an electron sufficiently to cross the bandgap. Consequently, the upper cut off was taken to be $\lambda_{0_{max}} = 1240$ nm V/$\text{E}_{\text{g,min}}$, where $\text{E}_{\text{g,min}}$ (in V) is the minimum value of the bandgap $\text{E}_g$ in the solar cell. These choices are typical values for studies on solar cells.

After assuming full quantum efficiency, i.e. each excited electron or hole is collected at the appropriate terminal, the optical short-circuit current density can be calculated as

$$
J_{\mathrm{SC}}^{\mathrm{Opt}}=q_{\mathrm{e}} \frac{1}{L_{x}} \int_{0}^{L_{z}} \int_{-L_{x} / 2}^{L_{x} / 2} G(x, z) \mathrm{d} x \mathrm{~d} z, \tag{19}
$$

where $q_e = 1.60218 \times 10^{-19}$ C is the elementary charge. Let us note that $J_{\text{SC}}^{\text{Opt}}$ provides only a rough benchmark for the device efficiency, although it is often used to assess the efficiency of solar cells [29, 30, 31]. However, as recombination is neglected, $J_{\text{SC}}^{\text{Opt}}$ is necessarily larger than the attainable short-circuit current density $J_{\text{SC}}$, which is the density of current that flows when the solar cell is illuminated and no external bias is applied (i.e., when $V_{\text{ext}} = 0$). We have already shown that, when the bandgap is one of the simulation parameters, optimizing Eq. (19) can lead to designs with high values of $J_{\text{SC}}^{\text{Opt}}$ but low values of extractable electrical power [8]. A better approach is to complement the photonic step by the electronic step, as accomplished in Section 3.

## 2.2 RCWA Convergence
There are two sources of approximation error in the RCWA. The first is the truncation of the Fourier series to include only $\ell \in \{-N_t, ..., N_t\}$, while the second is through the discretization of space in the $z$-direction whenever there is a need to approximate the relative permittivity slice by slice. As it is not possible to solve Eqs. (13) and (14) analytically, in order to investigate the convergence of RCWA, the electric field phasor $\underline{E}(x, z, \lambda_0)$ was calculated using an FEM code [24, 25] and compared with the RCWA results for various values of $N_t$, the slice thickness being fixed at a sufficiently low value.

The FEM data were obtained using an adaptive method implemented in NGSolve [32]. The adaptive algorithm uses mesh bisection and the Zienkiewicz-Zhu *a-posteriori* error estimator [33]. The FEM calculations were carried out using 5th-order continuous finite elements. Mesh adaptivity was terminated whenever the algorithm reached 100,000 degrees of freedom. The simulated domain was sandwiched between two perfectly matched layers (PMLs). Both of the PMLs were taken to be one-wavelength thick and with a constant PML parameter of $(1.5+2.5i)$ [34], the reflection coefficient of the PMLs being then $\sim 3 \times 10^{-12}$.

### 2.2.1 Global Convergence of Electric Field Phasor
In order to investigate the global convergence of the RCWA, a simple but adequate problem was chosen: reflection by the grating shown in Fig. 1(b). The region above the grating was taken to be occupied by air with relative permittivity $\varepsilon_{\text{rel}}=1+10^{-9}i$, the minuscule imaginary part needed for the stability of the RCWA

algorithm. The grating, made from a fictitious metallic material with relative permittivity $\varepsilon_{\text{rel}}=-22+0.4i$, comprises triangular protrusions on a 50-nm-thick film. Each protrusion is of height 50 nm and base 250 nm. Calculations were made with $\lambda_0=600$ nm and $L_{\text{x}}=500$ nm.

The triangular profile was chosen for the grating, because it is approximated by a stairstep when the piecewise-uniform approximation is used to solve Eqs. (13) and (14). In addition, the true solution has a singularity in the field at the tip of the triangle which tests the algorithm's ability to handle such behavior.

As the only non-zero Cartesian component of $\underline{E}(x,z,\lambda_0)$ for $s$-polarized illumination is the $y$-component, a relative global error was defined as

$$
e_{E_{s}}\left(N_{\mathrm{t}}\right)=\frac{\left\|E_{y, R C W A}\left(N_{\mathrm{t}}\right)-E_{y, F E}\right\|_{2}}{\left\|E_{y, F E M}\right\|_{2}}
\tag{20}
$$

as a function of $N_{\mathrm{t}}$, with $E_{y, R C W A}$ denoting the value of $E_y$ yielded by RCWA, and $E_{y, F E M}$ the value yielded by FEM. In addition, for any function $f(x,y)$,

$$
\|f\|_{2}^{2}=\int_{\Omega_{\mathrm{ph}}}|f(x,y)|^{2} \mathrm{d} z \mathrm{~d} x
\tag{21}
$$

and where $\Omega_{\text{ph}}$ is the entire simulation domain in the photonic step except the two PMLs. For $p$-polarized illumination, the relative global error was analogously defined as

$$
e_{E_{p}}\left(N_{\mathrm{t}}\right)=\frac{\sqrt{\left\|E_{x, R C W A}\left(N_{\mathrm{t}}\right)-E_{x, F E M}\right\|_{2}^{2}+\left\|E_{z, R C W A}\left(N_{\mathrm{t}}\right)-E_{z, F E M}\right\|_{2}^{2}}}{\sqrt{\left\|E_{x, F E M}\right\|_{2}^{2}+\left\|E_{z, F E M}\right\|_{2}^{2}}},
\tag{22}
$$

because only the $y$-component of $\underline{E}(x,z,\lambda_0)$ is null valued.

Four different choices of $\left\{\breve{M}, \breve{N}\right\}$, as described after Eq. (17), are possible when implementing the RCWA. Accordingly, four different studies were conducted to investigate the relative global error in the electric field phasor for $s$- and $p$-polarized illuminations.

![](./images/867764699754660385_2.jpg)

Figure 2: Global relative errors (a) $e_{E_{s}}$ and (b) $e_{E_{p}}$ vs. $N_{\mathrm{t}}$ for the simple problem depicted in Fig. 1(b). Choice 1: $\breve{M}=\breve{B}^{-1}$ and $\breve{N}=\breve{E}^{-1}$; Choice 2: $\breve{M}=\breve{B}^{-1}$ and $\breve{N}=\breve{B}$; Choice 3: $\breve{M}=\breve{E}$ and $\breve{N}=\breve{E}^{-1}$; Choice 4: $\breve{M}=\breve{E}$ and $\breve{N}=\breve{B}$. A straight line shows the empirical order of convergence.

Plots of $e_{E_{s}}$ and $e_{E_{p}}$ vs. $N_{\mathrm{t}}$ are presented in Fig. 2 for each of the four choices of $\left\{\breve{M}, \breve{N}\right\}$. For $s$-polarized illumination, the relative global error reduces as $\sim N_{\mathrm{t}}^{-2.1}$ until $N_{\mathrm{t}} \approx 8$ and saturates thereafter in Fig. 2(a), when $\breve{M}=\breve{E}$ (i.e., for Choices 1 and 3). The error saturation may be due to the limited accuracy of the FEM solution and/or due to stairstepping error. In contrast, $e_{E_{s}}$ reduces as $\sim N_{\mathrm{t}}^{-1}$ when $\breve{M}=\breve{B}^{-1}$ (i.e., for Choices 2 and 4). For $p$-polarized illumination, the relative global error decays slower than the reciprocal of $N_{\mathrm{t}}$ in Fig. 2(b), when $\breve{M}=\breve{E}$. The decay is somewhat faster when $\breve{M}=\breve{B}^{-1}$.

These results suggest that for calculating the electric field phasor due to s-polarized illumination, it is advantageous to choose $\breve{M} = \breve{E}$ because that should give second-order convergence to the true solution. For p-polarized illumination, it is preferable to choose $\breve{M} = \breve{B}^{-1}$ and $\breve{N} = \breve{E}^{-1}$, as that should give almost first-order convergence to the true solution even with stairstepping. The choice of Fourier representations for $\{\breve{M}, \breve{N}\}$ thus has a profound effect on the accuracy of the RCWA [5, 27].

### 2.2.2 Convergence of Electric Field Phasor in the Semiconductor Region
Correct calculation of the electric field phasor in the semiconductor region is paramount for photovoltaic solar cells, as is clear from Eq. (18). This motivated the second convergence study using the device in Fig. 1(a).

The chosen device contains a grating made from a representative metal with relative permittivity $\varepsilon_{\text{rel}} = -22 + 0.4i$ and has period $L_{\text{x}} = 500$ nm. The grating comprises rectangular protrusions on a 100-nm-thick film. Each protrusion is of height 50 nm and base 250 nm. The grooves of the grating are entirely filled with a dielectric material with relative permittivity $\varepsilon_{\text{rel}} = 3.33 + 0.016i$. Above this structure lies a 240-nm-thick semiconductor region with relative permittivity $\varepsilon_{\text{rel}} = 9.5 + 1.25i$, which is a representative value for a semiconductor at $\lambda_{0} = 680$ nm. Above this region is a 75-nm-thick layer of a dielectric material with relative permittivity $\varepsilon_{\text{rel}} = 3.33 + 0.016i$, which acts as an anti-reflection coating. The top layer is again air-like, with relative permittivity $\varepsilon_{\text{rel}} = 1 + 10^{-9}i$.

For this study, we used the definition
$$
\|f\|_{2}^{2} = \int_{x=-L_{x}/2}^{L_{x}/2} \int_{z=0}^{L_{z}} |f(x, y)|^{2} \, \mathrm{d}z \, \mathrm{d}x
\tag{23}
$$
in Eqs. (20) and (22). Four different choices of $\{\breve{M}, \breve{N}\}$, as described after Eq. (17), were used in four different studies, whose results are presented in Fig. 3.

![](./images/867764699754660385_3.jpg)

Figure 3: Relative errors (a) $e_{E_{s}}$ and (b) $e_{E_{p}}$ vs. $N_{\text{t}}$ in the semiconductor region of the solar cell depicted in Fig. 1(a). Choice 1: $\breve{M} = \breve{B}^{-1}$ and $\breve{N} = \breve{E}^{-1}$; Choice 2: $\breve{M} = \breve{B}^{-1}$ and $\breve{N} = \breve{B}$; Choice 3: $\breve{M} = \breve{E}$ and $\breve{N} = \breve{E}^{-1}$; Choice 4: $\breve{M} = \breve{E}$ and $\breve{N} = \breve{B}$. A straight line shows the empirical order of convergence.

Convergence rates for the second study are much slower than in the first study. The best observed rates are $O(N_{\text{t}}^{-1.6})$ for s-polarized illumination and $O(N_{\text{t}}^{-0.35})$ for p-polarized illumination. The slower convergence is due to the strong singularities in the solution near the corners of the grating. Those singularities lead to slower convergence of the Fourier series. It should be noted that these same singularities are also observed in the adaptive FEM solution.

Figure 3(a) contains a split in $e_{E_{s}}$ between successive odd and even values of $N_{\text{t}}$, when $\breve{M} = \breve{E}$ and $\breve{N} = \breve{E}^{-1}$ (Choice 3). This split is also present, although less extreme, in an earlier work [5]. It is also

present for $p$-polarized illumination but dramatically reduced, especially when $\breve{M}=\breve{E}$ and $\breve{N}=\breve{B}$ (Choice 1).

Lalanne [6] has already discussed in detail the complex issues behind RCWA convergence. Our contribution is to suggest that stairstepping is not a major cause of error in RCWA, but it is necessary to examine convergence for different grating morphologies. Also, RCWA is reliably convergent for $s$-polarized illumination of solar cells, and provides slower convergence for $p$-polarized illumination. We agree with previous studies [24, 25, 26] that RCWA can provide the accuracy needed for photonics simulations, but our studies also show that the convergence rates can be quite low. With an appropriate choice of parameters we can achieve almost 10% error with $N_{\mathrm{t}}=10$, which became our choice for the optimization study reported in Section 6.

## 3 Electronic Step

Taking into account the size of the features in the solar cell, and under standard assumptions on the electron transport, such as the device being in quasi-thermal equilibrium (QTE), the transport of electrons and holes in semiconductors can be modeled using the drift-diffusion equations [1, 2, 35]. To speed up the calculations, we neglected variations with respect to $x$ and therefore used the 1D electron-hole-pair generation rate

$$
G(z)=\frac{1}{L_{\mathrm{x}}} \int_{-L_{\mathrm{x}} / 2}^{L_{\mathrm{x}} / 2} G(x, z) \mathrm{d} x.
\tag{24}
$$

### 3.1 Drift-Diffusion Electronic Model

The DDE model comprises the following three differential equations holding in the semiconductor region $\Omega_{\mathrm{el}}=\left\{z \mid 0<z<L_{\mathrm{z}}\right\}$:

$$
\frac{d}{d z} J_{\mathrm{n}}(z)=-q_{\mathrm{e}}[G(z)-R(n, p ; z)],
\tag{25}
$$

$$
\frac{d}{d z} J_{\mathrm{p}}(z)=q_{\mathrm{e}}[G(z)-R(n, p ; z)],
\tag{26}
$$

$$
\varepsilon_{0} \frac{d}{d z}\left[\varepsilon_{d c}(z) \frac{d}{d z} \phi(z)\right]=-q_{\mathrm{e}}\left[N_{\mathrm{f}}(z)+p(z)-n(z)\right].
\tag{27}
$$

In these equations, the gradients of the electron current density $J_{n}(z)$, hole current density $J_{\mathrm{p}}(z)$, and electric potential $\phi(z)$ are related to the electron density $n(z)$, hole density $p(z)$, fixed charge (charged traps and doping) density $N_{\mathrm{f}}(z)$, electron-hole-pair generation rate $G(z)$, and electron-hole-pair recombination rate $R(n, p ; z)$. The zero-frequency (dc) relative permittivity is denoted by $\varepsilon_{d c}(z)$.

The two current densities are defined as

$$
J_{\mathrm{n}}(z)=q_{\mathrm{e}} \mu_{\mathrm{n}}(z) n(z) \frac{d}{d z} \mathrm{E}_{\mathrm{F}_{\mathrm{n}}}(z)
\tag{28}
$$

and

$$
J_{\mathrm{p}}(z)=q_{\mathrm{e}} \mu_{\mathrm{p}}(z) p(z) \frac{d}{d z} \mathrm{E}_{\mathrm{F}_{\mathrm{p}}}(z),
\tag{29}
$$

where $\mu_{\mathrm{n}}(z)$ and $\mu_{\mathrm{p}}(z)$ are the electron mobility and hole mobility, respectively;

$$
\mathrm{E}_{\mathrm{F}_{\mathrm{n}}}(z)=\mathrm{E}_{\mathrm{c}}(z)+V_{\mathrm{th}} \ln \left[\frac{n(z)}{N_{\mathrm{c}}(z)}\right]
\tag{30}
$$

is the electron quasi-Fermi level; and

$$
\mathrm{E}_{\mathrm{F}_{\mathrm{p}}}(z)=\mathrm{E}_{\mathrm{v}}(z)-V_{\mathrm{th}} \ln \left[\frac{p(z)}{N_{\mathrm{v}}(z)}\right]
\tag{32}
$$

is the hole quasi-Fermi level. In the expressions for the quasi-Fermi levels, $V_{\mathrm{th}}=k_{\mathrm{B}} T / q_{\mathrm{e}}$ is the thermal voltage of the electrons and holes with $T$ as the temperature and $k_{\mathrm{B}}=1.380649 \times 10^{-23} \mathrm{~J} \mathrm{~K}^{-1}$ as the Boltzmann constant, $N_{\mathrm{c}}(z)$ is the conduction-band density of states, $N_{\mathrm{v}}(z)$ is the valence-band density of states, $\mathrm{E}_{\mathrm{c}}(z)$ is the conduction-band energy, and $\mathrm{E}_{\mathrm{v}}(z)$ is the valence-band energy. The bandgap is defined as

$$
\mathrm{E}_{\mathrm{g}}(z)=\mathrm{E}_{\mathrm{c}}(z)-\mathrm{E}_{\mathrm{v}}(z)
\tag{33}
$$

and the intrinsic energy as

$$
\mathrm{E}_{\mathrm{i}}(z)=\frac{1}{2}\left\{\left[\mathrm{E}_{\mathrm{c}}(z)+\mathrm{E}_{\mathrm{v}}(z)\right]+V_{\mathrm{th}} \ln \left[\frac{N_{\mathrm{v}}(z)}{N_{\mathrm{c}}(z)}\right]\right\}.
\tag{34}
$$

In the Boltzmann approximation [1] the quasi-Fermi levels are assumed to lie far from the edges of the conduction and valence bands. Accordingly,

$$
n(z)=\bar{n}(z) \exp \left[\frac{\mathrm{E}_{\mathrm{F}_{\mathrm{n}}}(z)-\mathrm{E}_{\mathrm{i}}(z)}{V_{\mathrm{th}}}\right]
\tag{35}
$$

and

$$
p(z)=\bar{n}(z) \exp \left[-\frac{\mathrm{E}_{\mathrm{F}_{\mathrm{p}}}(z)-\mathrm{E}_{\mathrm{i}}(z)}{V_{\mathrm{th}}}\right].
\tag{36}
$$

Here, the intrinsic carrier density is given by

$$
\bar{n}(z)=\sqrt{N_{\mathrm{c}}(z) N_{\mathrm{v}}(z) \exp \left[\frac{\mathrm{E}_{\mathrm{g}}(z)}{V_{\mathrm{th}}}\right]}
\tag{37}
$$

and the conduction-band energy is given by

$$
\mathrm{E}_{\mathrm{c}}(z)=\mathrm{E}_{0}-\phi(z)-\chi(z),
\tag{38}
$$

where $\chi(z)$ is the electron affinity of the semiconductor, and the (arbitrary) reference energy level $\mathrm{E}_{0}$ is often chosen as [1]

$$
\mathrm{E}_{0}=\mathrm{E}_{\mathrm{c}}(0)+\phi(0)+\chi(0).
\tag{39}
$$

Equations (28) and (29) may now be simplified to

$$
J_{\mathrm{n}}(z)=-q_{\mathrm{e}} \mu_{\mathrm{n}}(z)\left\{n(z) \frac{d}{d z}\left[\phi(z)+\phi_{\mathrm{n}}(z)\right]-V_{\mathrm{th}} \frac{d}{d z} n(z)\right\}
\tag{40}
$$

and

$$
J_{\mathrm{p}}(z)=-q_{\mathrm{e}} \mu_{\mathrm{p}}(z)\left\{p(z) \frac{d}{d z}\left[\phi(z)+\phi_{\mathrm{p}}(z)\right]+V_{\mathrm{th}} \frac{d}{d z} p(z)\right\},
\tag{41}
$$

respectively. Here,

$$
\phi_{\mathrm{n}}(z)=\chi(z)+V_{\mathrm{th}} \ln \left[\frac{N_{\mathrm{c}}(z)}{N_{0}}\right]
\tag{42}
$$

and

$$
\phi_{\mathrm{p}}(z)=\chi(z)+\mathrm{E}_{\mathrm{g}}(z)-V_{\mathrm{th}} \ln \left[\frac{N_{\mathrm{v}}(z)}{N_{0}}\right]
\tag{43}
$$

are the built-in potentials for the electrons and holes (due to variations in the material properties), respectively. Both built-in potentials as well as the electron affinity may be discontinuous with respect to position at heterojunctions in the semiconductor region. The baseline number density $N_{0}$ is arbitrary because potentials are defined up to a constant.

Equations (25), (26), (27), (40), and (41), have to be solved concurrently for $z \in\left(0, L_{\mathrm{z}}\right)$, in conjunction with a set of boundary conditions for $n(z), p(z)$, and $\phi(z)$. We opted for the Dirichlet choice

$$
\begin{array}{ll}
n(0)=n_{0}(0), & n\left(L_{\mathrm{z}}\right)=n_{0}\left(L_{\mathrm{z}}\right), \\
p(0)=p_{0}(0), & p\left(L_{\mathrm{z}}\right)=p_{0}\left(L_{\mathrm{z}}\right), \\
\phi(0)=\phi_{0}(0), & \phi\left(L_{\mathrm{z}}\right)=\phi_{0}\left(L_{\mathrm{z}}\right)+V_{\text {ext }},
\end{array}
\tag{44}
$$
$$
\tag{45}
$$
$$
\tag{46}
$$


because it models an ideal ohmic contact [1, 2]. Herein, the functions $n_0(z)$, $p_0(z)$ and $\phi_0(z)$ are the electron density, hole density and potential at LQTE, as discussed in Section 3.2, while $V_{\text{ext}}$ is the externally applied voltage across the terminals at the boundaries of the semiconductor region. Solution of the system of five equations enables the calculation of the current density

$$
J = J_{\mathrm{n}}(z) + J_{\mathrm{p}}(z) \tag{47}
$$

flowing uniformly through the solar cell.

The current density $J$ depends on the choice of $V_{\text{ext}}$, i.e., $J \equiv J(V_{\text{ext}})$. Repeating calculations for various values of $V_{\text{ext}}$ produces the $JV$-curve, with the maximum value of the power density

$$
P(V_{\text{ext}}) = J(V_{\text{ext}})V_{\text{ext}} \tag{48}
$$

indicating the maximum power density

$$
P_{\mathrm{max}} = \max_{V_{\text{ext}}} P(V_{\text{ext}}) \tag{49}
$$

obtainable from the solar cell. This in turn gives the efficiency of the solar cell as

$$
\eta = \frac{P_{\mathrm{max}}}{P_{\mathrm{in}}} \tag{50}
$$

where $P_{\text{in}} = 1000$ W m$^{-2}$ is the incident solar power density. It is the efficiency of the solar cell that we wish to optimize.

### 3.2 Local Quasi-Thermal Equilibrium
If a region containing a homogeneous semiconductor is charge-free and isolated from any external influences (e.g., $G \equiv 0$ and $V_{\text{ext}} = 0$), the distributions of electrons and holes with respect to energy tend to the Fermi distribution, with the Fermi-level lying at the intrinsic energy level, i.e., $\mathrm{E_{F_n}} = \mathrm{E_{F_p}} = \mathrm{E}_F$. Then, $J_{\mathrm{n}} = J_{\mathrm{p}}$ are identically zero and the semiconductor is said to be in LQTE. This concept is used to model the ideal ohmic boundary conditions mentioned in Section 3.1.

With $n_0(z)$ and $p_0(z)$ denoting the electron and hole densities, respectively, at LQTE, Eqs. (35)-(37) can be combined to give the mass-action equation

$$
\bar{n}^2(z) = n_0(z)p_0(z) ; \tag{51}
$$

furthermore,

$$
N_{\mathrm{f}}(z) + p_0(z) - n_0(z) = 0 \,, \tag{52}
$$

as the semiconductor is charge-free. Combining Eqs. (51) and (52), we get

$$
n_0(z) = \frac{N_{\mathrm{f}}(z) + \sqrt{N_{\mathrm{f}}(z)^2 + 4\bar{n}(z)^2}}{2} \tag{53}
$$

and

$$
p_0(z) = \frac{-N_{\mathrm{f}}(z) + \sqrt{N_{\mathrm{f}}(z)^2 + 4\bar{n}(z)^2}}{2} . \tag{54}
$$

At LQTE, the electron and hole quasi-Fermi levels coincide and are uniform. Thus,

$$
\mathrm{E_{F_n}}(v) = \mathrm{E_{c}}(v) + V_{\mathrm{th}} \ln \left[ \frac{n_0(v)}{N_{\mathrm{c}}(v)} \right] \tag{55}
$$

and

$$
\mathrm{E_{F_p}}(\zeta) = \mathrm{E_{v}}(\zeta) - V_{\mathrm{th}} \ln \left[ \frac{p_0(\zeta)}{N_{\mathrm{v}}(\zeta)} \right] , \tag{56}
$$


must be equal to each other for all $v \in (0, L_{z})$ and $\zeta \in (0, L_{z})$. Substitution of Eqs. (33) and (38) into $\mathrm{E}_{\mathrm{F}_{\mathrm{n}}}(v)=\mathrm{E}_{\mathrm{F}_{\mathrm{p}}}(\zeta)$ yields

$$
\begin{aligned}
-\phi_{0}(v)-\chi(v)+ & V_{\mathrm{th}} \ln \left[\frac{n_{0}(v)}{N_{\mathrm{c}}(v)}\right]= \\
& -\phi_{0}(\zeta)-\chi(\zeta)-\mathrm{E}_{\mathrm{g}}(\zeta)+V_{\mathrm{th}} \ln \left[\frac{p_{0}(\zeta)}{N_{\mathrm{v}}(\zeta)}\right].
\end{aligned}
$$

Equation (57) simplifies to

$$
-\chi(0)+V_{\mathrm{th}} \ln \left[\frac{n_{0}(0)}{N_{\mathrm{c}}(0)}\right]=-\phi_{0}(z)-\chi(z)-\mathrm{E}_{\mathrm{g}}(z)+V_{\mathrm{th}} \ln \left[\frac{p_{0}(z)}{N_{\mathrm{v}}(z)}\right]
$$

with the choice $v=0$ and $\zeta=z$, and to

$$
-\phi_{0}(z)-\chi(z)+V_{\mathrm{th}} \ln \left[\frac{n_{0}(z)}{N_{\mathrm{c}}(z)}\right]=-\chi(0)-\mathrm{E}_{\mathrm{g}}(0)+V_{\mathrm{th}} \ln \left[\frac{p_{0}(0)}{N_{\mathrm{v}}(0)}\right]
$$

with the choice $v=z$ and $\zeta=0$, where we have chosen $\phi_{0}(0)=0$ without loss of generality. Subtracting Eq. (58) from Eq. (59), we get

$$
\begin{aligned}
\phi_{0}(z)= & -[\chi(z)-\chi(0)]-\frac{1}{2}\left[\mathrm{E}_{\mathrm{g}}(z)-\mathrm{E}_{\mathrm{g}}(0)\right] \\
& +\frac{1}{2} V_{\mathrm{th}} \ln \left[\frac{n_{0}(z)}{n_{0}(0)}\right]+\frac{1}{2} V_{\mathrm{th}} \ln \left[\frac{p_{0}(z)}{p_{0}(0)}\right] \\
& -\frac{1}{2} V_{\mathrm{th}} \ln \left[\frac{N_{\mathrm{c}}(z)}{N_{\mathrm{c}}(0)}\right]-\frac{1}{2} V_{\mathrm{th}} \ln \left[\frac{N_{\mathrm{v}}(z)}{N_{\mathrm{v}}(0)}\right].
\end{aligned}
$$

Equations (53), (54), and (60) give the initial functions needed to specify the boundary data identified in Eqs. (44)-(46). However, in view of the LQTE assumption (52), these initial functions do not satisfy the system of ODEs (25)-(27).

### 3.3 Recombination

Recombination of an electron and a hole can take place through several different mechanisms [1, 2]. The electronic step in our program accommodates three different contributions to $R(n, p ; z)$.

#### 3.3.1 Radiative Recombination

Radiative recombination occurs when an electrons and a hole recombine across the full bandgap, releasing the energy as a photon with energy equal to the bandgap. At QTE, radiative recombination is identically balanced by electrons being thermally excited across the bandgap. The (net) radiative recombination rate is given by

$$
R_{\text {rad }}(n, p ; z)=\frac{\alpha_{\text {rad }}(z)}{\bar{n}^{2}(z)}\left[n(z) p(z)-\bar{n}^{2}(z)\right],
$$

where $\alpha_{\text {rad }}(z)$ depends on the semiconductor material. It should be noted that $R_{\text {rad }}(z) \equiv 0 \forall z \in\left[0, L_{z}\right]$ at LQTE.

#### 3.3.2 Shockley-Read-Hall (SRH) Recombination

The SRH recombination contribution is due to electrons and holes recombining via an intermediate gap state. It is modeled by

$$
R_{S R H}(n, p ; z)=\frac{n(z) p(z)-\bar{n}^{2}(z)}{\tau_{\mathrm{p}}(z)\left[n(z)+n_{1}(z)\right]+\tau_{\mathrm{n}}(z)\left[p(z)+p_{1}(z)\right]},
$$

where $n_{1}(z)$ and $p_{1}(z)$ are, respectively, the electron and hole densities at the trap energy level. If this level is the intrinsic energy level $\mathrm{E}_{\mathrm{i}}(z)$, then $n_{1}(z)=p_{1}(z)=\bar{n}(z)$ from Eqs. (35) and (36). The functions $\tau_{\mathrm{n}}(z)$ and $\tau_{\mathrm{p}}(z)$ are material dependent.


#### 3.3.3 Auger Recombination

The Auger recombination contribution arises from a three-particle recombination pathway, occurring when an electron and a hole recombine across the bandgap, with the released energy transferred to a third charge carrier which is excited away from both band edges. This recombination rate is given by

$$
\begin{aligned}
R_{A u g}(n, p ; z) & =C_{\mathrm{n}}(z) n(z)\left[n(z) p(z)-\bar{n}^{2}(z)\right] \\
& +C_{\mathrm{p}}(z) p(z)\left[n(z) p(z)-\bar{n}^{2}(z)\right],
\end{aligned}
\tag{63}
$$

where the functions $C_{\mathrm{n}}(z)$ and $C_{\mathrm{p}}(z)$ are material dependent.

All three contributions add, so that

$$
R(n, p ; z)=R_{\text {rad }}(n, p ; z)+R_{S R H}(n, p ; z)+R_{A u g}(n, p ; z).
\tag{64}
$$

It can be seen that the total recombination $R=0$ at LQTE irrespective of the choice of the material parameters. For all results reported in this paper, we set $\alpha_{\text {rad }}(z) \equiv 0$ and $C_{\mathrm{n}}(z)=C_{\mathrm{p}}(z) \equiv 0 \forall z \in \Omega_{\mathrm{el}}$ and only the SRH recombination was activated, in order to present illustrative results without the expenditure of significant computational time.

### 3.4 Heterojunctions: Continuous Quasi-Fermi Levels

When there is a jump in either $\chi(z)$ or $E_{\mathrm{g}}(z)$ or both, and thus in $\phi_{\mathrm{n}}(z)$ or $\phi_{\mathrm{p}}(z)$, then $n(z)$ and $p(z)$ may also have jumps. A heterojunction is formed at the discontinuity [36]. A commonly used way to model this discontinuity requires the assumption of continuous quasi-Fermi levels, whereas another commonly used way requires consideration of thermionic emission at the discontinuity [37]. We chose to implement the continuous quasi-Fermi level (CQFL) model, although the thermionic-emission model is also compatible with the HDG method.

The CQFL model uses the limit of a continuum model to quantify the jump at a heterojunction. To understand the resulting jump conditions, let us examine a small region $0<z \leq \delta$ in which the electron affinity $\chi(z)$ changes linearly by $\Delta \chi$, while $N_{\mathrm{c}}(z)$ is uniform. Then, differentiating Eq. (42) with respect to $z$ yields

$$
\frac{d}{d z} \phi_{\mathrm{n}}(z)=\frac{\Delta \chi}{\delta}
\tag{65}
$$

in this region. Furthermore, we assume that $G \delta \approx R \delta \approx 0$ in this region so that Eq. (25) simplifies to

$$
\frac{d}{d z} J_{\mathrm{n}}(z)=0 ;
\tag{66}
$$

hence, $J_{\mathrm{n}}(z)=J_{\mathrm{n}}^{\circ}$. Finally, we also assume that both $\mu_{\mathrm{n}}(z) \approx \mu_{\mathrm{n}}^{\circ}$ and $\phi(z) \approx \phi^{\circ}$ are uniform in this region, so that Eq. (40) simplifies to

$$
J_{\mathrm{n}}^{\circ}=-q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} n(z) \frac{\Delta \chi}{\delta}+q_{\mathrm{e}} V_{\mathrm{th}} \mu_{\mathrm{n}}^{\circ} \frac{d}{d z} n(z),
\tag{67}
$$

after using Eq. (65).

The solution of Eq. (67) is

$$
n(z)=C \exp \left(\frac{\Delta \chi}{V_{\mathrm{th}}} \frac{z}{\delta}\right)-\frac{J_{\mathrm{n}}^{\circ} \delta}{q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} \Delta \chi},
\tag{68}
$$

where $C$ is the constant of integration. As $n(z)=n_{\mathrm{L}}$ at $z=0$, we get

$$
n(z)=\left(n_{\mathrm{L}}+\frac{J_{\mathrm{n}}^{\circ} \delta}{q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} \Delta \chi}\right) \exp \left(\frac{\Delta \chi}{V_{\mathrm{th}}} \frac{z}{\delta}\right)-\frac{J_{\mathrm{n}}^{\circ} \delta}{q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} \Delta \chi}
\tag{69}
$$

from Eq. (68). As $n(z)=n_{\mathrm{R}}$ at $z=\delta$, Eq. (69) yields

$$
n_{\mathrm{R}}=\left(n_{\mathrm{L}}+\frac{J_{\mathrm{n}}^{\circ} \delta}{q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} \Delta \chi}\right) \exp \left[\frac{\Delta \chi}{V_{\mathrm{th}}}\right]-\frac{J_{\mathrm{n}}^{\circ} \delta}{q_{\mathrm{e}} \mu_{\mathrm{n}}^{\circ} \Delta \chi}.
\tag{70}
$$

In the limit of $\delta \to 0$, we get the jump condition
$$
n_{\mathrm{R}}=\exp \left[\frac{\Delta \chi}{V_{\mathrm{th}}}\right] n_{\mathrm{L}} \tag{71}
$$
from Eq. (70). The same analysis can be performed for the hole density $p(z)$, which results in the jump condition
$$
p_{\mathrm{R}}=\exp \left[-\frac{\Delta \chi+\Delta \mathrm{E}_{\mathrm{g}}}{V_{\mathrm{th}}}\right] p_{\mathrm{L}}, \tag{72}
$$
where $\Delta \mathrm{E}_{\mathrm{g}}$ is the change in the bandgap over the region with thickness $\delta$. Equations (71) and (72) need to be enforced across any junction over which $\chi$ or $\mathrm{E}_{\mathrm{g}}$ jump. This is accomplished using the HDG method described in Section 4.

### 3.5 Dimensionless Formulation
The equations of the DDE model are scaled in order to ensure that the internal variables are dimensionless [35], the scaling parameters being provided in Table 1. Equations (25) and (26) are thus non-dimensionalized to $^{1}$
$$
\frac{d}{d z} J_{\mathrm{n}}(z)=-G(z)+R(n, p ; z) \tag{73}
$$
and
$$
\frac{d}{d z} J_{\mathrm{p}}(z)=G(z)-R(n, p ; z), \tag{74}
$$
respectively, and Eqs. (40) and (41) to
$$
J_{\mathrm{n}}(z)=-\mu_{\mathrm{n}}(z)\left\{n(z) \frac{d}{d z}\left[\phi(z)+\phi_{\mathrm{n}}(z)\right]-\frac{d}{d z} n(z)\right\} \tag{75}
$$
and
$$
J_{\mathrm{p}}(z)=-\mu_{\mathrm{p}}(z)\left\{p(z) \frac{d}{d z}\left[\phi(z)+\phi_{\mathrm{p}}(z)\right]+\frac{d}{d z} p(z)\right\}, \tag{76}
$$
respectively. Electing to keep $\varepsilon_{d c}(z) \equiv \varepsilon_{d c}^{0} \forall z \in\left[0, L_{z}\right]$ uniform in the semiconductor region, we obtain the non-dimensionalized form of Eq. (27) as
$$
-\lambda^{2} \frac{d^{2}}{d z^{2}} \phi(z)=N_{\mathrm{f}}(z)+p(z)-n(z), \tag{77}
$$
where the Poisson constant
$$
\lambda^{2}=\frac{\varepsilon_{0} \varepsilon_{d c}^{0} \phi_{\mathrm{s}}}{q_{\mathrm{e}} N_{\mathrm{s}} L_{\mathrm{s}}^{2}} \tag{78}
$$
is dimensionless. We define the dimensionless d.c. electric field
$$
E_{\mathrm{dc}}(z)=-\lambda^{2} \frac{d}{d z} \phi(z) \tag{79}
$$
and transform Eq. (77) to
$$
\frac{d}{d z} E_{\mathrm{dc}}(z)=N_{\mathrm{f}}(z)+p(z)-n(z), \tag{80}
$$
which has the same form as Eqs. (73) and (74). These three ODEs are discretized using the HDG method, as described in Section 4.

$^{1}$At the risk of confusion, we have not used new notation for the dimensionless variables in order to keep the text clean.

<table>
 <thead>
  <tr>
   <th>
    Scaling
   </th>
   <th>
    Symbol
   </th>
   <th>
    Representative Value
   </th>
   <th>
    Variable(s)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    Length
   </td>
   <td>
    $L_{\text{s}}$
   </td>
   <td>
    $\mathcal{O}{(L_{z})} \approx {2 \times 10^{- 4}}$ cm
   </td>
   <td>
    $z$
   </td>
  </tr>
  <tr>
   <td>
    Mobility
   </td>
   <td>
    $\mu_{\text{s}}$
   </td>
   <td>
    $1.5$ cm² V⁻¹ s⁻¹
   </td>
   <td>
    $\mu_{\text{n,p}}$
   </td>
  </tr>
  <tr>
   <td>
    Voltage
   </td>
   <td>
    $\phi_{\text{s}} = V_{\text{th}}$
   </td>
   <td>
    $0.0259$ V
   </td>
   <td>
    $\phi$, $\phi_{\text{n,p}}$, $\chi$, $V_{\text{ext}}$, $\text{E}_{\text{i,c,F}_{\text{n}},\text{F}_{\text{p}},\text{g,v}}$
   </td>
  </tr>
  <tr>
   <td>
    Density
   </td>
   <td>
    $N_{\text{s}}$
   </td>
   <td>
    $\max{({|N_{\text{f}}|})} \approx 10^{16}$ cm⁻³
   </td>
   <td>
    $n$, $p$, $\overline{n}$, $n_{0,1}$, $p_{0,1}$,$N_{\text{c,f,v}}$
   </td>
  </tr>
  <tr>
   <td>
    Poisson const.
   </td>
   <td>
    $\lambda^{2}$
   </td>
   <td>
    $4.1717 \times 10^{- 4}$
   </td>
   <td>
    –
   </td>
  </tr>
  <tr>
   <td>
    Density rate
   </td>
   <td>
    $G_{\text{s}} = \frac{\mu_{\text{s}}N_{\text{s}}\phi_{\text{s}}}{L_{\text{s}}^{2}}$
   </td>
   <td>
    $9.6945 \times 10^{21}$ cm⁻³ s⁻¹
   </td>
   <td>
    $G$, $R$
   </td>
  </tr>
  <tr>
   <td>
    Current
   </td>
   <td>
    $J_{\text{s}} = \frac{q_{\text{e}}\mu_{\text{s}}N_{\text{s}}\phi_{\text{s}}}{L_{\text{s}}}$
   </td>
   <td>
    $0.3106$ mA cm⁻²
   </td>
   <td>
    $J$, $J_{\text{n,p}}$
   </td>
  </tr>
 </tbody>
</table>

Table 1: Table of scaling parameters and applicable variables.

<table>
 <thead>
  <tr>
   <th>
   </th>
   <th>
    Eqs. (73) and (75)
   </th>
   <th>
    Eqs. (74) and (76)
   </th>
   <th>
    Eqs. (79) and (80)
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <th>
    J
   </th>
   <td>
    $J_{\text{n}}$
   </td>
   <td>
    $J_{\text{p}}$
   </td>
   <td>
    $E$
   </td>
  </tr>
  <tr>
   <th>
    m
   </th>
   <td>
    $n$
   </td>
   <td>
    $p$
   </td>
   <td>
    $\phi$
   </td>
  </tr>
  <tr>
   <th>
    Z
   </th>
   <td>
    $\phi$
   </td>
   <td>
    $\phi$
   </td>
   <td>
    $0$
   </td>
  </tr>
  <tr>
   <th>
    $\mathsf{v}_{\text{m}}$
   </th>
   <td>
    $\phi_{\text{n}}$
   </td>
   <td>
    $\phi_{\text{p}}$
   </td>
   <td>
    $0$
   </td>
  </tr>
  <tr>
   <th>
    $\text{c}_{1}$
   </th>
   <td>
    $1/\mu_{\text{n}}$
   </td>
   <td>
    $- {1/\mu_{\text{p}}}$
   </td>
   <td>
    $- {1/\lambda^{2}}$
   </td>
  </tr>
  <tr>
   <th>
    $\text{c}_{2}$
   </th>
   <td>
    $- 1$
   </td>
   <td>
    $1$
   </td>
   <td>
    $0$
   </td>
  </tr>
  <tr>
   <th>
    $\text{c}_{3}$
   </th>
   <td>
    $0$
   </td>
   <td>
    $0$
   </td>
   <td>
    $1$
   </td>
  </tr>
 </tbody>
</table>

Table 2: Correspondence between the generalized transport system of Eqs. (81)–(83) and Eqs. (73)–(80) of the dimensionless DDE model.

## 4 Hybridizable Discontinuous Galerkin Formulation

The hybridizable discontinuous Galerkin (HDG) method [13, 34] possesses several features which are advantageous for the implementation of the DDE model for solar cells [10]. The relaxation of the requirement that the solution is continuous at the boundaries of elements permits solutions where the variables have strong gradients and second derivatives. It also naturally allows discontinuities in the solution due to discontinuous material parameters, such as those which occur at heterojunctions discussed in Section 3.4.

### 4.1 Generalized Transport System

To simplify the description of the numerical scheme used to solve Eqs. (73)–(76), (79), and (80), it is useful to partition them into three sets, each with the form

$$
{\text{c}_{1}\text{J}} = {{\text{c}_{2}\text{m}\frac{d}{dz}{({\text{Z} + \mathsf{v}_{\text{m}}})}} + {\frac{d}{dz}\text{m}}},
\tag{81}
$$

$$
\frac{d}{dz}\text{J} = {{\text{f}{(n,p)}} + {\text{c}_{3}{({p - n})}}},
\tag{82}
$$

along the associated Dirichlet boundary conditions

$$
\left. \begin{aligned}
{\text{m}{(0)}} &amp; = {\text{m}_{0}{(0)}} \\
{\text{m}{(L_{z})}} &amp; = {\text{m}_{0}{(L_{z})}}
\end{aligned} \right\}.
\tag{83}
$$

Here, Z is either given by the solution of another set or vanishes, $\mathsf{v}_{\text{m}}$ is a given function of position, and $\text{f}{(n,p)}$ is also given. To get each of the three sets of equations in the dimensionless DDE model provided in Section 3.5, we choose the parameters and functions as in Table 2.

Henceforth, we refer to Eqs. (81)–(83) as the generalized transport system. We now proceed to design a numerical scheme to discretize this system of equations.

### 4.2 Discretization of Electronic Domain

The electronic domain $\Omega_{\text{el}}$ is covered by a mesh $\mathcal{S} = \{\mathcal{N}, \mathcal{T}\}$ of $N_z + 1$ nodes $\mathcal{N}$ and $N_z$ elements $\mathcal{T}$. The element $s_\gamma = (z_{\gamma-1}, z_\gamma)$ lies between the nodes $z_{\gamma-1}$ and $z_\gamma$,
$$
\mathcal{N} = \{z_\gamma|z_\gamma \in \Omega_{\text{el}}, \gamma \in \{0,.., N_z\}\} . \tag{84}
$$
is the set of all nodes, and
$$
\mathcal{T} = \{s_\gamma|s_\gamma = (z_{\gamma-1}, z_\gamma) \subset \Omega_{\text{el}}, \gamma \in \{1,..., N_z\}\} \tag{85}
$$
is the set of all elements. The generalized transport system is discretized using the space
$$
\mathbb{V}_h = \left\{v_h \in L^2(\Omega_{\text{el}}) \mid \left. v_h \right|_{s_\gamma} \in \mathbb{P}_{P_{\text{deg}}} \ \forall s_\gamma \in \mathcal{T}\right\} , \tag{86}
$$
where $\mathbb{P}_{P_{\text{deg}}}$ is the set of polynomials of degree $P_{\text{deg}}$ in $z$ (and so that $\mathbb{V}_h$ is a space of discontinuous piecewise polynomials),
$$
\mathbb{W}_h = \{w_h \in \left. w_h \right|_{z_\gamma} \in \mathbb{R}^+, \ \forall z_\gamma \in \mathcal{N}\}, \tag{87}
$$
and $\mathbb{R}^+$ is the set of positive real numbers. Although a different value of $P_{\text{deg}}$ may be chosen for each element $s_\gamma$, for simplicity of notation we choose the same value of $P_{\text{deg}}$ for all elements.

We seek the numerical solutions $(\mathcal{J}_h, \hat{\mathcal{J}}_h, \mathfrak{m}_h, \hat{\mathfrak{m}}_h) \in \mathbb{V}_h \times \mathbb{W}_h \times \mathbb{V}_h \times \mathbb{W}_h$ where $\hat{\mathcal{J}}_h$ and $\hat{\mathfrak{m}}_h$ are the vectors of numerical approximations to $\mathcal{J}$ and $m$ at the nodes in $\mathcal{N}$. Multiplying Eq. (81) by a test function $\psi \in \mathbb{V}_h$ and Eq. (82) by a test function $\eta \in \mathbb{V}_h$, and then integrating over $\Omega_{\text{el}}$, we obtain
$$
\begin{aligned}
\sum_{\gamma=1}^{N_z}(\mathrm{c}_1 \mathcal{J}, \psi)_\gamma = & \mathrm{c}_2 \sum_{\gamma=1}^{N_z} \left( \mathfrak{m} \frac{d}{dz} Z, \psi \right)_\gamma + \mathrm{c}_2 \sum_{\gamma=1}^{N_z} \left( \mathfrak{m} \frac{d}{dz} \mathrm{v}_{\mathfrak{m}}, \psi \right)_\gamma \\
& + \sum_{\gamma=1}^{N_z} \left( \frac{d}{dz} \mathfrak{m}, \psi \right)_\gamma
\end{aligned} \tag{88}
$$
and
$$
\sum_{\gamma=1}^{N_z} \left( \frac{d}{dz} \mathcal{J}, \eta \right)_\gamma = \sum_{\gamma=1}^{N_z} (\mathrm{f}, \eta)_\gamma + \mathrm{c}_3 \sum_{\gamma=1}^{N_z} ((p-n), \eta)_\gamma, \tag{89}
$$
where the notation
$$
(\eta, \pi)_\gamma = \int_{s_\gamma} \eta(z) \psi(z) \, \mathrm{d}z. \tag{90}
$$

For functions $\eta \in \mathbb{V}_h$, $\psi \in \mathbb{V}_h$, and $\hat{\eta} \in \mathbb{W}_h$, we define
$$
\left( \frac{d}{dz} \eta, \psi \right)_\gamma = < \hat{\eta}, \psi >_\gamma - \left( \eta, \frac{d}{dz} \psi \right)_\gamma \tag{91}
$$
via integration by parts, with
$$
< \hat{\eta}, \psi >_\gamma = \left. \hat{\eta}_\gamma \psi \right|_{\gamma, R} - \left. \hat{\eta}_{\gamma-1} \psi \right|_{\gamma, L} \tag{92}
$$
and
$$
\left.
\begin{aligned}
\left. \psi \right|_{\gamma, L} & = \lim_{z \to z_{\gamma-1}^+} \psi(z) \\
\left. \psi \right|_{\gamma, R} & = \lim_{z \to z_\gamma^-} \psi(z)
\end{aligned}
\right\}. \tag{93}
$$

Then, Eq. (88) can be written as
$$
\begin{aligned}
\sum_{\gamma=1}^{N_z} \bigg[ (\mathrm{c}_1 \mathcal{J}, \psi)_\gamma & - \mathrm{c}_2 \left( \mathfrak{m} \frac{d}{dz} Z, \psi \right)_\gamma - \mathrm{c}_2 \left( \mathfrak{m} \frac{d}{dz} \mathrm{v}_{\mathfrak{m}}, \psi \right)_\gamma + \left( \mathfrak{m}, \frac{d}{dz} \psi \right)_\gamma \\
& - < \hat{\mathfrak{m}}, \psi >_\gamma \bigg] = 0
\end{aligned} \tag{94}
$$

and Eq. (89) as

$$
\sum_{\gamma=1}^{N_{z}}\left[\left(\mathrm{J}, \frac{d}{d z} \eta\right)_{\gamma}+\mathrm{c}_{3}(p, \eta)_{\gamma}-\mathrm{c}_{3}(n, \eta)_{\gamma}+(\mathrm{f}, \eta)_{\gamma}-<\hat{\mathrm{J}}, \eta>_{\gamma}\right]=0.
\tag{95}
$$

To complete the discretization, we need to enforce approximate continuity of the discrete flux. Therefore, at each node we define the discrete flux as

$$
\hat{\mathrm{J}}_{\gamma}=\mathrm{J}\left(z_{\gamma}\right)+\tau_{m}\left(z_{\gamma}\right)\left[\mathrm{m}\left(z_{\gamma}\right)-\hat{\mathrm{m}}_{\gamma}\right],
\tag{96}
$$

where $\zeta(z_{\gamma})=\lim _{z \to z_{\gamma}^{ \pm}} \zeta(z)$ and $\tau_{m}(z_{\gamma}) \geq 0$ is a hybridization (or penalty) function to be chosen. Continuity of the flux requires

$$
\left.\mathrm{J}\right|_{\gamma+1, L}+\left.\tau_{m}\left(\mathrm{m}-\hat{\mathrm{m}}_{\gamma}\right)\right|_{\gamma+1, L}=\left.\mathrm{J}\right|_{\gamma, R}+\left.\tau_{m}(\mathrm{~m}-\hat{\mathrm{m}})\right|_{\gamma, R}
\tag{97}
$$

at each interior node. Finally, the boundary conditions are enforced by requiring

$$
\hat{\mathrm{m}}=\mathrm{m}_{0}
\tag{98}
$$

at the ends of $\Omega$.

By defining the jump operator as

$$
[\![\xi]\!]_{\gamma}=\left.\xi\right|_{\gamma, R}-\left.\xi\right|_{\gamma, L},
\tag{99}
$$

the problem becomes that of finding a discrete solution $(\mathrm{J}_{h}, \mathrm{~m}_{h}, \hat{\mathrm{m}}) \in \mathbb{V}_{h} \times \mathbb{V}_{h} \times \mathbb{W}_{h}$ such that

$$
\begin{aligned}
\sum_{\gamma=1}^{N_{z}}\left[(\mathrm{c}_{1} \mathrm{~J}_{h}, \psi)_{\gamma}-\mathrm{c}_{2}\left(\mathrm{~m}_{h} \frac{d}{d z} \mathrm{Z}, \psi\right)_{\gamma}-\mathrm{c}_{2}\left(\mathrm{~m}_{h} \frac{d}{d z} \mathrm{v}_{\mathrm{m}}, \psi\right)_{\gamma}+\left(\mathrm{m}_{h}, \frac{d}{d z} \psi\right)_{\gamma}\right. \\
\left.-<\hat{\mathrm{m}}, \psi>_{\gamma}\right]=0,
\end{aligned}
\tag{100}
$$

$$
\begin{aligned}
\sum_{\gamma=1}^{N_{z}}\left[\left(\mathrm{~J}_{h}, \frac{d}{d z} \eta\right)_{\gamma}+\mathrm{c}_{3}\left(p_{h}, \eta\right)_{\gamma}-\mathrm{c}_{3}\left(n_{h}, \eta\right)_{\gamma}+(\mathrm{f}, \eta)_{\gamma}\right. \\
\left.-<\mathrm{J}_{h}, \eta>_{\gamma}-<\tau_{m} \mathrm{~m}_{h}, \eta>_{\gamma}+<\tau_{m} \hat{\mathrm{m}}, \eta>_{\gamma}\right]=0,
\end{aligned}
\tag{101}
$$

$$
[\![\mathrm{J}_{h}]\!]_{\gamma}+[\![\tau_{m} \mathrm{~m}_{h}]\!]_{\gamma}-[\![\tau_{m}]\!]_{\gamma} \hat{\mathrm{m}}=0 \text { at all interior nodes, }
\tag{102}
$$

for all $(\psi, \eta) \in \mathbb{V}_{h} \times \mathbb{V}_{h}$, and with $\hat{\mathrm{m}}=\mathrm{m}_{0}$ for $z \in\{0, L_{z}\}$. Obviously, there are $2 N_{z}(P_{\mathrm{deg}}+1)$ degrees of freedom for the functions $\mathrm{J}$ and $\mathrm{m}$, and $N_{z}-1$ degrees for $\hat{\mathrm{m}}$. In turn, the test functions $\psi$ and $\eta$ give $2 N_{z}(P_{\mathrm{deg}}+1)$ equations from Eqs. (100) and (101), while Eqs. (102) give a further $N_{z}-1$ equations. For a linear problem of this type, existence and uniqueness of the solution have been proven and the error estimates have been derived, for example, by Fu *et al.* [13]; see also Cockburn *et al.* [12]. The nonlinear problem defined here remains to be analyzed.

To help with conditioning and also to provide a useful choice of discretization points for the nonlinear problem, we choose the interpolation points for $\mathbb{V}_{h}$ on each element to be the $P_{\mathrm{deg}}+1$ Gauss-Lobatto points [38]. We now replace functions $\mathrm{J}_{h}, \mathrm{~m}_{h}, \mathrm{Z}_{h}, n_{h}$, and $p_{h}$ by their finite-element approximations with the form

$$
\zeta_{h}(z)=\sum_{\ell=1}^{N_{z}\left(P_{\mathrm{deg}}+1\right)} \zeta_{\ell} \psi_{\ell}(z),
\tag{103}
$$

where $\psi_{\ell} \in \mathbb{V}_{h}$ are piecewise polynomial finite-element basis functions that are each compactly supported on one of the elements $s_{\gamma}$, and $\zeta_{\ell} \in \mathbb{R}$ are constants to be determined. Upon substitution of these into

Eqs. (100)-(102), and choosing the test functions $\eta$ and $\psi$ to also be the finite-element basis functions $\psi_{j} \in \mathbb{V}_{h}$ to be piecewise polynomials that are each compactly supported on element $s_{\gamma}$, we obtain the HDG equations

$$
\begin{aligned}
\sum_{\gamma=1}^{N_{z}}\left[\mathrm{~J}_{\ell}\left(\mathrm{c}_{1} \psi_{\ell}, \psi_{j}\right)_{\gamma}\right. &-\mathrm{c}_{2} \mathfrak{m}_{\ell} \mathrm{Z}_{k}\left(\psi_{\ell} \frac{d}{d z} \psi_{k}, \psi_{j}\right)_{\gamma}-\mathrm{c}_{2} \mathfrak{m}_{\ell}\left(\frac{d}{d z} \mathrm{v}_{\mathfrak{m}} \psi_{\ell}, \psi_{j}\right)_{\gamma} \\
&+\left.\mathfrak{m}_{\ell}\left(\psi_{\ell}, \frac{d}{d z} \psi_{j}\right)_{\gamma}-<\hat{\mathfrak{m}}, \psi_{j}>_{\gamma}\right]=0,
\end{aligned}
$$

$$
\begin{aligned}
\sum_{\gamma=1}^{N_{z}}\left[\mathrm{~J}_{\ell}\left(\psi_{\ell}, \frac{d}{d z} \psi_{j}\right)_{\gamma}\right. &-\mathrm{c}_{3}\left[n_{\ell}\left(\psi_{\ell}, \psi_{j}\right)_{\gamma}+p_{\ell}\left(\psi_{\ell}, \psi_{j}\right)_{\gamma}\right] \\
&-\left.\mathfrak{m}_{\ell}<\tau_{m} \psi_{\ell}, \psi_{j}>_{\gamma}+\left(\mathfrak{f}, \psi_{j}\right)_{\gamma}+<\hat{\mathfrak{m}}, \psi_{j}>_{\gamma}\right]=0,
\end{aligned}
$$

$$
\mathrm{J}_{\ell} [\!\!\mid \psi_{\ell}\!\!\mid]_{\gamma}+\mathfrak{m}_{\ell} [\!\!\mid \tau_{m} \psi_{\ell}\!\!\mid]_{\gamma}- [\!\!\mid \tau_{m}\!\!\mid]_{\gamma} \hat{\mathfrak{m}}_{\ell}=0 \text { at interior nodes, }
$$

$$
\hat{\mathfrak{m}}_{\gamma}=\mathfrak{m}_{0} \text { at the end points of } \Omega_{\mathrm{el} .},
$$

for $1 \leq j \leq N_{z}(P_{\mathrm{deg}}+1), 1 \leq k \leq N_{z}(P_{\mathrm{deg}}+1)$, and $1 \leq \ell \leq N_{z}(P_{\mathrm{deg}}+1)$. In Eqs. (104)-(107) and henceforth, we use the Einstein summation convention (i.e., summation is implied over any duplicated index), column vectors denoted as $\underline{v}$ comprise elements $v_{k}$, and matrices denoted as $\underline{\underline{M}}$ comprise elements $M_{k, \ell}$.

The full set of drift-diffusion equations (73)-(80) along with the boundary conditions (44)-(46) is now discretized by three copies of the above equations with function and parameter choices from Table 2. There are two usual ways to solve the resulting nonlinear system: Gummel iteration [35] and Newton's method [39]. We found that straightforward Gummel iteration did not converge reliably for the parameter values in our simulations. So we elected to use Newton's method with a scheme of the homotopy type [40] to help provide a good initial guess.

### 4.3 Nonlinear Convection

A practical difficulty with implementing the scheme arises when dealing with the nonlinear term

$$
\underline{\psi}_{\mathrm{m}}=\sum_{\gamma=1}^{N_{z}}\left[\mathfrak{m}_{\ell} \mathrm{Z}_{k}\left(\psi_{\ell} \frac{d}{d z} \psi_{k}, \psi_{j}\right)_{\gamma}\right].
$$

The integral

$$
\Psi_{\ell, j, k}^{0,0,1}=\sum_{\gamma=1}^{N_{z}}\left[\left(\psi_{\ell} \frac{d}{d z} \psi_{k}, \psi_{j}\right)_{\gamma}\right]
$$

on the right side of Eq. (108) is an element of a $\left[N_{z}(P_{\mathrm{deg}}+1)\right]^{3}$ tensor denoted by $\bar{\Psi}^{0,0,1}$, where the 0,0,1 superscript specifies that $\psi_{k}$ is differentiated once. The non-linear term can then be seen as the product

$$
\underline{\psi}_{\mathrm{m}} \equiv \Psi_{\ell, j, k}^{0,0,1} \mathfrak{m}_{\ell} \mathrm{Z}_{k},
$$

where the indices $\ell$, $j$, and $k$ select the elements of the tensor. Although manipulation of tensors with rank greater than 2 is not natively supported in Matlab, the tensor $\bar{\Psi}^{0,0,1}$ is very sparse as it is block diagonal; hence, the calculation speed can be increased by storing it as a non-square matrix.

As each of the finite-element basis functions $\psi_{j}$ is compactly supported on just one interval, a local tensor

$$
\bar{\Phi}_{\gamma}^{0,0,1} \equiv\left(\psi_{\ell} \frac{d}{d z} \psi_{k}, \psi_{j}\right)_{\gamma}
$$

with dimensions $\left[\left(P_{\mathrm{deg}}+1\right)\right]^{3}$ can be formed. This local tensor, which is not necessarily sparse, can be rewritten as a $\left[P_{\mathrm{deg}}+1\right] \times\left[\left(P_{\mathrm{deg}}+1\right)^{2}\right]$ rectangular matrix $\bar{\Psi}_{\gamma}^{0,0,1}$. Finally, a global matrix $\bar{\Psi}^{0,0,1}$ with

dimension $N_{\mathrm{z}}(P_{\mathrm{deg}}+1)\times(N_{\mathrm{z}}(P_{\mathrm{deg}}+1))^{2}$ to represent $\bar{\boldsymbol{\Psi}}^{0,0,1}$ is formed by repeating the local matrix as a block diagonal.

In order to calculate the term $\underline{\psi}_{\mathrm{m}}$, the vector of coefficients $\underline{\mathrm{m}}_{\ell}$ is reshaped into a $[N_{\mathrm{z}}(P_{\mathrm{deg}}+1)]^{2}\times N_{\mathrm{z}}(P_{\mathrm{deg}}+1)$ matrix $\underline{\underline{M}}$: the block diagonal is formed from $P_{\mathrm{deg}}+1$ blocks of $\mathrm{m}_{\ell}$, with each block repeated $N_{\mathrm{z}}$ times. The required solution is then given by
$$
\underline{\psi}_{\mathrm{m}}=\underline{\underline{M}}\underline{Z}.\tag{112}
$$

While this is more convoluted than simply performing the tensor multiplication, this matrix multiplication method is comparatively very fast because $\bar{\boldsymbol{\Psi}}^{0,0,1}$ is independent of the solution (i.e., constant) and so can be precomputed.

### 4.4 Upwinding
One of the reasons for choosing the HDG method is to include upwinding in a natural way through the choice of hybridization functions $\tau_{m}$ [13]. Upwinding was included in our simulations as follows.

First, the dimensionless effective average electron speed $u_{n}(z)=-J_{\mathrm{n}}(z)/n(z)$ and the effective average hole speed $u_{p}(z)=J_{\mathrm{p}}(z)/p(z)$ were formulated. Next, Eqs. (75) and (76) were used to obtain
$$
u_{n}(z)=\mu_{\mathrm{n}}(z)\frac{d}{dz}\left\{\phi(z)+\phi_{\mathrm{n}}(z)-\ln[n(z)]\right\}\tag{113}
$$
and
$$
u_{p}(z)=-\mu_{\mathrm{p}}(z)\frac{d}{dz}\left\{\phi(z)+\phi_{\mathrm{p}}(z)+\ln[p(z)]\right\},\tag{114}
$$
respectively. The terms containing $\ln[...]$ are identifiable as the diffusion terms, with the remaining terms modeling drift in the effective electric field. In drift-dominated regions of the solar cell, which often constitute most of $\Omega_{\mathrm{el}}$, we therefore get
$$
u_{n}(z)=-\lambda^{-2}\mu_{\mathrm{n}}(z)\left[E_{\mathrm{dc}}(z)+E_{n}(z)\right]\tag{115}
$$
and
$$
u_{n}(z)=\lambda^{-2}\mu_{\mathrm{p}}(z)\left[E_{\mathrm{dc}}(z)+E_{p}(z)\right],\tag{116}
$$
where
$$
E_{n}(z)=-\lambda^{2}\frac{d}{dz}\phi_{\mathrm{n}}(z)\tag{117}
$$
is the dimensionless effective electric field acting on electrons and
$$
E_{p}(z)=-\lambda^{2}\frac{d}{dz}\phi_{\mathrm{p}}(z)\tag{118}
$$
is the dimensionless effective electric field acting on holes. These two fields arise from material nonhomogeneity.

Information in this drift-dominated system travels in the directions of the electron and hole velocities. At each node, we therefore want to take values of $n(z)$ and $p(z)$ from the inflow side and pass them to the outflow side. As $\mu_{\mathrm{n}}(z)>0$ and $\mu_{\mathrm{p}}(z)>0$, the respective directions entirely depend on the signs of $E_{\mathrm{dc}}(z)+E_{n}(z)$ and $E_{\mathrm{dc}}(z)+E_{p}(z)$. While the hybridization function $\tau_{m}(z)$ is defined as a function of position, only the values at the ends of the elements contribute to the model. Consequently, we create $\bar{\tau}(z)$ as a piecewise linear function, defined by the limiting values at each side of each node. Two possible limiting values $\bar{\tau}_{1}$ and $\bar{\tau}_{2}$ are chosen such that $\bar{\tau}_{1}\ll\bar{\tau}_{2}$. Then, to ensure that the correct information flow is achieved,

- $\left.\tau_{m}\right|_{\gamma,R}=\bar{\tau}_{1}$ and $\left.\tau_{m}\right|_{\gamma,L}=\bar{\tau}_{2}$ are used if $E_{\mathrm{dc}}(z)+E_{n}(z)>0$, or
- $\left.\tau_{m}\right|_{\gamma,L}=\bar{\tau}_{1}$ and $\left.\tau_{m}\right|_{\gamma,R}=\bar{\tau}_{2}$ are used $E_{\mathrm{dc}}(z)+E_{n}(z)<0$.

Our choices of $\bar{\tau}_{1}$ and $\bar{\tau}_{2}$ are given in Table 5.

### 4.5 Recombination

The recombination term $R(n,p;z)$ is a nonlinear function of $n(z)$ and $p(z)$. Consequently, care needs to be taken on how to incorporate this term into the HDG method. For example, if radiative recombination given by Eq. (61) is incorporated in the HDG method, we get

$$
\left(R_{r a d}, \psi_{j}\right)_{\gamma}=n_{\ell} p_{k}\left(\frac{\alpha_{r a d}}{\bar{n}^{2}} \psi_{\ell} \psi_{k}, \psi_{j}\right)_{\gamma}-\left(\alpha_{r a d}, \psi_{j}\right)_{\gamma}.
\tag{119}
$$

The first term on the right side is nonlinear in the basis function, giving a third-rank tensor with indices $j$, $k$ and $\ell$. Note that $\alpha_{rad}$ and $\bar{n}$ are also projected onto $\mathbb{V}_h$ but, because both are material properties (and are therefore independent of the solution), they do not increase the rank of the tensor produced. The term can thus be implemented in a similar manner to the nonlinear drift term discussed in Section 4.3.

The SRH recombination is given by Eq. (62). If we test this term against the standard polynomial basis $\psi_j$ and integrate over $\Omega_{\mathrm{el}}$, we cannot write the result as a tensor, because the SRH term is not a polynomial in the basis functions. Consequently, we integrate using quadrature. For this, we chose Gauss–Lobatto quadrature $^2$ to maximize the order of the polynomials that can be exactly integrated, while maintaining use of the values at the nodes. In particular, for a general function $f$, the use of Gauss–Lobatto quadrature to integrate over the element $s_\gamma$ gives

$$
\int_{s_{\gamma}} f[n(z), p(z)] \psi_{j}(z) \mathrm{d} z=\int_{s_{\gamma}} f\left[\sum_{\ell=1}^{I_{\mathrm{deg}}} n_{\ell} \psi_{\ell}(z), \sum_{\ell=1}^{I_{\mathrm{deg}}} p_{\ell} \psi_{\ell}(z)\right] \psi_{j}(z) \mathrm{d} z
\tag{120}
$$

$$
\approx w_{j} f\left(n_{j}, p_{j}\right),
\tag{121}
$$

where $\{w_j\}_{j=1}^{P_{\mathrm{deg}}+1}$ are the Gauss-Lobatto quadrature weights for the element $s_\gamma$ and $I_{\mathrm{deg}}$ is the degree of integration. A computationally quick way is to use $I_{\mathrm{deg}}=P_{\mathrm{deg}}+1$ quadrature points per element [41, 42] as this does not require interpolation of the solution.

The Auger recombination is given by Eq. (63). As with the SRH term, we cannot write this as a tensor. Either mass-lumping [41] or quadrature [38] must then be used to calculate the integrals formed when the Auger term is incorporated into the HDG method.

### 4.6 Heterojunctions

To implement the jump conditions (71) or (72), we ensure that a node falls at each discontinuity in the material parameters. Every jump in $n(z)$ can be taken into account by redefining the jump operator as

$$
[\![\tau]\!]_{\gamma} \hat{n}_{\gamma}=\left[\left.\tau\right|_{\gamma+1, L} \exp \left(\Delta \chi_{\gamma}\right)-\left.\tau\right|_{\gamma, R}\right] \hat{n}_{\gamma}
\tag{122}
$$

and the difference operator as

$$
<\hat{n}, \zeta \psi_{j}>_{\gamma}=\left.\left(\zeta \psi_{j}\right)\right|_{\gamma, R} \hat{n}_{\gamma}-\left.\left(\zeta \psi_{j}\right)\right|_{\gamma, L} \exp \left(\Delta \chi_{\gamma-1}\right) \hat{n}_{\gamma-1},
\tag{123}
$$

where $\Delta \chi_\gamma$ is the jump in electron affinity $\chi$ across node $\gamma$ and $\zeta$ is a place-holder function. This is equivalent to defining to values of $\hat{n}_\gamma$ at each node, separated in value by the necessary jump induced by the discontinuous electron affinity. Jumps in $p(z)$ can be handled similarly.

### 4.7 Homotopy

In order to aid convergence of the highly nonlinear discrete system, homotopy is employed in our simulation. The fixed charge density $N_{\mathrm{f}}$, recombination rate $R(n,p;z)$, and bandgap non-homogeneity, i.e. $E_g(z)-E_{g,av}$ where $E_{g,av}$ is the mean bandgap, are all multiplied by a constant $\delta_{\mathrm{homo}}$. The simulation is started with $\delta_{\mathrm{homo}}^{(0)}=\delta_{\mathrm{min}}$. Once the simulation is deemed to have converged, a larger value

$$
\delta_{\mathrm{homo}}^{(1)}=\min \left(\delta_{\mathrm{homo}}^{(0)} \varepsilon_{\mathrm{homo}}, 1\right)
\tag{124}
$$

$^2$The interpolation points for the finite-element basis functions are the Gauss–Lobatto points, as discussed in Sec. 4.2.

---

<table>
<thead>
<tr>
<th>Parameter</th>
<th>Symbol</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Bandgap</td>
<td>$E_g$</td>
<td>1.3 V</td>
</tr>
<tr>
<td>Electron affinity</td>
<td>$\chi$</td>
<td>4.5 V</td>
</tr>
<tr>
<td>Conduction-band density of states</td>
<td>$N_c$</td>
<td>$2.22 \times 10^{18}$ cm$^{-3}$</td>
</tr>
<tr>
<td>Valence-band density of states</td>
<td>$N_v$</td>
<td>$1.78 \times 10^{19}$ cm$^{-3}$</td>
</tr>
<tr>
<td>DC relative permittivity</td>
<td>$\varepsilon_{dc}^{0}$</td>
<td>13.6</td>
</tr>
<tr>
<td>Electron mobility</td>
<td>$\mu_{\mathrm{n}}$</td>
<td>100 cm$^2$ V$^{-1}$s$^{-1}$</td>
</tr>
<tr>
<td>Hole mobility</td>
<td>$\mu_{\mathrm{p}}$</td>
<td>25 cm$^2$ V$^{-1}$s$^{-1}$</td>
</tr>
<tr>
<td>SRH lifetime parameter (electrons)</td>
<td>$\tau_{\mathrm{n}}(z)$</td>
<td>$1 \times 10^{-9}$s$^{-1}$</td>
</tr>
<tr>
<td>SRH lifetime parameter (holes)</td>
<td>$\tau_{\mathrm{p}}(z)$</td>
<td>$1 \times 10^{-9}$s$^{-1}$</td>
</tr>
</tbody>
</table>

Table 3: Electrical parameters of CIGS.

is chosen for $\delta_{\text{homo}}$, with $\varepsilon_{\text{homo}} > 1$ as the homotopy damping relaxation rate. Thus, the iteration

$$
\delta_{\mathrm{homo}}^{(\ell+1)}=\min \left(\delta_{\mathrm{homo}}^{(\ell)} \varepsilon_{\mathrm{homo}}, 1\right)
\tag{125}
$$

is employed, full convergence being deemed to occur in the iteration in which $\delta_{\text{homo}}$ becomes equal to unity.

## 5 Numerical Test of HDG Method

As a model test problem to show the behavior of the HDG method (but not to present a solar-cell design), the solar cell was taken to comprise a p-i-n junction made from copper-indium-gallium-(di)selenide (CIGS), as shown in Fig. 1(a). The electrical parameters of CIGS [43] are given in Table 3. For this test problem, the generation rate was taken to be uniform, with $J_{\mathrm{SC}}^{\mathrm{Opt}}=10 \mathrm{~mA} \mathrm{~cm}^{-2}$; thus RCWA results were not used. The $p$-type layer of thickness $L_{\mathrm{p}}=20 \mathrm{~nm}$ was taken to be doped with acceptor atoms with concentration specified via $N_{\mathrm{f}}=-10^{17} \mathrm{~cm}^{-3}$, and the $n$-type layer of thickness $L_{\mathrm{n}}=20 \mathrm{~nm}$ with donor atoms with concentration specified via $N_{\mathrm{f}}=10^{17} \mathrm{~cm}^{-3}$. The undoped $i$-type layer was taken to be $L_{\mathrm{i}}=200 \mathrm{~nm}$ thick; thus, $L_{z}=L_{\mathrm{p}}+L_{\mathrm{i}}+L_{\mathrm{n}}=240 \mathrm{~nm}$. All three layers were taken to be homogeneous. Neither the radiative nor the Auger recombination mechanism was activated for the test problem.

Chiefly, three parameters affect the accuracy of the HDG method: the degree of the interpolating polynomials $P_{\mathrm{deg}}$, the length of each element $d_{z}$, and the degree of quadrature integration $I_{\mathrm{deg}}$. The convergence of the method with respect to each of these parameters was investigated. The parameters used for the convergence study are given in Table 4.

The convergences of the short-circuit current density $J_{\mathrm{SC}}$, the open-circuit voltage $V_{\mathrm{OC}}$, the maximum power $P_{\max }$, and the fill factor $F F$ with respect to $P_{\mathrm{deg}}, d_{z}$, and $I_{\mathrm{deg}}$, were investigated. Figure 4 shows the error in each of four electrical characteristics relative to the value for $P_{\mathrm{deg}}=9$ when $d_{z}=2 \mathrm{~nm}$ and $I_{\mathrm{deg}}=10$. As $P_{\mathrm{deg}}$ increases from 2, each of the four errors is seen to decrease exponentially, with a rate approximately proportional to $\exp \left(-3 P_{\mathrm{deg}}\right)$. This reduction in error is seen to saturate at around $P_{\mathrm{deg}}=5$.

Figure 5 shows the error in each of four electrical characteristics relative to the value for $d_{z}=1 \mathrm{~nm}$ when $P_{\mathrm{deg}}=5$ and $I_{\mathrm{deg}}=10$. As $d_{z}$ decreases from $20 \mathrm{~nm}$, all four errors decrease as $\mathcal{O}\left(d_{z}^{4}\right)$ which is suboptimal.

Finally, Fig. 6 shows the error in each of four electrical characteristics relative to the value for $I_{\mathrm{deg}}=12$ when $P_{\mathrm{deg}}=5$ and $d_{z}=2 \mathrm{~nm}$. As $I_{\mathrm{deg}}$ increases, each error is seen to decrease exponentially, with a rate approximately proportional to $\exp \left(-4 I_{\mathrm{deg}}\right)$. This reduction in error is seen to saturate at around $I_{\mathrm{deg}}=5$.

Thus, Figs. 4-6 show that the short-circuit current density $J_{\mathrm{SC}}$, the open-circuit voltage $V_{\mathrm{OC}}$, the maximum power $P_{\max }$, and the fill factor $F F$, all converge at approximately the same rate with respect to $P_{\mathrm{deg}}$, $d_{z}$, and $I_{\mathrm{deg}}$. The order of convergence is not optimal, as might be expected since we used polynomials of the same degree in all elements.

## 6 Differential Evolution Algorithm for Optimization

The differential evolution algorithm [44] is a gradient-free optimization algorithm suited for maximizing an objective function over a high-dimensional parameter space. Given the objective function $C: \mathbb{S} \rightarrow \mathbb{R}$, where

<table>
<thead>
<tr>
<th>Symbol</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>$P_{\rm deg}$</td>
<td>variable</td>
<td>Degree of Lobatto polynomials</td>
</tr>
<tr>
<td>$N_{\rm zp}$</td>
<td>variable</td>
<td>Number of points in $p$-type layer</td>
</tr>
<tr>
<td>$N_{\rm zi}$</td>
<td>variable</td>
<td>Number of points in $i$-type layer</td>
</tr>
<tr>
<td>$N_{\rm zn}$</td>
<td>variable</td>
<td>Number of points in $n$-type layer</td>
</tr>
<tr>
<td>$I_{\rm deg}$</td>
<td>variable</td>
<td>Nonlinear term integration degree</td>
</tr>
<tr>
<td>$\bar{\tau}_1$</td>
<td>$10^{-3}$</td>
<td>First parameter for hybridization</td>
</tr>
<tr>
<td>$\bar{\tau}_2$</td>
<td>$10^3$</td>
<td>Second parameter for hybridization</td>
</tr>
<tr>
<td>$\delta V$</td>
<td>$0.01$</td>
<td>Maximum step for $V_{\rm ext}$</td>
</tr>
<tr>
<td>$\delta_{\rm min}$</td>
<td>$10^{-2}$</td>
<td>Initial homotopy damping</td>
</tr>
<tr>
<td>$\varepsilon_{\rm homo}$</td>
<td>$1.2$</td>
<td>Homotopy damping relaxation</td>
</tr>
<tr>
<td>$\delta_{\rm num}$</td>
<td>$1$</td>
<td>No. of homotopy attempts</td>
</tr>
<tr>
<td>$\delta_{\rm inc}$</td>
<td>$10$</td>
<td>Homotopy increase on new attempt</td>
</tr>
<tr>
<td>$n_{\rm loop}$</td>
<td>$10$</td>
<td>Maximum number of iterations for Newton's method</td>
</tr>
<tr>
<td>$E_{\rm rel,tol}$</td>
<td>$10^{-4}$</td>
<td>Relative change in state vector allowed</td>
</tr>
<tr>
<td>$E_{\rm abs,tol}$</td>
<td>$10^{-6}$</td>
<td>Absolute change in state vector allowed</td>
</tr>
<tr>
<td>$J_{\rm tol}$</td>
<td>$0.1$</td>
<td>Relative noise allowed in $J$</td>
</tr>
<tr>
<td>$P_{\rm ref}$</td>
<td>$100$</td>
<td>Max iteration to find $P_{\rm max}$</td>
</tr>
<tr>
<td>$P_{\rm tol}$</td>
<td>$10^{-6}$</td>
<td>Allowed variation around $P_{\rm max}$</td>
</tr>
</tbody>
</table>

Table 4: Baseline parameter settings in Sec. 5 for the HDG simulation of the model CIGS p-i-n solar cell in Fig. 1(a). Note that $N_z = N_{\rm zp} + N_{\rm zi} + N_{\rm zn}$. The state vector is the vector of all solution values in the electronic step.

![](./images/867764699754660385_4.jpg)

Figure 4: Relative errors in $P_{\rm max}$, $J_{\rm SC}$, $V_{\rm OC}$, and $FF$ against $P_{\rm deg} \in [2,8]$, when $d_z = 2$ nm and $I_{\rm deg} = 10$.

![](./images/867764699754660385_5.jpg)

Figure 5: Relative errors in $P_{\text{max}}$, $J_{\text{SC}}$, $V_{\text{OC}}$, and $FF$ against $d_z \in [1,20]$ nm, when $P_{\text{deg}} = 5$ and $I_{\text{deg}} = 10$.

![](./images/867764699754660385_6.jpg)

Figure 6: Relative errors in $P_{\text{max}}$, $J_{\text{SC}}$, $V_{\text{OC}}$, and $FF$ against $I_{\text{deg}} \in [1,11]$, when $P_{\text{deg}} = 5$ and $d_z = 2$ nm.

$\mathbb{S} \subset \mathbb{R}^{\tilde{N}}$ is the set of all possible choices of the $\tilde{N}$ input parameters, the DEA starts by selecting $N_{\text{P}}$ points to form an initial population $\mathbf{P}_{0} \subset \mathbb{S}$. The objective function $C$ is evaluated at each of these points, with the results used by DEA in a mutation-recombination-selection process to build a new population $\mathbf{P}_{1} \subset \mathbb{S}$. The objective function is then evaluated at each point of this new population to develop a new population $\mathbf{P}_{2} \subset \mathbb{S}$ in the second mutation-recombination-selection step. This process continues iteratively until the objective function appears to stabilize.

The efficiency $\eta$ defined in Eq. (50) is the appropriate objective function for designing solar cells. Following suggestions in the DEA documentation [44], we fix the crossover fraction as $C_{\text{R}} = 0.6$. The step size $F$ used in the mutation steps is set to be randomly distributed in $[0.5, 1]$ uniformly. Allowing $F$ to vary randomly with each iteration has been termed dither, and its use has been shown to improve convergence for many problems [4].

## 7 Numerical Test of DEA

As a model test problem, solar cell was taken to comprise a p-i-n junction made from CIGS, as shown in Fig. 1(a). The electrical parameters of CIGS [43] are given in Table 3. The $p$-type layer of thickness $L_{\text{p}} =$ 20 nm was taken to be doped with acceptor atoms with concentration specified via $N_{\text{f}} = -10^{17}$ cm$^{-3}$, and the $n$-type layer of thickness $L_{\text{n}} = 20$ nm with donor atoms with concentration specified via $N_{\text{f}} = 10^{17}$ cm$^{-3}$. The thickness $L_{\text{i}}$ of the undoped $i$-type layer was taken as a variable for optimization. All three layers were taken to be homogeneous, with bandgaps $\text{E}_{\text{g,p}}$, $\text{E}_{\text{g,n}}$, and $\text{E}_{\text{g,i}}$ taken to be variables for optimization. Neither the radiative nor the Auger recombination mechanism was activated for the test problem.

The antireflection coating in Fig. 1(a) was ignored. We fixed $L_{\text{m}} = 150$ nm. The period $L_{\text{x}}$ was kept variable. The height $L_{\text{g}}$ and base $\zeta_{\text{g}}L_{\text{x}}$, $\zeta_{\text{g}} \in (0,1)$, of the metallic protuberance in each period were also kept variable. The $\tilde{N} = 7$ parameters chosen to be optimized in our test problem thus are: $L_{\text{x}}$, $L_{\text{g}}$, $\zeta_{\text{g}}$, $L_{\text{i}}$, $\text{E}_{\text{g,p}}$, $\text{E}_{\text{g,n}}$, and $\text{E}_{\text{g,i}}$.

Both the photonic and the electronic steps were implemented. The population number was set as $N_{\text{P}} =$ 100. The remaining parameters used for the optimization algorithm were as described in the previous sections, together with values given in Table 5. These values were chosen to maintain reasonable accuracy, aid convergence for a wide range of solar cell designs, and to allow rapid computation of the efficiency at each step of DEA. These choices resulted in very quick evaluation of $\eta$ at a particular choice of the parameter values in roughly 6 min, with four evaluations running concurrently in MATLAB on a 20-processor (Intel Xeon Gold 61382GHz) Linux (Ubuntu 17.10) computer. The actual time per parameter set depends on the HDG solver (being longer if more homotopy steps are needed).

Figure 7 summarizes the progression of the DEA towards an optimal result. Each of panels (a)-(g) in this figure is a graph of the efficiency $\eta$ as a function of one of the parameters in the optimization. Thus, each point corresponds to a 7-dimensional vector of parameter values used by DEA. The optimal efficiency found is marked by a large red disk. The remaining panel, Fig. 7(h), shows the progress of optimization. In particular it shows the efficiency as a function of DEA step. The optimal values of the seven parameters in this study are given in Table 6 which result in $\eta = 15.7\%$.

## 8 Concluding Remarks

We have presented details of a design tool for optimizing the efficiency of thin-film photovoltaic solar cells. The solar cell can have multiple semiconductor layers in addition to dielectric layers serving as antireflection coatings, passivation layers, and buffer layers. The solar cell is backed by a metallic grating which is periodic along a fixed direction.

The heart of the design tool is a coupled optoelectronic simulation. The photonic step of the simulation delivers the 2D variation of the electron-hole-pair generation rate inside the semiconductor layers of the solar cell. After averaging along the direction of the periodicity of the grating, the electron-hole-pair generation rate becomes the input to the electronic step of the simulation. The chief output of the electronic step is the efficiency of the solar cell. The design tool uses the differential evolution algorithm to determine the dimensions and bandgaps of the semiconductor layers to maximize the efficiency of the solar cell.

<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$N_\text{t}$</td>
      <td>10</td>
      <td>Fourier order for RCWA</td>
    </tr>
    <tr>
      <td>$P_\text{deg}$</td>
      <td>3</td>
      <td>Degree of Lobatto polynomials</td>
    </tr>
    <tr>
      <td>$N_\text{zp}$</td>
      <td>10</td>
      <td>Number of points in $p$-type layer</td>
    </tr>
    <tr>
      <td>$N_\text{zi}$</td>
      <td>50</td>
      <td>Number of points in $i$-type layer</td>
    </tr>
    <tr>
      <td>$N_\text{zn}$</td>
      <td>10</td>
      <td>Number of points in $n$-type layer</td>
    </tr>
    <tr>
      <td>$I_\text{deg}$</td>
      <td>4</td>
      <td>Nonlinear term integration degree</td>
    </tr>
    <tr>
      <td>$\bar{\tau}_1$</td>
      <td>$10^{-6}$</td>
      <td>First parameter for hybridization</td>
    </tr>
    <tr>
      <td>$\bar{\tau}_2$</td>
      <td>$10^6$</td>
      <td>Second parameter for hybridization</td>
    </tr>
    <tr>
      <td>$\delta_\text{min}$</td>
      <td>$10^{-2}$</td>
      <td>Initial homotopy damping</td>
    </tr>
    <tr>
      <td>$\varepsilon_\text{homo}$</td>
      <td>1.1</td>
      <td>Homotopy damping relaxation</td>
    </tr>
    <tr>
      <td>$\delta_\text{num}$</td>
      <td>40</td>
      <td>No. of homotopy attempts</td>
    </tr>
    <tr>
      <td>$\delta_\text{inc}$</td>
      <td>5</td>
      <td>Homotopy increase on new attempt</td>
    </tr>
    <tr>
      <td>$n_\text{loop}$</td>
      <td>40</td>
      <td>Maximum number of iterations for Newton's method</td>
    </tr>
    <tr>
      <td>$E_\text{rel,tol}$</td>
      <td>$10^{-2}$</td>
      <td>Relative change in state vector allowed</td>
    </tr>
    <tr>
      <td>$E_\text{abs,tol}$</td>
      <td>$10^{-4}$</td>
      <td>Absolute change in state vector allowed</td>
    </tr>
    <tr>
      <td>$P_\text{tol}$</td>
      <td>$10^{-3}$</td>
      <td>Allowed variation around $P_\text{max}$</td>
    </tr>
    <tr>
      <td>$t_\text{max}$</td>
      <td>300 s</td>
      <td>Maximum computer time</td>
    </tr>
  </tbody>
</table>

Table 5: Baseline parameter settings for DEA optimization in Sec. 7. These are laxer than those used in Sec. 5 as rapid computation is necessary. Other settings are the same as in Table 4.

<table>
  <thead>
    <tr>
      <th>Variable Parameter</th>
      <th>Optimal Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>$L_\text{x}$</td>
      <td>632 nm</td>
    </tr>
    <tr>
      <td>$L_\text{g}$</td>
      <td>167 nm</td>
    </tr>
    <tr>
      <td>$\zeta_\text{g}$</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td>$L_\text{i}$</td>
      <td>596 nm</td>
    </tr>
    <tr>
      <td>$\text{E}_\text{g,p}$</td>
      <td>1.62 V</td>
    </tr>
    <tr>
      <td>$\text{E}_\text{g,i}$</td>
      <td>1.467 V</td>
    </tr>
    <tr>
      <td>$\text{E}_\text{g,n}$</td>
      <td>1.618 V</td>
    </tr>
  </tbody>
</table>

Table 6: Parameters varied in the optimal design study described in Sec. 6. The optimal value refers to the value at the end of the DEA computation.

The design tool can be augmented to incorporate a biperiodic metallic grating at the cost of increased computation time [8]. Whether biperiodicity should be incorporated will depend on the consequent aug- mentation of the efficiency of the solar cell, and is therefore a matter of further research. Given that the period of the grating is in the 400-to-1000 nm range in order to invoke guided-wave phenomena for increased photon trapping [8, 9, 45, 46, 47, 48] but the electronic step is electrostatic in character, the averaging of the electron-hole-pair generation rate delivered by the photonic step along the periodicity directions of the grating is appropriate; elimination of that averaging will significantly increase computational time without significant gain in the electronic step.

We have begun to apply the design tool for diverse types of thin-film photovoltaic solar cells and will report our results in due course of time.

## Acknowledgements

A. Lakhtakia thanks the Charles Godfrey Binder Endowment at the Pennsylvania State University for ongoing support of his research. The research of T. H. Anderson, B. J. Civiletti, and P. B. Monk was partially supported by the US National Science Foundation under grant number DMS-1619904. The research of A. Lakhtakia was partially supported by US National Science Foundation under grant number DMS-1619901.

## References

## References

[1] J. Nelson, *The Physics of Solar Cells*, Imperial College Press, London, United Kingdom, 2003.

[2] S. J. Fonash, *Solar Cell Device Physics, 2nd ed*, Academic Press,, Burlington, MA, USA, 2010.

[3] R. Storn and K. Price, "Differential evolution—a simple and efficient heuristic for global optimization over continuous spaces," *J. Global Optim.* **11**, pp. 341-359, 1997.

[4] S. Das and P. N. Suganthan, "Differential evolution: A survey of the state-of-the-art," *IEEE Trans. Evol. Comput.* **15**, pp. 4-31, 2011.

[5] P. Lalanne and G. M. Morris, "Highly improved convergence of the coupled-wave method for TM polarization," *J. Opt. Soc. Am. A* **13**, pp. 779-784, 1996.

[6] P. Lalanne, "Convergence performance of the coupled-wave and the differential methods for thin grat- ings," *J. Opt. Soc. Am. A* **14**, pp. 1583-1591, 1997.

[7] J. A. Polo Jr., T. G. Mackay, and A. Lakhtakia, *Electromagnetic Surface Waves: A Modern Perspective*, Elsevier, Waltham, MA, USA, 2013.

[8] B. J. Civiletti, T. H. Anderson, F. Ahmad, P. B. Monk, and A. Lakhtakia, "Optimization approach for optical absorption in three-dimensional structures including solar cells," *Opt. Eng.* **57**, art. no. 057101, 2018.

[9] F. Ahmad, T. H. Anderson, B. J. Civiletti, P. B. Monk, and A. Lakhtakia, "On optical-absorption peaks in a nonhomogeneous thin-film solar cell with a two-dimensional periodically corrugated metallic backreflector," *J. Nanophotonics* **12**, art. no. 016017, 2018.

[10] D. Brinkman, K. Fellner, P. A. Markowich, and M.-T. Wolfram, "A drift-diffusion-reaction model for excitonic photovoltaic bilayers: Asymptotic analysis and a 2-D HDG finite-element scheme," *Math. Models Methods Appl. Sci.* **23**, pp. 839-872, 2013.

[11] C. Lehrenfeld, *Hybrid Discontinuous Galerkin Methods for Solving Incompressible Flow Problems*, Diplomingenieur Thesis, Rheinisch-Westfaälischen Technischen Hochschule, Aachen, Germany, 2010.

[12] B. Cockburn, J. Gopalakrishnan, and R. Lazarov, "Unified hybridization of discontinuous Galerkin, mixed, and continuous Galerkin methods for second order elliptic problems," *SIAM J. Numer. Anal.* **47**, pp. 1319-1365, 2009.

[13] G. Fu, W. Qiu, and W. Zhang, "An analysis of HDG methods for convection-dominated diffusion problems," *ESAIM: Math. Model. Numer. Anal.* **49**, pp. 225-256, 2015.

[14] Y. Jaluria, *Computer Methods for Engineering*, Taylor & Francis, Washington, DC, USA, 1996.

[15] T. H. Anderson, T. G. Mackay, and A. Lakhtakia, "Enhanced efficiency of Schottky-barrier solar cell with periodically nonhomogeneous indium gallium nitride layer," *J. Photon. Energy* **7**, art. no. 014502, 2017.

[16] Z. Chen, *Finite Element Methods and Their Applications*, Springer, Berlin, Germany, 2005.

[17] T. H. Anderson, A. Lakhtakia, and P. B. Monk, "Optimization of nonhomogeneous indium-gallium- nitride Schottky-barrier thin-film solar cells," *J. Photon. Energy* **8**, art. no. 034501, 2018.

[18] J. Krč and M. Topič, *Optical Modeling and Simulation of Thin-Film Photovoltaic Devices*, CRC Press, Boca Raton, FL, USA, 2013.


[19] N. Saiprasad, S. Castelletto, and A. Boretti, "Optoelectronics modelling of thin film solar cells," in *Nonlinear Approaches in Engineering Applications*, R. N. Jazar and L. Dai, eds., pp. 331-350, Springer, Cham, Switzerland, 2016.

[20] D. Alonso-Álvarez, T. Wilson, P. Pearce, M. Fuührer, D. Farrell, and N. Ekins-Daukes, "Solcore: a multi-scale, Python-based library for modelling solar cells and semiconductor materials," *J. Comput. Electron.* **17**, pp. 1099-1123, 2018.

[21] J. W. Goodman, *Introduction to Fourier Optics*, McGraw-Hill, New York, NY, USA, 1968.

[22] D. Maystre (ed), *Selected Papers on Diffraction Gratings*, SPIE Optical Engineering Press, Bellingham, WA, USA, 1992.

[23] M. G. Moharam, D. A. Pommet, E. B. Grann, and T. K. Gaylord, "Stable implementation of the rigorous coupled-wave analysis for surface-relief gratings: enhanced transmittance matrix approach," *J. Opt. Soc. Am. A* **12**, pp. 1077-1086, 1995.

[24] M. E. Solano, M. Faryad, A. Lakhtakia, and P. B. Monk, "Comparison of rigorous coupled-wave ap- proach and finite element method for photovoltaic devices with periodically corrugated metallic back- reflector," *J. Opt. Soc. Am. A* **31**, pp. 2275-2284, 2014.

[25] M. V. Shuba, M. Faryad, M. E. Solano, P. B. Monk, and A. Lakhtakia, "Adequacy of the rigorous coupled-wave approach for thin-film silicon solar cells with periodically corrugated metallic backreflec- tors: spectral analysis," *J. Opt. Soc. Am. A* **32**, pp. 1222-1230, 2015.

[26] Z. Lokar, B. Lipovsek, M. Topic, and J. Krc, "Performance analysis of rigorous coupled-wave analysis and its integration in a coupled modeling approach for optical simulation of complete heterojunction silicon solar cells," *Beilstein J. Nanotechnol.* **9**, pp. 2315-2329, 2018.

[27] L. Li, "Use of Fourier series in the analysis of discontinuous periodic structures," *J. Opt. Soc Am. A* **13**, pp. 1870-1876, 1996.

[28] National Renewable Energy Laboratory, "Reference Solar Spectral Irradiance: Air Mass 1.5." http: //rredc.nrel.gov/solar/spectra/am1.5/ (5 June 2018).

[29] R. Dewan, M. Marinkovic, R. Noriega, S. Phadke, A. Salleo, and D. Knipp, "Light trapping in thin-film silicon solar cells with submicron surface texture," *Opt. Exp.* **17**, pp. 23058-23065, 2009.

[30] M. Solano, M. Faryad, A. S. Hall, T. E. Mallouk, P. B. Monk, and A. Lakhtakia, "Optimization of the absorption efficiency of an amorphous-silicon thin-film tandem solar cell backed by a metallic surface- relief grating," *Appl. Opt.* **52**, pp. 966-979, 2013; erratum: **54**, p. 398, 2015.

[31] N. Anttu, V. Dagytė, X. Zeng, G. Otnes, and M. Borgström, "Absorption and transmission of light in III-V nanowire arrays for tandem solar cell applications," *Nanotechnology* **28**, art. no. 205203, 2017.

[32] J. Schöberl, "Netgen/Ngsolv." https://ngsolve.org (5 June 2018).

[33] M. Ainsworth, J. Z. Zhu, A. W. Craig, and O. C. Zienkiewicz, "Analysis of the Zienkiewicz-Zhu *a- posteriori* error estimator in the finite element method," *Int. J. Numer. Math. Eng.* **28**, pp. 2161-2174, 1989.

[34] Z. Chen and H. Wu, "An adaptive finite element method with perfectly matched absorbing layers for the wave scattering by periodic structures," *SIAM J. Numer. Anal.* **41**, pp. 799-826, 2003.

[35] F. Brezzi, L. D. Marini, S. Micheletti, P. Pietra, R. Sacco, and S. Wang, "Discretization of semiconduc- tor device problems (I)," in *Handbook of Numerical Analysis: Numerical Methods for Electrodynamic Problems*, W. H. A. Schilders and E. J. W. ter Maten, eds., pp. 317-342, Elsevier, Amsterdam, The Netherlands, 2005.

[36] D. H. Foster, T. Costa, M. Peszynska, and G. Schneider, "Multiscale modeling of solar cells with interface phenomena," *J. Coupled Sys. Multiscale Dynam.* **1**, pp. 179-204, 2013.

[37] K. Yang, J. R. East, and G. I. Haddad, "Numerical modeling of abrupt heterojunctions using a thermionic-field emission boundary condition," *Solid-State Electron.* **36**, pp. 321-330, 1993.

[38] A. Stroud and D. Secrest, *Gaussian Quadrature Formulae*, Prentice-Hall, Englewood Cliffs, NJ, USA,1973.

[39] E. Isaacson and H. B. Keller, *Analysis of Numerical Methods*, Wiley, New York, NY, USA, 1966.

[40] J. Nocedal and S. J. Wright, *Numerical Optimization*, Springer, New York, NY, USA, 2006.

[41] G. Cohen and S. Pernet, *Finite Element and Discontinuous Galerkin Methods for Transient Wave Equations*, Springer, Dordrecht, The Netherlands, 2017.

[42] J. Douglas Jr. and T. Dupont, "The effect of interpolating the coefficients in nonlinear parabolic Galerkin procedures," *Math. Comput.* **20**, pp. 360-389, 1975.

[43] C. Frisk, C. Platzer-Björkman, J. Olsson, P. Szaniawski, J. T. Wätjen, V. Fjällström, P. Salomé, and M. Edoff, "Optimizing Ga-profiles for highly efficient Cu(In, Ga)Se₂ thin film solar cells in simple and complex defect models," *J. Phys. D: Appl. Phys.* **47**, art. no. 485104, 2014.

[44] "Differential Evolution Algorithm." `www1.icsi.berkeley.edu/~storn/code.html` (6 July 2017).

[45] L. M. Anderson, "Harnessing surface plasmons for solar energy conversion," *Proc. SPIE* **408**, pp. 172-178, 1983.

[46] P. Sheng, A. N. Bloch, and R. S. Stepleman, "Wavelength-selective absorption enhancement in thin-film solar cells," *Appl. Phys. Lett.* **43**, pp. 579-581, 1983.

[47] C. Heine and R. H. Morf, "Submicrometer gratings for solar energy applications," *Appl. Opt.* **34**, pp. 2476-2482, 1995.

[48] T. Khaleque and R. Magnusson, "Light management through guided-mode resonances in thin-film silicon solar cells," *J. Nanophoton.* **8**, art. no. 083995, 2014.

![](./images/867764699754660385_7.jpg)

Figure 7: Projections of the results from DEA optimization study of Sec. 7 onto the plane containing $\eta$ and
(a) $L_x$, (b) $L_g$, (c) $\zeta_g$, (d) $L_i$, (e) $E_{g,p}$, (f) $E_{g,i}$, (g) $E_{g,n}$, and (h) DEA iteration number.