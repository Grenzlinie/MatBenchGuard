# Modeling and Uncertainty Quantification of Nanofiber Enhanced Polymer Composite Materials with Functionally Graded Interphase Properties

M. Rouhi¹, M. Rais-Rohani²

Mississippi State University, Mississippi State, MS 39762

Micromechanical approaches are used in mathematical modeling of randomly distributed carbon nanofibers (CNF) in a thermoset polymer material. Both CNF waviness and CNF-matrix interphase properties are included in the model. The interphase mechanical properties are considered to vary as a function of the distance as in functionally graded materials. The effects of stochastic uncertainties on the overall properties of the composite material are represented using the probability theory. The uncertainties are propagated in calculating the axial buckling load of a thin-walled composite cylinder, which is then optimized for minimum material volume. The probabilistic optimization results are presented and discussed.

## I. Introduction

THE addition of nano-inclusions such as carbon nanofibers (CNF) to polymer matrix materials has been shown to significantly enhance the overall elastic properties of the resulting material called nano-enhanced matrix. One of the challenging aspects of using these advanced materials in industrial design applications is the accurate modeling of their mechanical responses. In recent years, many models have been developed to predict the properties of nano-enhanced polymer matrix materials; molecular dynamics simulation¹⁻² is one of the most accurate modeling approaches, but it is not suitable for solving large length-scale problems. On the other hand, finite element simulation with homogenized properties has been used successfully in modeling large length-scale problems, but it cannot accurately capture phenomena present at smaller length scales. Micromechanical methods, which are based on the work of Eshelby³, are among the modeling approaches that fall in between the previous two approaches with the capability to capture phenomena in relatively small scales as well as having sufficient computational efficiency to be used in large-scale problems.

An advantage of Eshelby-solution-based approaches is that one may manipulate the geometry (aspect ratios) of the ellipsoidal inclusion to obtain the elastic properties of the composite material for different types of inclusions (e.g., cylindrical fibers, elliptic or circular platelets, or spherical reinforcements). It should be noted that in using the Eshelby method the interaction among inhomogeneities (equivalent inclusions) is ignored, and consequently it only applies to reinforcement with relatively low volume fractions ($f << 0.1$) called "dilute" matrix-inclusion composites. For the case of relatively high volume fractions, there are several theoretical descriptions of elastic behavior of inclusion-matrix composites that explicitly account for collective interactions among inclusions. The Mori-Tanaka⁴⁻⁵ method is one of those micromechanical approaches that consider a weak interaction among the inclusions. It can estimate the elastic properties of a semi-dilute composite case up to a relatively high volume fraction ($f <= 0.3$).⁶

In an earlier effort, the authors and coworkers⁷ studied the influence of CNF reinforcements on mechanical (stiffness and strength) properties of a thermoset polymer matrix (vinyl ester) material through numerical modeling and simulation. In that paper, two approaches (general Mori-Tanaka and quasi-isotropic lamination approximation) were used to calculate the stiffness properties of a CNF reinforced polymer matrix. Both methods were basically based on the work of Eshelby and assumed perfect bonding between the inclusions and matrix with no interphase region between the constituents. However, some studies show that an interphase region may form as a three-dimensional region between the inclusions and matrix⁸ and play an important role in the mechanical performance of the composite materials. This interphase region may not be homogeneous and its properties may vary as a function

¹Graduate Research Assistant, Center for Advanced Vehicular Systems, Member AIAA.
²Professor, Department of Aerospace Engineering and Center for Advanced Vehicular Systems, Associate Fellow AIAA.


of distance from the vicinity of surface of the reinforcement materials in the matrix.⁹ So, one of the most challenging subjects in modeling the mechanical (stiffness and strength) properties of nano-enhanced materials has become the proper representation of properties in the interface/interphase region defining the boundary between the individual inclusions and the surrounding matrix. This region plays a crucial role in the load transfer from the matrix to the inclusions. Whether this region is a two-dimensional surface (interface) or a three-dimensional volumetric region (interphase) is very important in this regard. Another property of the inclusions that is very influential on the elastic properties of the nano-enhanced materials is their waviness. High waviness of CNF may drastically decrease the modulus enhancement of the matrix material so that the improvement in elastic properties due to addition of CNF is almost negligible.¹⁰

On the other hand the geometric and mechanical properties of the constituent materials are subject to random uncertainty. For instance, all the reinforcement materials (CNF) may not have the same aspect ratio, or the interphase region may not have constant thickness for all the nanofibers in the matrix. Hence, it is necessary to have a model that incorporates the random variability of the properties.

As an extension of our previous work⁷, three subjects are addressed in this paper: 1) the influence of the presence of three-dimensional nanofiber-matrix interphase as well as the waviness of nanofibers; 2) the effect of random variation in the material parameters on performance of structural components made of fiber-reinforced CNF-enhanced polymer composite materials; and 3) optimization under uncertainty of a hybrid composite structure made of conventional long fibers and nano-enhanced matrix materials.

In this paper, the general framework for modeling the stiffness properties of CNF enhanced composite materials is presented. Furthermore, the modeling of CNF waviness as well as the interphase region considering its anisotropy, such as in a functionally graded material, is discussed. The specific geometric and material properties treated as sources of random uncertainty are introduced and a probabilistic approach for modeling and propagation of uncertainty is presented. As an example, the elastic buckling of a hybrid composite cylinder made of glass fibers and CNF enhanced matrix is studied considering the effect of uncertainties in both material (nano-reinforced matrix and CNF volume fraction) and structural (laminate angles, fiber properties and volume fraction) levels.

## II. The Stiffness Properties of Nanofiber Enhanced Matrix with Perfect Bonding without Interphase

Assuming a perfect bonding between the inclusions and the matrix, one may use any of several micromechanical models to predict the overall stiffness of composite materials made of ellipsoidal inclusions in an elastic matrix. It is worth noting that the accuracy of those different approaches depends on the volume fraction and the level of interaction between the inclusions in a composite system. Mori-Tanaka, self-consistent and differential scheme are some of those micromechanical methods that are all based on the work of Eshelby.³

![](./images/814753486477459457_1.jpg)

Figure 1. Eshelby's cutting and welding procedure for a misfitting ellipsoidal inhomogeneity and the corresponding equivalent homogeneous inclusion.¹¹

Eshelby showed that if an elastic homogeneous ellipsoidal inclusion, surrounded by an infinite linear elastic matrix, is subjected to a uniform strain $\boldsymbol{e}^T$ (called the "eigenstrain", "transformation strain", "unconstrained strain", or "stress-free strain"), a uniform strain $\boldsymbol{e}^C$ is induced in the constrained inclusion, which is proportional to the induced unconstrained strain as

$$
\boldsymbol{e}^C = \mathbb{S} \boldsymbol{e}^T \tag{1}
$$


where $\mathbb{S}$ is the interior point Eshelby fourth-order tensor that depends solely on the geometry of the inclusion and the Poisson's ratio of the surrounding matrix. $^{3,12}$ The Eshelby tensor $\mathbb{S}$ basically relates the final constrained inclusion shape to the original shape mismatch between the matrix and the inclusion. $^{12}$ In Eq. (1), $\boldsymbol{e}^{\mathrm{T}}$ may be any kind of eigenstrain (e.g., thermal strain) that does not change the elastic constants of the inclusion and is uniform over the inclusion. For inhomogeneities embedded in a matrix, the concept of equivalent homogeneous inclusions is introduced to handle the mean field description of matrix-inhomogeneity composites. Figure 1 illustrates the equivalent inclusion procedure for a matrix-inhomogeneity system using Eshelby's cutting and welding exercises.

For a two-phase composite material, the Mori-Tanaka method estimates the effective stiffness tensor as

$$
\mathbb{L}^{M T}=\mathbb{L}_{0}+c_{1}\left\{\left(\mathbb{L}_{1}-\mathbb{L}_{0}\right) \mathbb{T}\right\}\left[c_{0} \mathbb{I}+c_{1}\{\mathbb{T}\}\right]^{-1}
\tag{2}
$$

where indices 0 and 1 represent matrix and reinforcing phase, respectively, $\mathbb{L}$ is the fourth-order stiffness tensor, $c$ is the volume fraction, $\mathbb{I}$ is the fourth-order identity tensor, and $\mathbb{T}$ relates the uniform strain in an inclusion embedded in an effective continuum to the average matrix strain. The curly brackets $\{\}$ are used to denote physical properties averaged over all possible inclusion orientations. For an ellipsoidal inclusion $\mathbb{T}$ may be calculated as

$$
\mathbb{T}=\left[\mathbb{I}+\mathbb{S} \mathbb{L}_{0}^{-1}\left(\mathbb{L}_{1}-\mathbb{L}_{0}\right)\right]^{-1}
\tag{3}
$$

where $\mathbb{S}$ is the fourth-order interior Eshelby tensor that only depends on the geometry of the inclusion and Poisson's ratio of the matrix. Having the volume fractions $(c)$ and elastic properties $(\mathbb{L})$ of all phases as well as the geometry of the inclusions $(\mathbb{S})$, one may implement the micromechanical model based on Eqs. (2) and (3).

In the case of non-aligned discontinuous fiber composites, it is necessary to average the stiffness tensor over all possible fiber orientations. Figure 2 shows a rotated ellipsoidal inclusion and the related Euler angles necessary to average the stiffness tensor over all possible directions.

In order to include the stiffness contribution from all orientations, $\mathbb{C}$ has to be transformed, multiplied by an orientation distribution function, and integrated over all possible orientations as follows $^{12,14}$

$$
\begin{aligned}
\left\{\mathbb{C}_{i j k l}\right\} & =\int_{0}^{2 \pi} \int_{0}^{2 \pi} \int_{0}^{\pi} g(\phi) a_{i p} a_{j q} a_{k r} a_{l s} \\
\mathbb{C}_{i j k l} & \sin (\phi) d \phi d \theta d \beta
\end{aligned}
\tag{4}
$$

where $g(\emptyset)$ is the orientation distribution function and $a_{i j}$ parameters are functions of Euler angles given as

$$
a_{i j}=\left\{\begin{aligned}
a_{11} & =\cos (\phi) \cos (\theta) \cos (\beta)-\sin (\theta) \sin (\beta) \\
a_{12} & =-\cos (\phi) \cos (\theta) \sin (\beta)-\sin (\theta) \cos (\beta) \\
a_{13} & =\sin (\phi) \cos (\theta) \\
a_{21} & =\cos (\phi) \sin (\theta) \cos (\beta)+\cos (\theta) \sin (\beta) \\
a_{22} & =-\cos (\phi) \sin (\theta) \sin (\beta)+\cos (\theta) \cos (\beta) \\
a_{23} & =\sin (\phi) \sin (\theta) \\
a_{31} & =-\sin (\phi) \cos (\beta) \\
a_{32} & =\sin (\phi) \sin (\beta) \\
a_{33} & =\cos (\phi)
\end{aligned}\right.
\tag{5}
$$

![](./images/814753486477459457_2.jpg)

Figure 2. A spatially oriented ellipsoidal inhomogeneity. $^{13}$

Maekawa et al. $^{15}$ used an incomplete Beta function for $g(\emptyset)$ to account for partially aligned inclusions. For the case of randomly oriented inclusions, $g(\emptyset)$ has a constant value$^{12}$

$$
g(\phi)=\frac{1}{8 \pi^{2}} \tag{6}
$$

The results shown in Figs. (3) and (4) are for a nano-enhanced matrix with CNF as the reinforcement material and vinyl ester resin as the matrix having the following elastic properties: $E_{0}=3.5$ GPa, $E_{1}=450$ GPa, and $v_{0}=v_{1}=$ 0.3.

Figure 3 illustrates the variation of the Young's modulus of the CNF enhanced vinyl ester as a function of CNF aspect ratio for different volume fractions using the Mori-Tanaka homogenization scheme. The stiffness appears to be highly influenced by the aspect ratio of CNF up to a (saturation) limit, after which there is no stiffness enhancement benefit for using CNF with higher aspect ratio.

Figure 4 shows the effect of CNF volume fraction on the overall stiffness of the composite with different CNF aspect ratios. At low volume fractions, the Mori-Tanaka scheme shows a nearly linear enhancement in stiffness with increasing CNF volume fraction that is much lower than that predicted by the simple rule of mixture (upper bound).

![](./images/814753486477459457_3.jpg)

Figure 3. The variation of Young's modulus (using 3-D Mori-Tanaka homogenization scheme) as a function of aspect ratio.

![](./images/814753486477459457_4.jpg)

Figure 4. The variation of Young's modulus (using 3-D Mori-Tanaka homogenization scheme) as a function of volume fraction.

### III. The Stiffness Properties of Nanofiber Enhanced Matrix using Multi-Inclusion Method

One of the major shortcomings of the micromechanical methods assuming perfect bonding between the inclusion and matrix (such as Mori-Tanaka) is that the interaction between the inclusions and their immediate surrounding matrix material of different elasticity is not directly included in the model. $^{16}$ The double-inclusion method may be used when the elastic properties of the matrix is significantly different from that of inclusions. As shown in Fig. 5, in

![](./images/814753486477459457_5.jpg)

Figure 5. A self-similar double-inclusion model.

![](./images/814753486477459457_6.jpg)

Figure 6. A four-phase multi-inclusion embedded in infinite domain.

double-inclusion method a distinct interphase region between an inclusion and the surrounding matrix is assumed and the overall elasticity of the composite is averaged based on the material and geometric properties of the constituent materials. $^{16}$

However, the double-inclusion model can be generalized to a multi-inclusion method $^{16}$ in which an ellipsoid, V, contains a nested series of ellipsoids, $\Omega_{\alpha}(\alpha=1,2,..., \mathrm{m})$, such that $\Omega_{1} \subset \Omega_{2} \subset... \subset \Omega_{\mathrm{m}} \equiv \mathrm{V}$ as it shown in Fig. 6.

Multi-inclusion method estimates the overall properties of the composite as:

$$
\overline{\mathbf{C}}^{\mathrm{MP}}=\mathbf{C}:\left\{\mathbf{1}^{(4 \mathrm{s})}+\sum_{\boldsymbol{\alpha}=1}^{\mathbf{n}} \mathbf{f}_{\boldsymbol{\alpha}}\left(\mathbf{S}^{\Omega}-\mathbf{1}^{(4 \mathrm{s})}\right):\left(\mathbf{A}^{\boldsymbol{\alpha}}-\mathbf{S}^{\Omega}\right)^{-1}\right\}:\left\{\mathbf{1}^{(4 \mathrm{s})}+\sum_{\boldsymbol{\alpha}=1}^{\mathbf{n}} \mathbf{f}_{\boldsymbol{\alpha}} \mathbf{S}^{\Omega}:\left(\mathbf{A}^{\boldsymbol{\alpha}}-\mathbf{S}^{\Omega}\right)^{-1}\right\}^{-1}
$$

$$
\mathbf{A}^{\boldsymbol{\alpha}} \equiv\left(\mathbf{C}-\mathbf{C}^{\boldsymbol{\alpha}}\right)^{-1}: \mathbf{C}
$$

where $\mathbf{C}$ is the fourth-order stiffness tensor, $\mathbf{1}^{(4 \mathrm{s})}$ is the $4^{\text {th }}$ order identity tensor, $\mathrm{f}_{\alpha}$ is the volume fraction of the $\alpha$ interphase region, $\mathbf{S}$ is the Eshelby tensor that depends on the geometry of the inclusion and $\alpha$ is the subdivision index.

Since Eq. (7) as a result of the multi-inclusion method gives the properties for aligned inclusion case, the resulting stiffness needs to be averaged in all orientations for the case of randomly distributed inclusions (see Eqs. (4) and (5)).

### A. Modeling the Functionally Graded Interphase

As stated earlier, some studies⁹ show that the interphase region may not be homogeneous with properties that vary as a function of distance from the vicinity of surface of the inclusions (fibers) as shown in Fig. 7. If the interphase region is not homogeneous, the double inclusion method may not be used to predict the overall properties of the composite since it is not constant through the region. However, the multi-inclusion method can be used to approximate the varying properties of the interphase. As shown in Fig. 8, a piecewise-constant-properties approximation technique is used for the interphase region in which the properties are varying similar to functionally graded materials.¹⁷,¹⁸

One way to model the variation in an interphase property (e.g., Young's modulus, Poisson's ratio) is by using¹⁷,¹⁸

$$
\mathrm{P}=\mathrm{P}_{\text {in }}+\left(\mathrm{P}_{\text {out }}-\mathrm{P}_{\text {in }}\right)\left(\frac{\mathrm{X}}{\mathrm{N}}\right)^{\mathrm{n}}
$$

where $\mathrm{P}, \mathrm{P}_{\text {in }}, \mathrm{P}_{\text {out }}$ represent the property of interest in the interphase subdivision at a nondimensional distance $\mathrm{x}$ from the outer surface of the inclusion, $1^{\text {st }}$ interphase subdivision and last or Nth interphase subdivision, respectively. The parameter $n$ is a constant power determining the functionality of the graded property. By changing $n$, one may control the rate of variation of the interphase property from $\mathrm{P}_{\text {in }}$ to $\mathrm{P}_{\text {out }}$ in a piecewise constant fashion.

![](./images/814753486477459457_7.jpg)

**Figure 7. Graded characteristic of interphase region captured by indentation test.⁹**

![](./images/814753486477459457_8.jpg)

**Figure 8. A piecewise constant model for functionally graded interphase.**

A MATLAB code was developed using the multi-inclusion technique described above. The code is able to calculate the overall stiffness properties of the composite based on inputs that include the mechanical properties and the volume fraction of the constituent materials (inclusion and matrix), the thickness of the interphase, as well as the power law intensity factor "n" controlling the functionality of the graded properties of the interphase as defined in Eq. (8). For the sake of verification, the case that the properties of the interphase are equal to the matrix properties was examined and the results were found to match exactly those shown in Figs. (3) and (4). Table 1 shows the effective elastic modulus of a short fiber reinforced polymer with different elastic properties of the interphase.

Table 1. Effective elastic modulus for different interphase thicknesses and elastic moduli with $E_f = 240$ GPa, $E_0 = 3.15$ GPa, AR = 100, Volume fraction = 0.0382.

<table>
  <thead>
    <tr>
      <th>Interphase modulus<br>$E_i$ (GPa)</th>
      <th>Effective modulus<br>$E_c$ (GPa)</th>
      <th>IPTR*</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No Interphase</td>
      <td>4.78</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td rowspan="3">100</td>
      <td>4.90</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>5.72</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>7.15</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td rowspan="3">2.0</td>
      <td>4.72</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td>4.67</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>4.57</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

*IPTR: Interphase thickness ratio = Interphase thickness/ fiber radius

As expected, for interphases with greater elastic moduls than the matrix, the overall stiffness of the composite increases by increasing the thickness of the interphase whereas for those interphases with smaller elastic modulus than the matrix, the overall stiffness decreases by increasing the thickness of the interphase.

## IV. Modeling of Wavy Fibers in Nano-Reinforced Matrix

Experimental observations of polymers reinforced by carbon nanotubes (CNT) via Scanning Electron Microscope (SEM) and Transmission Electron Microscope (TEM) has revealed that the embedded CNT remain highly curved when dispersed in a polymer. $^{19-21}$ This is to be expected when considering the very high aspect ratio and low bending stiffness of CNT and CNF. Hence, it is necessary to consider the waviness of CNF to have a better understanding of the mechanical behavior of CNF reinforced composite materials. It is also needed to have a more accurate quantitative model of the mechanical behavior of these composite materials.

Waviness has been modeled using different analytical and hybrid approaches. In analytical approaches $^{10,22}$, wavy embedded fiber is isolated and its effective reinforcing modulus ($E_{ERM}$) is calculated. This is a representative value that accounts for the reduction in reinforcement provided by the wavy fiber compared with the reinforcement provided by a straight fiber (of modulus $E_f$). $^{23,24}$ Therefore, while the modulus of the fiber $E_f$ is a material property, $E_{ERM}$ ($E_{ERM} \leq E_f$) is a material parameter influenced by the geometry of the wavy fiber.

Figure 9 shows how the planar sinusoidal waviness of a fiber drastically decreases $E_{ERM}$. This effective property can then be used in any micromechanical model as an equivalent value for the true CNF/CNT modulus. Fisher (2002) showed that the analytical model is only useful when the modulus of the straight nanotube $E_{NT}$ is much larger than the modulus of the matrix $E_{matrix}$. When this criterion is not satisfied (i.e., $E_{NT} / E_{matrix}$ <1000), a new model/analysis is needed to account for the lateral constraint (bonding between the inclusion and the matrix) imposed on the CNT by the surrounding matrix. In a more general case of fibers with three-dimensional waviness, Shady and Gowayed $^{22}$ assumed a helical geometry for the fibers and used the same methodology to solve for the equivalent stiffness. Figure 10 reveals their results for the effective stiffness compared with the one using Fisher's assumption $^{10}$ of planar sinusoidal geometry for wavy fibers. They concluded that underprediction of the effective stiffness based on their helical assumption of the waviness is lower compared to the sinusoidal geometry assumption for the waviness.

![](./images/814753486477459457_9.jpg)

Figure 9. (a) Comparison of finite element and analytical solutions for the effective modulus of a free standing wavy fiber, (b) Schematic of a free standing sinusoidal wavy fiber.¹⁰

![](./images/814753486477459457_10.jpg)

Figure 10. (a) The effect of curvature on the ratio of the modulus of effective fiber to the modulus of the fiber (on a semi-log scale) for Fisher's 2D analytical model¹⁰ and 3D modified fiber model²², (b) the geometry of a helical wavy fiber in matrix, $\gamma = \frac{1}{2}|(2\pi i)-2\pi|$.

In hybrid approaches (computational/micromechanical)²³,²⁴, the wavy CNF/CNT is embedded in a matrix material and a 3-dimensional finite element model is created to model the effectiveness of the wavy inclusion when it is perfectly bonded to the matrix. The effective modulus of the finite element cell is then related to $E_{ERM}$ based on the volume fraction of the inclusion. The resulting $E_{ERM}$ is used in conventional micromechanical techniques such as Mori-Tanaka scheme to calculate the modulus of the composite material. Figure 11 shows the finite element model and the results for equivalent stiffness of a sinusoidal wavy nanotube in matrix using hybrid method.¹⁰

Since the hybrid method, unlike the analytical approaches, considers the effect of bonding between the wavy fiber and its surrounding matrix, it predicts the effective stiffness by better estimating the equivalent stiffness of the wavy fibers.

![](./images/814753486477459457_11.jpg)

Figure 11. (a) $E_{ERM}$ as a function of nanotube waviness ratio (a/$\lambda$) for different ratios of phase moduli ($\lambda$/d = 100, $E_{matrix}$ = 1 GPa) and (b) finite cell model of the embedded wavy nanotube. $^{10}$

## V. Modeling of Random Properties

Because of many factors, mainly due to manufacturing and process imperfections, the geometric and mechanical properties of the constituents in nano-enhanced composite materials are subject to random uncertainty. For instance, all the CNF may not have the same aspect ratio, or the interphase region may not have constant thickness for all the CNF in the matrix. Thostenson and Chou$^{25}$ have used high-resolution TEM micrographs to measure the structural dimensions for quantifying both the distribution of CNT diameter and wall structure. Figure 12 shows a TEM micrograph of a multi-wall CNT (MWCNT) indicating the outer ($d$) and inner ($d_i$) diameter as well as a histogram for the nanotube outside diameter distribution.

![](./images/814753486477459457_12.jpg)

Figure 12. (a) Diameter distribution of MWCNT taken from measurements of (b) TEM micrographs. $^{25}$

Although some research has been conducted for quantifying the uncertainty in nano-inclusion structures and geometries (as distribution)$^{25,26}$, we have not been able to find any reports of research on the effect of these uncertainties on design of structures made of or containing nano-enhanced materials.

Hence, it is necessary to have a model that incorporates the variability of the properties in nano-enhanced composite materials. Furthermore, it is necessary to propagate these uncertainties from their root sources through the calculation of elastic properties of the material to determine the extent of variability in responses of the structural component made of such advanced materials. Since we do not have experimental data describing the variability of the influential parameters, we prescribe distribution function for each random variable in our modeling inputs as given in Table 2. The material-level random variables include but are not limited to CNF volume fraction and waviness, as well as interphase thickness and properties gradation factor. The variation of these material parameters may appear in the outputs of the micromechanical material model (stiffness and strength) in the form of a

distribution instead of deterministic output values. At the structural level, the design variables are the geometric parameters of the structure.

Some properties that may not have any significant variations, such as matrix elastic properties ($E_m = 3.5$ GPa, $v_m$ = 0.3) and CNF Poisson's ratio ($v_f = 0.3$), are considered deterministic and constant. The elastic properties of the innermost and outermost layers of the interphase ($E_{I-in}$ and $E_{I-out}$) are assumed to be equal to those properties of CNF and matrix, respectively. Therefore, other than the thickness (via IPTR) and the degradation factor of the property variation in the interphase region (via n), the uncertainty within the properties of the interphase (via $E_{I-out}$) is considered due to the uncertainties in $E_f$.

Table 2. Probabilistic values of the random variables influencing the overall properties of the composite in small length scale

<table>
  <thead>
    <tr>
      <th>Random<br>variable</th>
      <th>CNF Volume<br>Fraction</th>
      <th>$E_f$ (GPa)</th>
      <th>n (Interphase<br>gradation factor)</th>
      <th>Interphase Thickness<br>Ratio (IPTR)</th>
      <th>Waviness<br>($\lambda$)</th>
      <th>Waviness<br>(a)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean Value</td>
      <td>0.01</td>
      <td>450</td>
      <td>1</td>
      <td>0.5</td>
      <td>150</td>
      <td>50</td>
    </tr>
    <tr>
      <td>Standard<br>Deviation</td>
      <td>0.003</td>
      <td>100</td>
      <td>0.25</td>
      <td>0.05</td>
      <td>30</td>
      <td>15</td>
    </tr>
    <tr>
      <td>Output</td>
      <td>E_Composite (GPa)</td>
      <td>v_Composite</td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td>Mean Value</td>
      <td>3.92</td>
      <td>0.293</td>
      <td colspan="4"></td>
    </tr>
    <tr>
      <td>Standard<br>Deviation</td>
      <td>0.194</td>
      <td>0.002</td>
      <td colspan="4"></td>
    </tr>
  </tbody>
</table>

Using a Monte Carlo simulation with 1000 samples, the results for the effective properties of the nano-enhanced matrix are found to be those given in the bottom two rows of Table 2.

Having the uncertain elastic properties of the nano-reinforced matrix material, we are able to propagate them to the overall elastic properties of a single lamina made of such matrix and conventional fibers (E-glass in our case). To this end, we have used the rule of mixtures to calculate the ply properties made of E-glass and nano-enhanced matrix. It should be noted that there are some additional uncertainties in macroscale which may affect the ply/laminate properties including the E-glass elastic properties, the volume fraction of the fibers, and ply angles. Table 3 shows the results of 1000 Monte Carlo simulations considering the assumed uncertainties within the above properties in a [45/-45/90/90] E-glass vinyl-ester composite laminate.

Table 3. Probabilistic values of the random variables influencing the overall properties of the composite laminate in large length scale

<table>
  <thead>
    <tr>
      <th>Random variable</th>
      <th>Fiber (E-glass) Volume<br>Fraction</th>
      <th>$E_f$ x$10^6$ (GPa)</th>
      <th>$\theta_{45/-45}$ (deg)</th>
      <th>$\theta_{90/90}$ (deg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean Value</td>
      <td>0.4</td>
      <td>72.4</td>
      <td>45/-45</td>
      <td>90/90</td>
    </tr>
    <tr>
      <td>Standard<br>Deviation</td>
      <td>0.05</td>
      <td>6.9</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <td>Output</td>
      <td>On-axis modulus $E_1$ (GPa)</td>
      <td>Off-axis modulus $E_2$ (GPa)</td>
      <td>$G_{12}$ (GPa)</td>
      <td>$v_{12}$</td>
    </tr>
    <tr>
      <td>Mean Value</td>
      <td>29</td>
      <td>6.4</td>
      <td>4.8</td>
      <td>0.26</td>
    </tr>
    <tr>
      <td>Standard<br>Deviation</td>
      <td>4.6</td>
      <td>0.58</td>
      <td>0.028</td>
      <td>0.004</td>
    </tr>
  </tbody>
</table>

9
American Institute of Aeronautics and Astronautics

### VI. Buckling Analysis

For uncertainty propagation, we consider the axial buckling response of a thin-walled circular cylinder under uniform axial compression with the loaded edges clamped as shown in Fig. 13.

The cylinder is assumed to have a filament wound shell consisting of four unidirectional layers [45/-45/90/90] with each layer made of "E-glass/CNF-reinforced vinyl-ester" with statistical properties shown in Tables 2 and 3.

The computational model used treats the circular cylinder as a semicircular shell with the unloaded edges having symmetric boundary conditions and the loaded edges treated as clamped as shown in Fig. 14. This model falls under the general category of thin-shell structures with the displacement field described by the first-order shear deformation theory formulated as

$$
\begin{align*}
u(x,y, z) &= u_0(x,y) + z\phi_x (x,y) \\
v(x, y,z) &= v_0(x, y) + z\phi_y(x,y) \\
w(x, y,z) &= w_0(x, y)
\end{align*}
\tag{9}
$$

where $u_0, v_0, w_0$ are the mid-plane displacements in $x, y, z$ directions (see Fig. 14), respectively, and $\phi_x, \phi_y$ describe rotations about the y and x axes, respectively. The strain-displacement relations are based on Sanders-Koiter shell theory.

To obtain the critical buckling load, the displacements $u_0, v_0, w_0$ and rotations $x, y$ are approximated by different Ritz series with Legendre polynomials used as the interpolation functions such that the essential boundary conditions are satisfied. Then through the application of the principle of minimum total potential energy, the critical buckling load is found by solving the eigenvalue problem for the critical load factor.²⁷

![](./images/814753486477459457_13.jpg)

Figure 13. Structural model of the thin-walled composite cylinder.²⁷

![](./images/814753486477459457_14.jpg)

Figure 14. Computational model for circular cylinder in buckling.²⁷

A computer implementation of the described analysis procedure developed by Jaunky and Knight²⁸ is used to generate the necessary response samples of buckling loads.

### VII. Optimization under Uncertainty of a Composite Cylinder under Axial Loading

A circular cylinder with the overall elastic properties of the composite materials defined in Tables 2 and 3 is optimized for minimum volume (or weight) subject to a probabilistic constraint on the buckling load defined as

$$
\begin{align*}
\text{Min.} \quad &\text{Volume} \\
\text{s.t.} \quad &\text{P }[\text{Pcr/Volume} \leq (\text{Pcr/Volume})_0] < \text{P}_\text{fo} \\
&0.006 \text{ in} \leq \text{t}_{45} \leq 0.014 \text{ in} \\
&0.006 \text{ in} \leq \text{t}_{90} \leq 0.014 \text{ in} \\
&6 \text{ in} \leq \text{r} \leq 10 \text{ in}
\end{align*}
\tag{10}
$$


where Pcr, $P_{f0}$, r, $t_{45}$, and $t_{90}$ are the buckling load, prescribed probability of failure, mean radius of the cylinder, thickness of 45/-45 plies, and thickness of 90/90 plies, respectively. The cylinder has a fixed height of 14 in. Therefore, the design variables are r, $t_{45}$, and $t_{90}$ with (Pcr/Volume)$_0$ = 450 lb/in$^3$.

The challenging part of the optimization problem in Eq. (10) is the lack of an analytical function for the probabilistic constraint. To alleviate this problem, we relied on design and analysis of computer experiments to develop an analytical surrogate model which can estimate the probability of failure in terms of the design variables while considering the influence of the random variables affecting the material properties.

Using a uniform random sampling, we generated a population of twenty-five design points ($\textbf{DV}_1$ to $\textbf{DV}_{25}$) with each of the three design variables taking random values within the specified bounds in Eq. (10). In addition, we generated a population of 250 samples of random variables ($\textbf{RV}_1$ to $\textbf{RV}_{250}$) with each of the eleven variables taking random values based on their statistical properties in Tables 2 and 3. For each design point, we calculated 250 buckling loads corresponding to the random vectors $\textbf{RV}_1$ to $\textbf{RV}_{250}$. With random variables treated as input variables, a metamodel is constructed for the buckling load at each design point $\textbf{DV}_i$. Having an analytical metamodel for the buckling load, we performed $5\text{x}10^6$ Monte Carlo simulations to calculate the probability of failure $\textbf{P}_i$ for that specific design vector. After calculating the probability of failure $\textbf{P}_i$ for each set of design variables $\textbf{DV}_i$, we built another metamodel which relates the design variables to the probability of failure . This analytical surrogate model is the one we need to substitute in the optimization formulation (Eq. (10)) as the inequality constraint on the probability of failure for a specific buckling load capacity. Figure 15 shows the described bi-level metamodeling approach.

![](./images/814753486477459457_15.jpg)

Figure 15. The introduced bi-level metamodeling approach for design optimization under uncertainty of material properties in a hybrid composite cylinder.

### A. Surrogate Modeling

Radial Basis Functions (RBF) are used to establish surrogate models relating the response of interest (Specific Pcr or probability of failure) to the input variables. Given the normalized input variable vector $\boldsymbol{X}$ and response values at $n$ training points, an RBF approximation of the true response function can be found as

$$
f\left(\boldsymbol{X}\right)=\sum_{i=1}^{n} \lambda_{i} \varphi\left(\left\|\boldsymbol{X}-\boldsymbol{X}_{i}\right\|\right)
\tag{11}
$$

where $\boldsymbol{X}$ is the normalized vector of input variables, with $\boldsymbol{X}_i$ the corresponding value at the $i^{th}$ training point,
$r_{i}=\left\|\boldsymbol{X}-\boldsymbol{X}_{i}\right\|=\sqrt{\left(\boldsymbol{X}-\boldsymbol{X}_{i}\right)^{T}\left(\boldsymbol{X}-\boldsymbol{X}_{i}\right)}$ is the Euclidean norm representing the radial distance, $r$ from training point $\boldsymbol{X}$ to the sampling point or center $\boldsymbol{X}_i$, $\phi$ is a radial symmetric basis function, and $\lambda_{i}, i=1, n$ are the unknown interpolation coefficients. Equation (11) represents a linear combination of a finite number of radial symmetric basis functions. Here, we have used the multiquadric formulation of RBF $\phi(r)=\sqrt{r^{2}+c^{2}}$ with $c=0.01$.


To assess the overall accuracy of the constructed surrogate models, the average error statistics were considered. To estimate these error statistics, the accuracy of the RBF predictions were based on fitting a model using responses at $n$-1 training points and measuring the prediction at the $n^{th}$ point excluded from the set. The average of $n$ different surrogate models was used to obtain the associated error statistics. This offers maximum percentage of error = 1.37% for buckling load analyses and about 10% for the probability of failure predicted by the constructed meta-models.

## B. Results and Discussion
After finding an analytical form for the probabilistic constraint in Eq. (10), the resulting optimization problem can be solved using a conventional mathematical programming technique. For this particular case, we used sequential quadratic programming (SQP) tool in MATLAB software.

Figure 16 shows the optimum thickness of [45/-45] and [90/90] plies in the skin laminate of the composite cylinder in terms of the desired probability of failure. Failure in this problem is defined as the specific buckling load capacity (Pcr/Volume) less than $450\ \text{lb/in}^3$.

![](./images/814753486477459457_16.jpg)

Figure 16. The optimization results for the buckling problem.

The results in Fig. 16 show how the angle plies quantitatively should contribute more in carrying the axial load to avoid buckling of the hybrid composite cylinder. For the probability of failure less than a specific value (e.g., 0.3 in this case) the [90] plies should be thicker than their lower bound (0.006 in). This means that for the uncertainties defined by the random variables, the circumferential stiffness provided by the minimum thickness of [90] plies are not high enough to keep probability of failure less than 0.3. The fiber-direction properties of the plies are less prone to change by variability of matrix properties (coming from lower length scale uncertainties). Therefore, for low probabilities of failure, the [45/-45] plies' properties in circumferential direction of the cylinder are not high enough to guarantee the specific buckling load to be higher than the desired value. Therefore, the [90] plies should contribute more to keep the probability of failure less than the prescribed value. In all of the cases in Fig. 16, the optimum radius of the cylinder is its minimum value of 6 in.

![](./images/814753486477459457_17.jpg)

Figure 17. Minimum volume of the composite cylinder in terms of desired minimum probability of failure.

The radius of the composite cylinder as a result of the optimization problem did not change for different values of the probability of failure. Also as Fig. 16 reveals, summation of the optimum thicknesses of [45/-45] and [90/90] plies vary linearly so that it results in a linear variation of the minimum volume of the cylinder in terms of the probability of failure as shown in Fig. 17.

### VIII. Summary and Conclusions

In this paper, we presented micromechanical approaches to model the elastic properties of a CNF-enhanced matrix. Both CNF waviness and CNF-matrix interphase properties were included in the model. A piece-wise linear approximation along with multi-inclusion technique were used to consider the inhomogeneity of the interphase region. The nano-enhanced matrix combined with conventional long fibers was used to build a hybrid composite material for use in structural design applications. Stochastic uncertainties in different parameters of nano-enhanced matrix were modeled and propagated in determination of axial buckling response of a thin-walled circular cylinder made of E-glass/CNF-reinforced vinyl-ester composite materials. The small length scale uncertainties may come from the CNF mechanical properties, volume fraction of CNF, waviness of the CNF, properties of the interphase between CNF and the matrix and the functionally graded behavior of the interphase region. The large length scale uncertainties may come from the E-glass effective (wetted) volume fraction, ply angles and E-glass mechanical properties. These uncertainties were propagated for finding the overall elastic properties of the hybrid composite cylinder. Using a bi-level metamodeling procedure, the design variables (geometric properties of the composite cylinder) were related to the probability of failure of the cylinder in the form of an analytical surrogate model. Solving the resulting constrained optimization problem, we were able to calculate the optimum design values for the thickness and radius of a hybrid composite cylinder and quantify the required value for each design variable in terms of a prescribed maximum probability of failure in a buckling problem.

### Acknowledgments

This material is based on the work supported by the US Department of Energy under Award Number DE-EE0002323.

Disclaimer: This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor any of their employees, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe

13
American Institute of Aeronautics and Astronautics

privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof.

## References
¹Odegard, G. M., Gates, T. S., Nicholson, L. M., and Wise, K. E., "Equivalent-Continuum Modeling of Nano-Structured Materials," *Composites Science and Technology*, Vol. 62, No. 14, 2002, pp. 1869-1880.
²Odegard, G. M., Harik, V. M., Wise, K. E., and Gates, T. S., "Constitutive Modeling of Nanotube-Reinforced Polymer Composites," *Composites Science and Technology*, Vol. 63, 2003, pp. 1671-1687.
³Eshelby, J. D., "The Determination of the Elastic Field of an Ellipsoidal Inclusion, and Related Problems," Proc. Roy. Soc. London A, 241, pp. 376-396, 1957.
⁴Mori, T., and Tanaka, K., "Average Stress in Matrix and Average Elastic Energy of Materials with Misfitting Inclusions," *Acta Metal.*, Vol. 21, 1973, pp. 571-574.
⁵Benveniste, Y., "A New Approach to the Application of Mori-Tanaka's Theory in Composite Materials," *Mechanics of Materials*, Vol. 6, 1987, pp. 147-157.
⁶Friedrich, K., Fakirov S., and Zhang, Z. (Editors), *Polymer Composites: From Nano- to Macro-scale*, Springer, New York, 2005.
⁷Rouhi, M., Rais-Rohani, M., Lacy, T., Garg, M., & Abdi, F., "Mechanical Characterization of a Nanofiber Enhanced Polymer with Application to Composite Crush Tubes," 51st AIAA/ASME/ASCE/AHS/ASC Structures, Structural Dynamics, and Materials Conference, Orlando, FL, Apr 2010.
⁸Jancar, J., "Review of the role of the interphase in the control of composite performance on micro- and nano-length scales," *J. Mat. Sci.*, Vol. 43, No. 20, 2008, pp. 6747-6757.
⁹Gao, S. L. and Mader, E., "Characterization of interphase nanoscale property variations in glass fiber reinforced polypropylene and epoxy composites," *Composites A.*, Vol. 33, 2002, pp. 559-576.
¹⁰Fisher, F., "Nanomechanics and Viscoelastic Behavior of Carbon Nanotube Reinforced Polymers," PhD Dissertation, Northwestern University, 2002.
¹¹Withers, P. J., Stobbs, W. M., and Pedersen, O. B., "The Application of the Eshelby Method of Internal Stress Determination to Short Fiber Metal Matrix Composites, " *Acta metal.*, Vol. 37, No. 11, 1989, pp. 3061-3084.
¹²Mura, T., Micromechanics of Defects in Solids, Martinus Nijhoff Publishers, 1987.
¹³Huang, J. H., "Some Closed-Form Solutions for Effective Moduli of Composites Containing Randomly Oriented Short Fibers, " *Materials Science and Engineering A*, 315, 2001, pp. 11-20.
¹⁴Schjodt-Thomsen, J., and Pyrz, R., "The Mori-Tanaka Stiffness Tensor: Diagonal Symmetry, Complex Fiber Orientations and Non-Dilute Volume Fractions," *Composites Science and Technology*, Vol. 33, 2001, pp. 531-544.
¹⁵Maekawa, Z-I., Hamada, H., and Yokoyama, A., "Lamination Theory of Composite Material with Complex Fiber Orientation Distribution," Proc. Int. Conf. on Conceptual Structures (ICCS), pp. 701-714, 24-26 July 1989.
¹⁶Nemat-Nasser, S., and Hori, M., Micromechanics: Overall Properties of Heterogeneous Solids, Elsevier, Amsterdam, 1993.
¹⁷Reddy, J. N., "Analysis of Functionally Graded Plates," *Int. J. Numer. Method, Eng.*, Vol. 47, 2000, pp. 663-684.
¹⁸Ruhi, M., Angoshtari, A., and Naghdabadi, R., "Thermoelastic Analysis of Thick-walled Finite-length Cylinders of Functionally Graded Materials," *J Thermal Stresses* Vol. 28, 2005, pp. 391-408.
¹⁹Shaffer, M. S. P. and Windle, A. H., "Fabrication and Characterization of Carbon Nanotube/Poly (vinyl alcohol) Composites," *Advanced Materials*, Vol. 11, No. 11, 1999, pp. 937-941.
²⁰Vigolo, B., Penicaud, A. P., Couloun, C., Sauder, C., Pailler, R., Journet, C., et al., "Macroscopic Fibers and Ribbons of Oriented Carbon Nanotubes," *Science*, Vol. 290, 2000, pp. 1331-1334.
²¹Qian, D., Dickey, E. C., Andrews, R. and Rantell, T., "Load Transfer and Deformation Mechanisms in Carbon Nanotube-Polystyrene Composites," *Appl. Phys. Lett.*, Vol. 76, No. 20, 2000, pp. 2868-2870.
²²Shady, E. and Gowayed, Y., "Effect of Nanotube Geometry on the Elastic Properties of Nanocomposites," *Composites Science and Technology*, Vol. 70, 2010, pp. 1476-1481.
²³Chisholm, N., and Brinson L. C., "Fiber Waviness in Nanotube-reinforced Polymer Composites—I: Modulus Predictions Using Effective Nanotube Properties," *Composites Science and Technology*, Vol. 63, No. 11, 2003, pp. 1689-1703.
²⁴Bradshaw, R. D., Fisher, F. T. and Brinson L. C., "Fiber Waviness in Nanotube-reinforced Polymer Composites—II: Modelling via Numerical Approximation of the Dilute Strain Concentration Tensor," *Composites Science and Technology*, Vol. 63, No. 11, 2003, pp. 1705-1722.
²⁵Thostenson, E. T. and Chou,. T. W., "On the Elastic Properties of Carbon Nanotube-Based Composites: modeling and characterization," *J Phys D*, Vol 36, No. 5, 2003, pp. 573-82.
²⁶Thostenson, E. T., Li, W. Z., Wang, D. Z., Ren, Z. F., and Chou, T. W., "Carbon Nanotube/Carbon Fiber Hybrid Multiscale Composites", *Journal of Applied Physics*, Vol. 91, No. 9, 2002, pp. 6034-37.

14
American Institute of Aeronautics and Astronautics

$^{27}$Rais-Rohani, M., "Reliability Sensitivity Analysis and Design Optimization of Composite Structures Based on Response Surface Methodology," NASA Report, 2003.

$^{28}$Jaunky, N. and Knight, N., "An Assessment of Shell Theories for Buckling of Cylindrical Panels," *International Journal of Solid Structures*, Vol. 36, 1999, pp. 3799-3820.

---

15
American Institute of Aeronautics and Astronautics