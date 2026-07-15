Modelling and Simulation in Materials Science and Engineering

ACCEPTED MANUSCRIPT

# A spectral approach for discrete dislocation dynamics simulations of nanoindentation

To cite this article before publication: Nicolas R Bertin *et al* 2018 *Modelling Simul. Mater. Sci. Eng.* in press https://doi.org/10.1088/1361-651X/aabea1

Manuscript version: Accepted Manuscript

Accepted Manuscript is "the version of the article accepted for publication including all changes made as a result of the peer review process, and which may also include the addition to the article by IOP Publishing of a header, an article ID, a cover sheet and/or an 'Accepted Manuscript' watermark, but excluding any other editing, typesetting or other changes made by IOP Publishing and/or its licensors"

This Accepted Manuscript is © 2018 IOP Publishing Ltd.

During the embargo period (the 12 month period from the publication of the Version of Record of this article), the Accepted Manuscript is fully protected by copyright and cannot be reused or reposted elsewhere.
As the Version of Record of this article is going to be / has been published on a subscription basis, this Accepted Manuscript is available for reuse under a CC BY-NC-ND 3.0 licence after the 12 month embargo period.

After the embargo period, everyone is permitted to use copy and redistribute this article for non-commercial purposes only, provided that they adhere to all the terms of the licence https://creativecommons.org/licences/by-nc-nd/3.0

Although reasonable endeavours have been taken to obtain all necessary permissions from third parties to include their copyrighted content within this article, their full citation and copyright line may not be present in this Accepted Manuscript version. Before using any content from this article, please refer to the Version of Record on IOPscience once published for full citation and copyright details, as permissions will likely be required. All third party content is fully copyright protected, unless specifically stated otherwise in the figure caption in the Version of Record.

View the article online for updates and enhancements.

This content was downloaded from IP address 138.26.31.3 on 21/04/2018 at 13:25

ization technique, nanoindentation experiments have offered a unique opportunity to understand fundamental plasticity mechanisms. However, the connection between experimental responses (e.g. force-displacement curves, surface imprint) and plastic mechanisms at the nanoscale is still not fully understood, and extracting plastic properties (e.g. yield stress, hardening rate, etc.) directly from nanoindentation experiments remains a challenging task.

Concurrently, several modeling approaches have been employed to study the plasticity in the context of indentation experiments. At the continuum scale, the development of non-local plasticity theories (e.g. based on the concept of geometrically necessary dislocations (GND) [1] and strain gradient plasticity [2]), motivated by the discovery of the ISE, have proposed compelling extensions to classical continuum plasticity models in which indentation hardness is inherently scale independent. Over the years, non-local theories have led to critical insights on the plastic behavior of crystals, especially by exposing the key role of strain gradients in inhomogeneous deformation, and have led to the development of successful crystal plasticity models, that have been later incorporated into Finite Element Method (FEM) frameworks. However, as any continuum descriptions relying on phenomenological assumptions, such models do not contain an explicit representation of the materials microstructure, and therefore cannot be directly employed to elucidate the key mechanisms taking place at the scale of individual defects (e.g. dislocations). At the atomic scale, Molecular Dynamics (MD) simulations have been used to investigate plasticity mechanisms during indentation. However due to computational limitations, such simulations are typically limited to the study of first dislocation nucleation and pop-in events occurring during the early stage of the indentation process, and are restricted to indenters with very small radius of curvature. Consequently, MD simulations cannot be directly employed to simulate the collective behavior of dislocations during the whole indentation process on length scales relevant to experimental conditions.

In principle, Discrete Dislocation Dynamics (DDD) simulations can be used to bridge the gap between MD simulations and higher scales modeling such as Crystal Plasticity FEM (CP-FEM). In recent years, DDD simulations have demonstrated their usefulness in the study of plasticity in single crystals at the mesoscale. By allowing simulations on representative volumes typically on the order of several microns, DDD overcomes the time and length scales limitations associated with MD simulations, while retain-

ing an explicit representation of individual dislocation lines.

As a result, DDD models offer a fundamentally different approach for the study of plasticity compared to non-local continuum theories. At their core, plasticity in non-local models is governed by the generation of GNDs required to accommodate lattice curvatures in regions of high strain gradi- ents, while their evolution is specified in a phenomenological manner at the constitutive level. In contrast, DDD operates at a more fundamental level. The multiplication of dislocations and resulting plasticity directly evolve in response to stress via the Peach-Kohler force, while assumptions are pri- marily remitted to the choice of the initial conditions. Thus, by treating the physics of individual dislocations in an explicit fashion, DDD simula- tions offer a possibility for calibrating, validating and refining higher-scale models of plasticity.

Several DDD approaches have been developed to simulate nanoinden- tation experiments. It was for instance used to investigate the ISE as a function of the indenter shape [3], of the initial dislocation content [4], in single crystal thin-films [5], and to examine lattice rotations during inden- tation [6]. Interstingly, it appears that all these works employed 2D DDD simulations, presumably owing to the high cost associated with indentation simulations of dislocations. As a result, such simulations cannot capture the complex three-dimensional dislocation structures likely to develop un- der indentation loadings, and are further limited to consider symmetric indenter geometries, such as wedge or circular indenters. In comparison, few 3D DDD implementations were developed for nanoindentation simula- tions. Fivel and co-workers first proposed an edge / screw DDD framework in which a dislocation nucleation model was included [7, 8]. More recently, nodal implementations were used to investigate the formation of prismatic loops [9] and the effect of dislocation density on the incipient plasticity [10] during indentation. In all these approaches, the DDD model is coupled with a three-dimensional FEM framework to enforce the boundary conditions as- sociated with the indentation problem, thereby significantly increasing the computational burden associated with these simulations.

In this work we present an efficient spectral approach to perform nanoin- dentation simulations using a three-dimensional DDD model with nodal representation. The method relies on a staggered approach, whereby the contact problem between the indenter and the sample is first solved to deter- mine the contact pressure on the material's surface, after which the contact pressure is used as a boundary condition to determine the resulting stress

field produced within the whole simulation volume. In both stages, the mechanical fields are efficiently computed by means of Fast Fourier Transforms (FFT), following the spectral approach introduced in [11]. With this framework, the image stress produced by dislocations interactions with the free surface (outside of the contact region) is inherently accounted for. Thanks to its FFT-based formulation, the method is shown to be more efficient than three-dimensional FEM-based approaches by several orders of magnitude.

The goal of this paper is to present the numerical aspects of the proposed DDD spectral nanoindentation approach, and to provide some simple applications demonstrating its capabilities. The use of the method to gain physical insights on the plasticity during indentation will be the subject of a separate work. The rest of the paper is organized as follows. In section 2, the challenges associated with DDD nanoindentation simulations are briefly highlighted, after which the two stages of the spectral approach developed for the contact problem are presented in detail in §2.2. Special algorithms to accelerate the DDD simulation are then discussed in §2.3. In section 3, the validity of the method is demonstrated through a series of relevant benchmarks. Finally, an example of a DDD nanoindentation simulation with an initially complex microstructure is presented in §3.4.

## 2. Spectral approach for dislocation dynamics

### 2.1. General principle of DDD simulations and challenges

In this section, the key aspects of DDD simulations are briefly summarized while the challenges associated with the development of a three-dimensional nanoindentation nodal DDD simulation tool are presented. For a full description of the DDD approach, the reader is referred to references [12-16].

In nodal DDD simulations, dislocation lines are discretized into a series of segments connecting a set of nodes. The degrees of freedom of the simulated system are the dislocation nodal positions that are advanced in time. For that purpose, forces and velocities need to be calculated on each dislocation node.

The driving force $\vec{f}$ for dislocation motion is produced by the stress acting along each dislocation line, as expressed by the Peach-Koehler relation:

$$
\vec{f}=\left(\sigma^{\mathrm{tot}} \cdot \vec{b}\right) \times \vec{t} \tag{1}
$$

where $\vec{b}$ and $\vec{t}$ are the Burgers vector and the line tangent of the dislocation line, respectively. Following the superposition method introduced in [12, 15], the total stress $\sigma^{\text{tot}}$, which encompasses the contributions of all stress fields acting on dislocation lines, can be decomposed as:

$$
\sigma^{\text{tot}} = \sigma^{\infty} + \sigma^{\text{app}} + \sigma^{\text{cor}} \tag{2}
$$

where $\sigma^{\infty}$ are the stress fields in an infinite medium arising from the presence of all dislocation segments within the simulation volume, $\sigma^{\text{app}}$ is the stress from the applied loading, and $\sigma^{\text{cor}}$ is the image stress added to correct for the boundary conditions when necessary (e.g. in presence of free surfaces).

Combining equations (1) and (2), the forces on each dislocation segment can be calculated and assembled at the dislocation nodes. From there, the velocity $\vec{V}_i$ of each node $i$ is determined from its nodal force $\vec{F}_i$ through a mobility function:

$$
\vec{V}_i = \mathcal{M} \left( \vec{F}_i \right) \tag{3}
$$

The mobility function $\mathcal{M}$ is typically chosen to reproduce experimental observations of dislocation motion in the material of interest, or extracted from atomistic simulations. Once the nodal velocities are determined, new positions of the nodes are obtained by time-integration. During this process, the time step size is typically determined upon convergence of the nodal positions according to a specified tolerance [16]. Finally, after all dislocation nodes have been advanced in time, topological operations such as dislocation line collisions (e.g. leading to junction formation) and dislocation remeshing are performed.

Modelling nanoindentation experiments with DDD is achieved by cou- pling (i) a conventional DDD simulation of dislocations lines in an elastic half-space and (ii) a contact problem between an indenter of a given geom- etry and the elastic half-space. The challenges of enabling such simulations lie in three main aspects. First, the stress field contributions $\sigma^{\text{app}}$ and $\sigma^{\text{cor}}$ induced by the contact between the indenter and the free surface, respec- tively, must be determined along every dislocation segment present in the simulation volume. Second, the morphology of the free surface must be accurately represented in order to properly model the contact with the in- denter. Specifically, the surface steps produced by dislocations escaping the volume must be finely accounted for, as these provide an essential plastic- ity mechanism for accommodating the deformation. Finally, the important stress gradients produced during indentation experiments are expected to

(i) severely hinder the numerical convergence of dislocation motion, and (ii) generally result in substantial dislocation multiplication, further increasing the computational burden associated with nodal forces calculation. As a result, efficient time integration schemes need to be used in order to allow for accurate and tractable simulations.

From a general perspective, the different stages of a DDD nanoindenta- tion simulation are summarized in figure 1. The key aspects of each stage of the simulation are described in details in the next sections.

![](./images/813042432055705600_1.jpg)

Figure 1: Flow chart of a DDD nanoindentation simulation.

### 2.2. Spectral approach for the contact problem

Fundamentally, the indentation contact problem corresponds to a bound- ary value problem subjected to (i) displacement boundary conditions in the contact area, and (ii) traction-free boundary conditions outside of the con- tact area. Several approaches such as the collocation method, the Boundary Element Method (BEM), and the Finite Element Method (FEM) have been employed to address this problem in both the general context [17], and in the more specific context of DDD simulations [3–5, 7, 8] in which the su- perposition method [12, 15] is used. In this work, we propose a numerically

efficient approach based on the spectral method recently developed in [11] to solve for the image stress fields in equation (2) in the context of the superposition approach.

Essentially, the numerical procedure to model indentation can be decomposed into two steps. First, the contact problem is solved and the mechanical state (e.g. displacement, contact pressure) of the free surface is completely determined. Then, displacement and stress fields within the volume (e.g. along dislocation segments) are calculated based on the boundary conditions determined on the surface.

### 2.2.1. Contact solver
Consider the case of a contact problem between an indenter of arbitrary shape and an elastic half-space $z \leq 0$, i.e. with free surface at $z = 0$. When the two bodies come in contact, normal contact stress (or contact pressure) is generated, causing the surface of both solids to deflect inwards. In frictionless contact, the normal composite deflection $\bar{u}_z(x,y)$ field produced by a given contact pressure $p(x,y)$ is expressed as [18]:

$$
\bar{u}_{z}(x, y)=\iint_{S} Q\left(x-x^{\prime}, y-y^{\prime}\right) p\left(x^{\prime}, y^{\prime}\right) d x^{\prime} d y^{\prime}
\tag{4}
$$

where $Q(x,y)$ is the kernel function defining the elastic deflection produced by a unit point load acting on surface $S$. For two isotropic elastic bodies, $Q(x,y)$ is given by the Boussinesq formula [18]:

$$
Q(x, y)=\left(\frac{1-\nu_{1}^{2}}{\pi E_{1}}+\frac{1-\nu_{2}^{2}}{\pi E_{2}}\right) \frac{1}{\sqrt{x^{2}+y^{2}}}
\tag{5}
$$

where $E_1, E_2$ and $\nu_1, \nu_2$ are the Young moduli and Poisson's ratios of the two bodies, respectively. If we assume for simplicity a rigid indenter, the kernel in equation (5) reduces to:

$$
Q(x, y)=\frac{1-\nu^{2}}{\pi E} \frac{1}{\sqrt{x^{2}+y^{2}}}
\tag{6}
$$

where $E$ and $\nu$ are the Young modulus and the Poisson's ratio of the elastic half-space, and the normal displacement field in equation (4) now solely corresponds to the displacement of the half-space surface at $z = 0$.

For numerical convenience, we now assume that the elastic half-space is subjected to periodic boundary conditions (PBC) in the $x$ and $y$ directions,

with periodicity $L_x$ and $L_y$, respectively. The surface displacement and
contact pressure in equation (4) can be expanded in Fourier series as:

$$
\bar{u}_{z}(x, y)=\sum_{k_{x}} \sum_{k_{y}} \hat{\bar{u}}_{z}\left(k_{x}, k_{y}\right) e^{i k_{x} x+i k_{y} y}
$$

$$
p(x, y)=\sum_{k_{x}} \sum_{k_{y}} \hat{p}\left(k_{x}, k_{y}\right) e^{i k_{x} x+i k_{y} y}
\tag{7}
$$

where $\hat{\bar{u}}_{z}$ and $\hat{p}$ are the Fourier transforms of fields $\bar{u}_{z}$ and $p$, respectively,
and $k_x = 2\pi/L_x \cdot m$ and $k_y = 2\pi/L_y \cdot n$, with $m=(-N_x/2,...,N_x/2-1)$
and $n=(-N_y/2,...,N_y/2-1)$.

Using expressions (7), the convolution in equation (4) can be conve-
niently calculated in the Fourier space as:

$$
\hat{\bar{u}}_{z}(\vec{k})=\hat{Q}(\vec{k}) \hat{p}(\vec{k}), \quad \forall \vec{k} \neq \overrightarrow{0}
$$

$$
\hat{\bar{u}}_{z}(\overrightarrow{0})=\frac{L_{z}}{E}\langle p\rangle
\tag{8}
$$

where $\hat{Q}(\vec{k})$ is the Fourier coefficient associated with the kernel in equa-
tion (6) for each non-zero Fourier mode $\vec{k}=(k_x,k_y)$. In equation (8), $\hat{\bar{u}}_{z}(\overrightarrow{0})$
denotes the uniform displacement mode of the half-space surface resulting
from the average imposed force. In the present formulation, it corresponds
to the downward displacement produced by an uniaxial load $\langle p\rangle$ imposed
on the elastic half-space volume of height $L_z$ (along the $z$ direction), where
$\langle p\rangle=\frac{1}{S} \int_{S} p(x, y) d S$ denotes the average pressure acting on the free surface
$S$.

When solving for the contact problem in the context of an indentation
simulation, neither the pressure field $p(x, y)$ nor the contact area $S_{c}$ is known
a priori. However, the problem is fully specified by the following set of
equations:

$$
h(x, y)=u_{z}(x, y)+u_{z}^{p}(x, y)-\left(u_{\text {ind }}(x, y)+d\right) \quad \text { (gap) } \tag{9}
$$

$$
h(x, y)=0 \text { and } p(x, y) \geq 0 \quad \text { for }(x, y) \in S_{c} \quad \text { (contact region) } \tag{10}
$$

$$
h(x, y)>0 \text { and } p(x, y)=0 \quad \text { for }(x, y) \notin S_{c} \quad \text { (gap region) } \tag{11}
$$

where $h(x, y)$ denotes the gap between the free surface and the indenter,
$u_{\text{ind}}(x,y)$ describes the shape of the rigid indenter, and $d$ denotes the dis-
placement of the indenter in the downward direction. Note that with this

in step 4 is implemented. Specifically, a guess for $\delta$ is first chosen, and the error is monitored during the iterative process: if the error increases, the procedure is aborted and re-attempted with a smaller $\delta$; alternatively, when convergence is achieved, the value of $\delta$ is slightly increased for the next time step. In practice, the error can be evaluated by comparing the solution of successive iterations, or can be estimated by the product $\int_{S}|h(x,y)| \cdot |p(x,y)|dS$ which should vanish everywhere on the surface.

When the total force $F$ exerted by the indenter is prescribed as a boundary condition (instead of the displacement $d$), the contact problem can still be solved using the algorithm described above, with the addition that the contact pressure must be rescaled at each iteration to ensure that $\int_{S} p(x,y)dS = F$. During the iterative process, the displacement $d$ of the rigid indenter can be obtained from the largest magnitude of the surface deflection $u_z(x,y)$.

### 2.2.2. Stress field solver
Once the contact pressure $p(x,y)$ is obtained everywhere on the surface, the elastic displacement and stress fields within the volume are computed using the spectral approach introduced in [11]. While the approach in [11] was originally developed to solve the image problem associated with dislocations interactions with free-surfaces in half-spaces and thin-films, the method can, in principle, be employed to compute image stresses associated with arbitrary surface displacement and traction fields prescribed as boundary conditions, as shown in the following.

In the absence of body forces, the stress equilibrium in an isotropic linear elastic medium can be written in terms of the displacement field $\vec{u}(\vec{x})$ as:

$$
\mu u_{i, j j}+(\lambda+\mu) u_{j, j i}=0 \tag{12}
$$

where $\lambda$ and $\mu$ are the Lamé constants ($\mu$ is the shear modulus). Considering an elastic half-space (as for the indentation problem) that occupies region $z \leq 0$ and that is periodic in the $x$ and $y$ directions, the solution displacement field to equation (12) can be conveniently obtained as a Fourier series [20]:

$$
\vec{u}(x, y, z)=\sum_{k_{x}} \sum_{k_{y}} \tilde{\vec{u}}\left(k_{x}, k_{y}, z\right) e^{i k_{x} x+i k_{y} y} \tag{13}
$$

where the components of the Fourier coefficients $\tilde{\vec{u}}(k_x,k_y,z)$ corresponding to Fourier mode $(k_x,k_y)$ are given by:

$$
\hat{u}_{x}^{-}=\left(A k_{x} z-B k_{y}+i C k_{x}\right) e^{k_{z} z}
$$

$$
\hat{u}_{y}^{-}=\left(A k_{y} z+B k_{x}+i C k_{y}\right) e^{k_{z} z}
$$

$$
\hat{u}_{z}^{-}=\left(-i A k_{z} z+i A \frac{\lambda+3 \mu}{\lambda+\mu}+C k_{z}\right) e^{k_{z} z}
\tag{14}
$$

where $k_{z}=\sqrt{k_{x}^{2}+k_{y}^{2}}$ and $A$, $B$ and $C$ are complex coefficients [11]. Here superscript $\cdot^{-}$ is used to indicate that the solution exists in the domain $z \leq 0$. Using equations (13) and (14), the stress field can be readily obtained from Hooke's law as:

$$
\sigma_{i j}=\lambda u_{k, k} \delta_{i j}+\mu\left(u_{i, j}+u_{j, i}\right)
\tag{15}
$$

and is further expanded in Fourier series as follows:

$$
\sigma(x, y, z)=\sum_{k_{x}} \sum_{k_{y}} \hat{\sigma}\left(k_{x}, k_{y}, z\right) e^{i k_{x} x+i k_{y} y}
\tag{16}
$$

where the Fourier coefficients $\hat{\sigma}_{i j}\left(k_{x}, k_{y}, z\right)$ are related to the complex coefficients $A, B, C$ through the relations provided in Appendix C. The corresponding traction field on the free surface $z=0$ is composed of stress components $\sigma_{x z}, \sigma_{y z}, \sigma_{z z}$ and can be expanded in the following form:

$$
\vec{T}(x, y)=\sum_{k_{x}} \sum_{k_{y}}\left(\begin{array}{c}
\hat{T}_{x} \\
\hat{T}_{y} \\
\hat{T}_{z}
\end{array}\right) e^{i k_{x} x+i k_{y} y}
\tag{17}
$$

where $\hat{T}_{x}, \hat{T}_{y}, \hat{T}_{z}$ are related to the coefficients $A, B, C$ through the matrix $M$ (see Appendix C) as:

$$
\left(\begin{array}{c}
\hat{T}_{x} \\
\hat{T}_{y} \\
\hat{T}_{z}
\end{array}\right)=[M]\left(\begin{array}{c}
A \\
B \\
C
\end{array}\right)
\tag{18}
$$

From relationships (17) and (18), the Fourier coefficients $A, B, C$ associated with every Fourier mode $\left(k_{x}, k_{y}\right)$ can be determined, given any arbitrary surface traction field $\vec{T}(x, y)$.

In the case of a DDD nanoindentation simulation, the traction on the free surface is composed of two contributions. First, it contains the contribution from the contact pressure field $p(x, y)$ determined using relations (4)-(11).

Second, the presence of dislocations within the volume induces a non-zero traction field $\vec{T}^{\infty}(x,y)$ on the half-space surface. This contribution needs to be canceled out on the free surface. The equilibrium of traction on the surface is therefore specified by the following relation:

$$
\vec{T}^{\infty}+\vec{T}^{\text {img }}=\vec{T}^{\text {app }}
\tag{19}
$$

where $\vec{T}^{\text{app}}$ denotes the applied loading (from the indenter), whose only non-zero component (in the $z$-direction) is the contact pressure $p(x,y)$, and $\vec{T}^{\text{img}}$ is the image traction to enforce the boundary conditions; when there is no contact with the indenter ($\vec{T}^{\text{app}}=\vec{0}$), relation (19) reduces to the classical correction approach whereby the image traction is used to cancel dislocations stresses on the free surface (e.g. see [11, 12]); when no dislocation is present ($\vec{T}^{\infty}=\vec{0}$), the image traction solely corresponds to the loading imposed on the surface. Thus, the DDD indentation boundary value problem can be completely solved by prescribing the image traction field as the boundary condition in the spectral approach:

$$
\vec{T}^{\mathrm{img}}(x, y)=\left(\begin{array}{c}
-T_{x}^{\infty}(x, y) \\
-T_{y}^{\infty}(x, y) \\
p(x, y)-T_{z}^{\infty}(x, y)
\end{array}\right)
\tag{20}
$$

From there, the corresponding Fourier coefficients $A,B,C$ are obtained through relation (18), and the resulting displacement and stress field is completely determined in the region $z\leq0$ using equations (13), (14) and (15). The stress field calculated with this approach encompasses both the applied $\sigma^{\text{app}}$ (from the indenter contact) and the image $\sigma^{\text{cor}}$ (to correct for the presence of the free surface) contributions, thereby providing all the additional stress contributions required to calculate the driving force on each dislocation segment present in the DDD simulation (see equation (2)).

### 2.2.3. Numerical implementation and efficiency of the spectral method

Numerically, the spectral method detailed in the above is implemented in the ParaDiS code [21] by discretizing the free surface $z=0$ into a regular grid $\{x_i,y_i\}_{i=1,...,N_{\text{grid}}}$ of $N_{\text{grid}}=N_x\times N_y$ pixels. The method then operates in a staggered manner. First, the surface contact problem (9)-(11) is solved to determine the contact pressure $p(x_i,y_i)$ everywhere on the surface grid. During this process, the convolution in equation (8) is conveniently calculated in the Fourier space using FFTs. After convergence is achieved, the total load is obtained as $F=\sum_i p(x_i,y_i)\Delta_x\Delta_y$, where $\Delta_x$ and $\Delta_y$ are the

dimensions of the grid pixels in the $x$ and $y$ directions, respectively. The contact area is evaluated as $A = \sum_{i \in S_c} \Delta_x \Delta_y$, where the contact region $S_c$ is defined as the union of every pixel $i$ for which $p(x_i, y_i) \geq 0$ (see relation (10)). The Fourier coefficients $A, B, C$ required to evaluate the stress field in the volume are then determined using equation (18) by computing the FFT of the traction field $\vec{T}^{\text{img}}(x_i, y_i)$ prescribed on the free surface. The indenter and image stress acting on dislocation segments is then evaluated using equation (16).

The main advantage of employing the spectral approach for solving the contact problem lies in its computational efficiency. Specifically, when using a surface grid of size $N_{\text{grid}} = N_x \times N_y$, both the computation of the surface pressure field and individual iterations of the stress field solver require $\mathcal{O}(N_{\text{grid}} \log N_{\text{grid}})$ operations thanks to the FFT algorithm. Comparatively, solving the problem using a FEM approach is much more expensive at equivalent resolutions (see §3.5). First, this is because FEM achieves at best quadratic complexity in the number of elements. Second, using a FEM method requires to mesh the entire three-dimensional simulation volume. While the FEM allows for non-uniform meshes and local refinements, the stress field induced by an indenter load on the surface typically decays as $1/r^2$ and therefore requires a fine volumetric mesh in the vicinity of the contact zone, often yielding the cost of the FEM solver to be higher than that of solving the dislocation dynamics problem (see §3.5 for more details).

Nevertheless, one advantage of the FEM is that the indenter stress is retrieved in constant time on each segment by interpolation from the elements nodes. In the spectral method, it requires a summation over all Fourier modes, using equation (16). To alleviate this cost, an interpolation approach is employed by tabulating the indenter stress field, as described in §2.3.2.

Finally, we note that the main limitations associated with the FFT-based method are the prerequisites to (i) use a regular grid, and (ii) prescribe PBC in the surface plane.

### 2.3. Efficient algorithms for the DDD simulation
#### 2.3.1. Subcycling time-integration
To alleviate the computational cost and allow for nanoindentation simulations capable of reaching relevant deformation levels, the new subcycling time-integrator developed in [22] is coupled with the spectral nanoindentation framework. In the subcycling approach, the forces exerted on dislocation lines are broken down into different groups so as to isolate stiff

and non-linear modes from well-behaving interaction forces. At every time step, each group is then time-integrated under its proper time step size in a sequential fashion, as detailed in [22]. Since only a fraction of the overall dislocation interaction forces require small time steps and these are isolated from the rest of the system, significant computational gains are allowed in comparison with regular integrators, e.g. typically about two orders of magnitude compared to a Heun integrator [22].

In the context of nanoindentation simulations, a special treatment for the indenter force contribution has been devised to ensure efficient integra- tion with the subcycling approach. As mentioned earlier, the deformation associated with the indenter contact typically leads to high stress gradients, thus resulting in highly non-linear interactions with dislocation segments. This contribution is therefore grouped with all other stiff modes of the sys- tem.

### 2.3.2. Image stress interpolation

Although the spectral approach allows for a fast determination of the surface displacement Fourier coefficients, the evaluation of the correspond- ing stress along each dislocation segment using relation (16) still requires $\mathcal{O}(N_{\text{grid}})$ operations. While it might seem reasonable in a regular DDD simulation, it can quickly becomes very inefficient in the current context, especially when subcycling is used. This is because the forces on each seg- ment might be evaluated up to thousands of times during subcycling, while the stress field produced by the indenter remains constant. Consequently, substantial computational gains can be obtained by first tabulating the in- denter stress contribution on a regular grid spanning the entire half-space volume, and then evaluating the stress during time-integration by quadratic interpolation of the grid values, in a similar way to using a regular FEM mesh. The tabulation can be achieved efficiently by first partitioning the volume into a series of $N_z$ regularly spaced planes along the $z$-direction. For each $z$-plane, the stress is then calculated on a grid of the same resolution as the surface grid (i.e. with $N_{\text{grid}} = N_x \times N_y$ pixels) using a FFT (from the stress coefficients provided in Appendix C). With this, the indenter stress is entirely tabulated in $\mathcal{O}(N_z N_{\text{grid}} \log N_{\text{grid}})$ operations and is retrieved in constant time for each segment force evaluation during subcycling. More details on the accuracy of this procedure are provided in §3.5.

### 2.3.3. Surface steps displacement field

In the context of nanoindentation, surface steps created by dislocations intersecting the surface play a crucial role by providing a plastic mecha- nism to accommodate the deformation in the contact region. Specifically, accounting for the displacement field associated with the surface steps is critical to appropriately capture the plastic response produced by the in- denter load. Following the procedure fully described in Appendix B, the implementation of the surface displacements calculation proceeds in two stages. First, surface steps are created and evolved by tracking dislocation segments that intersect and escape the free surface. Then, the correspond- ing displacement field is evaluated on the half-space surface.

For the sake of numerical efficiency, the displacement field associated with each surface step is approximated by the displacement produced by an infinite screw dislocation dipole, orthogonal to the surface, and piercing the latter at both extremities of the surface step (see Appendix B). Note that this method differs from the conventional approach used for computing dislocations displacement fields (e.g. see [23]), in which the contribution of every dislocation segment present in the simulation is accounted for. The difference between both methods is a smooth field whose contribution is expected to have a minor effect on the overall mechanical response. This is because this approximation captures the discontinuous jumps experienced across the steps while producing a smooth displacement field (normal to the surface) in their vicinity. The main advantage of this method is that it allows for a significant reduction in computational cost. Instead of summing the displacement contribution for all segments in the simulation, only the displacement associated with surface steps need to be evaluated.

## 3. Examples and discussion

### 3.1. Elastic contact

As a first benchmark, the indentation spectral method presented in sec- tion 2 is employed to simulate the contact between a rigid indenter and a purely elastic half-space (i.e. without any dislocation).

#### 3.1.1. Surface contact at constant depth

The contact between the indenter and the half-space surface is first examined by performing a constant depth $d$ indentation simulation. The resulting elastic displacement profiles $u_z(x, y)$ of the half-space surface ob- tained for a parabolic indenter of radius $R = 1000b$ and a Berkovich indenter

![](./images/813042432055705600_2.jpg)

(a) Parabolic indenter

![](./images/813042432055705600_3.jpg)

(b) Berkovich indenter

Figure 2: Surface displacement profile $u_z(x,y)$ at depth $d=2000b$ for the contact with
(a) a parabolic indenter of radius $R=1000b$ and (b) a Berkovich indenter.

are reported in figure 2(a)-(b). In these examples, the indentation depth
is set to $d = 2000b$, where $b = 2.86 \times 10^{-10}$ m is the magnitude of the
Burgers vector in pure Aluminum. As expected, it is shown in both cases
that the displacement profile perfectly matches the indenter shape in the
contact region, thereby validating the iterative contact algorithm.

#### 3.1.2. Force-displacement response

The force displacement curves obtained for the indentation of a purely
elastic isotropic medium are shown in figure 3 for different indenter radii $R$,
box sizes $L$, and surface grid discretization $N_{\text{grid}}$. Elastic constants for Al are
used ($\mu = 26$ GPa, $\nu = 0.3$). The results show that the size of the indenter
radius has a major influence on the response, as predicted by the Hertzian
contact theory. In addition, it is found that the grid resolution $N_{\text{grid}}$ has
little influence on the elastic response overall. More specifically, the effect of
the grid discretization is limited to a small region of low indentation depths
in which the elastic response is not captured with full accuracy depending
on the grid resolution. This is because the spectral solver cannot accurately
model the contact when the grid spacing is on the order of the size of the
contact area. For instance, this region extends to $d \approx 20$nm for $N_{\text{grid}} = 64^2$
and is reduced to $d \approx 3$nm for $N_{\text{grid}} = 128^2$, for an indenter radius of
$R = 0.25\mu$m and box size $L = 5\mu$m. At higher indentation depths, the
force-displacement response is found to be very smooth and follows well the
Hertzian solution. As a result, the surface grid resolution must be chosen
appropriately depending on the indentation regime to be studied.

Here it is also important to note that, for a constant indenter radius $R$,

![](./images/813042432055705600_4.jpg)

(a) $R = 1000b \approx 0.25\mu\text{m}$

![](./images/813042432055705600_5.jpg)

(b) $R = 4000b \approx 1\mu\text{m}$

Figure 3: Force-displacement responses predicted by the spectral formulation for different box lengths $L$ and free-surface grid discretization $N_{\text{grid}}$ for an indenter radius (a) $R = 1000b \approx 0.25\text{nm}$ and (b) $R = 4000b \approx 1\mu\text{m}$.

different half-space surface lengths $L$ (along the $x$ and $y$ directions) lead to slightly different responses. Such a result is a direct consequence of the periodicity inherent to the use of the spectral formulation developed in this work. As a matter of fact, when using the current approach, a periodic array of indenters is prescribed to the half-space surface. Thus, the stress state calculated within the primary volume not only results from the pressure of the indenter acting on the primary surface, but also accounts for the contact with the periodic replica of the indenter. Periodic boundary effects are minimized when the contact region remains sufficiently small compared to the surface length. This behavior is clearly visible when comparing the examples reported in figure 3 with the elastic Hertzian solution $F = \frac{4}{3}E^*R^{1/2}d^{3/2}$ (dashed lines), where $E^* = E/(1 - \nu^2)$. First, it appears that the deviation from the Hertzian theory is lower for the smaller indenter radius $R \approx 0.25\mu\text{m}$, and it increases with the indentation depth, i.e. as the contact area increases. Second, it is observed that the deviation decreases when increasing the length $L$ of the primary surface, i.e. when decreasing the ratio of the contact area to the periodic surface length. In the limit $L \gg R$, the Hertzian solution is recovered (e.g. see results for $L = 25\mu\text{m}$ in figure 3(b)).

### 3.2. Quasi-static analysis of dislocations

#### 3.2.1. Dislocation source during constant depth indentation

In this section, the evolution of a single Frank-Read source is investigated during indentation at constant depth $d = 100b$. The Franck-Read source

has length $l = 2000b$, Burgers vectors $\frac{1}{2}[1\overline{1}0]$, and lies on the (111) slip plane. The source is initially straight, parallel to the [001] free surface at a depth $z_0 = 2000b$, and is inserted at the center of the simulation volume.

Different snapshots of the evolution of the dislocation source are reported in figure 4 when using a parabolic indenter of radius $R = 1000b$. For reference, the resolved shear stress (RSS) induced by the displacement field of the indenter is plotted on the glide plane of the dislocation source. As expected, it is observed that the initially straight dislocation source rapidly activates and expands within the region of maximum RSS. Yet the range of dislocation loops is limited in the domain where the indentation stress field is large.

![](./images/813042432055705600_6.jpg)

Figure 4: Evolution of a Frank-Read source (blue line) placed below an indenter of radius $R = 1000b$ held at constant depth $d = 100b$. The resolved shear stress (RSS) arising from the indentation contact is plotted on the plane of the dislocation for reference.

#### 3.2.2. Effect of the friction stress

As another benchmark, the effect of the friction stress is investigated by studying the position of a prismatic loop during indentation at constant depth $d = 10b$ with a parabolic indenter of radius $R = 1000b$. The prismatic loop has a Burgers vector $\vec{b} = \frac{1}{2}[10\overline{1}]$ and its four arms of length $l = 1000b$ lie on the (111) and $(1\overline{1}1)$ planes. The loop is initially inserted at depth $z_0 = 2000b$ below the contact region in a simulation volume of length $L = 20000b$.

In figure 5(a), the evolution of the loop position (from the free surface) with time is reported for several values of friction stresses. When no friction stress is accounted for ($\tau_{\text{fric}} = 0$ MPa), the prismatic loop rapidly glides away from the free surface as a result of the stress arising from the contact with the indenter. In the case of non-zero friction stresses, the velocity of the loop is reduced as the lattice friction stress increases. For $\tau_{\text{fric}} = 40$ MPa, the prismatic loop is found to be immobile in this setting, as the value of the

indenter stress becomes insufficient to overcome the large lattice resistance.
Another interesting result is provided by the equilibrium position reached by the dislocation loop as a function of the friction stress, as reported in figure 5(b). Since the indenter stress decays as $1/r^2$, the loop eventually stops to an equilibrium position when there exists a lattice friction stress. Alternatively, the loop will indefinitely glide away when no friction stress is accounted for, owing to the long range nature of the indenter stress.

![](./images/813042432055705600_7.jpg)

Figure 5: Effect of the friction stress on the position of a prismatic loop below an indenter of radius $R=1000b$ at a depth $d=10b$: (a) Evolution of dislocation position with time, and (b) Equilibrium position as a function of the friction stress.

### 3.3. Dislocation surface steps

#### 3.3.1. Prismatic loop surface steps
In order to assess the validity of the surface step procedure developed in this work (see Appendix B), the plastic displacement field associated with a prismatic loop escaping the free surface is investigated. To this end, a prismatic loop is introduced in the simulation volume, while the indenter is fixed above the surface ($d>0$) such that no contact is established. The prismatic loop has a Burgers vector $\vec{b}=\frac{1}{2}[011]$ and its four arms of length $l=2000b$ lie on the $(1\overline{1}1)$ and $(11\overline{1})$ planes. The loop is initially inserted at depth $z_0=2000b$ below the $[001]$ free surface in a simulation volume of length $L=20000b$.

Due to the image stress resulting from the traction free boundary condition, the prismatic loop is attracted towards the free surface and eventually escapes the volume. The different steps of this process are illustrated by the snapshots given in figures 6(a)-(d). In these snapshots, it is observed

that surface steps (blue lines) are progressively created as parts of the loop cross the free surface. Once fully escaped, the prismatic loop leaves a closed loop on the surface, whose contour corresponds to the intersection between the glide planes associated with each arm of the loop and the free surface $z=0$. The plastic displacement $u_z^p(x,y)$ corresponding to the surface steps and calculated using the methodology presented in Appendix B is shown in figures 6(d). As properly captured by the current approach, the prismatic loop has created a pit on the surface, whose height equals the magnitude of the Burgers vector projected along the surface normal.

![](./images/813042432055705600_8.jpg)

Figure 6: (a-c) DDD simulation of a prismatic loop attracted to the free surface. Orange and red arms are lying on the $(1\overline{1}1)$ and $(11\overline{1})$ planes, respectively. Surface steps are drawn in blue. (d) After fully escaping the volume, the prismatic loop has left a surface imprint whose contour is delimited by four surface steps inserted throughout the escape process. As expected, the corresponding surface displacement $u_z^p(x,y)$ shows that the prismatic loop has created a pit on the free surface.

### 3.3.2. Effect of surface steps on the mechanical response

In this section, the effect of the formation of surface steps on the mechanical response during a nanoindentation experiment is examined. For this purpose, a loading-unloading indentation cycle is performed on a half-space with $[111]$ surface orientation. To allow for the formation of surface steps, several glissile loops are periodically introduced during the simulation at random locations. An MD-informed nucleation algorithm will be discussed in a future work.

The force-displacement response for this simulation is reported in figure 7(a) (red line), and is compared with a purely elastic simulation in which no dislocation is introduced (blue line). The effect of the presence of dislocations is clearly visible through the deviation of the force-displacement response from the purely elastic reponse. The corresponding dislocation density is shown in figure 7(b) and is seen to substantially increase during

![](./images/813042432055705600_9.jpg)
![](./images/813042432055705600_10.jpg)

![](./images/813042432055705600_11.jpg)
![](./images/813042432055705600_12.jpg)

Figure 7: Effect of surface steps on the mechanical response. (a) Force-displacement responses and (b) dislocation density evolution during a loading/unloading cycle when dislocation loops are introduced (red) or not (blue). (c) Elastic and plastic (surface steps) contributions to the total surface displacement during loading when glissile loops are introduced. (d) A permanent surface imprint is left after unloading.

the loading regime due to the continuous introduction of new loops and their expansion by glide. More specifically, the deviation from the elastic response results from the creation of surface steps whose associated plas- tic displacement help accommodate the total displacement imposed by the indenter, as shown in figure 7(c). After unloading, the residual surface steps leave a permanent surface imprint, see figure 7(d), consistent with experimental observations. Interestingly, it is observed that surface steps are naturally created in the vicinity of the indenter contact region, thereby providing a mechanism to accommodate the elastic displacement imposed by the indenter contact.

### 3.4. Indentation of strain-hardened dislocation structure

In the vast majority of nanoindentation experiments, the indented crystals typically already contain a microstructure, i.e. initial defects are present. This is for instance the case when indentation is performed on strain-hardened metal samples for which one wants to infer the mechanical properties. In this section, an example of a DDD nanoindentation simulation with an initial complex microstructure is presented.

In order to obtain an initial complex dislocation configuration representative of strain-hardened crystals and yet compatible with the half-space setting, the following methodology is adopted. First, a work-hardening DDD simulation is performed to generate a strain-hardened dislocation structure. Since periodic boundary conditions are typically used in all directions in work-hardening simulations to simulate dislocation activity in the bulk, the resulting configuration must then be manipulated to be used within the nanoindentation half-space setting. Specifically, the periodicity must be broken in the $z$-direction and a free surface needs to be introduced at $z=0$. In order to do so, the chopping procedure illustrated in figure 8 and summarized by the following steps has been employed:

- All segments crossing the free surface $z=0$ are splitted and surface nodes are introduced at the intersection with the $z=0$ surface plane
- Nodes lying at the bottom of the simulation volume (at $z\approx z_{\text{min}}$) are pinned and disconnected from their periodic neighbors in the upper half-space $z>0$
- All nodes lying in the upper halfpsace $z>0$ are removed from the simulation volume

In the present example, the initial microstructure is chopped from a strain-hardened DDD structure obtained at $\gamma=0.2\%$ shear strain and rescaled to a $2\times2\times1\mu\text{m}^3$ half-space with a corresponding initial dislocation density of $\rho_0=2\times10^{12}\text{ m}^{-2}$, see figure 9(a). A constant indenter velocity $v_{\text{ind}}=10^{10}\text{ b/s}$ is prescribed on the [001] free surface. During the simulation, the dislocation sources close to the axis of the indenter are rapidly activated on different glide planes and expand in circular loops following the Frank-Read source process, as shown in figure 9(b). The dislocation density dramatically increases during this simulation, reaching $2.5\times10^{13}$ $\text{m}^{-2}$ at indentation depth $d=0.25\mu\text{m}$.

![](./images/813042432055705600_13.jpg)
![](./images/813042432055705600_14.jpg)

Figure 8: Preparation of an initial complex configuration for a DDD nanoindentation simulation: (a) a strain-hardened dislocation structure is extracted from a fully periodic work-hardening simulation and (b) chopped such as to only keep the structure in the lower half-space $z \leq 0$.

Note that this simulation required a total time of approximately 3 days to reach an indentation depth of $d = 0.25\mu\text{m}$ using a single CPU on a desktop computer. It is observed that more than 90% of the wall clock time is spent in the time-integration procedure, i.e. in the sequential calculation of nodal forces calculation until convergence in dislocation motion is achieved. We estimate that the same simulation would have required about a month if the subcycling integrator was not used, thereby rendering 3D nodal DDD simulations of complex nanoindentation processes prohibitively expensive. This simulation also demonstrates the efficiency of the spectral method developed in this work. Here, it accounts for less than 10% of the overall computation time. Alternatively, employing a 3D FEM-based would presumably lead to a significant increase in the cost associated with solving the contact problem, thereby further increasing the computational burden of such a type of simulations.

### 3.5. Elements of comparison between FEM-based and spectral-based approaches

In this section, we attempt to provide some comparison between FEM-based methods and the spectral approach developed in this work in the context of nanoindentation simulations. We first note that establishing a direct comparison is actually a difficult task, specifically because the treatment of the boundary conditions is different in both approaches, as will be detailed in the following. Consequently, the conclusions reported in this section are only meant to be qualitative in nature, while allowing to highlight

![](./images/813042432055705600_15.jpg)

Figure 9: DDD nanoindentation simulation of a $2 \times 2 \times 1 \mu \text{m}^3$ volume with initial complex microstructure. (a) Initial dislocation configuration. Dislocation lines are colored by slip system. (b) Configuration at $d=0.25\mu\text{m}$. (c) Evolution of the dislocation density.

the efficiency of the spectral method.

In an attempt to establish a comparison between both methods, the following procedure was used. First, the spectral contact solver presented in section 2.2.1 was used to determine the contact pressure resulting from forcing an indenter of radius $R=1\mu\text{m}$ at depth $d=100\text{nm}$ at the cen- ter of a cube of length $L=5\mu\text{m}$. (The problem dimensions are consistent with typical parameters used in DDD nanoindentation simulations, e.g. in [9, 10]). The resulting pressure field was then applied as a surface bound- ary condition for both the spectral stress solver and a FEM calculation performed using the commercial software Abaqus. Surface grids with res- olutions ranging from $N_{\text{grid}}=32^2$ to $1024^2$ were considered for the spec- tral solver. Uniform meshes of quadratic elements (C3D20) with resolution $N_{\text{res}}=32^3$ to $64^3$ were used in the FEM calculation, i.e. with total number of elements ranging from 32,768 to 262,144, consistent with typical mesh discretizations reported in the literature (e.g. [9, 10, 24]).

Importantly, the treatment of the boundary conditions outside of the free surfaces differ in two main aspects between both approaches: (i) the bottom of the simulation volume was fixed in the FEM calculation whereas a uniform displacement mode resulting from the average pressure is consid- ered in the spectral solver (see equation (8)), and (ii) no specific boundary conditions were applied to the side surfaces in the FEM simulation while PBC are inherently considered in the spectral approach.

Results for the surface displacement fields are shown in figure 10(a). It is observed that the surface displacements obtained with the FEM for $N_{\text{res}}=64^3$ elements agree very well with the spectral approach results. However, at a lower resolution of $N_{\text{res}}=32^3$ elements, the FEM calculation

is seen to be less accurate, with a maximum relative error of about 5%
at the tip of the indenter. In contrast, the displacement fields obtained
with the spectral approach are nearly indistinguishable for grid resolutions
ranging from $N_{\text{grid}}=32^2$ to $1024^2$ pixels, thereby highlighting the very fast
convergence of the spectral solver.

Results for the $\sigma_{zz}$ stress component plotted on a vertical slice passing
through the axis of the indenter are reported in figure 10(b). The stress
field calculated with the spectral method for a fine surface resolution of
$N_{\text{grid}}=1024^2$ is plotted in subfigure (b1). Because of the absence of an
analytical solution, this stress field, henceforth denoted $\sigma_{zz}^{\text{ref}}$, will serve as a
reference solution for the rest of this section. In subfigures (b2) to (b4), the
logarithm $\log E$ of the absolute error $E=|\sigma_{zz}^{\text{ref}}-\sigma_{zz}|$ is plotted for stress
fields obtained when using (b2) a FEM calculation with $N_{\text{res}}=64^3$ elements,
(b3) the spectral method with a surface grid resolution of $N_{\text{grid}}=64^2$, and
(b4) the spectral method with a surface grid resolution of $N_{\text{grid}}=64^2$ and
the grid interpolation procedure presented in §2.3.2. As expected, it is
observed in all cases that the maximum discrepancy with respect to the
finer reference solution is found at the edge of the contact region. Outside
of the contact region, the error $E$ is seen to be several orders of magnitude
lower than the stress values. We note that the error profile associated with
the FEM calculation in (b2) looks manifestly different than those reported
in (b3)-(b4) for the spectral method. This difference directly results from
the different set of boundary conditions used in both methods. As such,
a direct comparison between the accuracy of both methods is not possible
here. Finally, we note that the error profile reported in (b4) exhibits what
appears to be regular oscillations. These are a direct consequence of the
grid interpolation procedure detailed in §2.3.2. Since the magnitude of these
oscillations is found to be several orders of magnitude lower than the stress
values, the interpolation procedure is not expected to have a significant
effect on dislocation forces calculation.

The convergence of the spectral approach is examined in figure 11(a).
In this figure, the normalized Mean Square Error (MSE) is evaluated as

$$
\text{MSE} = \frac{\underset{i}{\text{mean}} \left\{ \left\| \sigma_{zz}^{\text{ref}}(i) - \sigma_{zz}(i) \right\|^2 \right\}}{\underset{i}{\text{mean}} \left\| \sigma_{zz}^{\text{ref}}(i) \right\|^2} \tag{21}
$$

where $i$ runs over the set of sampling points used to evaluate the stress
field on the slice in figure 10(b). While rapid convergence of the spectral
solver is shown, it is also observed that the use of the grid interpolation

![](./images/813042432055705600_16.jpg)
![](./images/813042432055705600_17.jpg)

Figure 10: Comparison of elastic fields resulting from a contact pressure field imposed on the free surface as computed with the spectral approach and a FEM calculation. (a) Surface displacement field $u_z$ on a line passing through the indenter axis. (b) Stress field on a $xz$-slice passing through the indenter axis. (b1) Reference $\sigma_{zz}$ stress component computed with the spectral approach for $N_{\text{grid}} = 1024^2$. Logarithm of the absolute error $\log E$ when using (b2) a FEM C3D20 mesh of $64^3$ elements, (b3) the spectral method with grid resolution of $64^2$ pixels, (b4) the spectral method with grid resolution of $64^2$ pixels along with the grid interpolation method detailed in §2.3.2.

procedure naturally leads to a loss of accuracy with a convergence rate that decreases towards high resolutions. In addition, although a fair comparison with FEM results is difficult for reasons mentioned earlier, and because it would otherwise require a fine FEM mesh reference solution which would be prohibitively expensive to obtain, it is nevertheless expected that the convergence rate of both approaches is comparable.

Finally, the efficiency of the spectral contact solver is assessed in figure 11(b). In this figure, the computation time as a function of the grid reso- lution is reported for a forward calculation, i.e. for the calculation of the displacement field resulting from the imposed contact pressure for a single iteration of the contact solver. These computations are performed on a 2.67GHz Intel Xeon single CPU and the FFTW library is used. It is seen that the spectral solver requires between $5 \times 10^{-5}$s for $N_{\text{grid}} = 32^2$ to 0.3s for $N_{\text{grid}} = 1024^2$ to complete such a calculation. In contrast, we find that the FEM calculation takes between $7 \times 10^2$s at $N_{\text{res}} = 32^3$ and $4 \times 10^4$s at $N_{\text{res}} = 64^3$ for the same forward calculation using Abaqus. We note here that better performance could certainly be achieved using dedicated and optimized FEM implementations. Nevertheless, these results qualitatively demonstrate the significant efficiency of the spectral approach compared

![](./images/813042432055705600_18.jpg)

Figure 11: (a) Convergence of the $\sigma_{zz}$ stress field in the spectral approach as a function of the surface grid resolution. (b) Wall clock time for a forward pressure-displacement calculation (single iteration) when employing the spectral method.

to FEM implementations. This difference of several orders of magnitude in the computation cost primarily results from the fact the spectral approach only requires a two-dimensional grid to solve the contact problem. Specifically, for a grid of resolution $N_{\text{grid}} = n^2$, the spectral contact solver requires $\mathcal{O}(n^2\log(n^2))$ operations. In comparison, the problem requires a three-dimensional mesh of the volume in the FEM approach. At equivalent resolution, i.e. for a mesh of $N_{\text{res}} \approx n^3$ elements, the FEM therefore requires a significantly higher number of $\mathcal{O}(n^6)$ operations due to its quadratic complexity.

While the cost of the image stress calculation is generally not discussed in DDD nanoindentation studies, the significant burden of the FEM solver in the context of DDD simulations was already pointed out in the literature (e.g. see [24]). In practice, the cost of such a solver is typically alleviated by using local mesh refinements and developing highly scalable parallel FEM implementations [24]. Alternatively, thanks to its high efficiency, the method developed in this work does not require mesh refinements, and allows to nearly eliminate the often predominant computational burden associated with solving the boundary value problem, even when using a single CPU.

## 4. Conclusion

In this paper, we presented a spectral approach to perform three-dimensional DDD simulations of nanoindentation experiments. We first developed an

algorithm to solve for the contact problem in an efficient manner by relying on a two-dimensional Fourier modes decomposition of the contact pressure and of the resulting stress field, which are both conveniently computed using FFTs. With this approach, the image stress arising from the interactions between dislocation segments and the free surface (outside of the contact region) is inherently accounted for. To reduce the computational burden associated with the dramatic dislocation multiplication typically associated with nanoindentation experiments, we further coupled the DDD nanoindentation framework with a recently developed subcycling integrator and devised a procedure to alleviate the computational cost of the displacement field associated with surface steps. As a benchmark, we demonstrated the ability of the method to capture the effects of the surface steps created by escaping dislocations on the mechanical response. Finally, we illustrated the capabilities of the approach by providing an example of a nanoindentation simulation performed on an initially strain-hardened microstructure.

## Acknowledgements

This work is partly supported by the Volkswagen Group (NB, VG and DD) and by the Department of Energy, Office of Basic Energy Science, under project DE-SC0010412 (WC).

## Appendix A. Examples of indenter shapes

The method presented in this work allows for simulating contact between an elastic half-space and an indenter of arbitrary shape. When considering a rigid indenter, its shape is simply prescribed by providing its initial surface profile $u_{\text{ind}}(x,y)$ (height coordinate) at any point along the half-space surface $(x,y)$. Note that this profile only needs to be specified once at the beginning of a simulation.

In this section, an example of the determination of the surface profile $u_{\text{ind}}(x,y)$ is given for two types of indenters, namely the parabolic and the Berkovich indenters.

### Appendix A.1. Parabolic indenter

The geometry of the parabolic indenter is specified by the following shape profile:

$$
u_{\text{ind}}(x,y) = \frac{(x-x_c)^2+(y-y_c)^2}{2R} \tag{A.1}
$$

where $(x_c, y_c)$ denotes the coordinate of the axis of the indenter projected on the surface, and $R$ is the tip radius of the indenter. As illustrated in figure A.12(a), this indenter produces a spherical contact surface near its tip. It can for instance be employed to simulate contact with the tip of a sphero-conical indenter.

![](./images/813042432055705600_19.jpg)

Figure A.12: Example of the discrete geometry $u_{\text{ind}}(x,y)$ for two types of indenters: (a) parabolic indenter and (b) Berkovich indenter truncated at height $h$.

### Appendix A.2. Berkovich indenter

The Berkovich indenter geometry is shown in figure A.12(b). The Berkovich indenter produces a typical triangular contact profile on the surface. The shape profile $u_{\text{ind}}(x,y)$ for a perfect Berkovich indenter can be numerically determined by calculating the intersection between each facet of the Berkovich indenter with a set of planes parallel to the surface at different height $h$.

The Berkovich indenters used in experiments are typically characterized by a blunted tip radius. To capture this feature, Oliver and Pharr [25] have proposed the following expression to describe the contact area $A$ as a function of the penetration depth $h$ of a blunted Berkovich indenter:


$$
A(h)=\sum_{i=0}^{8} C_{i} \cdot h^{2^{1-i}}=C_{0} h^{2}+C_{1} h+C_{2} h^{1 / 2}+\ldots+C_{8} h^{1 / 128} \tag{A.2}
$$

where $\{C_i\}$ is a set of coefficients accounting for the deviation from a perfect Berkovich indenter in the tip region. In [25], the following set of coefficients was obtained by fitting expression (A.2) against experimental indentation results:

$$
\begin{aligned}
C_{0}=24.65, \quad C_{1}=202.7, \quad C_{2}=0.03363 \\
C_{3}=0.9318, \quad C_{4}=0.02827, \quad C_{5}=0.03716 \\
C_{6}=1.763, \quad C_{7}=0.04102, \quad C_{8}=1.881
\end{aligned} \tag{A.3}
$$

The contact area as a function of the indentation depth for these coefficients is reported in figure A.13(a). By calculating the indenter profile using the coefficients given in (A.3), we estimated that the set of coefficients corresponds to a tip radius $R \approx 40$nm, as shown in figure A.13(b). We employ a scaling method to describe a blunted Berkovich of arbitrary tip radius $R$, as illustrated in figures A.13(b).

Numerically, the profile $u_{\text{ind}}(x,y)$ of the blunted Berkovich indenter at location $(x,y)$ is calculated by using a Newton-Raphson method to solve for function $f$, defined as $u_{\text{ind}}(x,y)=f(u_{\text{ind}}^{\text{perfect}}(x,y))$, such that the cross-section $A(h)$ of the blunted indenter given in (A.2) is respected.

## Appendix B. Surface steps implementation

During a DDD simulation, dislocations are free to escape the volume by crossing free surfaces when these are present. In doing so, each dislocation leaves a residual step on the surface, whose height is equal to the dislocation Burgers vector projected along the surface normal. In the context of nanoindentation, these surface steps play a crucial role by providing a plastic mechanism to accommodate the deformation in the contact region. As result, accounting for the surface steps in DDD nanoindentation is critical to appropriately capture the plastic response produced by the indenter load.

Numerically, the implementation of the surface steps proceeds in two stages. First, dislocation lines escaping through the free-surface $z=0$ are detected and specific topological operations are performed to "cut" the

![](./images/813042432055705600_20.jpg)

Figure A.13: (a) Indenter contact area as a function of the indenter height, for the perfect and the blunted Berkovich indenters. (b) Examples of blunted Berkovich indenter profiles (solid lines). Using coefficients given in (A.3), we estimate the reference tip radius at $R=40$nm (red). An example of the profile for $R=100$nm obtained by a simple scaling of the reference profile is shown in green. Fitting circles for the tip radius are shown with dashed lines.

corresponding segments. Since this mechanism is irreversible (dislocations that have escaped no longer exist), the steps created must be stored while their evolution must be tracked during the whole life of the simulation. Second, at each step of the simulation, the surface plastic displacement field $u_z^p(x,y)$ associated with all surface steps is computed and accounted for in solving for the contact problem (see equation (9)).

![](./images/813042432055705600_21.jpg)

Figure B.14: Schematic of the numerical procedure to handle dislocation segment intersection with the free surface and the creation of surface steps. (a) After time-integration of dislocation motion, part of a dislocation may have exited the half-space. (b) A set of topological operations is performed to "cut" dislocation segments that have exited the volume. In this example, nodes 3 and 5 are moved to the surface while segments $3-4$ and $4-5$ are removed from the simulation. Simultaneously, a surface step $3-5$ is created by reconnecting both newly created surface nodes. This surface step will serve to compute the displacement discontinuity left by the portion of the dislocation that escaped the half-space.

of two very long screw dislocations ($l_v \gg l_s$) connected at their ends by two additional edge segments required to close the loop. The displacement field associated with each surface step is then obtained by calculating the displacement field produced by their corresponding virtual loop.

For a closed dislocation loop, the displacement field $\vec{u}$ generated at field point $\vec{x}$ is given by:

$$
u_{i}(\vec{x})=-\frac{b_{i} \Omega}{4 \pi}+\frac{1}{8 \pi} \oint_{C}\left[\epsilon_{i k l} b_{l} R_{, p p}+\frac{1}{1-\nu} \epsilon_{k m n} b_{n} R_{, m i}\right] d l_{k} \tag{B.1}
$$

where $\vec{b}$ is the Burgers vector of the dislocation, $R$ denotes the magnitude the radius vector between the field point and the coordinate spanning the loop contour $C$, and $\Omega$ is the solid angle as viewed from the field point. Here, we employ the method devised in [26] and recently adapted for DDD simulations in [23] to evaluate expression (B.1). In this last approach, an analytical expression for the displacement field (B.1) produced by a triangular dislocation loop is obtained analytically and in a convenient form for numerical evaluation. In order to apply this approach, the virtual loops associated with each surface step are simply divided into four triangular loops, as depicted in figure B.15(a). The overall surface displacement $u_{z}^{p}(x, y)$ is then obtained by summing the contribution associated with each individual surface step.

Note that this approach differs from conventional methods in which the surface displacement field is obtained by summing the displacement associated with each dislocation segment present in the volume (e.g. see [23]). In the virtual loop approximation, the total displacement field is obtained from the surface steps alone, thereby allowing for significant computational savings. The displacement obtained with both methods is expected to differ by a smooth field with limited effect on the mechanical response.

Examples of the resulting displacement fields obtained for two individual surface steps are reported in figures B.15(b)-(c). As expected, when the Burgers vector of the surface step is orthogonal to the surface, e.g. for $\vec{b}=[00 \overline{1}]$, the magnitude of the displacement jump produced across the step is equal to the magnitude Burgers vector. For a step with Burgers vector non-orthogonal to the surface, e.g. $\vec{b}=\frac{1}{\sqrt{2}}[01 \overline{1}]$, the magnitude of the displacement jump equals the magnitude the Burgers vector projected along the $z$-direction. In addition, it is observed that the virtual loop procedure produces a smooth displacement field around the step discontinuity.

$$
\begin{align*}
\hat{u}_{x,x}^{-} &= ik_x \hat{u}_x^{-} & \hat{u}_{y,x}^{-} &= ik_x \hat{u}_y^{-} & \hat{u}_{z,x}^{-} &= ik_x \hat{u}_z^{-} \\
\hat{u}_{x,y}^{-} &= ik_y \hat{u}_x^{-} & \hat{u}_{y,y}^{-} &= ik_y \hat{u}_y^{-} & \hat{u}_{z,y}^{-} &= ik_y \hat{u}_z^{-} \\
\hat{u}_{x,z}^{-} &= Ak_x e^{k_z z} + k_z \hat{u}_x^{-} & \hat{u}_{y,z}^{-} &= Ak_y e^{k_z z} + k_z \hat{u}_y^{-} & \hat{u}_{z,z}^{-} &= -iAk_z e^{k_z z} + k_z \hat{u}_z^{-}
\end{align*}
\tag{C.3}
$$

$$
\hat{u}_{k,k}^{-} = \hat{u}_{x,x}^{-} + \hat{u}_{y,y}^{-} + \hat{u}_{z,z}^{-} = i2Ak_z \frac{\mu}{\lambda + \mu}
\tag{C.4}
$$

Using Hooke's law for an isotropic elastic medium, the stress field is obtained from the displacement field as:

$$
\sigma_{ij} = \lambda u_{k,k}^{-} \delta_{ij} + \mu \left( u_{i,j}^{-} + u_{j,i}^{-} \right)
\tag{C.5}
$$

The stress field can be readily expanded in the Fourier space as:

$$
\sigma(x, y, z) = \sum_{k_x} \sum_{k_y} \begin{bmatrix}
\hat{\sigma}_{xx} & \hat{\sigma}_{xy} & \hat{\sigma}_{xz} \\
\hat{\sigma}_{xy} & \hat{\sigma}_{yy} & \hat{\sigma}_{yz} \\
\hat{\sigma}_{xz} & \hat{\sigma}_{yz} & \hat{\sigma}_{zz}
\end{bmatrix} e^{ik_x x + ik_y y}
\tag{C.6}
$$

where the Fourier components are obtained from equations (C.3), (C.4) and (C.5) as:

$$
\begin{aligned}
\hat{\sigma}_{x x} &=2 \mu \hat{u}_{x, x}^{-}+\lambda\left(\hat{u}_{x, x}^{-}+\hat{u}_{y, y}^{-}+\hat{u}_{z, z}^{-}\right) \\
&=2 \mu\left(i A k_{x}^{2}-i B k_{x} k_{y}-C k_{x}^{2}+i A k_{z} \frac{\lambda}{\lambda+\mu}\right) e^{k_{z} z}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\sigma}_{y y} &=2 \mu \hat{u}_{y, y}^{-}+\lambda\left(\hat{u}_{x, x}^{-}+\hat{u}_{y, y}^{-}+\hat{u}_{z, z}^{-}\right) \\
&=2 \mu\left(i A k_{y}^{2}+i B k_{x} k_{y}-C k_{y}^{2}+i A k_{z} \frac{\lambda}{\lambda+\mu}\right) e^{k_{z} z}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\sigma}_{z z} &=2 \mu \hat{u}_{z, z}^{-}+\lambda\left(\hat{u}_{x, x}^{-}+\hat{u}_{y, y}^{-}+\hat{u}_{z, z}^{-}\right) \\
&=2 \mu\left((-i A z+C) k_{z}^{2}+i A k_{z} \frac{\lambda+2 \mu}{\lambda+\mu}\right) e^{k_{z} z}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\sigma}_{x y} &=\mu\left(\hat{u}_{x, y}^{-}+\hat{u}_{y, x}^{-}\right) \\
&=\mu i\left(2 A k_{x} k_{y} z+B\left(k_{x}^{2}-k_{y}^{2}\right)+2 i C k_{x} k_{y}\right) e^{k_{z} z}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\sigma}_{x z} &=\mu\left(\hat{u}_{x, z}^{-}+\hat{u}_{z, x}^{-}\right) \\
&=\mu\left(\left(2 A k_{x} z-B k_{y}+2 i C k_{x}\right) k_{z}-2 A k_{x} \frac{\mu}{\lambda+\mu}\right) e^{k_{z} z}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\sigma}_{y z} &=\mu\left(\hat{u}_{y, z}^{-}+\hat{u}_{z, y}^{-}\right) \\
&=\mu\left(\left(2 A k_{y} z+B k_{x}+2 i C k_{y}\right) k_{z}-2 A k_{y} \frac{\mu}{\lambda+\mu}\right) e^{k_{z} z}
\end{aligned} \tag{C.7}
$$

The traction field produced on free surface $z=0$ is obtained from equation (C.6) as:

$$
\vec{T}(x, y)=\sum_{k_{x}} \sum_{k_{y}}\left(\begin{array}{c}
\hat{T}_{x} \\
\hat{T}_{y} \\
\hat{T}_{z}
\end{array}\right) e^{i k_{x} x+i k_{y} y} \tag{C.8}
$$

The Fourier coefficients $\hat{T}_{x}, \hat{T}_{y}, \hat{T}_{z}$ are related to the coefficients $A, B, C$ through the matrix $M$ as:

$$
\left(\begin{array}{c}
\hat{T}_{x} \\
\hat{T}_{y} \\
\hat{T}_{z}
\end{array}\right)=\left(\begin{array}{c}
\hat{\sigma}_{x z}(z=0) \\
\hat{\sigma}_{y z}(z=0) \\
\hat{\sigma}_{z z}(z=0)
\end{array}\right)=[M]\left(\begin{array}{c}
A \\
B \\
C
\end{array}\right) \tag{C.9}
$$

where $M$ is obtained from relations (C.7) as:

$$
M = \begin{bmatrix}
-\frac{2\mu^2}{\lambda+\mu}k_x & -\mu k_y k_z & 2i\mu k_x k_z \\
-\frac{2\mu^2}{\lambda+\mu}k_y & \mu k_x k_z & 2i\mu k_y k_z \\
i\frac{2\mu(\lambda+2\mu)}{\lambda+\mu}k_z & 0 & 2\mu k_z^2
\end{bmatrix} \tag{C.10}
$$

Note that matrix $M$ in equation (C.10) is consistent with matrix $M^-$ provided in [11] for the negative half-space, with a typographical correction in component $M_{23}$.

## References

[1] W. D. Nix, H. Gao, Indentation size effects in crystalline materials: A law for strain gradient plasticity, Journal of the Mechanics and Physics of Solids 46 (3) (1998) 411 – 425.

[2] N. Fleck, J. Hutchinson, Strain gradient plasticity, Advances in Applied Mechanics 33 (1997) 295 – 361.

[3] H. G. M. Kreuzer, R. Pippan, Discrete dislocation simulation of nanoindentation, Computational Mechanics 33 (4) (2004) 292–298.

[4] A. Widjaja, E. V. der Giessen, A. Needleman, Discrete dislocation modelling of submicron indentation, Materials Science and Engineering: A 400 (2005) 456 – 459.

[5] D. Balint, V. Deshpande, A. Needleman, E. V. der Giessen, Discrete dislocation plasticity analysis of the wedge indentation of films, Journal of the Mechanics and Physics of Solids 54 (11) (2006) 2281 – 2303.

[6] Y. Zhang, Y. Gao, L. Nicola, Lattice rotation caused by wedge indentation of a single crystal: Dislocation dynamics compared to crystal plasticity simulations, Journal of the Mechanics and Physics of Solids 68 (2014) 267 – 279.

[7] M. Fivel, C. Robertson, G. Canova, L. Boulanger, Three-dimensional modeling of indent-induced plastic zone at a mesoscale, Acta Materialia 46 (17) (1998) 6183 – 6194.

[8] H.-J. Chang, M. Fivel, D. Rodney, M. Verdier, Multiscale modelling of indentation in fcc metals: From atomic to continuum, Comptes Rendus Physique 11 (3-4) (2010) 285-292.

[9] J. Gagel, D. Weygand, P. Gumbsch, Formation of extended prismatic dislocation structures under indentation, Acta Materialia 111 (2016) 399 – 406.

[10] J. C. Crone, L. B. Munday, J. J. Ramsey, J. Knap, Modeling the effect of dislocation density on the strength statistics in nanoindentation, Modelling and Simulation in Materials Science and Engineering 26 (1) (2018) 015009.

[11] C. R. Weinberger, S. Aubry, S. W. Lee, W. D. Nix, W. Cai, Modelling dislocations in a free-standing thin film, Modelling and Simulation in Materials Science and Engineering 17 (7).

[12] E. Van der Giessen, A. Needleman, Discrete dislocation plasticity: a simple planar model, Modelling and Simulation in Materials Science and Engineering 3 (5) (1995) 689.

[13] B. Devincre, L. P. Kubin, Mesoscopic simulations of dislocations and plasticity, Materials Science and Engineering a-Structural Materials Properties Microstructure and Processing 234 (1997) 8-14.

[14] H. M. Zbib, M. Rhee, J. P. Hirth, On plastic deformation and the dynamics of 3d dislocations, International Journal of Mechanical Sciences 40 (2-3) (1998) 113-127.

[15] D. Weygand, L. H. Friedman, E. Van der Giessen, A. Needleman, Aspects of boundary-value problem solutions with three-dimensional dislocation dynamics, Modelling and Simulation in Materials Science and Engineering 10 (4) (2002) 437-468.

[16] A. Arsenlis, W. Cai, M. Tang, M. Rhee, T. Oppelstrup, G. Hommes, T. G. Pierce, V. V. Bulatov, Enabling strain hardening simulations with dislocation dynamics, Modelling and Simulation in Materials Science and Engineering 15 (6) (2007) 553-595.

[17] J. Mackerle, Finite element and boundary element simulations of indentation problems: A bibliography (19972000), Finite Elements in Analysis and Design 37 (10) (2001) 811 - 819.

[18] J. Boussinesq, Applications des potentiels à l'étude de l'équilibre et du mouvement des solides élastiques, Gauthier-Villars, Paris, 1885.

[19] H. Stanley, T. Kato, An fft-based method for rough surface contact, Journal Of Tribology 119 (1997) 481-485.

[20] J. R. Barber, Elasticity 2nd edn, Dordrecht: Kluwer, 1982.

[21] ParaDiS.
URL http://paradis.stanford.edu

[22] R. B. Sills, A. Aghaei, W. Cai, Advanced time integration algorithms for dislocation dynamics simulations of work hardening, Modelling and Simulation in Materials Science and Engineering 24 (4) (2016) 045019.

[23] M. Fivel, C. Depres, An easy implementation of displacement calculations in 3d discrete dislocation dynamics codes, Philosophical Magazine 94 (28) (2014) 3206-3214.

[24] J. C. Crone, P. W. Chung, K. W. Leiter, J. Knap, S. Aubry, G. Hommes, A. Arsenlis, A multiply parallel implementation of finite element-based discrete dislocation dynamics for arbitrary geometries, Modelling and Simulation in Materials Science and Engineering 22 (3) (2014) 035014.

[25] W. C. Oliver, G. M. Pharr, Measurement of hardness and elastic modulus by instrumented indentation: Advances in understanding and refinements to methodology, Journal of materials research 19 (01) (2004) 3-20.

[26] D. M. Barnett, The displacement field of a triangular dislocation loop, Philosophical Magazine A 51 (3) (1985) 383-387.

38