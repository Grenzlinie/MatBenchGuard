# Computational analysis of progressive failure in a notched laminate including shear nonlinearity and fiber failure

F.P. van der Meer $^{a, *}$, C. Oliver $^{b}$, L.J. Sluys $^{a}$

$^{a}$ Delft University of Technology, Faculty of Civil Engineering and Geosciences, PO Box 5048, 2600 GA Delft, The Netherlands
$^{b}$ ENS Cachan, Department of Civil Engineering, 61 Avenue du Président Wilson, 94235 Cachan, France

---

## ARTICLE INFO

**Article history:**
Received 2 November 2009
Received in revised form 6 January 2010
Accepted 8 January 2010
Available online 15 January 2010

**Keywords:**
A. Laminate
B. Fracture
B. Nonlinear behavior
C. Computational mechanics
C. Damage mechanics

---

## ABSTRACT

A computational model for mesolevel analysis of progressive laminate failure is presented. A previously developed discrete model for mesh independent representation of matrix cracks is combined with continuum descriptions for fiber failure and matrix nonlinearity. For fiber failure, a continuum damage model is introduced and a phenomenological damage/plasticity law is used for the shear nonlinearity. Special attention is paid to the application of the dissipation based arclength method to these models, where the presence of residual stresses is also taken into account. With the analysis of a notched cross-ply laminate the importance of the different components of the model to capture the complete failure process correctly is exemplified.

© 2010 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

Reliable prediction of failure in laminates is difficult because different failure processes may occur and interact. Subcritical damage may cause significant redistribution of stresses and influences the load level at which final failure occurs. Therefore, there is need for models with which the complete failure process can be simulated. This paper deals with a computational model in which matrix cracking, delamination, fiber failure and matrix shear nonlinearity are represented. It is argued that, together, these allow for complete failure analysis.

For matrix cracking, the fact that cracks are necessarily oriented in fiber direction makes a discontinuous approach to failure favorable [1]. It is possible to use interface or spring elements for this [2–4]. However, this requires that the crack location is specified in advance and complicates mesh generation. Therefore, a mesh-independent representation of matrix cracks is to be preferred. This has been done with a partition of unity based approach with higher order shape functions by larve et al. [5,6] and with the phantom node method by Ling et al. [7] and Van der Meer and Sluys [8].

Delamination can be modeled with interface elements. Several sound descriptions for the traction–separation law have been proposed [9–11,4]. It has been shown that, when each ply is modeled with a single layer of solid elements, the interaction between delamination and matrix cracking can be captured well in a framework with the phantom node method for matrix cracking and standard interface elements for delamination [12].

In this paper, this framework is extended with two nonlinear continuum models, one for fiber failure and the other for shear nonlinearity. For both models, the fact that cohesive matrix cracks may appear, demands care for the interaction between the material models. In the following section, the description for matrix cracking and delamination is reiterated briefly. Then, the models for fiber failure and shear nonlinearity are introduced. Next, an extension of the employed arclength method is presented. And finally, the model is applied to the case of a centrally notched cross ply plate. The results are compared with experimental observations from literature and the influence of different model features on the results is investigated.

## 2. Matrix cracking and delamination

Matrix cracking is modeled with the phantom node method [13–15] a variation to the eXtended Finite Element Method [16]. This method allows for representation of cracks as real discontinuities in the displacement field without having to mesh them. Initiation and propagation of cracks is handled with a stress based criterion. The crack direction is set equal to the fiber direction, which allows for realistic representation of matrix cracks. Difficulties that continuum models have with predicting the crack orientation (see Van der Meer and Sluys [1]) are thus circumvented.

---

* Corresponding author. Tel.: +31 15 278 7770; fax: +31 15 278 5767.
E-mail address: f.p.vandermeer@tudelft.nl (F.P. van der Meer).

0266-3538/$ - see front matter © 2010 Elsevier Ltd. All rights reserved.
doi:10.1016/j.compscitech.2010.01.003

Because the direction of crack propagation is independent of the stress field, proper mixed mode behavior is of particular importance in this context. This is a source of problems when working with an initially rigid cohesive model, i.e. a traction-separation law that starts from zero crack opening with nonzero traction. Descriptions with a finite initial stiffness that are generally used in interface elements cannot be applied because the discontinuity is introduced during the computation. In [8] we proposed to constrain the cohesive law with a bulk stress term. Another solution is proposed by Hille et al. [17], namely to start from a traction separation relation with a finite initial stiffness and to shift this relation such that the traction for zero crack opening is equal to the traction at crack initiation. For simple cases both approaches give similar results, but in our experience, the solution by Hille et al. [17] results in a somewhat more robust model for large computations. The results presented in this paper were obtained with the mixed mode damage law as developed by Turon et al. [11], which has a finite initial stiffness, in combination with the shift of the origin as proposed by Hille et al. [17].

For delamination a similar bilinear damage law is used. Each ply is modeled with a layer of plane stress elements, and they are connected with interface elements. In absence of out of plane degrees of freedom, the interface can only capture sliding and the mixed mode law therefore reduces to a single mode bilinear law [12].

The method for matrix cracking and delamination is illustrated in Fig. 1. For more details, we refer to [8,12].

### 3. Fiber failure

Fiber failure is modeled with a continuum damage approach, i.e. the stiffness is reduced gradually as strain increases, see Fig. 2a. Several considerations have led to the preference of a continuum damage model over a discontinuous approach here. Firstly, the compelling reason to use a discontinuous representation for matrix cracks, namely that the direction of crack propagation is governed by the microstructure rather than by the stress field, is not present in this case. Moreover, in the case in which a band with fiber failure grows in the direction of a matrix crack in an adjacent ply, the approach will have more difficulty in predicting this orientation. Prior to failure there is a band of elements in which stress is high. With a continuum model this will automatically lead to failure in this band, while it is not clear how this propagation direction should be extracted from the stress field in case it is modeled as a propagating discontinuity in the displacement field. Secondly, the continuum description fits the physics well, because fiber failure is a mechanism that results in a band in which material is damaged. This is due to the fact that fibers do not fail in a smooth plane, the process generally involves pull out of fibers from a zone with extensive matrix failure.

The remaining disadvantage of the continuum approach to failure is that regularization is needed. In this work the crack band method [18] is employed. This simple method, in which the constitutive behavior depends on the element size, leads to mesh size independent results, although limited dependence on the orientation of the mesh may still be present. More advanced nonlocal damage theories such as the implicit gradient model by Peerlings et al. [19] are theoretically more sound, but require a very fine mesh in the damaged zone.

![](./images/811809731004858368_1.jpg)

Fig. 1. Deformed mesh from an analysis with matrix cracking and delamination: a $[\pm45]_s$-plate with circular hole loaded in tension [8].

![](./images/811809731004858368_2.jpg)

Fig. 2. Schematic representation of the nonlinear continuum models.

The continuum damage approach to fiber failure is only applicable when failure is initiated due to a stress concentration, i.e. when it is not governed by the statistical distribution of the strength. Statistical size effects cannot be captured with the proposed model. Methods based on the assumption of a Weibull strength distribution and an integral over the volume can capture these size effects [20], but do not predict where failure will occur. The statistical effect is less important when the location of failure is given by a stress concentration and there is quasi-brittle progression of failure. It is for such cases that the continuum damage approach is particularly suitable.

Because the fiber failure mechanism does not leave the matrix intact, isotropic softening is assumed

$$
\boldsymbol{\sigma}=\left(1-\omega_{\mathrm{f}}\right) \mathbf{D}^{\mathrm{e}} \boldsymbol{\varepsilon} \tag{1}
$$

The isotropic damage variable $\omega_{\mathrm{f}}$ should be interpreted as degradation of the ply stiffness due to fiber failure instead of as pure fiber failure, which would have an orthotropic effect.

The force that drives the degradation, however, is orthotropic, motivated by the obvious fact that fiber failure only occurs due to loading in fiber direction. Puck and Schürmann [21] argued that the difference between available formulations is small as far as failure initiation is concerned. Therefore, for simplicity, maximum strain and maximum stress criteria are to be preferred. Of these, we consider the maximum strain criterion most appropriate for use as a state variable, because this largely rules out the influence of transverse strain on the amount of energy dissipated due to fiber failure. The state variable $\kappa_{\mathrm{f}}$ is defined as the time maximum of the normalized strain in fiber direction

$$
\kappa_{\mathrm{f}}=\max _{\tau \leqslant t} \frac{E_{1}\left\langle\varepsilon_{1}\right\rangle}{F_{1 \mathrm{t}}} \tag{2}
$$

where $E_{1}$ is the ply Young's modulus in fiber direction, $\langle\varepsilon_{1}\rangle$ is the positive strain in fiber direction and $F_{1 \mathrm{t}}$ is the ply strength in fiber

direction. Damage initiates when $\kappa_{\mathrm{f}}=1$ and an exponential softening relation is used to compute $\omega_{\mathrm{f}}$.

$$
\omega_{\mathrm{f}}=
\begin{cases}
0 & \kappa_{\mathrm{f}} \leqslant 1 \\
1-\frac{1}{\kappa_{\mathrm{f}}} e^{-\beta\left(\kappa_{\mathrm{f}}-1\right)} & \kappa_{\mathrm{f}}>1
\end{cases}
\qquad(3)
$$

where $\beta$ is related to the characteristic element length $L^{*}$ and the fracture toughness $G_{I c, \mathrm{f}}$ with the crack band method as

$$
\beta=\frac{2 L^{*} F_{1 \mathrm{t}}^{\mathrm{e}}}{2 G_{I c, \mathrm{f}} E_{1}-L^{*} F_{1 \mathrm{t}}^{2}}
\qquad(4)
$$

For most realistic representation of crack bridging behavior as observed by Pinho et al. [22], linear-exponential [23] or bilinear [24] softening would be better, but for the current investigations we keep the formulation as simple as possible.

The characteristic element length $L^{*}$ is computed from the finite element area $A$ as $^{1}$

$$
L^{*}=\frac{6}{\pi \sqrt[4]{3}} \sqrt{A}
\qquad(5)
$$

With the crack band method, the width of the damaged band has to be estimated from the element size. This width is most clearly defined for low order elements, where it is ensured that a mechanism can only be formed when all integration points in a band of elements are damaging. In the presented analyses, linear triangular elements are used.

For the influence of fiber failure on the matrix cracking process we consistently work with the isotropic softening assumption. That means, firstly, that the failure criterion is applied on the effective stress $\left(\mathbf{D}^{\mathrm{e}} \boldsymbol{\varepsilon}\right)$ instead of on the nominal stress $\boldsymbol{\sigma}$ and, secondly, that after crack initiation fiber damage is also applied to the traction

$$
\mathbf{t}=\left(1-\omega_{\mathrm{f}}\right)\left(1-\omega_{\mathrm{m}}\right) \mathbf{K} \llbracket \mathbf{u} \rrbracket
\qquad(6)
$$

where $\left(1-\omega_{\mathrm{m}}\right) \mathbf{K} \llbracket \mathbf{u} \rrbracket$ is the traction computed with the cohesive damage law. In each cohesive integration point, $\omega_{\mathrm{f}}$ is computed from the bulk strain at that point, which is taken as the average of the independent strains on both sides of the crack.

Preliminary results obtained with the fiber failure model have shown that, in combination with the models for matrix cracking and delamination, it is possible to capture size effects that include a switch between different failure modes upon changing the specimen dimensions [25]. This connects to experimental observations by Wisnom et al. [26,27].

## 4. Shear nonlinearity
Composite materials may exhibit significant nonlinearity before failure due to deformations in the matrix, particularly with respect to shear deformations. Van Paepegem et al. have proposed a phenomenological model for shear nonlinearity [28,29]. This model includes both damage and plasticity, so that it can be fitted with respect to observed loading/unloading behavior with both stiffness degradation and permanent strain, see Fig. 2b. For failure analysis, a proper description of the unloading behavior is of importance, also under monotonic boundary conditions, because unloading of the bulk material will occur around the failure zone.

The basic relation between shear stress and shear strain with damage and plasticity is

$$
\tau_{6}=G_{6}\left(1-\omega_{6}\right)\left(\gamma_{6}-\gamma_{6}^{\mathrm{p}}\right)
\qquad(7)
$$

where we use subscript 6 to indicate the in-plane shear component. Van Paepegem et al. [28] propose exponential evolution relations for $\omega_{6}$ and $\gamma_{6}^{\mathrm{p}}$ in differential form. In order to obtain behavior that is independent of the time step size, the equations are rewritten here in closed form:

$$
\frac{\mathrm{d} \gamma_{6}^{\mathrm{p}}}{\mathrm{d} \gamma_{6}}=C_{1} \gamma_{6} \exp \left(C_{2} \gamma_{6}^{\mathrm{p}}\right) \Rightarrow \gamma_{6}^{\mathrm{p}}=-\frac{\ln \left(1-C_{1} C_{2} \gamma_{6}^{2} / 2\right)}{C_{2}}
\qquad(8)
$$

$$
\frac{\mathrm{d} \omega_{6}}{\mathrm{~d} \gamma_{6}}=C_{3} \exp \left(C_{4} \omega_{6}\right) \Rightarrow \omega_{6}=-\frac{\ln \left(1-C_{3} C_{4} \gamma_{6}\right)}{C_{4}}
\qquad(9)
$$

Apart from the elimination of the differential formulation, another change has been made in Eq. (9) with respect to the original formulation. Namely that the evolution of $\omega_{6}$ depends on the total strain $\gamma_{6}$ rather than on the elastic strain $\gamma_{6}^{\mathrm{e}}=\gamma_{6}-\gamma_{6}^{\mathrm{p}}$. This adaptation disentangles the influence of the four material parameters $C_{1}, \ldots, C_{4}$ on the stress strain behavior and therefore simplifies the curve fitting exercise in which these parameters are to be obtained.

In laminate analysis that is predictive with respect to the position and number of matrix cracks, a crack spacing parameter is required [12]. This is caused by the fact that matrix cracking does not lead to relaxation of the surrounding material unless it is accompanied by delamination. Crack initiation is only allowed in places where the projected distance with existing cracks is equal to a certain minimum value. As a consequence, it cannot be excluded that the stress in the bulk material between two cracks will exceed the matrix strength. For this reason, the model for shear nonlinearity, needs to remain well-posed beyond the failure strain, even though it is unclear what is the physical meaning of this part. The model by Van Paepegem et al. [28] starts to exhibit softening from a certain threshold strain. This would violate the separation between matrix nonlinearity and matrix failure and is therefore undesirable. This is solved by extending the phenomenological curve with a perfectly plastic part beyond the point where $\partial \tau_{6} / \partial \gamma_{6}=0$.

The interaction between shear nonlinearity and fiber damage is straightforward because the two processes are driven by independent strain components. Fiber damage is applied to the total stress after shear nonlinearity, i.e. Eq. (1) is generalized to

$$
\boldsymbol{\sigma}=\left(1-\omega_{\mathrm{f}}\right) \widehat{\mathbf{D}} \boldsymbol{\varepsilon}^{\mathrm{e}}
\qquad(10)
$$

where $\widehat{\mathbf{D}}$ is the orthotropic material stiffness matrix with nonlinear shear component $\widehat{D}_{66}=\left(1-\omega_{6}\right) G_{6}$ and $\boldsymbol{\varepsilon}^{\mathrm{e}}$ is the elastic strain with $\gamma_{6}^{\mathrm{e}}=\gamma_{6}-\gamma_{6}^{\mathrm{p}}$.

There is no coupling between hardening matrix damage $\omega_{6}$ and softening matrix damage in transverse cracks $\left(\omega_{\mathrm{m}}\right)$ or in the interface $\left(\omega_{\mathrm{d}}\right)$. This can only be justified if the microcracks that are represented by $\omega_{6}$ in the continuum are not aligned with the microcracks represented by $\omega_{\mathrm{m}}$ and $\omega_{\mathrm{d}}$ in the cohesive zones. For delamination this is a likely assumption, but for transverse cracking some kind of interaction would be realistic. Moreover, where parameter identification is concerned, in the measurement of $G_{I I c, \mathrm{~m}}$ there is definitely some energy dissipation involved that is due to the very same processes that are interpreted as shear nonlinearity in other measurements. The sharp distinction we currently hold between matrix damage in transverse cracks and matrix damage due to in-plane shear is debatable. This is a consequence of the mesolevel approach. Two phenomena are dealt with that are clearly distinct on the mesoscale but nevertheless connected on the microscale. For now, we leave this issue unresolved, because energy dissipation in matrix cracks is not a key issue in the complete failure simulation.

## 5. Path following technique
The material models described above are implemented in an implicit quasi-static finite element framework. The equilibrium

$^{1}$ Eq. (5) gives the average projected length of an equilateral triangle, which is computed with an integral over different possible orientations: $L^{*}=\frac{1}{\pi / 6} \int_{0}^{\pi / 6} L \cos \theta d \theta$, where $L$ is the length of the side of the triangle, which is related to the area via $A=\frac{\sqrt{3}}{4} L^{2}$.


path is followed with the dissipation based arclength method, which was developed by Gutiérrez [30]. In the derivation of this method secant unloading is assumed, which is not the case in our computations for two reasons, firstly for the permanent strain due to shear nonlinearity and secondly due to the residual stress from the curing process. An extension to plasticity has been derived before by Verhoosel et al. [31]. In that derivation, however, it is tacitly assumed that plasticity is the only dissipative mechanism, which is obviously not the case in our model. Therefore we need to derive a new constraint equation. This will also include the influence of thermal strain.

Like with other arclength methods, a constraint equation is added to the system of equations. In the dissipation based arclength method, the constraint equation is formulated such that a finite amount of energy is prescribed to be dissipated in the time step. For models with secant unloading, the constraint equation can be expressed in terms of nodal quantities only. The derivation is given in [30], and it can readily be shown that addition of cohesive tractions does not change the resulting constraint equation:

$$
\frac{1}{2} \hat{\mathbf{f}}^{T}\left(\lambda_{0} \Delta \mathbf{a}-\Delta \lambda \mathbf{a}_{0}\right)=\Delta \tau
\tag{11}
$$

where $\hat{\mathbf{f}}$ is a unit load vector, $\lambda$ is the load scale factor and $\mathbf{a}$ is the nodal displacement vector and $\Delta \tau$ is the prescribed amount of dissipated energy in the time step. The subscript 0 is used to refer to a quantity at the beginning of the time step, while $\Delta$ indicates an increment during the time step.

The presence of thermal strain and plasticity require an additional vector assembly, rendering the constraint equation as

$$
\hat{\mathbf{f}}^{T}\left(\lambda_{0} \Delta \mathbf{a}-\Delta \lambda \mathbf{a}_{0}\right)+\Delta \mathbf{a}^{T} \mathbf{f}_{0}^{*}=2 \Delta \tau
\tag{12}
$$

with

$$
\mathbf{f}_{0}^{*}=\int_{\Omega} \mathbf{B}^{T}\left\{\mathbf{D}_{0}\left(\boldsymbol{\varepsilon}^{\mathrm{th}}+\boldsymbol{\varepsilon}_{0}^{\mathrm{p}}\right)+\boldsymbol{\sigma}_{0}^{T}\left(\frac{\partial \boldsymbol{\varepsilon}^{\mathrm{p}}}{\partial \boldsymbol{\varepsilon}}\right)_{0}\right\} \mathrm{d} \Omega
\tag{13}
$$

where $\mathbf{B}$ is the strain nodal displacement matrix, $\mathbf{D}$ is the consistent stiffness matrix, $\boldsymbol{\varepsilon}^{\text {th }}$ is the thermal strain which is assumed to be constant and defined (in index notation) as

$$
\varepsilon_{i j}^{\text {th }}=\alpha_{i} \Delta T \delta_{i j}
\tag{14}
$$

where $\alpha_{i}$ are the orthotropic thermal expansion coefficients and $\Delta T$ is the temperature drop in the curing process [32]. The derivation of Eq. (12) is presented in Appendix A.

## 6. Numerical example

To test the model and to illustrate its use, a $[90 / 0]_{\mathrm{s}}$ laminate with a central notch is analyzed, which was investigated experimentally by Spearing and Beaumont [33] and numerically by Wisnom and Chang [2]. The geometry is given in Fig. 3.

Elasticity parameters are taken from Spearing and Beaumont [33], $E_{1}=135 \mathrm{GPa}, E_{2}=9.6 \mathrm{GPa}, v_{12}=0.31$ and $G_{6}=5.8 \mathrm{GPa}$. Tensile and shear matrix strength are set to $60 \mathrm{MPa}$ [33] and $75 \mathrm{MPa}$ [2], respectively. For transverse cracking the strength parameters are corrected to in situ values following Camanho et al. [34]. The mode I and mode II fracture energy for transverse cracking are taken from Wisnom and Chang [2]: $G_{I c, \mathrm{~m}}=0.15 \mathrm{~N} / \mathrm{mm}$ and $G_{I I c, \mathrm{~m}}=0.4 \mathrm{~N} / \mathrm{mm}$. Again following [2], the latter value is also used for delamination. It must be noted, however, that it is not a general fact that fracture energies related to transverse matrix cracking and delamination are equal. Micromechanically, the two processes are different. Delamination takes place in the resin rich zone between the plies, while transverse cracks may partially be constituted by fiber-matrix debonding. The ply strength in fiber direction is taken from Spearing and Beaumont [33]: $F_{1 \mathrm{t}}=1673 \mathrm{MPa}$. The parameters for the shear nonlinearity are chosen to fit data reported by Lafarie-Frenot and Touchard [35]: $C_{1}=22, C_{2}=-22, C_{3}=35$, and $C_{4}=-5$. Thermal expansion coefficients are taken from Jiang et al. [4]: $\alpha_{1}=0^{\circ} \mathrm{C}^{-1}$ and $\alpha_{2}=3 \times 10^{-5}{ }^{\circ} \mathrm{C}^{-1}$. The minimum spacing between the matrix cracks is $0.5 \mathrm{~mm}$.

![](./images/811809731004858368_3.jpg)

Fig. 3. Geometry and boundary conditions for notched plate analysis.

### 6.1. Fracture energy for fiber failure

A parameter that is not given by Spearing and Beaumont is the fracture energy related to fiber failure. However, this parameter is of high importance for the failure load. This setup is in the quasi-brittle regime where the strength of the specimen depends on the strength of the material as well as on its fracture energy. Spearing and Beaumont [33] report a far field failure stress of $426 \mathrm{MPa}$. The influence of the fracture energy on the global behavior can be observed in Fig. 4, where $\sigma_{\infty}$ is the applied load averaged over the cross section.

The maximum load decreases as the fracture energy is decreased, reaching the reported value for $G_{I c, \mathrm{f}}=50 \mathrm{~N} / \mathrm{mm}$. Therefore, in the remainder of this section, we will work with this value. Notably, due to the symmetry assumption near the plane of failure the effective value of the fracture energy for fiber failure is two times the input value. The fitting value of approximately $100 \mathrm{~N} / \mathrm{mm}$ is in the range of values measured for carbon/epoxy by Pinho et al. [22].

In Fig. 5 the deformation from a post peak time step is visualized. Deformations are magnified with a factor 5. In the top ply $\left(90^{\circ}\right)$ the shear nonlinearity is indicated, and in the bottom ply $\left(0^{\circ}\right)$ the fiber damage. In both plies, the mesh-independent matrix cracks can be observed, in the top ply as a distributed crack pattern in which the left most is opening in normal direction and in the bottom ply as a single split with shear displacement jump.

Fig. 6 shows the split length as a function of the applied load. The evolution of the length of the traction free matrix crack in the $0^{\circ}$-ply is compared with experimental observations from [33] and simulation results from [2]. The cohesive zone is also visualized, as the difference between the complete length of the discontinuity in the displacement field and the length of the traction free crack. The cohesive zone can be observed to be approximately con-

![](./images/811809731004858368_4.jpg)

Fig. 4. Global response with three different values of fracture energy related to fiber failure.

![](./images/811809731004858368_5.jpg)

Fig. 5. Deformed mesh of both plies with fiber damage $\omega_{f}$ in the $0^{\circ}$-ply and shear damage $\omega_{6}$ in the $90^{\circ}$-ply.

stant at 2.5 mm during crack propagation. Our results are very close to those reported by Wisnom and Chang [2]. The agreement with experimental data is reasonably well, although the last two experimental data points seem to indicate that the crack propagation is retarded in this stage, which has not been reproduced. Possibly, this retardation is caused by an increase in the fracture energy due to crack bridging with growing crack length, which was not accounted for in the analysis.

### 6.2. Transverse cracking

Extensive transverse cracking can be observed in the computational results. However, in each ply only one matrix crack is opening significantly and the amount of energy dissipated in the matrix cracks is small compared to the energy dissipation due to shear nonlinearity, delamination and fiber failure. Therefore, it is safe to limit the number of cracks in the analysis. Indeed, when the number of matrix cracks per ply was limited to one, this had a very limited effect on the global response. A small increase in the maximum far field average stress value (from 426 to 433 MPa) was observed. The predicted delamination profile was strongly similar in both cases, as can be seen in Fig. 7, where the matrix cracks and delamination profile from both analyses are shown for a load level close to the maximum. Indeed, in both cases the angle of the delamination front with the split in the $0^{\circ}$-ply is very close to the $3.5^{\circ}$ reported by Spearing et al. [36].

The fact that the secondary matrix cracks are not very significant has been used to simplify the following analysis. The number of matrix cracks was limited in all the following analyses, because this allows for use of a coarser mesh in the region without delamination and reduces the number of additional iterations that have to be carried out when cracks propagate [8]. The reduced problem without distributed matrix cracking is subjected to a mesh refinement study. Fig. 8a shows the maximum load level for five different meshes, with uniform refinement in the area where damage occurs. It can be observed that the peak load level is approximately constant for sufficient mesh refinement. The post-peak response is also independent of the element size (see Fig. 8b).

![](./images/811809731004858368_6.jpg)

Fig. 6. Split length as a function of applied load.

![](./images/811809731004858368_7.jpg)

Fig. 7. Delamination pattern with and without distributed matrix cracking; dotted lines indicate the experimentally observed angle of the delamination front [36]; $\sigma_{\infty} \approx 410$ MPa.

### 6.3. Influence of individual models

The analysis is repeated three more times, subsequently turning off shear nonlinearity, delamination damage, and fiber failure.

![](./images/811809731004858368_8.jpg)

(a) Peak load for five different meshes

![](./images/811809731004858368_9.jpg)

(b) Load-displacement relation for three different meshes

Fig. 8. Mesh-refinement study.

Without shear nonlinearity, delamination is more extensive and a significantly different angle in the delamination front is observed, see Fig. 9. This is in agreement with earlier computational results by Wisnom and Chang [2]. The obtained load displacement curves are shown in Fig. 10. The positive influence of delamination on the strength of the specimen can be observed clearly: the maximum load level drops from 433 to 281 MPa when delamination is not allowed. Subcritical delamination reduces the stress concentration at the notch tip and therefore delays the onset of fiber failure.

The increase in delamination when shear nonlinearity is not included does not lead to a strong increase in the maximum load level: the predicted maximum without shear nonlinearity is 439 MPa, which is an increase of less than 2%. Apparently, the shear nonlinearity also reduces the stress concentration with plastic deformations, which in this case cancels the influence of the fact that shear nonlinearity delays delamination. However, this cannot be taken as evidence that it is safe to neglect shear nonlinearity in all cases. The influence of shear nonlinearity on the subcritical damage and the influence of subcritical damage on the load bearing capacity together stress the importance of including shear nonlinearity in the failure analysis.

![](./images/811809731004858368_10.jpg)

Fig. 9. Delamination and matrix cracking without shear nonlinearity, $\sigma_{\infty} \approx 410$ MPa, cf. Fig. 7.

![](./images/811809731004858368_11.jpg)

(a) Load displacement relation

![](./images/811809731004858368_12.jpg)

(b) Maximum load level for varying $G_{I C, f}$

Fig. 10. Influence on global response of disregarding individual failure processes.

### 6.4. Thickness effect

In Fig. 11a it is shown that changing the ply thickness has a significant influence on the global response. When the ply thickness is increased with a factor 4 to $t=0.5$ mm, failure occurs in two steps. Delamination propagates more rapidly and the load drops for a first time when the delaminated area reaches the opposite boundary. After that, the delamination propagates rapidly from the plane of symmetry towards the loaded boundary. When the delamination almost extends over the complete specimen, the load increases again. What had remained is an unnotched $0^{\circ}$ ligament. The second maximum in the load is reached when this ligament fails. It must be remarked, however, that for the second maximum, neglecting statistical effects is not realistic. The statistical size effect that can be expected for the unnotched strength (see e.g. Wisnom [20]) cannot be represented with the current framework.

The ply thickness also influences the shape of the delamination profile. Spearing et al. [36] report an increase in the angle between delamination front and load direction for increasing ply thickness. This trend is reproduced in the computational results, as can be seen when comparing the thick ply results in Fig. 11b with the thin ply results in Fig. 7. However, the angle in the predicted delamination profile is larger than the observed $7^{\circ}$.

![](./images/811809731004858368_13.jpg)

(a) Load displacement relation

![](./images/811809731004858368_14.jpg)

(b) Delamination pattern $(\sigma_{\infty} \approx 250\ \text{MPa})$

Fig. 11. Influence of ply thickness on response; the dotted line in (b) indicates the experimentally observed angle of the delamination front [36].

### 6.5. Influence of residual stress

Up to this point, residual stresses due to the fabrication process have been neglected. The analysis is repeated with two different values for the temperature drop: $\Delta T=-50\ ^{\circ}\text{C}$ and $\Delta T=-100\ ^{\circ}\text{C}$. The influence of the residual stress on the maximum load level is shown in Fig. 12. The maximum load increases with increasing magnitude of the temperature drop. This can be explained by the fact that the residual stresses promote the delamination because the elastic energy related to the thermal stress is released as delamination drives. And, as observed before, delamination causes an increase in the failure load.

In Fig. 13 the evolution of the split length and cohesive zone is visualized for the case with $\Delta T=100\ ^{\circ}\text{C}$. The split length without temperature drop (cf. Fig 6) is also shown. The influence of residual stress is negligible for the part where the agreement with experimental observations is well. For high stress levels, however, the split grows faster when residual stress is taken into account, which is related to the abovementioned promotion of delamination.

The thick ply analysis is also repeated with residual stresses. In this case, a significant influence is obtained with regard to the load level at which the first load drop is observed. The load level corresponding with the second peak, however, is independent of the initial temperature drop. This is because after delamination residual stresses have vanished and the remaining fiber ligament that is loaded up to failure is exactly equal in all cases. In order to obtain this last results, the location of the crack in the $0^{\circ}$-ply had to be fixed. Otherwise, small deviations in this location influenced the failure load, because the exact size of the small part of the rounded notch tip that is still present in the almost unnotched ligament governs its strength.

![](./images/811809731004858368_15.jpg)

Fig. 12. Influence of residual stress on peak load level, for the thick ply analysis, there are two peaks in each analysis: the first related to delamination and the second to fiber failure (cf. Fig. 11a).

![](./images/811809731004858368_16.jpg)

Fig. 13. Split length as a function of applied load in the presence of residual stress (cf. Fig. 6).

Notably the residual stress did not have a visible influence on the angle of the delamination front. However, for the thick ply analysis, in the presence of residual stress, the delamination profile showed a stronger (concave) curvature.

### 7. Conclusions

A computational framework including different models for nonlinear processes has been applied to the failure analysis of a centrally notched cross-ply laminate. With the dissipation based arclength method it is possible to follow the equilibrium path until complete loss of integrity. The sequence of failure events that has been observed in experiments was reproduced. In combination with the phantom node method for matrix cracking and interface elements for delamination, the presented fiber failure model allows for predictive analysis of progressive failure in laminates.

The influence of ply thickness on the delamination profile could also be captured. It has been shown that, for this example, distributed transverse cracking does not influence the global behavior, only the primary matrix cracks that initiate at the notch tip are relevant. The influence of residual stress due to the curing process on the load level at which failure occurs can be either positive, or negative or negligible, depending on the type of failure.

Shear nonlinearity and residual stress due to the curing process accelerate delamination, which in turn delays the onset of fiber failure. It is exactly this kind of interaction between different processes that complicates failure prediction in laminates. The presented framework is able to capture the different processes and their interaction realistically.

The comparison with reported crack patterns validates the model for matrix cracking, shear nonlinearity and delamination. The model for fiber failure is not validated with the presented analysis, but it is demonstrated that the failure process can be captured with the proposed model.

## Acknowledgments
This research is supported by the Technology Foundation STW (under Grant DCB.6623) and the Ministry of Public Works and Water Management, The Netherlands.

## Appendix A. Derivation of constraint equation
The dissipation rate $G$ is computed as the difference between the exerted power $P$ and the rate of elastic energy $\dot{V}$ [30]
$$
G=P-\dot{V} \tag{15}
$$
with
$$
P=\dot{\mathbf{a}}^{T} \mathbf{f}_{\mathrm{ext}}=\lambda \dot{\mathbf{a}}^{T} \hat{\mathbf{f}} \tag{16}
$$
where $\hat{\mathbf{f}}$ is a unit load vector, $\lambda$ is the load scale factor and $\dot{\mathbf{a}}$ is the nodal displacement rate.

The elastic energy $V$ is defined as
$$
V=\frac{1}{2} \int_{\Omega}\left(\boldsymbol{\varepsilon}-\boldsymbol{\varepsilon}^{\mathrm{p}}-\boldsymbol{\varepsilon}^{\mathrm{th}}\right)^{T} \boldsymbol{\sigma} \mathrm{d} \Omega+\frac{1}{2} \int_{\Gamma} [\![\mathbf{u}]\!]^{T} \mathbf{t} \mathrm{d} \Gamma \tag{17}
$$
where $\Omega$ is the bulk domain and $\Gamma$ is the cohesive surface, either in an interface element or in a phantom node crack. With the kinematic relations $\boldsymbol{\varepsilon}=\mathbf{B a}$ and $[\![\mathbf{u}]\!]=\mathbf{Z a}$ , this can be reorganized to
$$
V=\frac{1}{2} \mathbf{a}^{T}\left(\int_{\Omega} \mathbf{B}^{T} \boldsymbol{\sigma} \mathrm{d} \Omega+\int_{\Gamma} \mathbf{Z}^{T} \mathbf{t} \mathrm{d} \Gamma\right)-\frac{1}{2} \int_{\Omega}\left(\boldsymbol{\varepsilon}^{\mathrm{p}}+\boldsymbol{\varepsilon}^{\mathrm{th}}\right)^{T} \boldsymbol{\sigma} \mathrm{d} \Omega \tag{18}
$$

The two integral terms between parentheses can be eliminated, because they are equal to the internal force vector, and hence, when equilibrium is satisfied, to the external force vector. So the elastic energy can be rewritten as
$$
V=\frac{1}{2} \lambda \mathbf{a}^{T} \hat{\mathbf{f}}-\frac{1}{2} \int_{\Omega}\left(\boldsymbol{\varepsilon}^{\mathrm{p}}+\boldsymbol{\varepsilon}^{\mathrm{th}}\right)^{T} \boldsymbol{\sigma} \mathrm{d} \Omega \tag{19}
$$

Next, we take the rate of the elastic energy (assuming constant $\boldsymbol{\varepsilon}^{\text{th}}$)
$$
\dot{V}=\frac{1}{2}\left(\dot{\lambda} \mathbf{a}^{T} \hat{\mathbf{f}}+\lambda \dot{\mathbf{a}}^{T} \hat{\mathbf{f}}\right)-\frac{1}{2} \int_{\Omega}\left(\dot{\boldsymbol{\varepsilon}}^{\mathrm{p}}\right)^{T} \boldsymbol{\sigma}+\left(\boldsymbol{\varepsilon}^{\mathrm{p}}+\boldsymbol{\varepsilon}^{\mathrm{th}}\right)^{T} \dot{\boldsymbol{\sigma}} \mathrm{d} \Omega \tag{20}
$$

After application of the chain rule, this can be reorganized as
$$
\dot{V}=\frac{1}{2}\left(\dot{\lambda} \mathbf{a}^{T} \hat{\mathbf{f}}+\lambda \dot{\mathbf{a}}^{T} \hat{\mathbf{f}}-\dot{\mathbf{a}}^{T} \mathbf{f}^{*}\right) \tag{21}
$$
with
$$
\mathbf{f}^{*}=\int_{\Omega} \mathbf{B}^{T} \mathbf{E}^{T} \boldsymbol{\sigma}+\mathbf{B}^{T} \mathbf{D}^{T}\left(\boldsymbol{\varepsilon}^{\mathrm{p}}+\boldsymbol{\varepsilon}^{\mathrm{th}}\right) \mathrm{d} \Omega \tag{22}
$$
where $\mathbf{D}$ is the consistent tangent matrix $D_{i j}=\partial \sigma_{i} / \partial \varepsilon_{j}$ and $\mathbf{E}$ is the gradient of plastic strain with respect to total strain $E_{i j}=\partial \varepsilon_{i}^{\mathrm{p}} / \partial \varepsilon_{j}$.

Substitution of (16) and (21) into Eq. (15) gives
$$
G=\frac{1}{2}\left(\dot{\mathbf{a}}^{T}\left(\lambda \hat{\mathbf{f}}+\mathbf{f}^{*}\right)-\dot{\lambda} \mathbf{a}^{T} \hat{\mathbf{f}}\right) \tag{23}
$$

With forward Euler integration we arrive at the constraint equation that prescribes that a finite amount of energy, $\Delta \tau$, is dissipated in the time step
$$
\lambda_{0} \Delta \mathbf{a}^{T} \hat{\mathbf{f}}-\Delta \lambda \mathbf{a}_{0}^{T} \hat{\mathbf{f}}+\Delta \mathbf{a}^{T} \mathbf{f}_{0}^{*}=2 \Delta \tau \tag{24}
$$
where subscript 0 refers to values at the beginning of the time step and $\Delta$ indicates an increment during the time step. Due to the forward Euler integration, the vector $\mathbf{f}^{*}$ has to be evaluated only once per time step.

## References
[1] van der Meer FP, Sluys LJ. Continuum models for the analysis of progressive failure in composite laminates. J Compos Mater 2009;43(20):2131-56.

[2] Wisnom MR, Chang F-K. Modelling of splitting and delamination in notched cross-ply laminates. Compos Sci Technol 2000;60(15):2849-56.

[3] Hallett SR, Wisnom MR. Numerical investigation of progressive damage and the effect of layup in notched tensile tests. J Compos Mater 2006;40(14):1229-45.

[4] Jiang W-G, Hallett SR, Green BG, Wisnom MR. A concise interface constitutive law for analysis of delamination and splitting in composite materials and its application to scaled notched tensile specimens. Int J Numer Methods Eng 2007;69(9):1982-95.

[5] Iarve EV. Mesh independent modelling of cracks by using higher order shape functions. Int J Numer Methods Eng 2003;56(6):869-82.

[6] Mollenhauer D, Iarve EV, Kim R, Langley B. Examination of ply cracking in composite laminates with open holes: a moiré interferometric and numerical study. Composites: Part A 2006;37(2):282-94.

[7] Ling D, Yang QD, Cox BN. An augmented finite element method for modeling arbitrary discontinuities in composite materials. Int J Fract 2009;156(1):53-73.

[8] van der Meer FP, Sluys LJ. A phantom node formulation with mixed mode cohesive law for splitting in laminates. Int J Fract 2009;158(2):107-24.

[9] Camanho PP, Dávila CG, de Moura MF. Numerical simulation of mixed-mode progressive delamination in composite materials. J Compos Mater 2003;37(16):1415-38.

[10] Yang QD, Cox BN. Cohesive models for damage evolution in laminated composites. Int J Fract 2005;133(2):107-37.

[11] Turon A, Camanho PP, Costa J, Dávila CG. A damage model for the simulation of delamination in advanced composites under variable-mode loading. Mech Mater 2006;38(11):1072-89.

[12] van der Meer FP, Sluys LJ. Mesh-independent modeling of both distributed and discrete matrix cracking in interaction with delamination. Eng Fract Mech, in press. doi:10.1016/j.engfracmech.2009.11.010.

[13] Hansbo A, Hansbo P. A finite element method for the simulation of strong and weak discontinuities in solid mechanics. Comput Methods Appl Mech Eng 2004;193(33-35):3523-40.

[14] Mergheim J, Kuhl E, Steinmann P. A finite element method for the computational modelling of cohesive cracks. Int J Numer Methods Eng 2005;63(2):276-89.

[15] Song J-H, Areias PMA, Belytschko T. A method for dynamic crack and shear band propagation with phantom nodes. Int J Numer Methods Eng 2006;67(6):868-93.

[16] Moës N, Belytschko T. Extended finite element method for cohesive crack growth. Eng Fract Mech 2002;69(7):813-33.

[17] Hille TS, Suiker ASJ, Turteltaub S. Microcrack nucleation in thermal barrier coating systems. Eng Fract Mech 2009;76(6):813-25.

[18] Bažant ZP, Oh B. Crack band theory for fracture of concrete. Mater Struct 1983;16(3):155-77.

[19] Peerlings RHJ, de Borst R, Brekelmans WAM, Geers MGD. Gradient-enhanced damage modelling of concrete fracture. Mech Cohes-Frict Mater 1998;3(4):323-42.

[20] Wisnom MR. Size effects in the testing of fibre-composite materials. Compos Sci Technol 1999;58(13):1937-57.

[21] Puck A, Schürmann H. Failure analysis of FRP laminates by means of physically based phenomenological models. Compos Sci Technol 1998;58(7):1045-67.

[22] Pinho ST, Robinson P, Iannucci L. Fracture toughness of the tensile and compressive fibre failure modes in laminated composites. Compos Sci Technol 2006;66(13):2069-79.

[23] Maimí P, Camanho PP, Mayugo JA, Dávila CG. A continuum damage model for composite laminates: part I - constitutive model. Mech Mater 2007;39(10):897-908.

[24] Dávila CG, Rose CA, Camanho PP. A procedure for superposing linear cohesive laws to represent multiple damage mechanisms in the fracture of composites. Int J Fract 2009;158(2):211-23.

[25] van der Meer FP, Sluys LJ. Combining models for splitting, delamination and fiber failure in the analysis of progressive laminate failure. In: Pinho ST, editor. Proceedings of 2nd ECCOMAS thematic conference on the mechanical response of composites, London; 2009.

[26] Green BG, Wisnom MR, Hallett SR. An experimental investigation into the tensile strength scaling of notched composites. Composites: Part A 2007;38(3):867-78.

[27] Wisnom MR, Hallett SR. The role of delamination in strength, failure mechanism and hole size effect in open hole tensile tests on quasi-isotropic laminates. Composites: Part A 2009;40(4):335-42.

[28] Van Paepegem W, De Baere I, Degrieck J. Modelling the nonlinear shear stress-strain response of glass fibre-reinforced composites. Part 1: experimental results. Compos Sci Technol 2006;66(10):1455-64.

[29] Van Paepegem W, De Baere I, Degrieck J. Modelling the nonlinear shear stress-strain response of glass fibre-reinforced composites. Part II: model development and finite element simulations. Compos Sci Technol 2006;66(10):1465-78.

[30] Gutiérrez MA. Energy release control for numerical simulations of failure in quasi-brittle solids. Commun Numer Methods Eng 2004;20(1):19-29.

[31] Verhoosel CV, Remmers JJC, Gutiérrez MA. A dissipation-based arc-length method for robust simulation of brittle and ductile failure. Int J Numer Methods Eng 2009;77(9):1290-321.

[32] Hyer MW. Stress analysis of fiber-reinforced composite materials. Boston: McGraw-Hill; 1998.

[33] Spearing SM, Beaumont PWR. Fatigue damage mechanics of composite materials. I: experimental measurement of damage and post-fatigue properties. Compos Sci Technol 1992;44(2):159-68.

[34] Camanho PP, Dávila CG, Pinho ST, Iannucci L, Robinson P. Prediction of in situ strengths and matrix cracking in composites under transverse tension and in-plane shear. Composites: Part A 2006;37(2):165-76.

[35] Lafarie-Frenot MC, Touchard F. Comparative in-plane shear behaviour of long-carbon-fibre composites with thermoset or thermoplastic matrix. Compos Sci Technol 1994;52(3):417-25.

[36] Spearing SM, Beaumont PWR, Ashby MF. Fatigue damage mechanics of composite materials, II: a damage growth model. Compos Sci Technol 1992;44(2):169-77.