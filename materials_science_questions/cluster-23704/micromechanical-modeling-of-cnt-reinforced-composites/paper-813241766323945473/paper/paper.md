![](./images/813241766323945473_1.jpg)

# Analytical solutions for bending, buckling and vibration responses of carbon nanotube-reinforced composite beams resting on elastic foundation

Nuttawit Wattanasakulpong $^{a,*}$, Variddhi Ungbhakorn $^{b,1}$

$^{a}$ Department of Mechanical Engineering, Mahanakorn University of Technology, Nongchok, Bangkok 10530, Thailand
$^{b}$ Department of Mechanical Engineering, Chulalongkorn University, Bangkok 10330, Thailand

---

## ARTICLE INFO

**Article history:**
Received 1 October 2012
Received in revised form 12 December 2012
Accepted 28 January 2013
Available online 26 February 2013

**Keywords:**
Bending
Buckling
Vibration
CNTRC beams
Elastic foundation

---

## ABSTRACT

The objective of the present paper is to investigate the bending, buckling and vibration behaviors of carbon nanotube-reinforced composite (CNTRC) beams. The beams resting on the Pasternak elastic foundation, including a shear layer and Winkler spring, are considered. The single-walled carbon nanotubes (SWCNTs) are aligned and distributed in polymeric matrix with different patterns of reinforcement. The material properties of the CNTRC beams are estimated by using the rule of mixture. Various shear deformation theories are employed to deal with the problems. The mathematical models provided in this paper are numerically validated by comparison with some available results. New results of bending, buckling and vibration analyses of CNTRC beams based on several higher-order shear deformation theories are presented and discussed in details. Several aspects of beam types, spring constant factors, carbon nanotube volume fraction, etc., are taken into investigation.

© 2013 Elsevier B.V. All rights reserved.

---

## 1. Introduction

Carbon nanotubes (CNTs) have been accepted as an excellent candidate for the reinforcement of polymer composites due to their high elastic modulus, tensile strength and low density. The potential applications of polymer/CNTs are found in the field of reinforcing composites, high performance structural and multi-functional composites [1–3]. To enhance multiple properties of materials, the CNTs can be potentially incorporated into existing aerospace structural composites [4]. The critical challenge of producing polymer/CNTs composites is how to enhance dispersion and alignment of CNTs in a polymer matrix. Xie et al. [5] reviewed the available techniques and recent progress on dispersion and alignment of CNTs in the polymer matrix using ex situ technique, force and magnetic fields, electro-spinning and liquid crystalline phase induced methods.

Material properties of carbon nanotube-reinforced composites (CNTRCs) have been examined by many investigators. Thermo-mechanical properties of nanocomposites made from epoxy and low weight fractions of randomly oriented single-and multi-walled carbon nanotubes were presented by Fidelus et al. [6]. The elastic properties in macro scale of CNTRCs through analyzing the elastic deformation of a representative volume element subjected to different loading conditions were presented by Hu et al. [7]. The elastic properties of CNTRC were also simulated by using molecular dynamics (MD) in the investigation of Han and Elliott [8]. An addition of small amounts of CNTs to polymer matrix results in significant improvement of mechanical, electrical and thermal properties of the polymeric composites, as observed from the stress–strain curves of CNT-reinforced Epon 862 composites [9]. Deflection and stress behaviors of layered nanocomposite beams was investigated using a multiscale analysis [10]. To alleviate the problem of weak interfacial bonding between CNTs and polymer, the idea of functionally graded materials (FGMs) was suggested for producing CNT-based composite structures to have a smooth and continuous variation of CNTs within an isotropic matrix along the desired direction [11,12]. Consequently, the previous investigations on mechanics of FGM structures can be used as the useful information for further development and validation of CNTRC structures, which were provided in Refs. [13–18].

In actual applications, the CNTRCs can be incorporated in the structural elements such as beams, plates and shells. There are a few studies on the mechanical behavior of the CNTRC beams in the open literature. For example, Ke et al. [19] analyzed the nonlinear free vibration of the CNTRC beams by means of the Timoshenko beam theory, using the Ritz method and direct iterative procedure. Yas and Heshmati [20] presented the dynamic response of the nanocomposite beams with randomly oriented carbon nanotubes under moving load. Stability and dynamic characteristics of the

---

* Corresponding author. Tel./fax: +66 2 9883655x3106.
E-mail addresses: nuttawit_mut@hotmail.com (N. Wattanasakulpong), v_ungbhakorn@yahoo.com (V. Ungbhakorn).
1 Tel.: +66 2 218 6629; fax: +66 2 252 2889.

0927-0256/$ - see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.commatsci.2013.01.028

![](./images/813241766323945473_2.jpg)
![](./images/813241766323945473_3.jpg)

Timoshenko CNTRC beams resting on the elastic foundation were carried out by Yas and Samadi [21] using the generalized differential quadrature method (GDQM). For mechanical problems of the CNTRC plates, there are some previous reports available in the open literature [22–24].

In the present study, the bending, buckling and vibration of the CNTRC beams are investigated using the Navier solution method. The simply supported CNTRC beams which are placed on the Pas- ternak elastic foundation, including a shear layer and Winkler spring, are considered. Various shear deformation theories are em- ployed to solve such problems. New solutions of deflections, stres- ses, buckling loads, natural frequencies based on higher-order shear deformation theories are presented and discussed in details. Several aspects of spring constants, thickness ratios, CNT volume fractions, types of CNT distribution, etc., which have considerable impact on the analytical solutions are also investigated.

## 2. CNTRC beams

A straight CNTRC beam made from a mixture of SWCNT and an isotropic polymer matrix is considered. The beam, having length ($L$) and thickness ($h$), is placed on the Pasternak elastic foundation, including a shear layer and Winkler spring, as shown in Fig. 1a. In this study, the beams are assumed to have four different patterns of reinforcement over the cross sections as shown in Fig. 1b.

The effective material properties of CNTRC beams can be esti- mated using the rule of mixture. Therefore, the expressions of the effective Young's modulus and shear modulus of CNTRC beams are as follows [19,21].

$$
E_{11}=\eta_{1} V_{c n t} E_{11}^{c n t}+V_{p} E^{p} \tag{1a}
$$

$$
\frac{\eta_{2}}{E_{22}}=\frac{V_{c n t}}{E_{22}^{c n t}}+\frac{V_{p}}{E^{p}} \tag{1b}
$$

$$
\frac{\eta_{3}}{G_{12}}=\frac{V_{c n t}}{G_{12}^{c n t}}+\frac{V_{p}}{G^{p}} \tag{1c}
$$

$E_{11}^{c n t}, E_{22}^{c n t}$ and $G_{12}^{c n}$ are defined as the Young's modulus and shear modulus of SWCNT, and $E^{p}$ and $G^{p}$ as the corresponding material properties of the polymer matrix. Also, $V_{c n t}$ and $V_{p}$ are the volume fractions for carbon nanotube and the polymer matrix, respectively, with the relation of $V_{c n t}+V_{p}=1$. To consider the size-dependent material properties of SWCNT, the CNT efficiency parameters, $\eta_{i}(i=1,2,3)$, are introduced. They can be determined from matching the elastic moduli of CNTRCs estimated by the MD simulation with the numerical results estimated by the rule of mixture [8]. By using the same rule, Poisson's ratio ($v$) and mass density ($\rho$) of the CNTRC beams are written as:

$$
v=V_{c n t} v^{c n t}+V_{p} v^{p} ; \rho=V_{c n t} \rho^{c n t}+V_{p} \rho^{p} \tag{2}
$$

where $v^{c n t}, v^{p}$ and $\rho^{c n t}, \rho^{p}$ are the Poisson's ratios and densities of the CNT and polymer matrix respectively. For different patterns of car- bon nanotube reinforcement distributed across the cross sections of the beams as shown in Fig. 1b, the continuous mathematical func- tions used for describing the distributions of material constituents are given below:

$$
\text { UD-Beam : } \quad V_{c n t}=V_{c n t}^{*} \tag{3a}
$$

$$
\text { O-Beam : } \quad V_{c n t}=2\left(1-2 \frac{|z|}{h}\right) V_{c n t}^{*} \tag{3b}
$$

$$
\text { X-Beam : } \quad V_{c n t}=4 \frac{|z|}{h} V_{c n t}^{*} \tag{3c}
$$

$$
\text { V-Beam : } \quad V_{c n t}=\left(1+\frac{2 z}{h}\right) V_{c n t}^{*} \tag{3d}
$$

where $V_{c n t}^{*}$ is the given volume fraction of CNTs, which can be obtained from the following equation:

$$
V_{c n t}^{*}=\frac{W_{c n t}}{W_{c n t}+\left(\rho^{c n t} / \rho^{m}\right)\left(1-W_{c n t}\right)} \tag{4}
$$

where $W_{c n t}$ is the mass fraction of CNTs. From Eq. (3), it can be de- fined that the O-, X-and V-Beams are some kinds of functionally graded beams in which their material constituents are varied con- tinuously across their thicknesses; while, the UD-Beam has uni- formly distributed carbon nanotube reinforcement. In this study, the CNT efficiency parameters $(\eta_{i})$ associated with the given volume fraction $(V_{c n t}^{*})$ are: $\eta_{1}=1.2833$ and $\eta_{2}=\eta_{3}=1.0556$ for the case of $V_{c n t}^{*}=0.12 ; \eta_{1}=1.3414$ and $\eta_{2}=\eta_{3}=1.7101$ for the case of $V_{c n t}^{*}=0.17 ; \eta_{1}=1.3238$ and $\eta_{2}=\eta_{3}=1.7380$ for the case of $V_{c n t}^{*}=0.28$ [21].

![](./images/813241766323945473_4.jpg)

Fig. 1. Geometry of a CNTRC beam on elastic foundation (a) and cross sections of different patterns of reinforcement (b).

## 3. Equations of motion

Consider a shear deformation beam theory, the displacement field consisting of the axial displacement, $u$, and the transverse displacement, $w$, can be written in the following forms [14]:

$$
u(x, z, t)=u_{0}-z \frac{\partial w_{0}(x, t)}{\partial x}+\Psi(z) f_{0}(x, t) \tag{5a}
$$

$$
w(x, z, t)=w_{0}(x, t) \tag{5b}
$$

where $u_{0}$ and $w_{0}$ are the axial and transverse displacement at the reference plane of the beam, respectively. $f_{0}$, defined as the

transverse shear strain at any point on the reference plane, can be expressed as:

$$f_{0}(x,t)=\frac{\partial w_{0}(x,t)}{\partial x}-\phi_{0}(x,t).\tag{6}$$

Here, $\phi_{0}$ is the total bending rotation of the cross-section at any point of the reference plane and $t$ is time. A shape function $(\Psi)$ in Eq. (5) is used for describing the transverse shear stress distribution across the beam thickness. For different beam theories, their shape functions are shown in Table 1.

The expression of normal and shear strain components associated with the displacement field in Eq. (5) are as follows.

$$\varepsilon_{xx}=\frac{\partial u}{\partial x}=\frac{\partial u_{0}}{\partial x}-z\frac{\partial^{2}w_{0}}{\partial x^{2}}+\Psi(z)\left(\frac{\partial^{2}w_{0}}{\partial x^{2}}-\frac{\partial\phi_{0}}{\partial x}\right)\tag{7a}$$

$$\gamma_{xz}=\frac{\partial u}{\partial z}+\frac{\partial w}{\partial x}=\frac{\partial\Psi(z)}{\partial z}\left(\frac{\partial w_{0}}{\partial x}-\phi_{0}\right)\tag{7b}$$

To obtain the equations of motion, the Hamilton's principle is employed as follows.

$$\int_{t_{1}}^{t_{2}}(\delta U+\delta V-\delta K)dt = 0\tag{8}$$

where $\delta U$ is the virtual variation of the total strain energy, $\delta V$ is the virtual work done by external forces and $\delta K$ is the virtual kinetic energy. The initial and final time are defined as $t_{1}$ and $t_{2}$, respectively. Each of these quantities in Eq. (8) is derived next.

Consider a beam resting on elastic foundation, the virtual total strain energy $(\delta U=\delta U_{b}+\delta U_{f})$ is composed of the virtual strain energy of the beam $(\delta U_{b})$ and the virtual potential energy of the elastic foundation $(\delta U_{f})$. The virtual strain energy of the beam is

$$
\begin{aligned}
\delta U_{b} &=\int_{0}^{L} \int_{A}\left(\sigma_{xx} \delta \varepsilon_{xx}+\sigma_{xz} \delta \gamma_{xz}\right) d A d x \\
&=\int_{0}^{L}\left(N_{x} \frac{d \delta u_{0}}{d x}-M_{x} \frac{d^{2} \delta w_{0}}{d x^{2}}+P_{x}\left(\frac{d^{2} \delta w_{0}}{d x^{2}}-\frac{d \delta \phi_{0}}{d x}\right)+Q_{x}\left(\frac{d \delta w_{0}}{d x}-\delta \phi_{0}\right)\right) d x
\end{aligned}
\tag{9}
$$

It is noted that $N_{x}, M_{x}, P_{x}$ and $Q_{x}$ are the stress resultants in terms of the normal force, bending moment, higher-order generalized force and shear force, respectively. All stress resultants are defined as follows.

$$N_{x}=\int_{A}\sigma_{xx}dA\tag{10a}$$

$$M_{x}=\int_{A}z\sigma_{xx}dA\tag{10b}$$

$$P_{x}=\int_{A}\Psi(z)\sigma_{xx}dA\tag{10c}$$

$$Q_{x}=\int_{A}\frac{d\Psi(z)}{dz}\sigma_{xz}dA\tag{10d}$$

In terms of the virtual potential energy of the elastic foundation, this can be expressed as:

<table>
<caption>Table 1 The shape functions $(\Psi)$ for various beam theories.</caption>
<thead>
<tr>
<th>Beam theories</th>
<th>Shape functions</th>
</tr>
</thead>
<tbody>
<tr>
<td>First order shear deformation theory (FSDT)</td>
<td>$\Psi(z)=z$</td>
</tr>
<tr>
<td>Third order shear deformation theory (TSDT)</td>
<td>$\Psi(z)=z\left(1-\frac{4z^{2}}{3h^{2}}\right)$</td>
</tr>
<tr>
<td>Trigonometric shear deformation theory (TrSDT)</td>
<td>$\Psi(z)=\frac{h}{\pi}\sin\left(\frac{\pi z}{h}\right)$</td>
</tr>
<tr>
<td>Exponential shear deformation theory (ESDT)</td>
<td>$\Psi(z)=ze^{-2(z/h)^{2}}$</td>
</tr>
<tr>
<td>Hyperbolic shear deformation theory (HSDT)</td>
<td>$\Psi(z)=h\sinh\left(\frac{z}{h}\right)-z\cosh\left(\frac{z}{h}\right)$</td>
</tr>
</tbody>
</table>

$$\delta U_{f}=\int_{0}^{L}\left(K_{w}w_{0}\delta w_{0}+K_{s}\frac{dw_{0}}{dx}\frac{d\delta w_{0}}{dx}\right)dx.\tag{11}$$

where $K_{w}$ and $K_{s}$ are the Winkler and shearing layer spring constants which can be obtained from $K_{w}=\beta_{w}A_{110}/L^{2}$ and $K_{s}=\beta_{s}A_{110}$ in which $\beta_{w}$ and $\beta_{s}$ are the corresponding spring constant factors. It is also defined that $A_{110}$ is the extension stiffness or the value of $A_{11}$ of a homogeneous beam made of pure matrix material.

The virtual work done $(\delta V)$ by the transverse load $(q)$ and axially compressive force $(N_{x0})$ can be expressed as:

$$\delta V=-\int_{0}^{L}\left(q\delta w_{0}+N_{x0}\frac{dw_{0}}{dx}\frac{d\delta w_{0}}{dx}\right)dx\tag{12}$$

For the dynamic case, the virtual kinetic energy $(\delta K)$ is required for the equations of motion, which takes the form

$$\delta K=\int_{0}^{L}\rho(z)[\dot{u}\delta\dot{u}+\dot{w}\delta\dot{w}]dAdx\tag{13}$$

or

$$
\begin{aligned}
\delta K &=\int_{0}^{L}\left\{I_{0}\left(\dot{u}_{0} \delta \dot{u}_{0}+\dot{w}_{0} \delta \dot{w}_{0}\right)-I_{1}\left(\frac{d \dot{w}_{0}}{d x} \delta \dot{u}_{0}+\dot{u}_{0} \frac{d \delta \dot{w}_{0}}{d x}\right)+I_{2}\right. \\
&\left(\frac{d \dot{w}_{0}}{d x} \frac{d \delta \dot{w}_{0}}{d x}\right)+I_{3}\left(\frac{d \dot{w}_{0}}{d x} \delta \dot{u}_{0}-\dot{\phi}_{0} \delta \dot{u}_{0}+\dot{u}_{0} \frac{d \delta \dot{w}_{0}}{d x}-\dot{u}_{0} \delta \dot{\phi}_{0}\right) \\
&+I_{4}\left(\dot{\phi}_{0} \frac{d \delta \dot{w}_{0}}{d x}-2 \frac{d \dot{w}_{0}}{d x} \frac{d \delta \dot{w}_{0}}{d x}+\frac{d \dot{w}_{0}}{d x} \delta \dot{\phi}_{0}\right) \\
&\left.+I_{5}\left(\frac{d \dot{w}_{0}}{d x} \frac{d \delta \dot{w}_{0}}{d x}-\dot{\phi}_{0} \frac{d \delta \dot{w}_{0}}{d x}-\frac{d \dot{w}_{0}}{d x} \delta \dot{\phi}_{0}+\dot{\phi}_{0} \delta \dot{\phi}_{0}\right)\right\} d x
\end{aligned}
\tag{14}
$$

where the superposed dot on a variable indicates time derivative and $I_{i}(i=0,1,2...5)$ are the mass moments of inertia defined as

$$[I_{0},I_{1},I_{2}]=\int_{A}\rho(z)[1,z,z^{2}]dA\tag{15a}$$

$$[I_{3},I_{4}]=\int_{A}\rho(z)\Psi(z)[1,z]dA\tag{15b}$$

$$I_{5}=\int_{A}\rho(z)\Psi^{2}(z)dA\tag{15c}$$

The equations of motion of the general shear deformation beam theory that can be used to describe static and dynamic behavior of CNTRC beams are obtained by substituting $\delta U, \delta V$ and $\delta K$ into Eq. (8). Applying the integration-by-parts and collecting the coefficients of $\delta u_{0}, \delta \phi_{0}$ and $\delta w_{0}$ lead to the following equations of motion.

$$\delta u_{0}:\frac{dN_{x}}{dx}=I_{0}\ddot{u}_{0}-I_{1}\frac{d\ddot{w}_{0}}{dx}+I_{3}\left(\frac{d\ddot{w}_{0}}{dx}-\ddot{\phi}_{0}\right)\tag{16a}$$

$$\delta \phi_{0}:\frac{dP_{x}}{dx}-Q_{x}=I_{3}\ddot{u}_{0}-I_{4}\frac{d\ddot{w}}{dx}+I_{5}\left(\frac{d\ddot{w}_{0}}{dx}-\ddot{\phi}_{0}\right)\tag{16b}$$

$$
\begin{aligned}
\delta w_{0} &: \frac{d^{2} P_{x}}{d x^{2}}-\frac{d^{2} M_{x}}{d x^{2}}-\frac{d Q_{x}}{d x}+K_{w} w_{0}-K_{s} \frac{d^{2} w_{0}}{d x^{2}}-q+N_{x 0} \frac{d^{2} w_{0}}{d x^{2}} \\
&=-I_{0} \ddot{w}_{0}-I_{1} \frac{d \ddot{u}_{0}}{d x}+I_{2} \frac{d^{2} \ddot{w}_{0}}{d x^{2}}+I_{3} \frac{d \ddot{u}_{0}}{d x} \\
&+I_{4}\left(\frac{d \ddot{\phi}_{0}}{d x}-2 \frac{d^{2} \ddot{w}_{0}}{d x^{2}}\right)+I_{5}\left(\frac{d^{2} \ddot{w}_{0}}{d x^{2}}-\frac{d \ddot{\phi}_{0}}{d x}\right)
\end{aligned}
\tag{16c}
$$

It is observed that the equations of motion in Eq. (16) are the function of stress resultants. For beam analysis, using the linear constitutive relations, the normal and shear stresses can be expressed as:

$$\sigma_{xx}=Q_{11}(z)\varepsilon_{xx}\tag{17a}$$

$$\sigma_{xz}=Q_{55}(z)\gamma_{xz}\tag{17b}$$

where
$$
Q_{11}(z)=\frac{E_{11}(z)}{1-v^{2}(z)}, \quad Q_{55}(z)=G_{12}(z). \tag{18}
$$

From above relations, all stress resultants of Eq. (10) can be written in the form of material stiffness components and displacements as follows.
$$
N_{x}=A_{11} \frac{d u_{0}}{d x}-B_{11} \frac{d^{2} w_{0}}{d x^{2}}+C_{11}\left(\frac{d^{2} w_{0}}{d x^{2}}-\frac{d \phi_{0}}{d x}\right) \tag{19a}
$$

$$
M_{x}=B_{11} \frac{d u_{0}}{d x}-D_{11} \frac{d^{2} w_{0}}{d x^{2}}+E_{11}\left(\frac{d^{2} w_{0}}{d x^{2}}-\frac{d \phi_{0}}{d x}\right) \tag{19b}
$$

$$
P_{x}=C_{11} \frac{d u_{0}}{d x}-E_{11} \frac{d^{2} w_{0}}{d x^{2}}+H_{11}\left(\frac{d^{2} w_{0}}{d x^{2}}-\frac{d \phi_{0}}{d x}\right) \tag{19c}
$$

$$
Q_{x}=A_{55}\left(\frac{d w_{0}}{d x}-\phi_{0}\right) \tag{19d}
$$

where
$$
\left[A_{11}, B_{11}, D_{11}\right]=\int_{A} Q_{11}\left[1, z, z^{2}\right] d A \tag{20a}
$$

$$
\left[C_{11}, E_{11}\right]=\int_{A} Q_{11} \Psi(z)[1, z] d A \tag{20b}
$$

$$
H_{11}=\int_{A} Q_{11} \Psi^{2}(z) d A \tag{20c}
$$

$$
A_{55}=\int_{A} Q_{55}\left(\frac{d \Psi(z)}{d z}\right)^{2} d A \tag{20d}
$$

The stress resultants of Eq. (19) are substituted into Eq. (16) to obtain the equations of motion or the governing equations in the form of displacements as follows.
$$
A_{11} \frac{d^{2} u_{0}}{d x^{2}}-B_{11} \frac{d^{3} w_{0}}{d x^{3}}+C_{11}\left(\frac{d^{3} w_{0}}{d x^{3}}-\frac{d^{2} \phi_{0}}{d x^{2}}\right)=I_{0} \ddot{u}_{0}-I_{1} \frac{d \ddot{w}_{0}}{d x}+I_{3}\left(\frac{d \ddot{w}_{0}}{d x}-\ddot{\phi}_{0}\right) \ (21a)
$$

$$
\begin{gathered}
C_{11} \frac{d^{2} u_{0}}{d x^{2}}-E_{11} \frac{d^{3} w_{0}}{d x^{3}}+H_{11}\left(\frac{d^{3} w_{0}}{d x^{3}}-\frac{d^{2} \phi_{0}}{d x^{2}}\right)-A_{55}\left(\frac{d w_{0}}{d x}-\phi_{0}\right)=I_{3} \ddot{u}_{0}-I_{4} \frac{d \ddot{w}}{d x} \\
+I_{5}\left(\frac{d \ddot{w}_{0}}{d x}-\ddot{\phi}_{0}\right)
\end{gathered} \tag{21b}
$$

$$
\begin{gathered}
C_{11} \frac{d^{3} u_{0}}{d x^{3}}-E_{11} \frac{d^{4} w_{0}}{d x^{4}}+H_{11}\left(\frac{d^{4} w_{0}}{d x^{4}}-\frac{d^{3} \phi_{0}}{d x^{3}}\right)-B_{11} \frac{d^{3} u_{0}}{d x^{3}}+D_{11} \\
\times \frac{d^{4} w_{0}}{d x^{4}}-E_{11}\left(\frac{d^{4} w_{0}}{d x^{4}}-\frac{d^{3} \phi_{0}}{d x^{3}}\right)-A_{55}\left(\frac{d^{2} w_{0}}{d x^{2}}-\frac{d \phi_{0}}{d x}\right) \\
+K_{w} w_{0}-K_{s} \frac{d^{2} w_{0}}{d x^{2}}-q+N_{x 0} \frac{d^{2} w_{0}}{d x^{2}} \\
=-I_{0} \ddot{w}_{0}-I_{1} \frac{d \ddot{u}_{0}}{d x}+I_{2} \frac{d^{2} \ddot{w}_{0}}{d x^{2}}+I_{3} \frac{d \ddot{u}_{0}}{d x}+I_{4}\left(\frac{d \ddot{\phi}_{0}}{d x}-2 \frac{d^{2} \ddot{w}_{0}}{d x^{2}}\right) \\
+I_{5}\left(\frac{d^{2} \ddot{w}_{0}}{d x^{2}}-\frac{d \ddot{\phi}_{0}}{d x}\right)
\end{gathered} \tag{21c}
$$

## 4. Analytical solutions for bending, buckling and vibration problems

The governing equations, based on the general shear deformation theory, presented in Eq. (21), can be solved analytically for bending, buckling and vibration problems of CNT RC beams. For a beam simply supported at both ends, the Navier solution procedure can be applied to solve such problems. The admissible displacement functions in the form of trigonometric series which satisfy the boundary condition of the problems are given below:
$$
u_{0}(x, t)=\sum_{n=1}^{\infty} U_{n} e^{i \omega t} \cos \alpha x \tag{22a}
$$

$$
\phi_{0}(x, t)=\sum_{n=1}^{\infty} \Phi_{n} e^{i \omega t} \cos \alpha x \tag{22b}
$$

$$
w_{0}(x, t)=\sum_{n=1}^{\infty} W_{n} e^{i \omega t} \sin \alpha x \text { in which } i=\sqrt{-1} ; \alpha=n \pi / L \tag{22c}
$$

where $U_{n}, \Phi_{n}$ and $W_{n}$ are the unknown parameters and $\omega$ is the frequency of free vibration. For bending analysis, the transverse load $(q)$ is also written in the trigonometric form as follows.
$$
q(x)=\sum_{n=1}^{\infty} Q_{n} \sin \alpha x \tag{23}
$$

where $Q_{n}$ is defined as the load magnitude which can be obtained from the following equation.
$$
Q_{n}=\frac{2}{L} \int_{0}^{L} q(x) \sin \alpha x d x \tag{24}
$$

For different types of load, the load magnitude $(Q_{n})$ can be expressed as
$$
Q_{n}= \begin{cases}q_{0}(n=1) & \text { for sinusoidal load } q_{0} \\ \frac{4 q_{0}}{n \pi}(n=1,3,5 \ldots) & \text { for uniform load } q_{0}\end{cases} \tag{25}
$$

The admissible displacements of Eq. (22) and the load function of Eq. (23) are substituted into the equations of motion in Eq. (21) in order to obtain the analytical solutions. The results of the substitution can be arranged into the following matrix form.
$$
\left(\left[\begin{array}{lll}
s_{11} & s_{12} & s_{13} \\
s_{21} & s_{22} & s_{23} \\
s_{31} & s_{32} & s_{33}
\end{array}\right]-\omega^{2}\left[\begin{array}{lll}
m_{11} & m_{12} & m_{13} \\
m_{21} & m_{22} & m_{23} \\
m_{31} & m_{32} & m_{33}
\end{array}\right]\right)\left\{\begin{array}{c}
U_{n} \\
\Phi_{n} \\
W_{n}
\end{array}\right\}=\left\{\begin{array}{c}
0 \\
0 \\
Q_{n}
\end{array}\right\} \tag{26}
$$

where the matrix elements of Eq. (26) can be written as
$$
s_{11}=-A_{11} \alpha^{2}, s_{12}=C_{11} \alpha^{2}, s_{13}=B_{11} \alpha^{3}-C_{11} \alpha^{3} \tag{27a}
$$

$$
s_{21}=-C_{11} \alpha^{2}, s_{22}=H_{11} \alpha^{2}+A_{55}, s_{23}=E_{11} \alpha^{3}-H_{11} \alpha^{3}-A_{55} \alpha \tag{27b}
$$

$$
s_{31}=C_{11} \alpha^{3}-B_{11} \alpha^{3}, s_{32}=-H_{11} \alpha^{3}+E_{11} \alpha^{3}-A_{55} \alpha \tag{27d}
$$

$$
s_{33}=-E_{11} \alpha^{4}+H_{11} \alpha^{4}+D_{11} \alpha^{4}-E_{11} \alpha^{4}+A_{55} \alpha^{2}+K_{w}+K_{s} \alpha^{2}-N_{x 0} \alpha^{2} \tag{27e}
$$

And
$$
m_{11}=-I_{0}, m_{12}=I_{3}, m_{13}=I_{1} \alpha-I_{3} \alpha \tag{28a}
$$

$$
m_{21}=-I_{3}, m_{22}=I_{5}, m_{23}=-I_{5} \alpha+I_{4} \alpha \tag{28b}
$$

$$
m_{31}=-I_{1} \alpha+I_{3} \alpha, m_{32}=I_{4} \alpha-I_{5} \alpha, m_{23}=I_{0}+I_{2} \alpha^{2}-2 I_{4} \alpha^{2}+I_{5} \alpha^{2}. \tag{28c}
$$

To solve bending problem, the axial force $(N_{x 0})$ and natural frequency $(\omega)$ in Eq. (26) are set to zero. The resulting simultaneous equations can be solved for displacements and stresses of the bending problem. For buckling and vibration problems, the determinant of the coefficient matrix of Eq. (26) is set to zero and the non-trivial solution corresponding to each problem can be obtained. All analytical results are presented in the dimensionless forms which can be written as follows.

For bending analysis : $\bar{w}=100 \frac{E_{p} h^{3}}{q_{0} L^{4}} w\left(\frac{L}{2}\right) ; \bar{u}=100 \frac{E_{p} h^{3}}{q_{0} L^{4}} u\left(0,-\frac{h}{2}\right)$
$$
\bar{\sigma}_{x x}=\frac{h}{q_{0} L} \sigma_{x x}\left(\frac{L}{2}, \frac{h}{2}\right) ; \quad \bar{\sigma}_{x z}=\frac{h}{q_{0} L} \sigma_{x z}(0,0) \tag{29}
$$

For buckling analysis : $\quad \bar{N}_{x 0}=\frac{N_{x 0}}{A_{110}} \tag{30}$


For vibration analysis :

$$
\bar{\omega}=\omega L \sqrt{\frac{I_{00}}{A_{110}}} \tag{31}
$$

where $A_{110}$ and $I_{00}$ are $A_{11}$ and $I_{0}$ of beam made of pure matrix material, respectively.

## 5. Numerical results and discussion

### 5.1. Bending analysis of CNTRC beams

In this section, it is important to first verify the accuracy of the present mathematical models in predicting bending analysis of beams. Since the numerical results for bending analysis of CNTRC beams are not available in the literature, the bending results in terms of axial and transverse displacements as well as normal and shear stresses of isotropic ($p=0$) and functionally graded (FG) beams given by [18] are adopted to compare with the present results as shown in Table 2. The FG beams made from alumina (as ceramic) and aluminum (as metal) are considered and their material compositions are varied linearly across the beam thickness with the power law index, $p=1.0$. The details of material properties and dimensionless forms of displacements and stresses are conforming to Ref. [18]. As observed, the results are in good agreement. Using different shear deformation theories yields similar results of displacements and normal stress. However, the higher order shear deformation theories predict different shear stresses.

The following investigation is to present numerical exercises of bending analysis of CNTRC beams. The effective material properties of CNTRC beams at ambient temperature used throughout this paper are given as follows. Poly methyl methacrylate (PMMA) is used as the matrix and its material properties are: $v^{p}=0.3$; $\rho^{p}=1190 \mathrm{~kg} / \mathrm{m}^{3}$ and $E^{p}=2.5 \mathrm{GPa}$. For reinforcement material, the armchair $(10,10)$ SWCNTs whose properties are: $v^{c n t}=0.19$; $\rho^{c n t}=1400 \mathrm{~kg} / \mathrm{m}^{3} ; \quad E_{11}^{c n t}=600 \mathrm{GPa} ; \quad E_{22}^{c n t}=10 \mathrm{GPa}$ and $G_{12}^{c n t}=$ 17.2 GPa [21], is chosen.

Table 3 presents dimensionless displacements and stresses of the UD Beams with and without elastic foundation under uniformly distributed load and sinusoidal load, using TSDT. The beams with three different volume fractions of CNTs $\left(V_{c n t}^{*}\right)$ are investigated by varying the thickness ratios $(L / h)$. It can be seen that the beams resting on elastic foundation have lower displacements and stresses compared to those of the beams without elastic foundation for every thickness ratio. Moreover, increasing amount of CNTs leads to higher strength of CNTRC beams.

Fig. 2 illustrates the dimensionless transverse displacement based on TSDT for different types of CNTRC beams under uniform load. Clearly, the maximum displacements are at the middle of each beam with $x / L=0.5$. It can be seen that the strongest beam is the X-Beam with the smallest transverse displacement, and followed by the UD-,V-and O-Beams, respectively.

In Fig. 3, the comparisons between the dimensionless transverse displacements of the strongest beams (X-Beams) subjected to uniform and sinusoidal loads with different values of given CNT volume fractions are presented. The beams are assumed to be placed on elastic foundation and the TSDT is used to determine the results. It is clearly seen that the uniform load acting on the beams yields more deformation.

<table>
<caption>Table 2 Comparisons of displacements and stresses for isotropic and FG beams without elastic foundation subjected to uniform load (L/h=20).</caption>
<thead>
<tr>
<th>Source</th>
<th colspan="4">$p=0$</th>
<th colspan="4">$p=1.0$</th>
</tr>
<tr>
<th></th>
<th>$\bar{w}$</th>
<th>$\bar{u}$</th>
<th>$\bar{\sigma}_{x}$</th>
<th>$\bar{\sigma}_{x z}$</th>
<th>$\bar{w}$</th>
<th>$\bar{u}$</th>
<th>$\bar{\sigma}_{x}$</th>
<th>$\bar{\sigma}_{x z}$</th>
</tr>
</thead>
<tbody>
<tr>
<td>TSDT</td>
<td>2.8963</td>
<td>0.2336</td>
<td>15.0133</td>
<td>0.7427</td>
<td>5.8049</td>
<td>0.5735</td>
<td>23.2060</td>
<td>0.7426</td>
</tr>
<tr>
<td>ESDT</td>
<td>2.8962</td>
<td>0.2335</td>
<td>15.0148</td>
<td>0.7896</td>
<td>5.8048</td>
<td>0.5735</td>
<td>23.2177</td>
<td>0.7893</td>
</tr>
<tr>
<td>HSDT</td>
<td>2.8962</td>
<td>0.2335</td>
<td>15.0131</td>
<td>0.7402</td>
<td>5.8050</td>
<td>0.5735</td>
<td>23.2057</td>
<td>0.7402</td>
</tr>
<tr>
<td>TrSDT</td>
<td>2.8962</td>
<td>0.2335</td>
<td>15.0139</td>
<td>0.7660</td>
<td>5.8049</td>
<td>0.5735</td>
<td>23.2072</td>
<td>0.7659</td>
</tr>
<tr>
<td>[18]</td>
<td>2.8962</td>
<td>0.2306</td>
<td>15.0129</td>
<td>0.7451</td>
<td>5.8049</td>
<td>0.5686</td>
<td>23.2053</td>
<td>0.7451</td>
</tr>
</tbody>
</table>

<table>
<caption>Table 3 Dimensionless displacements and stresses of UD-Beams with and without elastic foundation under uniform and sinusoidal loads.</caption>
<thead>
<tr>
<th rowspan="2">$V_{cnt}^{*}$</th>
<th rowspan="2">$L/h$</th>
<th colspan="5">$\beta_{w}=0,\beta_{s}=0$</th>
<th colspan="4">$\beta_{w}=0.1,\beta_{s}=0.02$</th>
</tr>
<tr>
<th>$\bar{w}$</th>
<th>$\bar{u}$</th>
<th>$\bar{\sigma}_{x}$</th>
<th>$\bar{\sigma}_{x z}$</th>
<th></th>
<th>$\bar{w}$</th>
<th>$\bar{u}$</th>
<th>$\bar{\sigma}_{x}$</th>
<th>$\bar{\sigma}_{x z}$</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="11">Uniform load</td>
</tr>
<tr>
<td rowspan="3">0.12</td>
<td>10</td>
<td>0.704</td>
<td>0.173</td>
<td>8.399</td>
<td>0.701</td>
<td></td>
<td>0.594</td>
<td>0.148</td>
<td>7.053</td>
<td>0.602</td>
</tr>
<tr>
<td>15</td>
<td>0.524</td>
<td>0.074</td>
<td>11.849</td>
<td>0.716</td>
<td></td>
<td>0.400</td>
<td>0.058</td>
<td>9.556</td>
<td>0.568</td>
</tr>
<tr>
<td>20</td>
<td>0.461</td>
<td>0.045</td>
<td>15.448</td>
<td>0.725</td>
<td></td>
<td>0.311</td>
<td>0.031</td>
<td>10.316</td>
<td>0.520</td>
</tr>
<tr>
<td rowspan="3">0.17</td>
<td>10</td>
<td>0.449</td>
<td>0.107</td>
<td>8.268</td>
<td>0.704</td>
<td></td>
<td>0.403</td>
<td>0.097</td>
<td>7.374</td>
<td>0.638</td>
</tr>
<tr>
<td>15</td>
<td>0.344</td>
<td>0.048</td>
<td>11.762</td>
<td>0.719</td>
<td></td>
<td>0.286</td>
<td>0.040</td>
<td>9.736</td>
<td>0.614</td>
</tr>
<tr>
<td>20</td>
<td>0.307</td>
<td>0.029</td>
<td>15.384</td>
<td>0.726</td>
<td></td>
<td>0.232</td>
<td>0.022</td>
<td>11.568</td>
<td>0.575</td>
</tr>
<tr>
<td rowspan="3">0.28</td>
<td>10</td>
<td>0.325</td>
<td>0.082</td>
<td>8.562</td>
<td>0.697</td>
<td></td>
<td>0.299</td>
<td>0.076</td>
<td>7.869</td>
<td>0.647</td>
</tr>
<tr>
<td>15</td>
<td>0.235</td>
<td>0.034</td>
<td>11.959</td>
<td>0.714</td>
<td></td>
<td>0.206</td>
<td>0.030</td>
<td>10.469</td>
<td>0.638</td>
</tr>
<tr>
<td>20</td>
<td>0.203</td>
<td>0.020</td>
<td>15.530</td>
<td>0.723</td>
<td></td>
<td>0.167</td>
<td>0.017</td>
<td>12.751</td>
<td>0.613</td>
</tr>
<tr>
<td colspan="11">Sinusoidal load</td>
</tr>
<tr>
<td rowspan="3">0.12</td>
<td>10</td>
<td>0.562</td>
<td>0.121</td>
<td>6.970</td>
<td>0.472</td>
<td>0.475</td>
<td>0.104</td>
<td>5.890</td>
<td>0.399</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>0.416</td>
<td>0.054</td>
<td>9.716</td>
<td>0.475</td>
<td>0.319</td>
<td>0.041</td>
<td>7.439</td>
<td>0.364</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>0.365</td>
<td>0.033</td>
<td>12.608</td>
<td>0.476</td>
<td>0.247</td>
<td>0.022</td>
<td>8.535</td>
<td>0.322</td>
<td></td>
</tr>
<tr>
<td rowspan="3">0.17</td>
<td>10</td>
<td>0.358</td>
<td>0.076</td>
<td>6.842</td>
<td>0.473</td>
<td>0.321</td>
<td>0.068</td>
<td>6.126</td>
<td>0.424</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>0.273</td>
<td>0.035</td>
<td>9.630</td>
<td>0.476</td>
<td>0.227</td>
<td>0.029</td>
<td>8.021</td>
<td>0.396</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>0.243</td>
<td>0.022</td>
<td>12.543</td>
<td>0.476</td>
<td>0.184</td>
<td>0.016</td>
<td>9.520</td>
<td>0.362</td>
<td></td>
</tr>
<tr>
<td rowspan="3">0.28</td>
<td>10</td>
<td>0.260</td>
<td>0.058</td>
<td>7.130</td>
<td>0.472</td>
<td>0.239</td>
<td>0.054</td>
<td>6.573</td>
<td>0.435</td>
<td></td>
</tr>
<tr>
<td>15</td>
<td>0.187</td>
<td>0.025</td>
<td>9.824</td>
<td>0.475</td>
<td>0.164</td>
<td>0.022</td>
<td>8.639</td>
<td>0.418</td>
<td></td>
</tr>
<tr>
<td>20</td>
<td>0.161</td>
<td>0.015</td>
<td>12.689</td>
<td>0.476</td>
<td>0.133</td>
<td>0.012</td>
<td>10.485</td>
<td>0.393</td>
<td></td>
</tr>
</tbody>
</table>

The TSDT is used to determine the maximum transverse displacement of the X-Beam associated with the changes of spring constant factors as illustrated in Fig. 4. The reduction of transverse displacements is almost linear as the spring constant factors are increased.

Fig. 5 shows the dimensionless axial displacements of the CNTRC beams on elastic foundation subjected to a uniform load. Different types of the beams are considered using TSDT. As seen in Fig. 1b, the UD-, X-and O-Beams have symmetrical distribution of CNTs, whereas, the V-Beam is unsymmetrical. Therefore, it can be observed that the axial displacements at the middle plane $(z=0)$ are zero for the symmetrical beams, while it is not for the V-Beam.

The dimensionless normal stresses of CNTRC beams subjected to a uniform load are calculated by TSDT as shown in Fig. 6. Similar to the previous case of axial displacement, the unsymmetrical V- Beam has non-zero normal stress at the middle plane. For symmetrical beams, variation of normal stresses across their thicknesses shows different parabolic type distributions.

By using different higher-order shear deformation theories, the dimensionless shear stresses of the V-Beam on elastic foundation under a uniform load are presented in Fig. 7. It is observed that different theories predict different values of maximum shear stresses. The ESDT gives the largest value of the maximum shear stress.

![](./images/813241766323945473_5.jpg)

Fig. 2. Dimensionless transverse displacements of CNTRC beams on elastic foundation under uniform load $(L/h=20;\beta _{w}=0.1;\beta _{s}=0.02;V_{cnt}^{*}=0.12)$.

![](./images/813241766323945473_6.jpg)

Fig. 3. Dimensionless transverse displacements of X-Beams on elastic foundation under different loads $(L/h=20;\beta _{w}=0.1;\beta _{s}=0.02)$.

![](./images/813241766323945473_7.jpg)

Fig. 4. Dimensionless transverse displacements of X-Beam on elastic foundation under uniform load with variations of spring constant factors $(L/h=10;V_{cnt}^{*}=0.12)$.

### 5.2. Buckling analysis of CRTRC beams

For buckling analysis of CNTRC beams, the present solutions based on high-order shear deformation theories agree well with the buckling results of Timoshenko CNTRC beams given by Yas and Samadi [21] as shown in Table 4. Since the existence of stretching-bending coupling property in V-Beam due to its asymmetry, this coupling produces deflections and bending moments when the beam is under compressive loading. Therefore, V-Beam has no bifurcation-type buckling [25]. According to bending analysis, the X-Beam is the strongest beam that carries the largest buckling load and followed by the UD-Beam and O-Beam.

![](./images/813241766323945473_8.jpg)

Fig. 5. Dimensionless axial displacements of CNTRC beams under uniform load $(L/h=10;\beta _{w}=0.1;\beta _{s}=0.02;V_{cnt}^{*}=0.12)$.

![](./images/813241766323945473_9.jpg)

Fig. 6. Dimensionless normal stresses of CNTRC beams under uniform load $(L/h=10;\beta _{w}=0.1;\beta _{s}=0.02;V_{cnt}^{*}=0.12)$.

![](./images/813241766323945473_10.jpg)

Fig. 7. Dimensionless shear stresses of V-Beam under uniform load $(L/h=10;\beta _{w}=0.1;\beta _{s}=0.02;V_{cnt}^{*}=0.12)$.

In Fig. 8, the strongest beam (X-beam) with various volume fractions of CNTs is investigated using TSDT. The dimensionless critical buckling loads of the beams resting on elastic foundation are plotted against the thickness ratios. Increasing the thickness ratios leads to reduction in the buckling loads. The dramatic reduction of the buckling loads is found in the range of $L/h=10$ to 30.

To study the effects of spring constant factors on the buckling loads, Fig. 9 presents the dimensionless critical buckling loads of the X-beam with different spring constant factors, using TSDT. It

<table>
<caption>Table 4 Comparisons of critical loads for CNTRC beams with and without elastic foundation ($L/h=15;V_{cnt}^\ast=0.12$).</caption>
<thead>
<tr>
<th>Source</th>
<th colspan="3">$\beta_w=0,\beta_s=0$</th>
<th colspan="3">$\beta_w=0.1,\beta_s=0.02$</th>
</tr>
<tr>
<th></th>
<th>UD</th>
<th>O</th>
<th>X</th>
<th>UD</th>
<th>O</th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr>
<td>FSDT</td>
<td>0.1032</td>
<td>0.0604</td>
<td>0.1367</td>
<td>0.1333</td>
<td>0.0905</td>
<td>0.1668</td>
</tr>
<tr>
<td>TSDT</td>
<td>0.0984</td>
<td>0.0576</td>
<td>0.1289</td>
<td>0.1286</td>
<td>0.0878</td>
<td>0.1590</td>
</tr>
<tr>
<td>ESDT</td>
<td>0.0987</td>
<td>0.0574</td>
<td>0.1295</td>
<td>0.1288</td>
<td>0.0875</td>
<td>0.1596</td>
</tr>
<tr>
<td>HSDT</td>
<td>0.0984</td>
<td>0.0576</td>
<td>0.1288</td>
<td>0.1286</td>
<td>0.0878</td>
<td>0.1590</td>
</tr>
<tr>
<td>TrSDT</td>
<td>0.0985</td>
<td>0.0575</td>
<td>0.1291</td>
<td>0.1287</td>
<td>0.0876</td>
<td>0.1592</td>
</tr>
<tr>
<td>[21]</td>
<td>0.0986</td>
<td>0.0588</td>
<td>0.1288</td>
<td>0.1287</td>
<td>0.0889</td>
<td>0.1590</td>
</tr>
</tbody>
</table>

![](./images/813241766323945473_11.jpg)

Fig. 8. Dimensionless critical buckling loads of X-Beam on elastic foundation with various thickness ratios ($\beta_w=0.1;\beta_s=0.02$).

![](./images/813241766323945473_12.jpg)

Fig. 9. Dimensionless critical buckling loads of X-Beam on elastic foundation with various spring constant factors ($L/h=10;V_{cnt}^\ast=0.12$).

is seen that the buckling loads increase linearly as the increase of the spring constant factors.

### 5.3. Vibration analysis of CRTRC beams

For vibration analysis, the present frequencies of CNTRC beams are numerically validated by comparing with available frequencies based on the Timoshenko beam theory as shown in Table 5. From the comparisons, a close agreement among the results is observed. It is also found that the X-Beam has the highest natural frequency, while the O-Beam, the lowest.

The influences of CNT volume fractions and the thickness ratios on frequency results of the X-Beam are considered in Fig. 10. The TSDT is used to determine the frequencies of the beam resting on elastic foundation. The beams with more CNT volume fractions have higher values of frequencies. Similar to the case of buckling analysis, increasing the thickness ratios results in the decrease of frequencies, especially in the range of $L/h = 10$–30. In addition, the effects of spring constant factors on frequencies are shown in Fig. 11. It is seen that frequencies increase linearly as the spring constant factors increase.

<table>
<caption>Table 5 Comparisons of fundamental frequencies for CNTRC beams with and without elastic foundation ($L/h=15;V_{cnt}^\ast=0.12$).</caption>
<thead>
<tr>
<th>Source</th>
<th colspan="4">$\beta_w=0,\beta_s=0$</th>
<th colspan="4">$\beta_w=0.1,\beta_s=0.02$</th>
</tr>
<tr>
<th></th>
<th>UD</th>
<th>O</th>
<th>X</th>
<th>V</th>
<th>UD</th>
<th>O</th>
<th>X</th>
<th>V</th>
</tr>
</thead>
<tbody>
<tr>
<td>FSDT</td>
<td>0.9976</td>
<td>0.7628</td>
<td>1.1485</td>
<td>0.8592</td>
<td>1.1339</td>
<td>0.9339</td>
<td>1.2688</td>
<td>1.0142</td>
</tr>
<tr>
<td>TSDT</td>
<td>0.9745</td>
<td>0.7453</td>
<td>1.1152</td>
<td>0.8441</td>
<td>1.1137</td>
<td>0.9198</td>
<td>1.2387</td>
<td>1.0014</td>
</tr>
<tr>
<td>ESDT</td>
<td>0.9756</td>
<td>0.7440</td>
<td>1.1180</td>
<td>0.8448</td>
<td>1.1147</td>
<td>0.9187</td>
<td>1.2413</td>
<td>1.0020</td>
</tr>
<tr>
<td>HSDT</td>
<td>0.9745</td>
<td>0.7454</td>
<td>1.1151</td>
<td>0.8441</td>
<td>1.1137</td>
<td>0.9198</td>
<td>1.2387</td>
<td>1.0014</td>
</tr>
<tr>
<td>TrSDT</td>
<td>0.9749</td>
<td>0.7446</td>
<td>1.1163</td>
<td>0.8443</td>
<td>1.1140</td>
<td>0.9192</td>
<td>1.2397</td>
<td>1.0016</td>
</tr>
<tr>
<td>[21]</td>
<td>0.9753</td>
<td>0.7527</td>
<td>1.1150</td>
<td>0.9453</td>
<td>1.1144</td>
<td>0.9258</td>
<td>1.2386</td>
<td>1.0883</td>
</tr>
</tbody>
</table>

![](./images/813241766323945473_13.jpg)

Fig. 10. Dimensionless fundamental frequencies of X-Beam on elastic foundation with various thickness ratios ($\beta_w=0.1;\beta_s=0.02$).

![](./images/813241766323945473_14.jpg)

Fig. 11. Dimensionless fundamental frequencies of X-Beam on elastic foundation with various spring constant factors (TSDT; $L/h=10;V_{cnt}^\ast=0.12$).

### 6. Conclusions

In this present study, several shear deformation theories are employed to investigate the bending, buckling and vibration problems of simply supported CNTRC beams resting on elastic foundation. The beams are reinforced by different patterns of CNT distributions in the polymeric matrix. The accuracy of the mathematical models is numerically verified by comparison with some available results.

Based on the analytical results, it is found that the X-Beam is the strongest among different types of CNTRC beams in resisting bending and buckling loads, while the O-Beam is the weakest. Due to unsymmetrical distribution of CNTs in the V-Beam, this leads to

non-zero axial displacement and normal stress at the middle plane of the beam. Using different shear deformation theories yield sim- ilar results of displacement and normal stress, except for the shear stress. It is found that higher-order shear deformation theories play an important role when used for predicting shear stress. Increase in the spring constant factors of the elastic foundation results in reduction of the transverse displacement. For buckling and vibra- tion analyses, the critical buckling loads and frequencies are found to increase when the springs become stiffer. For the effect of thick- ness ratio, it is revealed that the transverse displacements, buck- ling loads and frequencies of CNTRC beams decrease as the increase of the thickness ratios. Additionally, the X-Beam also has the highest natural frequency and followed by the UD-,V-and O-Beams, respectively.

## References

[1] E.T. Thostenson, Z.F. Ren, T.W. Chou, Compos. Sci. Technol. 61 (2001) 1899-1912.
[2] K.T. Lau, D. Hui, Composites Part B. 33 (2002) 263-277.
[3] A.M.K. Esawi, M.M. Farag, Mater. Des. 28 (2007) 2394-2401.
[4] N. Yamamoto, R.G. Villoria, B.L. Wardle, Compos. Sci. Technol. (2012). http://dx.doi.org/10.1016/j.compscitech.2012.09.006.

[5] X.L. Xie, Y.W. Mai, X.P. Zhou, Mater. Sci. Eng. 49 (2005) 89-112.
[6] J.D. Fadelus, E. Wiesel, F.H. Gojny, K. Schulte, H.D. Wagner, Composites Part A 36 (2005) 1555-1561.
[7] N. Hu, H. Fukunaga, C. Lu, M. Kameyama, B. Yan, Proc. Royal Soc. A. 461 (2005) 1685-1710.
[8] Y. Han, J. Elliott, Comput. Mater. Sci. 39 (2007) 315-323.
[9] R. Zhu, E. Pan, A.K. Roy, Mater. Sci. Eng. A 447 (2007) 51-57.
[10] J. Wuite, S. Adali, Compos. Strut. 71 (2005) 388-396.
[11] S. Suresh, A. Mortensen, London: IOM Communications Ltd., 1998.
[12] S.H. Shen, Compos. Struct. 91 (2009) 9-19.
[13] S.A. Sina, H.M. Navazi, H. Haddadpour, Mater. Des. 30 (2009) 741-747.
[14] M. Simsek, Nucl. Eng. Des. 240 (2010) 697-705.
[15] N. Wattanasakulpong, B.G. Prusty, D.W. Kelly, Int. J. Mech Sci. 53 (2011) 734-743.
[16] N. Wattanasakulpong, B.G. Prusty, D.W. Kelly, M. Hoffman, Mater. Des. 36 (2012) 182-190.
[17] M. Aydogdu, V. Taskin, Mater. Des. 28 (2007) 1651-1656.
[18] H.T. Thai, T.P. Vo, Int. J. Mech. Sci. 62 (2012) 57-66.
[19] L.L. Ke, J. Yang, S. Kitipornchai, Compos. Struct. 92 (2010) 676-683.
[20] M.H. Yas, M. Heshmati, Appl. Math. Model. 36 (2012) 1371-1394.
[21] M.H. Yas, N. Samadi, Int. J. Press Ves. Pip. (2012). http://dx.doi.org/10.1016/j.ijpvp.2012.07.012.
[22] Z. Ping, Z.X. Lei, K.M. Liew, Compos. Strut. 94 (2012) 1450-1460.
[23] H.S. Shen, C.L. Zhang, Mater. Des. 31 (2010) 3403-3411.
[24] Z.X. Wang, H.S. Shen, Comput. Mater. Sci. 50 (2011) 2319-2330.
[25] K.M. Liew, J. Yang, S. Kitipornchai, Int. J. Solid Strut. 40 (2003) 3869-3892.