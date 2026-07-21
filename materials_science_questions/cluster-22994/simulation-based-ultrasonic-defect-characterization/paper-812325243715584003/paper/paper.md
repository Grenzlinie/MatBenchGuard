# Approximate Model of Eddy-Current Probe Impedance for Surface-Breaking Flaws

R. E. Beissner¹

Received January 26, 1988

A theoretical model is derived for the prediction of eddy-current probe impedance changes caused by three-dimensional, surface-breaking flaws. Magnetic scalar potential theory and the surface impedance approximation are used to calculate fields on the flaw surface for arbitrary probe position and flaw geometry. Impedance changes are determined by a first-order perturbation calculation, with skin depth being the perturbation parameter. The end result is a relatively simple, three-dimensional model for simulating an eddy-current inspection. Numerical results for rectangular slots include maps of the impedance signals obtained in raster scan patterns and studies of skin-depth effects as a function of probe size, lift-off, and flaw dimensions.

KEY WORDS: Eddy current; nondestructive evaluation; theoretical model; flaw detection.

## 1. INTRODUCTION

In the preceding article⁽¹⁾ we presented a scalar potential theory of the magnetic field of the surface of a flaw. The theory was developed first for the general case, which requires the specification of a boundary condition relating the potential and its normal derivative on the surface. With the assumption that the normal derivative vanishes on the surface, the model was then specialized to the case of a perfect conductor. A further specialization to a surface-breaking flaw in a half-space resulted in a pair of integral equations for the field on the flaw surface.

The final form of the theory of Ref. 1 represents an extension of the earlier scalar potential theory of Auld et al.⁽²⁻⁴⁾ Their model makes use of the perfect conductor approximation and, in addition, involves the assumptions that the field on the opening of the flaw at the half-space surface is known and is symmetric about a line through the center of the flaw opening. The model of Ref. 1 avoids the latter assumptions by solving for the field on the flaw opening in the general asymmetric case. The extended theory is therefore applicable to the general, three-dimensional probe/flaw geometry, while the earlier model is restricted to certain symmetric cases.

Choice of the scalar potential theory for a perfect conductor was based on the success of Auld's model in predicting the impedance of eddy-current probes in the presence of surface-breaking slots and cracks.⁽⁴⁾ It was also motivated by Burke's development of a first-order perturbation treatment⁽⁵⁾ of probe impedance, in which corrections for finite conductivity are estimated to first order in the skin depth. In situations where the approximation is justified, Burke's theory offers a significant simplification because it requires that the fields on the flaw surface be known only for the case of infinite conductivity. The purposes of the present work were, then, to merge the theory of Ref. 1 with Burke's model and to explore applications of the result to impedance predictions for surface-breaking flaws in a conducting half-space.

¹Southwest Research Institute, San Antonio, Texas 78284.

25
0195-9298/88/0600-0025$06.00/0@1988 Plenum Publishing Corporation

Section 2, which is supplemented by the Ap- pendix, contains a detailed derivation of the zero- and first-order terms of Burke's theory in terms of the scalar potential and magnetic field on the surface of a flaw. Sections 3 and 4 contain numerical results for rectangular slots of finite length. The studies included here are examples of applications to asym- metric raster scan simulation, a test of convergence of the boundary element method (BEM) used in Ref.1, and a preliminary investigation of the validity of the theory in the prediction of probe impedance for small surface flaws.

## 2. CALCULATION OF THE PROBE IMPEDANCE
The problem we address is that illustrated in Fig. 1. The space $z<0$ is a conductor containing a surface-breaking flaw of arbitrary shape which is centered at the origin. The eddy-current probe is a coil, also of arbitrary shape, with axis inclined at an angle $\theta$ with respect to the $z$ axis. A general point is specified by its $z$ coordinate and a vector $\vec{\rho}$, which lies in the $x y$ plane. The coil is centered at $\vec{\rho}_{0}, z_{0}$. Although the theory developed in this section applies to coil impedance calculations for this general case, numerical results presented later are for a rectangular slot with a circular coil at $\theta=0$.

![](./images/812325243715584003_1.jpg)

Fig. 1. Geometry for the calculation of flaw response to an eddy-current probe. The flaw is located at the surface of the conducting half-space $z<0$. Coordinates of the center of the probe are $\vec{\rho}_{0}, z_{0}$. In the general theory, the probe axis may be tilted through an angle $\theta$ with respect to the $z$ axis; all calculations presented here are with $\theta=0$.

Following Burke, $^{(5)}$ the coil impedance change due to a flawed conductor, relative to the coil impedance in free space, can be written

$$\Delta Z=\Delta Z_{0}+\Delta Z_{1} \quad(1)$$

where $\Delta Z_{0}$ is the change in $Z$ (relative to $Z$ in free space) due to a perfect conductor, and $\Delta Z_{1}$ is the change in $Z$ (relative to a perfect conductor) due to the finite conductivity of the metal. The exact expres- sions for $\Delta Z_{0}$ and $\Delta Z_{1}$ are

$$\Delta Z_{0}=\frac{1}{I^{2}} \int_{S} \vec{n} \times \vec{E}_{A} \cdot \vec{H} d S\quad(2)$$

and

$$\Delta Z_{1}=\frac{1}{I^{2}} \int_{S} \vec{n} \times \vec{E}_{1} \cdot \vec{H} d S\quad(3)$$

where $S$ is the conductor surface, $\vec{n}$ is the outward normal to $S, \vec{E}_{A}$ and $\vec{E}_{1}$ are, respectively, the electric fields in air and on the surface of the conductor with finite conductivity, and $\vec{H}$ is the magnetic field on the surface of a perfect conductor. To obtain an approximate expression for $\vec{E}_{1}$ to first order in the skin depth $\delta$, we use the surface impedance ap- proximation $^{(6)}$ with time dependence $e^{i \omega t}$,

$$\begin{aligned}
\vec{E}_{1} & \sim \frac{1+i}{2} \omega \mu_{0} \delta \vec{n} × \vec{H}_{1} \\
& \sim \frac{1+i}{2} \omega \mu_{0} \delta \vec{n} × \vec{H}
\end{aligned}\quad(4)$$

In the second approximation, $\vec{H}_{1}$ is replaced by $\vec{H}$, the field on the perfect conductor, because the ex- pression for $\vec{E}_{1}$ is already of first order in $\delta$.

Equations (1), (2), and (3), with the approxima- tion given by Eq. (4), are Burke's formulas for $\Delta Z$ to first order in $\delta$. The simplification realized by this first-order theory is that it involves only fields in air and on the surface of a perfect conductor. This allows use of the scalar potential model for a perfect conductor, which was developed in Ref. 1, rather than a higher-order model for finite conductivity. The remainder of this section contains the mathemat- ical development needed to apply Burke's theory to a

![](./images/812325243715584003_2.jpg)

Fig. 2. Surfaces involved in the impedance integrals. B is the plane surface of the conductor, M is that part of the plane surface removed by the flaw, and C is a closure surface at infinity.

surface-breaking flaw in a half-space, making use of the scalar potential model.

The surface covered by the integrals in Eqs. (2) and (3) is the entire surface enclosing the conductor. With reference to Fig. 2, we have $S=B+F+C$. For the half-space problem, B is the half-space boundary with M, the surface at the mouth of the flaw, removed. If we let $\hat{z}$ be the outward normal to the half-space, then the surface $B+M$ is the infinite plane extending to $\pm\infty$ in the $x$ and $y$ directions. Surface F is that part of the flaw surface in the space $z<0$, and $C$ is the closure surface at infinity.

It is convenient to rewrite each of the integrals in Eqs. (2) and (3) as an integral over the plane $B+M$, plus an integral over the closed flaw surface $F+M$. To do this with Eq. (2), we note that the integral over $C$ vanishes and add and subtract an integral over $M$ to obtain
$$
\begin{aligned}
\Delta Z_{0}=\frac{1}{I^{2}}\left[\int_{B+M} \hat{z} \times \vec{E}_{A} \cdot \vec{H} d S\right. & +\int_{F} \vec{n} \times \vec{E}_{A} \cdot \vec{H} d S \\
& \left.-\int_{M} \hat{z} \times \vec{E}_{A} \cdot \vec{H} d S\right]
\end{aligned}
$$
where we have used $\vec{n}=\hat{z}$ on surfaces $B$ and $M$. If we now redefine $\vec{n}$ to be the outward normal to the flaw volume, and note that $B+M$ is the plane surface at $z=0$, the result is
$$
\Delta Z_{0}=\frac{1}{I^{2}}\left[\int_{\text {plane }} \hat{z} \times \vec{E}_{A} \cdot \vec{H} d S-\int_{F+M} \vec{n} \times \vec{E}_{A} \cdot \vec{H} d S\right]
$$

Recall that $\vec{H}$ is the field on the surface of the perfect conductor. It can be written as the negative gradient of the scalar potential $\Phi$, which is given by the BEM calculation of Ref. 1. Thus, with this substitution and use of the vector relations
$$
\begin{aligned}
\vec{n} \times \vec{E}_{A} \cdot \nabla \Phi & =\vec{n} \cdot \nabla \Phi \times \vec{E}_{A} \\
& =\Phi \vec{n} \cdot \nabla \times \vec{E}_{A}-\vec{n} \cdot \nabla \times\left(\vec{E}_{A} \Phi\right)
\end{aligned}
$$
we obtain
$$
\begin{aligned}
\Delta Z_{0}=-\frac{1}{I^{2}} & {\left[\int_{\text {plane }} \hat{z} \times \vec{E}_{A} \cdot \nabla \Phi d S\right.} \\
& +i \omega \mu_{0} \int_{F+M} \Phi \vec{n} \cdot \vec{H}_{A} d S \\
& \left.+\int_{F+M} \vec{n} \cdot \nabla \times\left(\vec{E}_{A} \Phi\right) d S\right]
\end{aligned}
$$
where use has been made of Maxwell's equation for the curl of $\vec{E}_{A}$. Application of the divergence theorem to the last integral results in a volume integral of the divergence of the curl of $\Phi \vec{E}_{A}$, which is identically zero. Thus
$$
\begin{aligned}
\Delta Z_{0}=-\frac{1}{I^{2}} & {\left[\int_{\text {plane }} \hat{z} \times \vec{E}_{A} \cdot \nabla \Phi d S\right.} \\
& \left.+i \omega \mu_{0} \int_{F+M} \Phi \vec{n} \cdot \vec{H}_{A} d S\right]
\end{aligned}
$$

The integral over the plane is transformed into a Fourier integral as follows:
$$
\begin{aligned}
\int_{\text {plane }} \hat{z} \times \vec{E}_{A} \cdot \nabla \Phi d S & =\int_{\text {plane }} \nabla \Phi \times \hat{z} \cdot \vec{E}_{A} d S \\
& =\int_{\text {plane }}\left[E_{x}^{A} \frac{d \Phi}{d y}-E_{y}^{A} \frac{d \Phi}{d x}\right] d S
\end{aligned}
$$

Integration by parts then gives
$$
\begin{aligned}
\int_{\text {plane }} \hat{z} \times \vec{E}_{A} \cdot \nabla \Phi d S & =\int_{\text {plane }} \Phi \hat{z} \cdot \nabla \times \vec{E}_{A} d S \\
& =-i \omega \mu_{0} \int_{\text {plane }} \Phi \hat{z} \cdot \vec{H}_{A} d S
\end{aligned}
$$

From Eqs. (A1) and (A2) in the Appendix we have
$$
\hat{z} \cdot \vec{H}_{A}=-\frac{1}{2 \pi} \int k \breve{\Phi}_{A}(\vec{k}, 0) e^{i \vec{k} \cdot \vec{\rho}} d^{2} k \quad(6)
$$

where
$$
\tilde{\Phi}_{A}(\vec{k}, z)=\frac{i}{\mu_{0} k}\left[k_{y} a_{x}^{0}(\vec{k}, z)-k_{x} a_{y}^{0}(\vec{k}, z)\right] \quad (7)
$$
and $a_{i}^{0}(\vec{k}, z)$ is the two-dimensional Fourier transform of the $i$ th component of the vector potential in free space. Therefore
$$
\begin{aligned}
\int_{\text {plane }} & z \times \vec{E}_{A} \cdot \nabla \Phi d S \\
& =\frac{i \omega \mu_{0}}{2 \pi} \int k \tilde{\Phi}_{A}(\vec{k}, 0) \int_{\text {plane }} \Phi e^{i \vec{k} \cdot \vec{\rho}} d S d^{2} k \quad(8) \\
& =i \omega \mu_{0} \int k \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}(-\vec{k}, 0) d^{2} k
\end{aligned}
$$
where $\tilde{\Phi}(\vec{k}, 0)$ is the transform of $\Phi(\vec{\rho}, z)$ at $z=0$.

To continue the calculation we need an expression for $\tilde{\Phi}$ in terms of the half-space potential $\Phi_{0}$ and known fields on the flaw surface, both at $z=0$. This is provided by Eq. (14) of Ref. 1, which is
$$
\begin{aligned}
\Phi(\vec{\rho}, 0)= & \Phi_{0}(\vec{\rho}, 0) \\
& -\int_{M} G\left(\vec{\rho}, 0 ; \vec{\rho}^{\prime}, z^{\prime}\right)\left(\frac{d \Phi\left(\vec{\rho}^{\prime}, z^{\prime}\right)}{d z^{\prime}}\right)_{z^{\prime}=0} d S^{\prime}
\end{aligned}
$$

The Fourier transform of this equation is
$$
\tilde{\Phi}(\vec{k}, 0)=\tilde{\Phi}_{0}(\vec{k}, 0)+\frac{1}{2 \pi k} \int_{M} H_{z}(\vec{\rho}, 0) e^{-i \vec{k} \cdot \vec{\rho}} d S \quad(10)
$$
where the transform of the Green's function $G$ has been evaluated using an integral from Ref. 7, and $H_{z}$, the $z$ component of the field on $M$, has been identified as the negative $z$ derivative of $\Phi$.

Substitution in Eq. (8) gives
$$
\begin{aligned}
\int_{\text {plane }} \hat{z} \times & \vec{E}_{A} \cdot \nabla \Phi d S \\
= & i \omega \mu_{0} \int k \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}_{0}(-\vec{k}, 0) d^{2} k \\
& +\frac{i \omega \mu_{0}}{2 \pi} \int \tilde{\Phi}_{A}(\vec{k}, 0) \int_{M} H_{z}(\vec{\rho}, 0) e^{i \vec{k} \cdot \vec{\rho}} d S d^{2} k \quad(11) \\
= & i \omega \mu_{0}\left[2 \int k \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}_{A}(-\vec{k}, 0) d^{2} k\right. \\
& \left.+\int_{M} H_{z}(\vec{\rho}, 0) \Phi_{A}(\vec{\rho}, 0) d S\right]
\end{aligned}
$$
where Eq. (A3) in the Appendix was used in the first term.

The final expression for $\Delta Z_{0}$ is, from Eqs. (5) and (11),
$$
\begin{aligned}
\Delta Z_{0}=-\frac{i \omega \mu_{0}}{I^{2}} & {\left[2 \int k \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}_{A}(-\vec{k}, 0) d^{2} k\right.} \\
& +\int_{M} H_{z}(\vec{\rho}, 0) \Phi_{A}(\vec{\rho}, 0) d S \\
& \left.+\int_{F+M} \Phi(\vec{\rho}, z) \vec{n} \cdot \vec{H}_{A}(\vec{\rho}, z) d S\right] \quad(12)
\end{aligned}
$$

To calculate $\Delta Z_{1}$ we use Eqs. (3) and (4) to obtain
$$
\begin{aligned}
\Delta Z_{1}=\frac{1+i}{2 I^{2}} \omega \mu_{0} \delta & {\left[\int_{\text {plane }}|\vec{H}|^{2} d S\right.} \\
& \left.-\int_{M}|\vec{H}|^{2} d S+\int_{F}|\vec{H}|^{2} d S\right]
\end{aligned}
$$

Because $H_{z}$ vanishes on the $z=0$ plane except on $\mathrm{M}$, the first integral is
$$
\int_{\text {plane }}|\vec{H}|^{2} d S=\int_{\text {plane }}\left[H_{x}^{2}+H_{y}^{2}\right] d S+\int_{M} H_{z}^{2} d S
$$

But
$$
H_{x}=-\frac{d \Phi}{d x}=-\frac{i}{2 \pi} \int k_{x} \tilde{\Phi}(\vec{k}, 0) e^{i \vec{k} \vec{\rho}} d^{2} k
$$
and
$$
\int_{\text {plane }} H_{x}^{2} d S=\int k_{x}^{2} \tilde{\Phi}(\vec{k}, 0) \tilde{\Phi}(-\vec{k}, 0) d^{2} k
$$
with a similar expression for the integral of $H_{y}^{2}$. Therefore,
$$
\int_{\text {plane }}|\vec{H}|^{2} d S=\int k^{2} \tilde{\Phi}(\vec{k}, 0) \tilde{\Phi}(-\vec{k}, 0) d^{2} k+\int_{M} H_{z}^{2} d S
$$

Substitution of Eq. (10) in the first integral produces four terms, one of which involves Eq. (6). The result

is

$$
\begin{aligned}
\int_{\text {plane }} & |\vec{H}|^{2} d S \\
& =4 \int k^{2} \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}_{A}(-\vec{k}, 0) d^{2} k \\
& +2 \int_{M} H_{z}(\vec{\rho}, 0)\left[H_{z}(\vec{\rho}, 0)-2 H_{z}^{A}(\vec{\rho}, 0)\right] d S
\end{aligned}
$$

where $H_{z}^{A}$ is the $z$ component of $\vec{H}_{A}$. The formula for $\Delta Z_{1}$ is, therefore,

$$
\begin{aligned}
\Delta Z_{1}=\frac{1+i}{2 I^{2}} \omega \mu_{0} \delta & {\left[4 \int k^{2} \tilde{\Phi}_{A}(\vec{k}, 0) \tilde{\Phi}_{A}(-\vec{k}, 0) d^{2} k\right.} \\
& +\int_{F}|\vec{H}(\vec{\rho}, z)|^{2} d S \\
& +\int_{M}\left[2 H_{z}(\vec{\rho}, 0)\left\{H_{z}(\vec{\rho}, 0)\right.\right. \\
& \left.\left.\left.-2 H_{z}^{A}(\vec{\rho}, 0)\right\}-|\vec{H}(\vec{\rho}, 0)|^{2}\right] d S\right] \quad(13)
\end{aligned}
$$

Equations (12) and (13) determine, to first order in $\delta$, the impedance change, relative to the impedance in free space, in terms of the magnetic scalar potential and field in free space (subscript $A$) and the potential and field on the surface of a flaw in a perfect conductor. Expressions for the free-space potential and field are developed in the Appendix; the potential and field on the flaw are provided by a BEM calculation, as described in Ref. 1.

In the absence of a flaw, the integrals over $F$ and $M$ vanish, and the impedance change is given by the two $\vec{k}$-space integrals in Eqs. (12) and (13). The impedance change in this case is that associated with a conducting half-space. The terms involving $F$ and $M$ integrals are, therefore, the impedance change caused by the introduction of a flaw in a conducting half-space. It can be shown that, in the special case of a single-turn circular coil, the "no-flaw" form of $\Delta Z_{0}$ reduces to the expression derived by Zaman et al. $^{(8)}$ and verified by Burke, ${ }^{(5)}$ i.e.,

$$
\Delta Z_{0}^{n f}=-i \pi \omega \mu_{0} r_{1} \int_{0}^{\infty} J_{1}^{2}(\xi) e^{-2 \xi z_{0} / r_{1}} d \xi \quad(14)
$$

where the superscript $n f$ refers to "no flaw" and $r_{1}$ is the coil radius.

The expression for $\Delta Z_{0}^{n f}$ points to an important scaling relationship that can be extended to all terms in $\Delta Z_{0}$ and $\Delta Z_{1}$. If we change to dimensionless integration variables by expressing all lengths in terms of some unit length such as $r_{1}$, then it can be shown that $\Delta Z_{0}$ scales in proportion to $r_{1}$, as in Eq. (14), while $\Delta Z_{1}$ is dimensionless. Thus, if we choose to multiply all dimensions (coil radius, lift-off, and flaw dimensions) by a constant factor, then $\Delta Z_{0}$ will change in proportion to that factor, and $\Delta Z_{1}$ will remain the same. We make use of such scaling in the study of skin-depth effects in Section 4.

## 3. APPLICATION TO A RECTANGULAR SLOT

From Ref. 1, the BEM, when applied to a flaw in a perfectly conducting half-space, leads to a system of equations of the form

$$
\sum_{Q} A_{P Q} X_{Q}=X_{P}^{0}
$$

where $X_{P}^{0}$ depends only on the half-space potential on surface $M, A_{P Q}$ depends only on the flaw geometry, and elements of the vector $X_{Q}$ are the potential on $F$ and its normal derivative on $M$. Because the matrix $A$ is independent of the source term $X_{P}^{0}$, the inverse of $A$ determines the field on the flaw surface for arbitrary $X_{P}^{0}$. It is therefore necessary to calculate the inverse of $A$, or equivalently, its LU decomposition, only once to determine the flaw surface field and $\Delta Z$ as a function of probe position and/or configuration.

The procedure is as follows:

(1) define the flaw geometry and compute $A$;
(2) compute the LU decomposition of $A$;
(3) for a fixed probe position and configuration, compute the scalar potential $\Phi_{0}$ at nodes on surface $M$ from Eqs. (A2) and (A3);
(4) solve for $X_{Q}$, which is $\Phi$ on $F$ and $H_{z}$ on $M$;
(5) compute $\Phi$ on $M$ and $\vec{H}$ on $F$ and $M$ from Eqs. (9) and (22) of Ref. 1;
(6) compute the free-space field $\vec{H}_{A}$ and the transformed potential $\tilde{\Phi}_{A}$ from Eqs. (A1) and (7);
(7) compute $\Delta Z_{0}$ and $\Delta Z_{1}$ from Eqs. (12) and (13)-the integrals over $F$ and $M$ are evaluated by introducing BEM shape functions as in Ref. 1;

![](./images/812325243715584003_3.jpg)

Fig. 3. Magnitude of the impedance of a circular coil scanned in a raster pattern. The flaw is a rectangular slot 5.0 mm long, 2.5 mm deep, and 0.5 mm wide, located at the center of the figure, with length oriented in the scan direction. The coil diameter is 6.4 mm, and the area covered by the scan pattern is 12.7×12.7 mm.

(8) for a given skin depth, compute $\Delta Z$; and
(9) repeat steps 3 through 8 for a new probe position or configuration or repeat step 8 to vary the skin depth.

To illustrate the application of the method to a three-dimensional flaw, we have computed $\Delta Z$ for a series of scans parallel to, and at $45^\circ$ to, a rectangular slot. The probe used was a single-turn coil with a 6.4-mm diameter at 1.3-mm lift-off. The skin depth was 0.17 mm and the flaw dimensions were 5 mm (length) by 2.5 mm (depth) by 0.5 mm (width).

Figures 3 and 4 are plots of $|\Delta Z|$ as a function of probe position for the flaw length at 0 and $45^\circ$, respectively, with respect to the scan direction. Each curve is $|\Delta Z|$ along a scan line; curves for adjacent scans are displaced in the vertical direction of the figure to give a pseudo three-dimensional view of $|\Delta Z|$ as a function of probe position in the scan plane. The length of each scan is 12.7 mm and the distance between scans is 0.25 mm. The center of the flaw is at the center of the scan pattern in both figures. Similar data were obtained for the phase of $\Delta Z$ but are not shown here.

![](./images/812325243715584003_4.jpg)

Fig. 4. Magnitude of the coil impedance with the flaw oriented at $45^\circ$ to the scan direction. All other data are the same as in Fig. 3.

Figure 5 illustrates the convergence of the BEM calculation with respect to the nodal point density. In this case we are plotting $|\Delta Z|$ for a single scan directly over the length of the slot. Curves 1, 2, and 3 are, respectively, data obtained by increasing the number of nodes from 218 to 338 to 482. The large difference between curve 1 and curve 2 indicates that the 218-node mesh is too sparse, while the much smaller difference between curve 2 and curve 3 indicates that the result for 482 nodes is approximately stable, i.e., further increases in the number of nodes would probably have little effect on the result. The data shown in Figs. 3 and 4 were generated with the 482-point mesh.

The points illustrated here are that the scalar potential/BEM method is stable with a reasonably small number of nodes and is capable of a fully three-dimensional simulation of an eddy-current raster scan. It is, perhaps, worth noting that the data shown in Figs. 3 and 4 are about what one would expect, based on Auld's interpretation of his calculations for a scan along the flaw length.⁽⁴⁾ When the scan direction is parallel to the flaw, as in Fig. 3, the signal produces a symmetrical pattern with peaks in $|\Delta Z|$ where the coil edges pass over the flaw. In Fig. 4, however, the pattern is asymmetrical and reflects the orientation of the flaw with respect to the scan pattern.

![](./images/812325243715584003_5.jpg)

Fig. 5. Convergence of the boundary element solution. Curves labeled 1, 2, and 3 are, respectively, magnitudes of the coil impedance for scans over the flaw and along its length with 218, 338, and 482 nodes used to define the flaw.

### 4. NUMERICAL STUDY OF SKIN-DEPTH EFFECTS

In the calculations presented in Figs. 3 and 4, the skin depth is about a factor of three smaller than the slot width and much smaller than all other dimensions of the flaw and coil. We would expect, therefore, that in this case $\Delta Z_{1}$ is a small correction to the perfect conductor impedance $\Delta Z_{0}$. In fact, direct calculation gives, at peak signal amplitude, $|\Delta Z_{1}^{f}| /|\Delta Z_{0}^{f}|=0.02$, where the superscript $f$ indicates impedance change caused by the flaw.

There are, however, many situations in eddy-current nondestructive evaluation (NDE) where the skin depth is not small compared to other dimensions, particularly flaw dimensions. In this section we use the parameter $|\Delta Z_{1}^{f}| /|\Delta Z_{0}^{f}|$ as an indicator of the validity of the first-order approximation in some such cases. It should be noted that this $\Delta Z$ ratio test is not conclusive; the only valid test of a truncated perturbation expansion is a comparison with an exact solution. However, exact solutions are not available for cases of interest, and the $\Delta Z$ ratio provides at least a guide to the magnitudes of skin-depth effects, which is why we use it here.

![](./images/812325243715584003_6.jpg)

Fig. 6. Relative magnitude of the skin-depth peturbation term as a function of the scale of the problem. A scale factor of 1.0 correspond to coil diameter 6.4 mm, lift-off 1.3 mm and flaw dimensions $5.0 \times 2.5 \times 0.5$ mm. Smaller scale factors refer to geometries in which all dimensions are reduced by the same factor.

Given the $\Delta Z_{0}$ and $\Delta Z_{1}$ data from the calculations in Figs. 3 and 4, we can use the scaling relationships described in Section 2 to extend the calculations to other situations in which all dimensions are proportional to those in the original calculations. Thus, if we multiply all dimensions by the scale factor 0.1, for example, so that the coil diameter is 0.64 mm, the lift-off is 0.13 mm and the slot is $0.5 \times 0.25 \times 0.05$ mm, then $|\Delta Z_{0}^{f}|$ is multiplied by 0.1 and $|\Delta Z_{1}^{f}|$ is unchanged. The scaled $\Delta Z$ ratio is then 10 times the original ratio, giving $|\Delta Z_{1}^{f}| /|\Delta Z_{0}^{f}|=0.2$. Figure 6 is a plot of the ratio thus obtained as a function of the scale factor.

From Fig. 6 we see that, for the 0.17-mm skin depth used here, the $\Delta Z$ ratio is less than 0.1 for scale factors greater than 0.2. Thus, if the first-order theory is considered acceptable when the fractional first-order correction is less than 0.1, then the theory can be applied when dimensions are greater than 0.2 times the dimensions used in the original calculation, i.e., for coil diameter and lift-off values greater than 1.27 and 0.25 mm, respectively, and flaw dimensions greater than $1.0 \times 0.5 \times 0.1$ mm.

![](./images/812325243715584003_7.jpg)

Fig. 7. Magnitude of the impedance for scans along the lengths of slots of different size. The largest slot, which produces the strongest signal, has dimensions 5.0×2.5×0.5 mm. Smaller slots, which yield successively smaller signals, have lengths of 2.5, 1.0, 0.5, and 0.25 mm, with other dimensions reduced proportionally; the signal from the smallest slot is not visible here.

It is significant that first-order corrections can be small even when the skin depth is not small compared to all other dimensions. In particular, in the example just given, the skin depth is actually greater than the flaw width and only slightly smaller than the lift-off distance, and yet the first-order correction is only 0.1 times the zero-order term. This suggests that the theory may be applicable to flaws that are much smaller than originally anticipated, which could greatly enhance the value of the model for NDE applications.

To explore this possibility further, we performed a series of calculations for different flaw sizes, with the coil diameter (6.4 mm) and lift-off (1.3 mm) held constant. Figure 7 is a plot of $|\Delta Z_{1}^{f}|$ for scans along the lengths of five slots with dimensions from $5.0 \times$ $2.5 \times 0.5$ to $0.25 \times 0.125 \times 0.025$ mm; signal amplitude variations for the smallest flaw are too small to be visible in this figure.

The ratio $|\Delta Z_{1}^{f}|/|\Delta Z_{0}^{f}|$ is given as a function of flaw size in Table I. In this case, flaw dimensions must be greater than about $2.5 \times 1.25 \times 0.25$ mm to obtain a $\Delta Z$ ratio less than 0.1. This differs from the result obtained from Fig. 6, where the coil diameter and lift-off were scaled in proportion to the flaw size.

<table>
<caption>Table I. Impedance Ratio $|f\Delta Z_{1}^{f}|/|\Delta Z_{0}^{f}|$ as a Function of Flaw Size</caption>
<thead>
<tr>
<th>Flaw dimensions (mm)</th>
<th>$\Delta Z$ ratio</th>
</tr>
</thead>
<tbody>
<tr>
<td>$5.0 \times 2.5 \times 0.5$</td>
<td>0.02</td>
</tr>
<tr>
<td>$2.5 \times 1.25 \times 0.25$</td>
<td>0.12</td>
</tr>
<tr>
<td>$1.0 \times 0.5 \times 0.1$</td>
<td>0.32</td>
</tr>
<tr>
<td>$0.5 \times 0.25 \times 0.05$</td>
<td>0.92</td>
</tr>
<tr>
<td>$0.25 \times 0.125 \times 0.025$</td>
<td>1.56</td>
</tr>
</tbody>
</table>

There is, however, no simple answer as to the minimum flaw dimensions one can treat by the first-order perturbation approximation. As indicated here, the magnitude of the first-order correction, and hence the probable validity of the approximation, depends on the lift-off and coil size, as well as on the flaw dimensions.

On the other hand, we can conclude that it is not necessary that all flaw dimensions be much smaller than the skin depth in order for the model to be valid. The two examples considered here show that skin-depth corrections can be of the order of 10% even when the smallest flaw dimension is approximately equal to the skin depth. It is also clear, however, that the theory fails for very small flaws and that another approach is needed in such cases.

## 5. SUMMARY AND CONCLUSIONS

The principal theoretical result of this paper is the pair of equations (12) and (13). These are formulas for the eddy-current probe impedance change, relative to the prove impedance in free space due to a perfect conductor ($\Delta Z_{0}$) and the additional change ($\Delta Z_{1}$) due to finite conductivity, the latter being given to first order in the skin depth. The sum of the impedance changes given by Eqs. (12) and (13) is the first-order perturbation model proposed by Burke,^{(5)} with fields derived from magnetic scalar potential theory.^{(1)} Burke's first-order approximation is based, in turn, on the surface impedance approximation,^{(6)} which requires that fields on the surface be approximately constant over distances of the order of the skin depth. Both the surface impedance approximation and the first-order model restrict the validity of Eq. (13) to small skin-depth situations.

To illustrate possible applications, the theory is used to simulate eddy-current probe raster scans in the vicinity of a surface-breaking, three-dimensional, rectangular slot. The generality of the model is

demonstrated by application to scans at an angle to, as well as along, the symmetry direction of the flaw. In both examples, all distances, including the coil diameter, lift-off, and flaw dimensions, are large compared to the skin depth.

There are many applications of eddy-current NDE where not all dimensions that define the problem are large compared to the skin depth. It is therefore important to inquire as to the limits of validity of the proposed model as the skin depth approaches problem dimensions. Although a thorough examination of this question requires extensive calculations that are beyond the scope of the present study, a few examples provide a partial answer. Two different numerical studies show that the perturbation term can be as small as one-tenth the infinite conductivity term in situations where the smallest flaw dimension is approximately equal to the skin depth. Therefore, the small-skin depth limitation may not be as restrictive as it would at first seem. On the other hand, the numerical studies also indicate that serious error may be involved when the flaw size is much less than the skin depth, in which case one should probably avoid altogether the perfect conductor/perturbation approximations.

## APPENDIX

With reference to Fig. 1, consider first the case of a current-carrying coil of arbitrary shape above a conducting half-space. The general solution of this problem, with time dependence $e^{-i \omega t}$, is given elsewhere. $^{(9)}$ In the development that follows we adopt the same time dependence because the magnetic scalar potential is independent of the choice of the time factor.

From Ref. 9 the electric field in the conductor ($z < 0$) is

$$\vec{E}_{0}=\nabla \times(\hat{z} \Psi)$$

where

$$\Psi(\vec{\rho}, z)=\frac{\omega}{\pi} \int \frac{k_{y} a_{x}^{0}(\vec{k}, 0)-k_{x} a_{y}^{0}(\vec{k}, 0)}{k(\lambda+k)} e^{i \vec{k} \cdot \vec{\rho}+\lambda z} d^{2} k$$

Here $\lambda=\sqrt{k^{2}-i \omega \mu_{0} \sigma}$, and $a_{x}^{0}(\vec{k}, 0)$ and $a_{y}^{0}(\vec{k}, 0)$ are the $x$ and $y$ components of the two-dimensional Fourier transform of the vector potential in free space at $z=0$. From Maxwell's equation for the magnetic field

$$\vec{H}_{0}=\frac{1}{i \omega \mu_{0}} \nabla \times \vec{E}_{0}$$

we find

$$\vec{H}_{0}=\frac{1}{i \omega \mu_{0}}\left[\hat{x} \frac{d^{2} \Psi}{d x d z}+\hat{y} \frac{d^{2} \Psi}{d y d z}-\hat{z}\left(\frac{d^{2} \Psi}{d x^{2}}+\frac{d^{2} \Psi}{d y^{2}}\right)\right]$$

For a perfect conductor we have, at $z=0$,

$$
\begin{aligned}
& \lim _{\sigma \rightarrow \infty}\left(\frac{d^{2} \Psi}{d x^{2}}+\frac{d^{2} \Psi}{d y^{2}}\right) \\
& \quad=-\lim _{\sigma \rightarrow \infty} \frac{\omega}{\pi} \int \frac{k_{y} a_{x}^{0}(\vec{k}, 0)-k_{x} a_{y}^{0}(\vec{k}, 0)}{\lambda+k} k e^{i \vec{k} \cdot \vec{\rho}} d^{2} k \\
& \quad=0
\end{aligned}
$$

in agreement with the boundary condition on $\vec{H}$ at the surface of a perfect conductor. It follows that a scalar potential that satisfies

$$\vec{H}=-\nabla \Phi_{0}$$

at $z=0$ (only) is

$$
\begin{aligned}
\Phi_{0} & =-\frac{1}{i \omega \mu_{0}} \lim _{\sigma \rightarrow \infty}\left(\frac{d \Psi}{d z}\right)_{z=0} \\
& =\frac{i}{\pi \mu_{0}} \int \frac{k_{y} a_{x}^{0}(\vec{k}, 0)-k_{x} a_{y}^{0}(\vec{k}, 0)}{k} e^{i \vec{k} \cdot \vec{\rho}} d^{2} k
\end{aligned}
$$

which applies on the surface of a perfectly conducting half-space for a coil of arbitrary shape located above the surface.

To develop an expression for the scalar potential in free space we start with the Fourier integral representation of the vector potential

$$\vec{A}_{A}(\vec{\rho}, z)=\frac{1}{2 \pi} \int \vec{a}_{0}(\vec{k}, z) e^{i \vec{k} \cdot \vec{\rho}} d^{2} k$$

where the subscript $A$ refers to the field in air. The curl of this expression gives a formula for the magnetic field in terms of the Fourier components $a_{i}^{0}(\vec{k}, z)$. Next, following the development in Ref. 9, we note that the following relationships hold in the space below the coil:

$$\frac{d a_{i}^{0}(\vec{k}, z)}{d z}=k a_{i}^{0}(\vec{k}, z)$$

and

$$
a_{z}^{0}(\vec{k}, z)=-\frac{i}{k}\left[k_{x} a_{x}^{0}(\vec{k}, z)+k_{y} a_{y}^{0}(\vec{k}, z)\right]
$$

A straightforward calculation then gives

$$
\begin{aligned}
\vec{H}_{A}(\vec{\rho}, z)= & -\frac{i}{2 \pi \mu_{0}} \int(i \vec{k}+k \hat{z}) \\
& \cdot\left[\frac{k_{y} a_{x}^{0}(\vec{k}, z)-k_{x} a_{y}^{0}(\vec{k}, z)}{k}\right] e^{i \vec{k} \cdot \vec{\rho}} d^{2} k \\
= & -\nabla \Phi_{A}(\vec{\rho}, z)
\end{aligned}
$$

where

$$
\Phi_{A}(\vec{\rho} f, z)=\frac{i}{2 \pi \mu_{0}} \int \frac{\begin{array}{c}
k_{y} a_{x}^{0}(\vec{k}, z) \\
-k_{x} a_{y}^{0}(\vec{k}, z)
\end{array}}{k} e^{i \vec{k} \cdot \vec{\rho}} d^{2} k \quad(\mathrm{~A} 2)
$$

for $z$ below the coil. In particular, for $z=0$ the half-space and free-space solutions are related by

$$
\Phi(\vec{\rho}, 0)=2 \Phi_{A}(\vec{\rho}, 0) \quad(\mathrm{A} 3)
$$

as might be anticipated from image theory as applied to a perfectly conducting half-space.

For a circular coil we have, from a calculation similar to that in Ref. 9,

$$
\begin{aligned}
& k_{y} a_{x}^{0}(\vec{k}, z)-k_{x} a_{y}^{0}(\vec{k}, z) \\
& \quad=-\frac{k}{k_{x}}\left[k \cos \theta+i k_{y} \sin \theta\right] a_{\eta}^{0}(\vec{k}) e^{-i \vec{k} \cdot \vec{\rho}-k\left(z_{0}-z\right)}
\end{aligned}
$$

where $\vec{\rho}_{0}$ and $z_{0}$ are the coordinates of the center of the coil, $\theta$ is the tilt angle defined in Fig. 1, and $a_{\eta}^{0}(\vec{k})$ is the integral given in Ref. 9. For the special case of a vertical coil $(\theta=0)$ with inner radius $r_{1}$, outer radius $r_{2}$, and height $l$, this reduces to

$$
\begin{aligned}
& k_{y} a_{x}^{0}(\vec{k}, z)-k_{x} a_{y}^{0}(\vec{k}, z) \\
& \quad=\frac{i \mu_{0} I \sinh (k l / 2)}{l\left(r_{2}-r_{1}\right) k^{3}} \\
& \quad \cdot\left[f_{J}\left(k r_{2}\right)-f_{J}\left(k r_{1}\right)\right] e^{-i \vec{k} \cdot \vec{\rho}_{0}-k\left(z_{0}-z\right)}
\end{aligned}
$$

where $I$ is the coil current, and

$$
f_{J}(k r)=\int_{0}^{k r} J_{1}(z) z d z
$$

In the numerical examples presented here we use the result for a coil of infinitesimal thickness $\left(r_{2} \rightarrow r_{1}\right)$ and height $(l \rightarrow 0)$, which is

$$
\begin{aligned}
& k_{y} a_{x}^{0}(\vec{k}, z)-k_{x} a_{y}^{0}(\vec{k}, z) \\
& \quad=\frac{i \mu_{0} I r_{1}}{2} J_{1}\left(k r_{1}\right) e^{-i \vec{k} \cdot \vec{\rho}_{0}-k\left(z_{0}-z\right)}
\end{aligned}
$$

This leads to the following expression for the potential in free space:

$$
\Phi_{A}(\vec{\rho}, z)=-\frac{I r_{1}}{2} \int_{0}^{\infty} J_{1}\left(k r_{1}\right) J_{0}\left(k\left|\vec{\rho}-\vec{\rho}_{0}\right|\right) e^{-k\left(z_{0}-z\right)} d k
$$

## ACKNOWLEDGMENT

This work was sponsored by the Center for Advanced Nondestructive Evaluation, operated by the Ames Laboratory, USDOE, for the Air Force Wright Aeronautical Laboratories/Materials under Contract W-7405-ENG-82 with Iowa State University.

## REFERENCES

1. R. E. Beissner, J. Nondestruct. Eval. 7:15 (1988).
2. F. Muennemann, B. A. Auld, C. M. Fortunko, and S. A. Padget, in D. O. Thompson and D. E. Chimenti (eds.), Review of Progress in Quantitative NDE, Vol. 2 (Plenum, New York, 1983), p. 1501.
3. B. A. Auld, S. Jefferies, J. C. Moulder, and J. Gerlitz, in D. O. Thompson and D. E. Chimenti (eds.), Review of Progress in Quantitative NDE, Vol. 5 (Plenum, New York, 1986), p. 383.
4. B. A. Auld, S. Ayter, F. Muennemann, and M. Riaziat, in D. O. Thompson and D. E. Chimenti (eds.), Review of Progress in Quantitative NDE, Vol. 3 (Plenum, New York, 1984), p. 489.
5. S. K. Burke, J. Phys. D 18:1745 (1985).
6. T. H. Fawzi, M. Taher Ahmed, and P. E. Burke, IEEE Trans. Magn. MAG-21:1835 (1985).
7. I. S. Gradsheteyn and I. M. Ryzhik, Tables of Integrals, Series and Products (Academic Press, New York, 1980), formula 6.565.2.
8. A. J. M. Zaman, S. A. Long, and C. G. Gardner, J. Nonde struct. Eval. 1:183 (1980).
9. R. E. Beissner and M. J. Sablik, J. Appl. Phys. 56:448 (1984).