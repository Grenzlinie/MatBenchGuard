# Form Birefringence Phase Matching in Multilayer Semiconductor Waveguides: Tuning and Tolerances

Alfredo De Rossi, Vincent Berger, Giuseppe Leo, and Gaetano Assanto, *Member, IEEE*

**Abstract**—GaAs–Alox waveguide structures for parametric processes are analyzed in detail. The geometric tolerances of the structure are numerically calculated with reference to its parametric tuning. Finally, the tunability of GaAs–Alox based parametric devices versus temperature is investigated.

**Index Terms**—Nonlinear optics, optical waveguides, phase matching, semiconductor waveguides.

## I. INTRODUCTION

THE CONCEPT of form-birefringence phase matching for nonlinear frequency conversion was introduced to achieve frequency conversion using high $\chi^{(2)}$ materials such as III–V semiconductors (e.g., GaAs) and demonstrated in recent years [1]. Such cubic materials, in fact, are optically isotropic and prevent the use of the standard critical phase matching. However, multilayer geometries allow to circumvent this limitation, opening new perspectives for nonlinear frequency conversion in highly nonlinear crystals [1]. To date, difference frequency generation [2], frequency doubling [3] and, more recently, parametric fluorescence [4], [5], have been reported in GaAs–oxidized AlAs (GaAs–Alox) waveguides. One of the most exciting goals in this framework, however, remains the realization of a semiconductor integrated parametric source: a widely tunable (from 1.4 to 3.5 $\mu$m) guided-wave optical parametric oscillator on a GaAs chip or else, below threshold, a twin photon source for quantum information or fundamental studies in quantum mechanics [6].

The object of our investigations in this paper is a GaAs–Alox waveguide of the type sketched in Fig. 1(a). This waveguide is designed for type I parametric fluorescence with degeneracy at 1065 nm, with a TM pump and TE signal and idler. Its vertical refractive index profile (i.e., along $x$) is reported in Fig. 1(b) along with the vertical profiles of the three interacting eigenmodes. This design is motivated by the fact that we aim at the fabrication of a guided-wave optical parametric oscillation, for which a 1.064-$\mu$m Nd:YAG laser is best suited. In the following, correspondingly, we will focus around this wavelength for the calculated tuning from the structure parameters [Fig. 2(a)].

![](./images/812136233072328705_1.jpg)

Fig. 1. Structure of a typical GaAs–Alox waveguide designed for parametric fluorescence. (a) 3-D structure, with propagation along $z$, vertical confinement along $x$, and horizontal confinement along $y$; the guiding ridge has width $W$ and height $H$. (b) Vertical structure, grown by molecular beam epitaxy (MBE) with the following layer sequence: GaAs (001) substrate, 1000-nm $\text{Al}_{0.92}\text{Ga}_{0.08}\text{As}$, 1000-nm $\text{Al}_{0.7}\text{Ga}_{0.3}\text{As}$, $4\times$ (34.5-nm Alox, 272-nm GaAs), 34.5-nm Alox, 1000-nm $\text{Al}_{0.7}\text{Ga}_{0.3}\text{As}$, 30-nm GaAs. TM pump mode at 1.065 $\mu$m and TE signal-idler mode at 2.13 $\mu$m are shown by solid and dotted lines, respectively.

In general, we find a remarkable sensitivity of the tuning curve and its position relative to the structure parameters (layer thicknesses, in particular), and this motivates the careful study of their influence which is addressed in this paper.

An experimental example of tuning curve is shown in Fig. 2(b) (open dots). This spectral analysis of parametric fluorescence requires a tunable laser pump. Since we dispose of a Ti:Sa laser (which is only tunable up to 1 $\mu$m), the spectrum of Fig. 2(b) was obtained with this pump on a waveguide similar to that of Fig. 1(b), but with the degeneracy wavelength deliberately shifted around 992 nm.

When comparing this parametric tuning curve to analogous ones obtained in bulk materials, we can note a significantly wide tunability of both signal and idler as a function of the pump wavelength. In other words, the tuning line appears quite "flat"

---

Manuscript received March 8, 2005; revised June 3, 2005. This work was supported in part by the European Union project "OFCORSE II."

A. De Rossi is with the Thales Research and Technology, Domaine de Corbeville, 91400 Orsay, France (e-mail: alfredo.derossi@thalesgroup.com).

V. Berger and G. Leo are with the Laboratoire Matériaux et Phénomènes Quantiques, Université Paris 7-Denis Diderot, 75251 Paris, France (e-mail: vincent.berger@thalesgroup.com; leo.giuseppe@paris7.jussieu.fr).

G. Assanto is with the Nonlinear Optics and Optoelectronics Laboratories (NOOEL) Department of Electronic Engineering, University of Rome Tre, 84-00146 Rome, Italy (e-mail: assanto@ele.uniroma3.it).

Digital Object Identifier 10.1109/JQE.2005.854133

0018-9197/$20.00 © 2005 IEEE

![](./images/812136233072328705_2.jpg)

Fig. 2. (a) Calculated tuning of the parametric GaAs-Alox waveguide described in Fig. 1(b). The thin solid line was obtained with a 1-D model, taking the Alox refractive index equal to 1.6. The dashed line corresponds to (2). The dots were calculated with a 2-D scalar model. (b) Example of an experimental tuning curve, with a fit given by (2). This spectrum was obtained with a Ti:Sa tunable laser.

at the degeneracy point: even small variations in the pump wavelength largely affect signal and idler.

The origin of this feature is the huge dispersion of the parametric waveguide. Due to strong dispersion near the material bandgap (see Fig. 3), the dependence of the effective index $\beta$ on wavelength is much more relevant for the pump $\lambda_p$ than for $\lambda_s$

$$
\frac{\partial \beta^{\mathrm{TM}}}{\partial \lambda}\left(\lambda_{p}\right) \gg \frac{\partial \beta^{\mathrm{TE}}}{\partial \lambda}\left(\lambda_{s} \approx 2 \lambda_{p}\right). \tag{1}
$$

Around degeneracy and neglecting the second-order derivative of the refractive indices, the relationship (tuning curve) between signal, idler and pump wavelengths can be approximated by the simple expression

$$
\lambda_{s, i}=\frac{2 \lambda_{p}}{1 \pm \alpha \sqrt{\frac{\lambda_{p}^{0}}{\lambda_{p}}-1}} \tag{2}
$$

with the "aperture" $\alpha$ of the tuning curve given by

$$
\alpha=\sqrt{\frac{\frac{\partial \beta^{\mathrm{TM}}}{\partial \lambda}\left(\lambda_{p}^{0}\right)}{2 \frac{\partial \beta^{\mathrm{TE}}}{\partial \lambda}\left(\lambda_{s}^{0}\right)}-1}. \tag{3}
$$

In the expression above, the superscript 0 indicates values at degeneracy. This simple approximation [dashed line in Fig. 2(a)] nicely follows the exact tuning obtained from the slab waveguide effective indices, with $\alpha=1.92$. It also fits well the experimental data [Fig. 2(b)], although for a different $\lambda_{p}^{0}$ and $\alpha=2.53$. The substantial agreement stems from the fact that the second-order derivatives of the effective indices are actually negligible, and allows using (2) and the waveguide eigenvalues without having to resort to complicated derivations. In addition, this expression is not only valid for birefringent phase matching in semiconductors, but for quasi-phase matching [7] or modal phase matching [8] in waveguides as well. It also elucidates some insight on the tuning-curve aperture: the greater the ratio between the derivatives of $\beta^{\mathrm{TM}}$ and $\beta^{\mathrm{TE}}$ (calculated at $\lambda_{p}^{0}$ and $\lambda_{s}^{0}$, respectively), the wider the aperture. This explains why the experimental curve, obtained at a lower $\lambda_{p}^{0}$, presents a wider aperture, too: lower wavelengths indeed imply higher dispersion near the bandgap.

![](./images/812136233072328705_3.jpg)

Fig. 3. Effective indices in the structure described in Fig. 1. The fundamental modes are shown with solid lines for the two polarizations, and higher order modes appear in dotted lines. Here we have $\beta^{TM_{0}}(1.065\ \mu m)=$ $\beta^{TE_{0}}(2.13\ \mu m)$: The degeneracy of the parametric process occurs for a 1.065 $\mu$m pump wavelength. The refractive indices of GaAs, $Al_{0.7}Ga_{0.3}As$, and $Al_{0.92}Ga_{0.08}As$ (cladding) are also shown (dashed lines).

For parametric processes farther in the infrared (IR), the tunability of signal and idler with pump wavelength is expected to be lower, and the linewidth of the matching resonances is expected to be larger.

Conversely, the large aperture of the tuning curve turns out to be a great advantage: while semiconductor laser sources that could be used to pump a compact parametric device usually exhibit a limited tunability, a widely tunable parametric source can be obtained owing to the high value of $d\lambda_{s,i}/d\lambda_p$ in GaAs-Alox waveguides. On the other hand, however, the curve flatness is responsible for the high sensitivity of the structure to variations of parameters such as refractive indices and layer thicknesses, temperature, or profile of the waveguide ridge. Except for temperature, these parameters are difficult to control with great precision. Despite the significant advancement represented by the introduction of oxidized AlAs, its refractive index and dispersion are not available with a satisfactory accuracy, and they seem to largely depend on the oxidation process. Moreover, the thickness of GaAs and AlAs layers grown by molecular beam epitaxy can hardly be kept accurate better than 1%. AlAs layers are known to shrink in thickness during the oxidation by a factor which also depends on the processing conditions. Finally, but not less importantly, the ridge depth after etching typically presents inhomogeneities along the length, resulting in detrimental effective-index variations (hence mismatch) along propagation.

In this paper, with explicit reference to GaAs–Alox wave-
guide structures, we attempt to quantitatively investigate the
influence that variations of the above parameters have on the
parametric tuning curve. Clearly, such analysis is of paramount
importance for any practical device design, and allows estab-
lishing the tolerances in both growth/processing steps and in the
refractive indices of the various layers. The paper is organized
as follows: Section II describes the numerical tools used for the
simulations, illustrating advantages and drawbacks of different
methods, i.e., one-dimensional (1-D) or two-dimensional (2-D)
multilayer waveguide calculations in the scalar approximation,
and full 2-D model with a vectorial solver. These tools are then
employed to study the dependence of parametric tuning versus
the film indices in the multilayer (Section III), the layer thick-
nesses (Section IV), the ridge profile (Section V), and the tem-
perature (Section VI). In the following, unless otherwise stated,
Fig. 2(a) will be our reference tuning curve, i.e., all the varia-
tions as a function of a given parameter will be calculated with
respect to it, keeping all the other parameters fixed.

## II. 1-D AND 2-D SIMULATIONS

With reference to the structure sketched in Fig. 1, the ef-
fective index and the waveguide modal field distributions are
calculated with three different degrees of approximation. The
first, and by far the simplest, is the 1-D or planar-waveguide
case. It is well known [9] that eigendistributions can be rig-
orously separated into transverse-electric or TE ($E_y$, $H_x$, $H_z$)
and transverse-magnetic or TM modes ($E_x$, $H_y$, $E_z$), with $z$
is the direction of propagation. The resulting scalar Helmholtz
equation is solved using a transmission matrix. This method
is semi-analytical and free of discretization/truncation errors.
Its accuracy is limited only by the precision reached in finding
the roots of transcendental equations in the complex plane. Al-
though this approximation begins to fail as the waveguide width
(across $y$) is decreased, for ridges wider than $5\ \mu$m, the main
contribution to form-birefringence is by far provided by the
Alox–GaAs stack. For such ridges, therefore, it is not surprising
that the 1-D method provides the phase-matching wavelength
with a better precision than that allowed by current models of
GaAs refractive index [11], [12].

The lateral confinement can be accounted for with the ef-
fective index method [9] unless the eigenfield distribution de-
parts significantly from a TE/TM separable form, as it is in the
case of deep ridges of high-index materials. A strong lateral
confinement couples TE and TM polarizations, and Maxwell
equations need be solved with the only assumption of a trans-
lational symmetry. This is implemented with the finite element
method (FEM), using specific basis functions such that each of
them satisfies Maxwell equations (this approach is also called
“full-wave” solution). The accuracy of this approach is related to
truncation and discretization errors and, therefore, to the number
of mesh elements. An additional problem is given by unphys-
ical solutions (such that $\nabla.\mathbf{D} \neq 0$), which must be correctly
handled. Finally, computation time on a Pentium 4 PC does not
constitute a problem, and effective indices can be calculated
within about $10^{-4}$ (i.e., within the model accuracy of mate-
rial indices) in a few minutes. With regards to our waveguides,

![](./images/812136233072328705_4.jpg)

Fig. 4. Tuning curves for different GaAs indices. The solid line is the reference
tuning curve, the dotted line on the left (right) is obtained with a GaAs index
greater (lower) than in the reference case by $\Delta n = 0.01$.

TE–TM coupling can be neglected in most cases, thereby justi-
fying the scalar approximation. The eigenvalue problem is for-
mulated as

$$\left(\nabla^{2}+n^{2}k_{0}^{2}\right)E_{y}=\beta^{2}k_{0}^{2}E_{y} \qquad \text{(TE)} \tag{4}$$

$$\left[\nabla\left(\frac{1}{n^{2}}\nabla\right)+k_{0}^{2}\right]H_{y}=\frac{\beta^{2}}{n^{2}}k_{0}^{2}H_{y} \qquad \text{(TM)} \tag{5}$$

with $n(x)$ the piecewise constant refractive index of the mul-
tilayer and $k_0$ the vacuum wavevector. These equations are
readily implemented using a scalar FEM solver. The numerical
results tend to be quite close ($10^{-4}$) to the full-wave solution
for near infrared wavelengths ($<2\ \mu$m) and waveguide wider
than $3\ \mu$m. The scalar solver is about ten times faster than the
full-wave one.

## III. TUNING-CURVE DEPENDENCE ON REFRACTIVE INDICES

AlGaAs refractive index versus wavelength is available in
literature with good accuracy. We checked this dependence by
effective indices measurements on AlGaAs waveguides [10]:
the guided-mode propagation constants were measured by
distributed coupling and m-line spectroscopy. Due to in-plane
wavevector conservation, a collimated beam impinging on
a photoresist grating on the guide surface could excite each
guided mode for a specific angle of incidence. Its measurement
led to the modal effective index with accuracies better than
$5\times 10^{-4}$ (for an example, see Section VI). In our geometry,
this yields four equations in order to solve the inverse problem,
i.e., to derive the refractive indices of the individual layers from
the effective indices of the multilayer guide. To this extent, the
layer thicknesses were acquired by X-ray reflectometry with
a relative accuracy of $10^{-3}$ [10]. Inferred values for AlGaAs
turned out in excellent agreement with those predicted in [11]
and used throughout this work. The refractive indices of GaAs,
Al$_{0.7}$Ga$_{0.3}$As, and Al$_{0.92}$Ga$_{0.08}$As are graphed in Fig. 3 as a
function of wavelength.

Fig. 4 shows variations in the tuning curve for a $10^{-2}$ change
in the index of GaAs layers. Since AlGaAs indices are known
with accuracies up to $10^{-3}$, it is apparent that a limited uncer-
tainty on AlGaAs is not a problem for the design of parametric
waveguides.

Different is the case with the refractive index of Alox. Its values are not available and hard to measure, because oxidized AlAs exists in thin layers and in small areas (e.g., 100-$\mu$m squares). This relates to the nature of the oxidation process, which proceeds laterally and with low speed in the plane of the epitaxial layers. While oxidized AlAs can be obtained at the top surface aiming at performing ellipsometric measurements on a large-area, there is no evidence that the materials obtained by this method or by lateral oxidation have the same properties. On the contrary, it is generally accepted that Alox refractive index depends on the oxidation conditions (time and temperature, AlAs thickness ...). So far, the Alox refractive index has not been studied systematically and accurately. This stems from the fact that in its most common applications, such as Alox-GaAs Bragg mirror fabrication, the index contrast is so large that the center wavelength of wide bandgap spectra is not a critical parameter. For phase-matching purposes, conversely, this issue requires a far greater attention. In this respect, employing transmission electron microscopy and low-angle X-ray reflectometry, Durand and co-workers [13] found that a thin (6 nm) film of Gaox is present on each side of the Alox layer. While this suggests that a three-layer "Gaox-Alox-Gaox" system should be investigated depending of oxidation conditions and layer thicknesses, for the sake of simplicity, hereby we will continue to refer to the "Alox refractive index." Using the method described earlier (X-ray reflectometry and grating coupling) we carried out the characterization of oxidized AlGaAs-AlAs quasi-planar waveguides to infer the "Alox refractive index." In this case, however, X-ray reflectometry did not yield an accurate estimate of the layer thicknesses because after oxidation the GaAs-Alox interface is no longer planar and Gaox films further complicate the issue bleaching the X-ray reflectometry signal. For AlAs thicknesses typical of our parametric waveguides, we measured the contraction of AlAs layers past oxidation [13], and found an Alox refractive index equal to $n = 1.60 \pm 0.005$, close to values reported elsewhere [14]. No data are available on the dispersion of Alox; however, owing to the large bandgap of this material its index versus wavelength can be taken constant at the mean value $n = 1.6$ with wavelength, thickness, oxidation time and temperature, allowing a deviation as large as 0.03. The latter error bar helps to account for the different results reported in literature for Alox films grown with various techniques and characterized at other wavelengths [14], [15].

Fig. 5 shows the calculated tuning curve of parametric fluorescence for several tentative values of Alox refractive index. Lower values enhance the contrast between the two materials in the multilayer and, hence, form birefringence. As a consequence, a larger amount of mismatch can be compensated and the degeneracy wavelength is shifted to lower values, closer to the bandgap where the dispersion is larger. At variance with the dependence previously seen on AlGaAs index, a 0.03 variation in Alox refractive index induces a shift larger than 10 nm from the degeneracy wavelength of the pump. This is an important issue, especially when the pump is a fixed wavelength source (e.g., a Nd:YAG laser). The designed tuning curve, in fact, may not intersect the pump wavelength at room temperature, due to a poor knowledge of the Alox index. This also applies to a certain extent to semiconductor lasers, which provide a limited tunability of a few nm. In such cases, temperature tuning can be adopted to shift the whole curve, as we will address in Section VI. We can therefore close this section by stressing that the accurate knowledge of the refractive indices of Alox is necessary for a proper design of parametric devices. The measurements reported above with $n = 1.6 \pm 0.005$ provide a satisfactory accuracy for given oxidation conditions ($T_{\text{oxidation}} = 405\,\mathrm{^\circ C}$, oxidation time $= 2\,\mathrm{h}$) and thickness $d_{\text{AlAs}} = 37.5\,\mathrm{nm}$. Different thicknesses or processing steps, however, could introduce significant discrepancies and render these values largely inadequate.

![](./images/812136233072328705_5.jpg)

Fig. 5. Tuning curves obtained with Alox refractive indices equal to 1.6 (solid line), 1.63, and 1.57 (dashed lines), respectively.

![](./images/812136233072328705_6.jpg)

Fig. 6. Form birefringence for an infinite multilayer GaAs-Alox structure, in the plane ($\Lambda/\lambda$; $a/\Lambda$), with $\lambda$ the wavelength, $\Lambda$ the multilayer period, and $a$ the GaAs layer thickness. The left axis corresponds to the large-wavelength approximation, where form birefringence is given by (6) and (7). The circle corresponds to our reference structure. The solid arrow indicates the structure drift due to an increased GaAs thickness. The dashed arrow represents the structure drift due to an increased Alox thickness.

### IV. TUNING-CURVE DEPENDENCE ON LAYER THICKNESSES

With reference to the structure in Fig. 1, Fig. 6 shows isobirefringence lines versus two parameters: the period $\Lambda$ of the Alox-GaAs unit cell in the form-birefringent multilayer, and the GaAs filling factor of such cell (i.e., the ratio between the GaAs thickness $a$ and $\Lambda$). The period $\Lambda$ is normalized with respect to

![](./images/812136233072328705_7.jpg)

Fig. 7. Parametric tuning curves for a 2% relative variation of GaAs layer thickness, as can occur in the case of a nonnominal growth.

the wavelength. For $\Lambda/\lambda \ll 1$ (near the left axis), a long-wavelength limit appears, and simple expressions give the dielectric constants in the two polarizations [1]

$$
\epsilon_{\mathrm{TE}} = \frac{a}{\Lambda} \epsilon_{\mathrm{GaAs}} + \left(1 - \frac{a}{\Lambda}\right) \epsilon_{\mathrm{Alox}} \tag{6}
$$

$$
\frac{1}{\epsilon_{\mathrm{TM}}} = \frac{a}{\Lambda} \frac{1}{\epsilon_{\mathrm{GaAs}}} + \left(1 - \frac{a}{\Lambda}\right) \frac{1}{\epsilon_{\mathrm{Alox}}}. \tag{7}
$$

It appears from Fig. 6 that this effective-medium approximation is reasonably good for typical ratios $\Lambda/\lambda < 0.1$, and fails for greater ratios. The circle represents the structure under study in this work (for a pump wavelength 1065 nm). An increase in the nominal thickness of the GaAs (Alox) layer corresponds to moving along the solid (dotted) arrow in the $(\Lambda/\lambda, a/\Lambda)$ plane. In fact, if the nominal GaAs thickness $a$ is increased by $\Delta a$, the coordinates of the structure are increased by $(\Delta(\Lambda/\lambda) = \Delta a/\lambda$, $\Delta(a/\Lambda) = (\Delta a/\Lambda)(1 - a/\Lambda))$. This is represented by the solid arrow in the figure, the direction of which is at $21^\circ$ from the horizontal axis. This angle is small because the structure contains a low Alox percentage. A change in Alox thickness (dashed arrow) has a little effect on the effective index of the multilayer guide: the dashed arrow follows approximately a line of constant birefringence. Conversely, a change in GaAs thickness (solid-line arrow), results in an important variation of the multilayer birefringence, because the displacement in the plane of Fig. 6 occurs in a direction of highest slope. In short, as we will illustrate in more details in the following, birefringence in typical parametric GaAs-Alox structures in more sensitive to the thickness of GaAs than Alox.

Notice that the maximum form-birefringence (between 0.5 and 0.6) is obtained for lower GaAs ratios as the period is increased. For structures located on this line of maxima, a deviation from nominal thicknesses implies small (second-order) variations on form-birefringence, hence this line represents a set of "stable" structures. It could be interesting to investigate form-birefringent structures using this type of multilayer. The use of a more birefringent multilayer in the waveguide core would imply a smaller number of Alox layers to compensate for material and modal dispersion and obtain phase matching.

The qualitative conclusions stemming from Fig. 6 are detailed in Figs. 7 and 8, which show the tuning variations when the thickness of GaAs or Alox layers varies. Such a structure modification can occur due to a nonnominal growth or a poorly predicted contraction factor of Alox. From Figs. 7 and 8 it is apparent that the main effect of a variation in layer thickness is a shift of the tuning curve, i.e., a shift of degeneracy wavelength for parametric fluorescence. This is explicitly shown in Fig. 9, where we can appreciate that thickness deviations in GaAs have far a greater impact than in Alox layers: for the former, the slope of the wavelength degeneracy variation is roughly 15 times larger for the latter. Since the thicknesses of Alox layers are less controllable (due to AlAs contraction during oxidation), this is indeed an advantage.

![](./images/812136233072328705_8.jpg)

Fig. 8. Parametric tuning curves for a 4% relative variation in Alox layer thickness, as can occur in the case of a nonnominal growth or unknown contraction.

![](./images/812136233072328705_9.jpg)

Fig. 9. Pump wavelength at degeneracy versus the deviation of GaAs and Alox layer thicknesses from the nominal values.

## V. TUNING-CURVE DEPENDENCE ON RIDGE WIDTH AND DEPTH

The waveguide effective indices depend on the transverse shape of the 2-D ridge defined by photolithography and etching, with an obvious impact on both phase matching and tuning. This dependence need be characterized for two main reasons: first, the processing steps can be tailored to shift the tuning curve by a desired quantity, to compensate e.g., for an epitaxial growth slightly off calibration. Second, a known dependence helps defining the tolerances to be enforced on the etching in order to guarantee that the parametric process is homogeneously phase-matched along the waveguide length.

![](./images/812136233072328705_10.jpg)

Fig. 10. Pump wavelength at degeneracy versus ridge width, for an etching depth H = 3 µm. For a process involving fundamental modes (e.g., one TM₀₀ photon gives two TE₀₀ signal and idler) two simulations are shown with different mesh accuracies: 8000 (solid line) and 2500 points (dashed line).

The dependence of the pump wavelength at degeneracy on the ridge width is displayed in Fig. 10 for three typical parametric processes, depending on both the pump mode (TM₀₀ or TM₀₁) and the TE polarized pair of signal and idler. In practice, the TM₀₀ → TE₀₀ process is usually preferred to maximize the field overlap. In the case of Fig. 10, where the ridge height is fixed equal to 3 µm, the pump wavelength at degeneracy is found to increase as the ridge width decreases. The reason for this is that the effective indices decrease as the ridge width becomes smaller, and this decrease is stronger for signal and idler modes (which are more sensitive than the pump to a width reduction, due to their longer wavelength). As the effective indices of signal and idler decrease, also the pump effective index at degeneracy has to do the same for phase matching to hold: this explains why the pump wavelength at degeneracy increases. Since this effect is significant below an 8-µm ridge width and most nonlinear applications require high power densities, 2-D effects are relevant. To stress this, the dashed line in Fig. 10 enlightens the outcome of an incorrect calculation carried out with an insufficient number of mesh points. The comparison with the result of a proper simulation indicates that the numerical precision is by no means a secondary issue.

This point is further addressed in Fig. 11, where the computed pump wavelength at degeneracy is graphed versus the number of points used in the 2-D mesh (in this case, ridge width and height were taken equal to 5 and 3 µm, respectively). The numerical convergence is clearly not satisfactory for less than $8 \times 10^3$ mesh points.

Finally, as illustrated in Fig. 12 for a constant width of 5 µm, the pump wavelength at degeneracy $\lambda_p^0$ increases as the ridge depth is augmented. This can be explained in two steps. Firstly, all effective indices decrease with an increasing depth, and this occurs more rapidly for signal and idler than for the pump. Secondly, as suggested by Fig. 3 in the case of a planar structure, as $\lambda_p^0$ increases the TM pump effective index decreases more rapidly than TE signal/idler does.

Therefore, $\lambda_p^0$ must increase such that the material dispersion compensates for the geometric effect. Note that the effect is much more relevant for TE₀₁ modes than for TE₀₀ modes, since the former is more sensitive to the lateral sidewalls of the ridge.

![](./images/812136233072328705_11.jpg)

Fig. 11. Pump wavelength at degeneracy, calculated for a ridge width W = 5 µm and an etching depth H = 3 µm, as a function of the number of mesh points. Typically, 8000–10 000 points are necessary for a satisfactory convergence.

![](./images/812136233072328705_12.jpg)

Fig. 12. Pump wavelength at degeneracy as a function of ridge depth, for a ridge width W = 5 µm (calculation performed with 8000 points).

The longer the waveguide, the more challenging it is to keep a uniform phase matching along propagation, and the more homogeneous the etching depth needs to be. In practice, in a photolithography/etching process, a longitudinally uniform etching depth is markedly more difficult to achieve than a uniform ridge width. The efficiency of the nonlinear interaction is proportional to $\text{sinc}^2(\Delta kL/2)$, where $L$ is the waveguide length and $\Delta k = k(\lambda_p) - k(\lambda_s) - k(\lambda_i)$ the wavevector mismatch. At degeneracy, $\Delta k = 2\pi\sigma(\lambda_p^0)\Delta\beta$, where $\sigma$ is the wavenumber and $\Delta\beta = \beta^{\text{TM}}(\lambda_p^0) - \beta^{\text{TE}}(2\lambda_p^0)$. The influence of a longitudinal inhomogeneity $\Delta k(z)$ on the conversion efficiency depends on the function $\Delta k(z)$, which can be random (e.g., in the case of thickness fluctuations), or deterministic (e.g., for a temperature gradient). Even with no assumptions on $\Delta k(z)$, one can reasonably assume that $\Delta k$ should not exceed $2/L$. For $L = 2$ mm, $\Delta k_{max} = 10$ cm⁻¹ is the maximum nonhomogeneity that can be tolerated. This leads to $\Delta\beta < 1.7 \times 10^{-4}$ for a 1065 nm pump wavelength. The above 2-D calculation allows to relate

![](./images/812136233072328705_13.jpg)

Fig. 13. Examples of effective index spectra for an nonoxidized GaAs-AlAs waveguide, for two temperatures: $T=15\ ^{\circ}\text{C}$ (solid line) and $T=35\ ^{\circ}\text{C}$ (dotted line).

this requirement on $\Delta\beta$ to a tolerance in etching depth homogeneity $\Delta H$. In our case, (where zeroth-order modes interact nonlinearly, with a 3-$\mu$m ridge width and an etching depth of 1 $\mu$m), we calculate that a uniformity as high as 3 nm is required in depth, i. e. of the order of a few GaAs atomic layers. This is beyond the state of the art in chemical or reactive ion etching, and explains the current interest for deeply etched waveguides [16]. Note that the sensitivity to depth can be reduced to zero in the case of a deeply etched waveguide, where the guided modes are entirely confined in the ridge. In this case the technological challenge is the fabrication of deeply etched waveguides with low losses.

## VI. TUNING-CURVE DEPENDENCE ON TEMPERATURE

Due to the temperature dependence of the refractive indices of each material in the multilayer, the waveguide effective indices are also expected to depend on temperature $T$. This permits to parametrically tune signal and idler even with a fixed pump. In order to model the thermal tunability of a parametric GaAs-Alox device, the AlGaAs index dependence on temperature, mainly due to the temperature dependence of its bandgap [11], need be precisely known or evaluated. In fact, Alox is an insulator rather than a semiconductor, and its refractive index is expected to vary negligibly with temperature. This is indeed the case for the well-known $\text{Al}_2\text{O}_3$, morphologically similar to Alox. The assumption that the temperature dependence of AlGaAs should be retained while the one of Alox can be neglected is verified by nonlinear measurements as a function of temperature, as reported hereafter.

Fig. 13 shows two $m$-line spectra of the waveguide at 1550.5 nm at different $T$, with each resonance corresponding to the effective index of a mode. [10] The temperature dependence of the effective indices can be appreciated in Fig. 14. Since [11] does not include any explicit temperature dependence for the indices, we endowed the former model only with the temperature effects on the AlGaAs energy gap. A far better agreement could be achieved between our data and Gehrsitz's model, [12] which agreed with our experimental $d\beta/dT$ values to better than $10^{-5}$. Once again, neglecting the thermooptic index variation of Alox proved to be appropriate.

![](./images/812136233072328705_14.jpg)

Fig. 14. Temperature dependence of the effective indices of an AlGaAs waveguide, for $\lambda=1550.5$ nm. The circles are experimental points obtained from the resonances in Fig. 13 and refer to the three lowest order TE modes. The solid lines represent the corresponding values predicted by Afromowitz's model (with an uncertainty of $\pm4\times10^{-3}$), and the dashed lines the predictions from Gehrsitz's model (with uncertainty $\pm1\times10^{-3}$).

![](./images/812136233072328705_15.jpg)

Fig. 15. Idler wavelength versus temperature in a DFG experiment [2], with a fixed pump at 1.32 $\mu$m and another tunable input around 1 $\mu$m. The experimental results are compared with a fit considering the sole variation of AlGaAs refractive index (keeping constant the Alox refractive index).

Additional validation was provided by experiments on difference-frequency-generation (DFG) and parametric-fluorescence. For DFG two near-infrared beams were simultaneously end-fire coupled in an oxidized multilayer waveguide: one wavelength was set at 1.32 $\mu$m, and the other was tuned around at 1 $\mu$m. [2]. Light of wavelength from 5.2 to 5.6 $\mu$m was generated by varying the waveguide temperature. This variation is illustrated in Fig. 15, and an excellent agreement is apparent with the calculated DFG wavelength assuming a constant index for Alox. The corresponding tuning curves, calculated for three different values of $T$, are displayed in Fig. 16. Obviously, the multilayer temperature need be kept stable: even far from degeneracy, where the idler (and signal) temperature dependence is weaker than at degeneracy, it amounts to 4 nm/K. Near degeneracy (where $\partial\lambda_p/\partial\lambda_{i,s}$ vanishes), good temperature control becomes mandatory.

The $T$ dependence of the pump wavelength at degeneracy is shown in Fig. 17. Again, the agreement between the experimental points and the calculation (with a constant Alox refrac-

![](./images/812136233072328705_16.jpg)

Fig. 16. Calculated tuning at various waveguide temperatures: $T=10^\circ$C (solid line), $T=30^\circ$C (dashed line), $T=50^\circ$C (dotted line).

![](./images/812136233072328705_17.jpg)

Fig. 17. Pump wavelength at degeneracy versus temperature: experimental data (dots) and calculation.

tive index) is excellent. At degeneracy we found a thermorefrac- tive coefficient of about 0.133 nm/K. Further insight is gained by measuring the variation of signal/idler wavelengths versus tem- perature, shown in Fig. 18 for $\lambda_p=1.064\mu$m. This provides the actual tunability of a device with a fixed pump wavelength. For a $\Delta T<10$ K, a change in signal/idler wavelength $>100$ nm is expected and experimentally observed, thereby demonstrating the large tunability of the device.

In summary, the thermorefractive behavior of our parametric waveguides is well explained by the AlGaAs refractive index variation, available with a good precision. This allows to predict the temperature dependence of both the parametric- fluorescence degeneracy point (Fig. 17) and the signal/idler wavelengths for a given pump (Fig. 18). Most importantly, the tunability of the parametric waveguides is found to be wide enough to cover a $0.3-\mu$m interval around $2\mu$m with $\Delta T=10$ K only, easily obtained with a Peltier element.

### VII. CONCLUSION

The sensitivity of parametric tuning in AlGaAs-Alox mul- tilayer waveguides has been investigated versus numerous parameters such as refractive indices, layer thicknesses, ridge shape and temperature. In particular, the analysis has pro- vided insightful estimates of the accuracies required to obtain the desired pump wavelength at degeneracy, as summarized in Table I. This work proves that, for an acceptable phase mismatch ($\Delta k=10$ cm$^{-1}$), the uniformity which is needed along the waveguide is a critical issue, because a typical threshold for destructive interference in the nonlinear process is $\mathrm{sinc}^2(\Delta kL/2)\approx0.5$. From the values in Table II, it stems that both temperature and GaAs thickness are critical. Despite the tight requirements, Fig. 19 shows that it is possible to obtain phase matched parametric fluorescence over several mm, as demonstrated by fitting the experimental spectrum with curves for various interaction-lengths. The best fit, obtained for $L=5$ mm, witnesses the good uniformity of the wave- guide. While our results were obtained around $\lambda_p=1.06\mu$m, a smaller impact of the parameter variation is expected for parametric processes further in the infrared. However, the qualitative conclusion would remain the same: the most sen- sitive parameter in form-birefringent structures for nonlinear frequency conversion is the thickness and homogeneity of the GaAs layer. Its control remains a challenge for present-day molecular beam epitaxy.

![](./images/812136233072328705_18.jpg)

Fig. 18. Signal/idler wavelengths versus temperature, for $\lambda_p=1.064\mu$m: experimental data (dots) and calculated curve.

<table>
<caption>TABLE I Variation of the Pump Wavelength at Degeneracy for Changes of Four Structure Parameters: Alox Thickness, GaAs Thickness, Ridge Width, and Temperature</caption>
<tr>
<th>$\frac{\partial\lambda_p^0}{\partial d_{Alox}}$</th>
<th>$\frac{\partial\lambda_p^0}{\partial d_{GaAs}}$</th>
<th>$\frac{\partial\lambda_p^0}{\partial W_{ridge}}$</th>
<th>$\frac{\partial\lambda_p^0}{\partial T}$</th>
</tr>
<tr>
<td>-3.5 nm/%</td>
<td>+5.2 nm/%</td>
<td>$3.10^{-3}$ nm/nm</td>
<td>0.133 nm/K</td>
</tr>
<tr>
<td>or</td>
<td>or</td>
<td></td>
<td></td>
</tr>
<tr>
<td>-1 nm/nm</td>
<td>+1.9 nm/nm</td>
<td></td>
<td></td>
</tr>
</table>

<table>
<caption>TABLE II Nonuniformities Inducing Local Variations of the Phase Mismatch $\Delta k=10$ cm$^{-1}$. $\Delta W_{ridge}$ is Given for $W=5\mu$m and $H=3\mu$m)</caption>
<tr>
<th>$\Delta d_{Alox}$</th>
<th>$\Delta d_{GaAs}$</th>
<th>$\Delta W_{ridge}$</th>
<th>$\Delta T$</th>
</tr>
<tr>
<td>0.3 nm</td>
<td>0.15 nm</td>
<td>100 nm</td>
<td>2 K</td>
</tr>
</table>

![](./images/812136233072328705_19.jpg)

Fig. 19. Parametric fluorescence spectra (open circles), for (top) $\lambda_p = 1059.4$ nm and (bottom) 1059.6 nm, in a typical parametric structure such as in Fig. 1. The three fitting lines assume interaction lengths of 3 (dashed line), 5 (solid line), and 7.6 mm (dotted line), respectively, (the latter was also sample length). The width of the parametric spectra depends on the interaction length.

## ACKNOWLEDGMENT

The authors would like to thank V. Ortiz, X. Marcadet (growth), and M. Calligaro (processing), Thales, Orsay, France, for their collaboration which resulted in the experimental data reported in the introduction.

## REFERENCES

[1] A. Fiore, V. Berger, E. Rosencher, P. Bravetti, and J. Nagle, "Phase matching using an isotropic nonlinear material," *Nature*, vol. 391, pp. 463-466, 1998.

[2] P. Bravetti, A. Fiore, V. Berger, E. Rosencher, J. Nagle, and O. Gauthier- Lafaye, "5.2-5.6 micron tunable source by frequency conversion in a GaAs based waveguide," *Opt. Lett.*, vol. 23, pp. 331-333, 1998.

[3] A. Fiore, S. Janz, L. Delobel, P. van der Meer, P. Bravetti, V. Berger, E. Rosencher, and J. Nagle, "Second harmonic generation at $\lambda = 1.06\ \mu$m in GaAs based waveguides using birefringence phase matching," *Appl. Phys. Lett.*, vol. 72, pp. 2942-2944, 1998.

[4] G. Leo, V. Berger, C. O. Yang, and J. Nagle, "Parametric fluorescence in AlGaAs waveguides," *J. Opt. Soc. Amer. B*, vol. 16, pp. 1597-1602, 1999.

[5] A. De Rossi, V. Berger, M. Calligaro, G. Leo, V. Ortiz, and X. Mar- cadet, "Parametric fluorescence in oxidized aluminum gallium arsenide waveguides," *Appl. Phys. Lett.*, vol. 79, pp. 3758-3760, 2001.

[6] P. G. Kwiat, K. Mattle, H. Weinfurter, A. Zeilinger, A. V. Sergienko, and Y. Shih, "New high intensity source of polarization entangled photon pairs," *Phys. Rev. Lett.*, vol. 75, pp. 4337-4341, 1995.

[7] L. A. Eyres, P. J. Tourreau, T. J. Pinguet, C. B. Ebert, J. S. Harris, M. M. Fejer, L. Becouarn, B. Gerard, and E. Lallier, "All-epitaxial fabri- cation of thick, orientation-patterned GaAs films for nonlinear optical frequency conversion," *Appl. Phys. Lett.*, vol. 79, pp. 904-906, 2001.

[8] A. De Rossi, N. Semaltianos, V. Berger, E. Chirlias, B. Vinter, and V. Ortiz, "Third order mode optically pumped semiconductor laser," *Appl. Phys. Lett.*, vol. 80, pp. 4690-4692, 2002.

[9] C. Balanis, *Advanced Engineering Electromagnetics*. New York: Wiley, 1989.

[10] G. Leo, C. Caldarella, G. Masini, A. De Rossi, G. Assanto, O. Du- rand, M. Calligaro, X. Marcadet, and V. Berger, "X-ray and optical char- acterization of multilayer waveguides," *Appl. Phys. Lett.*, vol. 77, pp. 3884-3886, 2000.

[11] M. A. Afromowitz, "Refractive index of GaAlAs," *Solid State Commun.*, vol. 15, pp. 59-63, 1974.

[12] S. Gehrsitz, F. K. Reinhart, C. Gourgon, and N. Herres, "The refractive index of $Al_x$Ga$_{1-x}$As below the bandgap: accurate determination and empirical modeling," *J. Appl. Phys.*, vol. 87, pp. 7825-7837, 2000.

[13] O. Durand, F. Wyckzisk, J. Olivier, M. Magis, P. Galtier, A. De Rossi, M. Calligaro, V. Ortiz, V. Berger, G. Leo, and G. Assanto, "Contraction of aluminum oxide thin layers in optical heterostructures," *Appl. Phys. Lett.*, vol. 83, pp. 2554-2556, 2003.

[14] F. Sfigakis, P. Paddon, V. Pacradouni, M. Adamcyk, C. Nicoll, A. R. Cowan, T. Tiedje, and J. F. Young, "Near-infrared refractive index of thick, laterally oxidized AlGaAs cladding layers," *J. Lightw. Technol.*, vol. 18, no. 2, pp. 199-202, Feb., 2000.

[15] K. J. Knopp, R. P. Mirin, D. H. Christensen, K. A. Bertness, A. Roshko, and R. A. Synowicki, "Optical constants of $(Al_{0.98}Ga_{0.02})_x$As$_{y}$ native oxides," *Appl. Phys. Lett.*, vol. 73, pp. 3512-3514, 1998.

[16] S. L. Rommel, J. H. Jang, W. Lu, G. Gueva, L. Zhou, I. Adesida, G. Pajer, R. Whaley, A. Lepore, Z. Schellanbarger, and J. H. Abeles, "Effect of $H_2$ on the etch profile of InP/InGaAsP alloys in $Cl_2$/Ar/ $H_2$ inductively coupled plasma reactive ion etching chemistries for photonic device fab- rication," *J. Vac. Sci. Tech. B*, vol. 20, pp. 1327-1330, 2002.

[17] D. Bouwmeester, J. W. Pan, K. Mattle, M. Eibl, H. Weinfurter, and A. Zeilinger, "Experimental quantum teleportation," *Nature*, vol. 390, pp. 575-579, 1997.

[18] J. W. Pan, D. Bouwmeester, M. Daniell, H. Weinfurter, and A. Zeilinger, "Experimental test of quantum nonlocality in three-photon Greenberger- Horne-Zeilinger entanglement," *Nature*, vol. 403, pp. 515-519, 2000.

[19] T. Tamir, Ed., *Guided-Wave Optoelectronics*, 2nd ed. Berlin, Ger- many: Springer Verlag, 1990.

Alfredo De Rossi was born in Rome, Italy, in 1971. He received the M.S. degree in electrical engineering from the Università La Sapienza, Rome, in 1997, and the Ph.D. degree in nonlinear optics from the "Università Roma III," Rome, in 2002.

In 1999, he joined the Corporate Research Laboratory of Thales Research and Technology (formerly Laboratoire Central de Recherches, Thomson-CSF), Orsay, France, in the framework of the European Commission funded project "OFCORSE." Since 2000, has been a permanent member of the Infrared Detec- tion Group. His work involves electromagnetic modeling of infrared detectors, the design of prototype monolithic laser-diode sources for quantum cryptog- raphy, and a research program on nonlinear optics in integrated semiconductor structures. He is author/coauthor of more than 20 papers and holds three patents.

Vincent Berger was born in Saint-Amand, France, in 1967. He graduated from the Ecole Normale Supérieure, Paris, France.

From 1990 to 2001, he worked in the Physics Laboratory of the Laboratoire Central de Recherches, Thales (formerly Thomson CSF), on optoelectronic de- vices such as midinfrared detectors and nonlinear optics in heterostructures (fre- quency conversion), including photonic bandgap materials. In 2000, he became a Professor at the University Denis Diderot-Paris 7, and is now the Head of the Quantum Phenomena and Materials Laboratory, University Paris 7. He intro- duced different schemes of phase matching nonlinear optical processes in semi- conductor waveguides, and for this work he received the Fabry-De Gramont award and the MIT Young Innovator award in 2002. He has published around 100 papers in international journals and has 15 patents.

Giuseppe Leo was born in Italy in 1966. He received the Laurea degree from the University of Rome I, Rome, Italy, and the Ph.D. degree at the University of Paris XI, Paris, France.

In 1992, he was an Assistant Professor in the Department of Electronic En- gineering at the University of Rome III, Rome, Italy, and became Associate Professor in 2001. During 2002-2003, he was an Invited Professor at the Uni- versity of Paris VII, Paris, France, where he became Professor of the Faculty of Physics in 2004. His scientific activity, often directed to applications [stays at CSELT (1994-1995) and Thales (1998-2001)], has been in optoelectronics and nonlinear optics, with a focus on semiconductor and $LiNbO_3$ integrated optics. His present interests at Paris VII are focused on optical parametric generation in AlGaAs heterostructures and waveguide diagnostics. He has been actively involved in several EU projects, and has authored about 85 publications.

Gaetano Assanto (M'99) received the Laurea degree in electronic engineering from the University of Palermo, Palermo, Italy, in 1981 and the Ph.D. degree in electronic and computer engineering from the Italian Ministry of Education in 1987.

From 1988 to 1990, he was Research Associate at the Optical Sciences Center, Tucson, AZ, and from 1990 to 1992, he was an Assistant Research Scientist at the Center for Research in Electro Optics and Lasers, University of Central Florida, Orlando. He is currently a Professor of Optoelectronics with the Department of Electronic Engineering, University "Roma Tre," Rome, Italy, and Head of the Nonlinear Optics and OptoElectronics Laboratory, Rome. He is a Topical Editor for the *Journal of the Optical Society of America B*. His current research interests include parametric effects for all-optical processing in III-V semiconductors and lithium niobate waveguides, quadratic spatial and gap solitons, Ge-on-Si detectors for the near infrared, and nonlinear optics in liquid crystals.

Prof. Assanto is a Fellow of the Optical Society of America, Chair of the Nonlinear Optics Technology Committee, and member of the IEEE Lasers and Electro-Optics Society.