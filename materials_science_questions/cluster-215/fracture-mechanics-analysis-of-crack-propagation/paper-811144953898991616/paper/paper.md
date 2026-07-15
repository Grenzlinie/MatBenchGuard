# Approximation of mixed mode propagation for an internally pressurized circular crack

Adam K. Schwartzkopff*, Chaoshui Xu, Nouné S. Melkoumian

School of Civil, Environmental and Mining Engineering, Faculty of Engineering, Computer and Mathematical Sciences, The University of Adelaide, SA 5005, Australia

---

## ARTICLE INFO

**Article history:**
Received 27 October 2015
Received in revised form 19 May 2016
Accepted 11 September 2016
Available online 17 September 2016

**Keywords:**
Fracture mechanics
Crack propagation
Stress intensity factors
Hydraulic fracturing

---

## ABSTRACT

Hydraulic fracturing of rocks has various engineering applications. However, there has been limited research into crack propagation prediction by three dimensional analytical techniques. This paper discusses such a technique for predicting the propagation surface of a pressurized circular crack subjected to various loading conditions. The propagation surfaces predicted from the proposed crack front propagation algorithm align well with published results. The suggested method consumes only a fraction of the time needed for a numerical simulation, and therefore it could be useful in assisting the design of hydraulic fracturing operations.

© 2016 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

It is important to predict the propagation paths of pressurized cracks in hydraulic fracturing operations in order to design and optimize the extraction of resources, such as geothermal energy and unconventional oil and gas. Hydraulic fracturing is the primary and most effective method used to increase productivity in these applications [1,2] as it can enhance the rock mass permeability significantly via the resultant fractures.

In an industrial setting, a method is needed for the quick initial assessment of the resultant fracture propagation surface according to the local stress conditions [3]. Establishing such an analytical method has clear advantages including ease of implementation and quick processing times. Numerical methods to address the problem exist [4], however, most of them have been limited to two dimensional [5,6] or highly intensive computational methods [7]. The numerical method proposed by Huang et al. [4] aims to solve a similar problem addressed by this paper. Their numerical method uses a virtual multidimensional internal bond model that is implemented in a three dimensional finite element code.

Rahman et al. [3] developed a two dimensional analytical method to predict the propagation of inclined cracks. Their calculated two dimensional stress intensity factors were close to those obtained from the boundary element analysis using FRANC3D. The propagation paths from their case studies exhibited close alignment with those obtained from FRANC3D and literature. To the knowledge of the authors, the work presented in this paper is the first attempt to extend the method described in Rahman et al. [3] to three dimensional applications.

The key advantage of the three dimensional methods is that they allow determination of the way a pre-existing crack re-orientates in the presence of various in-situ compressive stress regimes. In order to design effective hydraulic fracturing operations, it is important to determine this resultant crack propagation surface since the resultant fracture network

---

* Corresponding author.
E-mail addresses: adam.schwartzkopff@adelaide.edu.au (A.K. Schwartzkopff), chaoshui.xu@adelaide.edu.au (C. Xu), noune.melkoumian@adelaide.edu.au (N.S. Melkoumian).

http://dx.doi.org/10.1016/j.engfracmech.2016.09.002
0013-7944/© 2016 Elsevier Ltd. All rights reserved.

### Nomenclature

| Symbol | Definition |
|--------|------------|
| $a$ | radius or major axis of the elliptical crack (m) |
| $a_{median}$ | median crack increment input for FRANC3D (m) |
| $b$ | minor axis of the elliptical crack (m) |
| $inc$ | predefined incremental length for the proposed analytical method (m) |
| $inc_{FRANC3D}(\varphi)$ | incremental length used in FRANC3D (m) |
| $K_{I(median)}$ | median stress intensity factor for mode I along the crack front (Pa $\sqrt{\text{m}}$) |
| $K_{I}(\varphi)$ | stress intensity factor for mode I (Pa $\sqrt{\text{m}}$) |
| $K_{II}(\varphi)$ | stress intensity factor for mode II (Pa $\sqrt{\text{m}}$) |
| $K_{III}(\varphi)$ | stress intensity factor for mode III (Pa $\sqrt{\text{m}}$) |
| $K_{I(kinked)}(\varphi)$ | kinked crack analytical stress intensity factor for mode I (Pa $\sqrt{\text{m}}$) |
| $K_{II(kinked)}(\varphi)$ | kinked crack analytical stress intensity factor for mode II (Pa $\sqrt{\text{m}}$) |
| $K_{III(kinked)}(\varphi)$ | kinked crack analytical stress intensity factor for mode III (Pa $\sqrt{\text{m}}$) |
| $n$ | power input for calculating the incremental length in FRANC3D |
| $\alpha$ | dip direction (°) |
| $\beta$ | dip angle (°) |
| $\gamma$ | ellipse angle – the direction from the projected dip direction on the crack plane to the major axis of the ellipse (°) |
| $\theta$ | crack front angle – from the normal to the crack front towards the positive $z$ axis direction (°) |
| $\theta_{c}(\varphi)$ | critical crack front angle (°) |
| $\theta_{kink}(\varphi)$ | difference from the radial vector of the current fictitious plane to the kinked radial line (°) |
| $v$ | Poisson's ratio |
| $\sigma_{n(eff)}$ | effective normal stress on the surface of the crack (Pa) |
| $\sigma_{n(external)}$ | normal stress on the surface of the crack (Pa) |
| $\sigma_{t}$ | tensile strength (Pa) |
| $\tau$ | shear stress along the surface of the crack (Pa) |
| $\tau_{eff}$ | effective shear stress along the surface of the crack (Pa) |
| $\varphi$ | crack front angle – from the $x$ axis direction clockwise around the normal vector in the positive $z$ axis direction (°) |
| $\omega$ | shear angle – clockwise around the normal vector in the positive $z$ axis direction (°) |
| $B=(k^{2}-v)E(k)+v{k'}^{2}K(k)$ | constant used to calculate the elliptical crack stress intensity factors |
| $C=(k^{2}+v{k'}^{2})E(k)-v{k'}^{2}K(k)$ | constant used to calculate the elliptical crack stress intensity factors |
| $E(k)=\int_{0}^{\pi/2}\sqrt{1-k^{2}\sin^{2}(\alpha)}d\alpha$ | elliptical integral of the second kind |
| $k=\sqrt{1-\left(\frac{b}{a}\right)^{2}}$ | intermediate eccentricity parameter used to calculate the elliptical crack stress intensity factors |
| $k'=\frac{b}{a}$ | ratio of the minor to the major axis of the elliptical crack |
| $K(k)=\int_{0}^{\pi/2}\frac{d\alpha}{\sqrt{1-k^{2}\sin^{2}(\alpha)}}$ | elliptical integral of the first kind |
| LEFM | linear elastic fracture mechanics |

provides the major permeable pathways for fluid or gas flow. A properly established three dimensional hydraulic fracturing propagation model can assist in the design of the stimulated fracture network to better target the gas zone or geothermal energy resources. Therefore, it is of significant practical importance to develop an efficient and accurate method to predict the three dimensional propagation surfaces resulting from hydraulic fracturing.

To assist the development of such a mixed mode propagation method, the primary problem is simplified to a uniformly pressurized circular crack in an infinite medium subjected to uniform far-field stresses. Kassir and Sih [8] developed an analytical method to evaluate stress intensity factors of all three fracturing modes (opening, shearing and tearing) for a circular and an elliptical planar crack given an arbitrary loading regime based on the linear elastic fracture mechanics (LEFM) theory. It is well documented that these fracturing modes have a combined effect on the resultant crack propagation surface in rocks and other brittle materials [9-12].

In this paper, an analytical approach is developed to approximate the mixed mode propagation of a circular crack, by considering a fictitious equivalent elliptical crack and utilizing the maximum tangential stress criterion [13]. This fictitious elliptical crack assumes the surface and front formed by the propagation process are on the same plane. This assumption proved effective and satisfactory as the predicted propagation surfaces closely align with published results. Another simplification is using the effective normal and shear stresses to calculate the stress intensity factors, which is justified by the close alignment of their resultant values with the numerical results obtained from FRANC3D [14]. The stress tensor for the fictitious planar crack is also comparable to the stress tensor obtained from ABAQUS for the equivalent kinked crack. The finite element

method (FEM) and the boundary element method (BEM) are still slower than the proposed analytical approach, even if the above approximations are used.

In summary, this paper presents an approximate three dimensional analytical method that can solve the crack propagation problem efficiently for an arbitrarily orientated circular internal crack. A planar crack propagation surface and front are assumed to simplify the problem and the maximum tangential stress criterion is used.

## 2. Theory and calculations

### 2.1. Problem setup

Consider a circular crack with a radius of $a$ and orientated with a normal vector $\bar{v}_{n}$, in an infinite ideally brittle rock block subjected to a three dimensional stresses. The crack is internally pressurized by a fluid pressure $P$. The three principal effective stresses: $\sigma_{x}', \sigma_{y}'$ and $\sigma_{z}'$ are orientated along the $x, y$ and $z$ axes, respectively (see Fig. 1).

This is a mixed-mode problem, so opening and shearing modes are considered together when analyzing the propagation of this circular crack. The shearing mode is produced by unequal remote external compressive stresses.

Using spherical coordinates $r, \varphi$, and $\theta$ (see Fig. 3), the stress state at the crack front can be defined by the stress intensity factors. The stress intensity factors are defined as the product of the stress at the crack front at $\theta=0$ and $\sqrt{2 \pi r}$ when $r \rightarrow 0$, i.e., [15]:

$$
\begin{aligned}
K_{I}(\varphi) & =\lim _{r \rightarrow 0} \sigma_{\theta}(r, \varphi, \theta=0) \sqrt{2 \pi r} \\
K_{I I}(\varphi) & =\lim _{r \rightarrow 0} \tau_{r \theta}(r, \varphi, \theta=0) \sqrt{2 \pi r} \\
K_{I I I}(\varphi) & =\lim _{r \rightarrow 0} \tau_{t \theta}(r, \varphi, \theta=0) \sqrt{2 \pi r}
\end{aligned}
\tag{1}
$$

It has been observed that the concept of stress intensity factors, defined above, can predict the propagation of pre-existing macroscopic cracks [13]. These definitions are used below to convert the stress intensity factors of the fictitious planar elliptical crack to the stress intensity factors of the kinked crack. Note that this work is explicitly for an embedded circular crack.

### 2.2. Approximated stress intensity factors for an initially circular planar crack

The stress intensity factors of mode I, II and III for a circular crack can be evaluated using the formulations outlined by Tada et al. [16]. Note, in this paper the shear angle $\omega$, is defined in the crack plane, clockwise around the normal vector in the positive $z$ axis direction, following the system used in FRANC3D. Since Tada et al. [16] defined the shear angle $\omega$, clockwise around the negative $z$ direction, the $K_{I I}(\varphi)$ and $K_{I I I}(\varphi)$ values defined by Tada et al. [16] must be modified accordingly to obtain the stress intensity factors consistent to the definitions used in FRANC3D. The stress intensity factors given in Eq. (2) are considered approximate since the net pressure is used, rather than considering the internal pressure and the external compressive stress separately. Using the notations from Rahman et al. [3], the stress intensity factors can be expressed in the following general forms:

![](./images/811144953898991616_1.jpg)

Fig. 1. Problem formulation.

$$
\begin{aligned}
K_{I}(\varphi) & =2 \sqrt{\frac{a}{\pi}} \sigma_{n(e f f)} \\
K_{I I}(\varphi) & =-\frac{4 \cos (\varphi-\omega)}{(2-v)} \sqrt{\frac{a}{\pi}} \tau_{e f f} \\
K_{I I I}(\varphi) & =\frac{4(1-v) \sin (\varphi-\omega)}{(2-v)} \sqrt{\frac{a}{\pi}} \tau_{e f f}
\end{aligned}
\tag{2}
$$

The normal unit vector $\bar{v}_{n}$, of the crack can be calculated from the dip direction $\alpha$, and dip angle $\beta$, of the crack plane (see Fig. 2), as shown in Eq. (3). The dip direction here is defined as the clockwise rotation angle around the positive $z$ axis from the positive $x$ axis.

$$
\bar{v}_{n}=\left[\begin{array}{c}
l \\
m \\
n
\end{array}\right]=\left[\begin{array}{c}
\cos \left(90^{\circ}-\beta\right) \cos (\alpha) \\
\cos \left(90^{\circ}-\beta\right) \sin (\alpha) \\
\sin \left(\beta-90^{\circ}\right)
\end{array}\right]
\tag{3}
$$

Young and Budynas [17] published expressions to calculate the normal and shear stresses on a plane using the normal vector $(l, m, n)$ for a given external three dimensional stress configuration. Since it is assumed that $\sigma_{x}', \sigma_{y}'$ and $\sigma_{z}'$ are the effective principal stresses, then $\tau_{x y}, \tau_{y z}$ and $\tau_{x z}$ are equal to zero. Therefore, for our considered system, the expressions for normal and shear stresses on a plane can be simplified to the following:

$$
\begin{aligned}
\sigma_{n(\text { external })} & =\sigma_{x}^{\prime} l^{2}+\sigma_{y}^{\prime} m^{2}+\sigma_{z}^{\prime} n^{2} \\
\tau & =\sqrt{\left(\sigma_{x}^{\prime} l\right)^{2}+\left(\sigma_{y}^{\prime} m\right)^{2}+\left(\sigma_{z}^{\prime} n\right)^{2}-\sigma_{n(\text { external })}^{2}}
\end{aligned}
\tag{4}
$$

where the directional cosines of the shear vector are reduced to the following:

$$
\left[\begin{array}{c}
l_{\tau} \\
m_{\tau} \\
n_{\tau}
\end{array}\right]=\frac{1}{\tau}\left[\begin{array}{c}
\left(\sigma_{x}^{\prime}-\sigma_{n(\text { external })}\right) l \\
\left(\sigma_{y}^{\prime}-\sigma_{n(\text { external })}\right) m \\
\left(\sigma_{z}^{\prime}-\sigma_{n(\text { external })}\right) n
\end{array}\right]
\tag{5}
$$

The shear angle $\omega$, is the angle between the shear direction (Eq. (5)) and the vector obtained by projecting the dip direction on the crack plane (Eq. (6)):

$$
\left[\begin{array}{c}
l_{o} \\
m_{o} \\
n_{o}
\end{array}\right]=\left[\begin{array}{c}
\cos (\beta) \cos (\alpha) \\
\cos (\beta) \sin (\alpha) \\
\sin (\beta)
\end{array}\right]
\tag{6}
$$

and can be calculated as:

$$
\omega=\arccos \left(\frac{l_{\tau} l_{o}+m_{\tau} m_{o}+n_{\tau} n_{o}}{\sqrt{l_{\tau}^{2}+m_{\tau}^{2}+n_{\tau}^{2}} \sqrt{l_{o}^{2}+m_{o}^{2}+n_{o}^{2}}}\right)
\tag{7}
$$

The net normal pressure $\left(\sigma_{n(e f f)}\right)$ is calculated as:

![](./images/811144953898991616_2.jpg)

Fig. 2. Net pressure $\sigma_{n(e f f)}$, shear stress $\tau_{e f f}$, shear angle $\omega$, dip direction $\alpha$, dip angle $\beta$, and ellipse angle $\gamma$ definitions.

$$
\sigma_{n(e f f)}=P-\sigma_{n(\text { external })}=P-\left(\sigma_{x}^{\prime} l^{2}+\sigma_{y}^{\prime} m^{2}+\sigma_{z}^{\prime} n^{2}\right)
\tag{8}
$$

Since the shear resistance $\tau_{r}$, for the case of a crack opened by the fluid pressure is very small compared to the shear stress (as crack surfaces are not in contact and there is only small frictional resistance due to fluid viscosity), it can be neglected and therefore the effective shear stress becomes:

$$
\tau_{e f f}=\tau-\tau_{r}=\sqrt{\left(\sigma_{x}^{\prime} l\right)^{2}+\left(\sigma_{y}^{\prime} m\right)^{2}+\left(\sigma_{z}^{\prime} n\right)^{2}-\sigma_{n(\text { external })}^{2}}
\tag{9}
$$

The reason for presenting the normal and shear stresses and shear angle using the normal vector of the arbitrarily orien- tated plane is to provide direct expressions for the stress intensity factors that make the analytical propagation method easier to apply or extend, as discussed below.

### 2.3. Crack propagation directions using maximum tangential stress criterion

The maximum tangential stress criterion, proposed by Erdogan and Sih [13], is utilized to determine the crack propaga- tion direction. This criterion uses the maximum circumferential tangential stress $\sigma_{\theta}$, near the crack front. Hence, the formu lation of Sih and Liebowitz [18] on the stress distribution near a circular (or elliptical) crack is used (see Fig. 3). These stress definitions are normalized by $\sqrt{\pi}$ to be consistent with the definition of the stress intensity factor given in Section 2.1, where higher order terms are omitted because of their negligible influence:

$$
\begin{aligned}
\sigma_{n} & =\frac{K_{I}(\varphi)}{4 \sqrt{2 \pi r}}\left[3 \cos \left(\frac{\theta}{2}\right)+\cos \left(\frac{5 \theta}{2}\right)\right]-\frac{K_{I I}(\varphi)}{4 \sqrt{2 \pi r}}\left[7 \sin \left(\frac{\theta}{2}\right)+\sin \left(\frac{5 \theta}{2}\right)\right] \\
\sigma_{t} & =\frac{K_{I}(\varphi)}{\sqrt{2 \pi r}} 2 v \cos \left(\frac{\theta}{2}\right)-\frac{K_{I I}(\varphi)}{\sqrt{2 \pi r}} 2 v \sin \left(\frac{\theta}{2}\right) \\
\sigma_{z} & =\frac{K_{I}(\varphi)}{4 \sqrt{2 \pi r}}\left[5 \cos \left(\frac{\theta}{2}\right)-\cos \left(\frac{5 \theta}{2}\right)\right]-\frac{K_{I I}(\varphi)}{4 \sqrt{2 \pi r}}\left[\sin \left(\frac{\theta}{2}\right)-\sin \left(\frac{5 \theta}{2}\right)\right] \\
\tau_{t z} & =\frac{K_{I I I}(\varphi)}{\sqrt{2 \pi r}} \cos \left(\frac{\theta}{2}\right) \\
\tau_{z n} & =-\frac{K_{I}(\varphi)}{4 \sqrt{2 \pi r}}\left[\sin \left(\frac{\theta}{2}\right)-\sin \left(\frac{5 \theta}{2}\right)\right]+\frac{K_{I I}(\varphi)}{4 \sqrt{2 \pi r}}\left[3 \cos \left(\frac{\theta}{2}\right)+\cos \left(\frac{5 \theta}{2}\right)\right] \\
\tau_{n t} & =-\frac{K_{I I I}(\varphi)}{\sqrt{2 \pi r}} \sin \left(\frac{\theta}{2}\right)
\end{aligned}
\tag{10}
$$

According to the maximum tangential stress criterion [13], the crack extends from the crack front radially in the direction of the greatest tension.

The local stresses at the crack front can be obtained by converting the stresses in Eq. (10) from a cylindrical coordinate system to a spherical coordinate system using a rotation matrix defined by rotation against the $t$ axis by $\theta$ (as shown in Fig. 3) i.e.:

![](./images/811144953898991616_3.jpg)

Fig. 3. Rectangular stress components in a plane normal to the crack border.

$$
\begin{align}
\sigma_{r} &= \frac{1}{\sqrt{2\pi r}}\left[K_{I}(\varphi)\left(2\cos\left(\frac{\theta}{2}\right)-\cos^{3}\left(\frac{\theta}{2}\right)\right)+K_{II}(\varphi)\left(\sin\left(\frac{\theta}{2}\right)-3\sin^{3}\left(\frac{\theta}{2}\right)\right)\right] \
\sigma_{t} &= \frac{2v}{\sqrt{2\pi r}}\left[K_{I}(\varphi)\cos\left(\frac{\theta}{2}\right)-K_{II}(\varphi)\sin\left(\frac{\theta}{2}\right)\right] \
\sigma_{\theta} &= \frac{\cos^{2}\left(\frac{\theta}{2}\right)}{\sqrt{2\pi r}}\left[K_{I}(\varphi)\cos\left(\frac{\theta}{2}\right)-3K_{II}(\varphi)\sin\left(\frac{\theta}{2}\right)\right] \
\tau_{rt} &= \frac{K_{III}(\varphi)}{\sqrt{2\pi r}}\sin\left(\frac{\theta}{2}\right) \
\tau_{r\theta} &= \frac{\cos\left(\frac{\theta}{2}\right)}{2\sqrt{2\pi r}}\left[K_{I}(\varphi)\sin\theta+K_{II}(\varphi)(3\cos\theta - 1)\right] \
\tau_{t\theta} &= \frac{K_{III}(\varphi)}{\sqrt{2\pi r}}\cos\left(\frac{\theta}{2}\right)
\end{align}
\tag{11}
$$

Therefore $\sigma_{\theta}$ is a maximum when:

$$
\theta_{c}(\varphi)=
\begin{cases}
0^{\circ} & \text{if } K_{II}(\varphi)=0 \
2\arctan\left[\frac{K_{I}(\varphi)\pm\sqrt{K_{I}^{2}(\varphi)+8K_{II}^{2}(\varphi)}}{4K_{II}(\varphi)}\right] & \text{if } K_{II}(\varphi)\neq0
\end{cases}
\tag{12}
$$

Using these critical $\theta$ values, the maximum tangential tensile stress in the crack front can be evaluated using the following expression:

$$
\sigma_{\theta}\sqrt{2\pi r}=\cos^{2}\left(\frac{\theta_{c}(\varphi)}{2}\right)\left[K_{I}(\varphi)\cos\left(\frac{\theta_{c}(\varphi)}{2}\right)-3K_{II}(\varphi)\sin\left(\frac{\theta_{c}(\varphi)}{2}\right)\right]
\tag{13}
$$

### 2.4. Crack front propagation path modelling

In this paper, the focus is placed on developing an approximate but simple, purely analytical method for the evaluation of stress intensity factors for the discussed problem, which is well defined. If the crack propagation increment is constant around the circumference of the crack, the crack front will not be on the same plane after propagation due to different $\theta_{c}$ values at different $\varphi$ points. If the subsequent crack front is not planar, the stress intensity factors for the next step cannot be calculated analytically. Hence, to calculate the stress intensity factors using the analytical solution developed by Kassir and Sih [8], it is necessary to consider a fictitious planar crack front. Note that segmentation from mode III fracturing is not considered with this approach, since the maximum tangential stress criterion is used. Details of the calculation for the fictitious planar crack front used in this work are given in Appendices A and B. Note that the elliptical planar (fictitious) crack front is assumed in this case only to solve the propagation problem analytically. It is acknowledged that in reality, the geometry of actual crack propagation front in each time step may be more complex.

### 2.5. Approximated stress intensity factors for a planar elliptical fictitious crack

The stress intensity factors for a planar elliptical fictitious crack can be approximated by the following expressions as outlined in Tada et al. [16] using the same concept described in Section 2.2.

$$
\begin{align}
K_{I}(\varphi) &= \frac{\sigma_{n(eff)}}{E(k)}\sqrt{\frac{\pi b}{a}}\left[a^{2}\sin^{2}(\varphi)+b^{2}\cos^{2}(\varphi)\right]^{1/4} \
K_{II}(\varphi) &= -\frac{\tau_{eff}k^{2}\sqrt{\pi ab}}{\left[a^{2}\sin^{2}(\varphi)+b^{2}\cos^{2}(\varphi)\right]^{1/4}}\left[\frac{k'}{B}\cos(\omega)\cos(\varphi)+\frac{1}{C}\sin(\omega)\sin(\varphi)\right] \
K_{III}(\varphi) &= \frac{\tau_{eff}k^{2}(1 - v)\sqrt{\pi ab}}{\left[a^{2}\sin^{2}(\varphi)+b^{2}\cos^{2}(\varphi)\right]^{1/4}}\left[\frac{1}{B}\cos(\omega)\sin(\varphi)-\frac{k'}{C}\sin(\omega)\cos(\varphi)\right]
\end{align}
\tag{14}
$$

The concept of a fictitious crack is used where the effective normal stress $\sigma_{n(eff)}$, and shear stress $\tau_{eff}$, are calculated using the dip direction $\alpha$, and dip angle $\beta$, of the plane defined by the crack propagation front.

This concept produces a spatial stress tensor comparable to that obtained from finite element analysis. To compare the result of the fictitious crack with that of the kinked crack from FRANC3D; the analytical stress intensity factors based on the fictitious plane (Eq. (14)) were converted to their kinked coordinate system values by using the spherical coordinate stress system (Eq. (11)). The angles of interest $\theta_{kink}(\varphi)$, are the difference from the radial vector of the current fictitious plane to the kinked radial lines (see Fig. 4 for a graphical representation of the definition).

Note the two definitions for stress intensity factors of the planar fictitious crack and the kinked crack are fundamentally different since the planar fictitious crack does not consider the kink of the propagation surface. To compare the stress tensor

![](./images/811144953898991616_4.jpg)

Fig. 4. Definition of the angle of interest (to convert the fictitious planar stress intensity factors to a kinked coordinate system defined and used in FRANC3D).

of the planar fictitious crack from Eq. (11) with those from finite element analysis (ABAQUS), the stress intensity factors for a kinked crack were assessed (Eq. (15)). The stress components of the numerical and analytical models were compared in Sec- tion 3. Note the angles of interest are generally not zero since the radial directions from planar fictitious crack to the radial vectors of the kinked section of the crack are not aligned.

$$
\begin{aligned}
K_{I(\text {kinked})}(\varphi) & =\sigma_{0} \sqrt{2 \pi r}=\cos ^{2}\left(\frac{\theta_{\text {kink}}(\varphi)}{2}\right)\left[K_{I}(\varphi) \cos \left(\frac{\theta_{\text {kink}}(\varphi)}{2}\right)-3 K_{I I}(\varphi) \sin \left(\frac{\theta_{\text {kink}}(\varphi)}{2}\right)\right] \\
K_{I I(\text {kinked})}(\varphi) & =\tau_{r \theta} \sqrt{2 \pi r}=\frac{1}{2} \cos \left(\frac{\theta_{\text {kink}}(\varphi)}{2}\right)\left[K_{I}(\varphi) \sin \theta_{\text {kink}}(\varphi)+K_{I I}(\varphi)\left(3 \cos \theta_{\text {kink}}(\varphi)-1\right)\right] \\
K_{I I I(\text {kinked})}(\varphi) & =\tau_{t \theta} \sqrt{2 \pi r}=K_{I I I}(\varphi) \cos \left(\frac{\theta_{\text {kink}}(\varphi)}{2}\right)
\end{aligned}
\tag{15}
$$

The pressure $P$, is maintained from the previous step during crack propagation. For details of the propagation surface modelling when the crack front is elliptical, see Appendix B. By using a planar fictitious crack and following the process described, the entire propagation path of the crack can be traced in the three dimensional space.

## 3. Results and discussion

This section presents a comparison study between the published results of Rahman et al. [3] and the current results using the method proposed in this paper.

The geometric and mechanical properties of the model analyzed in this study are shown in Table 1. Note, that the prin- cipal compressive stresses and breakdown pressure used are higher than those for practical hydraulic fracturing operations. These stresses and pressure are chosen to be comparable with the study described in Rahman et al. [3].

The FRANC3D software package is designed to simulate crack growth in materials with a complex geometry, loading con- ditions and crack configuration [14]. In FRANC3D, the stress intensity factors are calculated using the M-integral [19] based on the finite element analysis results obtained from commercial codes such as ABAQUS, NASTRAN or ANSYS. FRANC3D can

<table>
<caption>Table 1<br>Model geometric and mechanical properties.</caption>
<thead>
<tr>
<th>Property type</th>
<th>Properties</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Geometric</td>
<td>Model X dimension</td>
<td>1 m</td>
</tr>
<tr>
<td></td>
<td>Model Y dimension</td>
<td>1 m</td>
</tr>
<tr>
<td></td>
<td>Model Z dimension</td>
<td>1 m</td>
</tr>
<tr>
<td></td>
<td>Initial crack shape</td>
<td>Circular</td>
</tr>
<tr>
<td></td>
<td>Initial crack radius</td>
<td>0.1 m</td>
</tr>
<tr>
<td></td>
<td>Crack position</td>
<td>At the center of the block</td>
</tr>
<tr>
<td></td>
<td>Crack inclination</td>
<td>Case 1 – dip direction = 0° and dip angle = 15°<br>Case 2 – dip direction = 0° and dip angle = 30°<br>Case 3 – dip direction = 0° and dip angle = 45°</td>
</tr>
<tr>
<td>Mechanical</td>
<td>$\sigma'_{x}$</td>
<td>92 MPa</td>
</tr>
<tr>
<td></td>
<td>$\sigma'_{y}$</td>
<td>92 MPa</td>
</tr>
<tr>
<td></td>
<td>$\sigma'_{z}$</td>
<td>63 MPa</td>
</tr>
<tr>
<td></td>
<td>Pressure inside the crack</td>
<td>80 MPa</td>
</tr>
<tr>
<td></td>
<td>Poisson's ratio</td>
<td>0.25</td>
</tr>
<tr>
<td></td>
<td>Elastic modulus</td>
<td>20 GPa</td>
</tr>
</tbody>
</table>

then determine the propagation directions of the crack front using the maximum tangential stress criterion. To determine the subsequent crack front, FRANC3D varies the extension lengths $inc_{FRANC3D}(\varphi)$, using inputs of the median crack increment value $a_{median}$, and a power value $n$. The extension lengths are calculated by multiplying the median crack increment value by the relative change in mode I stress intensity factor with respect to the median mode I stress intensity factor $K_{I(median)}$, to the power of $n$:

$$
inc_{FRANC3D}(\varphi)=a_{median}\left[\frac{K_{I}(\varphi)-K_{I(median)}}{K_{I(median)}}\right]^{n} \tag{16}
$$

This crack front is then smoothed by fitting a polynomial curve (with a user defined order that will give the best fit) to these calculated points. However, this propagation method implemented is problematic, since the crack is initially circular and hence the mode I stress intensity factors do not vary significantly. The lack of change in this stress intensity factor produces almost constant extension lengths in FRANC3D. As a consequence, once the crack kinks, the mesh cannot be generated properly in the first or subsequent steps. In addition, in FRANC3D the increment length $inc_{FRANC3D}(\varphi)$, cannot be below a critical value, as the mesh generator will then have difficulty to generate the mesh rosette required by the program. Consequently, the finite element model cannot be updated and the stress intensity factors and propagation for this particular scenario cannot be predicted. The analytical propagation method proposed does not have these issues. Note however, using an elliptical crack front in the first propagation step in FRANC3D solves the mesh generation issue of the kinked crack, but not the increment length issue.

The stress intensity factors for the pre-existing circular crack of case 3 calculated by FRANC3D and our proposed analytical method (see Eq. (2)), follow each other closely, and overlap, as presented in Fig. 5. The normalized crack front value (horizontal axis) is the circumference of the crack front from the $x$ axis in the positive $\varphi$ direction.

The coefficient of determination ($R^{2}$) regression values between the two methods for mode I, II and III are 0.9999369, 0.999985, and 0.999979, respectively. In addition, the factors generated by the linear regression for mode I, II and III analytical values were 1.015, 1.007 and 1.012, respectively, which demonstrate that the results between the two approaches agree extremely well in this case.

Similarly, the analytical stress intensity factors for the kinked crack in case 3 (Table 1), generated from the fictitious spatial stress tensor, after the application of the conversion above, were compared to the numerical results obtained from FRANC3D, as shown in Fig. 6 (see Section 2.5 for details of this conversion). The coefficient of determination ($R^{2}$) for mode I, II, and III for the kinked crack are 0.99707, 0.98331, and 0.99810, respectively, which indicate that the results from the two methods are closely related. The regression coefficients generated from the linear regression for modes I, II and III were 1.018, 1.572, and 1.498, respectively, suggesting the mode I stress intensity factors agree well, but mode II and III stress intensity factors differ by a proportion. However, the trends of variations from the two methods still align closely with each other (see Fig. 6). As the mode III stress intensity factor will not affect the determination of the propagation path when the maximum tangential stress criterion is used, only mode I and II are needed to predict the propagation direction and surface in the present study. The stress intensity factors for mode I and II from the two methods aligned well with each other along the crack front, especially for $\varphi=0^{\circ}, 90^{\circ}, 180^{\circ}$, and $270^{\circ}$ (see Fig. 6). Therefore, the two methods are expected to produce similar propagation surfaces. It is worthwhile to emphasize that the key purpose of the proposed method is not to evaluate the accurate stress intensity factors for a kinked crack, but to provide a simplified method to assess the overall trend of the propagation surface of an arbitrarily orientated crack.

Using a propagation step size of 10% of the initial crack radius ($inc=0.01$ m), a three dimensional propagation path for 20 steps was computed using the proposed method for case 3 (see Table 1) and the result is shown in Figs. 7 and 8 (note that for clarity the plot scale is exaggerated in $z$ direction in these figures). The increment length of 10% of the initial crack radius was chosen based on the experience of Rahman et al. [3], where a range between 5% and 10% provides reasonably accurate results

![](./images/811144953898991616_5.jpg)

Fig. 5. Comparison of stress intensity factors using the pre-existing crack for case 3 from Table 1 (analytical values and numerical results).

![](./images/811144953898991616_6.jpg)

Fig. 6. Comparison of stress intensity factors using a kinked crack for case 3 from Table 1 (analytical values with regression factors applied and numerical results).

![](./images/811144953898991616_7.jpg)

Fig. 7. Propagation surface for case 3 derived from the analytical method.

![](./images/811144953898991616_8.jpg)

Fig. 8. Cross section along the x axis of propagation surface for case 3 compared with the previous study by Rahman et al. [3].

for their two dimensional model. This increment value could be related or equal to the critical distance [20]. The crack only twists in the vertical direction and realigns to the horizontal plane, because the horizontal stresses are equal and the vertical stress is lower than the horizontal stresses. The angles when the tangential stress is a maximum determine the propagation

surface. Therefore, for this configuration the maximum tangential stress is produced when the crack realigns to the horizontal plane.

The propagation path on the XZ cross section through the middle of the model aligns well with the two dimensional results from the previous study by Rahman et al. [3] (see Fig. 8).

For case 2 in Table 1, using the same settings, a three dimensional propagation surface was calculated using the proposed method and the result is shown in Fig. 9.

Similar to case 3, the propagation profile on XZ cross section closely aligns with the results of the previous two dimensional study [3] (see Fig. 10).

For case 1 in Table 1, the result using the same settings is shown in Fig. 11.

The propagation profile on XZ cross section follows the same trend as that of previous analyses by Rahman et al. [3], but the current analysis produces a slightly higher propagation path (see Fig. 12).

The higher propagation path for case 1 is because the calculation of the stress intensity factors in the proposed method is based on an elliptical crack rather than on a circular or two dimensional linear crack and this is considered to be more realistic to represent the actual situation. Detailed examinations of case 2 (see Fig. 10) and case 3 (see Fig. 8) indicate that both resultant propagation paths defined by the analytical method are higher than the results from Rahman et al. [3], but with little significance. This suggests a trend where the difference is greater for pre-existing cracks with lower dip angles. This can be explained by using the same parameters as for the discussed three cases and assuming 0.1 m as the major axis of ellipse dimensions. When the ratio of minor to major axes of the ellipse becomes less than one, the crack becomes elliptical and the absolute value of $\theta_{c(\text{max})}$ is smaller than the absolute value of $\theta_{c(\text{max})}$ when a circular crack front is assumed. A smaller absolute value of $\theta_{c(\text{max})}$ produces a higher crack propagation path, since this determines how much the crack kinks. Therefore, using stress intensity factors based on elliptical cracks, the absolute value of $\theta_{c(\text{max})}$ is always smaller and hence produces a higher propagation path compared with that when the stress intensity factors based on circular cracks are used, as with Rahman et al. [3]. In other words, if the stress intensity factors based on elliptical cracks are not used, the resultant height of the crack propagation is underestimated, especially for cracks with lower dip angles. The value of $\theta_{c(\text{max})}$ is accurate at the apex of the crack, since the stress intensity factors for a kinked crack are aligned to the analytical values at these points; for example, see Fig. 6 when $\varphi=0^{\circ}$, and $180^{\circ}$. For cracks with higher dip angles, the results from the proposed method align closely with the published results of Rahman et al. [3].

## 4. Conclusions
In this paper, an efficient three dimensional analytical method using the LEFM theory was developed to solve the propagation problem of an arbitrarily orientated pressurized circular crack under different external compressive stresses. The stepwise solution is derived from the concept of a fictitious crack surface and the maximum tangential stress criterion.

The proposed method is efficient and can produce results using a fraction of the time needed for a full finite element or boundary element analysis. However, it is not intended to replace finite element or boundary element analyses, but rather to

![](./images/811144953898991616_9.jpg)

Fig. 9. Propagation surface for case 2 derived from the analytical method.

![](./images/811144953898991616_10.jpg)

Fig. 10. Cross section along the x axis of propagation surface for case 2 compared with the previous study by Rahman et al. [3].

![](./images/811144953898991616_11.jpg)

Fig. 11. Propagation surface for case 1 derived from the analytical method.

![](./images/811144953898991616_12.jpg)

Fig. 12. Cross section along the x axis of propagation surface for case 1 compared with the previous study by Rahman et al. [3].

provide a propagation algorithm that can be used for a quick assessment or in conjunction with these numerical analyses. As demonstrated, the results obtained from the proposed method align closely with published two dimensional studies.

As demonstrated in this study, the transformation from the initial crack geometry to the final crack surface is a complex process and generally involves curved propagation surfaces. It is important to be able to predict these curved propagation surfaces to understand the detailed fracture network developed by hydraulically fracturing the reservoir. The proposed analytical method provides an efficient tool to help to address this problem, though an extension to cover interacting propagating cracks is necessary. In addition, experimental validation of the results produced by the proposed method will need to be conducted.

### Appendix A. Crack propagation path when the initial crack is circular

The subsequent planar propagated crack front can be defined using all the corresponding crack propagation angles $\theta_{c}(\varphi)$ from the previous crack front, even if the propagation process kinks the crack. See Fig. 13 for the geometric description of variables used to model the crack front.

![](./images/811144953898991616_13.jpg)

Fig. 13. Geometric description of variables using circular to elliptical crack fronts.

To generate a planar crack propagation front, a predefined constant increment value inc, is used at two particular points only, which is at $\varphi_{\text{max}}$, corresponding to the maximum mode II stress intensity factor values. These two points are in the shear direction $\omega$, and are $90^{\circ}$ from the point $\varphi_{zero}$, where the stress intensity factor for mode II is zero, i.e.:

$$
\varphi_{\text{max}} = \varphi_{zero} \pm 90^{\circ} \tag{A.1}
$$

According to the maximum tangential stress criterion, at the $\varphi_{zero}$ point, the crack propagation is in the same plane as the initial crack plane, since the mode II stress intensity factor is equal to zero. For a circular crack, stress intensity factors for mode II are equal to zero when the crack front angle is at $90^{\circ}$ from the shear angle $\omega$, i.e.:

$$
\varphi_{zero} = \omega \mp 90^{\circ} \tag{A.2}
$$

Subsequently, $\varphi_{\text{max}}$ and $\theta_{c(\text{max})}$ can be calculated and hence a reference point on the propagated crack front can be determined (see Fig. 14).

For the convenience of calculating the propagation profile, a local crack plane coordinate system is introduced, where $f$ is in the dip direction of the original crack plane, $g$ is perpendicular to $f$ and on the plane of the circular crack, and $h$ is perpendicular to the crack plane. Therefore, the slope of the crack plane after propagation is $h_{\text{max}}/length_{\text{max}}$ in the $\varphi_{\text{max}}$ direction (see Fig. 14), which can be calculated as:

$$
\frac{h_{\text{max}}}{length_{\text{max}}} = \frac{(inc) \sin(\theta_{c(\text{max})})}{a + (inc) \cos(\theta_{c(\text{max})})} \tag{A.3}
$$

The other orthogonal local coordinates $h$ from the crack plane for different $\varphi$ points are calculated as:

$$
h(\varphi) = (inc) \sin(\theta_{c(\text{max})}) \cos(\varphi - \varphi_{\text{max}}) \tag{A.4}
$$

Therefore, the radial coordinates of the crack front after crack propagation can be calculated from the following expression:

$$
length(\varphi) = a + \frac{h(\varphi)}{\tan(\theta_{c}(\varphi))} \ \text{ if } \theta_{c}(\varphi) \neq 0^{\circ} \tag{A.5}
$$

When the crack propagation angle is zero, i.e. $\theta_{c}(\varphi) = 0$, the crack growth is planar but Eq. (A.5) does not evaluate and therefore an approximation is used by averaging the radial coordinates of neighborhood points.

![](./images/811144953898991616_14.jpg)

The radial lengths from the origin to the subsequent propagation front can then be calculated from the following expression:

$$
R(\varphi)=\sqrt{\operatorname{length}^{2}(\varphi)+h^{2}(\varphi)} \tag{A.6}
$$

The local vectors of the subsequent crack front after crack propagation can then be calculated as:

$$
\left[\begin{array}{l}
f(\varphi) \\
g(\varphi) \\
h(\varphi)
\end{array}\right]=\left[\begin{array}{c}
\operatorname{length}(\varphi) \cos (\varphi) \\
\operatorname{length}(\varphi) \sin (\varphi) \\
h(\varphi)
\end{array}\right] \tag{A.7}
$$

These coordinates can be transformed to the coordinates in the global system using the following expressions:

$$
\left[\begin{array}{l}
x(\varphi) \\
y(\varphi) \\
z(\varphi)
\end{array}\right]=\left[\begin{array}{c}
f(\varphi) \cos (\beta) \cos (\alpha)-g(\varphi) \sin (\alpha)-h(\varphi) \cos (\alpha) \sin (\beta) \\
f(\varphi) \cos (\beta) \sin (\alpha)+g(\varphi) \cos (\alpha)-h(\varphi) \sin (\alpha) \sin (\beta) \\
f(\varphi) \sin (\beta)+h(\varphi) \cos (\beta)
\end{array}\right] \tag{A.8}
$$

The normal vector $[x_{normal}, y_{normal}, z_{normal}]$ of the fictitious crack plane after crack propagation is calculated by the cross product of two vectors on the crack plane and then by converting them to the global coordinate system using Eq. (A.8). Using this normal vector, the dip angle $\beta$, and dip direction $\alpha$, for the subsequent fictitious crack plane after crack propagation can be calculated by Eqs. (A.9) and (A.10), respectively:

$$
\beta=
\begin{cases}
0^{\circ} & \text { if } \sqrt{x_{\text {normal }}^{2}+y_{\text {normal }}^{2}}=0 \\
90^{\circ}-\left\|\arctan \left(\frac{z_{\text {normal }}}{\sqrt{x_{\text {normal }}^{2}+y_{\text {normal }}^{2}}}\right)\right\| & \text { if } \sqrt{x_{\text {normal }}^{2}+y_{\text {normal }}^{2}} \neq 0
\end{cases} \tag{A.9}
$$

$$
\alpha=
\begin{cases}
\arctan(y_{normal}/x_{normal}) + Q & \text{if } x_{normal} \neq 0 \\
90^\circ & \text{if } x_{normal}=0 \text{ and } y_{normal} \geqslant 0 \\
270^\circ & \text{if } x_{normal}=0 \text{ and } y_{normal} < 0
\end{cases} \tag{A.10}
$$

$$
\text{where } Q=
\begin{cases}
0^\circ & \text{if } x_{normal} \geqslant 0 \text{ and } y_{normal} \geqslant 0 \\
180^\circ & \text{if } x_{normal} < 0 \text{ and } y_{normal} \geqslant 0 \\
180^\circ & \text{if } x_{normal} < 0 \text{ and } y_{normal} < 0 \\
360^\circ & \text{if } x_{normal} \geqslant 0 \text{ and } y_{normal} < 0
\end{cases}
$$

After the crack propagation, the propagation front on the fictitious crack plane can be approximated by an ellipse where the lengths of major and minor axis are calculated using the following expressions:

$$
\begin{align*}
a &= \max[R(\varphi)] \\
b &= \min[R(\varphi)]
\end{align*} \tag{A.11}
$$

The direction of the major axis of the ellipse, or ellipse angle $\gamma$, in relation to the crack front angle $\varphi$, is obtained from the location of the maximum radial length, i.e. the direction corresponding to the major axis $a$, in Eq. (A.11).

## Appendix B. Crack propagation path for subsequent steps when the fictitious planar crack is elliptical

When calculating the stress intensity factors for an elliptical fictitious planar crack, the angle $\varphi$, is defined as an apparent angle to the point of interest on the crack front from the major axis of the ellipse. The projection onto the actual ellipse, in the $g'$ direction of the intersection of $\varphi$ with the circumscribed circle provides the point of interest. The local coordinates of this point using this apparent angle are $[a\cos(\varphi), b\sin(\varphi), 0]$ (see Fig. 15).

Thus, the actual angle $\varphi_{actual}$, which is measured from the positive $f'$ direction (the direction of the major axis of the ellipse) clockwise against the direction of the positive $h'$ direction (the orthogonal component to $f'$ and $g'$), can be determined from the following relationships (Eq. (B.1)):

$$
\varphi_{actual}=
\begin{cases}
\arctan[b\sin(\varphi)/a\cos(\varphi)] + Q & \text{if } a\cos(\varphi) \neq 0 \\
90^\circ & \text{if } a\cos(\varphi)=0 \text{ and } b\sin(\varphi) \geqslant 0 \\
270^\circ & \text{if } a\cos(\varphi)=0 \text{ and } b\sin(\varphi) < 0
\end{cases} \tag{B.1}
$$

$$
\text{where } Q=
\begin{cases}
0^\circ & \text{if } a\cos(\varphi) \geqslant 0 \text{ and } b\sin(\varphi) \geqslant 0 \\
180^\circ & \text{if } a\cos(\varphi) < 0 \text{ and } b\sin(\varphi) \geqslant 0 \\
180^\circ & \text{if } a\cos(\varphi) < 0 \text{ and } b\sin(\varphi) < 0 \\
360^\circ & \text{if } a\cos(\varphi) \geqslant 0 \text{ and } b\sin(\varphi) < 0
\end{cases}
$$

Similar to the discussions in Appendix A, two apparent angles exist where the stress intensity factors for mode II of an elliptical crack are equal to zero. These two angles are $180^\circ$ apart and the corresponding points have planar crack growth, i.e. $\theta_c(\varphi_{zero})=0$. One of these two angles $\varphi_{zero}$ for an elliptical crack can be calculated by the following expression:

![](./images/811144953898991616_15.jpg)

Fig. 15. Definition of $\varphi$ and $\varphi_{actual}$.

$$
\varphi_{\text {zero }}=
\begin{cases}\arctan \left[\left(-k^{\prime} C\right) / B \tan (\omega)\right]+Q & \text { if } B \tan (\omega) \neq 0 \\ 90^{\circ} & \text { if } B \tan (\omega)=0 \text { and }-k^{\prime} C \geqslant 0 \\ 270^{\circ} & \text { if } B \tan (\omega)=0 \text { and }-k^{\prime} C<0\end{cases}
\tag{B.2}
$$

$$
\text{where } Q=
\begin{cases}0^{\circ} & \text { if } B \tan (\omega) \geqslant 0 \text { and }-k^{\prime} C \geqslant 0 \\ 180^{\circ} & \text { if } B \tan (\omega)<0 \text { and }-k^{\prime} C \geqslant 0 \\ 180^{\circ} & \text { if } B \tan (\omega)<0 \text { and }-k^{\prime} C<0 \\ 360^{\circ} & \text { if } B \tan (\omega) \geqslant 0 \text { and }-k^{\prime} C<0\end{cases}
$$

Eq. (B.2) is derived by determining the angle at which the stress intensity factor for mode II is equal to zero. Since $\varphi_{zero}$ is an apparent angle, it corresponds to a point at the coordinates of $[f', g', h'] = [a \cos(\varphi_{zero}), b \sin(\varphi_{zero}), 0]$ in the current local crack plane coordinate system. The actual $\varphi_{zero}$ angle $\varphi_{actual(zero)}$, can be calculated using the relationship presented in Eq. (B.1). Hence, the reference point on the subsequent crack front can then be determined, where similar to the description given in Appendix A, $\varphi_{actual(max)}$ is $90^{\circ}$ from $\varphi_{actual(zero)}$.

Since the direction of the major axis of the ellipse may not be aligned with the dip direction of the crack plane, the general form of an ellipse must be used, i.e.:

$$
\left[\begin{array}{l}
f(\varphi) \\
g(\varphi) \\
h(\varphi)
\end{array}\right]=\left[\begin{array}{c}
a \cos (\varphi) \cos (\gamma)-b \sin (\varphi) \sin (\gamma) \\
a \cos (\varphi) \sin (\gamma)+b \sin (\varphi) \cos (\gamma) \\
0
\end{array}\right]
\tag{B.3}
$$

where $\varphi$ is defined, in this case, from the major axis of the ellipse direction.

Using the slope $h_{max}/length_{max}$ of the plane after propagation in the $\varphi_{actual(max)}$ direction and projecting the orthogonal coordinates along an inclined plane results in the previous formulation (Eq. (A.3)). The radial coordinates (see Fig. 14) can be calculated from the following expression:

$$
\text { length }(\varphi)=\sqrt{[a \cos (\varphi) \cos (\gamma)-b \sin (\varphi) \sin (\gamma)]^{2}+[a \cos (\varphi) \sin (\gamma)+b \sin (\varphi) \cos (\gamma)]^{2}}+\frac{h(\varphi)}{\tan \left(\theta_{c}(\varphi)\right)} \text { if } \theta_{c}(\varphi) \neq 0^{\circ}
\tag{B.4}
$$

Similarly, when the crack angle is equal to zero, i.e. $\theta_{c}(\varphi)=0^{\circ}$, this expression above does not evaluate and therefore an approximation is used by averaging the radial coordinates of neighborhood points.

The radial length from the origin (see Fig. 14) for the subsequent crack front can be calculated from Eq. (A.6). These subsequent local crack front vectors are calculated from the following formulae:

$$
\left[\begin{array}{l}
f(\varphi) \\
g(\varphi) \\
h(\varphi)
\end{array}\right]=\left[\begin{array}{c}
\text { length }(\varphi) \cos \left(\varphi_{\text {actual }}\right) \\
\text { length }(\varphi) \sin \left(\varphi_{\text {actual }}\right) \\
h(\varphi)
\end{array}\right]
\tag{B.5}
$$

The cross product of two vectors on the subsequent fictitious crack plane after crack propagation is calculated then converted to the global system. This normal vector of the fictitious crack plane is subsequently used to calculate the dip angle and dip direction of this plane using Eqs. (A.9) and (A.10), respectively.

Similar to the process discussed in Appendix A, the subsequent crack front after crack propagation can be approximated by an ellipse where the lengths of the major and minor axis are calculated from Eq. (A.11). The ellipse angle $\gamma$, is then the angle $\varphi$, that makes the longest radial length.

### References

[1] Warpinski N, Teufel L. Influence of geologic discontinuities on hydraulic fracture propagation (includes associated papers 17011 and 17074). J Pet Technol 1987;39:209-20.

[2] Cherny S, Chirkov D, Lapin V, Muranov A, Bannikov D, Miller M, et al. Two-dimensional modeling of the near-wellbore fracture tortuosity effect. Int J Rock Mech Min Sci 2009;46:992-1000.

[3] Rahman MK, Hossain MM, Rahman SS. An analytical method for mixed-mode propagation of pressurized fractures in remotely compressed rocks. Int J Fract 2000;103:243-58.

[4] Huang K, Zhang Z, Ghassemi A. Modeling three-dimensional hydraulic fracture propagation using virtual multidimensional internal bonds. Int J Numer Anal Meth Geomech 2012;37:2021-38.

[5] Zhang X, Jeffrey RG, Bunger AP, Thiercelin M. Initiation and growth of a hydraulic fracture from a circular wellbore. Int J Rock Mech Min Sci 2011;48:984-95.

[6] Dong CY, de Pater CJ. Numerical implementation of displacement discontinuity method and its application in hydraulic fracturing. Comput Methods Appl Mech Eng 2001;191:745-60.

[7] Hossain MM, Rahman MK. Numerical simulation of complex fracture growth during tight reservoir stimulation by hydraulic fracturing. J Pet Sci Eng 2008;60:86-104.

[8] Kassir M, Sih G. Three-dimensional stress distribution around an elliptical crack under arbitrary loadings. J Appl Mech 1966;33:601-11.

[9] Reyes O, Einstein H. Failure mechanisms of fractured rock-a fracture coalescence model. In: 7th International society for rock mechanics congress.

[10] Dyskin AV, Sahouryeh E, Jewell RJ, Joer H, Ustinov KB. Influence of shape and locations of initial 3-D cracks on their growth in uniaxial compression. Eng Fract Mech 2003;70:2115–36.

[11] Yang S-Q, Jing H-W. Strength failure and crack coalescence behavior of brittle sandstone samples containing a single fissure under uniaxial compression. Int J Fract 2011;168:227–50.

[12] Germanovich LN, Salganik RL, Dyskin AV, Lee KK. Mechanisms of brittle fracture of rock with pre-existing cracks in compression. Pure Appl Geophys 1994;143:117–49.

[13] Erdogan F, Sih GC. On the crack extension in plates under plane loading and transverse shear. J Basic Eng 1963;85:519–25.

[14] Wawrzynek P, Carter B, Ingraffea A. Advances in simulation of arbitrary 3D crack growth using FRANC3D NG. In: 12th International conference on fracture, Ottawa.

[15] Rooke DP, Cartwright DJ. Compendium of stress intensity factors; 1976.

[16] Tada H, Paris P, Irwin G. The stress analysis of cracks handbook. 3rd ed. New York: ASME Press; 2000.

[17] Young WC, Budynas RG. Roark's formulas for stress and strain. New York: McGraw-Hill; 2002.

[18] Sih GC, Liebowitz H. Mathematical theories of brittle fracture. In: Liebowitz H, editor. Fracture an advanced treatise. Academic Press, Inc.; 1968. p. 128–51.

[19] Wawrzynek P, Carter B, Banks-Sills L. The M-Integral for computing stress intensity factors in generally anisotropic materials. National Aeronautics and Space Administration, Marshall Space Flight Center; 2005.

[20] Tsuji K, Iwase K, Ando K. An investigation into the location of crack initiation sites in alumina, polycarbonate and mild steel. Fatigue Fract Eng Mater Struct 1999;22:509–17.