Accepted Manuscript

Low velocity impact modeling of functionally graded carbon nanotube rein-
forced composite (FG-CNTRC) plates with arbitrary geometry and general
boundary conditions

Mohadeseh Fallah, AliReza Daneshmehr, Hamed Zarei, Hosein Bisadi,
Giangiacomo Minak

![](./images/813087247099232256_1.jpg)

<table>
<tr>
<td>PII:</td>
<td>S0263-8223(17)33182-3</td>
</tr>
<tr>
<td>DOI:</td>
<td>https://doi.org/10.1016/j.compstruct.2017.11.030</td>
</tr>
<tr>
<td>Reference:</td>
<td>COST 9096</td>
</tr>
<tr>
<td>To appear in:</td>
<td>Composite Structures</td>
</tr>
<tr>
<td>Received Date:</td>
<td>23 September 2017</td>
</tr>
<tr>
<td>Revised Date:</td>
<td>29 October 2017</td>
</tr>
<tr>
<td>Accepted Date:</td>
<td>13 November 2017</td>
</tr>
</table>

Please cite this article as: Fallah, M., Daneshmehr, A., Zarei, H., Bisadi, H., Minak, G., Low velocity impact modeling of functionally graded carbon nanotube reinforced composite (FG-CNTRC) plates with arbitrary geometry and general boundary conditions, Composite Structures (2017), doi: https://doi.org/10.1016/j.compstruct.2017.11.030

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Low velocity impact modeling of functionally graded carbon nanotube reinforced composite (FG-CNTRC) plates with arbitrary geometry and general boundary conditions

Mohadeseh Fallah $^{1}$, AliReza Daneshmehr$^{1*}$, Hamed Zarei$^{2}$, Hosein Bisadi$^{2}$, Giangiacomo Minak$^{3}$

$^{1}$ School of Mechanical Engineering, College of Engineering, University of Tehran, North Kargar St, Tehran, Iran.

$^{2}$ Department of Mechanical Engineering, Iran University of Science and Technology (IUST), Narmak, Tehran, Iran

$^{3}$ Department of Industrial Engineering (DIN), Università di Bologna, 40 Fontanelle Ave, Forli, Italy

* Corresponding author: daneshmehr@ut.ac.ir

### Abstract

The full dynamic response of FG-CNT reinforced composite plates with arbitrary geometry subjected to impact loading is considered in the present paper. The CNT reinforcement distribution is considered either uniform or functionally graded along the plate thickness and the equivalent mechanical properties of reinforced composite plates are estimated according to the extended rule of mixtures. The derived governing equations are based on high-order shear deformation theory, using Hamilton's principle. An integration scheme appropriate for calculating double integral with variable limits is developed based on the Simpson's rule to evaluate the components of Hamilton's equation. A two-dimensional Ritz formulation appropriate for general boundary conditions is incorporated in the nonlinear Hertzian contact law to establish the equations of motion. A well-known fourth-order Runge-Kutta method is employed to solve the resulting equations in time domain. The validation of the proposed model is accomplished by comparing its results and those published in the literature and good agreement is achieved. A comprehensive sensitivity analysis is conducted to study the effect of various involved parameters such as CNT volume fraction and its distribution profile along the thickness, boundary conditions, temperature rising and in-plane loading on impact characteristics of both circular and triangular plates.

### Keywords

Low velocity impact; carbon nanotube; functionally graded reinforced composite; general geometrical shape; Ritz formulation;

### 1. Introduction

The outstanding mechanical, thermal and electrical properties of carbon nanotubes (CNTs) over micro-sized carbon fibers have made them a privileged candidate for the new generation of reinforcement materials [1–3]. The superior properties of CNTs such as the extremely high elastic modulus, tensile strength, aspect ratio, low density and corrosion resistance, have attracted a great deal of interest among researchers. Unlike macro-sized reinforced fibers, CNT reinforcement can improve mechanical, thermal and physical properties of a structure to a significant extent. For instance, the Young's modulus of CNTs is superior to all carbon fibers with a value of more than 1 TPa while its density can be only $1.3\ \text{g/cm}^3$ [4].

The material mismatching between adjacent differently oriented layers in traditional laminated composites may cause delamination while the functionally graded (FG) reinforced materials, which is known as a new kind of heterogeneous isotropic composite materials, can overcome this issue. In general, a functionally graded material (FGM) is a mixtures of two constituents with smooth and continuous variation of properties across one or more direction which provide exceptional mechanical and thermal properties. FGMs are mainly composed of metals and ceramic constituents. Hence withstanding the high temperature gradients and the high strength properties are the main characteristics of FGMs. Therefore the outstanding characteristics of FGMs and CNTs can be obtained together through functionally graded distribution of CNTs as reinforcement in an isotropic polymer as the matrix.

Over the last decade, numerous theoretical studies have been dedicated to the structural behavior including static, vibration, buckling and dynamic response of functionally graded carbon nanotube reinforced composite (FG-CNTRC) beams [5–8], plates [9–12] and shells [13–16]. Shen is the pioneer in studying the CNT reinforcement effect on the large deflection

response of rectangular plates in thermal environment [9]. He found that functionally graded carbon nanotube distribution has a considerable effect on the load-bending moment curves while its effect on the load-deflection curves is less pronounced. The approach is based on high-order shear deformation plate theory (HSDT) incorporated into Von Karman-type of kinematic nonlinearity and the governing equations are solved using a two-step perturbation technique.

Based on this study, Shen and his co-workers investigated the vibration and postbuckling analysis of temperature -dependent FG-CNTRC plates and shells [14,17-19]. They concluded that in the case of mechanical loading, functionally graded nanotube reinforcement can increase the postbuckling strength and buckling load of the plates and shells while in the case of thermal loading, its effect is less pronounced. In addition, they found that the CNT distribution profiles significantly affect the nonlinear vibration characteristics of FG-CNTRC plates and shells.

Besides the fundamental analytical approach introduced by Shen, some numerical and finite element studies have been performed by other researchers to study the structural response of FG-CNTRC. For instance, Lei et al. [20-22] investigated the large deflection, free vibration and buckling of FG-CNTRC plates using the element-free-kp-Ritz method based on first-order shear deformation theory (FSDT). The effective material properties of CNTRC plates were estimated through a micromechanical model based on either the Eshelby-Mori-Tanaka approach or the extended rule of mixtures, and the effect of various parameters such as carbon nanotube volume fraction, plate width-to-thickness ratio, and plate aspect ratio were studied.

The impact characteristics of traditional reinforced composites structures have been studied extensively [23-25] while the impact response of FG-CNTRC structures is very limited. Based on Shen's approach, Wang et al. [10,26] and Bayat et al. [16] analyzed the nonlinear low velocity impact behavior of temperature-dependent FG-CNTRC rectangular plates and

cylindrical shells with simply supported boundary conditions, respectively. Jam and kiani [8] studied the dynamic response of FG-CNTRC beams subjected to low velocity impact loading. They found that by increasing the CNT volume fraction, the peak contact force increases while the contact duration decreases. Malekzadeh and Dehbozorgi [27] presented the low velocity impact analysis of FG-CNTRC skew plates using the finite element method based on FSDT in conjunction with Newmark's time integration scheme and Newton-Raphson algorithm.

Due to the superior properties of CNTs reinforcement, FGCNTRC plates have been the desirable candidate in various industries such as the aerospace and automobile [28], and as they are frequently exposed to impact loadings, their impact response is therefore important. In addition, according to the foregoing literature survey, the former researchers were concerned with either traditional reinforced composite structures or FG-CNTRC rectangular plates/shell panels under impact loading (with the exception of the study by Malekzadeh and Dehbozorgi [27] which was performed using a finite element approach). To the best of the authors' knowledge, hitherto there is no published research including the impact response of plates with arbitrary geometrical shape. Therefore, in the present paper, a semi analytical model is developed to investigate the low velocity impact response of temperature-dependent carbon nanotube reinforced composite plates with general geometrical shape based on the free-mesh Ritz method. The governing equations are derived based on high-order shear deformation theory using Hamilton's principle. A Ritz-based scheme appropriate for general boundary conditions is employed to simplify the equations in space domain. Finally, the equations are solved using the fourth order Runge-Kutta method in time domain. To have a good comprehensive sensitivity analysis, FG-CNTRC plates with two different geometrical shapes, i.e. circular and triangular, are considered, and the effect of various parameters such as boundary conditions, temperature rising, initial kinetic energy of impactor,

CNT volume fraction and its distribution profile across the thickness are taken into consideration.

## 2. The effective material properties of CNTRC plates

It is assumed that the FG-CNTRC plates are composed of single walled carbon nanotubes (SWCNTs) as reinforcements and an isotropic polymer as matrix. Distribution of SWCNTs along the plate thickness may be uniform or functionally graded. In this research, three distribution profiles of SWCNTs are considered: 1-uniform distribution (referred to as UD-CNTRC), 2- symmetric functionally graded (referred to as X-CNTRC) in which both top and bottom surfaces of the plate are CNT-rich, and 3-unsymmetric functionally graded (referred to as V-CNTRC) in which only the top surface of plate is CNT-rich. The corresponding distribution profiles of SWCNT across the plate thickness are mathematically given by [29,30]

$$
\begin{cases}
\mathrm{V}_{\mathrm{CNT}}=\mathrm{V}_{\mathrm{CNT}}^{*} & \mathrm{UD}-\mathrm{CNTRC} \\
\mathrm{V}_{\mathrm{CNT}}=2\left(\frac{2|z|}{\mathrm{h}}\right) \mathrm{V}_{\mathrm{CNT}}^{*} & \mathrm{X}-\mathrm{CNTRC} \\
\mathrm{V}_{\mathrm{CNT}}=\left(1+\frac{2 \mathrm{z}}{\mathrm{h}}\right) \mathrm{V}_{\mathrm{CNT}}^{*} & \mathrm{~V}-\mathrm{CNTRC}
\end{cases} \tag{1}
$$

where the effective volume fraction of CNT, $\mathrm{V}_{\mathrm{CNT}}^{*}$ is

$$
\mathrm{V}_{\mathrm{CNT}}^{*}=\frac{\rho^{\mathrm{m}}}{\mathrm{w}^{\mathrm{CNT}}+\left(\rho^{\mathrm{m}} / \mathrm{w}^{\mathrm{CNT}}\right)-\rho^{\mathrm{CNT}}}[29,30] \tag{2}
$$

in which $\mathrm{w}^{\mathrm{CNT}}, \rho^{\mathrm{CNT}}$ and $\rho^{\mathrm{m}}$ are the CNT mass fraction, CNT and matrix densities, respectively. In addition, h is the plate thickness and $-\frac{\mathrm{h}}{2} \leq \mathrm{z} \leq \frac{\mathrm{h}}{2}$. A simple calculation of

equation (1) shows that all distribution profiles have the same value of volume fraction of $\mathrm{V}_{\mathrm{CNT}}^{*}$.

The effective material properties of FG-CNTRC plates can be predicted based on various micromechanical models. In the present study, the extended rule of mixtures is employed to estimate the effective Young's and shear modulus of nanocomposite plates as in [31]

$$
\begin{aligned}
& \mathrm{E}_{11}=\eta_{1} \mathrm{~V}_{\mathrm{CNT}} \mathrm{E}_{11}^{\mathrm{CNT}}+\mathrm{V}_{\mathrm{m}} \mathrm{E}^{\mathrm{m}} \\
& \frac{\eta_{2}}{\mathrm{E}_{22}}=\frac{\mathrm{V}_{\mathrm{CNT}}}{\mathrm{E}_{22}^{\mathrm{CNT}}}+\frac{\mathrm{V}_{\mathrm{m}}}{\mathrm{E}^{\mathrm{m}}} \\
& \frac{\eta_{3}}{\mathrm{G}_{12}}=\frac{\mathrm{V}_{\mathrm{CNT}}}{\mathrm{G}_{12}^{\mathrm{CNT}}}+\frac{\mathrm{V}_{\mathrm{m}}}{\mathrm{G}^{\mathrm{m}}} \\
& \mathrm{v}_{12}=\mathrm{V}_{\mathrm{CNT}}^{*} \mathrm{v}^{\mathrm{CNT}}+\mathrm{V}_{\mathrm{m}} \mathrm{v}^{\mathrm{m}} \\
& \rho=\mathrm{V}_{\mathrm{CNT}} \rho^{\mathrm{CNT}}+\mathrm{V}_{\mathrm{m}} \rho^{\mathrm{m}} \\
& \alpha_{11}=\frac{\mathrm{V}_{\mathrm{CNT}} \mathrm{E}_{11}^{\mathrm{CNT}} \alpha_{11}^{\mathrm{CNT}}+\mathrm{V}_{\mathrm{m}} \mathrm{E}^{\mathrm{m}} \alpha^{\mathrm{m}}}{\mathrm{V}_{\mathrm{CNT}} \mathrm{E}_{11}^{\mathrm{CNT}}+\mathrm{V}_{\mathrm{m}} \mathrm{E}^{\mathrm{m}}} \\
& \alpha_{22}=\left(1+\mathrm{v}_{12}^{\mathrm{CNT}}\right) \mathrm{V}_{\mathrm{CNT}} \alpha_{22}^{\mathrm{CNT}}+\left(1+\mathrm{v}^{\mathrm{m}}\right) \mathrm{V}_{\mathrm{m}} \alpha^{\mathrm{m}}-\mathrm{v}_{12} \alpha_{11}
\end{aligned}
\tag{3}
$$

where $\mathrm{E}_{11}^{\mathrm{CNT}}, \mathrm{E}_{22}^{\mathrm{CNT}}$ and $\mathrm{G}_{12}^{\mathrm{CNT}}$ are the Young's moduli and shear modulus of the CNT, respectively and $\mathrm{E}^{\mathrm{m}}$ and $\mathrm{G}^{\mathrm{m}}$ are corresponding matrix properties. The coefficients $\eta_{\mathrm{i}} \quad \mathrm{i}=1,2$ and 3 are CNT/matrix efficiency parameters. In addition, $\mathrm{v}^{\mathrm{CNT}}, \mathrm{v}^{\mathrm{m}}, \rho^{\mathrm{CNT}}$ and $\rho^{\mathrm{m}}$ are Poisson's ratio and density of CNT and matrix, respectively. Furthermore, $\mathrm{V}_{\mathrm{m}}$ and $\mathrm{V}_{\mathrm{CNT}}$ are the volume fraction of matrix and CNT, respectively which are related by $\mathrm{V}_{\mathrm{m}}+\mathrm{V}_{\mathrm{CNT}}=1$. In addition, in equation (3), $\alpha_{11}^{\mathrm{CNT}}, \alpha_{22}^{\mathrm{CNT}}$ and $\alpha^{\mathrm{m}}$ are the thermal expansion coefficients in the longitudinal and transverse direction for CNT and matrix, respectively.

## 3. The governing equations

### 3.1. Displacement field and constitutive equations

The present study deals with the low velocity impact analysis of FG-CNTRC plates with arbitrary geometry with thickness h. Based on Reddy's high-order shear deformation theory (HSDT), the displacement field components can be expressed as [32,33]

$$
\left\{
\begin{aligned}
\mathrm{u}(\mathrm{x}, \mathrm{y}, \mathrm{z}, \mathrm{t}) & =\mathrm{u}_{0}(\mathrm{x}, \mathrm{y}, \mathrm{t})-\mathrm{z} \frac{\partial \mathrm{w}}{\partial \mathrm{x}}+\mathrm{f}(\mathrm{z}) \theta_{1}(\mathrm{x}, \mathrm{y}, \mathrm{t}) \\
\mathrm{v}(\mathrm{x}, \mathrm{y}, \mathrm{z}, \mathrm{t}) & =\mathrm{v}_{0}(\mathrm{x}, \mathrm{y}, \mathrm{t})-\mathrm{z} \frac{\partial \mathrm{w}}{\partial \mathrm{y}}+\mathrm{f}(\mathrm{z}) \theta_{2}(\mathrm{x}, \mathrm{y}, \mathrm{t}) \\
\mathrm{w}(\mathrm{x}, \mathrm{y}, \mathrm{z}, \mathrm{t}) & =\mathrm{w}_{0}(\mathrm{x}, \mathrm{y}, \mathrm{t}) \\
\mathrm{f}(\mathrm{z}) & =\mathrm{z}\left(1-\frac{4}{3}\left(\frac{\mathrm{z}}{\mathrm{h}}\right)^{2}\right)
\end{aligned}
\right. \tag{4}
$$

where $\mathrm{u}_{0}, \mathrm{v}_{0}, \mathrm{w}_{0}, \theta_{1}$ and $\theta_{2}$ are the corresponding in-plane, transverse displacement and rotation about y and x axes of the plate mid-surface, while f(z) represents the shear strain distribution along the thickness. According to the HSDT, one can write the in-plane strain components and constitutive equations as [23,29]

$$
\left\{
\begin{aligned}
\varepsilon_{\mathrm{xx}} \\
\varepsilon_{\mathrm{yy}} \\
\gamma_{\mathrm{xy}}
\end{aligned}
\right\}=\left\{
\begin{aligned}
\frac{\partial \mathrm{u}_{0}}{\partial \mathrm{x}} \\
\frac{\partial \mathrm{v}_{0}}{\partial \mathrm{y}} \\
\frac{\partial \mathrm{u}_{0}}{\partial \mathrm{y}}+\frac{\partial \mathrm{v}_{0}}{\partial \mathrm{x}}
\end{aligned}
\right\}-\mathrm{z}\left\{
\begin{aligned}
\frac{\partial^{2} \mathrm{w}_{0}}{\partial \mathrm{x}^{2}} \\
\frac{\partial^{2} \mathrm{w}_{0}}{\partial \mathrm{y}^{2}} \\
2 \frac{\partial^{2} \mathrm{w}_{0}}{\partial \mathrm{x} \partial \mathrm{y}}
\end{aligned}
\right\}+\mathrm{f}(\mathrm{z})\left\{
\begin{aligned}
\frac{\partial \theta_{1}}{\partial \mathrm{x}} \\
\frac{\partial \theta_{2}}{\partial \mathrm{y}} \\
\frac{\partial \theta_{1}}{\partial \mathrm{y}}+\frac{\partial \theta_{2}}{\partial \mathrm{x}}
\end{aligned}
\right\} \tag{5}
$$

$$
\left\{
\begin{aligned}
\gamma_{\mathrm{yz}} \\
\gamma_{\mathrm{xz}}
\end{aligned}
\right\}=\mathrm{f}^{\prime}(\mathrm{z})\left\{
\begin{aligned}
\theta_{2} \\
\theta_{1}
\end{aligned}
\right\} \tag{6}
$$

$$
\left\{\begin{array}{l}
\sigma_{\mathrm{xx}} \\
\sigma_{\mathrm{yy}} \\
\sigma_{\mathrm{xy}}
\end{array}\right\}=\left[\begin{array}{lll}
\overline{\mathrm{Q}}_{11} & \overline{\mathrm{Q}}_{12} & \overline{\mathrm{Q}}_{16} \\
\overline{\mathrm{Q}}_{12} & \overline{\mathrm{Q}}_{22} & \overline{\mathrm{Q}}_{26} \\
\overline{\mathrm{Q}}_{16} & \overline{\mathrm{Q}}_{26} & \overline{\mathrm{Q}}_{66}
\end{array}\right]\left\{\begin{array}{l}
\varepsilon_{\mathrm{xx}} \\
\varepsilon_{\mathrm{yy}} \\
\varepsilon_{\mathrm{xy}}
\end{array}\right\}
\tag{7}
$$

$$
\left\{\begin{array}{l}
\sigma_{\mathrm{yz}} \\
\sigma_{\mathrm{xz}}
\end{array}\right\}=\left[\begin{array}{ll}
\overline{\mathrm{Q}}_{44} & \overline{\mathrm{Q}}_{45} \\
\overline{\mathrm{Q}}_{45} & \overline{\mathrm{Q}}_{55}
\end{array}\right]\left\{\begin{array}{l}
\gamma_{\mathrm{yz}} \\
\gamma_{\mathrm{xz}}
\end{array}\right\}
\tag{8}
$$

where $\{\overline{\mathrm{Q}}_{\mathrm{ij}}\}$ is the reduced stiffness matrix which are related by $\overline{\mathrm{Q}}_{\mathrm{ij}}=\mathrm{Q}_{\mathrm{ij}}$ for an FG-CNTRC plates [12].

$$
\begin{gathered}
\mathrm{Q}_{11}(z)=\frac{\mathrm{E}_{11}}{1-v_{12} v_{21}}, \mathrm{Q}_{12}(z)=\frac{v_{21} \mathrm{E}_{11}}{1-v_{12} v_{21}}, \mathrm{Q}_{22}(z)=\frac{\mathrm{E}_{22}}{1-v_{12} v_{21}}, \\
\mathrm{Q}_{16}=\mathrm{Q}_{26}=0, \quad \mathrm{Q}_{66}(z)=\mathrm{G}_{12}, \quad \mathrm{Q}_{44}(z)=\mathrm{G}_{23}, \quad \mathrm{Q}_{55}(z)=\mathrm{G}_{13}
\end{gathered}
\tag{9}
$$

### 3.2. Hertzian contact law

In the impact problem, a contact law which gives a relationship between the contact force and the indentation is required. Moreover, in the low velocity impact, the time period of impact is longer than the time period of the plate first mode shape. Hence, Hertzian contact law which incorporates the full dynamic response of plate and impactor can be useful to trace contact force history. According to Hertzian contact law, the exerted external force can be defined by [23,29]:

$$
\begin{gathered}
\mathrm{F}_{\mathrm{c}}(\mathrm{t})=\mathrm{K}_{\mathrm{c}} \alpha^{\frac{3}{2}} \\
\mathrm{~K}_{\mathrm{c}}=\frac{4}{3} \mathrm{ER}_{\mathrm{i}}^{\frac{1}{2}} \\
\frac{1}{\mathrm{E}}=\frac{1-v_{1}^{2}}{\mathrm{E}_{1}}+\frac{1}{\mathrm{E}_{\mathrm{z}}}
\end{gathered}
\tag{10}
$$

in which $\mathrm{E}_{1}$ and $v_{1}$ are Young's modulus and Poisson's ratio of impactor, respectively, and $\mathrm{E}_{\mathrm{z}}$ is the transverse Young's modulus of CNTRC plate at the top surface (where impact occurs)

which can be approximated by $E_{22}$ [8] determined by equation (3). In addition $K_{c}$ and $\alpha$ denote the contact stiffness and the impactor indentation, respectively.

### 3.3. The equations of motion
The equations of motion are developed based on Hamilton's principle which take the following form [34]

$$
0=\int_{t_{1}}^{t_{2}}(\delta \mathrm{U}+\delta \mathrm{V}-\delta \mathrm{K}) \mathrm{dt} \tag{11}
$$

where $\delta \mathrm{U}$, $\delta \mathrm{V}$ and $\delta \mathrm{K}$ represent the virtual strain energy, the virtual work done by external forces including in-plane and out of plane forces and the virtual kinetic energy, respectively.

Based on HSDT, each components of equation (11) can be evaluated by [23,29]:

$$
\delta \mathrm{U}=\int_{\Omega}\left(\sigma_{\mathrm{xx}} \delta \varepsilon_{\mathrm{xx}}+\sigma_{\mathrm{yy}} \delta \varepsilon_{\mathrm{yy}}+\sigma_{\mathrm{xy}} \delta \gamma_{\mathrm{xy}}+\sigma_{\mathrm{xz}} \delta \gamma_{\mathrm{xz}}+\sigma_{\mathrm{yz}} \delta \gamma_{\mathrm{yz}}\right) \mathrm{dV} \tag{12}
$$

$$
\delta \mathrm{V}=\delta \mathrm{V}_{1}+\delta \mathrm{V}_{2}
$$

$$
\delta \mathrm{V}_{1}=-\int_{\Omega} \mathrm{F}_{\mathrm{c}} \delta_{0}\left(\mathrm{x}-\mathrm{x}_{\mathrm{i}}, \mathrm{y}-\mathrm{y}_{\mathrm{i}}\right) \delta \mathrm{wdxdy} \tag{13}
$$

$$
\delta \mathrm{V}_{2}=-\int_{\Omega}\left(\mathrm{N}_{\mathrm{xx}} \frac{\partial \mathrm{w}}{\partial \mathrm{x}} \delta\left(\frac{\partial \mathrm{w}}{\partial \mathrm{x}}\right)+\mathrm{N}_{\mathrm{yy}} \frac{\partial \mathrm{w}}{\partial \mathrm{y}} \delta\left(\frac{\partial \mathrm{w}}{\partial \mathrm{y}}\right)+\mathrm{N}_{\mathrm{xy}}\left(\frac{\partial \mathrm{w}}{\partial \mathrm{x}} \delta\left(\frac{\partial \mathrm{w}}{\partial \mathrm{y}}\right)+\frac{\partial \mathrm{w}}{\partial \mathrm{y}} \delta\left(\frac{\partial \mathrm{w}}{\partial \mathrm{x}}\right)\right)\right) \mathrm{dxdy}
$$

$$
\delta \mathrm{K}=\int_{\Omega} \rho(\dot{\mathrm{u}} \delta \dot{\mathrm{u}}+\dot{\mathrm{v}} \delta \dot{\mathrm{v}}+\dot{\mathrm{w}} \delta \dot{\mathrm{w}}) \mathrm{dV} \tag{14}
$$

where $\rho$ denotes the CNTRC density which is determined by equation (3). $(x_{i}, y_{i})$ and $F_{c}$ are the impact position and the contact force induced by the spherical impactor. $\delta_{0}$ is the two-dimensional Dirac's delta function. It is noteworthy that the $\Omega$ denotes the in-plane domain of the plate. As is clear for plates with general geometry (non-rectangular), the integral calculation in equation (12)-(14) includes variable upper and lower limits which cannot easily be determined. Hence, a 2D integration scheme based on Simpson's rule is adopted to evaluate the

Hamilton's principle components for plates with general shape. $N_{xx}$, $N_{yy}$ and $N_{xy}$ represent the in-plane loading corresponding to the mechanical or thermal loading. In thermal environments, the in-plane forces caused by temperature rising can be defined by [9]:

$$
\begin{bmatrix}
N_{xx}^{T} \\
N_{yy}^{T} \\
N_{xy}^{T}
\end{bmatrix}
=
\int_{-\frac{h}{2}}^{\frac{h}{2}}
\begin{bmatrix}
\overline{Q}_{11} & \overline{Q}_{12} & \overline{Q}_{16} \\
\overline{Q}_{12} & \overline{Q}_{22} & \overline{Q}_{26} \\
\overline{Q}_{16} & \overline{Q}_{26} & \overline{Q}_{66}
\end{bmatrix}
\begin{bmatrix}
1 & 0 \\
0 & 1 \\
0 & 0
\end{bmatrix}
\begin{bmatrix}
\alpha_{11} \\
\alpha_{22}
\end{bmatrix}
\Delta T dz
\tag{15}
$$

where $\alpha_{11}$ and $\alpha_{22}$ are the thermal expansion coefficients in the longitudinal and transverse directions of CNTRC plates, respectively, which are defined in equation (3). In addition, $\Delta T=T-T_{0}$ is temperature change, and T and $T_{0}$ are, respectively, the elevated temperature and reference temperature.

### 3.4. The proposed solution procedure
A Ritz-based solution in space domain appropriate for general boundary conditions is developed to simplify the governing equations. According to this technique, a solution is approximated by a finite linear combination of shape functions as follows [23,29]

$$
\left\{
\begin{array}{c}
u_{0} \\
v_{0} \\
w_{0} \\
\theta_{1} \\
\theta_{2}
\end{array}
\right\}
=
\sum_{n=1}^{N}
\begin{bmatrix}
N_{n}^{u}(\zeta, \eta) & 0 & 0 & 0 & 0 \\
0 & N_{n}^{v}(\zeta, \eta) & 0 & 0 & 0 \\
0 & 0 & N_{n}^{w}(\zeta, \eta) & 0 & 0 \\
0 & 0 & 0 & N_{n}^{\theta_{1}}(\zeta, \eta) & 0 \\
0 & 0 & 0 & 0 & N_{n}^{\theta_{2}}(\zeta, \eta)
\end{bmatrix}
\left\{
\begin{array}{c}
U_{n}(t) \\
V_{n}(t) \\
W_{n}(t) \\
X_{n}(t) \\
Y_{n}(t)
\end{array}
\right\}
\tag{16}
$$

in which the normalized coordinates $\zeta=\frac{\mathrm{x}}{\mathrm{L}_{\mathrm{x}}}, \eta=\frac{\mathrm{y}}{\mathrm{L}_{\mathrm{y}}}$ are chosen for convenience and generality. $L_{x}$ and $L_{y}$ are corresponding plate dimensions in the $x$ and $y$ directions, respectively. In addition, $\mathrm{U}_{\mathrm{n}}(\mathrm{t}), \mathrm{V}_{\mathrm{n}}(\mathrm{t}), \mathrm{W}_{\mathrm{n}}(\mathrm{t}), \mathrm{X}_{\mathrm{n}}(\mathrm{t})$ and $\mathrm{Y}_{\mathrm{n}}(\mathrm{t})$ are unknown functions in time domain which should be determined. Moreover $\mathrm{N}$ is the number of shape functions which should guarantee the convergence of the displacement field and is related to the degree of the used polynomial (p) as $\frac{(p+1)(p+2)}{2}$. In addition, the approximated shape functions $\mathrm{N}^{\mathrm{u}}, \mathrm{N}^{\mathrm{v}}, \mathrm{N}^{\mathrm{w}}, \mathrm{N}^{\theta_{1}}$ and $\mathrm{N}^{\theta_{2}}$ are used in the form as follows [35]:

$$
\mathrm{N}^{\alpha}(\zeta, \eta)=\sum_{\mathrm{q}=0}^{\mathrm{p}} \sum_{\mathrm{i}=0}^{\mathrm{q}} \phi_{\mathrm{b}_{\alpha}}(\zeta, \eta)\left(\zeta^{\mathrm{i}} \eta^{\mathrm{q}-\mathrm{i}}\right) \quad \alpha=\mathrm{u}, \mathrm{v}, \mathrm{w}, \theta_{1}, \theta_{2} \tag{17}
$$

in which $\mathrm{p}$ is the degree set of the polynomial and $\phi_{\mathrm{b}_{\alpha}}$ is the corresponding boundary equation which should satisfy the boundary conditions.

As mentioned earlier, the approximated shape functions have to satisfy the essential boundary conditions that are:

$$
\begin{cases}
\mathrm{u}=\mathrm{v}=\mathrm{w}=0 & \text { Simply supported (S) } \\
\mathrm{u}=\mathrm{v}=\mathrm{w}=\theta_{1}=\theta_{2}=0 & \text { Clamped (C) } \\
\text { no restriction } & \text { Free (F) }
\end{cases} \tag{18}
$$

Substituting equation (17) into equation (16) and using equation (11), a system of 5N+1 nonlinear coupled equations will be achieved by setting $\delta \mathrm{u}=0, \delta \mathrm{v}=0, \delta \mathrm{w}=0, \delta \theta_{1}=0$ and $\delta \theta_{2}=0$ in the following form

$$
\begin{cases}
\mathrm{M} \ddot{\chi}+\mathrm{K} \chi=\mathrm{F} \\
\mathrm{m} \ddot{\mathrm{y}}=-\mathrm{F}_{\mathrm{c}}
\end{cases} \tag{19}
$$

Where

$$
\chi=\left\{\left\{\mathrm{U}_{\mathrm{n}}\right\},\left\{\mathrm{V}_{\mathrm{n}}\right\},\left\{\mathrm{W}_{\mathrm{n}}\right\},\left\{\mathrm{X}_{\mathrm{n}}\right\},\left\{\mathrm{Y}_{\mathrm{n}}\right\}\right\}^{\mathrm{T}} \tag{20}
$$

$$
\ddot{\chi}=\left\{\left\{\ddot{\mathrm{U}}_{\mathrm{n}}\right\},\left\{\ddot{\mathrm{V}}_{\mathrm{n}}\right\},\left\{\ddot{\mathrm{W}}_{\mathrm{n}}\right\},\left\{\ddot{\mathrm{X}}_{\mathrm{n}}\right\},\left\{\ddot{\mathrm{Y}}_{\mathrm{n}}\right\}\right\}^{\mathrm{T}} \tag{21}
$$

$$
\mathrm{F}=\left\{0,0, \mathrm{~F}_{\mathrm{c}} \mathrm{N}_{\mathrm{n}}^{\mathrm{w}}\left(\zeta_{\mathrm{c}}, \eta_{\mathrm{c}}\right), 0,0\right\}^{\mathrm{T}} \tag{22}
$$

$$
\mathrm{F}_{\mathrm{c}_{\mathrm{i}}}=\mathrm{K}_{\mathrm{c}} \alpha^{\frac{3}{2}}=\mathrm{K}_{\mathrm{c}}(\mathrm{y}-\mathrm{w})^{\frac{3}{2}}=\mathrm{K}_{\mathrm{c}}\left(\mathrm{y}-\sum_{\mathrm{n}=1}^{\mathrm{N}} \mathrm{W}_{\mathrm{n}}(\mathrm{t}) \mathrm{N}_{\mathrm{n}}^{\mathrm{w}}\left(\zeta_{\mathrm{c}}, \eta_{\mathrm{c}}\right)\right)^{\frac{3}{2}} \tag{23}
$$

The complete definition of $[\mathrm{M}]$ and $[\mathrm{K}]$ matrices are presented in Appendix A, and $(\zeta_{\mathrm{c}}, \eta_{\mathrm{c}})$ is the position of the impact. $\alpha$ is the indentation value, defined as the difference between the impactor displacement and the plate deflection at the impact position. The nonlinear time dependent system of equations (19) is solved via the fourth-order Runge-Kutta method with the following initial conditions:

$$
\begin{cases}
\mathrm{U}_{\mathrm{n}}(0)=0, \mathrm{~V}_{\mathrm{n}}(0)=0, \mathrm{~W}_{\mathrm{n}}(0)=0, \mathrm{X}_{\mathrm{n}}(0)=0, \mathrm{Y}_{\mathrm{n}}(0)=0 \\
\dot{\mathrm{U}}_{\mathrm{n}}(0)=0, \dot{\mathrm{V}}_{\mathrm{n}}(0)=0, \dot{\mathrm{W}}_{\mathrm{n}}(0)=0, \dot{\mathrm{X}}_{\mathrm{n}}(0)=0, \dot{\mathrm{Y}}_{\mathrm{n}}(0)=0 \\
\mathrm{y}(0)=0, \dot{\mathrm{y}}(0)=-\mathrm{V}_{0}
\end{cases} \tag{24}
$$

where y and $\mathrm{V}_{0}$ are the corresponding displacement and initial velocity of the impactor, respectively.

## 4. Results and discussions

### 4.1. Model validation and convergence

To validate the efficiency and accuracy of the proposed formulation, the low velocity impact response of a clamped circular isotropic plate previously studied by Abrate [36] and Shariyat [37] with the following material and geometrical properties is re-solved:

| Impactor: | $E$=199.95 GPa, $v$=0.33, $\rho$=7971.8 kg/m³,  r=19 mm, $V_0$=2.54 m/s |
|-----------|-----------------------------------------------------------------------|
| Circular plate: | $E$=68.95 GPa, $v$=0.33, $\rho$=2768 kg/m³,  R=38 mm, h=6 mm |

Fig. 1 shows a comparison between the time histories of contact force, impactor displacement and lateral plate deflection predicted by Abrate [36] and Shariyat [37] and the present model. The comparisons show that the results of the presented model are in good agreement with existing results and the differences may be caused by the use of different theories and solution approaches. Authors in [36] employed an approximate method based on two-degrees-of freedom discretization approach, whereas in the present model a more general continuous model based on HSDT is considered. In addition, Abrate [36] and Shariyat [37] employed nonlinear Von-Karman strain terms in their model while in the present model only the linear strain terms is considered. Although this causes some differences, it is noteworthy that the results predicted by the linear model are in good agreement with the nonlinear model in which the predicted maximum contact force by the present model has only less than 8% difference compared to those of predicted by Abrate [36] and Shariyat [37]. Moreover, as is clear, during the loading phase, the impactor displacement curves are almost coincide with each other while during the unloading phase when the large deflection effect is more pronounced, the more difference can be seen.

![](./images/813087247099232256_2.jpg)

Fig. 1. Time histories of (a) impactor displacement (solid line), lateral deflection of plate (dashed line) and (b) contact force predicted by Abrate [36], Shariyat [37] and the present model.

### 4.2. Example 1: impact response of circular FG-CNTRC plates

In this section, a comprehensive sensitive analysis is performed to delineate the effect of various parameters on the impact response of FG-CNTRC circular plates. In the following sub-sections, an X-CNTRC circular plate with a radius of R=200 mm and thickness of h=10 mm is considered unless specified otherwise (see Fig. 2). In addition, the plate is impacted at the center under thermal environmental condition, T=300 K by a steel spherical projectile with radius of r=15 mm, density of $\rho$=7960 kg/m³ and impact velocity of $V_0$=3 m/s. As mentioned earlier, the extended rule of mixtures is employed to evaluate the effective mechanical properties of the FG-CNTRC plate. Hence the temperature-dependent mechanical properties of both CNT reinforcement and matrix are required; these are tabulated in Table 1-3 in which $T=T_0+\Delta T$ and $T_0$=300 K, room temperature. In this study, (10, 10) SWCNT (tube length=9.26 nm, tube mean radius=0.68 nm and tube thickness=0.067 nm [9]) and Poly (methyl methacrylate) are chosen as reinforcement and matrix, respectively.

![](./images/813087247099232256_3.jpg)

Fig. 2. A circular plate impacted by a spherical projectile at the center

Table 1. Temperature-dependent mechanical and thermal properties of (10, 10) SWCNT (tube length=9.26 nm, tube main radius= 0.68 nm, tube thickness=0.067 nm) [9]

<table>
  <thead>
    <tr>
      <th>Temperature (K)</th>
      <th>$E_{11}^{\text{CNT}}$ (TPa)</th>
      <th>$E_{22}^{\text{CNT}}$ (TPa)</th>
      <th>$G_{12}^{\text{CNT}}$ (TPa)</th>
      <th>$\alpha_{11}^{\text{CNT}} \left( \times 10^{-6} / \text{K} \right)$</th>
      <th>$\alpha_{22}^{\text{CNT}} \left( \times 10^{-6} / \text{K} \right)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>300</td>
      <td>5.6466</td>
      <td>7.0800</td>
      <td>1.9445</td>
      <td>3.4584</td>
      <td>5.1682</td>
    </tr>
    <tr>
      <td>500</td>
      <td>5.5308</td>
      <td>6.9348</td>
      <td>1.9643</td>
      <td>4.5361</td>
      <td>5.0189</td>
    </tr>
    <tr>
      <td>700</td>
      <td>5.4744</td>
      <td>6.8641</td>
      <td>1.9644</td>
      <td>4.6677</td>
      <td>4.8943</td>
    </tr>
  </tbody>
</table>

Table 2. The CNT/matrix efficiency parameter for three different CNT volume fractions [10]

<table>
  <thead>
    <tr>
      <th>$V_{\text{CNT}}^{*}$</th>
      <th>$\eta_1$</th>
      <th>$\eta_2$</th>
      <th>$\eta_3$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.12</td>
      <td>0.137</td>
      <td>1.022</td>
      <td>0.715</td>
    </tr>
    <tr>
      <td>0.17</td>
      <td>0.142</td>
      <td>1.626</td>
      <td>1.138</td>
    </tr>
    <tr>
      <td>0.28</td>
      <td>0.141</td>
      <td>1.585</td>
      <td>1.109</td>
    </tr>
  </tbody>
</table>

Table 3. Temperature-dependent mechanical and thermal properties of Poly (methyl methacrylate) [10]

<table>
  <thead>
    <tr>
      <th>$\rho^{\text{m}} \left( \text{kg} / \text{m}^3 \right)$</th>
      <th>$v^{\text{m}}$</th>
      <th>$\text{E}^{\text{m}} \left( \text{GPa} \right)$</th>
      <th>$\alpha^{\text{m}} \left( \times 10^{-6} / \text{K} \right)$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1150</td>
      <td>0.34</td>
      <td>3.52-0.0034T</td>
      <td>45(1+0.0005$\Delta$T)</td>
    </tr>
  </tbody>
</table>

### 4.2.1. Boundary conditions effect

To study the boundary conditions effect, two cases are considered: an X-CNTRC circular plate with simply supported and fully clamped boundary conditions. The contact force, lateral deflection of the plate, and impactor velocity are depicted in Fig. 3-(a), (b) and (c), respectively.

The peak contact force and the lateral deflection of the simply supported plate are greater than

those of the fully clamped one. The simply supported boundary conditions permit the plate to be more flexible than the fully clamped one, hence more kinetic energy is absorbed in the form of strain energy and greater lateral deflection and lower residual velocity of the impactor compared to the simply supported case will result (see Fig. 3-(c)).

![](./images/813087247099232256_4.jpg)

Fig. 3. Low velocity impact characteristics of simply supported and fully clamped X-CNTRC circular plate with $v_{\text{CNT}}^*=0.28$: (a)-contact force, (b)-lateral deflection and (c)-impactor velocity

4.2.2. Thermal field effect

In the present part, the thermal environment effect on the impact response of an X-CNTRC circular plate is investigated. To achieve this purpose, a fully clamped X-CNTRC circular plate is subjected to temperature rising prior to impact loading. Since the temperature-dependent properties of the studied CNT are available only for three temperatures, i.e. T=300, 500 and 700 K, two temperature rises ($\Delta$T=200, 400 K) are considered and their relevant results are illustrated in Fig. 4. The temperature-dependent material properties of both CNT and Poly methyl methacrylate (see Table 1 and 3) show that temperature rising reduces the structural stiffness values, hence an increased temperature in the CNTRC-plate, results in lower peak contact force while it increases the indentation value and contact duration which can be deduced from Fig. 4. Results confirm that the thermal environment effect on the impact characteristics of CNTRC plates especially on maximum indentation value, is enormous (the indentation value ranged from 0.23 mm to 0.31 mm (35%) by a temperature rise of $\Delta$T=400) and should be taken into consideration during the design processes. For instance, improving in the global stiffness of plate through an increase in the plate thickness can reduce the impactor indentation.

![](./images/813087247099232256_5.jpg)

Fig. 4. The temperature rise effect on the time history of (a)-contact force and (b)-indentation of X-
CNTRC circular plates with $v_{\text{CNT}}^*=0.28$

### 4.2.3. CNT distribution and its volume fraction effect

Herein the effect of CNT distribution profile as well as its volume fraction on the impact
response of FG-CNTRC circular plates are investigated. Hence a fully clamped FG-CNTRC
plate with three distributions profiles, i.e. UD, V, and X with different volume fractions, i.e.
$v_{\text{CNT}}^*=0.12,0.17$ and $0.28$ , is considered. The relevant impact characteristics including
Maximum Contact Force (MCF), maximum lateral deflection$(w_{\text{max}})$, maximum indentation
$(\alpha_{\text{max}})$ and the contact duration$(T_0)$ are tabulated in Table 4. Moreover, toward a better
understanding of the distribution profile effect, the impact response of the mentioned plate with
UD, V and X distributions of CNT along the plate thickness with volume fraction of 0.28 is
illustrated in Fig. 5. It can be inferred from the presented results that for all different CNT
volume fraction values, the plate with the both X and V distribution profiles have almost very

close MCF and maximum indentation values. Since the volume fraction value of both mentioned distribution profiles are the same at the top surface of the plate where impact occurs. In addition the least maximum lateral deflection is predicted for the plate with X-CNTRC distribution profile which may be result of optimum distribution of $v_{\text{CNT}}^{*}$ along plate thickness. Moreover, it can be observed from Table 4 that an increase in the CNT volume fraction leads to higher MCF and lower contact duration, maximum indentation and maximum lateral deflection due to increases in the structural stiffness as well as contact stiffness (See equations (3) and (10)).

Table 4. The CNT volume fraction and its distribution profile effect on the impact response of CNTRC circular plates

<table>
<thead>
  <tr>
    <th>$v_{c}^{i}$</th>
    <th>Pr ofile</th>
    <th>MCF (kN)</th>
    <th>$\alpha_{\text{max}}($ mm)</th>
    <th>$\text{w}_{\text{max}}($ mm)</th>
    <th>T $_{0}$($\mu$s)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="6">0 .12</td>
    <td>U</td>
    <td>1.766</td>
    <td>0.24</td>
    <td>0.466</td>
    <td>5</td>
  </tr>
  <tr>
    <td>D</td>
    <td></td>
    <td>2</td>
    <td></td>
    <td>88</td>
  </tr>
  <tr>
    <td>V</td>
    <td>1.840</td>
    <td>0.22</td>
    <td>0.516</td>
    <td>6</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>6</td>
    <td></td>
    <td>12</td>
  </tr>
  <tr>
    <td>X</td>
    <td>1.880</td>
    <td>0.22</td>
    <td>0.414</td>
    <td>5</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>9</td>
    <td></td>
    <td>55</td>
  </tr>
  <tr>
    <td rowspan="6">0 .17</td>
    <td>U</td>
    <td>2.207</td>
    <td>0.20</td>
    <td>0.370</td>
    <td>4</td>
  </tr>
  <tr>
    <td>D</td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>70</td>
  </tr>
  <tr>
    <td>V</td>
    <td>2.359</td>
    <td>0.18</td>
    <td>0.411</td>
    <td>4</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>0</td>
    <td></td>
    <td>92</td>
  </tr>
  <tr>
    <td>X</td>
    <td>2.410</td>
    <td>0.18</td>
    <td>0.323</td>
    <td>4</td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td>2</td>
    <td></td>
    <td>42</td>
  </tr>
</tbody>
</table>

<table>
<tbody><tr><td>U</td><td>2.406</td><td>0.19</td><td>0.309</td><td>4</td></tr>
<tr><td>0 D</td><td></td><td>6</td><td></td><td>29</td></tr>
<tr><td>.28 V</td><td>2.802</td><td>0.15</td><td>0.336</td><td>4</td></tr>
<tr><td></td><td></td><td>8</td><td></td><td>41</td></tr>
<tr><td>X</td><td>2.850</td><td>0.16</td><td>0.260</td><td>4</td></tr>
<tr><td></td><td></td><td>0</td><td></td><td>08</td></tr>
</tbody></table>

![](./images/813087247099232256_6.jpg)

![](./images/813087247099232256_7.jpg)

![](./images/813087247099232256_8.jpg)

Fig. 5. The distribution profile effect on the time history of (a)-contact force, (b)-indentation and (c)-lateral deflection of FG-CNTRC circular plates with $\mathrm{v}_{\mathrm{CNT}}^{*}=0.28$

### 4.2.4. Initial kinetic energy of impactor effect

The influence of the impactor kinetic energy before the impact - which is known as initial kinetic energy of impactor on the low velocity impact response of the X-CNTRC circular plate is analyzed in this part. In this regard, the initial kinetic energy of impactor is doubled in two ways: increasing the impactor mass by fixing its initial velocity and vice versa. As is clear, both the MCF and the maximum lateral deflection increase when the initial kinetic energy of the impactor increases. The results shown in Fig. 6 confirm that the impact response of the studied plate at the fixed initial kinetic energy of impactor is extremely dependent on its mass and velocity. It can be deduced that at the fixed initial kinetic energy, the contact force is significantly affected by the

impactor velocity while the maximum lateral deflection is significantly affected by the impactor mass. It should be noted that an increase in the impactor velocity does not affect the contact duration whereas this increases when the impactor mass increases. This can be explained by the fact that as the impactor velocity changes, the only effect will be a change in the initial conditions (See equation (24)) while a variation to the mass impactor will change the mass matrix of equation (19) which can affect the global response of the plate.

![](./images/813087247099232256_9.jpg)

Fig. 6. The initial kinetic energy of impactor effect on the time history of (a)-contact force and (b)-lateral deflection of X-CNTRC circular plates with $v_{\mathrm{CNT}}^{*}=0.28$

### 4.3. Example 2: impact response of triangular FG-CNTRC plates

In the following parts, the low velocity impact response of FG-CNTRC triangular plates is presented. Therefore, an equilateral triangle with sides of AB=BC=CA=200 mm and thickness of h=10 mm impacted by a spherical projectile at the center, is considered (see Fig. 7). All the

remaining relevant parameters are the same as those used for the FG-CNTRC circular plate in the previous example unless stated otherwise.

![](./images/813087247099232256_10.jpg)

Fig. 7. An equilateral triangular plate impacted by a spherical projectile at the center

### 4.3.1. Boundary conditions effect

Among the all possible boundary conditions, four cases i.e. an X-CNTRC plate with CCC, CFF, CSF, SSS are considered in this part. The symbolism CSF, for example, represents a triangular with edges AB, BC and CA with clamped, simply supported and free boundary conditions, respectively. The corresponding impact characteristics including the time history of contact force, lateral deflection at impact point and impactor velocity are illustrated in Fig. 8. As is shown, changing the boundary conditions will change the impact response of the X-CNTRC plate. The results indicate that in the case of CCC, due to its lesser flexibility, the plate has the lowest maximum deflection of the plate at impact position as well as the lowest absorbed energy with the highest MCF compared to the other studied cases. In contrast, in the case of CFF

boundary condition, the plate is more flexible and more kinetic energy is absorbed in the form of strain energy which causes less residual impactor velocity (see Fig. 8-c).

![](./images/813087247099232256_11.jpg)

Fig. 8. The boundary conditions effect on the Low velocity impact response of X-CNTRC triangular plates with $v_{\text{CNT}}^{*}=0.28$ : (a)-contact force, (b)-lateral deflection and (c)-impactor velocity history.

### 4.3.2. Thermal field effect

In this part, the effect of temperature rising on the impact response of fully clamped X-CNTRC triangular plates is investigated. According to the shown temperature-dependent material properties of both CNT and Poly methyl methacrylate in Table 1 and 3, as the temperature increases, the plate stiffness will be decreased and higher indentation value will be the result. Moreover, compressive reaction forces at the clamped edges will be applied as the temperature increases. Hence the compressive in-plane loading decreases the geometrical stiffness and consequently a reduction in the MCF will be the result, as can be deduced from the plotted results in Fig. 8.

![](./images/813087247099232256_12.jpg)

Fig. 9. The temperature rise effect on the time history of (a)-contact force and (b)-indentation of X-
CNTRC triangular plates with $v_{\text{CNT}}^{*}=0.28$

### 4.3.3. CNT distribution and its volume fraction effect

The effect of CNT volume fraction and its distribution profile on the impact characteristics of
a simply supported FG-CNTRC triangular plate are studied herein. The presented results in

Table 5 confirm that as the volume fraction increases, since the contact stiffness and the structural stiffness are increased, the maximum indentation, maximum deflection and contact duration will be decreased while the MCF increased. Moreover, for all CNT volume fractions, the X distribution profile leads to the lowest maximum deflection as well as the lowest contact duration and the highest MCF which are similar to those tabulated in Table 4 for the circular plate.

Table 5. The CNT volume fraction and its distribution profile effect on the impact response of CNTRC triangular plates

<table>
  <thead>
    <tr>
      <th>$v_{CNT}^{*}$</th>
      <th>Profile</th>
      <th>MCF(kN)</th>
      <th>$\alpha_{max}$(mm)</th>
      <th>$w_{max}$(mm)</th>
      <th>$T_{0}$($\mu$s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">0.12</td>
      <td>UD</td>
      <td>2.334</td>
      <td>0.292</td>
      <td>0.212</td>
      <td>492</td>
    </tr>
    <tr>
      <td>V</td>
      <td>2.384</td>
      <td>0.269</td>
      <td>0.222</td>
      <td>481</td>
    </tr>
    <tr>
      <td>X</td>
      <td>2.479</td>
      <td>0.276</td>
      <td>0.197</td>
      <td>464</td>
    </tr>
    <tr>
      <td rowspan="3">0.17</td>
      <td>UD</td>
      <td>2.877</td>
      <td>0.238</td>
      <td>0.166</td>
      <td>394</td>
    </tr>
    <tr>
      <td>V</td>
      <td>2.984</td>
      <td>0.210</td>
      <td>0.177</td>
      <td>379</td>
    </tr>
    <tr>
      <td>X</td>
      <td>3.103</td>
      <td>0.216</td>
      <td>0.157</td>
      <td>366</td>
    </tr>
    <tr>
      <td rowspan="3">0.28</td>
      <td>UD</td>
      <td>3.061</td>
      <td>0.230</td>
      <td>0.143</td>
      <td>366</td>
    </tr>
    <tr>
      <td>V</td>
      <td>3.328</td>
      <td>0.177</td>
      <td>0.158</td>
      <td>332</td>
    </tr>
    <tr>
      <td>X</td>
      <td>3.394</td>
      <td>0.179</td>
      <td>0.147</td>
      <td>324</td>
    </tr>
  </tbody>
</table>

## 5. Conclusion

In the present research, a semi analytical model is developed to study the low velocity impact response of temperature-dependent carbon nanotube reinforced composite plates with general geometrical shape based on the free-mesh Ritz method. The distribution of CNT across the

thickness may be uniform or functionally graded. The equivalent material properties of the reinforced composite are estimated according to the extended rule of mixtures. Kinematic equations of the plate are evaluated based on high-order shear deformation theory and the governing equations are derived using Hamilton's principle. The components of Hamilton's equation are determined using a developed integration scheme suitable for arbitrary domain. A Ritz-based solution approach appropriate for general boundary conditions is incorporated into Hertzian contact law to establish the equations in space domain in the form of matrix representation. The equations in time domain are then dealt with using the well-known fourth-order Runge-Kutta method. Numerical results are provided to assess the effect of boundary conditions, thermal field, initial kinetic energy of impactor, CNT volume fraction and its distribution profile on the time history of contact force, indentation, impactor velocity and lateral deflection of FG-CNTRC plates with circular and triangular geometrical shapes. Results show that the impact response of FG-CNTRC plates will be affected in different boundary conditions. Besides, since the structural stiffness of the plate decreases with temperature rising, temperature elevation leads to higher indentation and lower maximum contact force. It was found that with the same initial kinetic energy of impactor, the maximum contact force and the maximum lateral deflection of the plate are extremely dependent on the impactor velocity and mass, respectively. It is concluded that, regardless of the plate geometry, the CNT volume fraction and its distribution profile are highly influential on the impact response of FG-CNTRC plates and increasing the CNT volume fraction causes lower indentation as well as maximum deflection at impact position due to increases in structural and contact stiffness. In addition, the distribution profile of type X pattern results in lower maximum deflection and higher maximum contact force.

### Appendix A

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{uu}}\right]=\int_{\Omega} \mathrm{I}_{0} \mathrm{~N}_{\mathrm{n}}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}}^{\mathrm{u}} \mathrm{L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{uv}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{uw}}\right]=-\int_{\Omega} \mathrm{I}_{1} \mathrm{~L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}}^{\mathrm{u}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{u} \theta_{1}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{0}} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}}^{\mathrm{u}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{u} \theta_{2}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{vu}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{vv}}\right]=\int_{\Omega} \mathrm{I}_{0} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}}^{\mathrm{v}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{vw}}\right]=-\int_{\Omega} \mathrm{I}_{1} \mathrm{~L}_{\mathrm{x}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}}^{\mathrm{v}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{v} \theta_{1}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{v} \theta_{2}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{0}} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}}^{\mathrm{v}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{wu}}\right]=-\int_{\Omega} \mathrm{I}_{1} \mathrm{~L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{w}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{wv}}\right]=-\int_{\Omega} \mathrm{I}_{1} \mathrm{~L}_{\mathrm{x}} \mathrm{N}_{\mathrm{n}}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{w}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{w} \theta_{1}}\right]=-\int_{\Omega} \mathrm{I}_{\mathrm{f}_{1}} \mathrm{~L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{w}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{w} \theta_{2}}\right]=-\int_{\Omega} \mathrm{I}_{\mathrm{f}_{1}} \mathrm{~L}_{\mathrm{x}} \mathrm{N}_{\mathrm{n}}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{w}} \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{1} \mathrm{u}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{0}} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}}^{\theta_{1}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{1} \mathrm{v}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{1} \mathrm{w}}\right]=-\int_{\Omega} \mathrm{I}_{\mathrm{f}_{1}} \mathrm{~L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}}^{\theta_{1}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{1} \theta_{1}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{\mathrm{f}}} \mathrm{L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}}^{\theta_{1}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{1} \theta_{2}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{2} \mathrm{u}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{2} \mathrm{v}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{0}} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}}^{\theta_{2}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{2} \mathrm{w}}\right]=-\int_{\Omega} \mathrm{I}_{\mathrm{f}_{1}} \mathrm{~L}_{\mathrm{x}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}}^{\theta_{2}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{2} \theta_{1}}\right]=0
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\theta_{2} \theta_{2}}\right]=\int_{\Omega} \mathrm{I}_{\mathrm{f}_{\mathrm{f}}} \mathrm{L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}}^{\theta_{2}} \mathrm{~d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{M}_{\mathrm{mn}}^{\mathrm{ww}}\right]=\int_{\Omega}\left(\mathrm{I}_{0} \mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}}^{\mathrm{w}}+\mathrm{I}_{2} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{w}}+\mathrm{I}_{2} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left\{\begin{array}{c}
\mathrm{I}_{0} \\
\mathrm{I}_{1} \\
\mathrm{I}_{2} \\
\mathrm{I}_{\mathrm{f}_{0}} \\
\mathrm{I}_{\mathrm{f}_{1}} \\
\mathrm{I}_{\mathrm{f}_{\mathrm{f}}}
\end{array}\right\}=\int_{-\frac{\mathrm{h}}{2}}^{\frac{\mathrm{h}}{2}} \rho_{0}\left\{\begin{array}{c}
1 \\
\mathrm{z} \\
\mathrm{z}^{2} \\
\mathrm{f}(\mathrm{z}) \\
\mathrm{zf}(\mathrm{z}) \\
(\mathrm{f}(\mathrm{z}))^{2}
\end{array}\right\}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{uu}}\right]=\int_{\Omega}\left(\mathrm{A}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{A}_{16} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{A}_{16} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}+\mathrm{A}_{66} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{uv}}\right]=\int_{\Omega}\left(\mathrm{A}_{12} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{A}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{A}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}+\mathrm{A}_{66} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{uw}}\right]=-} & \int_{\Omega}\left(\mathrm{B}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}{ }^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{B}_{12} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+2 \mathrm{~B}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{B}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right. \\
& \left.+\mathrm{B}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}{ }^{2}} \mathrm{~N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}+2 \mathrm{~B}_{66} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{u} \theta_{1}}\right]=\int_{\Omega}\left(\mathrm{E}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{E}_{16} \mathrm{~N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{E}_{66} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{u}}+\mathrm{E}_{16} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{u} \theta_{2}}\right]=\int_{\Omega}\left(\mathrm{E}_{12} \mathrm{~N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{E}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{u}}+\mathrm{E}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{u}}+\mathrm{E}_{66} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{vu}}\right]=\int_{\Omega}\left(\mathrm{A}_{12} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{A}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{A}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}+\mathrm{A}_{66} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{vv}}\right]=\iint_{\Omega}\left(\mathrm{A}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{A}_{26} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{A}_{26} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}+\mathrm{A}_{66} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{vw}}\right]=-} & \iint_{\Omega}\left(\mathrm{B}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{B}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}+2 \mathrm{~B}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{v}}\right. \\
& \left.+\mathrm{B}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}+\mathrm{B}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}+2 \mathrm{~B}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{v}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{v} \theta_{1}}\right]=\iint_{\Omega}\left(\mathrm{E}_{12} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{E}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{E}_{66} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{u}}+\mathrm{E}_{16} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{u}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{v} \theta_{2}}\right]=\iint_{\Omega}\left(\mathrm{E}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{E}_{26} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta}^{\mathrm{v}}+\mathrm{E}_{26} \mathrm{~N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{v}}+\mathrm{E}_{66} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta}^{\mathrm{v}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{wu}}\right]=-} & \iint_{\Omega}\left(\mathrm{B}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{B}_{12} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+\mathrm{B}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}\right. \\
& \left.+2 \mathrm{~B}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}+\mathrm{B}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+2 \mathrm{~B}_{66} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{wv}}\right]=-} & \iint_{\Omega}\left(\mathrm{B}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{B}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{B}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+\mathrm{B}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}\right. \\
& \left.+2 \mathrm{~B}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}+2 \mathrm{~B}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{ww}}\right]=} & \iint_{\Omega}\left(\mathrm{D}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{3}} \mathrm{~N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{D}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+2 \mathrm{D}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{D}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}\right. \\
& +\mathrm{D}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{3}} \mathrm{~N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+2 \mathrm{D}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+2 \mathrm{D}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}+2 \mathrm{D}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}} \\
& \left.+4 \mathrm{D}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}-\mathrm{N}_{\mathrm{xx}} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{w}}-\mathrm{N}_{\mathrm{yy}} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{w}}-\mathrm{N}_{\mathrm{xy}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\mathrm{w}}-\mathrm{N}_{\mathrm{xy}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{w} \theta_{1}}\right]=} & -\iint_{\Omega}\left(\mathrm{F}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{F}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{F}_{12} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+\mathrm{F}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}\right. \\
& \left.+2 \mathrm{~F}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}+2 \mathrm{~F}_{66} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{~N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\mathrm{w} \theta_{2}}\right]=} & -\iint_{\Omega}\left(\mathrm{F}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{F}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta \zeta}^{\mathrm{w}}+\mathrm{F}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}+\mathrm{F}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \eta \eta}^{\mathrm{w}}\right. \\
& \left.+2 \mathrm{~F}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}+2 \mathrm{~F}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{~N}_{\mathrm{m}, \zeta \eta}^{\mathrm{w}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{1} \mathrm{u}}\right]=\iint_{\Omega}\left(\mathrm{E}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{E}_{16} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{E}_{16} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+\mathrm{E}_{66} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{1} \mathrm{v}}\right]=\iint_{\Omega}\left(\mathrm{E}_{12} \mathrm{~N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{E}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{E}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+\mathrm{E}_{66} \mathrm{~N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{1} \mathrm{w}}\right]=} & -\iint_{\Omega}\left(\mathrm{F}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{~N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{F}_{12} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+2 \mathrm{~F}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{F}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}\right. \\
& \left.+\mathrm{F}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{~N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+2 \mathrm{~F}_{66} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{1} \theta_{1}}\right]=\iint_{\Omega}\left(\mathrm{H}_{11} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{H}_{16} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{H}_{16} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+\mathrm{H}_{66} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+\mathrm{K}_{55} \mathrm{L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{1}} \mathrm{N}_{\mathrm{m}}^{\theta_{1}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{1} \theta_{2}}\right]=\iint_{\Omega}\left(\mathrm{H}_{12} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{H}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{1}}+\mathrm{H}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}+\mathrm{H}_{66} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{1}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{2} \mathrm{u}}\right]=\iint_{\Omega}\left(\mathrm{E}_{12} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{E}_{26} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{E}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{E}_{66} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{u}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{2} \mathrm{v}}\right]=\iint_{\Omega}\left(\mathrm{E}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{E}_{26} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{E}_{26} \mathrm{N}_{\mathrm{n}, \eta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{E}_{66} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\mathrm{v}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{aligned}
{\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{2} \mathrm{w}}\right]=-} & \iint_{\Omega}\left(\mathrm{F}_{12} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{F}_{22} \frac{\mathrm{L}_{\mathrm{x}}}{\mathrm{L}_{\mathrm{y}}^{2}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+2 \mathrm{F}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{F}_{16} \frac{\mathrm{L}_{\mathrm{y}}}{\mathrm{L}_{\mathrm{x}}^{2}} \mathrm{N}_{\mathrm{n}, \zeta \zeta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}\right. \\
& \left.+\mathrm{F}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+2 \mathrm{F}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta \eta}^{\mathrm{w}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}\right) \mathrm{d} \zeta \mathrm{d} \eta
\end{aligned}
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{2} \theta_{1}}\right]=\iint_{\Omega}\left(\mathrm{H}_{12} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{H}_{26} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{H}_{16} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{H}_{66} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{1}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\left[\mathrm{K}_{\mathrm{mn}}^{\theta_{2} \theta_{2}}\right]=\iint_{\Omega}\left(\mathrm{H}_{22} \frac{1}{\mathrm{~L}_{\mathrm{y}}} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{H}_{26} \mathrm{N}_{\mathrm{n}, \eta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{H}_{26} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \eta}^{\theta_{2}}+\mathrm{H}_{66} \frac{1}{\mathrm{~L}_{\mathrm{x}}} \mathrm{N}_{\mathrm{n}, \zeta}^{\theta_{2}} \mathrm{N}_{\mathrm{m}, \zeta}^{\theta_{2}}+\mathrm{K}_{44} \mathrm{L}_{\mathrm{x}} \mathrm{L}_{\mathrm{y}} \mathrm{N}_{\mathrm{n}}^{\theta_{2}} \mathrm{N}_{\mathrm{m}}^{\theta_{2}}\right) \mathrm{d} \zeta \mathrm{d} \eta
$$

$$
\begin{Bmatrix}
A_{ij} \
B_{ij} \
D_{ij} \
E_{ij} \
F_{ij} \
H_{ij}
\end{Bmatrix}
=
\sum_{k=1}^{n}
\int_{z_k}^{z_{k+1}}
\overline{Q}_{ij}^{(k)}
\begin{Bmatrix}
1 \
z \
z^2 \
f(z) \
z f(z) \
\bigl(f(z)\bigr)^2
\end{Bmatrix}
dz
\quad
i,j=1,2,6
$$

$$
K_{ij}
=
\sum_{k=1}^{n}
\int_{z_k}^{z_{k+1}}
\overline{Q}_{ij}^{(k)}
\bigl(f'(z)\bigr)^2 dz
\quad
i,j=4,5
$$

## References

[1] Ho YH, Chang CP, Shyu FL, Chen RB, Chen SC, Lin MF. Electronic and optical properties of double-walled armchair carbon nanotubes. Carbon N Y 2004;42:3159-67.
doi:10.1016/j.carbon.2004.07.027.

[2] Ruoff RS, Qian D, Liu WK. Mechanical properties of carbon nanotubes: Theoretical predictions and experimental measurements. Comptes Rendus Phys 2003;4:993-1008.
doi:10.1016/j.crhy.2003.08.001.

[3] Manchado MAL, Valentini L, Biagiotti J, Kenny JM. Thermal and mechanical properties of single-walled carbon nanotubes-polypropylene composites prepared by melt processing. Carbon N Y 2005;43:1499-505. doi:10.1016/j.carbon.2005.01.031.

[4] Liew KM, Lei ZX, Zhang LW. Mechanical analysis of functionally graded carbon nanotube reinforced composites: A review. Compos Struct 2015;120:90-7.
doi:10.1016/j.compstruct.2014.09.041.

[5] Lin F, Xiang Y. Vibration of carbon nanotube reinforced composite beams based on the first and third order beam theories. Appl Math Model 2014;38:3741-54.
doi:10.1016/j.apm.2014.02.008.

[6] Yas MH, Samadi N. Free vibrations and buckling analysis of carbon nanotube-reinforced composite Timoshenko beams on elastic foundation. Int J Press Vessel Pip 2012;98:119-
28. doi:10.1016/j.ijpvp.2012.07.012.

[7] Lin F, XIANG Y. Numerical Analysis on Nonlinear Free Vibration of Carbon Nanotube Reinforced Composite Beams. Int J Struct Stab Dyn 2014;14:1350056.

doi:10.1142/S0219455413500569.

[8] Jam JE, Kiani Y. Low velocity impact response of functionally graded carbon nanotube reinforced composite beams in thermal environment. Compos Struct 2015;132:35-43. doi:10.1016/j.compstruct.2015.04.045.

[9] Shen H-S. Nonlinear bending of functionally graded carbon nanotube-reinforced composite plates in thermal environments. Compos Struct 2009;91:9-19. doi:10.1016/j.compstruct.2009.04.026.

[10] Wang Z-X, Xu J, Qiao P. Nonlinear low-velocity impact analysis of temperature-dependent nanotube-reinforced composite plates. Compos Struct 2014;108:423-34. doi:10.1016/j.compstruct.2013.09.024.

[11] Ansari R, Torabi J, Shojaei MF. Buckling and vibration analysis of embedded functionally graded carbon nanotube-reinforced composite annular sector plates under thermal loading. Compos Part B Eng 2017;109:197-213. doi:10.1016/j.compositesb.2016.10.050.

[12] Kiani Y. Free vibration of functionally graded carbon nanotube reinforced composite plates integrated with piezoelectric layers. Comput Math with Appl 2016;72:2433-49. doi:10.1016/j.camwa.2016.09.007.

[13] Ansari R, Torabi J. Numerical study on the buckling and vibration of functionally graded carbon nanotube-reinforced composite conical shells under axial loading. Compos Part B Eng 2016;95:196-208. doi:10.1016/j.compositesb.2016.03.080.

[14] Shen H-S, Xiang Y. Nonlinear vibration of nanotube-reinforced composite cylindrical shells in thermal environments. Comput Methods Appl Mech Eng 2012;213-216:196-

205. doi:10.1016/j.cma.2011.11.025.

[15] Jooybar N, Malekzadeh P, Fiouz A. Vibration of functionally graded carbon nanotubes reinforced composite truncated conical panels with elastically restrained against rotation edges in thermal environment. Compos Part B Eng 2016;106:242-61. doi:10.1016/j.compositesb.2016.09.030.

[16] Bayat MR, Rahmani O, Mosavi Mashhadi M. Nonlinear low-velocity impact analysis of functionally graded nanotube-reinforced composite cylindrical shells in thermal environments. Polym Compos 2016;In press. doi:10.1002/pc.

[17] Shen H-S, Zhang C-L. Thermal buckling and postbuckling behavior of functionally graded carbon nanotube-reinforced composite plates. Mater Des 2010;31:3403-11. doi:10.1016/j.matdes.2010.01.048.

[18] Shen H-S. Thermal buckling and postbuckling behavior of functionally graded carbon nanotube-reinforced composite cylindrical shells. Compos Part B Eng 2012;43:1030-8. doi:10.1016/j.compositesb.2011.10.004.

[19] Wang Z-X, Shen H-S. Nonlinear vibration and bending of sandwich plates with nanotube- reinforced composite face sheets. Compos Part B Eng 2012;43:411-21. doi:10.1016/j.compositesb.2011.04.040.

[20] Lei ZX, Liew KM, Yu JL. Buckling analysis of functionally graded carbon nanotube- reinforced composite plates using the element-free kp-Ritz method. Compos Struct 2013;98:160-8. doi:10.1016/j.compstruct.2012.11.006.

[21] Lei ZX, Liew KM, Yu JL. Large deflection analysis of functionally graded carbon

nanotube-reinforced composite plates by the element-free kp-Ritz method. Comput Methods Appl Mech Eng 2013;256:189-99. doi:10.1016/j.cma.2012.12.007.

[22] Lei ZX, Liew KM, Yu JL. Free vibration analysis of functionally graded carbon nanotube- reinforced composite plates using the element-free kp-Ritz method in thermal environment. Compos Struct 2013;106:128-38. doi:10.1016/j.compstruct.2013.06.003.

[23] Zarei H, Fallah M, Minak G, Bisadi H, Daneshmehr AR. Low velocity impact analysis of Fiber Metal Laminates (FMLs) in thermal environments with various boundary conditions. Compos Struct 2016;149:170-83. doi:10.1016/j.compstruct.2016.04.036.

[24] Zarei H, Sadighi M, Minak G. Ballistic analysis of fiber metal laminates impacted by flat and conical impactors. Compos Struct 2017;161:65-72. doi:10.1016/j.compstruct.2016.11.047.

[25] Zarei H, Brugo T, Belcari J, Bisadi H, Minak G, Zucchelli A. Low Velocity Impact Damage Assessment of GLARE Fiber-Metal Laminates Interleaved by Nylon 6,6 Nanofiber Mats. Compos Struct 2017. doi:10.1016/j.compstruct.2017.01.079.

[26] Wang Z-X, Shen H-S. Nonlinear dynamic response of nanotube-reinforced composite plates resting on elastic foundations in thermal environments. Nonlinear Dyn 2012;70:735-54. doi:10.1007/s11071-012-0491-2.

[27] Malekzadeh P, Dehbozorgi M. Low velocity impact analysis of functionally graded carbon nanotubes reinforced composite skew plates. Compos Struct 2016;140:728-48. doi:10.1016/j.compstruct.2016.01.045.

[28] Bharti I, Gupta N, Gupta KM. Novel applications of functionally graded nano,

optoelectronic and thermoelectric materials. Int J Mater Mech Manuf 2013;1:221-4.

doi:10.7763/IJMMM.2013.V1.47.

[29] Zarei H, Fallah M, Bisadi H, Daneshmehr A, Minak G. Multiple impact response of temperature-dependent carbon nanotube -reinforced composite (CNTRC) plates with general boundary conditions. Compos Part B Eng 2017;113:206-17.

doi:10.1016/j.compositesb.2017.01.021.

[30] Kiani Y. Shear buckling of FG-CNT reinforced composite plates using Chebyshev-Ritz method. Compos Part B Eng 2016;105:176-87. doi:10.1016/j.compositesb.2016.09.001.

[31] Kiani Y. Free vibration of FG-CNT reinforced composite spherical shell panels using Gram-Schmidt shape functions. Compos Struct 2017;159:368-81.

doi:10.1016/j.compstruct.2016.09.079.

[32] Daneshmehr AR, Rajabpoor A, Hadi A. Size dependent free vibration analysis of nanoplates made of functionally graded materials based on nonlocal elasticity theory with high order theories. Int J Eng Sci 2015;95:23-35.

doi:http://dx.doi.org/10.1016/j.ijengsci.2015.05.011.

[33] Daneshmehr AR, Rajabpoor A, Pourdavood M. Stability of size dependent functionally graded nanoplate based on nonlocal elasticity and higher order plate theories and different boundary conditions. Int J Eng Sci 2014;82:84-100. doi:10.1016/j.ijengsci.2014.04.017.

[34] Mohammad-Abadi M, Daneshmehr AR. Modified couple stress theory applied to dynamic analysis of composite laminated beams by considering different beam theories. Int J Eng Sci 2015;87:83-102. doi:10.1016/j.ijengsci.2014.11.003.

[35] Wang CM, Liew KM. Buckling of triangular plates under uniform compression. Eng Struct 1994;16:43–50. doi:10.1016/0141-0296(94)90103-1.

[36] Abrate S. Impact on Composite Structures. Cambridge University press; 1998.

[37] Shariyat M, Jafari R. Nonlinear low-velocity impact response analysis of a radially preloaded two-directional-functionally graded circular plate: A refined contact stiffness approach. Compos Part B Eng 2013;45:981–94. doi:10.1016/j.compositesb.2012.05.014.