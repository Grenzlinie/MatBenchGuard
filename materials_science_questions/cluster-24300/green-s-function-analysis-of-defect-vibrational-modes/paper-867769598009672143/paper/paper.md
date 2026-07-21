# Dynamic Green's functions in discrete flexural systems

K. H. MADINE AND D. J. COLQUITT

Department of Mathematical Sciences, University of Liverpool, L69 7ZL, UK

## Abstract
The paper presents an analysis of the dynamic behaviour of discrete flexural systems composed of Euler-Bernoulli beams. The canonical object of study is the discrete Green's function, from which information regarding the dynamic response of the lattice under point loading by forces and moments can be obtained. Special attention is devoted to the interaction between flexural and torsional waves in a square lattice of Euler-Bernoulli beams, which is shown to yield a range of novel effects, including extreme dynamic anisotropy, non-reciprocity, wave-guiding, filtering, and the ability to create localised defect modes, all without the need for additional resonant elements or interfaces. The analytical study is complimented by numerical computations and finite element simulations, both of which are used to illustrate the effects predicted. A general algorithm is provided for constructing Green's functions as well as defect modes. This algorithm allows the tuning of the lattice to produce pass bands, band gaps, resonant modes, wave-guides, and defect modes, over any desired frequency range.

## 1 Introduction
In recent years, the study of lattice dynamics has undergone something of a renaissance due, in part, to the counter-intuitive effects associated with metamaterials, such as perfect lenses [1], negative refractive index materials [2], and invisibility cloaks [3]. The majority of scholarly work in this area has focused on photonic, plasmonic, and acoustic metamaterials, whilst the science of mechanical metamaterials attracts less attention. Nevertheless, elastic metamaterials have found applications a wide array of settings, from cloaking to energy dissipation in engineering structures and seismic protection, among many others [4-11].

Much of the work on metamaterials is underpinned by the study of wave propagation in periodic media, which has been studied in various forms for centuries and remains an active area of research today [12-14]. Dynamic vector systems corresponding to multi-scale mechanical materials offer unique opportunities to study the flexural and rotational displacements that occur in elastic lattice systems [15-22]. Devices that combine, for example, beams and plates with additional resonating structures have been used to produce novel effects associated with bending and rotation, leading to phononic properties not typically found in optical or plasmonic materials, such as uni-directional wave modes, allowing the transmission and localisation of energy [18, 23-27]. The Green's function is the canonical object of study for many problems associated with wave propagation in structured solids as it contains all the fundamental information (such as the dispersive properties) corresponding to the dynamic response of the system. There is a substantial amount of literature on Green's functions, particularly for scalar systems, such as the wide variety of topologies
1

and wave propagation modes (free and forced) studied on mass-spring lattices, [19, 28-30]. Green's functions afford the means to control wave propagation and analyse defects that occur in lattice systems [16, 31]. A method for the localisation of energy in scalar lattices was provided in [32], where the Green's function was used to customise evanescent defect modes that coincide with localised band gap modes.

Considering lattices of beams, various studies have explored systems of Rayleigh beams, including different topologies, the effects of rotational inertia, and the propagation of both in-plane and out-of-plane vibrations [33-36]. Forcing in the form of applied moments is uncommon in flexural systems, but has been shown to produce interesting wave patterns with varying degrees of anisotropy [35].

Lattices of Euler-Bernoulli beams have been the subject of studies focusing on many different facets, including their topology and propagation modes, and have been combined with additional resonators to produce interesting phenomena that can be used as wave guides [19, 20, 36-38]. One such example [34] demonstrated how the interface between a half-plane of Euler-Bernoulli beams, and a half-plane of Rayleigh beams can produce nega- tive refraction for incoming lattice waves. Another example [18] combined a periodic array of Euler-Bernoulli beams on a plate with gyroscopic resonators, leading to 'chiral flexural waves' and one way edge waves at the chiral interface. Unlike lattices of Rayleigh beams, rotational inertia is usually neglected on lattices of Euler-Bernoulli beams as standard. In this study, we explore the effect of rotational inertia and torsional stiffness in lattices of Euler-Bernoulli beams with remarkable results. We emphasise that torsional interactions are often neglected when studying flexural systems insofaras the two are treated indepen- dently. However, we show that properly accounting for the interaction between these flexural and torsional effects leads to unprecedented levels of control over the dispersive properties of the lattice. Alongside these observations, we also compare the different waveforms gener- ated in the lattices from applied forcing, versus applied moments and show that with applied moments, the lattice can act as a wave guide without the need for additional resonators or interfaces.

The structure of the paper is as follows: firstly, in § 2 we construct a class of Green's functions for a 2D square lattice of Euler-Bernoulli beams, where the nodes have mass and rotational inertia and the beams possess torsional stiffness. In § 2.4, we use applied forces and moments to induce dynamic anisotropy, including unusual asymmetric propagative (non- reciprocal) modes. In § 2.5 we show that altering the magnitude of the rotational inertia and torsional stiffness provides a range of possible (and significantly different) dispersion diagrams. In § 3 we study the related problem of a 1D chain of Euler-Bernoulli beams with nodes that possess rotational inertia, and show that the absence of torsional interactions allows us to evaluate the full class of Green's functions for the chain in closed form. Lastly, in § 4 we generalise the approach used in the previous sections to provide a method for constructing Green's functions on discrete lattices of any dimension, with lattice connections that take any form, and then go on to derive custom localised defect modes.

In this study, the control we demonstrate over the direction of wave propagation lays the foundation for designing metamaterials of Euler-Bernoulli beams that have tailor-engineered properties.

## 2 A square lattice of Euler-Bernoulli beams

In this section we consider an infinite square lattice of thin Euler-Bernoulli beams with junctions possessing both mass and rotational inertia. The beams have both flexural rigidity and torsional stiffness, meaning that the torsional rotation and flexural displacement at the junctions are coupled. In particular, whilst the flexural displacement and rotation within a beam are coupled, the torsional rotation is decoupled within the beam itself. At the junctions, however, the flexural rotation in a beam will induce a torsional rotation in the perpendicular beams, coupling the two classes of waves. This coupling of flexural and

torsional interactions is often overlooked in flexural systems but, as will be shown later (§ 2.4), properly accounting for these interactions leads to novel and interesting effects. In Figure 1, the eigenmodes of the lattice are illustrated using a finite element model of the lattice unit cell.

![](./images/867769598009672143_1.jpg)

**Figure 1:** The eigenmodes of the lattice unit cell, illustrating how out-of-plane flexural deformations couple with torsional displacements at the junctions.

We construct the lattice in the $xy$-plane and therefore define the out-of-plane translational motion along the $z$-axis. For convenience, we choose the mass of the nodes, the length of the beams and the flexural rigidity as natural units. Each lattice node is labelled by the double-index $(m,n) \in \mathbb{Z}^2$, such that $\mathbf{0}$ denotes the node located at $(x,y)=(0,0)$. We introduce the generalised displacement vector $\boldsymbol{u}_{(m,n)} = [w(m,n),\theta_x(m,n),\theta_y(m,n)]^\mathrm{T}$ to describe the displacement and rotation of each node. The first component of $\boldsymbol{u}_{(m,n)}$ describes the translation $w(m,n)$ of the $(m,n)^\mathrm{th}$ node, while the second and third components, $\theta_x(m,n)$ and $\theta_y(m,n)$, characterise the rotational displacement of the nodes around the respective coordinate axes, as indicated in Figure 2b.

![](./images/867769598009672143_2.jpg)

**Figure 2:** (a) The Euler–Bernoulli beam lattice geometry, with (b) the corresponding coordinate axes and displacements.

The four beams connected at the node $(m,n)$ are denoted by $X^+$, $X^-$, $Y^+$ and $Y^-$ corresponding to the axes on which the beams lie. Hence, the beam spanning $m \leq x \leq m+1$ is denoted $X^+$ and so forth, as shown in Figure 2a. The out-of-plane flexural deformation $w(x,y)$ of the lattice links is governed by the fourth order differential equation for Euler–Bernoulli beams,

$$
\frac{\partial^4 w}{\partial x^4}=0, \text{ on } X^\pm \quad \text{and} \quad \frac{\partial^4 w}{\partial y^4}=0, \text{ on } Y^\pm. \tag{2.1}
$$

The first-order spatial derivatives $w_{,x}(x,y)$, $w_{,y}(x,y)$, give the angles of flexural rotation, about the $x$- and $y$-axes respectively, associated with the flexural deformation; here subscript letters proceeded by commas indicate partial derivatives with respect to the relevant spatial variables. We define $\tau_x(x,y)$ as the torsion angle that the $X^\pm$ beams experiences about the

$x$-axis, and likewise for $\tau_y(x,y)$ about the $y$-axis. The torsion angles each satisfy

$$
\frac{\partial^{2} \tau_{x}}{\partial x^{2}}=0 \quad \text { and } \quad \frac{\partial^{2} \tau_{y}}{\partial y^{2}}=0. \tag{2.2}
$$

To construct the equation of motion, we first consider the forces and bending moments that the $X^{\pm}$ beams apply to the node $(m,n)$. From equations (2.1) and (2.2), we see that the flexural deformation and torsion angles are cubic and linear polynomials respectively. The coefficients of these polynomials are found by imposing boundary conditions at the ends of the $X^{\pm}$ beams; we use the following constants,

$$
\begin{align*}
w(m-1,n) &= W_1 & w(m,n) &= W_0 & w(m+1,n) &= W_1 \\
w_{,x}(m-1,n) &= \Theta^{(1)}_y & w_{,x}(m,n) &= \Theta^{(0)}_y & w_{,x}(m+1,n) &= \Theta^{(1)}_y \\
\tau_x(m-1,n) &= -\Theta^{(1)}_x & \tau_x(m,n) &= -\Theta^{(0)}_x & \tau_x(m+1,n) &= -\Theta^{(1)}_x.
\end{align*}
$$

Careful attention is required when considering the directions of the flexural moments and torsional moments around the in-plane coordinate axes, shown in Figure 2b. We stipulate that positive $\Theta_x$ refers to an anticlockwise angle around the $x$-axis, and likewise for the $y$-axis. Using the boundary conditions, we arrive at expressions for the flexural displacement of the $X^+$ beam

$$
w(x,n)_{X^{+}}=\left(\Theta_{y}^{(1)}-2 W_{1}+\Theta_{y}^{(0)}+2 W_{0}\right) x^{3}+\left(3 W_{1}-\Theta_{y}^{(1)}-2 \Theta_{y}^{(0)}-3 W_{0}\right) x^{2}+\Theta_{y}^{(0)} x+W_{0}, \tag{2.3}
$$

and the torsion angle of the $X^+$ beam

$$
\tau_{x}(x, n)_{X^{+}}=\left(\Theta_{x}^{(0)}-\Theta_{x}^{(1)}\right) x+\Theta_{x}^{(0)}. \tag{2.4}
$$

We also find the equivalent expressions for the $X^-$ beam, $w(x,n)_{X^-}$ and $\tau_x(x,n)_{X^-}$.

The shear force, the flexural bending moment and the torsional moment induced in the $X^{\pm}$ beams are

$$
F(x, n)=-\frac{\partial^{3} w}{\partial x^{3}}, \quad M_{f l e x}(x, n)=\frac{\partial^{2} w}{\partial x^{2}} \quad \text { and } \quad M_{t o r s}(x, n)=-C \frac{\partial \tau_{x}}{\partial x}, \tag{2.5}
$$

respectively, where $C$ in $M_{tors}$ is the non-dimensionalised torsional stiffness coefficient and the negative sign corresponds to the direction of the moment about the $x$-axis [39]. The forces and moments that a beam applies to the node $(m,n)$ can be expressed in terms of the generalised forcing vector $\mathbb{F}_{(m,n)} = [F(m,n), \Phi_x(m,n), \Phi_y(m,n)]^\text{T}$; where the moments $\Phi_x(m,n)$ and $\Phi_y(m,n)$ describe the total bending moment about their respective axes at node $(m,n)$, and so each contains both flexural moments $M_{flex}$ and torsion $M_{tors}$. As such, the forces and moments that the $X^{\pm}$ beams apply to the node $(m,n)$ are

$$
\begin{align*}
\begin{bmatrix}
F(m,n) \\
\Phi_x(m,n) \\
\Phi_y(m,n)
\end{bmatrix}_{(X^+)} &= \begin{bmatrix}
-12 & 0 & -6 \\
0 & -C & 0 \\
-6 & 0 & -4
\end{bmatrix}_{(A)} \begin{bmatrix}
W_0 \\
\Theta^{(0)}_x \\
\Theta^{(0)}_y
\end{bmatrix} + \begin{bmatrix}
12 & 0 & -6 \\
0 & C & 0 \\
6 & 0 & -2
\end{bmatrix}_{(B)} \begin{bmatrix}
W_1 \\
\Theta^{(1)}_x \\
\Theta^{(1)}_y
\end{bmatrix} ; \\
\begin{bmatrix}
F(m,n) \\
\Phi_x(m,n) \\
\Phi_y(m,n)
\end{bmatrix}_{(X^-)} &= \begin{bmatrix}
-12 & 0 & 6 \\
0 & -C & 0 \\
6 & 0 & -4
\end{bmatrix}_{(A)} \begin{bmatrix}
W_0 \\
\Theta^{(0)}_x \\
\Theta^{(0)}_y
\end{bmatrix} + \begin{bmatrix}
12 & 0 & 6 \\
0 & C & 0 \\
-6 & 0 & -2
\end{bmatrix}_{(B)} \begin{bmatrix}
W_1 \\
\Theta^{(1)}_x \\
\Theta^{(1)}_y
\end{bmatrix} ;
\end{align*} \tag{2.6}
$$

and we label the matrices for each beam $X^+_A$ and $X^+_B$, $X^-_A$ and $X^-_B$, as indicated in equation (2.6).

Following the same method, we apply boundary conditions to the ends of the $Y^{\pm}$ beams; since flexion in the $X^{\pm}$ beams induces torsion in the $Y^{\pm}$ beams, this is reflected in the continuity condition at $(m,n)$ such that $w_{,x}(m,n)=\Theta_{y}^{(0)}=\tau_{y}(m,n)$ and $w_{,y}(m,n)=-\Theta_{x}^{(0)}=$

$\tau_x(m,n)$. Using the boundary conditions, the polynomials for the flexural displacement $w(m,y)_{Y^\pm}$ and torsion angles $\tau_y(m,y)_{Y^\pm}$ associated with the $Y^\pm$ beams are found. The forces and bending moments that the $Y^\pm$ beams apply to the node $(m,n)$ are then found using the $y$-axis equivalent expressions to equation (2.5). In parallel with equation (2.6), we express the forces and moments from the $Y^\pm$ beams as vectors, and we label the corresponding matrices $Y_A^+$ and $Y_B^+$, $Y_A^-$ and $Y_B^-$.

Combining the forces and moments in both the $x$- and $y$-directions with Newton's second law for a time-harmonic system, the equation of motion of the $(m,n)^\text{th}$ node is then

$$
\begin{aligned}
-\omega^2 \mathrm{M} \boldsymbol{u}_{(m,n)} = &\left[X_A^+ + Y_A^+ + X_A^- + Y_A^-\right] \boldsymbol{u}_{(m,n)} \\
&+ X_B^+ \boldsymbol{u}_{(m+1,n)} + Y_B^+ \boldsymbol{u}_{(m,n+1)} + X_B^- \boldsymbol{u}_{(m-1,n)} + Y_B^- \boldsymbol{u}_{(m,n-1)}, \quad (2.7)
\end{aligned}
$$

where $\boldsymbol{u}_{(m,n)}$ is again the generalised displacement vector of the node $(m,n)$ and the $3 \times 3$ matrix $\mathrm{M} = \mathrm{diag}[1, \mu, \mu]$ describes the inertial properties of the lattice. The first component of M corresponds to the (unit) mass of the junction associated with the translational inertia, whilst the second and third components correspond to the rotational inertia associated with the flexural and torsional deformations, which we denote $\mu$. We apply the discrete Fourier transformation

$$
\boldsymbol{u}^F(k_1, k_2) = \sum_{(m,n) \in \mathbb{Z}^2} \mathrm{e}^{-\mathrm{i}k_1 m} \mathrm{e}^{-\mathrm{i}k_2 n} \boldsymbol{u}_{(m,n)}, \tag{2.8}
$$

to equation (2.7), where $\boldsymbol{u}^F(k_1, k_2) = \left[W^F(k_1, k_2), \Theta_x^F(k_1, k_2), \Theta_y^F(k_1, k_2)\right]^\mathrm{T}$ is the generalised displacement in reciprocal space in terms of the spectral parameters $k_1$ and $k_2$. Following the Fourier transformation, we arrive at the lattice's equation of motion in reciprocal space,

$$
\begin{aligned}
0 = \bigg[\omega^2 \mathrm{M} + X_A^+ + Y_A^+ + X_A^- + Y_A^- &+ \mathrm{e}^{\mathrm{i}k_1} X_B^+ + \mathrm{e}^{\mathrm{i}k_2} Y_B^+ \\
&+ \mathrm{e}^{-\mathrm{i}k_1} X_B^- + \mathrm{e}^{-\mathrm{i}k_2} Y_B^- \bigg] \boldsymbol{u}^F(k_1, k_2). \quad (2.9)
\end{aligned}
$$

As such, the three components of $\boldsymbol{u}^F(k_1, k_2)$ are defined as the Fourier transformed real space displacements $w(m,n)$, $\theta_x(m,n)$ and $\theta_y(m,n)$, respectively.

### 2.1 The dispersion equation
The dispersion equation $\sigma(\omega, k_1, k_2) = 0$ arises from the solvability condition of equation (2.9), where

$$
\begin{aligned}
\sigma(\omega, k_1, k_2) = 144 \sin^2(k_1) &\zeta(k_1, k_2) + 144 \sin^2(k_2) \zeta(k_2, k_1) \\
&+ \left(24 \cos(k_2) + 24 \cos(k_1) + \omega^2 - 48\right) \zeta(k_1, k_2) \zeta(k_2, k_1), \quad (2.10)
\end{aligned}
$$

and we define the repeated function

$$
\zeta(P, Q) = \left(-2C \cos(P) + 2C + 4 \cos(Q) - \mu \omega^2 + 8\right). \tag{2.11}
$$

As one would expect for a symmetric square lattice, the dispersion equation is symmetric in the spectral parameters $k_1$ and $k_2$. We also see that the dispersion equation is cubic in $\omega^2$ and therefore, closed form solutions can be found but are omitted here for brevity. In addition to the frequency and spectral parameters, $\sigma(\omega, k_1, k_2)$ is dependent on the material constants $\mu$ and $C$, which describe the non-dimensionalised rotational inertia and torsional stiffness, respectively. In $\S$ 2.5 we investigate the effects of changing $\mu$ and $C$ on the dispersion equation and show that it is possible to produce completely different dispersion diagrams, with and without the existence of a finite band gap. This control over the lattice's propagating frequencies (with their preferential directions and subsequent anisotropy)


![](./images/867769598009672143_3.jpg)

Figure 3: The dispersion diagram for the Euler-Bernoulli beam lattice across the Brillouin zone $(k_1,k_2)\in[-\pi,\pi]^2$, for the values of $\mu=0.01$, $C=0.1$.

is a particularly interesting feature that provides applications for metamaterials designed to control the propagation of waves in structures.

In Figure 3, we plot the solutions to $\sigma(\omega,k_1,k_2)=0$ for the illustrative values of $\mu=0.01$ and $C=0.1$. It is shown that these values of rotational inertia and torsional stiffness produce a dispersion diagram with two distinct pass bands and two band gaps, one finite and also the semi-infinite band gap associated with discrete systems. Given that the closed form solutions to the dispersion equation are in-hand, we can determine the exact limits of the band gaps for any desired $\mu$ and $C$.

### 2.2 Constructing the Green's function
A notable feature of the flexural lattice is the ability to induce translational displacements, rotational moments and combinations thereof. To construct the Green's function, we con- sider the application of time-harmonic unit forces and unit moments to the central node of the lattice through the forcing vector $\boldsymbol{f}\in\mathbb{C}^3$. In parallel with the components of $\mathbb{F}_{(m,n)}$, the forcing vector $\boldsymbol{f}=[f_w,f_{\theta_x},f_{\theta_y}]^\mathrm{T}$ has components corresponding to the application of translational force $f_w$ out-of-plane (along the $z$-axis) and two moments $f_{\theta_x}$ and $f_{\theta_y}$ about the $x$- and $y$-axes respectively. For any chosen frequency, there are seven different forcing configurations. These modes are generated by the permutations of $f_w,f_{\theta_x},f_{\theta_y}\in\{0,-1\}$ with the exclusion of $f_w=f_{\theta_x}=f_{\theta_y}=0$ corresponding to the absence of any applied forces or moments. We express the Green's function in reciprocal space in the form

$$
\begin{aligned}
\boldsymbol{u}^F(k_1,k_2)=\bigg[\omega^2\mathsf{M}+X_A^++Y_A^++X_A^-+Y_A^-\\
\quad+\mathrm{e}^{\mathrm{i}k_1}X_B^++\mathrm{e}^{\mathrm{i}k_2}Y_B^++\mathrm{e}^{-\mathrm{i}k_1}X_B^-+\mathrm{e}^{-\mathrm{i}k_2}Y_B^-\bigg]^{-1}\boldsymbol{f}.\quad(2.12)
\end{aligned}
$$

The inverse of the discrete Fourier transform is then applied to equation (2.12) to find the Green's function in real space, $\boldsymbol{u}_{(m,n)}$. The resulting components of $\boldsymbol{u}_{(m,n)}$ are written in terms of Fourier integrals and, whilst useful, are cumbersome. Therefore, in the interests of brevity and clarity of presentation, we will restrict ourselves to consideration of the flexural displacement component $W^F(k_1,k_2)$ of the Green's function $\boldsymbol{u}^F(k_1,k_2)$ for an arbitrary

applied forcing. In this case, the spectral form of the flexural displacement is,

$$
\begin{aligned}
W^{F}\left(k_{1}, k_{2}\right)=\frac{\zeta\left(k_{1}, k_{2}\right) \zeta\left(k_{2}, k_{1}\right) f_{w}}{\sigma\left(\omega, k_{1}, k_{2}\right)} &+\frac{12 \mathrm{i} \sin \left(k_{2}\right) \zeta\left(k_{2}, k_{1}\right) f_{\theta_{x}}}{\sigma\left(\omega, k_{1}, k_{2}\right)} \\
&-\frac{12 \mathrm{i} \sin \left(k_{1}\right) \zeta\left(k_{1}, k_{2}\right) f_{\theta_{y}}}{\sigma\left(\omega, k_{1}, k_{2}\right)}, \quad(2.13)
\end{aligned}
$$

where the functions $\sigma$ and $\zeta$ are given in equations (2.10) and (2.11) respectively. The difference of sign for the coefficients of $f_{\theta_{x}}$ and $f_{\theta_{y}}$ in equation (2.13) is a consequence of the sign convention adopted for shear forces and moments in equation (2.5). As expected for a symmetric lattice, the coefficient of the linear force $f_{w}$ is symmetric in the two spectral parameters. We also note that the denominator of equation (2.13) coincides with the dispersion equation, which arises from the inverted operator matrix in equation (2.12).

The inverse Fourier transformation is applied to find the displacement in real space as follows,

$$
w(m, n)=\frac{1}{4 \pi^{2}} \int_{-\pi}^{\pi} \int_{-\pi}^{\pi} W^{F}\left(k_{1}, k_{2}\right) \mathrm{e}^{\mathrm{i} k_{1} m} \mathrm{e}^{\mathrm{i} k_{2} n} \mathrm{~d} k_{1} \mathrm{~d} k_{2}.
\tag{2.14}
$$

Although explicit closed form representations do not exist in general, the integral form of the Green's function is amenable to numerical evaluation. In the following sections, we use numerical evaluation and finite element models to explore the effects of changing the forcing vector, and also the frequency with which the force is applied.

### 2.3 Anisotropic behaviour of localised modes

For a lattice with $\mu=0.01$ and $C=0.1$, consistent with the dispersion diagram in Figure 3, the lower boundary of the finite band gap is $\omega=4 \sqrt{6}$. Using equation (2.14), the flexural displacement band gap Green's functions of the lattice nodes, $w(m, n)$ is evaluated numerically for three examples of the seven forcing options, with each localised mode demonstrating a unique shape. Across each example in Figure 4, we chose the frequency of excitation to be $\omega=9.8$, such that it lies in the band gap, close to the band-edge; this demonstrates the rapid rate of decay and high degree of localisation associated with band gap Green's function in this regime.

Firstly, we consider out-of-plane forcing $\boldsymbol{f}=[-1,0,0]^{\mathrm{T}}$ and plot the flexural displacement in Figures 4a and 4b. In Figure 4a, the decay envelope of the displacement is clear, while Figure 4b displays the periodic oscillation of the nodes and the symmetry between the $x$- and $y$-directions. In mechanical lattices the preferential direction of wave propagation is most commonly seen along the principle axes of the lattice. Here, the localised mode is radially symmetric leading to isotropic behaviour which can be understood from the complex solutions $\left(k_{1}, k_{2}\right) \in \mathbb{C}^{2}$ to the dispersion equation, leading to a uniform decay rate in all directions.

When $\boldsymbol{f}=[0,-1,0]^{\mathrm{T}}$, a clockwise moment is induced about the $x$-axis at the $\mathbf{0}$ node; for this applied moment, the flexural displacement of the lattice nodes has been plotted in Figures 4c and 4d. While the displacement is localised radially, the displacement is not localised to the $y$-axis as one might expect for this type of forcing, this is again due to the complex solutions of the dispersion equation in this regime, meaning the mode has no preferential direction of travel. This is in particular comparison to Figure 5b where, for the same applied moment at a pass band frequency, the displacement field of the propagating mode is highly localised along the $y$-axis. In Figure 4d, we have indicated the dotted line $(m, 0)$ (the $x$-axis) where the lattice nodes do not have out-of-plane displacement but do experience rotational displacement, as expected with this type of forcing. We note that a moment applied about the $y$-axis $\boldsymbol{f}=[0,0,-1]^{\mathrm{T}}$ produces the same out-of-plane displacement in the lattice under a $\pi / 2$ rotation about the $z$-axis.


![](./images/867769598009672143_4.jpg)

![](./images/867769598009672143_5.jpg)

![](./images/867769598009672143_6.jpg)

![](./images/867769598009672143_7.jpg)

![](./images/867769598009672143_8.jpg)

![](./images/867769598009672143_9.jpg)

**Figure 4:** For a square lattice of Euler-Bernoulli beams, where $\mu = 0.01$, $C = 0.1$, the flexural displacement $w(m,n)$ of the nodes is plotted due to forcing $\boldsymbol{f}$ at $\boldsymbol{0}$ for $\omega = 9.8$. For $\boldsymbol{f} = [-1,0,0]^\mathrm{T}$, the lattice is viewed down the $x$-axis (a), and down the positive $z$-axis (b). The forcing $\boldsymbol{f} = [0,-1,0]^\mathrm{T}$ is demonstrated in (c) and (d); while the forcing $\boldsymbol{f} = [0,-1,-1]^\mathrm{T}$ is demonstrated in (e) and (f).

With $\boldsymbol{f} = [0,-1,-1]^\mathrm{T}$, two unit moments are applied clockwise around the $x$- and $y$-axes at $\boldsymbol{0}$ simultaneously and the resulting flexural displacement is plotted in Figures 4e and 4f. As with the single moment forcing above, the displacement field generated by the double moments is radially localised but not confined to a single direction; in this case, the line of zero flexural displacement lies on $\pi/4$, as has been indicated by the dotted line.

In addition to evaluating the flexural displacement $w(m,n)$, we can use the inverse Fourier transformation to evaluate the $\theta_x(m,n)$ and $\theta_y(m,n)$ components of the displacement vector. These components give a quantitative measure for the magnitude of the rota-

tion each node experiences around the relevant axis. In the interests of clarity, the plots of the Green's functions for rotational displacements are omitted here because they do not lend themselves to convenient graphical representation. However, it is important to note that these components contribute to the overall lattice response, can be evaluated as described above, and play an important role in the construction of defect modes (cf. § 4.2).

### 2.4 Extreme dynamic anisotropy and non-reciprocity in the pass band

The dispersive behaviour of lattice systems and the associated extreme anisotropy has been well documented and leads to interesting effects such as highly localised waveforms, uni- directional waves, one-way edge modes, and DASERs [17-19, 25, 35]. However these effects are often highly narrowband and usually require careful tuning of the material and geometric parameters through, for instance, the inclusion of resonant elements. In contrast, here we show how localised waveforms and uni-directional waves are easily achieved in broad frequency regimes as a result of incorporating the additional degrees of freedom associated with the interaction between flexural and torsional motion at the nodes. Furthermore, the lattice also supports the highly unusual phenomena of non-reciprocity, despite the lattice being symmetric.

In parallel to the numerical results derived from the analytical Green's function, we develop a novel finite element model to illustrate a range of interesting phenomena in theinfinite lattice. Using COMSOL Multiphysics $^{\circledR}$ , we build a lattice model of $201 \times 201$  Euler-Bernoulli beams and impose frequency-independent damping, in the form of complex stiffness values, on the beams in the vicinity of the boundary of the computational window in order to simulate an infinite lattice and minimise any artificial reflections. In this section, we set the values of $\mu=0.01$ and $C=0.1$ for the rotational inertia and torsional stiffness respectively across all figures.

Figure 5 illustrates the use of the forcing vector to control the propagation of waves through the lattice for pass band frequencies. In particular, we demonstrate that either uni- directional or asymmetric waves can be achieved by choosing the forcing vector appropriately. Firstly, in Figure 5a we choose $f=[-1,0,0]^{T}$ corresponding to an out-of-plane force of frequency $\omega=5$ . The corresponding slowness contour is provided in Figure 5f; as expected, the principle directions of anisotropy coincide with the normals to the slowness contours, which themselves define the directions of maximal group velocity. We note the stark contrast between Figures 5a and 5b and emphasise that the only difference between the two figures is in the choice of forcing; the frequency of excitation is identical in both figures. In particular, Figure 5b corresponds to $f=[0,-1,0]^{T}$ , which is associated with the application of a clockwise moment about the $x$ -axis. The symmetric slowness contour indicates that a wave should propagate along both of the principle axes of the lattice equally, however when the lattice is forced by a moment about the $x$ -axis, zero flexural displacement is induced in the $x$ -axis, and a uni-directional waveform is induced which propagates in the $y$ -direction only. Likewise, a uni-directional wave along the $x$ -axis can be induced using the forcing vector $f=[0,0,-1]^{T}$ . In this way, the forcing vector can be used to select the direction of propagation, similar to the mechanism identified in [19] for in-plane elastic systems.

The forcing vector also allows the application of combined forces and moments, producing modes with rare asymmetric anisotropy which can be used for applications in wave control and energy harvesting. In Figure 5c, the lattice was subjected to out-of-plane forcing with a simultaneous moment applied about the $x$ -axis, such that $f=[-1,-1,0]^{T}$ , at a frequency of $\omega=5$ . The resulting wave propagates along the principle axes as expected, however with remarkably higher amplitude of displacement along the positive $y$ -axis. The combination of the applied translational force and rotational moment causes the $Y^{+}$ beam to displace more than the $Y^{-}$ beam, which induces the asymmetry. Such non-reciprocity is rarely observed and usually requires PT-symmetry breaking but can sometimes be induced by creating asymmetric eigenmodes as in, for example, [27].

It is of note that while these effects have been demonstrated for the frequency $\omega=5$ ,

(a) $\omega = 5, \boldsymbol{f} = [-1,0,0]^\mathrm{T}$
(b) $\omega = 5, \boldsymbol{f} = [0,-1,0]^\mathrm{T}$
(c) $\omega = 5, \boldsymbol{f} = [-1,-1,0]^\mathrm{T}$

![](./images/867769598009672143_10.jpg)
![](./images/867769598009672143_11.jpg)
![](./images/867769598009672143_12.jpg)

![](./images/867769598009672143_13.jpg)
![](./images/867769598009672143_14.jpg)
![](./images/867769598009672143_15.jpg)

(d) $\omega = 8, \boldsymbol{f} = [-1,0,0]^\mathrm{T}$
(e) $\omega = 8, \boldsymbol{f} = [-1,-1,-1]^\mathrm{T}$
(f) Slowness contours

![](./images/867769598009672143_16.jpg)
![](./images/867769598009672143_17.jpg)
![](./images/867769598009672143_18.jpg)

![](./images/867769598009672143_19.jpg)
![](./images/867769598009672143_20.jpg)

**Figure 5:** The finite element model, with $\mu = 0.01$ and $C = 0.1$, subject to the following forces and moments at $\boldsymbol{0}$ for the chosen frequency: (a) forcing $\boldsymbol{f} = [-1,0,0]^\mathrm{T}$ of frequency $\omega = 5$; (b) forcing $\boldsymbol{f} = [0,-1,0]^\mathrm{T}$ of frequency $\omega = 5$; (c) forcing $\boldsymbol{f} = [-1,-1,0]^\mathrm{T}$ of frequency $\omega = 5$; (d) forcing $\boldsymbol{f} = [-1,0,0]^\mathrm{T}$ of frequency $\omega = 8$; (e) forcing $\boldsymbol{f} = [-1,-1,-1]^\mathrm{T}$ of frequency $\omega = 8$; and finally (f) the corresponding slowness contours for the lower dispersion surface of Figure 3.

these displacements can be achieved in a broad frequency regime. As can be seen in Figure 5f, there is an extended interval of frequencies for which the slowness contours all have the same quasi-rectalinear shape. The waveforms at these frequencies all display similar localisation as Figure 5a, and as such the same anisotropy can be induced through the choice of forcing vector; we further show in $\S$ 2.5 that the associated shape of the slowness contours is stable over a wide range of values of $\mu$ and $C$. This is especially advantageous for the implementation of these effects in practical devices; in previous studies, generating uni-directional waves has required exact values of the material parameters and forcing frequency [35] and also has been associated with so-called 'parabolic metamaterials' in narrow frequency regimes around Dirac cones [17]. In contrast we have shown that, by fully taking into account the flexural and torsional interactions present in the lattice, it is possible to achieve similar effects without requiring highly precise tuning of material parameters. This is particularly important for the fabrication of such devices where a degree of tolerance in the manufacturing process is required.

In Figure 5, we also demonstrate that it is possible to control the dynamic anisotropy and shape of the localised waveforms propagating through lattice by altering the forcing frequency. In Figure 5d, we subject the lattice to an out-of-plane force of frequency $\omega = 8$,

producing a wave that travels equally along the diagonals of the lattice consistent with the principal directions predicted from the slowness contours in Figure 5f. Comparing Figures 5a and 5d, it is observed that the principle directions of the two localised waveforms are rotated by $\pi/4$; the only difference between these two figures is the chosen forcing frequency.

A further example, illustrating non-reciprocity, is shown in Figure 5e, which gives the displacement under $\boldsymbol{f} = [-1,-1,-1]^\mathrm{T}$, inducing simultaneous out-of-plane forcing and dou- ble moments applied clockwise around both the $x$- and $y$-axes, at frequency $\omega=8$. While there is a small displacement propagating at $\pi/4$ to the principle axes, this is dominated by a much larger displacement propagating along the $3\pi/4$ line. We also remark that the displacement along $3\pi/4$ is larger than along $7\pi/4$; although this is difficult to discern from Figure 5e, it can be verified by direct evaluation of equation (2.14).

### 2.5 The effects of altering the rotational inertia and the torsional stiffness

We have shown above that the lattice provides significant control over the propagation of waves from the variety of forcing options alone, with rare examples of anisotropy. It is now shown that the dependence of the dispersion equation (2.10) on the rotational inertia and torsional stiffness, not only provides extensive control over the location (and existence) of band gaps for the lattice, but also the shape of the dispersion surfaces and in turn the preferential direction of wave propagation.

![](./images/867769598009672143_21.jpg)

**Figure 6:** The dispersion diagrams for square lattices of Euler-Bernoulli beams with different values of rotational inertia $\mu$ and torsional stiffness $C$, where (a) $\mu=0.001$ and $C=0.01$ (b) $\mu=1$ and $C=0.1$ (c) $\mu=0.1$ and $C=0.1$ (d) $\mu=0.1$ and $C=10$.

The different dispersion diagrams can be roughly classified into three shapes. When $\mu$ is very small (around 0.01 or below) and the torsional stiffness is allowed to range from very small to very large values, the dispersion diagrams have the same overall configuration as Figure 6a, most often with a finite band gap. Generally the boundary of the acoustic band (the lower dispersion surface) does not change, although the shape of the surface does alter, in turn producing slowness contours with very different shapes.

11

When $\mu$ is 1 or larger, we observe a conical shape which is more commonly associated with beam lattices, such as in Figure 6b. we also see that the boundary of the semi-infinite band gap usually occurs as much lower frequencies. For intermediate values of $\mu$, the dispersion diagram can have a shape similar to Figure 6a, although a finite band gap is seen less often, as is the case in Figure 6d. Alternatively, we can see an entirely different shape, such as Figure 6c, depending on the torsional stiffness. Note that Figures 6c and 6d were produced using the same value of $\mu$, but different $C$. This shows how amenable the dispersive properties of the lattice are to manipulation, indeed altering the values of $\mu$ and $C$ allows us to tailor the dispersion surfaces to desired choices of band gaps and slowness contours.

It is noticed that, regardless of the size of the rotational inertia and torsional stiffness, for $k_1 = k_2 = \pi$, the solution to the dispersion equation is always $\omega = 4\sqrt{6}$; that is, $\sigma(4\sqrt{6},\pi,\pi)=0$ for all values of $\mu$ and $C$. This $\omega=4\sqrt{6}$ often forms the boundary to a band gap (see, Figures 3, 6a and 6b), but not always (see, Figures 6c and 6d). Two other notable solutions to the dispersion equation are $\sigma(0,0,0)=0$, and $\sigma(4\sqrt{3},0,\pi)=\sigma(4\sqrt{3},\pi,0)=0$ for all values of $\mu$ and $C$. In particular, the frequency $\omega=4\sqrt{3}$ at the edge of the Brillouin zone provides a clear connection to the one-dimensional case, (cf. § 3.1).

## 3 A chain of Euler-Bernoulli beams

In this section, we construct a new class of Green's functions for an infinite one-dimensional chain of thin Euler-Bernoulli beams with connecting junctions that possess both mass and rotational inertia. Unlike the square lattice studied in $\S 2$, there are no torsional interactions to account for in the 1D chain. This simplification, along with having only one Fourier parameter means that the Green's functions can be evaluated in closed form, as will be shown. In a right-handed coordinate system, we construct the chain along the $y$-axis, and define the translational motion along the $z$-axis, as shown in Figure 7. While there are no torsional interactions, each junction in the chain has two degrees of freedom, corresponding to the translational displacement $w$ and rotational displacement (about the $x$-axis) $\theta_x$.

![](./images/867769598009672143_22.jpg)

**Figure 7:** The flexural displacement of an Euler-Bernoulli beam chain, lying along the $y$-axis, with rotations measured anticlockwise about the $x$-axis (out of the page).

As before, we introduce the generalised displacement vector $\boldsymbol{u}_n = [w(n),\theta_x(n)]^{\mathrm{T}}$ of the $n^{\text{th}}$ junction to describe the translational and rotational displacements of the nodes, which are coupled through the flexural deformations of the beams. The mass of the nodes, flexural rigidity and length of the beams are once again chosen as natural units. To construct the equation of motion for the $n^{\text{th}}$ unit cell, we evaluate the forces acting on the node at $y=n$ from the beam on $n \leq y \leq n+1$ which we denote $Y^+$, using the same method as previously.

The flexural deformation of the Euler-Bernoulli beams, $w(y)$ is governed by the same fourth order differential equation used in $\S 2$, equation (2.1). As before, $w(y)$ is a cubic polynomial in $y$, which is found using boundary conditions for the ends of the $Y^+$ beam,

$$
\begin{aligned}
w(n) &= W_0 & w(n+1) &= W_1 \\
w_{,x}(n) &= \Theta_0 & w_{,x}(n+1) &= \Theta_1;
\end{aligned}
$$

where $W_i$ are the translational displacements and $\Theta_i$ are the angles of rotation of the junctions. The positive flexural rotations of each junction are defined anticlockwise about the

$x$-axis, shown in Figure 7. We use the same equations for the shear force $F(y)$ and bending moment from the flexural rotations $M_{flex}(y)$ as in $\S 2$, equation (2.5). We introduce the generalised forcing vector $\mathbb{F}_{n} = [F(n), M_{flex}(n)]^{\mathrm{T}}$ and as such, the force and the bending moment at $y = n$ associated with the $Y^{+}$ beam can be expressed as

$$
\left.\mathbb{F}_{n}\right|_{Y_{+}}=A \boldsymbol{u}_{n}+B \boldsymbol{u}_{n+1} \tag{3.1}
$$

where the matrices
$$
A=\left[\begin{array}{ll}
-12 & -6 \\
-6 & -4
\end{array}\right] \quad \text { and } \quad B=\left[\begin{array}{ll}
12 & -6 \\
6 & -2
\end{array}\right]
$$

encapsulate the flexural rigidity of the beams connecting the $n^{\text {th }}$ node to the $(n+1)^{\text {th }}$ node.

Considering Figure 7, it can be seen that the translational forces at the $y=n+1, n-1$ nodes have opposite sign, while the bending moments have same direction. Hence we use the matrix $R=\operatorname{diag}[-1,1]$, which describes a rotation by $\pi$ of the coordinate system about the $x$-axis. Using this rotation, the forces exerted on the node at $y=n$ by the beam that lies on $n-1 \leq y \leq n$ (which we denote $Y^{-}$), are

$$
\left.\mathbb{F}_{n}\right|_{Y^{-}}=R A R^{-1} \boldsymbol{u}_{n}+R B R^{-1} \boldsymbol{u}_{n-1}. \tag{3.2}
$$

With Newton's second law, the time-harmonic equation of motion of the $n^{\text {th }}$ node can be expressed

$$
0=\left[\omega^{2} \mathrm{M}+A+R A R^{-1}\right] \boldsymbol{u}_{n}+B \boldsymbol{u}_{n+1}+R B R^{-1} \boldsymbol{u}_{n-1}, \tag{3.3}
$$

where $\mathrm{M}=\operatorname{diag}[1, \mu]$ is the matrix that describes the inertial properties of the chain. The first component of $\mathrm{M}$ corresponds to the mass of the junction whilst the second component corresponds to the rotational inertia, denoted $\mu$. In the chosen system of natural units $\mu$ is actually the moment of inertia per unit mass of the nodes and so, for junctions between thin beams, $0<\mu \ll 1$. After applying the discrete Fourier transformation

$$
\boldsymbol{u}^{F}(k)=\sum_{n \in \mathbb{Z}} \mathrm{e}^{-\mathrm{i} k n} \boldsymbol{u}_{n},
$$

to equation (3.3), we arrive at the equation of motion for the Euler-Bernoulli beam chain in reciprocal space,

$$
0=\left[\omega^{2} \mathrm{M}+A+R A R^{-1}+\mathrm{e}^{\mathrm{i} k} B+\mathrm{e}^{-\mathrm{i} k} R B R^{-1}\right] \boldsymbol{u}^{F}(k), \tag{3.4}
$$

where $k$ is the Fourier variable and $\boldsymbol{u}^{F}(k)=\left[W^{F}(k), \Theta^{F}(k)\right]^{\mathrm{T}}$ is the generalised displacement in reciprocal space, formed of the Fourier transformation of the real space displacements $w(n)$ and $\theta_{x}(n)$.

### 3.1 The dispersion equation

The solvability condition of equation (3.4) yields the dispersion equation, $\sigma(\omega, k)=0$, where

$$
\sigma(\omega, k)=\mu \omega^{4}+(24 \mu \cos (k)-4 \cos (k)-24 \mu-8) \omega^{2}+24 \cos (2 k)-96 \cos (k)+72. \quad(3.5)
$$

Given that equation (3.5) is quadratic in $\omega^{2}$, we can find analytical representations $\omega=\omega(k)$ for the dispersion curves, such that $\sigma(\omega(k), k)=0$. Moreover, the exact values of the edges of the band gaps can be found easily. The dependence of the dispersion equation on $\mu$ illustrates the importance of the rotational inertia; in particular the rotational inertia can be used as a parameter to control the location and width of the band gaps.

In Figure 8 we plot the dispersion diagram for a chain with $\mu=0.06$, across the first Brillouin zone $k \in[-\pi, \pi]$. It is seen that, for $\mu=0.06$, the Euler-Bernoulli beam chain has two band gaps, one finite band gap for $4 \sqrt{3}<\omega<10 \sqrt{2 / 3}$, and the semi-infinite band gap associated with discrete systems, for $\omega>10 \sqrt{2}$.

![](./images/867769598009672143_23.jpg)
Figure 8: Dispersion curves for the chain of Euler-Bernoulli beams, for the chosen value of $\mu=0.06$. The band gaps have been shaded light blue.

![](./images/867769598009672143_24.jpg)
Figure 9: Planes have been formed from the dispersion curves for the Euler-Bernoulli beam chain across a range of $\mu$. The planes do not touch apart from for one degenerate value of $\mu=1/12$ when $\omega=4\sqrt{3}$.

In Figure 9, we explore the evolution of the dispersion curves with changing rotational inertia. It is emphasised that Figure 9 does not show dispersion surfaces, rather planes have been formed by plotting the dispersion curves for a range $\mu$. The planes are disjoint except for at one degenerate value of $\mu=1/12$ when $\omega=4\sqrt{3}$. For any $\mu\neq1/12$, the chain always has two band gaps: a semi-infinite band gap for large $\omega$, and also a finite band gap with non-zero width. Even as $\mu\rightarrow\infty$, a finite band gap still exists, although it becomes infinitesimally thin. Furthermore, regardless of the value of $\mu$, the dispersion equation always satisfies $\sigma(4\sqrt{3},\pi)=0$. This provides a connection to the square lattice (c.f. $\S2$) since $\sigma(4\sqrt{3},0,\pi)=\sigma(4\sqrt{3},\pi,0)=0$ and, in this regime, the 2D problem becomes quasi-one-dimensional. When $\mu=1/12$ the semi-infinite band gap remains and, despite the fact there is no finite band gap, forcing the chain at this degeneracy nevertheless results in a localised mode, as discussed in $\S3.8$. In the vicinity of $\mu=1/12$, the critical point $(\omega,k)=(4\sqrt{3},\pi)$ is associated with the lower/upper boundaries of the finite band gap for $\mu\leqslant1/12$, and for $\mu\gg1/12$, $\omega=4\sqrt{3}$ forms the lower boundary of the semi-infinite band gap.

### 3.2 The Green's function

To construct the Green's function, we consider the application of force $\boldsymbol{f}\in\mathbb{C}^{2}$ to the central node of the lattice. The forcing vector $\boldsymbol{f}=[f_{w},f_{\theta}]^{\mathrm{T}}$ has components corresponding to the translational force $f_{w}$ and rotational moment $f_{\theta}$, and we let $f_{w},f_{\theta}\in\{0,-1\}$ with the exclusion of $f_{w}=f_{\theta}=0$ which equates to the absence of an applied force. The Green's function in reciprocal space can then be expressed

$$
\boldsymbol{u}^{F}(k)=\left[A+RAR^{-1}+\omega^{2}\mathrm{M}+\mathrm{e}^{\mathrm{i}k}B+\mathrm{e}^{-\mathrm{i}k}RBR^{-1}\right]^{-1}\boldsymbol{f}.\tag{3.6}
$$

For convenience, we separate the flexural displacement $W^F(k)$ and rotation $\Theta^F(k)$ components for evaluation. Explicitly, the flexural displacement of the chain in reciprocal space is
$$
W^{F}(k)=\frac{\left(\mu \omega^{2}-4 \cos (k)-8\right) f_{w}+12 \mathrm{i} \sin (k) f_{\theta}}{\sigma(\omega, k)}.\qquad(3.7)
$$

The denominator of $W^F(k)$ coincides with the dispersion equation (3.5) as a result of the inverted matrix in equation (3.6). The flexural displacement in direct space is obtained by applying the inverse Fourier transform to the spectral representation equation (3.7), as follows
$$
w(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} W^{F}(k) \mathrm{e}^{\mathrm{i} k n} \mathrm{~d} k.\qquad(3.8)
$$

A significant difference between the chain of beams and the square lattice from $\S 2$ is the ability to evaluate the integral of the inverse Fourier transformation in closed form. To evaluate the integral we use the substitution $z=\mathrm{e}^{\mathrm{i} k}$ to map the line segment $[-\pi, \pi]$ to the unit circle in the complex plane. Following the substitution, we denote the displacement $W^F(z)$, and apply Cauchy's Residue Theorem by determining where the poles of the integrand, $z_i$, lie in respect to the unit circle and taking the residues as follows,
$$
w(n)=\frac{-\mathrm{i}}{2 \pi} \oint z^{n-1} W^{F}(z) \mathrm{d} z=\sum_{\left|z_{i}\right|<1} \operatorname{Res}\left[W^{F}(z), z_{i}\right]-\frac{1}{2} \sum_{\left|z_{i}\right|=1} \operatorname{Res}\left[W^{F}(z), z_{i}\right].\qquad(3.9)
$$

The numerator of equation (3.7) is an entire function and, therefore, the poles of equation (3.8) are the zeros of the dispersion equation (3.5) and, consequently, are frequency dependent. Nevertheless, we can use the fact that the complex solutions of the dispersion equation only cross the unit circle when the frequency traverses the boundary of a pass band to construct closed form Green's functions for each frequency regime: finite band gap, semi-infinite band gap and pass band frequencies.

### 3.3 Finite band gap
As an example, we evaluate explicitly the flexural displacement Green's function in the finite band gap regime for translational forcing $\boldsymbol{f}=[-1,0]^{\mathrm{T}}$, using equation (3.9). For frequencies in the finite band gap,
$$
w(n)=\frac{\rho_{+} \gamma_{+}^{n}+\rho_{-} \gamma_{-}^{n}}{2^{\left(3 n+\frac{1}{2}\right)} 3^{n} \psi \omega^{2}\left(\omega^{2}-48\right)},\qquad(3.10)
$$
where the following repeated factors have been introduced
$$
\psi=\sqrt{144+\left(1-24 \mu+36 \mu^{2}\right) \omega^{2}}, \quad \gamma_{ \pm}=24+(1-6 \mu) \omega^{2} \pm \psi \omega \mp \sqrt{2} \rho_{ \pm} \quad \text { and }
$$
$$
\rho_{ \pm}=(6 \mu \omega-2 \omega \pm \psi) \sqrt{\left(36 \mu^{2}-18 \mu+1\right) \omega^{4} \pm(\psi-6 \mu \psi) \omega^{3}+(96-144 \mu) \omega^{2} \pm 24 \psi \omega}.
$$

In Figure 10, we plot $w(n)$ for the chosen values of $\mu=0.06$ and $\omega=7.5$, it can be seen that the waves decay exponentially away from the forcing point at the origin as expected.

![](./images/867769598009672143_25.jpg)

Figure 10: A plot of the flexural displacement Green's function $w(n)$ in the finite band gap of the Euler-Bernoulli beam chain subject to point forcing $\boldsymbol{f}=[-1,0]^{\mathrm{T}}$ at the origin, where $\mu=0.06$ and $\omega=7.5$.

15

### 3.4 Rotational forcing

Choosing the forcing vector $\boldsymbol{f} = [0, -1]^\mathrm{T}$ in equation (3.6) has the effect of applying a clockwise moment about the $x$-axis, rather than the previous translational force. We then evaluate the real space Green's function in the same manner, using equation (3.9), to find the flexural displacement of the chain in response to the applied moment. This is plotted in Figure 11, using the same values for $\mu = 0.06$ and $\omega = 7.5$ as were used in Figure 10 for comparison.

![](./images/867769598009672143_26.jpg)

**Figure 11:** A plot of the flexural displacement Green's function $w(n)$ for $\mu = 0.06$ and $\omega = 7.5$ within the finite band gap, induced by an applied moment about the $x$-axis $\boldsymbol{f} = [0, -1]^\mathrm{T}$, at $n = 0$.

Figure 11 clearly demonstrates the twist induced in the chain from the rotational forcing. There is notably zero translational motion at the $n = 0$ node, as expected for a purely rotational force, followed by a comparatively large displacement, anti-symmetric in each direction, which soon decays.

### 3.5 The semi-infinite band gap

Alongside studying the finite band gap, we also construct Green's functions for the semi-infinite band gap. Using the same value of the rotational inertia, the band gap Green's function for the flexural displacement in the case of translational forcing $\boldsymbol{f} = [-1, 0]^\mathrm{T}$ has been plotted in Figure 12 for $\omega = 14.3$. Similarly, we evaluate the Green's function for the flexural displacement due to an applied moment $\boldsymbol{f} = [0, -1]^\mathrm{T}$. This has been plotted in Figure 13 and exhibits the signature twist shape as expected.

![](./images/867769598009672143_27.jpg)

**Figure 12:** A plot of the flexural displacement Green's function $w(n)$ for $\mu = 0.06$ and $\omega = 14.3$ in the semi-infinite band gap, due to point forcing $\boldsymbol{f} = [-1, 0]^\mathrm{T}$ at $n = 0$.

![](./images/867769598009672143_28.jpg)

**Figure 13:** A plot of the flexural displacement Green's function $w(n)$ for $\mu = 0.06$ and $\omega = 14.3$ in the semi-infinite band gap, due to an applied moment $\boldsymbol{f} = [0, -1]^\mathrm{T}$ at $n = 0$.

Comparing Figures 10 and 12, it is seen that the displacements have significantly different shape despite having the same type of forcing. The same can be said comparing Figures 11 and 13. These differences can be explained by looking a the dispersion curves in Figure 8. For values of $\omega$ in the finite band gap, the complex solutions of the dispersion equation are of

the form $k = \pi + \mathrm{i}\hat{k}$, where $\hat{k} \in \mathbb{R}$, leading to oscillatory eigenmodes of the form $e^{i\pi n - \hat{k}n}$. In contrast, for the semi-infinite band gap, the complex solutions of the dispersion equation are purely imaginary, leading to eigenmodes of the form $e^{-\hat{k}n}$ associated with non-oscillatory evanescent waves.

### 3.6 Pass band frequencies
While the Euler–Bernoulli beam chain has two pass bands, we note that in both the upper and lower pass bands, the position of the poles in relation to the unit circle, from equation (3.9), remains unchanged for fixed $\mu$. Thus we can form one Green's function for both of the pass band regimes, which remains frequency dependent. The flexural displacement Green's function in response to a translational point force at $n = 0$ of frequency $\omega = 2$, is plotted in Figure 14. As expected, we note that waves of constant amplitude are observed, indicating propagative modes.

![](./images/867769598009672143_29.jpg)

**Figure 14:** A plot of the flexural displacement Green's function $w(n)$ for $\mu = 0.06$ and $\omega = 2$ in the lower pass band, due to point forcing $\boldsymbol{f} = [-1,0]^{\mathrm{T}}$ at $n = 0$.

### 3.7 Rotational displacement
Evaluating the inverse Fourier transformation of $\Theta^{F}(k)$ component of $\boldsymbol{u}^{F}(k)$ in equation (3.6) gives the rotational displacement of the chain $\theta_{x}$ in response to the applied force. Until now, we have emphasised the flexural displacement component since the plots of $w(n)$ can be interpreted intuitively as the deformed shape of the chain. However the rotational displacement Green's function is a useful tool that provides further insight into the lattice behaviour, and a quantitative measure of how much each mass rotates.

In Figure 15 we plot $\theta_{x}(n)$ in response to a translational point force $\boldsymbol{f} = [-1,0]^{\mathrm{T}}$ for $\omega = 7.5$ and $\mu = 0.06$. These are the same conditions applied that were applied to Figure 10 when plotting the flexural displacement. In Figure 15, it can be seen that the $n = 0$ mass has zero rotational displacement under purely translational forcing, which is expected at the central node of the lattice where the force is applied. This agrees with Figure 10 which shows that while the beams either side of the $n = 0$ mass deform, the mass itself does not twist in place. It is also seen that the magnitude of the rotational displacement of each node decreases as $n$ increases, which is characteristic of a decaying wave.

![](./images/867769598009672143_30.jpg)

**Figure 15:** A plot of the rotational displacement $\theta_{x}(n)$ of each node, for the values of $\mu = 0.06$ and $\omega = 7.5$ within the finite band gap, due to point forcing $\boldsymbol{f} = [-1,0]^{\mathrm{T}}$ at $n = 0$.

### 3.8 Degenerate point
As shown in $\S$ 3.1, the finite band gap collapses for only one value of the rotational inertia, $\mu = 1/12$. When $\mu = 1/12$, the dispersion equation degenerates and the two simple poles

associated with the Green's function coalesce at $\omega = 4\sqrt{3}$. At this point of degeneracy, for a translational point force at $n = 0$, the inverse Fourier transformation of the flexural displacement has a convenient representation in terms of the PFQ regularised hypergeometric function $\tilde{F}$ as follows

$$
w(n)=\frac{1}{2 \pi} \int_{-\pi}^{\pi} \frac{\mathrm{e}^{\mathrm{i} k n}}{12(\cos (k)-5)} \mathrm{d} k=-\frac{1}{36} \pi{ }_{3} \tilde{F}_{2}\left(\frac{1}{2}, 1,1 ; 1-n, n+1 ; \frac{1}{3}\right).\qquad(3.11)
$$

The displacement $w(n)$ at the degeneracy results in an oscillatory evanescent wave, despite the frequency $\omega=4 \sqrt{3}$ being a solution to the dispersion equation, that is $\sigma(4 \sqrt{3}, \pi)=0$, which would indicate a propagative mode. Other studies with detail on evaluating Green's functions using hypergeometric functions are found in [13, 31] and references therein.

## 4 General Method

In this section we extend the previous work to form a general method for the construction of dynamic Green's functions on $d$-dimensional lattices with vector connections capable of de- scribing a wide range of mechanical interactions, including elastic beams, rods, and springs. This method allows for the inclusion of interesting effects, such as the torsional stiffness and out-of-plane flexural deformations of the lattice connections, as was demonstrated in earlier sections.

The equations of motion are of the form

$$
\mathrm{D} \boldsymbol{u}_{\boldsymbol{n}}(t)+\mathrm{M} \ddot{\boldsymbol{u}}_{\boldsymbol{n}}(t)=\boldsymbol{f}_{\boldsymbol{n}},\qquad(4.1)
$$

where $\boldsymbol{n} \in \mathbb{Z}^{d}$ enumerates the lattice points in which the inertia of the system is concentrated, $d \in \mathbb{N} \backslash\{0\}$ is the dimension of space, $\boldsymbol{u}_{\boldsymbol{n}} \in \mathbb{C}^{d}$ denotes the generalised displacement which includes translation and rotation of the $\boldsymbol{n}^{th}$ node, $\mathrm{D}$ is a discrete [tensor] operator which encapsulates the interaction (e.g. compressional, torsional, flexural, stiffness) of the lattice connections and $\mathrm{M}$ is a tensor describing the inertial properties of the system. The vector $\boldsymbol{f}_{\boldsymbol{n}} \in \mathbb{C}^{d}$ describes the [generalised] forcing — which incorporates, for example, linear forces, bending moments, and torsional moments - and $\ddot{\boldsymbol{u}}_{\boldsymbol{n}}$ is the second derivative of $\boldsymbol{u}_{\boldsymbol{n}}$ with respect to time. In the absence of forcing and for time-harmonic motion, of angular frequency $\omega$, the equations of motion reduce to

$$
\mathrm{D} \boldsymbol{u}_{\boldsymbol{n}}-\omega^{2} \mathrm{M} \boldsymbol{u}_{\boldsymbol{n}}=\mathbf{0},\qquad(4.2)
$$

where $\mathbf{0}$ is the $d$-dimensional zero vector, and the common factor of $\mathrm{e}^{\mathrm{i} \omega t}$ has been omitted for convenience. We introduce the discrete Fourier transformation,

$$
\boldsymbol{u}^{F}(\boldsymbol{k})=\sum_{\boldsymbol{n} \in \mathbb{Z}^{d}} \mathrm{e}^{-\mathrm{i} \boldsymbol{k} \cdot \boldsymbol{n}} \boldsymbol{u}_{\boldsymbol{n}},\qquad(4.3)
$$

where $\boldsymbol{k}$ is the $d$-dimensional Fourier variable. The equation of motion in reciprocal space is provided by the Fourier transformation of equation (4.2),

$$
\left[\mathrm{L}(\boldsymbol{k})-\omega^{2} \mathrm{M}\right] \boldsymbol{u}^{F}(\boldsymbol{k})=\mathbf{0},\qquad(4.4)
$$

where we define $\mathrm{L}(\boldsymbol{k})$ as the Fourier transformed operator $\mathrm{D}$. The solvability condition of equation (4.4) leads to the dispersion equation

$$
\operatorname{det}\left[\mathrm{L}(\boldsymbol{k})-\omega^{2} \mathrm{M}\right]=0.\qquad(4.5)
$$

For discrete systems this equation is polynomial in $\omega$ and the solutions of the dispersion equations can be plotted to produce dispersion diagrams and identify the regions where no


real solutions to the dispersion equation exist, creating band gaps. In general, exciting the system at a frequency within a band gap will yield localised modes that decay exponentially with distance from the forcing point.

We construct the Green's functions by considering the action of time-harmonic generalised forces at the origin of the $d$-dimensional lattices. In this case, the equations of motion are
$$
\mathrm{D} \boldsymbol{u}_{\boldsymbol{n}}-\omega^{2} \mathrm{M} \boldsymbol{u}_{\boldsymbol{n}}=\delta_{\boldsymbol{n}, \boldsymbol{0}} \boldsymbol{f}_{\boldsymbol{n}},\qquad(4.6)
$$
where $\delta_{\boldsymbol{n}, \boldsymbol{m}}$ is the Krönecker delta, and we denote $\boldsymbol{f}_{\boldsymbol{0}}=\boldsymbol{f}$. Following the application of the Fourier transformation, equation (4.6) becomes
$$
\left[\mathrm{L}(\boldsymbol{k})-\omega^{2} \mathrm{M}\right] \boldsymbol{u}^{F}(\boldsymbol{k})=\boldsymbol{f}.\qquad(4.7)
$$

The Green's functions describing the real space displacements $\boldsymbol{u}_{\boldsymbol{n}}$ are determined by applying the inverse of the discrete Fourier transformation as follows,
$$
\boldsymbol{u}_{\boldsymbol{n}}=\frac{1}{(2 \pi)^{d}} \int_{-\pi}^{\pi} \mathrm{e}^{\mathrm{i} \boldsymbol{k} \cdot \boldsymbol{n}} \boldsymbol{u}^{F}(\boldsymbol{k}) \mathrm{d} \boldsymbol{k}=\frac{1}{(2 \pi)^{d}} \int_{-\pi}^{\pi} \mathrm{e}^{\mathrm{i} \boldsymbol{k} \cdot \boldsymbol{n}}\left[\mathrm{L}(\boldsymbol{k})-\omega^{2} \mathrm{M}\right]^{-1} \boldsymbol{f} \mathrm{d} \boldsymbol{k}.\qquad(4.8)
$$

Now, rather than applying external forces to the lattice systems, we consider creating localised modes through the introduction of an isolated defect in the inertial properties of the lattices at $\boldsymbol{n}=\boldsymbol{0}$. In each system the defect is denoted by the $d$-dimensional tensor $\mathcal{M}$ which describes the altered inertial properties at the origin. The Fourier transformed equations of motion for lattices with a defect at the origin are then
$$
\left[\mathrm{L}(\boldsymbol{k})-\omega^{2} \mathrm{M}\right] \boldsymbol{u}^{F}(\boldsymbol{k})=\mathcal{M} \omega^{2} \boldsymbol{u}_{\mathbf{0}}.\qquad(4.9)
$$

By choosing an $\mathcal{M}$ such that
$$
\mathcal{M} \omega^{2} \boldsymbol{u}_{\mathbf{0}}=\boldsymbol{f},\qquad(4.10)
$$
it is possible to recover equation (4.7) and, in doing so, one can produce localised eigenmodes that coincide with band gap Green's functions. The displacement field corresponding to the localised defect modes can be found from equation (4.9), using the inverse Fourier transformation.

### 4.1 A mass defect for the Euler-Bernoulli beam chain
Using the above method, we derive a localised defect $\mathcal{M}$ for the Euler-Bernoulli beam chain such that the chain supports a localised mode for a chosen band gap frequency $\omega$. The Green's functions $w(n)$ and $\theta_{x}(n)$, which form the vector $\boldsymbol{u}_{n}$ can be evaluated in closed form for band gap frequencies using equation (3.9) and the analogous equation for $\theta_{x}$. Thus, $\boldsymbol{u}_{\mathbf{0}}=[w(0), \theta_{x}(0)]^{\mathrm{T}}$ from equation (4.10) is in-hand.

It is noticed that in the case of a purely translational force, the central node experiences zero rotational displacement, that is, $\theta_{x}(0)=0$ when $\boldsymbol{f}=[-1,0]^{\mathrm{T}}$, as can be seen explicitly in Figure 15. Likewise in the case of an applied moment $\boldsymbol{f}=[0,-1]^{\mathrm{T}}$, we see that $w(0)=0$, which is demonstrated in Figure 11. To avoid singular matrices, we define the functions $\alpha_{1}$ and $\alpha_{2}$ as
$$
\alpha_{1}= \begin{cases}1 & \text { if } f_{w}=0 \\ \frac{f_{w}}{\omega^{2} w(0)} & \text { if } f_{w} \neq 0\end{cases}
\quad \text { and } \quad
\alpha_{2}= \begin{cases}\mu & \text { if } f_{\theta}=0 \\ \frac{f_{\theta}}{\omega^{2} \theta_{x}(0)} & \text { if } f_{\theta} \neq 0.\end{cases}
$$

As such, we define the inertial defect at the central node $n=0$ using the matrix
$$
\mathcal{M}=\left[\begin{array}{cc}
\alpha_{1} & 0 \\
0 & \alpha_{2}
\end{array}\right],\qquad(4.11)
$$

19

which is dependent on the applied forcing, and will result in a localised mode around the origin for the chosen band gap frequency. The function $\alpha_1$ corresponds to a change in the mass of the central node $n=0$, while $\alpha_2$ corresponds to the changing the rotational inertia. Off diagonal elements in the matrices would correspond to coupling between the mass and rotational inertia; coupling of parameters is studied in other works such as [8] but is not relevant for this problem.

### 4.2 A mass defect for the square Euler-Bernoulli beam lattice

In the same manner as above, we can evaluate the inertial defect required for the 2D square lattice to support a localised mode for a chosen band gap frequency $\omega$, coincident with the band gap Green's function for the desired forcing. Since the Green's function $\boldsymbol{u}_{(m,n)}$ can be evaluated numerically at the $\boldsymbol{0}$ node, it remains possible for us to find the required values of $w(0,0)$, $\theta_x(0,0)$ and $\theta_y(0,0)$ that compose the $\boldsymbol{u}_{(0,0)}$ vector. As above, to avoid singular matrices, we define the functions

$$
\beta_1 =
\begin{cases}
1 & \text{if } f_w = 0 \\
\dfrac{f_w}{\omega^2 w(0,0)} & \text{if } f_w \neq 0,
\end{cases}
\quad
\beta_2 =
\begin{cases}
\mu & \text{if } f_{\theta_x} = 0 \\
\dfrac{f_{\theta_x}}{\omega^2 \theta_x(0,0)} & \text{if } f_{\theta_x} \neq 0.
\end{cases}
$$

$$
\text{and }
\beta_3 =
\begin{cases}
\mu & \text{if } f_{\theta_y} = 0 \\
\dfrac{f_{\theta_y}}{\omega^2 \theta_y(0,0)} & \text{if } f_{\theta_y} \neq 0.
\end{cases}
$$

Following this, we define the inertial defect matrix as

$$
\mathcal{M} =
\begin{bmatrix}
\beta_1 & 0 & 0 \\
0 & \beta_2 & 0 \\
0 & 0 & \beta_3
\end{bmatrix} ; \tag{4.12}
$$

resulting in a localised defect mode about the $\boldsymbol{0}$ node. The component $\beta_1$ corresponds to a defect in the mass of the $\boldsymbol{0}$ node, while the $\beta_2$ and $\beta_3$ components correspond to defects in the rotational inertia for the $x$- and $y$-directions respectively.

## 5 Concluding Remarks

Firstly we studied a 2D square lattice of Euler-Bernoulli beams with junctions that possessed both mass and rotational inertia. The beams also possessed torsional stiffness, to account for the coupling between flexural and torsional waves at the junctions. The Green's function was used alongside finite element software to illustrate the extreme anisotropy (including remarkable asymmetric anisotropy, usually associated with PT-symmetry breaking) that can be achieved, and controlled in the lattice by altering the frequency and nature of the applied forcing. Analysis of the dispersion diagrams for various values of the rotational inertia and torsional stiffness was used to illustrate how the propagation of waves and dynamic behaviour of the lattice can be manipulated, giving an unprecedented level of control over the pass band frequencies and their preferential directions through the lattice.

We also studied the related problem of a 1D chain of Euler-Bernoulli beams with junctions that possess mass and rotational inertia. Closed form analytical Green's functions were achieved for each of the pass band and band gap regimes of the chain, for different choices of forcing. We also demonstrated how the rotational inertia provides significant control over the propagating frequencies on the lattice. Lastly, we provided a method to construct Green's functions for a generalised $d$-dimensional lattice with discrete mass and arbitrary linear interactions between nodes. We then provided a method to design lattice

defects such that the lattice possesses a localised mode of a chosen frequency. This method was used to derive inertial defect matrices for the 2D lattice and the 1D chain from earlier in the paper. The work in this paper has applications in many areas where the control of wave propagation through elastic structures is of particular interest — including metamaterials, seismic protection, energy dissipation, and others.

## Acknowledgements

Financial support from the University of Liverpool and National Tsing Hua University, through its dual-PhD programme, to KM is gratefully acknowledged. The authors are also grateful for valuable conversations with Professor Natasha Movchan regarding the structure of the paper.

## References

1.  J. B. Pendry. Negative refraction makes a perfect lens. *Phys Rev Lett*, 85(18):3966–3969, 2000.
2.  R. A. Shelby, D. R. Smith, and S. Schultz. Experimental verification of a negative index of refraction. *Science*, 292(April):77–80, 2001.
3.  J. B. Pendry, D. Schurig, and D. R. Smith. Controlling electromagnetic fields. *Science*, 312(5781):1780–2, 2006.
4.  D. Misseroni, D. J. Colquitt, A. B. Movchan, N. V. Movchan, and I. S. Jones. Cymatics for the cloaking of flexural vibrations in a structured plate. *Scientific Reports*, 6(1), 2016.
5.  D. J. Colquitt, M. Brun, M. Gei, A. B. Movchan, N. V. Movchan, and I. S. Jones. Transformation elastodynamics and cloaking for flexural waves. *Journal of the Mechanics and Physics of Solids*, 72:131–143, 2014.
6.  M. Brun, S. Guenneau, and A. B. Movchan. Achieving control of in-plane elastic waves. *Applied Physics Letters*, 94(6):061903, 2009.
7.  A. Colombi, D. J. Colquitt, P. Roux, S. Guenneau, and R. V. Craster. A seismic metamaterial: The resonant metawedge. *Scientific Reports*, 6(1), 2016.
8.  G. W. Milton, M. Briane, and J. R. Willis. On cloaking for elasticity and physical equations with a transformation invariant form. *New Journal of Physics*, 8(10):248–248, 2006.
9.  G. Carta, G. F. Giaccu, and M. Brun. A phononic band gap model for long bridges. The 'Brabau' bridge case. *Engineering Structures*, 140:66–76, 2017.
10. G. Carta, I. S. Jones, N. V. Movchan, A. B. Movchan, and M. J. Nieves. Gyro-elastic beams for the vibration reduction of long flexural systems. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 473(2203):20170136, 2017.
11. X. Zhou, X. Liu, and G. Hu. Elastic metamaterials with local resonances: an overview. *Theoretical and Applied Mechanics Letters*, 2(4):041001, 2012.
12. L. Brillouin. *Wave propagation in periodic structures*. McGraw-Hill Book Company Inc, 2nd edition, 1946.
13. J. M. Borwein, M. L. Glasser, R. C. McPhedran, J. G. Wan, and I. J. Zucker. *Lattice Sums Then and Now*. Encyclopedia of Mathematics and its Applications. Cambridge University Press, 2013.
14. L. I. Slepyan. *Models and phenomena in fracture mechanics*. Springer Science & Business Media, 2012.
15. P. G. Martinsson and A. B. Movchan. Vibrations of lattice structures and phononic band gaps. *The Quarterly Journal of Mechanics and Applied Mathematics*, 56(1):45–64, 2003.

16. M. J. Nieves, A. B. Movchan, I. S. Jones, and G. S. Mishuris. Propagation of Slepyan's crack in a non-uniform elastic lattice. *Journal of the Mechanics and Physics of Solids*, 61(6):1464-1488, 2013.

17. D. J. Colquitt, N. V. Movchan, and A. B. Movchan. Parabolic metamaterials and dirac bridges. *Journal of the Mechanics and Physics of Solids*, 95:621-631, 2016.

18. G. Carta, D. J. Colquitt, A. B. Movchan, N. V. Movchan, and I. S. Jones. Chiral flexural waves in structured plates: Directional localisation and control. *Journal of the Mechanics and Physics of Solids*, 137:103866, 2020.

19. D. J. Colquitt, I. S. Jones, N. V. Movchan, A. B. Movchan, and R. C. McPhedran. Dynamic anisotropy and localization in elastic lattice systems. *Waves in Random and Complex Media*, 22(2):143-159, 2012.

20. M. Ruzzene, F. Scarpa, and F. Soranna. Wave beaming effects in two-dimensional cellular structures. *Smart Materials and Structures*, 12(3):363-372, 2003.

21. R. S. Langley. The response of two-dimensional periodic structures to point harmonic forcing. *Journal of Sound and Vibration*, 197(4):447-469, 1996.

22. R. S. Langley, N. S. Bardell, and H. M. Ruivo. The response of two-dimensional periodic structures to harmonic point loading: a theoretical and experimental study of a beam grillage. *Journal of Sound and Vibration*, 207(4):521-535, 1997.

23. M. J. Nieves, G. Carta, I. S. Jones, A. B. Movchan, and N. V. Movchan. Vibrations and elastic waves in chiral multi-structures. *Journal of the Mechanics and Physics of Solids*, 121:387-408, 2018.

24. G. J. Chaplain, D. Pajer, J. M. De Ponti, and R. V. Craster. Delineating rainbow reflection and trapping with applications for energy harvesting. *New Journal of Physics*, 22(6):063024, 2020.

25. G. Carta, I. S. Jones, N. V. Movchan, A. B. Movchan, and M. J. Nieves. "Deflecting elastic prism" and unidirectional localisation for waves in chiral elastic systems. *Scientific Reports*, 7(1), 2017.

26. M. V. Ayzenberg-Stepanenko and L. I. Slepyan. Resonant-frequency primitive waveforms and star waves in lattices. *Journal of Sound and Vibration*, 313(3-5):812-821, 2008.

27. M. J. Nieves, G. Carta, V. Pagneux, and M. Brun. Rayleigh waves in micro-structured elastic systems: Non-reciprocity and energy symmetry breaking. *International Journal of Engineering Science*, 156:103365, 2020.

28. A. B. Movchan, N. V. Movchan, I. S. Jones, and D. J. Colquitt. *Mathematical modelling of waves in multi-scale structured media*. CRC Press, 2017.

29. P. A. Martin. Discrete scattering theory: Green's function for a square lattice. *Wave Motion*, 43(7):619-629, 2006.

30. A. L. Vanel, R. V. Craster, D. J. Colquitt, and M. Makwana. Asymptotics of dynamic lattice green's functions. *Wave Motion*, 67:15-31, 2016.

31. D. J. Colquitt, M. J. Nieves, I. S. Jones, A. B. Movchan, and N. V. Movchan. Localization for a line defect in an infinite square lattice. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 469(2150):20120579, 2013.

32. A. B. Movchan and L. I. Slepyan. Band gap Green's functions and localized oscillations. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 463(2086):2709-2727, 2007.

33. A. Piccolroaz and A. B. Movchan. Dispersion and localisation in structured Rayleigh beams. *International Journal of Solids and Structures*, 51(25-26):4452-4461, 2014.

34. A. Piccolroaz, A. B. Movchan, and L. Cabras. Dispersion degeneracies and standing modes in flexural waves supported by Rayleigh beam structures. *International Journal of Solids and Structures*, 109:152-165, 2017.

35. G. Bordiga, L. Cabras, D. Bigoni, and A. Piccolroaz. Free and forced wave propagation in a Rayleigh-beam grid: Flat bands, Dirac cones, and vibration localization vs isotropization. *International Journal of Solids and Structures*, 161:64-81, 2018.

36. L. Cabras, A. B. Movchan, and A. Piccolroaz. Floquet-Bloch Waves in Periodic Networks of Rayleigh Beams: Honeycomb Systems, Dispersion Degeneracies, and Structured Interfaces. *Mechanics of Solids*, 52(5):549-563, 2017.

37. A. Piccolroaz, A. B. Movchan, and L. Cabras. Rotational inertia interface in a dynamic lattice of flexural beams. *International Journal of Solids and Structures*, 112:43-53, 2017.

38. D. J. Colquitt, I. S. Jones, N. V. Movchan, and A. B. Movchan. Dispersion and localization of elastic waves in materials with microstructure. *Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences*, 467(2134):2874-2895, 2011.

39. K. F. Graff. *Wave Motion in Elastic Solids*. Oxford University Press, 1975.