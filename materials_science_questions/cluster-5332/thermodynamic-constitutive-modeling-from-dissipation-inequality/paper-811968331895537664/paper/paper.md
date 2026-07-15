## 5. Generalized Variables.

### 5.1. The concept of generalized variables.

#### 5.1.1. Introduction.

Limit analysis of a rigid perfectly plastic continuum is based on the three following concepts : (1) yield condition and related flow rule, (2) licit stress field, and (3) licit flow mechanism. Great simplification is achieved when these concepts can be applied without the need to discuss three-dimensional stress and displacement fields. This situation arises in linear elasticity when the considered solid is a beam, plate, or shell. Assumptions regarding the deformations of these particular structural elements are accepted as direct consequences of the fact that these elements are "thin" in certain directions (normal to the axis of a beam or to the median surface of a plate or shell).

For beams, the hypothesis of Bernoulli states that plane cross sections remain plane and orthogonal to the deformed material axis. For plates and shells, straight segments normal to the median surface remain straight and normal to the deformed median surface. As long as Hooke's law of linear elasticity is applicable, it is possible to obtain all stress components at every point of a beam, a plate, or a shell when stress resultants and resultant moments are known. To do this, we need only apply the assumption that normals to the median surface are preserved, and use the equilibrium equations and Hooke's law ; the latter immediately furnish all strain components [5.1]. Hence, stress resultants and resultant moments are sufficient for a complete description of stresses and strains.

Theory [5.2] and experiments [5.3] show that Bernoulli's hypothesis and its genera- lization to plates and shells (normals preserved) are *equally valid in the elastic and plastic ranges*. Bernoulli's hypothesis will therefore be adopted in the following discussion of rigid-plastic beams, plates, and shells.

#### 5.1.2. Beams without axial force.

A generic cross section is subjected to a bending moment M and a shear force V.

From Bernoulli's hypothesis, shear strains are seen to vanish and longitudinal strains $\varepsilon_x$ are given by (*)

(*) Transverse strains are irrelevant.

$$
\varepsilon_{\mathrm{x}}=\mathrm{y} \kappa, \tag{5.1}
$$

where y is the distance from the neutral plane and $\kappa$ is the curvature of the material axis. (Note that $\kappa$ is the reciprocal of the radius of curvature). The strain rate is therefore given by

$$
\dot{\varepsilon}_{\mathrm{x}}=\mathrm{y} \frac{\partial \kappa}{\partial \mathrm{t}}=\mathrm{y} \dot{\kappa}. \tag{5.2}
$$

Because the state of stress is uniaxial (*), the power dissipated per unit of length of the beam in a plastic region is

$$
\mathrm{D}=\int_{-\mathrm{h} / 2}^{\mathrm{h} / 2} \sigma_{\mathrm{Y}}\left|\dot{\varepsilon}_{\mathrm{x}}\right| \mathrm{b}(\mathrm{y}) \mathrm{dy}, \tag{5.3}
$$

where h is the height of the section and b(y) the width at the level y.

With the use of eq. (5.2), eq. (5.3) can be written

$$
\mathrm{D}=\int_{-\mathrm{h} / 2}^{\mathrm{h} / 2} \sigma_{\mathrm{Y}}|\mathrm{y} \dot{\kappa}| \mathrm{b}(\mathrm{y}) \mathrm{dy}=|\dot{\kappa}| \mathrm{M}_{\mathrm{p}}, \tag{5.4}
$$

where $\mathrm{M}_{\mathrm{p}}$ is the (ultimate) plastic moment (see Com. V, Section 2.2).

The total rate of dissipation $D_{t}$ is then

$$
D_{t}=\int_{\text {struct }}|\dot{\kappa}| M_{p} d s, \tag{5.5}
$$

or for plastic hinges with rotation rates $\dot{\theta}$,

(*) It is assumed that shear stresses do not influence yielding.

$$
D_{\mathrm{t}}=\sum \mathrm{M}_{\mathrm{pi}}\left|\dot{\theta}_{\mathrm{i}}\right|,
\tag{5.6}
$$

as was established in Com. V, Section 3.4. We see that

1.
The yield condition reduces to $|\mathrm{M}|=\mathrm{M}_{\mathrm{p}}$ and the flow rule to $\operatorname{sign} \dot{\theta}_{\mathrm{i}}=\operatorname{sign} \mathrm{M}_{\mathrm{i}}$, or $\mathrm{M}_{\mathrm{i}} \dot{\theta}_{\mathrm{i}} \geq 0$;

2. The stress field reduces to the M diagram ;

3. The strain rate field reduces to the distribution of the rate of curvature.

Beam and frame problems have been extensively studied in Com. V.

### 5.1.3. Arches.

In arches, neither the axial strain $\varepsilon_{\mathrm{o}}$ nor the axial force $\mathrm{N}$ can be neglected, even when we are not concerned with instability phenomena (see Com. V., Chapters 6 and 10). The longitudinal strain rate at the level y with respect to the centroid consists of a part due to bending $\dot{\varepsilon}_{\mathrm{y}}=\mathrm{y} \dot{\kappa}$, and of a part due to axial strain $\dot{\varepsilon}_{\mathrm{o}}$.

The total rate of dissipation is

$$
D_{\mathrm{t}}=\int_{\text {struct }}\left(\mathrm{M} \dot{\kappa}+\mathrm{N} \dot{\varepsilon}_{\mathrm{o}}\right) \mathrm{ds},
\tag{5.7}
$$

where M and N combine to produce complete plastification of the section. Interaction curves M versus N of various sections are given in Com. V., Section 5.2.

Assuming that the shear force $\mathrm{V}$ does not influence yielding, the functions $\mathrm{M}, \mathrm{N}, \dot{\kappa}$ and $\dot{\varepsilon}_{\mathrm{o}}$ of the abscissa $\mathrm{s}$ are sufficient for the problem at hand.

### 5.1.4. Simple plate and shell examples.

In both plates and shells, the thickness t must be small compared to the other dimensions. A plate has a plane median surface and is subjected solely to forces normal to this median plane (when the applied forces are parallel to this plane, the structure is called a disk). A shell has a median surface with at least one finite radius of curvature. A "membrane" is a shell with no bending rigidity.

On the median surface of one of the structures described above, and through a given point $\mathrm{P}$ of this surface, draw a line element ds that has $\mathrm{P}$ as its centre. The normals to the

median surface through the points of ds form the "cut based on ds". The stresses transmitted across this cut are statically equivalent to certain forces and couples acting at P, which are proportional to the length of ds. The factors of proportionality are called the "stress resultants" for the considered cut. The "state of stress" at P is specified by the stress resultants for two orthogonal cuts.

### 1. Circular plate with constant thickness and rotational symmetry in loading and supports :

With cylindrical coordinates $r, \theta, z$ (fig. 5.1), rotational symmetry indicates that the radial and circumferential bending moments $M_r$ and $M_\theta$ are the principal moments (the

![](./images/811968331895537664_1.jpg)

Fig. 5.1.

twisting moment $M_{r\theta}$ vanishes). These bending moments as well as the deflection rate depend solely on the coordinate r.

In accordance with the assumption that material normals remain normal to the deformed median surface, transverse shear strains are neglected. The strain rates are given by

$$
\dot{\varepsilon}_r = z\dot{\kappa}_r,
$$

$$
\dot{\varepsilon}_\theta = z\dot{\kappa}_\theta,
$$

where $\dot{\kappa}_r$ and $\dot{\kappa}_\theta$ are the radial and circumferential (that is the principal) rates of curvature.

In analogy with beams, the dissipation per unit area of the median plane is

$$
\mathrm{D}=\mathrm{M}_{\mathrm{r}} \dot{\kappa}_{\mathrm{r}}+\mathrm{M}_{\theta} \dot{\kappa}_{\theta} \tag{5.8}
$$

In relation (5.8), $\mathrm{M}_{\mathrm{r}}$ and $\mathrm{M}_{\theta}$ must combine to completely plastify the volume element $\mathrm{r} \mathrm{dr} \mathrm{d} \theta$ at the considered point.

Since the yield condition can be expressed solely in therms of $\mathrm{M}_{\mathrm{r}}$ and $\mathrm{M}_{\theta}$, the functions $\mathrm{M}_{\mathrm{r}}, \mathrm{M}_{\theta}, \dot{\kappa}_{\mathrm{r}}, \dot{\kappa}_{\theta}$ of $\mathrm{r}$ are sufficient for the limit analysis of the plate.

### 2. Cylindrical shells subjected to rotationally symmetric internal pressure :

Internal resultant forces and moments that the symmetry does not oblige to vanish are shown on fig. 5.2. We immediately note that, because of the rotational symmetry, the circumferential curvature rate $\dot{\kappa}_{\theta}$ vanishes. Indeed there is no circumferential displacement. Any point of the shell displaces in the meridian plane in which it is contained.

![](./images/811968331895537664_2.jpg)

Fig. 5.2.

Hence, any two neighbouring meridian planes experience no relative rotation, and $\mathrm{M}_{\theta}$ does not work. We thus have $\kappa_{\theta}=\dot{\kappa}_{\theta}=0$, because our generalized variables are defined from the expression of the internal energy (they are the Lagrange variables). Although the radius of the median surface varies from $\mathrm{R}$ to $\mathrm{R}+\mathrm{w}$, where $\mathrm{w}$ is the radial displacement of the median surface, the circumferential strain,

$$
\varepsilon_{\theta}=\frac{\mathrm{w}}{\mathrm{R}-\mathrm{z}} \quad \left(\frac{-\mathrm{t}}{2} \leq \mathrm{z} \leq \frac{\mathrm{t}}{2}\right),
$$

must be regarded as constant (and hence $\kappa_\theta=0$) because $z$ is negligible with respect to $R$ from the very definition of a shell.

Rates of transversal shear vanish because we assume the material normals to remain normal to the deformed median surface. The dissipation rate is then

$$
\mathrm{D}=\mathrm{M}_{\mathrm{x}} \dot{\kappa}_{\mathrm{x}}+\mathrm{N}_{\mathrm{x}} \dot{\varepsilon}_{\mathrm{x} 0}+\mathrm{N}_{\theta} \dot{\varepsilon}_{\theta 0}.
\tag{5.9}
$$

Expressing the yield condition solely in terms of $\mathrm{M}_{\mathrm{x}}, \mathrm{N}_{\mathrm{x}}$ and $\mathrm{N}_{\theta}$ (see Section 5.4), the functions $\mathrm{M}_{\mathrm{x}}, \mathrm{N}_{\mathrm{x}}, \mathrm{N}_{\theta}, \dot{\kappa}_{\mathrm{x}}, \dot{\varepsilon}_{\mathrm{x} 0}, \dot{\varepsilon}_{\theta 0}$ of $\mathrm{x}$ and $\theta$ will be sufficient for the limit analysis of the shell.

### 5.2. The general case : choice of the generalized variables.

Limit analysis of a structure will use collapse mechanisms of that structure. Denote by $\dot{\mathrm{q}}_{1}, \dot{\mathrm{q}}_{2}, \ldots, \dot{\mathrm{q}}_{\mathrm{n}}$, *the generalized strain rates* suitable for describing these mechanisms. As just seen, the generalized strain rates will be rates of curvature and extension for beams, plates and shells. For a three-dimensional body, or in the case of plane stress and plane strain, they will be the components of the strain-rate tensor.

The generalized stresses are then, *by definition* [5.4], the stress-type variables $\mathrm{Q}_{1}$, $\ldots, \mathrm{Q}_{\mathrm{n}}$ that must be associated with the generalized strain rates in order that the specific dissipation be given by

$$
\mathrm{D}=\mathrm{Q}_{1} \dot{\mathrm{q}}_{1}+\left\langle+\mathrm{Q}_{\mathrm{n}} \dot{\mathrm{q}}_{\mathrm{n}}.\right.
\tag{5.10}
$$

The variables $\mathrm{Q}_{\mathrm{i}}$ and $\dot{\mathrm{q}}_{\mathrm{i}}$ may even be chosen nondimensional, and eq. (5.10) may be rewritten in the slightly more general form

$$
\mathrm{D}=\mathrm{C}\left(\mathrm{Q}_{1} \dot{\mathrm{q}}_{1}+\left\langle+\mathrm{Q}_{\mathrm{n}} \dot{\mathrm{q}}_{\mathrm{n}}\right\rangle\right.
\tag{5.11}
$$

where $\mathrm{C}$ is a dimensional constant.

We now call "reactions" the generalized stresses that do not *a priori* vanish for reasons of symmetry or equilibrium and that nevertheless do not appear in eq. (5.10) because they correspond to generalized strain rates that, in the considered problem, have been assumed to vanish throughout the structure. For example, in beams, plates, and shells, transversal shear forces are always reactions because normals are assumed to remain normal to the deformed median surface. For the shell of the second example of Section 5.14, $\mathrm{M}_{\theta}$ is a "reaction" because $\dot{\kappa}_{\theta}$ vanishes.

Not only is it always possible to solve problems of limit analysis using only the generalized variables (with no reference to the reactions) but it is also the most efficient way for solving the problems. To that purpose, the reactions must be eliminated from the yield conditions. This will be discussed in Section 5.3.

Let us summarize as follows : The generalized stresses are the only stress-type variables that appear in the expression of the dissipation for the problem at hand. The yield condition is then expressed in terms of these generalized stresses only, by elimination of the reactions.

### 5.3. Eliminating the reactions.

#### 5.3.1. Introduction.

We now remark that the preceding definitions of generalized stresses and strain rates preserve the validity of formula (2.2) if the stress space $Q_{i}$ and the strain rate space $\dot{q}_{i}$ are superimposed. This fact is sufficient for all fundamental results of Chapter 3 to hold if one substitutes the generalized stresses $Q_{i}$ for the components of the tensor $(\sigma)$ and the generalized strain rates $\dot{q}_{i}$ for the components of the tensor $(\dot{\varepsilon})$. Fundamental properties (convexity of yield surface, plastic potential) and fundamental theorems (maximum dissi- pation, statical and kinematical theorems) are obtained in the very same manner, by mere modification of the terminology.

The only point to clarify is the elimination of the reactions, which, as a rule, initially appear in the most general yield condition.

Consider a structural element and denote by $Q_{1},...,Q_{i},...,Q_{n}$, the n stress-type variables acting on it. Suppose first that none is a reaction. The yield condition of this element can be written, in a normalized form :

$$
\mathrm{F}\left(Q_{1},...,Q_{i},...,Q_{n}\right)=1. \tag{5.12}
$$

We assume for the time being that F is a known function. The normality law applies to surface with eq. (5.12) in the superimposed stress space $\left(Q_{1},...,Q_{i},...,Q_{n}\right)$ and strain-rate space $\left(\dot{q}_{1},...,\dot{q}_{i},...,\dot{q}_{n}\right)$

We now suppose that (n - k) relations

$$
\begin{aligned}
\dot{\mathrm{q}}_{\mathrm{k}+1} & =0, \\
\dot{\mathrm{q}}_{\mathrm{k}+2} & =0, \\
& \dots \\
\dot{\mathrm{q}}_{\mathrm{n}} & =0,
\end{aligned} \tag{5.13}
$$

hold, expressing that, in the particular case under consideration, plastic flow can only occur with (n - k) vanishing generalized strain rates.

According to the normality law, eqs. (5.13) will select a set of points on the surface (5.12) where the projections of a normal vector on the axes k + 1, ..., n, vanish. This set of points form part of the original yield surface (5.12).

By projecting this part on the $\left(Q_{1},...,Q_{k}\right)$ space one obtains the simplified yield condition :

$$
\Phi\left(Q_{1},...,Q_{k}\right)=1, \tag{5.14}
$$

that contains only generalized stresses, and none of the reactions $Q_{k+1},...,Q_{n}$.

### 5.3.2. Direct elimination of the reactions through the use of the dissipation function.

Assuming that we know the dissipation function $\mathrm{D}\left(\dot{\mathrm{q}}_{1},..., \dot{\mathrm{q}}_{\mathrm{k}}\right)$ for a given problem with generalized strain rates $\dot{\mathrm{q}}_{1},..., \dot{\mathrm{q}}_{\mathrm{k}}$, we can generate the yield surface in the stress space $\mathrm{Q}_{1},..., \mathrm{Q}_{\mathrm{k}}$ with the technique described at the en of Section 2.5. The normality law obviously applies to that surface. We shall show that the surface obtained in this manner is identical with the surface (5.14) obtained by projection, and that, consequently, the normality law applies to that latter surface.

The basic yield surface (5.12) is, by nature, unique. Hence the manner in which it is obtained is irrelevant. We suppose we construct it from our knowledge of the dissipation function $\mathrm{D}\left(\dot{\mathrm{q}}_{1},..., \dot{\mathrm{q}}_{\mathrm{n}}\right)$ as described at the end of Section 2.5. We recall that, to every possible mechanism $\dot{\boldsymbol{\varepsilon}}$ with components $\dot{\mathrm{q}}_{1},..., \dot{\mathrm{q}}_{\mathrm{n}}$ (in the n dimensional space) there corresponds a plane tangent to the yield surface. This plane is normal to $\dot{\boldsymbol{\varepsilon}}$ and distant by $\mathrm{D}(\dot{\boldsymbol{\varepsilon}})$ from the origin (in the direction of $\dot{\boldsymbol{\varepsilon}}$), with $\dot{\boldsymbol{e}}$ the unit vector along $\dot{\boldsymbol{\varepsilon}}$. If we want to select, on the surface (5.12), the points where eqs. (5.13) are satisfied, we select a subset of tangent planes the normals of which have vanishing projections on axes k+1, ..., n.

The wanted simplified surface is the直到ar FortBAAdministration认识 younger originates breakdownDetails高性能难求ure of this subset of planes. Clearly this is identical to constructing the simplified surface directly from the knowledge of $\mathrm{D}\left(\dot{\mathrm{q}}_{1},..., \dot{\mathrm{q}}_{\mathrm{k}}\right)$ because we so select all mechanisms with $\dot{\mathrm{q}}_{\mathrm{k}+1}=\dot{\mathrm{q}}_{\mathrm{k}+2}=...=\dot{\mathrm{q}}_{\mathrm{n}}=0$ among all possible mechanisms. But this is also identical with the projection procedure of Section 5.3.1 that merely consists of taking the intersection of the subset of planes above in the $\left(Q_{1},...,Q_{k}\right)$ space.

To sum up, the same simplified yield condition (5.14) can be obtained either starting from the more general yield condition (5.12) and using conditions (5.13) or directly using the dissipation function $D\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)$

### 5.3.3. Remark on the reactions.

A distinction must be made between generalized strain rates that vanish because of the very definition of the structure and those that vanish because of special (symmetry) conditions. An example of the first class occurs when a shell or a plate or a beam is defined as a structure in which the direction normal to the median surface is a material direction. Hence, *there never is any transversal rate of shear*. Because of the normality law the yield surface is "cylindrical" with its axis parallel to the shear force axis (fig. 5.3). Consequently, *the shear forces may take any value*. They cannot be determined from mechanism and normality law, but may possibly be otained from equilibrium conditions.

On the other hand, the stress-type variables that are reactions because of some special (symmetry) conditions are assigned given values by the normality law. For example, in plane stress, $\dot{\varepsilon}_{2}=0$ imposes $\sigma_{2}=\frac{\sigma_{1}}{2}=\frac{1.15 \sigma_{\mathrm{Y}}}{2}$ for the Mises yield condition [fig. 5.4 (a)], or $0 \leq \sigma_{2} \leq \sigma_{\mathrm{Y}}$ [fig. 5.4 (b)] for the Tresca condition.

![](./images/811968331895537664_3.jpg)

Fig. 5.3.

But, at the same time, the equilibrium equations do not contain these reactions because of the special symmetry conditions above. Hence, when equilibrium and yield conditions are satisfied in terms of generalized stresses only, they can also always be satisfied when reactions are considered. Moreover, note that the equilibrium equations can be obtained from the theorem of virtual work by a variational procedure. No reaction will enter the virtual work equation. This remark proves that it is always possible to eliminate the reactions from the equations of equilibrium. Obviously, any definition of a structure will have a certain range of validity. Shear forces will have no effects on yielding of shells

in most cases, as the thickness-to-span ratio, that ranges from 10 to 30 for beams, goes from

![](./images/811968331895537664_4.jpg)

![](./images/811968331895537664_5.jpg)

20 to 50 for most plates and even to 500 for some shells [5.5]. Large concentrate forces may change the situation.

### 5.4. Obtaining yield conditions in generalized stresses.

#### 5.4.1. Method by integration.

Instead of establishing the most general yield condition (5.12) in order to obtain the simplified yield surfaces by section or projection [5.7], it is often desired to obtain the simplified yield condition directly.

To this purpose, the first method is an integration method. On the basis that normals remain normals, generalized strain rates are related to the components of the strain rate tensor at every level in the thickness. The strain rate tensor is related to the stress tensor by the normality law. Integration over the thickness furnishes the yield condition in generalized stresses. We illustrate this method with the example of a plate.

Consider a plate of constant thickness, transversally loaded and subjected to arbitrary boundary conditions. Orthogonal cartesian coordinate axes x and y are located in the median plane, and the positive z-axis has the direction of the loads (fig. 5.5). We assume not only that material normals remain normal to the deformed median surface but also that the transversal displacements w are small with respect to the constant thickness t, which, in turn, is small with respect to in-plane dimensions and do not vary with the deformation [5.1].

![](./images/811968331895537664_6.jpg)

Fig. 5.5.

The deflected shape of the plate is then completely described by the single function w(x,y) because we have (fig. 5.5):

$$
u=-z \frac{\partial w}{\partial x}, \quad v=-z \frac{\partial w}{\partial y}, \quad w=w(x,y), \tag{5.15}
$$

where u,v,w, are the components of the displacements of the points at the distance z of the midplane on the x-, y-, and z-axes, respectively.

Using eqs. (1.15) and (1.16), we obtain

$$
\begin{aligned}
\varepsilon_{x} &=-z \frac{\partial^{2} w}{\partial x^{2}}, \\
\varepsilon_{y} &=-z \frac{\partial^{2} w}{\partial y^{2}}, \\
\varepsilon_{z} &=0, \\
\tau_{x y} &=z \frac{\partial^{2} w}{\partial x \partial y}, \\
\tau_{x z} &=\tau_{y z}=0.
\end{aligned} \tag{5.16}
$$

![](./images/811968331895537664_7.jpg)

Fig. 5.6.

Because the midplane is deformation-free, we consider that the resultant forces parallel to this plane always vanish.

Hence, the remaining resultant forces and moments are shown in fig. 5.6, where all forces and moments are positive. Moments are related to stresses as follows :

$$
\begin{align}
M_x &= \int_{-1/2}^{1/2} \sigma_x z\ dz, \\
M_y &= \int_{-1/2}^{1/2} \sigma_y z\ dz, \\
M_{xy} &= -M_{yx} = \int_{-1/2}^{1/2} \tau_{xy} z\ dz.
\end{align}
\tag{5.17}
$$

Note that $\tau_{xy}$ is positive as shown in fig. 5.6.

Now, the virtual energy per unit area of the median plane is

$$
E = \int_{-1/2}^{1/2} \left( \sigma_x \varepsilon_x + \sigma_y \varepsilon_y + \tau_{xy} \gamma_{xy} \right) dz.
\tag{5.18}
$$

Using eqs. (5.16) in eq. (5.18), we obtain

$$
\begin{align}
E &= \left( -\frac{\partial^2 w}{\partial x^2} \right) \int_{-1/2}^{1/2} \sigma_x z\ dz + \left( -\frac{\partial^2 w}{\partial y^2} \right) \int_{-1/2}^{1/2} \sigma_y z\ dz \\
&\quad + \left( -2 \frac{\partial^2 w}{\partial x \partial y} \right) \int_{-1/2}^{1/2} \tau_{xy} z\ dz.
\end{align}
\tag{5.19}
$$

Within the framework of small deflection theory, the factors in parenthesis are the curvatures $\kappa_x$, $\kappa_y$ and twice the torsion $\kappa_{xy}$ of the deflected surface, respectively :

$$
\begin{align}
-\frac{\partial^2 w}{\partial x^2} &= \frac{1}{\rho_x} \equiv \kappa_x, \\
-\frac{\partial^2 w}{\partial y^2} &= \frac{1}{\rho_y} \equiv \kappa_y, \\
-2\frac{\partial^2 w}{\partial x \partial y} &= \frac{2}{\rho_{xy}} \equiv 2\kappa_{xy}.
\end{align} \tag{5.20}
$$

With the definitions (5.19) of the moments, relation (5.19) can hence be written $E = M_x \kappa_x + M_y \kappa_y + 2 M_{xy} \kappa_{xy}$, and the specific power of dissipation is

$$
D = M_x \dot{\kappa}_x + M_y \dot{\kappa}_y + 2 M_{xy} \dot{\kappa}_{xy}. \tag{5.21}
$$

The generalized stresses are $M_x, M_y, M_{xy}$ and the corresponding generalized strain rates are $\dot{\kappa}_x, \dot{\kappa}_y$ and $2\dot{\kappa}_{xy}$, respectively.

Because we actually consider each layer of thickness dz to be in plane stress, the yield condition is

$$
\sigma_R\left(\sigma_x, \sigma_y, \tau_{xy}\right) = \sigma_Y. \tag{5.22}
$$

On the other hand, inspection of relations (5.16) reveals that the strain-rate vector has components proportional to z. Hence, the corresponding stress point is the same for all z with same sign. If we now assume that the yield surface with eq. (5.22) is symmetric with respect to the origin (as for the von Mises and Tresca conditions), the stress point goes to a position symmetric with respect to the origin when z changes sign ()(fig. 5.7). If the yield state of stress is $(\sigma_x, \sigma_y, \tau_{xy})$ for positive z, it is $(-\sigma_x, -\sigma_y, -\tau_{xy})$ for negative z, and one obtains

$$
M_x = \sigma_x \frac{t^2}{4}, \quad M_y = \sigma_y \frac{t^2}{4}, \quad M_{xy} = \tau_{xy} \frac{t^2}{4}. \tag{5.23}
$$

Because moments are seen to be propositional to the stress components, the yield surface in the space of moments will have the same form as in the space of stress components.

It often proves convenient to use nondimensional (also called "reduced") variables. Stress components are rendered nondimensional by division by $\sigma_Y$, and relation (5.22) takes the "canonic" form

![](./images/811968331895537664_8.jpg)

Fig. 5.7.

$$
\Phi\left(\frac{\sigma_{\mathrm{X}}}{\sigma_{\mathrm{Y}}}, \frac{\sigma_{\mathrm{y}}}{\sigma_{\mathrm{Y}}}, \frac{\tau_{\mathrm{xy}}}{\sigma_{\mathrm{Y}}}\right)=1. \tag{5.24}
$$

Similarly, we define reduced moments

$$
\mathrm{m}_{\mathrm{x}}=\frac{\mathrm{M}_{\mathrm{x}}}{\mathrm{M}_{\mathrm{p}}}, \quad \mathrm{m}_{\mathrm{y}}=\frac{\mathrm{M}_{\mathrm{y}}}{\mathrm{M}_{\mathrm{p}}}, \quad \mathrm{m}_{\mathrm{xy}}=\frac{\mathrm{M}_{\mathrm{xy}}}{\mathrm{M}_{\mathrm{p}}}, \tag{5.25}
$$

where

$$
\mathrm{M}_{\mathrm{p}}=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4} \tag{5.26}
$$

is the yield moment for uniaxial bending. From definitions (5.25) and relations (5.23), we obtain

$$
\mathrm{m}_{\mathrm{x}}=\frac{\sigma_{\mathrm{x}}}{\sigma_{\mathrm{Y}}}, \quad \mathrm{m}_{\mathrm{y}}=\frac{\sigma_{\mathrm{y}}}{\sigma_{\mathrm{Y}}}, \quad \mathrm{m}_{\mathrm{xy}}=\frac{\tau_{\mathrm{yx}}}{\sigma_{\mathrm{Y}}}. \tag{5.27}
$$

With relations (5.27), condition (5.24) becomes

$$
\Phi\left(\mathrm{m}_{\mathrm{x}}, \mathrm{m}_{\mathrm{y}}, \mathrm{m}_{\mathrm{xy}}\right)=1. \tag{5.28}
$$

We see that the yield condition (5.28) in reduced moments is identical to that in reduced stresses.

For example, von Mises'condition (1.34) for plane stress, using reduced stresses, becomes

$$
\left(\frac{\sigma_{\mathrm{X}}}{\sigma_{\mathrm{Y}}}\right)^{2}+\left(\frac{\sigma_{\mathrm{y}}}{\sigma_{\mathrm{Y}}}\right)^{2}-\frac{\sigma_{\mathrm{X}}}{\sigma_{\mathrm{Y}}} \cdot \frac{\sigma_{\mathrm{y}}}{\sigma_{\mathrm{Y}}}+3\left(\frac{\tau_{\mathrm{XY}}}{\sigma_{\mathrm{Y}}}\right)^{2}=1
$$

Hence, the corresponding yield condition for a plate is simply

$$
\mathrm{m}_{\mathrm{x}}^{2}+\mathrm{m}_{\mathrm{y}}^{2}-\mathrm{m}_{\mathrm{x}} \mathrm{m}_{\mathrm{y}}+3 \mathrm{~m}_{\mathrm{xy}}^{2}=1. \tag{5.29}
$$

Similarly, Tresca's condition gives

$$
\max \left[\left|\mathrm{m}_{1}\right|,\left|\mathrm{m}_{2}\right|,\left|\mathrm{m}_{1}-\mathrm{m}_{2}\right|\right]=1. \tag{5.30}
$$

### 5.4.2. Use of the power of dissipation.

Consider the power of dissipation

$$
\mathrm{D}\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)=\mathrm{Q}_{1} \dot{\mathrm{q}}_{1}+\ldots+\mathrm{Q}_{\mathrm{k}} \dot{\mathrm{q}}_{\mathrm{k}}, \tag{5.31}
$$

where $\mathrm{Q}_{1}, \ldots, \mathrm{Q}_{\mathrm{k}}$ and $\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}$ are the generalized variables.

Because the function $\mathrm{D}\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)$ is homogeneous with the order one, Euler's theorem on homogeneous functions gives

$$
\mathrm{D}\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)=\frac{\partial \mathrm{D}}{\partial \mathrm{q}_{1}} \dot{\mathrm{q}}_{1}+\ldots+\frac{\partial \mathrm{D}}{\partial \mathrm{q}_{\mathrm{k}}} \dot{\mathrm{q}}_{\mathrm{k}}. \tag{5.32}
$$

By comparing eqs. (5.31) and (5.32) we find

$$
\mathrm{Q}_{1}=\frac{\partial \mathrm{D}\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)}{\partial \dot{\mathrm{q}}_{1}},
$$


![](./images/811968331895537664_9.jpg)

Fig. 5.8.

$$
Q_{k}=\frac{\partial \mathrm{D}\left(\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}\right)}{\partial \dot{\mathrm{q}}_{\mathrm{k}}} \tag{5.33}
$$

Relations (5.33) are the parametric equations of the yield surface, with parameters $\dot{\mathrm{q}}_{1}, \ldots, \dot{\mathrm{q}}_{\mathrm{k}}$. Actually, because a yield mechanism at a point defines the generalized strain rates except for a common positive factor, there are only k-1 parameters : for example the ratios

![](./images/811968331895537664_10.jpg)

Fig. 5.9.

of the $\dot{\mathrm{q}}_{\mathrm{i}}$ to one of them.

We illustrate the method in the example of the yield condition of a shell of revolution with axisymmetric loading [5.8]. Fig. 5.8 shows an element of the shell with the nonvanish- ing resultant forces and moments (per unit of length) acting on it. Principal directions are $\varphi$ and $\theta$ because of the symmetry. We denote by $\dot{\varepsilon}_{\theta}$ and $\dot{\varepsilon}_{\varphi}$ the principal rates of strain of the midsurface, and by $\dot{\kappa}_{\theta}$ and $\dot{\kappa}_{\varphi}$ the rates of curvature of that surface.

Because material normals remain normal to the deformed median surface, the dissipation per unit area of this surface is

$$
\mathrm{D}=\mathrm{M}_{\varphi} \dot{\kappa}_{\varphi}+\mathrm{M}_{\theta} \dot{\kappa}_{\theta}+\mathrm{N}_{\varphi} \dot{\varepsilon}_{\varphi}+\mathrm{N}_{\theta} \dot{\varepsilon}_{\theta}, \tag{5.34}
$$

so that $M_{\varphi}, M_{\theta}, N_{\varphi}, N_{\theta}$ are the generalized stresses.

We use Tresca's condition for plane stress $(\sigma_{z} \equiv \sigma_{3}=0$ ; see fig. 5.9).

To obtain the direction parameters of the outward pointing normal to the hexagonal cylinder at the various points of the plane hexagonal section of fig. 5.9, we simply note that the normal to the plane hexagon at one of its point is the projection in the $(O \sigma_{1}, O \sigma_{2})$ plane of the normal to the hexagonal cylinder at the same point. We further recall that the sum of the direction parameters p, q, and r, must vanish (see Section 2.6). We then can write table5.1, valid for points on the hexagon other than vertices A, B, ..., F. From table 5.1 we conclude that, according to eq. (2.8), the dissipation per unit volume is given by

Table 5.1.

<table>
  <thead>
    <tr>
      <th>Plastic<br>regimes</th>
      <th>p</th>
      <th>q</th>
      <th>r</th>
      <th>$\dot{\varepsilon}_{1}$</th>
      <th>$\dot{\varepsilon}_{2}$</th>
      <th>$\dot{\varepsilon}_{3}$</th>
      <th>$|\dot{\varepsilon}|$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AB</td>
      <td>1</td>
      <td>0</td>
      <td>-1</td>
      <td>$|\dot{\varepsilon}_{1}|$</td>
      <td>0</td>
      <td>$-\dot{\varepsilon}_{1}$</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{1}|$</td>
    </tr>
    <tr>
      <td>BC</td>
      <td>0</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>$|\dot{\varepsilon}_{2}|$</td>
      <td>$-\dot{\varepsilon}_{2}$</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{2}|$</td>
    </tr>
    <tr>
      <td>CD</td>
      <td>-1</td>
      <td>1</td>
      <td>0</td>
      <td>$-\dot{\varepsilon}_{2}$</td>
      <td>$|\dot{\varepsilon}_{2}|$</td>
      <td>0</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{2}|$</td>
    </tr>
    <tr>
      <td>DE</td>
      <td>-1</td>
      <td>0</td>
      <td>1</td>
      <td>$-\dot{\varepsilon}_{3}$</td>
      <td>0</td>
      <td>$|\dot{\varepsilon}_{3}|$</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{3}|$</td>
    </tr>
    <tr>
      <td>EF</td>
      <td>0</td>
      <td>-1</td>
      <td>1</td>
      <td>0</td>
      <td>$-\dot{\varepsilon}_{3}$</td>
      <td>$|\dot{\varepsilon}_{3}|$</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{3}|$</td>
    </tr>
    <tr>
      <td>FA</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>$|\dot{\varepsilon}_{1}|$</td>
      <td>$-\dot{\varepsilon}_{1}$</td>
      <td>0</td>
      <td>$\sqrt{2}\ |\dot{\varepsilon}_{1}|$</td>
    </tr>
  </tbody>
</table>

$$
\mathrm{D}_{\mathrm{u}}=\sigma_{\mathrm{Y}}\left|\dot{\varepsilon}_{\mathrm{i}}\right|. \tag{5.35}
$$

When the stress point is at a vertex, we may have a vertex of type A where only one stress component is not zero and hence has the value $\pm \sigma_{\mathrm{Y}}$. At point $\mathrm{A}, \sigma_{1}=\sigma_{\mathrm{Y}}$, $\sigma_{2}=\sigma_{3}=0$. The directions of the vector with components $\dot{\varepsilon}_{1}, \dot{\varepsilon}_{2}, \dot{\varepsilon}_{3}$ are bounded by those of the vectors associated with the regimes FA and AB. We thus have :

$$
\dot{\varepsilon}_{1} \geq\left|\dot{\varepsilon}_{2}\right|, \quad \dot{\varepsilon}_{1} \geq\left|\dot{\varepsilon}_{3}\right| \quad \text { and } \quad \dot{\varepsilon}_{1}>0.
$$

Thus,
$$
\mathrm{D}_{\mathrm{v}}=\sigma_{\mathrm{Y}} \max \left|\dot{\varepsilon}_{\mathrm{i}}\right|. \tag{5.36}
$$

A second vertex is of type B where $\sigma_{1}=\sigma_{2}=\sigma_{\mathrm{Y}}, \sigma_{3}=0, \mathrm{D}_{\mathrm{V}}=\sigma_{\mathrm{Y}}\left(\dot{\varepsilon}_{1}+\dot{\varepsilon}_{2}\right)$.

We also have $\dot{\varepsilon}_{1}+\dot{\varepsilon}_{2}=-\dot{\varepsilon}_{3}$ with $\dot{\varepsilon}_{1}>0$ and $\dot{\varepsilon}_{2}>0$.

![](./images/811968331895537664_11.jpg)

Thus, eq. (5.36) still holds. The same conclusion would be obtained for point E. As eq. (5.35) is a particular case of eq. (5.36) all cases are covered by eq. (5.36). By integration over the thickness t, we find the dissipation D per unit midsurface of the shell. The strain rates $\dot{\varepsilon}_{i}$ vary with z according to

$$
\dot{\varepsilon}_{1 z}=\dot{\varepsilon}_{1}+\dot{\kappa}_{1} z, \quad \dot{\varepsilon}_{2 z}=\dot{\varepsilon}_{2}+\dot{\kappa}_{2} z, \quad \dot{\varepsilon}_{3 z}=-\left(\dot{\varepsilon}_{1 z}+\dot{\varepsilon}_{2 z}\right) \tag{5.37}
$$

The direction 3 is that of the z-axis, and the directions 1 and 2 coincide with the $\varphi$ and $\theta$ directions. Note that the direction $\varphi$ and $\theta$ are interchangeable as far as the yield condition is concerned.

A typical distribution of $\dot{\varepsilon}_{i Z}$ is shown on fig. 5.10. The three parameters $\alpha_{1}, \alpha_{2}$, $\alpha_{3}$, defined by

$$
\alpha_{1}=\frac{\dot{\varepsilon}_{1}}{t \dot{\kappa}_{1}}, \quad \alpha_{2}=\frac{\dot{\varepsilon}_{2}}{t \dot{\kappa}_{2}}, \quad \alpha_{3}=\frac{\dot{\varepsilon}_{1}+\dot{\varepsilon}_{2}}{t\left(\dot{\kappa}_{1}+\dot{\kappa}_{2}\right)}, \tag{5.38}
$$

are sufficient to describe this distribution completely (see fig. 5.10 for notations). They locate the points P, Q, R of zero strain rate. The diagram of max $|\dot{\varepsilon}_{i}|$ is then constructed [fig. 5.10 (d)]. The dissipation D is given by the area of that diagram.

Now, relations (5.33) specialize to

$$
\mathrm{N}_{1}=\frac{\partial \mathrm{D}}{\partial \dot{\varepsilon}_{1}}, \quad \mathrm{~N}_{2}=\frac{\partial \mathrm{D}}{\partial \dot{\varepsilon}_{2}}, \quad \mathrm{M}_{1}=\frac{\partial \mathrm{D}}{\partial \dot{\kappa}_{1}}, \quad \mathrm{M}_{2}=\frac{\partial \mathrm{D}}{\partial \dot{\kappa}_{2}} \tag{5.39}
$$

The derivatives in relations (5.39) are most readily evaluated from the variations of the areas of the diagram in fig. 5.10 (d) for small variations of $\dot{\varepsilon}_{1}, \dot{\varepsilon}_{2}, \dot{\kappa}_{1}, \dot{\kappa}_{2}$.

For example, limiting values of the ratios of the dashed areas in fig. 5.10 to the corresponding variations of the parameters give (see [5.8]) :

$$
\mathrm{N}_{1}=\sigma_{\mathrm{Y}} \mathrm{t}\left[\frac{1}{2}-\alpha_{3}-\left(\frac{1}{2}+\alpha_{1}\right)\right]=-\sigma_{\mathrm{Y}} \mathrm{t}\left(\alpha_{1}+\alpha_{3}\right),
$$

$$
\mathrm{M}_{1}=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4}\left[\frac{1}{4}-\alpha_{3}^{2}+\left(\frac{1}{4}-\alpha_{1}^{2}\right)\right]=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4}\left[1-2\left(\alpha_{1}^{2}+\alpha_{3}^{2}\right)\right].
$$

Similarly,

$$
\mathrm{N}_{2}=-\sigma_{\mathrm{Y}} \mathrm{t}\left(\alpha_{3}+\alpha_{2}\right),
$$

$$
\mathrm{M}_{2}=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4}\left[1-2\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right)\right].
$$

With the following definitions of the reduced generalized stresses,

$$
\mathrm{n}_{1}=\frac{\mathrm{N}_{1}}{\mathrm{~N}_{\mathrm{p}}}, \quad \mathrm{n}_{2}=\frac{\mathrm{N}_{2}}{\mathrm{~N}_{\mathrm{p}}}, \quad \mathrm{m}_{1}=\frac{\mathrm{M}_{1}}{\mathrm{M}_{\mathrm{p}}}, \quad \mathrm{M}_{2}=\frac{\mathrm{M}_{2}}{\mathrm{M}_{\mathrm{p}}}, \tag{5.40}
$$

where $\mathrm{N}_{\mathrm{p}}=\sigma_{\mathrm{Y}} \mathrm{t}$ and $\mathrm{M}_{\mathrm{p}}=\sigma_{\mathrm{Y}}\left(\frac{\mathrm{t}^{2}}{4}\right)$, the preceding relations become

$$
\begin{gathered}
\mathrm{n}_{1}=-\left(\alpha_{1}+\alpha_{3}\right), \quad \mathrm{n}_{2}=-\left(\alpha_{2}+\alpha_{3}\right), \\
\mathrm{m}_{1}=1-2\left(\alpha_{1}^{2}+\alpha_{3}^{2}\right), \quad \mathrm{m}_{2}=1-2\left(\alpha_{2}^{2}+\alpha_{3}^{2}\right),
\end{gathered} \tag{5.41}
$$

Eqs. (5.41) are parametric equations of the desired yield surface, in $(\mathrm{n}_{1}, \mathrm{n}_{2}$,
$\mathrm{m}_{1}, \mathrm{m}_{2})$ space.

To obtain the complete surface, all relative positions of points P, Q, R of fig. 5.10 must be considered, with corresponding values of $\alpha_{1}, \alpha_{2}, \alpha_{3}$.

table 5.2. Points P, Q, R are distinct.

<table>
  <thead>
    <tr>
      <th>Central<br>point</th>
      <td>$\pm \mathrm{n}_{1}$</td>
      <td>$\pm \mathrm{n}_{2}$</td>
      <td>$\pm \mathrm{m}_{1}$</td>
      <td>$\pm \mathrm{m}_{2}$</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>P</th>
      <td>$-(\alpha_{1}+\alpha_{3})$</td>
      <td>$-(\alpha_{3}-\alpha_{2})$</td>
      <td>$1-2\left(\alpha_{1}^{2}+\alpha_{3}^{2}\right)$</td>
      <td>$2\left(\alpha_{2}^{2}-\alpha_{3}^{2}\right)$</td>
    </tr>
    <tr>
      <th>Q</th>
      <td>$-(\alpha_{1}+\alpha_{3})$</td>
      <td>$-(\alpha_{3}+\alpha_{2})$</td>
      <td>$1-2\left(\alpha_{1}^{2}+\alpha_{3}^{2}\right)$</td>
      <td>$1-2\left(\alpha_{3}^{2}+\alpha_{2}^{2}\right)$</td>
    </tr>
    <tr>
      <th>R</th>
      <td>$-(\alpha_{3}-\alpha_{1})$</td>
      <td>$-(\alpha_{3}+\alpha_{2})$</td>
      <td>$2\left(\alpha_{1}^{2}-\alpha_{3}^{2}\right)$</td>
      <td>$1-2\left(\alpha_{3}^{2}+\alpha_{2}^{2}\right)$</td>
    </tr>
  </tbody>
</table>

**Table 5.3. Points P, Q, R are not distinct.**

<table>
  <tr>
    <th>Coincidence</th>
    <th>Yield surface</th>
  </tr>
  <tr>
    <td>$P \equiv Q$</td>
    <td>$m_1 = \pm (1 - n_1^2)$</td>
  </tr>
  <tr>
    <td>$Q \equiv R$</td>
    <td>$m_2 = \pm (1 - n_2^2)$</td>
  </tr>
  <tr>
    <td>$R \equiv P$</td>
    <td>$m_1 - m_2 = \pm [1 - (n_1 - n_2)^2]$</td>
  </tr>
</table>

This discussion [5.8] gives the results shown in tables 5.2 and 5.3. Note that point P, Q, R must fall within the shell thickness. Hence $\alpha_1$, $\alpha_2$ and $\alpha_3$ are bounded by $-\frac{1}{2}$ and $+\frac{1}{2}$.

Two important particular situations occur when either one of the axial forces or one of the moments can be eliminated. The yield surface is then an ordinary surface in three-dimensional space (and not a hypersurface in a space of a higher number of dimen- sions). As the yield surface is symmetric with respect to the origin, representation and specification of one half of it is sufficient.

![](./images/811968331895537664_12.jpg)

Fig. 5.11.

Consider first $n_2 = 0$ (see [5.8]). The yield surface is shown in fig. 5.11. Part I is a plane with the equation

$$
m_2 = 1 \, , \tag{5.42}
$$

corresponding to $Q \equiv \mathrm{R}$ (table 5.3), + sign, with $n_2 = 0$. Part II corresponds to $P \equiv Q$, + sign. Its equation is

$$
m_1 = 1 - n_1^2 \tag{5.43}
$$

(cylinder with axis $\mathrm{Om_2}$). Part III corresponds to $P \equiv \mathrm{R}$, - sign. Its equation is

![](./images/811968331895537664_13.jpg)

Fig. 5.12.

$$
m_1 - m_2 = n_1^2 - 1 \tag{5.44}
$$

Eqs. of parts IV and V are obtained from table 5.1, taking Q and R for the central points, respectively. Condition $n_2 = 0$ gives $\alpha_3 = -\alpha_2$, and elimination of $\alpha_3$ and $\alpha_2$ from the remaining three relations furnishes, using the plus signs,

for part IV,
$$
m_1 = 1 - 2\left[\left(n_1 + \frac{\sqrt{1 - m_2}}{2}\right)^2 + \frac{1 - m_2}{4}\right], \tag{5.45}
$$

for part V,
$$
\mathrm{m}_{1}=2\left[\left(\mathrm{n}_{1}+\frac{\sqrt{1-\mathrm{m}_{2}}}{2}\right)^{2}-\frac{1-\mathrm{m}_{2}}{4}\right], \tag{5.46}
$$

The second interesting case occurs when $\mathrm{m}_{2}$ is a reaction, because $\dot{\kappa}_{2}=0$ (cylindrical shells with axisimmetrical loading, $\dot{\kappa}_{2}$ denoting circumferential rate of curvature [5.9, 5.10 and 4.3]). Elimination of $\mathrm{m}_{2}$ results in the yield surface of fig. 5.12. Part I is a plane with equation
$$
\mathrm{n}_{2}=1, \tag{5.47}
$$
bounded by parabolic arcs
$$
\mathrm{m}_{1}= \pm 2 \mathrm{n}_{1}\left(1-\mathrm{n}_{1}\right). \tag{5.47'}
$$

Part II is also a plane bounded by parabolic arcs. The relevant equations are
$$
\mathrm{n}_{2}-\mathrm{n}_{1}=1, \tag{5.48}
$$

$$
\mathrm{m}_{1}= \pm 2 \mathrm{n}_{1}\left(1+\mathrm{n}_{1}\right). \tag{5.48'}
$$

Part III is a portion of the parabolic cylinder with equation
$$
\mathrm{m}_{1}=1-\mathrm{n}_{1}^{2}, \tag{5.49}
$$
bounded by its intersection with the planes
$$
\mathrm{m}_{1}=0,
$$

$$
2 \mathrm{n}_{2}-\mathrm{n}_{1}= \pm 1. \tag{5.49'}
$$

Part IV and V belong to the paraboloids with equations
$$
\mathrm{m}_{1}= \pm \frac{1}{2}\left[2-\left(2 \mathrm{n}_{2}-1\right)^{2}-\left(2 \mathrm{n}_{2}-2 \mathrm{n}_{1}-1\right)^{2}\right]. \tag{5.50}
$$

Note that the yield surfaces are formed of parts with different analytic expressions, and the normality law can only be formulated explicitly when one knows on what part the stress point is located.

### 5.4.3. Purely statical method : adaptation of the reactions.

To begin with, suppose there is no reaction among the stress-type variables, the number of which is, say, three.

A part of the yield surface is shown schematically on fig. 5.13. Choose fixed values
$Q_1^0$ and $Q_2^0$ such that the point with the coordinates $Q_1^0$, $Q_2^0$, 0 falls within the yield surface.
Now let $Q_3$ vary from zero to the highest value $Q_3$ compatible with the yield condition of
the material (expressed in terms of the ordinary stress components $(\sigma_x,....,\tau_{xy},...)$). The
coordinates $Q_1^0, Q_2^0, Q_3$ are that of a point P of the desired yield surface. In a general manner
one attributes fixed values to all generalized stresses but one, which will be given the
extreme magnitudes compatible with the yield condition of the material. In this way, the
yield surface is generated point by point.

Now, if there exist reactions, the only nonfixed generalized stress depends not only
on the yield condition of the material but remains a function of the reactions which, as a
rule, are not fixed.

![](./images/811968331895537664_14.jpg)

Fig. 5.13.

The following theorem has been proved [5.5] :

**Adaptation :** If one fixes all generalized stresses but one, the reactions adapt
themselves to give the nonfixed generalized stress a maximum positive or minimum negative
value.

Thus, the procedure just described still holds when reactions exist, and the reactions
may be completely ignored.

We illustrate the results by these two examples :

1. *Bar with square cross section, subjected to two orthogonal bending moments*
$M_x$ and $M_y$ (fig. 5.14). We treat this problem by a variational procedure [3.8]. When the
cross section is completely plastic, we have at all points $|\sigma| = \sigma_Y$. If $y = \varphi(x)$ is the equation

of the boundary between the regions of tensions ($\sigma = \sigma_Y$) and compressions ($\sigma = -\sigma_Y$), we have

$$
\begin{aligned}
M_{x} &=\int_{-1 / 2}^{1 / 2}\left[\int_{-1 / 2}^{\varphi(x)} x\left(-\sigma_{Y}\right) d y+\int_{\varphi(x)}^{1 / 2} x \sigma_{Y} d y\right] d x \\
&=-2 \sigma_{Y} \int_{-1 / 2}^{1 / 2} x \varphi(x) d x,
\end{aligned}
$$

and, similarly,

![](./images/811968331895537664_15.jpg)

Fig. 5.14.

$$
M_{y}=\sigma_{Y} \int_{-1 / 2}^{1 / 2}\left[\frac{t^{2}}{4}-\varphi(x)^{2}\right] d x. \tag{5.51}
$$

Consider a fixed value of $M_x$ and assume $M_y$ to be an analytic maximum. If the stress distribution is then varied by an arbitrary small amount $\delta \sigma$, we have $\delta M_x = 0$ because $M_x$ is fixed ; and $\delta M_y = 0$ because $M_y$ is a maximum. Hence, $\alpha$ being a parameter, we can write, using eq. (5.51),

$$
\delta \mathrm{M}_{\mathrm{y}}+\alpha \delta \mathrm{M}_{\mathrm{x}}=-2 \sigma_{\mathrm{Y}} \int_{-1 / 2}^{1 / 2}[\varphi(\mathrm{x})+\alpha \mathrm{x}] \delta \varphi(\mathrm{x}) \mathrm{dx}=0,
$$

for all $\delta \sigma$, that is for all $\delta \varphi(\mathrm{x})$. Consequently, $\varphi(\mathrm{x})+\alpha \mathrm{x}=0$.

We see from the preceding relation that the boundary between tensions and compressions is a ray emanating from the origin. Hence, we readily obtain

$$
\mathrm{M}_{\mathrm{x}}=\frac{3}{4} \sigma_{\mathrm{Y}} \frac{\mathrm{t}^{3}}{8} \alpha, \quad \mathrm{M}_{\mathrm{y}}=\frac{2}{3} \sigma_{\mathrm{Y}} \frac{\mathrm{t}^{3}}{8}\left(3-\alpha^{2}\right)
$$

Eliminating $\alpha$ from the two equations above, and letting

$$
\mathrm{m}_{\mathrm{x}}=\frac{\mathrm{M}_{\mathrm{x}}}{\mathrm{M}_{\mathrm{p}}}, \quad \mathrm{m}_{\mathrm{y}}=\frac{\mathrm{M}_{\mathrm{y}}}{\mathrm{M}_{\mathrm{p}}}, \quad \mathrm{M}_{\mathrm{p}}=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4},
$$

![](./images/811968331895537664_16.jpg)

Fig. 5.15.

we finally obtain the desired equation

$$
\mathrm{m}_{\mathrm{y}}+\frac{3}{4} \mathrm{~m}_{\mathrm{x}}^{2}=1 \tag{5.52}
$$

of the yield curve.

Note that eq. (5.52) is valid only for $|\alpha| \leq 1$, that is for $|m_x / m_y| \leq 1$. Because the yield curve is symmetric with respect to the rays $m_x / m_y = \pm 1$, the remaining part is obtained without difficulty.

2. Circular cylindrical "sandwich" shell without axial force, subjected to axially symmetrical loading. Because of the absence of axial force and of the symmetry of revolution, the only nonvanishing stress type variables are $V_x$, $M_x$, $M_\theta$ and $N_\theta$ (see fig. 5.15).

Shear forces $V_x$ are reactions.

For a circular cylindrical shell, symmetry of revolution enforces $\dot{\kappa}_\theta = 0$. Hence, $M_\theta$ is a reaction and we must simply determine the yield condition in terms of $M_x$ and $N_\theta$.

![](./images/811968331895537664_17.jpg)

Fig. 5.16.

The "sandwich" shell is formed of a core with thickness H and two face sheets with thickness $t/2$ each (see fig. 5.16). The core carries exclusively shear forces $V_x$, to which it is always exceedingly resistant. The face sheets carry all other stresses and are assumed in a state of plane stress.

Denote by $\sigma_{\theta e}$ and $\sigma_{x e}$ the principal normal stresses in the external face sheet, and by $\sigma_{\theta i}$ and $\sigma_{x i}$ those in the internal sheet. We then have :

$$
\begin{aligned}
& N_{\theta}=\frac{t}{2}\left(\sigma_{\theta i}+\sigma_{\theta e}\right), \\
& M_{\theta}=\frac{t H}{4}\left(\sigma_{\theta i}-\sigma_{\theta e}\right), \\
& M_{x}=\frac{t H}{4}\left(\sigma_{x i}-\sigma_{x e}\right)
\end{aligned} \tag{5.53}
$$

Introducing reduced generalized stresses

$$
n_{\theta}=\frac{N_{\theta}}{N_{p}}, \quad m_{\theta}=\frac{M_{\theta}}{M_{p}}, \quad m_{x}=\frac{M_{x}}{M_{p}},
$$

where $N_{p}=\sigma_{Y} t$ and $M_{p}=\sigma_{Y}(t H / 2)$, we have

![](./images/811968331895537664_18.jpg)

Fig. 5.17.

$$
\begin{aligned}
n_{\theta} & =\frac{\sigma_{\theta i}+\sigma_{\theta e}}{2 \sigma_{Y}}, \\
m_{\theta} & =\frac{\sigma_{\theta i}-\sigma_{\theta e}}{2 \sigma_{Y}}, \\
m_{x} & =\frac{\sigma_{x i}-\sigma_{x e}}{2 \sigma_{Y}}.
\end{aligned}
\tag{5.54}
$$

Assume the material of the sheets obeys von Mises'yield condition :

$$
\sigma_{x}^{2}+\sigma_{\theta}^{2}-\sigma_{x} \sigma_{\theta}=\sigma_{Y}^{2},
\tag{5.55}
$$

represented by the ellipse of fig. 5.17. The state of stress in the shell is represented by points e and i on fig. 5.17, with coordinates $(\sigma_{x e}, \sigma_{\theta e})$ and $(\sigma_{x i}, \sigma_{\theta i})$, respectively. According to relations (5.54), the coordinates of the midpoint c of segment ei give $n_{x}$ and $n_{\theta}$, whereas the projections of the segment ei on the axes gives $m_{x}$ and $m_{\theta}$ (positive factors $1 / \sigma_{Y}$ and $1 / 2 \sigma_{Y}$ being irrelevant). Because $n_{x}=0$, the point c must remain on the $\sigma_{\theta}$ axis. For a given

position of point c (between points A and B) corresponding to some value of $n_\theta$, plastification of the shell element requires that at least one of the two points e and i be on the yield locus.

Now, the adaptation theorem tells us that the slope of segment ei must be such that its projection on the $\sigma_x$ axis is a maximum. This condition yields

$$
m_{\theta}=\frac{m_{x}}{2}, \tag{5.56}
$$

and points e and i both lie on the yield locus.

It is easily seen that when point c moved from A to B with condition (5.56) satisfied, the interaction relation is

$$
\frac{3}{4} m_{x}^{2}+n_{\theta}^{2}=1. \tag{5.57}
$$

![](./images/811968331895537664_19.jpg)

If the face-sheet material of the shell obeys Tresca's yield condition, represented on fig. 5.18, a similar analysis will furnish (a) for $0 \leq n_{\theta} \leq 1 / 2$,

$$
\mathrm{n}_{\theta} \leq \frac{\mathrm{m}_{\theta}}{\mathrm{m}_{\mathrm{x}}} \leq 1-\mathrm{n}_{\theta} \quad \text { and } \quad \mathrm{m}_{\mathrm{x}}=1, \tag{5.58}
$$

and (b) for $1 / 2 \leq n_\theta \leq 1$,

$$
m_{\theta}=\frac{m_{x}}{2} \quad \text { and } \quad \frac{m_{x}}{2}+n_{\theta}=1.
\tag{5.59}
$$

The interaction curve is given by eqs. (5.58) and (5.59).

### 5.4.4. Method of lower and upper bounds.

Let us imagine an isolated element of a structure. For a beam, such an element may be specified by a line element of length dx along the undeformed axis. This element is bounded by the normal cross sections of the beam through the endpoints of the line element and by part of the lateral surface of the beam. For a plate or shell, an element may be specified by an infinitesimal rectangle of sides $\mathrm{ds}_{1}$ and $\mathrm{ds}_{2}$ on the undeformed median surface ; it is bounded by the normals of this surface through the points of the rectangle and by parts of the two surfaces of the shell, fig. 5.19.

![](./images/811968331895537664_20.jpg)

A structural element of this kind may be regarded as a free body subjected to the resultant forces and couples of the stresses transmitted by neighbouring elements and such loads as may be directly applied to the considered element.

Any combination of stress resultants that causes the element to yield specifies a point of the yield locus.

From this point of view, the fundamental theorems of limit analysis of Sections 3.1 and 3.2 can be used to obtain yield surfaces in generalized stress space :

1. Any licit stress distribution on the element will furnish generalized stresses that will be the coordinates of a point on or within the yield surface ;

2. Any licit strain rate distribution across the element will be associated, through the normality law, with generalized stresses that will be the coordinates of a point on or outside the yield surface.

The yield surface can thus be bounded from the interior and exterior.

The application of the lower-bound theorem is obviously identical to the statical method of Section 5.4.3. Indeed, reciprocity of shearing stresses is the only condition enforced by local equilibrium, and plastic admissibility of a stress distribution reduces to not violating the yield condition (in terms of stress components). Usually, the stress distribution is varied to maximize one generalized stress while fixing the others, in order to move the representing point from the inside onto the yield surface, as explained in Section 5.4.3. Note that the stress distributions will in general correspond to nonvanishing "reaction". For example, suppose that the curvature $\dot{\kappa}_x$ vanishes whereas the extension rate $\dot{\varepsilon}_x$ does not vanish. Hence, $\sigma_x$ cannot be eliminated from the yield condition in terms of stress components, and the distribution of $\sigma_x$ on the cross section will generally correspond to $M_x \neq 0$. However, according to the adaptation theorem, the stress distributions can be chosen without regard to the values of the reactions.

On the other hand, when the internal restraint concerns strain-rate components at every point - for example $\dot{\gamma}_{xy}=0$ or $\dot{\varepsilon}_x=0$ everywhere), the corresponding stress component ($\tau_{xy}$ or $\sigma_x$) can be eliminated from the yield condition (see Section 5.3.3 and Chapter 11) as well as the reactions they produce.

Consider now the application of the upper-bound theorem. Suppose that, within the frame work of the basic assumptions, the flow mechanism of a structural element is completely known (as in the shell example treated in Section 5.4.2). Application of the upper-bound theorem will then directly furnish the exact yield surface. Actually, the procedure is identical to using the dissipation power (Section 5.4.2), as we shall show.

Let $\dot{q}_1,...,\dot{q}_n$ be the generalized strain rates (curvature rates, extension rates of the median surface) used to describe the flow mechanism of an element. The corresponding strain-rate components are given by relations of the type

$$
\dot{\varepsilon}=\dot{\varepsilon}\left(\dot{q}_{1},..., \dot{q}_{n}, z\right), \tag{5.60}
$$

where z is the distance of the considered point to the midsurface. Now, regard the qᵢ as the parameters of the problem. Through relations (5.60), each set of $\dot{q}_i$ gives a distribution of $\dot{\varepsilon}(z)$to which the yield condition and the normality law relate a distribution $\sigma(z)$. Hence, we can write

$$
\sigma=\sigma\left(\dot{\mathrm{q}}_{\mathrm{i}}, \ldots \dot{\mathrm{q}}_{\mathrm{n}}, \mathrm{z}\right). \tag{5.61}
$$

Next we obtain the corresponding generalized stress $Q_i$ by integration over the thickness. The type of integration to be done is often obvious : if $\dot{q}_i$ is a curvature rate, $Q_i$ is the corresponding moment, if $\dot{q}_i$ is an extension rate, $Q_i$ is the corresponding axial force, etc. It must however be emphasized that, as a rule, the type of integration to achieve is determined by the definition of $Q_i$. This definition is related to the expression of dissipation power D (see relation 5.10). Integration over z will result in a function of $\dot{q}_1,...,\dot{q}_n$ as shown by relation (5.61). This function $Q_i$ must be such that $D=\sum Q_{i} \dot{q}_{i}$. Because D must be homogeneous of the order one in $\dot{q}_i$ (see Section 2.4) we have $Q_{i}=\frac{\partial D}{\partial \dot{q}_{i}}$. We conclude that, from the very definition of $Q_i$, integration over z must yield the same parametric form for $Q_i$ as is obtained from relations (5.33).

It follows that the use of the lower-bound and upper-bound theorems to obtain yield surfaces in generalized stresses will differ from the other methods only if the yield mechanism of the element does not correspond by the normality law to the licit state of stress.

We illustrate this discussion by two examples.

1. Beam with uniform solid cross section subjected to bending and torsion [3.8].

![](./images/811968331895537664_21.jpg)

Fig. 5.20.

Let Gx and Gy be the two principal axes of inertia of the cross section of a beam (G being the centroid, fig. 5.20). Tresca's yield condition for pure torsion is $\tau^{2} = \tau_{zx}^{2} + \tau_{zy}^{2} = \frac{\sigma_{Y}^{2}}{4}$. Assume a uniform distribution of shear stress $\tau$ similar to that corresponding to the limit torque $M_{tp}$ but with $\tau < \frac{\sigma_{Y}}{2}$. The reduce torque $m_{t}$ will be

$$
m_{t}=\frac{M_{t}}{M_{tp}}=\frac{\tau}{\frac{\sigma_{Y}}{2}} \tag{5.62}
$$

To this shear stress distribution, we superimpose a distribution of normal stress $\sigma$ to that corresponding to the fully plastic bending moment $M_{p}$ about axis x, but with $\sigma < \sigma_{Y}$. The reduced bending moment is

$$
m \equiv \frac{M}{M_{p}}=\frac{\sigma}{\sigma_{Y}} \tag{5.63}
$$

The two distributions of stresses will best combine to satisfy

$$
\sigma^{2}+4 \tau^{2}=\sigma_{Y}^{2} \tag{5.64}
$$

everywhere, to furnish a fully plastified cross section. Substitution of expressions (5.62) and (5.63) for $\tau$ and $\sigma$, respectively, into eq. (5.64) yields

$$
m^{2}+m_{t}^{2}=1 \tag{5.65}
$$

Relation (5.65) is a lower bound for the interaction curve because the state of stress is licit but does not correspond to a kinematically admissible strain-rate distribution.

To obtain an upper bound, we arbitrarily assume that yielding results in a rate of curvature $\dot{\kappa}_{y}$ in the $G_{zy}$ plane and a rate of twist $\dot{\kappa}_{xy}$ about G, but no warping of the cross section. The corresponding strain rates are

$$
\dot{\varepsilon}_{z}=y \dot{\kappa}_{y}, \quad \dot{\gamma}_{z x}=-y \dot{\kappa}_{x y}, \quad \dot{\gamma}_{z y}=x \dot{\kappa}_{x y} \tag{5.66}
$$

The dissipation is

$$
D=\int_{A}\left(\sigma_{z} \dot{\varepsilon}_{z}+\tau_{z x} \dot{\gamma}_{z x}+\tau_{x y} \dot{\gamma}_{z y}\right) \mathrm{d} A
$$

or

$$
D=M \dot{\kappa}_{y}+M_{t} \dot{\kappa}_{x y}
$$

Because $\tau^{2}=\tau_{z x}^{2}+\tau_{z y}^{2}$, Tresca's condition (5.64) may be written

$$
\sigma_{z}^{2}+4\left(\tau_{z x}^{2}+\tau_{z y}^{2}\right)=\sigma_{Y}^{2} . \tag{5.67}
$$

The normality law (2.7) applied to condition (5.67) furnishes

$$
\dot{\varepsilon}_{z}=2 \lambda \sigma_{z}, \quad \dot{\gamma}_{z x}=8 \lambda \tau_{z x}, \quad \dot{\gamma}_{z y}=8 \lambda \tau_{z x} . \tag{5.68}
$$

From comparison of relations (5.66) and (5.67) we have

$$
\sigma_{z}=\frac{y \dot{\kappa}_{y}}{2 \lambda}, \quad \tau_{z x}=\frac{y \dot{\kappa}_{x y}}{8 \lambda}, \quad \tau_{z y}=\frac{x \dot{\kappa}_{x y}}{8 \lambda}. \tag{5.69}
$$

Substituting expressions (5.69) for $\sigma_{z}, \tau_{z x}, \tau_{z y}$ into relation (5.67), we obtain

$$
2 \lambda=\left(\frac{\dot{\kappa}_{y}}{\sigma_{Y}}\right)\left\{y^{2}+\alpha^{2}\left(x^{2}+y^{2}\right)\right\}^{1 / 2},
$$

where

$$
\alpha=\frac{\dot{\kappa}_{x y}}{2 \dot{\kappa}_{y}}.
$$

We now readily obtain

$$
m \equiv \frac{1}{M_{p}} \int_{A} \sigma_{x} y \mathrm{~d} A=\frac{\sigma_{Y}}{M_{p}} \int_{A} \frac{y^{2}}{\left[y^{2}+\alpha^{2}\left(x^{2}+y^{2}\right)\right]^{1 / 2}} \mathrm{~d} A,
$$

$$
\mathrm{m}_{\mathrm{t}} \equiv \frac{1}{\mathrm{M}_{\mathrm{tp}}} \int_{\mathrm{A}}\left(\mathrm{x} \tau_{\mathrm{zy}}-\mathrm{y} \tau_{\mathrm{zx}}\right) \mathrm{dA}=\frac{\sigma_{\mathrm{Y}} \alpha}{2 \mathrm{M}_{\mathrm{tp}}} \int_{\mathrm{A}} \frac{\left(\mathrm{x}^{2}+\mathrm{y}^{2}\right) \mathrm{dA}}{\left[\mathrm{y}^{2}+\alpha^{2}\left(\mathrm{x}^{2}+\mathrm{y}^{2}\right)\right]^{1 / 2}},
\tag{5.70}
$$

Relations (5.70) are the parametric equations of the interaction curve $\mathrm{m}$ versus $\mathrm{m}_{\mathrm{t}}$, $\alpha$ being used as parameter. Different cross-sections will give rise to different coefficients $\frac{\sigma_{\mathrm{Y}}}{\mathrm{M}_{\mathrm{p}}}$ and $\frac{\sigma_{\mathrm{Y}}}{\mathrm{M}_{\mathrm{tp}}}$. Because the relations (5.70) are obtained from a kinematically admissible strain-rate field [eqs. (5.66)], they furnish an upper bound for the exact interaction curve. Fig. 5.21, shows the two bounds for a circular cross section, curves a ; and for square cross section, curves b.

![](./images/811968331895537664_22.jpg)

Fig. 5.21.

(From Plastic Analysis of Structures by P.G. Hodge Jr. Copyright 1959, McGraw-Hill Book Company, Used by permission of McGraw-Hill Book Company, Inc.)

### 2. Cylindrical shell without axial force [3.9]

Consider a circular cylindrical shell as shown in fig. 5.22. It is subjected to an internal pressure that may solely depend on the coordinate x. Because of the symmetry of revolution and the absence of axial load, the only nonvanishing stress resultants and moments are those

shown in fig. 5.15. Shear force $V_x$ is a reaction (see Section 5.3.3), as well as bending moment $M_\theta$ (see Section 5.1.4, example 2). Tresca's yield condition may be expressed as

$$
\max\left[ \left|\sigma_x\right|,\left|\sigma_\theta\right|,\left|\sigma_x - \sigma_\theta\right| \right]=\sigma_Y, \tag{5.71}
$$

for all r. Plasticity occurs at a given level r of the shell thickness when one of the six relations

![](./images/811968331895537664_23.jpg)

Fig. 5.22.

(5.71) is satisfied. Obviously, the relation to satisfy may change at some values of r.

Let

$$
\begin{aligned}
m_x &= \frac{M_x}{M_p} = \frac{M_x}{\sigma_Y \frac{t^2}{4}}, \\
n_\theta &= \frac{N_\theta}{N_p} = \frac{N_\theta}{\sigma_Y t},
\end{aligned} \tag{5.72}
$$

be the reduced bending moment and axial force, respectively. They are the only generalized variables. We now distribute $\sigma_x$ and $\sigma_\theta$ over the thickness in order to maximize $n_\theta$ for a given $m_x$, while satisfying the yield condition (5.71). We first try

$$
m_x = 1. \tag{5.73}
$$

It is admissible as long as $\mathrm{n}_{\theta} \leq 1 / 2$. Indeed, as shown on fig. 5.23, we have $\mathrm{n}_{\theta}=1 / 2-\alpha$, and the reaction $\mathrm{m}_{\theta}$ is $\mathrm{m}_{\theta}=1 / 2-2 \alpha^{2}$, with $0 \leq \alpha \leq 1 / 2$. For $1 / 2 \leq \mathrm{n}_{\theta} \leq 1$, we may not have $\mathrm{m}_{\mathrm{x}}=1$ anymore. Fig. 5. 23 (b) shows the distribution that gives, for every $\mathrm{m}_{\mathrm{x}}$, the largest value of $\mathrm{n}_{\theta}$ compatible with the yield condition (5.71). We obtain

$$
\begin{aligned}
& \mathrm{m}_{\mathrm{x}}=1-4 \alpha^{2}, \\
& \mathrm{n}_{\theta}=\frac{1}{2}+\alpha
\end{aligned}
\tag{5.74}
$$

![](./images/811968331895537664_24.jpg)

Fig. 5.23

(and the reaction $\mathrm{m}_{\theta}=\frac{1}{2}-2 \alpha^{2}$, with $0 \leq \alpha \leq \frac{1}{2}$). Eqs. (5.73) and (5.74) define the interaction curve shown on fig. 5.24.

To prove that this curve is not only a lower bound but the exact interaction curve, we must associate, to the stress distributions above, corresponding strain-rate distributions. The principal strain rates $\dot{\varepsilon}_{\mathrm{x}}, \dot{\varepsilon}_{\theta}$ may be represented by the coordinates of a point (fig. 5.25). According to the normality law, all points of the first quadrant with $\dot{\varepsilon}_{\mathrm{x}}>0$ and $\dot{\varepsilon}_{\theta}>0$ are associated with the vertex B of Tresca's yield hexagon (see the insert in fig. 5.25). Similarly, it is easily seen that the regions bounded by the axes and the diagonals of the second and fourth quadrants correspond to the six vertices, whereas these six rays correspond to the six sides of the hexagon.

We now recall (see Section 5.4.2) that


$$
\begin{aligned}
\dot{\varepsilon}_{x} & =\dot{\varepsilon}_{x 0}+z \dot{\kappa}_{x}, \\
\dot{\varepsilon}_{\theta} & =\dot{\varepsilon}_{\theta 0}+z \dot{\kappa}_{\theta}=\dot{\varepsilon}_{\theta 0},
\end{aligned}\tag{5.75}
$$

![](./images/811968331895537664_25.jpg)

Fig. 5.24.

(From Plastic Analysis of Structures by P.G. Hodge Jr. Copyright 1959, McGraw-Hill Book Company, Used by permission of McGraw-Hill Book Company, Inc.)

where $\dot{\varepsilon}_{x 0}, \dot{\varepsilon}_{\theta 0}, \dot{\kappa}_{x}, \dot{\kappa}_{\theta}$ are rates of extension and of curvature of the midsurface in the longitudinal and circumferential directions, respectively. Curvature rate $\dot{\kappa}_{\theta}$ is known to vanish (Section 5.1.4) and $z$ is the radial distance of a layer from the median surface, counted as positive when directed inwards. Hence, if a point M (fig. 5.25) represents the state of strain rate at a point P on the median surface, strain rates of the various points on the normal at P will be represented by the points of a segment parallel to the $\dot{\varepsilon}_{x}$-axis and with center M. But because the axial force $n_{x}$ must vanish, there must be as many layers in regime D as in regime B (see the insert in fig. 5.25), or as many in regime A as in regime E. Consequently, the point M must fall on a certain dashed ray LON. Et is then easily seen that the kinematically admissible strain-rate distributions represented by the points of segments $M^{\prime} M_{1} M^{\prime}$ and $M^{\prime \prime} M_{2} M^{\prime \prime}$ in fig. 5.25 correspond to the stress distributions in fig. 5.23. The interaction curve shown in fig. 5.24 is therefore exact. Finally, we note that the parametric eqs. (5.73) and (5.74) could have been deduced from the results of Section

5.4.2 where the dissipation function was used. Indeed, if we relabel x and $\theta$ as 1 and 2, respectively, eqs. (5.75) show that the central point in fig. 5.10 is either P or Q because R goes to infinity. In both cases $\alpha_{1}=-\alpha_{3}$ because $n_{1}=0$, and $m_{1}=1-4 \alpha^{2}$, whereas $n_{2}=\frac{1}{2}+\alpha_{1}$, because $\alpha_{2}=\frac{1}{2}$ or $-\frac{1}{2}$, respectively (see [5.9]).

![](./images/811968331895537664_26.jpg)

### 5.5.Simplified yield surface.

#### 5.5.1. Convenience of a simplified yield surface.

A linear yield condition is very attractive from the mathematical point of view. Indeed, if the yield surface consists of plane facets, as long as the stress point remains on a given plane

![](./images/811968331895537664_27.jpg)

the yield vector retains the same direction and the yield "mechanism" does not change. All possible yield mechanisms can thus be classified into a finite number of plastic "regimes", each regime corresponding to the contact of the stress point with one plane, one edge, or one vertice (fig. 5.26). Limit analysis proves much easier in these circumstances than when the yield surface is curved, especially when the principal directions are known beforehand. There reasons explain the preference given to Tresca's yield condition over the condition of von Mises. But when generalized stresses are used, even Tresca's linear yield condition need not result in a piecewise linear yield surface, as shown in the second example of Section 5.4.4. The exact yield surface must then be replaced by a polyhedron, either inscribed (dashed lines in fig. 5.24) or circumscribed (dotted lines in fig. 5.24).

### 5.5.2. Influence on the limit load of linearizing the yield condition.

For the sake of simplification, consider a yield condition that involves only two generalized stresses $Q_{1}$ and $Q_{2}$. Let the exact yield curve be represented by the heavy line in fig. 5.27, and let $P_{1}$ be the corresponding exact limit load for a given structure and a given loading scheme. If, instead of the exact yield curve e, the inscribed polygon i (dashed lines) is used, the state of stress at collapse for polygon i is licit for curve e. If the corresponding limit load is $P_{i}$, the static theorem furnishes the inequality

$$
\mathrm{P}_{\mathrm{i}} \leq \mathrm{P}_{1} \tag{5.76}
$$

If $\mathrm{P}_{\mathrm{i}}^{-}$is statical licit load for i, we have

$$
\mathrm{P}_{\mathrm{i}}^{-} \leq \mathrm{P}_{\mathrm{i}} \tag{5.77}
$$

On the other hand, using a circumscribed polygon c would result in

$$
\mathrm{P}_{1} \leq \mathrm{P}_{\mathrm{c}} \tag{5.78}
$$

If $\mathrm{P}_{\mathrm{c}}^{+}$is a kinematical licit load for c, the kinematic theorem asserts that

$$
\mathrm{P}_{\mathrm{c}} \leq \mathrm{P}_{\mathrm{c}}^{+} \tag{5.79}
$$

Inequalities (5.76) to (5.79) may be combined into one continued inequality,

$$
\mathrm{P}_{\mathrm{i}}^{-} \leq \mathrm{P}_{\mathrm{i}} \leq \mathrm{P}_{1} \leq \mathrm{P}_{\mathrm{c}} \leq \mathrm{P}_{\mathrm{c}}^{+}, \tag{5.80}
$$

that enables us to bound the error introduced by the linearization process as follows.

![](./images/811968331895537664_28.jpg)

Fig. 5.27.

The limit load of a structure is directly proportional to the yield stress $\sigma_Y$ of the material. If the yield stress is multiplied by a factor that is greater or smaller than unity, the yield surface is similarly expanded or contracted with respect to the origin. Hence, if polygons i and c are homothetical with factor k, we have

$$
P_{c}=k P_{i} \tag{5.81}
$$

![](./images/811968331895537664_29.jpg)

Fig. 5.28.

If we want to bound $P_1$ from above and below, it is sufficient to know either $P_i$ or $P_c$, say $P_i$. We then determine the lowest expansion factor k that makes polygon i become circumscribed to e. Note also that, if the stress point, for all plastic regions, remains on a

certain part of curve e, as AB in fig. 5.28, the yield polygon obtained by expansion of polygon i must be external to curve e in that part only. This remark enables us to use the smallest possible expansion factor k.

### 5.5.3. Linearization process.
A first method consists of finding the exact yield surface and then inscribe (or circumscribe) more or less arbitrarily a polyhedron in order to simplify the subsequent analysis.

A second point of view consists of using an approximation not to the yield surface but to the structure itself [5.11].

![](./images/811968331895537664_30.jpg)

Fig. 5.29.

Consider (fig. 5.29) a structure (plate, shell) of the "ideal sandwich" type defined in Section 5.4.3, example 2. On a cross section, the axial force and bending moment per unit of length are [see eq. (5.53)]

$$
\mathrm{N}=\frac{\mathrm{t}^{*}}{2}\left(\sigma_{\mathrm{i}}+\sigma_{\mathrm{e}}\right), \tag{5.82}
$$

$$
\mathrm{M}=\frac{\mathrm{t}^{*} \mathrm{H}}{4}\left(\sigma_{\mathrm{i}}-\sigma_{\mathrm{e}}\right), \tag{5.83}
$$

where $\sigma_{\mathrm{i}}$ and $\sigma_{\mathrm{e}}$ are the normal stresses in the internal and external sheets, respectively, $\mathrm{t}^{*} / 2$ the thickness of each sheet and H the core thickness. A twisting moment $\mathrm{M}_{\mathrm{t}}$ (per unit of length) will produce shear stresses $\tau$ such that

$$
\mathrm{M}_{\mathrm{t}}=\tau \frac{\mathrm{t}^{*}}{2} \mathrm{H}. \tag{5.84}
$$

If we denote by $\tau_{\mathrm{Y}}^{*}$ the yield shearing stress of the sandwich sheets and $\sigma_{\mathrm{Y}}^{*}$ its yield stress in tension, the full plastic axial force, bending moment and twisting moment are

$$
\mathrm{N}_{\mathrm{p}}^{*}=\sigma_{\mathrm{Y}}^{*} \mathrm{t}^{*},
$$

$$
\mathrm{M}_{\mathrm{p}}^{*}=\sigma_{\mathrm{Y}}^{*} \mathrm{H} \frac{\mathrm{t}^{*}}{2},
$$

$$
\mathrm{M}_{\mathrm{tp}}^{*}=\tau_{\mathrm{Y}}^{*} \mathrm{H} \frac{\mathrm{t}^{*}}{2},
$$

For the sandwich structure to be substituted for a structure with uniform cross section of thickness $\mathrm{t}$ and yield stresses $\sigma_{\mathrm{Y}}$ and $\tau_{\mathrm{Y}}, \mathrm{H}$ and $\mathrm{t}^{*}$ must be so chosen as to satisfy

$$
\sigma_{\mathrm{Y}} \mathrm{t}=\sigma_{\mathrm{Y}}^{*} \mathrm{t}^{*} \equiv \mathrm{N}_{\mathrm{p}}, \tag{5.85}
$$

$$
\sigma_{\mathrm{Y}}^{*} \mathrm{H} \frac{\mathrm{t}^{*}}{2}=\sigma_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4} \equiv \mathrm{M}_{\mathrm{p}}, \tag{5.86}
$$

$$
\tau_{\mathrm{Y}}^{*} \mathrm{H} \frac{\mathrm{t}^{*}}{2}=\tau_{\mathrm{Y}} \frac{\mathrm{t}^{2}}{4} \equiv \mathrm{M}_{\mathrm{tp}}. \tag{5.87}
$$

Relations (5.85) to (5.87) then give

$$
\begin{aligned}
\sigma_{\mathrm{Y}}^{*} \mathrm{t}^{*} & =\sigma_{\mathrm{Y}} \mathrm{t}, \\
\mathrm{H} & =\frac{\mathrm{t}}{2}, \\
\frac{\tau_{\mathrm{Y}}^{*}}{\sigma_{\mathrm{Y}}^{*}} & =\frac{\tau_{\mathrm{Y}}}{\sigma_{\mathrm{Y}}}.
\end{aligned} \tag{5.88}
$$

The last relation of eqs.(5.88) just means that the same physical yield condition must hold for both structures.

Because the generalized stresses N, M, $M_t$ are linear functions of the stress components (relation (5.82) to (5.84)), any linear yield condition in terms of the stress components will thus generate a linear yield condition in terms of generalized stresses. Hence, the preceding procedure directly furnishes an approximate yield polyhedron without recourse to the exact yield surface. This polyhedron is inscribed in the exact yield surface because the latter is convex and, according to relations (5.88), both have in common the points on the axes. Fig. 5.30 shows, for example, the yield polyhedron of a sandwich cylindrical shell axisymmetrically loaded and made of a Tresca material. Equations of the various planes are :

![](./images/811968331895537664_31.jpg)

Fig. 5.30.

$$
\begin{align*}
\mathrm{I}: \quad & n_\theta = 1, \\
\mathrm{II}: \quad & n_\theta - n_x = 1, \\
\mathrm{III}: \quad & n_x - m_x = -1, \\
\mathrm{IV}: \quad & 2\,n_\theta - n_x + m_x = 2 \\
\mathrm{V}: \quad & 2\,n_\theta - n_x - m_x = 2, \tag{5.89}
\end{align*}
$$

Coordinates x and $\theta$ are as indicated in fig. 5.22. This yield polyhedron is a linearization of the yield surface in fig. 5.12, with which it should be compared (subscripts 1 and 2 becoming x and $\theta$, respectively).

#### 5.5.4. Example of application.

Following Hodge and Sawczuk [5.12], consider an infinitely long cylindrical shell without axial force, loaded in a cross section by a radial uniform line load of total magnitude

![](./images/811968331895537664_32.jpg)

$2\mathrm{F}_\mathrm{o}$ (fig. 5.31).

Because of the symmetry, the plastic region at collapse will extend over an (unknown) length x, on each side of the loaded cross section where we locate the origin of the abscissae. The only generalized stresses are $\mathrm{M}_\mathrm{x}$ and $\mathrm{N}_\theta$ (fig. 5.31).

We assume the real shell to exhibit uniform thickness and satisfy von Mises' yield criterion. We compare it to these shells regarded as approximations to the former : (a) sandwich shell made of von Mises material ; (b) uniform shell made of Tresca material ; (c) sandwich shell made of Tresca material ; (d) shell with the (arbitrarily simple) "limited interaction" yield curve.

The various yield curves are shown in fig. 5.32. In the absence of twisting moment, conditions (5.88) reduce to

$$
\stackrel{*}{\sigma_{\mathrm{Y}}} \mathrm{t}=\sigma_{\mathrm{Y}} \mathrm{t},
$$

$$
H = \frac{t}{2}
$$

![](./images/811968331895537664_33.jpg)

Fig. 5.32. Interaction curves.

The lines 2, 3 and 4 in fig. 5.32 were obtained in Section 5.4. Line 1 was given by Hodge [5.13] as a special case of the yield surface of a shell of revolution loaded with rotational symmetry. Line 5 was arbitrarily chosen for the sake of simplicity.

Line 4 is a linear approximation to lines 1, 2 and 3. Line 5 is an arbitrary linear approximation to lines 1 to 4.

The load was nondimensionalized as follow : $f_{0}=R^{1/2}\left(M_{p}N_{p}\right)^{-1/2}F_{0}$.

The various exact limit loads obtained by Hodge and Sawczuk are given in column
3 of table 5.4.

In column 4 we find the deviations of the preceding limit loads from those of the real shell (line 1 in fig. 5.32). Column 5 contains the relative deviations. The figures given in columns 6 and 7 were obtained as follows : each yield curve was similarly enlarged or reduced by a factor k (see Section 5.5.2) to become : (a) external to curve 1 for curves 2, 3, and 4 or (b) internal to curve 1 for curve 5 (see fig. 5.33). The exact yield curve is thus bounded, for each "approximation" shell, by two approximate curves that furnish lower and upper bounds for the limit load. The relative deviations of these bounds are indicated in columns 6 and 7. Note that the original "limited interaction" curve (line 5 in fig. 5.32) gives

neither a lower bound nor an upper bound as it arbitrarily cuts across the exact yield curve. After geometrically similar expansion or reduction, it does furnish bounds to the limit load, which differ appreciably from the other bounds. Nevertheless, the original curve itself furnishes a fairly good approximate limit load.

Table 5.4. Comparison of reduced limit loads $\mathrm{f}_{\mathrm{o}}=\mathrm{R}^{1 / 2}\left(\mathrm{M}_{\mathrm{p}} \mathrm{N}_{\mathrm{p}}\right)^{-1 / 2} \mathrm{~F}_{\mathrm{o}}$.

<table>
<thead>
<tr>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
</tr>
<tr>
<th rowspan="2">Type of shell</th>
<th rowspan="2">Yield condition</th>
<th rowspan="2">$\mathrm{f}_{\mathrm{o}}$</th>
<th>Deviation from uniform von Mises</th>
<th rowspan="2">Actual</th>
<th>Deviation</th>
<th></th>
</tr>
<tr>
<th></th>
<th>Lower bound</th>
<th>Upper bound</th>
</tr>
</thead>
<tbody>
<tr>
<td>Uniform</td>
<td>von Mises</td>
<td>1.949</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Sandwich</td>
<td>von Mises</td>
<td>1.905</td>
<td>- 0.044</td>
<td>- 2.3</td>
<td>- 2.3</td>
<td>2.6</td>
</tr>
<tr>
<td>Uniform</td>
<td>Tresca</td>
<td>1.826</td>
<td>- 0.123</td>
<td>- 6.3</td>
<td>- 6.3</td>
<td>7.9</td>
</tr>
<tr>
<td>Sandwich</td>
<td>Tresca</td>
<td>1.732</td>
<td>- 0.217</td>
<td>- 11.1</td>
<td>- 11.1</td>
<td>5.7</td>
</tr>
<tr>
<td>Limited interaction curve</td>
<td></td>
<td>2.000</td>
<td>+ 0.051</td>
<td>2.6</td>
<td>- 20.0</td>
<td>18.2</td>
</tr>
</tbody>
</table>

![](./images/811968331895537664_34.jpg)

![](./images/811968331895537664_35.jpg)

Fig. 5.34.

![](./images/811968331895537664_36.jpg)

Fig. 5.35.

Diagrams of the reduced bending moment $m_x = \frac{M_x}{M_p}$ and axial force $n_\theta = \frac{N_\theta}{N_p}$ are shown in figs. 5.34 and 5.35, where elastic diagrams corresponding to the maximum load in elastic range are also given. It is easily seen that an important redistribution of both $n_\theta$ and $m_x$ takes place prior to collapse.

### 5.6. Yield conditions of reinforced concrete plates and shells.

#### 5.6.1. General assumptions.

Each layer of concrete is assumed to be in state of plane stress and regarded as a rigid-perfectly plastic material. In terms of the in-plane principal stresses $\sigma_1$ and $\sigma_2$, the yield condition of such a layer is given in fig. 5.36, where $\sigma_c'$ is the compressive yield strength (crushing strength), whereas the tensile stress has a vanishing value because the concrete is cracked under any tensile stress.

Steel reinforcements are supposed to have a rigid-perfectly plastic behaviour, with the same tensile and compressive yield stress. Now, according to Johansen [5.14], we introduce the important concept of "yield lines" ("fracture lines" or "hinges lines"). Indeed, cracks patterns can be observed in some local regions of reinforced concrete slabs or shells (see fig. 9.2, 9.3 and 10.3). A yield-line is interpreted as a mathematical idealization of such a narrow zone.

The present yield condition, established by the junior author (G.S) by using the rate of dissipation (upper bound method, [5.15], [5.16]), extends those by Capurso [5.17] and Sawczuk-Olszak [5.18].

A layer of parallel reinforcing bars separated by a distance p and inclined of the angle $\alpha$ on the normal to the yield-line (fig. 5.3) is constituted by a number of bars equal to

$$
n = \frac{|\cos\alpha|}{p} \tag{5.90}
$$

for a unit length of yield line.

If A denotes the cross-sectional area of any reinforcement, the strength force of the layer by unit length of yield-line is equal to :

$$
N_s = \Omega_s \sigma_Y \tag{5.91}
$$

where the quantity :

$$
\Omega_{s}=\frac{A}{p} \cos ^{2} \alpha
$$

(5.92)

involves the reinforcement ratio A/p. This quantity is additive if we consider several layers.

### 5.6.2. The dissipation in a concrete layer.

First, the rate of dissipation by unit of volume $D_{c}$ associated with the yield curve of fig. 5.36 is given by :

$$
D_{c}=\sigma_{1} \dot{\varepsilon}_{1}+\sigma_{2} \dot{\varepsilon}_{2}
$$

(5.93)

Its value for each regime of plastic yielding is obtained by the use of the normality law and is given in table 5.5.

Table 5.5.

<table>
  <thead>
    <tr>
      <th>Regime</th>
      <th>Constraints</th>
      <th>Yielding law</th>
      <th>Power of dissipation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>O</td>
      <td>$\sigma_{1}=\sigma_{2}=0$</td>
      <td>$\dot{\varepsilon}_{1} \geq 0, \dot{\varepsilon}_{1} \dot{\varepsilon}_{2} \geq 0$</td>
      <td>$D_{c}=0$</td>
    </tr>
    <tr>
      <td>OA</td>
      <td>$\sigma_{2}=0$</td>
      <td>$\dot{\varepsilon}_{1}=0, \dot{\varepsilon}_{2} \geq 0$</td>
      <td>$D_{c}=0$</td>
    </tr>
    <tr>
      <td>A</td>
      <td>$\sigma_{1}=-\sigma_{c}' \sigma_{2}=0$</td>
      <td>$\dot{\varepsilon}_{1} \leq 0, \dot{\varepsilon}_{1} \dot{\varepsilon}_{2} \leq 0$</td>
      <td>$D_{c}=-\sigma_{c}' \dot{\varepsilon}_{1}$</td>
    </tr>
    <tr>
      <td>AB</td>
      <td>$\sigma_{1}=-\sigma_{c}'$</td>
      <td>$\dot{\varepsilon}_{1} \leq 0, \dot{\varepsilon}_{2}=0$</td>
      <td>$D_{c}=-\sigma_{c}' \dot{\varepsilon}_{1}$</td>
    </tr>
    <tr>
      <td>B<br>(other regimes<br>by symmetry)</td>
      <td>$\sigma_{1}=\sigma_{2}=-\sigma_{c}'$</td>
      <td>$\dot{\varepsilon}_{1} \leq 0, \dot{\varepsilon}_{1} \dot{\varepsilon}_{2} \geq 0$</td>
      <td>$D_{c}=-\sigma_{c}'(\dot{\varepsilon}_{1}+\dot{\varepsilon}_{2})$</td>
    </tr>
  </tbody>
</table>

### 5.6.3. Assumptions on discontinuities.

Let $\dot{w}$ be the rate of transverse displacement, $\dot{u}$ and $\dot{v}$ the rates of the tangential displacements, respectively normal and parallel to the yield-line (fig. 5.37). $\dot{w}$ must obviously remain a continuous function, and consequently, $\frac{\partial \dot{w}}{\partial s}$ also :

$$
\dot{w}]=\frac{\partial \dot{w}}{\partial s}]=0
$$

(5.94)

Table 5.6.

<table>
  <thead>
    <tr>
      <th>Regime</th>
      <th>Range of $\eta$</th>
      <th>Plastic yielding in the reinforcement</th>
      <th>Expression of n</th>
      <th>Expression of m</th>
      <th>Extreme points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CD'</td>
      <td>$-1 \leq -\eta < \rho$</td>
      <td>$\dot{\overline{u}}_o + 2\rho\dot{\theta} < 0$</td>
      <td>$n=-\gamma - \frac{1+\eta}{2}$</td>
      <td>$m=-2\gamma\rho - \frac{1+\eta^2}{2}$</td>
      <td>
        C $(-\gamma-1, -2\gamma\rho)$<br>
        D' $\left(-\gamma-\frac{1-\rho}{2}, -2\gamma\rho-\frac{1-\rho^2}{2}\right)$
      </td>
    </tr>
    <tr>
      <td>AA'</td>
      <td>$\rho < -\eta \leq 1$</td>
      <td>$\dot{\overline{u}}_o + 2\theta\dot{\rho} < 0$</td>
      <td>$n=\gamma - \frac{1+\eta}{2}$</td>
      <td>$m=2\gamma\rho - \frac{1+\eta^2}{2}$</td>
      <td>
        A $(\gamma, 2\gamma\rho)$<br>
        A' $\left(\gamma-\frac{1-\rho}{2}, 2\gamma\rho-\frac{1-\rho^2}{2}\right)$
      </td>
    </tr>
    <tr>
      <td>A'D'</td>
      <td>$\eta = -\rho$</td>
      <td>$\dot{\overline{u}}_o + 2\rho\dot{\theta} = 0$</td>
      <td>
        $n=\gamma s - \frac{1-\rho}{2}$<br>
        $\leq$<br>
        $(|s| \leq 1)$
      </td>
      <td>$m=2\gamma\rho s - \frac{1+\rho^2}{2}$</td>
      <td>
        A' $\left(\gamma-\frac{1-\rho}{2}, 2\gamma\rho-\frac{1-\rho^2}{2}\right)$<br>
        D' $\left(-\gamma-\frac{1-\rho}{2}, -2\gamma\rho-\frac{1-\rho^2}{2}\right)$
      </td>
    </tr>
  </tbody>
</table>

Table 5.7.

<table>
  <thead>
    <tr>
      <th>Regime</th>
      <th>Range of $\eta$</th>
      <th>Plastic yielding in the reinforcement</th>
      <th>Expression of n</th>
      <th>Expression of m</th>
      <th>Extreme points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AA'</td>
      <td>$-1 \leq \eta < -\rho$</td>
      <td>$\dot{\overline{u}}_o + 2\rho\dot{\theta} > 0$<br><br>$\dot{\overline{u}}_o - 2\rho\dot{\theta} > 0$</td>
      <td>$n=-\frac{1+\eta}{2}-2\gamma$</td>
      <td>$m=\frac{1-\eta^2}{2}$</td>
      <td>A $[2\gamma, 0]$<br><br>$A'\left[-\frac{1-\rho}{2}+2\gamma, \frac{1-\rho^2}{2}\right]$</td>
    </tr>
    <tr>
      <td>B'B''</td>
      <td>$-\rho < \eta < \rho$</td>
      <td>$\dot{\overline{u}}_o + 2\rho\dot{\theta} > 0$<br><br>$\dot{\overline{u}}_o - 2\rho\dot{\theta} < 0$</td>
      <td>$n=-\frac{1+\eta}{2}$</td>
      <td>$m=\frac{1-\eta^2}{2}+4\gamma\rho$</td>
      <td>$B'\left[-\frac{1-\rho}{2}, \frac{1-\rho^2}{2}+4\gamma\rho\right]$<br><br>$B''\left[-\frac{1+\rho}{2}, \frac{1-\rho^2}{2}+4\gamma\rho\right]$</td>
    </tr>
    <tr>
      <td>C''C</td>
      <td>$\rho < \eta \leq 1$</td>
      <td>$\dot{\overline{u}}_o + 2\rho\dot{\theta} < 0$<br><br>$\dot{\overline{u}}_o - 2\rho\dot{\theta} < 0$</td>
      <td>$n=-\frac{1+\eta}{2}-2\gamma$</td>
      <td>$m=\frac{1-\eta^2}{2}$</td>
      <td>$C''\left[-\frac{1+\rho}{2}-2\gamma, \frac{1-\rho^2}{2}\right]$<br><br>C $[-1-2\gamma, 0]$</td>
    </tr>
  </tbody>
</table>

The problem becomes simpler if we make the following assumptions :

a) no sliding of both sides of the yield line :

$$\dot{\mathrm{v}}]=0 \tag{5.95}$$

b) plane cross-sections remain plane during deformation :

$$\dot{\mathrm{u}}]=\dot{\mathrm{u}}_{\mathrm{o}}+\mathrm{z} \dot{\theta} \tag{5.96}$$

with

$$\dot{\mathrm{u}}_{\mathrm{o}}=\dot{\mathrm{u}}], \quad \mathrm{z}=0, \quad \dot{\theta}=\frac{\partial \dot{\mathrm{w}}}{\partial \mathrm{n}}]. \tag{5.97}$$

Hence, the strain rates in the yield-line are given by :

$$\dot{\varepsilon}_{\mathrm{n}}=\dot{\mathrm{u}}_{\mathrm{o}}+\mathrm{z} \dot{\theta}, \quad \dot{\varepsilon}_{\mathrm{s}}=0, \quad \dot{\gamma}_{\mathrm{ns}}=0. \tag{5.98}$$

### 5.6.4. Yield condition for shells with simple reinforcement.

It is obvious that n and s (fig. 5.37) are the principal axes of strain rates.

As $\dot{\varepsilon}_{\mathrm{s}}$ vanishes, the concrete yields according to regime OC when $\dot{\varepsilon}_{\mathrm{n}}>0$, and to the regime AB when $\dot{\varepsilon}_{\mathrm{n}} \leq 0$. First, let us assume that the upper layers of the concrete are in compression. Let $\eta$ be the non-dimensional ordinate of the neutral axis so that $\dot{\varepsilon}_{\mathrm{n}}$ is negative for $\mathrm{z}<\eta \frac{\mathrm{t}}{2}$ (fig. 5.38). According to table 5.5, the rate of dissipation is :

$$
\begin{aligned}
\mathrm{D}_{\mathrm{c}}=-\sigma_{\mathrm{c}}^{\prime}\left(\dot{\mathrm{u}}_{\mathrm{o}}+\mathrm{z} \dot{\theta}\right) & \text { if } \mathrm{z} \leq \eta \frac{\mathrm{t}}{2}, \\
\mathrm{D}_{\mathrm{c}}=0 & \text { if } \mathrm{z}>\eta \frac{\mathrm{t}}{2}.
\end{aligned}
$$

Now, let $\rho \frac{\mathrm{t}}{2}$ be the ordinate of the steel reinforcement (fig.5.38). The rate of dissipation in the reinforcement per unit of length of yield-line is :

$$D_{s}=\sigma_{y} \Omega_{s}|\dot{u}_{0}+\rho \frac{t}{2} \dot{\theta}|.$$

![](./images/811968331895537664_37.jpg)

Fig. 5.36.

![](./images/811968331895537664_38.jpg)

Fig.5.37.

![](./images/811968331895537664_39.jpg)

Fig. 5.38.

![](./images/811968331895537664_40.jpg)

Fig. 5.39.

The power of dissipation by unit length of yield-line is therefore :

$$\Phi=-\sigma_{c}^{\prime} \int_{-1 / 2}^{\eta / 2}\left(\dot{u}_{0}+z \dot{\theta}\right) d z+\sigma_{y} \Omega_{s}\left|\dot{u}_{0}+\rho \frac{t}{2} \dot{\theta}\right|.$$

At yielding, the cross-section is subjected to a bending moment M and to a normal force N which are deduces by the normality law :

![](./images/811968331895537664_41.jpg)

Fig. 5.40.

$$
\mathrm{N}=\frac{\partial \Phi}{\partial \dot{\mathrm{u}}_{\mathrm{o}}}, \quad \mathrm{M}=\frac{\partial \Phi}{\partial \dot{\theta}}, \quad \Phi=\mathrm{N} \dot{\mathrm{u}}_{\mathrm{o}}+\mathrm{M} \dot{\theta}.
$$

Introducing the following reduced variables:

$$
\mathrm{n}=\frac{\mathrm{N}}{\sigma_{\mathrm{c}}^{\prime} \mathrm{t}}, \quad \mathrm{m}=\frac{\mathrm{M}}{\frac{\sigma_{\mathrm{c}}^{\prime} \mathrm{t}^{2}}{4}}, \quad \dot{\overline{\mathrm{u}}}_{\mathrm{o}}=\frac{\dot{\mathrm{u}}_{\mathrm{o}}}{\frac{\mathrm{t}}{4}}, \quad \varphi=\frac{\Phi}{\frac{\sigma_{\mathrm{c}}^{\prime} \mathrm{t}^{2}}{4}},
\tag{5.99}
$$

one has :

$$
\mathrm{n}=\frac{\partial \varphi}{\partial \dot{\overline{\mathrm{u}}}_{\mathrm{o}}}, \quad \mathrm{m}=\frac{\partial \varphi}{\partial \dot{\theta}}, \quad \varphi=\mathrm{n} \dot{\overline{\mathrm{u}}}_{\mathrm{o}}+\mathrm{m} \dot{\theta}.
\tag{5.100}
$$

If $\gamma$ denotes the reduced reinforcement ratio

$$
\gamma=\frac{\sigma_{\mathrm{y}} \Omega_{\mathrm{s}}}{\sigma_{\mathrm{c}}^{\prime} \mathrm{t}}
\tag{5.101}
$$

the dissipation is expressed, in terms of reduced variables, by

$$
\varphi = -\frac{1 + \eta}{2} \dot{\overline{u}}_{0} + \gamma \dot{\overline{u}}_{0} + 2\rho \dot{\theta} + \frac{1 - \eta^{2}}{2} \dot{\theta}
\tag{5.102}
$$

This expression, which is not differentiable, has to be discussed with regard to the regime of plastic yielding :

a) the reinforcement is fully in tension :

$$
-1 \leq \eta < \rho \ , \ \dot{\overline{u}}_{0} + 2\rho \dot{\theta} > 0
$$

The normality law (5.100) gives :

$$
n = \gamma - \frac{1 + \eta}{2} \ , \ \ m = 2 \gamma \rho + \frac{1 - \eta^{2}}{2}
\tag{5.103}
$$

To obtain the yield condition, one has to eliminate the parameter $\eta$ between both relations (5.103) and one gets easily the following condition :

$$
m = 2 n^{2} + 2 n (1 - 2 \gamma) + 2 \gamma^{2} - 2 \gamma(1 + \rho) = 0
\tag{5.104}
$$

wich is indentical to that of Sawczuk and Olszak [5.18] :

Equation (5.104) represents a parabole, the apex of which is point B, (fig. 5.39) with coordinates $(\gamma - \frac{1}{2}, 2 \gamma \rho + \frac{1}{2})$ ; (5.104) is obtained by translation of $(\gamma, 2 \gamma \rho)$ from the parabole corresponding to the plain concrete :

$$
m = -2 n (1 + n)
\tag{5.105}
$$

As the regime under consideration is allowed only when $\eta$ is varying between -1 and $\rho$, we must preserve only the part of the parabole between points A $(\gamma, 2 \gamma \rho)$ and B' $\left(\gamma - \frac{1 + \rho}{2}, 2 \gamma \rho + \frac{1 - \rho^{2}}{2}\right)$ (fig. 5.39).

b) the reinforcement is fully in compression :

$$
\rho < \eta < 1 \ , \ \ \dot{\overline{u}}_{0} + 2 \rho \dot{\theta} < 0
$$

The normality law gives :

$$
n = - \gamma - \frac { 1 + \eta } { 2 } \quad , \quad m = - 2 \gamma \rho + \frac { 1 - \eta ^ { 2 } } { 2 } \tag{5.106}
$$

The stress state point belongs to a parabole obtained by translation of the parabole (5.105), but now in the opposite way $(-\gamma,-2\gamma\rho)$. As above, one must consider only the segment between the points $\mathrm{C'} \left(-\gamma-\frac{1+\rho}{2},-2\gamma\rho+\frac{1-\rho^2}{2}\right)$ and $\mathrm{C}\ (-\gamma-1,-2\gamma\rho)$.

c) the reinforcement is partly in compression :

$$
\eta = \rho, \quad \overline { \mathrm { u } } _ { \mathrm { o } } + 2 \rho \dot { \theta } = 0.
$$

There is a bifurcation of the stresses. The stress state point belongs to the straight segment between C' and B'. (*)

Il it is now assumed that the lower layers of the concrete are in compression $(z < \frac{\eta_t}{2})$. Three new regimes of plastic yielding are obtained in a similar way ; they are shown in table 5.5.

Finally, the yield curve is ABB'C'CDD'A'A (fig. 5.39). We can chek easily the convexity of the rigid domain.

### 5.6.5 Yield condition for shells with double reinforcements.

By reasoning in a similar way, the yield curve for doubly reinforced shells is determined. The general case of the non-symmetrical reinforcement layers is done in [5.15]. The table 5.6 shows the quite interesting case of symmetrical reinforcements (at $z = \pm \rho$ dt with the same reinforcement ratio). These curves may be deduced in a way similar to that of Section 5.6.4 , from the following expression of the power of dissipation :

$$
\varphi = - \frac { 1 + \eta } { 2 } \dot { \overline { \mathrm { u } } } _ { \mathrm { o } } + \frac { 1 - \eta ^ { 2 } } { 2 } \dot { \theta } + \gamma \left( \left| \dot { \overline { \mathrm { u } } } _ { \mathrm { o } } + 2 \rho \dot { \theta } \right| + \left| \dot { \overline { \mathrm { u } } } _ { \mathrm { o } } - 2 \rho \dot { \theta } \right| \right). \tag{5.107}
$$

(*) Remark that the function (5.102) is not differentiable at this point. The straight segment B'C' is the subdifferential to $\varphi$, in the sense of convex analysis [5.19].)

Obviously, the yield curve is symmetrical with respect to the n-axis, as shown in fig.5.40.

As a conclusion, a general approach for any number of reinforcement layers is thus established. Besides, as shown in [5.18], the present upper bound is the exact solution because, through the normality law, a licit stress distribution can be associated to the corresponding yield mechanisms.

### 5.7. Discontinuities.

#### 5.7.1. Introduction.

When searching for fields of generalized stresses $Q_{i}$ and strain rates $\dot{q}_{i}$, it often proves useful to introduce discontinuities. We already know some of these discontinuities from Com. V. : at a plastic hinge in a beam the slope jumps by a finite amount and in a plastically bent segment of the beam the stress $\sigma$ jumps from $\sigma_{Y}$ to $-\sigma_{Y}$ when the neutral layer is crossed. For a given theory, that is, for a given degree of idealization, these discontinuities are permissible because perfect plasticity relaxes some of the restraints of geometrical compatibility.

As a rule, displacements normal to the midsurface of a shell will be kept continuous if the shell is not to break, but slopes might be discontinuous, as well as displacements in the tangent plane. Obviously, these discontinuities must be regarded as limiting cases (that is, idealizations consistent with the level of the theory used) of very rapid variations over very narrow regions, in which compatibility remains fully satisfied. The stress fields will also be allowed to exhibit some discontinuities because stresses are no longer related in a unique manner to a continuous strain field.

It is important to know what the admissible discontinuities are and what relations they obey. We refer the reader to Prager [5.20] and Hill [5.21]. We restrict ourselves hereafter to the minimum amount of indications necessary for the applications in the coming chapters.

#### 5.7.2. Stress discontinuities.

Consider (fig. 5.41) a point O on a surface of discontinuity S, and a elementary parallelepiped with center O. The general rule is as follows : *elementary forces and moments forces and moments that balance each other across the discontinuity surface must be continuous*.

On the other hand, elementary forces and moments that balance each other along the discontinuity surface may experience discontinuities across that surface.

If we examine, for example, a plate subjected to bending, the discontinuity surface reduces to a discontinuity line DD as shown in fig. 5.42. The action at O across the line is a moment vector with components $M_{x}$ and $M_{xy}$. This vector must be continuous across the

![](./images/811968331895537664_42.jpg)

Fig. 5.41.

![](./images/811968331895537664_43.jpg)

Fig. 5.42.

line, and hence there is no discontinuity admissible on $M_x$ and $M_{xy}$. We express this result symbolically as

$$\left.M_x\right]=0, \quad \left.M_{xy}\right]=0. \tag{5.108}$$

The remaining component $M_y$ of the moment tensor at O may be discontinuous :

$$\left.M_y\right] \neq 0. \tag{5.109}$$

The equilibrium of an element with center O furnishes the relations :

$$
\frac{\partial \mathrm{M}_{\mathrm{x}}}{\partial \mathrm{x}}+\frac{\partial \mathrm{M}_{\mathrm{xy}}}{\partial \mathrm{y}}=\mathrm{V}_{\mathrm{x}}, \tag{5.110}
$$

$$
\frac{\partial \mathrm{M}_{\mathrm{y}}}{\partial \mathrm{y}}+\frac{\partial \mathrm{M}_{\mathrm{xy}}}{\partial \mathrm{x}}=\mathrm{V}_{\mathrm{y}}, \tag{5.111}
$$

$$
\frac{\partial \mathrm{V}_{\mathrm{x}}}{\partial \mathrm{x}}+\frac{\partial \mathrm{V}_{\mathrm{y}}}{\partial \mathrm{y}}=-\mathrm{p}, \tag{5.112}
$$

Eq. (5.110) shows that

$$
\left.\mathrm{V}_{\mathrm{x}}\right]=0 \tag{5.113}
$$

whereas eq. (5.111) does not exclude

$$
\left.\mathrm{V}_{\mathrm{y}}\right] \neq 0 \tag{5.114}
$$

because $\frac{\partial \mathrm{M}_{\mathrm{y}}}{\partial \mathrm{y}}$ may be discontinuous as well as $\mathrm{M}_{\mathrm{y}}$.

The preceding considerations will be used in Chapter 10 in dealing with reinforced concrete shells, as well as in Chapter 11 where plane stress and strain are studied.

### 5.7.3. Strain-rate discontinuities.
As noted in Section 5.6.1, the field of transversal displacement rates $\dot{\mathrm{w}}$ must be continuous. If we examine the consequences of this statement for the first derivatives $\frac{\partial \dot{\mathrm{w}}}{\partial \mathrm{x}}$ and $\frac{\partial \dot{\mathrm{w}}}{\partial \mathrm{y}}$, we see that we must have

$$
\left.\frac{\partial \dot{\mathrm{w}}}{\partial \mathrm{y}}\right]=0 \tag{5.115}
$$

(to exclude different displacement rates for points with coordinates $(-\delta, \mathrm{ds} / 2)$ and $(+\delta, \mathrm{ds} / 2)$ with vanishingly small $\delta$, fig. 5.42). But we may have


$$
\left. \frac{\partial \dot{\mathrm{w}}}{\partial \mathrm{x}} \right] \neq 0 \tag{5.116}
$$

a situation where the discontinuity lime DD (fig. 5.42) is a "yield line" or "hinge line" that generalizes the plastic hinge of beams.

Obviously, a certain quantity of energy is dissipated in the strain-rate discontinuities, and due account must be taken of this fact. Indeed, some mechanisms will be made solely of discontinuities, as we shall see in the coming chapters.

### 5.8. Final remark.

Derivation of yield conditions is necessary not only for plates, shells and disks but also for beams subjected to combined loadings, as was discussed in Com. V in Section 5.2 for the simple case of simultaneous action of bending moment and axial force. Many papers have been devoted to this subject, among which we may quote the book of 1981 by Zyczkowski [5.22] containing detailed discussions of most (if not all) possible cases and an extremely extensive list of references.

### 5.9. Problems.

#### 5.9.1. Show that the yield condition for a sandwich shell of revolution axisymmetri- cally loaded and made of a von Mises material is :

$$
\left(\mathrm{n}_{\theta}+\mathrm{m}_{\theta}\right)^{2}-\left(\mathrm{n}_{\theta}+\mathrm{m}_{\theta}\right)\left(\mathrm{n}_{\varphi}+\mathrm{m}_{\varphi}\right)+\left(\mathrm{n}_{\varphi}+\mathrm{m}_{\varphi}\right)^{2}=1,
$$

$$
\left(\mathrm{n}_{\theta}-\mathrm{m}_{\theta}\right)^{2}-\left(\mathrm{n}_{\theta}-\mathrm{m}_{\theta}\right)\left(\mathrm{n}_{\varphi}-\mathrm{m}_{\varphi}\right)-\left(\mathrm{n}_{\varphi}-\mathrm{m}_{\varphi}\right)^{2}=1,
$$

with $\mathrm{n}=\mathrm{N} / \mathrm{N}_{\mathrm{p}}$ and $\mathrm{m}=\mathrm{M} / \mathrm{M}_{\mathrm{p}}$.

#### 5.9.2. Determine analytically the minimum amplification coefficient k to apply to the yield curve of the sandwich structure to have it circumscribe the exact yield curve (corresponding to uniform cross section of a Tresca material).

(a) For a rectangular beam subjected to bending and axial force the exact interaction curve being (see Com. V., relation (5.4)), $\mathrm{m}=1-\mathrm{n}^{2}$.

Answer : $\mathrm{k}=1.25$.

(b) For a cylindrical shell without axial force and axisymmetrically loaded.

Answer : $\mathrm{k}=1.225$.

5.9.3. Determine analytically the minimum reduction coefficient k to apply to the "square" yield condition (of the type of curve 5, fig. 5.32) to have it inscribed in the exact Tresca yield curve :

(a) When the yield curve $m_1$ versus $n_1$ is considered.

Answer : $k = 0.50$.

(b) When the yield curve $m_1$ versus $n_2$ is considered.

Answer : $k = 0.75$.

5.9.4. Determine the interaction curve for biaxial bending (Section 5.4.3, example 1) in the presence of a given nonvanishing twisting moment. *Hint* : use statical approach.

Answer :

$$
\mathrm{m}_{\mathrm{y}}\left(1-\mathrm{m}_{\mathrm{t}}^{2}\right)^{1 / 2}+\frac{3}{4} \mathrm{~m}_{\mathrm{x}}^{2}+\mathrm{m}_{\mathrm{t}}^{2}=1 \quad\left(\left|\mathrm{m}_{\mathrm{x}}\right|<\mathrm{m}_{\mathrm{y}}\right), \text{ with } \mathrm{m}_{\mathrm{t}}=\frac{\mathrm{M}_{\mathrm{t}}}{\mathrm{M}_{\mathrm{tp}}}
$$

### References.

[5.1] K. GIRKMAN, Flächentragwerke, Springer, 1959.

[5.2] C. MASSONNET, "Faut-il introduire l'hypothèse de Bernouilli en résistance des matériaux?", Bull. Soc.Roy. des Sci., **12** : 301, Liège, 1947.

[5.3] A.R. RIANITSYN, Calcul à la rupture et plasticité des constructions, p. 34, Eyrolles, Paris, 1959.

[5.4] W. PRAGER, "The General Theory of Limit Design", Proc. 8th Int. Congr. Appl. Mech., Istambul, 1952, **2** : 65, 1956.

[5.5] M. SAVE, "On Yield Conditions in Generalized Stresses", Quart. of Applied Math., **XIX** : 3, October 1961.

[5.6] "Structures", L'architecture d'aujourd'hui, March 1956.

[5.7] A. SAWCZUK and J. RYCHLEWSKI, "On Yield Surfaces for Plastic Shells", Archiwus Mechaniki Stosowanej, **1** : 12, 1960.

[5.8] E.T. ONAT and W. PRAGER, "Limit Analysis of Shells of Revolution", Koninki. Nederl. Akademie van Wetenschappen, Amsterdam, 57 : 5, 1954.

[5.9] P.G. HODGE Jr., "The Rigid-Plastic Analysis of Asymmetrically Loaded Cy- lindrical Shells", J. of Appl. Mech., 21 : 336, 1954.

[5.10] E.T. ONAT, "The Plastic Collapse of Cylindrical Shells under Axially Symme- trical Loading", Quart. Appl. Math. 13 : 63, 1955.

[5.11] P.G. HODGE Jr., "The Linearization of Plasticity Problems by Means of Non- homogeneous Materials", Proc. I.U.T.A.M. Symp., 1958. Nonhomogeneity in Elasticity and Plasticity, W. OLSZAK, ed. pp. 147-156, Pergamon Press, 1959. See also W. PRAGER, "On the Plastic Analysis of Sandwich Structures", in Problems in Continuum Mechanics, pp. 342-349, Soc. for Ind. and Appl. Math., Philadelphia, 1961.

[5.12] A. SAWCZUK and P.G. HODGE Jr., "Comparison of Yield Conditions for Circular Cylindrical shells", J. of the Franklin Inst., 269 : n°5, May 1960.

[5.13] P.G. HODGE Jr., "The Mises Yield condition for Rotationally Symmetric Shells", Quart. of Appl. Math., 18 : 305, 1961.

[5.14] K.W. JOHANSEN, "Yield line Theory", (translated from the Danish), Cement and Concrete Association, London, 1962.

[5.15] G. DE SAXCE, "Extension de la méthode de JOHANSEN aux coques en béton armé", Laboratoire de Mécanique des Matériaux et Stabilité des Constructions, Int. Report, Univ. of Liège, Belgium, 1984.

[5.16] G. DE SAXCE, "Extension of the Yield-line Method to the Reinforced Concrete Shells", Proceedings Int. Conf., IASS-85, Moscow, September 1985.

[5.17] M. CAPURSO, "Sul calcolo a rottura delle volte in cemento armato", Giornale del genio civile, fasc. 2, pp. 83-100, February 1966.

[5.18] A. SAWCZUK and W. OLSZAK, "A Method of Limit Analysis of Reinforced Concrete Thank", Int. Coll. on Simplified Calculation Methods, report III/6, Brussels, IASS-ABEM, 1961.

[5.19] I. EKELAND and R. TEMAM, "Convex Analysis and Variational Problems", New-York North Holland, 1975.

[5.20] W. PRAGER, "Discontinuous Field of Plastic Stress and Flow", Proc. 2nd U.S. Nat. Congr. Appl. Mech., 21-32, A.S.M.E., Ann Arbor, 1954.

[5.21] R. HILL, "Discontinuity Relations in Mechanics of Solids", Progress in Solid Mechanics, vol. II, Sneddon, Hill, ed., North-Holland Publ. Co., Amsterdam, 1961.

[5.22] M. ZYCZKOWSKI, "Combined Loadings in the Theory of Plasticity", PWN-Polish Scientific Publishers, Warsaw, 1981.

147