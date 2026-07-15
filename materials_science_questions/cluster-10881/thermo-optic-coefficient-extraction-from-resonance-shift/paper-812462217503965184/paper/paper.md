# Theoretical and Experimental Analysis of Thermal Stress Effects on Modal Polarization Properties of Highly Birefringent Optical Fibers

Marie Fontaine, Binruo Wu, Velko P. Tzolov, Wojtek J. Bock, and Waclaw Urbanczyk

Abstract-A theoretical and experimental analysis of thermal stress effects on the modal polarization properties of highly elliptical-core fibers is presented. The theoretical analysis is based on solving the vectorial Maxwell's equations, using a finite-element scheme, when form-induced and stress-induced effects are introduced simultaneously through appropriate calculation of the refractive indexes of the anisotropic media. The experimental analysis is done by studying the temperature response of a white-light interferometric sensor employing highly elliptical-core fibers. The calculated temperature sensitivities of the modal birefringence and the polarization mode dispersion in highly elliptical-core fiber are in close agreement with the experimental results. Interpretation of the results useful for designing white-light interferometric sensors composed of highly elliptical-core fibers is also given.

## I. INTRODUCTION

T HAS BEEN shown that polarimetric and interferometric fiber-optic sensing devices composed of highly birefringent (HB) fibers are very effective for precisely registering a variety of measurands including temperature, strain and hydrostatic as well as axial pressure [1], [22]. The potential advantages of using sensors of these types for stress measurements, especially in noisy and harsh environments such as those encountered in civil engineering, are impressive: immunity to electromagnetic interference, suitability for adverse environments, and compatibility with optical fiber data transmission systems.

The newly emerging class of white-light interferometric sensors offers some additional important advantages over their polarimetric and classical interferometric counterparts [3], [4]. The white-light interferometric sensors make possible:
1) determination of the absolute value of the measurand (not only its relative value) in a practically unlimited range, by registering the measurand-induced displacement of the contrast function and
2) coherence multiplexing of single-point sensors into larger systems, by simultaneous detecting of displacements of several sensor contrast functions. In this class of sensors, the value of the measurand can be determined either from the measurand-induced displacement of the coherence function or from displacement of the individual interference fringes.

The displacement of the contrast function is proportional to the measurand-induced change in the polarization mode dispersion (PMD) $\tau$, while the displacement of the individual interference fringes is proportional to the change in the modal birefringence $B$. Therefore, when using the white-light interferometric techniques in sensor applications, it is of crucial importance to have knowledge of the relative sensitivity of $B$ and $\tau$ to the measurand $X$ defined, respectively, as

$$
S_{X}^{B}=\frac{\partial \ln (B)}{\partial X} \tag{1}
$$

and

$$
S_{X}^{\tau}=\frac{\partial \ln (\tau)}{\partial X}. \tag{2}
$$

For interferometric sensors composed of highly dispersive fibers, like highly elliptical-core (HEC) fibers, the relative sensitivities $S_{X}^{B}$ and $S_{X}^{\tau}$ to a given measurand $X$ can be different. For this reason, both sensitivities to the measurand $X$ have to be known in designing a single-point sensor or a system based on such sensors. Additionally, in the process of designing any sensor based on HB fibers, one of the most important issues to be solved is how to separate the measurand-induced changes from those induced by environmental temperature fluctuations [5]. Among the techniques to achieve this goal are 1) temperature-compensation by the cross-splicing method and 2) simultaneous determination of the value of the measurand and the ambient temperature (two-parameter sensing). However, for an effective temperature-compensation, the relative sensitivity of modal birefringence and PMD to the temperature changes must be precisely known.

The main objective of this article is to present a method for theoretical modeling of the temperature sensitivity of the modal birefringence $(S_{T}^{B})$ and modal polarization dispersion $(S_{T}^{\tau})$ of HEC fibers frequently employed as a sensing elements in white-light interferometric sensors. The theoretical results, obtained by using an exact approach based on the solution of the vectorial Maxwell equations, are compared with the measurements of $S_{T}^{B}$ and $S_{T}^{\tau}$ obtained by studying the temperature response of white-light interferometric sensors employing HEC fibers. Both the theoretical and experimental results are in close agreement and show clearly that the relative

Manuscript received October 13, 1995. This work was supported by the Natural Sciences and Engineering Research Council of Canada.
M. Fontaine, B. Wu, V. P. Tzolov, and W. J. Bock are with the Université du Québec à Hull, P.Q. J8X 3X7, Canada.
W. Urbanczyk is with the Institute of Physics, Technical University of Wroclaw, Wroclaw 50-370, Poland.
Publisher Item Identifier S 0733-8724(96)02939-8.

0733-8724/96$05.00 © 1996 IEEE

temperature sensitivity of the modal birefringence $S_T^B$ and the polarization mode dispersion $S_T^\tau$ of HEC fibers may be significantly different.

The remainder of the article is organized as follows: in Sec- tion II, we describe a highly accurate and efficient numerical method for solving the vectorial Maxwell's equations, based on a finite-element scheme, which can be used to analyze the polarization characteristics of any types of fibers as a function of various ambient temperature conditions. A brief description of the numerical model used to compute the distribution of the refractive indexes for different ambient temperatures is given. In Section III, the procedure is applied to compute the modal birefringence, polarization dispersion and chromatic dispersion in HEC fibers for a wide range of normalized frequencies. A comparison of the characteristic curves computed with and without thermal stress effects reveals clearly the interplay between the form-induced and stress-induced effects on the polarization properties of fibers. In Sections IV-A and -B, a theoretical and experimental analysis of the relative tempera- ture sensitivity of the modal birefringence and PMD of a HEC (Andrew ET-800) fiber, recently used as a sensing element in white-light interferometric strain and pressure sensors, are presented respectively. Section V provides a summary and conclusion.

## II. NUMERICAL PROCEDURE FOR SOLVING THE MAXWELL'S EQUATIONS

Most models used to date to investigate temperature ef- fects on the polarization properties of fibers are based on a first-order perturbation approach [6]-[9]. Birefringence and polarization dispersion are expressed as the sum of two compo- nents: a geometrical component, determined by the noncircular geometrical shape of the core and a material stress component induced by the thermal stresses. For HB fibers like York, bow-tie and Panda fibers, stress-induced effects contribute more significantly to polarization properties than form-induced effects. When investigating the polarization properties of such fibers, the geometrical and material stress components can be analyzed separately [8]-[10]. For step-profile HEC fibers, the nonuniformity of the refractive indexes and the inhomogeneity of thermal properties are intimately connected through their discontinuity at the interface between the core and the cladding of the fiber. Consequently, the contribution of form-induced and stress-induced effects on the polarization properties of HEC fibers cannot be separated [11]. In this paper, in or- der to avoid the artificial separation between form-induced and stress-induced effects on the polarization properties of HEC fibers, an efficient numerical procedure for solving the vectorial Maxwell's equations is used which simultaneously takes into account the effects of ambient temperature and the geometrical distribution of the refractive indexes of anisotropic propagation media.

### A. Vectorial Maxwell's Equations

In a source-free nondispersive medium, the transverse com- ponents of the electromagnetic field can be written using only longitudinal components $e_z$ and $h_z$ [12]. In this case, solving the vectorial Maxwell's equations is equivalent to solving the following system of coupled differential equations

$$
\begin{aligned}
\frac{\partial}{\partial x} & \left(\left(1+\frac{\beta^{2}}{p_{y}}\right) \frac{\partial e_{z}}{\partial y}-\frac{\beta}{p_{y}} \frac{\partial h_{z}}{\partial x}\right) \\
& -\frac{\partial}{\partial y}\left(\left(1+\frac{\beta^{2}}{p_{x}}\right) \frac{\partial e_{z}}{\partial x}+\frac{\beta}{p_{x}} \frac{\partial h_{z}}{\partial y}\right)-\beta h_{z}=0 \quad (3)
\end{aligned}
$$

and

$$
\begin{aligned}
\frac{\partial}{\partial x} & \left(\left(1+\frac{\beta^{2}}{p_{x}}\right) \frac{\partial e_{z}}{\partial x}+\frac{\beta}{p_{x}} \frac{\partial h_{z}}{\partial y}\right) \\
& +\frac{\partial}{\partial y}\left(\left(1+\frac{\beta^{2}}{p_{y}}\right) \frac{\partial e_{z}}{\partial y}-\frac{\beta}{p_{y}} \frac{\partial h_{z}}{\partial x}\right)+k^{2} n_{z}^{2} e_{z}=0. \text { (4) }
\end{aligned}
$$

In (3) and (4), functions $p_x$ and $p_y$ are defined, respectively, as $k^2n_x^2-\beta^2$ and $k^2n_y^2-\beta^2$. To take into account the geometrical characteristics of the optical fiber and the thermal stress effects, the diagonal components of the dielectric tensor of the anisotropic propagation media $n_x^2$, $n_y^2$, and $n_z^2$ are computed for every point in the cross section of the fiber for different conditions of ambient temperature $T$. The solution of (3) and (4) provides the modal propagation constant $\beta$ as a function of $T$. The procedure for calculating the components $n_x^2(T)$, $n_y^2(T)$, and $n_z^2(T)$ is described below.

To solve the coupled differential (3) and (4), we use a numerical procedure similar to the one we have recently proposed but extended to take into account the temperature effects [13]. The numerical steps for the procedure can be summarized as follows..

- Writing operators on $e_z$ and $h_z$ in (3) and (4) in a matrix form which depends non linearly on the propagation constant $\beta$.
- Solving (3) and (4) by replacing the zero on the right- hand sides of (3) and (4) with random nonzero functions and then solving them as a steady-state problem with a predetermined value of $\beta$.

When $\beta$ is close to an eigenvalue of a guided mode, the determinant of the matrix is nearly equal to zero and the norm of the vector solution becomes very high; the eigenvalues of the system are then the values of $\beta$ which maximize the value of the norm. Any measure of the norm computed as a function of $\beta$ can be used to identify the eigenvalues. In this paper, the integral of the solutions $e_z$ defined, respectively, as $\int_R |e_z|dx dy$ is used. For a given temperature $T$, the sharp peak of the integral of the solutions $e_z$ plotted versus $\beta/k$ in a given range $[\beta_{\text{inf}}/k, \beta_{\text{sup}}/k]$ makes it possible to identify the eigenvalues $\beta_x(T)/k$ and $\beta_y(T)/k$ for the $x$ and $y$ modes of polarization, respectively. In the next paragraph, we briefly describe the model used to compute the components $n_x^2(T)$, $n_y^2(T)$, and $n_z^2(T)$.

### B. Dielectric Tensor Components

When a composite glass fiber is drawn at high temperature from a preform, thermal stresses can develop once the fiber cools through the temperature at which glass sets. In the absence of any axial stress ($\sigma_3=0$), principal refractive

indexes $n_{1}, n_{2}$, and $n_{3}$, corresponding to principal thermal stresses $\sigma_{1}$ and $\sigma_{2}$ are obtained through the usual photoelastic effect as [14]

$$
n_{1}=n+\left[C_{1} \sigma_{1}+C_{2} \sigma_{2}\right] \tag{5}
$$

$$
n_{2}=n+\left[C_{1} \sigma_{2}+C_{2} \sigma_{1}\right] \tag{6}
$$

$$
n_{3}=n+\left[C_{2}\left(\sigma_{2}+\sigma_{1}\right)\right]. \tag{7}
$$

In (5)-(7), the parameter $n$ is the refractive index of the isotropic material of the core or cladding of the fiber. Coefficients $C_{1}$ and $C_{2}$ are the direct and the lateral photoelastic constants (negative), respectively.

Principal stress components $\sigma_{1}$ and $\sigma_{2}$ are determined by [15]

$$
\left[\sigma^{2}-\left(\sigma_{x}+\sigma_{y}\right) \sigma+\left(\sigma_{x} \sigma_{y}-\tau_{x y}^{2}\right)\right]=0 \tag{8}
$$

where

$$
\sigma_{1,2}=\frac{\left(\sigma_{x}-\sigma_{y}\right) \pm\left(\left(\sigma_{x}-\sigma_{y}\right)^{2}+4 \tau_{x y}^{2}\right)^{1 / 2}}{2}. \tag{9}
$$

In this paper, the normal stress components $\sigma_{x}$ and $\sigma_{y}$ and the shear stress component $\tau_{x y}$ are computed using the procedure proposed by Tsai et al. [16]. The thermal stress components are calculated at every point in the cross section of the fiber for various temperature changes $\Delta T$ equal to the difference between room (ambient) temperature $T_{\text {room }}$ and the glass softening temperature $T_{\text {soft }}$.

The calculation of the components of the dielectric tensor for the Cartesian coordinates defined as [17]

$$
[\varepsilon]_{x y z}=[T]^{-1}\left(\begin{array}{ccc}
\left(n_{1}\right)^{2} & 0 & 0 \\
0 & \left(n_{2}\right)^{2} & 0 \\
0 & 0 & \left(n_{3}\right)^{2}
\end{array}\right)[T] \tag{10}
$$

with

$$
[T]=\left(\begin{array}{ccc}
\alpha & \beta & 0 \\
-\beta & \alpha & 0 \\
0 & 0 & 1
\end{array}\right), \tag{11}
$$

$$
\alpha= \pm\left(1-\frac{\tau_{x y}^{2}}{2\left(\sigma_{x}-\sigma_{y}\right)^{2}}\right), \tag{12}
$$

and

$$
\beta= \pm \frac{\tau_{x y}}{\left(\sigma_{x}-\sigma_{y}\right)} \tag{13}
$$

and shows that the outer diagonal components are different from zero essentially only in the region near the interface between the core and the cladding of the fiber and are relatively small compared to the diagonal components. Accordingly, the components $n_{x}^{2}, n_{y}^{2}$, and $n_{z}^{2}$ in (3) and (4) are defined as the diagonal elements of the dielectric tensor, $[\varepsilon]_{x y z}$. The other elements of $[\varepsilon]_{x y z}$ are disregarded. This approximation is equivalent to considering the Cartesian axes nearly parallel to the principal axes of the anisotropic propagation media.

When the thermal stress effect is accounted for, the components $n_{x}, n_{y}$ and $n_{z}$ can be expressed as

$$
n_{i}(x, y, \Delta T)=n^{(0)}(x, y)+\Delta n_{i}(x, y, \Delta T), \quad i=x, y, z \tag{14}
$$

where $n^{(0)}(x, y)$ represents the stress-independent refractive index of the HEC fiber which is solely a function of the core's geometrical shape, and $\Delta n_{i}(x, y, \Delta T)$ is the correction due to temperature effects, expressed as a function of the thermal stress components. Since the numerical values of the components components $n_{x}, n_{y}$, and $n_{z}$ depend on the temperature difference $\Delta T=T_{\text {room }}-T_{\text {soft }}$, the present method can be used to compute and analyze the modal polarization properties of HEC fibers under various temperature conditions for a wide range of normalized frequencies.

## III. INVESTIGATION OF TEMPERATURE EFFECTS ON THE POLARIZATION PROPERTIES OF FIBERS

In this section, the numerical method reported previously is applied to investigate the modal birefringence, polarization dispersion and chromatic dispersion characteristics of highly elliptical-core fibers with and without thermal stress effects in order to highlight temperature effects on their polarization properties.

In addition to the propagation constant, two other physical parameters are used to characterize the propagation modes in fibers: group delay and chromatic dispersion. For HEC fibers, it is useful to normalize these parameters as a function of normalized frequency $V_{\text {ell }}$ defined as

$$
V_{\text {ell }}=k \sqrt{\rho_{x}} \sqrt{\rho_{y}}\left(n_{\mathrm{co}}^{2}-n_{\mathrm{cl}}^{2}\right)^{1 / 2} \tag{15}
$$

where the parameters $n_{\mathrm{co}}$ and $n_{\mathrm{cl}}$ are the stress-independent refractive indexes of the core and the cladding, respectively, while $\rho_{x}$ and $\rho_{y}$ are the major and minor semi-axes of the elliptical-core fiber, respectively. In this case, the difference in the normalized propagation constant $(\Delta b)$, the group delay $(\Delta d$, proportional to PMD $\tau$ ) and the chromatic dispersion $(\Delta g)$ between the $x$ and $y$ polarization modes of HEC fibers defined as [13]

$$
\Delta b=b_{x}-b_{y}=\frac{\beta_{x}^{2}-\beta_{y}^{2}}{k^{2}\left(n_{\mathrm{co}}^{2}-n_{\mathrm{cl}}^{2}\right)}, \tag{16}
$$

$$
\Delta d=d_{x}-d_{y}=\frac{d\left(V_{\mathrm{ell}} \Delta b\right)}{d V_{\mathrm{ell}}}, \tag{17}
$$

$$
\Delta g=g_{x}-g_{y}=V_{\mathrm{ell}} \frac{d^{2}\left(V_{\mathrm{ell}} \Delta b\right)}{d V_{\mathrm{ell}}^{2}} \tag{18}
$$

can be used for analyzing any HEC optical fiber having nearly the same core-cladding index difference, $\Delta n=n_{\mathrm{co}}-n_{\mathrm{cl}}$, and ellipticity $e=\left(\rho_{x} / \rho_{y}\right)$.

The physical parameters of the HEC fiber investigated in this paper are very close to those of the Andrew ET-800 fiber recently used as a sensing element in white-light interferometric strain and pressure sensors [3], [4]: core-cladding

![](./images/812462217503965184_1.jpg)

Fig. 1. Normalized polarization parameters $\Delta b$, $\Delta d$, and $\Delta g$ as a function of the normalized frequency $V_{\text{ell}}$. The dashed line is for the case when the stress effects are disregarded ($\Delta T = 0^\circ\text{C}$) and the solid line for when shape and stress-induced effects are simultaneously taken into account ($\Delta T = -830^\circ\text{C}$). The fiber parameters are: $\Delta n = 0.03$ and $e = 2$.

index difference $\Delta n$, 0.03; ellipticity $e$, 2.0; difference $\Delta\alpha$ between the thermal expansion coefficients of the core and the cladding, $1.585 \times 10^{-6}{^\circ\text{C}}^{-1}$; Young's modulus $E$, $7750\ \text{kg/mm}^2$; Poisson's ratio $\nu$, 0.186; direct photoelastic constant $C_1$, $-6.7 \times 10^{-6}\ \text{kg/mm}^2$; lateral photoelastic constant $C_2$, $-41.1{\times}10^{-6}\ \text{kg/mm}^2$; outer radius $\rho$ of the fiber, 40 $\mu\text{m}$.

Fig. 1 shows the characteristic curves $\Delta b(V_{\text{ell}})$, $\Delta d(V_{\text{ell}})$ and $\Delta g(V_{\text{ell}})$ for the HEC fiber where the temperature difference $\Delta T$ between room temperature and glass softening temperature ($\Delta T = T_{\text{room}} - T_{\text{soft}}$) was set to $-830\ {^\circ\text{C}}$. Fig. 1 indicates clearly that the contribution of thermal stresses to the modal birefringence depends greatly on the normalized frequency. For a low normalized frequency ($V_{\text{ell}} < 1.2$), the difference between $\Delta b$ computed with and without thermal stress is very small, less than $2.5\%$. This can be explained by the fact that, for low values of the normalized frequency $V_{\text{ell}}$, a large part of the electromagnetic field is far from the core region and, as shown by Fig. 2, the stress-induced corrections to the refractive index are very low in this region. For higher values of $V_{\text{ell}}$, an important observation is that stress-induced effects always add positively to the form-induced effects. From Fig. 1, it can be seen that the stress-induced effects cause a difference of up to $50\%$ for $V_{\text{ell}} = 3.25$. The positive contribution of the stress-induced effects to the birefringence can be easily explained using the scalar variational expression of the propagation constant written in terms of the field components [12]. In a first-order approximation, assuming that i) the transverse dependence $\vec{e}_t(x,y)$ of the modal fields on the perturbed (with thermal-stress effects) and unperturbed (without thermal-stress effects) fibers is similar, and ii) the total power $P$ is equally distributed between the $x$ and the $y$ polarization modes, it can be shown that

$$
(\Delta\beta/k)-(\Delta\beta^{(0)}/k)\approx\frac{\int_{A_{\infty}}\left\{(\Delta n_x - \Delta n_y)|\vec{e}_t|^2\right\}dA}{P}. \tag{19}
$$

![](./images/812462217503965184_2.jpg)

Fig. 2. (a) The step refractive index distribution ($\Delta T = 0^\circ\text{C}$) for the same fiber shown in Fig. 1 in a cross-section along the major axis $x(y = 0)$. The stress induced corrections $\Delta n_x$, $\Delta n_y$ and $\Delta n_z$ ($\Delta T = -830^\circ\text{C}$) to the refractive indexes along the principal axes (for the same cross-section) are indentified as (b), (c), and (d), respectively.

In (19), the parameters $\Delta\beta/k$ and $\Delta\beta^{(0)}/k$ represent the modal birefringence of the perturbed and unperturbed systems, respectively. As shown in Fig. 2, in the core region, corrections to the refractive indexes $\Delta n_x^{\text{co}}$ and $\Delta n_y^{\text{co}}$ are always negative. However, the difference $(\Delta n_x - \Delta n_y)$ is always positive since $|\Delta n_x^{\text{co}}| < |\Delta n_y^{\text{co}}|$. In the cladding region, $\Delta n_x^{\text{cl}}$ is positive while $\Delta n_y^{\text{cl}}$ is negative and the difference $(\Delta n_x - \Delta n_y)$ is also positive. Accordingly, at room temperature, the modal birefringence is always greater than the birefringence predicted theoretically from geometrical effects alone.

The difference between the normalized group delay $\Delta d$ computed with and without thermal stress is even more significant. Close to the cut-off frequency ($V_{\text{ell}} \approx 2.4$), results indicate that the group delay computed without temperature effects is only $15\%$ of that computed with both form-and stress-induced effects. At room temperature, for the whole range of the normalized frequency $V_{\text{ell}}$, the group delay is always positive. This means that the fast and the slow axes are never interchanged as would have been expected from the

characteristics curves of the group delay computed by taking into account form-induced effects alone [13]. In addition, the normalized chromatic dispersion curve $\Delta g$ displays a signifi cant shift of the zero dispersion wavelength, a parameter which is of crucial importance for investigating pulse propagation in both linear and nonlinear propagation regimes.

## IV. TEMPERATURE SENSITIVITY OF HEC FIBER
In this section, we investigate the relative temperature sensi- tivity of modal birefringence and polarization mode dispersion of the HEC (Andrew ET-800) fiber analyzed in the previous section.

### A. Theoretical Analysis
To theoretically investigate the relative temperature sen- sitivity of modal birefringence $S_{T}^{B}$ and polarization mode dispersion $S_{T}^{\tau}$ , defined, respectively, by (1) and (2), the modal birefringence
$$
B=\frac{\lambda}{2 \pi}\left(\beta_{x}-\beta_{y}\right) \quad(20)
$$
and PMD
$$
\tau=\frac{1}{c}\left(B-\left[\lambda \frac{d B}{d \lambda}\right]_{\lambda=\lambda_{0}}\right) \quad(21)
$$
are computed for various ambient temperatures $T(T_{room})$ using the numerical method described in Section II. The central wavelength $\lambda_{0}$ is fixed to 826 nm.

Fig. 3 illustrates the variation of $\ln (\frac{B}{B_{0}})$ and $\ln (\frac{\tau}{\tau_{0}})$ with ambient temperature for the Andrew ET-800 fiber. Normalized parameters $B_{0}$ and $\tau_{0}$ are the modal birefringence and PMD of the fiber at temperature equal to $10^{\circ} C$ . These results show that relative temperature sensitivities of modal birefringence $S_{T}^{B}$ , and PMD, $S_{T}^{\tau}$ , defined by (1) and (2) and represented by the slope of curves (a) and (b), respectively, are constant for ambient temperature fluctuations around $40^{\circ} C$ . While $|S_{T}^{B}|$ is around $3 ×10^{-4}^{\circ} C^{-1},|S_{T}^{\tau}|$ is equal to $7 ×10^{-4}^{\circ} C^{-1}$ . This feature indicates the PMD is more sensitive to tem- perature than the modal birefringence and concurs with the experimental observations described in the next paragraph.

![](./images/812462217503965184_3.jpg)

Fig. 3. The relative change of modal birefringence, $\ln (\frac{B(T)}{B_{0}})$ -solid line. The relative change of PMD, $\ln (\frac{\tau(T)}{\tau_{0}})$ -dashed line, for an Andrew ET-800 fiber as a function of ambient temperature T. The fiber parameters are $\Delta n=0.033$ , e=2, and wavelength $\lambda=0.826 \mu m$ .

### B. Experimental Analysis
A sketch of the experimental set-up for analyzing the polarization properties for an electronically scanned white- light sensor (of hydrostatic pressure or strain) employing HEC fiber as a sensing element is illustrated in Fig. 4. A broadband( $\lambda_{0}=826 nm$ ) light emitted by a superluminescent diode is polarized linearly by 3M polarization fiber and then coupled into one polarization mode of the lead-up HB fiber (Corning). The sensing HB fiber (Andrew ET-800) is spliced with the lead-up fiber at $45^{\circ}$ in order to excite both polarization modes equally. The input of the HB lead-down fiber (Corning) is spliced with output of the sensing fiber at $45^{\circ}$ and the output of the lead-down fiber is aligned to be at $45^{\circ}$ to the polarization axes of the receiving interferometer, which is composed of a quartz delay line, Wollaston prism, analyzer, CCD camera and processing software. The thickness of the quartz delay line is adjusted to compensate for the group delay between polarization modes introduced by the sensing fiber. As a result, these polarization modes interfere in the plane of the CCD array producing the white-light interference pattern which moves across the CCD array in response to temperature- induced changes in the birefringence of the sensing fiber. The processing software makes it possible to determine the displacement of the coherence function as well as the displace- ment of individual interference fringes, providing information about the temperature sensitivities of the PMD and the modal birefringence, respectively. If these displacements are ex- pressed in units of interference fringes ( $\delta M_{f}$ -displacement of individual fringes and $\delta M_{c}$ -displacement of the contrast function) the temperature sensitivities can be determined bythe following relations [4]
$$
\frac{\partial B}{\partial T}=\frac{1}{L} \frac{\delta M_{f}}{\delta T} \lambda_{0}\qquad(22)
$$

$$
\frac{\partial \tau}{\partial T}=\frac{1}{T} \frac{\delta M_{c}}{\delta T} \frac{\Delta N_{q}}{\Delta n_{q}} \frac{\lambda_{0}}{c}\qquad(23)
$$
where L is the length of the tested HB fiber (2.75 m); $\lambda_{0}$  is the central wavelength (826 nm); $\Delta n_{q}$ and $\Delta N_{q}$ are the phase and group birefringence of crystalline quartz $(8889 \times$  $10^{-5}$ , and $9520 ×10^{-5}$ , respectively). Fig. 5 illustrates the

![](./images/812462217503965184_4.jpg)

Fig. 4. Sketch of a configuration of a white-light interferometricsensor composed of an Andrew ET-800 fiber as a sensing element: SLD-superluminescence laser diode, L-collimating lens, DL-delay line, WP-Wollaston prism, A-analyzer, CL-collimating lens.

![](./images/812462217503965184_5.jpg)

Fig. 5. The shift of the individual interference fringes-solid line and the shift of the contrast function-dashed line versus the temperature for an Andrew ET-800 fiber. The length of the tested fiber is 2.75 m.

measured shift of the contrast function and individual fringes versus temperature for Andrew ET-800 fiber. From these experimental data, the sensitivities to temperature of modal birefringence $B$ and PMD $\tau$ can be deduced

$$
\frac{\partial B}{\partial T}=-7 \times 10^{-8}\left[\frac{1}{{ }^{\circ} \mathrm{C}}\right] \tag{24}
$$

$$
\frac{\partial \tau}{\partial T}=-6 \times 10^{-4}\left[\frac{\mathrm{ps}}{\mathrm{m}^{\circ} \mathrm{C}}\right]. \tag{25}
$$

Therefore, absolute values of relative sensitivities for modal birefringence $(B=1.63 \times 10^{-4})$ and PMD $(\tau=0.887 \mathrm{ps} / \mathrm{m})$ for Andrew ET-800 fiber are equal to

$$
\left|S_{T}^{B}\right|=4 \times 10^{-4}\left[{ }^{\circ} \mathrm{C}^{-1}\right] \tag{26}
$$

$$
\left|S_{T}^{\tau}\right|=7 \times 10^{-4}\left[{ }^{\circ} \mathrm{C}^{-1}\right] \tag{27}
$$

compared to their calculated values, $|S_{T}^{B}|=3 \times 10^{-4}{ }^{\circ} \mathrm{C}^{-1}$ and $|S_{T}^{\tau}|=7 \times 10^{-4}{ }^{\circ} \mathrm{C}^{-1}$. The small discrepancy between the theoretical and experimental values of $|S_{T}^{B}|$ is most probably related to the difference between the calculated and measured values of modal birefringence $B$.

## V. SUMMARY AND CONCLUSION

In this paper, a full-vectorial analysis based on the solution of the Maxwell's equations is used to investigate the combined form-induced and stress-induced (temperature) effects on the modal polarization characteristics of HEC fibers frequently used in the design of fiber-optic sensing devices. The charac- teristic curves of their modal birefringence, modal polarization dispersion and modal chromatic dispersion, computed with and without thermal stress effects are presented. It is shown that 1) the contribution of thermal stresses to the polarization properties depends greatly on the normalized frequency, 2) for the whole range of the normalized frequency, there is no interchange between the fast and the slow axes of the fibers, and 3) ambient temperature fluctuations could induce a significant shift in the zero dispersion wavelength.

An Andrew ET-800 fiber used recently in a fiber-optic sensing device has been investigated with the present model.

Computations of the modal birefringence and PMD of the fiber for ambient temperature fluctuations around $40{ }^{\circ} \mathrm{C}$ show that the relative sensitivities of PMD and modal birefringence are constant but differ significantly. These results concur with those obtained experimentally. It is therefore crucial to take into account the difference between the temperature sensitivity of the modal birefringence and PMD of HEC fibers when designing practical sensors based on this type of fiber.

## REFERENCES

[1] W. J. Bock, W. Urbanczyk, J. Wojcik, and M. Beaulieu, "White-light interferometric fiber-optic pressure sensor," IEEE Trans. Instrum. Meas., vol. 44, pp. 704-708, 1995.
[2] W. J. Bock, T. R. Wolinski, and A. Barwicz "Development of a polarimetric optical fiber sensor for electronic measurement of high pressure," IEEE Trans. Instrum. Meas., vol. 39, pp. 233-237, 1990.
[3] W. J. Bock and W. Urbanczyk, "Measurement of polarization mode dispersion and modal birefringence in highly birefringent fibers by means of electronically scanned shearing-type interferometry," Appl. Opt., vol. 32, pp. 5841-5848, 1993.
[4] W. Urbanczyk and W. J. Bock, "Analysis of dispersion effects for white-light interferometric fiber-optic sensors," Appl. Opt., vol. 33, pp.124-129, 1994.
[5] W. J. Bock, W. Urbanczyk, R. Buczynski, and A. Domanski, "Cross- sensitivity effect in temperature-compensated sensors based on highly birefringent fibers," Appl. Opt., vol. 33, pp. 6078-6083, 1994.
[6] N. Imoto, N. Yoshizawa, J.-I. Sakai, and H. Tsuchiya, "Birefringence in single-mode optical fiber due to elliptical core deformation and stress anisotropy," IEEE J. Quantum Electron., vol. QE-18, pp. 53-58, 1982.
[7] N. Shibata, M. Tateda, and S. Seikai, "Polarization mode dispersion mea- surement in elliptical core single-mode fibers by a spatial technique," IEEE J. Quantum Electron., vol. 16, pp. 1267-1271, 1980.
[8] Y. Liu, B. M. A. Rahman, and K. T. V. Grattan, "Thermal-stress induced birefringence in bow-tie optical fibers," Appl. Opt., vol. 33, pp. 5611-5616, 1994.
[9] K. Okamoto, M. P. Varnham, and D. N. Payne, "Polarization- maintaining optical fibers with low dispersion over a wide spectral range," Appl. Opt., vol. 22, pp. 2370-2373, 1983.
[10] K. Okamoto and T. Hosaka, "Polarization-dependent chromatic disper- sion in birefringent optical fibers," Opt. Lett., vol. 12, pp. 290-292,1987.
[11] M. Fontaine, "Computation of optical birefringence characteristics of highly eccentric elliptical core fibers under various thermal stress conditions," J. Appl. Phys., vol. 75, pp. 68-73, 1994.
[12] ______, "A new numerical method for computing the optical charac- teristics of birefringent fibers," J. Appl. Phys., vol. 73, pp. 1557-1560,1993.
[13] V. P. Tzolov and M. Fontaine, "Theoretical analysis of birefringence and form-induced polarization mode dispersion in birefringent optical fibers: A full-vectorial approach," J. Appl. Phys., vol. 77, pp. 1-6, 1995.
[14] C.-L. Chen, "Analysis of high birefringence fibers," J. Lightwave Technol., vol. 5, pp. 53-69, 1987.
[15] S. Timoshenko, Theory of Elasticity. New York: McGraw-Hill, 1934.
[16] K.-H. Tsai, K.-S. Kim, and T. F. Morse, "General solutions for stress- induced polarization in optical fibers," J. Lightwave Technol., vol. 9, pp.7-17, 1991.
[17] J.-I. Sakai and T. Kimura, "Birefringence caused by thermal stress in elliptically deformed core optical fibers," IEEE J. Quantum Electron., vol. 18, pp. 1899-1909, 1982.

![](./images/812462217503965184_6.jpg)

Marie Fontaine received the M.Sc. and Ph.D. de- grees in physics from the Laval University, Canada in 1978 and 1982, respectively.

From 1983 to 1985, she was with the Division of Electrical Engineering, National Research Council, Canada, as a Postdoctoral Fellow. She is currently a Professor with the Departement of Computer Science at the Université du Québec à Hull, Canada. Her research interests include linear and nonlinear optics.
Dr. Fontaine is a Member of OSA.

Binruo Wu, photograph and biography not available at the time of publication.

![](./images/812462217503965184_7.jpg)

Velko P. Tzolov received the M.Sc. degree in engineering physics and the Ph.D. degree in physics from "St. Kliment Ochridski" University of Sofia, in 1989 and 1993, respectively.

From 1993 to 1995, he was with the Department of Computer Science, Université du Québecà Hull, Canada, as a Postdoctoral Fellow. Since 1996 he is a Researcher at Optiwave Corporation, Ste-Foy, P.Q., Canada. His research interests include laser physics, linear, and nonlinear optics.

![](./images/812462217503965184_8.jpg)

Wojtek J. Bock received the M.Sc. degree in elec- trical engineering and the Ph.D. degree in solid state physics from the Warsaw University of Technology, Poland, in 1971 and 1980, respectively.

He is currently a Professor with the Department of Computer Science at the Université du Québecà Hull, Canada, where he leads the Optoelectronics Research Group. His research interests include fiber- optic sensors and devices, multisensor systems, and precise measurement systems of nonelectric quanti- ties.

Dr. Bock is a Senior Member of SME and a Member of SPIE.

Waclaw Urbanczyk, photograph and biography not available at the time of publication.