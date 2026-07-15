# Phase field modeling of chemomechanical fracture of intercalation electrodes: Role of charging rate and dimensionality

A. Mesgarnejad, A. Karma*

Center for Inter-disciplinary Research on Complex Systems, Department of Physics, Northeastern University, Boston, MA. 02115, U.S.A.

---

## ARTICLE INFO

**Article history:**
Received 18 June 2019
Revised 14 August 2019
Accepted 19 August 2019
Available online 19 August 2019

**Keywords:**
Phase-field modeling
Brittle fracture
Lithium-ion batteries
Flaw tolerance

## ABSTRACT

We investigate the fracture of Li-ion battery cathodic particles using a thermodynamically consistent phase-field approach that can describe arbitrarily complex crack paths and captures the full coupling between Li-ion diffusion, stress, and fracture. Building on earlier studies that introduced the concept of electrochemical shock, we use this approach to quantify the relationships between stable or unstable crack propagation, flaw size, and C-rate for 2D disks and 3D spherical particles. We find that over an intermediate range of flaw sizes, the critical flaw size for the onset of crack propagation depends on charging rate as an approximate power-law that we derive analytically. This scaling law is quantified in 2D by exhaustive simulations and is also supported by 3D simulations. In addition, our results reveal a significant difference between 2D and 3D geometries. In 2D, cracks propagate deep inside the particle in a rectilinear manner while in 3D they propagate peripherally on the surface and bifurcate into daughter cracks, thereby limiting inward penetration and giving rise to complex crack geometries.

© 2019 Elsevier Ltd. All rights reserved.

---

## 1. Introduction

With the demand for electric vehicles and hand-held electronics on the rise, research on rechargeable batteries and, specifically lithium-ion batteries, becomes increasingly important. The need to understand the failure mechanism of these batteries is essential for increasing their life span. Chemo-mechanical failure is one of the primary modes of degradation. The fracture of cathodic and anodic particles due to intercalation-induced stresses has been extensively studied experimentally (Gabrisch et al., 2008; Wang et al., 2013; 2012). The creation of new fracture surfaces impairs the performance of the batteries due to the loss of electrical contact (Chakraborty and Ramakrishnan, 2013; Zavalis et al., 2013) and the creation of solid electrolyte interfaces (SEI) that promotes the irreversible loss of lithium (Li) ions (Deshpande et al., 2012; Peled, 1979).

On the theoretical side, problems arising from the interplay of diffusion and mechanics have been long considered in the literature. Prussin (1961) and Lawrence (1966) were among the first to study the creation and motion of dislocations due to diffusion induced misfit strains. Subsequently, Liu (1970) studied the attraction of corrosive solutes to the crack tip. In the context of chemo-mechanical fracture, Huggins and Nix (2000) studied the initiation of fracture due to the intercalation-driven misfit stresses using a simple 1D model of a thin film bilayer. In this bilayer geometry with a rigid substrate, a constant misfit strain caused by Li intercalation in the thin film is sufficient to create cracks by a mechanism similar to thermal

* Corresponding author.
E-mail address: a.karma@northeastern.edu (A. Karma).

https://doi.org/10.1016/j.jmps.2019.103696
0022-5096/© 2019 Elsevier Ltd. All rights reserved.

expansion (Baldelli et al., 2014). Therefore, using a classical Griffith criterion (Lawn, 1993), Huggins and Nix were able to derive a critical film thickness for fracture. The extension to free-standing particles was subsequently considered in several studies (Bhandakkar and Gao, 2010; Christensen, 2010; Christensen and Newman, 2006; Woodford et al., 2010). Unlike in a thin film constrained on a substrate, a uniform concentration does not create stresses in a free-standing particle. However, due to the finite time to diffusively homogenize the Li concentration inside a particle, a concentration gradient that pro- duces stresses can nonetheless be created when the Li ion flux through the particle boundary, *i.e.*, the charging rate (C-rate), is sufficiently large. By analogy with thermal shock, Woodford et al. (2012, 2010, 2013) coined the term "electrochemical shock" to describe this mode of C-rate dependent fracture (Bourdin et al., 2014). A consistent model that considered the effect of intercalation induced stresses on diffusion was used by Christensen and Newman (2006) and Christensen (2010) to obtain a failure criterion solely based on the magnitude of the resulting stresses. Bhandakkar and Gao (2010) investigated the initiation of a periodic array of equidistant cracks in a thin strip under an imposed constant galvanostatic flux. Using a cohesive zone model and neglecting the effect of fracture on the concentration field, they derived a scaling law relating the largest "safe" strip thickness, below which cracks do not initiate, and C-rate. Woodford et al. (2010) investigated the prop- agation of fracture from an initial radial penny-shaped flaw on a spherical particle. Their calculation of the stress intensity factors at the crack tip was carried out in a simplified geometry, also neglecting the effect of fracture on the concentration field. Their results show that, at a given C-rate, both continuous and abrupt propagation modes are possible for different initial flaw sizes. They further show that for a given flux, there exists a largest safe particle size that does not fracture for any flaw size. Their numerical results indicate that this critical particle size scales as a power-law of charging rate (C-rate).

Even though those studies have yielded quantitative predictions of the dependence of safe particle size on C-rate (Bhandakkar and Gao, 2010; Woodford et al., 2010), they do not consider the full coupling between elasticity, fracture, and diffusion. In addition, penny-shaped cracks are assumed to remain coplanar as they penetrate a 3D spherical particle (Woodford et al., 2010). In practice, more complex non-coplanar crack patterns may develop that depend on C-rate. The goal of this article is to investigate the fracture of Li-ion battery cathodic particles using an extended formulation of the phase-field approach for brittle fracture (Bourdin et al., 2008; Francfort and Marigo, 1998; Karma et al., 2001) that captures the full coupling between elasticity, fracture, and diffusion (Klinsmann et al., 2016a; 2016b; Miehe et al., 2015; 2010; Zuo and Zhao, 2015). While this coupling can also be described by path-independent integral formulations, which provides an efficient method to compute the energy release rate $G$ associated with the crack extension (Haftbaradaran and Qu, 2014; Zhang et al., 2017), the phase-field method has additional advantages. It automatically incorporates the crack growth law $G = G_c$, where $G_c$ is the fracture energy, without explicit tracking of the crack front. This has been rigorously shown in a brittle fracture context by deriving this law from a path-independent integral formulation (Hakim and Karma, 2009), and the same property is expected to hold true for chemo-mechanical fracture as long as the phase-field formulation used to describe the coupled evolution of the concentration and displacement fields is variational. In addition, by regularizing the stress-field divergences on a process zone scale $\xi$, the phase-field approach can describe arbitrarily complex crack paths associated with crack branching, merging, or crack-front segmentation without mesh-size dependencies, which is difficult to achieve with traditional cohesive zone models implemented using the finite element method. Those advantages have been used to reproduce non-trivial experimental observations in brittle fracture including thin-film fracture (Mesgarnejad et al., 2013), thermal fracture (Bourdin et al., 2014), mixed-mode fracture (Chen et al., 2015), dynamic fracture (Chen et al., 2017; 2015; Lubomirsky et al., 2018), and fracture in colloidal systems (Peco et al., 2019). Phase-field approaches have also been developed for ductile fracture (Alessi et al., 2017; Ambati et al., 2015; Borden et al., 2016; Mozaffari and Voyiadjis, 2015) and fatigue crack growth (Alessi et al., 2019; Carrara et al., 2018; Mesgarnejad et al., 2019). In a chemo-mechanical fracture context, the phase-field approach have been used to simulate fracture patterns that qualitatively resemble experimental ob- servations (Klinsmann et al., 2016a; 2016b; Miehe et al., 2015; 2010; Zuo and Zhao, 2015) and to corroborate findings of Woodford et al. (2010) such as the existence of unstable and stable crack propagation as a function of initial flaw size and to describe simple 3D crack patterns (Klinsmann et al., 2016a; 2016b). In this article, we exploit the phase-field approach to quantify the relationship between crack propagation, flaw size, and C-rate, and to describe for the first time in a chemo- mechanical context complex 3D fracture patterns resulting from branched crack growth in pristine spherical particles.

We extend and generalize the results of previous studies (Bhandakkar and Gao, 2010; Klinsmann et al., 2016a; Woodford et al., 2010) to account for the effect of the crack length on the failure of 2D circular disks and 3D spherical particles during Li extraction. By performing an exhaustive series of 2D simulations for different flaw sizes and C-rates for a fixed parti- cle radius, we identify three regimes of fracture propagation where (I) large flaws comparable to the particle size do not propagate due to insufficient driving stresses, (II) for intermediate flaw sizes, the critical flaw size scales as an approximate power-law function of C-rate with an exponent that we derive analytically, (III) for very small flaw sizes the C-rate required for propagation diverges resulting in a flux-independent minimum flaw size. Next, we obtain a scaling law relating the safe particle size, computed with a fixed flaw size to particle radius ratio, to the C-rate. Furthermore, we perform 3D studies of fracture of full spherical particles containing a small subsurface penny-shaped crack without assuming any symmetries. Therefore, we do not assume that crack propagation remains coplanar, as in previous 3D analytical studies that assumed coplanarity (Woodford et al., 2010) or 3D phase-field studies that constrained cracks to remain coplanar by imposing sym- metries to reduce computational cost (Klinsmann et al., 2016a). As a result, our simulations reveal that the geometry of fracture changes profoundly in 3D compared to 2D. Instead of remaining coplanar, the penny-shaped crack grows mostly superficially, penetrating only a small depth below the surface and branching to tile the surface with a polygonal crack pattern that has a non-trivial C-rate dependent topology. This crack growth mechanism differs from previous studies in a

chemo-mechanical context where complex crack paths originated from irregularly shaped particle surfaces (Miehe et al., 2015) or grain boundaries in polycrystalline electrodes (Xu and Zhao, 2018). Our results further indicate that, despite this geometrical difference between 2D and 3D crack growth, the dependence of critical flaw size on C-rate follows a similar power-law scaling in 3D as in 2D.

This article is organized as follows. In Section 2, we outline a thermodynamically consistent formulation of chemo-mechanical concentration and stress evolution and fracture. In Section 3, we carry out a scaling analysis of the governing equations and define a subset of key dimensionless parameters. In Section 4.1, for a generic set of material parameters for $LiMn_2O_4$, we present the results of an extensive set of numerical simulations in 2D circular disks and examine the propagation of radial flaws of different sizes. We investigate the influence of C-rate and initial flaw size on crack stability, generalizing the findings of Woodford et al. (2010) and Klinsmann et al. (2016a). We extend our analysis to maximal C-rates in 4.2 and show that there exists a safe particle size regardless of the initial flaw size that can be predicted based on material properties including fracture energy, elastic modulus, and magnitude of misfit strain. We finally extend our analysis to 3D spherical particles with a single radial penny-shaped surface flaw in Section 4.3. Lastly, in Section 5, we summarize our main findings and point out possible future extensions.

## 2. Formulation

We define the total free energy $\mathscr{F}(u, c, \Gamma)$ for a domain $\Omega \subset \mathbb{R}^n$, containing the crack set $\Gamma \subset \Omega$, for displacement $u$ and concentration $c$

$$
\mathscr{F}(u, c, \Gamma)=\mathscr{F}_{e l}(u, c, \Gamma)+\mathscr{F}_{c}(c)+\mathscr{F}_{\Gamma}(\Gamma)
\tag{1}
$$

where $\mathscr{F}_{e l}$ is the elastic energy, $\mathscr{F}_{\Gamma}(\Gamma)$ is the energetic cost of fracture and $\mathscr{F}_{c}$ is the free energy due to the intercalation of Li ions. We can write the elastic energy as

$$
\mathscr{F}_{e l}(u, c, \Gamma)=\int_{\Omega \setminus \Gamma} \mathcal{W}(u, c) d x
\tag{2}
$$

where we define the elastic strain energy as $\mathcal{W}(u, c)=\sigma_{i j} \varepsilon_{i j} / 2$ and the elastic strain

$$
\varepsilon_{i j}(u, c)=e_{i j}(u)-\epsilon_{0} c \delta_{i j}
\tag{3}
$$

where $\epsilon_{0}$ is the coefficient of volume expansion assumed to be isotropic. Furthermore, we define the linear strain $e_{i j}(u)=$ $(u_{i, j}+u_{j, i}) / 2$, and the Cauchy stress tensor $\sigma_{i j}(u, c)=\mathcal{C}_{i j k l} \varepsilon_{k l}$. Moreover, for Lame's constants $\lambda, \mu$ the isotropic elasticity tensor is written as $\mathcal{C}_{i j k l}=\lambda \delta_{i j} \delta_{k l}+\mu\left(\delta_{i k} \delta_{j l}+\delta_{i l} \delta_{j k}\right)$.

We write the free energy of the Li ions intercalating in the host lattice as McKinnon and Haering (1983)

$$
\mathscr{F}_{c}(c)=\int_{\Omega} f_{c}(c) d x
\tag{4}
$$

where

$$
f_{c}=c_{\max } \mathcal{R} T\left[\frac{c}{c_{\max }} \ln \left(\frac{c}{c_{\max }}\right)+\left(1-\frac{c}{c_{\max }}\right) \ln \left(1-\frac{c}{c_{\max }}\right)\right]
\tag{5}
$$

is the entropy of mixing for an ideal binary solution, $c_{\max }$ is the maximum concentration achievable when all accommodating sites are filled, $\mathcal{R}$ is the gas constant, and $T$ is the absolute temperature. This ideal solution approximation is only valid to describe the Li intercalation reaction in a single phase, as in the present test case of Li ion extraction from $Li_{1-x} Mn_{2} O_{4}$ for $0 \leq x \leq 0.6$ (Thackeray et al., 1984). A more general formulation that includes an enthalpic contribution to the chemical free-energy density and the excess free-energy associated with compositional domain boundaries would be needed to model cathodes where two-phase reaction occurs (Singh et al., 2008).

In the spirit of brittle fracture, we write the energetic cost of creating fracture surfaces as

$$
\mathscr{F}_{\Gamma}(\Gamma)=G_{c} \mathcal{H}^{n-1}(\Gamma)
\tag{6}
$$

where $G_{c}$ is the energy required to create a unit area (unit length in 2D) of new cracks, $\mathcal{H}^{m}$ is the $m$-dimensional Hausdorff measure (i.e., $\mathcal{H}^{2}(\Gamma)$ is the aggregate area and $\mathcal{H}^{1}(\Gamma)$ is the aggregate length of cracks $\Gamma$ in three and two dimensions, respectively).

### 2.1. Phase-field model

We use the phase-field model to approximate the sharp interface free energy (1) by introducing a fracture phase field $\phi$ and an associated length-scale $\xi$. Roughly speaking, as $\xi \rightarrow 0$, the displacement field minimizing (7) converges to that of minimizing (1), the field $\phi$ converges to 1 almost everywhere and goes to zero near the cracks. In this article, we treat the length-scale $\xi$ as a regularization parameter to study the sharp-interface limit of the phase-field model that reduces to classical linear elastic fracture mechanics (Hakim and Karma, 2009). We write the approximate free energy replacing $\mathscr{F}_{e l}(u, c, \Gamma)$ by $\mathscr{F}_{e l}(u, c, \phi)$ and $\mathscr{F}_{\Gamma}(\Gamma)$ by $\mathscr{F}_{\phi}(\phi)$ as

$$
\mathscr{F}(u, c, \phi)=\mathscr{F}_{e l}(u, c, \phi)+\mathscr{F}_{c}(c)+\mathscr{F}_{\phi}(\phi)
\tag{7}
$$

with the elastic energy
$$
\mathscr{F}_{e l}(u, c, \phi)=\int_{\Omega} g(\phi) \mathcal{W}(u, c) d x
\tag{8}
$$
and the energetic cost of fracture
$$
\mathscr{F}_{\phi}(\phi)=\frac{G_{c}}{4 C_{\phi}} \int_{\Omega}\left(\frac{w(\phi)}{\xi}+\xi|\nabla \phi|^{2}\right) d x
\tag{9}
$$
where $C_{\phi}=\int_{0}^{1} \sqrt{w(\phi)} d \phi$ is a scaling constant. In the past decade, there has been a growing trend in studying a broad class of rate independent gradient damage models in the form of (7) (Pham and Marigo, 2012; 2013). In this article, we use the Karma-Kessler-Levine model (KKL) (Hakim and Karma, 2009; Karma et al., 2001) defined using $g(\phi)=4 \phi^{3}-3 \phi^{4}$, $w(\phi)=1-g(\phi)$. This model allows us to follow the propagation of a fracture from a single flaw by prohibiting the initiation of new cracks in undamaged material (i.e., $\phi=1$).

### 2.2. Diffusion equation

We write the continuity equation of mass conservation
$$
\frac{\partial c}{\partial t}=-\nabla \cdot J
\tag{10}
$$
with the flux of Li ions
$$
J=-a(\phi) M(c) \nabla \mu
\tag{11}
$$
and the mobility of Li ions in the host lattice $M(c)=m_{0} c\left(1-c / c_{\max }\right)$ (McKinnon and Haering, 1983). The chemical potential
$$
\mu=\frac{\delta \mathscr{F}}{\delta c}
\tag{12}
$$
where
$$
\frac{\delta \mathscr{F}}{\delta c}=\frac{d f_{c}}{d c}-\epsilon_{0} g(\phi) \sigma_{k k}
\tag{13}
$$
is the standard Fréchet derivative of the free energy functional $\mathscr{F}$ defined by Eq. (7) with respect to the concentration $c$. Replacing the above in (11) we obtain
$$
\frac{\partial c}{\partial t}=\nabla \cdot\left[m_{0} a(\phi)\left[\mathcal{R} T \nabla c+\left(\frac{c}{c_{\max }}\right)\left(1-\frac{c}{c_{\max }}\right) \nabla \psi\right]\right]
\tag{14}
$$

$$
\psi=-\epsilon_{0} c_{\max } g(\phi) \sigma_{k k}
\tag{15}
$$

We note that (14) represents Fickian diffusion with the second term only coupling to the mechanical hydrostatic stress because the volume expansion is assumed to be isotropic (Eq. (3)).

As a first estimate, we make the crack surface completely permeable to Li ion diffusion similar to Klinsmann et al. (2016a) by introducing $a(\phi)=1$. This choice assumes that the electrolyte will leak inside the fracture surfaces created by cracks extending from the particle surface, thereby making crack surfaces conduits of Li ion transport. This is a reasonable assumption for the present study that focuses on Li ion extraction where crack propagation at the surface of the particle is energetically favored. This assumption would need to be relaxed for the case of Li ion insertion where crack propagation is energetically favored in the interior of the particle where the electrolyte does not penetrate. The precise choice of $a(\phi)$ should be determined by further studies of the interaction of the electrolyte and fracture surfaces for specific materials that is beyond the scope of this article.

Furthermore, to model galvanostatic charging, we write the flow of Lithium ions from the boundary as a given imposed flux $\hat{J}$:
$$
\left.J\right|_{\partial_{f} \Omega} \cdot \vec{n}=\frac{i}{\mathcal{F}} \equiv \hat{J}
\tag{16}
$$
where $\vec{n}$ is the surface normal to $\partial_{f} \Omega, i$ is the surface current density, and $\mathcal{F}$ is Faraday's constant. In all simulations presented in this article we impose a uniform $\hat{J}$ over all boundaries. The galvanostatic boundary condition of form (16) is a first order approximation of ion transfer on the particle boundary. A more general study can be done by prescribing the value of the flux on the surface at a given voltage as using the Butler-Volmer equation to model reaction kinetics on the cathodic surface of the particle (Doyle et al., 1993). We should note that, as for any diffusion process of a bounded field (here $0 \leq c \leq c_{\max }$ ) with a flux boundary, this boundary condition cannot be maintained for any arbitrary value of $\hat{J}$ for an infinite time. In particular, $\hat{J} \gg 1$ at $t \ll R^{2} / m_{0} \mathcal{R} T$ a depleted boundary layer with thickness $h \ll R$ is created where the concentration at the boundary reaches zero and the flux cannot be maintained any longer.

### 3. Numerical implementation

#### 3.1. Dimensional analysis

For the flux boundary condition (16), it is pertinent to introduce the nominal charging time as the time required to fill the volume of the particle $V$ with a surface flux $\hat{J}$ acting on surface area $A$ i.e.,
$$
t_{\mathrm{C}}=\frac{c_{\max } V}{\hat{J} A}
\tag{17}
$$

It is also customary in Li-ion literature to introduce the so-called charging rate $C_{r}=1 / t_{\mathrm{C}}$, which is usually measured in $\mathrm{hr}^{-1}$ units. To perform the numerical simulations, we adimensionalize the spatial dimensions by the particle radius $R$, the concentration by $c_{\max }$, the time by the diffusion time $t_{D}=R^{2} / D_{0}$ where $D_{0}=m_{0} \mathcal{R} T$ is the diffusion constant, and the stresses by energy per unit volume $c_{\max } \mathcal{R} T$. We write dimensionless charging rate $C_{r}$ as
$$
C_{r}=t_{D} C_{r}=\frac{t_{D}}{t_{C}}
\tag{18}
$$
and the dimensionless flux as
$$
\mathcal{J}=C_{r} \frac{\bar{V}}{\bar{A}}=\frac{t_{D}}{t_{C}} \frac{\bar{V}}{\bar{A}}=\frac{\hat{J} R}{c_{\max } D_{0}}
\tag{19}
$$
where $\bar{V}=V / R^{n}$ is the dimensionless volume of the particle, and $\bar{A}=A / R^{n-1}$ is the dimensionless surface area of the flux boundary. The dimensionless charging rate $C_{r}$ can also be understood intuitively as a mechanical loading parameter noticing that the driving force for crack propagation is the gradient of the concentration field in (8) that is controlled by the flux $\hat{J}$. As a result, for low dimensionless charging rates $C_{r}<1$ (where the nominal charging time is long compared to the diffusion time $t_{C} \gg t_{D}$ ) the concentration will homogenize and thus creates no misfit stresses.

We should also highlight the important dimensionless numbers that uniquely define the simulations performed, namely the relative strength of the elastic energy compared to the chemical energy $E / c_{\max } \mathcal{R} T$ where $E$ is the elastic modulus, the Poisson's ratio $v$, the maximum misfit strain $\beta=c_{\max } \epsilon_{0}$, and the relative domain geometry i.e., radius and initial flaw size, compared to the Griffith length scale $R /\left(G_{c} / E\right)=R / l_{G}$ and $a_{0} / l_{G}$.

#### 3.2. Governing equations

To implement our numerical simulations using the Galerkin finite element method we introduce the weak forms of the governing equations. The governing equations for the concentration diffusion is derived from its flow rule (14)-(15) by multiplying both sides with test functions and integrating by parts. We also incorporate an implicit time integration scheme to ensure the accuracy and stability of the integration.
$$
\begin{aligned}
\int_{\Omega}\left(\frac{c_{t}-c_{t-1}}{\delta t}\right) \tilde{c} d x & +\int_{\Omega} a\left(\phi_{t-1}\right) \nabla_{\Theta} c \cdot \nabla \tilde{c} d x+\int_{\Omega} a\left(\phi_{t-1}\right) M\left(c_{t}\right) \nabla_{\Theta} \psi \cdot \nabla \tilde{c} d x \\
& +\int_{\partial_{f} \Omega}(\mathcal{J} \cdot n) \tilde{c} d s=0 \quad \forall \tilde{c} \in H^{1}(\Omega)
\end{aligned}
\tag{20}
$$

$$
\int_{\Omega}\left[\psi_{t}+\beta g\left(\phi_{t-1}\right) \sigma_{k k}\left(u_{t-1}, c_{t}\right)\right] \tilde{\psi} d x=0 \quad \forall \tilde{\psi} \in H^{1}(\Omega)
\tag{21}
$$
where $n$ is the surface normal to $\partial_{f} \Omega$, subscripts denote time steps with $\delta t$ as the time step size, and we define $\nabla_{\Theta}\{\circ\}=$ $(1-\Theta) \nabla\{\circ\}_{t}+\Theta \nabla\{\circ\}_{t-1}$ as the implicit gradient operator associated with time-fraction $\Theta$. In all calculations in this paper we used $\Theta=0.5$ which corresponds to the midpoint method and results in a second order accurate and unconditionally stable time integration for concentration field $c$.

Moreover, since in practical systems the time-scale of elasticity and fracture propagation are orders of magnitude smaller than that of diffusion, we assume that they are instantaneous. In this setting, we seek the minimizers for the displacement field $u$ and the fracture phase-field $\phi$ for each time step $t_{i}$. Hence, the governing equations for displacement (i.e., elasticity) and fracture phase-field, are written as Euler-Lagrange equations of the total energy (1) for displacement field $u$ and phase field $\phi$
$$
\int_{\Omega} g\left(\phi_{t}\right) \sigma_{i j}(u, c) e_{i j}(\tilde{u}) d x=0 \quad \forall \tilde{u} \in H^{1}(\Omega)
\tag{22}
$$

$$
\int_{\Omega}\left[\frac{d g}{d \phi}\left(\phi_{t}\right) \mathcal{W}(u, c)\right] \tilde{\phi} d x+\frac{G_{c}}{4 \mathcal{C}_{\phi}} \int_{\Omega}\left[\frac{1}{\xi}\left(\frac{d w}{d \phi}\left(\phi_{t}\right)\right) \tilde{\phi}+2 \xi \nabla \phi \cdot \nabla \tilde{\phi}\right] d x=0 \quad \forall \tilde{\phi} \in H^{1}(\Omega)
\tag{23}
$$
where $c_{t}$ is the concentration given by the solution of (20) and (21).

### 3.3. The solution algorithm

The phase-field fracture method requires that the spatial resolution of discretization resolves the characteristic approximation length $\xi$. The resulting problems are often very large and necessitate the use of a parallel programming paradigm and the complex numerical tools therein. Our implementation relies on the distributed data structures provided by `libMesh` (Kirk et al., 2006) and for linear algebra on PETSc (Balay et al., 2014; 1997). On the other hand, we assume that elasticity and fracture are instantaneous and write their governing equations as the weak forms of Euler-Lagrange equation for minimizers of (7) with respect to displacement field $u$ and phase field $\phi$ respectively (see 3.2 for details). This is roughly equivalent to the limit of vanishing relaxation time $\tau_{\phi} \to 0$ assuming that the phase field $\phi$ follows Ginsburg-Landau gradient dynamics:

$$
\tau_{\phi} \frac{\partial \phi}{\partial t}=\frac{1}{c_{\max} \mathcal{R} T} \frac{\delta \mathscr{F}}{\delta \phi}
\tag{24}
$$

We use a classical alternate minimization Algorithm 1 (Bourdin et al., 2008) since the governing equations for elasticity and phase-field are only convex in either $u$ or $\phi$ when the other is kept constant (Bourdin et al., 2008). It is also worth mentioning that to enforce irreversibility of fracture and ensure boundedness of phase field $0 \leq \phi \leq 1$ and the relative concentration $0 \leq c \leq 1$, we use a bounded reduced space Newton minimization scheme for the discrete energy provided in PETSc (Balay et al., 2014; 1997). In particular, at each time step we set upper bound for the solution of phase-field $\phi$ from the previous time step (i.e., $0 \leq \phi_{i} \leq \phi_{i-1}$) to ensure irreversibility of the fracture.

```
Algorithm 1 The alternate minimization algorithm. Subscripts are time steps while superscripts denote the internal alter-
nate minimization iteration.
 1: Set $\phi_0 = 1$ in bulk at $\phi = 0$ at the initial crack.
 2: Let $\delta_{altmin}$ be given tolerance parameters.
 3: for $n=0$ to $N$ do
 4:    Update $c_n$ based on $u_{n-1}$ and $\phi_{n-1}$~(20)-(21).
 5:    Initialize the phase field from last time step: $\phi^0 \longleftarrow \phi_{n-1}$.
 6:    while $|\phi^j - \phi^{j-1}|_{L^\infty} \geq \delta_{altmin}$ do
 7:        Update $u^{j+1}$ using $\phi^j$ and $c_n$~(22).
 8:        Update $\phi^{j+1}$ using $u^{j+1}$ and $c_n$~(23).
 9:        $j \longleftarrow j+1$.
10:    end while
11:    Store the converged time step $u_n \longleftarrow u^j$ and $\phi_n \longleftarrow \phi^j$.
12: end for
```

---

## 4. Numerical results

In the following section, we focus on the numerical simulation of a cathodic particle at the time of charging. We first present our two-dimensional results for circular particles with a preexisting radial flaw on its surface under galvanostatic and potentiostatic boundary conditions. Subsequently, we analyze the fracture of spherical particles with penny-shaped cracks in three dimensions.

### 4.1. Chemo-mechanical fracture of circular particles: (I) galvanostatic (flux) boundary condition

The misfit strains generated during charging and discharging processes can lead to the creation and propagation of cracks in Li-ion battery particles. For a preexisting flaw on the surface of a cathodic particle, the removal of Li-ions during the charging process causes the outer layer of the particle to contract faster than its inner core. Therefore, for fast enough charging rates, the region of tensile stresses created in the outer periphery can activate surface defects creating cracks that will then propagate through the particle. In this section, we present the results of numerical simulation for the fracture of circular particles induced by the removal of Lithium ions during charging. Our goal is two fold: (i) to understand the activation and propagation of a preexisting flaw in a circular cathodic particle, (ii) 2D simulations also enable us to combine the results of many such simulations to give insight into critical parameters for the design of these particles.

Fig. 1 shows a schematics for this problem. We assume a preexisting radial crack $\Gamma_0$ of length $a_0$ and impose a dimensionless galvanostatic flux $\mathcal{J}$ (corresponding to the dimensionless charge-rate $C_r = t_D/t_C$ according to (19)). As stated before, we treat phase-field length scale $\xi$ as a regularization of Griffith brittle fracture. Therefore for the Griffith length scale defined as

$$
l_{G}=\frac{G_{c}}{\mathrm{E}}
\tag{25}
$$

![](./images/812744289514684418_1.jpg)

Fig. 1. The schematics of 2D chemo-mechanical fracture of circular particles numerical simulations.

![](./images/812744289514684418_2.jpg)

Fig. 2. Time snapshots of crack propagation in chemo-mechanical fracture of a $R/l_G=4.2\times10^4$ 2D circular particle with a preexisting $a_0/l_G=10^4$ radial crack driven by $c_r=5.57$ charging rate showing continuous propagation (see also Fig. 5). Color codes depict the dimensionless hoop stress $\sigma_{\theta\theta}/c_{\max}RT$ distribution (top), and the dimensionless concentration distribution $c/c_{\max}$ perturbed as the result of the crack-tip stress field (bottom).

<table>
<thead>
<tr>
<th colspan="4">Table 1</th>
</tr>
<tr>
<th colspan="4">Material properties of ${\text{LiMn}}_2{\text{O}}_4$ for numerical simulation of chemo-mechanical fracture (Woodford et al., 2010).</th>
</tr>
<tr>
<th>Property</th>
<th>Symbol</th>
<th>Units</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>Elastic modulus</td>
<td>E</td>
<td>N m$^{-2}$</td>
<td>$2\times10^{11}$</td>
</tr>
<tr>
<td>Poisson ratio</td>
<td>$\nu$</td>
<td>-</td>
<td>0.3</td>
</tr>
<tr>
<td>Fracture toughness</td>
<td>$G_c$</td>
<td>N m$^{-1}$</td>
<td>100</td>
</tr>
<tr>
<td>Diffusivity</td>
<td>$D_0$</td>
<td>m$^2$ s$^{-1}$</td>
<td>$2.2\times10^{-13}$</td>
</tr>
<tr>
<td>Maximum concentration</td>
<td>$c_{\max}$</td>
<td>mol m$^{-3}$</td>
<td>$2.37\times10^4$</td>
</tr>
<tr>
<td>Misfit Strain constant</td>
<td>$\epsilon_0$</td>
<td>m$^3$ mol$^{-1}$</td>
<td>$1.09\times10^{-6}$</td>
</tr>
<tr>
<td>Density</td>
<td>$\rho$</td>
<td>kg m$^{-3}$</td>
<td>$4.28\times10^3$</td>
</tr>
<tr>
<td>Temperature</td>
<td>$T$</td>
<td>K</td>
<td>$3\times10^2$</td>
</tr>
<tr>
<td>Dimensionless expansion coefficient</td>
<td>$\beta$</td>
<td>m/m</td>
<td>0.025</td>
</tr>
<tr>
<td>Griffith length scale</td>
<td>$l_G$</td>
<td>$\mu$m</td>
<td>$5\times10^{-4}$</td>
</tr>
</tbody>
</table>

we use $\xi>l_G$. For these numerical simulations we use a constant relative process zone size $\xi/R=1.25\times10^{-2}$ for relative flaw size $a_0/R>0.1$ and use $\xi/a_0=5$ for $a_0/R<0.1$ for optimal use of computational resources. Table 1 summarizes the material properties corresponding to ${\text{LiMn}}_2{\text{O}}_4$ used in our simulations.

To highlight the mechanism and modes of radial crack penetration in these particles, we first study three sample cases in Figs. 2,3,4. These sample results correspond to fracture of a $R/l_G=4.2\times10^4$ and $a_0/l_G=2\times10^3,10^4$ initial radial flaws (corresponding to a $R=21\ \mu$m particle with $a_0=1,5\ \mu$m for material properties in Table 1) and using dimensionless charging rates $C_r=5.57,8.35$ (corresponding to physical charging rates $C_r=10,15$ h$^{-1}$ with material properties in Table 1 and gray circles in Fig. 7). In these simulations, we first compare two cases with different initial flaw lengths at the same dimensionless charging rate $C_r$ and then study two cases where we keep $a_0$ constant and change the $C_r$. As we stated before, our simulation results show that tensile hoop stresses are created on the periphery of these particles that can then drive the surface flaws to penetrate radially inside the particle (top row in Figs. 2-4). Fig. 2 shows that the crack propagation for the larger initial flaw $a_0/l_G=10^4$ under lower dimensionless charging rate $C_r=5.57$ is continuous. However, the smaller initial flaw under the same charging rate $C_r=5.57$ propagates abruptly jumping many process zone sizes (see third columns

![](./images/812744289514684418_3.jpg)

Fig. 3. Time snapshots of crack propagation in chemo-mechanical fracture of a $R/l_G=4.2\times10^4$ 2D circular particle with a preexisting $a_0/l_G=2\times10^3$ radial crack driven by $C_r=5.57$ charging rate showing initial $(a-a_0)/R\simeq0.7$ abrupt propagation for $t/t_C\simeq0.27$ followed by continuous propagation (see also Fig. 6). Color codes depict the dimensionless hoop stress $\sigma_{\theta\theta}/c_{\max}\mathcal{R}T$ distribution (top), and the dimensionless concentration distribution $c/c_{\max}$ perturbed as the result of the crack-tip stress field (bottom).

![](./images/812744289514684418_4.jpg)

Fig. 4. Time snapshots of crack propagation in chemo-mechanical fracture of a $R/l_G=4.2\times10^4$ 2D circular particle with a preexisting $a_0/l_G=2\times10^3$ radial crack driven by $C_r=8.35$ charging rate showing $(a-a_0)/R\simeq0.3$ abrupt propagation at $t/t_C\simeq0.13$ followed by continuous propagation (see also Fig. 6). Color codes depict the dimensionless hoop stress $\sigma_{\theta\theta}/c_{\max}\mathcal{R}T$ distribution (top), and the dimensionless concentration distribution $c/c_{\max}$ perturbed as the result of the crack-tip stress field (bottom).

in Fig. 3). The abrupt propagation occurs in the context of Griffith fracture where the crack releases more energy as it propagates (i.e., for the energy release rate defined as $G=-\partial\mathscr{F}_{el}/\partial a$ at a frozen concentration (constant load), the crack is unstable if $dG/da>0$). Analogous results on abrupt propagation due to misfit strains are also reported in the context of thermally driven cracks. For example, Bahr et al. (1987) explicitly calculate the energy release rate as a function of crack length for thermal-quenching-induced cracks.

A similar contrast between continuous and abrupt propagation is also predicted by Woodford et al. (2010) where they explicitly calculate the mode-I stress intensity factor $K_I$ (and, by symmetry since $K_{II}\equiv0$, the energy release rate $G$) for a radial penny-shaped crack in a spherical particle. Their calculations show that for some choices of particle size and initial flaw size $dG/da>0$; therefore, for such flaw sizes, propagation is unstable and abrupt. Concurring with our simulations, their calculations (Fig. 5. in Woodford et al. (2010) where their results correspond directly to Figs. 2-3) show that the flaws smaller than $a_0/l_G<4\times10^3$ will propagate abruptly given our choice of parameters and vice versa.

The transition from abrupt to continuous propagation can also be understood in analogy with mechanical loading in standard fracture mechanics configurations. At lower charging rates where the concentration field has to penetrate on the scale of the particle size before the energy release rate reaches the fracture energy, the activation of the initial notch is

![](./images/812744289514684418_5.jpg)

Fig. 5. Numerical results of a $R/l_G=4.2\times10^4$ particle with an initial $a_0/l_G=10^4$ flaw vs charging time fraction $t/t_C$ for different dimensionless charging rates $C_r$: showing relative crack length increase $a/R$ (dashed lines, right vertical axis) and maximum surface hoop stress far from the crack-tip $\sigma_{\theta\theta}(r=R)$ (solid lines, left vertical axis). Time snapshots for evolution of $C_r=5.57$ was previously shown in Fig. 2.

![](./images/812744289514684418_6.jpg)

Fig. 6. Numerical results of a $R/l_G=4.2\times10^4$ particle with an initial $a_0/l_G=2\times10^3$ flaw vs charging time fraction $t/t_C$ for different dimensionless charging rates $C_r$: showing relative crack length increase $a/R$ (dashed lines, right vertical axis) and maximum surface hoop stress far from the crack-tip $\sigma_{\theta\theta}(r=R)$ (solid lines, left vertical axis). Time snapshots for evolution of $C_r=5.57$ and $C_r=8.35$ were previously shown in Figs. 3 and 4 respectively.

![](./images/812744289514684418_7.jpg)

Fig. 7. Numerical simulation results for a $R/l_G=4.2\times10^4$ particle with $a_0/l_G=200-10^4$ initial flaws: flaw activation diagram for the dimensionless charge rate $C_r$ vs initial flaw size $a_0/l_G$. Circles show the activated vs. crosses show the unactivated cracks. The gray dashed line shows the power-law $a_0/l_G=e^{10.9}C_r^{-2}$ ($a_0\beta^2/l_G=35.93C_r^{-2}$). Computations corresponding to Figs. 2-4 are circled in gray.

![](./images/812744289514684418_8.jpg)

Fig. 8. Numerical simulation results for a $R/l_G=2\times10^5$ particle with $a_0/l_G=10^3$-$4\times10^4$ initial flaws: flaw activation diagram for the dimensionless charge rate $C_r$ vs initial flaw size $a_0/l_G$. Circles show the activated vs. crosses show the unactivated cracks. The gray dashed line shows the power-law $a_0/l_G=e^{10.6}C_r^{-2}$ ($a_0\beta^2/l_G=26.62C_r^{-2}$).

analogous to a crack in half plane under constant far field opening stress that results in an unstable propagation. On the other hand, at high charging rates where the concentration field penetrates on the scale of the initial notch only, the problem resembles a compact specimen with the crack opening from the back that results in stable propagation. Our hypothesis is further verified, comparing Figs. 3 and 4. We can see that at the higher $C_r$ (higher flux), the initial abrupt crack propagation is shorter. While surprising at first glance, we can explain the longer abrupt fracture propagation at lower $C_r$, noticing that the flaw is activated earlier for the higher $C_r$. Thus, at the time of the initial jump, the hoop stresses penetrate farther inside the particle for the lower flux providing more elastic energy to be converted to new fracture surfaces.

Different modes of fracture propagation are further demonstrated and quantified in Figs. 5 and 6 where we show the evolution of relative crack lengths $a/R$ and the dimensionless hoop stress in front of the crack at $r=R$ versus the charging time fraction $t/t_C$ for the simulations of a $R/l_G=4.2\times10^4$ particle with $a_0/l_G=2\times10^3$, $10^4$ preexisting radial flaws respectively and for different dimensionless charging rates $C_r$ (including cases highlighted in Figs. 3 and 4). Similar to Fig. 2, the simulations for the larger $a_0/l_G=10^4$, depicted in Fig. 5, show a clear trend whereby the crack is activated $t/t_C\simeq0.2$ and propagates smoothly. Unlike results presented in Fig. 5, the initial crack propagation in Fig. 6 is abrupt and decreases with higher $C_r$. We should also note, in Figs. 5 and 6, that while the abrupt initial propagation is bigger for the smaller flux, the cracks extend farther into the particle for higher fluxes in line with our intuitive understanding that higher fluxes provide more energy. Similar observations were also made in Klinsmann et al. (2016a) (see Fig. 15 in the reference) where for a $R/l_G=4.65\times10^{10}$ particle containing $a_0/l_G=9.3\times10^8$ initial crack they observed a larger initial abrupt propagation for lower fluxes and vice versa.

Our self-consistent simulations also allow us to observe the interaction of the stresses with the concentration field. We note that the tensile crack-tip stresses attract ions from its vicinity and results in crack tip enrichment. Many semi-analytic simulations, currently available in the literature, are based on the radial approximation of the concentration field (Bhandakkar and Gao, 2010; Woodford et al., 2010) (i.e., $c=c(r)$) which is calculated for an un-cracked particle. We study the crack-tip enrichment further in the Appendix A where in a simple setting we identify an enrichment length scale where its ratio to Griffith length scale, scales as the ratio of maximum misfit stresses to the chemical energy squared (see (A.9)).

With the propagation mechanism elucidated, we now turn our attention to obtaining design parameters for these particles. Fig. 7 shows a combined diagram for results of our simulations for $R/l_G=4.2\times10^4$ particles containing initial flaws of different sizes. In this phase diagram, the circles mark activated cracks and cross marks depict those not activated at a given charging rate $C_r$. As expected, longer radial cracks need lower charging rate to activate, but very long initial flaws do not propagate since the hoop stresses around the crack tip never grow large enough. We duplicated the simulations for a larger $R/l_G=2\times10^5$ particle in Fig. 8.

We can make three important observations from Figs. 7 and 8; First the simulations show that there exists a safe charging rate $C_{r,\min}\simeq2,1$ for $r/l_G=4.2\times10^4,2\times10^5$ particles respectively where flaws regardless of their size do not propagate. Secondly, for moderate dimensionless charging rates $C_r=O(1)$ ($t_D\sim t_C$), the minimum flaw size activated $a_{0,\min}$ decreases as the inverse of the dimensionless charging rate squared i.e., $a_{0,\min}\sim C_r^{-2}$. Thirdly, in Figs. 7 and 8, there exists a minimum flaw size $a_{0,\min}^\infty$ that flaws smaller, regardless of the dimensionless charging rate do not propagate.

The inverse square law can be understood by noting that the at moderate fluxes the concentration needs to penetrate at the particle length scale before there is enough energy for the flaw to activate (see Figs. 2-4). It is worth noting that the propagation at these critical fluxes is always abrupt only for smaller initial notches as detailed previously in this section (see Fig. 6). Therefore the time to activate an initial flaw is similar to the diffusion time of ions in particle size $t_0\sim t_D=R^2/D$. Using the mass conservation, we can write that the mass accumulated in the particle is equal to the mass of the ions inserted through its surface i.e., $R^2\Delta c\sim R\hat{J}t_0\sim R^3\hat{J}/D$. Rearranging the terms, we find the characteristic variation of Li ion's

![](./images/812744289514684418_9.jpg)

Fig. 9. Flaw activation diagram for circular particles with $a_0/R=0.1$ initial flaw. Circles show the activated vs. crosses show the unactivated cracks. The gray dashed line shows the scaling law $R=0.1 \hat{J}^{-2/3}$.

concentration across the particle scales as $\Delta c \sim \hat{J}R/D$. This variation generates maximum hoop stress $\sigma_{\theta\theta} \sim E\beta\Delta c/c_{\text{max}}$ at the particle surface. According to the standard Griffith criterion, this stress can activate a flaw of size $a_{0,\text{min}} \sim G_c E/\sigma_{\theta\theta}^2$. Combing the above expressions for $\sigma_{\theta\theta}$, $\Delta c$, $t_D$, $t_C$, and using (25) we obtain the prediction

$$
a_{0,\text{min}} \sim l_G (\beta C_r)^{-2}. \tag{26}
$$

In other words, the ratio of flaw size to the Griffith length-scale $a_{0,\text{min}}/l_G$, scales as the inverse square of dimensionless charging rate times the maximum misfit strain i.e., $a_{0,\text{min}}/l_G = A(\beta C_r)^{-2}$ where $A$ is a dimensionless numerical prefactor obtained from a numerical fit of this scaling law to the phase-field simulation results. We can now identify the "misfit length scale"

$$
l_c = \frac{l_G}{\beta^2} \tag{27}
$$

which takes into account that the magnitude of maximum misfit stresses generated $E\beta$ is the appropriate measure of stresses in diffusion driven fracture. We should highlight that similar length scale was also used in Bourdin et al. (2014) for the study of thermally driven cracks.

Using our phase-field simulations presented in Figs. 7 and 8 we can identify the scaling constants for the two particle sizes as $A=35.93, 26.62$ for $R/l_G=4.2 \times 10^4, 2 \times 10^4$ particles respectively. Perhaps not surprisingly, since Eq. (26) has many simplifications and does not encode all particle size dependencies. Most notably it ignores the effect of the relative initial flaw size compared to the particle radius $a_0/R$, where changing the relative size of the initial flaw will change the evolution of the concentration field for the moderate charging rates considered. Furthermore, (26) also ignores the effects of the crack tip enrichment. As alluded to before, tensile stresses at the tip attract concentration, this introduces another length scale (see (A.9)) into the system that, in principle, can introduce dependency on the particle radius. Therefore, the scaling constant in the case of two different particle sizes are different. With the scaling constants extracted from the phase-field simulations we can carry the analysis further and obtain the maximum safe charging rate for a given particle size. For these practical charging rates, we can rewrite the maximum safe $C_{r,\text{max}}$ below which no flaws can be activated in a particle of radius $R$ as

$$
C_{r,\text{max}} = \frac{1}{t_{c,\text{min}}} = \frac{D_0}{R^2} \left( \frac{A l_c}{a_{0,\text{min}}} \right)^{1/2} \tag{28}
$$

where $D_0$ is the diffusivity of Li ions in the cathode. This scaling law predicts the most conservative charging rate (minimum charging time $t_C$) in terms of basic material properties.

Furthermore, to demonstrate the particle size dependency, it is easy to rearrange the power-law in Eq. (26) for a given dimensionless flaw size $\bar{a}_0 = a_0/R$ as $R \sim \hat{J}^{-2/3}$. Fig. 9 depicts such a power-law emerging from the combined results of a series of simulations for particles of different size with a $a_0/R=0.1$ initial radial flaw on their surface. A similar power- law was independently derived by Bhandakkar and Gao (2010) for initiation of a periodic array of cracks in a thin film using a cohesive zone model. There, authors study the initiation of an array of equidistant cracks such that the maximum stress in the system is equal to the cohesive strength of the material under study. They then, given the fracture energy of the material, investigate whether the displacement opening for the potentially initiated cracks will exceed the critical displacement required to maintain them. They find that regardless of the cohesive strength of the material, there exists a critical film thickness $H_c \sim \hat{J}^{-2/3}$ below which no fracture is initiated in the thin film.

Following our third observation, we see that the minimum flaw size activated $a_{0,\text{min}}$ for small initial flaws deviates from the scaling law (26) and approaches a constant value $a_{0,\text{min}}^\infty \simeq 10^3 l_G$ for both particle sizes. At very large $C_r$ required to activate these minimal flaws, the concentration reaches its minimum physically allowed value $c=0$ at the particle surface in

![](./images/812744289514684418_10.jpg)

Fig. 10. Numerical simulation results for a $R/l_G=10^5$ particle with $a_0/l_G=400$ initial flaw at first time step after its activation $t/t_D=0.011$ showing the concentration field penetrating at the scale of the initial flaw. Color codes depict the dimensionless hoop stress $\sigma_{\theta\theta}/c_{\max}\mathcal{R}T$ distribution (left), and the dimensionless concentration distribution $c/c_{\max}$ perturbed as the result of the crack-tip stress field (right) with inlays showing area near the initial flaw magnified.

![](./images/812744289514684418_11.jpg)

Fig. 11. Flaw activation diagram for circular particles with Dirichlet boundary conditions: results for the dimensionless particle size $R/l_G=2\times10^3$–$4\times10^5$ vs the dimensionless initial flaw size $a_0/l_G=10^2$–$1.6\times10^3$. Circles show the activated vs. crosses show the unactivated cracks.

a time $t_0 \ll t_D$. In the next Section 4.2, we study the limit $C_r \to \infty$ where $t_0/t_D \to 0$ by imposing the potentiostatic (Dirichlet) boundary condition $c=0$ at the particle surface.

### 4.2. Chemo-mechanical fracture of circular particles: (II) potentiostatic (dirichlet) boundary condition

As discussed before for large fluxes $C_r \to \infty$, the concentration field reaches its minimum $c=0$ at time $t_0 \ll t_C$ as a result of which a depleted boundary layer is created on the surface of the particle. Therefore, it is more convenient to study this limit using Dirichlet boundary conditions. In this section, we present the results of numerical simulation for fracture of circular particles using $c(R)=0$, $t \in [0, t_{\max}]$ Dirichlet boundary condition that is analogous to the maximum flux attainable for this system. Using this boundary condition, we can find the minimum flaw size activated for different particle radii. Similar to the previous section, we chose phase field length scale $\xi$ such that the initial flaw is well resolved (i.e., $a_0/\xi \geq 4$).

Fig. 10 shows the activation of a $a_0/l_G=400$ radial flaw in a $R/l_G=10^5$ particle under Dirichlet boundary conditions. Unlike the simulations analyzed in the previous section, the initial flaw is activated at $t_a \ll t_D$ in these simulations. We observe that the fracture propagation stems from the creation of an ion-depleted boundary layer of thickness $h \sim \sqrt{D_0 t_a}$ with a size comparable to the minimum flaw size $a_0$ but much smaller than the particle radius i.e., $h \ll R$.

Fig. 11 shows the combined results of these numerical simulations for six particle sizes with different initial flaw sizes where we can make two observations. Firstly, our numerical results show that for our choice of parameters, there exists a maximum safe particle size $R_{\max} \simeq 10^4 l_G$ that no flaw would propagate in it. Simply put, since the minimum activated flaw size decreases with the particle size, it becomes comparable to the particle size for small particles which cannot produce high enough deriving forces to propagate them. This size is analogous to critical thickness derived in Huggins and Nix (2000) for a simple 1D bilayer. Secondly, we notice that as a function of growing particle radius $R \to \infty$, the smallest

![](./images/812744289514684418_12.jpg)

Fig. 12. Numerical simulation results for a $R/l_{G}=2\times 10^{4}$ particle showing the fracture topology (iso-surface visualization for $\phi=0.5$) after initial abrupt activation (see also Fig. 17). (a) $a_{0}/l_{G}=2\times 10^{3}$ radial penny-shaped crack under $C_{r}=21$ at $t/t_{C}=0.5$. (b) $a_{0}/l_{G}=2\times 10^{3}$ radial penny-shaped crack under $C_{r}=30$ at $t/t_{C}=0.28$. (c) $a_{0}/l_{G}=1.5\times 10^{3}$ radial penny-shaped crack under $C_{r}=30$ at $t/t_{C}=0.33$. (d) $a_{0}/l_{G}=1.5\times 10^{3}$ radial penny-shaped crack under $C_{r}=45$ at $t/t_{C}=0.22$. (e) $a_{0}/l_{G}=10^{3}$ radial penny-shaped crack under $C_{r}=36$ at $t/t_{C}=0.32$. (f) $a_{0}/l_{G}=10^{3}$ radial penny-shaped crack under $C_{r}=45$ at $t/t_{C}=0.26$.

flaw activated asymptotically approaches a constant value $a_{0,\min}^{\infty}/l_{G}\to 5\times 10^{4}$. Thus the smallest flaw activated for a large particle becomes independent of its radius. We can elucidate this observation noticing that in the absence of cracks, the maximum hoop stress generated under Dirichlet boundary conditions $\sigma \sim E\beta$ is independent of the particle radius. Therefore, analogous to a flaw on the boundary of a half-space, the flaw size scales $a_{0,\min}^{\infty}\sim G_{c}E/(\sigma)^{2}=l_{c}$ where the dimensionless prefactor is a function of the particle geometry. Also, we can relate our observations of minimum flaw size $a_{0,\min}$ at a given radius to results presented in the previous Section 4.1 for large fluxes $C_{r}\to \infty$. For example, for a $R/l_{G}=4.2\times 10^{4}$ particle presented in Fig. 7 the minimum flaw activated is predicted to be $a_{0}/l_{G}\simeq 4\times 10^{2}$ consistent with the results in Fig. 11.

### 4.3. Fracture of spherical cathodic particles with penny-shaped radial flaws

Although insight gained from the two-dimensional numerical simulations in the previous section is invaluable, only true 3D calculations can hope to capture all essential aspects of chemo-mechanical fracture in these particles. In this section, we demonstrate the similarities and differences between the simplified 2D and more realistic 3D simulations. Following the previous section, we model a spherical $R/l_{G}=2\times 10^{4}$ particle with a penny-shaped flaw on its surface (see 14). As already mentioned, in contrast to previous calculations in 3D (e.g., Klinsmann et al., 2016a; Klinsmann et al., 2016b), we simulate the complete sphere without explicit use of any symmetries. To this end, the elastic null-space (i.e., translation and rotational modes) was calculated and removed prior to the elastic sub-iteration in the alternate minimization algorithm (i.e., solving (22)). Since the computational cost of a uniform fine mesh was prohibitive, we chose a static adaptive meshing scheme, where for $r/l_{G}>1.6\times 10^{4}$ a fine mesh with an average edge length of $200l_{G}$ was generated and gradually coarsened to a coarse mesh with an average edge length of $500l_{G}$ for $r/l_{G}<1.2\times 10^{4}$. This meshing scheme, for different initial flaw sizes, resulted in the computational domain discretized into $\sim$13-25M tetrahedral elements (resulting overall in roughly the same number of degrees of freedom). These simulations were performed using 12 nodes each containing two 2.8GHz 10-Core Ivy Bridge-EP E5-2680 Xeon 64-bit Processors and 64Gb of RAM for an average time of 48 hours. Following the 2D simulations, we set the phase-field length scale to $\xi/R=3\times 10^{-2}$ and use the material properties as presented in Table 1. Moreover, due to the prohibitive cost of the 3D simulations, we limit our investigation to three flaw sizes $a_{0}/l_{G}=10^{3},1.5\times 10^{3},2\times 10^{3}$ and charging rates $15\leq C_{r}\leq 45$.

Fig. 12 shows the complex fracture topology that results from the activation of the penny-shaped flaw in 3D. The 3D fracture pattern highlights the role of dimensionality and follows from the fact that hoop stresses $(\sigma_{\theta\theta},\sigma_{\phi\phi})$ reach their

![](./images/812744289514684418_13.jpg)

Fig. 13. Evolution of dimensionless surface energy $\mathscr{F}_{\phi}/(G_{c}R^{2})$ for $R/l_{G}=2\times10^{4}$ spherical particle containing a $a_{0}/l_{G}=2\times10^{3}$ radial penny-shaped crack for $C_{r}=21$ and $C_{r}=30$. Associated topologies for different points in time is presented in Figs. 14-16.

![](./images/812744289514684418_14.jpg)

Fig. 14. Initial topology of the radial penny-shaped crack (iso-surface visualization for $\phi=0.5$) $a_{0}/l_{G}=2\times10^{3}$ in a $R/l_{G}=2\times10^{4}$ spherical particle (o in Fig. 13).

![](./images/812744289514684418_15.jpg)

Fig. 15. Evolution of high-flux fracture topology (iso-surface visualization for $\phi=0.5$) for $R/l_{G}=2\times10^{4}$ spherical particle containing an initial $a_{0}/l_{G}=2\times10^{3}$ radial penny-shaped crack under $C_{r}=21$: initial abrupt propagation a-1 at $t/t_{C}=0.5$ (left), a-2 $t/t_{C}=0.6$ (right) (see Figs. 13 and 17).

maximum values on the surface. Consequently, the tessellation of the particle surface by the crack releases the stresses and inhibits the inward propagation of the crack. These peripheral cracks only alleviate these stresses perpendicular to the crack surface, thereby causing new cracks to be initiated with different orientations than the plane of the initial penny-shaped crack. Therefore, we can hypothesize that for smaller charging rates where the opening stresses (Li ions) need to penetrate farther inside, the radial propagation is augmented compared to higher charging rates where the stresses generated are more superficial. This hypothesis is confirmed by the results of 3D simulations presented in Fig. 12. In that figure for all different initial flaw sizes simulated in 3D, crack propagation is abrupt and the added freedom for the cracks to release the stresses by tessellating the surface results in two dominant crack topologies: (I) cracks that propagate coplanar to the initial flaw under higher $C_{r}$ (b,d in Figs. 12-17), and (II) cracks with initial coplanar propagation that tip split and result in a more complex topology under lower $C_{r}$ (a,c,e,f in Figs. 12-17).

![](./images/812744289514684418_16.jpg)

Fig. 16. Evolution of low-flux fracture topology (iso-surface visualization for $\phi=0.5$) for $R/l_G=2\times10^4$ spherical particle containing an initial $a_0/l_G=$ $2\times10^3$ radial penny-shaped crack under $C_r=30$: initial abrupt propagation b-1 at $t/t_C=0.28$ (top left), b-2 $t/t_C=0.36$ (top right), b-3 $t/t_C=0.38$ (bottom left), b-4 $t/t_C=0.6$ (bottom right) (see Figs. 13 and 17).

![](./images/812744289514684418_17.jpg)

Fig. 17. Flaw activation diagram for a $R/l_G=2\times10^4$ radius spherical particle. Circles depict activated cracks with low-flux topology that split into multiple orientations and filled diamond depict activated cracks with high-flux topology that remain coplanar with the initial penny-shaped crack. Crosses show unactivated cracks. The gray dashed line shows the predicted power-law $a_0/l_G\sim C_r^{-2}$ relating minimum activated flaw size and dimensionless charging rate.

As explained before, we account for this transition using an argument similar to the one presented in Section 4.1 for abrupt versus continuous propagation in 2D. Unlike 2D radial cracks that can only release energy by penetrating towards the center of the particle, 3D penny-shaped cracks can both propagate radially and peripherally. The radial fracture in 3D simulations is akin to the radial propagation in 2D, *i.e.*, the bulk elastic energy is released due to the crack opening up in the back. On the other hand, the peripheral propagation is analogous to the creation of (mud) cracks in a biaxially stretched thin-films (León Baldelli et al., 2013; 2014) or formation of imperfect polygonal patterns due to thermal quenching (Bourdin et al., 2014). Therefore, since the highest opening stresses are always created on the surface of the particle, the initial propagation is always unstable in the peripheral direction. To clarify these two different fracture modes, we analyze two 3D topologies designated as cases **a** and **b** in Figs. 12-17. Due to the complex fracture topology in 3D, we use the dimensionless surface energy $\mathscr{F}_\phi/(G_c R^2)$ as a measure of the surface area of the cracks, noticing that following Eqs. (6) and (9):

$$
\frac{\mathscr{F}_\phi}{G_c R^2} \simeq \frac{\mathcal{H}^2(\Gamma)}{R^2} \tag{29}
$$

Fig. 13 depicts the dimensionless surface energy for $a_0/l_G=2\times10^3$ at two different dimensionless charging rates: $C_r=21$ (blue line in Fig. 13) and $C_r=30$ (red line in Fig. 13). Fig. 14 shows the initial penny-shaped crack of size $a_0/l_G=2\times10^3$ for cases **a-b**. Similar to the arguments presented for the 2D simulations at lower $C_r$ (cases **a,c,e,f** in Figs. 12-17 and those depicted using red circles in Fig. 17), the flaw is only activated when the concentration has penetrated on the scale of the particle size. As seen, for example, in **a-1** in Figs. 13 and 15, the propagation of the initial flaw is first planar which then

tip splits due to high biaxial stresses (due to the symmetry of the problem far from the initial flaw $\sigma_{\theta\theta} = \sigma_{\phi\phi}$). At higher $C_r$ (cases $\mathbf{b,d}$ in Figs. 12-17 and those shown using orange diamonds in Fig. 17) the initiation is faster and creates a coplanar crack with the initial flaw as seen, for example, in $\mathbf{b-1}$ in Figs. 13 and 16. Upon further Li ion depletion, a secondary pair of cracks are initiated perpendicular to the initial circumferential crack as depicted in $\mathbf{b-2-3}$ in Figs. 13 and 16. We should highlight that the radial penetration of the 3D penny-shaped crack is similar to radial propagation in 2D simulations. As a result, for case $\mathbf{a}$ at the lower $C_r=21$ after the initial activation the crack abruptly penetrates radial distance of $\simeq 12 \times 10^3 l_G$ compared to $\simeq 6 \times 10^3 l_G$ for the case $\mathbf{b}$ at the higher $C_r=30$.

Fig. 17 depicts the aggregate results of a series of 3D numerical simulations for a $R/l_G=2 \times 10^4$ particle for $a_0/l_G = 10^3, 1.5 \times 10^3, 2 \times 10^3$ initial penny-shaped radial flaws. Despite the major difference in crack propagation path (i.e., pen- etrating cracks in two-dimensional circular particles vs. surface cracks in the three-dimensional sphere), our 3D results suggest that critical flux to activate a surface flaw follows the inverse square power-law $a_{0,\min}\beta^2/l_G \sim C_r^{-2}$ for moderate charging rates as in the 2D simulations. This is not surprising since the same arguments presented in Section 4.1 to justify the power-law still applies for spherical particles exposed to moderate fluxes. Furthermore, the results in Fig. 17 also suggest that, like 2D simulations (see Figs. 3-4), the transition of the inverse square power-law occurs at $a_0/l_G \simeq 10^3$.

We also should note that the tiling of the sphere surface is of particular theoretical interest. The polygonal tiling and its number of defects is prescribed by Euler's celebrated theorem (Euler, 1758). In contrast, in many physical systems, the number of defects on the curved surface goes beyond the minimum number necessary and is assigned by the local ener- getic minima. Over the past decade, significant progress has been made in closely connected areas of crystal formation on spherical surfaces (Bausch et al., 2003; Irvine et al., 2010; Manoharan, 2015) and pattern formation as the result of buckling (Jiménez et al., 2016). Although the mechanism of surface tilings generated in this section is an attractive subject for further research, in this article, we limit ourselves to the general topology of the cracks generated.

## 5. Conclusions

In this article, we developed a thermodynamically consistent framework by combining the phase-field fracture method and diffusion to model chemo-mechanical fracture. We presented our formulation in Section 2 and detailed our implemen- tation of it in Section 3.

As our first case study, we investigated in Section 4.1 the fracture of 2D circular disks. Using different initial flaw sizes, we showed how the steep gradient created as a result of the charging rate could cause a surface flaw to propagate and fracture the particle. Our numerical results show that for a given particle size, there exists a maximum flaw independent charging rate that can be used as a conservative limit in practice. Furthermore, motivated by our simulation results, we showed how the activation of the surface flaws follows an inverse square law $a_{0,\min} \sim C_r^{-2}$ over intermediate dimensionless charging rates $C_r=O(1)$ ($t_D \sim t_C$). We justified this power-law behavior based on a Griffith type analysis of the stresses generated far from the crack-tip and showed how it could be used to calculate a maximum safe charging rate $C_{r,\text{max}}$ given the elastic and fracture properties as well as an estimate of the flaw sizes in the system. We should note that although the activation of surface flaws follows this simple power-law expression, the precise flux to activate a flaw is dictated by a non-trivial concentration profile around the crack-tip. Since the scaling law analysis ignores the ratio of flaw size to the radius of the particle, as well as the crack-tip enrichment, the scaling constant can only be derived from the numerical simulations, especially for small particles where the initial flaw size plays a more significant role. Furthermore, we showed that depending on the particle and flaw size, the initial propagation could be abrupt or continuous for low and high fluxes, respectively. While puzzling at first, we described how the abrupt fracture propagation length decreases for increasing fluxes for moderate initial flaw sizes due to smaller bulk energy available at the fracture onset.

We then extended our study to high fluxes that are necessary for the activation of very small flaws ($a_0 < 10^3 l_G$ for our choice of parameters). Our results show that for these small flaws, the safe charging rate deviates from the previously obtained scaling law. We explained our observation, noting that the high charging rate creates a depleted layer on the periphery of the particle and thus loses its effectiveness in creating a steep enough gradient to activate these flaws. As a result, we found out that there exists a minimum safe flaw size $a_{0,\min}$ for a given particle size that does not propagate under any charging rate. To effectively address these maximal charging rates, in Section 4.2, we examined the activation of surface flaws using potentiostatic (Dirichlet) boundary conditions. Our simulation results show that there exists a C-rate independent, safe particle size that no flaw of any size will propagate in it. In addition, they show that in large particles the minimum activated flaw size approaches a constant value (e.g., $a_{0,\min}^\infty \simeq 200l_G$ for our choice of parameters). In other words, our numerical simulations suggest that particles (no matter how large) containing flaws smaller than $a_{0,\min}^\infty$ do not crack due to diffusion-driven misfit stresses.

Finally, in Section 4.3, to investigate the role of dimensionality, we performed a series of 3D simulations on spheri- cal particles with penny-shaped flaws. Using our numerical observations, we showed that, unlike in 2D and assumptions (Woodford et al., 2010) and results (Klinsmann et al., 2016a) of previous studies, the crack topology changes from a coplanar penetrating mode to a surface tiling mode. These full (i.e., without any symmetries assumed) 3D calculations show that the initial mechanical mode of failure in three-dimensional particles during charging is due to the fracture on their sur- face. While all the propagations from the initial penny-shaped crack in 3D were abrupt, we showed how the change of the fracture topology could be explained using arguments akin to those used to justify the length of abrupt propagation in 2D.

Furthermore, our admittedly limited 3D results suggest that $a_{0,\text{min}} \sim c_r^{-2}$ scaling law is still valid in 3D for flaws larger than $a_0 > 10^3 l_G$.

Lastly, it is crucial to highlight that, in this article, we only model chemo-mechanical fracture due to Lithium diffusion with no phase change or discontinuity in expansion. As highlighted, for example, in Woodford et al. (2012, 2013), coherency stresses generated at the phase and grain boundaries can result in charging rate independent fracture in Li-storage materials.

## Acknowledgments
A.M. and A.K. acknowledge the support of Grant No. DE-FG02-07ER46400 from the U.S. Department of Energy, Office of Basic Energy Sciences. The majority of the numerical simulations were performed using resources of the Extreme Science and Engineering Discovery Environment (XSEDE) under the resource allocation TG-MSS160013. Additional numerical simulations were also performed on the Northeastern University Discovery cluster at the Massachusetts Green High Performance Computing Center (MGHPCC).

## Appendix A. Concentration enrichment around crack-tip due to mechanical loads
Examining Eqs. (14)-(15), it is easy to notice that the ions flow toward the regions with higher hydrostatic pressures; therefore, it is not surprising that in the presence of a crack, a higher concentration will accumulate at the crack-tip (see Fig. A.18). More specifically, for small eigen-strains (i.e., $\beta \ll 1$) the stresses become independent of the concentration field (i.e., the diffusion equation would be driven by the magnitude of hydrostatic stress).

To derive the enrichment at the crack-tip, we can rewrite the coupled equations of elasticity and concentration in terms of Airy stress function $\mathcal{A}$ in 2-D:
$$
\nabla^4 \mathcal{A} = -E^*\epsilon_0 \nabla^2 c \tag{A.1}
$$
where $E^* = \frac{E}{1 - \nu^2}$ for plane-stress. Therefore, for small eigen-strains i.e., $\beta \ll 1$ the stresses become independent of the concentration field (i.e., the diffusion equation would be driven by the magnitude of hydrostatic stress). Thus, for steady-state conditions and in absence of a surface flux, one can write
$$
J = -\nabla \frac{\delta F}{\delta c} = 0
$$
$$
\frac{\delta F}{\delta \overline{c}} = c_{\text{max}} \mathcal{R}T \ln\left(\frac{c}{c_{\text{max}} - c}\right) - c_{\text{max}} \epsilon_0 \text{Tr}(\sigma) = \mu_0 \tag{A.2}
$$
$$
c = \frac{c_{\text{max}}}{1 + \exp\left(-\frac{\beta \sigma_{kk} + \mu_0}{c_{\text{max}} \mathcal{R}T}\right)} \tag{A.3}
$$

A similar solution to (A.3) can be obtained for the dilute approximation where $f(c) = c \ln(c) - c$ as:
$$
c = c_{\text{max}} \exp\left(\frac{\beta \sigma_{kk} + \mu_0}{c_{\text{max}} \mathcal{R}T}\right) \tag{A.4}
$$

The above expression was also derived by the direct solution of the diffusion equation in Liu (1970).

To find the concentration profile around the crack-tip, we can replace the expression of $\text{Tr}(\sigma)$ from the asymptotic plane-stress solution of mode-I fracture:
$$
\sigma_{xx}(r, \theta) = \frac{K_I}{\sqrt{2\pi r}} \cos\left(\frac{\theta}{2}\right)\left[1 - \sin\left(\frac{\theta}{2}\right)\sin\left(\frac{3\theta}{2}\right)\right] + O(\sqrt{r}) \tag{A.5}
$$

![](./images/812744289514684418_18.jpg)

Fig. A1. Result of simulation for $R/l_G = 4.2 \times 10^4$ with a $a_0/l_G = 200$ initial crack, using $c_r = 22.75$ charging rate showing the enrichment at the crack tip at $t/t_c = 1.2$: concentration around crack tip (left) concentration map of the particle (right).

![](./images/812744289514684418_19.jpg)

Fig. A2. Comparison of relative concentration $c/c_{\text{max}}$ near crack-tip for $\beta=0.025$: numerical simulation using 2D simulations of circular geometry with asymptotic near crack-tip displacement boundary conditions (red circles), closed-form solution (A.8). (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

$$
\sigma_{y y}(r, \theta)=\frac{K_{I}}{\sqrt{2 \pi r}} \cos \left(\frac{\theta}{2}\right)\left[1+\sin \left(\frac{\theta}{2}\right) \sin \left(\frac{3 \theta}{2}\right)\right]+O(\sqrt{r}) \tag{A.6}
$$

where $K_{I}$ is the stress intensity factor. After some algebra $\operatorname{Tr}(\sigma)$ can be written as:

$$
\operatorname{Tr}(\sigma(r, \theta))=\frac{2 K_{I}}{\sqrt{2 \pi r}} \cos \left(\frac{\theta}{2}\right) \tag{A.7}
$$

where $K_{I}$ is the mode-I stress intensity factor. Using (A.7) we can write the concentration around the crack-tip at the time of fracture as:

$$
c=\frac{c_{\max }}{1+\exp \left(-\sqrt{\frac{2 r_{c}}{\pi r}}\left(\frac{K_{I}}{K_{I C}}\right) \cos \left(\frac{\theta}{2}\right)-\bar{\mu}_{0}\right)} \tag{A.8}
$$

where

$$
r_{c}=\left(\frac{\beta K_{I C}}{c_{\max } \mathcal{R} T}\right)^{2}=l_{G}\left(\frac{\beta \mathrm{E}}{c_{\max } \mathcal{R} T}\right)^{2} \tag{A.9}
$$

can be identified as the intrinsic length scale for the concentration of ions around the crack-tip. Eq. (A.9) shows that the ratio of the enrichment length scale to Griffith length scale scales as the square ratio of maximum misfit stresses to chemical energy. In (A.8) one can find the steady-state chemical potential $\mu_{0}$, from far field concentration as

$$
\mu_{0}=c_{\max } \mathcal{R} T \ln \left(c_{\infty} /\left(c_{\max }-c_{\infty}\right)\right) \tag{A.10}
$$

As we showed in the Section 4.1, crack-tip enrichment is a common occurrence in diffusion-driven fracture of Lithium-ion battery particles. We can easily calculate the length scale $r_{c} / l_{G} \simeq 7591.75$ for $\mathrm{LiMn}_{2} \mathrm{O}_{4}$ at room temperature where the crack-tip concentration is captured approximately by (A.8). Fig. A.19 shows a comparison between the results of the numerical simulation for a $R / l_{G}=4.2 \times 10^{4}$ particle (Fig. 2) and (A.8). The simulation is performed in a circular geometry of radius $R$ containing a sharp $1^{\circ}$ notch from $r=-150 \xi$ to $r=0$ at $\theta=\pi$. To simulate near tip stress fields, the displacement fields associated with (A.5)-(A.6) were imposed on the boundary of the domain. The concentration is initially uniform $c / c_{\max }=0.5$ everywhere and the value of $\mu_{0}$ was calculated based on the resulting concentration at $t / t_{D}=1$ and $r=R$.

We should note that the radial crack, driven by charging the cathodic particle, can stop propagating in the middle of the particle. In this situation the enrichment carried by the crack-tip can be shielded from the depleting flux by chemo-mechanical force exerted at the crack-tip. The remaining concentration then can change the dynamics of the charging process. Furthermore, while the main focus of this article is on the diffusion of Li-ions in battery particles, crack-tip enrichment can play an important role in other systems where diffusion and fracture happen concurrently such as corrosive cracks, crack-tip embrittlement, and fracture in poroelastic media (Bouklas et al., 2015; Song and Curtin, 2013).

### Supplementary material
Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.jmps.2019.103696

## References

Alessi, R., Marigo, J.-J., Maurini, C., Vidoli, S., 2017. Coupling damage and plasticity for a phase-field regularisation of brittle, cohesive and ductile fracture: one-dimensional examples. Int. J. Mech. Sci. Pages –

Alessi, R., Vidoli, S., De Lorenzis, L., 2018. A phenomenological approach to fatigue with a variational phase-field model: the one-dimensional case. Eng. Fract. Mech. 190, 53–73.

Ambati, M., Gerasimov, T., De Lorenzis, L., 2015. Phase-field modeling of ductile fracture. Comput. Mech. 55 (5), 1017–1040.

Bahr, H.-A., Balke, H., Kuna, M., Liesk, H., 1987. Fracture analysis of a single edge cracked strip under thermal shock. Theor. Appl. Fract. Mech. 8 (1), 33–39.

Balay, S., Abhyankar, S., Adams, M.F., Brown, J., Brune, P., Buschelman, K., Eijkhout, V., Gropp, W.D., Kaushik, D., Knepley, M.G., McInnes, L.C., Rupp, K., Smith, B.F., Zhang, H., 2014. PETSc users manual. Argonne National Laboratory Technical report anl-95/11 - revision 3.5.

Balay, S., Gropp, W.D., McInnes, L.C., Smith, B.F., 1997. Efficient management of parallelism in object oriented numerical software libraries. In: Arge, E., Bruaset, A.M., Langtangen, H.P. (Eds.), Modern Software Tools in Scientific Computing, pages 163–202. Birkhäuser Press.

Bausch, A.R., Bowick, M.J., Cacciuto, A., Dinsmore, A.D., Hsu, M.F., Nelson, D.R., Nikolaides, M.G., Travesset, A., Weitz, D.A., 2003. Grain boundary scars and spherical crystallography. Science 299 (5613), 1716–1718. 03

Bhandakkar, T.K., Gao, H., 2010. Cohesive modeling of crack nucleation under diffusion induced stresses in a thin strip: implications on the critical size for flaw tolerant battery electrodes. Int. J. Solids Struct. 47 (10), 1424–1434.

Borden, M.J., Hughes, T.J.R., Landis, C.M., Anvari, A., Lee, I.J., 2016. A phase-field formulation for fracture in ductile materials: finite deformation balance law derivation, plastic degradation, and stress triaxiality effects. Comput. Methods Appl. Mech. Eng 312, 130–166.

Bouklas, N., Landis, C.M., Huang, R., 2015. Effect of solvent diffusion on crack-tip fields and driving force for fracture of hydrogels. J. Appl. Mech. 82 (8), 081007.

Bourdin, B., Francfort, G.A., Marigo, J.J., 2008. The variational approach to fracture. J. Elast. 91 (1), 5–148.

Bourdin, B., Marigo, J.-J., Maurini, C., Sicsic, P., 2014. Morphogenesis and propagation of complex cracks induced by thermal shocks. Phys. Rev. Lett. 112, 014301.

Carrara, P., Ambati, M., Alessi, R., De Lorenzis, L., 2018. A novel framework to model the fatigue behavior of brittle materials based on a variational phase-field approach. arXiv:1811.02244.

Chakraborty, A., Ramakrishnan, N., 2013. Prediction of electronic conductivity of a degrading electrode material using finite element method. Comput. Mater. Sci 69, 455–465. 3

Chen, C.-H., Bouchbinder, E., Karma, A., 2017. Instability in dynamic fracture and the failure of the classical theory of cracks. Nat. Phys. Advance online publication:-,. 08

Chen, C.-H., Cambonie, T., Lazarus, V., Nicoli, M., Pons, A.J., Karma, A., 2015. Crack front segmentation and facet coarsening in mixed-mode fracture. Phys. Rev. Lett. 115, 265503.

Christensen, J., 2010. Modeling diffusion-induced stress in Li-ion cells with porous electrodes. J. Electrochem. Soc. 157 (3), A366–A380.

Christensen, J., Newman, J., 2006. A mathematical model of stress generation and fracture in lithium manganese oxide. J. Electrochem. Soc. 153 (6), A1019–A1030.

Deshpande, R., Verbrugge, M., Cheng, Y.-T., Wang, J., Liu, P., 2012. Battery cycle life prediction with coupled chemical degradation and fatigue mechanics. J. Electrochem. Soc. 159 (10), A1730–A1738. 01

Doyle, M., Fuller, T.F., Newman, J., 1993. Modeling of galvanostatic charge and discharge of the lithium/polymer/insertion cell. J. Electrochem. Soc. 140 (6), 1526–1533. 06

Euler, L., 1758. Demonstratio nonnullarum insignium proprietatum quibus solida hedris planis inclusa sunt praedita. Novi. Comm. Acad. Sci. Imp. Petrol 4, 140–160.

Francfort, G.A., Marigo, J.J., 1998. Revisiting brittle fracture as an energy minimization problem. J. Mech. Phys. Solid. 46 (8), 1319–1342.

Gabrisch, H., Wilcox, J., Doeff, M.M., 2008. Tem study of fracturing in spherical and plate-like lifepo4 particles. Electrochem. Solid-State Lett. 11 (3), A25–A29. 03

Haftbaradaran, H., Qu, J., 2014. A path-independent integral for fracture of solids under combined electrochemical and mechanical loadings. J. Mech. Phys. Solid. 71, 1–14.

Hakim, V., Karma, A., 2009. Laws of crack motion and phase-field models of fracture. J. Mech. Phys. Solid. 57 (2), 342–368. 2

Huggins, R.A., Nix, W.D., 2000. Decrepitation model for capacity loss during cycling of alloys in rechargeable electrochemical systems. Ionics 6 (1), 57–63.

Irvine, W.T.M., Vitelli, V., Chaikin, P.M., 2010. Pleats in crystals on curved surfaces. Nature 468 (7326), 947–951. 12

Jiménez, F.L., Stoop, N., Lagrange, R., Dunkel, J., Reis, P.M., 2016. Curvature-controlled defect localization in elastic surface crystals. Phys. Rev. Lett. 116 (10), 104301.

Karma, A., Kessler, D.A., Levine, H., 2001. Phase-field model of mode III dynamic fracture. Phys. Rev. Lett. 87, 045501.

Kirk, B.S., Peterson, J.W., Stogner, R.H., Carey, G.F., 2006. Libmesh: a c++ library for parallel adaptive mesh refinement/coarsening simulations. Eng. Comput. 22 (3–4), 237–254.

Klinsmann, M., Rosato, D., Kamlah, M., McMeeking, R.M., 2016. Modeling crack growth during Li extraction in storage particles using a fracture phase field approach. J. Electrochem. Soc. 163 (2), A102–A118. 01

Klinsmann, M., Rosato, D., Kamlah, M., McMeeking, R.M., 2016. Modeling crack growth during Li insertion in storage particles using a fracture phase field approach. J. Mech. Phys. Solid. 92, 313–344. 7

Lawn, B.R., 1993. Fracture of Brittle Solids. Cambridge University Press.

Lawrence, J.E., 1966. Diffusion-induced stress and lattice disorders in silicon. J. Electrochem. Soc. 113 (8), 819–824.

León Baldelli, A.A., Babadjian, J.-F.-F., Bourdin, B., Henao, D., Maurini, C., 2014. A variational model for fracture and debonding of thin films under in-plane loadings. J. Mech. Phys. Solids 70 (0), 320–348. 10

León Baldelli, A.A., Bourdin, B., Marigo, J.-J., Maurini, C., 2013. Fracture and debonding of a thin film on a stiff substrate: analytical and numerical solutions of a one-dimensional variational model. Continuum. Mech. Thermodyn. 25 (2), 243–268.

Liu, H.W., 1970. Stress-corrosion cracking and the interaction between crack-tip stress field and solute atoms. J. Basic Eng. 92 (3), 633–638. 09

Lubomirsky, Y., Chen, C.-H., Karma, A., Bouchbinder, E., 2018. Universality and stability phase diagram of two-dimensional brittle fracture. Phys. Rev. Lett. 121 (13), 134301.

Manoharan, V.N., 2015. Colloidal matter: packing, geometry, and entropy. Science 349 (6251).

McKinnon, W.R., Haering, R.R., 1983. Physical Mechanisms of Intercalation, pages 235–304. Springer US, Boston, MA.

Mesgarnejad, A., Bourdin, B., Khonsari, M.M., 2013. A variational approach to the fracture of brittle thin films subject to out-of-plane loading. J. Mech. Phys. solid. 61 (11), 2360–2379.

Mesgarnejad, A., Imanian, A., Karma, A., 2019. Phase-field models for fatigue crack growth. Theor. Appl. Fract. Mec. 102282.

Miehe, C., Dal, H., Raina, A., Raina, A., 2015. A phase field model for chemo-mechanical induced fracture in lithium-ion battery electrode particles. Int. J. Numer. Method. Eng. Pages n/a–n/a

Miehe, C., Welschinger, F., Hofacker, M., 2010. A phase field model of electromechanical fracture. J. Mech. Phys. Solids 58 (10), 1716–1740. 10

Mozaffari, N., Voyiadjis, G.Z., 2015. Phase field based nonlocal anisotropic damage mechanics model. Phys. D 308, 11–25. 7

Peco, C., Liu, Y., Rhea, C., Dolbow, J.E., 2019. Models and simulations of surfactant-driven fracture in particle rafts. Int. J. Solid. Struct. 156–157, 194–209.

Peled, E., 1979. The electrochemical behavior of alkali and alkaline earth metals in nonaqueous battery systems—the solid electrolyte interphase model. J. Electrochem. Soc. 126 (12), 2047–2051.

Pham, K., Marigo, J.J., 2012. Damage localization and rupture with gradient damage models. Fract. Struct. Integrr. 19.

Pham, K., Marigo, J.J., 2013. From the onset of damage to rupture: construction of responses with damage localization for a general class of gradient damage models. Continuum. Mech. Thermodyn. 1-25.

Prussin, S., 1961. Generation and distribution of dislocations by solute diffusion. J. Appl. Phys. 32 (10), 1876-1881.

Singh, G.K., Ceder, G., Bazant, M.Z., 2008. Intercalation dynamics in rechargeable battery materials: general theory and phase-transformation waves in lifepo4. Electrochim. Acta 53 (26), 7599-7613.

Song, J., Curtin, W.A., 2013. Atomic mechanism and prediction of hydrogen embrittlement in iron. Nat. Mater 12 (2), 145-151. 02

Thackeray, M.M., Johnson, P.J., de Picciotto, L.A., Bruce, P.G., Goodenough, J.B., 1984. Electrochemical extraction of lithium from limn2o4. Mater. Res. Bull. 19 (2), 179-187.

Wang, J.W., He, Y., Fan, F., Liu, X.H., Xia, S., Liu, Y., Harris, C.T., Li, H., Huang, J.Y., Mao, S.X., Ting, Z., 2013. Two-phase electrochemical lithiation in amorphous silicon. Nano. Lett. 13 (2), 709-715.

Wang, Y.H., He, Y., Xiao, R.J., Li, H., Aifantis, K.E., Huang, X.J., 2012. Investigation of crack patterns and cyclic performance of ti-si nanocomposite thin film anodes for lithium ion batteries. J. Power Sources 202, 236-245. 3

Woodford, W.H., Carter, W.C., Chiang, Y.-M., 2012. Design criteria for electrochemical shock resistant battery electrodes. Energy Environ. Sci. 5 (7), 8014-8024.

Woodford, W.H., Chiang, Y.-M., Carter, W.C., 2010. "Electrochemical shock" of intercalation electrodes: a fracture mechanics analysis. J. Electrochem. Soc. 157 (10), A1052-A1059.

Woodford, W.H., Chiang, Y.-M., Carter, W.C., 2013. Electrochemical shock in ion-intercalation materials with limited solid-solubility. J. Electrochem. Soc. 160 (8), A1286-A1292. 01

Xu, R., Zhao, K., 2018. Corrosive fracture of electrodes in li-ion batteries. J. Mech. Phys. Solid. 121, 258-280.

Zavalis, T.G., Klett, M., Kjell, M.H., Behm, M., Lindström, R.W., Lindbergh, G., 2013. Aging in lithium-ion batteries: model and experimental investigation of harvested lifepo4 and mesocarbon microbead graphite electrodes. Electrochim. Acta 110 (11), 335-348.

Zhang, M., Qu, J., Rice, J.R., 2017. Path independent integrals in equilibrium electro-chemo-elasticity. J. Mech. Phys. Solid. 107, 525-541.

Zuo, P., Zhao, Y.P., 2015. A phase field model coupling lithium diffusion and stress evolution with crack propagation and application in lithium ion batteries. Phys. Chem. Chem. Phys. 17 (1), 287-297.