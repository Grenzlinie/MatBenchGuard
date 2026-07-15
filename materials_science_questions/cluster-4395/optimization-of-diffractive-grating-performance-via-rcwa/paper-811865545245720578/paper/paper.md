# Homogeneous layer models for high-spatial-frequency dielectric surface-relief gratings: conical diffraction and antireflection designs

David L. Brundrett, Elias N. Glytsis, and Thomas K. Gaylord

The validity of various homogeneous layer models for high-spatial-frequency rectangular-groove (binary) dielectric surface-relief gratings is examined for both nonconical and conical diffraction. In each model the grating is described by a slab of uniaxial material with its optic axis parallel to the grating vector. The ordinary and principal extraordinary indices of the slab depend on the grating filling factor, the substrate and cover refractive indices, and the ratio of the wavelength to the grating period. These indices can be determined by solving two transcendental equations. Higher-order indices are defined as the exact solution to these equations. Second-order indices (second-order dependence on the wavelength-to-period ratio) and first-order indices (no dependence on the wavelength-to-period ratio) are defined by approximate solutions to these equations. Layer models using higher-order and second-order indices are shown to be accurate for high-spatial-frequency gratings, even at wavelength-to-period ratios near the onset of higher-order propagating diffracted waves. These models are used to design example antireflecting gratings on silicon substrates, including designs for conical incidence. All designs are evaluated and optimized by exact rigorous coupled-wave analysis.

## 1. Introduction

Antireflection surfaces are needed for solar cells, detectors, for low-light-level imaging systems, and in situations for which minimizing reflected light is a concern. Antireflection surfaces on any material can be obtained by forming high-spatial-frequency gratings directly on the substrate, $^{1-10}$ thereby avoiding the difficulties of adhesion between dissimilar materials and/or the lack of appropriate materials associated with standard coating technologies. Because of their equivalence to thin films, high-spatial-frequency gratings have also been used as color filters $^{11}$ and as artificial dielectrics. $^{12}$ Furthermore, their uniaxial nature has permitted these gratings to be used as artificial anisotropic dielectrics $^{12,13}$ and as wave-plate-type devices. $^{14}$

In typical grating diffraction applications, the plane of incidence contains the grating vector, and the TE and TM polarizations are decoupled. All diffracted orders lie in the plane of incidence. However, when the orientation of the incident light is such that the plane of incidence does not contain the grating vector, the TE and TM polarizations become coupled and the diffracted wave vectors lie on the surface of a cone (conical diffraction) as shown in Fig. 1(a). In addition, if the grating has a sufficiently small period, then all nonzero-diffracted orders will be cut off as shown in Fig. 1(b). The efficiencies and polarization states of the zero-order forward- and backward-diffracted waves will be a function of both the polar angle of incidence $\theta_{1}$ and the azimuthal angle $\phi$ from the grating vector to the plane of incidence. $^{15}$ Conical diffraction occurs in a variety of applications, including laser scanners and small $f$-number systems.

Rigorous electromagnetic analyses $^{16,17}$ accurately describe the conical diffraction by surface-relief gratings, but the numerical implementation of these analyses may be computationally intensive, limiting their use in design. Fortunately, there are several workable approximate models that may be used to describe diffraction by rectangular-groove (binary) high-spatial-frequency gratings. These models are based on the uniaxial nature of high-spatial-fre-

The authors are with the School of Electrical Engineering and the Microelectronics Research Center, Georgia Institute of Technology, Atlanta, Georgia 30332.
Received 19 March 1993; revised manuscript received 30 July 1993.
0003-6935/94/132695-12\$06.00/0.
© 1994 Optical Society of America.

1 May 1994 / Vol. 33, No. 13 / APPLIED OPTICS 2695

![](./images/811865545245720578_1.jpg)

Fig. 1. Rectangular-groove (binary) gratings at general incidence:
(a) low spatial frequency, (b) high spatial frequency. In both cases
the plane of incidence is rotated through an azimuthal angle $\phi$
from the $x$-$z$ plane. In the high-spatial-frequency case all nonzero-
diffracted orders are cut off.

quency periodic media. $^{18-22}$ By analyzing the homo
geneous layer models of the grating, we find it
possible to gain insight into the behavior of the
zero-order diffraction efficiencies. To assess their
applicability we must determine the accuracy of these
approximate models by comparing them with rigor-
ous theory, for both the nonconical and conical cases.
Furthermore, it is important to understand how the
various models compare with each other.

We demonstrate here that the homogeneous layer
models can give accurate results for a wide range of
grating parameters. The accuracies of the various
models are compared by exact rigorous coupled-wave
analysis (RCWA). $^{23}$ It is shown that homogeneous
layer models can accurately describe the diffracted
fields, including phase shifts and coupling between
orthogonal incident components in the conical diffrac-
tion case. It is also demonstrated that the models
can remain accurate even with the onset of propagat-
ing higher-order waves, making antireflection sur-
faces consisting of simple rectangular-groove geom-
etries at relatively small wavelength-to-period ratios
possible. Procedures are given for the design of
antireflection surfaces that use the layer models, and
it is shown that such a design can be refined by exact
methods such as the RCWA.

Section 2 describes homogeneous layer models for
high-spatial-frequency gratings and their use in anti-
reflection design. Section 3 demonstrates the valid-
ity of the homogeneous layer models for nonconical
incidence. Antireflection designs obtained by use of
the homogeneous layer models are evaluated with the
RCWA as a function of the wavelength-to-period
ratio, filling factor, groove depth, and angle of inci-
dence. Section 4 examines the validity of the homo-
geneous layer models for the conical incidence case,
and a method for antireflection design in the conical
case is presented. Sections 5 and 6 provide a discus-
sion and summary of the results.

## 2. Homogeneous Layer Models
### A. Equivalent Indices

Figure 2 shows a rectangular-groove grating cross
section in region 2, incident and reflected (backward-
diffracted zero-order) waves in region 1, and a trans-
mitted (forward-diffracted zero-order) wave in region
3. Regions 1 and 3 are homogeneous isotropic dielec-
trics with refractive indices $n_1$ and $n_3$. The grating
thickness is $d$, the period is $\Lambda$, the filling factor is $F$,
and the grating vector is $\mathbf{K} = \hat{x}(2\pi)/\Lambda$. The incident
wave vector in region 1 has magnitude $|\mathbf{k}| = n_1(2\pi/\lambda_0)$,
and it makes a polar angle $\theta_1$ with the surface normal.

The conical diffraction geometry is shown in Fig. 1
for high- and low-spatial-frequency gratings. In each
case the plane of incidence is rotated away from the
$x$-$z$ plane through an azimuthal angle $\phi$. The TE
and TM polarization vectors are defined by having the
electric-field vector orthogonal to or contained in the
plane of incidence, respectively.

The low-spatial-frequency grating has its diffracted

![](./images/811865545245720578_2.jpg)

Fig. 2. Dielectric surface-relief grating in cross section. The grating is characterized by the region 1 and region 3 refractive indices $n_1$ and $n_3$, as well as its thickness $d$, its period $\Lambda$, and its filling factor $F$. The incident wave vector makes a polar angle $\theta_1$ from the surface normal, and the wave-vector direction in region 3 is determined by Snell's law.

orders distributed over a cone centered around the $y$ axis, with the $x$ component of the $m$th wave vector given by $k_{xm} = k_{x0} - m2\pi/\Lambda$, where $k_{x0}$ is the $x$ component of the incident wave vector. When linearly polarized light is incident on this grating the light in the diffracted orders will be elliptically polarized in general, and decoupled TE-TM solutions to Maxwell's equations are not possible.

The defining property of the high-spatial-frequency grating is that its wavelength-to-period ratio $(\lambda_0/n_{1,3})/\Lambda$ is large enough so that all nonzerodiffracted orders are cut off. This ratio may be determined by the generalized grating equation. For instance, if the substrate refractive index $n_3$ is larger than the cover index $n_1$, the last order to be cut off is found to be the +1 forward-diffracted order at a wavelength-to-period ratio of $\lambda_0/\Lambda = n_1 \sin \theta_1 \cos \phi + (n_3{}^2 - n_1{}^2 \sin^2 \theta_1 \sin^2 \phi)^{1/2}$. Although only the zeroth orders propagate in the high-spatial-frequency case, coupling between orthogonal field components still occurs and linearly polarized input light again results in elliptically polarized output light.

The homogeneous layer models considered here replace the grating in region 2 with a layer of material of refractive index $n_2$ that is intermediate between $n_1$ and $n_3$, thus reducing the grating analysis problem to a layer analysis problem. That the index $n_2$ is dependent on polarization of the incident light can be seen by using the arguments of Born and Wolf. $^{21}$ At normal incidence, with the incident radiation polarized in the $\hat{y}$ direction $(\mathbf{E} \perp \mathbf{K})$, the electric field in region 2 is tangent to the grating grooves. Because $\lambda_0 \gg \Lambda$ and because $\mathbf{E}$ must be continuous across boundaries, $\mathbf{E}$ is approximately constant across a grating period. The $\mathbf{D}$ fields in region 2, however, will be discontinuous across the boundary because of the change in refractive index. If $\mathbf{D}$ is averaged over a grating period, the result is $\mathbf{D} = \epsilon_0[n_1{}^2(1 - F) + n_3{}^2F]\mathbf{E} = \epsilon_0[\varepsilon_2{}^{\text{TE}}]\mathbf{E}$, where $\epsilon_0$ is the permittivity of free space. Thus the equivalent refractive index for this case is

$$
n_2{}^{\text{TE}} = [\varepsilon_2{}^{\text{TE}}]^{1/2} = [n_1{}^2(1 - F) + n_3{}^2F]^{1/2}. \quad (1)
$$

This is also true for $\phi = 0^\circ$ and $\theta_1 \neq 0^\circ$.

If instead the incident radiation is polarized in the $\hat{x}$ direction $(\mathbf{H} \perp \mathbf{K})$, then a similar argument applies. In this case the $\mathbf{D}$ fields in region 2 are normal to the grating grooves, and they are therefore continuous across the boundary. Again imposing the longwavelength argument, we find that $\mathbf{D}$ is approximately unchanging over a grating period. However, the normal $\mathbf{E}$ fields will not be continuous across the boundary, and applying the same averaging arguments as for the TE case above we see that the equivalent index is

$$
n_2{}^{\text{TM}} = [\varepsilon_2{}^{\text{TM}}]^{1/2} = \left[\frac{(1 - F)}{n_1{}^2} + \frac{F}{n_3{}^2}\right]^{-1/2}. \quad (2)
$$

Finally consider the case of $\phi = 0^\circ$ and $\theta_1 \neq 0^\circ$ but with the electric field polarized in the plane of incidence $(\mathbf{H} \perp \mathbf{K})$. Now $\mathbf{E}$ will have both normal $(\hat{x})$ and tangential $(\hat{z})$ components along the grating walls, and neither of the above values will satisfy the boundary conditions on both field components. The $\hat{z}$ component sees the index given by Eq. (1) and the $\hat{x}$ component sees the index given by Eq. (2). Thus the index for polarization along $\hat{y}$ or $\hat{z}$ is $n_2{}^{\text{TE}}$, whereas the index for polarization along $\hat{x}$ is $n_2{}^{\text{TM}}$. This is the physical model that gives rise to the replacement of the grating by a layer of uniaxial material with its optic axis oriented parallel to the grating vector. The ordinary index is given by Eq. (1), and the extraordinary index is given by Eq. (2); these are the first-order indices, henceforth denoted by $\{n_O{}^{(1)}, n_E{}^{(1)}\}$.

These same solutions have appeared as a limiting case in papers by Rytov, $^{20}$ McPhedran et al., $^{22}$ and Bouchitte and Petit. $^{24}$ Rytov examined plane-wave propagation in an infinite periodic layered medium and arrived at two polarization-dependent transcendental equations for the ordinary and extraordinary equivalent indices of the medium:

$$
\begin{gathered}
(n_1{}^2 - n_O{}^2)^{1/2} \tan\left[\pi \frac{\Lambda}{\lambda_0} (1 - F)(n_1{}^2 - n_O{}^2)^{1/2}\right] \\
\quad = -(n_3{}^2 - n_O{}^2)^{1/2} \tan\left[\pi \frac{\Lambda}{\lambda_0} F(n_3{}^2 - n_O{}^2)^{1/2}\right], \\
\frac{(n_1{}^2 - n_E{}^2)^{1/2}}{n_1{}^2} \tan\left[\pi \frac{\Lambda}{\lambda_0} (1 - F)(n_1{}^2 - n_E{}^2)^{1/2}\right] \\
\quad = \frac{-(n_3{}^2 - n_E{}^2)^{1/2}}{n_3{}^2} \tan\left[\pi \frac{\Lambda}{\lambda_0} F(n_3{}^2 - n_E{}^2)^{1/2}\right]. \quad (3)
\end{gathered}
$$

Equation (3) can be shown to be equivalent to the eigenmode equations of Botten et al. $^{25}$ at normal incidence, on which the results of Ref. 22 are based. Solutions to these transcendental equations will be

termed higher-order indices and will be denoted $\{n_O^{(H)}, n_E^{(H)}\}$. The tangent terms in Eq. (3) may be expanded in the series $\tan x = x + x^3/3 + \cdots$, which may then be truncated for sufficiently small values of $\Lambda/\lambda_0$. If the truncation takes place at the first-order terms then the quantity $\Lambda/\lambda_0$ divides out, and the solutions for $n_O$ and $n_E$ are the first-order indices $\{n_O^{(1)}, n_E^{(1)}\}$ given by Eqs. (1) and (2). Truncation at the cubic terms yields higher-order polynomials in $n_O$ and $n_E$, which may fail to have real roots for large values of the tangent arguments. Rytov gave the following modified second-order solutions, denoted $\{n_O^{(2)}, n_E^{(2)}\}$:

$$
n_O^{(2)} = \left\{ \left[n_O^{(1)}\right]^2 + \frac{1}{3} \left[ \pi \frac{\Lambda}{\lambda_0} F(1-F) \right]^2 \left(n_3^2 - n_1^2\right)^2 \right\}^{1/2}
$$

$$
\begin{aligned}
n_E^{(2)} &= \left\{ \left[n_E^{(1)}\right]^2 + \frac{1}{3} \left[ \pi \frac{\Lambda}{\lambda_0} F(1-F) \right]^2 \left( \frac{1}{n_3^2} - \frac{1}{n_1^2} \right)^2 \right. \\
&\quad \left. \times \left[n_E^{(1)}\right]^6 \left[n_O^{(1)}\right]^2 \right\}^{1/2}. \tag{4}
\end{aligned}
$$

The use of these second-order solutions in antireflection design has been extensively treated in a recent paper by Raguin and Morris.⁹

Because the filling factor $F$ is a parameter assumed to be under the designer's control, the simple dependence of the first-order indices on $F$ makes their use with the homogeneous layer in the modeling-design process particularly attractive. However, as the wavelength-to-period ratio decreases more terms are needed in the series to approximate the tangents in Eq. (3), and the use of the second-order and higher-order indices in the homogeneous layer model is anticipated to yield more accurate predictions of the grating's behavior. Figure 3(a) shows the three different sets of indices as a function of filling factor at a constant wavelength-to-period ratio of 5.0 for a silicon grating in air illuminated by 1.5-$\mu$m radiation. At this wavelength the refractive index for silicon is approximately 3.5, whereas the extinction coefficient is negligible. These values of $\lambda_0$ and $n_3$ will be used throughout the remainder of this paper. It is seen from Fig. 3(a) that all the indices converge to 1.0 ($n_1$) for $F \to 0$ and to 3.5 ($n_3$) for $F \to 1$. Figure 3(b) plots the same indices at a constant filling factor of $F = 0.5$ while varying the wavelength-to-period ratio from 1.0 to 5.0. It can be seen from Fig. 3(b) that both $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ approach the $\{n_O^{(1)}, n_E^{(1)}\}$ values as $\lambda_0/\Lambda$ approaches infinity. However, it can also be seen that $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ both deviate considerably from $\{n_O^{(1)}, n_E^{(1)}\}$ as $\lambda_0/\Lambda$ decreases. Furthermore, the curve for $n_O^{(2)}$ in Fig. 3(b) exceeds $n_3$ as $\lambda_0/\Lambda$ approaches 2. However, the smallest wavelength-to-period ratio possible for this substrate without permitting the $\pm 1$ forward-diffracted orders to propagate is 3.5, at which point the value for $n_O^{(2)}$ still lies between $n_1$ and $n_3$. For large wavelength-to-period ratios (e.g., $\lambda_0/\Lambda$ greater than $\sim$15), the higher-order indices are essentially the same as the first-order indices. However, it is seen in Fig. 3(b) that significant differences can exist among the three sets of indices when the wavelength-to-period ratio becomes small. For intermediate wavelength-to-period ratios (e.g., $5 < \lambda_0/\Lambda < 15$), $\{n_O^{(2)}, n_E^{(2)}\}$ very closely approximates $\{n_O^{(H)}, n_E^{(H)}\}$.

![](./images/811865545245720578_3.jpg)

Fig. 3. Equivalent indices of the homogeneous layer model for a silicon grating ($n_3 = 3.5$) in air ($n_1 = 1$). (a) Indices are plotted as a function of $F$ at a constant wavelength-to-period ratio of $\lambda_0/\Lambda =$ 5.0. For $F = 0$ all indices equal $n_1$, whereas for $F = 1$ all indices equal $n_3$. The first-order indices can deviate significantly from $\{n_O^{(2)}, n_E^{(2)}\}$ and $\{n_O^{(H)}, n_E^{(H)}\}$. (b) Indices are plotted as a function of $\lambda_0/\Lambda$ at a constant filling factor of 0.5. Note that $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ both fall toward $\{n_O^{(1)}, n_E^{(1)}\}$ as $\lambda_0/\Lambda$ gets large.

From Fig. 3(b) we see that appropriate equivalent indices may be chosen based on the desired wavelength-to-period ratio. Once this is done the application of the homogeneous layer model is straightforward. The grating in region 2 is replaced by a slab of uniaxial material with a thickness equal to the groove depth and with its optic axis parallel to the grating vector. A single anisotropic layer surrounded by

isotropic media is easily analyzed by matrix meth- ods. $^{26,27}$ When $\phi \neq 0^{\circ}$ the plane of incidence does not contain the optic axis, and coupling between orthogo- nal components of the incident field will occur. Thus for linearly polarized light incident on the homogeneous layer, the refracted and reflected light will be elliptically polarized in general, just as in the conical diffraction case.

### B. Antireflection Properties
The antireflection characteristics of high-spatial- frequency gratings are well documented in the litera- ture. $^{1-10}$ Because the effective indices of the grating lie between those of the incident and substrate media and are a function of the filling factor $F$, it is possible to design a grating such that, given the proper groove depth, the antireflection condition is fulfilled. This may be accomplished analytically in the $\phi=0^{\circ}$ and $\phi=90^{\circ}$ (decoupled) planes of incidence. As a way to show this, the problem may be cast in terms of a polarization-dependent effective index $N$, for propaga- tion normal to the interface. This is analogous to the wave-impedance-surface-impedance technique used to analyze the behavior of plane waves at planar interfaces. $^{28,29}$ In the decoupled planes of incidence, the effective indices for each region are defined by the magnitude of the ratio of the transverse field compo- nents in the region $(H_{trans}/E_{trans})$ divided by the intrinsic admittance of free space. The effective indices for the isotropic regions 1 and 3 can be shown to have the form $N_{m}^{TE}=n_{m} \cos \theta_{m}$ and $N_{m}^{TM}=$ $n_{m}/\cos \theta_{m}$, where the subscript $m$ denotes the region. These expressions also hold in region 2 for $\phi=90^{\circ}$ with TE and TM polarization, and for $\phi=0^{\circ}$ with TE polarization. However, in region 2 for $\phi=0^{\circ}$ with TM polarization, $n_{2}$ depends on $\theta_{2}$. Solving Max well's equations for the ratio of transverse field components in this case yields an effective index of the form $N_{2}^{TM}=n_{E}^{2}/n_{2} \cos \theta_{2}$. Note that this is more accurate than the $N^{TM}$ expression introduced in Ref. 4.

Using appropriate expressions for the effective indices of each region, we see that the amplitude reflectance for a single layer embedded between two infinite media has the familiar form

$$
r = (N_1 - N_{\text{in}})/(N_1 + N_{\text{in}}), \tag{5}
$$

where the effective index $N_{\text{in}}$ for propagation in the $\hat{z}$ direction is given by

$$
N_{\text{in}} = N_2 \frac{(N_3 + jN_2 \tan \Delta)}{(N_2 + jN_3 \tan \Delta)}, \tag{6}
$$

and $\Delta = k_0 d n_2 \cos \theta_2$. For antireflection $N_1 = N_{\text{in}}$ is required. To achieve this we must satisfy the follow- ing two conditions. First, the antireflection (AR) thickness of the single layer, $d_{\text{AR}}$, must satisfy

$$
d_{\text{AR}} = \frac{\lambda_0}{4n_2 \cos \theta_2} p, \quad p = 1, 3, 5, \dots \tag{7}
$$

If $d$ takes on one of these values then the expression for $N_{\text{in}}$ becomes $N_{\text{in}} = N_2{}^2/N_3$, which leads to the second antireflection condition:

$$
N_2 = (N_1 N_3)^{1/2}. \tag{8}
$$

The quantity $N_2$ in Eq. (8) contains both $\cos \theta_2$ and $n_2$; $\theta_2$ depends on $\theta_1$ by means of phase matching at $z=0$, whereas $n_2$ implicitly depends on the polariza- tion of the incident radiation and on the quantities $F$, $n_1$, $n_3$, $\Lambda$, and $\lambda_0$. By choosing the thickness of the layer (depth of the grooves) to satisfy Eq. (7) and by specifying the angle of incidence, the incident and substrate indices, and the wavelength-to-period ratio desired, we find it possible to solve Eq. (8) for the antireflection filling factor $F_{\text{AR}}$. If the definitions for $\{n_O^{(1)}, n_E^{(1)}\}$ are used, analytic expressions may be derived for the antireflection filling factor $F_{\text{AR}}$ (see Appendix A). As has previously been shown in the $\phi = 0^{\circ}$ plane, $^{5,22}$ the success of such first-order antireflection designs depends on the wavelength-to- period ratio being large, particularly for TM polariza- tion. Greatly improved designs are possible by using $\{n_O^{(H)}, n_E^{(H)}\}$ or $\{n_O^{(2)}, n_E^{(2)}\}$. Although the expres- sions for $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ are too compli- cated to yield closed-form expressions for $F_{\text{AR}}$, a simple root-finding algorithm may be employed along with the above analysis to determine $F_{\text{AR}}$ and $d_{\text{AR}}$ for any specified wavelength-to-period ratio, provided that this ratio is chosen large enough to ensure the cutoff of all nonzero-diffracted orders.

Solutions for $F_{\text{AR}}$ in the four special cases are plotted as a function of incidence angle in Figs. 4(a) and 4(b) for the silicon grating in air ($n_3 = 3.5$ at $\lambda_0 = 1.5$ $\mu$m), using $\{n_O^{(1)}, n_E^{(1)}\}$, $\{n_O^{(2)}, n_E^{(2)}\}$, and $\{n_O^{(H)}, n_E^{(H)}\}$. Note in Fig. 4(b), TM polarization, the physically satisfying result that the antireflection filling factor may take on values of 1 or 0 at the Brewster angle for the substrate ($\theta_B = 74.05^{\circ}$). Either value corresponds to a planar interface for which the Brewster angle immediately satisfies the antireflection condition. The corresponding groove depths $d_{\text{AR}}$ are plotted in Fig. 4(c), where it is seen that $d_{\text{AR}}$ for the TE cases is the same regardless of the indices used. As can be seen from Eq. (8), this is due to $n_2 \cos \theta_2$ being set equal to the same constant for each model. This is also the case for TM polariza- tion in the $\phi = 90^{\circ}$ plane, where $n_2 = n_O$ for all values of $\theta_2$. Only in the case of TM polarization in the $\phi =$ $0^{\circ}$ plane, where $n_2$ becomes a function of $\theta_2$, is there any difference between the $d_{\text{AR}}$ values for the three different models. As we can see from Fig. 4(c), the difference is exceedingly small. The discontinuity in the $d_{\text{AR}}$ curves for the TM cases occurs at the Brewster angle, where $F_{\text{AR}}$ jumps from 1 to 0 and $n_2$ jumps from $n_3$ to $n_1$.

It can be seen in Figs. 4(a)-4(c) that $F_{\text{AR}}$ and $d_{\text{AR}}$ both vary slowly for each of the four cases plotted over a range of incidence angles from $0^{\circ} \leq \theta_1 \leq 50^{\circ}$. If a grating is designed to be antireflecting at an intermediate angle of incidence, say $30^{\circ}$, one might expect the grating's reflectance to remain relatively

![](./images/811865545245720578_4.jpg)

Fig. 4. Antireflection filling factors $F_{\text{AR}}$ for (a) TE polarization and (b) TM polarization, (c) antireflection groove depths $d_{\text{AR}}$ plotted as a function of angle of incidence in the decoupled planes of incidence. The Brewster angle is evident in (b) and (c). The antireflection filling factors and groove depths both vary slowly over the range $0^0 < \theta_1 < 50^0$.

low over this whole range. For larger values of $\theta_1$ the reflectance would be expected to rise more rap- idly, with the TM designs performing more poorly than the TE designs as the Brewster angle is ap- proached.

### 3. Nonconical Incidence
As a first example of the results that may be expected from the use of the homogeneous layer models, again consider the case of the silicon grating for use at 1.5 $\mu$m. The grating has been designed to be antireflect- ing for TE polarization at $\phi = \theta_1 = 0^\circ$ (normal incidence, $\mathbf{E} \perp \mathbf{K}$), with $F_{\text{AR}} = 0.222$ and $d_{\text{AR}} = 0.4010$ $\lambda_0$ from the first-order index formulas [Eqs. (A2) and (7)].

In Fig. 5 the zero-order backward diffraction effi- ciency $\text{DE}_0$ (power reflectance) for the grating is plotted as function of the wavelength-to-period ratio. The solid curve is the RCWA result (computed retaining 19 orders), which shows the anomalies associated with the cutoff of higher diffracted orders (indicated by arrows). For $\lambda_0/\Lambda < 3.5$ the homoge- neous layer models using $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$, the long-dashed and dashed-dotted curves, respec- tively, approximate the RCWA result with decreasing accuracy as the wavelength-to-period ratio decreases, and they eventually oscillate away from the correct result. For $\lambda_0/\Lambda > 3.5$, however, all non-zero- diffracted orders are cut off, and the homogeneous layer models using $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ very accurately follow the exact RCWA result. The short- dashed curve represents the first-order result, which shows a reflectance of exactly zero for all wavelength- to-period ratios. This is expected, because the first-

![](./images/811865545245720578_5.jpg)

Fig. 5. Response of a grating designed to be antireflecting using $\{n_O^{(1)}, n_E^{(1)}\}$ with $\phi = 0^\circ$, $\theta_1 = 0^\circ$, and TE polarization. The homogeneous layer reflectances using $\{n_O^{(1)}, n_E^{(1)}\}, \{n_O^{(2)}, n_E^{(2)}\}$, and $\{n_O^{(H)}, n_E^{(H)}\}$, together with the RCWA zero-order backward diffraction efficiency, are plotted as a function of wavelength-to- period ratio. For $\lambda_0/\Lambda > 3.5$ only the zeroth orders propagate, and the homogeneous layer models using $\{n_O^{(2)}, n_E^{(2)}\}$ and $\{n_O^{(H)}, n_E^{(H)}\}$ very closely approximate the RCWA result.

order indices contain no wavelength-to-period information. Finally, note that both the RCWA result and the homogeneous layer results using $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ smoothly approach the first-order result as the wavelength-to-period ratio approaches infinity.

Figures 6(a)-6(d) give a comparison of antireflection designs using $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$. The angle of incidence is now chosen as $\theta_1 = 30^\circ$, which gives a cutoff point for the +1 forward-diffracted order of $\lambda_0/\Lambda = 4.0$. Thus to ensure the cutoff of all nonzero-diffracted orders we choose the grating period to be $0.2\ \lambda_0$. Design values for $F_{\text{AR}}$ and $d_{\text{AR}}$ using first-order, second-order, and higher-order indices are given in Table 1 for TE and TM polarizations in the $\phi = 0^\circ$ plane, along with the diffraction efficiencies achieved for each design. In Figs. 6(a), 6(b), 6(c), and 6(d) the zero-order backward diffraction efficiencies for these designs are plotted as a function of the wavelength-to-period ratio with design values of $F$, $d/\lambda_0$, and $\theta_1$, as a function of normalized groove depth with design values for $F$, $\lambda_0/\Lambda$, and $\theta_1$, as a function of filling factor with design values of $\lambda_0/\Lambda$, $d/\lambda_0$, and $\theta_1$, and as a function of angle of incidence with design values of $\lambda_0/\Lambda$, $d/\lambda_0$, and $F$, respectively. The reduction in $\text{DE}_0$ by use of $\{n_O^{(2)}, n_E^{(2)}\}$ and $\{n_O^{(H)}, n_E^{(H)}\}$ is clear from these plots. However, it is seen that although the designs using $\{n_O^{(2)}, n_E^{(2)}\}$ and $\{n_O^{(H)}, n_E^{(H)}\}$ have produced gratings with lower reflectance, the reflectance minima are not located at the design points (indicated by vertical lines). For instance, in Fig. 6(d) the second-order design for TM polarization is seen to outperform the higher-order design at the design angle of incidence, and the higher-order design has its minimum at normal incidence. However, by using the design values from the homogeneous layer models as a starting point, we can further optimize the designs by using the RCWA. The optimized values for $F_{\text{AR}}$ and $d_{\text{AR}}$ are given in the last row of Table 1. The results of these optimizations are shown in Fig. 7, where very deep minima are now seen to occur at the design angle of incidence and wavelength-to-period ratio. By using these optimized values for $F_{\text{AR}}$ and $d_{\text{AR}}$, we achieve an improvement in performance of better than 2 orders of magnitude at the design points for both the TE and TM cases.

## 4. Conical Incidence
To demonstrate the validity of the homogeneous layer models at conical incidence, consider the silicon grating designed to be antireflecting at normal inci-

![](./images/811865545245720578_6.jpg)

Fig. 6. Relative performance of antireflection designs accomplished by the use of $\{n_O^{(1)}, n_E^{(1)}\}$, $\{n_O^{(2)}, n_E^{(2)}\}$, and $\{n_O^{(H)}, n_E^{(H)}\}$, as calculated by RCWA: (a) $\text{DE}_0$ as a function $\lambda_0/\Lambda$, holding $F$, $d$, and $\theta_1$ at their design values. The bump in each curve at $\lambda_0/\Lambda = 4.0$ is the cutoff point for the +1 diffracted order. (b) $\text{DE}_0$ as a function of $d/\lambda_0$ holding $\lambda_0/\Lambda$ and $F$ at their design values. Each of the TE designs has the same design groove thickness, whereas the TM designs have only slightly differing design thicknesses. (c) $\text{DE}_0$ as a function of $F$ while holding $\lambda_0/\Lambda$, $d$, and $\theta_1$ at their design values. All TE designs have the same response because of their identical $d$ values; the TM design responses are virtually identical for the same reason. (d) $\text{DE}_0$ as a function of $\theta_1$, holding $\lambda_0/\Lambda$, $F$, and $d$ at their design values. Each design shows a large range of incidence angles for which the reflectance remains below 1%. Input parameters, design values, and design-point performances are given in Table 1. The vertical lines in each plot indicate the design values of the abscissa quantities (line types as in the previous plots; solid vertical lines indicate values common to the three designs).

---
1 May 194 / Vol. 33, No. 13 / APPLIED OPTICS 2701

<table>
<caption>Table 1. Example Antireflection Design Parametersª</caption>
<thead>
<tr>
<th rowspan="2">Design Model</th>
<th colspan="3">TE Polarization</th>
<th colspan="3">TM Polarization</th>
</tr>
<tr>
<th>$d_{AR}/\lambda_0$</th>
<th>$F_{AR}$</th>
<th>$\text{DE}_0$ (%)</th>
<th>$d_{AR}/\lambda_0$</th>
<th>$F_{AR}$</th>
<th>$\text{DE}_0$ (%)</th>
</tr>
</thead>
<tbody>
<tr>
<td>First-order indices</td>
<td>0.1443</td>
<td>0.2000</td>
<td>1.1958</td>
<td>0.1268</td>
<td>0.8155</td>
<td>3.7546</td>
</tr>
<tr>
<td>Second-order indices</td>
<td>0.1443</td>
<td>0.1704</td>
<td>0.0104</td>
<td>0.1270</td>
<td>0.7178</td>
<td>0.0564</td>
</tr>
<tr>
<td>Higher-order indices</td>
<td>0.1443</td>
<td>0.1679</td>
<td>0.0135</td>
<td>0.1272</td>
<td>0.6633</td>
<td>0.4554</td>
</tr>
<tr>
<td>RCWA opti- mization</td>
<td>0.1460</td>
<td>0.1667</td>
<td>0.0001</td>
<td>0.1250</td>
<td>0.7100</td>
<td>0.0007</td>
</tr>
</tbody>
</table>

ªDesign and optimized values for $F_{AR}$ and $d_{AR}$ are computed by use of first-, second-, and higher-order indices and are finally optimized by RCWA. The resulting zero-order backward diffraction efficiencies are given for each design. The input parameters are $\lambda_0/\Lambda = 5$, $n_1 = 1.0$, $n_3 = 3.5$, $\phi = 0^\circ$, and $\theta_1 = 30^\circ$.

dence with $\mathbf{E} \perp \mathbf{K}$ (Fig. 5). Under TE illumination at $\phi = \theta_1 = 45^\circ$, the forward- and backward-diffracted orders each contain both TE and TM components, with some relative phase shift between them. Figure 8(a) shows the TE component of the zero-order backward diffraction efficiency $\text{DE}_0^{\text{TE}}$, the TM component $\text{DE}_0^{\text{TM}}$, and the total zero-order backward diffraction efficiency $\text{DE}_0$ ($\text{DE}_0^{\text{TE}} + \text{DE}_0^{\text{TM}} = \text{DE}_0$), whereas Fig. 8(b) shows the relative phase shift between these two components. The cutoff point for the +1 forward-diffracted order is at $\lambda_0/\Lambda = 3.96$. As in the nonconical case, the homogeneous layer models very

![](./images/811865545245720578_7.jpg)

Fig. 7. Optimization of TE and TM higher-order homogeneous layer model (HLM) designs by RCWA. Solid curves indicate contours of constant $\text{DE}_0$ given in percent. The input parameters are the same as those of Fig. 6.

![](./images/811865545245720578_8.jpg)

Fig. 8. Grating of Fig. 5, now illuminated at $\phi = 45^\circ$, $\theta_1 = 45^\circ$, with TE polarization. (a) TE component of the zero-order backward diffraction efficiency $\text{DE}_0^{\text{TE}}$, the TM component $\text{DE}_0^{\text{TM}}$, the total $\text{DE}_0$, and (b) the phase difference from TE to TM components are each plotted as a function of the wavelength-to-period ratio.

closely approximate the exact results from RCWA, including the polarization mixing associated with conical diffraction. Also as in Fig. 5, each plot shows convergence toward the first-order result in the long-wavelength limit.

Even though the homogeneous layer models accurately predict the actual diffraction characteristics, it is apparent from Fig. 8(a) that the grating designed to be antireflecting at normal incidence no longer exhibits its antireflecting behavior at conical incidence. To design an antireflecting grating for a particular conical incidence, we simply start with the $\phi = 0^\circ$ nonconical design that has the same angle of incidence $\theta_1$. This type of procedure is necessary because there are no analytical conical incidence antireflecting designs analogous to those for nonconical incidence. This is due to the inherent coupling between orthogonal polarizations that exists in the conical case.

To motivate the need for antireflection designs at conical incidence, consider Fig. 9, which is a schematic representation of linearly polarized light refracted onto an antireflection grating (e.g., detector surface) by a small $f$-number system. New angles $\alpha = \sin^{-1}[\sin(\theta_1)\sin(\phi)]$ and $\delta = \cos^{-1}[\cos(\theta_1)/\cos(\alpha)]$ are defined to facilitate this analysis. Prior to entering the system all the light is polarized along the $\hat{x}$ direction ($\mathbf{H} \perp \mathbf{K}$), but on passing through the lens all of the nonnormal incident plane waves with wave vectors not contained in the $\phi = 0^\circ$ or $\phi = 90^\circ$ planes acquire $\hat{y}$ and $\hat{z}$ polarization components such that the polarization is continuous across the refracting boundary.

![](./images/811865545245720578_9.jpg)

Fig. 9. Antireflection grating illuminated through a small $f$-number system. Linearly polarized light is deflected toward the grating, with electric-field vectors indicated by arrows.

To obtain a representation of the reflected power from the grating, we can calculate the plane-wave response by RCWA for each value of angles $\alpha$ and $\delta$. This is done for the range of $\alpha$ and $\delta$ that describes the converging cone's solid angle. The resulting plot of diffraction efficiencies is given in Fig. 10. The grating analyzed for this plot is the grating from Table 1, previously optimized for TM polarization at $\phi = 0^\circ$ and $\theta_1 = 30^\circ$. In Fig. 10, $\text{DE}_0$ is plotted for $\alpha$ and $\delta$ values contained in the solid angle described by $0^\circ < \theta_1 < 45^\circ$. $\text{DE}_0$ is not calculated for $\alpha$ and $\delta$ values outside this solid angle, and hence the efficiency is shown as zero for these points. It is seen in Fig. 10 that the reflectance does not exceed 6.97% over the entire range of conical incidence parameters. Similar results are obtained by use of the homogeneous layer model indices $\{n_O^{(H)}, n_E^{(H)}\}$, with the maximum error between the model and the RCWA results being 2.96% at $\alpha = 45^\circ$, $\delta = 0^\circ$ ($\phi = 90^\circ, \theta_1 = 45^\circ$).

This design can be optimized for a particular conical incidence. For example, it may be desired to have antireflection behavior for the polarization of Fig. 9 at an incidence of $\phi = 45^\circ$ and $\theta_1 = 30^\circ$. Starting with $\phi = 0^\circ$ and $\theta_1 = 30^\circ$, we obtain the values $d_{\text{AR}} = 0.1272\ \lambda_0$ and $F_{\text{AR}} = 0.6633$ by using $\{n_O^{(H)}, n_E^{(H)}\}$. For incidence at $\phi = 45^\circ$ and $\theta_1 = 30^\circ$, these grating parameters produce a $\text{DE}_0$ of 0.2970%. Figure 11 shows refinement using RCWA to obtain optimized grating parameters of $d_{\text{AR}} = 0.1310\ \lambda_0$ and $F_{\text{AR}} = 0.6762$. After optimization, the reflectance is reduced to $\text{DE}_0 = 0.0487\%$.

This design can also be optimized for all angles of conical incidence considered together. In this case the parameters of the grating would be scanned so as to minimize the volume under the surface in Fig. 10. The advantage of homogeneous layer analysis for such a computationally intensive project is clear,

AR Si GRATING
(Optimized Design for $\phi=0^{\circ}, \theta_{1}=30^{\circ}, H \perp K$)

![](./images/811865545245720578_10.jpg)

Fig. 10. Plane-wave impulse responses calculated by RCWA for the optimized antireflection grating design from Table 1 for $\phi = 0^\circ$, $\theta_1 = 30^\circ$, and TM polarization illuminated as in Fig. 9. Responses are calculated in the range $-46^\circ < \alpha < 46^\circ$ and $-45^\circ < \delta < 45^\circ$, thus covering the solid angle described by $0^\circ < \theta_1 < 45^\circ$.

1 May 1994 / Vol. 33, No. 13 / APPLIED OPTICS 2703

![](./images/811865545245720578_11.jpg)

Fig. 11. Higher-order antireflection grating design from Table 1 for $\phi = 0^\circ$, $\theta_1 = 30^\circ$, and TM polarization optimized by RCWA for $\phi = 45^\circ$, $\theta_1 = 30^\circ$, and the polarization of Fig. 9; HLM, homogeneous layer model.

because an analysis of the layer model uses approximately 1% of the CPU time required by the RCWA with 19 orders retained.

## 5. Discussion
The results of Section 4 provide a clear demonstration of the validity of the homogeneous layer model for predicting the behavior of dielectric high-spatial-frequency gratings. Several additional points regarding these results are as follows.

First, from Figs. 5 and 8 it is noted that even past the cut-on point when the first nonzero order begins to propagate, the homogeneous layer model predicts the total zero-order diffraction efficiency to within $\pm 10\%$.

Second, in the antireflection designs even the use of higher-order indices in the layer model does not guarantee zero reflectance at the design points. Rather, the minimum in reflectance comes at some point in the parameter space very close to, but not actually coinciding with, the point specified by the model. It is important to understand that the homogeneous layer models would each predict a $\text{DE}_0$ value of exactly zero at each of the design points indicated by the vertical lines in Figs. 6(a)-6(d). This serves to demonstrate that no matter how closely the model approximates the grating, it is still always necessary to utilize rigorous theory to determine the true behavior of the grating.

Third, antireflection designs such as those presented in Table 1 using $\{n_O^{(H)}, n_E^{(H)}\}$ and $\{n_O^{(2)}, n_E^{(2)}\}$ are sensitive to changes in groove depth and filling factor, and they are relatively insensitive to angle of incidence. For our example designs, the depth for which $\text{DE}_0$ remains below 1% is the design depth $\pm 0.01\ \lambda_0$ for both the TE and TM cases. Likewise, the filling factors for which $\text{DE}_0$ remains below 1% are the design filling factors $\pm 0.035$ for the TE designs and $\pm 0.055$ for the TM designs. Practically, these sorts of tolerances would be difficult to achieve at visible wavelengths. For example, for $\text{DE}_0 < 1\%$ with $\lambda_0 = 0.84\ \mu\text{m}$ and $\Lambda = 168\ \text{nm}$, in the TE case the groove depths must be between 111 and 132 nm, and the filling factor must be between 0.14 and 0.20 (corresponding to grating groove widths between 144 and 134 nm). In contrast, the range of $\theta_1$ for which $\text{DE}_0$ remains below 1% for our designs is quite large. For example, both optimized designs in the $\phi = 0^\circ$ plane had reflectances of less than 1% for $0^\circ < \theta_1 < 50^\circ$. As we expected, when the antireflection grating is designed for an angle of incidence between the Brewster angle and normal incidence, the reflectance remains very low for a wide field of view.

Although we have treated only the rectangular-groove (binary) case, the extension to arbitrary (one-dimensional) profiles could be accomplished by the film-stack method of Ono *et al.*,³ together with the layer analysis of Berreman²⁶ or Yeh.²⁷ The inclusion of loss in the substrate index should also be straightforward, thus permitting the modeling of conical diffraction by high-spatial-frequency metallic and lossy semiconductor gratings by this method as well. The lossy semiconductor case is of particular interest, because by optical or electrical injection of carriers into the substrate the conductivity and hence the complex refractive index could be actively modulated.

## 6. Conclusion
The use of homogeneous layer models for approximating the behavior of rectangular-groove (binary) dielectric surface-relief gratings in the conical diffraction case has been investigated. We have shown by comparison with rigorous theory that the models very accurately describe zero-order diffraction by such gratings, for all angles and planes of incidence, provided that all higher-diffracted orders are cut off. This holds true for the coupled conical diffraction case as well as for the decoupled nonconical cases. In the conical diffraction case, we have shown that the homogeneous layer models accurately describe the diffraction efficiency and phase shifts in the zero-diffracted orders for linearly polarized input light. This implies that the homogeneous layer models may be used in the design of retarders and wave-plate-type devices. We have shown that the models may be used with good results close to the onset of propagating higher orders, provided that the appropriate equivalent indices are used. Finally, we have demonstrated antireflection designs, using second-order and higher-order indices, for smaller wavelength-to-period ratios for both the coupled conical diffraction case and the decoupled nonconical case. We have shown how these designs may be optimized for both the conical and nonconical cases using the RCWA. The reduced wavelength-to-period ratios of these designs make the manufacture of such gratings feasible.

### Appendix A: Antireflection Filling Factors

To design antireflection surfaces with high-spatial-frequency gratings, we must specify (a) the desired wavelength-to-period ratio, (b) the refractive indices $n_1$ and $n_3$, (c) the angle of incidence $\theta_1$, (d) the plane of incidence ($\phi = 0^\circ$ or $\phi = 90^\circ$), and (e) the polarization (TE or TM). With these parameters specified, the effective index $N_2$ must be made to satisfy Eq. (8). To accomplish this we assign to the groove depth one of the values given by Eq. (7). Then Eq. (8) can be evaluated, either numerically by using the higher-order or second-order indices, or analytically as given below by using the first-order indices. Strictly speaking, the use of first-order indices in determining $F_{\text{AR}}$ only produces zero-reflectivity surfaces in the long-wavelength limit ($\lambda_0 \gg \Lambda$). However, it has been observed that the formulas given for the TE cases can produce good results for wavelength-to-period ratios as small as 5.

### Case 1: $\boldsymbol{\phi = 0^\circ}$, TE Polarization
With the electric field polarized in the $\hat{y}$ direction, only the ordinary wave is excited in the grating and $n_2$ is given by $n_O$. Thus the effective index in region 2 is $n_O \cos \theta_2$ and Eq. (8) reduces to
$$
n_O^2 - n_1 \cos \theta_1 n_3 \cos \theta_3 - n_1^2 \sin^2 \theta_1 = 0. \quad \text{(A1)}
$$
By use of $n_O^{(1)}$ this reduces to
$$
F_{\text{AR}} = \frac{n_1 \cos \theta_1}{n_1 \cos \theta_1 + n_3 \cos \theta_3} \cdot \tag{A2}
$$

### Case 2: $\boldsymbol{\phi = 0^\circ}$, TM Polarization
For polarization in the plane of incidence and for nonzero $\theta_1$, an extraordinary wave is excited in the grating. The index seen by this wave is $n_2(\theta_2) = \left[(n_E^2 n_O^2)/(n_E^2 \sin^2 \theta_2 + n_O^2 \cos^2 \theta_2)\right]^{1/2}$, where $\theta_2$ satisfies $\tan^2 \theta_2 = (n_O^2 n_1^2 \sin^2 \theta_1)/(n_E^2 n_O^2 - n_E^2 n_1^2 \sin^2 \theta_1)$. Using the effective index $N_2 = n_E^2 / n_2 \cos \theta_2$, we find that Eq. (8) becomes
$$
n_O^2 - n_E^2 n_O^2 \left( \frac{\cos \theta_1 \cos \theta_3}{n_1 n_3} \right) - n_1^2 \sin^2 \theta_1 = 0. \quad \text{(A3)}
$$
Utilizing $n_O^{(1)}$ and $n_E^{(1)}$ with these results, we find $F_{\text{AR}}$ to satisfy the quadratic equation
$$
F_{\text{AR}} = \frac{-B \pm \left[ B^2 - 4AC \right]^{1/2}}{2A}, \tag{A4}
$$
where the variables $A$, $B$, and $C$ are given by
$$
\begin{align*}
A &= (n_3^2 - n_1^2)^2, \\
B &= (n_3^2 - n_1^2)\left(n_1 \cos \theta_1 n_3 \cos \theta_3 + n_1^2 \cos^2 \theta_1 - n_3^2\right), \\
C &= n_1^2\left(n_1 \cos \theta_1 n_3 \cos \theta_3 - n_3^2 \cos^2 \theta_1\right). \tag{A5}
\end{align*}
$$
In order to have physically meaningful solutions for the filling factor ($0 \leq F \leq 1$), we take the positive discriminant in Eq. (A4) for $\theta_1$ values below the Brewster angle, and the negative discriminant is taken for $\theta_1$ values above the Brewster angle.

### Case 3: $\boldsymbol{\phi = 90^\circ}$, TE Polarization
Here the incident wave is polarized parallel to the grating vector for all values of $\theta_1$, and thus $n_2 = n_E$. Equation (8) has the form
$$
n_E^2 - n_1 \cos \theta_1 n_3 \cos \theta_3 - n_1^2 \sin^2 \theta_1 = 0, \quad \text{(A6)}
$$
and the antireflection filling factor using $n_E^{(1)}$ is found to be
$$
F_{\text{AR}} = \frac{n_3 \cos \theta_1}{n_1 \cos \theta_3 + n_3 \cos \theta_1} \cdot \tag{A7}
$$

### Case 4: $\boldsymbol{\phi = 90^\circ}$, TM Polarization
Again the grating behaves as an isotropic layer for all values of $\theta_1$, and the refractive index seen by the incoming wave is $n_2 = n_O$. Equation (8) becomes
$$
n_O^4 - \left( \frac{n_1 n_3}{\cos \theta_1 \cos \theta_3} \right)\left(n_O^2 - n_1^2 \sin^2 \theta_1\right) = 0, \quad \text{(A8)}
$$
and the use of $n_O^{(1)}$ leads to another quadratic expression for the antireflection filling factor, with new coefficients:
$$
\begin{align*}
A &= (n_3^2 - n_1^2)^2, \\
B &= (n_3^2 - n_1^2)\left[2 - n_1 n_3/(\cos \theta_1 \cos \theta_3)\right], \\
C &= n_1^2(n_1^2 - n_1 n_3 \cos \theta_1/\cos \theta_3). \tag{A9}
\end{align*}
$$
Once again the sign of the discriminant is chosen as in case 2 so that we have physically significant solutions on either side of the Brewster angle.

This research was supported in part by grant DAAL-03-90-0004 from the Joint Services Electronics Program.

---

### References
1. R. C. Enger and S. K. Case, "Optical elements with ultrahigh spatial-frequency surface corrugations," Appl. Opt. **22**, 3220-3228 (1983).
2. T. K. Gaylord, W. E. Baird, and M. G. Moharam, "Zero-reflectivity high spatial-frequency rectangular-groove dielectric surface-relief gratings," Appl. Opt. **25**, 4562-4567 (1986).
3. Y. Ono, Y. Kimura, Y. Ohta, and N. Nishida, "Antireflection effect in ultrahigh spatial-frequency holographic relief gratings," Appl. Opt. **26**, 1142-1146 (1987).
4. T. K. Gaylord, E. N. Glytsis, and M. G. Moharam, "Zero-reflectivity homogeneous layers and high spatial-frequency surface-relief gratings on lossy materials," Appl. Opt. **26**, 3123-3134 (1987).
5. E. N. Glytsis and T. K. Gaylord, "Antireflection surface structure: dielectric layer(s) over a high spatial-frequency surface-relief grating on a lossy substrate," Appl. Opt. **27**, 4288-4304 (1988).
6. T. K. Gaylord, E. N. Glytsis, M. G. Moharam, and W. E. Baird, "Technique for producing antireflection grating surfaces on dielectrics, semiconductors, and metals," U.S. Patent 5,007,708 (16 April 1991).
7. E. N. Glytsis and T. K. Gaylord, "High-spatial-frequency

---

1 May 1994 / Vol. 33, No. 13 / APPLIED OPTICS 2705

binary and multilevel stairstep gratings: polarization-selec- tive mirrors and broadband antireflection surfaces," Appl. Opt. 31, 4459-4469 (1992).

8. M. E. Motamedi, W. H. Southwell, and W. J. Gunning, "Antireflection surfaces in silicon using binary optics technol- ogy," Appl. Opt. 31, 4371-4376 (1992).

9. D. H. Raguin and G. M. Morris, "Antireflection structured surfaces for the infrared spectral region," Appl. Opt. 32, 1154-1167 (1993).

10. D. H. Raguin and G. M. Morris, "Analysis of antireflection- structured surfaces with continuous one-dimensional pro- files," Appl. Opt. 32, 2582-2598 (1993).

11. K. Knop, "Diffraction gratings for color filtering in the zero order," Appl. Opt. 17, 3598-3603 (1978).

12. D. C. Flanders, "Submicrometer periodicity gratings as artifi- cial anisotropic dielectrics," Appl. Phys. Lett. 42, 492-494 (1983).

13. W. Stork, N. Streibl, H. Haidner, and P. Kipfer, "Artificial distributed-index media fabricated by zero-order gratings," Opt. Lett. 16, 1921-1923 (1991).

14. L. Cescato, E. Gluch, and N. Streibl, "Holographic quarter- wave plates," Appl. Opt. 29, 3286-3290 (1990).

15. M. G. Moharam and T. K. Gaylord, "Three-dimensional vector coupled-wave analysis of planar-grating diffraction," J. Opt. Soc. Am. 73, 1105-1112 (1983).

16. R. Petit, ed., *Electromagnetic Theory of Gratings* (Springer- Verlag, Berlin, 1980).

17. M. G. Moharam and T. K. Gaylord, "Diffraction analysis of dielectric surface-relief gratings," J. Opt. Soc. Am. 72, 1385-1392 (1982).

18. O. Wiener, "Die theorie des mischkorpers fur das feld der stationaren stromung," Abh. Math. Phys. Kl. Saechs. Akad. Wiss. Leipzig 32, 509-604 (1912).

19. W. Thornburg, "The form birefringence of lamellar systems containing three or more components," J. Biophys. Biochem. Cytol. 3, 413-419 (1957).

20. S. M. Rytov, "Electromagnetic properties of a finely stratified medium," Soviet Phys. JETP 2, 466-475 (1956).

21. M. Born and E. Wolf, *Principles of Optics* (Pergamon, London, 1980), pp. 705-708.

22. R. C. McPhedran, L. C. Botten, M. S. Craig, M. Neviere, and D. Maystre, "Lossy lamellar gratings in the quasistatic limit," Opt. Acta 29, 289-312 (1982).

23. T. K. Gaylord and M. G. Moharam, "Analysis and applicationsof optical diffraction by gratings," Proc. IEEE 73, 894-938(1985).

24. G. Bouchitte and R. Petit, "Homogenization techniques as applied in the electromagnetic theory of gratings," Electro- mag. 5, 17-36 (1985).

25. L. C. Botten, M. S. Craig, R. C. McPhedran, J. L. Adams, and J. R. Andrewartha, "The dielectric lamellar diffraction grat- ing," Opt. Acta 28, 413-428 (1981).

26. D. Berreman, "Optics in stratified and anisotropic media:4 × 4-matrix formulation," J. Opt. Soc. Am. 62, 502-510(1972).

27. P. Yeh, "Electromagnetic propagation in birefringent layered media," J. Opt. Soc. Am. 69, 742-756 (1979).

28. R. F. Harrington, *Time Harmonic Electromagnetic Fields*(McGraw-Hill, New York, 1961), pp. 55-57.

29. A. Knoesen, M. G. Moharam, and T. K. Gaylord, "Electromag- netic propagation at interfaces and in waveguides in uniaxial crystals," Appl. Phys. B 38, 171-178 (1985).