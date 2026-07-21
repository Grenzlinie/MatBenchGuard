
ARTICLE TYPE

Cite this: DOI: 10.1039/xxxxxxx

# Theory of defect motion in 2D passive and active nematic liquid crystals

Xingzhou Tang \( ^{a} \)  and Jonathan V. Selinger \( ^{*a} \) 

Received Date
Accepted Date

DOI: 10.1039/xxxxxxx

www.rsc.org/journalname

The motion of topological defects is an important feature of the dynamics of all liquid crystals, and is especially conspicuous in active liquid crystals. Understanding defect motion is a challenging theoretical problem, because the dynamics of orientational order is coupled with backflow of the fluid, and because a liquid crystal has several distinct viscosity coefficients. Here, we suggest a coarse-grained, variational approach, which describes the motion of defects as effective "particles." For passive liquid crystals, the theory shows how the drag depends on defect orientation, and shows the coupling between translational and rotational motion. For active liquid crystals, the theory provides an alternative way to describe motion induced by the activity coefficient.

## 1 Introduction

One important feature of the dynamics of liquid crystals is the motion of topological defects. In conventional, passive liquid crystals, defects form when a disordered phase is quenched into a more ordered phase, e.g., when isotropic is quenched into nematic, or smectic-A into smectic-C. After the quench, defects of opposite topological charge move together and annihilate each other. \( ^{1-11} \)  Their motion is driven by the interaction among defects, as well as by boundary conditions and applied fields. In active liquid crystals, defects are constantly in motion, forming and annihilating each other, driven by the activity of the underlying medium. \( ^{12-14} \)  In particular, defects of topological change +1/2 move with a characteristic velocity, while defects of topological charge -1/2 move diffusively.

To model the motion of topological defects, researchers have used two types of theoretical approaches. First, and most fundamentally, one can use hydrodynamic equations to describe the simultaneous evolution of the liquid crystal order and the flow velocity fields throughout the system. For passive liquid crystals, the hydrodynamic equations can be derived from Ericksen-Leslie theory expressed in terms of the director field, \( ^{15-18} \)  or from Beris-Edwards theory expressed in terms of the nematic order tensor. \( ^{19} \)  These equations can be solved numerically to obtain the liquid crystal order and flow velocity as functions of position and time, and these solutions can include the motion of defects. \( ^{20,21} \)  For active liquid crystals, one can likewise construct hydrodynamic equations, which include an extra term representing the activity. \( ^{22-26} \)  When these equations are solved for the liquid crystal order and flow velocity, they show the formation, motion, and
annihilation of defects.

As an alternative theoretical approach, one can model defects as if they were effective “particles,” which move in response to the total forces acting on them. This approach is more coarse-grained than hydrodynamics, because it describes the motion in terms of just a few degrees of freedom for each defect, while hydrodynamics describes liquid crystal order and flow velocity at every point in the system. The forces on defects have been investigated by several researchers over many years, in the context of passive liquid crystals. The elastic force was derived in a classic calculation, \( ^{27} \)  which shows that the interaction energy scales logarithmically with the separation r between defects, and hence the force scales as 1/r, in two dimensions (2D). The drag force was first derived through a simple theory, which assumes small defect velocity and neglects fluid flow, and thereby predicts a drag coefficient diverging logarithmically with system size. \( ^{28} \)  Further studies considered the possibility of larger defect velocity, so that the divergence with system size is cut off by a velocity-dependent length scale, leading to anomalous scaling of the drag with velocity. \( ^{29-32} \)  Other models included fluid flow, and hence found more complex results for the drag, which is different for positive and negative topological defects. \( ^{33-35} \) 

In the context of active liquid crystals, several papers have used the effective particle approach to predict the statistical mechanics of defect formation, motion, and annihilation. \( ^{36-40} \)  This approach has been generalized to the motion of topologically required defects on the surface of a sphere. \( ^{13} \)  Those studies have shown that active defects should not be regarded as just point particles, but rather as oriented particles. In particular, defects of topological charge +1/2 are surrounded by a comet-shaped director field, and the orientation of the comet determines the direction of self-propelled motion, while defects of topological charge -1/2 are
 

surrounded by a triangular director field. Moreover, experimental and numerical studies of systems with many defects have found statistical order in the defect orientations. \( ^{14} \)  Motivated by those results, Vromans and Giomi developed a formalism to describe defect orientations by vectors, \( ^{41} \)  and we generalized the formalism using tensors. \( ^{42} \)  Most recently, Shankar et al. derived the general orientational dynamics of defects in active liquid crystals, and used those results to predict the nonequilibrium defect unbinding transition. \( ^{43} \) 

The first purpose of this paper, in Section 2, is to apply the concept of defect orientation to the dynamics of passive liquid crystals. In our previous paper about defect orientations, we determined the effect of orientation on the elastic interaction between defects in passive liquid crystals. This interaction generates elastic forces and torques on the defects. Now, we investigate the effect of orientation on drag forces and torques. We determine what translational and orientational drag coefficients are allowed by the symmetry of defects, and assess how translational drag coefficients depend the relative angle between defect orientation and velocity.

In the course of doing this calculation, we develop a formalism for defect motion in passive liquid crystals based on the Rayleigh dissipation function. We suggest that this formalism is particularly useful for coarse-graining the dissipative dynamics, from the hydrodynamic level to the effective particle level, because the same dissipation function can be expressed on either length scale. On the hydrodynamic level, it can be written in terms of the liquid crystal order and the flow velocity fields, with Ericksen-Leslie viscosity coefficients. Similarly, on the effective particle level, it can be written in terms of symmetry-allowed combinations of the defect velocity and orientation vectors, with effective drag coefficients. By comparing these expressions, we can determine how the effective drag coefficients are related to Ericksen-Leslie viscosity coefficients.

One result of this calculation is that some Ericksen-Leslie viscosities give drag that is independent of defect orientation, while other viscosities give drag that depends on defect orientation. Another result is that the drag on a positive topological charge is less than drag on a negative topological charge because of backflow effects, and hence positive topological charges move more rapidly, in agreement with experiments \( ^{5,6,8} \)  and previous calculations using other methods. \( ^{20,21,33-35} \)  We provide an example of how this method can be used to predict the motion of a defect in a channel, driven by boundary conditions.

In Section 3, we apply the formalism based on the Rayleigh dissipation function back to active liquid crystals. This calculation shows that activity can be represented by one extra term in the dissipation function, either on the hydrodynamic level or the effective particle level. Although this term is not positive-definite, and hence is not exactly a dissipation, it plays the role of the Rayleigh dissipation function in the equations of motion. Because of this term, +1/2 defects move with a velocity proportional to the activity coefficient, in the direction given by the defect orientation vector. We construct two examples of how this method can predict the motion of a defect, driven by activity. We recognize that these results for active liquid crystals are not new; they have been

![](./images/867754548570095811_1.jpg)

Fig. 1 Examples of defects in a 2D nematic liquid crystal, with red arrows indicating the defect orientation.

found through other approaches by Shankar et al. \( ^{43} \)  and previous articles. Even so, we think it is useful to present them here, using the formalism of the Rayleigh dissipation function and defect orientation vector, because we find this approach to be intuitive and other investigators might also.

Finally, in Section 4, we discuss these results, and consider the prospects for extending them to other defects and textures in passive and active liquid crystals.

## 2 Passive liquid crystals

## 2.1 Statement of problem

In this work, we consider a 2D nematic liquid crystal. At each point in the material, there is some orientational order, which may be described by the director field  \( \hat{\mathbf{n}}(\mathbf{r}, t) \)  or the nematic order tensor  \( Q_{ij}(\mathbf{r}, t) \) , as well as a fluid flow velocity  \( \mathbf{v}(\mathbf{r}, t) \) . A full description of the dynamics must involve coupled partial differential equations for orientational order and fluid flow velocity. Solving these equations is a complex problem, which usually can only be done numerically. Our goal is to provide a coarse-grained description of the dynamics in terms of a reduced number of degrees of freedom associated with topological defects.

Suppose the liquid crystal has a topological defect at position  \( \mathbf{R}(t) = (X(t), Y(t)) \) . This defect is characterized by a topological charge k, which is a half-integer or integer indicating how many times the director rotates as one passes through a loop around the defect. As discussed in recent papers, \( ^{[41,42]} \)  the defect is also characterized by an orientation, which describes where the director points radially outward from (or inward toward) the defect. This orientation is defined up to rotations through an angle of  \( \pi/|1-k| \) . Hence, as we argued previously, \( ^{[42]} \)  the defect orientation in a nematic phase can be represented by a tensor of rank  \( 2|1-k| \) . For topological charge  \( k = +1/2 \) , the defect orientation is a unit vector  \( \mathbf{p}(t) = (\cos \Psi(t), \sin \Psi(t)) \) , as illustrated by the arrow in Fig. 1(a). For topological charge  \( k = -1/2 \) , the defect orientation is a third-rank, completely symmetric tensor  \( T_{ijk}(t) \) , with  \( T_{xxx} = -T_{xyy} = -T_{yxy} = -T_{yyx} = \frac{1}{2} \cos 3\Psi \)  and  \( T_{xxy} = T_{xyx} = T_{yxy} = -\frac{1}{2} \sin 3\Psi \) , as represented by the triad of arrows in Fig. 1(b). Hence, the coarse-grained description should provide equations of motion for  \( X(t) \) ,  \( Y(t) \) , and  \( \Psi(t) \) .

For the static physics, there is a well-established procedure to
 

go from the microscopic theory based on the director field \(\hat{\mathbf{n}}(\mathbf{r}, t)\) to the coarse-grained theory based on the defect degrees of freedom. In this procedure, one minimizes the Frank free energy, subject to the constraint that topological defects are at specified positions, and determines how the minimum free energy \(F\) depends on the defect positions. This dependence gives an effective interaction of defects with boundary conditions or with other defects. Thus, a classic calculation shows that the interaction energy scales logarithmically with the separation between defects.\(^{27}\) In our previous paper,\(^{42}\) we generalized this procedure to include defect orientation, and found that there is an extra interaction energy if the defects do not have the optimal relative orientation. Hence, the elastic force acting on the position of a defect is \(\mathbf{f}_{\mathrm{elastic}} = -\partial F / \partial \mathbf{R}\), and the elastic force acting on the defect orientation is \(f_{\mathrm{elastic}} = -\partial F / \partial \Psi\).

For the dynamic physics, we need a procedure to go from the microscopic theory based on the Ericksen-Leslie equations for \(\hat{\mathbf{n}}(\mathbf{r}, t)\) and \(\mathbf{v}(\mathbf{r}, t)\) to a coarse-grained theory based on defect degrees of freedom. Here, we suggest an approach using the Rayleigh dissipation function, which is a theoretical construction representing half the rate of dissipating mechanical energy into heat.

In most theoretical work, the fundamental hydrodynamic theory is expressed in terms of the stress tensor. However, an alternative formulation of the same theory is expressed in terms of the Rayleigh dissipation function. To our knowledge, this version of the theory was first suggested by Vertogen, \( ^{44,45} \)  and related ideas have been advocated by Sonnet and Virga \( ^{46,47} \)  and by Doi. \( ^{48} \)  This approach begins by listing all of the modes that dissipate energy. Next, the Rayleigh dissipation function is constructed as the most general scalar that is allowed by symmetry, at quadratic order in these modes. Finally, the drag forces are found by differentiating the dissipation function with respect to the generalized velocities.

On a microscopic basis, there are two modes that dissipate energy: the strain rate tensor,  \( A_{ij} = \frac{1}{2} (\partial v_j + \partial y_i) \) , and the director rotation with respect to the background fluid vorticity,  \( N_i = \dot{n}_i - \frac{1}{2} (\partial_j v_i - \partial_i v_j) n_j \) . In terms of these two modes, the most general quadratic dissipation function can be constructed as \( ^{49} \) 

 \[ \begin{align*}D=\int d^{2}r&\Big[\frac{1}{2}\alpha_{4}A_{ij}A_{ij}+\frac{1}{2}(\alpha_{5}+\alpha_{6})n_{i}A_{ij}A_{jk}n_{k}+\frac{1}{2}\alpha_{1}(n_{i}A_{ij}n_{j})^{2}\\&\quad+\frac{1}{2}\gamma_{1}N_{i}N_{i}+\gamma_{2}N_{i}A_{ij}n_{j}\Big].\end{align*} \quad (1) \] 

Here, the  \( \alpha \)  coefficients are the Leslie viscosities for fluid flow. Note that  \( \alpha_{4} \)  is the isotropic viscosity, while the other terms provide corrections depending on the direction of the strain rate with respect to the director. For a 2D incompressible flow (unlike 3D), we have the identity  \( 2n_{i}A_{ij}A_{jk}n_{k}=A_{ij}A_{ij} \) , and hence the second term is equivalent to the first. \( ^{50} \)  By comparison,  \( \gamma_{1} \)  is the rotational viscosity for director rotation with respect to the background fluid vorticity. Finally,  \( \gamma_{2} \)  is the torsion coefficient, which expresses a dissipative coupling between strain rate and director rotation.

On a macroscopic basis, we can repeat the same type of analysis based purely on symmetry considerations. For a +1/2 defect, there are two modes that dissipate energy: the translational velocity  \( \dot{R} \)  and the rotational velocity  \( \dot{p} \) . In terms of those two modes, the most general quadratic dissipation function can be constructed as

 \[ D=\frac{1}{2}D_{1}|\dot{\mathbf{R}}|^{2}+\frac{1}{2}D_{2}(\mathbf{p}\cdot\dot{\mathbf{R}})^{2}+\frac{1}{2}D_{3}|\dot{\mathbf{p}}|^{2}+D_{4}\dot{\mathbf{p}}\cdot\dot{\mathbf{R}}. \quad (2) \] 

Here,  \( D_{1} \)  shows the energy dissipated by defect translation, and  \( D_{2} \)  shows how that energy dissipation depends on the defect orientation with respect to the velocity. Similarly,  \( D_{3} \)  shows the energy dissipated by defect rotation, and  \( D_{4} \)  shows a dissipative coupling between defect translation and rotation. This quadratic form is positive-definite if  \( D_{4}^{2} < D_{1}D_{3} \) . The drag force acting on the defect position is

 \[ \mathbf{f}_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\dot{\mathbf{R}}}=-D_{1}\dot{\mathbf{R}}-D_{2}\mathbf{p}(\mathbf{p}\cdot\dot{\mathbf{R}})-D_{4}\dot{\mathbf{p}}, \quad (3) \] 

and the drag force acting on the defect orientation is

 \[ f_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\dot{\mathbf{\Psi}}}=-D_{3}\dot{\mathbf{\Psi}}-D_{4}\mathbf{p}\times\dot{\mathbf{R}}. \quad (4) \] 

Those forces can be combined into a matrix equation as

 \[ \begin{bmatrix}f_{x}^{\mathrm{d r a g}}\\ f_{y}^{\mathrm{d r a}g}\\ f_{\psi}^{\mathrm{d r a g}}\end{bmatrix}=-\begin{bmatrix}D_{1}+D_{2}\cos^{2}\Psi&D_{2}\cos\Psi\sin\Psi&-D_{4}\sin\Psi\\ D_{2}\cos\Psi\sin\Psi&D_{1}+D_{2}\sin^{2}\Psi&D_{4}\cos\Psi\\ -D_{4}\sin\Psi&D_{4}\cos\Psi&D_{3}\end{bmatrix}\begin{bmatrix}\dot{x}\\\dot{y}\\\dot{\Psi}\end{bmatrix}. \quad (5) \] 

If a translational or rotational force is applied to the defect, the steady-state response is given by  \( f_{i}^{app} + f_{i}^{drag} = 0 \) , and hence

 \[ \begin{bmatrix}\dot{x}\\\dot{y}\\\dot{\Psi}\end{bmatrix}=\begin{bmatrix}D_{1}+D_{2}\cos^{2}\Psi&D_{2}\cos\Psi\sin\Psi&-D_{4}\sin\Psi\\ D_{2}\cos\Psi\sin\Psi&D_{1}+D_{2}\cos^{2}\Psi&D_{4}\cos\Psi\\ -D_{4}\sin\Psi&D_{4}\cos\Psi&D_{3}\end{bmatrix}^{-1}\begin{bmatrix}f_{x}^{\mathrm{app}}\\ f_{y}^{\mathrm{app}}\\\ f_{\psi}^{\mathrm{app}}\end{bmatrix}. \quad (6) \] 

Hence, a +1/2 defect responds to an applied force with a mobility tensor given by the inverse matrix in Eq. (6). This mobility tensor has the same structure as that of a boomerang-shaped colloidal particle. \( ^{51} \)  In particular, we note that a translational force can induce rotational motion, and a rotational force can induce translational motion.

Similar considerations apply to a -1/2 defect. There are two modes that dissipate energy: The translational velocity  \( \dot{R} \)  and the time derivative of the orientation tensor  \( \dot{T}_{ijk} \) . In terms of these modes, most general quadratic dissipation function becomes

 \[ D=\frac{1}{2}D_{1}^{\prime}|\dot{\mathbf{R}}|^{2}+\frac{1}{2}D_{3}^{\prime}\dot{T}_{i j k}\dot{T}_{i^{\prime}j k}=\frac{1}{2}D_{1}^{\prime}|\dot{\mathbf{R}}|^{2}+\frac{9}{2}D_{3}^{\prime}\dot{\Psi}^{2}, \quad (7) \] 

where  \( D_{1}^{\prime} \)  shows the dissipation due to defect translation and  \( D_{3}^{\prime} \)  shows the dissipation due to defect rotation. At quadratic order, symmetry does not allow any couplings between translation and orientation. Hence, the matrix equation for drag forces is simply

 \[ \begin{bmatrix}f_{x}^{\mathrm{d r a g}}\\ f_{y}^{\mathrm{d r a}g}\\ f_{\psi}^{\mathrm{d r a g}}\end{bmatrix}=-\begin{bmatrix}D_{1}^{\prime}&0&0\\ 0&D_{1}^{\prime}&\\ 0&0&9D_{3}^{\prime}\end{bmatrix}\begin{bmatrix}\dot{x}\\ \dot{y}\\ \dot{\Psi}\end{bmatrix}, \quad (8) \]
 

and the steady-state response to an applied force is

 \[ \begin{bmatrix}\dot{x}\\ \dot{y}\\ \dot{\Psi}\end{bmatrix}=\begin{bmatrix}D_{1}^{\prime}&0&0\\ 0&D_{1}^{\prime}&\\ 0&0&9D_{3}^{\prime}\end{bmatrix}^{-1}\begin{bmatrix}f_{x}^{\alpha\mathrm{pp}}\\ f_{y}^{\alpha\mathrm{pp}} \\ f_{\Psi}^{\alpha\mathrm{pp}}\end{bmatrix}. \quad (9) \] 

As a result, a  \( -1/2 \)  defect has the mobility tensor given by the inverse matrix in Eq. (9). Because that tensor is diagonal, a translational force induces only translational motion, and a rotational force induces only rotational motion, at lowest order in the forces.

The matrix equations (6) and (9) can be used directly, with the macroscopic D and  \( D' \)  coefficients considered as purely phenomenological parameters. However, one might want to determine these macroscopic coefficients in terms of the more microscopic  \( \alpha \)  and  \( \gamma \)  coefficients. That is the purpose of our coarse-graining calculation in the following sections.

## 2.2 Minimal model

As a first step, we consider a defect moving at a specified velocity with a fixed orientation. We want to calculate its dissipation from microscopic theory, and compare the result with the calculation from macroscopic theory. Although we use a minimal model, the calculation is still rather lengthy. Readers who are mainly interested in the result rather than the method may wish to skip ahead to Eq. (31).

Our minimal model of a 2D nematic liquid crystal is analogous to the model of a hexatic liquid crystal considered by Kats et al. \( ^{33} \)  We make the approximation of equal Frank constants, so that the Frank free energy becomes

 \[ F=\int d^{2}r\left[\frac{1}{2}K(\partial_{t}n_{j})(\partial_{t}n_{ j})\right]. \quad (10) \] 

Similarly, we consider just two viscosity coefficients, the isotropic fluid flow viscosity  \( \alpha_{4} \)  and the rotational viscosity  \( \gamma_{1} \) , so that the dissipation function becomes

 \[ D=\int d^{2}r\left[\frac{1}{2}\alpha_{4}A_{i j}A_{i j}+\frac{1}{2}\gamma_{1}N_{i}N_{i}\right]. \quad (11) \] 

The minimal model requires both  \( \alpha_{4}>0 \)  and  \( \gamma_{1}>0 \) , so that the system will have drag against shear flow and drag against director rotation. The other viscosity coefficients represent more subtle anisotropies in the viscous drag, and they will be added later as perturbations. Note that the limit of  \( \alpha_{4}\to\infty \)  corresponds to orientational order in a material that cannot flow.

We write the director field as  \( \hat{\mathbf{n}} = (\cos\theta, \sin\theta) \) , so that the Frank free energy simplifies to

 \[ F=\int d^{2}r\left[\frac{1}{2}K|\nabla\theta|^{2}\right]. \quad (12) \] 

Also, we assume that the material is incompressible, which implies that  \( \partial_{i}v_{i}=0 \) . Because of this constraint, the velocity field can be written in terms of a stream function  \( \psi(\mathbf{r},t) \)  as  \( v_{i}=\varepsilon_{ij}\partial_{j}\psi \) , where  \( \varepsilon_{ij} \)  is the 2D Levi-Civita symbol. The stream function  \( \psi \)  is a standard concept in fluid mechanics, and should not be confused with the defect orientation angle  \( \Psi \) . In terms of the stream function, the strain rate tensor becomes

 \[ A_{i j}=\frac{1}{2}(\partial_{i}v_{j}+\partial_{j}v_{i})=\frac{1}{2}(\varepsilon_{j k}\partial_{i}\partial_{k}\psi+\varepsilon_{i k}\partial_{j}\partial_{k}\Psi). \quad (13) \] 

Likewise, the background fluid vorticity becomes  \( \omega = \frac{1}{2} \varepsilon_{ij} \partial_{i} v_{j} = -\frac{1}{2} \nabla^{2} \psi \) , and the director rotation with respect to the background fluid becomes

 \[ \begin{align*}N_{i}=&\dot{n}_{i}-\omega\varepsilon_{ji}n_{j}=\partial_{t}n_{i}+v_{k}\partial_{k}n_{i}-\omega\varepsilon_{ji}n_{j}\\=&\varepsilon_{ji}n_{j}\left[\partial_{t}\theta+\varepsilon_{kl}(\partial_{k}\theta)(\partial_{l}\psi)+\frac{1}{2}\nabla^{2}\psi\right].\end{align*} \quad (14) \] 

Here, the first term  \( n_{i} \)  becomes a convective derivative, which leads to the nonlinear coupling  \( (\partial_{k}\theta)(\partial_{l}\psi) \) . The dissipation function then simplifies to

 \[ \begin{align*}D=\int d^{2}r\left[\frac{1}{2}\alpha_{4}\left[(\partial_{i}\partial_{j}\psi)(\partial_{i}\partial _{j}\psi)-\frac{1}{2}(\nabla^{2}\psi)^{2}\right]\right.\\\left.+\frac{1}{2}\gamma_{1}\left[\partial_{t}\theta+\varepsilon_{kl}(\partial_{k}\theta)(\partial_{l}\psi)+\frac{1}{2}\nabla^{2}\psi\right]^{2}\right].\end{align*} \quad (15) \] 

From the free energy and the dissipation function, we can derive the equations of motion for \(\theta\) and \(\psi\). For the director orientation \(\theta\), the elastic force is \(-\delta F/\delta\theta(\mathbf{r},t)\), and the drag force is \(-\delta D/\delta[\partial_{t}\theta(\mathbf{r},t)]\). Hence, the equation for overdamped motion is that the forces must sum to zero,

 \[ \begin{align*}0=&-\frac{\delta F}{\delta\theta(\mathbf{r},t)}-\frac{\delta D}{\delta[\partial_{t}\theta(\mathbf{r},t)]}\\=&K\nabla^{2}\theta-\gamma_{1}\left[\partial_{t}\theta+\varepsilon_{kl}(\partial_{k}\theta)(\partial_{l}\psi)+\frac{1}{2}\nabla^{2}\psi\right].\end{align*} \quad (16) \] 

For the generalized velocity \(\psi\), the elastic force is zero, and the drag force is \(-\delta D/\delta\psi(\mathbf{r},t)\). Hence, the equation for overdamped motion is that the drag force equals zero,

 \[ 0=-\frac{\delta D}{\delta\psi(\mathbf{r},t)}=-\frac{1}{2}\alpha_{4}\nabla^{4}\psi \quad (17) \] 

 \[ +\gamma_{1}\left[\varepsilon_{i j}(\partial_{t}\theta)\partial_{j}-\frac{1}{2}\nabla^{2}\right]\left[\partial_{t}\theta+\varepsilon_{k l}(\partial_{k}\theta)(\partial_{l}\psi)+\frac{1}{2}\nabla^{2}\psi\right]. \] 

These equations are nonlinear because of the convective derivative. As a check, in the limit of high viscosity  \( \alpha_{4} \rightarrow \infty \) , Eq. (17) implies that  \( \psi \)  is constant, meaning that the material does not flow. Equation (16) then becomes the standard diffusion equation  \( \gamma_{1}\partial_{t}\theta = K\nabla^{2}\theta \) .

We seek a solution of these equations corresponding to steady motion of a defect with a specified velocity u. In this steady state, we have  \( \theta(\mathbf{r},t)=\theta(\mathbf{r}-u\mathbf{t}) \)  and  \( \psi(\mathbf{r},t)=\psi(\mathbf{r}-u\mathbf{t}) \) . Hence, the time derivative becomes  \( \partial_{t}\theta=-u_{k}\partial_{k}\theta \) , and the equations of motion
 

take the time-independent form

 \[ 0=K\nabla^{2}\theta+\gamma_{1}\left[u_{k}\partial_{k}\theta-\varepsilon_{k l}(\partial_{k}\theta)(\partial_{l}\psi)-\frac{1}{2}\nabla^{2}\psi\right], \quad (18) \] 

 \[ \begin{align*}0=&-\frac{1}{2}\alpha_{4}\nabla^{4}\psi\\&-\gamma_{1}\left[\varepsilon_{ij}(\partial_{i}\theta)\partial_{j}-\frac{1}{2}\nabla^{2}\right]\left[u_{k}\partial_{k}\theta-\varepsilon_{kl}(\partial_{k}\theta)(\partial_{l}\psi)-\frac{1}{2}\nabla^{2}\psi\right].\end{align*} \quad (19) \] 

To solve these equations, we choose a coordinate system such that the defect velocity u is in the x-direction, with  \( u = u\hat{x} \) . We then assume that u is small, so that we can use perturbation theory as in Pismen and Rodriguez, \( ^{29} \)  writing

 \[ \begin{aligned}\theta(\mathbf{r})&=\theta_{0}(\mathbf{r})+u\theta_{1}(\mathbf{r})+O(u^{2}),\\\psi(\mathbf{r})&=\psi_{0}(\mathbf{r})+u\psi_{1}(\mathbf{r})+O(u^{2}).\end{aligned} \quad (20) \] 

At zeroth order in u, we assume that  \( \psi_{0}(\mathbf{r}) \)  is constant, meaning that the material does not flow if the defect does not move. With this assumption, the second differential equation is identically satisfied, and the first differential equation becomes Laplace's equation  \( 0 = K\nabla^{2}\theta_{0} \) . The solution of this equation, corresponding to a defect at the origin, can be written as

 \[ \theta_{0}=k\tan^{-1}\left(\frac{y}{x}\right)+\Theta_{0}. \quad (21) \] 

Here, k is the topological charge of the defect, and  \( \Theta_{0} \)  represents an overall rotation of the director about the z-axis. Previous papers \( ^{41,42} \)  have shown that  \( \Theta_{0} \)  is related to the defect orientation  \( \Psi \)  by  \( \Psi = \Theta_{0}/(1 - k) \)  (mod  \( \pi/|1 - k| \) ). In particular, for a defect of charge  \( k = +1/2 \) , we have  \( \Psi = 2\Theta_{0} \) . For a defect of charge  \( k = -1/2 \) , we have  \( \Psi = \frac{2}{3}\Theta_{0} \) .

At first order in u, the differential equations become

 \[ 0=K\nabla^{2}\theta_{1}+\gamma_{1}\left[\partial_{x}\theta_{0}-\varepsilon_{k l}(\partial_{k}\theta_{0})(\partial_{l}\psi_{1})-\frac{1}{2}\nabla^{2}\psi_{1}\right], \quad (22) \] 

 \[ 0=-\frac{1}{2}\alpha_{4}\nabla^{4}\psi_{1} \quad (23) \] 

 \[ -\gamma_{1}\left[\varepsilon_{i j}(\partial_{i}\theta_{0})\partial_{j}-\frac{1}{2}\nabla^{2}\right]\left[\partial_{x}\theta_{0}-\varepsilon_{k l}(\partial_{k}\theta_{0})(\partial_{l}\psi_{1})-\frac{1}{2}\nabla^{2}\psi_{1}\right]. \] 

To simplify these equations, we insert Eq. (21) for \(\theta_{0}\), and change variables to polar coordinates \((r,\phi)\). We then write \(\theta_{1}(r,\phi)=\theta_{r}(r)\sin\phi\) and \(\psi_{1}(r,\phi)=\psi_{r}(r)\sin\phi\). After those transformations, the differential equations take the form

 \[ \begin{aligned}0=&K\left[\theta_{r}^{\prime\prime}(r)+\frac{\theta_{r}^{\prime}(r)}{r}-\frac{\theta_{r}(r)}{r^{2}}\right]\\&+\gamma_{1}\left[-\frac{\psi_{r}^{\prime\prime}(r)}{2}-\frac{(1-2k)\psi_{r}^{\prime}(r)}{2r}+\frac{\psi_{r}(r)}{2r^{2}}-\frac{k}{r}\right],\\0=&\alpha_{4}\left[-\frac{\psi_{r}^{\prime\prime\prime}(r)}{2}-\frac{\psi_{r}^{^{\prime\prime\prime}}(r)}{r}+\frac{3\psi_{r}^{\prime\prime}(r)}{2r^{2}}-\frac{3\psi_{r}^{\prime}(r)}{2r^{3}}+\frac{3\psi_{r}(r)}{2r}\right]\\&+\gamma_{1}\left[-\frac{\psi_{r}^{\prime\prime\prime}(r)}{4}-\frac{\psi_{r}^{^{\prime\prime\prime}}(r)}{2r}+\frac{(3-4k+4k^{2})\psi_{r}^{\prime\prime}(r)}{4r^{2}}\right.\\&\left.\quad-\frac{(3-4k+4k^{2})\psi_{r}^{\prime}(r)}{4r^{3}}+\frac{(3-4k)\psi_{r}(r)}{4r^{4}}+\frac{k^{2}}{r^{3}}\right].\end{aligned} \quad (24) \quad (25) \] 

The solution of Eq. (25) is

 \[ \psi_{r}(r)=r+\sum_{i=1}^{4}C_{i}p_{i}^{n}, \quad (26) \] 

where the exponents \(p_{i}\) are the four roots of the characteristic equation

 \[ 0=\alpha_{4}\left[-\frac{p^{4}}{2}+2p^{3}-p^{2}-2p+\frac{3}{2}\right] \quad (27) \] 

 \[ +\gamma_{1}\left[-\frac{p^{4}}{4}+p^{3}-\left(\frac{1}{2}+k-k^{2}\right)p^{2}-(1-2k+2k^{2})p+\left(\frac{3}{4}-k\right)\right]. \] 

These roots are

 \[ p=1\pm\left[\frac{2}{2+g}\left[2+g(1-k+k^{2})\right.\right. \quad (28) \] 

 \[ \pm\left[4+2g(2-2k+k^{2})+g^{2}(1-k)^{2}(1+k^{2})\right]^{1/2}\Bigg]\Bigg]^{1/2}, \] 

where  \( g = \gamma_{1} / \alpha_{4} \)  is the ratio of viscosities. In general, two of the roots (with + in the first position) are greater than 1, and two of the roots (with - in the first position) are less than 1.

The coefficients  \( C_{i} \)  are fixed by the boundary conditions. At the defect, as  \( r \rightarrow 0 \) , we require that the velocity field v must not diverge, and hence that  \( \psi \)  cannot depend on r with an exponent less than one. This boundary condition implies that two of the coefficients are zero. Far from the defect, at a cutoff length  \( r_{max} \) , we require that  \( \psi_{r}(r_{\mathrm{max}}) = 0 \)  and  \( \psi_{r}^{\prime}(r_{\mathrm{max}}) = 0 \) , so that the velocity field v also goes to zero. Those boundary conditions determine the other two coefficients. Hence, the solution for  \( \psi_{r}(r) \)  becomes

 \[ \psi_{r}(r)=r+\frac{(p_{2}-1)r_{\max}^{1-p_{1}}r^{p_{1}}}{p_{1}-p_{2}}+\frac{(p_{1}-1)r_{\max}^{1-p_{2}}r^{p_{2}}}{p_{2}-p_{1}}, \quad (29) \] 

where  \( p_{1} \)  and  \( p_{2} \)  are the two roots with + in the first position. From that solution, the full stream function becomes  \( \psi = u\psi_{r}(r)\sin\phi \) , and the flow velocity field becomes  \( v_{i} = \varepsilon_{ij}\partial_{j}\psi \) . One interesting consequence of this result is that the velocity field at the defect is  \( \mathbf{v}(\mathbf{r} \to 0) = u\hat{\mathbf{x}} \) , which is equal to the velocity of the defect. regardless of the topological charge k and viscosity ratio g. Hence, the fluid flow velocity matches the defect velocity as
 
![](./images/867754548570095811_2.jpg)

Fig. 2 Visualization of the results of Eqs. (29) and (30) for a defect of topological charge  \( k = \pm 1/2 \)  moving to the right. Blue double-headed arrows show the director field, and black single-headed arrows show the flow velocity field. Parameters are  \( \Theta_{0} = \pi/2 \) , K = 1,  \( \gamma_{1} = \alpha_{4} = 1 \) , u = 1, and  \( r_{max} = 1 \) .

a result of the calculation, not as a boundary condition. If the fluid viscosity  \( \alpha_{4} \)  becomes very high, then the fluid flow velocity decreases very sharply going away from the defect, but it still matches the defect velocity right at the defect core.

To obtain the first-order correction to the director field, we insert the solution for  \( \psi_{r}(r) \)  into Eq. (24) and solve for  \( \theta_{r}(r) \) . For a boundary conditions, we require that  \( \theta_{r}(0) \)  does not diverge, and  \( \theta_{r}^{\prime}(r_{\mathrm{max}}) = 0 \) . The solution is

 \[ \begin{aligned}\theta_{r}(r)=\frac{\gamma_{1}}{2K}\Bigg[&\left(1+\frac{2k(p_{1}+p_{2}-p_{1}p_{2}-p_{ 1}^{2}p_{2}^{2})}{(p_{1}^{2}-1)(p_{2}^{2}-1)}\right)r\\&+\frac{(p_{1}^{2}-2kp_{1}-1)(p_{2}-1)r_{\max}^{1-p_{1}}r^{p_{1}}}{(p_{1}^{2}-1)(p_{1}-p_{2})}\\&+\frac{(p_{2}^{2}-2kp_{2}-1)(p_{1}-1)r_{\max}^{1-p_{2}}r^{p_{2}}}{(p_{2}^{2}-1)(p_{2}-p_{1})}\Bigg].\end{aligned} \quad (30) \] 

The full perturbation series for the director field then becomes \(\theta = k\phi + \Theta_{0} + u\Theta_{r}(r)\sin\phi\).

Figure 2 presents examples of the director field and flow velocity field that come from these calculations, for defects of topological charge  \( k = \pm 1/2 \)  moving to the right. The director field is slightly distorted compared with the standard arctangent form for the static director field around a topological defect (in a liquid crystal with equal Frank constants). Because of the factor of  \( \sin \phi \) , the distortion goes to zero in front of and behind the moving defect, and it is greatest in the direction perpendicular to the defect velocity. This distortion is similar to a recent result for a moving defect in a material that cannot flow. \( ^{32} \)  The flow velocity field is greatest at the defect core, and decreases moving away from the defect. It has a vortex on each side of the moving defect.

We now insert the perturbation series results for  \( \theta \)  and  \( \psi \)  back into Eq. (15), to calculate the dissipation function D as a perturbation series in defect velocity u. We integrate from the minimum radius  \( r_{core} \)  out to the maximum radius  \( r_{max} \) . The exact integral is quite complicated, and we cannot reproduce it here. However, it takes a simple and interesting form in the limit of  \( g = \gamma_{1}/\alpha_{4} \ll 1 \) , i.e. in the limit of high flow viscosity  \( \alpha_{4} \) , so that the material can only flow very slowly. When we expand in powers of g, the integrated dissipation becomes

 \[ \begin{aligned}D=&\frac{\pi\gamma_{1}k^{2}u^{2}}{2}\log\frac{r_{\max}}{r_{core}}-\frac{\pi\gamma_{1}^{3/2}k^{2}u^{2}}{2^{3/2}\alpha_{4}^{1/2}}\left[|k|\left(\log\frac{r_{\max}}{r_{core}}\right)^{2}\right.\\&\left.+(2-3k)\mathrm{sign}(k)\left(\log\frac{r_{\max}}{r_{core}}\right)-\left(2-\frac{3k}{2}\right)\mathrm{sign}(k)\right].\end{aligned} \quad (31) \] 

In this expression, the first term is a classic result for the dissipation of a moving defect in a material that cannot flow. \( ^{28} \)  The second term is a correction to the dissipation in a material that can flow slowly.

Two features of this expression are particularly important. First, the correction is negative: As the viscosity  \( \alpha_{4} \)  decreases from infinity to finite values, the drag on a moving defect also decreases. That result is reasonable, because backflow can partially compensate for the motion of the defect and reduce dissipation. Second, the classic term is even in topological charge k, but the correction term is not. In a material that cannot flow, with  \( \alpha_{4} \rightarrow \infty \) , there is a symmetry between positive and negative topological charges, which generate equal amounts of dissipation. In a material that can flow slowly, this symmetry is broken. The flow pattern reduces the dissipation of positive topological charges more than it reduces the dissipation of negative topological charges. As a result, negative defects generate more dissipation than positive defects, and hence negative defects will move more slowly than positive defects under the same force. This flow-induced asymmetry between positive and negative defects has been seen through experiments, \( ^{5,6,8} \)  simulations, \( ^{20,21} \)  and other theoretical techniques. \( ^{33-35} \)  Here, we see the asymmetry emerge as a specific term of the series expansion in the viscosity ratio g.

In Eq. (31), the dissipation depends logarithmically on  \( r_{max} \) . The length scale  \( r_{max}^{} \)  enters the calculation as a hard cutoff on the dissipation integral, just as it also enters the calculation for the energy of a topological defect. In a typical experiment with multiple defects, the effective length scale  \( r_{max} \)  is given by the characteristic distance between defects.

Some theoretical studies \( ^{29-32} \)  have criticized the dependence on  \( r_{max} \) . Their argument is essentially as follows: If a defect moves with finite velocity u, then the ratio  \( K/(\gamma_{1}u) \)  provides a new length scale for the problem, and the dissipation drops off for distances beyond that length scale. As a result, the dissipation integral really extends out to  \( r_{max} \)  or  \( K/(\gamma_{1}u) \) , whichever is smaller. Hence, the result for the dissipation should involve  \( \log(r_{\text{max}}/r_{\text{core}}) \)  or  \( \log[K/(\gamma_{1}ur_{\text{core}})] \) , whichever is smaller. If the system is truly infinite, with  \( r_{\text{max}} \to \infty \) , then  \( K/(\gamma_{1}u) < r_{\text{max}} \)  for any nonzero velocity u. Hence, these studies argue that the dissipation is really proportional to  \( \log[K/(\gamma_{1}ur_{\text{core}})] \) . Sometimes this dependence is written in terms of the Ericksen number as  \( \log(3.6/Er) \) . This dissipation can be considered as “anomalous” because the dependence on u is not proportional to  \( u^{2} \)  for small u.

Our response to that argument is that it only applies to a system that is strictly infinite. For any finite system size, there is
 

a crossover velocity  \( u_{c} = K / (\gamma_{1} r_{\text{max}}) \)  at which the cutoff length scale changes. For  \( u < u_{c} \) , the dissipation is proportional to  \( \log(r_{\text{max}} / r_{\text{core}}) \) ; for  \( u > u_{c} \) , it is proportional to  \( \log[K / (\gamma_{1} u r_{\text{core}})] \) . In general, we want to calculate the dissipation for small u in a finite system, and it scales in the standard way proportional to  \( u^{2} \) , with a coefficient proportional to  \( \log(r_{\text{max}} / r_{\text{core}}) \) . Indeed, this regime is reasonable based on experimental parameters. In an experiment on defect annihilation, \( ^{8} \)  the characteristic defect velocity is  \( u \sim 0.3 \mu m/s \) , and the characteristic distance between defects is  \( r_{max} \sim 100 \mu m \) . If we assume the Frank constant  \( K \sim 10^{-11} N \)  and rotational viscosity  \( \gamma_{1} \sim 10^{-1} Pa s \) , then the crossover velocity is  \( u_{c} \sim 1 \mu m/s \) , and we are roughly in the regime of  \( u < u_{c} \) .

Now we can do the key coarse-graining step: We compare the dissipation of Eq. (31) with the dissipation that would be expected through the macroscopic theory presented in Sec. 2.1. In this way, we can determine the coefficients of the macroscopic theory.

For a defect of topological charge  \( k = +1/2 \) , moving at velocity  \( u = u\dot{x} \)  with fixed orientation  \( \mathbf{p} = (\cos\Psi, \sin\Psi) \) , the macroscopic theory of Eq. (2) implies that the dissipation function is

 \[ D=\frac{1}{2}D_{1}|\dot{\mathbf{R}}|^{2}+\frac{1}{2}D_{2}(\mathbf{p}\cdot\dot{\mathbf{R}})^{2}=\frac{1}{2}D_{1}u^{2}+\frac{1}{2}{D_{2}}u^{2}\cos^{2}\Psi. \quad (32) \] 

By comparing Eq. (32) with Eq. (31) for  \( k = +1/2 \) , we see that the coefficient  \( D_{1} \)  is

 \[ D_{1}=\frac{\pi\gamma_{1}}{4}\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}-\frac{\pi\gamma_{1}^{3/2}}{2^{7/2}\alpha_{4}^{1/2}}\left[\left(\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}\right)^{2}+\left(\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}\right)-\frac{5}{2}\right]. \quad (33) \] 

Furthermore, we see that Eq. (31) does not depend on the defect orientation  \( \Psi \)  at all, and hence  \( D_{2}=0 \) . This lack of dependence on the defect orientation arises because of our minimal model with only the two viscosity coefficients  \( \alpha_{4} \)  and  \( \gamma_{1} \) . In the next section, we will discuss corrections arising from other viscosity coefficients.

For a defect of topological charge  \( k = -1/2 \) , again moving at velocity  \( u = u\dot{x} \)  with fixed orientation  \( T_{ijk} \) , the the macroscopic theory of Eq. (7) implies the dissipation function

 \[ D=\frac{1}{2}D_{1}^{\prime}|\dot{\mathbf{R}}|^{2}=\frac{1}{2}D_{1}u^{2}. \quad (34) \] 

Comparing Eq. (34) with Eq. (31) for \(k = -1/2\), we find that \(D_{1}^{\prime}\) is

 \[ D_{1}^{\prime}=\frac{\pi\gamma_{1}}{4}\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}-\frac{\pi\gamma_{1}^{3/2}}{2^{7/2}\alpha_{4}^{1/2}}\left[\left(\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}\right)^{2}-7\left(\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}\right)+\frac{11}{2}\right]. \quad (35) \] 

Here, we see explicitly  \( D_{1}^{\prime} \)  and  \( D_{1} \)  have the same value in the limit of no flow  \( \alpha_{4} \rightarrow \infty \) , but backflow effects reduce  \( D_{1}^{\prime} \)  less than they reduce  \( D_{11} \) . Thus, we obtain  \( D_{1}^{\prime} > D_{1} \)  in a system with backflow; i.e. a negative defect experiences more dissipation and hence more drag.

In addition to the drag coefficients for motion with fixed orientation, the macroscopic theory also includes drag coefficients for defect rotation ( \( D_{3} \)  for  \( +1/2 \)  defect,  \( D_{3}^{\prime} \)  for  \( -1/2 \)  defect) and for simultaneous motion and rotation ( \( D_{4} \)  for  \( +1/2 \)  defect). Ideally, we would like to calculate those drag coefficients from the same minimal model of liquid-crystal hydrodynamics. We do not yet have a method for this calculation, because defect rotation is a very long-range distortion that does not decrease with distance from the defect, and hence the dissipation depends sensitively on the boundary conditions. However, we can at least estimate these coefficients from dimensional analysis. Because  \( \dot{p} \)  has one fewer power of length than  \( \dot{R} \)  in Eq. (2), and  \( \dot{T}_{ijk} \)  has one fewer power of length than  \( \dot{R} \)  in Eq. (7), we obtain

 \[ D_{3}\sim D_{3}^{\prime}\sim\gamma_{1}r_{\max}^{2}, \quad (36) \] 

 \[ D_{4}\sim\gamma_{1}r_{\max}. \quad (37) \] 

Hence, these coefficients diverge with system size  \( r_{max} \)  much more severely than do  \( D_{1} \)  and  \( D_{1}^{\prime} \) . This divergence will be discussed in Sec. 4.

## 2.3 Other viscosity coefficients

The previous section presented a minimal model with only two viscosity coefficients. However, other viscosity coefficients are also allowed by symmetry in liquid-crystal hydrodynamics. As noted above, the  \( (\alpha_{5}+\alpha_{6}) \)  term is equivalent to the  \( \alpha_{4} \)  term in 2D (unlike 3D), so we do not need to consider that term separately. We would like to see how the  \( \gamma_{2} \)  and  \( \alpha_{1} \)  coefficients change the macroscopic theory.

To estimate the effects of those coefficients, we regard the extra terms in the full dissipation function, proportional to  \( \gamma_{2} \)  and  \( \alpha_{1} \) , as corrections to the minimal model. We suppose that  \( \gamma_{2} \)  and  \( \alpha_{4} \)  are much smaller than  \( \gamma_{1} \)  and  \( \alpha_{4} \) , and calculate these two terms using the director field  \( \theta(\mathbf{r}) = k\phi + \Theta_{0} + u\dot{\theta}_{r}(r) \sin \phi \)  and the flow velocity field  \( v_{i} = \varepsilon_{ij}\partial_{j}\psi \) , with  \( \psi(\mathbf{r}) = u\psi_{r}(r) \sin \phi \) , which were found from the minimal model in Sec. 2.2. We do not go back and recalculate the director and flow velocity fields with the other viscosity coefficients. This procedure is analogous to perturbation theory in quantum mechanics: At lowest order in perturbation theory, one calculates the expectation value of the perturbed Hamiltonian using the unperturbed wavefunction. The perturbed wavefunction only enters at higher order.

The term proportional to  \( \gamma_{2} \)  makes a contribution of

 \[ \int d^{2}r\left[\gamma_{2}N_{i}A_{i j}n_{j}\right]=0, \quad (38) \] 

except for the special cases of  \( k = +1 \)  or +2, which we do not discuss here. Hence,  \( \gamma_{2} \)  does not affect the drag coefficients, at this order of perturbation theory. (It may have effects at higher order in perturbation theory.)

By comparison, the term proportional to  \( \alpha_{1} \)  makes a contribution of

 \[ \int d^{2}r\left[\frac{1}{2}\alpha_{1}(n_{i}A_{i j}n_{j})^{2}\right]=\frac{\pi\gamma_{1}\alpha_{1}k^{2}u^{2}}{8\alpha_{4}}\left[\left(\log\frac{r_{\max}}{r_{\mathrm{c o r e}}}\right)-\frac{1}{2}\right], \quad (39) \] 

except in the special cases of  \( k = +1/2 \) , +1, or +3/2. In particular,
 

for  \( k = +1/2 \) , we obtain

 \[ \begin{aligned}\int d^{2}r\left[\frac{1}{2}\alpha_{1}(n_{i}A_{ij}n_{j})^{2}\right]=&\frac{\pi\gamma_{1}\alpha_{1}u^{2}}{32\alpha_{4}}\left[\left(\log\frac{r_{\max}}{r_{\mathrm{core}}}\right)-\frac{1}{2}\right]\\&+\frac{\pi\gamma_{1}\alpha_{1}u^{2}}{64\alpha_{4}}\left[\left(\log\frac{r_{\max}}{r_{\mathrm{core}}}\right)-1\right]\cos4\Theta_{0}.\end{aligned} \quad (40) \] 

The last term is particularly interesting, because it is proportional to  \( \cos4\Theta_{0} \) . As discussed earlier, previous papers \( ^{41,42} \)  have shown that  \( \Theta_{0} \)  is related to the defect orientation  \( \Psi \)  by  \( \Psi = 2\Theta_{0} \) , in the case of +1/2 defect. Hence, the last term in the dissipation depends on defect orientation as  \( \cos2\Psi \) , or equivalently as  \( \cos^{2}\Psi \) . This is exactly the orientational dependence that would be expected from the macroscopic drag coefficient  \( D_{2} \) . Hence, this orientation-dependent drag coefficient really is present, with a magnitude that scales with the viscosity  \( \alpha_{1} \) .

## 2.4 Example: Motion of a  \( \pm1/2 \)  defect in a channel

As a simple example to illustrate the microscopic and macroscopic theories, we consider the motion of a defect in a channel. Although this example is an idealized construction, it is related to lower textures, which have been studied experimentally and theoretically. \( ^{52,53} \) 

In this example, we consider a 2D nematic liquid crystal in a channel, which is infinite in the x-direction but finite in the y-direction. On the top and bottom surfaces of the channel, at  \( y = \pm d/2 \) , there is strong planar anchoring, so that the director field is constrained to be horizontal. Between those surfaces, the director field may be uniform in the horizontal direction, or it may rotate through an angle of  \( \pi \) . Indeed, there may be domains of x where the director is uniform or distorted through  \( \pi \) . In that case, the interface between a uniform domain and a distorted domain is a defect of topological charge  \( k = \pm 1/2 \) , as shown in Fig. 3(a).

If the defect does not move, then the director field must satisfy the equation for static equilibrium  \( 0 = K\nabla^{2}\theta \) . An explicit solution that obeys the boundary conditions is

 \[ \theta(x,y)=\pm\left[\frac{1}{2}\tan^{-1}\left(\frac{\tan(\pi y/d)}{\tanh(\pi x/d)}\right)+\frac{\pi y}{2d}+\frac{\pi}{2}\right], \quad (41) \] 

for  \( k = \pm 1/2 \) . In general, however, the defect will move in order to reduce the Frank elastic free energy. In the uniform domain to the left of the defect, the elastic free energy density is 0, but in the distorted domain to the right, it is  \( \frac{1}{2}K(\pi/d)^{2} \) . Hence, the defect will move to the right so that the uniform domain will grow, the distorted domain will shrink, and the elastic free energy will decrease. We can then ask: What is the velocity of the defect?

In the macroscopic theory, this problem is quite straightforward, and is analogous to the terminal velocity of a particle falling under gravity. In steady state, the total force acting on the defect must be zero, so that

 \[ 0=\mathbf{f}_{\mathrm{e l a s t i c}}+\mathbf{f}_{\mathrm{d r a g}}=-\frac{\partial F}{\partial\mathbf{R}}-\frac{\partial D}{\partial\mathbf{u}}. \quad (42) \] 

The elastic force is

 \[ \mathbf{f}_{\mathrm{e l a s t i c}}=-\frac{\partial F}{\partial\mathbf{R}}=\frac{\pi^{2}K}{2d}\hat{\mathbf{x}}, \quad (43) \] 

because the elastic free energy decreases by  \( \frac{1}{2}K(\pi/d)^{2}d\delta x \)  whenever the defect moves to the right by  \( \delta x \) . For the +1/2 defect, the orientation vector is  \( p = -\hat{x} \) , and hence Eq. (2) gives the drag force

 \[ \mathbf{f}_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\mathbf{u}}=-(D_{1}+D_{2})u\hat{\mathbf{x}}. \quad (44) \] 

Hence, the balance of forces requires that

 \[ u_{+1/2}=\frac{\pi^{2}K}{2d(D_{1}+D_{2})}. \quad (45) \] 

In the minimal model we have \(D_{2}=0\), and we can estimate \(D_{1}\) by Eq. (33), with \(d/2\) playing the role of \(r_{\max}\). Hence, the prediction for velocity becomes

 \[ u_{+1/2}=\frac{2\pi K}{\gamma_{1}d\log\frac{d}{2r_{\mathrm{c o r e}}}}\times \quad (46) \] 

 \[ \times\left[1+\frac{\gamma_{1}^{1/2}}{2^{3/2}\alpha_{4}^{1/2}}\frac{\left(\log\frac{d}{2r_{\mathrm{c o r e}}}\right)^{2}+\left(\log\frac{d}{2r_{\mathrm{c o r e}}}\right)-\frac{5}{2}}{\log\frac{d}{2r_{\mathrm{c o r e}}}}+\cdots\right] \] 

Similarly, for the -1/2 defect, Eq. (7) gives the drag force

 \[ \mathbf{f}_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\mathbf{u}}=-D_{1}^{\prime}u\hat{\mathbf{x}}, \quad (47) \] 

and hence the balance of forces requires that

 \[ u_{-1/2}=\frac{\pi^{2}K}{2dD_{1}^{\prime}}. \quad (48) \] 

In the minimal model, we can estimate  \( D_{1}^{\prime} \)  by Eq. (35), with d/2 in place of  \( r_{max} \) , and hence the prediction for velocity becomes

 \[ u_{-1/2}=\frac{2\pi K}{\gamma_{1}d\log\frac{d}{2r_{\mathrm{c o r e}}}}\times \quad (49) \] 

 \[ \times\left[1+\frac{\gamma_{1}^{1/2}}{2^{3/2}\alpha_{4}^{1/2}}\frac{\left(\log\frac{d}{2r_{\mathrm{c o r e}}}\right)^{2}-7\left(\log\frac{d}{2r_{\mathrm{c o r e}}}\right)+\frac{11}{2}}{\log\frac{d}{2r_{\mathrm{c o r e}}}}\right]. \] 

For a material that cannot flow, with  \( \alpha_{4}\rightarrow\infty \) , the predictions for  \( u_{+1/2} \)  and  \( u_{-1/2} \) are equal. As the flow viscosity  \( \alpha_{4} \)  decreases, both of these velocities increase, but  \( u_{+1/2} \)  increases more than  \( u_{-1/2} \) . Hence, +1/2 defects should move more quickly than -1/2 defects because of backflow effects.

To test this macroscopic argument, we perform hydrodynamic simulations of defect motion in a channel. For these simulations, we must use a formalism based on the 2D nematic order tensor  \( Q_{ij} = S(2n_{i}n_{j} - \delta_{ij}) \) , so that the scalar order parameter S can go to zero in the defect core. The minimal model for the free energy is

 \[ F=-\frac{1}{4}a Q_{i j}Q_{i j}+\frac{1}{16}b(Q_{i j}Q_{i j})^{2}+\frac{1}{16}L(\partial_{k}Q_{i j})(\partial_{k}Q_{\mathrm{i j}}), \quad (50) \] 

which favors \(S = (a/b)^{1/2}\) away from defects. To represent the
 

(a) Director n(r,t)

![](./images/867754548570095811_3.jpg)

(b) Velocity v(r,t)

![](./images/867754548570095811_4.jpg)

Fig. 3 Numerical solution of hydrodynamic equations for motion of a +1/2 defect toward the right, in a channel with planar boundary conditions. (a) Director field shown by black lines, with scalar order parameter indicated by colored contours. (b) Velocity field shown by black arrows, with  \( |v|^{2} \)  indicated by colored contours. In both cases, the red arrow represents the defect orientation vector p. Parameters are  \( a = b = 200 \) , L = 4,  \( \alpha_{4} = 5 \) ,  \( \Gamma_{1} = 8 \) ,  \( \rho = 1 \) , and d = 2. The relatively large values of a and b are chosen to give a relatively small defect core radius  \( r_{\mathrm{core}} = (L/a)^{1/2} = 0.2 \)  along with a bulk order parameter  \( S = (a/b)^{1/2} = 1 \) .

rotation of nematic order with respect to the background fluid, instead of the vector N, we use the tensor

 \[ B_{i j}=\dot{Q}_{i j}-\omega(\varepsilon_{i j}Q_{i l}+\varepsilon_{l i}Q_{l j}), \quad (51) \] 

where again \(\omega=\frac{1}{2}\varepsilon_{ij}\partial_{i}v_{j}\) and \(\varepsilon_{ij}\) is the 2D Levi-Civita symbol. The minimal model for the dissipation function then becomes

 \[ D=\int d^{2}r\left[\frac{1}{2}\alpha_{4}A_{i j}A_{i j}+\frac{1}{16}\Gamma_{1}B_{i j}B_{i j}\right]. \quad (52) \] 

The coefficients L and  \( \Gamma_{1} \)  in this tensor representation are related to the coefficients K and  \( \gamma_{1} \)  in the director representation by  \( K = LS^{2} \)  and  \( \gamma_{1} = \Gamma_{1}S^{2} \) .

We derive partial differential equations for the nematic order tensor  \( Q_{ij}(\mathbf{r},t) \)  and the flow velocity field  \( v_{i}(\mathbf{r},t) \)  from

 \[ 0=-\frac{\delta F}{\delta Q_{i j}(\mathbf{r},t)}-\frac{\delta D}{\delta[\partial_{i}Q_{i j}(\mathbf{r},t)]}, \quad (53) \] 

 \[ \rho\frac{\partial v_{i}}{\partial t}=-\frac{\delta D}{\delta v_{i}(\mathbf{r},t)}. \quad (54) \] 

For computational convenience, we work with constant pressure rather than constant density in this calculation, so that there is no pressure term in the equations, and we use a mass density  \( \rho \) . We integrate the equations numerically, with planar boundary conditions at  \( y = \pm d/2 \)  and open boundary conditions in x. For the initial condition, we use Eq. (41) for the director orientation around a defect of topological charge  \( \pm 1/2 \) . We also assume the initial scalar order parameter drops around the defect core as  \( S = (a/b)^{1/2}r/(r^{2} + r_{\mathrm{core}}^{2})^{1/2} \) , with a core radius  \( r_{\mathrm{core}} = (L/a)^{1/2} \) , and

![](./images/867754548570095811_5.jpg)

Fig. 4 Numerical results for the velocities of defects with topological charge  \( k = \pm 1/2 \)  in the channel geometry, as functions of the flow viscosity  \( \alpha_{4} \) . Solid lines show quadratic fits. Parameters are  \( a = b = 200 \) ,  \( L = 4 \) ,  \( \Gamma_{1} = 8 \) ,  \( \rho = 1 \) , and  \( d = 2 \) , and hence  \( r_{\mathrm{core}} = (L/a)^{1/2} = 0.2 \)  and bulk  \( S = (a/b)^{1/2} = 1 \) . Analogous parameters in the director representation are  \( K = LS^{2} \)  and  \( \gamma_{1} = \Gamma_{1}S^{2} \) .

the initial flow velocity is zero.

In the numerical solution, the system quickly reaches a steady state, in which the defect moves to the right with constant velocity, and the fluid flow pattern moves along with the defect. Figure 3 shows an example of the liquid crystal order and fluid flow pattern for a defect of topological charge +1/2. From these numerical results, we can find the defect velocity u for each topological charge as a function of the coefficients a, b, L,  \( \alpha_{4} \) , and  \( \Gamma_{1} \) , as well as the channel width d.

In Fig. 4, we plot the numerical results for the velocities of  \( \pm1/2 \)  defects as functions of fluid flow viscosity, transformed into  \( \alpha_{4}^{-1/2} \) . The results are well fit by the quadratic functions

 \[ \begin{aligned}&u_{+1/2}=0.81+0.69\alpha_{4}^{-1/2}+6.3\alpha_{4}^{-1},\\ &\\&u_{-1/2}=0.84+0.28\alpha_{4}^{-1/2}+1.4\alpha_{4}^{-1}.\\ \end{aligned} \quad (55) \] 

We can see that these results are generally consistent with the predictions of the macroscopic theory. In the limit of high viscosity \(\alpha_{4} \to \infty\), the \(\pm 1/2\) defects move at approximately the same velocity. From Eqs. (46) and (49), we expect that limiting velocity to be \(u = 2\pi K / [\gamma_{l} d \log d / (2 r_{\mathrm{core}})] = 0.98\) (with parameters given in the figure caption), which is close to the numerical value. The numerical velocities may be slightly lower because the hydrodynamic calculation includes extra drag for the motion of the defect core, which is a noticeable fraction of the total area. As the viscosity \(\alpha_{4}\) decreases, so that the material is able to flow, the velocities for \(\pm 1/2\) defects both increase, but the velocity for \(+1/2\) increases more than the velocity for \(-1/2\). This trend is also consistent with the expectation from Eqs. (46) and (49), although a quantitative comparison is difficult because those equations are derived assuming \(r_{\mathrm{max}} = \frac{1}{2} d \gg r_{\mathrm{core}}\), and the hydrodynamic calculation has only a factor of 5 between those values.

Based on this example, we suggest that the macroscopic theory provides a way to develop intuition for the forces that control
 

defect motion in passive liquid crystals. Furthermore, it gives predictions with far less computational effort than the hydrodynamic approach. Hence, we would like to extend it to describe active liquid crystals, in which defect motion is even more important.

## 3 Active liquid crystals

## 3.1 Coarse-graining the hydrodynamic theory

In recent years, there has been extensive theoretical and experimental research on active nematic liquid crystals. These active materials are not in thermal equilibrium, and hence their dynamic behavior is not just driven by minimizing a free energy. Rather, they continually consume energy, often from a food source or from ATP, and convert this energy into motion.

In the theory of active nematic liquid crystals, the effect of activity is usually modeled by an active contribution to the stress tensor, \( ^{22-24,36-40,43} \)  which can be written in terms of the nematic order tensor as

 \[ \sigma_{i j}^{\mathrm{a c t i v e}}=-Z Q_{i j}, \quad (56) \] 

or in terms of the director as

 \[ \sigma_{i j}^{\mathrm{a c t i v e}}=-\zeta\left(2n_{i}n_{j}-\delta_{i j}\right). \quad (57) \] 

Here, the parameter  \( \zeta = ZS \)  is an activity coefficient, with  \( \zeta > 0 \)  representing a material that tends to extend along the director, and  \( \zeta < 0 \)  indicating a material that tends to contract along the director. This term in the stress tensor contributes to the equation of motion as

 \[ \begin{aligned}\rho\frac{\partial v_{j}}{\partial t}&=(passive terms)+\partial_{i}\sigma_{ij}^{active}\\&=(passive terms)-2\zeta\partial_{i}\left(n_{i}n_{j}\right).\end{aligned} \quad (58) \] 

We suggest that the same effect of activity can also be modeled by an active contribution to the dissipation function, which can be written in terms of the nematic order tensor as

 \[ D^{\mathrm{a c t i v e}}=\int d^{2}r\left[-Z Q_{i j}A_{i j}\right], \quad (59) \] 

or in terms of the director as

 \[ D^{\mathrm{a c t i v e}}=\int d^{2}r\left[-2\zeta n_{i}n_{j}A_{i j}\right], \quad (60) \] 

with the strain rate tensor  \( A_{ij} = \frac{1}{2} (\partial_i v_j + \partial_j v_i) \)  as before. This term in the dissipation function contributes to the equation of motion as

 \[ \begin{aligned}\rho\frac{\partial v_{j}}{\partial t}&=(passive terms)-\frac{\delta D^{active}}{\delta v_{j}}\\&=(passive terms)-2\zeta\partial_{i}\left(n_{i}n_{j}\right),\end{aligned} \quad (61) \] 

which is identical to Eq. (58). Hence, the active term in the dissipation function can be used as a starting point for the theory, equivalent to the active term in the stress tensor.

We recognize that  \( D^{active} \)  cannot exactly be regarded as “energy dissipation,” because it is not positive-definite. An alternative description for it might be “rate of energy input” \( ^{54} \)  (with a negative sign). Nevertheless, it enters into the dissipation function in a formal way, to give the correct equation of motion, so we will use it regardless of the terminology.

We would now like to set up a macroscopic theory for the motion of defects in active nematic liquid crystals. As in Sec. 2.1, we need to construct the dissipation function in terms of the macroscopic variables that describe a defect. For a defect of topological charge  \( k = +1/2 \) , these variables are the defect position R and orientation vector p. At quadratic order in  \( \dot{R} \)  and  \( \dot{p} \) , the dissipation function has the passive terms in Eq. (2). In an active liquid crystal, the dissipation function may include one additional active term that is permitted by symmetry,

 \[ D^{\mathrm{a c t i v e}}=D_{5}\mathbf{p}\cdot\dot{\mathbf{R}}. \quad (62) \] 

This term is not allowed in the dissipation function for a passive liquid crystal because it is odd under time reversal, and hence not positive-definite. However, it can exist for an active liquid crystal, with the same understanding that is represents rate of energy input (with a negative sign), rather than actual dissipation.

For a defect of topological charge \(k = -1/2\), the macroscopic variables are the defect position \(\mathbf{R}\) and orientation tensor \(T_{ijk}\). In this case, there is no way to contract the indices to form a nonzero scalar \(D^{\mathrm{active}}\) at linear or quadratic order in velocity \(\dot{\mathbf{R}}\) (recalling that \(T_{ijk}\) is a completely symmetric tensor with \(T_{ijj} = 0\)). There could be a cubic term \(T_{ijk}\dot{R}_i\dot{R}_j\dot{R}_k\), but it does not affect the motion at low speeds. Hence, the dynamic behavior of \(-1/2\) defects should be governed by the passive dissipation function of Eq. (7).

In the coarse-graining calculation, we would like to determine how the macroscopic coefficient  \( D_{5} \)  is related to the more microscopic activity coefficient  \( \zeta \) . We follow the same procedure as in Sec. 2: We assume that a defect of topological charge  \( k = +1/2 \)  moves with fixed velocity  \( \mathbf{u} = (u, 0) \)  at fixed orientation  \( \mathbf{p} = (\cos \Psi, \sin \Psi) \) . We calculate the dissipation using both microscopic and macroscopic approaches, and compare the results.

For the microscopic calculation, we treat the activity coefficient  \( \zeta \)  in the same way that we treated the viscosity coefficients  \( (\alpha_{5} + \alpha_{6}) \) ,  \( \gamma_{2} \) , and  \( \alpha_{1} \)  in Sec. 2.3: We regard the active term of Eq. (60) as a perturbation to the minimal model for passive liquid crystals from Sec. 2.2. Hence, we calculate this term using the director field  \( \theta(\mathbf{r}) = k\phi + \Theta_{0} + u\theta_{r}(r)\sin\phi \)  and the flow velocity field  \( v_{i} = \varepsilon_{ij}\partial_{j}\psi \) , with  \( \psi(\mathbf{r}) = u\psi_{r}(r)\sin\phi \) . This calculation gives  \( D^{active} = 0 \)  except in the special cases of  \( k = +1/2 \)  or  \( +3/2 \) . In particular, for  \( k = +1/2 \) , we obtain

 \[ D^{\mathrm{a c t i v e}}=\frac{\pi\zeta\gamma_{1}^{1/2}u r_{\max}\cos2\Theta_{0}}{3(2\alpha_{4})^{1/2}}. \quad (63) \] 

By comparison, in the macroscopic theory, Eq. (62) implies that  \( D^{active} = D_{5}u \cos \Psi \) . Setting these expressions equal, and recalling that  \( \Psi = 2\Theta_{0} \) , we obtain

 \[ D_{5}=\frac{\pi\zeta\gamma_{1}^{1/2}r_{\max}}{3(2\alpha_{4})^{1/2}}. \quad (64) \] 

Several features of this result should be pointed out. First, it is clearly proportional to the activity coefficient  \( \zeta \) . It is also pro-
 

portional to the ratio  \( (\gamma_{1}/\alpha_{4})^{1/2} \) , so that it vanishes in the limit of high fluid flow viscosity  \( \alpha_{4} \rightarrow \infty \) . That limit is reasonable because the effects of activity require fluid flow. The result scales linearly with the cutoff length scale  \( r_{max} \) , which is a more severe divergence than the logarithmic scaling seen in other terms.

## 3.2 Example: Free motion of a +1/2 defect

As a example, we consider the free motion of a +1/2 defect in an active nematic liquid crystal. In the macroscopic theory, the defect position R and orientation  \( \mathbf{p} = (\cos \Psi, \sin \Psi) \)  evolve in response to the total forces acting on these macroscopic variables. If the defect is free, the Frank free energy is constant, and hence there is no elastic force. Hence, the only forces are the drag forces derived from the dissipation function. Combining passive and active terms, the full macroscopic dissipation function is

 \[ D=\frac{1}{2}D_{1}|\dot{\mathbf{R}}|^{2}+\frac{1}{2}D_{2}(\mathbf{p}\cdot\dot{\mathbf{R}})^{2}+\frac{1}{2}D_{3}|\dot{\mathbf{p}}|^{2}+D_{4}\dot{\mathbf{p}}\cdot\dot{\mathbf{R}}+D_{5}\mathbf{p}\cdot\dot{\mathbf{\mathbf{R}}}. \quad (65) \] 

Hence, the drag force acting on the position is

 \[ \mathbf{f}_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\mathbf{R}}=-D_{1}\dot{\mathbf{R}}-D_{2}\mathbf{p}(\mathbf{p}\cdot\dot{\mathbf{R}})-D_{4}\dot{\mathbf{p}}-D_{5}\mathbf{p}, \quad (66) \] 

and the drag force acting on the orientation is

 \[ f_{\mathrm{d r a g}}=-\frac{\partial D}{\partial\dot{\Psi}}=-D_{3}\dot{\Psi}-D_{4}\mathbf{p}\times\dot{\mathbf{R}}. \quad (67) \] 

In the steady state, the total force acting on position is zero, and the total force acting on orientation is also zero. This steady state occurs when

 \[ \begin{aligned}\dot{\Psi}&=0\quad\rightarrow\quad\dot{\mathbf{p}}=0,\\\dot{\mathbf{R}}&=-\frac{D_{5}}{D_{1}+D_{2}}\mathbf{p}.\end{aligned} \quad (68) \] 

In the minimal model, with  \( \alpha_{4} \gg \gamma_{1} \) , this ratio of dissipation coefficients reduces to

 \[ \dot{\mathbf{R}}=-\frac{4\zeta}{3(2\gamma_{1}\alpha_{4})^{1/2}}\frac{r_{\max}}{\log(r_{\max}/r_{\mathrm{core}})}\mathbf{p}. \quad (69) \] 

Hence, in the steady state, the defect moves at a constant velocity with a constant orientation. The direction of motion is given by the defect orientation +p if the material is contractile ( \( \zeta < 0 \) ), or -p if the material is extensile ( \( \zeta > 0 \) ). The speed is given by the balance between the active force that favors motion and the passive drag force that resists motion. As a result, the speed is linearly proportional to the activity coefficient  \( \zeta \)  and inversely proportional to the combination of viscosities ( \( \gamma_{1}\alpha_{4} \) ) \( ^{1/2} \) . Also, it is linearly proportional to the cutoff length scale  \( r_{max} \) , with a logarithmic correction. This length scale is generally the system size or the characteristic distance between defects, whichever is smaller. The linear dependence on cutoff length has been noted in previous work on active liquid crystals. \( ^{38} \) 

To confirm this macroscopic argument, we perform a modified version of the hydrodynamic simulation for a +1/2 defect in Sec. 2.4. For this modified simulation, we consider a channel with boundary conditions that require the director along the bottom

![](./images/867754548570095811_6.jpg)

(b) Velocity v(r,t)

![](./images/867754548570095811_7.jpg)

Fig. 5 Numerical solution of hydrodynamic equations for motion of a +1/2 defect toward the right, driven by extensile activity. (a) Director field shown by black lines, with scalar order parameter indicated by colored contours. (b) Velocity field shown by black arrows, with  \( |v|^{2} \)  indicated by colored contours. In both cases, the red arrow represents the defect orientation vector p. Parameters are  \( a = b = 200 \) , L = 4,  \( \alpha_{4} = 1 \) ,  \( \Gamma_{1} = 8 \) ,  \( \rho = 1 \) , d = 2, and Z = 0.25.

and top surfaces to be at \(\theta=\pm\pi/4\), as shown in Fig. 5(a). Because of that boundary condition, the director must rotate through an angle of \(\pi/2\) from bottom to top on both sides of the defect. Hence, in a system with equal Frank constants, there is equal elastic free energy on both sides of the defect. As a result, there is no elastic force in the \(x\) direction, the defect can move freely in this direction, and the only motion is driven by activity. Of course, there is still an elastic force that keeps the defect halfway between the walls in the \(y\) direction, and an elastic force that keeps the defect orientation at \(\Psi=\pi\).

We follow the same method as in Sec. 2.4, using the partial differential equations (53–54), but with the additional active term of Eq. (59) with coefficient Z in the dissipation function. The system quickly reaches a steady state, in which the defect moves to the left or right with constant velocity, and the fluid flow pattern moves along with the defect. Figure 5 shows an example of the liquid crystal order and fluid flow pattern for an extensile material  \( (Z > 0) \) . From these simulations, we can find the defect velocity u that is driven by activity.

In Fig. 6, we plot the numerical results for u as a function of activity coefficient Z. The results are well fit by the straight line u = 1.9Z. By comparison, from Eq. (69), we expect the relation  \( u = 0.2Z \)  (using  \( r_{max} = \frac{1}{2}d \)  and parameters given in the figure caption)). These relations show the same linear trend, although the quantitative discrepancy in the coefficient indicates a breakdown in some approximation. One possible issue may be that the analytic calculation was done in a circular geometry of radius  \( r_{max} \) , while the simulation was done in a rectangular geometry. For quantities like the passive drag force, which diverge logarithmically with system size, it is generally reasonable to approximate a rectangle by a circle with radius equal to the smaller rectangular
 
![](./images/867754548570095811_8.jpg)

Fig. 6 Numerical results for the velocity of a +1/2 defect as a function of the activity coefficient Z. The solid lines show a linear fit. Parameters are \(a = b = 200\), \(L = 4\), \(\Gamma_{1} = 8\), \(\alpha_{4} = 1\), \(\rho = 1\), and \(d = 2\), and hence \(r_{\mathrm{core}} = (L/a)^{1/2} = 0.2\) and \(\mathrm{bulk} S = (a/b)^{1/2} = 1\). Analogous parameters in the director representation are \(K = LS^{2}\), \(\gamma_{1} = \Gamma_{1} S^{2}\), and \(\zeta = Z S\).

(a) Director field at t = 0

![](./images/867754548570095811_9.jpg)

(b) Director field at t = 0.7

![](./images/867754548570095811_10.jpg)

(c) Director field at t = 1.9

![](./images/867754548570095811_11.jpg)

Fig. 7 Numerical solution of hydrodynamic equations for a +1/2 defect pushing against the top wall, driven by extensile activity. (a) The defect begins at the center of the channel, with its orientation vector p pointing downward. (b) The defect moves vertically upward until it reaches an equilibrium position at a distance  \( \delta y \)  below the top surface. (c) If the activity coefficient Z is greater than a critical value, the orientation p rotates slightly and the defect moves to the left or right at constant velocity. In all three visualizations, the director field is shown by black lines, with scalar order parameter indicated by colored contours. The velocity field is not shown. Parameters are a = b = 200, L = 4,  \( \alpha_{4} = 1 \) ,  \( \Gamma_{1} = 8 \) ,  \( \rho = 1 \) , d = 2, and Z = 30.

dimension. This may not be a reasonable approximation for the active driving force, which diverges more severely with system size.

## 3.3 Example: +1/2 defect pushing against wall

For a further example of defect motion, we modify the boundary conditions on the channel so that it requires planar alignment on the top surface and homeotropic alignment on the bottom surface. As a result, the system can form a defect of topological charge +1/2 with orientation vector  \( p = -\hat{y} \) , as shown in Fig. 7(a). When the system evolves with extensile activity Z > 0, the defect moves vertically toward the top surface, and it pushes against that wall, as in Fig. 7(b). After that, the behavior depends on the magnitude of the activity. If the activity is less than a critical value, the defect remains stable while pushing against the wall. By contrast, if the activity is greater than the critical value, the defect remains approximately stationary for some time, and then eventually breaks the symmetry between the  \( \pm\hat{x} \)  directions. At that time, it rotates its orientation slightly, and moves to the left or the right at constant velocity, as in Fig. 7(c). This symmetry-breaking behavior is similar to the formation of a “yinyang” structure by two +1/2 defects pushing outward against a circular wall. \( ^{55} \) 

In the simulation, we use fixed boundary conditions on the left and right edges, and hence the defect bounces off these edges and moves back and forth between left and right. Presumably, if the simulation were infinite in the x-direction, then the horizontal motion would continue at fixed velocity without limit.

This motion can be understood from the macroscopic view of a defect as an oriented particle. In the macroscopic view, the free energy arises from the interaction of the defect with the top aligning surface, which can equivalently be regarded as the interaction of the defect with an image defect above the top surface. Following the argument in our previous paper, \( ^{42} \)  this free energy becomes

 \[ F\approx-K\log\left(\frac{\delta y}{r_{\mathrm{c o r e}}}\right)+\frac{1}{2}K(\delta\Psi)^{2}, \quad (70) \] 

where K is the Frank constant,  \( \delta y = y_{max} - y \)  is the distance from the top surface, and  \( \delta\Psi = \Psi + \pi/2 \)  is the defect orientation relative to the favored orientation of  \( -\pi/2 \) . The dissipation function is still the same combination of passive and active terms as in Eq. (65).

In the first stage of motion, the defect moves upward until it reaches an equilibrium point at a fixed  \( \delta y \) . At that point, the elastic force pushing downward is  \( -\partial F/\partial y = -K/\delta y \) , and the active force pushing upward is  \( -\partial u/\partial y = D_{5} \) . Hence, the equilibrium occurs at the position

 \[ \delta y=\frac{K}{D_{5}}=\frac{3K}{\pi\zeta r_{\mathrm{m a x}}}\left(\frac{2\alpha_{4}}{\gamma_{1}}\right)^{1/2}=\frac{3L}{\pi Z r_{\mathrm{m a x}}}\left(\frac{2\alpha_{4}}{\Gamma_{1}}\right)^{1/2}. \quad (71) \] 

We can assume that the cutoff distance is  \( r_{max} \approx \delta y \) , because that is the distance from the defect to the nearest boundary. Hence, we obtain

 \[ \delta y\approx\left(\frac{3L}{\pi Z}\right)^{1/2}\left(\frac{2\alpha_{4}}{\Gamma_{1}}\right)^{1/4}. \quad (72) \]
 
![](./images/867754548570095811_12.jpg)

Fig. 8 Numerical results for a +1/2 defect pushing against the top wall, driven by extensile activity. (a) Distance  \( \delta y \)  below the top surface, as a function of activity coefficient Z, showing the scaling with  \( Z^{-1/2} \) .

(b) Velocity  \( u_{x} \) , also as a function of Z, showing the symmetry-breaking square-root bifurcation from the stationary state at low activity to the moving state at high activity. Parameters are  \( a = b = 200 \) , L = 4,  \( \Gamma_{1} = 8 \) ,  \( \alpha_{4} = 1 \) ,  \( \rho = 1 \) , and d = 2, and hence  \( r_{\mathrm{core}} = (L/a)^{1/2} = 0.2 \)  and bulk  \( S = (a/b)^{1/2} = 1 \) . Analogous parameters in the director representation are  \( K = LS^{2} \) ,  \( \gamma_{1} = \Gamma_{1}S^{2} \) , and  \( \zeta = ZS \) .

For the parameters in the simulation, this prediction gives  \( \delta y = 1.4Z^{-1/2} \) . In comparison, Fig. 8(a) shows the numerical results for  \( \delta y \)  as a function of Z, which are well fit by  \( \delta y = 1.0Z^{-1/2} \) . This agreement is reasonably good, considering the roughness of our estimate for the cutoff distance.

In the second stage of motion, the defect orientation  \( \Psi \)  rotates slightly, and the defect moves to the right or left with constant  \( \dot{x} \) , y, and  \( \Psi \) . The elastic force on  \( \Psi \)  is  \( -\partial F/\partial\Psi = -K\delta\Psi \) , and the drag force on  \( \Psi \)  is  \( -\partial D/\partial\Psi = -D_{4}\dot{x}\cos\delta\Psi \) . Likewise, the elastic force on x is zero, and the (passive plus active) drag force on  \( x \)  is  \( -\partial D/\partial\dot{x} = -D_{1}\dot{x} - D_{5}\sin\delta\Psi \)  (neglecting the  \( D_{2} \)  anisotropy). Balancing these two pairs of forces gives two simultaneous equations in  \( \delta\Psi \)  and  \( \dot{x} \) . The trivial solution to these equations is  \( \delta\Psi = \dot{x} = 0 \) . When the active coefficient  \( D_{5} \)  exceeds the critical value  \( D_{5}^{crit} = D_{1}K/D_{4} \) , there is a bifurcation to the nontrivial solution

 \[ \delta\Psi=\mp\left[\frac{3}{2}\frac{D_{5}-D_{5}^{\mathrm{c r i t}}}{D_{5}^{\mathrm{g r i t}}}\right]^{1/2}\propto\mp\left[Z-Z^{\mathrm{c r i t}}\right]^{1/2}, \] 

 \[ \dot{x}=\pm\frac{1}{D_{1}}\left[\frac{3}{2}D_{5}^{\mathrm{c r i t}}(D_{5}-D_{5}^{\mathrm{r i t}})\right]^{1/2}\propto\pm\left[Z-Z^{\mathrm{c r i t}}\right]^{1/2}. \quad (73) \] 

Hence, we expect a classic square-root bifurcation as a function of activity, beyond a finite critical activity. For comparison, Fig. 8(b) shows the numerical results for velocity  \( \dot{x} \)  as a function of Z. We can see the bifurcation at  \( Z^{crit} \) , with the velocity scaling as a square root for activity just above that point. Hence, the macroscopic view of defect dynamics effectively describes this instability.

## 4 Discussion

In this paper, we have combined the concept of defects as particles moving under forces with the concept of defect orientation. In this combined view, defects are effective particles with both position and orientation. Forces may act to change the position, orientation, or both. Hence, to predict the motion of defects, we must balance the elastic and drag forces acting on both position and orientation. For passive liquid crystals, the concept of defect orientation is moderately important, because it is an additional macroscopic degree of freedom, which can modify the elastic and drag forces. For active liquid crystals, the concept of defect orientation is even more important, because it defines the direction of the active force. In particular, +1/2 defects move as particles with a vector orientation, in a characteristic direction, while -1/2 defects move as particles with three-fold symmetry.

In addition to these specific results about defect orientation, we have explored the general formalism of the Rayleigh dissipation function as an approach to model the dynamics of liquid crystals. We see that this formalism can describe active dynamics, with activity appearing as a negative contribution to the dissipation. Of course, this negative contribution is not exactly dissipation; it might better be called the rate of energy input. Even so, it enters the dissipation function in a formal way to give the same equations of motion that have already been derived from an active stress tensor. Hence, it allows active forces to be modeled through the same approach as passive drag forces. We also see that the dissipation function formalism provides a way to coarse-grain the dynamics. By equating the dissipation functions calculated through different methods, one can go from the hydrodynamic theory of the director and velocity fields to the more macroscopic description of defects as effective oriented particles.

The greatest strength of the macroscopic description of defects as particles is to provide an intuitive understanding of defect motion. By considering all the forces acting on defect position and orientation, we can see how defects will move in either passive or active liquid crystals. The usefulness of this approach is demonstrated in the example of Sec. 3.3. In the macroscopic view of the defect as an oriented particle pushing against a wall, we can easily see that it should be stationary for low activity, but it should tilt and move horizontally for high activity. By contrast, in the hydrodynamic theory of the director and velocity fields, it is challenging to solve the partial differential equations for time evolution, and the result is not obvious.

By contrast, the greatest weakness of the macroscopic description is that the macroscopic drag coefficients  \( D_{1} \)  through  \( D_{5} \)  diverge logarithmically, or even more severely, as the cutoff length scale  \( r_{max} \rightarrow \infty \) . These divergences occur because defects create long-range distortions in the nematic director field, which only
 

decay slowly with distance from the defect core. Because of these divergences, the drag coefficients can change with the defect environment, especially as a defect gets close to a boundary or to other defects. That change is seen explicitly in the first stage of motion in Sec. 3.3, in the scaling behavior of  \( \delta y \)  with activity. This dependence on environment makes it more difficult to use the macroscopic approach for quantitative predictions of motion.

We note that 3D liquid crystals exhibit other types of moving structures, which are more localized than the 2D disclination defects studied here. These structures include skyrmions, topological configurations of a 3D director field, which “squirm” under an applied electric field. \( ^{56} \)  They also include bullet-like solitons, which form under an electric field and move rapidly across a sample. \( ^{57} \)  In future work, the macroscopic approach to dynamics might be applied to these structures. Because the director distortions are localized, we expect that all of the integrals for drag coefficients should converge. As a result, these structures might be even more effectively described as particles, with drag properties that are less dependent on their environment.

We would like to thank A. Baskaran for helpful discussions. This work was supported by National Science Foundation Grant No. DMR-1409658.

## References

1 I. Chuang, R. Durrer, N. Turok and B. Yurke, Science, 1991, 251, 1336–1342.

2 M. J. Bowick, L. Chandar, E. A. Schiff and A. M. Srivastava, Science, 1994, 263, 943–945.

3 A. Pargellis, N. Turok and B. Yurke, Phys. Rev. Lett., 1991, 67, 1570–1573.

4 A. N. Pargellis, P. Finn, J. W. Goodby, P. Panizza, B. Yurke and P. E. Cladis, Phys. Rev. A, 1992, 46, 7765–7776.

5 P. Oswald and J. Ignes-Mullol, Phys. Rev. Lett., 2005, 95, 027801.

6 C. Blanc, D. Svenšek, S. Žumer and M. Nobili, Phys. Rev. Lett., 2005, 95, 097802.

7 R. Stannarius, C. Bohley and A. Eremin, Phys. Rev. Lett., 2006, 97, 097802.

8 I. Dierking, M. Ravnik, E. Lark, J. Healey, G. P. Alexander and J. M. Yeomans, Phys. Rev. E, 2012, 85, 021703.

9 R. R. Guimaraes, R. S. Mendes, P. R. G. Fernandes and H. Mukai, J. Phys. Condens. Matter, 2013, 25, 404203.

10 Y.-K. Kim, S. V. Shiyanovskii and O. D. Lavrentovich, J. Phys. Condens. Matter, 2013, 25, 404202.

11 R. Stannarius and K. Harth, Phys. Rev. Lett., 2016, 117, 157801.

12 T. Sanchez, D. T. N. Chen, S. J. DeCamp, M. Heymann and Z. Dogic, Nature, 2012, 491, 431–434.

13 F. C. Keber, E. Loiseau, T. Sanchez, S. J. DeCamp, L. Giomi, M. J. Bowick, M. C. Marchetti, Z. Dogic and A. R. Bausch, Science, 2014, 345, 1135–1139.

14 S. J. DeCamp, G. S. Redner, A. Baskaran, M. F. Hagan and Z. Dogic, Nat. Mater., 2015, 14, 1110–1115.

15 J. L. Ericksen, Arch. Ration. Mech. Anal., 1960, 4, 231–237.

16 J. L. Ericksen, Trans. Soc. Rheol., 1961, 5, 23–34.

17 F. M. Leslie, Q. J. Mech. Appl. Math, 1966, 19, 357–370.

18 F. M. Leslie, Arch. Ration. Mech. Anal., 1968, 28, 265–283.

19 A. Beris and B. Edwards, Thermodynamics of Flowing Systems, Oxford, 1994.

20 G. Tóth, C. Denniston and J. M. Yeomans, Phys. Rev. Lett., 2002, 88, 105504.

21 D. Svenšek and S. Žumer, Phys. Rev. Lett., 2003, 90, 155501.

22 R. A. Simha and S. Ramaswamy, Phys. Rev. Lett., 2002, 89, 058101.

23 M. C. Marchetti, J. F. Joanny, S. Ramaswamy, T. B. Liverpool, J. Prost, M. Rao and R. A. Simha, Rev. Mod. Phys., 2013, 85, 1143–1189.

24 J. Prost, F. Jülicher and J.-F. Joanny, Nature Physics, 2015, 11, 111–117.

25 S. Ramaswamy, J. Stat. Mech. Theory Exp., 2017, 2017, 054002.

26 A. Doostmohammadi, J. Ignés-Mullol, J. M. Yeomans and F. Sagués, Nat. Commun., 2018, 9, 3246.

27 C. M. Dafermos, Q. J. Mech. Appl. Math, 1970, 23, 49–64.

28 H. Imura and K. Okano, Phys. Lett. A, 1973, 42, 403–404.

29 L. M. Pismen and J. D. Rodriguez, Phys. Rev. A, 1990, 42, 2471–2474.

30 G. Ryskin and M. Kremenetsky, Phys. Rev. Lett., 1991, 67, 1574–1577.

31 C. Denniston, Phys. Rev. B, 1996, 54, 6272–6275.

32 L. Radzihovsky, Phys. Rev. Lett., 2015, 115, 247801.

33 E. I. Kats, V. V. Lebedev and S. V. Malinin, J. Exp. Theor. Phys., 2002, 95, 714–727.

34 A. M. Sonnet, Continuum Mech. Thermodyn., 2005, 17, 287–295.

35 A. M. Sonnet and E. G. Virga, Liquid Crystals, 2009, 36, 1185–1192.

36 L. Giomi, M. J. Bowick, X. Ma and M. C. Marchetti, Phys. Rev. Lett., 2013, 110, 228101.

37 L. M. Pismen, Phys. Rev. E, 2013, 88, 050502.

38 L. Giomi, M. J. Bowick, P. Mishra, R. Sknepnek and M. C. Marchetti, Philos. Trans. Royal Soc. A, 2014, 372, 20130365.

39 R. Zhang, N. Kumar, J. L. Ross, M. L. Gardel and J. J. de Pablo, Proc. Natl. Acad. Sci. U.S.A., 2018, 115, E124–E133.

40 D. Cortese, J. Eggers and T. B. Liverpool, Phys. Rev. E, 2018, 97, 022704.

41 A. J. Vromans and L. Giomi, Soft Matter, 2016, 12, 6490–6495.

42 X. Tang and J. V. Selinger, Soft Matter, 2017, 13, 5481–5490.

43 S. Shankar, S. Ramaswamy, M. C. Marchetti and M. J. Bowick, Phys. Rev. Lett., 2018, 121, 108002.

44 G. Vertogen, Z. Naturforsch. A, 1983, 38, 1273–1275.

45 G. Vertogen and W. H. de Jeu, Thermotropic Liquid Crystals, Fundamentals, Springer, 1988.

46 A. M. Sonnet and E. G. Virga, Phys. Rev. E, 2001, 64, 031705.

47 A. M. Sonnet and E. G. Virga, Dissipative Ordered Fluids: Theories for Liquid Crystals, Springer, 2012.
 

48 M. Doi, J. Phys. Condens. Matter, 2011, 23, 284118.

49 I. W. Stewart, The Static and Dynamic Continuum Theory of Liquid Crystals, Taylor & Francis, 2004.

50 G. Ryskin, J. Non-Newton. Fluid Mech., 1991, 39, 207–210.

51 A. Chakrabarty, A. Konya, F. Wang, J. V. Selinger, K. Sun and Q.-H. Wei, Phys. Rev. Lett., 2013, 111, 160603.

52 P. Pieranski, M. H. Godinho and S. Čopar, Phys. Rev. E, 2016, 94, 042706.

53 P. Pieranski, S. Čopar, M. H. Godinho and M. Dazza, Eur. Phys. J. E, 2016, 39, 121.

54 M. Ravnik, personal communication.

55 M. M. Norton, A. Baskaran, A. Opathalage, B. Langeslay, S. Fraden, A. Baskaran and M. F. Hagan, Physical Review E, 2018, 97, 012702.

56 P. J. Ackerman, T. Boyle and I. I. Smalyukh, Nat. Commun., 2017, 8, 673.

57 B.-X. Li, V. Borshch, R.-L. Xiao, S. Paladugu, T. Turiv, S. V. Shiyanovskii and O. D. Lavrentovich, Nat. Commun., 2018, 9, 2912.
 
