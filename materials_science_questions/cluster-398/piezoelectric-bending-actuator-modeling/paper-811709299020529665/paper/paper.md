# Modeling and Testing of the Static Deflections of Circular Piezoelectric Unimorph Actuators

D. H. WANG $^{1,2, *}$ AND J. HUO $^{1,2}$

$^{1}$ Key Laboratory of Optoelectronic Technology and Systems of the Ministry of Education of China, Chongqing University, Chongqing 400044, China

$^{2}$ Precision and Intelligence Laboratory, Department of Optoelectronic Engineering, Chongqing University, Chongqing 400044, China

**ABSTRACT:** In this article, based on the classical laminated plate theory, a new static deflection model for CPUAs subjected to voltage is established and the bonding layer is taken into account as an individual layer. According to the established analytical model, the influences of the structural parameters and material properties of the CPUA on the transverse deflection are numerically simulated and the static and dynamic characteristics of the CPUA are experimentally tested. The research results show that the predicted static deflections of the CPUA by the established deflection model in this article agree well with the measured results, the established static deflection model considering the bonding layer is more accurate than the existing model neglecting the bonding layer, and the maximum relative error is reduced by $8.45\%$. The static deflections of the CPUA are apparently affected by the structural parameters and the material properties, which indicate that the performance of the CPUA can be optimized by the structural parameters and material properties. Because the hysteresis of the piezoelectric material is not considered when establishing the static deflection model, the apparent error exists when utilizing the static deflection model to predict the dynamic characteristics of the CPUA.

**Key Words:** piezoelectric actuator, circular piezoelectric unimorph, piezoelectric laminate, modeling, bonding layer.

## INTRODUCTION

CIRCULAR piezoelectric unimorph actuator (CPUA) consists of a polarized piezoelectric layer and a substrate layer, which are bonded to each other using the conducting epoxy as the bonding layer, while a circular piezoelectric bimorph actuator (CPBA) is made of two polarized piezoelectric layers and a substrate layer, and the polarized piezoelectric layers are axisymmetrically bonded to both sides of the substrate layer. Due to the simple structure, small size, light weight, and large deformation, the CPUAs and CPBAs, as two typical kinds of piezoelectric actuators based on the inverse piezoelectric effect of piezoelectric materials, have been widely used to develop electroacoustic transducers (Dorojkine et al., 1997; Zhang and Wang, 2002; Luan et al., 2004) and micro-fluidic transport (Li et al., 2004; Woias, 2005).

In order to predict and optimize the behavior of CPUAs, the key problem lies in establishing the analytical model for CPUAs (Morris and Forster, 2000; Papila et al., 2008). Dobrucki and Pruchnicki (1997) studied an analytical model for a piezoelectric axisymmetric bimorph using the finite element method (FEM) and a free boundary was assumed in their work. Based on the 3D elastic theory of the piezoelectric materials, Ding et al. (1999) studied the free vibration problem of a piezoelectric axisymmetric laminated circular plate for the rigid slipping support and the flexible simple support boundary conditions without considering the effect of the piezoelectric effect. Heyliger and Ramirez (2000) investigated the free vibration characteristics of the laminated composite piezoelectric plate. In their study, the influence of the electrostatic potential was considered while the non-piezoelectric materials were neglected. Using the FEM, Morris and Forster (2000) optimized the static deflection of the CPUA for fixed and pinned-edge conditions according to the given plate dimensions, the actuator-to-plate stiffness ratio, the actuator-to-plate radius ratio, and the bonding layer thickness. However, the deflection model derived by means of the FEM was not well suitable for the engineering design. Based on linear strain assumptions and considering the effect of the bonding layer, Li and Chen (2003) presented an analytical model for a partially covered circular piezoelectric actuator for the clamped support

*Author to whom correspondence should be addressed.
E-mail: dhwang@cqu.edu.cn
Figures 4–16 appear in color online: http://jim.sagepub.com

---

JOURNAL OF INTELLIGENT MATERIAL SYSTEMS AND STRUCTURES, Vol. 21—November 2010

1045-389X/10/16 1603-14 $10.00/0
DOI: 10.1177/1045389X10385485
© The Author(s), 2010. Reprints and permissions:
http://www.sagepub.co.uk/journalsPermissions.nav

condition and the bonding layer was considered when establishing the model. Their analytical results by the established model, however, did not agree well with their experimental results. Based on the classical laminated plate theory (CLPT) and neglecting the bonding layer, Mo et al. (2006) derived the transverse deflection model for a circular piezoelectric axisymmetric unimorph for various edge support conditions, such as simply supported edge, clamped edge, and elastically supported edge, with different radius ratios of the piezoelectric layer bonded to the substrate layer (fully covered and partially covered). Based on the CLPT, Prasad et al. (2006) proposed a transverse deflection model for a CPUA considering two layers, a piezoelectric layer bonded to a substrate layer of larger diameter for pressure and voltage loading cases. Based on the CLPT, Deshpande and Saggere (2007) presented an analytical deflection model for multi-layered circular diaphragm-type piezoelectric actuators subjected to voltage and uniform pressure loads. The analytical model was found to be in agreement with the finite element results within 0.5% and with the experimental measurements within 4%. However, when applying the model for computing the deflections of micromachined thin-film piezoelectric actuators, one must be careful to use the correct thin-film material elastic properties and take into account the residual stresses typically encountered in thin films, especially in the piezoelectric and the electrode layers. Using piezoelectric constitutive equations and combining with thin-plate and small-bending elastic theory, Dong et al. (2007) derived the generalized equation of motion for bending of thin piezoelectric–metal composite plates. Although the solutions could account for both the influence of an applied electric field and a concentrated or uniformly distributed mechanical load, the simulated results were not experimentally validated. Especially, the bonding layer was not taken into account when establishing the model.

The bonding layer of a CPUA is relatively very thin and the contribution to the transverse deflection is always considered as small compared with the piezoelectric layer and substrate layer. In this case, when modeling the deflections of CPUAs, both the piezoelectric layer and substrate layer are taken into account while the bonding layer is always neglected. However, the structure stress of the CPUA induced by the piezoelectric layer should be transmitted to the substrate layer through the bonding layer. Theoretically speaking, it is reasonable that the static deflection model for CPUAs, considering that the influence of the bonding layer can accurately model the static deflections of CPUAs.

In this article, a new static deflection model for CPUAs subjected to voltage is established based on the CLPT and the bonding layer is taken into account as an individual layer. According to the established analytical model for CPUAs, the influences of the structural parameters, such as the ratio $(R_{2}/R_{1})$ of the radius of the piezoelectric layer to that of the substrate layer, the ratio $(h_{\mathrm{p}}/h_{\mathrm{m}})$ of the thickness of the piezoelectric layer to that of the substrate layer, the ratio $(h_{\mathrm{b}}/h_{\mathrm{m}})$ of the thickness of the bonding layer to that of the substrate layer, and material properties, including the elastic compliance constants $(s_{11}^{E}, s_{\mathrm{m}}$, and $s_{\mathrm{b}})$ of the piezoelectric layer, substrate layer, and bonding layer, on the transverse deflection are numerically simulated and the static and dynamic characteristics of the CPUA are tested by the established experimental setup.

## MODELING THE STATIC DEFLECTIONS OF CPUAS

The schematic of a partially covered CPUA is shown in Figure 1. According to Figure 1, the CPUA, which is made by bonding a polarized piezoelectric layer to a substrate layer using the conducting epoxy as the bonding layer, is an axisymmetric circular laminate and the deflection can be clearly represented by a cylindrical coordinate system. The physical dimensions of the partially covered CPUA and the cylindrical coordinate system with the plane of $z=0$ located in the upper surface of the substrate layer are shown in Figure 2(a) and (b), respectively. According to the theory of the small deflection of the axisymmetric circular laminate from the point of view of elastic mechanics, when establishing the static deflection model for the partially covered CPUA, the assumptions for the partially covered CPUA are as follows (Zhang and Wang, 2002): (1) the deflection of the partially covered CPUA is very small, (2) the Kirchhoff's assumption for thin plates is satisfied, (3) the strain and stress are continuous at the bonding layer, (4) the piezoelectric layer is elastically isotropic and the polarized direction is perpendicular to the laminate of the partially covered CPUA, and (5) the electric field strength along the thickness direction of the piezoceramics is uniform.

![](./images/811709299020529665_1.jpg)

Figure 1. Schematic of a partially covered CPUA.

![](./images/811709299020529665_2.jpg)
![](./images/811709299020529665_3.jpg)

Figure 2. Physical dimension of the partially covered CPUA and the cylindrical coordinates: (a) the cross-sectional view and (b) the top view.

In order to facilitate the analysis, the partially covered CPUA is divided into two parts: the circular three-layer part and the annular substrate layer part. The circular three-layer part is the composite laminate of the piezoelectric layer, bonding layer, and substrate layer right beneath them. The annular substrate layer part is the substrate layer uncovered with the piezoelectric layer. According to Li and Chen (2003), the influence of the Poisson's ratios of the component materials on the deflection of the CPUA is less than $3\%$ and the Poisson's ratios of the three materials of the CPUA are nearly close, the Poisson's ratios of the three materials can be considered as same approximately. According to the CLPT, the relationships between the radial and circumferential strains and the deflections of the CPUA can be expressed as (Timoshenko and Woinowsky-Krieger, 1959; Vinson, 1974):

$$
S_{r}=\frac{\mathrm{d} u}{\mathrm{~d} r}+\left(z-Z_{\mathrm{c}}\right)\left(-\frac{\mathrm{d}^{2} \omega}{\mathrm{d} r^{2}}\right) \tag{1}
$$

$$
S_{\theta}=\frac{u}{r}+\left(z-Z_{\mathrm{c}}\right)\left(-\frac{1}{r} \frac{\mathrm{d} \omega}{\mathrm{d} r}\right) \tag{2}
$$

where $S_{r}$ and $S_{\theta}$ are the strains of the CPUA along the radial and circumferential directions, respectively; $\omega$ the transverse deflection along $z$-axis; $u$ the lateral deflection in the radial direction (in the plane of $z=0$ ); and $Z_{\mathrm{c}}$ the location of the neutral surface, in which the potential energy reaches the minimum (Dobrucki and Pruchnicki, 1997).

The constitutive equations for the piezoelectric layer are given by:

$$
S_{r}=s_{11}^{E}\left(\sigma_{r \mathrm{p}}-v \sigma_{\theta \mathrm{p}}\right)-d_{31} E_{3} \tag{3a}
$$

$$
S_{\theta}=s_{11}^{E}\left(\sigma_{\theta \mathrm{p}}-v \sigma_{r \mathrm{p}}\right)-d_{31} E_{3} \tag{3b}
$$

$$
D_{3}=-d_{31}\left(\sigma_{r \mathrm{p}}+\sigma_{\theta \mathrm{p}}\right)+\varepsilon_{33}^{T} E_{3} \tag{3c}
$$

where $s_{11}^{E}$ and $v$ are the elastic compliance constant and Poisson's ratio of the piezoceramics, respectively; $\sigma_{r p}$ and $\sigma_{\theta p}$ the stresses of the piezoceramics along the radial and circumferential directions, respectively; $\varepsilon_{33}^{T}$ the permittivity; $d_{31}$ the piezoelectric constant; $D_{3}$ the electric displacement; $E_{3}$ the electric field strength along $z$-axis, and $E_{3}=V / h_{\mathrm{p}}$ considering the applied voltage $V$ and the thickness $h_{\mathrm{p}}$ of the piezoelectric layer.

![](./images/811709299020529665_4.jpg)

Figure 3. Force analysis of the volume element in the partially covered CPUA.

Consider a volume element with dimension $\mathrm{d} r, \mathrm{~d} \theta$, and $\mathrm{d} z$ from the partially covered CPUA located at $(r, \theta$, and $z)$, as shown in Figure 2(b). The free body diagram of the volume element is shown in Figure 3. As shown in Figure 3, $N_{r}$ and $N_{\theta}$ are the components of the net forces along the radial and circumferential directions; $M_{r}$ and $M_{\theta}$ the components of the net moments along the radial and circumferential directions; and $Q_{r}$ the shear force. $N_{r}, N_{\theta}, M_{r}$, and $M_{\theta}$ of the circular three-layer part are given by:

$$
N_{r}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{r \mathrm{~m}} \mathrm{~d} z+\int_{0}^{h_{\mathrm{b}}} \sigma_{r \mathrm{~b}} \mathrm{~d} z+\int_{h_{\mathrm{b}}}^{h_{\mathrm{b}}+h_{\mathrm{p}}} \sigma_{r \mathrm{p}} \mathrm{d} z \tag{4}
$$

$$
N_{\theta}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{\theta \mathrm{m}} \mathrm{d} z+\int_{0}^{h_{\mathrm{b}}} \sigma_{\theta \mathrm{b}} \mathrm{d} z+\int_{h_{\mathrm{b}}}^{h_{\mathrm{b}}+h_{\mathrm{p}}} \sigma_{\theta \mathrm{p}} \mathrm{d} z \tag{5}
$$

$$
\begin{aligned}
M_{r}= & \int_{-h_{\mathrm{m}}}^{0} \sigma_{\mathrm{rm}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z+\int_{0}^{h_{\mathrm{b}}} \sigma_{r \mathrm{~b}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z \\
& +\int_{h_{\mathrm{b}}}^{h_{\mathrm{b}}+h_{\mathrm{p}}} \sigma_{r \mathrm{p}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z
\end{aligned}
$$

$$
\begin{aligned}
M_{\theta}= & \int_{-h_{\mathrm{m}}}^{0} \sigma_{\theta \mathrm{m}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z+\int_{0}^{h_{\mathrm{b}}} \sigma_{\theta \mathrm{b}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z \\
& +\int_{h_{\mathrm{b}}}^{h_{\mathrm{b}}+h_{\mathrm{p}}} \sigma_{\theta \mathrm{p}}\left(z-Z_{c}\right) \mathrm{d} z
\end{aligned}
$$

where $h$ represents the thickness; p, b, and m in the subscript represent the piezoelectric layer, bonding layer, and substrate layer, respectively.

Consider the components $N_{r \mathrm{o}}$ and $N_{\theta \mathrm{o}}$ of the net forces along the radial and circumferential directions of the annular substrate layer part and the components $M_{r \mathrm{o}}$ and $M_{\theta \mathrm{o}}$ of the net moments along the radial and circumferential directions. We have:

$$
N_{r \mathrm{o}}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{\mathrm{rm}} \mathrm{d} z
$$

$$
N_{\theta \mathrm{o}}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{\theta \mathrm{m}} \mathrm{d} z
$$

$$
M_{r \mathrm{o}}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{\mathrm{rm}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z
$$

$$
M_{\theta \mathrm{o}}=\int_{-h_{\mathrm{m}}}^{0} \sigma_{\theta \mathrm{m}}\left(z-Z_{\mathrm{c}}\right) \mathrm{d} z
$$

According to Equation (3), the radial and circumferential stresses of the piezoelectric layer can be expressed as:

$$
\sigma_{r \mathrm{p}}=\frac{1}{s_{11}^{E}\left(1-v^{2}\right)}\left[S_{r}+v S_{\theta}+(1+v) d_{31} E_{3}\right] \quad (12 \mathrm{a})
$$

$$
\sigma_{\theta \mathrm{p}}=\frac{1}{s_{11}^{E}\left(1-v^{2}\right)}\left[v S_{r}+S_{\theta}+(1+v) d_{31} E_{3}\right] \quad (12 \mathrm{~b})
$$

For the substrate layer, we have:

$$
\sigma_{\mathrm{rm}}=\frac{1}{s_{\mathrm{m}}\left(1-v^{2}\right)}\left(S_{r}+v S_{\theta}\right) \quad (13 \mathrm{a})
$$

$$
\sigma_{\theta \mathrm{m}}=\frac{1}{s_{\mathrm{m}}\left(1-v^{2}\right)}\left(v S_{r}+S_{\theta}\right) \quad (13 \mathrm{~b})
$$

where $s_{\mathrm{m}}$ is the elastic compliance constant of the substrate layer.

For the bonding layer, we have:

$$
\sigma_{r \mathrm{~b}}=\frac{1}{s_{\mathrm{b}}\left(1-v^{2}\right)}\left(S_{r}+v S_{\theta}\right) \quad (14 \mathrm{a})
$$

$$
\sigma_{\theta \mathrm{b}}=\frac{1}{s_{\mathrm{b}}\left(1-v^{2}\right)}\left(v S_{r}+S_{\theta}\right) \quad (14 \mathrm{~b})
$$

where $s_{\mathrm{b}}$ is the elastic compliance constant of the bonding layer.

In the absence of the external forces, the equilibrium equations for the axisymmetric plate are given by:

$$
\frac{\mathrm{d} N_{r}}{\mathrm{~d} r}+\frac{N_{r}-N_{\theta}}{r}=0
$$

$$
\frac{\mathrm{d} M_{r}}{\mathrm{~d} r}+\frac{M_{r}-M_{\theta}}{r}=Q_{r}=0
$$

where $Q_{r}$ is the shear force, which varies in the radial direction and can be neglected here (Wang et al., 2002).

Substitution of Equations (12)-(14) into Equations (4)-(7), substitution of Equations (4) and (5) into Equation (15), and substitution of Equations (6) and (7) into Equation (16) yield:

$$
\frac{C_{1}}{1-v^{2}}\left(\frac{\mathrm{d}^{2} u}{\mathrm{~d} r^{2}}+\frac{\mathrm{d} u}{r \mathrm{~d} r}-\frac{u}{r^{2}}\right)+\frac{C_{2}}{1-v^{2}}\left(\frac{\mathrm{d}^{3} \omega}{\mathrm{d} r^{3}}+\frac{\mathrm{d}^{2} \omega}{r \mathrm{~d} r^{2}}-\frac{\mathrm{d} \omega}{r^{2} \mathrm{~d} r}\right)=0
$$

$$
\frac{C_{3}}{1-v^{2}}\left(\frac{\mathrm{d}^{2} u}{\mathrm{~d} r^{2}}+\frac{\mathrm{d} u}{r \mathrm{~d} r}-\frac{u}{r^{2}}\right)+\frac{C_{4}}{1-v^{2}}\left(\frac{\mathrm{d}^{3} \omega}{\mathrm{d} r^{3}}+\frac{\mathrm{d}^{2} \omega}{r \mathrm{~d} r^{2}}-\frac{\mathrm{d} \omega}{r^{2} \mathrm{~d} r}\right)=0
$$

where $C_{1}, C_{2}, C_{3}$, and $C_{4}$ are the constants related to the material properties and structural parameters of the partially covered CPUA, and:

$$
C_{1}=\frac{h_{\mathrm{p}}}{s_{11}^{E}}+\frac{h_{\mathrm{b}}}{s_{\mathrm{b}}}+\frac{h_{\mathrm{m}}}{s_{\mathrm{m}}}
$$

$$
C_{2}=\frac{-\frac{1}{2} h_{\mathrm{p}}^{2}-h_{\mathrm{b}} h_{\mathrm{p}}+Z_{\mathrm{c}} h_{\mathrm{p}}}{s_{11}^{E}}+\frac{-\frac{1}{2} h_{\mathrm{b}}^{2}+Z_{\mathrm{c}} h_{\mathrm{b}}}{s_{\mathrm{b}}}+\frac{\frac{1}{2} h_{\mathrm{m}}^{2}+Z_{\mathrm{c}} h_{\mathrm{m}}}{s_{\mathrm{m}}}
$$

$$
C_{3}=\frac{\frac{1}{2} h_{\mathrm{p}}^{2}+h_{\mathrm{p}} h_{\mathrm{b}}-Z_{\mathrm{c}} h_{\mathrm{p}}}{s_{11}^{E}}+\frac{\frac{1}{2} h_{\mathrm{b}}^{2}-Z_{\mathrm{c}} h_{\mathrm{b}}}{s_{\mathrm{b}}}+\frac{-\frac{1}{2} h_{\mathrm{m}}^{2}-Z_{\mathrm{c}} h_{\mathrm{m}}}{s_{\mathrm{m}}}
$$

$$
\begin{aligned}
C_{4}= & \frac{-\frac{1}{3} h_{\mathrm{p}}^{3}-h_{\mathrm{p}}^{2} h_{\mathrm{b}}-h_{\mathrm{p}} h_{\mathrm{b}}^{2}+Z_{\mathrm{c}} h_{\mathrm{p}}^{2}+2 Z_{\mathrm{c}} h_{\mathrm{p}} h_{\mathrm{b}}-Z_{\mathrm{c}}^{2} h_{\mathrm{p}}}{s_{11}^{E}} \\
& +\frac{-\frac{1}{3} h_{\mathrm{b}}^{3}+Z_{\mathrm{c}} h_{\mathrm{b}}^{2}-Z_{\mathrm{c}}^{2} h_{\mathrm{b}}}{s_{\mathrm{b}}}+\frac{-\frac{1}{3} h_{\mathrm{m}}^{3}-Z_{\mathrm{c}} h_{\mathrm{m}}^{2}-Z_{\mathrm{c}}^{2} h_{\mathrm{m}}}{s_{\mathrm{m}}}
\end{aligned}
$$

Combining Equations (17) and (18) yields the differential equations for the motion of the circular three-layer part, which can be expressed as:

$$
\frac{\mathrm{d}^{2} u}{\mathrm{~d} r^{2}}+\frac{\mathrm{d} u}{r \mathrm{~d} r}-\frac{u}{r^{2}}=0
$$

$$
\frac{\mathrm{d}^{3} \omega}{\mathrm{d} r^{3}}+\frac{\mathrm{d}^{2} \omega}{r \mathrm{~d} r^{2}}-\frac{\mathrm{d} \omega}{r^{2} \mathrm{~d} r}=0
\tag{20}
$$

Equations (19) and (20) can also be obtained from the equilibrium equations, which are same as that for the three-layer part, given by Equations (15) and (16), for the motion of the annular substrate layer part. The general solution of Equations (19) and (20) yields the lateral and transverse deflections of the partially covered CPUA, which can be expressed as:

$$
u=-\frac{1}{2} B_{1} r^{-1}+B_{2} r
\tag{21}
$$

$$
\omega=-\frac{1}{2} B_{3} \ln r+\frac{1}{2} B_{4} r^{2}+B_{5}
\tag{22}
$$

where $B_{1}$, $B_{2}$, $B_{3}$, $B_{4}$, and $B_{5}$ are the undetermined coefficients that are determined by the boundary conditions.

The boundary conditions of the partially covered CPUA for the clamped edge are governed by:

$$
u(0)<\infty
\tag{23a}
$$

$$
\left.\frac{\mathrm{d} \omega}{\mathrm{d} r}\right|_{r=0}<\infty
\tag{23b}
$$

$$
\left.u\right|_{r=R_{2}}=\left.u_{\mathrm{o}}\right|_{r=R_{2}}
\tag{23c}
$$

$$
\left.\omega\right|_{r=R_{2}}=\left.\omega_{\mathrm{o}}\right|_{r=R_{2}}
\tag{23d}
$$

$$
\left.\frac{\mathrm{d} \omega}{\mathrm{d} r}\right|_{r=R_{2}}=\left.\frac{\mathrm{d} \omega_{\mathrm{o}}}{\mathrm{d} r}\right|_{r=R_{2}}
\tag{23e}
$$

$$
\left.N_{r}\right|_{r=R_{2}}=\left.N_{r \mathrm{o}}\right|_{r=R_{2}}
\tag{23f}
$$

$$
\left.M_{r}\right|_{r=R_{2}}=\left.M_{r \mathrm{o}}\right|_{r=R_{2}}
\tag{23g}
$$

$$
u_{\mathrm{o}}\left(R_{1}\right)=0
\tag{23h}
$$

$$
\omega_{\mathrm{o}}\left(R_{1}\right)=0
\tag{23i}
$$

$$
\left.\frac{\mathrm{d} \omega_{\mathrm{o}}}{\mathrm{d} r}\right|_{r=R_{1}}=0
\tag{23j}
$$

where $R_{1}$ and $R_{2}$ are the radiuses of the piezoelectric layer and the substrate layer, respectively; $u_{\mathrm{o}}$ and $\omega_{\mathrm{o}}$ the lateral deflection in the radial direction (in the plane of $z=0$) and the transverse deflection along $z$-axis of the annular substrate layer part, respectively.

Substitution of Equation (23) into Equations (21) and (22) yields the transverse deflections $\omega$ and $\omega_{\mathrm{o}}$ of the partially covered CPUA for the clamped edge, which can be expressed as:

$$
\omega=\frac{3(1+v) d_{31} s_{11}^{E} s_{\mathrm{b}} s_{\mathrm{m}}\left(C_{5}+C_{6}\right)\left[\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) r^{2}+2 R_{2}^{2} \ln \left(\frac{R_{2}}{R_{1}}\right)\right] V}{C_{7}+(1+v)^{2}\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right)^{2} C_{8}+4(1+v)\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) C_{9}}
$$

$$
0 \leq r \leq R_{2}
\tag{24a}
$$

$$
\omega_{\mathrm{o}}=\frac{3(1+v) d_{31} s_{11}^{E} s_{\mathrm{b}} s_{\mathrm{m}}\left(C_{5}+C_{6}\right)\left(\begin{array}{c}
2 R_{2}^{2} \mathrm{ln} r-\frac{R_{2}^{2}}{R_{1}^{2}} r^{2} \\
-2 R_{2}^{2} \ln R_{1}+R_{2}^{2}
\end{array}\right) V}{C_{7}+(1+v)^{2}\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right)^{2} C_{8}+4(1+v)\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) C_{9}}
$$

$$
R_{2} \leq r \leq R_{1}
\tag{24b}
$$

where $V$ is the applied voltage to the piezoelectric layer; $C_{5}$, $C_{6}$, $C_{7}$, $C_{8}$, and $C_{9}$ are the constants related to the material properties and structural parameters of the partially covered CPUA, and:

$$
C_{5}=s_{\mathrm{m}}(1+v)\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right)\left(h_{\mathrm{p}} h_{\mathrm{b}}+h_{\mathrm{b}}^{2}\right)
$$

$$
C_{6}=s_{\mathrm{b}}\left(4 h_{\mathrm{m}} h_{\mathrm{b}}+2 h_{\mathrm{m}}^{2}+h_{\mathrm{m}} h_{\mathrm{p}}\right)
$$

$$
C_{7}=4 s_{11}^{E 2} s_{\mathrm{b}}^{2} h_{\mathrm{m}}^{4}
$$

$$
C_{8}=s_{\mathrm{b}}^{2} s_{\mathrm{m}}^{2} h_{\mathrm{p}}^{4}+s_{11}^{E} s_{\mathrm{b}} s_{\mathrm{m}}^{2}\left(4 h_{\mathrm{p}} h_{\mathrm{b}}^{3}+4 h_{\mathrm{p}}^{3} h_{\mathrm{b}}+6 h_{\mathrm{p}}^{2} h_{\mathrm{b}}^{2}\right)+s_{11}^{E 2} s_{\mathrm{m}}^{2} h_{\mathrm{b}}^{4}
$$

$$
\begin{aligned}
C_{9}= & s_{11}^{E} s_{\mathrm{b}}^{2} s_{\mathrm{m}}\left(2 h_{\mathrm{p}}^{3} h_{\mathrm{m}}+2 h_{\mathrm{p}} h_{\mathrm{m}}^{3}+6 h_{\mathrm{p}}^{2} h_{\mathrm{b}} h_{\mathrm{m}}\right. \\
& \left.+6 h_{\mathrm{p}} h_{\mathrm{b}}^{2} h_{\mathrm{m}}+6 h_{\mathrm{p}} h_{\mathrm{b}} h_{\mathrm{m}}^{2}+3 h_{\mathrm{p}}^{2} h_{\mathrm{m}}^{2}\right) \\
& +s_{11}^{E 2} s_{\mathrm{b}} s_{\mathrm{m}}\left(8 h_{\mathrm{b}} h_{\mathrm{m}}^{3}+8 h_{\mathrm{b}}^{3} h_{\mathrm{m}}+12 h_{\mathrm{b}}^{2} h_{\mathrm{m}}^{2}\right)
\end{aligned}
$$

It is worth noting that the undetermined coefficients $B_{1}$, $B_{2}$, $B_{3}$, $B_{4}$, and $B_{5}$ for the general solution given by Equations (21) and (22), which are not given the concrete expressions, could be obtained from $C_{5}$, $C_{6}$, $C_{7}$, $C_{8}$, and $C_{9}$.

Equation (24) defines the transverse deflection model for the partially covered CPUA for the clamped edge subjected to voltage. When establishing the static deflection model, the bonding layer is considered as an individual layer.

If the bonding layer is neglected, we have $h_{\mathrm{b}}=0$. Equation (24) can be rewritten as:

$$
\omega=\frac{3(1+v) d_{31} s_{11}^{E} s_{\mathrm{m}} C_{10}\left[\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) r^{2}+2 R_{2}^{2} \ln \left(\frac{R_{2}}{R_{1}}\right)\right] V}{C_{11}+(1+v)^{2}\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right)^{2} C_{12}+4(1+v)\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) C_{13}}
$$

$$
0 \leq r \leq R_{2}
\tag{25a}
$$

$$
\omega_{\mathrm{o}}=\frac{3(1+v) d_{31} s_{11}^{E} s_{\mathrm{m}} C_{10}\left(2 R_{2}^{2} \mathrm{ln} r-\frac{R_{2}^{2}}{R_{1}^{2}} r^{2}-2 R_{2}^{2} \ln R_{1}+R_{2}^{2}\right) V}{C_{11}+(1+v)^{2}\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right)^{2} C_{12}+4(1+v)\left(1-\frac{R_{2}^{2}}{R_{1}^{2}}\right) C_{13}}
$$

$$
R_{2} \leq r \leq R_{1}
\tag{25b}
$$

where $C_{10}$, $C_{11}$, $C_{12}$, and $C_{13}$ are the constants related to the material properties and structural parameters of the partially covered CPUA, and $C_{10}=2h_{\mathrm{m}}^{2}+2h_{\mathrm{m}}h_{\mathrm{p}}$, $C_{11}=4s_{11}^{E}h_{\mathrm{m}}^{4}$, $C_{12}=s_{\mathrm{m}}^{2}h_{\mathrm{p}}^{4}$, and $C_{13}=s_{11}^{E}s_{\mathrm{m}}(2h_{\mathrm{p}}^{3}h_{\mathrm{m}}+2h_{\mathrm{p}}h_{\mathrm{m}}^{3}+3h_{\mathrm{p}}^{2}h_{\mathrm{m}}^{2})$.

Equation (25) defines the transverse deflection model for the partially covered CPUA for the clamped edge subjected to voltage, in which the bonding layer of the partially covered CPUA is neglected. Through analysis, we see that the transverse deflection model for the partially covered CPUA for the clamped edge subjected to voltage determined by Equation (25) is identical to the model established by Mo et al. (2006).

## NUMERICAL SIMULATIONS AND DISCUSSIONS

The relationships between the transverse deflections of the partially covered CPUA for the clamped edge and the structural parameters, including the ratio $(R_{2}/R_{1})$ of the radius of the piezoelectric layer to that of the substrate layer, the ratio $(h_{\mathrm{p}}/h_{\mathrm{m}})$ of the thickness of the piezoelectric layer to that of the substrate layer, the ratio $(h_{\mathrm{b}}/h_{\mathrm{m}})$ of the thickness of the bonding layer to that of the substrate layer, as well as the relationships between the transverse deflections of the partially covered CPUA for the clamped edge and the material properties, including the elastic compliance constants $(s_{11}^{E}, s_{\mathrm{m}}$, and $s_{\mathrm{b}})$ of the piezoelectric layer, substrate layer, and bonding layer, are numerically simulated and analyzed utilizing the established model given by Equation (24). When conducting the numerical simulations, the materials of the piezoelectric layer, the bonding layer, and the substrate layer of the partially covered CPUA are the piezoceramics (type: YT-5NM), epoxy, and brass, respectively, whose material properties and structural parameters are listed in Table 1.

### Influence of the Applied Voltage

Considering that the material properties and structural parameters of the partially covered CPUA are constant, the numerically simulated transverse deflection curves of the partially covered CPUA subjected to different voltages and the numerically simulated relationships between the central deflections and the applied voltages are shown in Figures 4 and 5, respectively. In Figure 4, the deflection decreases near the edge and is maximum at the center of the CPUA. In addition, the transverse deflection increases on increasing the applied voltage at the same radius. According to Figure 5, it is clearly seen that the central deflection varies linearly with the applied voltage. When the structure of the partially covered CPUA is determined, the different deflections can be available by changing the applied voltage and the central deflection is directly proportional to the applied voltage.

### Influence of the Radius and Thickness

Considering that the material properties of the partially covered CPUA are constant and the applied voltage is 50 V, the numerically simulated relationships between the central deflections and the structural parameters, including the ratio $(R_{2}/R_{1})$ of the radius

Table 1. Material properties and structural parameters of the partially covered CPUA.

| Material                     | YT-5NM          | Epoxy           | Brass           |
|------------------------------|-----------------|-----------------|-----------------|
| Radius (mm)                  | 8               | 8               | 10              |
| Thickness (mm)               | 0.2             | 0.025           | 0.1             |
| Density $(\mathrm{kg}\,\mathrm{m}^{-3})$ | 7500            | 7000            | 8500            |
| Elastic compliance constant $(\mathrm{m}^{2}\,\mathrm{N}^{-1})$ | $1.82\times10^{-11}$ | $1.934\times10^{-10}$ | $1.01\times10^{-11}$ |
| Poisson's ratio              | 0.29            | 0.3             | 0.34            |
| Piezoelectric constant $(\mathrm{C}\,\mathrm{N}^{-1})$ | $-270\times10^{-12}$ | $-$             | $-$             |

![](./images/811709299020529665_5.jpg)

Figure 4. Numerically simulated transverse deflection curves of the partially covered CPUA subjected to different applied voltages.

![](./images/811709299020529665_6.jpg)

Figure 5. Numerically simulated relationship between the central deflection and the applied voltage.

of the piezoelectric layer to that of the substrate layer, the ratio $(h_{\rm p}/h_{\rm m})$ of the thickness of the piezoelectric layer to that of the substrate layer, and the ratio $(h_{\rm b}/h_{\rm m})$ of the thickness of the bonding layer to that of the substrate layer, are shown in Figures 6-8, respectively.

According to Figure 6, when the thickness $(h_{\rm m})$ of the substrate layer is 0.1 mm and the radius $(R_{1})$ is 10 mm, the larger the radius ratio $(R_{2}/R_{1})$ is, the more severe the influence of the bonding layer thickness on the deflection is. The central deflection reaches a peak value when the radius ratio $(R_{2}/R_{1})$ is around 0.85-0.9. When $R_{2}=R_{1}$, that is to say, the CPUA is fully covered with the clamped support, the transverse deflection is 0, which means that the fully covered CPUA does not deform because the applied voltage has no influence on the deformation. The analysis result agrees well with the conclusion drawn by Mo et al. (2006). For the optimization of the CPUA, the optimal radius ratio $(R_{2}/R_{1})$ is around 0.85-0.9.

![](./images/811709299020529665_7.jpg)

Figure 6. Numerically simulated relationships between the central deflections and the radius ratio $(R_{2}/R_{1})$ of the partially covered CPUA for different thickness ratios $(h_{\rm b}/h_{m})$ when $h_{m}=0.1\,mm$, $R_{1}=10\,mm$, and $V=50V$.

According to Figure 7, when the thickness $(h_{\rm m})$ of the substrate layer is 0.1 mm, the thickness ratio $(h_{\rm b}/h_{\rm m})$ is 0, that is to say, the bonding layer is neglected, and the thickness ratio $(h_{\rm p}/h_{\rm m})$ is around 0.3, the central deflection of the partially covered CPUA reaches the peak value. When the thickness ratio $(h_{\rm b}/h_{\rm m})$ is 0.25, 0.5, 0.75, and 1.0, the central deflection decreases with increasing the thickness ratio $(h_{\rm p}/h_{\rm m})$.

![](./images/811709299020529665_8.jpg)

Figure 7. Numerically simulated relationships between the central deflections and the thickness ratio $(h_{\rm p}/h_{m})$ of the partially covered CPUA for different thickness ratios $(h_{\rm b}/h_{m})$ when $h_{m}=0.1\,mm$, $R_{1}=10\,mm$, $R_{2}=8\,mm$, and $V=50V$.

According to Figure 8, when the thickness $(h_{\rm m})$ of the substrate layer is 0.1 mm and the thickness ratio $(h_{\rm p}/h_{\rm m})$ is 0.5, the central deflection of the partially covered CPUA reaches the maximum value when the thickness ratio $(h_{\rm b}/h_{\rm m})$ approximately equals 0.2 instead of 0. The conclusion tallies well with Figure 7, from which we can see that the central deflection is not the maximum when the thickness ratio $(h_{\rm b}/h_{\rm m})$ is 0 and the thickness ratio $(h_{\rm p}/h_{\rm m})$ is less than 0.6. When the thickness ratio $(h_{\rm p}/h_{\rm m})$ equals 1, 1.5, and 2, the central deflection decreases linearly with increasing the thickness ratio $(h_{\rm b}/h_{\rm m})$. It is clearly seen from Figure 8 that the smaller the thickness ratio $(h_{\rm p}/h_{\rm m})$ is, the larger the central deflection is, when the thickness ratio $(h_{\rm p}/h_{\rm m})$ is more than or equal to 1.0. When designing the CPUA, large central deflection of the partially covered CPUA can be realized by reducing the thickness of the bonding layer, assuming strong attachment (or bonding) between the piezoelectric layer and the substrate is maintained.

![](./images/811709299020529665_9.jpg)

Figure 8. Numerically simulated relationships between the central deflections and the thickness ratio $(h_{\rm b}/h_{m})$ of the partially covered CPUA for different thickness ratios $(h_{\rm p}/h_{m})$ when $h_{m}=0.1\,mm$, $R_{1}=10\,mm$, $R_{2}=8\,mm$, and $V=50V$.

## Influence of the Material Properties

When the structural parameters of the partially covered CPUA are determined, the applied voltage is 50 V, and the elastic compliance constant $(s_{11}^{E})$ of the

![](./images/811709299020529665_10.jpg)

Figure 9. Numerically simulated relationships between the central deflections and the elastic compliance constant ratio $(\frac{s_m}{s_{11}^E})$ of the partially covered CPUA for different thickness ratios $(h_p/h_m)$ when $s_{11}^E=1.82\times 10^{-11}N^{-1}m^2$ and $V=50V$.

![](./images/811709299020529665_11.jpg)

Figure 10. Numerically simulated relationship between the central deflection and the elastic compliance constant $(s_b)$ of the bonding layer of the partially covered CPUA when $s_{11}^E=1.82\times 10^{-11}N^{-1}m^2$, $S_m=1.934\times 10^{-10}N^{-1}m^2$, and $V=50V$.

piezoelectric layer is $1.82\times 10^{-11}\text{m}^2\text{N}^{-1}$, the numerically simulated relationships between the central deflections and the elastic compliance constant ratio $\left(\frac{s_m}{s_{11}^E}\right)$ of the partially covered CPUA for different thickness ratios $(h_p/h_m)$ are shown in Figure 9 and the numerically simulated relationship between the central deflection and the elastic compliance constant $(s_b)$ of the bonding layer is shown in Figure 10.

In Figure 9, when $\frac{s_m}{s_{11}^E}<3$, $\frac{s_m}{s_{11}^E}$ has an apparent impact on the central deflection; when $\frac{s_m}{s_{11}^E}>3$, $\frac{s_m}{s_{11}^E}$ has a little impact on the deflection and the ratio $(h_p/h_m)$ of the thickness of the piezoelectric layer to the substrate layer should be considered primarily. In Figure 10, there are only a few nanometers of the central deflection of the partially covered CPUA when the elastic compliance constant $(s_b)$ of the bonding layer varies, so that there is a little influence of the elastic compliance constant $(s_b)$ of the bonding layer on the deflection of the partially covered CPUA. The elastic compliance constant of the bonding layer can be neglected when optimizing the performance of the partially covered CPUA.

## EXPERIMENTAL VALIDATION

### Experimental Setup

In order to verify the established transverse deflection model for the partially covered CPUA for the clamped support given by Equation (24), the schematic and photograph of the established experimental setup are shown in Figure 11(a) and (b), respectively. According to Figure 11, the experimental setup consists of the power amplifier for piezoelectric ceramic actuators (Wang et al., 2009; type: P&I-1, output voltage: 0-200V, linearity: $\geq99.98\%$, static ripple: $<20$mV, resolution: 10mV), the laser Doppler vibrometer (type: OFV-5000/OFV-505 from the Polytec GmbH), the real-time simulation system based on the dSPACE DS1103 with MATLAB/Simulink, the translation stage (type: WN104TA25H/WNMPC08, the parallel translation precision: $0.125\mu$m), and the tested CPUAs.

During test, the voltage applied to CPUA is generated by the real-time simulation system and amplified by the power amplifier. The positioning of the CPUA is realized using a translation stage that is controlled by a motion controller, and the deflection of the CPUA is measured by the laser Doppler vibrometer. The output of the laser Doppler vibrometer is sent to the host computer through the real-time simulation system.

In order to compare and according to the commercially available CPUA, two kinds of CPUAs, the partially covered CPUA with the ratio of the radius of the piezoelectric layer to the substrate layer $0.8$ ($R_2/R_1=0.8$) and half-covered CPUA with the ratio of the radius of the piezoelectric layer to substrate layer $0.5$ ($R_2/R_1=0.5$), are tested. The parameters of the partially covered and half-covered CPUAs are listed in Tables 1 and 2, respectively. The photograph of the partially covered CPUA is shown in Figure 12(a) and the photograph and exploded 3D drawing of the assembled partially covered CPUA for the clamped support are shown in Figure 12(b) and (c), respectively.

### Static Characteristics

The measured deflections of the partially covered CPUA for the clamped support subjected to voltages of 25, 50, 75, and 100V are shown in Figure 13(a)-(d), respectively. The theoretically predicted deflections considering and neglecting the bonding layer by Equation (24) and (25), as well as the fitted deflection curve in

![](./images/811709299020529665_12.jpg)

Figure 11. Experimental setup for the CPUAs: (a) the schematic and (b) the photograph.

<table>
<caption>Table 2. Material properties and structural parameters of the half-covered CPUA.</caption>
<thead>
<tr>
<th>Material</th>
<th>YT-5NM</th>
<th>Epoxy</th>
<th>Brass</th>
</tr>
</thead>
<tbody>
<tr>
<td>Radius (mm)</td>
<td>5</td>
<td>5</td>
<td>10</td>
</tr>
<tr>
<td>Thickness (mm)</td>
<td>0.16</td>
<td>0.01</td>
<td>0.1</td>
</tr>
<tr>
<td>Density ($\mathrm{kgm^{-3}}$)</td>
<td>7500</td>
<td>7000</td>
<td>8500</td>
</tr>
<tr>
<td>Plastic compliance constant ($\mathrm{m^{2}N^{-1}}$)</td>
<td>$1.82\times10^{-11}$</td>
<td>$1.934\times10^{-10}$</td>
<td>$1.01\times10^{-11}$</td>
</tr>
<tr>
<td>Poisson’s ratio</td>
<td>0.29</td>
<td>0.3</td>
<td>0.34</td>
</tr>
<tr>
<td>Piezoelectric constant ($\mathrm{CN^{-1}}$)</td>
<td>$-270\times10^{-12}$</td>
<td>–</td>
<td>–</td>
</tr>
</tbody>
</table>

least-squares sense according to the measured deflec-
tions, are also shown in Figure 13. The measured deflec-
tions of the half-covered CPUA for the clamped support
subjected to voltages of 25, 50, 75, and 100 V are shown
in Figure 14(a)–(d), respectively. The theoretically
predicted deflections considering and neglecting the
bonding layer by Equation (24) and (25), as well as the
fitted deflection curve in least-squares sense according to
the measured deflections, are also shown in Figure 14.
The measured relationships between the central deflec-
tions of the partially covered and half-covered CPUAs
and applied voltages are shown in Figure 15(a) and (b),
respectively. In Figure 15, the fitted relationships in least-
squares sense and theoretically predicted relationships by
the established model given by Equation (24) are also
presented.

In Figures 13 and 14, for both partially covered and
half-covered CPUAs for the clamped support, the
deflection model for the CPUAs considering the bond-
ing layer can predict the deflection of the CPUA more
accurately than that neglecting the bonding layer. The
predicted deflection errors for the partially covered
CPUA by the deflection model neglecting the bonding

![](./images/811709299020529665_13.jpg)

Figure 12. Partially covered CPUA: (a) the photograph of the partially covered CPUA, (b) the photograph of the assembled partially covered CPUA for the clamped support, and (c) the exploded 3D drawing of the partially covered CPUA for the clamped support.

![](./images/811709299020529665_14.jpg)

Figure 13. Measured and theoretically predicted deflections of the partially covered CPUA for the clamped support subjected to different applied voltages: (a) 25 V, (b) 50 V, (c) 75 V, and (d) 100 V.

![](./images/811709299020529665_15.jpg)

Figure 14. Measured and theoretically predicted deflections of the half-covered CPUA for the clamped support subjected to different applied voltages: (a) 25 V, (b) 50 V, (c) 75 V, and (d) 100 V.

![](./images/811709299020529665_16.jpg)

Figure 15. Measured and theoretically predicted relationships between the central deflections of the CPUA for the clamped support and applied voltage: (a) the partially covered CPUA and (b) the half-covered CPUA.

layer are obviously larger than those for the half-covered
CPUA, which agrees with the analytical results in
‘Influence of the Radius and Thickness’ section.

In order to quantify the modeling errors between the
theoretically predicted deflections and the experimental
data, the maximum error is defined as:

$$
\Delta_{\mathrm{MAX}}=\operatorname{MAX}[\omega(i)-\bar{\omega}(i)] \tag{26}
$$

where $\omega(i)$ and $\bar{\omega}(i)$ are the theoretically predicted and
experimentally fitted deflections of the tested CPUAs for
the clamped support, respectively; $i$ is the sampling index
and $1 \leq i \leq N$ ($N$ is the total number of sampling). The
relative maximum error is defined as:

$$
\delta_{\mathrm{MAX}}=\frac{\Delta_{\mathrm{MAX}}}{\omega_{\mathrm{MAX}}} \times 100 \% \tag{27}
$$

<table>
<thead>
<tr>
<th colspan="2">Voltage</th>
<th colspan="2">25 V</th>
<th colspan="2">50 V</th>
<th colspan="2">75 V</th>
<th colspan="2">100 V</th>
</tr>
<tr>
<th colspan="2">Error</th>
<th>$\Delta_{\text{MAX}}$ ($\times 10^{-4}$mm)</th>
<th>$\delta_{\text{MAX}}$ (%)</th>
<th>$\Delta_{\text{MAX}}$ ($\times 10^{-4}$mm)</th>
<th>$\delta_{\text{MAX}}$ (%)</th>
<th>$\Delta_{\text{MAX}}$ ($\times 10^{-4}$mm)</th>
<th>$\delta_{\text{MAX}}$ (%)</th>
<th>$\Delta_{\text{MAX}}$ ($\times 10^{-4}$mm)</th>
<th>$\delta_{\text{MAX}}$ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Partially covered CPUA</td>
<td>Neglecting bonding layer</td>
<td>8.32</td>
<td>14.56</td>
<td>14.42</td>
<td>12.24</td>
<td>21.77</td>
<td>12.22</td>
<td>24.79</td>
<td>9.98</td>
</tr>
<tr>
<td></td>
<td>Considering bonding layer</td>
<td>3.49</td>
<td>6.11</td>
<td>5.69</td>
<td>4.83</td>
<td>12.30</td>
<td>6.91</td>
<td>10.36</td>
<td>4.17</td>
</tr>
<tr>
<td>Half-covered CPUA</td>
<td>Neglecting bonding layer</td>
<td>4.21</td>
<td>8.45</td>
<td>7.76</td>
<td>7.48</td>
<td>12.53</td>
<td>7.93</td>
<td>6.60</td>
<td>3.05</td>
</tr>
<tr>
<td></td>
<td>Considering bonding layer</td>
<td>2.01</td>
<td>3.88</td>
<td>3.61</td>
<td>3.47</td>
<td>7.56</td>
<td>4.78</td>
<td>6.50</td>
<td>3.00</td>
</tr>
</tbody>
</table>

![](./images/811709299020529665_17.jpg)

Figure 16. Measured and theoretically predicted relationships between the central deflections and the frequencies of the applied voltages of the CPUAs for the clamped support: (a) the partially covered CPUA and (b) the half-covered CPUA.

where $\omega_{\text{MAX}}$ is the maximum value of the experimentally fitted central deflection of the partially covered and half-covered CPUAs for the clamped support. The maximum error $\Delta_{\text{MAX}}$ and relative maximum error $\delta_{\text{MAX}}$ between the theoretically predicted deflection and experimentally fitted deflection of the CPUAs subjected to different voltages are listed in Table 3. According to Table 3, the predicted deflection error by the deflection model for the partially covered and half-covered CPUAs considering the bonding layer can be reduced by 8.45% relative to that by the deflection model for the CPUA neglecting the bonding layer.

In Figure 15, the predicted central deflections of the tested CPUAs for the clamped support by the established model given by Equation (24) track the measured central deflections well. According to Equation (26), the maximum errors $\Delta_{\text{MAX}}$ between the measured and theoretically predicted central deflections of the partially covered and half-covered CPUAs for the clamped support are $1.7123 \times 10^{-4}$ mm and $5.2153 \times 10^{-4}$ mm, respectively. According to Equation (27), the relative maximum errors $\delta_{\text{MAX}}$ for the partially covered and half-covered CPUAs are 0.72% and 2.42%, respectively. In this case, the established deflection model considering the bonding layer can accurately predict the central deflections of the partially covered and half-covered CPUAs for the clamped support.

Dynamic Characteristics

When the sinusoidal voltages with amplitude of 50 and 100 V are individually applied to the partially covered and half-covered CPUAs for the clamped support, the measured relationships between the central deflections and the frequencies of the applied voltages are shown in Figure 16(a) and (b), respectively. The central deflections predicted by Equation (24) are also presented in Figure 16. According to Figure 16, the measured central deflections of the CPUAs subjected to the sinusoidal voltages do not agree with the theoretically predicted values. Except around the measured central deflections of the partially covered and half-covered CPUAs with applied voltage with frequency of 0 Hz, the other measured central deflections will increase on increasing the frequency of the applied voltage with different amplitudes. In addition, the central deflection of the partially covered CPUA appears the extremum when the frequency of the applied voltage approximately equals

800 Hz, while the central deflection of the half-covered CPUA appears the extremum when the frequency of the applied voltage approximately equals 550 Hz. According to the experimental results as shown in Figure 16, the resonant frequencies of the partially covered and half-covered CPUAs are 800 and 550 Hz, respectively, which are difficult to be calculated theoretically up to now. The differences between the measured and predicted central deflections of the CPUAs are mainly resulted from the fact that the hysteresis of the piezoceramics is not considered when establishing the deflection model for CPUAs for the clamped support given by Equation (24). In this case, the established deflection model given by Equation (24) in this article only fits to imitate the static deflection of the CPUAs subjected to static voltages. If the deflection model for CPUAs given by Equation (24) is used to predict the dynamic deflections, further research is needed.

## CONCLUSIONS

In this article, a new deflection model for CPUAs for the clamped support subjected to applied voltage was established based on the CLPT. When establishing the model, the bonding layer was taken into account as an individual layer. According to the established model for CPUAs for the clamped support, the influences of the structural parameters and material properties of the CPUA on the transverse deflections were numerically simulated and the static and dynamic characteristics of the CPUA were experimentally tested by the established experimental setup. The research results shown that the predicted static deflections of the CPUA by the established deflection model in this article agreed well with the measured results, the established static deflection model was more accurate than the existing model neglecting the bonding layer, and the maximum relative error was reduced by 8.45%. The static deflections of the CPUA were apparently affected by the structural parameters, such as the radius ratio of the piezoelectric layer to substrate layer, the thickness ratio of the piezoelectric layer to substrate layer, and the thickness ratio of the bonding layer to substrate layer, which indicated that the performances of the CPUA for the clamped support could be optimized by the structural parameters. In order to obtain larger deflection of the CPUAs, the structural parameters could be considered as follows: (1) the optimal radius ratio of the piezoelectric layer to substrate layer was around 0.85–0.9 when the other parameters were fixed, (2) the larger the radius ratio of the piezoelectric layer to substrate layer was, the larger the influence of the thickness of the bonding layer on the deflection was, and (3) the thickness of the bonding layer could be reduced assuming strong attachment (or bonding) between the piezoelectric layer and the substrate is maintained. Because the hysteresis of the piezoelectric materials was not considered when establishing the static deflection model for CPUAs, the modeling error apparently existed when utilizing the static deflection model to predict the dynamic characteristics of CPUAs.

## ACKNOWLEDGMENTS

The authors acknowledge the financial support by the Cultivation Fund of the Key Scientific and Technical Innovation Project, Ministry of Education of China (Grant No. 708048), the Program for New Century Excellent Talents in University (Grant No. NCET-05-0765), and the Foundation for the Author of National Excellent Doctoral Dissertation of PR China (Grant No. 200132).

## REFERENCES

Deshpande, M. and Saggere, L. 2007. "An Analytical Model and Working Equations for Static Deflections of a Circular Multi-layered Diaphragm-type Piezoelectric Actuator," *Sensors and Actuators A: Physical*, 136:673–689.

Ding, H.J., Xu, R.Q., Chi, Y.W. and Chen, W.Q. 1999. "Free Axisymmetric Vibration of Transversely Isotropic Piezoelectric Circular Plates," *International Journal of Solids and Structures*, 36:4629–4652.

Dobrucki, A.B. and Pruchnicki, P. 1997. "Theory of Piezoelectric Axisymmetric Bimorph," *Sensor and Actuator A: Physical*, 58:203–232.

Dong, S.X., Uchino, K., Li, L.T. and Viehland, D. 2007. "Analytical Solutions for the Transverse Deflection of a Piezoelectric Circular Axisymmetric Unimorph Actuator," *IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control*, 54:1240–1249.

Dorojkine, L.M., Volkov, V.V., Doroshenko, V.S., Lavrenov, A.A., Mourashov, D.A. and Rozanov, I.A. 1997. "Thin-film Piezoelectric Acoustic Sensors. Application to the Detection of Hydrocarbons," *Sensors and Actuators B: Chemical*, 44:488–494.

Heyliger, P.R. and Ramirez, G. 2000. "Free Vibration of Laminated Circular Piezoelectric Plates and Discs," *Journal of Sound and Vibration*, 229:935–956.

Li, S.F. and Chen, S.C. 2003. "Analytical Analysis of a Circular PZT Actuator for Valveless Micropumps," *Sensors and Actuators A: Physical*, 104:151–161.

Li, H.Q., Roberts, D.C., Steyn, J.L., Turner, K.T., Yaglioglu, O., Hagood, N.W., Spearing, S.M. and Schmidt, M.A. 2004. "Fabrication of a High Frequency Piezoelectric Microvalve," *Sensors and Actuators A: Physical*, 111:51–56.

Luan, G.T., Zhang, J.D. and Wang, R.Q. 2004. *Piezoelectric Transducer and Array (in Chinese)*, Peking University Press, Beijing.

Mo, C., Wright, R., Slaughter, S.W. and Clark, W.W. 2006. "Behaviour of a Unimorph Piezoelectric Actuator," *Smart Materials and Structures*, 15:1094–1102.

Morris, C.J. and Forster, F.K. 2000. "Optimization of a Circular Piezoelectric Bimorph for a Micropump Driver," *Journal of Micromechanics and Microengineering*, 10:459–465.

Papila, M., Sheplak, M. and Cattafesta III, L.N. 2008. "Optimization of Clamped Circular Piezoelectric Composite Actuators," *Sensors and Actuators A: Physical*, 147:310–323.

Prasad, S., Sankar, B., Cattafesta, L., Horowitz, S., Gallas, Q. and Sheplak, M. 2006. "Analytical Electroacoustic Model of a Piezoelectric Composite Circular Plate," *AIAA Journal*, 44:2311–2318.

Timoshenko, S. and Woinowsky-Krieger, S. 1959. *Theory of Plates and Shells*, McGraw-Hill, New York.

Vinson, J.R. 1974. *Structural Mechanics: The Behavior of Plates and Shells*, Wiley-Interscience, New York.

Wang, G., Sankar, B.V., Cattafesta, L.N. and Sheplak, M. 2002. "Analysis of a Composite Piezoelectric Circular Plate with Initial Stresses for MEMS," In: *Proceedings of 2002 ASME International Mechanical Engineering Congress and Exposition*, New Orleans, LA, USA, pp. 3–8.

Wang, D.H., Zhu, W., Yang, Q. and Ding, W.M. 2009. "A High-voltage and High-power Amplifier for Driving Piezoelectric Stack Actuators," *Journal of Intelligent Material Systems and Structures*, 20:1987–2001.

Woias, P. 2005. "Micropumps-Past, Progress and Future Prospects," *Sensors and Actuators B: Chemical*, 105:28–38.

Zhang, F.X. and Wang, L.K. 2002. *Modern Piezoelectricity (Vols. 1 and 2, in Chinese)*, Science Press, Beijing.