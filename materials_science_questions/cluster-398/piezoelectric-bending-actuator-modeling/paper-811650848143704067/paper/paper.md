# Buckling and post-buckling analyses for an axially compressed laminated cylindrical shell of FGM with PFRC in thermal environments

Hong-Liang Dai $^{a,b,*}$, Hong-Yan Zheng $^{b}$

$^{a}$State Key Laboratory of Advanced Design and Manufacturing for Vehicle Body, Hunan University, Changsha 410082, China
$^{b}$Department of Engineering Mechanics, College of Mechanical \& Vehicle Engineering, Hunan University, Changsha 410082, China

---

## ARTICLE INFO

Article history:
Received 2 October 2010
Accepted 11 May 2011
Available online 16 June 2011

Keywords:
Buckling
Post-buckling
Laminated cylindrical shell
Functionally graded material
Piezoelectric fiber reinforced composite

---

## ABSTRACT

In this paper, investigation on buckling and post-buckling behaviors of a laminated cylindrical shell of functionally graded material (FGM) with the piezoelectric fiber reinforced composite (PFRC) actuators subjected to thermal and axial compressed loads is presented. Based on the Donnell assumptions, the material properties of the FGM layer vary smoothly through the laminated cylindrical shell thickness according to a power law distribution of the volume fraction of constituent materials. In the present study, a numerical procedure for the laminated cylindrical shell is used based on the Ritz energy method and the nonlinear strain-displacement relations. Some useful discussion and numerical examples are presented to show various effects of temperature field, volume fraction and geometric parameters on the buckling and post-buckling behaviors of the laminated cylindrical shell with PFRC.

Crown Copyright © 2011 Published by Elsevier Masson SAS. All rights reserved.

---

## 1. Introduction

In the recent years, a great deal of research on the laminated composite shell comprised of two different materials has attracted much attention in many structural members and used in a wide variety of industries for high performance demands. A new class of materials known as "functionally graded materials" (Koizumi, 1993), are made of two or more materials varied continuously along a certain dimension. FGMs are now developed for general use as structural components in extremely high temperature environments. Another recent advance in material and structural engineering is in the field of smart structures, which incorporates adaptive materials. Therefore, the piezoelectric layers embedded on structures are well suited for uses as distributed sensors and actuators.

Early analytical studies were focused on the vibration control of such shell structures (Liew et al., 2002, 2004; Ng et al., 2002; Chen et al., 1999). Based on an approximate theory, Mirsky (1964) studied vibration of an orthotropic thick cylindrical shell in which the effect of transverse normal stress was retained. Sheng and Wang (2009) studied on dynamic behavior of FGM cylindrical shells with PZT layer for the application and the design of smart sensory structures.

Zhong and Shang (2003) and Hu et al. (2005) presented, respectively, three-dimensional exact analysis of piezoelectric plate and anti-plane shear crack in a functionally gradient piezoelectric layer. FGM piezoelectric structures and laminated elastic structures had attracted considerable attention of a few researchers Dai et al. (2007, 2010). Woo et al. (2003, 2005) presented Fourier series solutions for the thermo-mechanical post-buckling of thin and moderately thick FGM plates and shallow shells, from which the results for an initially heated cylindrical shell were obtained as a limiting case. Recently, with the rapidly increasing demands for heat-resisting, energy-absorbing, light-weight structures, more and more studies focused on buckling behaviors of the FGM cylindrical shell. Linear thermal buckling behaviors of the FGM cylindrical shell were investigated in literatures (Shahsiah and Eslami, 2003; Wu et al., 2005; Kadoli and Ganesan, 2006), in which temperature fields were assumed to be uniform or gradient through the shell thickness. Shen (2004, 2007) presented thermal post-buckling analysis for an FGM cylindrical shell under uniform temperature field and heat conduction shell theory based on classical shell theory and higher order shear deformation shell theory, respectively. Moreover, Zhao et al. (2007) and Zhao and Liew (2009, 2010) used the element-free kp-Ritz method for analysis of the thermal and mechanical buckling of functionally graded cylindrical shell structures. Piezoelectric composite materials have emerged as the new class of smart materials, and a new piezoelectric fiber reinforced composite (PFRC) was developed by Mallik and Ray (2003). Shen (2002, 2009) and Shen and Noda (2007) adopted

---

* Corresponding author. State Key Laboratory of Advanced Design and Manufacturing for Vehicle Body, Hunan University, Changsha 410082, China. Tel./fax: +86 73188822330.
E-mail address: hldai520@sina.com (H.-L. Dai).

0997-7538/$ - see front matter Crown Copyright © 2011 Published by Elsevier Masson SAS. All rights reserved.
doi:10.1016/j.euromechsol.2011.05.009

### Nomenclature

|  |  |  |  |
|-----|-----|-----|-----|
| $u, v, w$ | displacements along $x, y, z$ [m] | $T_o, T_i$ | the outermost and innermost temperature of the cylindrical shell [K] |
| $H, h$ | thickness of the cylindrical shell, thickness of the FGM layer [m] | $\sigma_i(i = x, y, z)$ | components of stress [$N/m^2$] |
| $R, L$ | mean radius, length of the laminated cylindrical shell [m] | $\epsilon_i(i = x,y), \gamma_{xy}$ | components of strain |
| $P_c, P_m$ | ceramic and metal material properties of FGM shell | $E_x, E_y, E_z$ | components of electric potential [W/A] |
| $V_c, V_m$ | ceramic, metal volume fractions of the FGM layer | $\Psi(z)$ | electric potential [W] |
| $k$ | volume fraction index | $V_p$ | the control voltage [V] |
| $E_F$ | Young's modulus of the FGM layer [GPa] | $A_{ij}, B_{ij}, D_{ij}$ | The coefficients of the membrane, coupling and flexural stiffness |
| $\kappa_F$ | thermal conductivity of the FGM layer [W/mK] | $N_i, M_i$ | the force [N] and force moment [N m]components caused by the deformation |
| $\alpha_F$ | thermal expansion coefficient of the FGM layer [Pa/K] | $N_i^T, M_i^T$ | the force [N m] and force moment [N m]components caused by thermal effects |
| $\mu_F$ | Poisson's ration of the FGM layer | $\overline{N}_i, \overline{M}_i$ | stress resultants [N] and force moments [N m] |
| $V^f, V^m$ | fiber, matrix volume fractions of the PFRC layer | $N_i^F, N_i^P$ | the force components of the FGM layer and the PFRC layer [N] |
| $\alpha_{ii}(i=1,2,3)$ | thermal expansion coefficient the Piezoelectric material [Pa/K] | $M_i^F, M_i^P$ | the force moment components of the FGM layer and the PFRC layer [N m] |
| $\kappa_P$ | thermal conductivity of the Piezoelectric material [W/mK] | $\varphi(x,y)$ | Airy's stress function |
| $e_{3i}(i=1,2,3)$ | piezoelectric constants [$C/m^2$] | $\overline{U}, \overline{U}_b, \overline{U}_m$ | the strain energy of stress, force and force moment [J] |
| $C_{ij}(i=1,2;\ j=1,2,3)$ | elastic constant of piezoelectric material [GPa] | $\overline{W}$ | the work done by the external forces [J] |
| $T, \Delta T$ | temperature distribution and temperature rise [K] | $\overline{\Pi}$ | the total potential energy of the system [J] |
|  |  | $P_x, P_{cr}$ | the axial compression stress and critical buckling load [N] |
|  |  | $\overline{\Delta}_x$ | the average end-shortening ratio |

a boundary layer theory for the shell buckling and found that the control voltage had a very small effect on the buckling and post-buckling behaviors. All these research in isotropic structures are effective references for further research in FGM structures. However, we need to know whether the control voltage has a significant effect on the buckling and post-buckling behaviors of a laminated cylindrical shell of the FGM with PFRC.

In the present paper, considering that the temperature is assumed to be a uniform distribution over the shell surface and varied in the thickness direction and that the electric field only has non-zero valued component $E_z$. The buckling and post-buckling problems of the axially compressed laminated cylindrical shell of FGM with PFRC actuators are investigated by using the Ritz energy method and the nonlinear strain-displacement relations of large deformation. The Donnell assumptions are applied by Yamaki (1984).

## 2. Formulation of the problem

Consider a hybrid laminated FGM cylindrical shell with mean radius of $R$, the length $L$ and total thickness $H$ as shown in Fig. 1. The outer and inner layers are PFRC bonded to surfaces of the FGM shell. The laminated cylindrical shell is compressed by an in-plane load $P_x = -\sigma_{0x}H$ with thermal and electric loads. The Cartesian coordinate system $(x,y,z)$ is set on the mid-plane $(z=0)$, where $x$ and $y$ denotes the axial and circumferential directions of the middle surface of the laminated cylindrical shell.

### 2.1. Material properties of FGM

The thickness of the middle FGM layer is $h$, the material properties of FGM's constituents $P_c$ and $P_m$ may be expressed as the following function with regard to temperature $T$ (in Kelvin).

$$
P_{c}(T) \text{ or } P_{m}(T)=P_{0}\left(P_{-1} T^{-1}+1+P_{1} T+P_{2} T^{2}+P_{3} T^{3}\right) \tag{1}
$$

where the subscripts "c" and "m" denote ceramic and metal, respectively, and $P_{-1}, P_{0}, P_{1}, P_{2}, P_{3}$ are temperature coefficients that are unique to the constituents.

FGM properties $P$ are related not only to the material properties of the constituents, but also to their volume fractions $V_c$ and $V_m$, therefore, one have

$$
P=P_{c} V_{c}+P_{m} V_{m}, \quad V_{c}+V_{m}=1 \tag{2}
$$

Assuming $V_c$ follows a simple power law distribution

$$
V_{c}=(0.5+z / h)^{k} \tag{3}
$$

where $k$ is volume fraction index $(0 \leq k \leq \infty)$, and $k$ represents the inhomogeneity of FGMs, and it degenerated into homogeneous isotropic material at $k=0$. Using Eq. (3), the properties of FGM are written as

$$
P(z)=\left(P_{c}-P_{m}\right)(0.5+z / h)^{k}+P_{m} \tag{4}
$$

Then, FGMs' properties vary smoothly from $P_{c}(z=h / 2)$ to $P_{m}(z=-h / 2)$ through the thickness according to $k$. From Eq. (4), the material properties are rewritten as

$$
E_{F}(z)=\left(E_{c}-E_{m}\right)(0.5+z / h)^{k}+E_{m} \tag{5a}
$$

$$
\alpha_{F}(z)=\left(\alpha_{c}-\alpha_{m}\right)(0.5+z / h)^{k}+\alpha_{m} \tag{5b}
$$

$$
\kappa_{F}(z)=\left(\kappa_{c}-\kappa_{m}\right)(0.5+z / h)^{k}+\kappa_{m} \tag{5c}
$$

where the effective Young's modulus $E_F$, thermal expansion coefficient $\alpha_F$ and thermal conductivity $\kappa_F$ are both temperature and

![](./images/811650848143704067_1.jpg)

Fig. 1. A laminated cylindrical shell of FGM with PFRC layers.

position dependent, and the Poisson's ratio $\mu_F$ depends weakly on temperature change and is assumed to be a constant.

### 2.2. Material properties of PFRC

The same thickness of the internal and external PFRC layers of the laminated cylindrical shell is $(H-h)/2$. The PFRC layer is composed of piezoelectric fiber and matrix. In terms of this model, the elastic stiffness constants $C_{ij}(i,j=1,2,3,6)$ may be shown in Appendix A, and the thermal expansion coefficients may be written (Tan and Tong, 2002)

$$
\alpha_{11}=C_{11}\left[\frac{V^{f} \alpha_{11}^{f}}{C_{11}^{f}}+\frac{V^{m} \alpha_{11}^{m}}{C_{11}^{m}}\right] \tag{6a}
$$

$$
\alpha_{22}=V^{f} \alpha_{22}^{f}+V^{m} \alpha^{m}+\frac{C_{12} \alpha_{11}}{C_{11}}-\frac{V^{f} C_{12}^{f} \alpha_{11}^{f}}{C_{11}^{f}}-\frac{V^{m} C_{12}^{m} \alpha_{11}^{m}}{C_{11}^{m}} \tag{6b}
$$

where superscript $f$ and $m$ denote the piezoelectric fiber and matrix, respectively, $V^{f}$ and $V^{m}$ are the fiber and matrix volume fractions and are related by $V^{f}+V^{m}=1$, and the thermal conductivity may be expressed as

$$
\kappa_{p}=V^{f} \kappa^{f}+V^{m} \kappa^{m} \tag{7}
$$

Here, the piezoelectric modulus $e_{31}$ and $e_{32}$ may be expressed (Mallik and Ray, 2003; Shen, 2009)

$$
\begin{aligned}
e_{31}= & V^{f} e_{31}^{f}-\left(V^{m} V^{f} / g\right)\left\{\left(C_{13}^{f}-C_{13}^{m}\right)\left[\left(V^{m} C_{22}^{f}+V^{f} C_{22}^{m}\right) e_{33}^{f}\right.\right. \\
& \left.-\left(V^{m} C_{23}^{f}+V^{f} C_{23}^{m}\right) e_{31}^{f}\right]+\left(C_{12}^{f}-C_{12}^{m}\right) \\
& \left.\times\left[\left(V^{m} C_{33}^{f}+V^{f} C_{33}^{m}\right) e_{31}^{f}-\left(V^{m} C_{23}^{f}+V^{f} C_{23}^{m}\right) e_{33}^{f}\right]\right\} \quad(8 \mathrm{a})
\end{aligned}
$$

$$
\begin{aligned}
e_{32}= & V^{f} e_{32}^{f}+\left(V^{m} / g\right)\left\{C_{22}^{f}\left[\left(V^{m} C_{23}^{f}+V^{f} C_{23}^{m}\right) e_{33}^{f}\right.\right. \\
& \left.-\left(V^{m} C_{33}^{f}+V^{f} C_{323}^{m}\right) e_{32}^{f}\right]-C_{23}^{f}\left[\left(V^{m} C_{22}^{f}+V^{f} C_{22}^{m}\right) e_{33}^{f}\right. \\
& \left.\left.-\left(V^{m} C_{23}^{f}+V^{f} C_{23}^{m}\right) e_{32}^{f}\right]\right\} \quad(8 \mathrm{~b})
\end{aligned}
$$

where

$$
g=\left(V^{m} C_{22}^{f}+V^{f} C_{22}^{m}\right)\left(V^{m} C_{33}^{f}+V^{f} C_{33}^{m}\right)-\left(V^{m} C_{23}^{f}+V^{f} C_{23}^{m}\right)^{2} \tag{9}
$$

It is assumed that the material property of matrix $C_{i j}^{m}$ is a function of temperature, so that all effective material properties of PFRC are functions of temperature.

### 2.3. The effects of temperature fields

Laminated cylindrical shells are most commonly used in thermal environment, thereby, effects of thermal environment should be considered in practice engineering. Assume that the temperature variation occurs in the thickness direction only, and the temperature field solving the following one-dimensional steady conduction equation is given (Shen and Noda, 2007)

$$
-\frac{\mathrm{d}}{\mathrm{d} z}\left[\kappa(z) \frac{\mathrm{d} T}{\mathrm{~d} z}\right]=0 \tag{10}
$$

where

$$
\kappa(z)= \begin{cases}\kappa_{p} & \left(\frac{h}{2}<|z|<\frac{H}{2}\right) \\ \kappa_{F} & \left(-\frac{h}{2}<z<\frac{h}{2}\right)\end{cases} \tag{11a}
$$

$$
T= \begin{cases}T_{p 1}(z) & \left(-\frac{H}{2} \leq z \leq-\frac{h}{2}\right) \\ T_{F}(z) & \left(-\frac{h}{2} \leq z \leq \frac{h}{2}\right) \\ T_{p 2}(z) & \left(\frac{h}{2} \leq z \leq \frac{H}{2}\right)\end{cases} \tag{11b}
$$

Eq.(10) is solved by imposing the boundary conditions $T=T_{o}(z=-\frac{H}{2})$ and $T=T_{i}(z=\frac{H}{2})$, and the continuity conditions

$$
T_{p 1}\left(-\frac{h}{2}\right)=T_{F}\left(-\frac{h}{2}\right)=T_{m}, \quad T_{p 2}\left(\frac{h}{2}\right)=T_{F}\left(\frac{h}{2}\right)=T_{c} \quad(12 \mathrm{a})
$$

$$
\left.\kappa_{p} \frac{\mathrm{d} T_{p 1}(z)}{\mathrm{d} z}\right|_{z=-\frac{h}{2}}=\left.\kappa_{m} \frac{\mathrm{d} T_{F}(z)}{\mathrm{d} z}\right|_{z=-\frac{h}{2}} \tag{12b}
$$

$$
\left.\kappa_{p} \frac{\mathrm{d} T_{p 2}(z)}{\mathrm{d} z}\right|_{z=\frac{h}{2}}=\left.\kappa_{c} \frac{\mathrm{d} T_{F}(z)}{\mathrm{d} z}\right|_{z=\frac{h}{2}} \tag{12c}
$$

By means of the polynomial series, the solution of Eqs.(10)-(12) is

$$
T_{p 1}(z)=\frac{2}{H-h}\left[\frac{H}{2} T_{m}-\frac{h}{2} T_{o}+\left(T_{m}-T_{o}\right) z\right] \tag{13a}
$$

$$
T_{F}(z)=T_{m}+\left(T_{c}-T_{m}\right) \frac{\sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i}(z / h+0.5)^{i k+1} \frac{1}{i k+1}}{\sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} \frac{1}{i k+1}} \tag{13b}
$$

$$
T_{p 2}(z)=\frac{2}{H-h}\left[\frac{H}{2} T_{c}-\frac{h}{2} T_{i}+\left(T_{i}-T_{c}\right) z\right] \tag{13c}
$$

where $\kappa_{c m}=\kappa_{c}-\kappa_{m}$, and

$$
T_{c}=\frac{\frac{1}{h \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} \frac{1}{i k+1}}\left[\kappa_{m} T_{i}+\kappa_{c} \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} T_{o}\right]+\frac{2 \kappa_{p}}{H-h} T_{o}}{\frac{1}{h \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} \frac{1}{i k+1}}\left[\kappa_{m}+\kappa_{c} \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i}\right]+\frac{2}{H-h} \kappa_{p}} \tag{14a}
$$

$$
T_{m}=\frac{\frac{1}{h \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} \frac{1}{i k+1}}\left[\kappa_{m} T_{i}+\kappa_{c} \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} T_{o}\right]+\frac{2 \kappa_{p}}{H-h} T_{i}}{\frac{1}{h \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i} \frac{1}{i k+1}}\left[\kappa_{m}+\kappa_{c} \sum_{i=0}^{\infty}\left(-\frac{\kappa_{c m}}{\kappa_{m}}\right)^{i}\right]+\frac{2}{H-h} \kappa_{p}} \tag{14b}
$$

It is remarkable that material properties are coupled with thermal environment. The material properties and the temperature field affect each other. In general, this iteration converges rapidly. For the sake of simplifying calculation, Eqs. (13b), (14a) and (14b) with $(i=1 \sim 5)$ is used in the present analysis.

Link layer and layer boundary conditions may be expressed as

$$
z=-h / 2, \quad E_{F}=E_{m}\left(T_{m}\right), \quad \alpha_{F}=\alpha_{m}\left(T_{m}\right), \quad \kappa_{F}=\kappa_{m}\left(T_{m}\right) \tag{15a}
$$

$$z=h / 2, \quad E_{F}=E_{c}\left(T_{c}\right), \quad \alpha_{F}=\alpha_{c}\left(T_{c}\right), \quad \kappa_{F}=\kappa_{c}\left(T_{c}\right) \quad(15 \mathrm{~b})$$

### 2.4. Fundamental equations

The Donnell shell theory is applied to characterize the defor- mation of the laminated cylindrical shell. According to the shallow shell approximations, the strain components on the middle surface of the laminated cylindrical shell are expressed as

$$
\begin{aligned}
\epsilon_{x}^{0} & =u_{, x}+\frac{1}{2} w_{, x}^{2}, \quad \epsilon_{y}^{0}=v_{, y}-\frac{w}{R}+\frac{1}{2} w_{, y}^{2}, \quad \gamma_{x y}^{0} \\
& =u_{, y}+v_{, x}+w_{, x} w_{, y}
\end{aligned}
$$

where $u(x, y)$ and $w(x, y)$ are the displacements along $x$ and $z$ axes, respectively, and subscripts following a comma stand for partial differentiations.

The strain components can be written as following

$$
\epsilon_{x}=\epsilon_{x}^{0}-z w_{, x x}, \quad \epsilon_{y}=\epsilon_{y}^{0}-z w_{, y y}, \quad \gamma_{x y}=\gamma_{x y}^{0}-2 z w_{, x y} \quad(17)
$$

According to the Kirchhoff-Love hypotheses, stress resultants of the $z$ direction are neglected, i.e. $\sigma_{z}=\tau_{y z}=\tau_{x z}=0$. Assume that the shell is subjected to a temperature rise $\Delta T$. Considering thermal effects, the stress-strain relations are given as

$$
\sigma_{x}=G(z)\left\{\epsilon_{x}+\mu_{F} \epsilon_{y}-\left(1+\mu_{F}\right) \alpha_{F}(z) \Delta T\right\}
$$

$$
\sigma_{y}=G(z)\left\{\epsilon_{y}+\mu_{F} \epsilon_{x}-\left(1+\mu_{F}\right) \alpha_{F}(z) \Delta T\right\}
$$

$$
\sigma_{x y}=\frac{1}{2} G(z)\left(1-\mu_{F}\right) \gamma_{x y}
$$

where
$$
G(z)=E_{F}(z) /\left(1-\mu_{F}^{2}\right)
$$

According to the thin shell assumption, the inner force and moment are denoted as

$$
\left[N_{x}, N_{y}, N_{x y}\right]=\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\sigma_{x}, \sigma_{y}, \sigma_{x y}\right] \mathrm{d} z
$$

$$
\left[M_{x}, M_{y}, M_{x y}\right]=\int_{-\frac{h}{2}}^{\frac{h}{2}}\left[\sigma_{x}, \sigma_{y}, \sigma_{x y}\right] z \mathrm{~d} z
$$

The stress resultants of the FGM layer are given by

$$
\left\{\begin{array}{c}
N_{x}^{F} \\
N_{y}^{F} \\
N_{x y}^{F} \\
M_{x}^{F} \\
M_{y}^{F} \\
M_{x y}^{F}
\end{array}\right\}=\left[\begin{array}{cccccc}
A_{11} & A_{12} & 0 & B_{11} & B_{12} & 0 \\
A_{21} & A_{22} & 0 & B_{21} & B_{22} & 0 \\
0 & 0 & A_{66} & 0 & 0 & B_{66} \\
B_{11} & B_{12} & 0 & D_{11} & D_{12} & 0 \\
B_{21} & B_{22} & 0 & D_{21} & D_{22} & 0 \\
0 & 0 & B_{66} & 0 & 0 & D_{66}
\end{array}\right]\left\{\begin{array}{c}
\epsilon_{x}^{0} \\
\epsilon_{y}^{0} \\
\gamma_{x y}^{0} \\
-w_{, x x} \\
-w_{, y y} \\
-w_{, x y}
\end{array}\right\}-\left\{\begin{array}{c}
N_{x}^{F T} \\
N_{y}^{F T} \\
N_{x y}^{F T} \\
M_{x}^{F T} \\
M_{y}^{F T} \\
M_{x y}^{F T}
\end{array}\right\}
$$

where

$$
\left(A_{i j}, B_{i j}, D_{i j}\right)=\int_{-\frac{h}{2}}^{\frac{h}{2}} Q_{i j}\left(1, z, z^{2}\right) \mathrm{d} z \quad(i, j=1,2,6)
$$

$$
\left(\begin{array}{cc}
N_{x}^{F T} & M_{x}^{F T} \\
N_{y}^{F T} & M_{y}^{F T} \\
N_{x y}^{F T} & M_{x y}^{F T}
\end{array}\right)=\int_{-\frac{h}{2}}^{\frac{h}{2}}\left(\begin{array}{c}
\left(Q_{11}+Q_{12}\right) \alpha_{F}(z) \\
\left(Q_{21}+Q_{22}\right) \alpha_{F}(z) \\
0
\end{array}\right)(1 \quad z) \Delta T \mathrm{~d} z \quad(21 \mathrm{~b})
$$

where $A_{i j}, B_{i j}$ and $D_{i j}$ represent the coefficients of membrane, coupling and flexural stiffness respectively. For the isotropic cylindrical shells, the coupled stiffness coefficients $B_{i j}$ should vanish. $N$ and $M^{T}$ are additional internal force and moment caused by temperature rise $\Delta T$. It is defined as following

$$
\begin{aligned}
Q_{i i} & =G(z), \quad Q_{12}=Q_{21}=\mu(z) G(z), \quad Q_{66} \\
& =[1-\mu(z)] G(z), \quad(i=1,2)
\end{aligned}
$$

According to the state of generalized plane stress of the thin shell assumption (Reddy, 2004), the constitutive equations of the PFRC layer can be expressed by the direct and the converse piezoelectric equations, respectively.

$$
\left\{\begin{array}{c}
\sigma_{x}^{P} \\
\sigma_{y}^{P} \\
\sigma_{x y}^{P}
\end{array}\right\}=\left[\begin{array}{ccc}
Q_{11}^{p} & Q_{12}^{p} & 0 \\
Q_{21}^{p} & Q_{22}^{p} & 0 \\
0 & 0 & Q_{66}^{p}
\end{array}\right]\left\{\begin{array}{c}
\epsilon_{x}-\alpha_{11 e} \Delta T \\
\epsilon_{y}-\alpha_{22 e} \Delta T \\
\gamma_{x y}
\end{array}\right\}-\left[\begin{array}{ccc}
0 & 0 & e_{31 e} \\
0 & 0 & e_{32 e} \\
0 & 0 & 0
\end{array}\right]\left\{\begin{array}{c}
E_{x} \\
E_{y} \\
E_{z}
\end{array}\right\}
$$

where $E_{x}, E_{y}$ and $E_{z}$ denote the electric field components, $Q_{i j}^{p}$ and $e_{i j e}$ are the elastic and piezoelectric constants, respectively, as (Sheng and Wang, 2009)

$$
e_{3 i e}=\frac{e_{3 i}}{C_{66}} \quad(i=1,2)
$$

$$
Q_{i j}^{p}=C_{i j}-\frac{C_{i 3} C_{i 3}}{C_{33}} \quad(i, j=1,2), \quad Q_{66}^{P}=C_{66}
$$

$$
\alpha_{i i e}=\alpha_{i i}-\frac{1}{C_{33}}\left(C_{31} \alpha_{11}+C_{32} \alpha_{22}\right), \quad(i=1,2)
$$

If the electric field applied on the shell is along the thickness direction of the shell, there exists only the electric field component $E_{z}$. Assume that the variation of the electric potential $\Psi$ (Shen, 2009) along the PFRC layer is linear, the aroused electric field in the PFRC layer $E_{z}$ is defined as $E_{z}=-\Psi_{, z}$, If the voltage applied to the actuator is in the thickness only, then

$$
E_{z}=V_{p} /\left(\frac{H-h}{2}\right)
$$

The stress resultants of the PFRC layer are computed by using Eq. (23) as follows

$$
\begin{aligned}
\left\{\begin{array}{c}
N_{x}^{P} \\
N_{y}^{P} \\
N_{x y}^{P} \\
M_{x}^{P} \\
M_{y}^{P} \\
M_{x y}^{P}
\end{array}\right\} & =\left[\begin{array}{cccccc}
A_{11}^{P} & A_{12}^{P} & 0 & B_{11}^{P} & B_{12}^{P} & 0 \\
A_{21}^{P} & A_{22}^{P} & 0 & B_{21}^{P} & B_{22}^{P} & 0 \\
0 & 0 & A_{66}^{P} & 0 & 0 & B_{66}^{P} \\
B_{11}^{P} & B_{12}^{P} & 0 & D_{11}^{P} & D_{12}^{P} & 0 \\
B_{21}^{P} & B_{22}^{P} & 0 & D_{21}^{P} & D_{22}^{P} & 0 \\
0 & 0 & B_{66}^{P} & 0 & 0 & D_{66}^{P}
\end{array}\right]\left\{\begin{array}{c}
\epsilon_{x}^{0} \\
\epsilon_{y}^{0} \\
\gamma_{x y}^{0} \\
-w_{, x x} \\
-w_{, y y} \\
-2 w_{, x y}
\end{array}\right\} \\
& -\left\{\begin{array}{c}
N_{x}^{P T} \\
N_{y}^{P T} \\
N_{x y}^{P T} \\
M_{x}^{P T} \\
M_{y}^{P T} \\
M_{x y}^{P T}
\end{array}\right\}+\left\{\begin{array}{c}
N_{x}^{E} \\
N_{y}^{E} \\
N_{x y}^{E} \\
M_{x}^{E} \\
M_{y}^{E} \\
M_{x y}^{E}
\end{array}\right\}
\end{aligned}
$$

where

$$
\left(A_{i j}^{P}, B_{i j}^{P}, D_{i j}^{P}\right)=\left(\int_{-\frac{H}{2}}^{-\frac{h}{2}} Q_{i j}^{P}+\int_{\frac{h}{2}}^{\frac{H}{2}} Q_{i j}^{P}\right)\left(1, z, z^{2}\right) \mathrm{d} z \quad(i, j=1,2,6)
\tag{27}
$$

and the thermal force and piezoelectric resultants of the PFRC layer are defined as

$$
\left(\begin{array}{cc}
N_{x}^{P T} & M_{x}^{P T} \\
N_{y}^{P T} & M_{y}^{P T} \\
N_{x y}^{P T} & M_{x y}^{P T}
\end{array}\right)=\left(\int_{-\frac{H}{2}}^{-\frac{h}{2}}+\int_{\frac{h}{2}}^{\frac{H}{2}}\right)\left(\begin{array}{c}
\left(Q_{11}^{P} \alpha_{11 e}+Q_{12}^{P} \alpha_{22 e}\right) \\
\left(Q_{21}^{P} \alpha_{11 e}+Q_{22}^{P} \alpha_{22 e}\right) \\
0
\end{array}\right)(1 \quad Z) \Delta T \mathrm{d} z
\tag{28}
$$

$$
\begin{aligned}
\left(\begin{array}{cc}
N_{x}^{E} & M_{x}^{E} \\
N_{y}^{E} & M_{y}^{E} \\
N_{x y}^{E} & M_{x y}^{E}
\end{array}\right)= & \left(\begin{array}{c}
2\left[\int_{-\frac{H}{2}}^{-\frac{h}{2}} e_{31 e} / \frac{H-h}{2}+\int_{\frac{h}{2}}^{\frac{H}{2}} e_{31 e} / \frac{H-h}{2}\right] \\
2\left[\int_{-\frac{H}{2}}^{-\frac{h}{2}} e_{32 e} / \frac{H-h}{2}+\int_{\frac{h}{2}}^{\frac{H}{2}} e_{32 e} / \frac{H-h}{2}\right] \\
0
\end{array}\right) \\
& \times(1 \quad z) V_{P} \mathrm{d} z
\end{aligned}
\tag{29}
$$

Then, stress resultants of the laminated cylindrical shell can be denoted as

$$
\bar{N}_{i}=N_{i}^{F}+N_{i}^{P}, \quad \bar{M}_{i}=M_{i}^{F}+M_{i}^{P}
\tag{30}
$$

where stress resultants $\bar{N}_{i}$ and $\bar{M}_{i}$ are decomposed into two parts as following, one is that related to the PFRC layer, and the other is related to the FGM shell.

Substituting Eqs. (20) and (26) into Eq.(30), stress resultants are

$$
\left\{\begin{array}{c}
\bar{N}_{x} \\
\bar{N}_{y} \\
\bar{N}_{x y} \\
\bar{M}_{x} \\
\bar{M}_{y} \\
\bar{M}_{x y}
\end{array}\right\}=\left[\begin{array}{cccccc}
A_{11}+A_{11}^{P} & A_{12}+A_{12}^{P} & 0 & B_{11}+B_{11}^{P} & B_{12}+B_{12}^{P} & 0 \\
A_{21}+A_{21}^{P} & A_{22}+A_{22}^{P} & 0 & B_{21}+B_{21}^{P} & B_{22}+B_{22}^{P} & 0 \\
0 & 0 & A_{66}+A_{66}^{P} & 0 & 0 & B_{66}+B_{66}^{P} \\
B_{11}+B_{11}^{P} & B_{12}+B_{12}^{P} & 0 & D_{11}+D_{11}^{P} & D_{12}+D_{12}^{P} & 0 \\
B_{21}+B_{21}^{P} & B_{22}+B_{22}^{P} & 0 & D_{21}+D_{21}^{P} & D_{22}+D_{22}^{P} & 0 \\
0 & 0 & B_{66}+B_{66}^{P} & 0 & 0 & D_{66}+D_{66}^{P}
\end{array}\right]\left\{\begin{array}{c}
\epsilon_{x}^{0} \\
\epsilon_{y}^{0} \\
\gamma_{x y}^{0} \\
\kappa_{x} \\
\kappa_{y} \\
\kappa_{x y}
\end{array}\right\}-\left\{\begin{array}{c}
N_{x}^{T}+N_{x}^{P T} \\
N_{y}^{T}+N_{y}^{P T} \\
N_{x y}^{T}+N_{x y}^{P T} \\
M_{x}^{T}+M_{x}^{P T} \\
M_{y}^{T}+M_{y}^{P T} \\
M_{x y}^{T}+M_{x y}^{P T}
\end{array}\right\}+\left\{\begin{array}{c}
N_{x}^{E} \\
N_{y}^{E} \\
N_{x y}^{E} \\
M_{x}^{E} \\
M_{y}^{E} \\
M_{x y}^{E}
\end{array}\right\}
\tag{31}
$$

where

$$
\left(\bar{A}_{i j}, \bar{B}_{i j}, \bar{D}_{i j}\right)=\left(A_{i j}+A_{i j}^{P}, B_{i j}+B_{i j}^{P}, D_{i j}+D_{i j}^{P}\right), \quad(i, j=1,2,6)
\tag{32a}
$$

$$
\bar{\phi}_{1}=N_{i}^{E}-N_{i}^{T}-N_{i}^{P T}, \quad \bar{\phi}_{2}=M_{i}^{E}-M_{i}^{T}-M_{i}^{P T}, \quad(i=x, y)
\tag{32b}
$$

From Eq. (17), the compatible equation is obtained as

$$
\epsilon_{x, y y}^{0}+\epsilon_{y, x x}^{0}-\gamma_{x y, x y}^{0}=-\frac{1}{R} w_{, x x}-w_{, x x} w_{, y y}+w_{, x y}^{2}
\tag{33}
$$

Regarding the definition of membrane forces, by introducing Airy's stress function $\varphi(x, y)$ which satisfies

$$
\bar{N}_{x}=\varphi_{, y y}, \quad \bar{N}_{y}=\varphi_{, x x}, \quad \bar{N}_{x y}=-\varphi_{, x y}
\tag{34}
$$

Substituting Eqs. (34) into Eqs. (31) and (32a,b) can be expressed (Huang and Han, 2009)

$$
\epsilon_{x}^{0}=F_{0}\left[\bar{A}_{11} \varphi_{, y y}-\bar{A}_{12} \varphi_{, x x}+F_{1} w_{, x x}+F_{2} w_{, y y}-F_{3} \bar{\phi}_{1}\right]
\tag{35a}
$$

$$
\epsilon_{y}^{0}=F_{0}\left[\bar{A}_{11} \varphi_{, x x}-\bar{A}_{12} \varphi_{, y y}+F_{2} w_{, x x}+F_{1} w_{, y y}-F_{3} \bar{\phi}_{1}\right]
\tag{35b}
$$

$$
\gamma_{x y}^{0}=F_{4} w_{, x y}-F_{5} \varphi_{, x y}
\tag{35c}
$$

where

$$
\begin{aligned}
& F_{0}=1 /\left(\bar{A}_{11}^{2}-\bar{A}_{12}^{2}\right), \quad F_{1}=\bar{A}_{11} \bar{B}_{11}-\bar{A}_{12} \bar{B}_{12}, \\
& F_{2}=\bar{A}_{11} \bar{B}_{12}-\bar{B}_{11} \bar{A}_{12} \quad F_{3}=\bar{A}_{11}-\bar{A}_{12}, \quad F_{4}=2 \frac{\bar{B}_{66}}{\bar{A}_{66}}, \\
& F_{5}=\frac{1}{\bar{A}_{66}}
\end{aligned}
\tag{36}
$$

Substituting Eq. (35) into Eq. (33), yields

$$
\nabla^{4} \varphi+F_{6} \nabla^{4} w+F_{7}\left(\frac{1}{R} w_{, x x}-w_{, x y}^{2}+w_{, x x} w_{, y y}\right)=0
\tag{37}
$$

where $F_{6}=\frac{\left(\bar{A}_{11} \bar{B}_{12}-\bar{B}_{11} \bar{A}_{12}\right)}{\bar{A}_{11}}$ and $F_{7}=\frac{\bar{A}_{11}^{2}-\bar{A}_{12}^{2}}{\bar{A}_{11}}$.

The strain energy is given as

$$
\bar{U}=\frac{1}{2} \iiint_{V}\left(\bar{\sigma}_{x} \epsilon_{x}+\bar{\sigma}_{y} \epsilon_{y}+\bar{\tau}_{x y} \gamma_{x y}\right) \mathrm{d} V
\tag{38}
$$

Substituting Eq. (17) and Eq. (19)into Eq. (38), yields

$$
\bar{U}=\bar{U}_{b}+\bar{U}_{m}
\tag{39}
$$

where

$$
\bar{U}_{m}=\frac{1}{2} \iint_{F}\left[\bar{N}_{x} \epsilon_{x}^{0}+\bar{N}_{y} \epsilon_{y}^{0}+\bar{N}_{x y} \gamma_{x y}^{0}\right] \mathrm{d} x \mathrm{d} y
\tag{40a}
$$

$$
\bar{U}_{b}=-\frac{1}{2} \iint_{F}\left[\bar{M}_{x} w_{, x x}+\bar{M}_{y} w_{, y y}+2 \bar{M}_{x y} w_{, x y}\right] \mathrm{d} x \mathrm{d} y
\tag{40b}
$$

Substituting Eq. (31) into Eqs. (40a) and (40b), and utilizing Eqs. (17) and (35a,b,c), one has

$$
\begin{aligned}
\bar{U}= & \frac{1}{2} \iint_{F}\left[J_{1}\left(\varphi_{x x}^{2}+\varphi_{y y}^{2}\right)+J_{2} \varphi_{x x} \varphi_{y y}+J_{3}\left(w_{x x}^{2}+w_{y y}^{2}\right)+J_{4} w_{x x} w_{y y}\right. \\
& \left.+\left(J_{5} \bar{\phi}_{1}-\bar{\phi}_{2}\right)\left(w_{x x}+w_{y y}\right)+J_{6} \bar{\phi}_{1}\left(\varphi_{x x}+\varphi_{y y}\right)\right] \\
& \left.+J_{7} w_{x y}^{2}+J_{8} \varphi_{x y}^{2}\right] \mathrm{d} x \mathrm{d} y
\end{aligned}
\tag{41}
$$

where $J_{i}(i=1,7)$ are shown in Appendix B.

Assume that the laminated cylindrical shell is subjected to an average axial compression stress $p_{x}$. With the aid of Eq. (16), the work done by the external forces during buckling is
$$
\overline{W}=-\sigma_{0 x} H \iint_{F}\left(\epsilon_{x}^{0}-\frac{1}{2} w_{, x}^{2}\right) \mathrm{d} x \mathrm{~d} y
\tag{42}
$$

Then, the total potential energy of the system is
$$
\overline{\prod}=\bar{U}-\overline{W}
\tag{43}
$$

For the laminated cylindrical shell, the following circumferential closed condition should be fully satisfied
$$
\int_{0}^{2 \pi R} v_{, y} \mathrm{~d} x \mathrm{~d} y=0
\tag{44}
$$

Similarly, the average end-shortening ratio $\bar{\Delta}_{x}$ can be given as
$$
\bar{\Delta}_{x}=-\frac{1}{2 \pi R L} \iint_{F} u_{x} \mathrm{~d} x \mathrm{~d} y
\tag{45}
$$

### 3. Solution of the problem

Here, the deflection of the laminated cylindrical shell is assumed as
$$
w=f_{0}+f_{1} \sin \alpha x \sin \beta y+f_{2} \sin ^{2} \alpha x
\tag{46}
$$
where $\alpha=m \pi / L$ and $\beta=n / R$. $m$ and $n$ are the axial half-wave numbers along $x$-axis and the wave numbers along $y$-axis, respectively. $f_{0}, f_{1}$ and $f_{2}$ are unknown amplitudes which corresponding to the pre-buckling, linear buckling and nonlinear buckling characters of $w$, respectively.

Substitution of Eq. (46) into Eq. (37), yields
$$
\begin{aligned}
\nabla^{4} \varphi= & b_{01} \cos 2 \alpha x+b_{02} \cos 2 \beta y+b_{03} \sin \alpha x \sin \beta y \\
& +b_{04} \sin 3 \alpha x \sin \beta y
\end{aligned}
\tag{47}
$$
where
$$
\begin{aligned}
& b_{01}=8 F_{6} \alpha^{4} f_{2}-4 F_{7} \frac{\alpha^{2}}{R} f_{2}+\frac{1}{2} F_{7} \alpha^{2} \beta^{2} f_{1}^{2}, b_{02}=\frac{1}{2} F_{7} \alpha^{2} \beta^{2} f_{1}^{2} \\
& b_{03}=\left[-F_{6}\left(\alpha^{2}+\beta^{2}\right)^{2}+\frac{F_{7}}{R} \alpha^{2}\right] f_{1}-F_{7} \alpha^{2} \beta^{2} f_{1} f_{2}, b_{04}=F_{7} \alpha^{2} \beta^{2} f_{1} f_{2}
\end{aligned}
\tag{48}
$$

The homogeneous solution for $\varphi$ is assumed as
$$
\varphi=-\frac{\bar{N}_{x 0}}{2} y^{2}-\frac{\bar{N}_{y 0}}{2} x^{2}
\tag{49}
$$
where $\bar{N}_{y 0}$ and $\bar{N}_{x 0}$ represent the circumferential internal force and axial internal force, respectively, and the axial internal force is determined by the force of the boundary conditions
$$
\bar{N}_{x 0}=-\sigma_{0 x} H
\tag{50}
$$

Then, the general solution of the stress function is given as
$$
\begin{aligned}
\varphi= & b_{1} \cos 2 \alpha x+b_{2} \cos 2 \beta y+b_{3} \sin \alpha x \sin \beta y+b_{4} \sin 3 \alpha x \sin \beta y \\
& -\frac{\bar{N}_{x 0}}{2} y^{2}-\frac{\bar{N}_{y 0}}{2} x^{2}
\end{aligned}
\tag{51}
$$
where
$$
b_{1}=\frac{b_{01}}{16 \alpha^{4}}, \quad b_{2}=\frac{b_{02}}{16 \beta^{4}}, \quad b_{3}=\frac{b_{03}}{\left(\alpha^{2}+\beta^{2}\right)^{2}}, \quad b_{4}=\frac{b_{04}}{\left(9 \alpha^{2}+\beta^{2}\right)^{2}}
\tag{52}
$$

Combined with Eqs. (46), (35b) and (51), the close condition Eq. (44) becomes
$$
\bar{N}_{y 0}=\frac{1}{\bar{A}_{11}}\left[\frac{f_{0}+f_{2} / 2}{F_{0} R}-\frac{f_{1}^{2} \beta^{2}}{8 F_{0}}+\bar{A}_{12} \sigma_{0 x} H-F_{3} \bar{\phi}_{1}\right]
\tag{53}
$$

Using Eqs. (46) and (51), the strain energy in Eq. (41) and the external work in Eq. (42) is rewritten as following
$$
\begin{aligned}
\bar{U}= & \pi R l\left\{J _ { 1 } \left[\frac{1}{4} b_{3}^{2}\left(\alpha^{2}+\beta^{2}\right)^{2}+\frac{1}{4} b_{4}^{2}\left(9 \alpha^{2}+\beta^{2}\right)^{2}+8 b_{1}^{2} \alpha^{4}\right.\right. \\
& \left.+8 b_{2}^{2} \beta^{4}\right]+J_{2} H \sigma_{0 x} \bar{N}_{y 0}+J_{3}\left[\frac{f_{2}^{2}}{4}\left(\alpha^{2}+\beta^{2}\right)^{2}+2 f_{2}^{2} \alpha^{4}\right] \\
& \left.+J_{1}\left(H^{2} \sigma_{0 x}^{2}+\bar{N}_{y 0}^{2}\right)-J_{6} \bar{\phi}_{1}\left(H \sigma_{0 x}+\bar{N}_{y 0}\right)\right\}
\end{aligned}
\tag{54}
$$

$$
\begin{aligned}
\overline{W}= & \frac{1}{4} \pi R l \sigma_{0 x} H\left[8 F_{0}\left(\bar{A}_{11} H \sigma_{0 x}-\bar{A}_{12} N_{y 0}\right)+f_{1}^{2} \alpha^{2}+2 f_{2}^{2} \alpha^{2}\right. \\
& \left.+8 F_{0} F_{3} \bar{\phi}_{1}\right]
\end{aligned}
\tag{55}
$$

Substituting Eqs. (54) and (55) into Eq. (43), yields the total potential energy, to which the Ritz energy method is applied, one has
$$
\frac{\partial \overline{\prod}}{\partial f_{0}}=\frac{\pi R l}{\bar{A}_{11} F_{0} R H}\left[2 J_{1} \bar{N}_{y 0}-J_{6} \bar{\phi}_{1}+\left(J_{2}+2 F_{0} \bar{A}_{12}\right) \sigma_{0 x} H\right]=0
\tag{56}
$$

$$
\begin{aligned}
\frac{\partial \overline{\prod}}{\partial f_{1}}= & \pi R l\left\{\frac{J_{1} f_{1}}{2\left(\alpha^{2}+\beta^{2}\right)^{2}}\left[\frac{F_{7}}{R} \alpha^{2}-F_{6}\left(\alpha^{2}+\beta^{2}\right)^{2}-F_{7} \alpha^{2} \beta^{2} f_{2}\right]^{2}\right. \\
& +\frac{J_{1} f_{1} f_{2}^{2}}{2\left(9 \alpha^{2}+\beta^{2}\right)^{2}} F_{7}^{2} \alpha^{4} \beta^{4}+\left(8 F_{6} F_{7} \alpha^{2} \beta^{2}-\frac{4 F_{7}^{2} \beta^{2}}{R}\right) J_{1} f_{1} f_{2} \\
- & \frac{1}{2} f_{1} \alpha^{2} \sigma_{0 x} H+\frac{1}{2} J_{1} f_{1}^{3} F_{7}^{2} \alpha^{4} \beta^{2}+\frac{J_{3}}{2} f_{1}\left(\alpha^{2}+\beta^{2}\right)^{2} \\
- & \left.\frac{f_{1} \beta^{2}}{4 F_{0} \bar{A}_{11}}\left[2 \bar{N}_{y 0} J_{1}-J_{6} \bar{\phi}_{1}+\left(J_{2}+2 F_{0} \bar{A}_{12}\right) \sigma_{0 x} H\right]\right\}=0
\end{aligned}
\tag{57}
$$

$$
\begin{aligned}
\frac{\partial \overline{\prod}}{\partial f_{2}}= & \pi R l\left\{\frac{J_{1} F_{7} f_{1}^{2} \alpha^{2} \beta^{2}}{2\left(\alpha^{2}+\beta^{2}\right)^{2}}\left[-\frac{F_{7}}{R} \alpha^{2}+F_{6}\left(\alpha^{2}+\beta^{2}\right)^{2}+F_{7} \alpha^{2} \beta^{2} f_{2}\right]\right. \\
& +\frac{J_{1} f_{1}^{2} f_{2}}{2\left(9 \alpha^{2}+\beta^{2}\right)^{2}} F_{7}^{2} \alpha^{4} \beta^{4}+\frac{J_{1}}{16 \alpha^{4}}\left(8 F_{6} \alpha^{4}-\frac{4 F_{7} \alpha^{2}}{R}\right) \\
\times & \left(8 F_{6} \alpha^{4} f_{2}-\frac{4 F_{7} \alpha^{2}}{R} f_{2}+\frac{1}{2} F_{7} f_{1}^{2} \alpha^{2} \beta^{2}\right) \\
& -f_{2} \alpha^{2} \sigma_{0 x} H+4 J_{3} f_{3} \alpha^{4}-\frac{1}{4 F_{0} R}\left[2 \bar{N}_{y 0} J_{1}-J_{6} \bar{\phi}_{1}\right. \\
& \left.\left.+\left(J_{2}+2 F_{0} \bar{A}_{12}\right) \sigma_{0 x} H\right]\right\}=0
\end{aligned}
\tag{58}
$$
```

Comparing Eqs. (53) with (56), yields

$$
\bar{N}_{y 0}=\frac{J_{6}}{2 J_{1}} \bar{\phi}_{1} \tag{59}
$$

Combined with Eqs. (53), (56), (57) and (58), yields

$$
\begin{aligned}
\sigma_{0 x} H= & \frac{2}{\left[\zeta_{2}+\left(\zeta_{1}-\zeta_{4}\right) f_{2}\right] \alpha^{2}}\left[\zeta_{1}^{2} f_{2}^{3}+3 \zeta_{1} \zeta_{2} f_{2}^{2}+\left(\zeta_{2}^{2}+\zeta_{1} \zeta_{3}-\zeta_{4} \zeta_{5}\right) f_{2}\right. \\
& \left.+\zeta_{2} \zeta_{3}\right]
\end{aligned} \tag{60}
$$

where

$$
\begin{aligned}
& \zeta_{1}=J_{1}\left[\frac{F_{7}^{2} \alpha^{4} \beta^{4}}{\left(\alpha^{2}+\beta^{2}\right)^{2}}+\frac{F_{7}^{2} \alpha^{4} \beta^{4}}{\left(9 \alpha^{2}+\beta^{2}\right)^{2}}\right], \\
& \zeta_{2}=J_{1}\left[2 F_{6} F_{7} \alpha^{2} \beta^{2}-\frac{F_{7}^{2} \alpha^{4} \beta^{2}}{\left(R \alpha^{2}+\beta^{2}\right)^{2}}-\frac{F_{7}^{2} \beta^{2}}{8 R}\right], \\
& \zeta_{3}=J_{1}\left[\frac{F_{7} \alpha^{2}}{R\left(\alpha^{2}+\beta^{2}\right)}+F_{6}\left(\alpha^{2}+\beta^{2}\right)\right]^{2}+J_{3}\left(\alpha^{2}+\beta^{2}\right)^{2}, \\
& \zeta_{4}=-\frac{J_{1} F_{7}^{2}\left(\alpha^{4}+\beta^{4}\right)}{16}, \quad \zeta_{5}=8 J_{1}\left(F_{6} \alpha^{2}-F_{7} / 4 R\right)^{2}+8 J_{3} \alpha^{4} \quad(61)
\end{aligned}
$$

By omitting the nonlinear buckling shape in Eq. (60), when $f_2=0$, the linear buckling load is

$$
P_{x}=\sigma_{0 x} H=\frac{J_{1}\left[\frac{F_{7}}{R} \frac{\alpha^{2}}{\left(\alpha^{2}+\beta^{2}\right)^{2}}-F_{6}\right]^{2} \times\left(\alpha^{2}+\beta^{2}\right)^{2}+J_{3}\left(\alpha^{2}+\beta^{2}\right)^{2}}{\alpha^{2}} \tag{62}
$$

With aid of Eq. (60), substituting Eqs. (46) and (51) into Eq. (45), one obtains

$$
\begin{aligned}
\bar{\Delta}_{x}= & \frac{\alpha^{2}}{32} 3 f_{2}^{2}-\frac{4}{\zeta_{3}}\left(\zeta_{1}+\zeta_{4} f_{2}^{2}+\zeta_{5} f_{2}-\frac{1}{2} \alpha^{2} H \sigma_{0 x}\right)+F_{0} \bar{A}_{12} H \sigma_{0 x} \\
& +\frac{1}{2} F_{0}\left(\bar{A}_{11}-\bar{A}_{12}\right) \bar{\phi}_{1}
\end{aligned} \tag{63}
$$

## 4. Numerical results and discussion

The FGM layer of the laminated cylindrical shell is made from a mixture of ceramic material silicon nitride and metallic material stainless. The temperature coefficients $P_{0}, P_{-1}, P_{1}, P_{2}, P_{3}$ in Eq. (1) for the two constituents are listed in Table 1 (Reddy and Chin, 1998). Poisson's ration of the FGM layer of the laminated cylindrical shell $\mu_{F}$ is taken as0.28. PZT-5A is selected for the piezoelectric fiber and material properties of which are (Shen, 2009; Hussein and Heyliger, 1998):

$$
\begin{aligned}
C_{11}^{f} & =C_{22}^{f}=121 \mathrm{GPa}, \quad C_{33}^{f}=111 \mathrm{GPa}, \quad C_{12}^{f} \\
& =75.4 \mathrm{GPa}, \quad C_{13}^{f}=C_{23}^{f}=75.2 \mathrm{GPa}, \quad C_{44}^{f}=C_{55}^{f} \\
& =21.1 \mathrm{GPa}, \quad C_{66}^{f}=22.6 \mathrm{GPa}, \quad e_{31}^{f}=e_{32}^{f} \\
& =-5.4 \mathrm{c} / \mathrm{m}^{2}, \quad e_{33}^{f}=15.8 \mathrm{c} / \mathrm{m}^{2} \quad \alpha_{11}^{f}=\alpha_{22}^{f} \\
& =0.9 \times 10^{-6} / \mathrm{K}, \quad \kappa^{f}=2.1 \mathrm{~W} / \mathrm{mK}, \quad C_{11}^{m}=C_{22}^{m}=C_{33}^{m} \\
& =(5.4015-0.000385 ~T) \mathrm{GPa}, \quad C_{12}^{m}=C_{13}^{m}=C_{23}^{m} \\
& =0.515 C_{11}^{m}, \quad C_{44}^{m}=C_{55}^{m}=C_{66}^{m}=0.242 C_{11}^{m}, \quad \alpha^{m} \\
& =45.0 \times 10^{-6} / \mathrm{K}, \quad \kappa^{m}=0.19 \mathrm{~W} / \mathrm{mK}.
\end{aligned}
$$

<table>
<caption>Table 1<br>Temperature-dependent coefficients for the material properties of ceramics and metals.</caption>
<thead>
<tr>
<th>Materials</th>
<th></th>
<th>$P_0$</th>
<th>$P_{-1}$</th>
<th>$P_1$</th>
<th>$P_2$</th>
<th>$P_3$</th>
</tr>
</thead>
<tbody>
<tr>
<td>Silicon nitride</td>
<td>$E_f$</td>
<td>$348.43 × 10^9$</td>
<td>0</td>
<td>$-3.070 × 10^{-4}$</td>
<td>$2.160 × 10^{-7}$</td>
<td>$-8.946 × 10^{-11}$</td>
</tr>
<tr>
<td></td>
<td>$\alpha_f$</td>
<td>$5.8723 × 10^{-6}$</td>
<td>0</td>
<td>$9.095 × 10^{-4}$</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>$\kappa_f$</td>
<td>13.732</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Stainless</td>
<td>$E_f$</td>
<td>$201.04 × 10^9$</td>
<td>0</td>
<td>$3.079 × 10^{-4}$</td>
<td>$-6.534 × 10^{-7}$</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>$\alpha_f$</td>
<td>$12.330 × 10^{-6}$</td>
<td>0</td>
<td>$8.086 × 10^{-4}$</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td></td>
<td>$\kappa_f$</td>
<td>15.379</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 2<br>Temperature-dependent coefficients for the material properties of ceramics and metals.</caption>
<thead>
<tr>
<th>$R/H$</th>
<th>$L/RH$</th>
<th>This paper</th>
<th>Huang and Han (2009)</th>
</tr>
</thead>
<tbody>
<tr>
<td>50</td>
<td>10</td>
<td>527.335(2,10)</td>
<td>528.652(2,10)</td>
</tr>
<tr>
<td></td>
<td>50</td>
<td>529.421(2,1)</td>
<td>531.159(2,1)</td>
</tr>
<tr>
<td></td>
<td>100</td>
<td>432.117(2,6)</td>
<td>433.234(2,6)</td>
</tr>
<tr>
<td></td>
<td>1000</td>
<td>5.223 (1,20)</td>
<td>5.245 (1,20)</td>
</tr>
<tr>
<td></td>
<td>5000</td>
<td>20.152(1,2)</td>
<td>20.919(1,2)</td>
</tr>
<tr>
<td>100</td>
<td>10</td>
<td>128.521(1,9)</td>
<td>130.326(1,9)</td>
</tr>
<tr>
<td></td>
<td>50</td>
<td>87.256(1,9)</td>
<td>87.908(1,9)</td>
</tr>
<tr>
<td></td>
<td>100</td>
<td>79.457(1,5)</td>
<td>81.432(1,5)</td>
</tr>
<tr>
<td></td>
<td>1000</td>
<td>3.212(1,4)</td>
<td>3.203(1,4)</td>
</tr>
<tr>
<td></td>
<td>5000</td>
<td>0.523(1,2)</td>
<td>0.523(1,2)</td>
</tr>
</tbody>
</table>

**Example 1.** In order to verify the present method for the purpose of the correctness, the laminated cylindrical shell is reduced to a single-layer cylindrical shell, and the geometric parameters of the cylindrical shell and the material properties are identical to those given in the literature (Huang and Han, 2009). In addition, the buckling loads for the simply supported, isotropic cylindrical shell under axial pressure is calculated and compared in Table 2, and it is clear that the present results agree well with the existing results.

**Example 2.** In this example, geometric parameters of the laminated cylindrical shell are, respectively, taken as $L=3$ m, $R=0.5$ m, $H=0.005$ m, $h=0.003$ m and $V^f=0.6$. Here, the corresponding buckling mode is taken as $(m,n)=(2,3)$. The temperature boundary condition to take the following two cases

- **Case I:** $T_i=T_o=300$ K
- **Case II:** $T_i=600$ K, $T_o=300$ K

Table 3 gives buckling loads $P_{cr}$ for perfect, the laminated cylindrical shell with different values of volume fraction index $k$

<table>
<caption>Table 3
Temperature-dependent coefficients for the material properties of ceramics and metals.</caption>
<thead>
<tr>
<th>Temperature</th>
<th>$V_f$</th>
<th>$k = 0$</th>
<th>$k = 2$</th>
<th>$k = 3$</th>
<th>$k = 4$</th>
</tr>
</thead>
<tbody>
<tr>
<td>$T_o = 300$ K</td>
<td>1.0</td>
<td>12.4116</td>
<td>9.2621</td>
<td>8.8681</td>
<td>8.6321</td>
</tr>
<tr>
<td>$T_i = 300$ K</td>
<td>0.9</td>
<td>12.2933</td>
<td>9.1433</td>
<td>8.7493</td>
<td>8.5211</td>
</tr>
<tr>
<td></td>
<td>0.8</td>
<td>12.1749</td>
<td>9.0244</td>
<td>8.6305</td>
<td>8.4239</td>
</tr>
<tr>
<td></td>
<td>0.6</td>
<td>11.9382</td>
<td>8.7867</td>
<td>8.3928</td>
<td>7.6814</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>11.8196</td>
<td>8.6677</td>
<td>8.2740</td>
<td>7.3718</td>
</tr>
<tr>
<td></td>
<td>0.4</td>
<td>11.7012</td>
<td>8.0084</td>
<td>7.6073</td>
<td>7.3718</td>
</tr>
<tr>
<td></td>
<td>0.2</td>
<td>11.4641</td>
<td>8.0084</td>
<td>7.6073</td>
<td>7.3718</td>
</tr>
<tr>
<td>$T_o = 300$ K</td>
<td>1.0</td>
<td>12.4116</td>
<td>9.2621</td>
<td>8.8681</td>
<td>8.6321</td>
</tr>
<tr>
<td>$T_i = 600$ K</td>
<td>0.9</td>
<td>11.8705</td>
<td>9.1597</td>
<td>8.7899</td>
<td>8.5499</td>
</tr>
<tr>
<td></td>
<td>0.8</td>
<td>12.0691</td>
<td>9.0052</td>
<td>8.6605</td>
<td>8.4239</td>
</tr>
<tr>
<td></td>
<td>0.6</td>
<td>11.9520</td>
<td>8.8093</td>
<td>8.4157</td>
<td>8.2011</td>
</tr>
<tr>
<td></td>
<td>0.5</td>
<td>11.8393</td>
<td>8.6868</td>
<td>8.2933</td>
<td>8.0256</td>
</tr>
<tr>
<td></td>
<td>0.4</td>
<td>11.7358</td>
<td>8.5643</td>
<td>8.0709</td>
<td>7.8041</td>
</tr>
<tr>
<td></td>
<td>0.2</td>
<td>11.4728</td>
<td>8.2763</td>
<td>7.8967</td>
<td>7.6214</td>
</tr>
</tbody>
</table>

subject to axial pressure in two type thermal boundary conditions.
The monolithic piezoelectric layer ($V^f = 1.0$), as previously used in Shen (2005, 2007, 2009), is the maximum value of the effective piezoelectric coefficient of the PFRC in this paper, and has the same value of the buckling loads under case I and case II. For the present

![](./images/811650848143704067_2.jpg)

Fig. 2. Variation of the critical buckling loads in the radial direction, where (a) $Ti = 300$ K and (b) $Ti = 600$ K.

![](./images/811650848143704067_3.jpg)

Fig. 3. Effects of temperature change on buckling behavior of the laminated cylindrical shell.

PZT-5A material, when the fiber volume fraction $V^f$ is equal to 0.4, 0.2 and become less, the buckling load is almost no change. It can be seen that a fully ceramic shell ($k = 0$) has the maximum buckling load. It can also be seen from Table 3 that the buckling loads decreases with increasing of the volume fraction index $k$ and temperature $T_i$.

Fig. 2(a) and (b), respectively, show the relation curves of the critical buckling loads versus radius with various volume fraction index $k$ under case I and case II. From Fig. 2, it is seen easily that values of the critical buckling load decreases with increasing of the radius of the laminated cylindrical shell, and the trend of variation becomes smaller as the increasing of the volume fraction index. It can be also seen from Fig. 2(a) that the volume fraction index $k = 4$ has the lowest buckling load.

Fig. 3 shows the effects of temperature rise on buckling behavior of the laminated cylindrical shell with various volume fraction indexes. It is seen easily from Fig. 3 that the temperature change has almost no effect on the critical buckling load.

![](./images/811650848143704067_4.jpg)

Fig. 4. Circumferential stress for the laminated cylindrical shell with volume fraction index.

![](./images/811650848143704067_5.jpg)

Fig. 5. Linear buckling behaviors of the laminated cylindrical shell with various electric loads.

Fig. 4 shows the circumferential stress for the laminated cylindrical shell with PFRC actuators of the volume fraction index under three electric loadings $V_{p}$ ($V_{p}$ is taken as 0, 100 V, 200 V). From Fig. 4, it can be found that the circumferential stress is very small, almost close to zero. This indicates that the circumferential stress should be zero when the axially compressed shell is free in radial displacement.

Example 3. In this example, it is presented the linear buckling behavior, and the linear buckling equilibrium path is defined by Eq. (46) without $f_{2}$. Geometric parameters of the laminated cylindrical shell are, respectively, taken as $L = 3$ m, $R = 0.5$ m, $H = 0.005$ m, $h = 0.003$ m. Here, the corresponding buckling mode is taken as $(m,n)=(2,3)$. The temperature boundary condition to take the following two cases:

Case I: $T_{i}=T_{o}=300$ K
Case II: $T_{i}=600$ K, $T_{o}=300$ K

![](./images/811650848143704067_6.jpg)

Fig. 6. Linear buckling behaviors of the laminated cylindrical shell with various volume fraction index.

![](./images/811650848143704067_7.jpg)

Fig. 7. Effects of volume fraction indexes on post-buckling of FGM shell with PFRC under cases I: load-shortening.

Fig. 5 shows the compressive linear buckling behavior versus deflection of the laminated cylindrical shell under two-type thermal boundary conditions and various electric loads. It is easily seen that the buckling load $P$ increases linearly as deflection increases. It can be seen from Fig. 5 that the buckling load decreases as the increasing of the electric load increases at the same average deflection. From Fig. 4, it can be also seen that the control voltage of this paper has a great effect on the linear buckling behavior, whereas Shen (2009) has a small effect on it.

Fig. 6 denotes effects of volume fraction indexes $k$ ($k$ is taken as 0.5, 2 and 4) on the linear buckling behavior versus deflection of the laminated cylindrical shell under the two thermal boundary conditions. It is obvious that the lower value of $k$ corresponds to the higher values of the buckling loads and higher linear buckling equilibrium path. The linear buckling loads decreases as the increasing of the temperature.

Example 4. In this example, it is presented that the post-buckling analysis of the laminated cylindrical shell. Geometric parameters of the laminated cylindrical shell are, respectively, taken as $L = 0.5$ m, $h = 0.003$ m, $H = 0.005$ m and $V^{f}=0.6$. Here, the temperature

![](./images/811650848143704067_8.jpg)

Fig. 8. Effects of volume fraction indexes on post-buckling of FGM shell with PFRC under case I: load-deflection.

![](./images/811650848143704067_9.jpg)

Fig. 9. Effects of volume fraction indexes on post-buckling of FGM shell with monolithic piezoelectric under case II: load-shortening.

boundary condition is taken as $T_{o}=T_{i}=300$ K. The temperature boundary condition to take the following two cases:

**Case I:** $T_{i}=T_{o}=300$ K
**Case II:** $T_{i}=600$ K, $T_{o}=300$ K

Figs. 7 and 8, respectively, show effects of volume fraction indexes $k$ ($k$ is taken as 0.5, 2 and 4) on post-buckling load-shortening and load-deflection curves for the FGM shell with PFRC layer under Case I. It can be found that the lowest of these curves depicts the post-buckling equilibrium path. It is obvious that a lower value of $k$ corresponds to higher values of the upper and lower critical loads and higher post-buckling equilibrium path. These show that a higher volume fraction of ceramic constituent material makes for increasing both the linear critical load and the load capacity after buckling. Also, it can be found that the post-buckling equilibrium path becomes much steeper.

Figs. 9 and 10, respectively, show effects of volume fraction indexes $k$ ($k$ is taken as 0.5, 2 and 4) on post-buckling load-shortening and load-deflection curves for the FGM shell with monolithic piezoelectric layer under Case II. Compared with Fig. 7, the upper and lower critical loads decrease as the temperature rise.

![](./images/811650848143704067_10.jpg)

Fig. 10. Effects of volume fraction indexes on post-buckling of FGM shell with monolithic piezoelectric under case II: load-deflection.

![](./images/811650848143704067_11.jpg)

Fig. 11. Comparisons of dimensional post-buckling behavior of FGM shell with PFRC and monolithic piezoelectric under case I: load-shortening.

Fig.11 shows comparison of dimensional post-buckling behavior of the FGM shell with PFRC and monolithic piezoelectric under case I. The buckling load as well as the post-buckling equilibrium path decrease greatly as the $R/H$ increases. It can be seen that the buckling upper and lower critical loads and post-buckling strength of the FGM with PFRC layer ($V^{f}=0.6$), is lower than that of the shell with monolithic piezoelectric layer ($V^{f}=1$).

### 5. Conclusions

In the present study, buckling and post-buckling analyses for an axially compressed laminated cylindrical shell of FGM with PFRC in thermal environments is presented. A numerical procedure for the hybrid laminated cylindrical shell (PFRC/FGM/PFRC) based on the Ritz energy method and the nonlinear strain-displacement relations are used, there are a few conclusions as follows

(1) For the present PZT-5A material, when the fiber volume fraction $V^{f}$ ranges from 0 to 0.4, the critical buckling load actually has almost no change. In contrast, the monolithic piezoelectric layer ($V^{f}=1.0$) is the maximum value of the effective piezoelectric coefficient of the PFRC in this paper.

(2) Numerical results show decreasing in the values of volume fraction index and temperature rise helps to increase the upper and lower critical loads as well as the carrying capacity after buckling.

(3) Numerical results reveal that the control voltage has a great effect on the buckling behavior of the laminated cylindrical shell, and show that the circumferential stress is very small, almost close to zero. This indicates that the circumferential stress should be zero when the axially compressed shell is free in radial displacement.

(4) Numerical results reveal that both the buckling load and the post-buckling equilibrium path are affected considerably by $R/H$, the buckling upper and lower critical loads and post-buckling strength of the FGM with PFRC layer, is lower than that of the shell with monolithic piezoelectric layer.

### Acknowledgements

The authors wish to thank reviewers for their valuable comments and the funded by the National Natural Science

Foundation of China (Grant No.11072077), State key Laboratory of Advanced Design and Manufacturing for Vehicle Body (Grant No.734215002), and the central colleges of basic scientific research and operational costs (funded by the Hunan University).

Appendix A

$$
C_{11}=\frac{C_{11}^{f} C_{11}^{m}}{V_{f} C_{11}^{f}+V_{m} C_{11}^{m}}, \quad C_{12}=C_{11}\left[\frac{V^{f} C_{12}^{f}}{C_{11}^{f}}+\frac{V^{m} C_{12}^{m}}{C_{11}^{m}}\right],
$$

$$
C_{22}=V^{f} C_{22}^{f}+V^{m} C_{22}^{m}+\frac{C_{12}^{2}}{C_{11}}-V^{f} \frac{\left(C_{12}^{f}\right)^{2}}{C_{11}^{f}}-V^{m} \frac{\left(C_{12}^{m}\right)^{2}}{C_{11}^{m}},
$$

$$
C_{13}=C_{11}\left[\frac{V^{f} C_{13}^{f}}{C_{11}^{f}}+\frac{V^{m} C_{13}^{m}}{C_{11}^{m}}\right],
$$

$$
C_{23}=V^{f} C_{23}^{f}+V^{m} C_{23}^{m}+\frac{C_{12} C_{13}}{C_{11}}-V^{f} \frac{C_{12}^{f} C_{13}^{f}}{C_{11}^{f}}-V^{m} \frac{C_{12}^{m} C_{13}^{m}}{C_{11}^{m}},
$$

$$
C_{33}=V^{f} C_{23}^{f}+V^{m} C_{33}^{m}+\frac{C_{13}^{2}}{C_{11}}-V^{f} \frac{\left(C_{13}^{f}\right)^{2}}{C_{11}^{f}}-V^{m} \frac{C_{13}^{m} C_{13}^{m}}{C_{11}^{m}},
$$

$$
C_{66}=\frac{C_{66}^{f} C_{66}^{m}}{V_{f} C_{66}^{f}+V_{m} C_{66}^{m}}.
$$

Appendix B

$$
J_{1}=\frac{\bar{A}_{11}}{\bar{A}_{11}^{2}-\bar{A}_{12}^{2}}, \quad J_{2}=\frac{2 \bar{A}_{12}}{\bar{A}_{12}^{2}-\bar{A}_{11}^{2}},
$$

$$
J_{3}=\frac{\bar{A}_{11}\left(\bar{B}_{11}^{2}+\bar{B}_{12}^{2}\right)-2 \bar{B}_{11} \bar{B}_{12} \bar{A}_{12}+\bar{D}_{11}\left(\bar{A}_{11}^{2}-\bar{A}_{12}^{2}\right)}{\bar{A}_{12}^{2}-\bar{A}_{11}^{2}},
$$

$$
J_{4}=2 \frac{\bar{A}_{12}\left(\bar{B}_{11}^{2}+\bar{B}_{12}^{2}\right)-2 \bar{B}_{11} \bar{B}_{12} \bar{A}_{11}+\bar{D}_{12}\left(\bar{A}_{11}^{2}-\bar{A}_{12}^{2}\right)}{\bar{A}_{11}^{2}-\bar{A}_{12}^{2}},
$$

$$
J_{5}=\frac{\bar{B}_{11}+\bar{B}_{12}}{\bar{A}_{11}+\bar{A}_{12}}, \quad J_{6}=\frac{1}{\bar{A}_{11}+\bar{A}_{12}}, \quad J_{7}=4 \frac{\bar{A}_{33} \bar{D}_{33}-\bar{B}_{33}^{2}}{\bar{A}_{33}},
$$

$$
J_{8}=\frac{1}{\bar{A}_{33}}.
$$

References

Chen, W.Q., Wang, X., Ding, H.J., 1999. Free vibration of fluid filled hollow sphere of a functionally graded material with spherical isotropy. Journal of the Acoustical Society of America 106, 2588-2594.

Dai, H.L., Fu, Y.M., Yang, J.H., 2007. Electromagnetoelastic behaviors of functionally graded piezoelectric solid cylinder and sphere. Acta Mechanica Sinica 23, 55-63.

Dai, H.L., Hong, L., Fu, Y.M., et al., 2010. Analytical solution for electro- magnetothermoelastic behaviors of a functionally graded piezoelectric hollow cylinder. Applied Mathematical Modeling 34, 343-357.

Hu, K.Q., Zhong, Z., Jin, B., 2005. Anti-plane shear crack in a functionally gradient piezoelectric layer bonded to dissimilar half spaces. International Journal of Mechanical Sciences 47, 82-93.

Huang, H.W., Han, Q., 2009. Nonlinear elastic buckling and post-buckling of axially compressed functionally graded cylindrical shells. International Journal of Mechanical Sciences 51 (7), 500-507.

Hussein, M., Heyliger, P., 1998. Three-dimensional vibrations of laminated piezo- electric cylinders. Journal of Engineering Mechanics 21, 568-593.

Kadoli, R., Ganesan, N., 2006. Buckling and free vibration analysis of functionally graded cylindrical shells subjected to a temperature-specified boundary condition. Journal of Sound and Vibration 289, 450-480.

Koizumi, M., 1993. The concept of FGM. Ceramic Transation 34, 3-10.

Liew, K.M., He, X.Q., Ng, T.Y., et al., 2002. Active control of FGM shells subjected to a temperature gradient via piezoelectric sensor/actuator patches. International Journal for Numerical Methods in Engineering 55, 653-668.

Liew, K.M., He, X.Q., Kitipornchai, S., 2004. Finite element method for the feedback control of FGM shells in the frequency domain via piezoelectric sensors and actuators. Computer Methods in Applied Mechanics and Engineering 193, 257-273.

Mallik, N., Ray, M.C., 2003. Effective coefficients of piezoelectric fiber-reinforced composites. AIAA Journal 41, 704-710.

Mirsky, I., 1964. Vibrations of orthotropic, thick, cylindrical shells. Journal of Acoustics Society of America 36, 41-51.

Ng, T.Y., He, X.Q., Liew, K.M., 2002. Finite element modeling of active control of functionally graded shells in frequency domain via piezoelectric sensors and actuators. Computational Mechanics 28, 1-9.

Reddy, J.N., 2004. Mechanics of Laminated Composite Plates and Shells. Seconded CRC Press, New York.

Reddy, J.N., Chin, C.D., 1998. Thermomechanical analysis of functionally graded cylinders and plates. Journal of Thermal Stresses 23, 593-629.

Shahsiah, R., Eslami, M.R., 2003. Thermal buckling of functionally graded cylindrical shell. Journal of Thermal Stresses 26, 277-294.

Shen, H.S., 2002. Postbuckling analysis of axially-loaded functionally graded cylindrical shells in thermal environments. Composites Science and Technology 62, 977-987.

Shen, H.S., 2004. Thermal post-buckling behavior of functionally graded cylindrical shells with temperature-dependent properties. International Journal of Solids and Structures 41, 1961-1974.

Shen, H.S., 2005. Postbuckling of axially loaded FGM hybrid cylindrical shells in thermal environments. Composites Science and Technology 65, 1675-1690.

Shen, H.S., 2007. Thermal post-buckling of shear deformable FGM cylindrical shells with temperature-dependent properties. Mechanics of Advanced Materials and Structures 14, 439-452.

Shen, H.S., 2009. A comparison of post-buckling behavior for FGM cylindrical shells with piezoelectric fiber reinforced composite actuators. Journal of Engineering Materials and Technology 131, 1-11.

Shen, H.S., Noda, N., 2007. Postbuckling of pressure-loaded FGM hybrid cylindrical shells in thermal environments. Composite Structures 77, 546-560.

Sheng, G.C., Wang, X., 2009. Studies on dynamic behavior of functionally graded cylindrical shells with PZT layers under moving loads. Journal of Sound and Vibration 323, 772-789.

Tan, P., Tong, L.Y., 2002. Modeling for the electro-magneto-thermo-elastic proper- ties of piezoelectric-magnetic fiber reinforced composites. Composites Part A: Applied Science and Manufacturing 33, 631-645.

Woo, J., Meguid, S.A., Liew, K.M., 2003. Thermomechanical post-buckling analysis of functionally graded plates and shallow shells. Acta Mechanica 165, 99-115.

Woo, J., Meguid, S.A., Stranart, J.C., et al., 2005. Thermomechanical post-buckling analysis of moderately thick functionally graded plates and shallow shells. International Journal of Mechanics Science 47, 1147-1171.

Wu, L.H., Jiang, Z.Q., Liu, J., 2005. Thermoelastic stability of functionally graded cylindrical shells. Composite Structures 70, 60-68.

Yamaki, N., 1984. Elastic Stability of Circular Cylindrical Shells. North-Holland Press, New York. 218-262.

Zhao, X., Liew, K.M., 2009. Geometrically nonlinear analysis of functionally graded shells. International Journal of Mechanical Sciences 51, 131-144.

Zhao, X., Liew, K.M., 2010. A mesh-free method for analysis of the thermal and mechanical buckling of functionally graded cylindrical shell panels. Computa- tional Mechanics 45, 297-310.

Zhao, X., Yang, Y., Liew, K.M., 2007. Geometrically nonlinear analysis of cylindrical shells using the element-free kp-Ritz method. Engineering Analysis with Boundary Elements 31, 783-792.

Zhong, Z., Shang, E.T., 2003. Three-dimensional exact analysis of a simply supported functionally graded piezoelectric plate. International Journal of Solids and Structures 40, 5335-5352.