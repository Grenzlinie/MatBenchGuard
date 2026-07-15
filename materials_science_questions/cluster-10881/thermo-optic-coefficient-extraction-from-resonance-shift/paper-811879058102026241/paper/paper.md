# ANALYSIS OF CLADDING MODES IN AN ASYMMETRIC DUAL-CORE FIBER

Florence Y. M. Chan, $^{1}$ Kiyotoshi Yasumoto, $^{1}$ and Enakshi K. Sharma $^{2}$
$^{1}$ Department of Computer Science and Communication Engineering, Kyushu University, Fukuoka 819-0395, Japan; Corresponding author: yasumoto@csce.kyushu-u.ac.jp
$^{2}$ Department of Electronic Science, University of Delhi, South Campus, New Delhi 110021, India

Received 2 June 2008

ABSTRACT: A theoretical analysis of the cladding modes is presented for an asymmetric dual-core fiber that consists of a primary core near the fiber axis and a secondary core. Numerical examples are given to demonstrate that the approximation of a two-layer fiber geometry is in- adequate to describe the accurate modal properties of the cladding modes. It is shown that the field distributions of the cladding modes are dependent on the azimuthal angle under the presence of two cores. The maximum field intensities are located away from the fiber axis with a shift in the local maxima in the primary core toward the secondary core. © 2008 Wiley Periodicals, Inc. Microwave Opt Technol Lett 51: 507-510, 2009; Published online in Wiley Inter- Science (www.interscience.wiley.com). DOI 10.1002/mop.24066

Key words: dual-core fiber; asymmetric configuration; cladding mode

## 1. INTRODUCTION
Dual-core fibers are passive devices commonly developed as wavelength-selective multiplexers, polarization splitters, power- dependent nonlinear couplers, and fiber sensors for use in optical communication and signal-processing systems [1-3]. Along with the mature fiber Bragg grating (FBG) fabrication technology, dual-core fibers incorporating FBGs have been proposed [4]. These couplers rely on the evanescent-field coupling between the core modes and hence the two cores are in close proximity [4] or else the fibers have to be fused tapered [5]. There has been no detailed theoretical analysis on the cladding modes of dual-core fibers because the energy in the cladding is regarded as a loss. Recently, it has been demonstrated that with the inscription of long-period gratings (LPGs) [6], light can be coupled from one core to the other through the cladding mode of a dual-core fiber and that leads to a more compact and robust device [7]. A widely adopted approach for cladding mode analysis in single-core fibers uses an approximation of a two-layer fiber geometry [6, 8] and ignores the presence of the core. However, it has been reported that such a simplified model can lead to incorrect designs of LPGs [8]. In this article, we present a semianalytical approach for the anal- ysis of the cladding modes in a dual-core fiber based on a com- posite dual-core model. Numerical examples are demonstrated to highlight the differences in modal properties obtained using the composite dual-core model and the simplified two-layer fiber model.

## 2. FORMULATION

The cross-section of the composite fiber is shown in Figure 1. Core1 and Core 2 of radii $a_{1}$ and $a_{2}$ and refractive indices $n_{1}$ and $n_{2}$ are embedded in a cladding of radius $a_{3}$ and refractive index $n_{3}$ , which is in turn enclosed by an ambient of infinite extent that has an index of $n_{4}$ . The two cores are centered at local cylindrical coor dinates $(r_{1}, \theta_{1})$ and $(r_{2}, \theta_{2})$ , which are at distances $d_{1}$ and $d_{2}$ in the global coordinate $(r_{0}, \theta_{0})$ centered at the fiber axis. In this article, we focus on the case where one core is located near to the center of the fiber. Such type of dual-core fiber is useful for LPG-based devices because the couplings between the center core and clad- ding modes are large. We use a scalar wave analysis which is adequate for solving the cladding modes in a large diameter fiber with a relatively large cladding/ambient index difference. Using basis functions which satisfy the scalar Helmholtz equations in the cylindrical coordinates $(r_{i}, \theta_{i})$ with i=0,1,2 as shown in Figure1 , the optical field $\varphi(r, \theta)$ in the respective regions of the fiber cross-section area is represented in vectorial form as

$$
\varphi(r, \theta)
= \begin{cases}\Phi_{3}^{T}\left(r_{0}, \theta_{0}\right) \cdot \mathbf{A}+\prod_{3}^{T}\left(r_{1}, \theta_{1}\right) \cdot \mathbf{B}_{1}+\prod_{3}^{T}\left(r_{2}, \theta_{2}\right) \cdot \mathbf{B}_{2} & \text { (region 3) (1a) } \\ \Phi_{1}^{T}\left(r_{1}, \theta_{1}\right) \cdot \mathbf{C}_{1} & \text { (region 1) (1b) } \\ \Phi_{2}^{T}\left(r_{2}, \theta_{2}\right) \cdot \mathbf{C}_{2} & \text { (region 2) (1c) } \\ \Psi_{4}^{T}\left(r_{0}, \theta_{0}\right) \cdot \mathbf{D} & \text { (region 4) (1d) }\end{cases}
$$

with

$$
\Phi_{v}\left(r_{i}, \theta_{i}\right)=\left[J_{m}\left(\kappa_{v} r_{i}\right) e^{i m \theta_{i}}\right](i=0,1,2, v=1,2,3), \quad (2)
$$

$$
\prod_{3}\left(r_{i}, \theta_{i}\right)=\left[Y_{m}\left(\kappa_{3} r_{i}\right) e^{i m \theta_{i}}\right](i=1,2), \quad (3)
$$

$$
\Psi_{4}\left(r_{0}, \theta_{0}\right)=\left[K_{m}\left(\gamma r_{0}\right) e^{i m \theta_{0}}\right] \quad (4)
$$

![](./images/811879058102026241_1.jpg)

Figure 1 Cross-section of a composite fiber comprises two cores of radii $a_{1}$ and $a_{2}$ which are distance d apart

DOI 10.1002/mop
MICROWAVE AND OPTICAL TECHNOLOGY LETTERS / Vol. 51, No. 2, February 2009

$$\mathbf{A}=\left[A_{m}\right], \mathbf{B}_{1}=\left[B_{1 m}\right], \mathbf{B}_{2}=\left[B_{2 m}\right], \quad \mathbf{C}_{1}=\left[C_{1, m}\right],$$
$$\mathbf{C}_{2}=\left[C_{2, m}\right], \mathbf{D}=\left[D_{m}\right] \quad(5)$$

where $\kappa_{v}=k_{0}(n_{v}^{2}-n_{eff }^{2})^{1 / 2}, \gamma=k_{0}(n_{eff }^{2}-n_{4}^{2})^{1 / 2}$ with $k_{0}=2 \pi / \lambda$, $\lambda$ being the wavelength in free space, and $n_{eff }(n_{4} \leq n_{eff } \leq n_{3})$ the effective index of the cladding modes, $J_{m}, Y_{m}$ , and $K_{m}$ are the Bessel, Neumann, and modified Bessel functions of integer order $m$ , and $A_{m}$ to $D_{m}$ are the unknown amplitude coefficients. The vectors in Eq. (1) are defined as column vectors and the superscript $T$ denotes the transpose. The unknown coefficients $A_{m}$ to $D_{m}$ aredetermined from the boundary conditions which require that $\varphi(r, \theta)$ and $(\partial / \partial r) \varphi(r, \theta)$ be continuous at the boundaries $r_{1}=a_{1}, r_{2}$  $=a_{2}$ , and $r_{0}=a_{3}$ . To apply these boundary conditions, the addition theorem for the cylindrical functions is used and the field representations of Eq. (1) in each region are rewritten in terms of the coordinate systems of their respective boundaries. Following a similar analytical procedure as reported in [9], we can express theamplitude vectors $B_{1}, B_{2}, C_{1}$ , and $C_{2}$ in terms of $A$ as follows:

$$\mathbf{B}_{1}=\overline{\mathbf{T}}_{1} \cdot \mathbf{A}, \quad \mathbf{B}_{2}=\overline{\mathbf{T}}_{2} \cdot \mathbf{A}\qquad(6)$$

$$\mathbf{C}_{1}=\mathbf{U}\left(\boldsymbol{\eta}_{10}+\boldsymbol{\alpha}_{12} \overline{\mathbf{T}}_{2}\right) \cdot \mathbf{A}, \quad \mathbf{C}_{2}=\mathbf{V}\left(\boldsymbol{\eta}_{20}+\boldsymbol{\alpha}_{21} \overline{\mathbf{T}}_{1}\right) \cdot \mathbf{A} \quad(7)$$
with

$$\overline{\mathbf{T}}_{1}=\left(\mathbf{I}-\mathbf{T}_{1} \boldsymbol{\alpha}_{12} \mathbf{T}_{2} \boldsymbol{\alpha}_{21}\right)^{-1} \mathbf{T}_{1}\left(\boldsymbol{\eta}_{10}+\boldsymbol{\alpha}_{12} \mathbf{T}_{2} \boldsymbol{\eta}_{20}\right)\qquad(8)$$

$$\overline{\mathbf{T}}_{2}=\left(\mathbf{I}-\mathbf{T}_{2} \boldsymbol{\alpha}_{21} \mathbf{T}_{1} \boldsymbol{\alpha}_{12}\right)^{-1} \mathbf{T}_{2}\left(\boldsymbol{\eta}_{20}+\boldsymbol{\alpha}_{21} \mathbf{T}_{1} \boldsymbol{\eta}_{10}\right)\qquad(9)$$

$$\mathbf{T}_{1}=\left[-\frac{\kappa_{3} J_{m}\left(\kappa_{1} a_{1}\right) J_{m}^{\prime}\left(\kappa_{3} a_{1}\right)-\kappa_{1} J_{m}^{\prime}\left(\kappa_{1} a_{1}\right) J_{m}\left(\kappa_{3} a_{1}\right)}{\kappa_{3} J_{m}\left(\kappa_{1} a_{1}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{1}\right)-\kappa_{1} J_{m}^{\prime}\left(\kappa_{1} a_{1}\right) Y_{m}\left(\kappa_{3} a_{1}\right)} \delta_{m n}\right] \quad(10)$$

$$\mathbf{T}_{2}=\left[-\frac{\kappa_{3} J_{m}\left(\kappa_{2} a_{2}\right) J_{m}^{\prime}\left(\kappa_{3} a_{2}\right)-\kappa_{2} J_{m}^{\prime}\left(\kappa_{2} a_{2}\right) J_{m}\left(\kappa_{3} a_{2}\right)}{\kappa_{3} J_{m}\left(\kappa_{2} a_{2}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{2}\right)-\kappa_{2} J_{m}^{\prime}\left(\kappa_{2} a_{2}\right) Y_{m}\left(\kappa_{3} a_{2}\right)} \delta_{m n}\right] \quad(11)$$

$$\mathbf{U}=\left[\frac{\kappa_{3} J_{m}\left(\kappa_{3} a_{1}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{1}\right)-\kappa_{3} J_{m}^{\prime}\left(\kappa_{3} a_{1}\right) Y_{m}\left(\kappa_{3} a_{1}\right)}{\kappa_{3} J_{m}\left(\kappa_{1} a_{1}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{1}\right)-\kappa_{1} J_{m}^{\prime}\left(\kappa_{1} a_{1}\right) Y_{m}\left(\kappa_{3} a_{1}\right)} \delta_{m n}\right] \quad(12)$$

$$\mathbf{V}=\left[\frac{\kappa_{3} J_{m}\left(\kappa_{3} a_{2}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{2}\right)-\kappa_{3} J_{m}^{\prime}\left(\kappa_{3} a_{2}\right) Y_{m}\left(\kappa_{3} a_{2}\right)}{\kappa_{3} J_{m}\left(\kappa_{2} a_{2}\right) Y_{m}^{\prime}\left(\kappa_{3} a_{2}\right)-\kappa_{2} J_{m}^{\prime}\left(\kappa_{2} a_{2}\right) Y_{m}\left(\kappa_{3} a_{2}\right)} \delta_{m n}\right] \quad(13)$$

$$\left[\boldsymbol{\alpha}_{12}\right]_{n m}=Y_{n-m}\left(\kappa_{3} d\right), \quad\left[\boldsymbol{\alpha}_{21}\right]_{n m}=(-1)^{n-m} Y_{n-m}\left(\kappa_{3} d\right) \quad(14)$$

$$\left[\boldsymbol{\eta}_{10}\right]_{n m}=J_{n-m}\left(\kappa_{3} d_{1}\right), \quad\left[\boldsymbol{\eta}_{01}\right]_{n m}=(-1)^{n-m} J_{n-m}\left(\kappa_{3} d_{1}\right)$$

$$\left[\boldsymbol{\eta}_{20}\right]_{n m}=(-1)^{n-m} J_{n-m}\left(\kappa_{3} d_{2}\right), \quad\left[\boldsymbol{\eta}_{02}\right]_{n m}=J_{n-m}\left(\kappa_{3} d_{2}\right)$$

where $\alpha_{i j}$ and $\eta_{i j}$ denote the translation matrices for converting the cylindrical functions from coordinate $(r_{j}, \theta_{j})$ to $(r_{i}, \theta_{i})$ , which arevalid for $r_{1}<d_{1}$ and $d_{2}<r_{2}<d, I$ is the unit matrix, and $\delta_{m n}$  is Kronecker's delta. Applying these relations to Eq. (1a), we obtain

$$\varphi_{3}(r, \theta)=\left[\Phi_{3}^{T}\left(r_{0}, \theta_{0}\right)+\prod_{3}^{T}\left(r_{0}, \theta_{0}\right) \cdot \overline{\mathbf{T}}_{0}\right] \cdot \mathbf{A}\left(\text { for } r_{0}>d_{1}, d_{2}\right) \quad(15)$$
where

$$\overline{\mathbf{T}}_{0}=\boldsymbol{\eta}_{01} \overline{\mathbf{T}}_{1}+\boldsymbol{\eta}_{02} \overline{\mathbf{T}}_{2}.\qquad(16)$$

Applying the boundary conditions at $r_{0}=a_{3}$ to Eqs. (1d) and(15) yields the linear equations for unknown coefficient vectorsA and D:

$$\left(\mathbf{J}+\mathbf{Y} \overline{\mathbf{T}}_{0}\right) \cdot \mathbf{A}=\mathbf{K} \cdot \mathbf{D}\qquad(17)$$

$$\kappa_{3}\left(\mathbf{J}^{\prime}+\mathbf{Y}^{\prime} \cdot \overline{\mathbf{T}}_{0}\right) \cdot \mathbf{A}=\gamma \mathbf{K}^{\prime} \cdot \mathbf{D}\qquad(18)$$
with
$$\begin{aligned}
\mathbf{J}=\left[J_{m}\left(\kappa_{3} a_{3}\right) \delta_{m n}\right], \quad \mathbf{Y}=\left[Y_{m}\left(\kappa_{3} a_{3}\right) \delta_{m n}\right], & \\
& \mathbf{K}=\left[K_{m}\left(\gamma a_{3}\right) \delta_{m n}\right] \quad(19)
\end{aligned}$$

$$\mathbf{J}^{\prime}=\left[J_{m}^{\prime}\left(\kappa_{3} a_{3}\right) \delta_{m n}\right], \quad \mathbf{Y}^{\prime}=\left[Y_{m}^{\prime}\left(\kappa_{3} a_{3}\right) \delta_{m n}\right], \quad \mathbf{K}^{\prime}=\left[K_{m}^{\prime}\left(\gamma a_{3}\right) \delta_{m n}\right].$$

Using Eqs. (17) and (18) the eigenvalue equation for solving the cladding-mode indices $n_{eff }$ is obtained as
$$\left|\mathbf{F}+\overline{\mathbf{T}}_{0}\right|=0\qquad(20)$$
with
$$\mathbf{F}=\left[\frac{J_{m}^{\prime}\left(\kappa_{3} a_{3}\right)\left\{\tilde{K}_{m}\left(\gamma a_{3}\right)-\tilde{J}_{m}\left(\kappa_{3} a_{3}\right)\right\}}{Y_{m}^{\prime}\left(\kappa_{3} a_{3}\right)\left\{\tilde{K}_{m}\left(\gamma a_{3}\right)-\tilde{Y}_{m}\left(\kappa_{3} a_{3}\right)\right\}} \delta_{m n}\right].\qquad(21)$$

$$\begin{aligned}
\tilde{J}_{m}\left(\kappa_{3} a_{3}\right)=\frac{J_{m}\left(\kappa_{3} a_{3}\right)}{\kappa_{3} J_{m}^{\prime}\left(\kappa_{3} a_{3}\right)}, \quad \tilde{Y}_{m}\left(\kappa_{3} a_{3}\right) & =\frac{Y_{m}\left(\kappa_{3} a_{3}\right)}{\kappa_{3} Y_{m}^{\prime}\left(\kappa_{3} a_{3}\right)} \\
\tilde{K}_{m}\left(\gamma a_{3}\right) & =\frac{K_{m}\left(\gamma a_{3}\right)}{\gamma K_{m}^{\prime}\left(\gamma a_{3}\right)}. \quad(22)
\end{aligned}$$

$$\mathbf{D}=\mathbf{K}^{-1}\left(\mathbf{J}+\mathbf{Y} \overline{\mathbf{T}}_{0}\right) \cdot \mathbf{A}.\qquad(23)$$

Once the value of $n_{eff }$ is determined from Eq. (20), the field distribution of the cladding modes of the dual-core fiber can be evaluated from Eqs. (1), (6), (7), and (23) using a proper normal- ization condition with the coefficient vector $A$ . When $n_{1}=n_{3}$ and d2 = 0, it follows from Eqs. (8), (10)-(12), (14), and (16) that $T_{1}=\overline{T}_{1}=0, \eta_{20}=\eta_{02}=I$ , and $\overline{T}_{0}=\overline{T}_{2}=T_{2}$ . In this case, Eq. (20) reduces to the eigenvalue equation of a three-layer single- core fiber as reported in [8].
As a numerical example, we take $n_{1}=n_{2}=1.4530, n_{3}$  $=1.4440$ (pure silica), $n_{4}=1.0$ (air), $a_{1}=3.0 \mu m, a_{2}$  $=3.6 \mu m, a_{3}=62.5 \mu m, d_{1}=32 \mu m$ , and $d_{2}=0$ . The truncation order $m$ in the cylindrical wave expansions given by Eq.(1) should be large enough [9] to give convergent solutions for the mode indices $n_{eff }$ and continuous field profiles across the interfaces $r_{1}=a_{1}, r_{1}=a_{1}, r_{2}=a_{2}$ , and $r_{0}=a_{3}$ . Here, we have truncated the expansions by $m= \pm 12$ , which yields $n_{eff }$ to an accuracy of up to 6 decimal places. The cladding modes in a symmetric single-core fiber are usually referred to as $LP_{0 n}(n \geq 2)$ modes. These $LP_{0 n}$ cladding modes are perturbed in the presence of asymmetric dual cores and the mode field distribution has no axially symmetric property. We shall designate here the perturbed mode with the effective index closest to that of the $LP_{0 n}$ mode as the $LP_{0 n}^{\prime}$ mode.
The three-dimensional field profile of the $LP_{03}^{\prime}$ mode at $\lambda$ = 1.550 um is plotted in Figure 2. Because of the asymmetric property of the cross-section, the field intensities are dependent on the azimuthal angle $\theta_{0}$ for all cladding modes. The normalized fieldprofile of the dual-core fiber along the azimuthal direction $\theta_{0}$  $=0$ and $\pi$ is shown in Figure 3 for the $LP_{03}^{\prime}$ mode at $\lambda$ = 1.550 um and compared with that of LP, mode obtained using a two-layer fiber model, namely, a coreless fiber approximation.


![](./images/811879058102026241_2.jpg)

Figure 2 3D field profile of the $LP_{03}'$ mode at $\lambda = 1.550\ \mu$m for the dual-core fiber with $d_2 = 0$, showing a nonuniform azimuthal intensity distribution. [Color figure can be viewed in the online issue, which is available at www.interscience.wiley.com]

As shown in Figure 3, the maximum field intensity for the dual-core fiber is located away from the fiber axis. In Core 2, the local maximum intensity indicates a shift towards Core 1. This is because the presence of Core 1 increases the average refractive index over one side of the fiber. Figure 4 shows the normalized field profiles of the dual-core fiber along the azimuthal direction $\theta_0 = 0$ and $\pi$ at $\lambda = 1.550\ \mu$m for the $LP_{03}'$, $LP_{04}'$, and $LP_{06}'$ modes which correspond to the $LP_{03}$, $LP_{04}$, and $LP_{06}$ modes of a single-core fiber. Their effective indices $n_{\text{eff}}$ are calculated to be 1.44380171, 1.44351011, and 1.44258249 from Eq. (20), while the respective values for the coreless fiber are 1.44362264, 1.44327905, and 1.44227425, respectively. The effective indices of the dual-core fiber are larger than those of the coreless fiber because the inclusion of the cores increases the average index of the cladding. The shift in the local maximum intensity in Core 2 becomes less pronounced as the mode order increases. By introducing a finite offset distance $d_2$, the location of the local maximum intensity in Core 2 can be shifted along the direction $\theta_0 = 0$. The normalized field profiles of the $LP_{03}'$ mode along the azimuthal direction $\theta_0 = 0$ and $\pi$ at $\lambda = 1.550\ \mu$m are shown in Figure 5 for $d_2 = 0$, 1, and $2\ \mu$m. It is seen that the location of the local maximum almost coincides with the fiber axis when $d_2 = 2\ \mu$m.

![](./images/811879058102026241_3.jpg)

Figure 3 Radial field profiles of the $LP_{03}'$ mode along $\theta_0 = 0$ and $\pi$ at $\lambda = 1.550\ \mu$m for the dual-core fiber with $d_2 = 0$ and the coreless fiber

![](./images/811879058102026241_4.jpg)

Figure 4 Radial field profiles of the dual-core fiber with $d_2 = 0$ along $\theta_0 = 0$ and $\pi$ at $\lambda = 1.550\ \mu$m for the $LP_{03}'$, $LP_{04}'$, and $LP_{06}'$ modes

In conclusion, we have presented a semianalytical approach for solving the cladding modes of an asymmetric dual-core fiber, which consists of a primary core near the fiber axis and a secondary core. The effective indices and field profiles of the cladding modes obtained from the composite dual-core model are different from those obtained by using the coreless fiber approximation, despite the core radii are significantly smaller than the cladding radius. The effective indices slightly increase because of the inclusion of two cores with higher indices. The maximum field intensities are deviated from the fiber axis while the local maxima in the primary core shift toward the secondary core. The present analysis provides insights into the characteristics of asymmetric dual-core fibers and may be useful for the design of LPG-based devices which need the phase matching and overlap of mode fields between the core and cladding modes under an inscribed LPG.

## ACKNOWLEDGMENTS
This work was supported by a grant from the 2008 Japan-Indo Collaboration Project on *"Infrastructural Communication Technologies Supporting Fully Ubiquitous Information Society,"* Ministry of Education, Culture, Sports, Science, and Technology, Japan.

![](./images/811879058102026241_5.jpg)

Figure 5 Radial field profiles of the $LP_{03}'$ mode along $\theta_0 = 0$ and $\pi$ at $\lambda = 1.550\ \mu$m for $d_2 = 0$, 1, and $2\ \mu$m, showing a shift in the local maximum

## REFERENCES
1. K. Kitayama and Y. Ishida, Wavelength-selective coupling of two-core optical fiber: Application and design, J Opt Soc Am A 2 (1985), 90-94.
2. G.D. Peng, T. Tjugiarto, and P.L. Chu, Polarisation beam splitting using twin-elliptic-core optical fibres, Electron Lett 10 (1990), 682-683.
3. S.R. Friberg, Y. Silberberg, M.K. Oliver, M.J. Andrejco, M.A. Saifi, and P.W. Smith, Ultrafast all-optical switching in a dual-core fiber nonlinear coupler, Appl Phys Lett 51 (1987), 1135-1137.
4. A.C. Jacob-Poulin, R. Vallée, S. LaRochelle, D. Faucher, and G.R. Atkins, Channel-dropping filter based on grating-frustrated two core fiber, J Lightwave Technol 18 (2000), 715-720.
5. R. Matsumoto, S. Yamasaki, T. Sakai, K. Nishide, and R. Yamauchi, Optical fiber filters using twin core fibers, Proc. APCC/OECC'99 2 (1999), 1616-1618.
6. A.M. Vengsarkar, P.J. Lemaire, J.B. Judkins, V. Bhatia, T. Erdogan, and J.E. Sipe, Long-period fiber gratings as band-rejection filters, J Lightwave Technol 14 (1996), 58-65.
7. F.Y.M. Chan and K. Yasumoto, Design of wavelength tunable long-period grating couplers based on asymmetric nonlinear dual-core fibers, Opt Lett 32 (2007), 3376-3378.
8. R. Singh, H. Kumar, and E.K. Sharma, Design of long-period gratings: Necessity of a three-layer fiber geometry for cladding mode characteristics, Microwave Opt Technol Lett 37 (2003), 45-49.
9. H. Toyama and K. Yasumoto, Electromagnetic scattering from a dielectric cylinder with multiple eccentric cylindrical inclusions, Prog Electromagn Res PIERS 40 (2003), 113-129.

© 2008 Wiley Periodicals, Inc.
