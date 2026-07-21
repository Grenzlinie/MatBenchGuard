# Analytical study of an active piezoelectric absorber on vibration attenuation of a plate

Y.M. Huang*, S.C. Hung

Department of Mechanical Engineering, National Central University, Jhongli 320, Taiwan, ROC

---

## ARTICLE INFO

Article history:
Received 30 October 2009
Received in revised form
6 August 2010
Accepted 19 August 2010
Handling Editor: D.J. Wagg
Available online 25 September 2010

## ABSTRACT

The attenuation of the transverse vibration of a plate, subjected to a harmonic force, is studied. This goal can be achieved by using an active dynamic absorber. The active absorber is made of a pair of piezoelectric sheets, attached to both sides of the plate, and closed electric circuits. One piece of the piezoelectric material provides a sensor for detecting the motion of the plate. Another piece serves as an active dynamic absorber. The equations of motion of the composite plate, including the plate and the piezoelectric material, and the circuit equations of the sensor and the absorber are derived. The displacements of the plate and the currents in the circuits are calculated. The active absorber can successfully attenuate the vibration. The numerical results show that the proposed active absorber can offer more reduction than that using a passive absorber while the absorber is designed to suppress the resonance of a particular vibration mode. Moreover, the active absorber can also reduce the displacements corresponding to other uncontrolled modes. The effects of altering various parameters of the active absorber are studied and discussed.

© 2010 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Mechanical systems or structures may encounter severe vibration owing to external excitations or disturbances. This can further result in degrading the designed performance. For reducing vibration of structures, different control methods can be used [1,2].

Two types of control algorithms, active and passive, are usually employed. Using a dynamic absorber is a traditional, passive control method for reducing vibration near a particular natural frequency of the main system. A mechanical absorber consists of a secondary mass, a spring, and usually an additional damper [3]. The passive absorber suffers from an inherent feature, i.e., the sensitivity of the attenuation effect to the absorber's parameters. In practice, one may obtain unsatisfied results if the parameters of the main system or the absorber are not precisely estimated. For overcoming this characteristic, the design of an active or adaptive absorber is brought out. Since these devices still preserve the properties of a traditional absorber, they are sometimes referred to as active-passive or semi-active absorbers. Various control methods have been employed to active absorbers [4]. However, only the topics of the papers close to this research are discussed here. Yuan [5] presented a tunable absorber by applying a displacement feedback and reassigning poles and zeros of the entire system. Filipovic and Schroder [6] proposed a single active absorber with displacement, velocity, and acceleration feedback for suppressing the vibration of a multimass vibrating system. However, not much result was

* Corresponding author. Tel.: +886 3 4267345; fax: +886 3 4254501.
E-mail address: t330005@cc.ncu.edu.tw (Y.M. Huang).

0022-460X/$ - see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.jsv.2010.08.025

demonstrated in the paper. An active absorber with an additional feedback compensator within the PZT actuator was proposed by Jalili and Knowles IV [7]. In the present study, an auto-tuning method was further introduced to effectively tune the compensator to improve the reduction effect. Hill and Snyder [8] designed a mechanical absorber with a continuous structure, a bell-rod set, to reduce the vibration of an electric transformer. Motion of the transformer with multifrequencies can be suppressed because of the existence of different resonant modes of the absorber. Similarly, Bonello et al. [9] developed a novel type of absorbers consisting of two curve beams with nonlinear stiffness. The characteristics of an active resonator were investigated by Sun et al. [10]. This resonator consists of two parts including an adaptive-passive vibration absorber along with an actuator providing a velocity-feedback control force to cancel the damping force. Steady-state responses were investigated to reveal the control effectiveness. However, no stability analysis was conducted. Recently, Utsumi [11] presented the numerical control results to the model of a building by using two absorbers. The introduction of feedback velocity signals has been proven effective for reduction in multiple frequencies. However, instability may occur when the control gain becomes large. His paper then introduced a new type controlled force for avoiding instability. Wu and Shao [12] developed a method to adaptively control the absorber with its stiffness dependent on the phase between the displacements of the main mass and the absorber. Besides the control methods mentioned previously, vibration reduction of a structure can also be achieved using absorbers with delayed feedback. This type of algorithm is demonstrated in Refs. [13,14].

For attenuating displacements with multiple frequencies, one active absorber usually cannot achieve the task. For overcoming the problem, one method proposed before was employing an absorber with an impact mechanism [15,16] which can eliminate energy of a wide range of frequencies.

Owing to the development of new materials, traditional mechanical absorbers can be replaced by absorbers made of smart materials, such as, shape memory alloys, magnetostrictive materials [17], and piezoelectric materials. Using the piezoelectric material along with a properly designed electric circuit can also form a passive absorber [18-20] for vibration and noise control. The piezoelectric absorber still possesses the drawback of a mechanical absorber. Therefore, the usage of an active piezoelectric absorber is necessary [21-23]. The control algorithm can be easily implemented by designing a specific circuit connecting to the piezoelectric material. Through the feedback of the different sensing signals [21-24], the motion of the structure is sent to the absorber for a more precisely control. In references [21,24], the self-sensing concept, through the bridge network, was brought out. Here, one piece of piezoelectric sheet can serve as the actuator and the sensor at the same time for different vibration control methods. Carabelli and Tonoli [25] showed that the measurement can be improved if the resistance in the bridge was replaced by an active element. The coupling effect of the bridge to the primary system can also serve as a vibration control mechanism.

In this research, an active piezoelectric absorber, with feedback from a piezoelectric sensor, is investigated for reducing vibration of the plate due to a harmonic point force. Our intention is to develop a simple but effective way for vibration attenuation of a continuous structure by applying an active absorber. The main contribution of this paper is the demonstration of multimode displacement attenuation achieved by employing an active piezoelectric absorber with velocity feedback. Some related references are discussed in the following. The paper by Tasi and Wang [26] mentioned an idea of using a passive/active absorber to reduce the random vibration of a beam. This paper brought out the idea of simultaneous use of a passive piezoelectric absorber and an actively controlled piezoelectric actuator on vibration reduction of a beam. The passive absorber also serves as the sensor for sending back the motion to the actuator. In this paper, the dynamics of a composite beam is detail investigated and a systematic design method was presented. In our paper, a bridge structure of circuit is adopted to feedback the velocity signal of the plate to the active absorber for reducing vibration. Numerical results are discussed and parametric studies are preformed. Related references about the sensor from a bridge are given in [11,21,24,25]. Our research is different from [11] because our sensor bridge is made of piezoelectric material while in [11] that is made of electric elements. The piezoelectric sensing bridge in [21,24] was not used on an absorber. In [25], most discussions were on the effectiveness of the sensor.

Other related papers, by Morgan and Wang [27,28], focused on the effectiveness of the active-passive piezoelectric absorber by feedback signal of the charge on the piezoelectric material or displacements of the structure. The method can be employed in the vibration reduction of a structure subject to a time-varying excitation through application of a DSP controller.

## 2. Equations of motion of the plate

Consider a metal plate, shown in Fig. 1, with simply supported edges. Two thin piezoelectric sheets are symmetrically attached to both sides of the plate and serve for the purpose of an active dynamic absorber to reduce the vibration.

![](./images/811736686420557826_1.jpg)

Fig. 1. The plate and the attached piezoelectric material.

The in-plane spatial coordinates on the plate are x and y. Coordinate z is in the transverse direction. The displacements of the plate and the piezoelectric material are denoted as $U_x(x,y,z,t)$, $U_y(x,y,z,t)$, and $U_z(x,y,z,t)$ with $t$ representing the time.

### 2.1. Equations of motion
The equations of motion of the composite system, including the plate and the piezoelectric material, can be obtained by Hamilton's principle as follows:

$$
\delta \int (Km+Kp-Wm-Wp)=0 \tag{1}
$$

where $\delta$ represents the variation notation, $K$ is the kinetic energy, and $W$ is the potential energy. The symbol with subscript $m$ represents a physical quantity of the metal plate and the symbol with subscript $p$ is that of the piezoelectric material. The kinetic energy of the transverse vibrating plate is written as

$$
Km=\int_{V_m} \frac{1}{2} \rho_m \boldsymbol{U}^T \boldsymbol{U} \mathrm{d}V \tag{2}
$$

and that of the piezoelectric material is

$$
Kp=\int_{V_p} \frac{1}{2} \rho_p \boldsymbol{U}^T \boldsymbol{U} \mathrm{d}V \tag{3}
$$

where $U=\{U_x,U_y,U_z\}$ is the displacement vector, and $\rho$ and $V$ are the density and the total volume, respectively.

The potential energy of the metal plate can be presented as

$$
W_m=\int_{V_m} \left[\frac{1}{2} \boldsymbol{S}^T \boldsymbol{c}_m \boldsymbol{S}-FzUz\right] \mathrm{d}V \tag{4}
$$

The first part in the integrand is the strain energy and the second part represents the work potential due to an external, volume distributed force $F_z$ in the $z$ direction. Here, the strain vector $\boldsymbol{S}=[S_{xx},S_{yy},S_{zz},S_{xz},S_{yz},S_{xy}]^T$ is related to the derivatives of displacements. Matrix $\boldsymbol{c}_m$ is the matrix of elastic constants and written as

$$
\boldsymbol{c}_m = \begin{bmatrix}
c_{11} & c_{12} & c_{13} & 0 & 0 & 0 \\
c_{12} & c_{22} & c_{13} & 0 & 0 & 0 \\
c_{13} & c_{13} & c_{33} & 0 & 0 & 0 \\
0 & 0 & 0 & c_{44} & 0 & 0 \\
0 & 0 & 0 & 0 & c_{44} & 0 \\
0 & 0 & 0 & 0 & 0 & c_{66}
\end{bmatrix} \tag{5}
$$

These constants are related to Young's modulus $Y$, Shear modulus $G$, and Poisson ratio $\mu$ by $C_{11}$=$C_{22}$=$C_{33}$=$Y/(1-\mu^2)$,$C_{12}$=$C_{13}$=$Y\mu/(1-\mu^2)$, $C_{44}$=$G$, and $C_{66}$=$Y/2(1+\mu)$. The electric enthalpy of the piezoelectric material is expressed as [11]

$$
W_p=\int_{V_p} \left[\frac{1}{2} \boldsymbol{S}^T \boldsymbol{c}_p \boldsymbol{S}-\boldsymbol{S}^T \boldsymbol{e}\mathrm{E}-\frac{1}{2} \boldsymbol{E}^T \boldsymbol{\varepsilon}^T \boldsymbol{E}\right] \mathrm{d}V \tag{6}
$$

with the matrix of elastic constants $\boldsymbol{c}_p$ similar to $\boldsymbol{c}_m$, $\boldsymbol{e}$ the matrix of piezoelectric constants and $\boldsymbol{\varepsilon}$ the matrix of dielectric constants written as

$$
\boldsymbol{e} = \begin{bmatrix}
0 & 0 & 0 & 0 & e_{15} & 0 \\
0 & 0 & 0 & e_{24} & 0 & 0 \\
e_{31} & e_{32} & e_{33} & 0 & 0 & 0
\end{bmatrix} \text{ and } \boldsymbol{\varepsilon} = \begin{bmatrix}
\varepsilon_{11} & 0 & 0 \\
0 & \varepsilon_{11} & 0 \\
0 & 0 & \varepsilon_{33}
\end{bmatrix} \tag{7}
$$

respectively, for the piezoelectric material polarized in the $z$ direction. Here, $\boldsymbol{E}=[0,0,E_z]^T$ is the vector of electric fields where only $E_z$ is considered if the piezoelectric material is polarized in the $z$ direction.

From Hamilton's principle, three coupled equations of motion can be obtained and expressed as [29]

$$
\left\{
\begin{aligned}
\rho_{m} \ddot{U}_{x}+\rho_{p} H^{*}(x, y) \ddot{U}_{x}-& \frac{\partial\left[\sigma_{x x}+\left(\sigma_{x x}-e_{31} E_{z}\right) H^{*}(x, y)\right]}{\partial x} \\
&-\frac{\partial\left[\sigma_{x y}+\sigma_{x y} H^{*}(x, y)\right]}{\partial y}-\frac{\partial\left[\sigma_{x z}+\sigma_{x z} H^{*}(x, y)\right]}{\partial z}=0 \\
\rho_{m} \ddot{U}_{y}+\rho_{p} H^{*}(x, y) \ddot{U}_{y}-& \frac{\partial\left[\sigma_{y y}+\left(\sigma_{y y}-e_{31} E_{z}\right) H^{*}(x, y)\right]}{\partial y} \\
&-\frac{\partial\left[\sigma_{x y}+\sigma_{x y} H^{*}(x, y)\right]}{\partial x}-\frac{\partial\left[\sigma_{y z}+\sigma_{y z} H^{*}(x, y)\right]}{\partial z}=0 \\
\rho_{m} \ddot{U}_{z}+\rho_{p} H^{*}(x, y) \ddot{U}_{z}-& \frac{\partial\left[\sigma_{z z}+\left(\sigma_{z z}-e_{31} E_{z}\right) H^{*}(x, y)\right]}{\partial z} \\
&-\frac{\partial\left[\sigma_{x z}+\sigma_{x z} H^{*}(x, y)\right]}{\partial x}-\frac{\partial\left[\sigma_{y z}+\sigma_{y z} H^{*}(x, y)\right]}{\partial y}=F_{z}
\end{aligned}
\right. \tag{8}
$$

within the stresses are written as $\sigma_{x x}, \sigma_{y y}, \sigma_{z z}, \sigma_{x z}, \sigma_{y z}$, and $\sigma_{x y}$. Note that no damping is introduced into the plate. In this research, two pieces of rectangular piezoelectric material are attached from $x_{1}$ to $x_{2}$ in the $x$ direction and from $y_{1}$ to $y_{2}$ in the $y$ direction. Notation $H^{*}(x, y)$ is a 2-D step function representing the covering area of the piezoelectric material. Then, $H^{*}(x, y)$ can be expressed as

$$
H^{*}(x, y)=H(x) H(y)=H_{x}(x) H_{y}(y)=\left(H\left(x_{1}\right)-H\left(x_{2}\right)\right)\left(H\left(y_{1}\right)-H\left(y_{2}\right)\right) \tag{9}
$$

where $H$ is the 1-D step function.

### 2.2. Love simplifications

According to Love simplifications, for a thin plate, the displacements can be approximately expressed as

$$
\left\{
\begin{aligned}
U_{x}(x, y, z, t) &=u_{x}(x, y, t)+z \beta_{x}(x, y, t) \\
U_{y}(x, y, z, t) &=u_{y}(x, y, t)+z \beta_{y}(x, y, t) \\
U_{z}(x, y, z, t) &=u_{z}(x, y, t)
\end{aligned}
\right. \tag{10}
$$

where $u_{x}, u_{y}$, and $u_{z}$ are mid-surface displacements. The rotating angles $\beta_{x}$ and $\beta_{y}$ can be derived by neglecting the shear strains $S_{x z}$ and $S_{y z}$ [30]. These requirements yield $\beta_{x}=-\partial u_{z} / \partial x$ and $\beta_{y}=-\partial u_{z} / \partial y$. As a result, the independent variables are reduced to $x, y$ and $t$. One can further neglect rotary inertia, i.e., the double time derivatives of $\beta_{x}$ and $\beta_{y}$ are zero. Three equations then can be combined into one in terms of displacement $u_{z}(x, y, t)$. The simplified equation of motion of the composite plate is written in the form of

$$
\begin{aligned}
& \rho_{m} h_{m} \ddot{u}_{z}+2 \rho_{p} h_{p} \ddot{u}_{z} H^{*}(x, y)+G_{s}(x, y, t) \\
= & F_{z}-e_{31} r_{a}\left(\phi_{a}+\phi_{s}\right) \delta^{\prime}(x) H(y)-e_{31} r_{a}\left(\phi_{a}+\phi_{s}\right) H(x) \delta^{\prime}(y)
\end{aligned} \tag{11}
$$

wherein $G_{s}(x, y)$ is a complicated function representing all stiffness terms of the composite plate and the last two terms in the right hand side describe the equivalent distributed forces due to piezoelectric effects. Here, two sheets of the piezoelectric material are attached to both sides of the plate surface. One sheet is acted as a dynamic absorber which contributes to electric potential $\phi_{a}$ while the other is the sensor which results in $\phi_{s}$. The expressions of $\phi_{a}$ and $\phi_{s}$ will be discussed in the next section. Notation $\delta^{\prime}$ is the twice derivative of the step function to the corresponding spatial coordinate, i.e., $\delta^{\prime}(x)=\mathrm{d}^{2} H_{x}(x) / \mathrm{d} x^{2}$ and $\delta^{\prime}(y)=\mathrm{d}^{2} H_{y}(x) / \mathrm{d} y^{2}$.

## 3. Design of the active piezoelectric absorber

For the purpose of vibration control, two piezoelectric sheets are symmetrically attached to both sides of the plate in the center position. One piezoelectric sheet along with a properly designed electric circuit can form a dynamic absorber similar to the traditional mass-spring absorber. Another piezoelectric sheet with certain electric circuit is attached to the other side of the plate for sensing purpose.

The electric field in the $z$ direction, induced by mechanical and electric effects of the piezoelectric material, can be expressed as [29]

$$
E_{z}=-h_{31}\left(S_{x x}+S_{y y}\right)+D_{z} / \varepsilon_{33} \tag{12}
$$

in which $h_{31}=e_{31} / \varepsilon_{33}$ is a piezoelectric constant and $D_{z}$ is the electric displacement in the $z$ direction. The piezoelectric effect then produces an electric potential $\phi=-\int_{h_{m} / 2}^{h_{m} / 2+h_{p}} E_{z} \mathrm{~d} z$ denoted as $\phi_{a}$ in the absorber and $\phi_{s}$ in the sensor. From the integration, electrical potential $\phi$ is the combination of $\phi^{*}(x, y)=\int_{h_{m} / 2}^{h_{m} / 2+h_{p}} h_{31}\left(S_{x x}+S_{y y}\right) \mathrm{d} z$ due to deflection of the plate and $\phi_{c}$ due to an equivalent capacitor $C_{p}=S_{p} \varepsilon_{33} / h_{p}$ [29]. Here, $S_{p}$ is the area of the piezoelectric material, $h_{m}$ and $h_{p}$ are the thicknesses of the metal plate and the piezoelectric material, respectively.

![](./images/811736686420557826_2.jpg)

Fig. 2. (a) The active absorber and (b) the sensor.

The piezoelectric absorber, including the piezoelectric material, an inductance and a resistance, is given in Fig. 2(a). A voltage source $V_a$=$KV_o$ is applied to the closed circuit for actively controlling the absorber with $K$ the control gain and $V_o$ the voltage output from the sensor. The circuit equation of the active absorber can be expressed as

$$
\frac{\mathrm{d}^{2}\left(L_{a} i_{a}\right)}{\mathrm{d} t^{2}}+\frac{\mathrm{d}\left(R_{a} i_{a}\right)}{\mathrm{d} t}+\frac{1}{C_{p}} i_{a}=\frac{\mathrm{d} V_{a}}{\mathrm{~d} t}+\frac{\mathrm{d} \phi_{a}^{*}(\tilde{x}, \tilde{y})}{\mathrm{d} t}
\tag{13}
$$

where $i_a(t) = \mathrm{d}D_z/\mathrm{d}t$ is the unknown current of the absorber and $\phi_a^*$ is evaluated at the location $(\tilde{x},\tilde{y})$ of the attached finite electrodes. Let $\omega_a$ represent the chosen natural frequency and $\zeta_a$ be the damping ratio of the absorber. Adopting a design rule similar to that of a mechanical dynamic absorber [3], the inductance $L_a$ and the resistance $R_a$ are defined as

$$
L_{a}=h_{p} /\left(S_{p} \varepsilon_{33} \omega_{a}^{2}\right) \quad \text { and } \quad R_{a}=2 \zeta_{a} \omega_{a} L_{a}
\tag{14}
$$

The terms in the left-hand side of (13) are equivalent to those of a mechanical dynamic absorber and the first term in the right-hand side is the feedback from the sensor.

The traditional, passive dynamic absorber, with $V_a$=0, can give a satisfactory result in eliminating vibration if the natural frequency of the absorber $\omega_a$ is exactly equal to the natural frequency of the primary system [3]. However, if these two frequencies do not match, the presence of the absorber can hardly affect the vibration. In our preliminary research, different types of feedback signals were sent to the absorber for overcome this drawback of a passive absorber. The results reveal that a velocity feedback of the main system can actually depress the frequency sensitivity of the absorber mentioned before and give a better control effect. A similar conclusion was also drawn and discussed in references [11,25]. On the contrary, the feedback signal containing displacement information can not significantly affect the attenuation effect of the absorber. In this paper, the sensor design (Fig. 2(b)) realizes the concept of sending back velocity information of the plate. The sensor is similar to the Wheatstone bridge in the papers by Dosch et al. [21] and by Anderson and Hagood [24]. The governing equations of the sensor are then given as

$$
\frac{\mathrm{d}\left(R_{1} i_{1}\right)}{\mathrm{d} t}+\frac{1}{C_{p}} i_{1}=\frac{\mathrm{d} V_{s}}{\mathrm{~d} t}+\frac{\mathrm{d} \phi_{1}^{*}(\tilde{x}, \tilde{y})}{\mathrm{d} t} \quad \text { and } \quad \frac{\mathrm{d}\left(R_{2} i_{2}\right)}{\mathrm{d} t}+\frac{1}{C_{2}} i_{2}=\frac{\mathrm{d} V_{s}}{\mathrm{~d} t}
\tag{15}
$$

where $R_1$ and $R_2$ are the additional resistances, $i_1(t)$ and $i_2(t)$ are currents, and $V_s$=$K_sV_o$ is the sensor input voltage with $K_s$ called a sensor gain or an amplification factor. Capacitor $C_p$ is from the piezoelectric sheet while capacitor $C_2$ is chosen proportional to $C_p$ for a standard bridge. In this design, the output voltage $V_o$=$V_2 - V_1$=$R_1(i_2 - i_1)$ of the sensor can be expressed in the following form in the frequency domain [24]

$$
V_{o}(s)=\frac{R_{1} C_{p} s}{1+R_{1} C_{p} s} \phi^{*}(s)+\left[\frac{R_{1} C_{p} s}{1+R_{1} C_{p} s}-\frac{R_{2} C_{2} s}{1+R_{2} C_{2} s}\right] V_{s}(s)
\tag{16}
$$

Here $\phi^* = \phi_a^* = \phi_s^*$ since both are resulted from the thin plate displacement. For $R_1$=$R_2$ and $s \ll 1/R_1C_2$, the output voltage $V_o(t)$ is approximately proportional to $\mathrm{d}\phi^*(\tilde{x},\tilde{y})/\mathrm{d}t$ and also the time derivative of the bending strain [24] which is proportional to the velocity of the plate. Therefore, feedbacking voltage $V_o$ to the active absorber is equivalent to sending back a velocity signal.

### 4. Solving the equation of motion

The displacement of the plate can be approximately expressed as
$$
u_{z}(x, y, t)=\sum_{m_{1}=1} \sum_{m_{2}=1} u_{m_{1} m_{2}}(t) \varphi_{m_{1} m_{2}}(x, y)
\tag{17}
$$
with $u_{m 1 m 2}(t)$ the generalized coordinate. Here, $\varphi_{m 1 m 2}$ is chosen as the normalized mode shape of the simply supported plate, without any piezoelectric material attachment, i.e.,
$$
\varphi_{m_{1} m_{2}}(x, y)=\frac{2}{\sqrt{a b \rho h_{m}}} \sin \left(\frac{m_{1} \pi x}{a}\right) \sin \left(\frac{m_{2} \pi y}{b}\right)
\tag{18}
$$

Following the standard procedures of Galerkin's method [3], the governing equation of the composite vibrating plate (11) is transformed to a set of ordinary differential equations in terms of $u_{m 1 m 2}(t)$. These equations are combined with the equations of electric circuits, derived in the last section, for simultaneously solving $u_{m 1 m 2}(t)$ and currents $i_{1}(t), i_{2}(t)$, and $i_{a}(t)$. Then, the motion of the plate is obtained by using (17).

### 5. Numerical results and discussions

In this paper, the material of the plate $(0.9 \mathrm{~m} \times 0.9 \mathrm{~m} \times 0.006 \mathrm{~m})$ is aluminum and the piezoelectric material is PVDF. Each piezoelectric sheet is of thickness $0.001 \mathrm{~m}$ and various areas. Table 1 shows the geometric and the material parameters of the plate and the piezoelectric material. For obtaining frequency responses of the plate, an external harmonic point force $F_{z}$, with forcing frequency $\omega$, is applied at the center point of the plate. Therefore, only the odd-modes are excited and need to be controlled. The natural frequencies $\omega_{n}$ of these modes, for the aluminum plate as well as the composite plate, are given in Table 2. Here, the first natural frequency of the aluminum plate is $\omega_{n 1}=36.49 \times 2 \pi \mathrm{rad} / \mathrm{s}$. The natural frequencies generally decrease due to the enlargement of the attached piezoelectric material.

Two piezoelectric sheets, each with size $0.4 \mathrm{~m} \times 0.4 \mathrm{~m}$ at first, are attached to both sides of the plate at the center. Except specified in the paper, the natural frequency of the absorber $\omega_{a}$ is set to $\omega_{c 1}=0.905 \omega_{n 1} \mathrm{rad} / \mathrm{s}$ which is the first natural frequency of the composite plate as shown in Table 2. The damping ratio of the absorber $\zeta_{a}$ is usually chosen as 0.001. This active absorber is designed to attenuate the resonance of mode $(1,1)$ of the vibrating plate.

#### 5.1. The sensor

The amplitude of the dimensionless velocity at the center of the plate and the sensor output voltage $V_{o}$ are given in Fig. 3(a) and (b), respectively, for validating the sensor. Here, the value of resistor $R_{1}$ is chosen based on $1 /\left(R_{1} C_{2}\right)=10^{+6}$ or $10^{+5}$. The abscissa is the dimensionless forcing frequency $\omega / \omega_{n 1}$ defined by the forcing frequency $\omega$ divided by the first natural frequency of the plate $\omega_{n 1}$. The solid curves in the figures are data obtained by using $1 /\left(R_{1} C_{2}\right)=10^{+6}$. Dashed curves are those by $1 /\left(R_{1} C_{2}\right)=10^{+5}$ which corresponding to a large value of $R_{1}$. The curves of output voltage $V_{o}$ in Fig. 3(b) are found having similar trends to the velocity curves shown in Fig. 3(a). This suggests that the sensor is effective. Note that, in Fig. 3(a), two curves for $K=5000, \varsigma_{a}=0.001$, and different values of $K_{s}$ are so close together that they coincide with each other.

<table>
<caption>Table 1<br>Geometric and material parameters.</caption>
<tr>
<th colspan="2">Plate</th>
<th colspan="2">PVDF</th>
</tr>
<tr>
<td>E</td>
<td>$7.1\times 10^{10}\ \text{N/m}^2$</td>
<td>E</td>
<td>$2.0\times 10^{9}\ \text{N/m}^2$</td>
</tr>
<tr>
<td>v</td>
<td>0.33</td>
<td>v</td>
<td>0.29</td>
</tr>
<tr>
<td>$\rho_{m}$</td>
<td>$2700\ \text{kg/m}^3$</td>
<td>$\rho_{p}$</td>
<td>$1780\ \text{kg/m}^3$</td>
</tr>
<tr>
<td>$h_{m}$</td>
<td>$0.006\ \text{m}$</td>
<td>$h_{p}$</td>
<td>$0.001\ \text{m}$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$e_{31}$</td>
<td>$4.76\times 10^{-2}\ \text{C/m}^2$</td>
</tr>
<tr>
<td></td>
<td></td>
<td>$\varepsilon_{33}$</td>
<td>$1.10\times 10^{-10}\ \text{C/V m}$</td>
</tr>
</table>

<table>
<caption>Table 2<br>First three natural frequencies of the odd-modes.</caption>
<tr>
<td>$m_{1}$</td>
<td>$m_{2}$</td>
<td>Aluminum plate<br>$\omega_{n}/\omega_{n1}$</td>
<td>Composite plate<br>$S_{p}$=$0.4\times 0.4$<br>$\omega_{c}/\omega_{n1}$</td>
<td>Composite plate<br>$S_{p}$=$0.6\times 0.6$<br>$\omega_{c}/\omega_{n1}$</td>
<td>Composite plate<br>$S_{p}$=$0.8\times 0.8$<br>$\omega_{c}/\omega_{n1}$</td>
</tr>
<tr>
<td>1</td>
<td>1</td>
<td>1.00</td>
<td>0.905</td>
<td>0.867</td>
<td>0.860</td>
</tr>
<tr>
<td>1</td>
<td>3</td>
<td>5.00</td>
<td>4.705</td>
<td>4.324</td>
<td>4.319</td>
</tr>
<tr>
<td>3</td>
<td>3</td>
<td>9.00</td>
<td>8.845</td>
<td>7.778</td>
<td>7.774</td>
</tr>
</table>

![](./images/811736686420557826_3.jpg)

Fig. 3. Sensor validity (a) velocity at the center of the plate and (b) output voltage $V_{o}$.

![](./images/811736686420557826_4.jpg)

Fig. 4. Frequency responses of the uncontrolled and the controlled beams by using absorbers (a) $1/(R_{1}C_{2})=10^{+5}$ and (b) $1/(R_{1}C_{2})=10^{+6}$.

### 5.2. Varying the system parameters of the absorber

Fig. 4 gives the frequency responses of the uncontrolled aluminum plate, the uncontrolled composite plate, the plate with two passive absorbers, and the plate with an active absorber. The ordinate is the dimensionless amplitude of the center displacement $u_{c}^{*}$ of the plate which is defined as the amplitude of the center displacement divided by the static deflection $F/k_{11}$ with $F$ the force amplitude and $k_{11}$ the (1,1) element of the stiffness matrix. For the composite plate, the resonant peak is found at $\omega_{c1}=0.905\omega_{n1}$ as listed in Table 2. The responses of the plate controlled by two passive absorbers, with $\omega_{a}=\omega_{c1}$ and various $\zeta_{a}$, are obtained when two pieces of piezoelectric sheets connected in parallel along with the closed electric circuit. In Fig. 4(a) the curves by using active absorbers are obtained for $1/(R_{1}C_{2})=10^{+5}$, $K=2000$, $K_{s}=100$, and various damping ratios $\zeta_{a}$ while in Fig. 4(b) for $1/(R_{1}C_{2})=10^{+6}$, $K=5000$, and $K_{s}=100$. Here, higher value of $1/(R_{1}C_{2})$ requires a smaller $R_{1}$ and yields smaller output voltage $V_{o}$ according to its definition given in Section 3.

Generally, the results controlled by active absorbers in Fig. 4(a) show superior reduction than those in Fig. 4(b) and also the wideband characteristic if an appropriate value of $\zeta_{a}$ is chosen. However, as mentioned in [11], velocity feedback may result in instability if a large control gain $K$ is used. The stability of the responses can be examined by checking the eigenvalues or natural frequencies of the dynamic system. In our research, the equations of the composite plate after Galerkin's method and the current Eqs. (13) and (15) are transformed to a state-space form. Then, the eigenvalues are solved. Numerical results show that the choice in Fig. 4(a) with a large $R_{1}$ can easily get into instability. Here, a better

strategy to use is to choose a small $R_1$ and a large $K$ as in Fig. 4(b). The latter case is expected to consume similar amount of input energy compared to the former. This is based on the fact that control gain $K$ is much higher but the sensor output voltage $V_o$ is smaller in the latter case.

For the above reasons, this research focuses on the cases of $1/(R_1C_2)$=$10^{+6}$ and only Fig. 4(b) is discussed. The passive or active absorbers with small $\zeta_a$ can bring an anti-resonance near the frequency $\omega$=$\omega_a$, which is surrounded by two new resonant peaks. Large reduction in the maximal displacement is found usually in company with the appearance of the anti-resonance. From this figure, both types of passive and active absorbers can evidently decrease the maximal displacement compared to that of composite plate. The control responses for $\zeta_a \leq 0.001$ in the active absorber have similar amplitudes and are apparently smaller than those for larger $\zeta_a$ and those by using passive absorbers. Introduction of a small $\zeta_a$ can also smooth out the peaks developed by employing passive or active absorbers. Note that the black dashed line represents data for the aluminum plate. The response looks small because its peak occurs near $\omega/\omega_{n1}$=1 which is out of the range of the plot.

From Fig. 4(b), passive absorbers with $\zeta_a$=0.01 behave better than those with $\zeta_a$=0.001. Fig. 5 then shows the frequency responses by using passive absorbers with $\zeta_a$=0.01 and active absorbers with $\zeta_a$=0.001. Different values of $\omega_a$ are chosen for observing the reduction effect for $\omega_a$ not equal to the natural frequency of the primary system $\omega_{c1}$. Here, $\omega_a$=$0.95\omega_{c1}$ indicates $\omega_a$ is 5% small than the natural frequency $\omega_{c1}$. Compared to the passive absorber, the active absorber shows more robust to the varying of $\omega_a$ and gives more reduction when $\omega_a \neq \omega_{c1}$. For the active absorber with $\omega_a$=$1.05\omega_{c1}$, it is worth to mentioning that an additional small resonance, which is out of the range of this figure, occurs around $\omega/\omega_{n1}$=0.96.

### 5.3. Varying the control gain $K$ and the sensor gain $K_s$

The effect of varying the control gain $K$ of the active absorber is illustrated in Fig. 6 where $K_s$=100. An anti-resonance, surrounded by two peaks, again occurs at $\omega$=$\omega_a$. The increase of the gain $K$ causes a deep anti-resonance and the decrease of the peaks. However $K > 9000$ is not recommended since the response may be unstable.

Fig. 7 presents the results for $K$=5000 and different values of the sensor gain $K_s$. The frequency responses are similar for different $K_s$. Large $K_s$ may also give rise to unstable responses and should be avoided.

### 5.4. Effects on the uncontrolled modes

The previously presented results show the typical characteristic of a dynamic absorber. That is, the absorber works when its natural frequency $\omega_a$ is chosen close to the resonant natural frequency of the primary system to be controlled. Each absorber usually can only attenuate one vibration mode of a continuous system. To evaluate whether the control of mode (1,1) affects other modes, the responses corresponding to modes (1,3) are given in Fig. 8. In these figures, notation "abs1" in the legend indicates using an active absorber for mode (1,1) with $\omega_a$=$\omega_{c1}$=$0.905\omega_{n1}$. On the other hand, notation "abs2" implies $\omega_a$=$4.705\omega_{n1}$ for an absorber designed to control mode (1,3). Some detail data about the maximum displacements of the response curves are also given in Table 3. In Fig. 8, the reduction in displacement by choosing the active absorber designed for mode (1,3) is surly successful. The reduction by using two passive absorbers for mode (1,3) is also satisfactory. Here, no anti-resonance is found and the suppression is not as much as that by using an absorber matching the natural frequency of mode (1,3). It has been found, in Fig. 7, that increasing $K_s$ in the absorber for mode (1,1) cannot influence the results near that resonance. However, one can surprisingly observe that a large value of $K_s$, in the

![](./images/811736686420557826_5.jpg)

Fig. 5. Frequency responses for varying natural frequency $\omega_a$ of the absorber.

![](./images/811736686420557826_6.jpg)

Fig. 6. Frequency responses for varying control gain $K$.

![](./images/811736686420557826_7.jpg)

Fig. 7. Frequency responses for varying sensor gain $K_s$.

active absorber designed for mode (1,1), can actually give considerable decrement in the frequency response near mode (1,3). The increase of control gain $K$ can hardly influence the results. For higher mode (3,3), most discussions for mode (1,3) also valid although the numerical data are not presented.

The responses of mode (1,1), by using the absorber frequency $\omega_a$=4.705$\omega_{n1}$ equal the natural frequency of mode (1,3) of the composite plate, are presented in Fig. 9 to confirm the characteristics discussed previously. The reduction of the maximal displacement, of mode (1,1), can be achieved but not so dramatic compared to that using the absorber for mode (1,1). Similarly, the increase of sensor gain $K_s$ can produce more reduction in the peak values of the response curves (shown in Table 4) as mentioned before.

### 5.5. Current analysis

The amplitudes of the current $i_a$ of the absorber and the current $i_1$ in the sensor are presented in Fig. 10(a) and (b) when the absorber frequency $\omega_a$ is chosen matching $\omega_{c1}$, $\zeta_a$=0.001, $K$=5000, and $K_s$=100 if not specified. In Fig. 10(a), the currents $i_a$ of different absorbers are found having a similar trend except the case with a large $\zeta_a$ ($\zeta_a$=0.01). For $\zeta_a$=0.01, a larger value of maximum $i_a$ is observed but it does not indicate a better vibration reduction. It is interesting to see that all curves coincide at one point near resonance $\omega$=$\omega_{c1}$. When a large $R_1$ is chosen (the case $1/(R_1C_2)$=$10^{+5}$), $i_a$, corresponding to frequencies away from resonant point, increases. Therefore, it can smoothe out the peaks, and enhances the reduction effect. But, one does need to watch the stability of the responses when $R_1$ increased. As discussed in Fig. 7, varying sensor gain $K_s$ has little influence on the results and two curves for $K_s$=100 and 6000 are overlapped in Fig. 10(a).

![](./images/811736686420557826_8.jpg)

Fig. 8. Frequency responses of mode (1,3) by controlling mode (1,1).

Table 3
Maximum displacements of the response curves in Fig. 8.

<table>
<thead>
<tr>
<th>System parameters</th>
<th>Max. displacement</th>
</tr>
</thead>
<tbody>
<tr>
<td>$K$=5000, $K_{s}$=100</td>
<td>1196</td>
</tr>
<tr>
<td>$K$=5000, $K_{s}$=1000</td>
<td>636</td>
</tr>
<tr>
<td>$K$=5000, $K_{s}$=3000</td>
<td>212</td>
</tr>
<tr>
<td>$K$=5000, $K_{s}$=6000</td>
<td>104</td>
</tr>
<tr>
<td>$K$=8000, $K_{s}$=100</td>
<td>1124</td>
</tr>
</tbody>
</table>

![](./images/811736686420557826_9.jpg)

Fig. 9. Frequency responses of mode (1,1) by controlling mode (1,3).

Table 4
Maximum displacements of the response curves in Fig. 9.

<table>
<thead>
<tr>
<th>System parameters</th>
<th>Max. displacement</th>
</tr>
</thead>
<tbody>
<tr>
<td>$K$=5000, $K_{s}$=100</td>
<td>7592</td>
</tr>
<tr>
<td>$K$=5000, $K_{s}$=6000</td>
<td>3614</td>
</tr>
<tr>
<td>$K$=8000, $K_{s}$=100</td>
<td>4803</td>
</tr>
</tbody>
</table>

![](./images/811736686420557826_10.jpg)

Fig. 10. Currents in the absorber and the sensor (a) $i_{a}$ (b) $i_{1}$.

![](./images/811736686420557826_11.jpg)

Fig. 11. Frequency responses for varying the piezoelectric area $S_{P}$.

On the other, the sensor current $i_{1}$ behaves quite different from $i_{a}$. In Fig. 10(b), $i_{1}$ usually has an anti-resonance at the resonant frequency reflecting the characteristic similar to that of the output voltage in Fig. 3(b). A large $K_{s}$ can produce a relatively large $i_{1}$. However, this cannot guarantee more reduction in the vibration.

From detail analysis of the data, one can find that the real parts of terms $\mathrm{d} V_{a} / \mathrm{d} t$ and $\mathrm{d} \phi_{a}^{*}(\tilde{x}, \tilde{y}) / \mathrm{d} t$, in the absorber equation, are almost canceled in the case of $\omega=\omega_{c 1}$. This along with the design of $\omega_{a}^{2}=L_{a} C_{p}$ result in an almost purely imaginary current $i_{a}$ which can destroy most of the external force and give very small displacement of the plate. However, the above mentioned characteristic is no longer valid when the damping in the absorber becomes large. When the forcing frequency is at the left or right peak of the response curve, the current $i_{a}$ of the absorber have an imagery part providing cancellation of part of the external force and a real part current developing addition force to excite the plate motion. At either peak, raising control gain $K$ can increase the imaginary part of $i_{a}$ and decrease the real part. This can result in more reduction in the displacement of the plate. On the other hand, $i_{a}$ is relatively insensitive to change in gain $K_{s}$ owing to the large coefficient of $i_{1}$ in the sensor equation. For such a reason, the peaks result almost identical values for different values of $K_{s}$.

### 5.6. Varying the area of the piezoelectric material

Varying the area of piezoelectric sheets gives shifts of the natural frequencies as listed in Table 2. Fig. 11 illustrates the results by using an active absorber with different sizes of the piezoelectric sheets when the frequency $\omega_{a}$ is set to the

![](./images/811736686420557826_12.jpg)

Fig. 12. Frequency responses due to hysteresis in the piezoelectric material.

corresponding (1,1) natural frequency of the composite plate. This figure shows that larger size of the piezoelectric sheets can result in a sharper anti-resonance. Moreover, increasing the size can also reduce the peak values although the difference is really not so much. Compared to Fig. 5, larger size of piezoelectric material can result in relatively smaller increase in the peak values of the response curves if $\omega_{a}$ is not equal to $\omega_{c 1}$.

### 5.7. Hysteresis of the piezoelectric material

Hysteresis is an exhibit phenomenon of the piezoelectric material. In other words, the equivalent capacitor $\bar{C}_{p}$ of the piezoelectric material may have a complex value instead of real value of $C_{p}$ as defined previously. The notation $R_{i}$ (presented in percentage) is defined as the ratio of imagery part of $\bar{C}_{p}$ to its real part while the absolute value of $\bar{C}_{p}$ still kept the same. In our design of the absorber and the sensor, the chosen values of $L_{a}, R_{a}$, and $C_{2}$ are based on the estimated capacitor $C_{p}=S_{p} \varepsilon_{33} / h_{p}$ despite that the equivalent capacitor of piezoelectric sheet may be actually complex. Fig. 12 demonstrates the results by an active absorber with different $R_{i}$. From the figure, a $\times 5 \% R_{i}$ can lead to about 10 times increase of the peak amplitude compared to the case of no hysteresis. The anti-resonance is no long observed when capacitor hysteresis occurs. For $R_{i}>0 \%$, the plate displacements are generally smaller than those for $R_{i}<0 \%$. From the figure, increased control gain $K$ cannot compensate hysteresis. Although not given here, varying $K_{s}$ has also no effect on the system. Instead, a better strategy for obtaining more reduction is to choose a large size of piezoelectric material.

## 6. Conclusions

The design of an active, piezoelectric absorber is investigated for reducing the vibration of a plate subjected to a harmonic force at the center. Two pieces of piezoelectric sheets, with proper electric circuits, are used for the sensor and the absorber. The piezoelectric sensor sends the velocity information of the plate to the active absorber. The governing equations of the coupled system, the plate, the attached piezoelectric absorber and sensor, are theoretically formulated and solved. The numerical results reveal the potential of using active, piezoelectric absorbers on the vibration control. The presented active absorber can yield effective reduction in plate vibration not only on the controlled mode but also on the uncontrolled resonances. Further parametric studies are also presented. The increase of the control gain $K$ of the active absorber can yield a better reduction effect in the displacements of the plate near the controlled resonant frequency. By using a larger sensor gain $K_{s}$, a better suppression in displacements can usually occur near the uncontrolled resonance.

## Acknowledgment

The authors are grateful for the financial support from the National Science Council under the Grant nos. NSC-91-2212-E008-012 and NSC-92-2212-E008-020.

## References

[1] T.T. Soong, M.C. Constantinou, *Passive and Active Structural Control in Civil Engineering*, Springer-Verlag, New York, 1994.
[2] C.R. Full, E.J. Elliott, P.A. Nelson, *Active Control of Vibration*, Academic Press, London, 1996.

[3] S.S. Rao, Mechanical Vibration, Prentice-Hall, New York, 2003.

[4] N. Jalili, A comparative study and analysis of semi-active vibration control systems, Journal of Vibration and Acoustics—Transactions of the ASME 124 (2002) 593–605.

[5] J. Yuan, Hybrid vibration absorption by zero/pole-assignment, Journal of Vibration and Acoustics—Transactions of the ASME 122 (2000) 466–469.

[6] D. Filipovic, D. Schroder, Control of vibrations in multi-mass systems with locally controlled absorbers, Automatica 37 (2001) 213–220.

[7] N. Jalili, D.W. Knowles IV, Structural vibration control using an active resonator absorber: modeling and control implementation, Smart Materials and Structures 13 (2004) 998–1005.

[8] S. Hill, S.D. Snyder, Design of an adaptive vibration absorber to reduce electrical transformer structural vibration, Journal of Vibration and Acoustics—Transactions of the ASME 124 (2002) 607–611.

[9] P. Bonello, M.J. Brennan, S.J. Elliott, Vibration control using an adaptive tuned vibration absorber with a variable curvature stiffness element, Smart Materials and Structures 14 (2005) 1055–1065.

[10] H.L. Sun, P.Q. Zhang, X.L. Gong, H.B. Chen, A novel kind of active resonator absorber and the simulation on its control effort, Journal of Sound and Vibration 300 (2007) 117–125.

[11] M. Utsumi, Active stabilization of a hybrid vibration absorber subjected to velocity feedback control, AIAA Journal 45 (2007) 786–792.

[12] S.T. Wu, Y.J. Shao, Adaptive vibration control using a virtual-vibration-absorber controller, Journal of Sound and Vibration 305 (2007) 891–903.

[13] D. Filipovic, N. Olgac, Delayed resonator with speed feedback—design and performance analysis, Mechatronics 12 (2002) 393–413.

[14] Y.Y. Zhao, J. Xu, Performance analysis of passive dynamic vibration absorber and semi-active dynamic vibration absorber with delayed feedback, International Journal of Nonlinear Sciences and Numerical Simulation 8 (2007) 607–614.

[15] S.E. Semercigil, D. Lammers, Z. Ying, A new tuned vibration absorber for wide-band excitations, Journal of Sound and Vibration 156 (1992) 445–459.

[16] S.E. Semercigil, F. Collette, D. Huynh, Experiments with tuned absorber—impact damper combination, Journal of Sound and Vibration 256 (2002) 179–188.

[17] H.X. Deng, X.L. Gong1, L.H. Wang, Development of an adaptive tuned vibration absorber with magnetorheological elastomer, Smart Materials and Structures 15 (2006) N111–N116.

[18] N.W. Hagood, A. von Flotow, Damping of structural vibrations with piezoelectric materials and passive electrical networks, Journal of Sound and Vibration 146 (1991) 243–268.

[19] C.H. Park, D.J. Inman, Enhanced piezoelectric shunt design, Shock and Vibration 10 (2003) 127–133.

[20] Y.M. Huang, C.H. Yang, Using piezoelectric dynamic absorbers on noise control of the fuselage, Journal of Chinese Society of Mechanical Engineers 24 (2003) 147–155.

[21] J.J. Dosch, D.J. Inman, E. Garcia, A self-sensing piezoelectric actuator for collocated control, Journal of Intelligent Material Systems and Structures 3 (1992) 166–185.

[22] J.J. Hollkamp, T.F. Starchville, A self-tuning piezoelectric vibration absorber, Journal of Intelligent Material Systems and Structures 5 (1994) 559–566.

[23] Y.M. Huang, H.C. Tseng, Active piezoelectric dynamic absorbers on vibration and noise reductions of the fuselage, Journal of Mechanics 24 (2008) 69–77.

[24] E.H. Anderson, N.W. Hagood, Simultaneous piezoelectric sensing/actuation: analysis and application to controlled structures, Journal of Sound and Vibration 174 (1994) 617–639.

[25] S. Carabelli, A. Tonoli, System properties of flexible structures with self-sensing piezoelectric transducers, Journal of Sound and Vibration 235 (2000) 1–23.

[26] M.S. Tasi, K.W. Wang, On the structure damping characteristics of active piezoelectric actuators with passive shunt, Journal of Sound and Vibration 221 (1999) 1–22.

[27] R.A. Morgan, K.W. Wang, An active–passive piezoelectric absorber for structural vibration control under harmonic excitations with time-varying frequency—part 1: algorithm development and analysis, Journal of Vibration and Acoustics—Transactions of the ASME 124 (2002) 77–83.

[28] R.A. Morgan, K.W. Wang, An active–passive piezoelectric absorber for structural vibration control under harmonic excitations with time-varying frequency—part 2: experimental validation and parametric study, Journal of Vibration and Acoustics—Transactions of the ASME 124 (2002) 84–89.

[29] H.S. Tzou, Piezoelectric Shells: Distributed Sensing and Control of Continua, Kluwer Academic Publishers, New York, 1993.

[30] W. Soedel, Vibrations of Shells and Plates, Marcel Dekker, New York, 1981.